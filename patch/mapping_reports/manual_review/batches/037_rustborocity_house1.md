# Manual review: 037_rustborocity_house1.json

verdicts: {'ok': 6}

| # | address | original | symbol | JP | CN | verdict | notes |
|---|---|---|---|---|---|---|---|
| 0 | 0x08203C6B | 0x08203D38 | RustboroCity_House1_Text_AllSortsOfPlaces | いろんな　ばしょに\nいろんな　ポケモンが　いる{FA}いろんな　ひとも　いる{FB}それが　たのしみで　わしも\nいろんな　ところに　でかけるのさ！ | 在不同地方生活着\n不同的人和不同的宝可梦，{FB}我觉得很有趣，\n所以四处旅行。 | ok | script msgbox/message words; CN faithful |
| 1 | 0x08203C61 | 0x08203D17 | RustboroCity_House1_Text_AnyPokemonCanBeCute | だいじに　そだてると\nどんな　ポケモンも　すごく　かわいいよねー | 如果用爱心和细心去照顾宝可梦，\n它们都会变得十分可爱。 | ok | script msgbox/message words; CN faithful |
| 2 | 0x08203C57 | 0x08203CDF | RustboroCity_House1_Text_DoesntLookLikeMonToMe | えー　どうみても　{STR_VAR_1}に\nみえないんだけど⋯⋯ | 嗯？这看上去可\n不是{STR_VAR_1}。 | ok | script msgbox/message words; CN faithful |
| 3 | 0x08203BEA | 0x08203C72 | RustboroCity_House1_Text_IllTradeIfYouWant | え？\nぼくの　ポケモンが　かわいい？{FA}ウン　しってるよー{FB}あっ　どうしても　って　いうなら\nこうかん　して　あげても　いいよ{FB}じゃあ　ぼくの　{STR_VAR_2}\n{STR_VAR_1}　となら　こうかん　するよ | 嗯？我的宝可梦很可爱？\n那是当然的。{FB}但你如果真的想要，\n我也可以考虑跟你交换。{FB}愿意的话，我用我的{STR_VAR_2}\n跟你换{STR_VAR_1}。 | ok | script msgbox/message words; CN faithful |
| 4 | 0x08203C3C | 0x08203CCC | RustboroCity_House1_Text_PleaseBeGoodToMyPokemon | えへへ⋯⋯\nちゃんと　かわいがってね | 呵呵呵⋯⋯\n要善待我的宝可梦啊。 | ok | script msgbox/message words; CN faithful |
| 5 | 0x08203C49 | 0x08203CF7 | RustboroCity_House1_Text_YouDontWantToThatsOkay | あ　いやなら　いいけど⋯⋯\nせっかく　かわいい　ポケモンなのに | 啊，如果你不想换也不要紧，\n但你知道，我的宝可梦非常可爱⋯⋯ | ok | script msgbox/message words; CN faithful |
