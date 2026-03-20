# FO76 Finding 026: Live Tuning System — Server-Side Drop Rate Controls

## Status: CONFIRMED NOVEL — Complete map of Bethesda's remote tuning infrastructure
## Source: GLOB_records.txt from ESM dump
## Validation: LTT_ prefix system not documented by community dataminers at this granularity

## What This Is
Bethesda has a "Live Tuning Toggle" (LTT_) system that lets them remotely adjust drop rates, spawn chances, and reward structures WITHOUT patching the game. Every LTT_ global has a Toggle (on/off) and often a DropRate (probability) or ChanceNone (inverse probability).

## Active Live Tuning Toggles

### Double/Bonus Item Events
| Toggle | What It Does |
|--------|-------------|
| LTT_RA_Rewards_Activities_DoubleLegendaryItem_Toggle | Double legendary drops from activities |
| LTT_DoubleFestiveGift_Toggle | Double festive gift drops |
| LTT_WaterLoggedGifts_Toggle | Enable waterlogged gifts |

### Drop Rate Adjustments
| Toggle | What It Controls |
|--------|-----------------|
| LTT_RA_Rewards_PublicEvents_Bobbleheads_Toggle + DropRate | Bobblehead drops from public events |
| LTT_RA_Rewards_PublicEvents_StableFlux_Toggle + DropRate | Stable flux drops from events |
| LTT_RA_Rewards_Activities_UMineItMap_Toggle + DropRate | U-Mine-It map drops |
| LTT_UMineItLegendary_Toggle + ChanceNoneDropRate | U-Mine-It legendary drops |
| LTT_UMineItBobbleHead_Toggle + ChanceNoneDropRate | U-Mine-It bobblehead drops |
| LTT_UMineItFlux_Toggle + ChanceNoneDropRate | U-Mine-It flux drops |
| LTT_UMineItTreasuryNote_Toggle + ChanceNoneDropRate | U-Mine-It treasury note drops |

### Event-Specific
| Toggle | What It Controls |
|--------|-----------------|
| LTT_IncreasedFasnachtGlowingMaskDrop_Toggle | Fasnacht rare mask increased rate |
| LTT_MothmanMutatedPartyPacks_Toggle | Mothman mutated party packs |
| LTT_HeadHunt4StarDrops_Toggle | 4-star drops from head hunts |
| LTT_GruntHuntBonusStarDrops_Toggle | Bonus star drops from grunt hunts |
| E01F_Fasnacht_EnableBossDropsMasks | Fasnacht boss mask drops |

### Regional/Feature
| Toggle | What It Controls |
|--------|-----------------|
| Burn_BountyHunt_HeadHunt_LCPToggle | Bounty head hunt system |
| Burn_BountyHunt_GruntHunt_LCPToggle | Bounty grunt hunt system |
| Burn_DustDevil_Push_Enable | Dust devil push mechanic |
| LCP_Burn_DustDevil_Enable | Dust devil spawns |
| MILE_CaravanQuests_SM_Enabled | Milepost caravan quests |

## Spawn Chance Globals
| Global | What It Controls |
|--------|-----------------|
| RA_PartyCrasherSpawnChance_Default | General boss crash rate at events |
| RA_PartyCrasherSpawnChance_Bigfoot | Bigfoot-specific crash rate |
| SpawnChance_RadhogAlpha | Alpha Radhog variant |
| SpawnChance_Cnone_PlasmaCasterModPlans | Plasma caster mod plan drops |
| SpawnChance_Cnone_GatlingPlasmaModPlans | Gatling plasma mod plan drops |
| SpawnChance_Cnone_RarePlayerTitle | Rare player title drops |
| SpawnChance_Cnone_ActivityCampTitle | CAMP title drops from activities |
| LCP_E07A_Mothman_SpecialEncounter_SpawnChance | Special Mothman encounter |
| Spooky_ScorchedSpawnChance | Spooky Scorched (Halloween) |
| Festive_ScorchedSpawnChance | Festive Scorched (Christmas) |
| TreasureHunt_SpawnChance | Treasure hunter mole miner |
| ScorchedStatueSpawnChance | Scorched statue spawn |

## Why This Matters for Players
1. **Drop rates change without patches** — what worked last week might not work this week
2. **Event bonuses stack** — multiple LTT toggles can be on simultaneously
3. **Bigfoot has a SEPARATE spawn rate** from other party crashers
4. **The "ChanceNone" pattern** means higher values = FEWER drops (it's inverted)
5. **Community-tested drop rates are snapshots** — they change whenever Bethesda flips a toggle
6. **Seasonal events use spawn chance globals** — the actual Halloween/Christmas rates are tunables

## Build Planner Implications
Drop rate analysis should always note that values are server-tunable and may not reflect current live rates. Any "farming guide" based on tested rates could be invalid if Bethesda has adjusted the LTT globals since testing.
