# Frontier floor corruption (kt1)

Wokann `data/layouts/layouts.json` identifies the 72x72 Frontier east
exterior as General plus BattleFrontierOutsideEast tilesets.
`data/tilesets/headers.inc` fixes the east header at `0x083B7C8C`; its
tile pointer is `0x08326A04`. The compressed resource matches Wokann
`data/tilesets/secondary/battle_frontier_outside_east/tiles.4bpp.lz`
byte-for-byte in the vanilla ROM and occupies 5024 bytes.

Batch 227 mistakenly overwrote `0x0832757E` within that compressed
stream. Its four bytes happened to equal `0x08223411`, the dialogue
address, but were compressed image data, not a pointer. This changed
6034 of the 16256 decompressed bytes in the tested build, starting in
tile 301 and corrupting many subsequent tiles through LZ backreferences.

Remove only that false reference write. Preserve the genuine script
pointer at `0x08222BA6`, which follows the `0F 00` loadword command in
`BattleFrontier_OutsideEast_EventScript_Camper`. Wokann scripts confirm
that it displays `BattleFrontier_OutsideEast_Text_StickyMonWithLongTail`.
Thus its Chinese dialogue remains active while original artwork is restored.

The historical batch mapping report remains unchanged as provenance;
this follow-up records why the extra raw-byte match must not be patched.
Run `python3 patch/tools/verify_frontier_map_graphics.py` after building
to check the east, west and General tile resources and decompressed artwork.
