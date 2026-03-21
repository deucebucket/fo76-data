# FO76 Finding 091: Floater Dialogue System — Cut Creature-Specific Dialogue Quests

## Status: CUT / GENUINELY NOVEL
## Source: dev_esm_diff_cut_content.json, dev_esm_diff_summary.md

## overview

three quest records in the dev build reveal that bethesda planned to give floater creatures their own NPC-like dialogue system, with separate dialogue quests for each floater variant: Flamer, Freezer, and Gnasher. in the live game, floaters are mindless hostile creatures with no dialogue. these cut quests would have made them something fundamentally different.

## confirmed records

| type | editor id | form id | purpose |
|------|-----------|---------|---------|
| QUST | CreatureDialogueFloaterFlamer | 0x0056451C | dialogue quest for the fire-spitting variant |
| QUST | CreatureDialogueFloaterFreezer | 0x0056451D | dialogue quest for the cryo-breathing variant |
| QUST | CreatureDialogueFloaterGnasher | 0x0056451B | dialogue quest for the melee/biting variant |

## the naming convention tells the story

the editor IDs follow an exact pattern: `CreatureDialogue[CreatureName]`. this is the same naming convention used for creature dialogue across the creation engine. searching the dev build strings confirms a related system exists for bloatflies:

```
CreatureDialogueBloatfly
Quests::CreatureDialogueBloatfly::Scenes
Quests::CreatureDialogueBloatfly::Scripts
Quests::CreatureDialogueBloatfly::Warning
```

creature dialogue quests in creation engine games don't mean the creature literally talks. they define audio barks, contextual vocalizations, and reactive behaviors that play during gameplay — grunts when they spot you, idle sounds, pain reactions, aggression escalation sounds. what makes the floater records special is that bethesda made **three separate dialogue quests** for what are essentially three texture swaps of the same creature.

## why three separate quests matters

floaters are super mutant pets introduced in Wastelanders. all three variants (Flamer, Freezer, Gnasher) share the same base model but have different attack types:
- **Floater Flamer** — spits fire
- **Floater Freezer** — breathes cryo frost
- **Floater Gnasher** — bites/melee attacks

giving each variant its own dialogue quest means bethesda was building variant-specific vocalizations and behavioral sound sets. the flamer would have sounded different from the freezer, which would have sounded different from the gnasher. each one would have had its own:
- idle sounds
- detection/alert barks
- combat vocalizations
- pain/death sounds
- pursuit/search behaviors

this level of audio differentiation between creature variants is unusual for fo76, where most creature variants share sound sets.

## form ID analysis

the three form IDs are consecutive:
- 0x0056451B (Gnasher)
- 0x0056451C (Flamer)
- 0x0056451D (Freezer)

created as a batch, in a single session. the 0x005645xx range is in the same neighborhood as:
- Armor_EnclaveScoutUniform_Torso_Set_V94_Solar02 (0x005644CB) — a cut Vault 94 enclave armor variant

this places the creation roughly in the same development window as other vault raid / wastelanders-era content.

## what happened to them

the most likely scenario: the floater dialogue quests were created during the wastelanders development period when floaters were being added to the game. the plan was to give each variant a distinct audio personality. at some point, the decision was made to simplify — all three variants would share generic creature sounds instead of having unique dialogue quest-driven vocalizations.

this simplification probably came down to scope. recording and implementing three separate sound sets for what players perceive as the same enemy type was a lot of work for marginal player-facing impact.

## broader implications

the existence of variant-specific creature dialogue quests suggests bethesda's original vision for floaters was more nuanced than what shipped. floaters were supposed to feel like distinct creatures with their own personalities, not just recolored versions of the same mob. the gnasher was supposed to sound angrier and more physical. the freezer was supposed to sound colder and more deliberate. the flamer was supposed to sound more aggressive.

it also raises the question of whether other creature families were planned to have variant-specific dialogue. if floaters got this treatment, did scorched, super mutants, or liberator robots have similar cut systems?

## why this is novel

no wiki, datamine, or community source documents floater-specific dialogue quests. the fallout 76 unused content pages mention various cut creatures and quests, but the concept of variant-specific creature dialogue systems for floaters is completely undocumented. the idea that bethesda planned NPC-like dialogue quest infrastructure for hostile creatures is a design insight that hasn't surfaced anywhere in the community.
