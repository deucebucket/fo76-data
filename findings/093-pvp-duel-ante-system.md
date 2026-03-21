# FO76 Finding 093: PvP Duel System with Betting/Ante Mechanics

## Status: CONFIRMED (in binary, not in retail gameplay)
## Source: dev_feature_deep_dive.json, dev_interesting_strings.json

## overview

the fo76 engine contains a fully implemented PvP duel system with real-stakes betting. players could challenge each other, put up an ante (a caps bet), and fight for the pot. the system includes server-side caps escrow, a house cut ("AnteServerCut"), bounty hunting with rewards, revenge mechanics with comeback bonuses, and dedicated quest infrastructure. while basic PvP exists in retail fo76, this structured duel-with-betting system was never exposed to players.

## the duel protocol

the entire system is implemented in a dedicated source file:
```
e:\buildagent\work\820e97cc99338fb0\project76\game\network\activeduelsmessages.cpp
```

it uses a client-server message protocol through `ActiveDuelClientMsg` and `ActiveDuelServerMsg`.

### duel flow (reconstructed from message data)

**1. challenge phase**
```
Data.Challenging.ChallengedId — who you're challenging
Data.Challenging.RequesterId — who initiated
Data.Challenging.Ante — the caps bet
Data.Challenging.AnteServerCut — server's percentage cut
```

one player challenges another and sets an ante amount. the server calculates its cut (a percentage of the pot).

**2. request/acceptance phase**
```
Data.Requesting.RequesterId — original challenger
Data.Requesting.ChallengedId — target player
Data.Requesting.Ante — the agreed bet
Data.Requesting.AnteServerCut — server's cut
Data.Accepting.RequesterId — original challenger (confirmed)
Data.Accepting.AccepterId — accepting player
```

the challenged player can accept or decline. both sides agree to the ante amount.

**3. active duel (scoring)**
```
Data.Scoring.RequesterId — player A
Data.Scoring.AccepterId — player B
Data.Scoring.RequesterScore — player A's score
Data.Scoring.AccepterScore — player B's score
Data.Scoring.AnteReward — caps from the ante pot
Data.Scoring.BonusReward — bonus caps (performance-based?)
Data.Scoring.Comeback — comeback bonus flag/multiplier
Data.Scoring.AnteServerCut — server's cut deducted
Data.Scoring.BonusServerCut — server's cut of bonus
Data.Scoring.BountyReward — additional bounty reward
```

the duel tracks score (kills? damage?). the winner gets the ante reward plus any bonus. the server takes its cut from both the ante and the bonus. there's a "comeback" mechanic that rewards players who rally from behind.

**4. ending**
```
Data.Ending.RequesterId — player A
Data.Ending.AccepterId — player B
Data.Ending.RequesterScore — final score A
Data.Ending.AccepterScore — final score B
DuelEndReason — why it ended (timeout? death? forfeit?)
```

**5. revenge system**
```
Data.Revenge.Revenger — the player seeking revenge
Data.Revenge.Target — who they're targeting
Data.Revenge.RevengerId — ID of revenger
Data.Revenge.TargetId — ID of target
Data.Revenge.AnteReward — revenge ante payout
Data.Revenge.RevengeReward — bonus for completing revenge
Data.Revenge.Comeback — comeback multiplier for revenge
```

after losing a duel, players could initiate a revenge match with its own separate reward structure. the revenge system even has its own comeback bonus.

## bounty hunting integration

the duel system ties into a bounty system with multiple quest stages:

| quest editor id | purpose |
|----------------|---------|
| SQ_Bounty_Parent | parent quest managing all bounty mechanics |
| SQ_Bounty_Wanted | player becomes wanted (from PvP murder) |
| SQ_Bounty_Murder | murder bounty quest |
| SQ_Bounty_MostWanted | escalated wanted status |
| SQ_Bounty_Assault | assault bounty quest |
| GQ_Bounty_Revenge | global revenge bounty |

each quest has scenes, scripts, and warning systems:
```
Quests::SQ_Bounty_Parent::Scenes / Scripts / Warning
Quests::SQ_Bounty_Murder::Scenes / Scripts / Warning
Quests::SQ_Bounty_Wanted::Scenes / Scripts / Warning
Quests::SQ_Bounty_MostWanted::Scenes / Scripts / Warning
Quests::SQ_Bounty_Assault::Scenes / Scripts / Warning
Quests::GQ_Bounty_Revenge::Scenes / Scripts / Warning
```

### bounty caps tracking

```
Snapshot.iBountyCaps — how many caps are on your head
Snapshot.iPlayerPlacedBountyCaps — caps from player-placed bounties
BountyState — current bounty status
$BountyPlayerPlaced — notification when a player puts a bounty on you
$PlayerStatBountyCollected — stat tracking: total bounties collected
$PlayerStatBountyCollectedTooltip — tooltip for bounty stat
$PlayerStatTimeWanted — stat tracking: total time spent wanted
$PlayerStatTimeWantedTooltip — tooltip for wanted time stat
```

these stats would have appeared in the player's stat page, tracking lifetime bounty earnings and time spent as a wanted criminal.

### bounty network protocol

```
RequestPlaceBountyMsg — request to put a bounty on someone
PlayerPlacedBountyMsg — notification that a bounty was placed
Data.BountyReward.WantedId — who has the bounty
Data.BountyReward.KillerId — who collected it
Data.BountyReward.BountyReward — the payout
```

players could place bounties on other players, and anyone could collect. the system tracks who placed it, who's wanted, and who collects.

## the server cut mechanic

one of the notable details is `AnteServerCut` and `BonusServerCut`. the server takes a percentage of every duel bet and every bonus reward. this functions as a caps sink — it removes currency from the economy with every duel. bethesda built a casino-style house edge into the PvP system.

this makes economic sense for an MMO: PvP betting without a house cut would be a neutral transfer (caps move between players but total economy stays the same). with a server cut, every duel removes caps from circulation, counteracting inflation.

## what shipped vs what was built

the live game has a simplified PvP system:
- slap damage (reduced damage until both players engage)
- wanted/bounty status for killing non-hostile players
- pacifist mode toggle
- basic revenge spawning after death

the built-but-unused system adds:
- structured duel challenges with wagering
- server-managed caps escrow
- house-cut economics
- score-based outcomes (not just first-to-kill)
- comeback mechanics rewarding rallies
- revenge chains with their own reward structure
- stat tracking for bounty hunting careers
- player-placed bounties

## PvP event data model

the interface layer for this system is implemented in:
```
e:\buildagent\work\820e97cc99338fb0\project76\game\interface\data\pvpeventdatamodel.cpp
```

this file handles the UI side — displaying duel challenges, ante amounts, scores, and results to both players.

## why it was never enabled

fo76's PvP history is well-documented: the community overwhelmingly rejected aggressive PvP. nuclear winter (the battle royale mode) was removed. survival mode servers were removed. the slap damage system was added specifically to prevent unwanted PvP. enabling a high-stakes betting duel system would have been tone-deaf to the playerbase.

the system was almost certainly built pre-launch or very early post-launch when bethesda still envisioned fo76 as a more competitive multiplayer experience. as the community pushed hard toward cooperative PvE gameplay, the duel system became dead code.

the irony is that the system is well-designed: the house cut prevents economic exploits, the comeback mechanic prevents stomps from being unfun, and the revenge system gives losers agency. if the community had wanted PvP, this would have been a solid foundation.
