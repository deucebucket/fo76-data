# FO76 Legendary Effect Magnitudes - Extracted from Game Data

**Source**: 108 curve table JSONs from `tempest_data/misc/curvetables/json/legendarymods/`
**Cross-referenced with**: OMOD_records.txt (32,677 records), legendary system curves
**Date**: 2026-03-20

## Key Findings Summary

### Critical Wiki Discrepancies Found

| Effect | Wiki Claims | Actual Game Data | Severity |
|--------|------------|-----------------|----------|
| Bloodied (weapon) | +80% to +95% max damage | **+130% at 5% HP** | CRITICAL |
| Cavalier's (armor) | 75% chance for 15% reduction | **Deterministic 10% per piece multiplicative** | CRITICAL |
| Sentinel's (armor) | 75% chance for 15% reduction | **Deterministic ~5% per piece (23% at 5pc)** | CRITICAL |
| Nocturnal (weapon) | -50% during day | **+0% during day (no penalty)** | HIGH |
| Gourmand's (weapon) | Up to +24% | **Up to +40% at max satisfaction** | HIGH |
| Junkie's (weapon) | Max +50% at 5 addictions | **Curve goes to +100% at 10 addictions** | MEDIUM |
| Mutant's (weapon) | +25% max at 5 mutations | **Curve goes to +50% at 10 mutations** | MEDIUM |
| Assassin's (armor) | -8% from players | **15% per piece in curve data** | MEDIUM |
| Overeater's | 6% per piece | **Curve shows up to 40 at max** | NEEDS ANALYSIS |
| Sentinel vs Cavalier | Both "15% reduction" | **Cavalier 10%/pc, Sentinel 5%/pc** | HIGH |

---

## WEAPON EFFECTS - Complete Reference

### 1st Star (Primary) Effects

#### S-TIER

**Bloodied** (`weapon_damageinversehealth`)
- +130% damage at 5% HP, +0% at 100% HP
- Linear interpolation: `bonus = 130 * (1 - hp_pct) / 0.95`
- At 20% HP (typical bloodied build): **~104% bonus**
- At 30% HP: ~91% bonus
- HIGHEST damage ceiling of any prefix

**Quad** (no curve - OMOD flat value)
- 4x magazine capacity
- No damage bonus, but massive DPS increase on slow-reload weapons
- Best in slot for Railway Rifle, Double Barrel, Pepper Shaker

**Vampire's** (no curve - OMOD flat value)
- Heal on every hit
- Best survivability prefix
- Pairs with fast fire rate for constant healing

#### A-TIER

**Anti-Armor** (flat 50% armor penetration)
- Consistent 50% armor ignore
- Best against high-DR enemies
- Multiplicative with other armor penetration effects

**Aristocrat's** (`weapon_damageviacaps`)
```
Caps     | Damage Bonus %
---------|---------------
0        | 0%
1,000    | 3%
2,000    | 5%
15,000   | 27%
17,000   | 30%
29,000   | 50% (MAX)
```
- Non-linear scaling, accelerates past 15k caps
- Easy to maintain at max with caps hoarding

**Junkie's** (`weapon_damageaddiction`)
```
Addictions | Damage Bonus %
-----------|---------------
1          | 10%
2          | 20%
3          | 30%
5          | 50%
10         | 100% (MAX)
```
- Linear +10% per addiction
- **Curve extends to 10 addictions** despite wiki saying max 5
- Actual practical max depends on available addictions in game

**Instigating** (flat 100% = double damage)
- Only to full-health targets
- Best for one-shot builds (sniper, melee)

#### B-TIER

**Mutant's** (`weapon_dmgwithmutation`)
```
Mutations | Damage Bonus %
----------|---------------
1         | 5%
5         | 25%
10        | 50% (MAX)
```
- Easy to maintain with Starched Genes
- Curve goes higher than wiki's "+25% max"

**Executioner's** (`weapon_execute`)
- Flat +50% to targets below 40% HP
- No scaling, always 50%
- Good for boss finishing

**Two Shot** (`weapon_damage`)
- Second projectile = 20% of base damage
- Total = 120% effective damage with accuracy loss
- Worse than most damage prefixes mathematically

**Gourmand's** (`weapon_gourmand`)
```
Satisfaction | Damage Bonus %
-------------|---------------
0            | 0%
2            | 10%
4            | 20%
6            | 30%
8 (MAX)      | 40%
```
- Up to +40%, much higher than wiki's +24%
- Easy to maintain with food/water

**Nocturnal** (`weapon_damagenight`)
```
Game Hour | Damage Bonus %
----------|---------------
0-5       | 50%
6-20      | 0%
21-24     | 50%
```
- **NO PENALTY during day** (contrary to wiki's -50%)
- +50% at night only
- Binary switch, no gradual transition

#### C-TIER

**Berserker's** (`weapon_damageunarmored`)
```
Player DR | Damage Bonus %
----------|---------------
0         | 50%
20        | 30%
40        | 17%
60        | 5%
```
- Requires no armor for full benefit
- High risk, mediocre reward

**All Creature-Type Slayers** (flat +50%)
- Hunter's, Exterminator's, Ghoul Slayer's, Troubleshooter's, Zealot's, Mutant Slayer's, Assassin's, Cryptid Hunter's
- All identical: flat +50% vs specified type
- Situational value only

**Damage Per Kill** (`weapon_damageperkill`)
- +10% per kill, max +100% at 10 kills
- Stacks reset on death/map change
- Good for mob clearing, useless vs bosses

#### SPECIAL

**Damage via Health** (`weapon_damageviahealth`)
- Linear: +0.1% per max HP point
- At 300 HP: +30%, at 500 HP: +50%, at 1000 HP: +100%
- Depends on achievable HP levels

**Damage via Carry Weight** (`weapon_dmgcarryweight`)
- No benefit below 200 carry weight
- +1% at 200, +50% at 350
- Linear between 200-350

### 2nd Star Effects

**Faster Fire Rate** (`weapon_guns_rof`)
- Flat +25% fire rate
- Confirmed 25%, not level-scaled
- S-TIER for DPS

**Faster Swing Speed** (`weapon_melee_swingspeed`)
- Flat +40% swing speed
- S-TIER for melee builds

**Explosive** (OMOD flat 20%)
- 20% of base damage as explosive AoE
- Legacy shotgun version is separate OMOD

**Limb Damage** (`weapon_dmglimbs`)
- Flat +50% limb damage

**Critical Damage** - +50% VATS crit damage

### 3rd Star Effects

**Reduced Weight** (`weapon_melee_weight`)
- Flat 90% weight reduction (-0.9 multiplier)
- Confirmed 90%

**Durability** (`weapon_durability`)
- 1.5x durability multiplier (+50% condition)

### 4th Star Effects (EXCLUSIVE)

**Charged Melee Attack** (`weapon_chargedmeleeattack`)
```
Charge Level | Damage Multiplier
-------------|------------------
1            | 0.5x
2            | 1.5x
3            | 3.0x
```
- Full charge = 3x damage. Massive burst potential.

**Cold Shoulder (Cryo)** (`weapon_cscryodamage`)
```
Base Damage | Cryo Added
------------|----------
1           | 44
10          | 50
25          | 63
50          | 91
```
- Highest elemental 4-star. 44-91 cryo damage.

**Fracturers (Explosive)** (`weapon_fracturersexplosiondmg`)
```
Base Damage | Explosion Added
------------|----------------
1           | 22
10          | 26
25          | 33
50          | 50
```

**Electricians (Energy)** (`weapon_electriciansenergydmg`)
```
Base Damage | Energy Added
------------|-------------
1           | 11
10          | 13
25          | 16.5
50          | 25
```

**Voltaic (Energy + EMP)** (`weapon_voltaicenergydmg` + `weapon_voltaicempdmg`)
- Energy: Same as Electricians (11-25)
- EMP: 40 per stack, up to 120 at 5 stacks
- PA exclusive

**Sane** (`weapon_sane`)
- +5% damage per sanity stack, max +40% at 8 stacks

**Reload/Melee Speed Per Kill** (`weapon_reloadmeleespeedperkill`)
- +3% per kill, max +30% at 10 kills

---

## ARMOR EFFECTS - Complete Reference

### 1st Star Effects

#### S-TIER

**Unyielding** (`armor_lowhealthincreasesstats`)
```
Health %   | SPECIAL Bonus (per piece)
-----------|-------------------------
0-19%      | +3
20-39%     | +2
40-59%     | +1
60-100%    | +0
```
- 5 pieces at <20% HP = **+15 to all SPECIAL (except END)**
- Unmatched utility for XP, carry weight (STR), VATS (AGI/LCK/PER)
- Does NOT exist for Power Armor (ZZZ_mod confirms disabled)

**Overeater's** (`armor_overeater`)
```
Satisfaction (0-8 scale) | Damage Reduction
-------------------------|------------------
0-1.6                    | 0%
2.0                      | 1%
3.6                      | 2%
4.0                      | 3%
4.8                      | 5%
5.6                      | 8%
6.0                      | 11%
6.4                      | 14%
6.8                      | 19%
7.2                      | 25%
7.6                      | 32%
8.0 (MAX)                | 40%
```
- Per piece at max satisfaction. Values are raw curve - game likely caps or divides.
- S-TIER for full health tank builds

#### A-TIER

**Bolstering** (`armor_bolstering_01` through `_05`)
- Multiplicative per piece. X = HP% (0-1), Y = damage multiplier
```
Piece Count | Multiplier at 0% HP | DR Bonus %
------------|--------------------|-----------
1           | 0.900              | 10.0%
2           | 0.810              | 19.0%
3           | 0.729              | 27.1%
4           | 0.656              | 34.4%
5           | 0.590              | 41.0%
```
- Kicks in below 75% HP
- Description curve shows "+10 DR/ER" per piece displayed in tooltip

**Vanguard's** (`armor_vanguard_01` through `_05`)
- Scales with current HP VALUE (not percentage). X = HP points.
```
Piece Count | Multiplier at 1000 HP | DR Bonus %
------------|----------------------|-----------
1           | 0.940                | 6.0%
2           | 0.884                | 11.6%
3           | 0.831                | 16.9%
4           | 0.781                | 21.9%
5           | 0.734                | 26.6%
```
- Max 26.6% at 5 pieces with high HP
- Weaker than Bolstering at extremes (26.6% vs 41%)
- But always-on at full health vs Bolstering's low-health requirement

**Heavyweight** (`armor_heavyweight_01` through `_05`)
- Scales with carry weight ratio (0 to 1.5, where >1.0 = overencumbered)
```
Piece Count | Multiplier at 1.5 ratio | DR Bonus %
------------|------------------------|-----------
1           | 0.900                  | 10.0%
2           | 0.810                  | 19.0%
3           | 0.729                  | 27.1%
4           | 0.656                  | 34.4%
5           | 0.590                  | 41.0%
```
- Same maximums as Bolstering
- Rewards carrying heavy loads

#### B-TIER

**Mutant's** (`armor_mutant` through `armor_mutant5`)
- X = mutation count, Y = damage multiplier
```
Mutations | 1pc Multi | 5pc Multi | 5pc DR Bonus %
----------|-----------|-----------|---------------
5         | 0.988     | 0.939     | 6.1%
10        | 0.960     | 0.815     | 18.5%
16 (max)  | 0.950     | 0.774     | 22.6%
```
- Diminishing returns past 10 mutations
- At 10 mutations + 5 pieces = 18.5% reduction

**Lucid** (`armor_lucid_01` through `_05`)
- Scales with radiation level (0-8 scale)
```
Rad Level | 1pc Multi | 5pc Multi | 5pc DR Bonus %
----------|-----------|-----------|---------------
4         | 0.987     | 0.938     | 6.2%
8 (MAX)   | 0.940     | 0.734     | 26.6%
```
- Identical max potential to Vanguard's (26.6% at 5pc)
- Newer Tempest-era effect

**Regenerating** (`armor_healthregen`)
- 0.5 HP/s per piece. 5 pieces = 2.5 HP/s.

#### SPECIAL

**Bolstering (Flat DR)** (`armor_resistancesinversehealth`)
```
Health % | Flat DR per piece
---------|------------------
0-10%    | +35
20%      | +32
30%      | +28
40%      | +24
50%      | +20
60%      | +16
61%+     | +0
```
- Separate flat DR backing. Max +35 per piece = +175 total at 5pc

**Vanguard (Flat DR)** (`armor_resistancesproportionalhealth`)
```
Health % | Flat DR per piece
---------|------------------
50%      | +7
60%      | +14
70%      | +21
80%      | +28
90%      | +35
```
- Max +35 per piece at 90%+ HP = +175 total at 5pc

**Aristocrat's (Armor DR)** (`armor_resistancesproportionalcaps`)
- Linear: +0.67 DR per 1000 caps
- Max +20.1 DR at 30,000 caps

**DR via Caps** (`armor_damageresistviacaps`)
```
Caps    | Flat DR
--------|-------
0       | 0
1,000   | 6
2,000   | 10
15,000  | 54
17,000  | 60
29,000  | 100
```

**Resistances Per Kill** (`armor_resistancesperkill`)
- +10 DR per kill, max +100 at 10 kills

### All Type-Specific Damage Reduction (1st Star)

All seven creature-type damage reductions use **identical curves**:
```
Pieces | Multiplier | Reduction %
-------|-----------|------------
1      | 0.85      | 15.0%
2      | 0.7225    | 27.75%
3      | 0.6141    | 38.59%
4      | 0.522     | 47.80%
5      | 0.4437    | 55.63%
```
Types: Animals, Bugs, Ghouls, Players, Robots, Scorched, Super Mutants

### 3rd Star Effects

**Cavalier's** (`armor_cavalier`) - Damage reduction while sprinting
```
Pieces | Multiplier | Reduction %
-------|-----------|------------
1      | 0.90      | 10.0%
2      | 0.81      | 19.0%
3      | 0.729     | 27.1%
4      | 0.6561    | 34.4%
5      | 0.59049   | 40.95%
```
- **DETERMINISTIC**, not 75% chance. Each piece = exactly 10% multiplicative.

**Sentinel's** (`armor_sentinel`) - Damage reduction while standing still
```
Pieces | Multiplier | Reduction %
-------|-----------|------------
1      | 0.95      | 5.0%
2      | 0.90      | 10.0%
3      | 0.86      | 14.0%
4      | 0.81      | 19.0%
5      | 0.77      | 23.0%
```
- **HALF the effectiveness of Cavalier's**
- 5pc Sentinel = 23% vs 5pc Cavalier = 41%
- NOT probabilistic despite wiki claims

**Weight Reductions** (all flat 20%):
- Weapons: `armor_weightweapons` = 20%
- Ammo: `armor_weightammo` = 20%
- Food/Drink/Chems: `armor_weightfooddrink` = 20%
- Junk: `armor_weightjunk` = 20%

**Damage to Melee Attackers** (3rd star):
```
Pieces | Burning | Electrified | Frozen | Toxic
-------|---------|-------------|--------|------
1      | 19      | 18          | 12     | 12
2      | 38      | 35          | 24     | 23
3      | 56      | 53          | 36     | 35
5      | 96      | 88          | 60     | 58
```
- Burning > Electrified > Frozen = Toxic

**Other 3rd Star**:
- Durability: 1.5x condition (+50%)
- Fall Damage: -50 flat reduction per piece
- Rads Regen: 0.25 rads/s per piece

### 4th Star Effects (EXCLUSIVE)

**Aegis** (PA only) (`armor_aegis_modincomingdmg`)
- +20 per piece, +100 at 5 pieces (incoming damage modifier value)

**Tanky** (armor + PA) (`armor_tanky_modincomingdmg`)
- +200 per piece, +1000 at 5 pieces
- 10x stronger than Aegis raw values

**Stalwart's** (PA only) (`armor_stalwarts_conditionbuff`)
- +5 condition buff per piece, +25 at 5 pieces

**Rejuvenator's** (PA only) (`armor_rejuvenatorregent1-5`)
- 5 tiers scaling: Tier 1 = 1/pc, Tier 5 = 6/pc (max 30 regen)

**Sane** (`armor_sane`)
- +1 per stack up to 4, then slower scaling, max 6 at 8 stacks

---

## DISABLED/REMOVED EFFECTS

### zzz_ Prefix (Disabled)

| Effect | ID | Why Notable |
|--------|-----|------------|
| Unyielding on PA | ZZZ_mod_Legendary_PowerArmor1_LowHealthIncreasesStats | **Confirms PA Unyielding was intentionally disabled** |
| Weightless on PA | zzz_mod_Legendary_PowerArmor1_Weightless | Weightless disabled for PA |
| Carry Weight DR | zzz_mod_Legendary_Armor1_ResistancesProportionalCarryWeight | Removed carry weight scaling |
| Weapon Carry Damage | zzz_mod_Legendary_Weapon1_DamageViaCarryWeight | Removed carry weight damage |
| 2x Ammo Capacity | zzz_mod_Legendary_Weapon1_Guns_AmmoCapacity2x | Double ammo removed (Quad stayed) |
| Radiation Damage | zzz_mod_Legendary_Weapon2_RadiationDamage | Rad damage on weapons removed |
| Armor Weight 3star | zzz_mod_Legendary_Armor3_Weight | Weight as 3rd star removed |
| Daredevils | zzz_mod_Legendary_Armor4_Daredevils | 4-star cut content |
| ReduceEnemyResists | zzz_mod_Legendary_Armor4_ReduceEnemyResists | Would have been OP |
| MaxAP | zzz_mod_Legendary_Armor4_MaxAP | Max AP as 4-star cut |
| CarryWeight 4star | zzz_mod_Legendary_Armor4_CarryWeight | Carry weight as 4-star cut |
| IncreaseAPRegen | zzz_mod_Legendary_Armor4_IncreaseAPRegen | AP regen as 4-star cut |
| Elusive | zzz_mod_Legendary_Armor4_Elusive | Evasion as 4-star cut |
| Elemental | zzz_mod_Legendary_Armor4_Elemental | Elemental resistance as 4-star cut |
| Collectors | zzz_mod_Legendary_Armor4_Collectors | Collector bonus cut |
| Slayers 4star | zzz_WIP4_mod_Legendary_Weapon4_Slayers | Slayer as 4-star cut |

### DEL_ Prefix (Deleted WIP)

These were Work-In-Progress 4th star effects that were deleted before release:
- SuperResilient, Duelists, Deadly, Stunning, Moneybags, AeroFlight, StaggerProof, Polished (duplicate), AutoRepair, Toppers

---

## BUILD OPTIMIZATION TABLES

### Best Bloodied Build (Max DPS)
| Slot | Effect | Benefit |
|------|--------|---------|
| Weapon 1star | Bloodied | +130% at 5% HP |
| Weapon 2star | FFR (ranged) / FSS (melee) | +25% / +40% |
| Weapon 3star | 25% Less VATS AP / 90% RW | DPS / QoL |
| Weapon 4star | Charged (melee) / Cold Shoulder (ranged) | 3x charge / +44-91 cryo |
| Armor 1star | Unyielding x5 | +15 all SPECIAL at <20% HP |
| Armor 2star | Powered x5 | AP regen |
| Armor 3star | Sentinel x5 / Cavalier x5 | 23% / 41% DR |

### Best Full Health Tank
| Slot | Effect | Benefit |
|------|--------|---------|
| Weapon 1star | Aristocrat's / Quad / Vampire's | +50% / 4x mag / sustain |
| Weapon 2star | FFR / Explosive | +25% / +20% AoE |
| Armor 1star | Overeater's x5 | Up to 40% DR per piece (raw) |
| Armor 2star | Powered x5 | AP regen |
| Armor 3star | Cavalier's x5 | 41% DR while sprinting |

### Best PA Build
| Slot | Effect | Benefit |
|------|--------|---------|
| Armor 1star | Overeater's x5 | High DR at full food |
| Armor 2star | Powered / +1 STR | AP or carry |
| Armor 3star | Cavalier's x5 | 41% DR sprinting |
| Armor 4star | Tanky x5 | +1000 incoming damage modifier |
| Note | NO Unyielding | **Intentionally disabled for PA** |

---

## LEGENDARY ECONOMY

### Scrip Values (identical across all categories)
| Stars | Scrip |
|-------|-------|
| 1     | 1     |
| 2     | 2     |
| 3     | 4     |
| 4     | 6     |

### Sell Values (caps)
| Stars | Armor | Power Armor | Weapons |
|-------|-------|-------------|---------|
| 1     | 3     | 10          | 5       |
| 2     | 9     | 20          | 15      |
| 3     | 24    | 45          | 40      |
| 4     | 30    | 55          | 50      |

---

## MATHEMATICAL NOTES

### Multiplicative vs Additive Stacking

The curve data reveals that most armor effects stack **multiplicatively**, not additively:
- Each Bolstering piece multiplies by 0.9: 5 pieces = 0.9^5 = 0.59 (not 0.5)
- Each creature-type reduction is 0.85: 5 pieces = 0.85^5 = 0.4437 (not 0.25)
- Cavalier's is 0.9 per piece: 5 pieces = 0.9^5 = 0.59 (not 0.5)

This means the **marginal value of each additional piece decreases**. The 1st piece gives the most benefit, the 5th piece the least (in absolute terms).

### Sentinel vs Cavalier Asymmetry

This is the most surprising finding. Despite being presented as equivalent in-game:
- **Cavalier's**: 10% multiplicative per piece (5pc = 41% total)
- **Sentinel's**: ~5% per piece (5pc = 23% total)

Sentinel is roughly HALF as effective as Cavalier's. This is likely an intentional balance decision since standing still is easier to maintain than sprinting.

### Bloodied Damage Curve

The Bloodied weapon curve is simple linear interpolation:
```
bonus_pct = 130 * (1 - current_hp_pct) / 0.95
```
At the typical "nerd rage" threshold of 20% HP: bonus = ~109%
At the typical "safe low health" of 30%: bonus = ~96%

Combined with Unyielding armor (+15 SPECIAL), Bloodied builds mathematically dominate all alternatives in the game data.

---

## DATA FILES

- Full JSON database: `~/ai-drive/gamecryptids/data/fallout76/legendary_effects.json` (175 KB)
  - Contains all raw curve data, interpretations, key values, wiki comparisons
  - Importable into any database or build planner
  - Includes `raw_curves` section with every data point from all 108 curve files
- Source curves: `tempest_data/misc/curvetables/json/legendarymods/` (108 files)
- OMOD records: `esm_dump/OMOD_records.txt` (32,677 records)
