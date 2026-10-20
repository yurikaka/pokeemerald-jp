# Factory rental species-name position

Cross-checked against `pokeemerald_wokann_dev` branch `dev`,
`src/battle_factory_screen.c`, `Select_PrintMonSpecies` (0819B688) and
`gUnknown_85DBC3C` window templates.

Window 1 at 085DBC44 is BG 0, tileLeft 24, tileTop 2, width 8, height 2,
palette 14, baseBlock 17. Its original x=192 leaves only 48 visible pixels.
Move tileLeft to 22 (x=176), keeping its size, tile allocation and all other
windows intact. Its 64-pixel width now ends at the screen edge, x=240.

Replace Select_PrintMonSpecies at 0819B688 with
ChsFactorySelectPrintMonSpecies. Preserve the original window clearing,
selected-Pokemon species lookup, species-token copying, font/colors/y/speed
and VRAM update. Replace Japanese byte-length positioning with a width scan
of ChsSpeciesNames: Chinese pairs occupy 12 pixels, single-byte characters
conservatively occupy 8 pixels. The screenshots additionally show that the
decorative diagonal occupies the left side of this window; the clear name
area starts around x=188. Five-character names therefore use the existing
ChsWriteNarrowSpeciesName helper with threshold 5, which emits F5 F3, the
complete name, then F5 F4 to restore the regular font. Budget 8 pixels per
narrow character, including mixed digits. Three/four/five Chinese glyphs
begin at screen x=200/188/196 respectively, with right edges at most x=236.
Short names retain the standard font and their previous alignment.

An ARM runtime check executed the installed JP entry for all 412 species,
capturing the native printer's window/font/x/y/text parameters. All names
fit and their measured right edges are at most x=236. The existing shared
display regression check also passes. These checks are not an interactive
GBA playthrough.
After the font correction, the actual native printer also rendered every
five-character species into an 8-by-2-tile window. Captured glyph positions
and glyph widths all stayed within the clear x=188..236 area, with the full
expected glyph count, including mixed-digit names.
Species names, rental generation, stored Pokemon and selection state are
unchanged. No stashed Easy Chat or Trainer Hill changes are restored.
