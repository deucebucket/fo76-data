# FO76 Finding 029: Unreleased, Disabled, and Hidden Quests from QUST Records

**Source**: `QUST_records.txt` (260,411 lines, 2,200 total quest records)
**Method**: Systematic search for CUT_, zzz_, ZZZ_, test/debug prefixes, high Form IDs, and content keywords
**Date**: 2026-03-20
**Cross-referenced**: Existing findings 000-027, Fallout Wiki, Nuka Knights

---

## Summary Statistics

- **Total QUST records**: 2,200
- **CUT_ prefixed quests**: 48 unique quest entries
- **zzz_/ZZZ_ prefixed quests**: 32 unique quest entries
- **Test/Debug quests**: 30+ developer quests still in the ESM
- **Highest Form IDs (newest content)**: 0x008A4xxx range (QDLBarbara lesson chain)

---

## Category 1: CUT Wastelanders Community Quests (Previously Undocumented)

These quests were built for the Wastelanders expansion (W05 prefix) but never shipped. They represent a **cut community faction system** at Foundation.

| Form ID | Editor ID | Notes |
|----------|-----------|-------|
| 0x00555A72 | CUT_W05_Community_Treehouse_Village_Quest | Full quest with FULL name, DESC, event data triggers, multiple dialogue stages |
| 0x00558E32 | CUT_W05_Community_RaiderBlockade_Quest | Raider siege event at a settlement |
| 0x003F514C | CUT_W05_MQS_201P_MotherlodeWave | Motherlode wave defense scenario — cut from the Motherlode quest chain |
| 0x005C8B50 | CUT_BS01_Dialogue_TreehouseVillage | Full combat dialogue for Treehouse Villagers (16+ combat bark types: taunt, suppressive fire, retreat, flank, cover, etc.) |

**What this reveals**: Wastelanders originally had a "Community" system where players could interact with settlements like the Treehouse Village. There was a raider blockade defense event and a Motherlode wave-defense mission. The Treehouse Villagers had full combat AI dialogue (16 combat bark categories), meaning they were meant to fight alongside the player. This system was stripped down to what shipped as simple Foundation/Crater reputation quests.

**Novelty assessment**: The Treehouse Village quest and Raider Blockade quest are not documented on the Fallout Wiki's cut content page. The Motherlode wave quest is mentioned only in passing. The full combat dialogue system for Treehouse Villagers (with marsupial-detection hellos) is novel.

---

## Category 2: Six Cut Settler Daily Quests (zzz_ Disabled)

Foundation originally had **six daily quests**, all disabled with zzz_ prefix:

| Form ID | Editor ID | Activity |
|----------|-----------|----------|
| 0x003F28CC | zzz_W05_SettlersDaily_Painting | Art/painting task |
| 0x003F2DC7 | zzz_W05_SettlersDaily_Clinic | Medical clinic work |
| 0x003F2DC9 | zzz_W05_SettlersDaily_Stew | Cooking stew |
| 0x00403436 | zzz_W05_SettlersDaily_Fieldhand | Farming/fieldwork |
| 0x0041B725 | zzz_W05_SettlersDaily_Restock | Supply restocking |
| 0x00541685 | zzz_W05_SettlersDaily_Secret | Secret mission with branching endings (Davie ending, Elsie optional path) |

Each has its own dialogue scene (Scene1). The "Secret" daily has the most complexity — it has **two named NPCs (Davie and Elsie)** with branching outcomes.

**Novelty assessment**: These six cut dailies are partially known to dataminers but the "Secret" daily with its branching Davie/Elsie endings has not been publicly analyzed. The full scope of six planned dailies versus the two that shipped (Retirement Plan/Photo Opportunity) is underdocumented.

---

## Category 3: Cut Wayward Bar Conversations (Jide & Gracie)

Three cut random conversations at The Wayward tavern:

| Form ID | Editor ID | Topic |
|----------|-----------|-------|
| 0x0042ECD4 | CUT_W05_DialogueWaywardRC_JideGracie_Gift | Gift-giving conversation |
| 0x0042ECD5 | CUT_W05_DialogueWaywardRC_JideGracie_Mort | Discussion about "Mort" (character or death?) |
| 0x0042ECD8 | CUT_W05_DialogueWaywardRC_JideGracie_ToadSteaks | Toad steak cooking discussion |

These are ambient bar conversations between Jide and Gracie that would have played at The Wayward. The "Mort" conversation is intriguing — this could reference a cut NPC or be about death/mortality.

**Novelty assessment**: Not documented anywhere. Minor flavor content but shows the Wayward was meant to feel more alive with random NPC conversations.

---

## Category 4: Cut Vault Raid System (V63, V94, V96)

The vault raid system was famously cut, but the quest records reveal the **full scope** of what was planned:

### Vault 94 (Partially shipped, then removed)
| Form ID | Editor ID | Status |
|----------|-----------|--------|
| 0x0005A240 | V94_1 | Shipped then removed |
| 0x0005A241 | CUT_V94_3_OLD | Old version of mission 3 |
| 0x0005A242 | CUT_V94_2_OLD | Old version of mission 2 |
| 0x0014DF31 | CUT_V94_3_Escape_OLD | Escape sequence cut from mission 3 |
| 0x0046B531-34 | CUT_V94_1_Repair/Access/Reactor/Reset | Four sub-missions within V94 mission 1 |
| 0x00482D60 | CUT_V94_2_Scenes_OLD | Cut scene package |

### Vault 96 (Planned, cut before release)
| Form ID | Editor ID | Status |
|----------|-----------|--------|
| 0x0032411E | CUT_V96_2_CUT | Mission 2 — double CUT prefix |
| 0x0032411F | CUT_V96_1_CUT | Mission 1 |
| 0x00324120 | V96_Access_CUT | Access quest |
| 0x00324121 | V96_CUT | Main quest |
| 0x00324122 | V96_3_CUT | Mission 3 |

V96 had genetics/biology logs (GeneticsLog01-03, BiologyLog01), a welcome holotape, a meeting scene, and a mission scene — a full 3-mission vault raid about genetic experiments.

### Vault 63 (Planned as raid, became Skyline Valley)
| Form ID | Editor ID | Status |
|----------|-----------|--------|
| 0x003241AC | V63_CUT | Main quest — repurposed for Skyline Valley |
| 0x003241AD | V63_1_CUT | Mission 1 |
| 0x00335396 | V63_3_CUT | Mission 3 |
| 0x00335397-99 | V63Access_1/2/3_CUT | Three access quests |
| 0x003241AC | V63_2_CUT | Mission 2 |

All three vaults were planned as a unified 3-mission raid system. V96 was about genetics. V63 was about an unspecified experiment. V94's GECK containment and vote system survive in the data.

**Novelty assessment**: The vault raids are well-known as cut content. However, the V94_1_Repair/Access/Reactor/Reset sub-quest structure and V96's genetics theme are less documented. The full 3x3 raid matrix (3 vaults x 3 missions each = 9 total raid missions) has not been clearly laid out before.

---

## Category 5: Cut Global Quest - "Invasion" System

| Form ID | Editor ID | Notes |
|----------|-----------|-------|
| 0x003CF449 | CUT_GQ_Invasion | Global quest under `System & Global\Global\` filter. Stage text: "Cleared location 01" |

This was a **server-wide invasion event** where locations would be attacked and players needed to clear them. It sits adjacent to `Nuke_Master` in the quest list (the nuke launch system), suggesting it was a high-level endgame event. The "GQ" prefix (Global Quest) means it would have affected all players on the server simultaneously.

**Novelty assessment**: Not documented on cut content pages. A global invasion system is a significant gameplay concept that was abandoned.

---

## Category 6: Cut Scorchbeast Queen Master Quest

| Form ID | Editor ID | Notes |
|----------|-----------|-------|
| 0x0043D032 | CUT_SFZ03_Queen_MasterQuest | 22 aliases (0x16), SFZ03BossEligiblePlayers tracking |

The Scorchbeast Queen fight originally had a **master quest** tracking eligible players. This suggests there was a more complex qualification system — not every player on the server could participate. The current Scorched Earth event lets anyone join. This master quest would have gated participation somehow.

**Novelty assessment**: The existence of player eligibility tracking for the Queen fight is novel. It implies a planned progression gate (level? quest completion?) that was removed to make the event more accessible.

---

## Category 7: Cut Power Plant and Factory Quests

| Form ID | Editor ID | Notes |
|----------|-----------|-------|
| 0x003E7F1E | CUT_PowerPlantStartup | Under `\Power Plant\` filter, startup sequence |
| 0x00241430 | CUT_Factory_GraftonSteel | Quest variables: BlastFurnaceCount, BlastFurnaceRepaired |

Grafton Steel was originally a **repairable factory** where you'd fix blast furnaces. The power plant startup quest was a separate quest from the existing power plant events — suggesting a one-time startup narrative quest rather than the repeatable event.

**Novelty assessment**: The blast furnace repair mechanic for Grafton Steel is novel. The power plant startup as a distinct quest (vs. the repeatable event) is a minor finding.

---

## Category 8: Burning Springs (BURN_) Cut and Active Content

### Active (shipped) content:
- **Bounty Hunting System**: Burn_BountyHunt_GruntHunt, Burn_BountyHunt_Headhunt, Burn_BountyHunt_Master — with Doc Bonds as NPC bounty giver (1/2/3 star hunts)
- **Rust King Arena**: BURN_SQ01 with full NPC cast (Ava, Eugene, Silas, Rust King) — pre-fight and post-fight phases
- **Side Quests**: Burn_SQ04_DirtyLaundry (Bodhi + Executive confrontation), BURN_SQ02 (Outro parts 1 & 2)
- **Random Encounters**: 8 KK assault encounters, scene encounters, travel encounters
- **The Drifter**: P62_TheDrifter_Quest (boss fight, "Burning Springs\Boss\The Drifter\" filter)
- **Loan Shark**: BURN_SQ02_Dialogue_LoanShark — a loan shark NPC in the Burning Springs story

### Cut/disabled (zzz_ prefixed):
| Form ID | Editor ID | Notes |
|----------|-----------|-------|
| 0x007AE5AC | zzzBurn_RE_Assault_Electrician2 | Cut assault encounter |
| 0x007AE5AD | zzzBurn_RE_FactionAssaultBG01 | Cut faction battle |
| 0x007CFAAD | zzzBurn_TestBountyQuest_TwoStar | Test bounty |
| 0x007CFAAE | zzzBurn_TestBountyQuest_OneStar | Test bounty |
| 0x007D2B3F | zzzBurn_TestBountyEvent_ThreeStar | Test event |
| 0x007D402E | zzzBURN_SQ04_Collectables | Cut collectible quest (SQ04 had a collectible component) |
| 0x007F749F | zzzBurn_BountyHunt_ResetMaster | Cut bounty reset system |
| 0x0081ACCB | zzzBurn_RE_Travel_BountyHunted | Cut "being hunted" reverse-bounty encounter |
| 0x0081ACCE | Burn_RE_Object_LD01 | Random encounter object |
| 0x0081ACCF | zzzBurn_RE_Scene_DeathclawHunter | Cut deathclaw hunter scene |
| 0x0081ACD0 | zzzBurn_RE_Travel_FeralDino | **Cut "Feral Dino" encounter** — suggests a dinosaur-themed feral ghoul variant |
| 0x0081ACD2 | zzzBurn_RE_Scene_GhoulsInGround | Ghouls emerging from ground |
| 0x0081AD0B-11 | zzzBurn_RE_FactionAssault_* | 7 cut faction assault variants (Deathclaw vs Scorpion, RKR vs creatures, etc.) |
| 0x00823683 | zzzBurn_RE_SceneTemplate_Copy01 | Template copy |
| 0x0082446B | zzzBurn_RE_Object_OldCampfire | Cut campfire encounter |
| 0x00824FA0 | zzzBurn_RE_Object_OldCampfire | Duplicate campfire |
| 0x00833F97 | ZZZBurn_RE_Scene_CowardlyRaiders | **Cut "cowardly raiders" scene** — raiders who flee? |
| 0x00834CFD | Burn_RE_Object_GR_01 | Encounter object |
| 0x00836548 | ZZZBurn_RE_Travel_RK01 | Cut travel encounter |
| 0x008447C4 | zzzBurn_RE_Object_GR_02 | Cut encounter object |
| 0x00848625 | ZZZ_Burn_Drive-in_Holotape | **Cut drive-in holotape** — suggests a drive-in theater location had story content removed |

### Novel Burning Springs findings:
1. **"Feral Dino" (zzzBurn_RE_Travel_FeralDino)**: A cut creature encounter referencing a dinosaur-like feral. This could be related to the RadHog (already identified) or an entirely separate creature concept.
2. **"Cowardly Raiders" (ZZZBurn_RE_Scene_CowardlyRaiders)**: Raiders with a fleeing behavior — a personality variant cut from random encounters.
3. **Drive-in Holotape**: A story holotape associated with a drive-in theater location was cut.
4. **BountyHunted reverse encounter**: Players could be hunted BY bounty hunters, creating a pursued-by-NPCs scenario.
5. **SQ04 Collectables**: The Dirty Laundry quest (SQ04) originally had a collectible component that was stripped out.

---

## Category 9: QDLBarbara — The Highest Form ID Quest Chain (Potentially Unreleased Future Content)

The absolute newest content in the ESM by Form ID (0x008952DF to 0x008A4CED):

| Form ID | Editor ID | Description |
|----------|-----------|-------------|
| 0x008952DF | QDLBarbara_Lesson02 | Lesson 2 — intercom puzzle |
| 0x008A45D6 | QDLBarbara_Lesson03 | Lesson 3 — NPC "Roxie" quest. Steaks delivery. Jenny's daughter. |
| 0x008A45D4 | QDLBarbara_Lesson04 | Lesson 4 — NPC "Marjorie" experiments (Intellectual/Combat/Social) |
| 0x008A45D8 | QDLBarbara_Lesson05 | Lesson 5 — Marjorie's basement, "Gene" unlocked |
| 0x008A45D9 | QDLBarbara_Lesson06 | Lesson 6 — Arena fight, Poseidon boss, boat destruction, BasketCount variable |

### Key details:
- **Lesson 03**: NPC named **Roxie** who was grounded/locked up. Player delivers steaks. References Jenny (Roxie's mom). Roxie has lines about "long arms," "smelly head," "injustice," and "you got this." She gives a reward.
- **Lesson 04**: NPC named **Marjorie** with three experiment types: Intellectual, Combat, Social. Has a debug location alias (`Loc_DebugBarbaraF`). Marjorie walks through doors. Mistrust dialogue.
- **Lesson 05**: Marjorie's basement. A "Gene" is unlocked. Basement instance.
- **Lesson 06**: **Arena fight**. Player enters arena. **Poseidon appears** as a boss. A **boat** gets damaged and destroyed. Eddie NPC. Ceremony ending. EBS (Event Broadcast System) for boat damage/destruction/boss death/ceremony end.

### EBS broadcast events in Lesson 06:
- `QDLBarbara_EBS_BossDead` — Boss killed
- `QDLBarbara_EBS_CeremonyEnded` — Ceremony completed
- `QDLBarbara_EBS_BoatDestroyed` — Boat destroyed
- `QDLBarbara_EBS_BoatDamaged` — Boat taking damage
- `QDLBarbara_EBS_Join` — Player joins event

**Novelty assessment**: This is the NEWEST quest content in the entire ESM (highest Form IDs). "QDL" likely means "Quest Dungeon Lesson" — this is a **training dungeon or school** run by someone named Barbara. The Poseidon boss fight with a destructible boat is a completely new event type. The existing findings file 018 noted a "DebugBarbaraF Location" but did not analyze the quest chain. **This is a 5-lesson progressive quest chain culminating in a boss arena event, with named NPCs (Roxie, Marjorie, Eddie, Jenny), branching experiment types, and a Poseidon sea-themed boss fight.** This appears to be upcoming content, not yet released.

---

## Category 10: New Creature Dialogue Systems (High Form IDs)

| Form ID | Editor ID | Notes |
|----------|-----------|-------|
| 0x008279EE | CreatureDialogueRadHog | New creature type — Rad Hog. Under `Dialogue\Generic\` |
| 0x0084FEF8 | CreatureDialogueRoboPawCat | Robotic cat pet — unique VoiceType 0x84FF12 |
| 0x0084FEF9 | CreatureDialogueRobotDog | Robot dog — separate from RoboPaw dog |
| 0x008527FA | CreatureDialogueRoboPawDog | RoboPaw brand robot dog — unique VoiceType 0x84FF13 |
| 0x00868BA1 | CreatureDialogueBigfoot | Bigfoot dialogue (shipped with Backwoods) |

**RoboPaw** is a brand name for robotic pets (cat and dog variants). These share VoiceTypes but are distinct creatures. The RadHog is in `Dialogue\Generic\` under `Burning Springs\Random Encounters\Scenes\`, confirming it's a Burning Springs creature. The Robot Dog (0x0084FEF9) is a SEPARATE entry from the RoboPaw Dog — suggesting there's both a generic robot dog and a branded RoboPaw variant.

**Novelty assessment**: RoboPaw pets are known from Atomic Shop datamines. The RadHog creature dialogue is in existing findings. The distinction between CreatureDialogueRobotDog and CreatureDialogueRoboPawDog (separate entries, same VoiceType) suggests the RoboPaw is a premium/Atomic Shop variant of a generic robot dog.

---

## Category 11: ATX_Quest_LadyLiberty

| Form ID | Editor ID | Notes |
|----------|-----------|-------|
| 0x00869A5B | ATX_Quest_LadyLiberty | ATX prefix = Atomic Shop. Actor alias "Actor_LadyLiberty". 16 INFO records with voiced dialogue. |

A Statue of Liberty-themed NPC with **16 unique dialogue lines** (both hellos and idles), sold through the Atomic Shop. The ATX prefix confirms this is an Atomic Shop item. This is likely a CAMP ally or collectron with a patriotic Lady Liberty persona.

**Novelty assessment**: Known from Atomic Shop datamines.

---

## Category 12: Cut Miscellaneous Quests

| Form ID | Editor ID | Notes |
|----------|-----------|-------|
| 0x000FC7FE | CUT_CreatureDialogueGorilla | Gorilla creature dialogue — "Gorilla idle dialogue. Ignore for export" |
| 0x0035ABF3 | CUT_DONOTUSE_CreatureDialogueDLC03CrRobotRobobrain | Robobrain dialogue marked DO NOT USE |
| 0x00088A9A | zzz_TWZ09 | Toxic Valley quest with baseball announcer dialogue — "Stretch and roll the R in Grrrrrrafton" |
| 0x00437AE8 | zzz_SQ_CustomItemQuest | Custom item naming system — 12 aliases including CB04_CustomItemName |
| 0x004ECC75 | CUT_RE_SceneBB02 | Cut random encounter scene |
| 0x004FC023-2F | CUT_RSVP00/01/03_Quest_Note | Cut Responders questline notes — RSVP00 has "Find Flatwoods" objective |
| 0x006E30D7 | ZZZ_Storm_ST | Cut Skyline Valley (Storm) quest |
| 0x00752278 | ZZZ_XPD_AC_VendorDialogueQuest | Cut Atlantic City vendor dialogue system |

### Notable:
- **CUT_CreatureDialogueGorilla**: Gorillas were planned as creatures in FO76. The developer note says "Ignore for export" — meaning the data was intentionally left but flagged to not ship.
- **zzz_TWZ09**: A Toxic Valley quest involving a baseball announcer. The dialogue directions mention Grafton specifically. This was likely a Grafton event or daily quest themed around baseball.
- **zzz_SQ_CustomItemQuest**: A **custom item naming system** was planned. The CB04 prefix suggests it was part of the C.A.M.P. building system. Players could have named their custom items.
- **CUT_RSVP Quest Notes**: The Responders questline (RSVP00-03) had additional quest note pickups that were cut. These would have provided more lore about the Responders.

---

## Category 13: Developer Test Quests Still in ESM

30+ developer test quests remain in the shipping ESM:

| Pattern | Count | Examples |
|---------|-------|----------|
| TestSmokeQuest00-29 | 22 quests | Automated test suite — each tests different systems |
| DebugKurtQuest/02 | 2 quests | Developer "Kurt" personal test quests with radio scenes |
| DebugCorrieQuest | 1 quest | Developer "Corrie" test with courser test scene, crash test |
| DebugSteveQuest | 1 quest | Developer "Steve" test with radio scenes |
| TestFerret/Quest | 2 quests | "Debug Trace Test 1/2" — tracing system tests |
| TestJayQuest | 1 quest | TestLocation alias |
| TestForMike | 1 quest | Developer "Mike" personal test |
| TestTrevorEvent01 | 1 quest | Event system test |
| TestFakePlayerQuest | 1 quest | Fake player for testing |
| TestDailyQuestForest01 | 1 quest | Daily quest system test |
| TestEMSBossOnDemand | 1 quest | Boss spawning test |
| DebugBadenGQuest | 1 quest | Developer "Baden G" — highest Form ID debug quest (0x8443D) in Burning Springs range |
| Test_SceneCrash | 1 scene | Deliberately tests scene crashes |
| Burn_TestRustKingDialogue | 1 quest | Rust King dialogue test with test scene |

**Notable**: `DebugBadenGQuest` (0x0084433D) is in the **Burning Springs Form ID range**, meaning a developer named Baden was actively testing Burning Springs content. `Test_SceneCrash` is a deliberate crash-testing scene.

---

## Category 14: Cut Event Content

| Form ID | Editor ID | Notes |
|----------|-----------|-------|
| 0x0046F508 | CUT_E01F_Fasnacht_Master | Original Fasnacht enable system — developer note: "OBSOLETE. We used it to enable Fasnacht refs before the content scheduler had the ability to do that." Replaced by SetStaticEnabled in LiveContentPackage Scheduler |
| 0x00620F7B | E07B_Invaders | Active Invaders from Beyond event |
| 0x00630078 | zCUT_E07B_Invaders | Cut Invaders broadcast: "HomerBroadcast_02A_AliensKilled" — Homer had a line for aliens being killed that was cut |

**The Fasnacht developer note** reveals an internal Confluence wiki URL: `https://confluence.zenimax.com:8443/display/P7/Using+the+LiveContentPackage+Scheduler` — confirming ZeniMax uses Confluence for FO76 documentation and the project code is "P7."

---

## Findings Priority (by novelty)

### Tier 1 — Genuinely Novel
1. **QDLBarbara Lesson Chain** (Category 9): 5-lesson progressive quest chain with arena boss fight, named NPCs, and experiment branches. Newest content in the ESM. Not publicly documented.
2. **CUT_GQ_Invasion** (Category 5): Global server-wide invasion event system. Not documented.
3. **CUT_SFZ03_Queen_MasterQuest** (Category 6): Player eligibility tracking for the Queen fight. Not documented.
4. **CUT_W05_Community system** (Category 1): Treehouse Village quest, Raider Blockade, Motherlode Wave. Partially known but scope is novel.
5. **Feral Dino encounter** (Category 8): Cut "FeralDino" creature type in Burning Springs random encounters.

### Tier 2 — Adds Detail to Known Cuts
6. **Six cut settler dailies** (Category 2): Known generally but the "Secret" daily with Davie/Elsie branching is novel.
7. **Vault 96 genetics theme** (Category 4): Known as cut but the genetics/biology focus is underappreciated.
8. **BountyHunted reverse encounter** (Category 8): Being hunted by bounty hunters. Novel gameplay concept.
9. **Custom item naming system** (Category 12): zzz_SQ_CustomItemQuest. Not publicly documented.
10. **Grafton Steel blast furnace repair** (Category 7): Novel mechanic detail.

### Tier 3 — Minor/Supplementary
11. Cut Wayward bar conversations (Category 3)
12. Cut Responders quest notes (Category 12)
13. Gorilla creature dialogue (Category 12)
14. Developer test quest catalog (Category 13)
15. Fasnacht/Confluence internal URL (Category 14)
