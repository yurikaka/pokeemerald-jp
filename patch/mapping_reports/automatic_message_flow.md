# Automatic message flow

Cross-reference: `../pokeemerald_wokann_dev` (`dev`),
`data/scripts/std_msgbox.inc`, map scripts, `data/scripts/contest_hall.inc`,
and `src/contest_util.c` (`BufferContestTrainerAndMonNames`).

`MSGBOX_GETPOINTS` prints the message, plays the BP fanfare, waits for the
fanfare and text, then returns without waiting for a button. Its native script
at `0x082423D6` remains unchanged. Chinese dialogue wrapping previously added
`0xFA` (button-triggered scrolling) to BP receipt messages.

Fixed seven definitions:

- Scott's BP receipt and the shared receipt used by all seven facilities:
  `{PLAYER}获得了\n{STR_VAR_1}BP！`.
- Lounge 3 BP receipt: the same concise wording. This checklist text did not
  wrap automatically, so its original long second line could clip instead.
- Pyramid summit: `新的金字塔征服者！\n其名为{PLAYER}！`, matching the Japanese content.
- Palace and Pike level selection: `要挑战50级\n还是开放等级？`.
- Contest entry announcement: retain the translation but use bounded widths
  for trainer name (48 px), entry number (8 px), and nickname (60 px), rather
  than assuming every string variable is a 96-pixel item name. All 96 translated
  NPC trainer/nickname pairs expand within the window (maximum line 128 px).

These definitions use `no_manual_prompt`: the build fails if they gain a
manual scrolling/page control or exceed two 168-pixel lines. Optional
`placeholder_widths` are local to each definition; other dialogue keeps its
existing estimates.

`verify_auto_message_flow.py` scans all direct `message` and
`MSGBOX_GETPOINTS` sites in the Japanese reference scripts: 434 sites,
329 translated symbols, and 293 references whose original text contains no
manual page controls. All literal message symbols are mapped; the sole
nonliteral symbol is `NULL`, used by standard message handlers. Messages
that already contain intentional Japanese page controls retain normal
dialogue wrapping. `messageautoscroll` already advances its pages automatically.

Validation: rebuilt CHS ROM, unchanged base-ROM comparison, automatic message
audit, all 96 native contestant-name expansions, and existing Frontier display
checks pass. This is script/ROM validation, not an emulator playthrough.
