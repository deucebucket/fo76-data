# 080: Fallout 76 Complete Execution Chains

## Methodology

Traced execution chains from trigger event through Papyrus scripts to native C++ function calls, mapping SFE addresses where available. Sources: 7,095 decompiled scripts, 293 SFE signatures, ESM dump data.

**Key architectural note:** FO76 is a client-server game. The Papyrus VM runs on the **server** for all gameplay logic. The client handles rendering, input, and prediction. Native functions marked "Native" in .psc files are C++ implementations in the server executable. SFE addresses are from the **client** executable (Fallout76.exe), which shares the same codebase but runs a subset of game logic for prediction/rendering.

---

## CHAIN 1: COMBAT (Weapon Fire to Death)

### 1.1 Trigger: Player Presses Fire

```
INPUT EVENT (Client-side)
  g_inputEventTable          @ 0x05A98AB0 (RelocPtr, GameInput.cpp)
  g_playerControls           @ 0x05A13268 (RelocPtr, GameInput.cpp)
  CreatePlayerControlHandlers @ 0x00F44BA0 (Hooks_Input.cpp)
  |
  v
CLIENT PREDICTION (Client-side)
  Input → PlayerControls → WeaponFireHandler
  Client plays animation, spawns projectile prediction
  |
  v
SERVER VALIDATION (Server-side)
  Engine validates fire action, ammo check, weapon condition
  No Papyrus script handles the fire trigger itself -- this is pure C++
```

**Side:** Client-side input capture, server-side validation

### 1.2 OnPlayerFireWeapon Event

```
ENGINE FIRES EVENT (Server-side)
  SendPapyrusEvent              @ 0x01374E90 (PapyrusVM.h)
  |
  v
Actor::OnPlayerFireWeapon(Form akBaseObject)    [actor.psc:120]
  -- Empty virtual event, dispatched to all scripts registered on the actor
  -- ActiveMagicEffect::OnPlayerFireWeapon also receives this [activemagiceffect.psc:151]
  |
  v
MAGIC EFFECT SCRIPTS (if weapon has enchantment):
  DLC01WeapOnFireEffect::OnAnimationEvent       [dlc01weaponfireeffect.psc]
    - Listens for animation event (e.g., "weaponFire")
    - Calls: Spell.Cast(akSource, None)           [spell.psc: Native]
    - SFE: No direct address; Cast() is a native Papyrus function
           dispatched through Impl_Invoke @ 0x02732500
```

**Native functions called:**
| Function | Declaration | SFE Address | Side |
|----------|------------|-------------|------|
| `Weapon.Fire(ObjectReference, Ammo, Bool)` | weapon.psc:5 | Via Impl_Invoke @ 0x02732500 | Server |
| `Spell.Cast(ObjectReference, ObjectReference)` | spell.psc:5 | Via Impl_Invoke @ 0x02732500 | Server |
| `Actor.GetEquippedWeapon(Int)` | actor.psc:629 | Via Impl_Invoke @ 0x02732500 | Server |

### 1.3 Projectile Hit / Damage Calculation

```
ENGINE HIT DETECTION (Server-side, pure C++)
  Projectile trajectory → collision check → hit target determined
  |
  v
DAMAGE FORMULA (Server-side, pure C++)
  Base Weapon Damage
  * Perk Multipliers (via Perk Entry Points - C++ perk system)
  * Legendary Effect Multipliers
  * Sneak Attack Multiplier
  * Critical Hit Multiplier
  * VATS accuracy
  |
  v
ARMOR REDUCTION (Server-side, pure C++)
  Damage Resistance check:
    Debug.GetNormalizedDamageResistance(target)    [debug.psc:209] -- Native
    Debug.GetNormalizedEnergyResistance(target)    [debug.psc:135] -- Native
    Debug.GetNormalizedRadiationResistance(target) [debug.psc:173] -- Native
    Debug.GetNormalizedPoisonResistance(target)    [debug.psc:37]  -- Native
    Debug.GetNormalizedFireResistance(target)      [debug.psc:215] -- Native
    Debug.GetNormalizedCryoResistance(target)      [debug.psc:217] -- Native
  |
  These debug natives EXPOSE the internal DR calculation to scripts
  Actual DR formula is engine-internal C++
  |
  v
APPLY DAMAGE (Server-side)
  ObjectReference.DamageValue(Health, finalDamage)  [objectreference.psc:60] -- Native
  -- or via direct C++ ActorValue modification
```

### 1.4 Legendary Weapon Effects on Hit

```
ON HIT EVENT (Server-side)
  LegendaryMagicEffectEventSenderScript::OnHit()  [legendarymagiceffecteventsenderscript.psc:68]
    akTarget, akAggressor, akSource, akProjectile, abPowerAttack, abSneakAttack, etc.
    |
    v
  SendLegendaryMagicEffectEvent(target, aggressor, iEventType_OnHit=3)
    |
    v
  PlayerLegendaryItemScript::SendLegendaryMagicEffectEvent(kArgs)  [playerlegendaryitemscript.psc:64]
    Self.SendCustomEvent("playerlegendaryitemscript_LegendaryMagicEffectEvent", kArgs)
    |
    SFE: SendCustomEvent_Internal @ 0x013D9340
    |
    v
  LegendaryMagicEffectEventListenScript::HandleEvent()  [legendarymagiceffecteventlistenscript.psc:22]
    -- Dispatched to all registered legendary effect listeners
    |
    v
  EXAMPLE: ModLegendaryConsecutiveHitsScript  [modlegendaryconsecutivehitsscript.psc]
    - Tracks consecutive hits on same target
    - Calls: Actor.SetValue(ConsecutiveHitsAV, count)   [objectreference.psc:288] -- Native
    - Calls: Actor.GetValue(ConsecutiveHitsAV)           [objectreference.psc:588] -- Native
```

**Native functions in hit chain:**
| Function | Declaration | Side |
|----------|------------|------|
| `ObjectReference.DamageValue(ActorValue, Float)` | objectreference.psc:60 | Server |
| `ObjectReference.SetValue(ActorValue, Float)` | objectreference.psc:288 | Server |
| `ObjectReference.GetValue(ActorValue)` | objectreference.psc:588 | Server |
| `ObjectReference.RestoreValue(ActorValue, Float)` | objectreference.psc:380 | Server |
| `ObjectReference.ModValue(ActorValue, Float)` | objectreference.psc:468 | Server |
| `Actor.HasActiveMagicEffect(MagicEffect)` | actor.psc:346 | Server |
| `Actor.HasMagicEffectWithKeyword(Keyword)` | actor.psc:544 | Server |
| `Form.HasKeyword(Keyword)` | form.psc:5 | Server |

### 1.5 Perk Application

```
PERK ENTRY POINT SYSTEM (Server-side, pure C++)
  Engine evaluates all perk entry points automatically during damage calc
  |
  Perk.OnEntryRun(entryID, target, owner)          [perk.psc:9]
  -- Papyrus event fired when a perk entry executes
  -- Most perk effects are PURE C++ (Mod Incoming Damage, Mod Attack Damage, etc.)
  -- Only perks with scripted effects trigger Papyrus
  |
  EpicCreaturePerk is applied to legendary creatures:
    EpicOutgoingDamageMultAV -- scales creature damage output
    EpicIncomingDamageMultAV -- scales damage input (damage resistance)
    Both set by EpicCreaturesScript during creature spawn
```

### 1.6 HP Change and Death Check

```
HP MODIFICATION (Server-side)
  Engine applies final damage to Health ActorValue
  |
  v
HEALTH THRESHOLD CHECK - LEGENDARY MUTATE (Server-side)
  AbLegendaryScript::OnEffectStart()                [ablegendaryscript.psc]
    Properties: Health AV, HealthThreshhold, LegendaryPowerUp spell
    When health drops below threshold → adds LegendaryPowerUp spell
    → creature "mutates" (heals to full, rank up FX)
    |
    v
  EpicCreatureRestoreHealthEffectScript             [epiccreaturerestorehealtheffectscript.psc]
    - Trigger: AbEpicCreature_RestoreHealth_Trigger spell
    - Removes trigger ability, casts AbEpicCreature_RestoreHealth
    - Plays LegendaryPowerUpMsg message
    - Plays PowerUpSound
    |
    v
  Native: Actor.ResetHealthAndLimbs()                [actor.psc:416] -- Native
  |
  v
DEATH CHECK (Server-side)
  Health <= 0 → Engine fires events:
    Actor::OnDying(Actor akKiller)                    [actor.psc:222]
    Actor::OnDeath(Actor akKiller)                    [actor.psc:232]
  |
  v
POST-DEATH PROCESSING:
  Actor.Kill(Actor akKiller)                         [actor.psc:434] -- Native
  Actor.KillSilent(Actor akKiller)                   [actor.psc:432] -- Native
  Actor.Dismember(bodyPart, forceExplode, ...)       [actor.psc:430] -- Native
  Actor.TriggerCriticalEffect(shader, stage, ...)    [actor.psc:310] -- Native
  |
  v
LEGENDARY DEATH EXPLOSION:
  AbLegendaryExplodeScript::OnDeath()                [ablegendaryexplodescript.psc]
    - Timer: ExplosionDelay seconds
    - Places DeathExplosion at corpse location
    - Native: ObjectReference.PlaceAtMe(explosion, ...)  [objectreference.psc:448]
```

### Complete Combat Chain Summary

```
[Client] Button Press → g_playerControls @ 0x05A13268
    → [Server] Weapon.Fire() → Native C++ projectile spawn
    → [Server] C++ hit detection → collision
    → [Server] C++ damage formula (base * perks * legendary * sneak * crit)
    → [Server] C++ armor reduction (DR/ER/RR formulas)
    → [Server] DamageValue(Health, finalDmg) → Native
    → [Server] OnPlayerFireWeapon event → SendPapyrusEvent @ 0x01374E90
    → [Server] Legendary OnHit → SendCustomEvent_Internal @ 0x013D9340
    → [Server] Health check → legendary mutate or death
    → [Server] OnDying/OnDeath → quest tracking, loot generation
```

---

## CHAIN 2: BOT FRAMEWORK (SetAIDriven to Combat)

### 2.1 Trigger: Bot Initialization

```
BOT STARTUP (Server-side)
  AutoTestClient:GrindMonsters::StartTest()          [grindmonsters.psc:9]
    |
    v
  Step 1: Load ammo form
    Game.GetFormFromFile(127606, "SeventySix.esm")    [game.psc:163] -- Native
    LookupFormByID @ 0x00152C90
    |
    v
  Step 2: Distribute clients
    autotestclient:common.DistributeClients()
    Utility.Wait(10.0)                                [utility.psc:107] -- Native
    |
    v
  Step 3: Set AI driven mode
    Player.SetAIDriven(True)                          [player.psc:77] -- Native
    -- Engine takes over player movement via AI packages
    -- Player character now responds to PathToReference, combat AI, etc.
    |
    v
  Step 4: Enable sprinting
    Actor.SetWantSprinting(True)                      [actor.psc:330] -- Native
```

**Side:** All server-side. SetAIDriven flips an engine flag making the player actor behave like an NPC.

### 2.2 Target Acquisition Loop

```
MAIN LOOP (Server-side)
  While !isTestComplete:
    |
    v
  Step 1: Find target
    Actor.FindRandomCombatTarget(10000.0)              [actor.psc:602] -- Native
    -- Engine queries the combat target list within 10000 unit radius
    -- Returns hostile actor or None
    -- Uses engine's detection/LOS system internally
    |
    v
  Step 2: Path to target (if found)
    Actor.PathToReference(target, 1.0)                 [actor.psc:428] -- Native
    -- 1.0 = walk/run percent (100% run)
    -- Engine's navmesh pathfinding system
    -- Blocks until arrival or failure
    |
    v
  Step 3: Fight sequence
    GrindMonsters::Fight(akTarget)                     [grindmonsters.psc:38]
      Player.SetAIDriven(False)                        -- Re-enable player controls
      -- Wait loop: 100 iterations * 0.01s = 1 second max
      While i < 100 && target != None && !target.IsDead():
        Utility.Wait(0.01)                             [utility.psc:107] -- Native
        Actor.IsDead()                                 [actor.psc:512] -- Native
      EndWhile
      -- Refill ammo
      FillAmmo():
        Game.GetLocalPlayer()                          [game.psc:181] -- Native
          g_player @ 0x05ADD3D8
        ObjectReference.GetItemCount(ammoForm)         [objectreference.psc:652] -- Native
      Player.SetAIDriven(True)                         -- Resume AI control
```

### 2.3 ExploreWorld Bot Chain

```
EXPLORE BOT (Server-side)
  AutoTestClient:ExploreWorld::StartTest()             [exploreworld.psc:20]
    |
    v
  Step 1: Initialize location data
    24 locations hardcoded with FormIDs (map markers, door pairs)
    |
    v
  Step 2: Enable AI
    CheckAndSetPlayerAIDriven():                       [exploreworld.psc:181]
      Actor.GetPlayerControls()                        [actor.psc:36] -- Native
      Player.SetAIDriven(True)                         [player.psc:77] -- Native
      Actor.SetWantSprinting(True)                     [actor.psc:330] -- Native
    |
    v
  Step 3: Visit locations loop
    For each destination:
      VisitLocation(name, mapMarker, interiors):       [exploreworld.psc:188]
        |
        v
      PathToLocation(formId):                          [exploreworld.psc:156]
        Game.GetFormFromFile(formId, "SeventySix.esm") [game.psc:163] -- Native
          LookupFormByID @ 0x00152C90
        Actor.PathToReference(targetRef, 1.0)          [actor.psc:428] -- Native
        -- Retries up to MaxPathRetries=5
        |
        v
      VisitInterior(doorIn, doorOut):                  [exploreworld.psc:137]
        doorRef.Activate(player, True)                 -- Native (objectreference)
        Utility.Wait(150.0)                            -- 2.5 minutes wait inside
        exitDoor.Activate(player, False)
        Utility.Wait(40.0)                             -- 40 seconds wait
    |
    v
  Step 4: Cleanup
    CheckAndClearPlayerAIDriven():                     [exploreworld.psc:174]
      Player.SetAIDriven(False)
      Actor.SetWantSprinting(False)
```

### Bot Framework Native Function Map

| Function | Declaration | SFE Address | Side |
|----------|------------|-------------|------|
| `Player.SetAIDriven(Bool)` | player.psc:77 | Via Impl_Invoke @ 0x02732500 | Server |
| `Actor.PathToReference(ObjectReference, Float)` | actor.psc:428 | Via Impl_Invoke @ 0x02732500 | Server |
| `Actor.FindRandomCombatTarget(Float)` | actor.psc:602 | Via Impl_Invoke @ 0x02732500 | Server |
| `Actor.SetWantSprinting(Bool)` | actor.psc:330 | Via Impl_Invoke @ 0x02732500 | Server |
| `Actor.GetPlayerControls()` | actor.psc:36 | Via Impl_Invoke @ 0x02732500 | Server |
| `Actor.IsDead()` | actor.psc:512 | Via Impl_Invoke @ 0x02732500 | Server |
| `Actor.StartCombat(Actor, Bool)` | actor.psc:326 | Via Impl_Invoke @ 0x02732500 | Server |
| `Game.GetFormFromFile(Int, String)` | game.psc:163 | LookupFormByID @ 0x00152C90 | Server |
| `Game.GetLocalPlayer()` | game.psc:181 | g_player @ 0x05ADD3D8 | Server |
| `ObjectReference.Activate(ObjectReference, Bool)` | objectreference (native) | Via Impl_Invoke @ 0x02732500 | Server |
| `Utility.Wait(Float)` | utility.psc:107 | Via Impl_Invoke @ 0x02732500 | Server |

---

## CHAIN 3: QUEST (Daily Quest from Start to Finish)

### 3.1 Trigger: Quest Start via Story Manager

```
QUEST START (Server-side)
  Player enters trigger zone / activates terminal / Story Manager event
  |
  v
ENGINE QUEST SYSTEM:
  Story Manager evaluates conditions
  Creates QuestInstance
  QuestInstance.psc defines QuestStage struct:        [questinstance.psc]
    QuestInstance QuestToSet
    Int StageToSet
  |
  v
DAILY QUEST INITIALIZATION:
  DefaultDailyQuestScript extends QuestInstance       [defaultdailyquestscript.psc]
    Properties:
      SQ_RegionDailyQuestKeyword -- Autofill keyword
      DailyQuestDoneAV -- ActorValue with timestamp
      StartingStage_DailyQuestKeyword -- stage for daily starts
      StartingStage_OtherKeyword -- stage for first-time starts
    |
    Engine sets DailyQuestDoneAV on all active players with current timestamp
```

### 3.2 Daily Quest Target/Kill Tracking

```
DAILY QUEST SETUP (Server-side)
  DailyQuestScript extends QuestInstance              [dailyquestscript.psc]
    |
    v
  Step 1: Roll target type
    TargetData[] -- array of TargetDatum structs
      Each has: TargetKeyword, MinLevel, MaxLevel, Count, Variability, Difficulty
    Random selection based on player level range
    |
    v
  Step 2: Roll implement (weapon type)
    ImplementData[] -- array of ImplementDatum structs
      Each has: ImplementKeyword, MinLevel, MaxLevel, RequiredPerk, Difficulty
    Random selection, checks Actor.HasPerk()          [actor.psc:540] -- Native
    |
    v
  Step 3: Calculate reward tier
    rewardValue = CountPoints + TargetDifficulty + ImplementDifficulty
    If rewardValue <= easyReward(6):  low reward
    If rewardValue <= mediumReward(12): medium reward
    Else: high reward
    |
    v
  Step 4: Set objectives
    Engine-internal SetObjectiveDisplayed()
    Text replacement via objective variables (VictimCountTextVar, VictimsRequiredTextVar)
```

### 3.3 Kill Tracking

```
KILL MANAGER (Server-side)
  DefaultQuestOnKillManager extends QuestInstance     [defaultquestonkillmanager.psc]
    |
    v
  REGISTRATION:
    When player becomes "active" on quest:
      RegisterForKill or RegisterForKillImmediate events
    |
    v
  ON KILL EVENT:
    Actor::OnKill(Actor akVictim)                     [actor.psc:174]
    -- or --
    Actor::OnKillImmediate(Actor akVictim)            [actor.psc:170]
    |
    v
  VALIDATION:
    Check VictimKeyword: victim.HasKeyword(VictimKeyword)  [form.psc:5] -- Native
    Check VictimFaction: victim faction membership
    Check VictimRace: victim race
    Check WeaponKeyword: equipped weapon keyword
    |
    v
  INCREMENT:
    CountVictims += 1
    If CountVictims >= VictimsRequired:
      Engine SetStage(StageToSet)
    |
    v
  ADDITIONAL THRESHOLDS:
    VictimCountData[] checked for intermediate stages/objectives
    ObjectiveToDisplay refreshed each kill (shows "Kill X (3/5)")
```

### 3.4 Quest Completion and Rewards

```
COMPLETION (Server-side)
  Stage reaches StageToSet (e.g., 9999)
  |
  v
  Engine processes quest stage fragments
  Reward stage triggers:
    ObjectReference.AddItem(rewardForm, count, silent, ...)  [objectreference.psc:838] -- Native
    Player.IncrementStat("Quests Completed", 1)              [player.psc:203] -- Native
  |
  v
  XP REWARD:
    Player XPSource_QuestComplete = 1                         [player.psc:5]
    Player XPSource_QuestReward = 3                           [player.psc:7]
  |
  v
  DAILY QUEST CLEANUP:
    DailyQuestDoneAV timestamp prevents re-triggering same day
    Quest shutdown, aliases cleared
```

### Quest Chain Native Functions

| Function | Declaration | Side |
|----------|------------|------|
| `Form.HasKeyword(Keyword)` | form.psc:5 | Server |
| `Form.HasKeywordInFormList(FormList)` | form.psc:32 | Server |
| `Actor.HasPerk(Perk)` | actor.psc:540 | Server |
| `Actor.GetLevel()` | actor.psc:24 | Server |
| `ObjectReference.AddItem(Form, Int, Bool, ...)` | objectreference.psc:838 | Server |
| `Player.IncrementStat(String, Int)` | player.psc:203 | Server |
| `Player.QueryStat(String)` | player.psc:109 | Server |
| `Utility.RandomInt(Int, Int)` | utility.psc:131 | Server |

---

## CHAIN 4: LEGENDARY ITEM GENERATION

### 4.1 Trigger: Enemy Spawn - Epic Creature Check

```
CREATURE SPAWN (Server-side)
  Actor loads into world → engine fires OnLoad
  |
  v
  EpicCreatureEffectScript::OnEffectStart()           [epiccreatureeffectscript.psc]
    -- Attached as ability spell to creatures
    Properties: SQ_EpicCreatures quest, AbConvertLegendaryCreature spell
    |
    v
  EpicCreaturesScript (SQ_EpicCreatures quest)        [epiccreaturesscript.psc]
    |
    v
  EPIC ROLL:
    Formula: (Base + ActorLevel * ActorLevelMult) * RegionMult
    Base = 1.0, ActorLevelMult = 0.04, MaxChance = 5.0
    MinActorLevel = 10 (below this, no legendary possible)
    |
    Check EpicCreatureDisallowedKeywords formlist
    Actor.HasKeywordInFormList(disallowed)              [form.psc:32] -- Native
    |
    v
  RANK DETERMINATION:
    EpicRankData[] array (one per rank):
      Rank1-5 creature chances (GlobalVariable percentages)
      MinLevelRequired, MaxLevelAllowed
      HealthMult, OutgoingDamageMult
      HordeChance, NemesisHordeChance
    |
    Roll: Utility.RandomInt() or Game.GetDieRoll()
    |
    v
  APPLY RANK:
    SetRank logic (with spinlock for thread safety):
      Actor.SetValue(EpicRankAV, rank)                 [objectreference.psc:288] -- Native
      Actor.AddKeyword(EpicCreatureRankXKeyword)       -- via objectmod
      |
      Health scaling:
        Cache: Actor.SetValue(EpicInitialBaseHealthAV, baseHealth)
        If baseHealth < MinStartingHealth(100), set to 100
        New health = baseHealth * HealthMult
        Actor.SetValue(Health, newHealth)
      |
      Damage scaling:
        Actor.SetValue(EpicOutgoingDamageMultAV, OutgoingDamageMult)
      |
      Name change:
        Add to NameCollection (e.g., "Legendary [CreatureName]")
        Unless: Actor.HasKeyword(IgnoreLegendaryNameKeyword)
      |
      Apply abilities:
        EpicRankAbilitiesData[] checked against rank and keywords
        Actor.AddSpell(ability)                        [actor.psc:516] -- Native
      |
      Apply mods:
        EpicRankModData[] checked against rank and keywords
      |
      Add legendary item ability:
        Actor.AddSpell(AddLegendaryItemAbility)        [actor.psc:516] -- Native
      |
      Add health restore trigger:
        Actor.AddSpell(AbEpicCreature_RestoreHealth_Trigger) [actor.psc:516] -- Native
```

### 4.2 Forced Legendary (Quest/Event Bosses)

```
FORCED LEGENDARY (Server-side)
  DefaultLegendaryCreatureRef extends ObjectReference   [defaultlegendarycreatureref.psc]
    bForceLegendary = True
    LegendaryRank = 0 (random) or 1-3 (forced)
    |
    v
  DefaultForceLegendaryAlias extends ReferenceAlias    [defaultforcelegendaryalias.psc]
    legendaryChance = 100 (% chance)
    minRank = 1, maxRank = 3
    doOnLoad = True, doOnRefAdded = False
    |
    v
  4-Star variant:
    DefaultLegendary4StarCreatureRef                    [defaultlegendary4starcreatureref.psc]
    Rank4Chance = 0.5 (50% chance to upgrade rank 3 → rank 4)
```

### 4.3 Legendary Enemy Death - Loot Generation

```
LEGENDARY DEATH (Server-side)
  Actor::OnDeath(akKiller)                             [actor.psc:232]
  |
  v
  AbLegendaryExplodeScript::OnDeath()                  [ablegendaryexplodescript.psc]
    StartTimer(ExplosionDelay, explosionTimerID)
    OnTimer → ObjectReference.PlaceAtMe(DeathExplosion) [objectreference.psc:448] -- Native
  |
  v
  LEGENDARY ITEM GENERATION:
    PlayerLegendaryItemScript                           [playerlegendaryitemscript.psc]
    |
    v
  Step 1: Select base item
    LGND_PossibleLegendaryItemBaseLists (LeveledItem)
    Engine resolves leveled list → base weapon or armor
    |
    v
  Step 2: Determine star count
    LegendaryRewardQuestScript                          [legendaryrewardquestscript.psc]
      MinStarRating, MaxStarRating
      QuestLegendaryDropChance (GlobalVariable)
      LeveledListOfItemsToSpawn
    |
    v
  Step 3: Roll legendary mods per slot
    GetAllowedMods(item, SlotXMods, SpecifiedMods, DisallowedMods)  [playerlegendaryitemscript.psc:68]
    |
    For each star (slot):
      WEAPON:
        WeaponSlot1Mods through WeaponSlot5Mods
        Each is LegendaryModRule[]:
          LegendaryObjectMod (objectmod)
          AllowedKeywords (FormList) -- item must have one
          DisallowedKeywords (FormList) -- item must NOT have any
        |
        Check: item.HasKeywordInFormList(AllowedKeywords)   [form.psc:32] -- Native
        Check: !item.HasKeywordInFormList(DisallowedKeywords)
        |
        Random selection from filtered AllowedMods array
      |
      ARMOR:
        ArmorSlot1Mods through ArmorSlot5Mods
        Same LegendaryModRule filtering logic
    |
    v
  Step 4: Apply mods and create item
    Engine applies objectmod to generated item
    ObjectReference.AddItem(legendaryItem, 1, ...)      [objectreference.psc:838] -- Native
    |
    v
  Step 5: Add appropriate ammo
    AmmoData[] checked for matching Ammo type
    LeveledItem resolved for ammo count
```

### 4.4 Legendary Effect Event System

```
EFFECT ACTIVATION (Server-side)
  Player equips legendary weapon/armor
  Engine applies associated magic effects
  |
  v
  LegendaryMagicEffectEventSenderScript::OnEffectStart()  [legendarymagiceffecteventsenderscript.psc:86]
    casterPlayerScript = akCaster as playerlegendaryitemscript
    If SendOnHitEvent:
      RegisterForHitEvent(target, caster, ...)
    If SendOnEffectStartEvent:
      SendLegendaryMagicEffectEvent(target, caster, iEventType_Starting=1)
    |
    v
  PlayerLegendaryItemScript.SendLegendaryMagicEffectEvent(kArgs)
    SendCustomEvent("playerlegendaryitemscript_LegendaryMagicEffectEvent", kArgs)
    SFE: SendCustomEvent_Internal @ 0x013D9340
    |
    v
  ALL REGISTERED LISTENERS receive event:
    LegendaryMagicEffectEventListenScript subclasses    [legendarymagiceffecteventlistenscript.psc]
    Examples:
      ModLegendaryConsecutiveHitsScript -- tracks hit streaks
      ModLegendaryOnCritHealPlayerTeamScript -- heals team on crit
      ModLegendaryOnCritHitRefillAPScript -- refills AP on crit
      LegendaryOnHitCrippleScript -- cripple on hit
      LegendaryChemistsRandomEffectScript -- random chem effect
      LegendaryBrutalistsKillTrackingScript -- kill tracking
      LegendaryVoltaicSprintCheckScript -- sprint voltage check
```

### Legendary Chain Native Functions

| Function | Declaration | SFE Address | Side |
|----------|------------|-------------|------|
| `Actor.AddSpell(Spell, Bool)` | actor.psc:516 | Via Impl_Invoke | Server |
| `Actor.HasSpell(Form)` | actor.psc:538 | Via Impl_Invoke | Server |
| `Actor.GetLevel()` | actor.psc:24 | Via Impl_Invoke | Server |
| `ObjectReference.SetValue(AV, Float)` | objectreference.psc:288 | Via Impl_Invoke | Server |
| `ObjectReference.GetValue(AV)` | objectreference.psc:588 | Via Impl_Invoke | Server |
| `ObjectReference.PlaceAtMe(Form, ...)` | objectreference.psc:448 | PlaceAtMe_Native @ 0x0140AFC0 | Server |
| `ObjectReference.AddItem(Form, ...)` | objectreference.psc:838 | Via Impl_Invoke | Server |
| `Form.HasKeywordInFormList(FormList)` | form.psc:32 | Via Impl_Invoke | Server |
| `Utility.RandomInt(Int, Int)` | utility.psc:131 | Via Impl_Invoke | Server |
| `SendCustomEvent_Internal` | (engine) | 0x013D9340 | Server |

---

## CHAIN 5: CRAFTING

### 5.1 Trigger: Player Uses Workbench

```
WORKBENCH ACTIVATION (Client → Server)
  Player activates workbench reference
  |
  v
  ObjectReference::OnActivate(player)                  [objectreference.psc:254]
  |
  v
  Actor::OnPlayerUseWorkBench(akWorkBench)             [actor.psc:94]
  ActiveMagicEffect::OnPlayerUseWorkBench(akWorkBench) [activemagiceffect.psc:124]
  -- Dispatched to all scripts on the player
  |
  v
  PlayerWorkbenchScript (ReferenceAlias)               [playerworkbenchscript.psc]
    State transition: playernotinworkbench → playerinworkbench
    Animation events: "HammersAnvil", "StartsSewing"
    Keywords: WorkbenchPlayerGruntTopic, WorkbenchPlayerHumWhistleTopic
    |
    v
  CLIENT MENU:
    Engine opens crafting menu (Scaleform UI)
    SendUIMessage @ 0x0204CA70
    IsMenuOpen @ 0x02042040
```

### 5.2 Recipe Selection and Material Check

```
RECIPE SYSTEM (Server-side, mostly C++)
  Engine checks recipe requirements:
    For each required component:
      ObjectReference.GetItemCount(component, includeStash)  [objectreference.psc:652] -- Native
      ObjectReference.GetItemCountKeywords(keywords, all)    [objectreference.psc:650] -- Native
    |
    v
  MATERIAL REMOVAL:
    ObjectReference.RemoveItem(material, count, silent, ...)  [objectreference.psc:404] -- Native
    ObjectReference.RemoveItemByComponent(comp, count, ...)   [objectreference.psc:402] -- Native
    ObjectReference.RemoveComponents(component, count, ...)   [objectreference.psc:406] -- Native
```

### 5.3 Item Creation

```
ITEM CRAFTED (Server-side)
  Engine creates item from recipe output
  |
  v
  ObjectReference.AddItem(craftedItem, count, ...)      [objectreference.psc:838] -- Native
  |
  v
  CRAFTING EVENT DISPATCHED:
    Player::OnItemCrafted(craftedItem, count, workbench, modTarget)  [player.psc:91]
    ActiveMagicEffect::OnItemCrafted(...)                            [activemagiceffect.psc:223]
    |
    v
  QUEST TRACKING:
    OnItemCraftedSetStage (ReferenceAlias)               [onitemcraftedsetstage.psc]
      If crafted item matches ItemToCraft:
        If PrereqStage met:
          Set StageToSet on quest
    |
    DefaultOnItemCraftedScript extends DefaultQuestCountEventsManager
      -- Generic event counter for quests that track crafting
    |
    v
  TUTORIAL SYSTEM:
    Tutorial_Crafting_PlayerConnectScript                 [tutorial_crafting_playerconnectscript.psc]
      Keywords: Tutorial_WeaponCraftingStartKeyword, Tutorial_ArmorCraftingStartKeyword
      Sets: Tutorial_WeaponCraftingStarted AV, Tutorial_ArmorCraftingStarted AV
```

### 5.4 Super Duper / Lucky Perk Check

```
PERK ENTRY POINTS (Server-side, pure C++)
  Super Duper and Lucky Break are implemented as Perk Entry Points
  They fire BEFORE the item is created in the engine
  |
  The perk entry point system is entirely C++ -- no Papyrus scripts
  |
  Super Duper: "Mod Crafting Result Count" entry point
    Engine doubles the output count
    Result delivered through same AddItem path
  |
  Lucky Break: "Mod Item Condition" entry point
    Engine modifies the created item's condition value
  |
  XP AWARD:
    Player.XPSource_ObjectConstruction = 4               [player.psc:8]
    Engine awards XP for crafting through C++ XP system
```

### 5.5 Weapon/Armor Modding

```
MOD APPLICATION (Server-side)
  Player selects mod in workbench UI
  |
  v
  Actor::OnPlayerModArmorWeapon(baseObject, modBaseObject)  [actor.psc:108]
  ActiveMagicEffect::OnPlayerModArmorWeapon(...)             [activemagiceffect.psc:138]
  |
  v
  ENGINE MOD SYSTEM (C++):
    ObjectReference.RemoveModFromInventoryItem(item, mod)    [objectreference.psc:392] -- Native
    ObjectReference.RemoveAllModsFromInventoryItem(item)     [objectreference.psc:396] -- Native
    -- New mod applied via engine objectmod system
  |
  v
  ROBOT MODDING (Automatron):
    Actor::OnPlayerModRobot(robot, modBaseObject)            [actor.psc:104]
    Actor::OnPlayerCreateRobot(newRobot)                     [actor.psc:132]
```

### Crafting Chain Native Functions

| Function | Declaration | SFE Address | Side |
|----------|------------|-------------|------|
| `ObjectReference.AddItem(Form, Int, ...)` | objectreference.psc:838 | Via Impl_Invoke | Server |
| `ObjectReference.RemoveItem(Form, Int, ...)` | objectreference.psc:404 | Via Impl_Invoke | Server |
| `ObjectReference.RemoveComponents(comp, Int, ...)` | objectreference.psc:406 | Via Impl_Invoke | Server |
| `ObjectReference.GetItemCount(Form, Bool)` | objectreference.psc:652 | Via Impl_Invoke | Server |
| `ObjectReference.GetItemCountKeywords(FormList, Bool)` | objectreference.psc:650 | Via Impl_Invoke | Server |
| `ObjectReference.RemoveModFromInventoryItem(Form, mod)` | objectreference.psc:392 | Via Impl_Invoke | Server |
| `SendUIMessage` | (engine) | 0x0204CA70 | Client |
| `IsMenuOpen` | (engine) | 0x02042040 | Client |

---

## CHAIN 6: PUBLIC EVENT SYSTEM

### 6.1 Trigger: Event Initialization

```
EVENT START (Server-side)
  Story Manager triggers quest start (timer, player proximity, or quickplay)
  |
  v
  DefaultEventQuest extends QuestInstance               [defaulteventquest.psc]
    |
    v
  CONFIGURATION:
    CenterMarker (ReferenceAlias) -- event location
    AliasEventPlayers (RefCollectionAlias) -- active participants
    SpawnRadius = 4000.0 -- respawn radius
    ActivityEnterRadius = 6000.0 -- join radius
    ActivityExitRadius = 8000.0 -- leave radius
    ExtraEntranceRadius[] -- additional entry points
    ExtraExitRadius[] -- additional exit boundaries
    |
    v
  QUICKPLAY PATH:
    If started via quickplay:
      QPContext (quickplaycontext) configured
      Stage set to StartStageQuickPlay
      TargetPlayersPerInstance = 8 (new instance if exceeded)
      AllowVisitors = True/False
      CountPlayersAsQuickplayers = True/False
    Else:
      Stage set to StartStageStandard
    |
    v
  REGISTRATION:
    When EventStageStandard is reached:
      Quest registered with QuickPlay event system
      Other players see event on map, can join
```

### 6.2 Player Join/Leave

```
PLAYER PROXIMITY CHECK (Server-side, engine-driven)
  Engine continuously checks player distances from CenterMarker
  |
  v
  PLAYER ENTERS (distance < ActivityEnterRadius):
    Player added to AliasEventPlayers RefCollection
    Player receives event HUD, objectives, respawn system
    |
    v
  PLAYER EXITS (distance > ActivityExitRadius):
    Player removed from AliasEventPlayers
    Event UI dismissed
    |
    v
  RESTRICTIONS:
    ActorValueRequirement checked on join
    ObjectReference.GetValue(ActorValueRequirement)      [objectreference.psc:588] -- Native
    Must equal ActorValueRequirementValue
  |
  LATE JOIN CONTROL:
    EventStageDisableLateJoin -- when set, no new players
    Removes event from non-participant maps
```

### 6.3 Event Objectives and Boss Spawn

```
OBJECTIVE TRACKING (Server-side)
  Kill objectives use DefaultQuestOnKillManager          [defaultquestonkillmanager.psc]
    Same kill tracking system as Daily Quests (Chain 3)
    |
    v
  WAVE SPAWNING:
    DefaultQuestEncounterWaveScript
    Enemies spawned via:
      ObjectReference.PlaceActorAtMe(actorBase, levelMod, zone, ...)  [objectreference.psc:446] -- Native
      PlaceAtMe_Native @ 0x0140AFC0
    |
    v
  BOSS SPAWN:
    Boss quest stage triggered
    DefaultQuestBossOnDemand spawns boss actor
    Boss may use DefaultForceLegendaryAlias (forced legendary)
    |
    v
  BOSS HEALTH BAR:
    AliasHealthBarScript
    ObjectReference.GetValue(Health)                     [objectreference.psc:588] -- Native
    ObjectReference.GetValuePercentage(Health)            [objectreference.psc:586] -- Native
```

### 6.4 Bounty Hunt Event (Specific Example)

```
BOUNTY HUNT (Server-side)
  Burn_BountyHunt_PublicQuestScript                      [burn_bountyhunt_publicquestscript.psc]
    |
    v
  SETUP:
    ChosenBountyTargetLocation -- random bounty location
    BountyTargetSpawnCenter -- spawn marker
    BountyBeacon -- activator to trigger spawn
    BountyBoard -- quest giver activator
    |
    v
  SPAWN:
    ThreeStarBoss (ReferenceAlias) -- 3-star legendary boss
    ThreeStarBossColl (RefCollectionAlias) -- boss tracking
    TwoStarEnemyColl (RefCollectionAlias) -- posse enemies
    |
    v
  BOSS TRACKING:
    BossHealthAV -- boss health meter ActorValue
    UpdateNumOfActivePublicBounties GlobalVariable
    |
    v
  COMPLETION:
    Boss killed → SmokeBombExplosion placed
    ObjectReference.PlaceAtMe(SmokeBombExplosion, ...)
    Rewards distributed to participating players
```

### 6.5 Reward Distribution

```
REWARD SYSTEM (Server-side)
  DefaultQuestRewardEnemyDamageScript                    [defaultquestrewardenemydamagescript.psc]
    |
    v
  PARTICIPATION CHECK:
    RewardItem[] struct array:
      enemiesDeadStage -- trigger stage
      enemies (RefCollectionAlias) -- tracked enemies
      rewardPlayers (RefCollectionAlias) -- who helped
      rewardStage -- stage to set for rewards
    |
    When enemiesDeadStage is set:
      Engine checks which players damaged enemies collection
      Those players added to rewardPlayers collection
      rewardStage is set
    |
    v
  REWARD DELIVERY:
    Quest stage conditions: GetIsAliasRef(rewardPlayers)
    Only players in rewardPlayers get rewards
    |
    ObjectReference.AddItem(reward, count, ...)          [objectreference.psc:838] -- Native
    |
    v
  LEGENDARY REWARD:
    LegendaryRewardQuestScript                           [legendaryrewardquestscript.psc]
      MinStarRating, MaxStarRating
      QuestLegendaryDropChance (GlobalVariable)
      LeveledListOfItemsToSpawn
      |
      Rolls legendary item through PlayerLegendaryItemScript (Chain 4)
    |
    v
  XP REWARD:
    Player XPSource_QuestComplete or QuestReward
```

### Event Chain Native Functions

| Function | Declaration | SFE Address | Side |
|----------|------------|-------------|------|
| `ObjectReference.PlaceActorAtMe(ActorBase, ...)` | objectreference.psc:446 | PlaceAtMe_Native @ 0x0140AFC0 | Server |
| `ObjectReference.PlaceAtMe(Form, ...)` | objectreference.psc:448 | PlaceAtMe_Native @ 0x0140AFC0 | Server |
| `ObjectReference.GetValue(ActorValue)` | objectreference.psc:588 | Via Impl_Invoke | Server |
| `ObjectReference.GetValuePercentage(ActorValue)` | objectreference.psc:586 | Via Impl_Invoke | Server |
| `ObjectReference.GetDistance(ObjectReference)` | objectreference (native) | Via Impl_Invoke | Server |
| `ObjectReference.AddItem(Form, ...)` | objectreference.psc:838 | Via Impl_Invoke | Server |
| `Actor.IsHostileToActor(Actor)` | actor.psc:494 | IsHostileToActor @ 0x00D90F60 | Server |

---

## CROSS-CHAIN: SFE ADDRESS MAP

### Direct Native C++ Addresses (from SFE signatures)

These are the confirmed C++ function addresses in Fallout76.exe that underpin the execution chains:

| SFE Address | Function Name | Source File | Used In Chains |
|-------------|--------------|-------------|----------------|
| **0x00152C90** | `LookupFormByID` | GameForms.cpp | All (form lookups) |
| **0x0140AFC0** | `PlaceAtMe_Native` | GameObjects.cpp | Legendary, Event, Combat |
| **0x05ADD3D8** | `g_player` | GameReferences.cpp | All (player reference) |
| **0x00D90F60** | `IsHostileToActor` | GameReferences.h | Combat, Bot, Event |
| **0x012C6470** | `GetRefFromHandle` | PapyrusInterfaces.cpp | All (ref resolution) |
| **0x00480EE0** | `GetLinkedRef_Native` | GameReferences.cpp | Quest, Event |
| **0x00480F00** | `SetLinkedRef_Native` | GameReferences.cpp | Quest, Event |
| **0x013FE6C0** | `MoveRefrToPosition` | GameReferences.cpp | Bot (PathTo), Event |
| **0x0135B560** | `HasDetectionLOS` | GameReferences.cpp | Combat (LOS checks) |
| **0x0072AE60** | `EvaluationConditions` | GameFormComponents.cpp | Quest (conditions) |
| **0x0072C410** | `Evaluate` (single condition) | GameFormComponents.h | Quest (conditions) |
| **0x002083D0** | `ScrapReference` | GameWorkshop.cpp | Crafting (scrap) |

### Papyrus VM Infrastructure

| SFE Address | Function Name | Source File | Purpose |
|-------------|--------------|-------------|---------|
| **0x01374E90** | `SendPapyrusEvent` | PapyrusVM.h | All event dispatch |
| **0x013D9340** | `SendCustomEvent_Internal` | PapyrusEvents.cpp | Legendary effect events |
| **0x013D68B0** | `CallFunctionNoWait_Internal` | PapyrusEvents.cpp | Async script calls |
| **0x01451960** | `CallGlobalFunctionNoWait_Internal` | PapyrusEvents.cpp | Global function dispatch |
| **0x02732500** | `Impl_Invoke` | PapyrusNativeFunctions.h | ALL native function calls |
| **0x02732DB0** | `GetParam` | PapyrusNativeFunctions.h | Parameter marshaling |
| **0x013E6F01** | `RegisterPapyrusFunctions_Start` | Hooks_Papyrus.cpp | Function registration |
| **0x0590C388** | `g_gameVM` | PapyrusVM.cpp | VM singleton |
| **0x06755BC0** | `g_objectHandlePolicy` | PapyrusInterfaces.cpp | Object handle management |

### Input/UI Infrastructure

| SFE Address | Function Name | Source File | Purpose |
|-------------|--------------|-------------|---------|
| **0x05A98AB0** | `g_inputEventTable` | GameInput.cpp | Input event routing |
| **0x05A13268** | `g_playerControls` | GameInput.cpp | Player control handler |
| **0x00F44BA0** | `CreatePlayerControlHandlers` | Hooks_Input.cpp | Control handler setup |
| **0x0204CA70** | `SendUIMessage` | GameMenus.h | UI message dispatch |
| **0x02042040** | `IsMenuOpen` | GameMenus.h | Menu state queries |
| **0x05907BA8** | `g_playerCamera` | GameCamera.cpp | Camera state |
| **0x05907C98** | `g_globalEvents` | GameEvents.cpp | Global event system |

### Event Processing

| SFE Address | Function Name | Source File | Purpose |
|-------------|--------------|-------------|---------|
| **0x020431A0** | `ProcessEventQueue_HookTarget` | Hooks_Threads.cpp | Event queue hook |
| **0x0211CE60** | `ProcessEventQueue_Internal` | Hooks_Threads.cpp | Event processing |
| **0x00D57E80** | `MessageQueueProcessTask` | Hooks_Threads.cpp | Message queue task |
| **0x05AFF540** | `g_messageQueue` | GameMessages.cpp | Message queue singleton |

---

## CROSS-CHAIN: CLIENT vs SERVER BOUNDARY

### Always Server-Side (Authoritative)
- All Papyrus script execution
- Damage calculation and application
- Item creation, removal, modification
- Quest stage changes and objective updates
- Actor spawning and death
- Perk entry point evaluation
- Legendary roll calculations
- Crafting recipe validation and execution
- Event player tracking and rewards

### Always Client-Side
- Input capture (keyboard/mouse/gamepad)
- Rendering and animation playback
- UI/menu display (Scaleform)
- Sound playback
- Camera positioning
- HUD updates

### Client-Side with Server Validation
- Weapon fire (client predicts, server validates)
- Movement (client predicts, server corrects)
- Hit detection (client assists, server authoritative)
- Inventory display (client caches, server authoritative)

### Critical SFE Hook Points
The SFE (Script Framework Extender) operates on the **client** executable. It can:
1. Hook input processing via `CreatePlayerControlHandlers` @ 0x00F44BA0
2. Hook event processing via `ProcessEventQueue_HookTarget` @ 0x020431A0
3. Register new Papyrus functions via `RegisterPapyrusFunctions_Start` @ 0x013E6F01
4. Access the Papyrus VM via `g_gameVM` @ 0x0590C388
5. Send custom events via `SendCustomEvent_Internal` @ 0x013D9340
6. Invoke native functions via `Impl_Invoke` @ 0x02732500

**All** native Papyrus functions (SetAIDriven, PathToReference, AddItem, DamageValue, etc.) ultimately flow through `Impl_Invoke` @ 0x02732500, which is the universal dispatcher from Papyrus bytecode to C++ native implementations.

---

## APPENDIX: Key Script Inheritance Hierarchy

```
ScriptObject
  +-- Form
  |     +-- ObjectReference
  |     |     +-- Actor
  |     |     |     +-- Player
  |     |     |           +-- AutoTestClient:GrindMonsters
  |     |     |           +-- AutoTestClient:ExploreWorld
  |     |     |           +-- PlayerLegendaryItemScript
  |     |     +-- DefaultLegendaryCreatureRef
  |     |     +-- DefaultLegendary4StarCreatureRef
  |     +-- Weapon
  |     +-- Spell
  |     +-- Perk
  +-- QuestInstance
  |     +-- DefaultEventQuest
  |     +-- DefaultDailyQuestScript
  |     +-- DailyQuestScript
  |     +-- EpicCreaturesScript
  |     +-- SQ_HordeScript
  |     +-- LegendaryRewardQuestScript
  |     +-- DefaultQuestOnKillManager
  |     +-- DefaultQuestRewardEnemyDamageScript
  +-- ActiveMagicEffect
  |     +-- AbLegendaryScript
  |     +-- AbLegendaryExplodeScript
  |     +-- EpicCreatureEffectScript
  |     +-- EpicCreatureRestoreHealthEffectScript
  |     +-- LegendaryMagicEffectEventSenderScript
  |     +-- LegendaryMagicEffectEventListenScript
  |     |     +-- ModLegendaryConsecutiveHitsScript
  |     |     +-- ModLegendaryOnCritHealPlayerTeamScript
  |     |     +-- ModLegendaryOnCritHitRefillAPScript
  |     |     +-- LegendaryOnHitCrippleScript
  |     +-- DLC01WeapOnFireEffect
  +-- ReferenceAlias
  |     +-- PlayerWorkbenchScript
  |     +-- OnItemCraftedSetStage
  |     +-- DefaultForceLegendaryAlias
```
