# Data Trust Levels — What Can Bethesda Change Without A Patch?

Based on Finding 045 (Patch Architecture), confirmed:

## BAKED (Cannot change without client patch download)
These values are in the ESM, BA2 curve table JSONs, or compiled Papyrus scripts.
Players would need to download a new patch for these to change.

- GMST game settings (no SetGameSetting() exists — read-only)
- Curve table JSONs (packed in BA2 archives)
- Weapon base damage tiers (curve JSONs)
- Armor resistance tiers (curve JSONs)
- Legendary effect magnitude curves (curve JSONs in legendarymods/)
- AP costs per action type (GMST)
- DR formula constants (GMST)
- Sneak multiplier (GMST)
- Melee/ranged AP costs (GMST)
- XP formula (GMST: fXPModBase, fXPModMult)
- Leveling formula (GMST)
- Script logic (compiled .pex in BA2)
- Crafting recipes and costs (COBJ records in ESM)
- Weapon/armor mod effects (OMOD records in ESM)
- Native function declarations (engine binary)

**Label: BAKED — accurate to installed patch version**

## SERVER-TUNABLE (Bethesda can change anytime without telling anyone)
These are GLOB values with the NTWK flag, pushed on login.

- LTT_ drop rate toggles and probabilities
- LCP_ content activation switches
- Spawn chance globals (RA_PartyCrasherSpawnChance, etc.)
- Event activation/deactivation
- Seasonal scorched spawn rates
- Fasnacht mask drop rates
- Double XP/Scrip/Gold multipliers
- Bounty hunt toggles
- Daily Ops mutation index
- Any GLOB with NTWK flag (130 confirmed)

**Label: SERVER-TUNABLE — may differ from ESM values on live servers**

## HYBRID (base value baked, but can be modified by server-tunable multipliers)
- Legendary creature spawn chance (base formula in GMST, regional multiplier in GLOB)
- Event reward quantities (base in LVLI, multiplier in LTT_)
- Cap stash contents (base probabilities baked, Cap Collector perk toggle could be LTT)

**Label: HYBRID — base value baked, multiplier may be server-adjusted**
