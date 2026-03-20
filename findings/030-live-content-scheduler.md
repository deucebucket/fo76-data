# FO76 Finding 030: Complete Live Content Scheduler (LCS/LCP/LTT) System Map

## Status: CONFIRMED NOVEL -- First complete map of Bethesda's three-layer remote content control infrastructure
## Source: GLOB_records.txt (11,009 globals), full_esm_dump.txt, 7,095 decompiled scripts
## Validation: Individual toggles known to dataminers; the three-layer SYSTEM architecture is undocumented

---

## Executive Summary

Fallout 76 uses a three-layer server-side control system that lets Bethesda remotely manipulate nearly every aspect of the game without pushing patches:

1. **LCP (Live Content Package)** -- Content activation layer. Turns entire features, quests, events, and content blocks on/off. Controls WHAT is available.
2. **LTT (Live Tuning Toggle)** -- Drop rate/reward tuning layer. Adjusts probabilities, amounts, and bonus rates. Controls HOW MUCH players get.
3. **Spotlight** -- Community event layer. Activates Double XP, Double Scrip, vendor bonuses. Controls PLAYER ECONOMY multipliers.

All three layers operate through GlobalVariable records in the ESM. The game client reads these globals at runtime; the server pushes new values without requiring a game update. Scripts check `GetValue()` on these globals to determine behavior.

---

## Layer 1: LCP (Live Content Package) -- The Master Switch Layer

LCP globals are the top-level content activation system. They control whether entire features, quest lines, events, and content blocks are available to players.

### Architecture (from decompiled scripts)

The `objectiverandomizer.psc` script explicitly documents the system:
> "For use with Live Content Packages. Use a unique GlobalVariable in each Mission for Each Objective. Default value should be 1. Use LCP to set a value of 0 to remove this objective from randomization"

The `dailymutation.psc` script confirms the naming:
> "The current mutation index -- gets set by the Live Content Scheduler"

The `festive_legendaryscorched.psc` script confirms scope:
> "A float value set in content scheduler to control percentage chance"

The `e01f_fasnacht_bossdropsmasks.psc` script confirms the toggle pattern:
> "The Boss Mask Drop Toggle -- Set By The Live Content Scheduler: Global Switch: 1 = Enable Boss MutatMask Drops, 0 = Disable Boss Mask Drops."

### Seasonal Event Master Switches

| LCP Global | FormID | What It Controls |
|-----------|--------|-----------------|
| LCP_E07A_Mothman | 0x00623C96 | Mothman Equinox event (entire event on/off) |
| LCP_E07B_Invaders | 0x006216CE | Invaders from Beyond event |
| LCP_E07B_Invaders_Week2 | 0x0063EE40 | Invaders Week 2 content phase |
| LCP_E07B_Invaders_DailyOps | 0x00635F95 | Invaders Daily Ops variant |
| LCP_E08A_Moonshine | 0x0064E8F5 | Moonshine Jamboree event |
| LCP_E08B_Eviction_Notice | 0x0064E70D | Eviction Notice event |
| LCP_E05_Caravan_Toggle | 0x0058C84B | Caravan event |
| LCP_SSE_BigBloom | 0x0079C38A | Big Bloom (Skyline Valley seasonal event) |
| LCP_SSE_BigBloom_EventPlaylist | 0x0079C38B | Big Bloom event rotation playlist |
| LCP_MN2_Mischief | 0x0077FA1C | Mischief Night 2.0 |
| LCP_MN2_Explosions | 0x00806B13 | MN2: Explodable cars/barrels enabled |
| LCP_MN2_Fanfare | 0x00806B15 | MN2: Success fanfare effects |
| LCP_MN2_Bonus | 0x00806B14 | MN2: Costume bonus multiplier |
| E02A_Meat_Enabled | 0x005C4F12 | Meat Week event |
| Festive_Holiday_Enabled | 0x0059CB08 | Holiday Scorched (Christmas) |
| Festive_Halloween_Enabled | 0x0059CB0A | Spooky Scorched (Halloween) |
| Spooky_EventEnabled | 0x0059CB09 | Spooky Scorched event system |
| TreasureHunt_EventEnabled | 0x005B72A1 | Treasure Hunter (Mole Miners) |
| TreasureHunt_CraftingEnabled | 0x005A75DF | Treasure Hunter pail crafting |

### Mothman Equinox Sub-Controls

| LCP Global | FormID | What It Controls |
|-----------|--------|-----------------|
| LCP_E07A_Mothman_SpecialEncounter_Enabled | 0x00621C35 | Special Mothman encounter toggle |
| LCP_E07A_Mothman_SpecialEncounter_SpawnChance | 0x00621C36 | Special Mothman spawn probability |

### Invaders From Beyond Sub-Controls

| LCP Global | FormID | What It Controls |
|-----------|--------|-----------------|
| LCP_E07B_Invaders_GeneralZetaGlowMask | 0x0083E310 | General Zeta glow mask drop toggle |
| LCP_E07B_Invaders_GeneralZetaGlowMask_ChanceNoneDropRate | 0x0083E311 | Glow mask drop probability |
| LCP_E07B_Invaders_PTSEventPlaylist | 0x0064811D | PTS-specific event playlist |

### The Backwoods (BURN) Content Progression System

"BURN" is the internal codename for the Backwoods expansion. LCP globals gate its quest progression:

| LCP Global | FormID | What It Controls |
|-----------|--------|-----------------|
| LCP_BURN_SQ01 | 0x00862153 | Side Quest 01 availability |
| LCP_BURN_SQ01_Radio | 0x00862152 | SQ01 radio broadcast |
| LCP_BURN_SQ02_OutroP1 | 0x00862563 | SQ02 Outro Part 1 |
| LCP_BURN_SQ02_OutroP2 | 0x00862564 | SQ02 Outro Part 2 |
| LCP_BURN_SQ04_DirtyLaundry | 0x00868F91 | "Dirty Laundry" side quest |
| LCP_BURN_MQ03_RustKingMid | 0x00868F90 | Main Quest 03 Rust King mid-point |
| LCP_BURN_Misc_BountyPinter | 0x00865FCD | Miscellaneous bounty: Pinter |
| LCP_Burn_DustDevil_Enable | 0x0086721D | Dust Devil world boss enable |
| zzzLCP_BURN_E01_Gear | 0x0085E064 | CUT: Gear event |
| zzzLCP_BURN_E02_Sinkhole | 0x0085E065 | CUT: Sinkhole event |
| zzzLCP_Disable_DirtyLaundry | 0x00863027 | DEPRECATED: Old DirtyLaundry disable |

**Key Finding**: The zzz-prefixed globals reveal that TWO Backwoods events were cut -- "Gear" (E01) and "Sinkhole" (E02). These were planned but removed before release.

### Skyline Valley (SSE/Big Bloom) Controls

| LCP Global | FormID | What It Controls |
|-----------|--------|-----------------|
| LCP_SSE_BigBloom | 0x0079C38A | Big Bloom event master switch |
| LCP_SSE_BigBloom_EventPlaylist | 0x0079C38B | Big Bloom playlist rotation |
| LCP_SSE_OvergrownFlowerDropChance_Cnone | 0x0085D7DC | Overgrown flower drop probability |

### Moonshot (MOON) System

| LCP Global | FormID | What It Controls |
|-----------|--------|-----------------|
| MOON_LCP_Toggle | 0x006D870E | Moonshot content master switch |
| MOON_LCP_Toggle_Dailies | 0x006DAEE4 | Moonshot daily quests toggle |

### The Drifter (P62) Keycard System

An elaborate LCP-controlled keycard drop system with per-activity-type probabilities:

| LCP Global | FormID | What It Controls |
|-----------|--------|-----------------|
| P62_LCP_TheDrifter_QuestKeycardEnabled | 0x0082D352 | Master keycard quest toggle |
| P62_LCP_TheDrifter_QuestKeycardReaderEnabled | 0x0082E198 | Keycard reader interactable toggle |
| P62_LCP_TheDrifter_KeycardChance_DailyOps | 0x008278F2 | Keycard drop chance from Daily Ops |
| P62_LCP_TheDrifter_KeycardChance_EventsPublic | 0x008278F3 | Keycard drop from public events |
| P62_LCP_TheDrifter_KeycardChance_EventsSeasonal | 0x008278F4 | Keycard drop from seasonal events |
| P62_LCP_TheDrifter_KeycardChance_EventsGeneric | 0x008278F5 | Keycard drop from generic events |
| P62_LCP_TheDrifter_KeycardChance_BlastZonesBoss | 0x0082D351 | Keycard drop from blast zone bosses |
| P62_LCP_TheDrifter_KeycardChance_Expeditions | 0x0082D353 | Keycard drop from Expeditions |
| P62_LCP_TheDrifter_KeycardChance_RAIDS | 0x0081FD76 | Keycard drop from Raids |

**Key Finding**: Bethesda can individually tune keycard drop rates for EVERY activity type independently. They could make keycards rain from Daily Ops while being rare from public events, or vice versa.

### Silver Bridge Phase System

| LCP Global | FormID | What It Controls |
|-----------|--------|-----------------|
| LCP_SilverBridgePhaseNumber | 0x00829276 | Controls which phase of Silver Bridge content is active |

This is a progressive content unlock system -- Bethesda can increment the phase number to reveal new content at Silver Bridge without patching.

### Milepost (MILE) LCP Controls

| LCP Global | FormID | What It Controls |
|-----------|--------|-----------------|
| MILE_LCP_CryptidHunter | 0x007B27B7 | Cryptid Hunter NPC/feature |
| MILE_LCP_MysteryCrate | 0x007B27B8 | Mystery Crate system |
| MILE_CaravanQuests_SM_Enabled | 0x008531DC | Caravan quest story manager |
| MILE_CaravanEscort_Toggle | 0x00772F30 | Caravan escort events |
| MILE_CaravanIntroQuest_Toggle | 0x00772F2F | Caravan intro quest |
| MILE_AppalachiaProps_Toggle | 0x0076B138 | Appalachia props/decorations |
| MN2_Decorations_Toggle | 0x00772F31 | Mischief Night 2 decorations |

### Ghoul Player System (GHL00)

| LCP Global | FormID | What It Controls |
|-----------|--------|-----------------|
| LCP_GHL00_Quest_Enabled | 0x0079C733 | Ghoul chargen quest enable |
| GHL00_GhoulChargenHealthThreshold | 0x00818BAF | Health threshold for ghoul creation |

### Fishing Monthly Rotation

| LCP Global | FormID | What It Controls |
|-----------|--------|-----------------|
| LCP_Fishing_Axolotl_MonthlyIndex | 0x008047AD | Which axolotl variant is catchable this month |

### Quest/Content Gating

| LCP Global | FormID | What It Controls |
|-----------|--------|-----------------|
| LCP_QDLBarbara_Lesson06 | 0x008A4D4E | Quest Data: Barbara Lesson 06 |
| LCP_RA_BigfootFightDuration | 0x008AC55F | Bigfoot fight encounter duration |
| LCP_BS01_Trust | 0x005D2BAD | BoS Questline: Trust |
| LCP_BS01_FieldTesting | 0x005D2BAE | BoS Questline: Field Testing |
| LCP_BS01_Arms | 0x005D80E5 | BoS Questline: Arms |
| LCP_BS01_MQ05_Raiders | 0x005D2B2A | BoS MQ05: Raider path |
| LCP_BS01_MQ06_Settlers | 0x005D1F86 | BoS MQ06: Settler path |
| LCP_BS02_Warfare | 0x005B682F | BoS Season 2: Warfare |
| LCP_BS01_MQ02_Invention | 0x005C8E8F | BoS MQ02: Invention |
| LCP_RetreatVillage | 0x005D2AF9 | Retreat Village content |
| LCP_BoSZ01 | 0x005D27FD | BoS Expansion zone |
| LCP_InternalPlaytestOnly | 0x006369E0 | Internal playtest content gate |
| LCP_E01_Test_VHarbison_RobotSpringBreak | 0x0063619C | Dev test: Robot Spring Break |
| BS02_E01_Metal_LCP_Global | 0x005FE4ED | BoS S2 E01: Metal event |

### Expedition Objective Randomization via LCP

LCP controls which expedition objectives can appear. Each expedition mission has 9 objectives (A01-A03, B01-B03, C01-C03), each with an LCP toggle:

**Missions with LCP objective control:**
- XPD_AC01 (Atlantic City Mission 1)
- XPD_AC02_Sensation (AC2: Sensation)
- XPD_AC03 (Atlantic City Mission 3)
- XPD_RTTP01 (Return to The Pitt Mission 1)
- XPD_Pitt01 (The Pitt Mission 1)
- XPD_Pitt02 (The Pitt Mission 2)
- XPD_TempEx01 (Temporary Expedition 01)

Setting any objective's LCP global to 0 removes it from the random pool. This means Bethesda can disable buggy objectives without patching.

---

## Layer 2: LTT (Live Tuning Toggle) -- The Drop Rate Knobs

LTT globals control reward probabilities. Each has a Toggle (1=on, 0=off) paired with a rate value (DropRate or ChanceNoneDropRate).

### Pattern: Toggle + Rate Pair

Every LTT feature uses this two-global pattern:
- `LTT_[Feature]_Toggle` -- Master on/off switch (1 or 0)
- `LTT_[Feature]_DropRate` or `LTT_[Feature]_ChanceNoneDropRate` -- The probability value

**Important**: "ChanceNone" is INVERTED -- higher values mean FEWER drops (it controls the probability of getting nothing).

### Complete LTT Toggle Map

#### Reward Activity (RA) Bonuses
| Toggle Global | Rate Global | Effect |
|--------------|-------------|--------|
| LTT_RA_Rewards_PublicEvents_Bobbleheads_Toggle | LTT_RA_Rewards_PublicEvents_Bobbleheads_DropRate | Bonus bobblehead drops from public events |
| LTT_RA_Rewards_PublicEvents_StableFlux_Toggle | LTT_RA_Rewards_PublicEvents_StableFlux_DropRate | Bonus stable flux from public events |
| LTT_RA_Rewards_Activities_UMineItMap_Toggle | LTT_RA_Rewards_Activities_UMineItMap_DropRate | U-Mine-It map drops from activities |
| LTT_RA_Rewards_Activities_DoubleLegendaryItem_Toggle | LTT_RA_Rewards_Activities_DoubleLegendaryItem_DropRate | DOUBLE legendary item drops |

#### U-Mine-It Bonus System (6 toggles!)
| Toggle Global | Rate Global | Effect |
|--------------|-------------|--------|
| LTT_UMineItLegendary_Toggle | LTT_UMineItLegendary_ChanceNoneDropRate | Legendary drops from U-Mine-It |
| LTT_UMineItBobbleHead_Toggle | LTT_UMineItBobbleHead_ChanceNoneDropRate | Bobblehead drops from U-Mine-It |
| LTT_UMineItFlux_Toggle | LTT_UMineItFlux_ChanceNoneDropRate | Flux drops from U-Mine-It |
| LTT_UMineItTreasuryNote_Toggle | LTT_UMineItTreasuryNote_ChanceNoneDropRate | Treasury note drops from U-Mine-It |
| -- | LTT_UMineItLegendary_Amount | Legendary item QUANTITY per drop |

#### Seasonal Event Tuning
| Toggle Global | Rate Global | Effect |
|--------------|-------------|--------|
| LTT_DoubleFestiveGift_Toggle | LTT_DoubleFestiveGift_DropRate | Double holiday gift drops |
| LTT_WaterLoggedGifts_Toggle | LTT_Odds_WaterLoggedGifts | Waterlogged gift drops |
| LTT_IncreasedFasnachtGlowingMaskDrop_Toggle | LTT_IncreasedFasnachtGlowingMaskDrop_ChanceNoneDropRate | Rare Fasnacht glowing mask boost |

#### Combat Bonus Drops
| Toggle Global | Rate Global | Effect |
|--------------|-------------|--------|
| LTT_HeadHunt4StarDrops_Toggle | LTT_HeadHunt4StarDrops_ChanceNoneDropRate | 4-star drops from head hunts |
| LTT_GruntHuntBonusStarDrops_Toggle | LTT_GruntHuntBonusStarDrops_ChanceNoneDropRate | Bonus star level from grunt hunts |
| LTT_MothmanMutatedPartyPacks_Toggle | LTT_MothmanMutatedPartyPacks_ChanceNoneDropRate | Mothman mutated party pack drops |

---

## Layer 3: Spotlight System -- Community Event Multipliers

Spotlight globals control the "community week" events that double or triple currency/XP:

| Spotlight Global | FormID | Effect |
|-----------------|--------|--------|
| Spotlight_DoubleXP | 0x003FBAAE | Double XP weekend |
| Spotlight_TripleXP | 0x005A4FA0 | Triple XP weekend |
| Spotlight_DoubleXPSurvival | 0x0040419A | Double XP (Survival mode) |
| Spotlight_DoubleVendorCurrency_LegendaryScrip | 0x005F0E61 | Double Legendary Scrip daily limit |
| Spotlight_TripleVendorCurrency_LegendaryScrip | 0x0063420D | Triple Legendary Scrip |
| Spotlight_DoubleVendorCurrency_GoldBullion | 0x005F0E60 | Double Gold Bullion daily limit |
| Spotlight_DoubleVendorCurrency_Caps | 0x005F0C23 | Double Caps vendor limit |

**Historical/Legacy Spotlight events still in data:**
- Spotlight_ReclamationDay, Spotlight_Holiday2018, Spotlight_NewYear2019
- Spotlight_Fasnacht, Spotlight_HeartToHeart, Spotlight_SpringCleaning
- Spotlight_WildAppalachia, Spotlight_Sheepsquatch, Spotlight_EverUpwards
- Spotlight_LegendaryVendor, Spotlight_Vault94Opening
- Spotlight_BobbleHeadBonanza, Spotlight_ShareTheLove
- Spotlight_Thanksgiving, Spotlight_WinterWonderland
- Spotlight_LetsCamp, Spotlight_BacktoNature, Spotlight_Nuked
- Spotlight_BrewHaha, Spotlight_ChildsPlay, Spotlight_TerrorInTheNight
- Spotlight_HeavyMetal, Spotlight_ImprovedCargoCrates
- Spotlight_LegendOfTheMothman, Spotlight_Unstoppable
- Spotlight_ShearTerror, Spotlight_RandR
- Spotlight_TBD-9, Spotlight_TBD-17 (PLACEHOLDER slots never used)

---

## DailyOps Rotation System -- The Index Architecture

Daily Ops uses a pure index-based system where the "Live Content Scheduler" sets numerical indices into FormLists:

| Global | FormID | What It Indexes |
|--------|--------|----------------|
| DailyOps_Mutation_Index | 0x005B2E9A | Which mutation spell is active today |
| DailyOps_Mutation_Mode_Index | 0x0060E42E | Single vs. double mutation mode (1=double) |
| DailyOps_Mutation_Chance | 0x005B2E9B | Probability of mutation applying |
| DailyOps_Encounter_Index | 0x005AE09C | Which enemy faction spawns |
| DailyOps_Location_Index | 0x005C65E3 | Which map location is used |
| DailyOps_GameMode_Index | 0x005C65E4 | Which game mode (Uplink, Decryption, etc.) |
| DailyOps_DoubleMutation_Index | 0x0060A2BB | Which double mutation combo |
| DailyOps_HighElder_Mode_Index | 0x0060A2BC | High Elder (hard mode) toggle |
| DailyOps_Encounter_FormList_Selection_Index | 0x0061DA37 | Which encounter FormList to pull from |

**How Mutation Rotation Works** (from `dailymutation.psc`):
1. The Live Content Scheduler sets `DailyOps_Mutation_Index` to a number
2. The script uses this index into `DailyOps_Mutation_Master_FormList` to get a mutation spell
3. The same index into `DailyOps_Mutation_NameMod_FormList` gets the display name mod
4. If `DailyOps_Mutation_Mode_Index == 1`, it uses the double mutation lists instead
5. Every spawned enemy gets `ApplyDailyMutation()` called, applying the spell

The "rotation" is entirely server-driven. There is no client-side randomization -- the server tells the client exactly which mutation, encounter, and location to use.

### Debug/Test Indices

| Global | FormID | Purpose |
|--------|--------|---------|
| DailyOps_DoubleMutation_TestFirst_Index | 0x0060A2BD | QA: Force first double mutation |
| DailyOps_DoubleMutation_TestSecond_Index | 0x0060A2BE | QA: Force second double mutation |

---

## Mutated Public Events -- Per-Event Mutation Control

Each public event that supports mutations has TWO LCP globals:
- `MutatedEvents_LCP_[EventCode]_MutationEnabled` -- Can this event be mutated?
- `MutatedEvents_LCP_[EventCode]_DoubleMutationEnabled` -- Can it have double mutations?

### Complete Mutated Events Map

| Event Code | Event Name | Mutation LCP | Double Mutation LCP |
|-----------|------------|-------------|-------------------|
| E01B_Herd | Free Range | MutationEnabled | DoubleMutationEnabled |
| E01C_Tales_Dark | A Colossal Problem / Tales from the Hills | MutationEnabled | DoubleMutationEnabled |
| E05_Radiation | Radiation Rumble | MutationEnabled | DoubleMutationEnabled |
| E08A_Moonshine | Moonshine Jamboree | MutationEnabled | DoubleMutationEnabled |
| E08B_EvictionNotice | Eviction Notice | MutationEnabled | DoubleMutationEnabled |
| FF06_Feed | Feed the People | MutationEnabled | DoubleMutationEnabled |
| FFZ10_Light | Lighthouse (Path to Enlightenment) | MutationEnabled | DoubleMutationEnabled |
| FFZ17_TeaTime | Tea Time | MutationEnabled | DoubleMutationEnabled |
| MTR08_Lode | Lode Baring | MutationEnabled | DoubleMutationEnabled |
| MTNS04_Night | One Violent Night | MutationEnabled | DoubleMutationEnabled |
| MTNS06_Uranium | Uranium Fever | MutationEnabled | DoubleMutationEnabled |
| MTNM03_Meditation | Meditation (Guided Meditation) | MutationEnabled | DoubleMutationEnabled |
| MTNM04_Guest | Distinguished Guests | MutationEnabled | DoubleMutationEnabled |
| SFS08_Heart | Heart of the Swamp | MutationEnabled | DoubleMutationEnabled |
| SFS09_Habitat | It's a Trap (Project Paradise) | MutationEnabled | DoubleMutationEnabled |
| TW008 | Swarm of Suitors | MutationEnabled | DoubleMutationEnabled |
| TWZ05 | Line in the Sand | MutationEnabled | DoubleMutationEnabled |
| BS02_E01_Metal | Brotherhood: Metal event | MutationEnabled | DoubleMutationEnabled |
| BoSr01 | Brotherhood patrol event | MutationEnabled | DoubleMutationEnabled |

From `eventmutationscript.psc`: The mutation system reuses the DailyOps mutation spell/name FormLists. Each event can also have a `BlockedListOfMutationsForThisEvent` -- certain mutations excluded per-event (e.g., a mutation that doesn't work in a specific location).

### Mutated Events Playlist Controls

| Global | FormID | What It Controls |
|--------|--------|-----------------|
| MutatedEvents_LCP_FeaturedFavoritesPlaylist | 0x0068D9EE | Which events are in the "Featured Favorites" rotation |
| MutatedEvents_LCP_FeaturedFavoritesPlaylist_V2 | 0x007A888D | V2 of the featured playlist |
| MutatedEvents_LCP_FeaturedFavoritesPlaylist_DoubleMutation | 0x006BEE42 | Double mutation featured playlist |
| MutatedEvents_LCP_LimitedTimeFeature_Playlist | 0x007A888C | Limited-time featured event playlist |
| MutatedEvents_LCP_Fallout1stRewardsThreshold | 0x00698822 | Fallout 1st bonus reward threshold for mutated events |

---

## Event Playlist System -- How Events Rotate

The game has multiple event playlists that can be switched:

| Global | FormID | Purpose |
|--------|--------|---------|
| DefaultPublicEventPlaylistEnable | 0x00621A97 | Standard event rotation on/off |
| FeaturedPublicEventPlaylistEnable | 0x006515D0 | Featured/curated playlist on/off |
| InternalPlaylist_Main_20min_Enable | 0x00653209 | Internal: 20-min rotation |
| InternalPlaylist_Main_Hourly_Enable | 0x0065320A | Internal: Hourly rotation |
| InternalPlaylist_DevMain_20min_Enable | 0x00653207 | DEV: 20-min fast rotation |
| InternalPlaylist_DevMain_Hourly_Enable | 0x00653208 | DEV: Hourly fast rotation |
| InternalPlaylist_DevCyan_20min_Enable | 0x006E23AB | DEV: Cyan team 20-min rotation |
| PTSPublicEventPlaylist_20min_Enable | 0x0065320B | PTS: 20-min test rotation |
| PTSPublicEventPlaylist_Hourly_Enable | 0x0065320C | PTS: Hourly test rotation |

**Key Finding**: The dev team has separate playlist controls for different internal teams (DevMain vs DevCyan). These are never toggled on live servers but remain in the data.

---

## Seasonal Event Spawn & Reward Architecture

### Fasnacht

| Global | FormID | Purpose |
|--------|--------|---------|
| E01F_FasnachtMaster_CanStart | 0x0046F50D | Master event start permission |
| E01F_FasnachtQuestTimer | 0x003FBF5A | Event timer |
| E01F_FasnachtMarcherTimer | 0x0047B7D1 | Parade marcher timing |
| E01F_FasnachtStartTimer | 0x00498881 | Event start delay |
| E01F_Fasnacht_SurvivorCount | 0x004036F7 | Robot survivor count |
| E01F_Fasnacht_ProtectronSpeedMult | 0x00786E07 | Protectron speed (tunable!) |
| E01F_Fasnacht_DisablePatch52Updates | 0x00786E08 | Revert to pre-patch 52 behavior |
| E01F_Fasnacht_EnableBossDropsMasks | 0x008A7A44 | Boss mask drops toggle |
| E01F_Fasnacht_DisableBossMegasloth | 0x0078A04D | Disable Megasloth boss |
| E01F_Fasnacht_DisableBossBlueDevil | 0x0078757F | Disable Blue Devil boss |
| E01F_Fasnacht_DisableBossSheepsquatch | 0x00787580 | Disable Sheepsquatch boss |
| E01F_Fasnacht_DisableBossGraftonMonster | 0x00787581 | Disable Grafton Monster boss |
| E01F_Fasnacht_DisableBossSMBehemoth | 0x00787582 | Disable Super Mutant Behemoth boss |
| E01F_Fasnacht_DisableBossOgua | 0x0078757E | Disable Ogua boss |

**Key Finding**: Bethesda can disable individual Fasnacht bosses server-side. If a boss is causing crashes or exploits, they can remove just that one.

### Fasnacht Reward Economy
| Global | FormID | Purpose |
|--------|--------|---------|
| Fasnacht_Reward_High_Rare_ECON | 0x005A6486 | High-tier rare reward weight |
| Fasnacht_Reward_High_Uncommon_ECON | 0x005A6487 | High-tier uncommon weight |
| Fasnacht_Reward_LOW_Common_ECON | 0x005A6488 | Low-tier common weight |
| Fasnacht_Reward_Medium_Uncommon_ECON | 0x005A648A | Mid-tier uncommon weight |
| Fasnacht_Masks_Rare_ECON | 0x00402D73 | Rare mask drop weight |
| Fasnacht_Masks_Uncommon_ECON | 0x00402D74 | Uncommon mask drop weight |

### Meat Week
| Global | FormID | Purpose |
|--------|--------|---------|
| E02A_Meat_Enabled | 0x005C4F12 | Master enable |
| E02A_Meat_SpawnChance | 0x005C4F13 | Prime meat creature spawn rate |
| E02A_Meatweek_LLS_RareRewards_ChanceNone_Best | 0x005CB50C | Best rare reward probability |
| E02A_Meatweek_LLS_RareRewards_ChanceNone_Good | 0x005CB50B | Good rare reward probability |
| E02A_Meatweek_LLS_RareRewards_ChanceNone_Bad | 0x005CB50D | Bad tier probability |
| E02A_Meatweek_LLS_FireworksReward_ChanceNone | 0x005CB50E | Fireworks reward probability |
| E02A_Meat_BBQ_PrepTime | 0x00553E07 | BBQ preparation timer |
| E02A_Meat_BBQ_QuestTimer | 0x0054B3FC | BBQ event timer |
| E02A_Meat_Hunt_QuestTimer | 0x0054E318 | Primal Cuts timer |
| E02A_Meat_Hunt_DrumTimer | 0x005532AD | Drum beat interval |
| E02A_Meat_Hunt_NextWaveTimer | 0x005532AA | Wave spawn interval |

### Spooky/Halloween Scorched
| Global | FormID | Purpose |
|--------|--------|---------|
| Festive_Halloween_Enabled | 0x0059CB0A | Halloween master switch |
| Spooky_EventEnabled | 0x0059CB09 | Spooky event system |
| Spooky_ScorchedSpawnChance | 0x0062038A | Spooky Scorched spawn rate |
| Spooky_BowlCooldownInMinutes | 0x00623BD0 | Candy bowl cooldown |
| Spooky_CandyKeyword | 0x00621C0B | Candy item keyword |

### Holiday/Festive Scorched
| Global | FormID | Purpose |
|--------|--------|---------|
| Festive_Holiday_Enabled | 0x0059CB08 | Holiday master switch |
| Festive_ScorchedSpawnChance | 0x0059B7D4 | Festive Scorched spawn rate |
| Festive_GiftCrafting_Enabled | 0x0059EFC9 | Gift crafting at tinker bench |
| FestiveScorchedChanceForTwoStarLegendary | 0x0059CB04 | 2-star legendary chance |
| FestiveScorchedChanceForThreeStarLegendary | 0x0059CB05 | 3-star legendary chance |
| LTT_DoubleFestiveGift_Toggle | 0x00864CC4 | Double gift drop event |

---

## Reward Activity (RA) System

RA_ globals control the game's general reward system:

| Global | FormID | Purpose |
|--------|--------|---------|
| RA_Rewards_Activities_Caps | 0x0086A8B1 | Base cap reward from activities |
| RA_Rewards_Activities_LegendaryItem_DropRate | 0x0086A8B2 | Legendary drop rate from activities |
| RA_Rewards_PublicEvents_Caps | 0x0086A8B7 | Cap reward from public events |
| RA_ChemNeedsAmount | 0x0086A8B4 | Chem reward quantity |
| RA_PartyCrasherSpawnChance_Default | 0x0086AEEB | Party Crasher boss spawn rate |
| RA_PartyCrasherSpawnChance_Bigfoot | 0x00869A34 | Bigfoot-specific party crasher rate |
| RA_RareTitleDropChance | 0x0085AD24 | Rare player title drop chance |
| RA_CapsLuckyStrikeRepeteableGlobal01 | 0x0086AEEA | Lucky Strike caps reward tier 1 |
| RA_CapsLuckyStrikeRepeteableGlobal02 | 0x008AC559 | Lucky Strike caps reward tier 2 |
| RA_CapsLuckyStrikeRepeteableGlobal03 | 0x008AC55A | Lucky Strike caps reward tier 3 |
| RA_Rewards_Activities_UniqueWeapon_DropRate_Cnone | 0x008B0D7A | Unique weapon drop probability |

---

## Mischief Night 2.0 -- Deep Control Architecture

From `mn2_questscript.psc`, MN2 has a "LiveToggles" group showing per-feature LCP control:

```
Group LiveToggles
  GlobalVariable Property LCP_Explosions  -- Toggle explodable cars/barrels
  Bool Property bLCPExplosionsOn          -- Runtime state
  Float Property ExplosionsCompensateMultiplier  -- Progress compensation when disabled
  GlobalVariable Property LCP_Fanfare    -- Toggle success fanfare effects
  Bool Property bLCPFanfareOn            -- Runtime state
  GlobalVariable Property LCP_Bonus      -- Toggle costume bonus
  Bool Property bLCPBonusOn              -- Runtime state
EndGroup
```

This reveals that if explosions cause performance issues, Bethesda can disable just the explosion feature while compensating progress with a multiplier -- players wouldn't notice the change.

The progress bar system (`collalias.psc`) has its own LiveToggle integration:
```
Group Optional_LiveToggle
  GlobalVariable Property LCP_Bonus      -- Bonus progress toggle
  GlobalVariable Property LCP_Fanfare    -- Fanfare effects toggle
  Float Property LiveToggleBonus          -- Bonus amount when toggled on
  GlobalVariable[] Property LiveToggles   -- Array of arbitrary LCP checks
EndGroup
```

---

## How the System Works End-to-End

### Data Flow

```
Bethesda Server Infrastructure
        |
        v
[Content Scheduler Service]
        |
        | Pushes new GlobalVariable values
        v
[FO76 Game Server]
        |
        | Server-authoritative globals
        v
[Client ESM Runtime]
        |
        | Scripts call GetValue() on globals
        v
[Game Behavior Changes]
    - Events appear/disappear
    - Drop rates shift
    - Mutations rotate
    - Quests unlock/lock
    - Boss spawns toggle
    - Reward multipliers change
```

### What Gets Controlled

1. **Content Availability** (LCP layer):
   - Which events are running (seasonal, public, special)
   - Which quest lines are accessible
   - Which features are enabled (crafting, fishing rotations, boss encounters)
   - Which expedition objectives are in the random pool
   - Which content phases are active (Silver Bridge progression)

2. **Reward Economy** (LTT layer):
   - Drop rates for legendaries, bobbleheads, flux, treasury notes
   - Bonus item quantities
   - Rare mask/plan drop probabilities
   - 4-star legendary drop rates
   - Event-specific reward tuning

3. **Community Events** (Spotlight layer):
   - Double/Triple XP weekends
   - Double Scrip/Gold/Caps limits
   - Historical event activations

4. **Daily Rotation** (Index system):
   - Daily Ops mutation, encounter, location, mode
   - Event playlists (which public events rotate in)
   - Per-event mutation eligibility

### The "ChanceNone" Pattern

Throughout the system, Bethesda uses an inverted probability model:
- A `ChanceNone` value of 0 = 100% drop rate (no chance of nothing)
- A `ChanceNone` value of 50 = 50% drop rate
- A `ChanceNone` value of 90 = 10% drop rate
- A `ChanceNone` value of 100 = 0% drop rate (guaranteed nothing)

This is the Creation Engine's standard leveled list probability model.

---

## Indicators of Upcoming/Unreleased Content

### Active Development Signals (high FormIDs = recently added)

1. **LCP_RA_BigfootFightDuration (0x008AC55F)** -- Very high FormID. Bigfoot encounter is getting dedicated fight-length tuning, suggesting it's being polished for a future event variant.

2. **RA_Rewards_Activities_UniqueWeapon_DropRate_Cnone (0x008B0D7A)** -- Highest FormID of any RA global. A new "unique weapon" drop system from activities is being added.

3. **SCORE_S24 items** -- Season 24 scoreboard items appearing (Mountain Retreat prefab, Survival Cache, Strange Curio Cabinet). Season 24 content is loaded.

4. **LTT_WaterLoggedGifts_Toggle (0x00864521)** -- "Waterlogged Gifts" is a completely new gift type not yet seen in any seasonal event.

5. **LTT_MothmanMutatedPartyPacks (0x0085712F)** -- "Mutated Party Packs" from Mothman events suggest a new reward type.

6. **LCP_QDLBarbara_Lesson06 (0x008A4D4E)** -- "QDL Barbara Lesson 06" appears to be part of a tutorial/quest system with a character named Barbara. Very high FormID suggests recent development.

7. **SpawnChance_Cnone_PlasmaCasterModPlans (0x008B1D61)** -- Highest FormID in the entire globals list. Plasma Caster mod plans are being added as world drops.

8. **SpawnChance_Cnone_RarePlayerTitle (0x008AA954)** -- Rare player titles as world drops, very recent addition.

9. **zzzLCP_BURN_E01_Gear and zzzLCP_BURN_E02_Sinkhole** -- Two Backwoods events ("Gear" and "Sinkhole") were planned but cut. The zzz prefix means deprecated but data remains.

10. **Spotlight_TBD-9 and Spotlight_TBD-17** -- Two placeholder Spotlight event slots that were never filled, suggesting planned events that never materialized.

---

## Community Knowledge Validation

**What the community knows:**
- Individual LTT toggles have been found by dataminers examining ESM updates
- Double XP/Scrip weekends are visibly communicated by Bethesda
- DailyOps rotations are tracked by community sites
- Seasonal event enable/disable dates are publicly announced

**What this analysis reveals that the community does NOT know:**
1. The three-layer architecture (LCP/LTT/Spotlight) as a unified system
2. The per-event mutation enable/disable granularity (38 individual toggles)
3. The expedition objective LCP control system (can disable objectives without patches)
4. The Fasnacht per-boss disable capability
5. The Drifter keycard per-activity-type drop rate system (7 separate knobs)
6. The Silver Bridge phase progression system
7. The dev/PTS playlist infrastructure (DevMain vs DevCyan teams)
8. The Mischief Night 2 per-feature disable with progress compensation
9. The full extent of Backwoods (BURN) content gating
10. Two cut Backwoods events (Gear, Sinkhole)
11. The "Barbara Lesson" quest system
12. The Waterlogged Gifts system
13. That the "Content Scheduler" is the official internal name for this infrastructure

---

## Implications for Players

1. **Drop rates are NEVER static** -- Any community-tested drop rate is only valid at the moment of testing. Bethesda can silently adjust any ChanceNone value.

2. **"Stealth nerfs" are trivially easy** -- Bethesda can reduce legendary drop rates, rare plan rates, or event rewards without any patch or announcement.

3. **"Stealth buffs" happen too** -- Bonus events like increased Fasnacht mask rates or U-Mine-It legendary boosts can be quietly enabled.

4. **Event content is granular** -- Bethesda doesn't just turn events "on" or "off." They control individual features within events (which bosses spawn, which rewards drop, whether explosions are enabled).

5. **The DailyOps rotation is NOT random** -- It's a server-pushed index. Bethesda explicitly chooses each day's combination.

6. **Seasonal events have tunable spawn rates** -- The density of Spooky/Festive Scorched and Treasure Hunter Mole Miners is a server-side dial.

7. **Bigfoot has special treatment** -- It has its own spawn chance separate from other party crashers AND a dedicated fight duration global, suggesting it's being developed as a more significant encounter.

---

## Technical Notes

- All globals are GLOB records in the ESM (SeventySix.esm)
- FormIDs above ~0x0085xxxx are from recent updates (Backwoods era, ~March 2026)
- The zzz prefix is Bethesda's convention for deprecated/cut content
- The CUT_ and DEL_ prefixes also indicate removed content
- "ECON" suffix globals are economy-balancing values used by leveled lists
- The P62 prefix appears to be a patch/update number designation
