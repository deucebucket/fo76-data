# Finding 075: Papyrus VM Analysis & Bytecode Tooling

**Date:** 2026-03-20
**Category:** Tooling / Reverse Engineering
**Priority:** High — foundational tooling for script-level game analysis

---

## Summary

Built a complete Papyrus .pex bytecode parser, disassembler, and dependency graph builder
for Fallout 76. Successfully parsed all 7,165 client-side .pex scripts with zero errors.
Key discovery: FO76 client scripts contain only ~17,647 bytecode instructions across 771
scripts — the vast majority of game logic (damage calculations, perk stacking, legendary
effects) runs server-side and is NOT in the client .pex files.

---

## PEX Binary Format (FO76 Variant)

### Header
| Field | Type | FO76 Value | Notes |
|-------|------|------------|-------|
| Magic | uint32 LE | 0xFA57C0DE | Bytes on disk: `DE C0 57 FA` |
| Major Version | uint8 | 3 | |
| Minor Version | uint8 | 15 | FO76 uses 3.15 (unique to FO76) |
| Game ID | uint16 LE | 3 | 1=Skyrim, 2=FO4, 3=FO76, 4=Starfield |
| Compilation Time | uint64 LE | varies | Unix timestamp |
| Source File | wstring | path | Build server path (e.g., `E:\BuildAgent\work\...`) |
| Username | wstring | "builds" | Always "builds" for FO76 |
| Machine Name | wstring | varies | e.g., "RKVBGSBUILD37" |

### Key Format Differences from Skyrim
- **Endianness:** FO76/FO4 use **little-endian** throughout; Skyrim uses big-endian
- **Object const flag:** Extra uint8 in object header (not present in Skyrim)
- **Variable const flag:** Extra uint8 after each variable's default value (not in Skyrim)
- **Struct definitions:** New section in object body (not in Skyrim)
- **Debug info extensions:** Property groups + struct orders sections after debug functions
- **New opcodes:** 0x24-0x2E from FO4, 0x2F potentially FO76-specific

### Complete Opcode Table

| Code | Name | Args | Description |
|------|------|------|-------------|
| 0x00 | nop | 0 | No operation |
| 0x01 | iadd | 3 | dest = a + b (int) |
| 0x02 | fadd | 3 | dest = a + b (float) |
| 0x03 | isub | 3 | dest = a - b (int) |
| 0x04 | fsub | 3 | dest = a - b (float) |
| 0x05 | imul | 3 | dest = a * b (int) |
| 0x06 | fmul | 3 | dest = a * b (float) |
| 0x07 | idiv | 3 | dest = a / b (int) |
| 0x08 | fdiv | 3 | dest = a / b (float) |
| 0x09 | imod | 3 | dest = a % b (int) |
| 0x0A | not | 2 | dest = !src |
| 0x0B | ineg | 2 | dest = -src (int) |
| 0x0C | fneg | 2 | dest = -src (float) |
| 0x0D | assign | 2 | dest = src |
| 0x0E | cast | 2 | dest = (type)src |
| 0x0F | cmp_eq | 3 | dest = (a == b) |
| 0x10 | cmp_lt | 3 | dest = (a < b) |
| 0x11 | cmp_lte | 3 | dest = (a <= b) |
| 0x12 | cmp_gt | 3 | dest = (a > b) |
| 0x13 | cmp_gte | 3 | dest = (a >= b) |
| 0x14 | jmp | 1 | Unconditional jump (relative) |
| 0x15 | jmpt | 2 | Jump if true |
| 0x16 | jmpf | 2 | Jump if false |
| 0x17 | callmethod | 3+varargs | obj.method(args...) |
| 0x18 | callparent | 2+varargs | parent.method(args...) |
| 0x19 | callstatic | 3+varargs | Class.method(args...) |
| 0x1A | return | 1 | Return value |
| 0x1B | strcat | 3 | dest = str1 + str2 |
| 0x1C | propget | 3 | dest = obj.Property |
| 0x1D | propset | 3 | obj.Property = value |
| 0x1E | array_create | 2 | dest = new Type[size] |
| 0x1F | array_length | 2 | dest = array.Length |
| 0x20 | array_getelement | 3 | dest = array[index] |
| 0x21 | array_setelement | 3 | array[index] = value |
| 0x22 | array_findelement | 4 | array.Find(val, start) |
| 0x23 | array_rfindelement | 4 | array.RFind(val, start) |
| 0x24 | is | 3 | dest = (obj is Type) — FO4+ |
| 0x25 | struct_create | 1 | dest = new StructType — FO4+ |
| 0x26 | struct_get | 3 | dest = struct.Member — FO4+ |
| 0x27 | struct_set | 3 | struct.Member = value — FO4+ |
| 0x28 | array_findstruct | 5 | Find struct in array — FO4+ |
| 0x29 | array_rfindstruct | 5 | Reverse find struct — FO4+ |
| 0x2A | array_add | 3 | array.Add(val, count) — FO4+ |
| 0x2B | array_insert | 3 | array.Insert(val, idx) — FO4+ |
| 0x2C | array_removelast | 1 | array.RemoveLast() — FO4+ |
| 0x2D | array_remove | 3 | array.Remove(idx, count) — FO4+ |
| 0x2E | array_clear | 1 | array.Clear() — FO4+ |
| 0x2F | array_getallmatchingstructs | 6 | Filter struct array — FO76? |

### Value Types (Instruction Operands)
| Code | Type | Payload |
|------|------|---------|
| 0 | None/Null | No data |
| 1 | Identifier | uint16 string table index (variable/function name) |
| 2 | String | uint16 string table index (literal constant) |
| 3 | Integer | int32 signed |
| 4 | Float | float32 IEEE 754 |
| 5 | Boolean | uint8 (0 or 1) |

---

## Aggregate Statistics (All 7,165 FO76 Client Scripts)

| Metric | Value |
|--------|-------|
| Total .pex files parsed | 7,165 |
| Parse errors | 0 |
| Scripts with bytecode | 771 (10.8%) |
| Total bytecode instructions | 17,647 |
| Total function definitions | 3,976 |
| Native functions (engine-provided) | 1,107 |
| Struct definitions | 560 |
| Unique event types handled | 166 |
| Total event handlers | 1,607 |
| Max inheritance depth | 7 |
| PEX version | 3.15 (all files) |
| Game ID | 3 (all files — FO76) |
| Build user | "builds" (all files) |

### Opcode Usage Distribution
```
callmethod        4,773  (27.0%)    — Instance method calls dominate
jmpf              2,318  (13.1%)    — Conditional branches
cast              2,251  (12.8%)    — Type casts (very frequent)
jmp               2,007  (11.4%)    — Unconditional jumps
assign            1,049   (5.9%)    — Variable assignment
cmp_eq              995   (5.6%)    — Equality checks
callstatic          845   (4.8%)    — Static/global calls
return              461   (2.6%)    — Function returns
not                 456   (2.6%)    — Boolean negation
array_getelement    419   (2.4%)    — Array access
array_setelement    334   (1.9%)    — Array write
strcat              312   (1.8%)    — String concatenation
struct_get          276   (1.6%)    — Struct field access (FO4+ opcode)
cmp_lt              186   (1.1%)    — Less-than comparison
iadd                154   (0.9%)    — Integer addition
```

### Most Called Functions
**Static calls (game engine API):**
```
utility.Wait                    242    — Timer/delay
debug.Trace                      85    — Debug logging
game.GetLocalPlayer              78    — Get player reference
sound.StopInstance               67    — Audio control
utility.RandomFloat              39    — RNG
utility.RandomInt                22    — RNG
game.GetFormFromFile             21    — Load game data
```

**Instance method calls:**
```
PlayAnimation                   521    — Animation triggers
Play (Sound)                    268    — Sound playback
Is3DLoaded                      186    — 3D mesh check
GoToState                       159    — State machine transitions
StartTimer                      109    — Timer creation
GetLinkedRef                     92    — Linked reference chains
GetValue                         87    — Actor value queries
SetValue                         73    — Actor value modification
HasKeyword                       58    — Keyword checks
Dismember                        56    — Gore/dismemberment
```

### FO4+ Opcode Usage in FO76
```
struct_get       276    — Struct member access (most used FO4+ opcode)
struct_set        68    — Struct member write
is                18    — Runtime type checking
array_findstruct  13    — Search struct arrays
array_add          9    — Dynamic array append
struct_create      5    — Struct instantiation
array_remove       5    — Array element removal
array_clear        1    — Array clear
```

---

## Critical Finding: Client vs. Server Script Split

**Only 10.8% of scripts contain bytecode.** The remaining 89.2% are "interface" scripts —
they define properties, native function signatures, and struct types, but contain no
executable instructions. This means:

1. **Damage calculations** — NOT in client scripts. The damage formula, perk multipliers,
   legendary effect processing, and DPS calculations are all server-side.

2. **Perk stacking logic** — NOT in client scripts. Perk application, rank scaling, and
   interaction effects are handled by the server.

3. **Quest stage transitions** — NOT in client scripts. Quest objective management,
   stage changes, and conditional logic are server-side.

4. **What IS in client scripts:**
   - Animation triggers (`PlayAnimation`: 521 calls)
   - Sound effects (`Play`: 268 calls, `StopInstance`: 67 calls)
   - Visual effects (gore/dismemberment: 56 calls)
   - UI tutorials (`PlayerTutorialScript`: 371 instructions, most complex client script)
   - State machine transitions for interactive objects (buttons, terminals, vaults)
   - Client-side creature behavior scripts (AI hints, not actual AI)

### Implications for Damage Calculator Verification
Our damage calculator CANNOT be verified against client .pex scripts because the formulas
live server-side. However, the client scripts reveal:
- **Struct definitions** for damage-related data structures (560 structs across 420 scripts)
- **Property types** and naming conventions used by the damage system
- **Native function signatures** that hint at the engine's internal API
- **Event handler patterns** showing when/how combat events fire

---

## Inheritance Hierarchy (Key Combat Classes)

```
ScriptObject
├── Form
│   ├── ObjectReference
│   │   ├── Actor (132 children)
│   │   │   ├── Player (unique)
│   │   │   ├── CompanionScript
│   │   │   ├── CreatureVariantScript
│   │   │   ├── ScorchbeastRaceScript
│   │   │   ├── AssaultronRaceScript
│   │   │   └── ... (127 more)
│   │   ├── Default2StateActivator (20+ children)
│   │   ├── GunTurretScript
│   │   └── ... (835 total children)
│   ├── Perk
│   ├── Spell
│   ├── Weapon
│   ├── Armor
│   └── ...
├── ActiveMagicEffect (many children)
│   ├── AbLegendaryScript
│   ├── PerkAdrenalineReactionScript
│   └── ...
└── Quest (many children)
    ├── DailyQuestScript
    ├── MissionQuestActivatorScript
    └── ...
```

---

## Tools Built

### 1. `pex_parser.py` — PEX Bytecode Parser & Disassembler
- Full .pex binary format parser (LE for FO4/FO76, BE for Skyrim)
- Human-readable disassembly output with opcode names and resolved arguments
- JSON output mode for programmatic use
- Opcode statistics analyzer
- Batch directory scanner (parsed 7,165 files in ~30 seconds)
- .pex vs .psc comparison tool

**Usage:**
```bash
python pex_parser.py script.pex              # Full disassembly
python pex_parser.py script.pex --json       # JSON output
python pex_parser.py script.pex --stats      # Opcode statistics
python pex_parser.py --scan /path/to/scripts # Batch analysis
python pex_parser.py script.pex --compare source.psc
```

### 2. `dependency_graph.py` — Script Dependency & Call Graph Builder
- Inheritance tree builder (extends relationships)
- Static + instance method call graph
- Event handler mapping (166 unique events, 1,607 handlers)
- Property/variable type references
- Per-script dependency tracing
- DOT graph output for visualization

**Usage:**
```bash
python dependency_graph.py /path/to/scripts/          # Full JSON graph
python dependency_graph.py /path/to/scripts/ --trace Actor
python dependency_graph.py /path/to/scripts/ --events
python dependency_graph.py /path/to/scripts/ --functions GetValue
python dependency_graph.py /path/to/scripts/ --dot --focus Actor
```

### 3. `fo76_dependency_graph.json` — Pre-built dependency graph
Complete dependency graph for all 7,165 scripts.

---

## Existing Tools Evaluated

### SkyMP PapyrusVM (github.com/skyrim-multiplayer/skymp)
- Full C++ Papyrus VM implementation for Skyrim multiplayer
- Located in `skymp5-server/cpp/papyrus_vm_lib/`
- **Not directly usable for FO76** — designed for Skyrim's opcode set and game API
- Would require significant adaptation for FO76's game ID 3, version 3.15, and extra opcodes
- Architecture is sound: lazy .pex loading, native function binding via C++ class registration

### Champollion (github.com/Orvid/Champollion)
- .pex to .psc decompiler
- Supports Skyrim, FO4, FO76, Starfield
- Source code was invaluable for understanding the .pex binary format
- Key insight: the `const_flag` byte in variables/objects is LE-only (FO4+)

### Open Papyrus (open-papyrus.github.io)
- Community documentation project for the Papyrus language
- PEX file format documentation exists but is incomplete
- Referenced UESP wiki and Papyrith compiler for instruction details

---

## Why a Full VM Won't Help (and What Will)

A standalone Papyrus VM cannot execute FO76 scripts meaningfully because:

1. **89% of scripts are interface-only** — no bytecode to execute
2. **Combat logic is server-side** — damage formulas, perk effects, legendary processing
3. **1,107 native functions** would need stubs — these are engine internals (GetValue,
   SetValue, HasKeyword, Cast, etc.) that require actual game state
4. **Client scripts are cosmetic** — animations, sounds, UI, visual effects

### What IS Useful
The tools we built provide real value for GameCryptids:

1. **Struct definitions reveal data models** — 560 struct types define how the game
   organizes damage data, disease data, quest data, etc. These are the "schemas" of
   the game's internal data.

2. **Native function signatures** map the engine API — 1,107 native functions show
   exactly what the engine can do (GetValue, HasKeyword, Cast, GetFormFromFile, etc.)

3. **Event handler mapping** shows the game's event-driven architecture — knowing
   which 166 events exist and which scripts handle them reveals trigger chains.

4. **Property naming conventions** reveal hidden game mechanics — property names like
   `HealthThreshhold`, `DiseaseChanceMult`, `LegendaryPowerUp` directly map to
   game mechanics even when the logic is server-side.

5. **The dependency graph** enables targeted decompiled source analysis — instead of
   reading 7,095 decompiled scripts randomly, we can trace exact dependency chains.

---

## Next Steps

1. **Cross-reference struct definitions with decompiled .psc files** — the struct types
   defined in .pex give us the field names; the .psc files may show how they're used.

2. **Map native function signatures to game mechanics** — the 1,107 native functions
   are the game engine's API. Documenting what each does helps understand game behavior.

3. **Event chain analysis** — trace which events trigger which state transitions to
   understand the full lifecycle of combat encounters, legendary spawns, etc.

4. **Property value extraction** — many scripts define Const properties with default
   values (health thresholds, damage multipliers, etc.) that ARE in the client data.

---

## References

- [UESP: Compiled Script File Format](https://en.uesp.net/wiki/Skyrim_Mod:Compiled_Script_File_Format)
- [Open Papyrus: PEX File Format](https://open-papyrus.github.io/docs/Pex_File_Format/)
- [Champollion Decompiler](https://github.com/Orvid/Champollion) — PEX reader source
- [SkyMP PapyrusVM](https://github.com/skyrim-multiplayer/skymp) — C++ VM reference
- [russo-2025/papyrus-compiler](https://github.com/russo-2025/papyrus-compiler) — V-lang compiler
