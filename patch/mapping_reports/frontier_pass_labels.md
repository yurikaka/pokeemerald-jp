# Frontier Pass untranslated labels (kt7 / kt8)

## Facility-name text references

Wokann `src/data/frontier_pass.h` fixes the seven 16-byte landmark records at
`gUnknown_854B174`. `src/frontier_pass.c::PrintOnFrontierMap` reads each record's
first word and passes it directly to `AddTextPrinterParameterized3`, preserving
the selected/unselected color tables. The second word is the description and
must not be changed by this name-label patch.

The native Japanese strings are in the packed `gUnknown_85CCAA8` definition in
`src/data/text/region_texts105.h`. Chinese strings below are copied verbatim from
the corresponding definitions in `pokeemerald_us_chs/src/strings.c`.

| Reference | Native target | Japanese | Chinese | US symbol |
|---|---|---|---|---|
| `0x0854B174` | `0x085CCBA8` | バトルタワー | 对战塔 | `gText_BattleTower3` |
| `0x0854B184` | `0x085CCBAF` | バトルドーム | 对战巨蛋 | `gText_BattleDome2` |
| `0x0854B194` | `0x085CCBB6` | バトルパレス | 对战宫殿 | `gText_BattlePalace2` |
| `0x0854B1A4` | `0x085CCBBD` | バトルアリーナ | 对战竞技场 | `gText_BattleArena2` |
| `0x0854B1B4` | `0x085CCBC5` | バトルファクトリー | 对战工厂 | `gText_BattleFactory2` |
| `0x0854B1C4` | `0x085CCBCF` | バトルチューブ | 对战管道 | `gText_BattlePike2` |
| `0x0854B1D4` | `0x085CCBD7` | バトルピラミッド | 对战金字塔 | `gText_BattlePyramid2` |

Tower was already translated by batch477 and is deliberately not overwritten
again. Batch499 redirects only the remaining six names. No descriptions,
coordinates, palettes, font selection, or highlight logic are changed.

## Baked-in cancel artwork

The kt7 upper-right `とじる` is not a printed string. Wokann's fixed resources are:

- `gUnknown_85469A4`: `graphics/frontier_pass/bg.4bpp.lz`.
- `gUnknown_8549DB8`: `graphics/frontier_pass/cancel.bin`, six by two tiles.
- `gUnknown_8549DD0`: `graphics/frontier_pass/cancel_highlighted.bin`, six by two tiles.

The loader's literal at `0x080C4EC4` points to `0x085469A4` and is consumed by
`DecompressAndCopyTileDataToVram`. It is redirected to a generated modified copy
of that same Japanese tileset. The build tool verifies the complete original
compressed resource against Wokann before editing.

Only the word's pixels are replaced, with the existing US Chinese `取消` artwork
from `graphics/frontier_pass/bg.png` and its two cancel tilemaps. Both normal and
highlighted variants are ported. US glyph pixels x28..51 map to Japanese button
x20..43. The arrow, palette indexes, Japanese tilemaps, bottom border, resource
length, and all unrelated tiles stay unchanged. No US screen layout is imported.
