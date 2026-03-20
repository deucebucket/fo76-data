# Finding 052: Fallout 76 World Map Reconstruction from ESM Data

## Summary

Complete extraction of Appalachia's world map data from the SeventySix.esm dump, covering every named location, region, fast travel point, workshop, vault, fissure site, and DLC expansion zone. The ESM contains **1,917 LCTN (location) records**, **461 REGN (region) records**, **470 named world references**, and **654 named interior cells** across the main APPALACHIA worldspace (FormID `0x0025DA15`).

## Data Sources

- `full_esm_dump.txt` (53MB) -- LCTN, REGN, and REFR record data
- `WRLD_records.txt` (3.6MB) -- Worldspace cells and placed references
- `CELL_records.txt` (632KB) -- Interior cell definitions
- `KYWD_records.txt` -- Location type classification keywords
- `seventysix_strings_en.txt`, `seventysix_ilstrings_en.txt`, `seventysix_dlstrings_en.txt` -- String tables for name resolution
- `disabled_zzz_records.txt` -- Cut/disabled content

## Methodology

Location classification is driven by keyword (KWDA) assignments on LCTN records. Key classification keywords:

| Keyword FormID | Classification | Count |
|---|---|---|
| `0x0033FE91` | LocTypeFastTravelDestination | 539 locations |
| `0x000234F1` | LocTypeWorkshop | 30 locations |
| `0x003AEDF7` | LocTypeWorkshopPublic | (subset of above) |
| `0x00396B77` | LocTypeDungeon | 254 locations |
| `0x000254BC` | LocTypeDungeonMajor | (subset) |
| `0x003DA753` | LocTypeMissileSilo | 7 locations |
| `0x00064EDE` | LocTypeClearable | (many) |
| `0x003D4B10` | HasMapMarker | 194 locations |
| `0x003A5E72` | NukeTarget | 38 locations |
| `0x0055C693` | CaveEntrance | 28 locations |
| `0x00417729` | VaultSystem | (vaults) |

Region keywords map locations to biomes:

| Keyword | Region | Location Count |
|---|---|---|
| `0x0001564F` | The Forest (ForestFloodlands) | 179 |
| `0x001789F7` | Savage Divide (Mountain) | 185 |
| `0x0001CA8C` | The Mire (SwampForest) | 76 |
| `0x000012A1` | Cranberry Bog | 74 |
| `0x0001CA8B` | Ash Heap (MTR) | 58 |
| `0x00088AAB` | Toxic Valley | 49 |
| `0x006923E7` | Skyline Valley (Storm DLC) | 65 |
| `0x007AE59D` | Burning Springs (Ohio DLC) | 64 |
| `0x006AFE11` | Atlantic City (AC DLC) | 12 |
| `0x0062D325` | The Pitt (Expedition) | 8 |
| `0x003B3731` | Whitespring | 5 |

---

## 1. Region Boundaries

### Main Game Regions (9 confirmed)

The WRLD file contains explicit region map marker references placed in the Appalachia worldspace:

| FormID | Editor ID | Display Name |
|---|---|---|
| `0x00869989` | RegionMapMarkerTheForest | The Forest |
| `0x0086998A` | RegionMapMarkerAshHeap | Ash Heap |
| `0x0086998B` | RegionMapMarkerBurningSprings | Burning Springs |
| `0x0086998C` | RegionMapMarkerCranberryBog | Cranberry Bog |
| `0x0086998D` | RegionMapMarkerMire | The Mire |
| `0x0086998E` | RegionMapMarkerToxicValley | Toxic Valley |
| `0x0086998F` | RegionMapMarkerSkylineValley | Skyline Valley |
| `0x00869990` | RegionMapMarkerSavageDivide1 | Savage Divide (north) |
| `0x00869991` | RegionMapMarkerSavageDivide2 | Savage Divide (south) |

**Note:** The Savage Divide has TWO region markers, confirming it spans such a large area it needs two label positions on the map.

### REGN Records Defining Boundaries

The ESM contains 461 REGN records. Key gameplay-significant regions:

**Main biome sub-regions (111 total):**
- Mountain (Savage Divide) sub-regions: MountainSubRegion01-34
- Cranberry Bog sub-regions: CranberrySubRegion01+
- Swamp (Mire) sub-regions: SwampSubRegion01-12
- Toxic Valley sub-regions: (managed by keyword)
- Forest sub-regions: (managed by keyword)

**Burning Springs / Ohio (85 REGN records):**
- `0x0079B5D8` BurningSpringsRegion -- master boundary
- BurningSpringsSubRegion01-20 -- internal sub-zones
- BurningSpringsBorderRegion01-08 -- edge transition zones
- BurnObjectRegion01-20 (x3 variants each: Default, Rocky, DenseForest/RustKingdom/LightForest)
- `0x00853ADA` BurningSpringsHighwayTownNukeExclusionRegion
- `0x00854EA1` BurningSpringsCheckpointRegion
- `0x00842D5C` BurningSpringsWeatherRegion

**Skyline Valley / Storm (28 REGN records):**
- `0x006923E9` StormRegion -- master boundary
- StormSubRegion01-18 -- internal sub-zones
- StormObjectRegion_Forest01-02, Corrupted01-02, Mountains01, Swamp01
- `0x00726986` StormWeatherRegion_Corrupted
- `0x006FCB10` StormWeatherRegion_DeadZone

**Workshop Regions (60 total):**
Each public workshop has a dedicated REGN defining its claim area:

| FormID | Workshop Region |
|---|---|
| `0x003879E8` | WorkshopAlleghenyAsylum |
| `0x00381299` | WorkshopPOI_01 through WorkshopPOI_16 |
| `0x00379F0A` | WorkshopPOI_24_n30_Region |
| `0x0036BAD0` | WorkshopPOI_7_41_Region |
| `0x0034C79C` | WorkshopToxicLake |
| `0x0033F8B6` | WorkshopHornwrightEstate |
| `0x007F2119` | BurningSpringsDriveinWorkshopRegion |

**Special Zones:**
- `0x002C613F` NonNukableZone -- prevents nuclear strikes
- `0x003B8AC9` Vault76Region -- Vault 76 starting area
- `0x003BE549` PrickettFortRegion
- `0x003A8DC7` LakeBedRegion
- `0x0072FCE9` DefaultWorkshopWeatherRegion

---

## 2. Fast Travel Network (539 Destinations)

All locations with keyword `0x0033FE91` (LocTypeFastTravelDestination). Organized by region:

### The Forest (122 fast travel points)

Aaronholt Homestead, Alpine River Cabins, Anchor Farm, Arktos Pharma, AVR Medical Center, Big Al's Tattoo Parlor, Billings Homestead, Black Mountain Ordnance Works, Bleeding Kate's Grindhouse, Blue Ridge Encampment, Bolton Greens, Camp Adams, Camp Adams Lookout, Camp McClintock, Charleston (x5 sub-locations), Charleston Capitol Building, Charleston Fire Department, Charleston Landfill, Charleston Station, Charleston Trainyard, Clancy Manor, Cow Spots Creamery, Crater Forest Outpost, Darling Sister's Lab, Deathclaw Island, East Kanawha Lookout, Enclave Extermination Site Alpha, Fissure Site (x3), Flatwoods, Flatwoods Lookout, Forward Station Tango, Foundation Outpost, Gauley Mine (x2), Gilman Lumber Mill, Gorge Junkyard, Green Country Lodge, Greg's Mine Supply, Groves Family Cabin, Helvetia, Hillfolk Hotdogs, Horizon's Rest, Hornwright Industrial Headquarters, Hornwright Summer Villa, Hunter's Ridge, Isolated Cabin, Kanawha County Cemetery, Kanawha Nuka-Cola Plant, Lady Janet's Soft Serve, Lakeside Cabins, Landview Lighthouse, Lewis & Sons Farming Supply, Mama Dolce's Food Processing, Marigold Pavilion, Moonshiner's Shack, Morgantown, Morgantown Airport, Morgantown High School, Morgantown Station, Morgantown Trainyard, New Gad, New River Gorge Bridge, New River Gorge Resort, North Kanawha Lookout, Ohio River Adventures, Organ Cave, Organ Cave South (x3), Orwell Orchards, Overlook Cabin, Overseer's Camp, Overseer's Home, Point Pleasant, Portside Pub, Poseidon Energy Plant WV-06 (x3), Poseidon Energy Plant Yard, Poseidon Power Substation PX-01, Poseidon Power Substation PX-02, Relay Tower EM-B1-27, Relay Tower HN-B1-12, Riverside Manor, RobCo Experimental Auto-Supply Cache #0001, Silva Homestead, Slocum's Joe, Sugarmaple, Summersville, Summersville Dam, Summersville Docks, Sunshine Meadows Industrial Farm, Sutton, Sutton Station, The Crosshair, The Deep (x2), The Fishermans Rest, The Giant Teapot, The Kill Box, Torrance House, Transmission Station 1AT-U03, Twin Pine Cabins, Tygart Water Treatment, Tyler County Dirt Track, Tyler County Fairgrounds, Vault 76, Vault-Tec Agricultural Research Center, Vault-Tec University, Vulcan Research Laboratory, WV Lumber Co., Wade Airport, White Powder Winter Sports, Widow's Perch, Wilson Brother's Auto Repair, Wixon Homestead

### Savage Divide (118 fast travel points)

98 NAR Regional, A Cave, Ammo Dump, Autumn Acre Cabin, Bailey Family Cabin, Bastion Park, Beckwith Farm, Big Bend Tunnel West, Big Fred's BBQ Shack, Blackwater Mine, Central Mountain Lookout, Cliffwatch, Colonel Kelley Monument, Converted Munitions Factory, Dent & Sons Construction, Devil's Backbone, East Mountain Lookout, Emmett Mountain Disposal Site, Federal Disposal Field HZ-21, Fissure Site (x4), Fort Atlas, Foundation, Foundation Outpost, Garrahan Mining Headquarters, Ghoul Camp (x3), Ghoul Cave, Hopewell Cave, Hornwright Estate, Huntersville, Investigator's Cabin, Johnson's Acre, Lake Eloise, Lucky Hole Mine, Metal Dome, Middle Mountain Pitstop, Miners Monument, Missile Silo Alpha (x2), Missile Silo Bravo (x2), Missile Silo Charlie (x2), Monongah, Monongah Mine, Monongah Overlook, Monongah Power Plant, Monongah Power Plant Yard, Monongah Power Substation MZ-01/02/03, Monorail Elevator, Mountainside Bed & Breakfast (x2), Mysterious Cave, National Isolated Radio Array, National Radio Research Center, New Appalachian Central Trainyard, North Cutthroat Camp, North Mountain Lookout, Palace of the Winding Path, Pleasant Valley Cabins, Pleasant Valley Ski Resort, Pleasant Valley Station, Point Repose (x2), Poseidon Power Substation PX-03, Pumpkin House, R & G Processing Services, R&G Station, Red Rocket Mega Stop, Relay Tower DP-B5-21, Relay Tower EL-B1-02, Relay Tower LW-B1-22, Ripper Alley, Safe 'n Clean Disposal, Scenic Overlook, Seneca Gang Camp, Seneca Rocks, Seneca Rocks Visitor Center, Skullbone Vantage, Solomon's Pond, Sons of Dane Compound, South Cutthroat Camp, South Mountain Lookout, Spruce Knob Campground, Spruce Knob Channels, Spruce Knob Lake, Sugar Grove, Sunnytop Ski Lanes, Sunnytop Ski Lanes Base Lodge, Sunnytop Station, Sylvie & Sons Logging Camp, The Bounty, The Bullengrube, The Freak Show, The Rose Room (x2), The Sludge Hole, The Vantage, The Whitespring, The Whitespring Station, Top of the World, Toxic Larry's Meat 'n Go, Twin Lakes, US-13C Bivouac, Uncanny Caverns, Vault 79 (x2), Vault 96, Wendigo Cave, West Tek Research Center, Whitespring Lookout, Yellow Sandy's Still

### Cranberry Bog (58 fast travel points)

AMS Corporate Headquarters (x2), Abandoned Bog Town (x2), Appalachian Antiques, Big Bend Tunnel East, Bootlegger's Shack, Creekside Sundew Grove, Crimson Prospect, Drop Site C2/G3/V9, Dueling Farms, Firebase Hancock/LT/Major, Fissure Site (x2), Fissure Site Prime, Flooded Trainyard, Fort Defiance (x2), Forward Station Alpha/Delta, Glassed Cavern (x2), Kerwood Mine, Lost Home, Mac's Farm, NAR Repair Yard, Old Mold Quarry, Overgrown Sundew Grove, Pylon V-13, Quarry X3, Ranger District Office, Ranger Lookout, RobCo Research Center, Sacramental Glade, Sparse Sundew Grove, Sunrise Field, Superior Sunset Farm, Survey Camp Alpha, The General's Steakhouse, The Thorn, Thunder Mountain Substation TM-02, Veiled Sundew Grove, Watoga, Watoga Civic Center (x2), Watoga Emergency Services, Watoga Estates, Watoga High School (x2), Watoga Municipal Center (x2), Watoga Shopping Plaza, Watoga Station, Watoga Transit Hub, Watoga Underground

### The Mire (55 fast travel points)

Abandoned Bunker, Abbie's Bunker, Berkeley Springs (x2), Berkeley Springs Station, Big B's Rest Stop, Big Maw, Blakes Offering, Bloody Frank's, Braxson's Quality Medical Supplies, Carson Family Bunker, Crashed Plane, Crevasse Dam, Dabney Homestead, Dagger's Den, Delano Grange, Dolly Sods Campground, Dolly Sods Lookout, Dolly Sods Wilderness, Dyer Chemical, East Ridge Lookout, Ella Ames' Bunker, Excelsior Model Home, Fisherman's Rest, Fissure Site, Freddy Fear's House of Scares, Gnarled Shallows, Gulper Lagoon, Harpers Ferry, Harpers Ferry Tunnel, Haven Church, Highland Marsh, Hunter's Shack, KMAX Transmission, Mire's Eye, Mosstown (x2), Moth-Home, Raider Cave 03, Raleigh Clay's Bunker, Ransacked Bunker (x2), Sacrament, Sam Blackwell's Bunker, Southern Belle Motel, Southhampton Estate, Sunday Brothers' Cabin, Tanagra Town, The Burrows, The Retreat, Thunder Mountain Power Plant, Thunder Mountain Substation TM-01, Thunder Mt. Power Plant Yard, Treetops, Valley Galleria, Vault 94

### Ash Heap (45 fast travel points)

AMS Testing Site, Abandoned Mine Shaft 1-6, Abandoned Mine Shaft Elaine, Abandoned Mine Site Kittery, Beckley, Beckley Mine Exhibit, Belching Betty, Brim Quarry, Camden Park, Fissure Site, Garrahan Estate, Hornwright Air Purifier Site #01-04, Hornwright Testing Site #01-04, Lake Reynolds, Lewisburg, Lewisburg Station, Mount Blair, Mount Blair Trainyard, Nicholson's End, Nuka-World On Tour, Pleasant Hills Cemetery, Pylon Ambush Site, Red Rocket Filling Station, Relay Tower HG-B7-09, Rollins Labor Camp, Sal's Grinders, Striker Row, The Burning Mine (x2), The Rusty Pick, The Sludge Works, Unfinished Mansion, Welch, Welch Station

### Toxic Valley (33 fast travel points)

Becker Farm, Black Bear Lodge, Carleton Mine, Clarksburg, Clarksburg Shooting Club, Cobbleton Farm, Crater Watchstation, Eastern Regional Penitentiary, Enclave Research Facility, Fissure Site, Grafton, Grafton Dam, Grafton Station, Grafton Steel, Grafton Steel Underground, Grafton Steel Yard, Graninger Farm, Hemlock Holes, Hemlock Holes Maintenance, Kiddie Corner Cabins, Knife Edge, Philippi Battlefield Cemetery, Pioneer Scout Camp, Pioneer Scout Lookout, Prickett's Fort, Smith Farm, Surly's Shack (x2), The Crater, Toxic Dried Lakebed, Wavy Willard's Water Park, Willard Corporate Housing, Woods Estate

### Skyline Valley (32 fast travel points)

Abandoned Convoy, Big Meadows Gas Well, Blue Ridge Shenandoah HQ, Camp Liberty, Crossroad, Dark Hollow Manor, Grindstone Arch, Hawksbill Weather Station, Hemlock Springs Dump, High Knob Lookout, Makeout Point, Milepost Zero, Naked Creek, Old Crimora Mines (x2), Old Rag Lookout, Park Ranger Radio Bunker, Rapidan Camp, Research Site Bavaria, Research Site Rhineland, Research Site Saxony, Shenandoah Visitor Center, Shining Creek Cavern, Skyline Drive Entrance, South River Bridge, Stony Man Lookout, Susan's Cabin, The Slumber Mill Motel, The Trading Post, Three Ponds, Treetop Lookout, Vault 63 Atrium

### Burning Springs / Ohio (31 fast travel points)

Abraxodyne Chemical Power Substation, Albany, Ash Cave, Athens Armory, Athens Ruins, Checkpoint Canyon, Cornhenge (x2), Dino Peaks Mini Golf, Fort Mitchell, Fort Steuben, Hamley Run Camp, Highway Town (x2), Hocking Hills Station, Honey Well Apiary, Jackson Junkyard, Meadow Breeze Storage Depot, Prospect Hill, Railroad Service Yard, Sand Fork Lumber, Sandy's Sock Hop, Shade Hill Church, Starlight Drive-in, Super Duper Mart, The Chop Shop, The Rust Kingdom, Tycoon Lake, Westbrook Horse Ranch, World of Corn (x2)

### Whitespring (5 fast travel points)

The Whitespring Bunker, The Whitespring Golf Club, The Whitespring Mall, The Whitespring Refuge, The Whitespring Resort

---

## 3. Map Marker Types

194 locations have the `HasMapMarker` keyword (`0x003D4B10`), indicating they appear as icons on the world map. These break down by marker icon type based on location keywords:

**Cities/Towns:** Morgantown, Charleston, Grafton, Welch, Lewisburg, Beckley, Watoga, Huntersville, Berkeley Springs, Clarksburg, Summersville, Monongah, Flatwoods, Sutton, Helvetia, Point Pleasant

**Military Installations:** Fort Defiance, Fort Atlas, Camp McClintock, Camp Venture, Camp Liberty, Sugar Grove, National Isolated Radio Array, National Radio Research Center, Converted Munitions Factory, Athens Armory

**Train Stations:** Morgantown Station, Sutton Station, Charleston Station, Grafton Station, Lewisburg Station, Welch Station, Pleasant Valley Station, Sunnytop Station, R&G Station, Berkeley Springs Station, Watoga Station, Hocking Hills Station

**Power Plants:** Poseidon Energy Plant WV-06, Monongah Power Plant, Thunder Mountain Power Plant (+ yards and substations)

**Caves:** Wendigo Cave, Glassed Cavern, Lucky Hole Mine, Uncanny Caverns, Ash Cave, Shining Creek Cavern, Hopewell Cave, Gauley Mine, Blackwater Mine, Old Crimora Mines

**Workshops:** (see Section 5)

**Vaults:** (see Section 7)

**Landmarks:** Top of the World, The Whitespring, Seneca Rocks, New River Gorge Bridge, Pumpkin House, Landview Lighthouse, Camden Park, Nuka-World On Tour

---

## 4. Fissure Site Locations (13 Total)

All fissure sites where Scorchbeasts emerge. Named with Greek alphabet designations in editor IDs:

| FormID | Editor ID | Region |
|---|---|---|
| `0x002D110F` | LocCranberryFissureSiteAlphaLocation | Cranberry Bog |
| `0x002D1110` | LocMountainsFissureSiteBetaLocation | Savage Divide |
| `0x003007B2` | LocMountainsFissureSiteGammaLocation | Savage Divide |
| `0x00097F97` | LocToxicFissureSiteDeltaLocation | Toxic Valley |
| `0x003A57E9` | LocCranberryFissureSiteEpsilonLocation | Cranberry Bog |
| `0x003A8CD8` | LocCranberryFissureSiteZetaLocation (**Prime**) | Cranberry Bog |
| `0x003A57F0` | LocForestFissureSiteThetaLocation | The Forest |
| `0x003A57EA` | LocForestFissureSiteKappaLocation | The Forest |
| `0x003A57EB` | LocForestFissureSiteLambdaLocation | The Forest |
| `0x003A57EC` | LocMTRFissureSiteOmegaLocation | Ash Heap |
| `0x003A57ED` | LocSwampFissureSiteOmicronLocation | The Mire |
| `0x003A57EE` | LocMountainsFissureSiteSigmaLocation | Savage Divide |
| `0x003A57EF` | LocMountainsFissureSiteTauLocation | Savage Divide |

**Fissure Site Prime** (`0x003A8CD8`, Zeta) in the Cranberry Bog is the Scorchbeast Queen encounter site and the primary nuke target in the game.

Distribution: Cranberry Bog (3), Savage Divide (4), The Forest (3), Ash Heap (1), Toxic Valley (1), The Mire (1).

---

## 5. Workshop Locations (22 Public Workshops)

Workshops with `LocTypeWorkshop` (`0x000234F1`) AND `LocTypeWorkshopPublic` (`0x003AEDF7`):

| FormID | Workshop Name | Region | Notable Resources |
|---|---|---|---|
| `0x00090629` | Sunshine Meadows Industrial Farm | The Forest | Food |
| `0x0008EDB3` | Lakeside Cabins | The Forest | Water |
| `0x00063DC7` | Gorge Junkyard | The Forest | Junk |
| `0x0010CCEA` | Charleston Landfill | The Forest | Junk |
| `0x002B9651` | Poseidon Energy Plant Yard | The Forest | Fusion Core |
| `0x002DE57D` | Tyler County Dirt Track | The Forest | -- |
| `0x0005D338` | Billings Homestead | The Forest | -- |
| `0x0010CCEF` | Wade Airport | The Forest | -- |
| `0x0009A3F1` | Sutton | The Forest | -- |
| `0x00438563` | Grafton Steel Yard | Toxic Valley | Steel |
| `0x0037D1D4` | Hemlock Holes Maintenance | Toxic Valley | -- |
| `0x003D4B17` | Monongah Power Plant Yard | Savage Divide | Fusion Core |
| `0x00115402` | Converted Munitions Factory | Savage Divide | Ammo |
| `0x0009A031` | Red Rocket Mega Stop | Savage Divide | -- |
| `0x00109D33` | Federal Disposal Field HZ-21 | Savage Divide | Nuclear |
| `0x00093BD1` | Mount Blair | Ash Heap | Mineral |
| `0x00004149` | Beckley Mine Exhibit | Ash Heap | -- |
| `0x00299948` | Berkeley Springs | The Mire | -- |
| `0x00109F43` | Dabney Homestead | The Mire | -- |
| `0x002DE581` | Dolly Sods Campground | The Mire | -- |
| `0x003D4B18` | Thunder Mt. Power Plant Yard | The Mire | Fusion Core |
| `0x003D69C3` | Abandoned Bog Town | Cranberry Bog | -- |
| `0x007ED7B0` | Starlight Drive-in | Burning Springs | -- |

**Note:** The Burning Springs DLC added the Starlight Drive-in as the newest workshop. Test/debug workshops (PVE Playground, Riverwood, TestWorkshopOrigin, etc.) exist in the data but are not accessible in gameplay.

---

## 6. Nuke Target Locations (38 Total)

Locations flagged with `NukeTarget` keyword (`0x003A5E72`) -- these can be specifically targeted by nuclear strikes:

All 3 Power Plant Yards (Poseidon, Monongah, Thunder Mt.) and their substations (PX-01/02/03, MZ-01/02/03, TM-01/02/03), Abandoned Bog Town, Beckley Mine Exhibit, Charleston, Clarksburg, Dabney Homestead, Deathclaw Island, Dolly Sods Campground, Federal Disposal Field HZ-21, Flatwoods, Green Country Lodge, Hemlock Holes Maintenance, Hopewell Cave, Morgantown, Pylon Ambush Site, Quarry X3, Sacramental Glade, Seneca Rocks Visitor Center, Solomon's Pond, Starlight Drive-in, Tanagra Town, The Freak Show, Treetops, Tycoon Lake, Tyler County Dirt Track, Arktos Pharma Biome Lab, Rust Kingdom Interior

---

## 7. Vault Locations

### Playable/Accessible Vaults

| Vault | FormID(s) | Region | Status |
|---|---|---|---|
| **Vault 76** | `0x000B1415` (ext), `0x00018BFE` (CharGen) | The Forest | Starting location, tutorial vault |
| **Vault 51** | `0x0060A6C1`, `0x005E9577` | The Forest | Nuclear Winter (cut), dungeon |
| **Vault 63** | `0x0012192A`, `0x007346A8`, `0x003241C2` | Skyline Valley | Skyline Valley DLC hub |
| **Vault 63 Atrium** | `0x006D7FBE` | Skyline Valley | Settlement (FastTravel + Settlement keyword) |
| **Vault 63 Organics Sector** | `0x006D8B27` | Skyline Valley | Dungeon/instanced |
| **Vault 63 Residential Sector** | `0x0072C017` | Skyline Valley | Instanced interior |
| **Vault 63 Engineering Sector** | `0x006CA3BE` | Skyline Valley | Region location |
| **Vault 79** | `0x00540390`, `0x005751A3` | Savage Divide | Wastelanders gold vault |
| **Vault 79 Entrance** | `0x0058D8C3` (Mysterious Cave) | Savage Divide | Exterior entrance |
| **Vault 94** | `0x005B7D8D`, `0x003F17CE`, `0x000AFBA5` | The Mire | Raid dungeon (Daily Ops) |
| **Vault 96** | `0x005E4844`, `0x000B1D42`, `0x0041F806` | Savage Divide | Dungeon (Daily Ops) |

### Cut/Unused Vaults (in ESM data)

| Cell | FormID | Editor ID | Notes |
|---|---|---|---|
| Vault 65 | `0x00002E22` | zCUTVault65 | Cut content |
| Vault 88 | `0x0011221B` | zCUTDLC06VaultWorkshop | Fallout 4 leftover |
| Vault 120 | `0x00004CCA`, `0x00004D4C`, `0x00004D4D` | zCUTUnusedVault120* | Multiple cut cells |
| Vault 120 Research | `0x00004CEE` | zCUTUnusedVault12004COPY0000 | Cut |
| Stellwagen Gorge | `0x00004CF4` | zCUTUnusedVault12003COPY0000 | Vault 120 variant |

### Vault Shelters (CAMP building items)

Vault Atrium Shelter (`0x005B1E4D`), Vault Living Quarters Shelter (`0x005B1E4E`), Vault Lobby Shelter (`0x005B5253`)

---

## 8. Burning Springs / Ohio Region

The newest DLC region. 85 REGN records define its boundaries:

**Master boundary:** `0x0079B5D8` BurningSpringsRegion

**20 sub-regions:** BurningSpringsSubRegion01 through 20 (`0x007D6A9F` - `0x007D6AB2`)

**8 border transition zones:** BurningSpringsBorderRegion01-08 (`0x007F74D3` - `0x007F74DA`)

**Special zones:**
- `0x00853ADA` BurningSpringsHighwayTownNukeExclusionRegion -- Highway Town is protected from nukes
- `0x00854EA1` BurningSpringsCheckpointRegion
- `0x00842D5C` BurningSpringsWeatherRegion
- `0x007F2119` BurningSpringsDriveinWorkshopRegion

**60+ environmental object regions:** BurnObjectRegion01-20 with variants (Default, Rocky, DenseForest, RustKingdom, LightForest) define terrain decoration distribution.

### Burning Springs Named Locations (31 with map markers)

| Name | FormID | Type |
|---|---|---|
| Highway Town | `0x007E8084` | Town hub |
| Athens Ruins | `0x007F9CE9` | City ruins |
| Athens Armory | `0x007F9CEA` | Military dungeon |
| The Rust Kingdom | `0x007D23FF` | Major dungeon (cave) |
| Fort Steuben | `0x007CA18C` | Major dungeon (cave) |
| Fort Mitchell | `0x007F67FA` | Major dungeon (cave) |
| Railroad Service Yard | `0x007D9F4E` | Major dungeon (cave) |
| The Chop Shop | `0x007D2A0E` | Clearable |
| Checkpoint Canyon | `0x007D0DDB` | Dungeon (cave) |
| Starlight Drive-in | `0x007ED7B0` | Workshop |
| Tycoon Lake | `0x0080BFF1` | Nuke target, large exterior |
| Super Duper Mart | `0x007CEA29` | Dungeon exterior |
| Dino Peaks Mini Golf | `0x007F1937` | Exterior dungeon |
| Hocking Hills Station | `0x007F74C0` | Train station |
| World of Corn | `0x007F67FB` | -- |
| Ash Cave | `0x007F6808` | Cave |
| Albany | `0x0084DB60` | Small POI |
| Cornhenge | `0x007F74C1` | -- |
| Honey Well Apiary | `0x0084DB5E` | Small POI |
| Westbrook Horse Ranch | `0x0084DB64` | Small POI |
| Sand Fork Lumber | `0x0084DB61` | Small POI |
| Sandy's Sock Hop | `0x0084DB5C` | Medium POI |
| Shade Hill Church | `0x0084DB5D` | Medium POI |
| Prospect Hill | `0x0084E8A5` | Small POI (UFO Watcher) |
| Hamley Run Camp | `0x0084DB5F` | Small POI |
| Abraxodyne Chemical Power Substation | `0x0084DB62` | Small POI |
| Meadow Breeze Storage Depot | `0x0084DB63` | Small POI |
| Jackson Junkyard | `0x007F03B9` | -- |
| Cobby's Corner | `0x0084DB65` | Small POI (playground) |

### Bounty Hunt System (Burning Springs)

The ESM contains 36 bounty target name overrides unique to Burning Springs, used by the bounty hunting system:
Freddy Adkin, Marvin Barber, Jim Britt, Willie Underwood, Francisco Dancisco, Annie Oakley, Billy John, Olga Lacy, Pauline Black, Ol Metal Leg, Matty Robbertson, Levi Acker, Holly Bow, Ashley Turnin, Barret Aimes, Cash Gold, Dallas Texas, Maxamilian Sea, Jonny Star, Gyro Zipp, Beau Pip, Pip Bort, Buster Clint, Clint Steel, Jesse Carson, Old Lady Pam, Old Man Breeches, Bella Knick, Alonzo Guard, Marcus Long, Granny Newark, Grandpa Oldworld, Francis Cage, Samuel Colt, Wes Smithson, Butch Springfield, Jimmy Smalls, Blaze Glory

---

## 9. Missile Silos

| Silo | Exterior FormID | Interior FormID | Cell Name | Region |
|---|---|---|---|---|
| **Alpha** | `0x0050FDF4` | `0x000921AE` | SugarGroveMissileSilo01 | Savage Divide |
| **Bravo** | `0x0051B059` | `0x00092213` | MonongahMissileSilo01 | Savage Divide |
| **Charlie** | `0x0051B05A` | `0x00092214` | SpruceKnobMissileSilo01 | Savage Divide |

A cut/old missile silo exists: `0x0044A6ED` CUT_OldMissileSiloLocation (Savage Divide).

---

## 10. Disabled/Cut Map Markers and Content

### Cut Location Records (zzz/zCUT prefix)

52 locations identified as cut/debug/test content. Notable finds:

| FormID | Name | Editor ID | Notes |
|---|---|---|---|
| `0x0084DB66` | World of Corn | zzzLocBurnCornhengeLocationCopy03 | Burned copy of Cornhenge |
| `0x007F74C1` | Cornhenge | zzzLocBurnCornhengeLocation_Copy02 | Multiple Cornhenge variants exist |
| `0x007F6807` | Cornhenge | zzzLocBurnCornhengeLocation_Copy01 | Another copy |
| `0x006371DD` | Chicken(?) | zzz_E09B_Wheel_BossName6 | Event boss name? |
| `0x0067A529` | Nuka Cola | zzz_E09B_Wheel_CombatTwistName4 | Event wheel content |
| `0x00690694` | RMTestMap | zzz_MOON_Herd_LOC | Moonshot herd event test |
| `0x007BE4A2` | zzzLocBurnDriveinWorkshopLocation | -- | Replaced workshop location |
| `0x007DF77D` | Rust Kingdom Arena TEST | BURN_SQ01_TestCellLocation | Test cell |

### Cut Interior Cells

| Cell FormID | Name | Editor ID |
|---|---|---|
| `0x005CAAA8` | Debug Shelters Test | zCUTDebugSheltersVaultTestMat01 |
| `0x00121929` | Vault 63 | zCUTVault63 (original, replaced) |
| `0x00044A50` | Vault 63 Entrance | zCUTVault63Entrance |
| `0x00003261` | Whitespring Bunker OLD | zCUTWhitespringBunkerOld |
| `0x00044CE9` | Charleston Capitol Building | zCUTCharlestonCapitolBuilding01 |
| `0x00006F40` | Huntersville Sewers | zCUTHuntersvilleSewers |
| `0x00530EBC` | Missile Silo Bravo | zCUTMonongahMissileSilo01OLD |
| `0x000242A2` | Quick Test Cell | zCUTMoleManCity01 |
| `0x00590369` | Clarksburg Pharmacy | zCUTClarksburgPharmacy01 |
| `0x003C2985` | Quick Test Cell | zCUT76TrailerInterior |
| `0x00208DF0` | Quick Test Cell | zCUTGraftonDam01 |
| `0x0000572C` | Quick Test Cell | zCUTBigFredsBBQShack01 |
| `0x005211F5` | Quick Test Cell | zCUTMissileSiloOLD |
| `0x003A62D0` | Quick Test Cell | zCUTOrion |
| `0x0040A89D` | New Hagerstown Greenhouse | zCUTMireBunker01 |

Notable: **Huntersville Sewers** (`zCUTHuntersvilleSewers`), **Mole Man City** (`zCUTMoleManCity01`), and **General Atomics Plant** (`zCUTGeneralAtomicsPlant01`) were planned interior spaces that were cut before release.

### Disabled Records File

The `disabled_zzz_records.txt` contains 8,535 disabled records across all types (not just locations), including cut workshop items, armor skins, keywords, and quest content.

---

## 11. Interior Cell Connections

654 named interior cells exist in the CELL records. Key interior-to-exterior connections based on editor ID naming patterns:

### Vault Interiors
- Vault 76: CharGen01-05, NVEVault7601, NPEVault7601
- Vault 51: Vault51Dungeon
- Vault 63: StormVault63AtriumUpper, StormVault63AtriumLower, StormVault63Entrance, Vault63Organics, StormEngineeringVlt63, StormWeatherLab01
- Vault 79: Vault79Entrance, Vault79Main, Vault79GoldVaultOperations
- Vault 94: Vault94Entrance, Vault94Dungeon, Vault94DungeonGECK
- Vault 96: Vault96Dungeon

### Major Dungeon Chains
- **West Tek:** WestTek01 (exterior) -> WestTek02 (FEV Production) -> WestTek02Arena (FEV Arena)
- **Glassed Cavern:** GlassedCavern01 -> GlassedCavernDungeon
- **Uncanny Caverns:** UncannyCaverns01 -> UncannyCaverns02 (Hidden Crevice)
- **Morgantown High:** MorgantownHighSchool01 -> MorgantownHighSchoolDungeon
- **Charleston Capitol:** CharlestonCapitolBuilding02 -> CharlestonCapitolDungeon -> CharlestonCapitolCourthouse01
- **Arktos Pharma:** ArktosPharmaLab01 -> ArktosPharmaLabDungeon
- **Watoga High:** WatogaHighSchool01 -> WatogaHighSchoolDungeon
- **Watoga Civic Center:** WatogaCivicCenter01 -> WatogaCivicCenterDungeon (Raider Arena)
- **Garrahan Mining HQ:** GarrahanMiningHQ01 -> GarrahanMiningHQDungeon
- **Poseidon Energy:** PoseidonPlant01 -> PoseidonPlant02 (Expansion)
- **The Pitt (Expedition):** XPDPitt01Industrial -> XPDPitt01Foundry -> XPDPitt01FoundryDungeon
- **Atlantic City:** XPDAC01Casino, XPDAC01NightClub, XPDAC02Aquarium, XPDAC02Pier, XPDAC02Boardwalk, XPDAC03CityHall, XPDAC03CommunityCenter, XPDAC03FloodedCityCenter

### Burning Springs Interiors
- Highway Town: BurnHWTownInt (main), BurnHWTLoanSharkInt, BurnHWTEugeneINT, BurnHWTMooseINT
- Athens: BurnAthensExecINT
- Abraxodyne: BurnAbraxodyneHQInt
- Railroad Service Yard: BurnRailroadServiceYardInt
- Rust Kingdom: BurnRustKingdomInterior
- Chop Shop: BurnChopShopBasement
- Checkpoint Canyon: BurnCheckpointCanyonInt

---

## 12. Event Trigger Zones

388 event-related quests identified in the QUST records. Events are triggered by location-based Story Manager entries. Key public events and their associated locations:

**Scorched Earth:** Fissure Site Prime (Cranberry Bog) -- triggered by nuking
**Encrypted:** Pylon Ambush Site (Ash Heap)
**Line in the Sand:** Fort Defiance (Cranberry Bog)
**Uranium Fever:** Blackwater Mine (Savage Divide)
**One Violent Night:** Sons of Dane Compound (Savage Divide)
**A Colossal Problem:** Monongah Mine (Savage Divide) -- triggered by nuking
**Radiation Rumble:** Emmett Mountain Disposal Site (Savage Divide)
**Moonshine Jamboree:** Big Maw (The Mire)
**Eviction Notice:** Foundation (Savage Divide)
**Test Your Metal:** Metal Dome (Savage Divide)
**Fasnacht:** Helvetia (The Forest)
**Monster Mash:** Watoga High School (Cranberry Bog)
**Feed the People:** Mama Dolce's Food Processing (The Forest)
**Path to Enlightenment:** Landview Lighthouse (The Forest)
**Campfire Tales:** Camp Adams (The Forest)
**Vault 94 raids:** Vault 94 (The Mire) -- now Daily Ops
**Burning Springs events:** Highway Town, Tycoon Lake, Athens, Rust Kingdom

Workshop events are location-bound to the 60 workshop REGN records listed above.

Random encounter events (RE_Travel, RE_Assault, RE_Object) spawn at placed markers throughout the APPALACHIA worldspace -- 50+ RE markers identified in Burning Springs alone.

---

## 13. Treasure Map Dig Sites

36 treasure maps exist as items in the game data (from strings file):

| Map | String ID |
|---|---|
| Forest Treasure Map #01-10 | `0x0003FC28` through `0x0003F98E` |
| Ash Heap Treasure Map #01-02 | `0x0003FBD6`, `0x0003FB7C` |
| Toxic Valley Treasure Map #01-04 | `0x0003FB9B` through `0x0003F8DE` |
| Savage Divide Treasure Map #01-10 | `0x0003FABD` through `0x0003FC1E` |
| Mire Treasure Map #01-05 | `0x0003FC62` through `0x0003FB28` |
| Cranberry Bog Treasure Map #01-04 | `0x0003F89A` through `0x0003FA8F` |
| Treasure Map 01 (generic) | `0x0003FBF7` |

**Total: 10 Forest + 2 Ash Heap + 4 Toxic Valley + 10 Savage Divide + 5 Mire + 4 Cranberry Bog + 1 generic = 36 maps**

Note: Dig site coordinates are not stored in location records but in the map note items themselves (BOOK records containing texture/image references). The actual dig positions are placed as REFR objects in the worldspace.

---

## 14. Worldspace Structure

### APPALACHIA Worldspace (`0x0025DA15`)

The main worldspace uses cell grid coordinates (XCLC fields) to divide the map into grid squares. Each cell is 4096 game units (roughly 57m) on a side. The DNAM field shows `1024.000000, 0.000000` indicating the world height map scale.

The worldspace XLCN links to location `0x0001558C` as the parent location for the entire map.

### Other Worldspaces in ESM

| FormID | Name | Purpose |
|---|---|---|
| `0x0000003C` | DefaultWorld | Fallout 4 leftover |
| `0x00635F96` | EXM1PittWorldspace | The Pitt expedition |
| `0x006FCD5A` | NPESuburbiaWorldspace | New Player Experience (tutorial) |
| `0x0025DA15` | APPALACHIA | Main game world |
| 50+ | Test/Debug worlds | Developer test spaces |

---

## 15. Expedition Locations (DLC)

### The Pitt (7 map marker locations)
All tagged with `LocTypeExpedition` (`0x0062D326`):
- The Foundry (x2, base + dungeon)
- The Pitt (Industrial)
- The Trench
- Steel Tower
- Purgatory
- Sanctum

### Atlantic City (8 map marker locations)
Tagged with `LocRegionAC` (`0x006AFE11`):
- Aquarium of the Atlantic (x2, base + dungeon)
- Boardwalk
- Casino
- Casino Quarter
- Community Center (x2, base + dungeon)
- Flooded City Center

---

## Technical Notes

- String references use prefix bytes to indicate table: `0x61` = .strings, `0x71` = .ilstrings, `0x41`/`0x81`/`0xd9` = .dlstrings
- Many FULL name references (especially `0x71` prefix) could not be resolved, likely stored in ILSTRINGS entries added by patches/DLC
- The `markers` binary tool in fo76utils can render map markers to DDS images given the ESM file and an icon list, but requires the actual .esm file (not the text dump)
- REFR records containing coordinates (DATA fields with X,Y,Z positions) are not included in the text dump format -- the dump captures record structure but not all sub-record binary data
- For actual X,Y,Z coordinates of every location, the fo76utils `esmdump` or `markers` tool needs to be run against the binary ESM with coordinate extraction flags
- Location hierarchy is defined by PNAM (parent location) fields in LCTN records, creating a tree from WorldLocation down to individual rooms

---

## Data Inventory

| Category | Count |
|---|---|
| Total LCTN records | 1,917 |
| Fast travel destinations | 539 |
| Map marker locations | 194 |
| Public workshops | 22 (+1 DLC) |
| Fissure sites | 13 |
| Vault locations | 38 (6 accessible vaults + shelters + systems) |
| Missile silos | 3 active + 1 cut |
| Nuke target locations | 38 |
| Cave entrances | 28 |
| Dungeon locations | 254 |
| Named interior cells | 654 |
| Region records (REGN) | 461 |
| Cut/disabled locations | 52 |
| Treasure maps | 36 |
| Event quests | 388 |
| Named world references | 470 |
| Burning Springs locations | 109 |
| Skyline Valley locations | 65 |
| Disabled records (all types) | 8,535 |
