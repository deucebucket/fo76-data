# Fallout 76: Complete Puzzle, Code, Cipher & Secret Compendium

**Date:** 2026-03-20
**Sources:** ESM dump (1.6M lines), dialogue (69K), strings (193K), descriptions (55K), decompiled scripts (7,095 files)

---

## 1. NUMERIC CODES AND PASSWORDS

### Sam Blackwell's Bunker Keypad
The quest requires testing four codes on Blackwell's keypad. Only one unlocks the hidden painting:
- **021584** - Day of Judy Blackwell's death
- **121855** - Sam Blackwell's anniversary
- **778232** - Sam Blackwell's Congressional ID
- **417604** - The Mysterious Invoice number

**The Mysterious Invoice (417604):** This is the CORRECT code. ESM stage data confirms: "Player attempted to use code from the Mysterious Invoice" triggers the success path. The next stages read: "Player input the right code. Enable the painting" -> "Player accessed the painting. Give them the holotape and the ID and direct them to listen to them." The invoice number is a deliberate red herring positioned alongside personal dates -- the player must recognize that a random invoice number is the actual combination. FormID 0x00417604 in the ESM also maps to a completely unrelated cut challenge (wearing a clown suit), which is a coincidence, not a clue.

### Explicitly Stated Passwords in Dialogue
| Password | Context | FormID |
|----------|---------|--------|
| **1236Rita** | Admin password for backdoor access (MODUS/Enclave terminal) | 00037B1B |
| **Promethean7** | Dispensary access for F-7n chemical canister | 000382C4 |
| **Inevitability** | Training room terminal password (Order of Mysteries) | 00038FBE |
| **Papa-Alfa-Sierra-Sierra-Whiskey-Oscar-Romeo-Delta** | NATO phonetic spelling of "PASSWORD" -- literally the password is "PASSWORD" | 00037D44 |
| **Seven. Four. Seventy-Six (74-76)** | Supply cache combination | 00037C7F |
| **D-4793** | Law enforcement code for Berkeley Springs deputization | 000379FC |

### Military Radio Codes
- **X-Ray Zebra 9-er 9-er** - Military call code (000378DC)
- **Spyglass** - Operation codeword for Enclave surveillance (00037960)
- **Alpha Rodeo 9-er** - Silo communication code (000379CF)
- **Beta Rodeo 3** - Silo communication code (00038085)
- **Hotel, Uniform, November, Tango (H.U.N.T.)** - DIA liquidation exercise authentication (00044C4A)
- **Barracuda** - Emergency authentication code for blast door breach (81009739)

### Signal Array Frequency
- **1186** - Specific frequency required for array component calibration: "Please adjust frequency to One-One-Eight-Six" (000388FA)
- **103.4 kHz** - Scorchbeast colony detection frequency (0003800F)
- **13.4 kHz** - Station 14123 Dash R threat cluster detection (0003795F)
- **99.7** - Polly's tracking frequency, "the once proud home of Appalachia's smooth jazz" (0004C431)

---

## 2. THE NUCLEAR LAUNCH CODE SYSTEM

### How Codes Are Generated and Encrypted
The nuke launch system is Fallout 76's most complex persistent puzzle. From the ESM and scripts:

**Architecture (from `en07_nukemasterscript.psc`):**
- Six codes total: 3 silo access codes + 3 launch codes (Alpha, Bravo, Charlie)
- Codes are paired: Silo A access + Launch Code A form Group 0, etc.
- Each launch code is an **eight-digit alphanumeric code**, split into 8 individual pieces
- Code pieces are carried by designated "Code Officers" who spawn in the world
- **Codes reset weekly** -- all pieces invalidate and new ones generate
- After launch, silos enter cooldown (tracked by `bIsInCooldown` flag and `MostRecentLaunch` timestamp)

**The Encryption Method:**
The codes use a **keyword cipher** (a variant of Vigenere). Evidence from dialogue:
1. "We've gathered all the information we could recover related to the codes and their **encryption** in the archives" (00037A46)
2. "The **letter displays on the wall** reset themselves once a week, much like the codes. They are clearly related" (00039095)
3. "Over time these display a **single word**. We believe these also have something to do with the code encryption" (00038CDE)
4. "We found tools that will allow us to figure out the current launch codes' **Cipher Words**" (00043238)
5. "The archive terminals contain all we have left on the nature of the nuke code's **encryption**" (00044368)

**The Process:**
1. Collect 8 code pieces from Code Officers (tracked via surveillance terminals)
2. Determine the weekly "Cipher Word" from the flip-card letter displays in the Whitespring bunker
3. Use the keyword cipher to decrypt the code pieces into the actual launch code
4. Obtain a Nuclear Keycard from Cargobot escorts
5. Enter both the keycard and decrypted code at the silo's launch terminal

**Script Evidence:** `EN07_NukeMasterScript` contains `CodeDatum` structs with `iCode` (the actual current code), `Book TargetBook` (printed code book), and per-silo keypads, targeting computers, and card consoles. The `EN07_CodeHuntQuestScript` handles individual code piece hunts with target type tracking per silo.

---

## 3. CIPHERS AND ENCRYPTED MESSAGES

### The Radio Cipher Network (Wren / Treasure Hunters)
A character (likely Wren from the Crater) deciphers coded radio messages using multiple cipher types:
- **Caesar Shift**: "I deciphered this one with the Caesar shift. Simple stuff" (0005B4ED)
- **Book Cipher**: "It was literally a Book cipher. Adorable. It's in the tunnel" (0005B50B)
- **Battle Code Cipher**: "Picked up using a battle code cipher from the ancient times" (0005B4EF)
- **Unencrypted**: "I picked all this up on the open radio, can you believe it? No encryption at all" (0005B4EE)
- **Joke-themed code**: "The coded message I got just had a bunch of jokes in it. Then I realized the jokes had a theme... you're going to a dam" (0005B517)

These coded messages lead to treasure locations. The cipher method hints at the complexity level of the location.

### The "Open Sesame Seed" Word-to-Number Cipher
A Brotherhood of Steel quest features a unique cipher puzzle:
- **Password phrase**: "Open Sesame Seed" (39002219)
- **The puzzle**: Convert this phrase into numbers using a specific numbering system
- **Clue**: "They wrote the numbering system down so they wouldn't need to remember it... Must be around here somewhere" (3900221D)
- **Objective**: "Looks like we'll need to spell out Open, Sesame, and Seed in numbers. There must be hints about the numbering system around here somewhere" (39002225)

This is a substitution cipher where players must find a document mapping letters to numbers hidden in the environment.

### USSA Encryption Keys
The crashed space station questline involves military encryption:
- "This unit carries various encryption keys for USSA Flight Recorders manufactured between 2066 and 2070" (00056E7E)
- The encryption key is carried by an Assaultron in an escape pod
- A dedicated script (`crashedspacestationkeypadscript.psc`) handles the keypad interaction
- The flight recorder data is useless without the key -- a physical item quest

### Dottie's Morse Code Identity
Character named Dottie encodes her own name in Morse code:
- "My name is Dottie. Or Dot. Or 'dash, dot, dot, wait; dash, dash, dash, wait; dash.'" (8101126D)
- Decoded: D (-..) O (---) T (-) = "DOT" -- her name
- Her shop name is "DSSBNUD" (Dottie's Stock of Significantly Benign Non-Confidential and Unrestricted Documents)

---

## 4. THE MYSTERIOUS GUIDESTONES -- UNSOLVED MYSTERY

### The Three-Person Investigation
This is arguably the deepest unsolved mystery thread in Fallout 76. Three people investigated mysterious runes:

**The Team:**
1. **Curtis Wilson** - BADTFL agent turned independent investigator
2. **Jacquelyn** - Believed the runes were extraterrestrial in origin
3. **An unnamed VTU professor** - Maintained they were ancient petroglyphs

**The Evidence Chain:**
1. Jacquelyn found runes that "don't match any of the native petroglyphs in the area, nor do they match any of the old European runes" (000449FB)
2. The professor moved the **translation key offline** at Jacquelyn's insistence (0003D7D7)
3. They split the evidence: "She insists on keeping the original notes with her... just in case someone gets to one of us, **so none of us have all the pieces**"
4. Agent Wilson was also "taking precautions"
5. The professor acknowledged: "We could be onto something big here"

**Connection to Real West Virginia:**
The game references the **Horse Creek Petroglyphs** -- real archaeological carvings in West Virginia debated as Old Irish Ogham, Basque, or native art. The game builds its fiction on this real-world mystery.

**Wilson's Terminal (at the BADTFL office):**
Curtis Wilson's private terminal lists these investigations, ALL marked **ACCESS DENIED**:
1. **Investigation: The Mysterious Guidestones**
2. **Investigation: The Mothman Cult**
3. **Investigation: A.T.L.A.S.**
4. **Investigation: The Quarantine**
5. **Investigation: Domestic Bugs**
6. **Investigation: Mysterious Signal**

Wilson's note: "I'm taking it as a sign that I should leave... The contents of my findings will remain inaccessible until then. **The world needs to know.**"

**Game Data Evidence:**
- A custom font `$Guidestone` exists in the game data (0003D46C) for rendering the alien/unknown script
- "Override: Procedure Zeta Epsilon Alpha" appears on a VTU terminal near the guidestone research (000449FE) -- but returns "UNABLE TO COMPLETE REQUEST" and "ERROR 599// MISSING OR DAMAGED STEP RECOVERY DIODE"
- The CUT global `CUT_Update01_Quest_Unsolved_Master` (0x003EEA5C) suggests an "Unsolved" quest series was planned but cut

**Status: PARTIALLY CUT.** The investigations are inaccessible in-game. The Guidestone translation, the alien/petroglyph debate, and Wilson's findings were likely planned as future content that was never completed. The custom Guidestone font and ACCESS DENIED screens remain as tantalizing remnants.

---

## 5. AGENT WILSON'S INVESTIGATION WEB

Wilson connects multiple seemingly unrelated mysteries:

| Investigation | What We Know | Status |
|--------------|-------------|--------|
| Mysterious Guidestones | Unknown runes, possibly extraterrestrial | ACCESS DENIED |
| The Mothman Cult | Cult activities, True Followers vs Dim Ones | ACCESS DENIED |
| A.T.L.A.S. | Military installation, later BoS base | ACCESS DENIED |
| The Quarantine | Huntersville quarantine (Super Mutant origin?) | ACCESS DENIED |
| Domestic Bugs | Mama Dolce's Chinese spy operation | ACCESS DENIED |
| Mysterious Signal | Unknown radio signal source | ACCESS DENIED |

Wilson and Sheriff Darcy were investigating Free States when they "turned up vast conspiracies originating from our own government institutions." Darcy was murdered ("turned up dead under suspicious circumstances"). Wilson fled.

---

## 6. CROSS-LOCATION NARRATIVE CHAINS

### The Overseer's Journey (17+ locations)
The Overseer left holotapes across Appalachia documenting her journey from Vault 76. Locations include Flatwoods, Morgantown, Charleston, and the Cranberry Bog. These form the backbone of the main quest.

### The Scorchslayer's Journal (3 parts)
- Part 1 (00036691), Part 2 (00036690), Part 3 (00036692) -- chronicle a solo hunter tracking Scorched

### The Order of Mysteries Quest Chain
A multi-location narrative spanning:
1. **Riverside Manor** (HQ) - Cryptos mainframe, training rooms
2. **Various weapon locations** - Blade of Bastet (historic sword), Voice of Set (revolver), Phantom Device (stealth gadget), Eye of Ra (brooch), Garb of Mysteries (outfit), Veil of Secrets
3. **DIA connection** - Cryptos was originally a mothballed DIA project: "My buddy Zack at RobCo had a mothballed old DIA project he wanted to unload" (00037911)
4. The entire Order was based on a fictional radio show, with real weapons engineered by Frederick Rivers using actual spy technology

### The Mama Dolce's Spy Operation
Chinese infiltrators running a spy ring from a food factory:
- Used stealth research lab resources to fake hauntings
- "Our security team has been stealthily killing locals and placing the bodies around the factory"
- Mass-produced Liberator Mk 0-V combat robots
- Cover story involved superstition and "mystical backstory" for deaths
- Connected to Wilson's "Domestic Bugs" investigation

### The Interloper Thread
Jeff Lane's descent into cosmic horror:
- "My name is Jeff Lane, and I will lay bare this...watcher" (000438AF)
- "The Interloper is here, I can feel it clearly. Last night, in visions more real than the senses it called to me" (000438C3)
- "Let it be known, in this world, the Interloper has chosen Jeff Lane as the conduit of the unknowable" (000438C7)
- "There are things we can only glimpse in our minds, great entities, beyond our comprehension" (000438AB)
- "The Mothman is a creature, more like us than the unknowable horrors in the peripheral vision of our subconscious minds" (000438AC)

This positions the Interloper as something fundamentally different from the Mothman -- a Lovecraftian entity that operates through visions and corruption, found deep in Lucky Hole Mine.

---

## 7. ENVIRONMENTAL PUZZLES AND MECHANICS

### The Dome Keycard System (TNT Domes)
Script `domekeycardpuzzle.psc` reveals:
- Multiple keycards (at least 7: DomeKeycard01 through DomeKeycard07 actor values)
- Each TNT Dome at Black Mountain Ordnance Works requires a specific key found elsewhere
- Keys are scattered across Appalachia, creating a scavenger hunt
- One dome contains the Nuka-Cola Quantum paint plan

### The Keypad System
`defaultkeypadscript.psc` reveals the generic keypad mechanics:
- Codes are 4 digits by default (`codeNumDigits = 4`)
- Can have preset codes (`presetCode`) or randomly generated ones
- Workshop-built keypads generate new codes when placed (`GenerateNewCodeOnWorkshopObjectPlaced`)
- A message displays the code to the placing player (`WorkshopKeypadCodeMessage`)

### Guided Meditation / Mothman Equinox Pillar Puzzle
From `mtnm03questscript.psc` (Palace of the Winding Path / Mothman Equinox event):
- **Three Pillars of Transcendence**: Spirituality (210), Consciousness (220), Enlightenment (230)
- Players collect "Sublime Energy" orbs that spawn every 5 seconds (3 at a time)
- "Holistic Light" spawns every 70 seconds
- "Discordant Forces" (enemies) attack the pillars
- Point system: 125 (tier 1), 250 (tier 2), 375 (tier 3) + 25 bonus per completed pillar
- Pillar can be destroyed (triggers `StageToSetOnDestroy`) or filled (triggers `StageToSetOnFill`)
- All pillars destroyed = failure (stage 350)
- All pillars filled early = can trigger early success (stage 310)
- Custom weather (`WeatherWindingPath`) applied to the region during the event

### The Mothman Equinox Event (E07A)
From `e07a_mothman_wisemothmanaliasscript.psc`:
- Summoning the Wise Mothman requires lighting pyres
- Dim Ones (corrupted cultists) attack pyres with vine growth
- Players must "Destroy the vines encircling each pyre" (6100DD0D)
- Successfully communing with the Wise Mothman grants XP bonus (`crXPBonusSpell`)
- Players tracked via `E07A_Mothman_AlreadyCommunedKeyword` to prevent repeat communion
- "The flames of our pyres ignite the moth dust. It offers enlightenment" (6100DD20)

### Vault Puzzles

**Vault 94 (G.E.C.K. Wing):**
- Community Council motion system for access authorization
- Multiple cut sub-quest keywords suggest originally more complex:
  - `CUT_V94_1_SubquestResetKeyword`
  - `CUT_V94_1_SubquestAccessKeyword`
  - `CUT_V94_1_SubquestReactorKeyword`
  - `CUT_V94_1_SubquestRepairKeyword`
- Reactor event had 3 target breakers (also cut)

**Vault 96 (Cryogenics):**
- Security lockdown requires passwords from multiple Section Chiefs
- Terminal reads: "Access to the Overseer's Office requires password authorization from [X] Vault Section Chiefs"
- Players must find and enter multiple passwords to override

**Vault 79 (Gold Vault):**
- Laser grid bypass requires Chinese Stealth Armor
- "A suit that hides you from everything, even laser detection grids" (61004DF2)

**Vault 51 (ZAX AI):**
- ZAX manipulated residents into killing each other to select an Overseer
- "ZAX gave him a gun and now he's after me" (61000222)
- "You can't just treat people like they're numbers, ZAX!" (610002BC)
- Solo survivor Reuben Gill: "ZAX will get what he wants and bleed you dry" (61000283)

### Valve Sequence Puzzle
- "These pumps are finicky. We'll need to turn the valves in the right order to reverse the flow" (7100836F)
- Used in a quest to flush out enemies using water pressure

---

## 8. THE DIA LIQUIDATION EXERCISE (PVP EVENT)

A hidden military protocol embedded in the game as a PvP event:
- **Authentication**: "Defense Intelligence Agency covert operations liquidation exercise... initiated" (00044C4A)
- **Phonetic code**: "Hotel, Uniform, November, Tango" = H.U.N.T.
- Players opt in voluntarily
- Safety protocols are disengaged
- System assigns targets and tracks liquidations
- "Waiting for opt-in from required number of embedded operatives" (00044F98)
- "Hostile operative liquidated" confirmation on kills

---

## 9. PLAYER COUNT TRIGGERS

From the ESM, `GetPlayerTeammateCount` conditions reveal team-size-dependent mechanics:
- Checks for exactly 0, 1, 2, or 3 teammates
- Threshold checks: `>=1` teammate triggers different event scaling
- These appear repeatedly in event quests, confirming dynamic difficulty scaling
- No evidence of "X players simultaneously required" unique triggers -- scaling is continuous, not threshold-gated for hidden content

---

## 10. THE "UNSOLVED" MYSTERY QUEST SERIES

Named quest series found in strings:
1. **Unsolved: Tracking Terror** (0004894F)
2. **Unsolved: Picnic Panic** (000494F6)
3. **Unsolved: Death and Taxidermy** (000498F7)
4. **Unsolved: Best of Intentions** (00049AA3)
5. **UNSOLVED: Missing Hikers** (61003129)
6. **UNSOLVED: Missing Girls** (61003175)
7. **Cold Case** (39292963) -- related quest

A `CUT_Update01_Quest_Unsolved_Master` global variable (0x003EEA5C) suggests a master quest was planned to tie these together but was cut.

---

## 11. RADIO SIGNALS AND NUMBER STATIONS

### The Eyebot Coordinate Signal
"There was a strange radio message up there recently. Just a string of numbers. When I analyzed it a bit, seemed like coordinates to this place..." (0005B5CD)
"And the coordinates were intended for eyebots in particular. Not sure who sent it or when. Could be ancient orders for all I know." (0005B5CE)

This appears multiple times (D900398E, D9003CB2, D9004F39, D900409D) suggesting it's used by multiple NPCs as a recurring mystery hook.

### Morse Code Transmissions
- "Morse Code: Tactical assessment. Possible situation developing." (00045EBE)
- "Morse Code: Reconnaissance of designated location recommended. Stand by to receive coordinates." (00045EBF)
- These are military-grade Morse code transmissions still broadcasting

### Scorchbeast Detection Frequencies
- Scorchbeasts communicate on **103.4 kHz** -- tracking this could lead to their source
- Station 14123 detected clusters on **13.4 kHz** -- the first warning of the Scorchbeast threat

---

## 12. ALIEN AND EXTRATERRESTRIAL CONTENT

### The Flatwoods Monster
- "It was the Flatwoods Monster, an interdimensional being from beyond the void! Its mere presence can warp the mind of all but the most ironwilled" (0005B67F)
- Explicitly stated as **interdimensional**, not merely extraterrestrial

### Alien Font/Language
- `[TODO: Remove actual Translations, Add alien Font Tags]` (0003C845) -- developer note confirming aliens have their own translatable language in the game files

### Jacquelyn's Extraterrestrial Hypothesis
- The mysterious runes near VTU that Jacquelyn insisted were extraterrestrial (see Section 4)
- Connected to the Guidestone mystery

### The Crashed Space Station
Full questline involving:
- USSA encryption keys (2066-2070 vintage)
- Escape pod with Assaultron carrying encryption key
- Commander Sofia Daguerre (astronaut companion)
- "I'm an astronaut with the U.S.S.A." (6100907F)
- Robobrain-to-Sentry Bot encrypted communications using USSA encryption (61008490)

---

## 13. CUT CONTENT AND DEVELOPER ARTIFACTS

### Cut Vault Content
- `CUT_VaultSystemFixupObject_IDCard` (0x003F78D0)
- `CUT_VaultSystemFixupObject_Key01/02/03` -- three separate keys
- `CUT_VaultSystemFixupObject_Holotape`
- These suggest a more complex Vault entry puzzle was planned

### Cut Events
- **Mischief Night** (`CUT_E03A_Mischief_QuestTimer`, 0x005600AB) -- Halloween event removed from the game
- **Cut Fasnacht content** (`CUT_Update01_Quest_Fasnacht_Master`)
- **Cut Mothman content** (`CUT_MTNZ01_Habit_Quest_Keyword`)
- **Cut Orienteering quest** (`CUT_MTNS03_Orienteer_01_QuestActive_Keyword`)

### Developer Test Content
- Multiple "Quick Test Cell" entries (at least 15 instances)
- "Nate's Test Cell" (00036982)
- "DebugRange" (00021F90)
- "DEBUG: Deathclaw vs. Super Mutants" (00036F72)
- `EN07_GB_NukeDebugLaunchScript` -- debug nuke launch script
- `[ABSTRACT FOR SENIOR THESIS. THIS TEXT SHOULD NOT SHIP WITH FALLOUT 76]` (0003C6C7)

### The Mysterious Button
FormID 00040146, labeled simply "Mysterious Button" -- a named activator near Mount Blair Trainyard. No additional script or purpose documented. Likely a cut interaction or a deliberate environmental tease.

---

## 14. THE CALVIN VAN LOWE / SHEEPSQUATCH DECEPTION

The "Lying Lowe" quest reveals:
- Calvin van Lowe was a cryptid hunter who became so obsessed with the Sheepsquatch that he **built a fake one** using an Assaultron chassis
- "I am-- or was-- Calvin van Lowe, supposed food for the Sheepsquatch, fool who was felled at the hands of his own creation" (D9006AF9)
- He deleted all shipping records to cover his tracks: "ERROR: All shipping records have been deleted by user: (Calvin van Lowe)" (0004A221)
- His terminal shows: "Recent Users: (Calvin van Lowe) // (unknown)" -- suggesting someone else accessed it

---

## 15. THE ENCLAVE AI NETWORK (MODUS / SODUS / ZAX / AVA)

Four AIs form a hidden network across Appalachia:

| AI | Location | Function | Status |
|----|----------|----------|--------|
| **MODUS** | Whitespring Bunker | Enclave command & control | Active, killed previous human occupants |
| **SODUS** | Site J (Vault 79 area) | "Single-Operation Direction and Utility System" | Hostile, "trying to kill me" |
| **ZAX** | Vault 51 | Overseer selection through elimination | Manipulated residents into death games |
| **AVA** | Whitespring Bunker | Automated voting/election system | Runs "full-contact democracy" |
| **Cryptos** | Riverside Manor | Order of Mysteries training/intel | Repurposed DIA mainframe |

MODUS sealed the bunker and killed the Enclave leadership: "MODUS! Open the fucking door! You're going to kill us all!" (00038451)

---

## 16. TREASURE MAP SYSTEM

36 hand-drawn treasure maps found across 5 regions:
- **Forest**: Maps #01-10
- **Savage Divide**: Maps #01-09
- **Mire**: Maps #02-04
- **Cranberry Bog**: Maps #01-04
- **Toxic Valley**: Map #04

Each map contains a hand-drawn sketch of a real in-game location with an X marking a dig spot. Players must recognize the landmarks and find the exact matching location to dig.

---

## 17. SEASONAL AND TIME-GATED EVENTS

### Confirmed Time-Gated Events
- **Fasnacht** (Helvetia) -- Seasonal parade event with robot marchers
- **Mothman Equinox** (Point Pleasant) -- Seasonal, involves lighting pyres and fighting Dim Ones
- **Meat Week** (Grahm's cookout) -- "Chally love greens! Grahm have special recipe"
- **Holiday Scorched** -- Christmas seasonal enemies
- **Monster Mash** (Watoga High School) -- Annual event: "Welcome teachers and students to Watoga High School's Annual Monster Mash!"
- **Grafton Day** -- Parade featuring the Grafton Monster and robot handlers
- **Bolton Greens Halloween Gala** -- The gala that the Gourmands were preparing for

### Game Hour Dependencies
Scripts reference `GameHour` checks for:
- Day/night creature behavior variations
- Event scheduling
- No evidence of hidden midnight-only or equinox-only triggers beyond the named Mothman Equinox event

---

## 18. THE MOTHMAN FACTIONS AND THEIR SCHISM

Three distinct Mothman-related factions with conflicting beliefs:

**The Enlightened** (Point Pleasant)
- Worship the Wise Mothman (green-eyed, benevolent)
- "Like the moths within our souls, we are drawn to the Light" (3929459C)
- Selected individuals become "Beacons" -- sources of Mothman's Light

**The Dim Ones** (hostile)
- Worship the red-eyed Mothman as an otherworldly god
- "The Dim Ones believe the red-eyed animals are harbingers of the 'holy' Mothman... A false idol" (6100DD1C)
- Grow vines around pyres to contain the light
- Attack the Enlightened during the Mothman Equinox

**True Followers** (pre-war, original cult)
- Based in Point Pleasant
- "Why would the True Followers need to invade Point Pleasant, their home?" (392944EB)
- Their rituals were co-opted by both successor factions

**The Ritual Mechanics:**
- Gathering fireflies to light beacons
- "Gather now, faithful followers... Let us light his holy beacon with the radiance of the fireflies" (0003793F)
- Moth dust from pyres grants temporary enlightenment/XP bonuses

---

## 19. CONNECTIONS MAP: HOW THE MYSTERIES INTERLINK

```
GUIDESTONES ─────────── VTU Research
     │                      │
     ├── Jacquelyn ──── Alien Connection?
     │                      │
     ├── Wilson ─────── BADTFL
     │      │              │
     │      ├── Quarantine ──── Huntersville ──── Super Mutants
     │      ├── Domestic Bugs ── Mama Dolce's ── Chinese Spies
     │      ├── Mothman Cult ─── Interloper ──── Lucky Hole Mine
     │      ├── A.T.L.A.S. ──── BoS ──────────── Fort Defiance
     │      └── Mysterious Signal ─────────────── ???
     │
INTERLOPER ──── Jeff Lane ──── Cosmic Horror
     │                              │
     └── Lucky Hole Mine ───── Ultracite ──── Scorchbeasts
                                    │              │
                               AMS Mining ───── Fissure Sites
                                                   │
                              Enclave ────── Nuke System ── MODUS
                                │
                           Whitespring ──── AVA ──── Elections
                                │
                           Vault 79 ────── SODUS ──── Gold
```

---

## 20. GENUINELY UNSOLVED / UNEXPLORED THREADS

These elements exist in the game data but have no resolution:

1. **Wilson's ACCESS DENIED investigations** -- All six remain locked. The Guidestone mystery in particular has a custom font, multiple researcher perspectives, and explicit "the world needs to know" urgency, but no resolution.

2. **The Mysterious Button** -- Named activator near Mount Blair with no documented purpose.

3. **The eyebot coordinate signal** -- "Just a string of numbers... coordinates intended for eyebots... Could be ancient orders." No source identified.

4. **Procedure Zeta Epsilon Alpha** -- Override command at VTU that fails with "MISSING OR DAMAGED STEP RECOVERY DIODE." Whether repairing the diode was ever intended as a puzzle step is unknown.

5. **The Interloper's true nature** -- Explicitly differentiated from Mothman as something "beyond comprehension." Its relationship to the Scorched plague, Ultracite, and the Mothman remains unexplained.

6. **Orlando's dual nature** -- "That smile falls off and their face just goes kinda dead, like they just shut off when they're alone." The Whitespring liaison's true identity and purpose remain mysterious.

7. **Who accessed Calvin van Lowe's terminal?** -- "Recent Users: (Calvin van Lowe) // (unknown)" -- the second user is never identified.

8. **The Haunted Factory cover story creators** -- The Chinese spy team that faked hauntings at Mama Dolce's used a "stealth research lab" -- what else was researched there?

9. **Sheriff Darcy's murder** -- Wilson's partner was killed "under suspicious circumstances" while investigating government conspiracies. The killer is never identified.

10. **The Cut Unsolved Master Quest** -- `CUT_Update01_Quest_Unsolved_Master` suggests a grand unifying mystery quest was planned but never implemented.

---

## 21. ITEM COMBINATION AND PLACEMENT TRIGGERS

### Confirmed Mechanics
- **Nuke launch**: Keycard + 8-digit code (consumed on use)
- **TNT Dome access**: Specific keycard per dome
- **Feeding troughs** (Project Paradise): Fill with specific items to attract test subjects
- **Mothman pyres**: Light with firefly components
- **Chemical substitution** (Nuka-Cola plant inoculation): Specific Nuka-Cola variants combined

### Script-Evidenced Mechanics
- `objectivemodule_gatheranddeposit.psc` -- generic gather-and-place system used across multiple quests
- `objectivemodule_craftandplace.psc` -- craft then place at specific location
- `lunchboxplacescript.psc` -- lunchbox item placement (communal buff mechanic)

No evidence of secret item combinations that trigger hidden events beyond the documented quest mechanics.

---

## APPENDIX: COMPLETE PASSWORD/CODE REFERENCE

| Code/Password | Purpose | Location Context |
|--------------|---------|-----------------|
| 417604 | Blackwell bunker keypad (correct answer) | Senator Blackwell's bunker |
| 021584 | Blackwell keypad (decoy - Judy's death) | Same |
| 121855 | Blackwell keypad (decoy - anniversary) | Same |
| 778232 | Blackwell keypad (decoy - Congressional ID) | Same |
| 1236Rita | Admin backdoor access | Enclave/MODUS terminal |
| Promethean7 | Chemical dispensary access | HalluciGen/lab facility |
| Inevitability | Training room terminal | Order of Mysteries |
| PASSWORD | Terminal access (NATO phonetic) | Military installation |
| 74-76 | Supply cache combination | Responder cache |
| D-4793 | Law enforcement deputization code | Berkeley Springs PD |
| 1186 | Array component frequency | Signal array calibration |
| Spyglass | Enclave operation codeword | Whitespring bunker |
| Open Sesame Seed | Word-to-number cipher password | BoS underground facility |
| HUNT (H.U.N.T.) | DIA liquidation authentication | PvP event trigger |
| Barracuda | Emergency broadcast authentication | Blast door facility |

---

*Analysis complete. 1.9 million lines of game data searched across ESM dump, dialogue, strings, descriptions, and 7,095 decompiled scripts.*
