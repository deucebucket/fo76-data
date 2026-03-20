# FO76 Finding 008: Babylon Bot as AI Follower Reference Architecture

## Status: OPPORTUNITY — Bethesda's own automated player bot can inform AI companion project
## Source: babylontest.psc, cross-reference with AI Companion project

## What the Babylon Bot Provides
The Nuclear Winter test bot demonstrates Bethesda-approved patterns for:

### Navigation
- `MoveTo(target)` — teleport to reference
- `GetHeadingToStormZoneCenter()` — heading calculation (equivalent patterns exist for any target)
- `DoMove(heading, time)` — directional movement
- `FindRandomReferenceWithKeyword()` — spatial search within radius

### Combat
- Weapon selection from loadout (12 weapons with Form IDs)
- Fire timing (randomized intervals for realistic behavior)
- Reload management (count-based magazine tracking)
- Multiple weapon types (ranged, heavy, explosive)

### Looting
- Keyword-based item search (`BabylonBagKeyword`)
- Proximity-based pickup (5000 unit radius)
- Timer-based loot cycles (29-31 second intervals)

### AI Decision Loop
```
While alive:
  - Check if in safe zone
  - If not: navigate toward center
  - Alternate flanking direction
  - Fire at intervals
  - Loot at intervals
  - Wait between decisions
```

## Connection to AI Companion Project
This + Mantella + GPT-SoVITS = an AI that:
- Moves and fights using Bethesda's own patterns
- Makes decisions via LLM
- Speaks in cloned NPC voices
- Could play FO76 cooperatively as a teammate

## Technical Requirements
- Second FO76 account or Fallout 1st private server
- Input injection for a second game instance
- LLM integration for decision-making (replacing hardcoded timers)
- Screen reading for situational awareness (Qwen2.5-VL already set up)

## Key Insight
Bethesda ALREADY BUILT the bot behavior. We just need to replace the hardcoded logic with an LLM brain.
