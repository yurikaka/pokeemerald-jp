# All-silver-symbol reward dialogue (kt6)

Wokann `data/maps/BattleFrontier_ScottsHouse/scripts.inc` confirms
`BattleFrontier_ScottsHouse_Text_YouveCollectedAllSilverSymbols` is the
dialogue used for collecting all silver symbols. The Japanese original
uses a scrolling newline for additional lines in its final page.

The US Chinese source and batch 231 instead ended with three lines
separated by two ordinary newline controls (FE). The third line,
`能妥善使用。`, fell outside the two-line dialogue window. The current
automatic width wrapper preserves this page because none of its lines
exceeds the width limit; it does not correct multiple ordinary newlines.

Remove the final newline in both the US Chinese source and the Japanese
batch. Keep all wording and punctuation unchanged. The final page is:

```text
这个送给你。
相信你一定能妥善使用。
```

The second line contains 11 characters including punctuation and fits
the dialogue window without an unnecessary third line or scrolling.
