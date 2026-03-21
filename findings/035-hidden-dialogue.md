# FO76 Hidden Dialogue & Cut Content in String Tables

**Source files analyzed:**
- `seventysix_en.ilstrings` (68,916 spoken dialogue lines)
- `seventysix_en.dlstrings` (20,090 description strings)
- `seventysix_en.strings` (158,134 name/label strings)

---

## 1. Cut Content: Named Systems & Items

### Needle SMG (CUT weapon)
A fully defined cut weapon with its own enchantment system, multiple spell tiers, and an exploding variant. The editor IDs are explicitly prefixed `CUT_`.

| Form ID | Record | Name |
|---------|--------|------|
| `0x71002215` | strings | Needle SMG |
| `0x71002214` | strings | Needle SMG Explode |
| `0x006CCC28` | MGEF | CUT_NeedleSmgEffect |
| `0x006CCC2E` | WEAP | CUT_NeedleSMG |
| `0x006CCC27` | ENCH | CUT_NeedleSMG_Explode |
| `0x006CCC29`-`2D` | SPEL | CUT_NeedleSMG_Spell_0 through _4 |

**Novelty:** Widely known in datamining circles since 2018 but never added. Five distinct spell tiers suggest it had a progressive damage system.

### "Enjoy" Quest (NPE_MQ01_Enjoy) -- Reworked New Player Tutorial
A massive, fully-scripted alternate new player experience set entirely inside Vault 76, featuring VR simulation pods, a rogue AI, and a branching finale. This is the reworked tutorial for the Skyline Valley era.

**Key dialogue (ilstrings):**

| Form ID | Text |
|---------|------|
| `[59002963]` | "I've awakened inside Vault 76 after recovering from an injury, and a mysterious voice has beckoned me to enter the survival training simulation pods nearby. My caretaker, Professor Dayton, is missing." |
| `[5900216A]` | "Amnesia, huh? I'm Professor Rupert Dayton. We're both residents of Vault 76." |
| `[590021A3]` | "Now the AI thinks it's 'rescuing' us by luring us in here and holding us hostage!" |
| `[59002186]` | "We used to be your survival training instructors, but the files contain found a better use for our simulation: keeping you safe and sound!" |
| `[590026C1]` | "Yes. You may go, resident, but Professor Dayton stays." |

**Branching quest structure discovered in ESM dump:**
- `NPE_MQ01_Enjoy_Dayton_Intro_Scene` -- player meets Dayton
- `NPE_MQ01_Enjoy_BuildingTutorial_*` -- CAMP building tutorial chain (place CAMP, build foundation, walls, bed, wallpaper)
- `NPE_MQ01_Enjoy_CombatTutorial_*` -- combat training
- `NPE_MQ01_Enjoy_PowerTutorial_*` -- power/wiring tutorial
- `NPE_MQ01_Enjoy_DaytonDeath_Scene` -- Dayton can die
- `NPE_MQ01_Enjoy_AIDeath_Scene` -- AI can be destroyed
- Scene choices: "Sided with Dayton" vs "Dayton downed" vs "Trigger Dayton death"

**Supporting records:**
- `ZZZNPE_MQ01_Enjoy_VRPod_Activator` (0x0072BC1F) -- VR pod interaction
- `DisrupterScript` -- player builds a "disrupter device" to crash the simulation
- `NPE_MQ01_Enjoy_IsGenericResident_Keyword` -- NPCs within the sim

**Novelty:** This quest system IS live content (added with Skyline Valley update, 2024). The branching death scenarios and VR simulation framing are well documented but the full dialogue tree and all the "debugger" mechanics haven't been widely cataloged.

### Feral Dino (Random Encounter)
A random encounter featuring a feral ghoul wearing a dinosaur mascot costume, tied to the Burning Man (Ohio) region.

| Record | Form ID | Name |
|--------|---------|------|
| QUST | `0x0081ACD0` | zzzBurn_RE_Travel_FeralDino |
| NPC_ | `0x0081ACBE` | Burn_RE_FeralGhoul_DinoMascot |
| OTFT | `0x0081ACBF` | Burn_RE_FeralDino_DinoGhoul |
| SCEN | `0x0081ACD5` | Burn_RE_FeralDino_Movement |
| PACK | `0x0081ACC8` | Burn_RE_FeralDino_MoveToB01 |

The `zzz` prefix on the quest indicates it was disabled/cut at some point but the NPC and outfit records remain. This is a wandering encounter -- a feral ghoul in a dinosaur costume from Dino Peaks Mini Golf.

**Novelty:** The quest being prefixed `zzz` (disabled) while NPC records remain active is interesting. Whether this encounter actually fires in-game or was cut is unclear.

---

## 2. Developer Notes & Placeholder Text

### Dev Notes Left in dlstrings
| Form ID | Text |
|---------|------|
| `[000001CB]` | "Needs to be zeroed out so NPCs don't use this (and t-pose). This is for the player only." |
| `[4100F1D0]` | Same dev note, duplicated |
| `[41011677]` | Same dev note, duplicated |
| `[61024720]`-`[61024724]` | Same dev note, 4 more copies |
| `[61025A11]` | Same dev note |
| `[8100FDCB]` | Same dev note |
| `[6102471E]` | Same dev note |
| `[0003E5FD]` | "Debug weapon to test ExplosionNuka enchantment (only found on paddleball)" |
| `[0003E60B]` | "Debug weapon to test mult+add modifier" |
| `[0003E628]`-`[0003E8F7]` | 18 debug weapon descriptions remain in dlstrings |
| `[39005968]` | "This is just a placeholder for where the tutorial message explaining how to launch expeditions would go." |
| `[39294FF9]` | "(TEMP) This is placeholder. Will be replaced with a tutorial screen listing benefits and downsides of playing as a ghoul." |
| `[59001AE7]` | "This is a PLACEHOLDER message to represent where loadout select should go." |
| `[7100B40A]` | "This is a placeholder to be filled in later." |
| `[6100F269]` | "debug message" |
| `[61003E0F]` | Dev note about Madeleine/Leah: "Do not get involved" |
| `[61018437]` | "DO NOT LOCALIZE (Reference only)" |
| `[71013672]` | "Debug AV used to set the grunt location" |
| `[81000071]` | "Debug RE Scene JN" |
| `[8100286F]` | "Placeholder Fail Message" |
| `[81002870]` | "Placeholder success Message" |
| `[D9002921]` | Dev design note accidentally left in: "From here, Duchess requests the player collect a body for Polly. Sol tells the player to go to local robotics dealer..." |

### Massive Placeholder Block in ilstrings
105 sequential `[PLACEHOLDER]` entries spanning Form IDs `[61005A00]`-`[61005C38]`. These are reserved dialogue slots that were never filled -- likely reserved for a content update that either shipped incomplete or was restructured.

### The "Placeholder" NPC (Vault 63)
A character who is self-aware about being a placeholder, with actual voiced lines:

| Form ID | Text |
|---------|------|
| `[8100D2B1]` | "Placeholder. How do *you* like it?" |
| `[8100D2B9]` | "'Placeholder. Placeholder. Placeholder.' That's you. That's what you sound like." |
| `[8100D2C2]` | "Huh? What do you mean, 'Placeholder'?" |
| `[8100D2C4]` | "Placeholder? I hardly know 'er!" |
| `[8100D2E5]` | "Gyro says you're dumb." |
| `[8100D2DC]` | "[TEMP] Stop it. STOOOOP IIIIIT." |

This is actually a character in Vault 63 (the decorator NPC). These lines are reactions to the player saying nonsensical things, demonstrating that Bethesda wrote dialogue for every possible player response including garbage input.

---

## 3. Interloper, Dunwich, & Lovecraftian Elements

### The Interloper (Deep Lore)
| Form ID | Text |
|---------|------|
| `[000438AF]` | "My name is Jeff Lane, and I will lay bare this...watcher. No matter how deep I must go, I will come to know the true nature of the interloper." |
| `[000438C3]` | "The Interloper is here, I can feel it clearly. Last night, in visions more real than the senses it called to me." |
| `[000438C7]` | "Let it be known, in this world, the Interloper has chosen Jeff Lane as the conduit of the unknowable..." |
| `[8100929E]` | "Interlopers! Guard the ritual chamber! Don't let them take another step!" |

### Dunwich & Blackhall Connection (dlstrings)
| Form ID | Text |
|---------|------|
| `[710081C5]` | "Urgent message for R. Dunwich and C. Blackhall: Nate knows too much. His followers are growing, and his word is convincing. Although most everything they're saying is speculation, a lot of it is based in collected facts. It's a good thing this information didn't get out before the war. The followers could be converted if they're not too dangerous. They could serve our cause well." |

This references both the Dunwich family (Dunwich Borers from FO4, Dunwich Building from FO3) and the Blackhall family (Point Lookout's "The Dark Heart of Blackhall" quest). The text implies a pre-war conspiracy network between these Lovecraftian bloodlines, with a figure named "Nate" threatening to expose them.

### The Wise Mothman vs The Interloper (dlstrings)
| Form ID | Text (excerpt) |
|---------|------|
| dlstrings | "The broken heard the song of the Interloper and turned from the Truth, scorning wisdom as the product of mere mortals in favor of the unknowable." |
| dlstrings | "We who would learn at the chitinous knee of the Wise Mothman...must speak not of the Interloper. There is no fouler deceit than one garbed in truth. Shun its call, for it can bring only darkness." |

**Novelty:** The Dunwich-Blackhall letter (`710081C5`) directly connecting these two franchise-spanning Lovecraftian families is notable. The "Nate" reference is ambiguous -- could be a follower of the occult, or a nod to FO4's protagonist.

---

## 4. Casino System & Atlantic City Content

### Casino Infrastructure (translate_en_utf8.txt)
| Key | Text |
|-----|------|
| `$CASINO_ERROR_CASINO_DISABLED` | "Casino games are currently unavailable." |
| `$CASINO_ERROR_CASINO_NOT_AVAILABLE` | "Casino games are not available in this region." |
| `$CASINO_ERROR_INSUFFICIENT_CAPS` | "You do not have enough caps to place a bet at this casino game." |
| `$CASINO_ERROR_PENDING_BET` | "You must wait to play this game until your previous casino game has resolved." |
| `$XPD_AC01_SubLocationName` | "The Neapolitan Casino" |

### Lombardi Family / Casino Quarter Dialogue
Extensive dialogue about the Lombardi crime family running the Neapolitan Casino and Casino Quarter in Atlantic City. This is live content from the Expeditions: Atlantic City update.

Key lines:
| Form ID | Text |
|---------|------|
| `[6101B51C]` | "The Lombardi Family runs the Neapolitan Casino and have their fingers in every pie here." |
| `[4100A4A8]` | "There's some...ne'er-do-wells hanging around the Casino Quarter, trying to ruff up the Family's patrons." |
| `[71001793]` | "You're gonna regret pissin' off the Family!" |
| `[71002F28]` | "Meet me in front of the Neapolitan when you land. It's the big casino, you can't miss it!" |
| `[71001D50]` | "I see it in my best interest to wait here in the safety of the club while our associates raid the casino." |

### Devil's Blood Drug Lore
| Form ID | Text |
|---------|------|
| `[59001A5F]` | "We weren't supposed to have it. It wasn't meant for us, but for the real high rollers." |
| `[59001A73]` | "...we couldn't do anything more than slump in our chairs and watch as it drifted away." |
| `[59001A75]` | "Addictol won't be enough to cure this hunger. Maybe nothing will." |

---

## 5. Vault-Tec Board of Directors / TV Show Connections

### Hugo Stolz -- Vault-Tec Board Member
The Vault 63 storyline introduces Hugo Stolz, a Vault-Tec board member and Overseer, which resonates with the Fallout TV show's depiction of the Vault-Tec board selecting vault experiments.

| Form ID | Text |
|---------|------|
| `[8100A790]` | "Founder and CEO of Stolz Enterprises, respected member of Vault-Tec's board of directors, and overall international man of mystery." |
| `[810095CD]` | "I shudder to think what would have happened if we didn't manage to secure a place on Vault-Tec's board of directors." |
| `[8100BB55]` | "Well business, of course! My position on the Vault-Tec board required a permanent move as things escalated." |
| `[8100ED3D]` | "Only quit for more money and better security. Opportunity to work with Vault-Tec, and some big-shot from the board of directors at that." |
| `[8100BB6B]` | "Climate control, increased life expectancy, and the deadliest weapons to ward off would-be survivors of the Apocalypse." |

Stolz's weather machine experiment mirrors the TV show's framing of corporate board members selecting their vault experiments for personal gain. His family dynamics (estranged daughter Audrey, deceased wife) add depth.

**Novelty:** While Vault 63 is live content (Skyline Valley), the explicit "board of directors" dialogue provides in-game confirmation of the organizational structure depicted in the TV show. Stolz is the first named board member actually encountered in a game.

---

## 6. Project Vulcan -- Enclave Ultracite Research

An entire hidden Enclave research narrative in the newest content (D9 Form ID range = The Backwoods update):

| Form ID | Text |
|---------|------|
| `[D90095AD]` | "No, this project, codenamed 'Vulcan,' has a different aim. For while others simply use Ultracite, we intend to understand it." |
| `[D90095C5]` | "I can hear the plaudits now. If it is possible to harness this new power, this 'Ultragenesis,' then we really will be the masters of Ultracite." |
| `[D90095C6]` | "The Enclave will be truly unstoppable!" |
| `[D90095D7]` | "Dr. Gaines was working in the lab, shooting soundwaves at crystals and pissing off his mutated test subject." |
| `[D90095D8]` | "Well what happens when you piss off a mutie? It breaks out of its cage and turns you into a human pretzel." |
| `[D90095DC]` | "We have observed a marked increase in paranoia, delusions, and hysteria among the infected." |
| `[D90095E0]` | "I regret nothing. Glory to the Enclave! And a curse on the gutless traitors that doomed Project Vulcan!" |

**Supporting strings:**
- `[4100DDDF]` references "Secretary Eckart" (Thomas Eckart, known Enclave leader in FO76) authorizing Project Vulcan with Epsilon Squad troops
- Research logs numbered 01-05: Goals, Direction, Breakthrough, Ultragenesis, Disaster

**Novelty:** Project Vulcan is Backwoods update content. The "Ultragenesis" concept -- growing Ultracite rather than just mining it -- is a significant lore expansion. The Enclave's attempt to understand Ultracite's growth properties connects to the Scorchbeast plague's origins.

---

## 7. Profanity & Adult Content

### F-bombs in Dialogue (52 instances total)
The game contains 52 uses of "fuck" across all dialogue, mostly in raider and Atlantic City content. Notable examples:

| Form ID | Text |
|---------|------|
| `[000379CB]` | "Fuck you, Charlie, I made it! I'm alive, and I made it out of that God forsaken shit hole of a mall." |
| `[00037F7E]` | "Scott... What did you do. What the fuck is that thing?" |
| `[61017F86]` | "Woah-whoa hey! Fuck you, huh. I don't go to where you work and tell you how to eat a dick!" |
| `[61017F87]` | "Aw, fuck! Heh, you got me. Sorry ma, that's 10 caps for the swear jar. Shit. I mean spit!" |
| `[7100189A]` | "You won't be messing with the Family any time soon!" (clean, but surrounded by F-bombs from Lombardi goons) |
| `[D9002789]` | "What the fuck, Regs? That's Chase you're talking about." |
| `[D9004E0B]` | "I don't like thinkin' about. Seein' 'em chokin on blood and the smell of shit in their pants, fuck I feel like I'm gonna pass out already." |

### Nudity References
Several instances of characters found "buck naked" -- mostly played for comedy or horror:

| Form ID | Text |
|---------|------|
| `[00043BC9]` | "Colton, the data contains you on the roof of your shack, buck naked, yelling at the top of your lungs." |
| `[0005B677]` | "Came across him acting like a rabid dog shivering in the woods naked, couldn't remember a thing..." (Flatwoods Monster encounter) |
| `[7100498E]` | "Then you'll find yourself splayed out naked on the Boardwalk two days later, choking on your own vomit." |
| `[D90016C5]` | "Or was it the time he got you to hand over your clothes and left you naked in the Mire?" |

### Mole Rat Pheromone Line
| Form ID | Text |
|---------|------|
| `[61005005]` | "I intercepted a molerat with human eyes, and it told me about a stash of junk nearby. I'm going to make a little coat in case it returns. It's naked!" |
| `[61004FFB]` | "You need to kill a Mole Rat. Just don't touch its skin, it sends out dangerous pheromones. Sex. Pheromones." |

---

## 8. Unreleased/New Ally: Grandma Junko

A new C.A.M.P. ally discovered in the D9 Form ID range (newest content):

| Form ID | Source | Text |
|---------|--------|------|
| `[D900889B]` | ilstrings | "Oh my, where are my manners? My name is Junko, but please feel free to call me Grandma." |
| `[D900889C]` | ilstrings | "My grandchildren have given me many nicknames over the years." |
| `[D90088A7]` | ilstrings | "Well, I am pretty handy in the kitchen, so I'm sure I can whip you up something if your tummy gets rumble-y." |
| `[D90088B0]` | ilstrings | "Oh my! Please make yourself decent, for Grandma's sake." |
| `[D90088B3]` | ilstrings | "Oh dearie... did you scrape your knee? Let me see if I can find a bandage for you." |
| `[D90088B8]` | ilstrings | "I know you like your soda pop, but be careful not to rot your teeth out." |
| `[D90088B6]` | ilstrings | "Everything is high-tech these days. When I was your age, that robot costume you stepped into would have been made out of cardboard and bits of string." |
| `[610193D6]` | strings | "Grandma Junko" (NPC name) |
| `[610193C0]` | strings | "Grandma Junko stop hunger/thirst" (mechanic label) |
| `[D9008707]` | strings | "Lite Ally: Grandma Junko" |

**Mechanics:** Has a "stop hunger/thirst" function, meaning she cooks for the player. She reacts to the player being naked, injured, irradiated, and in power armor. She's searching for her daughter who hasn't contacted her.

**Novelty:** Listed as a "Lite Ally" which is a newer ally category. The D9 Form IDs and presence in both strings tables suggest this is Backwoods update content, either recently released or incoming.

---

## 9. Ohio / The Backwoods Region

### Ohio as Playable Space
The Backwoods update expanded the map into Ohio. Multiple dialogue lines reference it:

| Form ID | Text |
|---------|------|
| `[61028190]` | "Let's just say I'm currently residing in Burning Springs, across the river in what used to be Ohio." |
| `[610282ED]` | "Remember; these cases are scattered all over Ohio, so you may need to look far and wide for them." |
| `[7100E30B]` | "Ohio used to be such a green place." |
| `[7100F7AE]` | "Abraxodyne Chemical Plant provides jobs and stability for Ohio." |
| `[7101045D]` | "I've seen a few of your kind in Ohio, but never... up close." |
| `[71010725]` | "As far as I can tell, they're scattered all over Ohio." |

### Abraxodyne Chemical (Ohio Faction)
Multiple strings reference "Abraxodyne Chemical" as an Ohio-based corporation with political influence (Prop 52 voting campaigns) and an environmental cleanup angle.

### The Rust King's Raiders
| Form ID | Text |
|---------|------|
| `[71010456]` | "Why, the Rust King's raiders of course. Those haraami are all over Ohio." |

---

## 10. ZZZ-Prefixed (Disabled) Content in Strings

Items and quests marked as disabled with the `zzz` prefix:

| Form ID | Name | Notes |
|---------|------|-------|
| `[6100D4DE]` | zzz | Unknown disabled record |
| `[7100AB20]` | DEPRECATED AC Vendor Quest | Atlantic City vendor quest cut |
| `[7100F121]` | ZZZ Checkpoint Canyon Interior | Cut interior cell |
| `[610273BE]` | ZZZ Kill the cultists standing guard | Cut quest objective |
| `[7100EB1D]` | zzz | Unknown disabled record |
| `[7101203C]` | ZZZ_Burn_Drive-in_Holotape | Cut Ohio holotape |
| `[4100EFF3]` | zzz_Collect a Mini Nuke with the Money Bags Backpack | Cut challenge |
| `[4100F035]` | zzz_Destroy a Protectron with the Money Bags Backpack | Cut challenge |
| `[590032CC]` | ZZZ_Craft a Glowing Bloodpack while wearing a Costume | Cut challenge |
| `[61023E59]`-`[61023E5C]` | zzz_* Money Bags Backpack challenges | Cut challenge set |
| `[39297632]` | ZZZNuclear-Powered Jetpack | Cut item |
| `[6101FBDA]` | Speech Bobblehead - DEPRECATED | Cut collectible |

### Nuclear-Powered Jetpack
`[39297632]` -- "ZZZNuclear-Powered Jetpack" -- A cut jetpack variant. Power Armor jetpacks exist, but a standalone nuclear-powered version was apparently planned and disabled.

---

## 11. Swimming Mechanics (Exist but Limited)

Contrary to typical Fallout mechanics, FO76 has a full swimming test system in Pioneer Scouts:

| Form ID | Text |
|---------|------|
| `[610004D5]` | "Time to prove you can swim... and not just because you want a badge, but because I don't feel like dragging your sorry behinds out of the water." |
| `[610004D3]` | "The test is stupid simple: Put on a swimsuit, go to each buoy and get back here before time runs out." |
| `[610004D1]` | "Listen close this time: swim to each buoy and get back here in time." |

This is live content (Pioneer Scouts), but demonstrates that swimming mechanics are more developed than in previous Fallout titles.

---

## 12. Homer -- Mysterious Alien Invasion Coordinator

An enigmatic AI or entity named "Homer" who coordinates human defense during alien invasions:

| Form ID | Text |
|---------|------|
| `[59000D8F]` | "Hello there. I am Homer. You can think of me as an... interested party." |
| `[59000D91]` | "Defenders of Earth, I am Homer, and I will be your remote support during this invasion." |
| `[59000D95]` | "I am Homer. Typically I would not get involved in public affairs, but... the extraterrestrial is my specialty." |
| `[59001578]` | "Fellow earthlings, I am Homer. Several uplinks I am using to track extraterrestrial movement have gone offline." |

Homer's nature is deliberately ambiguous -- he claims alien expertise, avoids public involvement, and has access to orbital tracking. This is live content from the Invaders from Beyond seasonal event but Homer's true identity remains unexplained in-game.

---

## Summary of Key Findings

| Category | Finding | Novelty Level |
|----------|---------|---------------|
| CUT weapon | Needle SMG with 5 spell tiers + explode variant | Known but unimplemented |
| CUT encounter | Feral Dino mascot ghoul (Ohio) | ZZZ-disabled, unclear if fires |
| CUT jetpack | Nuclear-Powered Jetpack | Previously undocumented as cut |
| CUT bobblehead | Speech Bobblehead | Deprecated |
| CUT quest | AC Vendor Quest (Atlantic City) | Deprecated |
| Developer debris | 18+ debug weapon descriptions ship in dlstrings | Amusing oversight |
| Developer debris | 105 sequential [PLACEHOLDER] dialogue slots | Reserved, never filled |
| Developer debris | Design note for Polly quest shipped in dlstrings | Copy-paste from design doc |
| Lovecraftian | Dunwich-Blackhall conspiracy letter | Cross-franchise connection |
| Lovecraftian | Interloper/Jeff Lane conduit dialogue | Deep vanilla lore |
| TV show parallel | Hugo Stolz as named Vault-Tec board member | First playable board member |
| New content | Project Vulcan / Ultragenesis (Enclave) | Backwoods update lore |
| New ally | Grandma Junko (Lite Ally, feeds player) | Backwoods content |
| Profanity | 52 F-bombs across all dialogue | Mostly raider/AC content |
| Meta humor | Self-aware "Placeholder" NPC in Vault 63 | Intentional, not cut |
