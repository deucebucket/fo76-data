# Fallout 76 Modding Reference Guide

## Address Library Overview
- **Total entries**: 3434
- **Named functions**: 1004
- **Virtual functions (vtable)**: 2430
- **Classes**: 253
- **Target**: Fallout76.exe Patch 66 (The Backwoods, March 2026)
- **Image Base**: 0x140000000

## Key Classes for Modders

### GameNetworkMessageManager (102 functions)

| Function | Address | RVA |
|----------|---------|-----|
| HandleMessage | 0x142000620 | 0x2000620 |
| HandleMessage::ActiveDuelServerMsg | 0x141804500 | 0x1804500 |
| HandleMessage::AuditClientSharedTitleStorageSettingsMessage | 0x141804500 | 0x1804500 |
| HandleMessage::AutomatedTesting::QuestAliasResponse | 0x141804500 | 0x1804500 |
| HandleMessage::AutomatedTesting::RequestExecutionIndex | 0x141804500 | 0x1804500 |
| HandleMessage::ChallengePassXPIncrementedMsg | 0x141804500 | 0x1804500 |
| HandleMessage::CreateChainExplosionMessageServer | 0x141804500 | 0x1804500 |
| HandleMessage::CreateInstancedCellInLocationMsg | 0x141804500 | 0x1804500 |
| HandleMessage::DialogueNetworkRM::SetScriptHeadTrackTargetDialogueMessage | 0x141804500 | 0x1804500 |
| HandleMessage::EnableClientToSpendVATSCrit | 0x141804500 | 0x1804500 |
| HandleMessage::HUDExperienceUpdateEventMsg | 0x141804500 | 0x1804500 |
| HandleMessage::HotloadPluginCompleteMessage | 0x141804500 | 0x1804500 |
| HandleMessage::LegendaryPerkCardRequest | 0x141804500 | 0x1804500 |
| HandleMessage::MessageBoxNetwork::ResetHelpMessageOnClient | 0x141804500 | 0x1804500 |
| HandleMessage::NetworkPathManagerHelpers::RequestShortPathBuild | 0x141804500 | 0x1804500 |
| HandleMessage::PlayerDecorating::RequestDisplayDecorateItemInSlot | 0x141804500 | 0x1804500 |
| HandleMessage::PlayerEmoteUIEventToClient | 0x141804500 | 0x1804500 |
| HandleMessage::RequestOpenPerkCardPackMsg | 0x141804500 | 0x1804500 |
| HandleMessage::RequestStartDailyContentMsg | 0x141804500 | 0x1804500 |
| HandleMessage::RequestTransferItemBatchMsg | 0x141804500 | 0x1804500 |
| HandleMessage::SeasonRankUpPurchasedMsg | 0x141804500 | 0x1804500 |
| HandleMessage::SecureTrading::PlayerTradeAcceptFail | 0x141804500 | 0x1804500 |
| HandleMessage::SecureTrading::PlayerTradeRejectOffer | 0x141804500 | 0x1804500 |
| HandleMessage::SecureTrading::PlayerTradeRequestItem | 0x141804500 | 0x1804500 |
| HandleMessage::SecureTradingCampVending::ShowItemSoldHudMessage | 0x141804500 | 0x1804500 |
| HandleMessage::SendOnScreenMsg | 0x141804500 | 0x1804500 |
| HandleMessage::WorkshopNetwork::LockItemMessage | 0x141804500 | 0x1804500 |
| HandleMessage::WorkshopNetwork::RequestAdjustableSettingUpdate | 0x141804500 | 0x1804500 |
| SendMessage::AbortTransportToInstancedCellMsg | 0x141804500 | 0x1804500 |
| SendMessage::AddMusicTypeOnClient | 0x141804500 | 0x1804500 |
| SendMessage::ApplyCategorySnapshotOnClient | 0x141804500 | 0x1804500 |
| SendMessage::AutomatedTesting::QuestAliasResponse | 0x141804500 | 0x1804500 |
| SendMessage::AutomatedTesting::QueueBatchedConsoleCommand | 0x141804500 | 0x1804500 |
| SendMessage::AutomatedTesting::RequestExecutionIndex | 0x141804500 | 0x1804500 |
| SendMessage::BabylonBriefcasePickupMsg | 0x141804500 | 0x1804500 |
| SendMessage::BabylonCombatFeedbackMsg | 0x141804500 | 0x1804500 |
| SendMessage::BabylonStalemateMsg | 0x141804500 | 0x1804500 |
| SendMessage::BabylonTeamLossMsg | 0x141804500 | 0x1804500 |
| SendMessage::ClientSNREventUpdated | 0x141804500 | 0x1804500 |
| SendMessage::ClientSpecificCollisionChangeMsg | 0x141804500 | 0x1804500 |
| SendMessage::CustomMarkerChangeMsg | 0x141804500 | 0x1804500 |
| SendMessage::DailyContentResetMsg | 0x141804500 | 0x1804500 |
| SendMessage::DebugGameplayAutoTestComplete | 0x141804500 | 0x1804500 |
| SendMessage::DialogueNetworkRM::SayTopicInfoMessage | 0x141804500 | 0x1804500 |
| SendMessage::DialogueNetworkRM::SetActorInPrivateSceneDialogueMessage | 0x141804500 | 0x1804500 |
| SendMessage::EnableClientToSpendVATSCrit | 0x141804500 | 0x1804500 |
| SendMessage::EntitlementMappingsRefreshReceiptMsg | 0x141804500 | 0x1804500 |
| SendMessage::FastTravel::PendingFastTravelCanceledMsg | 0x141804500 | 0x1804500 |
| SendMessage::ForceGetPerkCardChangesFromServerMsg | 0x141804500 | 0x1804500 |
| SendMessage::MessageBoxNetwork::ClearHelpMessagesOnClient | 0x141804500 | 0x1804500 |
| SendMessage::MessageBoxNetwork::ResetHelpMessageOnClient | 0x141804500 | 0x1804500 |
| SendMessage::PerkCardChangesMsg | 0x141804500 | 0x1804500 |
| SendMessage::PlayDistantLoopingSoundMsg | 0x141804500 | 0x1804500 |
| SendMessage::PlayDistantSoundMsg | 0x141804500 | 0x1804500 |
| SendMessage::PlayerCurrencyUpdateNotificationMsg | 0x141804500 | 0x1804500 |
| SendMessage::PlayerEmoteUIEventToServer | 0x141804500 | 0x1804500 |
| SendMessage::PlayerEnteredKeycodeMsg | 0x141804500 | 0x1804500 |
| SendMessage::PowerArmorRequestBatteryTransfer | 0x141804500 | 0x1804500 |
| SendMessage::PredictKillDeniedMsg | 0x141804500 | 0x1804500 |
| SendMessage::QuickPlayMapVotingVoteCastedMsg | 0x141804500 | 0x1804500 |
| SendMessage::RequestActivateRefMsg | 0x141804500 | 0x1804500 |
| SendMessage::RequestButtonPressOnServer | 0x141804500 | 0x1804500 |
| SendMessage::RequestCampSlotActivationMsg | 0x141804500 | 0x1804500 |
| SendMessage::RequestCampSlotUpdateMsg | 0x141804500 | 0x1804500 |
| SendMessage::RequestCriticalVATSMsg | 0x141804500 | 0x1804500 |
| SendMessage::RequestHitEvent | 0x141804500 | 0x1804500 |
| SendMessage::RequestInventorySyncMsg | 0x141804500 | 0x1804500 |
| SendMessage::RequestNextSpectatorTargetMsg | 0x141804500 | 0x1804500 |
| SendMessage::RequestPlaySoundForNearbyPlayersMsg | 0x141804500 | 0x1804500 |
| SendMessage::RequestReloadWeapon | 0x141804500 | 0x1804500 |
| SendMessage::RequestSpecialBuildReset | 0x141804500 | 0x1804500 |
| SendMessage::RequestStartExpeditionMsg | 0x141804500 | 0x1804500 |
| SendMessage::RequestStartExpeditionResponseMsg | 0x141804500 | 0x1804500 |
| SendMessage::RequestTransferItemMsg | 0x141804500 | 0x1804500 |
| SendMessage::SecureTrading::PlayerTradeAcceptFail | 0x141804500 | 0x1804500 |
| SendMessage::SecureTrading::PlayerTradeCancelRequestItem | 0x141804500 | 0x1804500 |
| SendMessage::SecureTrading::PlayerTradeRejectOffer | 0x141804500 | 0x1804500 |
| SendMessage::SecureTrading::PlayerTradeRequestItem | 0x141804500 | 0x1804500 |
| SendMessage::SecureTrading::RequestPlayerTradeSyncOffers | 0x141804500 | 0x1804500 |
| SendMessage::SecureTradingCampVending::PlayerVendingAcceptFail | 0x141804500 | 0x1804500 |
| SendMessage::SecureTradingCampVending::PlayerVendingCreateOffer | 0x141804500 | 0x1804500 |
| SendMessage::SecureTradingCampVending::RequestPlayerVendingAcceptOffer | 0x141804500 | 0x1804500 |
| SendMessage::SeenLootMsg | 0x141804500 | 0x1804500 |
| SendMessage::SyncGameSecondsPlayed | 0x141804500 | 0x1804500 |
| SendMessage::TerminalNet::NotifyTerminalCloseMessage | 0x141804500 | 0x1804500 |
| SendMessage::TerminalNet::ServerEvalResultsMessage | 0x141804500 | 0x1804500 |
| SendMessage::Transporting::CenterOnCellMsg | 0x141804500 | 0x1804500 |
| SendMessage::Transporting::DenyTeleportToLocationMsg | 0x141804500 | 0x1804500 |
| SendMessage::Transporting::ForceMoveToTransformMsg | 0x141804500 | 0x1804500 |
| SendMessage::Transporting::NotifyClientAreaLoadedMsg | 0x141804500 | 0x1804500 |
| SendMessage::UNKNOWNMESSAGETYPE | 0x141804500 | 0x1804500 |
| SendMessage::UpdateEntitlementRequests | 0x141804500 | 0x1804500 |
| SendMessage::WorkbenchNet::RequestScrapItemBatchMessage | 0x141804500 | 0x1804500 |
| SendMessage::WorkshopNetwork::CampCollisionMsg | 0x141804500 | 0x1804500 |
| SendMessage::WorkshopNetwork::ContestWorkshopMessage | 0x141804500 | 0x1804500 |
| SendMessage::WorkshopNetwork::NewWireMessage | 0x141804500 | 0x1804500 |
| SendMessage::WorkshopNetwork::PlacePackinMessage | 0x141804500 | 0x1804500 |
| SendMessage::WorkshopNetwork::ReconnectWireMessage | 0x141804500 | 0x1804500 |
| SendMessage::WorkshopNetwork::RepairAllMessage | 0x141804500 | 0x1804500 |
| SendMessage::WorkshopNetwork::RequestCampPackUpMsg | 0x141804500 | 0x1804500 |
| SendMessage::WorkshopNetwork::RequestWorkshopBudgetReportMessage | 0x141804500 | 0x1804500 |
| SendMessage::WorkshopNetwork::StoreItemMessage | 0x141804500 | 0x1804500 |

### Quests (74 functions)

| Function | Address | RVA |
|----------|---------|-----|
| CreatureDialogueAssaultron::Scenes | 0x142237c50 | 0x2237c50 |
| CreatureDialogueBloatfly::Scenes | 0x142237c50 | 0x2237c50 |
| CreatureDialogueBloodbug::Scenes | 0x142237c50 | 0x2237c50 |
| CreatureDialogueBrahmin::Scenes | 0x142237c50 | 0x2237c50 |
| CreatureDialogueRadRoach::Scripts | 0x142237c50 | 0x2237c50 |
| CreatureDialogueRadStag::Scripts | 0x142237c50 | 0x2237c50 |
| CreatureDialogueRadscorpion::Scripts | 0x142237c50 | 0x2237c50 |
| CreatureDialogueReaperBot::Scripts | 0x142237c50 | 0x2237c50 |
| DQ01_DailyQuest::Scripts | 0x141804500 | 0x1804500 |
| DQ01_KillCreatures::Scripts | 0x141804500 | 0x1804500 |
| DQ01_RadioDailyQuest::Scripts | 0x141804500 | 0x1804500 |
| DQR01::Scripts | 0x141804500 | 0x1804500 |
| DQR03::Scripts | 0x141804500 | 0x1804500 |
| DialogueSharedInfos::Warning | 0x142237c50 | 0x2237c50 |
| DialogueSuperMutantConversations01::Warning | 0x142237c50 | 0x2237c50 |
| DialogueSuperMutantConversations02::Warning | 0x142237c50 | 0x2237c50 |
| DialogueSuperMutantConversations03::Warning | 0x142237c50 | 0x2237c50 |
| ENz04_PatrolHandler::Scenes | 0x142237c50 | 0x2237c50 |
| ENz09_Room::Scenes | 0x142237c50 | 0x2237c50 |
| EWSEncounterBuyTable::Scenes | 0x142237c50 | 0x2237c50 |
| FF00_AreaSpawner::Scenes | 0x142237c50 | 0x2237c50 |
| FS02::Scripts | 0x142237c50 | 0x2237c50 |
| FS02_Fruition::Scripts | 0x142237c50 | 0x2237c50 |
| FS03::Scripts | 0x142237c50 | 0x2237c50 |
| FSS01::Scripts | 0x142237c50 | 0x2237c50 |
| GQ_Swarm::Warning | 0x142237c50 | 0x2237c50 |
| GQ_WorkshopAttack::Warning | 0x142237c50 | 0x2237c50 |
| GQ_WorkshopAttackScorchbeasts::Warning | 0x142237c50 | 0x2237c50 |
| GQ_WorkshopAttackVultures::Warning | 0x142237c50 | 0x2237c50 |
| MTNG01_Regional::Scripts | 0x142237c50 | 0x2237c50 |
| MTNZ03_Box_Hunter::Warning | 0x141804500 | 0x1804500 |
| MTNZ04_Meltdown::Warning | 0x141804500 | 0x1804500 |
| MTNZ05_Messenger::Warning | 0x141804500 | 0x1804500 |
| MTR03_BlackwaterMine_AreaSpawner::Scenes | 0x142237c50 | 0x2237c50 |
| MTR03_BurningMine_AreaSpawner::Scenes | 0x142237c50 | 0x2237c50 |
| MTR03_Demerits::Scenes | 0x142237c50 | 0x2237c50 |
| MTR03_DialogueMineGamesSystem::Scenes | 0x142237c50 | 0x2237c50 |
| MTR09_Misc::Scripts | 0x142237c50 | 0x2237c50 |
| MTR10_Battle::Scripts | 0x142237c50 | 0x2237c50 |
| MTRG01_Overtime::Scripts | 0x142237c50 | 0x2237c50 |
| MTR_Hornwright_Industrial_Master::Scenes | 0x141804500 | 0x1804500 |
| NoQuest::Scenes | 0x141804500 | 0x1804500 |
| Nuke_Codes::Scenes | 0x141804500 | 0x1804500 |
| RDR_Radio_Boosted::Warning | 0x142237c50 | 0x2237c50 |
| RDR_Radio_Weak::Warning | 0x142237c50 | 0x2237c50 |
| RE_AssaultKMK01::Warning | 0x142237c50 | 0x2237c50 |
| RE_AssaultKMK02::Warning | 0x142237c50 | 0x2237c50 |
| SF05_ReturnToNormalcy::Scripts | 0x142979840 | 0x2979840 |
| SF06_RespectTheDead::Scripts | 0x142979840 | 0x2979840 |
| SF07_MoeDigsSafety::Scenes | 0x142237c50 | 0x2237c50 |
| SF07_MoeDigsSafety::Scripts | 0x142979840 | 0x2979840 |
| SF08_SuicideRun::Scenes | 0x142237c50 | 0x2237c50 |
| SF08_SuicideRunPre::Scenes | 0x142237c50 | 0x2237c50 |
| SQ_AirDrop::Scripts | 0x142237c50 | 0x2237c50 |
| SQ_Bounty_Assault::Scripts | 0x142237c50 | 0x2237c50 |
| SQ_Bounty_MostWanted::Scripts | 0x142237c50 | 0x2237c50 |
| SQ_Bounty_Murder::Scripts | 0x142237c50 | 0x2237c50 |
| TESTQuestLVC_StackDialogue::Warning | 0x142237c50 | 0x2237c50 |
| TESTQuestMaster_LVC::Warning | 0x142237c50 | 0x2237c50 |
| TESTWeather::Warning | 0x142237c50 | 0x2237c50 |
| TW001::Warning | 0x142237c50 | 0x2237c50 |
| TestKurtHolotapeQuest::Scripts | 0x141804500 | 0x1804500 |
| TestKurtQuest02::Scripts | 0x141804500 | 0x1804500 |
| TestKurtQuest03::Scripts | 0x141804500 | 0x1804500 |
| TestKurtQuest::Scripts | 0x141804500 | 0x1804500 |
| TestObjectiveTimer::Scripts | 0x141804500 | 0x1804500 |
| V94Access::Scenes | 0x142237c50 | 0x2237c50 |
| V94_1::Scenes | 0x142237c50 | 0x2237c50 |
| V94_2::Scenes | 0x142237c50 | 0x2237c50 |
| V94_3::Scenes | 0x142237c50 | 0x2237c50 |
| W05_MQR101A::Scripts | 0x142237c50 | 0x2237c50 |
| W05_MQR_205P::Scripts | 0x142237c50 | 0x2237c50 |
| W05_MQS201::Scripts | 0x142237c50 | 0x2237c50 |
| W05_MQS202::Scripts | 0x142237c50 | 0x2237c50 |

### ClassTraits (56 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AVM1Movie | 0x14255596b | 0x255596b |
| AccessibilityImplementation | 0x1430b0e89 | 0x30b0e89 |
| ActionScriptVersion | 0x140bd3a5b | 0xbd3a5b |
| AppLifecycleEvent | 0x142342d90 | 0x2342d90 |
| ApplicationDomain | 0x140d10ede | 0xd10ede |
| BlendMode | 0x14254fb28 | 0x254fb28 |
| ByteArray | 0x142c82930 | 0x2c82930 |
| ColorTransform | 0x14197c170 | 0x197c170 |
| DropShadowFilter | 0x142bef260 | 0x2bef260 |
| Error | 0x142c81de0 | 0x2c81de0 |
| Event | 0x1427ba9a0 | 0x27ba9a0 |
| FileFilter | 0x140e9dc40 | 0xe9dc40 |
| FileReferenceList | 0x1418dbef0 | 0x18dbef0 |
| FocusEvent | 0x1431e2500 | 0x31e2500 |
| GeolocationEvent | 0x14197af10 | 0x197af10 |
| GlowFilter | 0x142ebb690 | 0x2ebb690 |
| GraphicsEndFill | 0x142e1ff70 | 0x2e1ff70 |
| IDataInput | 0x142c82060 | 0x2c82060 |
| IDynamicPropertyOutput | 0x142b90e70 | 0x2b90e70 |
| IDynamicPropertyWriter | 0x14197ba20 | 0x197ba20 |
| IGraphicsFill | 0x140d10ede | 0xd10ede |
| IME | 0x142c06370 | 0x2c06370 |
| InvalidSWFError | 0x1430b0e89 | 0x30b0e89 |
| Loader | 0x1434ee440 | 0x34ee440 |
| LoaderContext | 0x1430b0e89 | 0x30b0e89 |
| LoaderInfo | 0x14039a050 | 0x39a050 |
| Matrix3D | 0x141efebc0 | 0x1efebc0 |
| MorphShape | 0x143872ca0 | 0x3872ca0 |
| MovieClip | 0x142c82060 | 0x2c82060 |
| NetStatusEvent | 0x141293a50 | 0x1293a50 |
| PixelSnapping | 0x142c82a50 | 0x2c82a50 |
| QName | 0x142c821c0 | 0x2c821c0 |
| RangeError | 0x141906070 | 0x1906070 |
| ReferenceError | 0x143778200 | 0x3778200 |
| Responder | 0x142b838a0 | 0x2b838a0 |
| SecurityErrorEvent | 0x1404045b0 | 0x4045b0 |
| ShaderFilter | 0x14247ba3a | 0x247ba3a |
| ShaderJob | 0x142a19bcd | 0x2a19bcd |
| ShaderParameterType | 0x14049d3d0 | 0x49d3d0 |
| ShaderPrecision | 0x14164dde5 | 0x164dde5 |
| SharedObjectFlushStatus | 0x142b90680 | 0x2b90680 |
| SimpleButton | 0x14157d3f0 | 0x157d3f0 |
| Socket | 0x142b90730 | 0x2b90730 |
| SpreadMethod | 0x14226bd8f | 0x226bd8f |
| Sprite | 0x142d061d0 | 0x2d061d0 |
| StackOverflowError | 0x1426abc10 | 0x26abc10 |
| StageDisplayState | 0x141935a80 | 0x1935a80 |
| StageQuality | 0x142266ac0 | 0x2266ac0 |
| System | 0x142c060b0 | 0x2c060b0 |
| Timer | 0x141540e6a | 0x1540e6a |
| TimerEvent | 0x14177db20 | 0x177db20 |
| URLLoader | 0x142b90bb0 | 0x2b90bb0 |
| URLLoaderDataFormat | 0x142b90fe0 | 0x2b90fe0 |
| URLRequest | 0x142b90690 | 0x2b90690 |
| URLStream | 0x140bd3a90 | 0xbd3a90 |
| XMLDocument | 0x142ebb6a0 | 0x2ebb6a0 |

### Actor (52 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AddPerk | 0x1417ee390 | 0x17ee390 |
| AddTemporaryPerk | 0x1417ee390 | 0x17ee390 |
| AddWornOutfitImpl | 0x142021770 | 0x2021770 |
| AdjustForCap | 0x1406e8f90 | 0x6e8f90 |
| ApplyPerksFromBase | 0x1406d6ec0 | 0x6d6ec0 |
| CancelNetPredictDeath | 0x1438ca738 | 0x38ca738 |
| ChangeGunState | 0x143685d70 | 0x3685d70 |
| ChangeProcessLevel | 0x140949990 | 0x949990 |
| ClearLookAtTarget | 0x141c17640 | 0x1c17640 |
| CombatHit | 0x1402a59d0 | 0x2a59d0 |
| CreateBlood | 0x141bfc740 | 0x1bfc740 |
| CreateDisLimbs | 0x143496d90 | 0x3496d90 |
| DefaultRagdollHandler::InitRagdoll | 0x141ccc5a0 | 0x1ccc5a0 |
| DetachHavok | 0x1438822e0 | 0x38822e0 |
| Disable | 0x1406d6ec0 | 0x6d6ec0 |
| DismemberLimbs | 0x140e409b0 | 0xe409b0 |
| DoHitMe_Predicted | 0x140885c40 | 0x885c40 |
| DoNetAction | 0x143333d30 | 0x3333d30 |
| DoNetAction (FAILURE) | 0x141fb466a | 0x1fb466a |
| DoRemovePerk | 0x140d910e0 | 0xd910e0 |
| DrawWeaponMagicHands | 0x1416a1690 | 0x16a1690 |
| EvaluatePackage | 0x141aa6590 | 0x1aa6590 |
| GetControllingActor | 0x141759a60 | 0x1759a60 |
| HandleNetworkedLocationWarp | 0x1434da4f0 | 0x34da4f0 |
| HideLimb | 0x1433123f0 | 0x33123f0 |
| InitiateDialogue | 0x141ab1ed0 | 0x1ab1ed0 |
| IsDead | 0x141a13bf0 | 0x1a13bf0 |
| Jump | 0x140b86df0 | 0xb86df0 |
| LowMvmt | 0x141d09950 | 0x1d09950 |
| Move | 0x1427ad780 | 0x27ad780 |
| MoveToHigh_Internal | 0x140e409b0 | 0xe409b0 |
| MoveToLow | 0x142022d20 | 0x2022d20 |
| MovetoLow | 0x142022d20 | 0x2022d20 |
| MovetoMiddleHigh | 0x140a15420 | 0xa15420 |
| OnActionStarted | 0x143126f70 | 0x3126f70 |
| OnCrippleLimb | 0x140954450 | 0x954450 |
| PostReanimate | 0x1438f1fe0 | 0x38f1fe0 |
| RagdollHandler::DoRagdoll | 0x140bcdf00 | 0xbcdf00 |
| RagdollHandler::PrepareForRagdoll | 0x143883750 | 0x3883750 |
| ResetCachedValuesForPerk | 0x1416a25d0 | 0x16a25d0 |
| SetCurrentTarget | 0x143883750 | 0x3883750 |
| SetLookAtTarget | 0x141f01af0 | 0x1f01af0 |
| SetLooking | 0x1438f1fe0 | 0x38f1fe0 |
| TrymoveToMiddleLow | 0x1406d6ec0 | 0x6d6ec0 |
| UpdateCastPowers | 0x1407db090 | 0x7db090 |
| UpdateMagic | 0x141ffbdd0 | 0x1ffbdd0 |
| UpdateMinimal | 0x143882010 | 0x3882010 |
| UpdateParentSpace | 0x1434da4f0 | 0x34da4f0 |
| UpdateSoundCallBack | 0x140885c40 | 0x885c40 |
| UpdateVoiceTimer | 0x141656690 | 0x1656690 |
| WarpTo | 0x142025810 | 0x2025810 |
| WornArmorChanged | 0x1406d6ec0 | 0x6d6ec0 |

### Classes (38 functions)

| Function | Address | RVA |
|----------|---------|-----|
| ActionScriptVersion | 0x1403dd950 | 0x3dd950 |
| AppLifecycleEvent | 0x1418531f0 | 0x18531f0 |
| BitmapFilterQuality | 0x14197bc70 | 0x197bc70 |
| CapsStyle | 0x14209a913 | 0x209a913 |
| Date | 0x142d061e0 | 0x2d061e0 |
| Endian | 0x1420bcdd0 | 0x20bcdd0 |
| Error | 0x142bcd1f0 | 0x2bcd1f0 |
| ExternalInterface | 0x1433df5a0 | 0x33df5a0 |
| Font | 0x142342dc0 | 0x2342dc0 |
| FontStyle | 0x14197b810 | 0x197b810 |
| GamePadAnalogEvent | 0x14197a980 | 0x197a980 |
| GeolocationEvent | 0x14197b560 | 0x197b560 |
| GradientType | 0x141a00610 | 0x1a00610 |
| GraphicsPathWinding | 0x142e1ff10 | 0x2e1ff10 |
| HTTPStatusEvent | 0x14197af10 | 0x197af10 |
| IME | 0x142c82a40 | 0x2c82a40 |
| IMEConversionMode | 0x1418c3860 | 0x18c3860 |
| InteractiveObjectEx | 0x14208c570 | 0x208c570 |
| InterpolationMethod | 0x142d06270 | 0x2d06270 |
| LoaderInfo | 0x140d9708f | 0xd9708f |
| MouseCursorEvent | 0x14197c340 | 0x197c340 |
| NetStatusEvent | 0x142c82910 | 0x2c82910 |
| PressAndTapGestureEvent | 0x142c824b0 | 0x2c824b0 |
| SWFVersion | 0x142c82690 | 0x2c82690 |
| SecurityDomain | 0x141f4ce90 | 0x1f4ce90 |
| SharedObjectFlushStatus | 0x142b90730 | 0x2b90730 |
| StageDisplayState | 0x141e60730 | 0x1e60730 |
| StageScaleMode | 0x1413c5ad0 | 0x13c5ad0 |
| String | 0x142e1fd30 | 0x2e1fd30 |
| System | 0x142ff896f | 0x2ff896f |
| TextDisplayMode | 0x142bf4e30 | 0x2bf4e30 |
| TextEvent | 0x141fa3350 | 0x1fa3350 |
| TextFieldEx | 0x1423bfb7a | 0x23bfb7a |
| TextFormatAlign | 0x14197c260 | 0x197c260 |
| URLLoaderDataFormat | 0x14197b3e0 | 0x197b3e0 |
| UncaughtErrorEvent | 0x142c82750 | 0x2c82750 |
| Utils3D | 0x14197b750 | 0x197b750 |
| XMLNodeType | 0x142569980 | 0x2569980 |

### Scripts (35 functions)

| Function | Address | RVA |
|----------|---------|-----|
| DebugTrace::ENz03 | 0x1418d54cc | 0x18d54cc |
| DebugTrace::ENz04 | 0x1418d54cc | 0x18d54cc |
| DebugTrace::ENz05 | 0x1418d54cc | 0x18d54cc |
| DebugTrace::ENz06 | 0x1418d54cc | 0x18d54cc |
| DebugTrace::LC066 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::LC067 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::LC068 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::LC143 | 0x141804500 | 0x1804500 |
| DebugTrace::LC144 | 0x141804500 | 0x1804500 |
| DebugTrace::LC145 | 0x141804500 | 0x1804500 |
| DebugTrace::LC157 | 0x141804500 | 0x1804500 |
| DebugTrace::LC158 | 0x141804500 | 0x1804500 |
| DebugTrace::LC194 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::LC195 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::LC196 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::POI009 | 0x140957dc0 | 0x957dc0 |
| DebugTrace::POI010 | 0x140957dc0 | 0x957dc0 |
| DebugTrace::POI011 | 0x140957dc0 | 0x957dc0 |
| DebugTrace::POI012 | 0x140957dc0 | 0x957dc0 |
| DebugTrace::POI013 | 0x140957dc0 | 0x957dc0 |
| DebugTrace::POI030 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::POI031 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::POI032 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::POI059 | 0x141804500 | 0x1804500 |
| DebugTrace::POI060 | 0x141804500 | 0x1804500 |
| DebugTrace::POI061 | 0x141804500 | 0x1804500 |
| DebugTrace::POI158 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::POI159 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::POI160 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::POI187 | 0x141804500 | 0x1804500 |
| DebugTrace::POI188 | 0x141804500 | 0x1804500 |
| DebugTrace::POI189 | 0x141804500 | 0x1804500 |
| DebugTrace::V63 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::V76 | 0x1407050f0 | 0x7050f0 |
| DebugTrace::V94 | 0x1407050f0 | 0x7050f0 |

### InstanceTraits (32 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AccessibilityProperties | 0x14093c826 | 0x93c826 |
| BitmapFilter | 0x142bcd120 | 0x2bcd120 |
| BlurFilter | 0x14208c410 | 0x208c410 |
| Catch | 0x142e1feb0 | 0x2e1feb0 |
| ContextMenuBuiltInItems | 0x142266ae0 | 0x2266ae0 |
| ContextMenuClipboardItems | 0x141935c40 | 0x1935c40 |
| Dictionary | 0x141906070 | 0x1906070 |
| DisplacementMapFilter | 0x14197b1e0 | 0x197b1e0 |
| DisplayObject | 0x1439b886a | 0x39b886a |
| DisplayObjectContainer | 0x1412c52d0 | 0x12c52d0 |
| Event | 0x1403ea580 | 0x3ea580 |
| FileReference | 0x142b90e60 | 0x2b90e60 |
| GeolocationEvent | 0x14197c150 | 0x197c150 |
| GraphicsEndFill | 0x1420cb630 | 0x20cb630 |
| GraphicsPath | 0x142c06370 | 0x2c06370 |
| LoaderInfo | 0x140d9708f | 0xd9708f |
| MorphShape | 0x1412029d0 | 0x12029d0 |
| Namespace | 0x142e45f10 | 0x2e45f10 |
| NetConnection | 0x140f08200 | 0xf08200 |
| Number | 0x142e45ff0 | 0x2e45ff0 |
| Shape | 0x140679d10 | 0x679d10 |
| SimpleButton | 0x1431e2130 | 0x31e2130 |
| Socket | 0x142b90e80 | 0x2b90e80 |
| Sprite | 0x143872ca0 | 0x3872ca0 |
| TextFormat | 0x14197ae20 | 0x197ae20 |
| Timer | 0x14117e12a | 0x117e12a |
| URLLoader | 0x142bcd4b0 | 0x2bcd4b0 |
| URLRequestHeader | 0x142b907b0 | 0x2b907b0 |
| UncaughtErrorEvent | 0x1412029c0 | 0x12029c0 |
| Vector_double | 0x140d7ca30 | 0xd7ca30 |
| Vector_uint | 0x14276bfb0 | 0x276bfb0 |
| XML | 0x142deb840 | 0x2deb840 |

### Events (31 functions)

| Function | Address | RVA |
|----------|---------|-----|
| ActorForOnPCDialogueTarget | 0x14157c360 | 0x157c360 |
| CommandModeEnter | 0x140a779c0 | 0xa779c0 |
| CommandModeExit | 0x140a779c0 | 0xa779c0 |
| EnterBleedout | 0x140a779c0 | 0xa779c0 |
| EnterSneaking | 0x140a779c0 | 0xa779c0 |
| EscortWaitStart | 0x140a779c0 | 0xa779c0 |
| EscortWaitStop | 0x140a779c0 | 0xa779c0 |
| ExitBleedout | 0x140a779c0 | 0xa779c0 |
| ExitLooksMenu | 0x140a779c0 | 0xa779c0 |
| FormDeleteEvent | 0x1409b75e0 | 0x9b75e0 |
| Hit | 0x143ac3240 | 0x3ac3240 |
| LimbCrippleEvent | 0x142027260 | 0x2027260 |
| LocationLoadStateChanged | 0x1407050f0 | 0x7050f0 |
| LockChanged | 0x14157c360 | 0x157c360 |
| OnPlayerCompanionDismiss | 0x140a779c0 | 0xa779c0 |
| OnPlayerConnectionChange | 0x141b2e9b0 | 0x1b2e9b0 |
| OnPlayerCreateRobot | 0x14157c360 | 0x157c360 |
| OnPlayerEnterVertibird | 0x14157c360 | 0x157c360 |
| OnPlayerHealTeammate | 0x14157c360 | 0x157c360 |
| OnPlayerUseWorkBench | 0x14157c360 | 0x157c360 |
| OnSpeechChallengeAvailable | 0x140a779c0 | 0xa779c0 |
| PickNewIdleEvent | 0x140a779c0 | 0xa779c0 |
| QuestInit | 0x1409b75e0 | 0x9b75e0 |
| QuestInit::ERROR | 0x1409b75e0 | 0x9b75e0 |
| QuestStartStop::ERROR | 0x141874690 | 0x1874690 |
| Reset | 0x140a779c0 | 0xa779c0 |
| Resurrect | 0x140a779c0 | 0xa779c0 |
| SleepStartEvent | 0x140c0a070 | 0xc0a070 |
| SwitchRaceCompleteEvent | 0x140a779c0 | 0xa779c0 |
| WaitStartEvent | 0x1434a3b50 | 0x34a3b50 |
| WorkshopReferenceReservationChanged | 0x140a779c0 | 0xa779c0 |

### BSEnlighten (21 functions)

| Function | Address | RVA |
|----------|---------|-----|
| BSEnlightenTexture::Update | 0x143505cb0 | 0x3505cb0 |
| CubeMap::Scene::UpdateTexture | 0x14068b280 | 0x68b280 |
| CubeMap::UpdateVoxelSpaceBounds | 0x14044e320 | 0x44e320 |
| EnlightenSceneData::ReinitializeMaterials | 0x142097e90 | 0x2097e90 |
| EnlightenSceneData::ToggleCubeMaps | 0x142393570 | 0x2393570 |
| EnlightenSceneData::ToggleLightmaps | 0x142393570 | 0x2393570 |
| EnlightenSceneData::ToggleProbes | 0x142393570 | 0x2393570 |
| EnlightenSceneData::UpdateCubeMapPrioritiesAndVoxelSpace | 0x140458d70 | 0x458d70 |
| EnlightenSceneData::UpdateCubeMapVolumePlanes | 0x1420cc5c0 | 0x20cc5c0 |
| EnlightenSceneData::UpdateCubeMaps | 0x141806700 | 0x1806700 |
| EnlightenSceneData::UpdateDustersGPUVisibility | 0x141709f70 | 0x1709f70 |
| EnlightenSceneData::UpdateProbeSetPriorities | 0x141b89ed0 | 0x1b89ed0 |
| EnlightenSceneData::UpdateSystemPriorities | 0x141b89ed0 | 0x1b89ed0 |
| Global::ConvertPixels | 0x140b36920 | 0xb36920 |
| Global::ScopedLockPppiManager::EndUpdatePPPIIndirection | 0x140e99200 | 0xe99200 |
| Global::`anonymous-namespace'::UpdateEnlightenSystems | 0x141af5100 | 0x1af5100 |
| Global::`anonymous-namespace'::UpdateEnlightenSystemsProbeSetsAndCubemaps | 0x1406e8f90 | 0x6e8f90 |
| Lightmaps::UpdateLights | 0x141f49670 | 0x1f49670 |
| Lightmaps::`anonymous-namespace'::SetEnvironmentLightValues | 0x142c15690 | 0x2c15690 |
| Probes::Scene::LoadProbeData | 0x143149940 | 0x3149940 |
| Probes::Scene::UpdateProbesVisualization | 0x140f20665 | 0xf20665 |

### ObjectInterface (20 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AttachMovie | 0x140ed1720 | 0xed1720 |
| CreateEmptyMovieClip | 0x143955fb0 | 0x3955fb0 |
| GetArraySize | 0x140ec07d0 | 0xec07d0 |
| GetCxform | 0x140ec07d0 | 0xec07d0 |
| GetMember | 0x1439776c0 | 0x39776c0 |
| GetParent | 0x14388d040 | 0x388d040 |
| Invoke | 0x1413b1e80 | 0x13b1e80 |
| InvokeClosure | 0x14272f500 | 0x272f500 |
| IsByteArray | 0x1413ed830 | 0x13ed830 |
| IsDisplayObjectActive | 0x140f19930 | 0xf19930 |
| IsInstanceOf | 0x143198000 | 0x3198000 |
| PushBack | 0x142051200 | 0x2051200 |
| RemoveElements | 0x1413ed830 | 0x13ed830 |
| SetArraySize | 0x140ec07d0 | 0xec07d0 |
| SetCxform | 0x140ec07d0 | 0xec07d0 |
| SetElement | 0x1435f0230 | 0x35f0230 |
| SetMatrix3D | 0x14234c761 | 0x234c761 |
| SetMember | 0x1413b1e80 | 0x13b1e80 |
| ToString | 0x141244080 | 0x1244080 |
| VisitElements | 0x140a35100 | 0xa35100 |

### LoadedAreaManager (17 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AddToAppropriateBuffer | 0x140548c00 | 0x548c00 |
| AttachCell | 0x1416653a0 | 0x16653a0 |
| ClearOldestUnattachedBufferedCell | 0x141716200 | 0x1716200 |
| DebugDumpCells | 0x14274ee60 | 0x274ee60 |
| ForEachEntryInBuffer | 0x141cac120 | 0x1cac120 |
| ForEachLoadedCell | 0x1407d0790 | 0x7d0790 |
| ForEachLoadedExteriorCell | 0x14113c8a0 | 0x113c8a0 |
| ForEachLoadedInteriorCell | 0x1407d09c0 | 0x7d09c0 |
| ForEachNearbyLoadedCell | 0x140d6e960 | 0xd6e960 |
| FreeExteriorBuffers | 0x142010170 | 0x2010170 |
| FreeInteriorBuffers | 0x140686ef0 | 0x686ef0 |
| LoadCellInternal | 0x1407df540 | 0x7df540 |
| LoadExteriorCell | 0x14316bcf0 | 0x316bcf0 |
| NotifyCellLoaded | 0x141a28b20 | 0x1a28b20 |
| NotifyCellUnloaded | 0x1438ca738 | 0x38ca738 |
| ProcessPending | 0x14073e72a | 0x73e72a |
| UnloadCell | 0x141efc140 | 0x1efc140 |

### TESObjectREFR (15 functions)

| Function | Address | RVA |
|----------|---------|-----|
| ActivateRef | 0x141245829 | 0x1245829 |
| ApplyPrecomp | 0x141810320 | 0x1810320 |
| CreateInventoryList | 0x141ab40b0 | 0x1ab40b0 |
| DetachHavok | 0x1416a25d0 | 0x16a25d0 |
| Enable | 0x1420c6ff0 | 0x20c6ff0 |
| Events::SendResolveNPCTemplatesEvent | 0x1436be7d0 | 0x36be7d0 |
| GetInteraction() | 0x143935cb0 | 0x3935cb0 |
| GetWeightInContainer | 0x140d389c0 | 0xd389c0 |
| InitHavok() | 0x141f508c0 | 0x1f508c0 |
| InitInventoryIfRequired | 0x14082c750 | 0x82c750 |
| MarkForPredictiveEnable | 0x141a28a70 | 0x1a28a70 |
| MoveRefToNewSpace | 0x1411ed220 | 0x11ed220 |
| RemoveDefaultLeveledItems | 0x143114a50 | 0x3114a50 |
| RemoveItem | 0x142c5ca70 | 0x2c5ca70 |
| TESObjectREFR | 0x14184a910 | 0x184a910 |

### AIProcess (15 functions)

| Function | Address | RVA |
|----------|---------|-----|
| DoUpdate3dModel | 0x1418cabc0 | 0x18cabc0 |
| ProcessGreet | 0x1407ec450 | 0x7ec450 |
| ResolveEquipmentQueue | 0x1415dd930 | 0x15dd930 |
| SetFurniture | 0x14065aa40 | 0x65aa40 |
| Update | 0x141c3d0f0 | 0x1c3d0f0 |
| Update3dModel | 0x14065aa40 | 0x65aa40 |
| UpdateDetection | 0x1419d9f30 | 0x19d9f30 |
| UpdateDetection (vs target) | 0x141b2f6f0 | 0x1b2f6f0 |
| UpdateGunState | 0x14314df20 | 0x314df20 |
| UpdateHigh | 0x142c11b10 | 0x2c11b10 |
| UpdateKnockState | 0x142c339f0 | 0x2c339f0 |
| UpdateLow | 0x143734910 | 0x3734910 |
| UpdatePendingHeadLoads | 0x141875740 | 0x1875740 |
| UpdateTimers | 0x14177a070 | 0x177a070 |
| VisitProcedureTree | 0x1435cabd0 | 0x35cabd0 |

### DrawWorld (14 functions)

| Function | Address | RVA |
|----------|---------|-----|
| DeferredDecals | 0x1418504b0 | 0x18504b0 |
| DeferredLightsImpl | 0x141ed31f0 | 0x1ed31f0 |
| DeferredPrePass | 0x14117bda0 | 0x117bda0 |
| Imagespace | 0x1416a3e40 | 0x16a3e40 |
| LaunchPrevisQuery | 0x1420b9c30 | 0x20b9c30 |
| LightProbes | 0x1418c0ac0 | 0x18c0ac0 |
| MainRenderSetup | 0x14065aa40 | 0x65aa40 |
| Render_PostUI | 0x140f23120 | 0xf23120 |
| Render_PreUI | 0x141efd430 | 0x1efd430 |
| Render_UI | 0x143169fe0 | 0x3169fe0 |
| UpdateOcclusionMap | 0x1434d9bb0 | 0x34d9bb0 |
| UpdateTerrain | 0x141efd430 | 0x1efd430 |
| UpdateWater | 0x141efd430 | 0x1efd430 |
| ZPrepass | 0x141cf5350 | 0x1cf5350 |

### LocalPlayerCharacter (13 functions)

| Function | Address | RVA |
|----------|---------|-----|
| CenterOnCell | 0x140c0a070 | 0xc0a070 |
| ClearQuickPlayContext | 0x1438939b0 | 0x38939b0 |
| GetInventoryEncumbrance | 0x141671550 | 0x1671550 |
| HandleActivationResult | 0x141539b32 | 0x1539b32 |
| OnNetworkBaselinesComplete::RunScript | 0x141ffbdd0 | 0x1ffbdd0 |
| OnNetworkTargetAreaLoaded - called | 0x1434d00c0 | 0x34d00c0 |
| PreNetUpdate | 0x1438822e0 | 0x38822e0 |
| RequestNetworkAuthorityUpdate | 0x1438ca738 | 0x38ca738 |
| ShouldWaitInLoadScreen | 0x140672580 | 0x672580 |
| Update Block 1 | 0x142d191c0 | 0x2d191c0 |
| UpdatePickRef | 0x143944610 | 0x3944610 |
| UpdateQPShuttingDown | 0x140951e70 | 0x951e70 |
| WornArmorChangedImpl | 0x143622f60 | 0x3622f60 |

### TESObjectCELL (11 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AddReference | 0x14146bdc0 | 0x146bdc0 |
| AttachModels | 0x1418f5580 | 0x18f5580 |
| GetCellFromKey | 0x140f5f700 | 0xf5f700 |
| HandlePackInCalcAndReset | 0x140523310 | 0x523310 |
| LoadAllTempData | 0x140523310 | 0x523310 |
| LoadAndAttachVisibilityData | 0x140523310 | 0x523310 |
| LockEnlightenData | 0x140686ef0 | 0x686ef0 |
| PrepareStaticNodeAABB | 0x140523310 | 0x523310 |
| UnlockEnlightenData | 0x141ac00c0 | 0x1ac00c0 |
| UpdateManagedNodes | 0x1408d9530 | 0x8d9530 |
| UpdateReferences3DandProcess | 0x140687d00 | 0x687d00 |

### OtherInventoryTypeDataModel (9 functions)

| Function | Address | RVA |
|----------|---------|-----|
| CampVendingMachineInventoryTransferEvent | 0x141bc2040 | 0x1bc2040 |
| ContainerInteractionMsg | 0x1420b7b60 | 0x20b7b60 |
| MenuOpenCloseEvent | 0x140686ef0 | 0x686ef0 |
| PlayerTradeAcceptFail | 0x1417ceab0 | 0x17ceab0 |
| PlayerTradeEnd | 0x140686ef0 | 0x686ef0 |
| PlayerVendingBegin | 0x140686ef0 | 0x686ef0 |
| ProcessEvent | 0x1435cabd0 | 0x35cabd0 |
| UpdateSlotData | 0x14189b050 | 0x189b050 |
| VendorSnapshotData::PSRPreREFR | 0x141ae9790 | 0x1ae9790 |

### TES (8 functions)

| Function | Address | RVA |
|----------|---------|-----|
| GridArrayLoad | 0x143136ee0 | 0x3136ee0 |
| LoadAndAttachInteriorCell | 0x140d8c6b0 | 0xd8c6b0 |
| LoadExteriorCell | 0x143ac467a | 0x3ac467a |
| LoadGridCell() | 0x1408ff419 | 0x8ff419 |
| LoadInterior | 0x14129ebe6 | 0x129ebe6 |
| LoadedAndAttachInteriorCell | 0x140d8c6b0 | 0xd8c6b0 |
| RunAnims | 0x1417ceab0 | 0x17ceab0 |
| SetWorldSpace | 0x14214e260 | 0x214e260 |

### BSResource (8 functions)

| Function | Address | RVA |
|----------|---------|-----|
| GlobalLocations::DoCreateAsyncStream | 0x140848290 | 0x848290 |
| GlobalLocations::DoCreateStream | 0x140848290 | 0x848290 |
| GlobalLocations::Traverse | 0x14069fbf0 | 0x69fbf0 |
| GlobalPaths::DoCreateAsyncStream | 0x140848290 | 0x848290 |
| GlobalPaths::DoCreateStream | 0x140848290 | 0x848290 |
| GlobalPaths::Traverse | 0x14065ae00 | 0x65ae00 |
| LocationTree::DoCreateAsyncStream | 0x143489420 | 0x3489420 |
| LocationTree::DoCreateStream | 0x143489420 | 0x3489420 |

### LoggingSystem (8 functions)

| Function | Address | RVA |
|----------|---------|-----|
| DEV::game.guid | 0x141244cf2 | 0x1244cf2 |
| DEV::game.hotloading | 0x141244cf2 | 0x1244cf2 |
| DEV::game.misc.fow-setting-enum | 0x141244cf2 | 0x1244cf2 |
| DEV::game.misc.statsd | 0x142314ae0 | 0x2314ae0 |
| PROD::game.guid | 0x141244cf2 | 0x1244cf2 |
| PROD::game.hotloading | 0x141244cf2 | 0x1244cf2 |
| PROD::game.misc.statsd | 0x142314ae0 | 0x2314ae0 |
| PROD::game.network.componentFactory | 0x142314ae0 | 0x2314ae0 |

### Workshop (7 functions)

| Function | Address | RVA |
|----------|---------|-----|
| CreateWall | 0x141d06890 | 0x1d06890 |
| DestroyWall | 0x1438ca738 | 0x38ca738 |
| ExtraData::CreateWall Called. | 0x141d06890 | 0x1d06890 |
| ExtraData::DestroyWall Called. | 0x1438ca738 | 0x38ca738 |
| UpdateCellAttachment::CaptureBorders | 0x14117b0e0 | 0x117b0e0 |
| UpdateCellAttachment::CellAttached | 0x141a28b20 | 0x1a28b20 |
| WouldSnapFromDistance | 0x142917d50 | 0x2917d50 |

### CELL (7 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AttachToWorld | 0x140ede1b0 | 0xede1b0 |
| ChangeProcessLevel | 0x141c09390 | 0x1c09390 |
| ClearReference3D | 0x1435cd720 | 0x35cd720 |
| LoadTempDataFromFile | 0x1434e04c0 | 0x34e04c0 |
| RunAnimations | 0x14140cb00 | 0x140cb00 |
| UpdateActivateParents | 0x1420c6a00 | 0x20c6a00 |
| UpdateHavokCamera | 0x142c77910 | 0x2c77910 |

### Social (7 functions)

| Function | Address | RVA |
|----------|---------|-----|
| Lobby::GetLobby | 0x142a2aa90 | 0x2a2aa90 |
| Lobby::GetLobby - Members: | 0x142a2aa90 | 0x2a2aa90 |
| Lobby::JoinLobby - Join Lobby request sent | 0x14162a6f4 | 0x162a6f4 |
| Lobby::KickError - Error sending kick. Not lobby leader. | 0x14169b446 | 0x169b446 |
| Lobby::LeaveLobby - Left the Lobby | 0x141fb3444 | 0x1fb3444 |
| Lobby::LostLeadership - This client is no longer the lobby leader | 0x1434d00c0 | 0x34d00c0 |
| Lobby::MessageError - Attempted to send member message to the local client. | 0x142360188 | 0x2360188 |

### WorkshopClient (6 functions)

| Function | Address | RVA |
|----------|---------|-----|
| MultiEditHelper ::ResolveMustSnapItems | 0x142c77910 | 0x2c77910 |
| MultiEditHelper::PreStackItem | 0x141bbcff0 | 0x1bbcff0 |
| MultiEditHelper::PrepareBlueprintPackin | 0x140c91a60 | 0xc91a60 |
| MultiEditHelper::SetupPlacementValues | 0x141ab5480 | 0x1ab5480 |
| PrepareReferences | 0x140811290 | 0x811290 |
| TestBlueprintSupport | 0x140c91a60 | 0xc91a60 |

### BasePlayerCharacter (6 functions)

| Function | Address | RVA |
|----------|---------|-----|
| NotifyLeftCombatGroup | 0x14216c9d0 | 0x216c9d0 |
| SetGodMode | 0x14216c9d0 | 0x216c9d0 |
| SetVATSCriticalCharge | 0x1406eb7a0 | 0x6eb7a0 |
| SetVisitorType | 0x14216c9d0 | 0x216c9d0 |
| Update | 0x141cf33c0 | 0x1cf33c0 |
| Update::UpdateCollisionState | 0x1429232d9 | 0x29232d9 |

### InstancedCellManager (5 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AccessRemapperFn | 0x14068a1c0 | 0x68a1c0 |
| CloneCell | 0x142000620 | 0x2000620 |
| CreateInstancedCell | 0x14310eef0 | 0x310eef0 |
| ForEachLoc | 0x140bcdf00 | 0xbcdf00 |
| GenerateRefIDMapper::bDebugCellInstancing | 0x1412b1980 | 0x12b1980 |

### PipboyPlayerInfoData (5 functions)

| Function | Address | RVA |
|----------|---------|-----|
| FillArmorData | 0x142b72c40 | 0x2b72c40 |
| FillCarryWeightData | 0x1435468f0 | 0x35468f0 |
| FillGoldData | 0x142991d70 | 0x2991d70 |
| FillHPGainData | 0x1402152a3 | 0x2152a3 |
| FillWeaponData | 0x1418a95c0 | 0x18a95c0 |

### ProcessLists (5 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AddReference::SkippingBecauseInstanced | 0x142027d70 | 0x2027d70 |
| AddReferenceUnique::SkippingBecauseInstanced | 0x141874690 | 0x1874690 |
| QueueActorTransformWithFootIKResults | 0x142a848d0 | 0x2a848d0 |
| UpdateClient | 0x142c339f0 | 0x2c339f0 |
| UpdateMagicEffects | 0x140848290 | 0x848290 |

### BSTextureStreamer (5 functions)

| Function | Address | RVA |
|----------|---------|-----|
| HandleLoadRequest | 0x140ed1720 | 0xed1720 |
| HandleModifyRequest | 0x1438d9340 | 0x38d9340 |
| HandleUpgradeLoadRequest | 0x141fbcee0 | 0x1fbcee0 |
| Schedule | 0x141783c1a | 0x1783c1a |
| WaitForStreamedHandle | 0x140b0efc0 | 0xb0efc0 |

### BSClusterRenderer (5 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AppendIndices | 0x14172fb80 | 0x172fb80 |
| DoCullingAndPrepareForRendering | 0x1412b9990 | 0x12b9990 |
| GatherToUnifiedBuffer | 0x142c582b0 | 0x2c582b0 |
| GenerateBoundingSphere | 0x1412b9990 | 0x12b9990 |
| RenderClusters | 0x140d68110 | 0xd68110 |

### ExteriorCellLoader (5 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AttachLoadedCell | 0x1409b1050 | 0x9b1050 |
| CancelAllCellLoads | 0x1438ca738 | 0x38ca738 |
| FinishLoadingAllQueuedCells | 0x1438ca738 | 0x38ca738 |
| LoadCellData | 0x142a2ee50 | 0x2a2ee50 |
| RemoveCell | 0x1427357bb | 0x27357bb |

### ObjectREFRNetworkEntity (5 functions)

| Function | Address | RVA |
|----------|---------|-----|
| DetachTESObjectREFR | 0x1420096e0 | 0x20096e0 |
| MarkNetCreated canceling delete | 0x140957dc0 | 0x957dc0 |
| NetDelete | 0x143411c70 | 0x3411c70 |
| ProcessPendingNetDelete from game | 0x140957dc0 | 0x957dc0 |
| ProcessPendingNetDelete from network | 0x140957dc0 | 0x957dc0 |

### TESDataHandler (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| CompileFiles | 0x140f4ff00 | 0xf4ff00 |
| ConstructObject | 0x141abbf00 | 0x1abbf00 |
| CreateReferenceAtLocation | 0x140c91f40 | 0xc91f40 |
| UnloadCell | 0x140741830 | 0x741830 |

### BGSGrassManager (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AddCellGrass | 0x1420256f0 | 0x20256f0 |
| AddCellGrass::CreateGrassPoissonDiskSample | 0x140950560 | 0x950560 |
| LoadGrassType | 0x14202a3f0 | 0x202a3f0 |
| ProcessAttachQueue() | 0x141ab6750 | 0x1ab6750 |

### TESQuestInstance (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AddPlayerToActiveArray | 0x1413764d0 | 0x13764d0 |
| FillAliases | 0x141876140 | 0x1876140 |
| FindRefsForAlias | 0x143137940 | 0x3137940 |
| GetAllMatchingInfosHelper | 0x141cb6bf0 | 0x1cb6bf0 |

### BGSTerrainManager (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| RunUpdate | 0x1420b7b60 | 0x20b7b60 |
| RunUpdate_CellGridShift | 0x141fdf980 | 0x1fdf980 |
| SetClipVolume | 0x141ccc5a0 | 0x1ccc5a0 |
| UpdateLODLighting | 0x140b86df0 | 0xb86df0 |

### PowerArmor (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| EndWorkbenchInteraction | 0x141a28a70 | 0x1a28a70 |
| HandleFailedInteractionPowerArmorWorkbench | 0x141a28b20 | 0x1a28b20 |
| PowerArmorWorkBenchExitComplete | 0x14202f530 | 0x202f530 |
| PreloadSwitchToPowerArmor | 0x141819700 | 0x1819700 |

### ActorEquipManager (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| EquipFirstEqual | 0x1438f39e0 | 0x38f39e0 |
| EquipItem | 0x140d6e960 | 0xd6e960 |
| UnequipItem | 0x140d6e960 | 0xd6e960 |
| UseItem | 0x14202e7b0 | 0x202e7b0 |

### VirtualMachine (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AddPendingVariableUpdate | 0x14177cc40 | 0x177cc40 |
| DispatchMethodCallImpl | 0x142db9d30 | 0x2db9d30 |
| FindBoundObject | 0x14065aa40 | 0x65aa40 |
| FindBoundObjectImpl | 0x143975b60 | 0x3975b60 |

### BSPrecomputedVisibility (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| BuildShadowCullerJob | 0x141a12fb0 | 0x1a12fb0 |
| CombineStaticQueryResults | 0x141a12fb0 | 0x1a12fb0 |
| ShadowCullerBuilder::Build | 0x1419b4900 | 0x19b4900 |
| ShadowCullerBuilder::Setup | 0x1430f4f90 | 0x30f4f90 |

### EntityManager (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AddPlayerHelper player id [ | 0x14063e850 | 0x63e850 |
| AddTESObjectREFRHelper entity id [ | 0x14063e850 | 0x63e850 |
| ForEachPlayer | 0x14151ed10 | 0x151ed10 |
| GetEntity | 0x14169ded0 | 0x169ded0 |

### UI (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| Assert | 0x143577d50 | 0x3577d50 |
| FinishLoadingMovie | 0x142c582b0 | 0x2c582b0 |
| Trace | 0x1408eda30 | 0x8eda30 |
| Warning | 0x1416653a0 | 0x16653a0 |

### PC (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| Resurrect | 0x1409b62e0 | 0x9b62e0 |
| Update | 0x141cf33c0 | 0x1cf33c0 |
| UpdateActor3DPosition | 0x142fafa20 | 0x2fafa20 |
| UpdateAnimation | 0x140b86df0 | 0xb86df0 |

### Game (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| TESObjectREFR::All::SnapshotContents::SSyncedVariable::ScriptKey | 0x143ac4670 | 0x3ac4670 |
| TESObjectREFR::All::SnapshotContents::TESObjectREFRServerAuthSnapshotData | 0x142caad20 | 0x2caad20 |
| TESObjectREFR::Selected::SnapshotContents::SSyncedVariable::ScriptValue | 0x140e22756 | 0xe22756 |
| TESObjectREFR::Selected::SnapshotContents::TESObjectREFRServerAuthSnapshotData | 0x142caad20 | 0x2caad20 |

### CullingJob (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| Accum | 0x141fe1300 | 0x1fe1300 |
| BatchCullP1Arena | 0x141fe1300 | 0x1fe1300 |
| BatchProcessCuller | 0x141fe1300 | 0x1fe1300 |
| BatchProcessNodeCuller | 0x141fe1300 | 0x1fe1300 |

### PerkEntryVisitor (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| FanFareEntryPointVisitor | 0x141e8cc10 | 0x1e8cc10 |
| HandleEntryPointVisitor | 0x14290fa60 | 0x290fa60 |
| ListAllPerkEntryVisitor | 0x14278f620 | 0x278f620 |
| RenderPerkEntryArraysVisitor | 0x140741830 | 0x741830 |

### GroupMatchmakingManager (4 functions)

| Function | Address | RVA |
|----------|---------|-----|
| GetTeamMembersWithPermission Unable to find account [ | 0x1427da890 | 0x27da890 |
| OnWorldJoinInviteResponseReceived received response from an account that was not pending. | 0x140401d7a | 0x401d7a |
| SetPermissionsKey Failed to set PermissionsKey | 0x142ca2170 | 0x2ca2170 |
| Update determined time ran out on the invite. | 0x1427b26b0 | 0x27b26b0 |

### ModelLoader (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| ClearUnusedModels | 0x142c59150 | 0x2c59150 |
| QueueReference | 0x14181a040 | 0x181a040 |
| UpdateAttachDistant3DQueue | 0x140b0efc0 | 0xb0efc0 |

### BGSCombinedCellGeometryDB (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| DeferredPreload | 0x14391f9e0 | 0x391f9e0 |
| ModelDB::Create | 0x140560f80 | 0x560f80 |
| RequestPreload | 0x143975b60 | 0x3975b60 |

### CellLoaderTask (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| Cancel | 0x141a28a70 | 0x1a28a70 |
| Finish | 0x141efd430 | 0x1efd430 |
| Run | 0x140ae4df0 | 0xae4df0 |

### TESWorldSpace (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| FindCellInFile | 0x14040b6d5 | 0x40b6d5 |
| LoadCell | 0x1428972f0 | 0x28972f0 |
| RemoveFromPersistentRefData | 0x141ab6750 | 0x1ab6750 |

### ActorUtils (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| ForEachPlayerWithinRange | 0x1409990c0 | 0x9990c0 |
| ForEachRelevantHighProcess | 0x141fbe1d0 | 0x1fbe1d0 |
| ForEachRelevantPlayer | 0x1407fbe31 | 0x7fbe31 |

### BGSStoryTeller (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| BeginShutDownQuest | 0x140769b40 | 0x769b40 |
| BeginStartUpQuest | 0x1409aec40 | 0x9aec40 |
| PushUpdateEventsFromChanges:OnPreFlushFunc | 0x141787130 | 0x1787130 |

### QuestTrackerDataModel (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| SynchronizeObjectives | 0x1416a25d0 | 0x16a25d0 |
| UpdateDataModel | 0x14393cc50 | 0x393cc50 |
| UpdateProvider | 0x142c582b0 | 0x2c582b0 |

### PerkVisitor (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| ExportProgressDataPerkVisitor | 0x141fdf980 | 0x1fdf980 |
| NotifyPerksOnLoad | 0x140a085d0 | 0xa085d0 |
| RenderPerkVisitor | 0x14158e4b0 | 0x158e4b0 |

### StormWallManager (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| RunAnimations | 0x14087181a | 0x87181a |
| UpdateEffects | 0x141ac00c0 | 0x1ac00c0 |
| UpdateGeometryFromRadius | 0x140523310 | 0x523310 |

### InventoryDataModel (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| FlushRemoveQueue | 0x141b96f40 | 0x1b96f40 |
| PopulateItem | 0x141ffe4d0 | 0x1ffe4d0 |
| ProcessEvent::BGSInventoryListEvent | 0x141716200 | 0x1716200 |

### HUDDataModel (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| QueueNotification | 0x14331d900 | 0x331d900 |
| UpdateCompassModel::CompassMarkerFunctor.ClearParamList | 0x140659c05 | 0x659c05 |
| UpdateHUDModels | 0x14202dc4d | 0x202dc4d |

### ExamineMenu (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AdvanceMovie | 0x1404ac7a0 | 0x4ac7a0 |
| CalculateKnownModsStatus | 0x142022820 | 0x2022820 |
| MovieLoaded | 0x142022820 | 0x2022820 |

### ActiveEffectManager (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| ForEachActiveEffect | 0x14203c930 | 0x203c930 |
| GenerateUniqueActiveEffectID.Wrapped | 0x141716200 | 0x1716200 |
| RegisterActiveEffect | 0x143ac3ec0 | 0x3ac3ec0 |

### ClientInventoryMutator (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| AddItem | 0x142360188 | 0x2360188 |
| SendEvent | 0x1409b12b0 | 0x9b12b0 |
| SetEquipped | 0x14148f440 | 0x148f440 |

### SnapshotFollowingPlannerHandlerAgent (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| PerformMovementPlanning | 0x140adc100 | 0xadc100 |
| UpdateSmallDelta_Handler | 0x1422c4d1c | 0x22c4d1c |
| UpdateSmallDelta_Planner | 0x140887290 | 0x887290 |

### Umbra (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| ProcessMultiStreamInstanceShadows | 0x141cb6bf0 | 0x1cb6bf0 |
| ProcessTopFadeNode | 0x142030c20 | 0x2030c20 |
| Query::Lights | 0x1435cabd0 | 0x35cabd0 |

### BGSLODTerrainManager (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| SetupNodeHierarchy | 0x141af5100 | 0x1af5100 |
| UpdateClipmaps | 0x1435cd720 | 0x35cd720 |
| UpdateDB | 0x1427588e0 | 0x27588e0 |

### GlobalChanges (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| SetValue::Console | 0x141c29590 | 0x1c29590 |
| SetValue::InitialValue | 0x141c29590 | 0x1c29590 |
| SetValue::Script | 0x141c29590 | 0x1c29590 |

### HubDataModel (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| ProcessEvent::InitialClientInfoMsg_Execute | 0x1438ca738 | 0x38ca738 |
| ProcessEvent::ResetFromBabylon_Event | 0x1438ca738 | 0x38ca738 |
| ProcessEvent::ResetFromQuickplay_Event | 0x1438ca738 | 0x38ca738 |

### MagicTarget (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| CheckAddEffect | 0x1416653a0 | 0x16653a0 |
| HandleAddActiveEffect | 0x140f1b120 | 0xf1b120 |
| UpdateTarget | 0x141f37d50 | 0x1f37d50 |

### BGSSaveLoadGame (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| LoadCell | 0x141cf33c0 | 0x1cf33c0 |
| RevertGlobalData | 0x141715524 | 0x1715524 |
| SaveGlobalData | 0x141656be7 | 0x1656be7 |

### MovieImpl (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| Advance | 0x14355e410 | 0x355e410 |
| GetTopMostEntity | 0x1430a4380 | 0x30a4380 |
| ProcessUnloadQueue | 0x14119fea0 | 0x119fea0 |

### BNetWebsocket (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| Connect: Failed to parse websocket address | 0x1420e0100 | 0x20e0100 |
| Connect: Initialize failed setup | 0x1408686c2 | 0x8686c2 |
| Shutdown: called | 0x1434d00c0 | 0x34d00c0 |

### IAnimationGraphManagerHolder (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| CreateAnimationGraph | 0x14113ca10 | 0x113ca10 |
| CreateAnimationGraphManager | 0x141716200 | 0x1716200 |
| SetGraphVariableHelper | 0x142b6f7e0 | 0x2b6f7e0 |

### BSCoreMessage (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| DoWarning | 0x14082c750 | 0x82c750 |
| VSend | 0x14082c750 | 0x82c750 |
| Warning | 0x14112cec0 | 0x112cec0 |

### BSScaleformManager (3 functions)

| Function | Address | RVA |
|----------|---------|-----|
| FinalizeMovieLoad | 0x14290b7f0 | 0x290b7f0 |
| LoadMovieDef | 0x140686ef0 | 0x686ef0 |
| StartMovieLoad | 0x1423d1c60 | 0x23d1c60 |
