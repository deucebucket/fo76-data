# Reddit-Ready Fact-Check Checklist

**Date:** 2026-03-20
**Checker:** Claude Opus 4.6 (final pass)
**Method:** 2-3 web searches per claim + ESM dump cross-reference

---

## Claim 1: Sneak attacks do zero bonus damage without Covert Operative (base multiplier is 1.0x)

**ESM Verification:** CONFIRMED -- `fDamageSneakAttackMult = 1.000000` in game_settings.txt (line 4626-4627)

**Web Search Results:**
- Fallout Wiki (fandom + fallout.wiki) both state sneak attacks provide 2x ranged / 5x melee damage as baseline
- Multiple Steam discussions confirm "sneak attacks show damage bonus even with no perks"
- The Fallout 76 game settings wiki page (fallout.fandom.com/wiki/Fallout_76_game_settings) EXISTS and lists GMST values -- this specific setting MAY already be documented there

**Verdict: RISKY**
The ESM value of 1.0 is real, but the community ALREADY knows sneak attacks deal 2x damage without perks. The 1.0 multiplier is the GMST value, but additional sneak attack bonus appears to be applied through perk entries or spell effects rather than this single setting. If the 2x base damage comes from elsewhere (e.g., a perk or spell applied to all players), then claiming "zero bonus damage" based solely on fDamageSneakAttackMult=1.0 could be WRONG and embarrassing. The wiki game settings page may already list this value. Needs deeper analysis before posting.

---

## Claim 2: 4-star legendary is a 50% coin flip from 3-star (Rank4Chance = 0.5)

**ESM Verification:** CONTRADICTED -- `SQ_Epic_Creature_Star4_Rank4_Global = 0.000000` (FLTV 0.0, line 81904-81905)

Full legendary rank globals from ESM:
- Star1_Rank1: 1.0 (always)
- Star2_Rank1: 1.0, Star2_Rank2: 0.25
- Star3_Rank1: 1.0, Star3_Rank2: 0.2778, Star3_Rank3: 0.1111
- Star4_Rank1: 1.0, Star4_Rank2: 0.2708, Star4_Rank3: 0.1458, **Star4_Rank4: 0.0**

4-star legendary drops from world enemies are DISABLED (0.0 chance). They come exclusively from Gleaming Depths raid rewards via separate LGDI legendary item distribution records.

**Verdict: DO NOT POST**
The claim is factually wrong. The value is 0.0, not 0.5. Posting this would be immediately debunked by anyone who checks the ESM.

---

## Claim 3: Brahmin milking uses Charisma as the governing stat

**ESM Verification:** INCONCLUSIVE -- Found `BrahminMilkingPerk` (0x003F2B93) and curve tables `CT_BrahminMilkChance_Large` / `CT_BrahminMilkChance_Small`, but the ESM dump does not show a direct Charisma reference in the perk conditions. The perk checks race, death state, and keyword conditions, not a SPECIAL stat.

**Web Search Results:**
- No source anywhere mentions Charisma affecting brahmin milking
- Community guides describe milking as a simple interact-with-cooldown mechanic
- Some mention RNG (brahmin sometimes kicks, no milk) but no stat dependency

**Verdict: RISKY**
Cannot confirm Charisma connection from ESM dump or any public source. If the curve tables internally reference Charisma, it's not visible in our text dump. Posting an unverifiable claim about a stat connection that might not exist = high embarrassment risk.

---

## Claim 4: Death item drops have a pity timer (+5% per failure, starts at 10%)

**ESM Verification:** NOT FOUND -- Only death drop settings found are `uDeathDropSurvivalAidChance = 25` and `iDeathDropWeaponChance = 100`. No pity timer, escalating chance, or bad-luck-protection mechanic visible in game settings or globals.

**Web Search Results:**
- Zero results for "pity timer" in FO76 context
- No community discussion of escalating drop chances
- Pity timers are a gacha game concept, not present in Creation Engine games

**Verdict: DO NOT POST**
No evidence this mechanic exists. Cannot find it in ESM, cannot find it discussed anywhere online. Likely fabricated or misinterpreted data. Would be immediately challenged.

---

## Claim 5: Cap stash probabilities (1% jackpot 100-125, 7.5% high 50-60, 20% medium 30-40, 71.5% standard 10-20)

**ESM Verification:** INCONCLUSIVE -- No cap stash loot table with these exact probabilities found in the ESM text dump. Cap stashes likely use leveled list or container records that don't break down this cleanly in our dump format.

**Web Search Results:**
- Fallout Wiki describes cap stashes as "random, usually high amount" -- no specific tier breakdown
- Community guides mention 70-80 caps average with Cap Collector perk
- No source provides the exact probability distribution claimed

**Verdict: RISKY**
The specific numbers (1%, 7.5%, 20%, 71.5%) are not verifiable from our data or any public source. If these came from an actual leveled list analysis, they might be correct but cannot be independently verified. If wrong, the specificity makes it extra embarrassing.

---

## Claim 6: Cover combat system built (30+ animations) and pulled between Update 11 and 12

**ESM Verification:** CONFIRMED (animations exist) -- Found 40+ IDLE records for cover system:
- `GunEnterCoverLeftStanding`, `GunEnterCoverRightCrouching`, etc. (0x004Fxxxx FormIDs -- FO76 era)
- `enterCoverRightSneaking`, `enterCoverLeftSneaking` (0x0009xxxx -- inherited from engine)
- `enterMeleeCoverRight/Left` variants (0x0007xxxx)
- `GunBehaviorSimulateGraphEventToCoverIdle/Left/Right`
- NPC dialogue: "Asking for cover during combat" (quest records)

However: Many low-FormID animations (0x0003xxxx, 0x0007xxxx, 0x0009xxxx) are inherited from Fallout 4's Creation Engine, NOT purpose-built for FO76. The 0x004Fxxxx entries are FO76-specific additions that expand on the inherited system.

**Web Search Results:**
- No public documentation of these cover animations
- TCRF (Cutting Room Floor) Fallout 76 page does not mention a cover system
- No Reddit/wiki/YouTube results for "fallout 76 cover system datamined"
- "GunEnterCover" returns zero results online

**Verdict: RISKY**
The animations exist, but the claim "built and pulled between Update 11 and 12" is unverifiable -- many are inherited engine animations, not a purpose-built FO76 cover system. Saying "30+ cover animations" is technically true but misleading if most are Fallout 4 engine leftovers. The FO76-specific additions (0x004F range) are genuinely novel finds. Needs careful framing: "Cover system animations exist in the ESM, some inherited from FO4, some added specifically for FO76" rather than "a complete cover system was built and pulled."

---

## Claim 7: Tempest Armor -- complete undocumented 5-piece set with elemental linings

**ESM Verification:** CONFIRMED -- Extensive Tempest armor records found, ALL with `zzz_` prefix (disabled):
- 6 armor pieces: `zzz_Armor_Tempest_ArmLeft/ArmRight/LegLeft/LegRight/Torso` + `zzz_Headwear_Clothes_Tempest`
- 30+ modification records including linings: `Thunderous`, `Amplified`, `Recharged`, `FlameResistance`, `Explosion1/2`, `RadiationResistance`, `BioComm`, `StealthMove`, `Stabilized`
- Material tiers 0-4 for arms, legs, torso
- Jetpack mod: `zzz_mod_Player_Tempest_JetPack`
- Crafting recipes for all pieces and mods
- Paint: `zzz_SCORE_S17_mod_armor_Tempest_Material_Paint_ForestService` (was planned for Season 17 Scoreboard)

ALSO: Active (non-zzz) Tempest WEAPON exists: `P62_Weapon_Tempest_AddBleedPerk`, `P62_Mod_Custom_Tempest_*` -- this is a Drifter weapon variant from Patch 62, currently in-game.

**Web Search Results:**
- Zero results for "Tempest armor" as cut content in FO76
- No wiki, Reddit, or datamine site mentions the disabled armor set
- The Tempest weapon (Drifter variant) IS known, but the armor set is NOT

**Verdict: SAFE TO POST**
The disabled Tempest armor set with 6 pieces, 30+ mods, elemental linings, a jetpack, and a planned Scoreboard paint is genuinely novel. No public documentation found anywhere. However, be precise: call it "disabled" (zzz_ prefix) not "undocumented" -- and note that a Tempest weapon already exists in-game as a Drifter variant, so people will know the name but not the armor.

---

## Claim 8: Slot machines buff Luck on wins (ATX_BuffLuck spell)

**ESM Verification:** CONFIRMED -- `SPEL: 0x0060497D ATX_BuffLuck` exists in the ESM.

**Web Search Results:**
- ALREADY KNOWN: West Virginia Slot Machine grants +2 Luck for 30 minutes (documented on Fallout Wiki, multiple guides)
- The Duchess Flame, Fallout Wiki, Bethesda Support, and community discussions all describe this mechanic
- The specific spell name "ATX_BuffLuck" is not publicly documented, but the EFFECT is well-known

**Verdict: DO NOT POST**
The +2 Luck buff from slot machines is widely known and documented. The internal spell name "ATX_BuffLuck" adds nothing meaningful. Posting this as a "discovery" would embarrass us.

---

## Claim 9: Legendary creatures always heal to full at exactly 50% HP

**ESM Verification:** CONFIRMED (threshold) -- Found the trigger spell:
- `SPEL: 0x00450ADF AbEpicCreature_RestoreHealth_Trigger`
- Condition: `GetValuePercent:0x0(0x2D4,0x0,0,0x0,-1)<0.500000`
- This means: fires when Health (ActorValue 0x2D4) drops below 50%
- Paired with `AbEpicCreature_RestoreHealth_Effect` (full heal)

**Web Search Results:**
- Community GENERALLY knows legendary enemies "mutate and heal" at roughly half health
- Steam discussions confirm "legendary enemies heal once to full when they mutate"
- Fallout 4 threads state mutation happens "below 50% but above 25%"
- The EXACT 50% threshold is not widely cited with ESM evidence, but the behavior is well-understood

**Verdict: RISKY**
The behavior (legendary heals at ~half health) is common knowledge. The ESM confirmation of exactly 50% adds precision but isn't groundbreaking. Framing matters: "We confirmed the exact threshold is 50% via ESM data" is fine. "Hidden mechanic: legendaries heal at 50%!" would look silly because everyone already knows this.

---

## Claim 10: Cut VR tutorial "Enjoy" quest -- Tranquility Lane-style new player experience

**ESM Verification:** CONFIRMED -- Extensive ZZZNPE records found:
- Quest references: `ZZZNPE_MQ01_Enjoy_Recipe_Workshop_DisrupterDevice`
- Actor values: `ZZZNPE_MQ01_Enjoy_InBuildingTutorial_AV`, `ZZZNPE_MQ01_Enjoy_InCombatTutorial_AV`
- VR citizen system: `ZZZNPE_VRCitizens_VoiceTypes`, `ZZZNPE_VRBullies_VoiceTypes`
- Factions: `ZZZNPE_VRCitizenFaction`, `ZZZNPE_VRBullyFaction`
- Outfits: `ZZZNPE_LL_Outfit_VRCitizen01`, `ZZZNPE_LL_Outfit_VRBully01`, `ZZZNPE_LLI_Outfit_VaultVRCitizen`
- NPC tracking: `ZZZNPE_DaytonAwayValue`, `ZZZNPE_MetDaytonOffQuest`

This is a substantial cut quest system with VR citizens, bullies, building/combat tutorials, and an NPC named "Dayton."

**Web Search Results:**
- Zero results for "ZZZNPE" anywhere online
- Zero results for "MQ01_Enjoy" quest
- No Fallout Wiki, Reddit, TCRF, or datamine source mentions this content
- FO76 cut content pages do not list it

**Verdict: SAFE TO POST**
This is genuinely novel and undocumented. A complete VR tutorial quest system ("Enjoy") with citizens, bullies, combat/building tutorials, factions, and NPC "Dayton" -- all prefixed with ZZZNPE (disabled). The Tranquility Lane comparison is apt (VR simulation in a vault). No trace of this anywhere online.

---

## SUMMARY SCORECARD

| # | Claim | Verdict | Risk Level |
|---|-------|---------|------------|
| 1 | Sneak attack 1.0x base multiplier | RISKY | HIGH -- may be misinterpreting GMST vs actual behavior |
| 2 | 4-star legendary 50% chance | DO NOT POST | CRITICAL -- ESM says 0.0, not 0.5 |
| 3 | Brahmin milking uses Charisma | RISKY | HIGH -- unverifiable from our data |
| 4 | Death item pity timer | DO NOT POST | CRITICAL -- no evidence exists |
| 5 | Cap stash probability tiers | RISKY | MEDIUM -- unverifiable specifics |
| 6 | Cover combat system (30+ anims) | RISKY | MEDIUM -- many are inherited FO4 engine anims |
| 7 | Tempest Armor (disabled set) | SAFE TO POST | LOW -- genuinely novel, well-evidenced |
| 8 | Slot machine Luck buff | DO NOT POST | HIGH -- already widely known |
| 9 | Legendary heal at 50% HP | RISKY | MEDIUM -- behavior known, exact threshold adds little |
| 10 | Cut VR tutorial "Enjoy" quest | SAFE TO POST | LOW -- genuinely novel, zero online presence |

## RECOMMENDED POST LIST (2 of 10 survive)

1. **Tempest Armor** (Claim 7) -- Disabled 5-piece armor set + headwear with 30+ mods, jetpack, elemental linings, and a planned Season 17 Scoreboard paint. Well-evidenced, zero online presence.

2. **ZZZNPE "Enjoy" VR Tutorial** (Claim 10) -- Complete cut quest system with VR citizens, bullies, combat/building tutorials, factions, and NPC "Dayton." Tranquility Lane comparison is justified. Zero online presence.

## CLAIMS THAT NEED REWORK BEFORE POSTING

3. **Cover system animations** (Claim 6) -- Real find but needs honest framing. Many are engine-inherited. Focus on the FO76-specific 0x004Fxxxx additions.

4. **Legendary 50% health threshold** (Claim 9) -- ESM-confirmed precision on known behavior. Frame as "data confirmation" not "discovery."

5. **Cap stash probabilities** (Claim 5) -- Need to actually extract the leveled list data to back up the numbers.

## CLAIMS TO KILL

- Claim 2 (4-star chance) -- Factually wrong
- Claim 4 (pity timer) -- No evidence
- Claim 8 (slot machine buff) -- Already known
- Claim 1 (sneak multiplier) -- Likely misinterpreted
- Claim 3 (brahmin charisma) -- Unverifiable
