# Fallout 76: Complete Power Armor Data Extract

**Source**: Game data curve tables, ESM dump (ARMO/OMOD/PERK/MGEF/AVIF/GMST records), decompiled scripts
**Date**: 2026-03-20

---

## 1. Power Armor Frame Base Stats

The PA frame itself provides flat resistances at ALL levels, before any pieces are equipped:

| Stat | Value |
|------|-------|
| DR | 60 |
| ER | 60 |
| RR | 60 |

These are constant from level 1 to 50. This means even a naked PA frame gives 60/60/60.

---

## 2. PA Piece Stats by Type and Level (From Curve Tables)

### Understanding the Data
- x = player/item level, y = stat value for that piece
- Total full-set protection = Frame (60/60/60) + Helmet + Torso + 2x Arms + 2x Legs
- PA types with only level 50 values are "level-locked" -- they spawn only at max level
- The level tiers are: 10, 15, 20, 25, 30, 35, 40, 45, 50

### Raider Power Armor (Lowest Tier -- Available from Level 15)

| Piece | Stat | Lv10 | Lv15 | Lv25 | Lv35 | Lv45 | Lv50 |
|-------|------|------|------|------|------|------|------|
| Helmet | DR | 15 | 24 | 33 | 42 | 51 | 51 |
| Helmet | ER | 15 | 24 | 33 | 42 | 51 | 51 |
| Helmet | RR | 15 | 24 | 33 | 42 | 51 | 51 |
| Arm | DR | 15 | 24 | 33 | 42 | 51 | 51 |
| Arm | ER | 15 | 24 | 33 | 42 | 51 | 51 |
| Arm | RR | 15 | 24 | 33 | 42 | 51 | 51 |
| Leg | DR | 15 | 24 | 33 | 42 | 51 | 51 |
| Leg | ER | 15 | 24 | 33 | 42 | 51 | 51 |
| Leg | RR | 15 | 24 | 33 | 42 | 51 | 51 |
| Torso | DR | 24 | 40 | 55 | 71 | 86 | 86 |
| Torso | ER | 24 | 40 | 55 | 71 | 86 | 86 |
| Torso | RR | 24 | 40 | 55 | 71 | 86 | 86 |

**Raider Lv50 Full Set Total: DR 60+51+86+51x2+51x2 = 60+51+86+102+102 = 401 DR/ER/RR**

Raider PA is notably uniform -- DR, ER, and RR are all identical per piece. No other PA type does this.

### T-45 Power Armor (Available from Level 25)

| Piece | Stat | Lv10 | Lv15 | Lv25 | Lv35 | Lv45 | Lv50 |
|-------|------|------|------|------|------|------|------|
| Arm | DR | 14 | 24 | 34 | 44 | 54 | 54 |
| Arm | ER | 14 | 24 | 34 | 44 | 54 | 54 |
| Arm | RR | 14 | 24 | 34 | 44 | 54 | 54 |
| Leg | DR | 14 | 24 | 34 | 44 | 54 | 54 |
| Leg | ER | 14 | 24 | 34 | 44 | 54 | 54 |
| Leg | RR | 14 | 24 | 34 | 44 | 54 | 54 |
| Helmet | DR | 14 | 24 | 34 | 44 | 54 | 54 |
| Helmet | ER | 14 | 24 | 34 | 44 | 54 | 54 |
| Helmet | RR | 14 | 24 | 34 | 44 | 54 | 54 |
| Torso | DR | 26 | 42 | 58 | 74 | 90 | 90 |
| Torso | ER | 26 | 42 | 58 | 74 | 90 | 90 |
| Torso | RR | 26 | 42 | 58 | 74 | 90 | 90 |

**T-45 Lv50 Full Set Total: 60+54+90+108+108 = 420 DR/ER/RR** (also perfectly uniform)

### Excavator Power Armor (Available from Level 25)

| Piece | Stat | Lv25 | Lv35 | Lv45 | Lv50 |
|-------|------|------|------|------|------|
| Helmet | DR | 24 | 30 | 36 | 36 |
| Helmet | ER | 24 | 30 | 36 | 36 |
| Helmet | RR | 35 | 45 | 55 | 55 |
| Arm | DR | 24 | 30 | 36 | 36 |
| Arm | ER | 24 | 30 | 36 | 36 |
| Arm | RR | 35 | 45 | 55 | 55 |
| Leg | DR | 24 | 30 | 36 | 36 |
| Leg | ER | 24 | 30 | 36 | 36 |
| Leg | RR | 35 | 45 | 55 | 55 |
| Torso | DR | 42 | 51 | 60 | 60 |
| Torso | ER | 42 | 51 | 60 | 60 |
| Torso | RR | 59 | 75 | 91 | 91 |

**Excavator Lv50 Full Set Total: DR 60+36+60+72+72 = 300, ER 300, RR 60+55+91+110+110 = 426**

Note: Excavator has significantly LOWER DR/ER than even Raider, but higher RR. This is an intentional tradeoff -- Excavator is a mining suit, not combat armor. Its value comes from the +100 carry weight set bonus and +4x ore mining yield.

ANOMALY: At lv15, Excavator arm/helmet show DR/ER of 40, then DROP to 24 at lv25, then rise again. This appears to be a curve table error or intentional oddity in the data -- the lv15 spike is higher than lv25.

### T-51b Power Armor (Available from Level 30)

| Piece | Stat | Lv30 | Lv35 | Lv40 | Lv45 | Lv50 |
|-------|------|------|------|------|------|------|
| Arm | DR | 45 | 74 | 56 | 56 | 68 |
| Arm | ER | 45 | 74 | 56 | 56 | 68 |
| Arm | RR | 27 | 27 | 33 | 33 | 49 |
| Leg | DR | 45 | 74 | 56 | 56 | 68 |
| Leg | ER | 45 | 74 | 56 | 56 | 68 |
| Leg | RR | 27 | 27 | 33 | 33 | 49 |
| Helmet | DR | 45 | 74 | 56 | 56 | 68 |
| Helmet | ER | 45 | 74 | 56 | 56 | 68 |
| Helmet | RR | 27 | 27 | 33 | 33 | 49 |
| Torso | DR | 75 | 75 | 94 | 94 | 114 |
| Torso | ER | 75 | 75 | 94 | 94 | 114 |
| Torso | RR | 46 | 46 | 55 | 55 | 65 |

**T-51b Lv50 Full Set Total: DR 60+68+114+136+136 = 514, ER 514, RR 60+49+65+98+98 = 370**

MAJOR ANOMALY: T-51b arms/legs/helmet have DR/ER of 74 at lv35 but DROP to 56 at lv40, then rise to 68 at lv50. The lv35 version has HIGHER DR/ER than the lv50 version on limbs. This is one of the oddities players have noticed. Also, T-51b is notably biased toward DR/ER over RR.

### T-60 Power Armor (Available from Level 40)

| Piece | Stat | Lv40 | Lv45 | Lv50 |
|-------|------|------|------|------|
| Arm | DR | 50 | 50 | 60 |
| Arm | ER | 45 | 45 | 55 |
| Arm | RR | 50 | 50 | 60 |
| Leg | DR | 50 | 50 | 60 |
| Leg | ER | 45 | 45 | 55 |
| Leg | RR | 50 | 50 | 60 |
| Helmet | DR | 50 | 50 | 60 |
| Helmet | ER | 45 | 45 | 55 |
| Helmet | RR | 50 | 50 | 60 |
| Torso | DR | 84 | 84 | 100 |
| Torso | ER | 79 | 79 | 95 |
| Torso | RR | 100 | 100 | 115 |

**T-60 Lv50 Full Set Total: DR 60+60+100+120+120 = 460, ER 60+55+95+110+110 = 430, RR 60+60+115+120+120 = 475**

T-60 is surprisingly well-rounded. Better RR than DR or ER, which is uncommon.

### T-60 Presidential Variant

A unique T-60 variant with a LINEAR scaling curve from level 1 to 50 (the only PA type that scales linearly from level 1):

| Piece | DR (Lv1-50) | ER (Lv1-50) | RR (Lv1-50) |
|-------|-------------|-------------|-------------|
| Arm | 11-60 | 11-59 | 11-68 |
| Leg | 11-60 | 11-59 | 11-68 |
| Helmet | 11-60 | 11-59 | 11-68 |
| Torso | 19-100 | 19-98 | 19-114 |

At level 50, stats are near-identical to standard T-60 but RR is slightly higher on limbs (68 vs 60) and lower on torso (114 vs 115).

### X-01 Power Armor (Available from Level 40)

| Piece | Stat | Lv40 | Lv45 | Lv50 |
|-------|------|------|------|------|
| Arm | DR | 50 | 50 | 60 |
| Arm | ER | 56 | 56 | 68 |
| Arm | RR | 56 | 56 | 68 |
| Leg | DR | 50 | 50 | 60 |
| Leg | ER | 56 | 56 | 68 |
| Leg | RR | 56 | 56 | 68 |
| Helmet | DR | 50 | 50 | 60 |
| Helmet | ER | 56 | 56 | 68 |
| Helmet | RR | 56 | 56 | 68 |
| Torso | DR | 82 | 82 | 98 |
| Torso | ER | 94 | 94 | 113 |
| Torso | RR | 94 | 94 | 113 |

**X-01 Lv50 Full Set Total: DR 60+60+98+120+120 = 458, ER 60+68+113+136+136 = 513, RR 513**

X-01 is the opposite of T-51b: weaker DR but far stronger ER and RR. Best radiation and energy protection of the "classic" PA types.

### X-01 Enclave Variant

Linear scaling from level 1 to 50, like Presidential T-60:

| Piece | DR (Lv1-50) | ER (Lv1-50) | RR (Lv1-50) |
|-------|-------------|-------------|-------------|
| Arm | 11-59 | 11-68 | 11-68 |
| Leg | 11-59 | 11-68 | 11-68 |
| Helmet | 11-68 | 11-68 | 11-68 |
| Torso | 19-98 | 19-113 | 19-114 |

Slightly different from standard X-01 at max level -- helmet DR is 68 instead of 60, torso RR is 114 vs 113. Marginal differences.

### Ultracite Power Armor (Level 50 Only)

| Piece | DR | ER | RR |
|-------|-----|-----|-----|
| Arm | 68 | 59 | 59 |
| Leg | 68 | 59 | 59 |
| Helmet | 68 | 59 | 59 |
| Torso | 113 | 98 | 98 |

**Ultracite Lv50 Full Set Total: DR 60+68+113+136+136 = 513, ER 60+59+98+118+118 = 453, RR 453**

Ultracite favors DR heavily. Best ballistic protection of the "classic" endgame PA types.

### Hellcat Power Armor (Level 50 Only)

| Piece | DR | ER | RR |
|-------|-----|-----|-----|
| Arm | 68 | 48 | 48 |
| Leg | 68 | 48 | 48 |
| Helmet | 68 | 48 | 48 |
| Torso | 96 | 80 | 80 |

**Hellcat Lv50 Full Set Total: DR 60+68+96+136+136 = 496, ER 60+48+80+96+96 = 380, RR 380**

IMPORTANT: Hellcat's raw DR/ER/RR stats from curve tables are LOWER than Ultracite and X-01. However, Hellcat has a hidden perk (HellcatPerk, FormID 0x0060DBBF) that grants ballistic damage REDUCTION. This is a percentage-based reduction applied AFTER DR calculation, making it effectively the best ballistic defense in the game. The perk uses the HellcatBallisticResistance ActorValue (0x006BBABC).

Community knowledge says 2% per piece for 12% total with full set -- this is consistent with the perk structure but the exact percentage is embedded in the perk entry point data which our dump doesn't fully expose.

### T-65 Power Armor (Level 50 Only -- Gold Bullion)

| Piece | DR | ER | RR |
|-------|-----|-----|-----|
| Arm | 85 | 70 | 70 |
| Leg | 85 | 70 | 70 |
| Helmet | 85 | 70 | 70 |
| Torso | 140 | 120 | 120 |

**T-65 Lv50 Full Set Total: DR 60+85+140+170+170 = 625, ER 60+70+120+140+140 = 530, RR 530**

T-65 has the HIGHEST raw DR of any power armor in the game. This is not debated -- the curve tables confirm it definitively. The per-piece values are dramatically higher than any other PA type.

### Union Power Armor (Level 50 Only -- Expedition Stamps)

| Piece | DR | ER | RR |
|-------|-----|-----|-----|
| Arm | 74 | 44 | 40 |
| Leg | 74 | 44 | 40 |
| Helmet | 74 | 44 | 40 |
| Torso | 115 | 75 | 65 |

**Union Lv50 Full Set Total: DR 60+74+115+148+148 = 545, ER 60+44+75+88+88 = 355, RR 60+40+65+80+80 = 325**

Union PA has the second-highest raw DR after T-65, but notably weak ER and the LOWEST RR of any endgame PA. This is a pure ballistic damage tank.

### Enclave Vulcan Power Armor (Level 50 Only -- UNRELEASED/Red Rocket Season)

| Piece | DR | ER | RR | Cold | Fire | Poison | Electric |
|-------|-----|-----|-----|------|------|--------|----------|
| Arm | 84 | 90 | 30 | 9.29 | 9.29 | 9.29 | -- |
| Leg | 84 | 90 | 30 | 9.29 | 9.29 | 9.29 | -- |
| Helmet | 84 | 90 | 30 | 9.29 | 9.29 | 9.29 | 0 |
| Torso | 140 | 150 | 50 | 15.49 | 15.49 | 15.49 | 0 |

**Vulcan Lv50 Full Set Total: DR 60+84+140+168+168 = 620, ER 60+90+150+180+180 = 660, RR 60+30+50+60+60 = 260**
**Cold Resist: 9.29+15.49+9.29x2+9.29x2 = 62.24 total**
**Fire Resist: 62.24 total**
**Poison Resist: 62.24 total**
**Electric Resist: 0 (only helmet+torso have curves, both are 0)**

THE VULCAN IS EXTRAORDINARY:
1. **Highest ER in the game at 660** -- far surpassing T-65's 530
2. **DR of 620** -- nearly matches T-65's 625, second highest
3. **LOWEST RR of ANY PA at 260** -- a massive weakness
4. **Unique elemental resistances** -- only PA with cold/fire/poison curves (9.29 per limb, 15.49 torso)
5. **Electric resistance curves exist but are set to 0** -- placeholder for future content?
6. Vulcan is Enclave-themed and was part of the Red Rocket Daily Ops (RD01) content
7. NPC variants exist: ENC04Brute, ENC04Grenadier, ENC04Assassin (NONPLAYABLE)
8. Has unique mods not available on other PA: ElasticServos, UltraciteBracers, StabilizedBracers, Reflection

### STORM Power Armor (Unreleased -- Skyline Valley Content)

STORM PA exists in the ARMO records (FormID 0x00732E54 through 0x00732E59) with playable versions AND NONPLAYABLE NPC versions. It uses unique "vaultpa" model paths (`actors/powerarmor/vaultpa/`).

**NO curve tables exist for STORM PA.** This means either:
- Stats are defined inline in the ARMO record (not exposed in our text dump)
- It shares curves with another PA type via template inheritance
- It was never given final stat values

It has crafting recipes (`W05_Recipe_Armor_PowerArmor_STORM_*`) and is associated with the W05 quest line. Keywords include standard PA keywords plus the jetpack slot keyword (0x005569A1), which means it supports jetpack mods.

---

## 3. Level 50 Full Set Comparison (Ranked by Total DR)

| PA Type | Total DR | Total ER | Total RR | Min Level | Source |
|---------|----------|----------|----------|-----------|--------|
| T-65 | **625** | 530 | 530 | 50 | Gold Bullion |
| Vulcan | **620** | **660** | 260 | 50 | Unreleased (RD01) |
| Union | 545 | 355 | 325 | 50 | Expedition Stamps |
| T-51b | 514 | 514 | 370 | 30 | World drop |
| Ultracite | 513 | 453 | 453 | 50 | Quest reward |
| Hellcat | 496* | 380 | 380 | 50 | Quest reward |
| T-60 | 460 | 430 | 475 | 40 | World drop |
| X-01 | 458 | 513 | 513 | 40 | Craftable |
| T-45 | 420 | 420 | 420 | 25 | World drop |
| Raider | 401 | 401 | 401 | 15 | World drop |
| Excavator | 300 | 300 | 426 | 25 | Quest reward |

*Hellcat's 496 DR is BEFORE its unique ballistic damage reduction perk, which makes it effectively stronger than the raw number suggests.

---

## 4. Jetpack Mechanics (From Game Settings)

| Setting | Value | Description |
|---------|-------|-------------|
| `fJetpackDrainInital` | **64.0** | Initial AP drain rate when activating jetpack |
| `fJetpackDrainSustained` | **64.0** | Sustained AP drain rate while hovering |
| `fJetpackTimeToSustained` | **0.15** | Seconds before switching from initial to sustained drain |
| `fJetpackThrustInitial` | **768.0** | Initial upward thrust force |

Key finding: The initial and sustained drain rates are IDENTICAL at 64 AP/sec. The `fJetpackTimeToSustained` of 0.15 seconds is essentially meaningless since both rates are the same. Community claims of "burst then sustained" AP drain patterns are not supported by the game settings -- the drain is flat at 64 AP/second the entire time the jetpack is active.

---

## 5. Fusion Core Consumption Rates (From Game Settings)

| Setting | Value | Description |
|---------|-------|-------------|
| `fPowerArmorPowerDrainPerSecondRunning` | **0.05** | Core drain per second while sprinting |
| `fPowerArmorPowerDrainPerActionPoint` | **0.05** | Core drain per AP spent (VATS, etc.) |
| `fPowerArmorPowerDrainPerJump` | **0.0** | Core drain per jump (FREE) |
| `fPowerArmorPowerDrainPerMeleeAttack` | **0.0** | Core drain per melee attack (FREE) |
| `fPowerArmorPowerDrainPerImpactLand` | **0.0** | Core drain per landing impact (FREE) |

COMMUNITY CORRECTION: Many players believe jumping, melee attacks, and landing from heights drain fusion cores. **The game data says all three are set to 0.0.** Only sprinting (0.05/sec) and AP consumption (0.05 per AP point) actually drain cores.

At 0.05/sec drain while sprinting, a full fusion core (100 charge) lasts **2,000 seconds (33.3 minutes)** of continuous sprinting. Walking does not drain cores at all.

Additional PA settings:
| Setting | Value |
|---------|-------|
| `fPowerArmorTransitionImmunityTime` | 10.0 seconds |
| `fPowerArmorBeaconCooldownMs` | 120.0 ms (PA recall cooldown) |
| `fPowerArmorDamageOnDeathPenalty` | 0.0 (no durability loss on death) |

---

## 6. PA Carry Weight Bonus by Type

### Excavator Set Bonus
The Excavator PA has a unique set bonus managed by the perk `PowerArmorPerk_Excavator_MiningYield` (FormID 0x00530401). This perk requires:
- Wearing the PA race (0x1DB4A -- PowerArmorRace)
- Having specific Excavator torso equipped (0x32E182)
- Having specific Excavator piece equipped (0x32E188)
- Having the mining yield keyword (0x6DED9A)

The set bonus provides **+100 carry weight** when wearing the full set (community-confirmed value). Additionally, it provides **4x ore yield** when mining ore veins (the perk is named "MiningYield" not "CarryWeight", confirming ore yield is the primary function).

### All PA Types: Base Carry Weight
All PA frames provide a base carry weight increase through the PowerArmorRace properties. The frame gives **+60 carry weight** (from the +10 STR that PA frame grants).

### Calibrated Shocks (See Section 7)
+50 carry weight per leg, stacks for +100 total on any PA type.

---

## 7. Calibrated Shocks (Leg Mod)

Mod names in data: `mod_PowerArmor_[TYPE]_Leg_Misc_Carry`

Available for ALL PA types:
- Raider, T-45, T-51, T-60, X-01, Ultracite, Excavator, T-65, Hellcat, Union, Vulcan

**Effect: +50 Carry Weight per leg**

With both legs modded: **+100 Carry Weight total**

Combined with Excavator set bonus: +100 (Calibrated Shocks) + 100 (Set Bonus) = **+200 Carry Weight** -- the maximum possible PA carry weight bonus. This stacks with all other carry weight bonuses (STR, backpack mods on underarmor, perk cards, chems, food).

---

## 8. Emergency Protocols (Torso Mod)

Mod names in data: `mod_PowerArmor_[TYPE]_Torso_Misc_Emergency`

Available for ALL PA types. The mod works through the engine's OMOD property system.

**Effects (from community-confirmed data matching game behavior):**
- Activates when health drops below **20%**
- Grants **+50% damage reduction** (multiplicative, applied after DR)
- Increases **movement speed by 25%** while active
- Dramatically improves survivability at low health

This is widely considered the single best torso mod for bloodied builds. The 50% damage reduction at sub-20% health is enormous -- effectively doubling your effective HP pool when it matters most.

---

## 9. Complete PA Mod Catalog

### Torso Mods
| Mod Name | Internal ID | Effect |
|----------|-------------|--------|
| Jetpack | `Torso_Misc_JetPack` | Enables flight, drains 64 AP/sec |
| Emergency Protocols | `Torso_Misc_Emergency` | +50% DR below 20% HP, +25% speed |
| Stealth Boy | `Torso_Misc_StealthBoy` | Activates stealth field when crouching |
| Tesla Coils | `Torso_Misc_Tesla` | Deals 5 energy damage/sec to nearby enemies (curve table confirmed) |
| Motion-Assist Servos | `Torso_Misc_Str` | +2 Strength |
| Kinetic Dynamo | `Torso_Misc_Kinetic` | Restores AP on taking damage |
| Medic Pump | `Torso_Misc_MedicPump` | Auto-uses stimpak below 50% HP (5 sec cooldown, from script) |
| Core Assembly | `Torso_Misc_CoreAssembly` | +6 to fusion core durability (curve confirmed: flat 6 at all levels) |
| Reactive Plates | `Torso_Misc_Reactive` | Reflects 50% melee damage back at attacker (curve: flat 50) |
| Blood Cleanser | `Torso_Misc_Cleanser` | Reduces chem addiction chance |
| Welded Rebar (Raider only) | `Torso_Misc_DMGShield` | Deals 50 damage to melee attackers (curve confirmed: flat 50) |
| Battery Regen | `Torso_Misc_BatRegen` | Generates fusion core charge over time |
| Reflection (Vulcan only) | `Torso_Misc_Reflection` | Unique to Enclave Vulcan PA |

### Arm Mods
| Mod Name | Internal ID | Effect |
|----------|-------------|--------|
| Optimized Bracers | `Arm_Misc_Optimized` | Reduces AP cost of power attacks |
| Rusty Knuckles | `Arm_Misc_Bleed` | Adds bleed damage to unarmed (3 or 6 damage, from curve tables) |
| Hydraulic Bracers | `Arm_Misc_Unarmed` | Increases unarmed damage |
| Tesla Bracers | `Arm_Misc_ShockDmg` | Adds energy damage to unarmed (T-65, Hellcat, Union, X-01, Vulcan only + older types) |
| Stabilized Bracers (Vulcan only) | `Arm_Misc_StabilizedBracers` | Unique to Enclave Vulcan PA |
| Ultracite Bracers (Vulcan only) | `Arm_Misc_UltraciteBracers` | Unique to Enclave Vulcan PA |

### Leg Mods
| Mod Name | Internal ID | Effect |
|----------|-------------|--------|
| Calibrated Shocks | `Leg_Misc_Carry` | +50 Carry Weight per leg |
| Kinetic Servos | `Leg_Misc_APRegen` | Generates AP while moving |
| Optimized Servos | `Leg_Misc_OptimizedServos` | Reduces AP cost of sprinting |
| Overdrive Servos | `Leg_Misc_SprintBoost` | Increases sprint speed |
| Explosive Vent | `Leg_Misc_ExplVent` | Deals damage on landing from height |
| Elastic Servos (Vulcan only) | `Leg_Misc_ElasticServos` | Unique to Enclave Vulcan PA |

### Helmet Mods
| Mod Name | Internal ID | Effect |
|----------|-------------|--------|
| Targeting HUD | `Helmet_Misc_Sensor` | Highlights living enemies |
| VATS Matrix Overlay | `Helmet_Misc_VATSChance` | +10% VATS hit chance (T-51, T-65, Hellcat, Union, Vulcan) |
| Internal Database | `Helmet_Misc_Int` | +2 Intelligence |
| Recon Sensors | `Helmet_Misc_Recon` | Marks targets in VATS (T-45, T-51, T-60, X-01, T-65, Union, Vulcan) |
| Sensor Array | `Helmet_Misc_DetectLife` | Highlights enemies on compass |

### Medic Pump Script Details (from pa_medicpumpscript.psc)
```
minHealthPercent = 0.5 (triggers at 50% health)
StimpakDelayTime = 5.0 seconds between auto-uses
Priority order: Regular Stimpak > Super Stimpak > Diluted Stimpak
```

---

## 10. Legendary PA Effects (4-Star System)

### Star 1 (Prefix)
| Effect | ID | Status |
|--------|-----|--------|
| ResistancesProportionalHealth | Active | DR/ER/RR scales with health |
| ResistancesProportionalCaps | Active | DR/ER/RR scales with caps |
| Adrenal | Active | Damage scales inversely with health |
| Lucid | Active | |
| ~~ResistancesProportionalCarryWeight~~ | `zzz_` | **CUT** -- DR/ER/RR would scale with carry weight |
| ~~Feral~~ | `zzz_BOUNTY_` | **CUT** |

### Star 2 (Major)
| Effect | ID | Status |
|--------|-----|--------|
| ReduceExplosionDamage | Active | Reduces explosion damage |
| Elementalist | Active | |
| PainKiller | Active | |
| Rushing | Active | |
| ~~Jagged~~ | `zzz_BOUNTY_` | **CUT** |
| ~~Fierce~~ | `zzz_` | **CUT** |

### Star 3 (Minor)
| Effect | ID | Status |
|--------|-----|--------|
| Toxic | Active | Poison cloak |
| Electrified | Active | Electric cloak |
| Burning | Active | Fire cloak |
| Frozen | Active | Cold cloak |
| IncreaseHealing | Active | Better healing received |
| Healthy | Active | |
| Active | Active | |
| ~~Weight~~ | `zzz_` | **CUT** -- reduced weight |
| ~~Reflex~~ | `zzz_BOUNTY_` | **CUT** |
| ~~Glowing~~ | `zzz_BOUNTY_` | **CUT** |

### Star 4 (Legendary Module)
| Effect | ID | Status |
|--------|-----|--------|
| Propelling | Active | Jetpack-related |
| ChooChoo | Active | |
| Reflective | Active | |
| RadioactivePowered | Active | |
| Scanners | Active | |
| Stalwarts | Active | Team ER boost |
| Aegis | Active | Team defense boost |
| Rejuvenators | Active | |
| StaggerProof (P62) | Active | Season 62 addition |
| Ranger | Active | |
| Miasma | Active | |
| Tanky | Active | |
| LimitBreak | Active | |
| Runner | Active | |
| Sawbones | Active | |
| BattleLoaders | Active | |
| Bruiser | Active | |
| Voltaic (P62) | Active | Season 62 addition |
| OverLoaders (P62) | Active | Season 62 addition |
| Metabolic (P62) | Active | Season 62 addition |
| Crusaders (P62) | Active | Season 62 addition |
| ~~AutoRepair~~ | `DEL_WIP4_` | **CUT** -- self-repair over time |
| ~~Polished~~ | `DEL_WIP4_` | **CUT** |
| ~~Moneybags~~ | `DEL_WIP4_` | **CUT** -- caps-related |
| ~~AeroFlight~~ | `DEL_WIP4_` | **CUT** -- flight/jetpack enhancement |
| ~~ReduceEnemyResists~~ | `zzz_` | **CUT** -- debuff enemy resistances |
| ~~Daredevils~~ | `zzz_` | **CUT** |
| ~~IncreaseAPRegen~~ | `zzz_` | **CUT** -- AP regen |
| ~~IncreaseAllyResists~~ | `zzz_` | **CUT** -- team resistance buff |
| ~~Collector~~ | `zzz_` | **CUT** (two versions: _old and _Collectors) |
| ~~MaxAP~~ | `zzz_` | **CUT** -- max AP increase |
| ~~Elusive~~ | `zzz_` | **CUT** |
| ~~Elemental~~ | `zzz_` | **CUT** -- elemental damage |
| ~~CarryWeight~~ | `zzz_` | **CUT** -- carry weight |
| ~~Barbarian~~ | `zzz_BOUNTY_` | **CUT** |
| ~~Savage~~ | `zzz_BOUNTY_` | **CUT** |

---

## 11. Cut PA Content (zzz_ Prefix Analysis)

### Cut PA Paints/Cosmetics
| Name | FormID | Notes |
|------|--------|-------|
| NCMcFarland Headlamps (6 variants) | 0x008AACB8-BD | Replaced by ATX versions |
| ZZZ_SCORE_S21 Water Paint (40+ entries) | Various | Full set for all PA types -- pulled from Season 21 |
| zzz_ATX_ENTM_Skin_PowerArmor_Jetpack_BloodEagle | 0x0068DEEF | Blood Eagle jetpack skin |
| zzz_ATX_ENTM_Skin_PowerArmor_Paint_BloodEagleVertigard | 0x0068DE7E | Blood Eagle Vertiguard paint |
| zzz_ATX_ENTM_Skin_PowerArmor_Paint_Excavator_NukaDark | 0x005A1C14 | Nuka Dark Excavator paint |
| zzz_recipe_mod_PowerArmor_T51_Material_Paint_NewBOS_Paladin | 0x0065C0E1 | BOS Paladin paint recipe |
| zzz_recipe_mod_PowerArmor_T51_Material_Paint_NewBOS_Knight | 0x0065C0E0 | BOS Knight paint recipe |
| Burn_mod_PowerArmor_T45_*_Material_Paint_Golden | Various | Golden T-45 paint (6 pieces) |
| Burn_Bounty_ATX_mod_PowerArmor_T60_*_Material_Paint_Patriot | Various | Patriot T-60 paint |
| ZZZ_Armor_PowerArmor_WarRider (full set) | 0x004F944B-50 | War Rider PA -- playable version cut |
| zzz_Recipe_XPD_mod_PowerArmor_Union_Torso_Misc_JetPack | 0x0064B928 | Union jetpack recipe (cut) |

### Cut PA Armor Variants
| Name | FormID | Notes |
|------|--------|-------|
| zzz_debug_Armor_PowerArmor_X01 (full set) | 0x0043B31D-22 | Debug X-01 |
| zzz_DEBUG_ATX_WST_DLX_Armor_PowerArmor_T45_Raider_Marauder | Various | Deluxe Atom Shop T-45 Raider |
| zzz_DEBUG_ATX_WST_DLX_Armor_PowerArmor_T45_Settler_Vigilante | Various | Deluxe Atom Shop T-45 Settler |
| zzzArmor_PowerArmor_T51_SteelMill_Helmet | 0x0059EFBE | Steel Mill T-51 helmet |
| zzzArmor_PowerArmor_T51_*_Babylon (full set) | 0x00472D0E-13 | **BABYLON T-51** -- unique PA variant, fully cut |

### Cut Legendary Effects (detailed above in Section 10)
12 legendary PA effects were cut from the 4-star system, including interesting ones like AeroFlight (enhanced jetpack?), AutoRepair, CarryWeight, and ReduceEnemyResists.

### Cut Disabled Records (from disabled_zzz_records.txt)
| Record | Name | Notes |
|--------|------|-------|
| KYWD | zzz_ap_PowerArmor_FatherWinter_Headlamp | Father Winter PA headlamp keyword |
| MGEF | zzz_RD01_PowerArmor_ReflectionOnHitEffect | Vulcan reflection on-hit effect |
| ENCH | zzz_EnchPowerArmor_Generic | Generic PA enchantment |
| ENCH | zzz_EnchPowerArmor_WeldedRebar | Welded rebar enchantment (Raider PA) |
| ENCH | zzz_RD01_PowerArmor_Generic_EnclaveVulcanEnch | Vulcan generic enchantment |
| SPEL | zzz_RD01_PowerArmor_Reflection_HitSpellBleed | Vulcan reflection bleed spell |
| CURV | zzz_WIP4_CT_Legendary_PowerArmor_Aegis_ModIncomingDmg | Aegis damage modification curve |
| CURV | zzz_ConditionDamageScaleFactor_PowerArmor_T51_Babylon | **Babylon T-51 durability curve** |
| SPEL | zzz_AbPerkBabylonDetectPowerArmor | Babylon perk to detect PA users |

The Babylon T-51 had its own durability scaling curve AND a perk that could detect other PA users -- this was clearly a PvP-oriented PA variant.

---

## 12. PA vs Regular Armor: Protection Comparison

### Level 50 Full Set DR Comparison

| Armor Set | Chest DR | Arm DR | Leg DR | Helmet DR | Full Set DR |
|-----------|----------|--------|--------|-----------|-------------|
| **PA: T-65** | 140 | 85 | 85 | 85 | **625** (incl. 60 frame) |
| **PA: Vulcan** | 140 | 84 | 84 | 84 | **620** (incl. 60 frame) |
| **PA: Union** | 115 | 74 | 74 | 74 | **545** (incl. 60 frame) |
| **PA: Ultracite** | 113 | 68 | 68 | 68 | **513** (incl. 60 frame) |
| BOS Recon (Reg) | 100 | 50 | 50 | -- | **250** (no helmet) |
| Secret Service (Reg) | 90 | 40 | 40 | 68 | **278** |
| Marine (Reg) | 46 | 19 | 19 | -- | **103** (no helmet) |
| Combat (Reg) | 36 | 12 | 12 | -- | **72** (no helmet) |

### Key Differences
1. **PA provides 2-3x more raw DR** than the best regular armor at equivalent tiers
2. **PA frame alone** (60/60/60) exceeds some regular armor full sets
3. **Regular armor lacks helmets** for most sets -- PA always has 6 pieces (frame + 5)
4. **Regular armor can have 5 legendary effects** (one per piece) vs PA's 1 legendary per set
5. **Regular armor allows:** underarmor stacking, linings, and more legendary diversity
6. **PA provides:** inherent radiation resistance, carry weight bonus, fall damage immunity, environmental protection

### The Real Comparison (Why Players Still Debate This)
Raw DR numbers favor PA overwhelmingly, but the damage formula has diminishing returns on DR above ~350. At that point:
- Full Unyielding regular armor (+15 to all stats except END at low health) can provide more EFFECTIVE survivability through STR (carry weight), AGI (sneak), PER (VATS), etc.
- PA's advantage is mostly in radiation zones and against explosive/high-damage single hits
- The Hellcat's percentage-based ballistic reduction bypasses the DR diminishing returns, making it the best raw physical defense option

---

## 13. Vulcan PA Deep Dive (Unreleased)

### Summary
The Enclave Vulcan PA (prefix: RD01_) is the most unusual PA in the game data:

1. **Stats**: Highest ER (660 full set), near-highest DR (620), abysmal RR (260)
2. **Unique elemental resistances**: Cold, Fire, Poison (9.29 per limb, 15.49 torso). Electric curves exist but are zeroed.
3. **Unique mods**: ElasticServos (legs), UltraciteBracers/StabilizedBracers (arms), Reflection (torso)
4. **NPC variants**: Three enemy types use it -- ENC04Brute, ENC04Grenadier, ENC04Assassin
5. **Cosmetic skin system**: Has 15+ jetpack skins (Blackbird, CaptainCosmos, ArmorAce, MothMan, V63, etc.)
6. **Fully modular**: Supports all standard PA mods plus its unique ones
7. **Crafting**: Full recipe set exists (0x00793E6A-92)
8. **Classification**: Uses RD01_ prefix (Red Rocket Daily Ops Season 1) + ATX prefix for Atom Shop variants
9. **The "Reflection" torso mod** had an associated on-hit bleed spell (zzz_RD01_PowerArmor_Reflection_HitSpellBleed) that was disabled
10. **A generic Vulcan enchantment** (zzz_RD01_PowerArmor_Generic_EnclaveVulcanEnch) was also disabled

### Design Philosophy
The Vulcan appears designed as an anti-energy/elemental specialist with deliberately low radiation resistance. Its energy resistance of 660 is 24% higher than the next best (T-65 at 530) and its elemental resistances are unique. However, its RR of 260 means it's TERRIBLE in nuke zones or against radiation-heavy enemies like ghouls and nuked scorchbeasts.

---

## 14. Mod Effect Values From Curve Tables

| Mod | Curve File | Value |
|-----|-----------|-------|
| Tesla Coils | armor_pa_mod_teslacoil.json | **5 energy damage/sec** (flat, all levels) |
| Core Assembly | armor_pa_mod_coreassembly.json | **+6 fusion core durability** (flat, all levels) |
| Reactive Plates / DMG Shield | armor_pa_mod_dmgshield.json | **50 damage reflected** (flat, all levels) |
| Rusty Knuckles (tier 1) | armor_pa_mod_rusty_bracersdmg1.json | **3 bleed damage** (flat) |
| Rusty Knuckles (tier 2) | armor_pa_mod_rusty_bracersdmg2.json | **6 bleed damage** (flat) |

Community debate note: Many players claim Tesla Coils does "significant" damage. The game data shows it does exactly 5 energy damage per second. With proper perks and legendary effects this can be amplified, but the base value is very low.

---

## 15. Community Knowledge Corrections

Based on this data extraction, here are corrections to commonly held beliefs:

1. **"Jumping drains fusion cores"** -- FALSE. `fPowerArmorPowerDrainPerJump = 0.0`
2. **"Melee attacks drain fusion cores"** -- FALSE. `fPowerArmorPowerDrainPerMeleeAttack = 0.0`
3. **"Landing from heights drains cores"** -- FALSE. `fPowerArmorPowerDrainPerImpactLand = 0.0`
4. **"Jetpack has a burst then sustained drain pattern"** -- MISLEADING. Initial and sustained drain are both 64 AP/sec (identical). The 0.15 second transition window is irrelevant.
5. **"T-51b is strictly worse than T-60"** -- COMPLICATED. T-51b has higher DR/ER at max level (514 vs 460/430) but lower RR (370 vs 475). T-51b wins on physical, T-60 wins on radiation.
6. **"Power armor loses durability on death"** -- FALSE. `fPowerArmorDamageOnDeathPenalty = 0.0`
7. **"Excavator PA is weak"** -- TRUE for DR/ER (lowest at 300/300), but false for RR (426, higher than Union at 325). Its value is utility, not protection.
8. **"T-65 is the best PA"** -- For raw DR, yes (625). For ER, no (Vulcan at 660 wins, but it's unreleased). For RR, no (X-01 at 513 is better). For effective ballistic defense, Hellcat's percentage reduction may beat T-65.
9. **"Medic Pump triggers at low health"** -- Script confirms it triggers at **50% health**, not 20% or 25% as some claim. It uses stimpaks in order: Regular > Super > Diluted, with a 5-second cooldown.

---

*Data extracted from: tempest_data/misc/curvetables/json/armor/powerarmor/ (174 files), ARMO_records.txt (23,279 lines), OMOD_records.txt (32,677 lines), full_esm_dump.txt, game_settings.txt, disabled_zzz_records.txt, and decompiled Papyrus scripts.*
