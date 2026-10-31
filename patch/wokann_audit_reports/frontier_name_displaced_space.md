# Displaced Frontier trainer-name function

The Japanese `GetFrontierTrainerName` occupies `0x08162D24–0x08162E8F`
(364 bytes, including its literal pools and alignment); the next function
starts at `0x08162E90`. Its logic is reproduced in full by
`ChsOriginalFrontierName` in `patch/chinese_engine.s`.

| Address range | Bytes | Current use |
| --- | ---: | --- |
| `0x08162D24–0x08162D33` | 16 | Entry trampoline to `ChsOriginalFrontierName`. |
| `0x08162D34–0x08162D3B` | 8 | Veneer to `ChsFrontierNameDisplay`, used by eight explicit display call sites. |
| `0x08162D3C–0x08162DF7` | 188 | Direct battle nickname helper and its literal pool. |
| `0x08162DF8–0x08162E8F` | 152 | Displaced original instructions and literal pools; candidate space. |

The original-behavior helper does not jump back into the displaced body. A scan
found no external Thumb BL into the body. One aligned ROM word whose value falls
inside it occurs at `0x0868C108` within the original shakuhachi sample
`sound/direct_sound_samples/DirectSoundWaveData_sd90_classical_shakuhachi.bin`;
it is sample data, rather than a known code pointer. The remaining range has not
been proven free of every indirect reference. Before reuse, verify the specific
range against the Japanese ROM and Wokann `dev`, check active patch ranges, and
validate Thumb alignment and branch reach. The linker enforces the entire
340-byte capacity; reassess the remaining space if the helper changes size.
