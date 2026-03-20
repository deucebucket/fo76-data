# FO76 Finding 009: Complete Bethesda QA Automation Bot Suite

## Status: CONFIRMED — Multiple fully functional game-playing bots ship in client
## Source: Multiple AutoTestClient scripts

## Bot Scripts Found

### ExploreWorld (exploreworld.psc)
- Visits **24 named locations** across Appalachia with map marker Form IDs
- **Pathfinds** to each location using `PathToReference()` with retry logic (5 attempts)
- **Enters interiors** by activating door references, waits 150 seconds inside, exits
- **Supports multi-door interiors** (up to 3 door pairs per location)
- Uses `SetAIDriven(True)` to take control of player character
- Uses `SetWantSprinting(True)` for faster traversal
- Runs in an infinite loop visiting random locations
- Location list includes: Sugar Grove, Allegheny Asylum, Camden Park, Harpers Ferry, etc.

### GrindMonsters (grindmonsters.psc)
- `FindRandomCombatTarget(10000.0)` — finds hostile NPCs within 10,000 units
- Pathfinds to target, engages in combat
- Auto-refills ammunition
- Runs until timer expires

### BabylonTest (babylontest.psc)
- Nuclear Winter battle royale bot (12 weapon loadouts)
- Auto-fire, auto-loot, storm zone navigation

### Other AutoTest Scripts
- `distributeclientsformaxload.psc` — Load testing (max player simulation)
- `distributeclientsfromfile.psc` — Scripted client distribution
- `gatherloot.psc` — Automated looting bot
- `masscombat.psc` — Large-scale combat testing
- `cocandwait.psc` — Cell-of-center teleportation testing
- `damagetest.psc` — Damage calculation testing
- `actorvaluetests.psc` — Actor value verification

## Critical Native Functions Revealed
These are ENGINE-LEVEL functions (not scriptable by players):
```
Player.SetAIDriven(Bool) — Take/release AI control of player character
Player.SetWantSprinting(Bool) — Force sprint state
Player.PathToReference(ObjectReference, Float) — AI pathfinding to target
Player.FindRandomCombatTarget(Float radius) — Spatial enemy search
Player.GetPlayerControls() — Check if player has control
Player.IsInsideStormZone(Float) — Zone boundary check
Player.GetHeadingToStormZoneCenter() — Heading calculation
ObjectReference.FindRandomReferenceWithKeyword(Form, Float, Bool) — Keyword-based spatial search
```

## Significance for AI Companion Project
This is Bethesda's own framework for automated gameplay. It proves:
1. The engine supports AI-driven player characters natively
2. Pathfinding between any two points in the world works
3. Combat targeting and engagement is automatable
4. Door/interior transitions can be scripted
5. The entire game loop (explore → fight → loot → move) can be automated

## What Would Be Needed
- Access to these native functions (requires script extender or modded client)
- LLM replacing hardcoded decision logic
- Vision model for situational awareness beyond script API
- Second FO76 account for multiplayer co-op
