# Link trade display follow-up (lj.png and lj2.png)

## Connection standby

Wokann `src/data/trade.h` defines `sText_CommunicationStandby` as
`つうしんたいきちゅう！\nしばらくおまちください` with the original
foreground/background/shadow controls. The first `sTradeMessages` pointer
at 0x08300BDC targets 0x08300B38. This separate trade-menu string was
not covered by the similarly named Berry Blender standby translation.

Batch 498 redirects only this verified message-table slot to the US
Chinese text from `src/data/trade.h`:

```text
正在等待连接……
请稍等片刻。
```

The original color controls are retained.

## Bottom prompt and Cancel

Wokann `src/data/trade.h` confirms the six-entry `sActionTexts` table,
including its Japanese-exclusive final `Bボタン　で　もどります` entry
at 0x08300B10 pointing to 0x08300AEE. This entry is now `B键：返回`.
The Choose Pokemon, Cancel, and Cancel Trade text comes from the current
US Chinese `src/data/trade.h`.

The original `DrawBottomRowText` at 0x08079D3C passes byte-sliced strings
to `sub_080C66A4`, which splits them into four-byte blocks for 32x16
sprites. This can divide Chinese pairs and language controls, so merely
redirecting text pointers does not render these labels correctly.

Pre-render these four labels using the existing normal Chinese font and
the original sprite palette's white foreground and gray shadow. Each
32x16 sprite is packed independently, with a 256-byte Cancel image and
1536-byte images for the six-sprite bottom row. The two Cancel draw
sites at 0x08077280 and 0x08077818 copy the complete 256-byte image and
reconstruct the original following loads before resuming execution.
The bottom-row entry hook selects a pre-rendered image only for the
three known prompt pointers; other input executes the original prologue
and resumes at 0x08079D44.

## Five-character names

Wokann `src/trade.c`, `PrintPartyMonNickname`, and local Japanese
`sub_08079644` describe a display-only print routine for each party slot.
Replace only this routine. Copy its incoming nickname to a local display
buffer. For a Chinese species-name token resolving to five or more
characters, reuse `ChsWriteNarrowSpeciesName` with threshold 5 and append
the original gender/control suffix. Shorter tokens and original Japanese
nicknames are copied unchanged. The same original window ID calculation,
font, text colors, tilemap update and VRAM copy are retained.

No party data, nickname persistence, trade packets, mail, compatibility
checks, or species-name table is modified. `verify_trade_menu_followup.py`
checks original pointer values, built replacements, all four hooks,
sprite lengths/palette indices and the unchanged original species table.
Gameplay testing of both peers is still needed; build success is not
an emulator confirmation.

## Detail panes and confirmation (jh5, jh6, jh8)

The Japanese detail-pane `GetMonNicknameWidth` (`sub_0807946C`) obtains
an original nickname and copies it through `StringCopy10`. Redirect
only that copy site at 0x080794A8 to `ChsCopyMonNickname`, using the
already-selected mon in r4 and the original display destination in r5.
The small original destination retains a compact species token rather
than an expanded name, so this change does not enlarge the caller's
20-byte name buffer or overwrite its adjacent move-string buffer.

At the actual header print call (0x08079398), share the same local
64-byte display buffer and five-character narrow-font conversion used
by the party list. Retain the original gender, slash and level suffix.
A five-character name uses 40px rather than 60px, leaving room in the
96px header window for the existing suffix. Shorter names and custom
Japanese nicknames follow their existing display behavior.

Wokann `src/data/text/region_texts50.h` identifies `gUnknown_8300A9B`
as `わざ` (moves). Redirect its verified detail-pane print reference
at 0x08079418 to `招式`; no move IDs or move-name source data change.

The Japanese-only `DrawTradeMonNicknames` (0x08078120) concatenates
both original nicknames, `と　`, and the translated confirmation suffix
into a 28-byte buffer before using the byte-slicing sprite renderer.
That path still produced Japanese and broken multibyte characters.
Use the US confirmation presentation instead: `确定进行交换吗？` from
US `src/data/trade.h`, pre-rendered as the complete bottom-row image.
Only this display routine is replaced; the selected party indices,
confirmation input, trade compatibility checks and link messages remain
unchanged. The two selected names remain visible in the detail headers.

The jh6 standby string is already the independently redirected
`sTradeMessages[MSG_STANDBY]` slot described above. Verification checks
the actual built pointer and full translated payload, not just the JSON.

## Message width and Cancel centering (jh7, jh8)

The trade dialog has width 16 tiles (128px), with text starting at x=2.
The shared general-dialog translation assumed a wider window. Give only
the verified trade-message slot at 0x08300BF4 a dedicated copy with a
line break, preserving the US wording and punctuation:

```text
这只宝可梦暂时
不能交换！
```

Other uses of `gText_PkmnCantBeTradedNow` keep their original translation.
Both lines fit within the trade dialog's usable width.

The Cancel sprite is centered at x=224 and begins at x=208. The original
24px Japanese label began at sprite x=0, centered at screen x=220.
The Chinese two-character label also spans 24px, so remove its extra
4px inset to retain that same center within the orange button.

## Move label spacing and vertical Cancel centering (jh9)

Wokann `src/trade.c` prints the move label at x=0 and move names at
x=0x18 in the same window. Keep these original coordinates and render
only `招式` with the existing F5 F3 narrow-font mode (8px per character).
The 16px label leaves an 8px gap before the move names; their font is unchanged.

Center the Cancel bitmap's visible foreground and shadow bounds within
its original 16px sprite height. The current glyph bounds move down 1px,
from rows 1..12 to 2..13, leaving equal 2px top and bottom margins.
The sprite position and horizontal layout are unchanged.
