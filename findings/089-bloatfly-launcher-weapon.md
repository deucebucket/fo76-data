# FO76 Finding 089: Bloatfly Launcher — Standalone Cut Weapon

## Status: CUT / GENUINELY NOVEL
## Source: dev_esm_diff_cut_content.json, dev_esm_diff_summary.md

## overview

the dev build ESM contains a cut weapon called `E09A_Launcher_ThrowBloatflyWeapon` (0x0063D326) — a standalone launcher that fires bloatflies as projectiles. this is NOT the bloatfly larva syringe barrel mod that exists in the live game. this is a separate, purpose-built weapon that was part of the NukaWorld on Tour (E09) event content.

## confirmed records

| type | editor id | form id | purpose |
|------|-----------|---------|---------|
| WEAP | E09A_Launcher_ThrowBloatflyWeapon | 0x0063D326 | the bloatfly throwing weapon |
| WEAP | E09A_Launcher_Weapon | 0x00636969 | base launcher weapon (parent?) |
| WEAP | E09A_Launcher_Egg | — | egg variant of the launcher |

## what makes this distinct from the syringe barrel

the live game has a bloatfly larva syringe barrel mod for the syringer weapon. when you hit an enemy with it, a bloatfly spawns from their corpse on death. that's a weapon mod on an existing weapon.

E09A_Launcher_ThrowBloatflyWeapon is fundamentally different:
- it's a **standalone WEAP record**, not a mod attachment
- the name says "Throw" — suggesting you physically launch bloatflies at targets
- it's prefixed with E09A, tying it directly to NukaWorld on Tour's "A" stage
- it sits alongside E09A_Launcher_Egg, suggesting a family of thrown creature projectiles

## connection to NukaWorld on Tour

the E09A prefix tells us exactly where this weapon was going to live. NukaWorld on Tour (the traveling carnival event) has multiple stages:
- **E09A** — the first stage, which in the live game involves clearing creatures from ride areas
- **E09B** — the spin-the-wheel wave defense stage

67 E09 records were cut from the dev build while 1,141 E09 records made it to retail. the bloatfly launcher was among the casualties. other cut E09 weapons include E09A_Launcher_Egg (an egg-throwing variant) and E09A_Launcher_Weapon (the base launcher).

the picture that emerges: NukaWorld on Tour originally had a more elaborate weapon system where players could use carnival-themed launchers to throw creatures (bloatflies) and eggs at enemies. this was probably cut because it was too mechanically complex for a public event, or because throwing live creatures raised weird gameplay questions (are the bloatflies hostile to everyone? do they count as your kills?).

## form ID analysis

the form ID 0x0063D326 places this in the same creation batch as other late-development content. for reference:
- BossChicken records: 0x00636Dxx
- E09A_Launcher_Weapon: 0x00636969
- ArcadeManagerQuest: 0x0063F8D6

all of these cluster in the 0x0063xxxx range, indicating they were created in the same development period (likely mid-to-late 2023 based on the dev build date).

## why this is novel

no wiki, datamine, or community source documents a standalone bloatfly launcher weapon. the Fallout Wiki's unused content page doesn't list it. searches for "E09A_Launcher_ThrowBloatflyWeapon" return zero results. the bloatfly larva syringe barrel is well-documented, but this is a completely separate weapon concept that existed and died within the NukaWorld on Tour development cycle.

## creature damage curves

the dev build also contains cut creature weapon curves that would have applied to NPC bloatflies:
- `CT_Creatures_Weapon_BloatflyRanged` — ranged attack damage curve
- `CT_Creatures_Weapon_BloatflyUnarmed` — melee attack damage curve

these are the bloatfly's own attack curves (not related to the launcher), but their presence as cut content shows that bloatfly combat tuning was being actively worked on during the same development period.
