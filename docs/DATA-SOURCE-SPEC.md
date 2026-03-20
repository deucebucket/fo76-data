# Data Source Specification — Every Value Must Be Traceable

## Principle
Every numerical value, game mechanic, and data point displayed in any tool (Perkolatr, map, damage calculator) MUST include:

1. **Source File** — which extracted file contains this data
2. **Record Type** — GMST, CURV, GLOB, OMOD, PERK, WEAP, etc.
3. **Form ID** — the exact hexadecimal record identifier
4. **Trust Level** — BAKED, SERVER-TUNABLE, or HYBRID
5. **Patch Version** — which game patch these files were extracted from

## Trust Level Badges

### BAKED (green badge)
Cannot change without a client patch. Safe to publish.
- GMST game settings
- Curve table JSONs (in BA2 archives)
- OMOD effect magnitudes
- Script logic
- Crafting recipes (COBJ)
- Weapon/armor base stats

### SERVER-TUNABLE (yellow badge)
Bethesda can change anytime without notification.
- GLOB values with NTWK flag
- LTT_ drop rate toggles
- LCP_ content switches
- Spawn chance globals
- Event activation states

### HYBRID (orange badge)
Base value is baked, but a server-tunable multiplier can modify it.
- Legendary spawn chance (GMST base + GLOB regional multiplier)
- Event rewards (LVLI base + LTT_ multiplier)
- Flora spawn rates (CURV base + seasonal GLOB toggle)

## Display Format
Every tooltip, popup, or data display should show:

```
Bloodied Damage Bonus: +130% at 5% HP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Source: legendarymods/weap_legendary_bloodied_dmgbonus.json
Type: CURV (Curve Table)
Form ID: 0x008A9FE8
Trust: BAKED ●
Patch: 66 (The Backwoods, March 3 2026)
```

## For the Interactive Map
Item markers should show:
```
Bobblehead Spawn
━━━━━━━━━━━━━━━
Location: Fort Atlas Tunnel
Cell: FtAtlasTunnel_SM_PitRoom
Coordinates: X=4407.6, Y=-10789.3, Z=-5872.7
Base Object: LPI_Loot_Bobbleheads (0x0001911D)
REFR: 0x005EFC02
Trust: BAKED ● (placement is fixed)
Note: Contents determined by LPI leveled list (HYBRID)
```

## For the Build Planner
Perk and damage values should show:
```
Rifleman Rank 3: +30% Damage
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Source: PERK record 0x004A0D6A
Effect: MGEF via CURV reference
Trust: BAKED ●
Stacking: Additive with other damage perks
```
