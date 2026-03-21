# FO76-DATA

A searchable database of 38,000+ Fallout 76 game data entries extracted from the retail client's own files. Raw data from ESM records, curve table JSONs, BA2 archives, compiled Papyrus scripts, RTTI binary analysis, and dev build string extraction.

**Live site:** [deucebucket.github.io/fo76-data](https://deucebucket.github.io/fo76-data)

## Data Overview

| Category | Entries | Description |
|---|---|---|
| Native Functions | 1,107 | Papyrus VM native functions across 48 classes |
| Perks | 458 | All perk cards with SPECIAL attribute, rank, cost, level req, descriptions |
| Curve Tables | 269 | Raw X/Y scaling data used by the engine for damage, legendary effects, perks, mutations, XP |
| Legendary Effects | 171 | Weapon and armor legendary effects with scaling values and OMOD chain verification |
| Weapons | 152 | Weapons with damage scaling curves (level 1-50), AP cost, fire rate, accuracy, range, ammo |
| Game Settings | 35 | Key GMST values (damage formulas, XP scaling, sneak multipliers) |
| Research Findings | 33 | Verified research documents covering hidden mechanics, dev build analysis, cut content |
| Cut Content | 18 | Verified cut/disabled content entries with ESM record references |
| Mutations | 19 | Every mutation with positive/negative effects and curve data |
| Power Armor | 14 | All PA sets with stat curves |
| Model Renders | 4 | Rendered creature/item models (Wanamingo, Babymingo, Interloper, MechTest) |
| Speculations | 3 | Analysis-based interpretations clearly labeled as speculative |
| C++ Classes (RTTI) | 28,866 | Runtime Type Information from the retail binary — full class hierarchy (lazy-loaded) |
| Scripts | 7,095 | Papyrus script dependency graph nodes (lazy-loaded) |

**Total: 38,244 searchable entries** across 2,102 files.

## Key Data Categories

### Address Library & Engine Internals
28,866 RTTI class names extracted from the retail binary, plus named SFE addresses, engine module maps, and native function bindings. The Papyrus VM's complete native function interface (1,107 functions across 48 classes) is fully mapped.

### Curve Tables
1,898 raw curve table JSON files across 22 categories (legendary mods, weapons, perks, mutations, player stats, creatures, economy, crafting, and more). These are the actual X/Y point arrays the engine feeds to `CurveTable.GetValueAt()`.

**Universal tier system:** Weapons, armor, and legendary effects all reference the same shared tier curve tables rather than having individual per-item curves. A Bloodied Handmade and a Bloodied Gatling Plasma pull from the same `LegendaryModDamage_Bloodied` curve. The tier system scales by level, not by item.

### Network Protocol
DTLS-PSK transport layer analysis, protocol field mapping, snapshot component serialization, and workshop/transport quest protocols. The client connects via WolfSSL with hint "PROJECT_76" and NO_RSA.

### Cut Content & Dev Build Analysis
Content verified as cut, disabled, or dev-only through ESM record analysis, dev build string diffs, and orphaned asset identification. Includes cut quests, disabled NPCs, orphaned voice recordings, and removed systems. Every cut content claim is backed by specific record references.

### Dev Build Comparison
Dev build function lists, source tree paths, debug assert messages, and ESM diffs identifying content added or removed between the development and retail builds.

## Data Status Tags

Every entry carries a verification status. Common tags:

| Status | Meaning |
|---|---|
| **CONFIRMED** | Verified against game files with specific record/file references |
| **BAKED** | Values in GMST, curve table JSONs, or compiled scripts — cannot change without a client patch |
| **SERVER-TUNABLE** | GLOB values with the NTWK flag — server can adjust without patching (130 confirmed) |
| **HYBRID** | Base value baked, but a server-tunable multiplier can modify the effective value |
| **CUT / DEV BUILD ONLY** | Present in files but disabled, orphaned, or only in dev builds |
| **IN GAME** | Active in the current retail build |
| **UNDOCUMENTED** | Functional in-game but not described in any official or community documentation |

See `docs/DATA-TRUST-LEVELS.md` for the full classification.

## Universal Tier System vs. Per-Item Curves

A common misconception is that each weapon or legendary effect has its own unique damage curve. In practice, the engine uses a shared set of tier curves. Multiple items reference the same curve file. For example:

- All "Bloodied" legendary mods reference `LegendaryModDamage_Bloodied.json`
- Weapon base damage is tiered by weapon class, not individually per weapon
- Perk bonuses follow shared magnitude curves per perk rank

Legacy weapons (explosive energy weapons, etc.) persist because no server-side validation checks legendary effect + weapon type combinations. The curves themselves are baked into `SeventySix - Startup.ba2` and remain unchanged across all 12 update archives.

## How to Verify

All claims can be independently verified using publicly available tools:

1. **Get fo76utils** from [GitHub](https://github.com/fo76utils/fo76utils)
2. **Extract curve tables**: `baunpack "SeventySix - Startup.ba2" -- legendarymods`
3. **Dump ESM records**: `esmdump SeventySix.esm` and search for record names
4. **Verify OMOD chains**: find the legendary mod name in ESM → locate its CURV reference → match to the extracted JSON file
5. **Decompile scripts**: use [Champollion](https://github.com/jtljac/Champollion-Linux) on `.pex` files from the script BA2

The curve JSONs are simple X/Y point arrays. The engine interpolates between points using `CurveTable.GetValueAt()`, a local function with no network component.

## Project Structure

```
fo76-data/
├── index.html                # searchable database site (GitHub Pages)
├── data/
│   ├── search_index.json     # primary search index (2,283 entries)
│   ├── rtti_index.json       # C++ classes (28,866 entries, lazy-loaded)
│   ├── scripts_index.json    # script graph (7,095 entries, lazy-loaded)
│   ├── weapons.json
│   ├── perks.json
│   ├── mutations.json
│   ├── armor.json
│   ├── legendary_effects.json
│   ├── legendary_effects_full.json
│   ├── game_settings.json
│   ├── power_armor.json
│   ├── native_functions.json
│   ├── rtti_classes.json
│   ├── script_graph.json
│   ├── special_formulas.json
│   ├── weapon_damage_curves.json
│   ├── legendary_effect_curves.json
│   ├── mutation_curves.json
│   ├── perk_bonus_curves.json
│   ├── xp_curve.json
│   ├── materials_shaders_analysis.json
│   ├── curve_tables/         # 1,898 raw curve table JSONs across 22 categories
│   ├── engine/               # engine analysis, network protocol, RTTI cross-refs
│   ├── dev_build/            # dev build diffs, debug strings, cut content verification
│   ├── atom_shop/            # Atom Shop asset data
│   └── holotape_games/       # holotape game data (Automatron)
├── findings/                 # 49 research documents
├── images/                   # rendered models and visual references
└── docs/
    ├── DATA-TRUST-LEVELS.md
    └── DATA-SOURCE-SPEC.md
```

## Data Sources

All data extracted from the retail Fallout 76 client (Patch 66, The Backwoods). Read-only file analysis — no server interaction, no online exploitation.

| Source | Contents |
|---|---|
| `SeventySix.esm` | Master plugin — all game records (weapons, armor, perks, quests, NPCs, world data) |
| `SeventySix - Startup.ba2` | Curve table JSONs — damage scaling, legendary effects, perk bonuses, XP curves |
| `NW.esm` | Nuclear Winter plugin — battle royale system (removed from gameplay, still ships in client) |
| `.pex` scripts | Compiled Papyrus bytecode — game logic, quest scripts, event handlers |
| `Fallout76.exe` | RTTI class names and vtable layouts from the retail binary |
| `Project76Profile.exe` | Dev build binary — debug strings, assert messages, source tree paths |
| String tables | `.STRINGS`, `.DLSTRINGS`, `.ILSTRINGS` — all localized text |

## Tools Used

- [fo76utils](https://github.com/fo76utils/fo76utils) — ESM parser, BA2 extractor, map renderer
- [Champollion](https://github.com/jtljac/Champollion-Linux) — Papyrus PEX decompiler
- Python — data processing, JSON parsing, index generation
- Custom scripts — BA2 extraction, string table parsing, RTTI extraction, SFE address scanning

## Legal

Educational research. All data extracted from legitimately purchased game files using read-only analysis. No server interaction, no online exploitation, no redistribution of copyrighted assets (textures, audio, models).

Reverse engineering for interoperability and research purposes has legal protection under DMCA Section 1201(f). This project documents how the game works — it does not modify, exploit, or redistribute it.

Fallout 76 is a trademark of Bethesda Softworks LLC. This project is not affiliated with or endorsed by Bethesda, Microsoft, or ZeniMax.

## License

The data and research in this repository are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Share and adapt for any purpose with credit.

The site code (index.html) is released under MIT.
