# Finding 079: Papyrus .pex Bytecode Format Analysis

**Date:** 2026-03-20
**Scope:** All 7,165 FO76 client-side .pex files
**Tool:** `tools/papyrus_vm/pex_parser.py`

## Summary

Complete analysis of the Papyrus .pex compiled script format as used in Fallout 76.
Every .pex file was parsed without error, documenting the binary structure, instruction
set, string/function/property tables, and metadata.

---

## 1. File Header (14+ bytes)

All FO76 .pex files use **little-endian** byte order (FO4/FO76/Starfield). Skyrim uses big-endian.

| Offset | Size | Field | FO76 Value |
|--------|------|-------|------------|
| 0x00 | 4 | Magic | `DE C0 57 FA` (LE: 0xFA57C0DE) |
| 0x04 | 1 | Major version | 3 |
| 0x05 | 1 | Minor version | 15 (0x0F) |
| 0x06 | 2 | Game ID | 3 (Fallout 76) |
| 0x08 | 8 | Compilation timestamp | Unix epoch (seconds) |
| 0x10 | 2+N | Source filename | uint16 len + UTF-8 bytes |
| var | 2+N | Username | uint16 len + UTF-8 bytes |
| var | 2+N | Computer name | uint16 len + UTF-8 bytes |

**Key finding:** All 7,165 FO76 scripts are version **3.15**, game ID **3**.
Build metadata reveals: user `builds`, machine `RKVBGSBUILD37`, source paths
starting with `E:\BuildAgent\work\54f8b4883a620675\` (TeamCity CI server).

### Endianness Detection

The magic number `0xFA57C0DE` (mnemonic: "FAST CODE") is the canonical value.
- **FO4/FO76/Starfield:** Written as little-endian -> bytes on disk: `DE C0 57 FA`
- **Skyrim:** Written as big-endian -> bytes on disk: `FA 57 C0 DE`

Reading the first 4 bytes as LE uint32 gives `0xFA57C0DE` for FO4/FO76 and `0xDEC057FA` for Skyrim.

### Game IDs

| ID | Game |
|----|------|
| 1 | Skyrim |
| 2 | Fallout 4 |
| 3 | Fallout 76 |
| 4 | Starfield (assumed) |

---

## 2. String Table

Immediately follows the header. All string references in the file use uint16 indices into this table.

```
uint16  count       - number of strings
For each string:
  uint16  length    - byte length
  bytes   data      - UTF-8 encoded string
```

Strings include: script names, function names, variable names, type names, docstrings,
property group names, compiler-generated temp variable names (e.g., `::temp34`),
auto-var backing names (e.g., `::CombatSound_var`), and string literal constants.

---

## 3. Debug Info

```
uint8   has_debug   - 0 = no debug info, 1 = present
```

If present:

```
uint64  modification_time   - source file modification timestamp

uint16  function_count
For each function:
  uint16  object_name_idx   - string table index
  uint16  state_name_idx    - string table index (empty = default state)
  uint16  function_name_idx - string table index
  uint8   function_type     - 0=normal, 1=getter, 2=setter
  uint16  instruction_count
  uint16[] line_numbers     - source line for each instruction
```

### FO4/FO76 Additional Debug Sections (not in Skyrim)

**Property Groups:**
```
uint16  group_count
For each group:
  uint16  object_name_idx
  uint16  group_name_idx
  uint16  doc_string_idx
  uint32  user_flags
  uint16  name_count
  uint16[] name_indices    - property names in this group
```

**Struct Member Orders:**
```
uint16  order_count
For each order:
  uint16  object_name_idx
  uint16  order_name_idx
  uint16  name_count
  uint16[] name_indices    - member names in declaration order
```

**Metadata not in Champollion output:** Property group info (Group names, docstrings,
membership) and struct member ordering are preserved in debug info but Champollion
reconstructs these from the decompiled source structure.

---

## 4. User Flags

```
uint16  count
For each flag:
  uint16  name_idx      - string table index
  uint8   flag_index    - bit position (0-31)
```

Standard FO76 user flags:

| Name | Bit | Purpose |
|------|-----|---------|
| hidden | 0 | Hide from CK |
| conditional | 1 | Conditional property |
| default | 2 | Default value marker |
| collapsedonref | 3 | UI collapse in CK |
| collapsedonbase | 4 | UI collapse in CK |
| mandatory | 5 | Required property |
| transactional | 6 | FO76 multiplayer transaction safety |

---

## 5. Object Table

```
uint16  object_count
For each object:
  uint16  name_idx
  uint32  object_size       - total byte size (not used by readers)
  uint16  parent_class_idx  - string index (empty = no parent)
  uint16  doc_string_idx
  uint8   const_flag        - FO4/76 only
  uint32  user_flags
  uint16  auto_state_idx    - default state name
```

### 5.1 Struct Definitions (FO4/76 only)

```
uint16  struct_count
For each struct:
  uint16  name_idx
  uint16  member_count
  For each member:
    uint16  name_idx
    uint16  type_idx
    uint32  user_flags
    Value   default_value   - typed value (see below)
    uint8   const_flag
    uint16  doc_string_idx
```

420 scripts contain struct definitions (5.9% of total).

### 5.2 Variables

```
uint16  variable_count
For each variable:
  uint16  name_idx
  uint16  type_idx
  uint32  user_flags
  Value   default_value
  uint8   const_flag      - FO4/76 only
```

Compiler-generated variables start with `::` (e.g., `::CombatSound_var` for auto-properties,
`::temp34` for expression temporaries, `::nonevar` for discarded return values).

### 5.3 Properties

```
uint16  property_count
For each property:
  uint16  name_idx
  uint16  type_idx
  uint16  doc_string_idx
  uint32  user_flags
  uint8   flags           - bit0=read, bit1=write, bit2=autovar

  If flags & 0x04 (auto):
    uint16  auto_var_idx  - backing variable name
  Else:
    If flags & 0x01 (readable):
      Function read_handler
    If flags & 0x02 (writable):
      Function write_handler
```

### 5.4 States

```
uint16  state_count
For each state:
  uint16  name_idx        - empty string = default state
  uint16  function_count
  For each function:
    uint16  name_idx
    Function body
```

---

## 6. Function Body

```
uint16  return_type_idx
uint16  doc_string_idx
uint32  user_flags
uint8   flags             - bit0=global, bit1=native

uint16  param_count
For each param:
  uint16  name_idx
  uint16  type_idx

uint16  local_count
For each local:
  uint16  name_idx
  uint16  type_idx

uint16  instruction_count
[Instructions...]          - only if not native (flag bit1=0)
```

**Native functions** (bit 1 set) have no instruction body. They are implemented in
the game engine's C++ code. **1,107 unique native functions** exist across FO76 scripts.

---

## 7. Value Encoding

Every operand in instructions and every default value uses this tagged format:

```
uint8   type_tag
[payload based on type]
```

| Tag | Type | Payload | Size |
|-----|------|---------|------|
| 0 | None | (nothing) | 1 byte total |
| 1 | Identifier | uint16 string index | 3 bytes total |
| 2 | String | uint16 string index | 3 bytes total |
| 3 | Integer | int32 | 5 bytes total |
| 4 | Float | float32 | 5 bytes total |
| 5 | Bool | uint8 | 2 bytes total |

Identifier vs String: both reference the string table, but Identifier means a variable/
function/type name reference, while String means a literal string constant.

---

## 8. Complete Instruction Set (48 opcodes)

### 8.1 Skyrim Original Set (0x00 - 0x23, 36 opcodes)

| Op | Hex | Name | Args | Description |
|----|-----|------|------|-------------|
| 0 | 0x00 | nop | 0 | No operation |
| 1 | 0x01 | iadd | 3 | dest = a + b (integer) |
| 2 | 0x02 | fadd | 3 | dest = a + b (float) |
| 3 | 0x03 | isub | 3 | dest = a - b (integer) |
| 4 | 0x04 | fsub | 3 | dest = a - b (float) |
| 5 | 0x05 | imul | 3 | dest = a * b (integer) |
| 6 | 0x06 | fmul | 3 | dest = a * b (float) |
| 7 | 0x07 | idiv | 3 | dest = a / b (integer) |
| 8 | 0x08 | fdiv | 3 | dest = a / b (float) |
| 9 | 0x09 | imod | 3 | dest = a % b (integer modulo) |
| 10 | 0x0A | not | 2 | dest = !src (boolean negation) |
| 11 | 0x0B | ineg | 2 | dest = -src (integer negation) |
| 12 | 0x0C | fneg | 2 | dest = -src (float negation) |
| 13 | 0x0D | assign | 2 | dest = src |
| 14 | 0x0E | cast | 2 | dest = (type)src (type conversion) |
| 15 | 0x0F | cmp_eq | 3 | dest = (a == b) |
| 16 | 0x10 | cmp_lt | 3 | dest = (a < b) |
| 17 | 0x11 | cmp_lte | 3 | dest = (a <= b) |
| 18 | 0x12 | cmp_gt | 3 | dest = (a > b) |
| 19 | 0x13 | cmp_gte | 3 | dest = (a >= b) |
| 20 | 0x14 | jmp | 1 | Unconditional relative jump (int offset) |
| 21 | 0x15 | jmpt | 2 | Jump if condition is true |
| 22 | 0x16 | jmpf | 2 | Jump if condition is false |
| 23 | 0x17 | callmethod | 3+var | Call instance method: name, object, dest, [args...] |
| 24 | 0x18 | callparent | 2+var | Call parent method: name, dest, [args...] |
| 25 | 0x19 | callstatic | 3+var | Call static function: class, name, dest, [args...] |
| 26 | 0x1A | return | 1 | Return value from function |
| 27 | 0x1B | strcat | 3 | dest = str1 + str2 (concatenation) |
| 28 | 0x1C | propget | 3 | dest = object.PropertyName |
| 29 | 0x1D | propset | 3 | object.PropertyName = value |
| 30 | 0x1E | array_create | 2 | dest = new Type[size] |
| 31 | 0x1F | array_length | 2 | dest = array.Length |
| 32 | 0x20 | array_getelement | 3 | dest = array[index] |
| 33 | 0x21 | array_setelement | 3 | array[index] = value |
| 34 | 0x22 | array_findelement | 4 | dest = array.Find(value, startIndex) |
| 35 | 0x23 | array_rfindelement | 4 | dest = array.RFind(value, startIndex) |

### 8.2 Fallout 4 Additions (0x24 - 0x2E, 11 opcodes)

| Op | Hex | Name | Args | Description |
|----|-----|------|------|-------------|
| 36 | 0x24 | is | 3 | dest = (object is Type) runtime type check |
| 37 | 0x25 | struct_create | 1 | dest = new StructType |
| 38 | 0x26 | struct_get | 3 | dest = struct.MemberName |
| 39 | 0x27 | struct_set | 3 | struct.MemberName = value |
| 40 | 0x28 | array_findstruct | 5 | dest = array.FindStruct(member, value, startIdx) |
| 41 | 0x29 | array_rfindstruct | 5 | dest = array.RFindStruct(member, value, startIdx) |
| 42 | 0x2A | array_add | 3 | array.Add(value, count) |
| 43 | 0x2B | array_insert | 3 | array.Insert(value, index) |
| 44 | 0x2C | array_removelast | 1 | array.RemoveLast() |
| 45 | 0x2D | array_remove | 3 | array.Remove(index, count) |
| 46 | 0x2E | array_clear | 1 | array.Clear() |

### 8.3 Fallout 76 Addition (0x2F, 1 opcode)

| Op | Hex | Name | Args | Description |
|----|-----|------|------|-------------|
| 47 | 0x2F | array_getallmatchingstructs | 6 | Filter array of structs by field match |

**Finding:** Opcode 0x2F exists in Champollion's opcode table as FO76-specific, but
it was **not found in any of the 7,165 client-side scripts**. It may only appear in
server-side scripts (which we don't have) or was added for future use.

### Variable-Length Call Instructions

CALLMETHOD, CALLPARENT, and CALLSTATIC use variable arguments:
```
uint8   opcode
Value   fixed_arg_0     - method name (CALLMETHOD/CALLPARENT) or class (CALLSTATIC)
Value   fixed_arg_1     - object ref (CALLMETHOD) or method name (CALLPARENT/CALLSTATIC)
Value   fixed_arg_2     - dest var (CALLMETHOD/CALLSTATIC only)
Value   vararg_count    - INTEGER: number of following arguments
Value[] varargs         - actual call arguments
```

### Jump Instructions

Jump targets are **relative instruction offsets** (not byte offsets), stored as an
integer Value. A positive offset jumps forward, negative jumps backward.

---

## 9. Native Function Encoding

Native functions are declared with flag bit 1 set in the function body. They have
no instruction bytecode. The VM resolves them to C++ engine functions at load time.

```
Function flags byte: bit 0 = global/static, bit 1 = native
```

When a native function is called via CALLMETHOD/CALLSTATIC, the call looks identical
to a scripted function call. The VM checks the target function's native flag and
dispatches to the engine implementation.

**1,107 unique native functions** found across FO76 scripts, including:
- `ObjectReference.PlayAnimation`, `Sound.Play`, `Actor.Is3DLoaded`
- `Game.GetLocalPlayer`, `Utility.Wait`, `Math.Floor`
- `Form.HasKeyword`, `Actor.GetValue`, `ObjectReference.SetValue`

---

## 10. FO76 vs FO4 vs Skyrim Differences

| Feature | Skyrim | Fallout 4 | Fallout 76 |
|---------|--------|-----------|------------|
| Byte order | Big-endian | Little-endian | Little-endian |
| Game ID | 1 | 2 | 3 |
| Version | 3.1-3.2 | 3.9+ | 3.15 |
| Struct support | No | Yes | Yes |
| Variable const flag | No | Yes | Yes |
| Object const flag | No | Yes | Yes |
| Debug property groups | No | Yes | Yes |
| Debug struct orders | No | Yes | Yes |
| Opcodes 0x24-0x2E | No | Yes | Yes |
| Opcode 0x2F | No | No | Defined but unused in client scripts |
| `transactional` flag | No | No | Yes (bit 6, multiplayer safety) |

---

## 11. Opcode Usage Statistics (7,165 scripts, 17,859 total instructions)

| Opcode | Count | % |
|--------|-------|---|
| callmethod | 4,773 | 26.7% |
| jmpf | 2,318 | 13.0% |
| cast | 2,251 | 12.6% |
| jmp | 2,007 | 11.2% |
| assign | 1,049 | 5.9% |
| cmp_eq | 995 | 5.6% |
| callstatic | 845 | 4.7% |
| return | 461 | 2.6% |
| not | 456 | 2.6% |
| array_getelement | 419 | 2.3% |
| array_setelement | 334 | 1.9% |
| strcat | 312 | 1.7% |
| struct_get | 276 | 1.5% |

The dominance of `callmethod` (26.7%) and control flow (`jmpf`+`jmp` = 24.2%)
shows scripts are primarily orchestration code calling native engine functions.

---

## 12. Metadata Not in Champollion Decompilation

The .pex binary contains information that Champollion does not include in .psc output:

1. **Build server path**: `E:\BuildAgent\work\54f8b4883a620675\Source\Scripts\`
2. **Build user/machine**: `builds` / `RKVBGSBUILD37`
3. **Compilation timestamp**: Per-file compile time
4. **Debug line mappings**: Instruction-to-source-line correspondence
5. **Property group membership**: Which properties belong to which group
6. **Struct member ordering**: Preserved in debug section
7. **Compiler temporaries**: `::temp34`, `::nonevar` etc. visible in bytecode but
   abstracted away in decompilation
8. **Auto-var backing names**: `::PropertyName_var` pattern visible in variable table

---

## Tool

Parser/disassembler: `tools/papyrus_vm/pex_parser.py`

```bash
# Disassemble a single file
python pex_parser.py script.pex

# JSON output
python pex_parser.py script.pex --json

# Header only
python pex_parser.py script.pex --header

# Opcode statistics
python pex_parser.py script.pex --stats

# Compare with decompiled source
python pex_parser.py script.pex --compare script.psc

# Batch scan directory (recursive)
python pex_parser.py --scan /path/to/scripts/
```
