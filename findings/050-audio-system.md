# Fallout 76 Audio System Deep Dive

**Source**: 15,340 SNDR records from `full_esm_dump.txt`, decompiled scripts, `seventysix_strings_en.txt`

---

## 1. Explicitly Cut & Deleted Audio

### Cut Radio Tracks (Removed Songs)
The main Appalachia Radio had songs removed post-launch. These remain as tombstone records:

| FormID | Record Name | Notes |
|--------|-------------|-------|
| `0x0044CB88` | `_CUT_DELETE_MUSRadio76TurntableIxxxxxx` | Cut turntable track |
| `0x0038EFED` | `_CUT_DELETE_MUSRadio76Turntablexxx` | Cut turntable track |
| `0x0038EFE8` | `_CUT_DELETE_MUSRadio76Turntablexxxx` | Cut turntable track |
| `0x003D1BB2` | `DEL_MUSRadio76Generalxxxxx` | Deleted general radio song |
| `0x003EB662` | `DEL_MUSRadio76Generalxxx` | Deleted general radio song |
| `0x003EB651` | `DEL_MUSRadio76Generalxxxxxxxx` | Deleted general radio song |
| `0x003EB64F` | `DEL_MUSRadio76Generalxxxx` | Deleted general radio song |
| `0x003EB667` | `DEL_MUSRadio76Generalxxxxxxx` | Deleted general radio song |
| `0x0038E727` | `DEL_MUSRadio76Generalxxxxxxxxx` | Deleted general radio song |
| `0x0038E723` | `DEL_MUSRadio76Generalxxxxxx` | Deleted general radio song |

**Key finding**: At least **7 songs** were removed from Appalachia Radio. The names are obfuscated with "x" characters, suggesting licensing issues forced their removal. The `_CUT_DELETE_` prefix on turntable records indicates they were cut from the turntable/jukebox system specifically.

### Cut Creature Sounds

**Floaters (Original Sound Set — Completely Replaced)**:
Over **40 DEL_ prefixed Floater sounds** exist, covering every combat state (attack, death, dodge, hit, taunt) for all three variants (Chomper, Flamer, Freezer). The live game uses a completely redesigned sound set (`NPCFloater*` without DEL_ prefix). This means Floaters were fully re-voiced at some point during development.

**Trogs (Cut from The Pitt Expansion)**:
Over **30 DEL_ prefixed Trog sounds** across three tiers (Fledgling, Superior, Glowing), including attack, charge, death, dodge, scream, and slobber sounds. Only one live Trog sound reference remains: `QSTMTR08InteriorCollapseOpenOneshotTrog` and `FXPlayerTroglocideBurdenLPM`. The creature exists in-game but its original audio was scrapped and rebuilt.

**Overgrown Creatures (Partial Cut)**:
| FormID | Record Name |
|--------|-------------|
| `0x006DB602` | `NPCOvergrownThorn_DEL` |
| `0x006DB5DB`-`0x006DB608` | `DEL_OvergrownRusher_A` through `_G` + layers |

The "Overgrown Rusher" creature type was completely cut — 14 sound records deleted. The Overgrown Thorn and Elder survive with live audio.

**Scorch Tongue (Partial Cuts)**:
| FormID | Record Name |
|--------|-------------|
| `0x007AE642` | `zzzNPCScorchTongueAttackMelee01_GroundPound_DELETE` |
| `0x007A6C2C` | `zzzNPCScorchTongueDeathWhileStunned_DELETE` |
| `0x007A6C27` | `zzzNPCScorchTongueAttackRange03_Screech_DELETE` |
| `0x007A6C34` | `NPCScorchTongueHitFlinch01_DELETE` |

The `zzz` prefix is Bethesda's convention for "deprecated but kept for reference." The Scorch Tongue (lava boss from Gleaming Depths) had its ground pound, stun-death, and screech attacks cut or reworked. **92 total Scorch Tongue sounds** exist, making it one of the most sonically complex creatures.

### Other Cut Audio
| FormID | Record Name | Notes |
|--------|-------------|-------|
| `0x00113DE4` | `_CUT_DLC04GauntletRaidersIdlexxxxxxxLAYERALPM` | DLC04 Gauntlet Raiders idle — Nuka-World content that leaked into FO76 |
| `0x00522BED` | `CUT_FXExplosionMutationElectricallyChargedxxx` | Cut mutation explosion effect |
| `0x002479E1` | `CUT_test_XXXTestDialogueFPowerArmorSoldier` | Cut test dialogue for Power Armor soldier |
| `0x00537612` | `DEL_BabylonUIStormStops` | Deleted Nuclear Winter storm-stop sound (replaced) |
| `0x0059F5FA` | `DEL_OBJMotherlodeBrokenBLP` | Deleted Motherlode broken sound |
| `0x006EFE1D` | `DEL_OBJLightCreatureDiagramOff` | Deleted light creature diagram |

### Generic Removed Sound Tombstones
| FormID | Record Name |
|--------|-------------|
| `0x0077B583` | `zzz_RemovedSound` |
| `0x0077B582` | `zzz_RemovedUISound` |

These are catch-all records — sounds that were removed and their references redirected here to prevent crashes.

---

## 2. Mothman Sound Design — Complete Analysis

The Mothman has **one of the richest sound profiles** in the game with dedicated audio for every behavioral state.

### Stalking & Ambient Presence
| FormID | Sound | Purpose |
|--------|-------|---------|
| `0x000030FD` | `NPCMothmanIdleConsciousLP` | Base ambient drone — plays when Mothman watches from distance |
| `0x00290F5E` | `NPCMothmanIdleConsciousLAYER2DALP` | 2D ambient layer (surrounds player) |
| `0x00290F5D` | `NPCMothmanIdleConsciousLAYER3DALP` | 3D positional layer (directional) |
| `0x0009A554` | `NPCMothmanIdleConsciousLAYER3DBLP` | Second 3D layer for depth |
| `0x000030FE` | `NPCMothmanIdleBreatheIn` | Breathing in — organic presence |
| `0x000030FF` | `NPCMothmanIdleBreatheOut` | Breathing out |
| `0x00003100` | `NPCMothmanIdleFavorCombat` | Shifts to aggressive idle |

**Design insight**: The Mothman's idle uses a **4-layer compound loop** — a base drone, stereo ambiance, and two positional 3D layers. This creates the sense of an omnipresent threat that seems to come from everywhere at once.

### Teleportation (Appearing/Disappearing)
| FormID | Sound | Purpose |
|--------|-------|---------|
| `0x004E36D7` | `NPCMothmanTeleportEnter1` | First appearance sound |
| `0x004E36DA` | `NPCMothmanTeleportEnter2` | Alternate appearance |
| `0x004E36DD` | `NPCMothmanTeleportExit1` | Disappearing sound |
| `0x003CF679` | `FXExplosionMothmanTeleportDisappear1` | Explosion effect on vanish |
| + 2D/3D layers for each | | Spatial positioning variants |

### Warning / Curse
| FormID | Sound | Purpose |
|--------|-------|---------|
| `0x000030F2` | `NPCMothmanWarn` | Warning cry before attack |
| `0x003A24B6` | `NPCMothmanAttackCurse1` | The "curse" attack sound — unique mechanic |
| `0x003BE89F` | `NPCMothmanBlessing` | **Wise Mothman blessing** — positive encounter sound |

**The Mothman Blessing sound** (`0x003BE89F`) is particularly notable — it plays when the Wise Mothman grants XP bonus. This is one of the only creature sounds in the game that represents a *positive* interaction.

### Movement
The Mothman has turn-specific audio with layered "warn" and "turn" sublayers:
- `NPCMothmanFootTurn90InPlace` + `LAYER_Warn` + `LAYER_Turn`
- `NPCMothmanFootTurn90ToWalk` + layers
- `NPCMothmanFootTurn180ToWalk` + layers
- `NPCMothmanFootWalkDirtL/R`

This means every time the Mothman turns to face you, it plays a warning layer on top of the physical movement sound.

### Combat (Melee, Ranged, Dodge, Ambush)
- 5 melee attacks (`AttackMelee01`-`05`) with 2D/3D layers each
- 2 ranged attacks (`AttackRanged01`-`02`) with layers
- Dodge back/right with layers
- Evade right (2 variants) with layers
- **2 Wall Ambush sounds** (`AmbushWall1`, `AmbushWall2`) — the Mothman can ambush from walls

### Mothman Event & CAMP Sounds
| FormID | Sound | Purpose |
|--------|-------|---------|
| `0x00630A6A` | `WEAEventMothmanEquinoxLP` | Weather loop for Mothman Equinox event |
| `0x00630A77` | `FXPlayerMothmanInfluenced` | Player "influenced by Mothman" effect |
| `0x0062FEF5` | `FXExplosionMothmanTotem` | Totem explosion during event |
| `0x0062FEF7` | `OBJMothmanBloodTroughDonate` | Blood trough donation sound |
| `0x006333B1` | `AMBBonfireMothman_LPM` | Mothman bonfire ambient loop |
| `0x005CF078` | `OBJCuckooMothmanSong` | Cuckoo clock Mothman song |
| `0x005CF077` | `OBJCuckooMothmanChime` | Cuckoo clock chime variant |
| `0x0079A657` | `AMBChimesWorkshopMothman` | Workshop wind chimes — Mothman themed |

---

## 3. "Strange Noises" NPC References

The strings file reveals what NPCs are hearing:

### Direct "Strange Noise" References
- **Vault Harvester Maintenance**: *"I keep hearing strange noises coming from outside and it's starting to give me the willies..."* — refers to ambient Scorched/creature sounds outside vault infrastructure
- **Silo Guard**: *"I swear I heard something. A voice maybe? Could be a Chinese infiltrator using some kind of stealth technology."* — references pre-war paranoia, but in-game maps to ambient silo sounds (`AMBIntMissileSiloTunnelLP`)
- **Survivor Diary**: *"Wait, did you hear that? I think there is something out there."* — generic wilderness encounter trigger
- **"Mysterious Sound"** quest text: *"A strange creature attacks Buck's Den Beer House whenever it hears the sounds of partying."* — This is the **Party Crashers** event, which uses `MUSPartyCrashersDefault_01Start` and `MUSPartyCrashersBigfoot_01Start`

### The Flatwoods Monster ("Green Man") Reference
*"This is the third 'green man' sighting in as many months."* — The Flatwoods Monster's ambient hum is produced by **6 layered conscious loops**:
- `NPCFlatwoodsConsciousLayerALP` through `LayerELP`
- `NPCFlatwoodsConsciousCompoundLP` (master mix)
- Plus jet/hover sounds: `NPCFlatwoodsJetIdleLP`, `JetMedOneshot`, `JetHighOneshot`

### The Whalesong / Interloper Reference
*"I heard something other than whalesong on that tape."* — This directly references the eerie audio found on holotapes, potentially the Interloper's influence.

---

## 4. Holotape & Radio Content

### Cut/Unused Holotape Audio
| FormID | Sound | Notes |
|--------|-------|-------|
| `0x0078A049` | `QSTMQ09HolotapeDistantYell` | Distant yell on MQ09 holotape — atmospheric horror |
| `0x00685534` | `QSTHolotapeUltraciteAbominationTaunt` | Ultracite Abomination taunting on holotape |
| `0x0042B0D5`-`D9` | `QSTVault94_HolotapeDoorOpen/GunReady/GunFire/MinigunUp/MinigunFire` | Full combat sequence recorded on Vault 94 holotapes — sounds of the vault falling |
| `0x0054B4B8` | `QSTVault94_HolotapeGunfireB` | Second gunfire variant |
| `0x006C9DFF` | `QSTHoloSheepsquatchImposterVoxHigh` | Sheepsquatch Imposter vocalization on holotape |
| `0x006C9E01` | `QSTHoloNukeRumbleSiren` | Nuke rumble/siren on holotape |
| `0x0043F4C2` | `QSTHoloCrashedTruckGrafton` | Grafton truck crash holotape |

### Radio Stations Catalog
**Appalachia Radio (MUSRadio76General)**: ~56 songs total, 7 confirmed deleted (licensing)

Active tracks include classics:
- Ink Spots: "I Don't Want to Set the World on Fire", "Maybe", "It's All Over But The Crying", "We Three"
- Bing Crosby & Andrews Sisters: "Pistol Packin' Mama", "Don't Fence Me In"
- Johnny Cash (Co-Pilot): "Ring of Fire"
- Beach Boys: "Wouldn't It Be Nice"
- John Denver (Co-Pilot): "Country Roads" (the signature FO76 song)
- Tennessee Ernie Ford: "Sixteen Tons", "Dark as a Dungeon", "Shenandoah"
- Five Stars: "Atom Bomb Baby"
- Nat King Cole: "Orange Colored Sky"
- Count Basie: "Jumpin' at the Woodside"
- And many more (Glenn Miller, Fats Waller, Billie Holiday, Cole Porter, etc.)

**Pirate Radio (MUSRadioPirate)**: **107 records** — the largest radio station
- 47+ songs (`MUSRadioPirateSong` through `_47`)
- 28 ads (`MUSRadioPirateAd_01` through `_28`)
- Radio dramas: "Rip Daring" (4 episodes), "Tales From Nuka" (5 episodes), "Dread Island" (6 episodes), "Better Life Underground" (5 episodes), "Zorbo's Revenge" (7 episodes), "Inkwell" (4 episodes)

**Big Bloom Radio (MUSRadioBigBloom)**: Classical event station — 7 tracks
- Flight of the Bumblebee, Blue Danube Waltz, Marriage of Figaro Overture, Voice of Spring, Nutcracker Dance of the Reeds, Tales from the Vienna Woods, Waltz of the Flowers

**Mischief Night Radio**: 3 Halloween event tracks (`MUSEventRadio76MischiefNight01-03`)

**Rose's Muzak**: 3 muzak tracks at Top of the World (`QSTRobotRaiderRoseMuzak015/025/035`)

**Whitespring Muzak**: 5 tracks (`MUSRadio76WhitespringMuzakALP` through `DLP` + `DefaultLP`)

**Party Muzak (Jukebox)**: 8 tracks for CAMP jukeboxes (`MUSRadio76JukeboxMuzakParty01-08`)

**HWT Saloon Jukebox**: 7 Western-themed tracks (Born and Bred, The Entertainer, One More Round, Welcome to the South, Maple Leaf Rag, Easy Winners, Dustbowl Saloon)

**Classical Radio**: ~30 classical pieces including Beethoven, Chopin, Debussy, Satie, Holst (Mars + Venus), Wagner (Ride of the Valkyries), Rimsky-Korsakov, Bach, Schubert, Schumann, and more

### Busted Radio Object
`0x0072C7AE` — `OBJATXBustedRadioLP` — An Atomic Shop item that plays a broken/static radio loop. Decorative only.

---

## 5. Environmental Ambient Sounds by Region

### The Forest
- Standard Appalachian ambiance with birds, insects, wind
- Time-of-day cycling: morning birds, daytime insects, dusk cicadas, nighttime crickets/katydids

### Burning Springs / Ash Heap Region
Heavily **muted bird sounds** (suffix `_muted`):
- `AMBExtBurningSpringsBirds1MorningA01LP_muted` — birds exist but are deliberately suppressed
- Sandstorm wind beds: `AMBExtWeatherWindBedBurn_Sandstorm` and `_Lite` variant
- Interior burn region: creaking metal (`CreakMetalA-C`), rumbles (`RumbleA-C`), dirt slides
- Industrial ambiance: `AMBIntBurnHWTBedSmall/Medium/Large`

**Design insight**: The "muted" suffix on bird sounds means the audio designers recorded full birdsong for this region then deliberately suppressed it, creating an unnervingly quiet landscape where nature is dying.

### Cranberry Bog
- Fissure ambient: `AMBExtCaveFissureOmega` — the sound of fissure sites
- Scorchbeast sonic attack echoes throughout the region
- Wendigo Cave Screams: `AmbWendigoCaveScreamOneshot`

### The Mire
- Dense insect soundscapes
- Strangler vine ambient (referenced in dialogue about "controlled creatures")

### Toxic Valley
- `NPCRobotProtectronToxicBobConsciousLP` — Toxic Bob's unique idle with slosh layer
- Chemical/industrial ambient beds

### Savage Divide
- Cave systems with drip ambience
- Mine rumbles: `AmbIntMineRumbleHighComp_WL005`, `AmbIntMineLFEStOneshot_WL005`
- Burning mine interior: fire, embers, flame bursts

### The Burrows (Sewer Dungeon)
Highly detailed ambient system:
- Multiple bed zones: `CentralChamber`, `LeftAqua`, `LeftTunnel`, `LeftShanty`, `LeftRatway`, `OldTunnel`, `PumpStationBoss`
- Water drips (2D and 3D positional variants)
- Sewer pipes and grate ambience
- Wood creaks and "wonk" oneshots (structural stress)
- Squeek oneshots

### Gleaming Depths (Lava Area)
- `AMBIntGleamingDepthsLavaA3DLAYERBLP` — 3D lava ambient
- `AMBIntGleamingDepthsLavalB3D_waterfall_LAYERBLP` — Lava waterfall sound
- Multiple lava layers for depth perception

---

## 6. Cryptid Sound Sets

### Mothman
See Section 2 above. **120+ sound records** — the most sonically complex cryptid.

### Flatwoods Monster
28 records. A multi-layered alien presence:

**Ambient hum (6 layers)**:
- `NPCFlatwoodsConsciousLayerALP` — base hum
- Layers B through E add harmonic complexity
- `NPCFlatwoodsConsciousCompoundLP` — master compound mix
- `NPCFlatwoodsConsciousLayerCDELP` — combined upper layers

**Hover/jet system**:
- `NPCFlatwoodsJetIdleLP` — constant hover drone
- `NPCFlatwoodsJetMedOneshot` — movement burst
- `NPCFlatwoodsJetHighOneshot` — high-speed burst

**Combat**: Laser system with compound layering (`LaserComp`, `LaserLayerA/B`, `LaserProjectile`), melee, teleport in/out with separate SFX and Vox channels.

**Design insight**: The Flatwoods Monster's teleport has both mechanical SFX and alien vocalizations on separate channels — `TeleportIntoSFX` vs `TeleportIntoVox`. This dual-channel approach lets the audio team mix alien and technological elements independently.

### Wendigo
~50 records. Horror-focused sound design:

**Signature Sounds**:
- `NPCWendigoScream` — the iconic distant scream
- `QSTMTNS04WendigoCallClose/Med/Far` — **3 distance-variant calls** for the quest "One of Us" (MTNS04). These play at different ranges to create spatial tracking.
- `AmbWendigoCaveScreamOneshot` — ambient cave scream (plays without a Wendigo present to unnerve players)
- `NPCWendigoScrambleVox` + `NPCWendigoScrambleCompound` — scrambling/scuttling vocalization
- `NPCWendigoLeapAttackVox` + physical `LeapAttack` — separate voice and body layers
- `NPCWendigoChargeVox` + `ChargeFoot` + `ChargeCompound` — 3-layer charge sound
- `NPCWendigoAttackSlobber` — wet slobber attack layer
- `NPCWendigoConsciousLP` — breathing/stalking loop

### Wendigo Colossus (Earle Williams)
30 records. Boss-scale audio:

**Unique mechanics**:
- `NPCWendigoColossusFearPhase1/2` + layers — **2-phase fear attack** with escalating audio
- `NPCWendigoColossusSummon` + `FXWendigoColossusSummonAllies` — summoning wendigo minions
- `NPCWendigoColossusVomit` — vomit attack
- `NPCWendigoColossusAmbushLPM` — ambush loop
- `NPCWendigoColossusHeadA/B/CFire` — triple head fire attacks
- Massive footsteps with front left/right + Layer A/B per foot

### Grafton Monster
~60 records. Brutish audio profile:

**Signature moves**:
- `NPCGraftonAttackGroundPound` — ground pound with 2D/3D and separate impact sounds
- `NPCGraftonOilBombProjectile` + `OilBombExplosionA/B` — oil bomb ranged attack (3 sounds)
- `NPCGraftonAttackHammerFist` (Standing/Forward/Behind variants)
- `NPCGraftonAttackSweep` (Left/Right/Forward)
- `NPCGraftonAttackSalvoA` — salvo attack
- `NPCGraftonAmbushA` — ambush emergence
- `NPCGraftonWarnA` — warning vocalization
- `NPCGraftonLocoRunBreathe` — heavy breathing while running
- `NPCGraftonInjuredCrippleEnter/Exit` — crippled state transitions

### Snallygaster
~25 records. Predatory stalker:

- `NPCSnallygasterWarnA` + distance variants (`Close`, `Distant`) — 3-distance warning system
- `NPCSnallygasterAmbushA` — ambush attack
- `NPCSnallygasterAttackRangedA` — spit/projectile attack
- 6 attack variants (A-F)
- `NPCSnallygasterConsciousLP` — ambient hunting loop

### Sheepsquatch
~50 records. Dual-nature (real + robot imposter):

**Real Sheepsquatch**: Full organic combat sounds — sweeps, lunges, back kicks (Left45/90, Right45/90), power attacks, headbutt, dodge.
- `NPCSheepsquatchConsciousLPLayerA/B` — 2-layer ambient
- `NPCSheepsquatchIdleEquip` — equip/ready sound

**Robot Imposter (Assaultron)**: Complete separate sound set:
- `NPCRobotAssaultronSheepsquatchVoxBaa` — mechanical "baa" vocalization
- `NPCRobotAssaultronSheepsquatchVoxBaaEyebot` — eyebot speaker variant
- `NPCRobotAssaultronSheepsquatchVoxHigh/Low/Short` — multiple vocalizations
- `NPCRobotAssaultronSheepsquatchAttackHandSpinLPM` — spinning hand attack loop
- `NPCRobotAssaultronSheepsquatchPairedKill` variants — kill animations with head laser

### Bigfoot / Sasquatch (Party Crashers Event)
**58 records** — a surprisingly complete creature:

- `NPCBigfootIntroRoar` + layers — dramatic entrance
- `NPCBigfootOutroRoarStomps` + layers — exit with ground-shaking stomps
- `NPCBigfootAttack01-03` with A layers (MutedIntentionally variants exist — some attacks are silent!)
- `NPCBigfootAttackStomp` + `StompImpact` + layers — ground pound
- `NPCBigfootAttackRanged` + layers — ranged attack (tree trunk throw?)
- `NPCBigfootAttackOnGround_MutedIntentionally` — attack sound explicitly muted
- `WPNImpactBigfootTreeTrunkDirt` + 2D/3D layers — tree trunk weapon impacts
- `NPCBigfootInjuredHitDialogue` + layers — injured vocalization with "dialogue" tag (it speaks?)
- `NPCBigfootGetUpFaceDown/FaceUp` — recovery animations
- `MUSPartyCrashersBigfoot_01Start` — dedicated boss music

**Key discovery**: `NPCBigfootInjuredHitDialogueLayerA/B` — The "Dialogue" suffix on injured sounds is unique among creatures. This suggests the Bigfoot vocalizes something speech-like when hurt, unlike any other creature in the game.

### Scorchbeast / Scorchbeast Queen
**60+ records**. The apex predator:

- Sonic attack system: `WPNImpactScorchbeastSonicAttack` + flesh variant + rad layer
- Queen fissure spawn: Multiple scream variants (`Spawn01ScreamA/B/C`, `Spawn02ScreamA/B`) each with 3 audio layers
- Queen EMP attack with dedicated scream layers
- Takeoff explosion: `FXExplosionScorchBeastTakeoff` + 4 positional layers
- Queen forward charge: `AttackGroundForwardCharge` with 4 layers
- Fire fissure open/close sounds
- Specimen jar: `OBJScorchbeastHearSpecimenJarLP` — the mounted head display hums

### Ultracite Abomination
19 records. Underground horror:

- `NPCUltraciteAbominationTunnelEnter/Exit` — emerges from tunnels
- `NPCUltraciteAbominationScream` + layers — signature scream
- `NPCUltraciteAbominationBelch` + layers — acid belch
- `NPCUltraciteAbominationConsciousLP` — ambient loop
- `QSTHolotapeUltraciteAbominationTaunt` — taunts on holotape recordings

---

## 7. Cut Radio Stations & DJs

### Confirmed Removed Radio Content
- **7 deleted songs** from Appalachia Radio (see Section 1)
- **3 cut turntable tracks** — the turntable system had tracks removed
- `DEL_MUSRadio76General*` records prove songs existed and were pulled

### Nuclear Winter Radio
- `MUSRadioBabylonZAXMusicLP` — ZAX mainframe music in the lobby
- `MUSRadioBabylonLobbyMusicLP` + `SmallLP` — two lobby music variants (large/small lobby)

No evidence of a cut DJ character. The radio stations use pre-recorded playlists without DJ commentary (except Pirate Radio which has ad segments and radio dramas).

---

## 8. Vault 76 Tutorial Audio

Only one tutorial-specific sound found:
- `0x00436F9E` — `UITutorialPopUp` — the UI notification sound for tutorial prompts

The Vault 76 tutorial relies primarily on:
- Standard UI sounds for pip-boy interactions
- Environmental sounds reused from vault interiors
- The Overseer's holotape dialogue (handled by the dialogue system, not SNDR records)

The Overseer's chair sounds exist as DLC06-prefixed records: `DLC06NPCHumanOverseerChairEnter/Exit`.

---

## 9. Nuclear Winter (Babylon) Audio — Complete System

**55+ records** documenting the full battle royale experience:

### Pre-Match
| FormID | Sound | Purpose |
|--------|-------|-------|
| `0x0053C019` | `UIStartNewGameNuclearWinter` | Mode selection sting |
| `0x00469E1E` | `BabylonUIPickSpawnLocation` | Spawn location select |
| `0x00471378` | `BabylonUISpawnTimerFinal` | Final spawn countdown |
| `0x00471379` | `BabylonUISpawnTimerCountDown` | Countdown ticks |
| `0x0047137A` | `BabylonUIOverseerLevelLow` | Low overseer level warning |

### Match Ambience
| FormID | Sound | Purpose |
|--------|-------|-------|
| `0x004125A4` | `AMBBabylonEntryBirds` | Entry area birds |
| `0x00402DEE` | `AMBBabylonStagingBirds` | Staging area birds |
| `0x00404825` | `AMBBabylonCasinoAmbience` | Casino building ambient |
| `0x00405D33` | `AMBBabylonBoxingAmbience` | Boxing ring ambient |
| `0x004125A5` | `AMBBabylonZAXComputerRoom` | ZAX computer room |
| `0x004125A6` | `AMBBabylonZAXMainframe` | ZAX mainframe ambient |

### Storm System (6-tier boundary)
The fire storm had **6 boundary tiers**, each with enter/exit sounds:
- `BabylonBoundaryTier0Enter/Exit_LPM` through `Tier5Enter/Exit_LPM`
- `BabylonSearLine_LPM` + `LOD1_LPM` + `Compound_LPM` — the fire wall itself with LOD

### Combat & Events
| FormID | Sound |
|--------|-------|
| `0x0056940A` | `BabylonUIEnemyTargetKilled` |
| `0x00569409` | `BabylonUIEnemyTargetDowned` |
| `0x005A119C` | `BabylonUITicketsGained` |
| `0x0046ECE5` | `BabylonUINukeAvailable` |
| `0x00438B0B` | `BabylonUINukeBriefcaseFound` |
| `0x004FDEAE` | `BabylonIncomingNukeSiren` |
| `0x003CAD11` | `BabylonUINukeWarning` |

### End Game
| FormID | Sound |
|--------|-------|
| `0x00422178` | `BabylonUIPlayerWins` |
| `0x004277A8` | `BabylonUIEndGamePlayerWinsAnim` |
| `0x003CAD12` | `BabylonUIPlayerKilled` |
| `0x003CAD0F` | `BabylonUIFinalFight` |
| `0x003CAE58` | `BabylonUIVictory` |
| `0x00422175`-`79` | End game info blade, XP gained, rank gained, upcoming rewards |

### Loot Crates (3 tiers)
- `DRSBabylonHighCrateOpen/Close` — high-tier loot
- `DRSBabylonMedCrateOpen/Close` — medium-tier loot
- `DRSBabylonEpicCrateOpen/Close` — epic-tier loot

### Test Audio
| FormID | Sound | Notes |
|--------|-------|-------|
| `0x003D42B2` | `BabylonAudioTestOneshotLong` | Test tone — long |
| `0x003D42B4` | `BabylonAudioTestOneshotShort` | Test tone — short |
| `0x003D42B3` | `BabylonAudioTestOneshotLoop_LP` | Test tone — looping |

These test tones were used during development to calibrate NW audio and were never cleaned up.

---

## 10. The Smiling Man Encounter

### Audio Records
**No dedicated SNDR records** for the Smiling Man creature itself.

### ESM References Found
| Type | FormID | Name |
|------|--------|------|
| `NPC_` | `0x0068EB57` | `RE_Scene_Cold_SmilingMan` — Random encounter NPC |
| `VTYP` | `0x0068EB59` | `RE_Scene_Cold_SmilingManVoiceType` — Has a unique voice type |
| `OTFT` | `0x0068EB58` | `RE_Scene_Cold_SmilingManOutfit` — Custom outfit |
| `ENTM` | `0x008ABF8B` | `SCORE_S24_ENTM_PlayerIcon_SmilingManPatch` — Season 24 scoreboard icon |
| `AVTR` | `0x008ABF82` | `SCORE_S24_AVTR_PlayerIcon_SmilingManPatch` — Avatar icon |

The Smiling Man has:
- A unique voice type (suggesting dialogue exists)
- A bandana mesh: `armor/doggear/smilingmanbandana.bgsm`
- Season 24 Scoreboard cosmetics (player icon, avatar)

**Audio finding**: The Smiling Man relies on the generic human NPC sound system rather than having bespoke creature audio. The encounter's horror comes from the **absence** of unique sound — an eerily silent humanoid figure that shares the same audio profile as any other NPC. The `RE_Scene_Cold_` prefix means it's a "cold" random encounter type — it appears without warning or ambient buildup.

The strings file confirms the encounter exists as a full gameplay event with its own quest entry: *"The Smiling Man"* (`[39294757]`).

---

## 11. The Interloper & Lucky Hole Mine Audio

### Direct Records
No SNDR records found with "Interloper" or "LuckyHole" in their names.

### Related Audio
The Interloper encounter uses:

**Children of Atom Whisper**: `0x001107CA` — `DLC03QSTAtomM01Whisper2D` — a 2D whisper effect from the Far Harbor Atom cult questline, repurposed for the cultist presence in Lucky Hole Mine.

**Cultist Audio**:
- `0x0063538F` | `ITMCultistHighPriestPackUse/Up/Down` — Cultist High Priest item sounds
- `0x0062FADD` | `NPCCultistHighPriestConsciousLP` — High Priest ambient breathing loop
- `0x004275B5` | `ITMDarkBooksOccultUp` — Occult book interaction

**Cave Ambient System** (used in Lucky Hole Mine):
- `AMBIntCaveBedAFrontLP` / `ARearLP` — cave ambient beds
- Mining sounds: `AmbIntMineRumbleHighComp`, `AmbIntMineLFEStOneshot`
- Collapsing mine effects: `FXCollapsingMineIdleAnim01/02LPM`

**Design insight**: The Interloper's horror is achieved through **ambient design rather than creature-specific audio**. The creature itself uses no unique sound records — the atmosphere is built entirely from cave ambience, cult audio, and the oppressive silence of the mine interior. The lack of dedicated Interloper audio is itself the design choice — the thing is so alien it defies sonic representation.

The string *"I pray every moment I can. Nothing. I hear nothing. I used to hear something. I think?"* reflects this design philosophy — the Interloper's influence is characterized by the **absence** of expected sound.

---

## 12. Music Tracks by Region/Event

### Playable Instruments System
FO76 has an extensive instrument crafting system with **19 instrument types**, each with multiple song variations (A/B/C) and 4-part structure (Intro/Rhythm/Lead/Outro):

1. Acoustic Guitar (3 song variants)
2. Steel/Slide Guitar (3 variants + slide)
3. Upright Bass (3 variants)
4. Banjo (3 variants)
5. Snare Drum (3 variants)
6. Frame Drum (3 variants)
7. Lunchbox Drum (3 variants)
8. Plastic Barrel Drum (3 variants)
9. Metal Barrel Drum (3 variants)
10. Mouth Harp (3 variants)
11. Tuba (3 variants)
12. Jug (3 variants)
13. Upright Piano (3 variants)
14. Grand Piano (3 variants + casino variants)
15. Theremin (3 variants)
16. Metal Mallet Barrel Drum (variant of #9)
17. Electric Guitar (2 variants)
18. Organ (2 variants)
19. Pipe Organ (1 variant) + Drum Set (3 variants)
- Plus: Saxophone, Violin, Hambone (body percussion), Nukelele, Xylophone, Raider Guitar (4 variants)

**Total**: ~200+ instrument sound records.

### Event-Specific Music
| Sound | Event |
|-------|-------|
| `MUSPartyCrashersDefault_01Start` | Party Crashers (default creature) |
| `MUSPartyCrashersBigfoot_01Start` | Party Crashers (Bigfoot variant!) |
| `MUSEventRadio76MischiefNight01-03` | Mischief Night (removed Halloween event) |
| `MUSMysteriousStrangerA/B` | Mysterious Stranger perk activation |
| `E08A_Moonshine_MUSRadio76JukeboxMTNS0402` | Moonshine Jamboree jukebox |

### Location-Specific Jukeboxes
- **Frat House**: `MUSRadio76JukeboxFratHouse` + layers
- **Nukashine Distillery**: `MUSRadio76JukeboxNukashineTeaAtTheRitz` + layers
- **Blue Ridge Office**: `MUSRadio76JukeboxBlueRidgeOffice` + layers
- **Atlas Observatory**: `MUSRadio76JukeboxAtlasObservatory` + layers
- **Raider Crater**: `MUSRadio76JukeboxRaiderCrater` + layers
- **Raider Lumber Mill**: `MUSRadio76JukeboxRaiderLumberMill` + layers

### Weather-Specific Audio
- **Rad Storm (Outwaste)**: 5-layer system (`ATX_WeatherOutwasteRadStorm` + Layers A/B/C + Bed)
- **Halloween Overcast**: Creature howls (`WEAHalloweenOvercastCreature01-03`), wolf howl, heartbeat loop, CAMP ambient
- **Aurora/Winter**: 3 aurora layers + 2 spot layers for winter event
- **Big Bloom Pollen**: Wind bed loops for verdant pollen weather
- **Rain**: Heavy hi/lo, storm hi/lo, fake interior wood variant
- **Lightning**: Near strike sound
- **Thunder**: 3 variants (distant storm lo/hi/med)

### Unused/Interesting Music
- `MUSRadio76QSTBritishGrenadiers` — British Grenadiers march (quest-specific)
- `MUSRadio76QSTSM03` — Quest SM03 specific music
- `MUSRadio76GramophoneStart/Stop` — Gramophone player start/stop (not a radio station — physical object)

---

## Summary of Key Findings

1. **7+ songs removed from Appalachia Radio** due to likely licensing issues, names obfuscated
2. **Mothman has 120+ sound records** with a 4-layer ambient system designed to feel omnipresent
3. **Bigfoot has speech-like "dialogue" injury sounds** — unique among all creatures
4. **Floaters were completely re-voiced** — 40+ original sounds deleted and replaced
5. **Trog audio was scrapped and rebuilt** for The Pitt expansion
6. **The "Overgrown Rusher" creature was cut** — 14 sounds deleted
7. **Nuclear Winter's complete audio system** (55+ records) remains in the game files, including 6-tier storm boundaries and 3-tier loot crates
8. **The Smiling Man has no unique audio** — its horror comes from sharing generic NPC sounds
9. **The Interloper has no dedicated sound records** — the horror is built from silence and ambient cave audio
10. **3 Babylon audio test tones** were never cleaned up from the data
11. **Scorch Tongue had attacks cut** mid-development (ground pound, stun-death, screech)
12. **Pirate Radio is the largest station** with 107 records including 5 original radio drama series
13. **DLC04 Gauntlet Raiders** audio from Fallout 4's Nuka-World leaked into FO76's data
14. **Wendigo has 3-distance call system** for spatial tracking in quests
15. **24 playable instruments** with 200+ sound records — the largest musical sandbox in any Fallout game
