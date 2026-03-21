# FO76 Finding 088: TWZ09 Aerosolizer Quest — Complete Cut Toxic Water Event

## Status: CUT / GENUINELY NOVEL
## Source: dev_esm_diff_cut_content.json, dev_esm_diff_summary.md, dev_build_strings.txt

## overview

the nov 2023 dev build contains an entire cut quest called TWZ09 — part of the toxic water zone (TWZ) event series. while TWZ03, TWZ05, and TWZ07 shipped in some form (the toxic water zone events including dogwood die off), TWZ09 was fully cut and has never been documented by any dataminer, wiki, or community source.

what distinguishes this notable is the scope: TWZ09 wasn't a half-baked prototype. it had its own crafting system, a custom combat perk, a unique magic effect, mirelurk escort AI, challenge tracking, reward tables, and quest dialogue branches. this was a nearly complete event that got axed.

## all confirmed records

| type | editor id | form id | purpose |
|------|-----------|---------|---------|
| QUST | TWZ09 | 0x00088A9A | the quest itself |
| PERK | TWZ09AerosilzerKick | 0x002FD347 | custom perk — lets you kick the aerosolizer device |
| MGEF | TWZ09KickEffect | — | magic effect triggered by the kick |
| SPEL | TWZ09KickPerk | — | spell wrapper for the kick perk |
| COBJ | TWZ09AerosolizerRecipe | — | crafting recipe for the aerosolizer |
| KYWD | TWZ09AerosolizerKeyword | — | keyword for identifying the craftable item |
| LVLI | TWZ09_Chlorine | — | leveled list for chlorine crafting ingredient |
| LVLI | TWZ09_Fertilizer | — | leveled list for fertilizer crafting ingredient |
| MESG | TWZ09_NoFertilizerMsg | — | error message when player lacks fertilizer |
| MISC | Event_TWZ09 | — | event registration record |
| DIAL | TWZ09Branch | — | dialogue branch |
| DIAL | TWZ09_EBSTopic | — | EBS (emergency broadcast system) topic |
| MISC | ToxicEventDebugNode_TWZ09 | — | debug/testing node |
| FLST | QuestReward_TWZ09_Stage1000_01 | — | quest reward at completion stage |
| CHAL | Challenge_Lifetime_QuestsCompleted_Event_Sub_TWZ09 | 0x0043B551 | lifetime challenge tracking |
| CHAL | Challenge_Quests_SpecificEvent_TWZ09 | — | event-specific challenge |

### related mirelurk AI packages (cross-referenced from TWZ05)

| type | editor id | purpose |
|------|-----------|---------|
| PACK | TWZ05_MirelurkHordeAccompany01 | escort AI — mirelurk follows a path/player |
| PACK | TWZ05_MirelurkHordeAccompany02 | second escort variant |
| PACK | TWZ05_MirelurkHordeAccompany03 | third escort variant |
| PACK | TWZ05_MirelurkWait | mirelurk hold position AI |

## what the quest was about

piecing together the record names:

1. **the aerosolizer** was a craftable device. the player needed to gather chlorine and fertilizer (both have dedicated leveled item lists) and use TWZ09AerosolizerRecipe to build it. if you didn't have fertilizer, you'd see TWZ09_NoFertilizerMsg.

2. **the kick mechanic** was unique to this quest. TWZ09AerosilzerKick was a custom perk that granted a kick ability via TWZ09KickPerk/TWZ09KickEffect. you'd kick the aerosolizer to activate it — this would have been a scripted interaction, not a standard weapon attack.

3. **mirelurk horde escort** — the three "MirelurkHordeAccompany" AI packages (numbered 01/02/03, suggesting three mirelurks in the group) plus MirelurkWait indicate the quest involved escorting a group of mirelurks. the mirelurks would follow you and hold position on command.

4. **emergency broadcast** — TWZ09_EBSTopic is a dialogue branch for the emergency broadcast system, meaning the event was announced over the radio like other public events.

the most likely scenario: players would craft an aerosolizer using chlorine and fertilizer, escort a horde of mirelurks to a toxic water zone, then kick-activate the aerosolizer to disperse chemicals and cleanse the water. the mirelurks were probably being guided back to cleaned habitats.

## context within the TWZ series

the TWZ prefix covers the toxic water zone event chain:
- **TWZ03** — exists in dev build strings, has quest stages
- **TWZ05** — the mirelurk-related event (Dogwood Die Off uses mirelurk mechanics)
- **TWZ07** — exists in dev build strings, has quest stages
- **TWZ09** — this cut quest

all four appear in the dev build strings as `Quests::TWZxx::Scenes`, `Scripts`, and `Warning`, confirming they all had working quest logic with scenes and papyrus scripts. TWZ09 was the most mechanically ambitious — it combined crafting, a custom perk/ability, and escort AI into a single event.

## why this is novel

no wiki, datamine article, or community post documents TWZ09 as a discrete quest. the Fallout 76 cut content pages list various removed quests but TWZ09 is absent. the aerosolizer mechanic exists in the live game's Dogwood Die Off event, but the connection to a standalone TWZ09 quest with its own crafting recipe, custom combat perk, and mirelurk escort system has never been documented.

the most likely explanation for the cut: TWZ09's mechanics were partially cannibalized for the Dogwood Die Off event. the aerosolizer device and the toxic water cleanup concept survived, but the crafting system, kick perk, and mirelurk escort were stripped out to simplify the event.

## development maturity

this was a late-stage cut. the evidence:
- it has a lifetime challenge tracker (Challenge_Lifetime_QuestsCompleted_Event_Sub_TWZ09) — bethesda doesn't create challenge integration for early prototypes
- it has an event-specific challenge (Challenge_Quests_SpecificEvent_TWZ09)
- it has a reward table (QuestReward_TWZ09_Stage1000_01)
- it has emergency broadcast dialogue (TWZ09_EBSTopic)
- it has a debug testing node (ToxicEventDebugNode_TWZ09) — meaning QA was testing it

all of these point to a quest that was feature-complete or nearly so before being cut.
