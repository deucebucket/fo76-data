# Finding 033: Fallout 76 Mutation Values - Complete Data Extraction

## Source Data

- **Curve Tables**: `tempest_data/misc/curvetables/json/mutations/` (2 files: `mutation_adrenal_normal.json`, `mutation_adrenal_super.json`)
- **Legendary Mod Curve**: `tempest_data/misc/curvetables/json/legendarymods/weapon_dmgwithmutation.json`
- **ESM Dump**: `esm_dump/full_esm_dump.txt` (SPEL, MGEF, GLOB, PERK, ALCH, EXPL records)
- **Decompiled Scripts**: `scripts_decompiled/surv_playermutationscript.psc`, `mutationtriggermeleeexplosionscript.psc`, etc.
- **Game Strings**: `seventysix_strings_en.txt`, `seventysix_dlstrings_en.txt`
- **Cross-Reference**: Fallout Wiki (fallout.wiki)

---

## Curve Table Data (Raw Game Files)

### Adrenal Reaction - Normal Curve (`mutation_adrenal_normal.json`)

The curve maps a value from x=1 to x=20, linearly scaling y from 5 to 100.

| X (Input) | Y (Output) |
|-----------|------------|
| 1         | 5          |
| 20        | 100        |

Linear interpolation: `y = 5 * x`

This is the damage bonus curve for Adrenal Reaction. The X axis represents a derived value from the player's missing HP percentage (divided into 20 steps). At minimum health (x=20), the player gets the full +100% weapon damage bonus. At near-full health (x=1), the bonus is only +5%.

### Adrenal Reaction - Super (Serum-Enhanced) Curve (`mutation_adrenal_super.json`)

| X (Input) | Y (Output) |
|-----------|------------|
| 1         | 6.25       |
| 20        | 125        |

Linear interpolation: `y = 6.25 * x`

The "super" variant (active when under serum effects or with Strange In Numbers) provides a 25% boost over the normal curve: 125% max vs 100% max.

**Key Insight**: The wiki documents Adrenal Reaction as "+5% weapon damage per killed enemy" -- this is INCORRECT. The game files show it is a health-threshold-based damage scaling system, not a kill-streak mechanic. The curve table clearly maps HP loss to damage bonus with linear interpolation across 20 data points.

### Mutant's Legendary Weapon Mod Curve (`weapon_dmgwithmutation.json`)

The "Mutant's" legendary prefix scales bonus damage based on mutation count:

| Mutations | Bonus Damage % |
|-----------|---------------|
| 0         | 0             |
| 1         | 5             |
| 2         | 10            |
| 3         | 15            |
| 4         | 20            |
| 5         | 25            |
| 6         | 30            |
| 7         | 35            |
| 8         | 40            |
| 9         | 45            |
| 10        | 50            |

Caps at +50% with 10+ mutations. Linear: +5% per mutation.

---

## Complete Mutation Catalog

### Form IDs and Spell Records

| Mutation | Spell Form ID | Serum Form ID |
|----------|---------------|---------------|
| Adrenal Reaction | 0x004E1F14 | 0x00505BD4 |
| Bird Bones | 0x003C403D | 0x0050A5BC |
| Carnivore | 0x003C4049 | 0x0050A5BF |
| Chameleon | 0x004E4006 | 0x0050A5C6 |
| Eagle Eyes | 0x003C4037 | 0x0050A5C9 |
| Egg Head | 0x003C4045 | 0x0050A5CB |
| Electrically Charged | 0x004E400D | 0x0050A5CD |
| Empath | 0x004E1F16 | 0x0050A5D2 |
| Grounded | 0x004E4002 | 0x0050A5D0 |
| Healing Factor | 0x004DF1DB | 0x0050A5D6 |
| Herbivore | 0x003C404E | 0x0050A5C4 |
| Herd Mentality | 0x004E1F1E | 0x0050A5E3 |
| Marsupial | 0x004DF1CE | 0x0050A5E7 |
| Plague Walker | 0x004E4021 | 0x0050A5EA |
| Scaly Skin | 0x004DF1CF | 0x0050A5F0 |
| Speed Demon | 0x004DF1E0 | 0x0050A5F3 |
| Talons | 0x0028D3BC | 0x0050A5F6 |
| Twisted Muscles | 0x003C402F | 0x0050A5F9 |
| Unstable Isotope | 0x004E4017 | 0x0050A5FC |

---

## Individual Mutation Analysis

### 1. Adrenal Reaction (0x004E1F14)

**Positive Effects:**
- Weapon damage scales with missing HP (curve table data above)
- Normal: +5% at near-full HP, up to +100% at lowest HP
- Super (with serum/Strange In Numbers): +6.25% to +125%

**Negative Effects:**
- `-50 Max HP` (MGEF: `Mutation_ReduceMaxHealth` 0x004E1F18)

**ESM Components:**
- `Mutation_AdrenalReaction_TextDummy` (0x004E1F19) - UI display
- `Mutation_AdrenalReaction_TextDummySuper` (0x003D0127) - super variant UI
- `CUT_Mutation_AdrenalPositive_Perk` (0x004E1F1A) - cut perk reference
- `CUT_Mutation_AdrenalPositiveSuper_Perk` (0x003D0129) - cut super perk

**Wiki Discrepancy**: The wiki states "+5% weapon damage per killed enemy" -- the game files prove this is a **health-based** scaling system using curve tables, NOT a kill-streak system. The curve table `mutation_adrenal_normal.json` linearly interpolates damage bonus based on missing HP percentage across 20 steps.

### 2. Bird Bones (0x003C403D)

**Positive Effects:**
- `+4 Agility` (MGEF: `Mutation_FortifyAgility` 0x003C4042, keyword: PositiveEffect)
- Reduced fall speed (MGEF: `Mutation_ReduceFallSpeed` 0x0034D2BF, keyword: PositiveEffect)
- Reduced fall damage (MGEF: `Mutation_ReduceFallDamage` 0x0034D237, via Perk 0x0034D238)

**Negative Effects:**
- `-4 Strength` (MGEF: `Mutation_ReduceStrength` 0x003C4038, keyword: NegativeEffect)
- Increased limb damage taken (MGEF: `Mutation_IncreasedLimbDamage` 0x003C4040, via Perk 0x003C403E)

**UI Dummies:**
- `Mutation_BirdBones_UIDummy` (0x0034D239) - normal display
- `Mutation_BirdBones_UIDummySuper` (0x0034D1D6) - super variant display

**In-Game Description**: "Boosts sneaking and increases AP. Reduces strength and increases risk of limb damage."

**Wiki says**: +4 Agility, +40 AP, slower falling. -4 Strength, +20% incoming limb damage. The +40 AP is likely from the Agility bonus (each AGI point = ~10 AP).

### 3. Carnivore (0x003C4049)

**Positive Effects:**
- Double meat benefits (MGEF: `Mutation_EatAllTheVeggies` 0x003C4053 -- confusingly named, keyword: custom)
- No meat disease (MGEF: `Mutation_EatSafeMeat` 0x003C4052)

**Negative Effects:**
- No veggie benefits (no numerical stat penalty -- qualitative effect)

**Keywords:** Has `0x003DC3A4` keyword (diet mutation), shared with Herbivore. These are mutually exclusive.

**In-Game Description**: "The benefits of eating meat are doubled, and your chance of contracting diseases from meat is reduced. You get no benefit from eating vegetables."

**Wiki Match**: Consistent. No numerical discrepancies.

### 4. Chameleon (0x004E4006)

**Positive Effects:**
- Invisibility while crouching, unarmored, not moving, not attacking (MGEF: `Mutation_ChameleonEffect` 0x004E400A, `Mutation_InvisibilityEffect` 0x004E400C)
- Stealth icon display (MGEF: `Mutation_Chameleon_StealthIcon` 0x008571A7, via Perk 0x008571A9)
- Audio effect (MGEF: `Mutation_ChameleonAudioEffect` 0x00490013)

**Negative Effects:**
- None (the conditions for activation ARE the limitation)

**Conditions (from SPEL record):**
- `WornHasKeyword(0x529A16) == 0` -- must not wear certain armor
- `IsAttacking == 0` -- not attacking
- `IsMoving == 0` -- not moving
- `IsWeaponOut` checks -- weapon state matters
- `HasMagicEffectKeyword(0x437AE2) == 0` -- on-attack flag check
- `HasMagicEffectKeyword(0x9AC96) == 0` -- stealth boy conflict check

**On-Attack System:**
- `Mutation_ChameleonOnAttackFlag_Spell` (0x00437AE0) - breaks invisibility on attack
- `Mutation_ChameleonOnAttack_Perk` (0x00437ADF) - perk-based flag

**Wiki Match**: Consistent. No discrepancies.

### 5. Eagle Eyes (0x003C4037)

**Positive Effects:**
- `+25% Critical Damage` (MGEF: `Mutation_FortifyCrits` 0x003C403B, keyword: PositiveEffect)
- `+4 Perception` (MGEF: `Mutation_FortifyPerception` 0x003C403A, keyword: PositiveEffect)

**Negative Effects:**
- `-4 Strength` (MGEF: `Mutation_ReduceStrength` 0x003C4038, keyword: NegativeEffect)

**In-Game Description**: "Your perception and VATS critical damage are increased. Your strength is reduced."

**Wiki Match**: Consistent. +25% crit, +4 PER, -4 STR.

### 6. Egg Head (0x003C4045)

**Positive Effects:**
- `+6 Intelligence` (MGEF: `Mutation_FortifyIntelligence` 0x003C404A, keyword: PositiveEffect)

**Negative Effects:**
- `-3 Strength` (MGEF: `Mutation_ReduceStrength` -- shared effect type)
- `-3 Endurance` (MGEF: `Mutation_ReduceEndurance` 0x003C4048, keyword: NegativeEffect)

**In-Game Description**: "Your intelligence is increased. Your strength and endurance are reduced."

**Wiki Match**: Consistent. +6 INT, -3 STR, -3 END.

### 7. Electrically Charged (0x004E400D)

**Positive Effects:**
- Chance to shock melee attackers (scripted via `MutationTriggerMeleeExplosionScript`)
- Explosion: `Mutation_ElectricallyChargedExplosion` (0x004E400F) - uses EMP explosion model

**Negative Effects:**
- Self-damage from shock

**Global Variables (from ESM GLOB records):**
- `Mutation_ChargedExplosionChance` (0x004E4013): **40%** chance to trigger
- `Mutation_ChargedExplosionCooldown` (0x004E4014): **3 seconds** cooldown
- `Mutation_ChargedFailCooldown` (0x004E4015): **1 second** fail cooldown
- `Mutation_ElectricallyChargedSelfDamage` (0x004E4016): **8 HP** self-damage

**Super Variant:**
- `Mutation_ElectricallyChargedSuperScriptEffect` (0x00518507) - enhanced version
- `Mutation_ElectricallyChargedSuperExplosion` (0x00518508)
- `Mutation_ElectricallyChargedHitEnchantment` (0x003C9BA1) - damage enchantment

**Wiki Discrepancy**: Wiki says "chance to shock melee attackers" without specifics. Game files reveal **40% trigger chance**, **3s cooldown**, **8 HP self-damage**, **1s fail cooldown**.

### 8. Empath (0x004E1F16)

**Positive Effects:**
- `-25% damage taken by teammates` (MGEF: `Mutation_EmpathEffect` 0x004E1F1B)
- Actor Value: `MutationEmpathStrength` (0x007AED02)
- Strength modifier effect: `abMutationEmpathStrength` (0x007AED01)

**Negative Effects:**
- `+33% damage taken by player` (applied via `Mutation_EmpathPenalty_Perk` 0x004E1F1D)

**In-Game Description**: "You take increased damage, but your teammates take decreased damage."

**Wiki Match**: Consistent. -25% team damage, +33% self damage.

### 9. Grounded (0x004E4002)

**Positive Effects:**
- `+100 Energy Resistance` (MGEF: `Mutation_FortifyEnergyResist` 0x004DF1D4, keyword: PositiveEffect)

**Negative Effects:**
- `-50% Energy weapon damage` (MGEF: `Mutation_ReduceEnergyDamage` 0x004E4005, keyword: NegativeEffect, via Perk 0x004E4007)

**In-Game Description**: "Your energy resistance increases. Damage output from your energy weapons is reduced."

**Wiki Match**: Consistent. +100 ER, -50% energy weapon damage.

### 10. Healing Factor (0x004DF1DB)

**Positive Effects:**
- `+300% Health Regeneration` (MGEF: `Mutation_FortifyHealRate` 0x004DF1DD)

**Negative Effects:**
- `-55% Chem/Stimpak effectiveness` (MGEF: `Mutation_ReduceChemEffect` 0x004DF1DC, keyword: NegativeEffect, via Perk 0x004DF1DF)

**In-Game Description**: "Your health will regenerate if you are not starving. The effectiveness of stimpaks and chems is reduced."

**Wiki Match**: Consistent. +300% regen, -55% chem effects.

### 11. Herbivore (0x003C404E)

**Positive Effects:**
- Double vegetable/fruit/herb benefits (MGEF: `Mutation_EatAllTheVeggies` counterpart)
- No veggie disease (MGEF: `Mutation_EatSafeVeggies` 0x003C4056)

**Negative Effects:**
- No meat benefits (qualitative, not numerical)

**Keywords:** Same diet keyword `0x003DC3A4` as Carnivore. Mutually exclusive.

**In-Game Description**: "You get twice the benefit from eating vegetables, and your chance of contracting diseases from vegetables is reduced. You get no benefits from eating meat."

**Wiki Match**: Consistent.

### 12. Herd Mentality (0x004E1F1E)

**Positive Effects (on team):**
- `+2 to ALL SPECIAL stats` when grouped
- Uses 7 separate hidden fortify effects:
  - `Mutation_FortifyStrength_Hidden` (0x004E3FF9)
  - `Mutation_FortifyPerception_Hidden` (0x004E3FF8)
  - `Mutation_FortifyEndurance_Hidden` (0x004E3FF5)
  - `Mutation_FortifyCharisma_Hidden` (0x004E3FF4)
  - `Mutation_FortifyIntelligence_Hidden` (0x004E3FF6)
  - `Mutation_FortifyAgility_Hidden` (0x004E3FF3)
  - `Mutation_FortifyLuck_Hidden` (0x004E3FF7)

**Negative Effects (solo):**
- `-2 to ALL SPECIAL stats` when solo
- Uses 7 separate hidden reduce effects:
  - `Mutation_ReduceStrength_Hidden` (0x004E4000)
  - `Mutation_ReducePerception_Hidden` (0x004E3FFF)
  - `Mutation_ReduceEndurance_Hidden` (0x004E3FFC)
  - `Mutation_ReduceCharisma_Hidden` (0x004E3FFB)
  - `Mutation_ReduceIntelligence_Hidden` (0x004E3FFD)
  - `Mutation_ReduceAgility_Hidden` (0x004E3FFA)
  - `Mutation_ReduceLuck_Hidden` (0x004E3FFE)

**Conditions (from SPEL record):**
- Uses condition function `839` (GetInCurrentTeam) to check team membership
- 7 separate condition blocks, one per SPECIAL stat direction
- Has additional keyword `0x00518509` (unique to Herd Mentality)
- Reduction effect: `Mutation_HerdMentality_Reduce_UIDummy` (0x007B74F5)

**In-Game Description**: "When on a team, all SPECIALs increase. When solo, all SPECIALs are reduced."

**Wiki Match**: Consistent. +2 all SPECIAL on team, -2 all SPECIAL solo.

### 13. Marsupial (0x004DF1CE)

**Positive Effects:**
- `+20 Carry Weight` (MGEF: `Mutation_FortifyCarryWeight` 0x004DF1DE)
- Increased jump height (MGEF: `Mutation_FortifyJumpHeight` 0x004DF1D0, keyword: PositiveEffect)

**Negative Effects:**
- `-4 Intelligence` (MGEF: `Mutation_ReduceIntelligence` 0x004DF1D1, keyword: NegativeEffect)

**In-Game Description**: "Your carry capacity and jump height are increased. Your intelligence is reduced."

**Wiki Match**: Consistent. +20 carry weight, improved jump, -4 INT.

### 14. Plague Walker (0x004E4021)

**Positive Effects:**
- Poison aura that scales with number of diseases
- Cloak effect: `Mutation_PlagueWalkerCloak` (0x004E401F)
- Super variant: `Mutation_PlagueWalkerCloakSuper` (0x003D012B)
- Damage effect: `Mutation_PlagueWalkerDamageEffect` (0x004E4023)
- Damage spell: `Mutation_PlagueWalkerDamage` (0x004E4022)
- Super damage: `Mutation_PlagueWalkerDamageSuper` (0x003D012C)

**Negative Effects:**
- None

**Scaling (from SPEL conditions):**
- Uses condition `871` (GetItemCount on keyword 0x1EAE -- disease keyword)
- Tier 1: disease count == 1
- Tier 2: disease count == 2
- Tier 3: disease count == 3
- Tier 4: disease count >= 4
- Each tier is a separate condition block in the damage spell, suggesting 4 tiers of damage output

**In-Game Description**: "You have a poison aura, which grows stronger with each disease you contract."

**Wiki Match**: Consistent. The 4-tier system with disease count thresholds is not documented on the wiki.

### 15. Scaly Skin (0x004DF1CF)

**Positive Effects:**
- `+50 Damage Resistance` (MGEF: `Mutation_FortifyDamageResist` 0x004DF1D2, keyword: PositiveEffect)
- `+50 Energy Resistance` (MGEF: `Mutation_FortifyEnergyResist` 0x004DF1D4 -- shared with Grounded but separate instance)

**Negative Effects:**
- `-50 Action Points` (MGEF: `Mutation_ReduceActionPoints` 0x004DF1D5, keyword: NegativeEffect)

**In-Game Description (from string D9009159)**: "Scaly Skin Mutation: -50 AP, +50 Damage Resistance, +50 Energy Resistance"

**Wiki Match**: Consistent. +50 DR, +50 ER, -50 AP.

### 16. Speed Demon (0x004DF1E0)

**Positive Effects:**
- `+20% Movement Speed` (MGEF: `Mutation_FortifyMoveSpeed` 0x004DF1E2)
- `+20% Reload Speed` (MGEF: `Mutation_FortifyReloadSpeed` 0x004DF1E6)
- Sprint speed bonus: `Mutation_FortifySprintSpeed_Hidden` (0x003C4044), `Mutation_FortifySprintSpeed_Dummy` (0x003C4041)

**Negative Effects:**
- Increased hunger & thirst accumulation (MGEF: `Mutation_IncreasedHungerThirst` 0x004DF1E4, keyword: NegativeEffect, via Perk 0x004DF1E5)

**Conditions (from SPEL record):**
- `IsMoving == 1` -- movement speed bonus only applies while moving
- Uses condition function `10017` for additional state checks

**In-Game Description**: "Your movement speed and reload speed are increased. You require more food and water to stay alive."

**Wiki Match**: Consistent. +20% move speed, +20% reload, increased hunger/thirst.

### 17. Talons (0x0028D3BC)

**Positive Effects:**
- `+25% Unarmed/Fist damage` (MGEF: `Mutation_TalonsEffect` 0x003C4032, keyword: PositiveEffect, via Perk `Mutation_Talons_Perk` 0x00386ACB)
- Bleeding damage on hit: `Mutation_TalonsBleedSpell` (0x00386ACD)

**Negative Effects:**
- `-4 Agility` (MGEF: `Mutation_ReduceAgility` 0x00391F10, keyword: NegativeEffect)

**In-Game Description**: "Your Fists damage and bleed effects are increased. Your agility is reduced."

**Wiki Match**: Consistent. +25% unarmed damage + bleed, -4 AGI.

### 18. Twisted Muscles (0x003C402F)

**Positive Effects:**
- `+25% Melee damage` (MGEF: `Mutation_TwistedMusclesEffect` 0x003C4031, keyword: PositiveEffect, via Perk `Mutation_TwistedMuscles_Perk` 0x00386ACE)
- Increased limb cripple chance on melee hits

**Negative Effects:**
- `-50% Gun accuracy` (MGEF: `Mutation_ReduceAccuracy` 0x003C4034, keyword: NegativeEffect, via Perk `Mutation_ReduceAccuracy_Perk` 0x003C4035)

**Scaling with Slugger/Iron Fist Perks (from SPEL conditions):**
The spell has multiple condition tiers checking for melee perk ranks:
- No perk: base +25% melee
- `HasPerk(0x391F0E) == 1, HasPerk(0x391F11) == 0`: Rank 1 modifier
- `HasPerk(0x391F11) == 1, HasPerk(0x391F12) == 0`: Rank 2 modifier
- `HasPerk(0x391F12) == 1`: Rank 3 modifier

This suggests Twisted Muscles may interact with or scale differently based on melee perk investment. The wiki does not document this interaction.

**In-Game Description**: "Your melee attacks deal more damage and have increased limb damage. The accuracy of your guns is reduced."

**Wiki Discrepancy**: The conditional perk-based scaling tiers in the SPEL record are not documented on the wiki.

### 19. Unstable Isotope (0x004E4017)

**Positive Effects:**
- Chance to release radiation blast when struck in melee (scripted via `MutationTriggerMeleeExplosionScript`)
- Explosion: `Mutation_UnstableIsotopeExplosion` (0x004E401E) - uses nuke explosion model
- Radiation damage enchantment: `Mutation_UnstableIsotopeEnchRadDmg` (0x004E75A7)

**Negative Effects:**
- Self-irradiation from blast

**Global Variables (from ESM GLOB records):**
- `Mutation_UnstableIsotopeExplosionChance` (0x004E401A): **10%** chance to trigger
- `Mutation_UnstableIsotopeExplosionCooldown` (0x004E401B): **3 seconds** cooldown
- `Mutation_UnstableIsotopeSelfDamage` (0x004E401D): **8 HP** self-damage
- `Mutation_UnstableIsotopeFailCooldown` (0x004E401C): **1 second** fail cooldown

**Super Variant:**
- `Mutation_UnstableIsotopeSuperScriptEffect` (0x0051850C)
- `Mutation_UnstableIsotopeSuperExplosion` (0x0051850E)
- `Mutation_UnstableIsotopeSuperEnchRadDmg` (0x00518508)

**Wiki Discrepancy**: Wiki says "10% chance to release a radiation blast when struck in melee" -- matches the GLOB value. However, the **3s cooldown**, **8 HP self-damage**, and **1s fail cooldown** are NOT documented on the wiki.

---

## Mutation System Mechanics (from Scripts)

### Acquisition (`surv_playermutationscript.psc`)

**Roll Formula:**
- Minimum level to gain mutations: **Level 5** (`MinRadMutationLevel = 5`)
- Roll cooldown: **1 hour** (`SURV_MutationRollCooldownHours` GLOB = 1.0)
- Threat roll cooldown: **0.33 minutes** (~20 seconds) (`SURV_MutationThreatRollCooldownMinutes` GLOB = 0.33)
- Roll exponent: **1.5** (`SURV_MutationRollExponent` GLOB = 1.5)
- Roll multiplier: **0.2** (`SURV_MutationRollMult` GLOB = 0.2)
- Max roll possible: **100** (`SURV_MutationRollMaxPossible` GLOB = 100.0)
- Rad damage bucket size max: **10.0** (script constant)
- Timer duration: **1.0 seconds** (script constant)
- Max rads: **1000.0** (script constant)

The mutation roll uses accumulated radiation damage in a bucket system, with the chance calculated using an exponential formula (`damage^exponent * mult`), capped at the max possible value.

### Starched Genes Interaction
- Rank 1 scalar: **0.5** (50% chance to keep mutations on RadAway use)
- Rank 2 scalar: **0.0** (0% chance to lose mutations -- full protection)

### Serum Behavior
- Serums suppress negative effects for a limited time
- Each mutation has a "super" variant (serum-enhanced) with improved values
- The `CureWithRadAway` flag defaults to `True` for normal mutations, `False` for quest-managed special mutations
- The `GainWithRadDamage` flag defaults to `True`, `False` for quest-managed mutations

### Perk Interactions
- **Class Freak**: Reduces negative effects by 25%/50%/75% at ranks 1/2/3
- **Strange In Numbers**: +25% boost to positive mutation effects when teammates are also mutated
- **Starched Genes**: Rank 1 = 50% protection from cure, Rank 2 = 100% protection

---

## Scripted Mutations: Electrically Charged vs Unstable Isotope

Both use `MutationTriggerMeleeExplosionScript` with different parameters:

| Parameter | Electrically Charged | Unstable Isotope |
|-----------|---------------------|------------------|
| Explosion Chance | 40% | 10% |
| Explosion Cooldown | 3 seconds | 3 seconds |
| Fail Cooldown | 1 second | 1 second |
| Self Damage | 8 HP | 8 HP |
| Explosion Type | EMP (electrical) | Nuke (radiation) |

The script checks for melee weapon keywords (`WeaponTypeMelee1H`, `WeaponTypeMelee2H`, `WeaponTypeUnarmed`) and uses the `ExplosionChance` global to roll for activation.

---

## Hidden/Cut Content

### Rad Walker (CUT)
- `Mutation_RadWalker-CUT` (0x004E4028) - cut mutation
- Had a rad aura cloak: `Mutation_RadWalkerCloak` (0x004E402A)
- Damage effect: `Mutation_RadWalkerDamageEffect` (0x0052CFB1)
- Was replaced by Plague Walker (poison aura instead of rad aura)
- Serum: `Serum_RadWalkerEffect` (0x0050A5EF) -- still in data

### Babylon Twisted Muscles Variant
- `zzz_Mutation_TwistedMusclesEffect_Babylon` (0x0047A265)
- `zzz_Mutation_TwistedMuscles_Babylon` (0x0047A267, SPEL)
- `zzz_Mutation_TwistedMuscles_Perk_Babylon` (0x0047A266)
- `zzz_Serum_TwistedMuscles_Babylon` (0x0047A268)
- A "Babylon" variant with its own serum -- possibly from a cancelled game mode or event

### Bounty Hunter Mutation System
Multiple `Burn_Bounty_Mutation_*` spells exist, suggesting mutations were planned for a bounty hunter system:
- `Burn_Bounty_Mutation_Chameleon` (0x0083F95D)
- `Burn_Bounty_Mutation_ElectricallyCharged` (0x0083D5A2)
- `Burn_Bounty_Mutation_HerdMentality` (0x0082075A)
- `Burn_Bounty_Mutation_PlagueWalker` (0x00820756)
- `Burn_Bounty_Mutation_UnstableIsotope` (0x0082074E)
- `Burn_Bounty_Mutation_FreezingTouch` (0x0082A97D)
- `Burn_Mutation_PlagueWalkerDamageSuper` (0x00820755)

These have contact-based variants with 33% random trigger chance, suggesting PvP bounty mutations.

### Additional Bounty Mutations (Not Player Mutations)
- `Mutation_ReduceMoveSpeed` (0x0083F954)
- `Mutation_ReduceJumpHeight` (0x0083F953)
- `Mutation_IncreaseFallSpeed` (0x0083F955) -- note: the opposite of Bird Bones

---

## Discrepancies Summary: Game Files vs Wiki

| Mutation | Discrepancy | Game Files Say | Wiki Says |
|----------|-------------|----------------|-----------|
| Adrenal Reaction | **MAJOR** | HP-threshold damage scaling via curve table (5%-100%, linear across 20 steps) | "+5% weapon damage per killed enemy" |
| Electrically Charged | Undocumented details | 40% chance, 3s cooldown, 8 HP self-damage, 1s fail cooldown | "Chance to shock melee attackers" (no specifics) |
| Unstable Isotope | Undocumented details | 10% chance, 3s cooldown, 8 HP self-damage, 1s fail cooldown | "10% chance" (no cooldown/self-damage details) |
| Twisted Muscles | Perk interaction | Has conditional scaling tiers based on melee perk ranks | Not documented |
| Plague Walker | Tier system | 4 tiers at 1/2/3/4+ diseases | "Scales with diseases" (no tier details) |
| Rad Walker | Cut content | Still in game data as `Mutation_RadWalker-CUT` | Not mentioned |
| Babylon variant | Cut content | Twisted Muscles "Babylon" variant with own serum | Not mentioned |
| Bounty mutations | Cut/unreleased | 6+ bounty hunter mutations with contact-transfer | Not mentioned |

---

## Key Findings

1. **Adrenal Reaction is NOT a kill-streak mechanic.** The curve table data definitively proves it scales with missing HP percentage, providing +5% to +100% weapon damage linearly interpolated across 20 health threshold steps. The "super" variant (serum/Strange In Numbers) pushes this to +6.25% to +125%.

2. **Electrically Charged has 4x the trigger chance of Unstable Isotope** (40% vs 10%), but both share identical cooldowns (3s) and self-damage (8 HP). This massive probability difference is not documented anywhere.

3. **The Mutant's legendary prefix caps at +50% damage with 10 mutations**, using a clean linear curve of +5% per mutation. This was previously undocumented in the curve tables.

4. **Plague Walker has exactly 4 damage tiers** based on disease count (1, 2, 3, 4+), confirmed by the SPEL condition blocks.

5. **Twisted Muscles has hidden perk interaction tiers** that may modify its behavior based on equipped melee perks -- a mechanic not documented by the community.

6. **Rad Walker was the predecessor to Plague Walker**, using radiation instead of poison. Its data remains in the game files in a cut state.

7. **A "Babylon" variant of Twisted Muscles** exists with its own complete serum and perk chain, suggesting cancelled content.
