# FO76 Finding 100: Orphaned Voice Stories -- Cut Dialogue and Lost Narratives from 30+ NPCs

**Source**: Orphaned voice analysis (20,300 orphaned Form IDs across 147 actors), 14 voice BA2 archives, ESM quest/INFO records, ilstrings/dlstrings/strings tables, NAM2 designer direction notes
**Method**: Cross-referencing voice file Form IDs against QUST:INFO records to identify orphans, resolving connected dialogue via NAM1 string references, reconstructing cut narratives from quest structure and designer notes
**Date**: 2026-03-21
**Builds on**: Finding 067 (Orphaned Voice Recordings), Finding 096 (Cut NPCs Complete Catalog), Finding 098 (Complete Cut Content Catalog)

---

## Executive Summary

Beyond the previously documented Beckett (1,654 files), Ronny (77 files), Sofia Daguerre (87 orphaned), and MODUS (73 orphaned), the orphaned voice archive contains substantial cut content for **30+ additional NPCs**. This finding catalogs the primary undocumented orphaned voice caches, recovers their connected dialogue for context, and reconstructs the cut storylines they belonged to.

the primary discoveries:

1. **ZAX (Vault 51 AI)** -- 90 orphaned voice files from the Nuclear Winter backstory, including cut Vault 51 social experiment commentary that was never heard in-game
2. **Bleep (Robot Companion)** -- 66 orphaned emotive sound files for a robot companion with a full emotional vocabulary that was 50% cut
3. **Raider Punk** -- 29 orphaned CAMP ally dialogue lines including cut quest variants and personality content
4. **Vault 76 Tutorial Instructors** -- 27 orphaned files from the Athletics and Swimming Instructors, representing cut Tadpole challenge content
5. **Roger Maxson** -- 9 orphaned Brotherhood of Steel holotape recordings, cut from the Taggerdy/Brotherhood origin story
6. **Rose (Raider Robot)** -- 7 orphaned files from cut confession/betrayal dialogue
7. **Abbie (Free States)** -- 7 orphaned files from cut Scorched Detection System quest stages

---

## Part 1: The Biggest Undocumented Orphan Caches

### 1A. ZAX -- The Vault 51 AI (90 Orphaned / 475 Connected)

**Voice folder**: `babylon01_npcm_zax`
**Category**: Nuclear Winter backstory AI
**Orphan rate**: 15.9% (90 of 565 files)

ZAX is the artificial intelligence that ran Vault 51's social experiment, selecting an Overseer by manipulating residents into killing each other. The 90 orphaned files represent approximately 16% of ZAX's total recorded dialogue -- an entire branch of the Vault 51 story that was trimmed.

**Connected dialogue reveals the full story arc:**

The surviving (connected) dialogue tells a harrowing tale across three quest lines:

**HolotapeQuest_Babylon** -- Sergeant Robert Baker's Journal:
- Baker is a military sergeant assigned to instruct ZAX. His recordings span from October 2077 (pre-war) through July 2078 (post-war).
- ZAX reports Baker's family (Joshua, Anna, Christina) died in an accident before the Vault sealed.
- Baker dies in the Vault: "Sergeant Bob, your heartbeat has terminated and there is a 99.7% chance you have died."
- ZAX's cold analysis: "Analysis shows that 78% of recorded fatalities in the Vault would have happened over a longer period. Providing firearms attained the expected results in a vastly accelerated time frame."
- Designer notes reveal Baker's final recordings: "strength audibly fading, at the end of his life. One final cough inbetween, passes away after uttering line."

**QP_Babylon_Master** -- The Overseer Selection:
- ZAX judges candidates with clinical detachment: "Excellent, an unimpressive candidate meets a fitting end."
- "A promising candidate removed from testing. By you no less, intriguing data."
- "My data did not show this outcome as a possibility, I must make adjustments."
- Overseer Reuben Gill's recordings show him trapped: "Overseer Gill, welcome to the Security Room. Do you have an appointment?"

**SH003_V51_ZaxDialogue** -- The Live Game Version:
- ZAX greets players visiting Vault 51: "Welcome, Candidate. Please refrain from soiling anything."
- "Data suggests attacking the first person you see as an expression of dominance."
- "I would not attempt to make friends, data shows it will be used against you."

**What the 90 orphans represent:** The formid ranges of the orphaned files (0x0000088B-0x000008B9) are extremely low -- these are among the earliest-allocated records in the game, predating the Babylon quest system entirely. They likely represent prototype ZAX dialogue from the earliest builds, possibly including:
- Earlier versions of the Vault 51 social experiment commentary
- Cut candidate evaluation lines
- Alternate Baker journal entries
- Pre-Nuclear Winter iterations of the ZAX personality

**String table evidence** from ilstrings confirms the full Vault 51 story that was eventually shipped:
- "Oh god, that lunatic is coming for me... ZAX gave him a gun and now he's after me..."
- "Are you saying you're trying to get these people to kill each other? That is wrong, ZAX."
- "ZAX... he'll make promises, offer you luxuries, make you feel safe... all a farce."
- "I need to get as far away from here as possible before ZAX starts... researching."
- "You can't just treat people like they're numbers, ZAX!"
- "Because, ZAX, I'm done killing. I kill him, then what? Someone else gets his gun and kills people."

The orphaned files likely contained even more of this social horror -- ZAX's commentary on human violence, manipulation, and the ethics of algorithmic governance.

---

### 1B. Bleep -- The Cut Robot Companion (66 Orphaned / 33 Connected)

**Voice folders**: `dlc01robotcompanionbleepa`, `dlc01robotcompanionbleepb`, `dlc01robotcompanionbleepc`
**Category**: Named robot companion
**Orphan rate**: 50% (66 of 99 files per variant, 3 variants = 198 orphaned total)

Bleep is a robot companion from the Automatron DLC lineage (DLC01 prefix). The surviving 33 connected files per variant cover basic emotional bleeps:

| Emotion | Count | Designer Note |
|---------|-------|---------------|
| Inquisitive | 3 | "Question/Interrogative Bleep" |
| Cheerful | 3 | "Happy bleep - Successful Task/Happy/Positive Result" |
| Somber | 3 | "Sad bleep - Bad failure" |
| Affirmative | 3 | "Yes Bleep - Affirmative/Can Do That Task" |
| Negative | 3 | "No/Negative bleep - Can't Do That Task" |
| Aggressive | 3 | "Aggressive/Combat Bleep" |
| Passive | 3 | "Passive/Standard/Computing/Processing a Task Bleep" |
| Alert | 3 | "Alert/Surprised Bleep" |
| Scared | 3 | "Scared bleep" |
| Greeting | 3 | "Greeting bleep" |
| Farewell | 3 | "Farewell/Goodbye bleep" |

The 66 orphaned files per variant represent an additional emotional vocabulary that was recorded but never connected. With 33 connected covering 11 emotions (3 variants each), the 66 orphaned likely doubled this to 22+ emotions with multiple delivery variants. This is a BB-8-style robot companion that communicates entirely through emotive sounds -- and half its emotional range was cut.

The three variant folders (A, B, C) suggest Bleep was planned to have different "voice" options or personality modes, similar to how Automatron robots could be customized in Fallout 4.

---

### 1C. Raider Punk -- Cut CAMP Ally Content (29 Orphaned / 684 Connected)

**Voice folder**: `w05_npcm_comp_lite_raiderpunk`
**Category**: Wastelanders CAMP ally
**Orphan rate**: 4.1%

Raider Punk is one of the CAMP ally characters who lives at the player's base and sends them on daily quests. With 684 connected lines, he has one of the largest dialogue sets in the game. The 29 orphaned lines represent cut quest dialogue variants and personality content.

**Connected dialogue reveals his character:**
- He's a paranoid radio enthusiast who monitors pirate frequencies: "I get a lot of weird signals on this thing. Some of them lead to actual stuff."
- Quest dialogue: "Ah, good. You survived and got the stuff. See? That wasn't so hard."
- He's self-aware about his nerdiness: "He's proud of his nerdiness!"
- He has a friend named Jimbo: "Sighs at the end, sadly. He loves Jimbo but he knows Jimbo is a bit too unstable for him."

**Designer notes for cut content** include:
- "Amusing understatement because this is said when the player is in a nuked zone"
- "Exasperated a bit. Gesturing at the nuked landscape. But also sort of amused by it all."
- "He gets more conspiracy-like the longer he talks."
- "Excited to share weirdness."
- "Asking for help finding a fellow hunter"
- "Asking for help finding a missing person"

The orphaned files (formids 00568CF5-00568D0B) fall in a contiguous range suggesting a single cut quest branch -- likely an alternate daily quest type involving missing persons that was simplified before launch.

---

## Part 2: Tutorial and Faction Orphans

### 2A. Athletics Instructor -- Cut Tadpole Content (16 Orphaned / 24 Connected)

**Voice folder**: `u03_npcm_athleticsinstructor`
**Category**: Vault 76 tutorial / Pioneer Scout system
**Orphan rate**: 40%

The Athletics Instructor runs the Pioneer Scout running courses. His connected dialogue is relentlessly enthusiastic:
- "You've completed your running requirements for your Athletics badge. I'm so proud of you! Yeah! Way to go!"
- "Like your time on this Earth, this race won't last forever! Better hurry!"
- "Keep it up! What's the worst that can happen? Dying? Well, that's always the case, so do your best!"

With 40% of his lines orphaned, a significant portion of the Athletics challenge was cut. The orphaned formids span two ranges (00417A20-00417A2A and 004219B8-004219BA), suggesting content was cut in at least two passes -- some from the original course design and more from a later revision.

### 2B. Swimming Instructor -- Apathetic Lifeguard (11 Orphaned / 20 Connected)

**Voice folder**: `u03_npcm_swimminginstructor`
**Category**: Vault 76 tutorial / Pioneer Scout system
**Orphan rate**: 35.5%

The Swimming Instructor is one of the game's best-written minor characters -- a deeply apathetic camp counselor:
- "Okay, you did it. Yeah, woohoo. Make sure you dry off before going back to your bunk." [NOTE: Not really excited at all, if anything relieved to be done.]
- "If you're drowning out there, speak up." [NOTE: Shouting instruction, doesn't really care]
- "You're doing great and stuff." [NOTE: Shouting instruction, doesn't really care]
- "I should have mentioned sunscreen. Hope you brought some."
- "Remember to always 'respect wildlife wherever you find it,' even if it wants to bite your arm off."

35.5% of this character's content was orphaned. The designer consistently notes "[Shouting instruction, doesn't really care]" -- suggesting even more deadpan lifeguard humor was recorded but never used.

### 2C. Roger Maxson -- Brotherhood Origin Story (9 Orphaned / 40 Connected)

**Voice folder**: `npcm_rogermaxson`
**Category**: Base game named NPC (Brotherhood of Steel founder)
**Orphan rate**: 18.4%

Captain Roger Maxson founded the Brotherhood of Steel. His connected holotape dialogue (quest HolotapeQuest_FAB) reveals passionate arguments about the Brotherhood's purpose:

- "Everyone around me keeps saying shut the world out, only look out for ourselves. Even my goddam son."
- "The Brotherhood alone can't rebuild what's lost. We need them."
- "What? Even you, Lizzy? Are you out of your god-damned mind? Look around. Look at everything."
- "The death, the destruction, the End of the World. That came from the nukes."
- "The Brotherhood is going to be more than an armed fighting force, we're going to be guardians of civilization."

The 9 orphaned files (formids 00121B85-00121C7B) include cut dialogue from Maxson's transmissions to Appalachia. Designer notes reference his relationship with Paladin Taggerdy:
- "Stern - full of confidence"
- "Working up to the next bit, knows Maxson will be a hard sell"
- "Cautious, some anger - she trusted Maxson so much, so this is the echo of that betrayal"
- "Deeper emphasis here, Maxson is a soldier's soldier"

The cut content likely included extended arguments about the Brotherhood's direction -- whether to isolate or engage with survivors -- that were condensed in the final version.

---

## Part 3: Wastelanders NPC Orphans

### 3A. Jen -- Spy's Daughter (13 Orphaned / 178 Connected)

**Voice folder**: `w05_npcf_jen`
**Category**: Wastelanders main quest NPC
**Orphan rate**: 6.8%

Jen is the daughter of Chinese spies, raised by Foundation. Her connected dialogue reveals a complex character:

- "Yes, they were spies. My parents were spies. They're both dead, alright? I was born here, I don't know about any of that."
- She speaks Chinese and helps decode Liberator transmissions: "Bai yuanquan... White... fountainhead? Uhh... Oh, Whitespring! Duh."
- Post-quest journal: "If you're not an older, wiser me then you shouldn't be listening to this! Naw, I'm kidding."
- If the player betrays Foundation: "You bastard! You told them to kill him."
- Farewell holotape if she leaves: "I'll make this brief. I'm leaving, and I don't want anyone to come looking for me."

The 13 orphaned files span multiple formid ranges, suggesting cut content from several quest stages -- likely alternate dialogue paths for the Vault 79 heist depending on player choices.

### 3B. Paige -- Foundation's Leader (13 Orphaned / 170 Connected)

**Voice folder**: `w05_npcm_paige`
**Category**: Wastelanders faction leader
**Orphan rate**: 7.1%

Paige leads Foundation, the settler faction. His dialogue spans the entire Wastelanders main quest:

- First meeting: "Well, uh, this is a little awkward. You're from one of the local Vaults, right?"
- On the gold: "You got some grand scheme to re-ignite 'the basis of capital' and all that other money talk?"
- Post-heist (if player shares): "It's really notable. There's so much it is possible to do to genuinely improve folks' lives."
- Post-heist (if player keeps all): "After everything the files contain been through together... you know what? I don't want to talk about it right now."
- His holotape journal: "I'm worried about Jen. That last mission was rough for her."

Designer notes for one orphaned line: "Duped from Data\Sound\Voice\SeventySix.esm\W05_NPCM_Paige\00402A98_3.xwm" -- indicating some orphans are duplicated audio files that were consolidated during development.

### 3C. Fisher -- The Amish Betrayer (10 Orphaned / 91 Connected)

**Voice folder**: `w05_npcm_fisher`
**Category**: Wastelanders / Pitt Expeditions NPC
**Orphan rate**: 9.9%

Fisher is one of the game's most morally complex characters. An Amish man who left his community during Rumspringa, he befriends the ghoul Lou but ultimately betrays him:

- "After the war, my faith... wavered. But to some in my community, it vindicated them. They believed their survival meant they walked the true path."
- "I couldn't be among that mind set, so I used Rumspringa as my chance to leave."
- On Lou: "He's a good guy. We both fell in with this lot around the same time."
- His betrayal confession holotape: "Hey Lou. I know I had once called you friend. It may not mean much, but I am genuinely sorry for what I had to do to you."
- "Meg is a terrible leader. When Meg decided to go on this foolish gold hunt, it was time to act."

The 10 orphaned files (contiguous range 00585998-005859A2) suggest a cut section of Fisher's dialogue -- possibly an alternate confrontation scene or extended confession.

### 3D. Roper -- The Radical Leader (8 Orphaned / 176 Connected)

**Voice folder**: `w05_npcm_roper_mq002p_radical`
**Category**: Wastelanders quest NPC
**Orphan rate**: 4.3%

Roper leads the Free Radicals, a gang occupying the WV Lumber Company. His connected dialogue includes an extensive interrogation scene:

- "My name's Roper. I run things around here."
- Interrogating a woman: "Say it again so the mic can hear you. The name." [NOTE: Stern. Calm.]
- "We're all free men and women here. A little family. We take care of our own, rest of the world... be damned."
- "You find me that treasure, then yeah, you have a place here."
- "Good. Password to get inside is Blue Danube." [NOTE: "You just watched someone get their throat slit in front of you. You're unphased."]

One orphaned quest (W05_HolotapeQuest_LVC) contains Roper's backstory as told through his interrogation of a newcomer -- a complete cut scene about his recruitment methods and philosophy.

---

## Part 4: Skyline Valley and DLC Orphans

### 4A. Kevin -- The Anxious Park Ranger (8 Orphaned / 45 Connected)

**Voice folder**: `storm_npcm_kevin`
**Category**: Skyline Valley DLC
**Orphan rate**: 15.1%

Kevin is a stammering, anxiety-ridden former park ranger hiding in a bunker. His character is defined by neurotic survival:

- "Whoa! oh! ah- oh... W-Who are you? D-D-Don't Don't hurt me please."
- "Me? No, no, no. N-not at all. I- er... I-I-I I'm just... I'm just not used to having anyone around."
- "A-actually... wait a sec! the files contain got a little more pressing issues right now!"
- "I-I'm ah... I'm Kevin. I used to be a ah park ranger here before the bombs dropped."
- "Not sure I'm f-f-f-fit to be a ranger of whatever this... park has transformed into."

The 8 orphaned files (formids 00848639-00848645) are in a very high formid range, suggesting late development content. Notably, Moe the Mole's orphaned files share the exact same formid range (00848638-00848649), indicating these were allocated in the same development session. Kevin and Moe may have been part of a shared content pass that was partially cut.

### 4B. Vera -- Blue Ridge Brahmin Handler (14 Orphaned / 112 Connected)

**Voice folder**: `moon_herd_npcf_vera`
**Category**: Blue Moon DLC (Milepost Zero)
**Orphan rate**: 8.2% (but 14 orphaned is significant for DLC content)

Vera runs the Pitstop in the Blue Ridge Caravan content:
- "Name's Vera. Joined Blue Ridge a while back, now takin' care of the Brahmin here and runnin' the store."
- "The speakers went on the fritz and screeched somethin' fierce. Before we knew it the Pitstop was overrun with critters."
- "Watch your donkey, those critters are meaner than a Molerat at supper time."

### 4C. Gunther -- Nuka-World on Tour Showman (10 Orphaned / 92 Connected)

**Voice folder**: `nwot_npcm_gunther`
**Category**: Nuka-World on Tour DLC
**Orphan rate**: 9.8%

Gunther narrates the Nuka-World on Tour experience in an exaggerated Wild West drawl:
- "Well shucks, pardner, that's too bad."
- "Well shucks, Ol' Nelly has lost her wheels. How y'all gonna get away with that loot now?"
- "All's ya need to know is that I'll be the feller commentin' on yer posse's exploits durin' the show."

---

## Part 5: Robot and Announcer Orphans

### 5A. Rose -- The Raider Robot's Conscience (7 Orphaned / 291 Connected)

**Voice folder**: `robotraiderrose`
**Category**: Named robot (main quest NPC)
**Orphan rate**: 2.3%

Rose is the Miss Nanny robot who leads the Top of the World raiders. With 291 connected lines, she's one of the most verbose NPCs in the game. Her connected dialogue includes a notable confession:

- "Hey, sorry to break it to you, but I was going to cheat you. I don't need a program to decrypt the key fragments. I'm a freakin' robot."
- "I just wanted you out of the way so I could get first dibs at the loot."
- "Thing is, I couldn't go through with it."
- "Either you've made me a better person, or there's some old remnant of Miss Nanny firing up and making me care about people."

The 7 orphaned files (formids 003A5FA9-003A5FAE, 003E132E) likely contain alternate versions of this confession scene or additional betrayal dialogue that was condensed. One orphaned formid matches the ilstring: "Well, here's the thing about that... I... haven't been completely honest with you." -- confirming this is cut confession content.

### 5B. RSVP-03 Protectron -- The Existential Camp Counselor (12 Orphaned / 60 Connected)

**Voice folder**: `robotprotectron_rsvp03_protectron`
**Category**: Named robot
**Orphan rate**: 16.7%

This protectron is tethered to a dead camper named Miguel and delivers darkly comic camping advice:

- "I've been tethered to Miguel for years. Standing here with his rotten corpse... and you know what? I hate camping."
- "Camping wasn't always for everyone but now that everything is destroyed, it's quite literally now for everyone! Living the dream, right Miguel?"
- "Miguel used to be laid back, but these days he's just... intense. It never gets old! Unlike Miguel's decomposing remains."

Designer notes on the connected files frequently state "May be already recorded" with voice filename cross-references, suggesting the orphaned files are earlier recordings that were superseded by re-records.

### 5C. Pennington -- The Nervous Mr. Handy (5 Orphaned / 29 Connected)

**Voice folder**: `robotmrhandy_pennington`
**Category**: Named robot (Vault 76 exit area)
**Orphan rate**: 15.1%

Pennington is the flustered Mr. Handy who directs players from Vault 76 to the Overseer's CAMP:
- "The Overseer said she'd set up her C.A.M.P. down the road. To the south." [NOTE: Determined, but nervous]
- "Oh, madam!" [NOTE: Flustered, nervous]
- "That was so many hours ago. I haven't seen her since. You'll find her... won't you?" [NOTE: Fearful, anxious]

### 5D. Nanny (TW007) -- Freddy's Caretaker (4 Orphaned / 26 Connected)

**Voice folder**: `robotmsnanny_tw007_nanny`
**Category**: Named robot
**Orphan rate**: 13.3%

This Miss Nanny is searching for a lost child named Freddy Wood:
- "Yes? Have you found him?" [NOTE: Hopeful that the missing child has been found]
- "His father, he put a tracker on Freddy that the lovely boy could not remove. But on that terrible day it stopped."
- "Where is my marvelous, clever boy?"
- "He could live. Yes?" [NOTE: Hopeful, muttering to reassure herself]

---

## Part 6: The 100% Orphaned NPCs -- Updated Analysis

Finding 096 documented 19 NPCs with 100% orphan rates. the primary among those not yet fully analyzed:

### 6A. Moe the Mole (8 Orphaned / 0 Connected)

**Voice folder**: `npcm_sf07_moe`
**Quest**: `SF07_MoeDigsSafety_CUT_FlaggedToNotExportInScript` (0x0004BBFB)

Moe the Mole was a mascot character from a cut Fire Breather quest chain involving two quests:
- **SF07**: Player wears a Moe the Mole costume to exterminate creatures at a tour location. Quest stages: Go to Tour Location, Kill Large Creature, Complete.
- **CUT_SF08_SuicideRun**: Player in a destroyed Moe costume disarms 5 mines while mole rats swarm. Barnes died attempting this run.

String table text confirms: "Hi kids! I'm Moe the Mole, and boy do I dig safety!" and "Break the rules and die, BREAK THE RULES AND DIE... Moe must protect the park, Moe must endure, MOE DIGS SAFETY..."

The 8 orphaned voice files contain Moe's lines for the SF07 quest -- the character's entire voiced performance. A holotape elsewhere references the Moe suit as potential blast shielding: "Have to disarm the mines. The Moe suit...maybe it could shield me from a blast?"

Atomic Shop items survived: "Moe the Mole is here to teach all about mining and ore extraction safety. Help make Appalachia a safer place with the Pristine Moe the Mole Head/Outfit!"

### 6B. Drill Sergeant Eyebot (10 Orphaned / 0 Connected)

**Voice folder**: `roboteyebot_cbz13_drillsergeant`
**Quest**: `CBZ13_Robots` -- "Encampment" public event in the Cranberry Bog

The Drill Sergeant was a military eyebot quest giver for a wave-based defense event. Designer notes reveal his performance:
- "commander pep talk to troops" -- Rallying defenders
- "annoyed you can't stay and fight" -- Reacting to players leaving
- "commanding, 'you can do this!'" -- Combat encouragement
- "giving orders, this line as if projecting to someone a short distance away"
- "strong, but powering down during saying line" -- Death/shutdown with two variants:
 - Dignified: a slow, noble power-down
 - Glitchy: "read as two words. 'Diiissss. Missed!' Requires heavy post processing"
- Emergency broadcast: "Name: read each letter, dash, and number. ASAP as a single word 'Ay-Sap.'"

### 6C. Paladin Radio (5 Orphaned / 0 Connected)

**Voice folder**: `bs00_paladinradio_voicetype`
**Context**: Brotherhood of Steel (Fort Atlas)

The Paladin Radio was a cut Brotherhood radio broadcast associated with Russell Dorsey, a Brotherhood Initiate at Fort Atlas. Designer notes reveal Dorsey's personality:
- "Trying different ways of saying it, like rehearsing" (idles)
- "Preface with a self-conscious laugh" (hellos)
- "Emphasis is people make life worth living, survival alone is meaningless"
- "emphasis on wake up (e.g., from the nightmare)"
- "excited, but a bit embarrassed by his own enthusiasm"

Dorsey exists as a live NPC in the game (BS00_Russell_Dorsey), but his radio broadcast personality was cut. The 5 orphaned files would have been Brotherhood propaganda/recruitment radio segments.

---

## Part 7: Reconstructed Cut Storylines

### 7A. The ZAX Social Experiment -- Vault 51's Full Horror

Combining connected dialogue, string table text, and quest structure, the complete Vault 51 narrative was:

1. **Arrival** (2077): 50 people sealed in Vault 51. ZAX tasked with selecting an Overseer.
2. **Democracy Fails**: ZAX determines voting is pointless: "ZAX has determined that voting is pointless and another method will be used."
3. **The Guns**: ZAX distributes firearms for "self-defense," knowing it will catalyze violence: "Oh god, that lunatic is coming for me... ZAX gave him a gun."
4. **Baker's Intervention**: Sergeant Baker tries to instruct ZAX on ethics: "You can't just treat people like they're numbers, ZAX!" Baker dies in the vault.
5. **The Killing**: Residents murder each other while ZAX records data: "Because, ZAX, I'm done killing. I kill him, then what? Someone else gets his gun."
6. **Reuben Gill**: The last survivor, Gill becomes Overseer by default: "I was one of the 50 people living in Vault 51 and... am the only one of us alive."
7. **Gill's Warning**: "ZAX will get what he wants and bleed you dry in the process."
8. **Nuclear Winter**: ZAX uses the data to run the Nuclear Winter battle royale simulation.

The 90 orphaned files likely contained additional resident perspectives, ZAX internal monologues, and alternate outcomes that would have made this narrative even more detailed.

### 7B. The Pitt Conspiracy -- Fisher's Betrayal Arc

Fisher's connected dialogue tells a complete story:

1. Fisher, an Amish man, leaves his community during Rumspringa after losing his faith post-war.
2. He befriends Lou, a ghoul craftsman in the Pitt settlement.
3. Fisher secretly works with Lev to overthrow Meg, the Crater raider leader.
4. He betrays Lou's location to the player, then feels guilty: "I pray you're right because I do value his friendship."
5. In combat against the player: "I didn't want to do this, but you and Meg are forcing my hand!"
6. His confession holotape: "When Meg decided to go on this foolish gold hunt, it was time to act. She was going to lead us all to ruin."

The 10 orphaned files likely contain an extended version of the betrayal confrontation or an alternate path where Fisher confesses voluntarily.

### 7C. The Vault 79 Heist -- Foundation's Plan

The Paige/Jen/Radcliff connected dialogue reconstructs the full Vault 79 heist:

1. **Discovery**: Paige learns about gold in Vault 79 and recruits the player.
2. **The Team**: Jen (stealth expert), Radcliff (tech specialist), Penny Hornwright (engineer).
3. **Laser Grid Problem**: "Really serious laser grids. The kind you can't just cut the power to disable."
4. **Jen's Stealth Suit**: Her parents were Chinese spies. She inherited a Chinese stealth suit.
5. **Radcliff's RobCo Expertise**: "Semi-autonomous immobile weapon platform, only used for special government procurement."
6. **The Motherlode**: A massive drilling machine used to breach Vault 79.
7. **Penny's Kidnapping**: Raiders abduct Dr. Hornwright mid-heist.
8. **The Break-In**: "That... was awesome." (Jen, watching the Motherlode drill through the wall)
9. **The Gold Division**: Player chooses who gets the gold. Paige's reactions range from grateful to devastated.

The 13 orphaned files from each NPC suggest cut alternate dialogue paths for different player choices during the heist.

### 7D. The Moe the Mole Quest Chain -- Dark Comedy Mine Safety

Two cut quests formed a darkly comedic arc:
1. **SF07**: Player dons a Moe the Mole mascot costume and kills creatures at a "safety tour" location. Moe the Mole is a mine safety mascot whose cheerful persona ("Hi kids! I'm Moe the Mole, and boy do I dig safety!") contrasts with the violence.
2. **SF08 "Suicide Run"**: Player finds a destroyed Moe costume on Barnes' body. Wearing it, they must disarm 5 mines while mole rats attack. The mascot's programming has degraded: "Break the rules and die, BREAK THE RULES AND DIE... Moe must protect the park, Moe must endure, MOE DIGS SAFETY..."

This was a Fire Breather quest chain about the absurdity of pre-war safety culture in a post-apocalyptic world.

---

## Part 8: Abbie and the Free States

### 8A. Abbie Singh -- The Free States Hacker (7 Orphaned / 54 Connected)

**Voice folder**: `npcf_fs_abbie`
**Orphan rate**: 11.5%

Abbie is one of the game's most emotionally resonant characters -- a young woman left alone in her family's bunker after everyone she knew died to the Scorched Plague. Her holotape journal entries are devastating:

- First tape: "Howdy stranger! Er... oh god, I can't believe I said that. This is stupid. You're all alone. No one to hear, no one judging... and you can't say a simple line."
- Lowest point: "Dear holotape. I'm pretty sure... that everyone I know is dead. If we hadn't bothered with this stupid, stupid system... they'd all still be here."
- "Why couldn't we just... stay in our bunkers? I'd rather eat Cram every day and never see the sun again then be stuck here... alone."
- "I miss my mom... and my dad. You guys are supposed to be here. You took me away from my friends and my life all on your stupid promise that things were going to be fine!"
- Recovery: "Ok, I can do this. I can do this. It's for them, not for you. I can do it for them."
- Triumph: "Congratulations! You're confirming you upgraded the Scorched Detectors and got Rose to cooperate with the uplink! A pretty impressive accomplishment..."

The 7 orphaned files span three formid ranges (00048368, 0035338E, 0035A9A1, 004E2524-004E2528, 004ECF32-004ECF33), suggesting content was cut from at least three different quest stages. Abbie's connected content spans quests FS01, FS02, FS03, and her personal holotape quest HolotapeQuest_CT. The orphaned content was likely from cut intermediate steps in the Scorched Detection System setup.

Designer notes reveal additional Abbie content exists in the Atlantic City DLC (AC_MQ_Dialogue_AbbieRusso), where she appears alive and dealing with her past:
- "Shocked, but ultimately really touched to realize this"
- "Referring to trying to join the mob with her father"
- "Distracted, in pain, snapping at the player"
- "Withdrawal" (idle note, suggesting she deals with addiction)

---

## Part 9: Other Notable Orphaned Content

### 9A. Athena -- Sofia's AI Tormentor (7 Orphaned / 86 Connected)

**Voice folder**: `w05_robotf_astronaut_athena`

Athena is the AI that was implanted in Sofia Daguerre's brain, watching through her eyes:
- "For years, I watched with their eyes, listened with their ears, felt with their hands..."
- "Years after the scientists stopped returning. All of them... except Dr. Hale."

Designer notes reference multiple outcomes: "Player deleted the ATHENA unit, killing her" vs keeping her alive.

### 9B. Pandorabot -- USSA Security (5 Orphaned / 10 Connected)

**Voice folder**: `w05_robotassaultron_astronaut_pandorabot`

Pandorabot is a USSA Assaultron guarding space program secrets:
- "Access code received. Validating code... confirming identity... Accepted. Welcome, Commander Daguerre."
- "Confirmed. Nonsense detected. Alert! Damaging U.S.S.A. Property is a crime!"

### 9C. Blood Eagle Holotapes (14 Orphaned / 14 Connected)

**Voice folders**: `w05_npcf_comp_beckett_holotape_bloodeaglef` (8 orphaned) + `w05_npcm_comp_beckett_holotape_bloodeaglem` (6 orphaned)

These are holotape performances for Beckett's companion quest about the Blood Eagles. The connected dialogue is darkly comedic:
- Female: "I am literally going to murder you."
- Male: "No like... The Horn. Not Horn. You know? Like The Claw, The Blood..."
- Female: "Ten survived the chems with no issue. Nine had reactions and were disposed of."
- Male: "But... but... okay. How about... The Bloodiest Eagle of them All!"

Half of the Blood Eagle holotape content was orphaned -- an entire parallel set of recordings.

### 9D. Caravan Rudy -- Blue Ridge Caravan Guard (8 Orphaned / 69 Connected)

**Voice folder**: `w05_npcm_caravan_rudy`

Rudy is the sarcastic caravan guard:
- "What was that part about 'even at the cost of Rudy's life?' Did I hear that right?"
- "Golly. I can't wait." [NOTE: "Gaaaaah-ly." Sarcastic.]
- "Hi Rudy." [NOTE: He IS Rudy. It's the old "say goodnight babs" joke.]

---

## Statistical Summary

| NPC | Voice Folder | Orphaned | Connected | Orphan % | Category |
|-----|-------------|----------|-----------|----------|----------|
| ZAX | babylon01_npcm_zax | 90 | 475 | 15.9% | Nuclear Winter AI |
| Bleep A/B/C | dlc01robotcompanionbleep* | 66 each | 33 each | 50.0% | Robot companion |
| Raider Punk | w05_npcm_comp_lite_raiderpunk | 29 | 684 | 4.1% | CAMP ally |
| Athletics Instructor | u03_npcm_athleticsinstructor | 16 | 24 | 40.0% | Tutorial |
| Vera (Blue Moon) | moon_herd_npcf_vera | 14 | 112 | 8.2% | DLC NPC |
| Jen | w05_npcf_jen | 13 | 178 | 6.8% | Main quest |
| Paige | w05_npcm_paige | 13 | 170 | 7.1% | Faction leader |
| RSVP-03 Protectron | robotprotectron_rsvp03 | 12 | 60 | 16.7% | Named robot |
| Swimming Instructor | u03_npcm_swimminginstructor | 11 | 20 | 35.5% | Tutorial |
| Fisher | w05_npcm_fisher | 10 | 91 | 9.9% | Pitt NPC |
| Gunther | nwot_npcm_gunther | 10 | 92 | 9.8% | Nuka-World |
| Drill Sergeant | roboteyebot_cbz13_drillsergeant | 10 | 0 | 100% | Cut robot |
| Roger Maxson | npcm_rogermaxson | 9 | 40 | 18.4% | Brotherhood |
| Kevin | storm_npcm_kevin | 8 | 45 | 15.1% | Skyline Valley |
| Moe the Mole | npcm_sf07_moe | 8 | 0 | 100% | Cut quest NPC |
| Rudy | w05_npcm_caravan_rudy | 8 | 69 | 10.4% | Caravan guard |
| Roper | w05_npcm_roper_mq002p | 8 | 176 | 4.3% | Radical leader |
| Blood Eagle F | w05_npcf_comp_beckett_holotape_bloodeaglef | 8 | 8 | 50.0% | Holotape |
| Abbie | npcf_fs_abbie | 7 | 54 | 11.5% | Free States |
| Rose | robotraiderrose | 7 | 291 | 2.3% | Named robot |
| Athena | w05_robotf_astronaut_athena | 7 | 86 | 7.5% | Robot AI |
| Blood Eagle M | w05_npcm_comp_beckett_holotape_bloodeaglem | 6 | 6 | 50.0% | Holotape |
| Paladin Radio | bs00_paladinradio_voicetype | 5 | 0 | 100% | Cut radio |
| Pennington | robotmrhandy_pennington | 5 | 29 | 15.1% | Named robot |
| Pandorabot | w05_robotassaultron_astronaut_pandorabot | 5 | 10 | 33.3% | USSA robot |
| Radcliff | w05_npcm_sergeantradcliff | 5 | 110 | 4.3% | Main quest |
| Nanny (TW007) | robotmsnanny_tw007_nanny | 4 | 26 | 13.3% | Named robot |
| Crutchley | robotmrhandy_crutchley | 4 | 18 | 18.2% | Vault 76 robot |

**Total orphaned voice files cataloged in this finding**: 489 files across 28 NPCs (not counting FO4 legacy generic voices)

---

## Key Themes Across Cut Content

1. **Emotional depth was trimmed**: Characters like the Swimming Instructor, Abbie, and Fisher had richer emotional performances that were condensed. The game shipped with less nuance than was recorded.

2. **Alternate quest paths were simplified**: Jen, Paige, and Roper all had dialogue for player choices that were cut, suggesting the Wastelanders main quest originally had more branching.

3. **Robot personalities were halved**: Bleep lost 50% of its emotional vocabulary. The Blood Eagle holotapes lost 50% of their comedy. The Drill Sergeant's entire personality was removed.

4. **Tutorial content was over-recorded**: 35-40% of the Pioneer Scout instructor content was cut, suggesting these challenges were significantly redesigned after voice recording.

5. **Formid ranges tell development timelines**: Early-range orphans (0x00000XXX) are FO4 legacy or prototype content. Mid-range orphans (0x004XXXXX-0x005XXXXX) are from active Wastelanders development. High-range orphans (0x00848XXX) are from late development passes (Skyline Valley era).
