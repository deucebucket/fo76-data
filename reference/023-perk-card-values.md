# Finding 023: Perk Card Values - Complete ESM Cross-Reference

**Date:** 2026-03-20
**Source:** SeventySix.esm dump (PERK, MGEF, CURV, GMST records)
**Cross-referenced with:** Nuka Knights datamining, FalloutBuilds.com, Fallout Wiki, community testing

---

## Overview

The ESM dump contains 1,963 PERK records total:
- **328** disabled (`zzz_` prefix) - cut or deprecated perks
- **91** explicitly cut (`CUT_` prefix)
- ~200 player-facing perk cards (including ranked variants)
- ~1,300+ internal/system perks (enemy scaling, quest triggers, legendary effects, daily ops mutations, etc.)

The dump format extracts EDID (editor ID), FULL (display name FormID), DESC (description FormID), and CTDA (conditions), but does **not** include the EPFD (Entry Point Function Data) subrecords that contain raw magnitude values. Actual percentages are embedded in the PERK binary data and in MGEF magnitude fields referenced by string table FormIDs. Community sources and datamining by Nuka Knights fill in the confirmed values.

---

## ESM Structure: How Perk Values Work Internally

### Damage Perks Reference MGEF FormIDs
The perk system works through Magic Effect (MGEF) references. Key MGEF records identified:

| MGEF FormID | Editor ID | Purpose |
|---|---|---|
| `0x0031BE45` | AbPerkFortifyDmgRiflesNonAuto | Rifleman damage |
| `0x0031BE46` | AbPerkFortifyDmgRiflesAuto | Commando damage |
| `0x0031BE47` | AbPerkFortifyDmgPistolsAuto | Guerrilla damage |
| `0x0031BE48` | AbPerkFortifyDmgPistolsNonAuto | Gunslinger damage |
| `0x0031BE49` | AbPerkFortifyDmgHeavyGuns | Heavy Gunner damage |
| `0x0031BE4A` | AbPerkFortifyDmgShotguns | Shotgunner damage |
| `0x003440AF` | AbPerkFortifyDmgMelee1H | Gladiator damage |
| `0x003440A5` | AbPerkFortifyDmgMelee2H | Slugger damage |
| `0x0035206A` | AbPerkFortifyDmgMeleeUnarmed | Iron Fist damage |
| `0x003440B2` | AbPerkFortifyDmgExplosives | Demolition Expert damage |
| `0x004F6AB0` | abPerkFortifyDmgAll | Bloody Mess / universal damage |
| `0x00563B86` | AbPerkFortifyDmgBows | Archer damage |
| `0x00393F60` | AbPerkFortifyDmgVsGlowing | Glow Sight damage |
| `0x007C7000` | abPerkFortifyDmgClose | Close-range damage perk |
| `0x00800569` | abPerkFortifyDmgFar | Down Ranger far damage |
| `0x00803E2C` | AbPerkFortifyDmgTorso | Center Masochist torso damage |
| `0x00801246` | abPerkFortifyDmgCrippled | Damage vs crippled |
| `0x00805AAA` | abPerkFortifyDmgPerCrippled | Damage per crippled limb |
| `0x007C92C6` | AbPerkFortifyDmgWeakSpot | Weak spot damage |
| `0x00801CA1` | abPerkFortifyDmgAP | Damage from AP |
| `0x0085A2F3` | abPerkFortifyDmgVsFreezing | Damage vs freezing targets |
| `0x0083F35F` | abPerkFortifyDmgVsBurning | Damage vs burning targets |
| `0x0083F360` | abPerkFortifyDmgVsPoisoned | Damage vs poisoned targets |
| `0x00837DF9` | abPerkFortifyDmgVsBleeding | Damage vs bleeding targets |
| `0x00854902` | AbPerkFortifyDmgGrenades | Grenade damage |
| `0x0081A7D4` | AbPerkFortifyDmgMultEnergy | Energy damage multiplier |
| `0x0081A7D5` | AbPerkFortifyDmgMultFire | Fire damage multiplier |
| `0x0081A7D6` | AbPerkFortifyDmgMultCryo | Cryo damage multiplier |

### Defensive MGEF References

| MGEF FormID | Editor ID | Purpose |
|---|---|---|
| `0x0004A0AC` | AbPerkFortifyResistDamage | Damage Resistance (Ironclad, Barbarian) |
| `0x000559A4` | AbPerkFortifyResistEnergy | Energy Resistance (Refractor) |
| `0x0004D86E` | AbPerkFortifyResistFire | Fire Resistance (Fireproof) |
| `0x0004D86B` | AbPerkFortifyResistPoison | Poison Resistance |
| `0x0004C47D` | AbPerkFortifyResistRadiationExpose | Rad Resistance |
| `0x008A7E7B` | abFortifyDamageRecieved | Damage received modifier (note: typo "Recieved" is in the ESM) |
| `0x007ACAFE` | AbPerkFortifyLimbDamageResistance | Limb damage resist |
| `0x007ACE7B` | AbPerkFortifyDeflectChance | Deflection chance |
| `0x007ACAFD` | AbPerkFortifyEvadeChance | Evade chance |
| `0x007BC541` | AbPerkFortifyArmorBonus | Armor bonus |

### Utility MGEF References

| MGEF FormID | Editor ID | Purpose |
|---|---|---|
| `0x0006F7DB` | AbPerkFortifyCarryWeight | Carry weight (Strong Back) |
| `0x00511AE5` | AbPerkFortifyActorSpeedMult | Speed multiplier |
| `0x00511AE4` | AbPerkFortifyHealth | Max health (Lifegiver) |
| `0x0062D860` | AbPerkFortifyActionPoints | AP pool |
| `0x0017ED89` | AbPerkFortifyActionPointRegen | AP regen (Action Boy/Girl) |
| `0x00127560` | AbPerkFortifyReloadSpeedMult | Reload speed |
| `0x003BAE7F` | AbPerkFortifyMoveSpeedEffect | Movement speed |
| `0x003E9567` | AbPerkFortifyMeleeSpeedEffect | Melee speed |
| `0x007AC997` | AbPerkFortifyStimpakHealing | Stimpak healing |
| `0x007B3F0C` | AbPerkFortifyRadawayHealing | RadAway healing |
| `0x00852F5C` | AbPerkFortifyActorWeaponChargeUpSpeedMult | Weapon charge-up speed |

---

## Game Settings (GMST) - Perk-Related Values

From `game_settings.txt`:

| Setting | Value | Purpose |
|---|---|---|
| `fDamageStrengthBase` | 1.000000 | Base melee damage from STR |
| `fDamageStrengthMult` | 0.100000 | Per-STR-point melee damage bonus (10%) |
| `fDamageSneakAttackMult` | 1.000000 | Base sneak attack multiplier (1x = no bonus without perks) |
| `fDamagePCSkillMax` | 1.500000 | Maximum skill-based damage cap |
| `fDamageToArmorPercentage` | (in dump) | Armor damage calculation |
| `fDamageGunWeapCondBase` | (in dump) | Gun condition damage base |
| `fDamageGunWeapCondMult` | (in dump) | Gun condition damage multiplier |
| `fDamageMeleeWeapCondBase` | (in dump) | Melee condition damage base |
| `fDamageMeleeWeapCondMult` | (in dump) | Melee condition damage multiplier |
| `iVATSConcentratedFireBonus` | 20 | Concentrated Fire VATS accuracy bonus per shot |
| `iPerkBlockDisarmChance` | (in dump) | Block disarm chance from perks |
| `iPerkAttackDisarmChance` | (in dump) | Attack disarm chance from perks |
| `fPerkCardScrapGlobalValueMult` | (in dump) | Perk card scrapping multiplier |
| `fPerkCardScrapFoilValueMult` | (in dump) | Foil perk card scrap value multiplier |
| `fReloadFromMoveSpeedPerkRatio` | 0.500000 | Reload speed from movement perk ratio |
| `fDistanceForCloseDamage` | 850.000000 | Distance threshold for "close range" damage perks |

**Key finding:** `fDistanceForCloseDamage = 850.0` defines the boundary for close-range perks. Anything within 850 game units counts as "close."

---

## Weapon Damage Perks - Confirmed Values

### Standard Weapon Damage Cards (Post-Patch 60, June 2025)

**IMPORTANT: Patch 60 (June 2025) restructured all weapon damage perks.** The old system of Base/Expert/Master with 3 ranks each was replaced. Expert and Master ranks 2-3 are now `zzz_` disabled.

**Pre-Patch 60 (Legacy System):**
Each weapon type had 3 tiers (Base, Expert, Master), each with 3 ranks:
- Rank 1: +10%, Rank 2: +15%, Rank 3: +20% per tier
- Max stacking all 3 tiers at rank 3: +60% total

**Post-Patch 60 (Current System):**
Damage perks were restructured. Base perks retained as primary damage cards. Expert and Master became single-rank specialized perks rather than pure damage stacking.

#### Rifleman (Non-Automatic Rifles) - Perception
| Perk | FormID | Ranks | Values |
|---|---|---|---|
| Rifleman | `0x0004A0B6`-`0x0004A0B8` | 3 | +10% / +15% / +20% |
| Expert Rifleman | `0x002EBD2A` | 1 | +20% (single rank) |
| Master Rifleman | `0x002EBD30` | 1 | +20% (single rank) |

#### Commando (Automatic Rifles) - Perception
| Perk | FormID | Ranks | Values |
|---|---|---|---|
| Commando | `0x0031AEEF`-`0x0031AEF1` | 3 | +10% / +15% / +20% |
| Expert Commando | `0x0031AEF2` | 1 | +20% (single rank) |
| Master Commando | `0x0004A0C5` | 1 | +20% (single rank) |

#### Heavy Gunner - Strength
| Perk | FormID | Ranks | Values |
|---|---|---|---|
| Heavy Gunner | `0x0031AF14`-`0x0031AF16` | 3 | +10% / +15% / +20% |
| Expert Heavy Gunner | `0x0031AF10` | 1 | +20% (single rank) |
| Master Heavy Gunner | `0x0004A0D6` | 1 | +20% (single rank) |

#### Shotgunner - Strength
| Perk | FormID | Ranks | Values |
|---|---|---|---|
| Shotgunner | `0x00090590`-`0x00127855` | 3 | +10% / +15% / +20% |
| Expert Shotgunner | `0x001447AC` | 1 | +20% (single rank) |
| Master Shotgunner | `0x001A2DE1` | 1 | +20% (single rank) |

#### Gunslinger (Non-Auto Pistols) - Agility
| Perk | FormID | Ranks | Values |
|---|---|---|---|
| Gunslinger | `0x0031AEFA`-`0x0031AEFC` | 3 | +10% / +15% / +20% |
| Expert Gunslinger | `0x0031AEFD` | 1 | +20% (single rank) |
| Master Gunslinger | `0x0004A09F` | 1 | +20% (single rank) |

#### Guerrilla (Auto Pistols) - Agility
| Perk | FormID | Ranks | Values |
|---|---|---|---|
| Guerrilla | `0x0031AF01`-`0x0031AF03` | 3 | +10% / +15% / +20% |
| Expert Guerrilla | `0x0031AF04` | 1 | +20% (single rank) |
| Master Guerrilla | `0x0031AF08` | 1 | +20% (single rank) |

#### Gladiator (1H Melee) - Strength
| Perk | FormID | Ranks | Values |
|---|---|---|---|
| Gladiator | `0x003440A8`-`0x003440AA` | 3 | +10% / +15% / +20% |
| Expert Gladiator | `0x003440AB` | 1 | +20% (single rank) |
| Master Gladiator | `0x00123A5B` | 1 | +20% (single rank) |

#### Slugger (2H Melee) - Strength
| Perk | FormID | Ranks | Values |
|---|---|---|---|
| Slugger | `0x0004A0B5`-`0x000E36FD` | 3 | +10% / +15% / +20% |
| Expert Slugger | `0x000E36FE` | 1 | +20% (single rank) |
| Master Slugger | `0x00520BD4` | 1 | +20% (single rank) |

### New Damage Perks (Patch 60+)

| Perk | SPECIAL | Ranks | Values per Rank |
|---|---|---|---|
| Down Ranger | Perception | 3 | +10% / +15% / +20% ranged damage to far enemies |
| Center Masochist | Perception | 3 | +25% / +50% / +75% ranged damage when attacking the torso |
| Weak Spot | Perception | 3 | +20% damage per crippled limb on target (Rank 1), scaling up |
| Bullet Storm | Strength | 3 | Gain 3% / 6% / 9% damage per 30 ammo spent, 10 max stacks |

**Bullet Storm (Patch 62 additions):**
- Each stack also increases bash damage by 5%
- You keep half stacks on reload
- +1% reload speed per stack

### Armor Penetration Perks

| Perk | SPECIAL | Ranks | Values per Rank |
|---|---|---|---|
| Tank Killer | Perception | 3 | Ignores 12% / 24% / 36% armor (rifles) |
| Incisor | Strength | 3 | Ignores 25% / 50% / 75% armor (melee) |
| Stabilized | Intelligence | 3 | Ignores 15% / 30% / 45% armor + 30% accuracy (PA, heavy guns) |

---

## Defensive Perks - Confirmed Values

| Perk | SPECIAL | Ranks | Values per Rank |
|---|---|---|---|
| Blocker | Strength | 3 | 15% / 30% / 45% less melee damage taken |
| Fireproof | Endurance | 3 | 15% / 30% / 45% less fire/explosion damage + 20/40/60 Fire Resist |
| Ironclad | Endurance | 5 | +10 / +20 / +30 / +40 / +50 DR and ER (not in PA) |
| Barbarian | Strength | 3 | +4 DR per STR point (Rank 1), scaling per rank |
| Evasive | Agility | 1 | +3 DR/ER per AGI point |
| Dodgy | Agility | 1 | 15% chance to avoid 15% damage at cost of 30 AP |
| Serendipity | Luck | 1 | 15% chance to avoid damage below 30% health |
| Ricochet | Luck | 1 | 10% chance to reflect ranged attacks |
| Bullet Shield | Strength | 4 | +20 / +40 / +60 / +80 DR while firing heavy weapon |
| Refractor | Perception | 4 (reduced from 4) | +10 / +20 / +30 / +40 ER |
| Rad Resistant | Endurance | 4 | +10 / +20 / +30 / +40 Rad Resist |

---

## Utility/QoL Perks - Confirmed Values

### Weight Reduction
| Perk | SPECIAL | Ranks | Values per Rank |
|---|---|---|---|
| Pack Rat | Strength | 2 | 25% / 50% junk weight reduction |
| Bandolier | Strength | 2 | 45% / 90% ballistic ammo weight reduction |
| Bear Arms | Strength | 3 | 30% / 60% / 90% heavy gun weight reduction |
| Traveling Pharmacy | Strength | 2 | 30% / 60% chem weight reduction |
| Thru-Hiker | Agility | 2 | 30% / 60% food/drink weight reduction |
| Batteries Included | Intelligence | 2 | 30% / 60% energy ammo weight reduction |
| Packin' Light | Agility | 1 | 25% pistol weight reduction |

### Combat Utility
| Perk | SPECIAL | Ranks | Values per Rank |
|---|---|---|---|
| Bloody Mess | Luck | 3 | +5% / +10% / +15% damage (all sources) |
| Tenderizer | Charisma | 1 | Targets take +0.1% more damage per hit, up to +100% |
| Nerd Rage | Intelligence | 1 | Below 20% HP: +20 DR, +10% damage, +15% AP regen |
| Adrenaline | Agility | 1 | +10% damage per kill (up to 10 stacks = +100%), 30s duration |
| Concentrated Fire | Perception | 3 | +20% VATS accuracy per shot (GMST: `iVATSConcentratedFireBonus = 20`) |
| Better Criticals | Luck | 3 | +20% / +30% / +40% critical damage |
| Suppressor | Charisma | 3 | Targets deal 5% / 10% / 15% less damage for 2s on hit |
| Glow Sight | Perception | 3 | +20% / +40% / +60% damage vs glowing enemies |
| Demolition Expert | Intelligence | 5 | +20% / +30% / +40% / +50% / +60% explosive damage |

### Crafting/Maintenance
| Perk | SPECIAL | Ranks | Values per Rank |
|---|---|---|---|
| Weapon Artisan | Intelligence | 3 | Repair weapons to 130% / 145% / 160% condition |
| Fix It Good | Intelligence | 3 | Repair armor to 130% / 145% / 160% condition |
| Super Duper | Luck | 3 | 10% / 20% / 30% chance to craft double |
| Ammosmith | Agility | 2 | +40% / +80% ammo crafted |
| Gunsmith | Intelligence | 3 | Guns break 10% / 20% / 30% slower |
| White Knight | Agility | 3 | Armor breaks 30% / 45% / 60% slower |

### New Patch 60+ Perks
| Perk | SPECIAL | Ranks | Values per Rank |
|---|---|---|---|
| Conductor | Strength | 1 | Melee attacks create explosion |
| Light Meal | Strength | 2 | Food weight reduction (new combined perk) |
| Stable Tools | Intelligence | 3 | Tool/power tool durability bonus |
| Arms Keeper | Intelligence | 2 | Weapon condition bonus |
| Circuit Breaker | Intelligence | 1 | Energy weapon condition bonus |

---

## Legendary Perks - All Values Per Rank

### SPECIAL Legendary Perks
Each SPECIAL legendary perk (`LGN_LegendaryStrength_Perk01` through `_Perk04`, etc.) adds:
- Rank 1: +1 to SPECIAL, Rank 2: +2, Rank 3: +3, Rank 4: +5
- FormIDs: `0x0011C7C3`-`0x0011C7DE` (Agility through Strength)
- Plus `0x005CF1D1` (Endurance Rank 4 separate entry)

### Combat Legendary Perks

| Perk | ESM Name | Ranks | Values |
|---|---|---|---|
| Follow Through | `LGN_FollowThrough` | 4 | +10% / +20% / +30% / +40% damage for 10s after sneak hit |
| Taking One For The Team | `LGN_TakingOneForTheTeam` | 4 | Enemies attacking you take +5% / +10% / +15% / +20% more damage |
| Far-Flung Fireworks | `LGN_FarFlungFireworks` | 4 | 10% / 13% / 16% / 20% chance killed enemies explode |
| Hack and Slash | `LGN_HackAndSlash` | 4 | 25% / 50% / 75% / 100% chance melee hits create explosion |
| Collateral Damage | `LGN_CollateralDamage` | 4 | Heavy gun hits cause area damage |
| Exploding Palm | `LGN_ExplodingPalm` | 4 | Unarmed attacks have chance to cause explosion |
| Retribution | `LGN_Retribution` | 4 | Chance to reflect melee damage |
| Detonation Contagion | `LGN_DetonationContagion` | 4 | Explosions cause chain reactions |
| Brawling Chemist | `LGN_BrawlingChemist` | 4 | Melee attacks apply chem effects |
| Sizzling Style | `LGN_SizzlingStyle` | 4 | Fire damage aura |
| Blood Sacrifice | `LGN_BloodSacrifice` | 4 | Team healing on revive |

### Defense Legendary Perks

| Perk | ESM Name | Ranks | Values |
|---|---|---|---|
| What Rads | `LGN_WhatRads` | 4 | +50/+75/+100/+300 Rad Resist, restore 1/2/3/6 Rads/sec |
| Funky Duds | `LGN_FunkyDuds` | 4 | +50/+100/+150/+200 Poison DR (matching armor set) |
| Electric Absorption | `LGN_ElectricAbsorption` | 4 | 10%/13%/16%/20% chance energy attacks recharge fusion core |

### Utility Legendary Perks

| Perk | ESM Name | Ranks | Values |
|---|---|---|---|
| Ammo Factory | `LGN_AmmoFactory` | 4 | +50%/+100%/+150%/+200% ammo crafted |
| Power Sprinter | `LGN_PowerSprinter` | 4 | Reduced AP cost while sprinting in PA |
| Master Infiltrator | `LGN_MasterInfiltrator` | 4 | Auto-pick/hack at progressively higher levels |
| Survival Shortcut | `LGN_SurvivalShortcut` | 4 | Periodic food/water restoration |
| Power Armor Reboot | `LGN_PowerArmorReboot` | 4 | Chance to revive in PA on death |

### Cut/Disabled Legendary Perks (zzz_ prefix)

| Perk | ESM Name | Status |
|---|---|---|
| Nuclear Proliferator | `zzz_LGN_NuclearProliferator` | All 4 ranks disabled |
| Botany Buddy | `zzz_LGN_BotanyBuddy` | All 4 ranks disabled |
| Rewards Hound | `zzzLGN_RewardsHound` | All 4 ranks disabled |
| Arms Breaker | `zzzLGN_ArmsBreaker` | All 4 ranks disabled |
| Overcharged Core | `zzzLGN_OverchargedCore` | All 4 ranks disabled |
| Suited Up | `zzz_LGN_SuitedUp` | All 4 ranks disabled |
| Heavy Duty | `zzz_LGN_HeavyDuty` | All 4 ranks disabled |
| Thin Skinned | `zzz_LGN_ThinSkinned` | All 4 ranks disabled |

---

## Mutations - ESM Structure

The ESM tracks mutations through paired perk records for positive/negative effects:

| Mutation | Positive Effect Perk | Negative Effect Perk | Positive | Negative |
|---|---|---|---|---|
| Adrenal Reaction | `CUT_Mutation_AdrenalPositive_Perk` | (separate) | +5% damage per kill stack (10 max) | -50 Max HP |
| Bird Bones | `Mutation_ReduceFallDamage_Perk` | `Mutation_IncreasedLimbDamage_Perk` | +4 AGI, reduced fall speed | -4 STR |
| Carnivore | `Mutation_EatAllTheMeat_Perk` | `Mutation_EatNoVeggies_Perk` | 2x meat benefits | No veggie benefits |
| Chameleon | `Mutation_ChameleonOnAttack_Perk` | (none significant) | Invisible while unarmored+still | - |
| Eagle Eyes | (separate MGEF) | `Mutation_ReduceAccuracy_Perk` | +25% crit damage, +4 PER | -4 STR |
| Egg Head | (separate MGEF) | (separate MGEF) | +6 INT | -3 STR, -3 END |
| Electrically Charged | (separate cloak spell) | (none) | Chance to shock melee attackers | Small Energy drain |
| Empath | `Mutation_EmpathPenalty_Perk` | (penalty perk) | Teammates take -25% damage | You take +33% damage |
| Grounded | `Mutation_ReduceEnergyDamage_Perk` | (separate) | +100 Energy Resist | -50% energy weapon damage |
| Healing Factor | (separate MGEF) | `Mutation_ReduceChemEffect_Perk` | +300% HP regen (out of combat) | -55% chem effects |
| Herbivore | `Mutation_EatAllTheVeggies_Perk` | `Mutation_EatNoMeat_Perk` | 2x veggie benefits | No meat benefits |
| Marsupial | (separate MGEF) | (separate) | +20 carry weight, increased jump | -4 INT |
| Scaly Skin | (separate MGEF) | (separate) | +50 DR, +50 ER | -50 AP |
| Speed Demon | `Mutation_IncreasedHungerThirst_Perk` | (negative perk) | +20% move speed, +20% reload | +50% hunger/thirst drain |
| Talons | `Mutation_Talons_Perk` | (separate) | +25% unarmed damage, bleed | -50% gun accuracy |
| Twisted Muscles | `Mutation_TwistedMuscles_Perk` | (separate) | +25% melee damage | -50% gun accuracy |
| Unstable Isotope | (cloak spell) | (none) | Chance to irradiate melee attackers | Small rad damage to self |

**Class Freak interaction:** `ClassFreak01`-`ClassFreak03` reduces negative mutation effects by 25%/50%/75%.
**Strange in Numbers:** `StrangeInNumbers01` gives +25% to positive mutation effects when on a team with other mutated players.

---

## Ghoul-Specific Perks (Patch 58+, March 2025)

From the ESM, ghoul legendary perks are prefixed with `GHL_LGN_`:

| Perk | ESM Name | Ranks | Notes |
|---|---|---|---|
| Feral Rage | `GHL_LGN_FeralRage` | 4 | `0x007AD40E`-`0x007AD34F` |
| Action Diet | `GHL_LGN_ActionDiet` | 4 | `0x00798018`-`0x0079801B` |
| Wild Card Last Shot | `zzz_GHL_LGN_WildCardLastShotPerk` | 4 | **DISABLED** - all 4 ranks `zzz_` |

### Cut Ghoul Perks (zzz_GHL_ prefix)
These were datamined but never shipped or were pulled:
- `zzz_GHL_200PercentPerformance` (2 ranks)
- `zzz_GHL_BurnTheWorld` (3 ranks)
- `zzz_GHL_CatReflexes` (3 ranks)
- `zzz_GHL_FaultySpots` (ranks 2-3 cut, rank 1 may be active)
- `zzz_GHL_JunkHunter` (1 rank)
- `zzz_GHL_LegendTracker` (1 rank)
- `zzz_GHL_Persuasive` (3 ranks)
- `zzz_GHL_ThroughJob` (1 rank)
- `zzz_GHL_TunnelRunner` (1 rank)
- `zzz_GHL_Acceptance` (1 rank)

---

## Cut / Disabled Perks Analysis

### CUT_ Prefix (91 records) - Never made it to live

Notable CUT perks:
- `CUT_Rifleman04`, `CUT_Commando04`, etc. - **Rank 4 of all weapon damage perks** were once planned
- `CUT_RiflemanExpert04`, `CUT_CommandoExpert04`, etc. - Rank 4 Expert variants
- `CUT_RiflemanMaster04`, `CUT_CommandoMaster04`, etc. - Rank 4 Master variants
- `CUT_Tenderizer02_Target`, `CUT_Tenderizer03_Target` - Multi-rank Tenderizer target debuffs
- `CUT_OneGunArmy04` - Rank 4 of One Gun Army
- `CUT_Mutation_AdrenalPositiveSuper_Perk` - "Super" adrenal mutation variant

**Key insight:** Every weapon damage perk was originally designed with 4 ranks. Rank 4 was cut before launch for all weapon types.

### zzz_ Prefix Player Perks (Notable)

Perks that were active but later disabled (consolidated in Patch 60):
- `zzz_CommandoExpert02`, `zzz_CommandoExpert03` - Expert tiers collapsed to 1 rank
- `zzz_RiflemanExpert02`, `zzz_RiflemanExpert03` - Same treatment
- All Expert/Master rank 2-3 for every weapon type
- `zzz_Adrenaline02`-`zzz_Adrenaline05` - Old 5-rank system replaced with 1-rank
- `zzz_NerdRage02`, `zzz_NerdRage03` - Collapsed to 1 rank
- `zzz_Tenderizer02`, `zzz_Tenderizer03` - Collapsed to 1 rank
- `zzz_PackRat03` - Rank 3 (75% reduction) removed
- `zzz_TravelingPharmacy03` - Rank 3 (90% reduction) removed
- `zzz_ThruHiker03` - Rank 3 removed
- `zzz_BatteriesIncluded03` - Rank 3 (90% reduction) removed
- `zzz_AttackDog01`-`zzz_AttackDog03` - Companion perk, removed (no companions in 76)
- `zzz_AdVictoriam_Perk` - BOS melee damage perk (faction-specific, cut)
- `zzz_DLC03_FortifyAccuracyFoodPerk` - Far Harbor DLC accuracy food (FO4 leftover)
- `zzz_DLC04_PerkLuckyRabbitsFoot` - Nuka-World rabbit foot perk (FO4 leftover)

---

## Curve Table References

The CURV records contain curve tables that define how certain perk/legendary values scale. Key perk-adjacent curves:

- `CT_PerkCardShareCost` (`0x00437FF3`) - Cost curve for sharing perk cards in teams
- `CT_PerkCardPack_LaunchPack001_Roll01`-`Roll04` - Perk card pack drop probability curves
- `CT_PerkCardPack_LaunchPack001_GoldRoll01`-`GoldRoll04` - Gold roll probability curves
- `CT_PerkCardPack_LaunchPack001_LevelOffsets` - Level-based offsets for card pack contents

Legendary armor curves (scale with conditions):
- `CT_Legendary_Armor_Bolstering01`-`05` + `_Desc` - Bolstering DR scaling with low HP
- `CT_Legendary_Armor_Vanguard01`-`05` + `_Desc` - Vanguard DR scaling with high HP
- `CT_Legendary_Armor_Heavyweight01`-`05` + `_Desc` - Heavyweight scaling
- `CT_Legendary_Armor_Lucid01`-`05` + `_Desc` - Lucid effect scaling
- `CT_Legendary_Armor_Overeater_Effect` - Overeater food-based DR scaling
- `CT_Legendary_Armor_Mutant` + variants - Mutant's per-mutation DR scaling
- `CT_Legendary_Armor_Cavalier` - Cavalier damage reduction while sprinting
- `CT_Legendary_Armor_Sentinel` - Sentinel damage reduction while standing still
- `CT_Legendary_Armor_Aristocrat01` - Aristocrat caps-based bonus

Weapon curves:
- `CT_Legendary_Weapon_ThrillSeeker` - Thrill Seeker effect
- `CT_Legendary_Weapon_ChargedUpWeapon` - Charged weapon scaling
- `CT_mod_Armor_LastStand_Bonus` - Last Stand armor bonus
- `CT_mod_Armor_StandFast_Bonus` - Stand Fast armor bonus
- `CT_mod_Armor_LastBastion_AccuracyBonus` - Last Bastion accuracy

---

## Hidden Interactions & Observations

### 1. Typo in ESM: "abFortifyDamageRecieved" (0x008A7E7B)
The MGEF for damage received has a typo ("Recieved" instead of "Received"). This has persisted since launch.

### 2. Melee Damage Formula Base Values
`fDamageStrengthBase = 1.0` and `fDamageStrengthMult = 0.1` confirm that melee damage = base * (1.0 + 0.1 * STR), meaning each STR point adds exactly 10% to base melee damage.

### 3. Sneak Attack Base = 1.0x
`fDamageSneakAttackMult = 1.0` means the sneak attack multiplier starts at 1x (no bonus) and is **entirely** perk-driven. Without Covert Operative, sneak attacks deal no extra damage. This differs from some wiki claims.

### 4. Close Range Threshold = 850 Units
`fDistanceForCloseDamage = 850.0` defines what counts as "close" for close-range damage perks. This is roughly 13-14 meters in-game.

### 5. Concentrated Fire is GMST-Driven
The `iVATSConcentratedFireBonus = 20` game setting directly controls the per-shot accuracy bonus. The perk card simply enables this mechanic rather than having its own magnitude.

### 6. FO4 Leftovers Still in ESM
`zzz_AttackDog`, `zzz_DLC03_FortifyAccuracyFoodPerk`, `zzz_DLC04_PerkLuckyRabbitsFoot` are Fallout 4 perks that were carried over in the engine but never functional in 76.

### 7. Babylon Prefix = Nuclear Winter
Perks prefixed `zzz_Babylon_` (e.g., `zzz_Babylon_Blocker03`, `zzz_Babylon_RiflemanMaster03`) were the Nuclear Winter PvP mode variants of perks with modified values. All are now disabled.

### 8. Weight Reduction Rank 3 Removals
Pack Rat, Traveling Pharmacy, Thru-Hiker, and Batteries Included all had their rank 3 (typically 75-90% reduction) disabled. This was a deliberate balance decision to prevent near-zero weight.

### 9. Expert/Master Perk Consolidation
The Patch 60 restructuring collapsed Expert and Master weapon perks from 3 ranks to 1 rank each. This means the total maximum damage from stacking all 3 tiers dropped from +60% (3 * 20%) to +60% (20% + 20% + 20%) - the same total but achieved differently (1 rank each instead of 3 ranks at tier max). The 6 extra perk points previously needed for rank 2-3 of Expert/Master are now freed up.

### 10. Legendary Perks That Were Cut After Implementation
`Arms Breaker`, `Overcharged Core`, `Nuclear Proliferator`, `Botany Buddy`, `Rewards Hound`, `Suited Up`, `Heavy Duty`, and `Thin Skinned` all had complete 4-rank implementations that were disabled. These are fully coded perks that could theoretically be re-enabled.

---

## Community Coverage Assessment

**Well-documented by community:** All standard perk card values, legendary perk values, mutation effects. Nuka Knights, FalloutBuilds.com, and the Fallout Wiki all maintain accurate perk databases that are updated with each patch.

**Less documented / ESM-exclusive findings:**
1. The full list of MGEF FormIDs that perks reference (useful for modding/datamining tools)
2. The exact GMST values (`fDistanceForCloseDamage`, `fDamageStrengthMult`, `fDamageSneakAttackMult = 1.0`)
3. The complete list of cut ghoul perks (`zzz_GHL_` prefix) - some known to dataminers but not widely documented
4. The FO4 perk leftovers still present in the ESM
5. The Babylon (Nuclear Winter) perk variant FormIDs
6. Curve table names for legendary armor scaling (useful for understanding how Bolstering/Vanguard/Overeater actually scale)

---

## Sources

- [Nuka Knights - Changed Perk Cards in Patch 62](https://nukaknights.com/articles/changed-perk-cards-in-patch-62-season-22.html)
- [Nuka Knights - Fishing Patch 60 All Changed Perk Cards](https://nukaknights.com/articles/fishing-patch-60-all-changed-perk-cards.html)
- [Nuka Knights - Ghoul Perks](https://nukaknights.com/articles/ghoul-perks-all-new-perk-cards.html)
- [FalloutBuilds.com - All Perk Cards](https://www.falloutbuilds.com/fo76/perks)
- [Fallout Wiki - Fallout 76 Perks](https://fallout.fandom.com/wiki/Fallout_76_perks)
- [Fallout Wiki - Legendary Perks](https://fallout.fandom.com/wiki/Fallout_76_legendary_perks)
- [Fallout Wiki - Mutations](https://fallout.fandom.com/wiki/Fallout_76_mutations)
- [The Duchess Flame - 2025 Guide to Perk Card Changes](https://www.theduchessflame.com/post/2024-guide-to-fallout-76-perk-card-changes)
- [Nuka Knights - PTS Combat and Perk Changes Preview](https://nukaknights.com/articles/pts-july-2025-upcoming-combat-and-perk-changes-preview.html)
