# FO76 Finding 090: BossChicken — Complete Cut Boss Creature

## Status: CUT / GENUINELY NOVEL
## Source: dev_esm_diff_cut_content.json, curve_tables/creatures/health/health_bosschicken.json

## overview

a fully defined boss creature called "BossChicken" exists in the nov 2023 dev build ESM with every record type needed to spawn it in-game. it has its own race, leveled NPC, skin mesh, armor addon, and a health curve table that scales it to 20,000 HP at level 100. this wasn't a joke test entry — it was built with the same record structure as every other boss creature in the game.

in retail, every BossChicken record was renamed with a `ZZZ_` prefix (ZZZ_BossChickenRace, ZZZ_LvlBossChicken, etc.), which is bethesda's standard convention for disabled/deprecated content. this confirms it was deliberately shelved, not accidentally deleted.

## confirmed records

### dev build (original, functional)

| type | editor id | form id | purpose |
|------|-----------|---------|---------|
| RACE | BossChickenRace | 0x00636DDA | the creature's race — skeleton, body model, animation graph, behaviors |
| NPC_ | LvlBossChicken | 0x00636DD9 | leveled NPC record — what the game spawns, scales with player level |
| ARMA | AABossChicken | 0x00636DD5 | armor addon — attaches the skin mesh to the skeleton |
| ARMO | SkinBossChicken | 0x00636DD6 | armor record wrapping the skin — connects ARMA to NPC |

### retail (disabled with ZZZ_ prefix)

| type | editor id | purpose |
|------|-----------|---------|
| RACE | ZZZ_BossChickenRace | disabled race |
| NPC_ | ZZZ_LvlBossChicken | disabled leveled NPC |
| ARMA | ZZZ_AABossChicken | disabled armor addon |
| ARMO | ZZZ_SkinBossChicken | disabled skin armor |

the fact that retail keeps ZZZ_ versions means the records still exist in SeventySix.esm — they're just flagged as inactive. the form data is still there; the creature could theoretically be re-enabled with an ESM edit.

## health curve

the health curve table at `data/curve_tables/creatures/health/health_bosschicken.json` defines:

| player level | BossChicken HP |
|-------------|---------------|
| 25 | 2,000 |
| 50 | 8,000 |
| 100 | 20,000 |

for comparison, here's how this stacks up against other boss creatures:
- a level 100 scorchbeast queen has ~32,767 HP
- a level 100 mirelurk queen has ~5,000-8,000 HP
- a level 100 sheepsquatch has ~12,000-15,000 HP

at 20,000 HP at level 100, BossChicken would have been a serious boss-tier creature — tougher than a mirelurk queen, approaching sheepsquatch territory. this is not test data. these numbers were tuned to fit the game's existing creature power curve.

the curve has only 3 data points (levels 25, 50, 100), which is standard for fo76 creature health tables. the scaling is aggressive — HP quadruples from level 25 to 50, then nearly triples again from 50 to 100.

## form ID cluster analysis

all four form IDs sit in a tight cluster:
- 0x00636DD5 (AABossChicken)
- 0x00636DD6 (SkinBossChicken)
- 0x00636DD9 (LvlBossChicken)
- 0x00636DDA (BossChickenRace)

this 5-ID range (DD5-DDA) means they were created as a batch in a single development session. the IDs are also in the same neighborhood as NukaWorld on Tour content (E09A_Launcher_Weapon at 0x00636969) and ArcadeManagerQuest (0x0063F8D6), placing the creation date in the same mid-to-late 2023 development period.

## what kind of creature was this

fo76 has regular chickens (docile ambient creatures found around farms in appalachia). a "boss" chicken would be their irradiated/mutated giant variant, following the same pattern as:
- chicken -> BossChicken (cut)
- mirelurk -> mirelurk queen
- radstag -> glowing/legendary radstag
- mole rat -> glowing mole rat

the "Lvl" prefix on LvlBossChicken confirms this was a leveled creature — it would spawn at different levels with scaled stats. having its own RACE record means it had a unique skeleton and body proportions, not just a resized chicken.

## what's missing

while the core creature records are present, some expected supporting records were not found in the cut content:
- **CSTY (combat style)** — how it fights. previous analysis referenced a "csBossChicken" but this wasn't found in the cut records specifically. it may have been shared with another creature type or renamed.
- **sound records** — no BossChicken-specific audio was found in the cut records
- **encounter records** — no spawn point or location data tying it to a specific area

this could mean the creature was cut before its combat behavior and world placement were finalized, or that those records were merged into other existing combat styles rather than being standalone cut records.

## why this is novel

no wiki, datamine, or community source documents BossChicken. the Fallout 76 creature lists, cut content pages, and datamine articles all miss it. the closest anyone has come is documenting regular chickens (ambient critters added to Appalachia). the existence of a boss-tier giant chicken with 20,000 HP that was fully built and then shelved is completely undocumented.
