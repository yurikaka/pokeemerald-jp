# Displaced box-name getter

Japanese `GetBoxNamePtr` occupies `0x080D1970–0x080D1997` (40 bytes,
including its literal pool). The next function starts at `0x080D1998`.

| Address range | Bytes | Current use |
| --- | ---: | --- |
| `0x080D1970–0x080D197F` | 16 | Original writable-pointer entry to `ChsBoxNameOriginal`. |
| `0x080D1980–0x080D1987` | 8 | Display entry to `ChsBoxNameForDisplay`. |
| `0x080D1988–0x080D198F` | 8 | Title-width entry to `ChsBoxNameForWidth`. |
| `0x080D1990–0x080D1997` | 8 | Original literal pool; candidate space, not yet reused. |

Before reuse, verify external code and data references against the Japanese ROM
and Wokann `dev`, check all active patches, and validate Thumb alignment and
branch reach. The candidate literal pool has not been proven unreferenced.
