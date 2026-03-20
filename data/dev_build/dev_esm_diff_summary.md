# Fallout 76 ESM Diff: Dev Build vs Retail

- **Dev build ESM**: Nov 2023, 753MB, 245,657 named records
- **Retail ESM**: Mar 2026, 879MB, 319,883 named records
- **Diff date**: 2026-03-20

## Overview

| Metric | Count |
|--------|-------|
| Records only in dev (cut/removed) | 4,972 |
| Records only in retail (new/added) | 79,198 |
| Records in both | 240,685 |
| Relocated records (same name, different form ID) | 33 |

The retail ESM grew by ~126MB and gained 74,226 net new named records over ~28 months.

---

## Key Findings: Cut/Removed Content (Dev-Only)

### Cut Creature: BossChicken (already known)
- `RACE BossChickenRace` (0x00636DDA)
- `NPC_ LvlBossChicken` (0x00636DD9)
- `ARMA AABossChicken`, `ARMO SkinBossChicken`

### Cut Quest: TWZ09 (Aerosolizer Quest)
A complete cut quest with its own crafting, combat mechanics, and mirelurk horde AI:
- `QUST TWZ09` (0x00088A9A) - the quest itself
- `PERK TWZ09AerosilzerKick` - custom combat perk
- `MGEF TWZ09KickEffect` / `SPEL TWZ09KickPerk` - associated magic effects
- `COBJ TWZ09AerosolizerRecipe` - craftable recipe
- `KYWD TWZ09AerosolizerKeyword`
- `LVLI TWZ09_Chlorine`, `LVLI TWZ09_Fertilizer` - crafting ingredients
- `MESG TWZ09_NoFertilizerMsg` - error message for missing ingredients
- Related AI: `TWZ05_MirelurkHordeAccompany01/02/03`, `TWZ05_MirelurkWait` - mirelurk escort packages

### Cut Weapons: Named Uniques
Five named unique weapon variants that were cut:
- **PiratePunch** - `Blackpowder_Pistol_Blunderbuss_PiratePunch` (0x00647820)
- **CrowdControl** - `CombatShotgun_CrowdControl` (0x006477EC)
- **ToneDeath** - `DeathTambo_ToneDeath` (0x006477EF)
- **TheDebilitator** - `SuperSledge_TheDebilitator` (0x006477ED)
- **DoctorsOrders** - `HuntingRifle_DoctorsOrders` (0x006477EE)

All share consecutive form IDs (0x006477EC-EF), suggesting they were designed as a set.

### Cut Weapons: Brotherhood of Steel Arsenal
- `BoSPistol` (0x005E6FC0) - unique BoS sidearm with full damage curves
- `BOSRocketLauncher_NONPLAYABLE` (0x005EFA6A) - NPC-only BoS rocket launcher
- `CT_Weapon_BoSPistol_BaseDMG` / `CT_Weapon_BoSPistol_ModDMG` - damage tuning curves

### Cut Weapons: Other Notable
- `QuadLauncher` (0x005DD5B2) - 4-barrel missile launcher
- `crossbow` (0x00055463) - standalone crossbow
- `Fire_Axe` (0x0012B793) - fire axe melee weapon
- `E09A_Launcher_ThrowBloatflyWeapon` (0x0063D326) - bloatfly throwing launcher
- `FestiveScorched_BearArm` (0x005A205C) - seasonal Bear Arm variant

### Cut Perks: Rank 4/5 Cards (already known - 153 total)
Higher-rank versions of existing perk cards. Notable:
- `CUT_AdamantiumSkeleton04/05`, `CUT_BulletShield04`, `CUT_Ricochet04`, etc.
- Also full rank 2/3 sets that were consolidated into single-rank perks
- `AttackDog01/02/03` - companion attack perks (no pets in FO76)
- `BloodHealerPerk`, `CheerLeaderPerk` - team-oriented cut perks
- `Bruisers_OnBashPerk`, `HeavyHitter_OnHitPerk` - melee mechanic perks
- `CriticalHealers_ApplyOnHit`, `Scavengers_LootPerk` - utility perks

### Cut Event: E09 NukaWorld on Tour (Partial)
67 records cut from the dev build, while 1,141 E09 records appear in retail.
Cut records were early prototypes:
- `E09A_Launcher_Weapon`, `E09A_Launcher_Egg` - egg/bloatfly throwing mechanics
- `E09B_Wheel_*` - spin-the-wheel wave defense mechanics
- NukaWorld circus tent structures, photo boards, cutout boards
- Boss wave and regular wave scenes

### Cut Cells/Locations
- `Vault63Entrance` (0x00044A50) - early Vault 63 entrance (later rebuilt for Skyline Valley)
- `RaiderCave01/03` - raider cave interiors
- `zCUTSpruceKnobMissileSilo01OLD` - old version of Spruce Knob missile silo
- `zCUTProtoExpo04` - expedition prototype cell
- `76CellTemplateCopy01JOE` / `76GeorgePWindmilllTest` - developer test cells (named after devs)

### Cut NPCs
- `ATX_Collectron_FETCH_Rust` - cut Collectron variant
- `EncMirelurkSpawnHatchlingRaiderFaction` - raider-faction mirelurk hatchlings
- `Loot_CorpseFanatic01_XPD` - Pitt fanatic corpse loot
- `LvlSupermutantBoss_DailyOps` / `LvlSupermutantFloater*_DailyOps` - cut Daily Ops variants
- `LvlZetanAlienRanged_DailyOps` - Zetan aliens in Daily Ops
- `SFS08_Heart_LvlGrafton` / `SFS08_Heart_LvlMirelurkQueen` - seasonal boss variants

### Cut Power Armor: Four Horsemen Set (364 records)
Extensive cut PA paint set with four complete variants:
- **WarRider** - full armor set (helmet, arms, legs, torso) + headlamp mods
- **BlackRider** - headlamp mod variants
- **PaleRider** - headlamp mod variants
- **PlagueRider** - headlamp + detect life mods
All had ZZZ_ prefixed crafting recipes (disabled)

### Cut Vault Raids Music
- `MUS76CombatBossVaultRaidsM01/02/03` - 3 boss combat tracks
- `MUSzCombatHighVaultRaids` - high-intensity combat music

### Cut ArcadeManagerQuest (already known)
- `QUST ArcadeManagerQuest` (0x0063F8D6)
- `MESG ArcadeGameBusyMSG`, `MESG ArcadeGameFullMSG`

### Cut Floater Dialogue Quests
- `CreatureDialogueFloaterFlamer` (0x0056451C)
- `CreatureDialogueFloaterFreezer` (0x0056451D)
- `CreatureDialogueFloaterGnasher` (0x0056451B)
These Floater-specific dialogue quests were cut (Floaters still exist but use generic dialogue).

### Other Notable Cut Content
- `Armor_EnclaveScoutUniform_Torso_Set_V94_Solar02` - Vault 94 Enclave scout variant
- `IsCompanionKeyword_DO` - companion keyword default object
- `ExpeditionUltractiveBatteryFuel_DO` - cut expedition crafting component
- `SQ_CustomItemQuest` - player custom item quest system
- `RE_SceneBB02` - cut random encounter scene
- `FormulaQ` (SFS09) - mysterious consumable/formula
- Valentine's Day items: `P01E_Heart_*` - bouquet weapon, perfume grenade, nougat candies, heart-shaped box
- Mountain explore music palettes (10 palettes, ~130 tracks) - entire ambient music sets removed

---

## Key Findings: New Content (Retail-Only, Added Nov 2023 - Mar 2026)

### The Backwoods Update (~6,083 records, prefix: BURN_)
Massive content drop including:
- 348 new NPCs, 67 quests, 155 scenes
- Bounty hunting system: `Burn_BountyHunt_*`
- New settlements with settlers and raiders: `BURN_DialogueGeneric_HTSettlers`, `BURN_DialogueGeneric_RustRaiders`
- Vendor NPCs: `BURN_HWTVendors_Dialogue`
- Unique NPCs: Billie, Loan Shark, Athens Protectron, Cornhenge Cornbot
- 900 new layer records (world building)

### Skyline Valley (~5,431 records, prefix: Storm_)
- `StormBossRace` - Skyline Valley region boss creature
- 668 new static objects, 243 NPCs, 71 quests
- Storm weather system with electric arena hazards
- `ScorchtongueBodyRace/HeadRace/TailRace` - multi-part Scorchtongue creature

### Atlantic City Expeditions (~3,443 records, prefix: AC_/XPD_AC)
- Main quest line: `AC_MQ01` through `AC_MQ04` (Opportunity, Stage, HonorBound, Sins)
- Russo family NPCs: Abbie, Antonio, Evelyn, Vin
- Side quests: Hell's Eagles, Custodial, Reopening, Regent
- `XPD_JerseyDevilRace`, `XPD_LesserDevilRace` - Jersey Devil creatures
- `XPD_OvergrownElderRace/PollinatorRace/ThornRace` - Overgrown plant creatures

### Player Ghoul System (~1,270 records)
- `GHL_PlayerGhoulRace` - playable ghoul race
- Extensive supporting records across multiple categories

### New Creatures (34 non-dev/non-deleted)
- **BigfootRace** - Bigfoot creature
- **BlueDevilRace** - Blue Devil creature
- **DustDevilRace** - environmental hazard creature
- **OguaRace** - Ogua cryptid
- **LostRace/LostHealerRace/LostFeralSuiciderRace** - "Lost" creature family
- **RadHogRace/RadPheasantRace/RadTurkeyRace** - new irradiated animals
- **FishermanRace** - human-type NPC race
- **SuperMutantRustKingRace** - Super Mutant boss variant
- **GuardianBotRace** - robot creature
- **P62_TheDrifterRace** - story NPC race
- **WorkShopLiberatorRace** - workshop defense liberator variant
- **CAMPPets_Cat_TabbyRace/RoboPawRace, CAMPPets_Dog_GermanShepherdRace/RoboPawRace, CAMPPets_RadHogRace** - CAMP pet system

### New Lite Allies/Companions (7 new)
- Adelaide, Dottie, Grandma Junko, Joey Bello, Lawson, Nuka Agent, Scarberry

### New Player Experience
- `NPESuburbiaWorldspace` (0x006FCD5A) - entirely new worldspace for tutorial/starting area

### Legendary System Overhaul (~1,954 records)
Massive expansion of legendary crafting and effects

### New Event Content
- `E09D_LiberatorRace` - new Liberator variant for events
- 1,141 new E09 (NukaWorld on Tour) records in retail vs 67 cut from dev
- Extensive seasonal event records (Halloween, Christmas, Fasnacht, Meat Week)

### Record Type Growth (Top Changes)
| Type | Dev | Retail | Change |
|------|-----|--------|--------|
| STAT (statics) | 11,697 | 16,297 | +4,600 |
| LAYR (layers) | 2,700 | 5,989 | +3,289 |
| NPC_ | 4,260 | 6,082 | +1,822 |
| LCRT | 2,843 | 5,297 | +2,454 |
| BOOK | 2,765 | 3,879 | +1,114 |
| ACTI | 3,750 | 4,869 | +1,119 |
| ARMO | 2,564 | 3,559 | +995 |
| QUST | 2,128 | 2,574 | +446 |
| RACE | 145 | 190 | +45 |
| WRLD | 29 | 31 | +2 |

---

## Relocated Records (33)
Records with the same `type:editor_id` but different form IDs between dev and retail. The most notable:
- `Appalachia` -> `APPALACHIA` (same hex 0x0025DA15, just capitalization change in editor ID)

---

## Files
- Cut content details: `dev_esm_diff_cut_content.json` (4,972 records)
- New content details: `dev_esm_diff_new_content.json` (79,198 records)
- Raw dev dump: `/tmp/dev_esm_full.txt`
- Raw retail dump: `/tmp/retail_esm_full.txt`
