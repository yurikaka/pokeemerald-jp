# Match Call list row residue

The source-backed translated rival description in batch 464 is still
`邻居`, from US `gText_MayBrendanMatchCallDesc`. Its two pointers are the
May/Brendan header description fields at 0x085F760C and 0x085F769C.
The trainer table contains `小贡`, not `小贡奇`, for every Winston rematch.

Wokann dev `src/pokenav_list.c::LoopedTask_PrintListItems` buffers a new
entry and prints it into a recycled row without clearing that row first.
The original fixed/padded text layout covers old text; the Chinese Match Call
formatter uses variable-length narrow glyphs and jumps directly to the name
column, leaving the unused part of both columns untouched. This explains
long-to-short leftovers such as a previous class's trailing `小子` after `邻居`.
The exact preceding entry in the user's playthrough has not been captured.

The eight-byte veneer at 0x081C7BDC is at the original shared printing setup,
not inside a function-entry trampoline. Wokann's pokenav_list.o .text section
starts at 0x081C797C; offset 0x260 contains the exact bytes
`207a290102221143`. The instructions load windowId, compute row*16+2, and
resume with the text-printer argument stores at 0x081C7BE4.

The helper checks bufferItemFunc at list+0x34 against the original hooked
Match Call formatter entry 0x081CA7F5. Only Match Call rows are cleared.
It fills the full window width (list+4 tiles times eight) and 16-pixel row
height with 0x11, the same color used by Wokann's list initialization and
PrintMatchCallListTrainerName. Rematch ball icons live in the BG tilemap,
not the window pixel buffer, and are not cleared. Other Pokenav lists keep
their original behavior. Register values and LR are restored before replaying
the original four instructions.

The later jz1 repair additionally selects the new ribbon-list formatter for
the same row clearing; see `ribbons_list_display.md`. Other lists remain excluded.

No name, title, saved trainer data, comparison or string-matching rule changes.
Runtime acceptance requires scrolling long titles/names out and short ones in,
including the rival description and Winston's name. This environment has not
performed that emulator test.
