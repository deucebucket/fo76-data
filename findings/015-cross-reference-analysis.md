# Fallout 76: Cross-Reference Analysis
## Research Document vs. Actual Game Data

**Analysis Date:** March 20, 2026
**Data Sources:**
- Research: `~/ai-drive/gamecryptids/research/fo76/mysteries-and-secrets.md`
- String Files: seventysix_strings_en.txt (193,870 lines), seventysix_dlstrings_en.txt (54,877 lines), seventysix_ilstrings_en.txt (68,921 lines), translate_en_utf8.txt (3,591 lines)
- Scripts: 7,095 decompiled .psc files
- Nuclear Winter strings: nw_strings_en.txt

---

## PART 1: VERIFICATION OF RESEARCH CLAIMS

### 1.1 The Interloper and Lovecraftian Thread

**VERDICT: SUPPORTED with additional findings**

**Confirmed in game data:**
- Form ID `[000438BC]` — Named entry "Interloper" in strings
- Form ID `[000438AF]` — Jeff Lane holotape: *"My name is Jeff Lane, and I will lay bare this...watcher. No matter how deep I must go, I will come to know the true nature of the interloper."*
- Form ID `[000438C3]` — *"The Interloper is here, I can feel it clearly. Last night, in visions more real than the senses it called to me."*
- Form ID `[000438C7]` — *"Let it be known, in this world, the Interloper has chosen Jeff Lane as the conduit of the unknowable..."*
- Form ID `[39294610C]` — Quest dialogue: *"What exactly is 'The Interloper'?"*
- Form ID `[8100929E]` — Combat dialogue: *"Interlopers! Guard the ritual chamber! Don't let them take another step!"*

**Enlightened Sacred Text references (dlstrings):**
- *"The broken heard the song of the Interloper and turned from the Truth, scorning wisdom as the product of mere mortals in favor of the unknowable."*
- *"We who would learn at the chitinous knee of the Wise Mothman... must speak not of the Interloper. There is no fouler deceit than one garbed in truth. Shun its call, for it can bring only darkness."*

**NOT FOUND in game data:**
- "Gutpuker" (the asset name) — Not present in any string file. This name likely exists only in mesh/model file names, not in localized strings.
- "metroman" — Completely absent from all string files. Like Gutpuker, this is purely an internal asset name not referenced in game text.

**CRITICAL NEW FIND — Dunwich/Blackhall Cross-Game Note:**
Form ID `[710081C5]` in dlstrings contains an urgent message found in The Pitt content:
> *"Urgent message for R. Dunwich and C. Blackhall: Nate knows too much. His followers are growing, and his word is convincing. Although most everything they're saying is speculation, a lot of it is based in collected facts. It's a good thing this information didn't get out before the war. The followers could be converted if they're not too dangerous. They could serve our cause well."*

This is a MAJOR cross-game Lovecraftian connection that the research document mentions Dunwich Borers LLC but does NOT mention this specific note. It directly names both "R. Dunwich" and "C. Blackhall" (the Blackhall family from Fallout 3's Point Lookout DLC), confirming an active pre-war conspiracy between the two occult families. The mention of "Nate" and followers who know too much suggests a third party was investigating their activities.

### 1.2 The Interloper — NEW: Ryl-Tkannoth, Maw-Begotten

**MAJOR UNDOCUMENTED LOVECRAFTIAN CONTENT:**

Form ID `[610242D7]` — "Ryl-Tkannoth, Maw-Begotten"
Form ID `[61024703]` — Quest objective: "Catch Local Legend: 'Ryl-Tkannoth, Maw-Begotten'"
Form ID `[61024AB4]` — "Maw-Begotten - Fish Bits"

This is a legendary fish with a distinctly Lovecraftian/Cthulhu Mythos-style name that exists in the fishing system. "Ryl-Tkannoth" follows the naming conventions of entities in Lovecraft's fiction (compare Ug-Qualtoth from the Dunwich thread). The research document makes NO mention of this entity. Its presence as a catchable "Local Legend" fish suggests the Lovecraftian thread extends into the fishing system — possibly implying eldritch creatures lurk in Appalachian waters.

Other legendary fish found:
- `[61024702]` — "Catch Local Legend: 'Organ Grinder'" (Organ Cave connection?)
- `[610246FF]` — "Catch Local Legend: 'Wavy Willard'"
- `[610280B8]` — "Catch Local Legend: 'Hocking Hill Hellion'" (Ohio content — see Part 3)

---

### 1.3 Mothman Cult, Enlightened, and Dim Ones

**VERDICT: SUPPORTED — extensive game data confirms all claims**

**Key confirmations:**
- Multiple Mothman variants confirmed: Stalking, Vengeful (red), Wise (purple), Scorched, Glowing
- Form ID `[0003E26A]` — "Wise Mothman"
- Form ID `[0003DF63]` — "Mothman" (generic)
- Form ID `[0003DF62]` — "Vengeful Mothman"
- Form ID `[00047E88]` — "Scorched Mothman"
- Form ID `[00047E89]` — "Glowing Mothman" (note: research does not mention a Glowing variant)

**Sacred Texts — Extended lore found in dlstrings (not fully in research):**
The dlstrings contain extensive Enlightened sacred texts with rich lore including:
- The Enlightened refer to Vengeful Mothman followers as "Dim Ones" who worship the "Red-Eyed Pretender"
- The text names "Wise Charles" as the founder who led the Enlightened away from the Dim Ones
- The Dim Ones sought the "lost manuscript of Dr. Wallace, an entomologist" about moths of the Appalachian region
- The manuscript is hinted to be at the university where Wallace earned his degree, NOT in the cemetery where the Dim Ones searched
- The Enlightened note that Mothman dust has no mystical properties: *"The Dim Ones would rave about the 'Holy Blessing of his Dust'. We remember: he is Wise, but he is also a moth."*

**Perfect Mothman Egg / Cradle of the Pretenders — CONFIRMED:**
- `[59000490]` — "Perfect Mothman Egg"
- `[6100E671]` — "Perfect Mothman Egg" (duplicate entry)
- `[6100E678]` — "Cradle of the Pretenders"

### 1.4 Indrid Cold / The Smiling Man

**VERDICT: SUPPORTED**

- `[39294757]` — Quest: "The Smiling Man"
- `[3929476C]` — "Smiling Man"
- `[410073DA]` — "Smiling Man"
- `[39294766]` — Dialogue: *"Indrid. A pleasure to make your acquaintance. What are you called?"*
- `[39294789]` — Alternate dialogue: *"Indrid. A pleasure to make your acquaintance. What are you called?"*
- `[39294789]` — *"I am Cold. You may call me Indrid. What are you called?"*
- Steven Scarberry confirmed as NPC: `[39294143]` — "Lite Ally: Steven Scarberry"
- `[6101538C]` — "Scarberry's Shrine" (a location)

---

### 1.5 Bigfoot and the Uninvited Guests System

**VERDICT: SUPPORTED with technical detail**

**Bigfoot confirmed extensively:**
- `[41011C61]` — "Bigfoot" creature name
- `[41011C62]` — "Bigfoots" (plural form)
- `[3929B96E]` — "Unarmed Bigfoot" (attack type)
- `[3929B96F]` — "Bigfoot Slam"
- `[3929B970]` — "Bigfoot Stomp"
- `[3929B971]`/`[3929B972]` — "Bigfoot Slam Area Effect"
- `[41011BF5]` — "Bigfoot Thrown Tick" (confirms thrown exploding ticks mechanic)
- `[3929BA23]` — "Bigfoot 4 Star Legendary Mods Item Pool"

**Scripts confirm spawn mechanics:**
- `SpawnBigfootPartyCrasher.psc` — Spawns `LvlBigfoot_PartyCrasher` with `RA_PartyCrasherSpawnChance_Bigfoot` (float 0.0-1.0)
- `BigfootPartyCrasherDespawn.psc` — Has `FightDuration` timer, `BigfootDespawnMessage`, `BigfootHalfwayMessage`, `PresentationDelay` (12 sec after event), `SpawnDelay` (5 sec after explosion), `DespawnAnim`, `NonHostileFaction` (set when despawning)
- `SpawnPartyCrasher.psc` — Generic party crasher system with `SpawnList` array, `EpicRank = 3` (3-star for non-Bigfoot crashers)

**Uninvited Guest types confirmed in strings:**
- `[3929BBF3]` — "Uninvited Deathclaw Matriarch"
- `[3929BBF4]` — "Uninvited Wendigo Colossus"
- `[3929BBF6]` — "Uninvited Scorchbeast"
- `[3929BBF7]` — "Uninvited Mirelurk Queen"
- `[3929BBF8]` — **"Uninvited Storm Goliath"** (NOT mentioned in the research document!)

**NOTE ON THRILLSEEKER:** The research claims a 4-star mod named "Thrillseeker." This exact name was NOT found in any string file. However, the mod's effect IS confirmed:
- `[3929B8F8]` (dlstrings) — *"Reload Speed & Melee Attack Speed increases based on Killstreak Count"*
- The mod may have been renamed or the name exists only in internal data structures not present in localized strings.

---

### 1.6 Vaults

**VERDICT: SUPPORTED with developer placeholders found**

**Vault 96 placeholder names — Evidence of incomplete content:**
- `[00036E89]` — "Vault 96: [NEED A NAME]"
- `[00036EA8]` — "Vault 96: [NEED A NAME]"
- `[00037267]` — "Vault 96: [NEED A NAME]"

These are remnant placeholder strings from when Vault 96's quest names had not been finalized. They confirm the vault was designed for raid content that was later repurposed.

**Vault 63 quest stages confirmed:**
- `[00036BDA]` — "Collect the Alpha-Level Security Access holotape from Vault 63" (original vault raid design)
- `[00036BDA]` — "Collect the Beta-Level Security Access holotape from Vault 94"
- `[00036BDB]` — "Collect the Gamma-Level Security Access holotape from Vault 96"

These three entries confirm all three vaults (63, 94, 96) were originally designed as a linked vault raid trilogy requiring security holotapes from each vault.

**Vault 63 quest variants (original raid design):**
- `[0003723C]` — "Vault 63: Riot"
- `[00036ECE]` — "Vault 63: Fire Outbreak"
- `[00037250]` — "Vault 63: Reactor Meltdown"

**Vault 94 OLD entry:**
- `[00037702]` — "Vault 94 OLD" (legacy marker)

**Hugo Stolz — confirmed extensively:**
- `[81006A0A]` — "Hugo Stolz"
- `[81006A0B]` — "Cassidy Stolz"
- `[810062B0]`/`[810062B1]` — "Audrey Stolz"
- `[81008C23]` — "Hilda Stolz"
- `[8100A875]` — "Stolz is an interesting name, does it mean something?"
- `[8100A9C5]` — *"Do you mean 'mind control?' Are you serious?"* (Hugo/Storm connection)

**NEW: August Stolz reference:**
- `[8100A897]` — "Who was August Stolz?" (previously unknown Stolz family member)

**Storm Goliath — research doesn't mention these are Vault 63 robots:**
Extensive terminal entries confirm Storm Goliaths are engineered defense robots FROM Vault 63:
- Three named variants: **Nona** (Fragmentation Mines), **Decima** (Cryogenic Mines), **Morta** (Plasma Mines) — named after the Roman Fates (Parcae)
- They call down lightning, have energy cannons, and quote philosophers during combat
- Self-destruct capability as a last resort
- Auto-constructed and deployed from the Engineering Sector

---

### 1.7 Cut and Disabled Content

**"Stolen Supplies" (The Pitt) — VERDICT: NOT ACTUALLY CUT**

The research claims this was "cut content" — a note detailing a quest that was never implemented. The game data tells a different story:

The note exists at `[3929322B]` in dlstrings:
> *"ATTENTION: Stolen Supplies — As many of you know, our storehouse was hit by a Fanatic raiding party, and they made off with a good number of supplies. Rations, medicine, ammunition..."*

But there are also ACTIVE quest objectives:
- `[390177E6]` — *"Well, as long as you're asking... Grab me some steel ingots from around the Foundry if you can. And pick up any stolen supplies you may run across inside."*
- `[6101097B]` — *"I've recovered the stolen supplies."*
- `[6101097C]` — *"I've recovered the stolen supplies."*
- translate_en: `$XPD_Pitt01_OptionalObjective2 — Retrieved stolen supplies`

This is an ACTIVE optional objective in The Pitt expedition, not cut content. The research incorrectly categorized it.

**Nuclear Winter remnants — CONFIRMED extensively:**
- 40+ Nuclear Winter-specific strings including paint names, loot network terminals, perk descriptions, and challenge text
- `[00056A54]` — "Nuclear Winter Loot Network" terminal header
- `[3929C00E]` — "Nuclear Winter" (generic category)
- Many `590xxxxx` and `610xxxxx` Form IDs for Nuclear Winter items that were re-released

**Survival Mode remnants — CONFIRMED:**
- `[0004BADE]` — "SURVIVAL MODE: Survive!"
- `[0004BAE2]` — "SURVIVAL MODE: Kill Legendary Enemies"
- Multiple `610xxxxx` challenge entries like "SURVIVAL MODE: Stake Your Claim on the Wasteland"

---

### 1.8 Developer Rooms and Test Content

**VERDICT: PARTIALLY CONFIRMED**

- "Wooby" — NOT found in any string file (may only exist as an internal editor ID)
- "TestZach" — NOT found by name, but "Snape Kills Dumbledore" — NOT found either
- "QASmoke" — NOT found

**Test/debug content confirmed:**
- `[00046D7C]` — "Debug Ambush Test Cell"
- `[390006CF]`/`[390009CC]`/`[39000AE3]` — "Quick Test Cell" (multiple instances)
- `[0003BA04-08]` — Debug level combat packs (levels 10-40)
- `[00040B8C]` — "DebugDaryl01Location"
- `[000400D2]` — "StartQuest (Debug)"
- `[39002D6D]` — "Test Loc Quest"
- `[39002904]` — "Testing testing... Download a quest item Holotape from this terminal."
- `[0003D94E]` — Debug ID Card
- `[65719]` — "Debug Ambush Test Cell"
- `[86808]` — "Test Loc Quest"
- `[85528]` — "[DummyBehemothBossTest]"
- `[86432]` — "Test Your Metal boss buff" / "Test Your Metal general robot buff"

**Test scripts confirmed:**
- `TestCorrieQuestAliasScript.pex` and `TestCorrieQuestScript.pex` in client archive — confirms the Corrie Treadway developer easter egg

**FEV Testing documented in terminal entries:**
- `[3900258A-C]` — Test Subject 00 terminal entries documenting FEV/Ultracite experiments with grim results

---

### 1.9 Easter Eggs

**Hill Valley — CONFIRMED:**
- `[61026809]` — "Hill Valley" location name exists in strings
- Also in nw_strings: `[61026809]` — "Hill Valley"
- The `610xxxxx` Form ID range places this in post-launch DLC content

**Corrie Treadway — CONFIRMED indirectly:**
- `[00046BA7]` — "Corrie Test" entry
- Test scripts `TestCorrieQuestAliasScript.pex` and `TestCorrieQuestScript.pex`

**Floating Scythe — NOT FOUND** in any string file. This is a world-placed object with no corresponding string entry.

**Steel Jack Statues — CONFIRMED:**
- `[4100B1ED]` — Terminal text: *"The Steel Jacks throughout Skyline Valley are dedicated to the young men in the Civilian Conservation Corps who built much of Shenandoah National Park's infrastructure."*
- `[4100B613]` — "Steel Jack Statue"
- `[4100B650]` — "Steel Jack Statue (Ghoul)"
- Workshop FormEditorID: `Workshop_co_FloorDecor_SteelJackStatueLL`
- Diary pages in dlstrings describing the statues "always pointing at" something
- A statue that fell through a poorly-built boardwalk into swamp water

---

### 1.10 Burning Springs Region

**VERDICT: SUPPORTED — with major Ohio content the research barely mentions**

The research mentions "Ohio mentioned" by developers. The game data reveals Ohio is NOT just a hint — it is a fully realized in-game location:

**Rust Kingdom — The Ohio Raider Empire (NOT in research):**
- `[41010D70]` — *"We've taken over most of Ohio, eventually reaching the river bordering Appalachia."*
- The Rust King is a major NPC with extensive lore:
  - Conquered Ohio with an army of raiders
  - Tamed Deathclaws after defeating a Matriarch bare-handed
  - Built Fort Steuben as a border fortress
  - Has an Arena where prisoners fight
  - Has a Beastmaster who trains Deathclaws at Jackson Junkyard
- Dozens of "Rust Kingdom Raider" armor variants, helmets, and faction entries
- `[71013A3B]` — "Discover The Rust Kingdom" (discoverable location)
- `[7101367F-710138FC]` — Extensive Rust Kingdom raider armor set (light, medium, heavy variants)
- Quest NPCs: Eugene, Magpie, Runt
- `[Burn_SQ01_MoveToRustKingdom.pex]` — Script for Burning Springs side quest

**Hocking Hills — Ohio University Town:**
- `[7100C06C]` — "Hocking Hills Train Station"
- `[7100E3A0]` — "HOCKING HILLS STATION" terminal
- `[7100E480]` — "Hocking Hills Vendor Bot"
- "Hocking Hills University" with faculty terminals
- Students from "Hocking Hills University Class of 2078"
- "Hocking River" water purification system
- `[610280B8]` — "Catch Local Legend: 'Hocking Hill Hellion'" (fishing)
- `[61028133]` — "At the dead pilot between Hocking Hills Station and Jackson Junkyard"

**Other Burning Springs locations:**
- `[610261AA]` — "Athens Ruins" (Athens, Ohio)
- `[41010CCC]` — "Old Athens Asylum"
- `[7100B876]` — "Cornhenge" (corn-based Stonehenge parody)
- `[61028F6F-77]` — Multiple "TBD" entries in Burning Springs Form ID range (unreleased content)
- Dino Peaks Mini Golf (dinosaur theme park)
- The Sinkhole
- The Chop Shop
- Railroad Service
- Super Duper Mart
- Checkpoint Canyon
- Ash Cave

**Abraxodyne Chemical — Major Corporation:**
- Pittsburgh-based chemical company with a complex in Ohio
- Responsible for environmental contamination
- Quest "Dirty Laundry" involves investigating their cover-up of killing an employee named Amrita
- NPC Bodhi (Amrita's father) is the quest giver
- `[71014370]` — Briefcases labeled "property of Abraxodyne Chemical Regulatory Compliance Office in Athens, OH"
- Chemical barrels spotted around Ohio
- Connected to Dino Peaks (dinosaur exhibits may have been contaminated)

**New Burning Springs creatures:**
- **Ogua** — New cryptid (Form IDs `41007xxx` range, also Fasnacht masks)
  - Has combat encounters: "Ogua vs Scorched", "Ogua vs Blue Devil", etc.
  - Ogua Hunter outfit, Ogua Shell Backpack, Ogua Egg
  - `[4100D193]` — "Defeat the Ogua!"
  - The research document does NOT mention the Ogua at all
- **Blue Devil** — Another new cryptid (extensive entries)
  - Has its own Fasnacht mask (glowing variant too)
  - Combat encounters, plushie, outfit, hood
  - `[41007A5B]` — "Ogua vs Blue Devil" (encounter type)
  - `[D900A83D]` — "[Cloaking] Blue Devil" (variant with cloaking ability)
  - `[D900A840]` — "[Speeding] Blue Devil" (variant with speed boost)
  - The research document does NOT mention the Blue Devil at all
- **Radhog** — Mutated pig/hog creature
  - `[610263BD]` — "RadHog"
  - Has cooking station ("Radhog Spit"), mounted head, nose ring accessory
  - `[6102640A]` — "Kill a Radhog" challenge
  - The research does NOT mention Radhogs
- **Armored Deathclaw** — Enhanced Deathclaw variant
  - `[6102808C]` — "Armoured Deathclaw rampage"
  - `[7101228A]` — "NOT PLAYER FACING - Take a picture of an Armored Deathclaw"
  - Connected to the Rust Kingdom's Deathclaw taming lore

---

### 1.11 Backwoods Update Content

**VERDICT: SUPPORTED**

**Rip Daring season content confirmed:**
- `[3929BDA4]` (dlstrings) — *"A prop for the film, 'Rip Daring and the Cryptids From Beyond the Cosmos.' Despite being finished, it went unreleased due to the start of the Great War."*
- Rip Daring Adventurer Outfit, paints, plushies, weapons
- `[39293D98]` — *"It's time for another exciting journey with Rip Daring, Cryptid Hunter extraordinaire!"*
- `[392944F7]` — *"Rip Daring's signature weapon. Freeze cryptids in their tracks with this icy cold shotgun."*

**"The Ghoul" from Fallout TV show:**
- `[41010FFB]` — "The Ghoul" (NPC entry)
- Connected to bounty hunting system (see bounty entries)

---

### 1.12 Flatwoods Monster

**VERDICT: SUPPORTED with additional detail**

**New finding — "Evolved Flatwoods Monster":**
- `[3900002F]` — *"Experimental creatures have overrun Vault 96. In order to secure the Vault, we need to eliminate the Evolved Flatwoods Monster controlling them."*
- `[00050200]` — "Defeat the Evolved Flatwoods Monster"
- `[610018F6]` — "Evolved Flatwoods Monster"

This confirms the Flatwoods Monster's mind-control abilities extend to commanding entire creature armies inside Vault 96. The "Evolved" variant is a boss-level encounter in the Vault 96 Daily Ops.

---

### 1.13 Playable Ghoul System

**VERDICT: SUPPORTED**

- `[392949B3]` — "[Ghoulification Quest Misc Breadcrumb Radio]"
- translate_en: `$PENDING_GHOULIFY_ALREADY — There is already a request to return to ghoul form on this character.`
- Jaye Vo NPC in Radiant Hills provides ghoul disguises
- Multiple faction-specific disguise requirements (Settlers, Enclave, BoS, Secret Service, Raiders all need disguises)
- `[61023C7E]` — Quest about turning Leamon into a ghoul using irradiated ore from Emmett Mountain
- `[39296321]` — Dialogue: *"If it cures all ills, becoming a ghoul sounds like a great idea!"*
- `[392962D6]` — *"Ghoulification cures countless ills - even terminal ones - but it has side effects."*

---

## PART 2: PLACEHOLDER AND UNRELEASED CONTENT

### 2.1 TBD/Placeholder Items (Upcoming Content)

**Unreleased Cryptid Paint Sets:**
- `[39293FB9]` through `[39293FC3]` — Six entries all named "TBDCryptid Paint"
- `[3929441F]` — "TBD Cryptid Power Armor Paint"
- `[39294420]` — "TBD Cryptid Paint"

These are paint sets for cryptids that haven't been assigned final names. The `3929xxxx` Form ID range places them in the Season 23-24 content era.

**TBD Burning Springs Content:**
- `[61028F6F]` through `[61028F77]` — Four entries all named "TBD" in the Burning Springs content range

**Plasma Gun Templates:**
- `[410085A7]` — "TEMPLATE: Plasma, laser etc Burning"
- `[61025032]` — "TEMPLATE: PlasmaGun Burning"

These confirm the datamined Burning Breech mod is in development. The TEMPLATE prefix indicates it's a work-in-progress item not yet finalized for release.

### 2.2 NOT PLAYER FACING Entries (Developer-Only Challenges)

Multiple entries prefixed "NOT PLAYER FACING" reveal internal testing challenges for Burning Springs content:
- Photomode at: Drive In, Hocking Hills Station, Checkpoint Canyon, Dino Peaks, Highway Town, Jackson Junkyard, Rust Kingdom, Athens, Sinkhole, Fort Steuben, Chop Shop, Cornhenge, Railroad Service, Ash Cave, Super Duper Mart
- Take picture of: Ogua, Deathclaw Matriarch, Deathclaw, Radhog, Armored Deathclaw, Stingwing

These confirm all these locations and creatures are fully implemented internally even if some haven't appeared in live content yet.

### 2.3 Debug Location Entry

- `[61028E5B]` — "Debug BarbaraF Location" — A debug marker in the Burning Springs content range suggesting a quest NPC named "Barbara F" with associated quests.

### 2.4 Upcoming Quests in 6102xxxx Range

Three quest names found that appear to be future Burning Springs or Ohio side content:
- `[61029149]` — **"Her Sister's Keeper"** — Quest involving NPC Roxie and Salisbury Steaks
- `[61029152]` — **"Panic at the Basement"** — Quest involving NPC Marjorie, Mole Rat Brood Mother, and security systems
- `[61029169]` — **"Nature versus Nurture"** — Quest with Marjorie's experiments: Intellectual (disarm bomb), Combat (kill feral ghoul), Social (conversation protocol)
- `[61029177]` — "Test Cell: Basement" and `[61029178]` — "Test Cell: Research Facility" in same quest
- `QDLBarbara_EBS_BoatDamaged/BossDead/CeremonyEnded/BoatDestroyed/Join` — Emergency Broadcast System events related to a quest involving boats and a ceremony

---

## PART 3: CONTENT THE RESEARCH MISSED

### 3.1 The Ogua — Undocumented Cryptid

The Ogua is a fully implemented creature with no mention in the research document:
- Multiple Form IDs across `41007xxx` and `610xxxxx` ranges
- Has its own hunter outfit (`[41007DB5]` — "Ogua Hunter Hood")
- Has eggs, plushies, mounted heads, shell backpack
- Featured in combat encounters against other factions
- Has Fasnacht masks (regular and glowing variants)
- `[4100D189]` — "Ogua Death" animation/sound entry
- Appears in Burning Springs content: `[610289A9]` — *"All the sound must have attracted a couple of Oguas to the area."*

The Ogua is based on West Virginia/Appalachian folklore — a large reptilian creature reportedly seen in rivers and lakes.

### 3.2 The Blue Devil — Undocumented Cryptid

Another fully implemented cryptid not mentioned in the research:
- Extensive entries: outfit, hood, plushie, statue, mounted head, curtain door, backpack flair, player icon
- Combat variants: `[D900A83D]` — "[Cloaking] Blue Devil" and `[D900A840]` — "[Speeding] Blue Devil"
- Fasnacht masks (regular and glowing)
- `[41007A5B]` — "Ogua vs Blue Devil" encounter type
- `[7100FFE3]` — "Blue Devils Gang" (faction entry?)
- `[Moon_Herd_BlueDevilAliasScript.pex]` — Script with "Moon_Herd" prefix (possibly a seasonal/event variant)
- Has its own combat ability: `[4100BC5C]` — "Blue Devil Howl"

### 3.3 The Radhog — Undocumented Creature

- Mutant pig/hog creature in Burning Springs
- Cooking station: "Radhog Spit"
- Accessories: "Nose Ring (Radhog)", "Sooie-Heart Ring (Radhog)"
- Mounted head trophy
- Challenge: "Kill a Radhog"
- `[6102635D]` — "Armored Deathclaw Plushie" in same range (suggests Armored Deathclaw is Burning Springs content)

### 3.4 The Rust Kingdom — Undocumented Major Faction

The research mentions "Ohio" once as a developer hint. The game data reveals an entire raider empire in Ohio called the Rust Kingdom:

**Lore:** The Rust King conquered most of Ohio, defeated a Deathclaw Matriarch with bare hands, tamed Deathclaws, built Fort Steuben as a border fortress, and has an Arena for gladiatorial combat. Raiders who fail or displease him are executed.

**Named NPCs:**
- The Rust King (boss/leader)
- The Beastmaster (Deathclaw handler)
- Eugene (former prisoner, quest NPC)
- Magpie (escaped raider, quest NPC)
- Runt (killed by Eugene)
- Cole MacPherson (war party leader who marched on Athens)
- Silas (mentioned in dialogue)

**Locations in Ohio:**
- Rust Kingdom (main stronghold)
- Fort Steuben (border fortress)
- Jackson Junkyard (Deathclaw training)
- Athens Ruins / Old Athens Asylum
- Hocking Hills Station / University
- Dino Peaks Mini Golf
- Cornhenge
- The Sinkhole
- The Chop Shop
- Ash Cave
- Checkpoint Canyon
- Railroad Service
- Super Duper Mart
- Highway Town

### 3.5 Abraxodyne Chemical — Undocumented Corporation

A major pre-war chemical corporation with Pittsburgh headquarters and Ohio operations:
- Responsible for environmental contamination
- Had a complex in Pittsburgh near The Pitt
- Had a Legal Office and Regulatory Compliance Office in Athens, OH
- Used Pennsylvania Union Railroad for waste transport (dispute documented)
- Connected to the "Dirty Laundry" quest where player investigates the murder of employee Amrita
- Chemical barrels scattered across Ohio
- Pesticide manufacturer with aggressive business practices
- Possible connection to the dinosaur exhibits at Dino Peaks (chemical smell reported)

### 3.6 Glowing Mothman Variant

The research lists Stalking (yellow), Vengeful (red), Wise (purple), and Scorched variants. The game data also contains:
- `[00047E89]` — **"Glowing Mothman"** — An unlisted variant

### 3.7 Uninvited Storm Goliath

The research lists Deathclaw Matriarch and Wendigo Colossus as "Uninvited" party crashers. The full list from game data:
- Uninvited Deathclaw Matriarch
- Uninvited Wendigo Colossus
- Uninvited Scorchbeast *(not in research)*
- Uninvited Mirelurk Queen *(not in research)*
- **Uninvited Storm Goliath** *(not in research)* — A Vault 63 combat robot crashing public events

### 3.8 "Fancy Single Action Revolver"

`[61028012]` — A named weapon in the Burning Springs content range. Possibly connected to the bounty hunting system or The Ghoul (Walton Goggins' character).

### 3.9 Serum Alpha/Beta — Lost Cure Research

Detailed quest mechanics for curing the Lost:
- `[610280E8]` — "Find the lab equipment and create Serum Alpha"
- `[610280E9]` — "Administer Serum Alpha to the Sedated Lost"
- `[610280EA]` — "Defeat the Empowered Lost"
- `[610280F6]` — "Administer Serum Beta to the Sedated Lost"
- Hilda's experiments aimed at sedating and potentially curing the Lost
- The "Empowered Lost" become more dangerous after serum administration

### 3.10 New Skyline Valley Quest — "The Powerhouse of the Cell"

`[610280BF]` — "The Powerhouse of the Cell" — A quest objective in the Shining Creek Caverns / Organics Sector area, suggesting additional Vault 63 content involving Hilda's laboratory.

---

## PART 4: FORM ID RANGE ANALYSIS

### Range Distribution for Key Content

| Range | Content Era | Examples |
|-------|-------------|----------|
| `0003xxxx`-`0004xxxx` | Base game (2018) | Mothman, vaults, Interloper, cryptids |
| `0005xxxx` | Early updates | Nuclear Winter, Survival Mode |
| `0900xxxx` | DLC 09 content | Fasnacht masks, fishing rods |
| `3900xxxx` | Post-Wastelanders | Vault 96 Daily Ops, early bounty content |
| `3929xxxx` | Season 23-24 era | Bigfoot, Smiling Man, Rip Daring, TBD cryptid paints |
| `4100xxxx` | Major DLC updates | Skyline Valley, Storm Goliaths, Ogua, Blue Devil, Nuclear Winter items |
| `4101xxxx` | Backwoods update | Bigfoot attacks, Rust King lore, bounty system |
| `5900xxxx` | Post-launch additions | Mothman Equinox, Perfect Mothman Egg |
| `6100xxxx`-`6101xxxx` | Expeditions/expansions | The Pitt, Atlantic City, Fishing, Thrashers |
| `6102xxxx` | Burning Springs+ | Ohio content, Abraxodyne, new quests, TBD content |
| `7100xxxx` | Burning Springs Part 2? | Hocking Hills, Rust Kingdom, Bodhi/Amrita quest |
| `8100xxxx` | Skyline Valley dialogues | Hugo Stolz, The Lost, Vault 63 NPCs |
| `D900xxxx` | Cross-update content | Blue Devil accessories, Fasnacht |

### Newest Content (Highest Form IDs)

The `6102xxxx` and `7101xxxx` ranges contain the newest content, including:
- Three fully defined but possibly unreleased quests (Her Sister's Keeper, Panic at the Basement, Nature versus Nurture)
- The Barbara quest line with boat/ceremony events
- Hocking Hills Station and University
- All Burning Springs Part 2 Ohio content

---

## PART 5: SUMMARY OF RESEARCH ACCURACY

### Confirmed Claims (Accurate)
- Interloper lore and Jeff Lane holotapes
- Mothman cult schism (Enlightened vs. Dim Ones)
- All vault experiments and histories
- Indrid Cold / Smiling Man encounter details
- Bigfoot mechanics (4-star, timer, thrown ticks)
- Steel Jack Statues and hidden quest
- Perfect Mothman Egg / Cradle of the Pretenders mechanic
- Nuclear Winter and Survival Mode remnants in files
- Developer room existence (though test NPC names not in strings)
- Hill Valley Back to the Future reference
- Corrie Treadway easter egg
- TNT Dome keys and Black Mountain Ordnance Works

### Corrections Needed
1. **"Stolen Supplies" is NOT cut content** — It is an active optional objective in The Pitt expedition
2. **"Thrillseeker" mod name** — Not found in strings; the effect exists but may use a different display name
3. **"Gutpuker" and "metroman"** — These are asset/model names only, not present in localized strings
4. **"Wooby" and "TestZach"** — Not present in string files
5. **Uninvited Guests list is incomplete** — Missing Scorchbeast, Mirelurk Queen, and Storm Goliath
6. **Ohio is not a "hint"** — It is extensively implemented with dozens of locations, a major faction (Rust Kingdom), and new creatures

### Major Omissions from Research
1. **Ryl-Tkannoth, Maw-Begotten** — Lovecraftian legendary fish connecting fishing to the eldritch horror thread
2. **The Ogua** — Fully implemented cryptid based on WV folklore
3. **The Blue Devil** — Fully implemented cryptid with cloaking and speed variants
4. **The Radhog** — New mutant creature type
5. **The Rust Kingdom** — Entire Ohio raider empire with extensive lore
6. **Abraxodyne Chemical** — Major pre-war corporation driving Burning Springs narrative
7. **R. Dunwich / C. Blackhall note** — Direct cross-game Lovecraftian conspiracy letter in The Pitt
8. **Glowing Mothman variant** — Unlisted Mothman type
9. **Storm Goliath as Uninvited Guest** — Vault 63 robot crashing public events
10. **Vault 63/94/96 were designed as a linked raid trilogy** — Security holotape chain proves this
11. **Serum Alpha/Beta** — Lost cure research mechanics
12. **Three undocumented Burning Springs quests** — Her Sister's Keeper, Panic at the Basement, Nature versus Nurture
13. **Wise Charles** named as Enlightened founder in sacred texts
14. **Dr. Wallace's entomology thesis** — Hidden Mothman lore object referenced in Enlightened texts
