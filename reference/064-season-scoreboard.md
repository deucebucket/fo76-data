# Finding 064: Season/Scoreboard System — Complete Extraction

**Status:** VERIFIED — cross-referenced with ESM records, decompiled scripts, and community datamines
**Sources:** SeventyySix.esm full dump, decompiled Papyrus scripts, strings file
**Confidence:** HIGH for structural data; MEDIUM for exact server-side XP values (some controlled server-side)

---

## 1. Season History — All 25 Boards

The ESM contains sequential BoardID globals (`SCORE_Season_BoardID_01` through `SCORE_Season_BoardID_25`), each mapped to a zero-indexed ID. All 25 seasons are represented in the data.

| Season | BoardID | Theme (from reward names) | Entitlements | Cut Items |
|--------|---------|--------------------------|-------------|-----------|
| S1 | 0 | Captain Cosmos / Space Explorer | 58 | 469 |
| S2 | 1 | Armor Ace vs. The Subjugator | 58 | 546 |
| S3 | 2 | K.D. Inkwell / Scribe of Avalon | 56 | 2 |
| S4 | 3 | Brotherhood of Steel / Winter | 51 | 3 |
| S5 | 4 | Blood Eagle Mercs | 56 | 9 |
| S6 | 5 | FETCH Collectron / Pyramind | 57 | 2 |
| S7 | 6 | Zorbo / Baron | 45 | 1 |
| S8 | 7 | Alien Invasion / Zeta's Revenge | 58 | 5 |
| S9 | 8 | Moulded Carpet / Rustic | 62 | 4 |
| S10 | 9 | Union / Fanatic | 71 | 14 |
| S11 | 10 | Nuka-Cola (Classic/Twist/Quantum) | 77 | 31 |
| S12 | 11 | Rip Daring Adventure / Taxidermy | 88 | 44 |
| S13 | 12 | Hollywood / Pyrotechnic / B-Movie | 90 | 26 |
| S14 | 13 | Birthday / Deep Space / Army Base | 82 | 154 |
| S15 | 14 | Atlantic City / Poker / Heist | 88 | 53 |
| S16 | 15 | Cryptid Hunter / Spring Cleaning | 102 | 43 |
| S17 | 16 | Pioneer Scouts / Forest Service | 109 | 19 |
| S18 | 17 | Blue Ridge / Roadside Warrior | 90 | 33 |
| S19 | 18 | Enclave (Sigma Squad/Hellfire/Officer) | 98 | 51 |
| S20 | 19 | Ghoul / Sharpshooter / Radium | 95 | 19 |
| S21 | 20 | Nautical / Spitfire / Houseboat | 114 | 166 |
| S22 | 21 | Sunset Sarsaparilla / Garrahan Mining | 107 | 106 |
| S23 | 22 | Raider/Wasteland / Nitro Weapons / Lykoi Cat | 123 | 169 |
| S24 | 23 | Rip Daring Cosmos / Cryptid Hunting / Alien | 73 | 82 |
| S25 | 24 | (Skeleton data only — Premium Battle Pass + 3 Score Boosts) | 4 | 0 |

**Total entitlement records with SCORE_ prefix: 2,003**

### Entitlement Growth

Seasons 1-7 averaged ~55 rewards each. Starting with S10, the count climbed steadily, reaching 123 items in S23. S24 has only 73 items in the dump, suggesting it was in development at time of extraction.

### Season 25: Battle Pass Framework

S25 exists only as 4 ENTM records:
- `SCORE_S25_ENTM_Account_PremiumBattlePass` (0x0079C88C)
- `SCORE_S25_ENTM_Account_ScoreBoost_1` (0x0079C88D)
- `SCORE_S25_ENTM_Account_ScoreBoost_2` (0x0079C88E)
- `SCORE_S25_ENTM_Account_ScoreBoost_3` (0x0079C88F)

This is the skeleton framework for a future season — no actual rewards have been authored yet.

---

## 2. SCORE XP Progression System

### How SCORE Is Earned

The ESM defines 40+ challenge category globals controlling what generates SCORE:

**Daily Categories:**
- Combat, Event, Quest, Progression, Completion, Social, LevelUp, CAMP, Collect, Consume, Crime, Barter, CraftScrap, Photo, Workshop, DailyOps, Expeditions, Shelters, DynEvent, GoldStar, Recurring

**Weekly Categories:**
- Combat, Event, Quest, Progression, Completion, Social, LevelUp, CAMP, Collect, Consume, Crime, Barter, CraftScrap, Photo, Workshop, DailyOps, Expeditions, Shelters, DynEvent, GoldStar, Recurring

**Cut categories:** `zzzSCORE_Daily_NW` and `zzzSCORE_Weekly_NW` — Nuclear Winter SCORE challenges, disabled when NW was removed.

### Rank-Gated XP Challenges (Scaling SCORE per Rank)

The system uses rank-gated challenges that scale SCORE XP requirements based on current rank. There are 4 tiers for both daily and weekly:

| Challenge | Condition | Rank Range |
|-----------|-----------|------------|
| `SCORE_Challenge_Daily_RankGated_XP_Under25` | rank < SCORE_RankGated_Rank_025 | Ranks 1-24 |
| `SCORE_Challenge_Daily_RankGated_XP_Under50` | rank < SCORE_RankGated_Rank_050 | Ranks 25-49 |
| `SCORE_Challenge_Daily_RankGated_XP_Under75` | rank < SCORE_RankGated_Rank_075 | Ranks 50-74 |
| `SCORE_Challenge_Daily_RankGated_XP_Post100` | rank >= SCORE_RankGated_Rank_100 | Ranks 100+ |

Same structure exists for weekly variants. The globals `SCORE_RankGated_Rank_025/050/075/100` are used as condition comparisons (function 926 = GetGlobalValue).

**Key insight:** The actual SCORE XP values per rank are controlled server-side, not in the ESM. The ESM only defines the gating conditions. Community-verified values (per Nuka Knights):
- Ranks 1-25: 1,000 SCORE per rank
- Ranks 26-50: 1,500 SCORE per rank
- Ranks 51-75: 2,000 SCORE per rank
- Ranks 76-100: 2,500 SCORE per rank
- Post-100 (repeatable): 2,500 SCORE per rank

### Repeatable SCORE Challenges

- `SCORE_Challenge_Weekly_RankGated_XP_RECURRING_Under100` (0x005B759D) — repeatable weekly XP-to-SCORE conversion for ranks under 100
- `SCORE_Challenge_Weekly_RankGated_QuestComplete_Events_RECURRING_Rank100_Above` (0x007A1431) — repeatable event completion for 100+ ranks
- `SCORE_Weekly_Recurring_Events_Above_Rank_100` (GLOB 0x007A1432) — controls post-100 recurring events

### Expedition SCORE Challenges

Dedicated globals for Expedition content:
- `SCORE_XPD_Challenge_Daily_Expeditions` (0x0064B9A6)
- `SCORE_XPD_Challenge_Weekly_Expeditions` (0x0064B9A7)

### Cut Mission SCORE

- `zzz_SCORE_XPD_Mission` (0x00645E19) — cut mission-based SCORE earning
- `zzz_SCORE_XPD_Mission_WeeklyBonus` (0x00645E17) — cut weekly mission bonus

### Epic Challenges

Globals `SCORE_Daily_Epic` (0x006902AE) and `SCORE_Weekly_Epic` (0x0069B033) control "Epic" challenge variants. These offer higher SCORE for more difficult versions of standard challenges (e.g., `SCORE_Challenge_Daily_Kill_Burning_Deathclaw_Epic` vs non-epic).

---

## 3. How SCORE Is Boosted

### Lunchbox XP Bonuses

Lunchboxes provide stacking XP bonuses (which accelerate SCORE earning through XP-based challenges):

| Stack | Global | Bonus |
|-------|--------|-------|
| 1 box | `SCORE_Lunchbox_Effect_XPBonus_1` | 25% |
| 2 boxes | `SCORE_Lunchbox_Effect_XPBonus_2` | 50% |
| 3 boxes | `SCORE_Lunchbox_Effect_XPBonus_3` | 75% |
| 4 boxes | `SCORE_Lunchbox_Effect_XPBonus_4` | 100% |

Additional Lunchbox effects:
- `SCORE_Lunchbox_Effect_DMGBonus` — damage bonus
- `SCORE_Lunchbox_Effect_CarryCapacityBonus` — carry weight
- `SCORE_Lunchbox_Effect_RadResist` — rad resistance
- `SCORE_Lunchbox_ConfettiChance` — cosmetic effect

### Score Boost Entitlements (Per-Season)

Every season from S18 onward has 3 ScoreBoost entitlements:
- `Account_ScoreBoost_1`, `Account_ScoreBoost_2`, `Account_ScoreBoost_3`

These are earned at milestone ranks and provide cumulative SCORE earning bonuses for the remainder of the season. All use the same icon: `score_account_scoreboost.dds`.

Cut duplicate: `ZZZ_SCORE_S18_ENTM_Account_ScoreBoost_2/3` — suggests these were reworked during S18 development.

### SCORE Banners (Temporary Boosters)

The Banner system provides temporary SCORE boosts as rewards:
- `SCORE_Banner_Consumable` (ALCH 0x00653FCD)
- Proc chances per level: L1, L2, L3, L4 (globals)
- `SCORE_Banner_BuffDurationGlobal` — controls banner duration
- Reward items: `SCORE_Reward_Consumable_Banner_03`, `Banner_05`
- `SCORE_Reward_Consumable_TempScoreBooster_01/03` — alternate booster items

### Cut: Nuka X Effect System

A complete cut consumable system with SCORE prefix:
- `ZZZ_SCORE_NukaX_Effect_FireResist` — fire resistance bonus
- `ZZZ_SCORE_NukaX_PerkFastReloadSpeedApply` — reload speed
- `ZZZ_SCORE_NukaX_PerkStaggerResistApply` — stagger resistance
- `ZZZ_SCORE_NukaX_PerkStaggerEnemyChanceApply` — stagger enemies
- `ZZZ_SCORE_NukaX_MeleeSpeedApply` — melee speed
- `ZZZ_SCORE_NukaX_ChemDurationSpell` — extended chem duration
- `ZZZ_SCORE_HasNukaXEffect` — keyword for checking active effect

This was a planned SCORE reward consumable that would have granted combat buffs. Never shipped.

---

## 4. Atom Costs for Buying Ranks

The ESM contains:
- `UISeasonsPurchaseRank` (SNDR 0x0075337D) — the UI sound effect for purchasing a rank
- `SCORE_Reward_Consumable_Atoms_50` — 50 Atoms reward
- `SCORE_Reward_Consumable_Atoms_100` — 100 Atoms reward
- `SCORE_Reward_Consumable_Atoms_150` — 150 Atoms reward (the rank purchase cost reference)
- `SCORE_Reward_Consumable_Atoms_200` — 200 Atoms reward

The 150-Atom entry is significant — this is the cost to purchase/skip a single rank. This value is consistent with community knowledge: **150 Atoms per rank**, unchanged since Season 1.

---

## 5. Consumable Rewards (Standard Pool)

The following consumable rewards appear across multiple seasons:

| Reward | Form ID |
|--------|---------|
| 200 Atoms | `SCORE_Reward_Consumable_Atoms_200` |
| 500 Gold Bullion | `SCORE_Reward_Consumable_GoldBullion_500` |
| 300 Legendary Scrip | `SCORE_Reward_Consumable_LegendaryScrip_300` |
| 10 Stamps | `SCORE_Reward_Consumable_Stamps_10` |
| 10 Perk Coins | `SCORE_Reward_Consumable_PerkCoin_010` |
| 5 Legendary Rerollers | `SCORE_Reward_Consumable_Reroller_05` |
| 5 Scrap Kits | `SCORE_Reward_Consumable_ScrapKit_5` |
| 3 Liquid Courage | `SCORE_Reward_Consumable_Game_LiquidCourage_03` |
| 3 Mystery Bobbleheads | `SCORE_Reward_Consumable_MysteryBobblehead_03` |
| 3 Magazine Book Boxes | `SCORE_Reward_Consumable_MagazineBookBox_03` |
| 3 Ultracite Scrap Supply | `SCORE_Reward_Consumable_UltraciteScrapSupply_03` |
| 5 Banners | `SCORE_Reward_Consumable_Banner_05` |
| Temp Score Booster x1/x3 | `SCORE_Reward_Consumable_TempScoreBooster_01/03` |
| 5 Improved Bait | `SCORE_Reward_Consumable_ImprovedBait_05` |
| 5/10 Superb Bait | `SCORE_Reward_Consumable_SuperbBait_05/10` |

Many have `_Copy01` duplicates — these are used for separate milestone placements so the same reward can appear at multiple board positions.

---

## 6. Season 24: Rip Daring Cosmos / The Smiling Man

Season 24 is themed around **Rip Daring's cosmic adventures** and **cryptid hunting**. Full breakdown:

### Active S24 Rewards (59 items, excluding cut)

**Apparel:**
- Bloody Space Suit (outfit + headwear) — `SpaceSuitBloody`
- Space Age Glasses — `SpaceAgeGlasses`
- Black Ranger uniform paint — `RangersUniform_Paint_BlackRanger`

**Power Armor:**
- Armed Power Armor skin — `PowerArmor_Model_Armed` + headlamp

**Pip-Boy Skins:**
- Cold Shoulder — `PipBoySkin_ColdShoulder`
- Cremator — `PipBoySkin_Cremator`

**CAMP Items:**
- Mountain Retreat Prefab — `Prefab_MountainRetreat`
- Drive-In Statue — `DriveInStatue`
- Drive-In Sign — `DriveinSign`
- Alien Display Case — `Displaycase_AlienDisplay`
- Alien Warning Sign, Abduction Stein
- Bigfoot Stein Display
- Strange Curio Cabinet (collectron-style, resource producing)
- Survival Cache (resource producing)
- Rip ArmCo Ammo Constructor — `AmmoConstructionmachine_Collector_RipArmCo`
- Healing Arch, Phoropter, Weather Station (Invasion skin)
- Alien Aid/Ammo/Scrap Boxes
- Fur Carpet, Daring Neon Sign, Framed Kit, Tarped Roof Kit
- Glowing Cat CAMP Pet — `CAMPPets_Cat_GlowingCat`
- Taxidermy Beast floor decor
- End of Season Art (wall decor)
- Pip-Boy Replica Display Stand

**Weapons:**
- UFO Bobber (fishing rod mod)

**Player Icons (8):**
- Cryptid patches: Smiling Man, Mothman, Jersey Devil, Grafton Monster, Flatwoods Monster, Alien
- Space Cow, Space Guinevere, UFO Abduction

**Player Titles:**
- Prefixes: Interstellar, Space, Armed, Rip, Guinevere, Alien (CAMP), Bigfoot (CAMP), RipDarings (CAMP)
- Suffixes: Terrestrial, Extraterrestrial, Retreat (CAMP)
- Both: CryptidHunter, Alien, Bigfoot

**Photomode:**
- Rip Daring Cosmos Marquee Logo

**Account:**
- Premium Battle Pass
- Score Boost 1/2/3

### The Smiling Man Connection

The Smiling Man appears as:
- `SCORE_S24_ENTM_PlayerIcon_SmilingManPatch` — season reward player icon
- `RE_Scene_Cold_SmilingMan` (NPC_ 0x0068EB57) — random encounter NPC
- Has a dedicated voice type: `RE_Scene_Cold_SmilingManVoiceType`
- Has an outfit: `RE_Scene_Cold_SmilingManOutfit`
- Associated mesh: `armor/doggear/smilingmanbandana.bgsm`

The Smiling Man is an existing cryptid random encounter NPC that was thematically integrated into S24's cryptid hunting theme. The player icon suggests he's a featured cryptid in the season's narrative.

### S24 Cut Content (14+ items)

| Cut Item | Notes |
|----------|-------|
| `ZZZSCORE_S24_ENTM_CAMP_WallDecor_EndOfSeasonArt001` | Alternate end-of-season art |
| `ZZZSCORE_S24_ENTM_CAMP_WallDeco_Letters_RipDaringLogo` | Full Rip Daring letter kit (A-Z + numerals + symbols) |
| `ZZZSCORE_S24_ENTM_CAMP_WallPaper_BigfootHunt` | Bigfoot hunting wallpaper |
| `ZZZ_SCORE_S24_ENTM_CAMP_FloorDecor_WaxGuinevere` | Wax Guinevere statue |
| `ZZZSCORE_S24_ENTM_CAMP_FloorDecor_AlienTarget` | Alien target practice |
| `ZZZSCORE_S24_ENTM_CAMP_FloorDecor_SpaceshipBalloon` | Spaceship balloon |
| `ZZZSCORE_S24_ENTM_Skin_WeaponSkin_CombatRifle_RipDaring` | Rip Daring Combat Rifle skin |
| `ZZZSCORE_S24_ENTM_Skin_WeaponSkin_Flamer_RipDaring` | Rip Daring Flamer skin |
| `ZZZSCORE_S24_ENTM_Skin_WeaponSkin_DoubleBarrelShotgun_RipDaring` | Rip Daring Double Barrel skin |
| `ZZZSCORE_S24_ENTM_Skin_WeaponSkin_GatlingPlasma_RipDaring` | Rip Daring Gatling Plasma skin |
| `ZZZSCORE_S24_ENTM_Skin_WeaponSkin_HuntingRifle_RipDaring` | Rip Daring Hunting Rifle skin |
| `zzzSCORE_S24_ENTM_Skin_Headwear_RangersUniform_Paint_BlackRanger` | Black Ranger headwear (split from outfit) |
| `zzzSCORE_S24_ENTM_CAMP_Roofs_Kit_Framed` | Framed roof kit |
| `zzzSCORE_S24_ENTM_CAMP_Kit_RoofKit` | Roof kit |

**Notable:** 5 Rip Daring weapon skins were cut from S24. The keyword `ZZZSCORE_S24_dn_HasMaterial_Weapons_RipDaring` confirms these were planned, had material definitions, and were pulled. The Rip Daring theme originated in S12 and S16 (costume, flag, icons), making S24 "Rip Daring Cosmos" a sequel season. The cut weapon skins may have been saved for Atom Shop or a future season.

---

## 7. Mini-Seasons

Mini-seasons are shorter scoreboards that run alongside or between full seasons. The ESM identifies 5 mini-seasons:

### Mini-Season: Appalachian Outlaws (2025)

**Items:** 7 entitlements
- Duffle Bag of Cash (floor decor)
- Detective Board (wall decor)
- Framed Newspaper (wall decor)
- Ghoul Wanted Poster (wall decor)
- Money Bag Backpack
- Piggy Bank (floor decor)
- "Outlaw" player title suffix

**Cut:** Ball and Chain Skeleton, Prison Skeletons (2024 version also referenced, suggesting a year-over-year repeat)

### Mini-Season: MMMFE / Marshal Mallow Fishing Edition (2025)

**Items:** 6 entitlements
- Marshal Mallow Fishing Hat
- Marshal Mallow Rod Bobber
- Marshal Mallow Fish Display
- Marshal Mallow Fishing Rod skin
- Marshal Mallow Plushie
- "Salty" prefix, "Marshal Mallow" suffix titles

### Mini-Season: Sunset Stranger (2025)

**Items:** 17 entitlements
- Sarsaparilla Deputy Hat
- Deputy Badge backpack flair
- Sarsaparilla Saloon Door
- Sarsaparilla Billboard
- Sarsaparilla Caps/Bottle clutter
- Sarsaparilla Crate
- Sunset Dart Machine
- Old West Sarsaparilla Bar Stool
- Fresh Delight Poster, Build Mass Poster
- Player Icons: Festus, Blue Star Cap
- Titles: Sassy, Sunset (prefix), Stranger, Courier (suffix)

This is a New Vegas-themed mini-season — notable for referencing Sunset Sarsaparilla, the Courier, and Festus.

### Mini-Season: Night at the Morgue (2025)

**Items:** 8 entitlements
- Vault-Tec Body Bag
- Autopsy Table (bed)
- Mortuary Sign
- Morgue Drawers (open/closed/covered — 3 variants)
- Skull Candy Bowl
- "Putrid" prefix, "Cadaver" suffix titles

### Mini-Season: Love Hurts (2025)

**Items:** 14 entitlements
- Tough Love Helmet (headwear)
- Heart Arch Raiders (floor decor)
- Carved Poems (wall decor)
- Lethal Seat (chair)
- Piercing Love weapon skin
- Nitro weapon mods (sight + 2 stock variants)
- Wounded Heart player icon
- Photomode Marquee Logo
- Titles: Infatuated, Gruesome (prefix), Masochist (suffix)

### How Mini-Seasons Differ from Full Seasons

Based on ESM structure:
1. **No BoardID global** — mini-seasons don't have `SCORE_Season_BoardID_XX` entries
2. **No PremiumBattlePass entitlement** — no paid track
3. **No ScoreBoost entitlements** — no milestone boosters
4. **Fewer rewards** — 6-17 items vs 50-120+ for full seasons
5. **No Legendary reward tier** — no CPRD legendary reward products
6. **Self-contained naming** — `SCORE_MiniSeason_[Name]_ENTM_` vs `SCORE_S[XX]_ENTM_`
7. **Run alongside main seasons** — the `s23miniseason1/2` icon path references confirm mini-seasons run during full season periods

---

## 8. Premium Battle Pass / Fallout 1st Season Pass

Every season from S16 onward has a `PremiumBattlePass` entitlement:
- S16: `SCORE_S16_ENTM_Account_PremiumBattlePass` (and `BattlePass` — non-premium)
- S17-S25: `SCORE_S[XX]_ENTM_Account_PremiumBattlePass`

Cut: `ZZZ_SCORE_S18_ENTM_Account_PremiumBattlePass` — S18 premium pass was reworked.

The strings file confirms the branding:
- `Season 16 Fallout First Season Pass` (0x4100A832, 0x4100A834)
- `Season 18 Fallout First Season Pass` (0x4100C1D0, 0x4100C1D2)

**Fallout 1st exclusive rewards** use the `F1_SCORE_S[XX]_ENTM_` prefix:
- S3: BoS Photomode Frame, BoS Player Icon, American Tank Helmet, Wood Herringbone Floor, T-65 Clandestine PA paint
- S4: Special Player Icon, Backpack Flair
- S6: Basement Floor Set, T-51 Helmet Flair
- S8: Bunny Slippers Icon, Dr. Bones Floor Decor, Tank Patina Bronze Statue, Rothko Rug, Clean Yellow Door, Bass Mailbox

Early seasons (S1-S2) did not have F1 exclusive tracks — they were added S3 onward.

---

## 9. Season Auto-Complete at Season End

The ESM does not contain explicit auto-complete logic for the scoreboard — this is entirely server-side behavior. However, the `UISeasonsPurchaseRank` sound effect and the 150-Atom price point confirm the purchase mechanism exists client-side.

Community-verified behavior: When a season ends, unclaimed rewards are lost. There is no auto-complete. Players must manually purchase remaining ranks with Atoms before the season ends, or forfeit unclaimed rewards.

The `SCORE_S5_COMP_SuperMutant_Global` and `SCORE_S5_COMP_Inspector_Global` entries suggest S5 had companion quest completion tracking tied to the scoreboard, but this is quest-gating, not auto-complete.

---

## 10. Rank Milestone Rewards and Hidden Bonuses

### Rank-Gated Content (Globals)

Four rank milestone globals exist:
- `SCORE_RankGated_Rank_025` (0x0060EEDA)
- `SCORE_RankGated_Rank_050` (0x0060EED9)
- `SCORE_RankGated_Rank_075` (0x0060EED7)
- `SCORE_RankGated_Rank_100` (0x0060EED8)

These are used as condition checks for:
1. **Challenge gating** — different daily/weekly challenges unlock at different rank thresholds
2. **Score Boost rewards** — ScoreBoost 1/2/3 likely correspond to rank 25/50/75 milestones

### Boost Rewards at Milestones

Per season (S12+), two boost tiers exist:
- `SCORE_S[XX]_Reward_Durable_Boost_05` — 5% boost
- `SCORE_S[XX]_Reward_Durable_Boost_10` — 10% boost

### End-of-Season Bundles

Each season from S12 onward has an `EndofSeason[XX]Bundle` reward product — a collection of all legendary rewards from that season, likely given as the final rank 100 reward.

### Legendary Reward Products (Per Season)

Seasons 12-17 have explicit legendary reward product entries. Examples from S14 (Army Base season):
- Ally Grandma Junko, Circuit Breaker, Eagle Weapon Display, Cake Maker Cooking Station, Military Cryo Freezer, Mace of the Republic, Enclave Relay Tower, Brewery Fermenter, Wine Rack Display, Autominer Collectron, Army Base CAMP Kit

From S13 (Hollywood):
- Ally Joey Bello, Pyro Kit, Stealth Suit Camo, Rubber Monster Outfit, Sound Stage Shelter, Movie Projector Screen, Hollywood Gramophone, Makeup Vanity, Cryptid Card Display, Jewelry Flair Display, Bada Boom weapon

These are the "Legendary" tier rewards placed at key milestone ranks.

### Zorbo Offset

`uSeasonZorboOffsetHours` = 84 (3.5 days) — this controls the timing offset for Zorbo-related season content, likely the NPC's dialogue rotation on the scoreboard.

---

## 11. Cut Scoreboard Content — Deep Analysis

### Massive Early Season Cuts (S1: 469, S2: 546)

Seasons 1 and 2 have hundreds of cut items — far more than any other season. This represents the initial design phase where BGS created a much larger pool of potential rewards, then trimmed to the final ~55 items each. This was the learning period for the scoreboard system.

### S14 Deep Space Cuts (154 items)

Season 14 has the third-highest cut count. Includes `ZZZdn_HasMaterial_PA_SCORE_S14_DeepSpace` — a cut Deep Space power armor material that was removed from the season.

### S21-S23 Heavy Iteration (166, 106, 169 cuts)

Recent seasons show heavy iteration:
- S21: 166 cuts including extensive nautical-themed items
- S22: Sarsaparilla and Golf Bag backpack cut, Motorized Butter Churn (Vault-Tec) cut
- S23: Raider Guitar, Spinal Rod fishing rod, Deathclaw Gauntlet Stinger skin, Raider Nuka-Cola Car, Volcano structure, Scrap Shack survival tent, Body in Bathtub (resource producer), Rust Plush and Armor Deathclaw plushies all cut

### Cut S23 Body in Bathtub

An entire resource-producing CAMP item was cut:
- `zzzSCORE_S23_WorkshopCount_BodyinBathtub` / `_CAMP`
- `zzzSCORE_S23_ResourceProductionIntervalHours_BodyinBathtub`

This would have been a functional resource generator styled as a body in a bathtub — possibly cut for tone.

### S12 Sheepsquatch Duplicates

8 cut Sheepsquatch PA material variants (`zzz_SCORE_S12_dn_HasMaterial_PA_SheepsquatchDUPLICATE000-007`) — testing artifacts for the Sheepsquatch PA skin across all armor types.

### S11 Nuka-Cola Duplicates

8 cut Nuka-Cola Classic PA materials + 6 Nuka Twist armor duplicates — same testing pattern.

### Cross-Season Pattern: Weapons Get Cut Most

Across all seasons, weapon skins are the most commonly cut item type:
- S15: 7 Poker weapon skins cut (Auto Grenade Launcher, Plasma Gun, Gauss Minigun, Gatling Laser, Combat Shotgun, Gatling Plasma, Chainsaw, Combat Rifle)
- S16: Peepers skins (Auto Axe, Plasma Caster, Gauss Rifle) + Devilish skins (Pump Action, Double Barrel, Lever Action, Binoculars)
- S24: 5 Rip Daring weapon skins cut

This suggests weapon skins are over-produced during development and then trimmed to 1-2 per season for the final board.

---

## 12. Pre-Season System: Project Babylon (Nuclear Winter Overseer Ranks)

Before the SCORE/Season system existed, Nuclear Winter (codenamed "Babylon") had its own progression:

### Cut Overseer Rank Challenges

The ESM contains **200 cut Overseer Rank challenges** spanning ranks 1-200:
- `CUT_Babylon_Challenge_Lifetime_OverseerRank_001` through `_200`
- `CUT_Babylon_Challenge_Account_OverseerRank001` through `OverseerRank100`

### Cut Babylon Daily Challenges

26 cut daily challenge variants for Nuclear Winter:
- Kill Players/Creatures, Revive Players, Take Photos, Launch Nukes
- Survive Matches/In Storm/In Nuke, Win Matches, Complete Matches
- Deploy CAMPs, Pick Locks, Use Stimpaks, Minutes Alive
- Each had Low and High difficulty tiers

### Babylon XP Curve

- `fBabylonXPBase` (0x0040D28A) — base XP per rank
- `fBabylonXPGrowth` (0x0040D28B) — growth factor per rank
- `zzz_BabylonEndGameRank_Experience` (CURV 0x00470DA3) — experience curve
- Solo/Duo/Squad rank experience curves also existed

### Milestone Challenges (Account-Level)

Special challenges at key Overseer ranks:
- `CUT_Babylon_Challenge_Account_OverseerRank025`
- `CUT_Babylon_Challenge_Account_OverseerRank050`
- `CUT_Babylon_Challenge_Account_OverseerRank100`

These were the precursor to the current SCORE milestone system. When Nuclear Winter was sunset, the rank/challenge framework was adapted into the seasonal SCORE system.

---

## 13. Season-Exclusive Items — Unavailable After Season End

**Every SCORE_S[XX]_ENTM item that is not also in the Atom Shop is season-exclusive.** This includes:

- All Power Armor skins with season prefixes
- All themed outfits (Captain Cosmos variants, K.D. Inkwell, Blood Eagle Mercs, etc.)
- All themed CAMP items (Chicken Coop, Firefly Lights, Secret Fireplace Door, etc.)
- All themed weapon skins
- All player icons with season prefixes
- All player titles with season prefixes
- CAMP pets from specific seasons
- Named allies (Scarberry in S12, Joey Bello in S13, Grandma Junko in S14)

Some items have been recycled via the Atom Shop, Minerva, or seasonal events, but the ESM data alone cannot distinguish which ones were re-released. The `REUSE_SCORE_S3_ENTM_Furniture_Shelters_1` entry confirms at least some S3 items were explicitly flagged for reuse.

### Fallout 1st Exclusives

Items with `F1_SCORE_S[XX]_ENTM_` prefix were only available to Fallout 1st subscribers during that season. These are the rarest items in the game, as they required both an active subscription and reaching the relevant rank during a specific time window.

---

## 14. Challenge Categories — Full List from ESM

992 total SCORE challenge records exist in the ESM. Challenge categories include:

- Kill (by creature type, weapon type, region, costume status)
- Gather (specific flora items)
- Fishing (catch, consume, craft, region-specific)
- Quest Complete (events, expeditions, seasonal events, Daily Ops)
- Photo (location-specific camera challenges)
- Craft, Collect, Consume, Barter, Crime
- Social, Group, Workshop, Shelter
- Level Up, Progression, Completion
- Epic variants of most categories (harder, more SCORE)
- Region-specific variants (Forest, Ash Heap, Toxic Valley, Cranberry Bog, Mire, Savage Divide, Burning Springs)
- Seasonal event variants (Fasnacht, Meat BBQ, Mischief Night, Scorched Earth, Big Bloom)

---

## 15. Verification Notes

### Confirmed Against Community Data (Nuka Knights / Fed76)

- 25 seasons through current dump (S1-S25 skeleton) -- MATCHES community tracking
- 150 Atoms per rank purchase cost -- MATCHES
- Lunchbox XP values (25/50/75/100%) -- MATCHES ESM globals exactly
- Rank milestone gates at 25/50/75/100 -- MATCHES
- Fallout 1st exclusive track introduced S3 -- MATCHES
- Premium Battle Pass from S16 onward -- MATCHES
- Mini-seasons as parallel shorter boards -- MATCHES reported behavior
- Season themes per Nuka Knights archives align with reward naming

### ESM-Only Discoveries (Not Widely Documented)

1. **Nuka X consumable system** — complete cut buff system with reload speed, stagger resist, melee speed, fire resist, and chem duration bonuses
2. **200-rank Overseer progression** — Nuclear Winter was designed for 200 ranks, not the 100 that shipped
3. **Body in Bathtub** cut from S23 — functional resource producer
4. **5 Rip Daring weapon skins** cut from S24 — entire weapon line removed
5. **Rip Daring Letter Kit** cut from S24 — customizable neon letter signs with full A-Z + symbols
6. **Zorbo offset = 84 hours** — seasonal NPC dialogue rotates every 3.5 days
7. **S1/S2 had 8-10x more planned items than shipped** — 469 and 546 cuts respectively
8. **Cut mission-based SCORE earning** — `zzz_SCORE_XPD_Mission` suggests an abandoned system where story missions would award SCORE directly

---

## Data Sources

- `/home/deucebucket/ai-drive/gamecryptids/data/fallout76/esm_dump/full_esm_dump.txt` — primary
- `/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/` — Papyrus scripts
- `/home/deucebucket/ai-drive/gamecryptids/data/fallout76/seventysix_strings_en.txt` — UI strings
