# Berry Blender results alignment

Reference: `../pokeemerald_wokann_dev`, branch `dev`,
`src/berry_blender.c`, `Blender_PrintBlendingResults` and
`Blender_AddTextPrinter`.

The results window is window 5. Maximum speed is printed at `(72, 80)`;
elapsed time is printed at `(72, 96)`. Both use font 1. The last call's
`movs r2, #72` is at `0x0808312E`, immediately before `movs r3, #96`
and the call at `0x08083132`. Change only that x coordinate to 96.

The Chinese elapsed-time string has four 8-pixel digits and two 12-pixel
unit characters, for 56 pixels. At x=96 its right boundary is 152 in the
window, matching the existing maximum-speed string's boundary. The latest
Chinese screenshot has a shadow-inclusive speed rightmost pixel of 191
and elapsed-time rightmost pixel of 167 in screen coordinates, confirming
the required 24-pixel shift. Maximum speed's position and formatting stay
unchanged.

Batch 427 replaces `sText_Time` at the results label pointer `0x08083178`.
Use `时间` without the colon; do not change the unrelated `gText_TimeColon`
used by other screens.
