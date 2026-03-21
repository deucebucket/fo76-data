# FO76 Finding 001: Nuclear Winter (Battle Royale) Code Still Fully Present

## Status: CONFIRMED — 3,257+ string entries, full UI, match-finding, perk system
## Source: nw_en.strings, nw_en.dlstrings, translate_en_utf8.txt

## Contents
- **Internal codename: "Babylon"** — all code references use this name
- **3,257 string entries** in NW-specific string table (item names, locations, perks)
- **332 dialogue/description strings** in NW dlstrings
- **Complete match-finding system**: `$GameStatePrompt_FindingBabylonPrompt` "Finding a Nuclear Winter match"
- **Perk card system**: ZAX-dispensed perk cards, Overseer Ranks, NW-specific challenges
- **Vault 51 storyline**: Full overseer competition narrative
- **Main menu entry**: `$MainMenuBabylon` "NUCLEAR WINTER"
- **All UI**: Exit prompts, connecting screens, abandonment warnings

## Summary
Nuclear Winter was removed as a playable mode but NONE of the code was cleaned out. The entire battle royale system — matchmaking, ring mechanics, perk cards, UI — is dormant in the client. Most live service games strip removed features to reduce client size; the FO76 client retains all of it.

## Notes
- may indicate plans to eventually bring it back (possibly redesigned)
- Or simply that Bethesda doesn't clean deprecated code
- The NW.esm (28MB) still ships with the game as a separate plugin file
- Modders could theoretically re-enable portions of this on private servers
