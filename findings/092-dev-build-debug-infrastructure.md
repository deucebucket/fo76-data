# FO76 Finding 092: Dev Build Debug Infrastructure — ImGui, Web Server, Remote Viewer, Lua VM

## Status: CONFIRMED
## Source: engine_module_map.json, dev_interesting_strings.json, dev_feature_deep_dive.json

## overview

the fo76 dev build reveals the complete internal debug and development infrastructure that bethesda uses to build and test the game. this includes an ImGui overlay with 20+ debug windows, an embedded HTTP server accessible at localhost:8004, a remote game viewer at remoteviewer.bgs.local, an embedded Lua VM separate from Papyrus, Cheat Engine detection systems, and a full automated testing framework. none of this is accessible in retail builds, but all the code ships in the client binary.

## ImGui debug overlay

### the system

ImGui (a popular C++ immediate-mode GUI library) is built directly into the creation engine 2 renderer. it's not a bolt-on tool — it has dedicated engine integration through these source files:

- `bsshader/imgui/bsimguirenderer.cpp` — GPU rendering integration
- `bsmain/bsimgui.cpp` — core ImGui initialization and frame management
- `bsmain/bsimguiwebsocketrenderer.cpp` — WebSocket-based remote rendering
- `game/debug/imgui/bsimguihelpers.cpp` — game-specific ImGui utilities
- `game/debug/imgui/bsimguiperks.cpp` — perk system debug UI
- `game/debug/imgui/imguibnettracker.cpp` — bethesda.net connection tracker
- `game/debug/imgui/imguisocialsystems.cpp` — social system debug UI

### the frame lifecycle

the overlay runs on every frame:
```
BSImGui::Impl::BeginFrame
BSImGui::Impl::PerformInputProcessing
BSImGui::Impl::TickWindows
BSImGui::Impl::EndFrame
BSImGuiRenderer::Render
```

### confirmed debug windows (20+ tab windows)

each of these is a singleton ImGui panel that developers can open:

| window class | purpose |
|-------------|---------|
| BSImGuiChallengePass | season/scoreboard debug |
| BSImGuiChallenges | challenge tracking debug |
| BSImGuiConsole | in-game debug console |
| BSImGuiDailyContentManager | daily content rotation debug |
| BSImGuiDebugText | text overlay debug |
| BSImGuiEvents | event system debug |
| BSImGuiExpeditions | expedition system debug |
| BSImGuiHelpMenu | help/documentation menu |
| BSImGuiManagedWork | job/task system debug |
| BSImGuiPerkMenu | perk system debug |
| BSImGuiStreaming | asset streaming debug |
| ImGuiAtomicMods | atom shop/mod debug |
| ImGuiBNetTracker | bethesda.net connection monitoring |
| ImGuiCharacterManager | character/NPC debug |
| ImGuiEntitlements | entitlement/purchase debug |
| ImGuiFalloutWorlds | fallout worlds (custom worlds) debug |
| ImGuiFalloutWorldsCGMEditor | custom game mode editor |
| ImGuiHitData | combat hit registration debug |
| ImGuiJira | embedded Jira bug tracker integration |
| ImGuiSocialSystems | social features debug |
| ImGuiUIState | UI state machine debug |
| ImGuiWeapons | weapon stats/balance debug |
| ImGuiBatchFiles | batch file processing |
| BSImGuiBabylon | nuclear winter debug |
| GameValidationImGui | game state validation |

### configuration settings

```
bImGuiEnabled:Debug — master toggle
bImGuiOnScreen:Debug — render on screen vs remote
bImGuiAllowRemoteActivation:Debug — allow remote control
bImGuiAutoHideMenuBar:Debug — auto-hide the menu bar
bImGuiAutoHideMouse:Debug — hide mouse when not in use
bImGuiAutoShowControllerHelp:Debug — controller prompt display
bImGuiGrabMouseOnHover:Debug — capture mouse on hover
bAlwaysShowRenderDoc:ImGui — RenderDoc GPU debugger integration
sImGuiBatchFilesDir:Debug — batch file directory path
uImGuiFrameBufferSize:PathingDebug — pathfinding debug buffer
uImGuiHitDataMaxEntries:Debug — max hit data display entries
uImGuiRemotePort:Debug — port for remote ImGui access
fWebSocketRateLimitSeconds:ImGui — websocket frame rate limit
```

### remote ImGui via WebSocket

`BSImGuiWebSocketRenderer` enables ImGui to render over WebSocket connections. this means developers can view and interact with the debug overlay from a separate machine — they don't need to be at the game's display. combined with `bImGuiAllowRemoteActivation:Debug` and `uImGuiRemotePort:Debug`, this creates a full remote debug dashboard.

## embedded web server (localhost:8004)

### the system

the engine embeds CivetWeb, a lightweight C/C++ HTTP server, through two source files:
- `bswebserver/bswebserver.cpp`
- `bswebserver/civet/civetweb.c`

### confirmed endpoint

```
http://127.0.0.1:8004/dashboard/services/season/details/commands
```

this is a season service management dashboard. the "commands" path suggests it accepts POST requests to manipulate season/scoreboard state — advancing seasons, resetting progress, granting rewards.

### server telemetry and error tracking

```
bswebserver.start — server startup event
bswebserver.impl-init.failure — initialization failure
bswebserver.do-user-callback.timeout — request handler timeout
bswebserver.handle-request.exception — unhandled exception in request handler
bswebserver.request-tracker.init-info — request tracking initialization
bswebserver.request-tracker.end-info — request completion tracking
bswebserver.request-tracker.end-info.high-request-time — slow request warning
bswebserver.send-response.failure — response sending failure
bswebserver.do-write.size-overflow — response too large
uRequestTimeoutMs:WebServer — configurable request timeout
```

this isn't a toy — it has proper error handling, request tracking, timeout configuration, and performance monitoring for slow requests.

## remote game viewer (remoteviewer.bgs.local)

the dev build references `http://remoteviewer.bgs.local` — an internal bethesda tool that lets developers remotely view game state. the `.bgs.local` domain is bethesda game studios' internal network. this tool likely shows:
- live game world state
- player positions and inventories
- quest progress
- server performance metrics

## other internal URLs

| url | purpose |
|-----|---------|
| `http://rkv-bgsshader01.zenimax.com:3579` | shader build server (rkv = rockville office) |
| `http://localhost:3579` | local shader server instance |
| `http://comments.bgs.local/api/create` | internal code review/comments API |
| `https://bgs.atlassian.net/rest/api/2/` | jira bug tracking REST API |
| `https://certb-site.bethesda.net` | certification/testing environment |
| `https://int-site.bnet.run` | internal bethesda.net |
| `https://staging-api.bnet.run` | staging API server |

## Lua VM

### the system

a Lua 5.3 virtual machine is embedded in the engine:
- source: `bsvm/lua/bslua.cpp`
- version string: `$LuaVersion: Lua 5.3.0 Copyright (C) 1994-2015 Lua.org, PUC-Rio $`

this is completely separate from Papyrus (the game's scripting language). Lua is used for:
- internal tooling and automation
- debug scripting
- configuration management
- build system integration

papyrus handles gameplay scripting (quests, triggers, items). lua handles developer tooling. two separate scripting VMs running in the same engine.

## Cheat Engine detection

the dev build contains extensive anti-cheat detection specifically targeting Cheat Engine:

```
ClientReportedBadAppUsageCheatEngine
ClientReportedBadAppUsageCheatEngineByProcessName
ClientReportedBadDllUsageCheatEngineSpeedhack
Player detected with CheatEngine resident in memory by process name
Player detected with CheatEngine resident in memory by window name
Player detected with CheatEngine's speedhack DLL resident in process memory
```

detection methods:
1. **process name scanning** — looks for the CheatEngine process
2. **window name scanning** — looks for CheatEngine's window title
3. **DLL injection detection** — specifically checks for the speedhack DLL in process memory

configuration:
```
bAlwaysDetectCheats:CheatDetection
bAlwaysSendCheatDetectionToServer:CheatDetection
bEnableCheatPrompt:General
bEnableModuleRuns:CheatDetection
```

source file: `project76\game\misc\bscheatdetection.cpp`

the detection system fires a `PlayerCheatingEventToServer` network message when triggered, which the server logs and presumably flags the account.

## automated testing framework

a complete `GameplayAutomatedTesting` system exists for QA:

### network messages (client-server automated test protocol)

```
AutomatedTesting::ExecuteBatchedConsoleCommands — run a batch of console commands
AutomatedTesting::QueueBatchedConsoleCommand — queue a command for batch execution
AutomatedTesting::RequestExecutionIndex — request a test execution slot
AutomatedTesting::ExecutionIndexResponse — server assigns execution index
AutomatedTesting::RequestQuestAlias — query quest alias state
AutomatedTesting::QuestAliasResponse — server returns quest alias data
```

### configuration

```
bAutomatedTestEnableDebugLogging:AutomatedTesting — verbose logging
bAutomatedTestExitOnComplete:AutomatedTesting — exit game when tests finish
iAutomatedTestDuration:AutomatedTesting — test runtime limit
RunAutomatedTest — console command to start tests
```

### source files

```
game/gameplay/gameplayautomatedtesting.cpp
game/network/reliableautomatedtestmessages.h
```

the system supports client-server test coordination — a QA automation server can send batches of console commands to game clients, query quest state, and verify results. this is how bethesda runs automated regression testing on fo76 updates.

## debug text overlay system

beyond ImGui, there's a separate debug text system:

```
game/debug/debugtext.cpp
game/debug/debugtextpages/debugtextactor.cpp — actor stats overlay
game/debug/debugtextpages/debugtextcaching.cpp — cache performance
game/debug/debugtextpages/debugtextcombat.cpp — combat data overlay
game/debug/debugtextpages/debugtextloadedreferences.cpp — loaded ref count
game/debug/debugtextpages/debugtextnavmesh.cpp — navmesh visualization
game/debug/debugtextpages/debugtextpapyrus.cpp — papyrus VM stats
game/debug/debugtextpages/debugtextturfsystem.cpp — turf system debug
```

additional debug overlays:
```
game/debug/overlay/papyrusoverlay.cpp — papyrus script performance
game/debug/overlay/radiooverlay.cpp — radio system debug
game/debug/overlay/timingoverlay.cpp — frame timing
game/debug/overlay/warningsoverlay.cpp — runtime warnings
```

## build system

the build agent path `project76\` reveals:
- **TeamCity** is the CI/CD system (buildagent is TeamCity's agent directory)
- **work ID [redacted-hash]** is the project76 build configuration hash
- the build server runs on windows (e:\ drive)
- "project76" is the internal project name for fallout 76

total codebase metrics from the dev build:
- 34 engine modules
- 1,540 source files referenced in debug strings
- 2,163 assert/validation references
- 6,146 named C++ functions extracted from symbols
