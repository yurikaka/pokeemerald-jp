# Trick House Pokemon answer options

Checked against `../pokeemerald_wokann_dev` on branch `dev`:
`data/text/trick_house_mechadolls.inc` and `src/data/script_menu.h`.

The first six Mechadoll question menus contain 18 fixed Pokemon-name options.
They are ordinary `MenuAction` entries, not Easy Chat words. Their text pointers
occupy `0x08563838` through `0x085638C0`, spaced eight bytes apart.

Batch 506 redirects each text pointer to a Chinese name matching the existing
species-name table. Original Japanese strings were checked against the base ROM,
and all 18 labels, menu ordering, and individual pointer references were checked.
The four callback bytes following each pointer remain unchanged. No question,
answer index, or menu order changes.

The expansion localization already translates these options inline in
`src/data/script_menu.h`; the US localization's separate text labels remained
English, and the earlier Japanese text import omitted those entries.
