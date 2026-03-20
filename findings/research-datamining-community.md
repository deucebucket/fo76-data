# Fallout 76 Datamining Community Research

**Date:** 2026-03-20
**Status:** Active research, live service game with regular patches

---

## 1. Key FO76 Dataminers

### Core Community Figures

- **Eckserah** - Programmer and dataminer who maintains the FO76-specific branch of xEdit, colloquially known as "EcksEdit." Participated in the 2019 dataminer AMA on Reddit. Maintains a Champollion fork with FO76 support. One of the most technically skilled members of the community.
- **TheDuchessFlame (Kat)** - Australian data miner who creates guides for farming, events, and food buffs. Maintains theduchessflame.com. Believes knowledge should be freely accessible.
- **Nuka Knights (Skywalka)** - Runs nukaknights.com, the most prolific FO76 datamining article publisher (54+ datamining articles as of March 2026). Has YouTube, X, Facebook, Discord, Instagram, TikTok presence. Publishes PTS datamines within hours/days of PTS patches.
- **Aten_Ra** - Reddit dataminer, participated in the 2019 dataminer AMA.
- **Sole Survivor** - Dataminer, AMA participant.
- **Waffle Cop** - Dataminer, AMA participant.
- **Rynlnk** - Dataminer, AMA participant.
- **AHeroicLlama** - Created Mappalachia, the comprehensive FO76 mapping tool.
- **FWDekker** - Maintains fo76-dumps on GitHub, automated data dump pipeline for every game update.

### Content Creators Who Report on Datamines

- **JuiceHead (u/juicehead2)** - YouTube content creator who reports on datamined findings, particularly Atomic Shop leaks and upcoming content.
- **InnovSurvivalist** - FO76 content creator focused on news, guides, and opinion pieces.

---

## 2. Datamining Tools for FO76

### ESM/Record Exploration

| Tool | Description | Notes |
|------|-------------|-------|
| **EcksEdit (xEdit for FO76)** | Primary ESM browser/editor. Rename xEdit.exe to FO76Edit.exe or use `-fo76` parameter. Eckserah maintains the FO76-specific branch. | Latest builds on the FO76 Datamining Discord. Must update within hours of game patches since ESM format evolves. |
| **NukaCrypt** | Web-based searchable database of FO76 ESM records. Also provides nuke codes and weapon/mod info. | https://nukacrypt.com/ |
| **esmdump (fo76utils)** | CLI tool to list records from ESM files in text or TSV format. | Part of fo76utils suite. |
| **esmview (fo76utils)** | Interactive ESM browser with NIF viewer for objects with MODL references. | Part of fo76utils suite. |

### Archive Extraction (BA2)

| Tool | Description | Notes |
|------|-------------|-------|
| **BSA Browser** | Open-source Bethesda Archive browser/extractor for all Fallout & ES games. | https://www.nexusmods.com/fallout4/mods/17061 |
| **B.A.E. (Bethesda Archive Extractor)** | Popular BA2 extraction tool. | https://www.nexusmods.com/fallout4/mods/78 |
| **Bethesda Archive Manager - Fallout Edition** | FO76-specific archive manager. | https://www.nexusmods.com/fallout76/mods/2182 |
| **Archive2** | Official tool bundled with FO4 Creation Kit. | Works on FO76 BA2 files too. |
| **bsarch (via xEdit)** | BA2 code integrated into xEdit, supports FO76 texture formats. | |

### World/Map Tools

| Tool | Description | Notes |
|------|-------------|-------|
| **Mappalachia** | Complete mapping tool for FO76, generates maps of all entity placements. | https://github.com/AHeroicLlama/Mappalachia |
| **Map76** | Datamined map of every object, resource, vein, and deposit. | https://map76.com/ |
| **render (fo76utils)** | Renders world, cell, or object from ESM files + terrain data + archives. | CLI tool with comprehensive rendering. |

### Audio Extraction

| Tool | Description |
|------|-------------|
| **UnFuzer** | Converts .fuz files to .wav. Since Wastelanders update, FO76 uses Skyrim's .fuz format (xWMA + lip sync metadata) instead of raw xWMA. |
| **FO4/FO76 SFX Conversion Kit** | PowerShell-based bulk extraction and conversion tool. | https://github.com/suglasp/fallout4_fallout76_sfx_conversionkit |

### Rendering & Visualization

| Tool | Description |
|------|-------------|
| **fo76utils** | Full suite: btddump (terrain), cubeview (textures), render (worldspace rendering). Supports FO76 + FO4 + limited Starfield. Linux + Windows binaries auto-built via GitHub Actions. |
| **btddump** | Extracts terrain data from FO76 .BTD files (height maps, land textures, ground cover, terrain color). |

### Script Decompilation

| Tool | Description |
|------|-------------|
| **Champollion** | PEX to Papyrus decompiler. Main repo (Orvid/Champollion) supports FO76. Eckserah maintains a fork with additional FO76 support. CLI-only. |

---

## 3. FO76 vs FO4 File Format Differences

### ESM Files

- FO76 uses the same Creation Engine ESM format family as FO4, but **Bethesda updates the ESM structure frequently** with patches.
- xEdit must be updated within hours of each FO76 patch to correctly parse new record structures.
- **Server-side validation**: The ESM file hash is checked server-side. Modifying ESM files prevents connection to game servers.
- FO76 ESM contains records for items, NPCs, locations, quests, perks, etc. -- same record types as FO4 but with online-specific additions (Atomic Shop items, season rewards, event definitions).

### BA2 Archives

- Same BTDX container format as FO4, with two sub-types:
  - **GNRL** (General): Standard compressed files. Simple extraction.
  - **DX10** (Textures): DirectDraw texture archives. Extraction requires rebuilding DDS headers for texture chunks.
- **Audio format change**: Since the Wastelanders update, FO76 switched from raw xWMA (.xwm) to Skyrim's Fuze format (.fuz), which bundles xWMA audio with lip-sync metadata (.lip).
- FO76 BA2 files are generally larger and more numerous than FO4's due to ongoing content additions.

### Key Structural Differences from FO4

- FO76 has **no loose file loading from Data/** in the traditional sense -- mods must use BA2 archives or custom.ini overrides.
- New record types for online features: Atomic Shop (ATX) entries, Season/SCORE board data, event scheduling, server-side economy references.
- Version detection and format variations within core parsers (particularly ESMFile) handle game-specific record structure differences.

---

## 4. Recent PTS Patch Findings (2025-2026)

### The Backwoods (Patch 66, March 3, 2026)

- Most recent major update. Broke SFE (again).
- Datamining details being published on Nuka Knights.

### Burning Springs (Patch 64, December 2, 2025)

- Second map expansion: southeastern rural Ohio region.
- The Ghoul from the Fallout TV series (Walton Goggins reprising role) with bounty hunting missions.
- Removal of Milepost Zero caravan system; rewards redistributed to Highway Town vendors and seasonal events.
- 3 new events, new enemies.
- PTS datamines on Nuka Knights correctly predicted new Collectrons, collectors, Atomic Shop items.

### Season 24: "Rip Daring and the Cryptids Beyond the Cosmos"

- Datamined from PTS: alien invaders mixed with Appalachian cryptids.
- Glowing 4-star legendary Bigfoot, Mothman with UFO beams.
- Full reward track datamined before release.

### Season 20-23 Rewards

- All season reward tracks datamined from PTS patches before official release.
- Nuka Knights published complete reward lists from PTS data.

### PTS Atomic Shop Datamines

- Regular PTS patches include upcoming Atomic Shop items (cosmetics, C.A.M.P. items, bundles).
- Patch 58 Atomic Shop datamine (January 31, 2025) revealed upcoming store items.
- Skyline Valley (Patch 52) Atomic Shop items accurately predicted from PTS data.

---

## 5. Major Accurate Datamined Leaks

- **Skyline Valley map expansion** (June 2024): Season 17 rewards, Atomic Shop items, new region details all accurately datamined from PTS months before release.
- **Atlantic City Expeditions**: New expedition missions datamined before announcement.
- **The Pitt datamine**: Bear masks and "Lord of the Rings" inspired armor accurately leaked from game files (PCGamesN reported).
- **Season reward tracks**: Every season's complete reward list has been accurately datamined from PTS data before official release. This is essentially 100% reliable.
- **Atomic Shop items**: Consistently accurate -- upcoming cosmetics are found in PTS BA2 archives and ESM records before they hit the live shop.
- **Burning Springs/Ohio expansion**: Content datamined well before the December 2025 release.
- **Milepost Zero removal**: Dataminers correctly predicted the system's removal and reward redistribution.

---

## 6. SFE (Script Framework Extender) Situation

### What SFE Does

- Enables F4SE's Scaleform hook functionality for FO76.
- Required by: Text Chat mod, Perk Loadout Manager, Save Everything.
- Maintained by **Keretus** (GitHub: keretus/sfe).

### Current Status (March 2026): BROKEN

- **The Backwoods patch (March 3, 2026) broke SFE** -- this is noted in your MEMORY.md as well.
- As of March 2026, the DLL (dated February 25, 2026) produces errors: "You are using a newer version of Fallout 76."
- This is a recurring pattern: SFE updates have sometimes been released just before game patches go live, making them immediately obsolete.
- Community frustration with update cadence and communication from the developer.

### Fundamental Challenge

- SFE hooks into the game executable at specific memory addresses.
- Every FO76 patch changes the executable, breaking SFE.
- Unlike F4SE for FO4 (which has a large team and stable game), SFE has a single maintainer for a live service game with frequent patches.
- Nexus Mods page: https://www.nexusmods.com/fallout76/mods/287

---

## 7. Extracting FO76 BA2 Archives

### Tools (in order of recommendation)

1. **BSA Browser** - Most versatile, handles both GNRL and DX10 BA2 types.
2. **B.A.E. (Bethesda Archive Extractor)** - Simple and reliable for GNRL archives.
3. **fo76utils** - CLI tools, best for batch/automated extraction, Linux-native support.
4. **Archive2** (from FO4 CK) - Official Bethesda tool, works on FO76 archives.

### Key Differences from FO4 BA2 Extraction

- **Audio files**: Post-Wastelanders, voice BA2s use .fuz format instead of .xwm. Need UnFuzer to extract usable audio.
- **No loose file support**: FO76 loads from BA2 archives only (with custom.ini override exceptions). You cannot just drop loose files into Data/ like FO4.
- **BA2 load order**: Controlled via Fallout76Custom.ini `sResourceArchive2List` entries. A load order tool exists on Nexus.
- **Texture BA2s (DX10)**: Require DDS header reconstruction during extraction -- same as FO4 but important to note.

### Extraction Process

```
1. Locate BA2 files in Fallout 76/Data/
2. Open with BSA Browser or B.A.E.
3. For GNRL archives: direct extraction works
4. For DX10 archives: tool handles DDS header reconstruction
5. For audio .fuz files: run through UnFuzer to get .wav + .lip
6. For ESM data: use xEdit (FO76Edit mode) or fo76utils esmdump
```

---

## 8. FO76 Papyrus Scripts vs FO4

### Key Differences

| Aspect | Fallout 4 | Fallout 76 |
|--------|-----------|------------|
| **Source files (.psc)** | Available at `Data/Scripts/Source/` | **Not publicly available** -- no .psc distribution |
| **Compiled scripts (.pex)** | In BA2 archives | In BA2 archives |
| **Decompilation** | Champollion works well | Champollion supports FO76 (main repo + Eckserah fork) |
| **New properties** | DebugOnly, BetaOnly | Same + online-specific extensions |
| **Script execution** | Client-side | **Split: some client-side, some server-side** |
| **Modding** | Full Papyrus modding via CK | **Cannot create new Papyrus mods** -- no CK, no compiler access |

### What This Means for Datamining

- FO76 .pex files CAN be extracted from BA2 archives and decompiled with Champollion.
- However, many game logic scripts execute server-side and are **not included in client files at all**.
- Client-side scripts handle UI, visual effects, some quest stage tracking, and local game logic.
- Server-side scripts handle loot generation, economy, player inventories, combat resolution, and anti-cheat.

---

## 9. Client-Side vs Server-Side Data

### What's Client-Side (CAN analyze)

- **ESM records**: Item definitions, NPC data, location data, quest structures, perk cards, recipe definitions, dialogue trees, world cell data
- **BA2 archives**: Textures, meshes (NIF), audio, animations, UI assets (SWF), Papyrus scripts (.pex)
- **Terrain data**: BTD files (height maps, land textures, ground cover)
- **Atomic Shop definitions**: ATX item records, preview images, pricing structures
- **Season/SCORE board**: Reward definitions, challenge requirements
- **Configuration**: INI defaults, shader parameters

### What's Server-Side (CANNOT analyze)

- **Loot tables/drop rates**: Actual probability tables for legendary drops, rare items
- **Economy balancing**: Vendor cap amounts, trade restrictions, currency generation rates
- **Player inventory data**: All character data stored server-side
- **Anti-cheat logic**: Detection algorithms, ban criteria
- **Event scheduling**: When seasonal/daily events trigger
- **Server-side Papyrus scripts**: Core game logic that runs on Bethesda's servers
- **Matchmaking/instancing**: Server selection, world instance management
- **Real-time balancing**: Bethesda can adjust values without client patches

### The Gray Area

- Some data exists client-side but is overridden/validated server-side (e.g., item stats appear in ESM but server has final authority).
- PTS patches sometimes include server-side data that wouldn't normally be in client builds (accidental leaks).
- Challenge/achievement definitions are client-side but completion tracking is server-side.

---

## 10. FO76 Modding Scene

### What's Allowed (Unofficially Tolerated)

- **Custom INI tweaks**: Fallout76Custom.ini is the primary modding vector. Performance tweaks, visual settings, keybinds.
- **Texture replacements**: Via BA2 archives loaded through custom.ini. Widely used, very rarely (if ever) results in bans.
- **HUD/UI mods**: Interface replacements, inventory sorting, better crafting menus.
- **Photo mode enhancements**: Extended range, additional filters.
- **SFE-dependent mods**: Text chat, perk loadout manager (when SFE works).

### What Will Get You Banned

- ESM modifications (server checks the hash)
- Speed hacks, teleportation, item duplication
- Anything that modifies server-validated gameplay data
- Third-party injection tools that aren't SFE

### Key Modding Tools

- **Fallout 76 Quick Configuration**: INI editor + mod manager (Nexus)
- **Auto Custom INI**: Automatically generates Fallout76Custom.ini based on installed mods
- **Custom INI Generator and Editor**: Includes load order management
- **BA2 Archive Load Order tool**: Manages sResourceArchive2List entries

### Bethesda's Stance

- Bethesda has **never officially confirmed** whether client-side mods are allowed or banned.
- Todd Howard once said official mod support was "coming" -- six years later, Bethesda played this down (GamesRadar, 2024).
- No private server mod support has materialized despite years of requests.
- Community consensus: texture/UI mods are safe; anything touching gameplay is risky.

---

## 11. Community-Maintained Databases

| Resource | URL | Description |
|----------|-----|-------------|
| **NukaCrypt** | https://nukacrypt.com/ | Searchable datamined ESM records, nuke codes, weapon/mod info |
| **Map76** | https://map76.com/ | Datamined map of every object, resource vein, and deposit |
| **FED76** | https://fed76.info/ | Plan Collectors database, pricing guides, legendary trading info, community links |
| **fo76-dumps** | https://github.com/FWDekker/fo76-dumps | Automated data dumps for every game update, created via Python + xEdit + ba2extract |
| **Mappalachia** | https://github.com/AHeroicLlama/Mappalachia | Open-source map generation tool for all FO76 entities |
| **Nuka Knights** | https://nukaknights.com/ | Event dates, datamining articles, build guides, insider articles |
| **fo76utils** | https://github.com/fo76utils/fo76utils | Rendering, extraction, and visualization tools |
| **Fallout Wiki** | https://fallout.fandom.com/ and https://fallout.wiki/ | Community wiki with datamined information integrated |
| **FalloutBuilds** | https://www.falloutbuilds.com/fo76/ | Build calculator, news, resource maps |
| **fo76map.com / MapGenie** | Via MapGenie app | Interactive map with hundreds of location categories |

---

## 12. How PTS Data Leaks Happen

### The PTS Pipeline

1. **Bethesda pushes PTS update** to Steam (separate app: "Fallout 76 Public Test Server").
2. **PTS client downloads full game files** including updated ESM, BA2 archives, and sometimes files not intended for the PTS build.
3. **Dataminers diff the files** against the previous PTS or live build.
4. **ESM records are parsed** via xEdit/EcksEdit -- new items, quests, ATX shop entries, season rewards are immediately visible.
5. **BA2 archives are extracted** -- new textures, meshes, audio, and UI assets reveal upcoming cosmetics and content.
6. **Findings are published** on Discord, Nuka Knights, Reddit, Twitter/X within hours.

### Why PTS Leaks Are So Reliable

- PTS builds contain **complete content** even if it's not activated in the PTS gameplay.
- Atomic Shop items are added to ESM records before they appear in the shop rotation.
- Season reward tracks are fully defined in ESM data before the season launches.
- New world spaces, quests, and NPCs are in the client files even if the PTS only tests specific features.
- Bethesda occasionally includes **more data than intended** in PTS builds (accidental server-side data in client files).

### Datamine Publication Flow

```
PTS Patch → Steam Download → File Diff → xEdit/BA2 Extraction →
Discord (hours) → Nuka Knights Articles (hours-days) →
YouTube/Reddit (days) → General Gaming Press (days-weeks)
```

---

## 13. Key Communities for FO76 Datamining

### Discord Servers

| Server | Members | Focus |
|--------|---------|-------|
| **Fallout 76 Datamining** | 6,400+ | Teaching datamining, tool distribution, EcksEdit releases |
| **Fallout 76** (main) | 105,000+ | General community, datamine discussion |
| **Nuka Knights** | Active | Datamining articles, event tracking |

**Invite link**: https://discord.com/invite/fo76datamining

### Subreddits

| Subreddit | Focus |
|-----------|-------|
| **r/fo76** | Main FO76 subreddit, datamine posts are common |
| **r/fo76FilthyCasuals** | Casual community, datamine news shared |
| **r/Market76** | Trading, uses datamined item data |

### Websites

- **nukaknights.com** - Most prolific datamining article publisher
- **theduchessflame.com** - Guides and datamined content
- **fed76.info** - Community hub, tools aggregator, plan databases
- **nukacrypt.com** - Searchable datamined records
- **fallout.fandom.com** / **fallout.wiki** - Wiki with datamined info integrated

### Forums

- **Steam Community Discussions** (Fallout 76)
- **Bethesda.net Forums** (less active since Steam migration)

---

## 14. Game Update Distribution

### Update Schedule

- ~4 major updates per year (spring, summer, autumn, winter).
- Each major update followed by a supporting hotfix patch.
- PTS opens weeks before major updates.

### How Patches Are Distributed

- **Platform**: Steam (PC), with separate PTS app.
- **Patch sizes**: Typically 15GB+ for major updates. Bethesda does NOT use efficient delta patching -- patches often re-download entire BA2 archives even for small changes.
- **Files that change**: SeventySix.esm (main ESM), various BA2 archives (textures, meshes, audio, scripts), the game executable (Fallout76.exe).
- **Executable changes**: Every patch changes the executable, which is why SFE breaks with every update.

### What Dataminers Track Between Patches

- ESM record diffs (new/modified/deleted records)
- New BA2 archive contents
- Executable size/hash changes
- PTS-to-live differences (what was cut or changed)

### FWDekker's fo76-dumps Automation

- Python script runs xEdit + ba2extract after each patch.
- Creates standardized data dumps as GitHub release attachments.
- New release for every game update -- provides a historical record of all changes.

---

## 15. FO76-Specific Python Tools & Libraries

### bethesda-structs (PyPI)

```
pip install bethesda-structs
```

- Python library for reading BA2 (BTDX) archives and ESM plugin files.
- Supports GNRL and DX10 BA2 sub-types.
- Can parse ESM record structures programmatically.
- Documentation: https://bethesda-structs.readthedocs.io/
- GitHub: https://github.com/stephen-bunn/bethesda-structs
- **Note**: Last updated 2020 (v0.1.4) -- may need patches for latest FO76 ESM format changes.

### fo76-dumps Pipeline (Python + xEdit)

- GitHub: https://github.com/FWDekker/fo76-dumps
- Python script that automates xEdit data extraction and ba2extract.
- Creates standardized dumps for each game update.
- Best reference for building your own automated extraction pipeline.

### fo76utils (C++ with Python bindings)

- GitHub: https://github.com/fo76utils/fo76utils
- Building with `pymodule=1` creates Python bindings to libfo76utils.
- Supports ESM parsing, BA2 extraction, NIF rendering, terrain data extraction.
- Linux + Windows, auto-built binaries via GitHub Actions.

### FO4/FO76 SFX Conversion Kit (PowerShell)

- GitHub: https://github.com/suglasp/fallout4_fallout76_sfx_conversionkit
- PowerShell-based bulk audio extraction and conversion.
- Native BA2 processing in PowerShell code.
- Converts to WAV or MP3.

### Other Relevant Projects

- **Champollion** (C++): PEX decompiler, supports FO76. https://github.com/Orvid/Champollion
- **Caprica** (C++): Papyrus compiler (FO4-focused but relevant). https://www.nexusmods.com/fallout4/mods/7380
- **Open Papyrus**: Community Papyrus documentation project. https://open-papyrus.github.io/

---

## Summary: What's Actionable for GameCryptids

### Immediately Useful

1. **fo76-dumps** provides historical data dumps for every patch -- great for tracking changes over time.
2. **fo76utils** is the most comprehensive CLI toolkit and has Linux binaries.
3. **bethesda-structs** Python library enables programmatic BA2/ESM parsing.
4. **Champollion** can decompile FO76 .pex scripts (client-side ones at least).
5. **EcksEdit** from the Datamining Discord is the go-to for interactive ESM exploration.

### Limitations

1. Server-side data (loot tables, economy, combat resolution) is inaccessible.
2. ESM format changes with every patch -- tools need constant updates.
3. No official mod support or CK for FO76 -- can't create new Papyrus scripts.
4. SFE is perpetually broken by patches -- not reliable for any workflow.
5. Bethesda's unofficial tolerance of client-side mods could change at any time.

### Best Approach for FO76 Datamining

```
1. Join the FO76 Datamining Discord for EcksEdit and community support
2. Set up fo76utils for CLI extraction on Linux
3. Use bethesda-structs for Python-based programmatic access
4. Monitor fo76-dumps releases for automated patch diffs
5. Follow Nuka Knights for PTS datamine articles
6. Extract and decompile client-side Papyrus scripts with Champollion
7. Use NukaCrypt for quick record lookups without local tools
```

---

## Sources

- [Fallout Wiki: Datamining Resources](https://fallout.fandom.com/wiki/Resources:Datamining)
- [Fallout Wiki: Datamining Tools](https://fallout.wiki/wiki/Resource:Datamining_tools)
- [Nuka Knights: Datamining Articles](https://nukaknights.com/articles/datamining/)
- [FO76 Datamining Discord](https://discord.com/invite/fo76datamining)
- [FED76: Awesome FO76 Tools](https://fed76.info/i/awesome-fallout76-tools/)
- [fo76utils on GitHub](https://github.com/fo76utils/fo76utils)
- [fo76-dumps on GitHub](https://github.com/FWDekker/fo76-dumps)
- [Mappalachia on GitHub](https://github.com/AHeroicLlama/Mappalachia)
- [bethesda-structs on PyPI](https://pypi.org/project/bethesda-structs/)
- [SFE on Nexus Mods](https://www.nexusmods.com/fallout76/mods/287)
- [SFE on GitHub (Keretus)](https://github.com/keretus/sfe)
- [Champollion on GitHub](https://github.com/Orvid/Champollion)
- [NukaCrypt](https://nukacrypt.com/)
- [Map76](https://map76.com/)
- [FED76](https://fed76.info/)
- [BSA Browser on Nexus](https://www.nexusmods.com/fallout4/mods/17061)
- [B.A.E. on Nexus](https://www.nexusmods.com/fallout4/mods/78)
- [Fallout Wiki: BSA File Format](https://fallout.fandom.com/wiki/BSA_file)
- [Fallout Wiki: Papyrus](https://fallout.fandom.com/wiki/Papyrus)
- [Burning Springs Update (Fallout Wiki)](https://fallout.fandom.com/wiki/Burning_Springs_(update))
- [GamesRadar: Bethesda Plays Down FO76 Mod Support](https://www.gamesradar.com/games/fallout/6-years-later-bethesda-says-fallout-76-mod-support-wont-happen-despite-todd-howard-saying-its-coming/)
- [Steam Community: SFE Discussion](https://steamcommunity.com/app/1151340/discussions/0/4030222834115048178/)
- [Nuka Knights: Burning Springs PTS Datamine](https://nukaknights.com/articles/datamining-new-collectors-and-collectron-burning-springs-pts-update-2nd-oct-2025.html)
- [FO76 Season 24 Datamine Breakdown](https://www.u4gm.com/fallout-76/blog-fallout-76-season-24-rip-daring-and-the-cryptids-beyond-the-cosmos)
