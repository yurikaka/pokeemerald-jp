# Pokenav unvisited city name display

## Symptom and cause

Moving the region-map cursor onto an unvisited city, including Lavaridge Town
(釜炎镇), can leave the name area empty. The Chinese name table is valid;
the error is in the Chinese city-window clearing hook.

`ChsRegionMapCityWindowFillB` resumes at `0x081CC2DC` (Thumb target
`0x081CC2DD`). The eight-byte veneer at `0x081CC2D8` occupies
`0x081CC2D8..0x081CC2DF`, so this resumes inside its pointer literal.
The correct next instruction is at `0x081CC2E0` (Thumb target `0x081CC2E1`).
The visited-city branch already resumes at its correct continuation.

## Reference verification

Cross-checked `../pokeemerald_wokann_dev` on branch `dev`:

- `src/pokenav_region_map.c`, `UpdateMapSecInfoWindow`: both city branches
  put a 12-by-2 window rectangle, then print the city name. The unvisited
  branch hides the city picture, but still prints the title.
- `build/pokeemerald-jp/src/pokenav_region_map.o`: unvisited branch starts
  at function offset `0x78`. Its first four instructions occupy eight bytes;
  the next instruction is `movs r2, #0` at function offset `0x80`.
- JP `asm/pokenav_unk_4.s`, `sub_081CC260`: corresponding addresses are
  `0x081CC2D8` and `0x081CC2E0`, respectively. The existing manifest verifies
  all eight replaced native bytes: `287a022400940021`.

Only the unvisited-city hook continuation was changed. No visit flags,
city visibility rules, name strings, or save data were changed.

## Validation

`patch/tools/verify_region_map_city_names.py` executes the native info-window
function, the installed veneers, actual window fill and text rendering.
Tilemap/VRAM copies and city pictures are intercepted; this is not full game
emulation.

- Restoring the old continuation reproduces entry into the veneer literal
  before the name window rectangle can be set up.
- All 16 city names render and return normally in both city branches.
- Each city's title pixels match between visited and unvisited states.
- Each result replaces a dirty window and contains visible text.

Build command: `make chs -j4` with the configured `PATCH_ARM_PREFIX`.
ROM CRC32 after this fix: `9EE78642`.
