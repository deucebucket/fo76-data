# FO76 Finding 012: 4-Star Legendary Drop — Default 50% Upgrade Chance

## Status: CONFIRMED — Hard-coded default value in decompiled script
## Source: defaultlegendary4starcreatureref.psc

## The Formula
```
Rank4Chance = 0.5 (default)
```
When a creature is set to be a 3-star legendary, it has a **50% chance** to upgrade to 4-star. This is the DEFAULT value — individual creature placements can override it.

## How It Works
1. Creature is tagged with `DefaultLegendary4StarCreatureRef` script
2. If `bForceLegendary = True`, the creature MUST be legendary
3. `LegendaryRank` sets the forced rank (1-3), or random if 0
4. If rank is 3, `Rank4Chance` (0.0-1.0) determines upgrade to 4-star
5. The upgrade roll happens at spawn time, not at kill time

## Key Detail: Per-Placement Override
The `Rank4Chance` property is `Auto Const` — meaning individual creature placements in the world editor can override the default 0.5 value. Specific boss encounters could have 100% (guaranteed 4-star) or lower chances.

## Regular Legendary System (3-star and below)
From `defaultlegendarycreatureref.psc`:
- `bForceLegendary = False` by default — most creatures use the Epic Creature system's probability
- `LegendaryRank = 0` by default — random rank
- Valid ranks: 1-3 (the 4-star system is a SEPARATE script)

## What Players Didn't Know
1. The 50% default — many players assumed it was much lower
2. 4-star is determined at SPAWN, not at loot — server-hopping doesn't reroll it
3. The chance is per-creature-placement, meaning specific world spawns could have different rates
4. `bForceLegendary` can guarantee legendary status regardless of level (overrides the Level 10+ check)

## Build Planner Implications
- Farming 4-star legendaries: find creatures with the 4StarCreatureRef script
- Some bosses may have Rank4Chance = 1.0 (guaranteed)
- The upgrade is binary: either 3-star or 4-star, no intermediate roll
