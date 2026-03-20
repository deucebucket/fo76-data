# Finding 061: Fallout 76 Map Coordinate System Fix

## Summary

The interactive map's coordinate conversion was completely wrong. The old formula used a game range of 262,144 units (64 cells), but the actual rendered map covers 577,536 units (141 cells). This caused markers to render at 2.2x incorrect scale -- locations near the center looked roughly OK, but anything far from origin (Watoga, Morgantown, Ohio) was wildly misplaced or off-screen entirely.

## Root Cause

The old `convert_data.py` used:
```python
GAME_MIN = -131072   # -32 cells
GAME_MAX = 131072    # +32 cells
GAME_RANGE = 262144  # 64 cells total
```

This is wrong. The `262144` value is only 64 cells, which covers a small subset of the Appalachia worldspace. The actual map image was rendered by fo76utils with a view scale of `0.0070922` (= 1/141), which covers 141 cells centered at the game origin.

## Correct Coordinate System

### fo76utils Render Parameters

The standard fo76utils render command for FO76 4K maps:
```
./render SeventySix.esm fo76_map_4k.dds 4096 4096 Fallout76/Data \
  -r -71 -71 71 71 \
  -view 0.0070922 180 0 0 0 0 4096
```

Key parameters:
- **Image size**: 4096x4096 pixels
- **View scale**: 0.0070922 = 1/141 pixels per game unit
- **Rotation**: RX=180 (top-down view, north up)
- **Offsets**: (0, 0, 4096) -- image center = game origin (0,0)
- **Cell range**: -71 to 71 (for terrain loading only; view bounds are set by scale)
- **OFFS_Z=4096**: camera height (irrelevant for 2D projection)

The `-r -100 -100 100 100` parameter (from SConstruct.maps) extends the terrain loading range to include Ohio/Burning Springs but does NOT change the view bounds.

### View Scale Math

From the fo76utils documentation: "At a scale of 1.0, the size of one exterior cell is 4096 pixels."

- 1 cell = 4096 game units
- At scale 1.0: 1 game unit = 1 pixel
- At scale 0.0070922: 1 game unit = 0.0070922 pixels
- 1 cell = 0.0070922 * 4096 = 29.05 pixels
- Visible cells: 4096 / 29.05 = 141 cells
- Game coordinate range: [-288,768 to +288,768] in both X and Y (141 * 4096 / 2)

### Correct Conversion Formula

```
pixel_x = game_x * (1/141) + 2048
pixel_y = -game_y * (1/141) + 2048
```

Equivalently:
```
pixel_x = (game_x + 288768) / 577536 * 4096
pixel_y = (288768 - game_y) / 577536 * 4096
```

Where:
- `288768 = 70.5 * 4096` (half the visible range)
- `577536 = 141 * 4096` (full visible range)
- Game +X = east = image right (pixel_x increases)
- Game +Y = north = image up (pixel_y decreases)

### Inverse Formula (pixel to game)

```
game_x = (pixel_x - 2048) * 141
game_y = -(pixel_y - 2048) * 141
```

## Calibration Verification

Using known MapMarker positions from the ESM:

| Location | Game X | Game Y | Pixel X | Pixel Y | Map Position |
|---|---|---|---|---|---|
| Whitespring North Entrance | 942 | -49,735 | 2054.7 | 2400.7 | Center, slightly SE -- correct |
| Watoga Underground | 152,463 | -141,432 | 3129.3 | 3051.1 | Far SE quadrant -- correct |
| Top of the World | 39,089 | 14,204 | 2325.2 | 1947.3 | Center-north -- correct |
| Morgantown Station | -28,920 | 100,932 | 1842.9 | 1332.2 | NW area -- correct |
| Watoga (main marker) | 145,432 | -138,880 | 3079.4 | 3033.0 | SE quadrant -- correct |
| Watoga Station | 149,827 | -150,058 | 3110.6 | 3112.3 | Far SE -- correct |

### Old Formula Comparison (showing the errors)

| Location | Old Pixel | New Pixel | Error (px) |
|---|---|---|---|
| Whitespring North | (2063, 2825) | (2055, 2401) | (-8, -424) |
| Watoga Underground | (4430, 4258) | (3129, 3051) | **(-1301, -1207) OFF SCREEN** |
| Top of the World | (2659, 1826) | (2325, 1947) | (-334, +121) |
| Morgantown Station | (1596, 471) | (1843, 1332) | (+247, +861) |

The old formula placed Watoga completely off-screen and shifted Morgantown 860 pixels from its correct position.

## Map Image Sources

### Terrain Render (what we use)

The `appalachia_color.png` is a 4096x4096 top-down terrain render from fo76utils. This includes ALL terrain including Ohio/Burning Springs, because the render loads cells -100 to 100.

**Pros:**
- Shows actual terrain detail (roads, buildings, water features)
- Includes Ohio/Burning Springs
- Matches ESM coordinate system exactly
- Used by Mappalachia and other data-driven tools

**Cons:**
- No stylized labels or region names
- Looks like a satellite image, not a "game map"

### In-Game Paper Map (papermap_city_d.dds)

The in-game paper map texture is the stylized map visible in the Pip-Boy.

**Pros:**
- Familiar to players
- Has region labels and stylization

**Cons:**
- Does NOT include Ohio/Burning Springs (DLC area)
- Coordinate mapping is different (artistic projection, not linear)
- Lower detail than terrain render

### What Community Tools Use

- **Mappalachia**: Uses a 4096x4096 fo76utils terrain render as the base map image. SpotlightScale=2 (game coords per pixel in tile calculations). Handles coordinate conversion through its Space class.
- **map76.com**: Uses a datamined terrain render with tile-based zoom.
- **fo76map.com / falloutbuilds.com**: Use terrain render base maps with leaflet.js, similar to our approach.
- **Nexus mod (TZMap)**: Uses the in-game paper map with manual calibration.

All major community mapping tools use the fo76utils terrain render for data-accurate mapping. The paper map is only used for in-game replacements (cosmetic mods).

## SConstruct.maps Reference

From `fo76utils/SConstruct.maps`, the FO76 entry:
```python
["fo76", "Fallout76/Data",
 "SeventySix.esm", "Terrain/Appalachia.btd", "0x0025DA15", "0",
 -100, -100, 100, 100, 125, "0x600C2028", "fo76"]
```

- World form ID: `0x0025DA15` (APPALACHIA)
- Cell range: -100 to 100 (201 cells per axis)
- Light level: 125
- Water color: `0x600C2028`
- Map icons type: "fo76"

The cell range -100 to 100 is for terrain data loading. The render examples use a view scale of 1/141, not 1/201, so 60 cells on each edge are loaded but extend beyond the visible image area.

## Files Changed

- `perkolatr/static/map/convert_data_fixed.py` -- New script with correct coordinate formula
- `perkolatr/static/map/index.html` -- Needs JS constants updated to match

## Technical Notes

- The fo76utils `markers` tool uses the same coordinate system as the render tool. When given a reference DDS image, it reads the image dimensions and uses the same scale/offset embedded in the DDS header (or specified explicitly via view transform parameters).
- The `bobblehead_markers.dds` and `highvalue_markers.dds` in `data/fallout76/map_data/` are 4096x4096 and use the same coordinate mapping as the terrain render.
- Interior cells (CELL records with small coordinates) are local to that cell and cannot be mapped to worldspace coordinates. Only WRLD records have absolute world coordinates.
- The game Y axis is flipped relative to image coordinates: game +Y = north = up on map = lower pixel row number.
