# FO76 Finding 002: Atlantic City Full Casino System

## Status: CONFIRMED — Casino furniture, gambling tables, slot machines, weather control (SHIPPED via America's Playground)
## Source: seventysix_strings_en.txt, translate_en_utf8.txt

## Casino Furniture Found In Files
- `Atlantic City Slot Machines` [41008C9A]
- `West Virginia Slot Machine` [41003FF2] + craftable plan
- `Atlantic City Dice Table` [410091BB]
- `Atlantic City Roulette Table` [410091BC]
- `Atlantic City Poker Table` [41009D41]
- `Atlantic City Black Jack Table` [41009D42]
- `Atlantic City Casino Counter` [41009FD3]
- `Atlantic City Bar Stool` [4100A138]
- Casino wallpapers: Royal, Cobalt, Lilac, Mahogany variants
- `Casino Quarter Roof` [41008E52] — an entire casino district zone

## Casino Gaming — Shipped with Region Lock
- `$CASINO_ERROR_CASINO_DISABLED` — "Casino games are currently unavailable"
- The casino games SHIPPED and are playable in the America's Playground (Atlantic City) content
- The "disabled" flag is a region-lock mechanism — casino games are only available within the Atlantic City expedition area, not in the broader Appalachian map
- The error message displays when players attempt to use casino furniture outside the valid region

## Weather Control
- `Weather Control Station (Atlantic City Fog)` [41008640]
- `Weather Station (Atlantic City Fog)` [41008642]
- Atlantic City has its own weather system separate from Appalachia

## The Overgrown Faction
- Plant-based enemies specific to Atlantic City
- Quest: "Loot the evidence from the Overgrown"
- NPCs reference them: "Leafy hooligans? That sounds a lot like the Overgrown"
- They've somehow spread to Appalachia: "How did the Overgrown end up in Appalachia?"

## Gambler Title
- `Gambler` [41008635] — likely a player title earned through casino content

## Implications
The casino gambling system shipped as part of the America's Playground (Atlantic City) expedition content. The "disabled" error is a region-lock that restricts casino games to the Atlantic City area. The CAMP-placeable casino furniture (slot machines, tables) triggers this error outside the expedition zone, which is likely a regulatory compliance measure — keeping gambling mechanics contained within a specific game context rather than allowing them in the persistent open world where microtransactions are active.
