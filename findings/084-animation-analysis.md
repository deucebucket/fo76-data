# FO76 Animation Archive Deep Dive

**Source:** `SeventySix - Animations.ba2` (369MB)
**Total Files:** 31,432 (21,913 .hkx animation files + 9,519 .txt animation data files)
**Archive Type:** GNRL v1

---

## 1. High-Level Breakdown

### File Counts by Actor Type (Top 30)

| Actor | Files | Notes |
|-------|-------|-------|
| character (player/human NPCs) | 8,895 | 3,087 first-person + 6,092 third-person |
| powerarmor | 2,471 | Full separate skeleton with all weapon/emote mirrors |
| supermutant | 735 | Includes cover system animations |
| scorched | 725 | Cover system + weapon overrides |
| createabot (custom robots) | 613 | Assaultron, Protectron, Sentrybot |
| dlc03 (Far Harbor) | 570 | Angler, Fog Crawler, Gulper, Hermit, Rad Rabbit/Chicken |
| dogmeat | 429 | Full companion AI with swimming |
| dlc04 (Nuka-World) | 399 | Cave Cricket, Swarm, Animatronic, Bloodworm |
| dlc01 (Automatron) | 354 | Robot creation expansion |
| moleminer | 298 | Cover system animations present |
| feralghoul | 167 | Multiple ambush types |
| mirelurkking | 129 | Swimming animations |
| deathclaw | 115 | Includes car-flipping animation |
| radstag | 114 | |
| mirelurkqueen | 108 | |
| wendigo | 105 | |
| sheepsquatch | 104 | Quill attacks, back kicks, lunges |
| mirelurk | 104 | |
| mothman | 103 | Teleport, curse, blessing, stalking |
| yaoguai | 101 | Kill-move paired animations |
| robot (generic) | 97 | |
| radscorpion | 92 | |
| molerat | 92 | |
| mirelurkhunter | 91 | |
| snallygaster | 85 | |
| _testcharacter | 81 | **Dev test rig** |
| honeybeast | 81 | |
| alien | 81 | Full combat set |
| megasloth | 79 | |
| mosquito (bloodbug) | 78 | Paired human siphon kill-moves |

### Unique/Rare Actors

| Actor | Files | Significance |
|-------|-------|-------------|
| stormboss | 56 | **Tempest boss** - coil gun + lightning attacks |
| wendigocolossus | 51 | Earle Williams boss - fear/summon head attacks |
| trogg | 52 | The Pitt creatures |
| radbeaver | 32 | Newer critter addition |
| frog | 34 | Critter with 4 idle variants |
| fox | 34 | West Virginia wildlife critter |
| owl | 25 | Combat-capable (dodges, evades, attacks) |
| ultraciteabomination | 23 | Fissure emerge/retreat animations |
| radpheasant | 17 | |
| firefly | 16 | |
| vertibot | 14 | Cargo claw release animation |
| libertyprime | 10 | Full behavior set - gantry exit, agitator insert |
| radhog | 7 | **Skeleton + behaviors only, NO animations** |
| wanamingo | 2 | **Skeleton only** - classic Fallout 2 creature |
| zetaninvader | 2 | Spawn-in + alien rifle - minimal |
| vulture | 1 | Skeleton only |
| cat_pet | 1 | Skeleton only - planned pet system? |
| bipedrobot | 1 | Skeleton only |

---

## 2. Cover System Animations (The Big Find)

**Total cover animations: 284 files across 5 actor types.**

This is a COMPLETE cover-based shooter system that was built and then cut. The animations prove it was fully functional, not just prototyped.

### Cover Actors

| Actor | Cover Anims | Notes |
|-------|-------------|-------|
| character (player) | 177 | Standing, kneeling, left/right sides, weapon-specific |
| scorched | 40 | Full NPC cover AI |
| supermutant | 40 | Hunting rifle + machine gun cover |
| moleminer | 19 | Gripassault cover set |
| powerarmor | 8 | Covert sidearm only |

### Cover Animation Types Present

**Standing Cover (Right Side):**
- `riflecoverstandingrightentertrans` - enter cover from right
- `riflecoverstandingrightexittrans` - leave cover from right
- `riflecoverstandingidle` - idle behind cover
- `riflecoverstandingidleshuffleforward` - shuffle along cover
- `riflecoverstandingidlerighttolefttrans` - switch sides
- `riflecoverstandingrightfiresingleblind` - blind fire single shot
- `riflecoverstandingrightfireautoblind` - blind fire automatic
- `riflecoverstandingrightfireautoblindtrans` / `transrev` - transition in/out of blind fire

**Sighted (Peeking):**
- `riflecoverstandingidlesightedtrans` - transition to aimed
- `riflecoverstandingsightedfiresingle` - aimed single shot from cover
- `riflecoverstandingsightedfireauto` - aimed auto fire from cover
- `riflecoverstandingsightedgrenadethrow` - throw grenade from cover
- `riflecoverstandingsightedgrenadethrowleft` - left-hand grenade
- `riflecoverstandingidlesightedshuffleforward` - aimed shuffling

**Kneeling Cover:**
- `rifleidlereadycoverrightkneel` - kneel behind cover
- `rifleidlereadycoverrightkneelshuffleforward` - shuffle while kneeling
- `riflereloadcoverrightkneel` - reload while kneeling
- `riflestandingcovertocrouchcover` / `riflecrouchcovertostandingcover` - stand/crouch transitions

**Movement While in Cover:**
- `walkforwardcoverright` - walk forward in cover
- `walkbackcoverright` - walk backward in cover
- `walkrightcoverright` - walk right in cover
- `riflecrouchwalkforwardcoverright` - crouch walk forward
- `riflecrouchwalkbackcoverright` - crouch walk back
- `riflecrouchwalkrightcoverright` - crouch walk right
- `sneakwpnentercover` - enter cover from sneak

**Cover Entry:**
- `sneakwpnentercover` - sneak into cover
- `rifleidlereadycovermirrortrans` - mirror/switch sides

**Weapon-Specific Cover:**
- Pistol: Full cover set (23 anims)
- Grip Rifle Straight: Full cover set (27 anims)
- Hunting Rifle: Cover reload variants
- Laser Musket: Cover reload variants
- Laser Rifle (straight + rapid): Cover reload variants
- Pipe Rifle Pistol: Cover reload variants
- Double Barrel Shotgun: Cover reload variants

**Covert Sidearm (separate weapon class):**
- Full 1st-person weapon set (41 anims) - jiggle, fire, sight, reload, melee, sprint
- 3rd-person assembly/fire/reload
- Power armor covert sidearm variants
- This is a dedicated stealth pistol weapon class

### Assessment

The cover system was **production-ready**. Evidence:
1. Player animations in both 1st and 3rd person
2. Three enemy types had full cover AI (scorched, super mutant, mole miner)
3. Multiple weapon types supported
4. Standing AND kneeling variants
5. Blind fire AND aimed fire from cover
6. Grenade throwing from cover
7. Movement along cover walls
8. Transition animations between all states
9. Cover reload animations per weapon type

This was likely cut because it fundamentally changed FO76's combat pacing and would have made PvP dramatically different. May have been part of Nuclear Winter's original design.

---

## 3. Mothman Animation Set (Cryptid Analysis)

**103 animations total** - one of the most complex creature rigs in the game.

### Stalking/Passive Behavior
- `idle` - standing watch pose
- Multiple `idle_ver` variants via dynamic animation system
- `walkforward` / `walkbackward` - deliberate movement
- Full turning set (30, 90, 180 degrees, in-place and to-walk)

### Teleportation System
- `teleport_enter1` - vanish animation (non-combat)
- `teleport_exit1` - appear animation (non-combat)
- `combat/teleport_enter1` - vanish during fight
- `combat/teleport_exit1` - appear during fight

Two separate teleport sets: one for passive stalking, one for combat repositioning.

### Combat Abilities
- `attack_melee3` through `attack_melee5` - physical strikes
- `attack_ranged1` through `attack_ranged3` - ranged attacks
- `attack_ranged_additivewing4` - wing-based ranged attack variant
- `attack_curse1` - **curse attack** (unique to Mothman)
- `combat/blessing` - **blessing animation** (Wise Mothman?)
- `combat/warn` - warning behavior before attack

### Injured System (Mobility Damage)
- `injured/mobilityright/` - right wing damaged: limited movement, still attacks
- `injured/mobilityleft/` - left wing damaged: limited movement, still attacks
- `injured/mobilitydown/` - both wings damaged: grounded, ranged only
- Each injured state has: idle, walkforward, turning, 3 ranged attacks

### Ambush
- `combat/ambush/ambush` - standard ambush
- `combat/ambush2/ambush` - alternate ambush variant

### Player Emotes/Items Related
- `funkymothman` - dance emote
- `mothmanworship` - worship emote (male + female)
- `vengefulmothman` - vengeful emote
- `mothmanfound` - photomode pose
- `thronewisemothman` - furniture (sit on Wise Mothman throne)
- `sacredmothmantome` - furniture (read Sacred Mothman Tome)

---

## 4. Flatwoods Monster Animation Set

**71 animations** - complex alien entity with unique abilities.

### Key Animations
- `teleport_enter1` / `teleport_exit1` - teleportation (like Mothman)
- `healing` - self-healing animation
- `firesingle` / `fireauto` - ranged energy attacks
- `chargeattack1` / `chargestop1` / `chargestrike1` - charge attack combo
- `idle_dazed` - dazed/stunned state
- `injuredenter` - injury transition
- `furniture/spawnin/activate` - scripted spawn-in
- 6 melee attacks covering all directions (front, left, right, 180)
- Full dodge, evade, stagger, critical hit system
- Sprint and run additives

### Mind Control
No explicit "possess" or "mind control" animation, but the entity's behavior is likely handled through Papyrus scripts rather than dedicated animations. The `chargeattack` + `chargestrike` combo may be the visual component of its possession mechanic.

---

## 5. Cut/Unused Content

### Test Animations (Still in Archive)
- `meshes/test/defaultbehavior/` - 6 files: complete test project with skeleton, behavior, 2 anims
- `meshes/actors/_testcharacter/` - **81 files**: full behavior test rig with mood variants (confident, depressed, friendly, irritated, nervous, neutral), weapon behaviors, furniture
- `testblendingstates` - blending test behavior
- `targetdummy01` - shooting range target with skeleton + behavior
- `testchamberambush` - Super Mutant Behemoth test chamber

### Skeleton-Only Actors (Cut or Planned)
- **Wanamingo** (2 files) - Classic Fallout 2 creature. Only skeleton + bone LOD. Was planned then abandoned or the animations are in a different archive.
- **Vulture** (1 skeleton + 4 behavior files) - Flying scavenger. Has a unique behavior but the "animations" are just the behavior framework.
- **Cat Pet** (1 skeleton) - Separate from the regular cat actor. Suggests a pet system was planned with dedicated pet skeletons.
- **Biped Robot** (1 skeleton) - Generic humanoid robot skeleton. Possibly early prototype for a cut robot type.
- **Radhog** (7 files) - Has skeleton, root behavior, core behavior, ambush behavior, furniture behavior -- but **zero animation files**. The behaviors are built but the creature was never animated. Planned content.

### Zetaninvader (Alien NPC)
Only 2 animation files:
- `furniture/spawnin/activate` - spawning in
- `weapon/alienrifle/wpnassemblypose` - holding alien rifle

Suggests this was a humanoid alien NPC that would reuse the human character skeleton but was barely implemented.

---

## 6. Weapon Animation Analysis

### Full Weapon Types with Dedicated Animation Sets (1st Person)

**Standard Weapons (shipped):**
10mm SMG, .44 Pistol, Alien Blaster, Alien Rifle, Assault Rifle (Handmade), Auto Grenade Launcher, Binoculars, Black Powder Pistol/Rifle, Broadsider, Camera, Combat Shotgun, Compound Bow, Crossbow, Cryolator, Double Barrel Shotgun, Fat Man, Flamer, Flare Gun, Gamma Gun, Gatling Gun, Gatling Laser, Gatling Plasma, Gauss Rifle, Gauss Shotgun, Harpoon Gun, Hunting Rifle, Junk Jet, Laser Musket, Laser Rifle (straight + rapid), Lever Action, Minigun, Missile Launcher, Pipe Rifle variants, Plasma Caster, Plasma Pistol/Rifle, Pump Shotgun, Quad Launcher, Railway Rifle, Single Action Revolver, Submachine Gun, Syringer

**Melee with Dedicated Sets:**
1H Melee, 1H Short, 2H Melee, 2H Wide, Auto Axe, Baton, Board, Boxing Glove, Buzz Blade, Chainsaw, Deathclaw Gauntlet, Drill, Knuckles, Pitchfork, Power Fist, Ripper, Shepherd's Crook

**Interesting/Notable Weapon Sets:**

| Weapon | 1P Anims | Notes |
|--------|----------|-------|
| **Meltdown** | 38 | Has unique `wpnoverload` animation - weapon overload mechanic |
| **Lightning Gun** | 71 | Full weapon set - electric weapon |
| **Acid Soaker** | 62 | Full weapon set - water gun reskin? |
| **HMG** | full set | Heavy Machine Gun - distinct from minigun |
| **M2** | full set | .50 cal machine gun with charge up/down |
| **M79** | full set | Grenade launcher |
| **Screaming Eagle** | 3 | Reload only (drum mag variant) - mostly reuses assault rifle |
| **BOS Pistol** | 5 | Reload variants (mag556) - Brotherhood weapon |
| **Handmade Revolver** | full set | Both grip styles |
| **Gauss Pistol** | present | Wastelanders addition |
| **Pepper Shaker** | 18 | Shotgun variant |
| **Paddle Ball** | present | Novelty weapon from Nuka-World |
| **Thirst Zapper** | present | Nuka-World water gun |
| **Grognak Guitar** | present | Melee instrument weapon |
| **Plasma Caster** | present | Wastelanders heavy weapon |
| **Covert Sidearm** | 41 (1P) | Dedicated stealth pistol class |
| **Gamma Rifle** | separate | Different from Gamma Gun |
| **Assaultron Head** | present | Decapitated head weapon |
| **Compound Bow** | full set | Includes `wpnboltchargeready/sighted` and `wpnprechargehold` |

### Meltdown Weapon (Notable)
The "Meltdown" weapon has a unique `wpnoverload` animation in both 1st and 3rd person. This is the only weapon with an "overload" mechanic. It also has:
- `coremeltdownfx` unique behavior - visual FX for core meltdown
- `meltdownrifleweaponfx` - weapon-specific FX behavior
- Assembly pose, equip, fire (single + auto), reload, melee, sprint
- Power armor variants

This appears to be a weapon that can be overcharged to the point of meltdown, distinct from any currently shipped weapon.

---

## 7. Vehicle/Mount Animations

### Vertibird (29 animations)
Full flight system:
- `hoveridle` / `landidle` / `forwardglide` - flight states
- `takeoff` / `takeoffwithforwardmotion` / `takeoffuntrained` - takeoff variants
- `land` / `landtouchdown` / `crashland` - landing
- `injuredflight` / `forwardglideinjured` - damaged flight
- `injuredleftwing/` / `injuredrightwing/` - wing-specific damage (hover + glide)
- `prydwenperch/` - docking with Prydwen (FO4 holdover)
- `propellersstart` / `propellersstop` - engine animations
- `doorcloseopen` / `rudderandflaps` - mechanical parts
- `staggerright` / `staggerback` - hit reactions

### Vertibot (14 animations)
Automated drone:
- `hovertoland` / `hovertolandadditive` - landing
- `clawrelease` - **cargo drop claw** (supply drops)
- `directionaltiltadditive` - movement banking
- `deferreddeathidle` - delayed death state

### Vehicle-Adjacent
- `deathclaw_flipcar` - Deathclaw flipping a car
- `behemothcartfx` - Behemoth pushing/throwing a cart
- `dlc06/furniture/workshopstationarybike` - stationary exercise bike (Expeditions)
- `coinopgolfcartride` - rideable golf cart (CAMP item)
- `coinoprocketride` - rideable rocket (CAMP item)
- `giddyupbuttercupride` - rideable Giddyup Buttercup
- `mechanicalbuckingbrahmin` - rideable bucking brahmin
- `pepperonirollcoinopride` - rideable pepperoni roll (WV themed)
- `vertibirdinterior` / `vertibirdinteriorpilot` - player inside vertibird (furniture)

**No rideable mounts or drivable vehicles found.** All "rides" are stationary CAMP furniture. The vertibird system is NPC-only with the player as a passenger via furniture animations.

---

## 8. Swimming/Diving Animations

### Player Swimming
- 8 directional swim animations (swim000 through swim315 - 45-degree increments)
- `swimidle` - treading water
- `swimturnleft` / `swimturnright` - turning
- `swimturninplaceleft90` / `swimturninplaceright90` - quick turns
- `swimcrawlforward` - forward crawl stroke
- `swimdrink` - drinking while swimming
- `swimessentialdown` - essential NPC down-state in water
- 1st person: `rifle/swimforward`, `rifle/swimidle`, `rifle/swimsprint`

### Creature Swimming
- **Dogmeat:** 7 swim anims (forward, fast, left/right, idle)
- **Super Mutant:** swim idle, turns, crawl forward
- **Rad Beaver:** 3 swim anims (forward, turn left/right) - built for water
- **Mirelurk King:** 7 swim anims (idle, walk/run forward, turns, strafe) - most aquatic creature

### No Diving
No dedicated diving/underwater animations found. Swimming is surface-only.

---

## 9. Grafton Monster (FO76's "Bigfoot")

**68 animations** - the Grafton Monster serves as FO76's Appalachian cryptid equivalent to Bigfoot.

### Movement
- Walk forward/backward, run forward, sprint forward
- Turn set (15, 90, 180 degrees both directions)

### Combat
- `attackgroundpound` - area-of-effect stomp
- `attackoilbombthrow` - throws toxic oil bombs
- `attackoilbombsalvo` - rapid-fire oil bomb volley
- `attackoilbombsalvo_double` - double salvo variant
- `attackfromrun` / `attackfromrunearly` / `attackfromrunmid` / `attackfromrunlate` - charging attacks at different ranges
- `attackstandinghammerfist` / `attackforwardhammerfist` - fist slams
- `attackforwardsweepinghammerfist` - sweeping slam
- `attacksweepright` / `attacksweepleft` - wide swipes

### Special
- `ambushwater/ambush` - **emerges from water** (waterline ambush)
- `injuredenter` / `injuredexit` - injury state with dedicated injured combat variants
- `criticalhit_blowholes` - critical hit to its blowholes (unique weak point)
- `mtidle_warn` - warning idle before aggression
- `mtidle_flavor01` / `mtidle_flavor02` - passive idle variants

### Injured State
Full injured combat variant with reduced animations:
- Injured attacks (hammer fist, sweeping, sweep right)
- Injured walk/turn
- Injured idle

---

## 10. Cut Content References

### Stormboss (Tempest/Milepost Zero Boss)
**56 animations** - fully animated boss creature with unique mechanics:

- `calldownlightning` - **summons lightning strikes**
- `chargedstomp` - electrically-charged ground pound
- `coilgunautofirenonadd` / `coilgunidle` - **built-in coil gun weapon**
- `leftarmautofireenter` / `leftarmautofireloop` - left arm automatic weapon
- `leftarmsinglefire` - left arm single shot
- `meleekick` / `meleelungeforward` / `meleerushstomp` - melee combo
- `meleeswipebackward` / `meleeswipeforward` / `meleeswipeleft` / `meleeswiperight` - directional swipes
- `powerattackrange` - ranged power attack
- `stunned` / `stunnedstart` / `stunnedloop` / `stunnedexit` - stun mechanic (player can stun it)
- `ambush/fabricator/ambush` - **emerges from a fabricator machine**
- Full death, dodge, stagger, hit reaction sets

The Stormboss is a humanoid(?) boss with both a coil gun arm weapon AND the ability to call down lightning. The "fabricator" ambush suggests it's a manufactured/robotic entity. This is tied to the "Tempest" / "Milepost Zero" content that has been datamined.

### Storm-Prefixed Furniture (Milepost Zero)
Multiple furniture animations suggesting Milepost Zero quest content:
- `storm_coma` - NPC in a coma (enter/exit/idle)
- `storm_imposingsitatdesk` - important NPC sitting imposingly (7 directional enter/exit variants - high-priority NPC)
- `storm_layoutblueprint` - NPC laying out blueprints
- `storm_losttube` - NPC examining a "lost tube"
- `storm_telescope` - NPC using telescope
- `stormcaravanhqbook` - reading at Caravan HQ
- `stormtrapbook` - reading a trap book
- `stormelectricchair` - **electric chair** furniture

### Meltdown Weapon
Unique weapon with `wpnoverload` mechanic (see Section 6). Not matching any currently shipped weapon.

### Wanamingo
Classic Fallout 2 creature with skeleton data but zero animations. Either planned and abandoned, or animations are in a future update archive.

### Radhog
Skeleton + full behavior tree (core, root, ambush, furniture) but **zero animations**. The behavior framework is built and waiting for animation work. This creature is likely planned for a future update.

---

## 11. Emote/Social Animations

### Emotes (63 unique, most with male + female variants + power armor mirrors)

**Faction Salutes:** Standard, Communist, Free State, Raider, BOS, Flyboy
**S.P.E.C.I.A.L.:** Strength, Perception, Endurance, Charisma, Intelligence, Agility, Luck
**Social:** Wave, Follow, Confused, Frown, Heart, Thumbs Up/Down, Startled, Finger Guns
**Activities:** Camp, Cooking, Hungry, Thirsty, Radiated, Looking to Buy, Gift, Lunch Box
**Performance:** Grognak Yell, Grelok Yell, Protectron Shuffle, Rifle Drill, Laughing
**Mothman:** Funky Mothman (dance), Mothman Worship, Vengeful Mothman
**Special:** Mind Blown, So Sorry, No Mic, Not Thank You, Watching You, Nice Camp
**Seasonal:** Alien Flag, Hills Are Alive, Into the Shadows, Juggling, Wolf Howl
**Recent:** Alistair Triumphant, Coin Flip 25th, Military Halt, Rage, Roman Candle, Popcorn Eating, Reveille Wakeup, Wait for Me, Once Again

### Photo Mode Poses (52 unique, all with PA mirrors)
50s Dance, Air Guitar, Bowling Strike (2), Cannonball, Champ, Chic, Clean Sweep, Confetti, Confidence, Couples Pose (2), Deep Thoughts, Doctor Zorbo (2), Femme Fatale, Fighting Stance, Flag Wave, Flashlight, Gap Jump, Greaser, Gunslinger, Hands on Hips, Heart, Heroic, Hot Dog Roast, Kneel, Lightning Rod, Looking to the Future, Lotus, Lying Out, Mid-Air Jump (2), Military (+ Huddle x3), Mothman Found, No Evil (Hear/Say/See), Nuclear Glare, Paparazzi Ready, Peace, Pip-Boy, Point into the Sky, Presenter, Quick Draw, Rifle Across Shoulders, Salute, Science Guy, Sharpshooter, Showcase, Sitting, Skiing (3), Sparklers, Swan Dive, The Dancer, Thinking, Tough Girl/Guy, Tree Pose, Two Thumbs Up, Uncle Sam, Vault 94/96, Vault Boy, Victory (+ Squared), Walking, Wave, Wings, Wolverine

---

## 12. Trailer/Promotional Animations

**152 animations** from pre-launch and promotional materials still in the archive:

- **Vault Party Intro:** 14 party animations (dancing, socializing in vault)
- **Vault Picnic:** 6 picnic scenes + 6 nuke-reaction variants
- **Vault Door:** 9 vault door exit sequences
- **Vault Exit:** 10 exterior emergence scenes + 5 standing + 5 seated
- **Training Seats:** 13 training/orientation animations
- **Intro Workers:** 6 vault workers
- **Intro Room Pip-Boy:** 2 pip-boy examination scenes
- **Intro Standee:** 2 cardboard standee interactions
- **Vault Exit Anchor:** 1 anchor shot exterior
- **Trailer Hugs:** 2 hug animations (player hugging)

These are bespoke animations created for the E3 2018 / launch trailers that were never cleaned out.

---

## 13. Notable Furniture Interactions

### Interesting/Unusual Furniture Types
- `coverkneelrightambush` - **cover system kneeling ambush** (furniture-based cover)
- `uforide` - UFO ride CAMP item
- `atx_zetan_stasischamber` - Zetan alien stasis chamber
- `atx_ironmaiden` - Iron Maiden furniture
- `atx_torturerack` - Torture rack
- `autodoc` - Auto-Doc medical station
- `76trailerhug01/02` - Hugging animations from trailer
- `atx_alieninvasion_shootinggallery` - Alien shooting gallery
- `stormelectricchair` - Electric chair (Milepost Zero)
- `raraventhighexit` / `raraventitemdrop` / `raraventlowsidewaysenter/exit/idle` - **Ra-Ra vent crawling** (Wastelanders child NPC crawling through vents)
- `veraciocruz_idle` - Named NPC idle (quest character)
- `kentheadbuttssinjin` - **Kent headbutts Sinjin** (FO4 Silver Shroud quest - still in data)
- `dimachair` / `dimaexecution` - **DiMA's chair and execution** (Far Harbor content still present)
- `atx_therapeuticsauna` / `atx_thehottub` / `atx_outdoor_shower` - Spa furniture
- `atx_bowlingalley` - Full bowling alley
- `wstgoldpanning` - Gold panning at water

---

## 14. Summary of Key Findings

### Confirmed Cut Systems
1. **Cover-Based Combat** - 284 production-quality animations across 5 actor types. The most complete cut system in the archive.
2. **Stormboss** - Fully animated boss for upcoming/cut Tempest content. Coil gun arm + lightning summoning.
3. **Radhog** - Behavior tree built, zero animations. In development.
4. **Wanamingo** - Skeleton only. Fallout 2 nostalgia creature planned then shelved.
5. **Meltdown weapon overload** - Unique weapon mechanic with no current in-game match.

### Creatures by Animation Complexity (Excluding Humans)
1. Super Mutant (735) - most animated non-player actor
2. Scorched (725) - nearly tied
3. Dogmeat (429) - FO4 companion legacy
4. Mole Miner (298) - cover system contributor
5. Feral Ghoul (167) - multiple ambush variants
6. Mirelurk King (129) - best swimmer
7. Deathclaw (115) - car flipper
8. Wendigo (105) - more complex than expected
9. Sheepsquatch (104) - unique quill/kick attacks
10. Mothman (103) - teleportation + curse + blessing

### Cryptid Highlight Reel
- **Mothman:** Teleports, curses enemies, blesses allies, has damaged-wing combat modes
- **Flatwoods Monster:** Teleports, heals self, has charge attacks, dazed state
- **Grafton Monster:** Water ambush, oil bomb salvos, blowhole weak point
- **Sheepsquatch:** Quill projectiles, back kicks, lunge combos
- **Wendigo Colossus:** Three-headed attacks (fear, summon, fire), multi-head critical hits
- **Jersey Devil:** Sinister gaze attack, AOE roar, tail spin, bleed-out escape mechanic
- **Snallygaster:** Eye glow FX, full behavior set

### No Bigfoot
There is no "Bigfoot" or "Sasquatch" actor in the animation archive. The Grafton Monster is the closest Appalachian cryptid analog. If a Bigfoot exists in FO76, its animations would need to be in a patch/update archive, not the base game.
