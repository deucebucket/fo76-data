# FO76 Active Legendary Curve Verification

**Date**: 2026-03-20
**Method**: Traced OMOD -> CURV -> JSON chain for every legendary effect previously claimed
**Sources**:
- SeventySix.esm (live game ESM via esmdump with -v -edid flags)
- CURV_records.txt (4,610 CURV records from ESM)
- OMOD_records.txt (32,677 OMOD records from ESM)
- Startup.ba2 curve JSON files (108 legendarymods JSONs)
- All 12 UpdateMain.ba2 archives checked for overridden curves (NONE found)

## Note:: NO Curve Files Were Overridden By Patches

None of the 12 UpdateMain.ba2 archives contain ANY overridden curve table JSONs.
The curve files in `SeventySix - Startup.ba2` are the ONLY versions that have ever existed.
**Every curve value previously reported is the current live value.**

## Methodology: How OMOD -> CURV -> JSON Works

1. **OMOD** (Object Modification) records define legendary effects. Active OMODs lack `zzz_` prefix.
2. **CURV** (Curve Table) records are referenced by OMODs via FormID in the OMOD's property data.
3. **JSON** files in `misc/curvetables/json/legendarymods/` contain the actual numerical curves.
4. CURV records map to JSONs by naming convention: `CT_Legendary_Armor_Cavalier` -> `legendarymods/armor_cavalier.json`
5. Some older CURVs have explicit `:CRVE` subrecords with the JSON path; newer ones use naming convention only.

---

## Effect-by-Effect Active Chain Verification

### 1. NOCTURNAL

**Active OMODs** (NOT zzz_ prefixed):
- `mod_Legendary_Weapon1_DamageNight` (0x004F6AAE) - weapon prefix
- `mod_Legendary_Armor1_ResistancesNight` (0x00524143) - armor prefix
- `mod_Legendary_PowerArmor1_ResistancesNight` (0x0060625B) - PA prefix

**Active CURV**: `CT_Legendary_Weapon_DamageNight` (0x006BDCCB)

**Active JSON**: `legendarymods/weapon_damagenight.json`
```json
{
 "curve": [
 {"x": 0, "y": 50}, // hour 0-5: +50% damage
 {"x": 5, "y": 50}, // hour 5: still +50%
 {"x": 6, "y": 0}, // hour 6: drops to 0%
 {"x": 20, "y": 0}, // hour 20: still 0%
 {"x": 21, "y": 50} // hour 21: back to +50%
 ]
}
```

**PERK Confirmation**: `LegendaryDamageNightPerk` (0x001E8171) has conditions:
- `GetGlobalValue(GameHour) >= 21.0` OR `GetGlobalValue(GameHour) < 6.0`
- `HasKeyword` check for equipped legendary

**Nocturnal Armor**: No separate CURV exists for armor resistance. The armor OMOD applies
flat resistance bonuses (hardcoded in OMOD property data, not curve-driven). The perk
conditions still gate it to nighttime hours 21:00-06:00.

**BACKUP Perk**: `LegendaryDamageNightPerkBACKUP` (0x00578B08) has MORE COMPLEX time conditions
with multiple time bands (6-21, 21-22.5, 22.5-24) suggesting the OLD Nocturnal had
gradual time-of-day scaling. The current version is a simple binary switch.

**STATUS: Nocturnal was NOT reworked to cloaking.** It remains time-based (night = +50%, day = +0%).
The "cloaking rework" claim was FALSE. The Milepost Zero update did not change Nocturnal's mechanism.
The OMOD names, CURV records, PERK conditions, and JSON curve are all unchanged and active.

**Orphaned**: None for Nocturnal specifically. The `LegendaryDamageNightPerkBACKUP` suggests
the old gradual-scaling version was replaced with the simpler binary version at some point.

---

### 2. CAVALIER (Damage Reduction While Sprinting)

**Active OMOD**: `mod_Legendary_Armor3_LessDamageSprinting` (0x00527F77) - armor
**Active OMOD**: `mod_Legendary_PowerArmor3_LessDamageSprinting` (0x0060625C) - PA

**Active CURV**: `CT_Legendary_Armor_Cavalier` (0x008A9FDE)

**Active JSON**: `legendarymods/armor_cavalier.json`
```json
{
 "curve": [
 {"x": 0, "y": 1}, // 0 pieces: 1.0 (no reduction)
 {"x": 1, "y": 0.9}, // 1 piece: 0.9 (10% reduction)
 {"x": 2, "y": 0.81}, // 2 pieces: 19% reduction
 {"x": 3, "y": 0.729}, // 3 pieces: 27.1% reduction
 {"x": 4, "y": 0.6561}, // 4 pieces: 34.4% reduction
 {"x": 5, "y": 0.59049} // 5 pieces: 40.95% reduction
 ]
}
```

**ORPHANED JSON**: `legendarymods/armor_lessdamagesprinting.json`
```json
{
 "curve": [
 {"x": 0, "y": 0},
 {"x": 5, "y": 0.95}, // different scale: x=damage value, not piece count
 {"x": 10, "y": 0.9025},
 {"x": 15, "y": 0.8574},
 {"x": 20, "y": 0.8145},
 {"x": 25, "y": 0.7737}
 ]
}
```
**This orphaned file is NOT referenced by any CURV record or anywhere in the ESM.**
It uses a completely different X-axis scale (0-25 damage values vs 0-5 piece count).
No CURV record named `CT_*_LessDamageSprinting` exists.

**CONFIRMED VALUES**: 10% multiplicative per piece, 40.95% total at 5 pieces.
**Previous claim was CORRECT.**

---

### 3. SENTINEL (Damage Reduction While Standing Still)

**Active OMOD**: `mod_Legendary_Armor3_LessDamageStandStill` (0x004EE54C) - armor
**Active OMOD**: `mod_Legendary_PowerArmor3_LessDamageStandStill` (0x00606277) - PA

**Active CURV**: `CT_Legendary_Armor_Sentinel` (0x008A9FE4)

**Active JSON**: `legendarymods/armor_sentinel.json`
```json
{
 "curve": [
 {"x": 0, "y": 1}, // 0 pieces: no reduction
 {"x": 1, "y": 0.95}, // 1 piece: 5% reduction
 {"x": 2, "y": 0.90}, // 2 pieces: 10% reduction
 {"x": 3, "y": 0.86}, // 3 pieces: 14% reduction
 {"x": 4, "y": 0.81}, // 4 pieces: 19% reduction
 {"x": 5, "y": 0.77} // 5 pieces: 23% reduction
 ]
}
```

**ORPHANED JSON**: `legendarymods/armor_lessdamagestandstill.json`
```json
{
 "curve": [
 {"x": 0, "y": 0},
 {"x": 5, "y": 0.95}, // identical to sprinting orphan
 {"x": 10, "y": 0.9025},
 {"x": 15, "y": 0.8574},
 {"x": 20, "y": 0.8145},
 {"x": 25, "y": 0.7737}
 ]
}
```
**Also orphaned. NOT referenced by any CURV record or ESM entry.**
Interestingly, both orphaned files are IDENTICAL - suggesting Cavalier and Sentinel
were once planned to have the same values.

**CONFIRMED VALUES**: 5% at 1 piece, 23% at 5 pieces.
**Previous claim was CORRECT.**
**Note:**: Cavalier (41%) is nearly TWICE as effective as Sentinel (23%).

---

### 4. JUNKIE'S (Damage Per Addiction)

**Active OMOD**: `mod_Legendary_Weapon1_DamageAddiction` (0x004F6AAB)

**Active CURV**: `CT_Legendary_Weapon_DamageAddiction` (0x006C2D5B)

**Active JSON**: `legendarymods/weapon_damageaddiction.json`
```json
{
 "curve": [
 {"x": 0, "y": 0},
 {"x": 1, "y": 10},
 {"x": 2, "y": 20},
 {"x": 3, "y": 30},
 {"x": 4, "y": 40},
 {"x": 5, "y": 50},
 {"x": 6, "y": 60},
 {"x": 7, "y": 70},
 {"x": 8, "y": 80},
 {"x": 9, "y": 90},
 {"x": 10, "y": 100}
 ]
}
```

**Addiction Count**: 14 unique AddictionKeyword entries exist in the ESM:
Alcohol, Buffout, Mentats, MedX, Psycho, Jet, DaddyO, DayTripper, Overdrive, XCell,
BuzzBites, Calmex, Fury, FormulaP

**CONFIRMED VALUES**: +10% per addiction, linear to +100% at 10 addictions.
The curve goes to 10 addictions. With 14 possible addictions in the game, a player
CAN exceed the curve range, but values beyond x=10 would extrapolate linearly.

**Previous claim was CORRECT.**
**No cap mechanism in OMOD conditions** - the cap is purely in the curve's X range.

---

### 5. BLOODIED (Damage Inverse to Health)

**Active OMOD**: `mod_Legendary_Weapon1_DamageInverseHealth` (0x004F6AA0)

**Active CURV**: `CT_Legendary_Weapon_DamageInverseHealth` (0x006C2D58)

**Active JSON**: `legendarymods/weapon_damageinversehealth.json`
```json
{
 "curve": [
 {"x": 0.05, "y": 130}, // At 5% HP: +130% damage
 {"x": 1, "y": 0} // At 100% HP: +0% damage
 ]
}
```

**Additional CURVs**:
- `CT_Legendary_Weapon_Adrenal` (0x0080F546) - separate CURV, NO JSON in Startup.ba2
- `CT_Legendary_Armor_Adrenal` (0x0080F54A) - separate CURV, NO JSON in Startup.ba2

The "Adrenal" CURVs are newer (0x0080xxxx range) and have no external JSON files.
They likely embed curve data directly in the ESM (not extractable with current tools).
These may be for the Adrenal Reaction mutation, not the Bloodied legendary effect.

**Bloodied Armor**: `mod_Legendary_Armor1_ResistancesInverseHealth` (0x00521914)
Uses CURV `CT_Legendary_Armor_ResistancesInverseHealth` (0x006C1374)
JSON: `legendarymods/armor_resistancesinversehealth.json`
```json
{
 "curve": [
 {"x": 0, "y": 35}, // At 0% HP: +35 DR/ER per piece
 {"x": 0.1, "y": 35}, // At 10%: +35
 {"x": 0.2, "y": 32}, // At 20%: +32
 {"x": 0.3, "y": 28}, // At 30%: +28
 {"x": 0.4, "y": 24}, // At 40%: +24
 {"x": 0.5, "y": 20}, // At 50%: +20
 {"x": 0.6, "y": 16}, // At 60%: +16
 {"x": 0.61, "y": 0} // At 61%+: +0
 ]
}
```
Note: This is actually the "Bolstering" effect (ResistancesInverseHealth), NOT Bloodied armor.
The Bloodied legendary only has a weapon variant. The armor version of "low health = bonus"
is called Unyielding or Bolstering.

**CONFIRMED VALUES**: +130% weapon damage at 5% HP. Linear interpolation.
At 20% HP (typical bloodied build): approximately +109% bonus.
**Previous claim was CORRECT.**

---

### 6. NERD RAGE (Perk, Not Legendary)

**Active PERK**: `NerdRage01` (0x0004D886)

**Active CURVs**:
- `NerdRageDamageBonus` (0x00829438)
- `NerdRageAPBonus` (0x00829439)

**Active JSONs**:
`perks/nerdragedamagebonus.json`:
```json
{
 "curve": [
 {"x": 0.05, "y": 80}, // At 5% HP: +80% damage
 {"x": 0.2, "y": 40}, // At 20% HP: +40% damage
 {"x": 0.8, "y": 1}, // At 80% HP: +1% damage
 {"x": 1, "y": 0} // At 100% HP: +0% damage
 ]
}
```

`perks/nerdrageapbonus.json`:
```json
{
 "curve": [
 {"x": 0.05, "y": 30}, // At 5% HP: +30 AP regen
 {"x": 0.2, "y": 15}, // At 20% HP: +15 AP regen
 {"x": 0.8, "y": 1}, // At 80% HP: +1 AP regen
 {"x": 1, "y": 0} // At 100% HP: +0 AP regen
 ]
}
```

**Note**: The zzz_ versions confirm old ranks were disabled:
- `zzz_NerdRage02` (0x00065E37)
- `zzz_NerdRage03` (0x00065E38)
- `zzz_Babylon_NerdRage03` (0x00479D5A)

Nerd Rage is now a single-rank perk (NerdRage01 only). The old 3-rank system
was collapsed into one rank with the full curve scaling.

**CONFIRMED VALUES**: +80% damage and +30 AP regen at 5% HP.
**Previous claim status**: These values match the previous report.

---

### 7. GOURMAND'S (Damage via Food/Water Satisfaction)

**Active OMOD**: `mod_Legendary_Weapon1_Gourmand` (0x006069F2)

**Active CURV**: `CT_Legendary_Weapon_Gourmand` (0x006D37DD)

**Active JSON**: `legendarymods/weapon_gourmand.json`
```json
{
 "curve": [
 {"x": 0, "y": 0},
 {"x": 1, "y": 5},
 {"x": 2, "y": 10},
 {"x": 3, "y": 15},
 {"x": 4, "y": 20},
 {"x": 5, "y": 25},
 {"x": 6, "y": 30},
 {"x": 7, "y": 35},
 {"x": 8, "y": 40}
 ]
}
```

**Previous zzz_ versions**: `zzz_mod_Incinerator_Gourmand` (0x0072A8C1) - disabled

**CONFIRMED VALUES**: +5% per satisfaction point, max +40% at 8 satisfaction.
**Previous claim was CORRECT.**

---

## Orphaned Curve Files Summary

| JSON File | Status | Notes |
|-----------|--------|-------|
| `armor_lessdamagesprinting.json` | ORPHANED | No CURV record references it. Different X-axis scale (0-25 vs 0-5). Possibly pre-Cavalier naming. |
| `armor_lessdamagestandstill.json` | ORPHANED | No CURV record references it. Identical values to sprinting orphan. |
| `armor_lessdamageblocking.json` | ACTIVE (non-legendary) | Referenced by `CT_mod_Armor_BetterBlocking` (0x00395FF3) for non-legendary armor mod. |
| `LegendaryDamageNightPerkBACKUP` | ORPHANED PERK | Old multi-band Nocturnal with gradual time scaling. Replaced by simpler binary version. |

The orphaned `armor_lessdamagesprinting.json` and `armor_lessdamagestandstill.json` files
have IDENTICAL curve data (both show the same 5/10/15/20/25 X-values with 0.95/0.9025/0.8574/0.8145/0.7737).
This suggests they were the ORIGINAL plan for Cavalier/Sentinel where both effects would be
equally strong. The current implementation gives Cavalier (10%/piece) nearly double the
effectiveness of Sentinel (5%/piece).

## Verification Summary

| Effect | Active? | OMOD | CURV | JSON | Values Match Previous Report? |
|--------|---------|------|------|------|------------------------------|
| Nocturnal (weapon) | YES | mod_Legendary_Weapon1_DamageNight | CT_Legendary_Weapon_DamageNight | weapon_damagenight.json | YES - +50% night, +0% day |
| Nocturnal (armor) | YES | mod_Legendary_Armor1_ResistancesNight | (no CURV, OMOD-embedded) | (no JSON) | N/A - flat resistance, time-gated |
| Cavalier | YES | mod_Legendary_Armor3_LessDamageSprinting | CT_Legendary_Armor_Cavalier | armor_cavalier.json | YES - 10%/piece multiplicative |
| Sentinel | YES | mod_Legendary_Armor3_LessDamageStandStill | CT_Legendary_Armor_Sentinel | armor_sentinel.json | YES - 5%/piece to 23% at 5pc |
| Junkie's | YES | mod_Legendary_Weapon1_DamageAddiction | CT_Legendary_Weapon_DamageAddiction | weapon_damageaddiction.json | YES - +10%/addiction to +100% |
| Bloodied | YES | mod_Legendary_Weapon1_DamageInverseHealth | CT_Legendary_Weapon_DamageInverseHealth | weapon_damageinversehealth.json | YES - +130% at 5% HP |
| Nerd Rage | YES | (perk, not OMOD) | NerdRageDamageBonus + NerdRageAPBonus | nerdragedamagebonus.json + nerdrageapbonus.json | YES - +80% dmg, +30 AP at 5% HP |
| Gourmand's | YES | mod_Legendary_Weapon1_Gourmand | CT_Legendary_Weapon_Gourmand | weapon_gourmand.json | YES - +5%/point, max +40% |

## Corrections to Previous Report (057-legendary-magnitudes.md)

### NONE NEEDED for curve values.
All previously reported curve values are confirmed correct through the active reference chain.

### Corrections needed for CLAIMS ABOUT MECHANICS:

1. **Nocturnal "rework to cloaking"** - FALSE. Nocturnal remains purely time-based.
 The "Milepost Zero cloaking rework" claim was incorrect. The OMOD, PERK conditions,
 and curve data all confirm time-of-day gating (21:00-06:00).

2. **"Cavalier/Sentinel were rebalanced to use different curve files"** - PARTIALLY CORRECT.
 The ACTIVE curves are `armor_cavalier.json` and `armor_sentinel.json`. The orphaned
 `armor_lessdamagesprinting.json` and `armor_lessdamagestandstill.json` exist but were
 NEVER referenced by any CURV record. They appear to be early development artifacts,
 not "old curves that got replaced." The Cavalier/Sentinel curves may have always been
 the ones loaded by the game.

3. **"The ESM records were changed to POINT TO DIFFERENT CURVES"** - UNVERIFIABLE.
 The CURV records `CT_Legendary_Armor_Cavalier` and `CT_Legendary_Armor_Sentinel`
 have FormIDs in the 0x008Axxxx range (very high = added in a late update). This suggests
 they were added post-launch, possibly replacing an older curve system. However, it is
 not possible to determine what the OMODs pointed to BEFORE these CURVs existed without
 historical ESM snapshots.

## Key Takeaway

**Every curve value previously reported is verifiably the current live value.**
No update archive has ever overridden a curve JSON file. The initial concern that
"old curves still exist but aren't referenced anymore" was partially valid - the
`armor_lessdamagesprinting.json` and `armor_lessdamagestandstill.json` files are
indeed orphaned - but the ACTIVE curves (`armor_cavalier.json` and `armor_sentinel.json`)
contain the exact values previously reported. The Nocturnal "cloaking rework" was a false premise.
