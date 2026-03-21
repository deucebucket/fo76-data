# FO76 Finding 027: Cut VR Tutorial Space + Burning Springs Gladiator Arena

## Status: GENUINELY NOVEL — Neither documented by community
## Source: ESM dump FACT/KYWD/CELL records, cross-referenced

## Cut VR New Player Experience

### What Was Built
A virtual reality simulation INSIDE the game as a tutorial/new player experience:

- **VR Space Door**: `TEMP_NPE_VRSpace_Door_Ref` [006FB27E] — A physical door to enter the VR space
- **VR Citizens**: `ZZZNPE_VRCitizenFaction` [007283F3] — Friendly NPCs in the simulation
- **VR Bullies**: `ZZZNPE_VRBullyFaction` [00709C2A] — Hostile NPCs to practice combat against
- **Actor Types**: `ZZZNPE_ActorTypeVRCitizen` [007283F4], `ZZZNPE_ActorTypeVRBully` [00709C2B]
- **Quest**: `ZZZNPE_MQ01_Enjoy` — The tutorial quest was literally called "Enjoy"
- **Generic Residents**: `ZZZNPE_MQ01_Enjoy_IsGenericResident_Keyword` — Populate the VR world
- **Encounter System**: `ZZZNPE_LocEncMainVRBully`, `ZZZNPE_LocEncSubVRBully` — VR bullies had their own encounter zones

### Interpretation
Bethesda designed a VR simulation (like Tranquility Lane from FO3 or The Memory Den from FO4) as a TUTORIAL for new players. You'd enter a door, experience a simulated pre-war or idealized world with citizens, learn combat by fighting "bullies," and then exit to the real wasteland. The quest name "Enjoy" suggests it was meant to be a pleasant introduction before the harsh reality.

This was replaced by the current "Better Tomorrow" new player experience (`NPE_DQ01_BetterTomorrow`).

### Lore Context
A VR tutorial inside Vault 76 would make lore sense — Vault-Tec could have installed a simulation for dwellers to "practice" before Reclamation Day. This mirrors the Anchorage Simulation from FO3.

## Burning Springs Gladiator Arena (The Rust Kingdom)

### What Exists
A full arena combat system in the Rust Kingdom:

- **Arena Throne Trigger**: `BURN_SQ02_LocRef_Arena_ThroneTrigger` [00862567] — A THRONE overlooking the arena (the Rust King watches?)
- **Arena Respawn**: `BURN_SQ02_LocRef_RespawnMarker_Arena` [00854F21]
- **Arena Spikes**: `BURN_SQ02_LocRef_EnableMarker_ArenaSpikes` [00854F1F] — Physical arena decorations
- **Enemy Wave System**: `BURN_SQ01_Arena_EnemyWaveKeyword` — Wave-based arena combat
- **5 Arena Raider Types**: KW1 through KW5 keywords for different arena opponents
- **Arena Fight Faction**: `Burn_SQ01_ArenaFightFaction` [0084E89F]

### Connection to FO4 Combat Zone
Bethesda has now attempted to build a fighting arena in TWO Fallout games:
1. FO4: Combat Zone (massively cut, see Finding 003)
2. FO76: Rust Kingdom Arena (appears to be active in Burning Springs)

### Status
The arena keywords are NOT zzz_ prefixed, meaning this may be LIVE content in Burning Springs. The cut arena spike reference (`ZZZ_BURN_SQ02_LocRef_ArenaSpike_Right`) suggests some elements were trimmed, but the core system shipped.
