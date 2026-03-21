# 070 - Developer Caches, Hidden Objects & Test Content Left in Fallout 76

**Date:** 2026-03-20
**Data sources:** full_esm_dump.txt (1.6M lines), all_refr.tsv (5.1M placed objects), scripts_decompiled/, seventysix_strings_en.txt

---

## 1. QA Test Chests (Placed in Multiple Cells)

the primary result: a full suite of **9 QA testing chests** exists as defined container types, each stocked with every item in a category. These are placed in **at least 7 different interior cells**, with duplicate sets at the same coordinates suggesting multiple instances (likely for instanced interiors or different game modes).

### QA Chest Definitions

| FormID | EDID | Contents |
|--------|------|----------|
| `0x0032CE26` | QAVendorChest | All vendor items |
| `0x001E7DA2` | QAArmorChest | All armor |
| `0x001E7DA4` | QAWeaponChest | All weapons |
| `0x001E7DA6` | QABookChest | All books/notes |
| `0x001E7DA9` | QAHolotapeGamesChest | All holotape games |
| `0x001E7DAF` | QAHolotapesChest | All holotapes |
| `0x001E7DC6` | QAScrapChest | All scrap |
| `0x001E7DC8` | QAConsumableChest | All consumables |
| `0x001E7DC9` | QAMiscComponentChest | All misc components |

### Placed Instances (World Coordinates)

**Set A** (coords ~-2626, -1349 to -2843, -1935 — appears in 4 cell instances):
- REFRs: `0x007299F4`, `0x0083D2AE`, `0x0032CE27`, `0x007D3DFB` (QAVendorChest)
- Full set of 9 chests placed in a line formation

**Set B** (coords ~2104-2321, 1200-1854 — appears in 3 cell instances):
- REFRs: `0x007642E7`-`0x007642EF`, `0x006E91D6`-`0x006E91EF`, `0x0069CD89`-`0x0069CDA2`
- Another full set of 9 chests

**Set C** (coords ~-8346, -19597 to -8563, -20247 — appears in 1 cell):
- REFRs: `0x007B6D92`-`0x007B6DEF`
- Full set of 9 chests

**Standalone placements:**
- `0x0052A592`-`0x0052A5AA`: QAConsumableChest, QAScrapChest, QAMiscComponentChest at coords ~-2205, -951
- `0x003BCB85`: QABookChest at -480, -3429

**Associated quest:** `QAVendorQuest` (`0x0032CE0E`) — a quest that manages the QA vendor alias system.

**Player accessibility:** These are inside interior cells used by developer debug rooms. Not normally accessible in the live game without exploits. However, the sheer number of placements suggests some may exist in cells adjacent to playable spaces.

---

## 2. Developer-Named Debug Containers (Placed in World)

### DebugSteveCDropCrate (Steve C's Test Crates)
- **Base:** `0x004FC3E2` (DebugSteveCDropCrate)
- **Placed in DebugSteveC cell:**
 - `0x004FC3E3` (DebugSteveCDropCrate01) at 2267, 332, 1567
 - `0x004FC3E4` (DebugSteveCDropCrate02) at 1883, 332, 1567
 - `0x004FC3E5` (DebugSteveCDropCrate03) at 1499, 332, 1567
- Script `debugstevecdropcratescript.psc` has empty OnLoad/OnUnload handlers — container behavior only

### DebugKurt Containers
| FormID | EDID | Purpose |
|--------|------|---------|
| `0x0043B928` | DebugKurtGiveOnly | Give-only container (no take) |
| `0x00396BB9` | DebugKurtFilteredContainer01 | Filtered loot container |
| `0x00396BBB` | DebugKurtFilteredContainer02 | Filtered loot container |
| `0x00396BBD` | DebugKurtFilteredContainer03 | Filtered loot container |

### Debug Challenge Containers (Testing Challenge Completion)
| FormID | EDID |
|--------|------|
| `0x00450D66` | DebugChallenges_Chems |
| `0x00450D68` | DebugChallenges_Chems_Ingredients |
| `0x00450D6B` | DebugChallengeFood_Ingredients |
| `0x00450D6D` | DebugChallengeMisc_Junk |
| `0x00450D70` | DebugChallengeFood |
| `0x00450D71` | DebugChallengeMisc_Toys |

These are placed in interior cells and **one (DebugChallengeFood_Ingredients) has a second placement** at REFR `0x007F227C` at coordinates 11759, -16, 2859 — potentially in a live playable cell.

### P01E_Heart_DEBUG (Valentine's Event Debug Container)
- **Base:** `0x0045C4AB`
- **WORLD placement:** `0x0045C4AC` at **143637, 200472, 20526** (PO1E_Heart_Layer)
- This is placed in the open world at the Heart of the Swamp / Valentine's Day event area
- Contains debug items for testing the P01E seasonal event
- Also placed in a cell at `0x0062FA5F`

### Other Test Containers
| FormID | EDID | Notes |
|--------|------|-------|
| `0x0062F776` | TestZachariadisChest | Designer's test chest, placed in cell |
| `0x0062E228` | Test_Pentameter_Footlocker | For "Problems in Pentameter" training quest |
| `0x00621926` | TESTLoot_Toolbox | Test loot generation |
| `0x006127BF` | PROXY_NavM_TEST_STASH_ANIM | Animated stash test |
| `0x005AE93D` | zzzTest_Contextual_AmmoType | Tests ammo type context |
| `0x005A70B3` | Test_Locker | Placed at -824, -1535 |
| `0x0053F193` | TEST_V96CombatTestTrunk | Vault 96 combat testing |
| `0x003D143E` | Test_Drew_Container | Drew's personal test container |
| `0x003D1FAB` | test_QA_Test_Enclave_MK5 | Full Enclave MK5 gear set |
| `0x003D1FA9` | test_QA_Test_BOS_MK5 | Full BOS MK5 gear set |
| `0x003D1FAA` | test_QA_Test_BallisticWeave | Ballistic weave test gear |
| `0x0050FD16` | TestQAArmorheadware | QA headwear test container |
| `0x00368DAF` | TestQAArmorRecipe | Placed in **4 different cells** |
| `0x004E1F46` | TestChest_Caps100 | 100 caps test chest, placed with EDID name "TestChest" |

---

## 3. TestLoot_AmmoBox in Live Expedition Content

**Critical find:** `TestLoot_AmmoBox` (`0x003E0CAF`) is placed in **active Expedition (MILE) content**:
- 4 instances at MILE_HQ_ThemeParent_Military / MILE_Theme_Military layer
 - `0x007711B5` at 513, 4991
 - `0x007711B6` at 486, 5145
 - `0x007711B7` at 488, 5164
 - `0x007711B8` at 490, 5182
- 1 instance at `0x003E0CB1` at 5200, -4504

These ammo boxes with the "Test" prefix are in the military-themed Expedition headquarters. Players running Expeditions may be interacting with what are technically test objects.

---

## 4. Weapon Testing Gym

A dedicated test cell for weapon damage evaluation:

- **Cell:** `0x0065A633` (76WeaponTestingGym)
- **Activator:** `0x006BDBBC` (DebugWeaponTestingGymButton) — controls the gym
- **Damage resistance perks (4 tiers):**
 - WeaponTestingGym_DamageResistPerk1-4 (`0x006BECB3`-`0x006BECB6`)
- **Messages:**
 - WeaponTestingGymMoving (`0x006BECAC`)
 - WeaponTestingGymDamage (`0x006BECAB`)
 - WeaponTestingGymCreature (`0x006BDBBD`)
- **COC Marker:** DevGym_Markers layer (`0x006B7222`) at 768, 1536

### Test Damage Weapons

Purpose-built weapons for precise damage testing:

| FormID | EDID | Damage |
|--------|------|--------|
| `0x005CBA20` | zzz_TESTDMG_10 | 10 |
| `0x005CBA21` | zzz_TESTDMG_30 | 30 |
| `0x005CBA22` | zzz_TESTDMG_60 | 60 |
| `0x005CBA23` | zzz_TESTDMG_100 | 100 |
| `0x005CBA24` | zzz_TESTDMG_150 | 150 |
| `0x005CBA25` | zzz_TESTDMG_200 | 200 |
| `0x005CBA26` | zzz_TESTDMG_300 | 300 |
| `0x005CBA27` | zzz_TESTDMG_400 | 400 |

### Other Test Weapons
| FormID | EDID |
|--------|------|
| `0x005D0638` | zzz_AggDamageTestWeapon |
| `0x006FBA5E` | zzz10mmSMG_ElectricTestingGun |
| `0x007999F4` | zzz_TeslaCannon_NukaLauncherTest |
| `0x005853A3` | zzz_TestGaussShotgunNoCharge |
| `0x004F9016` | zzz_TestThrowingCaltropWeaponMulti |
| `0x008975FF` | zzz_crUnarmedTest01 |

### Test Activators
- `0x002A8D67` TestWeaponFireDummy — weapon fire testing target
- `0x0007EB05` TargetDummy01 — combat target dummy

---

## 5. Developer Debug Cells (322 Total)

**322 debug/test cells** exist in the game data. Many are prefixed with `zCUT` (cut content) but many active `Debug[Name]` cells remain. Notable ones:

### Active Debug Cells (Not zCUT-prefixed)

| FormID | EDID | Developer |
|--------|------|-----------|
| `0x00006F43` | DebugSteveC | Steve C (quest/systems designer) |
| `0x0028D187` | DebugSteveM | Steve M |
| `0x00544975` | DebugSteveM02 | Steve M (second cell) |
| `0x0040BE12` | DebugDobert02 | Dobert (level designer) |
| `0x004E231E` | DebugDobert | Dobert |
| `0x005F0E75` | DebugDobert04 | Dobert (fourth cell) |
| `0x00564B45` | DebugDobert03 | Dobert |
| `0x006781A8` | DebugRyanJohnson | Ryan Johnson |
| `0x0072F440` | DebugRyanJohnson2 | Ryan Johnson |
| `0x006EC234` | DebugRyanJohnsonPOI | Ryan Johnson POI test |
| `0x0060A0B8` | DebugJeffU01 | Jeff U (7 cells: 01-07) |
| `0x003904A7` | DebugStephanieZ | Stephanie Z |
| `0x0062152C` | DebugVeronicaH | Veronica H |
| `0x000922C3` | DebugCBernardo | C Bernardo |
| `0x00018E1D` | DebugCorrie | Corrie |
| `0x005A33C8` | DebugJustinN | Justin N |
| `0x0038F2F8` | DebugJustinM | Justin M |
| `0x00209234` | DebugJamesP | James P |
| `0x0030878F` | DebugJamieC | Jamie C |
| `0x006CD0F1` | DebugGreenScreen | **Chroma key green screen room** |
| `0x006AC521` | DebugHillValley | **Possible Back to the Future reference** |
| `0x007EBC85` | DebugGamejam2025 | **2025 game jam prototype cell** |
| `0x0065A633` | 76WeaponTestingGym | Weapon damage testing facility |
| `0x005350E2` | DebugEllysT | Ellys T |
| `0x005350E3` | DebugCarlM | Carl M |
| `0x00523D14` | DebugCarlM02 | Carl M |
| `0x00383DAA` | DebugRobA | Rob A |
| `0x004101F7` | DebugVictoria | Victoria |
| `0x003C6857` | DebugMJ | MJ |
| `0x003E08F9` | DebugDavidM | David M |
| `0x0043D930` | DebugRussellR | Russell R |
| `0x00468C4C` | DebugChrisM | Chris M |
| `0x005C8EB9` | DebugBrianna | Brianna |
| `0x006C88E9` | DebugFKhan | F Khan |
| `0x006CE265` | DebugDaveB | Dave B |
| `0x006EFE6C` | DebugSamuelC01 | Samuel C |
| `0x0053063A` | DebugMartin | Martin |
| `0x007AD265` | DebugMarkW | Mark W |
| `0x0079A1EF` | DebugJamieR | Jamie R |
| `0x0079B89D` | DebugGRoyer | G Royer |
| `0x007AE870` | DebugAsh | Ash |
| `0x0076A666` | DebugMarkoS01 | Marko S |
| `0x008952E0` | DebugBarbaraF | Barbara F |
| `0x00848C69` | DebugRaihanS | Raihan S |
| `0x007ED9BE` | DebugCKinsey | C Kinsey |
| `0x00713EA2` | DebugVFX | VFX testing room |
| `0x0010D513` | DebugVanityLightStagingCell | Vanity/lighting staging |

### Quest Designer Training Cells

A special **WarehouseQDTraining** system (`0x00116EF6`) exists for training new quest designers:
- Connected to DebugStephanieZ via load door (`0x00629B88`)
- Connected to DebugVeronicaH via load door (`0x00629B89`)
- Contains training quests that teach quest scripting (see Section 8)

---

## 6. Debug/Test Armor (Extensive Collection)

### Debug Power Armor (X-01 Full Set)
| FormID | EDID |
|--------|------|
| `0x0043B322` | zzz_debug_Armor_PowerArmor_X01_Helmet |
| `0x0043B31D` | zzz_debug_Armor_PowerArmor_X01_ArmLeft |
| `0x0043B31E` | zzz_debug_Armor_PowerArmor_X01_ArmRight |
| `0x0043B320` | zzz_debug_Armor_PowerArmor_X01_LegLeft |
| `0x0043B321` | zzz_debug_Armor_PowerArmor_X01_LegRight |

### Debug Legendary Armor Sets
- **Bolstering Combat set** (5 pieces): zzz_Debug_Legendary1_Armor_Combat_*_Bolstering
- **Chameleon Combat Torso**: `0x0048D6EF` zzz_Debug_Legendary1_Armor_Combat_Torso_Chameleon
- **Mutant's Marine set** (5 pieces): zzz_Debug_Legendary2_Armor_Marine_*_Mutants
- **Anti-Scorched Marine**: `0x0043B314` zzz_Debug_Legendary1_Armor_Marine_ArmRight_LessDmgScorched
- **Disarm-on-Melee Combat**: `0x00493164` zzz_Debug_Legendary4_Armor_Combat_Torso_OnMeleeDisarm
- **Weightless Leather**: `0x0043E171` zzz_TEST_Armor_Leather_LegLeft_Legendary1_Weightless

### Debug Regular Armor (Full Sets)
- Complete debug sets for: Combat, Sturdy Combat, Metal, RaiderMod (all body slots)

### ATX Debug Power Armor Skins
- 12 pieces of T-45 debug skins: Raider Marauder and Settler Vigilante variants
- FormIDs: `0x005A3C88` through `0x005A3C93`

### Other Test Armor
| FormID | EDID |
|--------|------|
| `0x008975C0` | zzz_SkinTest01 |
| `0x006F7D84` | ATX_Clothes_CommunistOutfit_Basic_TEST |
| `0x006F7D87` | ATX_Clothes_CommunistAdvanced_TEST |
| `0x0076F46E` | Temp_stub_ARMO_Outfit_Test |
| `0x0076D8C3` | zzzSCORE_Seasons_David_Test6 |
| `0x006820A4` | SkinMechTest |
| `0x00467FA4` | zzz_Test_Armor_BackPack_Default |

---

## 7. Developer Notes & Test Content Shipped in Data

### Placed Debug Notes (In Interior Cells)

| FormID | EDID | Location |
|--------|------|----------|
| `0x005A407B` | DebugJustinN_TestNote01 | Two placements in Justin N's cells |
| `0x005A407C` | DebugJustinN_TestNote03 | At 3656, -7807 |
| `0x005A407D` | DebugJustinN_TestNote02 | At 3400, -7794 |
| `0x005A1A8D` | TestJoshMoretto_Note | In Josh Moretto's cell |
| `0x005A1FEB` | TestJoshMoretto_BookFanfiction | "Fanfiction" book in test cell |
| `0x0042AE35` | DebugDobertNote01 | In Dobert's cell |
| `0x0062A5F4` | Test_Notebook_Formatting | Formatting test note |
| `0x007D70F5` | zzzPlaceholdernote | Literal placeholder note |
| `0x006E3902` | 76StormCDB_TestNote | Storm/Expeditions test note |
| `0x0040D829` | WU_HolotapePlaceholder01 | Placeholder holotape 1 |
| `0x0040D82B` | WU_HolotapePlaceholder02 | Placeholder holotape 2 |
| `0x0066D14B` | zzz_NWOT_Fortune_TEST_Neutral | Nuclear Winter fortune test |

### Debug Terminal
- `0x0064544D` test_CTestTerminalMain_VeronicaHDebug — "This is the Body Text of the CTest Terminal VeronicaHDebug. How's it look?"
- `0x000325C2` "QA Test TERMINAL" — a named QA terminal in the strings

### Quest Skip Debug Entries in Terminal Text
Terminal entries contain debug commands that shipped in the data:
- "DEBUG - Skip to bomb room - coc FortAtlasDungeon01 before using"
- "* DEBUG * Skip to Rose Room"
- "DEBUG: SKIP TO ROSE ROOM FINALE"

These suggest `coc` (Center-on-Cell) teleport commands were left in terminal scripts.

---

## 8. Quest Designer Training Quests (Shipped in Data)

These are training exercises for new BGS quest designers that exist as fully functional quests:

### Veronica Harbison's Training Quests
- `test_VHarbison_Quest` (`0x0062DB8D`)
- `test_VHarbison_Quest_Escape_Room` (`0x0062FA06`) — "Escape The Room" with fuse collection
- `test_VHarbison_A_Friend_In_Need` (`0x00631EC8`) — "A Friend In Need"
- `test_VHarbison_Someone_To_Watch_Over_Me` (`0x0063419D`) — "Someone To Watch Over Me"
- `test_Vharbison_E01RobotRager` (`0x00635BAE`) — "Robot Rager" event

### Stephanie Z's Training Quest
- `Test_Pentameter` (`0x0062E21E`) — "Problems in Pentameter" (described as "Stephanie's training quest")
- `Test_Pentameter_IdleDialogue` (`0x0062E21F`)
- Connected to DebugStephanieZ cell via WarehouseQDTraining

### Zachariadis' Training Quest
- `Test_Zachariadis_Lesson2` (`0x0062F766`)
- `Test_Zachariadis_Lesson2Dialogue` (`0x0062F767`)
- TestZachariadisChest (`0x0062F776`) — placed in cell

### Josh Moretto's Training Quests
- `TestJoshMorettoQuest_01` through `_04` (4 sequential quests)
- Contains NPCs: Rebecca Brandt, Devin Hardway
- Has activators, deposit boxes, book fanfiction, notes
- Two activators placed in world cells

### Other Developer Quests
- `DebugKurtQuest` / `DebugKurtQuest02` — Kurt's debug quests with radio scenes
- `DebugSteveQuest` (`0x0004FAEE`) — Steve's comprehensive bug demonstration quest
- `DebugCorrieQuest` — Corrie's test quest with courser test scene
- `Test_AFinn_Quest01` — A. Finn's quest
- `TestBardQuest` — Bard quest test
- 29+ `TestSmokeQuest` entries (00-29) — systematic smoke testing quests

---

## 9. Nuclear Winter ("Babylon") Remnants

Nuclear Winter's internal codename was "Babylon." Extensive test infrastructure remains:

### Fortune Test Containers
| FormID | EDID |
|--------|------|
| `0x0066D168` | NWOT_FortunesMajor_TestContainer |
| `0x0066D169` | NWOT_FortunesMinor_TestContainer |
| `0x0066D16A` | NWOT_FortunesNeutral_TestContainer |

### Babylon Loot Test Containers (20+ Containers)
| FormID | EDID | Contents |
|--------|------|----------|
| `0x003D0EA0` | zzz_Loot_Babylon_Test | General loot |
| `0x004F5497` | Loot_Babylon_Epic_Weps_Test | Epic weapons |
| `0x004F5496` | zzz_Loot_Babylon_Armor_Test | All armor |
| `0x003A02F4` | zzz_Loot_Babylon_High_Weps_Test | High-tier weapons |
| `0x002FF6B4` | zzz_Loot_Babylon_Med_Weps_Test | Med-tier weapons |
| `0x003FEC29` | Loot_Babylon_Melee_Weps_Test2 | Melee weapons |
| `0x0050D9C2` | Loot_Babylon_Test_Guns | All guns |
| `0x0050D9C1` | zzz_Loot_Babylon_Test_Ammo | All ammo |
| `0x0050D9C3` | zzz_Loot_Babylon_Test_Stims | All stimpaks |
| `0x003A261B` | zzz_Loot_Babylon_Medical_Test | All medical |
| `0x0047EF21` | Loot_Babylon_Bobbleheads_Test | All bobbleheads |
| `0x0047EF22` | zzz_Loot_Babylon_Magazines_Test | All magazines |
| `0x0047C2E6` | zzz_Loot_Babylon_Serums_Test | All mutation serums |
| `0x004F5498` | zzz_Loot_Babylon_Kits_Test | All kits |
| `0x004F5499` | zzz_Loot_Babylon_Melee_Weps_Test | Melee weapons |
| `0x0040609D` | zzz_Loot_Babylon_Holotapes_Test | All holotapes |

### Bot AI Functions (in Debug.psc)
The Debug script class contains Babylon bot AI commands that shipped:
- `Debug.BabylonBotShouldLoot()` — AI decision: should bot loot?
- `Debug.BabylonBotShouldShoot()` — AI decision: should bot shoot?
- `Debug.BabylonBotShouldMove()` — AI decision: should bot move?

These native functions for Nuclear Winter's AI bots remain callable in the script engine.

---

## 10. Developer Signatures & Named References

### Named Developer Objects/Cells
Over **80 unique Bethesda developer names** appear in debug cells and objects:

**Most Prolific (Multiple Cells):**
- **Jeff U** — 7+ cells (DebugJeffU01 through DebugJeffU07GD, plus instanced versions)
- **Dobert** — 4 cells (DebugDobert through DebugDobert04), location records, NPCs, notes
- **Steve C** — Extensive: cell, quest, NPCs, crates, terminals, triggers, assaultrons, radiation hazards
- **Ryan Johnson** — 3 cells (DebugRyanJohnson, DebugRyanJohnson2, DebugRyanJohnsonPOI)
- **Kurt** — Cell, 2 quests, actors (FollowPlayer, ForceGreet, ActorA/B), containers, disconnect quest
- **Carl M** — 2 cells
- **Brent C** — 2 cells
- **Baden G** — 2 cells (including instanced version)
- **Barbara F** — 2 cells (including instanced version)
- **Matt T** — 2 cells

**Named NPCs (Test Characters):**
- `DebugKurtActorFollowPlayer` — an NPC that follows the player
- `DebugKurtActorForceGreet` — an NPC that forces dialogue
- `DebugKurtActorA` / `DebugKurtActorB` — test actor pair
- `DebugKurtActor` — base test actor
- `DebugSteveCProtectron` — Steve C's test Protectron
- `DebugSteveCEyeBot` — Steve C's test Eyebot
- `DebugSteveCLiberatorAggressive` — Aggressive Liberator
- `DebugSteveC_LvlAssaultron_Unaggressive` — Passive Assaultron
- `DebugSteveC_LvlMirelurkCrab_Captive` — Captive Mirelurk
- `DebugDobert02_LvlProtectronConstruction_Hostile` — Hostile Protectron
- `DebugDobert02_CorpseBaseRobotProtectron` — Dead Protectron

### Steve Milner Easter Egg
In-game lore text references a real developer name:
> "We had our first Loss Of Life incident in 7 years. Today at approximately 9:30 AM, **Steve Milner** fell head-first into a smelting vat when an unsecured chain caught his leg and tripped him up."

This appears in a Hornwright Industrial note (FormID `0x0005B8B7`).

---

## 11. Special Interest Cells

### DebugGreenScreen (`0x006CD0F1`)
A chroma key green screen room with:
- `GreenScreen_Background` static (`0x006CD23B`)
- Material swap: `IndFloorToGreenScreen` (`0x006CD0F2`)
- Used for creating promotional screenshots/videos with green screen compositing

### DebugGamejam2025 (`0x007EBC85`)
A **2025 game jam prototype cell** — evidence of Bethesda's internal game jam culture. Game jam assets include:
- `gamejam/whale/whaleexplosion.nif` — an exploding whale model
- `gamejam2017/setdressing/tackycurtains01.bgsm` / `bedazzled01.bgsm` — from 2017 jam

### DebugHillValley (`0x006AC521`)
Possibly a Back to the Future reference ("Hill Valley" is the town from the films). No additional confirming data found, but the name itself is notable.

### DebugVanityLightStagingCell (`0x0010D513`)
A lighting staging cell for vanity/cosmetic item photography.

### Shelter Test Cells
- `zCUTDebugSheltersVaultTestMat01` (`0x005CAAA8`)
- `zCUTDebugShelterszzTestCell` (`0x005A5546`)
- `ShelterWorkshopTest` (`0x005A5548`) — base shelter workshop test
- Multiple shelter entrance snap test storage cells

---

## 12. Debug.psc — The Master Debug Script

The `Debug.psc` script (which ships with the game) exposes powerful native functions:

```
Debug.CenterOnCell(String asCellname) — teleport to any cell by name
Debug.CenterOnWorldAndWait(String worldName, Int x, Int y) — teleport to world coords
Debug.ExecuteServerConsole(String asCommand) — run server console commands
Debug.ExecuteLocalConsole(String asCommand) — run local console commands
Debug.EnableCollisions(Bool abEnable) — toggle collision (noclip)
Debug.QuitGame() — force quit
Debug.PlayerGoTo(String asStrKey) — teleport player
Debug.WorkshopExit() — force exit workshop mode
Debug.WorkshopBuildBlueprintRef(Int aiIndex) — build blueprint
Debug.WorkshopPlaceBlueprintRef(Int aiIndex) — place blueprint
Debug.GetFormsByType(Int type) — enumerate all forms of a type
Debug.AutoTestFire() — trigger automated tests
Debug.AutoTestComplete(Bool abSuccess) — mark test complete
```

These functions are **native** (implemented in C++) and theoretically callable if a player could execute Papyrus scripts.

---

## 13. Invisible Triggers & Hidden Activators

### TestNewCharControlTrigger
- `0x0032DA69` — an activator that controls character creation flow, potentially triggerable

### Fast Travel Terminal Test
- `0x00083A93` test_FastTravelTerminalTest — a test terminal for fast travel

### MODUS Vendor Armory (Test)
- `0x002B802A` TEST_ENB_ModusTerminal_Vendor_Armory — a test version of the Enclave MODUS vendor
- `0x002B8029` TEST_ENB_DialogueFaction_MODUS_Vendor_Armory — faction for the test vendor

### Legendary Test Templates
- `0x001EF488` TestTemplate_effect_mod_LegendaryWeaponListener — listens for legendary effects
- `0x001EF486` TestTemplate_effect_mod_LegendaryWeaponSender — sends legendary effects
- `0x001EF487` TestTemplate_ench_mod_LegendaryWeaponReceiver — receives legendary enchantments

### Infinite Ammo System (Thirst Zapper)
- `0x006873C1` EnchThirstZapperInfiniteAmmo — infinite ammo enchantment
- `0x006873C0` EnchThirstZapperInfiniteWater — infinite water enchantment
- `0x006873C2` ThirstZapper_WaterInfiniteAmmoPerk — the backing perk
- This is the **Thirst Zapper's** infinite ammo system, technically a "shipped" infinite ammo item

---

## 14. Layer Records Revealing Development Structure

### BerkeleySprings_Dev Layer (`0x0018ECCB`)
A development layer for Berkeley Springs content — suggests iterative development layering.

### Dev Layer (`0x0019C1BC`)
A generic "Dev" layer — the broadest development content layer in the game.

---

## 15. Cut Content Adjacent to Live Areas

### Bigfoot References
- `0x00868BAF` BigfootFaction — a faction for Bigfoot entities
- `0x007AC0D6` CUT_Recipe_Workshop_FloorDecor_HerdsmansBell_Bigfoot — cut Bigfoot decorative item
- Bigfoot Beer Stein display exists in Season 24 (`0x008A415A`)

### Cut Valentine's Day Items
- `0x0045C495` CUT_P01E_Heart_HeartShapedBox — placed in world at the event area
- `0x0045C491` CUT_P01E_Heart_Bouquet_NONPLAYABLE — cut weapon
- `0x0045C49A` CUT_P01E_Heart_PerfumeGrenade_NONPLAYABLE — cut grenade weapon
- `0x0045C49C` CUT_Recipe_Weapon_P01E_HeartPerfume — cut recipe, **placed in world**

### Burn/Athens DLC Cut Notes
7 cut notes from the "Burn" Athens update:
- Burn_CUT_AthensBestieLetter, Burn_CUT_AthensNoteSportCar, etc.

### Cut Mutated Events Recipes
6 cut "Mutated Events" infusion recipes (Steel Skin, Poison Cloud, Fiery — Tiers 1-3)

---

## Summary of Highest-Interest Findings

1. **QA Chests in 7+ cells** — Complete item catalog containers placed in multiple debug rooms. Server-side protection likely prevents access, but the data exists.

2. **TestLoot_AmmoBox in live Expeditions** — Test-prefixed ammo containers placed in active MILE content that players interact with during Expeditions.

3. **P01E_Heart_DEBUG in open world** — A debug container placed at world coordinates (143637, 200472, 20526) in the Valentine's event area. If the enable parent allows it, this could theoretically be interactable.

4. **322 developer debug cells** — Including a green screen room, a 2025 game jam cell, weapon testing gym, and quest designer training cells.

5. **Debug.psc native functions** — Server console execution, collision toggle, cell teleportation, and automated testing functions ship in the script engine.

6. **80+ developer names** embedded in object/cell names, constituting a de facto employee directory of the FO76 team.

7. **Nuclear Winter (Babylon) loot test infrastructure** — 20+ test containers with every item type, bot AI functions, and map voting systems remain in the data.

8. **Quest designer training system** — A structured training program (WarehouseQDTraining) with load doors connecting to individual developer cells, complete with training quests assigned to new hires.
