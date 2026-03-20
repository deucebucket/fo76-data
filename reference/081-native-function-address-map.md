# FO76 Native Function to SFE Address Map

Complete mapping of every Papyrus Native function to its corresponding C++ engine address.

## Statistics

| Metric | Count |
|--------|-------|
| Total Native functions | 1107 |
| Total classes with Native functions | 48 |
| Mapped to SFE addresses | 12 |
| SFE extension functions | 1 |
| Unmapped (engine-internal) | 1094 |
| Coverage | 1.2% |
| SFE total address definitions | 277 |
| Scanner signatures available | 9 |

## Class Summary

| Class | Parent | Total Natives | Mapped | Unmapped | Coverage |
|-------|--------|--------------|--------|----------|----------|
| Activator | Form | 1 | 0 | 1 | 0% |
| ActiveMagicEffect | ScriptObject | 10 | 0 | 10 | 0% |
| Actor | ObjectReference | 200 | 5 | 195 | 2% |
| ActorBase | Form | 17 | 2 | 15 | 12% |
| ActorValue | Form | 1 | 0 | 1 | 0% |
| Cell | Form | 18 | 0 | 18 | 0% |
| ConstructibleObject | MiscObject | 1 | 1 | 0 | 100% |
| CurveTable | Form | 2 | 0 | 2 | 0% |
| Debug | ScriptObject | 102 | 0 | 102 | 0% |
| EffectShader | Form | 2 | 0 | 2 | 0% |
| Enchantment | Form | 1 | 0 | 1 | 0% |
| Faction | Form | 19 | 0 | 19 | 0% |
| Form | ScriptObject | 10 | 0 | 10 | 0% |
| FormList | Form | 8 | 0 | 8 | 0% |
| Furniture | Activator | 3 | 0 | 3 | 0% |
| Game | ScriptObject | 82 | 0 | 82 | 0% |
| GlobalVariable | Form | 2 | 0 | 2 | 0% |
| ImageSpaceModifier | Form | 6 | 0 | 6 | 0% |
| Ingredient | Form | 4 | 0 | 4 | 0% |
| InputEnableLayer | ScriptObject | 33 | 0 | 33 | 0% |
| InstanceNamingRules | Form | 1 | 0 | 1 | 0% |
| LeveledActor | Form | 2 | 0 | 2 | 0% |
| LeveledItem | Form | 3 | 0 | 3 | 0% |
| Location | Form | 25 | 0 | 25 | 0% |
| MagicEffect | Form | 1 | 0 | 1 | 0% |
| Math | ScriptObject | 13 | 0 | 13 | 0% |
| Message | Form | 6 | 0 | 6 | 0% |
| MiscObject | Form | 1 | 0 | 1 | 0% |
| MusicType | Form | 3 | 0 | 3 | 0% |
| ObjectReference | Form | 267 | 5 | 262 | 2% |
| Package | Form | 2 | 0 | 2 | 0% |
| Perk | Form | 1 | 0 | 1 | 0% |
| PerkCard | Form | 6 | 0 | 6 | 0% |
| Player | Actor | 69 | 0 | 69 | 0% |
| Potion | Form | 1 | 0 | 1 | 0% |
| QuickPlayContext | ScriptObject | 5 | 0 | 5 | 0% |
| ScriptObject | - | 98 | 0 | 98 | 0% |
| ShaderParticleGeometry | Form | 2 | 0 | 2 | 0% |
| Sound | Form | 4 | 0 | 4 | 0% |
| SoundCategory | Form | 6 | 0 | 6 | 0% |
| SoundCategorySnapshot | Form | 2 | 0 | 2 | 0% |
| Spell | Form | 3 | 0 | 3 | 0% |
| Terminal | Form | 1 | 0 | 1 | 0% |
| Utility | ScriptObject | 43 | 0 | 43 | 0% |
| VisualEffect | Form | 5 | 0 | 5 | 0% |
| WaveEncounterType | Form | 1 | 0 | 1 | 0% |
| Weapon | Form | 4 | 0 | 4 | 0% |
| Weather | Form | 10 | 0 | 10 | 0% |

## Classes with Most Unmapped Functions

These represent the largest opportunities for new SFE hooks:

- **ObjectReference**: 262 unmapped of 267 total
- **Actor**: 195 unmapped of 200 total
- **Debug**: 102 unmapped of 102 total
- **ScriptObject**: 98 unmapped of 98 total
- **Game**: 82 unmapped of 82 total
- **Player**: 69 unmapped of 69 total
- **Utility**: 43 unmapped of 43 total
- **InputEnableLayer**: 33 unmapped of 33 total
- **Location**: 25 unmapped of 25 total
- **Faction**: 19 unmapped of 19 total

## Complete Function Mapping by Class

### Activator
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| IsRadio | Bool | () | No | `Bool Function IsRadio() Native` |

### ActiveMagicEffect
*extends ScriptObject*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Dispel | Void | () | No | `Function Dispel() Native` |
| GetBaseObject | MagicEffect | () | No | `MagicEffect Function GetBaseObject() Native` |
| GetCasterActor | Actor | () | No | `Actor Function GetCasterActor() Native` |
| GetDuration | Float | () | No | `Float Function GetDuration() Native` |
| GetElapsedTime | Float | () | No | `Float Function GetElapsedTime() Native` |
| GetMagnitude | Float | () | No | `Float Function GetMagnitude() Native` |
| GetSpell | Form | () | No | `Form Function GetSpell() Native` |
| GetTargetActor | Actor | () | No | `Actor Function GetTargetActor() Native` |
| StartObjectProfiling | Void | () | No | `Function StartObjectProfiling() Native` |
| StopObjectProfiling | Void | () | No | `Function StopObjectProfiling() Native` |

### Actor
*extends ObjectReference*

#### Mapped Functions

| Function | Return | Params | Address | SFE Type | Source |
|----------|--------|--------|---------|----------|--------|
| ChangeHeadPart | Void | headpart apHeadPart, Bool abRemovePar... | `0x005B9A10` | direct_address | GameObjects.h:236 |
| GetLevel | Int | () | `0x001497F0` | direct_address | GameFormComponents.h:224 |
| GetSex | Int | () | `0x005A2440` | direct_address | GameObjects.h:234 |
| HasDetectionLOS | Bool | ObjectReference akOther | `0x0135B560` | direct_address | GameReferences.cpp:15 |
| IsHostileToActor | Bool | Actor akActor | `0x00D90F60` | direct_address | GameReferences.h:466 |

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| AddPerk | Void | Perk akPerk, Bool abNotify | No | `Function AddPerk(Perk akPerk, Bool abNotify) Native` |
| AddPreferredCombatTarget | Void | ObjectReference akTarget | No | `Function AddPreferredCombatTarget(ObjectReference akTarge...` |
| AddSpell | Bool | Spell akSpell, Bool abVerbose | No | `Bool Function AddSpell(Spell akSpell, Bool abVerbose) Native` |
| AllowBleedoutDialogue | Void | Bool abCanTalk | No | `Function AllowBleedoutDialogue(Bool abCanTalk) Native` |
| AllowPCDialogue | Void | Bool abTalk | No | `Function AllowPCDialogue(Bool abTalk) Native` |
| AttachAshPile | Void | Form akAshPileBase | No | `Function AttachAshPile(Form akAshPileBase) Native` |
| AttemptAnimationSetSwitch | Void | () | No | `Function AttemptAnimationSetSwitch() Native` |
| CanFlyHere | Bool | () | No | `Bool Function CanFlyHere() Native` |
| CanMoveVertical | Bool | () | No | `Bool Function CanMoveVertical() Native` |
| CanStrafe | Bool | () | No | `Bool Function CanStrafe() Native` |
| ChangeAnimArchetype | Bool | Keyword apKeyword | No | `Bool Function ChangeAnimArchetype(Keyword apKeyword) Native` |
| ChangeAnimFaceArchetype | Void | Keyword apKeyword | No | `Function ChangeAnimFaceArchetype(Keyword apKeyword) Native` |
| ChangeAnimFlavor | Bool | Keyword apKeyword | No | `Bool Function ChangeAnimFlavor(Keyword apKeyword) Native` |
| ClearArrested | Void | () | No | `Function ClearArrested() Native` |
| ClearExpressionOverride | Void | () | No | `Function ClearExpressionOverride() Native` |
| ClearExtraArrows | Void | () | No | `Function ClearExtraArrows() Native` |
| ClearForcedMovement | Void | () | No | `Function ClearForcedMovement() Native` |
| ClearLookAt | Void | () | No | `Function ClearLookAt() Native` |
| CollectPowerArmor | Void | ObjectReference akPowerArmor | No | `Function CollectPowerArmor(ObjectReference akPowerArmor) ...` |
| Dismember | Void | String asBodyPart, Bool abForceExplod... | No | `Function Dismember(String asBodyPart, Bool abForceExplode...` |
| Dismount | Bool | () | No | `Bool Function Dismount() Native` |
| DispelAllSpells | Void | () | No | `Function DispelAllSpells() Native` |
| DispelPotion | Bool | Potion akPotion | No | `Bool Function DispelPotion(Potion akPotion) Native` |
| DispelSpell | Bool | Spell akSpell | No | `Bool Function DispelSpell(Spell akSpell) Native` |
| DoCombatSpellApply | Void | Spell akSpell, ObjectReference akTarget | No | `Function DoCombatSpellApply(Spell akSpell, ObjectReferenc...` |
| DogDropItems | Void | () | No | `Function DogDropItems() Native` |
| DogPlaceInMouth | Void | Form akItem | No | `Function DogPlaceInMouth(Form akItem) Native` |
| DrawWeapon | Void | () | No | `Function DrawWeapon() Native` |
| EnableAI | Void | Bool abEnable, Bool abPauseVoice | No | `Function EnableAI(Bool abEnable, Bool abPauseVoice) Native` |
| EquipDisguise | Void | Form akItem | No | `Function EquipDisguise(Form akItem) Native` |
| EquipItem | Void | Form akItem, Bool abPreventRemoval, B... | No | `Function EquipItem(Form akItem, Bool abPreventRemoval, Bo...` |
| EquipSpell | Void | Spell akSpell, Int aiSource | No | `Function EquipSpell(Spell akSpell, Int aiSource) Native` |
| EvaluatePackage | Void | Bool abResetAI | No | `Function EvaluatePackage(Bool abResetAI) Native` |
| ExitPowerArmor | Void | () | No | `Function ExitPowerArmor() Native` |
| FindRandomCombatTarget | Actor | Float afRange | No | `Actor Function FindRandomCombatTarget(Float afRange) Native` |
| ForceMovementDirection | Void | Float afXAngle, Float afYAngle, Float... | No | `Function ForceMovementDirection(Float afXAngle, Float afY...` |
| ForceMovementDirectionRamp | Void | Float afXAngle, Float afYAngle, Float... | No | `Function ForceMovementDirectionRamp(Float afXAngle, Float...` |
| ForceMovementRotationSpeed | Void | Float afXMult, Float afYMult, Float a... | No | `Function ForceMovementRotationSpeed(Float afXMult, Float ...` |
| ForceMovementRotationSpeedRamp | Void | Float afXMult, Float afYMult, Float a... | No | `Function ForceMovementRotationSpeedRamp(Float afXMult, Fl...` |
| ForceMovementSpeed | Void | Float afSpeedMult | No | `Function ForceMovementSpeed(Float afSpeedMult) Native` |
| ForceMovementSpeedRamp | Void | Float afSpeedMult, Float afRampTime | No | `Function ForceMovementSpeedRamp(Float afSpeedMult, Float ...` |
| ForceTargetAngle | Void | Float afXAngle, Float afYAngle, Float... | No | `Function ForceTargetAngle(Float afXAngle, Float afYAngle,...` |
| ForceTargetDirection | Void | Float afXAngle, Float afYAngle, Float... | No | `Function ForceTargetDirection(Float afXAngle, Float afYAn...` |
| ForceTargetSpeed | Void | Float afSpeed | No | `Function ForceTargetSpeed(Float afSpeed) Native` |
| GetAllCombatTargets | Actor[] | () | No | `Actor[] Function GetAllCombatTargets() Native` |
| GetBribeAmount | Int | () | No | `Int Function GetBribeAmount() Native` |
| GetCanBeResuscitated | Bool | () | No | `Bool Function GetCanBeResuscitated() Native` |
| GetCombatState | Int | () | No | `Int Function GetCombatState() Native` |
| GetCombatTarget | Actor | () | No | `Actor Function GetCombatTarget() Native` |
| GetCrimeFaction | Faction | () | No | `Faction Function GetCrimeFaction() Native` |
| GetCurrentPackage | Package | () | No | `Package Function GetCurrentPackage() Native` |
| GetCurrentUsedFurniture | ObjectReference | () | No | `ObjectReference Function GetCurrentUsedFurniture() Native` |
| GetDialogueTarget | Actor | () | No | `Actor Function GetDialogueTarget() Native` |
| GetEWSCurveTable | curvetable | () | No | `curvetable Function GetEWSCurveTable() Native` |
| GetEquippedItemType | Int | Int aiEquipIndex | No | `Int Function GetEquippedItemType(Int aiEquipIndex) Native` |
| GetEquippedShield | Armor | () | No | `Armor Function GetEquippedShield() Native` |
| GetEquippedSpell | Spell | Int aiSource | No | `Spell Function GetEquippedSpell(Int aiSource) Native` |
| GetEquippedWeapon | Weapon | Int aiEquipIndex | No | `Weapon Function GetEquippedWeapon(Int aiEquipIndex) Native` |
| GetFactionReaction | Int | Actor akOther | No | `Int Function GetFactionReaction(Actor akOther) Native` |
| GetFlyingState | Int | () | No | `Int Function GetFlyingState() Native` |
| GetForcedLandingMarker | ObjectReference | () | No | `ObjectReference Function GetForcedLandingMarker() Native` |
| GetGoldAmount | Int | () | No | `Int Function GetGoldAmount() Native` |
| GetHighestRelationshipRank | Int | () | No | `Int Function GetHighestRelationshipRank() Native` |
| GetKiller | Actor | () | No | `Actor Function GetKiller() Native` |
| GetLeveledActorBase | ActorBase | () | No | `ActorBase Function GetLeveledActorBase() Native` |
| GetLightLevel | Float | () | No | `Float Function GetLightLevel() Native` |
| GetLowestRelationshipRank | Int | () | No | `Int Function GetLowestRelationshipRank() Native` |
| GetNoBleedoutRecovery | Bool | () | No | `Bool Function GetNoBleedoutRecovery() Native` |
| GetPlayerControls | Bool | () | No | `Bool Function GetPlayerControls() Native` |
| GetRace | Race | () | No | `Race Function GetRace() Native` |
| GetRelationshipRank | Int | Actor akOther | No | `Int Function GetRelationshipRank(Actor akOther) Native` |
| GetSitState | Int | () | No | `Int Function GetSitState() Native` |
| GetSleepState | Int | () | No | `Int Function GetSleepState() Native` |
| HasActiveMagicEffect | Bool | MagicEffect akEffect | No | `Bool Function HasActiveMagicEffect(MagicEffect akEffect) ...` |
| HasAssociation | Bool | AssociationType akAssociation, Actor ... | No | `Bool Function HasAssociation(AssociationType akAssociatio...` |
| HasFamilyRelationship | Bool | Actor akOther | No | `Bool Function HasFamilyRelationship(Actor akOther) Native` |
| HasMagicEffect | Bool | MagicEffect akEffect | No | `Bool Function HasMagicEffect(MagicEffect akEffect) Native` |
| HasMagicEffectWithKeyword | Bool | Keyword akKeyword | No | `Bool Function HasMagicEffectWithKeyword(Keyword akKeyword...` |
| HasParentRelationship | Bool | Actor akOther | No | `Bool Function HasParentRelationship(Actor akOther) Native` |
| HasPerk | Bool | Perk akPerk | No | `Bool Function HasPerk(Perk akPerk) Native` |
| HasSpell | Bool | Form akForm | No | `Bool Function HasSpell(Form akForm) Native` |
| IsAIEnabled | Bool | () | No | `Bool Function IsAIEnabled() Native` |
| IsAlarmed | Bool | () | No | `Bool Function IsAlarmed() Native` |
| IsAlerted | Bool | () | No | `Bool Function IsAlerted() Native` |
| IsAllowedToFly | Bool | () | No | `Bool Function IsAllowedToFly() Native` |
| IsArrested | Bool | () | No | `Bool Function IsArrested() Native` |
| IsArrestingTarget | Bool | () | No | `Bool Function IsArrestingTarget() Native` |
| IsBeingRidden | Bool | () | No | `Bool Function IsBeingRidden() Native` |
| IsBeingRiddenBy | Bool | Actor akActor | No | `Bool Function IsBeingRiddenBy(Actor akActor) Native` |
| IsBleedingOut | Bool | () | No | `Bool Function IsBleedingOut() Native` |
| IsBribed | Bool | () | No | `Bool Function IsBribed() Native` |
| IsChild | Bool | () | No | `Bool Function IsChild() Native` |
| IsCommandedActor | Bool | () | No | `Bool Function IsCommandedActor() Native` |
| IsDead | Bool | () | No | `Bool Function IsDead() Native` |
| IsDetectedBy | Bool | Actor akOther | No | `Bool Function IsDetectedBy(Actor akOther) Native` |
| IsDismembered | Bool | String asBodyPart | No | `Bool Function IsDismembered(String asBodyPart) Native` |
| IsDoingFavor | Bool | () | No | `Bool Function IsDoingFavor() Native` |
| IsEngagedInPvPWithAnyPlayer | Bool | () | No | `Bool Function IsEngagedInPvPWithAnyPlayer() Native` |
| IsEngagedInPvPWithPlayer | Bool | player akTargetPlayer | No | `Bool Function IsEngagedInPvPWithPlayer(player akTargetPla...` |
| IsEquipped | Bool | Form akItem | No | `Bool Function IsEquipped(Form akItem) Native` |
| IsEssential | Bool | () | No | `Bool Function IsEssential() Native` |
| IsFlying | Bool | () | No | `Bool Function IsFlying() Native` |
| IsGhost | Bool | () | No | `Bool Function IsGhost() Native` |
| IsGuard | Bool | () | No | `Bool Function IsGuard() Native` |
| IsInAir | Bool | () | No | `Bool Function IsInAir() Native` |
| IsInCombat | Bool | () | No | `Bool Function IsInCombat() Native` |
| IsInIronSights | Bool | () | No | `Bool Function IsInIronSights() Native` |
| IsInKillMove | Bool | () | No | `Bool Function IsInKillMove() Native` |
| IsInPowerArmor | Bool | () | No | `Bool Function IsInPowerArmor() Native` |
| IsInScene | Bool | () | No | `Bool Function IsInScene() Native` |
| IsIntimidated | Bool | () | No | `Bool Function IsIntimidated() Native` |
| IsInvulnerable | Bool | () | No | `Bool Function IsInvulnerable() Native` |
| IsOnMount | Bool | () | No | `Bool Function IsOnMount() Native` |
| IsOverEncumbered | Bool | () | No | `Bool Function IsOverEncumbered() Native` |
| IsPlayerTeammate | Bool | () | No | `Bool Function IsPlayerTeammate() Native` |
| IsPlayersLastRiddenHorse | Bool | player akPlayer | No | `Bool Function IsPlayersLastRiddenHorse(player akPlayer) N...` |
| IsRunning | Bool | () | No | `Bool Function IsRunning() Native` |
| IsSeatOccupied | Bool | Keyword apKeyword | No | `Bool Function IsSeatOccupied(Keyword apKeyword) Native` |
| IsSneaking | Bool | () | No | `Bool Function IsSneaking() Native` |
| IsSprinting | Bool | () | No | `Bool Function IsSprinting() Native` |
| IsTalking | Bool | () | No | `Bool Function IsTalking() Native` |
| IsTrespassing | Bool | () | No | `Bool Function IsTrespassing() Native` |
| IsUnconscious | Bool | () | No | `Bool Function IsUnconscious() Native` |
| IsWeaponDrawn | Bool | () | No | `Bool Function IsWeaponDrawn() Native` |
| Kill | Void | Actor akKiller | No | `Function Kill(Actor akKiller) Native` |
| KillSilent | Void | Actor akKiller | No | `Function KillSilent(Actor akKiller) Native` |
| PathToReference | Bool | ObjectReference aTarget, Float afWalk... | No | `Bool Function PathToReference(ObjectReference aTarget, Fl...` |
| PlayIdle | Bool | Idle akIdle | No | `Bool Function PlayIdle(Idle akIdle) Native` |
| PlayIdleAction | Bool | Action aAction, ObjectReference aTarget | No | `Bool Function PlayIdleAction(Action aAction, ObjectRefere...` |
| PlayIdleWithTarget | Bool | Idle akIdle, ObjectReference akTarget | No | `Bool Function PlayIdleWithTarget(Idle akIdle, ObjectRefer...` |
| PlaySubGraphAnimation | Void | String asEventName | No | `Function PlaySubGraphAnimation(String asEventName) Native` |
| RemovePerk | Void | Perk akPerk | No | `Function RemovePerk(Perk akPerk) Native` |
| RemoveSpell | Bool | Spell akSpell | No | `Bool Function RemoveSpell(Spell akSpell) Native` |
| RepairEquippedArmorCondition | Bool | Int aiBipedObject, Float afPercent | No | `Bool Function RepairEquippedArmorCondition(Int aiBipedObj...` |
| RepairEquippedWeaponCondition | Bool | Int aiEquipIndex, Float afPercent | No | `Bool Function RepairEquippedWeaponCondition(Int aiEquipIn...` |
| ResetHealthAndLimbs | Void | () | No | `Function ResetHealthAndLimbs() Native` |
| RestoreDefaultOutfit | Void | Bool abSleepOutfit | No | `Function RestoreDefaultOutfit(Bool abSleepOutfit) Native` |
| Resurrect | Void | () | No | `Function Resurrect() Native` |
| SetAlert | Void | Bool abAlerted | No | `Function SetAlert(Bool abAlerted) Native` |
| SetAlpha | Void | Float afTargetAlpha, Bool abFade | No | `Function SetAlpha(Float afTargetAlpha, Bool abFade) Native` |
| SetAttackActorOnSight | Void | Bool abAttackOnSight | No | `Function SetAttackActorOnSight(Bool abAttackOnSight) Native` |
| SetAvoidPlayer | Void | Bool abAvoid | No | `Function SetAvoidPlayer(Bool abAvoid) Native` |
| SetBloodImpactMaterial | Void | material akMaterial | No | `Function SetBloodImpactMaterial(material akMaterial) Native` |
| SetBribed | Void | Bool abBribe | No | `Function SetBribed(Bool abBribe) Native` |
| SetCanDoCommand | Void | Bool abCanCommand | No | `Function SetCanDoCommand(Bool abCanCommand) Native` |
| SetCombatStyle | Void | combatstyle akCombatStyle | No | `Function SetCombatStyle(combatstyle akCombatStyle) Native` |
| SetCombatTargetPreferredSelectorIgnoresDamage | Void | Bool abIgnoreDamage | No | `Function SetCombatTargetPreferredSelectorIgnoresDamage(Bo...` |
| SetCombatTargetPrefersPlayers | Void | () | No | `Function SetCombatTargetPrefersPlayers() Native` |
| SetCombatTargetSelectorSupportsAllies | Void | () | No | `Function SetCombatTargetSelectorSupportsAllies() Native` |
| SetCommandState | Void | Bool abStartCommandMode | No | `Function SetCommandState(Bool abStartCommandMode) Native` |
| SetDoingFavor | Void | Bool abDoingFavor, Bool abWorkShopMode | No | `Function SetDoingFavor(Bool abDoingFavor, Bool abWorkShop...` |
| SetEquippedWeaponAttacksEnabled | Void | Int aiEquipIndex, Bool abAttacksEnabled | No | `Function SetEquippedWeaponAttacksEnabled(Int aiEquipIndex...` |
| SetEyeTexture | Void | textureset akNewTexture | No | `Function SetEyeTexture(textureset akNewTexture) Native` |
| SetForcedLandingMarker | Void | ObjectReference aMarker | No | `Function SetForcedLandingMarker(ObjectReference aMarker) ...` |
| SetGhost | Void | Bool abIsGhost | No | `Function SetGhost(Bool abIsGhost) Native` |
| SetGhostedToTeammates | Void | Bool abIsGhostedToTeammates | No | `Function SetGhostedToTeammates(Bool abIsGhostedToTeammate...` |
| SetHasCharGenSkeleton | Void | Bool abCharGen | No | `Function SetHasCharGenSkeleton(Bool abCharGen) Native` |
| SetHeadTracking | Void | Bool abEnable | No | `Function SetHeadTracking(Bool abEnable) Native` |
| SetIntimidated | Void | Bool abIntimidate | No | `Function SetIntimidated(Bool abIntimidate) Native` |
| SetInvulnerable | Void | Bool abInvulnerable | No | `Function SetInvulnerable(Bool abInvulnerable) Native` |
| SetLookAt | Void | ObjectReference akTarget, Bool abPath... | No | `Function SetLookAt(ObjectReference akTarget, Bool abPathi...` |
| SetNoBleedoutRecovery | Void | Bool abAllowed | No | `Function SetNoBleedoutRecovery(Bool abAllowed) Native` |
| SetNotShowOnStealthMeter | Void | Bool abNotShow | No | `Function SetNotShowOnStealthMeter(Bool abNotShow) Native` |
| SetOutfit | Void | Outfit akOutfit, Bool abSleepOutfit | No | `Function SetOutfit(Outfit akOutfit, Bool abSleepOutfit) N...` |
| SetOverrideVoiceType | Void | VoiceType akVoiceType | No | `Function SetOverrideVoiceType(VoiceType akVoiceType) Native` |
| SetPlayerControls | Void | Bool abControls | No | `Function SetPlayerControls(Bool abControls) Native` |
| SetPlayerResistingArrest | Void | () | No | `Function SetPlayerResistingArrest() Native` |
| SetPlayerTeammate | Void | Actor akPlayer, Bool abCanDoFavor, Bo... | No | `Function SetPlayerTeammate(Actor akPlayer, Bool abCanDoFa...` |
| SetRace | Void | Race akRace | No | `Function SetRace(Race akRace) Native` |
| SetRelationshipRank | Void | Actor akOther, Int aiRank | No | `Function SetRelationshipRank(Actor akOther, Int aiRank) N...` |
| SetRestrained | Bool | Bool abRestrained | No | `Bool Function SetRestrained(Bool abRestrained) Native` |
| SetSubGraphFloatVariable | Void | String asVariableName, Float afValue | No | `Function SetSubGraphFloatVariable(String asVariableName, ...` |
| SetUnconscious | Bool | Bool abUnconscious | No | `Bool Function SetUnconscious(Bool abUnconscious) Native` |
| SetVehicle | Void | Actor akVehicle | No | `Function SetVehicle(Actor akVehicle) Native` |
| SetWantSprinting | Bool | Bool abWantSprint | No | `Bool Function SetWantSprinting(Bool abWantSprint) Native` |
| SnapIntoInteraction | Bool | ObjectReference akTarget | No | `Bool Function SnapIntoInteraction(ObjectReference akTarge...` |
| StartCannibal | Void | Actor akTarget | No | `Function StartCannibal(Actor akTarget) Native` |
| StartCombat | Void | Actor akTarget, Bool abPreferredTarget | No | `Function StartCombat(Actor akTarget, Bool abPreferredTarg...` |
| StartFrenzyAttack | Void | Float aChance, Float aInterval | No | `Function StartFrenzyAttack(Float aChance, Float aInterval...` |
| StartSneaking | Void | () | No | `Function StartSneaking() Native` |
| StartVampireFeed | Void | Actor akTarget | No | `Function StartVampireFeed(Actor akTarget) Native` |
| StopCombat | Void | () | No | `Function StopCombat() Native` |
| StopCombatAlarm | Void | () | No | `Function StopCombatAlarm() Native` |
| TrapSoul | Bool | Actor akTarget | No | `Bool Function TrapSoul(Actor akTarget) Native` |
| TriggerCriticalEffect | Void | EffectShader apShader, Int aiStage, F... | No | `Function TriggerCriticalEffect(EffectShader apShader, Int...` |
| UnLockOwnedDoorsInCell | Void | () | No | `Function UnLockOwnedDoorsInCell() Native` |
| UnequipAll | Void | () | No | `Function UnequipAll() Native` |
| UnequipDisguise | Void | () | No | `Function UnequipDisguise() Native` |
| UnequipItem | Void | Form akItem, Bool abPreventEquip, Boo... | No | `Function UnequipItem(Form akItem, Bool abPreventEquip, Bo...` |
| UnequipItemSlot | Void | Int aiSlot | No | `Function UnequipItemSlot(Int aiSlot) Native` |
| UnequipSpell | Void | Spell akSpell, Int aiSource | No | `Function UnequipSpell(Spell akSpell, Int aiSource) Native` |
| WillIntimidateSucceed | Bool | () | No | `Bool Function WillIntimidateSucceed() Native` |
| WornHasKeyword | Bool | Keyword akKeyword | No | `Bool Function WornHasKeyword(Keyword akKeyword) Native` |
| WouldBeStealing | Bool | ObjectReference akObject | No | `Bool Function WouldBeStealing(ObjectReference akObject) N...` |
| WouldRefuseCommand | Int | ObjectReference akObject | No | `Int Function WouldRefuseCommand(ObjectReference akObject)...` |

### ActorBase
*extends Form*

#### Mapped Functions

| Function | Return | Params | Address | SFE Type | Source |
|----------|--------|--------|---------|----------|--------|
| GetLevel | Int | () | `0x001497F0` | direct_address | GameFormComponents.h:224 |
| GetSex | Int | () | `0x005A2440` | direct_address | GameObjects.h:234 |

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| GetClass | Class | () | No | `Class Function GetClass() Native` |
| GetDeadCount | Int | () | No | `Int Function GetDeadCount() Native` |
| GetGiftFilter | FormList | () | No | `FormList Function GetGiftFilter() Native` |
| GetLevelExact | Int | () | No | `Int Function GetLevelExact() Native` |
| GetRace | Race | () | No | `Race Function GetRace() Native` |
| GetUniqueActor | Actor | () | No | `Actor Function GetUniqueActor() Native` |
| IsEssential | Bool | () | No | `Bool Function IsEssential() Native` |
| IsInvulnerable | Bool | () | No | `Bool Function IsInvulnerable() Native` |
| IsProtected | Bool | () | No | `Bool Function IsProtected() Native` |
| IsUnique | Bool | () | No | `Bool Function IsUnique() Native` |
| SetEssential | Void | Bool abEssential | No | `Function SetEssential(Bool abEssential) Native` |
| SetGhostedToTeammates | Void | Bool abIsGhostedForTeammates | No | `Function SetGhostedToTeammates(Bool abIsGhostedForTeammat...` |
| SetInvulnerable | Void | Bool abInvulnerable | No | `Function SetInvulnerable(Bool abInvulnerable) Native` |
| SetOutfit | Void | Outfit akOutfit, Bool abSleepOutfit | No | `Function SetOutfit(Outfit akOutfit, Bool abSleepOutfit) N...` |
| SetProtected | Void | Bool abProtected | No | `Function SetProtected(Bool abProtected) Native` |

### ActorValue
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| GetPairedKeyword | Keyword | () | No | `Keyword Function GetPairedKeyword() Native` |

### Cell
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| EnableFastTravel | Void | Bool abEnable | No | `Function EnableFastTravel(Bool abEnable) Native` |
| GetActorOwner | ActorBase | () | No | `ActorBase Function GetActorOwner() Native` |
| GetFactionOwner | Faction | () | No | `Faction Function GetFactionOwner() Native` |
| GetWorldXY | Int[] | () | No | `Int[] Function GetWorldXY() Native` |
| IsAttached | Bool | () | No | `Bool Function IsAttached() Native` |
| IsExpedition | Bool | () | No | `Bool Function IsExpedition() Native` |
| IsExpeditionMission | Bool | () | No | `Bool Function IsExpeditionMission() Native` |
| IsInstanceable | Bool | () | No | `Bool Function IsInstanceable() Native` |
| IsInstanced | Bool | () | No | `Bool Function IsInstanced() Native` |
| IsInstancedDerived | Bool | Cell aTargetCell | No | `Bool Function IsInstancedDerived(Cell aTargetCell) Native` |
| IsInterior | Bool | Bool abIncludeVisualExteriors | No | `Bool Function IsInterior(Bool abIncludeVisualExteriors) N...` |
| IsLoaded | Bool | () | No | `Bool Function IsLoaded() Native` |
| SetActorOwner | Void | ActorBase akActor | No | `Function SetActorOwner(ActorBase akActor) Native` |
| SetFactionOwner | Void | Faction akFaction | No | `Function SetFactionOwner(Faction akFaction) Native` |
| SetFogColor | Void | Int aiNearRed, Int aiNearGreen, Int a... | No | `Function SetFogColor(Int aiNearRed, Int aiNearGreen, Int ...` |
| SetFogPlanes | Void | Float afNear, Float afFar | No | `Function SetFogPlanes(Float afNear, Float afFar) Native` |
| SetFogPower | Void | Float afPower | No | `Function SetFogPower(Float afPower) Native` |
| SetPublic | Void | Bool abPublic | No | `Function SetPublic(Bool abPublic) Native` |

### ConstructibleObject
*extends MiscObject*

#### Mapped Functions

| Function | Return | Params | Address | SFE Type | Source |
|----------|--------|--------|---------|----------|--------|
| GetCreatedObject | Form | () | `-` | sfe_extension | PapyrusConstructibleObject.cpp |

### CurveTable
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| GetValueAt | Float | Float afInput | No | `Float Function GetValueAt(Float afInput) Native` |
| HasValueAt | Bool | Float afInput | No | `Bool Function HasValueAt(Float afInput) Native` |

### Debug
*extends ScriptObject*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| AutoTestComplete | Void | Bool abSuccess | Yes | `Function AutoTestComplete(Bool abSuccess) Global Native` |
| AutoTestDebugLog | Void | String asMessage | Yes | `Function AutoTestDebugLog(String asMessage) Global Native` |
| AutoTestExpectEqBool | Void | Bool expected, Bool actual, String as... | Yes | `Function AutoTestExpectEqBool(Bool expected, Bool actual,...` |
| AutoTestExpectEqFloat | Void | Float expected, Float actual, String ... | Yes | `Function AutoTestExpectEqFloat(Float expected, Float actu...` |
| AutoTestExpectEqInt | Void | Int expected, Int actual, String asMe... | Yes | `Function AutoTestExpectEqInt(Int expected, Int actual, St...` |
| AutoTestExpectEqObject | Void | ScriptObject expected, ScriptObject a... | Yes | `Function AutoTestExpectEqObject(ScriptObject expected, Sc...` |
| AutoTestExpectEqString | Void | String expected, String actual, Strin... | Yes | `Function AutoTestExpectEqString(String expected, String a...` |
| AutoTestExpectFalse | Void | Bool condition, String asMessage | Yes | `Function AutoTestExpectFalse(Bool condition, String asMes...` |
| AutoTestExpectGreaterEqFloat | Void | Float expected, Float actual, String ... | Yes | `Function AutoTestExpectGreaterEqFloat(Float expected, Flo...` |
| AutoTestExpectGreaterEqInt | Void | Int expected, Int actual, String asMe... | Yes | `Function AutoTestExpectGreaterEqInt(Int expected, Int act...` |
| AutoTestExpectGreaterFloat | Void | Float expected, Float actual, String ... | Yes | `Function AutoTestExpectGreaterFloat(Float expected, Float...` |
| AutoTestExpectGreaterInt | Void | Int expected, Int actual, String asMe... | Yes | `Function AutoTestExpectGreaterInt(Int expected, Int actua...` |
| AutoTestExpectLessEqFloat | Void | Float expected, Float actual, String ... | Yes | `Function AutoTestExpectLessEqFloat(Float expected, Float ...` |
| AutoTestExpectLessEqInt | Void | Int expected, Int actual, String asMe... | Yes | `Function AutoTestExpectLessEqInt(Int expected, Int actual...` |
| AutoTestExpectLessFloat | Void | Float expected, Float actual, String ... | Yes | `Function AutoTestExpectLessFloat(Float expected, Float ac...` |
| AutoTestExpectLessInt | Void | Int expected, Int actual, String asMe... | Yes | `Function AutoTestExpectLessInt(Int expected, Int actual, ...` |
| AutoTestExpectNotEqBool | Void | Bool expected, Bool actual, String as... | Yes | `Function AutoTestExpectNotEqBool(Bool expected, Bool actu...` |
| AutoTestExpectNotEqFloat | Void | Float expected, Float actual, String ... | Yes | `Function AutoTestExpectNotEqFloat(Float expected, Float a...` |
| AutoTestExpectNotEqInt | Void | Int expected, Int actual, String asMe... | Yes | `Function AutoTestExpectNotEqInt(Int expected, Int actual,...` |
| AutoTestExpectNotEqObject | Void | ScriptObject expected, ScriptObject a... | Yes | `Function AutoTestExpectNotEqObject(ScriptObject expected,...` |
| AutoTestExpectNotEqString | Void | String expected, String actual, Strin... | Yes | `Function AutoTestExpectNotEqString(String expected, Strin...` |
| AutoTestExpectTrue | Void | Bool condition, String asMessage | Yes | `Function AutoTestExpectTrue(Bool condition, String asMess...` |
| AutoTestFaceTarget | Void | Actor target | Yes | `Function AutoTestFaceTarget(Actor target) Global Native` |
| AutoTestFire | Void | () | Yes | `Function AutoTestFire() Global Native` |
| AutoTestFireOnTarget | Void | Actor target | Yes | `Function AutoTestFireOnTarget(Actor target) Global Native` |
| AutoTestFireWeapon | Void | () | Yes | `Function AutoTestFireWeapon() Global Native` |
| AutoTestGetCurrentWeaponLevel | Int | () | Yes | `Int Function AutoTestGetCurrentWeaponLevel() Global Native` |
| AutoTestGetExecutionDuration | Int | () | Yes | `Int Function AutoTestGetExecutionDuration() Global Native` |
| AutoTestGetExecutionIndex | Int | () | Yes | `Int Function AutoTestGetExecutionIndex() Global Native` |
| AutoTestGetNormalizedHealth | Float | Actor target | Yes | `Float Function AutoTestGetNormalizedHealth(Actor target) ...` |
| AutoTestGetNormalizedHealthMax | Float | Actor target | Yes | `Float Function AutoTestGetNormalizedHealthMax(Actor targe...` |
| AutoTestGetNormalizedLevel | Int | Actor target | Yes | `Int Function AutoTestGetNormalizedLevel(Actor target) Glo...` |
| AutoTestGetSelectedRefr | ObjectReference | () | Yes | `ObjectReference Function AutoTestGetSelectedRefr() Global...` |
| AutoTestLog | Void | String asMessage | Yes | `Function AutoTestLog(String asMessage) Global Native` |
| AutoTestLootContainer | Void | ObjectReference container | Yes | `Function AutoTestLootContainer(ObjectReference container)...` |
| AutoTestRandRangeFloat | Float | Float min, Float max | Yes | `Float Function AutoTestRandRangeFloat(Float min, Float ma...` |
| AutoTestRandRangeInt | Int | Int min, Int max | Yes | `Int Function AutoTestRandRangeInt(Int min, Int max) Globa...` |
| AutoTestReadFile | String[] | String filename | Yes | `String[] Function AutoTestReadFile(String filename) Globa...` |
| BabylonBotShouldLoot | Bool | () | Yes | `Bool Function BabylonBotShouldLoot() Global Native` |
| BabylonBotShouldMove | Bool | () | Yes | `Bool Function BabylonBotShouldMove() Global Native` |
| BabylonBotShouldShoot | Bool | () | Yes | `Bool Function BabylonBotShouldShoot() Global Native` |
| CenterOnCell | Void | String asCellname | Yes | `Function CenterOnCell(String asCellname) Global Native` |
| CenterOnCellAndWait | Float | String asCellname | Yes | `Float Function CenterOnCellAndWait(String asCellname) Glo...` |
| CenterOnWorldAndWait | Float | String worldName, Int x, Int y | Yes | `Float Function CenterOnWorldAndWait(String worldName, Int...` |
| CloseUserLog | Void | String asLogName | Yes | `Function CloseUserLog(String asLogName) Global Native` |
| DBSendPlayerPosition | Void | () | Yes | `Function DBSendPlayerPosition() Global Native` |
| DumpAliasData | Void | questinstance akQuest | Yes | `Function DumpAliasData(questinstance akQuest) Global Native` |
| DumpEventRegistrations | Void | ScriptObject akScript | Yes | `Function DumpEventRegistrations(ScriptObject akScript) Gl...` |
| EnableAI | Void | Bool abEnable | Yes | `Function EnableAI(Bool abEnable) Global Native` |
| EnableCollisions | Void | Bool abEnable | Yes | `Function EnableCollisions(Bool abEnable) Global Native` |
| EnableDetection | Void | Bool abEnable | Yes | `Function EnableDetection(Bool abEnable) Global Native` |
| EnableMenus | Void | Bool abEnable | Yes | `Function EnableMenus(Bool abEnable) Global Native` |
| ExecuteBatchedServerConsoleCommands | Void | () | Yes | `Function ExecuteBatchedServerConsoleCommands() Global Native` |
| ExecuteLocalConsole | Void | String asCommand | Yes | `Function ExecuteLocalConsole(String asCommand) Global Native` |
| ExecuteServerConsole | Void | String asCommand | Yes | `Function ExecuteServerConsole(String asCommand) Global Na...` |
| FindRandomReferenceWithFormTypeId | ObjectReference | ObjectReference sourceRef, Int formTy... | Yes | `ObjectReference Function FindRandomReferenceWithFormTypeI...` |
| GetConfigName | String | () | Yes | `String Function GetConfigName() Global Native` |
| GetFormsByType | Form[] | Int type | Yes | `Form[] Function GetFormsByType(Int type) Global Native` |
| GetInstanceLevelOfPlayerWeapons | Int[] | Actor target | Yes | `Int[] Function GetInstanceLevelOfPlayerWeapons(Actor targ...` |
| GetMapMarkerByIndex | ObjectReference | Int index | Yes | `ObjectReference Function GetMapMarkerByIndex(Int index) G...` |
| GetNormalizedCryoResistance | Float | Actor target | Yes | `Float Function GetNormalizedCryoResistance(Actor target) ...` |
| GetNormalizedDamageResistance | Float | Actor target | Yes | `Float Function GetNormalizedDamageResistance(Actor target...` |
| GetNormalizedEnergyResistance | Float | Actor target | Yes | `Float Function GetNormalizedEnergyResistance(Actor target...` |
| GetNormalizedFireResistance | Float | Actor target | Yes | `Float Function GetNormalizedFireResistance(Actor target) ...` |
| GetNormalizedPoisonResistance | Float | Actor target | Yes | `Float Function GetNormalizedPoisonResistance(Actor target...` |
| GetNormalizedRadiationResistance | Float | Actor target | Yes | `Float Function GetNormalizedRadiationResistance(Actor tar...` |
| GetNormalizedUnarmedDamage | Float | Actor target | Yes | `Float Function GetNormalizedUnarmedDamage(Actor target) G...` |
| GetNormalizedWeaponsDamageForActor | Float[] | Actor target | Yes | `Float[] Function GetNormalizedWeaponsDamageForActor(Actor...` |
| GetNumMapMarkers | Int | () | Yes | `Int Function GetNumMapMarkers() Global Native` |
| GetPlatformName | String | () | Yes | `String Function GetPlatformName() Global Native` |
| GetVersionNumber | String | () | Yes | `String Function GetVersionNumber() Global Native` |
| GetWeaponsInActorInventory | Weapon[] | Actor target | Yes | `Weapon[] Function GetWeaponsInActorInventory(Actor target...` |
| MessageBox | Void | String asMessageBoxText | Yes | `Function MessageBox(String asMessageBoxText) Global Native` |
| Notification | Void | String asNotificationText | Yes | `Function Notification(String asNotificationText) Global N...` |
| OpenUserLog | Bool | String asLogName | Yes | `Bool Function OpenUserLog(String asLogName) Global Native` |
| PlayerGoTo | Void | String asStrKey | Yes | `Function PlayerGoTo(String asStrKey) Global Native` |
| PlayerMoveToAndWait | Float | String asDestRef | Yes | `Float Function PlayerMoveToAndWait(String asDestRef) Glob...` |
| QuestGetCompleted | Bool | Int instanceId | Yes | `Bool Function QuestGetCompleted(Int instanceId) Global Na...` |
| QuestGetFailed | Bool | Int instanceId | Yes | `Bool Function QuestGetFailed(Int instanceId) Global Native` |
| QuestGetInstanceIDs | Int[] | String questName | Yes | `Int[] Function QuestGetInstanceIDs(String questName) Glob...` |
| QuestGetStage | Int | Int instanceId | Yes | `Int Function QuestGetStage(Int instanceId) Global Native` |
| QuestRequestAlias | Int | Int instanceId, String aliasName, Int... | Yes | `Int Function QuestRequestAlias(Int instanceId, String ali...` |
| QueueBatchedServerConsoleCommand | Void | String command | Yes | `Function QueueBatchedServerConsoleCommand(String command)...` |
| QuitGame | Void | () | Yes | `Function QuitGame() Global Native` |
| SetFootIK | Void | Bool abFootIK | Yes | `Function SetFootIK(Bool abFootIK) Global Native` |
| SetGodMode | Void | Bool abGodMode | Yes | `Function SetGodMode(Bool abGodMode) Global Native` |
| ShowRefPosition | Void | ObjectReference arRef | Yes | `Function ShowRefPosition(ObjectReference arRef) Global Na...` |
| StartScriptProfiling | Void | String asScriptName | Yes | `Function StartScriptProfiling(String asScriptName) Global...` |
| StartStackProfiling | Void | () | Yes | `Function StartStackProfiling() Global Native` |
| StartStackRootProfiling | Void | String asScriptName, ScriptObject akObj | Yes | `Function StartStackRootProfiling(String asScriptName, Scr...` |
| StopScriptProfiling | Void | String asScriptName | Yes | `Function StopScriptProfiling(String asScriptName) Global ...` |
| StopStackProfiling | Void | () | Yes | `Function StopStackProfiling() Global Native` |
| StopStackRootProfiling | Void | String asScriptName, ScriptObject akObj | Yes | `Function StopStackRootProfiling(String asScriptName, Scri...` |
| TestAllCells | Void | Int aiCmdID, Int aiMode, Int aiCurren... | Yes | `Function TestAllCells(Int aiCmdID, Int aiMode, Int aiCurr...` |
| Trace | Void | String asTextToPrint, Int aiSeverity,... | Yes | `Function Trace(String asTextToPrint, Int aiSeverity, Stri...` |
| TraceFunction | Void | String asTextToPrint, Int aiSeverity,... | Yes | `Function TraceFunction(String asTextToPrint, Int aiSeveri...` |
| TraceStack | Void | String asTextToPrint, Int aiSeverity,... | Yes | `Function TraceStack(String asTextToPrint, Int aiSeverity,...` |
| TraceTransaction | Void | String asTextToPrint, Int aiSeverity,... | Yes | `Function TraceTransaction(String asTextToPrint, Int aiSev...` |
| TraceUser | Bool | String asUserLog, String asTextToPrin... | Yes | `Bool Function TraceUser(String asUserLog, String asTextTo...` |
| WorkshopBuildBlueprintRef | Void | Int aiIndex | Yes | `Function WorkshopBuildBlueprintRef(Int aiIndex) Global Na...` |
| WorkshopExit | Void | () | Yes | `Function WorkshopExit() Global Native` |
| WorkshopPlaceBlueprintRef | Void | Int aiIndex | Yes | `Function WorkshopPlaceBlueprintRef(Int aiIndex) Global Na...` |

### EffectShader
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Play | Void | ObjectReference akObject, Float afDur... | No | `Function Play(ObjectReference akObject, Float afDuration)...` |
| Stop | Void | ObjectReference akObject | No | `Function Stop(ObjectReference akObject) Native` |

### Enchantment
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| IsHostile | Bool | () | No | `Bool Function IsHostile() Native` |

### Faction
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| CanPayCrimeGold | Bool | () | No | `Bool Function CanPayCrimeGold() Native` |
| GetCrimeGold | Int | () | No | `Int Function GetCrimeGold() Native` |
| GetCrimeGoldNonViolent | Int | () | No | `Int Function GetCrimeGoldNonViolent() Native` |
| GetCrimeGoldViolent | Int | () | No | `Int Function GetCrimeGoldViolent() Native` |
| GetFactionReaction | Int | Actor akOther | No | `Int Function GetFactionReaction(Actor akOther) Native` |
| GetInfamy | Int | () | No | `Int Function GetInfamy() Native` |
| GetInfamyNonViolent | Int | () | No | `Int Function GetInfamyNonViolent() Native` |
| GetInfamyViolent | Int | () | No | `Int Function GetInfamyViolent() Native` |
| GetOwningQuestInstance | questinstance | () | No | `questinstance Function GetOwningQuestInstance() Native` |
| GetStolenItemValueCrime | Int | () | No | `Int Function GetStolenItemValueCrime() Native` |
| GetStolenItemValueNoCrime | Int | () | No | `Int Function GetStolenItemValueNoCrime() Native` |
| IsFactionInCrimeGroup | Bool | Faction akOther | No | `Bool Function IsFactionInCrimeGroup(Faction akOther) Native` |
| IsInstancedFaction | Bool | () | No | `Bool Function IsInstancedFaction() Native` |
| ModCrimeGold | Void | Int aiAmount, Bool abViolent | No | `Function ModCrimeGold(Int aiAmount, Bool abViolent) Native` |
| SendPlayerToJail | Void | Bool abRemoveInventory, Bool abRealJail | No | `Function SendPlayerToJail(Bool abRemoveInventory, Bool ab...` |
| SetAlly | Void | Faction akOther, Bool abSelfIsFriendT... | No | `Function SetAlly(Faction akOther, Bool abSelfIsFriendToOt...` |
| SetCrimeGold | Void | Int aiGold | No | `Function SetCrimeGold(Int aiGold) Native` |
| SetCrimeGoldViolent | Void | Int aiGold | No | `Function SetCrimeGoldViolent(Int aiGold) Native` |
| SetEnemy | Void | Faction akOther, Bool abSelfIsNeutral... | No | `Function SetEnemy(Faction akOther, Bool abSelfIsNeutralTo...` |

### Form
*extends ScriptObject*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| GetFormID | Int | () | No | `Int Function GetFormID() Native` |
| GetFormWeight | Float | () | No | `Float Function GetFormWeight() Native` |
| GetGoldValue | Int | () | No | `Int Function GetGoldValue() Native` |
| GetReservingQuests | questinstance[] | () | No | `questinstance[] Function GetReservingQuests() Native` |
| HasKeyword | Bool | Keyword akKeyword | No | `Bool Function HasKeyword(Keyword akKeyword) Native` |
| HasKeywordInFormList | Bool | FormList akKeywordList | No | `Bool Function HasKeywordInFormList(FormList akKeywordList...` |
| IsReserved | Bool | () | No | `Bool Function IsReserved() Native` |
| PlayerKnows | Bool | () | No | `Bool Function PlayerKnows() Native` |
| StartObjectProfiling | Void | () | No | `Function StartObjectProfiling() Native` |
| StopObjectProfiling | Void | () | No | `Function StopObjectProfiling() Native` |

### FormList
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| AddForm | Void | Form apForm | No | `Function AddForm(Form apForm) Native` |
| Find | Int | Form apForm | No | `Int Function Find(Form apForm) Native` |
| GetArray | Form[] | () | No | `Form[] Function GetArray() Native` |
| GetAt | Form | Int aiIndex | No | `Form Function GetAt(Int aiIndex) Native` |
| GetSize | Int | () | No | `Int Function GetSize() Native` |
| HasForm | Bool | Form akForm | No | `Bool Function HasForm(Form akForm) Native` |
| RemoveAddedForm | Void | Form apForm | No | `Function RemoveAddedForm(Form apForm) Native` |
| Revert | Void | () | No | `Function Revert() Native` |

### Furniture
*extends Activator*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| GetAssociatedForm | Form | () | No | `Form Function GetAssociatedForm() Native` |
| GetMarkerCount | Int | () | No | `Int Function GetMarkerCount() Native` |
| IsMarkerEnabled | Bool | Int aMarker | No | `Bool Function IsMarkerEnabled(Int aMarker) Native` |

### Game
*extends ScriptObject*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| AddNuclearWeatherNukeTransition | Void | String aNukeRampTexture | Yes | `Function AddNuclearWeatherNukeTransition(String aNukeRamp...` |
| AddNuclearWinterWeatherTransition | Void | Float aStormLevel, Weather aWeather, ... | Yes | `Function AddNuclearWinterWeatherTransition(Float aStormLe...` |
| ClearTempEffects | Void | () | Yes | `Function ClearTempEffects() Global Native` |
| EnablePipboyHDRMask | Void | Bool abEnable | Yes | `Function EnablePipboyHDRMask(Bool abEnable) Global Native` |
| FadeOutGame | Void | Bool abFadingOut, Bool abBlackFade, F... | Yes | `Function FadeOutGame(Bool abFadingOut, Bool abBlackFade, ...` |
| FinalizeSettingStormFXData | Void | () | Yes | `Function FinalizeSettingStormFXData() Global Native` |
| FindClosestActor | Actor | Float afX, Float afY, Float afZ, Floa... | Yes | `Actor Function FindClosestActor(Float afX, Float afY, Flo...` |
| FindRandomActor | Actor | Float afX, Float afY, Float afZ, Floa... | Yes | `Actor Function FindRandomActor(Float afX, Float afY, Floa...` |
| ForceDisableSSRDirLight | Void | Bool abDisableSSR, Bool abDisableDirL... | Yes | `Function ForceDisableSSRDirLight(Bool abDisableSSR, Bool ...` |
| GetAggressionAV | ActorValue | () | Yes | `ActorValue Function GetAggressionAV() Global Native` |
| GetAgilityAV | ActorValue | () | Yes | `ActorValue Function GetAgilityAV() Global Native` |
| GetAllLocations | Location[] | () | Yes | `Location[] Function GetAllLocations() Global Native` |
| GetCharismaAV | ActorValue | () | Yes | `ActorValue Function GetCharismaAV() Global Native` |
| GetConfidenceAV | ActorValue | () | Yes | `ActorValue Function GetConfidenceAV() Global Native` |
| GetDataFloat | Float | String asFilename, String asKey, Int ... | Yes | `Float Function GetDataFloat(String asFilename, String asK...` |
| GetDataFloats | Float[] | String asFilename, String asKey | Yes | `Float[] Function GetDataFloats(String asFilename, String ...` |
| GetDataInt | Int | String asFilename, String asKey, Int ... | Yes | `Int Function GetDataInt(String asFilename, String asKey, ...` |
| GetDataInts | Int[] | String asFilename, String asKey | Yes | `Int[] Function GetDataInts(String asFilename, String asKe...` |
| GetDataString | String | String asFilename, String asKey, Int ... | Yes | `String Function GetDataString(String asFilename, String a...` |
| GetDataStrings | String[] | String asFilename, String asKey | Yes | `String[] Function GetDataStrings(String asFilename, Strin...` |
| GetDifficulty | Int | () | Yes | `Int Function GetDifficulty() Global Native` |
| GetEnduranceAV | ActorValue | () | Yes | `ActorValue Function GetEnduranceAV() Global Native` |
| GetForm | Form | Int aiFormID | Yes | `Form Function GetForm(Int aiFormID) Global Native` |
| GetFormByEditorID | Form | String editorId | Yes | `Form Function GetFormByEditorID(String editorId) Global N...` |
| GetFormFromFile | Form | Int aiFormID, String asFilename | Yes | `Form Function GetFormFromFile(Int aiFormID, String asFile...` |
| GetGameSettingBool | Bool | String asGameSetting | Yes | `Bool Function GetGameSettingBool(String asGameSetting) Gl...` |
| GetGameSettingFloat | Float | String asGameSetting | Yes | `Float Function GetGameSettingFloat(String asGameSetting) ...` |
| GetGameSettingInt | Int | String asGameSetting | Yes | `Int Function GetGameSettingInt(String asGameSetting) Glob...` |
| GetGameSettingString | String | String asGameSetting | Yes | `String Function GetGameSettingString(String asGameSetting...` |
| GetGameSettingUInt | Int | String asGameSetting | Yes | `Int Function GetGameSettingUInt(String asGameSetting) Glo...` |
| GetGameWorldType | Int | () | Yes | `Int Function GetGameWorldType() Global Native` |
| GetHealthAV | ActorValue | () | Yes | `ActorValue Function GetHealthAV() Global Native` |
| GetIntelligenceAV | ActorValue | () | Yes | `ActorValue Function GetIntelligenceAV() Global Native` |
| GetLocalPlayer | player | () | Yes | `player Function GetLocalPlayer() Global Native` |
| GetLuckAV | ActorValue | () | Yes | `ActorValue Function GetLuckAV() Global Native` |
| GetMatchingLocations | Location[] | Location ParentLocation, Keyword[] Wa... | Yes | `Location[] Function GetMatchingLocations(Location ParentL...` |
| GetPerceptionAV | ActorValue | () | Yes | `ActorValue Function GetPerceptionAV() Global Native` |
| GetRealHoursPassed | Float | () | Yes | `Float Function GetRealHoursPassed() Global Native` |
| GetStrengthAV | ActorValue | () | Yes | `ActorValue Function GetStrengthAV() Global Native` |
| GetSuspiciousAV | ActorValue | () | Yes | `ActorValue Function GetSuspiciousAV() Global Native` |
| GetXPForLevel | Int | Int auiLevel | Yes | `Int Function GetXPForLevel(Int auiLevel) Global Native` |
| HideTitleSequenceMenu | Void | () | Yes | `Function HideTitleSequenceMenu() Global Native` |
| IsPluginInstalled | Bool | String asName | Yes | `Bool Function IsPluginInstalled(String asName) Global Native` |
| LoadNuclearWinterTextureMaps | Void | String[] aPaths | Yes | `Function LoadNuclearWinterTextureMaps(String[] aPaths) Gl...` |
| PassTime | Void | Int aiHours | Yes | `Function PassTime(Int aiHours) Global Native` |
| PlayBink | Void | String asFilename, Bool abInterruptib... | Yes | `Function PlayBink(String asFilename, Bool abInterruptible...` |
| PlayEventCamera | Void | camerashot akCamera, ObjectReference ... | Yes | `Function PlayEventCamera(camerashot akCamera, ObjectRefer...` |
| PrecacheCharGen | Void | () | Yes | `Function PrecacheCharGen() Global Native` |
| PrecacheCharGenClear | Void | () | Yes | `Function PrecacheCharGenClear() Global Native` |
| QuitToMainMenu | Void | () | Yes | `Function QuitToMainMenu() Global Native` |
| RegisterQPMap | Void | String asMapTexturePath, ObjectRefere... | Yes | `Function RegisterQPMap(String asMapTexturePath, ObjectRef...` |
| RequestAutoSave | Void | () | Yes | `Function RequestAutoSave() Global Native` |
| RequestModel | Void | String asModelName | Yes | `Function RequestModel(String asModelName) Global Native` |
| RequestSave | Void | () | Yes | `Function RequestSave() Global Native` |
| SetCharGenHUDMode | Void | Int aiCGHUDMode | Yes | `Function SetCharGenHUDMode(Int aiCGHUDMode) Global Native` |
| SetInChargen | Void | Bool abInChargen | Yes | `Function SetInChargen(Bool abInChargen) Global Native` |
| SetInsideMemoryHUDMode | Void | Bool aInsideMemory | Yes | `Function SetInsideMemoryHUDMode(Bool aInsideMemory) Globa...` |
| SetMapSpecificStormWallData | Void | Float aStormWallHeight, Float aStormW... | Yes | `Function SetMapSpecificStormWallData(Float aStormWallHeig...` |
| SetNumStormFXData | Void | Int aiNumEffects | Yes | `Function SetNumStormFXData(Int aiNumEffects) Global Native` |
| SetStormFXDataDistancesAndPlacementModes | Void | Float[] aMinDistancesA, Float[] aMaxD... | Yes | `Function SetStormFXDataDistancesAndPlacementModes(Float[]...` |
| SetStormFXDataEvenPlacementOffsets | Void | Float[] aEvenOrbitOffsetsA, Float[] a... | Yes | `Function SetStormFXDataEvenPlacementOffsets(Float[] aEven...` |
| SetStormFXDataFadeInOutDistances | Void | Float[] aFadeInDistancesA, Float[] aF... | Yes | `Function SetStormFXDataFadeInOutDistances(Float[] aFadeIn...` |
| SetStormFXDataFireVertexAnim | Void | Bool[] abVertexAnim, Float[] aWaveFre... | Yes | `Function SetStormFXDataFireVertexAnim(Bool[] abVertexAnim...` |
| SetStormFXDataHeightOffsetsAndAppModes | Void | Float[] aMinHeightOffsetsA, Float[] a... | Yes | `Function SetStormFXDataHeightOffsetsAndAppModes(Float[] a...` |
| SetStormFXDataPreStormWallAlpha | Void | Bool[] abPreStormWallAlpha | Yes | `Function SetStormFXDataPreStormWallAlpha(Bool[] abPreStor...` |
| SetStormFXDataRotationAnglesAndAppModes | Void | Float[] aMinRotationAnglesA, Float[] ... | Yes | `Function SetStormFXDataRotationAnglesAndAppModes(Float[] ...` |
| SetStormFXDataScalesAndAppModes | Void | Float[] aMinScalesA, Float[] aMaxScal... | Yes | `Function SetStormFXDataScalesAndAppModes(Float[] aMinScal...` |
| SetStormFXDataSkyEffect | Void | Bool[] abSkyEffect | Yes | `Function SetStormFXDataSkyEffect(Bool[] abSkyEffect) Glob...` |
| SetStormFXDataSpawnMultipliers | Void | Float[] aSpawnMultipliersA | Yes | `Function SetStormFXDataSpawnMultipliers(Float[] aSpawnMul...` |
| SetStormFXDataVisualEffects | Void | VisualEffect[] aParticleEffectsA, Boo... | Yes | `Function SetStormFXDataVisualEffects(VisualEffect[] aPart...` |
| SetStormFXNumInstancesAndModes | Void | Int[] aNumInstancesA, Int[] aInstance... | Yes | `Function SetStormFXNumInstancesAndModes(Int[] aNumInstanc...` |
| ShowFatigueWarningOnHUD | Void | () | Yes | `Function ShowFatigueWarningOnHUD() Global Native` |
| ShowFirstPersonGeometry | Void | Bool abShow | Yes | `Function ShowFirstPersonGeometry(Bool abShow) Global Native` |
| ShowPerkVaultBoyOnHUD | Void | String aVaultBoySwf, Sound aSoundDesc... | Yes | `Function ShowPerkVaultBoyOnHUD(String aVaultBoySwf, Sound...` |
| ShowPipboyBootSequence | Void | String asAnimationName | Yes | `Function ShowPipboyBootSequence(String asAnimationName) G...` |
| ShowPipboyPlugin | Void | () | Yes | `Function ShowPipboyPlugin() Global Native` |
| ShowTitleSequenceMenu | Void | () | Yes | `Function ShowTitleSequenceMenu() Global Native` |
| StartDialogueCameraOrCenterOnTarget | Void | ObjectReference akCameraTarget | Yes | `Function StartDialogueCameraOrCenterOnTarget(ObjectRefere...` |
| StartTitleSequence | Void | String asSequenceName | Yes | `Function StartTitleSequence(String asSequenceName) Global...` |
| StopDialogueCamera | Void | Bool abConsiderResume, Bool abSwitchi... | Yes | `Function StopDialogueCamera(Bool abConsiderResume, Bool a...` |
| error | Void | String asMessage | Yes | `Function error(String asMessage) Global Native` |
| warning | Void | String asMessage | Yes | `Function warning(String asMessage) Global Native` |

### GlobalVariable
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| GetValue | Float | () | No | `Float Function GetValue() Native` |
| SetValue | Void | Float afNewValue | No | `Function SetValue(Float afNewValue) Native` |

### ImageSpaceModifier
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Apply | Void | Float afStrength | No | `Function Apply(Float afStrength) Native` |
| ApplyCrossFade | Void | Float afFadeDuration | No | `Function ApplyCrossFade(Float afFadeDuration) Native` |
| GetDuration | Float | () | No | `Float Function GetDuration() Native` |
| PopTo | Void | ImageSpaceModifier akNewModifier, Flo... | No | `Function PopTo(ImageSpaceModifier akNewModifier, Float af...` |
| Remove | Void | () | No | `Function Remove() Native` |
| RemoveCrossFade | Void | Float afFadeDuration | Yes | `Function RemoveCrossFade(Float afFadeDuration) Global Native` |

### Ingredient
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| IsHostile | Bool | () | No | `Bool Function IsHostile() Native` |
| LearnAllEffects | Void | () | No | `Function LearnAllEffects() Native` |
| LearnEffect | Void | Int aiIndex | No | `Function LearnEffect(Int aiIndex) Native` |
| LearnNextEffect | Int | () | No | `Int Function LearnNextEffect() Native` |

### InputEnableLayer
*extends ScriptObject*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Create | InputEnableLayer | player player | Yes | `InputEnableLayer Function Create(player player) Global Na...` |
| Delete | Void | () | No | `Function Delete() Native` |
| DisablePlayerControls | Void | Bool abMovement, Bool abFighting, Boo... | No | `Function DisablePlayerControls(Bool abMovement, Bool abFi...` |
| EnableActivate | Void | Bool abEnable | No | `Function EnableActivate(Bool abEnable) Native` |
| EnableCamSwitch | Void | Bool abEnable | No | `Function EnableCamSwitch(Bool abEnable) Native` |
| EnableFastTravel | Void | Bool abEnable | No | `Function EnableFastTravel(Bool abEnable) Native` |
| EnableFavorites | Void | Bool abEnable | No | `Function EnableFavorites(Bool abEnable) Native` |
| EnableFighting | Void | Bool abEnable | No | `Function EnableFighting(Bool abEnable) Native` |
| EnableJournal | Void | Bool abEnable | No | `Function EnableJournal(Bool abEnable) Native` |
| EnableJumping | Void | Bool abEnable | No | `Function EnableJumping(Bool abEnable) Native` |
| EnableLooking | Void | Bool abEnable | No | `Function EnableLooking(Bool abEnable) Native` |
| EnableMenu | Void | Bool abEnable | No | `Function EnableMenu(Bool abEnable) Native` |
| EnableMovement | Void | Bool abEnable | No | `Function EnableMovement(Bool abEnable) Native` |
| EnablePlayerControls | Void | Bool abMovement, Bool abFighting, Boo... | No | `Function EnablePlayerControls(Bool abMovement, Bool abFig...` |
| EnableRunning | Void | Bool abEnable | No | `Function EnableRunning(Bool abEnable) Native` |
| EnableSneaking | Void | Bool abEnable | No | `Function EnableSneaking(Bool abEnable) Native` |
| EnableSprinting | Void | Bool abEnable | No | `Function EnableSprinting(Bool abEnable) Native` |
| EnableVATS | Void | Bool abEnable | No | `Function EnableVATS(Bool abEnable) Native` |
| IsActivateEnabled | Bool | () | No | `Bool Function IsActivateEnabled() Native` |
| IsCamSwitchEnabled | Bool | () | No | `Bool Function IsCamSwitchEnabled() Native` |
| IsFastTravelEnabled | Bool | () | No | `Bool Function IsFastTravelEnabled() Native` |
| IsFavoritesEnabled | Bool | () | No | `Bool Function IsFavoritesEnabled() Native` |
| IsFightingEnabled | Bool | () | No | `Bool Function IsFightingEnabled() Native` |
| IsJournalEnabled | Bool | () | No | `Bool Function IsJournalEnabled() Native` |
| IsJumpingEnabled | Bool | () | No | `Bool Function IsJumpingEnabled() Native` |
| IsLookingEnabled | Bool | () | No | `Bool Function IsLookingEnabled() Native` |
| IsMenuEnabled | Bool | () | No | `Bool Function IsMenuEnabled() Native` |
| IsMovementEnabled | Bool | () | No | `Bool Function IsMovementEnabled() Native` |
| IsRunningEnabled | Bool | () | No | `Bool Function IsRunningEnabled() Native` |
| IsSneakingEnabled | Bool | () | No | `Bool Function IsSneakingEnabled() Native` |
| IsSprintingEnabled | Bool | () | No | `Bool Function IsSprintingEnabled() Native` |
| IsVATSEnabled | Bool | () | No | `Bool Function IsVATSEnabled() Native` |
| Reset | Void | () | No | `Function Reset() Native` |

### InstanceNamingRules
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| MergeWith | Void | InstanceNamingRules aSource | No | `Function MergeWith(InstanceNamingRules aSource) Native` |

### LeveledActor
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| AddForm | Void | Form apForm, Int aiLevel | No | `Function AddForm(Form apForm, Int aiLevel) Native` |
| Revert | Void | () | No | `Function Revert() Native` |

### LeveledItem
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| AddForm | Void | Form apForm, Int aiLevel, Int aiCount | No | `Function AddForm(Form apForm, Int aiLevel, Int aiCount) N...` |
| HasForm | Bool | Form apForm | No | `Bool Function HasForm(Form apForm) Native` |
| Revert | Void | () | No | `Function Revert() Native` |

### Location
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| AddKeyword | Void | Keyword akKeyword | No | `Function AddKeyword(Keyword akKeyword) Native` |
| AddLinkedLocation | Void | Location akLoc, Keyword akKeyword | No | `Function AddLinkedLocation(Location akLoc, Keyword akKeyw...` |
| CountActors | Int | Keyword apRequiredLinkedRefKeyword, K... | No | `Int Function CountActors(Keyword apRequiredLinkedRefKeywo...` |
| GetActors | Actor[] | Keyword apRequiredLinkedRefKeyword, K... | No | `Actor[] Function GetActors(Keyword apRequiredLinkedRefKey...` |
| GetActorsInInstancedLocation | Actor[] | questinstance akQuestInstance, Keywor... | No | `Actor[] Function GetActorsInInstancedLocation(questinstan...` |
| GetAllLinkedLocations | Location[] | Keyword akKeyword | No | `Location[] Function GetAllLinkedLocations(Keyword akKeywo...` |
| GetAllPlayersInInstancedLocation | player[] | questinstance akQuestInstance | No | `player[] Function GetAllPlayersInInstancedLocation(questi...` |
| GetKeywordData | Float | Keyword akKeyword | No | `Float Function GetKeywordData(Keyword akKeyword) Native` |
| GetMaxLevel | Int | () | No | `Int Function GetMaxLevel() Native` |
| GetMinLevel | Int | () | No | `Int Function GetMinLevel() Native` |
| GetParentLocations | Location[] | Keyword akKeyword | No | `Location[] Function GetParentLocations(Keyword akKeyword)...` |
| GetRefTypeAliveCount | Int | LocationRefType akRefType | No | `Int Function GetRefTypeAliveCount(LocationRefType akRefTy...` |
| GetRefTypeDeadCount | Int | LocationRefType akRefType | No | `Int Function GetRefTypeDeadCount(LocationRefType akRefTyp...` |
| HasCommonParent | Bool | Location akOther, Keyword akFilter | No | `Bool Function HasCommonParent(Location akOther, Keyword a...` |
| HasEverBeenCleared | Bool | () | No | `Bool Function HasEverBeenCleared() Native` |
| HasRefType | Bool | LocationRefType akRefType | No | `Bool Function HasRefType(LocationRefType akRefType) Native` |
| IsChild | Bool | Location akOther | No | `Bool Function IsChild(Location akOther) Native` |
| IsCleared | Bool | () | No | `Bool Function IsCleared() Native` |
| IsLinkedLocation | Bool | Location akLocation, Keyword akKeyword | No | `Bool Function IsLinkedLocation(Location akLocation, Keywo...` |
| IsLoaded | Bool | () | No | `Bool Function IsLoaded() Native` |
| RemoveKeyword | Void | Keyword akKeyword | No | `Function RemoveKeyword(Keyword akKeyword) Native` |
| RemoveLinkedLocation | Void | Location akLoc, Keyword akKeyword | No | `Function RemoveLinkedLocation(Location akLoc, Keyword akK...` |
| Reset | Void | () | No | `Function Reset() Native` |
| SetCleared | Void | Bool abCleared | No | `Function SetCleared(Bool abCleared) Native` |
| SetKeywordData | Void | Keyword akKeyword, Float afData | No | `Function SetKeywordData(Keyword akKeyword, Float afData) ...` |

### MagicEffect
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| GetAssociatedSkill | String | () | No | `String Function GetAssociatedSkill() Native` |

### Math
*extends ScriptObject*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Ceiling | Int | Float afValue | Yes | `Int Function Ceiling(Float afValue) Global Native` |
| DegreesToRadians | Float | Float afDegrees | Yes | `Float Function DegreesToRadians(Float afDegrees) Global N...` |
| Floor | Int | Float afValue | Yes | `Int Function Floor(Float afValue) Global Native` |
| RadiansToDegrees | Float | Float afRadians | Yes | `Float Function RadiansToDegrees(Float afRadians) Global N...` |
| abs | Float | Float afValue | Yes | `Float Function abs(Float afValue) Global Native` |
| acos | Float | Float afValue | Yes | `Float Function acos(Float afValue) Global Native` |
| asin | Float | Float afValue | Yes | `Float Function asin(Float afValue) Global Native` |
| atan | Float | Float afValue | Yes | `Float Function atan(Float afValue) Global Native` |
| cos | Float | Float afValue | Yes | `Float Function cos(Float afValue) Global Native` |
| pow | Float | Float x, Float y | Yes | `Float Function pow(Float x, Float y) Global Native` |
| sin | Float | Float afValue | Yes | `Float Function sin(Float afValue) Global Native` |
| sqrt | Float | Float afValue | Yes | `Float Function sqrt(Float afValue) Global Native` |
| tan | Float | Float afValue | Yes | `Float Function tan(Float afValue) Global Native` |

### Message
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| ClearHelpMessages | Void | player[] akReceivingPlayers | Yes | `Function ClearHelpMessages(player[] akReceivingPlayers) G...` |
| ResetHelpMessage | Void | player[] akReceivingPlayers, String a... | Yes | `Function ResetHelpMessage(player[] akReceivingPlayers, St...` |
| Show | Void | player[] receivingPlayers, questinsta... | No | `Function Show(player[] receivingPlayers, questinstance aQ...` |
| ShowAsAnnounceMessage | Void | player[] akReceivingPlayers | No | `Function ShowAsAnnounceMessage(player[] akReceivingPlayer...` |
| ShowAsHelpMessage | Void | player[] akReceivingPlayers, String a... | No | `Function ShowAsHelpMessage(player[] akReceivingPlayers, S...` |
| UnshowAsHelpMessage | Void | player[] akReceivingPlayers | No | `Function UnshowAsHelpMessage(player[] akReceivingPlayers)...` |

### MiscObject
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| GetObjectComponentCount | Int | component akComponent | No | `Int Function GetObjectComponentCount(component akComponen...` |

### MusicType
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Add | Void | () | No | `Function Add() Native` |
| Remove | Void | () | No | `Function Remove() Native` |
| RemoveImmediately | Void | () | No | `Function RemoveImmediately() Native` |

### ObjectReference
*extends Form*

#### Mapped Functions

| Function | Return | Params | Address | SFE Type | Source |
|----------|--------|--------|---------|----------|--------|
| GetWorldSpace | WorldSpace | () | `0x0040F170` | direct_address | GameReferences.h:245 |
| MoveTo | Void | ObjectReference akTarget, Float afXOf... | `0x013FE6C0` | native_impl_match | GameReferences.cpp:21 |
| PlaceAtMe | ObjectReference | Form akFormToPlace, Int aiCount, Bool... | `0x0140AFC0` | variant_match | GameObjects.cpp:5 |
| SetLinkedRef | Void | ObjectReference akLinkedRef, Keyword ... | `0x00480F00` | variant_match | GameReferences.cpp:19 |
| getLinkedRef | ObjectReference | Keyword apKeyword | `0x00480EE0` | variant_match | GameReferences.cpp:17 |

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Activate | Bool | ObjectReference akActivator, Bool abD... | No | `Bool Function Activate(ObjectReference akActivator, Bool ...` |
| AddDependentAnimatedObjectReference | Bool | ObjectReference akDependent | No | `Bool Function AddDependentAnimatedObjectReference(ObjectR...` |
| AddDynamicTerminalMenuItem | Void | terminal akTemplateSource, Int aiTemp... | No | `Function AddDynamicTerminalMenuItem(terminal akTemplateSo...` |
| AddItem | Void | Form akItemToAdd, Int aiCount, Bool a... | No | `Function AddItem(Form akItemToAdd, Int aiCount, Bool abSi...` |
| AddKeyword | Void | Keyword apKeyword | No | `Function AddKeyword(Keyword apKeyword) Native` |
| AddMultipleTerminalTextReplacementDataForPlayer | Void | String[] asTokenLabels, Form[] akForm... | No | `Function AddMultipleTerminalTextReplacementDataForPlayer(...` |
| AddMultipleTerminalTextReplacementValueForPlayer | Void | String[] asTokenLabels, Float[] aValu... | No | `Function AddMultipleTerminalTextReplacementValueForPlayer...` |
| AddMultipleTextReplacementData | Void | String[] asTokenLabels, Form[] akForms | No | `Function AddMultipleTextReplacementData(String[] asTokenL...` |
| AddMultipleTextReplacementValue | Void | String[] asTokenLabels, Float[] aValues | No | `Function AddMultipleTextReplacementValue(String[] asToken...` |
| AddTerminalTextReplacementDataForPlayer | Void | String asTokenLabel, Form akForm, pla... | No | `Function AddTerminalTextReplacementDataForPlayer(String a...` |
| AddTerminalTextReplacementValueForPlayer | Void | String asTokenLabel, Float aValue, pl... | No | `Function AddTerminalTextReplacementValueForPlayer(String ...` |
| AddTextReplacementData | Void | String asTokenLabel, Form akForm | No | `Function AddTextReplacementData(String asTokenLabel, Form...` |
| AddTextReplacementValue | Void | String asTokenLabel, Float aValue | No | `Function AddTextReplacementValue(String asTokenLabel, Flo...` |
| ApplyConveyorBelt | Void | String aTarget, Float aLinVelX, Float... | No | `Function ApplyConveyorBelt(String aTarget, Float aLinVelX...` |
| ApplyFanMotor | Void | String aTarget, Float aAxisX, Float a... | No | `Function ApplyFanMotor(String aTarget, Float aAxisX, Floa...` |
| ApplyHavokImpulse | Void | Float afX, Float afY, Float afZ, Floa... | No | `Function ApplyHavokImpulse(Float afX, Float afY, Float af...` |
| AttachMod | Bool | objectmod akMod, Int aiAttachIndex | No | `Bool Function AttachMod(objectmod akMod, Int aiAttachInde...` |
| AttachModToInventoryItem | Bool | Form akItem, objectmod akMod | No | `Bool Function AttachModToInventoryItem(Form akItem, objec...` |
| AttachTo | Void | ObjectReference akParent | No | `Function AttachTo(ObjectReference akParent) Native` |
| BlockActivation | Void | Bool abBlocked, Bool abHideActivateText | No | `Function BlockActivation(Bool abBlocked, Bool abHideActiv...` |
| CalculateEncounterLevel | Int | Int aiDifficulty | No | `Int Function CalculateEncounterLevel(Int aiDifficulty) Na...` |
| CanProduceForWorkshop | Bool | () | No | `Bool Function CanProduceForWorkshop() Native` |
| ClearDestruction | Void | () | No | `Function ClearDestruction() Native` |
| ClearDynamicTerminalMenuItems | Void | terminal akTemplateSource | No | `Function ClearDynamicTerminalMenuItems(terminal akTemplat...` |
| ClearFromOldLocations | Void | () | No | `Function ClearFromOldLocations() Native` |
| ClearHolotape | Void | () | No | `Function ClearHolotape() Native` |
| ConveyorBeltOn | Void | Bool abOn | No | `Function ConveyorBeltOn(Bool abOn) Native` |
| CountActorsLinkedToMe | Int | Keyword apLinkKeyword, Keyword apExcl... | No | `Int Function CountActorsLinkedToMe(Keyword apLinkKeyword,...` |
| CountRefsLinkedToMe | Int | Keyword apLinkKeyword, Keyword apExcl... | No | `Int Function CountRefsLinkedToMe(Keyword apLinkKeyword, K...` |
| CreateDetectionEvent | Void | Actor akOwner, Int aiSoundLevel | No | `Function CreateDetectionEvent(Actor akOwner, Int aiSoundL...` |
| DamageObject | Void | Float afDamage | No | `Function DamageObject(Float afDamage) Native` |
| DamageValue | Void | ActorValue akAV, Float afDamage | No | `Function DamageValue(ActorValue akAV, Float afDamage) Native` |
| Delete | Void | () | No | `Function Delete() Native` |
| Disable | Void | Bool abFadeOut | No | `Function Disable(Bool abFadeOut) Native` |
| DisableLinkChain | Void | Keyword apKeyword, Bool abFadeOut | No | `Function DisableLinkChain(Keyword apKeyword, Bool abFadeO...` |
| DisableNoWait | Void | Bool abFadeOut | No | `Function DisableNoWait(Bool abFadeOut) Native` |
| Drop | Void | Bool abSilent | No | `Function Drop(Bool abSilent) Native` |
| DropFirstObject | ObjectReference | Bool abInitiallyDisabled | No | `ObjectReference Function DropFirstObject(Bool abInitially...` |
| DropObject | ObjectReference | Form akObject, Int aiCount | No | `ObjectReference Function DropObject(Form akObject, Int ai...` |
| Enable | Void | Bool abFadeIn | No | `Function Enable(Bool abFadeIn) Native` |
| EnableLinkChain | Void | Keyword apKeyword, Bool abFadeIn | No | `Function EnableLinkChain(Keyword apKeyword, Bool abFadeIn...` |
| EnableNoWait | Void | Bool abFadeIn | No | `Function EnableNoWait(Bool abFadeIn) Native` |
| Equip | Void | Bool abPreventRemoval, Bool abSilent | No | `Function Equip(Bool abPreventRemoval, Bool abSilent) Native` |
| FanMotorOn | Void | Bool abOn | No | `Function FanMotorOn(Bool abOn) Native` |
| FindAllReferencesOfType | ObjectReference[] | Form akObjectOrList, Float afRadius | No | `ObjectReference[] Function FindAllReferencesOfType(Form a...` |
| FindAllReferencesWithKeyword | ObjectReference[] | Form akKeywordOrList, Float afRadius,... | No | `ObjectReference[] Function FindAllReferencesWithKeyword(F...` |
| FindClosestReferenceOfAnyTypeInList | ObjectReference | FormList arBaseObjects, Float afRadius | No | `ObjectReference Function FindClosestReferenceOfAnyTypeInL...` |
| FindClosestReferenceOfType | ObjectReference | Form arBaseObject, Float afRadius | No | `ObjectReference Function FindClosestReferenceOfType(Form ...` |
| FindClosestValidReferenceOfType | ObjectReference | Form arBaseObject, Float afRadius | No | `ObjectReference Function FindClosestValidReferenceOfType(...` |
| FindRandomReferenceOfAnyTypeInList | ObjectReference | FormList arBaseObjects, Float afRadius | No | `ObjectReference Function FindRandomReferenceOfAnyTypeInLi...` |
| FindRandomReferenceOfType | ObjectReference | Form arBaseObject, Float afRadius | No | `ObjectReference Function FindRandomReferenceOfType(Form a...` |
| FindRandomReferenceWithKeyword | ObjectReference | Form akKeywordOrList, Float afRadius,... | No | `ObjectReference Function FindRandomReferenceWithKeyword(F...` |
| ForceActorDecay | Void | () | No | `Function ForceActorDecay() Native` |
| ForceAddRagdollToWorld | Void | () | No | `Function ForceAddRagdollToWorld() Native` |
| ForceRemoveRagdollFromWorld | Void | () | No | `Function ForceRemoveRagdollFromWorld() Native` |
| ForceSwapModelOnClient | Void | ObjectReference akRefrWithNewModel | No | `Function ForceSwapModelOnClient(ObjectReference akRefrWit...` |
| GetActivateParents | ObjectReference[] | () | No | `ObjectReference[] Function GetActivateParents() Native` |
| GetActorCause | Actor | () | No | `Actor Function GetActorCause() Native` |
| GetActorOwner | ActorBase | () | No | `ActorBase Function GetActorOwner() Native` |
| GetActorRefOwner | Actor | () | No | `Actor Function GetActorRefOwner() Native` |
| GetActorsLinkedToMe | Actor[] | Keyword apLinkKeyword, Keyword apExcl... | No | `Actor[] Function GetActorsLinkedToMe(Keyword apLinkKeywor...` |
| GetAngleX | Float | () | No | `Float Function GetAngleX() Native` |
| GetAngleY | Float | () | No | `Float Function GetAngleY() Native` |
| GetAngleZ | Float | () | No | `Float Function GetAngleZ() Native` |
| GetAnimationVariableBool | Bool | String arVariableName | No | `Bool Function GetAnimationVariableBool(String arVariableN...` |
| GetAnimationVariableFloat | Float | String arVariableName | No | `Float Function GetAnimationVariableFloat(String arVariabl...` |
| GetAnimationVariableInt | Int | String arVariableName | No | `Int Function GetAnimationVariableInt(String arVariableNam...` |
| GetArrayOfDamagingActors | Actor[] | Float afMinDamage, Bool abAsPercent | No | `Actor[] Function GetArrayOfDamagingActors(Float afMinDama...` |
| GetBaseObject | Form | () | No | `Form Function GetBaseObject() Native` |
| GetBaseValue | Float | ActorValue akAV | No | `Float Function GetBaseValue(ActorValue akAV) Native` |
| GetBuiltBy | player | () | No | `player Function GetBuiltBy() Native` |
| GetComponentCount | Int | Form akItem, Bool abIncludeStash | No | `Int Function GetComponentCount(Form akItem, Bool abInclud...` |
| GetContainer | ObjectReference | () | No | `ObjectReference Function GetContainer() Native` |
| GetContainerSearched | Bool | () | No | `Bool Function GetContainerSearched() Native` |
| GetCurrentDestructionStage | Int | () | No | `Int Function GetCurrentDestructionStage() Native` |
| GetCurrentLocation | Location | () | No | `Location Function GetCurrentLocation() Native` |
| GetCurrentScene | sceneinstance | () | No | `sceneinstance Function GetCurrentScene() Native` |
| GetDestructibleHealthPercent | Float | () | No | `Float Function GetDestructibleHealthPercent() Native` |
| GetDistance | Float | ObjectReference akOther | No | `Float Function GetDistance(ObjectReference akOther) Native` |
| GetEditorLocation | Location | () | No | `Location Function GetEditorLocation() Native` |
| GetEncounterZone | Location | () | No | `Location Function GetEncounterZone() Native` |
| GetFactionOwner | Faction | () | No | `Faction Function GetFactionOwner() Native` |
| GetFactionRank | Int | Faction akFaction | No | `Int Function GetFactionRank(Faction akFaction) Native` |
| GetFurnitureMarkerUser | Actor | Int aiMarker, Bool abIgnoreReserved | No | `Actor Function GetFurnitureMarkerUser(Int aiMarker, Bool ...` |
| GetFurnitureUsers | Actor[] | Bool abIgnoreReserved | No | `Actor[] Function GetFurnitureUsers(Bool abIgnoreReserved)...` |
| GetHeadingAngle | Float | ObjectReference akOther | No | `Float Function GetHeadingAngle(ObjectReference akOther) N...` |
| GetHeight | Float | () | No | `Float Function GetHeight() Native` |
| GetHighestItemCountKeywords | Int | FormList akKeywords, Bool abMustMatchAll | No | `Int Function GetHighestItemCountKeywords(FormList akKeywo...` |
| GetIgnorePlayerDamage | Bool | () | No | `Bool Function GetIgnorePlayerDamage() Native` |
| GetInventoryValue | Int | () | No | `Int Function GetInventoryValue() Native` |
| GetItemCount | Int | Form akItem, Bool abIncludeStash | No | `Int Function GetItemCount(Form akItem, Bool abIncludeStas...` |
| GetItemCountKeywords | Int | FormList akKeywords, Bool abMustMatchAll | No | `Int Function GetItemCountKeywords(FormList akKeywords, Bo...` |
| GetItemFormsWithKeywords | Form[] | FormList akKeywords, Bool abMustMatch... | No | `Form[] Function GetItemFormsWithKeywords(FormList akKeywo...` |
| GetItemHealthPercent | Float | () | No | `Float Function GetItemHealthPercent() Native` |
| GetKey | Key | () | No | `Key Function GetKey() Native` |
| GetKeypadCodeLength | Int | () | No | `Int Function GetKeypadCodeLength() Native` |
| GetLength | Float | () | No | `Float Function GetLength() Native` |
| GetLinkedRefChain | ObjectReference[] | Keyword apKeyword, Int iMaxExpectedLi... | No | `ObjectReference[] Function GetLinkedRefChain(Keyword apKe...` |
| GetLocRefTypes | LocationRefType[] | () | No | `LocationRefType[] Function GetLocRefTypes() Native` |
| GetLocationsWithinRange | Location[] | Float afRange, FormList apIncludeList... | No | `Location[] Function GetLocationsWithinRange(Float afRange...` |
| GetLockLevel | Int | () | No | `Int Function GetLockLevel() Native` |
| GetMass | Float | () | No | `Float Function GetMass() Native` |
| GetNearbyPlayers | player[] | Float findRange | No | `player[] Function GetNearbyPlayers(Float findRange) Native` |
| GetNthLinkedRef | ObjectReference | Int aiLinkedRef, Keyword apKeyword | No | `ObjectReference Function GetNthLinkedRef(Int aiLinkedRef,...` |
| GetOpenState | Int | () | No | `Int Function GetOpenState() Native` |
| GetOutfit | Outfit | () | No | `Outfit Function GetOutfit() Native` |
| GetParentCell | Cell | () | No | `Cell Function GetParentCell() Native` |
| GetParentRegion | region | Bool aOnlyStatic | No | `region Function GetParentRegion(Bool aOnlyStatic) Native` |
| GetPositionX | Float | () | No | `Float Function GetPositionX() Native` |
| GetPositionY | Float | () | No | `Float Function GetPositionY() Native` |
| GetPositionZ | Float | () | No | `Float Function GetPositionZ() Native` |
| GetRadioFrequency | Float | () | No | `Float Function GetRadioFrequency() Native` |
| GetRadioVolume | Float | () | No | `Float Function GetRadioVolume() Native` |
| GetRefsLinkedToMe | ObjectReference[] | Keyword apLinkKeyword, Keyword apExcl... | No | `ObjectReference[] Function GetRefsLinkedToMe(Keyword apLi...` |
| GetResourceDamage | Float | ActorValue akValue | No | `Float Function GetResourceDamage(ActorValue akValue) Native` |
| GetSafePosition | Float[] | Float aSearchRadius, Float aSafeRadius | No | `Float[] Function GetSafePosition(Float aSearchRadius, Flo...` |
| GetScale | Float | () | No | `Float Function GetScale() Native` |
| GetSimpleNetworkState | Int | () | No | `Int Function GetSimpleNetworkState() Native` |
| GetSyncAnimationProgress | Float | () | No | `Float Function GetSyncAnimationProgress() Native` |
| GetTeleportCell | Cell | () | No | `Cell Function GetTeleportCell() Native` |
| GetTransitionCell | Cell | () | No | `Cell Function GetTransitionCell() Native` |
| GetTriggerObjectCount | Int | () | No | `Int Function GetTriggerObjectCount() Native` |
| GetValue | Float | ActorValue akAV | No | `Float Function GetValue(ActorValue akAV) Native` |
| GetValuePercentage | Float | ActorValue akAV | No | `Float Function GetValuePercentage(ActorValue akAV) Native` |
| GetVoiceType | VoiceType | () | No | `VoiceType Function GetVoiceType() Native` |
| GetWidth | Float | () | No | `Float Function GetWidth() Native` |
| GetWorkshop | ObjectReference | () | No | `ObjectReference Function GetWorkshop() Native` |
| GetWorkshopClaimant | player | () | No | `player Function GetWorkshopClaimant() Native` |
| GetWorkshopOwnedObjects | ObjectReference[] | Actor akActor | No | `ObjectReference[] Function GetWorkshopOwnedObjects(Actor ...` |
| GetWorkshopOwner | player | () | No | `player Function GetWorkshopOwner() Native` |
| GetWorkshopResourceDamage | Float | ActorValue akValue | No | `Float Function GetWorkshopResourceDamage(ActorValue akVal...` |
| GetWorkshopResourceObjects | ObjectReference[] | ActorValue akAV, Int aiOption | No | `ObjectReference[] Function GetWorkshopResourceObjects(Act...` |
| HasActivateParents | Bool | () | No | `Bool Function HasActivateParents() Native` |
| HasActorRefOwner | Bool | () | No | `Bool Function HasActorRefOwner() Native` |
| HasDirectLOS | Bool | ObjectReference akTarget, String asSo... | No | `Bool Function HasDirectLOS(ObjectReference akTarget, Stri...` |
| HasEffectKeyword | Bool | Keyword akKeyword | No | `Bool Function HasEffectKeyword(Keyword akKeyword) Native` |
| HasKeyword | Bool | Keyword apKeyword | No | `Bool Function HasKeyword(Keyword apKeyword) Native` |
| HasKeywordInFormList | Bool | FormList akKeywordList | No | `Bool Function HasKeywordInFormList(FormList akKeywordList...` |
| HasLocRefType | Bool | LocationRefType akRefType | No | `Bool Function HasLocRefType(LocationRefType akRefType) Na...` |
| HasNode | Bool | String asNodeName | No | `Bool Function HasNode(String asNodeName) Native` |
| HasSharedPowerGrid | Bool | ObjectReference akCompare | No | `Bool Function HasSharedPowerGrid(ObjectReference akCompar...` |
| IgnoreFriendlyHits | Void | Bool abIgnore | No | `Function IgnoreFriendlyHits(Bool abIgnore) Native` |
| InstanceHasKeyword | Bool | Keyword apKeyword | No | `Bool Function InstanceHasKeyword(Keyword apKeyword) Native` |
| InterruptCast | Void | () | No | `Function InterruptCast() Native` |
| Is3DLoaded | Bool | () | No | `Bool Function Is3DLoaded() Native` |
| IsAPlayer | Bool | () | No | `Bool Function IsAPlayer() Native` |
| IsActivateChild | Bool | ObjectReference akChild | No | `Bool Function IsActivateChild(ObjectReference akChild) Na...` |
| IsActivationBlocked | Bool | () | No | `Bool Function IsActivationBlocked() Native` |
| IsConveyorBeltOn | Bool | () | No | `Bool Function IsConveyorBeltOn() Native` |
| IsCreated | Bool | () | No | `Bool Function IsCreated() Native` |
| IsDeleted | Bool | () | No | `Bool Function IsDeleted() Native` |
| IsDestroyed | Bool | () | No | `Bool Function IsDestroyed() Native` |
| IsDetachedCamp | Bool | () | No | `Bool Function IsDetachedCamp() Native` |
| IsDisabled | Bool | () | No | `Bool Function IsDisabled() Native` |
| IsDispenserItem | Bool | () | No | `Bool Function IsDispenserItem() Native` |
| IsFanMotorOn | Bool | () | No | `Bool Function IsFanMotorOn() Native` |
| IsFurnitureInUse | Bool | Bool abIgnoreReserved | No | `Bool Function IsFurnitureInUse(Bool abIgnoreReserved) Native` |
| IsFurnitureMarkerInUse | Bool | Int aiMarker, Bool abIgnoreReserved | No | `Bool Function IsFurnitureMarkerInUse(Int aiMarker, Bool a...` |
| IsIgnoringFriendlyHits | Bool | () | No | `Bool Function IsIgnoringFriendlyHits() Native` |
| IsInDialogueWithPlayer | Bool | () | No | `Bool Function IsInDialogueWithPlayer() Native` |
| IsInFaction | Bool | Faction akFaction | No | `Bool Function IsInFaction(Faction akFaction) Native` |
| IsInNukeZone | Bool | () | No | `Bool Function IsInNukeZone() Native` |
| IsInShelter | Bool | () | No | `Bool Function IsInShelter() Native` |
| IsLocalPlayer | Bool | () | No | `Bool Function IsLocalPlayer() Native` |
| IsLockBroken | Bool | Actor akActor | No | `Bool Function IsLockBroken(Actor akActor) Native` |
| IsLocked | Bool | () | No | `Bool Function IsLocked() Native` |
| IsMapMarkerVisible | Bool | player akPlayer | No | `Bool Function IsMapMarkerVisible(player akPlayer) Native` |
| IsOwnedBy | Bool | Actor akOwner | No | `Bool Function IsOwnedBy(Actor akOwner) Native` |
| IsPowered | Bool | () | No | `Bool Function IsPowered() Native` |
| IsProducer | Bool | () | No | `Bool Function IsProducer() Native` |
| IsQuestItem | Bool | () | No | `Bool Function IsQuestItem() Native` |
| IsRadioOn | Bool | () | No | `Bool Function IsRadioOn() Native` |
| IsRefInTransitionCell | Bool | ObjectReference akRef | No | `Bool Function IsRefInTransitionCell(ObjectReference akRef...` |
| IsSpellTarget | Bool | Form akMagicItemForm | No | `Bool Function IsSpellTarget(Form akMagicItemForm) Native` |
| IsWithinBuildableArea | Bool | ObjectReference akRef | No | `Bool Function IsWithinBuildableArea(ObjectReference akRef...` |
| KnockAreaEffect | Void | Float afMagnitude, Float afRadius | No | `Function KnockAreaEffect(Float afMagnitude, Float afRadiu...` |
| Lock | Void | Bool abLock, Bool abAsOwner | No | `Function Lock(Bool abLock, Bool abAsOwner) Native` |
| MakeRadioReceiver | Void | Float afFrequency, Float afVolume, ou... | No | `Function MakeRadioReceiver(Float afFrequency, Float afVol...` |
| MarkQPClientDataInitializationComplete | Void | () | No | `Function MarkQPClientDataInitializationComplete() Native` |
| ModValue | Void | ActorValue akAV, Float afAmount | No | `Function ModValue(ActorValue akAV, Float afAmount) Native` |
| MoveNukeTo | Void | Float afX, Float afY, Float afZ | No | `Function MoveNukeTo(Float afX, Float afY, Float afZ) Native` |
| MoveToMyEditorLocation | Void | () | No | `Function MoveToMyEditorLocation() Native` |
| MoveToNearestNavmeshLocation | Void | () | No | `Function MoveToNearestNavmeshLocation() Native` |
| MoveToNode | Void | ObjectReference akTarget, String asNo... | No | `Function MoveToNode(ObjectReference akTarget, String asNo...` |
| OpenWorkshopSettlementMenu | Location | Keyword akActionKW, Message astrConfi... | No | `Location Function OpenWorkshopSettlementMenu(Keyword akAc...` |
| OpenWorkshopSettlementMenuEx | Location | Keyword akActionKW, Message astrConfi... | No | `Location Function OpenWorkshopSettlementMenuEx(Keyword ak...` |
| PauseAudio | Void | () | No | `Function PauseAudio() Native` |
| PlaceActorAtMe | Actor | ActorBase akActorToPlace, Int aiLevel... | No | `Actor Function PlaceActorAtMe(ActorBase akActorToPlace, I...` |
| PlaceAtNode | ObjectReference | String asNodeName, Form akFormToPlace... | No | `ObjectReference Function PlaceAtNode(String asNodeName, F...` |
| PlayAnimation | Bool | String asAnimation | No | `Bool Function PlayAnimation(String asAnimation) Native` |
| PlayAnimationAndWait | Bool | String asAnimation, String asEventName | No | `Bool Function PlayAnimationAndWait(String asAnimation, St...` |
| PlayGamebryoAnimation | Bool | String asAnimation, Bool abStartOver,... | No | `Bool Function PlayGamebryoAnimation(String asAnimation, B...` |
| PlayImpactEffect | Bool | ImpactDataSet akImpactEffect, String ... | No | `Bool Function PlayImpactEffect(ImpactDataSet akImpactEffe...` |
| PlaySyncedAnimationAndWaitSS | Bool | String asAnimation1, String asEvent1,... | No | `Bool Function PlaySyncedAnimationAndWaitSS(String asAnima...` |
| PlaySyncedAnimationSS | Bool | String asAnimation1, ObjectReference ... | No | `Bool Function PlaySyncedAnimationSS(String asAnimation1, ...` |
| PlayTerrainEffect | Void | String asEffectModelName, String asAt... | No | `Function PlayTerrainEffect(String asEffectModelName, Stri...` |
| ProcessTrapHit | Void | ObjectReference akTrap, Float afDamag... | No | `Function ProcessTrapHit(ObjectReference akTrap, Float afD...` |
| PushActorAway | Void | Actor akActorToPush, Float aiKnockbac... | No | `Function PushActorAway(Actor akActorToPush, Float aiKnock...` |
| RaidTargetsAvailable | Int | Keyword akActionKW, Message astrConfi... | No | `Int Function RaidTargetsAvailable(Keyword akActionKW, Mes...` |
| ReleaseToHavok | Bool | Bool aHasGravity, Bool aAllowActivate | No | `Bool Function ReleaseToHavok(Bool aHasGravity, Bool aAllo...` |
| RemoveAllItems | Void | ObjectReference akTransferTo, Bool ab... | No | `Function RemoveAllItems(ObjectReference akTransferTo, Boo...` |
| RemoveAllMods | Void | () | No | `Function RemoveAllMods() Native` |
| RemoveAllModsFromInventoryItem | Void | Form akItem | No | `Function RemoveAllModsFromInventoryItem(Form akItem) Native` |
| RemoveComponents | Int | component akComponent, Int aiCount, B... | No | `Int Function RemoveComponents(component akComponent, Int ...` |
| RemoveDependentAnimatedObjectReference | Bool | ObjectReference akDependent | No | `Bool Function RemoveDependentAnimatedObjectReference(Obje...` |
| RemoveItem | Int | Form akItemToRemove, Int aiCount, Boo... | No | `Int Function RemoveItem(Form akItemToRemove, Int aiCount,...` |
| RemoveItemByComponent | Int | Form akComponentToRemove, Int aiCount... | No | `Int Function RemoveItemByComponent(Form akComponentToRemo...` |
| RemoveKeyword | Void | Keyword apKeyword | No | `Function RemoveKeyword(Keyword apKeyword) Native` |
| RemoveMod | Void | objectmod akMod | No | `Function RemoveMod(objectmod akMod) Native` |
| RemoveModFromInventoryItem | Void | Form akItem, objectmod akMod | No | `Function RemoveModFromInventoryItem(Form akItem, objectmo...` |
| Repair | Void | Float aPercentage | No | `Function Repair(Float aPercentage) Native` |
| Reset | Void | ObjectReference akTarget | No | `Function Reset(ObjectReference akTarget) Native` |
| ResetKeyword | Void | Keyword apKeyword | No | `Function ResetKeyword(Keyword apKeyword) Native` |
| RestoreValue | Void | ActorValue akAV, Float afAmount | No | `Function RestoreValue(ActorValue akAV, Float afAmount) Na...` |
| ResumeAudio | Void | () | No | `Function ResumeAudio() Native` |
| ReverseConveyorBelt | Void | Bool abReverse | No | `Function ReverseConveyorBelt(Bool abReverse) Native` |
| Say | Bool | Topic akTopicToSay, questinstance akQ... | No | `Bool Function Say(Topic akTopicToSay, questinstance akQue...` |
| SayAndWait | Bool | Topic akTopicToSay, questinstance akQ... | No | `Bool Function SayAndWait(Topic akTopicToSay, questinstanc...` |
| SayCustom | Bool | Keyword akKeywordToSay, Actor akActor... | No | `Bool Function SayCustom(Keyword akKeywordToSay, Actor akA...` |
| SayCustomAndWait | Bool | Keyword akKeywordToSay, Actor akActor... | No | `Bool Function SayCustomAndWait(Keyword akKeywordToSay, Ac...` |
| SetActivateTextOverride | Void | Message akText | No | `Function SetActivateTextOverride(Message akText) Native` |
| SetActorCause | Void | Actor akActor | No | `Function SetActorCause(Actor akActor) Native` |
| SetActorOwner | Void | ActorBase akActorBase, Bool abNoCrime | No | `Function SetActorOwner(ActorBase akActorBase, Bool abNoCr...` |
| SetActorRefOwner | Void | Actor akActor, Bool abNoCrime | No | `Function SetActorRefOwner(Actor akActor, Bool abNoCrime) ...` |
| SetAngle | Void | Float afXAngle, Float afYAngle, Float... | No | `Function SetAngle(Float afXAngle, Float afYAngle, Float a...` |
| SetAnimationVariableBool | Void | String arVariableName, Bool abNewValue | No | `Function SetAnimationVariableBool(String arVariableName, ...` |
| SetAnimationVariableFloat | Void | String arVariableName, Float afNewValue | No | `Function SetAnimationVariableFloat(String arVariableName,...` |
| SetAnimationVariableInt | Void | String arVariableName, Int aiNewValue | No | `Function SetAnimationVariableInt(String arVariableName, I...` |
| SetAttractionActive | Void | Keyword apKeyword, Bool abActive | No | `Function SetAttractionActive(Keyword apKeyword, Bool abAc...` |
| SetConveyorBeltVelocity | Void | Float afLinVelX, Float afLinVelY, Flo... | No | `Function SetConveyorBeltVelocity(Float afLinVelX, Float a...` |
| SetDestroyed | Void | Bool abDestroyed | No | `Function SetDestroyed(Bool abDestroyed) Native` |
| SetDirectAtTarget | Void | ObjectReference akTarget | No | `Function SetDirectAtTarget(ObjectReference akTarget) Native` |
| SetFactionOwner | Void | Faction akFaction, Bool abNoCrime | No | `Function SetFactionOwner(Faction akFaction, Bool abNoCrim...` |
| SetHarvested | Void | Bool abHarvested | No | `Function SetHarvested(Bool abHarvested) Native` |
| SetIsWorkshopItem | Void | ObjectReference akWorkshop, Bool abValue | No | `Function SetIsWorkshopItem(ObjectReference akWorkshop, Bo...` |
| SetLocRefType | Void | Location akLoc, LocationRefType akRef... | No | `Function SetLocRefType(Location akLoc, LocationRefType ak...` |
| SetLockLevel | Void | Int aiLockLevel | No | `Function SetLockLevel(Int aiLockLevel) Native` |
| SetMotionType | Void | Int aeMotionType, Bool abAllowActivate | No | `Function SetMotionType(Int aeMotionType, Bool abAllowActi...` |
| SetNoFavorAllowed | Void | Bool abNoFavor | No | `Function SetNoFavorAllowed(Bool abNoFavor) Native` |
| SetOpenState | Void | Bool abOpen, Bool abSnap | No | `Function SetOpenState(Bool abOpen, Bool abSnap) Native` |
| SetOverrideName | Void | Message aName | No | `Function SetOverrideName(Message aName) Native` |
| SetPersistLoc | Void | Location akLoc | No | `Function SetPersistLoc(Location akLoc) Native` |
| SetPlayerHasTaken | Void | Bool abTaken | No | `Function SetPlayerHasTaken(Bool abTaken) Native` |
| SetPosition | Void | Float afX, Float afY, Float afZ | No | `Function SetPosition(Float afX, Float afY, Float afZ) Native` |
| SetRadioFrequency | Void | Float afFrequency | No | `Function SetRadioFrequency(Float afFrequency) Native` |
| SetRadioOn | Void | Bool abOn | No | `Function SetRadioOn(Bool abOn) Native` |
| SetScale | Void | Float afScale | No | `Function SetScale(Float afScale) Native` |
| SetValue | Void | ActorValue akAV, Float afValue | No | `Function SetValue(ActorValue akAV, Float afValue) Native` |
| SplineTranslateTo | Void | Float afX, Float afY, Float afZ, Floa... | No | `Function SplineTranslateTo(Float afX, Float afY, Float af...` |
| SplineTranslateToLocal | Void | Float afX, Float afY, Float afZ, Floa... | No | `Function SplineTranslateToLocal(Float afX, Float afY, Flo...` |
| SplineTranslateToRefNode | Void | ObjectReference arTarget, String arNo... | No | `Function SplineTranslateToRefNode(ObjectReference arTarge...` |
| StopTranslation | Void | () | No | `Function StopTranslation() Native` |
| StoreInWorkshop | Void | Form akBaseItem, Int aiCount | No | `Function StoreInWorkshop(Form akBaseItem, Int aiCount) Na...` |
| TetherToHorse | Void | ObjectReference akHorse | No | `Function TetherToHorse(ObjectReference akHorse) Native` |
| TranslateTo | Void | Float afX, Float afY, Float afZ, Floa... | No | `Function TranslateTo(Float afX, Float afY, Float afZ, Flo...` |
| TranslateToLocal | Void | Float afX, Float afY, Float afZ, Floa... | No | `Function TranslateToLocal(Float afX, Float afY, Float afZ...` |
| UpdateAlphaGroupBounds | Void | () | No | `Function UpdateAlphaGroupBounds() Native` |
| UsesCellBasedNetworkingOptimization | Bool | () | No | `Bool Function UsesCellBasedNetworkingOptimization() Native` |
| WaitFor3DLoad | Bool | () | No | `Bool Function WaitFor3DLoad() Native` |
| WaitForAnimationEvent | Bool | String asEventName | No | `Bool Function WaitForAnimationEvent(String asEventName) N...` |
| countLinkedRefChain | Int | Keyword apKeyword, Int maxExpectedLin... | No | `Int Function countLinkedRefChain(Keyword apKeyword, Int m...` |
| getLinkedRefChildren | ObjectReference[] | Keyword apKeyword | No | `ObjectReference[] Function getLinkedRefChildren(Keyword a...` |

### Package
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| GetOwningQuest | Quest | () | No | `Quest Function GetOwningQuest() Native` |
| GetTemplate | Package | () | No | `Package Function GetTemplate() Native` |

### Perk
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| DoFanFare | Void | player akPlayer | No | `Function DoFanFare(player akPlayer) Native` |

### PerkCard
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| GetLevelRequirement | Int | () | No | `Int Function GetLevelRequirement() Native` |
| GetNumRanks | Int | () | No | `Int Function GetNumRanks() Native` |
| GetPerk | Perk | Int aSex, Int aRank | No | `Perk Function GetPerk(Int aSex, Int aRank) Native` |
| GetPerkPointCost | Int | Int aRank | No | `Int Function GetPerkPointCost(Int aRank) Native` |
| GetScrapValue | Int | Int aRank | No | `Int Function GetScrapValue(Int aRank) Native` |
| GetSpecialCategory | Int | () | No | `Int Function GetSpecialCategory() Native` |

### Player
*extends Actor*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| AdvanceSkill | Void | String asSkillName, Float afMagnitude | No | `Function AdvanceSkill(String asSkillName, Float afMagnitu...` |
| FastTravel | Bool | ObjectReference akDestination, Bool a... | No | `Bool Function FastTravel(ObjectReference akDestination, B...` |
| ForceFirstPerson | Void | () | No | `Function ForceFirstPerson() Native` |
| ForceThirdPerson | Void | () | No | `Function ForceThirdPerson() Native` |
| GetBountyState | Int | () | No | `Int Function GetBountyState() Native` |
| GetCapsAmount | Int | () | No | `Int Function GetCapsAmount() Native` |
| GetFollowers | Actor[] | () | No | `Actor[] Function GetFollowers() Native` |
| GetHeadingToStormZoneCenter | Float | () | No | `Float Function GetHeadingToStormZoneCenter() Native` |
| GetHighestLevelAchieved | Int | () | No | `Int Function GetHighestLevelAchieved() Native` |
| GetLastRiddenHorse | Actor | () | No | `Actor Function GetLastRiddenHorse() Native` |
| GetRadioFrequency | Float | () | No | `Float Function GetRadioFrequency() Native` |
| HasSeenBabylonTutorial | Bool | Int aiIndex | No | `Bool Function HasSeenBabylonTutorial(Int aiIndex) Native` |
| HasSeenTutorial | Bool | Int aiTutorialIndex | No | `Bool Function HasSeenTutorial(Int aiTutorialIndex) Native` |
| HasSpawnedIntoBabylonGame | Bool | () | No | `Bool Function HasSpawnedIntoBabylonGame() Native` |
| IncrementSkill | Void | ActorValue akActorValue, Int aiCount | No | `Function IncrementSkill(ActorValue akActorValue, Int aiCo...` |
| IncrementStat | Void | String asStatName, Int aiModAmount | No | `Function IncrementStat(String asStatName, Int aiModAmount...` |
| IsActivateControlsEnabled | Bool | () | No | `Bool Function IsActivateControlsEnabled() Native` |
| IsCamSwitchControlsEnabled | Bool | () | No | `Bool Function IsCamSwitchControlsEnabled() Native` |
| IsConnected | Bool | () | No | `Bool Function IsConnected() Native` |
| IsFactionEnemy | Bool | Faction arFaction | No | `Bool Function IsFactionEnemy(Faction arFaction) Native` |
| IsFastTravelControlsEnabled | Bool | () | No | `Bool Function IsFastTravelControlsEnabled() Native` |
| IsFavoritesControlsEnabled | Bool | () | No | `Bool Function IsFavoritesControlsEnabled() Native` |
| IsFightingControlsEnabled | Bool | () | No | `Bool Function IsFightingControlsEnabled() Native` |
| IsInRadioRange | Bool | Float afFrequency, questinstance akQu... | No | `Bool Function IsInRadioRange(Float afFrequency, questinst...` |
| IsInVATS | Bool | () | No | `Bool Function IsInVATS() Native` |
| IsInsideStormZone | Bool | Float extraRadius | No | `Bool Function IsInsideStormZone(Float extraRadius) Native` |
| IsInventoryWeightBelowAbsoluteLimit | Bool | () | No | `Bool Function IsInventoryWeightBelowAbsoluteLimit() Native` |
| IsJournalControlsEnabled | Bool | () | No | `Bool Function IsJournalControlsEnabled() Native` |
| IsJumpingControlsEnabled | Bool | () | No | `Bool Function IsJumpingControlsEnabled() Native` |
| IsListeningToRadioFrequency | Bool | Float afFrequency, questinstance akQu... | No | `Bool Function IsListeningToRadioFrequency(Float afFrequen...` |
| IsLookingControlsEnabled | Bool | () | No | `Bool Function IsLookingControlsEnabled() Native` |
| IsMenuControlsEnabled | Bool | () | No | `Bool Function IsMenuControlsEnabled() Native` |
| IsMovementControlsEnabled | Bool | () | No | `Bool Function IsMovementControlsEnabled() Native` |
| IsNewCharacter | Bool | () | Yes | `Bool Function IsNewCharacter() Global Native` |
| IsPVPFlagged | Bool | () | No | `Bool Function IsPVPFlagged() Native` |
| IsPacifist | Bool | () | No | `Bool Function IsPacifist() Native` |
| IsRadioOn | Bool | () | No | `Bool Function IsRadioOn() Native` |
| IsSneakingControlsEnabled | Bool | () | No | `Bool Function IsSneakingControlsEnabled() Native` |
| IsVATSControlsEnabled | Bool | () | No | `Bool Function IsVATSControlsEnabled() Native` |
| IsVisitor | Bool | () | No | `Bool Function IsVisitor() Native` |
| QueryStat | Int | String asStat | No | `Int Function QueryStat(String asStat) Native` |
| RadioSignalTrackerStart | Bool | ObjectReference akTransmitter, Object... | No | `Bool Function RadioSignalTrackerStart(ObjectReference akT...` |
| RadioSignalTrackerStop | Void | ObjectReference akTransmitter | No | `Function RadioSignalTrackerStop(ObjectReference akTransmi...` |
| RadioSignalTrackerUpdate | Bool | ObjectReference akTransmitter, Object... | No | `Bool Function RadioSignalTrackerUpdate(ObjectReference ak...` |
| Revive | Void | Player arTarget, Bool abUseAltHealitem | No | `Function Revive(Player arTarget, Bool abUseAltHealitem) N...` |
| SetAIDriven | Void | Bool abAIDriven | No | `Function SetAIDriven(Bool abAIDriven) Native` |
| SetCameraTarget | Void | Actor arTarget | No | `Function SetCameraTarget(Actor arTarget) Native` |
| SetFactionEnemy | Void | Faction arFaction, Bool abIsEnemy | No | `Function SetFactionEnemy(Faction arFaction, Bool abIsEnem...` |
| SetOnElevator | Void | Bool abOnElevator | No | `Function SetOnElevator(Bool abOnElevator) Native` |
| SetReportCrime | Void | Bool abReportCrime | No | `Function SetReportCrime(Bool abReportCrime) Native` |
| SetSeenBabylonTutorial | Void | Int aiIndex, Bool abSeen | No | `Function SetSeenBabylonTutorial(Int aiIndex, Bool abSeen)...` |
| SetSeenTutorial | Void | Int aiTutorialIndex, Bool abSeen | No | `Function SetSeenTutorial(Int aiTutorialIndex, Bool abSeen...` |
| SetSittingRotation | Void | Float afValue | No | `Function SetSittingRotation(Float afValue) Native` |
| ShakeCamera | Void | ObjectReference akSource, Float afStr... | Yes | `Function ShakeCamera(ObjectReference akSource, Float afSt...` |
| ShakeController | Void | Float afSmallMotorStrength, Float afB... | Yes | `Function ShakeController(Float afSmallMotorStrength, Floa...` |
| ShowAtomicShopMenu | Void | String akBiEvent, Keyword akCategory | Yes | `Function ShowAtomicShopMenu(String akBiEvent, Keyword akC...` |
| ShowCompanionNameMenu | Void | Actor aCompanion | Yes | `Function ShowCompanionNameMenu(Actor aCompanion) Global N...` |
| ShowInsufficientOverseerRankMessage | Void | Float requiredOSRank, Float currentOS... | No | `Function ShowInsufficientOverseerRankMessage(Float requir...` |
| ShowPerksMenu | Void | () | Yes | `Function ShowPerksMenu() Global Native` |
| ShowRaceMenu | Void | Int uiMode, ObjectReference akMenuSpo... | No | `Function ShowRaceMenu(Int uiMode, ObjectReference akMenuS...` |
| ShowSPECIALMenu | Void | () | No | `Function ShowSPECIALMenu() Native` |
| ShowSelfieMenu | Void | () | Yes | `Function ShowSelfieMenu() Global Native` |
| ShowSpecialBuildsMenu | Void | ObjectReference akSource | Yes | `Function ShowSpecialBuildsMenu(ObjectReference akSource) ...` |
| ShowTrainingMenu | Void | Actor aTrainer | No | `Function ShowTrainingMenu(Actor aTrainer) Native` |
| SpawnPickRandomPoint | Void | () | Yes | `Function SpawnPickRandomPoint() Global Native` |
| TravelToExpeditionLocation | Void | Location akLocation | No | `Function TravelToExpeditionLocation(Location akLocation) ...` |
| TriggerScreenBlood | Void | Int aiValue | No | `Function TriggerScreenBlood(Int aiValue) Native` |
| TurnRadioOn | Void | Bool abRadioOn | No | `Function TurnRadioOn(Bool abRadioOn) Native` |
| UsingGamepad | Bool | () | No | `Bool Function UsingGamepad() Native` |

### Potion
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| IsHostile | Bool | () | No | `Bool Function IsHostile() Native` |

### QuickPlayContext
*extends ScriptObject*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| GetPlayerScore | Float | player akActor, Keyword akScore | No | `Float Function GetPlayerScore(player akActor, Keyword akS...` |
| GetPlayersOnTeam | player[] | Int aTeamIndex | No | `player[] Function GetPlayersOnTeam(Int aTeamIndex) Native` |
| GetTeam | Int | player akActor | No | `Int Function GetTeam(player akActor) Native` |
| GetTeamCount | Int | () | No | `Int Function GetTeamCount() Native` |
| GetTeamScore | Float | Int aTeamIndex, Keyword akScore | No | `Float Function GetTeamScore(Int aTeamIndex, Keyword akSco...` |

### ScriptObject

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| AddInventoryEventFilter | Void | Form akFilter | No | `Function AddInventoryEventFilter(Form akFilter) Native` |
| AddLocationChangeEventFilter | Void | ScriptObject akFilter | No | `Function AddLocationChangeEventFilter(ScriptObject akFilt...` |
| CallFunction | Var | String asFuncName, Var[] aParams | No | `Var Function CallFunction(String asFuncName, Var[] aParam...` |
| CallFunctionNoWait | Void | String asFuncName, Var[] aParams | No | `Function CallFunctionNoWait(String asFuncName, Var[] aPar...` |
| CancelTimer | Void | Int aiTimerID | No | `Function CancelTimer(Int aiTimerID) Native` |
| CancelTimerAbsoluteTime | Void | Int aiTimerID | No | `Function CancelTimerAbsoluteTime(Int aiTimerID) Native` |
| CancelTimerGameTime | Void | Int aiTimerID | No | `Function CancelTimerGameTime(Int aiTimerID) Native` |
| CancelTimerTimePointTime | Void | Int aiTimerID | No | `Function CancelTimerTimePointTime(Int aiTimerID) Native` |
| CastAs | ScriptObject | String asScriptName | No | `ScriptObject Function CastAs(String asScriptName) Native` |
| GetPropertyValue | Var | String asPropertyName | No | `Var Function GetPropertyValue(String asPropertyName) Native` |
| IsBoundGameObjectAvailable | Bool | () | No | `Bool Function IsBoundGameObjectAvailable() Native` |
| LockAcquire | Void | Int aiLockid | No | `Function LockAcquire(Int aiLockid) Native` |
| LockRelease | Void | Int aiLockid | No | `Function LockRelease(Int aiLockid) Native` |
| ModTimer | Void | Float afModAmount, Int aiTimerID | No | `Function ModTimer(Float afModAmount, Int aiTimerID) Native` |
| ModTimerAbsoluteTime | Void | Float afModAmount, Int aiTimerID | No | `Function ModTimerAbsoluteTime(Float afModAmount, Int aiTi...` |
| ModTimerGameTime | Void | Float afModAmount, Int aiTimerID | No | `Function ModTimerGameTime(Float afModAmount, Int aiTimerI...` |
| PauseTimer | Void | Int aiTimerID, Bool abPause | No | `Function PauseTimer(Int aiTimerID, Bool abPause) Native` |
| PauseTimerGameTime | Void | Int aiTimerID, Bool abPause | No | `Function PauseTimerGameTime(Int aiTimerID, Bool abPause) ...` |
| RegisterAllPlayersForDistanceGreaterThanEvent | Void | ScriptObject akObj1, Float afDistance | No | `Function RegisterAllPlayersForDistanceGreaterThanEvent(Sc...` |
| RegisterAllPlayersForDistanceLessThanEvent | Void | ScriptObject akObj1, Float afDistance | No | `Function RegisterAllPlayersForDistanceLessThanEvent(Scrip...` |
| RegisterForAllPlayersEvents | Bool | String asEventName | No | `Bool Function RegisterForAllPlayersEvents(String asEventN...` |
| RegisterForAnimationEvent | Bool | ObjectReference akSender, String asEv... | No | `Bool Function RegisterForAnimationEvent(ObjectReference a...` |
| RegisterForChallengeCompleteEvent | Void | challenge akChallenge, player akPlayer | No | `Function RegisterForChallengeCompleteEvent(challenge akCh...` |
| RegisterForCustomEvent | Void | ScriptObject akSender, String asEvent... | No | `Function RegisterForCustomEvent(ScriptObject akSender, St...` |
| RegisterForDamageDealtEvent | Void | ScriptObject akAggressor, ScriptObjec... | No | `Function RegisterForDamageDealtEvent(ScriptObject akAggre...` |
| RegisterForDetectionLOSGain | Void | Actor akViewer, ObjectReference akTarget | No | `Function RegisterForDetectionLOSGain(Actor akViewer, Obje...` |
| RegisterForDetectionLOSLost | Void | Actor akViewer, ObjectReference akTarget | No | `Function RegisterForDetectionLOSLost(Actor akViewer, Obje...` |
| RegisterForDirectLOSGain | Void | ObjectReference akViewer, ObjectRefer... | No | `Function RegisterForDirectLOSGain(ObjectReference akViewe...` |
| RegisterForDirectLOSLost | Void | ObjectReference akViewer, ObjectRefer... | No | `Function RegisterForDirectLOSLost(ObjectReference akViewe...` |
| RegisterForDistanceGreaterThanEvent | Void | ScriptObject akObj1, ScriptObject akO... | No | `Function RegisterForDistanceGreaterThanEvent(ScriptObject...` |
| RegisterForDistanceLessThanEvent | Void | ScriptObject akObj1, ScriptObject akO... | No | `Function RegisterForDistanceLessThanEvent(ScriptObject ak...` |
| RegisterForHitEvent | Void | ScriptObject akTarget, ScriptObject a... | No | `Function RegisterForHitEvent(ScriptObject akTarget, Scrip...` |
| RegisterForHitEventFromAllPlayers | Void | ScriptObject akTarget, Form akSourceF... | No | `Function RegisterForHitEventFromAllPlayers(ScriptObject a...` |
| RegisterForLooksMenuEvent | Void | () | No | `Function RegisterForLooksMenuEvent() Native` |
| RegisterForMagicEffectApplyEvent | Void | ScriptObject akTarget, ScriptObject a... | No | `Function RegisterForMagicEffectApplyEvent(ScriptObject ak...` |
| RegisterForMenuOpenCloseEvent | Void | String asMenuName | No | `Function RegisterForMenuOpenCloseEvent(String asMenuName)...` |
| RegisterForMessageBoxPressEvent | Void | Message akMessage | No | `Function RegisterForMessageBoxPressEvent(Message akMessag...` |
| RegisterForPlayerConnectionEvent | Void | player[] akPlayerFilter | No | `Function RegisterForPlayerConnectionEvent(player[] akPlay...` |
| RegisterForPlayerSleep | Void | () | No | `Function RegisterForPlayerSleep() Native` |
| RegisterForPlayerTeleport | Void | () | No | `Function RegisterForPlayerTeleport() Native` |
| RegisterForPlayerWait | Void | () | No | `Function RegisterForPlayerWait() Native` |
| RegisterForPlayerWorkshopObjectPlaced | Void | player akTarget | No | `Function RegisterForPlayerWorkshopObjectPlaced(player akT...` |
| RegisterForPlayerWorkshopObjectRemoved | Void | player akTarget | No | `Function RegisterForPlayerWorkshopObjectRemoved(player ak...` |
| RegisterForRadiationDamageEvent | Void | ScriptObject akTarget | No | `Function RegisterForRadiationDamageEvent(ScriptObject akT...` |
| RegisterForRemoteEvent | Bool | ScriptObject akEventSource, String as... | No | `Bool Function RegisterForRemoteEvent(ScriptObject akEvent...` |
| RegisterForSyncAnimProgress | Void | ObjectReference akAnimatingObject, St... | No | `Function RegisterForSyncAnimProgress(ObjectReference akAn...` |
| RegisterForTrackedStatsEvent | Void | String asStat, Int aiThreshold, playe... | No | `Function RegisterForTrackedStatsEvent(String asStat, Int ...` |
| RegisterForTutorialEvent | Void | String asEventName | No | `Function RegisterForTutorialEvent(String asEventName) Native` |
| RemoveAllInventoryEventFilters | Void | () | No | `Function RemoveAllInventoryEventFilters() Native` |
| RemoveAllLocationChangeEventFilters | Void | () | No | `Function RemoveAllLocationChangeEventFilters() Native` |
| RemoveInventoryEventFilter | Void | Form akFilter | No | `Function RemoveInventoryEventFilter(Form akFilter) Native` |
| RemoveLocationChangeEventFilter | Void | ScriptObject akFilter | No | `Function RemoveLocationChangeEventFilter(ScriptObject akF...` |
| SendCustomEvent | Void | String asEvent, Var[] akArgs | No | `Function SendCustomEvent(String asEvent, Var[] akArgs) Na...` |
| SendRMIToServer | Void | String asFuncName, Var[] aParams | No | `Function SendRMIToServer(String asFuncName, Var[] aParams...` |
| SetPropertyValue | Void | String asPropertyName, Var aValue | No | `Function SetPropertyValue(String asPropertyName, Var aVal...` |
| SetPropertyValueNoWait | Void | String asPropertyName, Var aValue | No | `Function SetPropertyValueNoWait(String asPropertyName, Va...` |
| StartTimer | Void | Float afInterval, Int aiTimerID | No | `Function StartTimer(Float afInterval, Int aiTimerID) Native` |
| StartTimerAbsoluteTime | Void | Float afInterval, Int aiTimerID | No | `Function StartTimerAbsoluteTime(Float afInterval, Int aiT...` |
| StartTimerGameTime | Void | Float afInterval, Int aiTimerID | No | `Function StartTimerGameTime(Float afInterval, Int aiTimer...` |
| StartTimerTimePointTime | Void | Int aiMinute, Int aiHour, Int aiDay, ... | No | `Function StartTimerTimePointTime(Int aiMinute, Int aiHour...` |
| UnregisterAllPlayersForDistanceEvents | Void | ScriptObject akObj1 | No | `Function UnregisterAllPlayersForDistanceEvents(ScriptObje...` |
| UnregisterForAllChallengeCompleteEvents | Void | () | No | `Function UnregisterForAllChallengeCompleteEvents() Native` |
| UnregisterForAllCustomEvents | Void | () | No | `Function UnregisterForAllCustomEvents() Native` |
| UnregisterForAllDamageDealtEvents | Void | ScriptObject akAggressor | No | `Function UnregisterForAllDamageDealtEvents(ScriptObject a...` |
| UnregisterForAllEvents | Void | () | No | `Function UnregisterForAllEvents() Native` |
| UnregisterForAllHitEvents | Void | ScriptObject akTarget | No | `Function UnregisterForAllHitEvents(ScriptObject akTarget)...` |
| UnregisterForAllMagicEffectApplyEvents | Void | ScriptObject akTarget | No | `Function UnregisterForAllMagicEffectApplyEvents(ScriptObj...` |
| UnregisterForAllMenuOpenCloseEvents | Void | () | No | `Function UnregisterForAllMenuOpenCloseEvents() Native` |
| UnregisterForAllMessageBoxPressEvents | Void | () | No | `Function UnregisterForAllMessageBoxPressEvents() Native` |
| UnregisterForAllPlayerWorkshopEvents | Void | () | No | `Function UnregisterForAllPlayerWorkshopEvents() Native` |
| UnregisterForAllPlayersEvents | Void | String asEventName | No | `Function UnregisterForAllPlayersEvents(String asEventName...` |
| UnregisterForAllRadiationDamageEvents | Void | () | No | `Function UnregisterForAllRadiationDamageEvents() Native` |
| UnregisterForAllRemoteEvents | Void | () | No | `Function UnregisterForAllRemoteEvents() Native` |
| UnregisterForAllSyncAnimProgress | Void | () | No | `Function UnregisterForAllSyncAnimProgress() Native` |
| UnregisterForAllTrackedStatsEvents | Void | () | No | `Function UnregisterForAllTrackedStatsEvents() Native` |
| UnregisterForAnimationEvent | Void | ObjectReference akSender, String asEv... | No | `Function UnregisterForAnimationEvent(ObjectReference akSe...` |
| UnregisterForChallengeCompleteEvent | Void | challenge akChallenge, player akPlayer | No | `Function UnregisterForChallengeCompleteEvent(challenge ak...` |
| UnregisterForCustomEvent | Void | ScriptObject akSender, String asEvent... | No | `Function UnregisterForCustomEvent(ScriptObject akSender, ...` |
| UnregisterForDamageDealtEvent | Void | ScriptObject akTarget, ScriptObject a... | No | `Function UnregisterForDamageDealtEvent(ScriptObject akTar...` |
| UnregisterForDistanceEvents | Void | ScriptObject akObj1, ScriptObject akObj2 | No | `Function UnregisterForDistanceEvents(ScriptObject akObj1,...` |
| UnregisterForHitEvent | Void | ScriptObject akTarget, ScriptObject a... | No | `Function UnregisterForHitEvent(ScriptObject akTarget, Scr...` |
| UnregisterForHitEventFromAllPlayers | Void | ScriptObject akTarget, Form akSourceF... | No | `Function UnregisterForHitEventFromAllPlayers(ScriptObject...` |
| UnregisterForLOS | Void | ObjectReference akViewer, ObjectRefer... | No | `Function UnregisterForLOS(ObjectReference akViewer, Objec...` |
| UnregisterForLooksMenuEvent | Void | () | No | `Function UnregisterForLooksMenuEvent() Native` |
| UnregisterForMagicEffectApplyEvent | Void | ScriptObject akTarget, ScriptObject a... | No | `Function UnregisterForMagicEffectApplyEvent(ScriptObject ...` |
| UnregisterForMenuOpenCloseEvent | Void | String asMenuName | No | `Function UnregisterForMenuOpenCloseEvent(String asMenuNam...` |
| UnregisterForMessageBoxPressEvent | Void | Message akMessage | No | `Function UnregisterForMessageBoxPressEvent(Message akMess...` |
| UnregisterForPlayerConnectionEvent | Void | player[] akPlayerFilter | No | `Function UnregisterForPlayerConnectionEvent(player[] akPl...` |
| UnregisterForPlayerSleep | Void | () | No | `Function UnregisterForPlayerSleep() Native` |
| UnregisterForPlayerTeleport | Void | () | No | `Function UnregisterForPlayerTeleport() Native` |
| UnregisterForPlayerWait | Void | () | No | `Function UnregisterForPlayerWait() Native` |
| UnregisterForPlayerWorkshopObjectPlaced | Void | player akTarget | No | `Function UnregisterForPlayerWorkshopObjectPlaced(player a...` |
| UnregisterForPlayerWorkshopObjectRemoved | Void | player akTarget | No | `Function UnregisterForPlayerWorkshopObjectRemoved(player ...` |
| UnregisterForRadiationDamageEvent | Void | ScriptObject akTarget | No | `Function UnregisterForRadiationDamageEvent(ScriptObject a...` |
| UnregisterForRemoteEvent | Void | ScriptObject akEventSource, String as... | No | `Function UnregisterForRemoteEvent(ScriptObject akEventSou...` |
| UnregisterForSyncAnimProgress | Void | ObjectReference akAnimatingObject, In... | No | `Function UnregisterForSyncAnimProgress(ObjectReference ak...` |
| UnregisterForTrackedStatsEvent | Void | String asStat, player akRegisteredPlayer | No | `Function UnregisterForTrackedStatsEvent(String asStat, pl...` |
| UnregisterForTutorialEvent | Void | String asEventName | No | `Function UnregisterForTutorialEvent(String asEventName) N...` |

### ShaderParticleGeometry
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Apply | Void | Float afFadeInTime | No | `Function Apply(Float afFadeInTime) Native` |
| Remove | Void | Float afFadeOutTime | No | `Function Remove(Float afFadeOutTime) Native` |

### Sound
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Play | Int | ObjectReference akSource, String asFo... | No | `Int Function Play(ObjectReference akSource, String asFoll...` |
| PlayAndWait | Bool | ObjectReference akSource, String asFo... | No | `Bool Function PlayAndWait(ObjectReference akSource, Strin...` |
| SetInstanceVolume | Void | Int aiPlaybackInstance, Float afVolume | Yes | `Function SetInstanceVolume(Int aiPlaybackInstance, Float ...` |
| StopInstance | Void | Int aiPlaybackInstance | Yes | `Function StopInstance(Int aiPlaybackInstance) Global Native` |

### SoundCategory
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Mute | Void | Float afFadeSeconds | No | `Function Mute(Float afFadeSeconds) Native` |
| Pause | Void | () | No | `Function Pause() Native` |
| SetFrequency | Void | Float afFrequencyCoeffecient | No | `Function SetFrequency(Float afFrequencyCoeffecient) Native` |
| SetVolume | Void | Float afVolume | No | `Function SetVolume(Float afVolume) Native` |
| UnMute | Void | Float afFadeSeconds | No | `Function UnMute(Float afFadeSeconds) Native` |
| UnPause | Void | () | No | `Function UnPause() Native` |

### SoundCategorySnapshot
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Push | Void | Float afTransitionSecs | No | `Function Push(Float afTransitionSecs) Native` |
| Remove | Void | () | No | `Function Remove() Native` |

### Spell
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Cast | Void | ObjectReference akSource, ObjectRefer... | No | `Function Cast(ObjectReference akSource, ObjectReference a...` |
| IsHostile | Bool | () | No | `Bool Function IsHostile() Native` |
| RequestReconMarkOnServer | Void | () | No | `Function RequestReconMarkOnServer() Native` |

### Terminal
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| ShowOnPipboy | Void | () | No | `Function ShowOnPipboy() Native` |

### Utility
*extends ScriptObject*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| CallGlobalFunction | Var | String asScriptName, String asFuncNam... | Yes | `Var Function CallGlobalFunction(String asScriptName, Stri...` |
| CallGlobalFunctionNoWait | Void | String asScriptName, String asFuncNam... | Yes | `Function CallGlobalFunctionNoWait(String asScriptName, St...` |
| CaptureFrameRate | String | Int numFrames | Yes | `String Function CaptureFrameRate(Int numFrames) Global Na...` |
| EndFrameRateCapture | Void | () | Yes | `Function EndFrameRateCapture() Global Native` |
| EnterTestData | Void | String astestType, String astestMatte... | Yes | `Function EnterTestData(String astestType, String astestMa...` |
| GameTimeToString | String | Float afGameTime | Yes | `String Function GameTimeToString(Float afGameTime) Global...` |
| GetAverageFrameRate | Float | () | Yes | `Float Function GetAverageFrameRate() Global Native` |
| GetBudgetCount | Int | () | Yes | `Int Function GetBudgetCount() Global Native` |
| GetBudgetLimit | String | Int aiBudgetNumber | Yes | `String Function GetBudgetLimit(Int aiBudgetNumber) Global...` |
| GetBudgetName | String | Int aiBudgetNumber | Yes | `String Function GetBudgetName(Int aiBudgetNumber) Global ...` |
| GetCurrentBudget | String | Int aiBudgetNumber | Yes | `String Function GetCurrentBudget(Int aiBudgetNumber) Glob...` |
| GetCurrentGameTime | Float | () | Yes | `Float Function GetCurrentGameTime() Global Native` |
| GetCurrentMemory | String | () | Yes | `String Function GetCurrentMemory() Global Native` |
| GetCurrentRealTime | Float | () | Yes | `Float Function GetCurrentRealTime() Global Native` |
| GetCurrentStackID | Int | () | Yes | `Int Function GetCurrentStackID() Global Native` |
| GetMaxFrameRate | Float | () | Yes | `Float Function GetMaxFrameRate() Global Native` |
| GetMinFrameRate | Float | () | Yes | `Float Function GetMinFrameRate() Global Native` |
| IntToHex | String | Int IntID | Yes | `String Function IntToHex(Int IntID) Global Native` |
| IsGameMenuPaused | Bool | () | Yes | `Bool Function IsGameMenuPaused() Global Native` |
| Now | Float | () | Yes | `Float Function Now() Global Native` |
| NowDay | Int | () | Yes | `Int Function NowDay() Global Native` |
| NowDayOfWeek | Int | () | Yes | `Int Function NowDayOfWeek() Global Native` |
| NowDayOfYear | Int | () | Yes | `Int Function NowDayOfYear() Global Native` |
| NowHour | Int | () | Yes | `Int Function NowHour() Global Native` |
| NowMinute | Int | () | Yes | `Int Function NowMinute() Global Native` |
| NowMonth | Int | () | Yes | `Int Function NowMonth() Global Native` |
| NowSecond | Int | () | Yes | `Int Function NowSecond() Global Native` |
| NowYear | Int | () | Yes | `Int Function NowYear() Global Native` |
| OverBudget | Bool | Int aiBudgetNumber | Yes | `Bool Function OverBudget(Int aiBudgetNumber) Global Native` |
| PostStartUpTimes | Void | () | Yes | `Function PostStartUpTimes() Global Native` |
| RandomFloat | Float | Float afMin, Float afMax | Yes | `Float Function RandomFloat(Float afMin, Float afMax) Glob...` |
| RandomFloatsFromSeed | Float[] | Int aiSeed, Int aiCount, Float afMin,... | Yes | `Float[] Function RandomFloatsFromSeed(Int aiSeed, Int aiC...` |
| RandomInt | Int | Int aiMin, Int aiMax | Yes | `Int Function RandomInt(Int aiMin, Int aiMax) Global Native` |
| RandomIntsFromSeed | Int[] | Int aiSeed, Int aiCount, Int aiMin, I... | Yes | `Int[] Function RandomIntsFromSeed(Int aiSeed, Int aiCount...` |
| SetINIBool | Void | String ini, Bool value | Yes | `Function SetINIBool(String ini, Bool value) Global Native` |
| SetINIFloat | Void | String ini, Float value | Yes | `Function SetINIFloat(String ini, Float value) Global Native` |
| SetINIInt | Void | String ini, Int value | Yes | `Function SetINIInt(String ini, Int value) Global Native` |
| SetINIString | Void | String ini, String value | Yes | `Function SetINIString(String ini, String value) Global Na...` |
| SplitStringChars | Int[] | String aString | Yes | `Int[] Function SplitStringChars(String aString) Global Na...` |
| StartFrameRateCapture | Void | () | Yes | `Function StartFrameRateCapture() Global Native` |
| Wait | Void | Float afSeconds | Yes | `Function Wait(Float afSeconds) Global Native` |
| WaitGameTime | Void | Float afHours | Yes | `Function WaitGameTime(Float afHours) Global Native` |
| WaitMenuPause | Void | Float afSeconds | Yes | `Function WaitMenuPause(Float afSeconds) Global Native` |

### VisualEffect
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Play | Void | ObjectReference akObject, Float afTim... | No | `Function Play(ObjectReference akObject, Float afTime, Obj...` |
| SetAltitudeFollowsStatics | Void | ObjectReference akObject, Float afRay... | No | `Function SetAltitudeFollowsStatics(ObjectReference akObje...` |
| SetStormLevelFadeRange | Void | ObjectReference akObject, Float storm... | No | `Function SetStormLevelFadeRange(ObjectReference akObject,...` |
| Stop | Void | ObjectReference akObject | No | `Function Stop(ObjectReference akObject) Native` |
| UseOcclusionMap | Void | ObjectReference akObject | No | `Function UseOcclusionMap(ObjectReference akObject) Native` |

### WaveEncounterType
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| GetSpawnGroupCurveTable | curvetable | () | No | `curvetable Function GetSpawnGroupCurveTable() Native` |

### Weapon
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| Fire | Void | ObjectReference akSource, Ammo akAmmo... | No | `Function Fire(ObjectReference akSource, Ammo akAmmo, Bool...` |
| GetAmmo | Ammo | () | No | `Ammo Function GetAmmo() Native` |
| IsMelee | Bool | () | No | `Bool Function IsMelee() Native` |
| IsRanged | Bool | () | No | `Bool Function IsRanged() Native` |

### Weather
*extends Form*

#### Unmapped Functions (Potential New Hooks)

| Function | Return | Parameters | Global | Declaration |
|----------|--------|------------|--------|-------------|
| EnableAmbientParticles | Void | Bool abEnable | Yes | `Function EnableAmbientParticles(Bool abEnable) Global Native` |
| FindWeather | Weather | Keyword aKeyword | Yes | `Weather Function FindWeather(Keyword aKeyword) Global Native` |
| ForceActive | Void | region aOnRegion, Bool abOverride | No | `Function ForceActive(region aOnRegion, Bool abOverride) N...` |
| GetClassification | Keyword[] | () | No | `Keyword[] Function GetClassification() Native` |
| GetCurrentWeather | Weather | region aInRegion | Yes | `Weather Function GetCurrentWeather(region aInRegion) Glob...` |
| GetCurrentWeatherTransition | Float | region aInRegion | Yes | `Float Function GetCurrentWeatherTransition(region aInRegi...` |
| GetOutgoingWeather | Weather | region aInRegion | Yes | `Weather Function GetOutgoingWeather(region aInRegion) Glo...` |
| GetSkyMode | Int | () | Yes | `Int Function GetSkyMode() Global Native` |
| ReleaseOverride | Void | region aOnRegion | Yes | `Function ReleaseOverride(region aOnRegion) Global Native` |
| SetActive | Void | region aOnRegion, Bool abOverride, Bo... | No | `Function SetActive(region aOnRegion, Bool abOverride, Boo...` |

## SFE Extension Functions (Not in Vanilla Papyrus)

These functions are added by SFE and do NOT exist as vanilla Native declarations:

### Actor

- **GetFurnitureReference** - impl: `papyrusActor::GetFurnitureReference` (PapyrusActor.cpp)
- **GetWornItem** - impl: `papyrusActor::GetWornItem` (PapyrusActor.cpp)
- **QueueUpdate** - impl: `papyrusActor::QueueUpdate` (PapyrusActor.cpp)

### ActorBase

- **GetBodyWeight** - impl: `papyrusActorBase::GetBodyWeight` (PapyrusActorBase.cpp)
- **GetOutfit** - impl: `papyrusActorBase::GetOutfit` (PapyrusActorBase.cpp)
- **GetTemplate** - impl: `papyrusActorBase::GetTemplate` (PapyrusActorBase.cpp)
- **HasHeadPartOverlays** - impl: `papyrusActorBase::HasHeadPartOverlays` (PapyrusActorBase.cpp)
- **SetBodyWeight** - impl: `papyrusActorBase::SetBodyWeight` (PapyrusActorBase.cpp)

### Cell

- **GetWaterType** - impl: `papyrusCell::GetWaterType` (PapyrusCell.cpp)

### Component

- **GetScrapItem** - impl: `papyrusComponent::GetScrapItem` (PapyrusComponent.cpp)
- **GetScrapScalar** - impl: `papyrusComponent::GetScrapScalar` (PapyrusComponent.cpp)
- **SetScrapItem** - impl: `papyrusComponent::SetScrapItem` (PapyrusComponent.cpp)
- **SetScrapScalar** - impl: `papyrusComponent::SetScrapScalar` (PapyrusComponent.cpp)

### ConstructibleObject

- **GetCreatedCount** - impl: `papyrusConstructibleObject::GetCreatedCount` (PapyrusConstructibleObject.cpp)
- **GetPriority** - impl: `papyrusConstructibleObject::GetPriority` (PapyrusConstructibleObject.cpp)
- **GetWorkbenchKeyword** - impl: `papyrusConstructibleObject::GetWorkbenchKeyword` (PapyrusConstructibleObject.cpp)
- **SetCreatedCount** - impl: `papyrusConstructibleObject::SetCreatedCount` (PapyrusConstructibleObject.cpp)
- **SetCreatedObject** - impl: `papyrusConstructibleObject::SetCreatedObject` (PapyrusConstructibleObject.cpp)
- **SetPriority** - impl: `papyrusConstructibleObject::SetPriority` (PapyrusConstructibleObject.cpp)
- **SetWorkbenchKeyword** - impl: `papyrusConstructibleObject::SetWorkbenchKeyword` (PapyrusConstructibleObject.cpp)

### DefaultObject

- **Get** - impl: `papyrusDefaultObject::Get` (PapyrusDefaultObject.cpp)
- **GetDefaultObject** - impl: `papyrusDefaultObject::GetDefaultObject` (PapyrusDefaultObject.cpp)
- **Set** - impl: `papyrusDefaultObject::Set` (PapyrusDefaultObject.cpp)

### EncounterZone

- **GetLocation** - impl: `papyrusEncounterZone::GetLocation` (PapyrusEncounterZone.cpp)
- **GetMaxLevel** - impl: `papyrusEncounterZone::GetMaxLevel` (PapyrusEncounterZone.cpp)
- **GetMinLevel** - impl: `papyrusEncounterZone::GetMinLevel` (PapyrusEncounterZone.cpp)
- **GetRank** - impl: `papyrusEncounterZone::GetRank` (PapyrusEncounterZone.cpp)
- **IsNeverResetable** - impl: `papyrusEncounterZone::IsNeverResetable` (PapyrusEncounterZone.cpp)
- **IsWorkshop** - impl: `papyrusEncounterZone::IsWorkshop` (PapyrusEncounterZone.cpp)
- **SetLocation** - impl: `papyrusEncounterZone::SetLocation` (PapyrusEncounterZone.cpp)
- **SetMaxLevel** - impl: `papyrusEncounterZone::SetMaxLevel` (PapyrusEncounterZone.cpp)
- **SetMinLevel** - impl: `papyrusEncounterZone::SetMinLevel` (PapyrusEncounterZone.cpp)
- **SetNeverResetable** - impl: `papyrusEncounterZone::SetNeverResetable` (PapyrusEncounterZone.cpp)
- **SetRank** - impl: `papyrusEncounterZone::SetRank` (PapyrusEncounterZone.cpp)
- **SetWorkshop** - impl: `papyrusEncounterZone::SetWorkshop` (PapyrusEncounterZone.cpp)

### F4SE

- **GetPluginVersion** - impl: `papyrusF4SE::GetPluginVersion` (PapyrusF4SE.cpp)
- **GetVersion** - impl: `papyrusF4SE::GetVersion` (PapyrusF4SE.cpp)
- **GetVersionBeta** - impl: `papyrusF4SE::GetVersionBeta` (PapyrusF4SE.cpp)
- **GetVersionMinor** - impl: `papyrusF4SE::GetVersionMinor` (PapyrusF4SE.cpp)
- **GetVersionRelease** - impl: `papyrusF4SE::GetVersionRelease` (PapyrusF4SE.cpp)
- **TestInventoryFunc** - impl: `papyrusF4SE::TestInventoryFunc` (PapyrusF4SE.cpp)

### Form

- **AddSlotToMask** - impl: `papyrusForm::AddSlotToMask` (PapyrusForm.cpp)
- **GetDescription** - impl: `papyrusForm::GetDescription` (PapyrusForm.cpp)
- **GetEnchantment** - impl: `papyrusForm::GetEnchantment` (PapyrusForm.cpp)
- **GetEnchantmentValue** - impl: `papyrusForm::GetEnchantmentValue` (PapyrusForm.cpp)
- **GetEquipType** - impl: `papyrusForm::GetEquipType` (PapyrusForm.cpp)
- **GetIconPath** - impl: `papyrusForm::GetIconPath` (PapyrusForm.cpp)
- **GetMaskForSlot** - impl: `papyrusForm::GetMaskForSlot` (PapyrusForm.cpp)
- **GetMessageIconPath** - impl: `papyrusForm::GetMessageIconPath` (PapyrusForm.cpp)
- **GetName** - impl: `papyrusForm::GetName` (PapyrusForm.cpp)
- **GetRaceForm** - impl: `papyrusForm::GetRaceForm` (PapyrusForm.cpp)
- **GetSlotMask** - impl: `papyrusForm::GetSlotMask` (PapyrusForm.cpp)
- **GetWeight** - impl: `papyrusForm::GetWeight` (PapyrusForm.cpp)
- **GetWorldModelPath** - impl: `papyrusForm::GetWorldModelPath` (PapyrusForm.cpp)
- **HasWorldModel** - impl: `papyrusForm::HasWorldModel` (PapyrusForm.cpp)
- **RemoveSlotFromMask** - impl: `papyrusForm::RemoveSlotFromMask` (PapyrusForm.cpp)
- **SetEnchantment** - impl: `papyrusForm::SetEnchantment` (PapyrusForm.cpp)
- **SetEnchantmentValue** - impl: `papyrusForm::SetEnchantmentValue` (PapyrusForm.cpp)
- **SetEquipType** - impl: `papyrusForm::SetEquipType` (PapyrusForm.cpp)
- **SetGoldValue** - impl: `papyrusForm::SetGoldValue` (PapyrusForm.cpp)
- **SetIconPath** - impl: `papyrusForm::SetIconPath` (PapyrusForm.cpp)
- **SetMessageIconPath** - impl: `papyrusForm::SetMessageIconPath` (PapyrusForm.cpp)
- **SetName** - impl: `papyrusForm::SetName` (PapyrusForm.cpp)
- **SetRaceForm** - impl: `papyrusForm::SetRaceForm` (PapyrusForm.cpp)
- **SetSlotMask** - impl: `papyrusForm::SetSlotMask` (PapyrusForm.cpp)
- **SetWeight** - impl: `papyrusForm::SetWeight` (PapyrusForm.cpp)
- **SetWorldModelPath** - impl: `papyrusForm::SetWorldModelPath` (PapyrusForm.cpp)

### Game

- **GetCurrentConsoleRef** - impl: `papyrusGame::GetCurrentConsoleRef` (PapyrusGame.cpp)
- **SetGameSettingBool** - impl: `papyrusGame::SetGameSettingBool` (PapyrusGame.cpp)
- **SetGameSettingFloat** - impl: `papyrusGame::SetGameSettingFloat` (PapyrusGame.cpp)
- **SetGameSettingInt** - impl: `papyrusGame::SetGameSettingInt` (PapyrusGame.cpp)
- **SetGameSettingString** - impl: `papyrusGame::SetGameSettingString` (PapyrusGame.cpp)

### HeadPart

- **GetType** - impl: `papyrusHeadPart::GetType` (PapyrusHeadPart.cpp)
- **GetValidRaces** - impl: `papyrusHeadPart::GetValidRaces` (PapyrusHeadPart.cpp)
- **HasExtraPart** - impl: `papyrusHeadPart::HasExtraPart` (PapyrusHeadPart.cpp)
- **IsExtraPart** - impl: `papyrusHeadPart::IsExtraPart` (PapyrusHeadPart.cpp)
- **SetValidRaces** - impl: `papyrusHeadPart::SetValidRaces` (PapyrusHeadPart.cpp)

### Input

- **GetMappedControl** - impl: `papyrusInput::GetMappedControl` (PapyrusInput.cpp)
- **GetMappedKey** - impl: `papyrusInput::GetMappedKey` (PapyrusInput.cpp)

### InstanceData

- **GetAccuracyBonus** - impl: `papyrusInstanceData::GetAccuracyBonus` (PapyrusInstanceData.cpp)
- **GetActionPointCost** - impl: `papyrusInstanceData::GetActionPointCost` (PapyrusInstanceData.cpp)
- **GetAddAmmoList** - impl: `papyrusInstanceData::GetAddAmmoList` (PapyrusInstanceData.cpp)
- **GetAmmo** - impl: `papyrusInstanceData::GetAmmo` (PapyrusInstanceData.cpp)
- **GetAmmoCapacity** - impl: `papyrusInstanceData::GetAmmoCapacity` (PapyrusInstanceData.cpp)
- **GetArmorHealth** - impl: `papyrusInstanceData::GetArmorHealth` (PapyrusInstanceData.cpp)
- **GetArmorRating** - impl: `papyrusInstanceData::GetArmorRating` (PapyrusInstanceData.cpp)
- **GetAttackDamage** - impl: `papyrusInstanceData::GetAttackDamage` (PapyrusInstanceData.cpp)
- **GetAttackDelay** - impl: `papyrusInstanceData::GetAttackDelay` (PapyrusInstanceData.cpp)
- **GetCritChargeBonus** - impl: `papyrusInstanceData::GetCritChargeBonus` (PapyrusInstanceData.cpp)
- **GetCritMultiplier** - impl: `papyrusInstanceData::GetCritMultiplier` (PapyrusInstanceData.cpp)
- **GetFlag** - impl: `papyrusInstanceData::GetFlag` (PapyrusInstanceData.cpp)
- **GetGoldValue** - impl: `papyrusInstanceData::GetGoldValue` (PapyrusInstanceData.cpp)
- **GetMaxRange** - impl: `papyrusInstanceData::GetMaxRange` (PapyrusInstanceData.cpp)
- **GetMinRange** - impl: `papyrusInstanceData::GetMinRange` (PapyrusInstanceData.cpp)
- **GetNumProjectiles** - impl: `papyrusInstanceData::GetNumProjectiles` (PapyrusInstanceData.cpp)
- **GetOutOfRangeMultiplier** - impl: `papyrusInstanceData::GetOutOfRangeMultiplier` (PapyrusInstanceData.cpp)
- **GetProjectileOverride** - impl: `papyrusInstanceData::GetProjectileOverride` (PapyrusInstanceData.cpp)
- **GetReach** - impl: `papyrusInstanceData::GetReach` (PapyrusInstanceData.cpp)
- **GetReloadSpeed** - impl: `papyrusInstanceData::GetReloadSpeed` (PapyrusInstanceData.cpp)
- **GetResist** - impl: `papyrusInstanceData::GetResist` (PapyrusInstanceData.cpp)
- **GetSightedTransition** - impl: `papyrusInstanceData::GetSightedTransition` (PapyrusInstanceData.cpp)
- **GetSkill** - impl: `papyrusInstanceData::GetSkill` (PapyrusInstanceData.cpp)
- **GetSpeed** - impl: `papyrusInstanceData::GetSpeed` (PapyrusInstanceData.cpp)
- **GetStagger** - impl: `papyrusInstanceData::GetStagger` (PapyrusInstanceData.cpp)
- **GetWeight** - impl: `papyrusInstanceData::GetWeight` (PapyrusInstanceData.cpp)
- **SetAccuracyBonus** - impl: `papyrusInstanceData::SetAccuracyBonus` (PapyrusInstanceData.cpp)
- **SetActionPointCost** - impl: `papyrusInstanceData::SetActionPointCost` (PapyrusInstanceData.cpp)
- **SetAddAmmoList** - impl: `papyrusInstanceData::SetAddAmmoList` (PapyrusInstanceData.cpp)
- **SetAmmo** - impl: `papyrusInstanceData::SetAmmo` (PapyrusInstanceData.cpp)
- **SetAmmoCapacity** - impl: `papyrusInstanceData::SetAmmoCapacity` (PapyrusInstanceData.cpp)
- **SetArmorHealth** - impl: `papyrusInstanceData::SetArmorHealth` (PapyrusInstanceData.cpp)
- **SetArmorRating** - impl: `papyrusInstanceData::SetArmorRating` (PapyrusInstanceData.cpp)
- **SetAttackDamage** - impl: `papyrusInstanceData::SetAttackDamage` (PapyrusInstanceData.cpp)
- **SetAttackDelay** - impl: `papyrusInstanceData::SetAttackDelay` (PapyrusInstanceData.cpp)
- **SetCritChargeBonus** - impl: `papyrusInstanceData::SetCritChargeBonus` (PapyrusInstanceData.cpp)
- **SetCritMultiplier** - impl: `papyrusInstanceData::SetCritMultiplier` (PapyrusInstanceData.cpp)
- **SetFlag** - impl: `papyrusInstanceData::SetFlag` (PapyrusInstanceData.cpp)
- **SetGoldValue** - impl: `papyrusInstanceData::SetGoldValue` (PapyrusInstanceData.cpp)
- **SetMaxRange** - impl: `papyrusInstanceData::SetMaxRange` (PapyrusInstanceData.cpp)
- **SetMinRange** - impl: `papyrusInstanceData::SetMinRange` (PapyrusInstanceData.cpp)
- **SetNumProjectiles** - impl: `papyrusInstanceData::SetNumProjectiles` (PapyrusInstanceData.cpp)
- **SetOutOfRangeMultiplier** - impl: `papyrusInstanceData::SetOutOfRangeMultiplier` (PapyrusInstanceData.cpp)
- **SetProjectileOverride** - impl: `papyrusInstanceData::SetProjectileOverride` (PapyrusInstanceData.cpp)
- **SetReach** - impl: `papyrusInstanceData::SetReach` (PapyrusInstanceData.cpp)
- **SetReloadSpeed** - impl: `papyrusInstanceData::SetReloadSpeed` (PapyrusInstanceData.cpp)
- **SetResist** - impl: `papyrusInstanceData::SetResist` (PapyrusInstanceData.cpp)
- **SetSightedTransition** - impl: `papyrusInstanceData::SetSightedTransition` (PapyrusInstanceData.cpp)
- **SetSkill** - impl: `papyrusInstanceData::SetSkill` (PapyrusInstanceData.cpp)
- **SetSpeed** - impl: `papyrusInstanceData::SetSpeed` (PapyrusInstanceData.cpp)
- **SetStagger** - impl: `papyrusInstanceData::SetStagger` (PapyrusInstanceData.cpp)
- **SetWeight** - impl: `papyrusInstanceData::SetWeight` (PapyrusInstanceData.cpp)

### Location

- **GetEncounterZone** - impl: `papyrusLocation::GetEncounterZone` (PapyrusLocation.cpp)
- **GetParent** - impl: `papyrusLocation::GetParent` (PapyrusLocation.cpp)
- **SetEncounterZone** - impl: `papyrusLocation::SetEncounterZone` (PapyrusLocation.cpp)
- **SetParent** - impl: `papyrusLocation::SetParent` (PapyrusLocation.cpp)

### Math

- **Exp** - impl: `papyrusMath::Exp` (PapyrusMath.cpp)
- **LeftShift** - impl: `papyrusMath::LeftShift` (PapyrusMath.cpp)
- **Log** - impl: `papyrusMath::Log` (PapyrusMath.cpp)
- **LogicalAnd** - impl: `papyrusMath::LogicalAnd` (PapyrusMath.cpp)
- **LogicalNot** - impl: `papyrusMath::LogicalNot` (PapyrusMath.cpp)
- **LogicalOr** - impl: `papyrusMath::LogicalOr` (PapyrusMath.cpp)
- **LogicalXor** - impl: `papyrusMath::LogicalXor` (PapyrusMath.cpp)
- **RightShift** - impl: `papyrusMath::RightShift` (PapyrusMath.cpp)

### ObjectMod

- **GetLooseMod** - impl: `papyrusObjectMod::GetLooseMod` (PapyrusObjectMod.cpp)
- **GetMaxRank** - impl: `papyrusObjectMod::GetMaxRank` (PapyrusObjectMod.cpp)
- **GetPriority** - impl: `papyrusObjectMod::GetPriority` (PapyrusObjectMod.cpp)
- **SetMaxRank** - impl: `papyrusObjectMod::SetMaxRank` (PapyrusObjectMod.cpp)
- **SetPriority** - impl: `papyrusObjectMod::SetPriority` (PapyrusObjectMod.cpp)

### ObjectReference

- **GetDisplayName** - impl: `papyrusObjectReference::GetDisplayName` (PapyrusObjectReference.cpp)
- **GetInventoryWeight** - impl: `papyrusObjectReference::GetInventoryWeight` (PapyrusObjectReference.cpp)
- **GetMaterialSwap** - impl: `papyrusObjectReference::GetMaterialSwap` (PapyrusObjectReference.cpp)
- **SetMaterialSwap** - impl: `papyrusObjectReference::SetMaterialSwap` (PapyrusObjectReference.cpp)

### Perk

- **GetLevel** - impl: `papyrusPerk::GetLevel` (PapyrusPerk.cpp)
- **GetNextPerk** - impl: `papyrusPerk::GetNextPerk` (PapyrusPerk.cpp)
- **GetNumRanks** - impl: `papyrusPerk::GetNumRanks` (PapyrusPerk.cpp)
- **GetSWFPath** - impl: `papyrusPerk::GetSWFPath` (PapyrusPerk.cpp)
- **IsEligible** - impl: `papyrusPerk::IsEligible` (PapyrusPerk.cpp)
- **IsHidden** - impl: `papyrusPerk::IsHidden` (PapyrusPerk.cpp)
- **IsPlayable** - impl: `papyrusPerk::IsPlayable` (PapyrusPerk.cpp)

### ScriptObject

- **RegisterForCameraState** - impl: `papyrusScriptObject::RegisterForCameraState` (PapyrusScriptObject.cpp)
- **RegisterForControl** - impl: `papyrusScriptObject::RegisterForControl` (PapyrusScriptObject.cpp)
- **RegisterForExternalEvent** - impl: `papyrusScriptObject::RegisterForExternalEvent` (PapyrusScriptObject.cpp)
- **RegisterForFurnitureEvent** - impl: `papyrusScriptObject::RegisterForFurnitureEvent` (PapyrusScriptObject.cpp)
- **RegisterForKey** - impl: `papyrusScriptObject::RegisterForKey` (PapyrusScriptObject.cpp)
- **UnregisterForCameraState** - impl: `papyrusScriptObject::UnregisterForCameraState` (PapyrusScriptObject.cpp)
- **UnregisterForControl** - impl: `papyrusScriptObject::UnregisterForControl` (PapyrusScriptObject.cpp)
- **UnregisterForExternalEvent** - impl: `papyrusScriptObject::UnregisterForExternalEvent` (PapyrusScriptObject.cpp)
- **UnregisterForFurnitureEvent** - impl: `papyrusScriptObject::UnregisterForFurnitureEvent` (PapyrusScriptObject.cpp)
- **UnregisterForKey** - impl: `papyrusScriptObject::UnregisterForKey` (PapyrusScriptObject.cpp)

### UI

- **CloseMenu** - impl: `papyrusUI::CloseMenu` (PapyrusUI.cpp)
- **IsMenuOpen** - impl: `papyrusUI::IsMenuOpen` (PapyrusUI.cpp)
- **IsMenuRegistered** - impl: `papyrusUI::IsMenuRegistered` (PapyrusUI.cpp)
- **OpenMenu** - impl: `papyrusUI::OpenMenu` (PapyrusUI.cpp)
- **RegisterCustomMenu** - impl: `papyrusUI::RegisterCustomMenu` (PapyrusUI.cpp)

### WaterType

- **GetConsumeSpell** - impl: `papyrusWaterType::GetConsumeSpell` (PapyrusWaterType.cpp)
- **GetContactSpell** - impl: `papyrusWaterType::GetContactSpell` (PapyrusWaterType.cpp)
- **SetConsumeSpell** - impl: `papyrusWaterType::SetConsumeSpell` (PapyrusWaterType.cpp)
- **SetContactSpell** - impl: `papyrusWaterType::SetContactSpell` (PapyrusWaterType.cpp)

### Weapon

- **GetEmbeddedMod** - impl: `papyrusWeapon::GetEmbeddedMod` (PapyrusWeapon.cpp)
- **SetEmbeddedMod** - impl: `papyrusWeapon::SetEmbeddedMod` (PapyrusWeapon.cpp)

## SFE Address Table (All Known Addresses)

Total SFE address definitions: 277

| Name | Address | Type | Class | Source |
|------|---------|------|-------|--------|
| kHook_IMemoryStoreCtor_Offset | `0x00000000` | RelocAddr | - | Hooks_Memory.cpp:11 |
| kHook_IMemoryStoreCtor_VTable | `0x00000000` | RelocAddr | - | Hooks_Memory.cpp:12 |
| kHook_IMemoryStoreDtor_Offset | `0x00000000` | RelocAddr | - | Hooks_Memory.cpp:14 |
| CreateHandleByREFR | `0x0000A8A0` | RelocAddr | - | GameReferences.cpp:10 |
| LookupREFRByHandle | `0x0000AB60` | RelocAddr | - | GameReferences.cpp:7 |
| GetSetting | `0x0001E290` | DEFINE_MEMBER_FN | SettingCollectionMap | GameSettings.h:75 |
| ApplyMaterial | `0x00054170` | DEFINE_MEMBER_FN | BSLightingShaderProperty | NiProperties.h:178 |
| GetReferenceName | `0x000C0A00` | DEFINE_MEMBER_FN | ExtraTextDisplayData | GameExtraData.h:358 |
| Impl_Process | `0x00137E50` | DEFINE_MEMBER_FN | BSModelDB | BSModelDB.h:46 |
| SetSex | `0x00149720` | DEFINE_MEMBER_FN | TESActorBaseData | GameFormComponents.h:223 |
| GetLevel | `0x001497F0` | DEFINE_MEMBER_FN | TESActorBaseData | GameFormComponents.h:224 |
| Get | `0x0014FAF0` | DEFINE_MEMBER_FN | TESDescription | GameFormComponents.h:437 |
| LookupFormByID | `0x00152C90` | RelocAddr | - | GameForms.cpp:4 |
| LinkPower3_Internal | `0x001F67E0` | RelocAddr | - | GameWorkshop.cpp:6 |
| LinkPower_Internal | `0x001F6D70` | RelocAddr | - | GameWorkshop.cpp:3 |
| ctor | `0x001F8780` | DEFINE_MEMBER_FN | LocationData | GameData.h:291 |
| GetObjectAtConnectPoint | `0x001FF2B0` | RelocAddr | - | GameWorkshop.cpp:5 |
| FinalizeWireLink | `0x00200AA0` | RelocAddr | - | GameWorkshop.cpp:9 |
| SetWireEndpoints_Internal | `0x00200DA0` | RelocAddr | - | GameWorkshop.cpp:8 |
| LinkPower2_Internal | `0x00201A60` | RelocAddr | - | GameWorkshop.cpp:4 |
| LinkPower4_Internal | `0x00204560` | RelocAddr | - | GameWorkshop.cpp:7 |
| ScrapReference | `0x002083D0` | RelocAddr | - | GameWorkshop.cpp:10 |
| CopyCharacterTints | `0x002A4620` | RelocAddr | - | GameCustomization.cpp:19 |
| FillTintTemplates | `0x002A47C0` | RelocAddr | - | GameCustomization.cpp:22 |
| CreateCharacterTintEntry | `0x002A5630` | RelocAddr | - | GameCustomization.cpp:18 |
| ClearCharacterTints | `0x002AA8A0` | RelocAddr | - | GameCustomization.cpp:20 |
| dtor | `0x003900D0` | DEFINE_MEMBER_FN | BSShaderData | NiMaterials.h:519 |
| GetHavokWorld | `0x003B4880` | DEFINE_MEMBER_FN | TESObjectCELL | GameForms.h:1528 |
| GetInventoryWeight | `0x00400350` | DEFINE_MEMBER_FN | TESObjectREFR | GameReferences.h:246 |
| UpdateEquipment | `0x00408150` | DEFINE_MEMBER_FN | Actor | GameReferences.h:467 |
| GetReferenceName | `0x0040B640` | DEFINE_MEMBER_FN | TESObjectREFR | GameReferences.h:244 |
| GetWorldspace | `0x0040F170` | DEFINE_MEMBER_FN | TESObjectREFR | GameReferences.h:245 |
| GetLinkedRef_Native | `0x00480EE0` | RelocAddr | - | GameReferences.cpp:17 |
| SetLinkedRef_Native | `0x00480F00` | RelocAddr | - | GameReferences.cpp:19 |
| Copy | `0x004C3590` | DEFINE_MEMBER_FN | BSShaderTextureSet | NiTextures.h:82 |
| CreateFileStream | `0x00535940` | RelocAddr | - | GameStreams.cpp:3 |
| GetSex | `0x005A2440` | DEFINE_MEMBER_FN | TESNPC | GameObjects.h:234 |
| ctor | `0x005AE6E0` | DEFINE_MEMBER_FN | TESNPC | GameObjects.h:230 |
| ChangeHeadPartRemovePart | `0x005B5440` | DEFINE_MEMBER_FN | TESNPC | GameObjects.h:235 |
| GetSkinColorFromTint | `0x005B57C0` | DEFINE_MEMBER_FN | TESNPC | GameObjects.h:237 |
| ChangeHeadPart | `0x005B9A10` | DEFINE_MEMBER_FN | TESNPC | GameObjects.h:236 |
| HasOverlays | `0x005BFFF0` | DEFINE_MEMBER_FN | TESNPC | GameObjects.h:231 |
| GetOverlayHeadParts | `0x005C0110` | DEFINE_MEMBER_FN | TESNPC | GameObjects.h:232 |
| GetNumOverlayHeadParts | `0x005C01C0` | DEFINE_MEMBER_FN | TESNPC | GameObjects.h:233 |
| ApplyDynamicData | `0x00678D20` | DEFINE_MEMBER_FN | BSFaceGenManager | GameCustomization.h:438 |
| ctor | `0x00684320` | DEFINE_MEMBER_FN | BSFaceGenBaseMorphExtraData | NiExtraData.h:85 |
| CreateMergeTintTextures | `0x00689880` | RelocAddr | - | GameCustomization.cpp:24 |
| MergeTintTextures | `0x00689A90` | RelocAddr | - | GameCustomization.cpp:23 |
| ConvertHalfToFloat | `0x006944A0` | RelocAddr | - | BSGeometry.cpp:3 |
| ctor | `0x0072A650` | DEFINE_MEMBER_FN | Condition | GameFormComponents.h:1389 |
| EvaluationConditions | `0x0072AE60` | RelocAddr | - | GameFormComponents.cpp:4 |
| Evaluate | `0x0072C410` | DEFINE_MEMBER_FN | Condition | GameFormComponents.h:1394 |
| SetCameraState | `0x0082E810` | DEFINE_MEMBER_FN | TESCamera | GameCamera.h:39 |
| SetCameraState | `0x0082E810` | RelocAddr | - | Hooks_Camera.cpp:16 |
| GameDataReady_Original | `0x0082F930` | RelocAddr | - | Hooks_GameData.cpp:17 |
| HasHUDContext | `0x00A4F270` | RelocAddr | - | GameMenus.cpp:6 |
| WorldToScreen_Internal | `0x00AE2720` | RelocAddr | - | NiObjects.cpp:4 |
| CreateBaseShaderTarget | `0x00B06C80` | RelocAddr | - | ScaleformValue.cpp:13 |
| LoadPreset | `0x00CACC20` | DEFINE_MEMBER_FN | CharacterCreation | GameCustomization.h:416 |
| SaveGame | `0x00CDE3D0` | RelocAddr | BGSSaveLoadGame | Hooks_SaveLoad.cpp:15 |
| LoadGame | `0x00CDE8D0` | RelocAddr | BGSSaveLoadGame | Hooks_SaveLoad.cpp:19 |
| DeleteSaveGame | `0x00CECE30` | RelocAddr | BGSSaveLoadGame | Hooks_SaveLoad.cpp:23 |
| InitGameDataThread_Run_Original | `0x00D53460` | RelocAddr | - | Hooks_GameData.cpp:11 |
| MessageQueueProcessTask | `0x00D57E80` | RelocAddr | - | Hooks_Threads.cpp:17 |
| SetTextureSet | `0x00D5DE40` | DEFINE_MEMBER_FN | BSTCommonScrapHeapMessageQueue | GameMessages.h:49 |
| GetCarryWeight | `0x00D870D0` | DEFINE_MEMBER_FN | TESObjectREFR | GameReferences.h:247 |
| QueueUpdate | `0x00D8A0D0` | DEFINE_MEMBER_FN | Actor | GameReferences.h:465 |
| IsHostileToActor | `0x00D90F60` | DEFINE_MEMBER_FN | Actor | GameReferences.h:466 |
| UpdateEquipment | `0x00E60740` | DEFINE_MEMBER_FN | Actor | GameReferences.h:432 |
| CreatePlayerControlHandlers | `0x00F44BA0` | RelocAddr | - | Hooks_Input.cpp:23 |
| VPrint | `0x01262DA0` | DEFINE_MEMBER_FN | ConsoleManager | GameAPI.h:22 |
| Print | `0x01262E30` | DEFINE_MEMBER_FN | ConsoleManager | GameAPI.h:23 |
| CreateMenuControlHandlers | `0x012A7FD0` | RelocAddr | - | Hooks_Input.cpp:19 |
| SendUIMessageEx | `0x012BA8F0` | DEFINE_MEMBER_FN | UIMessageManager | GameMenus.h:41 |
| PlayUISound | `0x012BE200` | RelocAddr | - | ScaleformValue.cpp:12 |
| GetRefFromHandle | `0x012C6470` | RelocAddr | - | PapyrusInterfaces.cpp:6 |
| HasDetectionLOS | `0x0135B560` | RelocAddr | - | GameReferences.cpp:15 |
| SendPapyrusEvent | `0x01374E90` | DEFINE_MEMBER_FN | GameVM | PapyrusVM.h:299 |
| RevertGlobalData | `0x013761D0` | RelocAddr | - | Hooks_Papyrus.cpp:55 |
| CallFunctionNoWait_Internal | `0x013D68B0` | RelocAddr | - | PapyrusEvents.cpp:7 |
| SendCustomEvent_Internal | `0x013D9340` | RelocAddr | - | PapyrusEvents.cpp:6 |
| MoveRefrToPosition | `0x013FE6C0` | RelocAddr | - | GameReferences.cpp:21 |
| PlaceAtMe_Native | `0x0140AFC0` | RelocAddr | - | GameObjects.cpp:5 |
| CallGlobalFunctionNoWait_Internal | `0x01451960` | RelocAddr | - | PapyrusEvents.cpp:8 |
| SaveRegistrationHandles | `0x014749B0` | RelocAddr | - | Hooks_Papyrus.cpp:47 |
| LoadRegistrationHandles | `0x01474A40` | RelocAddr | - | Hooks_Papyrus.cpp:51 |
| Allocate | `0x01B0EEB0` | DEFINE_MEMBER_FN | Heap | GameAPI.h:9 |
| Free | `0x01B0F1C0` | DEFINE_MEMBER_FN | Heap | GameAPI.h:10 |
| CalculateCRC32_32 | `0x01B10680` | RelocAddr | - | GameUtilities.cpp:4 |
| CalculateCRC32_64 | `0x01B10710` | RelocAddr | - | GameUtilities.cpp:3 |
| kHook_CustomControlMap_Offset | `0x01B2A0B0` | RelocAddr | - | Hooks_Gameplay.cpp:38 |
| ctor | `0x01B41C20` | DEFINE_MEMBER_FN | StringCache | GameTypes.h:162 |
| Set | `0x01B41D50` | DEFINE_MEMBER_FN | StringCache | GameTypes.h:166 |
| SetMenuName | `0x01B41DB0` | RelocAddr | BSScaleformManager | Hooks_Scaleform.cpp:332 |
| CreateEmptyString | `0x01B429A0` | RelocAddr | - | ScaleformTranslator.cpp:4 |
| ctor_w | `0x01B42A40` | DEFINE_MEMBER_FN | StringCache | GameTypes.h:164 |
| SetWideString | `0x01B42AF0` | RelocAddr | - | ScaleformTranslator.cpp:6 |
| Release | `0x01B42EB0` | DEFINE_MEMBER_FN | StringCache | GameTypes.h:169 |
| Set_w | `0x01B442A0` | DEFINE_MEMBER_FN | StringCache | GameTypes.h:167 |
| AddManaged_Internal | `0x01B57490` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:184 |
| ReleaseManaged_Internal | `0x01B57510` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:187 |
| Construct | `0x01B93620` | DEFINE_MEMBER_FN | BSResourceNiBinaryStream | GameStreams.h:54 |
| Destroy | `0x01B938E0` | DEFINE_MEMBER_FN | BSResourceNiBinaryStream | GameStreams.h:56 |
| IsValid | `0x01B93A00` | DEFINE_MEMBER_FN | BSResourceNiBinaryStream | GameStreams.h:57 |
| Seek | `0x01B93A10` | DEFINE_MEMBER_FN | BSResourceNiBinaryStream | GameStreams.h:58 |
| Unk_04 | `0x01B93A80` | DEFINE_MEMBER_FN | BSResourceNiBinaryStream | GameStreams.h:59 |
| ReadLine | `0x01B93B20` | DEFINE_MEMBER_FN | BSResourceNiBinaryStream | GameStreams.h:55 |
| Read | `0x01B93BE0` | DEFINE_MEMBER_FN | BSResourceNiBinaryStream | GameStreams.h:60 |
| Write | `0x01B93C70` | DEFINE_MEMBER_FN | BSResourceNiBinaryStream | GameStreams.h:61 |
| Internal_IsEqual | `0x01B94970` | DEFINE_MEMBER_FN | NiObject | NiObjects.h:88 |
| Internal_LoadBinary | `0x01B962E0` | DEFINE_MEMBER_FN | NiExtraData | NiExtraData.h:35 |
| Internal_SaveBinary | `0x01B96380` | DEFINE_MEMBER_FN | NiExtraData | NiExtraData.h:37 |
| Internal_AddExtraData | `0x01B977A0` | DEFINE_MEMBER_FN | NiObjectNET | NiObjects.h:111 |
| ctor | `0x01B98800` | DEFINE_MEMBER_FN | NiNode | NiNodes.h:28 |
| SetScenegraphChange | `0x01BA46A0` | DEFINE_MEMBER_FN | NiAVObject | NiObjects.h:201 |
| CreateTexture | `0x01BA5100` | RelocAddr | - | NiTextures.cpp:3 |
| ctor | `0x01BB8E70` | DEFINE_MEMBER_FN | NiStream | NiSerialization.h:41 |
| dtor | `0x01BB90A0` | DEFINE_MEMBER_FN | NiStream | NiSerialization.h:42 |
| AddObject | `0x01BB91D0` | DEFINE_MEMBER_FN | NiStream | NiSerialization.h:43 |
| GetAVObjectByName | `0x01C93860` | DEFINE_MEMBER_FN | NiAVObject | NiObjects.h:200 |
| LoadMaterialFile | `0x01C9D050` | RelocAddr | - | NiMaterials.cpp:6 |
| ctor | `0x01CE67A0` | DEFINE_MEMBER_FN | BSTextureArray | NiTextures.h:58 |
| CreateBSGeometryData | `0x01D0BC40` | DEFINE_MEMBER_FN | BSRenderManager | BSGraphics.h:19 |
| CreateDynamicTriShape | `0x01D28030` | DEFINE_MEMBER_FN | BSTriShape | BSGeometry.h:189 |
| GetRenderData | `0x01D327F0` | DEFINE_MEMBER_FN | BSRenderTargetManager | BSGraphics.h:62 |
| Unk_01 | `0x01D32840` | DEFINE_MEMBER_FN | BSRenderTargetManager | BSGraphics.h:64 |
| LockTextureType | `0x01D32890` | DEFINE_MEMBER_FN | BSRenderTargetManager | BSGraphics.h:59 |
| ReleaseTextureType | `0x01D32920` | DEFINE_MEMBER_FN | BSRenderTargetManager | BSGraphics.h:61 |
| HasMember | `0x01be5c30` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:156 |
| GetMember | `0x01be5c30` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:159 |
| SetMember | `0x01be5c30` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:162 |
| Invoke | `0x01be5c30` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:165 |
| AddManaged_Internal | `0x01be5c30` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:185 |
| ReleaseManaged_Internal | `0x01be5c30` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:188 |
| IsMenuOpen | `0x02042040` | DEFINE_MEMBER_FN | UI | GameMenus.h:442 |
| RegisterMenu | `0x02043BD0` | DEFINE_MEMBER_FN | UI | GameMenus.h:441 |
| SendUIMessage | `0x0204CA70` | DEFINE_MEMBER_FN | UIMessageManager | GameMenus.h:39 |
| AttachMovie | `0x02081510` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:168 |
| CreateEmptyMovieClip | `0x02089FA0` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:167 |
| GetArraySize | `0x020A1D40` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:169 |
| GetDisplayInfo | `0x020A5120` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:181 |
| GetElement | `0x020A5A30` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:172 |
| GetMember | `0x020A7F40` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:157 |
| GetText | `0x020AD7B0` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:179 |
| GotoLabeledFrame | `0x020AF5D0` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:176 |
| HasMember | `0x020AFB90` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:154 |
| Invoke | `0x020B1C00` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:163 |
| AddManaged_Internal | `0x020B9B10` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:183 |
| ReleaseManaged_Internal | `0x020B9B60` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:186 |
| PopBack | `0x020BE770` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:174 |
| PushBack | `0x020C2850` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:173 |
| SetDisplayInfo | `0x020CEDD0` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:182 |
| SetMember | `0x020D04C0` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:160 |
| SetText | `0x020D35A0` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:180 |
| VisitElements | `0x020DAFC0` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:175 |
| VisitMembers | `0x020DB0F0` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:178 |
| GetChildElement | `0x020F0CA0` | RelocAddr | - | GameMenus.cpp:8 |
| BSScaleformTint | `0x020F2870` | RelocAddr | BSScaleformManager | Hooks_Scaleform.cpp:320 |
| ApplyColorFilter | `0x020F2870` | RelocAddr | - | ScaleformValue.cpp:5 |
| SetDefaultColors | `0x020F2AC0` | RelocAddr | - | ScaleformValue.cpp:6 |
| GetFilterColorByType | `0x020F2B70` | RelocAddr | - | ScaleformValue.cpp:4 |
| RemoveChild_Internal | `0x0210D220` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:265 |
| GetExtDisplayInfo | `0x0210DAC0` | RelocAddr | - | ScaleformValue.cpp:8 |
| SetExtDisplayInfo | `0x0210DC50` | RelocAddr | - | ScaleformValue.cpp:10 |
| SetExtDisplayInfoAlpha | `0x0210DDD0` | RelocAddr | - | ScaleformValue.cpp:9 |
| BSScaleformManager_Ctor | `0x02110310` | RelocAddr | BSScaleformManager | Hooks_Scaleform.cpp:316 |
| LoadMovie | `0x021109B0` | DEFINE_MEMBER_FN | BSScaleformManager | ScaleformLoader.h:46 |
| ProcessEventQueue_Internal | `0x0211CE60` | RelocAddr | - | Hooks_Threads.cpp:22 |
| SetArraySize | `0x0219C770` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:171 |
| BindObject | `0x02708B70` | DEFINE_MEMBER_FN | IObjectBindPolicy | PapyrusInterfaces.h:195 |
| Destroy_Internal | `0x02710F50` | DEFINE_MEMBER_FN | VMIdentifier | PapyrusValue.h:257 |
| Destroy | `0x02715910` | DEFINE_MEMBER_FN | VMValue | PapyrusValue.h:221 |
| Set | `0x02715F60` | DEFINE_MEMBER_FN | VMValue | PapyrusValue.h:220 |
| GetVMPropertyInfo | `0x02718920` | RelocAddr | - | PapyrusInterfaces.cpp:8 |
| GetOffset | `0x02728FB0` | DEFINE_MEMBER_FN | VMArgList | PapyrusArgs.h:32 |
| Get | `0x02729010` | DEFINE_MEMBER_FN | VMArgList | PapyrusArgs.h:34 |
| Impl_GetSourceFile | `0x027323D0` | DEFINE_MEMBER_FN | NativeFunctionBase | PapyrusNativeFunctions.h:113 |
| Impl_GetParamName | `0x027323F0` | DEFINE_MEMBER_FN | NativeFunctionBase | PapyrusNativeFunctions.h:114 |
| Impl_Invoke | `0x02732500` | DEFINE_MEMBER_FN | NativeFunctionBase | PapyrusNativeFunctions.h:112 |
| Impl_ctor | `0x02732A00` | DEFINE_MEMBER_FN | NativeFunction | PapyrusNativeFunctions.h:146 |
| Impl_dtor | `0x02732C20` | DEFINE_MEMBER_FN | NativeFunction | PapyrusNativeFunctions.h:147 |
| GetParam | `0x02732DB0` | DEFINE_MEMBER_FN | NativeFunctionBase | PapyrusNativeFunctions.h:82 |
| Destroy | `0x0273D000` | DEFINE_MEMBER_FN | VMValue | PapyrusValue.h:157 |
| SetFlag | `0x027E1390` | DEFINE_MEMBER_FN | BSShaderProperty | NiProperties.h:134 |
| SetMaterial | `0x027E1510` | DEFINE_MEMBER_FN | BSShaderProperty | NiProperties.h:133 |
| CreateBSShaderTextureSet | `0x027E2180` | RelocAddr | - | NiTextures.cpp:5 |
| ctor | `0x027E25E0` | DEFINE_MEMBER_FN | BSShaderData | NiMaterials.h:518 |
| ApplyMaterialData | `0x027E9500` | DEFINE_MEMBER_FN | BSShaderData | NiMaterials.h:520 |
| ctor | `0x027EFA70` | DEFINE_MEMBER_FN | BSEffectShaderProperty | NiProperties.h:148 |
| ctor | `0x027F1830` | DEFINE_MEMBER_FN | BSLightingShaderProperty | NiProperties.h:176 |
| MakeValidForRendering | `0x027F1B20` | DEFINE_MEMBER_FN | BSLightingShaderProperty | NiProperties.h:177 |
| LoadTextureSet | `0x027F21B0` | DEFINE_MEMBER_FN | BSLightingShaderProperty | NiProperties.h:179 |
| LoadTextureByPath | `0x027FB1A0` | RelocAddr | - | NiTextures.cpp:7 |
| UpdateShaderProperty | `0x02845180` | DEFINE_MEMBER_FN | BSGeometry | BSGeometry.h:174 |
| Copy | `0x0284AC20` | DEFINE_MEMBER_FN | BSLightingShaderMaterialBase | NiMaterials.h:205 |
| CreateShaderMaterialByType | `0x0284BC60` | RelocAddr | - | NiMaterials.cpp:4 |
| Runtime_DynamicCast_Internal | `0x0295BC2A` | RelocAddr | - | GameRTTI.cpp:7 |
| s_ExtraHealthVtbl | `0x02C7C228` | RelocAddr | - | GameExtraData.cpp:11 |
| s_ExtraPowerLinksVtbl | `0x02C7C3C8` | RelocAddr | - | GameExtraData.cpp:5 |
| s_ExtraMaterialSwapVtbl | `0x02C7C928` | RelocAddr | - | GameExtraData.cpp:14 |
| s_ExtraInstanceDataVtbl | `0x02C7DC50` | RelocAddr | - | GameExtraData.cpp:8 |
| dtor | `0x02C81C20` | DEFINE_MEMBER_FN | BSModelDB | BSModelDB.h:45 |
| g_gameVersion | `0x02C87748` | RelocAddr | - | Hooks_Gameplay.cpp:11 |
| s_BGSCharacterTint_Template_MaskVtbl | `0x02C94D58` | RelocAddr | - | GameCustomization.cpp:32 |
| s_BGSCharacterTint_Template_PaletteVtbl | `0x02C94D88` | RelocAddr | - | GameCustomization.cpp:34 |
| s_BGSCharacterTint_Template_TextureSetVtbl | `0x02C94DB8` | RelocAddr | - | GameCustomization.cpp:36 |
| s_BSFaceGenBaseMorphExtraDataVtbl | `0x02D15158` | RelocAddr | - | NiExtraData.cpp:7 |
| s_NiStringExtraDataVtbl | `0x02E3FA78` | RelocAddr | - | NiExtraData.cpp:5 |
| s_BSDynPosDataVtbl | `0x02E40CD8` | RelocAddr | - | NiExtraData.cpp:9 |
| s_NiBinaryExtraDataVtbl | `0x02E437D8` | RelocAddr | - | NiExtraData.cpp:11 |
| g_firstObScriptCommand | `0x0372EDD0` | RelocPtr | - | ObScript.cpp:4 |
| g_firstConsoleCommand | `0x0373EDC0` | RelocPtr | - | ObScript.cpp:6 |
| g_renderTargetManager | `0x03887D30` | RelocPtr | - | BSGraphics.cpp:10 |
| g_mainHeap | `0x03905A00` | RelocPtr | - | GameAPI.cpp:4 |
| g_invalidRefHandle | `0x03905E84` | RelocPtr | - | GameReferences.cpp:13 |
| g_playerCamera | `0x05907BA8` | RelocPtr | - | GameCamera.cpp:4 |
| g_globalEvents | `0x05907C98` | RelocPtr | - | GameEvents.cpp:7 |
| g_dataHandler | `0x05908100` | RelocPtr | - | GameData.cpp:4 |
| g_faceGenManager | `0x05909900` | RelocPtr | - | GameCustomization.cpp:11 |
| g_ui | `0x05909918` | RelocPtr | - | GameMenus.cpp:4 |
| g_uiMessageManager | `0x05909B48` | RelocPtr | - | GameMenus.cpp:11 |
| g_menuControls | `0x05909B58` | RelocPtr | - | GameInput.cpp:11 |
| g_gameVM | `0x0590C388` | RelocPtr | - | PapyrusVM.cpp:4 |
| g_TESProcessor | `0x0590C3F0` | RelocPtr | - | BSModelDB.cpp:4 |
| g_defaultObjectMap | `0x0590C750` | RelocPtr | - | GameData.cpp:10 |
| g_formFactoryList | `0x0590CC70` | RelocPtr | - | GameForms.cpp:7 |
| g_defaultObjectMapLock | `0x0590D1B8` | RelocPtr | - | GameData.cpp:13 |
| g_scaleformManager | `0x05917490` | RelocPtr | - | ScaleformLoader.cpp:4 |
| g_console | `0x05919B30` | RelocPtr | - | GameAPI.cpp:17 |
| g_gameSettings | `0x0591A080` | RelocPtr | - | GameSettings.cpp:11 |
| g_inputMgr | `0x05A13260` | RelocPtr | - | GameInput.cpp:8 |
| g_playerControls | `0x05A13268` | RelocPtr | - | GameInput.cpp:14 |
| g_customizationDummy2 | `0x05A13DB0` | RelocPtr | - | GameCustomization.cpp:16 |
| g_customizationDummy1 | `0x05A13DE8` | RelocPtr | - | GameCustomization.cpp:14 |
| g_isGameDataReady | `0x05A91A64` | RelocPtr | - | GameData.cpp:7 |
| g_inputDeviceMgr | `0x05A986B8` | RelocPtr | - | GameInput.cpp:6 |
| g_inputEventTable | `0x05A98AB0` | RelocPtr | - | GameInput.cpp:4 |
| g_favoritesManager | `0x05A98CE0` | RelocPtr | - | GameData.cpp:16 |
| g_characterCreation | `0x05AA0470` | RelocPtr | - | GameCustomization.cpp:6 |
| g_characterIndex | `0x05AA0490` | RelocPtr | - | GameCustomization.cpp:8 |
| g_player | `0x05ADD3D8` | RelocPtr | - | GameReferences.cpp:4 |
| g_consoleHandle | `0x05B144A8` | RelocAddr | - | GameAPI.cpp:20 |
| g_iniPrefSettings | `0x05B94E58` | RelocPtr | - | GameSettings.cpp:7 |
| NiRTTI_NiExtraData | `0x05C41E90` | RelocPtr | - | NiRTTI.cpp:22 |
| g_shaderResourceManager | `0x05C41F08` | RelocPtr | - | BSGraphics.cpp:13 |
| g_iniSettings | `0x05F14528` | RelocPtr | - | GameSettings.cpp:5 |
| g_regSettings | `0x060D4DC0` | RelocPtr | - | GameSettings.cpp:9 |
| g_D3D11Device | `0x060D4F88` | RelocPtr | - | BSGraphics.cpp:16 |
| g_D3D11DeviceContext | `0x06216C60` | RelocPtr | - | BSGraphics.cpp:19 |
| g_renderManager | `0x06219900` | RelocPtr | - | BSGraphics.cpp:7 |
| g_menuTableLock | `0x065B04B8` | RelocPtr | - | GameMenus.cpp:14 |
| g_scaleformHeap | `0x065B0EB0` | RelocPtr | - | ScaleformAPI.cpp:4 |
| g_objectHandlePolicy | `0x06755BC0` | RelocPtr | - | PapyrusInterfaces.cpp:4 |
| NiRTTI_BSShaderProperty | `0x06758ED0` | RelocPtr | - | NiRTTI.cpp:20 |
| NiRTTI_BSEffectShaderProperty | `0x06758F38` | RelocPtr | - | NiRTTI.cpp:18 |
| NiRTTI_BSLightingShaderProperty | `0x06758F48` | RelocPtr | - | NiRTTI.cpp:15 |
| g_renderer | `0x06759728` | RelocPtr | - | BSGraphics.cpp:4 |
| SetMember | `0x1B57C90` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:161 |
| AddManaged_Internal | `0x1C1C220` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:197 |
| ReleaseManaged_Internal | `0x1C1C220` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:198 |
| HasMember | `0x1C1C220` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:199 |
| GetMember | `0x1C1C220` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:200 |
| SetMember | `0x1C1C220` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:201 |
| Invoke | `0x1C1C220` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:202 |
| HasMember | `0x1b575a0` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:155 |
| GetMember | `0x1b578d0` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:158 |
| Invoke | `0x1b580d0` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:164 |
| AddManaged_Internal | `0x1b78e90` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:191 |
| ReleaseManaged_Internal | `0x1b78e90` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:192 |
| HasMember | `0x1b78e90` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:193 |
| GetMember | `0x1b78e90` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:194 |
| SetMember | `0x1b78e90` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:195 |
| Invoke | `0x1b78e90` | DEFINE_MEMBER_FN | GFxValue | ScaleformValue.h:196 |
| ScaleformInitHook_Start | `0x2792195` | RelocAddr | BSScaleformManager | Hooks_Scaleform.cpp:324 |
| ScaleformInitHook_Start | `0x27BB2F5` | RelocAddr | BSScaleformManager | Hooks_Scaleform.cpp:326 |
| ScaleformInitHook_Start | `0x2828105` | RelocAddr | BSScaleformManager | Hooks_Scaleform.cpp:325 |
| ScaleformInitHook_Start | `0x2867B05` | RelocAddr | BSScaleformManager | Hooks_Scaleform.cpp:327 |

## Key Observations

### Why Most Functions Are Unmapped

The vast majority of Papyrus Native functions are **engine-internal** -- they are
implemented directly in the Creation Engine's Papyrus VM and do not have corresponding
SFE address definitions. SFE (Script Framework Extender, the FO76 equivalent of F4SE)
only defines addresses for functions it needs to **hook, call, or extend**.

### What SFE Addresses Actually Cover

SFE's address definitions fall into categories:
1. **DEFINE_MEMBER_FN**: C++ class methods SFE calls directly (rendering, objects, customization)
2. **RelocAddr**: Standalone functions SFE calls (LookupFormByID, PlaceAtMe_Native, etc.)
3. **RelocPtr**: Global pointers to engine singletons (g_player, g_dataHandler, etc.)
4. **SFE Extensions**: New Papyrus functions SFE adds (GetWornItem, InstanceData, etc.)

### Modding Implications

Each unmapped Native function is a potential target for:
- **New SFE hooks**: Intercepting vanilla behavior
- **Address discovery**: Finding the C++ implementation in the FO76 executable
- **Signature scanning**: Creating byte patterns to locate these functions across game versions

### Server vs Client Execution

FO76 is a multiplayer game. Native function execution depends on context:
- **Server-authoritative**: Most gameplay functions (damage, inventory, quests) run server-side
- **Client-side**: Rendering, UI, visual effects, camera functions run locally
- **Replicated**: Some functions execute on both (position, animation)
- SFE hooks only affect the **client** -- server-side natives cannot be hooked
