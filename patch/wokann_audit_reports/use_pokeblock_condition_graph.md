# Use Pokeblock condition screen graphics

Verified against `../pokeemerald_wokann_dev`, branch `dev`:

- `src/use_pokeblock.c`, `sub_08168050`: literal `08168090` points to the
  compressed title at `085BEBC0`. The native sprite sheet is `0x800` bytes;
  two 64x32 sprites use animation tile offsets 0 and 32. Its palette is
  `USE_POKEBLOCK_CONDITION_PAL`, `085BEBC0 + 0x174 = 085BED34`.
- The background loader decompresses graph tiles through literal `081678AC`
  (`085BFAAC`), then loads exactly `0xFA0` bytes at BG tile offset `0x280`.
  Literal `081678CC` supplies its 1280-byte tilemap (`085C0230`).
- `data/data_b2d_mid70.s` declares these raw resource ranges. The generator
  checks them against the Wokann base ROM before producing replacements.
- The Chinese title comes from the Chinese reference's
  `graphics/pokeblock/use_screen/condition.png`; its palette matches JP.
  The inner graph and Chinese labels come from that directory's `graph.png`
  and `graph.bin`, remapped to JP color roles. Pixels outside the inner graph
  rectangle `(100,38)..(211,133)` retain the original JP artwork.
- Tile deduplication keeps the graph within its native `0xFA0` byte budget.
  JP tiles 115..124 and shared fill tile 5 retain their original indices and
  contents for the separate nature-window tilemap at `085C0410`.
  The stat overlay tilemap at `085C0488` remains unchanged.

Validation: successful `make chs`; verified all three installed compressed
resources, all 30,208 pixels outside the graph rectangle, preserved shared
tiles, nature-window map and stat overlay map. Visually inspected the composed
Chinese background. No in-game emulator verification was performed.

## Shared Return button

Wokann `src/menu_specialized.c`, `sConditionSelectionIconsSheets[2]`,
contains `{gPokenavConditionCancel_Gfx, 0x100, 102}`. The sheet table is
referenced by `LoadConditionSelectionIcons` at `081D284C`; its third pointer
at `085FA8D0` points to `085F9C38`. This matches
`graphics/pokenav/condition/cancel.4bpp`. Its palette at `085F9AF8` matches
`cancel.gbapal`. The Use Pokeblock sprite creator overrides the generic OAM
to 32x16, as does the PokeNav condition screen.

The replacement uses the US reference's 32x16 `cancel.png`, including its
original CANCEL lettering, frame and transparent padding. US text palette
index 15 is remapped to native JP index 1, preserving the native frame/text
color role; indices 0 (transparent) and 2 (fill) remain unchanged. Sheet size,
tag, OAM and selection logic are unchanged. Both selected and unselected
palette data and descriptors are checked against the native ROM.
