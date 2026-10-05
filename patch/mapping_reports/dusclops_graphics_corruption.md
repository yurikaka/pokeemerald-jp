# Dusclops graphics corruption (tj5)

Batch 219 redirected three occurrences of the raw four bytes `41 44 22 08`
to `Chs_BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice13Accept`.
These occurrences are compressed graphics data, not text pointers:

| False write | Wokann resource | Resource start | Compressed size |
| --- | --- | --- | --- |
| `0x08D17D1A` | `graphics/pokemon/dusclops/front.4bpp.lz` | `0x08D17AAC` | 928 |
| `0x08B7F496` | `graphics/pokemon/dusclops/anim_front.4bpp.lz` | `0x08B7F228` | 1712 |
| `0x08B6A699` | `graphics/pokemon/shedinja/anim_front.4bpp.lz` | `0x08B6A23C` | 1504 |

The animation symbols and addresses are explicitly declared in Wokann
`data/data_b2d_gfx_front.s`. The static front image is declared as
`gMonStillFrontPic_Dusclops` in `src/data/graphics/pokemon.h`, and its
complete compressed binary uniquely matches the vanilla ROM at the start
above. All original resources match the supplied Japanese base ROM.

Both damaged Dusclops streams fail software decompression with invalid
backreferences in the tested pre-fix build. Remove all three false writes
while retaining the dialogue's `0x085BC018` reference. These false writes
were introduced by commit `6ad376cb`.

The historical mapping report is kept unchanged as provenance. This
follow-up documents the rejected matches. The regression tool checks
static/animated fronts, backs, palettes, icons and footprints against the
Wokann resources and compares decompressed compressed resources.
