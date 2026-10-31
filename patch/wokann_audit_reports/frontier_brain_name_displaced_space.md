# Displaced Frontier Brain name function

Japanese `CopyFrontierBrainTrainerName` occupies `0x081A4944–0x081A49A7`
(100 bytes, including alignment and literal pools). The next function starts at
`0x081A49A8`. `ChsOriginalBrainName` fully reproduces the original logic.

| Address range | Bytes | Current use |
| --- | ---: | --- |
| `0x081A4944–0x081A4953` | 16 | Original-behavior entry trampoline to `ChsOriginalBrainName`. |
| `0x081A4954–0x081A495B` | 8 | Chinese display veneer to `ChsBrainNameDisplay`. |
| `0x081A495C–0x081A49A7` | 76 | Displaced instructions, alignment and literal pools; candidate space. |

The candidate bytes have not been proven free of all external branches or data
references. Before reuse, cross-check the intended range against the Japanese
ROM, Wokann `dev` and active patches; verify Thumb alignment and branch reach.
