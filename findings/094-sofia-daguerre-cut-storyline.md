# FO76 Finding 094: Sofia Daguerre's Cut Storyline Content -- Deleted Quests, Removed Branches, and Abandoned Mechanics

**Source**: 87 orphaned voice files (Sofia Daguerre), ESM quest records, DELETED_ records, CUT_ records, ilstrings, dlstrings
**Method**: Cross-referencing orphaned Form IDs against ESM QUST records, MISC items, KEYM keys, NPC_ records, PACK packages, SCEN scenes, and string table dialogue
**Date**: 2026-03-21
**Builds on**: Finding 067 (Orphaned Voice Recordings), Finding 068 (Cut Dialogue Reconstruction)

---

## Executive Summary

Sofia Daguerre's companion storyline shipped with 1,362 connected voice lines across a 16-quest arc (intro + 15 radiant fetch/kill quests + camp management + outro). Of her 1,449 total voice files, 87 are orphaned (6.0%), indicating targeted cuts rather than wholesale removal. The cuts reveal **three deleted quest variants**, **two cut vendor conversations**, **a deleted rescue quest system**, **a removed scrap/salvage scene**, **an abandoned intro sequence**, and **a deleted key item** pointing to a lab infiltration quest that was redesigned before shipping.

the primary cut is a **branching rescue quest system** where the player could rescue either A.T.H.E.N.A. or Emerson from robot captors -- a dynamic quest that would have varied based on the player's relationship progression. This mechanic was deleted entirely rather than simplified.

---

## The Shipped Storyline Architecture

Sofia's questline follows the standard Wastelanders companion template:

### Relationship Tiers (controlled by COMP_QuestCount globals)
- **Rank 1: Friendship** -- Initial quests after intro
- **Rank 2: Confidant** -- Mid-story quests, personal revelations
- **Rank 3: Infatuation** -- Late-story quests, romance option
- **Romance** -- Post-infatuation, unlocks romance-specific scenes

### Quest Structure
| Phase | Quest ID | Type | Content |
|-------|----------|------|---------|
| Intro | `COMP_Quest_Intro_Full_Astronaut` (0x0054EB40) | Story | Find Sofia at crash site, recover flight recorder, build USSA console at C.A.M.P. |
| Camp | `COMP_Quest_Camp_Full_Astronaut` (0x0054EB3E) | Hub | Camp dialogue, relationship progression, visitor scenes |
| Radiant 000 | `Astronaut_000_OneSmallStep` | Fetch | Damaged Device |
| Radiant 001 | `Astronaut_001_InCaseOfEmergency` | Fetch | Emergency protocols holotape |
| Radiant 002 | `Astronaut_002_BringHomeTheBeacon` | Fetch | USSA Beacon |
| Radiant 003 | `Astronaut_003_TheUniverseConspires` | Kill | USSA robots |
| Radiant 004 | `Astronaut_004_HopeRemains` | Fetch | Crew remains |
| Radiant 005 | `Astronaut_005_SearchAndDestroy` | Kill | Hostile robots |
| Radiant 006 | `Astronaut_006_HeavyEyes` | Fetch | Whalesong holotape |
| Radiant 007 | `Astronaut_007_PatentlyFalse` | Fetch | Deep Sleeper Pod schematics |
| Radiant 008 | `Astronaut_008_PrivacyViolation` | Fetch | Patient records |
| Radiant 009 | `Astronaut_009_ContractuallyObfuscated` | Fetch | USSA contract |
| Radiant 010 | `Astronaut_010_BootCamp` | Kill | Commander Gutsy robots |
| Radiant 011 | `Astronaut_011_PastExpiration` | Fetch | Experimental serum |
| Radiant 012 | `Astronaut_012_NoBrainer` | Kill | Robobrains |
| Radiant 013 | `Astronaut_013_BrazenBull` | Fetch | Board meeting holotape |
| Radiant 014 | `Astronaut_014_WhoSatDownBesideHer` | Fetch | Arachne MOD holotape |
| Radiant 015 | `Astronaut_015_LabRat` | Fetch | Lab data |
| Outro | `COMP_Quest_Outtro_Full_Astronaut` (0x0056BF31) | Story | Confront A.T.H.E.N.A. at Sugar Grove, deploy Arachne or transfer to Assaultron |

---

## Cut Content Catalog

### 1. DELETED Rescue Quest System (Two Variants)

Two fully structured rescue quests were deleted:

**Quest 1**: `DELETED_COMP_RQ_SpecificAliases_RandomRadiant_Rescue_Astronaut_001_Athena_has_Robots` (0x0059D817)
- **Condition**: Triggers when a specific actor value (0x5740F2) equals 1
- **Quest stage range**: 75-85 (mid-to-late storyline)
- **Aliases**: Player, Companion, RQReservedLocation, UnreservedLocation, Location, CaptiveMarker, TargetActor
- **Concept**: A.T.H.E.N.A. has captured robots; the player must rescue them

**Quest 2**: `DELETED_COMP_RQ_SpecificAliases_RandomRadiant_Rescue_Astronaut_002_Vendor_has_Robots` (0x0059D818)
- **Condition**: Triggers when that actor value does NOT equal 1 and is greater than 2
- **Quest stage range**: 75-85
- **Same alias structure as Quest 1**
- **Concept**: Emerson (the vendor) has captured robots; the player must rescue them

These two quests formed a **branching rescue system** -- depending on the player's relationship state with Sofia (or perhaps whether A.T.H.E.N.A. or Emerson was the current antagonist at that story point), different rescue quests would trigger. The quest stage conditions (75-85) place this in the late Confidant/early Infatuation tier.

This is the only known instance of a Wastelanders companion having **variant rescue quests** -- Beckett's companion questline uses only fetch and kill radiants with no rescue variants. The deletion of this system suggests Bethesda decided rescue missions were too complex for the companion framework.

### 2. Deleted Key: Lab Infiltration (Quest 015)

`DELETEDCOMP_Astronaut_015_Key_RDLab` (0x00571F62) -- KEYM record

A key item for "RDLab" (likely "Research & Development Lab") was created for Quest 015 (LabRat) and then deleted. The shipped version of Quest 015 (`COMP_RQ_Fetch_SpecificAliases_Astronaut_015_LabRat`) is a simple fetch quest. The deleted key suggests the original design required the player to **unlock a laboratory door**, turning what became a basic fetch into an infiltration quest with locked areas.

### 3. Deleted Misc Items (Quest Item Redesigns)

Two quest items were deleted during development:

- `DEL_COMP_RQ_Astronaut_MiscItem_026_ATHENAFragment` (0x0059C321) -- An A.T.H.E.N.A. fragment that was replaced by `COMP_RQ_Astronaut_MiscItem_026_HealthMonitor` (a health monitor). This suggests Quest 026 originally involved collecting a piece of A.T.H.E.N.A. itself, but was changed to a less dramatic health monitoring device.

- `DEL_COMP_RQ_Astronaut_MiscItem_028_FailedExperiment` (0x0059C323) -- A "Failed Experiment" item that was deleted and replaced by `COMP_RQ_Astronaut_MiscItem_028_BrainJar` (a brain jar). The original item implies the player would have found evidence of a botched USSA experiment; the replacement is more macabre and specific.

### 4. Cut Vendor Conversations

Two vendor conversations were marked CUT:

- `COMP_Conversation_Astronaut_Emerson_020_Vendor_CUT` (0x00574622) -- Emerson's vendor interaction scene
- `COMP_Conversation_Astronaut_Athena_020_Vendor_CUT` (0x00574624) -- A.T.H.E.N.A.'s vendor interaction scene

Both are numbered "020" and labeled "Vendor." In the shipped game, Emerson functions as a vendor after the outro quest, and A.T.H.E.N.A. (if saved) also becomes a vendor. These cut conversations suggest the vendor interactions were originally more elaborate, with dedicated conversation trees that were simplified to basic vendor menus.

Designer notes in dlstrings confirm these were tracked:
- `[61009007]` "Set to 1 if the player has played through ATHENA's vendor scene once"
- `[6100948D]` "Set to 1 if the player has played through Emerson's vendor scene once"

### 5. Retired Quest Variants (Quest 003 Redesign)

Two retired quest records reveal Quest 003 was redesigned at least once:

- `OLD_COMP_RQ_Fetch_SpecificAliases_Astronaut_RETIRED_003` (0x0058CE9B)
- `OLD_COMP_RQ_Fetch_SpecificAliases_Astronaut_RETIRED_003B` (0x0058CE9A)

Quest 003 shipped as "The Universe Conspires" -- a kill quest targeting USSA robots. The "003B" variant suggests there was originally an A/B quest variant system where the player might receive different versions of the same quest number, similar to the deleted rescue quest branching.

### 6. Deleted Scenes

- `DEL_COMP_Scene_Astronaut_Scrap` (0x0059FB17) -- A "scrap" scene for Sofia. This suggests there was originally a scene where Sofia would react to the player scrapping items or where the player could scrap USSA equipment. No equivalent exists in the shipped game.

- `DEL_ALLY_Astronaut_Scene_Intro` (0x0059FB19) -- A deleted intro scene, separate from the shipped intro. The shipped intro has Sofia found wounded in a building near her crash site. This deleted scene may represent an earlier version of the introduction that was overhauled.

### 7. Cut AI Behavior Packages

- `CUT_COMP_Astronaut_Intro_SpawnerSeeker01` (0x005A24AF) -- A "spawner seeker" package for the intro. This suggests the original intro had Sofia (or the player) actively seeking out spawned enemies, making the intro more combat-oriented than the shipped version.

- `CUT_COMP_Astronaut_Outro_Package_SofiaDizzyPostTerminal` (0x005A132F) -- A "dizzy" animation package for Sofia after using the A.T.H.E.N.A. terminal. In the shipped outro, Sofia reacts to the A.T.H.E.N.A. disconnection but doesn't have a dedicated disorientation animation. The cut package suggests a more dramatic physical reaction was planned.

### 8. Deleted Actor Value

`DELETED_COMP_AV_PlayerVisitorValue_Astronaut_DEPRECATED` (0x00563FB5) -- An actor value tracking visitor interactions was deprecated. This likely relates to the early companion system design where visitor NPCs (like Emerson) would track a "value" with the player separately from the main companion relationship.

### 9. Cut Dialogue Line

`CUT_COMP_Astronaut_Radiant_End_Randoms` (0x0056F682) -- A cut dialogue INFO record for random radiant quest endings. Sofia would have had randomized reaction lines when completing radiant quests, providing more variety. The shipped version uses a fixed set of 8 quest completion responses.

---

## The Archived NPC

`W05_COMP_Actor_Astronaut_SofiaDaguerre_Full_ARCHIVE_DONOTUSE` (0x005A3507) -- A complete NPC record for Sofia marked "ARCHIVE_DONOTUSE." This is a backup copy of her NPC data, preserved in the ESM but flagged to prevent accidental use. This is standard practice for major NPCs that undergo significant redesigns.

---

## The A.T.H.E.N.A. Storyline: What Shipped vs. What Was Planned

### Shipped Version
The shipped outro (`COMP_Quest_Outtro_Full_Astronaut`) presents a binary choice:
1. **Deploy Arachne** -- Destroys A.T.H.E.N.A., cures Sofia's headaches permanently
2. **Transfer to Assaultron** -- Gives A.T.H.E.N.A. a robot body (ARTEM1S), uncertain cure for Sofia

### Evidence of a More Complex Original Design

The ESM contains terminal options that hint at additional paths:
- `COMP_Astronaut_Outtro_Terminal_ATHENA_Main` -- A.T.H.E.N.A.'s main terminal
- `COMP_Astronaut_Outtro_Terminal_ATHENA_Options` -- A dedicated "options" terminal menu

Quest stage notes reveal additional interaction paths that were partially preserved:
- "Player asked if there's any way to save ATHENA" -- Unlocks the transfer option
- "ATHENA unlocked the 'Transfer' path in the terminal"
- "USE LUCK: Transfer to Assaultron" -- The transfer requires a LUCK check
- "USE: Console" with sub-stages for:
 - "TERMINAL: Access Granted"
 - "FOUND: Emerson's Password"
 - "PERC: ATHENA granted permission" (Perception check)
 - "INT: Hacked password" (Intelligence check)
 - "INT: Recall AV from Intro: Blue Sunset" (callback to intro quest)
 - "EMERSON uses Arachne" (Emerson makes the choice instead of the player)
 - "EMERSON reroutes to Assaultron" (Emerson makes the transfer choice)

This reveals the outro originally had **at least 6 different resolution paths** based on SPECIAL stats and player choices, compared to the 2 that shipped. Emerson could independently make either choice, the player could hack the terminal with INT, use PER to get A.T.H.E.N.A.'s permission, or recall a passphrase from the intro quest.

---

## The Deep Sleep Project: Narrative Threads

Sofia's backstory revolves around the USSA Deep Sleep Project -- a cryogenic hibernation mission launched in 2070. The string tables contain extensive dialogue about this project:

- The mission used Deep Sleeper Pods with whalesong audio conditioning
- Arktos Pharma partnered with USSA to create "Serum K" for the Deep Sleep process
- The serum didn't work as intended and caused aggressive behavior in some subjects
- A.T.H.E.N.A. was an AI monitoring system that maintained a parasitic connection to Sofia during hibernation
- The "Arachne" program was designed as a killswitch for A.T.H.E.N.A.

The cut content suggests the original questline explored these themes in more depth:
- The deleted ATHENAFragment quest item would have had the player physically collecting pieces of the AI
- The deleted FailedExperiment item would have provided evidence of what went wrong with Serum K
- The deleted rescue quests would have dramatized the ongoing conflict between A.T.H.E.N.A. and Emerson over control of Sofia's wellbeing

---

## 30 Quest Items That Survived

Despite the cuts, an unusually large set of 30 unique quest items made it into the shipped game (numbered 000-029, with two deleted). Each represents a different USSA artifact:

| # | Item | Description |
|---|------|-------------|
| 000 | DamagedDevice | Damaged USSA device |
| 001 | BloodSample | Blood sample |
| 002 | USSARobotMemory / Schematics | Robot memory core or schematics |
| 003 | ExperimentData | Experiment data |
| 004 | ExperimentMonitor | Experiment monitoring device |
| 005 | ReferenceCodes | USSA reference codes |
| 006 | ExperimentalModulator | Experimental modulator |
| 007 | AudioSensoryRelay | Audio sensory relay |
| 008 | EmergencyBeacon | Emergency beacon |
| 009 | CodeFragment | Code fragment |
| 010 | ScrubbedData | Scrubbed data |
| 011 | DeepSleepModule | Deep sleep module |
| 012 | ScannerModule | Scanner module |
| 013 | VisualSensoryRelay | Visual sensory relay |
| 014 | MeritOfHonor | Medal/commendation |
| 015 | ~~(not used)~~ | -- |
| 016 | RemoteMonitor | Remote monitoring device |
| 017 | SatellitePiece | Satellite fragment |
| 018 | AudioImprinter | Audio imprinter |
| 019 | DataRecorder | Data recorder |
| 020 | PodFragment | Deep Sleep pod fragment |
| 021 | SerumDiffuser | Serum diffuser (Serum K) |
| 022 | MainframeFragment | Mainframe fragment |
| 023 | TrackingInterceptor | Tracking interceptor |
| 024 | TactileModule | Tactile module |
| 025 | MemoryUnit | Memory unit |
| 026 | ~~ATHENAFragment~~ → HealthMonitor | Changed from AI fragment to medical device |
| 027 | ExperimentRecords | Experiment records |
| 028 | ~~FailedExperiment~~ → BrainJar | Changed from vague to specific |
| 029 | SealedFiles | Sealed classified files |

---

## Related NPCs and Voice Actors

| NPC | Voice Folder | Orphaned Lines | Role |
|-----|-------------|----------------|------|
| Sofia Daguerre | `w05_npcf_astronaut_sofiadaguerre` | 87 | Main companion |
| A.T.H.E.N.A. | `w05_robotf_astronaut_athena` | 7 | Antagonist AI |
| Pandora (Assaultron) | `w05_robotassaultron_astronaut_pandorabot` | 5 | USSA security bot |
| Emerson Hale | `w05_npcm_astronaut_visitoremerson` | 2 | USSA doctor, visitor NPC |
| ARTEM1S (Assaultron) | `w05_robotassaultron_astronaut_artemisbot` | 0 | A.T.H.E.N.A.'s new body |

---

## Conclusions

Sofia Daguerre's storyline underwent significant but surgical editing. The core narrative -- astronaut crashes, builds relationship with player, confronts parasitic AI, makes final choice -- survived intact. What was removed:

1. **Mechanical complexity** -- The branching rescue quest system and 6-path outro were simplified to reduce quest permutations
2. **Quest item specificity** -- Items that were too on-the-nose (ATHENAFragment, FailedExperiment) were replaced with less revealing alternatives
3. **Vendor elaboration** -- Dedicated vendor conversation scenes were cut in favor of standard vendor menus
4. **Physical lab infiltration** -- The LabRat quest's locked door requirement was removed
5. **NPC autonomy** -- Emerson's ability to independently resolve the A.T.H.E.N.A. conflict was cut, ensuring the player always makes the final choice

The 87 orphaned voice lines likely correspond to the cut rescue quest dialogue, the removed vendor conversations, the deleted intro scene, and variant takes on lines that were simplified during later recording passes.
