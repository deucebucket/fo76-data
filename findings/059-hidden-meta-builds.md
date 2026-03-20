# Finding 059: Hidden Meta Builds - What the Wiki Got Wrong Changes Everything

**Source**: Calculated using `perkolatr/damage_calculator.py` with corrected values from extracted game curve tables (108 legendary mod curves, 4,262 total curve tables)
**Cross-referenced with**: Findings 028, 033, 034, 037, 057
**Date**: 2026-03-20

---

## Executive Summary

The community meta is built on wrong numbers. Six critical wiki discrepancies -- confirmed by extracted game data -- create build opportunities that the playerbase has dismissed as unviable. When you plug the *real* values into the damage pipeline, builds that "shouldn't work" suddenly rival or exceed established meta choices.

**The corrected values that change everything:**

| Effect | Wiki Claims | Actual Game Data | Impact |
|--------|------------|------------------|--------|
| Nocturnal | -50% day / +50% night | **+0% day / +50% night** | No downside prefix |
| Junkie's | +50% max at 5 addictions | **+100% at 10 addictions** | Doubles expected output |
| Bloodied | +80-95% max | **+130% at 5% HP** | Even more dominant |
| Gourmand's | +24% max | **+40% max** | Jumps from trash to B-tier |
| Cavalier vs Sentinel | "Both 15%" | **Cav 41% vs Sent 23%** | Movement builds 1.8x better |
| Adrenal Reaction | "+5% per kill" | **+100% at low HP (curve)** | Health-based, not kill-based |

---

## Build Tier List (Corrected Values)

All calculations use The Fixer (level 50, base 59 damage), full Commando perks (3x rank 3 = +60%), Bloody Mess 3 (+15%), Tenderizer 3 (+7%), against a target with 200 DR. Sustained DPS includes reload time.

| Tier | Build | Dmg/Hit | Sustained DPS | vs Best |
|------|-------|---------|---------------|---------|
| **S** | Bloodied+AR+NR @15% HP, sneaking | 1,227 | 6,691 | 100.0% |
| **S** | Junkies@10+AR+NR @20% HP, sneaking | 1,008 | 5,497 | 82.2% |
| **A** | Nocturnal + Sneak + Mr Sandman (night) | 342 | 1,864 | 27.9% |
| **A** | Junkies@10 + AR @50% HP (safe hybrid) | 199 | 1,084 | 16.2% |
| **B+** | Junkies@10 (full HP, no mutations) | 111 | 607 | 9.1% |
| **B** | Aristocrat's (29k caps) | 72 | 392 | 5.9% |
| **B** | Mutant's @10 mutations (REAL cap) | 72 | 392 | 5.9% |
| **B** | Junkies @5 addictions (wiki max) | 72 | 392 | 5.9% |
| **B-** | Gourmand's (+40% REAL value) | 65 | 352 | 5.3% |
| **C** | Mutant's @5 mutations (wiki cap) | 54 | 294 | 4.4% |
| **C** | Nocturnal (daytime -- NO penalty) | 38 | 205 | 3.1% |
| **D** | No legendary | 38 | 205 | 3.1% |

**What shifted**: Junkies@10 jumps from B-tier to S-tier. Mutant's@10 jumps from C to B (ties Aristocrat's). Gourmand's jumps from D to B-. Nocturnal goes from F ("unusable") to C during day / A at night.

---

## Build 1: The Nocturnal Specialist

### Why It Works Now

The wiki claims Nocturnal imposes a **-50% damage penalty during daytime**. The game curve table `weapon_damagenight` shows:

```
Game Hour | Damage Bonus
0-5      | +50%
6-20     | +0%      <-- NOT -50%
21-24    | +50%
```

There is **no penalty**. Daytime Nocturnal performs identically to a weapon with no legendary prefix. At night, it is a free +50% -- matching Aristocrat's at 29,000 caps with zero conditions.

### Calculated DPS

| Scenario | Dmg/Hit | Burst DPS | Sustained DPS |
|----------|---------|-----------|---------------|
| Nocturnal (night, 9pm-5am) | 71.8 | 718.5 | 391.9 |
| Nocturnal (day, 6am-8pm) | 37.5 | 375.1 | 204.6 |
| Aristocrat's (29k caps) | 71.8 | 718.5 | 391.9 |
| No legendary | 37.5 | 375.1 | 204.6 |

Nocturnal at night **equals Aristocrat's at max caps**. During the day it equals a non-legendary weapon -- not a -50% penalty weapon.

### The Night Specialist Build

**Concept**: Combine Nocturnal's free +50% with night-specific bonuses that other builds can't stack.

**Weapon**: Nocturnal / Faster Fire Rate / 25% Less VATS AP Fixer
**Perks**: Full Commando + Mr. Sandman (night-only +50% sneak multiplier) + Covert Operative 3
**Mutations**: Adrenal Reaction + Speed Demon + Marsupial + standard suite

**DPS at night, sneaking, undetected**:
- Sneak multiplier: 3.0x (2.5x Covert Op + 0.5x Mr. Sandman)
- Nocturnal: +50%
- Result: **342 damage per hit, 1,864 sustained DPS**

**When to play**: FO76 day/night cycle is roughly 7 real-time minutes per game hour. Night (9pm-5am) is 8 game hours = ~56 real minutes. Day is ~98 minutes. You get ~36% of your playtime at night bonus.

**Synergies**:
- Mothman Equinox event (night-themed, +15% XP Wisdom of the Mothman buff)
- Night Person perk (+3 INT at night = +9% XP bonus)
- Mr. Sandman sneak bonus (night only, stacks with Covert Operative)
- Free vendor trash the rest of the time -- the weapon works as a baseline non-legendary during day

**Why the community missed this**: Everyone scripped Nocturnal weapons on sight because the wiki says "-50% during day." Nobody tested it because why would you test a weapon that's supposedly half-strength 14 hours a day?

---

## Build 2: The 10-Addiction Junkie

### The Addiction Math

The wiki says Junkie's caps at +50% with 5 addictions. The curve `weapon_damageaddiction` is:

```
Addictions | Bonus
0          | 0%
1          | 10%
5          | 50%    <-- Wiki says "max"
10         | 100%   <-- REAL max
```

Linear +10% per addiction. At 10 addictions, Junkie's matches Bloodied at 23% HP.

### Available Addictions (11 total in FO76)

Optimized for minimal SPECIAL penalty:

| Priority | Addiction | Raw Penalty | With Class Freak 3 (75% reduction) |
|----------|-----------|-------------|--------------------------------------|
| 1 | Psycho | None | None |
| 2 | X-Cell | None | None |
| 3 | Formula P | None | None |
| 4 | Med-X | None | None |
| 5 | Mentats | CHA -1 | Negligible |
| 6 | Fury | PER -1 | Negligible |
| 7 | Daddy-O | PER -1, INT -1 | INT -0.25 (rounds to 0) |
| 8 | Day Tripper | LCK -1, STR -1 | Negligible |
| 9 | Alcohol | STR -1, AGI -1, CHA -1 | STR -0.25 |
| 10 | Overdrive | STR -1, END -1 | Negligible |

**Raw total penalties**: STR -3, AGI -1, CHA -2, PER -2, INT -1, END -1, LCK -1
**With Class Freak 3**: STR -1 (rounded). Everything else rounds to zero.

The first 4 addictions have **zero penalty at all**. You can get +40% damage for literally free SPECIAL cost, then another +60% for effectively -1 STR.

### Junkie's vs Bloodied: Head-to-Head

| Build | Dmg/Hit | Sustained DPS | Risk Level |
|-------|---------|---------------|------------|
| Junkies @10 (full HP) | 111.2 | 606.5 | None |
| Junkies @5 (wiki max, full HP) | 71.8 | 391.9 | None |
| Bloodied @20% HP | 119.1 | 649.5 | HIGH |
| Bloodied @30% HP | 107.7 | 587.7 | Medium |

**Junkies @10 at full health outdamages Bloodied at 30% HP**. The gap only opens at extreme low health (Bloodied @15% = 124.8 dmg vs Junkies @10 = 111.2 dmg, a mere 12% difference).

### The Multiplicative Stack: Junkies + Adrenal Reaction

The damage pipeline processes legendary bonuses and mutation bonuses in **separate multiplicative categories**:

```python
after_legendary = after_perks * (1 + legendary_bonus)    # Step 4
after_mutations = after_legendary * (1 + mutation_bonus)  # Step 5
```

This means Junkies (+100%) and Adrenal Reaction (+80% at 20% HP) **multiply**:

| Build | Dmg/Hit | Sustained DPS |
|-------|---------|---------------|
| Junkies @10 alone (full HP) | 111.2 | 606.5 |
| Adrenal Reaction alone (20% HP) | 95.0 | 518.1 |
| **Junkies@10 + AR (20% HP) + NR** | **331.1** | **1,806.0** |
| Bloodied + AR + NR (20% HP) | 351.5 | 1,917.3 |

Combined, Junkies@10+AR at 20% HP reaches **94.2% of a full Bloodied+AR+NR build**. The trade-off: Junkies works at any health level. At 50% HP (much safer), Junkies@10+AR still hits 198.8 damage per hit (1,084 sustained DPS).

### The "Safe Junkie" Build

**Play at 50% HP instead of 20%**. You still get:
- Junkies: +100% (full regardless of health)
- Adrenal Reaction at 50% HP: +50%
- Total multiplicative: (1 + 1.0) * (1 + 0.5) = 3.0x legendary+mutation multiplier

Compare to Bloodied at 50% HP:
- Bloodied at 50%: +68%
- Adrenal at 50%: +50%
- Total: (1 + 0.68) * (1 + 0.5) = 2.52x

**Junkies@10 + AR at 50% HP beats Bloodied + AR at 50% HP by 19%**. The Safe Junkie outperforms Bloodied at equivalent health levels because +100% > +68%.

---

## Build 3: The Gourmand Tank

### Why +40% Changes Everything

Wiki says +24%. The actual curve `weapon_gourmand`:

```
Satisfaction | Bonus
0            | 0%
4            | 20%
8 (max)      | 40%
```

At +24%, Gourmand's was worse than every alternative. At +40%, it's 80% of Aristocrat's with the easiest condition in the game (eat food and drink water, which you do anyway).

### Risk-Adjusted Performance

| Build | Dmg/Hit | Sustained DPS | Risk | Uptime |
|-------|---------|---------------|------|--------|
| Gourmand's (+40%) | 64.5 | 351.9 | None | 100% |
| Aristocrat's (+50%) | 71.8 | 391.9 | Low (cap hoarding) | 95% |
| Bloodied @20% HP (+110%) | 119.1 | 649.5 | High (one-shot death) | ~85% |

Accounting for deaths (Bloodied players die to one-shot mechanics, losing DPS uptime):
- **Bloodied effective DPS** (assuming 85% uptime): 552.0
- **Gourmand's effective DPS** (100% uptime): 351.9
- Gourmand's delivers **63.7%** of Bloodied's *practical* output with zero risk

### The Gourmand Tank Build

**Weapon**: Gourmand's / FFR / 25% Less VATS AP
**Armor**: 5pc Overeater's + Cavalier's (1st + 3rd star combo)
**Playstyle**: Sprint, shoot, eat. Never die.

**Damage reduction while sprinting**:
- Overeater's 5pc at max food: 92.2% reduction (see note below)
- Cavalier's 5pc while sprinting: 41.0% reduction
- Combined (multiplicative): **95.4% total damage reduction**

**Note on Overeater's**: The raw curve shows 40% per piece at max satisfaction. If stacked multiplicatively across 5 pieces, that's 1 - (1 - 0.40)^5 = 92.2%. This may be capped in practice by the game engine, but the curve data supports these values. Even at a more conservative interpretation (6% per piece as commonly cited), that's still 26.5% stacked with Cavalier's 41% for 56.6% total.

You deal 90% of Aristocrat's damage while taking only 4.6% of incoming damage. The "scrip tier" legendary becomes the backbone of the safest build in the game.

---

## Build 4: The Cavalier Sprinter

### Cavalier Is 1.8x Better Than Sentinel

The community treats Cavalier's and Sentinel's as equivalent ("both give 15% reduction per piece"). The game data shows they are dramatically different:

| Pieces | Cavalier (sprint) | Sentinel (standing) | Cav Advantage |
|--------|-------------------|---------------------|---------------|
| 1 | 10.0% | 5.0% | 2.0x |
| 2 | 19.0% | 10.0% | 1.9x |
| 3 | 27.1% | 14.0% | 1.9x |
| 4 | 34.4% | 19.0% | 1.8x |
| 5 | **40.95%** | **23.0%** | **1.78x** |

Both are **deterministic** (not "75% chance" as the wiki claims). Each Cavalier piece multiplies incoming damage by exactly 0.9. Each Sentinel piece by approximately 0.95.

### The Sprint-Tank Build

**Concept**: Stay in permanent sprint with Speed Demon. Fire while running. 41% passive damage reduction.

**Armor**: 5pc Cavalier's (any 1st star -- Overeater's or Bolstering for extra DR)
**Mutations**: Speed Demon (+20% move speed), Marsupial (jump escape), Adrenal Reaction
**Perks**: Dodgy (25% chance to avoid 30% damage, costs AP), Serendipity (<30% HP: 45% avoid)
**Weapon**: Vampire's Heavy Gun (heal while sprinting, never stop moving)

**Damage reduction stack (sprinting at <30% HP)**:
- Cavalier's 5pc: 41.0%
- Dodgy: ~7.5% (25% * 30%, probabilistic)
- Serendipity: ~45% (at <30% HP)
- Emergency Protocols PA torso: 50% at <20% HP (if PA build)

**Why Sentinel builds are overvalued**: Standing still to get 23% reduction while enemies can target you freely is worse than sprinting for 41% while also being harder to hit. The community meta favoring Sentinel over Cavalier is based on wrong numbers.

---

## Build 5: Stacking Combinations Nobody Considers

### The Multiplicative Stack Table

The damage pipeline has four distinct multiplicative categories. Stacking across categories multiplies; stacking within a category only adds. Here's what matters:

```
Final = Base * (1 + PerkPool) * (1 + LegendaryBonus) * (1 + MutationBonus) * SneakMult * CritMult
```

| Category | Sources | Stack Type |
|----------|---------|------------|
| Perk Pool | Commando, Bloody Mess, Tenderizer, Adrenaline, Nerd Rage | Additive (within) |
| Legendary | Bloodied/Junkies/Nocturnal/Aristocrats/etc. | Multiplicative (separate) |
| Mutations | Adrenal Reaction, Twisted Muscles | Multiplicative (separate) |
| Sneak | Covert Operative, Mr. Sandman | Multiplicative (separate) |
| Critical | Better Criticals, Eagle Eyes | Multiplicative (separate) |

### Maximum Theoretical Damage Stack

**Junkies@10 + Adrenal Reaction (super) + Nerd Rage + Full Perks + Sneak + Crit**:

```
Base: 59 (The Fixer level 50)
Perks: +82% (Commando 60% + BM 15% + Tender 7%) -> 107.4
  + Nerd Rage @15% HP: +80% -> in perk pool
  + Adrenaline @10 kills: +100% -> in perk pool
  Perk pool total: +262%

After perks: 59 * (1 + 2.62) = 213.6

Legendary: Junkies@10 = +100%
After legendary: 213.6 * 2.0 = 427.2

Mutations: Adrenal (super) @15% HP = +100%
After mutations: 427.2 * 2.0 = 854.4

Sneak: Covert Op 3 + Sandman (night) = 3.0x
After sneak: 854.4 * 3.0 = 2,563.2

Crit: Better Criticals 3 + Eagle Eyes = +125% crit
After crit: 2,563.2 * 2.25 = 5,767.2

Armor reduction (@200 DR): 5,767^2 / (5,767 + 200) = 5,574 final
```

That's **5,574 damage per hit** from a Fixer. The same setup with Bloodied instead of Junkies@10 would be 6,080 -- only 9% more, while requiring dangerously low HP.

---

## Build 6: Anti-Meta Builds That Shouldn't Work (But Do)

### "The Moth Man" -- Nocturnal Night Sneak Commando

**What the community says**: "Nocturnal is a scrip legendary. The -50% day penalty makes it unusable."

**What the game data says**: No penalty. +50% at night, +0% during day.

**The build**:
- Nocturnal FFR/25VATS Fixer
- Full Commando + Covert Operative 3 + Mr. Sandman
- Play events at night (Mothman Equinox, Scorched Earth often spawns at night)
- Night Person perk for +3 INT (+9% XP at night)
- During day, weapon performs identically to a non-legendary -- swap to your Aristocrat's

**DPS at night, sneaking**: 342 dmg/hit, 1,864 sustained -- **higher than any non-sneak legendary build**

### "The All-In Mutant" -- 10 Mutations + Mutant's Legendary

**What the community says**: "Mutant's caps at +25% with 5 mutations. It's worse than Aristocrat's."

**What the game data says**: Curve goes to +50% at 10 mutations. Matches Aristocrat's at 29k caps.

**The build**:
- Mutant's FFR/25VATS Fixer
- 10+ mutations with Starched Genes 2 + Class Freak 3
- Adrenal Reaction at 50% HP adds +50% multiplicatively
- Effective: +50% (legendary) * +50% (AR) = 2.25x damage multiplier at half health

**DPS at 50% HP with AR**: 132.2 dmg/hit, 721.0 sustained

Mutant's@10 with AR at half health beats Aristocrat's at full health by 84%. The wiki's "+25% max" caused everyone to dismiss this prefix.

### "The Scrip Lord" -- Budget Build That Outperforms

Cheapest possible good build using "trash" legendaries the community scrips:

**Weapon**: Gourmand's / FFR / Any 3rd star (vendor trash, 100-500 caps)
**Armor**: Any Cavalier 3rd star pieces (cheap since community undervalues them vs Sentinel)
**Cost**: Under 5,000 caps total from player vendors

**Performance**: 64.5 dmg/hit, 352 sustained DPS with 41% DR while sprinting
**Comparison**: Aristocrat's Fixer costs 15,000-40,000 caps and deals 72 dmg/hit (only 11% more)

---

## Build 7: XP Farming -- The Real Maximum Multiplier

### Intelligence is 3% Per Point (Not 2%)

The GMST values confirm:
```
fXPModBase = 1.0
fXPModMult = 0.03
XP_multiplier = 1.0 + (INT * 0.03)
```

The community has debated 2% vs 3% for years. It is definitively 3%.

### Maximum Achievable Intelligence

| Source | INT Bonus |
|--------|-----------|
| Base SPECIAL allocation | +15 |
| Unyielding 5pc (<20% HP) | +15 |
| Egg Head mutation | +6 |
| Legendary INT perk (max rank) | +5 |
| Berry Mentats | +5 |
| Casual Team bond | +4 |
| Night Person 3 (at night) | +3 |
| Shielded Casual Underarmor | +3 |
| Brain Bombs (Herbivore 2x) | +8 |
| Herd Mentality (on team) | +2 |
| Marsupial penalty (Class Freak 3) | -1 |
| **Total** | **65** |

**INT XP Multiplier**: 1.0 + (65 * 0.03) = **2.95x**

### Additive XP Bonus Stack

| Source | XP Bonus |
|--------|----------|
| Lunchboxes x4 | +100% |
| Double XP event (when active) | +100% |
| Cranberry Relish (Herbivore 2x) | +10% |
| Inspirational 3 (on team) | +15% |
| Mothman Equinox buff | +15% |
| Well Rested / Lover's Embrace | +5% |
| Leader Bobblehead | +5% |
| Live & Love #8 | +5% |
| **Total additive** | **+255%** |

### Final XP Multiplier

```
Total = INT_mult * (1 + additive_bonuses)
      = 2.95 * (1 + 2.55)
      = 2.95 * 3.55
      = 10.47x
```

**10.47x XP** at theoretical maximum (requires Double XP event).

**Practical max (no Double XP event)**: 2.95 * 2.55 = **7.52x**

### What This Means

| Creature (Level 100) | Base XP | @7.52x (practical) | @10.47x (event) |
|----------------------|---------|---------------------|-----------------|
| Super Mutant (Medium) | 125 | 940 | 1,309 |
| Deathclaw (Large) | 200 | 1,504 | 2,094 |
| Scorchbeast Queen (Boss) | 500 | 3,760 | 5,236 |

### Bloodied XP Build vs Full Health XP Build

Without Unyielding (full health), max INT drops to ~50:
- Full health INT mult: 1.0 + (50 * 0.03) = 2.50x
- Full health total: 2.50 * 2.55 = **6.38x**

Bloodied XP build: **7.52x** (1.18x better than full health)

The 15 INT from Unyielding is worth an 18% XP boost. Whether that's worth the risk of low-health play depends on your playstyle, but the math says it's significant.

---

## Build 8: Economy Optimization

### The .308 Ammo Arbitrage

The Ammo-O-Matic production rates are **not equal**:

| Ammo | Rounds/Hour | vs 5.56 |
|------|-------------|---------|
| .308 | 1,667 | **8.0x** |
| .45 | 769 | 3.7x |
| .44 | 625 | 3.0x |
| Shotgun | 286 | 1.4x |
| 10mm | 278 | 1.3x |
| 5.56 | 208 | 1.0x |

The community assumes equal production rates. In reality, .308 produces **8 times faster** than 5.56.

**Optimal ammo strategy**:
1. Set Ammo-O-Matic to .308
2. Convert excess ammo to .308 (or sell directly)
3. If you use 5.56 weapons, buy .308 and trade with other players

### The Hidden 19% Tax

Items at 100% condition sell for only 81% of base value (`itemconditionvaluemultiplier` curve caps at 0.81). This is a hidden tax that stacks with the Charisma sell curve:

```
Effective sell value at CHA 30 = base * 0.25 * 0.81 = 20.25% of item value
```

### Vendor Cap Recovery Exploit

`fVendorIncomeMult = 0.25` -- when you **buy** from a vendor, they regain 25% of your spend into their cap pool.

**Strategy**: Before selling expensive items, buy cheap items (ammo, stimpaks) from the vendor first. Every 100 caps you spend buying gives the vendor 25 caps back, which you can then sell into.

### Caps Farming Optimization

| Source | Daily Caps | Notes |
|--------|-----------|-------|
| Player vendor sales | 1,400 | Daily cap on player vending income |
| NPC vendor selling | 1,400 | Across all vendor pools (shared 3-day reset) |
| Daily quests average | 700 | Foundation/BoS/regional dailies |
| Public events (~4/session) | 600 | 150 caps average per event |
| Cap stash exploration | 200 | Level 30+ loot cliff helps |
| Counterfeit Cap Press | 141 | CAMP item, 0.17 hours per cap |
| **Total** | **~4,500/day** | |

### Death Caps Loss (Actual Values)

| Level | % Lost | At 40,000 Caps |
|-------|--------|----------------|
| 1-20 | 1% | 400 |
| 21-40 | 2% | 800 |
| 41-50+ | 3% | 1,200 |

The community dramatically overestimates death penalties. At endgame with 40k caps, you lose 1,200 caps -- less than 30 minutes of efficient farming.

### Most Caps-Efficient Playstyle

1. **Use .308 weapons or heavy guns** -- cheapest ammo production
2. **Max Charisma for vendor visits** (CHA 30 sells at 25% vs CHA 1 at 10%)
3. **Sell legendaries to Purveyor for scrip**, not vendors for caps (scrip economy is more valuable long-term)
4. **Buy cheap from vendors before selling expensive items** (25% cap recovery exploit)
5. **Fast travel costs cap at 60** -- don't walk to save caps; the max cost is trivial
6. **Claim workshops for events**, not passive production (workshop XP bonus is 0.0 in game data)

---

## Mathematical Notes

### Why Multiplicative Stacking Matters

Most players think all damage bonuses "add up." The game engine uses a specific order:

```
final = base * (1 + perk_pool) * (1 + legendary) * (1 + mutation) * sneak * crit
```

At maximum stacking with corrected Junkies@10:
- Perk pool: +82% base (no Nerd Rage/Adrenaline) = 1.82x
- Legendary: +100% Junkies = 2.0x
- Mutation: +80% Adrenal @20% HP = 1.8x
- Sneak: 3.0x (CO3 + Sandman)
- Crit: 2.0x (base crit)

**Additive model would give**: 1 + 0.82 + 1.00 + 0.80 + 2.0 + 1.0 = **6.62x**
**Multiplicative model gives**: 1.82 * 2.0 * 1.8 * 3.0 * 2.0 = **39.3x**

The difference is **enormous**. This is why stacking across categories is the key to build optimization, and why the corrected legendary values create such outsized impact -- they're their own multiplicative tier.

### Armor Formula Deep Dive

The Fallout 76 adventure mode damage formula:

```
effective_dr = target_dr * (1 - armor_penetration)
damage_mult = damage / (damage + effective_dr)
final = damage * damage_mult = damage^2 / (damage + effective_dr)
```

This means high-damage builds get diminishing returns against armor, but those returns diminish *slowly*. At 1,000 damage vs 200 DR: `1000^2 / 1200 = 833` (83.3% throughput). The corrected Junkies/Adrenal stacks push damage so high that armor becomes nearly irrelevant.

---

## Summary: The New Meta

1. **Nocturnal is a free +50% at night with no penalty** -- stop scripping it
2. **Junkies@10 = +100%**, making it S-tier when stacked with Adrenal Reaction
3. **Gourmand's = +40%** makes it a legitimate full-health option, not a joke
4. **Cavalier's is 1.78x better than Sentinel's** -- movement builds are objectively superior
5. **Mutant's goes to +50% at 10 mutations** -- equals Aristocrat's with less effort
6. **Adrenal Reaction is +100% at low HP** (health-based, not kill-based) -- multiplicative with everything
7. **INT gives 3% XP per point** -- max achievable XP multiplier is 10.47x
8. **.308 produces 8x faster** in the Ammo-O-Matic than 5.56

The builds that the community calls "trash tier" are trash tier because the community is working with wrong numbers. The game data tells a different story.

---

## Data Files

- Damage calculator: `perkolatr/damage_calculator.py`
- Legendary effects database: `data/fallout76/legendary_effects.json`
- Source curve tables: `data/fallout76/tempest_data/misc/curvetables/json/legendarymods/` (108 files)
- Wiki discrepancies: `findings/fo76/057-legendary-magnitudes.md`
- Mutation values: `findings/fo76/033-mutation-values.md`
- Economy model: `findings/fo76/034-economy-model.md`
- XP system: `findings/fo76/037-xp-leveling-system.md`
- Weapon curves: `findings/fo76/028-damage-curve-tables.md`
