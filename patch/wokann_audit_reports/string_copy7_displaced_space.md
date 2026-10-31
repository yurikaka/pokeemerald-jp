# Displaced StringCopy7 function

Japanese `StringCopy7` occupies `0x08008888–0x080088B7` (48 bytes,
including alignment). `StringCopy` starts at `0x080088B8`.

| Address range | Bytes | Current use |
| --- | ---: | --- |
| `0x08008888–0x08008897` | 16 | Original-behavior trampoline to `ChsStringCopy7Original`. |
| `0x08008898–0x0800889F` | 8 | Explicit VS-display veneer to `ChsVsNameCopy`. |
| `0x080088A0–0x080088B7` | 24 | Displaced original instructions and alignment; candidate space. |

The candidate range is not yet proven free of all external entries or data
references. Verify the intended reuse against the Japanese ROM, Wokann `dev`
and active patches, including Thumb alignment and branch reach.
