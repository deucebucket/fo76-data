# Finding 062: Tiled Map System for Fallout 76 Interactive Map

## Summary

Research and implementation plan for a Google Maps-style tiled map system using Leaflet.js with pre-rendered tiles from fo76utils. The current 4K image overlay hits a detail ceiling when zooming in -- buildings become pixel mush. A proper tile pyramid renders progressively higher-resolution images from the actual game data at each zoom level, giving building-level detail at zoom 6.

## Current System (Problems)

The existing map uses `L.imageOverlay()` with a single 4096x4096 JPEG (11MB). While tiles exist in `static/map/tiles/0-4/`, they are simply the 4K image sliced into 256x256 chunks. Zooming past level 4 just stretches pixels -- there is no additional detail.

**Why this is bad:**
- 11MB image loaded upfront, even on mobile
- No detail gain past ~zoom 3 (each tile is the same resolution)
- Maximum effective resolution: 4096px across ~577,000 game units = ~141 units/pixel
- At zoom 6, you'd want ~2 units/pixel to see individual buildings

## How Leaflet Tile Layers Work

### URL Pattern

```javascript
L.tileLayer('tiles/{z}/{x}/{y}.jpg', {
    minZoom: 0,
    maxZoom: 6,
    maxNativeZoom: 6,  // highest zoom with actual tiles
    tileSize: 256,
    noWrap: true
}).addTo(map);
```

At each zoom level `z`, the map is divided into `2^z x 2^z` tiles. Leaflet requests tiles by `{z}/{x}/{y}` where:
- `z` = zoom level (0 = whole world in 1 tile, 6 = 4096 tiles)
- `x` = column from left (0 to 2^z - 1)
- `y` = row from top (0 to 2^z - 1)

### CRS.Simple for Game Maps

For non-geographic maps, Leaflet provides `CRS.Simple` where 1 map unit = 1 pixel at zoom 0. Our map uses this with bounds mapped to game coordinates.

```javascript
var map = L.map('map', {
    crs: L.CRS.Simple,
    minZoom: 0,
    maxZoom: 6
});
```

**Critical detail:** In CRS.Simple, the tile grid origin (0,0) is at the top-left. The coordinate system is `[y, x]` (latitude = y, longitude = x), and latitude increases downward in tile space but upward in Leaflet's latLng.

### maxNativeZoom

If we don't want to render all zoom levels, `maxNativeZoom` tells Leaflet the highest zoom with actual tiles. Beyond that, it upscales the native tiles. For example, with `maxNativeZoom: 5` and `maxZoom: 7`, zooming to 6 or 7 scales up the zoom-5 tiles.

## fo76utils Render Tool

### How It Works

The `render` command generates a top-down DDS image from ESM + terrain data:

```bash
./render SeventySix.esm output.dds WIDTH HEIGHT /path/to/Data [OPTIONS]
```

### Key Parameters

| Parameter | Purpose |
|---|---|
| `-r X0 Y0 X1 Y1` | Cell range to LOAD (terrain data bounds) |
| `-view SCALE RX RY RZ OX OY OZ` | Transform from world coords to image coords |
| `-btd file.btd` | Terrain heightmap/texture data |
| `-rq INT` | Render quality flags (see below) |
| `-ssaa INT` | Supersampling (2^N), use 1 for 2x |
| `-ltxtres INT` | Land texture resolution per cell |
| `-xm STRING` | Exclude model patterns |
| `-light S RY RZ` | Lighting brightness and direction |
| `-lcolor ...` | Light color tuning |

### View Scale Math

From the docs: "At a scale of 1.0, the size of one exterior cell is 4096 pixels."

- 1 cell = 4096 game units
- Scale 1.0 = 1 pixel per game unit
- Scale S means each game unit = S pixels
- Visible width = image_width / S game units

For the standard FO76 map covering cells -71 to 71 (141 cells):
- Total game range: 141 * 4096 = 577,536 units
- For a 4096px image: scale = 4096 / 577536 = 0.0070922
- This is the scale used in the existing `appalachia_color.jpg`

### Render Quality Flags (-rq)

Sum these values:
- `1` = pre-combined meshes (scol)
- `2` = all object types (structures, trees, etc.)
- `3` = scol + all objects
- `4` = normal mapping
- `8` = PBR on objects
- `12` = PBR on everything
- `15` = all quality + all objects + scol (what examples use)

### Rendering Specific Regions

The `-view` parameter controls what area maps to the output image. To render a specific tile, we calculate the view offset and scale so that the desired game-coordinate region fills the output image.

For a tile at zoom `z`, column `x`, row `y` covering 256x256 pixels:
- The full map at zoom z has `2^z * 256` total pixels
- Each tile covers `1/2^z` of the full range
- The game range for this tile can be calculated from the tile coordinates

## Tile Generation Strategy

### Approach: Render Full Images Per Zoom, Then Slice

Rather than rendering each individual tile (which would be thousands of render invocations), we render one large image per zoom level and slice it with ImageMagick. This is what Mappalachia does -- fo76utils renders the background, then it gets processed.

**Why not render each tile individually?**
- fo76utils has significant startup cost (loading ESM, terrain, textures)
- At zoom 6, there would be 4096 individual renders
- Each render loads the same ESM and archive data
- Rendering one big image and slicing is 100x faster

### Zoom Level Plan

| Zoom | Tiles | Total px | Game units/px | Detail Level | Render Size | Est. Time |
|---|---|---|---|---|---|---|
| 0 | 1x1 | 256 | 2,256 | Icon only | Skip (downscale z2) | - |
| 1 | 2x2 | 512 | 1,128 | Region shapes | Skip (downscale z2) | - |
| 2 | 4x4 | 1024 | 564 | Road network | Render 1024px | ~30s |
| 3 | 8x8 | 2048 | 282 | Town outlines | Render 2048px | ~1min |
| 4 | 16x16 | 4096 | 141 | Current quality | Render 4096px (exists) | ~2min |
| 5 | 32x32 | 8192 | 70 | Building shapes | Render 8192px | ~8min |
| 6 | 64x64 | 16384 | 35 | Building detail | Render 16384px | ~30min |

**Storage per zoom level:**
- z0: 1 tile (~30KB)
- z1: 4 tiles (~120KB)
- z2: 16 tiles (~400KB)
- z3: 64 tiles (~1.2MB)
- z4: 256 tiles (~4MB)
- z5: 1024 tiles (~12MB)
- z6: 4096 tiles (~40MB)
- **Total: ~58MB** (JPEG quality 85)

### Render Commands Per Zoom Level

The standard FO76 render uses cells -71 to 71, covering the full Appalachia worldspace. Each zoom level just changes the image resolution (and thus the view scale).

Base formula: `scale = image_size / (141 * 4096)`

| Zoom | Image Size | View Scale | Command |
|---|---|---|---|
| 2 | 1024 | 0.001773 | `-view 0.001773 180 0 0 0 0 1024` |
| 3 | 2048 | 0.003546 | `-view 0.003546 180 0 0 0 0 2048` |
| 4 | 4096 | 0.007092 | `-view 0.007092 180 0 0 0 0 4096` |
| 5 | 8192 | 0.014184 | `-view 0.014184 180 0 0 0 0 8192` |
| 6 | 16384 | 0.028369 | `-view 0.028369 180 0 0 0 0 16384` |

### Quality Settings Per Zoom

Lower zoom levels don't need high quality since detail is invisible:

| Zoom | -rq | -ssaa | -ltxtres | Notes |
|---|---|---|---|---|
| 2-3 | 3 | 0 | 128 | Terrain + basic objects, no AA |
| 4 | 15 | 0 | 256 | Full quality, no AA |
| 5 | 15 | 0 | 512 | Full quality, land textures |
| 6 | 15 | 1 | 512 | Full quality + 2x AA |

### Slicing with ImageMagick

After rendering each zoom level's full image to DDS, convert to PNG and slice:

```bash
# Convert DDS to PNG
magick input.dds input.png

# Slice into 256x256 tiles with directory structure
magick input.png -crop 256x256 -set filename:tile "%[fx:page.x/256]_%[fx:page.y/256]" tiles/%[filename:tile].png

# Or use a Python script for proper z/x/y directory creation
```

ImageMagick's crop with tile naming is somewhat unwieldy for creating the `z/x/y.jpg` directory structure. A Python script using PIL/Pillow is cleaner.

## Leaflet Integration

### Replacing imageOverlay with tileLayer

Current code:
```javascript
L.imageOverlay('appalachia_color.jpg', imageBounds).addTo(map);
```

New code:
```javascript
L.tileLayer('tiles/{z}/{x}/{y}.jpg', {
    minZoom: 0,
    maxZoom: 6,
    maxNativeZoom: 6,
    tileSize: 256,
    noWrap: true,
    bounds: imageBounds,
    errorTileUrl: 'tiles/blank.jpg'  // transparent tile for out-of-bounds
}).addTo(map);
```

### Coordinate Mapping

The current system maps game coordinates to a 4096x4096 pixel space. With tiles, we need to ensure the coordinate conversion still works. The key relationship:

- At zoom 0: the full map is 256x256 pixels (1 tile)
- At zoom 4: the full map is 4096x4096 pixels (current resolution)
- The CRS.Simple coordinate system uses pixels at zoom 0 as the base unit

In CRS.Simple, Leaflet uses `latLng` where:
- `lat` (y-axis) increases upward
- `lng` (x-axis) increases rightward
- At zoom 0, 1 unit = 1 pixel

So our map bounds in CRS.Simple at zoom 0 would be:
- SW corner: `L.latLng(0, 0)` or `L.latLng(-256, 0)`
- NE corner: `L.latLng(256, 256)` or `L.latLng(0, 256)`

The standard approach for a 256x256 base tile:

```javascript
var mapSize = 256;  // pixels at zoom 0
var bounds = [[0, 0], [mapSize, mapSize]];

var map = L.map('map', {
    crs: L.CRS.Simple,
    minZoom: 0,
    maxZoom: 6,
    maxBounds: [[-20, -20], [mapSize + 20, mapSize + 20]]
});

// Game coordinate conversion
var GAME_RANGE = 577536;  // 141 cells * 4096 units/cell
function gameToLatLng(gx, gy) {
    var px = (gx + GAME_RANGE/2) / GAME_RANGE * mapSize;
    var py = (GAME_RANGE/2 - gy) / GAME_RANGE * mapSize;
    return L.latLng(mapSize - py, px);  // flip y for latLng
}
```

## How Mappalachia Does It

Mappalachia uses fo76utils to render background images but does NOT use a tile layer. It renders the full world at a single resolution and uses it as a static background behind SVG-overlaid data points. The Mappalachia desktop app (C#/.NET) uses a single image, not web map tiles.

However, Mappalachia's rendering pipeline in `SConstruct.maps` shows the standard fo76utils parameters for FO76:
- Cell range: `-100 -100 100 100` (extends beyond 71 to include Ohio/Burning Springs)
- World ID: `0x0025DA15` (APPALACHIA)
- BTD file: `Terrain/Appalachia.btd`
- Default texture: `0` (none for FO76)
- Uses `terrain` + `landtxt` tools rather than `render` for its pipeline

The `render` examples in fo76utils docs show the direct approach:
```bash
./render .../SeventySix.esm fo76_map_4k.dds 4096 4096 .../Data \
    -r -71 -71 71 71 \
    -light 1.7 70.5288 135 \
    -lcolor 1 0xFFFCF0 0.875 -1 -1 \
    -ltxtres 512 -rq 15 -ssaa 1 \
    -xm swamptree \
    -view 0.0070922 180 0 0 0 0 4096
```

## Alternative: Render One Big Image + gdal2tiles

An alternative approach is to render a single maximum-resolution image (16384x16384 or even 32768x32768) and use gdal2tiles or Python to create the tile pyramid. This is simpler but:

**Pros:**
- Single render invocation
- gdal2tiles handles all the slicing automatically
- Proven workflow used by thousands of projects

**Cons:**
- 16K render takes ~30 min, 32K would take hours
- DDS output at 32K = ~3GB file (RGB24)
- May exceed GPU memory for texture cache at very high res
- Cannot tune render quality per zoom level

**For our use case:** The "render per zoom + slice" approach is better because we can tune quality per zoom level, and the intermediate DDS files can be deleted after slicing.

## VRAM / Memory Considerations

fo76utils render memory usage scales with output resolution:
- 4096x4096 at RGB24 = 48MB framebuffer (trivial)
- 8192x8192 at RGB24 = 192MB framebuffer
- 16384x16384 at RGB24 = 768MB framebuffer
- With `-ssaa 1` (2x), framebuffer quadruples

The RTX 3090 has 24GB VRAM. The texture cache (`-tc`) defaults to 1024MB. Total usage at 16K with ssaa:
- Framebuffer: ~3GB
- Texture cache: 1GB
- Model cache: varies
- **Should fit comfortably in 24GB**

## Implementation Plan

1. Write `generate_tiles.sh` script that:
   - Renders DDS images at zoom levels 2-6 using fo76utils
   - Converts DDS to PNG using ImageMagick
   - Slices each PNG into 256x256 tiles using Python/PIL
   - Creates `tiles/{z}/{x}/{y}.jpg` directory structure
   - Downscales zoom 2 render to create zoom 0 and 1

2. Update `index.html` to use `L.tileLayer` instead of `L.imageOverlay`

3. Test coordinate accuracy with known MapMarker positions

## File Locations

- Tile generator: `perkolatr/static/map/generate_tiles.sh`
- Tile slicer: `perkolatr/static/map/slice_tiles.py` (called by generate_tiles.sh)
- Tile output: `perkolatr/static/map/tiles/{z}/{x}/{y}.jpg`
- fo76utils render: `~/ai-drive/gamecryptids/tools/fo76utils/render`
- ESM: `~/.steam/steam/steamapps/common/Fallout76/Data/SeventySix.esm`
- BTD: `~/.steam/steam/steamapps/common/Fallout76/Data/Terrain/Appalachia.btd`
