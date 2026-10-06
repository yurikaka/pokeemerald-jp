# Five-character move names in Summary and battle menus

Keep `ChsMoveNames` unchanged and derive `ChsMoveDisplayNames` from the same
`patch/move_names.json` strings. Both tables retain the existing 16-byte stride.
Only five-character Chinese names in the display variant receive
`F5 F3` (Muzaipixel narrow font) before the glyphs and `F5 F4` (normal Chinese
font) before EOS. The five names are 百万吨重拳, 百万吨重踢, 尖刺加农炮,
骨头回力镖 and 种子机关枪. Each narrow entry occupies 15 bytes including EOS;
all remaining entries are byte-identical to the normal table.

Wokann source verification:

| Native pointer field | Source / use |
|---|---|
| `0x08059730` | `src/battle_controller_player.c`, move selection: copies each indexed name into `gDisplayedStringBattle`, then prints it |
| `0x081C3440` | `src/pokemon_summary_screen.c::PrintMoveNameAndPP`, shared by battle and contest move pages |
| `0x081C3800` | `PrintNewMoveDetailsOrCancelText`, battle-page new move name |
| `0x081C3874` | `PrintNewMoveDetailsOrCancelText`, contest-page new move name |

All four fields originally contain `0x082EACC4` (`gMoveNames`). Their Wokann
compiled objects have `R_ARM_ABS32` relocations explicitly referencing
`gMoveNames` at the matching locations. The existing patched move-name indexing
already uses stride 16 and does not need changes.

Exclude only these four fields from the global normal-table replacement and
redirect them explicitly to the display variant. Battle dialogue expansion,
other move-name callers, move data, IDs, PP, and persistent data remain unchanged.
The font reset before EOS prevents the following text from inheriting the
narrow font when a move name is copied into a larger display string.
