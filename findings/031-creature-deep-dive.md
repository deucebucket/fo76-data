# FO76 Creature Deep Dive: ESM Records, Scripts, and Hidden Mechanics

**Date:** 2026-03-20
**Source:** RACE_records.txt (156 races), NPC__records.txt (26,615 lines), WEAP_records.txt, decompiled scripts
**Method:** Cross-referencing ESM race records, NPC entries, creature weapon definitions, and decompiled Papyrus scripts

---

## 1. Complete Creature Race Registry (156 Races)

### Standard Combat Creatures (36)
| Race | ID | Skeleton |
|------|-----|----------|
| DeathclawRace | 0x0001DB4A | deathclawproject.hkx |
| ScorchBeastRace | 0x00019D95 | scorchbeastproject.hkx |
| WendigoRace | 0x0001554D | wendigoproject.hkx |
| WendigoColossusRace | 0x00547992 | wendigocolossusproject.hkx |
| MothmanRace | 0x0000D233 | (uses human models) |
| SheepsquatchRace | 0x00479D50 | (uses human models) |
| GraftonMonsterRace | 0x0000E889 | (uses human models) |
| FlatwoodsMonsterRace | 0x00110E0A | flatwoodsmonsterproject.hkx |
| SnallyGasterRace | 0x0000D191 | snallygasterproject.hkx |
| SuperMutantRace | 0x0001A009 | supermutantproject.hkx |
| SupermutantBehemothRace | 0x000BB7D9 | supemutantbehemoth.hkx |
| SupermutantBehemothBossRace | 0x005FF2FB | supemutantbehemoth.hkx |
| ShieldedSuperMutantRace | 0x005C4F6E | shieldedsupermutant.hkx |
| SuperMutantRustKingRace | 0x007EBA45 | supermutantproject.hkx |
| FeralGhoulRace | 0x0006B4EC | feralghoulproject.hkx |
| FeralGhoulGlowingRace | 0x000A96BF | feralghoulproject.hkx |
| MirelurkRace | 0x00023FFC | mirelurkproject.hkx |
| MirelurkHunterRace | 0x00064C60 | (uses human models) |
| MirelurkKingRace | 0x000B7F91 | (uses human models) |
| MirelurkQueenRace | 0x000E12A6 | (uses human models) |
| MirelurkSpawnRace | 0x004F60A7 | radroachproject.hkx |
| HoneyBeastRace | 0x0000E7D3 | (uses human models) |
| HoneyBeastBeeSwarmRace | 0x00388BD5 | dlc04_swarmproject.hkx |
| FloaterRace | 0x0055F6FA | floaterproject.hkx |
| ScorchedRace | 0x0010CA5F | (uses human models) |
| MegaSlothRace | 0x0013BA06 | megaslothproject.hkx |
| RadScorpionRace | 0x000636AB | radscorpionproject.hkx |
| RadToadRace | 0x00011B6A | radtoadproject.hkx |
| YaoGuaiRace | 0x000A0F2F | yaoguai.hkx |
| MoleMinerRace | 0x00012E6B | (uses human models) |
| FEVHoundRace | 0x00090C33 | fevhoundproject.hkx |
| AlienRace | 0x00184C4D | alienproject.hkx |
| MoleratRace | 0x0001D810 | moleratproject.hkx |
| StingwingRace | 0x0005FBB1 | (uses human models) |
| BloodbugRace | 0x0002456D | mosquitoproject.hkx |
| BloatflyRace | 0x00029463 | bloatflyproject.hkx |

### Expedition/DLC Creatures (15)
| Race | ID | Notes |
|------|-----|-------|
| TrogRace | 0x0063CC25 | The Pitt - has conditional keyword checks |
| DLC03_FogCrawlerRace | 0x00110A4E | fogcrawlerproject.hkx |
| DLC03_AnglerRace | 0x0011092F | (unique) |
| DLC03_GulperRace | 0x00110D23 | movement speed >= 420 condition |
| DLC03_GulperSmallRace | 0x00111655 | Same 420 speed condition |
| DLC03_HermitCrabRace | 0x00110B24 | hermitproject.hkx |
| DLC04_CaveCricketRace | 0x00112A18 | dlc04_cavecricket.hkx |
| DLC04_RadRatRace | 0x00112B95 | moleratproject.hkx |
| DLC04_SwarmRace | 0x00112AF6 | dlc04_swarmproject.hkx |
| OguaRace | 0x0068EC56 | Health <= 80% condition triggers shell |
| BlueDevilRace | 0x006A0649 | Uses deathclaw skeleton |
| XPD_JerseyDevilRace | 0x006C5D42 | jerseydevil.hkx |
| XPD_LesserDevilRace | 0x006FB703 | jerseydevil.hkx (smaller variant) |
| XPD_OvergrownElderRace | 0x006BCA2B | supermutantproject.hkx (plant mutants) |
| XPD_OvergrownPollinatorRace | 0x006B3A3E | floaterproject.hkx |
| XPD_OvergrownThornRace | 0x006B3A3F | feralghoulproject.hkx |

### Storm/Backwoods Content (6)
| Race | ID | Notes |
|------|-----|-------|
| StormBossRace | 0x006D65BB | Conditional spawning tied to global value |
| LostRace | 0x00727CCF | raiderproject.hkx - "The Lost" NPCs |
| LostFeralSuiciderRace | 0x0078BF08 | feralghoulproject.hkx |
| LostHealerRace | 0x0074D80B | raiderproject.hkx |
| P62_TheDrifterRace | 0x00802263 | raiderproject.hkx |
| ScorchtongueHeadRace | 0x00786D48 | scorchtongue.hkx |
| ScorchtongueBodyRace | 0x0079B8C2 | scorchtonguebody.hkx |
| ScorchtongueTailRace | 0x00787118 | scorchtonguetail.hkx |
| DustDevilRace | 0x00847624 | dustdevil.hkx |
| RadHogRace | 0x00822A4D | radhog.hkx |
| RadTurkeyRace | 0x00748739 | radturkey.hkx |
| RadPheasantRace | 0x0072EAA4 | radpheasantproject.hkx |
| BigfootRace | 0x00868BBC | supemutantbehemoth.hkx |

### Critter/Passive Races (13)
RadBeaverRace, RadSquirrelRace, OpossumRace, FoxRace, OwlRace, FrogRace, RadChickenRace, DLC03_RadRabbitRace, FireflyRace, CatRace, CatPetRace, BrahminRace, DLC04_BrahmiluffRace

---

## 2. CUT & DISABLED Creature Races

### Confirmed Cut (marked CUT_ or DEL_)

| Race | ID | What It Was |
|------|-----|-------------|
| **CUT_GorillaRace** | 0x000D9804 | Gorilla creature - has full keywords for beast/melee/combat. Uses human skeleton models. Had unique weapon `crUnarmedGorilla` (0x000ED6E4). **Never added to FO76.** Ported from FO4 Institute but never used. |
| **CUT_SuperMutantGhoulRace** | 0x0029565B | Super Mutant/Ghoul hybrid. Keywords include SuperMutant AND FeralGhoul markers. Would have been a unique crossover creature. |
| **CUT_DLC04DeathclawRaceQuantum** | 0x00112C58 | Quantum Deathclaw from Nuka-World. Ported from FO4 DLC but disabled. Uses deathclaw skeleton with unique keywords. |
| **CUT_DoNotUse_DLC03RoboBrainRace** | 0x00110FD9 | Robobrain variant explicitly marked "do not use." |
| **DEL_JerseyDevilRace** | 0x006B52AE | Early Jersey Devil using deathclaw skeleton - replaced by the jerseydevil.hkx version |
| **DEL_JerseyDevilRace001** | 0x006B3E24 | Second deleted Jersey Devil iteration |
| **DEL_zzzUltraciteAbominationRaceOLD** | 0x00641AE7 | Old Ultracite Titan implementation |
| **ZZZ_BossChickenRace** | 0x00636DDA | Boss Chicken! Uses radchicken skeleton but with boss-tier keywords (ActorTypeBoss, ActorTypeEpic). **A boss-level radchicken was prototyped and cut.** |
| **zzz_Test01Race** | 0x008975D5 | Uses cat skeleton (cat.hkx) - a test creature |
| **zzz_E09A_SentryRace** | 0x0065B8EA | Uses deathclaw skeleton with boss keywords - bizarre test combination |

### KEY FINDING: Boss Chicken
`ZZZ_BossChickenRace` (0x00636DDA) has an NPC entry `ZZZ_LvlBossChicken` (0x00636DD9), a dedicated skin `ZZZ_SkinBossChicken`, and a health curve `CT_Creatures_Health_BossChicken`. This was a fully implemented boss-tier radchicken with epic creature keywords. It was cut before release but the data is complete.

---

## 3. Creature Attack Weapons - Complete Registry

### Hidden Attack Types Most Players Don't Know About

**Deathclaw - GibTarget Function (deathclawracescript.psc):**
Deathclaws have a hidden `GibTarget()` function that **randomly dismembers players on a special kill animation.** When the "GibTarget" animation event fires, the script iterates through 6 body parts (Torso, Head, LeftLeg, RightLeg, LeftArm, RightArm). For each part, there's a 50% chance it gets affected, then a coin flip between explosion or dismemberment. This is why deathclaw kills sometimes look especially brutal - it's not just visual, it's procedural dismemberment.

The deathclaw also has an "Intimidate" animation event that places an AoE explosion at its feet - this is the fear roar mechanic.

**Scorchbeast - Tri-State Attack System (scorchbeastracescript.psc):**
The scorchbeast has three distinct combat states with different cooldown timers:
- **Flying:** Uses SonicAttackWeapon and StrafeAttackWeapon with flying-specific cooldowns
- **Ground:** Different sonic attack cooldowns (shorter than flying)
- **Interior:** Yet another set of cooldown ranges (tuned for enclosed spaces)

Each state independently manages which weapon slots are enabled/disabled via `SetEquippedWeaponAttacksEnabled`. The sonic attack is on equip slot 2, strafe on slot 3.

The queen has a completely separate AttackData struct with its own weapons and timing.

**Scorchbeast Queen-Specific Weapons:**
- `crScorchbeastQueenSonicAttack` (0x0052EEF8)
- `crScorchbeastQueenStrafeAttack` (0x0052EEF9)
- These are distinct from the regular scorchbeast versions

**Mothman - Three Behavior Modes:**
1. **Watcher** (`MothmanWatcherScript`): Stands and watches. Disappears if combat target gets within `RangeToDisappear`. Also disappears at sunrise (6:00 AM game time).
2. **Combatant** (`MothmanCombatantScript`): Has AoE attack weapon with initial delay and subsequent cooldown. Uses teleport explosions. Also disappears at sunrise.
3. **Defender** (`MothmanDefenderScript`): Starts as Watcher, transitions to combat when target enters `RangeToGoIntoCombat`. Has BOTH time-based and health-based disappear triggers (`DisappearHealthPercent`).

**Mothman Invisibility (MothmanInvisibilityEffect):**
When the Mothman uses its invisibility attack, it literally becomes a **ghost** - `SetGhost(True)` makes it completely immune to damage AND `SetAlpha(0.0)` makes it fully invisible. It stays this way for a random duration between `InvisibilityTimeMin` and `InvisibilityTimeMax`. This means there's a window during Mothman fights where it's literally unhittable.

**Wendigo Colossus - Dual Vomit System (wendigocolossusracescript.psc):**
The Colossus has TWO separate vomit attacks that come from different heads:
- **Rad Vomit**: Launches from `jnt_R_head` (right head) with configurable angle, distance, and variation
- **Poison Vomit**: Launches from `jnt_L_head` (left head) with its own angle/distance parameters

It also has a **combat style switching system** that alternates between melee-focused and range-focused combat styles on a timer (`CombatStyleSwitchTimeMin` to `CombatStyleSwitchTimeMax`). The `isNextStyleMelee` boolean toggles between them.

**Wendigo Colossus - Ally Summoning Mechanics:**
- Maintains between `MinNumberOfAllies` (2) and `MaxNumberOfAllies` (4) wendigo allies
- Summons more only when alive count drops below minimum
- Timer-based (`SummonAlliesTime` between summons)
- Requires `CanSummonAlliesKeyword` - can be removed to disable this ability
- The Colossus is explicitly `EpicCreatureDisallowed` - it can NEVER be legendary

**Sheepsquatch - Three-Stage Combat (sheepsquatchracescript.psc):**
The Sheepsquatch operates in three stages based on health thresholds:
- **Stage 1**: Default behavior
- **Stage 2**: Triggered at `HealthPercentageToStage2`
- **Stage 3**: Triggered at `HealthPercentageToStage3`

Each stage transition plays `SheepsquatchIdleStateChange` animation and swaps keywords (`Sheepsquatch_Stage1/2/3`), which likely changes available attacks or combat style.

**Grafton Monster - Oil Bomb Salvo (graftonracescript.psc):**
Has a multi-node salvo attack system launching from three back bubble nodes (`Grafton_BN_Def_BackBubble1/2/3`). Each fires sequentially with separate animation events. The salvo uses a projectile launch spell with configurable angle/distance variation. Has initial delay + cooldown timer.

**Ogua - Shell Mechanic (crOguaRaceScript.psc):**
When health drops below 80% (set on the race with `GetHealthPercentage <= 0.800000`), the Ogua enters its shell via `TurnInvulnerable` animation event. The shell:
- Heals the Ogua
- Can be triggered a limited number of times (`ShellLimit`, or infinite if -1)
- Is blocked by `crOguaBlockShellsKeyword`
- Tracks `timesShelled` counter

**RadHog - Howl Attack:**
`crRadHogHowlAttack` (0x00852EA3) uses a dummy weapon model but keywords suggest it's an AoE sonic-type attack with special ammo `crAmmoRadHogHowlAttack`.

**RadTurkey - Sonic Gobble:**
`crRadTurkeySonicGobble` (0x0075C201) - the radturkey has a sonic attack, not just melee.

**Megasloth - Sand Attack:**
`crMegaslothSandAttack` (0x007DB400) and `crMegaslothAreaAttack` (0x00521932E) - area denial attacks.

**Floater - Three Breath Types:**
- `crFloaterGnasherBite` (0x0055DA6E)
- `crFloaterFlamerBreath` (0x0055DA6B) - fire breath
- `crFloaterFreezerBreath` (0x0055DA67) - cryo breath

**Mirelurk King Sonic Attack:**
The `MirelurkKingSonicEffectScript` reveals the sonic attack **directly damages the target's PerceptionCondition** actor value. This means it doesn't just deal damage - it cripples your perception stat, reducing VATS accuracy and detection.

**Liberator - Volley Fire System (liberatorracescript.psc):**
Liberators fire in controlled volleys of `WeaponFireMaxShots`, then rest for `WeaponFireRestTime` seconds. This is why their laser fire comes in bursts.

---

## 4. Creature Weapons Used by Rust King Enemies (Backwoods/Burn Content)

**Burn/Abraxodyne Variant Attacks:**
- `Burn_crStingWingAbraxodyneSting` (0x00831C6F) - Abraxodyne chemical company modified stingwing
- `Burn_crRadScorpionAbraxodyneSting` (0x0082F44F) - Abraxodyne radscorpion variant
- `Burn_crRadScorpionBurningSting` (0x008270F7) - Fire-enhanced scorpion attack

These suggest the Abraxodyne company in the Backwoods/Burn update was experimenting on creatures, creating chemically-enhanced variants.

**Named Creature Weapons (Boss-Specific):**
- `cr44_Lawbringer` (0x008ADA17) - A .44 revolver used by a creature/NPC
- `cr10mm_CircuitBreaker` (0x00825CCD) - Named 10mm for a creature
- `cr44_MedicalMalpractice` (0x00820768) - Named .44 for a creature
- `crMeltdown` (0x00820767) - A unique meltdown weapon with extensive keywords
- `crE09A_Broadsider_GrandFinale` (0x00839C1C) - Named Broadsider for a creature event
- `crWarGlaive` (0x00833265) - War Glaive for creature use
- `crWarDrum` (0x0082447A) - War Drum for creature use
- `crGuitarSword` (0x00824479) - Guitar Sword for creature use
- `crTomahawk` (0x0082447D) - Thrown tomahawk for creatures
- `crThrowing_Knife` (0x00839C1D) - Thrown knife for creatures
- `crDynamiteBundleGrenade` (0x0082447C) - Dynamite bundle for creatures
- `crHalluciGenGrenade_Bounty` (0x00820766) - HalluciGen gas grenade for bounty creatures
- `crDLC04_FragGrenadeMIRV` (0x00820765) - MIRV grenade for creature use

---

## 5. The "Prime" Creature Variants - Disabled Event Content

### All Prime Specimens (Found with zzz_ prefix = disabled)

The Prime specimens were part of event `E02A` (Project Paradise / Arktos Pharma). Most have been disabled:

| Creature | Status | ID |
|----------|--------|-----|
| Deathclaw Prime | **zzz_ (disabled)** | 0x005C4F2D |
| Sheepsquatch Prime | **zzz_ (disabled)** | 0x005C4F24 |
| Yao Guai Prime | **zzz_ (disabled)** | 0x005C4F31 |
| Fog Crawler Prime | **zzz_ (disabled)** | 0x005C4F27 |
| Radscorpion Prime | **zzz_ (disabled)** | 0x005C4F2E |
| Honey Beast Prime | **zzz_ (disabled)** | 0x005C4F2B |
| Super Mutant Behemoth Prime | **zzz_ (disabled)** | 0x005C4F2A |
| Grafton Monster Prime | **zzz_ (disabled)** | 0x005C4F26 |
| Snallygaster Prime | **zzz_ (disabled)** | 0x005C4F28 |
| Radtoad Prime | **zzz_ (disabled)** | 0x005C4F25 |
| Cave Cricket Prime | **zzz_ (disabled)** | 0x005C4F23 |
| Gulper Prime | **zzz_ (disabled)** | 0x005C4F2C |
| Mirelurk Queen Prime | **zzz_ (disabled)** | 0x005C4F2F |
| Hermit Crab Prime | **zzz_ (disabled)** | 0x005C4F30 |
| Wolf Prime | **DEL_ (deleted)** | 0x005C4F29 |

### Still Active E02A Prime Specimens
Several E02A variants remain active, used in Project Paradise:
- `E02A_LvlGulper_Prime`, `E02A_LvlFogCrawler_Prime`, `E02A_LvlHoneyBeast_Prime`
- `E02A_LvlSMBehemoth_Prime`, `E02A_LvlRadtoad_Prime`, etc.

Some were also deleted: `DELETE_E02A_LvlMirelurkCrab_Prime`, `DELETE_E02A_LvlMolerat_Prime`, `DELETE_E02A_LvlMegasloth_Prime`

The zzz_ versions appear to be an older spawn system. The E02A_ versions are the active ones used in Project Paradise today.

---

## 6. The Epic (Legendary) Creature Spawn System

### The Formula (from EpicCreaturesScript)

**Epic Chance Calculation:**
```
Chance = (Base + (ActorLevel * ActorLevelMult)) * RegionMult
```
- `Base` = 1.0 (starting chance percentage)
- `ActorLevelMult` = 0.04 (each level adds 0.04%)
- `RegionMult` = varies by region (from `RegionChanceMultData`)
- `DefaultRegionMult` = 1.0
- `MaxChance` = 5.0 (capped at 5%)
- `MinActorLevel` = 10 (creatures below level 10 NEVER become legendary naturally)

**So a level 100 creature has: (1.0 + (100 * 0.04)) * RegionMult = 5.0 * RegionMult chance.**
This means legendary chance is capped at 5% base, modified only by region multipliers.

### Epic Rank System (5 Ranks = Star Levels)

Each rank has:
- `HealthMult` (default 1.25x per rank)
- `OutgoingDamageMult` (default 1.25x per rank)
- `HordeChance` (chance to spawn a horde on rank-up, d100)
- `NemesisHordeChance` (15% if also a Nemesis)
- `NemesisMinKillCount` (3 player kills to reach rank)
- Level range requirements (`MinLevelRequired` / `MaxLevelAllowed`)

### Rank Determination
Each rank has 5 creature chance globals (`Rank1CreatureChance` through `Rank5CreatureChance`). This creates a weighted probability table for what star level the legendary will be.

### Hidden Health Restore Mechanic
`AbEpicCreature_RestoreHealth_Trigger` is given to ALL epic creatures. When they hit 50% or less health, they heal to full and play the legendary "power up" animation. This is the "mutation" mechanic. The `EpicCreatureRestoreHealthEffectScript` handles this, removing the trigger ability after use (one-time heal).

### Minimum Health Floor
```
MinStartingHealth = 100
```
Even epic molerats get boosted to 100 HP minimum - "even epic Molerats need to take a couple bullets" (literal dev comment in the script).

### The Nemesis System
Referenced in `EpicCreaturesScript` with `GQ_NemesisKeyword` and kill tracking. Nemesis creatures have higher horde spawn chances (15% vs default) and need minimum 3 player kills to rank up. The actual nemesis quest fragment (`QF_Nemesis_000040CE`) is empty in the decompile, suggesting it's either data-driven or was cut.

### Key Insight: EpicCreatureDisallowed
Certain creatures are explicitly blocked from becoming legendary via `EpicCreatureDisallowedKeywords`. The Wendigo Colossus has `EpicCreatureDisallowed` keyword hardcoded in its race script - it can NEVER be a random legendary.

### Debug Variables
The epic system has debug override dice rolls:
- `DebugChanceDieRoll` - Force the chance roll
- `DebugRankDieRoll` - Force the rank
- `DebugAbilityDieRoll` - Force which ability
- `DebugHordeDieRoll` - Force horde spawn
All default to -1 (disabled). These are QA testing hooks.

---

## 7. The Scorchtongue - Multi-Body Boss

The Scorchtongue is a multi-part creature with THREE separate race records:
- **ScorchtongueHeadRace** (0x00786D48) - The main head, scorchtongue.hkx
- **ScorchtongueBodyRace** (0x0079B8C2) - The body segment, scorchtonguebody.hkx
- **ScorchtongueTailRace** (0x00787118) - The tail, scorchtonguetail.hkx

Each part is a separate actor with its own health pool. The body has an animation script (`ScorchtongueBodyAnimationScript`) that handles raising and lowering animations for the body segment.

**Scorchtongue Attacks:**
- `crRD01_Enc06_Scorchtongue_AcidBreath` (0x00787A8C) - Acid breath from the head
- `crRD01_Enc06_Scorchtongue_AcidSpit` (0x007878E4) - Ranged acid projectile

The ZZZ-prefixed body NPC (`ZZZ_RD01_Enc06_ScorchtongueBody`) suggests the body part was deprecated in favor of a new implementation, but the head and tail remain active.

---

## 8. Bigfoot - Party Crasher System

**BigfootRace** (0x00868BBC) uses the **Behemoth skeleton** (`supemutantbehemoth.hkx`). Only one NPC exists: `LvlBigfoot_PartyCrasher` (0x00868BBA).

### Bigfoot Spawn Mechanics (SpawnBigfootPartyCrasher + BigfootPartyCrasherDespawn):

1. **Spawn chance** controlled by `RA_PartyCrasherSpawnChance_Bigfoot` global variable
2. **Presentation sequence**: Waits `PresentationDelay` (12s) after a Public Event ends, then plays intro explosion to obscure entrance, waits `SpawnDelay` (5s), then reveals the actor
3. **Fight timer**: `FightDuration` (global variable) determines how long players can fight before despawn
4. **Halfway warning**: Message shown at 50% fight duration
5. **Despawn warning**: Message shown `DespawnMessageBuffer` (15s) before fight ends
6. **Despawn sequence**: Plays `DespawnAnim`, joins `NonHostileFaction`, outro roar, explosion obscures exit, then fades out after `FadeoutTimeDelay`
7. **Auto-legendary**: System calls `SQ_EpicCreatures` to force legendary status

### Bigfoot Attacks:
- `crUnarmedBigfoot` (0x00868BC3) - Melee unarmed
- `crBigfootTickToss` (0x00868BC2) - **Throws ticks as projectiles** (projectiletick.nif)
- `crBigfootTree` (0x00868BC1) - Melee with a tree bat (treebat.nif)

### Party Crasher System (Generic)
The `SpawnPartyCrasher` script reveals a generic system that can spawn ANY creature as a party crasher after public events. The struct includes:
- Any ActorBase can be a party crasher
- Each has its own spawn chance
- Default EpicRank of 3 (three-star legendary)
- Custom spawn sound effects

**Known Party Crashers:**
- Bigfoot (dedicated system)
- Mirelurk Queen
- Scorchbeast
- Wendigo Colossus
- Deathclaw (variant 04)
- Storm Boss

---

## 9. The Ultracite Titan - Phase-Based Boss

`CreatureUltraciteAbominationScript` reveals the Titan fight mechanics:

### Multi-Phase Mutation System
- Uses `MutationStages` struct array for arbitrary number of phases
- Each phase has: health percentage, new position, quest stage, transition stage
- **Tunneling mechanic**: Titan burrows underground (`enterTunnelFurniture`), stays for `tunnelDuration`, then ambushes from a new position (`exitTunnelFurniture`)
- Custom mutation spell replaces the default legendary mutation - allows unlimited phase transitions
- Final phase applies `BlockMutationsKeyword` to prevent further mutations
- `MutationEligibleKeyword` prevents premature mutations on laggy servers

### Add Management
- Max 6 Ultramites simultaneously (`MaxAdds_Ultramites`)
- Max 6 Mole Miners simultaneously (`MaxAdds_MoleMiners`)
- Uses wave-based spawning through EWS (Encounter Wave System)

### Between Phases
- Old Titan is DELETED after tunnel animation (`DeleteTitanTimerDuration` = 8s)
- NEW Titan is spawned using either normal or final-phase form
- Boss is invulnerable during transitions with player messaging

---

## 10. The Drifter Boss - Weapon Switching AI

`DrifterBossScript` reveals one of the most complex boss AIs in the game:

### Dynamic Weapon Selection
Switches between three weapons based on distance:
- `CloseRangeWeapon` (within `CloseRangeDistance` = 400 units)
- `MediumRangeWeapon` (between close and long)
- `LongRangeWeapon` (beyond `LongRangeDistance` = 1000 units)

Distance checked every 0.5 seconds (`CheckInterval`).

### Escalating Teleport Combat Styles
Five teleport frequency levels:
- `CombatStyleTeleportOff` -> `Min` -> `Low` -> `Mid` -> `High` -> `Max`

### Air Tank Mechanic
- Tracks `AvailableCondition1AV` (a crippleable part)
- When crippled: explosion + frenzy spell
- `DamageFraction` = 5 (takes 1/5 of max health as damage?)

### Enrage Mechanic
- `DrifterEnrageAnimation` plays for 4.8 seconds
- `DrifterEnrageExplosion` at 2.2 seconds into the animation
- Phase changes grant abilities from `DrifterEpicAbilities` FormList

---

## 11. The Storm Boss - Lightning Caller

`StormBossRaceScript` reveals unique mechanics:

### Call Down Lightning
- Finds all players within 512 units
- Places strike markers at player positions
- Two animation events: `CallDownLightningStart` (marks targets) and `CallDownLightning` (strikes)
- Melee attacks disabled until AFTER first lightning call (`Storm_RegionBoss_EnableMeleeAttacks`)

### Cripple-Based Spawning
- When specific body parts are crippled, objects spawn from those parts
- Configurable per-body-part: AV, Form, count, skeleton node
- e.g., breaking an arm might spawn additional enemies

### Multi-Stage Boss Event
The `RegionBossQuestScript` reveals a 3-stage boss fight:
- Each stage has its own boss actor
- Destructible floor system (lightning destroys 3 floors per strike)
- Laser grid puzzle with random open/close cycles (5-15s timer, 50% chance)
- When one boss dies and others remain, survivors get `EpicRankUpFX_Spell` (power up)
- Robot self-destruct mechanic available

---

## 12. The Interloper - NOT a Creature

The Interloper has **no RACE record, no NPC_ record, and no creature scripts**. Searching the full ESM dump yields zero results for "Interloper" in the main data files. It appears ONLY in string/text data:

- `[000438BC]` is a string reference titled simply "Interloper"
- Lore text describes it as an entity "beyond" that calls from "deep places of the earth"
- The Cult of the Mothman's scriptures warn against it as a deceiver

**Technical reality:** The Interloper in Lucky Hole Mine and other locations is implemented as **static world geometry** (STAT records) or activators, NOT as an NPC/creature. It has no health, no AI, no race. It is literally set dressing with lore significance. There is no hidden "Interloper boss fight" in the data.

---

## 13. Deleted WIP4 Test Creatures - Unreleased Modifiers

A batch of `DEL_WIP4_TESTNPC` entries reveal creature modifiers that were tested but deleted:

| Test NPC | Modifier |
|----------|----------|
| EncOgua_Vampire | Vampire (lifesteal?) |
| EncOgua_Burning | Burning (fire damage) |
| EncDeathclaw_AbsorbingBallistic | Absorbs ballistic damage |
| EncDeathclaw_AbsorbingEnergy | Absorbs energy damage |
| EncDeathclaw_AbsorbingExplosive | Absorbs explosive damage |
| EncDeathclaw_AbsorbingMelee | Absorbs melee damage |
| EncDeathclaw_AbsorbingFire | Absorbs fire damage |
| EncBlueDevil_Speeding | Enhanced speed |
| EncBlueDevil_Cloaking | Stealth/cloaking |
| EncSheepSquatch_Frenzying | Frenzy inducing |
| EncSheepSquatch_Energetic | Enhanced energy |

These "Absorbing" modifiers would have made creatures immune/resistant to specific damage types. The "Vampire" Ogua would drain health. None shipped, but the prefix "WIP4" suggests this was for a Work-In-Progress update phase 4.

---

## 14. Creature Variant System

`CreatureVariantScript` reveals a generic system for converting any creature to a variant at runtime:
- Matches creature by Race
- Applies an ObjectMod (visual/stat changes)
- Removes original factions, adds variant faction
- Plays transition VFX (shader + explosion)
- Adds variant keyword

This is likely the system behind Scorched creatures, Glowing variants, etc.

### Scorched Conversion
`ScorchedConversionMagicEffect` works by:
1. Looking up the target's race in a `SkinData` array
2. Applying the matching skin (armor) and ObjectMod
3. Adding the `ScorchedFaction` and `abRaceScorched` ability

`ScorchedConvertActorEffect` simply adds/removes the `ScorchedConvert` keyword, which the ability script watches for.

---

## 15. Disease System Details

`SURV_DiseasedCreatureScript` shows:
- Each creature type has its own disease chance (per-keyword globals)
- `MinCreatureLevelForDisease` = 10 (below level 10, no disease)
- Some creatures bypass the level check (radroaches, mirelurk spawn) via `SURV_DiseaseIgnoreMinCreatureLevelKeywords`
- Daily Ops creatures have a separate keyword check (`DailyOpsCreatureKeyword`)

---

## 16. MechTestRace - Unknown Prototype

`MechTestRace` (0x006820AD) has:
- A unique skeleton: `actors/mechtest/mechtest.hkx`
- An NPC: `EncMechTest` (0x006820AC)
- A skin: `SkinMechTest` (0x006820A4)
- No keywords, no FULL name in the dump
- Only one model reference

This appears to be a prototype for a mechanical/mech creature that never progressed beyond testing. The skeleton name suggests it was a test for a rideable or large mechanical entity.

---

## 17. Beezlebub - Named Honey Beast Boss

`SSE_Beezlebub` (0x0079AAA6) is a unique named Honey Beast that appears in the Skyline Valley expedition content:
- Has its own actor value: `SSE_BESusan_Beezlebub_AV`
- Unique weapon: `crUnarmed_SSE_Beezlebub` (0x007A3047)
- Unique weapon: `crBeezlebubBeeSwarmSpawn` (0x007B7711) - spawns bee swarms
- Has a world marker: `BeezlebubMarker` with a LocRefType `Beezlebub_Spawmarker_LocRef`
- Has dialogue: `BESusan_BeezlebubPrelude` - NPC Susan "gets aggressive when mentioning Beezlebub"
- Has a plushie: `ATX_Plushie_Beezlebub_Misc`

---

## 18. Healing Spear Weapons

Two healing spear weapons exist:
- `SpearHealing` (0x0084F1F7) - Used by Lost/Healer NPCs
- `crSpearHealing` (0x00883688) - Creature version

These are used by the "Lost Healers" (LostHealerRace) in the Backwoods update - NPC enemies that heal other enemies during combat.

---

## 19. Winding Path Hallucination Creatures

`WindingPathCreatureEffects` reveals that creatures at the Palace of the Winding Path are displayed at **10% opacity** (`SetAlpha(0.1)`) with a special shader effect. They're "hallucinatory" - semi-transparent ghosts. The effect is cleanly removed when the magic effect ends.

---

## 20. Super Mutant Behemoth Boss - Tantrum Phase

`BossScript` (for BS02_MQ05) reveals the Behemoth boss has THREE tantrum phases:
- Each triggered at a health percentage threshold
- Tantrums last `TantrumTime` seconds
- During tantrum: VFX spell applied, `IgnoreCombatKeyword` added
- Each can only trigger once (`Triggered` bool prevents re-trigger)

The Behemoth Boss also reuses the Grafton Monster's salvo attack system (`GraftonOilBombSalvoSpell`) but with target markers showing landing zones (`VisualTargetMarker` + `VisualTargetMarkerEffect` with a `SalvoLaunchDelay`).

---

## Summary of Key Community-Unknown Findings

1. **Deathclaws procedurally dismember players** - coin flip per body part on kill animation
2. **Mothman becomes literally unkillable** during invisibility (SetGhost + SetAlpha 0)
3. **Scorchbeast has THREE different attack timing modes** (flying/ground/interior)
4. **Wendigo Colossus can NEVER be legendary** - hardcoded exclusion
5. **Mirelurk King sonic attack damages perception**, not just health
6. **Legendary chance formula**: Base 1% + 0.04% per creature level, capped at 5%, modified by region
7. **16 Prime creature variants exist** in ESM, most disabled with zzz_ prefix
8. **Boss Chicken (ZZZ_BossChickenRace)** - fully implemented boss radchicken, cut
9. **Cut Gorilla Race** ported from FO4 but never activated
10. **Cut Quantum Deathclaw** from Nuka-World ported but disabled
11. **Cut Super Mutant Ghoul hybrid** - would have been SM/ghoul crossover
12. **WIP4 damage-absorbing creature modifiers** - tested but cut
13. **MechTestRace** - unknown mechanical creature prototype
14. **The Interloper is NOT a creature** - it's static geometry with no AI/health/race
15. **Bigfoot throws ticks as projectiles** and uses a tree as a melee weapon
16. **Sheepsquatch has 3 combat stages** that change behavior at health thresholds
17. **All epic creatures get a one-time full heal** at 50% health (the "mutation" mechanic)
18. **Minimum 100 HP floor** for legendary creatures - even molerats
