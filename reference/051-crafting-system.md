# Finding 051: Fallout 76 Complete Crafting System

## Sources
- `esm_dump/COBJ_records.txt` - 21,934 craftable object records
- `tempest_data/misc/curvetables/json/cobj/` - Crafting cost curve tables (ammo, armor, brewing, chem, cooking, legendary, leveled cobj, nukeflora, powerarmor, smelting, weapon, workshop)
- `tempest_data/misc/curvetables/json/crafting/` - 32 food/brewing effect curves
- `esm_dump/PERK_records.txt` - Perk definitions including crafting perks
- `esm_dump/KYWD_records.txt` - Workbench type keywords
- `esm_dump/full_esm_dump.txt` - Game settings (GMST), condition forms (CNDF)
- `scripts_decompiled/` - Plan/recipe unlock scripts, vendor scripts, gold bullion scripts

---

## 1. Total Craftable Items by Category

**21,934 total COBJ records** in SeventySix.esm. Breakdown by category:

| Category | Count | Notes |
|---|---|---|
| Weapon/Armor Mods (co_mod) | 6,797 | Largest category - receiver, barrel, grip, sight, etc. |
| Power Armor (paint + mods) | 3,146 | Includes all PA material/paint variants |
| Workshop/CAMP items | 2,687 | Structures, decorations, furniture, defenses |
| DLC content (co_DLC + co_XPD) | 982 | Post-launch DLC and expansion recipes |
| Clothes/Outfits | 804 | Cosmetic outfit crafting |
| Legendary Crafting (shards + mods) | 450 | Legendary module/shard system |
| Tinker's Workbench (all) | 392 | Ammo, grenades, souvenirs, misc |
| Armor (base crafting) | 323 | Craft armor pieces from scratch |
| Food/Meals | 246 | Cooking station recipes |
| Weapons (base crafting) | 266 | Craft weapons from scratch |
| Backpacks | 131 | Backpack mods and skins |
| Legendary Shards | 171 | Individual shard crafting |
| Ammo (Tinkers_Ammo) | 73 | Standard, bulk, ultracite, anti-scorchbeast |
| Headwear | 68 | Hats, helmets, masks |
| Fishing | 58 | Rods, bobbers, displays |
| Chems | 55 | Chemistry station recipes |
| Brewing | 42 | Fermentation station recipes |
| Player/CAMP Titles | 80 | Cosmetic title crafting |
| Scrap Recipes | 39 | Scrapping return definitions |

### By Unlock Source

| Source | Count | Notes |
|---|---|---|
| ATX (Atom Shop) | 4,169 | Purchased with Atoms |
| SCORE (Scoreboard) | 2,176 | Season pass rewards |
| POST (Post-launch) | 558 | Free post-launch content |
| RD01 (Regional DLC) | 104 | Regional quest rewards |
| Burn (Burning Springs) | 88 | Burning Springs event recipes |
| Storm (Storm events) | 88 | Storm-related event recipes |
| MOON (Moonshine Jamboree?) | 83 | Moon-themed event |
| F1 (Fallout 1st) | 62 | Subscription-exclusive |
| MILE (Milestone?) | 62 | Milestone rewards |
| BOUNTY (Bounty system) | 61 | Bounty hunter rewards |
| Meat Week | 23 | Seasonal event |
| Invaders (Zeta) | 17 | Alien invasion event |
| SURVIVAL | 16 | Survival mode rewards |
| Gold Vendor | 64 | Gold bullion vendor exclusives |

---

## 2. Crafting Cost Curves -- How Costs Scale

The game uses curve tables to define how material costs scale. The X axis represents a "recipe complexity" value (not player level), and the Y axis is the actual material quantity required.

### Weapon Crafting Costs (per-material scaling)

Weapons use aggressive scaling. Steel is the primary material with the steepest curve:

| Complexity | Steel | Lead | Screws | Springs | Acid |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 1 |
| 5 | 7 | 3 | 4 | 3 | 4 |
| 10 | 14 | 5 | 7 | 6 | 8 |
| 20 | 28 | 10 | 14 | 12 | 16 |
| 50 | 70 | 25 | 35 | 30 | 40 |
| 100 | 140 | 50 | 70 | 60 | 80 |

**Key insight**: Steel scales at 1.4x the complexity value, while rare materials (lead, springs) scale at 0.5-0.6x. This means high-tier weapons are steel-hungry but use moderate amounts of rare materials.

### Armor vs Weapon Cost Comparison

Armor costs slightly less than weapons at the same complexity:
- Armor acid at complexity 20 = 14 units vs Weapon acid at 20 = 16 units
- Armor scales at ~70% of the weapon rate for most materials

### Chem Crafting Costs

Chem costs scale at exactly 50% of the base rate:
- Complexity 1 = 1, Complexity 10 = 5, Complexity 20 = 10
- Pattern: `y = x * 0.5` (rounded)

### Workshop/CAMP Costs

Workshop items use a 1:1 linear scale -- the simplest cost model:
- Complexity 1 = 1, Complexity 10 = 10, Complexity 20 = 20
- No diminishing or escalating returns

### Ammo Crafting Costs

Ammo also uses a 1:1 linear scale identical to workshop items.

### Leveled Crafting Costs (Player Level Scaling)

Leveled armor and weapon recipes scale with player level, not recipe complexity:

**Leveled Armor Acid by Level:**
| Level | Cost |
|---|---|
| 1 | 0 |
| 10 | 2 |
| 20 | 5 |
| 30 | 7 |
| 40 | 10 |
| 50 | 13 |
| 60 | 18 |
| 100 | 34 |

**Leveled Weapon Acid by Level:**
| Level | Cost |
|---|---|
| 1 | 0 |
| 10 | 2 |
| 20 | 3 |
| 30 | 5 |
| 40 | 6 |
| 50 | 8 |
| 60 | 12 |
| 100 | 23 |

Armor costs more than weapons at the same level for leveled recipes (opposite of the static curves).

---

## 3. Super Duper Perk -- How the Double Proc Works

### Perk Records
- `SuperDuper01` (0x003BD597) - Rank 1
- `SuperDuper02` (0x003BD598) - Rank 2
- `SuperDuper03` (0x003BD599) - Rank 3
- `CUT_SuperDuper04` (0x003BD59A) - **Cut rank 4** (never released)

### Trigger Mechanism (from PERK conditions)

Each rank uses `GetRandomPercent` to roll a random number:
- The condition check is `GetRandomPercent <= X` where X is the proc chance
- Rank 3 condition visible in dump: roll occurs at craft time

### Exclusion System

Super Duper has two exclusion conditions on every rank:
```
GetIsObjectType:0x0(0x9A) != 1.000000    -- Excludes object type 0x9A
HasKeyword:0x0(0x43C439) != 1.000000     -- Excludes BlockSuperDuperPerk keyword
```

The keyword `BlockSuperDuperPerk` (0x0043C439) is explicitly described in the ESM:
> "Items with this keyword should be ignored by the Super Duper Perk"

**Items that block Super Duper:**
- Object type 0x9A (likely Power Armor pieces or certain high-value items)
- Anything tagged with `BlockSuperDuperPerk` keyword

### Proc Chances (from PERK entry points)
- Rank 1: 10% chance
- Rank 2: 20% chance
- Rank 3: 30% chance
- **CUT Rank 4**: Was planned but cut. Conditions reference `HasPerk(DryNurse)` and `GetRandomPercent <= 60` suggesting it may have been tied to another perk system or had a 40% chance

### How it Actually Works
The perk fires on the `OnItemCrafted` event. When the random percent check passes, the game duplicates the crafted output into the player's inventory. The materials are NOT consumed twice -- you get a free copy.

---

## 4. Ammo Crafting Yields per Type

### Standard Ammo (Tinker's Workbench)

73 total ammo recipes exist, in three tiers:
1. **Standard** - Base crafting (29 types)
2. **Bulk** - Higher yield per craft (20 types, added later)
3. **Ultracite/Anti-Scorchbeast** - Special variants (16 types)

Standard ammo types craftable:
- .38 Caliber, .44, .45, .50 Caliber, .50 Caliber Ball
- 10mm, 2mm EC, .308, 5.56, 5mm
- Shotgun Shell, Fusion Cell, Plasma Cartridge, Gamma Cell, Cryo Cell
- Railway Spike, Harpoon, Crossbow Bolt, Compound Bow Arrow
- Flare, Paddle Ball, Syringer Ammo, Camera Film
- Cannonball, Grenade Launcher, Missile, Mini Nuke, Plasma Core, Fusion Core
- Alien Blaster Rounds, Flamer Fuel

### Ammo Economy Ranking

Based on the ammo cost curves (which use a 1:1 linear scale), the materials-per-round ratio is defined by the recipe itself, not the curve. The curve simply says "if the recipe calls for X units of acid, you need X units of acid."

**Best yield-per-craft ammo types** (community-verified from recipe data):
- **5mm** - Highest rounds per craft (100+ with Ammosmith)
- **.38 Caliber** - High yield, cheap materials
- **Flamer Fuel** - High yield per craft
- **Fusion Cells** - Good yield, common materials

**Worst yield-per-craft:**
- **Mini Nukes** - 1 per craft, expensive
- **Missiles** - 1 per craft
- **Plasma Cores** - 1 per craft
- **2mm EC** - Low yield, rare materials

### Ammosmith Perk Effect
- `Ammosmith01` (0x003896DB): Rank 1 - +40% ammo production
- `Ammosmith02` (0x003BB50D): Rank 2 - +80% ammo production
- `CUT_Ammosmith03` (0x003BB50E): **Cut rank 3** - was planned but never released
- Condition: Requires `HasKeyword(0xF4AE8)` = must be at a Tinker's Workbench

---

## 5. Cut Recipes (zzz_ and CUT_ Prefix) -- What Was Planned

**1,067 total cut/disabled records** (zzz_ prefix) plus **98 CUT_ prefix** and **95 DEPRECATED/DEL_ prefix**.

### Notable Cut Content Categories

**Cut Weapons:**
- `CUT_co_Weapon_Ranged_LaserMusket` - Full Laser Musket with 24+ mod recipes (barrel, grip, muzzle, receiver tiers 1-5, scopes). Complete weapon system removed.
- `zzz_co_Weapon_Ranged_JunkJet` - Junk Jet from Fallout 4, was planned
- `zzz_co_Weapon_Melee_DynamiteSpear` - Dynamite-tipped spear
- `zzz_co_Tinkers_GrenadeFlashbang` - Flashbang grenade
- `zzz_co_Tinkers_GrenadeFragSmart` - Smart frag grenade
- `zzz_co_Tinkers_SoundmakerGrenade` - Sound distraction grenade
- `zzz_co_Tinkers_GrenadeThrowingBearTrapBleeding` - Bear trap throwing weapon
- `zzz_co_mod_Incinerator_*` - Full Incinerator weapon mod set (launcher, receiver, barrel)
- `zzz_co_mod_Nitro_*` - Complete Nitro weapon mod tree (receivers, scopes, special effects including "PenetratingStagger")
- `ZZZ_co_Weapon_StampVendor_1` through `_7` - **Stamp vendor weapon system** (7 weapons!)
- `zzz_E09A_co_NukaLauncher_NOCRAFT` - Nuka Launcher marked no-craft

**Cut Legendary Effects:**
- `zzz_BOUNTY_co_LegendaryShard_Barbarian` - Melee damage bonus
- `zzz_BOUNTY_co_LegendaryShard_Insane` - Unknown effect
- `zzz_BOUNTY_co_LegendaryShard_Jagged` - Bleed damage?
- `zzz_BOUNTY_co_LegendaryShard_MadScientist` - Unknown effect
- `zzz_BOUNTY_co_LegendaryShard_Pulsating` - Melee pulsating effect
- `zzz_BOUNTY_co_LegendaryShard_Rebate` - Ammo return on hit
- `zzz_BOUNTY_co_LegendaryShard_RestoreFeralRate` - Feral ghoul interaction
- `zzz_BOUNTY_co_LegendaryShard_Savage` - Unknown
- `zzz_BOUNTY_co_LegendaryShard_SelfRepair` - Self-repairing equipment
- `zzz_co_MiscMod_Legendary_elusive` - Evasion effect
- `zzz_co_MiscMod_Legendary_MaxAP` - Max AP bonus
- `zzz_co_MiscMod_Legendary_Readers` - Reading/intelligence bonus
- `zzz_co_MiscMod_Legendary_Warmongers` - Combat bonus
- `zzz_WIP4_co_LegendaryShard_Slayers` / `zzz_WIP4_co_mod_Legendary_Weapon4_Slayers` - 4th star legendary "Slayers" effect (WIP4 = Work In Progress 4-star)
- `zzz_co_mod_Legendary_Extract_1/2/3/4` - Legendary extraction system (4 tiers)
- `zzz_co_mod_Legendary_Scrap` - Direct legendary scrapping

**Cut Armor:**
- `zzz_co_Armor_Tempest_*` - Complete Tempest armor set (5 pieces + 30+ mods for linings, materials) with gold vendor variants
- `zzz_co_Armor_30fkfnsdf_*_REPAIRONLY` - Debug/test armor (gibberish name = developer test)
- `zzz_co_mod_BackPack_*` - 15+ cut backpack mods (colors, flairs, effects including ArmorPlated, Insulated, Refrigerated)

**Cut Perks:**
- `CUT_SuperDuper04` - Rank 4 Super Duper
- `CUT_Ammosmith03` - Rank 3 Ammosmith
- `CUT_GreenThumb02/03` - Green Thumb had 3 ranks planned
- `CUT_Scrapper02` - Scrapper had a second rank
- `zzz_Gunsmith04/05` - Gunsmith had 5 ranks
- `zzzMakeshiftWarrior04/05` - Makeshift Warrior had 5 ranks
- `zzz_GoodWithSalt03` - Good With Salt rank 3

**Cut Robot Crafting (DLC01Bot):**
- Over 200+ cut robot armor recipes for Automatron-style robot building (Assaultron, Mr. Handy, Protectron, Robobrain, Sentry Bot parts with wasteland armor tiers 1-10)
- This was a complete FO4 Automatron-style robot crafting system that was cut

**Cut Food/Drink:**
- `zzz_co_Brewing_P01E_HeartChampagne` - Valentine's champagne
- `zzz_co_Brewing_ToxicGin` - Toxic gin
- `CUT_co_chem_RefreshingBeverage` - Refreshing Beverage was going to be craftable
- `CUT_co_chem_SFS09_FormulaQ` - Formula Q chem
- `zzz_DLC04_co_NukaCola_*` - 5 cut Nuka-Cola recipes (BombDrop, Love, Punch, Sunrise, Void)
- `CUT_co_meal_P01E_HeartNougatCandy*` - 4 Valentine's candy recipes
- `zzz_co_meal_MatzohBallSoup` - Matzoh Ball Soup
- `zzz_co_meal_CannedCranberryTastyRelish` - Canned relish variant

**Cut Events:**
- `CUT_co_MutatedEvents_*` - Mutated event infusions (3 tiers each of SteelSkin, PoisonCloud, Fiery)
- `zzz_MutatedEvents_co_BackPack_*` - Mutated event backpack flairs

**Debug/Test Entries:**
- `zzz_co_23r23d`, `zzz_co_d1dff1d1`, `zzz_co_f1ffcdwc`, `zzz_co_g23dd3`, etc. -- Gibberish editor IDs indicating developer test/placeholder records

---

## 6. Condition/Repair Cost Formulas

### Repair Perks

**Weapon Artisan** (3 ranks: 0x003D295F/60/61):
- Allows repairing weapons to 130%/160%/200% condition
- No condition restrictions beyond workbench access

**Fix It Good** (3 ranks: 0x003E35BE/BF/C0):
- Allows repairing armor to 130%/160%/200% condition
- Condition: `HasKeyword(0xF4AE9)` = must be at Armor Workbench
- Ranks are exclusive (HasPerk check prevents stacking)

**White Knight** (3 ranks: 0x0038AB84/85/86):
- Reduces armor repair costs
- Condition: `HasKeyword(0xF4AE9)` AND NOT `HasKeyword(0x4D8A1)` = at Armor Workbench, NOT Power Armor
- Each rank reduces repair material costs further

**Power Patcher** (3 ranks: 0x00391F22/23/24):
- Reduces Power Armor repair costs
- Condition: `HasKeyword(0x4D8A1)` = must be Power Armor
- Same structure as White Knight but for PA

**Lucky Break** (3 ranks: 0x00356A06/07/08):
- Chance to not consume durability on armor hits

### Repair Cost System (from GMST)
- `sRepairCost` (0x000D4BCA) - UI label for repair costs
- `fCombatConditionRegenRateMult` (0x00018D02) - Combat condition regeneration rate
- `ConditionRateMult` (ActorValue 0x0000035A) - Multiplier on condition degradation

### Scrapping Return System (modScrapRecipe)

The game defines 39 explicit scrap return recipes that control what you get back from scrapping weapons/armor:

**Material returns (by tier):**
- Minor returns: Cloth, Leather, Plastic, Steel, Wood, Bone, Aluminum, Gold, Rubber, Screws
- Standard returns: Glass, Lead, Rubber, Nuclear Material, Asbestos, Circuitry, Antiballistic Fiber, Bone, Cloth, Leather, Plastic, Steel, Wood

**Weapon type-specific scrap returns:**
- `co_modScrapRecipe_Null_Repair_Weapons_BladeMelee` - Blade melee weapons
- `co_modScrapRecipe_Null_Repair_Weapons_BluntMelee` - Blunt melee weapons
- `co_modScrapRecipe_Null_Repair_Weapons_Energy` - Energy weapons
- `co_modScrapRecipe_Null_Repair_Weapons_Heavy` - Heavy weapons
- `co_modScrapRecipe_Null_Repair_Weapons_Launchers` - Explosive launchers
- `co_modScrapRecipe_Null_Repair_Weapons_MachinedGuns` - Machined ballistic weapons
- `co_modScrapRecipe_Null_Repair_Weapons_PipeGuns` - Pipe weapons
- `co_modScrapRecipe_Null_Repair_Weapons_Ultracite` - Ultracite weapons

ATX variants (Atom Shop items): 6 additional minor-return recipes for Bone, Cloth, Leather, Plastic, Steel, Wood. These ensure Atom Shop items return minimal materials when scrapped.

---

## 7. Scrapping Yield Formulas

### How Scrapping Works

Scrapping is NOT a simple "return X% of crafting cost." Instead, each weapon/armor type has a specific `modScrapRecipe` that defines exactly what components are returned. The recipe is keyed to the weapon category (energy, heavy, melee, etc.) not the specific weapon.

### Scrapper Perk
- `Scrapper01` (0x00065E65) - Rank 1 (only live rank)
- `CUT_Scrapper02` (0x001D2483) - **Cut rank 2**
- Condition: `HasKeyword(0xF4AEA)` OR `HasKeyword(0xF4AE9)` = at Weapon OR Armor Workbench
- Effect: Provides additional/rarer components when scrapping

### Perk Card Scrap Values (from GMST)
- `fPerkCardScrapGlobalValueMult` (0x005DC35F) - Multiplier for scrapping perk cards (standard)
- `fPerkCardScrapFoilValueMult` (0x005D0016) - Multiplier for scrapping foil perk cards (higher)
- `sPerkCardScrapUnavailable` (0x005C5F9E) - UI message when can't scrap a card

---

## 8. Items That Cannot Be Scrapped and Why

### Keyword-Based Restrictions

Items marked with specific keywords are blocked from scrapping:
- `BlockSuperDuperPerk` keyword items likely overlap with non-scrappable items
- Object type 0x9A exclusion (Power Armor or quest items)

### Categories That Cannot Be Scrapped
1. **Quest items** - Flagged as quest objects, cannot be dropped or scrapped
2. **Atom Shop items** (ATX prefix) - Can be scrapped but return minimal materials (Minor scrap recipes)
3. **Certain legendary items** - The old legendary extraction system was cut (`zzz_co_mod_Legendary_Extract_1/2/3/4`)
4. **REPAIRONLY items** - Several items flagged as repair-only in the data:
   - `zzz_co_Armor_30fkfnsdf_*_REPAIRONLY` (debug armor)
   - `zzz_co_Armor_Wastelander_Heavy_With_Helmet_RepairOnly`
   - `zzz_co_Weapon_Melee_W05_MQ_004P_*_REPAIRONLY` (Wastelander quest weapons)
   - `zzz_co_Weapon_Ranged_W05_MQ_004P_*_REPAIRONLY` (Wastelander quest guns)
5. **NOCRAFT items** - Cannot be crafted or scrapped:
   - `zzz_co_Weapon_Ranged_GaussRifle_Presidential_NOCRAFT`
   - `zzz_E09A_co_NukaLauncher_NOCRAFT`

---

## 9. Plan/Recipe Unlock System

### How the Game Tracks What You've Learned

Plans and recipes are tracked via **ConstructibleObject (COBJ)** records. The game has two primary script systems:

**DefaultTeachRecipeOnRead** (`defaultteachrecipeonread.psc`):
```
ScriptName DefaultTeachRecipeOnRead Extends ObjectReference
ConstructibleObject Property RecipeToTeach Auto Const mandatory
```
- Attached to plan/recipe note items
- When the player reads/uses the plan item, it calls the engine function to teach the ConstructibleObject
- The plan item is consumed on use

**DefaultTeachRecipeOnMenuItemRun** (`defaultteachrecipeonmenuitemrun.psc`):
- Used for terminal-based recipe unlocks (vendors, quest terminals)
- Supports complex unlock conditions:
  - `RequiredKeyword` - Player must have specific keyword
  - `RequiredFaction` - Player must be in faction
  - `RequiredActorValue` - Player must have AV at minimum value
  - `CompletedQuest` - Player must have completed a quest
- Supports OR/AND condition logic via `UseORConditions` flag

**LearnRecipeOnMenuItemRun** (`learnrecipeonmenuitemrun.psc`):
- Simpler version for direct terminal teaching
- Matches terminal menu IDs to ConstructibleObject recipes
- Can teach multiple recipes per menu item selection

### Plan Learning Tracking
Once a COBJ is "known" by the player, the engine tracks this in the player's save data. The COBJ conditions (CTDA entries) then check if the player has learned the recipe before showing it in crafting menus.

### Condition Function 859
The most common unlock condition is function `859` which checks if the player owns/has learned a specific entitlement (form ID). This is the primary mechanism for ATX, SCORE, and event-locked recipes. Example:
```
CTDA 859:0x0(0x8ADA16,0x0,0,0x0,-1)==1.000000
```
This checks: "Does the player have entitlement 0x8ADA16?" -- the entitlement is granted by purchasing from the Atom Shop, earning from Scoreboard, or completing events.

### CondProxy Pattern
830 recipes use a `CondProxy` pattern where a "proxy" COBJ exists to handle the condition checking. These act as redirects -- the proxy checks conditions, then the actual recipe is shown. Used heavily for Gold Vendor items, seasonal rewards, and cross-system unlocks.

---

## 10. Vendor Plan Inventory Rotation Mechanics

### Vendor System Architecture

From `workshopvendorparentscript.psc`, vendors have **7 inventory categories**:
1. Misc
2. Armor
3. Weapons
4. Bar (drinks)
5. Clinic (medical)
6. Clothing
7. Chems

Each category has **leveled containers** indexed by vendor level, meaning higher-level vendors stock rarer plans.

### Restock Mechanism

From `qf_w05_settlersdaily_restock_0041b725.psc`:
- Settler vendors use a daily restock quest (`W05_SettlersDaily_Restock`)
- Has a `CanDeposit` ActorValue check
- Triggers `Scene1` to refresh inventory
- Daily reset tied to the server's daily timer

### Vendor Faction System

From `defaultactivatorvendorfactionscript.psc` and `defaultvendorscript.psc`:
- Vendors are keyed to factions
- `SellOnly` property controls if vendor only sells (vs buying from player too)
- Non-actor vendors (machines, terminals) require explicit `VendorFaction` assignment

### Gold Vendor System

From `prkf_w05_playergoldvendorint_005a11a2.psc`:
- Gold bullion vendors use a perk-based interaction system
- `VendorInteractChoiceScript` handles the vendor menu trigger
- 64 recipes are specifically gated behind `GoldVendor` condition proxy patterns

---

## 11. Gold Bullion vs Cap vs Event-Only Recipes

### Gold Bullion Recipes

From `goldbullionrewardscript.psc`:
- Gold Bullion has a **daily earning cap** (`GoldBullion_RewardAmountMax`)
- Tracked via ActorValues:
  - `GoldBullion_AmountRewardedToday` - Daily counter
  - `GoldBullion_LastRewardedTimestamp` - Resets daily
- **Prerequisite**: Must complete `W05_MQA_206P` (final Wastelanders main quest)
- UI messages for daily limit reached and amount rewarded

64 specific `GoldVendor` recipes identified, including:
- Workshop utilities (SurvivalCache, SoulSoupServer, CrashedCargoBot, Cornbot, RoboButler, Beehive, BrewingVat, EspressoMachine, etc.)
- Backpack mods (ScrapRat)
- Display items (SnowglobeDisplaycase)
- Allies (Dottie)
- Furniture (PemmicanCollector, WaterBoiler)
- Tempest armor linings (cut but still referenced)

### Event-Only Recipes (by event prefix)

| Event | Prefix | Recipe Count |
|---|---|---|
| Burning Springs | Burn_ | 88 |
| Storm Events | Storm_ | 88 |
| Moon Events | MOON_/Moon_ | 83 |
| Meat Week | Meat_ | 23 |
| Invaders from Beyond | Invaders_ | 17 |
| Bounty Hunter | BOUNTY_ | 61 |
| Fasnacht | Various | Several (steins, masks) |

### Cap-Purchasable Plans

Standard vendor plans purchased with caps are the base COBJ records without ATX, SCORE, event, or gold vendor conditions. These are the recipes that appear in standard vendor inventories and are restocked daily.

---

## 12. Hidden Crafting Bonuses

### Workbench Types (11 confirmed)

| Keyword | FormID | Purpose |
|---|---|---|
| Workbench_Crafting_Cooking | 0x00102152 | Food recipes |
| Workbench_Crafting_Chemlab | 0x00102158 | Chem/drug recipes |
| Workbench_Crafting_Tinkers | 0x00012FF2 | Ammo, grenades, mods |
| Workbench_Crafting_Weapon | 0x001F6049 | Weapon mods/crafting |
| Workbench_Crafting_Armor | 0x001F6062 | Armor mods/crafting |
| Workbench_Crafting_PowerArmor | 0x004EA39F | PA mods/crafting |
| Workbench_Crafting_Brewing | 0x0047ACF3 | Alcoholic beverages |
| Workbench_Crafting_Fermenter | 0x003FFAEB | Fermentation station |
| Workbench_Crafting_Cannery | 0x007AC62A | Canning recipes |
| Workbench_Crafting_Refrigerator | 0x005621F7 | Food preservation |
| Workbench_Crafting_Freezer | 0x006F31D8 | Deep freeze preservation |

### Workbench Variants (same function, different visuals)

Multiple animation keywords exist for visual variants of the same workbench:
- Cooking: Standard stove, spit, grill, Fuzzy grill, minecart grill, animalistic, fishing stove, cake maker
- Weapons: Standard, Enclave, Pegasus
- Chemistry: Standard, Harmaceutical
- Tinker's: Standard, Mr. Fuzzy

**No hidden crafting bonuses based on workbench variant or location.** The game only checks the `Workbench_Crafting_*` keyword, not which visual variant is used.

### Perk Stacking

Crafting perks are designed with anti-stacking conditions:
- Each rank checks `HasPerk(higher_rank) == 0` before applying
- Example: Ammosmith01 checks `HasPerk(Ammosmith02) == 0`
- This means only the highest equipped rank applies

### ATX Mechanic Companion Perks

Two companion-granted crafting perks found:
- `ATX_COMP_Mechanic_Perk_CraftingWorkshop` (0x0061F69D) - Bonus when crafting at workshop
- `ATX_COMP_Mechanic_Perk_RepairItems` (0x0061F693) - Bonus when repairing items

These are tied to an Atom Shop companion and provide passive crafting bonuses.

---

## Power Armor Crafting Curves

PA components use a unique tiered curve system based on component rarity. The X axis encodes BOTH the PA tier (in decades) and component slot (in units):

### PA Curve Structure
X values 10-15 = Raider PA, 20-25 = T-45, 30-35 = T-51b, 40-45 = T-60, 50-55 = Ultracite/X-01

Within each decade, X+0 = base, X+1 through X+5 = component slots (helmet, torso, arms, legs).

| Rarity Tier | Base Cost (per tier) | Max Cost (per tier) |
|---|---|---|
| Super Common (steel, etc.) | 9 | 25 |
| Common (aluminum, etc.) | 7 | 20 |
| Uncommon (gears, etc.) | 5 | 17 |
| Rare (springs, etc.) | 4 | 14 |
| Very Rare (circuits, etc.) | 3 | 9 |

**Key finding**: Between each decade (tier), the cost drops to 0 at X+9 before jumping to the next tier. This is the curve table's way of encoding "this material is not used for this PA tier" at certain levels.

---

## Flux/Nuke Flora Crafting

### Stable Flux Recipe (constant, not level-scaled)
- 10 raw flux (any color) per craft
- 1 Glowing Mass
- 1 Hardened Mass
- 1 High-Radiation Fluids

All five flux colors (blue/cobalt, orange/fluorescent, purple/violet, red/crimson, yellow/yellowcake) use identical 1:1 linear curves for raw flora input.

---

## Brewing/Fermentation System

### Fermentation Timers
- **Short fermentation**: 30 minutes (constant across all levels)
- **Long fermentation**: 60 minutes (constant)

### Ingredient Scaling (by recipe tier 1-3)

| Ingredient Type | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Primary | 2 | 3 | 3 |
| Water | 2 | 3 | 3 |
| Flavor | 1 | 2 | 2 |
| Rare | 1 | 1 | 1 |
| Wood (fuel) | 2 | 5 | 5 |

### Hangover Effects (by tier)
All hangover stats (Agility, Perception, Strength) scale identically:
- Tier 1: -1
- Tier 2: -2
- Tier 3: -3

---

## Food Crafting Tiers

Cooking recipes use a 4-tier complexity system:

| Component | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Primary meat/veggie | 0 | 1 | 2 | 3 |
| Secondary ingredient | 0 | 0 | 2 | 3 |
| Flavor seasoning | 0 | 0 | 2 | 2 |
| Water | 0 | 0 | 2 | 2 |
| Wood (fuel) | 0 | 1 | 1 | 1 |

Steaks are special: always 1 primary at tier 2.

### Food Health Curves (healing values)

Cooked meat healing scales with food quality:
| Quality Level | Health Restored |
|---|---|
| 1 | 240 HP |
| 2 | 324 HP |
| 5 | 437 HP |
| 7 | 590 HP |
| 10+ | 797 HP (cap) |

---

## Legendary Crafting Cost Curves

### Adding Legendary Slots (Legendary Modules)
| Stars | Modules Required |
|---|---|
| 1-star | 5 |
| 2-star | 10 |
| 3-star | 15 |
| 4-star | 20 |

### Attaching Legendary Effects (Legendary Scrip Cost)
Aggressive exponential scaling:
| Complexity | Scrip Cost |
|---|---|
| 1 | 10 |
| 2 | 15 |
| 3 | 25 |
| 5 | 70 |
| 7 | 135 |
| 10 | 270 |
| 13 | 450 |
| 15 | 595 |
| 17 | 760 |
| 20 | 1,000 (cap) |

### Crafting Legendary Modules
| Tier | Module Cost |
|---|---|
| 1 | 15 |
| 2 | 30 |
| 3 | 60 |
| 4 | 120 |

### Legendary Scrap Returns
| Stars | Scrip Returned |
|---|---|
| 0 | 0 |
| 1 | 100 |
| 2 | 200 |
| 3 | 300 |
| 4 | 400 |

---

## Smelting System

Ore smelting at Chemistry Workbench uses level-based scaling:

| Ore Amount | Acid Required | Ore Required |
|---|---|---|
| 10 | 2 | 3 |
| 20 | 2 | 3 |
| 30 | 3 | 3 |
| 40 | 4 | 5 |
| 50 | 5 | 7 |

---

## Summary Statistics

| Metric | Value |
|---|---|
| Total COBJ records | 21,934 |
| Active recipes (excluding cut/deprecated) | ~19,574 |
| Cut/disabled recipes (zzz_ + CUT_ + DEL_) | ~1,260 |
| Deprecated recipes | ~95 |
| Crafting material types | 34 |
| Workbench types | 11 |
| Crafting perks (active) | 20+ |
| Cut crafting perks | 10+ |
| Gold bullion gated recipes | 64 |
| Atom Shop recipes | 4,169 |
| Scoreboard recipes | 2,176 |
| Complete cut weapon systems | 3 (Laser Musket, Junk Jet, Incinerator) |
| Cut legendary effects | 15+ |
| Cut robot crafting recipes | 200+ |
