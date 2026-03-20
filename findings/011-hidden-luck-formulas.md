# FO76 Finding 011: Hidden LUCK-Based Game Mechanics

## Status: CONFIRMED — Actual formulas extracted from decompiled scripts
## Source: re_objectts05_bombactivatorscript.psc, atxslotmachinescript.psc, arcadecontroller.psc

## Bomb Defusal Formula
```
Roll = Random(0, 100) + (Player.Luck × 0.8) + (Player.Intelligence × 1.6)
Success threshold: ≥ 85.0
```
### What This Means:
- Base success rate without SPECIAL: ~15% (need to roll 85+)
- With Luck 15: +12 to roll → ~27%
- With Intelligence 15: +24 to roll → ~39%
- With both at 15: +36 → ~51% success rate
- With both at 20 (max): +48 → ~63%
- Intelligence is TWICE as effective as Luck for bomb defusal

## Slot Machine Mechanics
- Costs configurable caps per spin
- Results determined by `chanceThreshold` array (0.0 to 1.0 probabilities)
- Three result types: Loss (0), Win (1), Jackpot (2)
- 3 tumblers × 5 possible symbols = 125 combinations
- **HIDDEN LUCK BUFF**: Winning or hitting jackpot grants `ATX_BuffLuck` spell
  - This means WINNING makes you MORE LUCKY for future spins
  - Creates a "hot streak" mechanic most players don't know about
- `ATX_DispellFortifyLuck` keyword suggests the buff can be dispelled

## Arcade Game Luck Bonus
- `bonusTicketMultiplier` is affected by `LuckAV`
- Higher Luck = more tickets from carnival games
- `BonusScoreSFX` and `BonusScoreMSG` play when luck triggers
- This directly affects ticket earning rate and rewards

## Scorchbeast Combat Mechanics
The ScorchbeastRaceScript reveals attack cooldown timers:
- **Ground sonic attack**: min/max cooldown (configurable)
- **Interior sonic attack**: different min/max (usually shorter)
- **Flying sonic attack**: different min/max (usually longer)
- Takeoff, landing, and area explosions are separate events
- Cooldowns are per-weapon, meaning the beast cycles through attacks

## Significance for Build Planning
These hidden formulas mean:
1. LUCK affects more than just critical hits — it influences gambling, bomb defusal, and arcade rewards
2. INTELLIGENCE has a hidden combat bonus in bomb encounters (2x the weight of Luck)
3. Slot machines have a "hot streak" mechanic via the Luck buff
4. Build planners should account for these hidden SPECIAL effects
