# 038 - World Placement Records: Hidden Locations, Disabled Markers, and Out-of-Bounds Content

**Source**: `WRLD_records.txt` (214,180 lines), `CELL_records.txt` (17,854 lines)
**Date**: 2026-03-20

---

## 1. All Worldspaces (56 Total)

The game contains **56 worldspace definitions**. Only 2 are used for live gameplay (APPALACHIA and EXM1PittWorldspace). The rest are test, debug, or legacy content.

### Live Worldspaces
| FormID | EditorID | Notes |
|--------|----------|-------|
| 0x0025DA15 | APPALACHIA | Main game world (formerly DefaultWorld 0x3C) |
| 0x00635F96 | EXM1PittWorldspace | The Pitt expeditions worldspace |
| 0x006FCD5A | NPESuburbiaWorldspace | New Player Experience (Vault 76 exit area) |

### Fallout 4 Leftover Worldspaces (Still in ESM!)
| FormID | EditorID | Notes |
|--------|----------|-------|
| 0x0000003C | DefaultWorld | FO4's Commonwealth worldspace definition |
| 0x00000F93 | DiamondCityFX | FO4 Diamond City effects worldspace |
| 0x00000F94 | DiamondCity | FO4 Diamond City worldspace |
| 0x00054BD5 | Goodneighbor | FO4 Goodneighbor worldspace |

These are vestigial records from when FO76 forked from the FO4 codebase. They contain no playable content but demonstrate the shared engine heritage.

### Developer Test Worldspaces (37 Total)
| FormID | EditorID | Developer |
|--------|----------|-----------|
| 0x00001206 | TestConnorExt | Connor |
| 0x00001559 | TestVertibirdWorld | Vertibird testing |
| 0x000027AC | TestGabe | Gabe |
| 0x00002ED3 | DebugAlexBurback | Alex Burback |
| 0x000040E3 | TestStaticCollectionWarehouse | Static collections |
| 0x00004B16 | DevCoryWorld | Cory |
| 0x00005842 | TestRafael | Rafael |
| 0x00006AE0 | Test76Worldspace | General 76 testing |
| 0x00006B8F | TestSal | Sal |
| 0x00007848 | TestGabeLandscape | Gabe (landscape) |
| 0x00008000 | TestSLABs | Terrain slabs |
| 0x00008C9C | TestRobertPOIwarehouse | Robert (POI) |
| 0x00008E13 | TestAndrewWorld | Andrew |
| 0x0000A94E | TestPBRWorld | PBR materials |
| 0x0000CE7A | TestTheHillsHaveEyes | "The Hills Have Eyes" POI |
| 0x0000D1F7 | TestSCOL | Static collections |
| 0x0000D6AF | TestMikeWorld | Mike |
| 0x0000DC58 | TestWorkshop | Workshop system |
| 0x0000DC6C | TESTNewTerrain | Terrain system |
| 0x0000DC6D | TestLandscape | Landscape |
| 0x0000DEB8 | TestJayWorld | Jay |
| 0x0000F37B | TestRE | Random encounters |
| 0x0000F7F6 | TestAudioWorld | Audio |
| 0x0000FBA6 | TestHkDestructionWorld | Havok destruction |
| 0x0000FD14 | TestEncSpawnWorld | Encounter spawning |
| 0x0000FFF0 | TestSimplygon | Simplygon LOD |
| 0x0000FFF1 | TestSimplygonStaticCollections | Simplygon + static |
| 0x000115EE | TestSimplygonWithSCHouses | Simplygon + houses |
| 0x00011A5C | TestRobertWorld | Robert |
| 0x00011B84 | TestRafael2 | Rafael |
| 0x00012219 | TestSimplygonStaticWithPoxyHouses | Simplygon edge cases |
| 0x000125A2 | TestPhysicsWorld | Physics |
| 0x00017DBB | TestSteveCWorld | Steve C |
| 0x00029257 | TestBales | Bales |
| 0x0004DED6 | TestMuckWorld | Muck/swamp |
| 0x0004E0EC | TestQuickplayWorld | Quickplay system |
| 0x00061705 | TestDrewWorld | Drew |
| 0x0008602D | DebugPurkey | Purkey |
| 0x00093E04 | TestJarrodWorld | Jarrod |
| 0x00093E05 | TestJarrod2 | Jarrod |
| 0x0009895B | TestChrisExt | Chris |
| 0x0009A264 | TestJHollar1 | J Hollar |
| 0x0010D87D | TestOutsource | Outsource testing |
| 0x0012D5EE | TestEffectsWorld | VFX |
| 0x0013B813 | TestNavmesh | Navmesh |
| 0x00173A2B | DebugFlight | Flight/vertibird |
| 0x001E0D39 | TestMadWorld | "Mad World" |
| 0x0043D900 | DebugRussellWorld | Russell |
| 0x006E5A1F | DebugJeffUWorldspace01 | Jeff U |

**Notable**: `TestTheHillsHaveEyes` (0x0000CE7A) suggests a location concept that may have been cut or reworked. `TestMuckWorld` was likely prototyping for the Mire region.

---

## 2. Cut and Disabled Cells

### Total Cut Content by Category
- **zCUT-prefixed cells**: 233
- **zzz/ZZZ-prefixed cells**: 50
- **Debug cells**: 122
- **Test cells in WRLD**: 137

### High-Value Cut Cells

#### Cut Vault Content
| FormID | EditorID | Significance |
|--------|----------|-------------|
| 0x00002E22 | **zCUTVault65** | Vault 65 -- entire vault cell existed and was cut |
| 0x00004CCA | zCUTUnusedVault120AirlockCOPY0000 | Vault 120 airlock -- 5 copies of Vault 120 cells |
| 0x00004CEE | zCUTUnusedVault12004COPY0000 | Vault 120 interior section |
| 0x00004CF4 | zCUTUnusedVault12003COPY0000 | Vault 120 interior section |
| 0x00004D4C | zCUTUnusedVault12002COPY0000 | Vault 120 interior section |
| 0x00004D4D | zCUTUnusedVault120COPY0000 | Vault 120 base cell |
| 0x0000DAFF | zCUTVault96 | Original Vault 96 (replaced) |
| 0x0000E7D1 | zCUTVault9402OLD | Old Vault 94 layout |
| 0x00044A50 | zCUTVault63Entrance | Cut Vault 63 entrance (pre-Skyline Valley) |
| 0x00121929 | zCUTVault63 | Original Vault 63 interior |
| 0x003F3166 | zCUTVault63Gear | Cut Vault 63 gear door |
| 0x003F3167 | zCUTVault96Gear | Cut Vault 96 gear door |
| 0x003F3A55 | zCUTVault96Gear02 | Second cut gear door |
| 0x00403828 | zCUTDebugVault79Entrance | Debug version of Vault 79 entrance |
| 0x00453A17 | zCUTVault94Gear | Cut Vault 94 gear door |
| 0x00455993 | zCUTVault94GECK | **Cut Vault 94 G.E.C.K. cell** |
| 0x00456F1D | zCUTVault94Main | Cut Vault 94 main area |
| 0x0046085D | zCUTVault9603Steve | Vault 96 dev iteration |
| 0x0046281B | zCUTVault96Main | Cut main Vault 96 |
| 0x00465421 | zCUTVault96OLD | Old Vault 96 |
| 0x0047D304 | zCUTVault9602 | Vault 96 iteration 2 |
| 0x0047F9CF | zCUTVault9603 | Vault 96 iteration 3 |
| 0x002FF5C2 | zCUTVaultSystemHoldingCell | Cut vault system staging cell |
| 0x006867AE | zzzCUTStormVault63Atrium | Cut Storm-era Vault 63 atrium |
| 0x00693DA8 | zzz76StormRDVault63Hub | Cut Vault 63 hub (Storm/Skyline Valley) |
| 0x006F8FAB | zCUTVault63AshHeapExt | **Cut Vault 63 Ash Heap entrance** -- suggests Vault 63 was originally in the Ash Heap, not Skyline Valley |
| 0x0011221B | zCUTDLC06VaultWorkshop | Cut DLC vault workshop |
| 0x006862F6 | ZZZ76StormGPVault | Cut Storm-era vault |

#### Cut Locations
| FormID | EditorID | Significance |
|--------|----------|-------------|
| 0x000242A2 | **zCUTMoleManCity01** | Cut Mole Miner underground city |
| 0x00006F40 | **zCUTHuntersvilleSewers** | Cut sewer system under Huntersville |
| 0x000073A5 | **zCUTGeneralAtomicsPlant01** | Cut General Atomics factory |
| 0x0000572C | **zCUTBigFredsBBQShack01** | Cut Big Fred's BBQ location |
| 0x00044CE9 | zCUTCharlestonCapitolBuilding01 | Cut original Charleston Capitol |
| 0x00098971 | zCUTWhitespringResort01 | Cut original Whitespring interior |
| 0x003CD8DA | zCUTMorgantownAirportTerminal01 | Cut Morgantown Airport terminal |
| 0x00590369 | zCUTClarksburgPharmacy01 | Cut Clarksburg pharmacy |
| 0x0054E80D | **zCUTSecretResearchLaboratory01** | Cut secret lab |
| 0x0040A89D | zCUTMireBunker01 | Cut bunker in the Mire |
| 0x00003261 | zCUTWhitespringBunkerOld | Original Whitespring Bunker layout |
| 0x00208DF0 | zCUTGraftonDam01 | Cut Grafton Dam interior |
| 0x0010E5C6 | zCUTTestConvertedMunitionsFactory01 | Cut Munitions Factory layout |
| 0x0057D7F5 | zCUTTestOrionGraftonSteelUnderground01 | **Cut underground section of Grafton Steel** |
| 0x00004057 | zCUTCharlestonHoldingCell | Cut Charleston staging cell |
| 0x002B802D | zCUTBabylonStagingAreaZax | Cut Babylon/ZAX staging area |
| 0x00530EBC | zCUTMonongahMissileSiloOLD | Original missile silo layout |

#### Cut Shelters (Player Housing)
| FormID | EditorID |
|--------|----------|
| 0x005A5883 | zCUTSheltersUnusedBoSBunker |
| 0x005ACC5B | zCUTSheltersUnusedBasicCave |
| 0x005B36E4 | zCUTSheltersUnusedGreenhouse |
| 0x005B4DC5 | zCUTSheltersUnusedWaterfallCave |
| 0x0077D002 | zzzSheltersHousingDevelopment |

#### Cut Backwoods/Burn Content
| FormID | EditorID |
|--------|----------|
| 0x007CFAB3 | ZZZBurnChopShop01 |
| 0x007DE6FD | ZZZBurnCheckpointCanyonInt |
| 0x007DF6DE | ZZZBurnCheckpointCanyonInterior |
| 0x007DF779 | zzzBURNSQ01TestCell |
| 0x007D3DF1 | zzzBURNSQ04TestCell |
| 0x0080BFDB | zzzBURNE02SinkholeTestCell |
| 0x0082B1BF | zzzBURNFictionCell |
| 0x007FE0CA | zzzBurnDinoGolfDinerInterior |
| 0x00815641 | zzzBurnRailroadServiceYardInt |

**The "Dino Golf Diner" is a cut interior from Backwoods** -- a mini-golf/dinosaur themed location that was prototyped but may have been changed or dropped.

---

## 3. Outside Appalachia References

### Ohio/Backwoods Content
The "Burn" (Backwoods) update extends the map westward into Ohio:

| Evidence | FormID | Details |
|----------|--------|---------|
| Road sign: "Athens City Limits" | 0x008024F6 | PackInBurnRoadSignAthensCityLimits01 |
| Road sign: "Ohio State Line" | 0x008024F8 | PackInBurnRoadsignsOhioStateLine01 |
| Road sign: "WV State Line" | 0x008024F3 | PackInBurnRoadSignWVStateLine01 |
| Road sign: "Route 35 East/West" | 0x00809E09/0A | US Route 35 runs through southern Ohio/WV |
| Interior: Athens Executive building | 0x008258D7 | BurnAthensExecINT |
| Cut debug: "David B Athens" | 0x007B7936 | zCUTDebugDavidBAthens |
| Deathclaw nest | 0x007EDE97 | DeathclawNest-Athens |
| Ohio River poster | 0x003DCA85 | mtr04_ohioriverposter (in main WRLD) |

**Burning Springs is the new 9th region**, confirmed by `RegionMapMarkerBurningSprings` (0x0086998B). The map literally crosses into Ohio.

### The Pitt (Pittsburgh)
- Separate worldspace: `EXM1PittWorldspace` (0x00635F96)
- Single exterior cell: `EXM1PittExt` (0x00635F97)
- Extensive Pitt02 Trench content in CELL records (train tunnels, sewer entrances, waterfall outposts)
- Cut version: `zzzXPDPitt02TrenchCopy01` (0x007F55F5)

### Shenandoah (Skyline Valley)
- 8 exterior cells: `StormShenandoahWeatherStationExt` through `Ext08`
- This is the Shenandoah National Park-inspired weather station, part of the Skyline Valley update

---

## 4. Complete Vault Location Map

### Active Vaults
| Vault | Interior Cell | Exterior Cell(s) | Status |
|-------|--------------|-------------------|--------|
| **Vault 51** | Vault51Dungeon (0x0060A6C0) | Vault51Ext (0x00264124) | Nuclear Winter lobby / dungeon |
| **Vault 63** | StormVault63Entrance (0x006F7FAC), StormVault63AtriumUpper (0x006DCD33), StormVault63AtriumLower (0x006FA30E), Vault63Organics (0x006A2D53), StormEngineeringVlt63 (0x006A0A3D) | Vault63Ext (0x00263BFA), StormVault63CrashSiteExt x4 | Skyline Valley main dungeon |
| **Vault 76** | NPEVault7601 (0x006BEEC5), NVEVault7601 (0x006AFE91) | Vault76Ext x7 (0x00263D52+), W05Vault76LandingExt x2 | Starting vault, new player experience |
| **Vault 79** | Vault79Main (0x00401116), Vault79Entrance (0x005661B4), Vault79GoldVaultOperations (0x004060AF) | Vault79EntranceExt (0x00260D52), Vault79ExitExt (0x00260D56) | Wastelanders gold vault |
| **Vault 94** | Vault94Dungeon (0x005B7D87), Vault94DungeonGECK (0x005D6247), Vault94Entrance (0x0011F9E7) | Vault94Ext (0x00260D62) | Raid dungeon / Daily Ops |
| **Vault 96** | Vault96Dungeon (0x005DD731) | Vault96Ext (0x002623A7), Vault96Ext02 (0x002623A6), Vault96TestEMS, Vault96ExtElevatorExit | Cryogenics vault |

### Cut/Unused Vaults
| Vault | Cell(s) | Notes |
|-------|---------|-------|
| **Vault 65** | zCUTVault65 (0x00002E22) | **Completely cut vault. Only a single cell remains.** |
| **Vault 120** | 5 cells: zCUTUnusedVault120 + 4 copies (0x00004CCA-0x00004D4D) | **Cut vault with airlock section. Multiple interior zones were built before being abandoned.** |

### Missing from Data
- **Vault 64**: No cell or reference found in either WRLD or CELL records
- **Vault 120**: Only cut copies remain -- the original was overwritten

### Makeship Vault
| FormID | EditorID | Notes |
|--------|----------|-------|
| 0x00263954 | MakeshiftVaultExt | Player-built or improvised vault exterior |
| 0x00263955 | MakeshiftVaultExt02 | Second exterior cell |

### Vault-Adjacent Content
- `ClassifiedVaultAccessLaserGridRef` (0x00591E69) -- a laser grid blocking access to an unnamed "classified vault"
- `zCUTVault94GECK` (0x00455993) -- Vault 94 had a G.E.C.K. cell that was cut
- `StormVault63AtriumUpperOLD` (0x00756ACE) -- old layout of the Vault 63 atrium before Skyline Valley shipped
- `76Trailer` vault exit actors (Margret, Biscuit, Louise, Alice, Kathy, Cody, Carol, Barney, Markie, Sandy, Ron) -- NPCs from the FO76 trailer's vault exit scene

---

## 5. Map Markers (127 Location Markers)

### Region Markers (9 regions confirmed)
| FormID | EditorID |
|--------|----------|
| 0x00869989 | RegionMapMarkerTheForest |
| 0x0086998A | RegionMapMarkerAshHeap |
| 0x0086998B | **RegionMapMarkerBurningSprings** |
| 0x0086998C | RegionMapMarkerCranberryBog |
| 0x0086998D | RegionMapMarkerMire |
| 0x0086998E | RegionMapMarkerToxicValley |
| 0x0086998F | RegionMapMarkerSkylineValley |
| 0x00869990 | RegionMapMarkerSavageDivide1 |
| 0x00869991 | RegionMapMarkerSavageDivide2 |

**Burning Springs is the 9th region, with Savage Divide split into 2 markers.**

### Fast Travel Destinations (17 confirmed)
All 10 train stations plus Point Pleasant, Abandoned Bog Town, Berkeley Springs bus stops, Super Duper Mart, Burn Chop Shop, and the SDM fast travel marker.

### Backwoods Map Markers
| FormID | EditorID |
|--------|----------|
| 0x007D9F4F | Burn_RailroadServiceYardMapMarker |
| 0x007E808C | HighwayTownMapMarker |
| 0x007CEAA0 | SuperDuperMartMapMarker |
| 0x00791779 | MilepostZeroMapMarker |
| 0x007981E5 | GhoulCampMapMarkerID |
| 0x007A8AA0 | FishermansRestMapMarker |

### Skyline Valley Map Markers
| FormID | EditorID |
|--------|----------|
| 0x006BBE8B | Storm_WeatherLab_MapMarkerRef |
| 0x006B9770 | TradingPostMapMarker |
| 0x00787C51 | Storm_DarkwoodManorMapMarker |

### Nuka-World on Tour
| FormID | EditorID |
|--------|----------|
| 0x00674C7F | NukaWorldMapMarker |

---

## 6. Out-of-Bounds Cells (Extreme Coordinates)

### Map Coordinate Ranges
- **Main Appalachia grid**: roughly -101 to +101 on both X and Y axes (202x202 cell grid)
- Standard cell size: 4096 game units

### Far-Field Cells (Outside Normal Grid)
| FormID | X | Y | Notes |
|--------|---|---|-------|
| 0x006DDDA4 | 178 | -10 | Far east of map boundary |
| 0x006DDDA5 | 233 | -10 | Very far east |
| 0x006DDDA6 | 237 | -10 | Very far east |
| 0x006DDDA7 | 251 | -10 | **Extreme east -- 150 cells past map edge** |
| 0x0051DDEC | -190 | -221 | **Extreme southwest -- 90 cells past map edge** |
| 0x0051DDED | -166 | -195 | Far southwest |

These unnamed cells at extreme coordinates are likely either:
- LOD (Level of Detail) anchor cells for distant rendering
- Skybox or environmental effect staging
- Legacy cells from development

The cell at (251, -10) is over **1 million game units** east of the map boundary -- far beyond any playable area.

### Cells with Negative Water Heights (Below Terrain)
| Cell | Water Height | Notes |
|------|-------------|-------|
| PalaceOfTheWindingPathExt | **-10000.0** | Extremely deep void below Palace |
| PalaceOfTheWindingPathExt02 | -100.0 | Moderately below terrain |
| AaronholtHomesteadExt03 | -512.0 | Below terrain water plane |
| TestCellConnor | -1024.0 | Test cell |
| TestVertibird01 | -1024.0 | Test cell |
| TestWorkshopOrigin | -1024.0 | Test cell |
| NavmeshCenter | -1024.0 | Test cell |
| DebugFlightExt | -1024.0 | Debug cell |

**The Palace of the Winding Path has a water height of -10,000** -- this is an intentional void beneath the location, likely to prevent players from reaching anything below it or to create the illusion of a bottomless pit.

---

## 7. Holding Cells (Hidden Staging Areas)

33 holding cells exist as invisible "backstage" areas where the game stores NPCs, manages quest state, and runs scripts:

| FormID | EditorID | Purpose |
|--------|----------|---------|
| 0x00004AC8 | 76HoldingCell | Main holding cell |
| 0x00001243 | 76HoldingCellSQHorde | Horde event staging |
| 0x0006DE63 | 76HoldingCellEnclave | Enclave NPC staging |
| 0x0030A736 | 76HoldingCellGraftonMayor | Grafton Mayor robot staging |
| 0x00345D4F | 76HoldingCellMoM | March of the Mothman staging |
| 0x003DE790 | 76HoldingCellMSilo | Missile Silo quest staging |
| 0x0040F5C1 | 76HoldingCellWayward | The Wayward quest staging |
| 0x006551DD | 76HoldingCellKennethDean | Kenneth Dean NPC staging |
| 0x00665A65 | 76HoldingCellNWOT | Nuka-World on Tour staging |
| 0x006957FF | **76HoldingCellMoon** | **"Moon" -- purpose unknown, possibly Moonshine Jamboree or future content** |
| 0x006F618C | 76HoldingCellStorm | Skyline Valley quest staging |
| 0x007915F8 | 76HoldingCellMile | Milepost Zero staging |
| 0x007BC5E3 | 76HoldingCellFishing | Fishing system staging |

---

## 8. Backwoods / Burning Springs Content (March 2026)

### Live Interior Cells
| FormID | EditorID |
|--------|----------|
| 0x007B11C8 | BurnHWTownInt (Highway Town interior) |
| 0x007FE836 | BurnRustKingdomInterior |
| 0x0082D9B1 | BurnChopShopBasement |
| 0x00830735 | BurnRailroadServiceYardInt |
| 0x008316E2 | BurnCheckpointCanyonInt |
| 0x0081E4EE | BurnHWTMooseINT |
| 0x00821653 | BurnHWTEugeneINT |
| 0x00821ED8 | BurnHWTLoanSharkInt |
| 0x00821B6B | BurnAbraxodyneHQInt |
| 0x008258D7 | BurnAthensExecINT |
| 0x007B11C9 | 76BurnAssetZoo (developer asset showcase) |

### Road Sign Content (Confirms Geography)
- Ash Cave sign, Cornhenge sign, Mini Golf sign, Fort sign, Drive-In sign
- Highway signs, Church signs, Bus stop rural
- Route 35 East/West signs
- All confirm the Burning Springs region is set in the WV/Ohio border area

---

## 9. Skyline Valley (Storm) Content

### Exterior Locations (100+ cells)
Major areas with exterior cells:
- **Darkwood Manor**: 16 exterior cells
- **Shenandoah Weather Station**: 8 exterior cells
- **Camp Rapidan**: 12 exterior cells
- **Pioneer Rangers Summer Camp**: 14 exterior cells
- **Vault 63 Crash Site**: 4 exterior cells
- **Red Rocket Motel**: 7 exterior cells
- **Natural Bridge**: 4 exterior cells
- **Three Ponds**: 4 exterior cells
- **Cultist Church**: 3 exterior cells
- **Blue Ridge Camp**: 2 exterior cells
- **Skybound Tower**, **Ice Cream Rest Stop**, **Makeout Point**, and more

### Interior Cells
| FormID | EditorID |
|--------|----------|
| 0x006D3EC7 | StormWeatherLab01 |
| 0x006C2935 | StormCultistTunnels |
| 0x006C3495 | StormHallucinogeniccave |
| 0x006F7FAA | StormStolzManor |
| 0x006DE4FF | StormBrownHouse |
| 0x006E38D2 | StormHighKnobFireTower01 |
| 0x006EC67D | StormVisitorCenterInt |
| 0x00727A5D | StormRadioBunkerInt |
| 0x0078CF48 | StormPresidentialBunker |

---

## 10. Developer Debug and Game Jam Cells

### Game Jam 2025
| FormID | EditorID |
|--------|----------|
| 0x007EBC85 | **DebugGamejam2025** | Internal game jam prototyping cell |

### Proto Expo Cells (Internal Showcases)
| FormID | EditorID |
|--------|----------|
| 0x005B0624 | zCUTProtoExpo01 |
| 0x005B30C8 | zCUTProtoExpo02 |
| 0x005AE424 | zCUTProtoExpo03 |
| 0x005B5E1E | zCUTProtoExpo05 |
| 0x005F1417 | zCUTProtoExpo06 |

These "Proto Expo" cells were internal presentation/demo cells where developers showcased upcoming features.

### Notable Debug Cells
| FormID | EditorID | Significance |
|--------|----------|-------------|
| 0x006AC521 | DebugHillValley | "Hill Valley" -- Back to the Future reference? |
| 0x006CD0F1 | DebugGreenScreen | Green screen studio for cinematics |
| 0x0010D513 | DebugVanityLightStagingCell | Lighting test for Atomic Shop items |
| 0x0066AFB5 | DebugWSEventTest | Whitespring event testing |
| 0x0077529A | WarehouseUnused | Unused warehouse interior |
| 0x00007860 | zCUT76PVEPlayground | Cut PVE playground |
| 0x00031121 | zCUT76AITestArena | Cut AI test arena |
| 0x00004007 | zCUT76DangerRoom | **"Danger Room" -- cut combat testing arena** |

---

## 11. Hidden Interior Cells (No Known Exterior Door)

These cells exist in the CELL records but have no corresponding exterior door reference or load door in the WRLD records:

| FormID | EditorID | Notes |
|--------|----------|-------|
| 0x0054E80D | zCUTSecretResearchLaboratory01 | Secret lab with no exterior connection |
| 0x000242A2 | zCUTMoleManCity01 | Underground mole miner city -- no exterior entry |
| 0x00006F40 | zCUTHuntersvilleSewers | Sewer network with no surface access |
| 0x0040A89D | zCUTMireBunker01 | Bunker in the Mire with no entry point |
| 0x002B802D | zCUTBabylonStagingAreaZax | ZAX computer staging area |
| 0x0000572C | zCUTBigFredsBBQShack01 | BBQ restaurant interior |
| 0x000073A5 | zCUTGeneralAtomicsPlant01 | General Atomics factory |
| 0x006957FF | 76HoldingCellMoon | Mysterious "Moon" holding cell |

---

## 12. Key Findings Summary

1. **56 worldspaces** exist, but only 3 are used for gameplay (Appalachia, The Pitt, NPE Suburbia). 4 are Fallout 4 leftovers.

2. **Vault 65 was fully cut** -- a single cell `zCUTVault65` confirms it existed in development. **Vault 120 had 5 cells** including an airlock before being cut. Vault 64 has zero data presence.

3. **Vault 63 was originally planned for the Ash Heap** (`zCUTVault63AshHeapExt`), not Skyline Valley. It was relocated during development.

4. **Burning Springs (Backwoods) extends into Ohio** -- road signs for Athens City Limits, Ohio State Line, and Route 35 confirm the map crosses the WV border. This is the 9th region.

5. **233 cut cells** preserve development history -- from a Mole Miner underground city to a Danger Room combat arena to Huntersville sewers.

6. **Cells exist at extreme coordinates** -- one cell sits at grid position (251, -10), over a million game units east of the playable map. Another pair sits at (-190, -221), far southwest.

7. **Palace of the Winding Path** has a water height of -10,000, the deepest void in the game data -- likely preventing any kind of underworld access.

8. **33 holding cells** serve as invisible backstage areas. The mysterious `76HoldingCellMoon` has no clear connection to known content.

9. **Game Jam 2025** left a debug cell in the shipping game, confirming internal prototyping events.

10. **Vault 94 originally had a G.E.C.K.** (Garden of Eden Creation Kit) cell that was cut -- significant lore implications for what that vault's experiment was meant to be.

11. **Backwoods has a cut "Dino Golf Diner"** interior, suggesting a dinosaur-themed mini-golf attraction was prototyped but may have been reworked or dropped.

12. **No disabled map markers with zzz_ prefix** were found in WRLD records -- Bethesda uses `zCUT` prefixing on cells rather than markers for disabled content.
