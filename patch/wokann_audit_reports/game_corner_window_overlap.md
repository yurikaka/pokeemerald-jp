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
confirms doll labels end at x=132. Use 17 tiles at (11, 0), rather than
22 at (6, 0): frame columns 11..29 stay onscreen.
At the user's subsequent request, replace the five `TMnn` prize labels
with normal-font `招式学习器nn`. Subsequently widen this menu by one more
tile to increase the name/price gap: the name ends at x=84 and price begins
at x=96 (SHIFT_RIGHT 88), leaving 12px instead of 4px. Four price digits
and two Chinese unit glyphs end at x=152, so this menu uses 19 tiles at
(9, 0). Its frame starts after the narrowed coin frame ending at column 8.
Its tile data ends at 0x140; relocate coin tiles from 0x136 to 0x140 to
avoid a VRAM overlap. At the user's subsequent request, dolls also use
19 tiles at (9, 0), matching the TM menu's edges. Subsequently replace
the single space after each doll name with SHIFT_RIGHT 88, matching the
TM price column at x=96. All three 1000-coin prices now end at x=152,
right-aligned with the TM prices; names and fonts remain unchanged.
At the user's subsequent request, standardize the balance label from
`枚代币` to `代币`, matching the prize prices (`Chs_gText_Coins`). This
shorter label needs 56px at most, so reduce the coin window from 8 tiles
to 7 and remove the original x=8 inset (now x=0). Its frame spans columns
0..8. The 14 coin tiles start at 0x140, after the largest prize menu.
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
inset, coin window width/text inset/tile base, coin unit wording, and TM
prize labels/price alignment change. Coin number conversion, four-digit
right alignment and the window removal routine remain native.

Verification:

- `verify_game_corner_windows.py` executes the native menu entry, native
  byte-width measurement and installed adapter in Unicorn for menus 48/49/55.
  It checks rectangles, frame separation and tile allocation separation.
  It also executes the actual native text printer, installed CHS renderer
  and CopyGlyphToWindow for every menu label and several four-digit balances,
  checks actual glyph extents and a sentinel after the window pixel buffer,
  verifies native four-digit right alignment for 0/9/50/500/6789/9999,
  and verifies native coin window construction (7x2 tiles at base 0x140),
  printing inset (x=0), and unchanged removal instructions.
  It also executes native money-window template construction and amount
  inset setup, renders 0/9/1000/10000/999999 in the 88px window, and checks
  the label sprite and top-aligned purchase menu remain separate.
- `verify_vending_menu.py` passes, including all 113 native menu entries and
  existing reporter/elevator/vending/Frontier rule regressions.
- `make -j1 chs` succeeds. No live game screenshot test performed.
