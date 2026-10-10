# Multichoice window bounds

`kt1.png` shows the Battle Tower reporter's menu extending past the right
edge of the screen. Its event requests menu 109 at (16, 4). The translated
entries produce a 15-tile window, putting its right frame at column 32.

Provenance checked against `../pokeemerald_wokann_dev` branch `dev`:

- `data/maps/BattleFrontier_BattleTowerLobby/scripts.inc`: reporter event uses
  `multichoice 16, 4, MULTI_BATTLE_TOWER_FEELINGS, FALSE`.
- `src/script_menu.c`, `DrawMultichoiceMenu`: the existing hook at 0x080E1458
  invokes `CreateWindowFromRect`, with left in r4, top in r5, width in r2,
  row count in r6, and menu ID in sb. The continuation is 0x080E1460.
- `CreateWindowFromRect` at 0x080E1F10 adds one tile to both coordinates.
  Including its frame, a window must satisfy `left + width + 1 <= 29`
  on the 30-column screen.

The existing vending adapter is now `ChsMultichoiceMenuWindow`. It moves
overflowing menus left to `28 - width`, retaining their width, height and top.
Fitting menus keep their position. The vending menu keeps its dedicated
(14, 0, 14, 8) layout to avoid the money window.

The reporter now uses (13, 4, 15, 8), with its right frame at column 29.
`verify_vending_menu.py` runs the actual reporter, elevator and vending entry
paths, all 113 native menu table entries (0 through 112), and a matrix of
window positions and widths. It also checks stack/register preservation.
This validates native ARM execution and geometry; it is not an emulator
screenshot comparison.
