# Dome winner name and imported punctuation

`kt4.png`: batch 201's `LastWinnerWasTough` inserts STR_VAR_1 without a
Japanese-mode boundary. The winner name is produced by Wokann `dev`
`src/battle_dome.c`, `BufferLastDomeWinnerName` and `CopyDomeTrainerName`;
the latter copies a saved player name, a facility trainer name, or the Dome
Brain name in native encoding. The event's `dome_getwinnersname` precedes
the message. Adding `japanese_placeholders: [2]` brackets the name with JPN
and ENG controls; stored names and the producer remain unchanged.

`kt3.png`: `ExplainTourneyTree` was in a checklist batch whose category does
not enable dialogue wrapping. Its first line exceeded the 168-pixel dialogue
width, clipping part of 树状图 and the closing quote. The entry now explicitly
enables automatic wrapping. Native B1/B2 Japanese quote shapes are retained
in both imported and directly encoded text, as requested by the user. The
closing quote is present in the first dialogue page and every line fits.

`kt5.png`: the original Level 50 menu string at 0x085CAB0D decodes to
レベル50, with no period. The imported translation was Lv. 50级. US period
AD is a Japanese full stop in the native font; it now selects Latin glyph AD
through the same 7F prefix. Direct text encoding also uses this prefix for
the ASCII period. Its two-pixel bitmap uses a four-pixel advance in normal
and small fonts. The explicit space after Lv. is removed in 34 text entries,
including menus, dialogue, records and ribbon descriptions. Existing Chinese
full stops remain Chinese punctuation.

`kt7.png`: `gText_MonTypeAndNo` was 宝可梦种类&数量. US ampersand 2D was
rendered as the JP font's キ. Imported and directly encoded ampersands now
use Latin glyph 2D through the 7F prefix. At the user's request this menu
entry is 宝可梦种类和数量, matching JP ポケモンのしゅるいとかず; it uses
only Chinese glyphs.

`verify_frontier_display_fixes.py` checks native placeholder expansion,
native quotes, compact period rendering, ampersand conversion, dialogue
bounds and the actual Ranking Hall header rendering path. The build reflows
the affected dialogue.
