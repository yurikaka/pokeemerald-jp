# Displaced Frontier trainer-name function

The Japanese `GetFrontierTrainerName` occupies `0x08162D24–0x08162E8F`
(364 bytes, including its literal pools and alignment); the next function
starts at `0x08162E90`. Its logic is reproduced in full by
`ChsOriginalFrontierName` in `patch/chinese_engine.s`.

| Address range | Bytes | Current use |
| --- | ---: | --- |
| `0x08162D24–0x08162D33` | 16 | Entry trampoline to `ChsOriginalFrontierName`. |
| `0x08162D34–0x08162D3B` | 8 | Veneer to `ChsFrontierNameDisplay`, used by eight explicit display call sites. |
| `0x08162D3C–0x08162E8F` | 340 | Displaced original instructions, alignment and literal pools; candidate space, not yet reused. |

The current helper does not jump back into the displaced function body. The
candidate range has not been proven free of every external entry, literal-pool
reference, or other data reference. Before reuse, verify the particular range
against the Japanese ROM and Wokann `dev`, check all active patch ranges, and
validate Thumb alignment and branch reach. Reassess this record if either
entry trampoline or the full original-behavior helper changes.
