# Fallout 76 AI Behavior & Package System — Complete Extraction

## Data Sources
- `full_esm_dump.txt` (1,608,058 lines)
- `NPC__records.txt` (26,615 NPC records)
- `scripts_decompiled/` (7,095 scripts, 207 PF_ package fragments)
- **2,737 PACK records** (AI packages)
- **196 CSTY records** (combat styles)

---

## 1. Every AI Package Type

The Creation Engine AI system is built on **AI Packages** — behavioral instructions assigned to NPCs in a priority stack. FO76 contains **2,737 unique package records** categorized by behavior type:

### Package Type Distribution (keyword frequency across all 2,737 packages)

| Type | Count | Purpose |
|------|-------|---------|
| **Travel** | 568 | Move to a specific location/marker |
| **Sandbox** | 244 | Wander freely within a radius |
| **Sit** | 228 | Use furniture (chairs, benches, consoles) |
| **Stay** | 205 | Hold position at current location or linked ref |
| **Combat** | 120 | Combat override packages (engage, ignore, brawl) |
| **Patrol** | 96 | Walk between patrol markers |
| **Follow** | 84 | Follow another actor (player or NPC) |
| **Guard** | 62 | Hold position, attack threats in radius |
| **Eat** | 63 | Use food/drink furniture or objects |
| **Idle** | 53 | Play idle animations at position |
| **Use** | 50 | Interact with specific objects |
| **Wait** | 43 | Wait at position (timed or conditional) |
| **Sleep** | 36 | Use bed furniture during scheduled hours |
| **Flee** | 29 | Run away from combat target |
| **Work** | 29 | Use workbenches/crafting stations |
| **Lean** | 26 | Use wall lean markers |
| **Vendor** | 24 | Stand at vendor post, sell to players |
| **HoldPosition** | 23 | Stay in exact spot, weapons ready |
| **Escort** | 16 | Lead/follow another actor along path |
| **Ambush** | 16 | Wait hidden, then attack |
| **Boss** | 17 | Boss-specific combat behavior |
| **Wander** | 14 | Walk randomly in area |
| **Spawn** | 18 | Post-spawn positioning |
| **Drink** | 4 | Use water sources |
| **Hide** | 4 | Take cover during combat |
| **Search** | 6 | Search for targets |
| **Alert** | 1 | Alert state override |

### Master Packages (Global Behavior Templates)

These define the base behavioral framework that all other packages override:

| Package | FormID | Purpose |
|---------|--------|---------|
| `DefaultMasterPackage` | 0x00042A1C | Standard NPC — allows hellos, combat, idles |
| `DefaultMasterPackageTemplate` | 0x0003F70E | Base template for all masters |
| `DefaultCombatMasterPackage` | 0x00042240 | Combat-focused NPCs |
| `DefaultMasterPackageNoHellos` | 0x003537F2 | Suppresses greeting dialogue |
| `DefaultMasterPackageIgnoreCombat` | 0x003A2947 | NPCs that never fight |
| `DefaultMasterPackageNoObserveCombat` | 0x0022D9EA | Ignores nearby combat |
| `DefaultMasterPackageNoInterrupts` | 0x000FDD5E | Cannot be interrupted by events |
| `DefaultMasterPackageNoCombatAlert` | 0x000E7420 | No combat alert transitions |
| `DefaultMasterPackageNoHellosOrCombat` | 0x0052BE02 | Pure scripted NPCs |
| `DefaultMasterPackage_NoHellosOrObserveCombatInWhitespringBunker` | 0x004F6F76 | Whitespring bunker NPCs |
| `DefaultMasterPackageDailyOps` | 0x005DC208 | Daily Ops enemy behavior |
| `DefaultMasterPackage_WeaponOut` | 0x005C38A3 | Always has weapon drawn |
| `DefaultMasterPackageNoRun` | 0x006536B7 | Walk only |

### Sandbox Radius Variants

Sandbox packages define wander zones by radius (Creation Engine units, ~1 unit = ~1.4 cm):

| Package | Radius | Typical Use |
|---------|--------|-------------|
| `SandboxNearSelf128` | 128 | Tight area, vendor posts |
| `DefaultSandboxLinkedRef512` | 512 | Small room |
| `DefaultSandboxLinkedRef1024` | 1024 | Large room |
| `DefaultSandboxLinkedRef1536` | 1536 | Building floor |
| `CAMPPets_DefaultSandboxCurrentLocation512` | 512 | CAMP pets |

---

## 2. Fight vs. Flee Decision System

FO76 uses a **Confidence-based** system inherited from Creation Engine, with several layers:

### Confidence Actor Value
Each NPC has a Confidence AV (0-4 scale):
- **0 (Cowardly)**: Flees on sight of any enemy
- **1 (Cautious)**: Flees when health drops below threshold or outnumbered
- **2 (Average)**: Standard behavior, fights unless outmatched
- **3 (Brave)**: Rarely flees, fights to near-death
- **4 (Foolhardy)**: Never flees under any circumstances

### Confidence Modifiers (Game Settings)
```
fCombatConfidenceModifierMin = -0.250000  (most they can be discouraged)
fCombatConfidenceModifierMax = 1.000000   (most they can be emboldened)
```

The engine dynamically adjusts confidence based on:
- **Health ratio**: Current HP vs max HP
- **Ally count vs enemy count**: Outnumbered NPCs lose confidence
- **Weapon comparison**: NPCs assess relative threat
- **Group morale**: Ally deaths reduce confidence for faction members

### Flee Distances
```
fFleeDistanceExterior = 5000.0 units (~70 meters)
fFleeDistanceInterior = 3000.0 units (~42 meters)
```

### Combat State Machine
NPCs transition through these states (from `DefaultAliasOnCombatStateChanged`):
```
0: Not In Combat
1: In Combat
2: Searching (target lost)
4: In Combat or Searching (combined check)
```

### Scripted Flee Behavior (`Burn_RE_FleePackageScript`)
The Burning Springs content adds timed flee behavior:
- NPC enters flee package
- Timer runs (default 10 seconds via `TimerDuration`)
- After timer, sets a conditional AV to disable the flee package
- If `DisableIfNoPlayersAround = True`, checks for players within `PlayerCheckRadius` (2048 units)
- If no players within radius, disables the NPC entirely

### Demoralized Combat Style
`csViciousDogDemoralized` (0x00136254) — a dedicated combat style for NPCs whose morale has broken, making them fight ineffectively before fleeing.

---

## 3. Combat Style Records — What Makes Each Creature Fight Differently

FO76 has **196 unique Combat Style records (CSTY)**, each containing sub-records that define:
- **CSGD**: General data (offense/defense multipliers, attack timing)
- **CSME**: Melee parameters (attack distance, stagger chance, power attack frequency)
- **CSRA**: Ranged parameters (accuracy, burst count, fire rate modifiers)
- **CSFL**: Flight/hovering parameters (for Scorchbeasts, Vertibots)
- **CSCR**: Cover/retreat behavior (when to take cover, how long to stay)
- **CSCV**: Close/visual range parameters
- **CSLR**: Long range behavior
- **CSTD**: Teleport data (Mothman, The Drifter — 33 records)
- **CSTG**: Target selection data (62 records)

### Creature-Specific Combat Styles

#### Alpha Predators (Melee-Dominant)
| Style | FormID | Creature | Behavior |
|-------|--------|----------|----------|
| `csDeathClaw` | 0x0004D8AE | Deathclaw | Charges aggressively, uses intimidate AoE explosion, can **gib players** (dismember all body parts randomly) |
| `csYaoGuai` | 0x000B3D84 | Yao Guai | Aggressive melee rusher |
| `csSheepsquatch` | 0x00479D3D | Sheepsquatch | Heavy melee with specials |
| `csMegasloth` | 0x0005303D | Megasloth | Slow but powerful |
| `csRadscorpion` | 0x000636A6 | Radscorpion | Burrowing ambusher |
| `csWendigo` | 0x00015584 | Wendigo | Fast, erratic melee |
| `csMolerat` | 0x0004291C | Mole Rat | Pack swarmer |
| `csSnallygaster` | 0x003B9861 | Snallygaster | Charge + spit attacks |

#### Flyers (Hover/Orbit/Strafe)
| Style | FormID | Behavior |
|-------|--------|----------|
| `csScorchBeast` | 0x002C041A | Full flight combat — sonic attacks, strafing runs, landing attacks, area explosions |
| `csScorchBeastQueen` | 0x00453FA8 | Enhanced version with queen-specific attack data |
| `csScorchBeastNoStrafe` | 0x0043B927 | Grounded variant, no strafe passes |
| `csVertibird` | 0x000F2590 | Military flight patterns |
| `csVertibot` | 0x00526B8B | Automated vertibot patrol |

**Flight Combat Parameters (Game Settings):**
```
fCombatHoverHeightMin = 500.0         (min hover altitude)
fCombatHoverTimeMin/Max               (hover duration range)
fCombatHoverStrafeDistanceMin         (strafe run minimum)
fCombatOrbitDistance = 400.0           (orbit radius around target)
fCombatOrbitTimeMin/Max               (orbit duration)
fCombatFlyingGroundAttackCooldownMin/Max  (landing attack cooldown)
```

#### Scorchbeast Attack System (from `ScorchbeastRaceScript`)
The Scorchbeast has the most complex combat script in the game:

```
AttackData struct per variant (regular vs queen):
- SonicAttackWeapon          (ranged sonic beam)
- StrafeAttackWeapon         (strafing flyby weapon)
- TakeOffAttackExplosion     (AoE when launching into air)
- LandingAttackExplosion     (AoE when landing)
- AreaAttackExplosion        (ground-pound AoE)

Cooldown system:
- Ground sonic: min/max cooldown (separate timers)
- Interior sonic: min/max cooldown (tighter space = different pacing)
- Flying sonic: min/max cooldown (aerial engagement timing)

States: 'flying' and 'ground' — different combat behavior per state
```

#### Robots (Ranged/Tactical)
| Style | FormID | Behavior |
|-------|--------|----------|
| `csProtectron` | 0x000D840C | Slow, methodical ranged |
| `csMrHandy` | 0x000EF218 | Mobile, buzzing attack patterns |
| `csMrGutsy` | 0x00149C9D | Aggressive ranged, will close distance |
| `csAssaultron` | 0x000E1AAF | Melee charge + laser head beam |
| `csAssaultronStealth` | 0x001CFB15 | Stealth variant, ambush predator |
| `csSentryBot` | 0x000B9D66 | Heavy weapons platform |
| `csEyebot` | 0x000A7DA3 | Reconnaissance, light harassment |
| `csEyebotSuicider` | 0x0040F96F | Kamikaze attack |
| `csLiberator` | 0x003E7B67 | Swarm tactics |
| `csLiberatorEasy` | 0x0042FF90 | Reduced threat variant |
| `DLC01csRobobrain` | 0x0010F3A4 | Tactical, uses cover |

#### Humanoid Faction Styles
| Style | FormID | Behavior |
|-------|--------|----------|
| `csRaiderRanged` | 0x0003183B | Standard raider, decent aim |
| `csRaider01Melee` | 0x00047165 | Melee raider, charges |
| `csRaiderRangedOffenseHigh` | 0x00064125 | Aggressive, lower defense |
| `csRaiderRangedDefenseHigh` | 0x00064126 | Takes cover more |
| `csBloodEagleMelee` | 0x00572DBD | Aggressive melee faction |
| `csBloodEagleRanged` | 0x00572DBE | Better aim than basic raiders |
| `csSettlerMelee` | 0x00572DBB | Defensive melee |
| `csSettlerRanged` | 0x00572DBC | Defensive ranged |
| `csCultistMelee` | 0x00572DBA | Cult of the Mothman melee |
| `csCultistRanged` | 0x00572DB9 | Cult ranged |
| `csSupermutantRanged` | 0x000A881F | Inaccurate but persistent |
| `csSupermutantRangedAuto` | 0x0006627E | Full-auto spray |
| `csSuperMutantBerserker` | 0x00130F03 | All-out melee charge |
| `csSuperMutantSuicider` | 0x0044AA13 | Mini-nuke kamikaze |
| `csScorchedMelee` | 0x00194D9D | Scorched melee |
| `csScorchedRanged` | 0x0016CC3C | Scorched ranged |

#### Boss-Specific Styles
| Style | FormID | Boss |
|-------|--------|------|
| `csSMBehemoth` | 0x000E4DD7 | Super Mutant Behemoth |
| `csSMBehemothBoss` | 0x0060A2BA | Behemoth boss variant |
| `csMirelurkQueen` | 0x0010817A | Mirelurk Queen |
| `csWendigoColossus_Melee` | 0x005A1277 | Wendigo Colossus close |
| `csWendigoColossus_Ranged` | 0x0054821D | Wendigo Colossus ranged |
| `csStormBoss` | 0x006F4EBC | Skyline Valley storm boss |
| `csOvergrownBoss` | 0x006C3325 | Overgrown boss |
| `csBossChicken` | 0x00636DD7 | Boss chicken (rad turkey?) |

#### Cryptid-Specific Styles
| Style | FormID | Creature |
|-------|--------|----------|
| `csMothman` | 0x0000EC89 | Mothman — teleport-based combat |
| `csFlatwoodsMonster` | 0x0010CCAE | Flatwoods Monster — teleport + mind control |
| `csGrafton` | 0x00073FA8 | Grafton Monster — oil bomb salvo attacks |
| `csHoneyBeast` | 0x0005F9A9 | Honey Beast — bee swarm summons |
| `csJerseyDevil_Duelling` | 0x006FB700 | Jersey Devil |
| `csBlueDevil` | 0x006A063C | Blue Devil variant |
| `csOgua` | 0x0068F385 | Ogua |
| `csBigfoot` | 0x00868BAB | Bigfoot |

#### The Drifter Combat Styles (Teleportation Scaling)
Unique system with 6 styles controlling teleport frequency:
```
P62_csTheDrifter_TeleportChanceOff   (0x0083C31A) — no teleporting
P62_csTheDrifter_TeleportChanceMin   (0x0082E47F) — rare teleports
P62_csTheDrifter_TeleportChanceLow   (0x0082E47E) — occasional
P62_csTheDrifter_TeleportChanceMid   (0x0082E47D) — moderate
P62_csTheDrifter_TeleportChanceHigh  (0x00802258) — frequent
P62_csTheDrifter_TeleportChanceMax   (0x0082E480) — constant teleporting
```

#### Daily Ops Modified Styles
Daily Ops creates alternate combat styles for enemies:
```
csBloodEagleRanged_DailyOps    — enhanced blood eagle accuracy
csMoleMinerRanged_DailyOps     — enhanced mole miner
csSupermutantRanged_DailyOps   — enhanced super mutant
csCultistRanged_DailyOps       — enhanced cultist
csAssaultron_DailyOps          — enhanced assaultron
csAlienRanged_DailyOps         — enhanced alien
csAlienPoisonRanged_DailyOps   — poison alien variant
csFlatwoodsMonster_DailyOps    — enhanced Flatwoods Monster
```

#### Burn Bounty Combat Archetypes
The Burning Springs bounty system defines tactical roles:
```
csBurnBounty_Default     — balanced fighter
csBurnBounty_Melee       — close-range specialist
csBurnBounty_Ranged      — long-range specialist
csBurnBounty_Sniping     — precision sniper
csBurnBounty_Flanking    — flanking/positioning
csBurnBounty_Stoic       — tank, absorbs damage
csBurnBounty_FireGang    — fire weapon users
csBurnBounty_EnergyGang  — energy weapon users
csBurnBounty_RadGang     — radiation weapon users
csBurnBounty_CryoGang    — cryo weapon users
```

#### Dynamic Combat Style Assignment
The `CreatureCombatStyle` script allows runtime switching between melee and ranged styles:
```papyrus
combatstyle Property MeleeCombatStyle   — used at close range
combatstyle Property RangedCombatStyle  — used at distance
```

The `DLC01BotSetCombatStyle` script dynamically sets combat styles via object mods:
```papyrus
OnEffectStart → akTarget.SetCombatStyle(myCombatStyle)   — mod installed
OnEffectFinish → akTarget.SetCombatStyle(DLC01csWorkbenchBot)  — mod removed
```

---

## 4. NPC Daily Schedules — Time-of-Day Behaviors

FO76 NPCs absolutely have time-of-day schedules. The package naming convention reveals the schedule:

### Anchor Farm (Wastelanders Settlement)
```
W05_AnchorFarm_Hannah_Sandbox_0900_to_2100    — wander farm 9 AM to 9 PM
W05_AnchorFarm_Hannah_Sleep_2100_to_0900      — sleep 9 PM to 9 AM

W05_AnchorFarm_Xavier_Sandbox_0600_to_2200    — wander 6 AM to 10 PM
W05_AnchorFarm_Xavier_Sleep_2200_to_0600      — sleep 10 PM to 6 AM

W05_AnchorFarm_MurrarySandbox_0800_to_2200    — wander 8 AM to 10 PM
W05_AnchorFarm_MurraySleep_2200_to_0600       — sleep 10 PM to 6 AM

W05_AnchorFarm_DanielSandbox_0600_to_2300     — wander 6 AM to 11 PM
W05_AnchorFarm_DanielLunch_1200_to_1300       — eat lunch noon to 1 PM
W05_AnchorFarm_DanielDinner_1900_to_2000      — eat dinner 7 PM to 8 PM
```

Daniel has the most detailed schedule — he sandboxes during the day but takes lunch AND dinner breaks at specific times.

### Foundation (Settler Hub)
```
W05_Foundation_Sleep_10_6         — generic settler sleep (10 PM to 6 AM)
W05_Foundation_SleepBarracks_10_8 — barracks sleep (10 PM to 8 AM)
W05_Foundation_MusicSandbox_8_10  — music area sandbox (8 AM to 10 AM?)
W05_Foundation_Listen_8_10        — listen to music (8 AM to 10 AM)
W05_Foundation_PlayMusicA_8_10    — play instrument A
W05_Foundation_PlayMusicB_8_10    — play instrument B
W05_Foundation_PlayMusicC_8_10    — play instrument C
W05_Foundation_Settler_Eat        — eat at mess hall
W05_Foundation_Settler_Sit        — sit at furniture
W05_Foundation_SandboxNightNoSitLinkedRef1536 — night wander (no sitting)
```

### Crater (Raider Hub)
```
W05_Raider_Sleep1-10PKG_Munch     — Munch sleeps (1 AM to 10 AM)
W05_Raider_SitPKG_Axel            — Axel sits
W05_Raider_SandboxPKG_Barb        — Barb wanders
W05_Raider_SandboxPKG_Fisher      — Fisher wanders
W05_Raider_SandboxPKG_Weasel      — Weasel wanders
W05_Raider_SandboxPKG_Lev         — Lev wanders
W05_Raider_SandboxPKG_Surge       — Surge wanders
W05_Raider_PatrolPKG              — generic raider patrol
W05_Raider_SitScenePKG            — sit during scenes
W05_Raider_SitScenePKGCheer       — sit and cheer during scenes
```

### Named NPC Schedules
```
W05_PaigeSleep_10_6               — Paige (Foundation leader) sleeps 10 PM - 6 AM
W05_LifeNPC_Sleep_9_5             — generic "life NPC" sleeps 9 PM - 5 AM
W05_JoeCreigh_PatrolJog_5_10      — Joe Creigh jog patrols 5 AM - 10 AM
```

### Wayward Tavern
```
W05_Wayward_DuchessSitAndHeadtrack          — Duchess sits at bar, head-tracks players
W05_Wayward_MortSitAndHeadtrack             — Mort sits, head-tracks
W05_Wayward_DuchessSitAtBar_PostQuest       — post-quest position
W05_Wayward_MortSit_PostQuest               — post-quest position
W05_Wayward_JideSandbox_0600_to_2200        — Jide wanders 6 AM - 10 PM
W05_Wayward_GracieSandbox_0400_to_2300      — Gracie wanders 4 AM - 11 PM
```

### Burning Springs
```
BURN_Billie_SitPackage                      — Billie sits
BURN_SQ02_PCKGE_StayAtSelf_LoanShark        — Loan Shark holds position
BURN_SQ02_PCKGE_StayAtSelf_Moose            — Moose holds position
BURN_SQ02_PCKGE_StayAtSelf_Leonard           — Leonard holds position
BURN_SQ02_PCKGE_StayAtSelf_Magpie           — Magpie holds position
BURN_SQ02_PCKGE_StayAtSelf_RustKing         — Rust King holds position
BURN_SQ02_PCKGE_StayAtSelf_Eugene           — Eugene holds position
BURN_SQ02_Furn_LoanShark_Chair_OffQuest     — Loan Shark sits when not in quest
BURN_SQ02_PCKGE_Furn_Moose_Lean             — Moose leans against wall
BURN_SQ02_PCKGE_Furn_Leonard_Sit            — Leonard sits
BURN_HWTChemsVendor_Idle                    — Chem vendor idles
BURN_HWTGunVendor_Idle                      — Gun vendor idles
BURN_HWTFoodVendor_Idle                     — Food vendor idles
BURN_HWTGeneralVendor_Idle                  — General vendor idles
```

---

## 5. Vendor NPC Behavior

### Vendor Package Structure
Vendors use `DefaultVendorScript` with properties:
```papyrus
Faction Property VendorFaction    — determines buy/sell inventory
Bool Property SellOnly = False    — sell-only vs two-way trading
```

### What Vendors Do When Not Trading
Based on package analysis, vendor NPCs have layered behavior:

1. **Primary**: Stand at vendor post (StayAtSelf or Sit package)
2. **Idle**: Play vendor-specific idle animations (`BURN_HWTChemsVendor_Idle`, etc.)
3. **Scene**: Participate in ambient dialogue scenes
4. **No-combat zone**: Most vendor NPCs use `IgnoreCombat` master packages — they never fight

### Vendor-Specific Packages
```
Fishing_Fisherman_VendorPackage_NoCombat     — fishing vendor, ignores combat
Fishing_TheCaptain_StayAtLinkedRefPackage_NoCombat — captain stays put
Storm_TradingPost_VendorPackage              — Skyline Valley vendor
Moon_Herd_VendorPackage                      — Moonshine Jamboree vendor
NWOT_Del_VendorPackage / NWOT_Betty_VendorPackage — Night of Terror vendors
BS02_SpecialVendor_Packages_Whitespring_TommyTenToes — Whitespring special vendor
BS02_SpecialVendor_Packages_Whitespring_Minerva      — Minerva's vendor post
COMP_Conversation_WalkToScenePartner_NoHellos_ATHENAVendorPackage — ATHENA vendor
```

### Whitespring Vendor Behavior
```
LC060_WhitespringVendor_Barbershop_BarberTravelPackage — barber travels to station
LC060_WhitespringVendor_DiningRoom_WaiterTravelPackage — waiter travels to tables
```
Whitespring robot vendors have **travel packages** — they move to their stations, unlike most static vendors.

---

## 6. Companion/Ally AI Packages

### Gold Allies (Full Companions) — `CompanionScript`
The most sophisticated AI system in FO76, handling:

**Core Systems:**
- **Radiant Quest Management**: `RadiantQuestData[]` — array of quest definitions with progression tracking
- **Quest Count Tracking**: `COMP_QuestCount` AV synced between player and companion
- **Cooldown System**: `COMP_DailyQuest_NextAllowedDay` — real-time day tracking
- **Location Reservation**: Prevents multiple quests in same location
- **Synced Actor Values**: Player and companion AVs kept in sync (higher value wins)

**Companion Progression:**
```
QuestCountTotal = 16 quests to complete relationship
OutroQuestPlayerQuestCount — triggers finale quest
QuestCount_Rank_Infatuation — romance threshold
PlayerLoves_AV — love status on player
```

**Companion Packages:**
```
COMP_MasterPackage           (0x00598566) — base companion behavior
COMP_RunBackToCamp           (0x00598567) — return to CAMP after distance
COMP_MasterPackage_Solomon   (0x005DC4E8) — Solomon-specific
COMP_RunBackToCamp_Solomon   (0x005D29AF) — Solomon return
```

**Companion-Specific Behavior Examples:**
```
BS01_COMP_Medic_Package_SandboxAtCamp  — Solomon sandboxes at CAMP
COMP_Astronaut_Package_AssaultronReadyForCombat — Emerson's Assaultron ready
COMP_Astronaut_Intro_Package_NPCSitConsole — Sofia sits at console
COMP_Quest_Outro_Beckett_FollowPlayer — Beckett follows during outro
COMP_Quest_Outro_Beckett_StayAtStart — Beckett waits at quest start
COMP_Astronaut_Intro_Package_NPCStandAndHeadtrack — Sofia watches player
```

### Lite Allies (ATX/Seasonal) — `CompanionLiteAllyScript`
Simpler system with just initial quest startup:
```
ATX_COMP_MasterPackage_LiteAlly          — base lite ally behavior
ATX_COMP_MasterPackage_LiteAlly_NONHUMAN — non-human allies
ATX_COMP_RunBackToCamp_LiteAlly          — return to CAMP
ATX_COMP_Package_Mechanic_Sandbox        — mechanic ally sandboxes
ATX_COMP_Ghoul_Package_FireWeaponAtPlayer — ghoul ally shoots at player(!)
```

### Ally Special Functions
- **Chef Ally** (`AllyChefScript`): Casts `Spell_Meal` to restore hunger/thirst, also has vendor faction
- **Medic Ally** (`AllyMedicScript`): Three healing spells (health, rads, disease), charges caps

### CAMP Visitor System (`CompanionVisitorScript`)
Companions attract NPC visitors to the player's CAMP:
```
SpawnChance = 20              — 20% chance per check
PlayerDistanceToSpawnVisitorAt = 10000.0 units
fSpawnMapMinDistanceFromPlayers = 1000.0 units
fSpawnMapMaxDistance = 2300.0 units
fSpawnMapDesiredRangeFromPlayers = 1500.0 units
ExpiryDay = 1.0               — 1 day cooldown
DeleteWhenUnloaded = True      — cleanup
```

Visitors spawn on CAMP outskirts and sandbox around it using `CampVistorToWorkshopLink`.

### CAMP Pets
```
CAMPPets_MasterPackagePlayerInCAMP       — master when player present
CAMPPets_PackageSandboxOnlyPlayerOutsideCAMP — sandbox when player away
CAMPPets_RunBackToCamp                   — return if strayed
CAMPPets_PetTravelToPlayerGiveGift       — bring player a gift
CAMPPets_CatFindUseCatBedPackage         — cat finds cat bed
CAMPPets_CatFindUseCatTreePackage        — cat finds cat tree
CAMPPets_DogFindUseDirtMoundPackage      — dog digs at dirt mound
CAMPPets_DogFindUseHousePackage          — dog uses doghouse
CAMPPets_DefaultSandboxCurrentLocation512 — default wander radius 512
```

---

## 7. MODUS AI Behavior

MODUS (the Whitespring bunker AI) is not a traditional NPC with AI packages. It is implemented as:

### Terminal State Machine (`ENB_ModusRefStateScript`)
MODUS exists as **animated terminal objects** throughout the bunker, each with emotional states:
```papyrus
Function BroadcastSetStateOn()       — activate terminal
Function BroadcastSetStateDEFCON()   — alert/emergency mode
Function BroadcastSetStateAngry()    — hostile emotional state
Function BroadcastSetStateNeutral()  — neutral emotional state
Function BroadcastSetStatePleased()  — pleased emotional state
Function BroadcastSetStateOff()      — deactivate terminal
```

Each terminal instance has:
```papyrus
Bool Property bOnbyDefault = True    — ON by default, or dark until triggered
```

### MODUS Reveal Event (`LC080_MODUSRevealManagerScript`)
A quest-driven event where MODUS reveals itself to the player:
- Server-side RMI calls (`SendRMIToServer`) to check reveal state
- Custom events: `MODUSRevealReset`, `MODUSRevealStart`, `MODUSRevealLoad`
- Tracks completion via ActorValue, Keyword, AND Quest (triple-check system)

### MODUS Sentry Bots (`LC080_MODUSSentryBotScript`)
MODUS controls sentry bots in its chamber:
- `LC080_LinkSetUnconsciousTrigger` — keyword to set bots unconscious
- `LC080_LinkSetConsciousTrigger` — keyword to wake bots up
- MODUS can activate/deactivate its sentries as a defensive mechanism

### MODUS Scene Reset (`MODUS_ResetStateOnSceneEnd`)
After dialogue scenes, MODUS terminals reset to their default state.

### Whitespring Bunker Package
`DefaultMasterPackage_NoHellosOrObserveCombatInWhitespringBunker` — all bunker NPCs ignore combat entirely, creating a "safe zone" feel.

---

## 8. Creature Territorial Behavior — Chase Distance & Leashing

### Leashing / Combat Reset System
FO76 does NOT use explicit "leash distance" values in scripts. Instead, territory is enforced by:

1. **Package Conditions**: Sandbox and guard packages have radius limits. When an NPC reaches its package boundary, the package re-evaluates and pulls the NPC back.

2. **Guard Package Attack Radius**:
```
fGuardPackageAttackRadiusMult = 0.5  (attack radius = 50% of guard radius)
```

3. **Combat Range Limits**:
```
fCombatAbsoluteMaxRangeMult = 4.0   (max engagement range = 4x weapon range)
fCombatAdvanceInnerRadiusMax = 256.0  (inner advance radius)
fCombatAdvanceOuterRadiusMid = 256.0  (mid advance radius)
fCombatAdvanceOuterRadiusMin = 128.0  (min outer advance)
fCombatAdvanceOuterRadiusMax = 512.0  (max outer advance)
```

4. **Health Regeneration on Disengage**:
```
fCreatureOutOfCombatHealthRegenPlayerMinDist = 5000.0 (~70 meters)
fCreatureOutOfCombatHealthRegenDelay = 15.0 seconds
```
When a player is more than 5000 units away AND 15 seconds have passed since combat, creatures begin health regeneration. This is the effective "leash" — creatures chase until the player is ~70m away for 15 seconds.

5. **Epic Creature Health Restore** (`EpicCreatureRestoreHealthEffectScript`):
Boss creatures have a separate health restoration system that triggers regeneration spells when certain conditions are met, with on-screen message notification.

6. **Combat Pathing Teleport** — for creatures that get stuck:
```
fCombatPathingTeleportTimeMax — max time before teleporting back
fCombatPathingTeleportTimeMin — min time before teleporting back
```

### Creature-Specific Territorial Notes

**Scorchbeasts** have extended chase range due to flight — their combat orbits at 400 units radius and hover at 500+ unit altitude mean they can follow targets across significant distances.

**Deathclaws** are purely melee so they charge and chase aggressively but are limited by ground pathing.

**Mothman** uses teleportation to close distance or escape, making traditional "chase" irrelevant — it appears where it wants.

**Flatwoods Monster** similarly teleports, with a dedicated `TeleportOutSpell` for disengagement.

---

## 9. Package Fragment (PF_) Scripts — All 207 Categorized

### Distribution by Quest/System

| Category | Count | Examples |
|----------|-------|---------|
| **Unnamed/Generic** | 11 | `pf__010009b7` through `pf__01003e27` — hex-only names, likely auto-generated |
| **Atlantic City (AC/XPD)** | 28 | Quest stages for Boardwalk content |
| **Wastelanders (W05)** | 42 | Settler/raider quest behaviors |
| **Brotherhood of Steel (BS01/BS02)** | 18 | BoS quest NPC movement |
| **Burning Springs (BURN)** | 6 | Burning Springs quest packages |
| **Storm/Skyline Valley** | 8 | Storm content NPC behavior |
| **Companion (COMP)** | 10 | Companion-specific quest packages |
| **CAMP Pets** | 2 | Pet gift-giving behavior |
| **Events (E05-E09)** | 8 | Event quest NPC positioning |
| **Milestones (MILE)** | 5 | Brahmin travel to encounter points |
| **Random Encounters (RE)** | 6 | Travel and patrol fragments |
| **Misc Quest** | 63+ | Various quest-specific NPC movements |

### What PF_ Scripts Actually Do

Most PF_ scripts are **empty fragment containers** — they declare the script class but contain no code. The actual behavior is defined in the PACK record's data fields (travel targets, conditions, animations). The script exists only to be called by the engine when the package starts/ends/changes.

Non-empty PF_ scripts typically:
1. Set quest stages when package begins/ends
2. Trigger scene transitions
3. Set actor values for conditional logic
4. Enable/disable linked references

---

## 10. NPC Awareness/Detection Ranges

### Detection System (Stealth Points)
FO76 uses a **stealth point** system where NPCs accumulate detection toward sneaking players:

```
fCombatStealthPointSoundThreshold = 25.0   — sound level to trigger alert
fCombatStealthPointRegenMin = 2.0          — minimum regen rate
fCombatStealthPointRegenAlertMult = 50.0   — regen rate while alert
fCombatStealthPointRegenLostMult = 20.0    — regen rate when lost target
fCombatStealthPointRegenHostileMult = 15.0 — regen rate while hostile
```

### Detection Dialogue Timing
```
fCombatDetectionDialogueMinElapsedTime  — min time before "I see you" line
fCombatDetectionDialogueMaxElapsedTime  — max time before line
fCombatDetectionDialogueIdleMinElapsedTime — idle detection timing
fCombatDetectionDialogueIdleMaxElapsedTime
```

### AI Awareness Parameters
```
fAIMinGreetingDistance            — how close before greeting dialogue triggers
fAIDistanceRadiusMinLocation     — minimum location awareness radius
fAISocialRadiusToTriggerConversation          — exterior conversation range
fAISocialRadiusToTriggerConversationInterior  — interior conversation range
fAISocialchanceForConversation                — exterior conversation chance
fAISocialchanceForConversationInterior        — interior conversation chance
fAISocialTimerForConversationsMin/Max         — conversation cooldown
```

### Creature-Specific Detection
Detection ranges are baked into race records and combat styles rather than scripts. Key differentiators:
- **Robots** (Protectrons, Mr. Gutsies): Enhanced detection, lower stealth point gain
- **Feral Ghouls**: Audio-focused detection, react strongly to sound
- **Deathclaws**: Wide detection cone, high aggression once detected
- **Mothman**: Watches silently at distance before engaging or fleeing (sunrise timer at 6 AM)
- **Mole Rats**: Appear from underground, bypassing normal detection

### Sneak Attack Bonuses
```
fCombatDamageBonusSneakingMult   — ranged sneak multiplier
fCombatDamageBonusMeleeSneakingMult — melee sneak multiplier
fCombatSneakAttackBonusMult      — base sneak attack bonus
```

---

## 11. Scorched Coordination — The "Hive Mind"

### Scorched Are NOT a True Hive Mind
Despite the lore about the Scorched Plague creating a connected consciousness, the AI implementation uses **faction-based coordination**, not swarm scripts. There is no dedicated "hivemind" or "swarm AI" script for Scorched.

### How Scorched Coordinate

#### Faction System
All Scorched share a faction (`ScorchedFaction`). The faction relationship system causes:
- Scorched are allies to each other
- Scorched are allies to Scorchbeasts
- When one Scorched enters combat, faction-sharing means nearby Scorched join
- This creates the APPEARANCE of coordinated behavior

#### Scorched Conversion (`ScorchedConversionMagicEffect`)
The plague converts creatures to Scorched variants:
```papyrus
Struct SkinDatum:
  Race CreatureRace    — original race
  Armor skin           — scorched skin overlay
  objectmod OMod       — modification applied

On conversion:
  1. Add to ScorchedFaction
  2. Apply abRaceScorched spell (abilities)
  3. Apply skin and OMod from SkinData array (matched by race)
```

#### Scorchbeast Summon Allies (`ScorchbeastSummonAlliesEffectScript`)
The closest thing to "swarm command":
```papyrus
Bool Property IsAbilityEnabled = True    — can toggle for debugging
Keyword Property SQ_ScorchbeastSummonAlliesStart — triggers story event
```
When a Scorchbeast enters combat, it sends a **story manager event** that spawns Scorched ground troops nearby. This is a spawn event, not a direct command — the spawned Scorched then use normal AI.

#### Scorched Suicider (`ScorchedSuiciderScript`)
Special variant with kamikaze behavior:
```papyrus
Float Property DistanceToExplode     — proximity detonation range
Explosion Property DeathExplosion    — explosion on death

State "explode":
  OnDeath → dismember head, both arms, both legs, both feet
```

#### Festive Legendary Scorched (`festive_legendaryscorched`)
Seasonal variant with modified loot/behavior during holiday events.

### Actual Swarm System — Workshop Attacks (`GQ_SwarmScript`)
The TRUE swarm system exists for **workshop defense events**, not specifically for Scorched:

```papyrus
Struct SwarmWave:
  enemies              — collection of enemies per wave
  rewardPlayers        — players who participated
  delayTime            — seconds before wave spawns
  bSwarmAttackStarted  — wave status
  bSwarmIsDead         — wave cleared
  maxCount / currentCount — wave size

Struct swarmType (from SQ_Master):
  minWaves = 1, maxWaves = 3    — wave count
  bossChance = 0.5               — 50% boss wave
  bossGiantChance = 0.25         — 25% boss is giant variant
  minActorsPerWave = 5
  maxActorsPerWave = 10
  minDeathToTriggerSwarm = 40    — kills needed to trigger swarm
  decrementDeathCountPerPulse = 10 — decay rate
  allowWorkshopTakeover          — can this enemy capture workshop
  allowHorde                     — can turn into horde event
```

Death tracking system: The game counts kills per enemy type across the server. When 40+ of a type die, a swarm event triggers. The count decays by 10 per pulse, so sustained killing is needed.

---

## 12. Settler/Raider Daily Life Packages

### Foundation (Settler) Daily Activities

**Morning Routine (6-8 AM):**
- Settlers wake from barracks (`W05_Foundation_SleepBarracks_10_8`)
- Some wake earlier (`W05_Foundation_Sleep_10_6`)

**Daytime (8 AM - 10 PM):**
- Music performance window (8-10 AM):
  - Three musicians play different instruments (`PlayMusicA/B/C_8_10`)
  - Other settlers listen (`W05_Foundation_Listen_8_10`)
- General sandbox within settlement (`W05_Foundation_SandboxNoSitLinkedRef512/1536`)
- Eating at communal area (`W05_Foundation_Settler_Eat`)
- Sitting at furniture (`W05_Foundation_Settler_Sit`)

**Night (10 PM - 6 AM):**
- Night sandbox with NO sitting (`W05_Foundation_SandboxNightNoSitLinkedRef1536`) — settlers patrol at night instead of sitting
- Sleep in barracks

**Named NPC Schedules:**
- **Paige**: Uses desk furniture during day (`W05_MQS_*_UsePaigeFurn`), travels between locations, sleeps 10 PM - 6 AM
- **Ward**: Sits at designated spot (`W05_DialogueSettler_Ward_SitPackage`)

### Crater (Raider) Daily Activities

**Raider Life:**
- Most raiders have sandbox packages — they wander their areas
- Named raiders have fixed positions:
  - **Meg**: Stays at self (`W05_Raider_StayAtSelfPKG_Meg`)
  - **Mortimer**: Stays at self (`W05_Raider_StayAtSelfPKG_Mortimer`)
  - **Lou**: Stays at self (`W05_Raider_StayAtSelfPKG_Lou`)
  - **Johnny**: Stays at self (`W05_Raider_StayAtSelfPKG_Johnny`)
  - **Gail**: Stays at self, ignores combat, allows idles (`W05_Gail_StayAtSelIgnoreCombatAllowIdle`)
  - **Axel**: Sits (`W05_Raider_SitPKG_Axel`)
  - **Wren/Rocksy**: Stand at designated spots
  - **Barb/Fisher/Weasel/Lev/Surge**: Sandbox within Crater

**Munch is the only raider with a sleep schedule**: `W05_Raider_Sleep1-10PKG_Munch` (1 AM - 10 AM)

**Raider Events:**
- Sitting during scenes (`W05_Raider_SitScenePKG`)
- Cheering during arena fights (`W05_Raider_SitScenePKGCheer`)
- Patrol duty (`W05_Raider_PatrolPKG`)

### Anchor Farm (Detailed Rural Schedule)
The most detailed daily life simulation — each farmer has unique schedules:
- **Hannah**: Farm 9AM-9PM, sleep 9PM-9AM (12-hour days)
- **Xavier**: Farm 6AM-10PM, sleep 10PM-6AM (16-hour days, hard worker)
- **Murray**: Farm 8AM-10PM, sleep 10PM-6AM
- **Daniel**: Farm 6AM-11PM with LUNCH (noon-1PM) and DINNER (7-8PM) breaks — the most human-like schedule

### Wayward Tavern
- **Duchess**: Sits at bar with head-tracking (watches players approach)
- **Mort**: Sits with head-tracking
- **Jide**: Sandboxes 6AM-10PM
- **Gracie**: Sandboxes 4AM-11PM (earliest riser in the game)
- **Bessie** (Brahmin): Has combat override sandbox (`W05_Wayward_BessieSandbox_CombatOverride`)

### Key Insight: Raider vs Settler Design Philosophy
- **Settlers** have MORE varied schedules: sleep, eat, work, play music, sit, patrol at night
- **Raiders** are mostly STATIC: stay at self, sandbox, sit — they "hang around" rather than having structured days
- This is intentional design — raiders are chaotic, settlers are organized

---

## Additional Systems

### Escort AI (`LDActorEscortQuestScript`)
Reusable framework for escort quests:
```
Behavior states:
  BEHAVIOR_CUSTOM     = 0  — custom behavior
  BEHAVIOR_TRANSITION = 1  — moving between states
  BEHAVIOR_PATROL     = 2  — following patrol path
  BEHAVIOR_WAIT       = 3  — waiting for player

Package templates: LDActorEscort_Patrol_Run, LDActorEscort_Patrol_Jog
Death handling: StageToSetOnEscortActorDeath
```

### Mothman Day/Night Cycle (`MothmanCombatantScript`)
Mothman has a **sunrise timer**:
```papyrus
Float sunriseTime = 6.0 Const    — 6 AM
Int sunriseTimerID = 2 Const

State Disappear:
  OnBeginState → PlayIdle(DisappearIdle)  — vanishes with explosion
```
At sunrise (6 AM), Mothman plays disappear animation and removes itself. This is one of the few creatures with hard day/night behavioral changes.

**Mothman Combat Abilities:**
```
AoEAttackWeapon                — area-of-effect attack
InitialAoEAttackTimeMin/Max   — delay before first AoE
AoEAttackDelayTime             — cooldown between AoEs
EnterTeleportExplosion         — explosion when teleporting
DisappearExplosion             — explosion when vanishing
```

### Deathclaw Intimidation System
```papyrus
Animation events: FootLeft, FootRight, Intimidate, GibTarget
Intimidate → places AoE explosion at self (fear/stagger effect)
GibTarget  → grabs player, randomly dismembers body parts:
  - 50% chance per limb to explode OR dismember
  - Checks: Torso, Head, LeftLeg, RightLeg, LeftArm, RightArm
```

### Grafton Monster Oil Bomb Salvo
Complex ranged attack system:
```papyrus
Three launch nodes: BackBubble1, BackBubble2, BackBubble3
SalvoAngle + SalvoAngleVariation     — spread pattern
SalvoDistance + SalvoDistanceVariation — range randomization
InitialSalvoAttackTimeMin/Max         — first salvo delay
SalvoCooldownTimeMin/Max              — between salvos
```

### Honey Beast Bee Swarm (`HoneyBeastBeeSwarmRaceScript`)
Bee swarms are separate actors spawned by the Honey Beast:
```papyrus
AliveTimeMin = 25.0 seconds
AliveTimeMax = 35.0 seconds
HealthPercentMid = 0.7  — visual change at 70% health
HealthPercentLow = 0.4  — visual change at 40% health
AliveTimeoutEnabled = True — swarms auto-disperse
```
Visual progression: `beeSwarmStage1` → `beeSwarmStage2` → `beeSwarmStage3` → `beeSwarmDisperse`

### Whitespring Assault Defense System
```
REWhitespringAssaultPackageDefenderTemplate (0x003CB620)
Conditions:
  - GetInFaction(WhitespringRobotFaction) == 1
  - HasLinkedRef with defense keywords
  - GetDistance(player) > 768.0 units  — only activate when player far enough
```
The Whitespring robots have dedicated assault defense packages that activate when the resort is under attack, with distance conditions preventing them from abandoning their posts unless threats are nearby.

---

## System Architecture Summary

```
┌─────────────────────────────────────────┐
│         MASTER PACKAGE LAYER            │
│  DefaultMasterPackage (base template)   │
│  + IgnoreCombat / NoCombatAlert / etc   │
└──────────────┬──────────────────────────┘
               │ overridden by
┌──────────────▼──────────────────────────┐
│      SCHEDULE PACKAGE LAYER             │
│  Time-of-day conditions:                │
│  Sleep_2200_to_0600                     │
│  Sandbox_0600_to_2200                   │
│  Eat_1200_to_1300                       │
└──────────────┬──────────────────────────┘
               │ overridden by
┌──────────────▼──────────────────────────┐
│      QUEST/EVENT PACKAGE LAYER          │
│  Quest conditions add temporary pkgs:   │
│  FollowPlayer, TravelTo, StayAtSelf     │
│  Scene-specific sit/stand/headtrack     │
└──────────────┬──────────────────────────┘
               │ overridden by
┌──────────────▼──────────────────────────┐
│      COMBAT PACKAGE LAYER               │
│  Combat Style (CSTY) determines:        │
│  - Offense/defense balance              │
│  - Range preference                     │
│  - Special attacks (teleport, fly, AoE) │
│  - Flee threshold                       │
│  Confidence AV determines flee behavior │
└──────────────┬──────────────────────────┘
               │ modified by
┌──────────────▼──────────────────────────┐
│      RACE SCRIPT LAYER                  │
│  Species-specific abilities:            │
│  - Scorchbeast sonic/strafe/land        │
│  - Deathclaw intimidate/gib             │
│  - Mothman teleport/AoE/sunrise vanish  │
│  - Grafton oil bomb salvo               │
│  - Honey Beast bee swarm spawn          │
│  - Flatwoods Monster teleport           │
└─────────────────────────────────────────┘
```

### Key Numbers
- **2,737** total AI packages
- **196** combat styles
- **207** package fragment scripts
- **26,615** NPC records
- **5,000 units** (~70m) flee distance exterior
- **3,000 units** (~42m) flee distance interior
- **5,000 units** creature health regen starts when player this far away
- **15 seconds** delay before health regen begins
- **40 kills** threshold to trigger a swarm event
- **6:00 AM** Mothman sunrise disappearance
- **16 quests** to max companion relationship
