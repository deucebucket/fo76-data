# Fallout 76 Economy Model - Complete Extraction from Game Data

**Source files:** Curve tables from `tempest_data/misc/curvetables/json/`, GLOB records and GMST values from `esm_dump/`

---

## 1. Vendor Buy/Sell Price Formulas

### Charisma-Based Barter Curves

The game uses two curve tables indexed by Charisma (x-axis) to determine price multipliers.

**Buying from vendors** (`chr_barterbuycurve.json`) - multiplier on base price:

| Charisma | Buy Multiplier |
|----------|---------------|
| 1 | 2.50x |
| 15 | 2.00x |
| 30 | 1.75x |
| 60 | 1.60x |
| 100 | 1.50x |

**Selling to vendors** (`chr_bartersellcurve.json`) - fraction of base price received:

| Charisma | Sell Multiplier |
|----------|----------------|
| 1 | 0.10x (10%) |
| 15 | 0.18x (18%) |
| 30 | 0.25x (25%) |
| 60 | 0.28x (28%) |
| 100 | 0.30x (30%) |

### GMST Caps on Barter

- `fBarterBuyMax` = **0.75** -- Maximum fraction of base value when buying (caps how low buy price can go)
- `fBarterSellMax` = **0.50** -- Maximum fraction of base value when selling (caps how high sell price can go)
- `fBarterMin` = **2.00** -- Minimum barter value floor
- `fVendorIncomeMult` = **0.25** -- Vendor income multiplier (vendors earn 25% of what you spend)

### Item Condition Value Multiplier (`itemconditionvaluemultiplier.json`)

Damaged items sell for less. Condition (x, as %) maps to value fraction (y):

| Condition % | Value Multiplier |
|-------------|-----------------|
| 0 | 0.00 |
| 1 | 0.15 |
| 5 | 0.28 |
| 10 | 0.35 |
| 20 | 0.44 |
| 30 | 0.50 |
| 50 | 0.61 |
| 70 | 0.70 |
| 85 | 0.75 |
| 100 | 0.81 |
| 200 | 0.81 (cap) |

**Note::** Even at 100% condition, an item's sell value is only 81% of its nominal base value. This is a hidden 19% tax that stacks with the Charisma sell curve.

### Effective Price Formula

```
Buy Price = BaseValue * BarterBuyCurve(CHA) * ConditionMult(condition%)
Sell Price = BaseValue * BarterSellCurve(CHA) * ConditionMult(condition%)
```

At CHA 15 (typical with perks/chems): you buy at 2.0x and sell at 0.18x.
At CHA 30 (Hard Bargain + buffs): you buy at 1.75x and sell at 0.25x.

**Spread at CHA 15:** Buy at 200% / Sell at 18% = **11.1x markup spread**
**Spread at CHA 30:** Buy at 175% / Sell at 25% = **7.0x markup spread**

### Comparison with Community Knowledge

Wiki typically says Hard Bargain rank 3 gives "25% better prices." The data confirms CHA 30 sells at 0.25x vs CHA 1 at 0.10x, which is a 150% improvement in sell price, not 25%. The perk likely adds a flat CHA equivalent, shifting position on the curve. The "25% better prices" shorthand likely refers to the combined effect of 3 ranks of Hard Bargain adding effective Charisma points.

---

## 2. Cap Stash Contents and Probabilities

### Container Loot Probability System (`econ/containers/`)

Containers use "chance none" curves where x = player level and y = percentage chance the slot is EMPTY.

**Primary item slot** (`containers_chancenone.json`):

| Player Level | Chance Empty |
|-------------|-------------|
| 1 | 75% |
| 5 | 50% |
| 10 | 35% |
| 15 | 25% |
| 20 | 20% |
| 25 | 15% |
| 30 | 10% |
| 50+ | 10% |

**Second item slot** (`containers_item2_chancenone.json`):

| Player Level | Chance Empty |
|-------------|-------------|
| 1 | 95% |
| 10 | 80% |
| 20 | 50% |
| 30 | 25% |
| 100 | 0% |

**Third item slot** (`containers_item3_chancenone.json`):

| Player Level | Chance Empty |
|-------------|-------------|
| 1 | 97% |
| 10 | 90% |
| 20 | 65% |
| 30 | 40% |
| 100 | 0% |

**Max cap count per container** (`containers_maxcount.json`):

| Player Level | Max Caps |
|-------------|----------|
| 1 | 1 |
| 5 | 1 |
| 10 | 2 |
| 15 | 2 |
| 20 | 3 |
| 25 | 4 |
| 30 | 6 |
| 40 | 7 |
| 100 | 10 |

**Recipe drops** (`containers_recipe_chancenone.json`):

| Player Level | Chance NO Recipe |
|-------------|-----------------|
| 1 | 99% |
| 10 | 95% |
| 20 | 80% |
| 30 | 50% |
| 100 | 0% |

### Ammo in Containers (`econ/ammo/`)

All ammo types share an identical distribution curve. This is a probability/weight distribution, NOT a count:

| x | y | Interpretation |
|----|-----|---------------|
| 0 | 0 | No ammo at level 0 |
| 1 | 12 | Weight 12 at tier 1 |
| 2 | 90 | Peak probability at tier 2 |
| 3 | 75 | High probability |
| 4 | 50 | Medium |
| 20 | 25 | Low |
| 30 | 5 | Very low |
| 99 | 5 | Minimum |
| 100| 0 | None |

**Ammo chance-none** (`ammo_lpi_chancenone.json`): At level 1, 60% chance of no ammo; at level 25+, only 10% chance of no ammo.

### Rare Item Spawn Probability (`lpi_rare_chancenone.json`)

| Player Level | Chance NO Rare Item |
|-------------|-------------------|
| 1 | 99% |
| 10 | 97% |
| 20 | 90% |
| 25 | 80% |
| 30 | 5% |
| 100 | 0% |

There is a dramatic cliff at level 30 where rare items go from 80% chance empty to only 5%. This is likely the game's intended "endgame loot" threshold.

### Fusion Core Spawns (`lpi_fusioncore_chancenone.json`)

| Tier | Chance Empty |
|------|-------------|
| 0 | 100% |
| 1 | 80% |
| 2 | 25% |

---

## 3. Fast Travel Cost Formula

### Distance-Based Cost (`fasttravelcostcurvedistance.json`)

| Distance (units) | Cap Cost |
|-------------------|----------|
| 1 | 0 |
| 10,000 | 0 |
| 500,000 | 60 |

The curve is linear from 10,000 to 500,000 units. Fast travel is FREE up to 10,000 units distance. Beyond that, the cost scales linearly up to 60 caps maximum.

### Level Multiplier (`fasttravelcostmultcurve.json`)

| Player Level | Multiplier |
|-------------|-----------|
| 1 | 1.0x |
| 100 | 1.0x |

**This is flat at 1.0x.** Player level does NOT affect fast travel cost.

### Overencumbered Multiplier (`fasttraveloverencumberedcostmultcurve.json`)

| Overencumbered Factor | Cost Multiplier |
|-----------------------|----------------|
| 1 | 1x |
| 5 | 100x |

Being overencumbered MASSIVELY increases fast travel cost (when travel perk allows it). The multiplier scales linearly: at 2x overencumbered, cost is ~25.75x; at 3x, ~50.5x; at 5x, 100x.

### GMST Values

- `fFastTravelDelaySeconds` = **15.0** -- 15-second loading delay
- `fFastTravelHungerIncrease` = **0.0** -- No hunger penalty (removed in later updates)
- `fFastTravelThirstIncrease` = **0.0** -- No thirst penalty (removed)
- `fFastTravelItemDegradation` = **0.0** -- No item degradation on fast travel
- `fFastTravelFoodItemDegradation` = **0.0** -- No food degradation on fast travel

### Comparison with Community Knowledge

Wiki says fast travel costs "a few caps based on distance." The data confirms it is purely distance-based, zero up to ~10k units, linear to 60 caps max. The 60-cap maximum is lower than many players assume. The overencumbered penalty is far more severe than documented -- community says "costs more" but the actual multiplier can hit 100x.

---

## 4. Scrip (Legendary Tokens) Values and Limits

### Scrip Values for Scrapping Legendaries (`legendary_scrapvalues_*.json`)

All item categories (armor, power armor, melee weapons, ranged weapons) share IDENTICAL scrip values:

| Stars | Scrip from Scrapping |
|-------|---------------------|
| 1 | 1 |
| 2 | 2 |
| 3 | 4 |
| 4 | 6 |

**CRITICAL DISCREPANCY:** Community wikis report scrip values of 3/9/24/40 for weapons and 3/9/24/30 for armor. Those are the **sell values** (see below), not scrap values. The game data distinguishes between "scrapvalues" (dismantling at workbench, yields legendary modules + scrip) and "sellvalues" (selling to Purveyor/legendary exchange).

### Scrip Values for Selling to Legendary Exchange (`legendary_sellvalues_*.json`)

**Armor:**

| Stars | Scrip Value |
|-------|------------|
| 1 | 3 |
| 2 | 9 |
| 3 | 24 |
| 4 | 30 |

**Power Armor:**

| Stars | Scrip Value |
|-------|------------|
| 1 | 10 |
| 2 | 20 |
| 3 | 45 |
| 4 | 55 |

**Weapons (Melee AND Ranged, identical):**

| Stars | Scrip Value |
|-------|------------|
| 1 | 5 |
| 2 | 15 |
| 3 | 40 |
| 4 | 50 |

### Legendary Crafting Costs

**Legendary Modules** (`cobj_legendary_crafting_module.json`) - modules needed to craft:

| Stars | Modules Required |
|-------|-----------------|
| 1 | 15 |
| 2 | 30 |
| 3 | 60 |
| 4 | 120 |

**Adding a Legendary Slot** (`cobj_legendary_addslot_module.json`):

| Stars | Modules to Add Slot |
|-------|-------------------|
| 1 | 5 |
| 2 | 10 |
| 3 | 15 |
| 4 | 20 |

**Attaching a Legendary Effect -- Scrip Cost** (`cobj_legendary_attach_scrip.json`):

This curve shows escalating scrip costs for repeated re-rolls:

| Roll # | Scrip Cost |
|--------|-----------|
| 1 | 10 |
| 2 | 15 |
| 3 | 25 |
| 4 | 45 |
| 5 | 70 |
| 6 | 100 |
| 7 | 135 |
| 8 | 175 |
| 9 | 220 |
| 10 | 270 |
| 15 | 595 |
| 20 | 1000 |

**Legendary Scrapping -- Scrip Return** (`cobj_legendary_scrap.json`):

| Stars | Scrip from Scrap |
|-------|-----------------|
| 1 | 100 |
| 2 | 200 |
| 3 | 300 |
| 4 | 400 |

Wait -- this contradicts the scrapvalues curves. The `cobj_legendary_scrap.json` likely represents the COBJ recipe scrip cost/return for the "Scrap Legendary" option at the crafting bench, distinct from the AVIF-based values above. The much higher values (100/200/300/400) suggest this is the constructible object recipe yield.

### Scrip Rewards from Activities

- `Econ_Systemic_Scrip_ChanceNone` = **10%** -- 10% chance of no scrip from systemic sources
- `RA_Rewards_Activities_Caps` = **75** -- Daily activities reward 75 caps
- `RA_Rewards_PublicEvents_Caps` = **150** -- Public events reward 150 caps
- `W05_Daily_Reward_LegendaryToken` = **8** -- Wastelanders daily: 8 scrip
- `COMP_RQ_Reward_LegendaryTokens` = **5** -- Companion quest reward: 5 scrip
- `ScripVaultSystemRewards_V94_Standard` = **5** -- Standard vault reward: 5 scrip
- `ScripVaultSystemRewards_V94_Expert` = **10** -- Expert vault reward: 10 scrip
- `LegendaryTokens_MQ_Overseer_Reward` = **100** -- Overseer quest completion: 100 scrip
- `LegendaryToken_Daily_Fishing` = value exists (fishing daily)

### Daily Scrip Limit

The daily scrip limit is NOT directly stored as a curve table or GLOB -- it is likely hardcoded or stored in server-side configuration. Community consensus is **300 scrip/day** at the exchange machine. The data files don't contain an explicit "daily_scrip_limit" value, which suggests it's a server-side cap.

---

## 5. Gold Bullion Daily/Weekly Limits

### Treasury Note Exchange Rates (from GLOBs)

Treasury notes earned per event/quest by difficulty:

| Difficulty | Treasury Notes |
|---------------|---------------|
| Easy | 2 |
| Medium | 3 |
| Hard | 4 |
| Very Hard | 8 |

- `Gold_Treasury_Note_Loot_Enabled` = **1.0** -- Treasury note drops are active
- `Gold_Treasury_Note_QuestReward_Easy` = **2**
- `Gold_Treasury_Note_QuestReward_Medium` = **3**
- `Gold_Treasury_Note_QuestReward_Hard` = **4**
- `Gold_Treasury_Note_QuestReward_VeryHard` = **8**

### Gold Bullion Reward Amounts

- `GoldBullion_RewardAmountEasy` = **2** gold per easy quest
- `GoldBullion_RewardAmountMedium` = **3** gold per medium quest
- `GoldBullion_RewardAmountHard` = **4** gold per hard quest
- `GoldBullion_RewardAmountMax` = **10** gold maximum per quest

### Gold Vendor Factions

Each faction has its own gold bullion balance tracked separately:
- `Vendor_GoldBullionBalance_Settler_Faction`
- `Vendor_GoldBullionBalance_Raider_Faction`
- `Vendor_GoldBullionBalance_SecretService_Faction`

Gold vendor reset days = **3 days** for both Settlers and Raiders.

### Daily Gold Limit

Like scrip, the daily gold exchange limit (200 gold/day from the machine, 300 treasury notes max carried) is server-side. The curve tables contain the reward amounts but not the daily cap.

---

## 6. Treasury Note Exchange Rates

From the GLOB data, treasury notes convert to gold bullion at the Wayward gold press machine:

- Exchange rate: **1 Treasury Note = variable gold** (community says 10 gold per note)
- Daily exchange limit: **20 notes/day = 200 gold/day** (server-side, not in curve data)
- The `Gold_Treasury_Note_Loot_Enabled` flag = 1.0 confirms the system is active

### Note Earning Rates

| Source | Notes Earned |
|---------------------------|-------------|
| Easy public event | 2 |
| Medium public event | 3 |
| Hard public event | 4 |
| Very Hard public event | 8 |
| Daily Ops (Standard) | 5 scrip (not notes) |

---

## 7. Crafting Material Costs

### Cost Curve System

The COBJ system uses curve tables where x = "tier" or "complexity level" of the recipe and y = material count required. Each material has its own curve per crafting category.

### Ammo Crafting Materials

Ammo materials scale 1:1 linearly. For tier N, you need N of each required material:
- `cobj_ammo_lead.json`: tier 1 = 1 lead, tier 10 = 10, tier 50 = 50
- `cobj_ammo_plastic.json`: same 1:1 linear
- `cobj_ammo_copper.json`: same 1:1 linear

### Weapon Mod Materials

Weapon mods use a ~0.5x scaling rate (roughly half the tier value):
- `cobj_weapon_adhesive.json`: tier 1 = 1, tier 5 = 3, tier 10 = 5, tier 20 = 10, tier 50 = 25
- `cobj_weapon_screws.json`: tier 1 = 1, tier 5 = 4, tier 10 = 7, tier 20 = 14, tier 50 = 35

Screws scale slightly higher than adhesive (0.7x vs 0.5x), reflecting their greater rarity.

### Armor Mod Materials

Armor mods use a lower scaling rate than weapons (~0.44x):
- `cobj_armor_adhesive.json`: tier 1 = 1, tier 5 = 2, tier 10 = 4, tier 20 = 9, tier 50 = 22
- `cobj_armor_screws.json`: tier 1 = 1, tier 5 = 3, tier 10 = 6, tier 20 = 12, tier 50 = 31

### Workshop/CAMP Building Materials

Workshop materials also scale 1:1 linearly, same as ammo.

### Power Armor Crafting

PA uses a tiered system where x encodes both PA type (10-15=Raider, 20-25=T-45, 30-35=T-51, 40-45=T-60, 50-55=X-01/Ultracite) and mod complexity (offset within each tier):

**Component costs by rarity class and PA type (using Raider/T-45 tier as example):**

| Material Rarity | Base (mod 0) | +1 | +2 | +3 | +4 | +5 |
|-----------------|-------------|-----|-----|-----|-----|-----|
| Super Common | 9 | 13 | 16 | 19 | 22 | 25 |
| Common | 7 | 12 | 14 | 16 | 18 | 20 |
| Uncommon | 5 | 9 | 11 | 13 | 15 | 17 |
| Rare | 4 | 6 | 8 | 10 | 12 | 14 |
| Very Rare | 3 | 5 | 6 | 7 | 8 | 9 |

All PA types share identical costs for the same rarity tier -- there's no cost difference between modding Raider vs X-01 in terms of material counts.

### Smelting Costs

| Tier | Ore Required | Acid Required |
|------|-------------|--------------|
| 10 | 3 | 2 |
| 20 | 3 | 2 |
| 30 | 3 | 3 |
| 40 | 5 | 4 |
| 50 | 7 | 5 |

### Flux Stabilization (Nuked Flora)

To stabilize raw flux into stable flux:
- **10 raw flux** of the specific type (fixed, from `nukeflora_flux_required`)
- **1 glowing mass** (fixed)
- **1 hardened mass** (fixed)
- **1 high-radiation fluids** (fixed)

All five flux colors (cobalt/crimson/fluorescent/violet/yellowcake) have identical costs. The raw flora types map 1:1 to their respective colors.

### Brewing Costs (by recipe tier 1/2/3)

| Ingredient Type | Tier 1 | Tier 2 | Tier 3 |
|-------------------|--------|--------|--------|
| Primary Ingredient| 2 | 3 | 3 |
| Water | 2 | 3 | 3 |
| Wood | 2 | 5 | 5 |
| Flavor Ingredient | 1 | 2 | 2 |
| Rare Ingredient | 1 | 1 | 1 |

### Intelligence Crafting Bonuses

**Scrap bonus from INT** (`scrapbonusint.json`):

| INT | Scrap Multiplier |
|-----|-----------------|
| 1 | 0.75x |
| 3 | 1.00x (baseline)|
| 5 | 1.10x |
| 10 | 1.20x |
| 15 | 1.25x |
| 20 | 1.30x |
| 25 | 1.325x |

At INT 1, you get 25% LESS scrap. At INT 15+, you get 25-33% MORE scrap.

**INT condition bonus** (`intconditionbonus.json`): Items crafted at INT 20+ are at 100% condition. Below INT 20, crafted item condition scales linearly from 0% at INT 1.

---

## 8. Ammo Crafting Yields

The ammo crafting system uses the same linear 1:1 curves for all materials. The actual yield per craft depends on the specific recipe (defined in COBJ records, not curve tables). The curve tables only define material costs.

### Ammo-O-Matic Production Rates (CAMP item)

The Ammo-O-Matic produces ammo passively. Production interval in hours per round:

| Ammo Type | Hours/Round | Rounds/Hour |
|-------------|-------------|-------------|
| .308 | 0.000600 | 1,667 |
| 10mm | 0.003600 | 278 |
| .44 | 0.001600 | 625 |
| .45 | 0.001300 | 769 |
| 5.56 | 0.004800 | 208 |
| Shotgun | 0.003500 | 286 |

**Observation:** .308 ammo produces 6x faster than 5.56 in the Ammo-O-Matic, which contradicts the common player assumption that all ammo produces at equal rates. 5.56 is actually the SLOWEST ammo to produce passively, yet is among the most demanded.

---

## 9. Repair Costs Formula

### GMST Repair Values

- `fWorkshopRepairComponentMult` = **0.25** -- Repairs cost 25% of the item's original crafting materials
- `fProportionalRepairModifier` = **0.60** -- Proportional repair modifier (60% efficiency)
- `fRepairPatchConditionPercent` = **0.10** -- Repair kits restore 10% condition (Improved kits restore more)

### Item Condition Degradation Rates

**Ballistic weapons** (`conditiondamagescalefactor_weapons_ballistic.json`):

| Level | Condition Loss/Shot |
|-------|-------------------|
| 1 | 0.015 |
| 15 | 0.012 |
| 30 | 0.010 |
| 50 | 0.007 |

Higher-level weapons degrade slower. A level 50 ballistic weapon loses condition 53% slower than a level 1.

**Weapon durability ranges** (level-scaled):

| Level | Min Durability | Max Durability |
|-------|---------------|---------------|
| 1 | 30 | 45 |
| 25 | 50 | 65 |
| 50 | 70 | 85 |

### Repair Cost Formula

```
Repair Cost = OriginalCraftingComponents * fWorkshopRepairComponentMult * (1 - CurrentCondition%)
 = OriginalCraftingComponents * 0.25 * ConditionDeficit
```

A weapon at 50% condition costs 12.5% of its original materials to repair.
A weapon at 0% condition costs the full 25% of its original materials.

**Comparison with wiki:** Community says "repair costs 25% of crafting materials." This is correct only at 0% condition. At partial damage, the cost is proportionally less.

---

## 10. CAMP Budget Costs Per Category

### GMST Budget Values

| Category | Budget Cost Per Unit |
|------------|---------------------|
| Light | 1.0 |
| Spline | 0.25 |
| Actor (NPC)| 9.0 |
| Container | 0.0 (free!) |
| Navmesh | 2.0 |

**Note::** Containers cost ZERO budget. This explains why players can place unlimited stash boxes. Actors (allies, collectrons) cost 9x a standard object, explaining why you can only place a few.

### CAMP Placement Costs

**Move CAMP cost** (`movecampcostcurve.json`):

| Player Level | Move Cost (caps) |
|-------------|-----------------|
| 1-5 | 5 |
| 50 | 40 |

Linear scaling from level 5 to 50.

**Quick Camp Move:** `uQuickCampMoveCost` = **0** (free instant camp moves added in later update)

**Move Penalty:** `fMoveCampCostPenaltyDurationInSeconds` = **600** (10 minutes), `fMoveCampCostPenaltyMultiplier` = **1.0** (no additional penalty multiplier)

### Workshop Claim Cost (`workshopclaimcost.json`)

| Player Level | Claim Cost (caps) |
|-------------|------------------|
| 0 | 25 |
| 1000 (?) XP | 50 |
| 3000 (?) XP | 100 |

This likely indexes on some progression metric rather than raw level.

### Camp Kit System

- `uMaxCampKits` = **2** -- Can carry 2 camp kits
- `fCampKitRegenTimeInMinutes` = **60** -- Camp kits regenerate every 60 minutes

---

## 11. Vendor Cap Pool Refresh Rate

### Vendor Reset Schedule (from GLOBs)

ALL vendor factions share a **3-day reset cycle**:

| Vendor Faction | Reset Days |
|------------------------|-----------|
| Enclave | 3 |
| Brotherhood of Steel | 3 |
| Raiders | 3 |
| Free States | 3 |
| Settlers | 3 |
| Whitesprings | 3 |
| Vault 63 | 3 |
| Shared Pool | 3 |
| Vending Machine | 3 |
| RE (Random Encounter) | 3 |
| Pioneer Scout (Tadpole)| 3 |
| Pioneer Scout (Possum) | 3 |
| Visitor Vendor | 3 |
| LGV01 | 3 |
| Raiders Gold Vendor | 3 |
| Settlers Gold Vendor | 3 |
| Showmen (Burning Springs)| tracked |
| Muni (Burning Springs) | tracked |
| Mobster (Burning Springs)| tracked |
| None | 0 |

**Vendor Balance Tracking:** Each faction has a `Vendor_CapsBalance_*` Actor Value (AVIF) that tracks remaining caps. When depleted, they won't buy until reset.

### Vendor Income Recovery

`fVendorIncomeMult` = **0.25** -- Vendors recover 25% of caps spent by players buying from them. If you buy 100 caps worth of items, the vendor gains 25 caps toward their pool.

### Stash Expansion System

**Stash weight increase** (`stash_weight_add.json`):

| Tier | Added Weight |
|------|-------------|
| 1 | 10 |
| 2 | 20 |
| 3 | 30 |
| 4 | 40 |
| 5 | 50 |
| 6 | 60 |
| 7 | 80 |
| 8 | 90 |

**Stash expansion cost** (`stash_cost_caps.json`):

| Tier | Cap Cost |
|------|---------|
| 1 | 100 |
| 2 | 200 |
| 3 | 300 |
| 4 | 400 |
| 5 | 500 |
| 6 | 600 |
| 7 | 700 |
| 8 | 800 |
| 50 | 5,000 |

### CAMP Resource Production Intervals

**Counterfeit Bottle Cap Press:** `ATX_ResourceProductionIntervalHours_CounterfeitBottleCapPress_resource` = **0.17 hours** (10.2 minutes per cap)

**Collectron Production:** 0.15 hours (9 minutes per item)

---

## 12. Player Death Caps Loss (`playerdeathcapsloss.json`)

| Player Level | % Caps Lost on Death |
|-------------|---------------------|
| 1-20 | 1% |
| 21-40 | 2% |
| 41-50 | 3% |

**Comparison with community knowledge:** Wiki says "you drop some caps on death." The actual data shows a very modest 1-3% loss that many players overestimate. At level 50 with 40,000 caps, you lose only 1,200 caps.

---

## 13. Large Creature Component Drops

Large creatures (Scorchbeasts, Behemoths, etc.) drop materials based on a tiered curve. Example for screws:

| Tier | Count |
|------|-------|
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |
| 4 | 5 |
| 5 | 6 |
| 6 | 7 |
| 7 | 1 (reset) |

The curve resets at tier 7, suggesting a cycling drop table. Ultracite drops follow a similar pattern but reset at tier 5.

---

## 14. Lucky Strike Repeatable Rewards

| Tier | Cap Reward |
|------|-----------|
| 1 | 75 |
| 2 | 150 |
| 3 | 225 |

---

## Summary of Key Discrepancies vs Community Documentation

1. **Item condition value:** Even 100% condition items are valued at only 81% of base -- a hidden 19% tax not documented on wikis.

2. **Overencumbered fast travel:** The 100x cost multiplier at 5x overweight is far more extreme than community guides suggest.

3. **Legendary scrap vs sell values:** The game has TWO separate value systems. Scrap values (1/2/4/6) are tiny; sell values (3-55) are what wikis report. The COBJ scrap recipe yields (100/200/300/400) are yet a third system.

4. **Ammo-O-Matic production rates:** .308 produces 8x faster than 5.56. Community assumes equal rates.

5. **Container budget = 0:** Stash boxes and containers are genuinely free in CAMP budget, which is confirmed in game data but rarely documented.

6. **Level 30 loot cliff:** Rare item spawn probability drops from 80% empty to 5% empty between level 25 and 30, creating a hidden loot quality breakpoint.

7. **Vendor income recovery:** Vendors regain 25% of what you spend buying from them -- meaning buying from a vendor partially refills their cap pool. This is key to efficient cap farming.

8. **Fast travel cost cap:** Maximum 60 caps regardless of distance. Many community guides overestimate this.

9. **Stash expansion exists in data:** The stash expansion curve (up to tier 50 at 5,000 caps) suggests a planned or active stash expansion system beyond the base 1,200 weight.

10. **PA mod costs are type-agnostic:** Modding Raider PA costs exactly the same materials as modding X-01 at the same complexity tier. The common belief that higher-tier PA costs more to mod is incorrect per the curve data.
