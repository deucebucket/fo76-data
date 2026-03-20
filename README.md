# FO76-DATA

A searchable database of 38,000+ Fallout 76 game data entries extracted directly from the game's own files. No guesswork, no wiki estimates — raw data from ESM records, curve table JSONs, BA2 archives, Papyrus scripts, and RTTI binary analysis.

**Live site:** [deucebucket.github.io/fo76-data](https://deucebucket.github.io/fo76-data)

## What's In Here

| Category | Entries | Description |
|---|---|---|
| Research Findings | 91 | Deep-dive documents covering cut content, hidden mechanics, removed features, lore analysis, and game architecture |
| Curve Tables | 269 | Raw X/Y scaling data the engine uses for damage, legendary effects, perks, mutations, XP, and more |
| Weapons | 153 | Every weapon with full damage scaling curves (level 1-50), AP cost, fire rate, accuracy, range, ammo type |
| Perks | 458 | All perk cards with SPECIAL attribute, rank, cost, level requirement, descriptions |
| Legendary Effects | 171 | Weapon and armor legendary effects with exact scaling values, curve file references, and OMOD chain verification |
| Mutations | 19 | Every mutation with positive/negative effects and curve data |
| Native Functions | 1,107 | Papyrus VM native functions across 48 classes — the API between scripts and the engine |
| C++ Classes (RTTI) | 28,866 | Runtime Type Information extracted from the retail binary — the full C++ class hierarchy |
| Scripts | 7,095 | Papyrus script dependency graph nodes |
| Power Armor | 14 | All PA sets with stat curves |
| Game Settings | 35 | Key GMST values (damage formulas, XP scaling, sneak multipliers, etc.) |

**Total: 38,278 searchable entries**

## Key Findings

Some of the data here contradicts what's on the wiki and in community guides. Everything below is verified against the actual game files with full OMOD → CURV → JSON reference chain tracing:

- **Bloodied** scales to **+130% at 5% HP** (wiki says 80-95%)
- **Nocturnal** has **no daytime penalty** — +0% day, +50% night (wiki says -50% day)
- **Junkie's** scales to **+100% at 10 addictions** (community says cap is +50% at 5)
- **Cavalier** gives **41% DR at 5 pieces** vs Sentinel's **23%** — nearly 2x better
- **Nerd Rage** scales continuously to **+80% at 5% HP** (wiki says flat +20%)
- **Gourmand's** maxes at **+40%** not +24%
- DR formula is **dmg²/(dmg+DR)** — confirmed from GMST
- INT XP bonus is exactly **3% per point**

These values are baked into `SeventySix - Startup.ba2` and have never been overridden by any of the 12 update archives. The server can't change them without pushing a patch.

## Research Highlights

The findings documents cover:

- **Nuclear Winter (Babylon)** — the entire battle royale system is still in the client files. 3,589 string entries, complete matchmaking, perk cards, Vault 51 storyline. None of it was cleaned out.
- **Bot Framework** — `SetAIDriven()` function in the base Player class. Full bot infrastructure with 763 native C++ functions mapped. Headless client capability built into the engine.
- **Cut Dialogue** — 3+ hours of recovered Beckett dialogue reconstructing his original storyline. The Fisherman character's full script stage directions revealing fish-human hybrid with telepathic abilities.
- **Wanamingo** — animation skeleton found in the animation archive. The Fallout 2 creature was planned for FO76.
- **Legacy Weapons** — persist because zero server-side validation exists for legendary effect + weapon type combinations. A fix was built but never deployed.
- **Live Content Scheduler** — three-layer system (LCP/LTT/Spotlight) for seasonal content, with 130 server-tunable GLOB values.
- **Hidden Mechanics** — exact AP costs per weapon class, armor DR tiers, mutation stacking math, critical hit formulas, and the complete damage pipeline.
- **DTLS-PSK Protocol** — client connects using WolfSSL with hint "PROJECT_76" and NO_RSA.
- **CDX Spatial Index** — 50,283 cell records in a 16x16 grid streaming system.

## Data Sources

All data extracted from the retail Fallout 76 client (Patch 66, The Backwoods). No server interaction, no online exploitation — read-only file analysis.

| Source | What It Contains |
|---|---|
| `SeventySix.esm` | Master plugin — all game records (weapons, armor, perks, quests, NPCs, world data) |
| `SeventySix - Startup.ba2` | Curve table JSONs — damage scaling, legendary effects, perk bonuses, XP curves |
| `NW.esm` | Nuclear Winter plugin — complete battle royale system (removed from gameplay but still ships) |
| `.pex` scripts | Compiled Papyrus bytecode — game logic, quest scripts, event handlers |
| `Fallout76.exe` | RTTI class names and vtable layouts extracted from the retail binary |
| String tables | `.STRINGS`, `.DLSTRINGS`, `.ILSTRINGS` — all localized text |

### Data Trust Levels

- **BAKED**: Values in GMST, curve table JSONs, compiled scripts — cannot change without a client patch
- **SERVER-TUNABLE**: 130 GLOB values with the NTWK flag — server can adjust these without patching

See `docs/DATA-TRUST-LEVELS.md` for the full classification.

## How to Verify

You don't have to take my word for any of this. Here's how to check yourself:

1. **Get fo76utils** from [GitHub](https://github.com/fo76utils/fo76utils) (compiles on Linux, Windows builds available via GitHub Actions)
2. **Extract curve tables**: `baunpack "SeventySix - Startup.ba2" -- legendarymods`
3. **Dump ESM records**: `esmdump SeventySix.esm` and grep for the record names
4. **Verify OMOD chains**: search the ESM dump for the legendary mod name → find the CURV reference → match to the JSON file

The curve JSONs are simple X/Y point arrays. The engine interpolates between them using `CurveTable.GetValueAt()`, which is a local function with no network component.

## Tools Used

- [fo76utils](https://github.com/fo76utils/fo76utils) — ESM parser, BA2 extractor, map renderer
- [Champollion](https://github.com/jtljac/Champollion-Linux) — Papyrus PEX decompiler
- Python — data processing, JSON parsing, SQLite population
- Custom scripts — BA2 extraction, string table parsing, RTTI extraction, SFE address scanning

## Project Structure

```
fo76-data/
├── index.html              # searchable database site (GitHub Pages)
├── data/
│   ├── search_index.json   # primary search index (2,317 entries)
│   ├── rtti_index.json     # C++ classes (28,866 entries, lazy-loaded)
│   ├── scripts_index.json  # script graph (7,095 entries, lazy-loaded)
│   ├── weapons.json        # weapon database
│   ├── perks.json          # perk database
│   ├── mutations.json      # mutation database
│   ├── legendary_effects.json      # legendary effects from DB
│   ├── legendary_effects_full.json # full legendary data with curves
│   ├── game_settings.json  # GMST values
│   ├── power_armor.json    # PA sets
│   ├── native_functions.json       # Papyrus native function map
│   ├── rtti_classes.json   # full RTTI class hierarchy
│   ├── script_graph.json   # script dependency graph
│   ├── weapon_damage_curves.json
│   ├── legendary_effect_curves.json
│   ├── mutation_curves.json
│   ├── perk_bonus_curves.json
│   ├── xp_curve.json
│   ├── special_formulas.json
│   └── curve_tables/       # 917 raw curve table JSONs
│       ├── legendarymods/  # 108 legendary effect curves
│       ├── weapons/        # weapon damage curves
│       ├── perks/          # perk bonus curves
│       ├── mutations/      # mutation effect curves
│       └── player/         # player stat curves (XP, HP, AP, etc.)
├── findings/               # 91 research documents
│   ├── 001-nuclear-winter-code-intact.md
│   ├── 002-atlantic-city-casino-system.md
│   ├── ...
│   ├── 087-rtti-vtable-mapping.md
│   └── research-*.md       # compiled reference documents
└── docs/
    ├── DATA-TRUST-LEVELS.md
    └── DATA-SOURCE-SPEC.md
```

## The Site

Single-page static site with:
- **Fuse.js** fuzzy search across all 38,000+ entries
- **Category filters** with counts
- **Expandable cards** showing human-readable details (not raw hex dumps)
- **Lazy loading** for large datasets (C++ classes and scripts load on-demand)
- **URL hash routing** for deep-linking to categories
- **Terminal/Pip-Boy aesthetic** because obviously

The RTTI classes (28,866) and scripts (7,095) are loaded on-demand when you click their filter buttons — keeps the initial page load fast.

## Legal

This is educational research. All data was extracted from legitimately purchased game files using read-only analysis. No server interaction, no online exploitation, no redistribution of copyrighted assets (textures, audio, models).

Reverse engineering for interoperability and research purposes has legal protection under DMCA Section 1201(f). This project documents how the game works — it doesn't modify, exploit, or redistribute it.

Fallout 76 is a trademark of Bethesda Softworks LLC. This project is not affiliated with or endorsed by Bethesda, Microsoft, or ZeniMax.

## License

The data and research in this repository are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You can share and adapt it for any purpose as long as you give credit.

The site code (index.html) is released under MIT.
