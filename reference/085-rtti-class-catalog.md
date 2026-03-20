# Fallout 76 RTTI Class Catalog

**Extraction Date:** 2026-03-20
**Executable:** Fallout76.exe (101 MB)
**Total RTTI Strings:** 28,866
**Parsed Classes:** 28,866

## Executive Summary

Extracted 28,866 RTTI class names from the Fallout 76 retail executable using
MSVC mangled name format (`.?AV` for classes, `.?AU` for structs). These represent
every C++ class with virtual functions in the binary -- the complete type hierarchy
of the Creation Engine as used in Fallout 76.

Additionally found 102 source file paths, 1,354 Class::Method
references in strings, and 2,716 error/exception strings.

## Category Breakdown

| Category | Count | % |
|----------|------:|--:|
| BS (Core) | 7,288 | 25.2% |
| Other | 4,460 | 15.5% |
| Templates | 3,554 | 12.3% |
| AutoRegister (Factory) | 2,538 | 8.8% |
| std | 2,034 | 7.0% |
| Scaleform | 1,511 | 5.2% |
| Lambda | 1,494 | 5.2% |
| BSScript | 1,130 | 3.9% |
| Havok | 1,099 | 3.8% |
| Combat | 1,043 | 3.6% |
| Events | 865 | 3.0% |
| BGS (Game) | 484 | 1.7% |
| NetImmerse/Gamebryo | 301 | 1.0% |
| BSResource | 211 | 0.7% |
| UI | 173 | 0.6% |
| UI/Menu | 139 | 0.5% |
| TES (Engine) | 123 | 0.4% |
| Havok (Behavior) | 85 | 0.3% |
| Actor/Character | 68 | 0.2% |
| World/Cell | 38 | 0.1% |
| Networking | 35 | 0.1% |
| Animation | 32 | 0.1% |
| Workshop | 27 | 0.1% |
| BS (Rendering) | 24 | 0.1% |
| BSGraphics | 19 | 0.1% |
| Navigation | 17 | 0.1% |
| Json | 14 | 0.0% |
| Inventory/ExtraData | 13 | 0.0% |
| Quest | 13 | 0.0% |
| Magic/Effects | 12 | 0.0% |
| BS (Input/Platform) | 7 | 0.0% |
| BethesdaNet | 5 | 0.0% |
| BS (Audio) | 5 | 0.0% |
| BS (UI) | 3 | 0.0% |
| Scaleform/GFx | 1 | 0.0% |
| Shaders | 1 | 0.0% |
| **Total** | **28,866** | **100%** |

## Namespace Distribution

Top 30 namespaces by class count:

| Namespace | Count |
|-----------|------:|
| `(global)` | 6,258 |
| `BSTGlobalEvent` | 2,860 |
| `std` | 2,175 |
| `Scaleform` | 1,504 |
| `BSScript` | 927 |
| `UBSTSingletonSDMOpStaticBuffer` | 895 |
| `stl` | 623 |
| `$0CAA` | 495 |
| `DeferredComponentUpdate` | 444 |
| `$0BAA` | 414 |
| `VBSTSingletonImplicit` | 406 |
| `bps` | 288 |
| `$0EA` | 259 |
| `VCombatObjectBase` | 248 |
| `GameScript` | 234 |
| `VBSFixedString` | 172 |
| `BSResource` | 169 |
| `VCombatPathingSearchPolicyStandard` | 155 |
| `NetworkOperation` | 147 |
| `NewPipBoy` | 124 |
| `?A0x91efa4dc` | 121 |
| `VCombatPathDestinationLocation` | 108 |
| `hkReflect` | 104 |
| `Workshop` | 103 |
| `VCombatPathDestinationNone` | 101 |
| `nsContainerMenu` | 89 |
| `VBGSProcedureTreeExecStateFactory` | 74 |
| `Enlighten` | 73 |
| `VIProcedureTreeExecState` | 71 |
| `$0BA` | 65 |

## Scaleform/GFx Classes (SFE Hook Targets)

Found **1546** Scaleform/GFx related classes.
These are the UI system classes that SFE hooks into.

### (root) (15)

- `BSGFxDisplayObject`
- `BSGFxFunctionBase`
- `BSGFxFunctionHandler`
- `BSGFxObject`
- `BSScaleformFileOpener`
- `BSScaleformImageLoader`
- `BSScaleformManagedExternalTexture`
- `BSScaleformManager`
- `BSScaleformMovieLoadTask`
- `BSScaleformRenderer`
- `BSScaleformThreadCommandQueue`
- `BSScaleformTranslator`
- `BSUIScaleformData`
- `GFxConvertHandler`
- `SFRenderBufferManager`

### ?A0x4d03a30b (1)

- `BSScaleformTextureManager`

### ?A0xe5300337 (2)

- `BSScaleformAllocatorPaged`
- `BSScaleformSysMemMapper`

### ?A0xe5300337::VBSScaleformAllocatorPaged (3)

- `BSTSDMTraits`
- `BSTSingletonSDMBase`
- `BSTSingletonSDMOpStaticBuffer`

### BSResource::BSResource (1)

- `EntryDBBase`

### BSResource::ScaleformFile (4)

- `BSTSDMTraits`
- `BSTSingletonSDMBase`
- `BSTSingletonSDMOpStaticBuffer`
- `EntryDB`

### BSScaleformImageLoader (1)

- `BSTextureImage`

### ModManager_Priv::VDownloadedModTexture (1)

- `BSScaleformExternalTextureManager`

### QEAAXXZ::Scaleform (1)

- `ImagePackVisitor`

### Scaleform (46)

- `AcquireInterface`
- `AmpMovieObjectDesc`
- `BoolFormatter`
- `BufferedFile`
- `DefaultAcquireInterface`
- `DelegatedFile`
- `DoubleFormatter`
- `Event`
- `FILEFile`
- `File`
- `FileConstants`
- `FmtResource`
- `Formatter`
- `Log`
- `LongFormatter`
- `MemoryFile`
- `MemoryHeap`
- `MemoryHeapMH`
- `MemoryHeapPT`
- `MsgFormat`
- `Mutex`
- `Mutex_AreadyLockedAcquireInterface`
- `NumericBase`
- `RefCountImpl`
- `RefCountImplCore`
- `RefCountNTSImpl`
- `RefCountNTSImplCore`
- `RefCountVImpl`
- `RefCountWeakSupportImpl`
- `RepeatFormatter`
- `ResourceFormatter`
- `Semaphore`
- `SemaphoreWaitableIncrement`
- `StrFormatter`
- `SwitchFormatter`
- `SysAlloc`
- `SysAllocBase`
- `SysAllocMalloc`
- `SysAllocMapper`
- `SysAllocPaged`
- `SysAllocStatic`
- `SysFile`
- `SysMemMapper`
- `Thread`
- `UnopenedFile`
- `Waitable`

### Scaleform::$01 (45)

- `NewOverrideBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBaseNTS`
- `RefCountBaseNTS`
- `RefCountBaseNTS`
- `RefCountBaseNTS`
- `RefCountBaseStatImpl`
- `RefCountBaseStatImpl`

### Scaleform::$02 (2)

- `RefCountBaseStatImpl`
- `RefCountBaseV`

### Scaleform::$0BAB (2)

- `RefCountBase`
- `RefCountBaseStatImpl`

### Scaleform::$0BAF (7)

- `RefCountBase`
- `RefCountBaseNTS`
- `RefCountBaseNTS`
- `RefCountBaseNTS`
- `RefCountBaseNTS`
- `RefCountBaseStatImpl`
- `RefCountBaseStatImpl`

### Scaleform::$0BAH (2)

- `RefCountBase`
- `RefCountBaseStatImpl`

### Scaleform::$0BAI (3)

- `RefCountBase`
- `RefCountBase`
- `RefCountBaseStatImpl`

### Scaleform::$0BEC (4)

- `RefCountBaseNTS`
- `RefCountBaseStatImpl`
- `RefCountBaseStatImpl`
- `RefCountBaseWeakSupport`

### Scaleform::$0BED (3)

- `NewOverrideBase`
- `RefCountBase`
- `RefCountBaseStatImpl`

### Scaleform::$0BEE (2)

- `RefCountBase`
- `RefCountBaseStatImpl`

### Scaleform::$0BEF (2)

- `RefCountBaseNTS`
- `RefCountBaseStatImpl`

### Scaleform::$0BEH (7)

- `NewOverrideBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBaseNTS`
- `RefCountBaseStatImpl`
- `RefCountBaseStatImpl`

### Scaleform::$0BEI (4)

- `NewOverrideBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBaseStatImpl`

### Scaleform::$0BEJ (1)

- `NewOverrideBase`

### Scaleform::$0BFB (2)

- `RefCountBase`
- `RefCountBaseStatImpl`

### Scaleform::$0BFD (1)

- `NewOverrideBase`

### Scaleform::$0CAB (2)

- `RefCountBase`
- `RefCountBaseStatImpl`

### Scaleform::$0EB (6)

- `NewOverrideBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBaseStatImpl`

### Scaleform::$0ED (12)

- `NewOverrideBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBaseNTS`
- `RefCountBaseStatImpl`
- `RefCountBaseStatImpl`
- `RefCountBaseStatImpl`
- `RefCountBaseV`

### Scaleform::$0EE (2)

- `RefCountBase`
- `RefCountBaseStatImpl`

### Scaleform::$0EF (3)

- `RefCountBase`
- `RefCountBase`
- `RefCountBaseStatImpl`

### Scaleform::$0EH (10)

- `NewOverrideBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBaseNTS`
- `RefCountBaseStatImpl`
- `RefCountBaseStatImpl`

### Scaleform::$0EI (7)

- `NewOverrideBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBaseStatImpl`

### Scaleform::$0EJ (2)

- `RefCountBase`
- `RefCountBaseStatImpl`

### Scaleform::$0EK (13)

- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBase`
- `RefCountBaseNTS`
- `RefCountBaseNTS`
- `RefCountBaseNTS`
- `RefCountBaseNTS`
- `RefCountBaseNTS`
- `RefCountBaseStatImpl`
- `RefCountBaseStatImpl`

### Scaleform::$0EL (5)

- `RefCountBase`
- `RefCountBase`
- `RefCountBaseNTS`
- `RefCountBaseStatImpl`
- `RefCountBaseStatImpl`

### Scaleform::2 (1)

- `SysAllocBase_SingletonSupport`

### Scaleform::GFx (954)

- `AS3ByteArray_DIPixelProvider`
- `AS3Support`
- `AS3Vectoruint_DIPixelProvider`
- `ASIMEManager`
- `ASIntervalTimerIntf`
- `ASMovieRootBase`
- `ASRefCountCollector`
- `ASStringManager`
- `ASSupport`
- `ASVM`
- `AVM1Movie`
- `AVM1Movie`
- `AVM1Movie`
- `AbcDataBuffer`
- `AbcFileWithMovieDef`
- `Accelerometer`
- `Accelerometer`
- `Accelerometer`
- `Accelerometer`
- `AccelerometerEvent`
- `AccelerometerEvent`
- `AccelerometerEvent`
- `AccelerometerEvent`
- `Accessibility`
- `Accessibility`
- `AccessibilityImplementation`
- `AccessibilityImplementation`
- `AccessibilityImplementation`
- `AccessibilityProperties`
- `AccessibilityProperties`
- `AccessibilityProperties`
- `ActionScriptVersion`
- `ActionScriptVersion`
- `Activation`
- `ActivityEvent`
- `ActivityEvent`
- `Anonimous`
- `AntiAliasType`
- `AntiAliasType`
- `AppLifecycleEvent`
- `AppLifecycleEvent`
- `AppLifecycleEvent`
- `AppLifecycleEvent`
- `ApplicationDomain`
- `ApplicationDomain`
- `ApplicationDomain`
- `ApplicationDomain`
- `ArgumentError`
- `ArrVisitor`
- `Array`
- ... and 904 more

### Scaleform::HeapPT (2)

- `SysAllocGranulator`
- `SysAllocWrapper`

### Scaleform::MemoryHeap (1)

- `LimitHandler`

### Scaleform::Render (330)

- `Allocator`
- `BevelFilter`
- `BlendModeBundle`
- `BlendModeEffect`
- `BlendPrimitive`
- `BlurFilter`
- `BlurFilterImpl`
- `Bundle`
- `CacheAsBitmapFilter`
- `CacheBase`
- `CacheData`
- `CacheEffect`
- `CacheablePrimitive`
- `CacheableTargetEffect`
- `ColorMatrixFilter`
- `ComplexFill`
- `ComplexMesh`
- `ComplexMeshVertexOutput`
- `ComplexPrimitiveBundle`
- `CompositionStringBase`
- `ContextCaptureNotify`
- `ContextCaptureNotifyListVisitor`
- `ContextCaptureNotifyListVisitor_OnCapture`
- `ContextCaptureNotifyListVisitor_OnNextCapture`
- `ContextCaptureNotifyListVisitor_OnSetCaptureThreadId`
- `ContextCaptureNotifyListVisitor_OnShutdown`
- `ContextData_ImplMixin`
- `ContextData_ImplMixin`
- `ContextData_ImplMixin`
- `ContextData_ImplMixin`
- `ContextLock`
- `DDSFileImageSource`
- `DICommand`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandImpl`
- `DICommandQueue`
- ... and 280 more

### Scaleform::Scaleform (17)

- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`
- `ListNode`

### Scaleform::String (1)

- `InitStruct`

### Scaleform::V123 (3)

- `ListNodeSafe`
- `ListNodeSafe`
- `ListNodeSafe`

### ScaleformFile (2)

- `DBTraits`
- `MemoryFile`

### UBSTSingletonSDMOpStaticBuffer::?A0xe5300337 (1)

- `BSTSingletonSDM`

### UBSTSingletonSDMOpStaticBuffer::BSResource (1)

- `BSTSingletonSDM`

### UBSTSingletonSDMOpStaticBuffer::VBSScaleformManager (1)

- `BSTSingletonSDM`

### VBSScaleformManagedExternalTexture (1)

- `BSScaleformExternalTextureManager`

### VBSScaleformManager (1)

- `BSTSingletonSDMOpStaticBuffer`

### VBSScaleformManager::U?$BSTSingletonSDMOpStaticBuffer (2)

- `BSTSDMTraits`
- `BSTSingletonSDMBase`

### Z::4 (1)

- `StringReader`

### Z::_N (1)

- `FontsVisitor`

### Z::_N1 (1)

- `TextFormatVisitor`

### std::VBSGFxObject (1)

- `_Ref_count_obj_alloc`

## Player/Actor/ObjectReference Classes

Found **378** player/actor related classes.
These contain Papyrus native function implementations.

- `Actor` (Actor/Character)
- `ActorBehaviorComponent` (Actor/Character)
- `H::VActor::ActorBoneWeightsActionChannel` (Actor/Character)
- `M::VActor::ActorCCNormDotUpChannel` (Actor/Character)
- `_N::VActor::ActorCCOnStairsChannel` (Actor/Character)
- `_N::VActor::ActorCCSuportChannel` (Actor/Character)
- `ActorCombatComponent` (Actor/Character)
- `H::VActor::ActorCopyGraphVariableChannel` (Actor/Character)
- `M::VActor::ActorCopyGraphVariableChannel` (Actor/Character)
- `ActorCoreSnapshotComponent` (Actor/Character)
- `M::VActor::ActorDirectionChannel` (Actor/Character)
- `M::VActor::ActorDirectionDegreesChannel` (Actor/Character)
- `ActorEquipManager` (Actor/Character)
- `M::VActor::ActorFlightPitchChannel` (Actor/Character)
- `M::VActor::ActorFlightRollChannel` (Actor/Character)
- `?A0xc3c4fcbb::ActorItemEquippedToMiscStatHandler` (Actor/Character)
- `ActorKnowledge` (Actor/Character)
- `M::VActor::ActorLeftWeaponSpeedChannel` (Actor/Character)
- `H::VActor::ActorLookAtModeChannel` (Actor/Character)
- `ActorMagicCaster` (Actor/Character)
- `ActorMediator` (Actor/Character)
- `ActorMotionComponent` (Actor/Character)
- `M::VActor::ActorMovementDeltaSmoothedChannel` (Actor/Character)
- `ActorMover` (Actor/Character)
- `ActorPackageData` (Actor/Character)
- `ActorPathComponent` (Actor/Character)
- `ActorPerksSnapshotComponent` (Actor/Character)
- `M::VActor::ActorPitchChannel` (Actor/Character)
- `M::VActor::ActorPitchDeltaChannel` (Actor/Character)
- `ActorPowerArmorWorkbenchComponent` (Actor/Character)
- `ActorProjectileSnapshotComponent` (Actor/Character)
- `M::VActor::ActorRollChannel` (Actor/Character)
- `ActorServerAuthSnapshotData` (Actor/Character)
- `ActorSpecialMutator` (Actor/Character)
- `M::VActor::ActorSpeedChannel` (Actor/Character)
- `M::VActor::ActorSpeedSmoothedChannel` (Actor/Character)
- `ActorState` (Actor/Character)
- `ActorTargetCheck` (Actor/Character)
- `?A0xee76dd5a::ActorTargetCheck` (Actor/Character)
- `M::VActor::ActorTimeDeltaChannel` (Actor/Character)
- `M::VActor::ActorTurnDeltaChannel` (Actor/Character)
- `M::VActor::ActorTurnDeltaSmoothedChannel` (Actor/Character)
- `ActorValueInfo` (Actor/Character)
- `ActorValueOwner` (Actor/Character)
- `?A0x5bc61b29::ActorValueReplaceTagsFunc` (Actor/Character)
- `ActorValuesSnapshotComponent` (Actor/Character)
- `ActorValuesSnapshotComponent::ActorValuesSnapshotData` (Actor/Character)
- `H::VActor::ActorWantBlockChannel` (Actor/Character)
- `M::VActor::ActorWardHealthChannel` (Actor/Character)
- `M::VActor::ActorWeaponSpeedChannel` (Actor/Character)
- `GameScript::AllPlayersEventHandler` (Other)
- `BGSMoviePlayer` (BGS (Game))
- `BGSPlayerMusicChanger` (BGS (Game))
- `BGSPlayerTitle` (BGS (Game))
- `BGSSceneActionPlayerDialogue` (BGS (Game))
- `BGSSceneActionPlayerDialogueInstance` (BGS (Game))
- `BGSVisitProceduresInitActorLocation` (BGS (Game))
- `BSISoundOutputModel::BSIAttenuationCharacteristics` (BS (Core))
- `BSISoundDescriptorUtils::BSIPlaybackCharacteristics` (BS (Core))
- `BSPlayerDistanceCheckController` (BS (Core))
- `BSPlayerEnableManager` (BS (Core))
- `BabylonEndMatchForPlayerMsg` (Other)
- `BasePlayerCharacter` (Other)
- `BootPlayersFromInstanceWarning` (Other)
- `CharacterCardDataModel` (Actor/Character)
- `CharacterCard_HoverCharacter` (Actor/Character)
- `CharacterCollisionHandler` (Actor/Character)
- `MainSinks::CharacterCollisionMessagePlayerAdapter` (Actor/Character)
- `Scaleform::GFx::CharacterDef` (Scaleform)
- `CharacterEvent` (Actor/Character)
- `CharacterIdPayload` (Actor/Character)
- `CharacterManager` (Actor/Character)
- `CharacterMenu_DeleteCharacter` (Actor/Character)
- `CharacterMenu_ListCharacters` (Actor/Character)
- `CharacterMenu_NewCharacter` (Actor/Character)
- `CharacterMenu_SelectCharacter` (Actor/Character)
- `CharacterNameChangeMsg` (Actor/Character)
- `CharacterSelection_DemandImage` (Actor/Character)
- `CharacterSelection_ImageLoad` (Actor/Character)
- `CharacterSelection_ImageUnload` (Actor/Character)
- `CharacterSelection_MenuClose` (Actor/Character)
- `CharacterSelection_MenuOpen` (Actor/Character)
- `CharacterSelection_SelectionChange` (Actor/Character)
- `hkXmlParser::Characters` (Havok)
- `ClientAuthPlayerMotionComponent` (Networking)
- `ClientPlayerCoreSnapshotComponent` (Networking)
- `CombatMovementRequestFollowActor` (Combat)
- `CombatPathDestinationActor` (Combat)
- `CombatPathDestinationFollowActor` (Combat)
- `CombatTargetSelectorPrefersPlayers` (Combat)
- `CharacterManager::CreateCharacterOperation` (Other)
- `CustomActorPackageData` (Other)
- `CharacterManager::DeleteCompleteCharacterOperation` (Other)
- `CharacterManager::DeleteFOWCharacterNoWorldOperation` (Other)
- `CharacterManager::DeleteIncompleteCharacterOperation` (Other)
- `DisableCharacterBumperHandler` (Other)
- `DisableCharacterPitchHandler` (Other)
- `DumpActorInfoToLog` (Other)
- `BGSSoundOutput::DynamicAttenuationCharacteristics` (Other)
- `EnableCharacterBumperHandler` (Other)
- `EnableCharacterPitchHandler` (Other)
- `EnablePlayerPipboyRequest` (Other)
- `DialogueNetworkRM::EndPlayerDialogueMessage` (Other)
- `EvaluatePlayerActivationMsg` (Other)
- `EvaluatePlayerActivationResultMsg` (Other)
- `ExtraActorCause` (Other)
- `ExtraActorFlagOverrides` (Other)
- `ExtraActorValueStorage` (Other)
- `ExtraPlayerCrimeList` (Other)
- `ExtraPlayerPrivateSceneInfo` (Other)
- `ExtraPlayerStorage` (Other)
- `FalloutWorldsCharacterMenu` (UI/Menu)
- `FalloutWorlds_CloseFalloutWorldsCharacterMenu` (UI/Menu)
- `FalloutWorlds_OpenFalloutWorldsCharacterMenu` (UI/Menu)
- `FalloutWorlds_ReimportCharacter` (Other)
- `FalloutWorlds_RevertCharacter` (Other)
- `FalloutWorlds_TransformCharacter` (Other)
- `FalloutWorlds_UnlinkCharacterFromWorlds` (Other)
- `CharacterManager::ForkCharacterOperation` (Other)
- `ProcessLists::GetActorsFilter` (Other)
- `CharacterManager::GetCharacterListOperation` (Other)
- `CharacterManager::GetCharacterOperation` (Other)
- `GetFullyEnabledActorCountOnServerMsg` (Other)
- `GetFullyEnabledActorResponseMsg` (Other)
- `CharacterManager::GetSelectedCharacterOperation` (Other)
- `GuardActorPackageData` (Other)
- `HUDActorValueMeterBase` (UI)
- `HUDPlayerHealthMeter` (UI)
- `?A0xbf4ba210::HandlePlayerPerspectiveSwitchForEyeTracking` (Other)
- `HighActorCuller` (Other)
- `IMovementPlayerControls` (Other)
- `IMovementPlayerControlsFilter` (Other)
- `IMovementQueryActorAvoidance` (Other)
- `IMovementSetPlayerControls` (Other)
- `Scaleform::GFx::ImageShapeCharacterDef` (Scaleform)
- `KillActorHandler` (Other)
- `LocalPlayerCharacter::LocalPlayerBestBuildProximityTracker` (Other)
- `LocalPlayerCharacter` (Other)
- `LowPriorityActorValueSnapshotComponent` (Other)
- `Scaleform::GFx::MorphCharacterDef` (Scaleform)
- `MovementAgentActorAvoider` (Other)
- `MovementAgentActorState` (Other)
- `MovementHandlerAgentPlayerControls` (Other)
- `MovementHandlerAgentPlayerControlsActionTrigger` (Other)
- `MovementMessageActorCollision` (Other)
- `MoviePlayer` (Other)
- `NetPlayerDownMsg` (Other)
- `NewPlayerLoadoutSelectedEventToServer` (Other)
- `NewPlayerLoadoutSelectedResponseToClient` (Other)
- `NewPlayerLoadoutsDataModel` (Other)
- `NewPlayerLoadoutsMenu` (UI/Menu)
- `NonActorMagicCaster` (Other)
- `NonActorMagicTarget` (Other)
- `VObjectREFRNetworkEntityComponent::UActorCombatSnapshot::NonAuthObjectREFRNetworkEntityComponent` (Templates)
- `VInterpolatorComponent::UAnimProgressSnapshotData::NonAuthObjectREFRNetworkEntityComponent` (Templates)
- `VObjectREFRNetworkEntityComponent::UPlayerPrivateQuestSnapshot::NonAuthObjectREFRNetworkEntityComponent` (Templates)
- `VObjectREFRNetworkEntityComponent::UPVPCombatSnapshot::NonAuthObjectREFRNetworkEntityComponent` (Templates)
- `VObjectREFRNetworkEntityComponent::TESObjectACTIDefs::URadioReceiverData::NonAuthObjectREFRNetworkEntityComponent` (Templates)
- `VObjectREFRNetworkEntityComponent::I::V?$RadioAudioData::NonAuthObjectREFRNetworkEntityComponent` (Templates)
- `VObjectREFRNetworkEntityComponent::BSResource::UID::V?$RadioAudioData::NonAuthObjectREFRNetworkEntityComponent` (BSResource)
- `NotifyPlayerAddictionMsg` (Other)
- `NotifyPlayerOnCharacterLoadMissingFormError` (Other)
- `NotifyPlayerOnCharacterSaveFailureMsg` (Other)
- `NotifyPlayerOnSpecialBuildCardRemovalMsg` (Other)
- `NotifySheltersPlayerEnterExit` (Other)
- `ObjectREFRNetworkEntity` (Other)
- `ObjectREFRNetworkEntityComponent` (Other)
- `AIProcess::PendingActorHeadData` (Other)
- `PerformHitsOnActors` (Other)
- `PipboyPlayerInfoData` (Other)
- `PipboyPlayerInfoMenu` (UI/Menu)
- `PlayerActivatedExplosionTimerMsg` (Other)
- `?A0xc3c4fcbb::PlayerAddictedToMiscStatHandler` (Other)
- `PlayerArea` (Other)
- `PlayerBedEnterHandler` (Other)
- `PlayerCamera` (Other)
- `PlayerCameraTransitionState` (Other)
- `PlayerCastFinishedHandler` (Other)
- `PlayerCaughtFishHandler` (Other)
- `PlayerChairEnterHandler` (Other)
- `PlayerCheatingEventToServer` (Other)
- `PlayerConnection` (Other)
- `PlayerContextMenuDataModel` (Other)
- `M::VActor::PlayerControllerXRawChannel` (Templates)
- `M::VActor::PlayerControllerXSmoothedChannel` (Templates)
- `M::VActor::PlayerControllerXSumChannel` (Templates)
- `M::VActor::PlayerControllerYRawChannel` (Templates)
- `M::VActor::PlayerControllerYSmoothedChannel` (Templates)
- `M::VActor::PlayerControllerYSumChannel` (Templates)
- `PlayerControls` (Other)
- `PlayerCoreSnapshotComponent` (Other)
- `PlayerCurrencyUpdateNotificationMsg` (Other)
- `PlayerData` (Other)
- `HUDMessages::PlayerData` (Other)
- `PlayerDeathUIDataModel` (Other)
- `M::VActor::PlayerDirectionSmoothedChannel` (Templates)
- `PlayerEmoteCancelUIEventToClient` (Other)
- `PlayerEmoteUIEventToClient` (Other)
- `PlayerEmoteUIEventToServer` (Other)
- `PlayerEnteredKeycodeMsg` (Other)
- `PlayerFastEquipSoundHandler` (Other)
- `PlayerFearEffect` (Other)
- `M::VActor::PlayerFirstSpeedSmoothedChannel` (Templates)
- `PlayerFishingSnapshotComponent` (Other)
- `PlayerFurnitureExitHandler` (Other)
- `PlayerInfoUIDataModel` (Other)
- `PlayerInfo_ViewedChangePlayerIconPrompt` (Other)
- `PlayerInfo_ViewedChangePlayerIconTutorial` (Other)
- `PlayerInputHandler` (Other)
- `PlayerInventoryDataModel` (Other)
- `PlayerLobbyMembershipChangedMsg` (Other)
- `PlayerMurderMsg` (Other)
- `PlayerPickedLockMsg` (Other)
- `M::VActor::PlayerPitchDeltaSmoothedChannel` (Templates)
- `PlayerPlacedBountyMsg` (Other)
- `PlayerPrivateChallengeComponent` (Other)
- `PlayerPrivateCoreSnapshotComponent` (Other)
- `PlayerPrivatePositionListSnapshotComponent` (Other)
- `PlayerPrivateQuestComponent` (Other)
- `PlayerPrivateStatsComponent` (Other)
- `PlayerQuestAutoTrackMsg` (Other)
- `PlayerRegionState` (Other)
- `PlayerRejectSharedPerksMsg` (Other)
- `DialogueNetworkRM::PlayerRequestDialogueSkip` (Other)
- `PlayerSendBabylonLoadoutToServer` (Other)
- `WorkshopNetwork::PlayerSettingsInfo` (Other)
- `PlayerSightedStateChangeHandler` (Other)
- `MainSinks::PlayerSleepWaitMovementControllerAdapter` (Other)
- `PlayerSneakStateChangeHandler` (Other)
- `PlayerStartPickingLockMsg` (Other)
- `PlayerStatusMsg` (Other)
- `PlayerTeam` (Other)
- `PlayerTerminalEnterHandler` (Other)
- `PlayerTitleManager` (Other)
- `SecureTrading::PlayerTradeAcceptFail` (Other)
- `SecureTrading::PlayerTradeAcceptOffer` (Other)
- `SecureTrading::PlayerTradeBegin` (Other)
- `SecureTrading::PlayerTradeCancelRequestItem` (Other)
- `SecureTrading::PlayerTradeCreateOffer` (Other)
- `SecureTrading::PlayerTradeDeleteOffer` (Other)
- `SecureTrading::PlayerTradeEnd` (Other)
- `SecureTrading::PlayerTradeInviteTimeout` (Other)
- `SecureTrading::PlayerTradeRejectOffer` (Other)
- `SecureTrading::PlayerTradeRequestItem` (Other)
- `SecureTrading::PlayerTradeSyncOffers` (Other)
- `PlayerUnlockedWithKeyMsg` (Other)
- `SecureTradingCampVending::PlayerVendingAcceptFail` (Other)
- `SecureTradingCampVending::PlayerVendingAcceptOffer` (Other)
- `SecureTradingCampVending::PlayerVendingBegin` (Other)
- `SecureTradingCampVending::PlayerVendingCreateOffer` (Other)
- `PlayerVendingMenu` (UI/Menu)
- `SecureTradingCampVending::PlayerVendingRemoveOffer` (Other)
- `GameScript::PlayerWorkshopEventHandler` (Other)
- `QueuedActor` (Other)
- `QueuedCharacter` (Other)
- `QueuedPlayer` (Other)
- `QuickPlayPlayerViewDataComponent` (Other)
- `QuickplayPlayerEndMatchResults` (Other)
- `RemotePlayerCharacter` (Other)
- `RemotePlayerInventoryDataModel` (Other)
- `RemotePlayerListener` (Other)
- `RemoteServerActorBehaviorComponent` (Other)
- `RemoteServerActorMotionComponent` (Other)
- `RemoteServerActorProjectileComponent` (Other)
- `DialogueNetworkRM::RequestExitPlayerDialogueScene` (Other)
- `RequestHitsOnActors` (Other)
- `RequestMakePlayerGhoul` (Other)
- `RequestOpenNewPlayerLoadoutsMenuMsg` (Other)
- `RequestPlaySoundForNearbyPlayersMsg` (Other)
- `DialogueNetworkRM::RequestPlayerDialogueSceneHistoryMsg` (Other)
- `RequestPlayerTitleChange` (Other)
- `SecureTrading::RequestPlayerTradeAcceptOffer` (Other)
- `SecureTrading::RequestPlayerTradeBegin` (Other)
- `SecureTrading::RequestPlayerTradeCancelRequestItem` (Other)
- `SecureTrading::RequestPlayerTradeCreateOffer` (Other)
- `SecureTrading::RequestPlayerTradeDeleteOffer` (Other)
- `SecureTrading::RequestPlayerTradeEnd` (Other)
- `SecureTrading::RequestPlayerTradeRejectOffer` (Other)
- `SecureTrading::RequestPlayerTradeRequestItem` (Other)
- `SecureTrading::RequestPlayerTradeSyncOffers` (Other)
- `SecureTradingCampVending::RequestPlayerVendingAcceptOffer` (Other)
- `SecureTradingCampVending::RequestPlayerVendingBegin` (Other)
- `SecureTradingCampVending::RequestPlayerVendingCreateOffer` (Other)
- `SecureTradingCampVending::RequestPlayerVendingEnd` (Other)
- `CharacterManager::ResetCharacterOperation` (Other)
- `ResetPlayerAFKTimerMsg` (Other)
- `DialogueNetworkRM::SayInPlayersHeadMessage` (Other)
- `?A0x0b4a4e72::SelfieCameraCharacterController` (Other)
- `DialogueNetworkRM::SendPlayerDialogueChoiceMessage` (Other)
- `GameScript::?A0xae65dc8b::SendPlayerToJailFunctor` (Other)
- `DialogueNetworkRM::SetActorInPrivateSceneDialogueMessage` (Other)
- `Scaleform::GFx::ShapeBaseCharacterDef` (Scaleform)
- `ShowTutorialToPlayerMsg` (Other)
- `GameScript::SingleActorArgument` (Other)
- `GameScript::SinglePlayerArgument` (Other)
- `SocialData_UpdateRecentPlayers` (Other)
- `BGSStandardSoundDef::SoundPlaybackCharacteristics` (Other)
- `DialogueNetworkRM::StartPlayerDialogueActionMessage` (Other)
- `Scaleform::GFx::StaticTextCharacter` (Scaleform)
- `?A0x4eb84d2a::SubGraphCharacterPropertySymbolMap` (Other)
- `Scaleform::GFx::SwfShapeCharacterDef` (Scaleform)
- `SyncPlayerTitles` (Other)
- `TESActorBase` (TES (Engine))
- `TESActorBaseData` (TES (Engine))
- `TESLevCharacter` (TES (Engine))
- `TESObjectREFR` (TES (Engine))
- `TESObjectREFRCoreSnapshotComponent` (TES (Engine))
- `?A0x1e0766f5::TESObjectREFRFactory` (TES (Engine))
- `TESObjectREFRPhysicsSnapshotComponent` (TES (Engine))
- `TESObjectREFRQuestItemSnapshotComponent` (TES (Engine))
- `TESObjectREFRScriptObjectSnapshotComponent` (TES (Engine))
- `TESObjectREFRServerAuthSnapshotData` (TES (Engine))
- `TESObjectREFRTransformSnapshotComponent` (TES (Engine))
- `TESObjectREFR_EventsWrapper` (TES (Engine))
- `?A0x9815ed7f::UnlinkCharacterFromWorlds_ConfirmCallback` (Other)
- `?A0x9815ed7f::UnlinkCharacterToEnterWorld_ConfirmCallback` (Other)
- `WarnPlayerBeforeAFKDisconnectMsg` (Other)
- `WorldData_OpenCharacterCreation` (World/Cell)
- `bhkCharacterCollisionHandler` (Havok (Behavior))
- `bhkCharacterController` (Havok (Behavior))
- `bhkCharacterControllerCinfo` (Havok (Behavior))
- `bhkCharacterPointCollector` (Havok (Behavior))
- `bhkCharacterProxy` (Havok (Behavior))
- `bhkCharacterRigidBody` (Havok (Behavior))
- `bhkCharacterRigidBodyCinfo` (Havok (Behavior))
- `bhkCharacterState` (Havok (Behavior))
- `bhkCharacterStateClimbing` (Havok (Behavior))
- `bhkCharacterStateFloating` (Havok (Behavior))
- `bhkCharacterStateFlying` (Havok (Behavior))
- `bhkCharacterStateInAir` (Havok (Behavior))
- `bhkCharacterStateJumping` (Havok (Behavior))
- `bhkCharacterStateOnGround` (Havok (Behavior))
- `bhkCharacterStateSwimming` (Havok (Behavior))
- `bhkRemoteCharacterManager` (Havok (Behavior))
- `RemoteCharacterState::bhkRemoteCharacterState` (Havok (Behavior))
- `hkbCharacter` (Havok)
- `hkbCharacterAddedInfo` (Havok)
- `hkbCharacterControlCommand` (Havok)
- `hkbCharacterController` (Havok)
- `hkbCharacterControllerDriver` (Havok)
- `hkbCharacterControllerModifier` (Havok)
- `hkbCharacterControllerModifierInternalState` (Havok)
- `hkbCharacterControllerSceneModifier` (Havok)
- `hkbCharacterData` (Havok)
- `hkbCharacterInfo` (Havok)
- `hkbCharacterSelectedInfo` (Havok)
- `hkbCharacterSetup` (Havok)
- `hkbCharacterSkeletonChangedCommand` (Havok)
- `hkbCharacterSkinInfo` (Havok)
- `hkbCharacterSteppedInfo` (Havok)
- `hkbCharacterStringData` (Havok)
- `hkbCharacterSymbolLinker` (Havok)
- `hkbClientCharacterState` (Havok)
- `hkbMoveCharacterModifier` (Havok)
- `hkbMoveCharacterModifierInternalState` (Havok)
- `hkbRotateCharacterModifier` (Havok)
- `hkbRotateCharacterModifierInternalState` (Havok)
- `hkbSetSelectedCharacterCommand` (Havok)
- `hkbUpdateCharacterTask` (Havok)
- `hkbnpCharacterController` (Havok)
- `hkbnpCharacterProxyController` (Havok)
- `hkbnpCharacterRigidBodyController` (Havok)
- `hknpBSCharacterProxy` (Havok)
- `hknpBSCharacterRigidBody` (Havok)
- `hknpCharacterContext` (Havok)
- `hknpCharacterProxy` (Havok)
- `hknpCharacterProxyCinfo` (Havok)
- `hknpCharacterProxyListener` (Havok)
- `hknpCharacterRigidBody` (Havok)
- `hknpCharacterRigidBodyCinfo` (Havok)
- `hknpCharacterRigidBodyListener` (Havok)
- `hknpCharacterState` (Havok)
- `hknpCharacterStateClimbing` (Havok)
- `hknpCharacterStateInAir` (Havok)
- `hknpCharacterStateJumping` (Havok)
- `hknpCharacterStateManager` (Havok)
- `hknpCharacterStateOnGround` (Havok)
- `hknpFirstPersonCharacter` (Havok)

## Debug/Developer Classes in Retail Build

Found **739** classes with debug/developer naming in the retail executable.
These should not normally ship in release builds.

### Animation (1)

- `GameScript::Internal::AnimationCallbacks`

### AutoRegister (Factory) (20)

- `VCombatAcquireSearchDebugData::AutoRegisterCombatObject`
- `VCombatCoveredPathDebugData::AutoRegisterCombatObject`
- `VCombatCoverSearchDebugData::AutoRegisterCombatObject`
- `VCombatMeleeDebugData::AutoRegisterCombatObject`
- `VCombatPathingDebugData::AutoRegisterCombatObject`
- `VCombatProjectileDebugData::AutoRegisterCombatObject`
- `$0CAA::IVCombatObjectBase::V?$BSTCreateFactoryManager::VCombatAcquireSearchDebugData::AutoRegisterCreator`
- `$0CAA::IVCombatObjectBase::V?$BSTCreateFactoryManager::VCombatCoveredPathDebugData::AutoRegisterCreator`
- `$0CAA::IVCombatObjectBase::V?$BSTCreateFactoryManager::VCombatCoverSearchDebugData::AutoRegisterCreator`
- `$0CAA::IVCombatObjectBase::V?$BSTCreateFactoryManager::VCombatMeleeDebugData::AutoRegisterCreator`
- `$0CAA::IVCombatObjectBase::V?$BSTCreateFactoryManager::VCombatPathingDebugData::AutoRegisterCreator`
- `$0CAA::IVCombatObjectBase::V?$BSTCreateFactoryManager::VCombatProjectileDebugData::AutoRegisterCreator`
- `VPhotoGalleryMenu_MakeProfilePhoto::V?$TUIEventDispatcher::AutoRegisterEvent`
- `$0CAA::IVCombatObjectBase::V?$BSTCreateFactoryManager::VCombatObjectBase::VCombatAcquireSearchDebugData::U?$BSTDerivedCreator::AutoRegisterFactory`
- `$0CAA::IVCombatObjectBase::V?$BSTCreateFactoryManager::VCombatObjectBase::VCombatCoveredPathDebugData::U?$BSTDerivedCreator::AutoRegisterFactory`
- `$0CAA::IVCombatObjectBase::V?$BSTCreateFactoryManager::VCombatObjectBase::VCombatCoverSearchDebugData::U?$BSTDerivedCreator::AutoRegisterFactory`
- `$0CAA::IVCombatObjectBase::V?$BSTCreateFactoryManager::VCombatObjectBase::VCombatMeleeDebugData::U?$BSTDerivedCreator::AutoRegisterFactory`
- `$0CAA::IVCombatObjectBase::V?$BSTCreateFactoryManager::VCombatObjectBase::VCombatPathingDebugData::U?$BSTDerivedCreator::AutoRegisterFactory`
- `$0CAA::IVCombatObjectBase::V?$BSTCreateFactoryManager::VCombatObjectBase::VCombatProjectileDebugData::U?$BSTDerivedCreator::AutoRegisterFactory`
- `VBSTSingletonImplicit::$0CAA::VUIEventDispatcher::VBSFixedString::V?$BSTFactoryManager::VPhotoGalleryMenu_MakeProfilePhoto::V?$TUIEventDispatcher::AutoRegisterFactory`

### BGS (Game) (1)

- `logging::BGSMessageHandlerDebugOutput`

### BS (Core) (35)

- `BSImGuiShader`
- `BSImagespaceShaderISDOFComposite_DEBUG_FOCAL`
- `BSImagespaceShaderISDownsampleCS_GRIDSIZE_X_PICK_BRIGHTEST`
- `BSImagespaceShaderISDownsample_COMPENSATE_PICK_BRIGHTEST`
- `BSImagespaceShaderISShadowAtlasDebug`
- `BSNiAlphaPropertyTestRefController`
- `VCombatObjectBase::VCombatAcquireSearchDebugData::BSTDerivedCreator`
- `VCombatObjectBase::VCombatCoveredPathDebugData::BSTDerivedCreator`
- `VCombatObjectBase::VCombatCoverSearchDebugData::BSTDerivedCreator`
- `VCombatObjectBase::VCombatMeleeDebugData::BSTDerivedCreator`
- `VCombatObjectBase::VCombatPathingDebugData::BSTDerivedCreator`
- `VCombatObjectBase::VCombatProjectileDebugData::BSTDerivedCreator`
- `UTESTopicInfoEvent::BSTEventSink`
- `UTESTrackedStatsEvent::BSTEventSink`
- `UTESTrapHitEvent::BSTEventSink`
- `UTESTriggerEnterEvent::BSTEventSink`
- `UTESTriggerLeaveEvent::BSTEventSink`
- `VPhotoGalleryMenu_MakeProfilePhoto::BSTEventSink`
- `UConsoleLogAddEvent::BSTEventSource`
- `UDebugOverlayUpdateEvent::BSTEventSource`
- `UTESTopicInfoEvent::BSTEventSource`
- `UTESTrackedStatsEvent::BSTEventSource`
- `UTESTrapHitEvent::BSTEventSource`
- `UTESTriggerEnterEvent::BSTEventSource`
- `UTESTriggerEvent::BSTEventSource`
- `UTESTriggerLeaveEvent::BSTEventSource`
- `VPhotoGalleryMenu_MakeProfilePhoto::BSTEventSource`
- `BSTGlobalEvent::VPhotoGalleryMenu_MakeProfilePhoto::V?$EventSource::U?$BSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::VPhotoGalleryMenu_MakeProfilePhoto::V?$EventSource::BSTSDMTraits`
- `VConsoleLog::U?$BSTSingletonSDMOpStaticBuffer::VConsoleLog::BSTSDMTraits`
- `UBSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::VPhotoGalleryMenu_MakeProfilePhoto::V?$EventSource::BSTSingletonSDM`
- ... and 5 more

### BSScript (344)

- `BSScript::Internal::AutoPropGetFunction`
- `BSScript::Internal::AutoPropSetFunction`
- `BSScript::Internal::UFunctionMessage::BSTCommonLLMessageQueue`
- `BSScript::Internal::UFunctionMessage::BSTCommonMessageQueue`
- `$0IA::BSScript::Internal::USuspendedStack::BSTCommonStaticMessageQueue`
- `BSScript::Internal::UFunctionMessage::BSTFreeList`
- `BSScript::Internal::UFunctionMessage::BSTMessageQueue`
- `BSScript::Internal::USuspendedStack::BSTMessageQueue`
- `$0EAA::BSScript::Internal::UFunctionMessage::BSTStaticFreeList`
- `BSScript::Internal::PEAD::CachedErrorMessageImpl`
- `BSScript::Internal::PEBD::CachedErrorMessageImpl`
- `BSScript::Internal::std::Z::$$A6AXAEAVBSFixedString::V?$function::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_000d9932fcc5ef59a8ca536ffbdbdcf1>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_01d3077005695ffd017103cb08a7b4cb>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_026c798660227a30ff6907caf3eac2ce>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_02af2855ca4fc227d521c33062509c85>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_03055c5726eff8742aba93148de34f15>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_0318c85035bc031f6e1362f34196cbb4>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_04d6538eaa2d34cbfc73b2a1d1ab6546>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_04ea37b39edcb2a34a6fafb5c5a41161>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_04f05bb16d6eb6733a20b4e491a86d8a>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_04f45c4c94af0eb744d64c6ae150d431>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_0535a95e6d5139c29b199db5f9344c30>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_063f10df0f8d5ed56c3fa769c5a165e3>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_076430ac052de30bfc68e09e7ff3d9b5>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_07710e8f4f2acb7d500202cc406b2793>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_09511f3207d101eaa2f0e3d38366b6e5>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_09aeb6ff51fba55be58e4ba3cd4740be>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_09d019cb3b563f95ba2b3ae6a74bd189>::CachedErrorMessageImpl`
- `BSScript::Internal::V<lambda_0a2b79ba5f034c0fa090681a57cd46ae>::CachedErrorMessageImpl`
- ... and 314 more

### BethesdaNet (1)

- `bnet::internal::?A0x1bac7261::ModuleDeleter`

### Combat (6)

- `CombatAcquireSearchDebugData`
- `CombatCoverSearchDebugData`
- `CombatCoveredPathDebugData`
- `CombatMeleeDebugData`
- `CombatPathingDebugData`
- `CombatProjectileDebugData`

### Events (6)

- `GameScript::DebuggerMessages::Event`
- `BSTGlobalEvent::VPhotoGalleryMenu_MakeProfilePhoto::EventSource`
- `GameScript::DebuggerMessages::OutputEvent`
- `GameScript::DebuggerMessages::StoppedEvent`
- `GameScript::DebuggerMessages::ThreadEvent`
- `GameScript::DebuggerMessages::VersionEvent`

### Havok (91)

- `hknpCompressedMeshShapeInternals::UhkContainerHeapAllocator::UhknpShapeKeyDiscriminant::I$0PPPPPPPP::U?$hkHandle::V?$hkArray::AabbOverlaps`
- `hknpCompressedMeshShapeInternals::VhknpCollisionQueryCollector::AabbOverlaps`
- `hkContainerDebugAllocator::Allocator`
- `hknpCompressedMeshShapeInternals::BaseUnaryQuery`
- `hkbInternal::hks::BinOperatorEnum`
- `hkgpJobQueue::hkgpMeshInternals::ConcaveEdgeJob::UHandle::Box`
- `UhknpCompressedMeshShapeTreeDataRun::$0BF::I_K$0L::U?$hkcdStaticMeshTreeCommonConfig::?$hkcdStaticMeshTree::hknpCompressedMeshShapeInternals::UGeometryProvider::BuildGeometryProvider`
- `hkbInternal::hks::ChunkVisitor`
- `hkbInternal::hks::CodeGenerator`
- `hkbInternal::hks::CompilerParseAcceptor`
- `hkbInternal::hks::CompilerStateInterface`
- `hkgpIndexedMeshInternals::DefaultEdgeCollapseInterface`
- `hkReflect::Detail::UnitTestClang::TestDefaultTypes::W4EnumValue1::EnumPropertyImpl`
- `hkbInternal::hks::FrequencyProfiler`
- `hkbInternal::hks::GettableProfiler`
- `hkbInternal::hks::HeapVisualizer`
- `hkgpCgoInternal::ICollapse`
- `hkbInternal::hks::IProfiler`
- `hknpCompressedMeshShapeInternals::KeyMask`
- `hkbInternal::LuaPlus::LuaStateOutFile`
- `hkbInternal::hks::MemoryAllocationsByType`
- `hkbInternal::hks::Preprocessor`
- `hkbInternal::hks::Preprocessor::PreprocessorStateProxy`
- `hknpCharacterProxyInternals::QueryCollector`
- `hkbInternal::hks::ReachableChunksAreValid`
- `hkReflect::Detail::UnitTest::UBiggerStruct::RecordPropertyImpl`
- `hkReflect::Detail::UnitTest::UColorHSV2::RecordPropertyImpl`
- `hkReflect::Detail::UnitTest::UColorHSV::RecordPropertyImpl`
- `hkReflect::Detail::UnitTest::UColorRGB::RecordPropertyImpl`
- `UhknpCompoundShapeEx::?$hknpCompoundShapeInternals::ScaleAndTransformCollector`
- ... and 61 more

### Networking (3)

- `ClientHealthDiagnosticsReport1`
- `ClientHealthDiagnosticsReport2`
- `ClientHealthDiagnosticsReport3`

### Other (143)

- `UnitTest::ArrayOfRefPtrs`
- `?A0xe43d375d::AssertHandler`
- `VarTest::Bar`
- `UnitTestClang::AfterReflect::BaseVtable`
- `UnitTest::CArrayOfhkArray`
- `UnitTest::ClassTest2`
- `UnitTest::ClassTest3`
- `UnitTest::ClassWithArrayOfClassWithClassWithHashMap`
- `UnitTest::ClassWithClassWithHashMap`
- `UnitTest::Cloning::CloneFuncWrapper`
- `UnitTest::Cloning::Cloner`
- `WorkshopUI::ConfirmContestWorkshopCallback`
- `ConsoleData`
- `ConsoleLog`
- `logging::ConsoleLogOutput`
- `WorkshopNetwork::ContestWorkshopMessage`
- `GameScript::DebuggerMessages::ContinueRequest`
- `bcs::telemetry::Counter`
- `BGSGlobalLoggers::CreateBGSMsgDebugAppender`
- `BGSGlobalLoggers::CreateOutputDebugStringAppender`
- `UnitTest::CustomArrayType_Impl`
- `Camera::DebugCinematicCamera`
- `DebugConnectionClientCommandMsg`
- `DebugConnectionCommandMsg`
- `DebugGameplayAutoTestComplete`
- `Camera::DebugModule`
- `DebugPrintClientConsoleMessage`
- `DebugSetClientConsoleTarget`
- `DebugSetServerConsoleTarget`
- `Camera::DebugTargetCamera`
- ... and 113 more

### Quest (1)

- `AutomatedTesting::QuestAliasResponse`

### Scaleform (7)

- `Scaleform::Render::23::UDICommand::Scaleform::Render::UDICommand_HitTest::DICommandImpl`
- `Scaleform::Render::DICommand_HitTest`
- `Scaleform::GFx::Text::EditorKit`
- `Scaleform::Render::Text::EditorKitBase`
- `Scaleform::Render::ProfileModifier`
- `Scaleform::Render::ProfileViews`
- `Scaleform::$0EK::Scaleform::Render::Text::VEditorKitBase::RefCountBase`

### TES (Engine) (5)

- `TESTexture`
- `TESTopic`
- `TESTopicInfo`
- `TESTrap`
- `TESTrapListener`

### Templates (30)

- `UnitTest::H::ClassWithHashMap`
- `UnitTest::HXXXXX::_KVhkStringPtr::U?$hkTuple::ClassWithHashMap`
- `UnitTest::UnitTest::$$CBUObjKey::V?$hkRefPtr::ClassWithHashMap`
- `UnitTest::VhkStringPtr::ClassWithHashMap`
- `GameScript::$00::GameScript::?A0x9aaff1c6::VMoveToOwnEditorLocFunctor::ConcreteDelayFunctorFactory`
- `$0GC::VTESTopic::ConcreteFormFactory`
- `$0GD::VTESTopicInfo::ConcreteFormFactory`
- `$0CH::VTESTrap::ConcreteFormFactory`
- `$02X::$0KK::$0CH::VTESTrap::ConcreteObjectFormFactory`
- `BSInputEnableManager::V<lambda_4b8b8308f7434758c3b5ea52cdddbde5>::DebugNameFunctor`
- `BSPlayerEnableManager::V<lambda_836b8fffb3ee9beea6315bfa35f20578>::DebugNameFunctor`
- `BSInputEnableManager::V<lambda_b2e2e73bf7c4f2ee80419af6e1db4858>::DebugNameFunctor`
- `BSInputEnableManager::V<lambda_b84c567c4a4518bc261126a037782296>::DebugNameFunctor`
- `BSInputEnableManager::V<lambda_bb8e2a498fa40cc06e44bffda4385aaf>::DebugNameFunctor`
- `GameScript::GameScript::Internal::VHitRegistrationList::DispatchAndClean`
- `GameScript::GameScript::Internal::VMagicEffectApplyRegistrationList::DispatchAndClean`
- `GameScript::GameScript::Internal::VRadiationDamageRegistrationList::DispatchAndClean`
- `?A0x91efa4dc::UTESTopicInfoEvent::QueueableEventSource`
- `?A0x91efa4dc::UTESTrackedStatsEvent::QueueableEventSource`
- `?A0x91efa4dc::UTESTrapHitEvent::QueueableEventSource`
- `?A0x91efa4dc::UTESTriggerEnterEvent::QueueableEventSource`
- `?A0x91efa4dc::UTESTriggerEvent::QueueableEventSource`
- `?A0x91efa4dc::UTESTriggerLeaveEvent::QueueableEventSource`
- `bcs::telemetry::bcs::telemetry::UNullLockPolicy::SampleStorage`
- `VPhotoGalleryMenu_MakeProfilePhoto::TUIEventDispatcher`
- `UnitTestClang::UnitTestClang::AfterReflect::UInterface1::WithTemplateInterface`
- `fmt::v6::internal::D::buffer`
- `fmt::v6::internal::I::buffer`
- `fmt::v6::internal::fmt::v6::internal::D::V?$buffer::container_buffer`
- `fmt::v6::internal::D::formatbuf`

### UI/Menu (1)

- `ConsoleNativeUIMenu`

### std (44)

- `std::2::$03::AEBU?$_Ph::2::$02::AEBU?$_Ph::2::$01::AEBU?$_Ph::2::$00::AEBU?$_Ph::ZPEAV34::E::4::GAEAVBitMsgReader::EAAIAEBUnetadr_t::net::P8InternalHost::std::U_Unforced::_Binder`
- `std::2::$00::AEA_KAEBU?$_Ph::ZPEAV34::bcs::telemetry::EAA_N_KAEAVMetricBase::net::P8NetworkMetricsLogger::std::U_Unforced::_Binder`
- `std::2::$00::AEBU?$_Ph::ZPEAV3::VNiNode::EAAXAEBV?$NiPointer::P8SpawnMapDebugManager::std::U_Unforced::_Binder`
- `std::V123::stl::stl::bcs::telemetry::VSample::V?$fixed_heap_circular_buffer_storage::bcs::telemetry::VSample::?$fixed_circular_buffer_impl::NVconst_iterator::_Func_base`
- `std::$$V::std::std::GameScript::DebuggerMessages::URequest::U?$default_delete::GameScript::DebuggerMessages::URequest::V?$unique_ptr::_Func_base`
- `std::BSPlatform::X$$QEAVInternalErrorInfo::_Func_base`
- `std::UBSTSmartPointerIntrusiveRefCount::GameScript::Internal::VHitRegistrationList::XAEBV?$BSTSmartPointer::_Func_base`
- `std::UBSTSmartPointerIntrusiveRefCount::GameScript::Internal::VMagicEffectApplyRegistrationList::XAEBV?$BSTSmartPointer::_Func_base`
- `std::UBSTSmartPointerIntrusiveRefCount::GameScript::Internal::VRadiationDamageRegistrationList::XAEBV?$BSTSmartPointer::_Func_base`
- `std::V123::stl::stl::bcs::telemetry::VSample::V?$fixed_heap_circular_buffer_storage::bcs::telemetry::VSample::?$fixed_circular_buffer_impl::XVconst_iterator::_Func_base`
- `std::UBSTSmartPointerIntrusiveRefCount::GameScript::Internal::VRadiationDamageRegistrationList::XAEBV?$BSTSmartPointer::X::V?$BSTThreadScrapSTLAllocator::V<lambda_405c60446f76b9b80ba0e00cbb213408>::_Func_impl`
- `std::UBSTSmartPointerIntrusiveRefCount::GameScript::Internal::VMagicEffectApplyRegistrationList::XAEBV?$BSTSmartPointer::X::V?$BSTThreadScrapSTLAllocator::V<lambda_901f5ac83cdab32e1875799533b3d5f3>::_Func_impl`
- `std::UBSTSmartPointerIntrusiveRefCount::GameScript::Internal::VHitRegistrationList::XAEBV?$BSTSmartPointer::X::V?$BSTThreadScrapSTLAllocator::V<lambda_9c9d7a9a1264e560273a1e87d863ceb6>::_Func_impl`
- `std::UBSTSmartPointerIntrusiveRefCount::GameScript::Internal::VHitRegistrationList::XAEBV?$BSTSmartPointer::X::V?$BSTThreadScrapSTLAllocator::V<lambda_a1ea549248f1bfb890bb5e746f1f633b>::_Func_impl`
- `std::VNiNode::XAEBV?$NiPointer::std::2::$00::AEBU?$_Ph::ZPEAV3::VNiNode::EAAXAEBV?$NiPointer::P8SpawnMapDebugManager::std::U_Unforced::V?$_Binder::_Func_impl_no_alloc`
- `std::V234::stl::stl::bcs::telemetry::VSample::V?$fixed_heap_circular_buffer_storage::bcs::telemetry::VSample::?$fixed_circular_buffer_impl::XVconst_iterator::V<lambda_0493f95af75e0a20b4fba7eb8312076b>::_Func_impl_no_alloc`
- `std::$$V::std::std::GameScript::DebuggerMessages::URequest::U?$default_delete::GameScript::DebuggerMessages::URequest::V?$unique_ptr::V<lambda_122d74ae7d7bce586fa5af68ba3431a3>::_Func_impl_no_alloc`
- `std::$$V::std::std::GameScript::DebuggerMessages::URequest::U?$default_delete::GameScript::DebuggerMessages::URequest::V?$unique_ptr::V<lambda_1360cbaad8abddb60c780f18b781614a>::_Func_impl_no_alloc`
- `std::$$V::std::std::GameScript::DebuggerMessages::URequest::U?$default_delete::GameScript::DebuggerMessages::URequest::V?$unique_ptr::V<lambda_26661c3ee60583f82c0a8e4f33007bc6>::_Func_impl_no_alloc`
- `std::$$V::std::std::GameScript::DebuggerMessages::URequest::U?$default_delete::GameScript::DebuggerMessages::URequest::V?$unique_ptr::V<lambda_2fd73b4ad82a856a7f35262bac6da198>::_Func_impl_no_alloc`
- `std::$$V::std::std::GameScript::DebuggerMessages::URequest::U?$default_delete::GameScript::DebuggerMessages::URequest::V?$unique_ptr::V<lambda_44c26bdb4b5ba5aeec4291ac67f7a6ea>::_Func_impl_no_alloc`
- `std::V234::stl::stl::bcs::telemetry::VSample::V?$fixed_heap_circular_buffer_storage::bcs::telemetry::VSample::?$fixed_circular_buffer_impl::XVconst_iterator::V<lambda_477be143ad7e64de185de55426a63c7a>::_Func_impl_no_alloc`
- `std::BSPlatform::X$$QEAVInternalErrorInfo::V<lambda_4beadb5f9ce861f9fb2e4272dbb15624>::_Func_impl_no_alloc`
- `std::$$V::std::std::GameScript::DebuggerMessages::URequest::U?$default_delete::GameScript::DebuggerMessages::URequest::V?$unique_ptr::V<lambda_5be18c27ec4408ca8098fb8223deb5ce>::_Func_impl_no_alloc`
- `std::$$V::std::std::GameScript::DebuggerMessages::URequest::U?$default_delete::GameScript::DebuggerMessages::URequest::V?$unique_ptr::V<lambda_7199839f7256b32d08449753b214a28d>::_Func_impl_no_alloc`
- `std::V234::stl::stl::bcs::telemetry::VSample::V?$fixed_heap_circular_buffer_storage::bcs::telemetry::VSample::?$fixed_circular_buffer_impl::XVconst_iterator::V<lambda_9520f46decdaeab5ce46cc260198eb0e>::_Func_impl_no_alloc`
- `std::$$V::std::std::GameScript::DebuggerMessages::URequest::U?$default_delete::GameScript::DebuggerMessages::URequest::V?$unique_ptr::V<lambda_d0ad324750966cdb38ff81b276ce6632>::_Func_impl_no_alloc`
- `std::$$V::std::std::GameScript::DebuggerMessages::URequest::U?$default_delete::GameScript::DebuggerMessages::URequest::V?$unique_ptr::V<lambda_d9eb1cbb1d5f998b1066c554599b9fe8>::_Func_impl_no_alloc`
- `std::$$V::std::std::GameScript::DebuggerMessages::URequest::U?$default_delete::GameScript::DebuggerMessages::URequest::V?$unique_ptr::V<lambda_df6b8aeef250e9bd805139848d266a90>::_Func_impl_no_alloc`
- `std::$$V::std::std::GameScript::DebuggerMessages::URequest::U?$default_delete::GameScript::DebuggerMessages::URequest::V?$unique_ptr::V<lambda_e76183cdfd22a0c0b2c4a932df7c7eb2>::_Func_impl_no_alloc`
- ... and 14 more

## Source File Paths (Project Structure)

Found **102** source file paths embedded in the executable.
These reveal the internal project structure at Bethesda.

### Build Paths Discovered

- `Fallout76`
- `Project76`
- `project76`
- `project76_devmain`

### BethesdaNet SDK (9 files)

- `e:\buildagent\work\17a4e262df1933f4\project76\sdk\bethesdanet\bdk2\include\bnet\common\customdata\customdatavalue.h`
- `e:\buildagent\work\17a4e262df1933f4\project76\sdk\bethesdanet\bdk2\include\bnet\common\functional.h`
- `e:\buildagent\work\17a4e262df1933f4\project76\sdk\bethesdanet\bdk2\include\bnet\common\optional.h`
- `e:\buildagent\work\17a4e262df1933f4\project76\sdk\bethesdanet\bdk2\include\bnet\fulfillment\fulfillmenttype.h`
- `e:\buildagent\work\17a4e262df1933f4\project76\sdk\bethesdanet\bdk2\include\bnet\impl\memory\uniqueptrfactory.h`
- `e:\projects\project76_devmain\sdk\bethesdanet\bdk2\external\libtomcrypt\src\hashes\md5.c`
- `e:\projects\project76_devmain\sdk\bethesdanet\bdk2\external\libtomcrypt\src\hashes\sha1.c`
- `e:\projects\project76_devmain\sdk\bethesdanet\bdk2\external\libtomcrypt\src\hashes\sha2\sha256.c`
- `e:\projects\project76_devmain\sdk\bethesdanet\bdk2\external\libtomcrypt\src\misc\crypt\crypt_register_hash.c`

### Chromium/CEF (7 files)

- `E:\Project76_Main\SDK\cef\libcef_dll/ctocpp/ctocpp_ref_counted.h`
- `E:\Project76_Main\SDK\cef\libcef_dll/ctocpp/ctocpp_scoped.h`
- `e:\buildagent\work\17a4e262df1933f4\project76\bschromium\source\bschromium.cpp`
- `e:\buildagent\work\17a4e262df1933f4\project76\bschromium\source\bschromiumbrowserprocess.cpp`
- `e:\buildagent\work\17a4e262df1933f4\project76\bschromium\source\bschromiumclient.cpp`
- `e:\buildagent\work\17a4e262df1933f4\project76\bschromium\source\bschromiumrenderer.cpp`
- `e:\buildagent\work\17a4e262df1933f4\project76\sdk\cef\include\base\cef_ref_counted.h`

### Enlighten (GI) (69 files)

- `C:\Projects\Enlighten\Src\EnlightenAPI\LibSrc\GeoCore/GeoAutoPtr.h`
- `C:\Projects\Enlighten\Src\EnlightenAPI\LibSrc\GeoCore/GeoRefCount.h`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3\EnlightenUtils.inl`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3\enlightenoutputbuffer.cpp`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3\impl\../EnlightenLightTransportOutput.h`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3\impl\bakeoutputprobeset.cpp`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3\impl\bakeoutputprobesetvisibility.cpp`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3\impl\clusteringoutputimpl.cpp`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3\impl\lighttransportoutputimpl.cpp`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3\impl\meshsimpatlaschartoutput.cpp`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3\impl\meshsimpchartoutput.cpp`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3\impl\meshsimpinstanceoutput.cpp`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3\impl\meshsimpmeshoutput.cpp`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3\impl\meshsimpoutputimpl.cpp`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3\impl\runtimecharts.cpp`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3hlrt\albedohandler\cpualbedohandler.cpp`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3hlrt\cubemap\../System/BaseSystem.h`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3hlrt\cubemap\BaseCubeMap.h`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3hlrt\cubemap\cpucubemap.cpp`
- `c:\projects\enlighten\src\enlightenapi\libsrc\enlighten3hlrt\dynamicobject\BaseDynamicObject.h`
- ... and 49 more

### Havok (7 files)

- `* E:\Projects\Fallout76\Havok\Source\Common/Base/System/StackTracer/Impl/hkStackTracerWin32.cxx`
- `E:\Projects\Fallout76\Havok\Source\Behavior/Utilities/Utils/hkbProjectAssetManager.inl`
- `E:\Projects\Fallout76\Havok\Source\Common/Base/Monitor/hkMonitorStream.h`
- `E:\Projects\Fallout76\Havok\Source\Common/Internal/GeometryProcessing/Triangulator/hkgpTriangulator.inl`
- `E:\Projects\Fallout76\Havok\Source\Physics/Physics/Collide/Shape/Composite/hknpSparseCompactMap.inl`
- `E:\Projects\Fallout76\Havok\Source\Physics/Physics/Dynamics/Body/hknpBody.inl`
- `E:\Projects\Fallout76\Havok\Source\Physics/Physics/Dynamics/Motion/hknpMotion.inl`

### OpenSSL (2 files)

- `c:\perforce\project76work\sdk\openssl\openssl-1.1.1i\ssl\packet_local.h`
- `e:\buildagent\work\17a4e262df1933f4\project76\idnet\src\openssl\bio.cpp`

### Other (2 files)

- `C:\Program Files\Common Files\SSL/ct_log_list.cnf`
- `SRV*c:\websymbols*http://msdl.microsoft.com/download/symbols;`

### Scaleform (6 files)

- `E:\Projects\Project76\Scaleform\Src\Kernel/SF_Array.h`
- `E:\Projects\Project76\Scaleform\Src\Kernel/SF_Hash.h`
- `e:\buildagent\work\17a4e262df1933f4\project76\scaleform\src\kernel\sf_memory.h`
- `e:\projects\project76\scaleform\src\kernel\SF_Array.h`
- `e:\projects\project76\scaleform\src\kernel\SF_Hash.h`
- `e:\projects\project76\scaleform\src\kernel\SF_RefCount.h`

## Class::Method References (Function Names)

Found **1,354** Class::Method references in embedded strings.
These come from error messages, log strings, and assert macros.

### Classes with Most Method References

| Class | Methods | Examples |
|-------|--------:|---------|
| `UnitTest` | 74 | AfterReflect, AfterReflectWrapper1, AfterReflectWrapper2, AlignTest0, AlignTest1 ... +69 |
| `hkReflect` | 37 | Any, ArrayType, ArrayVar, BoolType, BoolVar ... +32 |
| `UnitTestClang` | 43 | Abstract1, Abstract2, Abstract3, Abstract4, AfterReflect ... +38 |
| `bnet` | 18 | Account, Catalog, Entitlements, Friends, Fulfillment ... +13 |
| `Athena` | 27 | CloseAthenaCharacterMenu, CloseAthenaDetailsModal, CloseAthenaMenu, CloseAthenaUnlinkMenu, CloseEditAthenaMenu ... +22 |
| `WorldData` | 27 | JoinInvalidWorld, JoinNormalWorld, JoinOpenCustom, JoinPrivateNormal, JoinPublicCustom ... +22 |
| `SeasonMenu` | 25 | BattlePassUpsellEndEvent, BattlePassUpsellStartEvent, ClaimAllEvent, ClaimEvent, ClaimTimeEndEvent ... +20 |
| `VarTest` | 16 | Bar, CustomMethods, Empty, Foo, ImplicitMethods ... +11 |
| `HAL` | 15 | BeginFrame, BeginScene, ClearSolidRectangle, DrawProcessedComplexMeshes, DrawProcessedPrimitive ... +10 |
| `hclObjectSpaceDeformer` | 16 | EightBlendEntryBlock, FiveBlendEntryBlock, FourBlendEntryBlock, LocalBlockP, LocalBlockPN ... +11 |
| `idTCP` | 5 | Accept, Connect, Listen, Read, Write |
| `hkbStateMachine` | 12 | ActiveTransitionInfo, DelayedTransitionInfo, EventPropertyArray, NestedStateMachineData, ProspectiveTransitionInfo ... +7 |
| `hkcdDynamicTree` | 12 | AnisotropicMetric, BalanceMetric, CentroidMetric, Codec18, Codec32 ... +7 |
| `hclBoneSpaceDeformer` | 12 | FourBlendEntryBlock, LocalBlockP, LocalBlockPN, LocalBlockPNT, LocalBlockPNTB ... +7 |
| `HUD` | 12 | ChangeAppearance, ClearCompletionRewardsFlag, DiscardFanfare, ListenForQuestAccept, ListenForQuestTrack ... +7 |
| `NewPipBoyMenu` | 12 | ClearQuestInstance, OnQuestSelection, PageCycle, PageSet, PlaySmallTransition ... +7 |
| `INV` | 11 | Drop, Fav, Inspect, SelectionChange, Sort ... +6 |
| `SecureTrade` | 11 | CancelRequestItem, CreateOffer, DeclineItem, DeclineItemOpen, ExitMenu ... +6 |
| `StoreMenu` | 11 | AccountUpgradesStoreOpen, CategoryChanged, ChromiumBrowserClosed, CloseMenu, EquipUnequip ... +6 |
| `castTest` | 10 | Interface0, Interface1, Interface2, InterfaceBase, InterfaceOtherBase ... +5 |
| `hkcdStaticMeshTreeBase` | 6 | Connectivity, Edge, Links, Primitive, PrimitiveDataRunBase ... +1 |
| `HLRT` | 10 | CubeMapSolveTask, DynamicObjectInterpolation, DynamicObjectInterpolationTask, Housekeeping, InputLighting ... +5 |
| `hclVirtualCollisionPointsData` | 9 | BarycentricDictionaryEntry, BarycentricPair, Block, EdgeFan, EdgeFanLandscape ... +4 |
| `SplashMenu` | 9 | Close, CloseZeus, GotoBrowser, GotoSeasons, GotoStore ... +4 |
| `BestBuilds` | 8 | OpenModalBestBuild, PreviewBestBuild, ProcessedBuildFlyout, ReportBestBuild, ToggleBestBuildLike ... +3 |
| `CampSlots` | 8 | ActivateEvent, FastTravelEvent, ManageBestBuildEvent, OpenStoreEvent, RenameEvent ... +3 |
| `SocialData` | 8 | ChangePublicTeamType, CloseMenu, CreatePublicTeam, FriendRequestResponse, JoinPublicTeam ... +3 |
| `SpecialBuilds` | 8 | CloseMenu, EditActivePerks, LoadBuild, RenameBuild, ResetBuild ... +3 |
| `WorkshopMenu` | 8 | CategorySelect, ChangeSubMode, Hide, ServerSpinnerUpdated, ToggleFilter ... +3 |
| `Container` | 7 | InspectItem, RefreshStash, TakeAll, TransferAid, TransferItem ... +2 |
| `Expeditions` | 7 | Blocked, Exit, JoinExpedition, LaunchExpedition, ResumeExpedition ... +2 |
| `hkcdStaticTree` | 7 | Codec3Axis, Codec3Axis4, Codec3Axis5, Codec3Axis6, CodecRaw ... +2 |
| `CharacterSelection` | 6 | DemandImage, ImageLoad, ImageUnload, MenuClose, MenuOpen ... +1 |
| `ExternalPurchaseMenu` | 6 | BulkPurchase, CancelPurchase, Failure, GotoAtoms, GotoStore ... +1 |
| `hclSimClothData` | 6 | CollidablePinchingData, CollidableTransformMap, LandscapeCollisionData, OverridableSimulationInfo, ParticleData ... +1 |
| `MapMenu` | 6 | GotoChallengesMenuEvent, MarkerSelectionChange, MarkerSelectionEvent, ShowQuestInPipBoy, ToggleMarkerTracked ... +1 |
| `PhotoGalleryMenu` | 6 | DeletePhoto, DemandImage, HideMenu, MakeProfilePhoto, RegisterImage ... +1 |
| `PurchaseRank` | 6 | BulkPurchaseBegin, BulkPurchaseComplete, Close, ConfirmationFailure, ConfirmationSuccess ... +1 |
| `Scaleform` | 1 | Render |
| `TthkSerialize` | 2 | Load, Save |

## Key Classes for Address Library / Modding

### PlayerCharacter
- `BasePlayerCharacter` [class] (Other)
- `LocalPlayerCharacter` [class] (Other)
- `RemotePlayerCharacter` [class] (Other)

### Actor
- `?A0xc3c4fcbb::ActorItemEquippedToMiscStatHandler` [struct] (Actor/Character)
- `ActorServerAuthSnapshotData` [struct] (Actor/Character)
- `ActorValuesSnapshotComponent::ActorValuesSnapshotData` [struct] (Actor/Character)
- `H::VActor::ActorBoneWeightsActionChannel` [class] (Actor/Character)
- `M::VActor::ActorCCNormDotUpChannel` [class] (Actor/Character)
- `_N::VActor::ActorCCOnStairsChannel` [class] (Actor/Character)
- `_N::VActor::ActorCCSuportChannel` [class] (Actor/Character)
- `H::VActor::ActorCopyGraphVariableChannel` [class] (Actor/Character)
- `M::VActor::ActorCopyGraphVariableChannel` [class] (Actor/Character)
- `M::VActor::ActorDirectionChannel` [class] (Actor/Character)

### TESObjectREFR
- `TESObjectREFRServerAuthSnapshotData` [struct] (TES (Engine))
- `TESObjectREFR` [class] (TES (Engine))
- `TESObjectREFRCoreSnapshotComponent` [class] (TES (Engine))
- `TESObjectREFR_EventsWrapper` [class] (TES (Engine))
- `?A0x1e0766f5::TESObjectREFRFactory` [class] (TES (Engine))
- `TESObjectREFRPhysicsSnapshotComponent` [class] (TES (Engine))
- `TESObjectREFRQuestItemSnapshotComponent` [class] (TES (Engine))
- `TESObjectREFRScriptObjectSnapshotComponent` [class] (TES (Engine))
- `TESObjectREFRTransformSnapshotComponent` [class] (TES (Engine))

### TESForm
- `TESForm` [class] (TES (Engine))
- `TESFormUIData` [class] (TES (Engine))

### VirtualMachine
- `BSScript::IVirtualMachine` [class] (BSScript)
- `BSScript::Internal::VirtualMachine` [class] (BSScript)

### GameVM
- `GameVM` [class] (Other)

### TESQuest
- `TESQuest` [class] (TES (Engine))
- `TESQuestInstance` [class] (TES (Engine))

### BGSStoryManagerBranchNode
- `BGSStoryManagerBranchNode` [class] (BGS (Game))

### TESObjectCELL
- `?A0x38100c62::$0FD::VTESObjectCELL::TESObjectCELLConcreteFormFactory` [class] (TES (Engine))
- `TESObjectCELL` [class] (TES (Engine))
- `TESObjectCELLWeakPtr` [class] (TES (Engine))

### TESWorldSpace
- `TESWorldSpace` [class] (TES (Engine))

### BGSKeyword
- `BGSKeyword` [class] (BGS (Game))
- `BGSKeywordForm` [class] (BGS (Game))

### BGSMessage
- `BGSMessage` [class] (BGS (Game))
- `logging::BGSMessageHandlerDebugOutput` [class] (BGS (Game))
- `logging::BGSMessageHandlerOutput` [class] (BGS (Game))
- `BGSMessageIcon` [class] (BGS (Game))

### BGSLocation
- `BGSLocation` [class] (BGS (Game))
- `BGSLocationRefType` [class] (BGS (Game))

### ActorValueInfo
- `ActorValueInfo` [class] (Actor/Character)

### ActorValueOwner
- `ActorValueOwner` [class] (Actor/Character)

### BSInputDevice
- `BSInputDevice` [class] (BS (Input/Platform))

### NiNode
- `BSFaceGenNiNode` [class] (BS (Core))
- `BSNiNode` [class] (BS (Core))
- `NiNode` [class] (NetImmerse/Gamebryo)

### NiAVObject
- `NiAVObject` [class] (NetImmerse/Gamebryo)
- `NiAVObjectPalette` [class] (NetImmerse/Gamebryo)

### NiObject
- `NiObject` [class] (NetImmerse/Gamebryo)
- `NiObjectNET` [class] (NetImmerse/Gamebryo)

### bhkWorld
- `bhkWorld` [class] (Havok (Behavior))
- `bhkWorldM` [class] (Havok (Behavior))

## BS* (Bethesda Core) Prefix Breakdown

| Prefix | Count |
|--------|------:|
| `BS(other)` | 6638 |
| `BSExtra` | 236 |
| `BSImagespace` | 166 |
| `BSCounted` | 21 |
| `BSPathing` | 18 |
| `BSLighting` | 14 |
| `BSNavmesh` | 13 |
| `BSScaleform` | 13 |
| `BSAuto` | 12 |
| `BSQueued` | 11 |
| `BSFace` | 11 |
| `BSMulti` | 10 |
| `BSShader` | 10 |
| `BSTemp` | 7 |
| `BSPathfinding` | 6 |
| `BSParticle` | 6 |
| `BSAudio` | 5 |
| `BSEffect` | 5 |
| `BSGeometry` | 5 |
| `BSInput` | 5 |
| `BSLimb` | 5 |
| `BSAnimation` | 4 |
| `BSBone` | 4 |
| `BSChromium` | 4 |
| `BSLook` | 4 |
| `BSPath` | 4 |
| `BSPortal` | 4 |
| `BSResource` | 4 |
| `BSShadow` | 4 |
| `BSSystem` | 4 |

## TES* (Engine) Classes

Found **123** TES-prefixed classes:

- `TES` [class]
- `TESAIForm` [class]
- `TESActionData` [class]
- `TESActorBase` [class]
- `TESActorBaseData` [class]
- `TESAmmo` [class]
- `TESAsyncConditionEvaluator` [class]
- `TESAttackDamageForm` [class]
- `?A0x367991da::TESAudioInitialLoadListener` [class]
- `TESBipedModelForm` [class]
- `TESBoundAnimObject` [class]
- `TESBoundObject` [class]
- `TESCamera` [class]
- `TESCameraState` [class]
- `TESChildCell` [class]
- `TESClass` [class]
- `TESClimate` [class]
- `TESCombatStyle` [class]
- `TESContainer` [class]
- `TESCustomPackageData` [class]
- `TESDataHandler` [class]
- `TESDataHandlerPostBuildFileListSource` [class]
- `TESDescription` [class]
- `TESDescriptionReplaceTagsFuncBase` [class]
- `TESDialoguePackageData` [class]
- `TESEffectShader` [class]
- `TESEnchantableForm` [class]
- `UActionRefKey::TESEvaluationCache` [class]
- `TESEvaluationCacheBase` [class]
- `TESEyes` [class]
- `TESFaction` [class]
- `TESFlora` [class]
- `TESFollowPackageData` [class]
- `TESForm` [class]
- `TESFormUIData` [class]
- `TESFullName` [class]
- `TESFurniture` [class]
- `TESGlobal` [class]
- `TESGrass` [class]
- `TESHealthForm` [class]
- `TESIcon` [class]
- `TESIdleForm` [class]
- `TESImageSpace` [class]
- `$03::TESImageSpaceModifiableCountForm` [class]
- `TESImageSpaceModifiableForm` [class]
- `TESImageSpaceModifier` [class]
- `TESKey` [class]
- `TESLandTexture` [class]
- `TESLevCharacter` [class]
- `TESLevItem` [class]
- `TESLeveledList` [class]
- `TESLoadScreen` [class]
- `TESMagicCasterForm` [class]
- `TESMagicTargetForm` [class]
- `TESModel` [class]
- `AnimationSystemUtils::TESModelAndAnimationHandles` [class]
- `TESModelTri` [class]
- `TESNPC` [class]
- `TESObject` [class]
- `TESObjectACTI` [class]
- `TESObjectANIO` [class]
- `TESObjectARMA` [class]
- `TESObjectARMO` [class]
- `TESObjectBOOK` [class]
- `TESObjectCELL` [class]
- `?A0x38100c62::$0FD::VTESObjectCELL::TESObjectCELLConcreteFormFactory` [class]
- `TESObjectCELLWeakPtr` [class]
- `TESObjectCONT` [class]
- `TESObjectDOOR` [class]
- `TESObjectLIGH` [class]
- `TESObjectMISC` [class]
- `TESObjectREFR` [class]
- `TESObjectREFRCoreSnapshotComponent` [class]
- `?A0x1e0766f5::TESObjectREFRFactory` [class]
- `TESObjectREFRPhysicsSnapshotComponent` [class]
- `TESObjectREFRQuestItemSnapshotComponent` [class]
- `TESObjectREFRScriptObjectSnapshotComponent` [class]
- `TESObjectREFRServerAuthSnapshotData` [struct]
- `TESObjectREFRTransformSnapshotComponent` [class]
- `TESObjectREFR_EventsWrapper` [class]
- `TESObjectSTAT` [class]
- `TESObjectTREE` [class]
- `TESObjectWEAP` [class]
- `TESPackage` [class]
- `TESPackageData` [class]
- `TESModelDB::?A0x58ba151d::TESProcessor` [class]
- `TESProduceForm` [class]
- `TESQuest` [class]
- `TESQuestInstance` [class]
- `TESModelDB::TESQueuedHandles` [class]
- `TESRace` [class]
- `TESRaceForm` [class]
- `TESReactionForm` [class]
- `TESRegion` [class]
- `TESRegionData` [class]
- `TESRegionDataManager` [class]
- `TESRegionDataMap` [class]
- `TESRegionDataObjects` [class]
- `TESRegionDataSound` [class]
- `TESRegionDataWeather` [class]
- `TESRegionDataWorkshop` [class]
- `TESRegionList` [class]
- `TESRegionNoiseFunction` [class]
- `TESRegionObject` [class]
- `TESRegionObjectBase` [class]
- `TESRegionObjectList` [class]
- `TESSound` [class]
- `TESSpellList` [class]
- `TESTexture` [class]
- `TESTopic` [class]
- `TESTopicInfo` [class]
- `TESTrap` [class]
- `TESTrapListener` [class]
- `TESUtilityItem` [class]
- `TESValueForm` [class]
- `TESWaterDisplacement` [class]
- `TESWaterForm` [class]
- `TESWaterNormals` [class]
- `TESWaterObject` [class]
- `TESWaterReflections` [class]
- `TESWeather` [class]
- `TESWeightForm` [class]
- `TESWorldSpace` [class]

## BGS* (Bethesda Game Studio) Classes

Found **484** BGS-prefixed classes:

- `BGSAIWorldLocation` [class]
- `BGSAIWorldLocationInteriorCell` [class]
- `BGSAIWorldLocationPointRadius` [class]
- `BGSAIWorldLocationPrimitive` [class]
- `BGSAIWorldLocationRefRadius` [class]
- `BGSATXDefaultObject` [class]
- `BGSAbilityPerkEntry` [class]
- `BGSAcousticSpace` [class]
- `BGSAction` [class]
- `BGSActionData` [class]
- `BGSAddonNode` [class]
- `BGSAddonNodeSoundHandleExtra` [class]
- `BGSAimAssistModel` [class]
- `BGSAimAssistPoseData` [class]
- `BGSAimModel` [class]
- `BGSArtObject` [class]
- `BGSArtObjectCloneTask` [class]
- `BGSAssociationType` [class]
- `BGSAttachParentArray` [class]
- `BGSAttackData` [class]
- `BGSAttackDataForm` [class]
- `BGSAttackDataMap` [class]
- `BGSAttractionRule` [class]
- `BGSAudioEffectChain` [class]
- `BGSAutoWeaponSoundDef` [class]
- `BGSAvatar` [class]
- `BGSBaseAlias` [class]
- `BGSBehaviorGraphModel` [class]
- `BGSBendableSpline` [class]
- `BGSBipedObjectForm` [class]
- `BGSBlockBashData` [class]
- `BGSBody` [class]
- `BGSBodyPartData` [class]
- `BGSCameraPath` [class]
- `BGSCameraShot` [class]
- `BGSCampIcon` [class]
- `BGSCampTitle` [class]
- `BGSChallenge` [class]
- `BGSChallengePassRewardData` [class]
- `BGSChargenUtils` [class]
- `BGSCollisionLayer` [class]
- `BGSColorForm` [class]
- `BGSComponent` [class]
- `$00::VBGSStaticCollection::VBGSLodOwnerComponent::BGSComponentOwnerInterface` [class]
- `$00::VTESObjectACTI::VBGSLodOwnerComponent::BGSComponentOwnerInterface` [class]
- `$00::VTESObjectSTAT::VBGSLodOwnerComponent::BGSComponentOwnerInterface` [class]
- `BGSCompoundSoundDef` [class]
- `BGSConditionForm` [class]
- `BGSConstructibleObject` [class]
- `BGSConsumableEntitlement` [class]
- `BGSCraftingUseSound` [class]
- `BGSCrateServiceEntitlement` [class]
- `BGSCurveTableForm` [class]
- `BGSDailyContentGroup` [class]
- `BGSDamageType` [class]
- `BGSDebris` [class]
- `BGSDecalNode` [class]
- `BGSDefaultObject` [class]
- `BGSDefaultObjectManager` [class]
- `BGSDestructibleObjectForm` [class]
- `BGSDialogueBranch` [class]
- `BGSDistrict` [class]
- `BGSDualCastData` [class]
- `BGSEchoListener` [class]
- `BGSEmote` [class]
- `BGSEmoteCategory` [class]
- `BGSEntitlement` [class]
- `BGSEntryPointFunctionData` [class]
- `BGSEntryPointFunctionDataAVAndValue` [class]
- `BGSEntryPointFunctionDataActivateChoice` [class]
- `BGSEntryPointFunctionDataBooleanGraphVariable` [class]
- `BGSEntryPointFunctionDataItem` [class]
- `BGSEntryPointFunctionDataLeveledList` [class]
- `BGSEntryPointFunctionDataOneValue` [class]
- `BGSEntryPointFunctionDataSpellItem` [class]
- `BGSEntryPointFunctionDataText` [class]
- `BGSEntryPointFunctionDataTwoValue` [class]
- `BGSEntryPointPerkEntry` [class]
- `BGSEquipSlot` [class]
- `BGSEquipType` [class]
- `BGSEquipableObjectInstanceData` [class]
- `BGSEventPlaylist` [class]
- `BGSEventQuestWidget` [class]
- `BGSExplosion` [class]
- `BGSFeaturedItemMessage` [class]
- `BGSFish` [class]
- `BGSFootIkRaycastInterfaceDB` [class]
- `BGSFootstep` [class]
- `BGSFootstepManager` [class]
- `BGSFootstepSet` [class]
- `BGSForcedLocRefType` [class]
- `BGSGamebryoSequenceGenerator` [class]
- `BGSGamebryoSequenceGeneratorHolderSingleton` [class]
- `BGSGameplayReward` [class]
- `BGSGroundCover` [class]
- `BGSHavokGeometryAttach` [class]
- `BGSHazard` [class]
- `BGSHeadPart` [class]
- `BGSIdleCollection` [class]
- `BGSIdleMarker` [class]
- `BGSImpactData` [class]
- `BGSImpactDataSet` [class]
- `BGSImpactManager` [class]
- `BGSInstanceNamingRules` [class]
- `BGSInstanceNamingRulesForm` [class]
- `BGSInventoryInterface` [class]
- `BGSInventoryList` [class]
- `BGSItemBreakageSound` [class]
- `BGSJSONFileForm` [class]
- `BGSKeyword` [class]
- `BGSKeywordForm` [class]
- `BGSLOSData` [class]
- `BGSLegendaryItem` [class]
- `BGSLensFlare` [class]
- `BGSLensFlareSprite` [class]
- `BGSLevPackIn` [class]
- `BGSLevPerkCard` [class]
- `BGSLightingTemplate` [class]
- `BGSListForm` [class]
- `BGSLoadFormBuffer` [class]
- `BGSLoadFormData` [class]
- `BGSLoadGameBuffer` [class]
- `BGSLoadout` [class]
- `BGSLocAlias` [class]
- `BGSLocation` [class]
- `BGSLocationRefType` [class]
- `BGSLodOwnerComponent` [class]
- `BGSMaterialObject` [class]
- `BGSMaterialSwap` [class]
- `BGSMaterialType` [class]
- `BGSMenuDisplayObject` [class]
- `BGSMessage` [class]
- `logging::BGSMessageHandlerDebugOutput` [class]
- `logging::BGSMessageHandlerOutput` [class]
- `BGSMessageIcon` [class]
- `BGSModelMaterialSwap` [class]
- `BGSModelSwap` [class]
- `BGSMovableStatic` [class]
- `BGSMovementType` [class]
- `BGSMoviePlayer` [class]
- `BGSMultiTechniqueAttach` [class]
- `BGSMusicPaletteTrack` [class]
- `BGSMusicSilenceTrack` [class]
- `BGSMusicSingleTrack` [class]
- `BGSMusicTrack` [class]
- `BGSMusicTrackFormWrapper` [class]
- `BGSMusicType` [class]
- `BGSNamedNodeAttach` [class]
- `VIAITarget::BGSNamedPackageData` [class]
- `VIPackageData::BGSNamedPackageData` [class]
- `VIPackageDataAIWorldLocationHandle::BGSNamedPackageData` [class]
- `BGSNativeTerminalForm` [class]
- `BGSNavmeshableObject` [class]
- `BGSNote` [class]
- `BGSObjectInstanceExtra` [class]
- `BGSObjectPlacementDefaults` [class]
- `BGSObjectVisibilityManager` [class]
- `BGSOpenCloseForm` [class]
- `BGSOutfit` [class]
- `BGSOverridePackCollection` [class]
- `BGSOwnerAwarenessComponent` [class]
- `BGSPackIn` [class]
- `B$0A::3VBSFixedString::$1?kPackageDataRefTypeName::$0M::$0BD::V?$BSUntypedPointerHandle::VTESObjectREFR::V?$BSPointerHandle::VIAITarget::BGSPackageDataBasicTemplate` [class]
- `3HB::B$1?iPackageDataIntDefault::3VBSFixedString::H$1?kPackageDataIntTypeName::VIPackageData::BGSPackageDataBasicTemplate` [class]
- `3MB::B$1?fPackageDataFloatDefault::3VBSFixedString::M$1?kPackageDataFloatTypeName::VIPackageData::BGSPackageDataBasicTemplate` [class]
- `BGSPackageDataBool` [class]
- `BGSPackageDataFloat` [class]
- `BGSPackageDataInt` [class]
- `BGSPackageDataLocation` [class]
- `BGSPackageDataLocationWrapper` [class]
- `BGSPackageDataObjectList` [class]
- `B::3VBSFixedString::$1?kPackageDataRef2TypeName::VPackageTarget::VIAITarget::BGSPackageDataPointerTemplate` [class]
- `B::3VBSFixedString::$1?kPackageDataLocationTypeName::VPackageLocation::VIPackageDataAIWorldLocationHandle::BGSPackageDataPointerTemplate` [class]
- `B::3VBSFixedString::$1?kPackageDataTargetSelectorTypeName::VPackageTarget::VIPackageData::BGSPackageDataPointerTemplate` [class]
- `BGSPackageDataRef` [class]
- `BGSPackageDataRefOLD` [class]
- `3HB::B$1?iPackageDataIntDefault::3VBSFixedString::H$1?kPackageDataIntTypeName::VIPackageData::BGSPackageDataSaveableTemplate` [class]
- `3MB::B$1?fPackageDataFloatDefault::3VBSFixedString::M$1?kPackageDataFloatTypeName::VIPackageData::BGSPackageDataSaveableTemplate` [class]
- `BGSPackageDataTargetSelector` [class]
- `BGSPackageDataTopic` [class]
- `V1::VBGSPackageDataBool::BGSPackageDataTypeCheck` [class]
- `V1::VBGSPackageDataFloat::BGSPackageDataTypeCheck` [class]
- `V1::VBGSPackageDataInt::BGSPackageDataTypeCheck` [class]
- `V1::VBGSPackageDataObjectList::BGSPackageDataTypeCheck` [class]
- `V1::VBGSPackageDataTargetSelector::BGSPackageDataTypeCheck` [class]
- `V1::VBGSPackageDataTopic::BGSPackageDataTypeCheck` [class]
- `VBGSPackageDataObjectList::VIAITarget::BGSPackageDataTypeCheck` [class]
- `VBGSPackageDataRef::VIAITarget::BGSPackageDataTypeCheck` [class]
- `VBGSPackageDataLocation::VIPackageDataAIWorldLocationHandle::BGSPackageDataTypeCheck` [class]
- `VBGSPackageDataRef::VIPackageDataAIWorldLocationHandle::BGSPackageDataTypeCheck` [class]
- `BGSPairedPrimitive` [class]
- `BGSParticleArrayAttach` [class]
- `BGSParticleObjectCloneTask` [class]
- `BGSPerk` [class]
- `BGSPerkCard` [class]
- `BGSPerkCardPack` [class]
- `BGSPerkEntry` [class]
- `BGSPerkRankArray` [class]
- `BGSPhotoModeFeature` [class]
- `BGSPickupPutdownSounds` [class]
- `BGSPlayerMusicChanger` [class]
- `BGSPlayerTitle` [class]
- `BGSPowerArmorChassis` [class]
- `BGSPreloadable` [class]
- `BGSPreviewTransform` [class]
- `BGSPrimitive` [class]
- `BGSPrimitiveBox` [class]
- `BGSPrimitiveCylinder` [class]
- `BGSPrimitiveEllipsoid` [class]
- `BGSPrimitiveLine` [class]
- `BGSPrimitivePlane` [class]
- `BGSPrimitiveSphere` [class]
- `BGSPriorityAttackableObject` [class]
- `BGSProcedureAcquire` [class]
- `BGSProcedureAcquireExecState` [class]
- `BGSProcedureActivate` [class]
- `BGSProcedureActivateExecState` [class]
- `BGSProcedureBase` [class]
- `BGSProcedureDialogue` [class]
- `BGSProcedureDialogueActivate` [class]
- `BGSProcedureDialogueActivateExecState` [class]
- `BGSProcedureDialogueExecState` [class]
- `BGSProcedureDone` [class]
- `BGSProcedureDoneExecState` [class]
- `BGSProcedureEat` [class]
- `BGSProcedureEatExecState` [class]
- `BGSProcedureEscort` [class]
- `BGSProcedureEscortExecState` [class]
- `BGSProcedureFind` [class]
- `BGSProcedureFindByLinkChain` [class]
- `BGSProcedureFindByLinkChainExecState` [class]
- `BGSProcedureFindExecState` [class]
- `BGSProcedureFlee` [class]
- `BGSProcedureFleeExecState` [class]
- `BGSProcedureFlightGrab` [class]
- `BGSProcedureFlightGrabExecState` [class]
- `BGSProcedureFollow` [class]
- `BGSProcedureFollowExecState` [class]
- `BGSProcedureFollowTo` [class]
- `BGSProcedureForceGreet` [class]
- `BGSProcedureGuard` [class]
- `BGSProcedureGuardArea` [class]
- `BGSProcedureGuardExecState` [class]
- `BGSProcedureHeadtrack` [class]
- `BGSProcedureHeadtrackExecState` [class]
- `BGSProcedureHoldPosition` [class]
- `BGSProcedureHoldPositionExecState` [class]
- `BGSProcedureHover` [class]
- `BGSProcedureHoverExecState` [class]
- `BGSProcedureKeepAnEyeOn` [class]
- `BGSProcedureKeepAnEyeOnExecState` [class]
- `BGSProcedureLock` [class]
- `BGSProcedureLockUnlockExecState` [class]
- `BGSProcedureOrbit` [class]
- `BGSProcedureOrbitExecState` [class]
- `BGSProcedurePatrol` [class]
- `BGSProcedurePatrolExecState` [class]
- `BGSProcedurePlayIdle` [class]
- `BGSProcedurePlayIdleExecState` [class]
- `BGSProcedurePursue` [class]
- `BGSProcedureRange` [class]
- `BGSProcedureRangeExecState` [class]
- `BGSProcedureSandbox` [class]
- `BGSProcedureSandboxExecState` [class]
- `BGSProcedureSay` [class]
- `BGSProcedureSayExecState` [class]
- `BGSProcedureSit` [class]
- `BGSProcedureSitSleepExecState` [class]
- `BGSProcedureSleep` [class]
- `BGSProcedureStayAway` [class]
- `BGSProcedureStayAwayExecState` [class]
- `BGSProcedureTravel` [class]
- `BGSProcedureTravelExecState` [class]
- `BGSProcedureTreeBranch` [class]
- `BGSProcedureTreeConditionalItem` [class]
- `BGSProcedureTreeFallback` [class]
- `BGSProcedureTreeFallbackExecState` [class]
- `BGSProcedureTreeOneChildExecState` [class]
- `BGSProcedureTreeProcedure` [class]
- `BGSProcedureTreeRandom` [class]
- `BGSProcedureTreeRandomExecState` [class]
- `BGSProcedureTreeSequence` [class]
- `BGSProcedureTreeSequenceExecState` [class]
- `BGSProcedureTreeSimultaneous` [class]
- `BGSProcedureTreeSimultaneousExecState` [class]
- `BGSProcedureTreeStacked` [class]
- `BGSProcedureTreeStackedExecState` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureAcquireParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureActivateParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureDialogueActivateParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureDialogueParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureDoneParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureEatParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureEscortParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureFindByLinkChainParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureFindParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureFleeParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureFlightGrabParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureFollowParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureFollowToParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureForceGreetParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureGuardAreaParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureGuardParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureHeadtrackParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureHoldPositionParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureHoverParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureKeepAnEyeOnParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureLockParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureOrbitParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedurePatrolParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedurePlayIdleParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedurePursueParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureRangeParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureSandboxParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureSayParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureSitParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureSleepParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureStayAwayParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureTravelParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureUnlockParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureUseIdleMarkerParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureUseMagicParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureUseWeaponParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureWaitParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `B::3QBUBGSProcedureParamInfo::$1?kProcedureWanderParamTypes::VBGSProcedureBase::BGSProcedureTyped` [class]
- `BGSProcedureUnlock` [class]
- `BGSProcedureUseIdleMarker` [class]
- `BGSProcedureUseIdleMarkerExecState` [class]
- `BGSProcedureUseMagic` [class]
- `BGSProcedureUseMagicExecState` [class]
- `BGSProcedureUseWeapon` [class]
- `BGSProcedureUseWeaponExecState` [class]
- `BGSProcedureWait` [class]
- `BGSProcedureWaitExecState` [class]
- `BGSProcedureWander` [class]
- `BGSProcedureWanderExecState` [class]
- `BGSProjectile` [class]
- `BGSPropertySheet` [class]
- `BGSQuestModule` [class]
- `BGSQuestObjectiveTimingsMsg` [struct]
- `BGSQuestText` [class]
- `BGSQueuedGrassModelHandles` [class]
- `BGSQueuedObjectDowngrade` [class]
- `BGSQueuedObjectInitialLoad` [class]
- `BGSQueuedObjectUpgrade` [class]
- `BGSQueuedTerrainDowngrade` [class]
- `BGSQueuedTerrainInitialLoad` [class]
- `BGSQueuedTerrainUpdate` [class]
- `BGSQueuedTerrainUpgrade` [class]
- `BGSRefAlias` [class]
- `BGSRefCollectionAlias` [class]
- `BGSReferenceEffect` [class]
- `BGSReferenceGroup` [class]
- `BGSRelationship` [class]
- `BGSRequiredEntitlementForm` [class]
- `BGSResource` [class]
- `BGSRetargetOnDeleteExtraData` [class]
- `BGSReverbParameters` [class]
- `BGSSWFImageForm` [class]
- `BGSSaveFormBuffer` [class]
- `BGSSaveGameBuffer` [class]
- `BGSSaveLoadManager` [class]
- `BGSSaveLoadStatsMap` [class]
- `BGSSaveLoadThread` [class]
- `BGSScene` [class]
- `BGSSceneAction` [class]
- `BGSSceneActionConversationBase` [class]
- `BGSSceneActionConversationBaseInstance` [class]
- `BGSSceneActionDialogue` [class]
- `BGSSceneActionDialogueInstance` [class]
- `BGSSceneActionInstance` [class]
- `BGSSceneActionNPCResponseDialogue` [class]
- `BGSSceneActionNPCResponseDialogueInstance` [class]
- `BGSSceneActionPackage` [class]
- `BGSSceneActionPackageInstance` [class]
- `BGSSceneActionPlayerDialogue` [class]
- `BGSSceneActionPlayerDialogueInstance` [class]
- `BGSSceneActionRadio` [class]
- `BGSSceneActionRadioInstance` [class]
- `BGSSceneActionStartScene` [class]
- `BGSSceneActionStartSceneInstance` [class]
- `BGSSceneActionTimer` [class]
- `BGSSceneActionTimerInstance` [class]
- `BGSSeasonRewardTile` [class]
- `BGSShaderParticleGeometryData` [class]
- `BGSSkinForm` [class]
- `BGSSnapTemplate` [class]
- `BGSSnapTemplateComponent` [class]
- `BGSSnapTemplateNode` [class]
- `BGSSoundCategory` [class]
- `BGSSoundCategorySnapshot` [class]
- `BGSSoundDescriptor` [class]
- `BGSSoundDescriptorForm` [class]
- `BGSSoundEcho` [class]
- `BGSSoundKeywordMapping` [class]
- `BGSSoundOutput` [class]
- `BGSSoundTagComponent` [class]
- `BGSSoundTagSet` [class]
- `BGSSpellThresholdData` [class]
- `BGSStandardSoundDef` [class]
- `BGSStaticCollection` [class]
- `BGSStoryHelper` [class]
- `BGSStoryManager` [class]
- `BGSStoryManagerBranchNode` [class]
- `BGSStoryManagerEventNode` [class]
- `BGSStoryManagerNodeBase` [class]
- `BGSStoryManagerQuestFinder` [class]
- `BGSStoryManagerQuestNode` [class]
- `BGSStoryManagerTreeForm` [class]
- `BGSStoryManagerTreeVisitor` [class]
- `BGSStoryTeller` [class]
- `BGSSynchronizedAnimationInstance` [class]
- `BGSSynchronizedAnimationManager` [class]
- `BGSTalkingActivator` [class]
- `BGSTerminal` [class]
- `BGSTextureModel` [class]
- `BGSTextureSet` [class]
- `BGSTextureSet::BGSTextureSetImpl` [class]
- `BGSTitle` [class]
- `BGSTransform` [class]
- `VBGSAIWorldLocation::VBGSAIWorldLocationInteriorCell::BGSTypedItem` [class]
- `VBGSAIWorldLocation::VBGSAIWorldLocationPointRadius::BGSTypedItem` [class]
- `VBGSAIWorldLocation::VBGSAIWorldLocationPrimitive::BGSTypedItem` [class]
- `VBGSAIWorldLocation::VBGSAIWorldLocationRefRadius::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureAcquireExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureActivateExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureDialogueActivateExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureDialogueExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureDoneExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureEatExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureEscortExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureFindByLinkChainExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureFindExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureFleeExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureFlightGrabExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureFollowExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureGuardExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureHeadtrackExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureHoldPositionExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureHoverExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureKeepAnEyeOnExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureLockUnlockExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureOrbitExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedurePatrolExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedurePlayIdleExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureRangeExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureSandboxExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureSayExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureSitSleepExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureStayAwayExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureTravelExecState::BGSTypedItem` [class]
- `VBGSProcedureTreeOneChildExecState::VBGSProcedureTreeFallbackExecState::BGSTypedItem` [class]
- `VBGSProcedureTreeBranch::VBGSProcedureTreeFallback::BGSTypedItem` [class]
- `VBGSProcedureTreeConditionalItem::VBGSProcedureTreeProcedure::BGSTypedItem` [class]
- `VBGSProcedureTreeOneChildExecState::VBGSProcedureTreeRandomExecState::BGSTypedItem` [class]
- `VBGSProcedureTreeBranch::VBGSProcedureTreeRandom::BGSTypedItem` [class]
- `VBGSProcedureTreeOneChildExecState::VBGSProcedureTreeSequenceExecState::BGSTypedItem` [class]
- `VBGSProcedureTreeBranch::VBGSProcedureTreeSequence::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureTreeSimultaneousExecState::BGSTypedItem` [class]
- `VBGSProcedureTreeBranch::VBGSProcedureTreeSimultaneous::BGSTypedItem` [class]
- `VBGSProcedureTreeOneChildExecState::VBGSProcedureTreeStackedExecState::BGSTypedItem` [class]
- `VBGSProcedureTreeBranch::VBGSProcedureTreeStacked::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureUseIdleMarkerExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureUseMagicExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureUseWeaponExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureWaitExecState::BGSTypedItem` [class]
- `VIProcedureTreeExecState::VBGSProcedureWanderExecState::BGSTypedItem` [class]
- `$01::BGSTypedKeywordValueArray` [class]
- `$03::BGSTypedKeywordValueArray` [class]
- `$04::BGSTypedKeywordValueArray` [class]
- `$08::BGSTypedKeywordValueArray` [class]
- `BGSVisitProceduresCheckGuardWarnTarget` [class]
- `BGSVisitProceduresInitActorLocation` [class]
- `BGSVisitProceduresProcess` [class]
- `BGSVivoxVoiceChat` [class]
- `BGSVoiceChat` [class]
- `BGSVoiceType` [class]
- `BGSVolumetricLighting` [class]
- `BGSWaterCollisionManager::BGSWaterUpdateI` [class]
- `BGSWorkshopPermissions` [class]
- `BGSZoneTargetListener` [class]
- `BGSZoomData` [class]
- `BGShkMatFadeController` [class]
- `BGShkPhonemeController` [class]

## Notable Findings

### Networking Classes (164)

- `Transporting::ActivateClientTeleportDoorMsg`
- `ActiveDuelClientMsg`
- `ActiveDuelServerMsg`
- `ActiveEffectNetworkEntity`
- `ActorServerAuthSnapshotData`
- `AddMusicTypeOnClient`
- `ApplyCategorySnapshotOnClient`
- `AuditClientSharedTitleStorageSettingsMessage`
- `BSChromiumClient`
- `BSGeometryConstructorClient`
- `BSSocket`
- `BSSocketServer`
- `BaseGameNetworkMessage`
- `BaseGameNetworkMessageToClient`
- `BaseGameNetworkMessageToServer`
- `BestBuilds::BestBuildClientMediaUploadResponseMsg`
- `CefClient`
- `MessageBoxNetwork::ClearHelpMessagesOnClient`
- `bps::client::seasonv2::Client`
- `ClientAccountsDataManager`
- `PowerArmor::ClientActiveArmor`
- `ClientAuthBehaviorComponent`
- `ClientAuthPlayerMotionComponent`
- `ClientAuthProjectileComponent`
- `WorkshopHavokUtils::ClientDropProxyCache`
- `ClientHealthDiagnosticsReport1`
- `ClientHealthDiagnosticsReport2`
- `ClientHealthDiagnosticsReport3`
- `ClientLobbyData`
- `ArchiveValidation::ClientManager`
- `?A0x7792840c::ClientNetEntityInterface`
- `ClientPlayerCoreSnapshotComponent`
- `ClientQuestActionRequestMsg`
- `ClientRealtimeMetricsComponent`
- `ClientSNREventUpdated`
- `ClientSpecificCollisionChangeMsg`
- `Transporting::ClientStateMsg`
- `GameScript::ConnectionEventHandler`
- `?A0x7792840c::CoreSocketLogger`
- `CreateChainExplosionMessageServer`
- ... and 124 more

### Workshop/CAMP Classes (50)

- `BGSWorkshopPermissions`
- `CombatTargetSelectorWorkshopObject`
- `WorkshopUI::ConfirmContestWorkshopCallback`
- `WorkshopNetwork::ContestWorkshopMessage`
- `Workshop::ExtraWorkshopPackin`
- `ExtraWorkshopResourceCapacities`
- `HUDWorkshopMarkers`
- `BSEnlighten::IWorkshopManager`
- `NewWorkshop::IWorkshopMode`
- `ExamineConfirmMenu::InitDataWorkshopRepairAll`
- `ExamineConfirmMenu::InitDataWorkshopRepairFailure`
- `ExamineConfirmMenu::InitDataWorkshopScrapAllFailure`
- `NewWorkshop::NewWorkshopMenu`
- `PipboyWorkshopData`
- `PipboyWorkshopMenu`
- `GameScript::PlayerWorkshopEventHandler`
- `WorkshopNetwork::RequestWorkshopBudgetReportMessage`
- `ShelterWorkshopProxyListener`
- `TESRegionDataWorkshop`
- `NewWorkshop::WorkshopBuildMode`
- `WorkshopChangeSubMode`
- `WorkshopEventClose`
- `WorkshopHavokUtils::WorkshopFreeCameraHitCollector`
- `WorkshopFreeCameraState`
- `WorkshopHavokUtils::WorkshopGroundCollector`
- `NewWorkshop::WorkshopItemNodeManager`
- `WorkshopListener`
- `BSEnlighten::WorkshopManagerImpl`
- `WorkshopMenuCategorySelect`
- `nsInventory3DManager::WorkshopMenuItemLoadTask`
- `WorkshopNetwork::WorkshopModeMessage`
- `WorkshopNetwork::WorkshopModeReceiptMessage`
- `NewWorkshop::WorkshopModifyMode`
- `NewWorkshop::WorkshopNullMode`
- `Workshop::WorkshopReferenceEventSink`
- `WorkshopRegionBasedWeatherData`
- `WorkshopRemovedInvalidItemsMsg`
- `WorkshopUI::WorkshopRepairFailureCallback`
- `WorkshopClient::WorkshopStateIdle`
- `WorkshopClient::WorkshopStateUpdate`
- `WorkshopClient::WorkshopStateWait3D`
- `WorkshopClient::WorkshopStateWaitForWireReceipt`
- `WorkshopToggleFilter`
- `WorkshopToggleMainMode`
- `WorkshopToggleMoreOptions`
- `WorkshopUpdateServerSpinner`
- `WorkshopHavokUtils::hknpWorkshopCastCollector`
- `WorkshopHavokUtils::hknpWorkshopIntersectCollector`
- `WorkshopHavokUtils::hknpWorkshopLineOfSightCollector`
- `WorkshopHavokUtils::hknpWorkshopRayCastCollector`

### Nuclear Winter / PvP Classes (36)

- `VWorldData_JoinSurvivalWorld::V?$TUIEventDispatcher::AutoRegisterEvent`
- `VBSTSingletonImplicit::$0CAA::VUIEventDispatcher::VBSFixedString::V?$BSTFactoryManager::VWorldData_JoinSurvivalWorld::V?$TUIEventDispatcher::AutoRegisterFactory`
- `UHUDSurvivalItemHoverEvent::BSTEventSink`
- `ULocalPlayerExitPvPCombatEvent::BSTEventSink`
- `VWorldData_JoinSurvivalWorld::BSTEventSink`
- `UHUDSurvivalItemHoverEvent::BSTEventSource`
- `ULocalPlayerExitPvPCombatEvent::BSTEventSource`
- `USurvivalThresholdEvent::BSTEventSource`
- `VWorldData_JoinSurvivalWorld::BSTEventSource`
- `BSTGlobalEvent::UHUDSurvivalItemHoverEvent::V?$EventSource::U?$BSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::UHUDSurvivalItemHoverEvent::V?$EventSource::BSTSDMTraits`
- `BSTGlobalEvent::ULocalPlayerExitPvPCombatEvent::V?$EventSource::U?$BSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::ULocalPlayerExitPvPCombatEvent::V?$EventSource::BSTSDMTraits`
- `BSTGlobalEvent::USurvivalThresholdEvent::V?$EventSource::U?$BSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::USurvivalThresholdEvent::V?$EventSource::BSTSDMTraits`
- `BSTGlobalEvent::VWorldData_JoinSurvivalWorld::V?$EventSource::U?$BSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::VWorldData_JoinSurvivalWorld::V?$EventSource::BSTSDMTraits`
- `UBSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::UHUDSurvivalItemHoverEvent::V?$EventSource::BSTSingletonSDM`
- `UBSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::ULocalPlayerExitPvPCombatEvent::V?$EventSource::BSTSingletonSDM`
- `UBSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::USurvivalThresholdEvent::V?$EventSource::BSTSingletonSDM`
- `UBSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::VWorldData_JoinSurvivalWorld::V?$EventSource::BSTSingletonSDM`
- `BSTGlobalEvent::UHUDSurvivalItemHoverEvent::V?$EventSource::U?$BSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::UHUDSurvivalItemHoverEvent::V?$EventSource::U?$BSTSDMTraits::BSTSingletonSDMBase`
- `BSTGlobalEvent::ULocalPlayerExitPvPCombatEvent::V?$EventSource::U?$BSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::ULocalPlayerExitPvPCombatEvent::V?$EventSource::U?$BSTSDMTraits::BSTSingletonSDMBase`
- `BSTGlobalEvent::USurvivalThresholdEvent::V?$EventSource::U?$BSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::USurvivalThresholdEvent::V?$EventSource::U?$BSTSDMTraits::BSTSingletonSDMBase`
- `BSTGlobalEvent::VWorldData_JoinSurvivalWorld::V?$EventSource::U?$BSTSingletonSDMOpStaticBuffer::BSTGlobalEvent::VWorldData_JoinSurvivalWorld::V?$EventSource::U?$BSTSDMTraits::BSTSingletonSDMBase`
- `BSTGlobalEvent::UHUDSurvivalItemHoverEvent::V?$EventSource::BSTSingletonSDMOpStaticBuffer`
- `BSTGlobalEvent::ULocalPlayerExitPvPCombatEvent::V?$EventSource::BSTSingletonSDMOpStaticBuffer`
- `BSTGlobalEvent::USurvivalThresholdEvent::V?$EventSource::BSTSingletonSDMOpStaticBuffer`
- `BSTGlobalEvent::VWorldData_JoinSurvivalWorld::V?$EventSource::BSTSingletonSDMOpStaticBuffer`
- `BSTGlobalEvent::UHUDSurvivalItemHoverEvent::EventSource`
- `BSTGlobalEvent::ULocalPlayerExitPvPCombatEvent::EventSource`
- `BSTGlobalEvent::USurvivalThresholdEvent::EventSource`
- `BSTGlobalEvent::VWorldData_JoinSurvivalWorld::EventSource`
- `WorldRules::W4FOWPvPRules::FOWSettingEnum`
- `UHUDSurvivalItemHoverEvent::?$BSTEventSource::Processor`
- `ULocalPlayerExitPvPCombatEvent::?$BSTEventSource::Processor`
- `USurvivalThresholdEvent::?$BSTEventSource::Processor`
- `VWorldData_JoinSurvivalWorld::?$BSTEventSource::Processor`
- `VWorldData_JoinSurvivalWorld::TUIEventDispatcher`
- `WorldData_JoinSurvivalWorld`

### Atom Shop / Store Classes (80)

- `AccountUpgradesStore`
- `AccountUpgradesStoreDataModel`
- `AccountUpgradesStoreGotoMarketplace`
- `AccountUpgradesStoreManager`
- `AccountUpgradesStoreOpen`
- `AccountUpgradesStoreOpenMarketplacePayload`
- `AccountUpgradesStore_Close`
- `AtomUpdateNotificationMsg`
- `AtomicShopMenu`
- `BGSConsumableEntitlement`
- `BGSCrateServiceEntitlement`
- `BGSEntitlement`
- `BGSRequiredEntitlementForm`
- `CampSlotsOpenStoreEvent`
- `ConfirmPurchaseHandler`
- `ConfirmPurchaseRankPayload`
- `WorkshopUI::ConfirmScrapStoredItemCallback`
- `EntitlementMappingsManager::CachedMappings::EntitlementInstance`
- `EntitlementMappingsManager`
- `EntitlementMappingsRefreshReceiptMsg`
- `?A0x381ba398::Entitlement_BGSEntitlement`
- `?A0x381ba398::Entitlement_CustomerService_QuestRestart`
- `ExternalPurchaseDataModel`
- `ExternalPurchaseItemData`
- `ExternalPurchaseMenu`
- `ExternalPurchaseMenu_BulkPurchase`
- `ExternalPurchaseMenu_CancelPurchase`
- `ExternalPurchaseMenu_Failure`
- `ExternalPurchaseMenu_GotoAtoms`
- `ExternalPurchaseMenu_GotoStore`
- `IMemoryStore`
- `IMemoryStoreBase`
- `IMovementDeltaStore`
- `BSScript::IStore`
- `MovementHandlerAgentStorePlannerOutput`
- `NPEPurchaseLevelBoostEvent`
- `OnProcessedPurchaseCompleteEvent`
- `PSConfirmPurchaseRankEvent`
- `PSPurchaseRankEvent`
- `PSPurchaseSeasonPassEvent`
- `PerksUIDataModel_PurchaseLevelBoost`
- `PurchaseCompleteData`
- `PurchaseRankCloseEvent`
- `PurchaseRankMenu`
- `RankInsufficientAtoms`
- `RefreshEntitlementMappingsMsg`
- `WorkshopNetwork::ScrapStoredItemMessage`
- `SeasonRankUpPurchasedMsg`
- `SplashGotoFO1Purchase`
- `SplashGotoStore`
- `SplashMenuGotoStorePayload`
- `CompactingStore::Store`
- `GameScript::Store`
- `AtomicShopMenu::StoreBrowserImage`
- `StoreCategoryChanged`
- `StoreCategoryPayload`
- `StoreDataModel`
- `StoreEquipUnequipPayload`
- `StoreGotoMarketplace`
- `StoreItemInspectedBeginEvent`
- `StoreItemInspectedBeginPayload`
- `StoreItemInspectedEndEvent`
- `StoreItemInspectedEndPayload`
- `WorkshopNetwork::StoreItemMessage`
- `StoreManager`
- `StoreMenuEquipUnequip`
- `StoreMenuOnBalanceDisabled`
- `StoreMenuPurchase`
- `StorePurchaseClosed`
- `StorePurchaseOpened`
- `StorePurchasePayload`
- `WorkshopNetwork::StoredItemTransactionMessage`
- `hkbPoseStoringGeneratorOutputListener::StoredPose`
- `bps::client::seasonv2::SyncEntitlementsResult`
- `UpdateEntitlementRequests`
- `ValidateEntitlementsHashMismatchMsg`
- `ValidateEntitlementsMsg`
- `WorldData_OpenAtomicShop`
- `hknpConstraintAtomSolver`
- `nsContainerMenu::workbenchStoreAllJunk`

## Methodology

1. Extracted all ASCII strings from Fallout76.exe using `strings -a`
2. Filtered for MSVC RTTI type descriptor format: `.?AV<name>@@` (class) and `.?AU<name>@@` (struct)
3. Demangled names by parsing the MSVC name encoding (namespace separators `@`, template prefix `?$`)
4. Categorized by namespace and class name prefix patterns
5. Cross-referenced with embedded source paths, Class::Method strings, and error messages

### Limitations

- RTTI only captures classes with virtual functions (polymorphic types)
- Template instantiations with complex parameters may not fully demangle
- VTABLE addresses not extracted (requires PE section parsing beyond strings)
- SFE address cross-reference requires the SFE address list file

### Data Files

- Full catalog: `data/fallout76/rtti_classes.json`
- This analysis: `findings/fo76/085-rtti-class-catalog.md`