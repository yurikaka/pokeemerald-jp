# Displaced box Pokémon nickname getter

Japanese `GetMonNick` occupies `0x0806F4D0–0x0806F4EF` (32 bytes,
including alignment). The next function starts at `0x0806F4F0`.

| Address range | Bytes | Current use |
| --- | ---: | --- |
| `0x0806F4D0–0x0806F4DF` | 16 | Default display entry to `ChsGetMonNicknameFromBox`. |
| `0x0806F4E0–0x0806F4E7` | 8 | Explicit original entry to `ChsCopyBoxMonNicknameOriginal`. |
| `0x0806F4E8–0x0806F4EF` | 8 | Displaced instructions and alignment; candidate space. |

Before reuse, check external branches and references against the Japanese ROM,
Wokann `dev` and active patches, including Thumb alignment and branch reach.
The candidate bytes have not been proven free of all external references.
