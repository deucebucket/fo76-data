# Finding 097: Rendered Model Gallery - Aliens, Robots, and Creatures

## Summary

22 models rendered from the FO76 mesh BA2 archives using fo76utils nif_info. Focus on alien-related content, cut/interesting robots, and notable creatures not previously rendered.

## Rendered Models

### Alien Faction Models

| File | Mesh Path | Description |
|------|-----------|-------------|
| `flatwoods_monster.png` | `actors/flatwoodsmonster/characterassets/flatwoodsmonster.nif` | The Flatwoods Monster - psychic alien entity with metallic body, glowing purple energy arms, and domed head |
| `alien_body.png` | `actors/alien/characterassets/alien_body.nif` | Classic Zetan alien body - small grey humanoid with oversized cranium |
| `alien_animatronic.png` | `actors/dlc04/animatronic/characterassets/animatronicalienreplace.nif` | DLC04 alien animatronic replacement mesh - mechanical alien replica |
| `zetan_invader.png` | `actors/zetaninvader/zetaninvader.nif` | Zetan Invader - armored alien soldier from "Invaders from Beyond" event |
| `zetan_invader_v2.png` | `actors/zetaninvader_2/zetaninvader.nif` | Zetan Invader variant 2 - updated model with different textures |
| `zetan_drone.png` | `actors/zetandrone/characterassets/zetandrone.nif` | Zetan Drone - alien combat drone with pointed fins and energy weapon |
| `zetan_drone_variant.png` | `actors/zetandrone/characterassets/zetandrone_variant.nif` | Zetan Drone suicide variant - modified drone with explosive capability |
| `zetan_brainwave_extractor.png` | `props/brainwaveextractor/zetan_brainwaveextractor_new.nif` | Zetan brainwave extraction device - glowing energy sphere in metallic frame |

### Robot Models

| File | Mesh Path | Description |
|------|-----------|-------------|
| `mr_gutsy.png` | `loadscreenart/creaturemrgutsy.nif` | Mr. Gutsy - military robot, the platform used by the EN05 Drill Sergeant at Camp McClintock |
| `drillsergeant_hat.png` | `actors/robot/parts/drillsergeanthat.nif` | Drill Sergeant hat attachment for Mr. Gutsy robots - military cap with insignia badge |
| `eyebot.png` | `actors/eyebot/characterassets/eyebot.nif` | Standard Eyebot - floating surveillance/broadcast robot |
| `eyebot_bos.png` | `actors/eyebot/characterassets/eyebot_bos.nif` | Brotherhood of Steel Eyebot variant with BoS markings |
| `eyebot_pod.png` | `furniture/eyebotpod/eyebotpod.nif` | Eyebot deployment pod - docking/charging station |
| `robobrain.png` | `dlc01/loadscreenart/dlc01creaturerobobrain.nif` | Robobrain - brain-in-a-tank robot |
| `assaultron.png` | `loadscreenart/creatureassaultron.nif` | Assaultron - fast melee combat robot |
| `rust_devil.png` | `dlc01/loadscreenart/dlc01creaturerustdevil.nif` | Rust Devil - raider-modified junk robot |

### Creature Models

| File | Mesh Path | Description |
|------|-----------|-------------|
| `grafton_monster.png` | `loadscreenart/creaturegrafton.nif` | Grafton Monster - headless giant mutant, unique to Appalachia |
| `honeybeast.png` | `loadscreenart/ creaturehoneybeast.nif` | Honeybeast - mutated bear covered in beehive growths |
| `deep_one.png` | `dlc03/loadscreenart/creaturedeepone.nif` | Deep One - Lovecraftian aquatic humanoid creature |
| `gulper.png` | `dlc03/loadscreenart/creaturegulper.nif` | Gulper - mutated salamander/newt creature |
| `angler.png` | `dlc03/loadscreenart/creatureangler.nif` | Angler - bioluminescent ambush predator fish-creature |

### Misc

| File | Mesh Path | Description |
|------|-----------|-------------|
| `survey_marker.png` | `setdressing/surveymarkers/surveymarker_spruceknob.nif` | Spruce Knob survey marker - USGS-style geodetic marker |

## Notes on Requested Items

### Payroll Terminal
No mesh found under "payroll" in the Meshes BA2. The Payroll Terminal (`announcerf_mtrg01_payrollterminal`) is a voiced announcer NPC that uses a standard terminal mesh model. Its 9 voice lines are all orphaned (not connected to any active quest). The terminal model would be a generic `furniture/terminals/terminalon.nif`.

### Drill Sergeant Eyebot
The "Drill Sergeant" at Camp McClintock (EN05) is NOT an Eyebot -- it is a Mr. Gutsy robot (`EN05_DialogueGutsyDrillSergeant`, quest 0x00039DD4). It has a unique hat attachment (`drillsergeanthat.nif`) that sits on top of the Gutsy's dome. Both the hat and the Gutsy loadscreen model are rendered.

### Survey Bot
No "Survey Bot" or "Survey Protectron" exists in the meshes or ESM. The only survey-related meshes are USGS-style survey markers at 5 locations (Alvon, Canaan, Cheat, Lansing, Spruce Knob).

### Ryan Ainsley (Whitespring Ghost)
Ryan Ainsley exists as a CUT voice type (`CUT_NPCM_LC060_RyanAinsley`, VTYP 0x003CDB12) -- one of 7 cut Whitespring NPCs alongside Dorothy Orris, Paula Hamilton, Phillip Ross, Marcus Wellsby, Ted Hollingsworth, Robert Mitchell, and Sophia Hollingsworth. These are human NPCs with no unique meshes -- they would use standard human character models. No ghost-specific mesh exists for Ainsley.

## Cut Whitespring NPCs (LC060)

The full list of cut Whitespring characters discovered:

| Voice Type | FormID | Name |
|------------|--------|------|
| CUT_NPCM_LC060_RyanAinsley | 0x003CDB12 | Ryan Ainsley |
| CUT_NPCF_LC060_DorothyOrris | 0x003CDB11 | Dorothy Orris |
| CUT_NPCF_LC060_PaulaHamilton | 0x003CDB0A | Paula Hamilton |
| CUT_NPCM_LC060_PhillipRoss | 0x003CDB04 | Phillip Ross |
| CUT_NPCM_LC060_MarcusWellsby | 0x003CDB05 | Marcus Wellsby |
| CUT_NPCM_LC060_TedHollingsworth | 0x003CDB06 | Ted Hollingsworth |
| CUT_NPCM_LC060_RobertMitchell | 0x003CDB0B | Robert Mitchell |
| CUT_NPCF_LC060_SophiaHollingsworth | 0x003CDB0F | Sophia Hollingsworth |

Additionally, cut Whitespring vendor factions exist:
- `CUT_LC060_WhitespringVendor_BoS_Faction`
- `CUT_LC060_WhitespringVendor_Raiders_Faction`
- `CUT_LC060_WhitespringVendor_Responders_Faction`
- `CUT_LC060_WhitespringVendor_FreeStates_Faction`
- `CUT_LC060_WhitespringVendor_Neutral_Faction`

These cut vendors have NPC records with actual form data, suggesting they were nearly implemented before being removed.
