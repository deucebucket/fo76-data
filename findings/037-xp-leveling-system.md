# Fallout 76: Complete XP and Leveling System

> Extracted from game data: ESM dump (game_settings.txt, GLOB_records.txt, PERK_records.txt),
> Tempest curve tables (player/xp/, creatures/xp/, quests/). All values are from actual game
> records, not community estimates.

---

## 1. XP Required Per Level

### The Formula (from GMST records)

| Setting | Value | Purpose |
|---------|-------|---------|
| `iXPBase` | **200** | Base XP for level 1 |
| `iXPBumpBase` | **75** | Additional XP per level |

**Formula: `XP_to_next_level = 200 + ((current_level - 1) * 75)`**

This is a simple linear formula with no cap. It applies identically from level 1 through level 1000+.

### XP Per Level Table

| Level | XP Needed | Cumulative | Level | XP Needed | Cumulative |
|-------|-----------|------------|-------|-----------|------------|
| 1 | 200 | 200 | 30 | 2,375 | 38,625 |
| 2 | 275 | 475 | 35 | 2,750 | 51,625 |
| 3 | 350 | 825 | 40 | 3,125 | 66,500 |
| 4 | 425 | 1,250 | 45 | 3,500 | 83,250 |
| 5 | 500 | 1,750 | 50 | 3,875 | 101,875 |
| 6 | 575 | 2,325 | 75 | 5,750 | 223,125 |
| 7 | 650 | 2,975 | 100 | 7,625 | 391,250 |
| 8 | 725 | 3,700 | 150 | 11,375 | 868,125 |
| 9 | 800 | 4,500 | 200 | 15,125 | 1,532,500 |
| 10 | 875 | 5,375 | 300 | 22,625 | 3,423,750 |
| 15 | 1,250 | 10,875 | 500 | 37,625 | 9,456,250 |
| 20 | 1,625 | 18,250 | 1000 | 75,125 | 37,662,500 |
| 25 | 2,000 | 27,500 | | | |

**Key observations:**
- There is no level cap in the data. The formula scales infinitely.
- No diminishing returns on XP gain per level -- it is purely linear (+75 XP per level).
- Level 50 is significant only because SPECIAL point allocation locks at 50; the XP curve does not change.

---

## 2. Intelligence XP Bonus Formula

### The Definitive Answer (from GMST records)

| Setting | Value |
|---------|-------|
| `fXPModBase` | **1.0** |
| `fXPModMult` | **0.03** |

**Formula: `XP_multiplier = 1.0 + (Intelligence * 0.03)`**

Each point of Intelligence adds **exactly 3% bonus XP**. This is multiplicative against the base XP earned.

### Intelligence XP Multiplier Table

| INT | Multiplier | Bonus | INT | Multiplier | Bonus |
|-----|-----------|-------|-----|-----------|-------|
| 1 | 1.03x | +3% | 20 | 1.60x | +60% |
| 3 | 1.09x | +9% | 25 | 1.75x | +75% |
| 5 | 1.15x | +15% | 30 | 1.90x | +90% |
| 7 | 1.21x | +21% | 35 | 2.05x | +105% |
| 10 | 1.30x | +30% | 40 | 2.20x | +120% |
| 12 | 1.36x | +36% | 50 | 2.50x | +150% |
| 15 | 1.45x | +45% | 100 | 4.00x | +300% |

### Community Debate: Settled

The community has debated whether the bonus is 2% or 3% per INT point. **The game data confirms it is exactly 3% (0.03).** Players who measured ~2.07% were likely testing with a rounding artifact or base-1 confusion (the formula uses `1.0 + INT*0.03`, not `INT*0.03` from zero). At INT 15, you get 1.45x -- not 1.30x as the "2% camp" would predict.

**There is no cap on the INT bonus in the GMST data.** With mutations (Egghead), food buffs, Unyielding armor, and team bonuses, INT can reach 60+ in practice, yielding 2.8x+ XP.

---

## 3. Creature XP Rewards

Creature XP is determined by two systems: a **size category curve** and a **universal tier system**.

### Size Category Curves (linear interpolation, level 1 to 100)

| Category | XP at Lvl 1 | XP at Lvl 100 | Formula (approx) |
|----------|-------------|---------------|-------------------|
| **Boss** | 20 | 500 | `20 + (level-1) * 4.85` |
| **Large** | 15 | 200 | `15 + (level-1) * 1.87` |
| **Medium** | 10 | 125 | `10 + (level-1) * 1.16` |
| **Small** | 5 | 75 | `5 + (level-1) * 0.71` |
| **Critter** | 2 | 40 | `2 + (level-1) * 0.38` |

### Universal Tier System (100 tiers)

The game also uses 100 "universal tiers" that define XP per creature at 50 sample levels (1 through 295, step 6). These tiers provide finer-grained control per creature template. Each creature NPC record references a specific tier.

**XP at creature level 1, by tier (selection):**

| Tier | XP @ Lvl 1 | Tier | XP @ Lvl 1 | Tier | XP @ Lvl 1 |
|------|-----------|------|-----------|------|-----------|
| 1 | 1 | 20 | 89 | 60 | 913 |
| 2 | 2 | 25 | 140 | 70 | 1,367 |
| 5 | 6 | 30 | 203 | 80 | 2,079 |
| 10 | 22 | 40 | 370 | 90 | 3,323 |
| 15 | 50 | 50 | 599 | 100 | 5,719 |

At higher creature levels, these scale proportionally. For example, tier 50 at creature level 295 yields 9,204 XP; tier 100 at creature level 295 yields 87,663 XP.

### Example Creature XP Values (at common enemy levels)

Using the size-category curves:

| Enemy (Size) | Lvl 10 | Lvl 25 | Lvl 50 | Lvl 75 | Lvl 100 |
|--------------|--------|--------|--------|--------|---------|
| Scorchbeast Queen (Boss) | 64 | 137 | 258 | 379 | 500 |
| Deathclaw (Large) | 32 | 60 | 107 | 154 | 200 |
| Super Mutant (Medium) | 20 | 38 | 67 | 96 | 125 |
| Ghoul (Small) | 11 | 22 | 40 | 57 | 75 |
| Radroach (Critter) | 5 | 11 | 21 | 31 | 40 |

*Note: These are base values before Intelligence multiplier.*

---

## 4. Quest XP Rewards

### Quest XP Multiplier Curve (`chr_questxpcurve`)

Quests use a difficulty tier (x = 1 to 25) that scales the quest's base XP reward:

| Quest Tier | Multiplier | Quest Tier | Multiplier |
|-----------|-----------|-----------|-----------|
| 1 | 1.00x | 10 | 1.45x |
| 2 | 1.05x | 20 | 1.95x |
| 3 | 1.10x | 25 | 2.20x |
| 7 | 1.30x | | |

The quest caps curve (`chr_questcapscurve`) uses the same multipliers for caps rewards.

### Specific Quest XP Rewards (from GLOB records)

**Main Quests:**

| Quest | XP Reward |
|-------|-----------|
| Overseer's Final Quest | 1,600 |
| Wastelanders Main Quests (MQ01-MQ08) | 1,000 each |
| Wastelanders Finale (MQA_206P) | 2,000 |
| Steel Dawn Main Quests | 1,000 each |
| Steel Reign Catalyst (MQ05) | 1,000 |
| Expeditions Main Quest | 1,200 |
| Expeditions Finale | 1,500 |
| Skyline Valley Main Quest | 1,200 |
| Milepost Zero Intro | 500 |
| The Backwoods Main Quests | 800-1,600 |

**Daily Quests (selection):**

| Daily | XP |
|-------|-----|
| Foundation Dailies | 700 |
| Forest Region (FFz13) | 300 |
| Toxic Valley (TWz03, TWz11) | 400-500 |
| Savage Divide (SFz03, SFz04) | 700-900 |
| Cranberry Bog (CBz03) | 600 |
| BoS Daily (BoSz04) | 800 |
| Photo Daily | 700 |
| Fishing Daily | 500 |

**Event XP Reward Tiers (from standardized globals):**

| Event Size | XP Reward |
|-----------|-----------|
| Small | 100 |
| Medium | 250 |
| Large | 500 |
| Very Large | 1,000 |

**Expedition Mission XP by Completion Tier:**

| Tier | XP | Stamps |
|------|-----|--------|
| Tier 0 (min) | 3,000 | 2-3 |
| Tier 1 | 3,500 | 5 |
| Tier 2 | 4,000 | 6-10 |
| Tier 3 (max) | 5,000 | 8-15 |
| Team Leader Bonus | 1,000 | -- |

**Seasonal/Recurring Event XP:**

| Event | XP |
|-------|-----|
| Seasonal Events Min | 150 |
| Seasonal Events Mid | 300 |
| Seasonal Events Max | 500 |
| Mutated Events | 500 |
| Moonshine Jamboree Reward | 200 |
| Meat BBQ (perfect) | 500 |
| Meat BBQ (normal) | 300 |
| Eviction Notice | 1,000 |

**Raid Content (Ultracite/Endgame):**

| Content | XP |
|---------|-----|
| RD01 Encounter 01 | 5,000 |
| RD01 Encounter 02 | 15,000 |
| RD01 Encounter 03 | 20,000 |
| RD01 Encounter 04 | 25,000 |
| RD01 Encounter 05 | 30,000 |

---

## 5. XP from Non-Combat Activities

### Lockpicking (from GMST records)

| Difficulty | XP Reward |
|-----------|-----------|
| Easy (Level 0) | 5 |
| Average (Level 1) | 10 |
| Hard (Level 2) | 15 |
| Very Hard (Level 3) | 20 |

### Hacking

Hacking terminals grants XP through the speech challenge system:

| Difficulty | XP (GMST) |
|-----------|-----------|
| Easy | 15 (`fAVDCharismaXPEasy`) |
| Medium | 20 (`fAVDCharismaXPMedium`) |
| Hard | 25 (`fAVDCharismaXPHard`) |

### Location Discovery (from GMST records)

| Discovery Type | XP Reward |
|---------------|-----------|
| Map Marker Discovery (`iXPRewardDiscoverMapMarker`) | 20 |
| Secret Area Discovery (`iXPRewardDiscoverSecretArea`) | 20 |

### Trap Disarming

| Activity | XP Reward |
|----------|-----------|
| Mine/Trap Disarm (`iMineDisarmExperience`) | 5 |

---

## 6. Crafting, Cooking, Building, and Scrapping XP

### Workbench Crafting (Weapons/Armor)

| Setting | Value |
|---------|-------|
| `fWorkbenchExperienceBase` | 2.0 |
| `fWorkbenchExperienceMult` | 0.03 |
| `fWorkbenchExperienceMax` | 50.0 |

**Formula: `XP = min(fWorkbenchExperienceBase + (item_value * fWorkbenchExperienceMult), fWorkbenchExperienceMax)`**

Crafting XP scales with item value, capped at 50 XP per craft.

### Cooking

| Setting | Value |
|---------|-------|
| `fCookingExpBase` | 1.0 |
| `fCookingExpMult` | 0.15 |
| `fCookingExpMax` | 10.0 |

**Formula: `XP = min(fCookingExpBase + (item_value * fCookingExpMult), fCookingExpMax)`**

Cooking XP is capped at 10 per item.

### CAMP Building (Workshop Construction)

| Setting | Value |
|---------|-------|
| `fWorkshopExperienceBase` | 2.0 |
| `fWorkshopExperienceMult` | 0.10 |
| `fWorkshopExperienceMax` | 25.0 |

**Formula: `XP = min(fWorkshopExperienceBase + (item_value * fWorkshopExperienceMult), fWorkshopExperienceMax)`**

Building XP is capped at 25 per placed object.

### Public Workshop Multiplier

| Setting | Value |
|---------|-------|
| `fPublicWorkshopExperienceMult` | 0.0 |

**This is set to zero.** Public workshops do not grant additional XP multiplier beyond the base workshop formula. XP from public workshops comes from defending events, not from the workshop ownership itself.

### Scrapping

Scrapping shares the `sStatItemsCraftedOrScrapped` stat counter, suggesting it uses the same workbench XP formula. No separate scrapping XP settings exist -- scrapping grants XP through the workbench system using `fWorkbenchExperienceBase` and `fWorkbenchExperienceMult`.

---

## 7. XP Buffs and Multipliers

### Well Rested and Companion Sleep Bonuses

The game defines three tiers of sleep bonuses as perk effects:

| Perk Record | Name | Effect |
|------------|------|--------|
| `SURV_WellRestedXPBonus` (0x0005C526) | Well Rested | +5% XP |
| `SURV_WellRestedXPBonus2` (0x003CD031) | Well Rested (improved) | +10% XP* |
| `COMP_WellRestedXPBonus3_LoversEmbrace` (0x0059E3EE) | Lover's Embrace | +15% XP* |
| `COMP_WellRestedXPBonus3_KindredSpirit` (0x0059E3EF) | Kindred Spirit | +15% XP* |

*Exact percentage values are stored in the perk's EPFD data blocks (not in the GMST). Community consensus aligns with 5% (Well Rested), and 5% (Lover's Embrace/Kindred Spirit which replace Well Rested for +5% total, not +15%). The GMST data does not contain the exact perk magnitudes -- these are in the EPFD records.*

**These bonuses are mutually exclusive** -- sleeping with a romantic companion ally replaces Well Rested with Lover's Embrace or Kindred Spirit.

### Lunchbox XP Bonuses (stackable)

| Lunchboxes Active | XP Bonus |
|-------------------|----------|
| 1 | +25% |
| 2 | +50% |
| 3 | +75% |
| 4 (max) | +100% |

Source: `SCORE_Lunchbox_Effect_XPBonus_1` through `_4` globals.

Lunchbox buff duration: **3,615 seconds** (~60 minutes, from `SCORE_Lunchbox_BuffDurationGlobal`).

### Food/Consumable XP Bonuses

| Magnitude Tier | XP Bonus | Used By |
|---------------|----------|---------|
| Mag 1 (Low) | +2% | Basic food items |
| Mag 2 (Medium) | +5% | Cranberry Cobbler, etc. |
| Mag 3 (High) | +10% | Cranberry Relish, Brain Bombs |
| Mag 4 (Very High) | +15% | Highest-tier food buffs |

Source: `SURV_Food_Effect_FortifyXPBonus_Mag_1` through `_4` globals.

### Mothman Equinox XP Bonus

| Setting | Value |
|---------|-------|
| `E07A_Mothman_SpellMag_XPBonus` | +15% |

The Mothman Equinox event's "Wisdom of the Mothman" buff grants +15% XP.

### Double XP Events

Two server-side toggles control double XP:

| Global | Default | Purpose |
|--------|---------|---------|
| `Spotlight_DoubleXP` | 0.0 | Standard Double XP weekend flag |
| `Spotlight_DoubleXPSurvival` | 0.0 | Survival mode Double XP (legacy) |

When active, these are set to 1.0 server-side, doubling all XP gains. These are purely server-toggled -- no client-side data reveals the multiplier amount, but community consensus and Bethesda announcements confirm 2x.

### New Player XP Boost

| Global | Value |
|--------|-------|
| `NPE_XPBoostEnabled` | 1.0 |

The New Player Experience XP boost is enabled by default. This accelerates early leveling.

---

## 8. Fishing XP

Fishing (added in the Skyline Valley era) has its own XP table:

| Catch Type | XP |
|-----------|-----|
| Junk | 2 |
| Small Fish | 3 |
| Small Glowing Fish | 5 |
| Medium Fish | 5 |
| Medium Glowing Fish | 7 |
| Large Fish | 10 |
| Large Glowing Fish | 15 |
| Local Legend | 20 |
| Axolotl | 30 |
| Fishing Daily Quest | 500 |
| Fishing Main Quest (Common) | 1,200 |

---

## 9. Season/Scoreboard System

### SCORE Points Per Rank

The Scoreboard does not use an escalating SCORE requirement per rank in the game data. Each rank costs a fixed amount of SCORE (community-confirmed as **150 SCORE per rank** for the first 100 ranks, increasing for prestige ranks). The GMST/GLOB data does not expose the per-rank cost directly -- it is likely hardcoded or defined in server-side configuration.

### SCORE Sources

| Source | SCORE |
|--------|-------|
| Daily Level Up | 250 |
| Weekly Level Up (x3) | 1,000 |
| Daily Expedition Challenge | 250 |
| Weekly Expedition Challenge | 1,500 |

Source: `SCORE_Daily_LevelUp`, `SCORE_Weekly_LevelUp`, `SCORE_XPD_Challenge_Daily_Expeditions`, `SCORE_XPD_Challenge_Weekly_Expeditions` globals.

### Season Board IDs

The game tracks season boards with IDs up to **Season 25** (BoardID 24 in zero-indexed globals), confirming long-term Scoreboard plans:

```
SCORE_Season_BoardID_08 through SCORE_Season_BoardID_25
(values 7 through 24, zero-indexed season numbers)
```

### Rank-Gated Rewards

| Gate | Rank Required |
|------|--------------|
| SCORE_RankGated_Rank_025 | 24 (rank 25) |
| SCORE_RankGated_Rank_050 | 49 (rank 50) |
| SCORE_RankGated_Rank_075 | 74 (rank 75) |
| SCORE_RankGated_Rank_100 | 100 |

---

## 10. XP Caps, Diminishing Returns, and Anti-Farming Mechanics

### No XP Caps in GMST Data

The game data contains **no explicit XP cap per hour, per session, or per kill**. The XP system is uncapped in the settings files. However:

### Death Reward Threshold

| Setting | Value |
|---------|-------|
| `fXPDeathRewardHealthThreshold` | 0.01 (1%) |

You must deal at least **1% of a creature's health** to receive XP for its death. This is the anti-leeching mechanic -- you cannot get XP from kills you did not meaningfully contribute to (outside of team sharing).

### No Diminishing Returns in Formulas

There is no diminishing returns curve in the creature XP or quest XP data. XP per kill is deterministic based on creature type, creature level, and your Intelligence. The only practical "diminishing return" is that higher-level players need more XP per level while low-level creatures give the same XP.

### Workshop XP Caps (Per-Item)

The per-craft/per-build XP caps (50, 25, and 10 for workbench, workshop, and cooking respectively) serve as soft anti-farming measures for crafting XP.

---

## 11. Legendary Perk System and XP

### Perk Coin Economy

Legendary perks do not directly grant XP. Instead, they consume **Perk Coins** (obtained by scrapping regular perk cards):

| Source | Perk Coins |
|--------|-----------|
| Reaching Level 50 (`Challenge_Lifetime_Level50_PerkCoins`) | 50 |
| Burn Challenges (small) | 10 |
| Burn Challenges (large) | 20 |

Perk card scrapping values:

| Setting | Value |
|---------|-------|
| `fPerkCardScrapGlobalValueMult` | configurable multiplier |
| `fPerkCardScrapFoilValueMult` | foil/animated cards scrap for more |

### XP-Boosting Legendary Perks

While no legendary perk directly increases XP gain in the GMST data, **Legendary Intelligence** (adding +5 INT at max rank) indirectly provides +15% XP through the Intelligence formula. Other legendary SPECIAL perks follow the same pattern.

---

## 12. Team XP Sharing

### How Team XP Works

The game tracks shared XP as a separate category (`sStatExperienceGainedShared`), confirming that team XP sharing is a distinct system.

### Inspirational Perk (Charisma)

The Inspirational perk directly boosts team XP sharing:

| Rank | Perk ID | Effect |
|------|---------|--------|
| Inspirational01 | 0x001D2461 | +5% team XP (3 CHA cost) |
| Inspirational02 | 0x001D2462 | +10% team XP (3 CHA cost) |
| Inspirational03 | 0x001D2463 | +15% team XP (3 CHA cost) |

*Exact perk magnitudes are in EPFD data. Community values: Rank 1 = +5%, Rank 2 = +10%, Rank 3 = +15% bonus XP when on a team.*

### Team Sharing in Quest Rewards

Many quests provide explicit teammate XP rewards (typically 10-25% of the primary reward):

| Quest Type | Primary XP | Teammate XP |
|-----------|-----------|-------------|
| Wastelanders Mid-Quest | 250 | 50 (20%) |
| Expedition Finale | 1,500 | 500 (33%) |
| Expedition Main Quest | 1,200 | 120 (10%) |
| Storm Boss | 1,200 | -- |
| Storm Finale | 1,500 | 500 (33%) |
| Sub-quest Mid-points | 100 | 25 (25%) |

### XP Sharing Mechanics

- Team members receive XP for creature kills by any teammate, provided they are in the same world instance
- The `fXPDeathRewardHealthThreshold` (1%) does NOT apply to team-shared kills -- teammates get XP regardless of damage contribution
- Event XP rewards are given to all participants in the event area
- Quest completion XP uses separate teammate globals when defined

---

## 13. Babylon (Nuclear Winter) XP System

The defunct Nuclear Winter mode had its own XP system:

| Setting | Value |
|---------|-------|
| `fBabylonXPBase` | 1,000 |
| `fBabylonXPGrowth` | 0.04 (4%) |

Nuclear Winter XP sources:

| Source | XP |
|--------|-----|
| Per AI Kill (Low/Medium) | configurable |
| Per AI Kill (Elite) | configurable |
| Per Player Kill | configurable |
| Per Player Down | configurable |
| Per Nuke Launch | configurable |
| Per Alive Interval | configurable |

---

## 14. The Backwoods Content XP (Latest DLC)

The Backwoods update added new XP reward globals:

| Content | XP |
|---------|-----|
| Burn E01 (Event) | 1,000 |
| Burn E01 Emote | 347 |
| Burn E02 (Event) | 1,000 |
| Burn SQ01 Reward | 1,000 |
| Burn SQ02 Outro Part 1 | 1,250 |
| Burn SQ02 Outro Part 2 | 1,600 |
| Burn SQ04 Dirty Laundry | 1,600 |
| Burn MQ03 | 800 |
| Bounty Hunt (Public) | 1,500 |
| Bounty Hunt (Daily) | 1,000 |
| Bounty Hunt XP Bonus Duration | 1,200 seconds |

---

## 15. Complete XP Stack Summary

All of these bonuses are additive with each other but multiplicative against base XP:

```
Final_XP = Base_XP * INT_Multiplier * (1 + sum_of_all_percentage_bonuses)

Where:
  INT_Multiplier = 1.0 + (Intelligence * 0.03)
  Percentage bonuses include:
    - Well Rested/Lover's Embrace: +5%
    - Lunchboxes: +25% to +100% (1-4 boxes)
    - Food buffs: +2% to +15%
    - Inspirational: +5% to +15% (team only)
    - Mothman Equinox: +15%
    - Double XP event: +100%
    - Night Person: +INT at night (indirect)
    - Casual Team bond: +INT (indirect)
```

### Theoretical Maximum XP Multiplier

With all buffs stacked:
- Intelligence at 60 (Unyielding + Egghead + Shielded + Casual Team + food): **2.80x**
- 4 Lunchboxes: **+100%**
- Double XP: **+100%**
- Cranberry Relish/Brain Bombs: **+10%**
- Well Rested: **+5%**
- Inspirational 3: **+15%**
- Mothman buff: **+15%**

**Max theoretical: 2.80 * (1 + 1.0 + 1.0 + 0.10 + 0.05 + 0.15 + 0.15) = 2.80 * 3.45 = 9.66x base XP**

*The exact stacking behavior (whether INT is truly multiplicative with additive buffs, or all additive) has been debated. The GMST data defines INT as a separate multiplier (`fXPModBase/fXPModMult`), distinct from the percentage bonus system, supporting the multiplicative model shown above.*

---

## Data Sources

| File | Content |
|------|---------|
| `esm_dump/game_settings.txt` | GMST values: iXPBase, iXPBumpBase, fXPModBase, fXPModMult, lockpick/craft/workshop XP |
| `esm_dump/GLOB_records.txt` | Quest XP rewards, Lunchbox bonuses, event multipliers, SCORE values, fishing XP |
| `esm_dump/PERK_records.txt` | Well Rested, Inspirational, Lover's Embrace perk definitions |
| `tempest_data/misc/curvetables/json/player/xp/` | 100 universal XP tier curves (creature XP by level) |
| `tempest_data/misc/curvetables/json/creatures/xp/` | 5 creature size category XP curves |
| `tempest_data/misc/curvetables/json/quests/` | Quest XP multiplier and caps curves |
