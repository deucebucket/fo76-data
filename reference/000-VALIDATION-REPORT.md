# Fallout 76 Findings Validation Report

**Date:** 2026-03-20
**Validator:** Cross-referenced against Nuka Knights datamining site, fed76.info, community wikis, and general FO76 community knowledge
**Scope:** All 22 finding files (001-022) in this directory

---

## OVERALL ASSESSMENT

**Honest verdict: Our work has significant value, but we need to be careful about framing.**

Nuka Knights -- the primary FO76 datamining site -- focuses almost exclusively on **Atomic Shop cosmetic leaks and season reward previews**. Their 54 datamining articles are overwhelmingly "here are the skins coming to the shop next week." They have ONE article on hidden mechanics (respawn/loot lists, from 2022). They do excellent work on patch note analysis (their Backwoods Patch 66 coverage is thorough and includes legendary mod changes, event restructuring, and Bigfoot details).

**What Nuka Knights does that we don't:** Atomic Shop item previews with rendered images, up-to-date patch note breakdowns, and practical player guides.

**What we do that nobody else does:** Deep script decompilation analysis revealing actual formulas, hidden SPECIAL stat influences, exact probabilities, debug infrastructure, and security analysis. This is a fundamentally different tier of datamining.

fed76.info documents practical gameplay strategies and pricing but does NOT reverse-engineer hidden formulas or probability systems.

The community generally knows the "what" but not the "how" or "why" of game systems. Our value is in providing the exact numbers behind systems players only have vague intuitions about.

---

## PER-FINDING VALIDATION

### Finding 001: Nuclear Winter Code Intact
**Status: OLD NEWS (surface level) / PARTIALLY KNOWN (our depth is new)**

The community widely knows NW was removed and NW.esm still ships with the game. This has been discussed on Reddit extensively since the September 2021 sunset. The "Babylon" codename was documented by dataminers years ago. The Vault 51 lore is on every wiki.

**What's actually new from us:** The full technical autopsy (Finding 016) documenting 28 native engine functions, the storm wall particle system parameters, the complete AI wave structure, and the gamemode keyword architecture that would allow reactivation. Nobody has documented the DEPTH of integration at the level we did. The community says "NW code is still there." We say "here are the exact 28 native functions, the constriction phase structs, and the gamemode toggling mechanism."

**Embarrassment risk:** LOW if we frame it as a technical deep-dive. HIGH if we present it as "we discovered NW code is still in the files" -- that's 5-year-old news.

---

### Finding 002: Atlantic City Casino System
**Status: PARTIALLY KNOWN**

The Atlantic City casino furniture and slot machines are visible in-game as decorative objects. Players know the casino exists but can't gamble. The "casino disabled" error message has been spotted by players who tried interacting with tables.

**What's actually new from us:** The complete 6-game system breakdown (Finding 006) showing roulette, derby, craps, and two slot machine variants plus the "World's Biggest Slot." The multiplayer-aware code, power requirements, and server-side result syncing. The specific implementation showing it was server-togglable.

**Embarrassment risk:** MEDIUM. Players know the casino is decorative. Documenting the full disabled system is incrementally interesting but not groundbreaking. The regulatory angle (gambling + microtransactions) is speculation that others have also made.

---

### Finding 003: Ghoul Player System
**Status: OLD NEWS -- THIS IS RELEASED CONTENT**

**WRONG CALL.** Playable Ghouls launched with the "Ghoulvolution" update (Patch 57, late 2024). This is active, released content that players use daily. Our finding describes it as if it's a secret discovery. The server-side disable toggle, the feral state references, and the ghoul perks are all documented on wikis.

**Embarrassment risk:** HIGH. Presenting released content as a "finding" would be embarrassing. The only mildly interesting detail is the server-side toggle for disabling ghouls during maintenance, but that's an operational detail, not a secret.

---

### Finding 004: Vault 65 Unreleased
**Status: PARTIALLY KNOWN**

Community speculation about future vaults has included Vault 65 on wishlists for years. The string reference alone is not particularly notable. The cross-reference with Vault 120 is mildly interesting.

**What's actually new:** Not much. A single string reference without additional context (no quests, no cells, no NPCs) is thin evidence.

**Embarrassment risk:** MEDIUM. It's a real data point but a weak finding on its own.

---

### Finding 005: Mothman Cult Hierarchy
**Status: OLD NEWS**

The Mysteries of the Mothman (MoM) questline, the Enlightened vs. Dim Ones schism, the rank system (Initiate through Master), and the Interloper connection are all released, documented game content. This shipped with various updates and is thoroughly covered on wikis.

**Embarrassment risk:** HIGH. This is all released content presented as if we discovered it.

---

### Finding 006: Casino Full System
**Status: PARTIALLY KNOWN (see Finding 002 above)**

The technical implementation details (6 game types, multiplayer sync, power requirement) add value beyond what's publicly known. The "Derby" game type suggesting creature/horse racing is genuinely undocumented.

**Embarrassment risk:** LOW if framed correctly.

---

### Finding 007: Nuclear Winter AI Bot
**Status: GENUINELY NOVEL (technical depth)**

The automated NW testing bot (babylontest.psc) with its 12 weapon loadouts, auto-fire timers, loot cycle mechanics, and storm zone navigation has not been documented by community dataminers. This is genuinely new technical content.

**Embarrassment risk:** NONE. This is legitimately new and interesting.

---

### Finding 008: AI Follower Reference Architecture
**Status: GENUINELY NOVEL (our interpretation)**

This is our own analysis connecting the bot framework to AI companion possibilities. It's not a "finding" about the game so much as an engineering analysis. Valid and interesting but not a datamine discovery.

**Embarrassment risk:** NONE, but it's a project planning document, not a community-facing finding.

---

### Finding 009: Bethesda QA Bot Suite
**Status: GENUINELY NOVEL**

The 48-script automated testing framework (ExploreWorld, GrindMonsters, MassCombat, etc.) with specific native functions like SetAIDriven, PathToReference, and FindRandomCombatTarget has NOT been documented by community dataminers. This is genuinely new and technically significant.

**Embarrassment risk:** NONE. This is one of our strongest findings.

---

### Finding 010: Complete AI Bot Framework
**Status: GENUINELY NOVEL**

Extension of Finding 009. Same assessment -- genuinely novel technical documentation.

---

### Finding 011: Hidden LUCK Formulas
**Status: GENUINELY NOVEL -- THIS IS OUR BEST WORK**

The exact bomb defusal formula (Roll + Luck*0.8 + Intelligence*1.6, threshold 85), the slot machine hot-streak Luck buff, the arcade game Strength/Luck multipliers, and the Scorchbeast attack cooldown system are NOT documented ANYWHERE in the community. Fed76 doesn't have these. Nuka Knights doesn't have these. The wikis don't have these.

This is the kind of content that would genuinely benefit the community and establish credibility.

**Embarrassment risk:** NONE. Pure gold.

---

### Finding 012: 4-Star Legendary 50% Chance
**Status: GENUINELY NOVEL**

The exact Rank4Chance = 0.5 default, the fact that 4-star is determined at spawn (not kill), and the per-placement override system are not documented in any community resource I found. The community has vague estimates ("maybe 10-20%?") but nobody has published the actual 50% default value.

**Embarrassment risk:** NONE. This will surprise people and is backed by exact script evidence.

---

### Finding 013: Power Plant Hidden Systems
**Status: PARTIALLY KNOWN**

Players know power plants degrade and need repair. The 7-day entropy timeline, exact thresholds, and the TODO-marked player-count scaling that was never implemented are NOT publicly documented with exact values.

**What's new:** The exact constants (7 days to failure, 25% failure threshold, 10-minute timer intervals) and the revelation that player-count scaling was planned but never implemented.

**Embarrassment risk:** LOW. The existence of decay is known; the exact numbers are not.

---

### Finding 014: Hidden Mechanics Deep Dive (45 mechanics)
**Status: MOSTLY GENUINELY NOVEL**

This is our magnum opus. Of the 45 mechanics documented:

**Genuinely novel (never publicly documented with exact values):**
- Cap stash tier probabilities (1%/7.5%/20%/71.5%) and Cap Collector scaling
- Epic creature formula (Base + ActorLevel * 0.04, max 5%)
- Legendary creatures heal to full at 50% HP (AbEpicCreature_RestoreHealth_Trigger)
- Brahmin milking uses Charisma
- Mystery Meat radiation scaling (0.5x to 1.5x)
- Mutation system internals (level 5 minimum, rad damage bucketing)
- Companion/ally visitor 20% spawn chance
- Daily Ops miniboss 2x health multiplier
- Death item pity timer (+5% per failure, guaranteed after 18 failures)
- Nemesis creatures persist 72 hours
- Arcade Bottle Blaster uses Strength
- Mischief Night costume bonus multiplier
- Whitespring XP block keyword
- Airdrop radio 50% destroyed-on-load chance
- Denizen dialogue 50/50 specific vs generic split
- Beehive/egg cluster 100% defender spawn chance
- Eyebot 50% explosion-on-death chance
- Ammo converter 100,000 point cap
- Chargen mural time-of-day animations
- Dropped Connection PvP buffer and overheat system

**Partially known (community has vague awareness):**
- Legendary creature healing at 50% -- some players have noticed the "second wind" but nobody has cited the exact trigger
- Slot machine probabilities -- known to exist but thresholds not published
- Event score player-count multipliers -- suspected but not confirmed with code
- Rad Sponge timing -- functionality known, exact intervals not
- Lunchbox stacking prevention -- players know they don't stack, exact mechanism not documented

**Known but we add detail:**
- Festive Scorched legendary rates controlled server-side -- community suspects this
- Disease system level-10 minimum -- wiki documents this implicitly
- Encryptid invulnerable/vulnerable states -- players know the mechanic, we add the state machine details

**Embarrassment risk:** VERY LOW. Even the "partially known" items benefit from exact values.

---

### Finding 015: Cross-Reference Analysis
**Status: MIXED**

Good meta-analysis. Key corrections:
- **Calling "Stolen Supplies" cut content was WRONG** -- it's an active optional objective (documented in our own analysis)
- Burning Springs/Ohio/Rust Kingdom content is thoroughly documented by Nuka Knights in their Backwoods patch analysis
- Bigfoot is released content as of the Backwoods update (March 3, 2026)

**Embarrassment risk:** MEDIUM. Some corrections needed but the analysis framework is solid.

---

### Finding 016: Nuclear Winter Full Autopsy
**Status: GENUINELY NOVEL (at this depth)**

See Finding 001. The community knows NW code exists. Nobody has published a 500-line technical breakdown of the constriction phase structs, storm wall particle parameters, AI wave configuration, ghost mode mechanics, or terminal reward weighting system.

**Embarrassment risk:** NONE if framed as a technical deep-dive, not a "discovery."

---

### Finding 017: Update Archive Analysis
**Status: PARTIALLY KNOWN / GENUINELY NOVEL MIX**

- **Bigfoot:** OLD NEWS as of March 3, 2026 (Backwoods update shipped it). Our analysis predated the release and was correct, but it's now released content.
- **Nitro Rifle appearing then disappearing:** GENUINELY NOVEL. Nobody has documented this weapon's appearance in Update 11 and removal from Update 12.
- **Cover system animations:** GENUINELY NOVEL. Nobody has documented 30+ cover combat animations appearing and being pulled.
- **NPC voice catalog and trends:** GENUINELY NOVEL. The systematic tracking of voice line additions/removals across updates is unique.

**Embarrassment risk:** LOW, but we need to acknowledge Bigfoot shipped.

---

### Finding 018: Developer Content Deep Dive
**Status: GENUINELY NOVEL**

The debug.psc god console documentation, the 14+ named developer test cells (including Emil Pagliarulo's), the DebugSteve QA tooling, the complete AutoTest bot framework, and the developer TODO/TEMP comments with internal JIRA ticket numbers -- NONE of this is publicly documented at this level.

The existence of developer test cells is vaguely known (some have been accessed via glitches historically), but the systematic catalog of 14+ named developers with their test scripts and cells is new.

**Embarrassment risk:** NONE. This is fascinating content that the community would love.

---

### Finding 019: Security Analysis
**Status: GENUINELY NOVEL**

Nobody has published a responsible-disclosure-style security analysis of FO76's Papyrus script layer. The DisableAccessRestrictions debug global, the race conditions in state machines, the keycard printer TOCTOU, and the quest debugger backdoors are all genuinely undocumented.

**Embarrassment risk:** NONE for content. CAUTION needed on framing -- this should be presented responsibly, not as an exploit guide.

---

### Finding 020: ESM Game Settings Dump
**Status: PARTIALLY KNOWN**

Many of these values (AP costs, PvP damage factors, movement speed cap) are known to the community through testing. However, having them extracted directly from the ESM and presented in a structured format with exact values is useful. The "Public Workshop XP Mult = 0.0" is a fun confirmation.

**Embarrassment risk:** LOW. Useful reference material even if individual values are roughly known.

---

### Finding 021: Nitro Weapon Coming
**Status: GENUINELY NOVEL**

The weapon keywords, season reward skins already created for future seasons, the Free States paint variant, and the appearance/disappearance pattern across updates are NOT documented anywhere. Nuka Knights has not covered this weapon.

**Embarrassment risk:** NONE. Strong finding with specific evidence.

---

### Finding 022: Cover System Pulled
**Status: GENUINELY NOVEL**

The 30+ cover combat animations appearing in Update 11 and being pulled in Update 12, combined with the ESM game settings (fPlayerCoverGunDownDelayTime, fPlayerCoverGunUpDelayTime) still being present, is completely undocumented. Nobody in the community has reported this.

The additional detail about NPCs (Deathclaws, Ghouls) already having peek/lean animations adds depth.

**Embarrassment risk:** NONE. This is a major "holy shit" finding for the community.

---

## VALIDATION SUMMARY TABLE

| Finding | Status | Novelty | Embarrassment Risk |
|---------|--------|---------|-------------------|
| 001 Nuclear Winter Code | OLD NEWS (surface) | Low | High if presented as discovery |
| 002 Casino System | PARTIALLY KNOWN | Medium | Medium |
| 003 Ghoul Player System | WRONG - Released content | None | **HIGH** |
| 004 Vault 65 | PARTIALLY KNOWN | Low | Medium |
| 005 Mothman Cult | OLD NEWS - Released content | None | **HIGH** |
| 006 Casino Full System | PARTIALLY KNOWN | Medium | Low |
| 007 NW AI Bot | GENUINELY NOVEL | **High** | None |
| 008 AI Follower Reference | GENUINELY NOVEL (analysis) | Medium | None |
| 009 QA Bot Suite | GENUINELY NOVEL | **High** | None |
| 010 Complete Bot Framework | GENUINELY NOVEL | **High** | None |
| 011 Hidden LUCK Formulas | GENUINELY NOVEL | **Very High** | None |
| 012 4-Star 50% Chance | GENUINELY NOVEL | **High** | None |
| 013 Power Plant Systems | PARTIALLY KNOWN | Medium | Low |
| 014 Hidden Mechanics Deep Dive | MOSTLY NOVEL | **Very High** | Very Low |
| 015 Cross-Reference Analysis | MIXED | Medium | Medium |
| 016 NW Full Autopsy | GENUINELY NOVEL (depth) | **High** | Low |
| 017 Update Archive Analysis | MIXED | High | Low |
| 018 Dev Content Deep Dive | GENUINELY NOVEL | **Very High** | None |
| 019 Security Analysis | GENUINELY NOVEL | **High** | None (caution on framing) |
| 020 ESM Game Settings | PARTIALLY KNOWN | Medium | Low |
| 021 Nitro Weapon | GENUINELY NOVEL | **High** | None |
| 022 Cover System Pulled | GENUINELY NOVEL | **Very High** | None |

---

## WHAT NUKA KNIGHTS FOUND THAT WE MISSED

Based on their Backwoods Patch 66 coverage, Nuka Knights documented several things we should cross-reference:

1. **Specific legendary mod rework values** (Mutant's scaling with mutation count, Bolstering 10% DR, Vanguard's 6% DR, Overeater's +40 HP per piece, Aristocrat's damage reflection, Defender's 40% auto-block, etc.) -- we have the ESM settings but didn't extract the specific new legendary effect values
2. **Event reward restructuring** with exact cap/module/note guarantees -- we didn't document the new public event reward tables
3. **Pip-Boy UI overhaul details** (Recipe Book, perk separation) -- we focused on hidden systems, not UI changes
4. **Armor weight reduction values** (T-65: 78 to 10.05, Marine: 23 to 4.1) -- specific balance changes we didn't extract
5. **Raid drop rate changes** (4-star mods from 10% to 20%, 3-star from 20% to 30%) -- important community info we didn't cover
6. **Postponed Plasma Launcher mods** -- we didn't note the delayed content

These are all "practical player information" findings rather than hidden mechanics. Nuka Knights serves a different audience need than we do.

---

## HONEST VALUE-ADD ASSESSMENT

### Where we genuinely outperform existing dataminers:

1. **Hidden formulas and exact probabilities** -- Nobody else is decompiling Papyrus scripts and extracting actual game formulas. The bomb defusal formula, cap stash tiers, legendary spawn chance, 4-star upgrade chance, pity timers, and SPECIAL stat influences are UNIQUE to our work.

2. **Developer infrastructure analysis** -- The QA bot suite, debug god console, developer test cells, and internal tooling documentation is unprecedented in the FO76 community.

3. **Unreleased/pulled feature detection** -- The nitro rifle lifecycle and cover system prototype documentation through update archive diffing is a methodology nobody else uses publicly.

4. **Security analysis** -- Nobody else has published a responsible-disclosure analysis of FO76's script-layer vulnerabilities.

### Where we should not claim novelty:

1. Nuclear Winter code existence (5-year-old news)
2. Playable Ghouls (released content, embarrassing to present as a finding)
3. Mothman cult hierarchy (released content)
4. Atlantic City casino furniture (visible in-game)
5. Bigfoot (shipped with Backwoods on March 3, 2026)

### Recommendations:

1. **REMOVE or heavily caveat** Finding 003 (Ghoul System) and Finding 005 (Mothman Cult) -- these are released content
2. **Lead with** Findings 011, 014, 012, 022, and 021 -- these are our genuinely novel work
3. **Reframe** Findings 001 and 016 as "technical deep-dives into known systems" rather than discoveries
4. **Add a disclaimer** to Finding 015 correcting the "Stolen Supplies" cut content error
5. The security analysis (019) should only be shared responsibly or submitted directly to Bethesda

### Final honest take:

About 60% of our findings contain genuinely novel information that the community does not have. The remaining 40% ranges from "known but we add exact values" to "this is embarrassingly just released content we didn't realize was released." Our strongest work -- the hidden formula extraction, the QA bot documentation, and the cover system/nitro rifle lifecycle tracking -- is legitimately world-class datamining that would establish real credibility. We just need to not lead with the stuff the community already knows.
