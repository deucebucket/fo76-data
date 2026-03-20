# 046: Headless Fallout 76 Test Client - Technical Feasibility & Legal Analysis

**Date:** 2026-03-20
**Type:** Research / Feasibility Study
**Status:** Research Complete - Significant Legal and Technical Barriers Identified

---

## Executive Summary

Building a headless Fallout 76 test client is **technically conceivable but practically daunting and legally hazardous**. The FO76 network protocol has been partially reverse-engineered by community projects, but progress stalled years ago. The legal landscape is hostile: Bethesda's EULA explicitly prohibits reverse engineering, the DMCA anti-circumvention provisions apply to authentication bypass, the CFAA creates criminal exposure for unauthorized server access, and the bnetd v. Blizzard precedent directly addresses this exact scenario unfavorably. The distinction between "research" and "building a client" is legally meaningful but narrow.

---

## 1. Existing Reverse Engineering Efforts

### Fo76 Private Server Project (GitHub Organization)
- **URL:** https://github.com/Fo76-Private-Server
- **Status:** Largely inactive. 9 repositories, most archived. Last meaningful update was BnetAPI in December 2022.
- **What was built:**
  - `BnetAPI` - Login, community features, and matchmaking handling
  - `Fo76_Communication` - Library wrapping client-server communication
  - `Fo76_Packets` - Packet parsing and creation library (archived)
  - `Fo76_Snapshot` - Snapshot parsing (archived)
  - `Fo76_SnapshotCompression` - Compression algorithm reconstruction (archived)
  - `Fo76_UDPServer` - DTLS communication handler
  - `Tools` - Analysis utilities for game traffic
  - `WinHttpWrapper` - HTTP wrapper for forcing server connections
- **Languages:** C#, JavaScript, C++
- **Key takeaway:** They got far enough to parse packets, handle DTLS, and decompress snapshots, but the project appears abandoned. This is the most technically advanced public effort.

### Fo76UDPServer (Nexusphobiker)
- **URL:** https://github.com/Nexusphobiker/Fo76UDPServer
- **Status:** Dead. 3 commits. Only implements the initial handshake.
- **Language:** C#
- **Developer's own assessment:** "This needs a rewrite badly."

### Server76 (myfo.online)
- **URL:** https://myfo.online/
- **Status:** Unknown — landing page with links to Discord/Reddit/Patreon, no technical details public.
- **Notable quote from their site:** "Developing a server is legally fine, running one is against the Bethesda EULA."
- **Key takeaway:** They make a legal distinction between development and operation. This is a common community interpretation but has NOT been tested in court for Bethesda specifically.

### Server Emulator Proof-of-Concept (Corianas)
- **URL:** https://3speak.tv/watch?v=corianas/hpavrgse
- **Status:** Video demonstration existed, technical depth unknown. Appears to be a very early PoC.

### ElitePvPers Thread
- **URL:** https://www.elitepvpers.com/forum/private-server/4945964-fallout-76-server-emulation.html
- **Status:** Forum discussion about FO76 server emulation. Access blocked (403), but search results indicate the community acknowledges "high-level skills in reverse engineering are required."

### Summary of Protocol Knowledge
The community has identified:
- FO76 uses **UDP on ports 3000-3010** for game traffic
- Communication is wrapped in **DTLS** (Datagram Transport Layer Security)
- There is a separate **HTTP/HTTPS layer** for authentication via Bethesda.net
- The server architecture is **authoritative** — the server controls game state
- The world is divided into regions handled by separate server processes ("fog-based architecture")
- Snapshot data uses custom compression algorithms
- Authentication involves Bethesda.net account linking (Steam/Xbox/standalone) with MFA support

**What remains unknown publicly:**
- Complete packet format specifications
- World state synchronization protocol details
- Entity replication mechanisms
- The full authentication token flow (OAuth-like, but undocumented)
- Server-side validation logic
- Anti-cheat communication protocol (beyond window/process enumeration)

---

## 2. Private Server Emulation Projects

### Active Projects: Effectively None

All known public projects have stalled or gone underground:
- The Fo76-Private-Server GitHub org has archived its core repos
- Fo76UDPServer never got past handshake
- Server76's actual progress is hidden behind Discord/Patreon

### Why They Stall
1. **Complexity** — FO76 is a live-service MMO-lite with constant patches that change protocols
2. **DTLS encryption** — Traffic is encrypted, making passive observation difficult
3. **Authoritative server model** — Can't fake server responses without understanding the full state model
4. **Legal risk** — Developers get spooked (reasonably so)
5. **Small community** — Unlike WoW, the FO76 private server community is tiny

### Contrast with Other Bethesda Games

| Game | Emulation Status | Legal Action |
|------|-----------------|--------------|
| Morrowind | **OpenMW + TES3MP** — Full engine reimplementation with multiplayer. Mature, actively developed. Expanded to support FO3/FNV/FO4 as of v0.49.0 (July 2025). | None. Bethesda has never acted against OpenMW. |
| Skyrim | **SkyMP** — Multiplayer mod with custom Papyrus VM. Active development. | None known. |
| Fallout 4 | **OpenFallout4** — Very early RE project (7 commits, framerate fix focus). **CommonLibF4** — Reverse-engineered API library for modding. | None for these projects. |
| Fallout 76 | **Stalled** — Multiple abandoned attempts. | No known legal action, but no project got far enough to trigger it. |
| Elder Scrolls Online | No known emulation attempts (full MMO, vastly more complex). | N/A |

**Key observation:** Bethesda has historically tolerated single-player RE projects (OpenMW, CommonLibF4, SkyMP) but has never been tested on a multiplayer service emulator for a live commercial product.

---

## 3. Legal Landscape

### Three Overlapping Legal Frameworks

#### A. Bethesda EULA / Terms of Service
Bethesda's EULA explicitly prohibits:
- Modifying, adapting, reverse engineering the game
- Attempting to derive source code
- Disassembling or decompiling
- Creating derivative works

**However:** Bethesda has a long history of tolerating and even encouraging modding through official tools (Creation Kit). The EULA prohibition exists as a legal safety net, not as actively enforced policy — for single-player games. FO76 as a live service is a different context.

**Risk level for a headless client:** HIGH. A headless client that connects to Bethesda servers would almost certainly be considered a ToS violation, resulting in account bans at minimum.

#### B. DMCA (Digital Millennium Copyright Act)

The DMCA's anti-circumvention provisions (Section 1201) are the biggest legal threat:

- **Authentication handshakes** are "technical protection measures" (TPMs)
- Bypassing or reimplementing authentication to connect to game servers = circumvention
- The bnetd case (Blizzard v. bnetd, 2004-2005) established that CD key verification is a TPM, and emulating the authentication server violates the DMCA
- **No fair use defense worked** in bnetd — the court rejected interoperability arguments

The DMCA does contain a narrow reverse engineering exception for interoperability, but:
- It requires that RE is the "sole means" of achieving interoperability
- It only applies to "independently created computer programs"
- Courts have interpreted this very narrowly
- Building a game client to connect to someone else's servers is unlikely to qualify

**The Copyright Office explicitly rejected** a DMCA exemption for game server emulation in preservation contexts. If preservation doesn't qualify, research/testing certainly doesn't.

**Risk level:** VERY HIGH for anything that circumvents authentication or connects to live servers.

#### C. CFAA (Computer Fraud and Abuse Act)

The CFAA prohibits "accessing a computer without authorization or exceeding authorized access." This creates **criminal** (not just civil) exposure:

- Connecting to Bethesda's servers with an unauthorized client = potentially "exceeding authorized access"
- The Van Buren v. United States (2021) Supreme Court case narrowed CFAA scope somewhat, but connecting with a custom client to production servers remains risky
- If the headless client manipulates game state or accesses data not intended for the user, CFAA exposure increases

**Risk level:** MODERATE to HIGH, depending on whether you connect to live servers.

### Key Legal Precedents

| Case | Year | Relevance |
|------|------|-----------|
| **Sony v. Connectix** | 1999 | Intermediate copying for RE is fair use (console emulation). Favorable for RE generally. |
| **Sega v. Accolade** | 1992 | RE for interoperability is fair use when disassembly is the only way. Narrow applicability. |
| **Blizzard v. bnetd** | 2004 | Emulating authentication server violates DMCA. Directly adverse to headless client work. |
| **Blizzard v. Scapegaming** | 2010 | $88M judgment against WoW private server operator. Running a server = massive liability. |
| **Nintendo v. Yuzu** | 2024 | $2.4M settlement. No court ruling on merits, but chilling effect on emulation projects. |
| **Van Buren v. United States** | 2021 | Narrowed CFAA "exceeds authorized access." Slightly helpful but doesn't cover custom clients. |

### The Research vs. Building Distinction

This is the critical legal nuance:

**Likely Legal (Lower Risk):**
- Capturing your own network traffic with Wireshark while playing normally
- Analyzing packet structure from your own captures (observing, not circumventing)
- Reading publicly available reverse engineering research
- Documenting protocol observations without distributing circumvention tools
- Running fo76-dumps or fo76utils on your own game files (static data extraction, no server interaction)
- Building a Papyrus VM that runs scripts standalone (no game connection)
- Academic research and publication about protocol design

**Gray Area:**
- Decrypting DTLS traffic using keys extracted from the client (circumvention of TPM?)
- Building tools that parse game packets but don't connect to servers
- Reimplementing protocol handlers that could theoretically connect but don't
- Server76's position of "developing but not running"

**Likely Illegal / High Risk:**
- Building a client that authenticates with Bethesda.net servers
- Bypassing or reimplementing the authentication handshake
- Connecting a custom client to live Bethesda game servers
- Operating a private server that accepts connections from the real game client
- Distributing tools specifically designed to circumvent FO76's authentication

---

## 4. Papyrus VM: Standalone Viability

### Existing Standalone Implementation: PapyrusVM (SkyMP)

The SkyMP project (Skyrim Multiplayer) has built a standalone Papyrus Virtual Machine:
- **What it does:** Executes `.pex` (compiled Papyrus) bytecode outside the game engine
- **Language:** C++
- **Features:**
  - Loads and runs compiled Papyrus scripts
  - Supports custom native function registration
  - Hot-reload during development
  - Event-driven execution model
  - Cross-platform (any C++ target)
- **Limitations:**
  - Only implements a subset of Skyrim's Papyrus API
  - Complex script-heavy mods may not work
  - Missing many vanilla native functions
  - Stub implementations for some functions (e.g., SetScale does nothing)

### Applicability to FO76
- FO76 uses Papyrus (evolved from Skyrim/FO4 version)
- The PapyrusVM could theoretically run FO76 `.pex` files, but:
  - FO76 Papyrus has multiplayer-specific extensions not in Skyrim's version
  - Native function bindings would need to be reimplemented for FO76's specific APIs
  - Without the game engine backing the native calls, scripts would execute but couldn't interact with world state
  - Could be useful for **script analysis and testing** without needing the full client
- **Legal status:** Building/using a Papyrus VM is likely fine — it's a clean-room reimplementation of a scripting language, not circumvention of protection measures.

### Open-Source Papyrus Compilers
- `open-papyrus/papyrus-compiler` — Open-source Papyrus compiler
- `russo-2025/papyrus-compiler` — Compiler in V language with PEX analysis
- `zerratar/PapyrusDotNet` — .NET Papyrus compiler for FO4/Skyrim
- These could compile and analyze FO76 scripts without the game

---

## 5. fo76-dumps: Data Extraction Method

### How It Works
- **Repository:** https://github.com/FWDekker/fo76-dumps
- **Method:** Python script (`fo76dumps.py`) using **xEdit** and **ba2extract**
- **Process:**
  1. `ba2extract` unpacks Bethesda Archive (.ba2) files from the game installation
  2. xEdit (with custom scripts in `Edit scripts/`) parses ESM/ESP plugin files
  3. Python orchestrates the pipeline and formats output
- **Output formats:** CSV, JSON, Wikitext, SQLite database
- **Data extracted:** Form IDs, NPC data, dialogue, item stats, game settings, keywords
- **Release cycle:** New dump with each game patch

### What It Does NOT Do
- Does NOT interact with game servers
- Does NOT capture network traffic
- Does NOT reverse engineer the protocol
- Does NOT extract runtime/server-side data
- Purely **static file analysis** of the game's local data files

### Complementary Tool: fo76utils
- **Repository:** https://github.com/fo76utils/fo76utils
- **What it does:** Renders worldspaces, extracts and visualizes ESM data
- **Language:** C++ (88.4%)
- **Supports:** FO76, FO4, and older Elder Scrolls games (limited Starfield)
- **Also purely static** — no server interaction

### Legal Status
These tools are **almost certainly legal** — they parse files you own from a game you purchased. No circumvention, no server access, no authentication bypass. This is equivalent to hex-editing your own files.

---

## 6. Traffic Interception Feasibility

### What Could Be Captured
- FO76 uses **UDP 3000-3010** for game traffic
- HTTP/HTTPS for Bethesda.net authentication and API calls
- Wireshark can capture all of this on your own network

### Practical Wireshark Approach
```
# Capture filter for FO76 game traffic
udp portrange 3000-3010

# Display filter for FO76 after capture
udp.port >= 3000 && udp.port <= 3010

# Capture authentication traffic
tcp.port == 443 && ip.addr == [bethesda.net IP]
```

### The DTLS Problem
- Game traffic is **DTLS-encrypted** (TLS over UDP)
- Wireshark CAN decrypt DTLS if you have the session keys
- Getting the keys requires either:
  - Extracting them from the client process memory (invasive, likely ToS violation)
  - MITM proxying (requires certificate manipulation, circumvention)
  - Hooking the client's TLS library (code injection, definitely ToS violation)
- Without decryption, you can observe:
  - Packet sizes and timing patterns
  - Connection establishment sequences
  - Server IP addresses and port usage
  - Traffic volume correlations with in-game events
- **This metadata analysis is likely legal** — observing your own traffic without circumvention

### Legal Assessment of Traffic Capture
- **Capturing your own unencrypted traffic:** Legal
- **Observing encrypted packet metadata:** Legal (no circumvention)
- **Decrypting traffic via key extraction:** Gray area to illegal (circumvention of TPM)
- **MITM attack on your own connection:** Likely circumvention under DMCA

---

## 7. Headless Client Requirements

If someone were to build a headless FO76 client (purely theoretical), it would need:

### Authentication Layer
1. Bethesda.net account authentication (HTTPS)
2. Platform linking (Steam/Xbox integration)
3. Session token acquisition
4. MFA handling
5. Character selection/creation API
6. Server assignment/matchmaking

### Network Layer
1. DTLS handshake with game server
2. UDP packet framing and sequencing
3. Custom compression/decompression (the Fo76_SnapshotCompression project worked on this)
4. Packet parsing for all message types
5. Keep-alive and heartbeat mechanisms
6. Disconnect/reconnect handling

### Game State Layer
1. World state synchronization (cell loading, entity tracking)
2. Player state management (position, inventory, stats, perks)
3. NPC state tracking
4. Event system participation
5. Combat state machine
6. Quest state tracking

### Anti-Cheat Evasion (if connecting to live servers)
1. Window enumeration responses (fake being a normal game window)
2. Process list responses (hide analysis tools)
3. Debugger detection responses
4. Module enumeration responses
5. Periodic integrity checks

### Rendering (Optional for headless)
- Not needed if truly headless
- But the server may validate client behavior that implies rendering is occurring
- Some anti-cheat checks may require valid rendering state responses

### Estimated Complexity
This is roughly equivalent to building an MMO client from scratch with zero documentation. The WoW emulation community (MaNGOS, TrinityCore, AzerothCore) took **15+ years** with thousands of contributors to reach maturity, and WoW's protocol was far more extensively documented by its larger community.

---

## 8. Creation Engine Server Emulators for Other Games

### OpenMW + TES3MP (Morrowind) — The Gold Standard
- Full engine reimplementation (not just server)
- Multiplayer added via TES3MP
- Server-side Lua scripting
- As of v0.49.0 (July 2025), expanding to support FO3, FNV, FO4
- **Key difference from FO76:** Morrowind is single-player; multiplayer was added by the community, not reverse-engineered from an existing server
- **Legal status:** Tolerated by Bethesda for 10+ years. Requires owning the original game.

### SkyMP (Skyrim Multiplayer)
- Multiplayer mod with custom Papyrus VM
- Server component in Node.js + C++
- Client hooks into the existing Skyrim client
- **Key difference:** Adds multiplayer to a single-player game, doesn't emulate an existing service
- **Legal status:** Appears tolerated

### No Direct FO76 Analogue Exists
The critical difference: OpenMW and SkyMP add new functionality to single-player games. A FO76 headless client would replicate existing functionality of a live commercial service. This is legally and technically a completely different proposition.

---

## 9. Packet Capture Tools

### General Tools Applicable to FO76
- **Wireshark** — Full packet capture and analysis. DTLS dissector available but needs session keys.
- **tcpdump** — Command-line capture, good for automated logging
- **mitmproxy** — For HTTPS authentication traffic (but MITM = circumvention risk)
- **Fiddler** — HTTP/HTTPS proxy, useful for Bethesda.net API calls

### FO76-Specific Tools (from Fo76-Private-Server project)
- **Fo76_Packets** — Packet parsing library (C#, archived)
- **Tools** — Analysis utilities for game traffic
- **Fo76_SnapshotCompression** — Decompression of game state snapshots

### Game Hacking Tools (referenced in anti-cheat analysis)
FO76's anti-cheat specifically scans for:
- Cheat Engine (and variants)
- x64dbg
- IDA Pro
- WinDbg
- MHS (Memory Hacking Software)

Running these while FO76 is active will flag your account. Wireshark and tcpdump are **not** on the known blacklist, making passive network capture lower risk from an anti-cheat perspective.

---

## 10. "Observing the Protocol" vs "Building a Client"

### The Legal Spectrum

```
SAFER ◄──────────────────────────────────────────────► RISKIER

Reading public     Capturing your    Decrypting    Building a     Connecting to    Operating a
research about     own network       captured      client that    live Bethesda     private server
the protocol       traffic metadata  DTLS traffic  could connect  servers with it   accepting real
                   (packet sizes,                                                    game clients
                   timing, IPs)

[Likely Legal]     [Likely Legal]    [Gray Area]   [ToS Violation] [DMCA + CFAA]    [Full Liability]
```

### What "Observing" Means Legally
- You can watch packets flow on your own network
- You can note packet sizes, timing, frequency
- You can correlate traffic patterns with in-game events
- You can identify server IPs and port usage
- You can document the DTLS handshake structure (it's a standard protocol)
- You CANNOT decrypt the payload without risking DMCA anti-circumvention claims

### What "Building a Client" Means Legally
- Implementing authentication = circumventing a TPM (DMCA 1201)
- Connecting to live servers = potentially exceeding authorized access (CFAA)
- Even if you never run it, distributing circumvention tools is independently illegal under DMCA

### The Server76 Interpretation
Server76 claims "developing a server is legally fine, running one is against the Bethesda EULA." This is:
- **Partially correct:** Writing code that parses packets is probably fine
- **Incomplete:** If the code circumvents protection measures, even possessing/distributing it may violate DMCA
- **Untested:** No court has ruled on this specific claim for Bethesda products
- **Not a defense:** The bnetd case suggests courts may not draw this line favorably

---

## Conclusions and Recommendations

### What IS Feasible and Lower-Risk
1. **Static data analysis** using fo76-dumps, fo76utils, xEdit — fully legal, very useful
2. **Papyrus script analysis** using standalone VMs — legal, could reveal game logic
3. **Passive traffic metadata observation** — legal, limited utility without decryption
4. **Academic protocol research** — reading and documenting public findings
5. **Building tools that parse game files** without server interaction

### What Is Technically Possible but Legally Dangerous
1. **DTLS traffic decryption** — technically possible but likely DMCA circumvention
2. **Authentication flow reimplementation** — definitively circumvention
3. **Headless client connecting to live servers** — DMCA + CFAA + ToS triple threat
4. **Private server operation** — bnetd precedent makes this extremely risky

### What Is Practically Impossible (Currently)
1. **Full headless client** — Not enough protocol documentation exists publicly
2. **Private server at game-quality fidelity** — Would require years of work by a large team
3. **Running the server-side game logic** — It's not in the client files; it runs on Bethesda's infrastructure

### Honest Assessment
The FO76 headless client idea is:
- **10% feasible** from a technical standpoint (handshake works, everything else is unknown)
- **0% safe** from a legal standpoint if it connects to live servers
- **Somewhat useful** as a static analysis / Papyrus VM project that never touches the network
- **Years away** from any functional implementation even with a dedicated team

The WoW emulation community (the most successful game server emulation effort in history) had millions of players providing motivation, extensive protocol documentation, and a 15-year head start. FO76 has none of these advantages.

### Alternative Approaches Worth Considering
Instead of a headless client, consider:
1. **Enhanced static analysis** — More sophisticated ESM/BA2 parsing for game data research
2. **Papyrus script decompilation and analysis** — Understand game logic without network interaction
3. **Client-side modding** (SFE when updated) — Work within the existing client
4. **Bethesda's official Custom Worlds** (Fallout 1st) — Limited but legal customization
5. **OpenMW expansion** — The v0.49.0 expansion to FO3/FNV/FO4 may eventually provide a legal engine alternative, though FO76 multiplayer support is far off

---

## Sources

### GitHub Projects
- [Fo76 Private Server Project](https://github.com/Fo76-Private-Server)
- [Fo76UDPServer](https://github.com/Nexusphobiker/Fo76UDPServer)
- [fo76-dumps](https://github.com/FWDekker/fo76-dumps)
- [fo76utils](https://github.com/fo76utils/fo76utils)
- [OpenFallout4](https://github.com/ZehMatt/OpenFallout4)
- [CommonLibF4](https://github.com/Ryan-rsm-McKenzie/CommonLibF4)
- [SkyMP (Skyrim Multiplayer)](https://github.com/skyrim-multiplayer/skymp)
- [Open Papyrus Compiler](https://github.com/open-papyrus/papyrus-compiler)
- [TES3MP](https://github.com/TES3MP/TES3MP)

### Legal Resources
- [EFF Reverse Engineering FAQ](https://www.eff.org/issues/coders/reverse-engineering-faq)
- [Bethesda EULA](https://bethesda.net/data/eula/en.html)
- [Server76](https://myfo.online/)
- [The Lawbringer: A Primer on Private Servers (Engadget)](https://www.engadget.com/2011-01-28-the-lawbringer-a-primer-on-private-servers.html)
- [Blizzard Wins $88M Against WoW Private Server](https://www.gamerlaw.co.uk/2010/blizzard-wins-88m-lawsuit-against-wow-private-server-owner/)
- [Nintendo v. Yuzu Analysis (Argo Law)](https://argolawyer.com/the-possibly-illegal-world-of-video-game-emulators-understanding-yuzu/)
- [Legal Status of Emulation (Emulation Wiki)](https://emulation.gametechwiki.com/index.php/Legal_status_of_emulation)
- [IPWatchdog: Reverse Engineering and the Law](https://ipwatchdog.com/2021/03/27/reverse-engineering-law-understand-restrictions-minimize-risks/id=131543/)
- [Gamasutra: Reverse Engineering and You](https://www.gamedeveloper.com/game-platforms/analysis-reverse-engineering-and-you)
- [Video Game Modding in U.S. IP Law (Digital Law Journal)](https://www.digitallawjournal.org/jour/article/view/119?locale=en_US)

### Technical Resources
- [Douggem: How to Get Caught by Fallout's Anti-Cheat](https://douggemhax.wordpress.com/2019/06/13/how-to-get-caught-by-fallouts-anti-cheat/)
- [SkyMP Papyrus Integration (DeepWiki)](https://deepwiki.com/skyrim-multiplayer/skymp/2.7-papyrus-integration)
- [OpenMW Multiplayer Announcement](https://openmw.org/2017/openmw-multiplayer-here/)
- [FO76 Port Forwarding (Bethesda Support)](https://help.bethesda.net/app/answers/detail/a_id/44035/)
- [Game Hacking Academy: Packet Analysis](https://gamehacking.academy/pages/6/02/)
