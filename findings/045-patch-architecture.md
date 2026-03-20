# Finding 045: Fallout 76 Patch & Update Architecture -- Complete Analysis

**Analysis Date:** 2026-03-20
**Source:** Actual installed game files, ESM dump (1.6M lines), 5,496 GLOB records, 58,748 GMST records, 3,841 CURV records, 7,095 decompiled scripts
**Game Install:** `/var/home/deucebucket/.local/share/Steam/steamapps/common/Fallout76/`

---

## Executive Summary

Fallout 76 uses a four-layer data architecture that separates what requires a client patch from what can be changed server-side:

1. **Base ESM** (SeventySix.esm, 878 MB) -- The foundation layer containing all record definitions
2. **Update BA2 Archives** (00-12, ~18 GB total) -- Client-side content patches that override base ESM assets
3. **Curve Table JSONs** (~4,262 files) -- Level-scaling formulas packed inside BA2 archives (client-side)
4. **Server-Pushed Globals** (LCP/LTT/Spotlight) -- 5,496 GLOB records, of which ~130 are network-synced and server-writable at runtime

**The critical finding:** Bethesda can change game behavior through three completely different mechanisms, each with different deployment requirements. This is why "hotfixes" and "patches" feel so different to players -- they literally ARE different systems.

---

## 1. The Update Archive System (13 Numbered BA2 Sets)

### Physical Structure

Each update number (00 through 12) ships as a set of up to 4 BA2 files:

| Suffix | Content Type | Example |
|--------|-------------|---------|
| `Main` | Meshes, scripts, materials, misc data | `SeventySix - 12UpdateMain.ba2` (477 MB) |
| `Textures` | DDS textures, normal maps, cubemaps | `SeventySix - 10UpdateTextures.ba2` (2.1 GB) |
| `Voices` | FUZ voice files, lip sync data | `SeventySix - 10UpdateVoices.ba2` (135 MB) |
| `Stream` | Terrain, LOD meshes, streaming data | `SeventySix - 12UpdateStream.ba2` (122 MB) |

Note: Update 00 has no Stream archive. All others have all four types.

### Total Archive Count and Size

52 update BA2 archives spanning updates 00-12, approximately 18 GB total. The base game archives (Meshes, Textures01-10, Sounds, etc.) add another ~30 GB.

### Load Order: How They Layer

The load order is explicitly defined in `Fallout76.ini` under `[Archive]`:

```ini
sResourceArchive2List = SeventySix - 00UpdateMain.ba2, SeventySix - 01UpdateMain.ba2,
  ..., SeventySix - 12UpdateMain.ba2, SeventySix - 01UpdateStream.ba2, ...,
  SeventySix - 12UpdateStream.ba2, SeventySix - 00UpdateTextures.ba2, ...,
  SeventySix - 12UpdateTextures.ba2, SeventySix - 00UpdateVoices.ba2, ...,
  SeventySix - 12UpdateVoices.ba2, SeventySix - StaticMeshes.ba2,
  SeventySix - GeneratedMeshes01.ba2, SeventySix - GeneratedMeshes02.ba2
```

**Key technical detail:** `sResourceArchive2List` is the OVERRIDE list. Archives in this list replace files with matching paths from the base archives (`SResourceArchiveList`). Within `sResourceArchive2List`, **later entries override earlier ones** when they contain files with the same path.

The ordering within the list is: all Main archives (00-12), then all Stream (01-12), then all Textures (00-12), then all Voices (00-12). This means:
- `12UpdateMain.ba2` overrides any file also present in `00UpdateMain.ba2` through `11UpdateMain.ba2`
- `12UpdateTextures.ba2` overrides textures from `00-11UpdateTextures.ba2`
- And so on per category

### Do Newer Archives OVERRIDE Older Ones?

**Yes, confirmed.** The Creation Engine BA2 system uses a last-writer-wins model for loose file paths within archives. When two BA2 archives contain a file at the same internal path (e.g., `meshes/weapons/handmaderifle/handmade_reciever.nif`), the archive listed later in `sResourceArchive2List` wins.

Evidence:
- The ini load order explicitly places 12 after 00-11
- Modded BA2s are appended AFTER the official update archives in `Fallout76Custom.ini`, proving the override pattern (e.g., `EnhancedBlood - Meshes.ba2` at the end overrides vanilla blood meshes)
- Finding 017 showed that NitroRifle animations appeared in Update 11 but were ABSENT from Update 12 -- if 12 had them, they'd override; since 12 doesn't include them, the Update 11 versions persist. This proves partial override (only files that exist in the newer archive override; files unique to older archives remain accessible)

### What Each Update Roughly Corresponds To

Based on file size and content analysis from Finding 017:

| Update | Approx. Era | Notable Content |
|--------|-------------|-----------------|
| 00 | Launch / early patches | Base corrections |
| 01-03 | Wild Appalachia / Nuclear Winter | Early content additions |
| 04 | Wastelanders | NPCs, dialogue, quests (529 MB Main) |
| 05-06 | Steel Dawn / Steel Reign | BOS questline |
| 07 | Expeditions | The Pitt |
| 08 | Nuka-World on Tour | Atlantic City groundwork |
| 09 | Atlantic City | Casino systems |
| 10 | Skyline Valley | Largest update (587 MB Main, 2.1 GB Textures) |
| 11 | Milepost Zero | Cover system prototyped + pulled |
| 12 | The Backwoods | Bigfoot, Bounty Hunts, Rad Hogs |

---

## 2. The ESM and Supporting Files

### SeventySix.esm (878 MB)

The master record database. Contains ALL form definitions: every weapon, NPC, quest, cell, dialogue line, perk, keyword, and global variable. This file defines the STRUCTURE of the game world.

**Critical point:** The ESM is a single monolithic file that gets replaced wholesale with each major patch. There is no "delta" ESM system -- when Bethesda adds a new weapon or changes a damage formula reference, the entire 878 MB ESM is redownloaded.

### SeventySix.cdx (786 KB) -- Cell Distance Index

**Header magic:** `bcdx` (bytes: `62 63 64 78`)

This is a binary index file for the cell (worldspace) loading system. It maps spatial coordinates to cell data, enabling the engine to quickly look up which cells to load based on player position. The regular structure in the hex dump (repeating 16-byte entries with consistent timestamps) confirms this is a spatial index/lookup table, not configuration data.

**Verdict:** Pure client-side spatial optimization data. Not server-tunable. Gets rebuilt/replaced with patches that change world layout.

### SeventySix.bin (137 bytes)

A tiny binary blob (only 137 bytes). At this size, it's almost certainly a hash, checksum, or version identifier for the ESM. The content appears to be a cryptographic hash (high entropy, no readable strings). This likely serves as the version stamp that the client sends to the server during connection handshake to verify ESM version compatibility.

**Verdict:** Version/integrity check file. Replaced with every ESM update.

### NW.esm (27 MB)

The Nuclear Winter (Battle Royale) mode ESM. Still present in the game data despite the mode being officially retired. Contains Babylon-prefixed records and battle royale-specific mechanics (see Finding 016).

---

## 3. GMST Values -- Baked Constants, NOT Server-Tunable

### What They Are

Game Settings (GMST) are engine-level constants defined in the ESM. There are **58,748 lines** in the GMST dump, representing thousands of individual settings that control:

- Combat formulas: `fDamageSneakAttackMult` (4.0), `fVATSPlayerDamageMult`, `fCombatPlayerLimbDamageMult`
- Movement: `fMoveSpeedMultMax` (150.0), `fEvadeUsesAPScale` (30.0)
- Weapon mechanics: `fWeaponConditionJam1-4`, `fWeaponConditionRateOfFire1-9`
- Armor formulas: `fPhysicalArmorBase_NORM` (51.0), `fPhysicalArmorDmgReductionExp_NORM` (0.6377)
- Event parameters: `fFastTravelDelaySeconds` (15.0), `fHoldToReviveHoldTime` (3.0)
- Legendary system: `fLegendaryModShardChance` (0.015 = 1.5%)
- Stagger: `fStaggerCooldownDurationPlayer` (15.0)
- Scope/aiming: `fScopeEnteringFadeInSec` (0.1), `fScopeEnteringFadeOutSec` (0.1)

### Can the Server Override GMST at Runtime?

**No.** GMSTs are baked into the ESM and loaded by the client engine at startup. There is no evidence of a server-to-client GMST override mechanism in the decompiled scripts. The Papyrus scripting layer has no `SetGameSetting()` function -- only `Game.GetGameSettingFloat()`, `Game.GetGameSettingInt()`, and `Game.GetGameSettingString()` (read-only).

The server cannot send different GMST values to different players. There is no A/B testing infrastructure for game settings.

**To change a GMST, Bethesda must:**
1. Modify the ESM in their internal toolset
2. Build a new ESM
3. Push a client patch through Steam/Bethesda.net
4. Players download the ~878 MB ESM + affected BA2 archives

This is why GMST changes (like the armor formula rework that changed `fPhysicalArmorDmgReductionExp_NORM`) only happen in numbered patches, never in hotfixes.

---

## 4. GLOB Values -- The Server-Tunable Layer

### Scale

5,496 GLOB records in the ESM, each containing a float value (FLTV). Of these, **130 have the NTWK (Network) flag**, meaning they are explicitly tagged for server synchronization.

### The Three GLOB Subsystems

#### 4a. LCP (Live Content Package) -- Content Switches

103 GLOB records with `LCP_` prefix. These are master on/off switches for entire features:

- **Seasonal events:** `LCP_E07A_Mothman`, `LCP_E08A_Moonshine`, `LCP_MN2_Mischief`, `Festive_Holiday_Enabled`
- **Quest gating:** `LCP_BURN_SQ01` through `LCP_BURN_SQ04_DirtyLaundry` (The Backwoods quest progression)
- **Mutated events:** 38 individual `MutatedEvents_LCP_*` toggles, one per public event, each with `MutationEnabled` and `DoubleMutationEnabled` variants
- **Feature toggles:** `LCP_Fishing_Axolotl_MonthlyIndex`, `LCP_GHL00_Quest_Enabled`, `MOON_LCP_Toggle`
- **Content gating:** `LCP_SilverBridgePhaseNumber` (progressive content unlock)

**How it works (from script evidence):**
```
; From objectiverandomizer.psc:
"For use with Live Content Packages. Use a unique GlobalVariable in each Mission
for Each Objective. Default value should be 1. Use LCP to set a value of 0 to
remove this objective from randomization"

; From dailymutation.psc:
"The current mutation index -- gets set by the Live Content Scheduler"
```

The server pushes GLOB values on login. Scripts check `GlobalVariable.GetValue()` to determine what content is active.

#### 4b. LTT (Live Tuning Toggle) -- Drop Rate Knobs

29 GLOB records with `LTT_` prefix, always in Toggle + DropRate/ChanceNone pairs:

| Toggle | Paired Value | Purpose |
|--------|-------------|---------|
| `LTT_RA_Rewards_Activities_DoubleLegendaryItem_Toggle` | `_DropRate` (100.0) | Double legendary drops |
| `LTT_DoubleFestiveGift_Toggle` | `_DropRate` (100.0) | Holiday double drops |
| `LTT_IncreasedFasnachtGlowingMaskDrop_Toggle` | `_ChanceNoneDropRate` (90.0) | Fasnacht rare masks |
| `LTT_HeadHunt4StarDrops_Toggle` | `_ChanceNoneDropRate` (100.0) | 4-star bounty drops |
| `LTT_UMineItLegendary_Toggle` | `_ChanceNoneDropRate` + `_Amount` | U-Mine-It legendaries |

**Default state:** All LTT toggles are 0 (off) in the ESM dump. Bethesda enables them server-side during community events.

**ChanceNone inversion:** Higher `ChanceNoneDropRate` values mean FEWER drops. A value of 90 means 90% chance of getting nothing (10% chance of the item). A value of 0 means guaranteed drop.

#### 4c. Spotlight / Economy Globals -- Dynamic Values

Hundreds of GLOB records control specific game parameters:

- **Caps rewards:** `RA_Rewards_Activities_Caps` (75), `RA_Rewards_PublicEvents_Caps` (150), `Burn_Challenges_Caps_0010-0500`
- **XP rewards:** `XP_BURN_SQ01_Reward` (1000), `Burn_MQ03_XPReward` (800), `BURN_SQ04_DirtyLaundry_XP` (1600)
- **Spawn chances:** `SpawnChance_RadhogAlpha` (10%), `RA_PartyCrasherSpawnChance_Default` (34%), `RA_PartyCrasherSpawnChance_Bigfoot` (33%)
- **Event timers:** `Burn_E01_QuestTimer` (900s), `FF08_ProjectBeanstalk_EventTime` (600s), `Burn_BountyHunt_PublicExpiryTimer` (2700s)
- **Level scaling:** `Renorm_MinLVL_Tier13-20`, `Renorm_MinLVL_Boss_GearinUp` (75-85), `Renorm_MinLVL_Boss_JerseyDevil`
- **CAMP limits:** `WorkshopCount_AnimatedDisplays_Camp` (20), `ATX_WorkshopCount_Explosives_CAMP` (25)
- **Resource production:** `ATX_ResourceProductionIntervalHours_Collectron_Peppino` (0.15h = 9 min)
- **Season tracking:** 109 GLOB records with `SCORE_S23_` or `SCORE_S24_` prefixes

### Which GLOBs Actually Change Server-Side?

Based on naming conventions and observed behavior:

**Confirmed server-pushed (change without patches):**
- All `LCP_*` toggles -- seasonal events turn on/off regularly
- All `LTT_*` toggles -- community events (Double XP, increased drops)
- `DailyOps_Mutation_Index` -- changes daily, set by Live Content Scheduler
- `MutatedEvents_LCP_*` -- per-event mutation playlist
- `LCP_Fishing_Axolotl_MonthlyIndex` -- monthly rotation
- Seasonal spawn chances (`Festive_ScorchedSpawnChance`, `Spooky_ScorchedSpawnChance`, `TreasureHunt_SpawnChance`)
- `Burn_BountyHunt_NumOfActivePublicBounties` -- runtime state

**Likely server-pushed but changed rarely:**
- `RA_Rewards_Activities_Caps` / `RA_Rewards_PublicEvents_Caps` -- cap reward tuning
- `RA_Rewards_Activities_LegendaryItem_DropRate` (currently 25%) -- could be tuned for events
- `RA_PartyCrasherSpawnChance_*` -- boss spawn rates during events

**Probably only changed via patches:**
- `Renorm_*` level scaling ranges -- fundamental balance
- `WorkshopCount_*` CAMP limits -- tied to UI code
- `BOUNTY_KillstreakArmorBonus01-10` -- specific numeric progressions
- `SURV_Food_Effect_*` -- survival mode tuning

---

## 5. Curve Table JSONs -- Client-Side, Requires Patch

### Structure

3,841 CURV records in the ESM. Of these:
- **755** reference external JSON files via `:CRVE` subrecord (e.g., `weapons/weap_44dmg.json`)
- **3,079** have `JASF` (JSON Auto-Scale Factor) data embedded directly in the ESM record

The JSON files with `:CRVE` references live inside the BA2 archives at paths like:
```
misc/curvetables/json/weapons/weap_44dmg.json
misc/curvetables/json/armor/armo_combat_arm_dr.json
misc/curvetables/json/crafting/scrapbonusint.json
misc/curvetables/json/itemcondition/conditiondamagescalefactor_weapons_ballistic.json
```

### Are These Server-Sent or Client-Loaded?

**Client-loaded from BA2 archives.** The `CurveTable` Papyrus class (from `curvetable.psc`) only has two methods:

```papyrus
Bool Function HasValueAt(Float afInput) Native
Float Function GetValueAt(Float afInput) Native
```

Both are engine-side lookups against the locally-loaded curve data. There is no `SetCurveValue()`, `LoadRemoteCurve()`, or any network function on the CurveTable class. Scripts reference curve tables by CURV form ID, and the engine resolves them from the local BA2.

**To change weapon damage curves, Bethesda must push a client patch** that includes updated JSON files in an UpdateMain BA2 archive.

### Categories of Curve Tables

| Category | Count | Examples |
|----------|-------|---------|
| Weapon damage (ranged) | ~50 | `weap_44dmg.json`, `weap_handmaderifledmg.json` |
| Weapon damage (melee) | 78 | `weap_supersledgedmg.json`, `weap_chainsawdmg.json` |
| Weapon mods | 169 | `weap_template_mod_fasttrigger.json` |
| Armor DR/ER | 367 | `armo_combat_arm_dr.json` |
| Legendary effects | 108 | Magnitude scaling per level |
| Player XP tiers | ~300 | `CT_Player_XP_Universal_Tier01-100` |
| Creature stats | ~200 | Health, armor, damage per level |
| Item condition | 114 | Durability degradation |

---

## 6. The LiveContentScheduler System -- What It Can Change Without a Patch

### Architecture

The Live Content Scheduler (LCS) is a server-side system that manipulates GLOB values on a schedule. It is NOT part of the Papyrus scripting layer -- it operates at the server engine level, below the script VM.

**What it controls:**

1. **Daily Operations mutation rotation** -- `DailyOps_Mutation_Index` changes daily
2. **Seasonal event activation** -- Fasnacht, Meat Week, Mothman Equinox, Holiday Scorched on/off
3. **Weekly mutation playlists** -- `MutatedEvents_LCP_*_MutationEnabled` for each public event
4. **Monthly rotations** -- `LCP_Fishing_Axolotl_MonthlyIndex` for fishing content
5. **Content unlock gating** -- `LCP_BURN_SQ01` etc. for staggered quest releases
6. **Community event bonuses** -- LTT toggles for Double XP / increased drops
7. **Boss spawn rates** -- Party crasher and seasonal creature spawn chances

### What It CANNOT Change

- Weapon base damage numbers (curve table JSONs in BA2)
- Armor resistance formulas (GMST values baked in ESM)
- Perk card effects (CURV records + OMOD records in ESM)
- New content (meshes, textures, sounds -- require BA2)
- UI layouts (SWF files in BA2)
- Script logic (compiled PEX in BA2)
- NPC stats, inventory templates (ESM records)
- Legendary effect definitions (OMOD records in ESM)

---

## 7. When Bethesda "Nerfs a Weapon" -- Which System Do They Use?

### Scenario Analysis

**Changing base weapon damage (e.g., "The Fixer now does 10% less damage"):**
- Requires modifying `weapons/weap_combatrifledmg.json` (curve table)
- This file is inside a `UpdateMain.ba2` archive
- **Requires a client patch** -- new BA2 download

**Changing a legendary effect magnitude (e.g., "Bloodied bonus reduced from 95% to 80%"):**
- Requires modifying the CURV record for the Bloodied legendary effect
- Either a JASF value in the ESM or a JSON in the BA2
- **Requires a client patch**

**Changing a perk card bonus (e.g., "Demolition Expert rank 5 reduced from 60% to 40%"):**
- Requires modifying the CURV record for the perk's scaling
- **Requires a client patch**

**Changing a game formula constant (e.g., "Sneak attack multiplier reduced from 4x to 3.5x"):**
- Requires modifying `fDamageSneakAttackMult` GMST in the ESM
- **Requires a client patch** (878 MB ESM re-download)

**Changing a drop rate (e.g., "Legendary item drop rate increased during this event"):**
- Flip `LTT_RA_Rewards_Activities_DoubleLegendaryItem_Toggle` from 0 to 1
- **Server-side only** -- no patch needed

**Changing a spawn chance (e.g., "More Festive Scorched this weekend"):**
- Adjust `Festive_ScorchedSpawnChance` GLOB
- **Server-side only** -- no patch needed

**Changing event timers (e.g., "Radiation Rumble now lasts 15 minutes instead of 10"):**
- If timer is a GLOB: server-side change possible
- If timer is hardcoded in script: requires patch with new PEX
- Most event timers in The Backwoods are GLOBs (e.g., `Burn_E01_QuestTimer` = 900s)

**Enabling/disabling a feature (e.g., "Meat Week is now live"):**
- Flip `E02A_Meat_Enabled` from 0 to 1
- **Server-side only** -- no patch needed, happens within seconds

### The "Hotfix" Pattern

When Bethesda announces a "hotfix" vs. a "patch":

| Term | Mechanism | What Can Change |
|------|-----------|-----------------|
| **Patch** | Steam/Bethesda.net download (ESM + BA2) | Everything: new content, damage values, formulas, scripts |
| **Hotfix** | Server-side GLOB push | Drop rates, spawn chances, event toggles, timers (if GLOB-based) |
| **Maintenance** | Server restart with new config | GLOB values, possibly server-side validation rules |

**Weapons are NEVER nerfed via hotfix.** All weapon damage changes require curve table modifications, which require a client patch. This is why weapon balance changes are always in numbered patches, never in "server-side hotfixes."

---

## 8. Patterns in Scripts: Server Config and Dynamic Behavior

### Script Search Results

Searching all 7,095 decompiled scripts for server-side configuration patterns:

| Pattern | Occurrences | Context |
|---------|------------|---------|
| `Live Content Scheduler` | 4 scripts | Explicitly names the server-side scheduling system |
| `Live Content Packages` | 9 references (1 script) | `objectiverandomizer.psc` documents LCP usage |
| `GlobalVariable.GetValue()` | 37+ scripts | Runtime checks against server-pushed globals |
| `ServerSideEventObjects` | 1 script | `debugstevequestscript.psc` (debug only) |
| `SendRMIToServer` | 20 scripts | Client-to-server event notifications |
| `OnSyncVariableNetworkChanged` | 28 scripts | Server-to-client state replication |
| `CurveTable.GetValueAt()` | 20+ scripts | Local curve table lookups (no network) |
| `hot fix` / `runtime override` | 0 | No scripts reference these concepts |
| `server config` / `dynamic config` | 0 | No scripts reference these concepts |
| `A/B test` / `experiment` (non-quest) | 0 | No A/B testing infrastructure |

### Key Script: eventmutationscript.psc

Shows the LCP pattern most clearly:
```papyrus
GlobalVariable Property LCP_MutationEnabled Auto Const mandatory
{ LCP global variable specific to this event indicating whether mutation is
  currently enabled for this event. }
```

The script checks `LCP_MutationEnabled.GetValue()` at runtime. When the server sets this GLOB to 1, the event becomes mutated. When set to 0, it runs normally. No patch needed.

---

## 9. Can the Server Send Different Values to Different Players? (A/B Testing)

**No evidence of A/B testing capability.**

- GLOB records are world-global, not per-player. All players on the same server see the same GLOB values.
- The `NTWK` flag on 130 GLOBs indicates they are network-synchronized, but this means "server pushes to all clients," not "server sends different values per client."
- No `PlayerSpecificGlobal`, `ABTestGroup`, or similar mechanism exists in the Papyrus API.
- No scripts check player ID/group to branch on different GLOB values.
- The `actorvaluetests.psc` test explicitly names `ShouldOnlyWorkOnServer` for player value changes, confirming the one-way push model.

**However**, there is indirect per-player tuning possible:
- Different SERVERS could theoretically run different GLOB configs (not proven, but architecturally possible)
- The PTS (Public Test Server) uses different GLOB values (confirmed by `LCP_E07B_Invaders_PTSEventPlaylist`)
- Per-player state exists through Actor Values and quest stages, but these are gameplay state, not configuration

---

## 10. The zzz_ Prefix Pattern -- Disabled/Deprecated Content

47 GLOB records have `zzz` prefix, indicating deprecated or disabled content:

- `zzzLCP_BURN_E01_Gear` -- Cut Backwoods event
- `zzzLCP_BURN_E02_Sinkhole` -- Cut Backwoods event
- `zzzLCP_Disable_DirtyLaundry` -- Replaced by new toggle
- `zzzBurn_BountyHunty_CapsPrice2Star` -- Old pricing removed
- `zzz_ATX_ResourceProductionIntervalHours_AmmOMatic_resource` -- Old ammo machine rate
- `zzz_MILE_CaravanEscort_BrahminPathing_FailsafeObjectiveTimer` -- Debug timer

These records remain in the ESM but are never referenced by active scripts. The zzz prefix is a Bethesda convention for "soft delete" -- keeping the form ID stable but marking it as unused.

---

## Summary: The Decision Tree

```
When Bethesda wants to change something:

Is it a drop rate, spawn chance, or event toggle?
  YES --> Server-side GLOB push (no patch, instant)

Is it a damage number, armor value, or level scaling curve?
  YES --> Modify curve table JSON in BA2 --> Requires client patch

Is it a formula constant (sneak mult, armor exponent, etc.)?
  YES --> Modify GMST in ESM --> Requires client patch (878 MB)

Is it new content (meshes, textures, sounds, scripts)?
  YES --> New/updated BA2 archive --> Requires client patch

Is it a quest/event that already exists but isn't activated yet?
  YES --> Flip LCP_ GLOB from 0 to 1 --> Server-side (no patch)

Is it enabling a bonus weekend (Double XP, Double Scrip)?
  YES --> Flip LTT_ GLOB --> Server-side (no patch)
```

---

## Data Source Paths

- Game install: `/var/home/deucebucket/.local/share/Steam/steamapps/common/Fallout76/`
- Game INI (archive lists): `Fallout76/Fallout76.ini` line 82
- User INI (with mods): `compatdata/1151340/pfx/drive_c/users/steamuser/Documents/My Games/Fallout 76/Fallout76Custom.ini`
- ESM dump: `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/esm_dump/full_esm_dump.txt`
- GLOB records: `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/esm_dump/GLOB_records.txt`
- GMST records: `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/esm_dump/game_settings.txt`
- CURV records: `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/esm_dump/CURV_records.txt`
- Decompiled scripts: `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/`
- Related findings: 017 (update archives), 026 (live tuning), 028 (damage curves), 030 (live content scheduler), 032 (network architecture), 043 (client prediction)
