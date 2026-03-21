# Finding 096: NRARC Alien Language Cipher - Developer TODO Left in Strings

## Summary

A developer TODO note was left in the FO76 string tables at FormID 0x0003C845, revealing the alien language cipher system used at the National Radio Astronomy Research Center (NRARC). The note explicitly instructs developers to "Remove actual Translations, Add alien Font Tags" -- meaning the English translations of the alien messages were never meant to ship in readable form.

## Location in Game Data

**String Table**: `seventysix_strings_en.txt`
**FormIDs**: 0x0003C843 through 0x0003C849

### The Full Cipher Text (FormID 0x0003C845)

```
[TODO: Remove actual Translations, Add alien Font Tags]
id;R9q^S(N={+Q"%6

(Long have wait arrive Stars Listen)
ACELRX

(We are going to come soon)
KLJ

(Prepare yourself, Wait)
WE

x+iK!?pl-H{C<0wF{.&^
```

### Additional Alien Messages

| FormID | Alien Text | English Translation |
|--------|-----------|---------------------|
| 0x0003C845 | ACELRX | Long have wait arrive Stars Listen |
| 0x0003C845 | KLJ | We are going to come soon |
| 0x0003C845 | WE | Prepare yourself, Wait |
| 0x0003C847 | WOPNML | Prepare yourself for Destruction of your life by Fire When you Arrive |
| 0x0003C849 | PGQVc | Life Weakens. Protect what remains here on Earth |

### Garbled/Encrypted Headers

- `id;R9q^S(N={+Q"%6` (appears before translations)
- `x+iK!?pl-H{C<0wF{.&^` (appears after translations)
- `/%^#@3.r#<3cConnection Terminated` (appears in FormIDs 0x0003C846, 0x0003C848, 0x0003C84A as transmission cutoffs)

## ESM Context

The NRARC terminals are defined in the ESM dump:
- `TERM: 0x00307BB2 NRARC_WallTerminal` - Wall-mounted terminal
- `TERM: 0x00307BB1 NRARC_DeskTerminal` - Desk terminal

Both are located at the National Radio Astronomy Research Center, a location connected to the National Isolated Radio Array (NIRA) deep space listening project.

**Important**: FormID 0x0003C845 in the ESM record structure maps to `SNDR: WPNImpactArrowStick` (a sound descriptor). The string table uses its own indexing -- the alien text at string index 0x0003C845 is associated with the NRARC terminal content, not the sound record.

## Cipher Analysis

The alien language follows a compression pattern -- each alien "word" (all caps Latin letters) maps to an entire English phrase:

| Alien | Letters | English Words | Compression Ratio |
|-------|---------|---------------|-------------------|
| ACELRX | 6 | 6 words | 1:1 |
| KLJ | 3 | 7 words | 1:2.3 |
| WE | 2 | 3 words | 1:1.5 |
| WOPNML | 6 | 14 words | 1:2.3 |
| PGQVc | 5 | 7 words | 1:1.4 |

The alien text uses ALL CAPS Latin letters (A-Z), except for PGQVc which includes a lowercase 'c'. There is no obvious letter substitution cipher -- the alien words are arbitrary symbol sequences representing entire concepts/phrases, more like logographic compression than alphabetic encoding.

The garbled text (`id;R9q^S(N={+Q"%6` and `x+iK!?pl-H{C<0wF{.&^`) uses a different character set including numbers, punctuation, and mixed case, suggesting it represents a different encoding layer -- possibly the raw signal data before translation.

## Connection to Alien Factions

### Flatwoods Monster
The Flatwoods Monster has its own creature mesh (`meshes/actors/flatwoodsmonster/`) and is a pre-war alien entity. The NRARC detected alien signals in September 2077, and the Flatwoods Monster is encountered near the same region of the map. However, there is no direct ESM link between the NRARC terminal FormIDs and the Flatwoods Monster records.

### Zetan Aliens (Invaders from Beyond event)
The Zetans are a separate alien faction added with the "Invaders from Beyond" seasonal event (E07B). They have extensive ESM entries:
- `DailyOps_ZetanInquisitorKeyword`
- `DailyOpsWaveKeyword_Zetan`
- `Music_Type_Event_Zetan`
- `ap_ZetanDrone_EyeBeam`

The NRARC signals pre-date the Zetan invasion content and likely represent a different alien civilization -- possibly the same species as the Flatwoods Monster, which uses psychic/telepathic abilities rather than the Zetans' technological approach.

### Skyline Valley Aliens (DLC04)
DLC04 includes alien animatronic content (`meshes/actors/dlc04/animatronic/characterassets/animatronicalienreplace.nif`), which are mechanical replicas rather than actual aliens.

## Community Documentation Status

The Fallout Wiki at fallout.wiki documents these terminal entries on the [NRARC terminal entries page](https://fallout.wiki/wiki/National_Radio_Astronomy_Research_Center_terminal_entries), including the alien text and translations. However, the wiki presents them as in-game content without highlighting the developer TODO note as evidence of incomplete implementation. The TODO note itself -- the instruction to remove translations and add alien font tags -- is the real finding: it proves the alien language was designed with a real cipher system that was meant to be obscured behind custom font rendering, and the developers forgot to strip the human-readable translations from the shipping build.

## Implications

This is a rare case of developer process notes shipping in production data. The TODO reveals:

1. **The alien language has real translations** -- it's not random gibberish
2. **A custom alien font was planned** -- "alien Font Tags" implies a rendering system that would display the text in alien glyphs
3. **The translations were supposed to be hidden** -- players were meant to see alien symbols, not English
4. **The implementation was never completed** -- the TODO was never acted on
5. **Multiple encoding layers exist** -- garbled ASCII text alongside the clean alien->English mappings suggests a multi-stage decryption concept

This represents either cut content (the alien font system was abandoned) or an oversight (the TODO was forgotten during the content pipeline).
