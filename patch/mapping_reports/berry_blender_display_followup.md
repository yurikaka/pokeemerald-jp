# Berry Blender display follow-up

Verified against Wokann dev `src/berry_blender.c` and the Japanese base ROM.

- `Blender_PrintPlayerNames`, `0x08080250`: the original link-player name is
  copied to `sp + 8` before printing. Resolve the NPC display name before this
  copy, since the printer resolver intentionally accepts only original NPC
  name-slot pointers. Preserve player and linked-player names.
- `Blender_CopyBerryData`: stores the item ID at offset 0 and the Japanese
  berry name at offset 2. Each cached berry occupies 16 bytes.
- `Blender_PrintBlendingResults`, `0x08082FDC`: `r4` points to the cached
  berry name (state offset `0x15A` plus player index times 16). Read the item
  ID at `r4 - 2` and copy its full Chinese item name to the existing display
  buffer at state offset `0x9F`. Resume at `0x08082FEC`, skipping the old
  suffix append because Chinese item names already include the berry suffix.

Neither hook changes link-player storage, cached berry data, save data, or
NPC-name initialization. The original Japanese name block remains intact.

## Made-Pokeblock message

Wokann `Blender_PrintMadePokeblockString` appends these fragments in order:
name, `0x0830F6FD` (completion phrase), `0x0830F849` (newline), level,
feel, `0x0830F860` (Japanese sentence ending), and paragraph break.

Batch 427 incorrectly redirected the newline literal at `0x0808333C` to
the Chinese completion phrase, leaving the original Japanese completion
phrase intact. Move this reference write to `0x08083338`, restoring the
original newline. This separates the name/completion line from the
level/feel line instead of letting them run beyond the window and damage
other lines. Replace the Japanese `だ` ending at `0x08083348` with the
US Chinese message's period (`sText_Dot2`). Keep the paragraph break intact.

Wokann `Blender_AddTextPrinter` already clears the full window through
`FillWindowPixelBuffer` for the dialog's color mode 0. No additional window
clearing hook is needed; the malformed single-line message was overflowing
the window's layout. Emulator confirmation of the reported residual is
still required.
