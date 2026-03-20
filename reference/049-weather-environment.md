# Finding 049: Weather, Environment, and World Simulation System

**Source files:**
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/esm_dump/full_esm_dump.txt`
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/` (multiple scripts)
- `/var/home/deucebucket/ai-drive/gamecryptids/data/fallout76/tempest_data/misc/curvetables/json/misc/weather/`

---

## 1. Complete Weather Type Inventory (116 WTHR Records)

The ESM contains **116 weather definitions** (WTHR records). They break into the following categories:

### Base Appalachian Weather (Main World)
| FormID | EditorID | Keywords | Notes |
|--------|----------|----------|-------|
| `0x0000015E` | `DefaultWeather` | Clear | Engine fallback |
| `0x002DB88D` | `NewWeatherFoggy` | Fog | Standard fog |
| `0x002DB88E` | `NewWeatherMisty` | Mist | Light haze |
| `0x002DB88F` | `NewWeatherMistyRainy` | Rain, HUDRain | Mist + rain |
| `0x002DB890` | `NewWeatherOvercast` | Overcast | Cloud cover |
| `0x002DB891` | `NewWeatherRadstorm` | Aurora, Lightning | Green rad storm with `sky/radstormskyeffect.nif` |
| `0x002DB892` | `NewWeatherRain` | Rain, HUDRain | Heavy rain |
| `0x004398AE` | `NewWeatherClear_i` | Clear | Standard clear |
| `0x004398AF` | `NewWeatherClear_HarpersFerry` | Clear, Fog | Harpers Ferry fog-tinted clear |

### Region-Specific Weather

**Cranberry Bog:**
| `0x0043E30B` | `NewWeatherMisty_Bog` | Mist | Bog-specific mist |
| `0x0043E30C` | `NewWeatherMistyRainy_Bog` | Rain | Bog rain |
| `0x0043E30D` | `NewWeatherOvercast_Bog` | Overcast | Bog overcast |

**The Mire (MTR) / Toxic Valley:**
| `0x003AA623` | `NewWeatherClear_Toxic` | Clear | Toxic Valley clear |
| `0x003AA62C` | `NewWeatherFoggy_MTR` | Fog, MTR_Foggy | Mire fog |
| `0x003AA666` | `NewWeatherMisty_MTR` | Mist, MTR_Misty | Mire mist |
| `0x003AA667` | `NewWeatherMistyRainy_MTR` | Rain, MTR_MistyRainy | Mire rain |
| `0x003AA668` | `NewWeatherOvercast_MTR` | Overcast, MTR_Overcast | Mire overcast |
| `0x003AA669` | `NewWeatherRain_MTR` | Rain, HUDRain | Mire heavy rain |
| `0x003AA66A` | `NewWeatherMisty_Toxic` | Mist | Toxic Valley mist |
| `0x00509F0C` | `NewWeatherAshstorm_MTR` | Ash, MTR_Ashstorm | **Ash Heap ash storm** |

**Swamp / Cranberry Bog Lowlands:**
| `0x002BA027` | `NewWeatherClear_Swamp` | Clear | Swamp clear |
| `0x003A1A9F` | `NewWeatherFoggy_Swamp` | Fog | Thick swamp fog |
| `0x003A1AA0` | `NewWeatherMisty_Swamp` | Mist | Swamp mist |
| `0x003A1AA1` | `NewWeatherMistyRainy_Swamp` | Rain, HUDRain | Swamp rain |

### Nuke Zone Weather
| `0x002BDCA8` | `NewWeatherPostNukeBlast` | Nuke, Aurora, Lightning | Post-nuke blast zone weather with `sky/radstormskyeffect.nif` |
| `0x001256FB` | `FXNukeWeather` | Clear | Initial nuke flash FX weather |

### Skyline Valley Storm Weather (Hugo Stolz Weather Machine)
| `0x0072C7C7` | `Storm_NewWeather_Overcast` | Aurora | Base storm overcast with `sky/redstormregionskyeffect.nif` |
| `0x0072C7C6` | `Storm_NewWeather_CorruptedZone` | Aurora | Corrupted zone (red sky) |
| `0x0075F0A7` | `Storm_NewWeather_CorruptedZone_Rain` | Aurora, Rain | Corrupted + rain |
| `0x006A0F8F` | `Storm_NewWeather_DeadZone` | Aurora, Lightning | Dead zone (intense red) |
| `0x00782D99` | `Storm_NewWeather_DeadZone_Rain_New` | Aurora, Lightning, Rain | Dead zone + rain |
| `0x00761063` | `Storm_NewWeather_Nuke_New` | Aurora, Nuke | Nuke in Skyline Valley |
| `0x007613D3` | `Storm_NewWeather_Nuke_New_Rain` | Aurora, Nuke, Rain | Nuke + rain in SV |
| `0x00761062` | `Storm_NewWeather_Overcast_Rain` | Aurora, Rain | Storm overcast + rain |
| `0x00782D98` | `Storm_NewWeather_Overcast_Rain_New` | Aurora, Rain | Updated overcast rain |
| `0x0078DE52` | `Storm_NewWeather_Overcast_Misty` | Aurora | Storm misty |
| `0x0078DE53` | `Storm_NewWeather_Overcast_Clear` | Aurora | Storm clearing |

### Burning Springs (The Backwoods DLC) Weather
| `0x007EBA4B` | `Burn_DesertBaseWeather` | Clear | Base desert clear with `sky/burn_auroraborealis_01.nif` |
| `0x007EE02B` | `Burn_DesertSandStormWeather` | Sandstorm, Ash | Full sandstorm |
| `0x00805B97` | `Burn_DesertSandStormWeather_Lite` | Ash | Light sandstorm |
| `0x008524EA` | `Burn_DesertSandStormWeather_Event` | Sandstorm, Ash | Event-specific sandstorm |
| `0x008535D3` | `Burn_DesertSandStormNukeWeather` | Sandstorm, Nuke, Aurora | **Nuked sandstorm** |

### Atlantic City / Expedition Weather
| `0x006DA64C` | `XPD_Weather_Boardwalk_Fog` | Fog | Original AC boardwalk fog |
| `0x006DC976` | `XPD_Weather_BoardwalkFog_NEW` | Fog, Aurora, Lightning | Updated with aurora effects |
| `0x006FA237` | `XPD_Weather_EntertainmentDistrict_Misty` | Mist, MTR_Misty | Entertainment district haze |
| `0x0072DB94` | `XPD_Weather_EntertainmentDistrict_Misty02` | Mist | Variant 2 |
| `0x00752D01` | `XPD_Weather_FloodedCity_Exterior` | Fog, Aurora | Flooded city exterior |
| `0x00661551` | `XPD_Weather_ThePitt_Smoky01_Exterior` | Fog, Aurora, Lightning | The Pitt smoky weather |
| `0x00661CD5` | `XPD_Weather_ThePitt_RadStorm01` | Aurora, Lightning | The Pitt rad storm with `sky/nukastormskyeffect.nif` |

### Shelters Weather (Interior Overrides)
| `0x0077D52A` | `Shelters_Weather_HousingDevelopment_Clear` | Clear, MTR_Clear | Housing shelter |
| `0x0077FECA` | `Shelters_Weather_SummerCamp_Clear` | Clear, MTR_Clear | Summer camp shelter |
| `0x0074E0EB` | `Shelters_Weather_Flatlands_Clear` | Clear, MTR_Clear | Flatlands shelter |
| `0x006A4337` | `Shelters_Weather_NuclearTestBunker_Smoky01` | Fog, Aurora | Smoky bunker |

### Atomic Shop / CAMP Weather Station Skins
| `0x006EE8F9` | `ATX_Weather_Clear` | Clear | CAMP clear override |
| `0x006F0681` | `ATX_Weather_Radstorm` | Radstorm, Aurora | CAMP rad storm |
| `0x007263BD` | `ATX_Weather_Snow01` | Snow | **Snow weather** |
| `0x0079B16A` | `ATX_Weather_RadstormNukeVariation` | Radstorm, NukeZone | Nuke variant rad storm with `sky/orangestormregionskyeffect.nif` |
| `0x007962BE` | `ATX_Weather_HalloweenOvercast01` | Halloween | Bats sky effect `sky/halloweenbatskyeffect01.nif` |
| `0x00798D60` | `ATX_Weather_MothmanEquinox` | Mothman | Mothman event weather |
| `0x007ACD5C` | `ATX_Weather_FallFoliage` | FallFoliage | Autumn leaves |
| `0x007B24CF` | `ATX_Weather_SnowAurora01` | Snow, Aurora | Snow with aurora borealis `sky/auroragreenblue01.nif` |
| `0x007F1829` | `ATX_Weather_VerdantPollen` | VerdantPollen | Pollen particle weather |
| `0x00811398` | `ATX_Weather_Fireworks` | Fireworks, Aurora | Fireworks sky `sky/fireworkregionskyeffect.nif` |
| `0x00832AD7` | `ATX_Weather_LightRain` | Rain, HUDRain, LightRain | Light rain |
| `0x0076B55A` | `ATX_Weather_Thunderstorm` | Rain, HUDRain, Thunder, Aurora | Full thunderstorm with `sky/thunderstormskyeffect01.nif` |
| `0x00782D9A` | `ATX_Weather_Storm_DeadZone_New` | DeadZone, Aurora | SV dead zone skin |
| `0x0073ABA8` | `ATX_Weather_XPD_AC_Boardwalk_Fog` | AC_Boardwalk | Atlantic City fog skin |
| `0x0086C996` | `ATX_Weather_BurningNight` | BurningNight | Burning Springs night sky |
| `0x0085354E` | `ATX_Weather_BurningSandStorm` | BurningSandstorm, Sandstorm | Burning Springs sandstorm |
| `0x008AACC1` | `ATX_Weather_Invasion` | Invasion, Aurora | UFO invasion sky `sky/atx_weather_invasion_ships_skyeffect.nif` |
| `0x008ABBCE` | `ATX_Weather_Outwaste` | Outwaste, Aurora | Wasteland aurora `sky/outwasteskyeffect.nif` |

### Babylon (Nuclear Winter Successor) Weather
| `0x003F8793` | `Babylon_WeatherClear` | Clear | Babylon clear |
| `0x003F8794` | `Babylon_WeatherSear` | Clear | Babylon searing heat |
| `0x003F8795` | `Babylon_WeatherSear2` | Aurora, Lightning, Clear | Searing with rad storm effects |

### Custom Worlds Weather
| `0x00616197` | `Worlds_WeatherNukaQuantumStorm` | Aurora, Lightning, Clear | **Nuka Quantum Storm** with `sky/nukastormskyeffect.nif` |
| `0x00616198` | `Worlds_WeatherNukaQuantumStormRain` | Aurora, Lightning, Rain, HUDRain | Quantum storm + rain |
| `0x00612B91` | `Worlds_WeatherFoggyDark` | Fog | Dark fog for custom worlds |

### Event-Specific Weather
| `0x00623CA7` | `NewWeatherMothmanEvent` | Aurora, Lightning | Mothman event with `sky/radstormskyeffect.nif` |
| `0x0062E7CE` | `WeatherMothmanEquinoxEventE07A` | Fog, Aurora | Mothman Equinox public event |
| `0x007D0F07` | `Weather_SSEBigBloomEvent` | Clear | **Ultracite Bloom / Scorched Earth** event weather |

### Fasnacht on Wheels (FOW) Weather
| `0x00620B1C` | `FOWWeatherRadstorm` | Aurora, Lightning | FOW rad storm |
| `0x00620B1D` | `FOWWeatherPostNukeBlast` | Nuke, Aurora, Lightning | FOW nuke weather |

### Fishing Weather
| `0x007ABE87` | `Fishing_Weather_FishermansRest_Fog` | Fog | Fisherman's Rest fog |

### FX / Lighting Weathers (Non-Gameplay)
| `0x0007548F` | `FXWthrSunlight` | -- | Pure sunlight FX |
| `0x00075491` | `FXWthrSunlightWhite` | -- | White sunlight |
| `0x00141AB4` | `FXWthrSunlightWhiteBounce` | -- | Bounced white sunlight |
| `0x0006ED5A` | `FXWthrInvertDayNight` | -- | Day/night inversion |
| `0x000777CF` | `FXWthrInvertDayNighWarm` | -- | Warm day/night inversion |
| `0x00191647` | `FXWthrInvertDayNightGS` | -- | Game settings version |
| `0x00088C57` | `FXWthrMoonlightOnly` | -- | Moonlight-only FX |
| `0x00096C61` | `FXWthrMorningOnly` | -- | Morning-only FX |
| `0x00029BB8` | `FXWthrSunlightOffAtNight` | -- | Sunlight off at night |
| `0x00171636` | `FXWthrSunlightOffAtNightGlass` | -- | Glass variant |
| `0x001D1CEC` | `FXWthrSunlightOffAtNightBlack` | -- | Black variant |
| `0x001ACEBF` | `FXWthrSunlightOffAtNightBlackChargen` | -- | Character creation |
| `0x000A6858` | `WorldMapWeather` | -- | World map sky |
| `0x0010E3D4` | `EditorCloudPreview` | Clear | CK cloud preview |

---

## 2. Weather Transition System

### Game Settings
| Setting | Value | Function |
|---------|-------|----------|
| `fWeatherTransMax` | **3.0** | Maximum weather transition duration (seconds of real time, though modified by acceleration) |
| `fWeatherTransAccel` | **16.0** | Acceleration factor when `abAccelerate = True` is used in weather override scripts |

### Transition Mechanics

Weather transitions are managed through the engine's `Weather` native class (from `weather.psc`):

```
Function ForceActive(region aOnRegion, Bool abOverride) Native
Function SetActive(region aOnRegion, Bool abOverride, Bool abAccelerate) Native
Function ReleaseOverride(region aOnRegion) Global Native
Float Function GetCurrentWeatherTransition(region aInRegion) Global Native
Weather Function GetOutgoingWeather(region aInRegion) Global Native
Weather Function GetCurrentWeather(region aInRegion) Global Native
Weather Function FindWeather(Keyword aKeyword) Global Native
```

Key behaviors:
- **`SetActive`** applies weather to a region with optional override and acceleration flags
- **`ForceActive`** immediately applies weather (used for quest-critical moments like the Hugo Stolz fight)
- **`ReleaseOverride`** removes a quest/event weather override, returning to the climate's natural rotation
- Transitions blend via the engine's `fWeatherTransMax` setting; the `abAccelerate` flag multiplies transition speed by `fWeatherTransAccel` (16x)

### Region-Locked Weather
Weather is region-bound. The `WeatherOverrideScript` (and its Storm variant `Storm_E01_WeatherOverrideScript`) take a `Region` property that determines the geographic area affected:

```papyrus
region Property RegionToAffect Auto mandatory
Int Property StageToStartWeather = -1 Auto Const  ; -1 = activate on quest init
Int Property StageToStopWeather = -1 Auto Const    ; always released on quest shutdown
```

Weather overrides are **always released on quest shutdown** to prevent permanent weather locks.

### Climate System
The game uses **10 climate records** (CLMT), with `76Climate` (`0x0000727D`) as the primary:
- `76Climate` - Main Appalachia (PBR variant: `76Climate_PBR`)
- `76Climate_Backup` - Fallback
- `ClearClimate` - Forced clear
- `DefaultClimate` / `DefaultClimateBackup` - Engine defaults (inherited from FO4)
- `SanctuaryHillsWorldClimate`, `GoodneighborClimate`, `DiamondCityClimate`, `DiamondCityPastelClimate` - Leftover FO4 climates still in data

Climate records define the weather probability distribution (WLST sub-records) that the engine cycles through when no override is active. Only 4 of the 10 climates have WLST data, meaning most are decorative or use defaults.

---

## 3. Nuke Zone Weather Mechanics

### Blast Sequence
When a nuke is launched (via `EN07_NukeMasterScript`), the following happens:

1. **Warhead reentry audio** plays within `EN07_Blast_WarheadReentryAudioRadius` = **600,000 units** (effectively the entire map)
2. **Nuke flash FX** (`FXNukeWeather`) applied within `EN07_StormNukeFlashRadius` = **40,920 units**
3. **Visual FX radius**: `EN07_NukeFXRadius` = **32,736 units**
4. **Blast music radius**: `EN07_Blast_MusicRadius` = **122,760 units**
5. **NPC reaction radius**: `W05_NPCNukeReactionRadius` = **32,736 units**
6. Weather transitions to **`NewWeatherPostNukeBlast`** (`0x002BDCA8`) within the blast zone

### Blast Zone Parameters
| Global | Value | Notes |
|--------|-------|-------|
| `EN07_NukeBlastRadius` | **20,460 units** | Actual nuke zone radius (~300m) |
| `EN07_NukeZoneTimeLength` | **7,200 seconds** | Nuke zone duration = **2 hours real time** |
| `EN07_StormNukeBlastRadius` | **64,000 units** | Skyline Valley nuke blast radius (3x larger) |
| `EN07_StormNukeZoneTimeLength` | **1,200 seconds** | SV nuke zone = **20 minutes** (much shorter) |

### Nuke Zone Weather Properties
- Weather type: `NewWeatherPostNukeBlast` with keywords: Nuke (`0x00525F63`), PermanentAurora (`0x0015A069`), Lightning
- Sky model: `sky/radstormskyeffect.nif` (green/yellow radioactive sky)
- The `ImmuneToNukeWeather` keyword (`0x00538218`) can be applied to actors to make them ignore nuke weather effects
- Blast zones block respawning (`sNoRespawnBlastZone`) and fast travel (`sNoFastTravelBlastZone`)

### Nuke Zone Radiation
The curve table `weather_nukefallout_rad.json` defines a flat radiation curve:
- At player level 1-100: **40 rads/sec** constant
- This radiation is applied as a weather effect; Rad-X, hazmat suits, and power armor reduce it

---

## 4. Rad Storm Damage and Scaling

### Rad Storm Spell Chain
The base rad storm applies via `RadStormSpell` (`0x001C5E7B`) with conditions:
- Player must NOT have `Ghoulish` perk (FormID `0x000A2775`)
- Player must NOT have `ImmuneToNukeWeather` keyword (`0x0023954F`)
- Player must NOT be in an interior (`IsInInterior == 0`)

### Radiation Damage Settings
| Setting | Value | Purpose |
|---------|-------|---------|
| `fRadsDamageBase` | **0.0** | Base rad damage (modified by weather/hazard spells) |
| `fRadsDamageFactor` | **0.15** | Damage scaling multiplier |
| `fRadsArmorBase` | **0.0** | Base rad resistance from armor |
| `fRadsArmorBase_NORM` | **51.0** | Normalized rad armor base |
| `fRadsArmorDmgReductionExp` | **0.365** | Exponential falloff for armor damage reduction |
| `fRadsMaxDamageReduction` | **0.99** | Maximum 99% radiation damage reduction cap |
| `fRadiationHealthCurve` | **1.0** | Linear health loss per rad accumulated |
| `Nuke fallout radiation` | **40 rads/sec** | Constant from curve table |

### Region-Specific Rad Storm Variants
- **Main Appalachia**: `NewWeatherRadstorm` - standard green rad storm
- **Skyline Valley**: `Storm_NewWeather_Nuke_New` - red storm sky, enhanced lightning
- **The Pitt**: `XPD_Weather_ThePitt_RadStorm01` - uses `sky/nukastormskyeffect.nif` (amber/orange)
- **FOW**: `FOWWeatherRadstorm` - event-specific
- **Burning Springs**: `Burn_DesertSandStormNukeWeather` - sandstorm + nuke radiation

### Skyline Valley Storm Mutations
The Skyline Valley storm introduces unique electric mutation effects:
- `Storm_MutationEffect_Electric` - base electric buff
- `Storm_MutationEffect_Electric_radStorm` - enhanced during rad storms
- `Storm_Mutation_ElectricDamage_lightningStrike` - lightning strike damage
- `Storm_NukeWeatherEnemyBuff_Cloak` - enemies get a cloaking buff during nuke weather in the storm region

---

## 5. Day/Night Cycle

### Time Settings
| Global | Value | Purpose |
|--------|-------|---------|
| `TimeScale` | **20.0** | 1 real minute = 20 game minutes |
| `GameHour` | **11.0** | Default start hour |
| `GameDay` | **23** | Default start day |
| `GameMonth` | **10** | October (Reclamation Day) |
| `GameYear` | **287** | Internal year counter |
| `iGameYear` (GMST) | **2105** | Display year |

**Real-time cycle**: At TimeScale 20, a full 24-hour game day = **72 real minutes** (1 hour 12 minutes).

### Day/Night Spawn Effects
- **Feral Ghoul Day/Night Sandbox** (`DMP_Feral_DayNightSandbox`, `0x000ED13D`): Feral ghouls use a pack-in (`LvlFeralGhoulDayNightPackIn`, `0x000ED173`) that changes their behavior between day (dormant/wandering) and night (aggressive/sandbox)
- **Nocturnal Fortitude** perk (`NocturnalFortitude01/02`): Player perk that grants bonuses at night
- FX weathers like `FXWthrSunlightOffAtNight`, `FXWthrMoonlightOnly`, and `FXWthrInvertDayNight` are used for interior lighting rigs and special locations, not gameplay day/night mechanics
- The `W05_WL059_RaiderFishCamp_OncePerDaySpawner` actor value gates certain spawns to once per in-game day

### Image Space Modifiers
Each weather defines 8 image space settings for different times of day:
- Dawn Early, Dawn Late, Day, Dusk Early, Dusk Late, Night, plus transition states
- This creates smooth visual transitions as the day progresses

---

## 6. Season/Time-Based Environment Changes

### CAMP Weather Station System
Players can place **CAMP Weather Stations** that override the local weather with cosmetic weather types. 22 weather station variants exist in the Atomic Shop:

- Clear, Light Rain, Snow, Snow Aurora, Thunderstorm
- Radstorm, Nuke Zone, Fall Foliage, Halloween (bats)
- Mothman Equinox, Verdant Pollen, Fireworks
- Skyline Valley Dead Zone, Atlantic City Boardwalk Fog
- Burning Night, Burning Sandstorm
- Invasion (UFOs), Outwaste (wasteland aurora)

These use the `LinkTerminalATXCampWeatherStation` keyword (`0x006EE8F5`) to link a terminal to the weather station. The terminal inherits native functions to control the weather within the CAMP boundary.

### Seasonal Events with Weather
- **Mothman Equinox**: Uses `WeatherMothmanEquinoxEventE07A` (dark foggy weather with aurora) and `ATX_Weather_MothmanEquinox` (CAMP version) with dedicated image space and volumetric lighting
- **Scorched Earth / Ultracite Bloom**: Uses `Weather_SSEBigBloomEvent` in the `BigBloomWeatherRegion` (`0x007D18C6`)
- **Fasnacht on Wheels (FOW)**: Has its own weather list (`FOW_Weather`, FormList `0x00606B56`) with `FOWWeatherRadstorm` and `FOWWeatherPostNukeBlast`

---

## 7. Skyline Valley Storm Mechanics (Hugo Stolz Weather Machine)

### Region Structure
The Skyline Valley storm system uses a layered region structure:
- **`StormRegion`** (`0x006923E9`) - Master region for the entire Skyline Valley
- **`StormWeatherRegion_Corrupted`** (`0x00726986`) - Corrupted zone (moderate storm)
- **`StormWeatherRegion_DeadZone`** (`0x006FCB10`) - Dead zone (intense storm)
- **`Storm_E01_Region`** (`0x007729A5`) - Public event region (Dangerous Storms)
- **18 StormSubRegions** (StormSubRegion01 through StormSubRegion18) - Granular sub-areas

### Weather Machine Quest Line
The Storm questline (`Storm_MQ01` through `Storm_MQ13`) progresses through these stages:
- **MQ01**: Breadcrumb via radio (`Storm_MQ01_Breadcrumb_Radio`)
- **MQ02-MQ03**: Introduction (IntroPt1, IntroPt2)
- **MQ04-MQ06**: Hugo storyline (HugoPt1, HugoPt2, HugoPt3)
- **MQ07-MQ09**: Oberlin storyline (OberlinPt1, OberlinPt2, OberlinPt3)
- **MQ13**: Finale - Weather Machine confrontation
  - `Storm_MQ13_WeatherMachineTriggeredEffect` / `Storm_MQ13_WeatherMachineTriggeredSpell` - Weather machine activation
  - `Storm_MQ13_HarvesterHealth` = **50 HP** (harvester health during defense)
  - `Storm_MQ13_HarvesterDefendTime` = **45 seconds**
  - Hugo boss fight includes: stealth, flashbang, trippy vision effects, electric arc spell, fade to black

### Lightning Strike System
From `Storm_E01_LightningStrikes`:
- **Spawn strikes** every **30-45 seconds** (SpawnTimeBetweenStrikesMin/Max)
- **Utility strikes** every **5-15 seconds** (deprecated but still in data)
- **Gap between individual strikes**: 0.5-1.5 seconds
- Strikes spawn **Charged creatures** at designated markers
- Electrical hazards prevent rooftop camping during both "Charge the Harvester" and "Kill the Boss" phases

### Lightning Harvester (Public Event)
From `Storm_LightningHarvesterScript`:
- 3 harvester positions with dedicated strike marker arrays
- Strike timing: 5-15 seconds between volleys, 1.0 second gap between individual strikes
- Each harvester has near markers and far markers for visual effect distribution

### Corrupted Flora
Skyline Valley introduced corrupted flora variants:
- `Storm_FoxgloveCorruptedV1` through `V6` - 6 variants of corrupted foxglove
- `Storm_Lightning_Flux02` - Lightning flux (harvestable)
- Dedicated corrupted tree and fern pack-ins for the corrupted/dead zones

### Lost Creatures
- `Storm_LostStateHandler` extends `W05_InstSwapEnableState` to swap actors into "Lost" state
- `Storm_LostHealingEffect` / `Storm_LostHealingcloak` - Lost creatures have a healing cloak
- Lost Feral Suiciders exist as both living and corpse variants

### Weather Machine Effect
`Storm_MQ13_WeatherMachineTriggeredEffect` (`0x0077092D`) is a magic effect applied when the weather machine fires during the finale. The weather transitions are handled by `Storm_E01_WeatherOverrideScript`, which includes a reset function with `WeatherReset` (clear weather form) and can accelerate transitions via `fWeatherTransAccel`.

---

## 8. Atlantic City Fog System

### Weather Types
Atlantic City uses several dedicated fog/mist weathers across its districts:

| Weather | District | Visual Style |
|---------|----------|-------------|
| `XPD_Weather_Boardwalk_Fog` | Boardwalk | Standard thick fog |
| `XPD_Weather_BoardwalkFog_NEW` | Boardwalk | Updated version with aurora and lightning |
| `XPD_Weather_EntertainmentDistrict_Misty` | Entertainment | Light haze (MTR_Misty keyword) |
| `XPD_Weather_EntertainmentDistrict_Misty02` | Entertainment | Variant with slightly different image space |
| `XPD_Weather_FloodedCity_Exterior` | Flooded City | Fog with aurora, used in exterior flooded areas |

### Image Space
Dedicated fog image spaces handle time-of-day variations:
- `Fishing_Weather_FishermansRest_Foggy` (day) and `_Night` variants
- Boardwalk fog has unique volumetric lighting settings

### The Pitt Expedition Weather
The Pitt uses its own smoky/rad storm weathers:
- `XPD_Weather_ThePitt_Smoky01_Exterior` - Smoky industrial haze
- `XPD_Weather_ThePitt_RadStorm01` - Pitt-specific rad storm with amber `sky/nukastormskyeffect.nif`
- These are applied via region overrides during expedition instances

---

## 9. Weather Effects on Player Stats

### Direct Weather Damage Types
1. **Rad Storm Radiation**: Applied via `RadStormSpell` - rads over time while outdoors during rad storms
2. **Nuke Zone Radiation**: 40 rads/sec (flat curve, level-independent)
3. **Disease Risk from Weather**: `AbReduceDiseaseChanceWeather` (`0x002BA530`) - weather affects disease chance
4. **Sandstorm VATS Accuracy**: `Burn_SandstormVATsAccuracy_Weather` (`0x00830285`) and `Burn_SandstormVATsAccuracy` (`0x00802828`) - sandstorms in Burning Springs **reduce VATS accuracy**
5. **Sandstorm Armor Reduction**: `BURN_AbraxoAntiArmour_Weather` (`0x00853E03`) and PA variant (`0x00853E04`) - Abraxodyne sandstorm effect that strips armor during weather events

### Babylon Storm Damage
In Nuclear Winter's successor mode (Babylon):
- `fBabylonDestructiblesMaxHealthPerSecondStormDamage` = **0.5 HP/sec** to destructibles
- Storm shrinking mechanic (similar to battle royale ring)
- `BabylonImmuneToStormKeyword` (`0x0045E3CC`) grants immunity

### Water and Radiation
Multiple water radiation tiers exist:
| Spell | Purpose |
|-------|---------|
| `WaterRadiationHazard` (`0x00023F1B`) | Standard irradiated water |
| `WaterRadiationHighHazard` (`0x001FE6A3`) | High-rad water (Toxic Valley pools) |
| `WaterRadiationHighDrinkingToxic` (`0x001FE6A4`) | Drinking toxic water |
| `WaterRadiationSevereHazard` (`0x003C2E05`) | Severe radiation water |
| `WaterRadiationDrinkingDirty` (`0x00024FBF`) | Drinking dirty water |
| `DLC03_WaterRadiationAtomsSpringDrinking` (`0x00111722`) | Atom's Spring special water |
| `V94_WaterRadiationHighHazard` (`0x0040E613`) | Vault 94 GECK water |

Disease risk keywords for toxic water are split by contact type:
- `SURV_DiseaseRiskForm_ToxicWater_Standing` (standing in)
- `SURV_DiseaseRiskForm_ToxicWater_Swimming` (swimming)
- `SURV_DiseaseRiskForm_ToxicWater_UnderWater` (submerged)

The `WaterRadiationImmune` keyword (`0x005EEAE5`) can be applied to protect actors.

### Environmental Heat
- `CoolingTowerHeatDamage` = **10 damage** (from cooling tower hazards, not ambient weather)
- No ambient temperature/cold system exists; FO76 does not have Survival-mode exposure mechanics

### Nuke Zone Entry Protection
- `LoadIntoNukeZoneRadResist` (`0x0059BCD1`) - temporary rad resistance spell applied when a player loads into a nuke zone
- `LoadIntoNukeZoneFortifyResistRadiationExpose` - 30-second grace period with `RemoveSpellTime = 30.0` seconds
- Removed if player moves more than 2.0 units (`PlayerRemoveSpellDistance`)

---

## 10. Flora Respawn Timers

### Standard Flora
The `Flora` base script (`flora.psc`) extends `Activator` and is a hidden base class. Flora respawn is handled by the engine's built-in harvestable object system rather than through script timers. The engine respawn time for flora objects is set per-world-space and is generally **30 minutes** of real time for standard flora in Appalachia (controlled by cell-level reset timers).

### Fissure/Encounter Respawn
| Global | Value | Notes |
|--------|-------|-------|
| `EN07_Fissure_RespawnTimerLength` | **600 seconds** (10 minutes) | Fissure site creature respawn |
| `EN07_Fissure_UnloadTimerLength` | **90 seconds** | Time before unloading fissure contents |
| `EN07_Fissure_ResetLength` | **21,600 seconds** (6 hours) | Full fissure reset timer |
| `EN07_FissureClosureDistance` | **20,500 units** | Distance at which a fissure closes |

### Info Reset Timers (General Respawn Framework)
| Timer | Value |
|-------|-------|
| `InfoResetTimerShort_6mins` | 6 minutes |
| `InfoResetTimerMedium_30mins` | 30 minutes |
| `InfoResetTimerLong_60mins` | 60 minutes |
| `InfoResetTimerVeryLong_12Hrs` | 12 hours |

---

## 11. Water Radiation Levels by Region

### Water Type Records (47 WATR Records)
| Water Type | Region/Context |
|------------|---------------|
| `ExtRiverOhioWater` (`0x00000018`) | Ohio River - base water |
| `ExtClearWaterDefault` (`0x000C8633`) | Clear streams, rivers |
| `ExtClearWaterFlow` (`0x00034519`) | Flowing clear water |
| `ExtMurkyWaterDefault` (`0x001BDDB6`) | Murky water (light rad) |
| `ExtMurkyWaterFlow` (`0x000C863D`) | Flowing murky water |
| `ExtMurkyWaterPuddle` (`0x00102D5B`) | Stagnant murky puddles |
| `ExtToxicWaterBasin` (`0x000114CE`) | **Toxic Valley** standing water |
| `ExtToxicWaterFlow` (`0x00044F50`) | Flowing toxic water |
| `ExtToxicWaterTransition` (`0x0050E3FE`) | Transition zone |
| `ExtCranBogWater` (`0x00102D5A`) | Cranberry Bog water |
| `ExtCranBogWaterFlow` (`0x0015F578`) | Cranberry Bog flowing |
| `ExtCranBogWaterTransition` (`0x00432C4C`) | Bog transition |
| `ExtMtnRemovalWater` (`0x003852D6`) | Mountain removal site |
| `ExtNuclearWasteWater` (`0x003C2E02`) | Nuclear waste dumps (high rad) |
| `IntNuclearWasteWater` (`0x003C2E03`) | Interior nuclear waste |
| `IntFEVWater` (`0x003A6059`) | FEV water (West-Tek) |
| `IntFEVWaterPuddle` (`0x003A605A`) | FEV puddles |
| `Storm_ExtStormWater` (`0x006A16E3`) | Skyline Valley storm-irradiated water |
| `Storm_WaterClear` (`0x006FC4B7`) | Skyline Valley clear water |
| `ExtStormRadioactiveWasteDump` (`0x00744C47`) | SV radioactive waste |
| `LavaUltracite` (`0x007929AB`) | Ultracite lava |
| `Burn_ExtAbraxoWaterBasin` (`0x0080FFA5`) | Burning Springs Abraxodyne water |
| `Burn_ExtToxicAbraxoWaterBasin` (`0x0082F8B9`) | Toxic Abraxodyne water |

Radiation severity increases: Clear < Murky < Cranberry Bog < Toxic < Nuclear Waste < FEV. Each water type has associated hazard spells and disease risk keywords.

---

## 12. Environmental Storytelling Triggers

### Weather-Gated Events
- **Mothman Equinox**: Forces `WeatherMothmanEquinoxEventE07A` during the public event, creating the atmospheric dark-fog-with-aurora ambience
- **Dangerous Storms** (Skyline Valley public event): `Storm_E01_WeatherOverrideScript` forces storm weather for the event duration, always releasing on quest shutdown
- **Scorched Earth / Ultracite Bloom**: Forces `Weather_SSEBigBloomEvent` in the `BigBloomWeatherRegion` during the event
- **Burning Springs events**: Desert sandstorm weather applied during bounty hunts and sinkhole events via `Burn_DesertSandStormWeather_Event`

### Time-Gated Behaviors
- **Feral Ghoul Day/Night**: `LvlFeralGhoulDayNightPackIn` changes behavior -- ghouls are more dormant during the day and more active at night
- **Once-per-day spawners**: `W05_WL059_RaiderFishCamp_OncePerDaySpawner` gates certain encounters to one per game day

### Quest-Triggered Weather
- All Storm MQ quests (MQ01-MQ13) use weather overrides that activate at specific quest stages (`StageToStartWeather`) and deactivate at others (`StageToStopWeather`)
- The Hugo Stolz finale (MQ13) triggers a unique sequence: weather machine activation spell, harvester defense, boss fight with trippy vision effects, and lightning arc attacks

---

## 13. Blast Zone Creation Mechanics

### Radius and Duration
| Parameter | Standard Nuke | Skyline Valley Nuke |
|-----------|--------------|-------------------|
| Blast radius | 20,460 units (~300m) | 64,000 units (~940m) |
| Zone duration | 7,200 sec (2 hours) | 1,200 sec (20 min) |
| Flash radius | 40,920 units | 40,920 units |
| FX radius | 32,736 units | 32,736 units |
| NPC reaction radius | 32,736 units | 32,736 units |

### Flora Mutation System
When a nuke detonates, flora within the blast zone is "swapped" to nuked variants that yield **raw flux** (5 colors):
- **Raw Cobalt Flux** (Blue, `PlantTypeFluxBlue`)
- **Raw Fluorescent Flux** (Yellow, `PlantTypeFluxYellow`)
- **Raw Crimson Flux** (Red, `PlantTypeFluxRed`)
- **Raw Violet Flux** (Purple, `PlantTypeFluxPurple`)
- **Raw Yellowcake Flux** (Orange, `PlantTypeFluxOrange`)

#### Swap Percentages (ECON = Economy Values)
| Flux Color | Swap % (ECON) | Tier Priority |
|------------|--------------|---------------|
| General | 10% | -- |
| Red | 100% | 5 (highest priority) |
| Blue | 100% | 3 |
| Purple | 100% | 4 |
| Orange | 100% | 2 |
| Yellow | 100% | 1 (lowest priority) |

The ECON values are all 100%, meaning **all eligible flora is swapped** within range. The Tier values (1-5) determine priority when multiple flux types could apply.

#### Distance Tiers for Flora Mutation
| Distance Tier | Range (units) | Tier Value |
|--------------|---------------|------------|
| Inner | 4,092 | 4 (highest density) |
| Medium | 8,184 | 3 |
| Far | 12,276 | 2 |
| Region | Full blast radius | 1 (lowest density) |

Flora is swapped using `EN07_NukeFloraStubMarker` (`0x001D7F74`) activators placed throughout the world. The `NukeFlora_SwapPercent_V94` = 10% (used for Vault 94 raid, lower mutation rate).

### Blast Zone Books (Player Guides)
Five in-game guide books exist for nuked flora identification:
- `ENB_NukedFloraGuide_Blue` (`0x003CFB3A`)
- `ENB_NukedFloraGuide_Red` (`0x003CFB3C`)
- `ENB_NukedFloraGuide_Orange` (`0x003CFB3E`)
- `ENB_NukedFloraGuide_Yellow` (`0x003CFB3B`)
- `ENB_NukedFloraGuide_Purple` (`0x003CFB3D`)

### Crafting
Components for nuke flora crafting:
- `c_NukeFlora_Blue`, `c_NukeFlora_Red`, `c_NukeFlora_Purple`, `c_NukeFlora_Orange`, `c_NukeFlora_Yellow`
- Recipe filter: `RecipeFilter_Chem_NukeFlora`
- Curve tables: `COBJ_Ammo_NukedFlora`, `COBJ_Weapon_NukedFlora`

### Babylon-Specific Nuke Mechanics
The Babylon game mode uses a smaller nuke zone:
- `BabylonNukeZoneWeatherRadius` = **3,000 units** (much smaller than standard)
- `BabylonUseNukeZoneBlastRadius` keyword indicates whether to use the standard blast radius
- `fBabylonEndGameOverseerExperiencePerNukeLaunch` = **50 XP** per nuke launch
- `fBabylonNukeBriefcaseMarkerInWorldDistance` = **1,900 units** (briefcase tracking range)

---

## 14. Cut Weather Types and Environment Events

### Deprecated Weather (zzz / CUT prefix)
| FormID | EditorID | Status | Notes |
|--------|----------|--------|-------|
| `0x002D32CC` | `NewWeatherClear_DONOTUSE` | Disabled | Original clear weather, replaced |
| `0x003A1AA3` | `_CUT_NewWeatherRain_Swamp` | Cut | Rain weather for swamp areas |
| `0x003A1AA2` | `_CUT_NewWeatherOvercast_Swamp` | Cut | Overcast for swamp |
| `0x00509F0B` | `_CUT_NewWeatherRadstorm_Toxic` | Cut | **Toxic Valley rad storm** - would have given Toxic Valley its own unique rad storm |
| `0x003AA635` | `_CUT_NewWeatherClear_MTR` | Cut | Mire clear weather |
| `0x0065CE06` | `XPD_Weather_CUT_ThePitt_Smoky01` | Cut | Original Pitt smoky weather |
| `0x00853D48` | `zzzATX_Burn_DesertSandStormWeather` | Replaced | Original Burning Springs sandstorm |
| `0x0079A1EE` | `zzzATX_Weather_P56` | Cut | Snow weather variant ("P56" = internal season code) |
| `0x007990A3` | `zzz_SCORE_S19_NewWeather_Nuke_New` | Replaced | Season 19 nuke weather (superseded) |
| `0x0077E755` | `zzzATX_Weather_Storm_DeadZone` | Replaced | Original dead zone weather |
| `0x0075F0A8` | `zzzStorm_NewWeather_DeadZone_Rain` | Replaced | Original dead zone rain |
| `0x00757618` | `zzzATX_Weather_Storm_CorruptedZone` | Replaced | Original corrupted zone weather |
| `0x0072DC86` | `zzzStorm_NewWeather_Nuke` | Replaced | Original SV nuke weather |
| `0x006A0F8D` | `zzzStorm_NewWeather_BaseStorm_Nuke` | Replaced | Used blue nuke sky (`sky/bluestormregionnukeskyeffect.nif`) - **unique blue nuke storm sky model not used in any active weather** |
| `0x00743E70` | `zzzzATX_Weather_Thunderstorm_OLD` | Replaced | Original thunderstorm (4x zzz = very deprecated) |

### Babylon Weather (Nuclear Winter Successor)
Three Babylon weather types exist but the mode was never publicly released:
- `Babylon_WeatherClear` - Standard clear
- `Babylon_WeatherSear` - Heat searing effect
- `Babylon_WeatherSear2` - Searing with rad storm aurora/lightning (the closing storm ring)
- Storm shrinking mechanic (`sBabylonStormShrinkingMsg`) confirms battle royale ring behavior

### Notable Cut/Unused Elements
1. **Blue Nuke Storm Sky**: `sky/bluestormregionnukeskyeffect.nif` was used by `zzzStorm_NewWeather_BaseStorm_Nuke` - a unique blue nuclear sky that was replaced by the red storm sky
2. **Toxic Valley Rad Storm**: `_CUT_NewWeatherRadstorm_Toxic` would have given Toxic Valley a unique rad storm variant instead of sharing the generic one
3. **Swamp Weather Suite**: Two cut swamp weathers suggest the Cranberry Bog/swamp was originally planned to have a more varied weather rotation
4. **Season P56**: `zzzATX_Weather_P56` appears to be a seasonal snow weather that was cut or replaced before release
5. **Nuka Quantum Storm**: `Worlds_WeatherNukaQuantumStorm` and rain variant exist in Custom Worlds data with unique `sky/nukastormskyeffect.nif` - a **blue/purple quantum-colored storm** available only in Custom Worlds

---

## Key Weather Keywords Reference

| FormID | Keyword | Purpose |
|--------|---------|---------|
| `0x00176988` | (Clear) | Clear weather classification |
| `0x0002F28B` | `WeatherTypeAuroraFollowsSun` | Aurora follows sun position |
| `0x0015A069` | `WeatherTypePermanentAurora` | Aurora persists day and night |
| `0x00151838` | `WeatherTypeHUDRain` | Shows rain on HUD/screen |
| `0x0017698D` | (Rain particles) | Rain particle system |
| `0x0017698E` | (Lightning) | Lightning effects |
| `0x00176989` | (Precipitation) | Precipitation particles |
| `0x00525F63` | (Nuke) | Nuclear blast weather |
| `0x004510DB` | (Rain - alternate) | Secondary rain keyword |
| `0x00017C6F` | (Ash) | Ash/sandstorm particles |
| `0x0084A7BD` | `s_wt_Sandstorm` | Sandstorm classification |
| `0x0076EA1B` | `WeatherTypeIntenseLightEffects` | When applied, lightning and sky box effects can be disabled by player settings |
| `0x00538218` | `ImmuneToNukeWeather` | Actor ignores nuke weather effects |
| `0x005EEAE5` | `WaterRadiationImmune` | Actor ignores water radiation |
| `0x0045E3CC` | `BabylonImmuneToStormKeyword` | Immune to Babylon storm ring |

---

## Summary Statistics
- **116 total WTHR records** (47 water types, 10 climates)
- **22 CAMP Weather Station variants** in the Atomic Shop
- **15 cut/deprecated weather types** (zzz/CUT prefix)
- **5 flux colors** for nuked flora mutation
- **47 unique water type records** with varying radiation levels
- **18 Storm Sub-Regions** in Skyline Valley
- **3 distinct storm zone types**: Corrupted, Dead Zone, and Nuke
- Day/night cycle: **72 real minutes** per in-game day
- Nuke zone duration: **2 hours** (standard), **20 minutes** (Skyline Valley)
- Nuke zone radiation: flat **40 rads/sec** regardless of level
