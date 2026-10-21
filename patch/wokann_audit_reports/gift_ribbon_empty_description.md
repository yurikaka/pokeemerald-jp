# Empty gift-ribbon descriptions leave stale screen text

Verified against `../pokeemerald_wokann_dev` branch `dev`,
`src/pokenav_ribbons_summary.c`, `PrintRibbonNameAndDescription`.
After clearing the window buffer, gift ribbon slots read their description
ID from SaveBlock1 `giftRibbons`. An ID of zero returns before
`CopyWindowToVram`, leaving the previous description visible on screen.

The original ROM function is `081D05AC`. It indexes SaveBlock1 with the
ribbon ID plus `0x318F`, equivalent to `0x31A8 + (ribbonId - 25)`.
The conditional branch at `081D061E` originally jumps to the epilogue at
`081D0662`. It now jumps to `081D065A`, which copies the already-cleared
window to VRAM before returning. Nonzero description IDs retain their
original lookup and rendering behavior.

The local save used for the reported screenshot has eleven zero bytes in
its `giftRibbons` array at SaveBlock1 `0x31A8`. These slots have no configured
description. This patch clears stale text; it does not assign descriptions
or change any save data.

Validation: successful ROM build; verified the changed conditional branch
targets the native window-copy path and that the nonzero lookup path is
unchanged. In-game verification remains pending.
