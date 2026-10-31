# Displaced StringCopy10 function

Japanese `StringCopy10` occupies `0x08008828–0x0800885B` (52 bytes,
including alignment). `StringGetEnd10` begins at `0x0800885C`.

| Address range | Bytes | Current use |
| --- | ---: | --- |
| `0x08008828–0x08008837` | 16 | Original five-byte copy entry to `ChsStringCopy7Original`. |
| `0x08008838–0x0800883F` | 8 | TV nickname display with species at `r4 + 2`. |
| `0x08008840–0x08008847` | 8 | TV nickname display with species at `r5 + 2`. |
| `0x08008848–0x0800884F` | 8 | TV nickname display with species at `r5 + 0x10`. |
| `0x08008850–0x0800885B` | 12 | Displaced instructions and alignment; candidate space. |

The native five-byte copying semantics match `StringCopy7`, so the original
entry shares its existing helper. Before reusing the candidate 12 bytes, check
external branches and data references against the Japanese ROM and Wokann
`dev`, active patch overlaps, Thumb alignment, and branch reach.
