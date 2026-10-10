# NPC trade species display

Two species-name literals were still Japanese in NPC trade conversations.
Both now point to the existing six-byte-stride `ChsSpeciesNameTokens` display
table. No species IDs or exchange records are rewritten.

Address provenance was checked against `../pokeemerald_wokann_dev` branch `dev`,
`src/trade.c:4963` (`GetInGameTradeSpeciesInfo`) and `:4971`
(`BufferInGameTradeMonName`), and corresponding JP assembly:

- 0x0807E1BC: `GetInGameTradeSpeciesInfo`, function 0x0807E174, copies requested
  species at trade-record +56 into STR_VAR_1 and offered species at +12 into
  STR_VAR_2. Record stride is 60; the function returns the original requested
  species ID for script comparison. All four NPC trade scripts call it.
- 0x0807E224: `BufferInGameTradeMonName` (JP asm `sub_0807E1C4`), copies the
  player's nickname into STR_VAR_1 and the offered species into STR_VAR_2.
  The existing display-only nickname conversion remains in use.

Both original literals are 0x082EA31C. Native constructors still use the
original Japanese species/nickname data. NPC nickname, OT, mail and exchange
record bytes at 0x0830D114 are untouched.

`verify_npc_trade_species.py` executes both native producers for all four NPC
trades, expands each translated offer, renders every involved species token
in JP-mode placeholders, and checks original species IDs, custom nicknames,
output guards, Pokemon bytes, save guards and all four original trade records.
This is ARM validation, not a complete in-game exchange test.
