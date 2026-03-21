# FO76 Finding 067: Orphaned Voice Recordings -- 9,456 Ghost Voice Files

**Source**: All 14 voice BA2 archives (SeventySix - Voices.ba2 + 00-12 UpdateVoices.ba2)
**Cross-referenced against**: full_esm_dump.txt (62,407 INFO records), seventysix_ilstrings_en.txt (68,916 dialogue strings)
**Method**: Extract all voice file Form IDs from BA2 naming convention (`{FormID}_N.fuz`), compare against INFO records in ESM
**Date**: 2026-03-20

---

## Executive Summary

Of 57,676 unique voice Form IDs across all BA2 archives, **9,456 (16.4%) have no matching INFO record** in the current ESM. These are voice recordings that actors performed and Bethesda packaged into the game, but which are disconnected from any dialogue system -- true ghost data.

Of those 9,456 orphaned Form IDs, **8,913 have no reference of any kind anywhere in the ESM**. They exist only as .fuz audio files with nothing pointing to them. The remaining 543 have Form IDs that coincidentally match unrelated records (STAT, BOOK, SNDR objects) -- false collisions, not real references.

None of the orphaned Form IDs appear in the ilstrings (dialogue text) file either, meaning their spoken text has also been removed. These lines were recorded, packaged, but then had both their ESM records AND their text strings deleted.

---

## Archive Distribution

| Archive | Unique IDs | Orphaned | % | Notes |
|---------|-----------|----------|---|-------|
| **SeventySix - Voices.ba2** | 54,556 | 21,889 files | 40.1% | Launch archive, bulk of orphans |
| 00UpdateVoices.ba2 | 598 | 0 | 0% | Clean |
| 01UpdateVoices.ba2 | 602 | 0 | 0% | Clean |
| 02UpdateVoices.ba2 | 760 | 0 | 0% | Clean |
| 03UpdateVoices.ba2 | 726 | 0 | 0% | Clean |
| 04UpdateVoices.ba2 | 1,896 | 0 | 0% | Wastelanders |
| 05UpdateVoices.ba2 | 1,151 | 0 | 0% | Clean |
| 06UpdateVoices.ba2 | 1,062 | 0 | 0% | Clean |
| 07UpdateVoices.ba2 | 725 | 0 | 0% | Clean |
| 08UpdateVoices.ba2 | 1,792 | 0 | 0% | Clean |
| 09UpdateVoices.ba2 | 650 | 0 | 0% | Clean |
| **10UpdateVoices.ba2** | 2,655 | 19 | 0.7% | Moe (8), Kevin (8), narrator (2), Strategist (1) |
| **11UpdateVoices.ba2** | 1,963 | 8 | 0.4% | Kevin (8) |
| 12UpdateVoices.ba2 | 935 | 0 | 0% | Clean |

**Key insight**: 99.8% of orphaned voice files are in the original launch archive. The update archives are nearly spotless -- Bethesda's post-launch pipeline is clean. The 27 orphaned files in Updates 10-11 belong to Moe the Mole (a confirmed CUT quest) and Kevin (Skyline Valley iterative cuts).

---

## Category 1: Generic Voice Types (7,789 orphaned -- 82.4% of total)

The largest group of orphaned files belongs to generic voice types used for combat grunts, ambient dialogue, and NPC barks. These are Fallout 4 legacy voice assets inherited by FO76 but never connected to the INFO system:

| Voice Type | Orphaned | Total | % Orphaned |
|-----------|----------|-------|------------|
| robotmrhandy | 3,018 | 3,854 | 78.3% |
| malerough | 2,080 | 2,130 | 97.7% |
| maleeventoned | 1,139 | 1,187 | 96.0% |
| maleghoulcombatant01 | 446 | 446 | **100.0%** |
| femaleeventoned | 386 | 405 | 95.3% |
| femalerough | 293 | 315 | 93.0% |
| robotprotectron | 239 | 1,361 | 17.6% |
| maleold | 154 | 230 | 67.0% |
| maleghoul | 130 | 160 | 81.2% |
| malechild | 111 | 134 | 82.8% |
| femalechild | 85 | 108 | 78.7% |
| femaleghoul | 86 | 94 | 91.5% |
| robotmrgutsy | 77 | 480 | 16.0% |
| robotmsnanny | 69 | 310 | 22.3% |
| femaleold | 60 | 75 | 80.0% |
| robotassaultron | 52 | 367 | 14.2% |
| robotsentrybot | 20 | 223 | 9.0% |
| roboteyebot | 7 | 47 | 14.9% |

**Analysis**: The `maleghoulcombatant01` voice type is 100% orphaned (446 lines, zero connected). This was likely a dedicated feral ghoul combat voice type from Fallout 4 that was never wired into FO76's creature dialogue system. The `malerough` and `maleeventoned` types are 95-98% orphaned -- these are FO4 settler voice types that FO76 replaced with its own named NPC system.

The `robotmrhandy` type has 3,018 orphaned lines (78% of its total), suggesting FO76 recycled Mr. Handy lines from FO4 but only connected ~850 of them to actual dialogue.

---

## Category 2: Named NPCs with Cut Dialogue (1,667 orphaned)

These are the notable orphaned lines -- they belong to specific, named characters and likely represent cut quest content, removed dialogue branches, or iterative development cuts.

### Tier 1: Major NPCs with 50+ Orphaned Lines

| NPC | Character | Orphaned | Total | % | Context |
|-----|-----------|----------|-------|---|---------|
| w05_npcm_comp_beckett_main | **Beckett** (companion) | 156 | 1,287 | 12.1% | Cut companion dialogue |
| babylon01_npcm_zax | **ZAX** (Nuclear Winter AI) | 90 | 280 | 32.1% | Nuclear Winter cut content |
| w05_npcf_astronaut_sofiadaguerre | **Sofia Daguerre** (companion) | 87 | 1,446 | 6.0% | Cut companion dialogue |
| robotmodus | **MODUS** (Enclave AI) | 73 | 533 | 13.7% | Cut Enclave content |

**Beckett (156 orphaned lines)**: The most cut companion dialogue. Beckett was Wastelanders' companion with the Blood Eagle backstory. 156 voice recordings -- roughly 12% of his total -- were cut. This suggests at least one entire conversation tree or personal quest stage was removed. His visitor Ronny also has 32 orphaned lines (50% of her total), and the Blood Eagle holotape characters have 14 more orphaned lines (50% of theirs). Beckett's storyline was clearly more extensive than what shipped.

**ZAX / Nuclear Winter AI (90 orphaned lines)**: 32% of ZAX's voice recordings are orphaned. Combined with Finding 016 (Nuclear Winter Full Autopsy), this confirms that the Nuclear Winter game mode had substantially more ZAX commentary and match narration than what players ever heard. The `babylon01` prefix confirms these are Nuclear Winter-era recordings.

**Sofia Daguerre (87 orphaned lines)**: 87 cut recordings for the Astronaut companion. Like Beckett, this represents cut personal quest content or conversation branches that were trimmed before Wastelanders shipped.

**MODUS (73 orphaned lines)**: The Enclave AI has 73 orphaned voice recordings (13.7% of total). Given Finding 029's documentation of cut Enclave quests, these likely belong to removed Enclave storyline branches.

### Tier 2: Named NPCs with 10-49 Orphaned Lines

| NPC | Character | Orphaned | Total | % | Context |
|-----|-----------|----------|-------|---|---------|
| w05_npcf_duchess_wayward | **Duchess** (Wayward bartender) | 37 | 542 | 6.8% | Cut Wayward dialogue |
| dlc01robotcompanionbleep A/B/C | **Automatron Bleep robots** | 33 each | 66 each | 50.0% | FO4 carryover, half unused |
| w05_npcf_comp_beckett_visitor_ronny | **Ronny** (Beckett's visitor) | 32 | 64 | 50.0% | Half of Ronny's lines are cut |
| w05_npcm_comp_lite_raiderpunk | **Punk** (CAMP ally) | 29 | 644 | 4.5% | Cut ally dialogue |
| w05_npcm_genericraider03 | Generic Raider Male | 20 | 377 | 5.3% | Cut raider barks |
| u03_npcm_athleticsinstructor | **Athletics Instructor** (Vault 76) | 16 | 40 | 40.0% | Vault 76 tutorial cut content |
| w05_npcm_paige | **Paige** (Foundation leader) | 13 | 172 | 7.6% | Cut Foundation dialogue |
| w05_npcf_jen | **Jen** (Raider ally) | 13 | 191 | 6.8% | Cut Crater dialogue |
| npcm_lc060_ryanainsley | **Ryan Ainsley** (Whitespring) | 11 | 11 | **100.0%** | Entirely cut NPC |
| robotprotectron_twg01_surveybot | **Survey Bot** | 10 | 10 | **100.0%** | Entirely cut robot |
| roboteyebot_cbz13_drillsergeant | **Drill Sergeant Eyebot** | 10 | 10 | **100.0%** | Cut military robot |
| w05_npcm_fisher | **Fisher** (Raider) | 10 | 101 | 9.9% | Cut raider quest dialogue |
| nwot_npcm_gunther | **Gunther** (NW on Tour) | 10 | 102 | 9.8% | Cut Wild West show dialogue |
| u03_npcm_swimminginstructor | **Swimming Instructor** (Vault 76) | 11 | 31 | 35.5% | Vault 76 tutorial cut |

### Tier 3: Named NPCs with 3-9 Orphaned Lines

| NPC | Character | Orphaned | Total | % | Context |
|-----|-----------|----------|-------|---|---------|
| npcm_rogermaxson | **Roger Maxson** (BoS founder) | 9 | 49 | 18.4% | Cut Brotherhood holotape/quest content |
| announcerf_mtrg01_payrollterminal | **Payroll Terminal** | 9 | 9 | **100.0%** | Entirely cut terminal voice |
| npcm_sf07_moe | **Moe the Mole** (mascot NPC) | 8 | 8 | **100.0%** | Confirmed CUT quest: SF07_MoeDigsSafety |
| storm_npcm_kevin | **Kevin** (Skyline Valley) | 8 | 53 | 15.1% | Iterative Skyline Valley cuts |
| w05_npcm_roper_mq002p_radical | **Roper** (Radical) | 8 | 184 | 4.3% | Cut Free Radicals dialogue |
| w05_npcm_caravan_rudy | **Rudy Fernandez** (Caravan) | 8 | 77 | 10.4% | Cut caravan quest content |
| w05_npcf_comp_beckett_holotape_bloodeaglef | Blood Eagle Female | 8 | 16 | 50.0% | Cut Blood Eagle holotapes |
| moon_herd_npcf_vera | **Vera** (Blue Moon event) | 7 | 119 | 5.9% | Cut Blue Moon content |
| npcf_fs_abbie | **Abbie** (Free States) | 7 | 61 | 11.5% | Cut Free States quest dialogue |
| robotraiderrose | **Rose** (Top of the World) | 7 | 298 | 2.3% | Cut Rose dialogue |
| w05_robotf_astronaut_athena | **ATHENA** (Astronaut robot) | 7 | 93 | 7.5% | Cut astronaut questline dialogue |
| dlc03robotrobobrain | **Robobrain** (DLC03 type) | 6 | 6 | **100.0%** | Entirely cut robot voice |
| w05_npcm_comp_beckett_holotape_bloodeaglem | Blood Eagle Male | 6 | 12 | 50.0% | Cut Blood Eagle holotapes |
| storm_npcm_hugo | **Hugo Stolz** (Skyline Valley) | 5 | 332 | 1.5% | Minor Skyline Valley cuts |
| robotprotectron_sfg01_announcer | **SFG01 Announcer** | 5 | 5 | **100.0%** | Entirely cut robot |
| roboteyebot_cbz13_robotic | **CBZ13 Robot Eyebot** | 5 | 5 | **100.0%** | Cut military eyebot |
| robotmrhandy_pennington | **Pennington** (Wayward robot) | 5 | 34 | 14.7% | Cut Wayward robot dialogue |
| w05_npcm_sergeantradcliff | **Sgt. Radcliff** (BoS) | 5 | 115 | 4.3% | Cut Brotherhood quest dialogue |
| bs00_paladinradio_voicetype | **Paladin Radio** (BoS) | 5 | 5 | **100.0%** | Entirely cut BoS broadcast |
| mile_npcf_strategist | **Strategist** (Milepost Zero) | 5 | 174 | 2.9% | Cut Milepost Zero content |
| w05_npcf_penelopehornwright | **Penelope Hornwright** | 3 | 199 | 1.5% | Minor cuts |
| w05_npcf_spymochou | **Mochou** (spy NPC) | 3 | 30 | 10.0% | Cut espionage dialogue |
| npcm_lc060_marcuswellsby | **Marcus Wellsby** (Whitespring) | 3 | 3 | **100.0%** | Entirely cut NPC |
| nwot_npcf_chloetheclown | **Chloe the Clown** (NW on Tour) | 3 | 26 | 11.5% | Cut carnival dialogue |
| announcerf_mtr05_motherlode | **Motherlode** announcer | 3 | 47 | 6.4% | Cut Motherlode dialogue |
| mile_npcf_brahmintamer | **Brahmin Tamer** (Milepost Zero) | 3 | 136 | 2.2% | Minor cuts |

---

## Category 3: Completely Cut NPCs (100% Orphaned)

These NPCs have voice recordings in the BA2 archives but **zero** connected INFO records -- every line was cut:

| NPC | Character | Lines | Analysis |
|-----|-----------|-------|----------|
| maleghoulcombatant01 | Feral Ghoul Combat | 446 | FO4 legacy voice type, never connected |
| npcm_lc060_ryanainsley | **Ryan Ainsley** | 11 | Whitespring architect (LC060 = Whitespring Resort). Voiced but never appeared as an interactive NPC. The strings file mentions him as "Lead Architect Ryan Ainsley" who designed The Springhill golf course |
| roboteyebot_cbz13_drillsergeant | **Drill Sergeant Eyebot** | 10 | Military drill sergeant eyebot (CBZ13 = robot event system). Quest `CBZ13_Robots` exists in ESM with shutdown scene |
| robotprotectron_twg01_surveybot | **Survey Bot** (TWG01) | 10 | Survey/mapping protectron, entirely orphaned |
| announcerf_mtrg01_payrollterminal | **Payroll Terminal** | 9 | Automated payroll system with voice, completely cut |
| npcm_sf07_moe | **Moe the Mole** | 8 | **Confirmed CUT quest**: `SF07_MoeDigsSafety_CUT_FlaggedToNotExportInScript`. Moe is a mascot character (NPC_ record: `SF07_MoeTheMole_VOICEONLY`). The quest involved Moe, radscorpions, and a "safety" theme. Had 3 scene variants (Scene1, SceneOne, SceneTest). Voice type was also explicitly cut: `_CUT_NPCM_SF07_MoeTheMole` |
| robotprotectron_sfg01_announcer | **SFG01 Announcer** | 5 | Announcer protectron at an unknown facility |
| roboteyebot_cbz13_robotic | **CBZ13 Robotic Eyebot** | 5 | Second cut eyebot from the CBZ13 military robot system |
| bs00_paladinradio_voicetype | **Paladin Radio** | 5 | Brotherhood of Steel radio broadcast NPC (`BS00_PaladinRadioQuest_01` and `_04` exist in ESM). A Paladin was meant to broadcast radio messages -- possibly a BoS radio station |
| npcm_lc060_marcuswellsby | **Marcus Wellsby** | 3 | Whitespring resort NPC. Strings mention "Mr. Wellsby volunteered to go talk with a couple of [people on the roads]" -- a pre-war Whitespring staffer who would have been interactive |
| dlc03robotrobobrain | **Robobrain** (DLC03) | 6 | DLC03 robobrain voice type. ESM explicitly marks it: `CUT_DONOTUSE_CreatureDialogueDLC03CrRobotRobobrain` |
| robotmsnanny_scenemp02_rhonda | **Rhonda** (Ms. Nanny) | 1 | Rhonda from the Rose questline -- 1 orphaned line |
| npcm_lc044_jeremiahward | **Jeremiah Ward** | 1 | A Ward family member (LC044 = a location quest). Single orphaned line |
| npcf_numberstation | **Number Station** | 1 | Automated number station broadcast voice |
| announcerm_ebs_radio | **EBS Radio** | 2 | Emergency Broadcast System announcer |
| announcerm_dq01_radiovoice | **DQ01 Radio Voice** | 1 | Daily quest radio announcer |
| 76trailervoicetype | **Trailer Voice** | 1 | Voice-over from the FO76 announcement trailer |

---

## Category 4: Cut Content Clusters by Update/Expansion

### Wastelanders Cuts (W05 prefix) -- 475 orphaned lines across named NPCs

The Wastelanders expansion (April 2020) has the most orphaned dialogue of any update. Key cut content clusters:

- **Beckett's storyline**: 156 (Beckett) + 32 (Ronny) + 14 (Blood Eagle holotapes) = **202 orphaned lines** from Beckett's questline alone. His Blood Eagle backstory was originally far more detailed.
- **Sofia Daguerre's storyline**: 87 (Sofia) + 7 (ATHENA) + 5 (Pandorabot) = **99 orphaned lines** from the Astronaut companion questline.
- **Duchess and the Wayward**: 37 (Duchess) + 5 (Pennington robot) + 2 (Mort) + 1 (Sol) = **45 orphaned lines** from the Wayward tavern. Cross-references Finding 029's documentation of cut Jide & Gracie bar conversations.
- **Foundation/Settlers**: 13 (Paige) + 3 (Penelope Hornwright) + 8 (generic settlers) = **24 orphaned lines**. Supports Finding 029's cut Settler daily quests.
- **Crater/Raiders**: 13 (Jen) + 10 (Fisher) + 8 (Roper) + 7 (Rose) + 32 (generic raiders) = **70 orphaned lines**.
- **Spy Mochou**: 3 orphaned lines for this espionage-themed NPC.

### Skyline Valley Cuts (Storm prefix) -- 13 orphaned lines

- **Kevin**: 8 orphaned lines (15.1%), found in both Update 10 and 11 archives
- **Hugo Stolz**: 5 orphaned lines (1.5%), minor iterative cuts

### Once in a Blue Moon Cuts (MOON prefix) -- 7 orphaned lines

- **Vera**: 7 orphaned lines from the Blue Moon herd event

### Nuka-World on Tour Cuts (NWOT prefix) -- 14 orphaned lines

- **Gunther**: 10 orphaned lines (9.8%) from the Wild West show
- **Chloe the Clown**: 3 orphaned lines from carnival content

### Milepost Zero Cuts (MILE prefix) -- 8 orphaned lines

- **Strategist**: 5 orphaned lines
- **Brahmin Tamer**: 3 orphaned lines

### Expeditions Cuts (XPD prefix) -- 8 orphaned lines

- **Responder Medic**: 3 orphaned lines
- **Sal**: 3 orphaned lines
- **Wicker**: 2 orphaned lines

---

## Category 5: Key NPC Status Check

### The Smiling Man
- **Voice type**: `RE_Scene_Cold_SmilingManVoiceType` (0x0068EB59)
- **NPC record**: `RE_Scene_Cold_SmilingMan` (0x0068EB57)
- **Voice files found**: 5 (Form IDs 0x0068EB50-0x0068EB55)
- **Orphaned**: **ZERO**. All 5 voice files have matching INFO records.
- **Status**: The Smiling Man's dialogue is fully connected. This mysterious random encounter NPC has exactly the content Bethesda intends.

### The Fisherman (Fisher)
- **W05_Raider_Fisher** (0x0040D481): The Wastelanders raider Fisher has 10 orphaned lines out of 101 total (9.9%). His cut content includes dialogue from the MQ_102P quest chain.
- **Fish_Vendor_TheFisherman** (0x007AC576): The fishing system's Fisherman vendor has **ZERO** orphaned lines. All dialogue is connected.
- **Bounty Fisherman** variants: Active bounty target NPCs, all connected.

### Ward (Foundation)
- **Ward** does not have a dedicated orphaned voice type. Ward's dialogue is under the Foundation settler system and appears fully connected.
- **Jeremiah Ward** (`npcm_lc044_jeremiahward`): A different Ward -- 1 orphaned line, 100% cut. Likely a relative or ancestor.

### Duchess
- 37 orphaned lines (6.8% of 542 total). The Wayward bartender had notably more dialogue planned.

### Paige
- 13 orphaned lines (7.6% of 172 total). Foundation's leader had additional dialogue cut.

### Rahmani
- Rahmani (Steel Dawn BoS) does not appear in the orphaned data. Her dialogue appears fully connected.
- However, **Sgt. Radcliff** (BoS) has 5 orphaned lines, and the **Paladin Radio** broadcast has 5 entirely orphaned lines -- suggesting cut Brotherhood of Steel radio content.

### Rose
- 7 orphaned lines (2.3% of 298 total). Minor cuts to the Top of the World raider queen.

### Roger Maxson
- 9 orphaned lines (18.4% of 49 total). The Brotherhood of Steel founder holotapes had additional recordings that were cut. Given his importance to FO76's BoS lore, these could contain cut backstory.

---

## Category 6: The Moe the Mole Investigation

The most clearly documented cut NPC quest in the orphaned data:

**Quest**: `SF07_MoeDigsSafety` -- explicitly flagged `CUT_FlaggedToNotExportInScript`
**NPC**: `SF07_MoeTheMole_VOICEONLY` (0x0034142E) -- a voice-only mascot character
**Voice Type**: `_CUT_NPCM_SF07_MoeTheMole` (0x0034142F) -- doubly confirmed as cut

**What the ESM records reveal**:
- The quest involved radscorpions (both `SF07LvlRadscorpionLarge` and `SF07LvlRadscorpionSmall` NPCs exist)
- It had creature spawn markers and swarm markers
- Three scene variants were built (Scene1, SceneOne, SceneTest) -- suggesting iterative development
- There was a `SF07_Costume` alias and a `SF07_ScorpionChatter` keyword
- The quest name "MoeDigsSafety" suggests a safety/mining theme with digging
- 8 voice lines were recorded and packaged but all 8 are completely orphaned

**Interpretation**: Moe the Mole was going to voice-narrate a quest about radscorpion safety in the mines, likely at the Moe the Mole animatronic location. The quest was built with multiple scene iterations but ultimately cut entirely. The voice recordings remain as the only evidence the quest was ever voiced.

---

## Category 7: Vault 76 Tutorial Cuts

Two Vault 76 tutorial NPCs have significant orphaned content:

- **Athletics Instructor** (`u03_npcm_athleticsinstructor`): 16 of 40 lines orphaned (40%)
- **Swimming Instructor** (`u03_npcm_swimminginstructor`): 11 of 31 lines orphaned (35.5%)

These instructors were part of the Vault 76 new-player tutorial system. Given Finding 035's documentation of the `NPE_MQ01_Enjoy` VR tutorial rework, these orphaned lines likely represent either the original pre-Skyline Valley tutorial content or iterative cuts from the reworked system. 40% of the Athletics Instructor's dialogue being cut suggests major tutorial restructuring.

---

## Statistical Summary

| Category | Orphaned Lines | % of Total |
|----------|---------------|------------|
| Generic voice types (FO4 legacy) | 7,789 | 82.4% |
| Named NPCs (cut quest dialogue) | 1,667 | 17.6% |
| **Total orphaned** | **9,456** | **100%** |
| **Total voice Form IDs** | **57,676** | |
| **Orphan rate** | **16.4%** | |

| Metric | Count |
|--------|-------|
| Unique NPCs with voice files | 1,044 |
| NPCs with at least 1 orphaned line | 143 |
| NPCs with 100% orphaned lines | 23 |
| Named NPCs with 100% orphaned lines | 14 |
| Confirmed CUT quests linked to orphans | 3 (SF07_MoeDigsSafety, CUT_DONOTUSE_DLC03Robobrain, BS00_PaladinRadio) |

---

## Cross-References to Existing Findings

- **Finding 016** (Nuclear Winter Full Autopsy): ZAX's 90 orphaned lines corroborate the extensive Nuclear Winter cut content
- **Finding 025** (Cut Content Validated): The zzz_ disabled records align with orphaned voice data for Storm, MOON, NWOT, and MILE prefixes
- **Finding 029** (Unreleased Quests): Cut Wayward conversations, Settler dailies, and Foundation content confirmed by orphaned Duchess/Paige/Settler voice lines
- **Finding 035** (Hidden Dialogue): The Vault 76 tutorial rework (NPE_MQ01_Enjoy) connects to the Athletics/Swimming Instructor orphaned lines
- **Finding 017** (Update Archive Analysis): The clean update archives (0% orphan rate for most) vs. the 40% orphan rate in the launch archive shows Bethesda's voice pipeline improved dramatically post-launch

---

## Novel Findings Not Previously Documented

1. **Beckett's cut storyline scope**: 202 total orphaned lines across Beckett + associated NPCs reveals his Blood Eagle backstory was ~15% larger than what shipped
2. **Paladin Radio broadcast**: An entirely cut Brotherhood of Steel radio station with 5 recorded lines -- never documented as cut content
3. **Ryan Ainsley and Marcus Wellsby**: Two Whitespring resort NPCs with fully recorded dialogue (14 lines total) who were voiced but never made interactive
4. **Moe the Mole voiced quest**: SF07_MoeDigsSafety had 8 voice recordings for a radscorpion safety quest that was completely cut
5. **Payroll Terminal**: A 9-line voiced payroll system terminal that was entirely scrapped
6. **Survey Bot (TWG01)**: A 10-line mapping/survey protectron with no remaining quest references
7. **The generic voice type inheritance problem**: FO76 inherited ~7,800 voice files from Fallout 4's generic voice system but never connected them, leaving them as permanent dead weight in the archives
8. **The Smiling Man is NOT orphaned**: Despite community speculation about hidden content, all 5 of the Smiling Man's voice recordings are properly connected to INFO records
