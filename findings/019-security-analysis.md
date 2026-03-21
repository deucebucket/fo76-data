# Fallout 76 Client-Side Security Analysis

**Date:** 2026-03-20
**Scope:** 7,095 decompiled Papyrus scripts (.psc), string tables
**Purpose:** Responsible disclosure analysis for potential Bethesda bug bounty submission
**Classification:** RESPONSIBLE DISCLOSURE ONLY

---

## Executive Summary

Analysis of Fallout 76's decompiled Papyrus scripts reveals a client-server architecture where most critical game logic (economy, inventory, combat) is handled server-side via Native functions. The Papyrus scripting layer primarily handles UI presentation, state machine transitions, and event coordination. While the architecture is fundamentally sound for an online game, several categories of potential vulnerabilities exist, primarily around race conditions in state machines, debug code remnants, and client-trust patterns in older subsystems.

**Note:** Most economy-sensitive operations (AddItem, RemoveCurrency, etc.) appear to be Native functions that execute server-side, significantly limiting the attack surface from script manipulation alone. The primary risk vectors are timing-based exploits and logical bypasses rather than direct value manipulation.

---

## Category 1: Client-Server Trust Issues

### Finding 1.1: Casino Game RNG Appears Partially Client-Influenced
**Severity:** Medium
**File:** `atxslotmachinescript.psc`, `xpd_ac_casinogame.psc`
**Evidence:**
- `ATXSlotMachineScript` defines `PossibleResults` with `chanceThreshold` values (0.0-1.0) as script properties
- Tumbler values (`lastTumbler1Value`, `lastTumbler2Value`, `lastTumbler3Value`) are synced network variables (`Const hidden` pattern used for sync)
- The `ResultAnimationIdx` in `XPD_AC_CasinoGame` is synced to all clients via `OnSyncVariableNetworkChanged`
- However, the actual random roll logic is not visible in scripts (likely Native/server-side)
**Assessment:** The outcome determination appears server-side (good), but the sync variable pattern could potentially be intercepted. The `chanceThreshold` values in PossibleResults are Const properties -- a client modifying the compiled script could alter perceived thresholds, though the server would reject invalid outcomes. Low exploitability.

### Finding 1.2: Slot Machine Luck Buff Applied Client-Side
**Severity:** Low
**File:** `atxslotmachinescript.psc`
**Evidence:**
```
Keyword Property ATX_DispellFortifyLuck Auto Const mandatory
Spell Property ATX_BuffLuck Auto Const mandatory
{ Luck buff to grant if the player has a Win or Jackpot result. }
```
- A Luck buff spell is cast on win/jackpot results
- If the spell application is client-initiated, a modified client could trigger the buff without winning
**Assessment:** Spell application is likely validated server-side. Low risk.

### Finding 1.3: Nuke Code System Stores Codes in Script Properties
**Severity:** Medium
**File:** `en07_nukemasterscript.psc`, `nuke_masterscript.psc`, `nuke_codesscript.psc`
**Evidence:**
- `iCode` property in `CodeDatum` struct stores "The actual current code" (line 18)
- Codes are 8-digit integers: `iMinCodeNum = 10000000`, `iMaxCodeNum = 99999999`
- Code rotation happens on weekly timer (`NukeCodeTimerDays = 7`)
- Nuke codes JSON filename hardcoded: `nuke_Code_Filename = "nuke_codes"`
- Code data includes cipher, codeword, and code number column names
**Assessment:** Players already brute-force or solve these externally (nukacrypt.com), so this is known. However, the script reveals that codes are deterministic from server-side JSON data, and the cipher system structure is fully exposed. The `currentCode` property being readable in memory would bypass the entire code-hunting questline. This is a design-level issue Bethesda is likely aware of.

---

## Category 2: Race Conditions (TOCTOU)

### Finding 2.1: Keycard Printer State Machine Race Condition
**Severity:** High
**File:** `keycardprinterscript.psc`
**Evidence:**
```papyrus
Auto State Ready
 Event OnActivate(ObjectReference akActionRef)
 Self.GotoState("Busy")
 If akActionRef.IsLocalPlayer()

 EndIf
 Self.GotoState("Ready") ; <-- Returns to Ready immediately
 EndEvent
EndState

State Busy
 Event OnActivate(ObjectReference akActionRef)
 ; Empty function
 EndEvent
EndState
```
- The script transitions to "Busy" but returns to "Ready" within the same event handler
- The IsLocalPlayer() check has an empty body (decompilation artifact or stripped server logic)
- Two players activating simultaneously could both enter the Ready state before either transitions to Busy
- If the actual card-giving logic runs between GotoState calls, rapid activation could yield multiple cards
**Assessment:** The Busy state is meant to prevent concurrent access but the immediate return to Ready creates a window. Whether this is exploitable depends on what the stripped Native code does in the empty block. If the server generates cards, this is benign. If the script generates cards, rapid activation by multiple players could duplicate them.

### Finding 2.2: KidsLunchBox Double-Activation Race
**Severity:** Medium
**File:** `kidslunchboxscript.psc`
**Evidence:**
```papyrus
Event OnActivate(ObjectReference akActionRef)
 If akActionRef.IsAPlayer()
 If LunchBoxActivated == False
 LunchBoxActivated = True
 Self.damageObject(10.0)
 Else
 Self.disable(False)
 akActionRef.AddItem(LunchBoxToAdd as Form, 1, False, False, None, 0)
 Self.Delete()
 EndIf
 EndIf
EndEvent
```
- Two rapid activations: first sets `LunchBoxActivated = True`, second gives item
- But a simultaneous double-activation could have both threads see `LunchBoxActivated == False`
- This is the classic boolean check-then-act TOCTOU pattern
- The AddItem in the Else branch would give the item to whichever player activates second
**Assessment:** In practice, Papyrus script execution is serialized per-object, so true simultaneity is unlikely. However, the pattern is a code smell and similar patterns in other scripts (particularly those handling more valuable items) could be exploitable.

### Finding 2.3: OnActivateAddItem Client-Side Lock Without Server Validation
**Severity:** Medium
**File:** `onactivateadditem.psc`
**Evidence:**
```papyrus
Bool activationLock = False
Bool Property BlockFutureActivation = True Auto Const
```
- Uses a simple boolean `activationLock` to prevent re-activation
- No state machine (which would provide at least script-level atomicity)
- `DoNotAddDuplicate` check: `If true, this script will not add the item if it already exists in the player's inventory`
- The duplicate check and the add are separate operations (TOCTOU)
**Assessment:** The boolean lock pattern without GotoState is weaker than state-machine-based locking. Multiple concurrent activations in a multiplayer environment could bypass the lock.

### Finding 2.4: Fortune Teller Timer-Based Item Grant
**Severity:** Low
**File:** `atx_fortunetellermachinescript.psc`
**Evidence:**
- Stores `activatingPlayer` reference, then uses a timer to grant items
- If a second player activates between state changes, `activatingPlayer` could be overwritten
- Item would be granted to the wrong player
**Assessment:** Race window exists but impact is low (fortune book items are not valuable).

---

## Category 3: Input Validation Gaps

### Finding 3.1: CustomItemQuestScript Bypasses Item Instantiation Rules
**Severity:** High
**File:** `customitemquestscript.psc`
**Evidence:**
```
FormList ModsFormlist
{ List of mods to install on item
****IMPORTANT NOTE****
THIS BYPASSES ALL NORMAL ITEM INSTANTIATION RULES }
```
- Developer comment explicitly states this system bypasses normal item creation rules
- Used for quest reward items (named/unique items)
- If a crafted quest submission could manipulate which `RewardDatum` is selected, arbitrary mods could be applied
**Assessment:** The bypass is intentional for unique quest rewards, but the explicit developer warning suggests they recognized the risk. If any quest using this system has controllable input parameters, items with illegal mod combinations could be created.

### Finding 3.2: Bounty Collection System Uses Hardcoded Reward Values
**Severity:** Low
**File:** `bountycollectionsystemrefscript.psc`
**Evidence:**
```
MiscObject Property RewardItem Auto Const mandatory
{ TODO - 6280 - TEMP reward item. In the future, this should be a leveled list }
Int Property iRewardAmount = 100 Auto Const
{ TODO - 6280 - TEMP reward amount. This will be cut in the future }
```
- Developer TODO indicates temporary reward values that were meant to be adjusted
- If still using the temp values, reward amounts may be higher than intended
**Assessment:** This is a design oversight rather than a security vulnerability. The TODO suggests it was flagged internally but may not have been addressed.

### Finding 3.3: Daily Quest Debug Spawn Properties Still Present
**Severity:** Medium
**File:** `dailyquestscript.psc`
**Evidence:**
```papyrus
Group DebugData
 Int Property ForceTarget = -1 Auto Const
 Int Property ForceImplement = -1 Auto Const
 Form Property DebugAmmo5mm Auto Const
 Form Property DebugAmmo10mm Auto Const
 ...
```
- Debug properties that force specific targets and grant debug ammo
- `ForceTarget` and `ForceImplement` allow overriding random selection
- These are compile-time constants, so they can't be changed at runtime by players
**Assessment:** These are set via the Creation Kit and compiled into the script. A player would need to modify the compiled script on the server to exploit these. Not directly exploitable, but indicates debug infrastructure remains in production code.

---

## Category 4: Economy Exploits

### Finding 4.1: Workshop Attack Timer Manipulation
**Severity:** Medium
**File:** `workshopscript.psc`
**Evidence:**
```papyrus
Float decrementNextAttackTimerSecondsMax = 180.0 Const
Float decrementNextAttackTimerSecondsMin = 90.0 Const
Float refreshInventoryTimeSeconds = 1800.0 Const
Bool bAllowNextAttackDecrement = True
```
- Workshop attack cooldowns use timer-based decrements
- `bAllowNextAttackDecrement` is a non-Const boolean (mutable)
- `WorkshopNextAttackDecrementPerCollectorDays` and `WorkshopNextAttackDecrementWhenClaimedDays` allow building/claiming to accelerate attacks
- Building many collectors could rapidly trigger workshop defense events (which give rewards)
**Assessment:** A player rapidly building and scrapping collector objects could theoretically farm workshop defense events faster than intended. The timer system relies on server-side time tracking though.

### Finding 4.2: Nuke Silo Cooldown Tracking
**Severity:** Medium
**File:** `en07_nukemasterscript.psc`
**Evidence:**
```papyrus
GlobalVariable Property EN07_SiloResetCooldown Auto Const mandatory
GlobalVariable Property EN07_PlayerLaunchCooldownTime Auto Const mandatory
Message Property EN07_CooldownRemaining Auto Const mandatory
Bool bIsInCooldown
Float MostRecentLaunch
```
- Silo cooldown is tracked via GlobalVariables and a per-CodeDatum boolean
- `MostRecentLaunch` stores timestamp of last launch
- If the cooldown check happens client-side before server validation, a modified client could bypass cooldown display and attempt rapid launches
**Assessment:** The actual launch mechanism requires server-side quest stage progression, so cooldown bypass would be caught server-side. The client-side display could be spoofed but wouldn't grant actual launches.

### Finding 4.3: Power Plant System Has Configurable Entropy Rates
**Severity:** Low
**File:** `powersystemdatascript.psc`
**Evidence:**
- `CONST_EntropyPlayerCountBase = 10.0` -- entropy scales with player count
- `CONST_EntropyPlayerCountMultiplier = 1.0` -- but the multiplier is 1.0 (no effect)
- Multiple TODO comments indicate the entropy scaling system was never fully implemented
- Power plants running at full power award Fusion Cores to players
**Assessment:** The incomplete entropy system means power plants may be easier to maintain than designed, giving slightly more Fusion Cores than intended. Not directly exploitable.

---

## Category 5: Item Duplication Vectors

### Finding 5.1: DefaultEmptyInvIntoLinkOnLoad Container Transfer
**Severity:** Medium
**File:** `defaultemptyinvintolinkonload.psc`
**Evidence:**
```papyrus
Auto State WaitForLoad
 Event OnLoad()
 Self.GoToState("done")
 Self.RemoveAllItems(Self.GetLinkedRef(None), False)
 EndEvent
EndState
```
- Transfers ALL items from one container to a linked container on load
- If the source container is loaded/unloaded rapidly (cell boundary manipulation), items could potentially be duplicated
- The GoToState("done") prevents re-triggering on the same load, but a cell reset would restore the WaitForLoad state
**Assessment:** Cell reset duplication is a known category of FO76 exploits. This script pattern would be vulnerable if the source container's inventory persists across cell resets while the state does not.

### Finding 5.2: Death/Corpse Item Handling
**Severity:** Medium
**File:** `tutorial_playerdeathscript.psc`, `sq_recovercorpsescript.psc`
**Evidence:**
- Player death creates a corpse object via `Alias_Corpse` with a 2-hour game timer (`questTimeGameHours = 2.0`)
- `DeathLootedMSGSent` boolean tracks whether the "looted" notification has been sent
- `DeathQuest_CorpseInaccessible` ActorValue controls corpse access
- Corpse persistence and item transfer between death and respawn creates a timing window
**Assessment:** The death/respawn cycle creates inherent timing windows. If a player's items are simultaneously "on" the corpse and "in" the respawned player's inventory during the transition, duplication could occur. This is the basis of many historical FO76 dupe exploits.

### Finding 5.3: Quest Item Spawning On Death
**Severity:** Medium
**File:** `defaultquestadddeathitemscript.psc`
**Evidence:**
```papyrus
Int Property BaseChance = 10 Auto Const
Int Property MaxChance = 100 Auto Const
Int Property BaseChanceFailureBump = 5 Auto Const
```
- Uses a pity timer system: each failed roll increases future chances by `BaseChanceFailureBump`
- The `currentChance` variable is per-quest-instance, not per-player
- If multiple players trigger the same quest instance's death handler, the pity counter increments for all of them collectively
- This could be exploited by having group members farm kills to inflate the pity timer for everyone
**Assessment:** This is more of a game design issue than a security vulnerability. The shared pity counter means coordinated groups get slightly better drop rates. Impact is limited because the base chances are designed for this.

---

## Category 6: Activation Bypasses

### Finding 6.1: RestrictedAccessScript Debug Global Override
**Severity:** High
**File:** `restrictedaccessscript.psc`
**Evidence:**
```papyrus
Group Autofill_Properties
 GlobalVariable Property DisableAccessRestrictions Auto Const mandatory
 { Debug global. When set, disables all access restrictions. }
EndGroup
```
- A single GlobalVariable can disable ALL access restrictions across every RestrictedAccessScript instance
- This is an autofill property, meaning it references a single game-wide global
- Every laser grid, hand scanner, and restricted access point inherits from this script
- If this global were set to a non-zero value (through any means), all access restrictions would be disabled
**Assessment:** This is a debug backdoor that should have been removed for production. While setting a GlobalVariable requires server-side access (console commands are disabled in FO76), if any bug allows writing arbitrary GlobalVariables, this would be the highest-value target. The fact that it's `mandatory` and `Auto Const` means it's baked into every instance.

### Finding 6.2: InstancedLaserGridScript and InstancedHandScannerScript BypassInstanceCheck
**Severity:** Medium
**File:** `instancedlasergridscript.psc`, `instancedhandscannerscript.psc`
**Evidence:**
```papyrus
Bool Property BypassInstanceCheck = False Auto Const
{ If TRUE, bypass checking if the team leader is the instance owner.
 This allows the script to be used outside of instances. Should NOT be used inside instances. }
```
- Both scripts have a `BypassInstanceCheck` property
- If set to True on an instanced laser grid/hand scanner, any team leader would gain access regardless of instance ownership
- The comment explicitly warns "Should NOT be used inside instances"
- `UseTeamLeaderAccess` combined with `BypassInstanceCheck = True` means a team leader in any team gains access
**Assessment:** If any instance-interior laser grid or hand scanner accidentally has `BypassInstanceCheck = True`, it would allow unauthorized access. This is a configuration error rather than a code vulnerability, but the existence of the bypass flag in production code increases the risk surface.

### Finding 6.3: Tripwire Owner Check Can Be Overridden
**Severity:** Low
**File:** `traptripwire.psc`
**Evidence:**
```papyrus
Bool Property triggerByEnemiesOnly = False Auto hidden
{ Used by workshop terminal to make this triggered only be enemies of the owner }
```
- The `hidden` keyword means this is set at runtime, not in the editor
- Workshop terminal scripts can flip this value
- If the ownership check uses the workshop's owner faction, and a player joins/leaves that faction, the tripwire behavior changes
**Assessment:** Limited exploitability. A player could potentially avoid triggering enemy tripwires by manipulating faction membership, but this requires specific workshop ownership scenarios.

---

## Category 7: PvP Abuse

### Finding 7.1: Raid Hack Master Attacker/Defender Team Switching
**Severity:** Medium
**File:** `raidhackmasterscript.psc`
**Evidence:**
```papyrus
Event ObjectReference.OnTriggerEnter(ObjectReference akSender, ObjectReference akActionRef)
 If akSender == Self.GetLinkedRef(LinkCustom01)
 Self.ClientHasJoinedAttackers(akActionRef)
 ElseIf akSender == Self.GetLinkedRef(LinkCustom02)
 Self.ClientHasJoinedDefenders(akActionRef)
 EndIf
EndEvent
```
- Team assignment is done by walking through trigger volumes
- No cooldown on switching teams (can walk back and forth)
- The `ClientHasJoined*` functions only apply visual effects -- actual team tracking uses synced `AttackerCount`/`DefenderCount` variables
- `TeamStatusNotification` has an empty body (stripped or unimplemented)
- No check preventing the same player from registering on both teams
**Assessment:** A player could potentially trigger both team assignments rapidly, confusing the team count tracking. The visual effect switching (AttackerEffect/DefenderEffect) without proper team validation could lead to players appearing as allies while actually being enemies.

### Finding 7.2: Bounty System Uses TODO-Marked Temporary Values
**Severity:** Low
**File:** `bountycollectionsystemrefscript.psc`
**Evidence:**
- Reward amounts and items are flagged as temporary
- The Ready/Busy state machine has the same minimal protection pattern seen elsewhere

---

## Category 8: Memory/Resource Issues

### Finding 8.1: Power Armor Display Search Radius
**Severity:** Low
**File:** `workshoppowerarmordisplayscript.psc`
**Evidence:**
```papyrus
Float Property fPowerArmorSearchRadius = 280.0 Auto Const
ObjectReference[] nearbyPowerArmors
Bool editingArray = False
```
- Searches for power armor in a 280-unit radius on each activation
- The `nearbyPowerArmors` array is rebuilt each time
- The `editingArray` boolean flag suggests awareness of concurrent access issues
- No upper bound on array size
**Assessment:** In a camp with many power armor pieces, the search could be expensive. The `editingArray` lock pattern is not atomic. Minimal real-world impact.

### Finding 8.2: Arcade Token Dispenser Sound Loop
**Severity:** Low
**File:** `arcadetokendispenserscript.psc`
**Evidence:**
```papyrus
Function PlayDispenseSound(Int aiTokensToGive)
 Int I = 0
 While I < aiTokensToGive
 TokenExchangeDispenseSFX.Play(Self as ObjectReference, "")
 Utility.Wait(0.1)
 I += 1
 EndWhile
EndFunction
```
- If `aiTokensToGive` is very large, this creates a long-running sound loop
- The `Utility.Wait(0.1)` blocks the script thread for 0.1 seconds per token
- 1000 tokens would block for 100 seconds
**Assessment:** `aiTokensToGive` is likely bounded by the amount of PreWarMoney the player has, limiting the practical impact. But the pattern of looping with Utility.Wait is inefficient.

---

## Category 9: Access Control Issues

### Finding 9.1: Workshop State Machine Has No Authentication
**Severity:** Medium
**File:** `workshopscript.psc`
**Evidence:**
```papyrus
Int Property WorkshopState00Blocked = 0 Auto Const
Int Property WorkshopState01Unowned = 1 Auto Const
Int Property WorkshopState02Owned = 2 Auto Const
Int Property WorkshopState03Contested = 3 Auto Const
Int Property WorkshopState04Claimable = 4 Auto Const
Int Property WorkshopState05Claiming = 5 Auto Const
Int Property WorkshopState06Claimed = 6 Auto Const
Int Property WorkshopState10PublicContested = 10 Auto Const
Int Property WorkshopState11PublicClaiming = 11 Auto Const
```
- Workshop state transitions are tracked via ActorValue (`WorkshopState`)
- The `EnableAutomaticPlayerOwnership = True` default means workshops become usable when the location is "cleared"
- `InitialWorkshopState` can override the initial state "for special case (e.g. testing)"
- State transitions from Claimable -> Claiming -> Claimed appear to have no server-side authentication beyond the PvP contesting system
**Assessment:** The workshop ownership system relies on the game's contesting/PvP mechanics for access control. If the PvP contesting system has edge cases (e.g., joining/leaving a server during the claiming animation), ownership could potentially be stolen without proper PvP engagement. This is consistent with known historical workshop exploits.

### Finding 9.2: Storm/Expedition Team Leader Check
**Severity:** Low
**File:** `storm_instancemaster.psc`, `objectivemodule_repelenemies.psc`
**Evidence:**
- Team leader is stored as a reference in `Alias_Leader`
- The `teamInstance` variable of type `playerteam` is set at runtime
- Expedition modules check `ModuleExpeditionTeam_RefCollAlias` for team membership
- If the team leader disconnects mid-expedition, the leader reference could become invalid
**Assessment:** Leader disconnection handling is a common source of bugs in team-based content. The script stores `leaderInstance` separately, suggesting Bethesda is aware of this risk. Low direct exploitability.

---

## Category 10: Debug Backdoors

### Finding 10.1: QuestDebuggerScript with Full Quest Manipulation
**Severity:** High (if accessible)
**File:** `questdebuggerscript.psc`
**Evidence:**
```
Function SetDebugStage(int DebugStage, bool FastFowarding = false)
Function MoveActivePlayersTo(ObjectReference RefToMoveTo)
Function AddItemToActivePlayers(form FormToAdd)
Function SetActorValueOnActivePlayers(ActorValue ActorValueToSet, float ValueToSetTo)
```
- Full quest manipulation: set arbitrary stages, teleport players, add items, set actor values
- Accessible via server console: `CQF <InstanceID> FunctionName Param1 Param2 etc.`
- The script header says "need to compile locally or run with debug archives"
- However, the compiled script IS in the production game files (it was decompiled)
**Assessment:** While the functions exist in the compiled scripts, the console is disabled in FO76 multiplayer. These functions would only be callable via the CQF console command, which should not be accessible to normal players. However, if any exploit grants console access (which has happened historically in FO76), these debug functions would be extremely dangerous -- they can add arbitrary items and set arbitrary actor values on all players in the session. The script's `DebugStageData` array provides a structured interface for jumping through quest progression, which is exactly what a quest manipulation exploit would need.

### Finding 10.2: EN07 Debug Quest with Nuke Launch Bypass
**Severity:** Critical (if accessible)
**File:** `en07_debugquestscript.psc`
**Evidence:**
```papyrus
Int Property iBypassIntroValue = 1 Auto Const
{ Debug value to bypass the missile launch intro }
Int Property iResetValue = 2 Auto Const
{ Debug value to reset the missile launch }
Int Property iScorchedSpawnValue = 3 Auto Const
{ Debug value to spawn a scorched at the specified target }
```
- Allows bypassing the entire nuke launch introduction sequence
- Can reset missile launch state (potentially clearing cooldowns)
- Can force-spawn scorched enemies
- References `EN07_SlioSGCodeEnteredIndex` -- silo access actor value
- Can mark the targeting computer with `EN07_Silo_LaunchPrepCompleteKeyword` (permanently launch-prepped)
**Assessment:** This debug quest, if triggered, would allow launching nukes without completing any prerequisites. The launch prep keyword bypass is particularly dangerous as it makes the targeting computer permanently ready. Same console-access caveat as 10.1.

### Finding 10.3: DEBUG_LVCDebugQuestScript -- Enclave Questline Skip
**Severity:** High (if accessible)
**File:** `debug_lvcdebugquestscript.psc`, `debug_en05startscript.psc`
**Evidence:**
- Sets `EN02_JoinedEnclaveValue` (joins Enclave faction)
- Sets `EN05_CompletedValue`, `EN05_MQ_CompletedValue` (marks quests as complete)
- Gives Congressional ID key and Enclave Officer uniform
- Can start any Enclave questline at any point
- `W05_MQ_004P_Crane_DuchessCooldown` -- manipulates NPC cooldown timers
**Assessment:** Complete questline bypass. Same console-access requirement as above.

### Finding 10.4: Test Scripts with Item-Granting Triggers
**Severity:** Medium
**File:** `testadditemontriggerenter.psc`
**Evidence:**
```papyrus
ScriptName TestAddItemOnTriggerEnter Extends ObjectReference Const
{ This is for debugging purposes - adds an item to the player's inventory when they pass through a trigger. }
Form Property ItemToAdd Auto Const mandatory
Int Property iItemAmount Auto Const mandatory
```
- If any trigger volumes in the game world still use this script, walking through them would grant items
- The script is `Const`, meaning all data is baked in at creation time
**Assessment:** Depends entirely on whether any world triggers reference this script. If debug triggers were left in the game world but made invisible/disabled, a player who discovers their location could potentially interact with them.

### Finding 10.5: Nuclear Winter Bot Framework Still Compiled
**Severity:** Low
**Files:** Multiple bot test scripts (spawnai.psc, spawnandkillai.psc, gatherloot.psc, exploreworld.psc, grindmonsters.psc, killallnpcs.psc, etc.)
**Evidence:**
- Complete automated QA bot framework remains in compiled scripts
- Includes: combat testing, item spawning, creature stat gathering, loot gathering
- `spawnallitems.psc` -- spawns all items in the game
- `distributeclientsfromfile.psc` -- distributes bot clients from configuration files
- All use `IsLocalPlayer()` checks (bot framework patterns)
**Assessment:** These are test automation scripts that require server console access to invoke. Their presence in production is a code hygiene issue rather than a direct vulnerability. However, they represent a rich attack surface if console access is ever gained.

---

## Architectural Observations

### Server-Side Protections (Positive Findings)
1. **Native functions for critical operations:** AddItem, RemoveItem, currency operations, quest stage changes, and combat calculations all use `Native` functions that execute server-side
2. **Network-synced variables:** The `OnSyncVariableNetworkChanged` pattern ensures state is authoritatively set by the server
3. **SyncVariable pattern for casino games:** Tumbler values and results are synced from server to all clients
4. **Player.psc Native functions:** Economy functions (`GetCapsAmount`, `GetBountyState`, etc.) are all Native, preventing client-side manipulation

### Systemic Weaknesses
1. **State machine pattern without atomicity:** The GotoState("Busy") / GotoState("Ready") pattern is used extensively but lacks true mutex protection in a multiplayer environment
2. **Boolean locks vs. state machines:** Some scripts use simple boolean flags (`activationLock`, `editingArray`) instead of the more robust GotoState pattern
3. **Debug code in production:** Approximately 50+ scripts contain debug functionality, test triggers, or developer bypass mechanisms
4. **TODO comments in production code:** Multiple scripts have unresolved TODO items affecting game balance (reward values, entropy systems)
5. **Hardcoded constants for timing:** Cooldowns, respawn timers, and attack intervals are all visible in script properties, allowing players to precisely time exploits around known windows

---

## Risk Summary Table

| # | Finding | Severity | Exploitable Client-Side? |
|---|---------|----------|--------------------------|
| 1.1 | Casino RNG partially client-visible | Medium | Requires packet manipulation |
| 1.3 | Nuke codes in script properties | Medium | Memory reading only |
| 2.1 | Keycard printer race condition | High | Yes, timing-based |
| 2.2 | LunchBox double-activation | Medium | Yes, timing-based |
| 2.3 | OnActivateAddItem boolean lock | Medium | Yes, timing-based |
| 3.1 | CustomItem bypasses instantiation rules | High | Requires quest manipulation |
| 4.1 | Workshop attack timer farming | Medium | Yes, gameplay manipulation |
| 5.1 | Container transfer on load | Medium | Cell boundary manipulation |
| 5.2 | Death/corpse item timing | Medium | Yes, timing-based |
| 6.1 | DisableAccessRestrictions global | High | Requires GlobalVariable write |
| 6.2 | BypassInstanceCheck flag | Medium | Configuration error risk |
| 7.1 | Raid team switching no cooldown | Medium | Yes, trigger volume abuse |
| 9.1 | Workshop state no authentication | Medium | PvP edge cases |
| 10.1 | QuestDebugger full manipulation | High* | Requires console access |
| 10.2 | EN07 Debug nuke bypass | Critical* | Requires console access |
| 10.3 | Enclave questline skip | High* | Requires console access |
| 10.4 | Test trigger item grants | Medium | If triggers exist in world |

*These findings are Critical/High IF console access is obtained through any means. They represent force-multiplier vulnerabilities.

---

## Recommendations for Bethesda

1. **Remove debug scripts from production builds:** Scripts like `questdebuggerscript.psc`, `en07_debugquestscript.psc`, and all test framework scripts should not be compiled into production ESM files
2. **Replace boolean locks with state machines:** All `activationLock` patterns should use GotoState for multiplayer safety
3. **Remove DisableAccessRestrictions global:** This debug backdoor should be removed entirely from production
4. **Resolve TODO items:** Temporary reward values and incomplete entropy systems should be finalized
5. **Add server-side validation for keycard printing:** The empty IsLocalPlayer() block suggests missing server logic
6. **Audit BypassInstanceCheck usage:** Verify no instanced content has this flag incorrectly set to True
7. **Add team-switching cooldowns:** The raid hack system should prevent rapid team switching

---

*This analysis is based solely on decompiled Papyrus scripts and does not include any testing against live servers. All findings are theoretical and require practical verification. This document is intended for responsible disclosure to Bethesda Game Studios.*
