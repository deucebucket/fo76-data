# FO76 Finding 010: Complete AI Bot Framework — "Agent 76" Reference Material

## Status: CRITICAL OPPORTUNITY — Full game-playing bot architecture for AI companion project
## Source: AutoTestClient scripts (babylontest, exploreworld, grindmonsters, gatherloot, masscombat, etc.)

## Native Engine Functions (Available to ALL Scripts)

### Player Control
```
Player.SetAIDriven(Bool) — AI takes/releases player character control
Player.SetWantSprinting(Bool) — Force sprint state
Player.GetPlayerControls() — Check if human has control
Player.CheckAndSetPlayerAIDriven() — Safe toggle with state check
Player.CheckAndClearPlayerAIDriven() — Safe release with state check
```

### Navigation
```
Player.PathToReference(ObjectReference target, Float tolerance) — AI pathfinding
  - Returns Bool (success/failure)
  - Supports retry logic (Bethesda uses 5 attempts)
Player.MoveTo(ObjectReference target) — Teleport to reference
Player.DoMove(Float heading, Float time) — Directional movement
Player.GetHeadingToStormZoneCenter() — Heading calculation
Player.IsInsideStormZone(Float buffer) — Zone boundary check
```

### Combat
```
Player.FindRandomCombatTarget(Float radius) — Find hostile in radius (10000 units = massive range)
Player.Fight(Actor target) — Engage in combat (sets AIDriven False for combat)
Player.FillAmmo() — Ammunition management
```

### Perception
```
ObjectReference.FindRandomReferenceWithKeyword(Form keyword, Float radius, Bool) — Spatial search
Game.GetFormFromFile(Int formID, String plugin) — Lookup any game object by ID
```

### Environment
```
ObjectReference.Activate(ObjectReference activator, Bool) — Use doors, terminals, items
Game.GetLocalPlayer() — Reference to local player character
```

## Bot Patterns (Copy-Paste Ready)

### Exploration Loop (exploreworld.psc)
1. Set AI driven, enable sprinting
2. Pick random location from list (24 locations with Form IDs)
3. PathToReference to map marker (retry 5x)
4. If location has interiors: Activate door, wait, activate exit door
5. Repeat forever

### Combat Loop (grindmonsters.psc)
1. FindRandomCombatTarget(10000.0)
2. PathToReference to target
3. Fight(target) — releases AI control during combat
4. FillAmmo after combat
5. Repeat until timer expires

### Loot Loop (babylontest.psc)
1. FindRandomReferenceWithKeyword(lootKeyword, 5000.0)
2. MoveTo(lootReference)
3. Timer-based cycles (29-31 second intervals)

### Multi-Client Load Testing
- DistributeClients() — spreads bot players across the map
- DistributeClientsFromFile() — scripted placement
- Supports multiple simultaneous bot instances

## How This Maps to Agent 76

| Bot Function | Agent 76 Equivalent |
|---|---|
| Hardcoded location list | LLM decides where to go |
| Timer-based combat | Vision model detects threats |
| Random target selection | LLM prioritizes targets |
| Scripted door activation | Vision + LLM navigates |
| Hardcoded weapon selection | LLM evaluates loadout |
| Timer-based looting | LLM decides what's worth picking up |

## Key Technical Notes
- `SetAIDriven(True)` gives FULL control — movement, interaction, everything
- `PathToReference` uses the engine's built-in navmesh pathfinding
- Combat temporarily releases AI control (engine handles VATS/shooting)
- All functions are native (C++ engine level), not scriptable by modders without SFE
- SFE is currently broken (as of Backwoods patch) — may need alternative injection method
