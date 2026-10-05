# Storage menu follow-up

## Box-title spacing

Wokann `frontier_pass.c::sub_080C66A4` splits raw strings into four-byte
chunks rendered to separate 32-pixel sprites. The translated default BOX
prefix contains a leading language control, so the first chunk contains
the control and BO, while X starts in the next sprite. Skip a leading
Japanese/English language control only at the two box-title drawing calls
in `sub_080CC3C4` and `sub_080CC57C` (hooks `0x080CC4CC`, `0x080CC660`).
Forward the original scratch-buffer stack argument and leave the shared
renderer, saved box name, trade callers and title animation unchanged.

Verified against Wokann dev `src/pokemon_storage_system.c` and
`src/data/pokemon_storage_system.h`.

- `LoadPSSMenuGfx` loads compressed menu artwork `gUnknown_854BF9C` from
  `0x0854BF9C`. The literal is at `0x080C9908`. Redirect only this literal
  to the US Chinese menu artwork. Both sheets contain 4608 bytes of tiles;
  the Japanese decompressed display tilemap at `0x0854BDC0` is byte-identical
  to the US `display_menu.bin`. Keep the Japanese tilemaps and palettes.
- The artwork contains the Pokemon-data heading, party button, close-box
  button and return label shown in hz1/hz2. No box names are changed.
- `SetMenuText` reads `gUnknown_855657C` as a 39-entry pointer table.
  Comparing base and patched ROMs found five unchanged entries: Summary,
  Jump, Give (two slots), and Info. Batch 497 redirects these pointers to
  the corresponding US Chinese `gPCText_*` text. Other entries were already
  redirected by batch 436.
- The menu stores a pointer and action ID separately. These replacements
  only change display strings, not action IDs, saved names or Pokemon data.

`sub_080C9F68` loads the party menu map through the literal at `0x080C9FE0`.
The US and Japanese decompressed maps are both 528 bytes and differ in only
ten entries in the last two rows (indices 240 through 263), which form the
return-button footer. Redirect this map to its US counterpart so that the
footer uses the matching Chinese sheet tiles. Pokemon-slot rows, separate
empty/filled-slot maps, dimensions, coordinates and animation logic remain
unchanged.
