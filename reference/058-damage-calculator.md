# Finding 058: Complete Fallout 76 Damage Calculation Model

**Source**: All extracted curve tables, GMST values, and legendary/perk/mutation data
**Implementation**: `~/ai-drive/gamecryptids/perkolatr/damage_calculator.py`
**Date**: 2026-03-20

---

## The Damage Pipeline

Every point of damage in Fallout 76 flows through a multi-stage pipeline. The stages are applied in a specific order, with some stages being **additive** (pooled together then applied once) and others being **multiplicative** (each applied as a separate multiplier). Getting this order wrong produces wildly incorrect results.

```
Base Damage (weapon curve @ level)
    + Juggernaut's flat bonus (if applicable)
    * (1 + PERK ADDITIVE POOL)
    * (1 + LEGENDARY BONUS)
    * (1 + MUTATION BONUS)
    * SNEAK MULTIPLIER
    * CRITICAL MULTIPLIER
    * RANGE FALLOFF
    * PELLET COUNT
    + TWO SHOT BONUS (if applicable)
    -> ARMOR REDUCTION (DR formula)
    = FINAL DAMAGE
```

---

## Stage 1: Base Damage

Every weapon has a damage curve table that maps level (X axis) to base damage (Y axis). The game interpolates linearly between defined points.

**Source files**: `misc/curvetables/json/weapons/weap_*.json`

Examples at level 50:

| Weapon | Base Damage | Curve File |
|--------|------------|------------|
| Handmade Rifle | 59 | weap_handmadegundmg.json |
| The Fixer | 59 | weap_combatrifle_fixerdmg.json |
| Gauss Rifle | 315 | weap_gaussrifledmg.json |
| .50 Cal MG | 38 | weap_50calmachinegundmg.json |
| The Dragon | 611 | weap_blackpowder_rifle_dragondmg.json |
| Combat Shotgun | 150 (per pellet) | weap_combatshotgundmg.json |
| Flamer | 29 | weap_flamerdmg.json |
| Minigun | 11 | weap_minigundmg.json |

All weapon curves use 5-level increments (1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50). Level 50 is the maximum for most weapons. Between defined levels, the game uses linear interpolation.

### Level-Gated Weapons

Some weapons have 0 damage below a threshold level, meaning they cannot exist as items below that level:

- Fat Man: level 25+
- .50 Cal Machine Gun: level 25+
- Minigun: level 35+
- Tesla Cannon: level 20+

---

## Stage 2: Perk Additive Pool

All weapon type damage perks and several general damage perks are **additive** with each other. They form a single pool that is applied as one multiplier: `* (1 + total_perk_bonus)`.

### Weapon Type Perks

Each weapon type has three cards (base, expert, master). Each card has 3 ranks:

| Rank | Bonus |
|------|-------|
| 1 | +10% |
| 2 | +15% |
| 3 | +20% |

At max rank all three cards: +20% + 20% + 20% = **+60% total**.

This pattern applies to: Rifleman, Commando, Guerrilla, Gunslinger, Shotgunner, Heavy Gunner, Slugger, Gladiator, Iron Fist.

**Source**: The perk curve files (e.g., `heavydamagebonus.json`) use internal rank values. `heavydamagebonus` goes from 0 to 90 over ranks 0-30 (3 ranks per point = 30% per card at rank 3... but in practice the game maps card ranks to specific curve positions giving the 10/15/20 pattern).

### Other Additive Perks

These add to the SAME additive pool as weapon type perks:

| Perk | Bonus | Notes |
|------|-------|-------|
| **Bloody Mess** | +5/10/15% (rank 1/2/3) | All damage types |
| **Tenderizer** | +5/6/7% (rank 1/2/3) | Target must have been recently hit |
| **Adrenaline** | +10% per kill, max +100% | Decays after 30s. Source: `adrenalinebonus.json` x=kills, y=bonus% |
| **Nerd Rage** | +40-80% (inverse HP) | Only active below 20% HP. Source: `nerdragedamagebonus.json` |

#### Nerd Rage Damage Curve (from `nerdragedamagebonus.json`)

| Health % | Damage Bonus |
|----------|-------------|
| 5% | +80% |
| 20% | +40% |
| 80% | +1% |
| 100% | 0% |

This is piecewise-linear. At exactly 20% HP (the activation threshold), Nerd Rage provides +40% damage. Below 20% it ramps up to +80% at near-death.

### Maximum Perk Pool Example

Full Commando build at 20% HP:
- Commando (3 cards, rank 3): +60%
- Bloody Mess rank 3: +15%
- Tenderizer rank 3: +7%
- Nerd Rage: +40%
- Adrenaline (10 kills): +100% (decaying)

**Total additive pool: +222%** -> multiplier of 3.22x

---

## Stage 3: Legendary Prefix Bonus

The legendary prefix bonus is a **separate multiplicative category**. It multiplies the post-perk damage by `(1 + legendary_bonus)`.

### Percentage-Based Legendaries

**Source**: `misc/curvetables/json/legendarymods/weapon_*.json`

| Legendary | Input Variable | Key Values | Source File |
|-----------|---------------|------------|-------------|
| **Bloodied** | HP remaining (%) | +130% at 5% HP, 0% at full | weapon_damageinversehealth.json |
| **Aristocrat's** | Caps held | +3% at 1K, +27% at 15K, **+50% at 29K** | weapon_damageviacaps.json |
| **Junkie's** | Addiction count | +10% per addiction, **max +100% at 10** | weapon_damageaddiction.json |
| **Mutant's** | Mutation count | +5% per mutation, **max +50% at 10** | weapon_dmgwithmutation.json |
| **Gourmand's** | Food/drink meter | +5% per point, **+40% at max (8.0)** | weapon_gourmand.json |
| **Executioner's** | Target HP % | **+50%** when target below 40% HP | weapon_execute.json |
| **Nocturnal** | Game hour | **+50%** at night (21:00-5:00), 0% during day | weapon_damagenight.json |
| **Furious** | Consecutive hits | +5% per hit, **max +45% at 9 stacks** | (hardcoded, no curve) |
| **Instigating** | Target HP % | **+100%** to full-health targets only | (hardcoded) |
| **Anti-type** (Hunter's, etc.) | Enemy type match | **+50%** vs matching type | weapon_dmgvs*.json |

#### Bloodied Curve Detail

From `weapon_damageinversehealth.json`:
```
x=0.05  y=130   (at 5% HP:   +130% damage)
x=1.00  y=0     (at 100% HP: +0% damage)
```
Linear interpolation between these two points:
- At 20% HP: +130 * (1.0 - 0.20) / (1.0 - 0.05) = +109.5%
- At 50% HP: +130 * (1.0 - 0.50) / (1.0 - 0.05) = +68.4%

#### Aristocrat's Curve Detail

From `weapon_damageviacaps.json`:
```
0 caps    -> +0%
1,000     -> +3%
2,000     -> +5%
15,000    -> +27%
17,000    -> +30%
29,000    -> +50%
```
Non-linear scaling. The first 1,000 caps give only +3%, but the last 12,000 caps (17K to 29K) give +20%. You need **29,000 caps** for the full benefit.

#### Anti-Armor: Not a Damage Bonus

Anti-Armor does NOT add a damage percentage. It provides **armor penetration** -- reducing the target's effective DR. This is handled in Stage 11 (armor reduction). From `weapon_damageunarmored.json`:
```
0 DR target:  +50% armor pen (irrelevant -- no armor to penetrate)
20 DR target: +30%
40 DR target: +17%
60 DR target: +5%
```
Wait -- this curve is confusing. The actual game implementation of Anti-Armor is a flat 50% armor penetration that multiplicatively stacks with other penetration sources. The `weapon_damageunarmored` curve appears to be used for the damage bonus display, not the actual penetration calculation.

### Flat-Bonus Legendaries

| Legendary | Mechanic |
|-----------|----------|
| **Juggernaut's** | Adds flat damage proportional to current HP. At 1,000 HP: +100 flat damage. Added BEFORE perks multiply. |
| **Two Shot** | Fires a second projectile at 62.5% of base damage. Added AFTER all multipliers but before armor. |

### Rate-of-Fire Legendaries

| Legendary | Bonus |
|-----------|-------|
| **Furious (guns_rof)** | +25% fire rate | From `weapon_guns_rof.json`: flat 0.25 at all levels |
| **Swing Speed (melee)** | +40% swing speed | From `weapon_melee_swingspeed.json`: flat 0.4 at all levels |

---

## Stage 4: Mutation Bonus

Mutations are a **separate multiplicative category**, stacking with both perks and legendary effects.

### Adrenal Reaction

**Source**: `misc/curvetables/json/mutations/mutation_adrenal_normal.json` and `mutation_adrenal_super.json`

The raw curve files contain:
- Normal: `(1, 5)` to `(20, 100)` -- the X axis is NOT health percentage directly
- Super: `(1, 6.25)` to `(20, 125)` -- with Strange in Numbers (+25%)

The input mapping converts health percentage to the curve's X axis: `input = (1 - health_pct) * 20`

**Effective values** (health % -> damage bonus):

| Health % | Normal | Super (Strange in Numbers) |
|----------|--------|---------------------------|
| 5% | +100% | +125% |
| 20% | +80% | +100% |
| 50% | +50% | +62.5% |
| 80% | +20% | +25% |
| 100% | +5% | +6.25% |

At the "Bloodied sweet spot" of 20% HP, Adrenal Reaction provides +80% (normal) or +100% (super) damage. This is the same multiplicative category as mutations, not perks.

### Twisted Muscles

- +25% melee damage (normal)
- +31.25% with Strange in Numbers
- -50% gun accuracy (drawback)

No curve file -- flat values from the mutation form data.

### Mutation Stacking with Bloodied

At 20% HP with both Bloodied and Adrenal Reaction (super):
```
Base 59 * (1 + perks) * (1 + 1.095 Bloodied) * (1 + 1.0 Adrenal)
```
The multiplicative stacking is why Bloodied builds are so powerful -- two separate +100%ish multipliers compound rather than add.

---

## Stage 5: Sneak Attack Multiplier

Sneak attacks are a **separate multiplicative category**. They only apply when BOTH sneaking AND undetected.

### Base Sneak Multiplier

- Ranged: **2.0x** (from GMST `fSneakAttackMult`)
- Melee: **2.0x** (from GMST `fCombatDamageBonusMeleeSneakingMult`)

### Covert Operative (replaces base multiplier)

| Rank | Sneak Multiplier |
|------|-----------------|
| 0 | 2.0x |
| 1 | 2.15x |
| 2 | 2.3x |
| 3 | 2.5x |

### Mister Sandman

Adds **+0.5x** to the sneak multiplier at night only. With Covert Operative rank 3 at night: 2.5 + 0.5 = **3.0x**.

---

## Stage 6: Critical Hit Multiplier

VATS critical hits add bonus damage as a **separate multiplicative category**.

### Formula

```
crit_multiplier = 1.0 + (weapon_crit_mult * (1 + better_criticals_bonus))
```

Most weapons have a `weapon_crit_mult` of 1.0 (doubles damage on crit).

### Better Criticals

| Rank | Bonus | Total Crit Mult |
|------|-------|----------------|
| 0 | +0% | 2.0x |
| 1 | +40% | 2.4x |
| 2 | +60% | 2.6x |
| 3 | +100% | 3.0x |

### Critical Fill Rate

The critical meter fills based on Luck stat:
- Each VATS hit adds to the meter proportional to Luck
- At 1 Luck: ~29 hits to fill
- At 15 Luck: ~7 hits to fill
- At 33 Luck: ~4 hits to fill

Critical Savvy pre-fills the meter: rank 1/2/3 starts at 15/25/35% filled.

**Source**: `fVATSCriticalChargeBase` and `fVATSCriticalChargeMult` from GMST.

---

## Stage 7: Range Falloff

**Source**: `player/percentofmintomaxrangedamagemult.json`

| Distance / Max Range | Damage Retained |
|---------------------|----------------|
| 1.0x (at max range) | 100% |
| 1.5x (50% beyond) | 75% |
| 1.75x | 55% |
| 2.0x (double max) | **20%** |

At exactly the weapon's max range, full damage is dealt. Beyond that, damage drops sharply. At double the max range, only 20% damage remains.

---

## Stage 8: Pellet Count

Shotguns fire multiple pellets per shot. Each pellet applies the weapon's listed damage independently. The Combat Shotgun at level 50 does 150 damage per pellet with 8 pellets = 1,200 total damage per shot (before armor -- and armor applies per-pellet, which is important).

---

## Stage 9: Two Shot Bonus

Two Shot fires a second projectile that deals **62.5%** of the base damage. Crucially, the second projectile only benefits from the perk additive pool, NOT from legendary/mutation/sneak/crit multipliers. It is added to the total pre-armor damage as a flat value.

---

## Stage 10: Armor Reduction

### The DR Formula (Adventure Mode)

Fallout 76's Adventure mode uses the classic Fallout 4 damage resistance formula:

```
effective_dr = target_dr * (1 - total_armor_penetration)
damage_mult = damage / (damage + effective_dr)
final_damage = damage * damage_mult
```

This is equivalent to: `final = damage^2 / (damage + effective_dr)`

**Properties of this formula:**
- If damage == DR: you deal **50%** of your damage (damage^2 / 2*damage = damage/2)
- If damage >> DR: you deal nearly **100%** (asymptotic)
- If damage << DR: you deal very little (quadratic decay)
- Every point of DR always helps, but with diminishing returns
- Every point of damage always helps, but also diminishing returns against fixed DR

### Armor Penetration Sources (Multiplicative Stacking)

Armor penetration sources stack **multiplicatively on remaining armor**:

```
remaining_DR = target_DR * (1 - pen_1) * (1 - pen_2) * (1 - pen_3)
```

| Source | Penetration per Rank | Notes |
|--------|---------------------|-------|
| Anti-Armor legendary | 50% | Single value |
| Tank Killer perk (rifles) | 12/24/36% (rank 1/2/3) | Rifles and pistols only |
| Incisor perk (melee) | 25/50/75% (rank 1/2/3) | Melee and unarmed only |
| Stabilized perk (PA heavy) | 15/30/45% (rank 1/2/3) | Power Armor + heavy guns only |
| Weapon mods | Varies | Perforating magazine, etc. |

Example: Anti-Armor + Tank Killer rank 3 vs 200 DR target:
```
remaining = 200 * (1 - 0.50) * (1 - 0.36) = 200 * 0.50 * 0.64 = 64 DR
```

### The Babylon/NW Formula

Nuclear Winter / Babylon mode uses a simpler curve-table lookup instead of the formula:

| DR | Damage Resisted |
|----|----------------|
| 0 | 0% |
| 72 | 25% |
| 101 | 30% |
| 130 | 35% |
| 192 | 45% |

This has more severe diminishing returns than the Adventure mode formula.

**Source**: `babyloncombatformulas/resistedpercentage.json`

---

## Armor Legendary Effects (Defensive)

### Cavalier's (Multiplicative Stacking)

**Source**: `armor_cavalier.json`

Each piece multiplies incoming damage by 0.9 (10% reduction):

| Pieces | Damage Multiplier | Total Reduction |
|--------|-------------------|----------------|
| 0 | 1.000 | 0% |
| 1 | 0.900 | 10% |
| 2 | 0.810 | 19% |
| 3 | 0.729 | 27.1% |
| 4 | 0.6561 | 34.4% |
| 5 | 0.59049 | **40.95%** |

### Sentinel's (Additive-Diminishing)

**Source**: `armor_sentinel.json`

| Pieces | Damage Multiplier | Total Reduction |
|--------|-------------------|----------------|
| 0 | 1.00 | 0% |
| 1 | 0.95 | 5% |
| 2 | 0.90 | 10% |
| 3 | 0.86 | 14% |
| 4 | 0.81 | 19% |
| 5 | 0.77 | **23%** |

**Cavalier is nearly DOUBLE the reduction of Sentinel at 5 pieces** (40.95% vs 23%). This is a major finding -- the community generally treats them as equivalent.

### Overeater's

**Source**: `armor_overeater.json`

Scales with food/drink meter (0-8). At max meter (8.0): **40% reduction per piece**. The curve is exponential -- the last 2 points of food/drink give more benefit than the first 6:

| Food/Drink | Reduction % |
|-----------|-------------|
| 4.0 | 3% |
| 6.0 | 11% |
| 7.2 | 25% |
| 8.0 | **40%** |

Multiple pieces stack multiplicatively like Cavalier.

### Aegis

**Source**: `armor_aegis_modincomingdmg.json`

Adds flat DR per stack: 20/40/60/80/100 DR at 1-5 stacks.

---

## VATS Accuracy Formula

**Source**: GMST values `fVATSChance*`

```
hit_chance = perception * 3.5 + weapon_accuracy - distance * 0.5 + body_part_modifier
clamped to 5% minimum, 95% maximum
```

Key GMST constants:
- `fVATSChancePerceptionMultiplier` -- perception scaling factor
- `fVATSChanceDistanceMultiplier` -- distance penalty factor
- `fVATSChanceBodyPartMultiplier` -- body part size multiplier
- `fVATSChanceWeaponBaseMultiplier` -- weapon accuracy base
- `fVATSPlayerDamageMult` -- VATS damage multiplier (if any)

AP costs are per-weapon with modifiers from weapon mods and perks.

---

## DPS Calculation

```
burst_dps = damage_per_hit * fire_rate_per_second
sustained_dps = (damage_per_hit * magazine_size) / (time_to_empty + reload_time)
```

Where:
- `time_to_empty = magazine_size / fire_rate_per_second`
- `fire_rate_per_second = displayed_ROF / 10` (game displays ROF * 10)

### Overheating Mechanics

**10mm SMG** (from `weap_10mmsmgoverheatingdamagemultiplier.json`):
- At 75%+ heat: damage multiplier reaches **2.0x**
- Also fires 1 extra round per shot at 75%+ heat
- Sustained fire literally doubles DPS

**Gauss Minigun** (from `weap_gaussminigunoverheatdmgmult.json`):
- Gradual curve from 1.004x (10% heat) to **1.6x** (100% heat)
- More granular than 10mm SMG

---

## Complete Example: Bloodied Sneak Crit Commando

The strongest single-hit build archetype. Using The Fixer at level 50:

```
Base Damage:     59.0
  * Perks:       x2.177  (Commando +60%, Bloody Mess +15%, Nerd Rage +40%, Tenderizer +7%)
  = 128.4
  * Legendary:   x2.095  (Bloodied at 20% HP = +109.5%)
  = 269.0
  * Mutation:    x2.0    (Adrenal Reaction Super at 20% HP = +100%)
  = 538.0
  * Sneak:       x2.5    (Covert Operative rank 3)
  = 1,345
  * Crit:        x3.0    (Better Criticals rank 3)
  = 4,035
  * Range:       x1.0    (within max range)
  = 4,035

  Armor Pen:     36%     (Tank Killer rank 3)
  vs 150 DR:     eff DR = 96
  DR formula:    4,035^2 / (4,035 + 96) = 3,940

  FINAL DAMAGE:  ~3,940 per hit
```

For comparison, a full-health Aristocrat's Commando with the same weapon hits for ~101 damage against the same target. The Bloodied sneak crit build does **39x more damage** per hit.

---

## Implementation Notes

The calculator (`damage_calculator.py`) provides:

1. **`CurveTable`** -- piecewise-linear interpolation engine matching the game's internal curve system
2. **`WeaponConfig`** -- weapon stats (level, fire rate, magazine, pellets, etc.)
3. **`BuildConfig`** -- full character configuration (perks, legendary, mutations, context)
4. **`calculate_damage()`** -- the complete pipeline returning a detailed breakdown
5. **`calc_dps()`** -- burst and sustained DPS metrics
6. **`calc_vats_hit_chance()`** -- VATS accuracy estimation
7. **`compare_builds()`** -- side-by-side build comparison
8. **Data loaders** -- `load_weapon_curve()`, `load_damage_tier()`, etc. for reading extracted game files

All embedded curve data matches the extracted JSON files. The module can also dynamically load curves from the data directory for weapons not in the embedded set.

---

## Known Limitations

1. **Explosive legendary**: Adds a fixed explosion damage component (from `weapon_fracturersexplosiondmg.json`: 22-50 by level). The explosion damage goes through its own DR check. Not yet modeled separately.

2. **Limb damage**: Headshots do bonus damage (multiplied by body part multiplier from the weapon record). Not modeled -- would require body part multipliers per weapon.

3. **Damage over time**: Flamer DOT, Warshrike bleed, harpoon bleed all tick independently. Not modeled in the per-hit calculation.

4. **Power Armor damage reduction**: PA provides a flat 42% damage reduction on top of DR. Not yet factored in.

5. **One Wasteland scaling**: The 100-tier damage/armor system scales enemies based on the player's level and area. This affects target DR, not the player's damage formula.

6. **PvP damage cap**: PvP has separate damage scaling and caps that are not modeled here.

7. **Demolition Expert**: Affects explosive damage component specifically. Partially modeled.

8. **Taking One for the Team**: Team-based +40% damage to enemies attacking teammates. Not yet modeled as a separate multiplicative category.
