# 086 - Server Emulation & Protocol Reverse Engineering Research

**Date**: 2026-03-20
**Category**: Reverse Engineering Intelligence Gathering
**Purpose**: Catalog all known FO76 server emulation, protocol RE, and private server projects for potential address mappings, function names, and protocol documentation

---

## Executive Summary

The FO76 server emulation scene is **small and largely abandoned**. Two main projects exist, both stalled around 2020-2022. They accomplished the DTLS handshake and initial snapshot reception but never progressed to full game protocol implementation. However, they did produce valuable technical findings about the authentication flow, DTLS configuration, snapshot compression algorithm, and packet structure that are directly relevant to our reverse engineering work.

No publicly shared IDA/Ghidra databases exist for FO76. No RTTI dumps were found in any server emulation project (our own 085-rtti-class-catalog.md appears to be the most comprehensive public catalog). The SFE (Script Framework Extender) project does internal offset work but doesn't publish address databases.

---

## Project 1: Fo76-Private-Server (GitHub Organization)

**URL**: https://github.com/Fo76-Private-Server
**Status**: Effectively abandoned (last meaningful activity: Jan 2020, BnetAPI touched Dec 2022)
**Game Version**: 1.2.6.3 (very early, late 2018/early 2019)
**Discord**: https://discord.gg/p8FXc9k (may be dead)
**Languages**: C# (primary), JavaScript (BnetAPI), C++ (WinHttpWrapper)

### Repositories (9 total)

| Repository | Description | Language | Status |
|---|---|---|---|
| **Documentation** | Project overview and setup | - | Last: Jan 2020 |
| **BnetAPI** | Login, matchmaking, community features server | JavaScript | Last: Dec 2022 |
| **Fo76_Communication** | Client/server communication wrapper library | C# | Last: Feb 2020 |
| **Fo76_UDPServer** | DTLS communication handler | C# | Last: Jan 2020 |
| **Fo76_Packets** | Packet parsing/creation library | C# | Archived Jan 2020 |
| **Fo76_Snapshot** | Snapshot parsing including components | C# | Archived Jan 2020 |
| **Fo76_SnapshotCompression** | Snapshot compress/decompress algorithm reconstruction | C# | Archived Jan 2020 |
| **Tools** | Traffic analysis tools (Frida-based) | JS/Python | Last: Jan 2020 |
| **WinHttpWrapper** | Modified WinHttpWrapper for server redirection | C++ | Last: Jan 2020 |

### What They Accomplished

1. **Authentication flow fully documented**:
   - Login retrieves character and account data via HTTP(S) API
   - Game connects to WebSocket endpoint `/bps/pub/wsa` for matchmaking/server selection
   - WebSocket returns: Server IP, Port, and **PSK (Pre-Shared Key)**
   - Game initiates DTLS connection using PSK with hint string **"PROJECT_76"**

2. **DTLS handshake working**:
   - Uses WolfSSL library for DTLS-PSK
   - Compilation flags reveal: `WOLFSSL_DTLS`, `WOLFSSL_AES_128`, `HAVE_AESGCM`, `WOLFSSL_STATIC_PSK`, `HAVE_ENCRYPT_THEN_MAC`
   - **No certificate-based auth**: `NO_CERTS`, `NO_RSA`, `NO_ASN`, `NO_DH` flags set
   - This means the game-to-server DTLS channel uses **pure PSK authentication, not RSA**
   - The RSA-1024 signatures we found in the client may be for a different purpose (login token verification, content signing, etc.)

3. **Initial snapshot received and partially parsed**:
   - Snapshot components referenced at address **@13321B0** in v1.2.6.3
   - Snapshot parsing library created but incomplete

4. **Snapshot compression algorithm identified**:
   - Based on **DOOM 3 BFG Edition's `LightweightCompression.cpp`** (`neo/sys/LightweightCompression.cpp`)
   - This makes sense given id Software's involvement in FO76's netcode (Quake Champions integration)
   - The compression is a lightweight delta/RLE scheme optimized for game state snapshots

5. **CommunicationLogger tool created**:
   - Uses **Frida** (dynamic instrumentation) to hook game process
   - Logs unencrypted DTLS communication to `fo76.log`
   - Offsets documented for game version 1.2.6.3
   - Script: `fo76_GameCommunication.py`

### What They Did NOT Accomplish

- Full message structure parsing beyond initial snapshot
- Game state replication
- Player movement / entity synchronization
- World loading / cell management
- Any actual gameplay in the emulated server
- No IDA/Ghidra databases shared
- No RTTI class name documentation
- No function name mappings published

### Key Technical Finding: DTLS-PSK, Not RSA

The WolfSSL compilation explicitly disables RSA (`NO_RSA`). The game-server channel uses **DTLS with Pre-Shared Keys only**. This is a critical finding for our project:
- The RSA-1024 key we found in the client binary is NOT used for the game server DTLS channel
- It's likely used for: login token signing, content verification, update authentication, or Bethesda.net API
- The game server auth is PSK-based, with the key distributed via the matchmaking WebSocket

---

## Project 2: Fo76UDPServer (Nexusphobiker)

**URL**: https://github.com/Nexusphobiker/Fo76UDPServer
**Status**: Abandoned (created Nov 2018, 3 commits total)
**Language**: C# (100%)
**Progress**: "Currently only does the handshake. This needs a rewrite badly."

### Assessment

Minimal project. Only implements the initial DTLS handshake. No protocol documentation, no address mappings, no useful reverse engineering data beyond what Fo76-Private-Server already covers. This appears to be an early prototype that was superseded by the Fo76-Private-Server organization's work.

---

## Project 3: Server76

**URL**: https://myfo.online/
**Status**: Unknown (website is a bare landing page)
**Community**: Reddit, Discord, Patreon linked but may be inactive
**Legal note**: Site acknowledges EULA violation

### Assessment

No technical details available on the website. Community channels (Discord/Reddit) would need to be checked manually. The project may have been a continuation of the Fo76-Private-Server work or an independent effort, but no public documentation or code is available.

---

## Project 4: Corianas Server Emulator PoC

**URLs**:
- https://peakd.com/@corianas/hpavrgse (blog post, May 2021)
- https://3speak.tv/watch?v=corianas/hpavrgse (video demo)
- https://odysee.com/@F76:f/FO76-Terminals-Test:7 (terminals test video, July 2021)

### Assessment

Video demonstrations show:
- **Proof of concept local server** with game connecting
- **Terminals working** in the emulated environment (July 2021 video)
- This is likely the most advanced server emulation achieved publicly

The blog post is on PeakD (Hive blockchain) and the videos are on decentralized platforms (3Speak, Odysee), suggesting the developer was cautious about DMCA/legal takedowns. No source code has been publicly shared. This may be the emulator referenced in GUNetwork forum discussions as being "downloadable from a Discord."

---

## Project 5: SFE (Script Framework Extender)

**URL**: https://github.com/keretus/sfe
**Fork**: https://github.com/RobertBateman/F76SE (archived, keretus resumed maintenance)
**Status**: Maintained (updated when game patches break offsets)
**Language**: C/C++ (based on F4SE)

### Relevance to Our Work

SFE is the most active reverse engineering project for FO76's executable. It:
- Hooks Scaleform functions for UI extension (Text Chat, Perk Loadout Manager, etc.)
- Must find and update offsets after every game patch
- Uses IDA and ASM analysis internally to trace offset changes
- Based on F4SE architecture, which has extensive Creation Engine knowledge

**However**: SFE does not publish its offset databases, IDA databases, or function name mappings. The knowledge is held by the maintainer (keretus) and contributors. The source code may contain hardcoded offsets worth examining.

### Key Differences from Fallout 4

Unlike FO4 which has an **Address Library** (https://www.nexusmods.com/fallout4/mods/47327) providing version-independent offset databases for F4SE plugins, **FO76 has no equivalent Address Library**. Each SFE update requires manual offset hunting. This is a significant gap.

---

## Data/Tool Projects (Not Server Emulation)

### fo76-dumps (FWDekker)
**URL**: https://github.com/FWDekker/fo76-dumps
**Status**: Actively maintained (updated Feb 2026)
**Content**: ESM/BA2 game data dumps in CSV, SQLite, MediaWiki formats
**Assessment**: **Purely game data** (items, NPCs, dialogue, recipes, etc.). No executable analysis, no RTTI, no function names, no address mappings. Uses xEdit and ba2extract. Does auto-detect game version from executable but only for versioning purposes.

### fo76utils
**URL**: https://github.com/fo76utils/fo76utils
**Status**: Actively maintained
**Content**: Worldspace rendering, BA2 extraction, data visualization tools
**Assessment**: Parses ESM/BA2 binary formats but does NOT reverse engineer the game executable. No Creation Engine internals, RTTI, or function references.

### Mappalachia
**URL**: https://github.com/AHeroicLlama/Mappalachia
**Status**: Actively maintained (March 2026)
**Content**: Complete mapping tool for FO76
**Assessment**: Uses FO76Edit for data extraction. No executable reverse engineering.

---

## FO76 Anti-Cheat System (Relevant Intel)

Source: https://douggemhax.wordpress.com/2019/06/13/how-to-get-caught-by-fallouts-anti-cheat/

The anti-cheat implements three detection vectors:

1. **EnumWindowsTask**: Scans window titles for substrings matching known tools (Cheat Engine, IDA, WinDbg, x64dbg, etc.). Uses XOR-based string obfuscation with 4-byte values where only LSB is the actual character.

2. **EnumToolsTask**: Calls `IsDebuggerPresent`, `CheckRemoteDebuggerPresent`, and `OutputDebugString` with error code validation.

3. **EnumLibrariesTask**: Enumerates processes and loaded modules against blacklist (cheatengine, x64dbg, MHS, IDA, windbg) and DLL blacklist (speedhack DLLs). Has whitelist of 200+ legitimate modules; unlisted modules trigger flags.

Each detection assigns unique values to a "cheater" flag sent to Bethesda servers. The system is described as relatively unsophisticated compared to modern anti-cheats.

---

## Quake 3 Netcode Architecture (FO76's Foundation)

FO76's multiplayer was built by BattleCry Studios (now BGS Austin) using **Quake Champions netcode from id Software**, integrated into the Creation Engine. Understanding the Quake 3 network model is essential:

### Snapshot System
- Server maintains authoritative game state ("Master Gamestate")
- 32-snapshot cycling history per client
- Server sends delta-compressed snapshots at fixed tick rate
- Each field uses 1-bit changed/unchanged markers
- Only changed fields are transmitted
- Uses "memory introspection" via preprocessor macros and offset arrays

### Delta Compression
- Compresses current state against **last acknowledged** snapshot (not most recent)
- Handles packet loss gracefully by referencing confirmed state
- "Dummy Gamestate" (zeroed) used when no prior snapshot exists (first frame)

### Packet Format
- UDP with Huffman compression + XOR obfuscation
- First 4-12 bytes raw (contain decryption key derivation)
- 32-bit sequence numbers (little-endian)
- Max 1400 bytes per packet (avoids MTU fragmentation)

### Connection Handshake (Quake 3)
- Connectionless packets prefixed with four 0xFF bytes
- Flow: `getchallenge` -> `challengeResponse` -> `connect` -> sequence-numbered packets
- Central authorization server verifies CD keys

### FO76 Modifications
FO76 replaced the Quake auth system with:
- Bethesda.net login -> WebSocket matchmaking -> DTLS-PSK game connection
- "PROJECT_76" as the DTLS hint string
- DOOM 3 BFG's LightweightCompression for snapshot compression (instead of raw Huffman)
- The fundamental snapshot-delta architecture likely remains similar

---

## Discord Communities

### Fallout 76 Datamining Discord
- **Invite**: https://discord.com/invite/fo76datamining
- **Members**: ~6,400+
- **Focus**: Teaching datamining tools, extracting game data, debunking myths
- **Affiliated with**: Fallout Wiki
- **Assessment**: Focused on ESM data extraction, not executable RE. But may have members with deeper knowledge.

### Fo76-Private-Server Discord
- **Invite**: https://discord.gg/p8FXc9k
- **Status**: Likely dead/inactive (project abandoned ~2020)
- **Assessment**: May have archived technical discussions worth reviewing if server still exists.

### Server76 Discord
- **Linked from**: myfo.online
- **Status**: Unknown

---

## Cheat Engine Community

**URL**: https://guidedhacking.com/threads/fallout-76-cheat-table-trainer-25.15704/
**Content**: 25-feature cheat table with memory offsets for player health, ammo, coordinates, etc.
**Assessment**: Contains hardcoded memory addresses that could help map game structures. However, these change with every patch and are focused on player-facing values rather than engine internals. The community at guidedhacking.com and mpgh.net may have more detailed offset tables.

---

## Key Findings Summary

### What Exists and Is Useful

| Finding | Source | Relevance |
|---|---|---|
| Auth flow: Login -> WebSocket -> DTLS-PSK | Fo76-Private-Server | High - explains connection architecture |
| DTLS uses PSK, NOT RSA | Fo76-Private-Server/WolfSSL flags | Critical - RSA key serves different purpose |
| DTLS hint string: "PROJECT_76" | Fo76-Private-Server | High - protocol identification |
| Snapshot compression = DOOM 3 BFG LightweightCompression | Fo76_SnapshotCompression | High - known algorithm |
| Snapshot components at @13321B0 (v1.2.6.3) | Fo76-Private-Server docs | Medium - old version, offset changed |
| Frida-based communication logger | Fo76-Private-Server/Tools | High - methodology for intercepting traffic |
| Anti-cheat: window title + process scan + module whitelist | douggemhax blog | Medium - know what to avoid |
| Quake 3 snapshot-delta architecture | id Software docs | High - foundational protocol understanding |
| Netcode uses 1-bit field change markers + delta compression | Quake 3 protocol docs | High - packet format understanding |

### What Does NOT Exist Publicly

- **No IDA/Ghidra databases** for FO76 executable
- **No RTTI dumps** from server emulation projects (ours in 085 is unique)
- **No Address Library** equivalent for FO76 (unlike FO4)
- **No complete protocol documentation** beyond initial handshake
- **No function name mappings** from executable analysis
- **No working server emulator** (Corianas' PoC closest but source not public)
- **No packet format specifications** beyond initial snapshot reception

### Implications for GameCryptids

1. **Our RTTI catalog (085) is the most comprehensive public FO76 executable analysis** - no other project has published this
2. **The RSA-1024 key is NOT for game server auth** - it's for something else (login tokens, content signing, etc.)
3. **The snapshot system follows Quake 3 architecture** with DOOM 3 BFG compression - this is a known, documented system
4. **Frida is a proven approach** for intercepting FO76 game communication
5. **SFE's offset work is the closest to our needs** but is not publicly documented
6. **The anti-cheat is relatively simple** - process/window name scanning, no kernel-level protection
7. **The datamining Discord** may have members with unpublished RE knowledge worth connecting with

---

## Recommendations

1. **Examine SFE source code** (`sfe/` directory in https://github.com/keretus/sfe) for hardcoded offsets and hooked functions - these represent verified, maintained address mappings
2. **Clone Fo76-Private-Server repos** to extract packet structure definitions, snapshot component parsing code, and communication protocol details from the C# source
3. **Review the DOOM 3 BFG LightweightCompression.cpp** to understand the exact compression algorithm used for FO76 snapshots
4. **Check the Fo76-Private-Server Discord** for any archived technical discussions
5. **Cross-reference our RTTI classes** with any structures found in server emulation code
6. **Build on the Frida approach** from the Tools repo for our own traffic analysis
7. **Investigate the Corianas PoC** - try to find the Discord where the emulator was distributed

---

## All URLs Referenced

### GitHub Repositories
- https://github.com/Fo76-Private-Server (organization - 9 repos)
- https://github.com/Fo76-Private-Server/Documentation
- https://github.com/Fo76-Private-Server/BnetAPI
- https://github.com/Fo76-Private-Server/Fo76_UDPServer
- https://github.com/Fo76-Private-Server/Fo76_Packets
- https://github.com/Fo76-Private-Server/Fo76_Snapshot
- https://github.com/Fo76-Private-Server/Fo76_SnapshotCompression
- https://github.com/Fo76-Private-Server/Tools
- https://github.com/Fo76-Private-Server/Fo76_Communication
- https://github.com/Fo76-Private-Server/WinHttpWrapper
- https://github.com/Nexusphobiker/Fo76UDPServer
- https://github.com/keretus/sfe
- https://github.com/RobertBateman/F76SE
- https://github.com/FWDekker/fo76-dumps
- https://github.com/fo76utils/fo76utils
- https://github.com/AHeroicLlama/Mappalachia

### Server Emulation Demos
- https://peakd.com/@corianas/hpavrgse
- https://3speak.tv/watch?v=corianas/hpavrgse
- https://odysee.com/@F76:f/FO76-Terminals-Test:7
- https://myfo.online/

### Community & Forums
- https://discord.com/invite/fo76datamining
- https://discord.gg/p8FXc9k (Fo76-Private-Server Discord)
- https://www.gunetwork.org/t21133-fo76-singleplayer-offline-hack-discussion
- https://www.elitepvpers.com/forum/private-server/4945964-fallout-76-server-emulation.html
- https://guidedhacking.com/threads/fallout-76-cheat-table-trainer-25.15704/

### Technical References
- https://douggemhax.wordpress.com/2019/06/13/how-to-get-caught-by-fallouts-anti-cheat/
- https://www.jfedor.org/quake3/ (Quake 3 protocol)
- https://fabiensanglard.net/quake3/network.php (Quake 3 network model)
- https://www.nexusmods.com/fallout4/mods/47327 (FO4 Address Library - FO76 lacks equivalent)
- https://www.pcgamesn.com/fallout-76/fallout-76-making-of (Quake netcode integration story)
