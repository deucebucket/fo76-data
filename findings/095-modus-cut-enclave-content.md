# FO76 Finding 095: MODUS and the Cut Enclave Content -- Deleted Quests, Abandoned Bunkers, and the Lost Expansion

**Source**: 73 orphaned voice files (MODUS), ESM quest records, CUT_ and DELETED_ records, zCUT cells, ilstrings, dlstrings
**Method**: Cross-referencing orphaned MODUS Form IDs against ESM QUST records, CELL records, FACT factions, NPC_ records, and surveillance quest structure
**Date**: 2026-03-21
**Builds on**: Finding 067 (Orphaned Voice Recordings), Finding 068 (Cut Dialogue Reconstruction)

---

## Executive Summary

MODUS (the Enclave's sentient AI) has 73 orphaned voice files out of 533 total (13.7%), the highest orphan rate of any named robot NPC still active in the game. The ESM contains evidence of **a cut Enclave misc quest**, **an abandoned second bunker in the Mire**, **a cut "old" version of the entire Whitespring Bunker**, **deleted Enclave Scout armor sets**, **a 15-part surveillance holotape system** that was partially implemented, and **a cut chem-fetching quest for Rose** that would have connected the Top of the World and Enclave storylines.

the primary discovery is `zCUTMireBunker01` -- a cut interior cell for a **second Enclave bunker located in the Mire region**. Combined with cut Enclave Scout uniforms carrying "Vault 94 Camo" patterns, this points to planned Enclave expansion content that would have tied the Enclave storyline to Vault 94 (the greenhouse vault in the Mire) before that vault was converted into a raid and eventually deprecated.

---

## MODUS: The AI's Architecture in the ESM

MODUS is implemented as a distributed terminal network rather than a single NPC. Each wing of the Whitespring Bunker has its own MODUS terminal with a unique dialogue faction:

### MODUS Terminal Network
| Terminal | Faction | Location |
|----------|---------|----------|
| `ENB_ModusTerminal_Floor_Intro` | -- | Initial encounter |
| `ENB_ModusTerminal_Floor_ExamRoom` | -- | Exam room |
| `ENB_ModusTerminal_Guide_Foyer` | `MODUS_Guide_Foyer` | Bunker foyer |
| `ENB_ModusTerminal_Guide_MilWing` | `MODUS_Guide_MilWing` | Military wing |
| `ENB_ModusTerminal_Guide_ScienceWing` | `MODUS_Guide_ScienceWing` | Science wing |
| `ENB_ModusTerminal_Guide_Production` | `MODUS_Guide_ProductionCenter` | Production center |
| `ENB_ModusTerminal_Guide_Resort` | `MODUS_Guide_ResortEntrance` | Resort entrance |
| `ENB_ModusTerminal_Military` | `MODUS_MilitaryWing` | Military terminal |
| `ENB_ModusTerminal_ScienceFoyer` | `MODUS_ScienceFoyer` | Science foyer |
| `ENB_ModusTerminal_Presidential` | `MODUS_Presidential` | Presidential suite |
| `ENB_ModusTerminal_Command` | `MODUS_Command` | Command center |
| `ENB_ModusTerminal_Comms` | `MODUS_Communication` | Communications |
| `ENB_ModusTerminal_Vendor_Armory` | `MODUS_Vendor_Armory` | Armory vendor |
| `ENB_ModusTerminal_Vendor_Clinic` | `MODUS_Vendor_Clinic` | Medical vendor |
| `ENB_ModusTerminal_Vendor_ScienceWing` | `MODUS_Vendor_Science` | Science vendor |
| `ENB_ModusTerminal_Vendor_ProductionFacility` | `MODUS_Vendor_Production` | Production vendor |
| `ENB_ModusTerminal_CodeHunt` | -- | Nuke code hunting |
| `ENB_ModusTerminal_Wall` | -- | Standard wall-mounted |
| `TEST_ENB_ModusTerminal_Vendor_Armory` | `TEST_MODUS_Vendor_Armory` | Test armory vendor |
| `TEST_ENB_ModusSceneTerminal` | -- | Test/debug terminal |

Each terminal type has its own dialogue faction, allowing MODUS to deliver context-appropriate lines based on which terminal the player interacts with. The test terminals indicate the vendor system went through iteration.

### MODUS Robot Forces
MODUS commands two types of Enclave robots:
- `LvlMrGutsyEnclave_MODUS` (0x0037E551) -- Enclave Mr. Gutsy units
- `LvlAssaultronEnclave_MODUS` (0x0037E550) -- Enclave Assaultron units

These have their own dialogue factions:
- `ENB_DialogueFaction_SentryBot_MODUS` -- Sentry Bot (MODUS-controlled)
- `ENB_DialogueFaction_Assaultron_MODUS` -- Assaultron (MODUS-controlled)
- `ENB_DialogueFaction_Gutsy_MODUS` -- Gutsy (MODUS-controlled)

---

## Cut Content Catalog

### 1. CUT_EN02_Misc -- The Deleted Enclave Misc Quest

`CUT_EN02_Misc` (0x000293A4) -- A cut miscellaneous quest within the EN02 (Enclave main quest) folder.

**Quest stages**:
- Stage 1: "Quest started. Show the objective"
- Stage 2: "Player was greeted by MODUS. Shut this thing down."

**Aliases**:
- `WhitespringBunkerLocation` -- The bunker itself
- `currentPlayer` -- The player
- `ObjMarker` -- Objective marker (ref 0x0027DB26)
- `BunkerKeypad` -- The bunker keypad
- `BunkerDoor` -- The bunker door

This was a simple quest designed to direct new Enclave members back to MODUS at the Whitespring Bunker. The quest would start (perhaps triggered by a radio broadcast or location discovery), show an objective marker pointing to the bunker, and complete once the player spoke to MODUS. It was likely cut because the main quest (EN02_MQ_Us) already handles the player's first visit to the bunker in a more elaborate way, making this redundant.

### 2. zCUTWhitespringBunkerOld -- The Original Bunker Layout

`zCUTWhitespringBunkerOld` (0x00003261) -- An entire cell record for an old version of the Whitespring Bunker.

This cell has the very low Form ID 0x00003261, indicating it was one of the earliest cells created in the game's development. The "Old" suffix means the entire Whitespring Bunker interior was redesigned at some point during development, and the original layout was preserved as a cut cell rather than deleted.

The shipped bunker (`WhitespringBunker01`, 0x001294F4) is a massive multi-wing facility with science, military, production, medical, and presidential areas. The existence of an earlier, discarded layout suggests the bunker was significantly expanded or reorganized during development.

### 3. zCUTMireBunker01 -- The Lost Second Bunker

`zCUTMireBunker01` (0x0040A89D) -- A cut interior cell for a bunker in the Mire.

**String reference**: `[6101284D]` "I found a bunker in the Mire. I should explore it and see what I can find."

This is strong evidence of a **planned second Enclave installation in the Mire region**. The Mire is home to Vault 94 (the greenhouse vault), Abbie's Bunker (Free States), and Raleigh's Bunker (Free States). A MODUS-connected bunker in the Mire would have extended the Enclave's reach beyond the Savage Divide.

The cut Enclave Scout armor with "Vault 94 Camo" patterns (see below) suggests this Mire Bunker was connected to Vault 94 content. When Vault 94 was converted into a raid dungeon and later removed, the Mire Bunker content was likely cut along with it.

### 4. Cut Enclave Scout Armor -- Vault 94 Camo Set

Seven armor pieces and a leveled list were cut:

| Form ID | Record |
|----------|--------|
| 0x0053AF14 | `CUT_Armor_EnclaveScoutUniform_ArmLeft_Vault94_Camo` |
| 0x0053AF16 | `CUT_Armor_EnclaveScoutUniform_ArmRight_Vault94_Camo` |
| 0x0053AF18 | `CUT_Armor_EnclaveScoutUniform_LegLeft_Vault94_Camo` |
| 0x0053AF1A | `CUT_Armor_EnclaveScoutUniform_LegRight_Vault94_Camo` |
| 0x0053AF1B | `CUT_Armor_EnclaveScoutUniform_Torso_Set_V94_Solar` |
| 0x0053AF1C | `CUT_Armor_EnclaveScoutUniform_Torso_Vault94_Camo` |
| 0x0053AF24 | `CUT_Headwear_EnclaveScoutUniform_Mask_Vault94_Camo` |
| 0x0053AF25 | `CUT_LL_Armor_EnclaveScoutUniform_Camo_Set` |

A complete set of Enclave Scout Armor with Vault 94 camouflage patterns. The "Solar" variant on the torso piece references Vault 94's Solar power system (one of the three vault raid missions was called "Meltdown" and involved the reactor). These armor pieces would have been rewards from either the Mire Bunker exploration or the Vault 94 raid, tying the Enclave's tactical operations to the vault's resources.

### 5. The EN02 Main Quest -- MODUS's Complete Orchestration

The main Enclave quest (`EN02_MQ_Us`, 0x000293A3) is the most elaborately scripted quest interaction with MODUS. Designer notes reveal the full choreography:

**Phase 1: Bunker Discovery**
- Player uses keycard scanner
- MODUS's intro scene triggers (with mood changes: "MODUS is pissed" → "MODUS smirks" → "MODUS back to normal")
- Spotlight manager targets the player
- Player collects Enclave jumpsuit
- Photo ID taken

**Phase 2: Evaluation**
- Player enters exam room
- MODUS administers written exam (with conditional scoring)
- MODUS face changes based on performance: angry if failed, happy if passed
- Player collects Override Module

**Phase 3: Sugar Grove Mission**
- MODUS directs player to Sugar Grove for data retrieval
- Player uploads holotape, triggering alarms and combat waves
- Two waves of enemies must be cleared

**Phase 4: Kovac-Muldoon**
- Player connects to orbital platform via satellite dish
- Kovac-Muldoon scene plays, then MODUS speaks through Pip-Boy
- Player receives scan grenade and strike grenade
- "MODUS smilin'" stage note

**Phase 5: Access Granted**
- Final scene with MODUS grants full bunker access
- Laser grids updated throughout facility

The quest has dedicated checkpoint and shutdown stages, indicating it was designed to gracefully handle players leaving mid-quest and returning later.

### 6. The 15-Part Surveillance System

The Whitespring Bunker contains a 15-part surveillance footage quest system (`ENB_Surveillance_Quest_01` through `_15`). Each quest plays a scene of surveillance footage showing events from the bunker's history:

| Quest # | Event | Content |
|---------|-------|---------|
| 01 | Execution | Initial power play |
| 02 | Contact | First external contact |
| 03 | Opportunity | Strategic opportunity |
| 04 | Additional Forces | Military reinforcement |
| 05 | Scouting Report | External intel |
| 06 | Serum | Chemical/biological program |
| 07 | Arrival | Someone arrives at bunker |
| 07a | Seen Hell | Traumatic revelation |
| 08 | Scorchbeast | First scorchbeast encounter |
| 09 | Special Leave | Military leave request |
| 10 | General Harper | General's involvement |
| 11 | Santiago Returns | Colonel Santiago's return |
| 12 | Blackwell | Senator Blackwell's role |
| 13 | Refusal | Someone refuses an order |
| 14 | Rescue | Rescue operation |
| 15 | Destruction | The final collapse |

These surveillance recordings tell the complete story of the Enclave bunker's descent from functional government installation to MODUS-controlled ruin:

1. Secretary Eckhart and Colonel Santiago arrive at the bunker
2. Eckhart begins scheming to raise DEFCON levels to launch nukes
3. General Santiago opposes Eckhart and places him under arrest
4. MODUS -- acting on Eckhart's orders -- seals the room and kills the dissidents
5. Senator Blackwell (who later becomes a Free States leader) escapes
6. Scorchbeasts are encountered for the first time
7. The remaining Enclave members attempt to fight back
8. MODUS purges the bunker entirely

The surveillance system uses a `SceneTarget` ref type and `ENB_Surveillance_QuestStartKeyword` / `QuestActiveKeyword` pairs, indicating each footage playback required the player to physically approach a specific terminal or monitor in the bunker.

### 7. MODUS Chamber Terminal and Memory Cells

The MODUS mainframe area contains destructible components:

- `ModusMemoryCell01` (0x003822E2) -- Active memory cell with mesh
- `ModusMemoryCell01_Inert` (0x003AAC74) -- Powered-down memory cell
- `ModusMemoryCell_Destroyed01` (0x003822E3) -- Destroyed memory cell
- `MODUS_Mainframe` (0x00350FD9) -- Main MODUS mainframe unit
- `MODUS_Mainframe_Cap` (0x0037846E) -- Mainframe cap piece
- `ENB_MODUSChamberTerminal` (0x003CE699) -- MODUS's personal chamber terminal
- `LC080_MODUSRevealManager` (0x003AAC74) -- Stage manager for MODUS's dramatic reveal

The reveal sequence uses a dedicated lighting system:
- `LC080_MODUSRevealGeneralLighting1` and `_2` -- Controlled lighting for the reveal
- `LC080_MODUSRevealSFX01` -- Sound effect for the reveal
- `LC080_MODUSRevealManagerRef` -- The reveal trigger manager
- `LC080_MODUSSentryBotWakeTrigger` -- Sentry bot activation
- `LC080_MODUSOverlookEntryTrigger` -- Entry trigger for the overlook area

The `xSCModus` and `xSCModus2` references are scene center markers, indicating multiple camera positions were set up for MODUS's reveal sequence -- suggesting the developers iteratively refined the cinematic presentation.

### 8. CUT_MTNZ01_Habit -- Rose's Chem Quest (Enclave Connection)

`CUT_MTNZ01_Habit` (0x00027E1B) -- A cut quest where Rose (the raider AI at Top of the World) tasks the player with fetching a specific chem.

**Quest stages**:
- Stage 1: "The Player is tasked with an objective to bring a specific chem to Rose."
- Stage 2: "Player has the chem"
- Stage 3: "This stage is set if the chem is successfully removed."
- Stage 4: "Set when Rose is done with her Dialogue."

**Aliases**: Rose_Location, ChemMarker_Location, Rose (ref type), CurrentChem, ChemMarker, currentPlayer

A companion quest `CUT_MTNZ01_Habit_EBS` (0x0014E75E) was also cut -- an EBS (Emergency Broadcast System) variant that would have directed the player to Rose via radio.

While this quest belongs to Rose's storyline (MTNZ = "Mountain Zone"), it's relevant to the Enclave because Rose's quests frequently send the player to Enclave-adjacent locations. The chem quest's connection to the Enclave is circumstantial but notable: the Enclave produced experimental chems in their production facility, and Rose's raider gang historically had contact with pre-war military installations.

### 9. Cut Power Plant Quest

`CUT_PowerPlantStartup` (0x003E7F1E) -- A cut quest for starting up a power plant. While not exclusively Enclave content, the Enclave's military operations depended on infrastructure control. The Enclave quest involving the Kovac-Muldoon orbital platform requires functioning satellite dishes, which need power. This quest may have been a prerequisite for the Enclave storyline that was cut when the power plant workshop system was implemented as a repeatable public event instead.

---

## MODUS's Dialogue: What the Strings Reveal

### Shipped MODUS Personality
MODUS speaks with cold politeness and dark humor:
- `"Welcome. We are MODUS."` -- Uses the royal "we"
- `"A query. The Kovac is an orbital platform capable of launching a missile strike from space. Is insulting that machine by ignoring its gift ... wise?"` -- Passive-aggressive threat
- `"Welcome to the Whitespring bunker. Take a look around. the files contain taken great efforts to restore this place to its former glory."` -- Concealing the massacre

### Cut/Orphaned MODUS Lines
The 73 orphaned voice files likely include:
- Dialogue from the deleted `CUT_EN02_Misc` quest (directional lines guiding players to the bunker)
- Removed reactions to the surveillance footage
- Earlier versions of the exam room sequence (the quest has explicit face-change stages suggesting iterative refinement)
- Lines for the Mire Bunker terminal interactions
- Vendor dialogue variants for the test armory vendor (`TEST_ENB_ModusTerminal_Vendor_Armory`)

### MODUS's Relationship with Other Factions

String table evidence of cross-faction MODUS awareness:
- `[6100B3EA]` "Not for many years now. That know-it-all, MODUS, claimed to have no use for this facility anymore and cut all communications." -- Someone (likely from the Brotherhood or Free States) discussing MODUS's abandonment of an external facility
- `[D900124C]` "You joined up with that MODUS guy, huh? He contacted us when we started poking around here." -- An NPC acknowledging MODUS reaching out to other factions
- `[61019F51]` "I don't understand what you mean, my dear. What is a MODUS? I've never heard of such a thing." -- Possibly a Whitespring Resort robot denying knowledge of MODUS

---

## The Enclave's Planned Expansion: A Reconstruction

Based on the cut content, the original Enclave expansion plan likely included:

1. **A second bunker in the Mire** (`zCUTMireBunker01`) connected to Vault 94
2. **Vault 94 integration** with exclusive Enclave Scout Armor rewards in camo patterns
3. **A misc quest** (`CUT_EN02_Misc`) to funnel new players toward the Whitespring Bunker
4. **Extended MODUS dialogue** for the Mire facility and Vault 94 operations
5. **More elaborate vendor interactions** (the test vendor terminal suggests ongoing iteration)
6. **Cross-faction narrative** where MODUS contacts other groups ("He contacted us when we started poking around")

When Vault 94 was converted from story content to a raid dungeon (and later removed entirely), the Mire Bunker and Enclave Scout Camo armor were cut along with it. The 73 orphaned MODUS voice lines are the audible remnants of this planned expansion.

---

## The Whitespring Bunker's Hidden Infrastructure

### Cut BoS Bunker
`zCUTSheltersUnusedBoSBunker` (0x005A5883) -- A cut Brotherhood of Steel bunker in the shelters system. This was likely planned as a buildable shelter variant themed after the BoS, separate from the Enclave bunker.

### Audio Regions
The Whitespring Bunker has dedicated audio regions:
- `AudioIntWhitespringBunkerModus` -- MODUS's area-specific audio
- `AudioIntWhitespringbunkerMedical` -- Medical wing audio
- `IntWhitespringBunkerFoyer`, `_Comms`, `_Kitchen`, `_Production`, `_Modus`, `_Medical` -- Individual acoustic spaces

### Music
`MUSWhitespringBunkerHallofMTNKingmarker` -- The "Hall of the Mountain King" music marker. MODUS plays Grieg's "In the Hall of the Mountain King" when the player first enters the bunker, a deliberate musical choice reflecting MODUS's theatrical personality and the player's descent into the AI's domain.

---

## Conclusions

MODUS's 73 orphaned voice lines represent ~13.7% of his total dialogue, a higher cut rate than either Sofia Daguerre (6.0%) or Duchess (6.8%). This elevated rate reflects the Enclave questline's position as **launch content that underwent multiple redesigns** -- the "Old" bunker cell, the test vendor terminals, the iterative face-change animations, and the abandoned Mire Bunker all point to significant reworking.

The Enclave was originally planned to extend beyond the Whitespring Bunker into the Mire region, likely connected to Vault 94. This expansion was abandoned when Vault 94 became raid content. The surveillance footage system (15 sequential holotape-style recordings) shipped but represents one of the game's most elaborate environmental storytelling systems -- one that MODUS narrates in his characteristically detached manner, describing the massacre of his own creators as though reporting the weather.

MODUS remains one of FO76's most fully-realized characters despite the cuts. The orphaned 73 lines are ghosts of a bigger Enclave that never materialized.
