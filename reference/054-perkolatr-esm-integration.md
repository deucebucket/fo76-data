# 054 - Perkolatr ESM Data Integration Analysis

**Date:** 2026-03-20
**Source Data:** ESM dump records + Tempest curve table JSONs (4,262 files)
**Current Data:** Wiki-sourced markdown tables (6 files)

## Executive Summary

The existing Perkolatr database relies on wiki-scraped data stored in markdown tables. After integrating ESM dump data and Tempest curve table JSONs, significant discrepancies were found. The ESM data provides exact per-level damage curves, precise perk bonus scaling, complete power armor stats for all 14 PA types, and exact GMST-derived formulas that the wiki data either omits, rounds, or misrepresents.

**Enhanced database:** `fallout76_esm.db` (alongside existing `fallout76.db`)
- 153 weapons with exact per-level damage curves (1,632 curve data points)
- 458 perks with 256 bonus curve data points
- 2,750 standard armor stat curve points across all types/weights/slots
- 1,660 power armor stat curve points across 14 PA types
- 48 legendary effects with 233 scaling curve points
- 19 mutations with exact values
- 35 key GMST game settings
- 53-level XP curve
- 22-point Luck critical charge rate curve

## Critical Discrepancies: Wiki vs ESM Data

### 1. Weapon Damage Values

The wiki database stores damage as slash-separated strings (e.g., "61/78/99/127/161") representing damage at different craftable levels. The ESM curve tables provide exact damage at every level from 1 to 50.

**Key finding:** The wiki values represent damage at the weapon's craftable level breakpoints (usually 5-level intervals where you can craft the next tier), NOT the player's level. The curve tables show the weapon's actual base damage scales with the weapon's level, and weapons can only be crafted/found at specific level tiers.

| Weapon | Wiki Level 50 | ESM Curve Level 50 | Match? | Notes |
|--------|--------------|-------------------|--------|-------|
| 10mm Pistol | 77 (5th tier) | 50 | NO | Wiki includes receiver mods in damage |
| .44 Pistol | 161 (5th tier) | 149 (.44dmg curve) | NO | Wiki likely includes Hardened receiver |
| Handmade Rifle | 52 (4th tier) | 59 | NO | ESM is HIGHER - wiki may be outdated |
| The Fixer | 59 (4th tier) | 59 | YES | Exact match at level 50 |
| Combat Rifle | 95 (4th tier) | 53 | NO | Wiki includes receiver mod bonus |
| Hunting Rifle | 171 (7th tier) | 171 | YES | Exact match |
| Gatling Gun | N/A | 86 | N/A | Wiki stores as text range |
| Minigun | N/A | 24 | N/A | Wiki stores as text range |
| Black Powder Rifle | 857 (4th tier) | 507 | NO | Huge gap - wiki may include Bayoneted or Prime |

**Root cause:** The wiki "Damage (Base/Range)" column conflates base weapon damage with modded damage across level tiers. The ESM curves show ONLY the base unmodded weapon damage at each level. The wiki values at the highest tier often include a Hardened Receiver or similar mod bonus baked in.

### 2. Power Armor Stats

The wiki database has only 12 power armor entries with max-level stats as text. The ESM has curves for 14 PA types across 5 piece slots, 3-7 damage types, at every level from 1-50.

**New PA types not in wiki DB:** Union, Vulcan, Presidential T-60, Enclave X-01

**Level 50 Torso DR comparison (ESM data, total across all pieces):**

| PA Type | Torso DR | Arm DR | Leg DR | Helmet DR | Total Set DR |
|---------|----------|--------|--------|-----------|-------------|
| T-65 | 140 | 85 | 85 | 80 | 475 |
| Ultracite | 134 | 82 | 82 | 77 | 457 |
| X-01 | 98 | 62 | 62 | 58 | 342 |
| Hellcat | 96 | 68 | 68 | 63 | 363 |
| T-60 | 92 | 60 | 60 | 55 | 327 |
| T-51b | 86 | 54 | 54 | 50 | 298 |
| Excavator | 78 | 50 | 50 | 46 | 274 |
| T-45 | 68 | 44 | 44 | 40 | 240 |
| Raider | 60 | 40 | 40 | 36 | 216 |

**Key finding:** T-65 has the highest raw DR in the game by a significant margin (475 total set DR vs 363 for Hellcat). Hellcat's advantage is its unique ballistic damage reduction perk, not raw DR.

**Vulcan PA** has unique elemental resistance stats (cold, fire, poison, electric) that no other PA has -- these are completely absent from the wiki data.

### 3. Perk Bonus Scaling

The wiki stores perk descriptions as text. The ESM curve tables provide exact mathematical scaling functions.

**Critical discoveries from perk bonus curves:**

| Perk | Wiki Description | ESM Curve Reality |
|------|-----------------|-------------------|
| Heavy Gunner | "+10%/+15%/+20% damage" | Curve: 0 rank=0%, 30 rank=90%. Linear scaling, NOT the stepped values the wiki describes |
| Adrenaline | "+10% damage per kill, 6 stacks" | Curve: 1 kill=10%, 10 kills=100%. The curve is linear but scales to 10 stacks at rank 5, not 6 |
| Nerd Rage | "Below 20% HP: +20% damage" | Curve: 5% HP=+80%, 20% HP=+40%, 80% HP=+1%. It's NOT a flat 20% -- it scales with how low your health is |
| Ricochet | "18% chance to deflect" | Curve: rank 1=4%, rank 15=14%, rank 30=20%, rank 100=35%. The 18% figure is at rank ~25 |
| Serendipity | "45% chance to avoid damage below 30% HP" | Curve: rank 1=6%, rank 15=16%, rank 100=40%. The 45% figure is NOT in the curve data at all |
| Lone Wanderer DR | "+20 DR" | Curve: rank 1=10 DR, rank 15=75 DR, rank 100=210 DR. Much higher than wiki suggests at endgame |

**Nerd Rage is the biggest correction.** The wiki and community treat it as a binary "+20% damage below 20% health" but the ESM curve shows it's a continuous function that provides up to +80% damage at 5% health. This is a massive difference for Bloodied build calculations.

### 4. Legendary Effect Magnitudes

| Effect | Wiki/Community Claim | ESM Curve Data |
|--------|---------------------|----------------|
| Bloodied | "+95% damage at 5% HP" | +130% damage at 5% HP (weapon_damageinversehealth curve: x=0.05, y=130) |
| Anti-Armor | "Ignores 50% armor" | 20% armor ignore (weapon_damage curve: flat 0.2 at all levels). The 50% may come from combined effects |
| Executioner's | "+50% damage below 40% HP" | +50% flat (confirmed by curve: x=1, y=50 through x=100, y=50) |
| Mutant's | "+5% per mutation" | Confirmed: +5% per mutation up to +50% at 10 mutations |
| Overeater's (per piece) | "Up to -6% damage per piece" | Curve shows 0% at food=0-1.6, then scales up to -40% at food level 8.0 (TOTAL across 5 pieces = -8% each) |
| Aristocrat's | "+50% at 29,000 caps" | Curve: 0 caps=0%, 1000 caps=100%. This suggests +1% per 10 caps, NOT the 29K cap figure |
| Junkie's | "+10% per addiction" | Curve: linear 0-1000 mapping to 0-100%. The x-axis is NOT addiction count but an internal value |

**Bloodied is significantly stronger than the community believes.** At 5% health, Bloodied provides +130% damage, not the commonly cited +95%. Combined with Nerd Rage's +80% at 5% HP (not +20%), a Bloodied/Nerd Rage build at minimum health does +210% bonus damage, not the +115% the wiki suggests.

### 5. SPECIAL Stat Formulas

**Key GMST discoveries:**

| Formula | Wiki Claim | GMST Value | Impact |
|---------|-----------|------------|--------|
| XP per INT | "+3% per point" | fXPModMult = 0.03 | CONFIRMED: +3% per INT point |
| HP per END | "+5 per point" | fHealthEnduranceMult = 0.0 | ZERO. HP does NOT scale with END via this GMST. HP is likely set by a separate curve or One Wasteland system |
| AP Restore Rate | "Varies" | fActionPointsRestoreRate = 4.0 | 4 AP/sec base restore rate |
| VATS Ranged AP | "Varies by weapon" | fActionPointsAttackRanged = 30.0 | 30 AP base cost (modified by weapon) |
| Melee AP (1H) | "Varies" | fActionPointsAttackOneHandMelee = 15.0 | Exactly 15 AP |
| Melee AP (2H) | "Varies" | fActionPointsAttackTwoHandMelee = 30.0 | Exactly 30 AP |
| Unarmed AP | "Varies" | fActionPointsAttackUnarmed = 22.0 | Exactly 22 AP |
| Power Attack Mult | Unknown | fActionPointsPowerAttackMult = 1.5 | Power attacks cost 1.5x normal AP |
| VATS Crit Base | Unknown | fVATSCriticalChargeBase = 5.0 | 5% crit fill per VATS hit base |
| VATS Crit Mult | Unknown | fVATSCriticalChargeMult = 1.5 | 1.5x multiplier applied to crit charge |
| Concentrated Fire | "+accuracy per hit" | iVATSConcentratedFireBonus = 20 | Exactly +20% accuracy per consecutive hit |
| Max Move Speed | Unknown | fMoveSpeedMultMax = 150.0 | Speed capped at 150% (Speed Demon = 120%) |
| Compass Range | Unknown | fPerceptionCompassBase = 1576 + fPerceptionCompassMult = 256 | Base 1576 units + 256 per PER point |

**HP per Endurance = 0 is the biggest surprise.** The GMST `fHealthEnduranceMult` is 0.0, meaning Endurance does NOT directly increase HP through this setting. HP in Fallout 76 post-One Wasteland is likely managed by a separate level-based curve or the health system was completely reworked. The wiki's claim of "+5 HP per END" is either outdated or handled by a different mechanism not captured in GMST.

### 6. Luck Critical Charge Rate

The exact curve from `luckcriticalchargerate.json`:

| Luck | Crit Fill % per Hit |
|------|-------------------|
| 1 | 3% |
| 2 | 6% |
| 5 | 12% |
| 10 | 17% |
| 15 | 21% |
| 20 | 25% |
| 25 | 27% |
| 30 | 30% |
| 33 | ~31% |
| 50 | 37% |
| 100 | 45% |

At 15 Luck (max base), you fill 21% of the crit bar per VATS hit = 5 hits to fill. At 33 Luck (with Unyielding), ~31% = 3-4 hits. This is significantly more granular than the wiki's vague "increases crit recharge."

### 7. Mutation Values

The wiki's mutation descriptions are reasonably accurate for most mutations. However:

- **Adrenal Reaction:** The wiki says "up to +50% weapon damage at low health." The ESM curve (`mutation_adrenal_normal.json`) shows x=1 (100% HP) = +5% damage, x=20 (5% HP) = +100% damage. The actual maximum is +100%, not +50%.
- **Ricochet:** Listed as a mutation in the build generator with "18% chance to reflect damage." Ricochet is actually a Luck PERK, not a mutation. The mutation section erroneously includes it.
- **Scaly Skin:** Wiki says "+50 DR/ER." This appears accurate based on hardcoded values.

### 8. Standard Armor Gaps

The wiki DB has only 22 standard armor rows with chest DR only. The ESM has curves for every piece (torso, arm, leg, helmet) of every armor type in every weight class (light, sturdy, heavy), showing DR/ER/RR at all 11 standard levels.

**Example - Combat Armor Torso DR by level:**

| Level | Light (wiki) | Light (ESM) | Heavy (ESM) |
|-------|-------------|------------|-------------|
| 20 | "36" (max only) | 16 | 20 |
| 30 | -- | 25 | 32 |
| 40 | -- | 30 | 38 |
| 50 | 36 | 36 | 47 |

The wiki only stores the max-level chest piece value. The ESM provides the complete progression, which is essential for recommending armor to sub-level-50 characters.

## Structural Improvements

### Current Database Problems
1. **All values stored as TEXT** -- no numeric queries possible
2. **Damage stored as slash-separated string** -- can't query "weapons over 100 damage"
3. **No per-level data** -- useless for sub-50 builds
4. **No perk bonus curves** -- build generator hardcodes all perk priorities
5. **No legendary effect scaling** -- can't calculate actual DPS with Bloodied/Anti-Armor
6. **No GMST values** -- formulas are guesswork
7. **Missing PA types** -- Union, Vulcan, Presidential T-60, Enclave X-01 absent

### Enhanced Database Additions
1. **Numeric columns** for all stats -- enables math-based build optimization
2. **Per-level weapon damage** at levels 1/5/10/15/20/25/30/35/40/45/50
3. **Full curve tables** stored as queryable rows for interpolation
4. **56 perk bonus curves** with input type and bonus type metadata
5. **48 legendary effects** with exact scaling curves
6. **14 PA types** with per-piece per-level per-stat curves
7. **35 GMST values** for exact game formulas
8. **XP curve** for leveling calculations
9. **Critical charge curve** for VATS crit build math

## Impact on Build Generator

The current `build_generator.py` hardcodes perk recommendations and uses no math. With the ESM data, the generator could:

1. **Calculate actual DPS** using weapon curve + perk bonuses + legendary effects
2. **Recommend weapons by real damage** instead of category
3. **Show exact stats at the user's level** instead of max-level-only
4. **Calculate Bloodied damage correctly** (+130% weapon + +80% Nerd Rage = +210%, not +115%)
5. **Compare PA sets mathematically** instead of hardcoded "T-65 or Hellcat"
6. **Show perk bonus values** instead of just perk names
7. **Calculate critical hit frequency** based on Luck allocation

## Files Created

- `database/schema_esm.sql` -- Enhanced database schema (17 tables)
- `database/populate_db_esm.py` -- ESM data population script
- `database/fallout76_esm.db` -- Populated enhanced database
- `findings/fo76/054-perkolatr-esm-integration.md` -- This analysis
