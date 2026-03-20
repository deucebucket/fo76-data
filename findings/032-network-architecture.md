# Fallout 76 Network Architecture: Complete Client-Server Analysis

**Analysis Date:** 2026-03-20
**Source:** 7,095 decompiled Papyrus scripts + ESM data
**Method:** Exhaustive search of all Native function declarations, network keywords, sync variables, RMI calls, and client/server code paths

---

## Executive Summary

Fallout 76 runs a **hybrid client-server architecture** built on top of Bethesda's single-player Papyrus scripting VM. The engine was retrofitted with multiplayer primitives that reveal a clear authority model:

- **Server-authoritative**: Inventory, actor values (stats/SPECIAL), quest state, NPC spawning, damage, currency, PvP status, workshop ownership
- **Client-authoritative**: Rendering, UI/HUD, camera, audio, image space modifiers, tutorials, input controls, visual effects
- **Synchronized via engine**: Object positions, animation states (via SimpleNetworkState and SyncVariable), activator states

The scripting layer exposes **1,107 Native C++ engine functions** across the core classes, plus three FO76-specific networking primitives not found in Fallout 4.

---

## 1. FO76-Specific Networking Primitives

Three mechanisms were added to the Creation Engine specifically for multiplayer. None of these exist in Fallout 4.

### 1.1 SendRMIToServer (Remote Method Invocation)

**Defined in:** `scriptobject.psc` (base class for ALL scripts)
```
Function SendRMIToServer(String asFuncName, Var[] aParams) Native
```

This is the primary client-to-server communication channel in Papyrus. The client calls a function name as a string, and the server executes it. Found in **20 scripts** across the codebase.

**Usage patterns:**
- Arcade games: `SendRMIToServer("RegisterWin")`, `SendRMIToServer("UpdateScore")`, `SendRMIToServer("RegisterSpeedup")`, `SendRMIToServer("BecomeVulnerable")`
- Character creation: `SendRMIToServer("TellQuestWeHaveLeftFaceGen")`, `SendRMIToServer("TellQuestIntroVideoHasFinished")`
- Quest/world state: `SendRMIToServer("RequestEventState")`, `SendRMIToServer("CheckPlayerWaywardValue")`
- Raid system: `SendRMIToServer("RemovePlayerFromRaid")`
- Laser grids/collisions: `SendRMIToServer("RequestCollisionUpdate")`, `SendRMIToServer("ReevaluateConditions")`
- Mission quests: `SendRMIToServer("ClearMissionQuestExit")`, `SendRMIToServer("PerformMissionQuestExit")`
- Whitespace barber: `SendRMIToServer("ServerPlayLooksMenuEventComment")`

**Key insight:** RMI functions that execute on the server receive a `player akSendingPlayer` parameter, allowing the server to know which client sent the request. Example from `mpscripttestserverrmikeyword.psc`:
```
Function ServerRMIFunction(player akSendingPlayer)
```

### 1.2 OnSyncVariableNetworkChanged

**Defined in:** `objectreference.psc` and `activemagiceffect.psc` (as empty event handlers)
```
Function OnSyncVariableNetworkChanged(String varName)
```

This is the server-to-client variable synchronization callback. When the server changes a property marked for network sync, all clients receive this event with the variable name. Found in **25+ scripts**.

**Usage patterns:**
- Animation sync: Doors, buttons, and activators listen for property changes like `"SetOpenAnim"`, `"SetClosedAnim"`, `"bShouldEnableRef"` and replay animations client-side
- Power systems: `workshoppowercounterscript`, `workshoplightboxscript`, `workshoppoweredspeakerscript`
- Casino/arcade machines: `atxslotmachinescript`, `xpd_ac_slotmachine`, `xpd_ac_casinogame`
- Environmental hazards: `cyclicelectricalhazard`, `trapelectricarc`
- Quest objects: Nuke silo cameras, flip card signs, resource generator buttons

**Critical discovery from `mpscripttestsyncpropertykeyword.psc`:**
```papyrus
Function ClientFunction()
  If bShouldEnableRef
    Self.GetNthLinkedRef(2, None).EnableNoWait(False)
  EndIf
EndFunction

Function OnSyncVariableNetworkChanged(String varName)
  If varName == "bShouldEnableRef"
    Self.ClientFunction()
  EndIf
EndFunction
```
This test script explicitly labels the flow: server changes `bShouldEnableRef` -> client receives `OnSyncVariableNetworkChanged` -> client calls `ClientFunction()`.

### 1.3 SimpleNetworkState (Integer State Sync)

**Defined in:** `objectreference.psc`
```
Int Function GetSimpleNetworkState() Native
Function OnSimpleNetworkStateSet()  ; Event handler
```

A lightweight integer-based state sync mechanism. The server sets an integer state, and all clients receive the `OnSimpleNetworkStateSet` callback. Used primarily for multi-state activators (doors, switches, vault mechanisms).

**Found in:** `defaultmultistateactivator.psc`, `vaultdefaultmultistateactivator.psc`, `vaultdefault2stateactivator.psc`, `vaultdefault1stateactivator.psc`, `vaultidcardreaderscript.psc`, `vaulthandscannerscript.psc`, `vaultcanisterpanelscript.psc`, `v94_1_stranglerheartscript.psc`

Related: `UsesCellBasedNetworkingOptimization()` -- a Native bool check that determines whether the activator should update its visual state based on cell-level networking.

---

## 2. Complete Native Function API Map (Core Classes)

### 2.1 Player.psc (69 Native Functions)

Extends Actor. All functions unique to the local/remote player distinction.

**Network/Multiplayer:**
| Function | Authority |
|----------|-----------|
| `IsConnected()` | Query - is this player connected to the server |
| `IsPacifist()` | Server - pacifist mode flag |
| `IsPVPFlagged()` | Server - PvP engagement flag |
| `IsVisitor()` | Server - visitor status in instanced location |
| `HasSpawnedIntoBabylonGame()` | Server - Nuclear Winter session check |
| `GetBountyState()` | Server - wanted/bounty level |
| `Revive(Player, Bool)` | Server - revive downed player |
| `FastTravel(ObjectReference, Bool)` | Server - `abMakeSoloInstance` flag reveals instancing |
| `TravelToExpeditionLocation(Location)` | Server - expedition instancing |

**Stats/Inventory (Server-Authoritative):**
| Function | Notes |
|----------|-------|
| `GetCapsAmount()` | Currency query |
| `QueryStat(String)` | Gameplay statistics |
| `IncrementStat(String, Int)` | Modify tracked stats |
| `IncrementSkill(ActorValue, Int)` | Skill progression |
| `AdvanceSkill(String, Float)` | Alternative skill progression |
| `GetHighestLevelAchieved()` | Level tracking |
| `IsInventoryWeightBelowAbsoluteLimit()` | Weight check |

**Client-Only (UI/Camera/Audio):**
| Function | Notes |
|----------|-------|
| `ShakeCamera(ObjectReference, Float, Float)` | Screen shake effect |
| `ShakeController(Float, Float, Float)` | Controller rumble |
| `ForceFirstPerson()` | Camera mode |
| `ForceThirdPerson()` | Camera mode |
| `ShowSelfieMenu()` | Photo mode UI |
| `ShowPerksMenu()` | Perk selection UI |
| `ShowSPECIALMenu()` | SPECIAL selection UI |
| `ShowAtomicShopMenu(String, Keyword)` | Atom shop UI |
| `ShowRaceMenu(...)` | Character appearance |
| `ShowTrainingMenu(Actor)` | Training UI |
| `ShowSpecialBuildsMenu(ObjectReference)` | Loadout UI |
| `ShowCompanionNameMenu(Actor)` | Companion naming |
| `ShowInsufficientOverseerRankMessage(Float, Float)` | Error message |
| `TriggerScreenBlood(Int)` | Visual effect |
| `UsingGamepad()` | Input device query |

**Controls:**
| Function | Notes |
|----------|-------|
| `IsActivateControlsEnabled()` | All 10 control state queries |
| `IsCamSwitchControlsEnabled()` | |
| `IsFastTravelControlsEnabled()` | |
| `IsFavoritesControlsEnabled()` | |
| `IsFightingControlsEnabled()` | |
| `IsJumpingControlsEnabled()` | |
| `IsLookingControlsEnabled()` | |
| `IsMenuControlsEnabled()` | |
| `IsMovementControlsEnabled()` | |
| `IsSneakingControlsEnabled()` | |
| `IsVATSControlsEnabled()` | |

**Radio/Audio:**
| Function | Notes |
|----------|-------|
| `GetRadioFrequency()` | |
| `IsRadioOn()` | |
| `IsInRadioRange(Float, questinstance)` | |
| `IsListeningToRadioFrequency(Float, questinstance)` | |
| `TurnRadioOn(Bool)` | |
| `RadioSignalTrackerStart/Update/Stop(...)` | Signal tracking system |

**Other:**
| Function | Notes |
|----------|-------|
| `SetAIDriven(Bool)` | Toggle AI control of player |
| `SetCameraTarget(Actor)` | Camera target override |
| `SetOnElevator(Bool)` | Elevator state |
| `SetReportCrime(Bool)` | Crime reporting toggle |
| `SetFactionEnemy(Faction, Bool)` | PvP faction system |
| `IsFactionEnemy(Faction)` | PvP faction query |
| `SetSeenTutorial(Int, Bool)` | Tutorial tracking |
| `HasSeenTutorial(Int)` | Tutorial query |
| `IsNewCharacter()` | First-time character check |
| `SpawnPickRandomPoint()` | Spawn selection |
| `GetFollowers()` | NPC follower array |
| `GetHeadingToStormZoneCenter()` | Nuclear Winter storm |
| `IsInsideStormZone(Float)` | Nuclear Winter storm |
| `GetLastRiddenHorse()` | Mount system |
| `IsInVATS()` | VATS state |

**FO76 Babylon/Battle Royale:**
| Function | Notes |
|----------|-------|
| `SetSeenBabylonTutorial(Int, Bool)` | NW tutorial tracking |
| `HasSeenBabylonTutorial(Int)` | NW tutorial query |

**XP Source Constants (reveal server-side XP tracking):**
- `XPSource_Unknown`, `QuestComplete`, `SpeechChallenge`, `QuestReward`, `ObjectConstruction`, `LockPick`, `CorpseLoot`, `LevelExpSync`, `LootDropOnDeath`, `LeveLRaise`, `TrapDisarmed`, `NPCKill`, `LocationDiscovery`, `RevivedPlayer`, `Hacking`, `NPCKillAssist`, `ChallengeReward`, `FishCaught`

**Currency Change Reasons (server-side economy audit trail):**
- `NukaColaUsed`, `ReservationSystemReservation/Refund`, `MissionQuestReward`, `CapsStashActivated`, `ExitCharGen`, `DialogueBribe/Purchase`, `SlotMachineUsed/Reward`, `NukaCadeGameStarted`, `RouletteTableUsed/Reward`, `MechanicalDerbyMachineUsed/Reward`, `CrapsTableUsed/Reward`

### 2.2 Actor.psc (200 Native Functions)

Extends ObjectReference. Controls all NPCs and players.

**Movement Control (Ambiguous -- client predicts, server validates):**
| Function | Notes |
|----------|-------|
| `ForceMovementDirection(Float, Float, Float)` | Override movement direction |
| `ForceMovementSpeed(Float)` | Override movement speed |
| `ForceMovementSpeedRamp(Float, Float)` | Smooth speed changes |
| `ForceMovementRotationSpeed(Float, Float, Float)` | Override rotation |
| `ForceMovementDirectionRamp(Float, Float, Float, Float)` | Smooth direction |
| `ForceMovementRotationSpeedRamp(Float, Float, Float, Float)` | Smooth rotation |
| `ForceTargetAngle(Float, Float, Float)` | Face direction |
| `ForceTargetDirection(Float, Float, Float)` | Move direction |
| `ForceTargetSpeed(Float)` | Move speed |
| `ClearForcedMovement()` | Release overrides |
| `PathToReference(ObjectReference, Float)` | AI pathing |

**Combat (Server-Authoritative):**
| Function | Notes |
|----------|-------|
| `StartCombat(Actor, Bool)` | Initiate combat |
| `StopCombat()` | End combat |
| `StopCombatAlarm()` | Clear alarm |
| `Kill(Actor)` | Kill actor |
| `KillSilent(Actor)` | Silent kill |
| `Resurrect()` | Revive from death |
| `ResetHealthAndLimbs()` | Full heal |
| `Dismember(String, Bool, Bool, Bool, Explosion)` | Body dismemberment |
| `DoCombatSpellApply(Spell, ObjectReference)` | Apply combat spell |
| `StartFrenzyAttack(Float, Float)` | Frenzy effect |
| `IsEngagedInPvPWithAnyPlayer()` | PvP state check |
| `IsEngagedInPvPWithPlayer(player)` | Specific PvP check |
| `FindRandomCombatTarget(Float)` | Target acquisition |
| `GetAllCombatTargets()` | All combat targets |
| `GetCombatTarget()` | Current target |
| `GetCombatState()` | Combat state query |
| `SetCombatStyle(combatstyle)` | AI behavior |

**Inventory/Equipment (Server-Authoritative):**
| Function | Notes |
|----------|-------|
| `EquipItem(Form, Bool, Bool)` | Equip item |
| `UnequipItem(Form, Bool, Bool)` | Unequip item |
| `UnequipAll()` | Unequip everything |
| `UnequipItemSlot(Int)` | Unequip by slot |
| `EquipSpell(Spell, Int)` | Equip spell |
| `UnequipSpell(Spell, Int)` | Unequip spell |
| `EquipDisguise(Form)` | Equip disguise |
| `UnequipDisguise()` | Remove disguise |
| `AddSpell(Spell, Bool)` | Add spell |
| `RemoveSpell(Spell)` | Remove spell |
| `AddPerk(Perk, Bool)` | Add perk |
| `RemovePerk(Perk)` | Remove perk |
| `RepairEquippedArmorCondition(Int, Float)` | Repair armor |
| `RepairEquippedWeaponCondition(Int, Float)` | Repair weapon |
| `CollectPowerArmor(ObjectReference)` | Collect PA |
| `ExitPowerArmor()` | Exit PA |

**State/Status (Server-Authoritative):**
| Function | Notes |
|----------|-------|
| `SetInvulnerable(Bool)` | Invulnerability |
| `SetGhost(Bool)` | Ghost mode (no collision) |
| `SetGhostedToTeammates(Bool)` | Teammate ghosting |
| `SetAlert(Bool)` | Alert state |
| `SetUnconscious(Bool)` | Unconscious state |
| `SetRestrained(Bool)` | Restrained state |
| `EnableAI(Bool, Bool)` | AI toggle |
| `SetPlayerTeammate(Actor, Bool, Bool)` | Teammate assignment |
| `SetPlayerControls(Bool)` | Player control toggle |
| `SetRelationshipRank(Actor, Int)` | Relationship adjustment |
| `SetRace(Race)` | Race change |
| `SetOutfit(Outfit, Bool)` | Outfit assignment |
| `SetAttackActorOnSight(Bool)` | Aggression toggle |
| `SetAvoidPlayer(Bool)` | Avoidance toggle |

**Visual/Animation (Client-Side):**
| Function | Notes |
|----------|-------|
| `PlayIdle(Idle)` | Play animation |
| `PlayIdleWithTarget(Idle, ObjectReference)` | Targeted animation |
| `PlayIdleAction(Action, ObjectReference)` | Action animation |
| `PlaySubGraphAnimation(String)` | Sub-graph animation |
| `SetSubGraphFloatVariable(String, Float)` | Animation variable |
| `ChangeAnimArchetype(Keyword)` | Animation archetype |
| `ChangeAnimFlavor(Keyword)` | Animation flavor |
| `ChangeAnimFaceArchetype(Keyword)` | Face animation |
| `AttemptAnimationSetSwitch()` | Animation set change |
| `SetAlpha(Float, Bool)` | Transparency |
| `SetBloodImpactMaterial(material)` | Blood effect |
| `SetEyeTexture(textureset)` | Eye texture |
| `SetHeadTracking(Bool)` | Head tracking |
| `SetLookAt(ObjectReference, Bool)` | Look direction |
| `ClearLookAt()` | Clear look target |
| `AttachAshPile(Form)` | Death effect |
| `TriggerCriticalEffect(...)` | Critical hit VFX |

**Detection/AI (Server-Authoritative for gameplay, client for visuals):**
| Function | Notes |
|----------|-------|
| `HasDetectionLOS(ObjectReference)` | Line of sight |
| `IsDetectedBy(Actor)` | Detection state |
| `StartSneaking()` | Enter sneak |
| `SetNotShowOnStealthMeter(Bool)` | Stealth meter display |
| `WouldBeStealing(ObjectReference)` | Theft check |
| `WouldRefuseCommand(ObjectReference)` | Command check |
| `WillIntimidateSucceed()` | Intimidation check |

### 2.3 ObjectReference.psc (267 Native Functions)

The largest class. All placed objects in the world.

**FO76 Networking Natives:**
| Function | Notes |
|----------|-------|
| `IsLocalPlayer()` | TRUE only for the local player's client |
| `IsAPlayer()` | TRUE for any player reference |
| `GetSimpleNetworkState()` | Get synced integer state |
| `UsesCellBasedNetworkingOptimization()` | Cell-level network optimization |
| `MarkQPClientDataInitializationComplete()` | Client data init signal |
| `ForceSwapModelOnClient(ObjectReference)` | Client-side model swap |
| `GetNearbyPlayers(Float)` | Find players in radius |
| `GetBuiltBy()` | Player who built this object |
| `GetWorkshopOwner()` | Workshop owner query |
| `GetWorkshopClaimant()` | Workshop claimant query |

**Inventory Manipulation (Server-Authoritative):**
| Function | Notes |
|----------|-------|
| `AddItem(Form, Int, Bool, Bool, player, Int)` | Add item -- note `player` param for per-player instancing |
| `RemoveItem(Form, Int, Bool, ObjectReference, Bool)` | Remove item -- `abIncludeStash` flag |
| `RemoveAllItems(ObjectReference, Bool)` | Clear inventory |
| `RemoveComponents(component, Int, Bool)` | Remove crafting components |
| `RemoveItemByComponent(Form, Int, Bool, ObjectReference)` | Remove by component |
| `GetItemCount(Form, Bool)` | Count items -- `abIncludeStash` |
| `GetComponentCount(Form, Bool)` | Component count |
| `StoreInWorkshop(Form, Int)` | Workshop stash |
| `DropObject(Form, Int)` | Drop from inventory |
| `DropFirstObject(Bool)` | Drop first item |

**Actor Values (Server-Authoritative):**
| Function | Notes |
|----------|-------|
| `SetValue(ActorValue, Float)` | Set AV |
| `ModValue(ActorValue, Float)` | Modify AV |
| `DamageValue(ActorValue, Float)` | Damage AV |
| `RestoreValue(ActorValue, Float)` | Restore AV |
| `GetValue(ActorValue)` | Get current AV |
| `GetBaseValue(ActorValue)` | Get base AV |
| `GetValuePercentage(ActorValue)` | Get AV percentage |

**World Manipulation:**
| Function | Notes |
|----------|-------|
| `MoveTo(ObjectReference, Float, Float, Float, Bool)` | Teleport object |
| `MoveToNode(ObjectReference, String, String)` | Move to specific node |
| `MoveToNearestNavmeshLocation()` | Snap to navmesh |
| `MoveToMyEditorLocation()` | Reset to editor position |
| `MoveNukeTo(Float, Float, Float)` | Nuke strike positioning |
| `SetPosition(Float, Float, Float)` | Direct position set |
| `SetAngle(Float, Float, Float)` | Direct rotation set |
| `SetScale(Float)` | Scale change |
| `Enable(Bool)` / `Disable(Bool)` | Object visibility |
| `Delete()` | Permanent removal |
| `SetDestroyed(Bool)` | Destruction state |
| `Lock(Bool, Bool)` | Lock state |
| `SetLockLevel(Int)` | Lock difficulty |
| `Activate(ObjectReference, Bool)` | Trigger activation |
| `BlockActivation(Bool, Bool)` | Block activation |

**Translation/Movement (Synchronized):**
| Function | Notes |
|----------|-------|
| `TranslateTo(...)` | Smooth movement |
| `TranslateToLocal(...)` | Local space movement |
| `SplineTranslateTo(...)` | Spline path movement |
| `SplineTranslateToRefNode(...)` | Spline to node |
| `StopTranslation()` | Stop movement |

**Havok Physics:**
| Function | Notes |
|----------|-------|
| `ApplyHavokImpulse(Float, Float, Float, Float)` | Physics impulse |
| `SetMotionType(Int, Bool)` | Physics mode |
| `ReleaseToHavok(Bool, Bool)` | Physics activation |
| `PushActorAway(Actor, Float)` | Knockback |
| `KnockAreaEffect(Float, Float)` | Area knockback |
| `ForceRemoveRagdollFromWorld()` | Ragdoll cleanup |
| `ForceAddRagdollToWorld()` | Ragdoll activation |

### 2.4 Game.psc (82 Native Functions)

Global game-state functions.

**Key Multiplayer Functions:**
| Function | Notes |
|----------|-------|
| `GetLocalPlayer()` | Get the local player reference |
| `GetGameWorldType()` | Returns world type (Adventure, Nuclear Winter, etc.) |
| `GetDifficulty()` | Server difficulty setting |
| `RequestSave()` / `RequestAutoSave()` | Save requests (server-side persistence) |
| `QuitToMainMenu()` | Disconnect from server |

**Nuclear Winter / Battle Royale:**
| Function | Notes |
|----------|-------|
| `AddNuclearWinterWeatherTransition(...)` | Storm wall weather |
| `LoadNuclearWinterTextureMaps(String[])` | Storm textures |
| `SetNumStormFXData(Int)` | Storm effects count |
| `SetStormFXData*()` | 10+ storm VFX configuration functions |

**Rendering/Visual (Client-Only):**
| Function | Notes |
|----------|-------|
| `FadeOutGame(Bool, Bool, Float, Float, Bool)` | Screen fade |
| `ShowFirstPersonGeometry(Bool)` | First-person body visibility |
| `EnablePipboyHDRMask(Bool)` | Pipboy rendering |
| `ForceDisableSSRDirLight(Bool, Bool)` | SSR/lighting override |
| `SetInsideMemoryHUDMode(Bool)` | HUD mode change |
| `SetCharGenHUDMode(Int)` | Character creation HUD |
| `PlayBink(String, Bool, Bool, Bool, Bool, Bool)` | Video playback |
| `PlayEventCamera(camerashot, ObjectReference)` | Camera event |
| `StartDialogueCameraOrCenterOnTarget(ObjectReference)` | Dialogue camera |
| `StopDialogueCamera(Bool, Bool)` | End dialogue camera |

**UI (Client-Only):**
| Function | Notes |
|----------|-------|
| `ShowPipboyPlugin()` | Pipboy display |
| `ShowPipboyBootSequence(String)` | Pipboy boot animation |
| `ShowPerkVaultBoyOnHUD(String, Sound)` | Perk notification |
| `ShowFatigueWarningOnHUD()` | Fatigue warning |
| `ShowTitleSequenceMenu()` / `HideTitleSequenceMenu()` | Title sequence |
| `StartTitleSequence(String)` | Title animation |
| `SetInChargen(Bool)` | Character creation mode |
| `PrecacheCharGen()` / `PrecacheCharGenClear()` | Chargen asset loading |

**Data Access:**
| Function | Notes |
|----------|-------|
| `GetForm(Int)` / `GetFormFromFile(Int, String)` / `GetFormByEditorID(String)` | Form lookup |
| `GetDataInt/Float/String(...)` | External data file reading |
| `GetGameSettingInt/Float/String/Bool/UInt(String)` | INI settings access |
| `GetXPForLevel(Int)` | XP curve query |
| `IsPluginInstalled(String)` | Plugin check |
| `RegisterQPMap(String, ObjectReference)` | QP map registration |

**Timing:**
| Function | Notes |
|----------|-------|
| `GetRealHoursPassed()` | Real-time tracking |
| `PassTime(Int)` | Advance game time |

### 2.5 Debug.psc (102 Native Functions)

**Server/Client Console Split (KEY FINDING):**
```
Function ExecuteServerConsole(String asCommand) Global Native
Function ExecuteLocalConsole(String asCommand) Global Native
Function QueueBatchedServerConsoleCommand(String command) Global Native
Function ExecuteBatchedServerConsoleCommands() Global Native
```

This proves the console command system is split into server-side and client-side execution. Server console commands are batched and executed atomically, while local console commands execute immediately on the client.

**Bot/Testing Infrastructure:**
| Function | Notes |
|----------|-------|
| `BabylonBotShouldLoot()` | NW bot looting AI |
| `BabylonBotShouldShoot()` | NW bot combat AI |
| `BabylonBotShouldMove()` | NW bot movement AI |
| `SetGodMode(Bool)` | Invincibility toggle |
| `EnableCollisions(Bool)` | Collision toggle |
| `EnableDetection(Bool)` | Detection toggle |
| `EnableAI(Bool)` | Global AI toggle |
| `EnableMenus(Bool)` | Menu toggle |
| `PlayerGoTo(String)` | Teleport by string key |
| `PlayerMoveToAndWait(String)` | Teleport and wait |
| `DBSendPlayerPosition()` | Send position to database |
| `TraceTransaction(String, Int, String)` | Transaction logging |

**AutoTest Framework (42+ functions):** Complete testing framework with `AutoTestExpect*` assertions, fire/loot/move commands, and weapon/health queries. See finding 009 for details.

### 2.6 Utility.psc (43 Native Functions)

| Function | Authority | Notes |
|----------|-----------|-------|
| `Wait(Float)` | Client | Script delay |
| `WaitGameTime(Float)` | Client | Game-time delay |
| `WaitMenuPause(Float)` | Client | Menu-aware delay |
| `RandomInt/Float(...)` | Ambiguous | RNG (likely client-side seeded) |
| `RandomIntsFromSeed/RandomFloatsFromSeed(...)` | Deterministic | Seeded RNG for sync |
| `Now()` | Client | Real-time clock |
| `NowYear/Month/Day/Hour/Minute/Second/DayOfWeek/DayOfYear()` | Client | Time components |
| `GetCurrentGameTime()` | Server | Synced game time |
| `GetCurrentRealTime()` | Client | Real-time seconds |
| `CallGlobalFunction/NoWait(...)` | Either | Dynamic function dispatch |
| `GetBudgetCount/Name/Limit/CurrentBudget(Int)` | Client | Performance budgets |
| `OverBudget(Int)` | Client | Budget check |
| `GetCurrentMemory()` | Client | Memory query |
| `GetAverageFrameRate/Min/Max()` | Client | Frame rate tracking |
| `StartFrameRateCapture/EndFrameRateCapture()` | Client | FPS benchmarking |
| `CaptureFrameRate(Int)` | Client | FPS snapshot |
| `SetINIFloat/Int/Bool/String(String, value)` | Client | INI modification |
| `IntToHex(Int)` | Either | String conversion |
| `GameTimeToString(Float)` | Either | Time formatting |
| `SplitStringChars(String)` | Either | String parsing |
| `GetCurrentStackID()` | Either | Script debug |

### 2.7 Form.psc (10 Native Functions)

| Function | Notes |
|----------|-------|
| `GetFormID()` | Get form ID |
| `HasKeyword(Keyword)` | Keyword check |
| `HasKeywordInFormList(FormList)` | Keyword list check |
| `PlayerKnows()` | Player knowledge |
| `GetGoldValue()` | Base gold value |
| `GetFormWeight()` | Base weight |
| `IsReserved()` | Quest reservation |
| `GetReservingQuests()` | Quest reservation list |
| `StartObjectProfiling()` / `StopObjectProfiling()` | Performance profiling |

### 2.8 ScriptObject.psc (98 Native Functions)

Base class for ALL scripts. Key networking functions:

| Function | Authority | Notes |
|----------|-----------|-------|
| `SendRMIToServer(String, Var[])` | Client->Server | Remote method invocation |
| `RegisterForPlayerConnectionEvent(player[])` | Server | Player connect/disconnect |
| `RegisterAllPlayersForDistanceLessThanEvent(...)` | Server | Proximity events for all players |
| `RegisterForHitEventFromAllPlayers(...)` | Server | Hit detection for all players |
| `RegisterForAllPlayersEvents(String)` | Server | Universal player event registration |
| `CallFunction(String, Var[])` | Either | Dynamic function call |
| `CallFunctionNoWait(String, Var[])` | Either | Non-blocking call |
| `SendCustomEvent(String, Var[])` | Either | Custom event dispatch |
| `SetPropertyValue(String, Var)` | Either | Dynamic property set |
| `GetPropertyValue(String)` | Either | Dynamic property get |
| `LockAcquire(Int)` / `LockRelease(Int)` | Either | Thread synchronization |
| `IsBoundGameObjectAvailable()` | Either | Object validity check |

**Player Connection Events:**
```
Function OnPlayerConnected(player akPlayer)    ; Server event
Function OnPlayerDisconnected(player akPlayer) ; Server event
Function OnPlayerReady(player akPlayer)        ; Server event
```

### 2.9 InputEnableLayer.psc (33 Native Functions)

Complete input control system:
```
InputEnableLayer Function Create(player player) Global Native
Function EnablePlayerControls(Bool Movement, Bool Fighting, Bool CamSwitch, Bool Looking,
                              Bool Sneaking, Bool Menu, Bool Activate, Bool JournalTabs,
                              Bool VATS, Bool Favorites, Bool Running) Native
Function DisablePlayerControls(...) Native  ; Same params
```

Individual control toggles: `EnableMovement`, `EnableFighting`, `EnableCamSwitch`, `EnableLooking`, `EnableSneaking`, `EnableMenu`, `EnableActivate`, `EnableJournal`, `EnableVATS`, `EnableFavorites`, `EnableRunning`, `EnableSprinting`, `EnableJumping`, `EnableFastTravel`

---

## 3. Client vs Server Authority Model

### 3.1 Confirmed Server-Authoritative Systems

**Evidence from script comments and test code:**

1. **Actor Values / SPECIAL Stats**: Test script `actorvaluetests.psc` has function named `Player_SetActorValue_ShouldOnlyWorkOnServer` -- explicitly confirms SetValue on players is server-only
2. **Quest State**: `QuestInstance` is a server-side object. All quest stage changes happen server-side
3. **Inventory**: `AddItem` has a `player` parameter for per-player instancing. `RemoveItem` has `abIncludeStash` for server-side stash access
4. **Currency**: All CurrencyChangeReason constants reveal server-side economy tracking with audit trail
5. **XP/Leveling**: All XPSource constants indicate server-side XP calculation
6. **Workshop Ownership**: `GetWorkshopOwner()`, `GetWorkshopClaimant()`, `GetBuiltBy()` are server state
7. **PvP State**: `IsPacifist()`, `IsPVPFlagged()`, `IsEngagedInPvPWithPlayer()`, `GetBountyState()`
8. **Damage/Kill**: `Kill()`, `KillSilent()`, `DamageValue()`, `Resurrect()` are server-authoritative
9. **Spell Application**: `ApplyOnServer` property default = True in spell scripts with comment "Should always be true for anything that effects gameplay"

**From Default2StateActivator property comments:**
```
Bool Property IsOpen = False Auto conditional
{ DEFAULT: FALSE. VALID ONLY ON SERVER - NOT SYNC. Set to TRUE to start in the open state. }
Int Property OpenState = 3 Auto conditional hidden
{ VALID ONLY ON SERVER - NOT SYNC. }
Bool Property IsSynced = False Auto conditional hidden
{ VALID ONLY ON SERVER - NOT SYNC. }
```

### 3.2 Confirmed Client-Authoritative Systems

1. **Rendering**: All visual effects (ImageSpaceModifier, EffectShader, camera shake, screen blood)
2. **UI/HUD**: All menu shows, tutorials, help messages, notifications
3. **Audio**: Sound playback, radio tuning, conveyor belt sounds
4. **Input**: InputEnableLayer is per-client
5. **Camera**: First/third person, selfie mode, dialogue camera
6. **Tutorials**: `ShowHelpMessageClientAndFlagTutorialSeen` runs entirely on the local client
7. **Image Space Modifiers**: Applied/removed client-side (blackout, nukshine FX, etc.)
8. **Animation Playback**: `PlayAnimation`, `PlayIdle` are client-side visual

### 3.3 Split Authority (Client predicts, Server validates)

Scripts explicitly use `IsLocalPlayer()` to gate client-side effects:

**Pattern:** Check `IsLocalPlayer()` before applying visual/audio effects
```papyrus
; From blackout.psc, nukashinefx.psc, spelleffectimodplayeronly.psc, etc.
If akTarget.IsLocalPlayer()
  HoldAtBlackImod.Apply(1.0)  ; Only apply visual effect on the local player
EndIf
```

**Pattern:** Check `IsAPlayer()` before server-side gameplay effects
```papyrus
; From various trigger scripts
If akActionRef.IsAPlayer()
  ; Apply gameplay effect that should affect any player
EndIf
```

### 3.4 Dual-Execution Model (ApplyOnClient / ApplyOnServer)

Found in `addspelloneffectscript.psc`, `castspelloneffectscript.psc`, and `failsafeaddspelloneffectscript.psc`:

```papyrus
Bool Property ApplyOnClient = True Auto Const
{ Cast this spell on the Client? Uncheck this only if you want no visual/audio/HUD/etc. component. }
Bool Property ApplyOnServer = True Auto Const
{ Cast this spell on the Server? Uncheck this with caution. Should always be true for anything that effects gameplay. }
```

**Key insight:** Spells execute on BOTH client and server by default. The client handles visual/audio components, the server handles gameplay effects. Designers can disable either side independently. The comment "Should always be true for anything that effects gameplay" confirms server authority for game mechanics.

---

## 4. Multiplayer Script Architecture

### 4.1 MP Test Scripts (Rosetta Stone)

Five `MPScriptTest*` files reveal the complete multiplayer scripting model:

| Script | Pattern | Description |
|--------|---------|-------------|
| `MPScriptTestServerRMIKeyword` | Client->Server RMI | Client calls `SendRMIToServer`, server executes function with `player akSendingPlayer` |
| `MPScriptTestClientFunctionKeyword` | Client-only execution | Functions that only run on the activating client |
| `MPScriptTestSyncPropertyKeyword` | Server->Client sync | Server changes property, clients receive `OnSyncVariableNetworkChanged` |
| `MPScriptTestServerFunctionKeyword` | Server-only execution | Functions that only run on server (script body is empty) |
| `MPScriptTestServerEventKeyword` | Server-only events | Events that only fire on server |

### 4.2 Script Execution Context

Scripts in FO76 run in one of three contexts determined by **keywords attached to the script's object in the ESM**:

1. **Server Functions**: Execute only on the server. Set via keyword on the object. The decompiled script body appears empty because the implementation is in C++ or controlled by engine flags.
2. **Client Functions**: Execute only on the activating player's client. Named `ClientFunction` by convention.
3. **Sync Variables**: Properties marked for network sync. When server changes them, `OnSyncVariableNetworkChanged` fires on all clients.

### 4.3 Player Connection Lifecycle

From `scriptobject.psc` and `defaultonplayerconnect.psc`:

1. Player connects to server -> `OnPlayerConnected(player)` fires on registered scripts
2. Player data loads -> `OnPlayerReady(player)` fires
3. Player disconnects -> `OnPlayerDisconnected(player)` fires

`DefaultOnPlayerConnect` demonstrates the pattern: on connection, check player's ActorValues and adjust Factions/Keywords/AVs accordingly. This is how the server reconciles returning players.

### 4.4 Client-Side vs Server-Side Activators

Two parallel class hierarchies exist:

**Server-synced:** `Default2StateActivator`, `Default2StateSyncActivator`, `DefaultMultiStateActivator`
- State changes sync to all clients via `OnSyncVariableNetworkChanged` or `OnSimpleNetworkStateSet`
- Properties marked "VALID ONLY ON SERVER - NOT SYNC"
- All clients see the same state

**Client-side:** `DefaultMultiStateClientSideActivator`
- Script comment: "All animation states are per-client; the object resets to its default state on each load"
- Functions named `ClientPlayAnimation`, `ClientPlayAnimationRMI`
- Used for visual-only objects that don't need sync

---

## 5. Nuclear Winter (Babylon) Architecture

The battle royale mode reveals additional networking infrastructure:

- `HasSpawnedIntoBabylonGame()` - session check
- `GetGameWorldType()` - world type enum (Adventure vs NW)
- `GetGameSettingBool("bNuclearWinterMode")` - mode check used to disable tutorials
- `DLC01_BabylonClientDataInitializer` - initializes storm wall weather, textures, FX data on client
- `MarkQPClientDataInitializationComplete()` - signals client is ready
- `BabylonBotShouldLoot/Shoot/Move()` - AI bot control for NW (see finding 007/010)
- Storm zone functions: `GetHeadingToStormZoneCenter()`, `IsInsideStormZone(Float)`, `StormArea_*` constants

---

## 6. Anti-Cheat and Validation

### 6.1 Server-Side Validation

No dedicated anti-cheat scripts exist in the Papyrus layer. The security model relies on:

1. **Server-authoritative actor values**: `SetValue` on players only works on the server (confirmed by test script name)
2. **Server-authoritative inventory**: Item add/remove operations go through server
3. **Server-authoritative quest state**: QuestInstance is server-side
4. **Server console separation**: `ExecuteServerConsole` vs `ExecuteLocalConsole` prevents client from running server commands
5. **RMI validation**: `SendRMIToServer` includes `player akSendingPlayer` for attribution

### 6.2 What the Client CAN Do (Attack Surface)

The client has direct access to:
- Visual effects, camera, UI (cosmetic only)
- `ForceMovementDirection/Speed` on actors (movement prediction)
- `PlayAnimation` on any loaded object
- `SetAnimationVariable*` on any loaded object
- `EnableCollisions(Bool)` in debug (likely stripped in release)
- `SetGodMode(Bool)` in debug (likely stripped in release)
- `EnableDetection(Bool)` in debug (likely stripped in release)

### 6.3 Transaction Logging

`Debug.TraceTransaction()` is a dedicated Native function for logging transactions, separate from general trace logging. Combined with the detailed `CurrencyChangeReason` constants, this indicates server-side audit trailing of all economy transactions.

---

## 7. Complete Player Automation API

Every function that could control a player character:

### Movement
- `ForceMovementDirection/Speed/Ramp(...)` - Override movement
- `ForceTargetAngle/Direction/Speed(...)` - Force facing/movement
- `ClearForcedMovement()` - Release overrides
- `PathToReference(ObjectReference, Float)` - AI pathing
- `SetWantSprinting(Bool)` - Sprint toggle
- `StartSneaking()` - Sneak entry
- `SetOnElevator(Bool)` - Elevator state
- `MoveTo/MoveToNode/MoveToNearestNavmeshLocation()` - Teleportation
- `FastTravel(ObjectReference, Bool)` - Fast travel
- `TravelToExpeditionLocation(Location)` - Expedition travel

### Combat
- `StartCombat(Actor, Bool)` / `StopCombat()` - Combat toggle
- `SetAttackActorOnSight(Bool)` - Auto-aggression
- `DrawWeapon()` - Draw equipped weapon
- `SetEquippedWeaponAttacksEnabled(Int, Bool)` - Weapon attack toggle
- `SetFrenzyAttack(Float, Float)` - Frenzy state
- `IsInVATS()` - VATS check

### Equipment
- `EquipItem/UnequipItem/UnequipAll()` - Inventory management
- `EquipSpell/UnequipSpell()` - Spell management
- `AddPerk/RemovePerk()` - Perk management
- `AddSpell/RemoveSpell()` - Spell management

### State Control
- `SetAIDriven(Bool)` - Toggle AI control of player
- `SetPlayerControls(Bool)` - Toggle player input
- `SetInvulnerable(Bool)` - Invincibility
- `SetGhost(Bool)` - No collision
- `SetUnconscious(Bool)` - Unconscious state
- `EnableAI(Bool, Bool)` - AI toggle
- `Kill(Actor)` / `Resurrect()` - Death/revival

### Camera
- `SetCameraTarget(Actor)` - Camera follow target
- `ForceFirstPerson()` / `ForceThirdPerson()` - Camera mode
- `ShowSelfieMenu()` - Photo mode

### Input Control
- `InputEnableLayer.Create(player)` - Create input layer
- `EnablePlayerControls/DisablePlayerControls(11 bools)` - Granular control
- Individual: `EnableMovement/Fighting/CamSwitch/Looking/Sneaking/Menu/Activate/Journal/VATS/Favorites/Running/Sprinting/Jumping/FastTravel`

---

## 8. System Authority Summary

| System | Authority | Sync Method |
|--------|-----------|-------------|
| Player Stats (SPECIAL, HP, AP) | Server | Engine-level sync |
| Inventory | Server | Engine-level sync |
| Currency (Caps) | Server | Engine-level sync with audit trail |
| XP / Leveling | Server | Engine-level sync |
| Quest State | Server | QuestInstance server object |
| PvP / Bounty | Server | Engine-level flags |
| Workshop Ownership | Server | Engine-level sync |
| NPC AI / Combat | Server | Engine-level sync |
| Object Activation | Server | SimpleNetworkState / SyncVariable |
| Doors / Switches | Server | OnSyncVariableNetworkChanged |
| Damage Calculation | Server | Engine-level |
| Spell Effects (Gameplay) | Server | ApplyOnServer flag |
| Camera / POV | Client | Local only |
| UI / HUD / Menus | Client | Local only |
| Tutorials | Client | Local + server flag sync |
| Visual Effects (IMOD, Shaders) | Client | IsLocalPlayer() gated |
| Audio / Radio | Client | Local only |
| Input Controls | Client | InputEnableLayer per-client |
| Animation Playback | Client | Triggered by sync callbacks |
| Spell Effects (Visual) | Client | ApplyOnClient flag |
| Movement | Hybrid | Client predicts, server validates |
| Physics (Havok) | Hybrid | Client simulates, limited sync |

---

## Key Architectural Insights

1. **Retrofitted Architecture**: The entire multiplayer system was bolted onto a single-player engine. The `Player` type extending `Actor` and the `IsLocalPlayer()` / `IsAPlayer()` distinction were added specifically for FO76. Fallout 4 had no such concept.

2. **Keyword-Based Script Context**: Whether a script runs on server, client, or both is determined by keywords in the ESM, not by anything visible in the decompiled script. This is why `MPScriptTestServerFunctionKeyword` has an empty body -- the keyword tells the engine to run it server-side.

3. **No Client-Side Validation**: There is zero evidence of client-side cheat detection in Papyrus. All security relies on server authority. The client can manipulate visuals, animations, and local state freely.

4. **Deterministic RNG**: `RandomIntsFromSeed` and `RandomFloatsFromSeed` provide seeded random number generation, likely used to keep client and server in sync for procedural operations.

5. **Transaction Logging**: The combination of `TraceTransaction()`, `CurrencyChangeReason` constants, and `XPSource` constants reveals a comprehensive server-side audit system for economy and progression.

6. **Three-Tier Networking**: Simple integer sync (SimpleNetworkState) for basic objects, variable-level sync (OnSyncVariableNetworkChanged) for complex objects, and RMI (SendRMIToServer) for client-initiated actions. This layered approach minimizes bandwidth while maintaining consistency.
