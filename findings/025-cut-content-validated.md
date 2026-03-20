# FO76 Cut Content Analysis: 4,831 Disabled (zzz_) Records

**Source**: `disabled_zzz_records.txt` (12,473 lines)
**Method**: Full ESM dump analysis of all zzz_-prefixed disabled records
**Date**: 2026-03-20
**Validation**: Cross-referenced against Fallout Wiki cut content pages (Fandom + fallout.wiki), community datamines, and web searches

---

## Record Type Breakdown

| Type | Count | Description |
|------|-------|-------------|
| COBJ | 1,151 | Crafting recipes |
| OMOD | 696 | Object modifications |
| PERK | 338 | Perk cards/effects |
| LVLI | 329 | Leveled item lists |
| WEAP | 258 | Weapons |
| MGEF | 212 | Magic effects |
| STAT | 205 | Static objects |
| BOOK | 204 | Plans/recipes/notes |
| SPEL | 156 | Spells/abilities |
| KYWD | 154 | Keywords |
| ARMO | 134 | Armor/apparel |
| MISC | 121 | Misc items |
| PCRD | 117 | Perk cards |
| ALCH | 105 | Consumables |
| CHAL | 72 | Challenges |
| ENCH | 69 | Enchantments |
| NPC_ | 67 | NPCs/creatures |
| ENTM | 50 | Entitlement/shop items |
| ACTI | 48 | Activators |

---

## Prefix Pattern Analysis

Major disabled content clusters by internal prefix:

| Prefix | Count | Meaning |
|--------|-------|---------|
| Babylon_ | 427 | Nuclear Winter battle royale (internal codename) |
| MOON_ | 119 | Once in a Blue Moon update iterative cuts |
| BOUNTY_ | 95 | Bounty Hunting legendary system cuts |
| GHL_ | 89 | Ghoul player system (Ghoulification) |
| MutatedEvents_ | 79 | Cut Mutated Public Events system |
| BURN_ | 66 | Burning Springs update iterative cuts |
| LGN_ | 45 | Legendary crafting system cuts |
| Tempest_ | 37 | Entire cut armor set |
| Storm_ | 30 | Skyline Valley (Storms) iterative cuts |
| XPD_ | 36 | Expeditions system cuts |
| NWOT_ | 26 | Nuka-World on Tour iterative cuts |
| MILE_ | 18 | Milepost Zero iterative cuts |
| WIP4_ | 23 | Work-in-progress legendary PA effects |
| RD01_ | 16 | Raid system (early) cuts |
| Nitro_ | 15 | Cut Nitro Rifle mod system |
| RECLAIM_ | 21 | Reclamation Day event system cuts |
| SSE_ | 7 | Skyline Valley creatures |

---

## VALIDATED UNDOCUMENTED FINDINGS

The following findings are NOT present on the Fallout Wiki cut content pages (checked against fallout.fandom.com/wiki/Fallout_76_cut_content, fallout.wiki/wiki/Fallout_76_Unused_Content, and fallout.wiki/wiki/Fallout_76_Removed_Content).

---

### 1. BOUNTY HUNTING: 14 Cut Legendary Effects (UNDOCUMENTED)

The Bounty Hunting system (Burning Springs update) shipped with 8 active legendary effects. The ESM contains 14 additional effects that were disabled, revealing the system was originally far more ambitious.

**Cut Weapon Legendary Effects:**
- **Pulsating** (`zzz_BOUNTY_HasLegendary_Weapon_Pulsating`) - Has a full explosion effect chain. The weapon would trigger area-of-effect pulses on hit.
- **Rebate** (`zzz_BOUNTY_HasLegendary_Weapon_Rebate`) - Likely returned ammo or resources on kill.
- **Healthy** (`zzz_BOUNTY_HasLegendary_Weapon_Healthy`) - Healing-on-hit weapon. Has a curve table capped at 300 health (`GetValue:0x0(0x2E1,0x0,0,0x0,-1)<=300`).
- **Adrenal** (`zzz_BOUNTY_HasLegendary_Weapon_Adrenal`) - Low-health damage boost (different from existing Adrenal Reaction mutation).
- **Self-Repairing** (`zzz_BOUNTY_HasLegendary_Weapon_SelfRepairing`) - Weapon that repairs its own condition.
- **Mad Scientist** (`zzz_BOUNTY_HasLegendary_Weapon_MadScientist`) - Unknown effect, shared between weapon and armor.
- **Insane** (`zzz_BOUNTY_HasLegendary_Weapon_Insane`) - Unknown effect, shared between weapon and armor.
- **Recollecting** (`zzz_BOUNTY_HasLegendary_Weapon_Recollecting`) - Likely returned some resource on kill.

**Cut Armor Legendary Effects:**
- **Glowing** (`zzz_BOUNTY_HasLegendary_Armor_Glowing`) - Full implementation with AddPerk effect. Condition checks evasion bonus.
- **Feral** (`zzz_BOUNTY_HasLegendary_Armor_Feral`) - Increases feral rate (attack speed?).
- **Self-Repairing** (`zzz_BOUNTY_HasLegendary_Armor_SelfRepairing`) - Armor that self-repairs condition.
- **Mad Scientist** (`zzz_BOUNTY_HasLegendary_Armor_MadScientist`) - Unknown, paired with weapon version.
- **Insane** (`zzz_BOUNTY_HasLegendary_Armor_Insane`) - Unknown, paired with weapon version.
- **Recollecting** (`zzz_BOUNTY_HasLegendary_Armor_Recollecting`) - Unknown, paired with weapon version.

**What shipped vs. what was planned:** Only 8 effects made it live (Active, Elementalist, Lucid, Reflex, Savage for armor; Barbarian, Feral, PickPocket for weapons). The cut effects represent a nearly 2x larger legendary pool that was scrapped. The "Self-Repairing" and "Pulsating" effects would have been genuinely novel mechanics.

**Evidence:** Full crafting recipes exist (`BOUNTY_co_mod_Legendary_*`), legendary shards (`BOUNTY_LegendaryShard_*`), enchantments, and magic effects -- the system was fully implemented then cut.

---

### 2. TEMPEST ARMOR: Complete Cut Armor Set (UNDOCUMENTED)

A full 5-piece non-PA armor set called "Tempest" was built and disabled. This is NOT documented on any wiki.

**Records found:**
- `zzz_Armor_Tempest_ArmLeft` (0x00755144)
- `zzz_Armor_Tempest_ArmRight` (0x00755148)
- `zzz_Armor_Tempest_LegLeft` (0x00755145)
- `zzz_Armor_Tempest_LegRight` (0x00755146)
- `zzz_Armor_Tempest_Torso` (0x00755147)
- `zzz_Headwear_Clothes_Tempest` (0x00755149)

**Supporting systems (all disabled):**
- 20 curve tables for per-piece DR/ER/Poison/Fire/Cold/Electric/Rad resistances across torso, arms, legs
- 3 unique lining mods: Amplified, Recharged, Thunderous
- Keywords for every piece slot (ma_armor_Tempest_*)
- Armor addon meshes (AA_Tempest_*)
- Visual geo effects for each lining (`abPlayerAmplified_Tempest_Geo`, etc.)
- Team AP spell (`Tempest_TeamAPSpell`, `Tempest_TeamAPCloakEffect`)

**Reconstruction:** Tempest was a Storm-themed armor set (Skyline Valley era, based on FormID range 0x0075xxxx) with three unique elemental linings that applied visual effects to the player. The "Amplified" lining appears to have boosted energy damage, "Recharged" restored AP, and "Thunderous" applied electric effects. The Team AP spell suggests it had a team support component. The DNAM description reads "Mod Association for Combat Armor pieces (for paints)" suggesting it used Combat Armor's base mesh with unique skins.

---

### 3. GHOUL PLAYER: 11 Cut Perk Cards (PARTIALLY DOCUMENTED)

The GHL (Ghoulification) system shipped with certain perks. These 11 perk cards were built as PCRD records and disabled:

| Card Name | Description |
|-----------|-------------|
| **200% Performance** | Unknown, possibly combat buff |
| **Acceptance** | Social/faction perk |
| **Burn The World** | Likely fire damage boost |
| **Cat Reflexes** | Dodge/agility bonus |
| **Frankenstein's Monster** | Likely resurrection or durability |
| **Junk Hunter** | Improved junk finding |
| **Legend Tracker** | Legendary enemy detection |
| **Persuasive** | Charisma/speech check bonus |
| **Through Job** | Unknown (alchemy keyword condition) |
| **Tunnel Runner** | Speed boost in tunnels/interiors |
| **Wild Card** | Elemental random damage (fire/poison/freeze/radiation/explosion) |

The **Wild Card** perk is the most complex -- it has a master spell that randomly selects from fire, poison, freeze, radiation, or explosion damage types. This has 4 ranks (`WildCardLastShotPerk01-04`) suggesting it scaled with investment.

**What's documented vs. not:** The Fandom wiki documents the ghoul player system broadly, but these specific cut perk cards and the Wild Card's multi-element random system are not documented anywhere.

---

### 4. NUCLEAR WINTER / "BABYLON": 427 Disabled Records Reveal Full BR System (PARTIALLY DOCUMENTED)

"Babylon" was Nuclear Winter's internal codename. The disabled records contain:

**Babylon-specific perk cards (68 PCRD records):** Complete copies of every standard perk card rebalanced for battle royale. Examples: `Babylon_CommandoMasterCard`, `Babylon_FrogLegsCard`, `Babylon_DodgyCard`. These are documented as existing but the full scope (68 cards) is not.

**Babylon-specific systems NOT documented:**
- **Gold Perk Card Packs** with multi-roll curve tables (Roll01-04 + GoldRoll01-04) -- a gacha/loot-box perk system
- **Beginner Perk Card Pack Currency** (`BabylonBeginnerPerkCardPackCurrency`) -- new players got starter packs
- **Babylon ZAX Ticket Currency** (`BabylonZAXTicketCurrency`) -- tickets earned through play
- **End-game ranking with Solo/Duo/Squad caps and XP** -- separate reward curves for each team size:
  - `BabylonEndGameSoloTeamRank_Caps/Experience`
  - `BabylonEndGameDuoTeamRank_Caps/Experience`
  - `BabylonEndGameSquadTeamRank_Caps/Experience`
- **Storm zone damage stages 1-4** with escalating curves
- **Babylon-specific consumables**: Ghost Mode potion, Warmth effect, radiation immunity, custom Stimpak/SuperStimpak/Diluted
- **Babylon-unique weapons**: Radium Rifle, Laser Damage variants
- **Vaporize visual effect** -- players killed could be vaporized
- **Reveal enemies on map potion** + detect briefcase/terminal/power armor perks
- **Nuke briefcase system** (`Babylon_Nuke_Briefcase`, `Babylon_Nuke_Code`) -- mini-nukes were lootable objectives
- **Tutorial flags system** (`BabylonTutorialFlags`)
- **Complete loot container hierarchy**: 17+ loot containers from Low/Med/High/Ammo/Meds/Armor/Melee/Perks/Grenades/Kits/Mines/Magazines/Holotapes/Serums

**Babylon bobbleheads and magazines:** Full pickup + potion + book + perk systems for all 14 bobbleheads and ~30 magazines, all rebalanced for BR play. These functioned as temporary buffs when picked up during a match.

---

### 5. MUTATED PUBLIC EVENTS: Cut Fallout 1st Tier System (UNDOCUMENTED)

A 4-tier Fallout 1st exclusive reward system for Mutated Events was built and disabled:

- `zzz_MutatedEvents_Giftbox_FalloutFirstPackage_Tier1-4`
- `zzz_LL_MutatedEvents_Fallout1st_Rewards_Tier1-4`
- `zzz_MutatedEvents_Package_SingleMutatedEvent_Fallout1st_Effect`

This would have given Fallout 1st subscribers tiered bonus rewards from Mutated Public Events. It was likely cut due to pay-to-win optics.

Additionally, **15 cut mutation-specific giftbox rewards** were found:
Active Camo, Blistering Cold, Chilling Mend, Clouded Toxins, Freezing Touch, Group Regeneration, Relentless, Resilient, Stinging Frost, Swift Footed, Swift Stalker, Toxic Blood, Unstable, Vaporous, Volatile

Each had consumable items, spells, and leveled reward lists. The system appears to have given players temporary mutation-like abilities as event rewards.

---

### 6. CUT WEAPONS (NOT ON WIKI CUT CONTENT PAGE)

| Weapon | FormID | Notes |
|--------|--------|-------|
| **Nitro Rifle** | 0x0085780F | Has 15+ mod crafting recipes (receivers, scopes, grips, muzzles, magazines). Internal name `zzz_NitroRifle`. Full weapon with .556 ammo variants including Anti-Scorchbeast, High Velocity, Central. Was likely the predecessor to or rejected version of a Burning Springs weapon. |
| **Heavy Incinerator** | 0x0072A8C2 | `zzz_HeavyIncinerator` -- Fallout 3's iconic weapon ported to 76 engine, then cut |
| **Fusion Cannon** | 0x0074D578 | `zzz_Broadsider_FusionCannon` -- Broadsider variant using fusion/energy ammo |
| **Flashbang Grenade** | 0x0055C15B | `zzz_FlashbangGrenade` -- stun/blind grenade (documented on Fandom) |
| **Soundmaker Grenade** | 0x0055C158 | `zzz_SoundmakerGrenade` -- noise distraction grenade (documented on Fandom) |
| **Nuclear Proliferator** | 0x005CF0A0 | `zzz_LGN_NuclearProliferator_Weapon` -- 4-rank scaling weapon with buildup AV |
| **Nuka Acid Grenade** | 0x00692A0D | `zzz_Moon_NukaAcidGrenade` -- Once in a Blue Moon era |
| **Nuka Homemade Grenade** | 0x00692A0C | `zzz_Moon_NukaHomemadeGrenade` -- crude explosive |
| **Cultist Pickaxe** | 0x006A0092 | `zzz_Moon_CultistPickaxe` -- melee weapon (documented partially) |
| **HeadHunter Scythe** | 0x007551DE | `zzz_HeadHunter_Scythe` -- melee scythe, Skyline Valley era. Note: This MAY have released later |
| **Pilgrim Musket** | 0x0059D52D | `zzz_Pilgrim_Musket` -- historical weapon |
| **Tesla Cannon variants** | 0x00799A10+ | `zzz_TeslaCannon_MissileLauncher`, `zzz_TeslaCannon_NukaLauncherTest` -- experimental Tesla Cannon crossovers |
| **Chaos Engine** | 0x00802196 | `zzz_P62_Weapon_ChaosEngine_ApplyCryoFreezeEffect` -- cryogenic weapon with freeze |
| **Abraxolator** | keyword only | `zzz_CustomItemName_Abraxolator` -- named weapon, likely Abraxodyne-themed |
| **Dynamite Spear** | recipe only | `zzz_W05_Recipe_Weapon_Melee_DynamiteSpear` -- explosive spear |

**Nitro Rifle deep dive:** The Nitro Rifle has the most complete unreleased weapon system in the dump. 15 crafting objects exist for it:
- Multiple receiver types (Base .556, Central, High Velocity, Anti-Scorchbeast)
- Scopes (Iron Sights, Reflex Glow, Short Scope, Long Scope, Long NV, Long Recon, Short Recon)
- Magazine, Grip, Muzzle Brake
- Special effects: Penetrating Stagger, Stagger
- Conditions reference stamps/plans vendors, suggesting it was destined for gold vendor or stamp vendor

---

### 7. CUT "PRIME" CREATURE SYSTEM (UNDOCUMENTED)

15 "Prime" creature variants were built and disabled. These are NOT the Primal Cuts event bosses:

`LvlDeathclaw_Prime`, `LvlYaoGuai_Prime`, `LvlSheepsquatch_Prime`, `LvlGulper_Prime`, `LvlRadscorpion_Prime`, `LvlHoneyBeast_Prime`, `LvlFogCrawler_Prime`, `LvlCaveCricket_Prime`, `LvlRadtoad_Prime`, `LvlGrafton_Prime`, `LvlSnallygaster_Prime`, `LvlSMBehemoth_Prime`, `LvlMirelurkQueen_Prime`, `LvlHermitCrab_Prime`, `LvlWolf_Prime`

Each has a matching `LLD_Creature_*_Prime` distribution record. The spawn condition checks against a collectron-like percentage roll (`GetRandomPercent`), suggesting these were meant to be rare overworld spawns -- elite versions of every major creature type. Distinct from Primal Cuts (which only uses a few boss types at event locations).

---

### 8. VAULT MISSION PERK CARD SLOTS (UNDOCUMENTED)

9 placeholder perk cards exist for a vault mission reward system that was never completed:

- **Vault 63**: 3 mission reward perk cards (`Vault63Mission01-03PerkCardTBD`)
- **Vault 96**: 3 mission reward perk cards (`Vault96Mission01-03PerkCardTBD`)
- **Vault 94**: 3 mission reward perk cards (`Vault94Mission01-03PerkCardTBD`)

These suggest each vault raid was originally planned to reward unique perk cards, one per mission tier. Vault 94 raids shipped without perk card rewards, and when Vault 94/96 were later repurposed for Daily Ops, the system was abandoned. Vault 63 eventually became the Skyline Valley update's explorable location but without raid missions.

---

### 9. CUT CAMP/WORKSHOP ITEMS OF NOTE (SELECTED)

| Item | Notes |
|------|-------|
| **Workshop Sub-Categories** | `zzz_Workshop2_SubCategory_Power_Switches`, `SubCategory_Furniture_Couches`, `SubCategory_Furniture_MusicalInstruments` -- the CAMP menu was going to be more granular |
| **Fish Tank Display** | `zzz_Fishing_workshop_FishDisplay_FishTank01` -- aquarium CAMP item |
| **Region-Specific Bait Stations** | 9 cut workshop items for region bait (Ash Heap, Cranberry Bog, Forest, Glowing, Mire, Savage Divide, Skyline Valley, Toxic Valley, Default) |
| **Pillory** | `zzz_SCORE_S19_Pillory` -- medieval punishment device for CAMP |
| **Ogua Eggs / Blue Devil Claws** | Workshop display items from cut Moon content |
| **Soda Machines** (7 flavors) | Freestanding Nuka-Cola machines: Orange, Quantum, Grape, Dark, Wild, Victory, Quartz |
| **Summoning Circle** | `zzz_ATX_FloorDecor_SummoningCircle` -- occult CAMP decoration |
| **Alien Whack-A-Mole** | `zzz_Invaders_AlienWhackAMole` -- interactive CAMP game |

---

### 10. GHOUL DISGUISE WARDROBE (UNDOCUMENTED DEPTH)

The GHL disguise system shipped with a simple drifter outfit + sack hood. But 12 disguise costumes were built:

- BoS Field Scribe, BoS Knight Lancer, BoS Engineer Scribe
- Enclave Officer Uniform (Clean)
- Raider Green Hood Gasmask, Raider Suit 02A
- Fasnacht Jester Mask
- Silver Shroud Costume
- Makeshift Ronin Helmet
- Deep Mine Gas Mask
- Enclave Colonel outfit + hat (SCORE S19)

This suggests the disguise system was originally faction-based -- you'd wear a BoS disguise to infiltrate BoS, Enclave disguise for Enclave, etc. This was simplified to a single generic disguise for launch.

---

### 11. CUT NUKA-COLA VARIANTS (UNDOCUMENTED)

5 Nuka-Cola recipes and consumables were cut from the Nuka-World on Tour update:

- **Nuka-Love** (with custom bottle model `nukacolabottlelove.nif`)
- **Nuka-Void** (with model `nukacolabottlevoid.nif`)
- **Nuka-Punch** (with model `nukacolabottlepunch.nif`)
- **Nuka-Bombdrop** (standard bottle model)
- **Nuka-Sunrise** (standard bottle model)

Each had a recipe book and was craftable at a soda fountain workstation. These appear to be NW4 (Nuka-World) DLC assets ported from Fallout 4 that were cut from the FO76 implementation.

---

### 12. "AD VICTORIAM" CUT MELEE SYSTEM (UNDOCUMENTED)

A BoS-themed melee combat system called "Ad Victoriam" was fully implemented then disabled:

- **Buildup mechanic**: Actor value `AV_AdVictoriam_Buildup` (0x00885C62) tracks power attack buildup
- **Buildup spell**: Triggers at 3 stacks of buildup
- **Power attack spell**: Fires on powered melee strikes
- **Apply perk effect**: Grants the Ad Victoriam perk on activation
- **Fortify melee damage**: `zzz_FortifyMeleeDamageAdVictoriam`

This was a BoS melee power attack combo system -- stack 3 power attacks to trigger a bonus effect. FormID range (0x00885Cxx) places it in very recent development, likely Burning Springs era or later.

---

### 13. FISHING: CUT BAIT AND RECIPE SYSTEM (UNDOCUMENTED SCOPE)

While fishing exists in FO76, the disabled records reveal a much larger planned system:

- **9 region-specific bait types** with workshop crafting recipes, static meshes, and cooking recipes
- **Glowing fish recipes**: Grilled Fish Glowing, Fish Chowder Glowing, Fish and Tatos Glowing
- **12 fishing rod mods** with recipes: Skyfire Float, Flamewood Float, Pin Bobber, Bicycle Rod, Crimson Stripe Float, Festive Float, Red Tide Float, Nuka-Cola Quantum Bobber, Twin Timber Float, Rocket Bobber, Scuba Tank backpack
- **Workshop items**: Kelp Curtain wall decor, Fish Display Plaque, Reclaimed Ship Chandelier, Angler/Crab Boat/Mirelurk Plushies
- **Fisherman's Cooking Stove** -- a dedicated cooking station for fish

The fishing system that shipped is a simplified version of what was planned. The region-specific bait system would have added strategic depth -- using Cranberry Bog bait in the Cranberry Bog for better catches, etc.

---

### 14. ENCLAVE SECRET OPERATIVE UNDERARMOR (UNDOCUMENTED)

A cut underarmor set for Enclave operatives:
- `zzz_RD01_Underarmor_EnclaveSecretOperative_FortifyEnergyResistEffect`
- `zzz_RD01_Underarmor_EnclaveSecretOperative_ReduceActionPointsEffect`
- `zzz_RD01_Underarmor_EnclaveSecretOperative_FortifyDamageResistEffect`

This was an underarmor that boosted DR and ER but reduced AP -- a trade-off underarmor. Associated with the RD01 (Raid) prefix, suggesting it was a vault raid reward.

---

### 15. CUT LEGENDARY CRAFTING MODS OF NOTE

| Mod | Description |
|-----|-------------|
| **Collector** (old) | `zzz_LegendaryCollectorPerk_old` -- earlier version of a loot-finding legendary |
| **Warmongers** | `zzz_MiscMod_Legendary_Warmongers` -- unknown legendary mod |
| **Max AP** | `zzz_MiscMod_Legendary_MaxAP` -- maximize action points |
| **Elusive** | `zzz_MiscMod_Legendary_elusive` -- stealth/dodge legendary |
| **Readers** | `zzz_MiscMod_Legendary_Readers` -- magazine/book buff legendary |
| **Weight (Ammo)** | `zzz_ench_Legendary_Armor_WeightAmmo` -- reduce ammo weight |
| **Slayers** (WIP4) | `zzz_WIP4_HasLegendary_Weapon_Slayers` -- extra damage vs specific enemy type |
| **Aegis** (WIP4) | `zzz_WIP4_Legendary_PowerArmor_AegisApplyTeamEffect` -- PA legendary that buffs team DR with count-based scaling |
| **Stalwarts** (WIP4) | `zzz_WIP4_Legendary_PowerArmor_StalwartsApplyTeamEREffect` -- PA legendary that buffs team ER |

The WIP4 (Work-In-Progress batch 4) PA legendaries Aegis and Stalwarts would have been the first team-buffing Power Armor legendary effects, making PA tanks viable team support.

---

## Summary of Validation Status

| Finding | Wiki Documented? | Novel? |
|---------|-----------------|--------|
| 14 cut Bounty legendary effects | NO | YES - names and mechanics undocumented |
| Tempest Armor (complete set) | NO | YES - entire armor set unknown |
| 11 GHL perk cards | NO | YES - specific cards undocumented |
| Babylon BR economy (currencies, ranks, loot) | PARTIALLY (mode known, internals not) | YES - economy design undocumented |
| Mutated Events Fallout 1st tiers | NO | YES - pay-gated reward system |
| Nitro Rifle (15 mods) | NO | YES - complete weapon system |
| Prime creature variants (15) | NO | YES - elite spawn system |
| Vault mission perk rewards (9) | NO | YES - reward perk cards |
| Ghoul faction-based disguises (12) | NO | YES - faction disguise wardrobe |
| Cut Nuka-Cola variants (5) | NO | YES - with custom bottle models |
| Ad Victoriam melee combo system | NO | YES - BoS power attack system |
| Expanded fishing bait/rod system | NO | YES - region-specific bait |
| Enclave Secret Operative underarmor | NO | YES - trade-off underarmor |
| WIP4 team-buff PA legendaries | NO | YES - Aegis/Stalwarts |
| Heavy Incinerator | PARTIALLY (FO3 weapon known) | YES - FO76 implementation |
| Fusion Cannon (Broadsider variant) | NO | YES |
| Cultist Executioner | YES (documented) | NO |
| Flashbang/Soundmaker grenades | YES (documented) | NO |
| HeadHunter Scythe | Likely released later | UNCERTAIN |
