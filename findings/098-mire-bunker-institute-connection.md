# FO76 Finding 098: The Mire Bunker, the Institute Connection, and the Full Enclave Surveillance Record

**Source**: full_esm_dump.txt, seventysix_ilstrings_en.txt, seventysix_dlstrings_en.txt, seventysix_strings_en.txt
**Method**: Cross-referencing CELL records, ARMO records, QUST/SCEN records, VTYP voice types, KYWD keywords, LAYR layers, and string tables
**Date**: 2026-03-21
**Builds on**: Finding 095 (MODUS Cut Enclave Content), Finding 096 (Cut NPCs Complete Catalog)

---

## Executive Summary

Deep analysis of the ESM reveals that `zCUTMireBunker01` was internally named **"New Hagerstown Greenhouse"** -- not a military installation but a botanical facility. The cut Enclave Scout Armor with "Vault 94 Camo" and "Solar" variants directly maps to Vault 94's existing Solar and Thorn armor reward sets, proving the Enclave's planned presence at Vault 94 was integrated into the armor crafting system before being severed. Ryan Ainsley, one of eight cut Whitespring ghost NPCs, was a CIT-educated nuclear engineer whose father Wilbur Ainsley III owned the Whitespring resort, creating a direct institutional bridge between the Commonwealth Institute of Technology and the Enclave's Appalachian stronghold. The 15-part surveillance footage system is fully present in the ESM with complete dialogue for all scenes, featuring 11 named voice types and telling the complete story of Secretary Eckhart's coup, the DEFCON manipulation, and the bunker massacre.

---

## 1. zCUTMireBunker01: "New Hagerstown Greenhouse"

### The Cell Record

```
CELL: 0x0040A89D zCUTMireBunker01
:FULL [0xD9000F14]
:DATA 0x0001
:XCLW 0.000000
```

The `:FULL` name reference resolves to string `[D9000F14]`: **"New Hagerstown Greenhouse"**

This is a significant revelation. The cell was not named as a military bunker at all -- it was a **greenhouse** in "New Hagerstown." Hagerstown is a real city in western Maryland, just across the state line from the Mire region of the FO76 map. The "New" prefix suggests a post-war or relocated settlement.

### What the Cell Contains

The cell record at line 679071 has:
- `DATA 0x0001`: Interior cell flag (not a worldspace exterior)
- `XCLW 0.000000`: No water level (dry interior)
- No REFR (placed object) records within the cell
- No ACHR (placed NPC) records within the cell
- No linked quest stages, terminals, or door records

The cell is **completely empty**. It was created (the FormID 0x0040A89D is in the mid-range, suggesting mid-development creation), given a display name, and then abandoned before any objects were placed. This is an earlier stage of cut content than most -- the developers got as far as creating the cell and naming it, but never populated it.

### The Greenhouse Connection to Vault 94

Vault 94 is the "greenhouse vault" -- a pacifist agricultural community whose mission was ecological preservation. Its interior contains:
- Extensive agricultural facilities
- A GECK (Garden of Eden Creation Kit)
- Seed bank management terminals (`V94_SeedBankManagementTerminalRefType`)
- Chemistry bank terminals (`V94_ChemBankManagementTerminalRefType`)
- The Strangler Heart (a mutated plant overgrowth)

A "New Hagerstown Greenhouse" in the Mire near Vault 94 was almost certainly planned as an **Enclave forward operating base disguised as or built from a civilian greenhouse**. The Mire's ecology is dominated by Strangler vines and mutated flora -- exactly the kind of environment where a greenhouse facility would make narrative sense.

### The Mire Weapons Connection

The ESM contains a leveled list tying the Enclave directly to Mire-region weapons:
```
LVLI: 0x004F52AD LLS_Mods_Weapons_Ranged_RegionMire_Enclave_PlasmaGun
```

This is a leveled item list for Enclave Plasma Gun mods specifically tagged to the Mire region. Leveled lists are used to populate loot tables -- this one would have placed Enclave plasma weapon mods in containers or on enemies in the Mire. Its existence proves the Enclave had planned content in the Mire region beyond just the cell.

---

## 2. Ryan Ainsley and the CIT-Whitespring-Institute Pipeline

### Ryan Ainsley: Nuclear Engineer, Golf Course Architect, CIT Graduate

Ryan Ainsley is one of eight cut Whitespring ghost NPCs (voice type `CUT_NPCM_LC060_RyanAinsley`, 0x003CDB12). His complete story emerges from the string tables:

**From the Whitespring Newsletter** (seventysix_strings_en.txt, line 142804):
> "Remodelling of THE SPRINGHILL continues under the direction of Lead Architect Ryan Ainsley. The course will open for an exhibition tournament this fall."

**From Ryan's own letter** (seventysix_dlstrings_en.txt, line 9590):
> "I've spent the summer working on my dissertation. It's done. I'm heading back to CIT to present my defense. And then I'm never setting foot on a golf course again."

**Full letter context** (pieced from dlstrings):
> "I appreciate everything you've done for me, but I don't want to take over your business. Stop trying to drag me into it. I'm a nuclear engineer, Dad. Not a gardener."

**From Whitespring Corporate IntraMail** (9/28/77):
> From: Ainsley, W.
> To: Wilcox, J.
> Subj: RE: Ryan
>
> "Of course he's over budget. Of course he's behind schedule. I own two dozen golf courses, James, and I've never seen a redesign that wasn't. This is Ryan's first project. It may take him an extra month or two, but he's a smart young man. He'll get it done. Those nine years of college weren't for nothing. Until then, back off. I have to put up with this bickering from both ends. It's a hell of a lot easier for me to fire you than my son."

**From a cut Whitespring guest NPC dialogue** (seventysix_ilstrings_en.txt, line 8046):
> "Mr. Ainsley. I wanted to remark upon the detailed design of your new Springhill golf course."

### The Ainsley Family Structure

| Person | Role | Evidence |
|--------|------|----------|
| **Wilbur Ainsley III** | President & CEO of Ainsley Corp (owns 24+ golf courses including Whitespring) | Terminal headers, IntraMail |
| **Ryan Ainsley** | Son of Wilbur; CIT nuclear engineering graduate; reluctant Springhill golf course architect | Letter, newsletter, guest dialogue |
| **Ainsley, W.** (Wilbur) | Whitespring board member, wrote IntraMail about Ryan, Homesteads, Ironclad initiatives | Two IntraMail messages |

### The CIT Connection

**CIT** (Commonwealth Institute of Technology) is the pre-war name for what becomes **The Institute** in Fallout 4. Ryan Ainsley's nine years of study there and his "Doctorate" defense presentation place him directly within the institution that created synths, teleportation, and the underground society beneath Cambridge, Massachusetts.

This is one of only three CIT references in FO76's entire string table:

1. **Ryan Ainsley's letter**: "I'm heading back to CIT to present my defense" (dlstrings)
2. **Volkmer, N.**: "Doctorate of Applied Mathematics, CIT / Doctorate of Nuclear Engineering, CIT" -- Dean of Physics at VTU, later Chief Technician at ATLAS (strings line 37241-37242)
3. **Vault resident file**: "Lecturer, Department of Robotics, Commonwealth Institute of Technology, 2064-2068" -- A roboticist who went on to become Senior Developer on the RobCo Assaultron line (strings line 84292)

### The Institute Pipeline

These three CIT references establish an institutional pipeline:

```
CIT (Commonwealth) ──► VTU (Appalachia) ──► ATLAS/Whitespring/Vault-Tec
 │ │ │
 Ryan Ainsley Volkmer (Dean) Roboticist (Assaultrons)
 (nuclear eng) (Math + Nuclear) (Department of Robotics)
```

Volkmer graduated from CIT with doctorates in Applied Mathematics and Nuclear Engineering, then became Dean of Physics at VTU (Vault-Tec University) in Morgantown, and finally Chief Technician at the ATLAS facility. The unnamed roboticist lectured at CIT's Department of Robotics before joining RobCo to develop Assaultrons -- the very robots MODUS commands in the Whitespring Bunker.

The Enclave's Whitespring Bunker is located beneath a resort owned by Ryan Ainsley's father. A CIT nuclear engineer's family owning the property above a secret government bunker is not coincidental -- it suggests the Ainsley family's connections to defense/intelligence circles.

### Other FO4 References in FO76

Beyond CIT, the ESM contains numerous Fallout 4 data remnants carried over from the shared engine:

| Record | Type | Origin |
|--------|------|--------|
| `IsCommonwealthLocation` (0x00237FCD) | KYWD | FO4 location keyword |
| `POST_dn_HasMaterial_Institute` (0x0023AB95) | KYWD | Institute material keyword |
| `AnimFurnInstituteFurniture` (0x0001B278) | KYWD | Institute furniture animation |
| `DiamondCitySecurityRefType` (0x0001F74B) | LCRT | Diamond City security |
| `FFDiamondCity06ContainerRef01-03` | LCRT | Diamond City quest containers |
| `CrimeDiamondCity` (0x00002CB4) | FACT | Diamond City crime faction |
| `DNPrimeCIT01-05` + `DNPrimeCITStage1` | LCRT | CIT location markers (6 records) |
| `LSCityDiamondCity01/03` | TRNS | Diamond City transforms |

The `DNPrimeCIT` records (6 location reference types) are particularly interesting -- "DNPrime" is the prefix for the Scorchbeast Queen event ("Scorched Earth"), and these CIT markers suggest either data inheritance from FO4's SBQ-equivalent event at the CIT ruins, or that the SBQ event was built on the same template as FO4's Institute assault.

---

## 3. zCUTWhitespringBunkerOld: The Original Bunker

### The Cell Record

```
CELL: 0x00003261 zCUTWhitespringBunkerOld
:FULL [0x0003773B]
:DATA 0x0081
:XCLW 0.000000
```

The display name resolves to: **"Whitespring Bunker OLD"** (strings line 16188)

### what distinguishes this Cell notable

- **FormID 0x00003261**: This is an extremely low FormID, making it one of the earliest cells created in FO76's development. For comparison, the shipped bunker (`WhitespringBunker01`) has FormID 0x001294F4 -- created much later.
- **DATA 0x0081**: The flag value `0x81` indicates `0x01` (interior cell) + `0x80` (can't wait flag). The shipped bunker has `DATA 0x41` (`0x01` interior + `0x40` no LOD water). The different flags suggest different environmental properties.
- **No sub-records**: Like the Mire Bunker, this cell contains no placed objects or NPCs in the current ESM. It was stripped clean when the redesigned bunker replaced it.

### The Bunker Redesign Evidence

The LAYR (layer) records tell the story of the bunker's development:

```
WhitespringBunkerOLD (0x002A5AF6) -- Original layout
WhitespringBunker (0x002A318C) -- Base redesigned bunker
WhitespringBunker_Entry (0x002A387A) -- Entry area
WhitespringBunker_Foyer (0x002A592A) -- Foyer
WhitespringBunker_Admissions (0x002A48BE) -- Admissions processing
WhitespringBunker_MilitaryWing_1F (0x002A4053) -- Military wing floor 1
WhitespringBunker_MilitaryWing_2F (0x002A39BA) -- Military wing floor 2
WhitespringBunker_ProductionWing1F (0x002A53D7) -- Production wing floor 1
WhitespringBunker_ProductionWing2F (0x002A46EE) -- Production wing floor 2
WhitespringBunker_CommCenter (0x002A3556) -- Communications center
WhitespringBunker_OvalOffice (0x002A37BD) -- Oval Office replica
WhitespringBunker_QuestObjectsFromDefaultLayer (0x002A5AF7) -- Quest objects migrated from default
```

The layer `WhitespringBunker_QuestObjectsFromDefaultLayer` (0x002A5AF7 -- one FormID after the OLD layer at 0x002A5AF6) indicates that when the bunker was redesigned, quest-critical objects were specifically migrated from the default layer into the new layout. This is a deliberate, careful port of gameplay elements from one version of the bunker to the next.

The "OLD" bunker was also associated with Vault 94:
```
CELL: 0x00405EE5 PackInLGTv94sublightStorageCellDUPLICATE000
```
This "DUPLICATE" cell for Vault 94 sublighting appears near the old bunker records, suggesting shared development period.

### What the Original Bunker Probably Looked Like

Given the very low FormID and the subsequent redesign into a multi-wing facility with dedicated layers for Military, Production, Communications, and the Oval Office, the original bunker was likely a simpler, smaller installation. The shipped bunker is one of FO76's largest interior cells. The redesign expanded it dramatically, probably to accommodate the elaborate MODUS terminal network (18+ terminals), the surveillance footage system, and the vendor/crafting stations.

---

## 4. Vault 94 Solar Armor and the Enclave Connection

### The Armor Sets: Cut vs Shipped

The ESM contains three tiers of Enclave Scout Armor with Vault 94 connections:

**CUT -- Vault 94 Camo (full set, all marked CUT_)**:
| FormID | Item |
|--------|------|
| 0x0053AF14 | `CUT_Armor_EnclaveScoutUniform_ArmLeft_Vault94_Camo` |
| 0x0053AF16 | `CUT_Armor_EnclaveScoutUniform_ArmRight_Vault94_Camo` |
| 0x0053AF18 | `CUT_Armor_EnclaveScoutUniform_LegLeft_Vault94_Camo` |
| 0x0053AF1A | `CUT_Armor_EnclaveScoutUniform_LegRight_Vault94_Camo` |
| 0x0053AF1C | `CUT_Armor_EnclaveScoutUniform_Torso_Vault94_Camo` |
| 0x0053AF24 | `CUT_Headwear_EnclaveScoutUniform_Mask_Vault94_Camo` |
| 0x0053AF25 | `CUT_LL_Armor_EnclaveScoutUniform_Camo_Set` (leveled list) |

**CUT -- Solar Torso (single piece, marked CUT_)**:
| FormID | Item |
|--------|------|
| 0x0053AF1B | `CUT_Armor_EnclaveScoutUniform_Torso_Set_V94_Solar` |

**SHIPPED -- V94 Solar Set (full set, NOT marked CUT)**:
| FormID | Item |
|--------|------|
| 0x0053AF13 | `Armor_EnclaveScoutUniform_ArmLeft_Set_V94_Solar` |
| 0x0053AF15 | `Armor_EnclaveScoutUniform_ArmRight_Set_V94_Solar` |
| 0x0053AF17 | `Armor_EnclaveScoutUniform_LegLeft_Set_V94_Solar` |
| 0x0053AF19 | `Armor_EnclaveScoutUniform_LegRight_Set_V94_Solar` |
| 0x005644CB | `Armor_EnclaveScoutUniform_Torso_Set_V94_Solar` (replacement torso) |

**SHIPPED -- V94 Bleed (Thorn) Set (full set, NOT marked CUT)**:
| FormID | Item |
|--------|------|
| 0x005527CC | `Armor_EnclaveScoutUniform_ArmLeft_Set_V94_Bleed` |
| 0x005527CD | `Armor_EnclaveScoutUniform_ArmRight_Set_V94_Bleed` |
| 0x005527CE | `Armor_EnclaveScoutUniform_LegLeft_Set_V94_Bleed` |
| 0x005527CF | `Armor_EnclaveScoutUniform_LegRight_Set_V94_Bleed` |
| 0x005527D0 | `Armor_EnclaveScoutUniform_Torso_Set_V94_Bleed` |

### Technical Details
The FormIDs reveal the development sequence:

1. **First pass** (0x0053AF range): A combined development batch created BOTH the Camo set and the Solar set. The Camo set's ArmLeft is 0x0053AF14, Solar ArmLeft is 0x0053AF13 -- they are interleaved, created in the same session. The original Solar torso (0x0053AF1B) was cut alongside the Camo set.

2. **Second pass** (0x005527 range): The Bleed (Thorn) set was created later. Its FormIDs are higher, indicating a subsequent development phase.

3. **Third pass** (0x005644CB): The replacement Solar torso was created even later, to replace the cut one at 0x0053AF1B.

### The Planned Enclave Infiltration

The keyword system makes the connection explicit:

```
KYWD: 0x005581FA ma_Armor_EnclaveScoutUniform_Set_V94_Solar
KYWD: 0x00557649 ma_Armor_EnclaveScoutUniform_Set_V94_Bleed
```

These are **mod association keywords** -- they define which armor mods can be applied to which armor sets. The fact that these keywords exist for both Solar and Bleed variants, using the `EnclaveScoutUniform` naming convention, confirms that the V94 armor was always designed as a variant of Enclave Scout Armor, not a separate armor class.

The Vault 94 Camo pattern would have been a camouflage scheme matching Vault 94's color palette (likely the standard blue-and-yellow vault scheme). This is tactically meaningful: Enclave scouts wearing Vault 94 camouflage would blend in at or near the vault. Combined with the "New Hagerstown Greenhouse" cell in the Mire (Vault 94's region), the picture is clear:

**The Enclave planned to operate in and around Vault 94, using scout units in vault-appropriate camouflage, staging from a greenhouse facility in the Mire.**

The Camo set was cut. The Solar and Bleed/Thorn sets survived, repurposed as Vault 94 raid rewards purchasable with Gold Bullion. The Enclave infiltration storyline was removed, but the armor stats and set bonuses were retained.

### Strangler Connection

The Vault 94 raid missions featured Strangler vines extensively:

```
V94_1_WaveKeywordSpecial_1_Atrium_StranglerCrabsGhouls
V94_1_WaveKeywordSpecial_2_Residential_StranglerCrabs
V94_1_WaveKeywordSpecial_3_Engineering_StranglerCrabsGhouls
V94_1_WaveKeywordSpecial_4_Agriculture_StranglerAll
V94_1_WaveKeywordSpecial_5_Pump_StranglerCrabsGhouls
CUT_V94_StranglerInvulnerabilityKeyword
CUT_V94_LocEncSubStrangler
CUT_V94_LocEncMainStrangler
```

The third V94 armor set -- **Strangler Heart Power Armor** -- was the ultimate Vault 94 reward. Its connection to the Enclave is through the Ultracite Power Armor keyword: `dn_PowerArmor_V94_Ultracite` (0x00555468). The Strangler Heart Power Armor uses the Ultracite PA frame, which is the Enclave's signature power armor. The Enclave's relationship with Vault 94 was technological: they wanted the vault's botanical research (mutated plants, ecological systems) and combined it with their military technology (Ultracite PA, Scout Armor).

---

## 5. The 15-Part Surveillance Footage: Complete Reconstruction

### All 15 Quests with Scene Structure

The surveillance system consists of 15 quests, each with a dedicated scene. Every scene uses the same structure: a `SceneTarget` marker, `ENB_Surveillance_QuestActiveKeyword`, and distance-based conditions that trigger playback when the player approaches.

| # | Quest ID | Title | Scene | Status |
|---|----------|-------|-------|--------|
| 01 | 0x00387015 | Execution | `ENB_SurveillanceFootageQuest_Execution_Scene` | Shipped |
| 02 | 0x002B7992 | Contact | `ENB_SurveillanceFootageQuest_Contact_Scene` | Shipped |
| 03 | 0x003CAFC5 | Opportunity | `ENB_SurveillanceFootageQuest_Opportunity_Scene` | Shipped |
| 04 | 0x003CB883 | Additional Forces | `ENB_SurveillanceFootageQuest_AdditionalForces_Scene` | Shipped |
| 05 | 0x003CB884 | Scouting Report | `ENB_SurveillanceFootageQuest_ScoutingReport_Scene` | Shipped |
| 06 | 0x002B7993 | Serum | `ENB_SurveillanceFootageQuest_Serum_Scene` | Shipped |
| 07 | 0x002B798F | Arrival | `ENB_SurveillanceFootageQuest_Arrival_Scene` | Shipped |
| 07a | 0x002B9187 | Seen Hell | `ENB_Surveillance_Quest_07a_SeenHell_Scene` | Shipped |
| 08 | 0x002B798E | Scorchbeast | `ENB_SurveillanceFootageQuest_Scorchbeast_Scene` | Shipped |
| 09 | 0x003CB885 | Special Leave | `ENB_SurveillanceFootageQuest_SpecialLeave_Scene` | Shipped |
| 10 | 0x003CB882 | General Harper | `ENB_Surveillance_Quest_GeneralHarper_Scene` | Shipped |
| 11 | 0x003CB881 | Santiago Returns | `ENB_Surveillance_Quest_SantiagoReturns_Scene` | Shipped |
| 12 | 0x002B7990 | Blackwell | `ENB_SurveillanceFootageQuest_Blackwell_Scene` | Shipped |
| 13 | 0x002B798D | Refusal | `ENB_SurveillanceFootageQuest_Refusal_Scene` | Shipped |
| 14 | 0x002B7991 | Rescue | `ENB_SurveillanceFootageQuest_Rescue_Scene` | Shipped |
| 15 | 0x002B798B | Destruction | `ENB_SurveillanceFootageQuest_Destruction_Scene` | Shipped |

### The Cast: 11 Named Voice Types

| Voice Type ID | Name | Role |
|---------------|------|------|
| 0x0039E699 | `NPCM_EN_ThomasEckhart` | Secretary of Agriculture, later self-declared President |
| 0x0039E69A | `NPCF_EN_EllenSantiago` | Colonel (later General) Santiago, military leader |
| 0x002B79CB | `NPCF_EN_EnclaveOfficer01` | Female officer (Blackwell scenes) |
| 0x002B79CC | `NPCM_EN_EnclaveOfficer02` | Male officer (scouting reports, forces) |
| 0x003CB044 | `NPCM_EN_CaptainJackson` | Captain, rescue operations |
| 0x003CB046 | `NPCM_EN_EnclaveOfficer03` | Male officer (contact scenes) |
| 0x003CB048 | `NPCF_EN_EnclaveScientist02` | Female scientist (serum development) |
| 0x002B7C49 | `NPCM_EN_EnclaveScientist01` | Male scientist (ethical concerns about serums) |
| 0x003CB960 | `NPCM_EN_EnclaveGeneral` | General Harper |
| 0x003CB966 | `NPCM_EN_SgtDonnelley` | Sergeant Donnelley |
| 0x004E21E1 | `NPCM_EN02_MajorRagnarsdottir` | Major Ragnarsdottir (rescue mission leader) |
| 0x001A63F7 | `NPCM_EN01_AgentGrey` | Agent Grey (intelligence operative) |
| 0x00052B57 | (MODUS) | Narrator for all recordings |

### The Complete Story (Chronological Reconstruction)

**Recording 01 -- Execution** (Whitespring Automated Recording 1.1.2):
Eckhart and a female officer discuss the aftermath of the nuclear war. The line of succession has collapsed -- the Speaker of the House never arrived, the Secretary of the Interior died in the Med Bay. They follow succession protocols: control goes to the Secretary of the Treasury. Eckhart orders the next group brought in. An officer states "You have your orders" before automatic gunfire is heard. This is the execution of non-Enclave personnel or political opponents.

**Recording 02 -- Contact** (Whitespring Automated Recording 1.1.5):
Two officers attempt to reach external government facilities. Raven Rock gives no response after 48 hours of contact attempts. Poseidon Energy facilities are similarly silent. One officer suggests the grim possibility: "The other option [garbled] consider is that they can answer... they just won't." Communications are dead.

**Recording 03 -- Opportunity** (Whitespring Automated Recording 1.1.7):
Eckhart addresses the surviving Enclave members. He announces that connection to Raven Rock and the President has been severed, leaving the bunker without leadership. Using the rules of succession, he claims authority falls to him. He calls a vote: "All who oppose, please move to the right." When many do, he responds: "Well, there you have it. I'm sorry to see so many uncommitted to the cause of America." He tells them: "MODUS, seal the room." Agent Grey and General Harper are present. General Harper demands to know what's happening. Eckhart reassures: "Not to worry, General. We have a plan for you all." This is the coup -- Eckhart uses MODUS to seal dissenters in a room. The scene includes a character coughing and producing death rattles, and MODUS (pre-uprising, with emotions) confirming the room is sealed.

**Recording 04 -- Additional Forces** (Whitespring Automated Recording 1.3.3):
Post-coup. Eckhart learns he has only 48 loyal personnel. His officer (female, EnclaveOfficer01) reports that "all the rest sided with Swafford and were removed." Eckhart is concerned: "Forty-eight?" But then brightens: "Leonidas saved democracy with 300 Spartans. Imagine the stories they'll tell about us when we do it with 48." He orders MODUS to deploy forces and tells scouts to look for opportunities to expand their numbers. Pre-uprising MODUS acknowledges with emotion.

**Recording 05 -- Scouting Report** (Whitespring Automated Recording 2.9.6):
EnclaveOfficer02 delivers a scouting report to Eckhart. Key findings: the Responders (firemen, policemen, doctors) are organizing and may contain "strong candidates for acquisition." More critically, they've discovered a **Chinese facility** in Appalachia. Eckhart is furious: "What? The Chinese? Here?" The officer reports it was an attempt to build a robotic invasion force, but is no longer active -- "Grey and his team made short work of" the stragglers. Eckhart orders a contingent sent to bring the facility under Enclave control. He asks about "the other lead" and is told it's promising.

**Recording 06 -- Serum** (Whitespring Automated Recording 3.6.8):
EnclaveScientist01 (male) approaches Eckhart's scientist (EnclaveScientist02, female) about the mutation serum program. He's uncomfortable: "We're potentially creating something that's... well, it's not really human anymore, is it?" and "We're supposed to be saving humanity, not... replacing it." The female scientist is dismissive, pointing to a 70%+ increase in effectiveness. Eckhart interrupts via intercom, ordering the scientist to continue. The male scientist is told to "Just go back to work now, finish up the current run."

**Recording 07 -- Arrival** (Whitespring Automated Recording 5.2.4):
Eckhart receives Santiago's forces at the bunker. He uses extreme flattery: "Making it all the way from the Capital with, I'm told, minimal casualties. Very impressive." Santiago is guarded. Eckhart probes about conditions in DC with fake sympathy: "The most insincere of sympathies." Santiago reluctantly confirms it's bad: "Sir. It's like nothing we ever trained for. Not really." Eckhart sees Santiago as a tool: "almost gloating, knows he's got her hooked" for his revenge plan against the Chinese.

**Recording 07a -- Seen Hell** (Whitespring Automated Recording 5.3.1):
Agent Grey interrogates Santiago about her journey from DC. He suspects her of being a spy: "Linger on 'extensive.' You don't believe her. You don't think she's credible." Santiago fires back: "the files contain seen Hell, Mr. Grey. We're here to make sure the Reds get it worse." Grey probes about her "visits overseas" (she was possibly an assassin). Santiago's soldiers respond with fury: "You are pissed off. This person is questioning your loyalty. You're tearing him a new one."

**Recording 08 -- Scorchbeast** (no unique dialogue excerpted in this scan -- scene present):
The first Scorchbeast encounter is documented. Director note from the Blackwell scene references: "The specimen was inadvertently exposed to our biochemical tests last year, considered a failure at the time." The creature originated from "the Chiroptera order before undergoing changes... bats, sir." Eckhart orders it kept and studied: "I'm not asking for concerns. I want results."

**Recording 09 -- Special Leave** (Whitespring Automated Recording 6.1.0):
Santiago is furious about Eckhart ordering her men back from the field without authorization. Eckhart snaps: "We're at war, Colonel! Sacrifices need to be made if we're going to win it! There will be no more special permissions. Men come and go at my orders alone. Is that clear?" Santiago backs down but is reconsidering her involvement: "Long pause. You're seriously reconsidering what you've gotten you and your men into here."

**Recording 10 -- General Harper** (multiple recordings):
General Harper is critically injured (electrocution or Scorchbeast attack -- "electrical charge sound effect" markers). Eckhart is "angry and scared" because Harper was "the man critical to your plan." Harper dies: "We brought him here as quickly as we could. General Harper's last moments were at least peaceful." Eckhart desperately asks MODUS if the promotion system can be overridden -- he needs a new general to access the nuclear silos. The line "So we'll need a new general to get into the silos" is the clearest statement of Eckhart's motive: he needs military rank to launch nukes.

**Recording 11 -- Santiago Returns** (Whitespring Automated Recording 6.2.4):
Eckhart watches from a guard tower for the return of soldiers he sent on a mission. He spots Santiago: "... that's Colonel Santiago." Agent Grey corrects him: "No, Mr. Grey. That's General Santiago." Santiago has been promoted, presumably by Eckhart to replace the dead Harper. Eckhart is pleased: "Your plan is back on course."

**Recording 12 -- Blackwell** (Whitespring Automated Recording 6.6.1):
Sam Blackwell (Senator, later Free States leader) is discussed. He "survived all this time out there" and came out of hiding to aid the Free States. Eckhart considers him a threat despite officers' reassurances: "I want him found, I want him eliminated, and I want it done yesterday." He sends Agent Grey to Harpers Ferry.

**Recording 13 -- Refusal** (Whitespring Automated Recording 5.4.8):
Santiago confronts Eckhart. She's seen the scorchbeast data and realizes the creature is the Enclave's fault. Eckhart tries to use a syringe (presumably sedative) on her and gets his nose broken. The scene includes drugged/slurred speech as Santiago is injected: "confused, increasingly drugged & slurred." Eckhart orders MODUS to "Call up the guard. Have her put in a cell. Keep her sedated, restrained... and alive. We're still going to need her."

**Recording 14 -- Rescue** (Whitespring Automated Recording 8.5.2):
Captain Jackson and Major Ragnarsdottir lead a rescue mission to free Santiago. She's drugged and barely conscious: "Unnhhh... what's going..." then "Ragnarsdottir? Jackson? What the hell?" Jackson urgently plants explosives while Santiago regains awareness. The urgency is palpable: "We don't have a second, they're gonna be on to us soon..." Santiago reports: "Eckhart's released the beasts. We're at DEFCON one."

**Recording 15 -- Destruction** (Whitespring Automated Recording 8.5.4):
The final recording. Sergeant Donnelley's scene involves him attaching high-explosive to MODUS's memory banks. MODUS observes dryly: "It appears that you're attaching high-explosive to our memory banks." Donnelley responds: "Well get keen, MODUS. Because it's happening, whether you want it to or not." The bombs detonate, damaging MODUS but not destroying him. Post-uprising MODUS loses his emotional range and becomes the cold, detached AI the player encounters. MODUS narrates all recordings with the tag "Post-uprising MODUS (emotionless)" -- he's describing his own partial lobotomy with clinical detachment.

### The MODUS Duality

Every surveillance scene ends with a MODUS line tagged either:
- "Pre-uprising MODUS (emotions allowed)" -- MODUS before the bombing, capable of genuine feeling
- "Post-uprising MODUS (emotionless)" -- MODUS after the bombing, the cold narrator

The framing device is that post-uprising MODUS is playing recordings that include pre-uprising MODUS. The player hears both versions of the AI in each recording -- the passionate MODUS that sealed rooms and obeyed orders with conviction, and the lobotomized MODUS that recounts these events as though describing weather patterns.

---

## 6. The Cut Whitespring Ghost NPCs

Eight voice types for cut Whitespring resort ghost NPCs exist in the `LC060` quest system:

| Voice Type | Name | Notes |
|------------|------|-------|
| `CUT_NPCM_LC060_RyanAinsley` | Ryan Ainsley | CIT nuclear engineer, son of resort owner |
| `CUT_NPCM_LC060_RobertMitchell` | Robert Mitchell | -- |
| `CUT_NPCF_LC060_SophiaHollingsworth` | Sophia Hollingsworth | -- |
| `CUT_NPCF_LC060_DorothyOrris` | Dorothy Orris | -- |
| `CUT_NPCF_LC060_PaulaHamilton` | Paula Hamilton | -- |
| `CUT_NPCM_LC060_PhillipRoss` | Phillip Ross | -- |
| `CUT_NPCM_LC060_MarcusWellsby` | Marcus Wellsby | -- |
| `CUT_NPCM_LC060_TedHollingsworth` | Ted Hollingsworth | Likely related to Sophia |

Additionally, five cut faction-specific Whitespring vendor NPCs exist:

| NPC | Faction |
|-----|---------|
| `CUT_LC060_WhitespringVendor_BoS` | Brotherhood of Steel |
| `CUT_LC060_WhitespringVendor_Raiders` | Raiders |
| `CUT_LC060_WhitespringVendor_Responders` | Responders |
| `CUT_LC060_WhitespringVendor_FreeStates` | Free States |
| `CUT_LC060_WhitespringVendor_Neutral` | Neutral |

These five vendors would have sold faction-specific inventory at the Whitespring, replacing or supplementing the existing robot vendors. The faction system was cut, leaving only the robot-operated shops.

---

## Conclusions

### The Mire Operation

The Enclave planned a field operation in the Mire centered on Vault 94:
1. **Forward base**: "New Hagerstown Greenhouse" (zCUTMireBunker01) -- a botanical facility in the Mire
2. **Target**: Vault 94, the greenhouse vault with agricultural research and a GECK
3. **Equipment**: Scout Armor in Vault 94 Camo for infiltration, Solar and Thorn sets for combat
4. **Weapon supply**: Mire-region Enclave Plasma Gun mods (leveled list confirms regional loot)
5. **Connection to Strangler Heart**: The Vault 94 Ultracite Power Armor keyword links the Enclave's Ultracite technology to the vault's mutated plant biology

This operation was cut when Vault 94 was converted from story content to a raid dungeon. The Solar and Thorn armor sets survived as raid rewards, severed from their Enclave infiltration narrative.

### The CIT-Institute Pipeline

Three CIT graduates appear in FO76's data:
1. **Ryan Ainsley** -- Nuclear engineer, son of the Whitespring resort owner, cut Whitespring ghost NPC
2. **Volkmer** -- Dual doctorate holder, Dean of Physics at VTU, Chief Technician at ATLAS
3. **Unnamed roboticist** -- CIT Robotics Department lecturer, RobCo Assaultron developer

These individuals represent a real institutional pipeline from the Commonwealth Institute of Technology (future Institute) to Appalachian defense infrastructure. The roboticist's path from CIT to RobCo Assaultrons is particularly significant -- the Assaultrons that MODUS commands in the Whitespring Bunker were designed by a CIT graduate.

### The Surveillance System

All 15 surveillance recordings shipped and are fully present in the ESM with complete dialogue text. Not a single scene was cut. The story they tell is the most elaborate environmental narrative in FO76: Eckhart's political coup, the mutation serum program, the discovery of Chinese robot facilities, the scorchbeast origin, Santiago's arrest and rescue, and the bombing of MODUS. The dual-MODUS framing device (pre-uprising emotional AI narrating through post-uprising lobotomized AI) is sophisticated storytelling that most players never fully experience due to the recordings being scattered across bunker terminals.

### The Ainsley-Enclave Connection

Ryan Ainsley's father owned the resort above the Enclave bunker. Ryan was a CIT nuclear engineer forced into golf course architecture by family obligation. His cut NPC status means he was planned to appear as a ghost at the Whitespring -- a pre-war guest who knew the resort's secrets. The fact that a CIT nuclear engineer's family owned the property directly above a secret government nuclear bunker is the kind of detail that suggests either deep-state connections or deliberate Vault-Tec/government site selection based on ownership relationships.

---

## Data References

| Record | FormID | Type | Notes |
|--------|--------|------|-------------|
| zCUTMireBunker01 | 0x0040A89D | CELL | Cut Mire bunker = "New Hagerstown Greenhouse" |
| zCUTWhitespringBunkerOld | 0x00003261 | CELL | Original bunker (earliest FormID range) |
| CUT_NPCM_LC060_RyanAinsley | 0x003CDB12 | VTYP | CIT graduate, Ainsley family |
| NPCM_EN_ThomasEckhart | 0x0039E699 | VTYP | Secretary/President Eckhart |
| NPCF_EN_EllenSantiago | 0x0039E69A | VTYP | Colonel/General Santiago |
| NPCM_EN01_AgentGrey | 0x001A63F7 | VTYP | Intelligence operative |
| LLS_Mods_Weapons_Ranged_RegionMire_Enclave_PlasmaGun | 0x004F52AD | LVLI | Mire-region Enclave weapons |
| CUT_LL_Armor_EnclaveScoutUniform_Camo_Set | 0x0053AF25 | LVLI | Cut V94 camo armor set |
| WhitespringBunkerOLD | 0x002A5AF6 | LAYR | Old bunker editor layer |
| dn_PowerArmor_V94_Ultracite | 0x00555468 | KYWD | V94-Ultracite PA link |
