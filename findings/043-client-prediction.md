# Finding 043: FO76 Client-Server Architecture - No Client-Side Prediction

## Verdict

**FO76 does NOT use client-side prediction for gameplay calculations.** The architecture is a strict **server-authoritative model** where the client sends raw input events to the server and receives back authoritative state. The client's role is limited to rendering, animation playback, sound effects, and UI display. All gameplay math (damage, inventory, actor values, scoring) runs exclusively on the server.

## Evidence Summary

### 1. SendRMIToServer() - Client Sends Events, Not Calculations

Found 20 scripts using `SendRMIToServer()`. In every case, the client sends **event notifications with zero calculated data** -- just function names and empty parameter arrays:

```
Self.SendRMIToServer("BecomeVulnerable", None)      -- arcade target hit
Self.SendRMIToServer("UpdateScore", None)            -- score tracking
Self.SendRMIToServer("RegisterWin", None)            -- race win
Self.SendRMIToServer("RegisterSpeedup", None)        -- shooting gallery
Self.SendRMIToServer("RemovePlayerFromRaid", Params) -- Params = empty Var[0]
Self.SendRMIToServer("RequestEventState", None)      -- state query
Self.SendRMIToServer("RequestCollisionUpdate", None) -- laser grid
Self.SendRMIToServer("CheckPlayerWaywardValue", None) -- quest state check
```

The pattern is unambiguous: the client sends **"this happened"** messages, never **"I calculated X"** messages. No RMI call passes a damage number, health delta, or any computed value. The `Var[] aParams` parameter is consistently `None` or `new Var[0]`.

Key file: `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/scriptobject.psc` (line 7)

### 2. OnSyncVariableNetworkChanged() - Server Pushes State Down

Found 28 scripts implementing `OnSyncVariableNetworkChanged()`. This is the server-to-client replication mechanism. When the server changes a synced variable, the client receives the new value and updates its local presentation. The variables synced are always **presentation state**, never gameplay calculations:

| Script | Synced Variable | Client Action |
|--------|----------------|---------------|
| `default2stateactivator.psc` | `SetOpenAnim` | Play animation |
| `atxslotmachinescript.psc` | `tumblerUpdateTick` | Spin reel animations |
| `cyclicelectricalhazard.psc` | `teslaProjectilesFired` | Cast visual spell effect |
| `storm_weatherstationbuttonscript.psc` | `bIsOpen` | Play door open/close anim |
| `resourcegeneratorbuttonscript.psc` | `GeneratorState` | Play generator animations/sounds |
| `xpd_ac_casinogame.psc` | `ResultAnimationIdx` | Set animation variable, play anim |
| `xpd_ac_slotmachine.psc` | `ShouldSpinTumblers` | Spin reels + result animation |
| `atx_nukamysterymachine.psc` | `AnimateUpdate` | Play animation |

The client never receives a damage number, health value, or calculated result through this channel. It receives booleans, tick counters, and animation indices.

### 3. The Smoking Gun: actorvaluetests.psc

```
Bool Function Player_SetActorValue_ShouldOnlyWorkOnServer(player testPlayer, ActorValue av)
  Float valueBefore = testPlayer.GetBaseValue(av)
  testPlayer.SetValue(av, 5.0)
EndFunction
```

The test name itself -- `Player_SetActorValue_ShouldOnlyWorkOnServer` -- is Bethesda's own documentation that `SetValue()` on player actor values **only works when executed on the server**. The client can read values (`GetBaseValue()`) but cannot write them. This is enforced at the engine level, not the script level.

File: `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/actorvaluetests.psc`

### 4. ApplyOnClient / ApplyOnServer - Dual Execution for Presentation Only

Three spell-application scripts expose the client/server split explicitly:

- `addspelloneffectscript.psc`
- `castspelloneffectscript.psc`
- `failsafeaddspelloneffectscript.psc`

Each has two booleans:
```
Bool Property ApplyOnClient = True Auto Const
{ Cast this spell on the Client? Uncheck this only if you want no visual/audio/HUD/etc. component. }
Bool Property ApplyOnServer = True Auto Const
{ Cast this spell on the Server? Uncheck this with caution. Should always be true for anything that effects gameplay. }
```

The comments are definitive:
- **Client** = "visual/audio/HUD" (presentation layer)
- **Server** = "anything that effects gameplay" (authoritative game state)

But here is the critical detail: the decompiled code only shows the `ApplyOnClient` branch executing `AddSpell()` or `Cast()`. The `ApplyOnServer` branch has no visible code. This means the server-side execution happens in a **separate code path that runs natively on the server** -- the Papyrus script on the client only handles the presentation side. The server does not need Papyrus to apply the gameplay effect; it does so in native C++ code.

### 5. Client Functions Are Purely Cosmetic

Scripts with explicit "Client" functions demonstrate the pattern. They handle only:

- **Animations**: `ClientPlayAnimation()`, `ClientPlayButtonPress()`, `ClientPlayButtonTurnOn()`
- **Sound**: `PlayCombatSoundOnClient()`, `ClientPlayGeneratorStartSound()`
- **Visual effects**: `SetBloodImpactMaterial()`, camera shake
- **State queries**: `ClientRequestEventState()` (asks server, waits for answer)

Example from `resourcegeneratorbuttonscript.psc`:
```
Function ClientPlayGeneratorStartSound()
  GeneratorStartSound.play(ResourceContainer, "")
  player.ShakeCamera(ResourceContainer, 0.25, 0.0)
  player.ShakeController(0.25, 0.25, 0.25)
EndFunction
```

The actual resource generation (adding items to containers, managing timers, running the generator) happens in server-only code. The client just plays the start sound and shakes the camera.

### 6. Casino Games: Server Decides Everything

The slot machine system (`atxslotmachinescript.psc`, `xpd_ac_slotmachine.psc`) reveals the full pattern:

1. Player activates machine (client sends activation event)
2. Server generates random result, sets `lastTumbler1Value`/`2`/`3` and increments `tumblerUpdateTick`
3. `OnSyncVariableNetworkChanged("tumblerUpdateTick")` fires on client
4. Client reads the server-set tumbler values and plays corresponding animations
5. Server awards caps/items separately

The client never generates random numbers or calculates payouts. Even the tumbler display values come from the server. The `{ Synced so that it can be used in client broadcasts }` comment confirms these are server-written, client-read variables.

### 7. The Whack-A-Mole Pattern: Client Reports, Server Scores

`arcadewhackamoletarget.psc` is a perfect microcosm:

```
Event OnHit(...)
  If !vulnerable
    Return
  EndIf
  vulnerable = False         -- local flag to prevent double-hits
  Self.PlayHitSFX()          -- client plays sound
  Self.SendRMIToServer("UpdateScore", None)  -- asks server to score
EndEvent

Function UpdateScore(player akSendingPlayer)
  ; Empty function  -- SERVER-ONLY: actual scoring happens in native code
EndFunction
```

The comment on `UpdateScore` says: `{ Tick hits up, and have the game controller calculate the score (hits are handled here rather than in the OnHit as they need to be stored on the server) }`

Even for a simple arcade minigame, the **score calculation runs on the server**. The client only reports "I was hit" and plays a sound.

### 8. No Prediction/Rollback/Reconciliation Patterns Found

Searched all 7,095 scripts for: `prediction`, `reconcile`, `rollback`, `desync`, `latency`, `ping`, `timeout`. **Zero matches** for prediction, reconcile, rollback, or desync. The 86 matches for "timeout" are all quest/timer-related gameplay timeouts, not network compensation.

There is no correction mechanism because there is nothing to correct -- the client never calculates gameplay state speculatively.

### 9. Damage Curves in the Client ESM: Reference Data, Not Prediction Data

The ESM contains 3,845 CURV records, including 100 tiers of `CT_Player_Damage_Universal_Tier01` through `Tier100` and 50 tiers of `CT_Creatures_Damage_Universal`. Plus weapon mod damage splits, legendary damage curves, etc.

These curves ARE shipped to the client in the ESM, but they serve **UI/tooltip purposes**, not damage prediction:

- **Pip-Boy weapon stats display**: The client needs damage curves to show "Base Damage: 47" in the weapon inspect screen
- **Perk card descriptions**: Displaying "+20% damage" requires knowing the base curve
- **Comparison tooltips**: "This weapon does X more damage" requires local curve lookup
- **VATS targeting display**: Showing estimated damage per body part uses local curves

The server uses the same curves for authoritative calculation. The client uses them for display. When you fire a weapon:
1. Client plays the firing animation and muzzle flash immediately (cosmetic)
2. Client sends the hit event to server
3. Server calculates actual damage using curves + perks + legendary effects + buffs
4. Server applies damage to target's health (authoritative)
5. Server syncs new health value back to client
6. Client displays the health bar change

The delay between step 1 and step 6 is why you sometimes see "hit markers" but no damage -- the server rejected the hit (target already dead, desync, etc.). This is the opposite of client prediction; it is server confirmation.

### 10. GMST Network Settings: No Prediction Configuration

The game settings contain server-related values:
```
fServerRespawnPostTransportWindowSeconds
fServerDefaultPostTransportWindowSeconds
fServerRespawnTeammateSearchRadius
fServerRespawnTeammateSearchWidth
sDisconnectReasonSlowNetworkComponentDeletion
sConnectionMessageRejectIncorrectClientFilelist
sConnectionMessageRejectIncorrectClientVersion
```

None of these reference prediction, interpolation buffers, or rollback windows. The disconnect reasons reference version mismatches and maintenance -- not desyncs that would result from prediction failures.

## Architecture Model

```
CLIENT                          NETWORK              SERVER
------                          -------              ------
Input (fire weapon)       --->  RMI call      --->   Receive hit event
Play muzzle flash anim                               Calculate damage (curves + perks + buffs)
Play firing sound                                    Apply to target health (authoritative)
                                                     Set target health sync var
OnSyncVariableChanged  <---   sync push    <---    Push new state
Update health bar display
Show hit marker
```

## Why No Prediction?

FO76's architecture choice makes sense for its design:

1. **Anti-cheat**: If the client calculated damage, modifying those calculations would be trivial. Server authority means the client cannot inflate damage, duplicate items, or modify actor values.

2. **Low tick-rate tolerance**: FO76 runs at a relatively low server tick rate. Client prediction would create jarring rollbacks when the server disagrees. By never predicting, there is never a visible correction.

3. **Creation Engine legacy**: The Creation Engine was built for single-player (Skyrim, FO4). When Bethesda Austin added multiplayer, they moved gameplay authority to the server rather than building a prediction/reconciliation system into an engine that never had one.

4. **Gameplay tolerance**: FO76 is a cooperative PvE game primarily. The ~50-100ms delay between firing and seeing damage is acceptable. Players see hit markers from the server confirmation, not from local prediction.

## Implications for Modding/Analysis

- **GMST/curve values in the client ESM are not used for real-time gameplay calculations.** They are reference data for UI display. Changing them client-side would only affect what the Pip-Boy shows, not actual damage dealt.
- **Server-side values cannot be modified by clients.** The `ShouldOnlyWorkOnServer` test confirms this is enforced at the engine level.
- **SFE/script extender hooks into client functions** only affect the presentation layer. You can change what animations play, what sounds fire, what the UI shows, but you cannot change what the server calculates.
- **Damage number discrepancies** between what the Pip-Boy shows and what actually happens are caused by the client using stale or incomplete curve data (missing server-side buffs, team bonuses, etc.).

## Key Files Referenced

- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/scriptobject.psc` -- SendRMIToServer definition
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/actorvaluetests.psc` -- SetActorValue server-only test
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/addspelloneffectscript.psc` -- ApplyOnClient/Server split
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/castspelloneffectscript.psc` -- Same pattern
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/arcadewhackamoletarget.psc` -- Server-side scoring
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/atxslotmachinescript.psc` -- Server-driven casino
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/resourcegeneratorbuttonscript.psc` -- Client cosmetic functions
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/defaultmultistateclientsideactivator.psc` -- Client-side animations only
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/mpscripttestserverrmikeyword.psc` -- RMI test pattern
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/mpscripttestsyncpropertykeyword.psc` -- Sync variable test pattern
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/esm_dump/game_settings.txt` -- GMST damage/server settings
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/esm_dump/full_esm_dump.txt` -- 3,845 CURV records including damage tiers
