# Trick House numeric answer options

Checked against `../pokeemerald_wokann_dev` on branch `dev`:
`data/text/trick_house_mechadolls.inc`, `src/data/script_menu.h`, and
`data/maps/Route110_TrickHousePuzzle5/scripts.inc`.

Batch 507 translates the 13 remaining Japanese numeric answer options:
Mechadoll 3 question 2 (60/55 yen), Mechadoll 4 question 3 (one/two people),
and all nine options for Mechadoll 5 (Pokemon, tree houses, and triathletes).
Chinese counters are respectively 元, 人, 只, 间, and 人.

The 15 menus have three eight-byte MenuAction entries each, starting at
`0x08563838`. Each new override was verified against its original pointer and
the Japanese source string encoded with the reference charmap. Only the text
pointers change; callback fields, menu order, and correct-answer indices remain
unchanged. Combined with the existing translations, all 45 fixed answer options
now use Chinese text.

The same Japanese script was also used to review all five introductions,
15 questions, and the shared answer feedback in batch 067. Corrections:

- Doll 4 describes itself as beautiful, rather than saying its quiz concerns beauty.
- Doll 3 is particular about money, rather than caring only about prices.
- Doll 1 requires consecutive correct answers through doll 5 to reach the password.
- Doll 2's third question uses 橙华森林, without the erroneous 市.
- Doll 1's opening noise follows カタカタ as 咔嗒咔嗒, without adding 噼啪.
- The wrong-answer response follows ザンネン！マチガイ デーーース！ as
  很遗憾！答——错——啦！, retaining the drawn-out delivery.

These changes replace text within the existing entries and keep all script
references and answer checks intact.

## Full Japanese dialogue review

The subsequent full review covers 25 puzzle texts, four shared scroll/door texts
in `Route110_TrickHouseEntrance/scripts.inc`, and all 45 answer options.
Batch 067 now restores the Japanese numbering, exclamations, rattling sound,
drawn-out delivery, doll 4's feminine voice, and dolls 1/2/3/5's boastful self
reference. Doll 5 identifies itself as the master's highest masterpiece.
The mail question uses 港口邮件, matching the item-name table and answer option.
The password consistently uses 暗号; the door inscription retains 大人 and the
unlock message reports hearing the lock open rather than adding a specific sound.
Batches 061/062 restore the shared locked-door and scroll messages accordingly.
These shared fixes also apply when those messages appear in other puzzles.

Original manual line/scroll/page controls are preserved in all 25 puzzle texts.
Chinese width requires automatic wrapping for doll 5 question 1 and the laugh;
this does not add page breaks. Player-name placeholders explicitly switch to
Japanese mode and back, preserving the original save-name rendering.

Verified all 74 installed strings and references, all 45 unchanged menu callbacks,
dialogue widths, and player-name language controls. `make compare` passed.
