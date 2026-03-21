# FO76 Finding 006: Atlantic City Casino — Complete 6-Game Gambling System

## Status: CONFIRMED — Full multiplayer casino game system in client code
## Source: xpd_ac_casinogame.psc

## Games Implemented
The `CasinoGameToOpen` property defines 6 distinct games:
| Index | Game | Notes |
|-------|------|-------|
| 0 | **Roulette** | Full table |
| 1 | **Derby** | Horse/creature racing? |
| 2 | **Craps** | Dice table |
| 3 | **Slot Machine 1** | Standard slots |
| 4 | **Slot Machine 2** | Variant |
| 5 | **World's Biggest Slot** | Oversized special machine |

## Technical Implementation
- **Multiplayer-aware**: Shows "busy" message if another player is using the machine
- **Power requirement**: Machines need power to function (MessageNoPower)
- **Synced animations**: `ResultAnimationIdx` synced across all clients
- **Server-side results**: Winning number sent from server, animations play on all clients
- **UI integration**: Bet resolution with cap rewards, fanfare display
- **Physical furniture**: Each game has physical furniture with animations

## Disabled Components
- `$CASINO_ERROR_CASINO_DISABLED` — Server-side toggle exists
- The furniture exists in Atlantic City Expedition content
- All UI elements are present

## Possible Reasons for Disabling
- Gambling mechanics in a game with real-money microtransactions (Atoms) could face regulatory issues
- Some regions have strict laws about gambling in games
- May be waiting for a specific content update to activate
- Could be a seasonal event feature

## Further Investigation
- Search for cap bet amounts and payout tables in curve tables
- Check if "Derby" refers to horse racing or creature racing (brahmin? radstag?)
- Look for casino-specific perk cards or bonuses
