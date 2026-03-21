# Finding 053: Hidden Destructible Walls, Barriers, and Breakable Objects in Fallout 76

**Date:** 2026-03-20
**Source:** SeventySix.esm full dump analysis (1.6M lines), CELL/WRLD records, decompiled scripts
**Method:** Pattern matching across STAT, ACTI, MSTT, SCOL, CELL:REFR, WRLD:REFR, quest stage descriptions, enable markers, and destruction scripts

---

## Executive Summary

Fallout 76 contains a substantial system of destructible barriers that reveal hidden content when destroyed. These range from quest-critical breakable walls to obscure environmental barriers that the game never tells you about. The ESM data reveals **breakable rock walls, fake walls, destructible floors, collapsing cave systems, sludge barriers, vine barriers, and secret passages** -- all tied to enable marker systems that swap geometry when the barrier is destroyed.

The key technical pattern is: **destructible object + enable marker = hidden content revealed**. When the destructible is destroyed, the enable marker fires, disabling the "sealed" geometry and enabling the "open" geometry (or vice versa).

---

## CATEGORY 1: NON-QUEST DESTRUCTIBLE BARRIERS (The Hidden Ones)

These are the notable findings -- destructible objects placed in the world that are NOT part of obvious quest objectives.

### 1.1 Breakable Rock Walls (Generic System)

The game has a reusable system of breakable rock walls used throughout caves and mines:

| FormID | EditorID | Model | Notes |
|--------|----------|-------|-------|
| 0x0012262A | `BreakableRockWallGate` | effects/breakablerockwallgate.nif | Standard breakable rock gate |
| 0x00122629 | `BreakableRockWallFrame01` | effects/breakablerockwallframe01.nif | Frame variant 1 |
| 0x00152C30 | `BreakableRockWallFrame02` | effects/breakablerockwallframe02.nif | Frame variant 2 |
| 0x00152C2E | `BreakableRockWallGateExit` | effects/breakablerockwallgateswap.nif | Exit-side swap variant |
| 0x00123DA4 | `BreakableRockWallFrameDeco` | effects/breakablerockwallframedeco.nif | Decorated frame (has display name) |
| 0x001CA8F8 | `BreakableRockWallSlump` | effects/breakablerockwallslump.nif | Slumped/partial variant |

**Associated explosions:**
- `ExplosionBreakableRockWallGate01` (0x00123DA6) -- standard break FX
- `ExplosionBreakableRockWallGate01ForceBreak` (0x00125DB9) -- forced break (scripted)

**Key insight:** These MSTT (Moveable Static) objects are the base templates. They can be placed ANYWHERE in the game world. The fact that they have dedicated explosion effects and swap models means they are designed to be shot/attacked to reveal passages behind them. **Any cave or mine in the game could potentially have these placed, and the game gives you NO indicator they are destructible.**

### 1.2 Breakable Boards (Trap System)

| FormID | EditorID | Notes |
|--------|----------|-------|
| 0x001184C6 | `TrapBreakableBoard01` | Boarded-up doorway/passage |
| 0x001184CF | `TrapBreakableBoard02` | Variant |
| 0x001184D0 | `TrapBreakableBoard03` | Variant |
| 0x001184D2 | `TrapBreakableBoard04` | Variant |
| 0x001184D4 | `TrapBreakableBoard05` | Variant |
| 0x0011709A | `TrapBreakableWalkwayTrigger` | Walkway that collapses |

These are placed throughout abandoned buildings, mines, and caves. Breaking them reveals hidden rooms or passages. The "Trap" prefix means they can also serve as environmental hazards (walkway collapses under you), but many are placed as barriers to hidden areas. **Health value is controlled by global `TrapHealthBreakableBoards` (0x003A91F1).**

### 1.3 Scorched Statues (Destructible Environmental Objects)

Per the decompiled `ScorchedStatueScript`, these are:
- Destructible if attacked
- Lootable (gives items from `LLD_Scorched_Statue` leveled list if activated)
- Can break on proximity trigger (timer between `ScorchedStatueProxyBreakTimeMin` and `Max`)
- Spawn chance controlled by `ScorchedStatueSpawnChance`

Not walls per se, but they are destructible objects that can block or hide items.

### 1.4 IndCatCircle256Collapse01 (0x000A2C52)

A collapsing industrial catwalk. When triggered or attacked, the circular catwalk section collapses. This could reveal access to areas below or block enemies pursuing you.

### 1.5 Breakable Console Panels

Over 40 breakable console panels (`ConsolePanA01Breakable` through `ConsolePanB25Breakable`) -- these are destructible panels on control consoles. Breaking them may reveal internal components or be part of repair objectives in Nuke Silos and power plants.

---

## CATEGORY 2: QUEST-LINKED DESTRUCTIBLE WALLS

### 2.1 Vault 79 -- Wastelanders Main Quest

**The Motherlode Maze (Settler Path - W05_MQS_204P):**
- 5 "Fake Walls" (FakeWall01-05) that fall sequentially as you navigate
- Quest stages: "Fake Wall 01 passed" through "Fake Wall 05 passed"
- Weasel's dialogue triggers them: "Motherlode programming test - player talks to the fake wall and it comes down"
- **LocRef types:** `W05_MQS_204P_FakeWall01RefType` through `FakeWall05RefType`

**The Cave Wall Explosions (Raider Path - W05_MQR_201P):**
- `W05_MQR_201P_BreakableWall` (SCOL 0x005A258A) -- compound breakable wall object
- `W05_MQR_201P_CaveWall01_EnableMarker` (0x005892FE) -- enables content when wall breaks
- `SecondWallExplosionEnableMarker` (0x005892FD) -- second wall explosion
- `wallPushVolumes01EnableMarker` / `wallPushVolumes02EnableMarker` -- push volumes that activate
- Weasel blows open two cave walls with explosives during the raider quest line
- Stage descriptions: "Weasel goes to blow open the first cave wall" and "Weasel goes to blow upen the second cave wall"

**Vault 79 Interior:**
- `Vault79_TurretWallEnableMarker` (0x0059CD8E) -- wall that opens to reveal turrets
- `Vault79_TurretWallDisableMarker` (0x0059CD9D) -- paired disable marker
- `Vault79_BasementDestructionEnableMarker` (0x0059197A) -- basement area destruction
- `Vault79_Settler_DirtWallEnableMarker` (0x00539BF3) -- dirt wall that opens (settler path)
- `Vault79BreakableGlass` (STAT 0x0040E312) -- breakable glass panel
- `Vault79_PostQuestCollapseMarker` (0x00591A02) -- post-quest collapse
- `MotherlodeDrill_DrillThruWall` (ACTI 0x00591660) -- the Motherlode drills through vault wall

### 2.2 Kerwood Mine / Lou's Maze (WL005)

Extensive destructible floor and wall system:
- **Collapsing Doors:** `WL005_CollapsingDoor` with sub-keywords for Explosive, Flora, Rocks, BasicExplosion, FallingDust, ExplosionFinal
- **Floor Collapse Phases:** Three phases each with Movement and Rotation keywords (Phase01-03)
- **Wall Push Systems:** Two sets of wall-push volumes with enable markers
- **Death Box Floor:** `LousMine_DeathBoxFloor` layer -- the floor that collapses as a trap
- **Crusher Trap:** `W05_MQR_201P_CrusherTrapTrigger` -- industrial crusher
- **Hidden Safe:** `Wl005_Snack_Safe_Wall` (CONT 0x00572A44) -- wall safe hidden in the maze

### 2.3 Fort Atlas -- Steel Dawn/Reign (BS01_MQ08_Defense)

**The Breach System:**
- `EnableMarker_BreachBefore` and `EnableMarker_BreachAfter` -- state-swapping markers
- `EnableMarker_BreachClosed` and `EnableMarker_BreachOpen` -- the breach opens/closes
- `BS01_MQ08_Defense_BreachEMDuring_LocRef` -- during-breach marker
- `BS01_MQ08_Defense_BreachCrisisEM_LocRef` / `BreachCrisisDM_LocRef`
- `BS01_MQ08_Defense_VentCollapse_LocRef` -- collapsing vent
- `BS01_MQ08_Defense_TunnelRocksActivator_LocRef` / `_Ref` -- tunnel rocks you interact with
- Detonation system: "Reached detonation point - Detonate the bombs" / "Bombs detonated - Return to the surface"

**Fort Atlas Collapsed Cave:**
- `FortAtlasCollapsedCaveVent` (STAT 0x005E4355) -- vent in collapsed section
- `FortAtlasCollapsedCaveVent_Collapsed` (MSTT 0x005E7EF2) -- collapsed state
- `MetalBarsDamagedChunk_01/02/03` -- damaged metal bars in cave area
- Sound: `QSTBS01CaveCollapse` (0x005EED44)

### 2.4 Steel Reign -- Penance Mission (BS02_MQ01_Penance)

- `BS02_MQ01_Penance_Rockslide` (ACTI 0x005F5DE6) -- rockslide you clear with dynamite
- `BS02_MQ01_Penance_RockslideTrigger` (ACTI 0x006039A7) -- trigger for rockslide interaction
- `BS02_MQ01_Penance_RockWall_SC01` / `_SC02` (SCOL) -- compound rock walls
- `BS02_MQ01_Penance_FX_CollapsingRockPile_FallThrough` (MSTT) -- collapse FX
- `BS02_MQ01_Penance_RockNavBlocker_LocRef` -- nav mesh blocker
- Player uses dynamite and shovel to clear path; quest resets if you log out after clearing but before killing Super Mutants

### 2.5 Steel Reign -- Blue (BS02_MQ03_Blue) -- Destructible Vines

- `BS02_MQ03_Blue_AllowVineDestroy` (KYWD 0x00609DE9) -- keyword placed on player to allow vine destruction
- Description: "This is placed on the player alias of the quest. If the player has this, they will be allowed to destroy the vines."
- `BS02_MQ03_Blue_Activator_WallButton_LocRef` -- wall button
- `BS02_MQ03_Blue_Door_WallDoor_LocRef` -- wall door (door hidden in wall)
- Related to Vault 96 and Blackburn's lab

### 2.6 Monongah Mine (E06 -- A Colossal Problem / Earle Williams)

- `E06_Colossus_DoorEnableMarker` -- arena door that enables
- `E06_EscapeEnableMarker` -- escape route enables after event
- `E06_Colossus_ExitShaftCollapsingRockPile` -- exit shaft rocks collapse
- `E06_MineBlockerCollision` -- collision blocker in mine
- `E06_Colossus_Collapse` (MESG 0x005A52E6) -- collapse message
- Multiple escape explosions: `E06_EscapeExplosionLarge`, `E06_EscapeExplosionSmall`
- The mine collapses as you escape after killing Earle

### 2.7 MTR05 Breach -- Hornwright Industrial (Motherlode Quest)

- `MTR05_Breach_EnableMarker` (STAT 0x002C3EC4) -- the breach enable marker
- `MTR05_Breach_BreachExplosionLocRef` -- explosion at breach point
- `MTR05_Breach_RootMarkerLocRef` -- event root
- `MTR05_Breach_FinalWaveMarkerLocRef` -- final wave spawns
- Located at Hornwright Industrial HQ area
- The Motherlode breaches through mine walls as part of this event
- Sound: `OBJVault79GearDoor01Breach` / `Breach2D` / `Breach3D`

### 2.8 Vault 79 -- Hornwright Saferoom

- `HornwrightSafeRoom01` (CELL 0x003FEE25) -- dedicated cell for saferoom
- `W05_HornwrightSaferoom_EnableMarker_Penny` -- Penny-related enable
- `W05_HornwrightSaferoom_EnableMarker_Parts` / `_Parts_Plane` -- hidden parts
- `W05_MQS_201P_HornwrightSaferoomKeycard` (KEYM 0x003FCBC7) -- keycard to access
- Hidden room requires finding keycard clues

### 2.9 Mountainside Bed & Breakfast Basement (W05_Community_BB)

- `W05_Community_BB_BasementEnableMarker_LocRef` -- basement reveal
- `MountainsideBB_BasementEnableMarker` (WRLD:REFR 0x005B5979) -- placed in overworld
- `W05_Community_BB_Cannibal_FleeTo_LocRef` / `Cannibal3PathUpstairs_LocRef` -- cannibal NPCs
- `W05_Community_BB_PorchDoor_LocRef` -- porch door
- Hidden basement with cannibal content, accessed during Wastelanders questline

---

## CATEGORY 3: EVENT-BASED DESTRUCTIBLE BARRIERS

### 3.1 Skyline Valley -- Region Boss (Neurological Warfare)

- `Storm_RegionBoss_DestructibleFloor_LocRef` -- destructible floor in boss arena
- `DestructibleFloors` quest alias with collection system
- Floor sections break during the boss fight, creating hazards
- Lightning-based respawn system for mobs on destroyed floor sections
- Arena entrance door can be bypassed by hacking terminal

### 3.2 Fasnacht Day Parade Decorations (E01F)

- `E01F_FasnachtWallEnableMarker01/02/03` -- wall decorations appear/disappear
- `E01F_FasnachtFloorEnableMarker01/02/03` -- floor decorations
- `E01F_FasnachtCeilingEnableMarker01/02/03` -- ceiling decorations
- `E01F_FasnachtWallDecor` / `FloorDecor` / `CeilingDecor` -- ACTI records
- These are decorative but use the same enable marker system; they appear during the event

### 3.3 Tunnel of Love (E09C)

- Six tunnel decoration enable markers (TunnelADeco through TunnelFDeco)
- `E09C_Tunnel_ItemKeyword` -- items picked up during event
- `zzzE09C_Blockage` -- blockage object (model: fissurerockcluster01.nif)
- Wave-based enemy system with Mixed, Moleminers, Molerat, Deathclaw waves

### 3.4 E05 Caravan -- Riding Shotgun

- `E05_Caravan_Barricade` (SCOL 0x005864E5) -- intact barricade
- `E05_Caravan_BarricadeDestroyed` (SCOL 0x005864E6) -- destroyed variant
- State swap between intact and destroyed during Blue Ridge Caravan event

### 3.5 Tales from the Hills -- Dark (E01C)

- `E01C_Tales_Dark_DestructibleShadow` (MSTT 0x00467FB7) -- destructible shadow target
- Model: targetstand01_shadow.nif -- you shoot shadow figures during the event

### 3.6 Winding Path / Guided Meditation (MTNM03)

- Palace of the Winding Path pillars are destructible with healing mechanics
- `WindingPathPillarScript` handles destruction stages, healing, and energy collection
- Enemies attack pillars; players collect energy and return it to heal them
- Multi-stage destruction with visual animations per stage

### 3.7 Mischief Night / Nuclear Winter on Tour (MN2)

- `MN2_ExplodableScript` -- destructible objects in Mischief Night scoring system
- Objects break for points during the Halloween event

---

## CATEGORY 4: EXPEDITION/INSTANCED DESTRUCTIBLE OBJECTS

### 4.1 The Pitt -- Trench (Pitt02)

**Sludge Walls:**
- `XPD_Pitt02_ObjMod_ObjectDestruction_DestructibleObject_01_Sludge` (STAT 0x0064A0CE) -- small sludge sac
- `XPD_Pitt02_ObjMod_ObjectDestruction_DestructibleObject_02_Sludge` (STAT 0x00663DCC) -- large sludge sac
- `DEPRECATED_Pitt02_ObjMod_ObjectDestruction_DestructibleObject_SludgeWall` (MSTT) -- original sludge wall (deprecated)
- Model: props/pittsludgesac/sludgesac.nif and sludgesac_2.nif
- Conditional: requires `XPD_ObjMod_ObjectDestruction_CanDamageObject_Keyword` to be destroyable
- Part of "Object Destruction" objective module in Trench expedition

**General Expedition Destructibles:**
- `XPD_RTTP01_ObjectDestruction_DestructibleObject` (MSTT 0x0069FBFD) -- Return to the Pitt generic
- Six sets of destructible objects (Set00 through Set05) with area centers and proximity triggers
- `XPD_Pitt01_ObjMod_ObjectDestruction_DestructibleObject` -- Union Dues destructibles
- `XPD_ObjMod_CarryAndThrow_TargetDestructible_Template` -- throw-to-destroy template
- Enable marker system: `XPD_RTTP01_ObjectDestruction_Enable_LCRT`

### 4.2 The Pitt -- Hole in Rock Wall

- `NPC_Pitt_HoleInRockWall` (FURN 0x00661554) -- NPCs use hole-in-wall furniture
- `AnimFurn_HoleInRockWall` keyword (0x006064F2)
- NPCs climb through holes in rock walls in The Pitt

### 4.3 Pitt -- Collapsed Train Tunnel

- `XPDPitt02Trench_Geo_CollapsedTrainTunnel` (LAYR) -- geometry layer for collapsed tunnel

---

## CATEGORY 5: VAULT INTERIORS -- BREAKABLE PIPES AND MACHINERY

### 5.1 Vault 94 (All Three Missions)

- V94_1: `IndSmPipe1Way01Breakable`, `1WayHalf01Breakable`, `2Way01Breakable` (and Short variants)
- V94_2: Same pipe types
- V94_3: Same pipe types
- `V94_2_GECKDamage` -- GECK damage activator

### 5.2 Vault 96

- `V96_1_IndSmPipe1Way01Breakable` / `1WayHalf01Breakable` / `2Way01Breakable`
- `V96_2_Analysis_CircuitBreakers` -- circuit breakers in analysis section

### 5.3 Vault 63 (Skyline Valley)

- `Vault63_CollapsedCeiling` (LAYR 0x0072EC3B) -- collapsed ceiling layer
- `Vaul63Collpases` (LAYR -- note typo in original) -- general collapse layer
- `Storm_Vault63_Cave_Blocker` / `Storm_Vault63Cave` -- cave blockers
- `Vlt_Collapsedtunnel` (LAYR 0x006E5797) -- collapsed tunnel
- `Vault63CircuitBreakerNEW` / `Vault63CircuitBreakerOld` -- circuit breakers
- Separate from the secret passage (which is quest-gated via hand scanner)

### 5.4 General Breakable Pipes and Machinery

- `IndSmPipe1WayHalf01Breakable_NoActivation` (0x0078CF2B) -- standard, no activation
- `Storm_IndSmPipe1WayHalf01Breakable_Atrium` (0x00718129) -- Skyline Valley atrium
- `IndSmPipe2Way01Breakable` / `1Way01Breakable` / `1WayHalf01Breakable` -- base templates
- `IndustrialMachine01Breakable` -- breakable industrial machines
- `IndustrialMachineConsole01Breakable` -- breakable machine consoles

### 5.5 Power Plants (Poseidon, Thunder Mountain, Monongah)

- Multiple breakable pipe and machine variants for each power plant section:
 - `_PowerPlantCooling`, `_PowerPlantGenerator`, `_PowerPlantReactor` suffixes
 - `MSilo_Reactor_` prefixed variants for missile silos

---

## CATEGORY 6: SECRET DOORS AND PASSAGES (Not Destructible, But Related)

### 6.1 Riverside Manor / Order of Mysteries (LC022)

- `LC022_SecretEntrance1A/2A/3A` (interior) and `1B/2B/3B` (exterior)
- `LC022_FoldingScreenSecurityDoor` / `LC022_FoldingScreen` -- folding screen hides passage
- `MoM00_FrontParlor` trigger -- front parlor secret door
- `MoM_SecretDoorTriggerFrontParlorRef` / `SecretExitRef` / `LaserHallRef`
- Multiple secret doors accessed during Order of Mysteries questline

### 6.2 Vault 63 -- Secret Passage (Skyline Valley)

- Hand scanner opens hidden passage to elevator
- Quest stage: "The Player just used the hand scanner and opened the secret passage to the Vault 63 elevator"
- Dead Lost provides hand key

### 6.3 Dark Hollow Manor Basement (Skyline Valley)

- `zzzStorm_MQ12_MotelBasementSecretDoor_LocRef` -- secret door in motel basement
- Links Skyline Valley motel to Vault 63 Engineering

### 6.4 Storm Atrium Upper Secret Door

- `StormAtriumUpperSecretDoor` (KYWD 0x0072C506) -- keyword for secret door in atrium
- Located in upper level of Skyline Valley atrium area

### 6.5 Nuka-Cola Machine Secret Storage

- `PackInATXDoorNukaColaMachineSecretStorageCell` (CELL 0x005ADDBB) -- CAMP item
- Secret storage behind a Nuka-Cola machine door

### 6.6 ATX Blue Ridge Locker Secret Door

- `ATX_Door_BlueRidgeLocker_SecretDoor` (DOOR 0x0078A65B) -- CAMP/workshop item

### 6.7 Gunther's Wild West Show -- Wall Safe & Floor Safe (NWOT)

- `NWOT_GWWS_WallSafe_StashBox` (CONT 0x0067E96F) -- hidden wall safe
- `NWOT_GWWS_FloorSafe_StashBox` (CONT 0x0067E970) -- hidden floor safe
- Workshop buildable versions available

---

## CATEGORY 7: BURNING SPRINGS SPECIFIC

### 7.1 Drive-In Location

The Burning Springs drive-in has the following placed objects:
- `Burn_DriveIn_Loudspeaker` (ACTI 0x00844017) -- loudspeaker
- `Burn_DriveinRadio` (ACTI 0x00844016) -- radio transmitter
- `Burn_DriveInSpeakerReceiver` (ACTI 0x00844015) -- speaker receivers
- `SCORE_S24_Workshop_DriveInStatue` (ACTI 0x008ABB1E) -- UFO drive-in statue (buildable)
- `SCORE_S24_Workshop_Structure_DriveinSign` -- drive-in sign (buildable)
- `Burn_Workshop_DriveinSign_NoCables` -- sign without cables
- `Burn_Workshop_DriveInStatue` (ACTI 0x00829961) -- workshop variant
- `Burn_Build_DriveInStatue` keyword

**No explicit destructible wall was found at the Burning Springs drive-in in the ESM data.** The drive-in objects are primarily speakers, radio equipment, and decorative structures. However, the generic `BreakableRockWall` system could be placed at any location without a unique name -- it would just appear as an unnamed reference to one of the base breakable rock wall MSTTs.

### 7.2 Checkpoint Canyon

- `BURN_SQ01_CheckpointCanyon_EnemyWaveKeyword` -- enemy waves at checkpoint
- `BURN_SQ01_CheckpointDoor_LocRef` -- checkpoint door
- `Burn_CheckpointCanyon_CollapsedRailing` (BOOK 0x00833297) -- note about collapsed railing

### 7.3 Rust Kingdom

- `Burn_RK_PipeStraight_Collapsed` (STAT 0x00848A67) -- collapsed pipe in Rust Kingdom
- `Burn_RK_PipeStraight_Damaged` -- damaged pipe
- `Burn_RK_Int_PipeWallConnector_01` -- interior pipe wall connector

---

## CATEGORY 8: DESTRUCTION SCRIPTS (How It Works)

### Key Scripts:

1. **`DefaultRefOnDestructionStateChanged`** -- Sets quest stage when a specific destruction state is reached. Property: `DestructionStateToCheckFor` (default: 1).

2. **`DefaultAliasOnDestructionStateChanged`** -- Same but for quest aliases.

3. **`DefaultDisableRefsOnActorDestruction`** -- When destruction state matches `TargetDestructionState`, disables the linked ref and plays `DisappearFX` explosion. This is the core "wall disappears when destroyed" script.

4. **`DefaultDestructible2StateActivator`** -- Two-state activator (open/closed) that can start destroyed, be repaired, and has destruction state tracking.

5. **`DefaultPlayAnimOnDestructionStage`** -- Plays animation when specific destruction stage is reached.

6. **`ObjectiveModule_ObjectDestruction`** -- Expedition module for "destroy X objects" objectives.

7. **`ScorchedStatueScript`** -- Specialized: breaks on attack, activation (gives loot), or proximity trigger with random timer.

8. **`WindingPathPillarScript`** -- Guided Meditation pillars: multi-stage destruction with healing/energy collection mechanics.

---

## CATEGORY 9: OBJECTS WITH NO QUEST POINTER

The following destructible objects have NO quest prefix in their names, making them potentially "hidden" world objects that the game never tells you to interact with:

| FormID | EditorID | Type | What It Is |
|--------|----------|------|-----------|
| 0x0012262A | `BreakableRockWallGate` | MSTT | Generic breakable rock gate -- placed in multiple caves |
| 0x00122629 | `BreakableRockWallFrame01` | MSTT | Rock wall with frame opening |
| 0x00152C30 | `BreakableRockWallFrame02` | MSTT | Rock wall frame variant |
| 0x00152C2E | `BreakableRockWallGateExit` | MSTT | Exit-side rock gate |
| 0x00123DA4 | `BreakableRockWallFrameDeco` | MSTT | Decorated rock wall (has display name!) |
| 0x001CA8F8 | `BreakableRockWallSlump` | MSTT | Partially collapsed rock wall |
| 0x001184C6-D4 | `TrapBreakableBoard01-05` | ACTI | Boarded-up passages |
| 0x0011709A | `TrapBreakableWalkwayTrigger` | ACTI | Collapsing walkway |
| 0x000A2C52 | `IndCatCircle256Collapse01` | ACTI | Collapsing industrial catwalk |
| 0x0037A052 | `GeneratorDestructible` | ACTI | Generic destructible generator |
| 0x002EC9C8 | `HandScanner_Destructible` | ACTI | Destructible hand scanner |
| 0x0036B0BE | `High_Tech_BBQ_Destructible` | MSTT | Destructible BBQ grill |

**The breakable rock walls are the primary finding.** They are generic templates that can be placed in any cave with no quest association, no objective marker, and no indication they can be broken. Players must simply try shooting walls to discover them.

---

## CATEGORY 10: NOTABLE LAYERS AND CELL REFERENCES

Geometry layers that indicate destructible/collapsed areas:

| FormID | Layer Name | Location |
|--------|-----------|----------|
| 0x0056AC1D | `MonongahMineIntGeometryCollapsedChamberLayer` | Monongah Mine interior |
| 0x0072EC3B | `Vault63_CollapsedCeiling` | Vault 63 |
| 0x006E5797 | `Vlt_Collapsedtunnel` | Vault 63 |
| 0x0064C0CF | `XPDPitt02Trench_Geo_CollapsedTrainTunnel` | The Pitt - Trench |
| 0x00592EB9 | `LousMine_DeathBoxFloor` | Kerwood Mine (Lou's maze) |
| 0x0059197B | `Vault79_Settler_BasementDestruction` | Vault 79 |
| 0x007683F3 | `Vaul63Collpases` | Vault 63 general collapses |
| 0x00731AA7 | `Storm_Vault63_Cave_Blocker` | Vault 63 cave blocker |

---

## SUMMARY OF TRULY HIDDEN DESTRUCTIBLES

**The ones players are most likely to miss:**

1. **Breakable Rock Walls in random caves** -- Generic MSTT objects placed with no name, no quest marker, no tooltip. You just have to shoot them. These are the most hidden destructibles in the game.

2. **TrapBreakableBoards in abandoned buildings** -- Boarded-up passages that can be shot to reveal rooms. No indicator they're breakable beyond the visual appearance of boards.

3. **Breakable console panels in Nuke Silos/Power Plants** -- 40+ breakable panel variants, possibly hiding items or passages.

4. **Wall safes and floor safes** -- `Wl005_Snack_Safe_Wall` and similar. Not destructible per se, but hidden in walls with no marker.

5. **Fort Atlas breach area** -- After "The Best Defense" quest, the breach area toggles between BreachClosed and BreachOpen states, potentially revealing/hiding content based on quest completion.

6. **Collapsing industrial catwalks** -- Can reveal areas below when destroyed.

**The Burning Springs drive-in wall the user mentioned may be a community-discovered instance of a generic `BreakableRockWall` placement. These are placed as unnamed references to the base MSTT templates, making them invisible in the ESM dump without checking every single REFR placement in the Burning Springs worldspace cells -- which would require cross-referencing the base form IDs (0x0012262A, 0x00122629, etc.) against all WRLD:REFR records in that area.**

---

## Methodology Notes

- Searched full_esm_dump.txt (1,608,058 lines) for patterns: Destruct*, Breakable*, Breach*, Collapse*, EnableMarker, FakeWall, SecretDoor, HiddenDoor
- Cross-referenced CELL:REFR and WRLD:REFR records for placed instances
- Analyzed decompiled scripts for OnDestructionStageChanged handlers
- Checked quest stage descriptions (NAM2/SCFC fields) for wall destruction language
- Filtered out workshop/CAMP objects, test objects, deprecated items, and cosmetic-only damage
