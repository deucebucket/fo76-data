# Fallout 76 Fishing System — Complete Technical Analysis

**Finding ID:** 063
**Date:** 2026-03-20
**Data Sources:** ESM dump, decompiled scripts, leveled list analysis
**Status:** VERIFIED — system is live with hidden mechanics documented below

---

## 1. System Overview

Fishing was added in Season 21 (The Mire expansion). It is a full minigame system with dedicated FISH records (71 total in the ESM), a custom XP source (`XPSource_FishCaught = 17` in Player.psc), weather-driven probability tables, regional loot pools, and a persistent Lovecraftian narrative layer centered on **Fisherman's Rest** and its two NPCs.

Key locations:
- **Fisherman's Rest** — hub location in The Mire, has its own fog weather (`Fishing_Weather_FishermansRest_Fog`), custom LUT color grading (`lutfishermansrest01.dds`), and loadscreen
- **Ohio River Adventures** — existing raider fish camp (Fishbones/Blackeye NPCs, mirelurk meat turn-ins)
- Fishing spots scattered across all 8 regions (7 original + Burning Springs)

---

## 2. Fish Species — Complete Catalog

### 2.1 Generic Fish (available in all regions)

| Fish | Size | Form ID | Notes |
|------|------|---------|-------|
| Brook Silverside | Small | `007CE510` | Common generic |
| Redbelly | Small | `007CE50C` | Common generic |
| Sunscream | Small | `007CE528` | Common generic |
| Yellow Bullhead | Medium | `007CE50D` | Common generic |
| Walleye | Medium | `007CE526` | Common generic |
| Smoky Salmon | Medium | `007CE524` | Common generic |
| Chain Pickerel | Medium | `007CE529` | Common generic |
| Ridge Trout | Medium | `007CE513` | Common generic |

### 2.2 Region-Specific Fish

**Forest Region** (`Fishing_FishType_Forest`):
| Fish | Size | Form ID |
|------|------|---------|
| Kanawha Piranha | Small | `007CE520` |
| Glowing Kanawha Piranha | Small (Glowing) | `007CE522` |
| Timber Sawgill | Small (Universal) | `007CE523` |
| Bloodwhisker | Large | `007D2B00` |

**Ash Heap** (`Fishing_FishType_AshHeap`):
| Fish | Size | Form ID |
|------|------|---------|
| Sooty Sawgill | Small (Universal) | `007CE51A` |
| Ashen Ambusher | Medium | `007CE51C` |
| Glowing Ambusher | Medium (Glowing) | `007CE521` |
| Deathjaw | Large | `007D2AFF` |

**Savage Divide** (`Fishing_FishType_SavageDivide`):
| Fish | Size | Form ID |
|------|------|---------|
| Leatherback | Small | `007CE514` |
| Alpine Sawgill | Small (Universal) | `007CE515` |
| Armored Spinefish | Large | `007CE50F` |
| Glowing Spinefish | Large (Glowing) | `007CE51D` |

**The Mire** (`Fishing_FishType_Mire`):
| Fish | Size | Form ID |
|------|------|---------|
| Spikesnapper | Small | `007D2B04` |
| Muddy Sawgill | Small (Universal) | `007CE512` |
| Gulpy | Large | `007CE527` |
| Glowing Gulpy | Large (Glowing) | `007CE51E` |

**Cranberry Bog** (`Fishing_FishType_CranberryBog`):
| Fish | Size | Form ID |
|------|------|---------|
| Blisterfish | Small | `007CE51B` |
| Bog Sawgill | Small (Universal) | `007CE51F` |
| Bog Lurker | Medium | `007D2B02` |
| Glowing Bog Lurker | Medium (Glowing) | `007D2B03` |

**Toxic Valley** (`Fishing_FishType_ToxicValley`):
| Fish | Size | Form ID |
|------|------|---------|
| Noxious Sawgill | Small (Universal) | `007CE519` |
| Potbelly Kelt | Large | `007CE50E` |
| Glowing Potbelly Kelt | Large (Glowing) | `007D2B01` |
| Purple Radpole | Large | `007CE517` |

**Skyline Valley** (`Fishing_FishType_SkylineValley`):
| Fish | Size | Form ID |
|------|------|---------|
| Static Sawgill | Small (Universal) | `007CE518` |
| Bluefin Zapper | Medium | `007CE516` |
| Stormswimmer | Large | `007CE511` |
| Glowing Stormswimmer | Large (Glowing) | `007D2AFE` |

**Burning Springs** (`Fishing_FishType_BurningSprings`) — **NEWEST REGION**:
| Fish | Size | Form ID | Notes |
|------|------|---------|-------|
| Burning Springs Sawgill | Small (Universal) | `008482A4` | `Burn_` prefix |
| Burning Springs Walleye | Medium | `008482A7` | Unique model: `burningspringswalleye.nif` |
| Two-Headed Fish | Medium | `008482A5` | Unique model: `burningsprings_twoheadedfish.nif` |
| Glowing Two-Headed Fish | Medium (Glowing) | `008482A6` | `burningsprings_twoheadedfishglowing.nif` |

### 2.3 Sawgill Sub-Species (Universal Fish)

Every region has its own Sawgill variant, all tagged `Fishing_FishType_Sawgill` (`007FE7BD`). These are "universal" small fish that appear in their home region and cross-pollinate loot lists. The keyword `Fishing_FishType_Sawgill` functions as a cross-region catch mechanic — 8 total Sawgill variants exist (one per region including Burning Springs).

### 2.4 Axolotls — Collectible Sub-System

12 Axolotl variants exist, tagged with `Fishing_FishType_Axolotl` (`00800713`). These are a dedicated collection system with their own challenge tree:

| Axolotl Variant | Form ID |
|-----------------|---------|
| Charcoal Axolotl | `0080070C` |
| Pink Axolotl | `00800708` |
| Brown Axolotl | `00800704` |
| Dotted Axolotl | `0080070E` |
| Purple Axolotl | `00800709` |
| Banded Axolotl | `0080070D` |
| Scaled Axolotl | `00800711` |
| Striped Axolotl | `00800710` |
| Shadow Axolotl | `0080070A` |
| Spotted Axolotl | `0080070F` |
| Speckled Axolotl | `0080070B` |
| Stone Axolotl | `00800706` |

**CUT Axolotls:** `zzz_Fishing_Fish_Small_Axolotl02_PeachAxolotl` (`00800707`) and `zzz_Fishing_Fish_Small_Axolotl02_StoneAxolotl` (`00800705`) — two additional variants were cut. The Peach Axolotl shares the `_02` index with Pink, suggesting it was replaced during development.

---

## 3. Local Legend Fish (Legendary / Boss-Tier)

Tagged with `Fishing_FishType_LocalLegend` (`00804F7E`). Locations that can spawn them have `LocTypeFishingLocalLegend`. Four confirmed:

| Local Legend | Form ID | Material Swap | Notes |
|-------------|---------|---------------|-------|
| **Maw-Begotten** | `00804F7A` | `actors/fish/locallegend/mawbegotten.bgsm` | **THE LOVECRAFTIAN FISH** — name suggests eldritch/cosmic horror origin |
| **Wavy Willard** | `00804F7B` | `actors/fish/locallegend/wavywillard.bgsm` | Named after the Wavy Willard's water park |
| **Organ Grinder** | `00804F7C` | `actors/fish/locallegend/organgrinder.bgsm` | Visceral name implies grotesque appearance |
| **Deathjaw** | `0085A4F8` | `actors/fish/fish_large/characterassets/alligatorgar_deathjaw.nif` | Burning Springs local legend, alligator gar model |

### Ryl-Tkannoth Connection

The "Maw-Begotten" name is significant. "Maw-Begotten" implies being spawned/born from a great maw — an enormous mouth or void. This connects to the broader Lovecraftian undertone in FO76's aquatic lore:

- The `Eldritch_Deity_Font` static object (`0013B7EF`) exists with model `setdressing/eldritch_deity_font/eldritch_deity_font.nif`
- "The Deep One" fog crawler variants exist: `actors/dlc03/fogcrawler/characterassets/thedeepone.nif` with Scorched, Seaweed, Glowing, and Albino material swaps — direct H.P. Lovecraft "Deep Ones" reference
- The Fisherman NPC at Fisherman's Rest makes "creepy fish person noises" (quest direction: `NAM2: "Makes fish-person noises"`) and "Creepy fish person noises" — suggesting he is partially transformed
- Captain Raymond is described as "Struggling to speak as the Fisherman controls his brain" and "Momentarily breaks out of his reverie, but then the Fisherman checks him with searing head pain"
- The Fisherman speaks in "unintelligible words" that Captain Raymond "translates" with an "Ominous, creepy, foreboding" tone

**HIDDEN MECHANIC:** The Fisherman is NOT a normal NPC — he appears to be a fish-human hybrid controlling Captain Raymond telepathically. The quest narrative implies the fishing system's lore is that something in Appalachia's waters is transforming people, consistent with the "Maw-Begotten" local legend name. Linda-Lee (the creature you feed fish bits to at the Chum Trough) has custom "eating" animations — she's another fish-creature being sustained by player catches.

---

## 4. Bait Types and Effects on Catch Probability

Three bait tiers exist as MISC items:

| Bait | Form ID | Effect |
|------|---------|--------|
| Common Bait | `007AC1AF` | Baseline probabilities |
| Improved Bait | `007FDC33` | Better odds for uncommon/rare fish |
| Superb Bait | `007FDC32` | Best odds for Local Legends and Axolotls |

The game has a `Fishing_BaitLootChanceNone` global (`007DC633`) that controls the base failure rate.

**CUT: Region-Specific Bait** — An entire system of region-specific bait was designed and then cut (all `zzz_` prefixed):
- `zzz_Fishing_Workshop_Recipe_DefaultBait`
- `zzz_Fishing_Workshop_Recipe_AshHeapBait`
- `zzz_Fishing_Workshop_Recipe_CranberryBogBait`
- `zzz_Fishing_Workshop_Recipe_ForestBait`
- `zzz_Fishing_Workshop_Recipe_SavageDivideBait`
- `zzz_Fishing_Workshop_Recipe_SkylineValleyBait`
- `zzz_Fishing_Workshop_Recipe_TheMireBait`
- `zzz_Fishing_Workshop_Recipe_ToxicValleyBait`
- `zzz_Fishing_Workshop_Recipe_GlowingBait`

This would have been a CAMP-craftable bait system with 9 region-specific variants. The workshop statics also exist (`zzz_Fishing_workshop_DefaultBait`, etc.) and the old baited leveled lists survive as `zzz_Fishing_LLS_*_CommonBaited` / `_ImprovedBaited` / `_GlowingBaited`.

**CUT: Glowing Bait List** — `zzz_Fishing_BaitList_Glowing` (`007AE145`) was a fourth bait tier specifically for catching glowing fish. Cut in favor of the current three-tier system.

---

## 5. Catch Probability System

The probability system uses **84 global variables** that form a 3D matrix:

**Axes:**
1. **Weather:** NoWeather, RainWeather, NukeWeather
2. **Bait:** CommonBait, ImprovedBait, SuperbBait
3. **Fish Category:** GenericFish, CommonRegionFish, UnCommonRegionFish, GlowingFish, LocalLegendFish, Axolotl

### Global Variable Naming Pattern
```
Fishing_Odds_{Weather}_{Bait}_{FishCategory}
```

Example globals:
- `Fishing_Odds_NoWeather_CommonBait_GenericFish` — baseline, most common outcome
- `Fishing_Odds_NukeWeather_SuperbBait_LocalLegendFish` — best possible Local Legend odds
- `Fishing_Odds_NoWeather_SuperbBait_Axolotl` — Axolotl odds with top bait
- `Fishing_Odds_RainWeather_SuperbBait_Axolotl` — rain bonus for Axolotls

**Key insight:** Rain and Nuke Zones each modify catch tables independently. The system checks weather via `Fishing_RNG_WeatherGlowingFishChance` (`007D2B05`) for glowing fish specifically.

### Weather Check Architecture
Each region has 6 weather-check leveled lists:
- `Fishing_LLS_{Region}_WeatherCheck_None`
- `Fishing_LLS_{Region}_WeatherCheck_Rain`
- `Fishing_LLS_{Region}_WeatherCheck_Nuke`
- `Fishing_LLS_{Region}_WeatherCheck_Radstorm`
- `Fishing_LLS_{Region}_WeatherCheck_CAMP_Rain` (CAMP shelter proximity)
- `Fishing_LLS_{Region}_WeatherCheck_CAMP_Radstorm`
- `Fishing_LLS_{Region}_WeatherCheck_CAMP_None`
- `Fishing_LLS_{Region}_WeatherCheck_CAMP_Radstorm`

**HIDDEN:** CAMP-based weather checks exist! The `_CAMP_` variants suggest fishing near your CAMP has separate weather detection logic, possibly factoring in CAMP weather machines or shelter proximity.

### Burning Springs Weather — Sandstorm Fishing
Burning Springs adds a **sandstorm** weather condition for fishing:
- `Fishing_IsCampSandstormWeather_Condition` (`008974E5`)
- `Fishing_IsNaturalSandstormWeather_Condition` (`008974E4`)
- 5 tiers of sandstorm fishing challenges: `Burn_Challenge_Lifetime_Fishing_FishInSandStorm_01` through `_05`

This is the only region with a unique weather type for fishing probability.

---

## 6. Nuke Zone Fishing

When a nuke zone overlaps a fishing spot, the catch tables shift to `_NukeWeather_` globals. The probability matrix shows nuke zones affect EVERY fish category:

- `Fishing_Odds_NukeWeather_CommonBait_GenericFish`
- `Fishing_Odds_NukeWeather_CommonBait_CommonRegionFish`
- `Fishing_Odds_NukeWeather_CommonBait_UnCommonRegionFish`
- `Fishing_Odds_NukeWeather_CommonBait_GlowingFish`
- `Fishing_Odds_NukeWeather_CommonBait_LocalLegendFish`
- `Fishing_Odds_NukeWeather_ImprovedBait_*` (6 categories)
- `Fishing_Odds_NukeWeather_SuperbBait_*` (6 categories)

**Note::** Nuke zones have their own complete probability tables (18 globals for nuke weather alone). Nuking a fishing spot does NOT just increase glowing fish — it shifts the entire loot table, potentially increasing Local Legend odds as well (`Fishing_Odds_NukeWeather_SuperbBait_LocalLegendFish`).

---

## 7. Junk Catches

Two tiers of junk items can be caught:

**Common Junk (5 pools):**
- `Fishing_Fish_Junk_Common01` through `Common05`
- Leveled list: `Fishing_LLS_Junk_Common` (`00829631`)

**Rare Junk (5 pools):**
- `Fishing_Fish_Junk_Rare01` through `Rare05`
- Leveled list: `Fishing_LLS_Junk_Rare` (`00829632`)
- Controlled by `Fishing_Odds_Junk_Rare` (`00829630`)

**XP for Junk:** The `PlayerFishingScript` has `bXPForJunk = True` by default, using `GenericCatchXPGlobal` — you DO get XP for fishing up junk.

---

## 8. Waterlogged Gifts (Seasonal Event Fish)

Three seasonal FISH records exist that are NOT actual fish but gift containers:

| Gift | Form ID | Notes |
|------|---------|-------|
| Waterlogged Gift Tier 01 | `0086451E` | Lowest tier |
| Waterlogged Gift Tier 02 | `0086451F` | Mid tier |
| Waterlogged Gift Tier 03 | `0086451D` | Best tier |

These are controlled by:
- `LTT_WaterLoggedGifts_Toggle` (`00864521`) — master on/off switch
- `LTT_Odds_WaterLoggedGifts` (`00864520`) — catch probability
- `Fishing_LL_LTT_WaterLoggedGifts` (`00864522`) — leveled list

Corresponding consumable rewards:
- `Festive_WaterLoggedHolidayGift_Loot_Tier_01/02/03` — ALCH items containing actual loot

**HIDDEN:** These only appear when the toggle global is set to 1 (during holiday events). They are injected into the fishing loot tables alongside normal catches.

---

## 9. XP System

XP is granted via `PlayerFishingScript` using a struct-based lookup system. XP source is `XPSource_FishCaught = 17`.

### XP Globals by Fish Category:

| Category | Global ID | Notes |
|----------|-----------|-------|
| Junk | `XP_Fishing_FishCaught_Junk` (`007EEE2B`) | Lowest, optional via `bXPForJunk` |
| Small | `XP_Fishing_FishCaught_Small` (`007EEE2C`) | Base small fish |
| Small Glowing | `XP_Fishing_FishCaught_Small_Glowing` (`007EEE29`) | Higher than base small |
| Medium | `XP_Fishing_FishCaught_Medium` (`007EEE2A`) | Mid-tier |
| Medium Glowing | `XP_Fishing_FishCaught_Medium_Glowing` (`007EEE28`) | Higher than base medium |
| Large | `XP_Fishing_FishCaught_Large` (`007EEE2D`) | High tier |
| Large Glowing | `XP_Fishing_FishCaught_Large_Glowing` (`007EEE27`) | Very high |
| Axolotl | `XP_Fishing_FishCaught_Axolotl` (`008157F5`) | Special category |
| Local Legend | `XP_Fishing_FishCaught_LocalLegend` (`008157F6`) | Highest XP |
| MQ Common | `XP_Fishing_MQ_Common` (`007C7336`) | Quest-specific XP |

The `FishExperienceValues` property maps `FishSizeKeyword` to both regular `XPGlobal` and `GlowingXPGlobal` — each size has TWO XP values. The `bDirectXP` flag can bypass Intelligence scaling and entry point adjustments.

---

## 10. Fishing Rod System

### Rod Base Skins (Cosmetic)

| Rod Skin | Keyword / Form ID | Source |
|----------|-------------------|--------|
| Janky Rod | `Fishing_dn_RodBase_JankyRod` (`007BABD3`) | Default/starter |
| Bicycle Rod | `Fishing_dn_RodBase_Bicycle` (`007B2372`) | Craftable |
| Ruby Reel Rod | `Fishing_dn_RodBase_RubyReel` (`007B2375`) | Season 21 SCORE |
| Shishkebab Rod | ATX (`007B2374`) | Atom Shop |
| Charmcaster | ATX (`00809318`) | Atom Shop (also ZZZ cut S21 version) |
| Well-Kept Rod | ATX (`008482A8` / `00841312`) | Atom Shop |
| Atomic Cast | ATX (`0085724F`) | Atom Shop |
| Marshal Mallow Rod | SCORE Mini-Season 2025 | Season reward |

**CUT Rod Skins:**
- `ZZZ_SCORE_S23_Fishing_dn_RodBase_SpinalRod` — Season 23 Spinal Rod (vertebrae-themed?)
- `ZZZ_Fishing_dn_RodBase_MantaMan` — Season 22 Manta Man Rod

### Rod Functional Upgrades (OMOD)

| Upgrade | OMOD Form ID | Craft Recipe |
|---------|-------------|--------------|
| No Upgrade (default) | `007A95BC` | — |
| Stabilized Gear Ratio | `007B2379` | `co_Fishing_mod_FishingRod_Weapon_Upgrade_StabilizedGearRatio` |
| Steady Handle | `007B237A` | `co_Fishing_mod_FishingRod_Weapon_Upgrade_SteadyHandle` |
| Advanced Drag | `007B237B` | `co_Fishing_mod_FishingRod_Weapon_Upgrade_AdvancedDrag` |
| Improved Bearing | `007B237C` | `co_Fishing_mod_FishingRod_Weapon_Upgrade_ImprovedBearing` |
| Attractive Hook | `007DB4C1` | `co_Fishing_mod_FishingRod_Weapon_Upgrade_AttractiveHook` |

The `Fishing_ReelCatchSpeedMultiplier` AVIF (`007B2365`) suggests upgrades modify reel speed during the minigame.

### Fishing Line Upgrades (5 tiers)

| Line Upgrade | OMOD Form ID | Notes |
|-------------|-------------|-------|
| Line Upgrade 01 | `007FE7BE` | `ap_FishingLineUpgrade` keyword |
| Line Upgrade 02 | `007FE7C2` | |
| Line Upgrade 03 | `007FE7C1` | |
| Line Upgrade 04 | `007FE7BF` | |
| Line Upgrade 05 | `007FE7C0` | |

### Bobber Cosmetics (19 total)

**Base Game Bobbers:**
- Flamewood Float, Red Tide Float, Mossy Meadow, Twin Timber Float, Festive Float, Crimson Stripe Float, Skyfire Float, Pin Bobber, Rocket, Nuka-Cola Quantum

**Season/ATX Bobbers:**
- Nuka-Cola, Baby Rattle, Grenade, Light Bulb (Season 21)
- Eye of Ra (Season 22)
- Glowing Skull (ATX)
- Atomic Swimmer (ATX)
- Marshal Mallow (Mini-Season 2025)
- UFO Bobber (Season 24)
- Doll Head (Burning Springs)

All bobbers have both display (`_Display_*_Misc`) and animated (`_animated.nif`) variants.

---

## 11. Chum Trough & Linda-Lee System

### Chum Trough Mechanics
- Location: Fisherman's Rest (`Fishing_ChumTroughRef` at `007AED29`)
- AV tracking: `Fishing_ChumTrough_AV` (`007C62AB`)
- Reward threshold: `Fishing_ChumTrough_RewardThreshold` global (`007C62B0`)
- Deposit options: Fish Bits (regular) and Glowing Fish Bits
- Deposit messages: `Fishing_ChumTrough_DepositFishBitsMessage` and `DepositGlowingFishBitsMessage`
- Enabled flag: `Fishing_FishBitsDepositEnabled` (`008020FD`)

### Reward System
When the deposit counter reaches the threshold, players receive rewards from:
- `Fishing_LLS_ChumTrough_Weapon` (`0081193B`)
- `Fishing_LLS_ChumTrough_Armor` (`0081193C`)
- `Fishing_LLS_ChumTrough_PowerArmor` (`0081193D`)

**HIDDEN:** The Chum Trough gives **weapons, armor, AND power armor** as rewards — not just food or fishing items. The `DepositCountMultiplier` in the script allows different items to have different deposit values.

### Linda-Lee
- Custom animation system: `LindaLeeAnimationManager` handles eat animations (`StartEating` event)
- `LindaLeeEatSound` — custom sound for feeding
- Status system: `LindaLeeStatuses` array with `Location TextLoc` (display names) and `MaxValue` thresholds — Linda-Lee has MULTIPLE satisfaction states based on how much she's been fed
- Feeding Linda-Lee during the intro quest sets quest progress stages

---

## 12. Fish Cooking & Crafting

### Fish Bits (base crafting ingredient)
- Regular Fish Bits: `Fish_Fishbits` (`007CE310`)
- Glowing Fish Bits: `Fish_Fishbits_Glowing` (`007CE311`)
- Every fish can be scrapped into Fish Bits via `Fishing_Fish_CO_Meal_FishbitsFrom*` recipes

### Cooked Fish Meals
| Meal | Form ID | Glowing Variant |
|------|---------|-----------------|
| Grilled Fish | `007B2B9A` | `007D34A5` |
| Fish Chowder | `007B3FB6` | `007D34A6` |
| Fish and Tatos | `007AED80` | `007D34A4` |

**Cannery Variants** (pre-packaged):
- `Fishing_GrilledFish_Cannery` (`00804719`)
- `Fishing_FishChowder_Cannery` (`00804717`)
- CUT: `ZZZ_Fishing_GrilledFish_Glowing_Cannery`, `ZZZ_Fishing_FishChowder_Glowing_Cannery`

---

## 13. Quests

### Casting Off (Main Fishing Quest)
- **Quest ID:** `Fishing_MQ01_Casting` (`007ACB4C`)
- **Trigger:** Entering The Mire region (`Fishing_MQ01_ChangeLocation` quest)
- **Alternative trigger:** Activating a barrel at Fisherman's Rest (`BarrelTriggerScript`)
- **Radio quest:** `Fishing_MQ01_Casting_Radio` (`007D18D3`) — broadcasts to draw players
- **Steps:** Arrive at Fisherman's Rest → Speak to Fisherman → Pick up rod and bait → Catch 3 fish → Create fish bits → Feed Linda-Lee
- **Rewards:** Fishing rod weapon (`Fishing_FishingRod`), default bait, fishing enabled system-wide
- **Player tracking:** `Fishing_MQ01_FishCaught` AV, `RefCol_CaughtFish` collection alias

### Big Fish in a Small Pond (Repeatable Daily)
- **Quest ID:** `Fishing_BigFish` (`007B95E1`)
- **NPC:** Captain Raymond Clark
- **Mechanic:** Randomly selects a region via `ChosenRegionAV`, player must catch **7 fish** (`totalRequiredFish = 7.0`) in that region
- **Stages:** `canFishNowStage = 200`, `allFishCaughtStage = 270`
- **Region stages:** `RegionStages` array maps region AV values to quest stages
- **Checkpointing:** `FishCaughtAV` persists between sessions
- **Reward:** `LegendaryToken_Daily_Fishing` (`007DC662`) — legendary scrip

### Captain Raymond's Holotapes
- Quest: `Fishing_CaptainRaymond_Holotapes` (`007D4362`)
- 3 holotape scenes: `CaptainsLog01/02/03_Scene`
- 2 books: `Fishing_CaptainRaymondDiary01` (`007BD0A4`), `Fishing_CaptainRaymondDiary02` (`007C62B2`)

### Ohio River Adventures (Pre-Fishing Raider Content)
- System quest: `W05_Community_RaiderFishCamp` — raider NPCs Fishbones and Blackeye
- Mirelurk meat turn-in system (`HowManyTurnInsAVRef`, once per day `OncePerDayAVRef`)
- Defend quest: `W05_Com_RFC_Defend` — EWS-style defense event
- NOT directly connected to the fishing minigame system

---

## 14. Challenges & Achievements

### Lifetime Fishing Challenges (Permanent)

**Regional Completion (per region):**
- Catch all common fish in region
- Catch unique fish #1 in region
- Catch unique fish #2 in region
- Catch glowing fish in region
- META challenge per region completing all sub-challenges
- `Challenge_Lifetime_Fishing_AllRegions_META` — master completion

**Progress Tiers (skill progression):**
| Tier | Required Catches | Example SUBs |
|------|-----------------|--------------|
| Progress 01 | Any Small fish, Any Medium fish | `_AnySmall_SUB`, `_AnyMedium_SUB` |
| Progress 02 | Kanawha Piranha, Leatherback, Any Sawgill | Specific species |
| Progress 03 | Ashen Ambusher, Bluefin Zapper, Any Axolotl | Harder species |
| Progress 04 | Deathjaw, Purple Radpole, Glowing Bog Lurker | Largest/rarest |

**Quantity Challenges:**
- `Challenge_Lifetime_Fishing_Any_01` through `_04` — catch X total fish
- `Challenge_Lifetime_Fishing_AnyGlowing_01` through `_03` — catch X glowing fish
- `Challenge_Lifetime_Fishing_CompleteDailies_01` through `_03` — complete X daily quests

**Special Collections:**
- `Challenge_Lifetime_Fishing_CatchAxolotls` — catch any Axolotl
- `Challenge_Lifetime_Fishing_Axolotl_01_SUB` through `_12_SUB` — catch each specific Axolotl
- `Challenge_Lifetime_Fishing_Axolotls_META` — catch ALL 12 Axolotls
- `Challenge_Lifetime_Fishing_Any_LocalLegend` — catch any Local Legend
- `Challenge_Lifetime_Fishing_LocalLegend_01` through `_03` — catch specific legends
- `Burn_Challenge_Lifetime_Fishing_LocalLegend_04` — Deathjaw (Burning Springs)

**Local Legend Challenge Rewards:**
- `ChallengeReward_Challenge_Lifetime_Fishing_LocalLegend_Caps` — caps
- `ChallengeReward_Challenge_Lifetime_Fishing_LocalLegend_Modules` — legendary modules
- `ChallengeReward_Challenge_Lifetime_Fishing_LocalLegend_TreasuryNotes` — treasury notes
- `ChallengeReward_Challenge_Lifetime_Fishing_LocalLegend_SuperbBait` — superb bait

**Burning Springs Challenges:**
- `Burn_Challenge_Lifetime_Fishing_BurningSprings_SUB_Sawgill/TwoHeaded/TwoHeadedGlowing/Walleye`
- `Burn_Challenge_Lifetime_Fishing_Any_BurningSprings_01` through `_05`
- `Burn_Challenge_Lifetime_Fishing_FishInSandStorm_01` through `_05` — FISH DURING SANDSTORMS

### SCORE Challenges (Seasonal Rotators)

**Daily:**
- Catch regular fish (any region)
- Catch fish in specific region (Forest/Ash Heap/Savage Divide/Mire/Cranberry Bog/Skyline Valley/Toxic Valley/Burning Springs)
- Craft fish bits
- Consume regular fish / fish bits
- Catch fish while intoxicated (`SCORE_Challenge_Daily_Fishing_Catch_While_Intoxicated`)
- Catch fish while NOT intoxicated (epic variant)

**Weekly:**
- Catch regular fish (quantity)
- Catch regular fish in rain
- Craft fish bits (quantity)

### CUT Challenges
- `ZZZ_SCORE_Challenge_Weekly_Fishing_Catch_Glowing_Fish` — weekly glowing fish catch (cut)
- `CUT_Challenge_Weekly_Fishing_Survival` — fishing in Survival mode (entire subtree cut)
- `CUT_Challenge_Weekly_Fishing_SUB_CranberryBogQuest_Survival`
- `CUT_Challenge_Weekly_Fishing_SUB_KillAquatic_Survival`
- `CUT_Challenge_Weekly_Fishing_SUB_CookAquatic_Survival`
- `CUT_Challenge_Weekly_Fishing_SUB_ClaimLakesideCabins_Survival`
- `CUT_Challenge_Daily_Kill_Mirelurks_while_wearing_Fishing_Gear_Camera` — kill mirelurks in fishing outfit
- `CUT_Challenge_Daily_Picture_Players_Creatures_wearing_FishingOutfit_fighting_MirelurkQueen_Camera` — photomode challenge
- `CUT_Challenge_Weekly_Kill_Aquatic_while_wearing_FishingHat` — kill aquatic enemies in fishing hat
- `CUT_Challenge_Weekly_Photomode_LakesPonds_SUB_FishingHole`

---

## 15. Bounty Fisherman (Burning Springs PvE Content)

A bounty hunting system related to fishing exists in Burning Springs:

| Record | ID | Notes |
|--------|----|-------|
| Regular Bounty Target | `Burn_BountyTarget_REG_Fisherman` (`008333E9`) | NPC_ record |
| Big Bounty Target | `Burn_BountyTarget_BIG_Fisherman` (`00833083`) | Boss variant |
| CUT Lite Bounty | `zzzBurn_BountyTarget_BIG_Fisherman_Lite` (`0083BD86`) | Cut easier version |
| Fisherman Cloak spell | `Burn_Bounty_FishermanCloak` (`008333EC`) | Area effect |
| Fisherman Effect | `Burn_Bounty_FishermanEffect` (`008333EB`) | Applied spell |
| Unhooking Ability perk | `Burn_Bounty_FishermanUnhookingAbility` (`0083BD8A`) | Enemy perk |
| Hooking Range effect | `Burn_Bounty_FishermanHookingRange` (`008333E8`) | MGEF |
| Dispel Unhookable | `Burn_Bounty_Fisherman_DispelUnhookable` (`0083E660`) | Counter-mechanic |

**HIDDEN MECHANIC:** The Bounty Fisherman is a hostile NPC that has a "hooking" attack (pulls players?), a cloak effect, and an "Unhookable" state that must be dispelled. This is a PvE boss that uses fishing-themed combat mechanics — unique to the Burning Springs bounty system.

---

## 16. Fishing Rod — The Weapon

The fishing rod is classified as a **weapon** (`WeaponTypeFishingRod`, `007995A5`) with keyword `ma_FishingRod` (`007995A6`). It was given to all players retroactively via `PlayerConnect_FishingRodCheck` quest (`0084B300`) — if a player logs in without a fishing rod, one is automatically added with an optional message.

Base weapon: `FishingRod` MISC (`00059B36`) — note the low form ID suggests very early asset creation.

The weapon uses dedicated animation sets:
- `AnimsFishingRodWeapon` (`007995A4`)
- `AnimFurnFishingSpot` (`007995A2`)
- `AnimFurnFisherman` (`007AC575`)

The fishing rod has a `NOCRAFT` recipe variant (`Fishing_co_Weapon_Melee_FishingRod_NOCRAFT` at `0082962A`), meaning it cannot be crafted at workbenches — only modifications can be applied.

---

## 17. CAMP and Display Items

### Fish Displays
- Fish Hook Display: `SCORE_S21_ENTM_CAMP_Display_FishDisplay_FishHook`
- Fish Tank: `ATX_ENTM_CAMP_Displaycase_FishTank`
- Bobber Display Case: `ATX_ENTM_CAMP_Displaycase_FishingBobber`
- Fishing Lure Rack: `ATX_ENTM_CAMP_DisplayCase_FishingLureRack`
- Fishing Rod Displays: Boat (`SCORE_S21`), Fish Head (`SCORE_S21`), Fungal (`ATX`)
- Fish Pond: `ATX_ENTM_CAMP_FloorDecor_FishPond`
- Marshal Mallow Fish Display (2025)
- Bobber Display keyword: `Fishing_FishingBobber_DisplayObject`
- Rod Display keyword: `Fishing_FishingRod_DisplayObject`

### CUT Displays
- `zzz_Fishing_workshop_FishDisplay_FishTank01` — earlier fish tank
- `zzz_Fishing_FishStand_01Activator` — fish stand

### Plushies (CAMP craftable)
- Angler Plushie: `Fishing_Workshop_MISC_AnglerPlushie` (`007A835A`)
- Crab Boat Plushie: `Fishing_Workshop_MISC_CrabBoatPlushie` (`007A8353`)
- Mirelurk Plushie: `Fishing_Workshop_MISC_MirelurkPlushie` (`007A834C`)

### Player Titles
- Angler: `SCORE_S21_ENTM_PlayerTitles_Suffix_Angler`
- Bobber: `SCORE_S21_ENTM_PlayerTitles_Suffix_Bobber`
- Fishing Finalist: `Community_ATX_ENTM_PlayerTitles_Suffix_FishingFinalist`

### Player Icons
- Fisher Vault Boy, Fish Pot, Linda-Lee, Burning Springs Fish

---

## 18. Cut Content Summary

### CUT Systems
1. **Region-Specific Bait (9 types)** — entire craftable bait system per region, would have added CAMP crafting depth
2. **Glowing Bait tier** — fourth bait quality specifically for glowing fish
3. **Survival Mode fishing challenges** — an entire challenge tree for the cut Survival mode
4. **Fishing outfit combat challenges** — kill mirelurks/aquatic creatures while wearing fishing gear
5. **Photomode fishing challenges** — take photos at fishing holes, of fishing with mirelurk queens
6. **Weekly glowing fish catch challenge** — replaced by other challenge types
7. **Glowing Cannery food** — pre-packaged glowing fish meals (2 of 3 cut)
8. **Fishing cutout** — CAMP item `zzzSCORE_S21_FishingCutout`
9. **Ceiling fishing nets** — `zzzSCORE_S21_CAMP_CeilingDecor_FishingNets`
10. **Fishing cooler loot bag** — `ZZZ_SCORE_S21_Skin_LootBag_FishingCooler`
11. **Scuba Tank backpack** — `zzz_Fishing_Recipe_Backpack_ScubaTank`
12. **Multiple rod skins** — Spinal Rod (S23), Manta Man Rod (S22), Charmcaster (S21 version)
13. **Doll Head Bobber recipe book** — `zzzBurn_Recipe_mod_FishingRod_RodBobber_DollHead`
14. **CUT fishing hat/outfit** — `CUT_ATX_Headwear_FishingOutfitHat`, `CUT_ATX_Clothes_FishingOutfit`
15. **Peach and Stone Axolotl** — two axolotl variants removed
16. **CUT old glowing fish-to-fishbits recipes** — 7 `zzz_` recipes for individual glowing fish scrapping

### CUT Workshop Items
- `zzz_Fishing_Workshop_Recipe_WallDecor_KelpCurtain`
- `zzz_Fishing_Workshop_Recipe_FishDisplay_Plaque`
- `ZZZ_Fishing_Workshop_Recipe_DrownedChaise`
- `ZZZ_Fishing_Workshop_Recipe_DrownedLamp_02`
- `zzz_Fishing_Workshop_Recipe_ReclaimedShipChandelier`
- `ZZZ_Fishing_Workshop_Recipe_StashBox_Seaweed`
- `ZZZ_Fishing_Workshop_Recipe_CreatureInAJar_Octopus` — **an octopus-in-a-jar CAMP item was planned**
- `zzz_Fishing_Workshop_Recipe_AnglerPlushie/CrabBoatPlushie/MirelurkPlushie` — plushie recipes cut (items still exist)

---

## 19. Game Settings (GMST)

| Setting | ID | Purpose |
|---------|----|---------|
| `bFishingUseLightingRig` | `00818AFD` | Toggle special fishing lighting |
| `fFishingMinBobDelay` | `0081138A` | Minimum bobber delay before bite |
| `fFishingMinigameFishOutRumbleIntensity` | `0080F9A0` | Controller rumble when fish escapes |
| `fFishingBaseReelSize` | `008082AD` | Base reel size for minigame |
| `fFishingBaseReelRotationSpeed` | `008082AC` | Reel rotation speed |

---

## 20. Key Hidden Findings

1. **The Fisherman is a fish-human hybrid** that telepathically controls Captain Raymond. This is buried in quest dialogue directions, not directly stated in game text.

2. **Nuke zone fishing has full probability tables** — it's not just "more glowing fish." Every fish category gets rebalanced under nukes, including Local Legends.

3. **CAMP weather checks exist separately** — fishing near your CAMP has different weather detection than wild fishing, possibly affected by CAMP weather machines.

4. **Sandstorm fishing** is a Burning Springs-exclusive mechanic with its own 5-tier challenge tree.

5. **The Chum Trough rewards weapons, armor, and power armor** — not just fishing-related items.

6. **Waterlogged Gifts inject into fishing loot** during holiday events via a toggle global.

7. **The Bounty Fisherman** is a PvE boss with fishing-themed combat (hooking attacks, unhookable state).

8. **14 Axolotl variants were planned** (12 shipped, 2 cut) — the Peach Axolotl was replaced by Pink.

9. **An entire region-specific bait crafting system was cut** — 9 bait types for CAMP crafting stations, one per region plus default and glowing.

10. **An octopus-in-a-jar** CAMP item was planned, along with kelp curtains, drowned furniture, a ship chandelier, and a seaweed stash box — suggesting a much more extensive underwater/nautical CAMP theme was planned.

11. **71 FISH records exist** in the ESM — a dedicated record type just for this system.

12. **Fish display size keywords** (`Fishing_DisplayOffset_Large`) affect how fish appear on display plaques.

13. **Linda-Lee has a multi-state satisfaction system** with named statuses and max thresholds — she gets progressively more "full" as players feed her.

14. **The fishing rod base item has form ID 00059B36** — an extremely low ID suggesting it was planned very early in development, possibly from the original FO76 design documents.

---

*Total FISH records: 71 | Total fishing scripts: 59 | Total ESM fishing references: 3,401*
*Regions with fishing: 8 (Forest, Ash Heap, Savage Divide, Mire, Cranberry Bog, Toxic Valley, Skyline Valley, Burning Springs)*
*Local Legends: 4 (Maw-Begotten, Wavy Willard, Organ Grinder, Deathjaw)*
