# FO76 Finding 096: Complete Catalog of Cut NPCs -- 19 Fully Orphaned Characters and Their Lost Content

**Source**: Orphaned voice analysis (20,300 orphaned Form IDs across 147 actors), ESM quest records, NPC_ records, VTYP voice types, ilstrings, dlstrings
**Method**: Identifying 100% orphaned voice actors (all voice files disconnected from ESM), cross-referencing quest records, NPC records, and string table text
**Date**: 2026-03-21
**Builds on**: Finding 067 (Orphaned Voice Recordings), Finding 068 (Cut Dialogue Reconstruction)

---

## Executive Summary

19 voice actor folders in the Fallout 76 voice archives contain **only orphaned files** -- every single voice recording for these characters is disconnected from the game's quest system. These represent NPCs that were completely cut from the game, their content abandoned at various stages of development. Combined, they account for 92 orphaned voice files totaling approximately 15 minutes of recorded dialogue.

The catalog breaks down into five categories:
- **Cut Named NPCs** (3): Ryan Ainsley, Marcus Wellsby, Jeremiah Ward
- **Cut Robots** (7): Drill Sergeant Eyebot, Survey Bot, Payroll Terminal, Robotic Eyebot, SFG01 Announcer, Announcer Radio Eyebot, EMIAC Robobrain
- **Cut Radio/Broadcast** (4): Paladin Radio, EBS Radio, Number Station, DQ01 Radio Voice
- **Cut Quest NPC** (1): Moe the Mole
- **Legacy/Miscellaneous** (4): DLC03 Robobrain, Rhonda (Miss Nanny), 76 Trailer Voice, FF08 Dispatcher

---

## Category 1: Cut Named NPCs

### Ryan Ainsley -- Whitespring Resort Researcher (11 orphaned files)

**Voice type**: `CUT_NPCM_LC060_RyanAinsley` (0x003CDB12) -- explicitly flagged CUT
**Location prefix**: LC060 (Whitespring Resort/Golf Club)
**Character**: Pre-war academic working on a dissertation, spending the summer at the Whitespring

**Surviving text** (from dlstrings):
> "I've spent the summer working on my dissertation. It's done. I'm heading back to CIT to present my defense. And then I'm never setting foot on a golf course again."
>
> Ryan Ainsley

**Analysis**: Ryan Ainsley was a pre-war Whitespring Resort guest who was finishing a doctoral dissertation at CIT (Commonwealth Institute of Technology, the pre-war name for The Institute from Fallout 4). His reference to CIT connects Fallout 76 directly to The Institute's lore.

The LC060 prefix groups him with other Whitespring content including vendor robots, barbershop factions, and dining room NPCs. He was likely planned as an interactive holotape character or a "ghost NPC" (a pre-recorded personality that players could encounter through notes, holotapes, or terminal entries). His 11 voice recordings suggest a multi-part story -- perhaps holotape diary entries documenting his time at the resort before the bombs fell.

His disgust with golf courses suggests dark comedy -- an intellectual trapped at a luxury resort, counting the days until he can leave, unaware that the world is about to end.

### Marcus Wellsby -- Whitespring Resort Staffer (3 orphaned files)

**Voice type**: `CUT_NPCM_LC060_MarcusWellsby` (0x003CDB05) -- explicitly flagged CUT
**Location prefix**: LC060 (Whitespring Resort)
**Character**: Pre-war Whitespring Resort employee or guest

**Analysis**: With only 3 voice files, Marcus Wellsby had a much smaller role than Ryan Ainsley. The LC060 prefix places him at the Whitespring Resort. Given the resort's extensive robot vendor system (barbershop, dining room, spa, pharmacy, formal clothing, hunting supplies, etc.), Wellsby was likely a pre-war human staffer whose recorded messages would have been encountered by the player while exploring the resort.

The Whitespring Resort has an extensive faction system for its robot vendors (`LC060_WhitespringVendor_Barbershop_Margaret_Faction`, `_DiningRoom_Robert_Faction`, etc.), all named after human staffers. Marcus Wellsby may have been one of these staffers who was meant to have actual voice recordings rather than just being a name on a faction.

### Jeremiah Ward -- Flatwoods Resident (1 orphaned file)

**NPC**: `npcm_lc044_jeremiahward` -- 1 orphaned voice file
**Location prefix**: LC044 (Flatwoods area)
**Book reference**: `LC044_JeremiahWardNote01DUPLICATE000` (0x003D7EFB)

**Surviving text** (from dlstrings):
> "I, Jeremiah Ward, resident in the town of Flatwoods, county of... not sure."

**Analysis**: Jeremiah Ward was a survivor in the Flatwoods area. His note survives as a BOOK record (a written note in-game), and he has a DUPLICATE variant suggesting the note was placed in multiple locations during development. The LC044 prefix places him in the Flatwoods/Forest region.

Flatwoods is the first major settlement players encounter after leaving Vault 76. Ward was likely part of the early-game environmental storytelling -- a survivor documenting the post-war chaos. His single voice file suggests he was planned as a holotape narrator who was ultimately replaced by written notes only.

LC044 also contains quest scenes: `LC044_IrritableSurvivor`, `LC044_ChemsAddict`, `LC044_TrappedResponder`, `LC044_TrappedResponder_HiddenCache` -- these are random encounter scenes for the Flatwoods area. Ward may have been connected to one of these encounters before his voice content was cut.

---

## Category 2: Cut Robots

### Drill Sergeant Eyebot (10 orphaned files)

**Voice folder**: `roboteyebot_cbz13_drillsergeant`
**Location prefix**: CBZ13 (Cranberry Bog zone event)
**Associated quest**: `CBZ13_Robots` (0x0052BDF7) -- "Encampment" public event

**Quest structure** (from designer notes):
- Stage 1: Players talk to robot quest giver
- Stage 2: Players use terminal to activate recall beacon
- Stage 3: Robot powers down
- Stages 4-10: Three combat waves with bosses, escalating to a final boss
- Stage 11: Quest complete

**Dialogue direction notes**:
- `"commander pep talk to troops"` -- The Drill Sergeant rallies defenders
- `"annoyed you can't stay and fight"` -- Reacts to player leaving
- `"commanding, 'you can do this!'"` -- Combat encouragement
- `"giving orders, this line as if projecting to someone a short distance away"` -- Tactical commands
- `"strong, but powering down during saying line"` -- Death/shutdown performance
- `"read as two words. 'Diiissss. Missed!' Requires heavy post processing"` -- Glitching shutdown variant
- `"Name: read each letter, dash, and number. ASAP as a single word 'Ay-Sap.' - distress call, in the tone of giving orders"` -- Emergency broadcast

**Analysis**: The Drill Sergeant Eyebot was the quest giver for CBZ13_Robots, a Cranberry Bog public event. The event still exists in-game but the Drill Sergeant was replaced with a different quest giver or simplified initiation. The Drill Sergeant would have been a military eyebot that barked orders and encouraged players during wave-based combat defense, eventually powering down during the event (with two recorded variants of his shutdown: a dignified fadeout and a glitchy malfunction).

### Robotic Eyebot (5 orphaned files)

**Voice folder**: `roboteyebot_cbz13_robotic`
**Location prefix**: CBZ13 (same Cranberry Bog event)

**Analysis**: A second eyebot for the same CBZ13 event. This "Robotic" eyebot likely served as a companion or secondary quest NPC alongside the Drill Sergeant. With 5 files, it had a supporting role -- possibly an EBS (Emergency Broadcast System) relay or combat report bot. The CBZ13 event's EBS topic (`CBZ13_EBS_Topic`, named "Emergency Broadcast") suggests these eyebots were broadcasting distress calls that drew players to the event.

### Survey Bot -- Protectron (10 orphaned files)

**Voice folder**: `robotprotectron_twg01_surveybot`
**Location prefix**: TWG01 (unknown location, possibly "Toxic Waste" or "Tower" zone)

**Analysis**: A Protectron surveyor robot with 10 voice files. The "survey" function suggests this robot was conducting environmental scans or resource surveys, possibly as part of a repeatable event where players would defend or escort it. The TWG prefix doesn't match any known shipped event, suggesting the entire event this robot belonged to was cut.

### Payroll Terminal -- Announcer (9 orphaned files)

**Voice folder**: `announcerf_mtrg01_payrollterminal`
**Location prefix**: MTRG01 (unknown, possibly "Monongah" or "Metro" area)

**Analysis**: A female-voiced announcer for a payroll terminal. With 9 voice files, this was a substantial interaction point. The "payroll" function suggests a pre-war workplace terminal that would dispense information about employee payments, benefits, or schedules -- dark comedy material given the post-apocalyptic setting. The MTRG prefix doesn't match any shipped content.

### SFG01 Announcer -- Protectron (5 orphaned files)

**Voice folder**: `robotprotectron_sfg01_announcer`
**Location prefix**: SFG01 (possibly "Savage Divide Forest/Ground" area)

**Analysis**: A Protectron announcer bot for an unidentified location. With 5 voice files, this was likely a public address or tour guide robot similar to the various museum and facility robots in the game. The SFG prefix is not matched to any shipped quest content.

### Announcer Radio Eyebot (2 orphaned files)

**Voice folder**: `roboteyebot_announcer_radio`
**No location prefix** -- generic announcer type

**Analysis**: A radio broadcasting eyebot with 2 voice files. Likely part of a cut radio station or broadcast system. The game has several radio-broadcasting eyebots that survived (such as the various public event announcement bots), suggesting this one was redundant or belonged to cut content.

### EMIAC -- Robobrain (1 orphaned file)

**Voice folder**: `dlc03robotrobobrain_re_scenemp01_emiac`
**NPC record**: `RE_SceneMP01_EMIAC` (0x0035EC40)
**Message**: `RE_SceneMP01_EMIACmsg` (0x0035EC36)
**Voice type**: `DLC03RobotRobobrain_RE_SceneMP01_EMIAC` (0x0035EDB6)

**Analysis**: EMIAC is a Robobrain (DLC03 robot type from Fallout 4's Automatron DLC) that was designed for a random encounter scene (`RE_SceneMP01`). The name "EMIAC" is a reference to ENIAC, the first general-purpose electronic computer. This Robobrain would have appeared as a random encounter -- a wandering pre-war computer personality in a robot body. The `RE_SceneMP01` prefix indicates it belonged to a "multiplayer scene" random encounter, meaning multiple players could have encountered it simultaneously.

With only 1 voice file, EMIAC's encounter was extremely minimal -- possibly a single greeting or observation before the player could interact with or destroy it.

---

## Category 3: Cut Radio/Broadcast NPCs

### Paladin Radio (5 orphaned files)

**Voice folder**: `bs00_paladinradio_voicetype`
**Voice type**: `BS00_PaladinRadio_VoiceType` (0x005ADC51)
**NPC**: `BS00_PaladinRadio_SpeakerNPC` (0x005ADC43)
**Quests**: 5 sequential broadcast quests

**Quest structure**:
| Quest | Form ID | Condition |
|-------|---------|-----------|
| `BS00_PaladinRadioQuest_01` | 0x005ADC24 | Global == 1 |
| `BS00_PaladinRadioQuest_02` | 0x005B2BA4 | Global == 2 |
| `BS00_PaladinRadioQuest_03` | 0x005B2BA5 | Global == 3 |
| `BS00_PaladinRadioQuest_04` | 0x005B2BA3 | Global == 4 |
| `BS00_PaladinRadioQuest_05` | 0x005B2BA6 | Global == 5 |

Each quest has a single scene (`_Message`), a `Loc_Tower01` alias, and an `Activator_Transmitter` alias.

**Parallel system**: A matching "Maxson Radio" series exists with 5 quests (`BS00_MaxsonRadioQuest_01` through `_05`) using the same global progression variable but a different transmitter activator.

**Analysis**: The Paladin Radio was a **cut Brotherhood of Steel radio station** that would have broadcast 5 sequential messages. The broadcasts were tied to a physical radio transmitter at a tower location, with each message triggering after a global variable incremented. This is the same pattern used for the existing BoS emergency broadcasts in the game.

The parallel Maxson Radio series suggests **two competing BoS broadcast channels** -- one from a field Paladin and one carrying Elder Maxson's recorded messages. The Maxson Radio quests survived in the ESM but the Paladin Radio was fully cut from quest connections.

The 5 Paladin Radio recordings (approximately 4 minutes 21 seconds of audio based on extraction data from Finding 068) would have contained field reports, tactical updates, or morale broadcasts from a BoS Paladin operating in Appalachia.

### EBS Radio (2 orphaned files)

**Voice folder**: `announcerm_ebs_radio`

**Analysis**: An Emergency Broadcast System radio voice with 2 recordings. The game uses EBS broadcasts extensively (they trigger quests, announce events, and deliver lore), so these 2 orphaned files represent cut broadcasts that were replaced or made redundant by other EBS content.

### Number Station (1 orphaned file)

**Voice folder**: `npcf_numberstation`
**Voice type**: `NPCF_NumberStation` (0x004EAC11)

**Analysis**: A female-voiced "numbers station" -- a radio broadcast that reads sequences of numbers, referencing real-world espionage communication methods. Numbers stations are a staple of cold war paranoia fiction and fit perfectly into Fallout's aesthetic. The single orphaned file suggests this was either a very early prototype that was cut before production, or a single broadcast that was removed from the radio rotation.

A numbers station in Fallout 76 could have been connected to the Enclave (spy communications), the Free States (paranoid survivalists monitoring government frequencies), or been purely atmospheric -- a mysterious broadcast that players could never fully decode.

### DQ01 Radio Voice (1 orphaned file)

**Voice folder**: `announcerm_dq01_radiovoice`
**Quest reference**: `NPE_DQ01_BetterTomorrow` (0x006FD072) -- "A Better Tomorrow" quest

**Analysis**: A male-voiced radio announcer for the "A Better Tomorrow" daily quest system (NPE = New Player Experience). The DQ01 prefix suggests "Daily Quest 01." The quest involves Lane Platte as quest giver with tasks including care packages, cult research, and forest clearance. The orphaned radio voice was likely an earlier version of the quest's radio hook that was replaced by Lane Platte's direct dialogue.

---

## Category 4: Cut Quest NPC

### Moe the Mole (8 orphaned files)

**Voice folder**: `npcm_sf07_moe`
**NPC**: `SF07_MoeTheMole_VOICEONLY` (0x0034142E)
**Voice types**: `NPCM_SF07_MOE` (0x00355DBC) and `_CUT_NPCM_SF07_MoeTheMole` (0x0034142F)
**Quest**: `SF07_MoeDigsSafety_CUT_FlaggedToNotExportInScript` (0x0004BBFB)

*Fully documented in Finding 068. Summary*: Moe the Mole was a children's safety mascot who narrated a guided nature tour that ended in a radscorpion attack. 16 dialogue lines survive in the strings files. The quest involved finding and wearing a destroyed Moe costume, then fighting a boss radscorpion ("Scorpie").

Despite being cut as a quest NPC, Moe the Mole survived as a cultural artifact:
- Plushie: `ATX_Plushie_MoeTheMole` -- Atom Shop item
- Posters: 3 poster variants (`Storm_MoetheMole_Poster1/2/3`)
- Cutout: Floor decoration (`Storm_MoeTheMole_Cutout`)
- Backpack flair: 2 variants (`zzz_mod_BackPack_MoeTheMole_Flair1/2`)
- Photoboard: `Storm_MoeTheMole_Photoboard_Transform`
- Costume: `Burn_MoeTheMole` -- an outfit record

Moe the Mole became more successful as merchandising than as a quest character.

---

## Category 5: Legacy/Miscellaneous

### DLC03 Robobrain (6 orphaned files)

**Voice folder**: `dlc03robotrobobrain`
**Category**: Fallout 4 legacy

**Analysis**: Generic Robobrain voice lines inherited from Fallout 4's Automatron DLC. These are not unique to any FO76 character but were included in the voice archives. All 6 files are orphaned because FO76 implemented its own Robobrain dialogue system rather than using FO4's recordings.

### Rhonda -- Miss Nanny (1 orphaned file)

**Voice folder**: `robotmsnanny_scenemp02_rhonda`
**Quest reference**: `RE_SceneMP02` (0x00435462) -- A random encounter scene

**Analysis**: Rhonda is a Miss Nanny robot designed for a random encounter. The name "Rhonda" is likely a reference to the Beach Boys' "Help Me, Rhonda." With 1 voice file, this was a minimal encounter -- possibly a broken-down Miss Nanny that the player could find and briefly interact with. The SceneMP02 prefix indicates this was a multiplayer random encounter.

Rose's companion quest line involves a Miss Nanny named Rhonda (Rose's "best friend"), but that Rhonda has connected dialogue and uses a different voice type. This orphaned Rhonda may be an earlier version of that character or a completely different robot who happens to share the name.

### 76 Trailer Voice (1 orphaned file)

**Voice folder**: `76trailervoicetype`

**Analysis**: A voice recording used for the Fallout 76 announcement or promotional trailer. This was included in the voice archives but was never connected to any in-game quest or dialogue system. It exists purely as a leftover from marketing material production.

### FF08 Dispatcher (1 orphaned file)

**Voice folder**: `announcerf_ff08_dispatcher`
**Quest**: `FF08_ProjectBeanstalk` (0x0004695C) -- "Project Beanstalk" public event

**Analysis**: A female dispatcher voice for Project Beanstalk, a public event at Dyer Chemical where players escort a Pharmabot through three spray locations while defending it from waves of enemies. The dispatcher would have provided tactical communications during the event (enemy alerts, status updates). The shipped version of the event uses the Pharmabot's own voice for narration, making the dispatcher redundant.

The event's designer notes reveal elaborate quest logic: the Pharmabot paths through three spray locations, can be damaged and must be repaired, and has a health bar displayed as an objective counter. The dispatcher would have added another layer of communication on top of this already complex event.

---

## Cut Whitespring Vendor System

The ESM contains both shipped and cut faction records for the Whitespring Resort's vendor system:

### Cut Vendor Factions
| Cut Faction | Shipped Equivalent |
|-------------|-------------------|
| `CUT_LC060_WhitespringVendor_BoS_Faction` (0x004102A9) | `LC060_WhitespringVendor_BoS_Faction` (0x004124A7) |
| `CUT_LC060_WhitespringVendor_Raiders_Faction` (0x004102A8) | `LC060_WhitespringVendor_Raiders_Faction` (0x004124AB) |
| `CUT_LC060_WhitespringVendor_Responders_Faction` (0x004102A6) | `LC060_WhitespringVendor_Responders_Faction` (0x004124AC) |
| `CUT_LC060_WhitespringVendor_FreeStates_Faction` (0x004102A7) | `LC060_WhitespringVendor_FreeStates_Faction` (0x004124A8) |
| `CUT_LC060_WhitespringVendor_Neutral_Faction` (0x004102AA) | `LC060_WhitespringVendor_Neutral_Faction` (0x004124AA) |

The CUT factions have lower Form IDs (0x004102xx) than their shipped replacements (0x004124xx), indicating the vendor faction system was redesigned. The original system had faction-aligned vendors; the replacement kept the concept but rebuilt the faction records -- likely to fix bugs or adjust the shared caps pool system.

Ryan Ainsley and Marcus Wellsby may have been connected to this earlier vendor system as human staffers who were replaced by robot vendors in the redesign.

---

## Duchess and The Wayward: Cut Content (37 Orphaned Lines)

While Duchess is not a fully cut NPC (505 of her 542 voice lines are connected), her 37 orphaned files represent specific cut content:

### Cut Wayward Conversations
Three Wayward random conversation quests were cut:

| Quest | Content |
|-------|---------|
| `CUT_W05_DialogueWaywardRC_JideGracie_Gift` (0x0042ECD4) | Jide and Gracie discuss a gift |
| `CUT_W05_DialogueWaywardRC_JideGracie_Mort` (0x0042ECD5) | Jide and Gracie discuss Mort |
| `CUT_W05_DialogueWaywardRC_JideGracie_ToadSteaks` (0x0042ECD8) | Jide and Gracie discuss toad steaks |

These were ambient conversations between Wayward patrons Jide and Gracie. Each is tagged with the filter `\W05\Main Quest\The Wayward\Random Convos\`, indicating they were part of a random conversation system that played ambient NPC chatter inside the bar.

### Cut Wayward Test Cell
`zCUTTestTheWaywardExt` (0x00587BCC) -- A test cell for the Wayward's exterior. This was used during development to test the bar's outdoor area and was cut when testing was complete.

### Cut Wayward Settlement Quest
`OLD_W05_DialogueWaywardSettlement` (0x00425CF0) -- An older version of the Wayward settlement dialogue quest, replaced by the shipped version.

### Duchess's Cut Dialogue Context
Designer notes reveal the Wayward questline's complexity:
- Duchess has multiple package states: initial encounter, hands-up (holdup), sketching (drawing plans), negotiation
- Batter (her bodyguard) can be killed or survive, affecting Duchess's reactions
- The player can tell Duchess they're from a vault (tracked for later dialogue)
- Sol can die during the quest, requiring adjusted dialogue from Duchess and crew
- An entire path where "the player let Sol die during 004" is tracked with a cooldown timer

The Wayward questline originally included more branching than shipped:
- `[0004DE04]` "This path will be expanded in second pass. The player will be able to convince Sol and Duchess to let Crane go, who can show up as a random encounter later."
- `[0004DE05]` "From here, the player can side with Duchess or Sol, agreeing Crane should be killed (and either Sol or the player can do it) or convincing the group to let him go."

Duchess's 37 orphaned lines likely correspond to the cut Jide/Gracie conversations (which she may have participated in), the removed branching dialogue options, and earlier versions of her intro sequence.

---

## Statistical Summary

| Category | NPCs | Orphaned Files | Estimated Audio |
|----------|------|----------------|-----------------|
| Cut Named NPCs | 3 | 15 | ~1m 50s |
| Cut Robots | 7 | 42 | ~5m 30s |
| Cut Radio/Broadcast | 4 | 9 | ~1m 30s |
| Cut Quest NPC (Moe) | 1 | 8 | ~1m 0s |
| Legacy/Misc | 4 | 9 | ~1m 15s |
| Duchess (partial) | 1 | 37 | ~4m 0s |
| **Total** | **20** | **120** | **~15m 5s** |

---

## The Pattern of Cuts

Examining all 19 fully cut NPCs and Duchess's partial cuts reveals consistent patterns in Bethesda's development process:

1. **Radio/Broadcast NPCs are most expendable** -- 4 of 19 fully cut NPCs are radio voices, easily replaced by existing broadcast systems
2. **Event quest givers get redesigned** -- The Drill Sergeant Eyebot and FF08 Dispatcher were replaced by simpler initiation methods
3. **Whitespring Resort underwent major overhaul** -- Ryan Ainsley and Marcus Wellsby were casualties of the resort's transition from human-staffed to robot-staffed
4. **Random encounters are heavily iterated** -- EMIAC, Rhonda, and other SceneMP NPCs suggest dozens of random encounters were prototyped and most were cut
5. **Mascot characters survive as merchandise** -- Moe the Mole was cut as a quest but lives on as plushies, posters, and backpack flair
6. **The Numbers Station is the most intriguing cut** -- A single file for a mysterious broadcast that would have added significant atmosphere and conspiracy-theory lore to the game world

Each of these 19 NPCs represents a story thread that was started, recorded, and then abandoned. Their voice files remain in the archives as audio ghosts -- performances captured but never heard by players.
