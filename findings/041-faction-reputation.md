# Fallout 76: Complete Faction Reputation System

Extracted from ESM dumps, decompiled Papyrus scripts, and global variable records.

---

## 1. Reputation System Architecture

The reputation system is built on **ActorValues** stored on the player, tracked by `W05_ReputationPlayerScript` (the core engine) and `W05_ReputationQuestScript` (per-quest stage hooks).

### Core ActorValues (AVIF records)
| ActorValue | FormID | Description |
|---|---|---|
| `Reputation_AV_Crater` | 0x0055C5BF | Crater (Raider) reputation value |
| `Reputation_AV_Foundation` | 0x0055C5C0 | Foundation (Settler) reputation value |
| `Reputation_AV_Vault63` | 0x0068DE49 | Skyline Valley / Vault 63 reputation value |
| `Reputation_AllowHostileTier_AV_Crater` | 0x00592E8A | Gate: if <= 0, can't drop below Cautious with Crater |
| `Reputation_AllowHostileTier_AV_Foundation` | 0x00592E8B | Gate: if <= 0, can't drop below Cautious with Foundation |
| `Reputation_AllowHostileTier_AV_Vault63` | 0x0068DE4A | Gate: if <= 0, can't drop below Cautious with Vault 63 |

### Key Script: `W05_ReputationPlayerScript`

This script defines two critical data structures:

**ReputationFactionDatum** (per-faction config):
- `Reputation_AV` — the ActorValue tracking the player's numeric rep
- `Reputation_Faction` — NPC faction linked to this reputation
- `MurderRepMod_Global` — rep penalty for killing faction NPCs (references `Rep_Mod_Murder`)
- `ReputationTierAboveHostile_Global` — floor value when `AllowFactionHostileTier_AV <= 0`
- `ReputationTierAboveNeutral_Global` — threshold for enabling damage forgiveness
- `AllowFactionHostileTier_AV` — controls whether Hostile tier is reachable
- `CurrentTier_Global` — hidden, tracks current tier state

**ReputationTierDatum** (per-tier config):
- `Reputation_AV` — which faction this tier belongs to
- `ReputationTier_Global` — global holding the numeric threshold value
- `TierPerk` — perk granted/removed at this tier
- `AchievementID` — achievement triggered on reaching this tier (default -1)

### Anti-Grief Mechanic: `_ModifyReputationSpinlock`

The reputation system uses a **spinlock** (`_ModifyReputationSpinlock`) to prevent concurrent reputation modifications. This ensures server-side atomicity in multiplayer.

### Murder Keyword: `Reputation_IgnoreMurder_Keyword` (0x005A0303)

NPCs tagged with this keyword do NOT trigger the murder reputation penalty when killed. Used for quest-specific NPCs, creatures, and combat-zone actors.

---

## 2. Reputation Tiers and Thresholds

### Crater (Raiders) Reputation Tiers
| Tier | Rank Name | Global Variable | FormID |
|---|---|---|---|
| 0 | Hostile | `Rep_Tier_Crater_0_Hostile` | 0x0055C5B1 |
| 1 | Cautious | `Rep_Tier_Crater_1_Cautious` | 0x0055C5B2 |
| 2 | Neutral | `Rep_Tier_Crater_2_Neutral` | 0x0055C5B3 |
| 3 | Cooperative | `Rep_Tier_Crater_3_Cooperative` | 0x0055C5B4 |
| 4 | Friendly | `Rep_Tier_Crater_4_Friendly` | 0x0055C5B5 |
| 5 | Neighborly | `Rep_Tier_Crater_5_Neighborly` | 0x0055C5B6 |
| 6 | Ally | `Rep_Tier_Crater_6_Ally` | 0x0055C5B7 |

### Foundation (Settlers) Reputation Tiers
| Tier | Rank Name | Global Variable | FormID |
|---|---|---|---|
| 0 | Hostile | `Rep_Tier_Foundation_0_Hostile` | 0x0055C5B8 |
| 1 | Cautious | `Rep_Tier_Foundation_1_Cautious` | 0x0055C5B9 |
| 2 | Neutral | `Rep_Tier_Foundation_2_Neutral` | 0x0055C5BA |
| 3 | Cooperative | `Rep_Tier_Foundation_3_Cooperative` | 0x0055C5BB |
| 4 | Friendly | `Rep_Tier_Foundation_4_Friendly` | 0x0055C5BC |
| 5 | Neighborly | `Rep_Tier_Foundation_5_Neighborly` | 0x0055C5BD |
| 6 | Ally | `Rep_Tier_Foundation_6_Ally` | 0x0055C5BE |

### Vault 63 (Skyline Valley) Reputation Tiers
| Tier | Rank Name | Global Variable | FormID |
|---|---|---|---|
| 0 | Hostile | `Rep_Tier_Vault63_0_Hostile` | 0x0068DE3A |
| 1 | Cautious | `Rep_Tier_Vault63_1_Cautious` | 0x0068DE38 |
| 2 | Neutral | `Rep_Tier_Vault63_2_Neutral` | 0x0068DE3B |
| 3 | Cooperative | `Rep_Tier_Vault63_3_Cooperative` | 0x0068DE36 |
| 4 | Friendly | `Rep_Tier_Vault63_4_Friendly` | 0x0068DE3C |
| 5 | Neighborly | `Rep_Tier_Vault63_5_Neighborly` | 0x0068DE35 |
| 6 | Ally | `Rep_Tier_Vault63_6_Ally` | 0x0068DE39 |

**NOTE:** The ESM stores the tier threshold VALUES inside these globals, but the actual numeric values are not exposed in the decompiled scripts (they're set in the ESM record data). The tier naming convention reveals a **7-tier system** (0-6), which notably includes "Cooperative" as Tier 3 -- a tier NOT shown in the in-game UI bar, which only displays Hostile/Cautious/Neutral/Friendly/Neighborly/Ally. The "Cooperative" tier exists in data as a hidden internal checkpoint.

---

## 3. Reputation Gain/Loss Values

### Standard Modifier Globals
| Global Variable | FormID | Purpose |
|---|---|---|
| `Rep_Mod_Add_Small` | 0x003FB9F4 | Small positive rep gain |
| `Rep_Mod_Add_Medium` | 0x003FB9F5 | Medium positive rep gain |
| `Rep_Mod_Add_Large` | 0x003FB9F6 | Large positive rep gain |
| `Rep_Mod_Add_Huge` | 0x003FB9FA | Huge positive rep gain |
| `Rep_Mod_Subtract_Small` | 0x003FB9F7 | Small rep penalty |
| `Rep_Mod_Subtract_Medium` | 0x003FB9F8 | Medium rep penalty |
| `Rep_Mod_Subtract_Large` | 0x003FB9F9 | Large rep penalty |
| `Rep_Mod_Subtract_Huge` | 0x003FB9FB | Huge rep penalty |

### Daily Quest Reputation Globals
| Global Variable | FormID | Purpose |
|---|---|---|
| `Rep_Mod_DailyR_Add` | 0x0059C24B | Daily raider quest rep reward (Retirement Plan, Wren's tech retrieval) |
| `Rep_Mod_DailyS_Add` | 0x0059C24A | Daily settler quest rep reward (Ward's theft recovery) |

### Main Quest Reputation Globals
| Global Variable | FormID | Purpose |
|---|---|---|
| `Rep_Mod_MQ_Add_Small` | 0x0059C23B | Small main quest rep gain |
| `Rep_Mod_MQ_Add` | 0x0059C23C | Standard main quest rep gain |
| `Rep_Mod_MQ_Add_Large` | 0x0059C23D | Large main quest rep gain |
| `Rep_Mod_Murder` | 0x00592E89 | Murder penalty (killing faction NPCs) |

### Vault 79 Gold Heist Reputation (Quest 206P)
| Global Variable | FormID | Purpose |
|---|---|---|
| `Rep_Mod_206_Gold_SingleFaction` | 0x0059C274 | Give all gold to your faction |
| `Rep_Mod_206_Gold_SplitMyFaction` | 0x0059C275 | Split gold, your faction's share |
| `Rep_Mod_206_Gold_SplitOtherFaction` | 0x0059C273 | Split gold, other faction's share |
| `Rep_Mod_206_Gold_KeepMyself` | 0x0059C276 | Keep gold for yourself |

### Expedition Recipe Reputation (XPD)
| Global Variable | FormID | Purpose |
|---|---|---|
| `XPD_Fuel_Recipe_ReputationPositive` | 0x0065850A | Positive rep for Expedition recipe quest |
| `XPD_Fuel_Recipe_ReputationNeutral` | 0x0065850B | Neutral rep for Expedition recipe quest |

### Event Reputation
| Global Variable | FormID | Purpose |
|---|---|---|
| `E08A_ReputationRewardValue` | 0x00647A37 | Moonshine Jamboree reputation reward |
| `E08B_ReputationReward` | 0x00647822 | Moonshine event reputation reward |
| `W05_Daily_Foundation01_DonationRepValue` | 0x00635AEE | Donation reputation bonus (Ward quest) |

### "Fixer" Reputation Pay Tiers (Wayward/Sol dialogue)
| Global Variable | FormID | Purpose |
|---|---|---|
| `Rep_Pay01_Fixer` | 0x0059A662 | Fixer payment tier 1 (cap cost to fix rep) |
| `Rep_Pay02_Fixer` | 0x0059AA71 | Fixer payment tier 2 |
| `Rep_Pay03_Fixer` | 0x0059AA6F | Fixer payment tier 3 |
| `Rep_Pay04_Fixer` | 0x0059AA70 | Fixer payment tier 4 |

The Wayward's Sol acts as a "reputation fixer" -- the player can pay caps to repair damaged reputation with Crater or Foundation. The scripts (`TIF_W05_DialogueTheWayward`) check `Rep_Tier_Crater_0_Hostile`, `Rep_Tier_Crater_1_Cautious`, and equivalent Foundation globals to determine pricing tiers based on how badly reputation is damaged.

---

## 4. Reputation Actions by Source

### Foundation (Settler) Daily: Ward's Quest (`W05_Daily_Foundation01`)
- **Complete quest (return item):** `Rep_Mod_DailyS_Add` to Foundation
- **Return item to Crater raider thief instead:** `Rep_Mod_Add_Small` to Crater, `Rep_Mod_Subtract_Small` to Foundation
- **Donation option:** `W05_Daily_Foundation01_DonationRepValue` extra Foundation rep
- **Rep_Mod_Add_Medium** and **Rep_Mod_Add_Large** also referenced as potential rewards

### Crater (Raider) Daily: Wren's Tech (`W05_Daily_R01`)
- **Complete quest:** `Rep_Mod_DailyR_Add` to Crater

### Crater Daily: Retirement Plan (`W05_Daily_R02`)
- **Complete quest:** `Rep_Mod_DailyR_Add` to Crater
- **Bonus (specific targets):** `Rep_Mod_Add_Large` to Crater

### Davenport's Photo Daily (`W05_Daily_Photo`)
- **Complete photo quest:** Can award Crater OR Foundation rep depending on target
- **Standard reward:** `Rep_Mod_Add_Medium` or `Rep_Mod_Add_Small`
- **Bonus (specific photo):** `Rep_Mod_Add_Huge` for particularly valuable intelligence photos

### Main Quest Line Reputation Events
**Raider MQ 203P (Arena fight):**
- `Rep_Mod_Add_Large` to Crater (completing arena)
- `Rep_Mod_Subtract_Medium` to Crater (betrayal/bad choices)
- `Rep_Mod_MQ_Add` standard quest completion

**Settler MQ 203P (Robobrain quest):**
- `Rep_Mod_Add_MQ` to Foundation on completion

**Vault 79 Heist MQ 102P:**
- `Rep_Mod_MQ_Add_Small` to both Crater and Foundation at various stages

**Post-MQ Dialogue with Meg/Gail:**
- **"Foundation is weak" (agree with Meg):** `Rep_Mod_Add_Medium` to Crater
- **"Don't have to listen to this":** `Rep_Mod_Subtract_Small` to Crater
- **"Good parent" (support Gail):** `Rep_Mod_Add_Medium` to Crater
- **"Stupid mistakes" (insult Gail):** `Rep_Mod_Subtract_Medium` to Crater

### Random Encounter Reputation
- **Camp encounters (AF02 - Settler/Raider doctors):** `Rep_Mod_Add_Small` for donating supplies
- **Camp encounters (BS_RE_CampJN01):** `Rep_Mod_Add_Small` or `Rep_Mod_Add_Medium` to Crater
- **Ohio River Adventure (mirelurk defend):** Reputation reward via dialogue after defending

### Vault 79 Gold Distribution (MQA_206P)
The final gold split has major reputation consequences:
- **Give all gold to your aligned faction:** `Rep_Mod_206_Gold_SingleFaction` (large gain)
- **Split gold with both factions:** `Rep_Mod_206_Gold_SplitMyFaction` (moderate gain to yours), `Rep_Mod_206_Gold_SplitOtherFaction` (small gain to other)
- **Keep gold for yourself:** `Rep_Mod_206_Gold_KeepMyself` (large LOSS to both)
- **Hostile tier unlocking:** `Reputation_AllowHostileTier_AV_Crater` and `Reputation_AllowHostileTier_AV_Foundation` are modified during this quest, meaning certain gold choices can make you permanently hostile

### NPC Murder Penalty
- Killing faction NPCs without `Reputation_IgnoreMurder_Keyword`: `Rep_Mod_Murder` applied to relevant faction
- **Anti-grief floor:** If `AllowFactionHostileTier_AV <= 0`, reputation cannot drop below Cautious tier (prevents accidental hostile lockout during normal gameplay)

---

## 5. Daily Reputation Caps

The system does NOT use an explicit "daily cap" global. Instead, daily quests are limited by:
1. **Quest availability:** Each daily quest can only be completed once per 24-hour real-time cycle
2. **`Rep_Mod_DailyR_Add` and `Rep_Mod_DailyS_Add`:** These globals define the FIXED amount per daily completion -- the effective daily cap is determined by how many dailies exist per faction

Available dailies per reset cycle:
- **Crater:** Wren's tech retrieval + Retirement Plan + Rocksy (Ohio River Adventure defend)
- **Foundation:** Ward's stolen item + Davenport's photo (can be allocated to either faction)
- **Both:** Random encounters provide additional small rep gains (no cap on these, but spawn-limited)

The Expedition recipe system (`XPD_Fuel_Recipe`) provides an additional reputation source outside the daily structure.

---

## 6. Reputation Effects on Vendors and Items

### Gold Bullion Vendor System
Gold bullion vendors are reputation-gated:

| Vendor | Faction | FormID |
|---|---|---|
| `W05_Settler_Samuel_GoldVendorFaction` | Foundation (Samuel) | 0x0059672B |
| `W05_Raider_Mortimer_GoldVendorFaction` | Crater (Mortimer) | 0x0058736D |
| `W05_SecretService_Reginald_GoldVendorFaction` | Secret Service (Reginald) | 0x0057CE6B |
| `BS02_SpecialVendor_Minerva_GoldVendorFaction` | Minerva (traveling) | 0x005FFDEA |

### Gold Vendor Tier Economy
13 pricing tiers exist for gold vendors:
```
Econ_GoldVendor_Tier_01 through Econ_GoldVendor_Tier_13
(FormIDs 0x005A5044 through 0x005A5050)
```
These tiers likely control plan pricing, tied to reputation rank progression.

### Vendor Toggle Globals (Live Tuning)
| Global | FormID | Purpose |
|---|---|---|
| `W05_GoldVendor_Settler_LiveToggle` | 0x005A3C66 | Enable/disable Foundation gold vendor |
| `W05_GoldVendor_Raider_LiveToggle` | 0x005A3C67 | Enable/disable Crater gold vendor |
| `W05_GoldVendor_SecretService_LiveToggle` | 0x005A3C65 | Enable/disable SS gold vendor |

### Vendor Reset Schedule
| Global | FormID | Purpose |
|---|---|---|
| `Vendor_Reset_Days_Settlers_GoldVendor` | 0x005A37E6 | Days between Foundation vendor reset |
| `Vendor_Reset_Days_Raiders_GoldVendor` | 0x005A37E7 | Days between Crater vendor reset |

### Gold Vending Machines (caps-based)
| Vending Machine | FormID |
|---|---|
| `Gold_VendingMachine_VendorFaction_Crater` | 0x005A4D7C (mapped to 0x005A5438) |
| `Gold_VendingMachine_VendorFaction_Foundation` | 0x005A5439 |
| `Gold_VendingMachine_VendorFaction_WhitespringMall` | 0x00667492 |

### Reputation-Gated Vendor Perk
`W05_Crater_PlayerVendorInteractChoicePerk` — referenced in MQ_102P, this perk appears to control vendor interaction availability based on Crater reputation. Each reputation tier adds/removes a `TierPerk` via `ReputationTierDatum`, which likely gates specific vendor inventories and plan availability.

### Bullion Purchase Tracking
`W05_BullionPurchased` — ActorValue tracking total bullion purchased (referenced in Wayward script alongside `GoldBullion_LastPurchasedTimestamp`), used to enforce the weekly bullion purchase cap. The Wayward script shows `DayOfWeekToResetBullion = 1` (Monday reset) and `DaysInAWeek = 7`.

---

## 7. Cut Faction Content (ZZZ/CUT prefix)

### Cut Factions
| Faction | FormID | Notes |
|---|---|---|
| `ZZZNPE_VRCitizenFaction` | 0x007283F3 | Cut VR tutorial citizen faction (see finding 027) |
| `ZZZNPE_VRBullyFaction` | 0x00709C2A | Cut VR tutorial bully faction |
| `ZZZ_CultistHighPriestFaction` | 0x006295E1 | Original cultist high priest faction, replaced by `CultistHighPriestFactionDUPLICATE000` (0x006366F4) |
| `zzzNW020Faction` | 0x0050E626 | Nuclear Winter faction (cut game mode) |
| `zzzBurn_REPackIn_FactionAssault` | 0x007AE5AB (PKIN) | Cut Burning Springs faction assault pack-in |

### Cut Whitespring Vendor Factions
Five complete vendor faction sets were cut from the Whitespring:
| Faction | FormID |
|---|---|
| `CUT_LC060_WhitespringVendor_BoS_Faction` | 0x004102A9 |
| `CUT_LC060_WhitespringVendor_Raiders_Faction` | 0x004102A8 |
| `CUT_LC060_WhitespringVendor_Responders_Faction` | 0x004102A6 |
| `CUT_LC060_WhitespringVendor_FreeStates_Faction` | 0x004102A7 |
| `CUT_LC060_WhitespringVendor_Neutral_Faction` | 0x004102AA |

These were replaced by the current live vendor factions (same FormIDs without CUT_ prefix, different FormIDs). The existence of BOTH sets suggests the Whitespring vendor factions were restructured during development -- the cut versions may have had different inventory pools or faction alignment requirements.

### Cut Content Insight: `DEL_XPD_OvergrownPollinatorFaction` (0x006C3326)
A deleted expedition faction for "Overgrown Pollinators" -- likely cut enemies from an expedition.

---

## 8. Ohio / Burning Springs Faction System (Rust Raiders, Highway Town Settlers)

The Burning Springs update ("Burn_" prefix) introduced a new regional faction structure in Ohio. Unlike Wastelanders' reputation system, this uses **combat factions** rather than a numeric reputation ActorValue -- there are NO `Reputation_AV_Ohio` or equivalent globals.

### Core Ohio Factions
| Faction | FormID | Role |
|---|---|---|
| `Burn_RustRaiderFaction` | 0x007F0A52 | Rust Raiders (new raider sub-faction) |
| `Burn_HTSettlerFaction` | 0x007F8228 | Highway Town Settlers |
| `Burn_HTSettlerChemVendorFaction` | 0x00844090 | HT Settler chem vendor |
| `Burn_HTSettlerGunVendorFaction` | 0x00844093 | HT Settler gun vendor |
| `Burn_HTSettlerFoodVendorFaction` | 0x00844091 | HT Settler food vendor |
| `Burn_HTSettlerGeneralVendorFaction` | 0x00844092 | HT Settler general vendor |
| `Burn_Doctor_VendorFaction` | 0x0081ACE8 | Ohio doctor vendor |
| `Burn_BountyTargetFaction` | 0x007D2B18 | Bounty system targets |
| `Burn_Bounty_CaptiveFaction_NotPlayerFriendly` | 0x0082F6C6 | Bounty captives (hostile) |

### Ohio Combat/Event Factions
| Faction | FormID | Purpose |
|---|---|---|
| `Burn_RobotFaction` | 0x0081F1B0 | Ohio region robots |
| `Burn_ViciousDogFaction` | 0x0081F1AF | Ohio hostile dogs |
| `Burn_E01_CombatantsFaction` | 0x00893EE6 | Event combatants |
| `Burn_E01_TamedDeathclawFaction` | 0x00893EE5 | Tamed deathclaw event |
| `Burn_E01_DeathclawFaction` | 0x0081CAC7 | Ohio deathclaws |
| `Burn_DinoGolf_Faction` | 0x0080282A | Dino Golf location faction |
| `Burn_SDM_Faction` | 0x007FECA1 | SDM (likely location) faction |
| `BURN_AthensProtectronFaction` | 0x00824BD7 | Athens protectrons |
| `BURN_AthensGhoulFaction` | 0x00824BD6 | Athens ghouls |
| `BURN_Eugene_Faction` | 0x0086A7BD | Eugene NPC faction |
| `BURN_E02_Sinkhole_Faction` | 0x0080BFDD | Sinkhole event faction |

### Ohio Faction Assault System
The Burn prefix includes a faction assault random encounter system:
| Faction | FormID |
|---|---|
| `Burn_REFactionAssaultFaction01` | 0x007AE596 |
| `Burn_REFactionAssaultFaction02` | 0x007AE597 |
| `Burn_REFactionAssaultFaction03` | 0x007AE595 |
| `Burn_REFactionAssaultFactionFriend` | 0x007AE594 |

Multiple quest scripts handle these encounters (`qf_burn_re_factionassault*`), with variants for temple, background, arena, defense, and Rust Raider attacks.

### Ohio Arena System
| Faction | FormID |
|---|---|
| `Burn_SQ01_ArenaFightFaction` | 0x0084E89F |
| `Burn_SQ01_SilasEugeneFaction` | 0x0084B618 |
| `BURN_SQ02_ThugFaction` | 0x00847312 |

### Key Observation
Ohio/Burning Springs operates on a **quest-state faction model** (combat allegiances set by quest stages) rather than Wastelanders' numeric reputation grind. The `BURN_AthensProtectronFaction` and `BURN_AthensGhoulFaction` both have condition checks on ActorValue `0x7A767C >= 0x7A7689`, suggesting a progression-gated faction unlocking mechanic.

---

## 9. Atlantic City Faction Relationships (Showmen, Munis, Mobsters)

Atlantic City uses an expedition-based faction system (XPD_AC prefix) with three competing factions. Like Ohio, this does NOT use the Wastelanders reputation ActorValue system.

### Three AC Factions

**The Showmen (entertainment/casino faction):**
| Faction | FormID | Purpose |
|---|---|---|
| `ShowmenGenericFaction_XPD_AC` | 0x006CC15D | Generic Showmen NPCs |
| `ShowmenFriendlyFaction_XPD_AC` | 0x006F0CF6 | Player-friendly Showmen |
| `ShowmenCombatantFaction_XPD_AC` | 0x006D344D | Showmen combat faction |
| `XPD_AC_Showmen_ExpeditionVendorFaction` | 0x0072EBC7 | Showmen vendor |

**The Municipal Auditors (Munis - bureaucratic faction):**
| Faction | FormID | Purpose |
|---|---|---|
| `MunicipalWorkerFaction_XPD_AC` | 0x006CC10B | Muni workers |
| `MunicipalAuditorFriendlyFaction_XPD_AC` | 0x006F0CF8 | Player-friendly Munis |
| `MunicipalAuditorCombatantFaction_XPD_AC` | 0x006D344C | Muni combat faction |
| `XPD_AC_Muni_ExpeditionVendorFaction` | 0x0072EBC8 | Muni vendor |

**The Mobsters (Lombardi crime family):**
| Faction | FormID | Purpose |
|---|---|---|
| `MobsterFriendlyFaction_XPD_AC` | 0x006F0CF7 | Player-friendly Mobsters |
| `MobsterCombatantFaction_XPD_AC` | 0x006BAAF6 | Mobster combat faction |
| `MobsterAllyFaction_XPD_AC` | 0x006D9052 | Mobster ally faction |
| `XPD_AC_Mobster_ExpeditionVendorFaction` | 0x0072EBC9 | Mobster vendor |
| `XPD_AC01_MobsterCarryandThrow_Faction` | 0x0073E2ED | Mobster carry/throw combat |

### AC Quest Factions
| Faction | FormID | Purpose |
|---|---|---|
| `AC_MQ01_Opportunity_AllyFaction` | 0x006C2D1C | MQ01 ally faction |
| `AC_MQ01_Opportunity_EnemyFaction` | 0x006C2D1D | MQ01 enemy faction |
| `AC_MQ04_PlayerAllyFaction` | 0x007347BF | MQ04 player ally |
| `CivilianGenericFaction_XPD_AC` | 0x006B1BE5 | AC civilians |
| `CivilianCompetitorFaction_XPD_AC` | 0x006D1DBF | Civilian competitors |
| `ClownFaction_XPD_AC` | 0x006F4576 | Clown enemies |

### AC Anti-Cheat System
| Faction | FormID |
|---|---|
| `XPD_AC01_AntiCheatSystem` | 0x006C35A4 |
| `XPD_AC01_CheaterFaction` | 0x006C35A5 |

These factions are used in the casino game system -- NPCs caught cheating get added to the CheaterFaction.

### AC Taxman System
| Faction | FormID |
|---|---|
| `XPD_AC01_TaxmanFaction_Tax` | 0x006DE9C0 |
| `XPD_AC01_PlayerFaction_tax` | 0x006BEE44 |
| `XPD_AC01_EnemyFaction_Tax` | 0x006BBFF1 |
| `XPD_AC01_EnemyFaction_Tax_Buttercup` | 0x007399D4 |

The Taxman represents a combat encounter system within AC expeditions.

### AC Faction Relationship Scripting
The DLC01 faction relation scripts handle AC's complex multi-faction setup:
- `DLC01ManyToManyFactionRelationScript` — sets all factions in arrays as mutual Allies/Friends/Enemies/Neutral
- `DLC01OneToManyFactionRelationScript` — sets one faction's relationship to multiple others
- `DLC01PlayerFactionRelationScript` — sets PlayerFaction relationships to AC factions dynamically

---

## 10. Brotherhood of Steel Faction Mechanics

### No Rahmani vs Shin Reputation System
Despite the Rahmani/Shin choice being a major story beat, there is **no numeric reputation ActorValue for either**. The BoS questline uses:

**Valdez Relationship (BS01 - Steel Dawn):**
| Global | FormID | Purpose |
|---|---|---|
| `BS01_MQ02_Invention_ValdezRep_UpsetThreshold` | 0x005C9040 | Threshold for Valdez being upset |
| `BS01_MQ02_Invention_ValdezRep_EcstaticTheshold` | 0x005C9041 | Threshold for Valdez being ecstatic |
| `BS01_MQ02_Invention_ValdezRep_RaiseLarge_Global` | 0x005C6CC8 | Large positive Valdez rep |
| `BS01_MQ02_Invention_ValdezRep_RaiseSmall_Global` | 0x005C6CC7 | Small positive Valdez rep |
| `BS01_MQ02_Invention_ValdezRep_LowerSmall_Global` | 0x005C6CC5 | Small negative Valdez rep |
| `BS01_MQ02_Invention_ValdezRep_LowerLarge_Global` | 0x005C6CC6 | Large negative Valdez rep |

This is a **quest-local disposition system** (like FO4's companion affinity), not a persistent faction reputation. It only affects Valdez's reactions during the Invention quest.

### BoS Faction Hierarchy
| Faction | FormID | Notes |
|---|---|---|
| `BrotherhoodofSteelFaction` | 0x0005DE41 | Main BoS faction (condition-gated) |
| `BS02_HellcatMercenariesFaction` | 0x005FAC47 | Hellcat mercenaries (Steel Reign) |
| `BS01_MQ07_Over_AllyFaction` | 0x005EAC6D | BoS finale ally |
| `BS01_MQ07_Over_EnemyFaction` | 0x005D99ED | BoS finale enemy |
| `BS01_MQ05_Raiders_AllyFaction` | 0x005DB23C | Raiders allied during BoS quest |
| `BS01_MQ05_Raiders_EnemyFaction` | 0x005DB23D | Raiders hostile during BoS quest |
| `BS02_MQ05_Catalyst_BrotherhoodEnemyFaction` | 0x00603BE3 | BoS enemies in Catalyst quest |
| `BS02_MQ01_Penance_AllyFaction` | 0x00603AA2 | Penance quest allies |
| `BS02_MQ01_Penance_EnemyFaction` | 0x00603AA1 | Penance quest enemies |
| `BS02_MQ04_ValdezFollowerFaction` | 0x00616037 | Valdez following player |

---

## 11. Hidden Mechanics and Bonuses

### Damage Forgiveness Above Neutral
The `ReputationTierAboveNeutral_Global` in `ReputationFactionDatum` enables **damage forgiveness** when the player is above Neutral reputation. This means faction NPCs are more tolerant of accidental hits at higher rep tiers -- a hidden mechanic not documented in-game.

### Hostile Tier Floor Protection
The `AllowFactionHostileTier_AV` system prevents casual players from ever reaching Hostile. By default, `AllowFactionHostileTier_AV <= 0`, meaning reputation bottoms out at Cautious. Only specific main quest choices (like the Vault 79 gold heist betrayal) set `AllowFactionHostileTier_AV > 0`, enabling the Hostile tier.

### Denizen Dialogue Reputation Checks
`DenizenDialogueScript` shows that random settler/raider NPCs ("denizens") change their dialogue based on:
- `Rep_Tier_Foundation_2_Neutral` — settlers become conversational
- `Rep_Tier_Foundation_4_Friendly` — settlers offer more
- `Rep_Tier_Crater_2_Neutral` — raiders stop being hostile
- `Rep_Tier_Crater_4_Friendly` — raiders share info
- `PlayersFactionRepDV` — conditional variable tracking which faction views player more favorably

### PlayerTransferFactionsScript
This script (`PlayerTransferFactionsScript`) automatically adds players to faction membership based on ActorValue checks or quest completion flags. This means some faction memberships are INVISIBLE -- players get silently added to factions when they hit certain thresholds, affecting NPC behavior without any notification.

### Cooperative Tier (Hidden)
The "Cooperative" tier (Tier 3) between Neutral and Friendly exists in the data but is not shown on the in-game reputation bar. This creates a hidden sub-tier where specific dialogue or vendor options may unlock before the visible "Friendly" indicator appears.

### Caravan Escort Reputation
`TIF_MILE_CaravanEscort_00769d25` shows that Caravan Escort expeditions award reputation via `ReputationAV` and `RepChangeGlobal` -- a less-documented reputation source outside the standard daily system.

### Vault 63 Reputation System (Skyline Valley)
Vault 63 has a COMPLETE parallel reputation system with all 7 tiers, its own `AllowHostileTier` gate, and likely its own vendor/content gating -- structurally identical to Crater/Foundation but for the Vault 63 dweller factions:
- `Storm_Vault63ScientistFaction` (0x0075E0A6)
- `Storm_Vault63DwellerFaction` (0x0075E0A7)
- `Storm_Vault63SecurityFaction` (0x0075E0A9)
- `Storm_Vault63DoctorFaction` (0x0075E0A9)
- `Storm_Vault63SecretaryFaction` (0x0075E0A8)
- `Storm_LostFaction` (0x006B3C32) — The Lost (hostile ghoul faction)
- `StormCultistFaction` (0x006EE8FC) — Storm cultists

Point Repose faction (`GHL_PointReposeFaction`, 0x007AD0B6) also has condition checks matching the Vault 63 reputation system pattern.

---

## 12. Complete Faction Census

### Total FACT Records: 935

### Faction Categories by Count
| Category | Approximate Count | Notes |
|---|---|---|
| Workshop Crime Factions | ~70 | WorkshopCrimeFaction01-70 (one per workshop) |
| Vendor Factions | ~120+ | Station vendors, Whitespring, gold vendors, expedition vendors |
| Combat/Event Factions | ~200+ | Per-quest/event temporary factions |
| Creature Factions | ~60+ | Per-species combat factions |
| Named NPC Factions | ~50+ | Per-character dialogue/behavior factions |
| Location Factions | ~80+ | Per-location crime/ownership factions |
| DLC Legacy Factions | ~40+ | FO4 DLC factions still in records |
| Ohio/Burn Factions | ~25 | Burning Springs content |
| Atlantic City Factions | ~25 | AC expedition content |
| Storm/Vault 63 Factions | ~20 | Skyline Valley content |
| Core Reputation Factions | 6 | Crater, Foundation, Vault 63 (rep + allow hostile) |

### Faction Relationship Data
The ESM contains **3,087 XNAM (faction relationship) records** across all 935 factions, defining the combat relationship matrix. Only **2 factions have RNAM** (rank) data -- the `RSVP00_Faction_RespondersVolunteers` (ranks 0 and 1) -- one of the only factions with explicit internal ranks.

---

## Summary of Key Findings

1. **Three full reputation systems exist:** Crater, Foundation, and Vault 63 -- all with 7 tiers (including hidden "Cooperative")
2. **Ohio and Atlantic City do NOT have reputation systems** -- they use quest-state faction combat allegiances
3. **Brotherhood has no reputation** -- only a quest-local Valdez disposition system
4. **Hostile tier is gated** -- most players can never reach Hostile unless specific quest choices unlock it
5. **Damage forgiveness** is a hidden perk above Neutral tier
6. **Sol at the Wayward** is a paid reputation fixer with 4 pricing tiers
7. **Gold vendor economy** has 13 pricing tiers, suggesting much more granular price scaling than the visible 6 reputation ranks
8. **The Cooperative tier** (between Neutral and Friendly) is hidden from the UI but functional in game data
9. **5 Whitespring vendor factions were cut** -- suggesting a planned faction-aligned shopping district that was scrapped
10. **Murder protection keyword** prevents quest NPCs from causing rep damage when killed in scripted encounters
