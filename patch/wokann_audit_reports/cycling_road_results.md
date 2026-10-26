# Cycling Road result text

Reference: `../pokeemerald_wokann_dev` branch `dev`,
`data/maps/Route110/scripts.inc` and `src/field_specials.c`.

In `057_route110.json`, removed the duplicate 次 after the collision variable:
the native results routine already appends that unit. Corrected the Good
reaction to warn against excessive speed and accidents, and the Ok reaction
to mention immature technique while encouraging enjoyment of cycling, matching
the Japanese dialogue. All five reaction pointers already referenced Chinese.

In `435_checklist_fixed_text_blocks.json`, changed the overflow strings to
1分钟以上 and 99次以上. These match the native Japanese meaning:

- `0x085CB018`: `1ぷん　いじょう` (one minute or more).
- `0x085CB00E`: `99かい　いじょう` (99 collisions or more).

`DetermineCyclingRoadResults` at `0x08137DCC` retains its thresholds, numeric
formatting and scoring. The normal time suffix is already Chinese 秒.

Validation against the final working ROM:

- 40 time/collision combinations and 80 expanded current/best-record strings
  verified the dynamic suffixes and removal of the duplicate result unit.
- Updated reaction payloads match the requested text, fit dialogue line widths,
  and have correctly installed script references.
- Native overflow result generation produces the new Chinese strings.
- `make compare` and `git diff --check` pass.

The separate symbol-rendering audit documents the general Latin glyph fixes.
Final working ROM CRC32, including those fixes: `68559D33`.
