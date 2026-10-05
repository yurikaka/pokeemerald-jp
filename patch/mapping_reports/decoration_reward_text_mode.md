# Decoration reward message mode (kt4/kt5)

Wokann `data/scripts/obtain_item.inc::EventScript_ObtainDecorationMessage`
buffers the decoration name in STR_VAR_2. `EventScript_ObtainedDecor`
then prints `gText_ObtainedTheDecor` followed by
`gText_TheDecorWasTransferredToThePC`.

Chinese decoration names in `ChsDecorations` are four-byte compact resource
tokens (F5 F1 resource-ID FF), preserving the original fixed-size name
fields. In `ChineseRenderHook`, the compact resource end uses the shared
compact-species completion path, which restores Japanese text mode before
resuming the outer string.

Batch 363 did not restore Chinese mode after the decoration placeholder.
Consequently the Chinese exclamation mark after the shield name was
decoded as Japanese, and the transfer message after that name also used
Japanese decoding. This is a mode-boundary bug, not missing shield names
or untranslated source text.

Insert explicit ENG controls immediately after STR_VAR_2 in both messages.
Keep the US Chinese wording, punctuation and newline unchanged:

- `获得了{STR_VAR_2}{ENG}！`
- `{STR_VAR_2}{ENG}\n传送到电脑里了。`

Leave the renderer's Japanese reset behavior intact for other mixed-language
uses. No decoration IDs, inventory, reward flags or save data are changed.
