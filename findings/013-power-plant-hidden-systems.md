# FO76 Finding 013: Power Plant Hidden Complexity — Entropy, Decay, and Server Scaling

## Status: CONFIRMED — Complete system with hidden constants
## Source: powersystemdatascript.psc

## Hidden Constants

### Fuel System
- `PowerToFuelRatio = 0.00741` — Converts power output to fuel consumption
- `FuelConsumptionTimerIntervalSeconds = 600` — Fuel checked every 10 minutes
- `RefuelQuest starts at 2 hours remaining fuel`
- `RefuelQuest completes at 48 hours remaining fuel`
- Each fuel item has a FuelValue that determines how long it powers the plant

### Entropy (Natural Decay)
- `EntropyBaseTimeToPlantFailureDays = 7.0` — Plants fail in 7 days without maintenance
- `EntropyBreakdownWhileOffRateDays = 2.0` — Powered-off plants decay in 2 days
- `EntropyMaxThresholdPercent = 15.0` — Entropy stops at 15% health (never fully kills)
- `EntropyTimerIntervalSeconds = 600` — Decay updates every 10 minutes
- `InitialDamageVariance = 15.0` — Random starting damage so subsystems aren't identical

### SERVER SCALING (mostly TODO but framework exists)
- `EntropyPlayerCountBase = 10.0` — Baseline player count
- `EntropyPlayerCountMultiplier = 1.0` — Plants decay faster with >10 players
- `EntropyHealthMultiplier = 1.0` — Decay accelerates as health drops (exponential)
- These are marked TODO but the framework is live and the defaults are active

### Subsystem Failure
- `SubsystemFailureThresholdPercent = 25.0` — Below 25% = system shutdown
- `RepairQuest starts at 40%` health
- `RepairQuest completes at 60%` health
- `CoolingTowerLockdownMaxTimeMinutes = 10.0` — Cooling tower can be disabled for max 10 min

### Change System
- `ChangeSubquestDuration = 900.0` — Power system changes take 15 minutes
- `ChangeSubquestDelaySeconds = 1800.0` — 30-minute cooldown between changes

## Why These Values Are Not Visible to Players
- Power plants appear to "just work" because the entropy system is slow (7 days)
- Most servers reset before entropy becomes noticeable
- The player count scaling creates invisible difficulty that players attribute to "bad luck"
- The refuel/repair quest triggers seem random but are based on these exact thresholds

## Festive Scorched Legendary Rates
From `festive_legendaryscorched.psc`:
- 2-star and 3-star chances controlled by **Live Content Scheduler**
- Bethesda changes these rates during holiday events SERVER-SIDE
- Players can't determine the actual rates from gameplay alone
