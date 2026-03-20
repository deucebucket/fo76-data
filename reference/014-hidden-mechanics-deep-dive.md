# Fallout 76 Hidden Mechanics Deep Dive

## Source: 7,095 Decompiled Papyrus Scripts (.psc files)
## Path: ~/ai-drive/gamecryptids/data/fallout76/scripts_decompiled/

---

## 1. CAPS STASH HIDDEN PROBABILITIES

**Script:** `capsstashscript.psc`

Cap stashes use a hidden tiered loot system with exact probabilities:

| Tier | Chance | Caps Range |
|------|--------|------------|
| Jackpot | 1% (0.01) | 100-125 |
| High | 7.5% (0.075) | 50-60 |
| Medium | 20% (0.2) | 30-40 |
| Standard | 71.5% (remainder) | 10-20 |

**Cap Collector perk hidden scaling (lines 18-23):**
- Rank 1: 2.0x caps multiplier, 33% activation chance
- Rank 2: 2.25x caps multiplier, 66% activation chance
- Rank 3: 2.5x caps multiplier, 100% activation chance

**Bobblehead bonus (line 17):** `capsBobbleheadChanceMultiplier = 2.0` -- having the Caps Bobblehead DOUBLES all chance thresholds for better tiers.

---

## 2. LEGENDARY/EPIC CREATURE SCALING FORMULA

**Script:** `epiccreaturesscript.psc`

The exact formula for whether a creature becomes legendary (line 72):

```
Epic Chance = (Base + (ActorLevel * ActorLevelMult)) * RegionMult
```

**Default values:**
- `Base = 1.0` (line 73)
- `ActorLevelMult = 0.04` (line 75) -- each creature level adds 0.04% chance
- `DefaultRegionMult = 1.0` (line 79) -- regions can have different multipliers
- `MaxChance = 5.0` (line 81) -- **capped at 5%** maximum
- `MinActorLevel = 10` (line 83) -- creatures below level 10 CANNOT become legendary

**Per-rank health and damage multipliers (lines 25-28):**
- Default `HealthMult = 1.25` per rank (compound on base health)
- Default `OutgoingDamageMult = 1.25` per rank
- `IncomingDamageMultClamp = -0.99` (line 108) -- legendary damage resistance capped at 99%

**Horde trigger chances (lines 30-33):**
- Normal epic creature: `HordeChance = 0` (0% chance to trigger horde)
- Nemesis creature: `NemesisHordeChance = 15` (15% chance to trigger horde event)
- Nemesis requires `NemesisMinKillCount = 3` player kills to rank up

**Hidden mechanic (line 132):** All epic creatures get `AbEpicCreature_RestoreHealth_Trigger` -- they heal to FULL health when hitting 50% or less. This is hardcoded, not tied to legendary rank. Every legendary creature has a hidden "second life" at 50% HP.

---

## 3. 4-STAR LEGENDARY CHANCE

**Script:** `defaultlegendary4starcreatureref.psc`

When a creature is set to Legendary Rank 3, there's a hidden roll for rank 4:
- `Rank4Chance = 0.5` (line 11) -- **50% chance** that a 3-star creature becomes 4-star
- This is per-reference, meaning individual placed creatures can have different values

---

## 4. BOMB DEFUSAL: LUCK AND INTELLIGENCE MATTER

**Script:** `re_objectts05_bombactivatorscript.psc`

Random encounter bomb defusal has a hidden dice roll:
- `RollSuccessThreshold = 85.0` (line 14) -- you need to roll 85+ out of 100
- **Luck modifier:** `LuckModifier = 0.8` (line 16) -- your Luck stat * 0.8 is added to your roll
- **Intelligence modifier:** `IntelligenceModifier = 1.6` (line 18) -- your Intelligence * 1.6 is added to your roll

So with 15 Intelligence and 15 Luck, you get: roll + (15*1.6) + (15*0.8) = roll + 24 + 12 = roll + 36, making it nearly impossible to fail.

---

## 5. BRAHMIN MILKING USES CHARISMA

**Script:** `brahminracemilkingscript.psc`

Brahmin milking uses curve tables tied to Charisma (line 58) to determine:
- Chance of getting a large milk yield vs. small yield
- Large yield range: `MilkLargeQuantityMin` to `MilkLargeQuantityMax`
- Small yield range: `MilkSmallQuantityMin` to `MilkSmallQuantityMax`
- Fail state plays a kick animation

**Hidden cooldown per brahmin** (lines 13-16): After successful milking, there's a random cooldown between `MilkingDisabledTimeMin` and `MilkingDisabledTimeMax` seconds before that specific brahmin can be milked again. Workshop brahmin have a separate keyword check.

---

## 6. POWER PLANT ENTROPY SYSTEM

**Script:** `powersystemdatascript.psc`

Power plants have a complex hidden degradation system:

- **Fuel consumption timer:** Every 600 seconds (10 minutes) (line 26)
- **Entropy timer:** Every 600 seconds (10 minutes) (line 50)
- **Time to failure:** 7 days from perfect to subsystem failure (line 52)
- **Failure threshold:** Subsystem fails at 25% health (line 35)
- **Repair quest triggers at:** 40% subsystem health (line 37)
- **Repair quest completes at:** 60% subsystem health (line 39)
- **Refuel quest starts:** 2 hours of fuel remaining (line 28)
- **Refuel quest ends:** 48 hours of fuel remaining (line 30)
- **Cooling tower lockdown max:** 10 minutes (line 41)
- **Breakdown while off:** 2 days to failure rate (line 54)
- **Power setting change cooldown:** 1800 seconds (30 minutes) after success/failure (line 76)

**TODO comments reveal unimplemented features (lines 57-61):**
- `CONST_EntropyHealthMultiplier = 1.0` -- labeled "TODO: actually an exponent" suggesting plants were meant to degrade faster at lower health
- `CONST_EntropyPlayerCountBase = 10.0` -- "TODO: for each player above 10 on the server, systems fail faster"
- `CONST_EntropyPlayerCountMultiplier = 1.0` -- the player count scaling was never actually implemented (left at 1.0)

---

## 7. SILO OPERATIONS SECURITY SYSTEM

**Script:** `msiloquestscript_operations.psc`

Missile silo security level system has hidden constants:
- Security level range: **400 to 1000** (lines 23-24)
- Security wave scene delay: **45 seconds** (line 13)
- Security event timer updates every **1 second** (line 16)
- Encounter wave startup delay: **5 seconds** (line 19)
- `SecurityMultiplierMainframePanel = 1.0` (line 21) -- each mainframe panel destroyed reduces security proportionally

---

## 8. NUKE MECHANICS

**Script:** `dlc01_nuketargetscript.psc`

- **Post-nuke weather duration:** `iNukeWeatherTimerLength = 1500` seconds = **25 minutes** (line 91)
- **Nuke blast delay:** `fNukeBlastTimerLength = 2.5` seconds after drop animation (line 93)
- **Bomb touchdown point:** `fNukeDropTouchdownProgress = 0.46` -- blast triggers at 46% of the drop animation (line 95)
- **Cloud spawn point:** `fCloudSpawnProgress = 0.27` -- mushroom cloud spawns at 27% of animation (line 97)
- Distance-based systems: `NukeBlastDistance`, `NukeWeatherDistance`, `NukeFXRadius` all controlled by GlobalVariables

---

## 9. HUNTER/HUNTED RADIO MECHANICS

**Script:** `hunterhuntedquestscript.psc`

- **Ping distance multiplier:** `PingDistanceTimeMultiplier = 6.0` (line 8)
- **Max ping distance:** 20,000 units (line 9)
- **Min ping distance:** 256 units (line 10)
- **Target marker move time:** 3.0 seconds (line 11)
- **Failsafe quest end:** 900 seconds = **15 minutes** (line 12) -- if no kills after 15 min, quest force-ends
- **Ping interval range:** 0.1 to 6.0 seconds (lines 49-50) -- closer = faster pings
- **Win kill bonus:** 2 extra kills added to count if you win (line 54), but only if you have `WinHuntKillBonusMinimumKills = 1` (line 56)
- **Required players:** 4 minimum to start (hunterhuntedmasterquestscript.psc line 50)
- **Radio frequency:** 96.5 (line 53)

---

## 10. MYSTERY MEAT HIDDEN RADIATION SCALING

**Script:** `perks_playerspecificperkfunctions.psc`

Mystery Meat perk has hidden radiation-based scaling:
- `radsMaxValue = 1000.0` (line 23) -- max rads value used for calculations
- `mysteryMeatRadsChanceModMin = 0.5` (line 51) -- at 0 rads, chance is multiplied by 0.5x
- `mysteryMeatRadsChanceModMax = 1.5` (line 53) -- at max rads, chance is multiplied by 1.5x
- `cooldownSeconds = 60.0` (line 55) -- **60 second cooldown** between Mystery Meat procs

**The more irradiated you are, the more likely Mystery Meat triggers.** At max rads it's 3x more likely than at 0 rads.

---

## 11. MUTATION SYSTEM INTERNALS

**Script:** `surv_playermutationscript.psc`

- `MinRadMutationLevel = 5` (line 42) -- players below level 5 CANNOT gain mutations from radiation
- `RadDamageBucketSizeMax = 10.0` (line 38) -- rad damage is bucketed in groups of 10
- Mutation chance uses: `SURV_MutationRollExponent`, `SURV_MutationRollMult`, `SURV_MutationRollMaxPossible` (GlobalVariables, lines 59-63)
- `SURV_MutationRollCooldownHours` (line 57) -- cooldown between successful mutation rolls
- `SURV_MutationThreatRollCooldownMinutes` (line 55) -- cooldown between threat rolls
- Starched Genes has rank-specific scalars: `Perk_StarchedGenes01Scalar` and `Perk_StarchedGenes02Scalar` (lines 77-78)
- Mutations with `CureWithRadAway = False` cannot be removed by RadAway (line 23)
- Mutations with `GainWithRadDamage = False` can only be gained through quests (line 25)

---

## 12. COMPANION/ALLY VISITOR SYSTEM

**Script:** `companionvisitorscript.psc`

Camp ally visitors have a hidden spawn system:
- Default `SpawnChance = 20` on a d100 roll (line 14) = **20% chance**
- `PlayerDistanceToSpawnVisitorAt = 10000.0` (line 64) -- visitor only spawns when you're within 10,000 units
- `fSpawnMapMinDistanceFromPlayers = 1000.0` (line 38) -- visitors spawn at least 1000 units away
- `fSpawnMapMaxDistance = 2300.0` (line 39) -- maximum spawn distance
- `fSpawnMapDesiredRangeFromPlayers = 1500.0` (line 43) -- preferred spawn distance
- `TimerDur_CampVisitorCheck = 3.0` seconds between checks (line 42)
- `CampRadiusVisitorMult = 2.0` (line 59) -- visitor detection area is 2x the camp build radius
- `ExpiryDay = 1.0` (line 22) -- default 1 day cooldown before same visitor can return
- `DistanceToConsiderUnloadedForDeletion = 5000.0` (line 27) -- visitors delete when you're 5000+ units away

---

## 13. DAILY OPS BOSS HEALTH BUFF

**Script:** `defaultmutation.psc` (DailyOps_Mode02)

Daily Ops minibosses get a hidden health multiplier:
- `MiniBossHealthMult = 2.0` (line 24) -- **minibosses have 2x health** on top of their base
- Wave enemies get `DailyOps_Mode02_IgnoreArmorPerk` (line 10) -- armor piercing is applied via perk, not a damage type
- Wave enemies also get `DailyOps_Mode02_ImprovedAccuracyPerk` (line 15) -- improved accuracy is a perk, not an AI change

---

## 14. EVENT SCORE MULTIPLIER (MISCHIEF NIGHT / GENERAL)

**Script:** `mn2_questscript.psc`

Events can scale rewards by player count:
- `bEnablePlayerCountMultipliers` (line 100) -- toggle for player-count scaling
- `PlayerCountMultipliers` array (line 102) -- struct with Count and Multiplier fields
- `CostumeBonusMultiplier` (line 59) -- wearing specific costumes gives bonus event progress
- `ExplosionsCompensateMultiplier = 0.0` (line 92) -- compensatory multiplier for explosion damage contributions
- `bDoubleProgress = False` (line 21) -- internal flag for double progress mode

---

## 15. FESTIVE SCORCHED LEGENDARY CHANCES

**Script:** `festive_legendaryscorched.psc`

Holiday Scorched legendary ranks are controlled by content scheduler:
- `FestiveScorchedChanceForTwoStarLegendary` -- percentage chance set server-side
- `FestiveScorchedChanceForThreeStarLegendary` -- percentage chance set server-side

These are GlobalVariables, meaning Bethesda can change them on the fly without a patch.

---

## 16. DISEASE SYSTEM HIDDEN RULES

**Script:** `surv_diseasedcreaturescript.psc`

- `MinCreatureLevelForDisease = 10` (line 20) -- **creatures below level 10 are NEVER diseased**
- Exception list: `SURV_DiseaseIgnoreMinCreatureLevelKeywords` (line 22) -- radroaches and mirelurk spawn ignore the level check
- Daily Ops creatures use a separate keyword (`DailyOpsCreatureKeyword`) and are excluded from normal disease rules

**Antibiotic perk (perkantibioticscript.psc):** Two separate chance globals: `PerkAntibioticChance1` and `PerkAntibioticChance2` per rank

**Anti-Epidemic perk (perkantiepidemicscript.psc):** Has a `Radius` GlobalVariable -- it's AOE-based, curing teammates within a radius when you use disease cure

---

## 17. RAD SPONGE HIDDEN TIMING

**Script:** `perkradspongescript.psc`

- `ReadyCheckInterval = 1.0` (line 13) -- checks every 1 second while NOT on cooldown
- `CooldownCheckInterval = 10.0` (line 15) -- checks every 10 seconds while ON cooldown
- Uses `PerkRadSpongeHealSpell` duration as actual cooldown (not the check interval)
- `Radius` is a GlobalVariable -- the AOE range can be changed server-side

---

## 18. BEEHIVE SPAWN CHANCE

**Script:** `beehivecontainerscript.psc`

When looting a beehive:
- `SpawnChance = 1.0` (line 10) -- default **100% chance** to spawn a bee swarm
- This is configurable per-beehive from 0.0 to 1.0

---

## 19. SLOT MACHINE MECHANICS

**Script:** `atxslotmachinescript.psc`

CAMP slot machines have a full probability table system:
- Each result has a `chanceThreshold` (0.0 to 1.0)
- Results have types: Loss (0), Win (1), Jackpot (2)
- 5 possible tumbler symbols total (`totalSymbolCount = 5`, line 29)
- Winning/jackpot grants `ATX_BuffLuck` spell -- **slot machine wins buff your Luck stat**
- `ATX_DispellFortifyLuck` keyword prevents stacking luck buffs

**Animation timings:**
- Spin duration: 6.5 seconds
- Win animation: 3.8 seconds
- Lose animation: 3.8 seconds
- Jackpot animation: 5.0 seconds

---

## 20. DEATH ITEM DROP SYSTEM (PITY TIMER)

**Script:** `defaultquestadddeathitemscript.psc`

Quest-specific death item drops have a built-in **pity timer**:
- `BaseChance = 10` (line 20) -- starts at 10% chance on d100
- `MaxChance = 100` (line 22) -- capped at 100%
- `BaseChanceFailureBump = 5` (line 24) -- each failure INCREASES the chance by 5%
- After 18 consecutive failures: 10 + (18*5) = 100% guaranteed drop

The chance resets back to base after a successful drop. This is a classic pseudo-random distribution system.

---

## 21. PLAYER KILLER NEMESIS SYSTEM

**Script:** `gq_playerkillerquestscript.psc`

When a creature kills a player, it enters the Nemesis system:
- `NearbyPlayerDistance = 5000.0` (line 9) -- alerts players within 5000 units
- `shutdownTimerInitialHours = 1.0` (line 19) -- non-epic nemesis despawns after 1 hour
- `shutdownTimerEpicHours = 72.0` (line 21) -- **epic nemesis persists for 72 hours (3 days)**
- Kill tracking prevents counting the same player death twice per rank (line 28)

Ties into epic creatures: `NemesisMinKillCount = 3` means a creature needs to kill 3 different players to rank up.

---

## 22. ARCADE GAME HIDDEN STAT INFLUENCE

**Script:** `arcadebottleblastertarget.psc`

The Bottle Blaster arcade game uses your **Strength** stat:
- `StrengthScoreDampener = 0.5` (line 13) -- Strength * 0.5 factor in score calculation
- Score formula (line 26): `Floor(baseScore * damagePercentDone * 10.0 * DamageScoreDampener * StrengthAV * StrengthScoreDampener)`
- Higher Strength = higher arcade scores

**Script:** `arcadecontroller.psc` -- Arcade games also reference `LuckAV` and have `bonusTicketMultiplier` for bonus ticket rewards.

---

## 23. NUCLEAR WINTER / BABYLON TEST WEAPONS

**Script:** `babylontest.psc`

Internal test script reveals 12 hardcoded weapon/ammo FormID pairs used for automated testing:

| Index | Weapon FormID | Ammo FormID | Ammo Count |
|-------|--------------|-------------|------------|
| 0 | 0x00467796 | 0x004CE87 | 100 |
| 1 | 0x00055463 | 0x0032B235 | 100 |
| 2 | 0x00110D41 | 0x0001F66A | 100 |
| 3 | 0x00011BF6 | 0x0001F66C | 100 |
| 4 | 0x0009983B | 0x000C1897 | 100 |
| 5 | 0x000FF995 | 0x001025AA | 100 |
| 6 | 0x00182634 | 0x001CF27D | 10 |
| 7 | 0x0010F0EC | 0x000C1897 | 100 |
| 8 | 0x00100AE9 | 0x0001DBB7 | 100 |
| 9 | 0x0003F6F8 | 0x000CABA3 | 10 |
| 10 | 0x0008F0EF | 0x001CF27D | 10 |
| 11 | 0x0012DBB3 | 0x0001F673 | 100 |

Also references FormID `5307850` (0x50FACA) as `BabylonBagKeyword` from SeventySix.esm (line 24).

---

## 24. GHOUL SURVIVAL MODE (UNRELEASED/INTERNAL)

**Script:** `ghl_surv_playerstatsmanager.psc`

A Ghoul-specific survival system exists:
- `GHL_SURV_Feral` actor value -- a "feral" meter that replaces hunger/thirst
- `FeralThresholdPoll` checks every **5 seconds** (line 20)
- **Respawn grace period:** `SecondsToDyingAgain = 1800` (30 minutes) (line 40)
- **Rads clamp on respawn:** `ClampRads = 900.0` (line 42) -- rads capped to 900 on death
- **Fast travel cost:** `UnitsPerSecond = 0` (line 47) -- currently disabled (no feral cost for fast travel)
- `SecondsToDyingAfterFastTravelingDamage = 300` (line 49) -- 5 minutes of damage protection after fast traveling while low on feral meter

---

## 25. CAMP ANIMAL TAMING HIDDEN MECHANICS

**Script:** `sq_animaltamingscript.psc`

Tamed animals have a hidden budget trick:
- `WorkshopBudgetObjectMultiplier` (line 22) -- used to **zero out** the budget cost of a tamed animal
- Tamed animals get recreated from a race/base lookup table when "lost" (line 8)
- `SQ_AnimalTamingTamedAnimalFlag` actor value tracks whether player has a tamed animal (for reconnection handling)

---

## 26. ENCRYPTID EVENT MECHANICS

**Script:** `timerscript.psc` (E01B_Encryptid)

- `cooldownTimeSeconds` -- GlobalVariable controlling Encryptid cooldown (configurable server-side)
- `onCooldown` -- GlobalVariable tracking cooldown state

**Script:** `assaultronbossscript.psc` (E01B_Encryptid)

The Imposter Sheepsquatch has two explicit states:
- `invulnerable` state -- changes blood impact material to `InvulnerableImpactMaterial`
- `vulnerable` state -- resets blood impact material to None

---

## 27. MISCHIEF NIGHT COSTUME BONUS

**Script:** `mn2_questscript.psc`

Players wearing items with `WearingKeyword` get a `CostumeBonusMultiplier` applied to their event progress contributions. Wearing costumes during Mischief Night literally makes the event progress faster.

---

## 28. DEVELOPER TODO/TEMP/HACK COMMENTS

**Script:** `clearactiveeffectonrespawn.psc` (line 2):
> `TEMP. DELETE WHEN 16477 IS DONE. Used to remove effects from players when they respawn. Used for crits where a player's body is destroyed.`

This is a temporary workaround for bug #16477 that was never removed.

**Script:** `powersystemdatascript.psc` (lines 57-61):
Multiple `TODO:` comments revealing player-count-based power plant scaling was **planned but never implemented** -- all multipliers left at 1.0.

---

## 29. LUNCHBOX XP STACKING PREVENTION

**Script:** `lunchboxeffectscript.psc` and `templunchboxeffectscript.psc`

- `HasLunchboxEffect_MTX` keyword (line 24/13) -- explicitly prevents stacking multiple lunchbox effects
- Each new lunchbox **dispels the previous one** before applying
- `SCORE_Lunchbox_Level` actor value tracks XP boost level (line 29)
- Party favors are randomly selected from `LunchboxPartyFavors` array
- Note the typo: `GuarenteedBuffSpell` (line 36) -- misspelled "Guaranteed"

---

## 30. MOTHMAN XP BONUS

**Scripts:** `ffz10_light_mothmanaliasscript.psc`, `e07a_mothman_wisemothmanaliasscript.psc`

Communing with the Wise Mothman grants `crXPBonusSpell` -- a hidden XP boost spell. Players are tracked in `PlayersAlreadyCommuned` collection to prevent repeated communion in the same encounter.

---

## 31. BLOODBUG SPIT ATTACK MECHANICS

**Script:** `bloodbugracescript.psc`

Bloodbugs have a hidden melee-hit counter:
- Must land between `SpitAvailableHitCountMin` and `SpitAvailableHitCountMax` melee hits
- After reaching threshold, waits `SpitWaitSeconds` before spit attack
- `BloodSuckSpell` heals the Bloodbug on each melee hit (line 23)
- If the blood sac is full and it's crippled or killed, `SacFullExplosion` detonates (line 24)

---

## 32. AMMO CONVERTER HIDDEN CAP

**Script:** `ammoconverterterminalscript.psc`

- `AmmoPointPlayerMax = 100000` (line 16) -- hard cap of **100,000 ammo points** per player
- Transaction sizes: High = 100, Medium = 10 (lines 14-15)
- Confirmation codes: BuyFail=0, BuySuccess=1, SellFail=10, SellSuccess=11, SellFail_TooCloseToMax=12

---

## 33. CHARGEN MURAL TIME-OF-DAY SYSTEM

**Script:** `chargenmural.psc`

The Vault 76 entrance mural plays different animations based on in-game time:
- 4:00 AM to 10:00 AM: "JumpMorning01"
- 10:00 AM to 6:00 PM: "JumpDay01"
- 6:00 PM to 4:00 AM: "JumpNight01"

---

## 34. DROPPED TREASURE (BOX/CRATE HUNT) PVP BUFFER

**Script:** `mtnz03questscript.psc`

The Dropped Connection event has hidden PvP mechanics:
- `iPVPLevel = 3` (line 13) -- PvP threat level 3 (highest)
- `PVPBufferTimerLength = 60` seconds (line 99) -- 60 second PvP buffer on event start
- Box overheat system with 3 levels (line 89-93): Light (1), Strong (2), Deadly (3)
- `OverheatTimerMinLength = 180.0` to `OverheatTimerMaxLength = 270.0` seconds (3-4.5 minutes) (lines 77-79)
- Warning timer: 10 seconds (line 82)
- Damage tier 1 timer: 10 seconds (line 84)
- Damage tier 2 timer: 20 seconds (line 86)
- Box cooldown: 45 seconds (line 88)
- Quest delivery tracker area shrinks in 6 steps over 180 seconds each (lines 73-75)

**Faction rewards track separately:**
- `MTNZ03_EnclaveDropOffs_Global` -- server-wide Enclave delivery count
- `MTNZ03_DIADropOffs_Global` -- server-wide DIA delivery count
- `MTNZ03_RewardMajor_Global` -- number of deliveries needed for higher tier rewards

---

## 35. SIMPLE RESPAWN SYSTEM

**Script:** `defaultsimplerespawnscript.psc`

Event creature respawn timing:
- `RespawnTimerSecondsMin = 30` (line 32) -- minimum 30 seconds between respawns
- `RespawnTimerMaxResetCount = 3` (line 33) -- timer can only be reset 3 times to prevent infinite resets

---

## 36. TRIGGERED ACTOR RESPAWN SYSTEM

**Script:** `defaulttriggerrespawnactorgroup.psc`

The world respawn system controlled by triggers has these parameters:
- `fTriggeredActorRespawnResetTimeMinutes` -- global controlling player cooldown for triggering respawns
- `fTriggeredActorRespawnOccupiedResetTimeMinutes` -- global controlling occupied area respawn time
- `fTriggeredActorRespawnMinDistanceFromPlayers` -- minimum spawn distance from players
- `fTriggeredActorRespawnMinTimeSinceDeathMinutes` -- minimum time since creature death before respawn allowed

All are GlobalVariables, meaning they can be tuned server-side without patches.

---

## 37. ENCOUNTER WAVE DIFFICULTY SYSTEM

**Script:** `defaultquestencounterwavescript.psc`

The encounter system has detailed hidden parameters:

**Difficulty levels (lines 33-40):** 0=Very Easy, 1=Easy, 2=Medium, 3=Hard, 4=Very Hard

**Subwave speed (lines 42-51):** 0=Very Slow, 1=Slow, 2=Medium, 3=Fast, 4=Very Fast, 5=Ultra, 6=Instant

**Actor skew system (lines 58-66):**
- -1: Random (default)
- 0: Fewest enemies, hardest possible
- 1: Fewer enemies, harder per enemy
- 2: Balanced
- 3: More enemies, easier each
- 4: Most enemies, easiest possible

**Player count for encounters (lines 264-271):**
- MinNumberOfPlayersOverride: minimum 2, capped at 6
- System already assumes 1 player if none detected
- Peak Difficulty Curve scales by number of players

**Boss epic chance defaults:**
- Boss-on-demand: `BossEpicChance = 1.0` (100%) (defaultquestbossondemand.psc line 47)
- Wave bosses: `BossEpicChance = 0.1` (10%) (defaultquestencounterwavescript.psc line 76)

---

## 38. GLOBAL DEBUG TRACE SYSTEM

**Script:** `defaultscriptfunctions.psc` (line 6):

```papyrus
If ShowTrace || (Game.GetFormFromFile(320332, "SeventySix.esm") as GlobalVariable).value as Bool
```

FormID `320332` (0x4E34C) in SeventySix.esm is a GlobalVariable that acts as a master debug toggle. If this value is set to True, ALL trace debug logging is enabled across the entire game. This is the dev debug switch.

---

## 39. EGG CLUSTER DEFENDER SPAWN

**Script:** `eggclustercontainerscript.psc`

- `SpawnChance = 1.0` (line 9) -- **100% chance** that a defender spawns when you loot an egg cluster
- Configurable per egg cluster instance from 0.0 to 1.0

---

## 40. EYEBOT DEATH EXPLOSION

**Script:** `eyebotactorscript.psc`

- `chanceToExplode = Utility.RandomInt(1, 2)` (line 19)
- Explodes if result == 1 (line 20)
- **50% chance** of explosion on Eyebot death

---

## 41. WHITESPRING INFINITE RESPAWN XP BLOCK

**Script:** `lc060_whitespringrespawnscript.psc`

- `BlockXPFromInfiniteRespawnEnemiesKeyword` (line 19) -- Whitespring robots that infinitely respawn are tagged with a keyword that **blocks XP from kills**, preventing the classic Whitespring XP farm.

---

## 42. AIRDROP RADIO STATION DESTRUCTION

**Script:** `gq_airdropradiostationterminalscript.psc`

- `chanceDestroyedOnLoad = 0.5` (line 8) -- **50% chance** that an airdrop radio station is already destroyed when it loads in

---

## 43. DENIZEN/NPC DIALOGUE RANDOMIZATION

**Script:** `denizendialoguescript.psc`

- `ChanceToUseSpecificLines = 50` (line 16) -- 50% chance NPCs use specific dialogue lines vs. generic ones
- The "other half" (40% if specific is 60%) is generic lines

**Script:** `denizeneffectscript.psc` / `denizensendstoryevent.psc`:
- `UseSpecialScenesChance = 50` -- 50% chance of special scene dialogue

---

## 44. BLUEFANG INTIMIDATION (BOUNTY HUNTING)

**Script:** `burn_bounty_bluefangintimidation.psc`

- `ChanceToFearOnHit = 20` (line 9) -- **20% chance** to fear enemies on hit
- `ChanceToCrippleOnHit = 10` (line 14) -- **10% chance** to cripple enemies on hit

---

## 45. FRENZY ATTACK TARGET SWITCHING

**Script:** `frenzyscript.psc`

- `SwitchTargetChance = 0.0` (line 14) -- default 0% chance to switch targets during frenzy
- Configurable per-effect from 0.0 to 1.0

---

## Summary of Most Impactful Hidden Mechanics

1. **Legendary creatures heal to full at 50% HP** -- every time, hardcoded
2. **Cap stash jackpot is 1%** with exact tier breakdowns
3. **Bomb defusal uses Intelligence (1.6x) and Luck (0.8x)** as hidden stat checks
4. **Brahmin milking uses Charisma** as the governing stat
5. **Mystery Meat triggers 3x more at max rads** than at 0 rads
6. **Power plant player count scaling was never implemented** (TODO comments)
7. **Death item drops have a built-in pity timer** (+5% per failure)
8. **Nemesis creatures persist for 72 hours** after becoming epic
9. **Creatures below level 10 cannot be legendary OR diseased**
10. **Slot machine wins buff your Luck stat**
11. **4-star legendary has a 50% chance** when a creature rolls 3-star
12. **Whitespring has an XP block keyword** for infinite respawn enemies
13. **Arcade scores use your Strength stat** as a multiplier
