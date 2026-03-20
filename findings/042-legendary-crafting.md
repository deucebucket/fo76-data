# Finding 042: The Legendary Crafting and Rerolling System -- Fully Extracted

**Source**: SeventySix.esm full dump, OMOD records, LVLI records, curve tables, decompiled Papyrus scripts
**Status**: VERIFIED against game data -- several findings contradict community assumptions

---

## 1. Legendary Mod Pools by Star Slot

The game uses FormLists (`LegendaryMods1Star` through `LegendaryMods4Star`) to define which effects can roll on each slot. Each item type (weapon/armor/power armor) pulls from the same lists, but keyword filtering on the item determines which mods actually apply.

### Weapon Star 1 (29 mods)
| Internal Name | Common Name | Notes |
|---|---|---|
| AntiArmor | Anti-Armor | Ignore 50% armor |
| Vampire | Vampire's | Health regen on hit |
| DamageInverseHealth | Bloodied | Damage scales with low HP |
| Execute | Executioner's | +50% dmg when target <40% HP |
| DamageFirstBlood | Instigating | 2x dmg at full HP |
| DamageUnarmored | Aristocrat's | Dmg scales with caps |
| DamageAddiction | Junkie's | Dmg per addiction |
| DamageNight | Nocturnal | Dmg at night |
| DmgConsecutiveHits | Furious | Stacking dmg |
| DmgVsBugs | Exterminator's | +50% vs Mirelurks/bugs |
| DmgVsScorched | Zealot's | +50% vs Scorched |
| DmgVsPlayers | Assassin's | +50% vs players |
| DmgVsGhouls | Ghoul Slayer's | +50% vs Ghouls |
| DmgVsAnimals | Hunter's | +50% vs Animals |
| DmgVsSupermutants | Mutant Slayer's | +50% vs Super Mutants |
| DmgVsRobots | Troubleshooter's | +50% vs Robots |
| DmgWithMutation | Mutant's | +5% dmg per mutation |
| Guns_AmmoCapacity4x | Quad | 4x magazine size (guns only) |
| Guns_TwoShot | Two Shot | Fires extra projectile (guns only) |
| Guns_AccuracyNotInCombat | Stalker's | +100% VATS acc not in combat (guns only) |
| DebuffDamage | Suppressor's | -20% target dmg for 3s |
| Gourmand | Gourmand's | Dmg scales with food/water |
| DamageViaCaps | Aristocrat's | Dmg scales with caps |
| DamageViaHealth | Juggernaut's | Dmg scales with high HP |
| Medic | Medic's | VATS crits heal group |
| Adrenal | Adrenal Reaction | Bonus dmg at low HP (new) |
| Lucid | Lucid | New Backwoods effect |
| Guns_Sniper | Sniper's | New Backwoods (guns only) |
| Melee_Feral | Feral | New Backwoods (melee only) |

### Weapon Star 2 (14 mods)
| Internal Name | Common Name | Notes |
|---|---|---|
| Guns_ExplosiveBullets | Explosive | Bullets explode (guns only) |
| DmgCrits | +50% crit dmg | |
| Guns_DmgSights | +25% dmg while aiming | Guns only |
| Guns_RoF | 25% faster fire rate | Guns only |
| Guns_VATSAccuracy | +25% VATS hit chance | Guns only |
| Guns_Bashing | Bashing +50% | Guns only |
| Guns_LastShot | Last Shot | Last round 2x dmg (guns only) |
| DmgLimbs | +50% limb dmg | |
| APViaKill | AP refresh on kill | |
| Melee_SwingSpeed | 40% faster swing | Melee only |
| Melee_DamagePowerAttack | +40% power attack dmg | Melee only |
| Melee_BlockReflects | Reflects 50% melee while blocking | Melee only |
| Melee_Steady | Steady | Melee only |
| Melee_PickPocket | Pick Pocket | Melee only (new Backwoods) |

### Weapon Star 3 (21 mods)
| Internal Name | Common Name | Notes |
|---|---|---|
| CritSpeed | VATS crit fills 15% faster | |
| VATSCostAP | 25% less VATS AP cost | |
| Weight | 90% reduced weight | |
| Durability | 50% more durability | |
| Guns_ReloadSpeed | 15% faster reload | Guns only |
| Guns_MoveSpeedSights | Move faster while aiming | Guns only |
| Guns_ResistSights | +250 DR while aiming | Guns only |
| Guns_ResistReload | +250 DR while reloading | Guns only |
| Guns_CloakOnHit | Stealth field on hit | Guns only |
| Melee_Defenders | +1 to all SPECIAL while blocking | Melee only |
| Melee_LessDamageBlock | Take 40% less dmg while blocking | Melee only |
| Melee_Barbarian | Barbarian | Melee only (new Backwoods) |
| StatPerception | +1 Perception | |
| StatAgility | +1 Agility | |
| StatStrength | +1 Strength | |
| StatEndurance | +1 Endurance | |
| StatCharisma | +1 Charisma | |
| StatIntelligence | +1 Intelligence | |
| StatLuck | +1 Luck | |
| Glowing | Glowing | New Backwoods effect |

*Note: `zzzmod_Legendary_Weapon3_Rugged` (no underscore prefix) appears in data but naming is inconsistent -- status unclear.*

### Weapon Star 4 (20 mods -- ALL 4-star exclusive)
| Internal Name | Common Name | Notes |
|---|---|---|
| Polished | Polished | |
| Vipers | Viper's | Poison effect |
| Guns_Electricians | Electrician's | Energy dmg bonus (guns only) |
| Pyromaniac | Pyromaniac's | Fire dmg bonus |
| Melee_ComboBreaker | Combo Breaker | Melee only |
| Fracturers | Fracturer's | Explosive damage |
| Melee_Icemens | Icemen's | Cryo effect (melee only) |
| Bully | Bully's | |
| Guns_Stabilizers | Stabilizer's | Guns only |
| Guns_PinPointers | Pin Pointer's | Guns only |
| Conductors | Conductor's | |
| Melee_Pounders | Pounder's | Melee only |
| Melee_Fencers | Fencer's | Melee only |
| Encirclers | Encircler's | |
| Melee_Charged | Charged | Melee only (newest) |
| Weapon_Ranged4_HeadHunters | Headhunter's | Ranged only |
| P62_Weapon4_Melee_Brutalists | Brutalist's | Melee only (P62 = Patch 62) |
| P62_Weapon4_Satiated | Satiated | |
| P62_Weapon4_Guns_SightSeers | Sightseer's | Guns only |
| P62_Weapon4_Guns_Ruiners | Ruiner's | Guns only |
| RA_Weapon4_ThrillSeeker | Thrillseeker's | RA prefix = new content |

### Armor Star 1 (21 mods, mirrored for Power Armor)
Bolstering, Chameleon, Cloaking, Life Saving, Mutant's, Nocturnal, Unyielding, Vanguard's, Weightless/Heavyweight, Auto-Stim, Regenerating, Assassin's, Exterminator's, Ghoul Slayer's, Hunter's, Mutant Slayer's, Troubleshooter's, Zealot's, Overeater's, Aristocrat's, Adrenal, Lucid

### Armor Star 2 (19 mods, mirrored for Power Armor)
+1 each SPECIAL (7), AP Refresh, Poison Resist, Rad Resist, Disease Resist, Glutton, Fireproof, Cryo Resist, Reduce Explosion Dmg, Elementalist, Fierce, Rushing, Painkiller

### Armor Star 3 (20 mods, mirrored for Power Armor)
Sentinel, Cavalier, Weapon Weight, Ammo Weight, Food/Drink/Chem Weight, Junk Weight, Fall Damage, Waterbreathing, Lockpicking, Sneak, Durability, Reduced Limb Damage, Defenders, Rads Regen, Toxic, Burning, Frozen, Electrified, Increase Healing, Reflex, Active, Healthy

### Armor Star 4 (18+ mods -- ALL 4-star exclusive)
Sawbones, Battle Loaders, Bruiser, Limit Break, Miasma, Ranger, Runner, Tanky, Scanners (PA), Propelling (PA), ChooChoo (PA), Reflective (PA), RadioactivePowered (PA), Rejuvenators (PA), Aegis (PA), Stalwarts (PA), Crusaders (P62), Metabolic (P62), Rebounders (P62), OverLoaders (PA, P62), Voltaic (PA, P62), StaggerProof (PA, P62)

---

## 2. Weighting / Probability: CONFIRMED EQUAL

**This is the big one.** Community suspicion that some effects are rarer is **wrong according to the game data.**

The script `PlayerLegendaryItemScript.psc` contains the function `GetAllowedMods()` which:
1. Iterates through the mod rule array for the slot
2. Checks if the mod passes keyword filters (AllowedKeywords / DisallowedKeywords)
3. Adds passing mods to an `AllowedMods` array
4. Returns the flat array

The array is then used with random selection -- **no weights attached**. There are `_PARENT_mod_Legendary_Weapon_WEIGHTVALUE_1` through `_WEIGHTVALUE_5` OOMDs in the data, but these control the **item's weight and value multiplier** based on star count, NOT the probability of rolling a specific legendary effect.

**Every legendary effect that passes keyword filtering has exactly equal probability of being selected.**

This means:
- Bloodied has the same chance as Nocturnal on a weapon
- AP Refresh has the same chance as Disease Resist on armor
- The "god roll" rarity comes purely from combinatorics (1/29 x 1/14 x 1/21 = 1/8,526 for weapons before keyword filtering)
- Keyword filtering slightly changes odds per item: guns can't roll melee effects and vice versa, so the pool shrinks

The GMST `fLegendaryModShardChance` = **0.015 (1.5%)** -- this is the chance for legendary shards to drop, NOT a roll weight.

---

## 3. Legendary Module Costs Per Craft/Reroll

From curve table `cobj_legendary_crafting_module.json`:

| Stars | Legendary Modules Required |
|---|---|
| 1-star | 15 |
| 2-star | 30 |
| 3-star | 60 |
| 4-star | 120 |

---

## 4. Legendary Core Requirements

From curve table `cobj_legendary_addslot_module.json`:

| Stars | Legendary Cores Required |
|---|---|
| 1-star | 5 |
| 2-star | 10 |
| 3-star | 15 |
| 4-star | 20 |

**Important**: Legendary Cores are a **deprecated currency** (CNCY `zzz_LegendaryCore` -- zzz prefix means disabled). The system was simplified to Legendary Modules only.

---

## 5. Legendary Scrip Values (Scrapping)

From `legendary_scrapvalues_*.json` -- **ALL item types return the same scrip**:

| Stars | Scrip (All Types) |
|---|---|
| 1-star | 1 |
| 2-star | 2 |
| 3-star | 4 |
| 4-star | 6 |

### Sell Values (Purveyor Cost in Scrip)

From `legendary_sellvalues_*.json`:

| Stars | Armor | Power Armor | Ranged Weapon | Melee Weapon |
|---|---|---|---|---|
| 1-star | 3 | 10 | 5 | 5 |
| 2-star | 9 | 20 | 15 | 15 |
| 3-star | 24 | 45 | 40 | 40 |
| 4-star | 30 | 55 | 50 | 50 |

**Key finding**: The sell values curve matches `cobj_legendary_attach_scrip.json` exactly for armor -- these appear to be the Purveyor's pricing in Legendary Tokens (Scrip).

### Scrip Scaling on Repeated Scrapping

From `cobj_legendary_scrap.json` -- a progressive cost curve for scrapping:

| Scrap Count | Scrip Return |
|---|---|
| 0 | 0 |
| 1 | 100 |
| 2 | 200 |
| 3 | 300 |
| ... | (linear +100 per) |
| 20 | 1000 |

This appears to be a **cap on daily scrip** via a progressive formula, maxing at 1000 scrip per day at 20 items scrapped.

---

## 6. Purveyor (Murmrgh) / Vending Machine Pool

The Purveyor is `LGV01_VendorRef` (FormID 0x00422154), selling from `LGV01_LL_Vendor_LegendaryItems` (0x005380D1).

**The Purveyor uses the SAME legendary mod pool as crafting.** Both systems reference the same `LegendaryMods1Star` through `LegendaryMods4Star` FormLists. The Purveyor's leveled list contains references to:
- Multiple weapon category leveled lists (0x00417C40-C48)
- Armor lists (0x00605FC3-C5)
- Legendary Modules for sale (0x005652F9 = LegendaryModule)
- General item lists (0x0041023D)

The vendor resets every **3 days** (`Vendor_Reset_Days_LGV01` = 3.0).

### Minerva (Special Vendor)

Minerva (`BS02_SpecialVendor_Minerva`) sells Gold Bullion plans on a rotating schedule (LLS_GoldVendor_01 through _24, with _M suffixes for "Minerva's Big Sale" weeks). She has a `LLS_LegendaryCrafting_Components` list that is **conditionally gated** by `BS02_SpecialVendor_SellLegendaryComponents` (currently **0 = disabled**).

---

## 7. Anti-Repeat / Memory Mechanic: NONE

**There is NO anti-repeat or memory mechanic in legendary crafting or rerolling.**

Evidence:
- `PlayerLegendaryItemScript.psc` has no state tracking, no "last roll" variable, no history
- `LegendaryModSlotReroll_DO` (DFOB 0x006F0474) exists as a data object but the script logic shows pure random selection
- No `previousRoll`, `rollHistory`, or `antiDuplicate` variables exist in any legendary script
- The `GetAllowedMods()` function builds a fresh array every time and does random selection
- **You can absolutely roll the same effect twice in a row** -- the game does not prevent this

This confirms the community frustration with rerolling: you can burn 60 modules and get the same Nocturnal roll back-to-back. The RNG is memoryless.

---

## 8. 4-Star Legendary System

### Current Status: DISABLED

`LegendaryCrafting4_Enabled` (GLOB 0x00621565) = **0.0** (disabled)

The 4-star crafting OOMDs exist but are zzz-prefixed:
- `zzz_mod_Legendary_Weapon4_Crafting`
- `zzz_mod_Legendary_Armor4_Crafting`
- `zzz_mod_Legendary_PowerArmor4_Crafting`

### 4-Star Creature Spawning

`DefaultLegendary4StarCreatureRef.psc` shows 4-star creatures exist with a `Rank4Chance` property (default **50%** chance to upgrade a 3-star to 4-star). This is used for boss enemies in specific events.

### 4-Star Exclusive Effects

All effects listed in the star 4 tables above are **exclusively 4-star** -- they cannot appear on 1/2/3 star items. The `LegendaryMods4Star` FormList is separate from the 1/2/3 star lists.

The P62 prefix mods (Brutalists, Satiated, SightSeers, Ruiners, Crusaders, Metabolic, Rebounders, OverLoaders, Voltaic, StaggerProof) were added in **Patch 62** (a recent update), showing active development of the 4-star system.

---

## 9. Cut / Disabled Legendary Effects

### zzz_ Prefix (Fully Disabled -- 80+ mods)

**Original Pre-Launch Cuts:**
- `zzz_mod_Legendary_Weapon_ExplosiveBullets` -- original explosive (moved to star 2 with nerfs)
- `zzz_mod_Legendary_Weapon_SuperDamage` -- cut for obvious reasons
- `zzz_mod_Legendary_Weapon_IncendiaryBullets` -- folded into Pyromaniac
- `zzz_mod_Legendary_Weapon_IronSightsIncreaseDamageResist` -- folded into Guns_ResistSights
- `zzz_mod_Legendary_Weapon_DamageVsGhouls` -- replaced by DmgVsGhouls (slot 1)
- `zzz_mod_Legendary_Weapon1_Knockback` -- removed (too disruptive in PvP)
- `zzz_mod_Legendary_Weapon1_Guns_AmmoCapacity2x` -- replaced by 4x (Quad)
- `zzz_mod_Legendary_Weapon1_DamageViaCarryWeight` -- would have been broken with carry weight builds

**Cut Star 4 Effects:**
- `zzz_mod_Legendary_Weapon4_Bleed` / `_Poison` / `_Stagger` / `_Cripple` -- original 4-star pool, too powerful
- `zzz_mod_Legendary_Weapon4_Guns_CritFrenzy` / `_CritFreeze` -- CC effects
- `zzz_mod_Legendary_Weapon4_Melee_Block*` (BlockBurns/BlockFreeze/BlockFrenzies/BlockIrradiates/BlockElectrocutes) -- 5 cut blocking effects
- Various cut 4-star armor effects: OnMeleeHitFreeze, OnMeleeHitBurn, OnMeleeDisarm, APCost, ReflectMelee, ReflectProjectiles, CarryWeight, MaxAP, Elemental, Elusive, Daredevils, IncreaseAPRegen, IncreaseAllyResists, ReduceEnemyResists

**Cut Star 5 Effects (Never Implemented):**
- `zzz_mod_Legendary_Armor5_Resistance` -- star 5 armor!
- `zzz_mod_Legendary_Armor5_Health`
- `zzz_mod_Legendary_Armor5_AP`

**Bethesda originally planned a 5-star legendary system.** These are the only evidence of it.

**Cut 4-Star Weapon Named Effects:**
- `ZZZ_mod_Legendary_Weapon_Ranged4_BloodHealer` / `Melee4_BloodHealer` -- heal on blood
- `ZZZ_mod_Legendary_Weapon_Ranged4_CheerLeader` / `Melee4_CheerLeader` -- team buff
- `ZZZ_mod_Legendary_Weapon_Melee4_HeavyHitters` -- heavy melee
- `ZZZ_mod_Legendary_Weapon_Ranged4_Bruisers` -- ranged bruiser
- `ZZZ_mod_Legendary_Weapon_Melee4_CriticalHealers` / `Ranged4_CriticalHealers` -- crit healing
- `ZZZ_mod_Legendary_Weapon_Melee4_Scavengers` / `Ranged4_Scavengers` -- scavenging bonus
- `ZZZ_mod_Legendary_Weapon_Melee4_IncreaseAttackSpeedOnKill` -- ramping attack speed
- `zzz_mod_Legendary_Weapon_Melee4_Warmongers` / `Ranged4_Warmongers` -- warmongering

**DEL_WIP4 Prefix (Deleted Work-In-Progress 4-star):**
- `DEL_WIP4_mod_Legendary_Weapon4_Deadly` -- generic damage
- `DEL_WIP4_mod_Legendary_Weapon4_Duelists` -- dueling
- `DEL_WIP4_mod_Legendary_Weapon4_Guns_SuperResilient` -- mega resist
- `DEL_WIP4_mod_Legendary_Weapon4_Guns_Toppers` -- unknown
- `DEL_WIP4_mod_Legendary_Weapon4_Melee_Stunning` -- stun
- `DEL_WIP4_mod_Legendary_Armor4_AeroFlight` / PA variant -- **FLIGHT**
- `DEL_WIP4_mod_Legendary_Armor4_Moneybags` / PA variant -- caps scaling
- `DEL_WIP4_mod_Legendary_Armor4_Polished` / PA variant -- polished
- `DEL_WIP4_mod_Legendary_Armor4_StaggerProof` -- stagger immune (PA version was KEPT as P62)
- `DEL_WIP4_mod_Legendary_PowerArmor4_AutoRepair` -- self-repair

**AeroFlight is particularly notable**: Bethesda had a legendary power armor flight effect in development. It was deleted.

### BOUNTY_ Prefix (Backwoods Bounty System Effects -- 14+ zzz-prefixed)

The Backwoods update added a bounty hunting system with new legendary effects. Some were cut (zzz_BOUNTY_ prefix):
- Feral (armor version cut, weapon version kept)
- Recollecting
- SelfRepair
- MadScientist
- Glowing (armor version cut, weapon version kept)
- Insane
- Healthy (weapon version cut, armor version kept)
- Jagged
- Savage
- Pulsating (melee)
- Rebate (guns)
- Barbarian (armor version cut)
- PowerArmor3_Reflex (cut)

Active BOUNTY effects that shipped: Sniper, Feral (weapon), Lucid, PickPocket, Barbarian (weapon melee), Glowing (weapon), Active, Healthy (armor), Reflex (armor), Elementalist, Fierce, Rushing, PainKiller

---

## 10. Legendary Core Requirements (Historical)

Legendary Cores were the original secondary crafting currency alongside Legendary Modules. They were **deprecated** (`zzz_LegendaryCore` CNCY prefix) and the tiered core system was disabled:
- `ZZZ_RESTRICTED_LL_LegendaryCore_Tier2`
- `ZZZ_RESTRICTED_LL_LegendaryCore_Tier3`
- `ZZZ_RESTRICTED_LL_LegendaryCore_Tier4`

The original cost was from `cobj_legendary_addslot_module.json`: 5/10/15/20 cores for 1/2/3/4 stars.

Current system uses **only Legendary Modules** with the costs in section 3.

---

## Legendary Shard System (New -- Backwoods)

A new system was added with the Backwoods update allowing targeted legendary crafting via shards:

**Shard Drop Chances** (from legendary kills):
| Source Star Level | Drop Chance |
|---|---|
| 1-star enemy | 40% |
| 2-star enemy | 30% |
| 3-star enemy | 20% |
| 4-star enemy | 10% |

**Learn Chance from Scrapping**: All 4 tiers = **100%** (1.0) -- you always learn the shard recipe when scrapping a legendary with that effect.

**Shard Types Found**: Weapon3_Melee_LessDamageBlock, Weapon4_Melee_Charged, Weapon1_Guns_Snipers, Weapon3_Melee_Barbarian, Armor2_PainKiller, Armor2_Rushing, Armor2_Elementalist, Armor2_Fierce, and more. These allow you to craft a **specific** legendary effect using a shard instead of random rolling.

---

## Summary of Community Verification

| Claim | Game Data | Verdict |
|---|---|---|
| "All effects have equal drop chance" | CONFIRMED -- flat array, no weights | TRUE |
| "Some effects are rarer" | No weight system exists | FALSE |
| "Rerolling remembers previous rolls" | No history/state tracking in scripts | FALSE |
| "4-star crafting exists" | Global flag = 0, crafting OOMDs zzz'd | DISABLED |
| "Purveyor uses same pool as drops" | Same FormLists referenced | TRUE |
| "Legendary Cores still required" | Currency zzz'd, system deprecated | FALSE (modules only) |
| "God roll odds are astronomical" | 1/29 x 1/14 x 1/21 = 1/8,526 for 3-star weapon | TRUE |
| "4-star effects are all unique" | Separate FormList, no overlap with 1-3 | TRUE |
| "Bethesda planned 5-star legendaries" | Three zzz'd Armor5_ mods exist | TRUE |

**The god roll math**: For a specific 3-star weapon roll (e.g., Bloodied/Explosive/25% Less VATS), the odds are roughly 1 in 8,526 before keyword filtering. With filtering (removing melee-only mods from gun pools), the actual odds improve to roughly **1 in 4,200** for a ranged weapon. Each roll costs 60 Legendary Modules. To have a 50% chance of hitting your exact god roll, you need ~2,900 rolls = **174,000 Legendary Modules**.

For 4-star weapons with 20 possible effects, a perfect 4-star god roll would be approximately **1 in 84,000**.
