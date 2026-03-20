# FO76 Update Archive Analysis (Updates 10, 11, 12)

**Date:** 2026-03-20
**Source:** BA2 dry-run listings of SeventySix - {10,11,12}Update{Main,Voices}.ba2
**Archive Location:** /home/deucebucket/.steam/steam/steamapps/common/Fallout76/Data/

## Archive Summary

| Archive | Type | File Count | Notes |
|---------|------|-----------|-------|
| 10UpdateMain | GNRL | 11,322 | Largest Main archive |
| 10UpdateVoices | GNRL | 9,527 | Largest Voice archive (4,882 .fuz) |
| 11UpdateMain | GNRL | 8,286 | Mid-size |
| 11UpdateVoices | GNRL | 3,405 | Mid-size (2,233 .fuz) |
| 12UpdateMain | GNRL | 8,040 | Newest, "The Backwoods" patch |
| 12UpdateVoices | GNRL | 2,315 | Smallest voice archive (1,159 .fuz) |

Update 10 has the most content overall, suggesting it was a major content dump. Updates 11 and 12 are more targeted, with progressive trimming of voice files (likely moving older voices to earlier archives).

---

## MAJOR FINDING: Bigfoot / Sasquatch Creature

**First appearance: Update 12 only (not in 10 or 11)**

A full Bigfoot creature has been added under the Super Mutant Behemoth actor class:

```
meshes/actors/supermutantbehemoth/bigfoot/characterassets/bigfootdespawnexplosion.nif (38,920 bytes)
meshes/actors/supermutantbehemoth/bigfoot/characterassets/bigfootdespawnvfx.nif (37,975 bytes)
meshes/actors/supermutantbehemoth/bigfoot/characterassets/bigfootintroexplosion.nif (35,795 bytes)
meshes/actors/supermutantbehemoth/bigfoot/characterassets/projectiletick.nif (121,130 bytes)
meshes/actors/supermutantbehemoth/bigfoot/characterassets/skeleton.nif (72,978 bytes)
meshes/actors/supermutantbehemoth/bigfoot/characterassets/supermutantbehemoth_bigfoot.nif (710,170 bytes)
```

Additional Bigfoot collectible:
```
meshes/atx/setdressing/atx_displaycase_beersteins_bigfoot/atx_displaycase_beersteins_bigfoot.nif
```

Also new in Update 12 under supermutantbehemoth:
```
meshes/actors/supermutantbehemoth/treebat.nif
```

**Analysis:** Bigfoot uses the Behemoth skeleton (large biped), has intro/despawn VFX (event boss pattern), and throws projectile ticks. This is a fully-realized cryptid creature -- likely "The Backwoods" update content or a future seasonal boss. The Bigfoot beer stein display case suggests an ATX collectible to accompany the creature's introduction. The "treebat" mesh may be a weapon used by Bigfoot (behemoth-scale club).

---

## New Weapons & Combat Systems

### Nitro Rifle (Update 11 exclusive -- removed from 12)
Full animation set for a new weapon type called "nitrorifle":
- First-person: jiggle, fire auto, fire single, sighted, jump, pitch, turn animations
- Power Armor: assembly pose, bolt charge, fire, reload animations
- 16+ animation files total

This weapon appeared in Update 11 but was NOT carried forward to Update 12, suggesting it was either:
- Pulled back for further development
- Renamed and shipped under a different name
- Cut content

### Shoulder-Mounted Weapon (Update 12)
```
meshes/actors/character/_1stperson/behaviors/shouldermounted_gunwrappingbehavior.hkx
meshes/actors/character/behaviors/shouldermountedgunwrappingbehavior.hkx
```
New weapon grip/behavior type -- a shoulder-mounted weapon (rocket launcher? minigun variant?).

### BOS Launcher (Update 12)
```
meshes/actors/character/_1stperson/behaviors/boslauncher_gunwrappingbehavior.hkx
meshes/actors/character/behaviors/boslauncherwrappingbehavior.hkx
```
Brotherhood of Steel branded launcher weapon.

### Cover System Animations (Update 11 exclusive)
Extensive cover-based combat animations under `griprifleshort/`:
- Standing cover idle, sighted, shuffle, enter/exit transitions
- Crouching cover transitions, kneeling cover
- Blind fire (auto and single)
- Grenade throw from cover
- 30+ animation files

These were in Update 11 but NOT in Update 12, suggesting a cover system was prototyped and either shelved or will ship later.

### 10mm SMG Animations (Update 11)
```
meshes/actors/character/animations/weapon/10mmsmg/wpnfiresinglereadyslave.hkx
```
Possible new 10mm submachine gun variant.

---

## New Power Armor Skins (ATX / Atomic Shop)

### Update 10: Edison PA
Full PA skin set (helmet, arms, legs, torso + headlamps in 6 colors + VFX).

### Update 11: 65 PA + Lady Liberty PA
- **65 PA:** Full set -- possibly referencing Route 65 or a year theme
- **Lady Liberty PA:** Full set with custom jetpack, VFX, and 42 voice lines from "atx_ladylibertyvoice" (a talking PA skin)

### Update 12: Armed PA
Full PA skin set named "Armed" -- military/weapons themed.

---

## New NPCs by Update

### Voices Added in Update 11 (not in Update 10)

| NPC | Category | Voice Lines | Notes |
|-----|----------|-------------|-------|
| atx_ladylibertyvoice | ATX | 42 | Talking PA skin, massive voice set |
| atx_npcm_comp_lite_joeybello | ATX Companion | 2 | New C.A.M.P. lite companion |
| atx_npcm_comp_lite_lawson | ATX Companion | 2 | New C.A.M.P. lite companion |
| atx_npcm_comp_lite_mechanic | ATX Companion | 2 | New C.A.M.P. lite companion |
| bs01_npcf_dagger | Brotherhood | 2 | Dagger faction leader voice |
| bs01_npcm_pierce | Brotherhood | 2 | Brotherhood NPC |
| npcm_ghl00_maddoxmullen | Ghoulish | 4 | New ghoul NPC |
| npcm_ghl00_quest_asher | Ghoulish | 6 | Quest NPC (most lines) |
| npcm_ghl00_quest_leamonprice | Ghoulish | 2 | Quest NPC |
| nwot_npcf_bettyhill | Nuka-World | 2 | New NW on Tour NPC |
| nwot_npcf_pat | Nuka-World | 2 | New NW on Tour NPC |
| nwot_npcm_gunther | Nuka-World | 2 | New NW on Tour NPC |
| sse_npcf_susan | Seasonal Event | 2 | New seasonal NPC |
| storm_npcf_margaret | Stormchaser | 2 | New storm content NPC |
| storm_npcm_blair | Stormchaser | 2 | New storm content NPC |
| w05_npcf_fridamadani | Wastelanders | 2 | New W05 NPC |
| w05_npcf_juliette | Wastelanders | 2 | New W05 NPC |
| w05_npcf_spymochou | Wastelanders | 4 | "Spy Mochou" -- espionage? |
| xpd_ac_npcf_anna | Expedition AC | 2 | New Atlantic City NPC |
| xpd_ac_npcf_surly | Expedition AC | 2 | New Atlantic City NPC |
| xpd_npcf_esme | Expedition | 2 | New expedition NPC |
| fishing_npcm_thecaptain | Fishing | 2 | Fishing system NPC |
| fish_npcm_fisherman | Fishing | 2 | Fishing system NPC |
| femalechild / malechild | Generic | -- | Child voice types added |

### Voices Added in Update 12 (not in Update 11)

| NPC | Category | Voice Lines | Notes |
|-----|----------|-------------|-------|
| bs01_npcf_gloriachance | Brotherhood | 2 | New BoS NPC |
| bs01_npcm_georgeputnam | Brotherhood | 2 | Related to Carol/Marty Putnam |
| bs01_npcm_tadchance | Brotherhood | 2 | Related to Gloria Chance |
| bs02_npcf_cassiehalloway | Brotherhood 2 | 2 | New BoS NPC |
| bs02_npcf_vault96prisoner_01 | Brotherhood 2 | 2 | Vault 96 content |
| atx_npcf_comp_lite_inspector | ATX Companion | 2 | New lite companion: Inspector |
| atx_npcf_comp_lite_astronomer | ATX Companion | 2 | Returned from U10 |
| burn_npcf_magpie | Burning | 2 | Returned from U10 |
| burn_npcm_eugene | Burning | 2 | Returned from U10 |
| burn_npcm_exec | Burning | 2 | Returned from U10 |
| burn_npcm_moose | Burning | 2 | Returned from U10 |
| npcm_fs_eddie | FS (new prefix) | 3 | New content line "fs_" |
| storm_npcf_scarlet | Stormchaser | 2 | New storm NPC |
| storm_npcm_craig | Stormchaser | 2 | New storm NPC |
| storm_npcm_laurence | Stormchaser | 2 | Returned from U10 |
| w05_npcf_heatherellis | Wastelanders | 2 | New NPC |
| w05_npcm_colecarver | Wastelanders | 2 | New NPC |
| w05_npcm_jide_wayward | Wastelanders | 2 | New Wayward NPC |
| w05_npcm_joecreigh | Wastelanders | 2 | New NPC |
| w05_npcm_comp_lite_raiderpunk | Companion | 2 | Raider Punk as lite companion |
| mile_npcf_importedgoodsmerchant | Milestone | 2 | New merchant type |
| u04_npcf_v94_pastorgabriellasalavar | Vault 94 | 2 | Vault 94 pastor NPC |
| xpd_ac_npcm_quentinolombardi | Expedition AC | 2 | Quentino's club owner? |
| xpd_ac_npcm_mobdenier | Expedition AC | 2 | "Mob Denier" -- AC mafia content |
| xpd_npcf_orlando | Expedition | 2 | New expedition NPC |
| xpd_npcm_wicker | Expedition | 2 | Returned from U10 |

### Voice NPC Prefix Guide
- **atx_** = Atomic Shop / premium content
- **bs01_/bs02_** = Brotherhood of Steel season 1/2
- **burn_** = Milepost Zero / Burning content (highway town)
- **storm_** = Stormchaser content (Darkwood Manor area)
- **moon_** = Blue Moon (Moonshine Jamboree area)
- **nwot_** = Nuka-World on Tour
- **xpd_** = Expeditions (xpd_ac_ = Atlantic City)
- **w05_** = Wastelanders (base NPC pool)
- **npe_** = New Player Experience
- **ghl00_** = Ghoulish content line
- **mile_** = Milestone merchants
- **fs_** = Unknown new content line (only "Eddie")
- **sse_** = Seasonal event
- **u02_/u04_/u06_** = Nuclear Winter era updates

---

## Notable Voice Trends

### Growing Voice Sets (U10 to U12)
NPCs getting significantly MORE voice lines across updates:
- **crscorchedfemale:** 11 -> 25 (+14 lines) -- Scorched getting more dialogue
- **storm_npcf_genericlost01:** 2 -> 13 (+11) -- "The Lost" faction expanding
- **xpd_npcm_genericunion02:** 5 -> 15 (+10) -- Union faction expanding
- **robotprotectron:** 20 -> 28 (+8) -- More Protectron bark lines
- **xpd_npcf_genericunion01:** 7 -> 14 (+7) -- Union expanding
- **xpd_npcf_genericunionghoul03:** 9 -> 15 (+6) -- Ghoulified Union members

### Large Voice Removals (U10 to U11)
Many "burn_" NPCs removed between U10 and U11 -- these Milepost Zero/Highway Town characters were likely migrated to an earlier archive:
- 40+ burn_ NPCs removed including: director, doctore, enclaveofficer, janitor1/2, julius, kerry, mac, martinfinch, millstone, moses, narrator, professormetter, rattler, ronny, runt, rustking, terry, tony, wilbur
- This suggests the Milepost Zero expedition had its voices consolidated elsewhere

---

## New Atomic Shop Content (ATX)

### Update 12 (New)
- **Armed PA skin** -- Full power armor set
- **Evidence Collection Protectron** -- New collectron skin (detective/forensics themed)
- **Atomic Roller Machine** -- Interactive furniture with sit animations
- **Porch Swing (atx_pswing)** -- New C.A.M.P. furniture
- **Framed Housing Kit** -- Complete building set with destroyed variants and tarped roofs
- **Alien-themed boxes** -- Ammo, aid, and scrap boxes in alien style
- **Alien warning signs** -- cow, grey, hitchhikers variants
- **Alien display case** -- for collected alien items
- **Quentino's Saxophone** -- decorative item from AC nightclub
- **Atomic Blast Lamp** -- new lighting item
- **Mobile Home/Trailer door** -- new prefab structure
- **Prospector Saloon Shelter** -- new shelter with large/small doors
- **Lumberjack Collectron legs** -- new collectron variant parts
- **Bigfoot Beer Stein display case**
- **Fishing bobbers** -- Atomic Swimmer, grenade, lightbulb, Eye of Ra, UFO bobbers
- **UFO bobber** -- animated variant for fishing

### Update 11 (New)
- **65 PA skin** -- Full power armor set
- **Lady Liberty PA** -- Full PA set with talking voice (42 lines!)
- **Saloon Booth** -- Interactive furniture with walk-in animations
- **Saloon Bar** -- Corner, counter, and regular bar pieces
- **Saloon Doors** -- Swinging saloon door
- **Saloon Lights** -- Ceiling and wall variants
- **Prospector Saloon Shelter** -- Same as in U12

### Update 10
- **Edison PA** -- Full power armor set with color-coded VFX
- **Dr. Bones mannequin** -- Skeleton mannequin (body, hands, head)
- **Red Rocket Robot/Sales Bot**
- **Toxic Bob Collectron** -- with VFX
- **Fire Watch Tower** -- with explosion effect
- **Various doors** -- accordion, alien laser, BoS, bulkhead
- **Zetan Stasis Chamber** -- furniture with animation

---

## New C.A.M.P. Companions (Lite)

Full companion roster across all 3 updates:
- **Astronomer** (female) -- in U10 and U12
- **Dottie** (female) -- in all 3
- **Grandma Junko** (female) -- in U10 and U11
- **Inspector** (female) -- new in U12
- **Ghoul** (male) -- in all 3
- **Scarberry** (male) -- in all 3
- **Super Mutant** (male) -- in all 3
- **Joey Bello** (male) -- new in U11
- **Lawson** (male) -- in U11 and U12
- **Mechanic** (male) -- in U11 and U12
- **Raider Punk** (male, lite) -- new in U12 (existing full companion getting lite version)

---

## Expedition Content (Atlantic City)

### New in Update 12
- **Quentino Lombardi** (NPC) -- likely the nightclub owner
- **Mob Denier** (NPC) -- someone denying mafia connections
- **Quentino's Club signs** -- 2 workshop sign variants + saxophone decoration
- **Nightclub exterior sign** -- workshop buildable
- **Aquarium pillar** (VFX) -- decorative/environmental
- **Orlando** (female NPC) -- new expedition character
- **Mob content expansion** -- mobster03 added, existing mobdenier

### New in Update 11
- **Anna** (female NPC) -- new AC civilian
- **Surly** (female NPC) -- new AC character

### Existing AC Content
Both updates maintain the full AC cast: Russo family (Abbie, Evelyn, Antonio, Vin), Billy Belt Buckles, Buttercup, Fabio, Juchi, Little Rob, Mayor Tim, Concerta, Sloane Cao, Stratton, Jullian, Mother Charlotte, etc.

---

## Storm / Darkwood Content

### Update 12 New
- **Darkwood Manor snowglobe** -- collectible
- **Secret brick door** (storm_dkwd_interior_bricksecretdoor) -- hidden passage
- **Scarlet** (new NPC)
- **Craig** (new NPC)
- **Serum extraction machine** -- ties to mutations/serums
- **Lost-in-a-tube** mesh -- "The Lost" faction members in containment
- **Boss fabricator** -- ambush event boss spawner
- **Boss charge VFX** -- storm boss attack effects
- **Bomb book** (storm_trapbook01) -- booby-trapped book
- **Severed arm hand scanner** -- gruesome security device
- **Ranger stash box** -- new container type
- **Specimen jar** -- collectible/decoration
- **Slumber Mill Motel sign** -- animated location sign
- **Lightning tile hazards** -- 12+ hazard variations + mirrored variants

### Storm Boss System
The storm boss has a full VFX/effect pipeline:
- Charge marker VFX + charge VFX
- Flare effects
- Storm system weather effects
- Lightning tile hazards (extensive set of variations)
- Laser grid barriers (multiple sync patterns)

---

## Guardian Bot (CreateABot)

New in Update 12 -- a "Guardian Bot" type for the CreateABot system:
```
meshes/actors/createabot/guardianbot/guardianbotbase.nif
meshes/actors/createabot/guardianbot/guardianbotdoors01.nif
meshes/actors/createabot/guardianbot/torsoguardianbot.nif
meshes/effects/electricfloorparticles_guardianbot.nif
meshes/effects/electricfloor_guardianbot.nif
meshes/effects/energycannonexplosion_guardianbot.nif
meshes/effects/guardianbot_large_explosion.nif
```

This appears to be a new enemy robot type or a buildable CAMP defense robot with electric floor attacks and an energy cannon.

---

## Cryptid Mobile (Blue Moon)

```
meshes/bluemoon/setdressing/moon_cryptid_mobile/moon_cryptid_mobile.nif
```

A cryptid-themed hanging mobile decoration, likely for the Blue Moon / Moonshine Jamboree area. Could be baby-room themed or a bar decoration featuring local cryptids.

---

## Content Lifecycle Observations

### Content that appeared then disappeared:
1. **Nitro Rifle** -- Full animation set in U11, completely absent from U12
2. **Cover system** -- 30+ cover combat animations in U11, gone in U12
3. **Cupid's Arrow emote** -- In U11 (Valentine's seasonal?), gone from U12
4. **Lady Liberty voice** -- 42 voice lines in U11, removed from U12 (likely shipped and consolidated)
5. **mile_npcf_cryptidhunter** -- In U10, removed from U11/12 (cryptid hunter NPC)

### Content that returned:
1. **Astronomer companion** -- In U10, missing from U11, back in U12
2. **Multiple burn_ NPCs** -- Removed in U11, some returned in U12
3. **storm_npcm_laurence** -- In U10, missing from U11, back in U12
4. **xpd_npcm_wicker** -- In U10, missing from U11, back in U12

### Steady growth areas:
- Union faction generic NPCs getting more voice lines each update
- "The Lost" faction (storm_) expanding
- Scorched getting more dialogue variety
- Brotherhood content continuing to expand

---

## Unreleased / Upcoming Content Indicators

### High Confidence (assets are complete)
1. **Bigfoot cryptid** -- Full creature model, skeleton, intro/despawn VFX, projectile attack, beer stein collectible. Only in U12.
2. **Guardian Bot** -- Full enemy/buildable with electric floor attacks and energy cannon
3. **Framed Housing Kit** -- Complete building set with destroyed variants
4. **Evidence Collection Protectron** -- New ATX collectron
5. **Armed PA skin** -- Complete power armor set
6. **Inspector companion** -- New lite C.A.M.P. ally
7. **Quentino's Club expansion** -- Signs, saxophone, NPC owner

### Medium Confidence (partial assets)
1. **Shoulder-mounted weapon** -- Behavior files only, may need more work
2. **BOS Launcher** -- Behavior files only
3. **npcm_fs_eddie** -- New content prefix "fs_" with 3 voice lines, purpose unknown
4. **Darkwood Manor secret door** -- Hidden passage suggests exploration content
5. **Serum extraction machine** -- New mutation/serum content

### Lower Confidence (may be cut)
1. **Nitro Rifle** -- Appeared in U11, removed from U12 (possibly cut or renamed)
2. **Cover system** -- Extensive animations in U11, removed from U12 (ambitious feature, possibly deferred)
3. **Cryptid Hunter NPC** -- Present in U10, absent since (may have been renamed or folded into another NPC)

---

## File Extension Distribution

| Extension | U10 | U11 | U12 |
|-----------|-----|-----|-----|
| .nif (meshes) | 6,625 | 4,630 | 4,691 |
| .txt (animdata) | 3,649 | 3,412 | 3,279 |
| .hkx (havok anim) | 985 | 240 | 70 |
| .ssf (sound) | 58 | 4 | 0 |
| .tri (morph) | 2 | 0 | 0 |

The dramatic drop in .hkx files from U10 (985) to U12 (70) and .ssf files (58 to 0) suggests animation and sound descriptor consolidation into earlier archives.

---

## Key Takeaways

1. **Bigfoot is coming** -- The most significant unreleased cryptid find. Full creature model with event boss VFX, built on the Behemoth skeleton. This is clearly tied to "The Backwoods" content.

2. **A cover system was prototyped** -- 30+ animations for cover-based combat appeared in U11 and were removed. This would be a massive gameplay change if it ships.

3. **The Nitro Rifle was prototyped** -- Complete weapon animations existed in U11 but were pulled. Could return under a different name.

4. **Atlantic City is still expanding** -- Quentino's Club, new NPCs like the "Mob Denier," and ongoing faction content suggests more AC expeditions are coming.

5. **Darkwood Manor has secrets** -- Secret doors, bomb traps, specimen jars, and a serum machine suggest a deeper dungeon/quest area.

6. **Guardian Bot is a new enemy/ally type** -- Electric floor attacks and energy cannons make this either a formidable CAMP defense or a new dungeon enemy.

7. **The Atomic Shop pipeline is full** -- Armed PA, Evidence Collection Protectron, Inspector companion, Framed Housing Kit, Atomic Roller Machine, and Prospector Saloon shelter are all ready to sell.
