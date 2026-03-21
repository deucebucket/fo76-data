# FO76 Finding 098: Complete Cut Content Catalog -- Deleted Quests, Hidden Cells, Disabled Objects

## Status: CONFIRMED -- 99 cut quests, 120+ debug/test cells, 200+ cut NPCs, dozens of orphaned items
## Source: SeventySix.esm full dump, dev build ESM diff, string tables

---

## Part 1: All Deleted and Cut Quests (99 Total)

### 1A. Scorched Fever / Fire Breathers Cut Quests

**SF05_ReturnToNormalcy_CUT** (`0x00011A5A`)
- Stages: Collect 3 sets of clothing, place them on mannequins
- Aliases: Mannequin1-3, PlacedClothing1-3
- Context: Fire Breathers quest where player restores normalcy by dressing mannequins in pre-war clothing. A humanizing, post-disaster recovery mission.

**SF06_RespectTheDead_CUT** (`0x00004158`)
- Stages: Prime 3 mannequins, burn them, fight aggro greeter (NPC "CINDY" taunts player)
- Aliases: Mannequin1-3, nukaGrenade, GrenadeContainer
- Context: Ceremonial cremation quest. Player throws Nuka grenades at mannequins representing the dead. CINDY is an antagonist NPC who taunts during the ceremony.

**SF06_Radio_CUT** (`0x00354E17`)
- Stages: Started
- Aliases: Transmitter
- Context: Radio broadcast component of the Respect the Dead quest.

**SF07_MoeDigsSafety_CUT** (`0x0004BBFB`)
- Stages: Go to Tour Location, Kill Large Creature, Complete
- Aliases: BossCreature, SF07_Costume, SmallCreatures
- Context: Player wears a Moe the Mole mascot costume and exterminates creatures at a tour location. Comedic boss-fight quest.

**SF08 "Suicide Run" -- TWO-PART CUT QUEST**

**CUT_SF08_SuicideRunPre** (`0x0000DEC7`)
- Stages: Pick up Moe Costume, Wear destroyed Moe costume
- Aliases: DirtyMoeCostume
- Context: Prelude quest -- player finds and dons a destroyed Moe the Mole mascot costume.

**CUT_SF08_SuicideRun** (`0x00015676`)
- Stages: Disarm Mines (0/5), one by one, Quest Complete or Quest Failure
- Aliases: Mine1-5, DirtyMoleCostume, BarnesBody, BarnesHolotape, MoleRatSwarm
- Connected items: CUT_SF08_SuicideRun_BarnesLastNote (`0x0000898B`), CUT_SF08_SuicideRun_BarnesBody (`0x0000899E`)
- Context: Player in a Moe the Mole costume must disarm 5 mines while mole rats swarm. Barnes died attempting this run. His body and final holotape tell the story. A darkly comedic "mascot minefield" quest.

### 1B. Mire / Mountain / Region Cut Quests

**CUT_MTNS03_Orienteer_01** (`0x00027DEE`) + **Misc** (`0x00027DEF`)
- Stages: 6 control points to find using Orienteering Terminal at Spruce Knob
- Aliases: TerminalRef, ControlPoints
- String table confirms: "This week's Orienteering Control Points are scattered throughout the Spruce Knob area"
- Context: Navigation/exploration quest tied to the existing Scout system. Would have been a repeatable orienteering challenge.

**CUT_Dialogue_MTNS03_QuestGiver** (`0x00027DE8`)
- Context: NPC quest giver dialogue for the Orienteering quest above. Completely stripped.

**CUT_MTNZ01_Habit** (`0x00027E1B`) + **EBS** (`0x0014E75E`)
- Stages: Bring a specific chem to Rose, chem is removed from inventory, Rose gives dialogue
- Aliases: Rose, CurrentChem, ChemMarker
- Context: "Feed the Habit" -- Rose asks you to bring her chems. Repeatable fetch quest for the raider radio host. The EBS version (`0x0014E75E`) would have broadcast an emergency alert to start it.

**CUT_MTNM03_Misc** (`0x0017CD87`)
- Stages: Get recipe from terminal, craft spiritual incense, use incense in brazier
- Aliases: GuidedMeditationLocation, Brazier, Terminal
- Context: Crafting quest at the Guided Meditation location. Player makes ritual incense -- cut content for the Palace of the Winding Path monastery.

**MTNS02_Curse_CUT** (`0x0002E539`)
- Aliases: MTNS02_CorpseAlias, MTNS02_WendigoAlias
- Context: Wendigo curse quest. Corpse + Wendigo encounter, likely a horror investigation.

**CUT_MTNM04_Master** (`0x0003FC94`)
- Context: Master controller quest, completely stripped. Name suggests mountain region master quest orchestrator.

**MTR01_Flame_CUT** (`0x001D33D2`)
- Stages: Craft precursor chemicals (4 options, A01/A02/B01/B02), combine at forge, drop off materials
- Aliases: TargetFire01, TargetFire02, TargetForge, Precursors A/B
- Context: Elaborate crafting quest involving forge chemistry. Player makes two pairs of chemical precursors and combines them. Multi-step alchemy quest.

**SFM01_Glow_CUT** (`0x0022728C`)
- Stages: Spin up radstorm, play EBS, increase water at Crevasse Dam, neutralize river at Dyer Chemical, collect Aluminum/Oxygen/Silicon/Catalyst, place chemicals, defend against Mirelurk Queen
- Aliases: CrevasseDamTerminal, DyerChemicalTerminal, MirelurkQueenLocations
- Context: MAJOR CUT EVENT -- "The Glow" was a public event where players would respond to a radstorm emergency, manipulate dam infrastructure, collect and place chemicals, then fight a Mirelurk Queen. Multi-stage environmental disaster response event.

**SFS01_Brew_CUT** (`0x002564DA`)
- Stages: Prep 3 distillers, start generator, defend distillers from waves, collect rewards
- Aliases: Distiller01-03, DistillerBoiler01-03, SundayBrothersCabin
- Context: Brewing defense event at Sunday Brothers' Cabin. Prepare stills, defend from enemies in waves. A tower-defense style quest around moonshine production.

### 1C. Vault Raid System -- MASSIVE CUT CONTENT (20+ Quests)

The original Vault Raid system was far more elaborate than what shipped. Three vaults (63, 94, 96) had complete multi-mission quest lines that were cut.

**Vault 94 (The GECK Vault)**

**V94Access_CUT** (`0x0000E79B`)
- Stages: Listen to radio broadcast, investigate Vault 94, locate access code
- Aliases: AccessTerminal, AccessCode, AmbassadorCorpse, MapMarker
- Context: Original Vault 94 access quest with radio-guided entry sequence.

**CUT_V94_2_OLD** (`0x0005A242`)
- Stages: Identify radiation source, unseal GECK Wing (requires council vote), locate GECK, restore containment field, defend GECK
- Note in stages: "'G.E.C.K.' is pronounced 'Geck', as in gecko -- don't say the individual letters"
- Context: The GECK mission. Players had to pass a resolution through the Vault's council system to unseal the wing containing the Garden of Eden Creation Kit. This is significant lore -- a fully functional GECK was in Vault 94.

**CUT_V94_3_OLD** (`0x0005A241`) + **Escape** (`0x0014DF31`)
- Stages: Initiate Emergency Flooding Protocol, follow instructions, escape from Vault 94
- Context: Flood escape sequence. Players trigger emergency flooding and must escape before drowning.

**CUT_V94_1_Repair** (`0x0046B531`)
- Stages: Head for Pump Control Station, repair pipes in Atrium/Residential/Engineering Wings, drain water
- Context: Detailed pipe repair quest moving through multiple vault sections.

**CUT_V94_1_Access** (`0x0046B532`)
- Stages: Find Tyrone's ID, access Nursery/Workroom/Community Council Chamber, get Reset Codes
- Context: Exploration quest through vault living quarters to find access credentials.

**CUT_V94_1_Reactor** (`0x0046B533`)
- Stages: Restart the Reactor
- Context: Power restoration sub-quest.

**CUT_V94_1_Reset** (`0x0046B534`)
- Stages: Reset Flood Control Pumps Alpha/Beta/Gamma/Delta
- Context: Four-pump reset sequence to prevent flooding.

**CUT_V94_2_Scenes_OLD** (`0x00482D60`)
- Context: Scene controller for the GECK mission.

**Vault 96 (The Genetics Vault)**

**V96_Access_CUT** (`0x00324120`) + **V96Access_CUT** (`0x0041F800`)
- Stages: Listen to radio, investigate vault, acquire meat of endangered critter, place sample in genetic analyzer
- Context: Two versions of the Vault 96 access quest. Players had to hunt a specific endangered creature and bring its meat to prove genetic viability.

**V96_CUT** (`0x00324121`)
- Stages: Three missions with Prep/Ready/Shutdown phases each
- Aliases: PredatorCreatureName, PreyCreatureName
- Context: Master quest controller for Vault 96's genetics preservation missions.

**CUT_V96_1_CUT** (`0x0032411F`)
- Stages: Open 4 sections progressively, clear enemies in each, reach mainframe
- Context: Progressive dungeon clear through the vault's creature containment sections.

**CUT_V96_2_CUT** (`0x0032411E`) + **V96_3_CUT** (`0x00324122`)
- Stages: Restart Pump System
- Context: Pump maintenance sub-quests.

**Vault 63 (The Nuclear Vault)**

**V63Access_1_CUT** (`0x003241AB`)
- Stages: Listen to radio, find nuclear engineer, obtain ID card from corpse at VTU, use ID
- Context: Access required finding a nuclear engineer's corpse at Vault-Tec University.

**V63Access_2_CUT** (`0x00335398`)
- Stages: Find on-duty Fire Chief's ID at Charleston Fire Department
- Context: Alternate access path through the fire department.

**V63Access_3_CUT** (`0x00335397`)
- Stages: Find Military Officer's ID at Camp McClintock
- Context: Third access path through military credentials.

**V63_CUT** (`0x003241AC`)
- Stages: Three missions with Prep/Ready/Shutdown phases
- Context: Master quest like V96, three rotating missions.

**V63_1_CUT** (`0x003241AD`)
- Stages: Run Cooldown Process, Secure Reactor Until Cooldown Complete
- Context: Nuclear reactor cooldown mission. The vault's reactor was in meltdown.

**V63_2_CUT** (`0x00335399`)
- Stages: Gain access through Residential/Recreation/Atrium/Maintenance areas, activate Fire Suppression
- Context: Fire suppression quest moving through the vault's residential areas.

**V63_3_CUT** (`0x00335396`)
- Stages: Stop the Riot, turn in the Culprits
- Context: Social disorder quest -- a riot broke out among vault dwellers and players must apprehend the culprits.

### 1D. Enclave and Endgame Cut Quests

**CUT_EN02_Misc** (`0x000293A4`)
- Stages: Player greeted by MODUS, shut down system
- Aliases: WhitespringBunkerLocation, BunkerKeypad, BunkerDoor
- Context: Alternate MODUS encounter at the Whitespring Bunker.

**CUT_FF15_Lockdown** (`0x00056FD2`)
- Stages: Examine corpse (Hayley), listen to holotape, investigate terminal, retrieve Overseer keys for Vaults 63/94/96, disable Alpha/Beta/Gamma, use final terminal
- Aliases: HayleyCorpse, HayleyHolotape, Vault63/94/96 OverseerKey/Desk
- Context: MAJOR CUT QUEST -- "Lockdown" was a quest where players find Hayley's body and her holotape revealing a conspiracy. Players then retrieve Overseer keys for ALL THREE vaults and disable security systems. This was the original meta-quest connecting the entire Vault Raid system.

### 1E. Wastelanders (W05) Cut Quests

**CUT_W05_MQS_201P_MotherlodeWave** (`0x003F514C`)
- Stages: 3 enemy waves at Motherlode location, each with threshold kills
- Aliases: MotherlodeActivator, ActiveEnemies
- Context: Wave defense at the Motherlode during the Wastelanders main quest. Cut from the final version.

**zzz_W05_SettlersDaily_Painting** (`0x003F28CC`)
- Stages: Pick up paint, paint 3 graffiti locations
- Context: Daily quest to paint Foundation's graffiti/murals. Community beautification.

**zzz_W05_SettlersDaily_Clinic** (`0x003F2DC7`)
- Stages: Get recipe, craft medical kit, deposit kit
- Context: Daily quest to craft and deliver medical supplies to Foundation's clinic.

**zzz_W05_SettlersDaily_Stew** (`0x003F2DC9`)
- Stages: Get recipe, cook stew, deposit stew
- Context: Daily quest to cook and deliver food to Foundation.

**zzz_W05_SettlersDaily_Fieldhand** (`0x00403436`)
- Stages: Get animal feed, feed 4 animals
- Context: Daily quest to feed Foundation's livestock. The settlers had a working farm.

**zzz_W05_SettlersDaily_Restock** (`0x0041B725`)
- Stages: Get recipe, craft supply kit, deposit kit
- Context: Daily quest to restock Foundation's supplies.

**zzz_W05_SettlersDaily_Secret** (`0x00541685`)
- Stages: Find kickball, return to Elsie/Davie, optional step
- Aliases: actorElsie, actorDavie
- Context: Secret daily quest involving settler children (Elsie and Davie) and their lost kickball. NOTE: Elsie and Davie Taylor are LIVE Foundation NPCs — they shipped as part of Wastelanders content. This specific daily quest variant was cut, but the characters themselves are in-game.

**CUT_W05_Community_Treehouse_Village_Quest** (`0x00555A72`)
- Stages: Fix generator, help settlers, repair 3 objects (power/alarm/other), choose what to activate, defend from attack
- Aliases: TreehouseLocationAlias, LeaderAlias, Settler02/03Alias
- Context: MAJOR CUT LOCATION QUEST -- Treehouse Village was a planned settlement location with a quest line. Players would help settlers establish defenses, make choices about infrastructure (power vs alarm), and defend against attacks. This location was planned but never placed in the world.

**CUT_W05_Community_RaiderBlockade_Quest** (`0x00558E32`)
- Stages: Quest Started, Quest Completed
- Aliases: BlockadeLocationAlias, Guard01/02, TreepassGuard01/02, AllPlayersAlias
- Context: Raiders blocking access to a location. A confrontation quest at a raider checkpoint.

**CUT_W05_DialogueWaywardRC_JideGracie_Gift/Mort/ToadSteaks** (`0x0042ECD4-D8`)
- Aliases: Jide, Gracie
- Context: Three cut dialogue quests between NPCs Jide and Gracie at The Wayward. Topics: giving a gift, discussing Mort (the Mothman lookalike), and toad steaks. Shows deeper NPC relationship content.

**CUT_BS01_Dialogue_TreehouseVillage** (`0x005C8B50`)
- Context: Additional dialogue for the cut Treehouse Village location.

### 1F. Companion System Cut Quests

**DELETED_COMP_RECreateCompanion** (`0x003F5E73`)
- Context: Random encounter that would create/spawn a companion. Scrapped companion spawning system.

**COMP_Conversation_Astronaut_Emerson/Athena_020_Vendor_CUT** (`0x00574622/24`)
- Aliases: Astronaut, Visitor (Emerson/Athena)
- Context: Sofia Daguerre (the Astronaut companion) had cut conversations with both Emerson and Athena as visitors. These were vendor-related dialogue trees.

**DELETED_COMP_Conversation_Beckett_Visitor_009/013_Ronny** (`0x00582158/6D`)
- Aliases: Beckett, Ronny
- Context: Ronny was a cut visitor NPC who would visit Beckett twice (conversations 9 and 13). Ronny was likely a Blood Eagles contact.

**DELETED_COMP_Conversation_Beckett_Visitor_015_Sage** (`0x0058216C`)
- Aliases: Beckett, Visitor (Sage)
- Context: Sage was another cut visitor for Beckett's questline.

**DELETED_COMP_Quest_Outtro_Full_Beckett** (`0x00582161`)
- Stages: Talk to Beckett, Find Brother's Room, Talk with Brother, CHOICE: Edwin's Gang kills the Bone OR kills the Blood Eagles generally
- Aliases: Poseidon interior markers, JailKeys, JailDoor, spawnMarker
- Context: MAJOR CUT -- Beckett's original ending was at Poseidon Energy Plant. Players found Beckett's brother in a jail cell, had a choice about how Edwin's gang would handle the Blood Eagles. Much more elaborate than the shipped version.

**DELETED_COMP_RQ_Fetch_SpecificAliases_Beckett_007_Formula** (`0x0058215C`)
- Context: Beckett sends player to fetch a chemical formula.

**DELETED_COMP_RQ_Kill_SpecificAliases_Beckett_011_MurderBot** (`0x00582166`)
- Context: Kill quest targeting a "Murder Bot" for Beckett.

**DELETED_COMP_RQ_Fetch_SpecificAliases_Beckett_012_BrotherClawHolotape** (`0x00582169`)
- Context: Fetch the "Brother Claw" holotape for Beckett -- deeper Blood Eagles lore.

**DELETED_COMP_RQ_Fetch_SpecificAliases_Beckett_014_BearHolotapeDatabase** (`0x005966FB`)
- Context: Fetch the "Bear" holotape database -- more Blood Eagles intelligence.

**DELETED_COMP_RQ_Rescue_SpecificAliases_Beckett_015_Defector** (`0x00582159`)
- Context: Rescue a Blood Eagles defector for Beckett.

**DELETED_COMP_RQ_Astronaut_001_Athena/002_Vendor** (`0x0059D817/18`)
- Context: Two cut astronaut companion radiant quests involving rescuing Athena from robots, and rescuing a vendor from robots.

### 1G. Event and Public Quest Cut Content

**CUT_GQ_Invasion** (`0x003CF449`)
- Stages: Clear 3 invasion locations
- Aliases: InvasionLocation01-03, InvasionEnemies01-03
- String table: "Super Mutants have invaded <Location>. Drive them out!"
- Context: Multi-location invasion clearing event. Super Mutants simultaneously invade 3 locations.

**CUT_PowerPlantStartup** (`0x003E7F1E`)
- Context: Power plant startup event, completely stripped. Would have been a public event.

**CUT_Factory_GraftonSteel** (`0x00241430`)
- Stages: Obtain Ignition Cores, install them, start Blast Furnace, repair Furnace/Smelter/Mill
- Aliases: FactoryLocation, IgnitionCoreActivator, FurnaceDestructibles
- String table confirms detailed stage descriptions about restarting Grafton Steel's industrial equipment
- Context: Workshop-style event to restart the Grafton Steel factory. Multi-stage industrial repair quest.

**CUT_E01F_Fasnacht_Master** (`0x0046F508`)
- Stages: Enable decorations and Master of Ceremonies
- Context: Original Fasnacht event master controller. Replaced by the current version.

**CUT_SFZ03_Queen_MasterQuest** (`0x0043D032`)
- Aliases: SFZ03BossEligiblePlayers, LocNormalBoss01-05, LocCryptidBoss01-04
- Context: ALTERNATE SCORCHBEAST QUEEN SYSTEM -- Originally 5 normal boss locations and 4 cryptid boss locations. The Queen fight was designed to rotate between these locations rather than always spawning at the fissure site.

**zzz_TWZ09** (`0x00088A9A`)
- Stages: Kick aerosolizers at 3 farms, collect fertilizer, event timer, baseball announcer commentary
- Note in stages: "Baseball play by play announcer. Chipper and upbeat. Stretch and roll the R in Grrrrrrafton"
- Context: A Grafton farm event with a baseball announcer narrating the action. Players activate aerosolizers at three farm locations and fight enemies. Comedic event with sports commentary.

**CUT_RE_SceneBB02** (`0x004ECC75`)
- Stages: "Stage when cats are all dead"
- Context: Random encounter involving cats being killed. Dark content that was cut.

**CUT_TESTWeather** (`0x00435462`)
- Context: Weather test quest, completely stripped.

### 1H. Random Encounter Cut Quests

**RE_SceneDRE05GQ_CUT** (`0x000187DD`)
- Stages: Assaultron ready, cook at station, kill bloatflies, collect meat, bake bloatfly, eat it, make Refreshing Beverage, drink it, Jesse gives dialogue, defeat Super Mutant boss
- Aliases: Assaultron, CookingStation, ChemStation, Boss
- Context: Multi-step random encounter with an Assaultron cooking companion. Player must cook bloatfly meat, make a drink, then fight a Super Mutant. Comedic cooking adventure with a robot.

**RE_SceneDRE05_CUT** (`0x000187DE`) / **RE_SceneDRE02_CUT** (`0x00019A32`) / **RE_SceneDRE03_CUT** (`0x0016B4B4`)
- DRE03 stages: "Cubs attacked, Mother killed"
- Context: Three cut random encounter scenes. DRE03 involved animal family drama -- baby creatures and their mother.

**DELETED_RE_SceneCMB01** (`0x00453B6D`)
- Stages: Robot greets player, gives smoke grenades, end encounter
- Context: Friendly robot encounter that gives the player smoke grenades. Cut NPC interaction.

**DELETED_RE_TravelDWD02_Old** (`0x00481EEA`)
- Aliases: AlbinoYaoGuai, AlbinoDeathClaw
- Context: Rare albino creature travel encounter -- Albino Yao Guai and Albino Deathclaw together.

**DELETED_RE_TravelDWD03_Old** (`0x00481EE9`)
- Aliases: EyeBotActor01, PoliceA
- Context: Eyebot and police encounter.

**DELETED_RE_ObjectDWD01/02_Old** (`0x00481EEC`, `0x00460613`)
- DWD01 stages: "Under his breath"
- Context: Whispering NPC encounter objects.

**DELETED_RE_SceneDWD07_Old** (`0x00481EEB`)
- Context: Another cut scene encounter.

**DELETED_W05_RE_AssaultBB01** (`0x0056F036`)
- Stages: Trigger Assault, Defenders win, Attackers win
- Context: Assault encounter with attackers vs defenders and lootable objects.

### 1I. Miscellaneous Cut Quests

**CUT_P01B_Unsolved_MasterQuest** (`0x003EEA5D`)
- Stages: Setup for "A Perfect Getaway", "Lying Lowe/Lowe Down", "A Friend In Need"
- Aliases: Squatch01_EnableMarker_Harpers, Wolf_EnableMarker
- Context: Master quest for the "Unsolved" mystery quest series involving the Sheepsquatch. Would have orchestrated multiple mystery quests.

**CUT_CreatureDialogueGorilla** (`0x000FC7FE`)
- Stages: "Gorilla idle dialogue. Ignore for export"
- Context: GORILLAS WERE PLANNED FOR FO76. They would have had idle dialogue/vocalizations. No gorillas exist in the shipped game.

**CUT_DONOTUSE_CreatureDialogueDLC03CrRobotRobobrain** (`0x0035ABF3`)
- Context: Robobrain dialogue imported from Fallout 4 DLC03 (Far Harbor). Never adapted for 76.

**zzz_SQ_CustomItemQuest** (`0x00437AE8`)
- Aliases: CB04/RSVP03/EN02/EN05/FS01/MTNM01/RS01B/SFL02/SFM04/TW002 CustomItemNames
- Context: System for custom-named quest items across 10 different quest lines. A naming/personalization system that was cut.

**CUT_RSVP00/01/03_Quest_Note** (`0x004FC02F`, `0x004FC02A`, `0x004FC023`)
- RSVP00: Find Flatwoods
- RSVP01/03: Use Terminal, completion
- Context: Responders volunteer program note quests. RSVP = Responders Volunteer Program.

**CUT_VTemp** (`0x00040E4F`)
- Context: Vault template quest, completely stripped.

### 1J. Burning Springs (Backwoods) Cut Quests

**ZZZ_Storm_ST** (`0x006E30D7`)
- Context: Storm quest, stripped.

**ZZZ_Burn_RE_FactionAssault_RKR_Stingwing** (`0x0081AD0F`)
- Stages: Trigger Faction Assault, Faction 01/02/03 wins
- Context: Three-faction stingwing assault encounter in the Burning Springs region.

**ZZZ_Burn_Drive-in_Holotape** (`0x00848625`)
- Connected note: ZZZ_Burn_DriveIn_Holotape (`0x0084864A`)
- Context: Drive-in holotape quest for the Burning Springs drive-in theater location.

**ZZZ_XPD_AC_VendorDialogueQuest** (`0x00752278`)
- Aliases: Loc_Pier, Loc_Quentinos, Loc_CityHall, Vendor_Showmen, Vendor_Mob, Vendor_Muni
- Context: Atlantic City vendor dialogue system with three vendor factions (Showmen, Mob, Municipal).

### 1K. Expeditions and DLC Cut Quests

**CUT_XPD_Pitt02_Mission_HelplessSurvivor_01/02/03** (scenes `0x0064DE7B-7D`)
- Context: Three cut Pitt Expedition scenes involving helpless survivors. Rescue scenarios removed from The Pitt.

**CUT_AC_MQ02_Stage_AimedForLimbs_00/01** (scenes `0x006F58C9`, `0x006FC2F7`)
- Context: Atlantic City main quest scenes about aiming for limbs. Combat tutorial or special mechanic.

**CUT_AC_MQ04_Sins_AbbieMansion** (scene `0x006F7C80`)
- Context: Atlantic City main quest scene at "Abbie's Mansion" dealing with sins.

---

## Part 2: Hidden, Test, and Debug Cells (120+ Cells)

### 2A. Cut Game Locations (Accessible via console/glitch)

| Cell | Form ID | Description |
|------|---------|-------------|
| zCUTVault63 | `0x00121929` | Original Vault 63 interior -- predates the Skyline Valley version |
| zCUTVault63Entrance | `0x00044A50` | Original Vault 63 entrance area |
| zCUTVault65 | `0x00002E22` | VAULT 65 -- never released, never announced |
| zCUTVault94Main | `0x00456F1D` | Original Vault 94 interior layout |
| zCUTVault96Gear02 | `0x003F3A55` | Vault 96 gear room variant |
| zCUTVault9603Steve | `0x0046085D` | Developer Steve's Vault 96 test area |
| zCUTHuntersvilleSewers | `0x00006F40` | CUT DUNGEON -- Sewer system beneath Huntersville |
| zCUTMoleManCity01 | `0x000242A2` | CUT DUNGEON -- Mole Miner underground city |
| zCUTMireBunker01 | `0x0040A89D` | Cut bunker in The Mire |
| zCUTWhitespringResort01 | `0x00098971` | Cut Whitespring interior section |
| zCUTGraftonDam01 | `0x00208DF0` | Cut Grafton Dam interior dungeon |
| zCUTMonongahMissileSilo01OLD | `0x00530EBC` | Original missile silo design |
| zCUTMissileSiloOLD | `0x005211F5` | Even older missile silo layout |
| zCUTSpruceKnobMissileSilo01OLD | `0x0036DABA` | Spruce Knob missile silo variant |
| zCUTSecretResearchLaboratory01 | `0x0054E80D` | SECRET RESEARCH LAB -- unnamed cut interior |
| zCUT76TrailerInterior | `0x003C2985` | Pre-release trailer interior set |
| zCUTRaRaPrototypes01/02/03 | `0x0041302A/29/28` | Three prototype Ra-Ra quest cells |
| zCUTBabylonStagingAreaZax | `0x002B802D` | Nuclear Winter ZAX staging area |
| zCUTCharlestonHoldingCell | `0x00004057` | Charleston holding cell (quest staging) |
| zCUTProtoExpo01/05 | `0x005B0624/5B5E1E` | Prototype exposition cells |
| zCUTSheltersUnusedBoSBunker | `0x005A5883` | Unused BoS bunker shelter layout |
| zCUTTestOrionWatogaCivicCenter | `0x005A0384` | Watoga Civic Center test -- planned Orion content |
| zCUTTestMothman | `0x0052F531` | Mothman behavior test cell |
| zCUT76AITestCellSheepsquatch | `0x003F53FC` | Sheepsquatch AI test arena |
| zCUT76AITestCellMoleMiner | `0x000E2805` | Mole Miner AI behavior cell |
| zCUT76AITestCellTick | `0x0005F105` | Tick creature AI test cell |
| zCUTTestConvertedMunitionsFactory01 | `0x0010E5C6` | Converted Munitions Factory test layout |
| zCUTDebugVault79Entrance | `0x00403828` | Vault 79 entrance debug area |
| zCUTDebugCrackpotsHouse01 | `0x00403827` | Planned "Crackpot's House" interior |
| zCUTW05MQS205PTest | `0x0041CB6F` | Wastelanders MQ test cell |
| zCUTW05DialogueTestInstanced | `0x005633A8` | Wastelanders dialogue testing |
| ZZZBurnCheckpointCanyonInterior | `0x007DF6DE` | Burning Springs canyon checkpoint interior |
| ZZZ76StormGPVault | `0x006862F6` | Storm/Lost vault cell |
| ZZZStormWeatherLab | `0x006BB412` | Weather testing laboratory |
| ZCUT76GOD11 | `0x007C22B7` | D11 (Burning Springs) game object cell |
| CharGen03 / CharGen04 | `0x0051EF4F/4E` | Character generation rooms |
| zCUTUnusedVault120/Airlock/02/03 | `0x00004D4D/4CCA/4D4C/4CF4` | VAULT 120 -- 4 cells for a vault that was never completed |

### 2B. Developer Test Cells (Named After Developers)

| Cell | Form ID | Developer |
|------|---------|-----------|
| DebugLiam | `0x0000208A` | Liam |
| DebugJamesP | `0x00209234` | James P |
| DebugSteveM / 02 | `0x0028D187/544975` | Steve M |
| DebugJamieC | `0x0030878F` | Jamie C |
| DebugJamieR | `0x0079A1EF` | Jamie R |
| DebugMJ | `0x003C6857` | MJ (contains Wastelanders test markers) |
| DebugDavidM | `0x003E08F9` | David M |
| DebugDobert / 04 | `0x004E231E/5F0E75` | Dobert |
| DebugCarlM02 | `0x00523D14` | Carl M |
| DebugJMoretto | `0x005A0596` | Josh Moretto (full test quest with NPCs Rebecca/Devin) |
| DebugJustinN02 | `0x005A5AE6` | Justin N |
| DebugBrianna | `0x005C8EB9` | Brianna |
| DebugElishaM | `0x00606D6E` | Elisha M |
| DebugJeffU01/03/05/07 | various | Jeff U (4 cells, lighting/dungeon tests) |
| DebugVeronicaH | `0x0062152C` | Veronica H |
| DebugABlack | `0x00623C66` | A Black |
| DebugRyanJohnson | `0x006781A8` | Ryan Johnson |
| DebugBrentC | `0x0067D4BF` | Brent C |
| DebugHillValley | `0x006AC521` | Hill Valley (Back to the Future reference?) |
| DebugRobA | `0x00383DAA` | Rob A |
| DebugMattT | `0x0061DAF0` | Matt T |
| DebugJosephSLightingExamples | `0x008270F8` | Joseph S |
| DebugBarbaraF / Instanced | `0x008952E0/8A45DA` | Barbara F |
| DebugCKinsey / 022 | `0x007ED9BE/837C1C` | C Kinsey |
| DebugBSTownBuildings | `0x0078BD9D` | BS (Burning Springs town building tests) |
| TestDan | `0x00807565` | Dan |
| TestCellVincent | `0x006779D9` | Vincent |

### 2C. Holding Cells (Quest Staging Areas)

| Cell | Form ID | Purpose |
|------|---------|---------|
| 76HoldingCellPowerSystem | `0x000182CC` | Power system quest objects |
| 76HoldingCellRegionForest | `0x00207A60` | Forest region quest items (contains RSVP holotape markers) |
| 76HoldingCellRegionMire | `0x0038C583` | Mire region quest items |
| 76HoldingCellWorkshop | `0x00062547` | Workshop system objects |
| 76HoldingCellMoM | `0x00345D4F` | Mistress of Mystery quest objects |
| 76HoldingCellMissionQuest | `0x0052C090` | Mission quest staging |
| 76HoldingCellESSTemp | `0x0012D5B7` | Event System Temp |
| 76HoldingCellMile | `0x007915F8` | Milestone quest staging |
| 76HoldingCellStorm | `0x006F618C` | Skyline Valley quest staging |

### 2D. Warehouse Cells (AI/Combat Testing)

| Cell | Form ID | Purpose |
|------|---------|---------|
| WarehouseUnused | `0x0077529A` | Unused warehouse |
| WarehouseTestAmbushes | `0x001CC3DE` | Ambush behavior testing |
| WarehouseCombat | `0x0014D4B0` | Combat mechanics testing |
| WarehouseEncounterWave / 02 | `0x00044CF1/076730` | Wave encounter testing |
| WarehouseTraps | `0x000EB775` | Trap mechanics testing |
| WarehouseActorRespawn01/02 | `0x00439AD7/D6` | Actor respawn behavior |
| WarehouseTestDefaultBehavior | `0x0034629F` | Default AI behavior |
| WarehouseTestHoldPos | `0x004F955D` | Hold position AI testing |
| WarehouseDoors | `0x001660F3` | Door mechanics testing |
| WarehouseSubStations | `0x0032676E` | Substation layout testing |
| WarehouseVaultKit | `0x0007C659` | Vault kit piece testing |
| WarehouseFissureCell | `0x0048A196` | Fissure site testing |
| WarehouseRaids | `0x0078CBDF` | Vault Raid encounter testing |
| WarehouseExpeditionsDungeon | `0x006139EB` | Expeditions dungeon testing |
| WarehouseExpeditionsBeautifulCorner | `0x0062BC0D` | Expeditions aesthetics testing |
| WarehouseCrowds | `0x00749DC9` | NPC crowd behavior testing |
| WarehouseEWSTest | `0x005E95AE` | Emergency Warning System testing |

---

## Part 3: Cut Weapons, Armor, and Items

### 3A. Cut Weapons

| Item | Form ID | Description |
|------|---------|-------------|
| CUT_NeedleSMG | `0x006CCC2E` | Needle-based submachine gun -- entirely new weapon type |
| zzz_NitroRifle | `0x0085780F` | Nitro-powered rifle |
| zzz_TeslaCannon_MissileLauncher | `0x00799A10` | Tesla Cannon / Missile Launcher hybrid -- early iteration (Tesla Cannon SHIPPED via Gleaming Depths) |
| zzz_TeslaCannon_NukaLauncherTest | `0x007999F4` | Nuka-powered Tesla Cannon test variant (Tesla Cannon SHIPPED via Gleaming Depths) |
| zzz_GatlingPlasmaLost | `0x00773F9D` | Lost faction Gatling Plasma variant |
| zzz_MissileLauncherLostNPC | `0x00773F9C` | Lost faction Missile Launcher |
| zzz_HeadHunter_Scythe | `0x007551DE` | Scythe melee weapon -- "Head Hunter" themed |
| zzz_Broadsider_FusionCannon | `0x0074D578` | Fusion-powered Broadsider variant |
| zzz_HeavyIncinerator | `0x0072A8C2` | Heavy Incinerator -- early iteration (SHIPPED via America's Playground update) |
| zzz_Moon_CultistPickaxe | `0x006A0092` | Cultist pickaxe for Mothman event |
| zzz_Moon_Flamer_BlueFlamer | `0x00693D37` | Blue flame variant Flamer |
| zzz_Moon_NukaAcidGrenade | `0x00692A0D` | Nuka Acid Grenade |
| zzz_Moon_NukaHomemadeGrenade | `0x00692A0C` | Nuka Homemade Grenade |
| zzz_Moon_PumpActionShotgun_Tornado | `0x0069255D` | "Tornado" shotgun variant |
| zzz_Moon_JawboneBlade | `0x0069229A` | Jawbone melee weapon |
| zzz_E09C_CompoundBow | `0x00661DD9` | Compound Bow variant |
| zzz_LGN_NuclearProliferator_Weapon | `0x005CF0A0` | "Nuclear Proliferator" weapon |
| zzz_Burn_SingleActionRevolver_Prop | `0x0082B89A` | Burning Springs prop revolver |

### 3B. Cut Armor and Clothing

| Item | Form ID | Description |
|------|---------|-------------|
| zzz_Armor_Tempest (full set) | `0x00755144-49` | Complete "Tempest" armor set (ArmL/R, LegL/R, Torso, Headwear) |
| zzz_GHL_Disguise series | various | 12+ disguise outfits for Ghoul infiltration (BoS Scribe, Knight, Engineer, Enclave Officer, Raider, Silver Shroud, Fasnacht Mask, Ronin Helmet, Gas Mask) |
| ZZZ_Storm_Clothes_RadTurkey_Outfit | `0x0078211D` | Rad Turkey outfit |
| zzz_Storm_LostHeadMirror | `0x0072AA71` | Head mirror for Lost faction |
| zzz_SCORE_S19_Clothes_Enclave_Colonel | `0x00798131` | Enclave Colonel uniform |
| zzz_XPD_AC_Headwear_Muni | `0x006E734E` | Atlantic City Municipal headwear |
| zzz_MOON_ScoutHat | `0x006C8646` | Mothman event scout hat |
| ZZZ_OvergrownThornArmor_Torso | `0x006DEBE8` | Overgrown thorn armor variant |
| ZZZ_ATX_ARMO_Headwear_BirthdayHat | `0x006F65A1` | Birthday hat (Atom Shop cut) |

### 3C. Cut Notes and Holotapes

| Item | Form ID | Description |
|------|---------|-------------|
| CUT_SF08_SuicideRun_BarnesLastNote | `0x0000898B` | Barnes' final words about the mine-clearing suicide run |
| CUT_W05_Holotape_RobCoResearchCenter_Robobrains | `0x00586F1E` | RobCo robobrain research holotape |
| CUT_W05_MQS_201P_Holotape_TopographicMap | `0x0040E46B` | Topographic map holotape for Wastelanders MQ |
| CUT_LC091_MonPowerTransmission_Holotape | `0x002BA2E4` | Monongah Power transmission holotape |
| DELETED_Holotape | `0x0047B7F6` | Generic deleted holotape |
| ZZZ_Burn_DriveIn_Holotape | `0x0084864A` | Burning Springs drive-in holotape |
| zzz_P01B_Lying_Shelley03/04/05_Holotape | various | Three Shelley holotapes for the "Lying Lowe" mystery quest |
| zzz_P01B_CLUE_Holotape | `0x00478DE1` | Mystery clue holotape |
| zzz_Burn_ValdsDiary (7 entries) | `0x0085B8CE-D4` | Vald's Diary -- 7 entries spanning Nov 2077 to Sep 2105 (28 years of post-war journal) |
| Burn_CUT_Athens series | various | 6 cut Athens notes: Bestie Letter, Sport Car, University Essay, Halloween Block Party, Burn Pit, Water Distribution, Failed Scavenge |
| ZZZ_S21_Dottie_Note03 | `0x00824D14` | Ally Dottie's third note |
| zzz_NPE_NoteNathanRedSox | `0x0072BC30` | Nathan's Red Sox note (New Player Experience) |
| ZZZ_Burn_CheckpointCanyon_MonsterSighting | `0x008162DB` | Monster sighting at Checkpoint Canyon |

### 3D. Cut Miscellaneous Items

| Item | Form ID | Description |
|------|---------|-------------|
| zzz_DELETE_E07A_Mothman_Egg_MiscItem | `0x0061D14D` | Mothman Egg -- collectible cryptid item |
| CUT_HerdsmansBell_Bigfoot | `0x007AC0D8` | Bigfoot Herdsman's Bell -- BIGFOOT CAMP ITEM |
| CUT_Souvenir_Stein_FasnachtCommemorativeStein | `0x007AC034` | Fasnacht commemorative stein |
| ZZZCUT_BURN_SQ02_Turpentine/Battery/Lighter/DuctTape | `0x00815C73-76` | Burning Springs quest crafting components |
| zzz_BURN_SQ04_FilmPiece | `0x007D3DF7` | Film piece for drive-in quest |
| zzz_MutatedEvents_ConcentratedInfusionReagant | `0x00690658` | Mutated Event chemical reagent |
| zzz_MutatedEvents_InfusionReagant | `0x00683DF5` | Event infusion reagent |
| zzz_MutatedEvents_UnstableMedium | `0x00690657` | Unstable medium for mutated events |
| zzz_NukacadeTicket | `0x00644AE9` | Nukacade arcade ticket |
| zzz_E09C_HeartItem / small | `0x0065C096/666897` | Heart items (Nuka-World on Tour) |
| zzz_E08A_AcidGulperVenom | `0x00657DD8` | Acid Gulper Venom |
| ZZZ_RD01_Enc02_Fuel_DEPRECATED | `0x0079261A` | Vault Raid fuel item |
| zzz_c_LegendaryScrap_scrap | `0x0078040F` | Legendary scrap material |

### 3E. Cut Legendary Modules/Shards (22 Effects)

The legendary crafting system had 22+ additional effects that were cut:

| Shard | Form ID | Effect |
|-------|---------|--------|
| LegendaryShard_BloodHealers | `0x0062AFDA` | Blood healing |
| LegendaryShard_Bruisers | `0x006337C5` | Bruiser bonus |
| LegendaryShard_CarryWeight | `0x0062B360` | Carry weight increase |
| LegendaryShard_CheerLeader | `0x0062D31B` | Cheerleader support buff |
| LegendaryShard_Collectors | `0x0062AFEC` | Collection bonus |
| LegendaryShard_CriticalHealers | `0x0063384E` | Critical hit healing |
| LegendaryShard_Daredevils | `0x00633E8B` | Daredevil risk/reward |
| LegendaryShard_Elemental | `0x0062B79A` | Elemental damage |
| LegendaryShard_Elusive | `0x0062B7A8` | Elusiveness/dodge |
| LegendaryShard_Headhunters | `0x006346F7` | Headshot bonus |
| LegendaryShard_HeavyHitters | `0x0063367E` | Heavy attack bonus |
| LegendaryShard_IncreaseAPRegen | `0x006337E6` | AP regeneration |
| LegendaryShard_IncreaseAllyResists | `0x00631CE2` | Ally resistance buff |
| LegendaryShard_IncreaseAttackSpeedOnKill | `0x00634705` | Kill speed ramp |
| LegendaryShard_MaxAP | `0x0062D861` | Maximum AP increase |
| LegendaryShard_ReduceEnemyResists | `0x00634706` | Enemy resistance debuff |
| LegendaryShard_Scavengers | `0x006344F6` | Scavenging bonus |
| LegendaryShard_Warmongers | `0x006316B0` | Warmonger combat bonus |
| zzz_BOUNTY_LegendaryShard_Barbarian | `0x0084B66C` | Barbarian effect |
| zzz_BOUNTY_LegendaryShard_Armor2_Jagged | `0x00849310` | Jagged armor |
| zzz_BOUNTY_LegendaryShard_Weapon2_Ranged_Rebate | `0x0084930F` | Ammo rebate |
| zzz_BOUNTY_LegendaryShard_Weapon2_Melee_Pulsating | `0x0084930E` | Pulsating melee |

---

## Part 4: Cut NPCs and Creatures

### 4A. Cut Named NPCs

| NPC | Form ID | Context |
|-----|---------|---------|
| CUT_GHL00_Quest_AsherWhitt_Actor_WithBandana | `0x00798442` | Asher Whitt (Ghoul infiltration quest NPC) |
| CUT_GHL00_Quest_LeamonPrice_TEMP | `0x0078DB2E` | Leamon Price (Ghoul quest NPC) |
| zzz_BURN_SQ01_SilasKiller_NPC | `0x0084CA42` | Silas's killer (Burning Springs murder mystery) |
| zzz_BURN_SQ01_RKIGuard4_NPC | `0x0085CD35` | Rust Kingdom guard #4 |
| zzz_BURN_Millstone_NPC | `0x0084CC96` | Millstone character |
| zzzBURN_Eugene_NPC_TEMPDELETE | `0x007F79D4` | Eugene (Burning Springs NPC, temporarily deleted) |
| zzz_Storm_MQ13_HugoClones | `0x00739AC9` | Hugo clones (Skyline Valley MQ) |
| ZZZ_S17_Scoutmaster | `0x00771DD3` | Scoutmaster NPC |
| zzz_Raider_GenericF_Unaggressive | `0x00731734` | Non-hostile female raider |
| DEL_XPD_AC_DELETE (12+ faces) | various | 12+ cut Atlantic City NPC face templates |

### 4B. Cut Creature Types

| Creature | Form ID | Context |
|----------|---------|---------|
| CUT_CreatureDialogueGorilla | `0x000FC7FE` | GORILLAS -- never appeared in FO76 |
| EncMirelurkSpawnHatchlingRaiderFaction | `0x005B6C48` | Raider-faction mirelurk hatchlings (tamed?) |
| LvlBossChicken | `0x00636DD9` | BOSS CHICKEN -- leveled boss version |
| SFS08_Heart_LvlGrafton | `0x0052C789` | Grafton Monster heart event variant |
| SFS08_Heart_LvlMirelurkQueen | `0x0009318D` | Mirelurk Queen heart event variant |
| LvlSupermutantBoss_DailyOps | `0x005CB906` | Daily Ops super mutant boss |
| zzz_BURN_LvlAshCaver_Boss | `0x0082BB61` | Ash Caver boss (Burning Springs) |
| zzz_BURN_LvlOgua | `0x00821B45` | Ogua creature (Burning Springs cryptid?) |
| zzz_Storm_LvlLost series | various | 15+ Lost faction NPCs (Security, Ferals, Mr. Handy, Mr. Gutsy, Healers, Weather) |

### 4C. Cat Pet System (Animation Evidence)

Five dedicated animations exist for a cut pet cat system:
- CatPetDeath (`0x00545DBF`)
- CatPetDeathWait (`0x00545DBE`)
- CatPetIdleMeow (`0x0054467F`)
- CatPetTurnLeft (`0x00545DC3`)
- CatPetTurnRight (`0x00545DC4`)

These are IDLE animations (not combat), indicating cats were planned as CAMP pets with full behavioral AI before the current pet system existed.

---

## Part 5: Cut Locations (LCTN Records)

### 5A. Named Cut Locations

| Location | Form ID | Context |
|----------|---------|---------|
| LocMountainsIngramMansionLocation | `0x0037FA8F` | Ingram Mansion -- named mountain location, never placed |
| LocMountainsLousMineLocation | `0x0040BC91` | Lou's Mine -- cut mine dungeon |
| LocMountainsLousMineInteriorLocation | `0x0040D4E6` | Lou's Mine interior |
| Vault63Location | `0x0012192A` | Original Vault 63 location (before Skyline Valley) |
| LocMountainsUncannyCaverns DUPLICATE | `0x005F112C` | Duplicate Uncanny Caverns |
| LocMountainsWestTekResearch DUPLICATE | `0x005FAD0C` | Duplicate West Tek |
| LocMountainsWendigoCave DUPLICATE | `0x005FAD0D` | Duplicate Wendigo Cave |
| zzz_E09B_Wheel_BossName1-6 | various | 6 boss name locations for a "Wheel" event (Nuka-World) |
| zzz_MOON_Herd_LOC | `0x00690694` | Herd location for Mothman event |
| zzzLocBurnCornhengeLocation (4 copies) | various | "Cornhenge" -- corn Stonehenge, 4 early iterations (SHIPPED in Burning Springs as final version) |
| zzzLocBurnDriveinWorkshopLocation | `0x007BE4A2` | Burning Springs drive-in workshop |
| LocBurnPOI37UFOWatcherLocation | `0x0084E8A5` | UFO Watcher point of interest |
| LocBurnPOI101WildwoodRanchLocation | `0x0084DB64` | Wildwood Ranch |
| LocBurnPOI41ApiaryLocation | `0x0084DB5E` | Apiary (bee farm) |
| LocBurnPOI133AbraxodyneStorageDepotLocation | `0x0084DB63` | Abraxodyne Chemical storage |
| LocBurnPOI73DerelictPowerSubstationLocation | `0x0084DB62` | Derelict power substation |
| LocBurnPOI16HillsideChurchLocation | `0x0084DB5D` | Hillside Church |
| LocBurnPOI59LanganMillLocation | `0x0084DB61` | Langan Mill |
| LocBurnPOI54AlbanyLocation | `0x0084DB60` | Albany (SHIPPED in Burning Springs) |
| LocBurnPOI19SockHopLocation | `0x0084DB5C` | Sock Hop dance hall (SHIPPED in Burning Springs) |
| LocBurnPOI32DesolateEncampmentCampLocation | `0x0084DB5F` | Desolate Encampment |
| LocBurnPOI71PlaygroundLocation | `0x0084DB65` | Playground |
| SheltersLocation_NuclearTestBunker | `0x0069623F` | Nuclear Test Bunker shelter |
| SheltersLocation_ProspectorSaloon | `0x0086A801` | Prospector's Saloon shelter |
| SheltersLocation_WranglerCasino | `0x0085258A` | Wrangler Casino shelter |
| DELETED_COMP_QuestNameOverride_Beckett_012-014 | various | Beckett companion quest locations |
| Burn_BountyTargetNameOverride_OldManBreeches | `0x007CFA61` | Old Man Breeches bounty target |
| Burn_BountyTargetNameOverride_OldLadyPam | `0x007CFA60` | Old Lady Pam bounty target |
| E09_NukaWorld_SnakeBoss_Static | `0x006355A9` | Snake Boss for Nuka-World on Tour |
| RaiderCave01 / RaiderCave03 | `0x005AFB11/5B59C8` | Two raider cave interiors (dev build only) |

### 5B. Key Observations About Locations

The Burning Springs (Backwoods) region has 15+ POI locations defined with descriptive names. Many of these shipped in the final Burning Springs update, including Albany, Cornhenge (which went through 4 design iterations before the final version), and Sock Hop. The zzz-prefixed location records represent earlier iterations that were superseded, not necessarily cut content.

Two shelter locations (Prospector's Saloon, Wrangler Casino) and a Nuclear Test Bunker shelter were designed but never released.

---

## Part 6: Cut World Objects and CAMP Items

### 6A. Cut CAMP/Workshop Items

| Object | Type | Form ID | Description |
|--------|------|---------|-------------|
| ATX_Raider_Metal_Brazier01/02/03 | STAT | various | Three raider brazier variants |
| ATX_WorkshopCollector_Enclave series | CONT | various | 9 Enclave-themed mineral extractors (Aluminum, Copper, Crystal, Gold, Lead, Nuclear, Silver, Steel, Titanium) |
| E09_NukaWorld_SnakeBoss_Static | STAT | `0x006355A9` | Snake Boss statue |
| FasnachtBeerStein | STAT | `0x005A728C` | Fasnacht beer stein decorative |
| TrafficLight_Mounted_Pitt_CAMP | ACTI | `0x0065A404` | Pitt traffic light CAMP item |
| ZZZ_ATX_FloorDecor_FiveFingerFiletTable | ACTI | `0x007B288C` | Five Finger Fillet game table |
| zzz_ATX_FloorDecor_SummoningCircle | ACTI | `0x007B2842` | Summoning circle floor decoration |
| zzz_Invaders_AlienWhackAMole | ACTI | `0x0075FBFD` | Alien Whack-a-Mole game (SHIPPED as Season 7 scoreboard reward) |
| zzz_Fishing_workshop_FishTank01 | ACTI | `0x0083A31D` | Fish tank |
| zzz_StarLight01 | ACTI | `0x0072DB1E` | Star light decoration |
| ATX_Pennant_ThePitt_Framed/NoFrame | STAT | various | Pitt pennants (framed and unframed) |
| zzz_ATX_Utility_BeerMysteryMachine | ACTI | `0x00773E16` | Beer Mystery Machine (Scooby-Doo reference?) |
| ZZZ_SCORE_S24_FloorDecor_WaxGuinevere | ACTI | `0x008A5DFE` | Wax Guinevere figure |
| ZZZ_SCORE_S22_MistressofMysteriesWaxFigure | ACTI | `0x0082E151` | Mistress of Mysteries wax figure |
| ZZZ_SCORE_S19_DisplayCase_StasisChamber | ACTI | `0x0079B5D5` | Stasis chamber display |
| ZZZ_SCORE_S20_Fortune_Telling_Machine_Broken | ACTI | `0x007AE529` | Broken fortune telling machine |
| ZZZ_SCORE_S20_Weather_WeatherStation_Radstorm | ACTI | `0x007ADC9B` | Radstorm weather station |

### 6B. Cut Vault Raid Music

Three combat music tracks for Vault Raids still exist:
- MUS76CombatBossVaultRaidsM01 (`0x0041F362`)
- MUS76CombatBossVaultRaidsM02 (`0x0041F363`)
- MUS76CombatBossVaultRaidsM03 (`0x0041F364`)

### 6C. Cut Test Radio Music

- test_MUSzRadioTestEnclaveBattleHymn (`0x0001FA5D`)
- test_MUSzRadioTestRoyBrownButcherPete (`0x0001FA5E`)

---

## Part 7: Most Significant Discoveries

### Tier 1: Major Cut Content

1. **Vault Raid System (20+ quests)** -- Three vaults (63, 94, 96) each had complete multi-mission quest lines with unique mechanics (GECK recovery, genetics preservation, nuclear reactor management, riot suppression). The "Lockdown" meta-quest (`CUT_FF15_Lockdown`) connected all three vaults through an Overseer key conspiracy. Hayley's corpse held the truth.

2. **"The Glow" Public Event** (`SFM01_Glow_CUT`) -- A radstorm emergency event involving dam infrastructure, chemical collection, and a Mirelurk Queen boss fight. Would have been one of the largest public events in the game.

3. **Treehouse Village** (`CUT_W05_Community_Treehouse_Village_Quest`) -- An entire settlement location with infrastructure quests, NPC settlers, and player choice (power vs alarm systems). Never placed in the world.

4. **Beckett's Original Ending** (`DELETED_COMP_Quest_Outtro_Full_Beckett`) -- Set at Poseidon Energy Plant with a jailbreak sequence and a meaningful choice about the Blood Eagles' fate.

5. **Rotating Scorchbeast Queen** (`CUT_SFZ03_Queen_MasterQuest`) -- 5 normal boss + 4 cryptid boss locations for a rotating boss system instead of the current static fissure spawn.

### Tier 2: Notable Cut Features

6. **Gorilla Creature** -- Dialogue system proves gorillas were designed for the game
7. **Cat Pet System** -- 5 full IDLE animations for pet cats
8. **Needle SMG** -- Entirely new weapon class
9. **Tempest Armor Set** -- Complete 6-piece armor set
10. **Vault 65 and Vault 120** -- Two unannounced vaults with cell data
11. **Huntersville Sewers** -- Cut dungeon beneath an existing location
12. **Mole Miner City** -- Underground mole miner settlement
13. **Secret Research Laboratory** -- Unnamed cut interior
14. **GHL Disguise System** -- 12+ disguise outfits for a ghoul infiltration quest
15. **22 Cut Legendary Effects** -- Including Barbarian, Headhunters, Daredevils, Elemental, and more
16. **7 Foundation Daily Quests** -- Painting, clinic, stew, fieldhand, restock, secret (note: Elsie and Davie Taylor are live NPCs; only these specific daily quest variants were cut)
17. **Vald's Diary** -- 7 entries spanning 28 years of post-war survival (2077-2105)

### Tier 3: Curiosities

18. **Baseball Announcer Event** (`zzz_TWZ09`) -- Grafton farm event with sports commentary
19. **Assaultron Cooking Companion** -- Random encounter with a cooking robot
20. **Albino Yao Guai + Deathclaw** -- Dual albino creature encounter
21. **Boss Chicken** -- A leveled boss chicken exists in the data
22. **Ogua Creature** -- Unknown cryptid for Burning Springs
23. **Bigfoot Herdsman's Bell** -- Bigfoot-themed CAMP item
24. **Five Finger Fillet Table** -- RDR2-style minigame furniture
25. **Summoning Circle** -- Occult floor decoration
26. **Alien Whack-a-Mole** -- Shipped as Season 7 scoreboard reward (zzz_ prefix is from an earlier iteration)

---

## Data Totals

| Category | Count |
|----------|-------|
| Cut/Deleted Quests | 99 |
| Cut Quest Scenes/Branches | 25+ |
| Debug/Test Cells | 120+ |
| Holding Cells | 9 |
| Warehouse Test Cells | 17 |
| Cut Named Locations | 40+ |
| Cut NPCs | 208 |
| Cut Weapons | 18+ |
| Cut Armor/Clothing | 30+ |
| Cut Notes/Holotapes | 25+ |
| Cut Misc Items | 40+ |
| Cut Legendary Effects | 22 |
| Cut CAMP Items | 20+ |
| Cut Creatures | 15+ |
