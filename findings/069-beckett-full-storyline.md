# FO76 Finding 069: Beckett's Complete Original Storyline -- Shipped & Cut Content Reconstruction

**Source**: 1,654 orphaned voice files (Beckett) + 77 (Ronny), full ESM dump, ilstrings, strings, decompiled scripts
**Method**: Cross-referencing voice file form IDs, DELETED_ quest records, quest stage NAM2 notes, SCFC designer comments, NPC records, and dialogue strings
**Date**: 2026-03-20
**Builds on**: Finding 068 (Cut Dialogue Reconstruction)
**Audio paths**: `~/ai-drive/gamecryptids/data/fallout76/orphaned_audio/wav/w05_npcm_comp_beckett_main/` (979MB, 1,654 files), `w05_npcf_comp_beckett_visitor_ronny/` (36MB, 77 files)

---

## Executive Summary

Beckett's companion storyline in Fallout 76 was originally designed as a **17-quest arc** with a radically different finale. The shipped version contains 15 quests (intro + 11 radiant story quests + camp quest + outro + 2 endgame radiants) set in Watoga Underground with a linear confrontation. The **original finale** was set at **Poseidon Energy Plant**, featured **two simultaneous villain targets** (The Bone AND The Claw), a **branching strategic choice** involving Edwin's gang, and a recruitment facility called **"The Nest."**

Seven quests were deleted during development:
1. `MurderBot` (Quest 011 alt) -- Kill a Blood Eagle "doctor's" reprogrammed surgical Assaultron
2. `BrotherClawHolotape` (Quest 012) -- Retrieve a holotape connecting Frankie to The Claw
3. `Ronny Visitor 013` -- A Ronny conversation at quest stage 10+
4. `BearHolotapeDatabase` (Quest 014) -- Retrieve/destroy the Triune's mobile dictation database
5. `Defector` (Quest 015) -- Rescue a Blood Eagle defector
6. `Formula` (Quest 007 alt) -- Fetch a Blood Eagle chem formula
7. `Sage Visitor 015` -- A second Sage conversation at quest stage 12+

An NPC named **Mariposa** (`DELETED_W05_COMP_Actor_Beckett_Hostile_Mariposa`, 0x00587A27) was cut -- a hostile female character likely named after the Fallout 1 military base, suggesting a Blood Eagle enforcer who underwent forced transformation (paralleling the original Mariposa's FEV experiments).

The complete voice recordings total approximately **3 hours 12 minutes** across 1,654 Beckett files and 77 Ronny files, covering shipped dialogue, cut dialogue, and multiple variant takes per line.

---

## The Blood Eagle Power Structure: The Triune

The Blood Eagles are led by a triumvirate called **The Triune**, consisting of three leaders with complementary functions:

| Title | Role | Shipped Fate | Original Fate |
|-------|------|-------------|---------------|
| **The Blood** | Recruiter -- gathers new members, stockpiles chems | Killed by player (Quest 005) | Same |
| **The Eye** | Intelligence -- extracts information, tortures for intel | Killed by player (Quest 011) | Same |
| **The Claw** | Enforcer -- tortures/breaks resistant recruits | Revealed as Frankie, Kill/Spare choice | Originally a separate villain alongside The Bone |
| **The Bone** | *CUT* -- Unknown specific role | N/A (does not exist in shipped) | Killed by Edwin's gang OR by player (branching choice) |

The Triune maintains a **mobile dictation database** that records their entire history, rituals, contacts, debts, chem formulas, and plans to control other Raider gangs and Settlers. This database was the target of the deleted Quest 014 ("BearHolotapeDatabase").

### The Bone: The Lost Fourth Leader

The Bone appears only in the deleted outro quest's designer notes:

> *"Player must kill the Bone and the Claw at the same time. They are at separate locations converting new batches of Blood Eagles from the Nest."*

This indicates The Bone was originally a **fourth Triune member** (making it a "Quadrumvirate" in the original design) or replaced one of the existing three. The Bone's function was **conversion** -- turning kidnapped victims into Blood Eagles at The Nest, likely through forced chem addiction and torture. The name "The Bone" evokes the stripping-down of identity (reducing a person to "bones") that the Blood Eagle brainwashing process represents.

When the finale was redesigned:
- The Bone was removed entirely
- The Triune was streamlined to three members: The Blood, The Eye, The Claw
- The Claw absorbed The Bone's narrative weight as the final boss
- The twist that Frankie IS The Claw was added (original version had "Brother" as a separate alias from the villains)

---

## Complete Quest Catalog

### Shipped Quests (15 total)

#### Phase 0: Introduction
**"Ally: [Intro Quest]"** -- `COMP_Quest_Intro_Full_Beckett` (0x00574625)
- Find Beckett imprisoned in a Blood Eagle holding cell
- Locate keys, free Beckett
- Retrieve Beckett's belongings (backpack)
- Build Beckett's Bar at your C.A.M.P.
- Reward: 80 Caps, 800 XP

#### Phase 1: Building Alliances (Quests 000-004)

| # | Quest ID | Quest Name | Type | Objective |
|---|----------|-----------|------|-----------|
| 000 | `Beckett_000_SadDiary` | **Ally: Dirty Little Secrets** | Fetch | Find Edwin's diary for Beckett -- stolen to impress the Eagles, now needed to mend fences |
| 001 | `Beckett_001_CultistSage` | **Ally: Exit Sage Left** | Rescue | Rescue Beckett's friend Sage from a Mothman cult |
| 002 | `Beckett_002_Key` | **Ally: Out Of Key** | Fetch | Steal Edwin's weapon cache key -- a traitor stole it to goad gangs into fighting |
| 003 | `Beckett_003_Bronx` | **Ally: Traitor's Demise** | Kill | Kill "Bronx," the traitor who stole Edwin's key |
| 004 | `Beckett_004_Cave` | **Ally: Supply And Demand** | Fetch | Steal Blood Eagles' Buffout supply from a cave |

**Narrative arc**: Beckett needs allies to take down the Blood Eagles. He rebuilds his relationship with Edwin's gang (a more reasonable Raider group) by returning Edwin's stolen diary and resolving internal gang problems. Simultaneously, he reconnects with Sage, an ex-lover who joined a Mothman cult and now perceives things "differently."

#### Phase 2: Striking the Blood Eagles (Quests 005-010)

| # | Quest ID | Quest Name | Type | Objective |
|---|----------|-----------|------|-----------|
| 005 | `Beckett_005_Blood` | **Ally: Spilling Blood** | Kill | Kill The Blood (first Triune leader) -- the recruiter |
| 006 | `Beckett_006_Pet` | **Ally: Pet Peeve** | Rescue | Rescue Edwin's "dog" (actually a Mole Rat) |
| 007 | `Beckett_007_DJ` | **Ally: Shooting Star** | Kill | Kill "Star," a mechanic recruited by Eagles to take over a radio station |
| 008 | `Beckett_008_MissNanny` | **Ally: Bot Of Gold** | Rescue | Rescue a Miss Nanny robot (connected to Beckett's guilt -- he killed a sick family for chems) |
| 009 | `Beckett_009_Holotapes` | **Ally: Sibling Piracy** | Fetch | Retrieve holotapes from Foundation seeking info about Frankie |
| 010 | `Beckett_010_PoisonedFood` | **Ally: Needs Of The Many** | Fetch | Stop Blood Eagles from poisoning Settler food supplies |

**Narrative arc**: Beckett systematically dismantles the Blood Eagles. He kills The Blood (the recruiter), disrupts their radio propaganda campaign (Star), steals their chem supplies, and prevents their biological warfare against Settlers. The Miss Nanny quest forces Beckett to confront his worst memory -- murdering a sick family for their chems. Sage visits the camp and delivers a cryptic oracle: *"The Claw is meant for you, and it is exactly where your heart left it."*

#### Phase 3: The Eye (Quest 011)

| # | Quest ID | Quest Name | Type | Objective |
|---|----------|-----------|------|-----------|
| 011 | `Beckett_011_Eye` | **Ally: Eye For An Eye** | Kill | Kill The Eye at the "Bear Cave" (his torture lab) |

**Narrative arc**: Beckett sends the player to kill The Eye, the Blood Eagle intelligence extractor, at his laboratory in a place called the Bear Cave. The Eye recorded his torture sessions on holotapes. Beckett references "The Lab" and its "stench of death." Sage visits again and helps decode what the holotapes mean. This leads to the revelation that Frankie is held by The Claw.

#### Phase 4: Camp & Outro

**"Ally: An Eagle Flies Free"** -- `COMP_Quest_Camp_Full_Beckett` (0x00582162)
- Camp management quest with visitor interactions (Sage, Ronny, Frankie post-game)
- Tracks romance progression through affection ranks
- Stages: Ready for Outro Scene -> Back From Outro -> Romance Scene Resolved -> Quest Completes

**"Ally: Thicker Than Water"** -- `COMP_Quest_Outro_Full_Beckett` (0x005A05DE) -- SHIPPED VERSION
- Location: **Watoga Underground** (underground parking garage complex)
- Ronny's gang provides backup
- The twist: **Frankie IS The Claw**
- Player choice: Kill or Spare Frankie
- 4 scene variants: `KillFrankie`, `SaveFrankie`, `FrankieDead`, `FrankieLives`

#### Endgame Radiants (repeatable)

| Quest ID | Quest Name | Type |
|----------|-----------|------|
| `Beckett_BloodEagleRandomLoc` | **Ally: Loose Ends** | Kill Blood Eagles at random location |
| `Beckett_BloodEagleDungeon` | **Ally: Loose Ends** | Kill Blood Eagles in dungeon |

Plus generic radiants: `Ally: Stalking Stuffer` (Fetch), `Ally: Cropping Spree` (Kill generic), `Ally: Saving Skin` (Rescue).

---

### Deleted Quests (7 total)

#### Quest 007 (alt): The Formula
**ID**: `DELETED_COMP_RQ_Fetch_SpecificAliases_Beckett_007_Formula` (0x0058215C)
**Type**: Fetch
**Item**: `DELETED_W05_COMP_RQ_Beckett_Fetch_Formula` (0x0059671F)
**Analysis**: An alternate version of Quest 007 where instead of killing "Star" the DJ, the player would retrieve a Blood Eagle chem formula. This was likely the recipe for the chems used to brainwash recruits. Replaced by the more dramatic radio station assault ("Shooting Star").

#### Quest 011 (alt): Murder Bot
**ID**: `DELETED_COMP_RQ_Kill_SpecificAliases_Beckett_011_MurderBot_OBSOLETE` (0x00582166)
**Type**: Kill
**Target**: A Blood Eagle "doctor's" reprogrammed robot
**Designer note**: *"Doctor is excited about his murder bot that has a 85% success rate at removing limbs and teeth. I really want them to sound smiley here."*
**Related dialogue**: *"She does amputations too. From what I understand it wasn't too hard to overwrite her programming. And she has an 85% success rate!"*
**Analysis**: The "Murder Bot" was a reprogrammed Miss Nanny or Assaultron serving as The Eye's surgical assistant, performing forced amputations and tooth extractions on prisoners. The quest occupied the same slot as "Eye For An Eye" (both numbered 011), meaning it was an earlier version of the Eye confrontation. The original concept had the player destroy the torture robot separately before confronting The Eye himself. The "smiley" voice direction suggests the Blood Eagle doctor was enthusiastically proud of his creation -- a darkly comic horror moment.

The NPC record `COMP_Beckett_RQ05_Name` (0x005A1C07) was referenced as the TargetActor, suggesting the Murder Bot had its own named identity within the Blood Eagles.

#### Quest 012: Brother Claw Holotape
**ID**: `DELETED_COMP_RQ_Fetch_SpecificAliases_Beckett_012_BrotherClawHolotape` (0x00582169)
**Type**: Fetch
**Quest Display Name**: "Beckett's Quest 12"
**Analysis**: Retrieve a holotape that revealed the connection between Frankie (Beckett's brother) and The Claw. In the original storyline, this was a separate discovery quest -- the player found evidence linking Frankie to The Claw before the finale. In the shipped version, this revelation happens during the finale itself as a dramatic twist.

#### Quest 013: Ronny Visitor Conversation
**ID**: `DELETED_COMP_Conversation_Beckett_Visitor_013_Ronny` (0x0058216D)
**Condition**: Triggers at relationship progress >= 10
**Uses NPC**: `DELETED_W05_COMP_Actor_Beckett_Visitor_Ronny` (0x00587A28)
**Analysis**: A camp visitor scene where Ronny arrives to brief Beckett on intelligence. The deleted Ronny NPC actor (0x00587A28) was replaced by the instanced version (0x005A0615) that shipped. This conversation likely delivered critical intel about The Bone and/or The Claw's locations at The Nest. Its deletion corresponds to the removal of The Bone from the storyline.

#### Quest 014: Bear Holotape Database
**ID**: `DELETED_COMP_RQ_Fetch_SpecificAliases_Beckett_014_BearHolotapeDatabase` (0x005966FB)
**Type**: Fetch
**Quest Display Name**: "Beckett's Quest 14"
**Analysis**: Retrieve or destroy the Triune's mobile dictation database. Beckett describes it: *"I know that it's a mobile recorder that moves between the Triune members, takes dictation, then moves on. Constantly."* And: *"This stores the entire history of the Triune, all of their rituals, all of their contacts and owed deeds... any other formulas... And it also has their entire plans for how they can control the rest of the Raiders next, then the Settlers. Without this, they are just raging assholes with no direction, no vision, no goals."*

The dialogue for this quest **survived in the shipped game** (ilstrings 61005C2A-61005C33) even though the quest was deleted. This is significant -- the voice recordings were made and the text was committed to the string tables, but the quest was never activated.

#### Quest 015: Defector Rescue
**ID**: `DELETED_COMP_RQ_Rescue_SpecificAliases_Beckett_015_Defector_OBSOLETE` (0x00582159)
**Type**: Rescue
**Analysis**: Rescue a Blood Eagle defector. This quest was explicitly marked "OBSOLETE" in addition to "DELETED," suggesting it was cut early in development. A defector rescue would have provided intelligence about The Nest and the conversion process, feeding into the branching finale. The "15" numbering places it after all other story quests, meaning it was designed as the penultimate quest before the finale.

#### Sage Visitor 015 Conversation
**ID**: `DELETED_COMP_Conversation_Beckett_Visitor_015_Sage` (0x0058216C)
**Condition**: Triggers at relationship progress >= 12
**Analysis**: A second visit from Sage late in the questline. At relationship level 12, this would have occurred just before the finale. Sage's cryptic wisdom would have provided the final piece of the puzzle before the assault on Poseidon/The Nest.

---

## The Original Finale: Poseidon Power Plant

### Quest Record

**ID**: `DELETED_COMP_Quest_Outtro_Full_Beckett` (0x00582161)
**Display Name**: "[Not Playable]" (string D90050C1 -- flagged as unplayable)
**Filter**: `Companions\Lite\`

### Quest Stages

```
--- SETUP ---
START: Quest

--- INTRO ---
TALK: to Beckett

[DESIGNER NOTE: Player must kill the Bone and the Claw at the same
time. They are at separate locations converting new batches of Blood
Eagles from the Nest. Player must pick: Send Edwin's gang to kill
the Bone, OR Send Edwin's gang to clear out extra Blood Eagles which
makes everything easier.]

FIND: Brother's Room
TALK: with Brother

--- MAIN ---
CHOICE has been made
   CHOICE: Edwin's Gang kills the Bone
   CHOICE: Edwin's Gang kills the Blood Eagles generally

--- END ---
> Success <
> Fail <
> Shut Down <
```

### Location Aliases

The deleted quest contains explicit references to **Poseidon Energy Plant**:

| Alias | Reference | Purpose |
|-------|-----------|---------|
| `XMarker_Poseidon_Exterior` | 0x00574BA6 | Exterior approach marker |
| `XMarker_Poseidon01_Interior` | 0x00574BA7 | Interior center marker (inside `PoseidonPlant01` cell) |
| `XMarker_Poseidon02_Interior_KeyRoom` | unassigned | Key room inside Poseidon |
| `XMarker_Jailcell` | 0x00574B9D | Prison cell (for Brother?) |
| `XMarker_Belongings` | 0x00574BA8 | In `PoseidonPlant01` cell |
| `XMarker_HoldingCell` | 0x00574BA4 | Secondary holding area |
| `JailKeys` | unassigned | Keys to free prisoner |
| `JailDoor` | 0x00574B9C | Door peer furniture (Beckett talks through door) |
| `Beckett` | -- | Beckett actor |
| `Brother` | unassigned | Frankie, held separately from The Claw |
| `Belongings` | -- | Items to retrieve |
| `spawnMarker` | 0x005693E9 | Enemy spawn point |

**Critical detail**: The `DefaultAliasOnDistanceLessThan` script on the quest triggers at 500 units from either the Poseidon exterior marker or the Poseidon01 interior marker. This confirms Poseidon was the intended dungeon for the original finale.

### The Branching Choice

The original finale presented a genuine **strategic dilemma**:

**Option A: Edwin's Gang kills The Bone**
- The player personally assaults The Claw's position
- Edwin's gang handles The Bone simultaneously
- The player faces The Claw alone (harder personal fight)
- The Bone is guaranteed dead (Edwin's gang succeeds)

**Option B: Edwin's Gang clears out extra Blood Eagles**
- The player must kill BOTH The Bone AND The Claw
- Edwin's gang thins out the general Blood Eagle forces
- "Makes everything easier" -- fewer enemies overall
- But the player must handle both bosses personally

This is a classic quantity-vs-quality trade-off: do you want the hard fight against one boss with guaranteed success on the other, or do you want an easier overall experience but have to personally kill both targets?

### Why "The Nest"?

The Nest was the Blood Eagle **recruitment/conversion facility**. The designer notes describe The Bone and The Claw as being "at separate locations converting new batches of Blood Eagles from the Nest." This tells us:

1. The Nest was a processing center where captured victims were brought
2. The Bone and The Claw ran parallel conversion operations
3. New "batches" implies an industrial-scale brainwashing operation
4. The conversion process involved forced chem addiction (Buffout, custom formulas)

The Nest likely occupied Poseidon Energy Plant's interior -- the industrial setting with multiple wings, a reactor room, maintenance areas, and basement levels would perfectly serve as a conversion factory. The existing ESM records for Poseidon include maintenance areas, reactor rooms, and multiple key rooms that the quest aliases reference.

---

## Who Was Mariposa?

**NPC Record**: `DELETED_W05_COMP_Actor_Beckett_Hostile_Mariposa` (0x00587A27)
**Display Name**: "Mariposa" (strings D9005102, D9005103)
**Hostility**: Explicitly hostile (unlike other Beckett visitors who are friendly)
**Race**: 0x00013746 (Human)

Mariposa was a **hostile NPC** in Beckett's storyline -- the only Beckett-associated character explicitly marked as an enemy. The name carries enormous weight in Fallout lore:

- **Mariposa Military Base** (Fallout 1): The facility where the U.S. government developed the Forced Evolutionary Virus (FEV), creating super mutants through involuntary human experimentation
- **Mariposa** means "butterfly" in Spanish -- metamorphosis, transformation

In the context of Beckett's Blood Eagle storyline, Mariposa was almost certainly a **Blood Eagle enforcer or conversion specialist** at The Nest. The name is a deliberate parallel: just as Mariposa Military Base forcibly transformed humans into super mutants, this character forcibly transformed kidnapped victims into Blood Eagles through chem-induced brainwashing.

Mariposa's hostile designation means the player would have fought her. She was likely:
- A boss-level enemy at The Nest
- The person who directly oversaw the chem-conversion process
- Possibly working under The Bone (who ran conversion operations)
- Named Mariposa either as her chosen Blood Eagle callsign (the "butterfly" -- she transforms people) or as a developer reference to the FEV facility

Her NPC record (0x00587A27) sits directly between Sage (0x00587A25), Frankie (0x00587A26), and the deleted Ronny (0x00587A28), meaning she was created in the same development pass as the core Beckett cast.

---

## Edwin's Gang: The Swing Factor

Edwin's gang is the linchpin of Beckett's entire strategy. Beckett cannot take down the Blood Eagles alone -- he needs an allied Raider force.

### Edwin
- Leader of a mid-tier Raider gang, one of the "bigger low-key raider gangs"
- "Sharpened his teeth into points" -- eccentric but not Blood Eagle-level crazy
- "Never made us do anything we didn't want to do" -- Beckett's former gang
- Loved a fat cat that the Blood Eagles killed, skinned, and cooked (sent the pelt back in a sack)
- Has "a ton of health issues" -- declining health, Edwin is fading
- Owns an embarrassing "sad diary" that Beckett stole to impress the Eagles

### Ronny
- Edwin's niece, functionally the gang's real leader for years
- After Edwin "retires" (due to health), Ronny takes full command
- "A thorn in the Blood Eagles' side forever. She's got it down to a damn art."
- Provides the key and intelligence for both the original and shipped finales
- Has 77 dedicated voice recordings (6 minutes 57 seconds)
- In the shipped finale, she bribes someone for a key to Watoga Underground

### The Alliance Path
Beckett's questline is essentially a **diplomatic campaign** to win Edwin's gang as allies:

1. **Quest 000**: Return Edwin's diary (mend fences)
2. **Quest 002**: Recover Edwin's stolen weapon cache key
3. **Quest 003**: Kill Bronx (the traitor who stole the key)
4. **Quest 006**: Rescue Edwin's "dog" (a Mole Rat he loves)
5. **Ronny contacts**: Regular updates from Ronny as trust builds
6. **Edwin retires**: His health fails, Ronny takes full command
7. **Finale**: Ronny brings the entire gang as backup

In the **original finale**, Edwin's gang played a far more critical role -- the branching choice literally determined whether they killed The Bone or cleared generic Blood Eagles.

---

## The Shipped Finale: Watoga Underground

### Quest Flow

**"Ally: Thicker Than Water"** (`COMP_Quest_Outro_Full_Beckett`, 0x005A05DE)

1. **Find Beckett in Watoga Underground** -- An underground parking garage complex
2. **Speak to Beckett** -- He's already inside with Ronny
3. **Proceed to the Garage Control Room** -- Navigate Blood Eagle-infested garage
4. **Ronny Leaves The Dungeon** -- She exits to rally her gang outside
5. **Open the Garage Door** -- Press button to let Ronny's gang in (player opens from inside)
6. **Clear the remaining Blood Eagles** -- Fight alongside Raider allies
7. **Confront The Claw** -- Frankie's door opens after Blood Eagles are dead
8. **The Twist**: Frankie IS The Claw

### The Frankie Revelation

The shipped finale's central twist is that Beckett's younger brother Frankie has become The Claw:

- **Frankie's NPC record**: `W05_COMP_Actor_Beckett_BloodEagle_Frankie` (0x00587A26) -- display name "The Claw" (string 61008818)
- **The quest alias**: `FrankieClaw` -- explicitly linking the two identities
- **Beckett's reaction**: *"No... no way. This doesn't make any sense! You're The Claw? How's that possible?"*
- **Explanation**: *"After the previous Claw got wiped out, and it was clear Frankie was one of the craziest in the gang at the time, he filled the spot."*
- **Frankie taunts**: *"Frankie's dead. You killed him, Beckett. By abandoning him, YOU pulled the trigger."*
- **The Claw philosophy**: *"The Claw lives within all of us, waiting for the moment it awakens and tears its way through our flesh only to burst forth anew! We're. ALL. The Claw."*

### The Kill/Spare Choice

The player advises Beckett on what to do with Frankie:

**Kill Frankie** (objective string: "Convince Beckett to kill his brother"):
- Scenes: `COMP_Quest_Outro_Full_Beckett_KillFrankie` -> `FrankieDead`
- Package: `W05_Beckett_ExecuteFrankie` (Beckett aims at and executes Frankie)
- ActorValue: `COMP_AV_Beckett_FrankieDies` tracks this choice
- Frankie's death dialogue: *"Frankie? No... no, no, no, no. Frankie's dead. You killed him, Beckett."*
- Beckett's aftermath: *"Sigh. Look, uh. I need some... time. To bury my brother and get myself together, okay?"*
- *"He was my kid brother, watching me having the time of my life in these stupid raider gangs instead of trying to make an honest living."*

**Spare Frankie** (objective string: "Convince Beckett to spare his brother's life"):
- Scenes: `COMP_Quest_Outro_Full_Beckett_SaveFrankie` -> `FrankieLives`
- Beckett appeals to Frankie's memories: *"We're family and I love you, Frankie. Always have, always will."*
- Uses childhood memories: *"You fought off those dogs with nothing but a goddamn broken baseball bat. It almost killed you, man. You... you saved me."*
- Frankie responds: *"I love you too, Beckett. And... and I'm sorry. Sorry for everything."*
- *"The hell... happened to me, Beckett? God, this hurts... it hurts so much..."*
- Recovery: Frankie is sent to Ronny's camp, addiction recovery
- *"Ronny said she'll kick his butt out of her camp the moment Frankie clears his head."*

### Post-Finale

- If Frankie lives: *"Had some news for you about Frankie."* -- He eventually reaches out, his mother is informed
- If Frankie dies: *"I talked to Ronny, and she's taken care of everything... you know, burying him and all that. I... just couldn't deal with it."*
- Beckett reflects on his future and the player can pursue romance
- Reward: Final Beckett's .50 Cal Machine Gun (`W05_COMP_Beckett_50CalMachineGun_QuestReward`)
- 80 Caps, 1200 XP

---

## What Changed: Original vs. Shipped Timeline

### Original Design (17+ quests, branching finale)

```
INTRO: Free Beckett from Blood Eagle prison
   |
PHASE 1: Build Edwin alliance (Quests 000-004)
   |-- 000: Dirty Little Secrets (Edwin's diary)
   |-- 001: Exit Sage Left (Rescue Sage)
   |-- 002: Out Of Key (Edwin's cache key)
   |-- 003: Traitor's Demise (Kill Bronx)
   |-- 004: Supply And Demand (Steal Buffout)
   |
PHASE 2: Strike Blood Eagles (Quests 005-010)
   |-- 005: Spilling Blood (Kill The Blood)
   |-- 006: Pet Peeve (Rescue Edwin's "dog")
   |-- 007: [ORIGINAL] Retrieve chem Formula
   |-- 007: [REVISED] Shooting Star (Kill Star the DJ)
   |-- 008: Bot Of Gold (Rescue Miss Nanny)
   |-- 009: Sibling Piracy (Holotapes from Foundation)
   |-- 010: Needs Of The Many (Stop poison plot)
   |
PHASE 3: Intel & Preparation (Quests 011-015) [MOSTLY CUT]
   |-- 011: [ORIGINAL] Kill MurderBot (The Eye's surgical Assaultron)
   |-- 011: [REVISED] Eye For An Eye (Kill The Eye directly)
   |-- 012: [CUT] Brother Claw Holotape (discover Frankie/Claw link)
   |-- 013: [CUT] Ronny Visitor (intel on The Bone's location)
   |-- 014: [CUT] Bear Holotape Database (destroy Triune records)
   |-- 015: [CUT] Defector Rescue (rescue Blood Eagle defector)
   |-- [CUT] Sage Visitor 015 (final cryptic guidance)
   |
FINALE: Assault on Poseidon Energy Plant / The Nest
   |-- Talk to Beckett
   |-- Enter Poseidon (trigger at 500 units)
   |-- Find Brother's Room (Frankie imprisoned)
   |-- Talk with Brother
   |-- BRANCHING CHOICE:
   |    |-- A: Send Edwin's gang to kill The Bone -> Player kills The Claw
   |    |-- B: Send Edwin's gang to clear Blood Eagles -> Player kills BOTH
   |-- Fight through The Nest (Blood Eagle conversion facility)
   |-- Face Mariposa (hostile enforcer)
   |-- Kill The Bone and/or The Claw
   |-- Success / Fail
```

### Shipped Design (15 quests, linear finale)

```
INTRO: Free Beckett from Blood Eagle prison
   |
PHASE 1: Build Edwin alliance (Quests 000-004) [UNCHANGED]
   |
PHASE 2: Strike Blood Eagles (Quests 005-010) [MINOR CHANGES]
   |-- Quest 007 changed from Formula fetch to DJ kill
   |
PHASE 3: The Eye (Quest 011 only)
   |-- Eye For An Eye (Kill The Eye at Bear Cave)
   |-- MurderBot removed, Quests 012-015 all cut
   |
FINALE: Watoga Underground
   |-- Linear dungeon crawl
   |-- Ronny provides garage key, brings gang as backup
   |-- Open garage door to let allies in
   |-- Clear Blood Eagles
   |-- TWIST: Frankie IS The Claw
   |-- Binary choice: Kill or Spare Frankie
   |-- No branching strategic element
   |-- The Bone doesn't exist
   |-- Mariposa doesn't exist
   |-- The Nest doesn't exist
```

---

## Why It Was Changed

The restructuring from the original to shipped version follows a clear development logic:

1. **Scope reduction**: 7 quests were cut (012-015 plus alternates), reducing the arc from ~17 to ~15 quests. The companion questlines had to ship with Wastelanders (Update 20) and needed to be completable alongside the main story.

2. **Emotional focus over strategic complexity**: The original branching choice (where to send Edwin's gang) was a tactical decision. The shipped Kill/Spare Frankie choice is a deeply personal moral dilemma. Bethesda chose emotional impact over strategic gameplay.

3. **The Frankie twist**: Making Frankie BE The Claw is narratively brilliant -- it transforms the entire questline into dramatic irony. Everything Beckett does to find and save his brother is simultaneously bringing him closer to having to confront/kill him. This twist didn't work as well with The Bone as a separate fourth villain diluting the focus.

4. **Location consolidation**: Poseidon Energy Plant is a large, complex location already used for a public event (Powering Up Poseidon). Using it for a companion finale would create conflicts with the public event system. Watoga Underground is a dedicated, self-contained dungeon with no competing uses.

5. **Mariposa's removal**: A named hostile NPC enforcer at The Nest was unnecessary once The Nest itself was cut. Mariposa's narrative function (representing the dehumanizing conversion process) was absorbed into The Claw's philosophy: *"The Claw lives within all of us, waiting for the moment it awakens and tears its way through our flesh."*

---

## Narrative Timeline: The Complete Beckett Story

### Beckett's Backstory
- Independent scavenger, struggled alone until joining gangs for survival
- Ran with the Hopkins Hooligans until Hopkins was killed
- Joined **Edwin's gang** -- "good booze, good people and good memories." Felt like "King Shit"
- Blood Eagles "recruited" (kidnapped) him into their gang through forced chem addiction
- Rose through Blood Eagle ranks as a chemist/enforcer
- Younger brother **Frankie** idolized Beckett's raider lifestyle
- Beckett had a relationship with **Sage**, who eventually joined a Mothman cult
- At his lowest: *"I killed them all for their chems and a couple of caps"* -- murdered a sick family, stole their Miss Nanny's medical supplies
- Eventually broke free of the Blood Eagle brainwashing: *"I'm one of three Blood Eagles to ever 'escape' their brainwashing and kick the chem habit. It was painful... it almost killed me."*
- Left the Blood Eagles, left Frankie at Foundation hoping he'd be safe
- Frankie didn't stay. He followed Beckett's footsteps into raider life.

### The Quest Arc
- Blood Eagles capture Beckett as punishment for leaving. Player frees him.
- Beckett opens a bar at the player's CAMP, begins planning his revenge
- Through 11 story quests, Beckett rebuilds his alliance with Edwin's gang, rescues old friends (Sage, various victims), and systematically eliminates Blood Eagle leadership (The Blood, The Eye)
- Sage delivers the crucial prophecy: *"The Claw is meant for you, and it is exactly where your heart left it"*
- Beckett eventually decodes this: *"It's almost as though he's tying The Claw and Frankie together. Holy shit! That's it. Sage was saying that Frankie is being held by The Claw!"*
- But the truth is worse than Beckett imagined

### The Finale
- Ronny secures entrance to Watoga Underground
- Player fights through Blood Eagles with Ronny's gang as backup
- Confronts The Claw -- discovers it's Frankie
- Frankie, broken by chem addiction and Blood Eagle indoctrination, has become The Claw
- *"After the previous Claw got wiped out, and it was clear Frankie was one of the craziest in the gang at the time, he filled the spot."*
- Player helps Beckett choose: kill his brother, or try to save him

### The Claw's Philosophy
The Blood Eagles' title system is explicitly fungible -- The Claw is not a person, it's a role:
- *"The Claw lives within all of us, waiting for the moment it awakens and tears its way through our flesh only to burst forth anew!"*
- *"We're. ALL. The Claw."*
- *"And so... a new Claw is reborn!"*
- *"The Claw demands a high price for failure. The price is suffering."*

This philosophy mirrors the Blood Eagle conversion process itself: strip away identity, replace it with the gang.

---

## Data Inventory

### Voice Recordings
| Character | Files | Duration | Orphaned % |
|-----------|-------|----------|------------|
| Beckett (main) | 1,654 | ~3h 12m | Mixed (shipped + orphaned) |
| Ronny (visitor) | 77 | ~7m | Mixed |
| **Total** | **1,731** | **~3h 19m** | -- |

1,287 unique dialogue form IDs across 1,654 files (multiple takes per line).

### ESM Records
- 640 total references to "Beckett" in the ESM
- 29 quest records (15 shipped, 7 deleted, 7 related/alternate)
- 11 Outro dungeon keywords (`COMP_Beckett_Outro_Dun01` through `_Dun11`) -- suggesting up to 11 dungeon layouts were considered
- 8 NPC records (5 active, 3 deleted including Mariposa)
- 3 holotape scenes (Ayla, Frankie, Blood)
- Poseidon markers still present in the shipped ESM (0x00574BA6, 0x00574BA7) despite the quest being deleted

### Strings
- Quest names recovered: 16 unique quest titles
- Dialogue text: Hundreds of lines survive in ilstrings even for deleted quests
- The deleted quest display name "[Not Playable]" (D90050C1) confirms the original outro was explicitly disabled

### Scripts
- 17 Beckett-related scripts survive in the decompiled data
- Key script: `qf_comp_quest_outro_full_bec_005a05de.psc` contains the full shipped finale logic
- `pf_w05_beckett_executefranki_005a179a.psc` contains the Frankie execution package
- `qf_comp_quest_outtro_beckett_01001fc6.psc` is a simplified version (possibly early prototype) with only jail/belongings logic

---

## Significance

This reconstruction reveals that Beckett's companion storyline underwent a **major structural revision** during development. The original design was more ambitious -- more quests, a branching finale, multiple villain targets, a named hostile NPC (Mariposa), and a dedicated location (Poseidon/The Nest). The shipped version traded breadth for emotional depth, centering the entire arc on the brotherly relationship between Beckett and Frankie.

The ghost data is extensive: Poseidon markers, Mariposa's NPC record, deleted quest skeletons, the Triune database dialogue, and MurderBot's voice direction all survive in the ESM. The dialogue strings for Quest 014 (BearHolotapeDatabase) are **fully intact** in the ilstrings -- meaning Beckett's voice actor recorded lines about the Triune's mobile database that players will never hear in normal gameplay.

The 1,654 voice files represent one of the largest single-character voice recording sets in the game. Cross-referencing with the 1,287 unique form IDs suggests hundreds of orphaned lines exist beyond what the shipped quests use. A systematic audio-to-text correlation would likely recover additional cut dialogue not represented in the strings files.

---

*Finding 069 | GameCryptids Project | Fallout 76 Companion Content Analysis*
