# Contest display follow-up (hl5, hl6, hl7)

## Graphics mapping

All original compressed resources are checked byte-for-byte against Wokann
`dev` before conversion. Chinese artwork comes from the US Chinese repository.
The Japanese palettes, category order, title rectangle sizes and UI tiles remain
unchanged.

The hl8 follow-up corrects the category extraction: both Wokann
`sub_080DAAD4` and US `PrintContestMoveDescription` use 5-by-2-tile icons
starting at `0x40`, `0x45`, `0x4A`, `0x6A`, and `0x8A`. Copy all 40-by-16
pixels at those exact offsets, without the previous 32-pixel crop or padding.
Each category's output pixels are checked against the US Chinese source.

The hl9 follow-up makes only the results title slots opaque: zero-index pixels
in the copied title tiles and padded columns use palette index 8, matching the
original Japanese blank title tile `0x10` (`0x88` in every packed byte). Other
graphics, sprites and their intentional transparent pixels remain unchanged.
The sliding-text scratch window uses fill `0x11` and foreground/background/shadow
indices `15/1/14`, matching the original `0x085CC4E4` color prefix
(`FC 04 0F 01 0E FF`) used by Wokann `sub_080F739C`. This prevents transparent
scratch-window margins from overwriting the original opaque dialogue interior.

## Next-turn banner (hl10)

The Japanese text under the contestant is `ツギ1バン`: the next appeal's
turn-order indicator, not a nickname or dialogue string. Wokann
`src/contest.c::sSpriteSheet_NextTurn` uses four pointers at `0x08560A4C`,
`0x08560A54`, `0x08560A5C`, and `0x08560A64` to `gContestNextTurnGfx`
(`0x08D8E920`). The builder verifies the original compressed data against
`graphics/contest/nextturn.4bpp.lz`.

The Chinese artwork is copied from US `graphics/contest/nextturn.png`:
the four-character label occupies the first 32 pixels after removing its
two-pixel left margin, followed by the original number/unknown slot. The JP
five-tile allocation (`0xA0` bytes), 40-by-8-pixel subsprite layout, palette,
position, original digit graphics and unknown-order graphic remain unchanged.

Wokann `ShowHideNextTurnGfx` writes the dynamically selected digit into tile 2
using its `0x080DD810` literal (`0x06010040`). This literal becomes
`0x06010080` to write into tile 4, following the longer Chinese label. Wokann
`GetTurnOrderNumberGfx` and its references at `0x080DD880`/`0x080DD88C` are
untouched. No turn-order calculation or participant data is changed.

| Original resource | Patched references | Wokann evidence | Localization |
| --- | --- | --- | --- |
| `0x08C17AB8` | `0x080D6FAC`, `0x080D7700` | `src/contest.c`, `LoadContestBgAfterMoveAnim` and the initial graphics loader; `graphics/contest/interface.png.4bpp.lz` | Appeal/jam labels and five category icons |
| `0x08D8EAAC` | `0x08560B14` | `src/contest.c`, `sSpriteSheet_ApplauseMeter`; `src/graphics.c`, `gContestApplauseGfx` | Applause-meter label |
| `0x08C196CC` | `0x080F61CC` | `src/contest_util.c`, `sub_080F6114`; `graphics/contest/results_screen/tiles.4bpp.lz` | Rank/category/contest title artwork |

Result title pointer mappings are verified against
`data/contest/contest_results.inc` and `src/contest_util.c::sub_080F7A3C`:

| Title | Pointer | Original tilemap |
| --- | --- | --- |
| Normal | `0x080F7A80` | `0x08569334` |
| Super | `0x080F7A94` | `0x08569354` |
| Hyper | `0x080F7AB0` | `0x08569374` |
| Master | `0x080F7ADC` | `0x08569394` |
| Link | `0x080F7A64` | `0x085693B4` |
| Cool | `0x080F7AE4` | `0x085693D4` |
| Beauty | `0x080F7AF4` | `0x085693E8` |
| Cute | `0x080F7B18` | `0x085693FC` |
| Smart | `0x080F7B3C` | `0x08569410` |
| Tough | `0x080F7B94` | `0x08569424` |
| Contest | `0x080F7B98` | `0x08569438` |

Ranks retain their 8-by-2-tile slots. Categories and the contest suffix retain
their 5-by-2-tile slots. Title artwork is assigned only to tiles outside the
Japanese interface/icon range; the builder also checks for conflicts with the
background, interface and winner-banner tilemaps.

## Display hooks

- `0x080D7DAC`: Wokann `src/contest.c` confirms that move-list `r4` holds
  `moveId * 8`. The new display hook doubles this offset when reading the
  16-byte Chinese move-name table. Contest-effect indexing remains unchanged.
- `0x080F626C`: Wokann `src/contest_util.c` confirms separate nickname and
  trainer-name windows. The replacement uses the existing display-only
  contestant lookup and nickname comparison helpers, retaining the original
  slash, window IDs, and player color prefix.
- `0x080F6B9C`: the winner announcement's trainer-name copy uses the same
  display-only lookup. The subsequent nickname copy at `0x080F6BAC` already
  has a Chinese display hook and is not patched again.
- `0x080F7430`, `0x080F7438`, `0x080F76E8`: the results sliding-message path
  originally uses `RenderTextFont9` and byte-based `StringLength`. That renderer
  does not understand Chinese encoding. The replacement rasterizes through the
  existing Chinese TextPrinter into a temporary 32-by-2-tile window, repacks
  columns into the original top/bottom glyph layout, and measures actual cursor
  advancement for the frame length and centering. Text colors are restored.
  Battle healthboxes and other `RenderTextFont9` callers are untouched.

`src/text.c`, `include/text.h` and the original ASM confirm the temporary printer
at `0x0202018C`, its `currentX` field at offset `0x08`, and synchronous rendering
with `TEXT_SKIP_DRAW`. The temporary window is removed after use.

No contestant nickname, trainer name, contest participant structure or save
record is rewritten. Custom names retain their Japanese display behavior.

## Validation

- `make chs` builds `pokeemerald_jp_chs.gba` with validated original hook bytes.
- `make compare` confirms that the unpatched Japanese ROM still matches.
- `git diff --check` passes.
- Resource verification checks compressed input identity, palette-index packing,
  original title-slot sizes and preservation of non-title interface tiles.
- In-emulator validation of selection, move animation, result sliding messages
  and custom names is still required; no emulator run is claimed here.
