# Restore Japanese Easy Chat words and cursor alignment

Batch 468 incorrectly classified two Easy Chat vocabulary entries as
generic interface strings:

- 0x085758F4 points to 0x08575756, `おとうさん`.
  Wokann `src/data/easy_chat/easy_chat_group_people.h` identifies the
  entry as `gEasyChatWord_Father`, not a generic `gText_Dad` label.
- 0x08575AD4 points to 0x08575805, `ともだち`.
  The same header identifies `gEasyChatWord_Friend`.

Remove both pointer replacements and their unused translation definitions.
Retain the Japanese word table, word IDs, ordering, and saved questionnaire
data. Questionnaire title, instructions, and Chinese footer buttons remain
localized. The separate interface label `gText_Friend2` is unchanged.

Local Japanese `asm/easy_chat.s` confirms that
`GetEasyChatWordStringLength` uses byte-counting `StringLength`, and the
selected-word cursor sums those lengths before multiplying by eight.
The translated strings included language controls and two-byte Chinese
glyphs, so byte length no longer represented the displayed width.
Restoring these original entries removes this mismatch without changing
cursor code or translating the vocabulary.

Validation checks that both pointers and their original string bytes match
the base ROM, and that their decoded strings match the Wokann declarations.
Build and vanilla comparison are also run; emulator interaction remains
to be verified.
