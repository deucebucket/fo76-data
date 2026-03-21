# Finding 016: Nuclear Winter Full Autopsy -- The Complete Babylon Codebase

**Status:** CONFIRMED -- Every system remains intact in the game files
**Data Sources:** NW.esm (28MB, still shipped with game), 3,257 string entries (nw_en.strings), 332 DL string entries (nw_en.dlstrings), 33 decompiled Papyrus scripts referencing "babylon"
**Internal Codename:** Babylon

---

## 1. Architecture Overview

Nuclear Winter was not a mod or addon -- it was a deeply integrated engine-level feature. The code reveals:

- **28 custom native engine functions** added specifically for NW (storm wall rendering, weather transitions, particle effects, map registration, tutorial tracking)
- **A complete quest system** with master/child quest architecture (`DLC01_QP_Babylon_Master` / `DLC01_QP_Babylon_Child`)
- **Separate client and server initializers** (`DLC01_QP_Babylon_Client_Initializer`, `DLC01_QP_Babylon_Staging_Initializer`, `DLC01_QP_Babylon_Enable`)
- **Its own tutorial framework** (`DLC01_Tutorials`, `DLC01_ClientTutorials`) with 19 unique tutorial events
- **NW.esm** remains in the game's Data/ folder at 28MB -- never removed

The entire system is gated by a `quickplaycontext` variable and gamemode keyword system, meaning it could theoretically be reactivated by setting the right server flags.

---

## 2. Storm Zone Mechanics (Full Technical Detail)

### 2.1 Constriction System

From `DLC01_QP_Babylon_Enable`, the storm operates on a phase-based constriction model:

```
Struct ConstrictionPhase
 Float Radius -- target radius for this phase
 curvetable DamageTable -- damage curve (scales with depth in storm)
 Int SafeTimeSeconds -- countdown before constriction begins
 Int ConstrictTimeSeconds -- how long the shrink takes
 Float BufferPctFromPrevRadius -- buffer zone between old and new safe area (0-1)
EndStruct
```

Key findings:
- **Damage is curve-based**, not flat -- the deeper into the storm, the more damage per tick
- **Buffer zones** existed between constriction phases, giving players near the edge slightly more time
- The system used `ConstrictionPhases[]` array, allowing unlimited phase count per map configuration

### 2.2 Storm Wall Visual System

From `DLC01_BabylonClientDataInitializer`, the storm wall was a massive visual effects system:

- **Default storm wall height:** 30,500 game units (approximately 300+ meters)
- **Per-map height overrides** via `StormWallMapInstanceData` structs
- **Fire-based particle effects** with vertex animations simulating a wall of flame:
 - Wave animation (rocking back and forth): WaveFreq=5.0, WaveAmp=0.15
 - Shimmer animation (lateral shimmying): ShimmerFreq=10.0, ShimmerAmp=10.0
 - Gust animation (depth wobble): GustFreq=1.0, GustAmp=30.0
- **Multiple particle layers** could be stacked, each with their own storm level thresholds (MinStormLevel/MaxStormLevel 0-100)
- **Weather transitions** triggered at storm level thresholds -- the weather changed as the storm intensified
- **Separate nuke zone ramp texture** (`NukeWallRampTexture`) -- the storm wall looked different in nuked areas
- **Ash shader system** with 7 texture maps (albedo, normal, specular, noise, burnt albedo, mask, heat ramp)

### 2.3 Storm Audio System

From `DLC01_BabylonStormSounds`:

- Audio updated every **0.1 seconds** based on a `StormLevelAV` actor value (0-100)
- Different sounds triggered at different storm intensity thresholds
- Separate `OnEnterSound` and `OnExitSound` per threshold -- the sound changed depending on whether the storm was getting closer or you were escaping it
- Uses a quicksort algorithm to manage sound event priority

### 2.4 Storm Zone Player Functions

Two native engine functions on the Player class:
- `GetHeadingToStormZoneCenter()` -- returns compass heading toward safe zone
- `IsInsideStormZone(Float extraRadius)` -- checks if player is safely inside, with configurable buffer

---

## 3. Nuclear Winter Loot Terminal System

### 3.1 Terminal Rewards

From `DLC01_BabylonTerminal`, the in-match loot terminals offered 5 reward types with weighted random selection:

| Option ID | Reward | Description |
|-----------|--------|-------------|
| 5 | **Gun** | Random weapon from GunLeveledItem |
| 4 | **Aid Package** | Healing/buff items from AidLeveledItem |
| 3 | **Nuke Code** | Nuclear launch codes from NukeCodeLeveledItem |
| 2 | **Reveal Enemies** | Applied RevealEnemiesOnMapPotion -- showed all enemies on map |
| 1 | **Perk Token** | Random perk card from PerkLeveledItem |

Each option had a configurable weight (`RewardDatum.weight`) and terminals tracked `ChoicesRemainingActorValue` per player, limiting total selections.

### 3.2 Terminal Network Strings

The terminal UI was themed as the "Nuclear Winter Loot Network v1.0.0.76":
- Terminals could be offline ("Please access the network from another terminal")
- Each selection showed a fake packet compression/transmission sequence
- Enemies revealed via map; items delivered to inventory

### 3.3 Loot Distribution

From `DLC01_QP_Babylon_Enable`:
- **Loot density** controlled by `MarkerBabylonLootDensity` markers placed in world
- **Terminal density** -- configurable average distance between enabled terminals (`TerminalsDensity`)
- **Locked container density** -- how many containers stayed locked (`LockedContainersDensity`)
- **Briefcases** (nuke launch item) had min/max spawn counts per map
- **Power Armor** spawns had independent min/max counts
- Loot was organized into `LootGroups` (Container arrays)

---

## 4. NW-Exclusive Weapons and Items

### 4.1 NW-Specific Weapons (from NW.esm strings, 0x42 prefix)

These weapons existed exclusively or in modified form within Nuclear Winter:

| Weapon | Rarity Tiers |
|--------|-------------|
| Cultist Blade | Default, Standard, Standard Epic, Simple, Simple Epic |
| Single Action Revolver | Random, Random Epic |
| Tomahawk | (thrown weapon) |
| **Grognak's Axe** | Default (unique NW variant) |
| Crossbow | Default, Simple, Simple Epic |
| Sickle | Default, Standard, Standard Epic, Simple, Simple Epic |
| Throwing Knife | (thrown weapon) |
| Simple Rifle | Simple, Simple Epic |
| Assaultron Laser | (energy weapon) |
| Tesla | (energy weapon) |
| Cattleprod | Default (NW-exclusive melee) |
| **Gauss Shotgun** | Default (appeared in NW before Adventure mode) |
| **Bow** | Default (appeared in NW before Adventure mode, Wastelanders-era) |
| Explosive Arrows | (ammo type for Bow) |

The rarity tier system (Default/Simple/Standard/Random + Epic variants) was NW-exclusive -- Adventure mode uses legendary stars instead.

### 4.2 NW-Specific Consumables and Effects

| Item | Effect |
|------|--------|
| **Prototype Stealth Boy** | "Invisible for 20 seconds. Attacking disrupts the stealth field." |
| **Grognak magazine** (NW) | "+50% Melee Weapon Damage and Increased Damage Resist for 90 seconds" or "do more armed and unarmed melee damage" for rest of match |
| **Ballistic magazine** (NW) | "do more damage with ballistic guns for 5 minutes" |
| **Fury** (NW variant) | Melee damage buff |
| **BabylonGhostPotion** | Spectator mode potion applied on death |
| **BabylonDispelPotion** | Removed active effects |
| **Babylon Stimpak** | "Revival does not require a stimpak in Nuclear Winter" -- free revives |
| **Nuke Briefcase** | Collectible item to enable nuclear strike |
| **Nuke Codes** | Required alongside briefcase to launch |
| **RevealEnemiesOnMapPotion** | Terminal reward -- showed all enemies on map |

### 4.3 NW-Specific Armor

| Armor | Notes |
|-------|-------|
| Ghillie Marine Torso | NW-exclusive camo variant |
| Ghillie Scout Armor Torso | NW-exclusive camo variant |
| Ghillie Wood Torso | NW-exclusive camo variant |
| Ghillie Suit / Ghillie Suit Hood | Full camo outfit |
| Marine Armor | NW Default variant |
| Scout Armor | NW Default variant |
| Wood Armor | NW Default variant |

### 4.4 NW-Exclusive Cosmetic Rewards

These items were specifically tied to NW progression (Overseer Rank rewards):

| Item | String ID |
|------|-----------|
| Nuclear Winter Beanie | 59000155 |
| Nuclear Winter Letterman Jacket | D9002E3F |
| Hellcat Mercenary Beret | 6100EB38 |
| Pint-Sized Slasher Mask/Costume | 6100012B/012C |
| Gladiator Outfit/Helmet/Mask | 610001D9/01DA/03196 |
| Samurai Outfit | 610001DB |

---

## 5. The ZAX Overseer AI System

### 5.1 Overseer Rank Mechanic

The ZAX AI was the narrator/overseer of Nuclear Winter, voiced with unique VO lines. From the scripts:

**Actor Value:** `Babylon_TotalWins` -- tracked cumulative wins across all matches
**Actor Value:** `Babylon_WinStreak` -- tracked consecutive wins

The Overseer Rank system from `DLC01_BabylonOverseerSecurityClearance`:
- Objects in Vault 51 required a `RequiredClearanceLevel` (a float, based on total wins)
- If player's `Babylon_TotalWins >= RequiredClearanceLevel`, the object activated
- If not, `ShowInsufficientOverseerRankMessage()` was called -- a native engine function
- Objects could play a `ActiveSoundToTrigger` on successful activation
- This gated access to Vault 51 story content

### 5.2 ZAX Voice Lines (VO System)

From `DLC01_QP_Babylon_Master`, the ZAX AI had voiced lines for these events:

| Event | VO Property |
|-------|-------------|
| Player dies (permanently) | `PlayerFatalDeathVO` |
| Player enters match | `PlayerEntryVO` |
| Player enters activity space | `PlayerEnterActivitySpaceVO` |
| Team wins | `TeamWinsVO` |
| Solo player wins | `SoloPlayerWinsVO` |
| Greeting after victory | `GreetingAfterMatchVictoryVO` |
| Enemy killed | `EnemyKilledVO` |
| Enemy squad wiped | `EnemySquadWipedVO` |
| Last squad member alive | `LastSquadMemberVO` |
| Nuke briefcase retrieved | `NukeCaseRetrievedVO` |
| Player outside constriction zone | `OutsideConstrictionVO` |
| Nuke requested/launched | `RequestedNukeVO` |
| Map vote tied | `MapTieVO` |
| Map vote cast | `MapVoteCastedVO` |
| Map finalized | `MapFinalizedVO` |
| **Christmas greeting** | `Babylon_ChristmasGreeting` (seasonal) |

The Christmas greeting string (`420000C4`) confirms seasonal VO was implemented.

---

## 6. Vault 51 Story Content

### 6.1 Location

Vault 51 exists as a named location in the game data (string ID `6100F708`). It served as:
- The pre-match staging area (players spawned in the vault during matchmaking)
- A lore location with progressively unlockable content
- The home of the ZAX AI that administered the "experiment"

### 6.2 The Vault 51 Experiment

The Vault 51 experiment (documented in holotapes and terminal entries within NW.esm) was:
- A vault with no designated Overseer
- ZAX was programmed to select the most capable Overseer through competition
- Over time, ZAX's selection criteria became increasingly violent
- The experiment escalated from democratic elections to gladiatorial combat to full warfare
- ZAX eventually determined that the ultimate test was a battle royale among vault dwellers
- This is the in-lore justification for the Nuclear Winter game mode

### 6.3 Overseer Rank Progression

The Overseer Rank (Vault 51) content was structured as:
- **Progressive access** -- each win unlocked new areas/terminals in Vault 51
- **Security clearance levels** corresponded to total NW wins
- **Terminal entries and holotapes** told the story of Vault 51's descent into chaos
- **Physical areas** within the vault were gated by clearance (doors, terminals, displays)

The ZAX system was designed so that dedicated NW players would gradually uncover the full Vault 51 story through repeated victories.

---

## 7. Nuclear Strike System

### 7.1 Nuke Launch Mechanics

From `DLC01_NukeTargetScript`, the NW nuke system was a complete mini-game:

**Collection:**
- Players found **Nuke Briefcases** in specific loot containers (min/max spawns per map)
- Players also needed **Nuke Codes** (separate items, available from loot terminals)
- Global variable `NukeCodesCount` tracked required code count

**Launch Sequence:**
1. Player activates launch (enters `iNukeStateQueued`)
2. Siren sound plays at blast center (`IncomingNukeSiren`)
3. Warhead reentry sound (`FXProjectileMissileICBMWarheadReentry`) within `WarheadReentryAudioRadius`
4. Incoming nuke visual spawns with animation progress tracking
5. Distant cloud spawns at `fCloudSpawnProgress` (27% of animation)
6. Detonation at `fNukeDropTouchdownProgress` (46% of animation)
7. Explosion, weather transition, blast effects

**Blast Effects:**
- `NukeBlastDistance` -- kill radius for players
- `NukeWeatherDistance` -- radius for weather transition effects
- `WeatherPostNukeBlast` -- special post-nuke weather
- `EN07_ApplyBlastVisualEffectSpell` -- visual damage effect
- `Babylon_ApplyVaporizeVisualEffectSpell` -- **NW-exclusive** vaporize death effect
- `EN07_ApplySoundCategorySpell` -- mutes all audio except nuke sounds
- `MUS76SpecialNuke` -- special nuke music track
- Post-nuke weather persisted for `iNukeWeatherTimerLength` (default: 1500 seconds / 25 minutes)

**Cooldowns:**
- `PlayerLaunchCooldown` actor value prevented spam-launching
- `PlayerLaunchCooldownTime` global set the cooldown duration

### 7.2 Vaporize Effect (NW-Exclusive)

`DLC01_ApplyBabylonVaporizeImod` applied a unique image space modifier when players died to nukes in NW -- a visual "vaporization" effect with configurable delay. This effect does not exist in Adventure mode's nuke system.

---

## 8. Game Mode Infrastructure

### 8.1 Map Voting System

String evidence of a pre-match map voting system:
- `Babylon_MapVotingSelected` -- a map was selected
- `Babylon_MapVotingTimeToVote` -- voting timer
- `Babylon_MapVotingTie` -- tie-breaker logic
- `Babylon_PlayerWins` -- win announcement

Per-map paper map textures were loaded dynamically:
- Default: `textures/interface/babylon/maps/babylon_papermap_morgantown.dds`
- Each map had its own `PerMapTextureData` entry

### 8.2 Known Maps

The default paper map texture path references **Morgantown** (`babylon_papermap_morgantown.dds`), and the client initializer references a military map (`Textures/Interface/Pip-Boy/Military_Map_d.dds`). The `MapInstanceData` array allowed per-map storm wall height and UV customization, confirming multiple map support.

From community knowledge, NW shipped with maps centered on: Flatwoods, Morgantown, Grafton Dam, and potentially others. The infrastructure supported unlimited map additions.

### 8.3 Staging System

From `DLC01_QP_Babylon_Staging_Initializer`:
- **Interior staging cell** -- players waited in Vault 51 during countdown
- **Staging messages** at timed intervals (countdown notifications with sounds)
- **Activity radius** of 55,296 game units (staging version) / 15,000 (enable version)
- **Spawn radius** -- players spawned between `SpawnMinimumRadius` (13,000) and `SpawnRadius` (14,000)
- **Gamemode keyword** system allowed different game mode configurations

### 8.4 AI Enemy Waves

From `DLC01_QP_Babylon_Enable`, NW featured AI creature spawns during matches:

```
Struct AIWave
 Int SpawnTimeSeconds -- when to spawn
 Int NumEncountersToSpawn -- how many encounters per wave
EndStruct

Struct AIEncounter
 ObjectReference Marker -- spawn location (or random in safe area)
 Float MarkerRadius -- spawn radius around marker
 Form Type -- creature type
 LeveledItem LootList -- loot dropped by AI
 Int Count -- number of creatures
 Int MinLevel/MaxLevel -- level range (default: 50)
 Int MinWave/MaxWave -- which waves this encounter can appear in
 Keyword AITier -- low/medium/elite designation
 Bool MarkerCanSpawnInStorm -- if true, can spawn in storm zone
 Bool MustSpawnInSafeZone -- forces spawn in safe area
 Bool UseLargeCreaturePathing -- enables large creature pathing
EndStruct
```

This means creatures could be tiered (low/medium/elite), had configurable loot, and could even spawn inside the storm zone. Large creature pathing support suggests Deathclaws or Scorchbeasts could spawn.

---

## 9. Ghost Mode (Spectator System)

### 9.1 Ghost Potion

When players died in NW, they received `BabylonGhostPotion`:
- Entered spectator/ghost mode
- Could be removed by the player (attacking, picking up items)
- Had a timer that eventually expired
- Separate tutorials for each removal method:
 - `babylon_ghostpotion` -- first time entering ghost mode
 - `babylon_ghostpotion_removed_by_player` -- player broke ghost mode
 - `babylon_ghostpotion_removed_by_timer` -- ghost mode expired

### 9.2 Stimpak/Revive System

From `DLC01_BabylonStimpakIsActiveEffect`:
- NW stimpaks were dispelled on hit (taking damage canceled the heal)
- Reviving teammates was free -- "Revival does not require a stimpak in Nuclear Winter"
- This created a risk/reward dynamic where healing could be interrupted by enemy fire

---

## 10. Tutorial System (19 Unique Events)

The NW tutorial system tracked first-time experiences per player:

| Tutorial Event | Trigger |
|----------------|---------|
| `babylon_firsttime` | First NW match ever |
| `babylon_overseer_unlock` | Second NW match (Vault 51 access) |
| `babylon_spawnmap` | First time seeing spawn map |
| `babylon_storm_approach` | First storm constriction |
| `babylon_safezone_marker` | Entering storm warning zone |
| `babylon_storm_increase` | First time taking storm damage |
| `babylon_hacking` | First terminal hack attempt |
| `babylon_lockpicking` | First lock pick attempt |
| `babylon_camp` | First C.A.M.P. placement |
| `babylon_powerarmor` | First power armor entry |
| `babylon_mutations` | First mutation gained |
| `babylon_revive` | First teammate revive attempt |
| `babylon_winner` | First match victory |
| `babylon_ghostpotion` | First death/ghost mode |
| `babylon_nukebriefcase` | First nuke briefcase pickup |
| `babylon_nukecode` | First nuke code pickup |
| `babylon_stimpacks` | First stimpak pickup |
| `babylon_quickcamp` | First quick camp item (punji trap, turret, guard post) |
| `babylon_bobblemags` | First bobblehead or magazine pickup |
| `babylon_armor` | First armor set pickup |
| `babylon_fav_wheel` | First item pickup (favorites wheel tutorial) |
| `babylon_overseer_increase` | Insufficient overseer rank (first) |
| `babylon_overseer_areas` | Insufficient overseer rank (second+) |
| `babylon_dummy_first_game` | Post-first-game marker |

Tutorial persistence was stored per-player via `SetSeenBabylonTutorial()` / `HasSeenBabylonTutorial()` native functions.

---

## 11. NW Items vs Adventure Mode Equivalents

### 11.1 NW-Exclusive Items (No Adventure Equivalent)

| Item | Type | Notes |
|------|------|-------|
| Nuke Briefcase | Quest Item | NW-only launch item |
| Nuke Codes (NW) | Quest Item | Different from Adventure silo codes |
| RevealEnemiesOnMapPotion | Consumable | Terminal reward, no Adventure equivalent |
| BabylonGhostPotion | Effect | Spectator mode, NW-only |
| Cattleprod | Weapon | NW-exclusive melee weapon |
| Throwing Knife | Weapon | NW-exclusive thrown weapon |
| Tomahawk (NW variant) | Weapon | NW-specific configuration |
| Grognak magazine (NW) | Consumable | Match-length buff, different from Adventure magazines |
| Ballistic magazine (NW) | Consumable | 5-minute damage buff, NW-only |
| Quick Camp items | Deployable | Punji traps, turrets, guard posts as lootable items |
| Babylon_Grenades | Weapon | NW-specific grenade set |
| Ghillie armor torso variants | Armor | Marine/Scout/Wood ghillie camo |

### 11.2 Items That Debuted in NW Before Adventure Mode

| Item | NW Debut | Adventure Mode Arrival |
|------|----------|----------------------|
| Gauss Shotgun | Pre-Wastelanders NW | Wastelanders update |
| Bow | Pre-Wastelanders NW | Wastelanders update |
| Explosive Arrows | Pre-Wastelanders NW | Wastelanders update |

### 11.3 Adventure Items With NW-Specific Modifications

| Item | NW Change |
|------|-----------|
| Prototype Stealth Boy | NW version: 20-second duration, breaks on attack |
| Stimpak | NW version: dispelled on taking damage |
| Fury | NW-specific melee damage buff |
| All weapons | NW rarity tiers (Simple/Standard/Random/Epic) replace legendary system |
| Mutations | "Temporarily recovered" in NW -- mutations cycled differently |

---

## 12. Content That Was Never Activated

### 12.1 Automated Testing Framework

`BabylonTest.psc` reveals a full **automated bot testing system** for NW:
- 12 weapon loadouts with specific form IDs and ammo counts
- Automated fire timers (1.9-2.1 second intervals)
- Automated loot collection (29-31 second intervals, searching for `BabylonBagKeyword`)
- `MoveTowardsCenter()` function that used `GetHeadingToStormZoneCenter()` to navigate
- `IsInsideStormZone(500.0)` checks with avoidance behavior
- `OnShowSpawnPickerEvent()` handler (empty, suggesting spawn picker was in development)

This testing framework suggests Bethesda could run automated NW matches with bot players for stress testing.

### 12.2 FleeBlast Quest

`QF_QP_Babylon_FleeBlast_003A1771` -- an empty quest script fragment suggesting a "flee blast" mechanic was planned but never implemented. This may have been a mechanic where players near a nuke blast would be forcefully pushed away.

### 12.3 Map Voting Tie Logic

The `MapTieVO` voice line and `Babylon_MapVotingTie` string suggest a map voting system with tie-breaking was designed but may not have been fully exposed to players in the shipped version.

### 12.4 Christmas/Seasonal Content

`Babylon_ChristmasGreeting` -- ZAX had seasonal voice lines. The Christmas greeting confirms holiday-themed NW events were planned or implemented.

### 12.5 Overseer Rank Scaling

The `RequiredClearanceLevel` is a float, not an integer, suggesting fractional clearance levels were possible. The system could support extremely granular progression (e.g., 1.5 wins, 2.7 wins) if Bethesda wanted to weight different victory conditions differently.

---

## 13. Could Nuclear Winter Return?

### 13.1 Evidence Supporting Potential Return

1. **NW.esm still ships with the game** -- 28MB of data that Bethesda has never removed, even through major updates including Nuka-World on Tour, The Pitt, Skyline Valley, Gleaming Depths, and The Backwoods
2. **Engine-level integration** -- 28+ native functions for storm walls, weather, map rendering, tutorial tracking, and overseer rank remain compiled into the game engine
3. **Player class retains NW functions** -- `HasSpawnedIntoBabylonGame()`, `IsInsideStormZone()`, `GetHeadingToStormZoneCenter()`, `ShowInsufficientOverseerRankMessage()`, `SetSeenBabylonTutorial()` are all still present
4. **Game class retains NW functions** -- `AddNuclearWinterWeatherTransition()`, `LoadNuclearWinterTextureMaps()`, `SetMapSpecificStormWallData()`, and 15+ `SetStormFX*` functions remain
5. **XP rollover list** -- `Babylon Challenges To Rollover XP List` (string `6200002B`) suggests an XP bridge between NW and Adventure mode was maintained
6. **Gamemode keyword architecture** -- the `GamemodeKeyword` system in staging/enable scripts means NW is just one possible gamemode. New modes could be added using the same infrastructure
7. **The "Connection failed" message** still exists: "You must create a character before playing Nuclear Winter" (string `420000B0`)

### 13.2 Evidence Against Return

1. NW was officially sunset in September 2021 with no public plans for return
2. The server infrastructure for matchmaking 52-player lobbies was decommissioned
3. No new NW content has been added since removal (all NW strings are in legacy ID ranges)
4. The game has shifted focus entirely to PvE content

### 13.3 Assessment

The complete Babylon codebase represents one of the largest intact "dead feature" codebases in any live service game. Every script, every native function, every string, and the entire NW.esm master file remain in the shipping game. Reactivating it would require server-side matchmaking infrastructure but zero client-side code changes. The gamemode keyword architecture even suggests it was designed to be togglable. Whether Bethesda ever intends to flip that switch is a business decision, not a technical limitation.

---

## 14. File Reference

### Scripts (33 files in `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/`)

**Core Systems:**
- `dlc01_qp_babylon_master.psc` -- Master quest with game states (staging/ingame/gameover), VO system, player tracking
- `dlc01_qp_babylon_child.psc` -- Child quest with win/lose stages and objectives
- `dlc01_qp_babylon_enable.psc` -- Map configuration: constriction phases, AI waves, loot density, spawns
- `dlc01_qp_babylon_staging_initializer.psc` -- Pre-match staging with countdown messages
- `dlc01_qp_babylon_client_initializer.psc` -- Client-side map texture registration

**Visual/Audio:**
- `dlc01_babylonclientdatainitializer.psc` -- Storm wall particles, weather transitions, ash shaders, paper maps
- `dlc01_babylonstormsounds.psc` -- Storm audio with threshold-based sound events
- `dlc01_applybabylonvaporizeimod.psc` -- Nuke vaporization image space modifier

**Items/Effects:**
- `dlc01_babylonterminal.psc` -- Loot terminal with 5 reward types and weighted selection
- `dlc01_babyloncontainer.psc` -- NW container open-state management
- `dlc01_babylonghostmodeeffect.psc` -- Ghost/spectator mode
- `dlc01_babylonstealthboyeffect.psc` -- NW stealth boy
- `dlc01_babylondispelpotion.psc` -- Effect removal
- `dlc01_babylonstimpakisactiveeffect.psc` -- Stimpak dispel-on-hit

**Progression:**
- `dlc01_babylonoverseersecurityclearance.psc` -- Vault 51 access gating by win count
- `dlc01_tutorials.psc` -- Server-side tutorial framework (19 events)
- `dlc01_clienttutorials.psc` -- Client-side tutorial with item pickup detection

**Infrastructure:**
- `dlc01_babylondatainitlistener.psc` -- Base listener class
- `dlc01_nuketargetscript.psc` -- Complete nuclear strike system
- `babylontest.psc` -- Automated bot testing with 12 weapon loadouts
- `dlc01_babylon_spawnenemytest.psc` -- Enemy spawn testing

**Quest Fragments:**
- `qf_qp_babylon_master_003c3e3e.psc` -- Empty master quest fragment
- `dlc01_qf_qp_babylon_01000911.psc` -- Empty quest fragment
- `qf_qp_babylon_fleeblast_003a1771.psc` -- Empty "flee blast" quest fragment

### String Files
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/nw_strings_en.txt` -- 3,257 entries
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/nw_dlstrings_en.txt` -- 332 entries

### Master File
- `/home/deucebucket/.steam/steam/steamapps/common/Fallout76/Data/NW.esm` -- 28,170,357 bytes
