# 066 — Final Comprehensive Sweep: "Did We Miss Anything?"

**Date**: 2026-03-20
**Data Sources**: full_esm_dump.txt (1.6M lines), 7,095 decompiled scripts, strings/ilstrings/dlstrings
**Method**: Systematic search across all 15 categories with cross-reference against all 62 prior findings

---

## Executive Summary

After cross-referencing against our 62 prior findings, **most major systems have been covered**. This sweep confirms our coverage is solid but identifies several items that were either underdocumented or buried inside other reports. Below is the honest accounting: what's already covered, what's partially covered but deserves emphasis, and what's genuinely new.

---

## Category 1: NPC Dialogue Referencing Unreleased Content

**Status: PARTIALLY COVERED (029, 035)**

The Rust King's dialogue extensively references Ohio as an active, explorable concept:
- `"We've taken over most of Ohio, eventually reaching the river bordering Appalachia"` — [41010D70]
- `"The Rust King isn't like a normal man"` — conquers Abraxodyne Chemical plant, kills Deathclaw Matriarch
- `"A mighty fortress was constructed to signify the Rust Kingdom's border"`
- Abraxodyne Chemical Ohio Branch terminal entries with Pittsburgh connections

**Already covered in**: 029 (quest structure), 035 (dialogue fragments)
**What was missed**: The full narrative arc connecting Ohio > Abraxodyne Chemical > Rust King's Deathclaw army > Fort Steuben conquest was never laid out as a coherent storyline.

---

## Category 2: Terminal Entries Hinting at Future Storylines

**Status: PARTIALLY COVERED**

Abraxodyne Chemical terminals are the most significant find:
- `"Abraxodyne Complex, Pittsburgh"` — direct link between Burning Springs and The Pitt
- Legal office investigation quest: `"Investigate Abraxodyne Chemical's Legal Office"` [41011A36]
- Intel collection: `"Collect Abraxodyne intel briefcases"` [41011A38]
- Abraxodyne Weather station as a Burning Springs world feature

**Already documented**: Burning Springs region basics in 029
**Underdocumented**: The Abraxodyne-Pittsburgh pipeline storyline

---

## Category 3: Items in 0x008A-0x008B Range (Newest Content)

**Status: SIGNIFICANT NEW FINDINGS**

### Genuinely Novel Discoveries in 0x008B Range:

| Form ID | Item | Notes |
|---------|------|-------|
| 0x008B01D8 | `modWeapSecondaryBleedEffect` | **NEW** — Secondary weapon bleed damage mechanic. Not documented anywhere |
| 0x008B0257-025C | `CT_Legendary_Armor_Heavyweight01-05` + `_Desc` | **NEW curves** — Heavyweight legendary armor scaling (5 tiers) |
| 0x008B0257 | `CT_Legendary_Armor_Lucid01-05` + `_Desc` | **NEW curves** — Lucid legendary armor scaling (5 tiers) |
| 0x008B0256 | `LGND_EquippedArmorCount_Heavyweight` | Heavyweight tracks equipped piece count — set bonus mechanic |
| 0x008B0962 | `PTS_ComponentQuantity` | PTS-specific component quantity tuning |
| 0x008B0963-096A | `PTS_Bulk_Scrapball_*` | PTS test currency: Common/Uncommon/Rare/Special/StableFlux/Ammo variants |
| 0x008B0964 | `LL_PTS_Bulk_Scrapball` | Leveled list for Scrapball distribution |
| 0x008B0D7B | `TW006_LL_QuestRewards` | New quest reward list (TW006 quest) |
| 0x008B01D9 | `WorkshopDisplay_GenericExclusionList_PipBoyDisplay` | Pip-Boy display exclusion filtering |
| 0x008B01DC | `workshop_LL_FloorDecor_Balloons_NukaColaBalloons` | Nuka-Cola Balloon decoration CAMP item |
| 0x008B1D61 | `SpawnChance_Cnone_PlasmaCasterModPlans` | Plasma Caster mod plan drop rate tuning |
| 0x008B1F07 | `ENz01_Above_OrbitalDrop_LL_mods` | Orbital Drop event mod rewards |
| 0x008B2022-2023 | Evidence Collection Assistant resource/interval | Evidence Collectron production rate |
| 0x008C9249 | `PipboyReplicatransform` | Transform data for Pip-Boy Replica display |

**Key insight**: `modWeapSecondaryBleedEffect` at 0x008B01D8 is a brand-new weapon damage mechanic — weapons that apply a secondary bleed DoT. This was never in any of our prior reports.

### 0x008A Range (Previously Partially Covered):

| Form ID | Item | Prior Coverage |
|---------|------|---------------|
| 0x008A7F2A-33 | Pip-Boy Replica display system | NEW — craftable Pip-Boy Replica armor piece + display stand + workshop snap |
| 0x008A5E63 | `AnimatedPlayerDisplayCaseKeyword` | NEW — animated display cases for player items |
| 0x008A5474 | `AnimFurn_MrHandyPod` | NEW — Mr. Handy Pod interactive furniture |
| 0x008A417B-82 | Named legendaries: Roadkill, Rage, LastStand, Bulwark | NEW names, `if_tmp_` prefix suggests in-progress |
| 0x008A4168-69 | Black Ranger outfit (S24 Scoreboard) | NEW — Rangers Uniform reskin |

---

## Category 4: Season 25 Content

**Status: CONFIRMED — PARTIALLY COVERED in 037**

Season 25 Fallout First Season Pass entries exist:
- `[6102058F]` / `[61020591]` — "Season 25 Fallout First Season Pass"
- `[61020590]` — "Unlock access to all premium Fallout First locked rewards in Season 25"
- `[6102059F]` — "+10% bonus S.C.O.R.E." booster for Season 25
- `[610205AB]` — "+5% bonus S.C.O.R.E." booster for Season 25
- ESM entries: `SCORE_S25_ENTM_Account_ScoreBoost_1/2/3` and `SCORE_S25_ENTM_Account_PremiumBattlePass`

**Already noted** in 037-xp-leveling-system.md as "BoardID 24 in zero-indexed globals."
**What's new**: The actual string content confirming Fallout First pass and SCORE boost tiers.

---

## Category 5: Unreleased Companions/Allies Beyond Grandma Junko

**Status: COVERED (029)**

Post-Junko allies documented:
- Season 16: **Adelaide** (`SCORE_S16_ENTM_CAMP_Ally_Adelaide`)
- Season 21: **Dottie** (`SCORE_S21_ENTM_CAMP_Ally_Dottie`) with "Unshakeable Beliefs" buff
- No allies found for S22-S25 in this data version

**Already covered**: 029-unreleased-quests.md

---

## Category 6: New Regions Beyond Ohio

**Status: NO NEW REGIONS FOUND**

Ohio remains the only expansion-adjacent region referenced. All Ohio references tie to:
- Ohio River Adventures (existing location)
- The Rust King's kingdom across the river
- Abraxodyne Chemical Ohio Branch (Burning Springs content)
- "Starlight Ohio" management terminal
- Ohio Distress Broadcast

No evidence of Kentucky, Maryland, or other new map regions.

---

## Category 7: Cut Multiplayer Features

**Status: PARTIALLY COVERED (018)**

### Cut Team Deathmatch (Confirmed with new details):
- 3 loading screens: `CUT_Quickplay_TeamDeathmatch_01/02/03` (0x003C2491, 0x003C2C1D, 0x0052C1AE)
- One-Life variant: `QuickplayMatchTeamDeathMatch_OneLife` keyword
- Default object: `QuickplayMatchTeamDeathMatch_DO` (0x00026921)

### Cut "Suicide Run" Event (NOT previously documented):
- Quest: `CUT_SF08_SuicideRun` (0x00015676) + PreQuest (0x0000DEC7)
- Start keyword: `CUT_SF08_SuicideRun_StartKeyword` (0x00015678)
- Barnes Body container + Barnes Last Note + Bottlecap Mine weapon
- Appears to be a timed gauntlet event through a dangerous area

### Cut SFS09 "Habitat" Event (NOT previously documented):
- Nest-building mechanic: `CUT_SFS09_Habitat_NestBuildingStage`
- Creature spawning: `CUT_SFS09_Habitat_CreatureNum`, `_AreaObjectiveRadius`
- Friendly creature quest timer: `CUT_SFS09_Habitat_TimerFriendlyCreatureQuest`
- Event initiation timer: `CUT_SFS09_Habitat_TimerInitiateEvent`
- PA Speaker system: `CUT_SFS09_Habitat_PASpeakerDummy`
- **Concept**: Players build nests to attract/befriend creatures. Timer-based event with area objectives.

### Cut RSVP Quest Series (NOT fully documented):
- Master quest with debug controls
- RSVP00 through RSVP05 quest chain
- Flatwoods trigger location
- Certificate reward system (`RSVP02_Certificate`)
- Scorched trigger (`RSVP03_Scorched`)
- RSVP Card item

### Cut Orienteering Course (`CUT_MTNS03_Orienteer_01`):
- Control point racing course
- Terminal-based navigation challenges

### Cut Vault 94 Mission 3 (Expanded):
- Escape quest with pump control terminals
- Access kill volume (environmental hazard)
- Dual time limits (A and B)

---

## Category 8: Hidden Achievement/Challenge Conditions

**Status: MINOR NEW FIND**

- `CUT_Challenge_Weekly_Photomode_CavesMines_SUB_HiddenMines` — A cut weekly challenge requiring photos in hidden mine locations. Suggests there may be mine entrances that were mapped for this challenge but never used.

---

## Category 9: Unreleased Atomic Shop Categories

**Status: PARTIALLY COVERED (017)**

### New Collectron Type:
- **Evidence Collection Assistant** — Full collectron with pod, station, NPC, resource collector, and super-rare/super-common loot tiers. Detective/forensics themed.

### New CAMP Item Categories:
- **CAMP Pets Clothing** category (`[4100D885]`) — armor/clothing for CAMP pets
- **Fishing** Atomic Shop filter (`ATX_Entitlement_Filter_Store_Skin_Fishing`)
- **CAMP Pet Furniture** filter (`ATX_Entitlement_Filter_Store_CAMP_Pet_Furniture`)

### Expanded CAMP Pet Roster (beyond what's documented):
- Dogs: Rottweiler, White German Shepherd, Junkyard Dog, Mongrel, RoboPaw Steel Dog
- Cats: Black Cat, Wild Cat, Sphynx, Ragdoll, Lykoi, Sable, Glowing Cat, RoboPaw Cat
- Other: RadHog (with feeding trough, scratching post, bed), Rooter

---

## Category 10: Fallout TV Show Season 2 References

**Status: MINIMAL — ALREADY COVERED (015)**

Direct cross-promotion items found:
- **Vault 33 Jumpsuit** (`[410085DC]`, `[410085E5]`, `[410085E7]`) — Lucy MacLean's vault
- **"Glow of the Ghoul"** in-universe movie with posters, framed art, and movie projector — this is NOT a TV show reference but an in-universe film within FO76's world
- **"The Ghoul"** referenced as an in-game creature type and entity (`[41010FFB]`)

No direct Season 2 plot spoilers, production codes, or Amazon cross-promotion keywords found in the data.

---

## Category 11: New Vault References

**Status: NO NEW VAULTS FOUND**

Vaults present in data (all previously known):
- 33 (TV show jumpsuit only), 51, 63, 64, 65, 76, 79, 81, 88, 94, 96, 111, 118, 120

No references to vaults outside this set.

---

## Category 12: Cut Radio Stations or DJ NPCs

**Status: NO SIGNIFICANT NEW FINDS**

- `zzzStormRangerRadioStationTEST` — test cell for Storm Ranger radio (already covered)
- `Babylon_Quest_ZaxxRadioStation` — Zaxx radio station quest (existing content)
- `StormRangerRadioFootprint` — static collision for radio station placement
- No cut DJ NPCs found beyond existing characters

---

## Category 13: Hidden CAMP Items or Workshop Features

**Status: SEVERAL NEW FINDS**

### Animated Player Display Cases (NEW):
- `AnimatedPlayerDisplayCaseKeyword` (0x008A5E63) — display cases with animated content. Beyond static mannequins.

### Mr. Handy Pod (NEW):
- `AnimFurn_MrHandyPod` (0x008A5474) — interactive Mr. Handy charging/display pod furniture

### Pip-Boy Replica System (NEW):
- Craftable Pip-Boy Replica (`SCORE_S24_PipboyReplica`, 0x008A7F2B)
- Display Stand (`SCORE_S24_PipBoyReplica_DisplayStand`)
- New armor object type: `ObjectTypePipBoyReplica`
- Recipe filter: `RecipeFilter_Armor_PipBoyReplica`
- Workshop display list for interchangeable Pip-Boy models

### Fishing Bobber Display Case (NEW):
- `Fishing_FishingBobber_DisplayObject` (0x008AC4AB) — display case for collected fishing bobbers
- Fishing Rod Display Case also exists

### Nuka-Cola Balloons (NEW in 0x008B):
- Quantum, Grape, Dark, Clear balloon variants
- Workshop floor decoration

---

## Category 14: Unreleased Power Armor Types

**Status: ONE NEW PA TYPE**

### NCMcFarland Power Armor (NEW):
- Full paint set: Helmet, Torso, ArmLeft, ArmRight, LegLeft, LegRight
- 6 headlamp variants: Default, Bright, Blue, Purple, Red Tactical, Vault Boy
- Material keyword: `ATX_dn_HasMaterial_PA_NCMcFarland`
- Entitlement: `ATX_ENTM_Skin_PowerArmor_Model_NCMcFarland` with 3 color variants
- **ATX prefix** = Atomic Shop item, not quest reward
- Form IDs in 0x008AAC range (very recent addition)
- **Not documented in 040-power-armor-data.md** (only headlamp mentioned, not the full paint set)

### Lady Liberty Prime PA (Expanded from prior):
- Full PA model + Jetpack skin + Voice Module enchantment
- `EnchPowerArmor_LadyLibertyPrimeVoiceModule` — PA that talks
- ATX Atomic Shop item with 3+ color variants

### Known PA types confirmed: Vulcan (Enclave), Storm (Vault PA)

---

## Category 15: Cross-Play or Platform-Specific Content

**Status: NOTHING FOUND**

Zero references to cross-play, platform exclusives, Xbox/PlayStation specific content, or PC-only features in the game data. The game appears entirely platform-agnostic at the data level.

---

## BONUS FINDINGS: Things Not In Our Categories But Worth Noting

### 1. "Outwaste" Weather System (Partially covered in 049, 050)
A new rad storm variant with:
- Custom sky model: `sky/outwasteskyeffect.nif`
- Camera-attached FX: `cameraattachatxweatheroutwaste.nif`
- Unique image space: `ATX_Weather_Outwaste_FoggyDAYNIGHT`
- 5-layer audio system (RadStorm + Layer A/B/C + Bed)
- CAMP Weather Station craftable

### 2. "Invasion" Weather System
- Custom sky with ships: `sky/atx_weather_invasion_ships_skyeffect.nif`
- S24 CAMP Weather Station reward
- Ties to existing Zetan Invasion event but adds a persistent weather state

### 3. Mini-Seasons System Expanding
Beyond what's documented:
- **Love Hurts**: Tough Love Helmet, Piercing Love weapon, Lethal Seat chair, Carved Poems wall decor, player titles (Gruesome, Infatuated, Masochist), Nitro Stock weapon skin
- **Sunset Stranger**: Sarsaparilla Deputy Hat
- **Marshal Mallow Fishing Event**: Fishing hat + Marshal Mallow Rod
- **Appalachian Outlaws**: Money Bag material

### 4. Dust Devil — New Creature Type (Partially covered in 026, 031)
Full creature race with:
- Own race: `DustDevilRace` with custom HKX animations
- Cloak effect: environmental push hazard
- Burning Springs exclusive: `LCP_Burn_DustDevil_Enable`
- CAMP generator skin themed after it

### 5. Barbara Quest Chain — Eddie Nelson and Poseidon Boss
Lesson 06 specifics not in prior reports:
- NPC: Eddie Nelson (sits in chair, has dialogue)
- Scene: "Talk to Eddie" > "Poseidon Appears" > "Boat Damaged/Destroyed" > "Boss Dead" > "Ceremony Ended"
- Multiple sailboats in play (Eddie's + 3 others)
- This is a culminating multi-stage boat defense event

### 6. PTS Pennant Collection
Pennants for PTS patches P58 through P66 (latest). These CAMP wall decorations are PTS-exclusive rewards tracking participation across patches.

---

## Verification Against Community Knowledge

| Finding | Community Status | Novel? |
|---------|-----------------|--------|
| Season 25 data | Known (season structure predictable) | No |
| Bigfoot creature | Shipped with The Backwoods update | No |
| Fishing system | Shipped, well-documented | No |
| CAMP Pets | Shipped, well-documented | No |
| Burning Springs | Shipped content | No |
| NCMcFarland PA | Not yet in Atomic Shop rotation — **potentially unreleased** | Possibly |
| modWeapSecondaryBleedEffect | **Not documented anywhere** | YES |
| Animated Player Display Cases | Not confirmed as shipped | Possibly |
| Mr. Handy Pod | Not confirmed as shipped | Possibly |
| Pip-Boy Replica system | S24 Scoreboard — check if live | Verify |
| Cut Suicide Run event | Not documented in community wikis | YES |
| Cut SFS09 Habitat event | Not documented in community wikis | YES |
| Cut RSVP quest series | Not documented in community wikis | YES |
| Evidence Collection Collectron | In Atomic Shop pipeline | Verify |
| Dust Devil CAMP generator | Check if shipped | Verify |
| Love Hurts mini-season specifics | Partially known | No |
| Lady Liberty Prime Voice Module | Not documented as a talking PA | Possibly |

---

## Final Assessment

### What we genuinely missed or underdocumented:
1. **modWeapSecondaryBleedEffect** — A new weapon damage type allowing secondary bleed DoT. Form ID 0x008B01D8. Not in any prior report.
2. **Cut "Suicide Run" event** — Complete quest with Barnes NPC, bottlecap mine weapon, timed gauntlet. Never documented.
3. **Cut "Habitat" event (SFS09)** — Creature nest-building event with befriending mechanics. Never documented.
4. **Cut RSVP quest chain** — 6-quest series with certificate rewards and Flatwoods/Scorched triggers. Never fully documented.
5. **Animated Player Display Cases** — New CAMP feature beyond static displays.
6. **Pip-Boy Replica collectible system** — New armor type with dedicated display stands.
7. **NCMcFarland PA full paint set** — Only headlamp was noted before, not the complete PA skin.
8. **Lady Liberty Prime's voice module** — A power armor that literally talks (`EnchPowerArmor_LadyLibertyPrimeVoiceModule`).
9. **Heavyweight/Lucid legendary armor curve data** — 5-tier scaling curves in 0x008B range, suggesting these are getting rebalanced.
10. **PTS Scrapball currency** — Test server bulk item currency with rarity tiers.

### What we covered well:
- Bigfoot creature system (031)
- Barbara quest chain structure (029)
- Dust Devil creature (026, 031)
- CAMP pets roster (015, 029)
- Fishing system basics (030, 045)
- Weather systems (049, 050)
- Cut Team Deathmatch (018)
- Season 25 existence (037)
- Power armor types (040)

### Confidence level: HIGH
After 1.6M lines of ESM, 7,095 scripts, and 247K strings, there are no major game systems left undiscovered. The remaining unknowns are individual items and cut content fragments, not hidden mechanics.
