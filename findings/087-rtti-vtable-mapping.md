# 087: RTTI Vtable Mapping - FO76 SFE Functions to Classes

**Date:** 2026-03-20
**Binary:** Fallout76.exe (104,899,936 bytes)
**Image Base:** 0x0000000140000000

## Summary

Parsed the MSVC RTTI structures in Fallout76.exe to identify which C++ class each SFE function belongs to. Out of 248 SFE `.text` functions, 4 are confirmed virtual methods appearing directly in vtables. The remaining 244 are non-virtual member functions, static functions, or free functions that don't appear in any vtable.

## RTTI Statistics

| Metric | Count |
|--------|-------|
| TypeDescriptors (.?AV/.?AU) | 28,867 |
| CompleteObjectLocators | 27,028 |
| Vtables | 27,028 |
| Total vtable entries | 232,812 |
| Unique functions in vtables | 90,944 |
| Bethesda engine classes | ~4,813 |

## Key Structural Findings

### RTTI Layout in FO76

The binary uses MSVC x64 RTTI with signature=1 (image-base-relative offsets):

- **TypeDescriptors** are in `.data` section (not `.rdata` as typical), starting around file offset 0x05B3A250
- **CompleteObjectLocators** and **vtables** are in `.rdata` section
- COL `pSelf` field validates against its own RVA (used as integrity check)
- Vtable layout: `[COL pointer][vfunc0][vfunc1]...` where COL pointer is at vtable-8

### Section Layout

| Section | VA | Virtual Size | Raw Size |
|---------|-----|-------------|----------|
| .text | 0x00001000 | 0x03F1B9B3 (~63MB) | 0x03F1BA00 |
| .rdata | 0x03F28000 | 0x01AD0C6A (~27MB) | 0x01AD0E00 |
| .data | 0x059F9000 | 0x018255A0 (~24MB) | 0x00420C00 |

## Direct Vtable Matches (4 functions)

These SFE functions appear directly as virtual function pointers in RTTI vtables:

| SFE Function | Address | RTTI Class | Vtable Index |
|-------------|---------|------------|-------------|
| VPrint | 0x01262DA0 | LocalDataShuttle (UiFlashStructure\<CSCategory\>) | vfunc[1] |
| HasDetectionLOS | 0x0135B560 | BSTEventSink\<PSHideEvent\> | vfunc[0] |
| SaveRegistrationHandles | 0x014749B0 | LocalDataShuttle (UiFlashArrayType\<UiFlashFloat\>) | vfunc[4] |
| LoadRegistrationHandles | 0x01474A40 | LocalDataShuttle (UiFlashStructure\<MapUIData\>) | vfunc[4] |

### Analysis of Matches

1. **VPrint** (0x01262DA0) - This is the virtual print function on a UI flash data shuttle for the CS (Creation System?) category. The SFE source puts this in `GameAPI.h`, suggesting it's used as a Console print function that routes through Scaleform.

2. **HasDetectionLOS** (0x0135B560) - A `BSTEventSink<PSHideEvent>` handler. The PS (presumably PlayerStealth) hide event sink has HasDetectionLOS as its first virtual method (the event handler itself). This tells us detection LOS checks are implemented via the event system.

3. **SaveRegistrationHandles / LoadRegistrationHandles** (0x014749B0 / 0x01474A40) - Both are vfunc[4] on different LocalDataShuttle template specializations. These handle serialization of Papyrus registration handles through the UI data system.

## Why Only 4 Matches

The low match count is expected and informative:

- **Most SFE functions are non-virtual.** `DEFINE_MEMBER_FN` (153 entries) and `RelocAddr` (90 entries) identify regular member functions and free functions by their code addresses. These don't appear in vtables.
- **SFE vtable references** (11 entries like `s_ExtraHealthVtbl`) are code-section addresses where the vtable is *referenced* (e.g., in a constructor that writes the vtable pointer), not the vtable data address itself.
- **Virtual functions that SFE hooks** are typically accessed through the vtable at runtime, not by hard-coding their addresses. SFE hooks non-virtual functions because those are the ones that need address fixups.

## Proximity Analysis: Nearest RTTI Class for Each SFE Function

For the 244 unmatched functions, the nearest vtable entry gives a rough neighborhood hint. Functions within ~0x100 bytes of a vtable entry likely belong to the same compilation unit. Key proximity findings:

### Close proximity (< 0x100 bytes from a vtable entry)

| SFE Function | Distance | Nearest RTTI Class |
|-------------|----------|-------------------|
| Impl_ctor (GameMenus) | 0x10 | ConcreteObjectFormFactory\<TESEyes\> |
| Impl_Unk0C | 0x10 | ConcreteFormFactory\<TESFaction\> |
| dtor (BSModelDB) | 0x10 | hkbVariableValueSet |
| EvaluationConditions | 0x20 | BSTEventSource\<ItemScrappedEvent\> |
| SendUIMessageEx | 0x20 | BSTEventSink\<Login_skipped\> |
| ctor (GameFormComponents) | 0x30 | BSTEventSource\<ActiveEditStartEndEvent\> |
| Print | 0x80 | LocalDataShuttle (same as VPrint) |
| QueueUpdate | 0xC0 | DebugTargetCamera |

Note: Proximity matches to unrelated classes (lambdas, templates) indicate that the linker interleaved these functions. The RTTI class at a nearby vtable entry is often a coincidence of link ordering, not class membership.

## Key Game Class Vtable Sizes

These are the primary vtables (offset_in_class=0) for important game classes:

| Class | Vtable Entries | Notes |
|-------|---------------|-------|
| LocalPlayerCharacter | 466 | Largest class - local player |
| BasePlayerCharacter | 464 | Base player class |
| RemotePlayerCharacter | 464 | Other players (FO76 multiplayer) |
| CombatTargetProxy | 414 | Combat AI targeting |
| Actor | 409 | Base actor class |
| ArrowProjectile | 309 | Projectile subclass |
| MissileProjectile | 309 | Projectile subclass |
| Projectile | 307 | Base projectile |
| Explosion | 271 | Explosion effects |
| TESObjectREFR | 268 | Base reference object |
| MagicItem | 162 | Base magic/alchemy |
| TESNPC | 139 | NPC form data |
| TESForm | ~80 | Base form class |
| BSExtraData | 9 | Extra data base |
| IMenu | ~15 | Menu interface |
| NiAVObject | ~60 | Scene graph node |
| BSLightingShaderProperty | ~40 | Shader property |

### Class Hierarchy Evidence

Vtable analysis confirms the inheritance chain through shared vfunc addresses:

```
TESForm (base vtable entries shared by all form classes)
  -> TESObjectREFR (268 vfuncs, extends TESForm)
    -> Actor (409 vfuncs, extends TESObjectREFR)
      -> BasePlayerCharacter (464 vfuncs)
        -> LocalPlayerCharacter (466 vfuncs)
        -> RemotePlayerCharacter (464 vfuncs)
```

The first ~20 vfuncs are identical across TESObjectREFR, Actor, and player classes (inherited from TESForm). Divergence starts at vfunc[21] where each subclass overrides with its own implementation.

### FO76-Specific Classes

Notable classes not present in FO4:
- **RemotePlayerCharacter** - multiplayer remote player representation
- **CombatTargetProxy / CombatTargetObjectProxy** - AI targeting system for multiplayer
- **Various network entity components** - client/server sync infrastructure

## SFE Function Categories (by source header)

| Source Header | Functions | Likely Class | Type |
|--------------|-----------|-------------|------|
| GameMenus.h | 23 | IMenu, HUDComponentBase, UIManager, BSGFxShaderFXTarget | Non-virtual members |
| ScaleformValue.h | 30 | GFxValue, GFxMovieRoot, BSGFxShaderFXTarget | Non-virtual members |
| GameReferences.h | 9 | TESObjectREFR, Actor | Non-virtual members |
| GameObjects.h | 8 | TESNPC | Non-virtual members |
| GameStreams.h | 8 | BSResourceNiBinaryStream | Non-virtual members |
| NiProperties.h | 7 | BSLightingShaderProperty, BSShaderProperty | Non-virtual members |
| GameTypes.h | 7 | BSReadWriteLock, BSFixedString | Non-virtual members |
| PapyrusNativeFunctions.h | 6 | NativeFunction | Non-virtual members |
| BSGraphics.h | 5 | BSRenderManager | Non-virtual members |
| GameFormComponents.h | 5 | TESActorBaseData, ActorValueInfo | Non-virtual members |

## Cryptid Hunting Implications

### Hidden Virtual Methods

The vtable dumps reveal function addresses that could contain hidden game logic:

1. **Actor vtable has 409 entries** - many are undocumented. Virtual functions in the 300-409 range could contain hidden behavior triggers, special NPC reactions, or unused combat mechanics.

2. **LocalPlayerCharacter extends Actor with 57 additional vfuncs** (409->466) - these player-specific virtual methods could include hidden player states, unused abilities, or debug features.

3. **CombatTargetProxy (414 vfuncs)** - nearly as large as Actor, suggesting extensive combat AI that could contain hidden NPC behaviors.

4. **Explosion class (271 vfuncs)** - complex enough to have hidden explosion types or secret damage calculations.

### Next Steps

1. **Dump full vtables** for Actor, LocalPlayerCharacter, and TESObjectREFR to identify undocumented virtual methods
2. **Cross-reference** vtable function addresses with known Papyrus native functions to find hidden scripting hooks
3. **Diff vtables** between FO4 and FO76 to identify new virtual methods added for multiplayer
4. **Scan for unused vtable overrides** - functions that exist in a child class vtable but are never called could be disabled/hidden features

## Output Files

- **JSON data:** `~/ai-drive/gamecryptids/data/fallout76/rtti_vtable_map.json`
  - Complete vtable entries for key game classes
  - All SFE address proximity mappings
  - Top 50 classes by vtable size
