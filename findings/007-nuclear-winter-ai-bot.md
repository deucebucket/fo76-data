# FO76 Finding 007: Nuclear Winter Automated Playtesting Bot

## Status: CONFIRMED — Complete AI bot for automated battle royale testing
## Source: babylontest.psc

## What It Does
A fully automated player bot that:
1. **Selects weapons** from 12 pre-defined loadouts (by Form ID)
2. **Auto-fires** on a random timer (1.9-2.1 seconds between shots)
3. **Auto-reloads** when magazine is empty
4. **Auto-loots** supply drops (BabylonBag keyword) on 29-31 second timer
5. **Navigates toward storm zone center** when outside safe zone
6. **Alternates movement direction** (left/right flanking) when repositioning
7. **Teleports to loot bags** within 5000 unit radius

## Weapon Loadouts (12 weapons with Form IDs)
All 12 weapon types with specific ammo types and counts are hardcoded. Some weapons get 100 rounds, others get 10 (likely heavy/explosive weapons).

## What This Tells Us
- Bethesda had automated testing infrastructure for Nuclear Winter
- The bot simulates realistic player behavior (fire, loot, move to zone)
- `IsInsideStormZone(500.0)` and `GetHeadingToStormZoneCenter()` are native engine functions
- The storm zone system is built into the engine at a native level, not just scripted
- These native functions still exist in the current build

## Significance
- The battle royale infrastructure is MORE deeply integrated than previously thought
- Storm zone mechanics are native engine features, not removable without engine changes
- This lends weight to the theory that Nuclear Winter could return
