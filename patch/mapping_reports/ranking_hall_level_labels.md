# Ranking Hall level labels

`kt6.png` shows the untranslated Open Level label on the Battle Factory
ranking screen. Ranking Hall uses a separate two-pointer level-name table;
the existing seven facility-record screen references were already covered.

Checked Wokann `dev`, `src/frontier_util.c`,
`DomePrintPrevOrCurrentStreak` (Ranking Hall renderer): it loads the pointer
at 0x081A465C, which points to table 0x085DD504. The renderer indexes this
table by level mode and prints its entry at x=132, y=2. The late data block
`gUnknown_85DD504` contains pointers 0x085DD4F4 (Level 50) and 0x085DD4FC
(Open Level). US `frontier_util.c` names this table `sLevelModeText`.

Batch 504 redirects both entries to the existing translated RecordsLv50 and
RecordsOpenLevel labels. All Ranking Hall facilities share this table.
