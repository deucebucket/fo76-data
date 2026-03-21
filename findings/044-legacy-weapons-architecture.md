# Finding 044: Legacy Weapons Architecture - Why They Can't Die

## Summary

Legacy weapons in Fallout 76 are items carrying legendary effects that have been removed from the drop pool but continue to function because the engine stores legendary effects as persistent OMOD (Object Modification) references on individual item instances. Bethesda's removal strategy only targets the **input side** (loot tables and crafting filters) while leaving the **runtime side** (OMOD definitions and effect scripts) completely intact. There is zero server-side validation that checks whether an item's attached legendary mods are currently "legal."

## How Legendary Effects Are Stored on Items

### The OMOD Reference Architecture

Legendary effects are **not** baked into items as raw stat values. They are stored as **references to OMOD records** (Object Modification records) in the ESM. Each item instance in a player's inventory carries a list of attached OMOD FormIDs.

Key evidence from `objectreference.psc`:
```
Bool Function AttachMod(objectmod akMod, Int aiAttachIndex) Native
Bool Function AttachModToInventoryItem(Form akItem, objectmod akMod) Native
Function RemoveMod(objectmod akMod) Native
Function RemoveModFromInventoryItem(Form akItem, objectmod akMod) Native
Function RemoveAllMods() Native
```

These are **Native** functions (implemented in C++ engine code, not Papyrus), meaning the OMOD attachment system operates at the engine level. When a legendary item drops, the game:

1. Selects a base weapon/armor from a leveled list (`LGND_PossibleLegendaryItemBaseLists`)
2. Rolls for legendary rank (1-5 stars via `EpicCreaturesScript`)
3. Calls `GetAllowedMods()` on `PlayerLegendaryItemScript` to filter valid mods for each slot
4. Calls `AttachModToInventoryItem()` to apply the selected OMOD to the item instance

The item then carries these OMOD FormID references in its **instance data** within the character save. The OMOD itself defines the stat changes, keywords, and visual modifications.

### OMOD Records Still Exist in the ESM

Note:: **removed legendary OMADs are never deleted from the ESM**. They are either:

1. **Renamed with `zzz_` prefix** (standard Bethesda deprecation convention):
 - `zzz_mod_Legendary_Weapon_ExplosiveBullets` (0x001E73BD) - the original FO4-era explosive
 - `zzz_mod_Legendary_Weapon2_RadiationDamage` (0x004F5776)
 - `zzz_mod_Legendary_Weapon4_Poison` (0x004F5778)
 - `zzz_mod_Legendary_Weapon4_Bleed` (0x004ED02F)
 - `zzz_mod_Legendary_Armor_ReflectDamage` (0x004E89B3)
 - And **60+ more** deprecated legendary OMODs

2. **Explicitly tagged as LEGACY**:
 - `mod_Legendary_Weapon2_Guns_ExplosiveBullets_Shotgun_LEGACY` (0x00425E28) - reduced explosive for shotguns
 - `mod_Legendary_Weapon1_CritsHealGroup_LEGACY` (0x00527F8B)

3. **Left completely intact** with active FormIDs, FULL name references, and functional effect data

This is the core architectural reason legacies persist: the OMOD records that define their effects are still fully functional game data.

## What Bethesda Actually Changes to "Remove" an Effect

### Layer 1: The Legendary Rolling Filter (PlayerLegendaryItemScript)

The `GetAllowedMods()` function in `PlayerLegendaryItemScript` is the gatekeeper for new legendary rolls:

```papyrus
Struct LegendaryModRule
 objectmod LegendaryObjectMod
 FormList AllowedKeywords ; weapon must have one of these keywords
 FormList DisallowedKeywords ; weapon must NOT have any of these keywords
EndStruct
```

To remove an effect from the drop pool, Bethesda removes the OMOD from the `WeaponSlot1Mods` / `WeaponSlot2Mods` / etc. arrays. These are **property arrays filled at the quest level** (not in the script itself), so they're defined in the ESM quest data for the legendary crafting system.

### Layer 2: Keyword-Based Weapon Filtering

For effects that are restricted by weapon type rather than fully removed, Bethesda uses FormList-based keyword filters:

**Found in ESM:**
- `Legendary_Keywords_ExplosiveBulletsDisallowed` (0x0044FEB3) - keywords that block explosive
- `Legendary_Keywords_ExplosiveBulletsShotgunAllowed` (0x004263C2) - shotgun-specific allow list
- `Legendary_Keywords_ExplosiveBullets_ShotgunDisallowed` (0x005A4CBB) - shotgun-specific block list
- `LegendaryModRule_AllowedKeywords_WeaponTypeBallistic` (0x001E7174) - ballistic-only filter
- `LegendaryModRule_DisallowedKeywords_WeaponTypeGammaGun` (0x00249D8F)
- `LegendaryModRule_DisallowedKeywords_WeaponTypeCryoGun` (0x001F547B)
- `LegendaryModRule_DisallowedKeywords_NoUnlimitedAmmo` (0x002489DE)

The explosive bullets legendary was not fully removed. Instead, its `DisallowedKeywords` FormList was expanded to include `WeaponTypeEnergy` (0x0033A7C9) and other energy weapon keywords, preventing it from rolling on energy weapons. But the OMOD `mod_Legendary_Weapon2_Guns_ExplosiveBullets` (0x004F5771) itself remains fully functional.

### Layer 3: COBJ Crafting Recipes

For the legendary crafting bench (introduced with legendary crafting), each rollable mod has a COBJ recipe:
- `co_mod_Legendary_Weapon2_Guns_ExplosiveBullets` (0x00786F5F) - still exists (explosive is still rollable on ballistic weapons)
- `zzz_co_mod_Legendary_Armor3_Weight` (0x008A9FCF) - deprecated with `zzz_` prefix
- Many `zzz_BOUNTY_co_mod_Legendary_*` recipes disabled for bounty hunting system

### Layer 4: Leveled Item Lists (LVLI)

The LVLI records control what legendary modules and items can drop:
- `LGND_PossibleLegendaryItemBaseLists` (0x001CCDA8) - master list of base items
- `RESTRICTED_LL_LegendaryModule_*` - restricted legendary module drop lists
- `ZZZ_RESTRICTED_LL_LegendaryCore_*` - deprecated legendary core lists

## Why Existing Legacy Weapons Don't Break

### No Runtime Validation

**There is zero evidence of any script or system that validates whether an item's attached OMADs are currently in the active drop pool.** Exhaustive search of all decompiled scripts found:

- No `ValidateItem`, `CheckItemLegality`, `ValidateMod`, or similar functions
- No periodic scan of player inventories for illegal mod combinations
- No event handler for "item loaded with deprecated mod"
- No hook in the vending machine, trading, or drop systems that checks mod legality

The `VendingMachineScript` is minimal:
```papyrus
ScriptName Economy:VendingMachineScript Extends ObjectReference
Faction Property VendingMachineFaction Auto Const mandatory
Bool Property SellOnly = True Auto Const
```

No legendary validation. No mod checking. Items are treated as opaque containers of OMOD references.

### The Engine's Permissive Design

The Creation Engine (both FO4 and FO76) was designed with a **permissive mod system**:

1. **OMADs are independent records** - they define stat modifications, keyword additions, and visual changes. They don't "know" whether they're in the current drop pool.

2. **Item instances store OMOD FormIDs** - when an item is saved to a character, the save stores the base item FormID plus a list of attached OMOD FormIDs. On load, the engine resolves these FormIDs against the ESM data.

3. **FormID resolution is unconditional** - if the OMOD FormID exists in the ESM (even with `zzz_` prefix), the engine loads it and applies its effects. The `zzz_` prefix is a **naming convention for developers**, not a flag the engine interprets.

4. **`AttachMod()` has no legality check** - the Native function attaches any valid OMOD to any item. There is no "is this mod currently rollable?" check.

### The Specific Legacy Explosive Energy Weapon Case

The most famous legacy combination (Explosive + Energy Weapon) works because:

1. `mod_Legendary_Weapon2_Guns_ExplosiveBullets` (0x004F5771) is a fully functional OMOD
2. The OMOD's effect adds explosive damage to projectiles as a percentage of base damage
3. The `DisallowedKeywords` filter only operates at **roll time** via `PlayerLegendaryItemScript.GetAllowedMods()`
4. An item that already has this OMOD attached never re-runs the filter check
5. The engine happily applies the explosive effect to energy projectiles because the OMOD modifies weapon damage values universally

There is even a shotgun-specific LEGACY variant:
- `mod_Legendary_Weapon2_Guns_ExplosiveBullets_Shotgun_LEGACY` (0x00425E28)

This appears to be a reduced-damage version of explosive specifically for shotguns that were already in circulation, suggesting Bethesda at one point tried to address shotgun explosive balance by creating a weaker variant for existing items but apparently never deployed an item migration.

## Item Trading and Vending: No Checks

### Player Vending Machines

The `WorkshopVendorParentScript` manages vendor containers by category (Misc, Armor, Weapons, Bar, Clinic, Clothing, Chems) but performs no inspection of item properties:

```papyrus
ObjectReference[] Property VendorContainersWeapons Auto hidden
```

Items are moved into vendor containers as opaque references. No legendary mod validation occurs.

### Player-to-Player Trading

Trading uses the engine's native barter system. The `VendorInteractChoiceScript` is an empty shell:
```papyrus
Function TriggerVendorInteraction(player currentPlayer, ObjectReference vendor)
 ; Empty function
EndFunction
```

The actual trade logic is handled entirely in C++ engine code with no Papyrus-level hooks for item validation.

### Legendary Scrip Exchange

Searching for purveyor/exchange scripts reveals no item validation beyond basic category checks (weapon vs armor). The exchange accepts any legendary item for scrip regardless of whether its mods are currently rollable.

## Anti-Legacy and Item Validation: What Exists (Almost Nothing)

### What Was Found

1. **Vault Exploit Check System** - `VaultSystemExploitCheckTriggerScript` exists but is specifically for vault raid mission sequence validation (preventing players from skipping mission stages), not item validation.

2. **MoM Item Manager** - `MoMItemManagerQuestScript` has a `RevalidateItem` timer, but this is for Mistress of Mystery quest items (ensuring quest state consistency), not legendary mod validation.

3. **No Global Item Validation Service** - There is no background quest, periodic timer, or login check that scans player inventories for "illegal" legendary combinations.

### What Does NOT Exist

- No `ItemValidationService` or equivalent
- No `OnItemLoaded` event that checks mod legality
- No `AntiCheat_LegendaryCheck` or similar
- No keyword like `IllegalLegendary` or `BannedMod`
- No script that calls `RemoveModFromInventoryItem` based on a deprecation list
- No server-side filter in the trade/vending pipeline

## Duplication Exploit Architecture

### The Fundamental Flaw

FO76's item system inherited FO4's **client-authoritative inventory model** with server reconciliation added on top. The architectural flaw that enabled mass duplication:

1. **Items are objects with instance data** - each legendary item is a unique instance (base FormID + attached OMODs + condition + etc.)
2. **Client-server desync windows** - the game has timing windows during certain operations (trading, dropping, storing, server hopping) where the client and server briefly disagree about item ownership
3. **No transaction atomicity** - item transfers (trade, drop, stash, vendor) are not atomic database transactions. They are sequential operations (remove from source, add to destination) with a gap between them

### Known Exploit Categories (from architectural analysis)

1. **Trade Window Exploits** - initiating trade while simultaneously performing another inventory operation creates a race condition where the item can exist in two locations
2. **Server Hop Duplication** - quickly leaving a server after dropping/trading an item but before the server confirms the removal from inventory. The character save retains the item while the world instance also has it
3. **Vendor/Stash Transfer Exploits** - rapidly moving items between inventory, stash, and vendor containers during high server load creates desync opportunities
4. **Display Case Exploits** - CAMP display cases had a separate inventory tracking system that could desync from the main inventory

### Why Bethesda's Fixes Were Temporary

Each fix addressed a specific timing window but the fundamental architecture remained:
- Items are mutable objects, not ledger entries
- No blockchain-style transaction log
- No unique item serial numbers that could be checked for duplicates
- Server trusts client state during reconciliation windows

## Could Bethesda Remove All Legacy Weapons?

### Technically Yes, Here's What It Would Take

**Option 1: OMOD Migration Script (Targeted)**
```
For each player character in the database:
 For each item in inventory + stash + vendor + display:
 For each attached OMOD on the item:
 If OMOD is in the deprecated list:
 Call RemoveModFromInventoryItem(item, OMOD)
 Optionally: AttachModToInventoryItem(item, replacement_OMOD)
```

This is technically possible using the existing `RemoveModFromInventoryItem()` and `AttachModToInventoryItem()` Native functions. They could run this as a one-time migration.

**Option 2: Engine-Level FormID Blacklist**
Add a flag to OMOD records (beyond the `zzz_` naming convention) that tells the engine to skip loading that OMOD when resolving item instance data. Items would load without the blacklisted mod, effectively stripping them.

**Option 3: Delete the OMOD Records**
Remove the `zzz_` OMOD records from the ESM entirely. Items referencing deleted FormIDs would lose those mods on next load. This is the nuclear option and risks crashes if the engine doesn't handle missing FormID references gracefully.

**Option 4: Runtime Validation Quest**
Create a background quest that periodically scans player inventories and strips deprecated OMADs. The scripting functions already exist:
```papyrus
Function RemoveModFromInventoryItem(Form akItem, objectmod akMod) Native
Function RemoveAllModsFromInventoryItem(Form akItem) Native
```

### Why They Haven't Done It

1. **Player backlash** - Legacy weapons are the most valuable trade items in the game economy. Removing them would enrage the most dedicated players.
2. **Economy disruption** - Legacies are the de facto top-tier currency. Their removal would collapse the player trading economy.
3. **Technical risk** - A mass item migration on millions of character saves across all platforms is a high-risk operation. Any bug could corrupt inventories.
4. **Precedent** - Establishing that Bethesda can and will strip items from player inventories undermines player trust in item permanence.
5. **Revenue** - Players who chase legacy weapons through trading spend more time in-game. Some may spend money on Fallout 1st or Atoms.
6. **The Shotgun LEGACY OMOD Precedent** - The existence of `mod_Legendary_Weapon2_Guns_ExplosiveBullets_Shotgun_LEGACY` (a reduced-damage variant apparently intended for existing legacy shotguns) suggests Bethesda considered a migration approach but abandoned it. Creating replacement OMADs with reduced stats would be the "diplomatic" solution.

## Architectural Diagram

```
ITEM DROP / CRAFT FLOW (where filtering happens):
 EpicCreaturesScript
 -> determines star rating
 -> triggers AddLegendaryItemAbility spell
 -> PlayerLegendaryItemScript.GetAllowedMods()
 -> checks WeaponSlot1Mods/WeaponSlot2Mods/etc arrays
 -> for each LegendaryModRule:
 -> checks AllowedKeywords FormList against item keywords
 -> checks DisallowedKeywords FormList against item keywords
 -> if passes: add to AllowedMods array
 -> randomly selects from AllowedMods
 -> calls AttachModToInventoryItem(item, selectedMod)

ITEM PERSISTENCE (where no filtering happens):
 Character Save Data
 -> Item Instance: BaseFormID + [OMOD_FormID_1, OMOD_FormID_2, ...]
 -> On Load: resolve each OMOD_FormID against ESM
 -> If FormID exists in ESM: apply mod effects (NO legality check)
 -> If FormID missing: unknown behavior (likely skip or crash)

ITEM TRANSFER (where no filtering happens):
 Player Trade / Vending / Drop / Stash
 -> Item instance moves as-is with all attached OMADs
 -> No inspection of OMOD legality
 -> No validation against current drop pool
```

## The 60+ Deprecated Legendary OMADs

A partial catalog of `zzz_`-prefixed (deprecated) legendary OMADs still in the ESM, each one potentially active on existing items:

| OMOD ID | Name | Category |
|---------|------|----------|
| 0x001E73BD | zzz_mod_Legendary_Weapon_ExplosiveBullets | Original FO4 explosive |
| 0x004E89B3 | zzz_mod_Legendary_Armor_ReflectDamage | Reflect damage |
| 0x004E89B0 | zzz_mod_Legendary_Weapon_SuperDamage | Double damage |
| 0x004E89AF | zzz_mod_Legendary_Weapon_IncendiaryBullets | Incendiary |
| 0x004E89AE | zzz_mod_Legendary_Weapon_IronSightsIncreaseDamageResist | Steadfast |
| 0x004E89AC | zzz_mod_Legendary_Weapon_DamageVsGhouls | Ghoul Slayer's (old) |
| 0x004E89B2 | zzz_mod_Legendary_Armor_LessDMGGhouls | Ghoul resist (old) |
| 0x004E89B6 | zzz_mod_Legendary_Armor_MaxHealth | Max health |
| 0x004E89B5 | zzz_mod_Legendary_Armor_Speed | Movement speed |
| 0x004F5776 | zzz_mod_Legendary_Weapon2_RadiationDamage | Radiation damage |
| 0x004F5778 | zzz_mod_Legendary_Weapon4_Poison | Poison |
| 0x004ED02F | zzz_mod_Legendary_Weapon4_Bleed | Bleeding |
| 0x004EE54B | zzz_mod_Legendary_Armor4_ReflectMelee | Reflect melee |
| 0x005299FE | zzz_mod_Legendary_Weapon4_Guns_CritFreeze | Crit freeze |
| 0x00527F6C | zzz_mod_Legendary_Weapon4_Guns_CritFrenzy | Crit frenzy |
| 0x00527F74 | zzz_mod_Legendary_Armor2_Speed | Speed (slot 2) |
| 0x00527F82 | zzz_mod_Legendary_Armor4_APCost | AP cost |
| 0x00525400 | zzz_mod_Legendary_Weapon4_Stagger | Stagger |
| 0x00525401 | zzz_mod_Legendary_Weapon4_Cripple | Cripple |
| 0x005299ED | zzz_mod_Legendary_Weapon1_Knockback | Knockback |
| 0x0052BDC7 | zzz_mod_Legendary_Armor5_Health | 5-star health |
| 0x0052BDC5 | zzz_mod_Legendary_Armor5_Resistance | 5-star resistance |
| 0x0052BDC8 | zzz_mod_Legendary_Armor5_AP | 5-star AP |
| 0x0052BDC2 | zzz_mod_Legendary_Armor4_ReflectProjectiles | Reflect projectiles |
| 0x00606E7A | zzz_mod_Legendary_Weapon1_DamageViaCarryWeight | Damage by carry weight |
| 0x00609C47 | zzz_mod_Legendary_Armor1_ResistancesProportionalCarryWeight | Resist by carry weight |
| 0x004392CD | zzz_mod_Legendary_Weapon1_Guns_AmmoCapacity2x | Double ammo capacity |
| 0x0084D521 | zzz_mod_Legendary_Weapon3_HealingSpear | Healing spear |
| 0x008493EA | zzz_mod_Legendary_PowerArmor2_Fierce | PA Fierce |
| 0x008A9FD1 | zzz_mod_Legendary_Armor3_Weight | Weightless (slot 3) |
| 0x008A9FD2 | zzz_mod_Legendary_PowerArmor3_Weight | PA Weightless |

## Key Takeaways

1. **Legacy weapons are an architecture problem, not a data problem.** The engine has no concept of "this OMOD is deprecated." The `zzz_` prefix is a human-readable convention that the engine ignores.

2. **The validation gap is by design.** The Creation Engine was built for single-player Fallout 4 where all items were earned through gameplay. There was no need for item legality validation. FO76 inherited this assumption.

3. **Bethesda has the tools to fix this.** The `RemoveModFromInventoryItem()` Native function exists. A server-side migration script is technically feasible. They choose not to use it.

4. **The shotgun LEGACY OMOD is a smoking gun.** The existence of `mod_Legendary_Weapon2_Guns_ExplosiveBullets_Shotgun_LEGACY` proves Bethesda prototyped a targeted migration approach (create weaker replacement OMADs, swap them on existing items) but never deployed it.

5. **Duplication was an architecture failure, not a bug.** The client-server inventory model lacks transactional atomicity, making any item transfer operation a potential duplication vector. This is why dupe exploits kept recurring in different forms.

6. **The 60+ deprecated OMADs are ghosts in the machine.** Every single one is still a valid, functional game record. Any item that references one will continue to work indefinitely, or until Bethesda removes the records from the ESM (which they have never done for any OMOD).

---

*Source data: SeventySix.esm dump (OMOD, LVLI, COBJ, FLST, KYWD records), decompiled Papyrus scripts (PlayerLegendaryItemScript, EpicCreaturesScript, ObjectReference, VendingMachineScript, WorkshopVendorParentScript)*

*Analysis date: 2026-03-20*
