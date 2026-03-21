# FO76 Finding 022: Cover Combat System — Built, Animated, Then Pulled

## Status: PULLED — 30+ animations in Update 11, removed in Update 12
## Source: Update archive diff, ESM game settings

## Evidence

### ESM Game Settings (Still Present)
- `fPlayerCoverGunDownDelayTime` — Time to lower weapon behind cover
- `fPlayerCoverGunUpDelayTime` — Time to raise weapon from cover
- These are ENGINE-LEVEL settings, meaning cover combat was integrated into the core

### Update 11 Animations (30+, Now Removed)
- Standing cover animations
- Crouching cover animations
- Blind fire from cover
- Grenade throws from cover
- Peek/lean animations

### Related ESM Content
- `AnimFurnDeathclawPeekIntoDoorwayAmbush` — Deathclaws have PEEK animations (suggests cover/peek was planned for NPCs too)
- `AnimFurn_GhoulLeaning` — Ghouls have leaning animations
- Combat dialogue: "Cover me!" (`sTopicSubtypeTextCombatCoverMe`) and "Take cover!" orders

### What Was Pulled
All 30+ cover combat animations were present in Update 11 but absent in Update 12. The game settings remain in the ESM but the player-facing animations were removed.

## Implications
1. Bethesda built a COMPLETE cover-based combat system for FO76
2. NPCs (Deathclaws, Ghouls) already have cover/peek animations
3. The engine supports it at the game settings level
4. It was tested and pulled — possibly for gameplay feel, performance, or PvP balance
5. The infrastructure still exists and could be re-enabled

## Notes
- Cover combat would fundamentally change FO76's gameplay loop
- Could be planned for a future "tactical" game mode or private server option
- May have been pulled because it favors ranged builds too heavily
- The NPC animations suggest it was planned as a TWO-WAY system (players and NPCs both use cover)
