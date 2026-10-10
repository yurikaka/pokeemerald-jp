# Frontier BP price columns

`kt2.png` shows BP prices clipped at the right edge. Imported US CLEAR_TO
positions assumed 6-pixel Latin text, while JP-mode prices use 8-pixel glyphs.
The existing converter maps CLEAR_TO to native SHIFT_TEXT without changing
the argument; SHIFT_TEXT adds the argument to the printer's initial x.

Checked against Wokann `dev`, `src/field_specials.c`,
`ShowScrollableMultichoice` (0x0813A164): menu IDs 3-6 have 15-tile windows,
and tutor menu IDs 9-10 have 14-tile windows. The native list template at
0x03005F10 uses item x=8. Its source names table is 0x0859274C, stride 64.
JP `asm/text.s` at 0x08005A3C confirms SHIFT_TEXT's initial-x origin.

Only the 50 price-text positions in batch 438 change:

- Exchange prices: 1-digit BP at 88, 2-digit BP at 80, 3-digit BP at 72.
- Tutor prices: 2-digit BP at 72.

Every price ends at its window's right edge. Names, amounts, windows and
exchange logic remain unchanged. `verify_frontier_bp_prices.py` runs the
native menu setup, price-width calculation and SHIFT_TEXT opcode, and measures
name glyph advances through the Chinese renderer for all 50 entries. It
checks complete prices, right alignment and no overlap with names.
