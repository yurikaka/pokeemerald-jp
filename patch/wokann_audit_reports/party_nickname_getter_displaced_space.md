# Displaced party nickname getter

Japanese `GetMonNickname2` (`GetBoxMonNick` in Wokann `dev`) occupies
`0x0806F4B0–0x0806F4CF` (32 bytes, including alignment). The next getter
starts at `0x0806F4D0`.

| Address range | Bytes | Current use |
| --- | ---: | --- |
| `0x0806F4B0–0x0806F4BF` | 16 | Default display entry to `ChsCopyMonNickname`. |
| `0x0806F4C0–0x0806F4C7` | 8 | Explicit original nickname entry to `ChsCopyMonNicknameOriginal`. |
| `0x0806F4C8–0x0806F4CF` | 8 | Displaced instructions and alignment; candidate space. |

Before reuse, verify external branches and references against the Japanese ROM
and Wokann `dev`, check active patch ranges, and validate Thumb alignment and
branch reach. The candidate bytes have not been proven free of every reference.
