# Finding 082: NW.esm Full Dump and Analysis

**Date:** 2026-03-20
**Source:** NW.esm (27MB), Fallout 76 Data directory
**Tool:** fo76utils/esmdump with verbose + EDID output
**Dump location:** ~/ai-drive/gamecryptids/data/fallout76/nw_esm_dump/

---

## 1. Record Type Summary

The NW.esm contains 506,492 lines of dump data. Complete record counts:

| Record Type | Count | Description |
|-------------|-------|-------------|
| REFR | 154,992 | Placed object references (the bulk of the file) |
| CELL | 9,733 | Cell records (interior + exterior) |
| TERM | 2,384 | Terminal records |
| ARMO | 1,927 | Armor/clothing items |
| QUST | 49 | Quest records |
| CONT | 476 | Container records |
| REGN | 442 | Region definitions |
| RFGP | 261 | Reference groups |
| STAT | 112 | Static objects |
| GMST | 108 | Game settings |
| SNDR | 105 | Sound descriptors |
| PGRE | 104 | Placed grenades/projectiles |
| ACHR | 74 | Placed actors/NPCs |
| MESG | 46 | Message records |
| LVLI | 38 | Leveled item lists |
| WRLD | 24 | Worldspaces |
| WEAP | 12 | Weapon records |
| MGEF | 9 | Magic effects |
| FLST | 8 | Form lists |
| OMOD | 7 | Object modifications |
| GLOB | 7 | Global variables |
| INFO | 6 | Dialog info |
| DFOB | 6 | Default objects |
| PERK | 5 | Perk records |
| DIAL | 5 | Dialog topics |
| IDLE | 4 | Idle animations |
| AVIF | 3 | Actor value info |
| SMQN | 3 | Story manager quest nodes |
| ARTO | 2 | Art objects |
| EXPL | 2 | Explosions |
| MSTT | 2 | Moveable statics |
| PACK | 2 | AI packages |
| ALCH | 2 | Consumables |
| WTHR | 1 | Weather |
| AMMO | 1 | Ammunition |
| KYWD | 1 | Keyword |
| PROJ | 1 | Projectile |
| SPEL | 1 | Spell |
| NAVM | 1 | Navmesh |
| NAVI | 1 | Navigation info |
| SMBN | 1 | Story manager branch node |

---

## 2. NW-Exclusive Weapons (12 total)

Three weapons appear to be NW-first introductions that were later backported to Adventure mode:

- **RegularBow** (0x0055C152) -- The bow, using `weapons/bow/bow.nif`, ammo linked to `LL_Ammo_RegularBow_Fixed`
- **gaussshotgun** (0x0055C150) -- The Gauss Shotgun, using `weapons/gausspistol/gausspistolreceiverdummy.nif`
- **Cattleprod** (0x0055C153) -- The Cattle Prod, using `weapons/cattleprod/cattleprod.nif`

Other weapons in NW.esm are overrides of existing Adventure weapons:
- crAssaultronLaser, DLC01LightningGun, Tomahawk, Throwing_Knife, DN160_GrognakAxe, SingleActionRevolver, Sickle, CultistBlade, Crossbow

**NW-exclusive ammo:** `Ammo_Arrow_Broadhead` (0x005A5DD2)

**NW-exclusive weapon mods (7 OMOD records):**
- `mod_MissileLauncher_Scope_ScopeLong_Babylon` -- NW-specific missile launcher scope
- `mod_melee_CattleProd_Shock_Babylon` -- NW shock mod for cattle prod
- `mod_RegularBow_Bolt_Explosive_babylon` -- Explosive arrows (NW version)
- `mod_RegularBow_Scope_ScopesMustHave_Babylon` -- NW bow scope
- `ATX_mod_armor_Wood_Torso_Ghillie` -- Ghillie suit wood armor mod
- `ATX_mod_armor_EnclaveScout_Torso_Ghillie` -- Ghillie suit Enclave Scout mod
- `ATX_mod_armor_Marine_Torso_Ghillie` -- Ghillie suit Marine armor mod

**NW-exclusive projectile:** `ProjectileCompoundBow_Babylon` (0x005B2935)

---

## 3. NW-Exclusive Items and Consumables

### Babylon-Specific Consumable
- **Fury_Babylon** (0x0037D292) -- NW version of Fury (model: `props/pyscho.nif`). Separate from Adventure mode Fury.
- **StealthBoy** (0x0004F4A6) -- NW override with different keyword set

### NW-Exclusive Armor/Apparel (17 Babylon-prefixed items)
- `Babylon_Headwear_GladiatorMask` -- NW reward headwear (model: `babylon/armor/championhelmet/`)
- `Babylon_Headwear_CenturionHelmet` -- NW reward headwear
- `Babylon_Headwear_MakeshiftRoninHelmet` -- NW reward (model: `babylon/armor/samuraihelmet/`)
- `Babylon_Apparel_Outfit_LetterJacket_NW` -- NW letterman jacket
- `Babylon_Clothes_HalloweenCostume02Glow_Skeleton` + headwear -- Halloween 2019 NW event
- `Babylon_Armor_Apparel_Headwear_Beanie_Christmas2019` -- Christmas 2019 NW event
- `Babylon_Apparel_Outfit_FurJacketandJeans_Christmas2019` -- Christmas 2019 NW event
- `Babylon_Clothes_GhillieSuit_Outfit_Survivors2020` + helmet -- NW Survivors 2020 event
- `Armor_Babylon_Wood_ArmorSet` -- NW wood armor (model: `armor/wood/m/woodarmor_babylon_go.nif`)
- `Armor_Babylon_EnclaveScoutUniform_ArmorSet` -- NW Enclave Scout (model: `armor/enclavereconuniform/enclavereconuniform_babylon_go.nif`)
- `Armor_Babylon_DLC03_Marine_ArmorSet` -- NW Marine armor (model: `dlc03/armor/combatarmor/combatarmor_babylon_go.nif`)
- Various NONPLAYABLE versions for NPCs

---

## 4. Vault 51 Interior Cells

### Vault51Dungeon (0x0060A6C0)
- Interior cell with XLCN location link 0x0060A6C1
- Contains placed objects (furniture, terminals, props)
- This is the explorable Vault 51 interior unlocked via Overseer rank progression

### Vault51Ext (WRLD:CELL 0x00264124)
- Exterior worldspace cell for the Vault 51 entrance

### PackInBabylonHalloweenDecoOverseerAndZaxRealStorageCell (0x00577859)
- Storage cell for the Overseer and ZAX decorations
- Contains multiple placed `Babylon_Loot_Terminal_02` and `Babylon_Loot_Terminal_03` references
- This is where the Halloween event NW decorations were stored

---

## 5. Cut Content (zzz_ prefix)

**110 total zzz_/ZZZ_ prefixed records found.** Major categories:

### Cut NW Loot Containers (4)
- `zzz_Loot_Babylon` (0x003C3E16) -- Original NW loot box (disabled)
- `zzz_Loot_Babylon_Low` (0x003C3E17) -- Low-tier NW loot (model: small Vault-Tec box)
- `zzz_Loot_Babylon_High` (0x003C4115) -- High-tier NW loot (model: large Vault-Tec box)
- `zzz_Loot_Babylon_Grenades` (0x003C4E2C) -- Dedicated grenade loot box

**Active loot containers (2 remaining):**
- `Loot_Babylon_Med` (0x003C4114) -- Medium tier (model: medium Vault-Tec box), the standard NW terminal
- `Loot_Babylon_NWCorpseBag` (0x003F363D) -- Death drop duffle bag (model: `babylon/nwdufflebag/nwdufflebag.nif`)

### Cut Storm/Skyline Valley Content (21 cells)
- `ZZZStormWeatherLab` -- Test weather lab
- `zzzStormRangerRadioStationTEST` -- Test ranger radio station
- `zzzzzStormVisitorCenter` -- Cut visitor center (5 z's!)
- `zzzStormTrainTunnelsTest` -- Cut train tunnel system
- `zzzSTORMTreetopLookout` -- Cut treetop lookout location
- `zzz76StormCDBTest` -- Storm test cell
- `zzzCUTStormVault63Atrium` -- **CUT Vault 63 Atrium layout** (early Skyline Valley)
- `ZZZ76StormGPVault` -- Cut vault test
- `zzzDebugStormHKFT` -- Debug Hawk's Nest/Fort cell
- `StormVault63AtriumUpperOLD` -- Old upper atrium layout

### Cut Burn/Gleaming Depths Content (3 cells)
- `ZZZBurnChopShop01` -- Cut chop shop interior
- `zzzBURNSQ04TestCell` -- Cut side quest test
- `ZZZBurnCheckpointCanyonInterior` -- Cut checkpoint canyon

### Cut Storm Terminals (12)
- `zzzStorm_CRB_C` -- Camp Rapidan terminal (cut)
- `ZZZ_Storm_CRBT_TS` -- Camp Rapidan terminal (cut)
- `ZZZ_Storm_CR_VP_SIT` / `_SET` / `_SHT` / `_AGT` / `_SWT` / `_ST` -- Multiple Vertibird Pad terminals at Camp Rapidan, all cut
- `ZZZ_Storm_HKFT_LST` -- Hawks Nest Fort terminal (cut)
- `ZZZ_Storm_V63O_DOE` / `_HO_PL` -- Vault 63 Organics terminals (cut)
- `ZZZ_Storm_RB_T` -- Region Boss terminal (cut, replaced by `Storm_RegionBoss_Terminal`)
- Various `zzzStormV63_E_*` engineering terminals (3)
- `zzzStorm_Terminal` / `zzzStorm_Terminal2` -- Generic Storm terminals (cut)

### Cut Armor (50+ items)
Includes cut Ranger armor variants, Fasnacht masks, Pioneer Scout outfits, Civil War outfits, debug ATX items, and seasonal SCORE items. Notable entries:
- `zzz_DEBUG_ATX_Clothes_RangerOutfitClean` -- Debug Ranger outfit
- `zzz_DEBUG_ATX_Headwear_FlightHelmetRed` -- Debug flight helmet
- `ZZZ_Storm_Clothes_RadTurkey_Outfit` -- Cut Storm rad turkey outfit
- `zzz_Storm_LostHeadMirror` -- Cut Storm "Lost" faction mirror head item

---

## 6. Storm Zone Configuration

### Weather System
- `bUpdatePlayerWeatherFromStormLevel` = 1 (GMST) -- Links player weather to storm ring level
- `fWeatherHourOverride` = 13.0 -- Forces time to 1 PM (permanent daytime in NW)
- **NewWeatherPostNukeBlast** (0x002BDCA8) -- The sole weather record, with Nuke76WeatherDistantCloud model and radstorm sky effect

### Storm Visual Effects
- `effects/babylon/babylon_nuke76weatherdistantcloud.nif` -- Distant storm wall
- `effects/babylon/babylon_nuke76explosion.nif` -- Nuke explosion effect
- `Nuke76SmokeCameraAttach` -- Camera smoke effect (attached to player in storm)
- `Nuke76VictimCameraAttach` -- Death camera smoke effect

### Storm Sound
- `BabylonUIStormStopsDUPLICATE001` -- Sound for storm stopping (duplicated, suggesting iteration)

### Storm Damage Settings
- `fFireDamageBase` = 329.0 -- Base fire damage (storm damage type)
- `fFrostDamageBase` = 329.0
- `fPoisonDamageBase` = 329.0
- `fRadsDamageBase` = 329.0
- `fShockDamageBase` = 329.0
- `fEnergyDamageBase` = 329.0
- `fPhysicalDamageBase` = 329.0
- All damage factors set to -0.5 (reduction formula)

---

## 7. NW Map Definitions

### Worldspaces (24 total)
The NW.esm contains **Appalachia** (0x0025DA15) as the main playable worldspace, plus 23 developer test worlds:
- `TestConnorExt`, `TestGabe`, `DebugAlexBurback`, `TestStaticCollectionWarehouse`
- `DevCoryWorld`, `Test76Worldspace`, `TestSLABs`, `TestRobertPOIwarehouse`
- `TestAndrewWorld`, `TestPBRWorld`, `TestTheHillsHaveEyes`, `TestWorkshop`
- `TestLandscape`, `TestRobertWorld`, `TestPhysicsWorld`, `TestSteveCWorld`
- `TestMuckWorld`, `TestJarrodWorld`, `TestJarrod2`, `TestOutsource`
- `TestEffectsWorld`, `TestMadWorld`, `DebugRussellWorld`

### Map Voting System
The QP_Babylon_Master quest contains dialog topics for a map voting system:
- `Babylon_MapVotingTimeToVote` (0x005A0A44) -- ZAX announcing vote time
- `Babylon_MapVotingSelected` (0x005A0A45) -- Map selected announcement
- `Babylon_MapVotingTie` (0x005A0A46) -- Tie-breaker logic (includes random percent check <=10%)

**This confirms a map rotation/voting system existed.** The INFO record (0x005A0A4C) under the Tie topic has a condition `GetRandomPercent <= 10.0`, suggesting the system used weighted randomization for tie resolution.

### Storm/Skyline Valley Regions (pre-release map data in NW.esm)
The NW.esm contains region data for Skyline Valley (Storm) update zones:
- `StormSubRegion01` through `StormSubRegion16` (10 subregions)
- `StormWeatherRegion_DeadZone` -- The Shenandoah dead zone
- `StormObjectRegion_Mountains01` -- Mountain biome objects
- `StormObjectRegion_Swamp01` -- Swamp biome objects
- `StormObjectRegion_Forest01` -- Forest biome objects

### Burning Springs/Gleaming Depths Regions (pre-release)
- `BurningSpringsSubRegion02` through `BurningSpringsSubRegion20` (12 subregions)
- `BurningSpringsDriveinWorkshopRegion`
- `BurningSpringsWeatherRegion`
- `BurningSpringsBorderRegion03`
- `BurnObjectRegion01_Rocky` through `BurnObjectRegion17_RustKingdom` (5 object regions)

---

## 8. NW-Exclusive NPCs and Characters

### ZAX AI / Vault 51
- `PackInBabylonHalloweenDecoOverseerAndZaxRealStorageCell` -- Storage cell for ZAX and Overseer visual assets
- `BabylonUIEndGameOverseerRankGained` (SNDR) -- Sound for ranking up
- `Babylon_PlayerWins` (DIAL) -- ZAX announcing player victory
- `Babylon_ChristmasGreeting` (DIAL) -- ZAX Christmas event dialog

### Placed Actors (74 ACHR records)
74 placed actor references exist in the NW.esm, with 15 having VMAD (script) attachments. These would be quest-related NPCs in Vault 51 and the RSVP questline.

---

## 9. Loot Table System

### Terminal-Based Loot
The NW loot system used interactive terminals rather than simple containers:

**Babylon_Loot_Terminal_02** (0x002BA064) -- Standing terminal model (`terminalonstanding02.nif`)
**Babylon_Loot_Terminal_03** (0x003D79FA) -- Desk terminal model (`terminaldesk01.nif`)
**Babylon_Test_LoreTerminal** (0x0040DEEC) -- Test/lore terminal (`terminalon.nif`)

All three share identical loot logic with 5 tiers:
- Tier checks via GetValue on AVs 0x3A0F44, 0x3A0F45, 0x3A0F46 (likely ring/phase counters)
- Tier 1: Available when round counter > 0 (early game)
- Tier 2: When all three counters == 2
- Tier 3: When all three counters == 3
- Tier 4: When all three counters == 4
- Tier 5: When all three counters == 5
- Uses AV 0x3CAEB9 as a "has been looted" check

The tier system scales loot quality based on how many storm ring contractions have occurred.

### Leveled Item Lists (38 total)
- `LLC_Babylon_Guns_Medium` -- Medium-tier NW gun list (includes bow)
- `LL_Babylon_Weapon_Ranged_RegularBow` -- Bow-specific loot entry
- `LLC_Babylon_Ammo_Normal_Playtest` -- Playtest ammo list (self-referencing, suggesting dynamic scaling)
- 35 ammo lists (all ammo types with "_Fixed" suffix for NW-balanced quantities)
- `LLD_Scorched_Statue` -- Scorched statue drop

### Loot Containers Summary
| Container | Status | Model |
|-----------|--------|-------|
| Loot_Babylon | CUT | (unknown) |
| Loot_Babylon_Low | CUT | Small Vault-Tec box |
| Loot_Babylon_Med | ACTIVE | Medium Vault-Tec box |
| Loot_Babylon_High | CUT | Large Vault-Tec box |
| Loot_Babylon_Grenades | CUT | (unknown) |
| Loot_Babylon_NWCorpseBag | ACTIVE | NW duffle bag |

The evolution from 5 container tiers to a single medium container + death bag suggests the loot system was heavily simplified during development.

---

## 10. Overseer Rank Progression

### Sound Effect
- `BabylonUIEndGameOverseerRankGained` (0x00422179) -- Plays when gaining Overseer rank

### Perk: Babylon_OverlyGenerous02 (0x00479B4A)
This perk scales based on player value 0x2E1 (likely Overseer rank or XP):
- Level 1-199: 30% chance to trigger
- Level 200-399: 50% chance
- Level 400-599: 70% chance
- Level 600+: Always active

This is a progressive generosity perk that increased loot sharing/drops as players ranked up.

### Challenges Rollover
- `BabylonChallengesToRolloverXPList` (0x005A1F21) -- Form list for NW challenges that converted to XP. This list appears empty in NW.esm (populated at runtime or in SeventySix.esm).

### Global Variables
- `NWWorkshopDestructionHealthStructure_Floors` -- Health values for floor destruction in NW CAMP battles
- `NWWorkshopDestructionHealthStructure_Stairs` -- Health values for stair destruction

---

## 11. Game Mode Variants That Never Shipped

### Evidence of Planned Features

**Map Voting System** -- Fully implemented dialog system (Babylon_MapVotingTimeToVote, Babylon_MapVotingSelected, Babylon_MapVotingTie) confirms multiple map variants were planned. The tie-breaking logic with random percent checks suggests a robust voting UI.

**4-Tier Loot System (Cut)** -- The original design had 5 loot container tiers (base, low, med, high, grenades). Only the medium tier survived, suggesting dramatic simplification. The dedicated grenade box (`zzz_Loot_Babylon_Grenades`) implies grenades were originally found in specific containers rather than mixed loot.

**Workshop Blacklist/Whitelist System** -- Two large form lists controlled what CAMP items could be built in NW:
- `Babylon_WorkshopBlacklist` -- Blocked items (lockers, toolboxes, storage containers)
- `Babylon_WorkshopWhitelist` -- Allowed items (stairs, ramps, foundations)
- This suggests NW originally allowed more CAMP building than the final version

**BabylonBlockActivationList** -- Items players couldn't interact with in NW (brew dispensers, workshop terminals, danger room terminals, desks)

**BabylonPersistentMapMarkerExcludeList** -- Map markers hidden in NW mode

**AI Kill Rewards (Never fully implemented?):**
- `fBabylonEndGameCapsPerAiKill_Elite` = 5.0 caps
- `fBabylonEndGameCapsPerAiKill_Medium` = 4.0 caps
- `fBabylonEndGameExperiencePerAiKill_Elite` = 9.0 XP
- These suggest end-game AI enemies that awarded caps/XP -- possibly cut content where AI creatures spawned in the final circle

**Christmas Event** -- `Babylon_ChristmasGreeting` dialog topic on QP_Babylon_Master confirms seasonal NW events with ZAX holiday greetings

---

## 12. NW vs Adventure Mode Stat Differences

### Critical Game Settings (NW overrides)
The 108 GMST records reveal massive balance changes from Adventure mode:

| Setting | NW Value | Effect |
|---------|----------|--------|
| `bNuclearWinterMode` | 1 | Master toggle for NW |
| `bWeaponConditionDamage` | 0 | **Weapons don't degrade** |
| `bDisableSurvival` | 1 | No hunger/thirst |
| `bDisableDisease` | 1 | No diseases |
| `bDisableAddiction` | 1 | No addictions |
| `bHoldToReviveEnabled` | 1 | Downed/revive system |
| `fHoldToReviveHoldTime` | 2.5s | Revive hold duration |
| `fPlayerBaseReviveHealth` | 125 | Health after revive |
| `bPVPNormalizeEnabled` | 0 | No PVP level scaling |
| `bPlayerHasUnlimitedLockPicks` | 1 | Infinite lockpicks |
| `iContainerLockLevelOverride` | 1 | All containers level 1 lock |
| `iTerminalLockLevelOverride` | 1 | All terminals level 1 hack |
| `iHackingMinWords` / `MaxWords` | 8 / 8 | Fixed 8-word hacking |
| `fJumpingAPDrain` | 0 | **Free jumping** |
| `fCombatPlayerLimbDamageMult` | 0 | **No limb damage** |
| `fLimbDamageFactor` | 0 | Limb damage completely disabled |
| `bDisableExplosionLimbDamage` | 1 | No explosion crippling |
| `fCombatPlayerDamagePlayerMult` | 1.0 | Full PvP damage (no Adventure slap) |
| `bDeathDropAllExceptCosmeticAndBrokenItems` | 1 | Death drops everything |
| `fXPModMult` | 0 | **No XP from kills** |
| `fDamageStrengthMult` | 0 | Strength doesn't affect damage |
| `fAVDHealthStartEndMult` | 0 | Endurance doesn't affect health |
| `fAVDActionPointsMult` | 0 | Agility doesn't affect AP |
| `fAVDCarryWeightMult` | 0 | Strength doesn't affect carry weight |
| `fAVDCarryWeightBase` | 75 | Fixed 75 carry weight |
| `fAVDMeleeDamageMult` | 0 | No melee SPECIAL scaling |
| `fSprintActionPointsEndMult` | 0 | Endurance doesn't affect sprint |
| `fVATSCriticalChargeMult` | 0 | No VATS crit charging |
| `fVATSChancePerceptionMultiplier` | 0 | Perception doesn't affect VATS |
| `fLockSkillMult` | 0 | Lock skill irrelevant |
| `bPipboyShowPlayerXPInfo` | 0 | Hide XP display |
| `fMagicDiseaseTransferMult` | 0 | No disease transmission |
| `fMoveCampCost` | 10 | CAMP move cost: 10 caps |
| `fPlayerMobility*CrippledSpeedMult` | 1.0 | No speed penalty from crippled legs |
| `bSetAllRegionNukable` | 1 | All regions can be nuked |
| `fLeveledLockMult` | 0 | No leveled locks |
| `fMapMarkerScale` | 2.5 | Enlarged map markers |
| `fEnemyMarkerMaxDistance` | 12000 | Enemy markers visible at long range |
| `bAllowCampInRestrictedAreas` | 1 | CAMP anywhere |
| `fCombatActionPointsRegenRateMult` | 1.0 | Normal AP regen in combat |
| `fOutOfBreathActionPointsRegenDelay` | 0 | No AP regen delay |
| `fBabylonPlayerHealthOffset` | 5.0 | +5 base health adjustment |
| `bShowFeaturedItemPopup` | 0 | No Atom Shop popups |
| `bEnableItemConditionDamage` | 1 | Items still take condition damage (despite weapons not) |

### Armor Formula Overrides
NW completely rebuilds the armor damage reduction formula:
- `fArmorBaseFactor` = 0 (zeroed out)
- `fClothingArmorBase` = 0
- `fPhysicalArmorBase` = 0
- `fEnergyArmorBase` = 0
- `fFireArmorBase` = 0
- `fFrostArmorBase` = 0
- All physical/energy/fire/frost armor factors set to 1.0
- `fPoisonArmorBase` = 280 and `fPoisonArmorFactor` = 5.4 (poison heavily resisted)
- `fShockArmorBase` = 280 and `fShockArmorFactor` = 5.7 (shock heavily resisted)

This means in NW, armor provided minimal physical/energy/fire protection but significant poison and shock resistance -- likely to make the storm (which used these damage types) survivable in early rings but deadly in late game.

### Stagger Completely Disabled
- `iStaggerAttackChance` = 0
- `fStagger1WeapAR` = 0
- `fStagger2WeapAR` = 0
- `fStaggerBowAR` = 0
- `fStaggerDaggerAR` = 0

### NW Magic Effects
- `Mutation_TwistedMusclesEffect_Babylon` -- NW-specific Twisted Muscles (separate from Adventure)
- `Babylon_Fury_Effect` -- NW-specific Fury drug effect
- `Mutation_TwistedMuscles_Babylon` (SPEL) -- NW spell version

### Mutation Whitelist
`SURV_MutationWhiteList` -- Controls which mutations can appear in NW mode. The mutation system was modified:
- `SURV_MutationRollMult` (GLOB) -- Mutation chance multiplier
- `SURV_MutationThreatRollCooldownMinutes` (GLOB) -- Cooldown between mutation rolls

---

## 13. RSVP Questline (Responders/Vault 51 Story)

The RSVP quests represent the Vault 51 Overseer backstory questline, unlocked through Overseer rank progression:

### Quest Chain
1. **RSVP00_Quest_Vector_to_Flatwoods** -- Introduction quest, directs to Flatwoods
2. **RSVP00_Quest_Master** -- Master quest tracking overall RSVP progress
3. **RSVP01_Quest** ("Thirst") -- Water safety quest, finding Kesha, collecting water samples
4. **RSVP02_Quest** ("Hunger") -- Food quest, finding Delbert's body, cooking Ribeye steak
5. **RSVP03_Quest** -- Camp quest, finding Miguel's camp, listening to holotape
6. **RSVP04_Quest** -- Final quest with control tower terminal

### Developer Notes in Quest Data
The RSVP quests contain extensive designer notes (NAM2/SCFC fields) revealing the internal development process:
- Confluence wiki links (`bnet-confluence.zenimax.com:8443/display/P7/`)
- Checkpoint-based quest flow (CP 500, CP 1000, etc.)
- Detailed spawn wave logic for encounters
- Shared vs non-shared objective tracking

### RSVP Terminals (48 terminal records)
Extensive terminal network for the RSVP questline including:
- Kiosk terminals (registration, status, courses)
- Database terminals (guest logs, volunteer records)
- Admin terminals (restricted access, food management)
- Kitchen terminals (Delbert's cookbook, bug reports, pantry)
- Science terminals (water testing, cooked samples)
- Miguel's journals and research (bug research)

---

## 14. Additional Findings

### "Storm" Content (Skyline Valley Pre-Release in NW.esm)
The NW.esm contains extensive pre-release data for the Skyline Valley update:
- 77 Storm-prefixed references
- Full terminal networks for locations: Camp Rapidan, Hawks Nest Fort Tower, Red Rocket Motel, Shenandoah Visitor Center, Summer Camp, Vault 63 Organics labs, Natural Gas facility
- `Storm_MQ13_LightningHarvester*` terminals (A, B, C) -- Lightning harvester quest
- `Storm_MQ13_Pt2_WeatherMachineControls` -- Weather machine controls
- `Storm_RegionBoss_Terminal` -- Region boss system
- `StormPresidentialBunker` -- Presidential bunker interior cell

### "Burn" Content (Gleaming Depths Pre-Release)
- Rust Kingdom faction: `BurnObjectRegion17_RustKingdom`, Raider helmets and outfits
- Bounty Hunter system: `Burn_Clothes_Outfit_BountyHunter`, `BURN_BountyGiver_*`
- Deathclaw Tamer: `Burn_Armor_Outfit_DeathclawTamer`
- `BURN_ARMO_AvaOutfit` -- Named NPC outfit

### "Moon" Content (Skyline Valley Flavor)
- Blue Moon-themed outfits: Farmhand, Cowboy, Trucker, Ogua Hunter, Blue Devil
- Blue Ridge Scout gear
- Luca Costa cowboy outfit (model: `bluemoon/clothes/lucacosta/`)

### Nuke System
The QP_Babylon_Master quest contains three nuke blast markers and art objects:
- `NukeBlastMarkerA/B/C` -- Three possible nuke locations
- `IncomingNukeA/B/C` -- Incoming nuke warning aliases
- `NukeBlastArtA/B/C` -- Visual effect aliases
- `EN07_NukeBlastRadius` (GLOB) -- Nuke blast radius
- `EN07_Blast_ExplosionDistanceGlobal` (GLOB) -- Explosion distance
- `EN07_FleeBlastObjTimer` (GLOB) -- Flee timer for NPCs

### QP_Babylon_Master Quest Structure
The main NW game quest (0x003C3E3E) with 0x41 (65) aliases, managed by story manager branch `QP_Babylon_Branch`. Condition: `GetEventData == 1.0` on event 0x314B0000 (QuickPlay game start event).

---

## 15. Cryptid Hunting Implications

### What NW.esm Reveals About Hidden Content
1. **The map voting system** confirms multiple NW map variants were planned. Only Flatwoods was ever used, but the infrastructure for Charleston, Morgantown, and others was built.
2. **The 5-tier loot system** was collapsed to 1 tier, suggesting major late-development changes to NW's design.
3. **AI kill rewards** (caps + XP for elite/medium kills) suggest PvE elements in the final circle were planned or prototyped.
4. **Storm/Burn/Moon content** in NW.esm means the plugin was used as a dumping ground for in-development content from later updates. This is unusual and suggests NW.esm was a convenient override layer.
5. **The zzz-prefixed terminals** from Storm (Skyline Valley) and their cut Vault 63 content pre-date the final release versions, showing iteration on location design.
6. **RSVP questline** is fully intact with designer notes -- these quests were the narrative backbone of Nuclear Winter's single-player exploration component.

### Items for Further Investigation
- Cross-reference the 1,927 ARMO records against SeventySix.esm to find NW-exclusive cosmetics not available in Adventure mode
- The 442 REGN records may contain NW-specific spawn/loot regions worth mapping
- The 2,384 TERM records contain the majority of NW's content -- full terminal dump could reveal narrative content
- The `BabylonExcludeList` and `BabylonBlockActivationList` form lists enumerate every item Bethesda explicitly blocked from NW, which inversely reveals what WAS allowed
