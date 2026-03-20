# Fallout 76 CAMP & Workshop Building System Internals

Deep dive into the internal mechanics governing CAMP placement, Workshop claiming, budget systems, turret scaling, crop timers, resource extraction, Collectron rates, pet systems, attack formulas, ally mechanics, and cut content.

---

## 1. Budget System

### Game Settings (GMST)

| Setting | FormID | Value | Purpose |
|---------|--------|-------|---------|
| `fWorkshopBudgetLightCost` | 0x003F237A | 1.0 | Budget cost per light source |
| `fWorkshopBudgetSplineCost` | 0x00452A6F | 0.25 | Budget cost per wire/spline connection |
| `fWorkshopBudgetCategoryNavmesh` | 0x004FBDC3 | 2.0 | Budget cost multiplier for navmesh-generating objects |
| `fWorkshopBudgetCategoryActor` | 0x003E3A3A | 9.0 | Budget cost multiplier for actor objects (turrets, allies, pets) |
| `fWorkshopBudgetCategoryContainer` | 0x004F5674 | 0.0 | Budget cost for container objects (zero = free) |

### Budget Actor Values

| ActorValue | FormID | Purpose |
|------------|--------|---------|
| `WorkshopBudgetLocation` | 0x0033D523 | Stores the budget baseline for a specific location |
| `WorkshopBudgetObjectMultiplier` | 0x0033D522 | Per-object multiplier (used to override individual object costs) |

### Default Objects (Budget Control)

| DFOB | FormID | Purpose |
|------|--------|---------|
| `WorkshopBudgetMultiplier_DO` | 0x0033D525 | Global multiplier applied to all budget calculations |
| `WorkshopBudgetBaseline_DO` | 0x0033D524 | Base budget capacity for workshops |

### How Budget Is Calculated

From `workshopscript.psc`:
- Workshop inventory refresh uses `refreshInventoryWorkshopBudgetMult = 0.5` to scale component generation to budget
- Base component count: 200 (`refreshInventoryBaseComponentCount`)
- Minimum component count: 200 (`refreshInventoryMinComponentCount`)
- Refresh timer: 1800 seconds (30 minutes) (`refreshInventoryTimeSeconds`)

**Budget cost hierarchy**: Actors cost 9x the baseline, navmesh objects cost 2x, lights cost 1x, splines/wires cost 0.25x, and containers are free. The `WorkshopBudgetObjectMultiplier` AV can zero out specific items (used for tamed animals to make them budget-free).

### CAMP Workshop Count Globals

Each placeable object has paired globals tracking placement limits:
- `WorkshopCount_[ItemName]` -- limit in public workshops
- `WorkshopCount_[ItemName]_CAMP` -- limit in CAMPs (often identical or slightly different)

Example observed limits from GLOB FLTV values:
- `ATX_WorkshopCount_Explosives_CAMP`: 25
- `WorkshopCount_ScrapCubes_CAMP`: 25
- Prefab kits: typically 1 per CAMP
- Collectrons: typically 1 per CAMP (separate limit per skin variant)

---

## 2. CAMP Placement Rules

### Core Settings

| Setting/Global | FormID | Value | Purpose |
|----------------|--------|-------|---------|
| `uMaxCampKits` | 0x00019472 | 2 | Maximum number of CAMP kits a player can hold |
| `fCampKitRegenTimeInMinutes` | 0x00128834 | 60.0 | CAMP kit regeneration time (1 hour) |
| `CampRadius` | 0x00411B6C | 1500.0 | CAMP build radius in game units (~29.3 meters) |
| `fWorkshopBuildHeight` | 0x003D6559 | 1900.0 | Maximum build height in game units |
| `fWorkshopVisibleBorderHeight` | 0x0001C16C | 128.0 | Height of visible CAMP border walls |
| `fWorkshopHUDRadiusBuffer` | 0x003F2A2E | 1500.0 | Buffer distance for HUD display of CAMP boundaries |

### CAMP Kit Mechanics (from addcampkitsscript.psc)

The `AddCampKitsScript` is an ActiveMagicEffect that adds to the player's `CampKits` actor value. CAMP kits are treated as a consumable AV resource:
- Maximum 2 kits at any time
- 60-minute regeneration per kit
- Managed through magic effect magnitude

### CAMP Slot System

The game supports multiple CAMP slots per account:

| ENTM | FormID | Description |
|------|--------|-------------|
| `ATX_ENTM_Account_CAMP_Slot_01` | 0x0060DD2B | CAMP Slot 1 |
| `ATX_ENTM_Account_CAMP_Slot_02` | 0x0060DD2D | CAMP Slot 2 |
| `ATX_ENTM_Account_CAMP_Slot_03` | 0x0060DD2E | CAMP Slot 3 |
| `ATX_ENTM_Account_CAMP_Slot_04` | 0x0060DD2F | CAMP Slot 4 |
| `ATX_ENTM_Account_CAMP_Slot_05` | 0x0060DD30 | CAMP Slot 5 |
| `ATX_ENTM_Account_CAMP_Slot_06` | 0x0060DD31 | CAMP Slot 6 |
| `ATX_ENTM_Account_CAMP_Slot_07` | 0x0060DD32 | CAMP Slot 7 |
| `ATX_ENTM_Account_CAMP_Slot_08` | 0x0060DD33 | CAMP Slot 8 |

All slots share the same thumbnail (`atx_account_camp_slot.dds`). CAMP slots are account-level entitlements (ATX prefix), meaning they are purchased/unlocked independently of character.

### CAMP Build Constraints

- **Radius**: 1500 game units (~29.3m) from the CAMP device
- **Height limit**: 1900 game units above the placement point
- **Contest radius**: 512.0 units (`fWorkshopContestRadius`) -- the radius within which a workshop becomes contested
- **Contested height**: 256.0 units (`fWorkshopContestedHeight`)
- **State transition delta**: 2.0 (`fWorkshopStateTransitionDelta`) -- hysteresis for state changes

---

## 3. Workshop States & Claiming

From `workshopscript.psc`, workshops have the following states:

| State | Value | Description |
|-------|-------|-------------|
| `WorkshopState00Blocked` | 0 | Inaccessible |
| `WorkshopState01Unowned` | 1 | No owner, enemies present |
| `WorkshopState02Owned` | 2 | Player-owned |
| `WorkshopState03Contested` | 3 | Under attack |
| `WorkshopState04Claimable` | 4 | Ready to claim |
| `WorkshopState05Claiming` | 5 | Claim in progress |
| `WorkshopState06Claimed` | 6 | Fully claimed |
| `WorkshopState10PublicContested` | 10 | Public workshop contested |
| `WorkshopState11PublicClaiming` | 11 | Public workshop being claimed |

### Workshop Properties

- `EnableAutomaticPlayerOwnership` (default True): Workshop auto-becomes usable when location is cleared
- `AllowAttacks` (default True): Set to False to prevent ALL random attacks
- `CustomClaimedStoryKeyword`: Per-workshop keyword sent to Story Manager on claim
- `WorkshopPlayerClaimRecipes`: FormList of recipes awarded to player when claiming a workshop

---

## 4. Turret Damage & Health Scaling (Curve Tables)

All turret stats scale with **encounter zone level** (x = level, y = stat value). Data from `workshop/defenses/` curve tables.

### Turret Damage Per Shot (by level)

| Turret Type | Lv2 | Lv10 | Lv20 | Lv50 | Lv75 | Lv100 |
|-------------|-----|------|------|------|------|-------|
| **Machine Gun** | 7 | 8 | 10 | 18 | 28 | 46 |
| **Machine Gun Heavy** | 9 | 11 | 14 | 24 | 38 | 62 |
| **Laser** | 11 | 13 | 16 | 28 | 44 | 71 |
| **Laser Heavy** | 15 | 17 | 21 | 36 | 57 | 93 |
| **Shotgun** | 7 | 8 | 10 | 18 | 28 | 46 |
| **Missile Launcher** | 20 | 25 | 30 | 52 | 82 | 133 |
| **Military** | 20 | 25 | 30 | 52 | 82 | 133 |

### Turret Health (by level)

| Turret Type | Lv2 | Lv10 | Lv20 | Lv50 | Lv75 | Lv100 |
|-------------|-----|------|------|------|------|-------|
| **Machine Gun** | 16 | 30 | 50 | 125 | 226 | 398 |
| **Machine Gun Heavy** | 23 | 44 | 73 | 183 | 330 | 579 |
| **Laser** | 23 | 44 | 73 | 183 | 320 | 579 |
| **Laser Heavy** | 32 | 61 | 101 | 251 | 437 | 789 |
| **Shotgun** | 16 | 30 | 50 | 125 | 226 | 398 |
| **Missile Launcher** | 32 | 61 | 101 | 251 | 437 | 789 |
| **Military** | 32 | 61 | 101 | 251 | 437 | 789 |
| **Spotlight** | 16 | 30 | 50 | 125 | 226 | 398 |
| **Spotlight Wall** | 16 | 30 | 50 | 125 | 226 | 398 |

### Trap Damage (Flat -- Does Not Scale)

| Trap Type | Damage |
|-----------|--------|
| **Flamethrower** | 25 (flat, all levels) |
| **Tesla Arc** | 5 (flat, all levels) |

### Turret Health Multiplier

`fWorkshopLevelHealthMult` = 0.1 -- turret health scales at 10% of the curve table value per level (applied as a multiplier to the base health curve).

### Turret Targeting

- **Spotlight turrets** (`workshopspotlightturretscript.psc`): Use `WorkshopLinkSpotlightTarget` keyword to create linked references to their target. They illuminate targets for other turrets.
- **Trap guns** (`workshoptrapgun.psc`): Fire weapon arrays (`weaponData[]`) with configurable firing time (default 1.0s between shots) and max fire count (default 20 shots per trigger).

---

## 5. Crop Growth & Food Production

### System Design

From `workshopparentscript.psc`:
- `updateIntervalGameHours = 24.0` -- the daily update cycle runs every 24 in-game hours
- `maxFoodProductionPerFarmer = 10` -- each assigned farmer can produce a maximum of 10 food units per cycle
- `dailyUpdateSpreadHours = 12.0` -- daily updates are spread across 12 hours to avoid server spikes

### Flora Damage System

`WorkshopFloraDamageHelperScript` passes damage received to linked flora objects, meaning crops can be damaged during attacks. The damage helper is attached to invisible collision boxes around plants.

### Workshop Repair

`fWorkshopRepairComponentMult` = 0.25 -- repairing damaged objects (including crops) costs 25% of the original material requirements.

---

## 6. Workshop Resource Extraction Rates

### Public Workshop Extractors

Workshop resource extractors are categorized by TRNS (Transform) records:

| Extractor Type | FormID | Description |
|----------------|--------|-------------|
| `workshop_ResourceCollector_Minerals` | 0x0002F9F6 | Mineral extractor (aluminum, copper, gold, lead, silver, steel, titanium) |
| `workshop_ResourceCollector_Fertilizer` | 0x0014CAB4 | Fertilizer collector |
| `workshop_ResourceCollector_Scavenge` | 0x0014CAB5 | Scavenging station |
| `DLC01workshop_ResourceScanner` | 0x0010FC2C | Resource scanner |

### Cosmetic Extractor Skins

These are cosmetic ATX/SCORE variants that share the same extraction logic:
- `ATX_ENTM_CAMP_Machinery_Resource_Extractor_VaultTec` (0x007E6F25)
- `SCORE_S22_ENTM_CAMP_Machinery_Resource_Extractor_GarrahanCompanyExt` (0x00839573)
- `ATX_ENTM_CAMP_Machinery_Resource_Extractor_Enclave` (Possum Miner badge unlock, 0x0064EF36)

### Workshop Inventory Refresh System

From `workshopscript.psc`:
- Refresh interval: 1800 seconds (30 minutes)
- Base component count per refresh: 200
- Budget scaling multiplier: 0.5 (higher budget = more components)
- Minimum components per refresh: 200

---

## 7. Collectron Collection Rates & Item Pools

### Production Interval (ResourceProductionIntervalHours)

| Collectron Variant | FormID | Interval (hours) | Items per hour |
|-------------------|--------|-------------------|----------------|
| **Standard (Junk mode)** | 0x00555DAF | 0.170 (~10.2 min) | ~5.9 |
| **Standard (Scrap mode)** | 0x00555DAE | 0.170 (~10.2 min) | ~5.9 |
| **FETCH (Electronics/Junk)** | 0x006667F0 | 0.080 (~4.8 min) | ~12.5 |
| **FETCH (Electronics)** | 0x00622F79 | 0.080 (~4.8 min) | ~12.5 |
| **Gold Scrap** | 0x005F0D27 | 0.080 (~4.8 min) | ~12.5 |
| **Morbid Well** | 0x00662E6D | 0.120 (~7.2 min) | ~8.3 |
| **Evidence Collection Assistant** | 0x008B2022 | 0.150 (~9.0 min) | ~6.7 |
| **Peppino** | 0x008A52C3 | 0.150 (~9.0 min) | ~6.7 |
| **Liberated** | 0x0084CCA5 | 0.150 (~9.0 min) | ~6.7 |
| **BivBev** | 0x007C7299 | 0.170 (~10.2 min) | ~5.9 |
| **Radstalker Field Dressing** | 0x0068E77C | 0.170 (~10.2 min) | ~5.9 |
| **Tree Sap Bucket** | 0x0067F3AD | 0.170 (~10.2 min) | ~5.9 |
| **Slocum's Joe Coffee** | 0x0067ADC7 | 0.170 (~10.2 min) | ~5.9 |
| **Cornbot** | 0x0085CE4F | 0.170 (~10.2 min) | ~5.9 |
| **RoboButler** | 0x00836461 | 0.170 (~10.2 min) | ~5.9 |
| **Scoutmaster** | 0x00771DC5 | 0.170 (~10.2 min) | ~5.9 |

### Collectron Junk/Scrap Rarity Weights

Economy globals control rarity distribution for junk/scrap modes:

| Rarity | Junk Global | Scrap Global |
|--------|-------------|--------------|
| Super Common | `ATX_CNone_Collectron_Junk_SuperCommon_ECON` | `ATX_CNone_Collectron_Scrap_SuperCommon_ECON` |
| Uncommon | `ATX_CNone_Collectron_Junk_UnCommon_ECON` | `ATX_CNone_Collectron_Scrap_Uncommon_ECON` |
| Common | -- | `ATX_CNone_Collectron_Scrap_Common_ECON` |
| Rare | `ATX_CNone_Collectron_Junk_Rare_ECON` | `ATX_CNone_Collectron_Scrap_Rare_ECON` |
| Very Rare | -- | `ATX_CNone_Collectron_Scrap_VeryRare_ECON` |

### Other Resource Producers

| Producer | Interval (hours) | Notes |
|----------|-------------------|-------|
| AmmOMatic (10mm) | 0.003600 (~13 sec) | Extremely fast, tiny amounts |
| AmmOMatic (.308) | 0.003600 | Same rate all ammo types |
| AmmOMatic (.44) | 0.003600 | |
| AmmOMatic (.45) | 0.003600 | |
| AmmOMatic (5.56) | 0.003600 | |
| AmmOMatic (Shotgun) | 0.003600 | |
| Survival Cache | 0.170 | |
| Strange Curio Cabinet | 0.170 | |
| Crashed Cargo Bot | 0.170 | |
| Shredder | - | Resource production rate set separately |
| Toxic Bob | - | Resource production rate set separately |
| Motorized Butter Churn | - | Cooking oil |
| Apple Tree | - | Apples |
| Boiler | - | Boiled water |
| Mirelurk Steamer | - | Food items |
| Mothman Nest | - | Eggs |
| Birthday Cake | - | Cake |
| Dirty Water Well | - | Dirty water |
| Cooler | - | Purified water |
| Counterfeit Cap Press | - | Bottle caps |
| Deathclaw Slow Roaster | - | Cooked food |
| Nodding Donkey | - | Oil |
| Red Rocket Dumpster | - | Junk |
| Fish Trap | - | Food |
| Live Bait Barrel | - | Food |
| Meat Cooker | - | Food |
| Pumpkin Pie | - | Food |
| Wall-mounted Oven | - | Food |
| Spice Rack | - | Spices |
| RockerBox | - | Unknown resource |
| Paint Can Generator | - | Paint/crafting resources |

---

## 8. Workshop Defense vs Attack Scaling

### Attack Timer System

From `workshopcampscript.psc` and `workshopscript.psc`:

**CAMP Attacks:**
- Minimum player level for attacks: 6 (`MinLevelForAttack`)
- Min time between attacks: 0.16 days (3.84 hours / ~4 hours)
- Max time between attacks: 0.32 days (~7.68 hours / ~8 hours)
- Attack timer check interval: 0.01 days (~14.4 minutes)

**Public Workshop Attacks:**

| Global | FormID | Value | Purpose |
|--------|--------|-------|---------|
| `WorkshopNextAttackMinDays` | 0x001A05CF | 0.040 | Minimum days before next attack (~58 min) |
| `WorkshopNextAttackDecrementPerCollectorDays` | 0x003E8634 | 0.010 | Each resource extractor decreases time to next attack |
| `WorkshopNextAttackDecrementWhenClaimedDays` | 0x00434DC5 | 0.020 | Claiming a workshop decreases time to next attack |

**Attack decrement mechanics** from `workshopscript.psc`:
- `decrementNextAttackTimerSecondsMax = 180.0` -- max seconds to decrement attack timer
- `decrementNextAttackTimerSecondsMin = 90.0` -- min seconds to decrement

### Attack Wave System (from sq_masterscript.psc)

The swarm/attack system uses `swarmType` structs with configurable parameters:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `minWaves` | 1 | Minimum number of attack waves |
| `maxWaves` | 3 | Maximum waves (hard cap at 5) |
| `bossChance` | 0.5 (50%) | Chance of a boss wave at the end |
| `bossGiantChance` | 0.25 (25%) | Chance the boss is a giant variant (Behemoth, Mirelurk Queen, etc.) |
| `minActorsPerWave` | 5 | Minimum enemies per wave |
| `maxActorsPerWave` | 10 | Maximum enemies per wave |
| `minDifficultyPerWave` | 0 | Minimum difficulty scaling |
| `maxDifficultyPerWave` | 4 | Maximum difficulty scaling |
| `minDelayTime` | 0.0 | Minimum delay before wave starts |
| `maxDelayTime` | 0.0 | Maximum delay before wave starts |
| `allowWorkshopTakeover` | False | Whether this enemy type can cause a takeover |
| `minDeathToTriggerSwarm` | 40 | Kill count threshold to trigger a swarm event (-1 = never) |
| `decrementDeathCountPerPulse` | 10 | Death count decreases by this on each pulse |

### Defense Event Mechanics

**GQ_WorkshopAttack** (`gq_workshopattackscript.psc`):
- `AttackersWinTimerSecondsPerWave = 180.0` -- attackers win if not defeated within 3 minutes per wave
- `AttackersWinMinPlayerDistance = 10000.0` -- attackers auto-win if all players are >10,000 units away
- `TriggeredAttackDelaySeconds = 1000.0` -- delay for triggered (non-random) attacks

**GQ_WorkshopDefend** (`gq_workshopdefendscript.psc`):
- `GQ_WorkshopDefendMinDistance` = 4000.0 game units -- minimum distance players must be within to count as defending

### Quickplay Raid Spawn Distances

From `workshopscript.psc`:
- Defender spawn min distance: 500 units from workshop center
- Defender spawn max distance: 1500 units (500 + 1000 width)
- Defender spread: 500 units apart along circumference
- Attacker spawn min distance: 5000 units from center
- Attacker spawn max distance: 7000 units (5000 + 2000 width)
- Attacker spread: 1000 units apart along circumference
- Activity bounds radius: 8000 units

---

## 9. Ally/Companion Assignment Mechanics

### Camp Object System (campobjectscript.psc)

Allies use the `CampObjectScript` which extends `ObjectReference`. Key mechanics:

**Spawn system:**
- `UseSpawnMap = True` (default) -- uses spawn map system
- `fSpawnMapMaxDistance = 2300.0` -- maximum spawn distance from CAMP object
- `fSpawnMapMinDistanceFromPlayers = 1000.0` -- minimum distance from players
- `fSpawnMapDesiredRangeFromPlayers = 1500.0` -- preferred distance from players

**Keyword linking chain:**
1. `CampActorToWorkshopLink` -- ally actor linked to player's workshop
2. `CampActorToMapMarkerLink` -- ally linked to map marker (sandbox target)
3. `CampActorToPlayerLink` -- ally linked to owning player
4. `CampActorToCampObjectLink` -- ally linked to their camp object (bed/station)
5. `CampObjectToActorLink` -- reverse link: object to its actor
6. `CampObjectToWorkshopLink` -- object linked to workshop

**Companion features:**
- `CompanionCampQuest` -- starts a dialogue quest (e.g., `COMP_Quest_Camp_Beckett`)
- `SpawnedActorNameOverride` -- custom name display
- `PerksToAddToPlayer` -- array of perks granted when ally is present
- `GlobalToggle` -- can disable ally spawning
- `GlobalToggleMessage` -- error message when ally is toggled off

### Vendor Types

From `workshopparentscript.psc`, NPCs can be assigned as vendors:

| VendorType | ID | Description |
|------------|-----|-------------|
| Player | 0 | Player vendor |
| Armor | 1 | Armor vendor |
| Weapons | 2 | Weapons vendor |
| Bar | 3 | Bar/drinks vendor |
| Clinic | 4 | Medical vendor |
| Clothing | 5 | Clothing vendor |
| Chems | 6 | Chems vendor |
| Misc | 7 | Miscellaneous vendor |

- `VendorTopLevel = 2` -- three vendor levels (0, 1, 2)
- Each vendor type has container FormLists indexed by level

### Beckett-Specific

From `comp_quest_camp_beckettscript.psc`:
- Tips range: 5-35 caps (`MinTips = 5`, `MaxTips = 35`)
- Has a bar vendor faction and dedicated bar scene

---

## 10. Collectron Variants (Full Catalog)

All identified Collectron skins from ESM data:

| Season/Source | Name | FormID | Notes |
|---------------|------|--------|-------|
| ATX (Store) | Junkyard Dog | 0x00662E6B | Standard junk collectron |
| ATX | Evidence Collection Assistant | 0x008599E3 | Investigation theme |
| ATX | Toxic Bob | 0x0084130D | Toxic theme |
| ATX | Liberated | 0x0082A6AB | |
| ATX | BivBev | 0x0079A1D5 | Drink-themed |
| ATX | Lumberjack | 0x0076A6BD | Wood/crafting |
| ATX | Peppino | 0x00857249 | Newest ATX variant |
| SCORE S6 | FETCH | 0x0062201B | Electronics focus |
| SCORE S7 | Zetan (CUT) | 0x0062F43C | **zzz_ prefix -- cut content** |
| SCORE S8 | Silver | 0x0063C6E5 | |
| SCORE S11 | Nuka Quantum | 0x00679A77 | |
| SCORE S14 | AutoMiner | 0x006C6DC0 | Mining theme |
| SCORE S17 | Scoutmaster | 0x00771DC9 | Scout theme |
| SCORE S22 | RoboButler | 0x00836464 | Butler theme |
| SCORE S23 | Cornbot | 0x0085CE4D | Farm theme |
| CUT | SilverBot | 0x00536D29 | **zzz_ prefix -- cut** |

---

## 11. Cut Workshop Items & Building Pieces

### Cut CAMP Items (zzz_ prefix)

**Cut Turret Skins:**
| FormID | Name | Notes |
|--------|------|-------|
| 0x007964DF | zzz_SCORE_S18_WorkshopTurretShotgun_Rusted | Cut S18 turret skin |
| 0x007964DE | zzz_SCORE_S18_WorkshopTurretMissileLauncher_Rusted | Cut S18 skin |
| 0x007964DD | zzz_SCORE_S18_WorkshopTurretLaserHeavy_Rusted | Cut S18 skin |
| 0x007964DC | zzz_SCORE_S18_WorkshopTurretLaser_Rusted | Cut S18 skin |
| 0x0078E64F | zzz_SCORE_S18_WorkshopTurretLaserHeavy_BlueRidge | Cut Blue Ridge turret |
| 0x0078E650 | zzz_SCORE_S18_WorkshopTurretMissileLauncher_BlueRidge | Cut Blue Ridge turret |
| 0x0078E651 | zzz_SCORE_S18_WorkshopTurretShotgun_BlueRidge | Cut Blue Ridge turret |
| 0x0078E64E | zzz_SCORE_S18_WorkshopTurretLaser_BlueRidge | Cut Blue Ridge turret |

**Cut Utility/Functional Items:**
| FormID | Name | Notes |
|--------|------|-------|
| 0x0062F43C | zzzSCORE_S7_ENTM_CAMP_Utility_Collectron_Zetan | Cut alien Collectron |
| 0x00536D29 | zzzATX_ENTM_CAMP_Utility_Collectron_SilverBot | Cut silver Collectron |
| 0x006FAD33 | zzzATX_ENTM_CAMP_Utility_WeatherStation_DefaultWeatherStation | Cut default weather station |
| 0x006FAD34 | zzzATX_ENTM_CAMP_Utility_WeatherStation_SnowWeatherStation | Cut snow weather station |
| 0x00787EE1 | zzzATX_ENTM_CAMP_Utility_WeatherStation_Falls_Leaves | Cut fall leaves weather station |
| 0x007A7E7D | zzzATX_ENTM_CAMP_Utility_PopcornMachine_NukaCola | Cut Nuka-Cola popcorn machine |
| 0x00830905 | ZZZ_SCORE_S22_ENTM_CAMP_Utility_MotorizedButterChurn_VaultTec | Cut Vault-Tec butter churn |
| 0x00691C09 | zzz_SCORE_S12_ENTM_CAMP_Utility_FirewoodPile | Cut firewood pile |
| 0x00854BED | zzzz_ATX_ResourceProductionIntervalHours_AmmOMatic_resource | Cut original AmmOMatic rate |
| 0x0083E1D9 | zzzATX_ENTM_CAMP_Structure_GasStationCanopy_Copy01 | Cut gas station canopy variant |
| 0x0083E1D8 | zzzATX_ENTM_CAMP_Structure_PoseidonEnergyGasStation | Cut Poseidon gas station |

**Cut Decorative Items (highlights):**
| FormID | Name | Season |
|--------|------|--------|
| 0x008A5DFF | ZZZ_SCORE_S24_FloorDecor_WaxGuinevere | S24 |
| 0x0085B1D7 | ZZZ_SCORE_S23_Structure_RaiderNukaColaCar | S23 |
| 0x0084A554 | ZZZ_SCORE_S23_Defense_Barrier_BoneWall | S23 -- cut defense item |
| 0x0084A53A | ZZZ_SCORE_S23_Furniture_Instrument_RaiderGuitar | S23 |
| 0x0084A4B8 | ZZZ_SCORE_S23_FloorDeco_RaiderTotem | S23 |
| 0x0084A471 | ZZZ_SCORE_S23_FloorDeco_HeadOnSpike | S23 -- cut dark decoration |
| 0x0083EAED | ZZZ_SCORE_S23_Machinery_Workbench_Brewing_Makeshift | S23 -- cut workbench |
| 0x0083EAEB | ZZZ_SCORE_S23_Machinery_Workbench_Weapon_GunSmith | S23 -- cut weapon workbench skin |
| 0x00836465 | ZZZ_SCORE_S22_Floor_WhiteSpringGrass | S22 |
| 0x00834CDE | ZZZ_SCORE_S22_Floor_NukaCola_Tiled | S22 |
| 0x008335DB | ZZZ_SCORE_S22_CAMPPets_IdleFurniture_JunkFoodTrashPile | S22 -- cut pet furniture |
| 0x0082E15D | ZZZ_SCORE_S22_FloorDecor_MistressofMysteriesWaxFigure | S22 |
| 0x007DC4ED | ZZZ_SCORE_S21_FloorDecor_OgopogoStatue | S21 |
| 0x00868F72 | zzzATX_ENTM_CAMP_CAMPPets_RadHog_Rooter | Cut RadHog pet variant |
| 0x0084B0BA | zzzSCORE_S23_ResourceProductionIntervalHours_BodyinBathtub | Cut body in bathtub resource producer |
| 0x00830174 | ZZZ_SCORE_S22_FloorDecor_ChryslusSportsCar | S22 |

**Cut Workshop Category Keywords:**
| FormID | Name | Notes |
|--------|------|-------|
| 0x008229FB | zzz_Workshop2_SubCategory_Power_Switches | Cut category reorganization |
| 0x00822A06 | zzz_Workshop2_SubCategory_Furniture_Couches | Cut sub-category |
| 0x00822A0A | zzz_Workshop2_SubCategory_Furniture_MusicalInstruments | Cut sub-category |
| 0x00569325 | zzz_REUSE_WorkshopCategoryWallpapers | Recycled keyword |
| 0x0062E20F | ZZZ_ap_Turret_Weapons | Cut turret weapon category |

**Cut Challenges:**
| FormID | Name | Notes |
|--------|------|-------|
| 0x003808C4 | CUT_HappyCamper03 | Cut perk or challenge |
| 0x004275E3 | CUT_Babylon_Challenge_Daily_DeployCAMPs_Low | Cut "Babylon" (early 76 codename?) CAMP challenge |
| 0x004275E5 | CUT_Babylon_Challenge_Daily_DeployCAMPs_High | Cut Babylon high variant |
| 0x003FCD35 | CUT_Babylon_Challenge_Lifetime_CampsPlaced_1 | Cut lifetime CAMP tracking |

---

## 12. Blueprint System Internals

### Blueprint Script

`w05_mq_102p_blueprintsscript.psc` exists but is specific to a quest (MQ102). The general blueprint system is handled engine-side rather than through Papyrus scripts, with blueprints stored as serialized object groups in server-side character data.

### Blueprint Implementation

The blueprint system uses the native workshop menu:
- `Debug.StoreBlueprint()` -- Papyrus function exposed through the Debug script
- `Debug.BuildBlueprint()` -- Places a stored blueprint
- Blueprints store relative positions, rotations, and snap points of all included objects
- Budget cost of a blueprint equals the sum of all individual object costs
- Blueprints are per-character, stored in server-side save data

---

## 13. Pet System Internals

### Legacy Taming System (SQ_AnimalTaming)

The original FO76 taming system (now removed) used the Wasteland Whisperer / Animal Friend perks:

**Core scripts:**
- `sq_animaltamingscript.psc` -- Main taming quest (per-player instance)
- `sq_animaltamingencounterscript.psc` -- Random encounter spawner

**Mechanics:**
- Three taming perk tiers: `SQ_AnimalTaming01Keyword` (0x00004166), `SQ_AnimalTaming02Keyword` (0x003B70BD), `SQ_AnimalTaming03Keyword` (0x003B70BE)
- Each tier has its own faction: `SQ_AnimalTamingPerkFaction01/02/03`
- Find radius: 20,000 game units (`RE_Scene_AnimalTamingFindPlayerRadius`)
- When tamed, animal gets `SQ_AnimalTamingFaction` (0x00004167) added
- Budget cost zeroed via `WorkshopBudgetObjectMultiplier` set to 0
- Animals tracked via `SQ_AnimalTamingTamedAnimalFlag` AV on the player
- `TamedAnimal` struct stores Race + AnimalBase for recreation if "lost"
- Animal travels to camp via `SQ_AnimalTamingTravelToCamp` package, then sandboxes via `SQ_AnimalTamingSandboxAtCamp`

**Available animal leveled lists:**
| Tier | Leveled List | FormID |
|------|-------------|--------|
| Tier 1 | SQ_AnimalTaming01Animals | 0x0000416A |
| Tier 2 | SQ_AnimalTaming02Animals | 0x003B75B4 |
| Tier 3 | SQ_AnimalTaming03Animals | 0x003B75B5 |

### Modern CAMP Pets System (CAMPPets)

The current pet system replaced taming with buildable pet furniture:

**Core scripts:**
- `petspawnfurniturescript.psc` -- Furniture that spawns the pet actor
- `petactorscript.psc` -- Base pet actor behavior

**Pet Furniture Properties:**
- `ActorBaseToSpawn` -- Which actor to create
- `SnapActorIntoFurniture` (default True) -- Snap pet into its bed/furniture on spawn
- `ItemToGiftPlayer` -- LeveledItem list for periodic gifts
- `PerksToAddToPlayer` -- Perks granted while pet is present

**Pet Gift System:**
- `CAMPPets_PetGiftInveral` (note: typo in game data) = 7200.0 seconds (2 hours)
- `PETS_PlayerGifts_ResourceProductionInterval_Default` = 0.050 hours (3 minutes) -- production interval for resource collector AV
- `CAMPPets_PetHasGiftForPlayer` -- AV tracking gift quantity
- Gift notification: `CAMPPets_PetGiftPlayerMessage01`

**Pet Gift Leveled Lists:**
| Pet Type | Gift Resource | Gift LL |
|----------|--------------|---------|
| Dog | `PETS_Dog_PlayerGifts_Resource` (0x00424571) | `PETS_Dog_PlayerGifts_LL_Tier1` (0x0042456E) |
| Cat | `PETS_Cat_PlayerGifts_Resource` (0x00412205) | `PETS_Cat_PlayerGifts_LL_Tier1` (0x00411B77) |

**Pet Keyword Chain:**
1. `CAMPPets_ActorToWorkshopLink` -- pet to workshop
2. `CAMPPets_ActorToMapMarkerLink` -- pet to map marker (sandbox center)
3. `CAMPPets_ActorToPlayerLink` -- pet to owner
4. `CAMPPets_ActorToCampObjectLink` -- pet to its furniture
5. `CAMPPets_ObjectToActorLink` -- furniture to pet (reverse)
6. `CAMPPets_ObjectToWorkshopLink` -- furniture to workshop

**Pet Emote Responses:**
| Keyword | Response Type |
|---------|--------------|
| `PETS_EmoteResponse_Happy` | Happy reaction |
| `PETS_EmoteResponse_Sad` | Sad reaction |
| `PETS_EmoteResponse_Angry` | Angry reaction |
| `PETS_EmoteResponse_Confused` | Confused reaction |
| `PETS_EmoteResponse_Neutral` | Neutral reaction |
| `PETS_EmoteResponse_Trick1-4` | Trick responses |
| `CAMPPets_EmoteType_PetCommand` | Direct pet commands |

**Available Pet Types:**
| Pet | FormID/Keyword | Source |
|-----|----------------|--------|
| Standard Cat | Various | Base game |
| Standard Dog | Various | Base game |
| Glowing Cat | SCORE_S24_CAMPPets_GlowingCat (0x008A5DF6) | Season 24 |
| Lykoi Cat | SCORE_S23_CAMPPets_Lykoi (0x00853B85) | Season 23 |
| RadHog Standard | CAMPPets_RadHog_Standard (0x0084FB8D) | ATX |
| RadHog Rooter | ATX_CAMPPets_Rooter (0x0089A8C6) | ATX (variant cut: 0x00868F72) |
| Mongrel | ATX_CAMPPets_Mongrel (0x0084132C) | ATX |
| RoboPaw (Dog) | ATX_CAMPPets_RoboPaw (0x0082A99F) | ATX |
| RoboPaw (Cat) | ATX_CAMPPets_Cat_RoboPaw (0x0082BCB7) | ATX |
| RoboPawPS (Dog) | ATX_CAMPPets_RoboPawPS (0x0085B0CB) | ATX |

**Pet Clothing:**
- `ATX_CAMPPets_PetClothing` keyword (0x0079956B)
- Recipe filter: `RecipeFilter_Armor_CAMPPets` (0x007BB114)
- Example: `SCORE_S23_Apparel_CAMPPets_Cat_Neckwear_CollarNailsCat`

**Cut Pet Challenges:**
Multiple `CUT_PETS_Challenge_*` records suggest planned but removed pet interaction milestones:
- Feed once per day
- Pet once per day
- Complete tricks
- Complete quests with pet

---

## 14. Hidden Workshop Crafting Bonuses & Multipliers

### Experience System

| Setting | Value | Purpose |
|---------|-------|---------|
| `fWorkshopExperienceBase` | 2.0 | Base XP per crafted item |
| `fWorkshopExperienceMax` | 25.0 | Maximum XP per single craft |
| `fWorkshopExperienceMult` | Variable | XP multiplier (base value in next DATA field) |

### Repair Discount

`fWorkshopRepairComponentMult` = 0.25 -- repairing workshop objects costs only 25% of original materials.

### Turret Auto-Repair

From `workshopobjectscript.psc`:
- `bAllowAutoRepair` (default True) -- objects can be repaired by the daily update process
- `bWork24Hours` (default False) -- if True, assigned NPC works 24/7 with no sleep/relaxation

### Created Actor Death Timers

From `workshopcreatedactorscript.psc`:
- `DestroyAfterDeathSecondsMin` -- base respawn delay for created actors (turrets, brahmin, etc.)
- `DestroyAfterDeathSecondsMax` -- maximum respawn delay cap
- `DestroyAfterDeathSecondsAddPerDeath` -- each death increases respawn delay
- `DestroyAfterDeathResetSeconds = 900.0` -- 15 minutes of no deaths resets the timer

### Workshop Grenade Auto-Refill

From `workshoprefillingcontainerscript.psc`:
- `MinGrenadeCount = 10` -- containers auto-refill when below 10 grenades
- `ResetInventoryTimeDays = 0.04` (~58 minutes) -- check interval for refill

### Shelter System

From `shelterentrance.psc`:
- Shelters use `ShelterCell` (interior cells) with `ShelterCellTeleportPosition` for entry
- Each shelter entrance links to a `ConstructibleObject` recipe
- Shelter budgets are separate from CAMP budget (managed engine-side)
- `ShelterWorkshop` script extends `ObjectReference` as a minimal conditional script

---

## Source Files

### Scripts
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/workshopscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/workshopcampscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/workshopparentscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/workshopobjectscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/campobjectscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/petactorscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/petspawnfurniturescript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/sq_animaltamingscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/sq_animaltamingencounterscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/sq_masterscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/gq_workshopattackscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/gq_workshopdefendscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/workshopcreatedactorscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/workshoprefillingcontainerscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/workshoptrapgun.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/addcampkitsscript.psc`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/shelterentrance.psc`

### Data
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/tempest_data/misc/curvetables/json/workshop/defenses/` (18 turret/trap curve files)
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/esm_dump/full_esm_dump.txt`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/esm_dump/GLOB_records.txt`
