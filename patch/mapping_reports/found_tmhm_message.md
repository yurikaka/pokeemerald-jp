# Found TM/HM message layout (zs2)

US `data/event_scripts.s::gText_PlayerFoundOneTMHM` has exactly two lines:

```
{PLAYER}找到了{STR_VAR_1}
“{STR_VAR_2}”！
```

The old batch439 `auto_wrap` estimated placeholders conservatively and moved
the item onto a second line and the move onto a scrolling third line. The
built sequence contained an added `FE` before the item and an added `FA`
before the move. Disable wrapping for this string and keep its original
US encoded bytes and punctuation unchanged.

Keep Japanese mode around PLAYER only. Wokann
`data/scripts/obtain_item.inc::EventScript_FoundTMHM` buffers the item in
STR_VAR_1. `src/field_specials.c::BufferTMHMMoveName` buffers the move in
STR_VAR_2. Both name providers already return Chinese strings with their own
mode prefix; neither is a Japanese-only placeholder.

Wokann `gText_PlayerFoundOneTMHM` is fixed at `0x08243DB3`. Both compiled
`data/event_scripts.o` message operands reference that same symbol:

| Pointer field | Use |
|---|---|
| `0x08242D28` | `EventScript_FoundTMHM` |
| `0x08242DA3` | `EventScript_FoundHiddenTMHM` |

The first reference was already in batch439; add the second. Both native
fields follow event opcode `0x67` (message), and their original values are
`0x08243DB3`. Do not change item granting, move lookup, item IDs, pocket
messages, or the player's stored name.
