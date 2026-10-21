# Pokeblock Case labels and Berry Blender start sprite

Address evidence comes from `../pokeemerald_wokann_dev` on branch `dev`.

- `src/pokeblock.c`, `sub_08135C88`: literal `08135CE4` loads the compressed
  menu graphics at `08D9B4B4`. `src/graphics.c` binds these to
  `graphics/pokeblock/menu.png.4bpp.lz`. The generator verifies this base asset,
  edits only the eight feel-label tiles, and preserves the Japanese tilemap
  and frame. The replacement label is `细腻度`.
- `sub_08135DF8` uses `08135E50` and `08135E5C` for the dry and sour labels.
  These become `涩味` and `酸味`. Together with the existing spicy, sweet and
  bitter translations, each label occupies 24 pixels in its 24-pixel window.
- `src/berry_blender.c`: `0807F3EC` loads sprite sheet `gUnknown_830FB48`.
  Its initializer is `{data=0830E5B4, size=0400, tag=303A}`; the following
  template at `0830FB50` references this tag and the 64x32 OAM at `0830FB34`.
  `src/data/berry_blender.h` preserves the source sprite and palette within
  `graphics/berry_blender/jp/830d794.bin`.
- The start generator checks that source blob and sheet header, then converts
  the Chinese reference `graphics/berry_blender/start.png` to raw 4bpp tiles.
  Its 64x32 size and all 16 palette entries match the Japanese resources.
  Only the sheet's data pointer at `0830FB48` is redirected. Native animation,
  sprite dimensions, tag and palette remain in use.

Validation: successful `make chs`; output ROM sprite pixels match the Chinese
PNG, the sheet size/tag/template and palette match the base ROM, the Pokeblock
graphics match the generated tiles, and its original tilemap is preserved.
No in-game emulator verification was performed for this change.
