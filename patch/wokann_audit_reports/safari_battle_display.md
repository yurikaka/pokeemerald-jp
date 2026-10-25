# Safari battle display

Cross-referenced Wokann `dev` before adding address hooks:

- `battle_controller_safari.c`: `SafariHandleChooseAction` uses
  `gText_SafariZoneMenu`, the ordinary native action-menu printer, and cursors.
- `battle_interface.c`: `AddTextPrinterAndCreateWindowOnHealthbox` at
  `0x080741E0` and `UpdateLeftNoOfBallsTextOnHealthbox` at `0x08074320` use the
  independent single-byte `RenderTextFont9` path. The count reads
  `gNumSafariBalls` at `0x02039D18`. Their only update branch is Safari healthboxes.
- `CreateSafariPlayerHealthboxSprites` uses two square sprites with the second
  object's tile index at +64. The Wokann compressed healthbox graphics match
  the Japanese base ROM at `0x08C1F98C` exactly.

Batch 438 previously retained the US menu's 56px right-column position and a
48px Chinese Pokeblock label in the JP 80px window. The Safari-only layout now
widens the menu to 96px, preserving the full 宝可方块 label. The right column
uses the same 48px offset as the ordinary translated action menu. Other labels
are 狩猎球, 靠近, and 逃跑. Action IDs and directional navigation are unchanged.

The window layout is verified against `data/data_b2.s` at `0x082EB870` and
`BattleInitBgsAndWindows` in `battle_bg.c`. The Safari copy moves window 2 left
two tiles (19 to 17), increases its width (10 to 12), and reduces prompt window
1 to 13 tiles. Its base block moves from `0x1B8` to `0x1C0` to avoid overlapping
the larger menu; the combined tile allocation ends at the same `0x1F4`.
The native table is used unchanged outside Safari battles.

The native frame map at `0x08C00530` moves its left edge from column 17 to 15
only in Safari. Both `LoadBattleTextboxAndBackground` and case 1 of
`LoadChosenBattleElement` apply the change, including returning from the
Pokeblock case. Cursor draw/erase routines are cross-referenced against
`battle_controller_player.c`: Safari cursors move left two tiles, while the
ordinary battle coordinates, tile IDs, palette, and copy dimensions remain
unchanged. No static frame or window table is globally replaced.

`safari_display.c` replaces the two Safari-only drawing routines. It uses a
temporary window and the existing Chinese small font (10px advance, 13px high),
then copies 狩猎球 and 剩余NN个 into the healthbox interior. The palette remains
background 2, foreground 1, shadow 3. Each update replaces the complete count
rectangle, so changing from two digits to one cannot leave old glyphs behind.
VRAM writes use halfwords, preserving adjacent pixels and the frame. No
encounter, ball-consumption, save, or ordinary battle logic changes.

Validation: `verify_safari_display.py` executes both hooked native entry points
and the native action-menu printer under Unicorn. BIOS copies and temporary
window allocation are substituted; actual font rendering and VRAM pixel writes
execute. Counts 30, 29, 10, 9, 1, and 0 all match fresh renders; pixels outside
the text rectangles remain identical to the native frame. The generated menu
and healthbox previews were visually checked. `make compare` also passes.
Additional layout checks exercise the three actual veneers, both frame-load
paths, all four cursor draw/erase positions, and normal/Safari battle flags.
They verify that ordinary templates and frame maps remain byte-identical and
the menu/prompt tile allocations do not overlap.
Full emulator gameplay has not been exercised by this test.

## Temporary window alignment follow-up

The runtime screenshot showed only strips of the healthbox glyphs. The constant
window template was a byte array at an address ending in `0x6E`. Native
`AddWindow` copies it using two word LDR instructions at `0x08003368` and
`0x0800336A`. ARM7 unaligned word loads rotate the aligned word, corrupting
window metadata and making the renderer's tile stride differ from the copy
stride. The template now explicitly uses four-byte alignment, as does the
copied battle-window table. The earlier test substituted the entire template
with a correct mock and therefore missed this defect. Its allocation substitute
now checks pointer alignment, reads the actual template bytes, and uses a late
window slot (24), like a running battle.

The screenshot also confirmed that the 112px menu had 16px of unnecessary
right padding. The current 96px menu fits the full Chinese label at a 48px
column offset; its border and cursors move left only two tiles from native.
