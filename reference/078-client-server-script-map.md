# Finding 078: Client vs Server Papyrus Script Execution Map

**Date:** 2026-03-20
**Source:** misc_extracted/scripts/client/ archive (2,854 .pex files), scripts_decompiled/ (7,095 .psc files), full_esm_dump.txt
**Method:** Diff client archive against full decompiled set, cross-reference with RMI/sync patterns and ESM keywords

---

## Executive Summary

Of 7,095 total Papyrus scripts in Fallout 76, **2,854 (40.2%) run client-side** and **4,273 (59.8%) run server-only**. Script execution context is NOT determined by anything in the Papyrus code itself — it's controlled by ESM keywords attached to the objects that carry the scripts (confirmed by MPScriptTest pattern in finding 032).

The client archive contains virtually all "default" framework scripts (392 of 395), all base engine classes (59 types), and the vast majority of quest logic, visual effects, sound, animations, traps, CAMP objects, and UI scripts. The server retains control of spawning, loot drops, boss management, item grants, faction changes, vendor transactions, and auto-generated fragments (quest stages, terminal menus, packages, perks).

**Bottom line for modding:** The client-side surface is enormous. If SFE can inject modified .pex files, almost every player-facing system is touchable — visuals, audio, animations, CAMP, traps, quest triggers, even some economy-adjacent scripts. The server validates outcomes but the client runs most of the game logic.

---

## 1. Client-Side Scripts (2,854 total)

### Breakdown

| Category | Count | Notes |
|----------|-------|-------|
| Non-fragment scripts | 2,853 | Real scripts with game logic |
| Fragment scripts (qf_/pf_/prkf_/term_) | 1 | Nearly all fragments are server-only |
| Base engine classes | 59 | Actor, ObjectReference, Quest, Perk, Weapon, etc. |
| Default framework scripts | 392 | DefaultSetStageOnActivate, DefaultEnableOnTrigger, etc. |
| Quest-specific scripts | ~752 | EN, LC, WL, MOM, CB, FS, SFS, BURN, MTR, STORM, BOS, etc. |
| Visual FX / Effects | ~155 | Explosions, particles, glow, shaders, imagespace |
| Sound / Audio | ~72 | Audio activators, speakers, radios, klaxons, music |
| Workshop / CAMP | ~65 | COMP_ scripts, workshop objects, power, displays |
| Trap scripts | 43 | All trap types: bear traps, tripwires, flame, gas, etc. |
| Debug / Test | ~117 | Debug tools, test scripts, QA automation |
| Chargen | 29 | Character creation, barber, perk boards |
| Animation | 18 | Direct animation control scripts |
| Camera | 8 | Camera shake, attachment, dialogue camera |
| Creature / NPC | ~71 | Race scripts, creature behavior, AI |
| Arcade / Minigames | 16 | Bottle blaster, whack-a-mole, Nuka Zapper |
| Terminal scripts | 71 | Terminal interaction logic |
| Perk scripts | 46 | Perk card effects, application |
| Nuclear / Silo | 41 | Nuke launch, silo interaction, fissures |
| Power Armor | ~10 | PA chassis, FX, battery, stealth, medic pump |
| ATX (Atom Shop) | 9 | Cosmetic/store items |

### Base Engine Classes (Client-Side)

All 59 Papyrus base types ship in the client archive:

```
Action, Activator, ActiveMagicEffect, Actor, ActorBase, ActorValue,
Alias, Ammo, Armor, Book, Cell, Component, ConstructibleObject,
Container, Debug (x2), Enchantment, Faction, Flora, Form, FormList,
Furniture, Game, GlobalVariable, Hazard, HeadPart, Holotape, Idle,
ImageSpaceModifier, Ingredient, Keyword, LeveledActor, LeveledItem,
Location, MagicEffect, Math, Message, MiscObject, MusicType, ObjectMod,
ObjectReference, Outfit, Perk, Potion, Quest, Race, Scene, ScriptObject,
Sound, SoundCategorySnapshot, Spell, Topic, TopicInfo, Utility,
VisualEffect, VoiceType, Weapon, Weather, WorldSpace
```

This means the client has access to every Native function defined on these types. The full Papyrus API surface is available client-side.

---

## 2. Server-Only Scripts (4,273 total)

### Breakdown

| Category | Count | Notes |
|----------|-------|-------|
| Auto-generated fragments | 2,510 | qf_ (quest), pf_ (package), prkf_ (perk), term_ (terminal), ti_ (topic info), sf_ (scene) |
| Non-fragment scripts | 1,763 | Actual unique game logic |

### Key Server-Only Systems

**Boss / Enemy Management (13 scripts)**
```
assaultronbossscript, bossenemyscript, bosslootdrop, bossscript,
drifterbossscript, flatwoodsbossscript, jerseydevilbossscript,
lc096_legendarybosstrigger, midbosscollectionscript,
regionbossquestscript, smbehemothbossracescript,
stormbossaliasscript, stormbossracescript
```

**Spawning / Encounters (18 scripts)**
```
baseencounterscript, burn_bounty_gruntspawnscript,
burn_bounty_headhuntspawnscript, dlc01robobrainghostspawn,
kindlingspawner, lightningrespawnaliasscript,
mile_encountermodulescript, petspawnfurniturescript,
respawnpoint (x5 variants), respawnpointmanager,
spawnai, spawnallitems, spawnandkillai, spawnpartycrasher
```

**Loot / Drops (3 scripts)**
```
bosslootdrop, gatherloot, glowinglootdrop
```

**Item Operations (6 scripts)**
```
aliasonactivateremovemultipleitems, equipitemonactivate,
festivegiftadditem, refcollectionaliasadditem,
spawnallitems, topicinfoexchangeitemsorcurrency
```

**Economy / Vendors (4 scripts)**
```
disguisevendorscript, disguisevendortopicinfoscript,
topicinfoexchangeitemsorcurrency, vendingmachinescript
```

**Faction / Reputation (6 scripts)**
```
addtofaction, cb04_addfactionperkscript, cb04_addtofactionscript,
dlc01manytomanyfactionrelationscript, dlc01onetomanyfactionrelationscript,
dlc01playerfactionrelationscript
```

**Perk / Mutation (Server Logic) (17 scripts)**
```
cb04_addfactionperkscript, dailymutation, defaultdisplayperkfanfare,
defaultitemgrantperkscript, defaultmutation, dlc01botremoveperk,
dlc01_perksearchscript, eventmutationscript, frogcollectingperkscript,
lunchboxperkfanfarescript, mile_hurrybrahminperkmanager,
modammoamountperkscript, modelementalperkscript, perkcardtests,
specialbonusperkcardstests, timeofdayperkcardstests, update0_addperks
```

**Health / Damage (Server Validation) (8 scripts)**
```
aliashealthbarscript, collaliashealthbarscript, damagetest,
dlc01_babylonstimpakisactiveeffect, eyebotrepairscript,
setstageonhealthpercent, setstageonhealththreshold, usestimpak
```

**Lunchbox / Score (7 scripts)**
```
lunchboxeffectscript, lunchboxmessagescript, lunchboxperkfanfarescript,
lunchboxplacescript, lunchboxvfxscript, lunchboxxpscript,
badgehandlerquestscript
```

**Recipe / Crafting Unlock (3 scripts)**
```
objectivemodule_craftandplace, scorchbeastrecipesscript,
unlocktaxidermyrecipesscript
```

### Server-Only Fragments (2,510)

These are auto-generated by the Creation Kit and run entirely server-side:

| Prefix | Type | Count | Significance |
|--------|------|-------|--------------|
| qf_ | Quest stage fragments | ~900+ | ALL quest stage logic runs server-side |
| pf_ | Package fragments | ~400+ | NPC AI packages run server-side |
| prkf_ | Perk fragments | ~200+ | Perk effect calculations run server-side |
| term_ | Terminal menu fragments | ~700+ | Terminal menu actions run server-side |
| ti_ / tif_ | Topic info fragments | ~150+ | Dialogue result scripts run server-side |
| sf_ | Scene fragments | ~50+ | Scene action scripts run server-side |

**This is the critical insight:** Even though quest trigger scripts (DefaultSetStageOnActivate, etc.) run client-side, the actual quest stage logic (what happens when stage X is set) runs server-side via qf_ fragments. The client fires the trigger; the server decides what happens.

---

## 3. Hybrid Scripts: Client-Server Boundary Crossings

### Scripts Using SendRMIToServer (20 scripts)

These scripts run client-side but can call server functions. The client initiates; the server executes.

| Script | Context | What It Does |
|--------|---------|-------------|
| arcadenukazapperracerocket | CLIENT | Arcade game score → server |
| arcadeshootinggallerytarget | CLIENT | Target hit → server registers |
| arcadewhackamoletarget | CLIENT | Whack hit → server registers |
| chargenfacechairscript | CLIENT | Face gen → server saves |
| chargenplayeractorscript | CLIENT | Photo mode/face gen → server |
| comp_multistateclientsideanimwcomp | CLIENT | Request event state from server |
| lasergridscript | CLIENT | Laser grid interaction → server |
| lc060_whitespringbarberscript | CLIENT | Barber → server saves |
| lc080_modusrevealmanagerscript | CLIENT | MODUS reveal → server |
| missionquestactivatorscript | CLIENT | Mission activator → server |
| mom02bswordactivatorscript | CLIENT | Sword visibility → server |
| msilolasergridscript | CLIENT | Silo laser grid → server |
| storm_weatherstationbuttonscript | CLIENT | Weather station → server |
| v96_vaultexteriorgeardoorscript | CLIENT | Vault door → server |
| w05_waywardstateswaprefscript | CLIENT | Wayward state → server |
| wl029_waywardstatechangemanagerscript | CLIENT | Wayward state change → server |
| scriptobject | CLIENT | Base class defines SendRMIToServer Native |
| mpscripttestserverrmikeyword | CLIENT | Test harness |
| lgvanimcontroller | SERVER | Legendary vendor animations (server-only) |
| playerscript | SERVER | Raid quest removal (server-only) |

**21 unique RMI function names found:**
```
BecomeVulnerable, CheckMODUSRevealStateRMI, CheckPlayerWaywardValue,
ClearMissionQuestExit, PerformMissionQuestExit, ReevaluateConditions,
RegisterSpeedup, RegisterWin, RemovePlayerFromRaid,
RequestCollisionUpdate, RequestEventState, RequestSwordVisibility,
RequestUpdateExteriorGearDoorStateForPlayerOnClientLoad,
ServerPlayLooksMenuEventComment, ServerRMIFunction,
TellQuestIntroVideoHasFinished, TellQuestWeHaveLeftFaceGen,
TellQuestWeHaveLeftPhotoMode, TurnOff, UpdateLinkedButtonState,
UpdateScore
```

### Scripts Using OnSyncVariableNetworkChanged (28 scripts)

These respond to server-pushed variable updates. The server changes a synced variable; the client reacts (usually visual/audio).

| Script | Context | What Syncs |
|--------|---------|-----------|
| default2stateactivator | CLIENT | Animation state (open/closed) |
| defaultsequentialstateactivator | CLIENT | Sequential animation states |
| cyclicelectricalhazard | CLIENT | Hazard on/off visual |
| trapelectricarc | CLIENT | Trap active state |
| powerboxscript | CLIENT | Power state visual |
| workshoplightboxscript | CLIENT | Light state |
| workshoppowercounterscript | CLIENT | Counter display |
| workshoppoweredspeakerscript | CLIENT | Speaker active state |
| resourcegeneratorbuttonscript | CLIENT | Generator button state |
| klaxonmanagerscript | CLIENT | Alarm visual/audio |
| flipcardsigncounterscript | CLIENT | Sign counter display |
| en07_nukesilocameraattachscript | CLIENT | Silo camera state |
| lc060_whitespringbarberscript | CLIENT | Barber state |
| lc101rotationscript | CLIENT | Rotation state |
| mtr03_autominerconsolerefscript | CLIENT | Mine console state |
| raidhackmasterscript | CLIENT | Raid hack progress |
| sfs08_heart_stranglerheartscript | CLIENT | Strangler Heart state |
| storm_weatherstationbuttonscript | CLIENT | Weather station state |
| atx_nukamysterymachine | CLIENT | Mystery machine state |
| activemagiceffect | CLIENT | Base class definition |
| objectreference | CLIENT | Base class definition |
| mpscripttestsyncpropertykeyword | CLIENT | Test harness |
| atxslotmachinescript | SERVER | Slot machine state |
| dlc01_containeraudio | SERVER | Container audio sync |
| hiddencrateaudio | SERVER | Hidden crate audio sync |
| objectivemodule_repelenemies_refr | SERVER | Enemy repel state |
| xpd_ac_casinogame | SERVER | Casino game state |
| xpd_ac_slotmachine | SERVER | Slot machine state |

### The Pattern

```
CLIENT triggers action → SendRMIToServer("FunctionName", Params)
SERVER validates & processes → changes synced variables
SERVER pushes state → OnSyncVariableNetworkChanged fires on CLIENT
CLIENT updates visuals/audio based on new state
```

The client is the presentation layer. It handles input, triggers, animations, FX, and sound. The server handles validation, state changes, item operations, and progression.

---

## 4. Trust Boundary Map

### CLIENT = Moddable (if SFE works)

These systems run client-side Papyrus and can be modified by replacing .pex files:

| System | Moddable? | Scripts | Risk Level |
|--------|-----------|---------|-----------|
| **Visual FX** | YES | ~155 scripts | Low — cosmetic only |
| **Sound / Audio** | YES | ~72 scripts | Low — cosmetic only |
| **Animations** | YES | ~18+ scripts | Low — cosmetic only |
| **Camera** | YES | 8 scripts | Low — cosmetic only |
| **Traps** | YES | 43 scripts | Medium — could disable traps |
| **CAMP / Workshop** | YES | ~65 scripts | Medium — visual/functional |
| **Quest Triggers** | YES | ~392 default scripts | Medium — can fire stages |
| **Chargen / Barber** | YES | 29 scripts | Low — appearance only |
| **Arcade Games** | YES | 16 scripts | Low — minigame only |
| **Power Armor FX** | YES | ~10 scripts | Low — visual/audio |
| **Nuclear Silo (presentation)** | YES | ~41 scripts | Medium — UI/visual only |
| **Map / Location** | YES | ~54 scripts | Medium — display only |
| **ATX Cosmetics** | YES | 9 scripts | Low — cosmetic |
| **Creature Behavior (client)** | YES | ~71 scripts | Medium — AI/visual |
| **Perk Application (client)** | YES | ~46 scripts | Medium — display/trigger |

### SERVER = Locked, Cannot Modify

These systems run only on Bethesda's servers:

| System | Scripts | Why It's Locked |
|--------|---------|----------------|
| **Quest Stage Logic** | ~900+ qf_ fragments | ALL quest outcomes determined server-side |
| **NPC AI Packages** | ~400+ pf_ fragments | NPC behavior packages run server-side |
| **Perk Calculations** | ~200+ prkf_ fragments | Perk effect math runs server-side |
| **Terminal Actions** | ~700+ term_ fragments | Terminal menu results run server-side |
| **Dialogue Results** | ~150+ ti_/tif_ fragments | Dialogue choice outcomes server-side |
| **Boss Management** | 13 scripts | Boss health, phases, drops — all server |
| **Enemy Spawning** | 18+ scripts | What spawns, where, when — server decides |
| **Loot Generation** | 3+ scripts | What drops from what — server generates |
| **Item Grant / Remove** | 6+ scripts | Adding/removing items — server validates |
| **Vendor Transactions** | 4+ scripts | Buying/selling — server processes |
| **Faction Changes** | 6 scripts | Reputation changes — server authorizes |
| **Perk/Mutation Grants** | 17 scripts | Granting perks/mutations — server only |
| **Health/Damage Validation** | 8 scripts | Damage numbers — server calculates |
| **Score/Lunchbox Effects** | 7 scripts | Scoreboard progress — server tracks |
| **Recipe Unlocks** | 3 scripts | Learning plans — server authorizes |

### HYBRID = Client Triggers, Server Validates

These 44 scripts sit on the boundary. The client can trigger actions, but the server must authorize the result:

- **Arcade scores** — client detects hit, server registers the score
- **Chargen/barber** — client runs face editor, server saves the result
- **State activators** — client plays animation, server syncs state to all players
- **Workshop objects** — client interacts, server validates and syncs
- **Quest activators** — client fires trigger, server sets the stage
- **Raid mechanics** — client displays UI, server tracks progress

---

## 5. What's Client-Side Modifiable?

### Definitely Moddable

**UI / HUD / Messages** (~50 scripts)
- Message display, challenge notifications, quest prompts
- Menu item handlers (additemonmenuitemrun, etc.)
- PipBoy scripts

**Camera** (8 scripts)
- Camera shake, attachment, dialogue camera
- Tutorial camera, silo camera
- Could adjust FOV, shake intensity, camera behavior

**Animations** (18+ scripts)
- Direct animation playback and control
- Autodoc, bonfire, generator, windmill animations
- Could modify animation timing, add new animations to existing triggers

**Visual FX** (~155 scripts)
- Explosion effects, glow effects, particle systems
- Weather visuals, environmental FX
- ImageSpace modifiers
- Could dramatically alter game visuals

**Sound / Audio** (~72 scripts)
- Sound playback, audio activators
- Radio scripts, speaker systems
- Klaxon/siren/alarm audio
- Could replace sounds, adjust volumes, add new audio triggers

**Input Handling** (~84 scripts matching "key/button/controller")
- Keypad scripts, button activators
- Controller input scripts
- Could remap or modify input responses (within Papyrus limits)

**Quest Stage Display** (~47 scripts that call SetStage are client-side)
- Quest trigger scripts (DefaultSetStageOnActivate, etc.)
- Objective display scripts
- NOTE: Setting a stage is client-initiated but server-validated

**Map / Location** (~54 scripts)
- Location discovery, map markers
- Fast travel targets
- Spawn markers (visual only, actual spawn is server)

**Traps** (43 scripts)
- All trap types: bear, tripwire, flame, gas, spike, saw, punji
- Could modify trap behavior, damage FX, trigger distances
- NOTE: Actual damage numbers are server-validated

### Partially Moddable (Client Visuals, Server Logic)

**Workshop / CAMP** (~65 scripts)
- Object placement, power systems, displays — client handles
- Resource generation rates, vendor pricing — server controls
- Visual mods work; economic mods don't

**Nuclear Silo** (~41 scripts)
- Silo puzzle UI, camera, FX — client runs
- Launch authorization, target selection — server validates
- Could make silo runs more visually dramatic

**Power Armor** (~10 scripts)
- PA FX, battery insert animation, chassis visual — client
- PA stat effects, damage reduction — server via perk fragments

---

## 6. What's Locked Server-Side?

### Completely Locked

**Damage Calculation** — YES, locked server-side
- `damagetest`, `setstageonhealthpercent`, `setstageonhealththreshold`
- All prkf_ perk fragments that modify damage run server-side
- Client sees the result; never computes it

**Item Spawning / Loot** — YES, locked server-side
- `bosslootdrop`, `gatherloot`, `glowinglootdrop`
- All container contents generated server-side
- Legendary drops determined server-side

**Legendary Rolling** — YES, locked server-side
- `lc096_legendarybosstrigger`, `festive_legendaryscorched`
- Legendary effects are rolled server-side
- Client only sees the result

**XP Distribution** — YES, locked server-side
- `lunchboxxpscript` and XP-related systems
- XP awards processed server-side
- No client-side XP scripts found

**Currency Changes** — YES, locked server-side
- `topicinfoexchangeitemsorcurrency`
- All vendor transactions, cap transfers run server-side
- `vendingmachinescript` is server-only

**Faction / Reputation** — YES, locked server-side
- All 6 faction relation scripts are server-only
- Reputation gains/losses processed server-side

**Enemy Spawning** — YES, locked server-side
- 18+ spawn scripts are server-only
- `baseencounterscript` controls all encounters
- Client cannot force spawns

**Boss Mechanics** — YES, locked server-side
- All 13 boss scripts are server-only
- Boss phases, health gates, drops — all server

**Recipe / Plan Unlocks** — YES, locked server-side
- `scorchbeastrecipesscript`, `unlocktaxidermyrecipesscript`
- Learning recipes requires server authorization

---

## 7. ESM Keywords Controlling Execution Context

The ESM contains specific keywords that determine where scripts execute:

| Keyword | FormID | Purpose |
|---------|--------|---------|
| AllowNonActorToAnimateOnServer | 0x0052B545 | Lets non-actor objects animate server-side (used by MPScriptTest buttons) |
| AllowNonActorToAnimate | 0x00548236 | Enables animation for non-actors |
| NoSimulatedGraphOnServer | 0x005274F0 | Disables physics graph simulation server-side |
| ClientSpecificCollision | 0x003968AC | Collision only computed client-side |
| WaywardClientToggledObjectKeyword | 0x0058CE75 | Client-side toggle for Wayward quest objects |
| WaywardClientEnableKeyword | 0x0042F661 | Client-side enable for Wayward objects |

There is also a keyword described as: *"Call this keyword through script when you want to prevent an activating object from sending activation to the server"* — this explicitly controls the client/server activation boundary.

**The execution context model:**
1. The **script code itself** doesn't determine where it runs
2. The **ESM keyword** on the object carrying the script determines execution context
3. The **client archive** contains the .pex files the client needs
4. Scripts NOT in the client archive can never run client-side — they don't exist on the player's machine

---

## 8. Implications for Modding

### What SFE Enables
If SFE can replace .pex files in the client archive at runtime:
- **2,853 non-fragment scripts** are modifiable
- All base engine classes, all default framework scripts
- Visual overhaul of any system is possible
- Audio replacement/modification for any client-side trigger
- CAMP/workshop behavior modifications (visual/functional)
- Trap behavior changes
- Quest trigger timing and conditions (but not outcomes)

### What SFE Cannot Do
- Modify the 4,273 server-only scripts (they literally don't exist on the client)
- Change loot tables, damage formulas, XP rates, or currency
- Force item spawns, enemy spawns, or boss behavior changes
- Modify quest stage outcomes (only quest triggers are client-side)
- Bypass server validation for any economic or progression system

### The 2,510 Fragment Gap
The most significant finding: **all auto-generated fragments (quest stages, terminal actions, perk effects, dialogue results, scene actions) run exclusively server-side.** This means:
- A client mod can change WHEN a quest stage is triggered
- But it CANNOT change WHAT HAPPENS when that stage fires
- A client mod can change how a terminal looks or sounds
- But it CANNOT change what the terminal menu options DO
- A client mod can adjust perk card visuals or descriptions
- But it CANNOT change perk numerical effects

### Safe Modding Opportunities
1. **Visual/FX overhauls** — completely client-side, no server interaction
2. **Audio mods** — replace sounds, add ambient audio
3. **Camera mods** — adjust camera behavior, FOV, shake
4. **CAMP aesthetic mods** — visual changes to workshop objects
5. **Trap behavior** — modify trigger distances, visual effects
6. **Map/UI mods** — change how information is displayed
7. **Animation mods** — modify animation timing and playback

### Risky Modding (Detection Possible)
1. **Quest trigger manipulation** — server may flag unexpected stage triggers
2. **Disabling trap damage FX** — server still applies damage but client shows nothing
3. **Modifying creature client behavior** — may desync from server state
4. **Workshop functionality changes** — server validates resource operations

---

## Appendix: Script Counts by Content Area (Client-Side)

| Content Prefix | Full Name | Client Scripts |
|----------------|-----------|---------------|
| default | Framework scripts | 392 |
| wl/w05 | Wastelanders | 238 |
| en | Enclave / Endgame | 132 |
| debug/test | Debug & Testing | 117 |
| mtr/mtnl | Mire Trail | 111 |
| v94/v96 | Vault Raids | 79 |
| fs/sfs | Seasons Content | 43 |
| bos/bs | Brotherhood of Steel | 40 |
| burn | Backwoods Update | 37 |
| workshop | Workshop Objects | 36 |
| storm | Storm Content | 31 |
| comp_ | CAMP/Companion | 29 |
| chargen | Character Creation | 29 |
| sq | Side Quests | 23 |
| lc | Living Content | 21 |
| arcade | Arcade Games | 16 |
| cb | Content Bundles | 15 |
| mom | Mysteries of Morgantown | 11 |
| atx | Atom Shop | 9 |
| xpd | Expeditions | 6 |
| npe/d01 | New Player Experience | 5 |
| mile | Milestones | 3 |
| mq/ac_mq | Main Quest | 1 |

---

*Total client: 2,854 scripts (40.2%). Total server: 4,273 scripts (59.8%). The client runs the presentation layer; the server runs the authority layer. Bethesda's architecture is a clean split — the client is trusted with visuals and triggers, but never with outcomes or progression.*
