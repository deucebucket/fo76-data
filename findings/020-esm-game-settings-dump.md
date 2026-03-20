# FO76 Finding 020: ESM Game Settings — 2,822 Hard-Coded Values Extracted

## Status: CONFIRMED — Direct ESM dump via fo76utils
## Source: SeventySix.esm via esmdump

## Tool Used
fo76utils (compiled from source at ~/ai-drive/gamecryptids/tools/fo76utils/)
Command: `./esmdump SeventySix.esm`

## Critical Combat Values

### Action Point Costs
| Action | AP Cost |
|--------|---------|
| Ranged Attack | 30 |
| Two-Hand Melee | 30 |
| Unarmed | 22 |
| One-Hand Melee | 15 |
| Reload | 10 |
| Switch Weapon | 10 |
| Heal | 10 |
| Run and Gun | 0 (FREE) |
| VATS Melee Mult | 1.0x |

### Sneak/Stealth
| Setting | Value |
|---------|-------|
| Melee Sneak Multiplier | 3.0x |
| Stealth Sound Threshold | 25.0 |
| Detection Dialogue Min Time | 10s |
| Detection Dialogue Max Time | 30s |

### PvP
| Setting | Value |
|---------|-------|
| Base Weapon Damage Mult | 0.0 (!!) |
| PvP Damage Factor | 1.5x |
| Player Extra Health Mult | 0.5 (50% more HP) |
| Forced PvP Level | 5 |

### Legendary
| Setting | Value |
|---------|-------|
| Mod Shard Chance | 1.5% |
| Legendary Rarity Base | 6 |
| Epic Keyword Chance | 100% |
| Epic Loot Min PC Level Mult | 0.5 |
| Epic Loot Min Zone Level Mult | 0.5 |

### Movement
| Setting | Value |
|---------|-------|
| Max Speed Multiplier | 150% |
| Carry Weight Speed Penalty Ratio | 4.0 |
| Speed of Sound | 24010 units |

### VATS
| Setting | Value |
|---------|-------|
| Concentrated Fire Bonus | +20 per shot |
| Inside Min Range Penalty Reduction | 75% |
| Recoil Penalty Max | 5 degrees |
| Cone of Fire Penalty Max | 5 degrees |
| Perception Range Influence | 0.5 |

### Bounty Hunting Hidden Perks
| Perk | Trigger Condition |
|------|------------------|
| Burn_Bounty_AntiRich | Target has 1000-5000 caps |
| Burn_Bounty_DamageToHungry | Target hunger ≥ 6000 |
| Burn_Bounty_DamageToIrradiated | Target rads ≥ 600 |
| Burn_BountyHunting_DamageUpPerk | Target is alive (not dead) |

### Nuclear Winter XP (Historical)
| Action | Overseer XP |
|--------|------------|
| Player Kill | 20 |
| Player Down | 10 |
| AI Kill (Elite) | 20 |
| AI Kill (Low/Med) | 5 |
| Nuke Launch | 50 |
| Base XP per level | 1000 |
| XP Growth Rate | 4% per level |

### Misc
| Setting | Value |
|---------|-------|
| Radiation Health Curve | 1.0 |
| Crime Object Damage Buffer | 99999 |
| Fishing Reel Speed | 70 |
| Workshop Light Budget Cost | 1.0 |
| Workshop Spline Budget Cost | 0.25 |
| Public Workshop XP Mult | 0.0 (NO XP from public workshops!) |

## Total Records
- 2,822 Game Settings (GMST)
- 1,963 Perk Records (PERK)
- Full dump saved to: data/fallout76/game_settings_full.txt

## What This Enables
A data-driven build planner using actual game values instead of community-tested approximations.
