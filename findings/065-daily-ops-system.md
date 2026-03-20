# Finding 065: Daily Ops System - Complete Mechanical Extraction

**Source**: ESM dump (GLOB, FLST, SPEL, KYWD, LVLI, MGEF, PERK records), decompiled Papyrus scripts (DailyOps_Mode02:Master, DailyOps_All:DailyMutation, DailyOps_All:HighElderMode, SupplyRun:ActivatorProgress, EventMutationScript, EWS_Manager, etc.), curve tables
**Confidence**: CONFIRMED (direct game data)

---

## 1. Mode Types

### Mode 01: Uplink ("Supply Run")
- **Script namespace**: `SupplyRun:*`
- **Objective**: Repair repeater, then stand near two Uplink devices to fill progress bars
- **Progression stages** (from Mode01 quest fragments):
  - Intro > Repeater Repaired > Uplink 1 Started > Uplink 1 Complete > Uplink 2 Started > Uplink 2 Completed > Boss Room Arrived > Boss Incoming > Boss Dead
- **Uplink mechanic** (`SupplyRun:ActivatorProgress`):
  - Progress ticks every `PROGRESS_INTERVAL = 1.0` seconds
  - Speed scales with player count in proximity (`PROXIMITY_THRESHOLD = 1024 units`)
  - Backup multipliers when fewer players are near the Uplink:
    - 4 players: `2.5x`
    - 3 players: `2.14x`
    - 2 players: `1.87x`
    - 1 player: `1.67x`
    - 0 players: `0.5x` (progress regresses)
  - Visual stage transitions at configurable thresholds (Stage1/2/3 percentage breakpoints)

### Mode 02: Decryption
- **Script namespace**: `DailyOps_Mode02:*`
- **Master script**: `DailyOps_Mode02:Master`
- **Objective**: Kill enemies in rounds, defeat code-carrier bosses, disable Radio Interceptors
- **Progression stages** (from Master script):
  - ST_INIT (0) > ST_AMB_TRIGGER_ENTERED (50) > ST_KILLED_R1_ENEMIES (100) > ST_KILLED_FIRST_BOSS (200) > ST_COMPLETED_FIRST_ACTIVATOR (300) > ST_KILLED_R2_ENEMIES (400) > ST_KILLED_SECOND_BOSS (500) > ST_COMPLETED_SECOND_ACTIVATOR (600) > ST_KILLED_R3_ENEMIES (700) > ST_KILLED_THIRD_BOSS (800) > ST_COMPLETED_THIRD_ACTIVATOR (900) > ST_MISSION_COMPLETE (1500)
- **Three Radio Interceptors** must be disabled (activators at indices 0, 1, 2)
- Interceptor states cycle through: Running > DownOne > DownTwo > Disabled (animation states JumpState00-03)
- Enemies drop code fragments when killed; codes are used at interceptors

### No Mode 03+ Found
- No `DailyOps_Mode03` or higher exists in ESM data. Only two quest modes are defined.

---

## 2. All Mutations (Single)

Extracted from `DailyOps_MutationName_*` keywords and corresponding spell records:

| # | Mutation | FormID (Spell) | Effect |
|---|----------|----------------|--------|
| 1 | **Volatile** | 0x005B2E9E | Enemies explode on death (Explosion_DailyOps_Mutation_Volatile, 0x005B2E99). Deals frag grenade-level AoE damage. Has perk DailyOps_MutationPerk_Volatile (0x005DB341). |
| 2 | **Resilient** | 0x005C6BFB | Enemies cannot be killed by ranged damage alone -- must be finished with melee. Plays invulnerable impact material (ResilientImpactVFX script). Condition: only applies when target health <= 2 (i.e., at very low HP they become immune to ranged). Blocked from certain Mutated Public Events via `MPE_NotResilient` keyword. |
| 3 | **Active Camouflage** | 0x005C6BE9 | Enemies turn invisible. Conditions: only cloaks when not dead, distance >= 1.5 (1500 units), and not in attack state 16 (power attack). Blocked via `MPE_NotCamo` keyword. |
| 4 | **Vampire** | 0x005D02B0 | Enemies heal when they deal damage to players. Companion spell `DailyOps_Mutation_VampireRestore` (0x005D02B1) fires the regen. Uses effect `DailyOps_VampireRegenEffect`. |
| 5 | **Freezing Touch** | 0x005D03C5 | Enemy attacks apply progressive freeze stages to players. 4-stage system (Normal > Chilled > Frosted > Frozen) defined in `FreezingTouchFreezeEffect` script. Each stage requires multiple hits; not hitting resets stages over time (`LastHitTime` property). Also has explosion variant `DailyOps_Mutation_FreezingTouchExplosion`. Slow spell: `DailyOps_Mutation_FreezingTouch_SlowSpell` (0x0068CC25). |
| 6 | **Vengeful Rage** | 0x005D1C0B | When enemies are injured, nearby allies enrage and deal increased damage. Has explosion component `DailyOps_Mutation_VengefulRageExplosion` (0x005D1C0C) and VFX effect. Perk: `DailyOps_MutationPerk_VengefulRage` (0x005D1C0A). |
| 7 | **Toxic Blood** | 0x005F092B | Enemies leave toxic hazard zones on death. Three tiers of increasing damage: TierOneToxin, TierTwoToxin, TierThreeToxin (from ToxicBloodEffect script). Creates `DailyOps_Mutation_ToxicBlood_Hazard` (0x005F0B28) -- a persistent ground hazard with custom model (toxicbloodhazard.nif). Explosion variant: `Explosion_DailyOps_Mutation_ToxicBlood` (0x005F0925). |
| 8 | **Reflective Skin** | 0x005F0D15 | Enemies periodically gain a damage-reflect shield. Has timer offset system (`ReflectiveSkinOffsetTimer` script) so enemies don't all activate simultaneously -- random delay up to `MaxDelayTime` seconds after spawn. Multiple spell phases: InactiveSpell > WarningSpell > ReflectSpell > SFXSpell. Perk for reflect SFX: `DailyOps_Mutation_ReflectiveSkin_ReflectSFXPerk`. |
| 9 | **Group Regeneration** | 0x005F0DB3 | Enemies heal nearby allies. The heal spell (`DailyOps_Mutation_GroupRegenerationHeal`, 0x005F0DB4) only fires when the GroupRegeneration effect is active on caster, caster is alive, target is hostile to player, and target is NOT a specific excluded race (0x6B3A3E). Blocked from certain events via `MPE_NotSwiftFooted`. |
| 10 | **Swift-Footed** | 0x005F0E5F | Enemies move significantly faster. Blocked via `MPE_NotSwiftFooted` keyword (0x0067E98A). |
| 11 | **Danger Cloud** | 0x0068C8A5 | Enemies emit damaging poison clouds. Damage spell: `DailyOps_Mutation_DangerCloud_DMGSpell` (0x0068C8A6). Damage scales by level via curve table `CT_DailyOps_Mutation_DangerCloud_DMG` (0x0068EC58). Only active when enemy is alive (condition: GetDead == 0). |

**Danger Cloud Damage Curve** (from `dops_dangercloud_dmg.json`):
| Enemy Level | Damage |
|-------------|--------|
| 1 | 20 |
| 10 | 30 |
| 25 | 50 |
| 50 | 120 |
| 75 | 140 |
| 100 | 160 |

### Mutation Ignore Keywords
Each mutation has a companion `DailyOps_IgnoreMutation_*` keyword that can be placed on specific enemy types to exempt them:
- `DailyOps_IgnoreMutation_Volatile` (0x005B2E9C)
- `DailyOps_IgnoreMutation_Resilient` (0x005C72BA)
- `DailyOps_IgnoreMutation_ActiveCamouflage` (0x005C6BE5)
- `DailyOps_IgnoreMutation_Vampire` (0x005D02AA)
- `DailyOps_IgnoreMutation_FreezingTouch` (0x005D03BF)
- `DailyOps_IgnoreMutation_VengefulRage` (0x005D1C04)
- `DailyOps_IgnoreMutation_ToxicBlood` (0x005F0AAF)
- `DailyOps_IgnoreMutation_ReflectiveSkin` (0x005F0D11)
- `DailyOps_IgnoreMutation_GroupRegeneration` (0x005F0D12)
- `DailyOps_IgnoreMutation_SwiftFooted` (0x005F0E5A)

FormList for all ignore keywords: `DailyOps_Mutation_IgnoreKeyword_FormList` (0x005F23B6)

---

## 3. Double Mutations (Combined Mutations)

When `DailyOps_Mutation_Mode_Index` == 1, enemies receive a combined double mutation from a separate pool. These are NOT random pairs of single mutations -- they are pre-authored combinations with unique names and spell records.

| Double Mutation | FormID (Spell) | Component Mutations |
|-----------------|----------------|---------------------|
| **Swift Stalker** | 0x0060A6A8 | Swift-Footed + Active Camouflage (fast AND invisible; conditions: not dead, distance >= 1.5, not power attacking) |
| **Stinging Frost** | 0x0060A6A7 | Freezing Touch + ? (freeze damage combination) |
| **Relentless** | 0x0060DCDC | Vengeful Rage + Group Regeneration (enrage + healing aura) |
| **Unstable** | 0x0060DCDD | Volatile + Vengeful Rage (explode on death + enrage when hurt) |
| **Blistering Cold** | 0x0060DCDE | Freezing Touch + ? (cold-based combination) |
| **Chilling Mend** | 0x0060EC80 | Freezing Touch + Group Regeneration (freeze players + heal allies) |
| **Clouded Toxins** | 0x0060EC81 | Active Camouflage + Toxic Blood (invisible + leave poison on death; same camo conditions) |
| **Vaporous** | 0x0060EC7F | Active Camouflage + Danger Cloud (invisible + poison cloud aura; same camo conditions) |

### Double Mutation FormLists
- `DailyOps_DoubleMutation_Master_FormList` (0x0060A6A0)
- `DailyOps_DoubleMutation_Mutation_Spell_FormList` (0x0060A6A1)
- `DailyOps_DoubleMutation_Mutation_NameMod_FormList` (0x0060A6A2)
- `DailyOps_DoubleMutation_Mutation_Valid_FormList` (0x0060A69F)

### Double Mutation Globals
- `DailyOps_DoubleMutation_Index` (0x0060A2BB) -- which double mutation is active
- `DailyOps_DoubleMutation_TestFirst_Index` (0x0060A2BD) -- value 1.0
- `DailyOps_DoubleMutation_TestSecond_Index` (0x0060A2BE) -- value 1.0
- `DailyOps_Mutation_Mode_Index` (0x0060E42E) -- 0 = single mutation, 1 = double mutation

### Double Mutation Reward
Keyword: `DailyOps_DoubleMutationReward` (0x0062A86A) -- used to gate additional reward rolls when double mutation is active.

---

## 4. Cut / Disabled Mutations

### zzz_DailyOps_Mutation_LastStand (CUT)
- Keyword: `zzz_DailyOps_MutationName_LastStand` (0x0068C4AC)
- Spell: `zzz_DailyOps_Mutation_LastStand` (0x0068C4B0)
- Effect: `zzz_DailyOps_MutationEffect_LastStand_ApplyPerk` (0x0068C4AD)
- Perk: `zzz_DailyOps_MutationPerk_LastStand` (0x0068C4AF)
- Shader spell: `zzz_DailyOps_MutationSpell_LastStand_ApplyShader` (0x0068C4B3)
- NameMod: `zzz_DailyOps_MutationNameMod_LastStand` (0x0068C4AE)
- **Analysis**: Fully built mutation that was cut before release. "Last Stand" likely made enemies more dangerous (damage boost or damage resistance) when at low health.

### Other Cut/Deprecated Daily Ops Records
- `zzz_DailyOps_DefaultMutation_FormList` (0x005FE5CD) -- cut default mutation system
- `zzz_DailyOps_Mutation_Default_Mode01` (0x005D1F85) -- cut default mutation for Uplink
- `zzz_DailyOps_Mutation_Default_Mode02` (0x005FE5CE) -- cut default mutation for Decryption
- `zzz_DailyOps_Mode02_DamageMultPerk` (0x005FD6AE) -- cut damage multiplier perk for Decryption
- `zzz_DailyOps_Ench_VolatileExplosion` (0x0061285B) -- cut enchantment variant of Volatile
- `zzz_DailyOps_CryoBreathSlowEffect_Stage2` (0x005D2323) -- cut second tier of Freezing Touch slow
- `zzzDailyOps_MutationEffectSFX_Resilient` (0x005E47C2) -- cut SFX variant
- `zzzDailyOps_Mutation_ActiveCamouflage_InvisibilitySpell` (0x005D22BE) -- earlier version of camo invisibility
- `zzzDailyOps_Mutation_ActiveCamouflage_InvisibilityDispel` (0x005D22BF) -- earlier version of camo dispel
- `DEL_DailyOps_Mutation_Volatile_ExplosionSpellDUPLICATE000` (0x005DBDC9) -- duplicate cleanup
- `DEL_DailyOps_MutationPerk_VolatileDUPLICATE000` (0x005DBDC8)
- `DELETED_DailyOps_ExitMessage` (0x005DC206) -- originally had a different exit message
- `DELETED_SkinSuperMutantBoss_DailyOps` (0x005DC820) -- cut unique super mutant boss skin
- `DELETED_LvlScorchedCreature_RadAnt_DailyOps` (0x005F579D) -- cut Scorched Rad Ant enemy
- `DELETED_LvlScorchedCreature_Bloatfly_DailyOps` (0x005F579F) -- cut Scorched Bloatfly enemy
- `DEL_DailyOps_BossOutfit_Scorched` (0x005F57A7) -- cut Scorched boss outfit
- `DEL_crPRCBoss_RiotShotgun_DailyOps` (0x00617303) -- cut PRC Boss riot shotgun
- `DEL_crMoleMinerBoss_NukeLauncher_DailyOps` (0x005F838E) -- cut Mole Miner Boss nuke launcher
- `DEL_DailyOps_Template_Keyword_Molerat` (0x005F6DBF) -- cut mole rat enemy template
- `DELETED_DailyOps_Mode02_MinibossDamResist` (0x005F12F7) -- originally bosses had a damage resistance perk

### Cut SCORE Challenges
- `CUT_SCORE_Challenge_Weekly_QuestComplete_DailyOps_Paladin` (0x005EBE8D)
- `CUT_SCORE_Challenge_Weekly_QuestComplete_DailyOps_Elder` (0x005EBE8E)
- `CUT_SCORE_Challenge_Daily_QuestComplete_DailyOps_Paladin` (0x005D22E2)
- `CUT_SCORE_Challenge_Daily_QuestComplete_DailyOps_Elder` (0x005D22E3)
- `CUT_SCORE_Challenge_Weekly_QuestComplete_DailyOps_FullTeam` (0x005D22DE)
- `CUT_SCORE_Challenge_Daily_QuestComplete_DailyOps_FullTeam` (0x005D22DB)

**Key finding**: Bethesda originally planned SCORE challenges for specifically achieving Paladin/Elder rank and for completing with a full team. These were cut, replaced with the simpler "complete a Daily Op" challenges.

---

## 5. Rotation System

### How Rotation Works
The Daily Ops rotation is entirely **server-pushed via Live Content Pipeline (LCP)** globals. The game does NOT calculate rotation locally. Three independent indices are set by the server:

| Global | FormID | Purpose | Default |
|--------|--------|---------|---------|
| `DailyOps_GameMode_Index` | 0x005C65E4 | Which mode (Uplink/Decryption) | 0 |
| `DailyOps_Location_Index` | 0x005C65E3 | Which map location | 0 |
| `DailyOps_Encounter_Index` | 0x005AE09C | Which enemy faction | 0 |
| `DailyOps_Mutation_Index` | 0x005B2E9A | Which mutation (single) | 0 |
| `DailyOps_Mutation_Mode_Index` | 0x0060E42E | 0=single, 1=double | 0 |
| `DailyOps_DoubleMutation_Index` | 0x0060A2BB | Which double mutation | -- |
| `DailyOps_Encounter_FormList_Selection_Index` | 0x0061DA37 | Sub-selection within encounter list | 0 |

### FormLists Indexed by These Globals
- `DailyOps_GameMode_FormList` (0x005C65E2) -- indexed by GameMode_Index
- `DailyOps_Location_FormList` (0x005C65E0) -- indexed by Location_Index
- `DailyOps_Encounter_FormList` (0x005AE09A) -- indexed by Encounter_Index
- `DailyOps_Mutation_Master_FormList` (0x005F23B4) -- indexed by Mutation_Index
- `DailyOps_Mutation_Spell_FormList` (0x005F23B7) -- parallel spell list
- `DailyOps_Mutation_NameMod_FormList` (0x005F23B5) -- parallel name mod list
- `DailyOps_Mutation_Valid_FormList` (0x005C65E1) -- validation bitmask
- `DailyOps_Mutation_Valid_Master_FormList` (0x0061DA35) -- master validation
- `DailyOps_Encounter_Valid_Master_FormList` (0x0061DA36) -- encounter validation

### Location Size Classification
Locations are classified as Large or Small, affecting spawn counts:
- `DailyOps_Location_Large_FormList` (0x00602815)
- `DailyOps_Location_Small_FormList` (0x00606278)

### All Map Locations (per-location encounter FormLists)
| Location | FormList FormID |
|----------|----------------|
| Morgantown High School | 0x0078A03A |
| Arktos Pharma Lab | 0x0078A03B |
| Charleston Capitol | 0x0078A03C |
| Uncanny Caverns | 0x0078A03D |
| Vault 96 | 0x0078A03E |
| Watoga High School | 0x0078A03F |
| Watoga Civic Center | 0x0078A040 |
| West Tek Research | 0x0078A041 |
| Aquarium (AC02) | 0x0078A042 |
| Pitt (Pitt01) | 0x0078A043 |
| Vault 94 | 0x0078A044 |
| Burning Mine | 0x0078A045 |
| Garrahan Mining | 0x0078A046 |
| The Burrows | 0x0078A047 |
| Valley Galleria | 0x0078A048 |
| Glassed Cavern | 0x00796314 |
| Community Center (AC03) | 0x00796315 |

Each location has its own encounter FormList that defines which enemy factions can spawn there.

### Mutation Chance
- `DailyOps_Mutation_Chance` (0x005B2E9B) = **1.0** (100% chance -- mutations always apply)

---

## 6. Time Thresholds (Completion Ranks)

Extracted from GLOB records:

| Rank | Time Threshold (seconds) | Time (minutes) | Global FormID |
|------|--------------------------|-----------------|---------------|
| **Elder** | 480 | 8:00 | `DailyOps_Timer_Tier_High` (0x005CB976) |
| **Paladin** | 720 | 12:00 | `DailyOps_Timer_Tier_Medium` (0x005CB977) |
| **Knight** | 960 | 16:00 | `DailyOps_Timer_Tier_Low` (0x005CB978) |
| **Initiate** | >960 | >16:00 | (no global -- any completion beyond Knight) |

---

## 7. Reward Tiers and Drop Tables

### Rare Reward Roll Chances Per Tier
| Rank | Rare Roll Chance (%) | Global FormID |
|------|---------------------|---------------|
| **Elder** | **100%** | `DailyOps_RareRoll_Tier_High` (0x005CB979) = 100 |
| **Paladin** | **10%** | `DailyOps_RareRoll_Tier_Medium` (0x005CB97A) = 10 |
| **Knight** | **5%** | `DailyOps_RareRoll_Tier_Low` (0x005CB97B) = 5 |
| **Initiate** | **0%** | (no rare roll) |

- `DailyOps_Rewards_ChanceNone_Rare` (0x005D080D) = **50** -- within the rare loot table itself, there is a 50% chance of getting "nothing" (ChanceNone), effectively halving the displayed percentages for any specific rare item.

### Reward Structure

**Per-tier chase reward lists**:
- `LL_DailyOps_Rewards_Chase_Tier01` (0x005CB9FF) -- Knight rewards. Random % check against `DailyOps_RareRoll_Tier_Low` (5%). Routes to High or Low LVL chase list based on player level >= 50.
- `LL_DailyOps_Rewards_Chase_Tier02` (0x005DBD0F) -- Paladin rewards. Random % check against `DailyOps_RareRoll_Tier_Medium` (10%). Same level routing.
- `LL_DailyOps_Rewards_Chase_Tier03` (0x005DBD0D) -- Elder rewards. Random % check against `DailyOps_RareRoll_Tier_High` (100%). Same level routing.

**Level-based chase lists** (level >= 50 vs below):
- `LLS_DailyOps_Rewards_Chase_HighLVL` (0x005D9CBB) -- high-level rare + uncommon pools
- `LLS_DailyOps_Rewards_Chase_LowLVL` (0x005D9CBD) -- low-level rare + uncommon pools

**High-level chase pools**:
- `LL_DailyOps_Rewards_HighLVL_Chase_Rare` (0x005D080E) -- plans like Burrows Signs, Valley Galleria Signs, Super Reactor, The Gutter, Whistle in the Dark, etc. Each entry has an entitlement check (condition 875) and a "not already known" check (condition 853) for learning protection.
- `LL_DailyOps_Rewards_HighLVL_Chase_Uncommon` (0x005CB9FC) -- uncommon plans with same protection system
- `LL_DailyOps_Rewards_HighLVL_Chase_RareUntradable` (0x0073DAB4) -- untradable rare rewards (newer additions)
- `LL_DailyOps_Rewards_HighLVL_Chase_UncommonUntradable` (0x0073DAB5) -- untradable uncommon rewards

**Low-level chase pools**:
- `LL_DailyOps_Rewards_LowLVL_Chase_Rare` (0x005D9CBC) -- routes to `LLS_DailyOps_Rewards_Recipes_Rare` (common + PA recipes)
- `LL_DailyOps_Rewards_LowLVL_Chase_Uncommon` (0x005D9CBE) -- routes to `LLS_DailyOps_Rewards_Recipes_UnCommon`

**Repeatable quest rewards** (`LL_DailyOps_Repeatable_Quest_Rewards`, 0x005CBA06):
- Currency (`LLS_DailyOps_Rewards_Currency`, 0x005CB9FB)
- Legendaries (0x00391F05)
- Aid items (`LLS_DailyOps_Rewards_Aid`, 0x005DC356)
- Additional aid (0x005DC357)
- More legendaries (x2)

**Chase Tier FormLists** (used by entitlement system):
- `DailyOpsRewardsChaseTier01FormList` (0x005E5401)
- `DailyOpsRewardsChaseTier02FormList` (0x005E5403)
- `DailyOpsRewardsChaseTier03FormList` (0x005E5402)

### Cursed Weapons
- `LL_DailyOps_Rewards_CursedRollingPin` (0x005FDE0C) -- special cursed weapon reward

### Double Mutation Bonus Currency
- `LL_DailyOps_Rewards_AdditionalCurrency_Tier03` (0x005DBD10) -- Elder tier gets double currency when `DailyOps_Mutation_Mode_Index` == 1 (double mutation active). Contains two entries from the currency list, with the second gated by the double mutation global check.

### XP Rewards
| Reward Type | XP Amount | Global FormID |
|-------------|-----------|---------------|
| Additional (first completion) | 500 | `XP_DailyOps_Reward_Additional` (0x005DBD0A) |
| Repeatable | 300 | `XP_DailyOps_Reward_Repeatable` (0x005CBA08) |

### Contextual Ammo Drops
Daily Ops gives significantly more contextual ammo than normal gameplay:
| Source | Ammo Count |
|--------|------------|
| Regular enemy kill | 4 |
| Boss kill | 12 |
| Quest completion reward | 35 |

---

## 8. Enemy Spawning System (Wave System)

### Decryption Mode (Mode 02) Wave Architecture

From `DailyOps_Mode02:Master`:

**Wave types** (constant integers):
- `AMBIENT_WAVE = 0` -- background enemies
- `MINIBOSS_WAVE = 1` -- code carrier miniboss
- `BOSS_WAVE = 2` -- final boss
- `MINION_WAVE = 3` -- minions that follow boss/miniboss

**Kill requirements per round** (defaults):
- Round 1: `R1NumEnemiesToKill = 10`
- Round 2: `R2NumEnemiesToKill = 10`
- Round 3: `R3NumEnemiesToKill = 10`

**Max concurrent enemies by location size**:

| Round | Normal | Large | Small |
|-------|--------|-------|-------|
| R1 | 6 | 7 | 6 |
| R2 | 7 | 8 | 7 |
| R3 | 8 | 9 | 8 |

**Boss mechanics**:
- `DesiredMinions_Num = 2` -- each miniboss/boss gets 2 minion escorts
- Guards assigned to Radio Interceptors: `R1Guards_Num = 4` (first round), `R2Guards_Num = 3` (subsequent)
- `RecruitmentRange = 900.0` units -- ambient enemies within this range can be promoted to minions/guards
- `RecruitMinHealthPercent = 0.9` -- only healthy enemies (>90% HP) get recruited
- After 1 activator completed (`NumActivatorsCompleted_RunThreshold = 1`), enemies switch to running behavior

**Minion recruitment system**:
- Ambient enemies are dynamically promoted to "minions" or "guards" based on proximity and health
- `PromotedToMinion_AmbEnemies` -- ambient enemies upgraded to minion role
- `DemotedToAmbEnemy_SpawnedMinions` -- minions demoted back to ambient if needed
- Guard spawns tracked per-activator: `GuardSpawnRecruiting` boolean array

### Uplink Mode (Mode 01) Wave Architecture
- Uses `SupplyRun:EWSModuleBase` for wave management
- Waves tied to quest stages via `StageStartWave` and `StageStopWave`
- Supports "endless waves" (`IsEndlessWave` flag) for continuous spawning during uplink progress
- `SupplyRun:AmbientEWS` handles ambient enemy spawning with `WAVE_BUFFER = 0.0` (no delay between waves)

### EWS (Encounter Wave Script) Manager
From `DailyOps_Mode02:EWS_Manager`:
- Enemy type determined by `DailyOps_Encounter_Index` global indexing into `DailyOps_Encounter_FormList`
- Location selected by `DailyOps_Location_Index`
- Filter keywords in `DailyOps_EWS_FilterKeywords_FormList` (0x005C9B1F) control which enemies can spawn
- `DailyOps_Mode02_IncludeNearby_FormList` (0x005F0CDB) allows nearby world enemies to join the fight

---

## 9. Boss Mechanics

### Default Mutations (Mode 02 Bosses)
From `DailyOps_Mode02:DefaultMutation`:
- **Ignore Armor**: Wave enemies get `DailyOps_Mode02_IgnoreArmorPerk`; Boss gets a separate `DailyOps_Mode02_IgnoreArmorPerk_Boss` (stronger version)
- **Improved Accuracy**: Wave enemies get `DailyOps_Mode02_ImprovedAccuracyPerk`
- **Miniboss Health Buff**: `MiniBossHealthMult = 2.0` -- minibosses get **double health** via ActorValue multiplication, tracked by `DailyOps_Mode02_HealthBuffed_Keyword` to prevent double-application

### Boss Spawning
- Boss uses `Boss` LocationRefType
- Boss sandbox position stored in `BossSandbox`
- Dedicated `BossRespawnPoints_AliasArray` -- two closest respawn points to boss encounter
- All enemies get `AlwaysShowOnCompassKeyword` (always visible on compass)

### Level Normalization
| Parameter | Value | Global |
|-----------|-------|--------|
| Creature Min Level | 40 | `Renorm_MinLVL_Creatures_DailyOps` |
| Creature Max Level | 60 | `Renorm_MaxLVL_Creatures_DailyOps` |
| Creature Level Offset | 0 | `Renorm_Offset_Creatures_DailyOps` |
| Boss Min Level | 40 | `Renorm_MinLVL_Bosses_DailyOps` |
| Boss Max Level | 100 | `Renorm_MaxLVL_Bosses_DailyOps` |
| Boss Level Offset | 0 | `Renorm_Offset_Bosses_DailyOps` |

**Key finding**: Regular enemies cap at level 60 but bosses scale up to **level 100**. Both floor at level 40 with zero offset. This means the boss difficulty gap is real and significant -- bosses can be 40 levels higher than regular enemies.

---

## 10. High Elder Mode (Hard Mode)

From `DailyOps_All:HighElderMode`:

- Toggled by `DailyOps_HighElder_Mode_Index` (0x0060A2BC) -- set by Live Content Pipeline
- **Time limit**: `DailyOps_HighElder_TimeLimit` = **360 seconds (6 minutes)**
- Timer ID: 2095
- Failure stages: `ST_MISSION_FAILED = 2100`, `ST_MISSION_FAILED_END = 2200`
- On failure, players get a loot window before ejection
- Objective: `OBJ_HIGH_ELDER_TIME_LIMIT = 2090`

**This is distinct from Elder rank** -- High Elder Mode is a separate hard mode toggle with a strict 6-minute time limit and failure state.

---

## 11. Hidden Modifiers and Bonuses

### Daily Ops Team Bonus
- Spell: `PT_DailyOpsTeamBonus` (0x005D0CD8)
- Perk: `PT_DailyOpsTeamBonusPerk` (0x005D0CD7)
- Effect: `PT_DailyOpsTeamBonusBuff` (0x005D0CD6)
- Conditions check for team size (1, 2, 3, 4 players) with event type 12 and condition 9
- **This is a hidden stat bonus applied to players in a Daily Ops team** -- the conditions suggest it scales with team size

### Uplink Timing Secrets
The uplink times reveal the intended solo vs group experience:
| Configuration | Time to Complete (seconds) | Time (minutes) |
|---------------|---------------------------|-----------------|
| Base time | 300 | 5:00 |
| 1 Player | 150 | 2:30 |
| 2 Players | 130 | 2:10 |
| 3 Players | 110 | 1:50 |
| 4 Players | 90 | 1:30 |
| 0 Players (regress) | 600 | 10:00 |

**Key finding**: With 0 players at the uplink, progress takes 600 seconds (10 minutes effectively = regression). The backup multipliers from ActivatorProgress (2.5x for 4 players, 0.5x for 0 players) are applied on top of these base times -- meaning progress actually REVERSES when nobody stands on the uplink.

### Eject Timer
- `DailyOps_EjectTimer` = **300 seconds** (5 minutes) -- players have 5 minutes to loot after mission complete before forced ejection

### Post-Match Cleanup
- From `DailyOps_All:PostMatchCleanup`: After mission complete + eject timer, remaining enemies are killed via `DailyOps_Cleanup_Spell` which triggers `DailyOps_All:CleanupEffect` -- enemies spontaneously dismember (Torso dismember + explosion VFX)

### Mutated Public Events Integration
- The mutation system is shared between Daily Ops and Mutated Public Events
- `EventMutationScript` extends `QuestInstance` and uses the SAME mutation FormLists
- Each public event can block specific mutations via `BlockedListOfMutationsForThisEvent` (index array)
- Double mutations also blockable via `BlockedListOfDoubleMutationsForThisEvent`
- Mutated events use LCP globals `LCP_MutationEnabled` and `LCP_DoubleMutationEnabled` per-event
- MPE exclusion keywords: `MPE_NotResilient`, `MPE_NotCamo`, `MPE_NotSwiftFooted`

### Vernon Dodge Misc Quest
- `DailyOps_VernonDodge_Misc_Live_Global` (0x005D1EDF) = 1 -- Vernon Dodge has a relationship-gated misc quest tied to Daily Ops
- Requires `AV_VernonRelationship` >= 2 to trigger
- Quest: `DailyOps_VernonDodge_Misc` (0x005CF0C7)

### Invaders from Beyond Integration
- `LCP_E07B_Invaders_DailyOps` (0x00635F95) -- the Invaders from Beyond event can use Daily Ops as a delivery mechanism
- Cut reward list: `zzz_DailyOps_InvadersFromBeyond_LLS_Event_Reward_Rare` (0x00620E81)

### Drifter Keycard Chance
- `P62_LCP_TheDrifter_KeycardChance_DailyOps` (0x008278F2) -- The Drifter character has a special keycard drop chance modifier specific to Daily Ops

### SCORE Challenges
- `SCORE_Daily_DailyOps` (0x005D22E0) -- daily SCORE for completing a Daily Op
- `SCORE_Weekly_DailyOps` (0x005D22E1) -- weekly SCORE for completing Daily Ops

---

## 12. Summary of Key Hidden Mechanics

1. **Uplink progress reverses with 0 players** -- the 0.5x backup multiplier against 600s base time means progress actively goes backward, not just pauses
2. **Reflective Skin has staggered activation** -- enemies don't all reflect simultaneously; each has a random delay timer after spawn up to MaxDelayTime seconds
3. **Freezing Touch is a 4-stage progressive system** -- Normal > Chilled > Frosted > Frozen, not a binary freeze. Not being hit causes regression through stages
4. **Toxic Blood has 3 damage tiers** -- the hazard scales up, not a flat amount
5. **Double mutations give bonus currency** -- Elder rank in double mutation ops gets a second currency roll
6. **Boss enemies scale to level 100 while regular enemies cap at 60** -- a hidden 40-level gap
7. **Mode 02 bosses inherently ignore armor AND have improved accuracy** -- these are default mutations applied on top of the daily mutation
8. **Minibosses get exactly 2x health** -- a hard multiplier, not a range
9. **Ambient enemies get dynamically promoted to minions/guards** based on 900-unit proximity and >90% health requirement
10. **High Elder Mode exists as a separate hard mode with 6-minute time limit** -- distinct from Elder completion rank
11. **The Daily Ops team bonus perk is a hidden scaling buff** based on team size
12. **LastStand was a fully implemented mutation that was cut** -- would have made low-health enemies more dangerous
13. **Bethesda originally planned a unique Super Mutant Boss skin for Daily Ops** -- deleted along with Scorched boss outfits and specialized boss weapons
