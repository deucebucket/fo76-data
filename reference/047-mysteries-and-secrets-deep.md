# Fallout 76: Deep Mysteries, Secrets, and Hidden Encounters

## Data Sources Analyzed
- 7,095 decompiled Papyrus scripts (791 RE_ random encounter scripts)
- 69,000+ dialogue lines (seventysix_ilstrings_en.txt)
- 158,000+ name/string entries (seventysix_strings_en.txt)
- Full ESM dump (full_esm_dump.txt)
- Community sources (Fandom wiki, GameRant, Gamepur, Steam forums)

---

## 1. THE SMILING MAN (Indrid Cold)

### What He Is
A rare random encounter NPC introduced in the Mutation Invasion update. His real name is **Indrid Cold**, drawn from real West Virginia cryptid lore. In 1966, a WV resident named Woodrow Derenberger reported encountering a man on the road whose unsettling smile never faded -- a figure historically linked to the Mothman phenomenon.

### ESM Records
- **NPC record**: `NPC_: 0x0068EB57 RE_Scene_Cold_SmilingMan`
- **Quest**: `QUST: 0x0068EB2C RE_Scene_Cold` with 30+ dialogue INFO records
- **Voice type**: `VTYP: 0x0068EB59 RE_Scene_Cold_SmilingManVoiceType`
- **Outfit**: `OTFT: 0x0068EB58 RE_Scene_Cold_SmilingManOutfit`
- **Scene**: `QUST:SCEN: 0x0068EB5A RE_Scene_Cold_Scene01` -- a complex branching scene with 16 scene element pairs
- **String IDs**: `[39294757] "The Smiling Man"` (quest name), `[3929476C] "Smiling Man"` (NPC name), `[410073DA] "Smiling Man"` (display name)

### Script Analysis: `qf_re_scene_cold_0068eb2c.psc`
```
Alias_MysteriousMan -- his internal alias name
Alias_TRIGGER -- proximity trigger to start the encounter
pExplosion -- explosion property for his vanishing act
```
When attacked, he vanishes in a **puff of black smoke via an explosion effect** -- the same mechanic used by the Mothman's disappearance idle (`Mothman_Disappear`). This is a deliberate design parallel linking the Smiling Man to the Mothman.

### Full Dialogue (All Lines Confirmed in Data)
| Form ID | Line |
|---------|------|
| `39294787` | "Indrid. A pleasure to make your acquaintance. What are you called?" |
| `39294789` | "I am Cold. You may call me Indrid. What are you called?" |
| `3929478B` | "Of course it is. The pleasure is mine. So nice to see a smiling face." |
| `39294792` | "Do not be afraid. I do hope I have found you well." |
| `39294793` | "No gentle lamb I presume. A beast in sheep's clothing perhaps?" |
| `39294794` | "Seeking a seeker who cannot be found. Or perhaps it is I that am lost." |
| `39294795` | "I have been away a long time. It appears that much has changed during my absence. I have such sights to see." |
| `39294796` | "Perhaps you can recommend a local peculiarity?" |
| `39294797` | "Salutations!" |
| `39294798` | "Smile, and the whole world smiles with you." |
| `39294799` | "I've heard the moon can be belewe and I trust that to be true." |
| `3929479A` | "Better the devil you know than the devil you don't. At least, not yet." |
| `3929479B` | **"Ever dance with the devil under a blue moon?"** (Batman/Joker reference) |
| `3929479C` | "I really must be on my way. As must you." |
| `3929479D` | "An enlightened idea. I shall do just that." |
| `3929479F` | **"Yesterday upon the stair, I met a man who wasn't there. He wasn't there again today. Oh, how I wish he'd go away."** (Hughes Mearns poem "Antigonish") |
| `3929478A` | "Not from you. For you. I want only happiness for you." |
| `3929478C` | "I get the impression it will keep more than one eye out for me." |
| `3929478D` | "Am I? I am in no way special or spectacular." |
| `3929478E` | "Alas, some friendships are not meant to be. Yet stranger things have happened." |
| `3929478F` | "The devil lies. In the details, or so I have heard." |
| `39294788` | "Grafton has monsters now, does it? I shall keep my head down." |

### NPC Gossip About the Smiling Man
Other NPCs comment on him with suspicion:
- `[39002CB0]` "Now there's an odd duck. Sketchy, if you ask me. Never trust anybody that smiles that much."
- `[39002D3B]` "All smiles and fake chumminess. It's like...the smile doesn't reach their eyes, you know? Just a put-on."
- `[39294680]` "A very friendly man. While his personality was cold, he could not shake his smile."

### Spawn Chance
2% at random encounter locations. The encounter is classified as a **Scene** type random encounter under the Season 12/Mutation Invasion content system with global `Season12_Content_RE_Scene` (`0x006A168E`).

### Cultural References in His Dialogue
1. **"Yesterday upon the stair"** -- William Hughes Mearns' poem "Antigonish" (1899), about a man who wasn't there, perfectly fitting the cryptid theme
2. **"Ever dance with the devil under a blue moon?"** -- Jack Nicholson's Joker in Batman (1989)
3. **"I have such sights to see"** -- Echo of Pinhead from Hellraiser: "We have such sights to show you"
4. **The Antigonish poem** is itself about Point Pleasant-adjacent paranormal folklore

---

## 2. THE STRANGE WOMAN (Lucky Hole Mine Terminal Entry)

### What She Actually Is
**Not an NPC** -- she is a terminal entry at Lucky Hole Mining Co. The string `[0003D838] Strange Woman` is a menu item on terminal `0x0031BA8F` (`LC037_Boss_TerminalDesk`).

### The Terminal Entry (Reconstructed)
The "Strange Woman" entry sits alongside "Closing Up" and "Break In" on the mine foreman's personal message terminal:

**"Strange Woman"** entry: An old woman kept appearing at the mine, watching the foreman. She came with friends. They asked about the mine. They wanted to see "the depths." They wanted the foreman to show them.

> *"God help me. I ran."*

**"Break In"** entry: The locks they put up were smashed open.

> *"Look, we don't want it. The mine. It's yours now. Just... stay down there, all right? Don't bother us, we won't bother you. Deal?"*

### Connection to the Interloper
Lucky Hole Mine is the primary location of the **Interloper** -- the Lovecraftian entity worshipped by a pre-war cult. The "Strange Woman" and her friends were early cultists seeking access to the deep mine where the Interloper resides. This terminal is the origin story of how the cult took over Lucky Hole Mine.

---

## 3. THE INTERLOPER

### Lore Records
- `[000438BC]` Name: "Interloper"
- `[3929460C]` Topic: "What exactly is 'The Interloper'?"
- `[000438AF]` "My name is Jeff Lane, and I will lay bare this...watcher. No matter how deep I must go, I will come to know the true nature of the interloper."
- `[000438C3]` "The Interloper is here, I can feel it clearly. Last night, in visions more real than the senses it called to me."
- `[000438C7]` "Let it be known, in this world, the Interloper has chosen Jeff Lane as the conduit of the unknowable..."

### In-Game Behavior
No dedicated scripts were found in the decompiled scripts for the Interloper itself. It functions as a **static world object** deep in Lucky Hole Mine -- a massive, non-interactive eldritch horror. Its "interactions" are environmental: players who reach the deepest chamber see the Interloper's form and can collect the Ritual Bindings and Ritual Mask from the cultist remains around it.

The Interloper has no triggered events, no activation scripts, and no dynamic behavior. It is pure environmental horror -- which arguably makes it more unsettling.

---

## 4. CRYPTID ENCOUNTER SCRIPTS

### Mothman Stalking Behavior
**`mothmanactorscript.psc`** -- Core Mothman behavior:
```
Idle Property Mothman_Blessing -- plays when communed with (Wise variant)
Idle Property Mothman_Disappear -- vanishing animation
ActorValue Property AbleToCommune -- gates communion ability
Spell Property crXPBonusSpell -- the XP bonus reward
```
On activation by a player, plays the `Mothman_Blessing` idle. Has a `disappear` state that triggers the vanishing idle animation.

### Flatwoods Monster
**`flatwoodsmonsterracescript.psc`** -- Teleportation system:
```
String animEventTeleportVFX = "FlatwoodsmonsterMist" -- visual effect name
Spell Property TeleportOutSpell -- spell cast when teleporting
```
The Flatwoods Monster teleports using a mist VFX and a dedicated teleport spell.

**`flatwoodsmonsterwatcherscript.psc`** -- Stalking behavior:
```
Float Property RangeToDisappear -- disappears when player gets too close
Idle Property DisappearIdle -- the vanishing animation
Sound Property DisappearSound -- audio cue
```
The Flatwoods Monster has a **watcher state** where it observes the player from a distance. If the player closes within `RangeToDisappear`, it plays a disappear animation with sound effect and vanishes. This is the "stalking from the treeline" behavior players report.

**`flatwoodsbossscript.psc`** -- Boss version (Tales from the Stars):
```
TimeBetweenInvulnerableMessages -- warns players attacking during invulnerable phase
FlatwoodsMonsterDisappear -- teleports out when quest ends
```

**`flatwoodsclonesscript.psc`** -- The Flatwoods Monster creates **clones** of itself:
```
Int NumClonesAlive -- tracks living clones
Int Property FlatwoodsVulnerableState -- boss becomes vulnerable when clones die
```
The boss Flatwoods Monster spawns clones that must be killed to make it vulnerable.

### Wendigo
No mimicry-specific scripts found. The Wendigo's "mimicry" behavior (sounding like humans calling for help) appears to be handled purely through audio assets, not scripted behavior. Relevant lore:
- `[0005B65A]` "If I'm not mistaken what I saw was a Wendigo. Former humans that feast on the flesh of their fellow man. Quick as lighting, and twice as erratic."
- `[6101A39F]` "Flesh eating freaks with an insatiable appetite for flesh, folklore says the Wendigo are former criminals possessed by ravenous spirits."

### Cryptid Story Random Encounters
**`w05_re_cryptidstories_master.psc`** -- Master cryptid random encounter controller:
```
Int[] CryptidList
Float SpawnCryptidChance
Int Property ChosenCryptid -- which cryptid spawns
Int Property ShouldSpawn -- whether cryptid appears
ActorValue Property FlatwoodsAVRef
ActorValue Property SnallygasterAVRef
ActorValue Property WendigoAVRef
ActorValue Property SheepsquatchAVRef
```
This script manages the random encounter where NPCs tell stories about cryptids. It randomly selects which cryptid type (Flatwoods Monster, Snallygaster, Wendigo, or Sheepsquatch) appears and whether the cryptid actually spawns during the story.

---

## 5. BIGFOOT -- CONFIRMED NEW CRYPTID

### Evidence from ESM Data
Bigfoot is **fully implemented** as a creature in the game data, not just teased:

- **Race**: `RACE: 0x00868BBC BigfootRace`
- **Faction**: `FACT: 0x00868BAF BigfootFaction`
- **Actor Type**: `KYWD: 0x00868BB0 ActorTypeBigfoot`
- **Skin**: `ARMO: 0x00868BA9 SkinBigfoot`
- **Combat Music**: `KYWD: 0x008AADC9 AudioMusicCombatType_Bigfoot`
- **Spawn Location**: `LCRT: 0x008AEBA2 RA_BigfootSpawnLocRefType`

### Abilities
| Record | Name |
|--------|------|
| `SPEL: 0x00868BBD` | crBigfootStomp |
| `SPEL: 0x00868BBF` | crBigfootSlam |
| `SPEL: 0x00868BBE` | AbRaceBigfoot |
| `MGEF: 0x00868BB3` | crBigfootStompAreaEffect |
| `MGEF: 0x00868BB4` | crBigfootSlamAreaEffect |

### Attacks (from strings)
- `[3929B96F]` "Bigfoot Slam"
- `[3929B970]` "Bigfoot Stomp"
- `[3929B971]` "Bigfoot Slam Area Effect"
- `[41011C61]` "Bigfoot" (NPC name)
- `[41011BF5]` "Bigfoot Thrown Tick" -- **throws ticks at players**

### Spawn System -- Party Crasher Mechanic
**`spawnbigfootpartycrasher.psc`**:
```
ActorBase Property LvlBigfoot_PartyCrasher -- leveled Bigfoot actor
GlobalVariable Property RA_PartyCrasherSpawnChance_Bigfoot -- spawn chance percentage
Sound Property MUSPartyCrashersBigfoot_01Start -- dramatic music on spawn
Message Property PartyCrasherSpawnMessage_Bigfoot -- on-screen alert
```
Bigfoot spawns as a **Party Crasher** during public events, with a configurable spawn chance.

**`bigfootpartycrasherdespawn.psc`** -- Timed fight with dramatic entrance/exit:
```
FightDuration -- time limit for the fight (minimum 60 seconds)
RA_BigfootIntroExplosion -- explosion to mask his entrance
NPCBigfootIntroRoar -- entrance roar sound
NPCBigfootOutroRoar -- exit roar sound
DespawnExplosion -- explosion to mask despawn
BigfootHalfwayMessage -- "halfway" warning message
BigfootDespawnMessage -- "retreating soon" warning
PresentationDelay = 12 -- 12-second delay after event ends before intro explosion
SpawnDelay = 5 -- 5 seconds between explosion and Bigfoot appearing
```

Bigfoot appears **after a public event ends**, waits 12 seconds, triggers an explosion, then 5 seconds later materializes with a roar. He fights for a set duration, gives a halfway warning, then roars and disappears in another explosion. He becomes **non-hostile** (joins a NonHostileFaction) during his despawn animation.

### Rewards
- `[3929BA22]` "Bigfoot Weapon Rewards" -- dedicated weapon reward pool
- `[3929BA23]` "Bigfoot 4 Star Legendary Mods Item Pool" -- drops **4-star legendary items**
- `[3929BB79]` "Bigfoot's" -- possessive camp title prefix
- `[3929BB86]` "'Bigfoot's' C.A.M.P. Title Prefix"
- Bigfoot Beer Stein Display, Bigfoot Wanted Poster, Fasnacht Bigfoot Mask

### Season 24 Scoreboard Tie-In
Multiple SCORE_S24 entries confirm Bigfoot is the Season 24 headline content:
- `SCORE_S24_ENTM_PlayerIcon_SmilingManPatch` (Season 24 also includes the Smiling Man)
- Bigfoot wallpaper, player titles, beer stein display

---

## 6. HIDDEN ROOMS AND SECRET DOORS

### All Secret Door Types Found in Strings
| Form ID | Secret Door Type |
|---------|-----------------|
| `[0002AB8F]` | hidden door (generic) |
| `[3929B636]` | **Abandoned Estate Secret Door** |
| `[410006E0]` | Nuka-Cola Secret Door |
| `[41001338]` | Brick Wall Secret Door (3 variants) |
| `[41001859]` | Top Secret Door (3 variants) |
| `[41003328]` | Elevator Secret Door |
| `[410033AB]` | Wavy Willard Stone Secret Door |
| `[41003534]` | Portrait Secret Door |
| `[4100A715]` | Phonebooth Secret Door |
| `[41000B47]` | Fireplace Secret Door |
| `[61009F0A]` | Fireplace Secret Door (CAMP variant) |
| `[6100A624]` | Secret Door Brick Wall (CAMP variant) |
| `[61011B92]` | Pittsburgh Union Steel Furnace Secret Door |

### The Abandoned Estate Secret Door
From ESM data, this is a **CAMP prefab item**, not a world location:
- `ACTI: 0x0085B2BE ATX_Structure_AbandonedEstate` -- the structure itself
- `DOOR: 0x0085B2C3 ATX_Barrier_AbandonedEstateBarrier_SecretDoor_256` -- the secret door
- Model: `atx_abandonedestate_secretdoor_256.nif`
- Associated walls: `ATX_Barrier_AbandonedEstateBarrier_Wall_256`, Column, Wall_128

This is an Atomic Shop CAMP building with a built-in secret door. Players buy the Abandoned Estate prefab and it includes a hidden door mechanic within the structure.

### Weapon-Activated Hidden Passages
`[39297D7E]` "(Optional) Open hidden passages using the weapon"
Context from surrounding strings:
- `[39297D7C]` "(Hint) 'Open Sesame Seed'"
- `[39297D7D]` "(Hint) Look for a number conversation chart"
- `[39002219]` "'Open Sesame Seed,' eh? I've always been more of an everything bagel person."
- `[3900221F]` "So I guess we'll need to find a way to change 'Open Sesame Seed' into a series of numbers."

This is from a **Brotherhood of Steel quest** involving a cipher puzzle. Players must convert the phrase "Open Sesame Seed" to numbers using a conversion chart, and can optionally use a weapon to open hidden passages within the quest location.

---

## 7. THE WISE MOTHMAN -- MECHANICAL BREAKDOWN

### Communion Mechanic
From `ffz10_light_mothmanactorscript.psc` and `mothmanactorscript.psc`:

**Requirements to commune:**
1. Player must be in `FFZ10_Light_WiseMothmanFaction` OR have `FFZ10_Light_CanCommuneKeyword`
2. Player must NOT have `FFZ10_Light_AlreadyCommunedKeyword` (one commune per event)

**What happens:**
1. Player activates the Wise Mothman
2. Script checks faction membership and keyword status
3. If valid: `Self.PlayIdle(Mothman_Blessing)` -- plays the blessing animation
4. Server applies `crXPBonusSpell` -- an **XP bonus buff**
5. Player receives `FFZ10_Light_AlreadyCommunedKeyword` (preventing re-communion)
6. `FFZ10_Light_BlessingMessage` displays on screen

**The reward is confirmed to be `crXPBonusSpell`** -- an XP bonus spell that increases experience gain for a limited time. From `e07a_mothman_wisemothmanaliasscript.psc`, the Mothman Equinox version uses the same `crXPBonusSpell` and displays `E07A_Mothman_BlessingMessage`.

### Mothman Equinox Special Encounter
`LCP_E07A_Mothman_SpecialEncounter_SpawnChance` (`0x00621C36`) and `LCP_E07A_Mothman_SpecialEncounter_Enabled` (`0x00621C35`) control a **rare special spawn** during the Mothman Equinox event -- possibly a unique Mothman variant.

---

## 8. NPCS THAT WATCH PLAYERS / BEHAVE STRANGELY

### Confirmed Creepy NPC Dialogue
| Form ID | Line | Analysis |
|---------|------|----------|
| `[7100A423]` | "I've seen one of these before stalking around the city center. Not something I'd want to piss off, I'll say that much." | Cryptid stalking report |
| `[61009AD7]` | "Don't you understand? She's watching you, watching us, right now." | Unknown "she" watching players |
| `[39006067]` | "Oh, uh, just local gossip? I haven't been watching you or anything like that." | Suspicious denial of surveillance |
| `[71004AF7]` | "Keep your eyes on the skies!" | Cryptid/UFO warning |
| `[000438AA]` | "We all know the Mothman is out there, stalking and watching us, but what of the unseen." | References something BEYOND the Mothman |
| `[7100F8F0]` | "Stop staring at me! Stop it!" | NPC aware of being observed |
| `[61000515]` | "I wasn't programmed to enjoy watching you struggle. But I do." | Robot fourth-wall-adjacent line |
| `[710039C1]` | "We're watching you, our little adversary." | Direct threat |
| `[00042AEB]` | "We are watching you, member." | Enclave surveillance |

### The Mothman's Watching Behavior
`[000438AA]` is particularly interesting: "...but what of the unseen." This references something watching beyond even the Mothman -- possibly the Interloper or an undiscovered force.

---

## 9. THE "STRANGE NOISES" PHENOMENON

### All "Strange Noises" Dialogue Lines
| Form ID | Line | Context |
|---------|------|---------|
| `[0005B564]` | "I've heard a lot of chatter lately about this place. Sounds like there are tons of grunts and strange noises coming from this place." | Generic encounter location |
| `[0005B66A]` | "Watch your back out there, we've heard strange noises tonight." | Night-specific warning |
| `[0005BEA8]` | "Watch your back out there, I've heard strange noises tonight." | Night-specific variant |
| `[0005BED4]` | "Watch your back traveler, there's strange noises out there tonight." | Traveler variant |
| `[6100938C]` | "A trader said this place stank and was full of weird noises." | Location-specific |
| `[6101A213]` | "Well watch your back out there, I've heard some strange noises tonight." | Another night variant |
| `[81007D6D]` | "Things like strange noises coming from the generator room." | Interior-specific |

These lines are used by the **dynamic encounter system** to set atmosphere before random encounter locations. The "noises" are narrative framing -- they're the in-universe explanation for why a random encounter exists at that location. They particularly trigger at night, suggesting some encounters have time-of-day weighting.

---

## 10. FOURTH WALL BREAKS AND META-REFERENCES

### Confirmed Fourth Wall / Meta Lines
| Form ID | Line |
|---------|------|
| `[3900121B]` | **"Here's one I heard: we're all just living in a simulation."** |
| `[81011263]` | **"You know this is a simulation right?"** |
| `[61000515]` | "I wasn't programmed to enjoy watching you struggle. But I do." |
| `[0004E00F]` | **"Now a second NPC is going to speak."** (Dev test line left in data) |
| `[D90010AD]` | **"The second NPC is now going to speak."** (Another dev test line) |
| `[D9001051]` | **"We'll now enter the dialogue menu with the second NPC."** (Dev test line) |
| `[6100C9D7]` | "Ha, provided I can still play it. It's a bit like playing a video game." |

The "living in a simulation" line is delivered by a regular NPC as gossip/rumor, making it a subtle meta-commentary. The "NPC is going to speak" lines are development artifacts left in the string tables.

---

## 11. EASTER EGGS AND CULTURAL REFERENCES

### Movie/Media References (Beyond Smiling Man)
| Form ID | Reference | Source |
|---------|-----------|--------|
| `[3929479B]` | "Ever dance with the devil under a blue moon?" | Batman (1989) -- Joker's line |
| `[3929479F]` | "Yesterday upon the stair, I met a man who wasn't there..." | Hughes Mearns' "Antigonish" poem |
| `[00043833]` | "I'm flying man, I'm flying!" | Could be Titanic reference (chem-induced) |
| `[6100E800]` | "The object of my desire is a bird, so steeped in mystery and legend..." | Maltese Falcon echo |
| `[61007435]` | "Death smiles at us all. All we can do is smile back." | Gladiator (2000) -- Marcus Aurelius quote |
| `[6100B9CB]` | "This is me having a sinister smile." | Self-aware NPC humor |

### The Assaultron Date (RE_SceneDRE05)
A full random encounter where an Assaultron takes the player on a **romantic picnic date**:
- `[000388A0]` "You want to go on a date, then? Splendid! I know a great spot for us to have a romantic picnic, come with me!"
- `[00037E34]` "My perfect picnic location has been taken over by these pesky flies. Be a dear and clear them out?"
- `[000386E3]` "How brave! You took out those flies in no time at all. How about we whip up some Charred Bloatfly for our picnic?"
- `[000386C5]` "Armed combat really brings people together, don't you think? It's romantic!"
- Features: bloatfly meat collection, picnic setup, food preparation, bar finding, drink creation, enemy combat

Keywords confirm the full date flow:
- `RE_SceneDRE05_AssaultronDateAcceptedDialogueSubtopic`
- `RE_SceneDRE05_AssaultronPicnicEncounterDialogueSubtopic`
- `RE_SceneDRE05_AssaultronFoodCreatedDialogueSubtopic`
- `RE_SceneDRE05_AssaultronDrinkCreatedDialogueSubtopic`
- `RE_SceneDRE05_AssaultronBarEnemyKilledFoundDialogueSubtopic`

### The Mannequin Mystery (RE_SceneMP03)
A random encounter with clothed and unclothed mannequins -- with 5 notes:
- Male and female mannequins in clothed and burnt variants
- `RE_SceneMP03_Note01` through `Note05`
- Separate container inventories for each mannequin
- Community interpretation: a serial killer tableau using mannequins

---

## 12. PARANORMAL / SUPERNATURAL ENCOUNTERS

### The Haunted Factory Cover Story
`[strings]` A pre-war government document reveals a government operation using **staged hauntings** as cover:

> "Because of rampant superstition in the local population, we've landed on a cover story involving the factory being haunted. Our security team has been stealthily killing locals and placing the bodies around the factory. We've used the resources in the stealth research lab to give a mystical backstory to the deaths."

This is arguably more disturbing than an actual haunting.

### The Mine Screams
> "The generators are holding, for now. But I hear all kinds of noises from the flooded part of the mine. I know it's impossible, but it sounds like screams. Horrified screams that haunt my nightmares."

### The Cultist Mothman Ritual (RE_ObjectZW01)
`qf_re_objectzw01_0056368f.psc` -- A random encounter with:
- 6 cultists (`Alias_Cultist01` through `06`)
- 1 Mothman (`Alias_Mothman01`)
- Cult statues in 4 sizes (Huge, Big, Med, Small)
- A `Bloodcrate` container
- `MothFurniture01` -- furniture the Mothman uses
- A center marker for the ritual circle

Players can stumble upon an active Mothman summoning ritual in progress.

---

## 13. THE MYSTICAL JUNKIE MERCHANT (Storm Content)

A rare random encounter NPC:
- `NPC_: 0x006F61AB Storm_MysticalJunkieMerchant`
- `QUST: 0x006F73D1 Storm_RE_Scene_MysticalJunkie`
- `KYWD: 0x006F618F MysticalJunkieMerchant_StartKeyword`
- `OTFT: 0x006F61AC Storm_MysticalJunkieMerchantOutfit`
- Has a `FailsafeTimer` global -- times out and despawns

A drug dealer with "mystical" wares, appearing during storm conditions. Part of the Skyline Valley content wave.

---

## 14. STEVEN SCARBERRY -- MOTHMAN PILGRIM COMPANION

### Who He Is
`NPC_: 0x0068D3DA ATX_COMP_Actor_StevenScarberry` -- A CAMP companion NPC. Named after the **real Scarberry family** who were among the original Mothman witnesses in Point Pleasant, WV in 1966.

### His Mechanics
- Vendor: `FACT: 0x0068D3D4 ATX_COMP_Scarberry_VendorFaction` -- sells items
- Sells: Cultist plans, cryptid items, cultist weapons, cultist clothes, cultist armor, books
- Blessing: `MGEF: 0x006939DC ATX_COMP_Scarberry_Blessing_XPBonusEffect` -- gives XP bonus
- Shrine: `FURN: 0x0068D3D5 SCORE_S12_CAMP_Scarberry_Shrine_FURN` -- placeable shrine
- Has a greeting dialogue system and a "wrong player" rejection script

### His Dialogue (Mothman Cult Lore)
Scarberry is a **Mothman cultist on a pilgrimage**, providing deep lore about the cult:

- Claims he was "chosen" by the Mothman, not recruited
- His parents were "freed from their flesh prisons to ascend to His light" (killed/transformed by Mothman)
- He was placed "among the eggs of future harbingers" as a child
- He distinguishes between the "Holy Mothman" and "Wise Mothman"
- References "False Gods" -- other cryptids that test his faith
- Performs blood sacrifice rituals at an altar to grant XP buffs
- `[392945B5]` "Can I get Mothman's Blessing?" -- player can receive his buff

---

## 15. ENCOUNTERS WITH OBSCURE TRIGGERS

### Time-Gated Encounters
The "strange noises at night" dialogue confirms some random encounters have **nighttime weighting**. Multiple variants exist specifically for night:
- "Watch your back out there, we've heard strange noises **tonight**."

### Weather-Gated Content
- `Radstorm_GlowingCreature_Chance` (`0x008464F3`) -- rad storms increase glowing creature spawns
- `Spooky_ScorchedSpawnChance` / `Festive_ScorchedSpawnChance` -- seasonal spawn modifiers
- The Mystical Junkie Merchant is Storm-content-gated

### Spawn Chance Globals (Rarity Hierarchy)
| Global | Description |
|--------|-------------|
| `REChance_Scene` | Base random encounter chance |
| `REChance_Travel` | Travel encounter chance |
| `REChance_Assault` | Assault encounter chance |
| `REChance_Zetan_Content` | Alien encounter chance |
| `REChance_Scene_Special_MTNZ05` | Special scene chance |
| `REChance_Assault_Nuke_Special_WendigoColossus` | Wendigo Colossus in nuke zones |
| `RA_PartyCrasherSpawnChance_Bigfoot` | Bigfoot party crasher chance |
| `LCP_E07A_Mothman_SpecialEncounter_SpawnChance` | Special Mothman variant |

### Zetan/Alien Random Encounters
Full alien encounter content system confirmed:
- `Zetan_Content_RE_Scene` -- scene encounters
- `Zetan_Content_RE_Travel` -- travel encounters
- `Zetan_Content_RE_Assault` -- assault encounters
- `Zetan_Content_RE_Object` -- object encounters
- `RE_Scene_Zetan_01_Headwear_FedoraNONPLAYABLE` -- a fedora worn by the Zetan encounter NPC

---

## 16. WEST VIRGINIA FOLKLORE BEYOND KNOWN CRYPTIDS

### Real-World Cryptids/Folklore in Game
| Creature | WV Folklore Origin | In-Game Status |
|----------|-------------------|----------------|
| **Mothman** | Point Pleasant, 1966 | Full creature + cult + events |
| **Indrid Cold / Smiling Man** | Woodrow Derenberger encounter, 1966 | Rare NPC encounter |
| **Flatwoods Monster** | Braxton County, 1952 | Full creature with teleportation |
| **Grafton Monster** | Grafton, WV, 1964 | Full creature boss |
| **Sheepsquatch** | Boone County, multiple sightings | Full creature + quest line |
| **Snallygaster** | Maryland/WV border folklore | Full creature |
| **Wendigo** | Algonquian mythology (regional) | Full creature + Colossus variant |
| **Jersey Devil** | Pine Barrens (NJ, expanded to WV) | Full creature with fear attack |
| **Bigfoot** | Appalachian sasquatch sightings | NEW -- Party Crasher encounter |
| **The Interloper** | Lovecraftian original (WV mine lore) | Static environmental horror |
| **Steven Scarberry** | Named after real Mothman witness family | CAMP companion |

### Folklore References in Dialogue
- `[6101A39F]` "Flesh eating freaks with an insatiable appetite for flesh, **folklore** says the Wendigo are former criminals possessed by ravenous spirits."
- `[0004AD41]` "Fasnacht traces its roots to **Alemannic folklore**." (German-Appalachian cultural fusion)
- `[8100E289]` "Legendary storyteller **Ray Gary**, who roams the Appalachian wilderness, speaks tall tales of which Cryptid?" (A wandering cryptid storyteller)
- `[71003F68]` "Or perhaps the myth never happened at all, and the truth of this lethal ocean remains buried. The mystery entices, does it not?"

---

## 17. THE EMISSARY

### What We Found
- Three string entries: `[59000779]`, `[5900077B]`, `[5900077C]` -- all named "The Emissary"
- ESM shows two NPC records with FULL names pointing to Emissary strings
- A dedicated voice type: `[59000779]`
- Extremely sparse data -- this appears to be a **Skyline Valley** addition (0x59 prefix = DLC content)
- Community reports describe The Emissary as one of the rarest NPCs in the game

---

## 18. HIDDEN COMPANION INTERACTIONS

### Brother Scarberry's Blessing System
Scarberry has a full prayer/blessing system with multiple states:
- First-time blessing with full ritual dialogue
- "Lilac deception" -- detects if player has been blessed by a rival Mothman faction
- Cooldown system: "I'll be able to pray for you again tomorrow"
- Distinction between Holy Mothman and Wise Mothman factions
- References "False Gods" that test his faith -- the other cryptids

### The "She's Watching" Mystery NPC
`[61009AD7]` "Don't you understand? She's watching you, watching us, right now."
This line appears in a companion/NPC conversation context, suggesting an unnamed female entity surveilling both the player and NPCs. Given the surrounding dialogue context (astronaut training, firearm experience), this may be related to ATHENA or another AI system.

---

## 19. SUMMARY OF UNSOLVED MYSTERIES

1. **What exactly is the Interloper?** -- Jeff Lane's holotapes hint at something beyond comprehension. No scripts interact with it. It just... exists.

2. **Who is "she" that's watching?** -- The line "Don't you understand? She's watching you, watching us, right now" has no clear referent in the surrounding dialogue.

3. **The Strange Woman of Lucky Hole Mine** -- She and her friends wanted to see "the depths." The foreman ran. They broke in. They never came back up. What exactly did they find?

4. **What is "the unseen" beyond the Mothman?** -- "We all know the Mothman is out there, stalking and watching us, but what of the unseen." Explicitly references something ELSE watching.

5. **Indrid Cold's purpose** -- He says he's "seeking a seeker who cannot be found." Who is this seeker? Is it the player? The Mothman? The Interloper?

6. **The "man who wasn't there"** -- Indrid Cold quotes the Antigonish poem. Is this self-referential? Is he the man who wasn't there?

7. **Bigfoot's full implementation** -- When exactly does the Season 24 content go live? The scripts and data are fully in place.

---

## Sources
- [Smiling Man - Fallout Wiki (Fandom)](https://fallout.fandom.com/wiki/Smiling_Man)
- [The Smiling Man (Random Encounter) - The Fallout Wiki](https://fallout.wiki/wiki/The_Smiling_Man_(Random_Encounter))
- [Most Fallout 76 Players Have Never Met These NPCs - GameRant](https://gamerant.com/fallout-76-rare-npcs-smiling-man-emissary-wendigo-colossus/)
- [Fallout 76 Smiling Man Story and Location Guide - GameSkinny](https://www.gameskinny.com/tips/fallout-76-smiling-man-story-and-location-guide/)
- [How to find the Smiling Man in Fallout 76 - Gamepur](https://www.gamepur.com/guides/how-to-find-the-smiling-man-in-fallout-76)
- [Fallout 76's Smiling Man Cranks The Creepy Factor Up to a 10 - GameRant](https://gamerant.com/fallout-76-smiling-man-horror-scary-impact-good/)
- [Fallout 76 in 2026 Is About to Get Wild - EzNPC](https://eznpc.com/fallout-76/blog-fallout-76-in-2026-is-about-to-get-wild-everything-we-know-so-far)
- [25 Hidden Things Many Still Haven't Found In Fallout 76 - TheGamer](https://www.thegamer.com/hidden-things-many-havent-found-fallout-76/)
- [Fallout 76 Players Looking For Secrets Off The Beaten Path - Kotaku](https://kotaku.com/fallout-76-players-are-looking-for-secrets-off-the-game-1830545893)
