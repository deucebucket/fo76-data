# Fallout 76 Developer Content Deep Dive

**Date**: 2026-03-20
**Sources**: 7,095 decompiled scripts, 158K+ string entries, DL/IL strings, UI strings
**Method**: Systematic search of all debug/test scripts, developer names, hidden tools, and cut content

---

## 1. The Debug.psc Master Script -- Bethesda's God Console

The `debug.psc` script is the crown jewel -- a native API exposing **every debug/cheat function** available to Bethesda developers. These are engine-level functions compiled directly into the game executable.

### Cheat Functions
- `SetGodMode(Bool abGodMode)` -- Invincibility toggle
- `EnableDetection(Bool abEnable)` -- Toggle NPC detection (stealth mode)
- `EnableAI(Bool abEnable)` -- Freeze/unfreeze all AI
- `EnableCollisions(Bool abEnable)` -- Noclip mode
- `EnableMenus(Bool abEnable)` -- Toggle all UI menus
- `QuitGame()` -- Force quit

### Server Console Commands (LEAKED SERVER TOOLS)
- `ExecuteServerConsole(String asCommand)` -- **Execute arbitrary console commands on the server**
- `ExecuteLocalConsole(String asCommand)` -- Execute console commands locally
- `QueueBatchedServerConsoleCommand(String command)` -- Queue multiple server commands
- `ExecuteBatchedServerConsoleCommands()` -- Fire all queued server commands

These functions prove that Bethesda developers could remotely execute console commands on live servers. This is the server admin toolkit that shipped in client scripts.

### Teleportation & Navigation
- `CenterOnCell(String asCellname)` -- Teleport to any cell by name (the `coc` command equivalent)
- `CenterOnCellAndWait(String asCellname)` -- Same but waits for load
- `CenterOnWorldAndWait(String worldName, Int x, Int y)` -- Teleport to world coordinates
- `PlayerGoTo(String asStrKey)` -- Teleport player by string key
- `PlayerMoveToAndWait(String asDestRef)` -- Move to reference and wait
- `GetMapMarkerByIndex(Int index)` -- Get any map marker by index
- `GetNumMapMarkers()` -- Count all map markers
- `DBSendPlayerPosition()` -- Send player position to an external database (telemetry)

### Profiling & Diagnostics
- `StartScriptProfiling(String asScriptName)` / `StopScriptProfiling` -- Profile individual scripts
- `StartStackProfiling()` / `StopStackProfiling()` -- Profile call stacks
- `StartStackRootProfiling(String, ScriptObject)` -- Profile from a root object
- `DumpAliasData(questinstance)` -- Dump all alias data for a quest
- `DumpEventRegistrations(ScriptObject)` -- Show what events a script listens for
- `ShowRefPosition(ObjectReference)` -- Display reference position data
- `FindRandomReferenceWithFormTypeId(ObjectReference, Int, Float)` -- Find random refs by form type

### Version & Platform Info
- `GetVersionNumber()` -- Returns game build version string
- `GetPlatformName()` -- Returns platform name
- `GetConfigName()` -- Returns config name
- `TestAllCells(Int, Int, Int, Int, String)` -- Automated test of ALL game cells

### AutoTest Framework (FULL UNIT TESTING SUITE)
The Debug script contains a complete assertion/testing framework:
- `AutoTestExpectTrue/False` -- Boolean assertions
- `AutoTestExpectEqBool/Int/Float/String/Object` -- Equality checks
- `AutoTestExpectNotEqBool/Int/Float/String/Object` -- Inequality checks
- `AutoTestExpectGreaterInt/Float` -- Greater-than checks
- `AutoTestExpectGreaterEqInt/Float` -- Greater-or-equal checks
- `AutoTestExpectLessInt/Float` -- Less-than checks
- `AutoTestExpectLessEqInt/Float` -- Less-or-equal checks
- `AutoTestComplete(Bool abSuccess)` -- Mark test complete
- `AutoTestLog/AutoTestDebugLog` -- Test logging
- `AutoTestFire()` / `AutoTestFireWeapon()` -- Automated weapon firing
- `AutoTestFireOnTarget(Actor)` -- Fire at specific target
- `AutoTestFaceTarget(Actor)` -- Face a target
- `AutoTestLootContainer(ObjectReference)` -- Auto-loot a container
- `AutoTestGetSelectedRefr()` -- Get currently selected reference
- `AutoTestReadFile(String filename)` -- **Read files from disk** during tests
- `AutoTestRandRangeInt/Float` -- Random values for tests
- `AutoTestGetExecutionDuration()` -- Test timing
- `AutoTestGetExecutionIndex()` -- Which test is running
- `AutoTestGetNormalizedHealth/Level` -- Get normalized actor stats
- `AutoTestGetCurrentWeaponLevel()` -- Current weapon level

### BabylonBot Functions (Nuclear Winter AI Bot)
- `BabylonBotShouldLoot()` -- Should the bot pick up loot?
- `BabylonBotShouldShoot()` -- Should the bot fire weapons?
- `BabylonBotShouldMove()` -- Should the bot navigate?

### Combat Analysis Functions
- `GetNormalizedDamageResistance(Actor)` -- Normalized DR
- `GetNormalizedEnergyResistance(Actor)` -- Normalized ER
- `GetNormalizedFireResistance(Actor)` -- Fire resist
- `GetNormalizedCryoResistance(Actor)` -- Cryo resist
- `GetNormalizedPoisonResistance(Actor)` -- Poison resist
- `GetNormalizedRadiationResistance(Actor)` -- Rad resist
- `GetNormalizedUnarmedDamage(Actor)` -- Unarmed damage
- `GetNormalizedWeaponsDamageForActor(Actor)` -- All weapon damages
- `GetWeaponsInActorInventory(Actor)` -- List all weapons
- `GetInstanceLevelOfPlayerWeapons(Actor)` -- Weapon instance levels

---

## 2. Who is "Steve"? -- DebugSteve Scripts

Steve is almost certainly **Steve M** (referenced as `DebugSteveM` in strings [61004ECB]). The scripts reveal him to be a QA engineer or technical designer who built elaborate bug reproduction/demonstration tools.

### DebugSteveQuestScript.psc
Header: *"Steve's bug-demonstration quest script."*

This is a massive test quest touching nearly every game system:
- **Workshop testing**: PoseidonPlant, WorkshopStateOwned references
- **Nuke silo testing**: MainframeCore, ReactorCatalyst, Keylock keys (Vault 94 content)
- **Biofabricator system**: BiofabricatorButtons, BiofabricatorCreatures, FabricatedCreatureValue, CaptiveFaction
- **Radio scene testing**: RadioScene1, RadioScene2 with toggle
- **Door/terminal testing**: TestSteveCDoor, DebugSteveCTerminalAV
- **EyeBot testing**: DebugSteveCEyebot with DLC01EyebotInteractVFX
- **Destructible testing**: TestDestructible
- **Name/text override testing**: TestNameOverride1/2, TestActivateTextOverride1/2
- **Item spawning**: TestSpawnItemMarker, TestSpawnItemAlias, GiddyupButtercup spawning
- **Radiation hazard testing**: TestSteveCRadiationHazard
- **Corpse Flower testing**: CorpseFlowerRefAlias, CorpseFlowerRight, CorpseFlowerRefCollection
- **Keypad testing**: TestKeypad
- References to Mothman of Mystery content (MoMMaster, MoMCryptosVoiceF_VOICEONLY)

### DebugSteveQuestScript2.psc
Header: *"Steve's bug-demonstration quest script, Part 2!"*
- Equipment testing: TestSteveHat, ClothesSuitDirty_Black
- Temporary quest item testing
- Conditional objective system testing
- References unfilled properties (intentional bug test: `ThisPropertyIsNotFilled`)

### DebugSteveTestObjectScript.psc
Header: *"Steve's test object for bug demonstrations."*
- `TestRMI01(player p)` -- Tests Remote Method Invocation (client-server)
- `TestRMI02(ObjectReference p)` -- Second RMI test
- `TestIMod()` -- Tests Vault 96 Quantum Stabilizer image space modifier
- `TestSoundIssue()` -- Rapid-fire sound play/stop (testing audio bug)
- `RegisterForHitClient()` -- Client-side hit registration testing
- `TraceIsMaleClient(player p)` -- Tests gender detection on client

### Supporting DebugSteve Scripts
- **DebugSteveCActorPackageScript**: Empty event handlers for OnPackageStart/Change/End (package system testing)
- **DebugSteveCDropCrateScript**: Empty OnLoad/OnUnload (load/unload event testing)
- **DebugSteveCTerminalScript**: Terminal with multi-select counter, Whitespring reservation system
- **DebugSteveCTriggerScript**: Empty trigger volume testing

---

## 3. AutoTestClient -- Bethesda's Bot Army (48 Scripts)

A complete automated testing system where AI-driven bots play the game. These are the same bots Bethesda uses for server load testing and QA.

### Bot Navigation & Movement (12 scripts)
| Script | Purpose |
|--------|---------|
| `Common.psc` | Distributes test clients across 24 hardcoded world coordinates |
| `ExploreWorld.psc` | AI bot visits 24 named locations, enters/exits interiors (VTecAG, Sugar Grove, Blackwater Mine, etc.) |
| `NavigateMapMarkers.psc` | Bot pathfinds between all map markers sequentially |
| `MoveInDirection.psc` | Bot walks in a compass heading |
| `MoveInDirectionSoak.psc` | Long-duration directional movement stress test |
| `MoveAndFightInDirection.psc` | Walks and fights anything encountered |
| `MoveInCircles.psc` | Bot walks in circles |
| `MoveInFixedDirectionDistributed.psc` | Multiple bots spread out walking same direction |
| `MoveToInteriorDistributed.psc` | Multiple bots enter interiors simultaneously |
| `PathfindToReference.psc` | Bot pathfinds to specific reference |
| `InteriorExteriorTransition.psc` | Repeatedly enters/exits interior cells |
| `VisitInterior.psc` | Visits specific interior via door FormIDs (4103764/4103721) |

### Combat Testing (7 scripts)
| Script | Purpose |
|--------|---------|
| `GrindMonsters.psc` | Bot hunts monsters: `FindRandomCombatTarget(10000.0)`, pathfinds, fights, loops |
| `SpawnAndKillAI.psc` | Spawns LvlMolerat, equips weapon (FormID 974060), auto-fights |
| `MassCombat.psc` | Orchestrates mass battles: `RatsVBoS()`, `RaidersVSDeathclaw()`, `RobotFight()` |
| `CombatBat.psc` | Simple combat stress test (distribute then wait 180s) |
| `KillAllNPCs.psc` | Iterates all NPC forms (type ID 50), kills them with 3-second delays |
| `DamageTest.psc` | Spawns creatures from file, equips weapons, measures damage per hit and hits-to-kill |
| `SpawnCreaturesAndGetStats.psc` | Spawns creatures, logs all stats: DR, ER, fire/poison/cryo/rad resist, HP, weapon damage |

### Weapon & Equipment Testing (4 scripts)
| Script | Purpose |
|--------|---------|
| `EquipAndFireWeapon.psc` | Cycles through 17 weapons by FormID, equips/fires 150 shots each, validates ammo consumption |
| `EquipAllArmor.psc` | Equips every armor form in the game sequentially |
| `DamageTest.psc` | Per-weapon damage testing against spawned creature targets |
| `GetWeaponStatsInPlayerInventory.psc` | Logs all weapons, damage values, and instance levels in inventory |

### Loot & Economy Testing (2 scripts)
| Script | Purpose |
|--------|---------|
| `GatherLoot.psc` | Bot finds containers/flora within 10,000 unit radius, pathfinds, loots, clears inventory, repeats |
| `SpawnAllItems.psc` | Spawns every item in the game by form type: ARMO, BOOK, INGR, MISC, CNCY, WEAP, AMMO, KEYM, NOTE, PPAK, PACH, LVLI, ARMA, OTFT, COBJ, OMOD |

### Nuclear Winter Bot (1 script)
| Script | Purpose |
|--------|---------|
| `BabylonTest.psc` | **Nuclear Winter AI player bot** -- equips 1 of 12 weapons, fires on timers (1.9-2.1s), loots "BabylonBag" keyword items within 5000 units every 29-31s, navigates toward storm zone center using `IsInsideStormZone()` and `GetHeadingToStormZoneCenter()` |

### Quest & Smoke Testing (4 scripts)
| Script | Purpose |
|--------|---------|
| `SmokeTestQuests.psc` | Runs TestSmokeQuest01 through TestSmokeQuest10 sequentially |
| `SimultaneousTestQuests.psc` | 5 bots each run different smoke test quests simultaneously using `player.moveto` console commands |
| `LoadTestQuests.psc` | Uses `BatchRunCommand("player.moveto")` and `setStage` to load test quests -- **proves scripts can execute raw console commands** |
| `COCAndWait.psc` | Center-on-cell and wait |

### Vault & Shelter Testing (3 scripts)
| Script | Purpose |
|--------|---------|
| `LoadVault94_v1.psc` | Vault 94 load test: teleport in, walk in pattern, fight enemies, teleport out, repeat for 10 min |
| `ShelterTest.psc` | Creates CAMP, enters 4 shelter types (VaultLivingQuarters/ServerRoom/Atrium/Reception), tests 26 locations via encoded coordinate strings |
| `ShelterTest_Cycle/InOut.psc` | Shelter enter/exit cycling |

### Infrastructure Testing (7 scripts)
| Script | Purpose |
|--------|---------|
| `DistributeClientsFromFile.psc` | Reads cell names from file, distributes bots using spiral placement algorithm to avoid overlap |
| `DistributeClientsForMaxLoad.psc` | Maximum load distribution |
| `TACAllStandard/TACAllStandardDistributed.psc` | "Test All Cells" automated cell loading |
| `TACGraphicsTest/TACGraphicsTestLimited.psc` | Graphics testing across cells |
| `TACInteriorsStandard.psc` | Interior-only cell testing |
| `TestScriptNetworkingKeywords.psc` | Tests all multiplayer script networking: synced properties, RMI, client/server events |

### Misc Testing (8 scripts)
| Script | Purpose |
|--------|---------|
| `UsePowerArmor.psc` | Finds nearest power armor (FormID 133022), enters, validates, exits |
| `UseChems.psc` | Automated chem usage |
| `UseStimpak.psc` | Automated stimpak usage |
| `ExplosionTest.psc` | Tests explosion forms sequentially |
| `SpawnAI.psc` | AI spawning helper |
| `Wait.psc` | Timer-based waiting |

---

## 4. Developer-Named Test Cells (14+ Identified Devs)

The strings file reveals personal test cells belonging to individual Bethesda developers:

| Cell Name | Form ID | Developer |
|-----------|---------|-----------|
| Nate's Test Cell | 00036982 | Nate (designer/level artist) |
| Mandi2 Test Cell | 00037748 | Mandi (second iteration) |
| James' Test Cell | 00040B5E | James |
| Emil's Test Cell | 00045243 | **Emil Pagliarulo** (lead designer) |
| Martins Test Cell | 0005678B | Martin |
| Jaes Test Cell | 61006202 | Jae |
| Ryan Salvatore's Test Cell | 610084E9 | Ryan Salvatore |
| FKhanTestCell | 61017C99 | F. Khan |
| My GWWS Test Cell | 81002F55 | Unknown (GWWS = ?) |
| Stephanie's Debug Cell | 39295204 | Stephanie |
| Veronica's Test Cell | 6100F04F | Veronica H. |
| David Debug Cell | 810047F7 | David |

### Developer Debug Locations/Worldspaces
| Location | Form ID | Developer |
|----------|---------|-----------|
| DebugSteveM | 61004ECB | Steve M. |
| DebugChrisMLocation | 39002A71 | Chris M. |
| DebugJeffU_Worldspace01 | 4100ACE5 | Jeff U. |
| DebugJeffULocation01 | 6101960F | Jeff U. |
| DebugBarbaraF Location | 61028E5B | Barbara F. |
| DebugABlackLocation | 7100C210 | A. Black |
| DebugBadenGLocation | 81005954 | Baden G. |
| DebugRussellWorld | 81005AB5 | Russell |
| DebugBadenGInstancedLocation | 81005B92 | Baden G. (instanced) |
| DebugTomRLocation | 8100BA73 | Tom R. |
| DebugDaryl01Location | 00040B8C | Daryl |
| DebugDobert03 | D9005142 | Dobert |

### Developer-Named Test Scripts
| Script | Developer |
|--------|-----------|
| test_VHarbison (7+ scripts) | V. Harbison -- built escape room quest prototype, robot destroyer, NPC companion systems |
| TestKurt (6 scripts) | Kurt -- PvP/bounty systems, quest scripting, terminal testing, disconnect handling |
| TestBurke | Burke -- quest scripting |
| TestCorrie (3 scripts) | Corrie -- actor/quest scripting |
| TestJay (2 scripts) | Jay -- quest/trigger scripting |
| TestBryan (4 scripts) | Bryan -- explosions, timers, struct scripting |
| TestDaryl (3+ scripts) | Daryl -- activate parent client/server/alias testing |
| TestAlyssa (2 scripts) | Alyssa -- one-way container, trigger enter scripting |
| TestBos | Unknown -- Brotherhood of Steel activation testing |
| TestForMikeScript | Mike -- empty quest instance |
| DebugJustinN01 | Justin N. -- NPC sandbox/patrol button system |
| DLC01_testJeffBScript | Jeff B. -- DLC01 testing |
| SF_TestDonScript | Don -- Suicide Run quest variant |
| DebugFunctionsTests | N/A -- Unit tests for the AutoTest assertion framework itself |

---

## 5. The "76 QA Smoke" Test Cell

**Form IDs**: 00037761, 00040B87, 81000007

The QA Smoke test cell is a comprehensive testing environment containing:

### Test Items (with "TestSmoke" prefix)
Items specifically created for QA testing, found in strings:
- TestSmoke Ashtray, TestSmoke Acid, TestSmoke Tall Flask
- TestSmoke Tube Flange, TestSmokeAdhesive, TestSmoke Lamp
- TestSmoke Cooking Oil, TestSmokeCircuitBoard, TestSmoke Bonesaw
- TestSmoke Coolant, TestSmoke Fuse, TestSmoke Baseball
- TestSmokeQuantum, TestSmoke Nuka Cherry
- Smoketest25 Pipe (weapon)

### Smoke Test Quests (29 quests!)
TestSmokeQuest00 through TestSmokeQuest28, each testing a different game system. The `SmokeTestQuests.psc` automated bot sequentially runs quests 01, 02, 04, 05, 06, 07, 08, 09, and 10.

### Related Cell Names
- 76 Quest Smoke Test [00037762, 00040B88]
- 76 PVP Playground [000376B2]

---

## 6. Other Test Cells (300+)

The strings file contains **300+ "Quick Test Cell"** entries across all DLC modules, plus specialized test cells:

| Cell | Form ID | Purpose |
|------|---------|---------|
| Debug Ambush Test Cell | 00046D7C | Ambush encounter testing |
| Ambush Test Cell | 000376A8 | Ambush system testing |
| Encounter Test Cell | 000376FF, 0003776A | Encounter system testing |
| Animation Test Cell | 41004BE3, 610090F0 | Animation playback testing |
| Glass Shader Test Cell | 4100A883 | Shader/material testing |
| Instancing Test Cell | 6100D852 | Instance/server testing |
| Test Cell: Basement | 61029177 | Interior testing |
| Test Cell: Research Facility | 61029178 | Interior testing |
| Debug Flight World | 000529DF | Flying/vertibird testing |
| DebugRange | 00021F90, 000376A9, 000376C2 | Weapon testing range |
| DebugGreenScreen | 6101853A | Screenshot/video capture |

---

## 7. Debug Quest Shortcuts & Teleport Systems

### Enclave Quest Debug Chain
Three debug scripts allow developers to **skip directly to any point** in the Enclave questline:
- `DEBUG_EN02_StartScript` -- Jump to EN02 with Congressional ID key and debug marker
- `DEBUG_EN05StartScript` -- Jump to EN05 with full Enclave faction membership, all prerequisites set, Enclave Officer uniform equipped
- `DEBUG_StartENz01` -- Jump to repeatable Enclave events with configurable debug value

### Wayward Quest Debug
`DEBUG_LVC_StartWaywardQuestline` -- Comprehensive Wastelanders questline skip:
- Teleports player to specific quest stage
- Auto-completes prerequisite quests
- Sets Polly's body choice (Protectron/Handy/Assaultron)
- Controls Sol's fate (alive/dead via BadEnding AV)
- Gives specific items for the quest stage
- Configures Wayward state value

### LVC Debug Quest
`DEBUG_LVCDebugQuestScript` -- Full Enclave + Wayward debug control panel with Deja debug channel "LVC", cooldown management for Duchess, and quest completion shortcuts.

### TestFastTravelPrototype
A **prototype fast travel system** using terminals instead of the map:
- Array of FastTravelLocationData structs with Location, unlock AV, and destination marker
- Terminal menu system for selecting destinations
- Unlock tracking via ActorValues (0=locked, 1=unlocked)

---

## 8. Multiplayer Networking Test Scripts

Six `MPScriptTest*` scripts test the fundamental client-server architecture:

| Script | Tests |
|--------|-------|
| `MPScriptTestClientRMIKeyword` | Client-only Remote Method Invocation (enables object for activating client only) |
| `MPScriptTestServerRMIKeyword` | Server RMI via `SendRMIToServer()` (enables object for all clients) |
| `MPScriptTestRMIToAllClientsKeyword` | Broadcast RMI to all connected clients |
| `MPScriptTestSyncPropertyKeyword` | Synchronized network variables with `OnSyncVariableNetworkChanged()` callback |
| `MPScriptTestClientBroadcastKeyword` | Client broadcast messaging |
| `MPScriptTestClientEventKeyword` / `ServerEventKeyword` | Client/server event systems |
| `MPScriptTestClientFunctionKeyword` / `ServerFunctionKeyword` | Client/server function calls |

---

## 9. Disabled/Cut Game Modes

### Nuclear Winter (Codename: "Babylon")
Internal codename confirmed as "Babylon" across 21+ scripts and UI strings:
- `$GameMode_Babylon` = "Nuclear Winter"
- `$MainMenuBabylon` = "NUCLEAR WINTER"
- `$MainMenuPlayNuclearWinter` = "Nuclear Winter (BETA)"
- Full PvP mode with storm zones, custom perk cards, overseer ranking
- AI bot system (`BabylonTest.psc`) for testing matches
- Enemy spawn testing (`DLC01_Babylon_SpawnEnemyTest.psc`)
- Ghost mode effect, stealth boy effect, stimpak tracking
- Nuclear Winter Loot Terminal network (4 separate terminal instances)
- Mode-specific tutorial tips about addiction immunity, reduced fall damage, no hunger/thirst

### Survival Mode (CUT)
A separate hardcore PvP mode with leaderboards:
- `$ModeSelectHeaderSurvival` = "SURVIVAL MODE"
- `$Challenge_SurvivalModeOnly_ToolTip` = "Can only be completed in Survival Mode."
- `$LeaderBoardMenuTitle` = "SURVIVAL MODE LEADERBOARDS"
- Leaderboard categories: BountyCollected, EnemyKills, EventsCompleted, PlayerKills, TimeAlive, TimeWanted, WorkshopsClaimed, XpGained
- Unrestricted PvP, train station respawns only, higher stakes/greater rewards
- `$ModeSelectSurvivalModeDetailLine1` = "Other players may be attacked without restriction"

### PvP Game Modes (PARTIALLY CUT)
Quest fragments for multiple PvP modes exist:
- `QF_QP_PvP_TDM_Master` -- Team Deathmatch
- `QF_QP_PvP_TDM_OneLife_Master` -- Team Deathmatch One Life variant
- `QF_QP_PvP_FFA_Master` -- Free For All
- `QF_QP_PvP_FFA_HunterHunted_M` -- Hunter/Hunted FFA variant
- "76 PVP Playground" test cell [000376B2]
- TDM scoring: "first team to score 50 points, wins"
- "The arenas for Team Deathmatch are randomly picked from one of the many locations within Appalachia"

---

## 10. TEMP/TODO Comments -- Unfinished Business

Scripts contain developer comments revealing incomplete or placeholder systems:

| Script | Comment |
|--------|---------|
| `bountycollectionsystemrefscript.psc` | "TODO - 6280 - TEMP reward item. In the future, this should be a leveled list once we figure out how rewards should work" |
| `bountycollectionsystemrefscript.psc` | "TODO - 6280 - TEMP reward amount. This will be cut in the future" |
| `clearactiveeffectonrespawn.psc` | "TEMP. DELETE WHEN 16477 IS DONE. Used to remove effects from players when they respawn." |
| `enz09_questscript.psc` | "TEMP - 6900 - To be replaced with cool reward in the future" (x2) |
| `en07_accesspanelaliasscript.psc` | "TEMP - 21622. Remove once we has a good way to mark EN05 completed" |
| `gq_wanderingbossscript.psc` | "TODO: In future we will probably limit [boss spawns] by region" |
| `qp_testworkshopscript.psc` | "TEMP - Very temp - put this on a workshop or trigger box linked to a workshop to start a quickplay match onInit" |
| `workshopparentscript.psc` | "used to check if something is a resource producer - TEMP until 28338" |
| `objectivemodule_proximitytracker.psc` | "TO BE REMOVED" |
| `powersystemdatascript.psc` | Three TODO comments about entropy multiplier systems for power plant failure rates |
| `temp_en05_startontriggerenterscript.psc` | "TEMP Script to be used until terminals work again" |
| `burn_bounty_handleondying.psc` | "***DEPRECATED*** -- SET THESE PROPERTIES IF THIS IS USED ON A THREE STAR ALIAS FOR A HEADHUNT" |
| `petspawnfurniturescript.psc` | "TEMPORARY What actor base is spawned - code will do this eventually" |

The numbered IDs (6280, 16477, 6900, 21622, 28338) are **Bethesda's internal bug/task tracker IDs** (likely JIRA or similar).

---

## 11. EWS Test Button -- Designer Cheat Panel

`EWSTestButton.psc` exposes a debug button with toggleable cheat powers:
- `KillAllHostiles = True` -- Kill every hostile in the area
- `SetPlayerLevel = True` -- Set player to any level via `EWSTest_PlayerLevel` global
- `MovePlayer = True` -- Teleport player to linked destination
- `StartEWS = True` -- Start Encounter Wave System
- `OverrideEWSParameters = False` -- Override ActorSkew and Difficulty
- `ImmobilizeSpawnedEnemies = True` -- Freeze all spawned enemies

---

## 12. Internal Tooling References

### Deja Debug Channels
Multiple scripts reference "Deja" channels -- this is **Deja Insight**, a Bethesda internal debugging/profiling tool:
- `String DejaChannel = "LVC"` (Level/Voice/Content)
- `String asDejaChannel` parameter on all Trace functions
- Custom sub-channels per system

### GPU Benchmark System
`GPUBenchFakePlayerScript.psc` -- Creates fake players for GPU benchmarking:
- Enables AI, moves to linked position, disables AI
- Used for consistent benchmark scenes

### Debug Controls
`[0003A547] Debug Controls for RSVP series` -- Developer debug menu for the RSVP event system

### Debug Visualization
Multiple string entries for `DebugVisualization = <Token.Value=TokenDebugVisualization>` -- a debug rendering overlay system

### ImGui Debug
`[7100684B] ImguiDebugDisplayFormList` -- Proof that Bethesda uses **ImGui** (Immediate Mode GUI) for internal debug displays, with a form list viewer

---

## 13. Console Command Usage in Scripts

The `LoadTestQuests.psc` and `SimultaneousTestQuests.psc` scripts prove that raw console commands can be batch-executed from Papyrus:

```
Self.BatchRunCommand("player.moveto 003971E0")
Self.BatchRunCommand("setStage " + instance + " 200")
Self.BatchRunCommand("player.moveto 0x0001578D")
Self.BatchRunCommand("player.moveto 0x002EB7DA")
Self.BatchRunCommand("player.moveto 0x00030561")
```

These use FormIDs to teleport test bots to specific quest locations and advance quest stages.

---

## 14. V. Harbison's Prototype Systems (7+ Scripts)

Developer V. Harbison built several prototype quest systems:

### Escape Room Quest
`test_VHarbison_Escape_Room_Script.psc`:
- Multi-slot puzzle system (3 item slots with configurable requirements)
- Environmental lights (MainLight, NoteLight, SpeakerLight)
- Proctor NPC that moves to evaluate performance
- Fuse box scenario interaction

### Robot Rager
`test_VHarbison_RobotRager.psc` / `RobotDestroy01.psc` / `PlayerDestroy03.psc`:
- Robot destruction combat encounter
- Player destruction tracking
- SuperHandy robot reference
- Debug message system

### NPC Companion Prototype
`test_VHarbison_Someone_To_Watch_Over_Me` (quest name visible in fragment):
- "Bob" NPC marker system
- Instance enable marker
- Return intro scene
- Dialogue quest integration

### Container System
`test_VHarbison_Container_On_Activate.psc`:
- Custom container activation with Activator_ID global tracking

---

## 15. Veronica's Debug Terminal

```
[39005AC6] Veronica Debug Test Terminal
[39005AC7] This is the Body Text of the CTest Terminal VeronicaHDebug. How's it look?
```

A developer named Veronica H. left a test terminal with a casual message checking how the terminal body text renders. Her test cell is at `[6100F04F] Veronica's Test Cell`.

---

## 16. Additional Interesting Test Scripts

### TestFakePlayerQuestScript
Creates fake players with patrol behavior (`DMP_Patrol_WeaponOut_Run`) between marker arrays -- used to simulate populated servers.

### WeaponTestingRangeSpellScript
Debug weapon testing with health percentage tracking for damage calculation.

### TestChargEnStartingAnimsScript
Tests character generation starting animations.

### KnifeThrowing_TestScript
Test script for an unreleased or prototype knife throwing mechanic.

### PowerSystem_TestScript
Debug terminal and testing framework for the Poseidon/Monongah/Thunder Mountain power plant system.

### Debug_PlayAnimationScript
Utility to play any animation event by name on any object -- essentially an animation debug tool.

### Debug_ForceIntoFurniture
Forces actors into furniture -- used for testing sit/sleep/use animations.

---

## 17. String-Based Evidence Summary

### Developer Loot Items
- `[000400D2] StartQuest (Debug)` -- Debug quest starter
- `[000400D3] DEBUG: Start Test_Tut04` -- Tutorial debug start
- `[0003DBD3] Debug ID Card` -- Developer access card
- `[0004BE12] Begin Debug Sequence` -- Debug sequence initiator
- `[00049424] Debug Ingredients` -- Crafting ingredient test items
- `[61002D46] Debug EyeBot` -- Debug eyebot NPC
- `[81000089] Debug JustinN Plastic Fork` -- Justin N's test weapon

### Debug Combat Packs
- `[0003BA04] DEBUG: Level 40 Combat Pack`
- `[0003BA05] DEBUG: Level 20 Combat Pack`
- `[0003BA06] DEBUG: Level 30 Combat Pack`
- `[0003BA08] DEBUG: Level 10 Combat Pack`
- `[00036F72] DEBUG: Deathclaw vs. Super Mutants` -- Staged fight encounter

### Debug Quest Starts
- `[00040180] Start Quest: Test_Tut04 (Debug)`
- `[00040344] DEBUG: ShowMessage`
- `[81000068] JustinN Test Quest`
- `[8100008B] JustinN Test Wave Quest`
- `[81000088] JustinN Settler`

### Anti-Cheat Reference
From UI strings: `$XPD_AC01_OptionalObjective2` = "Reaped the bloody rewards of the anti-cheat detection system" -- suggests an in-game quest references the anti-cheat system (possibly The Pitt expedition content).

---

## 18. Key Takeaways

1. **Server admin tools shipped in client scripts**: `ExecuteServerConsole()`, `QueueBatchedServerConsoleCommand()`, and `ExecuteBatchedServerConsoleCommands()` expose raw server command execution capability.

2. **48 automated test bot scripts** reveal exactly how Bethesda load-tests their servers -- AI-driven bots that explore, fight, loot, craft, enter shelters, and play Nuclear Winter.

3. **14+ named Bethesda developers** have personal test cells left in the game data, including lead designer Emil Pagliarulo.

4. **Steve M.** was a prolific QA engineer who built elaborate bug demonstration quests touching nearly every game system.

5. **Three cut game modes** remain in data: Nuclear Winter (Babylon), Survival Mode, and multiple PvP variants (TDM, FFA, Hunter/Hunted).

6. **Internal task tracker IDs** (6280, 6900, 16477, 21622, 28338) are embedded in TODO/TEMP comments.

7. **ImGui debug displays** prove Bethesda uses ImGui for internal development tools.

8. **Deja Insight** is Bethesda's internal debugging/profiling tool, referenced across dozens of scripts.

9. The **complete unit testing framework** (AutoTest*) embedded in debug.psc rivals professional testing libraries with assertions, timing, and file I/O.

10. **Console commands can be batch-executed from scripts**, proven by LoadTestQuests and SimultaneousTestQuests using `player.moveto` and `setStage`.
