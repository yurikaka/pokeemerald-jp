# Game Corner exchange window separation

Reference: `../pokeemerald_wokann_dev`, branch `dev`:

- `data/maps/MauvilleCity_GameCorner/scripts.inc`: prize menus 48/55 at
  (12, 0); coin box at (1, 1). Purchase menu 49 starts at (15, 0), alongside
  money and coin windows.
- `src/script_menu.c`: `GetLengthWithExpandedPlayerName` counts bytes, not
  displayed Chinese glyphs or control sequences. `CreateWindowFromRect`
  adds one to x/y and uses tile base 0x5c. Removal clears the menu/frame;
  it does not reconstruct another window covered by that menu.
- `src/coins.c`: coin window width 8, height 2, tile base 0x136, text x=8.
- `src/text.c`: SHIFT_RIGHT sets currentX to initialX plus its argument.

Original JP prize strings produce width 16. Before this fix Chinese dolls
produced width 22 and moved left from 12 to 6; TM strings produced width 18
and moved left to 10. Dolls therefore covered the coin window, and removing
that menu erased the covered coin-window map area, explaining both screenshots.

Preserve prize labels and their spacing. Actual native printing
confirms doll labels end at x=132, TM labels at x=136. Use 17 tiles at
(11, 0), rather than 22 at (6, 0): frame columns 11..29 stay onscreen.
At the user's subsequent request, standardize the balance label from
`枚代币` to `代币`, matching the prize prices (`Chs_gText_Coins`). This
shorter label fits the native 8-tile coin window with its original x=8
inset. Keep the native allocation at 0x136 and its frame at columns 0..9.
The largest prize menu ends at tile 0x128, so allocations do not overlap.
The native number formatter still right-aligns the numeric portion in a
four-character field; the whole string is not right-aligned to the window.

Purchase menu 49 has a different adjacent window: the original money frame
spans columns 0..13. Its unchanged labels need 120px, so use 15 tiles at
(13, 0), rather than byte-counting 18 tiles at (10, 0). At the user's
request preserve original top alignment, shrinking the shared field money
window from 12 to 11 tiles and shifting its numeric text inset from 40 to
32 pixels. The label sprite occupies screen x=3..34; numeric text begins
at screen x=40, leaving a 5px gap. Even 999999 yen ends at window x=88.
The money frame now ends at column 12, before the purchase menu at 13.
No text, font, letter spacing, numeric right alignment or saved data changes.

No script, save, coin value, prize, payment or removal routine changes.
Only multichoice window width/position, field money window width/amount
inset, and the coin unit wording change.
Native coin sizing, text inset, number conversion and tile base are restored
byte-for-byte (the earlier widened coin window is no longer necessary).

Verification:

- `verify_game_corner_windows.py` executes the native menu entry, native
  byte-width measurement and installed adapter in Unicorn for menus 48/49/55.
  It checks rectangles, frame separation and tile allocation separation.
  It also executes the actual native text printer, installed CHS renderer
  and CopyGlyphToWindow for every menu label and several four-digit balances,
  checks actual glyph extents and a sentinel after the window pixel buffer,
  verifies native four-digit right alignment for 0/9/50/500/6789/9999,
  and verifies the native coin printing/allocation/removal instructions.
  It also executes native money-window template construction and amount
  inset setup, renders 0/9/1000/10000/999999 in the 88px window, and checks
  the label sprite and top-aligned purchase menu remain separate.
- `verify_vending_menu.py` passes, including all 113 native menu entries and
  existing reporter/elevator/vending/Frontier rule regressions.
- `make -j1 chs` succeeds. No live game screenshot test performed.
