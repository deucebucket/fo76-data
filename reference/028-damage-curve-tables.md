# Finding 028: Complete Damage Curve Tables from Game Data

**Source**: Extracted curve table JSONs from Startup BA2 (`misc/curvetables/json/`)
**Total files**: 4,262 curve tables across 28 categories
**Date**: 2026-03-20

## What Curve Tables Are

Every scaling value in Fallout 76 -- weapon damage, creature health, armor resistance, legendary effect magnitude, perk bonuses -- is driven by a **curve table**. These are JSON files containing `{x, y}` coordinate pairs where X is typically the item/creature level (in 5-level increments for weapons, 2-level increments for creatures) and Y is the actual value at that level. The game interpolates between points.

This is the raw math that drives every damage calculation. Community wikis test values at specific levels; these curves show the complete picture.

## Category Breakdown

| Category | File Count | Description |
|----------|-----------|-------------|
| armor | 367 | All armor DR/ER/RAD by piece and type |
| weaponmods | 169 | Weapon modification damage values |
| itemcondition | 114 | Item durability curves |
| legendarymods | 108 | Legendary effect magnitude scaling |
| weapons (ranged) | ~50 | Base weapon damage by level |
| weapons/melee | 78 | Melee weapon damage by level |
| weapons/thrown | 41 | Grenade/mine damage |
| perks | 56 | Perk card bonus scaling |
| player (tiers) | ~300 | Universal damage/armor/XP tier system (100 tiers each) |
| creatures | 7 subdirs | Health, armor, weapons, tiers, loot, XP |
| babylonendgame | 10 | Nuclear Winter / Babylon mode rewards |
| babylonstormdamage | 5 | Storm damage stages |
| babyloncombatformulas | 1 | Resistance formula |
| legendary | 8 | Legendary scrap/sell values |
| legendarymods | 108 | Legendary effect magnitudes |
| legendaryperks | 2 | Legendary perk rank costs |
| mutations | 2 | Adrenal Reaction curves |
| enchantments | 5 | Special weapon enchantments |
| spells | 10 | Barbarian, Evasive, cryo effects |
| brewing/crafting/econ/etc. | ~80 | Economy and misc systems |

---

## Weapon Damage Curves: The Complete Picture

### How to Read These Tables
- **X axis** = weapon level tier (1-50, in increments of 5). Level 50 is max for most weapons.
- **Y axis** = base damage value before any perks, legendary effects, or mutations.
- Weapons showing 0 at low levels are **level-gated** -- they literally cannot exist below that level.
- Growth rate (level 50 / level 1) shows how much a weapon improves with levels.

### Top 10 Highest Base Damage Weapons at Level 50

| Rank | Weapon | Lvl 1 | Lvl 50 | Growth | Notes |
|------|--------|-------|--------|--------|-------|
| 1 | **The Dragon** (Black Powder Rifle) | 183 | 611 | 3.34x | Highest single-shot damage in game |
| 2 | **Fat Man** | 0 (lvl 25+) | 455 | N/A | Level-gated, no low-level variant |
| 3 | **Gauss Rifle** | 94 | 315 | 3.35x | Best scaling ratio of any weapon |
| 4 | **Gauss Shotgun** | 86 | 285 | 3.31x | Per-pellet, total = 285 x pellets |
| 5 | **Cold Shoulder** | 69 | 231 | 3.35x | Shares top growth rate with Gauss |
| 6 | **Gauss Pistol** | 65 | 218 | 3.35x | Same growth rate as Gauss family |
| 7 | **Tesla Cannon** | 0 (lvl 20+) | 175 | N/A | Level-gated |
| 8 | **Gauss Rifle (Presidential)** | 120 | 170 | 1.42x | Flat curve, much worse scaling |
| 9 | **Combat Shotgun** | 45 | 150 | 3.33x | Per-pellet |
| 10 | **Warshrike** | 70 | 120 | 1.71x | Linear scaling + bleed + explosion |

### Weapon Scaling Tiers

**Best Scalers (3.3x+ growth from level 1 to 50)**:
- Gauss family (Rifle 3.35x, Shotgun 3.31x, Pistol 3.35x)
- The Dragon (3.34x)
- Cold Shoulder (3.35x)
- Combat Shotgun (3.33x)
- Handmade Rifle (3.28x)

**Flat/Poor Scalers**:
- Warshrike (1.71x) -- compensated by bleed+explosion components
- Presidential Gauss Rifle (1.42x) -- barely improves with level
- Flamer (1.26x) -- nearly flat, 23 damage from level 1-35, reaches only 29 at 50
- Gauss Minigun: flat 25 damage from level 1-40, jumps to 50 only at level 50

**Level-Gated Weapons (0 damage below threshold)**:
- Fat Man: available at level 25+ only
- .50 Cal Machine Gun: level 25+
- Tesla Cannon: level 20+
- Minigun: level 35+
- MG42: level 30+
- Incinerator: level 30+
- Chainsaw: level 20+
- Shock Halberd: level 30+
- Drill Fist: level 30+
- BoS Rocket Launcher: level 40+
- Lickety-Split: level 30+
- M79 Grenade Launcher: level 15+

### Interesting Weapon Notes

**10mm SMG Overheating Mechanic**: The 10mm SMG has a hidden overheating system:
- `overheatingdamagemultiplier`: damage multiplier goes from 1.0x at cold to **2.0x** at 75%+ heat
- `overheatingadditionalammo`: fires extra ammo per shot at 75%+ heat (1 extra round)
- This means sustained fire literally doubles your damage output

**Gauss Minigun Overheat**: Separate gradual curve from 1.004x (10% heat) to **1.6x** (100% heat). More granular than 10mm SMG.

**Flamer**: Nearly flat damage curve (23-29). The DOT file (`flamerdot`) is identical. NPC-only Flamer (`flamer_npc-only`) does 1-9 damage across 100 levels -- deliberately nerfed for NPC use.

**Two 10mm SMG Curves**: `weap_10mm_smgdmg.json` (4-11 damage) and `weap_10mmsmgdmg.json` (13-42 damage). The first appears to be a legacy/unused curve.

**weap_xxxxdmg.json**: Placeholder/template weapon. 1 damage at level 1, 8 at level 50. Developer testing artifact.

**Circuit Breaker = Enclave Plasma**: Both have identical curves (19-64). Circuit Breaker internally shares the Enclave Plasma damage curve.

**Meltdown = Handmade**: Both have identical curves (18-59). Meltdown shares the Handmade Rifle's base damage.

### Warshrike (Cut/New Content) - Multi-Component Damage

The Warshrike has four separate curve files:
- **Base damage**: 70-120 (linear, 1 point per level-step)
- **Bleed damage**: 30-80 (DOT component)
- **Explosion damage**: 30-80 (AoE component)
- **Projectile seek strength**: 0.000025 to 0.025 (homing projectile, ramps over 3 seconds)
- **Projectile speed**: 150 to 1200 (accelerates over 3 seconds)

Total combined damage at level 50: **120 + 80 + 80 = 280** (before bleed ticks). The homing projectile is a unique mechanic -- seek strength increases by 1000x over 3 seconds of flight time.

---

## Creature Health Curves

### Health at Level 100 (Max One Wasteland Scaling)

| Creature | HP at Lvl 2 | HP at Lvl 50 | HP at Lvl 100 | Growth Factor |
|----------|-------------|--------------|---------------|---------------|
| **Wendigo Colossus** | 24,495 | 161,586 | **393,180** | 16.1x |
| **Scorchbeast Queen** | 14,690 | 97,754 | **241,408** | 16.4x |
| **Behemoth Boss** | 1,351 | 9,415 | **25,182** | 18.6x |
| **Blue Devil** | 1,351 | 9,415 | **25,182** | 18.6x |
| **Boss Chicken** | 2,000 (lvl25) | 8,000 | **20,000** | 10.0x |
| **Blood Eagle Destroyer** | 810 | 5,711 | **15,575** | 19.2x |
| **Scorchbeast** | 576 | 4,094 | **11,317** | 19.6x |
| **Hewsen** | 346 | 2,487 | **7,020** | 20.3x |
| **Deathclaw** | 207 | 1,513 | **4,363** | 21.1x |
| **Alien** | 124 | 922 | **2,719** | 21.9x |
| **Super Mutant** | 63 | 479 | **1,454** | 23.1x |
| **Feral Ghoul** | 38 | 295 | **914** | 24.1x |
| **Mobster** | 53 | 407 | **1,245** | 23.5x |
| **Municipal Auditor** | 53 | 407 | **1,245** | 23.5x |

### Key Observations

**Blue Devil = Behemoth Boss**: Identical health curves (1,351 to 25,182). The Blue Devil is mechanically a reskinned Behemoth Boss.

**Boss Chicken**: Only 3 data points (levels 25, 50, 100). Simplified curve compared to everything else. 20,000 HP at level 100.

**Mobster = Municipal Auditor**: Identical health curves. Both are "human" enemy types with shared stats.

**The Drifter Weakpoint**: `thedrifter_weakpointdmg.json` is a flat **175,000** damage value at all levels. This is a one-shot kill mechanic triggered by hitting a specific weakpoint. The Drifter boss fight is designed around finding and hitting this point.

---

## Legendary Effect Curves

### Weapon Legendary Effects

| Effect | Curve Type | Key Values |
|--------|-----------|------------|
| **Junkie's** (weapon_damage) | Flat | **+20%** damage at all levels (0.2 multiplier) |
| **Bloodied** (damageinversehealth) | Inverse HP% | **+130%** at 5% HP, 0% at full HP |
| **Aristocrat's** (damageviacaps) | Caps-based | +3% at 1K caps, +27% at 15K, **+50% at 29K** caps |
| **Juggernaut's** (damageviahealth) | HP-based | Linear, **+100 flat damage** at 1000 HP (not %) |
| **Executioner's** (execute) | Flat | **+50%** damage to targets below 40% HP |
| **Hunter's/Exterminator's/etc.** (dmgvs*) | Flat | **+50%** damage vs specific enemy types |
| **Cryptid Hunter** (dmgvsscryptids) | Flat | **+50%** vs cryptids (same as all anti-type effects) |
| **Gourmand's** (gourmand) | Food meter | 0% at empty, **+40% at 8 (max food/drink)** |
| **Anti-Armor** (damageunarmored) | Inverse DR | **+50%** at 0 DR, +17% at 40 DR, +5% at 60 DR |
| **Sane** (weapon_sane) | Linear | 0-40% across 8 tiers (AP-related) |

**Bloodied vs Junkie's math confirmed**: Bloodied at 5% HP gives +130% damage. Junkie's is a flat +20% regardless. Community has long known Bloodied is superior; curves confirm the exact numbers.

**Aristocrat's surprising scaling**: Not linear. The first 1,000 caps only gives +3%, but the curve accelerates. You need **29,000 caps** for the full +50%.

**Anti-Armor diminishing returns**: At 0 DR it adds +50%, but at 60 DR only +5%. The effect is strongest against unarmored targets, nearly useless against heavily armored ones.

### Armor Legendary Effects

| Effect | Mechanism | Key Values |
|--------|-----------|------------|
| **Overeater's** | Food/drink meter | 0% at empty, **40% damage reduction at max (8.0)** |
| **Sentinel's** | Per-piece stacking | 5% → 10% → 14% → 19% → **23% total** (5 pieces) |
| **Cavalier's** | Per-piece multiplicative | 10% → 19% → 27.1% → 34.4% → **40.95%** (5 pieces) |
| **Bolstering** (rank 5) | HP-inverse DR mult | 0.59x DR at 0% HP → 1.0x at 75%+ HP |
| **Vanguard's** (rank 5) | HP-proportional | 1.0x at full HP → 0.734x at 1000+ DR point |
| **Aegis** | Stacking DR | 20/40/60/80/**100 DR per stack** (up to 5) |
| **Tanky** | Massive DR | 200/400/600/800/**1000 DR per stack** |
| **Lucid** (rank 5) | Stacking reduction | 1.9%/2.9%/4.2%/6.2%/9%/13.1%/18.9%/**26.6% reduction at 8 stacks** |

**Cavalier vs Sentinel**: Cavalier uses multiplicative stacking (each piece multiplies by 0.9), giving 40.95% total reduction with 5 pieces. Sentinel uses additive-but-diminishing stacking (5/5/4/5/4%), giving only 23% total. **Cavalier is significantly better than Sentinel** -- nearly double the damage reduction at 5 pieces. This contradicts the common community assumption that they're equivalent.

**Overeater's dominance confirmed**: Full food/drink meter = 40% damage reduction per piece. With 5 pieces at full meters, the stacking makes it the strongest defensive legendary in the game.

**Tanky is absurd**: Up to **1000 DR per stack**, 5 stacks possible. This is clearly designed for extreme endgame content.

### Electrician's vs Voltaic

Both `weapon_electriciansenergydmg` and `weapon_voltaicenergydmg` have **identical curves** (11-25 energy damage scaling by level). They're the same effect under different names. However, Voltaic also has an EMP component (`voltaicempdmg`): 40/60/80/100/**120 EMP damage** scaling with some other variable (possibly stacks or rank).

### Fracturer's Explosion Damage
Scales from 22 at level 1 to **50** at level 50. This is added explosion damage on hit.

### Cold Shoulder Cryo Damage
`weapon_cscryodamage`: 44 at level 1 to **91** at level 50. Significant additional cryo damage component.

---

## Damage Resistance Formula (Babylon/Nuclear Winter)

The `babyloncombatformulas/resistedpercentage.json` curve defines how armor converts to damage reduction:

| DR Value | % Damage Resisted |
|----------|------------------|
| 0 | 0% |
| 72 | 25% |
| 101 | 30% |
| 130 | 35% |
| 192 | 45% |

This is the Babylon/Nuclear Winter damage formula. It has severe diminishing returns -- going from 0 to 72 DR gives you 25% reduction, but going from 72 to 192 (2.67x more DR) only gives you 20% more reduction.

---

## Babylon/Nuclear Winter Storm Damage

The storm damage system has 4 stages that ramp over time:

| Stage | Ambient Tick | 70% Ring | 90% Ring | Edge (100%) |
|-------|-------------|----------|----------|-------------|
| Stage 1 | 2% max HP | 9% | 27% | 100% (instant kill) |
| Stage 2 | 7% max HP | 15% | 45% | 100% |
| Stage 3 | 13% max HP | 35% | 60% | 100% |
| Stage 4 | 18% max HP | 45% | 80% | 100% |

The **time multiplier** kicks in after 1 second, starting at 1.0x and ramping to **2.5x at 60 seconds**. So Stage 4 at 60 seconds deals 18% * 2.5 = **45% max HP per tick** in ambient storm.

---

## Power Armor DR Rankings (Torso at Level 50)

| PA Set | Torso DR | Notes |
|--------|----------|-------|
| **Vulcan** | 140 | Unreleased. Highest DR in game. |
| **T-65** | 140 | Current best available |
| **Union** | 115 | Expedition reward |
| **T-51b** | 114 | Classic mid-tier |
| **Ultracite** | 113 | Nearly identical to T-51b |
| **T-60** | 100 | Includes Presidential variant (same stats) |
| **X-01** | 98 | Enclave variant exists (same stats) |
| **Hellcat** | 96 | Despite anti-ballistic reputation |
| **T-45** | 90 | Starter PA |
| **Excavator** | 60 | Mining PA, lowest DR |

**Vulcan PA = T-65 stats**: Both have 140 DR torso. Vulcan also has elemental resistance slots: Cold (15.49), Fire (15.49), Poison (15.49), but Electric is **0**. The zero electric resistance looks like incomplete implementation.

**Secret Service (non-PA) armor**: Torso DR is flat 75 from level 1-45, jumping to **90** at level 50 only. ER and RAD are flat 50 until level 50 where they jump to 60. This "everything at level 50" pattern is unique to SS armor.

---

## Adrenal Reaction Mutation

| Health % | Normal Bonus | Super (Strange in Numbers) |
|----------|-------------|---------------------------|
| 5% (near death) | **+100%** damage | **+125%** damage |
| 50% | ~50% | ~62.5% |
| 100% (full) | +5% | +6.25% |

The curve is linear between 1% and 20% health percentage, meaning every point of health lost adds roughly 5% damage (normal) or 6.25% (with Strange in Numbers). At the "Bloodied sweet spot" of ~20% HP, Adrenal Reaction alone gives approximately +80% damage.

---

## Perk Card Curves

### Damage Perks
| Perk | Rank 1 | Max Rank | Scaling |
|------|--------|----------|---------|
| Heavy Gunner (3 cards) | varies | **+90%/+180%/+270%** at rank 30 | Linear per-rank |
| Adrenaline | +10% per kill | **+100%** at 10 kills | 10% per kill stack |
| Nerd Rage (damage) | +40% at 20% HP | **+80%** at 5% HP | Inverse HP |
| Nerd Rage (AP) | +15 at 20% HP | **+30** at 5% HP | Inverse HP |
| Serendipity | 6% at rank 1 | **40%** at rank 100 | Diminishing returns |
| Ricochet | 4% at rank 1 | **35%** at rank 100 | Diminishing returns |
| Barbarian (DR per STR) | +2 DR per STR (rank 1) | **+4 DR per STR** (rank 3), cap **80 DR** at 20 STR | Linear per-STR, caps at 20 |
| Evasive (DR per AGI) | +1 DR per AGI (rank 1) | **+3 DR per AGI** (rank 3), cap **45 DR** at 15 AGI | Linear per-AGI, caps at 15 |
| Lone Wanderer (DR) | 10 DR at rank 1 | **210 DR** at rank 100 | Steep curve |

### Interesting Perk Findings

**Guerrilla Master has absurd theoretical values**: The curve goes from 5 at rank 1 to **500** at rank 100. This is likely a multiplier/scaling factor rather than direct damage %, but the curve itself goes far beyond the 3-rank cards players actually use.

**Shotgunner Master**: 10 at rank 1 to **300** at rank 30. Another high-ceiling curve.

**Heavy Gunner stacking**: The three Heavy Gunner cards (heavydamagebonus 1/2/3) give +90/+180/+270 at rank 30. At max rank all three cards together can provide up to +270% heavy weapon damage.

---

## Ranged Damage Falloff

`player/percentofmintomaxrangedamagemult.json`:

| Distance Multiplier | Damage Retained |
|---------------------|----------------|
| 1.0x (min range) | 100% |
| 1.5x | 75% |
| 1.75x | 55% |
| 2.0x (max range) | **20%** |

At double a weapon's effective range, you deal only 20% damage. This is the universal falloff curve for all ranged weapons.

---

## Legendary Perk Costs

Legendary Perk upgrade costs (perk coins per rank):
- Rank 1: 50
- Rank 2: 75
- Rank 3: 100
- Rank 4: 150
- Rank 5: 200
- Rank 6: **300**

Total cost for a max rank legendary perk: **875 perk coins** (175 perk card scraps at 5 coins each = 35 perk cards scrapped).

---

## Universal Tier System (Player Scaling)

The `player/damage/`, `player/armor/`, and `player/xp/` directories each contain **100 tier files**. These appear to be the backbone of the One Wasteland scaling system.

Sample damage tier values at level 50:
- Tier 1: 3
- Tier 25: 112
- Tier 50: 449
- Tier 100: **2,088**

The ratio between Tier 1 and Tier 100 at level 50 is **696x**. This enormous range suggests these tiers are used to scale enemy damage from trash mobs (Tier 1) to boss enemies (Tier 100), with creatures assigned to specific tiers.

---

## Cut/Unreleased Content Identified

### Vulcan Power Armor
- Has complete curve tables for all body parts (torso, arms, legs, helmet)
- Includes **elemental resistance types**: Cold, Fire, Electric, Poison -- a system not present on any released PA
- Electric resistance is **0** on all pieces -- possibly incomplete
- DR values match T-65 (140 torso), making it a T-65 equivalent with elemental bonuses

### Blue Devil
- Health curve identical to Behemoth Boss (1,351 to 25,182)
- Has its own unarmed attack damage curve (44-120+ over levels 2-100)
- Full set of elemental armor resistances defined
- This is a boss-tier creature, not a regular enemy

### Hewsen
- Named NPC/creature with full health (346-7,020), armor, and resistance curves
- Roughly 2.8x the health of a standard Deathclaw at level 100
- Has elemental armor values (cold, fire, poison, etc.)

### Boss Chicken
- Simplified 3-point curve (levels 25/50/100 only)
- 20,000 HP at level 100 -- between Behemoth and Wendigo Colossus tier
- The name is clearly a developer placeholder

### Municipal Auditor
- Full human NPC with complete weapon loadouts (pistol, rifle, shotgun, sniper, heavy, melee, explosives, flamer, minigun)
- Same health as Mobster NPCs (407 HP at level 50)
- "Municipal Auditor" is likely a faction or encounter-specific enemy

### Mobster NPCs
- Complete weapon suite including **Shishkebab fire damage** -- the only human NPC type with a dedicated Shishkebab curve
- Full elemental armor set

### Bounty Hunting Headhunt System
- Boss, Boss PA (power armor variant), and Lackey curves
- Full health, armor, and resistance suites
- Appears to be a PvE bounty hunting system

### The Drifter
- Weakpoint mechanic: **175,000** flat damage -- a one-shot kill trigger
- This is a boss fight designed around precision shooting at a specific target

### Babylon Population Constriction
- `babylonpopulationconstrictionfastforward.json`: Value of 390 for first 20 entries, then drops to 0
- This controls how quickly the Nuclear Winter play area shrinks when player count is low

---

## Anomalies and Balance Issues

1. **Cavalier >> Sentinel**: Cavalier gives nearly **double** the damage reduction of Sentinel at 5 pieces (40.95% vs 23%). Community generally treats them as equal.

2. **Flamer nearly flat**: 23 damage from level 1 through 35, only reaching 29 at 50. One of the worst-scaling weapons despite being popular due to fire rate.

3. **Gauss Minigun damage cliff**: Flat 25 damage for 40 levels, then jumps to 48-50 at levels 45-50. Below level 45, the Gauss Minigun does less damage than a level 1 10mm Pistol.

4. **Presidential Gauss Rifle underperforms**: Only 170 damage at level 50 vs standard Gauss Rifle's 315. The "special" variant does **46% less damage** than the standard version.

5. **NPC Flamer is deliberately gimped**: NPC-only Flamer curve caps at 9 damage at level 100. Player Flamer does 29 at level 50. NPCs with Flamers are cosmetically threatening but nearly harmless.

6. **Vulcan PA electric = 0**: Every elemental resistance on Vulcan PA has a value (cold 15.49, fire 15.49, poison 15.49) except electric, which is 0. Either intentionally weak to electricity or incomplete.

7. **Heavy Gunner perk cards stack to +270%**: The three tiers of Heavy Gunner provide up to 90+180+270 = potentially stacking damage bonuses. This is why Heavy Gunner builds dominate endgame.

---

## Community Knowledge Verification

Much of the base weapon damage data aligns with values on falloutbuilds.com and the Fandom wiki at specific levels. What these curve tables add that the community generally lacks:

1. **Complete level-by-level scaling** -- wikis typically only show max-level values
2. **Exact legendary effect formulas** with full curves (e.g., Aristocrat's non-linear caps scaling, Anti-Armor diminishing returns by DR)
3. **Cavalier vs Sentinel multiplicative stacking math** -- the actual formulas showing Cavalier's superiority
4. **Overheating mechanics** on 10mm SMG and Gauss Minigun with exact multiplier curves
5. **Universal tier system** revealing the One Wasteland scaling backbone
6. **Cut content** curves (Vulcan PA elemental system, Blue Devil, The Drifter weakpoint, Boss Chicken)
7. **Babylon/Nuclear Winter storm damage** exact stage-by-stage numbers with time multiplier
8. **NPC-only weapon variants** with deliberately reduced damage
