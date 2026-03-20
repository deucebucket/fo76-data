# FO76 Finding 003: Ghoul Player Character System — Full Mechanics

## Status: ACTIVE FEATURE — Detailed mechanics visible in game files
## Source: translate_en_utf8.txt, seventysix_strings_en.txt

## Core Mechanics Found
- **Ghoulification Quest**: `[Ghoulification Quest Misc Breadcrumb Radio]` [392949B3]
- **Transformation**: `$GHOULIFY_SUCCESS` — "Your character has been transformed"
- **Reversion**: `$GhoulToHumanTutorial01` — "Revert your character back into a human for free!"
- **Re-ghoulification**: Can return to ghoul form after reverting
- **Feral state references**: `Weak Feral Ghoul Player Icon` / `Feral Ghoul Player Icon` — suggests feral transformation mechanic
- **Ghoul-specific perk**: `Player Ghoul Perk` [4100F0FB]
- **Ghoul Glutton**: `Ghoul Glutton Perk description` [410105F1]

## Maintenance/Disable System
- `$GHOULS_DISABLED` — "The ghoul player experience is currently unavailable"
- `$GHOULS_DISABLED_MUST_TRANSFORM` — Forces ghoul players to transform back to human during maintenance
- `$ConnectionMessageRejectGhoulCharacterFeatureDisabled` — Ghoul characters blocked from joining worlds
- This is a server-side toggle — Bethesda can disable ghouls independently

## Settlement Integration
- `Player Ghoul Settlement Faction` [39295CA7] — Ghouls have their own settlement faction
- `[Dialogue quest for ghoulified Leamon]` [39295CA7] — NPC-specific ghoul dialogue

## Marketing Integration
- Level 50 Character Boost advertised with ghoul access: "Jump right into level-restricted content, like playable ghouls"
- Ghoul transformation has had Atom costs at various points

## Player Icons
Extensive ghoul player icon variants: Male, Female, Action Boy/Girl, Armed, Screaming, Mutated, Crooner, Halloween variants — suggests this is a major feature with ongoing cosmetic support

## Cross-Reference Needed
- Compare with patch notes to determine current cost status (free vs Atoms)
- Check if Feral Ghoul transformation is an active mechanic or cut concept
- Verify settlement faction implications for gameplay
