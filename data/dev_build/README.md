# Dev Build Analysis

Data extracted from Project76Profile.exe (Jan 2024 profiling build, 139MB).

## Contents

- **dev_build_functions.txt**: 6,146 named C++ functions (Class::Function format)
- **dev_build_source_tree.txt**: 3,625 source file paths from Bethesda's build server
- **dev_only_rtti_classes.txt**: 641 RTTI classes present in dev build but stripped from retail

## Key Stats

| Metric | Dev Build | Retail | Delta |
|--------|-----------|--------|-------|
| File size | 139 MB | 101 MB | +38 MB |
| PE sections | 10 | 8 | +2 |
| Total strings | 1,246,492 | 879,871 | +366,621 |
| RTTI classes | 4,898 | 4,533 | +365 |
| Named functions | 6,146 | 0 | +6,146 |
| Source file paths | 3,625 | 0 | +3,625 |

## Build Server

Build path: `project76\`

## Engine Module Structure

Key modules discovered:
- bps/client — networking (lobby, matchmaking, ping)
- bsscript — Papyrus VM
- bsvm/lua — Lua scripting VM
- bswebserver — embedded debug web server
- bshavok — Havok physics integration
- bsmenu — UI/menu system
- bsanimation — animation graph system
- bsgraphics — rendering
- bsshader/enlighten — Enlighten GI lighting
- bsshader/imgui — ImGui debug overlay
- facegen — face generation
- bcstelemetry — telemetry/analytics
