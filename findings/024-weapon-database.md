# FO76 Finding 024: Complete Weapon Database from ESM Dump

## Source: WEAP_records.txt (1,501 records), OMOD_records.txt (32,677 records), CURV_records.txt (4,610 records)
## Status: COMPREHENSIVE — Full weapon inventory with cut content, creature weapons, and mod systems

---

## 1. Weapon Inventory Summary

| Category | Count | Description |
|----------|-------|-------------|
| Total WEAP records | 1,501 | Every weapon definition in the ESM |
| Creature weapons (cr*) | 769 | What enemies actually attack with |
| Cut/disabled (zzz_) | 281 | Removed or test weapons |
| Deleted (DEL_) | 16 | Explicitly marked for removal |
| CUT_ prefix | 3 | Another cut naming convention |
| Burn_ (NPC variants) | 4 | Creature poison/special attack variants |
| ATX_ (Atom Shop) | 21 | Cosmetic/store weapons |
| SCORE_ (Season) | 4 | Scoreboard reward weapons |
| Player-usable core | ~200 | Base weapons + named uniques |

---

## 2. Cut Weapons That Never Shipped

### High-Value Cuts (Not Just Test Items)

| Form ID | Name | Notes |
|----------|------|-------|
| 0x0085780F | **zzz_NitroRifle** | Full weapon system built (see Finding 021). Uses 10mm dummy receiver model. Has WeaponTypeNitro keyword, full mod tree, season skins pre-made |
| 0x006CCC2E | **CUT_NeedleSMG** | Automatic rifle with SMG characteristics. Keywords: WeaponTypeAutomatic + WeaponTypeRifle. Model: handmade dummy receiver. Unique among cuts — uses "CUT_" prefix instead of "zzz_" |
| 0x0072A8C2 | **zzz_HeavyIncinerator** | Heavy auto grenade launcher variant. Model: autogrenadelauncherreceiver.nif. Had WeaponTypeGrenadeLauncher + WeaponTypeAutomatic + WeaponTypeHeavyGun keywords |
| 0x0074D578 | **zzz_Broadsider_FusionCannon** | Broadsider variant using fusion ammo. Same model as Broadsider. Had full weapon type keywords including WeaponTypeBroadsider + WeaponTypeExplosive |
| 0x007551DE | **zzz_HeadHunter_Scythe** | 2H melee weapon with custom ATX model (atx/weapons/headhunter_scythe/). WeaponTypeMelee2H + WeaponTypeArchaic. Had its own unique model — this was a designed weapon, not a test |
| 0x00799A10 | **zzz_TeslaCannon_MissileLauncher** | Tesla Cannon using missile launcher model/framework. Heavy weapon hybrid |
| 0x007999F4 | **zzz_TeslaCannon_NukaLauncherTest** | Tesla Cannon using Fat Man model. Would have been a nuclear tesla weapon |
| 0x005CF0A0 | **zzz_LGN_NuclearProliferator_Weapon** | Named unique weapon (LGN prefix = Legendary Named). Nuclear-themed |
| 0x005A25FD | **zzz_HotRodBow** | Bow variant with hot rod aesthetic |
| 0x0059D52D | **zzz_Pilgrim_Musket** | A musket weapon, possibly tied to seasonal/historical content |
| 0x00313982 | **zzz_GaussRifle_Presidential** | A unique Gauss Rifle variant. Has its own curve table: CT_Weapon_GaussRifle_Presidential_BaseDMG [00505AD3] |
| 0x000E942B | **zzz_JunkJet** | The Junk Jet from FO4 — was in the files but never released for FO76 |
| 0x001128F0 | **zzz_DLC04_AcidSoaker** | Nuka-World themed acid weapon — cut from the Nuka-World on Tour content |
| 0x0001DACF | **zzz_LaserMusket** | The FO4 Laser Musket. Curve table exists: CUT_CT_Weapon_LaserMusket_BaseDMG [0014945D] |
| 0x000865E9 | **zzz_FusionCoreKnightWeapon** | A weapon that uses fusion cores, tied to Brotherhood of Steel |
| 0x0055C15B | **zzz_FlashbangGrenade** | Non-lethal grenade. Would have been first non-damage throwable |
| 0x0055C158 | **zzz_SoundmakerGrenade** | Noise/distraction grenade. Another non-lethal utility weapon |
| 0x0084D524 | **zzzHealingSpearOriginalPerk** | Original version of the Healing Spear perk weapon before redesign |

### Cut Compound Bow/Crossbow Elemental Variants
Six compound bow and six crossbow elemental variants were cut:
- zzz_CompoundBow: Cryo, Explosive, Firework, Poison, Flaming, Plasma
- zzz_crossbow: Cryo, Explosive, Firework, Poison, Flaming, Plasma

These suggest Bethesda planned elemental ammo types for bows/crossbows but pulled them.

### "Moon" (Blue Moon) Cut Content
Six weapons prefixed "zzz_Moon_" tied to the Blue Moon event/questline:
- **zzz_Moon_CultistPickaxe** [006A0092] — Custom model: bluemoon/weapons/bloodiedpickaxe.nif
- **zzz_Moon_Flamer_Weapon_BlueFlamer** [00693D37] — Blue-flame Flamer variant
- **zzz_Moon_NukaAcidGrenade** [00692A0D] — Nuka acid throwable
- **zzz_Moon_NukaHomemadeGrenade** [00692A0C] — Homemade nuka grenade
- **zzz_Moon_PumpActionShotgun_Weapon_Tornado** [0069255D] — Named shotgun "Tornado"
- **zzz_DONOTUSE_Moon_JawboneBlade** [0069229A] — Jawbone melee weapon (extra "DONOTUSE" prefix)

The Blue Moon content has custom models in a dedicated `bluemoon/` asset folder, indicating significant development before being cut.

### Test/Debug Weapons (Less Interesting)
- 7 zzz_TESTDMG_ weapons (10-400 damage test guns)
- ~70 zzz_TestAudio_ weapons (fire rate/suppressor audio testing)
- Various zzz_Debug_Legendary_ weapons for testing legendary effects
- zzz_TEST_Balance weapons for level-scaling tests

---

## 3. The Nitro Weapon System — Deep Dive

**Expands on Finding 021 with OMOD data.**

### Two WEAP Records
| Form ID | Name | Key Difference |
|---------|------|----------------|
| 0x0084460B | **Nitro** (Pistol) | Has 0x0037D0B2 keyword but NOT 0x001C9E78 |
| 0x0085780F | **zzz_NitroRifle** | Has 0x001C9E78 keyword (rifle scope), extra keyword 0x0085780C (AnimsGripNitroRifle) |

Both use 10mm dummy receiver model. This confirms convertible pistol/rifle like the 10mm and Pipe weapons.

### Complete Nitro Mod Tree (from OMOD records)
**Receivers (ammo calibers):**
- mod_Nitro_Receiver_Base [0085780E]
- mod_Nitro_Receiver_308 [008445DF] — .308 caliber
- mod_Nitro_Receiver_308HighVelocity [008445E1]
- mod_Nitro_Receiver_308Central [008445E7]
- mod_Nitro_Receiver_308AntiScorchBeast [008445DC]
- mod_Nitro_Receiver_50Cal [008445EC] — .50 caliber
- mod_Nitro_Receiver_50CalHighVelocity [008445E9]
- mod_Nitro_Receiver_50CalCentral [008445ED]
- mod_Nitro_Receiver_50CalAntiScorchBeast [008445EA]
- mod_Nitro_Receiver_556Central [008445E6] — 5.56mm
- mod_Nitro_Receiver_556HighVelocity [008445F0]
- mod_Nitro_Receiver_556AntiScorchBeast [008445F2]
- zzz_mod_Nitro_receiver_556Base [008445EB] — Cut base 5.56 receiver

**Barrels:**
- mod_Nitro_Barrel_Long [00851B73]
- mod_Nitro_Barrel_Short [00851B72]
- mod_Nitro_Barrel_VeryShort_Base [008445DD]

**Grips/Stocks:**
- mod_Nitro_Grip_Base [008445E2]
- mod_Nitro_Grip_Recoil [008445FF]
- mod_Nitro_Grip_HipAccuracy [008445FE]
- mod_Nitro_Grip_SecondaryDMG [008445F1]
- mod_Nitro_Grip_HipAccuracy-SecondaryDMG [008445F5]
- mod_Nitro_Grip_Recoil-HipAccuracy [008445D3 via full stock]
- mod_Nitro_grip_FullStock_Base/Recoil/HipAccuracy/SecondaryDMG variants

**Sights:**
- Iron Sights, Reflex, Reflex Glow, Short Scope, Short Scope NV, Medium Scope, Medium Scope NV
- Cut: Long Scope, Long Scope NV, Long Scope Recon, Short Scope Recon, Glow base

**Special Effects:**
- mod_Nitro_SpecialEffect_Explosive [008445E0]
- mod_Nitro_SpecialEffect_Penetrating [008445E3]
- mod_Nitro_SpecialEffect_ExplosivePenetrating [008445E4]
- zzz_mod_Nitro_SpecialEffect_Stagger [008445EF] — Cut
- zzz_mod_Nitro_SpecialEffect_StaggerPenetrating [008445EE] — Cut

**Magazines:**
- mod_Nitro_Magazine_Base/Default [00844604/00869A3E]
- mod_Nitro_Magazine_Swift6 [008445D5]
- mod_Nitro_Magazine_Fortunate4/6 [008445DA/00844605]
- mod_Nitro_Magazine_Hardened6 [00844602]
- zzz_mod_Nitro_magazine_Loaded8 [008445E5] — Cut 8-round magazine

**Cut Cylinder/Speedloader System (DEL_ prefix):**
- DEL_mod_Nitro_cylinder_4Shot/6Shot — Suggests original design was a revolver cylinder
- DEL_mod_Nitro_speedloader_4Shot/6Shot
- DEL_mod_Nitro_speedbullet_4Shot/6Shot
- DEL_mod_Nitro_emptybullet_4Shot/6Shot

This is significant: the Nitro was originally designed as a revolver-style weapon with a cylinder mechanism before being redesigned to use magazines.

**Paint:**
- ATX_mod_Nitro_Weapon_Paint_FreeStates [0086272A]

### Key Insight
The Nitro has THREE ammo calibers (.308, .50, 5.56) which is unique — most weapons use one or two. Combined with the Anti-Scorchbeast receiver variants for each caliber, this weapon was clearly being designed as a versatile endgame weapon. The custom model path `weapons/nitro/nitro.nif` confirms it has its own unique model, not a reskin.

---

## 4. The 44 Lawbringer — Newest Player Weapon

**Form ID: 0x008ADA17** — The highest Form ID player weapon in the ESM.

Keywords decoded:
- 0x0004A0A0 = WeaponTypePistol
- 0x00092A86 = WeaponTypeBallistic
- 0x00340878 = WeaponTypeRevolver
- 0x0033A7C8 = WeaponTypeRanged
- 0x003CFD83 = UI_WeaponTypeRevolver
- 0x000CE97E = The .44 weapon template reference
- 0x0037D0B2 = Standard weapon flag
- 0x003ECB8C, 0x00499F7A = Likely legendary/mod pool keywords

This is a named .44 Revolver variant. "Lawbringer" suggests a quest reward or seasonal unique.

---

## 5. Creature Weapon Database — Enemy Attack Mechanics

### Cryptid Attack Arsenals

**Bigfoot (3 weapons):**
| Form ID | Name | Type | Notes |
|---------|------|------|-------|
| 0x00868BC3 | crUnarmedBigfoot | Unarmed | Basic melee (WeaponTypeUnarmed) |
| 0x00868BC2 | crBigfootTickToss | Thrown | Model: projectiletick.nif — throws ticks at players |
| 0x00868BC1 | crBigfootTree | 1H Melee | Model: treebat.nif — swings a tree like a bat. Has WeaponTypeClub + WeaponTypeHammer |

Bigfoot's tick-tossing attack uses a unique projectile model. The tree-bat has full melee weapon keywords, meaning it benefits from melee damage calculations.

**Mothman (6+ weapons):**
| Form ID | Name | Notes |
|---------|------|-------|
| 0x0000EC88 | crUnarmedMothman | Basic melee |
| 0x0000F266 | crMothmanAttack1 | Primary attack |
| 0x00011A7C | crMothmanAttack2 | Secondary attack |
| 0x0000F39C | crMothmanRangedAttackSingleShotVer1 | Ranged single shot v1 |
| 0x004E5567 | crMothmanRangedAttackSingleShotVer2 | Ranged single shot v2 (updated) |
| 0x004E5568 | crMothmanRangedAttackRapidFire | Rapid fire ranged |
| 0x004E5566 | crMothmanAreaAttack | Area-of-effect attack |
| 0x0000F268 | crMothmanStalk | Non-combat stalking "weapon" |

The Mothman has SEVEN distinct attack modes. The "Stalk" weapon is non-damaging — it's what the Mothman uses when following players without attacking. Community wikis typically only document 2-3 attack types.

**Wendigo Colossus (4 weapons):**
| Form ID | Name | Notes |
|---------|------|-------|
| 0x0054821E | crUnarmedWendigoColossus | Basic melee |
| 0x0055830C | crWeaponWendigoColossusRadVomit | Radiation vomit attack |
| 0x0055830B | crWeaponWendigoColossusPoisonVomit | Poison vomit (different from rad!) |
| 0x0055830D | crWeaponWendigoColossusRanged | Ranged attack |

**Key finding:** The Wendigo Colossus has TWO distinct vomit attacks — radiation and poison. Most community guides don't differentiate between these, but they deal different damage types and would be resisted by different perks/armor.

**Grafton Monster (Multiple encounter variants):**
The Grafton Monster has encounter-specific weapon sets:
- Standard: crUnarmedGrafton, crGraftonOilBombWeapon, crGraftonOilBombSalvoWeapon
- SFS08 variant: Separate unarmed + oil bomb + salvo weapons
- SFS09 variant: Another complete set
- E09B variant: Yet another complete set

Each encounter variant has its own weapons, meaning Grafton Monsters in different events may deal different damage values.

**Flatwoods Monster:**
| Form ID | Name | Notes |
|---------|------|-------|
| 0x00004117 | crFlatwoodsMonsterLaser | Energy/Laser weapon (WeaponTypeEnergy + WeaponTypeLaser) |
| 0x0018A8D1 | crUnarmedFlatwoodsMonster | Melee backup |
| 0x007A85AC | cr_E01C_FlatwoodsMonsterLaser | Quest-specific laser variant |
| 0x007A85AD | cr_E01C_UnarmedFlatwoodsMonster | Quest-specific melee variant |

The E01C prefix indicates encounter-specific versions with potentially different damage values.

**Megasloth (4 weapons):**
- crMegaslothDirtThrow [0003226A] — Ranged dirt attack
- crMegaslothAreaAttack [0052193E] — AoE ground pound
- crMegaslothSandAttack [007DB400] — Sand throw
- crMegaslothSandStorm [00802D6A] — Sand storm AoE

**Trog (5+ weapons, The Pitt):**
- crUnarmedTrogMelee [0063CC26] — Basic melee
- crTrogBite [006419C1] — Bite attack
- crTrogSpitAttack [0063CC27] — Ranged spit
- crTrogAcidReflux [0065F1B8] — Acid AoE
- crUnarmedTrog_Fledgling/Superior — Level-tiered variants

**Sheepsquatch (3 weapons):**
- crUnarmedSheepsquatch [00479D53] — Melee
- crSheepsquatchRangedQuill [00482C6F] — Ranged quill attack
- Player weapons: SheepsquatchShard, SheepsquatchStaff, SheepSquatchClub

### NPC Weapon Variants by Faction

The ESM contains faction-specific creature weapon copies for:
- **Showmen**: crShowmenHandMadeRifle, crShowmenLeverGun
- **Municipal Auditors**: crMunicipalAuditorLeverGun, crMunicipalAuditorHandMadeRifle
- **Civilian Competitors**: crCivilianCompetitorLeverGun, crCivilianCompetitorHandMadeRifle
- **Mobsters**: crMobsterLeverGun
- **Fanatics**: crFanaticLeverGun, crFanaticSledgehammer (with custom bleed)
- **RD01 (Roadside) encounters**: crRD01_Stalker_MoleMinerGauntlet, RD01_cr* variants

Each faction's weapons could have different base damage values, explaining why the same enemy type hits differently in different encounters.

### Storm Boss (Vault 63 Content)
- crStormBossLightningGunAuto [006F4EBB] — Automatic lightning
- crStormBossLightningGun [006F4EB9] — Single-shot lightning
- Both use unique model: actors/stormboss/characterassets/dummyweapon.nif

### Beezlebub (Event Boss)
- crBeezlebubBeeSwarmSpawn [007B7711] — Spawns bee swarms as an attack
- crUnarmed_SSE_Beezlebub [007A3047] — Melee attack

### Abraxodyne Creature Variants
- Burn_crStingWingAbraxodyneSting [00831C6F] — Stingwing with Abraxodyne poison
- Burn_crRadScorpionAbraxodyneSting [0082F44F] — Radscorpion with Abraxodyne poison
- Burn_crRadScorpionBurningSting [008270F7] — Burning radscorpion variant

These "Burn_" prefix weapons are encounter-specific creature attacks, likely for the Abraxodyne Chemical event content.

---

## 6. Weapon Type Keywords — Complete Taxonomy

### Primary Damage Types
| Keyword | Form ID | Description |
|---------|---------|-------------|
| WeaponTypeBallistic | 00092A86 | Physical/bullet damage |
| WeaponTypeLaser | 00092A84 | Laser energy damage |
| WeaponTypePlasma | 00092A85 | Plasma energy damage |
| WeaponTypeEnergy | 0033A7C9 | Generic energy |
| WeaponTypeRadiation | 0033A7CA | Radiation damage |
| WeaponTypeExplosive | 0004C922 | Explosion damage |
| WeaponTypeFireDamage | 0051850D | Fire/burn damage |
| WeaponTypeCryoDamage | 00859A8C | Cryo/freeze damage |
| WeaponTypePoisonDamage | 00859A8D | Poison damage |
| WeaponTypeBleedDamage | 00824367 | Bleed damage |
| WeaponTypeDOT | 008447D8 | Damage over time |

### Weapon Class Types
| Keyword | Form ID |
|---------|---------|
| WeaponTypeRifle | 0004A0A1 |
| WeaponTypePistol | 0004A0A0 |
| WeaponTypeAutomatic | 0004A0A2 |
| WeaponTypeHeavyGun | 0004A0A3 |
| WeaponTypeMelee1H | 0004A0A4 |
| WeaponTypeMelee2H | 0004A0A5 |
| WeaponTypeThrown | 0004A0A6 |
| WeaponTypeUnarmed | 0005240E |
| WeaponTypeGrenade | 0010C415 |
| WeaponTypeMine | 0010C414 |

### Special/New Weapon Types
| Keyword | Form ID | Notes |
|---------|---------|-------|
| WeaponTypeNitro | 008445C8 | Unreleased Nitro weapon |
| WeaponTypeV63 | 008493EF | Applied to Meltdown + Ultracite weapons |
| WeaponTypeUltracite | 008493EE | New keyword for Ultracite weapons |
| WeaponTypeTeslaCannon | 007999F6 | Tesla Cannon type |
| WeaponTypeCremator | 00729BDA | Cremator heavy weapon |
| WeaponTypeAutomaticMelee | 006D5081 | Auto Axe, Chainsaw, Drill |
| WeaponTypeExplosiveHybrid | 005F0940 | Weapons with mixed explosive damage |
| WeaponTypeNonOffensive | 0040D277 | Camera, binoculars |
| WeaponTypeFishingRod | 007995A5 | Fishing rod |

**WeaponTypeV63 finding:** This keyword (0x008493EF, Form ID in the 0x0084 range = recent addition) is applied to:
1. The Meltdown weapon [006F5790]
2. UltraciteLaserGun [00186171]
3. Ultracite_GatlingLaser [002EF66E]
4. UltraciteLaserGun_E09A [00664D6A]

"V63" refers to Vault 63, suggesting these weapons were tagged as part of the Vault 63/Skyline Valley content system. The Meltdown weapon having this tag confirms it was introduced with or connected to the Vault 63 storyline.

---

## 7. Curve Table Weapon Damage System

All weapons use curve tables (CURV records) for level-scaled damage. Key patterns:

### Active Damage Curves (non-ZZZ)
These are the LIVE damage formulas the game uses:
- CT_Weapon_10mm_BaseDMG, CT_Weapon_44_BaseDMG
- CT_Weapon_CombatRifle_BaseDMG, CT_Weapon_HuntingRifle_BaseDMG
- CT_Weapon_CombatShotgun_BaseDMG, CT_Weapon_DoubleBarrel_BaseDMG
- CT_Weapon_PumpActionShotgun_DMG
- CT_Weapon_AssaultRifle_BaseDMG
- CT_Weapon_50CalMachineGun_BaseDMG
- CT_Weapon_MG42_BaseDMG, CT_Weapon_MiniGunDMG_BaseDMG
- CT_Weapon_GatlingPlasmaDMG
- CT_Weapon_LaserGun_BaseDMG, CT_Weapon_UltraciteLaserGun_DMG
- CT_Weapon_Flamer_BaseDMG
- CT_Weapon_FatmanDMG_BaseDMG, CT_Weapon_MissileLauncher_BaseDMG
- CT_Weapon_M79_BaseDMG
- CT_Weapon_10mm_SMGBaseDMG, CT_Weapon_SubMachineGun_BaseDMG
- CT_Weapon_PipeGun_BaseDMG, CT_Weapon_PipeBoltAction_BaseDMG
- CT_Weapon_Broadsider_BaseDMG
- CT_Weapon_DLC01AssaultronHeadChargingDMC
- CT_Weapon_PipeSyringerDMG
- CT_Weapon_DLC04_RevolverDMG (Western Revolver)
- CT_Weapon_GaussRifle_Presidential_BaseDMG
- CT_Weapon_Gauss_Shotgun, CT_Weapon_Gauss_Pistol
- CT_Weapon_Bow_RegularDMG, CT_Weapon_Bow_CompoundDMG
- CT_Weapon_AutoAxeDMG, CT_Weapon_ChainsawDMG

### Deprecated Damage Curves (ZZZ_ prefix)
These were REPLACED — old balance values:
- ZZZ_CT_Weapon_CrossbowDMG — Crossbow damage was rebalanced
- ZZZ_CT_Weapon_HandMadeGunDMG — Handmade was rebalanced
- ZZZ_CT_Weapon_RadiumRifleDMG — Radium Rifle was rebalanced
- ZZZ_CT_Weapon_GaussRifle_BaseDMG — Gauss Rifle was rebalanced
- ZZZ_CT_Weapon_PlasmaGunDMG_BaseDMG — Plasma Gun rebalanced
- ZZZ_CT_Weapon_PipeRevolver_BaseDMG — Pipe Revolver rebalanced
- ZZZ_CT_Weapon_GatlingLaser_BaseDMG — Gatling Laser rebalanced
- ZZZ_CT_Weapon_DLC01LightningGun_BaseDMG — Tesla Rifle rebalanced
- ZZZ_CT_Weapon_RailwayRifleDMG — Railway Rifle rebalanced
- ZZZ_CT_Weapon_DLC03_LeverGunDMG — Lever Action rebalanced
- ZZZ_CT_Weapon_DLC03_HarpoonGunDMG — Harpoon Gun rebalanced
- ZZZ_CT_Weapon_Enclave_PlasmaGunDMG — Enclave Plasma rebalanced

**Notable: Many melee weapons also had their curves deprecated** including Baseball Bat, Sledgehammer, Power Fist, Death Tambo, Pitchfork, Super Sledge, and numerous others. This suggests a large-scale melee rebalance pass.

### Weapon-Specific Overheating/Special Curves
- CT_Weapon_Gauss_Minigun_OverheatDMGMult — Gauss Minigun overheating penalty
- CT_Weapon_MeltdownOverheatingDMGMultiplier — Meltdown overheating system
- CT_Weapon_STORM_10mmSMGOverheatingAdditionalAmmo — 10mm SMG "Storm" variant overheating

### Tesla Cannon Curves (Extensive)
The Tesla Cannon has 13 active damage curves for its various receiver types:
- SparkGap I/II/III, SolidState I/II/III, Oscillator I/II/III, AmplifiedLens 1/2
- Plus 2 cut JuryRiggedBeamFocuser curves

### Cremator Curves
- CT_Weapon_Cremator_Slowburn, _Heavy, _Explosion, _Napalmer
- Plus cut: _BaseDMG, _burn, _Multi, _Double

### NPC-Only Damage Curves
- CT_Weapon_Flamer_NPC-ONLY [005A4005] — NPCs using Flamers get a DIFFERENT damage curve than players. This is a hidden balance mechanic.

---

## 8. Cut Legendary Weapon Mods

### "BOUNTY" Legendary System (Cut)
A complete set of "Bounty" legendary effects were built and disabled:

**Weapon effects:**
- zzz_BOUNTY_mod_Legendary_Weapon1_Recollecting — Star 1 effect
- zzz_BOUNTY_mod_Legendary_Weapon2_Guns_Rebate — Star 2 gun effect
- zzz_BOUNTY_mod_Legendary_Weapon2_Melee_Pulsating — Star 2 melee effect
- zzz_BOUNTY_mod_Legendary_Weapon2_Insane — Star 2 effect
- zzz_BOUNTY_mod_Legendary_Weapon3_SelfRepair — Weapon repairs itself
- zzz_BOUNTY_mod_Legendary_Weapon3_Healthy — Health-based effect
- zzz_BOUNTY_mod_Legendary_Weapon3_MadScientist — Unique effect

**Armor effects (same system):**
- BOUNTY legendary armor mods for stars 1-4 including Feral, Jagged, Savage, Barbarian, Reflex, Glowing

This appears to be a complete alternative legendary system tied to the Bounty event system. The effects span all three stars and cover both weapons and armor.

### Cut 4-Star Effects
- zzz_WIP4_mod_Legendary_Weapon4_Slayers — Cut 4th-star "Slayers" effect
- DEL_WIP4_mod_Legendary_Weapon4_Duelists — Deleted "Duelists" effect
- DEL_WIP4_mod_Legendary_Weapon4_Guns_Toppers — Deleted "Toppers" effect
- DEL_WIP4_mod_Legendary_Weapon4_Stunning — Deleted "Stunning" effect
- DEL_WIP4_mod_Legendary_Weapon4_Guns_SuperResilient — Deleted "SuperResilient"

### Other Cut Legendary Effects
- zzz_mod_Legendary_Weapon_Ranged4_Warmongers — Cut ranged 4-star
- zzz_mod_Legendary_Weapon_Melee4_Warmongers — Cut melee 4-star
- zzz_mod_Legendary_Weapon1_DamageViaCarryWeight — Damage scales with carry weight (cut!)
- zzz_mod_Legendary_Weapon1_Knockback — Knockback effect (removed)
- zzz_mod_Legendary_Weapon1_Guns_AmmoCapacity2x — Double ammo (nerfed to 4x version for specific weapons)

---

## 9. Named Unique Weapons (Quest Rewards / Event Exclusives)

### Expedition/Event Uniques (E08/E09 series)
| Form ID | Name | Base Weapon |
|---------|------|-------------|
| 0x006667CF | E09C_CompoundBow_BurningLove | Compound Bow |
| 0x006477EC | E08B_CombatShotgun_CrowdControl | Combat Shotgun |
| 0x006477EE | E08B_HuntingRifle_DoctorsOrders | Hunting Rifle |
| 0x006477ED | E08B_SuperSledge_TheDebilitator | Super Sledge |
| 0x00646880 | E08B_Minigun_FoundationsVengeance | Minigun |
| 0x00647820 | E08B_Blunderbuss_PiratePunch | Blunderbuss |
| 0x006477EF | E08B_DeathTambo_ToneDeath | Death Tambo |
| 0x00668991 | E09A_Broadsider_GrandFinale | Broadsider |
| 0x00668807 | E09A_BaseballBat_RatBat | Baseball Bat |
| 0x00662761 | E09B_SuperSledge_WhackerSmacker | Super Sledge |
| 0x0066275F | E09C_SubmachineGun_LoveTap | Submachine Gun |
| 0x0066957F | E09D_LeverGun_WesternSpirit | Lever Action |
| 0x00663505 | E09D_SingleActionRevolver_GunthersRevolver | Single Action Revolver |
| 0x00633475 | E08A_GulperSmacker | Unique melee |

### Survival Mode Uniques (Legacy — mode removed)
| Form ID | Name | Base Weapon |
|---------|------|-------------|
| 0x00403022 | Survival_44_MedicalMalpractice | .44 Revolver |
| 0x00403025 | Survival_50CalMachineGun_TheActionHero | .50 Cal MG |
| 0x00403024 | Survival_Fatman_TheGuarantee | Fat Man |
| 0x00403023 | Survival_LeverGun_SoleSurvivor | Lever Action |
| 0x00403021 | Survival_M79_CrushingBlow | M79 |
| 0x00403026 | Survival_Switchblade_TheQuickFix | Switchblade |
| 0x0042B0D2 | Survival_AssaultRifle_WhistleInTheDark | Assault Rifle |
| 0x0042B0CE | Survival_DeathclawGauntlet_UnstoppableMonster | Deathclaw Gauntlet |
| 0x0042B0CC | Survival_GatlingGun_ResoluteVeteran | Gatling Gun |
| 0x0042B0D0 | Survival_HarpoonGun_Kingfisher | Harpoon Gun |
| 0x0042B0CF | Survival_LaserGun_AcceptableOverkill | Laser Gun |
| 0x0042B0CB | Survival_Baton_DisorderlyConduct | Baton |
| 0x0042B0CD | Survival_LightningGun_NightLight | Tesla Rifle |
| 0x0042B0D1 | Survival_PipeWrench_MechanicsBestFriend | Pipe Wrench |
| 0x0042B0D3 | Survival_DoubleBarrelShotgun_SaltOfTheEarth | Double Barrel |
| 0x0042B0D4 | Survival_RevolutionarySword_CommandersCharge | Revolutionary Sword |

### Recent Additions (High Form ID)
| Form ID | Name | Notes |
|---------|------|-------|
| 0x008ADA17 | 44_Lawbringer | Newest — .44 Revolver unique |
| 0x0084F1F7 | SpearHealing | Healing Spear (active) |
| 0x0084460B | Nitro | Nitro pistol (unreleased) |
| 0x007D3AF4 | WarShrike | Melee/thrown hybrid, custom model |
| 0x0079AC42 | TeslaCannon | Tesla Cannon (released S19) |
| 0x0072DF0B | Stormcutter | Melee weapon, custom model |
| 0x00729BFE | Cremator | Heavy fire weapon (released S16) |
| 0x006F5790 | meltdown | Energy auto weapon |
| 0x006D3C69 | 10mm_CircuitBreaker | Named 10mm energy variant |

---

## 10. Weapon Balance Observations

### Wiki Discrepancies
1. **Wendigo Colossus has two vomit types** (rad AND poison) — most guides treat them as one
2. **Grafton Monster has encounter-specific weapons** — damage varies by event
3. **Mothman has 7 attack modes** — wikis typically list 2-3
4. **NPCs use different Flamer damage curves** than players (CT_Weapon_Flamer_NPC-ONLY)
5. **WeaponTypeV63 is applied retroactively** to Ultracite weapons — they're part of the Vault 63 content system
6. **The Meltdown has an overheating mechanic** (CT_Weapon_MeltdownOverheatingDMGMultiplier) that reduces damage at heat cap

### Massive Melee Rebalance Evidence
Nearly every melee weapon's original damage curve has been deprecated (ZZZ_ prefix), suggesting a comprehensive melee rebalance pass. Active curves remain only for: Bowie Knife, Cultist Blade, Chinese Officer Sword, Fire Axe, Knife, Knuckles, Machete, Pickaxe, Ripper, Sickle, Spear, Sledgehammer, Super Sledge, Walking Cane, Chainsaw, and a few others. All other melee weapons now use different (presumably shared or category-based) curves.

### Weapon Condition System (from Game Settings)
The game has a 9-tier weapon condition system that affects both spread and rate of fire:
- fWeaponConditionSpread1-9: Accuracy degrades with condition
- fWeaponConditionRateOfFire1-9: Fire rate degrades with condition
- fWeaponConditionJam1-4: Jamming chance at low condition
- fDamageGunWeapCondBase/Mult: Base damage penalty for condition
- fDamageMeleeWeapCondBase/Mult: Melee damage penalty for condition

---

## 11. Cross-Reference with Previous Findings

- **Finding 021** (Nitro): Confirmed and massively expanded. The Nitro has 60+ OMOD records, 3 ammo calibers, and was originally a revolver-style weapon
- **Finding 012** (4-Star Legendary): The BOUNTY legendary system represents an alternative/expanded legendary framework that was cut
- **Finding 018** (Dev Content): The Blue Moon (zzz_Moon_) content aligns with cut event content documented there
- **Finding 022** (Cover System): The weapon balance curves show weapons being continuously retuned, consistent with systems being pulled and reworked
