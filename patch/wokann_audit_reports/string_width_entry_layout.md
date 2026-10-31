# String-width entry layout

Japanese `GetStringWidth` starts at `0x08005DAC`. Its entry was split into:

| Address range | Bytes | Current use |
| --- | ---: | --- |
| `0x08005DAC–0x08005DBB` | 16 | Original-behavior trampoline to `ChsOriginalGetStringWidth`. |
| `0x08005DBC–0x08005DC3` | 8 | Explicit Hall of Fame width veneer. |
| `0x08005DC4–0x08005DC5` | 2 | Displaced second half of the original `BL`; not available for reuse. |
| `0x08005DC6` onward | — | Original width function body, still executed. |

The original-behavior helper reproduces the first 24 bytes, including the
`GetFontWidthFunc` call, and resumes at `0x08005DC6`. The veneer overwrites
only the first half of the original four-byte BL, so `0x08005DC4–0x08005DC5`
is an orphaned instruction halfword; do not treat it as safe reusable space.
The original function body and its literal pools are still active: no remaining
space is claimed here.
