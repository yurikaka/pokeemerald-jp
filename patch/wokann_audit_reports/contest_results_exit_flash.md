# Contest results score-star tiles overwritten by Chinese titles

## Root cause

`patch/tools/build_contest_gfx.py` previously allocated Chinese title tiles
from `1..15`, `17..63`, and `178..255` (`B2..FF`). It checked the three
static results tilemaps for conflicts, but did not check tiles inserted
at runtime. This overwrote the original score-star graphics at `B2..B4`.
In particular, tile `B3` became a solid `88` tile instead of a star.

Verified against `../pokeemerald_wokann_dev` branch `dev`,
`src/contest_util.c`:

- `sub_080F6114`: `080F61E4` contains tilemap value `60B2`; the drawing
  loop at `080F61A8` also adds two to select `60B4`.
- `sub_080F8310`: `080F83D8` contains `60B3`, used when updating the score
  stars. The first-round score update dynamically inserts these entries.
- `sub_080F7114`: repeatedly blends palette entries `68`, `6B`, and `6E`.
  Color index 8 in palette 6 is therefore rewritten by the flash task.
- `sub_080F7044`: clears the background/object palettes, then disables
  hardware darkening. The Chinese solid-color `B3` tile exposes the
  rewritten palette color as four strips on the otherwise black screen.
  The original star does not use color index 8.

The shared native cleanup structure was initially mistaken for an
original-game defect. Loading the Chinese `.ss4` with an original ROM
preserves corrupted graphics in VRAM, so that test cannot establish
original-game behavior. Fresh results initialization from `.ss3` agrees
with the user's observation: original Japanese graphics do not flash.
US cleanup source alone likewise does not prove a visible US-game bug.

## Fix

Reserve all three native score-star tiles `B2..B4`; start the upper title
allocation range at `B5`. Deduplicate identical title tiles to recover
space: the 140 title positions now use 94 unique tiles. Apply the title's
left-edge crop before deduplication so shared tiles are never modified
later. Verify that all three score-star tiles remain byte-identical to
those in the original Japanese resource.

Removed the provisional `ChsContestResultsStopFlashing` hook. The native
exit function at `080F7044..080F70D7` is byte-identical to the base ROM;
no extra task cleanup is needed.

## Verification

Used the mGBA software core embedded in the existing
`pokeemerald_expansion_chs/tools/mgba/mgba-rom-test` binary. Started from
the user's `.ss3` on the contest-hall map so each ROM builds its own
results screen. Tests use identical A-button input. Save files and user
states were not edited.

Temporary diagnostic ROMs and logs were kept under
`/tmp/contest-investigation`. Baseline removes the provisional cleanup
hook from the previous build. Results:

| Experiment | CRC32 | Flash after results fade |
| --- | --- | --- |
| Restore all contest graphics pointers | F460E05D | None |
| Restore results text/name hooks only | C69306B8 | 932, 932, then 488 pixels |
| Restore only results graphics pointer `080F61CC` | 816391EC | None |
| Restore only the eleven title-map pointers | C7E7E576 | 932, 932, then 488 pixels |
| Restore only star tiles B2/B3 in the old graphics | C9B988FF | None |
| Final resource fix, original native exit code | 0834A5BB | None |

The isolated star restoration leaves all text hooks and other graphics
unchanged. Its alternate compressed copy was placed in unused temporary
ROM space, without changing the source ROM. This directly isolates the
corrupted score-star graphics as the cause.

Additional checks: all 140 title placements across all eleven Chinese
labels have identical rendered tile pixels before and after allocation
changes; all three native star tiles match the original; no cleanup code
patch remains; `git diff --check` passes. Successful `make chs -j4` build.

The earlier intermediate allocator build (`451D4AD4`) reserved B2/B3;
the final build also preserves B4, which initialization selects via the
runtime `+2` calculation.

## Existing instant saves

The old `.ss4` already contains overwritten graphics in VRAM. A ROM
resource correction cannot replace graphics cached inside that state.
Load `.ss3` and let the results screen initialize again to test the fix.

Final ROM CRC32: `0834A5BB`.
