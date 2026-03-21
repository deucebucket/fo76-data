# Fallout 76 Event System Deep Dive

**Source**: Decompiled Papyrus scripts, ESM GLOB records, ESM QUST records, encounter wave curve tables
**Date**: 2026-03-20

---

## 1. Event Rotation and Scheduling

The event system is **server-driven via the Live Content Package (LCP) scheduler**, not purely random.

### How It Works

Events are toggled on/off through **GlobalVariable** properties prefixed with `LCP_`. The server sets these globals remotely without requiring a patch. Every significant event has its own LCP toggle:

- `LCP_E07A_Mothman` -- Mothman Equinox seasonal
- `LCP_E07B_Invaders` -- Alien Invaders seasonal
- `LCP_E08A_Moonshine` -- Moonshine Jamboree
- `LCP_E08B_Eviction_Notice` -- Eviction Notice
- `LCP_SSE_BigBloom` -- Big Bloom seasonal
- `LCP_E05_Caravan_Toggle` -- Riding Shotgun
- `LCP_MN2_Mischief` -- Mischief Night
- `MOON_LCP_Toggle` -- Moonshine/Backwoods events
- `MOON_LCP_Toggle_Dailies` -- Backwoods daily quest toggle

The **Fasnacht Master quest** (`CUT_E01F_Fasnacht_Master`) previously used a dedicated quest to enable refs, but the QUST record itself notes:

> "This quest is OBSOLETE. We used it to enable Fasnacht refs before the content scheduler had the ability to do that. Now we use the SetStaticEnabled feature of the content scheduler."

This confirms the LCP system is the centralized method for enabling/disabling all seasonal and rotating content.

### Mutated Events Playlist System

Public events can be **mutated** (applying Daily Ops-style mutation spells to spawned enemies). This is controlled per-event via paired LCP globals:

- `MutatedEvents_LCP_<EventID>_MutationEnabled` -- single mutation toggle
- `MutatedEvents_LCP_<EventID>_DoubleMutationEnabled` -- double mutation toggle
- `MutatedEvents_LCP_LimitedTimeFeature_Playlist` (value: 0.0) -- limited-time featured playlist
- `MutatedEvents_LCP_FeaturedFavoritesPlaylist` / `_V2` / `_DoubleMutation` -- curated rotation lists

The `EventMutationScript` (`mutatedevents:eventmutationscript`) handles this:
- Reads the LCP global to determine if mutation is enabled
- Selects a random mutation from the DailyOps spell/namemod formlists
- Events can **block specific mutations** via `BlockedListOfMutationsForThisEvent` (index array)
- Applies the mutation spell to all spawned actors in the encounter wave

Source: `/scripts_decompiled/eventmutationscript.psc`

---

## 2. Event Cooldown Timers (From GLOB Records)

All values are in **seconds** unless noted:

| Global Variable | Value | Meaning |
|---|---|---|
| `PublicEventsCDTimer` | **720s (12 min)** | Cooldown between public events spawning on a server |
| `PublicEventPrepTimer` | **420s (7 min)** | Standard prep/warning time before event goes active |
| `PublicEventPrepTimer_Short` | **270s (4.5 min)** | Short prep timer variant |
| `PublicEventQuestTimer_10Mins` | **600s (10 min)** | Standard public event quest duration |
| `CB15_DurationTimer` | **1800s (30 min)** | Scorched Earth duration |
| `CB15_ExpireTimer` | **2700s (45 min)** | Scorched Earth expiration (for nuke zone) |
| `E01B_Encryptid_QuestTimer` | **600s (10 min)** | Encryptid event duration |
| `E01B_Encryptid_SpawnTimer` | **30s** | Delay before Sheepsquatch spawns |
| `E01B_Encryptid_KeycardTimer` | **600s (10 min)** | Recall keycard activation timer |
| `E01F_FasnachtQuestTimer` | **1800s (30 min)** | Fasnacht parade event total timer |
| `E01F_FasnachtMarcherTimer` | **900s (15 min)** | Timer for marcher prep phase |
| `E01F_FasnachtStartTimer` | **600s (10 min)** | Fasnacht startup timer |
| `E06_Colossus_EventTimer` | **1800s (30 min)** | Colossal Problem total event timer |
| `E06_Colossus_BossTimer` | **1800s (30 min)** | Wendigo Colossus fight timer |
| `E06_Colossus_DropdownTimer` | **300s (5 min)** | Time before mine shaft collapse sequence |
| `E06_Colossus_EscapeTimer` | **120s (2 min)** | Escape timer after boss dies |
| `E06_Colossus_DetonationTimer` | **20s** | Final detonation countdown |
| `MOON_Ambush_EventTimer` | **1200s (20 min)** | Moonshine Ambush total timer |
| `MOON_Ambush_OguaFight_240Secs` | **240s (4 min)** | Ogua boss fight timer |
| `MOON_Ambush_CargoCollection_300Secs` | **300s (5 min)** | Cargo collection phase |
| `MOON_Ambush_TalkToLucaTimer_300Secs` | **300s (5 min)** | NPC interaction phase |
| `E09C_StartEventTimer` | **300s (5 min)** | Wedding event startup |
| `E09C_EventTimer` | **780s (13 min)** | Wedding event total duration |
| `Storm_E01_MainEventBodyTimer` | **450s (7.5 min)** | Storm boss main event body |
| `Storm_E01_KillBossTimer` | **180s (3 min)** | Storm boss kill phase |
| `Storm_E01_HarvesterRepairTimer` | **240s (4 min)** | Harvester repair phase |
| `BS02_E01_Metal_PublicEventPrepTimer` | **300s (5 min)** | Metal event prep timer |
| `Burn_BountyHunt_PublicExpiryTimer` | **2700s (45 min)** | Backwoods bounty hunt expiry |

### Power Plant Cooldowns (from script)

From `powerplantmasterquestscript.psc`:
- **Success cooldown**: 8.0 hours (`PowerPlantEventSuccessCooldown_Hours`)
- **Failure cooldown**: 5.0 minutes (`PowerPlantEventFailureCooldown_Minutes`)
- **Failed startup cooldown**: 30.0 seconds (`PowerPlantEventFailedStartupCooldown_Seconds`)
- **Late join cutoff**: 20 minutes (`CONST_LateJoinCutoffTime_Minutes`)

---

## 3. Difficulty Scaling Based on Player Count

The Encounter Wave System (EWS) is the core difficulty scaling engine. It uses **curve tables** that map player count to difficulty multipliers.

### Peak Difficulty Multipliers (Location Level Multiplier by Player Count)

From curve tables in `tempest_data/misc/curvetables/json/encounterwave/waveglobals/`:

| Difficulty Setting | Multiplier (flat across all player counts) |
|---|---|
| Very Easy | 1x |
| Easy | 2x |
| Medium | 3x |
| Hard | 4x |
| Very Hard | 5x |

These are **flat multipliers** -- they do NOT scale with player count. The multiplier is applied to the location level to determine the "point buy pool" for spawning enemies.

### What DOES Scale With Player Count

**Max Wave Actors** (`ct_ews_maxwaveactors.json`) -- the maximum living enemies at once:

| Players | Max Actors |
|---|---|
| 0-1 | 5 |
| 2 | 8 |
| 3 | 10 |
| 4+ | 12 |

**Points Per Player Level** (`ct_ews_pointsperplayerlevel.json`) -- diminishing returns per additional player:

| Players | Points Multiplier |
|---|---|
| 1 | 1.0x |
| 2 | 0.5x |
| 3 | 0.3x |
| 4+ | 0.2x |

This means the first player contributes their full level to the budget, the second player adds 50%, third 30%, and fourth+ only 20%. This prevents difficulty from spiraling with large groups.

### Boss Specific -- BoS R01 (Custom Per-Event Curve)

`ct_ews_peakdifficulty_bosr01.json` shows a **player-count-aware** curve:

| Players | Multiplier |
|---|---|
| 0-1 | 3x |
| 2 | 4x |
| 3 | 4.5x |
| 4 | 5x |
| 5 | 5.5x |
| 6-26 | 6x |

This is one of the few events with an actual player-scaling peak difficulty curve.

### Subwave Timing (Seconds Between Enemy Subwaves)

| Speed Setting | Seconds Between Subwaves |
|---|---|
| Very Slow | (not read, likely 120+) |
| Slow | (not read) |
| Medium | 60s (flat) |
| Fast | 30s (flat) |
| Very Fast | (not read) |
| Ultra | (not read) |
| Instant | 0s |

Short timers (when a subwave is killed quickly) follow similar curves.

### Actor Price System

Each enemy type has a "price" that determines how many can spawn within the point buy budget:

| Actor Type | Price at Level 1 | Price at Level 50 | Price at Level 90 |
|---|---|---|---|
| Fodder | 3 | 50 | 90 |
| Normal | 3 | 50 | 90 |
| Boss HTK | 10 | 500 | 900 |
| Scorchbeast Queen | 10 | 500 | 900 |

Bosses and SBQ cost the same -- they are extremely expensive relative to normal enemies, ensuring they spawn alone or with minimal lackeys.

### EWS Configuration Per Event

Each event defines its waves via `DefaultQuestEncounterWaveScript` with these key properties per wave:
- **WaveType**: 0=Endless, 1=Timed, 2=Subwave Duration, 3=Actor Duration
- **Difficulty**: 0-4 (Very Easy to Very Hard)
- **SubwaveTimer_Speed**: 0-6 (Very Slow to Instant)
- **ActorSkew**: -1 to 4 (controls enemy count vs. enemy difficulty tradeoff)
- **BossWave**: boolean, spawns a single boss subwave
- **BossEpicChance**: 0.0-1.0, chance of boss being epic rank (default 0.1 = 10%)
- **BossEpicLevel**: 0-3 (0 = random roll)
- **PeakDifficultyCurve**: per-event override curve table
- **MinNumberOfPlayersOverride**: forces minimum player count for scaling (capped at 6)

Source: `/scripts_decompiled/defaultquestencounterwavescript.psc`

---

## 4. Reward Distribution Mechanics

### How Contribution Works

The `DebugEventScoreScript` reveals the scoring categories used internally:
- **ActivateScore**: 20.0 points (interacting with event objectives)
- **KillScore**: 20.0 points (killing enemies)
- **ReviveScore**: 20.0 points (reviving other players)
- **RepairScore**: 20.0 points (repairing event objects)

The Mischief Night script (`mn2_questscript.psc`) provides the most detailed look at contribution scoring:
- Players have a **PlayerCount multiplier** system (`bEnablePlayerCountMultipliers`)
- An array of `PlayerCount` structs maps player count ranges to score multipliers
- Wearing a **costume with the correct keyword** grants a bonus multiplier via `CostumeBonusMultiplier` (controlled by `LCP_MN2_Bonus` toggle)

### Reward Tiers (Power Plant Example)

Power Plant events have explicit tiered rewards:
- `PowerPlantRewardLevel`: 0 = Minimum (basic repair), 1 = Fully Repaired
- Subsystem repair percentage directly affects reward level
- Subsystem failure threshold: 70% (`CONST_SubsystemFailureThresholdPercent`)

### Fixed Reward Values (From GLOB Records)

| Event | XP Reward | Caps Reward |
|---|---|---|
| Scorched Earth (CB15) | 1,200 XP | 100 caps |
| Wedding Event (E09C) | 200 XP | 50 caps |

### Participation Model

From the `DefaultEventQuest` base script:
- Players are tracked via `AliasEventPlayers` RefCollectionAlias
- You join by entering `ActivityEnterRadius` (default 6000 units) of the CenterMarker
- You leave by exiting `ActivityExitRadius` (default 8000 units)
- Rewards go to all players in the `AliasEventPlayers` collection at completion
- There is **no damage-based contribution requirement** in the base event scripts -- if you are in the event radius at completion, you get rewards

---

## 5. Public Event vs. Activity Distinction (Backwoods Change)

The scripts reveal a clear structural distinction:

### Public Events (Pre-Backwoods Standard)
- Use `DefaultEventQuest` base script with full map notification
- Have `PublicEventPrepTimer` (420s/7min) warning period
- Subject to `PublicEventsCDTimer` (720s/12min) server cooldown
- Appear on all players' maps
- Use the QuickPlay system (`AllowVisitors`, `TargetPlayersPerInstance = 8`)
- Can be mutated via `EventMutationScript`

### Activities (Backwoods Terminology)
- The Backwoods update (`BURN_*` prefix scripts) introduced "Activities" as a separate category
- `SpawnChance_Cnone_ActivityCampTitle` -- CAMP-based activity titles are a separate pool
- Bounty Hunts use `Burn_BountyHunt_PublicExpiryTimer` (2700s = 45 min), much longer than standard events
- Activities have their own LCP toggles (`LCP_BURN_SQ01`, `LCP_BURN_SQ02_OutroP1/P2`, etc.)
- The `Burn_PublicEvent_HelperScript` specifically aids Patch 64 public events, handling a tamed Deathclaw escort with health-based scene triggers (75%, 50%, 25%)

### The Drifter's Keycard Drop System

The Backwoods update also introduced the Drifter keycard system with **per-content-type drop chances**:
- `P62_LCP_TheDrifter_KeycardChance_EventsPublic` -- drop from public events
- `P62_LCP_TheDrifter_KeycardChance_EventsSeasonal` -- drop from seasonal events
- `P62_LCP_TheDrifter_KeycardChance_EventsGeneric` -- drop from generic events
- `P62_LCP_TheDrifter_KeycardChance_DailyOps` -- drop from Daily Ops
- `P62_LCP_TheDrifter_KeycardChance_BlastZonesBoss` -- drop from nuke zone bosses
- `P62_LCP_TheDrifter_KeycardChance_Expeditions` -- drop from Expeditions
- `P62_LCP_TheDrifter_KeycardChance_RAIDS` -- drop from raids

This confirms the game internally classifies content into these distinct categories.

---

## 6. Party Crasher / Boss Spawn Mechanics

### The 33% Confirmed From Script Data

From GLOB records:
- `RA_PartyCrasherSpawnChance_Default` = **0.34 (34%)**
- `RA_PartyCrasherSpawnChance_Bigfoot` = **0.33 (33%)**

These are **close to but not exactly equal**. The standard party crasher has a slightly higher chance than Bigfoot.

### SpawnPartyCrasher Script (`spawnpartycrasher.psc`)

The generic party crasher system uses a struct array:
```
Struct PartyCrashers
 ActorBase CreatureToSpawn -- the creature to spawn
 GlobalVariable SpawnChance -- float 0.0-1.0 representing spawn percentage
 ReferenceAlias SpawnMarker -- where to spawn
 Int EpicRank = 3 -- intended legendary rank (default: 3-star!)
 Sound SpawnSoundEffect -- audio cue on spawn
EndStruct
```

Key properties:
- `questCompleteStage = 9000` -- checked at event completion
- `NearbyPlayerRange = 10000` -- 10,000 unit radius for showing the spawn message
- Party crashers spawn as **3-star legendary by default** (`EpicRank = 3`)
- Uses `SQ_EpicCreatures` quest for legendary assignment

### Bigfoot Party Crasher (`spawnbigfootpartycrasher.psc`)

Bigfoot is a special case party crasher:
- Uses `LvlBigfoot_PartyCrasher` actor base (leveled)
- `NearbyPlayerRange = 12000` (larger notification radius than standard)
- Has dedicated music stinger: `MUSPartyCrashersBigfoot_01Start`
- Dedicated spawn message: `PartyCrasherSpawnMessage_Bigfoot`

### Bigfoot Fight Duration and Despawn (`bigfootpartycrasherdespawn.psc`)

The Bigfoot fight is **timed** and has a full despawn choreography:
- `LCP_RA_BigfootFightDuration` = **300 seconds (5 minutes)**
- **Presentation delay**: 12 seconds after event ends before intro explosion
- **Spawn delay**: 5 seconds after explosion before actor appears
- **Halfway warning**: Message displayed at 50% fight duration
- **Final warning**: `DespawnMessageBuffer = 15` seconds before fight ends
- **Despawn sequence**: Plays `DespawnAnim`, waits `FadeoutTimeDelay` seconds, then fades out with `DespawnExplosion`
- On despawn, actor is set to `NonHostileFaction` to stop combat
- Intro: `RA_BigfootIntroExplosion` + `NPCBigfootIntroRoar`
- Outro: `NPCBigfootOutroRoar` + `DespawnExplosion`

---

## 7. Fasnacht Event Mechanics

### Structure

Quest: `E01F_Fasnacht` (0x0049886E)
Master: `CUT_E01F_Fasnacht_Master` (0x0046F508) -- now uses LCP scheduler
Script: `E01F_FasnachtQuest` extends `QuestInstance`

### Phase Breakdown

**Phase 1 -- Prep (up to 15 min / 900s)**
- 5 Protectron marchers selected from `ProtectronList` array
- Each gets a random parade mask from `ProtectronParadeMasks` array
- Players must find and help each marcher (Baker, Beekeeper, Butcher, Candlemaker, Decorator, Librarian, Musician, Woodsman)
- Decorator task has 4 max decorations (`MaxDecorationCount = 4`)
- Musician task is a **progress bar**: increment of 1.0 per tick, goal of 60.0 total, with 1-second timer intervals

**Phase 2 -- Parade March (3 attack waves)**
- Waves of Super Mutant Suiciders spawn at `SuiciderMarkers` locations
- Spawn count: random between `MinToSpawn` and `MaxToSpawn` per wave
- Wave timing (original): `AttackerTimerMin` to `AttackerTimerMax` seconds between waves
- Wave timing (Patch 52 adjusted): `AttackerTimerMin_P52Adjusted` to `AttackerTimerMax_P52Adjusted` (QoL reduction)
- The `E01F_Fasnacht_DisablePatch52Updates` global can revert to original timing
- Marchers have a Fortify Resistance perk (`E01F_Fasnacht_FortifyResistancePerk`) and speed multiplier spell
- Master of Ceremonies Mr. Handy plays parade music (switches to broken music variant during combat)
- Wave messages displayed: `Wave1Message`, `Wave2Message`, `Wave3Message`

**Phase 3 -- Boss Fight**
- Boss wave selected from `BossWaves` array (multiple possible bosses)
- Each boss wave has a `DisabledVar` global -- allows Bethesda to enable/disable specific bosses remotely
- `ChosenBossWave` index set at runtime (-1 initially)

### Mask Rewards

From `E01F_Fasnacht_BossDropsMasks`:
- Controlled by `FasnachtMaskDropToggle` global (set by Live Content Scheduler)
- When toggle = 1: Boss drops masks from `FasnachtMaskRewards` leveled item list
- Masks are added to the boss's loot pool AND directly awarded to players via `PlayerCollectionAlias`
- The `SurvivingMarchers` global tracks how many marchers survived (affects reward quality)

### Failure Conditions
- `QuestTimerExpiredStage` -- overall 30-minute timer expires
- `MarchersAllDeadStage` -- all parade marchers killed during the march

### Key Timers
- Total event: 1800s (30 min)
- Marcher prep: 900s (15 min)
- Event startup: 600s (10 min)

---

## 8. Scorched Earth / SBQ Fight Mechanics

### Quest Structure

Quest: `CB15_ScorchedEarth` (0x003E271D)
Trigger: Nuke launched at a fissure site
Duration: 1800s (30 minutes)
Expiration: 2700s (45 minutes, for the nuke zone itself)

### Nuke-to-Event Pipeline

From `EN07_FissureQuestScript`:
1. Fissure sites have `EdgeMarkers` defining their boundary
2. When a nuke blast radius overlaps the fissure edges, the fissure "opens"
3. `bBossQuestStarted` flag prevents duplicate boss spawns
4. The fissure quest uses the `RB_Master` (Regional Boss Master) to kick off the boss encounter
5. Scorched waves spawn on timer (`iScorchedWaveTimerID`) with encounter wave index 0
6. Scorchbeast waves spawn on separate timer (`iScorchbeastWaveTimerID`) with encounter wave index 3
7. Wave respawn timer: `EN07_Fissure_RespawnTimerLength` global
8. Unload timer: `EN07_Fissure_UnloadTimerLength` -- how long to wait before turning off wave spawns when area is empty

### SBQ Combat

From `ScorchbeastRaceScript`:
- Uses **two separate attack data sets**: one for regular Scorchbeasts, one for the Queen
- Sonic attack weapon with cooldown timers:
 - Ground: `GroundSonicAttackCooldownTimeMin/Max`
 - Interior: `InteriorSonicAttackCooldownTimeMin/Max`
 - Flying: `FlyingSonicAttackCooldownTimeMin/Max`
- Strafe attack weapon (separate equip slot)
- Landing attack explosion, Takeoff attack explosion, Area attack explosion
- The script tracks flight state (`flying` vs `ground` states)

### SBQ Legendary Chance

From `ScorchbeastRaceScript` LegendaryChance group:
- `ScorchbeastChanceForOneStarLegendary` -- float 0.0-1.0
- `ScorchbeastChanceForTwoStarLegendary` -- float 0.0-1.0
- `ScorchbeastChanceForThreeStarLegendary` -- float 0.0-1.0

These are separate globals (values not in GLOB dump extract, set at runtime).

### Fissure Site Scorchbeast Spawning (Minor Fissures)

From `SQ_FissureSpawnTriggerScript`:
- **Spawn chance**: 10% per player entry (`ChanceToSpawn = 10`)
- **Normal cooldown**: 300s (5 min) between rolls
- **Post-spawn cooldown**: 1200s (20 min) after a successful scorchbeast spawn
- Uses a `coolingdown` state to prevent spam

### Reward
- XP: 1,200
- Caps: 100
- Improved Repair Kit loot: `Econ_ImprovedRepairKitLoot_CB15_ChanceNone` = 0.0 (guaranteed drop)

---

## 9. Encryptid Event Mechanics

### Quest Structure

Quest: `E01B_Encryptid` (0x00454CB6)
Master: `E01B_Encryptid_MasterQuest` (0x00416654)
Trigger: Player uses Assaultron Recall Keycard at terminal
Duration: 600s (10 minutes)

### Activation Sequence

From terminal scripts (`term_e01b_encryptid_recallte_*.psc`):
1. Player interacts with recall terminal
2. `E01B_Encryptid_KeycardTimer` (600s) starts the keycard consumption countdown
3. `E01B_Encryptid_SpawnTimer` (30s) -- delay before the Sheepsquatch (Imposter) spawns
4. `E01B_Encryptid_LockOnTimer` (25s) -- targeting lock-on delay

### The Sheepsquatch Boss

- Referenced as `BossRef` in the quest fragments
- Has a cooldown bool: `E01B_Encryptid_CooldownTimerBool` (prevents re-triggering)
- Quest timer: 600s (10 minutes) to kill the boss

### Related: The Herd (Free Range)

`E01B_Herd` (0x00498662) shares the E01B prefix:
- `E01B_Herd_QuestTimer` = 600s (10 minutes)
- Has its own misc quest: `E01B_Herd_Misc` (0x0047A17E)

---

## 10. Seasonal Event Toggle System

The LCP (Live Content Package) system is the **master toggle** for all seasonal content. Key observations:

### Toggle Architecture

Every seasonal event has at minimum:
- A **main toggle** (`LCP_<EventID>`) -- enables/disables the event entirely
- A **playlist toggle** for mutated variants
- Individual **feature toggles** for sub-systems

### Known Seasonal LCP Toggles

| Global | Purpose |
|---|---|
| `LCP_E07A_Mothman` | Mothman Equinox |
| `LCP_E07A_Mothman_SpecialEncounter_Enabled` | Special encounter within Mothman event |
| `LCP_E07A_Mothman_SpecialEncounter_SpawnChance` | Spawn chance for special encounter |
| `LCP_E07B_Invaders` | Alien Invaders from Beyond |
| `LCP_E07B_Invaders_Week2` | Week 2 variant of Invaders |
| `LCP_E07B_Invaders_DailyOps` | Alien Daily Ops variant |
| `LCP_SSE_BigBloom` | Big Bloom (flower event) |
| `LCP_SSE_BigBloom_EventPlaylist` | BigBloom event playlist |
| `LCP_MN2_Mischief` | Mischief Night |
| `LCP_MN2_Fanfare` / `Explosions` / `Bonus` | Sub-feature toggles |
| `MOON_LCP_Toggle` | Backwoods/Moonshine events |
| `LCP_InternalPlaytestOnly` | Dev-only testing toggle |

### Alien Invasion Takeover System

The `EventTakeoverScript` shows how seasonal events **hijack** regular events:
- Maps regular encounter wave indices to alien alternatives via `WaveIndices` struct
- Changes weather to `Worlds_WeatherNukaQuantumStorm` (Quantum storm)
- Plays `ZetanAudioStinger` alert sound
- Displays `E07B_Invaders_Message_PublicEventInvasion` to players
- Controlled by `LCP_E07B_Invaders` global
- Has special mask drop: `LCP_E07B_Invaders_GeneralZetaGlowMask` with `ChanceNoneDropRate`

Source: `/scripts_decompiled/eventtakeoverscript.psc`

### Spooky/Festive Scorched

Seasonal replacements for regular scorched:
- `Spooky_ScorchedSpawnChance` = value in GLOB (Halloween)
- `Festive_ScorchedSpawnChance` = value in GLOB (Holiday)

---

## 11. Colossal Problem (Wendigo Colossus)

### Event Structure

Quest: `E06_Colossus` (0x00583D14)
Location: Monongah Mine
Trigger: Nuke at specific location

### Timers
- **Event timer**: 1800s (30 min)
- **Boss timer**: 1800s (30 min)
- **Dropdown timer**: 300s (5 min) -- ceiling collapse warning
- **Escape timer**: 120s (2 min) -- escape the mine
- **Detonation timer**: 20s -- final explosion

### Wendigo Colossus Combat (`wendigocolossusracescript.psc`)

**Dual Vomit Attacks**:
- Rad Vomit: Right head (`jnt_R_head`), launches projectile at configurable angle/distance with variation
- Poison Vomit: Left head (`jnt_L_head`), same projectile system

**Summon Allies**:
- Spawns Wendigo allies via separate quest
- Max allies: 4 (`MaxNumberOfAllies`)
- Min allies before re-summon: 2 (`MinNumberOfAllies`)
- Summon timer: `SummonAlliesTime` seconds between summons
- Triggered by `SummonWendigoAllies` animation event

**Combat Style Switching**:
- Alternates between melee-centric and range-centric combat styles
- Timer-based switching: `CombatStyleSwitchTimeMin` to `CombatStyleSwitchTimeMax`

---

## 12. Event Failure Conditions and Timers

### Universal Failure Conditions

From `DefaultEventQuest`:
- **Timer expiration**: Every event has a quest timer; when it expires, the event fails
- **Player departure**: Exceeding `ActivityExitRadius` (default 8000 units) removes player from event
- **Late join cutoff**: `EventStageDisableLateJoin` stage prevents new players from joining mid-event

### Event-Specific Failure Conditions

**Fasnacht**: `MarchersAllDeadStage` -- all 5 parade marchers killed = instant fail

**Power Plant**:
- Subsystem failure at 70% damage (`CONST_SubsystemFailureThresholdPercent = 70`)
- All subsystems can fail independently (Reactor, Generator, Cooling)
- Failure cooldown is only 5 minutes vs. 8-hour success cooldown

**Scorched Earth**: 30-minute timer; SBQ must be killed before timer expires

**Colossal Problem**: 30-minute boss timer, then mine collapses with 2-minute escape timer

**Encryptid**: 10-minute timer to defeat the Imposter Sheepsquatch

**Mischief Night**: Has both timer-based failure and objective-based failure; the `MN2_Mischief_Dialogue` global tracks result:
- 0 = Default
- 1 = Event succeeded recently
- 2 = Event failed recently

### The QuickPlay / Instance System

From `DefaultEventQuest`:
- `TargetPlayersPerInstance = 8` -- if more than 8 players join, the system spins up a new instance
- `CountPlayersAsQuickplayers` -- whether proximity-joined players count as quickplay slots
- `AllowVisitors` -- enables QuickPlay fast-travel joining
- Events use the `quickplaycontext` native type for matchmaking

---

## Summary of Key Findings

1. **Event rotation is NOT random** -- it is server-controlled via the LCP GlobalVariable system. Bethesda can toggle any event, sub-feature, or seasonal content remotely without a patch.

2. **The 12-minute server cooldown** (`PublicEventsCDTimer = 720s`) is the global pacing mechanism between public events.

3. **Difficulty does NOT scale with player count for most events** -- the peak difficulty multiplier is flat. What scales is the **max simultaneous actors** (5 solo to 12 at 4+ players) and the **point buy budget** (with heavy diminishing returns: 2nd player adds 50%, 3rd adds 30%, 4th+ adds 20%).

4. **Party crasher spawn chance is 34% (standard) and 33% (Bigfoot)** -- confirming the community-reported "roughly 1 in 3" figure. They spawn as 3-star legendaries by default.

5. **Reward distribution is participation-based, not contribution-based** at the engine level. Being inside the event radius at completion qualifies you for rewards. Contribution scoring exists (kill, activate, revive, repair) but is used for secondary mechanics like Mischief Night's progress system, not for gating primary rewards.

6. **Fasnacht mask drops are controlled by a live toggle** (`FasnachtMaskDropToggle`) that the LCP scheduler sets, meaning Bethesda can enable/disable rare mask drops per seasonal run.

7. **The Backwoods update formalized the Public Event / Activity / Seasonal distinction** with separate keycard drop chance globals for each category.
