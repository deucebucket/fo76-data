# Finding 099: The Cut Rotating Boss Encounter System (CUT_SFZ03_Queen_MasterQuest)

**Category:** Cut Content / Boss Systems
**ESM Records:** 80+ related records across QUST, KYWD, GLOB, PERK, MGEF, SPEL, WAVE, LCTN, LCRT, FLST, ACTI, CONT, BOOK, TERM, NPC_, CELL, AVIF, SMQN, CHAL, GMRW types

---

## Overview

Buried in the Fallout 76 ESM is evidence of an alternate Scorchbeast Queen encounter system that would have replaced the current fixed-location nuke-triggered fight with a rotating multi-location boss event. The system is identified as `CUT_SFZ03_Queen_MasterQuest` (FormID `0x0043D032`) and represents one of the most mechanically complex cut systems in the game.

Unlike the live Scorched Earth event (CB15), which always spawns at a single fissure site in the Cranberry Bog when nuked, this cut system would have rotated the Queen fight across **five distinct outdoor locations** in the Cranberry Bog/Mire region, with each rotation featuring both standard creature bosses and a **cryptid boss encounter** drawn from the five West Virginia cryptid species.

---

## 1. The Rotating Boss System Architecture

### CUT_SFZ03_Queen_MasterQuest (`0x0043D032`)

The MasterQuest is the orchestrator. It contains **22 aliases** (`ANAM 0x00000016`):

| Alias | Count | Purpose |
|-------|-------|---------|
| `SFZ03BossEligiblePlayers` | 1 | Player collection for eligibility |
| `LocNormalBoss01-05` | 5 | Standard creature boss spawn slots |
| `LocCryptidBoss01-05` | 5 | Cryptid boss spawn slots (tagged `SFZ03_Queen_CryptidBossKeyword`) |
| `LocPile01-05` | 5 | Cryptid sample/corpse pile locations (tagged `SFZ03_Queen_CryptidBossKeyword`) |
| *Unknown remaining* | 6 | Likely trigger/marker aliases |

All LocCryptidBoss and LocPile aliases carry keyword `0x00518904` (`SFZ03_Queen_CryptidBossKeyword`), confirming they are part of the cryptid subsystem.

### Rotation Globals

Three global variables controlled which locations were active per rotation:

| Global | FormID | Purpose |
|--------|--------|---------|
| `SFZ03_Queen_NormalLocation01` | `0x0043D035` | Index of first normal boss location |
| `SFZ03_Queen_NormalLocation02` | `0x0043D036` | Index of second normal boss location |
| `SFZ03_Queen_CryptidLocation` | `0x0043D034` | Index of the cryptid boss location |
| `SFZ03_Queen_BossGlobal` | `0x00031A99` | Master rotation state tracker |

All initialize to `0.000000`, meaning the rotation logic was script-driven. The child quest `SFZ03_Queen` (`0x000451FC`) uses a `BossLocation_var` script variable checked across six conditions (values 1, 2, 3 compared against three different variable hashes), confirming a three-location-per-run selection system.

### How a Single Run Worked

The child quest `SFZ03_Queen` reveals the complete flow:

1. **Startup** (Debug stage)
2. **Investigate the shack** -- Player discovers Shelby's research terminal
3. **Investigate the locations** -- Terminal directs player to 3 selected boss locations
4. **Enter trigger volumes** -- `LocTrigger01/02/03` fire stages via `DefaultAliasOnTriggerEnter`
5. **Boss spawned** at each location via `DefaultQuestEncounterWaveScript`
6. **Boss encountered** -- Combat detected via `DefaultCollectionAliasOnHit` or `DefaultCollectionOnCombatStageChanged`
7. **Boss dead** at each location
8. **Kill the cryptid** -- One of the three locations has a cryptid instead of a normal boss (stages 151/161/171 determine which)
9. **Extract the sample** -- Loot cryptid tissue sample from the corpse (stages 155/165/175)
10. **Deposit Sample** in the Tissue Analyzer (`SFZ03_Queen_TissueAnalyzer`, model: techbox01a.nif)
11. **Sample deposited** -- `DefaultAliasOnActivateRemoveItem` fires
12. **AnalyzerScene plays** -- `SFZ03_Queen_AnalyzerScene` (`0x00519B99`) runs in two phases: enable SFX (phase 1), then cast buff (phase 3)
13. **Buff applied** -- One of five cryptid-specific buffs granted to the player
14. **Complete**

The quest uses three BossCollection aliases (`BossCollection01/02/03`), each tagged with:
- `SFZ03_Queen_BossKeyword` (`0x00004192`)
- `ImmuneToNukes` (`0x0044A9FB`)
- `NoDisintegrate` (`0x0022DB8F`)

The ImmuneToNukes keyword is notable -- it means these bosses were designed to survive nuclear detonation, unlike regular enemies in nuke zones.

### The Five Boss Locations

| Location | FormID | Cell | Grid Coords | XLCN | Region |
|----------|--------|------|-------------|------|--------|
| BossLocation01 | `0x000451FF` | `SFZ03QueenBossCell01` (`0x00260648`) | (44, 42) | `0x000451FF` | Northern Mire |
| BossLocation02 | `0x00045208` | `SFZ03QueenBossCell02` (`0x0026032A`) | (48, 36) | `0x00045208` | Eastern Mire |
| BossLocation03 | `0x0003BD69` | `SFZ03QueenBossCell03` (`0x00260332`) | (48, 28) | `0x0003BD69` | Cranberry Bog (north) |
| BossLocation04 | `0x002B5634` | `SFZ03QueenBossCell04` (`0x0026033C`) | (48, 18) | `0x002B5634` | Cranberry Bog (south) |
| BossLocation05 | `0x002B5639` | `SFZ03QueenBossCell05` (`0x00260D6F`) | (35, 20) | `0x002B5639` | Cranberry Bog (west) |

All five locations share the keyword `LocTypeFastTravelDestination` (`0x0033FE91`), confirming they would have been fast-travel-eligible map markers.

Each location has:
- A **BossTrigger** activator ref (`CUT_SFZ03_Queen_BossTrigger`, `0x0043AF12`) -- proximity trigger to initiate the encounter
- A **BossMarker** ref -- spawn point for the boss creature
- Association with `SFZ03_Queen_BossTriggerLocRefType` (`0x0043AF13`) and `SFZ03_Queen_BossSpawnsLocRefType` (`0x000451FE`)

The geographic spread covers a diagonal swath from the northern Mire (44,42) down through the eastern edge of the map (48,36 and 48,28) to the southern and western Cranberry Bog (48,18 and 35,20). This is a much larger combat zone than the current Scorched Earth event's single fissure site.

---

## 2. The Five Cryptid Bosses

### Confirmed Cryptid Species

Each cryptid is verified by race ID conditions on its corresponding perk:

| Cryptid | Perk | Race | Race FormID |
|---------|------|------|-------------|
| **Flatwoods Monster** | `SFZ03_Queen_FlatwoodsPerk` (`0x00007393`) | FlatwoodsMonsterRace | `0x00110E0A` |
| **Grafton Monster** | `SFZ03_Queen_GraftonPerk` (`0x00007394`) | GraftonMonsterRace | `0x0000E889` |
| **Mothman** | `SFZ03_Queen_Mothman` (`0x00007395`) | MothmanRace | `0x0000D233` |
| **Snallygaster** | `SFZ03_Queen_Snallygaster` (`0x00007396`) | SnallyGasterRace | `0x0000D191` |
| **Wendigo** | `SFZ03_Queen_Wendigo` (`0x00007397`) | WendigoRace | `0x0001554D` |

Notably absent: **Sheepsquatch** (added later with the Wild Appalachia update). The five cryptids here are the original West Virginia cryptid roster from launch.

### Cryptid Buff System

Each cryptid, when killed and its tissue sample analyzed, would grant a unique buff to the player:

| Cryptid | Spell (Buff) | Magic Effect |
|---------|-------------|--------------|
| Flatwoods Monster | `SFZ03_Queen_FlatwoodsBuff` (`0x002D0839`) | `SFZ03_Queen_FlatwoodsEffect` (`0x000041A1`) |
| Grafton Monster | `SFZ03_Queen_GraftonBuff` (`0x002D083A`) | `SFZ03_Queen_GraftonEffect` (`0x000041A2`) |
| Mothman | `SFZ03_Queen_MothmanBuff` (`0x002D083B`) | `SFZ03_Queen_MothmanEffect` (`0x00007390`) |
| Snallygaster | `SFZ03_Queen_SnallygasterBuff` (`0x002D083E`) | `SFZ03_Queen_SnallygasterEffect` (`0x00007391`) |
| Wendigo | `SFZ03_Queen_WendigoBuff` (`0x002D083F`) | `SFZ03_Queen_WendigoEffect` (`0x00007392`) |

The buff names are stored in localization strings (FULL references), meaning they would have had player-visible names. The specific stat bonuses are not recoverable from the dump format, but the five-buff system suggests a design where players would seek out specific cryptids for their preferred buff, adding a strategic layer to which rotation to farm.

### Cryptid Detection Perk

`SFZ03_Queen_CryptidPerk` (`0x005105EE`) has three conditions:
1. Target `HasKeyword` `SFZ03_Queen_CryptidBossKeyword` -- confirms it's a cryptid boss
2. Target `GetDead == 1` -- cryptid must be dead
3. Target `HasKeyword` `SFZ03_Queen_CryptidContainerKeyword` (`0x0043D037`) -- enables sample looting

This is the perk that fires stage progression when the player activates a dead cryptid boss, triggering the tissue sample collection.

### Day/Night Cryptid Variants

The system had separate wave spawners for day and night cryptids:

| Wave Type | FormID | Keyword |
|-----------|--------|---------|
| `WaveType_SpecialSFZ03Creatures` | `0x0043D03C` | `WaveKeyword_SFZ03Creatures` (`0x0043D039`) |
| `WaveType_SpecialSFZ03CryptidsDay` | `0x0043D03E` | `WaveKeyword_SFZ03CryptidsDay` (`0x0043D03A`) |
| `WaveType_SpecialSFZ03CryptidsNight` | `0x0043D03D` | `WaveKeyword_SFZ03CryptidsNight` (`0x0043D03B`) |

Corresponding form lists:
- `CUT_SFZ03_Queen_CryptidKeywordsDay` (`0x0051890B`)
- `CUT_SFZ03_Queen_CryptidKeywordsNight` (`0x00031AAD`)
- `CUT_SFZ03_Queen_CreatureKeywords` (`0x00031AA8`)

All three form lists are flagged CUT in the live game. The day/night distinction suggests certain cryptids would only appear at specific times -- consistent with Mothman's nocturnal lore and the Flatwoods Monster's association with nighttime sightings.

---

## 3. Trigger Mechanism: NOT Nuke-Based

### Evidence Against Nuke Triggering

The SFZ03_Queen system was **not nuke-triggered**. Key evidence:

1. **Quest filter path:** `SwampForest\` -- The quest is categorized under Swamp/Forest (Mire region), not Cranberry Bog where nukes currently trigger Scorched Earth.

2. **Story Manager node conditions:** `SFZ03_Queen_QuestNode` (`0x005105EC`) triggers on:
   - `HasKeyword` `SFZ03_Queen_OnQuestKeyword` == 0 (player not already on quest)
   - Quest `SFZ03_Queen` (`0x000451FC`) running check == 0
   - `GetEventData` matching `SFZ03_Queen_StartKeyword` (`0x00031AB9`)

   No nuke-related conditions are present.

3. **Daily quest classification:** The system uses `DailyQuestAVRegionSwamp_SFZ03_Queen` (`0x005105E8`), placing it in the daily quest rotation for the Mire/Cranberry Bog region, not the nuke event system.

4. **Challenge reference:** `Challenge_Quests_SpecificQuest_Daily_Launch_SFZ03_Queen` (`0x0043AC4D`) -- the word "Launch" here refers to quest launch, not nuclear launch. It is a daily quest challenge tracker.

5. **Boss immunities:** The `ImmuneToNukes` keyword on all three BossCollections means the bosses would survive nuclear detonation. If the event required a nuke to start, making bosses nuke-immune would be redundant with the current design but necessary if players might nuke a boss location during an active event.

### Actual Trigger: Daily Quest via Terminal

The triggering mechanism was a **terminal interaction** at Shelby's research shack:

- `SFZ03_Queen_StartRef` (`0x001488E3`) -- the quest start marker in the world
- `SFZ03_Queen_TerminalRef` (`0x000451F9`) -- Shelby's terminal that kicks off the quest
- `SFZ03_Queen_ShelbyTerminal` (`0x00519B9A`) -- the terminal object with quest-conditional text
- `GQ_MiscRegionPointer_SFZ03` (`0x00389CC0`) -- the miscellaneous pointer quest that directs players to the shack

The Shelby Terminal has three body text states based on quest progression:
1. Pre-quest (stage 100 not done): Initial discovery text
2. Mid-quest (stage 100 done, stage 200 not done): Progress update
3. Post-quest: Different text state

The system was designed as a **repeatable daily quest** triggered by visiting a research terminal, not by launching a nuclear weapon.

---

## 4. Comparison with the Live Boss System

### Live Game Boss Events (as of March 2026)

| Event | Trigger | Location | Added |
|-------|---------|----------|-------|
| Scorched Earth (SBQ) | Nuke Cranberry Bog fissure | Fixed: Fissure Site Prime | Launch |
| A Colossal Problem (Earle) | Nuke Monongah Mine | Fixed: Monongah Mine | Wastelanders |
| Encryptid | Assaultron Recall Keycard | Fixed: Pylon site near Whitespring | Wild Appalachia |
| Ultracite Titan | Nuke specific zones | Semi-fixed zones | Expeditions |
| Storm Goliaths | Seasonal/weather events | Roaming | Atlantic City |
| EN06 Guardian | Expedition completion | Fixed: Pitt expedition | Expeditions |
| Bigfoot | World event | Roaming | Skyline Valley |

### How the Cut System Differs

**Design Philosophy:**
- **Live system:** Fixed-location, single-boss encounters. Each event has one location and one boss type. Players know exactly what they'll fight and where.
- **Cut system:** Variable-location, multi-boss rotations. Three of five locations selected per run, with one featuring a cryptid instead of a standard boss. Players would get different experiences each time.

**Engagement Model:**
- **Live system:** High-investment triggers (nukes cost significant resources; keycards require grinding).
- **Cut system:** Low-investment daily quest triggered by terminal interaction. Repeatable without resource expenditure.

**Reward Structure:**
- **Live system:** Boss-specific loot tables (SBQ drops Ultracite plans, Earle drops Cursed weapons, etc.)
- **Cut system:** Standard quest reward (`SFZ03_Queen_Rewards` `0x003D75B8` references `LLS_Recipe_Mod_UnderArmor_Casual_Mk5_Chance`) PLUS unique cryptid-specific buffs. The buff system added a secondary reward layer not present in any live boss event.

**Complexity:**
- **Live system:** Simple -- go to location, kill boss, collect loot.
- **Cut system:** Multi-stage investigation with terminal interaction, traveling to three locations, killing standard bosses AND a cryptid, harvesting a tissue sample, returning to the analyzer, and receiving a buff. This is closer to a daily expedition than a world boss fight.

### Was It Meant to Replace or Complement?

Evidence strongly suggests the rotating system was an **earlier design iteration** that was replaced by the simpler fixed-location system, not a complement to it:

1. The `SFZ03_Queen` child quest shares its quest expire global (`QuestExpireGlobal_Default`, `0x00380939`) with many other daily quests, not with the Scorched Earth event system which uses its own timer (`0x00530618`).

2. The quest is filed under `SwampForest\`, the same category as other Mire daily quests, not the event system.

3. CB15_ScorchedEarth uses a completely different architecture (Region/FissureLocation/AffectedEventLocation aliases vs the BossLocation/BossCollection pattern) and references a Confluence design doc URL, suggesting it was designed from scratch as a replacement.

4. The Confluence doc URL on CB15 (`https://bnet-confluence.zenimax.com:8443/display/P7/CB15+-+Scorched+Earth`) uses the CB15 prefix (Cranberry Bog event 15), while SFZ03 uses the SFZ prefix (Swamp/Forest Zone event 03), indicating different design phases.

---

## 5. Lore Elements

### NPCs and Story

- **Shelby** (`_CUT_NPCF_SFZ03_Shelby`, voice type `0x00180AE3`) -- Female NPC, cut. Researcher who studied cryptids and set up the tissue analyzer system. Her terminal (`SFZ03_Queen_ShelbyTerminal`) was the quest-giver.
- **Zack** (`SFZ03_Queen_ZackCorpse`, NPC `0x004FD286`, world ref `0x004FD288`) -- Dead NPC found in the world. Likely Shelby's research partner who didn't survive.

### Written Materials

- `SFZ03_Queen_MiscCabinBook` (`0x00389CC1`) -- Note found at a cabin, world ref placed at `0x00389CC2`
- `SFZ03_Queen_MiscFreddyBook` (`0x00389A86`) -- Note referencing "Freddy" (possibly Freddy Fear's House of Scares connection)
- `SFZ03_Queen_CryptidsSubTerminal` (`0x0000D0BC`) -- Sub-terminal with **five menu entries** (one per cryptid: corresponding to the five ITXT references for Flatwoods Monster, Grafton Monster, Mothman, Snallygaster, Wendigo)
- `SFZ03_Queen_JournalSubTerminal` (`0x001488D5`) -- Sub-terminal with **eight journal entries** (extensive research log)

### Physical Props

- `CUT_SFZ03_Queen_SamplesContainer` (`0x00073CC7`) -- Cooler model (`cooler01.nif`) for storing collected samples
- `SFZ03_Queen_TissueAnalyzer` (`0x005105DC`) -- Tech box (`techbox01a.nif`) used to analyze cryptid tissue
- `SFZ03_Queen_Sample` (`0x0000418D`) -- The tissue sample misc item

---

## 6. Connection to Nuke Zones

Despite not being nuke-triggered itself, the system has indirect connections to the nuke ecosystem:

1. **ImmuneToNukes keyword** on all boss creatures confirms the developers anticipated players might nuke these locations while the event was running. The bosses would survive, but ambient creatures would die.

2. **Geographic overlap:** Boss locations 03 (48,28), 04 (48,18), and 05 (35,20) are in the Cranberry Bog, the same region players nuke for Scorched Earth. Locations 01 (44,42) and 02 (48,36) are in the Mire. There is no evidence of specific "nuke here for cryptid X" zones -- the cryptid assignment was randomized per rotation via the global variables.

3. **Parallel development:** The form ID ranges tell a story. `SFZ03_Queen_BossKeyword` is `0x00004192` (very low range, early development), while `CUT_SFZ03_Queen_MasterQuest` is `0x0043D032` (mid-range, later iteration). The cryptid buff spells are `0x002D0839-0x002D083F` (mid development). This suggests the boss encounter concept existed from early development and was iteratively expanded before being cut.

4. **No blast zone dependency:** Unlike Scorched Earth (which requires nuking a specific fissure site) or A Colossal Problem (which requires nuking Monongah Mine), the SFZ03 system had no nuke prerequisite. The five locations were self-contained encounter zones activated by the daily quest system.

---

## 7. Why It Was Likely Cut

Several factors likely contributed to the system's removal:

1. **Complexity vs. payoff:** The multi-location, multi-stage design required players to travel extensively, fight multiple bosses, harvest samples, and return to an analyzer. For a daily quest, this is a heavy time investment compared to "nuke, fast travel, fight."

2. **Server performance:** Spawning bosses at three of five outdoor locations simultaneously, with wave-based encounters at each, would strain the server more than a single fixed-location event.

3. **Player coordination difficulty:** The nuke system creates a natural coordination mechanism -- everyone sees the nuke and converges. A daily quest spawning at random locations would be harder to organize.

4. **Reward balance:** The cryptid buff system, while interesting, would have created mandatory daily farming for optimal builds. Bethesda has generally avoided combat buffs that require daily grinding.

5. **Streamlined replacement:** CB15_ScorchedEarth achieves the same goal (epic boss fight with group content) in a simpler, more repeatable package.

---

## Complete Record Index

### Keywords (KYWD)
| FormID | EditorID |
|--------|----------|
| `0x00004192` | SFZ03_Queen_BossKeyword |
| `0x00031AB9` | SFZ03_Queen_StartKeyword |
| `0x00073CBA` | SFZ03_Queen_OnQuestKeyword |
| `0x00518904` | SFZ03_Queen_CryptidBossKeyword |
| `0x0043D037` | SFZ03_Queen_CryptidContainerKeyword |
| `0x0043D039` | WaveKeyword_SFZ03Creatures |
| `0x0043D03A` | WaveKeyword_SFZ03CryptidsDay |
| `0x0043D03B` | WaveKeyword_SFZ03CryptidsNight |

### Globals (GLOB)
| FormID | EditorID |
|--------|----------|
| `0x00031A99` | SFZ03_Queen_BossGlobal |
| `0x0043D034` | SFZ03_Queen_CryptidLocation |
| `0x0043D035` | SFZ03_Queen_NormalLocation01 |
| `0x0043D036` | SFZ03_Queen_NormalLocation02 |
| `0x00559E58` | Caps_Daily_SFZ03 |

### Quests (QUST)
| FormID | EditorID |
|--------|----------|
| `0x000451FC` | SFZ03_Queen (child quest -- the actual encounter) |
| `0x0043D032` | CUT_SFZ03_Queen_MasterQuest (orchestrator) |
| `0x00389CC0` | GQ_MiscRegionPointer_SFZ03 (pointer/breadcrumb) |

### Perks (PERK)
| FormID | EditorID | Cryptid |
|--------|----------|---------|
| `0x00007393` | SFZ03_Queen_FlatwoodsPerk | Flatwoods Monster |
| `0x00007394` | SFZ03_Queen_GraftonPerk | Grafton Monster |
| `0x00007395` | SFZ03_Queen_Mothman | Mothman |
| `0x00007396` | SFZ03_Queen_Snallygaster | Snallygaster |
| `0x00007397` | SFZ03_Queen_Wendigo | Wendigo |
| `0x005105EE` | SFZ03_Queen_CryptidPerk | Detection/loot perk |

### Spells (SPEL) and Magic Effects (MGEF)
| FormID | EditorID |
|--------|----------|
| `0x002D0839` | SFZ03_Queen_FlatwoodsBuff |
| `0x002D083A` | SFZ03_Queen_GraftonBuff |
| `0x002D083B` | SFZ03_Queen_MothmanBuff |
| `0x002D083E` | SFZ03_Queen_SnallygasterBuff |
| `0x002D083F` | SFZ03_Queen_WendigoBuff |
| `0x000041A1` | SFZ03_Queen_FlatwoodsEffect |
| `0x000041A2` | SFZ03_Queen_GraftonEffect |
| `0x00007390` | SFZ03_Queen_MothmanEffect |
| `0x00007391` | SFZ03_Queen_SnallygasterEffect |
| `0x00007392` | SFZ03_Queen_WendigoEffect |

### Locations (LCTN)
| FormID | EditorID |
|--------|----------|
| `0x000451FF` | SFZ03_Queen_BossLocation01 |
| `0x00045208` | SFZ03_Queen_BossLocation02 |
| `0x0003BD69` | SFZ03_Queen_BossLocation03 |
| `0x002B5634` | SFZ03_Queen_BossLocation04 |
| `0x002B5639` | SFZ03_Queen_BossLocation05 |

### Location Ref Types (LCRT)
| FormID | EditorID |
|--------|----------|
| `0x0043AF13` | SFZ03_Queen_BossTriggerLocRefType |
| `0x000451FE` | SFZ03_Queen_BossSpawnsLocRefType |

### Wave Types (WAVE)
| FormID | EditorID |
|--------|----------|
| `0x0043D03C` | WaveType_SpecialSFZ03Creatures |
| `0x0043D03D` | WaveType_SpecialSFZ03CryptidsNight |
| `0x0043D03E` | WaveType_SpecialSFZ03CryptidsDay |

### Form Lists (FLST)
| FormID | EditorID |
|--------|----------|
| `0x00031AA8` | CUT_SFZ03_Queen_CreatureKeywords |
| `0x00031AAD` | CUT_SFZ03_Queen_CryptidKeywordsNight |
| `0x0051890B` | CUT_SFZ03_Queen_CryptidKeywordsDay |
| `0x0043D033` | SFZ03_Queen_CorpseContainerList |
| `0x0043D038` | SFZ03_Queen_EWSKeyword |

### Activators and Containers (ACTI/CONT/MISC)
| FormID | EditorID |
|--------|----------|
| `0x0043AF12` | CUT_SFZ03_Queen_BossTrigger |
| `0x005105DC` | SFZ03_Queen_TissueAnalyzer |
| `0x00073CC7` | CUT_SFZ03_Queen_SamplesContainer |
| `0x0000418D` | SFZ03_Queen_Sample |

### Terminals (TERM)
| FormID | EditorID |
|--------|----------|
| `0x00519B9A` | SFZ03_Queen_ShelbyTerminal |
| `0x0000D0BC` | SFZ03_Queen_CryptidsSubTerminal |
| `0x001488D5` | SFZ03_Queen_JournalSubTerminal |

### NPCs (NPC_) and Voice Types (VTYP)
| FormID | EditorID |
|--------|----------|
| `0x004FD286` | SFZ03_Queen_ZackCorpse |
| `0x001EF0C1` | AnnouncerF_SFZ03_Analyzer |
| `0x00180AE3` | _CUT_NPCF_SFZ03_Shelby |

### Books (BOOK)
| FormID | EditorID |
|--------|----------|
| `0x00389CC1` | SFZ03_Queen_MiscCabinBook |
| `0x00389A86` | SFZ03_Queen_MiscFreddyBook |

### World References (WRLD:REFR/ACHR)
| FormID | EditorID |
|--------|----------|
| `0x002BA706` | SFZ03_Queen_BossTrigger01Ref |
| `0x002BA705` | SFZ03_Queen_BossTrigger02Ref |
| `0x002BA704` | SFZ03_Queen_BossTrigger03Ref |
| `0x002BA703` | SFZ03_Queen_BossTrigger04Ref |
| `0x002BA710` | SFZ03_Queen_BossTrigger05Ref |
| `0x002B5643` | SFZ03_Queen_BossMarker01Ref |
| `0x002B5644` | SFZ03_Queen_BossMarker02Ref |
| `0x002B6C5D` | SFZ03_Queen_BossMarker03Ref |
| `0x002BA700` | SFZ03_Queen_BossMarker04Ref |
| `0x002BA70F` | SFZ03_Queen_BossMarker05Ref |
| `0x001488E3` | SFZ03_Queen_StartRef |
| `0x000451F9` | SFZ03_Queen_TerminalRef |
| `0x004FD288` | SFZ03_Queen_ZackCorpseRef |
| `0x00389CC2` | SFZ03_Queen_MiscCabinBookRef |
| `0x0049210C` | SFZ03_Queen_QuestStartRef |
| `0x005105DD` | (Analyzer ref, referenced as ALFR in quest) |

### Cells (WRLD:CELL)
| FormID | EditorID | Grid |
|--------|----------|------|
| `0x00260648` | SFZ03QueenBossCell01 | (44, 42) |
| `0x0026032A` | SFZ03QueenBossCell02 | (48, 36) |
| `0x00260332` | SFZ03QueenBossCell03 | (48, 28) |
| `0x0026033C` | SFZ03QueenBossCell04 | (48, 18) |
| `0x00260D6F` | SFZ03QueenBossCell05 | (35, 20) |

### Other Records
| FormID | Type | EditorID |
|--------|------|----------|
| `0x003D75B8` | LVLI | SFZ03_Queen_Rewards |
| `0x005105E8` | AVIF | DailyQuestAVRegionSwamp_SFZ03_Queen |
| `0x0049210D` | AVIF | SFZ03_Queen_QuestCompletedValue |
| `0x005105EC` | SMQN | SFZ03_Queen_QuestNode |
| `0x0043AC39` | CHAL | Challenge_Lifetime_QuestsCompleted_DailyQuests_Sub_SFZ03_Queen |
| `0x0043AC4D` | FLST | Challenge_Quests_SpecificQuest_Daily_Launch_SFZ03_Queen |
| `0x006312F8` | GMRW | QuestReward_SFZ03_Queen_Stage1000_01 |
