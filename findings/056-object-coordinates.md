# Finding 056: Extracting X,Y,Z World Coordinates for Every Placed Object in FO76

## Summary

**Yes, we can extract X,Y,Z world coordinates for every placed object in the game.** The ESM contains 5,105,349 placed reference (REFR) records, each with full position and rotation data. The `esmdump` tool from fo76utils extracts these in both verbose and TSV formats.

## Method

### Command to Extract All REFR Records with Coordinates

```bash
cd ~/ai-drive/gamecryptids/tools/fo76utils

# Full dump - all 5.1M placed references (723MB output)
./esmdump \
  /path/to/SeventySix.esm \
  /path/to/Fallout76/Data \
  -i REFR -t -F fo76refr.txt -edid -n \
  -o output.tsv

# Verbose mode (shows subrecord structure, good for debugging)
./esmdump \
  /path/to/SeventySix.esm \
  /path/to/Fallout76/Data \
  -i REFR -v -n 2>&1 | head -100
```

### Field Definition File (fo76refr.txt)

Created at `~/ai-drive/gamecryptids/tools/fo76utils/fo76refr.txt`:

```
REFR	NAME	Base Object	d
REFR	DATA	Position/Rotation	ffffff
REFR	XSCL	Scale	f
REFR	XLYR	Layer	d
REFR	XESP	Enable Parent	d*
REFR	XTEL	Teleport	d*
REFR	XPRM	Primitive	fff*
```

### Key Flags

- `-t` = TSV output format
- `-F fo76refr.txt` = custom field definitions to parse DATA subrecord
- `-edid` = resolve form IDs to editor IDs (shows names like "LPI_Loot_Bobbleheads")
- `-n` = suppress statistics
- `-i REFR` = include only placed reference records

### DATA Subrecord Format

Each REFR's DATA subrecord contains 6 floats:
- **X, Y, Z** = world position (game units; 1 unit ~ 1.4cm)
- **RotX, RotY, RotZ** = rotation in radians

### TSV Output Format

```
Group	Record	FormID	EDID	FULL	DESC	RNAM	[BaseObj]	[Layer]	[Scale]	X	Y	Z	RotX	RotY	RotZ
```

**Caveat:** The XSCL (scale) and XLYR (layer) columns shift the coordinate columns when present. The verbose mode (`-v`) is more reliable for parsing individual records.

### WRLD vs CELL

- `WRLD` prefix = exterior worldspace (Appalachia overworld) -- coordinates are absolute world coordinates
- `CELL` prefix = interior cell -- coordinates are local to that cell

## Specific Object Findings

### BreakableRockWallGate (0x0012262A) and Variants

Base records exist as MSTT (moveable static) type:
- `0x0012262A` - BreakableRockWallGate
- `0x00122629` - BreakableRockWallFrame01
- `0x00152C30` - BreakableRockWallFrame02
- `0x00123DA4` - BreakableRockWallFrameDeco
- `0x001CA8F8` - BreakableRockWallSlump
- `0x00152C2E` - BreakableRockWallGateExit

**Result: ZERO placed REFR records found for any BreakableRockWall variant.** These objects are never directly placed in the worldspace. They are likely spawned dynamically by quest scripts or are components of static collections (SCOL records) that get decomposed at runtime. The explosion records `ExplosionBreakableRockWallGate01` (0x00123DA6) and `ExplosionBreakableRockWallGate01ForceBreak` (0x00125DB9) confirm these are scripted destructible objects.

### TrapBreakableBoard01-05

Base form IDs:
- `0x001184C6` - TrapBreakableBoard01
- `0x001184CF` - TrapBreakableBoard02
- `0x001184D0` - TrapBreakableBoard03
- `0x001184D2` - TrapBreakableBoard04
- `0x001184D4` - TrapBreakableBoard05

**Result: ~50 placed references found.** Locations include:
- Kerwood Mine interior (5 boards)
- Pitt DLC Trench area (5 boards)
- Multiple exterior worldspace locations
- Various interior cells

Sample coordinates (exterior worldspace):
| FormID | Base | X | Y | Z |
|--------|------|---|---|---|
| 0x00009EEF | TrapBreakableBoard03 | 24139.9 | 12075.9 | 6172.1 |
| 0x00009EEE | TrapBreakableBoard01 | 24156.7 | 12100.7 | 6168.2 |
| 0x00009EED | TrapBreakableBoard03 | 24145.6 | 12125.5 | 6168.2 |

### Burn_Drivein Destructibles

**Burn_Drivein_DesructablepSlatsWall (0x007FD760):**
- 1 placed reference: FormID 0x007FD7D7
- Position: X=-200008.0, Y=112096.0, Z=5584.0
- Layer: Burn_06_Drivein_Bathroom_Int_Clutter (0x0083651D)

**Burn_Drivein_DesructableWlpWall (0x007F4A3B):**
- 1 placed reference: FormID 0x007FD7D8
- Position: X=-200016.0, Y=112104.0, Z=5584.0
- Layer: Burn_06_Drivein_Bathroom_Int_Shell (0x00836520)

Both are in the same location -- the drive-in bathroom interior -- placed 8 units apart (the slats wall overlays the wallpaper wall).

## High-Value Item Dumps

All data saved to `~/ai-drive/gamecryptids/data/fallout76/map_data/`:

| File | Count | Description |
|------|-------|-------------|
| all_refr.tsv | 5,105,349 | Every placed object in the game (723MB) |
| bobbleheads.tsv | 1,102 | Bobblehead spawn points (737 base game + 328 Babylon + 37 DLC) |
| magazines.tsv | 1,972 | Magazine/skill book spawn points |
| power_armor.tsv | 838 | Power armor workbenches and related objects |
| breakable_walls.tsv | 3,010 | All breakable/destructible walls and barriers |
| cap_stashes.tsv | 339 | Cap stash containers (tin, standard, medium, high, jackpot) |
| fusion_cores.tsv | 289 | Fusion core spawn points |
| treasure_maps.tsv | 142 | Treasure map item placements |
| rare_nuka_colas.tsv | 224 | Rare Nuka-Cola variants (Cherry, Quantum, etc.) |

### Breakdown by Location Type

| Category | Exterior (WRLD) | Interior (CELL) |
|----------|-----------------|-----------------|
| All refs | 3,527,856 | 1,577,492 |
| Bobbleheads | 663 | 439 |

## Markers Tool (Visual Maps)

The `markers` tool generates DDS overlay images showing object positions on a map.

### Usage

```bash
# With view transform (no terrain file needed)
./markers SeventySix.esm output.dds "4096,4096,0.0625,0,0,0,0,0,0" markers.txt

# With terrain reference (needs fo4land heightmap)
./markers SeventySix.esm output.dds heightmap.dds markers.txt
```

### Marker Definition Format

Tab-separated: `FormID  FilterType  Color  MipLevel`
- FormID = base object form ID (NAME field of REFR)
- FilterType = -1 for any, or flags mask
- Color = 0xTARRGGBB (T=shape type, A=opacity)
  - Shape: 1=circle, 5=square, 9=diamond
  - Edges: 0=soft, 1=outline, 2=hard, 3=filled outline
- MipLevel = 0.0=full size, 2.0=quarter size

### Generated Maps

- `bobblehead_markers.dds` - Bobblehead spawn locations (green dots)
- `highvalue_markers.dds` - Multi-category overlay (bobbleheads=green, caps=yellow, fusion=cyan, breakable=red, PA=magenta)

## Coordinate System Notes

- Game uses Bethesda's Creation Engine coordinate system
- 1 game unit = ~1.4 centimeters
- Exterior coordinates are absolute world position
- Interior coordinates are relative to cell origin
- To convert to map pixels: multiply by view scale (0.0625 for 4096px map)
- The map center is approximately (0, 0) in world coordinates

## Key Insight: Interior vs Exterior Coordinates

Interior CELL coordinates are **local to the cell** and cannot be directly plotted on the overworld map. To map interior objects to world locations, you would need to:
1. Find the parent CELL record
2. Look up its worldspace position (if it has a door/teleport marker linking to the exterior)
3. Use the door's exterior position as the map pin location

## Tools & Files

- esmdump: `~/ai-drive/gamecryptids/tools/fo76utils/esmdump`
- markers: `~/ai-drive/gamecryptids/tools/fo76utils/markers`
- Field defs: `~/ai-drive/gamecryptids/tools/fo76utils/fo76refr.txt`
- Marker defs: `~/ai-drive/gamecryptids/data/fallout76/map_data/highvalue_markers.txt`
- ESM: `/home/deucebucket/.steam/steam/steamapps/common/Fallout76/Data/SeventySix.esm`
- Output data: `~/ai-drive/gamecryptids/data/fallout76/map_data/`
