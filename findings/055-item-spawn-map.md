# Finding 055: Item Spawn Location Map -- Complete Loot System Extraction

## Summary

Comprehensive extraction of Fallout 76's item spawn system from the ESM data, covering every loot container type, leveled item list (LVLI), world-placed spawn point (LPI), flora harvest location, resource extraction node, and spawn probability curve. The game uses a sophisticated multi-layered loot system with **10,411 leveled item lists** (LVLI records), **755 world-placed spawn points** (LPI records), **146 flora spawn definitions**, **125 container loot configurations**, **70 workshop production lists**, and **144 spawn chance globals** -- all governed by economy curve tables that dynamically adjust spawn rates based on player level.

## Data Sources

- `LVLI_records.txt` (49,308 lines) -- All leveled item lists (loot tables)
- `WRLD_records.txt` (214,180 lines) -- World cell data with 7,529 placed references
- `GLOB_records.txt` (11,009 lines) -- Global variables including spawn chances
- `CELL_records.txt` (17,854 lines) -- Interior cell definitions
- `BOOK_records.txt` -- Treasure map items
- `ACTI_records.txt` -- Activator records (resource extractors)
- `MISC_records.txt` -- Miscellaneous items (flux, components)
- `FLST_records.txt` -- Form lists (bobblehead/magazine challenge lists)
- Economy curve tables: `tempest_data/misc/curvetables/json/econ/`

## The LVLI Naming Convention System

Bethesda uses a strict naming prefix system for leveled item lists:

| Prefix | Purpose | Count |
|---|---|---|
| `LL_` | Standard leveled list (items, weapons, armor) | 5,409 |
| `LLS_` | Leveled list sub-list (nested references) | 1,729 |
| `LPI_` | Leveled Placed Item (world-spawn point) | 755 |
| `LLV_` | Vendor leveled list | 274 |
| `LLD_` | Drop leveled list (event/creature drops) | 205 |
| `crLLI_` | Creature leveled item (creature inventories) | 261 |
| `Container_Loot_` | Container-specific loot tables | 143 |
| `ATX_` | Atom Shop / premium items | 854 |
| `workshop_` | Workshop/CAMP buildable items | 1,345 |
| `WorkshopProduce` | Workshop resource production | 70 |

**LPI records are the key to the interactive map** -- they represent physically placed items in the world with specific spawn rules.

---

## 1. Resource Extraction Nodes (Workshop Resources)

### Workshop Production Lists (70 total)

Every workshop resource extractor produces items via a WorkshopProduce LVLI. These are the extractable resources:

**Raw Materials:**
| FormID | Resource | Notes |
|---|---|---|
| `0x000897C3` | Acid | |
| `0x000897C4` | Adhesive | |
| `0x000897DF` | Aluminum | |
| `0x0054B42B` | Aluminum (Scrap variant) | |
| `0x0033E207` | Ash | Ash Heap specific |
| `0x0054B42A` | Ceramic | |
| `0x0054B42C` | Cloth | |
| `0x004DE22C` | Coal | |
| `0x000897E0` | Concrete | |
| `0x00089807` | Copper | |
| `0x00089809` | Crystal | |
| `0x0054B42D` | Crystal (Scrap) | |
| `0x00249BEB` | Fertilizer | |
| `0x0054B42E` | Fiberglass | |
| `0x0054B42F` | Fiber Optics | |
| `0x003EB3D2` | Fusion Core | Power plants |
| `0x0054B425` | Gears | |
| `0x000897E2` | Gold | |
| `0x000897E6` | Lead | |
| `0x000897E1` | Nuclear Material | |
| `0x000897E7` | Oil | |
| `0x0054B430` | Oil (Scrap) | |
| `0x0054B428` | Plastic | |
| `0x0054B429` | Rubber | |
| `0x002932BC` | Silver | |
| `0x0054B436` | Silver (Ore) | |
| `0x0054B427` | Springs | |
| `0x000897E8` | Steel | |
| `0x004DE22E` | Titanium | |
| `0x00026833` | Water (Purified) | |
| `0x005D1F8D` | Dirty Water | |
| `0x00294337` | Wood | |
| `0x003CA908` | Ore (Mount Blair) | Excavator PA bonus |
| `0x0054B426` | Circuitry | |

**Food Production:**
| FormID | Food Tier | Notes |
|---|---|---|
| `0x003D101E` | Food00 (basic) | |
| `0x003D101D` | Food01 | |
| `0x003D101C` | Food02 | |
| `0x003D101B` | Food03 | |
| `0x003D1016` | Food04 (best) | |

**Ammo Production (Workshop Ammo Plants):**
| FormID | Ammo Type |
|---|---|
| `0x003B253D` | 10mm |
| `0x003B253E` | .308 |
| `0x003B253F` | .38 |
| `0x003B252B` | .44 |
| `0x003B252C` | .45 |
| `0x003B252D` | .50 |
| `0x003B252E` | 5.56 |
| `0x003B252F` | 5mm |
| `0x003B2530` | Fusion Cell |
| `0x003B2531` | Gamma Cell |
| `0x003B2532` | Plasma Cartridge |
| `0x003B2533` | Shotgun Shell |

**Wastelanders (W05) Ammo Construction Machine** adds duplicate ammo production lists with different FormIDs (0x00599473-0x005A668B).

---

## 2. Flora Spawn Locations

### Flora LPI Records (World-Placed Harvestable Plants)

Each flora type has a dedicated LPI_ record placed by level designers. The 0x0035D2xx range contains the bulk of flora spawns:

**Fruits/Vegetables (Farmable):**
| FormID | Plant | Variants |
|---|---|---|
| `0x0035D213` | Wild Tato Plant | 01, 02 |
| `0x0035D217` | Wild Melon Vine | 01 |
| `0x0035D221` | Wild Mutfruit | |
| `0x0035D222` | Wild Corn Stalk | 01 |
| `0x0035D239` | Wild Gourd Vine | 01 |
| `0x0035D23B` | Wild Razorgrain | 01 |
| `0x0035D215` | Wild Carrot Flower | |
| `0x0035D224` | Wild Tarberry Float | 01, 02 |

**Medicinal/Crafting Flora:**
| FormID | Plant | Rarity |
|---|---|---|
| `0x0035D236` | Starlight Creeper | 01, 02 (RARE - plantmarkerrare01.nif) |
| `0x0035D238` | Firecracker Berry | 01, 02 |
| `0x0035D235` | Fever Blossom | 01, 02 |
| `0x0035D232` | Snap Tail Reed | 01, 02 |
| `0x0035D234` | Soot Flower | 01, 02 |
| `0x0035D22E` | Bloodleaf | 01, 02 |
| `0x0035D230` | Silt Bean | 01, 02 |
| `0x0035D23C` | Firecap | 01 |
| `0x0035D242` | Ash Rose | 01, 02 |
| `0x0035D22A` | Blight | 01 |
| `0x0035D21D` | Blackberry | 01, 02 |
| `0x0035D216` | Bleach Dogwood Bark | 01, 02, 03 |
| `0x0035D228` | Glowing Fungus | 01-06 |
| `0x0035D218` | Brain Fungus | 01-03 |
| `0x0035D22F` | Sap | 01, 02 |
| `0x0035D24E` | Aster | 01 |
| `0x0035D21B` | Bloodleaf | 02 |
| `0x0035D21C` | Sap | 02 |

**Region-Specific Flora:**
| FormID | Plant | Region |
|---|---|---|
| `0x000686BB` | Cranberry | 01-03 (Cranberry Bog) |
| `0x002FAE94` | Cranberry (Leveled) | Cranberry Bog |
| `0x0035D227` | Cranberry (Diseased) | 01-03 |
| `0x0036B805` | Toxic Soot Flower | 01, 02 (Toxic Valley) |
| `0x0038F0A8` | Swamp Pod | 01 (The Mire) |
| `0x003FFAD9` | Kaleidopore | 01 (Skyline Valley) |
| `0x00412189` | Gut Shroom | 01 |
| `0x00519299` | Ginseng | 01 |
| `0x00525648` | Rhododendron | 01 |
| `0x0052B5CA` | Pitcher Plant | |
| `0x0052CF9C` | Pumpkin | 01 |
| `0x00853BA2` | Slipper Cactus | 01-03 (Burning Springs) |
| `0x00848005` | Ginseng | (LL_Flora) |

**Event Flora:**
| FormID | Plant | Event |
|---|---|---|
| `0x0035D237` | Mothman Eggs | 01-03 |
| `0x006189AC` | Enlightened Mothman Eggs | 01-03 (Equinox event) |

**Nuke Zone Flora Marker:** Flora LPI records using `plantmarkerrare01.nif` (rare marker mesh) indicate less common spawns. Standard flora uses `plantmarker01.nif`.

### Flora Economy Curves

The `flora_harvestable_chancenone.json` curve controls whether a harvestable plant is actually present when a player visits:

| Player Level | Chance None (%) | Effective Spawn Rate |
|---|---|---|
| 0 | 100% | 0% (nothing spawns at level 0) |
| 1 | 60% | 40% |
| 5 | 50% | 50% |
| 10 | 40% | 60% |
| 15 | 30% | 70% |
| 20 | 20% | 80% |
| 25 | 10% | 90% |
| 30-99 | 10% | 90% |
| 100 | 0% | 100% |

**Key insight:** At max level, ALL flora harvestable points are guaranteed to have items. Low-level players see far fewer harvestable plants.

The `flora_vein_chancenone.json` curve is identical to harvestable -- ore veins follow the same scaling.

---

## 3. Bobblehead Spawn Points

### The Bobblehead System

Bobbleheads use a two-tier spawn system:

1. **LPI_Loot_Bobbleheads** (`0x0001911D`) -- The master world-placed bobblehead list
   - References `LL_Loot_Bobbleheads_Agility_POI288` (`0x004FC090`) with a location condition (`GetInCurrentLocation` = `0x4FA7AA`)
   - Falls back to `LL_Loot_Bobbleheads` (`0x004FC08F`) for all other locations
   - Uses dummy marker: `markers/dummymarkers/dummymarkerbobblehead01.nif`

2. **LL_Loot_Bobbleheads** (`0x004FC08F`) -- Contains 4 LVLO entries (`0x004FE4E2`, `0x004FE4E7`, `0x004FE4E9`, `0x004FE4EB`) which are sub-lists for each bobblehead type

### Bobblehead Sub-Systems

| FormID | List Name | Purpose |
|---|---|---|
| `0x003EE9F3` | LL_Loot_CapsStash_Bobblehead | Bobblehead in cap stashes (2% chance) |
| `0x003DF3D2` | LLS_Loot_Bobbleheads_MTX | Premium/MTX bobblehead drops |
| `0x0072D4FE` | LL_BobbleheadBox_Loot | Bobblehead display box contents |
| `0x0072D4FF` | LL_BobbleheadBox_Loot_Normal | Normal quality |
| `0x00826865` | LL_BobbleheadBox_Loot_Glowing | Glowing variant |
| `0x007B74D6` | RD01_LLS_Raids_Rewards_BobbleHeads | Raid reward bobbleheads |
| `0x0079B9C7` | MILE_LL_Scavenger_BobbleHeads | Milepost scavenger reward |
| `0x007A2FA2` | GHL_LLS_GlowingBobbleheads | Glowing bobblehead list |
| `0x008A7176` | LTT_RA_Rewards_PublicEvents_Bobbleheads_DropRate | Drop rate toggle (currently 0.0) |

**Challenge tracking:** `0x0043AC12` (Challenge_Lifetime_META_Bobbleheads) and `0x0021666F` (AchievementBobbleheadList) track collection progress.

---

## 4. Magazine Spawn Points

### The Magazine System

| FormID | List Name | Purpose |
|---|---|---|
| `0x00322788` | LPI_Loot_Magazines | Master world-placed magazine list |
| `0x003DF3D1` | LLS_Loot_Magazines_MTX | Premium magazine drops |
| `0x0075887E` | LL_MagazineBookBox_Loot | Magazine rack contents |
| `0x0075887D` | LL_MagazineBookBox_Loot_List | Sub-list |
| `0x007B74DC` | RD01_LLS_Raids_Rewards_Magazines | Raid reward |
| `0x0079B9C4` | MILE_LL_Scavenger_Magazines | Milepost reward |

**LPI_Loot_Magazines** (`0x00322788`) contains 4 LVLO entries referencing sub-lists (`0x00432D60`, `0x0043037E`, `0x00430380`, `0x00430383`) covering all magazine families. Uses dummy marker: `markers/dummymarkers/dummymarkermagazine01.nif`.

### Wastelanders Region-Specific Magazines

| FormID | List | Region/Faction |
|---|---|---|
| `0x00598DB9` | W05_Denizen_LPI_Loot_Magazines_Backwoodsman | Wastelanders denizens |
| `0x00598DB8` | W05_Denizen_LPI_Loot_Magazines_GunsBullets | Wastelanders denizens |
| `0x00598DBB` | W05_Denizen_LPI_Loot_Magazines_Grognak | Wastelanders denizens |
| `0x00598DBC` | W05_Denizen_LPI_Loot_Magazines_LiveLove | Wastelanders denizens |
| `0x00598DBA` | W05_Denizen_LPI_Loot_Magazines_Unstoppables | Wastelanders denizens |

**Challenge tracking:** `0x0044D473` (Challenge_Magazines_All) with sub-lists for each magazine family (Grognak, Tesla Science, Tumblers Today, Scouts Life, Live and Love, Guns and Bullets, Astonishing Tales, Awesome Tales, US Covert Ops, Unstoppables).

---

## 5. Power Armor Spawn Locations

### PA Spawn Types

Power armor spawns use LPI_PowerArmorFurniture records, each placing a `powerarmorfurniture.nif` mesh:

| FormID | Type | Contents |
|---|---|---|
| `0x003B5FEB` | LPI_PowerArmorFurniture_General | Random PA: T-45 / T-51 / T-60 partial sets |
| `0x003B51E1` | LPI_PowerArmorFurniture_General_Locked | Same but requires lockpick |
| `0x0073C960` | LPI_PowerArmorFurniture_T45 | Guaranteed T-45 partial set |
| `0x0073C961` | LPI_PowerArmorFurniture_T45_Locked | T-45, locked |
| `0x003B51C9` | LPI_PowerArmorFurniture_Raider_Locked | Raider PA, locked |
| `0x0045CB38` | RE_ObjectCMB07_LPI_PowerArmorFurniture_Raider | Random encounter raider PA |
| `0x00613818` | DONOTUSELPI_PowerArmorFurniture_Hellcat_Full | Hellcat PA (quest reward only) |
| `0x00788D53` | RD01_DONOTUSELPI_PowerArmorFurniture_EnclaveVulcan_Full | Enclave Vulcan PA (raid reward) |
| `0x0059EFC3` | LPI_W05_MQR_202P_PowerArmorFurniture_FrameOnly | Frame only (Wastelanders quest) |

### PA Loot Chain

`LPI_PowerArmorFurniture_General` resolves to:
- `0x003B5FEC` = `LL_Armor_PowerArmor_T45_Frame_Partial` (T-45 partial)
- `0x003B5FDC` = T-51 partial
- `0x003B5FDD` = T-60 partial

Each "partial" list spawns a frame + random subset of armor pieces (helmet, torso, arms, legs).

**Named world reference:** `0x00002CA0` = WorkbenchPowerArmorBlackwaterMine (PA workbench in Blackwater Mine).

**PA Frame form list:** `0x001D271B` (PowerArmorFramesList) tracks all valid PA frame types.

---

## 6. Plan/Recipe Spawn Locations

### Plan and Recipe Lists

Plans and recipes use a region-based system. The Skyline Valley and Burning Springs DLCs introduced explicit regional plan pools:

**Regional Plan Pools:**
| Region | Armor Plans | Weapon Plans (Melee) | Weapon Plans (Ranged) | PA Plans |
|---|---|---|---|---|
| Skyline Valley | `0x0081EB25` | `0x0081EB2B` (LLS) | `0x0081EB2D` (LLS) | `0x0081EB39` |
| Burning Springs | `0x0081EB26` | `0x0081EB2C` (LLS) | `0x0081EB2E` (LLS) | `0x0081EB3A` |

**Vendor-Specific Regional Plans:**
| FormID | List | Content |
|---|---|---|
| `0x0081EB47` | LL_Recipes_Mods_Weapons_Any_RegionSkylineValley_Vendor | SV vendor weapon mods |
| `0x0081EB48` | LL_Recipes_Mods_Weapons_Any_RegionBurningSprings_Vendor | BS vendor weapon mods |
| `0x0081EB4C` | LL_Recipes_Mods_Armor_RegionBurningSprings_Vendor | BS vendor armor mods |

**Regional Mod Lists:**
| FormID | List | Region |
|---|---|---|
| `0x0081EAE2` | LL_Mods_PowerArmor_RegionSkylineValley | SV PA mods |
| `0x0081EAE4` | LL_Mods_PowerArmor_RegionBurningSprings | BS PA mods |
| `0x0081EB1F` | LL_Mods_Weapons_Ranged_RegionBurningSprings | BS ranged weapon mods |
| `0x0081EB20` | LL_Mods_Weapons_Any_RegionBurningSprings | BS all weapon mods |

**Burning Springs vendor plans include specific weapon mod breakdowns:**
- Pipe Gun (`0x0081EB16`)
- Pipe Syringer (`0x0081EB18`)
- Pump Action Shotgun (`0x0081EB1A`)
- Single Action Revolver (`0x0081EB1C`)
- Submachine Gun (`0x0081EB1D`)
- Combat Rifle (`implied`)

---

## 7. Loot Container Types and Their Leveled List Contents

### Container Hierarchy (125 unique container loot lists)

**Standard Containers:**
| FormID | Container Type | Contents Focus |
|---|---|---|
| `0x0006D4A3` | Container_Loot_Priority_AmmoBox | Ammo |
| `0x0006D4A6` | Container_Loot_Priority_Cooler | Food/drink |
| `0x000A0F5A` | Container_Loot_Priority_Cooler_PreWar | Pre-war food |
| `0x0006D4A7` | Container_Loot_Priority_Cooler_Raider | Raider food/chems |
| `0x0006D4A8` | Container_Loot_Priority_DuffleBag_Guns | Weapons |
| `0x0006D4A9` | Container_Loot_Priority_DuffleBag_Guns_Raider | Raider weapons |
| `0x0006D4AA` | Container_Loot_Priority_ExplosivesBox_Raider | Explosives |
| `0x000D6E66` | Container_Loot_Priority_Footlocker | General loot |
| `0x0006D4B8` | Container_Loot_Priority_Footlocker_FoodSupplies | Food supplies |
| `0x0006D4AC` | Container_Loot_Priority_Medkit | Medical |
| `0x0022335C` | Container_Loot_Priority_Medkit_Chems | Chems |
| `0x001BA1A8` | Container_Loot_Priority_Medkit_Chems_Prewar | Pre-war medical |
| `0x0006D4AB` | Container_Loot_Priority_Medkit_Chems_Raider | Raider chems |
| `0x0006D4AD` | Container_Loot_Priority_Medkit_Wall | Wall-mounted medkit |
| `0x000673B8` | Container_Loot_Locker_ChanceEmpty | Locker (may be empty) |
| `0x001C246D` | Container_Loot_Mailbox_ChanceEmpty | Mailbox (may be empty) |
| `0x00439714` | Container_Loot_Metalbox | Metal box |
| `0x003CF086` | Container_Loot_WoodCrate_Brown | Wood crate |
| `0x003CF085` | Container_Loot_Priority_WoodCrate_Dynamite | Dynamite crate |

**Locked/Special Containers:**
| FormID | Container Type | Notes |
|---|---|---|
| `0x001B8812` | Container_Loot_Priority_Raider_Safe | Raider safe |
| `0x003B810E` | Container_Loot_Priority_Raider_Safe_Trap | Trapped raider safe |
| `0x00369E82` | Container_Loot_Priority_Medkit_Chems_Locked | Locked medkit |
| `0x00369E83` | Container_Loot_Priority_Medkit_Chems_Prewar_Locked | Locked pre-war medkit |
| `0x00369E84` | Container_Loot_Priority_Medkit_Chems_Raider_Locked | Locked raider medkit |

**Boss/Event Containers:**
| FormID | Container Type | Notes |
|---|---|---|
| `0x00452A5D` | Container_Loot_Priority_Trunk_Industrial_Boss | Boss trunk (industrial) |
| `0x0055F9E0` | Container_Loot_Priority_Trunk_Prewar_Boss_NoWeaponsOrAmmo | Boss trunk (no weapons) |
| `0x004FD949` | Container_Loot_POI286_Trunk_Boss_TreasureMap | Treasure map boss trunk |

**ChanceEmpty Containers:**
| FormID | Container Type |
|---|---|
| `0x003D5B6A` | Container_Loot_ToolBox_ChanceEmpty |
| `0x003D5B6B` | Container_Loot_ToolBox_Large_ChanceEmpty |
| `0x003D5B6C` | Container_Loot_ToolChest_ChanceEmpty |
| `0x004351F3` | Container_Loot_CargobotWreckage_ChanceEmpty |
| `0x0039ED1D` | Container_Loot_Doctors_Bag_ChanceEmpty |
| `0x0036BA95` | Container_Loot_Golfbag_ChanceEmpty |
| `0x0018B218` | Container_Loot_DuffleBag_Cash_ChanceEmpty |

**Overseer's Cache Containers:**
| FormID | Cache Location |
|---|---|
| `0x003D7F48` | Overseer's Camp |
| `0x003D7F47` | Morgantown |
| `0x003D7F49` | Top of the World |
| `0x003D7F4A` | Free States |
| `0x003D7F4D` | Allegheny |
| `0x003D7F4E` | Camp McClintock |
| `0x003D7F4F` | Fort Defiance |
| `0x003D7F51` | Grafton |
| `0x003D7F52` | Sugar Grove / Nuke Silo |
| `0x003D7F53` | Spruce Knob / Nuke Silo |

### Container Economy Curves

**containers_chancenone.json** -- Primary container spawn probability (x = player level, y = chance nothing spawns):

| Level | Chance None | Effective Loot Rate |
|---|---|---|
| 0 | 0% | 100% (tutorial) |
| 1 | 75% | 25% |
| 5 | 50% | 50% |
| 10 | 35% | 65% |
| 15 | 25% | 75% |
| 20 | 20% | 80% |
| 25 | 15% | 85% |
| 30-100 | 10% | 90% |

**containers_maxcount.json** -- Maximum items per container:

| Level | Max Items |
|---|---|
| 0 | 0 |
| 1 | 1 |
| 5 | 1 |
| 10 | 2 |
| 15 | 2 |
| 20 | 3 |
| 25 | 4 |
| 30 | 6 |
| 40 | 7 |
| 100 | 10 |

**containers_item2_chancenone.json** (bonus 2nd item slot):

| Level | Chance None |
|---|---|
| 1 | 95% |
| 10 | 80% |
| 20 | 50% |
| 30 | 25% |
| 100 | 0% |

**containers_item3_chancenone.json** (bonus 3rd item slot):

| Level | Chance None |
|---|---|
| 1 | 97% |
| 10 | 90% |
| 20 | 65% |
| 30 | 40% |
| 100 | 0% |

**containers_recipe_chancenone.json** (recipe/plan spawn in containers):

| Level | Chance None |
|---|---|
| 1 | 99% |
| 10 | 95% |
| 20 | 80% |
| 30 | 50% |
| 100 | 0% |

---

## 8. Cap Stash Locations and Probabilities

### Cap Stash Tiers

| FormID | Tier | Contents |
|---|---|---|
| `0x003EE9E1` | Container_Loot_CapsStash_Standard | 4x caps (low) |
| `0x003EE9E0` | Container_Loot_CapsStash_Medium | 4x caps (medium) |
| `0x003EE9DE` | Container_Loot_CapsStash_High | 4x caps (high) |
| `0x003EE9DF` | Container_Loot_CapsStash_Jackpot | 4x caps (jackpot) |

Each tier's _Base list contains `[x4] :LVLO 0x0000000F` (caps currency, 4 rolls).

### Cap Stash Bonus Rolls

**LL_Loot_CapsStash** (`0x003EE9F2`) -- Standard cap stash bonus:
- 1% chance: bonus item `0x003EE9D7` (rare loot)
- 7.5% chance: bonus item `0x003EE9D6` (uncommon loot)

**LL_Loot_CapsStash_Bobblehead** (`0x003EE9F3`) -- Cap stash with bobblehead bonus:
- 2% chance: bonus item `0x003EE9D7` (rare loot, doubled from standard)
- 15% chance: bonus item `0x003EE9D6` (uncommon loot, doubled from standard)

### World-Placed Cap Stash

**LPI_Loot_CapsStash_Tin** (`0x00528649`) -- The classic bottle cap tin:
- Model: `props/bottlecaptin.nif`
- If player has Cap Collector perk (`0x6167C`): uses `LL_Loot_CapsStash_Bobblehead` (better odds)
- Otherwise: uses `LL_Loot_CapsStash` (standard odds)

---

## 9. Treasure Map Dig Sites

### Treasure Map Items (35+ maps)

BOOK records define treasure map items (FormIDs `0x0051B8A6` through `0x0051B8DE`):

TreasureMap02 through TreasureMap35, each a unique BOOK item that can be consumed to mark a dig site.

### Treasure Map Regional Rewards

| FormID | Reward List | Region |
|---|---|---|
| `0x0050CC2D` | LLS_TreasureMap_Reward_RegionCB_SF | Cranberry Bog / Savage Divide |
| `0x0050CC2E` | LLS_TreasureMap_Reward_RegionFF | The Forest (ForestFloodlands) |
| `0x0050CC2F` | LLS_TreasureMap_Reward_RegionMTN | Mountain (Savage Divide) |
| `0x0050CC30` | LLS_TreasureMap_Reward_RegionMTR | Ash Heap (MTR) |
| `0x0050CC31` | LLS_TreasureMap_Reward_RegionTV | Toxic Valley |

**Reward structure:**
- `LLS_TreasureMap_Reward_Base` (`0x0050CC2C`) selects region via `GetInCurrentLocation` conditions
- Each regional reward list contains `[x3]` rolls of region-appropriate loot
- `LL_Caps_TreasureMap` (`0x0050CC2A`) provides bonus caps (`0x003AE2A1`)
- Teammate reward: `LL_TreasureMap_TeammateReward` (`0x001A721E`)

### Treasure Map Drop Sources

| FormID | Source List | Contains |
|---|---|---|
| `0x0038B471` | LL_TreasureMap | Master drop list for treasure maps |
| `0x003D0CD5` | LLS_TreasureMap_FF | Forest region maps (`[x4]` of `0x0051B7A2`) |
| `0x003D0CD6` | LLS_TreasureMap_TV | Toxic Valley maps (`[x4]` of `0x0051B7A2`) |
| `0x003D0CD7` | LLS_TreasureMap_MTR | Ash Heap maps |
| `0x003D0CD8` | LLS_TreasureMap_CB_SF | Cranberry Bog maps (`[x3]` of `0x0051B8BA`) |
| `0x003D0CD9` | LLS_TreasureMap_MTN | Mountain maps |

---

## 10. Rare Item Spawn Locations

### Alien Blaster

| FormID | List | Source |
|---|---|---|
| `0x00684972` | LL_Weapon_Simple_Ranged_AlienBlasterDailyOps | Daily Ops reward |
| `0x0062F3C3` | LL_Weapon_Poison_Ranged_AlienBlaster | Poison variant |
| `0x0062F3C2` | LL_Weapon_Cryo_Ranged_AlienBlaster | Cryo variant |
| `0x00631E0D` | LL_Weapon_Simple_Ranged_AlienRifle | Alien Rifle (Invaders event) |
| `0x0082068F` | crLLI_Burn_BountyHunt_Weapon_Ranged_AlienBlaster | Burning Springs bounty |
| `0x00621A93` | SCORE_S8_LL_AlienBlaster_ZetasRevenge | Zeta's Revenge (Scoreboard S8) |
| `0x00684BAC` | LL_Ammo_AlienBlaster_DailyOps | Alien blaster ammo (Daily Ops) |
| `0x00633458` | LLS_Contextual_Ammo_AlienBlaster | Contextual ammo drop |

### Other Rare Items

| FormID | List | Item |
|---|---|---|
| `0x004277E2` | LPI_Weapon_Ranged_HarpoonGun | Harpoon gun world spawn |
| `0x0076855B` | LPI_Weapon_Ranged_Blackpowder_Rifle_01 | Black powder rifle |
| `0x006873BF` | LPI_Weapon_Ranged_ThirstZapper | Thirst Zapper |
| `0x004010E3` | LPI_SheepsquatchQuill_100 | Sheepsquatch quill (100%) |

---

## 11. The LVLI (Leveled Item List) System

### How Loot Tables Work

Each LVLI record contains:
- **OBND**: Object bounds (for world-placed items)
- **LVLO**: Leveled list output entries (FormID references to items or other LVLIs)
- **CTDA**: Condition data (GetRandomPercent, GetInCurrentLocation, HasPerk, etc.)
- **MODL**: 3D model path (for world-placed LPI items)

### LVLI Resolution Chain

When the game evaluates a loot container:

```
Container → Container_Loot_Priority_X → LL_Loot_Category → LLS_SubCategory → Actual Item
```

Example: A medkit container:
```
Container_Loot_Priority_Medkit (0x0006D4AC)
  → LL_Loot_Medical
    → LLS_Stimpak
      → Stimpak item
    → LLS_RadAway
      → RadAway item
    → LLS_RadX (conditional: GetRandomPercent <= X)
      → RadX item
```

### Conditional Spawning (CTDA)

Many LVLI entries use conditions:
- `GetRandomPercent <= X` -- X% chance to include this entry
- `GetInCurrentLocation == FormID` -- Only spawn in specific location
- `HasPerk == FormID` -- Player perk check (e.g., Cap Collector for cap stashes)
- `GetGlobalValue == X` -- Check a global variable (event toggles)

Example from `RD01_LLS_Raids_Rewards_SuperStimpaks`:
```
:LVLO 0x00117DF9  (Super Stimpak)
:CTDA GetRandomPercent <= 25.000000  (25% for first)
:LVLO 0x00117DF9  (Super Stimpak again)
:CTDA GetRandomPercent <= 50.000000  (50% for second)
```
Result: ~25% chance of 1 Super Stimpak, ~12.5% chance of 2.

### The `[xN]` Multiplier

Records show `[x3]` or `[x4]` prefixes on LVLO entries, meaning the game rolls that entry N times. Example: `[x4] :LVLO 0x0000000F` = roll caps 4 times.

---

## 12. Spawn Chance Globals

### Direct Spawn Chance Controls (17 SpawnChance_ globals)

| FormID | Global Name | Value | Effect |
|---|---|---|---|
| `0x008B1D61` | SpawnChance_Cnone_PlasmaCasterModPlans | 95.0 | 95% chance of NO plasma caster mod plans (5% drop) |
| `0x008AA954` | SpawnChance_Cnone_RarePlayerTitle | 95.0 | 95% chance of no rare title (5% drop) |
| `0x0089EA90` | SpawnChance_Cnone_ActivityCampTitle | 75.0 | 75% chance of no camp title (25% drop) |
| `0x00829437` | SpawnChance_Cnone_GatlingPlasmaModPlans | 95.0 | 95% cnone (5% drop) |
| `0x0085928D` | SpawnChance_RadhogAlpha | 10.0 | 10% chance radhog alpha spawns |
| `0x0086AEEB` | RA_PartyCrasherSpawnChance_Default | 0.34 | 34% party crasher spawn |
| `0x00869A34` | RA_PartyCrasherSpawnChance_Bigfoot | 0.33 | 33% Bigfoot variant |
| `0x0062038A` | Spooky_ScorchedSpawnChance | 10.0 | 10% spooky scorched (seasonal) |
| `0x005C4F13` | E02A_Meat_SpawnChance | 25.0 | 25% Meat Week spawn |
| `0x005A7539` | TreasureHunt_SpawnChance | 0.0 | **DISABLED** (treasure hunt off) |
| `0x0059B7D4` | Festive_ScorchedSpawnChance | 0.0 | **DISABLED** (holiday off) |
| `0x00621C36` | LCP_E07A_Mothman_SpecialEncounter_SpawnChance | 0.0 | **DISABLED** |
| `0x0043348C` | ScorchedStatueSpawnChance | 101.0 | **ALWAYS** (>100 = guaranteed) |
| `0x0058E6F6` | COMP_AllySpawnChance_Standard | 10.0 | 10% companion ally spawn |
| `0x0058E6F7` | COMP_AllySpawnChance_Always | 100.0 | 100% guaranteed ally |
| `0x0058E6F8` | COMP_AllySpawnChance_High | 50.0 | 50% high-priority ally |
| `0x00596566` | COMP_AllySpawnChance_Denizen_Standard | 10.0 | 10% denizen companion |

### Event Drop Rate Toggles (ChanceNone / DropRate globals)

Key event reward tuning knobs (197 total):

| FormID | Global | Value | Notes |
|---|---|---|---|
| `0x005D080D` | DailyOps_Rewards_ChanceNone_Rare | varies | Daily Ops rare reward chance |
| `0x0065FF7A` | Expedition_WeeklyRewards_ChanceNone_Rare | varies | Expedition rare reward |
| `0x005CB50C` | E02A_Meatweek_LLS_RareRewards_ChanceNone_Best | varies | Meat Week best reward |
| `0x005CB50B` | E02A_Meatweek_LLS_RareRewards_ChanceNone_Good | varies | Meat Week good reward |
| `0x005CB50D` | E02A_Meatweek_LLS_RareRewards_ChanceNone_Bad | varies | Meat Week bad reward |
| `0x005CB50E` | E02A_Meatweek_LLS_FireworksReward_ChanceNone | varies | Meat Week fireworks |
| `0x0085E2C2` | LTT_IncreasedFasnachtGlowingMaskDrop_ChanceNoneDropRate | varies | Fasnacht glowing mask |
| `0x0083E311` | LCP_E07B_Invaders_GeneralZetaGlowMask_ChanceNoneDropRate | varies | Invaders glow mask |
| `0x0085DB74` | LTT_UMineItLegendary_ChanceNoneDropRate | varies | Uranium Mine legendary |
| `0x0085DB6F` | LTT_UMineItBobbleHead_ChanceNoneDropRate | varies | Uranium Mine bobblehead |
| `0x0085DB75` | LTT_UMineItFlux_ChanceNoneDropRate | varies | Uranium Mine flux |
| `0x008553A1` | LTT_MothmanMutatedPartyPacks_ChanceNoneDropRate | varies | Mothman party packs |
| `0x008553A2` | LTT_GruntHuntBonusStarDrops_ChanceNoneDropRate | varies | Grunt Hunt bonus stars |
| `0x007DC633` | Fishing_BaitLootChanceNone | varies | Fishing bait find rate |

### Collectron Chance None (ATX_CNone_)

Every Atom Shop Collectron robot has tunable spawn rates for each rarity tier:

| Collectron | SuperCommon | Uncommon | Rare | SuperRare |
|---|---|---|---|---|
| Electronics | `0x00622F77` | `0x00622F78` | `0x00622F76` | `0x006237DF` |
| BoS | `0x005C5E19` | `0x005C5E1A` | (n/a) | (n/a) |
| Auto Parts | `0x0060DF50` | `0x0060DF51` | `0x0060DF52` | (n/a) |
| Evidence Collection | `0x008AD798` (0.0) | (n/a) | (n/a) | `0x008AD797` (97.0) |
| Peppino | (n/a) | (n/a) | (n/a) | `0x008A52C2` (95.0) |
| Junkyard Electronics | `0x006667F2` | `0x006667F1` | `0x006667F3` | `0x006667F4` |

---

## 13. Regional Loot Differences

### Confirmed Regional Loot Pools

**Yes, different regions have different loot pools.** This is implemented at two levels:

#### Level 1: Location-Conditioned LPI Records

LPI records use `GetInCurrentLocation` conditions to vary spawns by location. Example: `LPI_Loot_Bobbleheads` has a special entry for location `0x4FA7AA` (a specific POI) that gives only Agility bobbleheads.

#### Level 2: Explicit Regional LVLI Records

The Skyline Valley and Burning Springs DLCs introduced the most explicit regional loot differentiation:

| Category | Skyline Valley | Burning Springs |
|---|---|---|
| Armor Recipes | `LL_Recipes_Armor_RegionSkylineValley` | `LL_Recipes_Armor_RegionBurningSprings` |
| Melee Weapon Recipes | `LLS_Recipes_Weapons_Melee_RegionSkylineValley` | `LLS_Recipes_Weapons_Melee_RegionBurningSprings` |
| Ranged Weapon Recipes | `LLS_Recipes_Weapons_Ranged_RegionSkylineValley` | `LLS_Recipes_Weapons_Ranged_RegionBurningSprings` |
| PA Recipes | `LL_Recipes_PowerArmor_RegionSkylineValley` | `LL_Recipes_PowerArmor_RegionBurningSprings` |
| PA Mods | `LL_Mods_PowerArmor_RegionSkylineValley` | `LL_Mods_PowerArmor_RegionBurningSprings` |
| Helmet/Clothes | `LLS_Recipes_Clothes_Helmets_RegionSkylineValley` | `LLS_Recipes_Clothes_Helmets_RegionBurningSprings` |
| Armor Mods | `LL_Recipes_Mods_Armor_RegionSkylineValley` | `LL_Recipes_Mods_Armor_RegionBurningSprings` |

#### Level 3: Treasure Map Regional Rewards

Treasure maps use explicit region checks (see Section 9) to give region-appropriate rewards.

#### Level 4: Fishing Regional Pools

Each region has unique fishing pools including nuke-weather variants:
- `Fishing_LLS_Ash_*` (Ash Heap)
- `Fishing_LLS_Cranberry_*` (Cranberry Bog)
- `Fishing_LLS_SavageDivide_*`
- `Fishing_LLS_Mire_*`
- `Fishing_LLS_Toxic_*` (Toxic Valley)
- `Fishing_LLS_Skyline_*` (Skyline Valley)
- `Fishing_LLS_BurningSprings_*` (Burning Springs)

Each has Common, Improved, and Superb baited variants, plus NukeWeather variants.

---

## 14. Nuke Zone Flora Mutation Locations

### How Nuke Zone Flora Works

When a nuke hits a zone, normal flora is replaced with flux-producing variants. The system uses three economy curves:

**flora_nukeswap_chancenone.json** -- Whether flora transforms into flux:
| Distance from nuke center | Chance None | Transform Rate |
|---|---|---|
| 0 (ground zero) | 100% | 0% (too close, destroyed) |
| 1+ | 0% | 100% (all flora transforms) |

**Key finding:** At distance 0, nothing transforms (ground zero is too hot). At distance 1+, ALL eligible flora transforms into flux variants. The swap is binary -- once you're in the nuke zone but not at ground zero, every harvestable plant becomes flux.

**flora_nukedistance_chancenone.json** -- Flora survival by distance from blast center:
| Distance | Chance None | Survival Rate |
|---|---|---|
| 0 | 100% | 0% (destroyed) |
| 1 | 95% | 5% |
| 2 | 85% | 15% |
| 3 | 75% | 25% |
| 4 | 50% | 50% |
| 100 | 0% | 100% |

**Key finding:** Flora closer to the blast center is more likely to be destroyed entirely. At distance 4+, half survive, and by the edge of the zone nearly all survive and become flux.

### Flux Types

From MISC_records.txt, flux items include stable variants:
- `0x008B0965` PTS_Bulk_Scrapball_StableFlux (Pitt scrappable)
- Flux containment models: `props/consumables/pitt/pitt_fluxcontainment_01.nif`
- BoS Flux Sensors: `props/bosfluxsensor/bosfluxsensor.nif`

### Nuke Flora Scrap Reward

`0x0049A072` QuestReward_LLS_NukeFlora_Scrap -- The scrap reward for harvesting nuked flora.

---

## LPI Spawn Economy Curves

### World-Placed Item Spawn Curves

**lpi_spawn_chancenone.json** -- Master LPI spawn probability:

| Level | Chance None | Spawn Rate |
|---|---|---|
| 0 | 100% | 0% |
| 1 | 95% | 5% |
| 5 | 90% | 10% |
| 10 | 75% | 25% |
| 15 | 60% | 40% |
| 20 | 40% | 60% |
| 25 | 25% | 75% |
| 30-99 | 10% | 90% |
| 100 | 0% | 100% |

**lpi_rare_chancenone.json** -- Rare LPI spawn probability:

| Level | Chance None | Spawn Rate |
|---|---|---|
| 0 | 100% | 0% |
| 1 | 99% | 1% |
| 5 | 99% | 1% |
| 10 | 97% | 3% |
| 15 | 95% | 5% |
| 20 | 90% | 10% |
| 25 | 80% | 20% |
| 30 | 5% | 95% (massive jump!) |
| 99 | 5% | 95% |
| 100 | 0% | 100% |

**CRITICAL FINDING:** Rare item spawn rates have a massive cliff at level 30 -- going from 20% spawn rate at level 25 to 95% at level 30. This means level 30+ players see dramatically more rare items than level 29 players. This is likely intentional to reward players who reach the endgame threshold.

**lpi_fusioncore_chancenone.json** -- Fusion core spawn:
| Level | Chance None |
|---|---|
| 0 | 100% |
| 1 | 80% (20% spawn) |
| 2 | 25% (75% spawn) |

Fusion cores are readily available even at low levels.

**lpi_packagedfood_chancenone.json** -- Identical to lpi_spawn_chancenone.

**ammo_lpi_chancenone.json** -- Ammo world spawn: identical to flora_harvestable curve.

---

## Generated Map Data Files

### Previously Extracted (with XYZ coordinates from esmdump -t -i REFR)

A prior session already ran esmdump in TSV mode against the actual SeventySix.esm and extracted the full REFR dataset. These files contain actual world coordinates (X, Y, Z) for placed references:

| File | Records | Description |
|---|---|---|
| `map_data/all_refr.tsv` | 5,105,349 | **Complete placed reference database** -- every REFR in the game with XYZ coords |
| `map_data/bobbleheads.tsv` | 1,102 | All bobblehead spawn locations with coordinates |
| `map_data/magazines.tsv` | 1,972 | All magazine spawn locations with coordinates |
| `map_data/power_armor.tsv` | 838 | Power armor workbenches and chassis spawns with coordinates |
| `map_data/cap_stashes.tsv` | 339 | Cap stash tin locations with coordinates |
| `map_data/fusion_cores.tsv` | 289 | Fusion core spawn locations with coordinates |
| `map_data/rare_nuka_colas.tsv` | 224 | Rare Nuka-Cola spawn locations with coordinates |
| `map_data/treasure_maps.tsv` | 142 | Treasure map dig sites and placed maps with coordinates |
| `map_data/breakable_walls.tsv` | 3,010 | Destructible wall/board locations with coordinates |
| `map_data/bobblehead_markers.dds` | (64MB) | Marker overlay image -- bobblehead locations on map |
| `map_data/bobblehead_markers.txt` | (marker def) | fo76utils marker definition for bobbleheads |
| `map_data/highvalue_markers.dds` | (64MB) | Marker overlay image -- high-value items on map |
| `map_data/highvalue_markers.png` | (91KB) | PNG version of high-value marker overlay |
| `map_data/highvalue_markers.txt` | (marker def) | Marker definitions: bobbleheads (green), cap stashes (yellow), fusion cores (cyan), breakable walls (red), PA workbenches (magenta) |

**TSV coordinate format:** `Group  Record  FormID  EDID  FULL  DESC  RNAM  BaseFormID (EditorID)  [CellFormID (CellName)]  X  Y  Z  RotX  RotY  RotZ`

### Extracted This Session (LVLI analysis without coordinates)

| File | Records | Description |
|---|---|---|
| `map_data/spawn_chance_globals.tsv` | 144 | All spawn chance/ChanceNone globals with values |
| `map_data/lpi_world_spawns.tsv` | 755 | All LPI world-placed spawn point type definitions with sub-entries |
| `map_data/flora_leveled_lists.tsv` | 146 | All flora leveled list definitions |
| `map_data/container_loot_lists.tsv` | 125 | Container loot configurations (what each container type drops) |
| `map_data/workshop_production.tsv` | 70 | Workshop resource production list definitions |

---

## Tooling Notes

### fo76utils markers Tool

The `markers` tool at `~/ai-drive/gamecryptids/tools/fo76utils/markers` generates map marker overlay images from ESM data. It has already been used to produce:
- `bobblehead_markers.dds` -- Green dots at every bobblehead spawn
- `highvalue_markers.dds` / `.png` -- Multi-colored overlay with bobbleheads, cap stashes, fusion cores, breakable walls, and PA workbenches

The marker definition format uses shape+color codes (e.g., `0x4FFF00FF` = circle, full opacity, green):
```
FormID  MarkerType  ShapeColor  MipLevel  [Priority]
```

### esmdump TSV Mode

The full REFR extraction has already been completed via `esmdump -t -i REFR`, producing `all_refr.tsv` (757MB, 5.1M records). This contains XYZ coordinates for every placed object in the game. Specific item type extractions (bobbleheads, magazines, etc.) were filtered from this master file.

---

## Key Findings Summary

1. **Level 30 is the critical threshold** -- Rare item spawns jump from 20% to 95% at level 30, and containers reach near-maximum fill rates.

2. **Flora is guaranteed at level 100** -- The harvestable curve hits 0% chance-none at level 100, meaning every plant node will have items.

3. **Nuke zone flora is binary** -- At distance 1+ from ground zero, ALL eligible flora transforms. At distance 0, everything is destroyed. The optimal flux farming ring is distance 2-4 from the blast center.

4. **Cap stashes have hidden bonus rolls** -- The Cap Collector perk doubles bonus item chances from 1%/7.5% to 2%/15%.

5. **Seasonal events use server-side toggles** -- SpawnChance globals for Festive Scorched, Treasure Hunt, and Mothman events are set to 0.0 when inactive, switched on server-side during events.

6. **Regional loot is real but limited** -- Base game regions share most loot pools. DLC zones (Skyline Valley, Burning Springs) have fully separate recipe/mod pools. Fishing has the most granular regional differentiation.

7. **The LVLI system is deeply nested** -- Some loot chains go 4-5 levels deep (Container → Priority list → Category → Sub-category → Item), with conditions at each level.

8. **755 unique world spawn point types** -- Each LPI represents a category of item that can appear at map coordinates placed by level designers.
