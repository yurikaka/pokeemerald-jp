# Manual review: 104_fortreecity.json

verdicts: {'ok': 12}

| # | address | original | symbol | JP | CN | verdict | notes |
|---|---|---|---|---|---|---|---|
| 0 | 0x081DFE3C | 0x081E0049 | FortreeCity_Text_BugPokemonComeThroughWindow | きのうえで　くらすのは　いいんだけど{FB}ときどき　まどの　そとから\nむしポケモンが　はいって　きたりして{FA}びっくり　しちゃうんだよね | 住在树顶上\n没什么问题，{FB}但有时虫属性宝可梦会\n从窗户爬进来，{FA}经常吓人一跳。 | ok | msgbox; CN faithful |
| 1 | 0x081DFE4E | 0x081E0126 | FortreeCity_Text_CitySign | ここは　ヒワマキ　シティ\nきの　うえで　しぜんと　たわむれる　まち | 这里是茵郁市。\n“与自然嬉戏的树上城市。” | ok | msgbox; CN faithful |
| 2 | 0x081DFE33 | 0x081DFFEA | FortreeCity_Text_EveryoneHealthyAndLively | このまちは　きのうえに\nいえを　たてて　くらしている⋯⋯{FB}そのせいか　みんな　げんきで\nイキイキと　している　のですよ{FB}わしも　このまちに　きてから\n30ねんほど　わかがえった　きぶんです | 城市中的房子\n都建在树上。{FB}也许正因这种生活方式，\n大家都很健康，充满活力。{FB}哈，我也一样——我感觉\n好像年轻了30岁。 | ok | msgbox; CN faithful |
| 3 | 0x081DFE57 | 0x081E0148 | FortreeCity_Text_GymSign | ヒワマキ　シティ　ポケモンジム\nリーダー　ナギ{FA}せかいに　はばたく　とりつかい！ | 茵郁市宝可梦道馆\n馆主：娜琪{FB}“翱翔在世界的\n鸟宝可梦训练家！” | ok | msgbox; CN faithful |
| 4 | 0x081DFE45 | 0x081E008B | FortreeCity_Text_PokemonThatEvolveWhenTraded | ともだちと　こうかんを　すると\nしんか　する　ポケモンが　いるんだって！ | 我听说，有些宝可梦\n会在交换中进化！ | ok | msgbox; CN faithful |
| 5 | 0x081DFE02 | 0x081DFEC0 | FortreeCity_Text_SawGiganticPokemonInSky | だれも　しんじて　くれないけど\nおおきな　ポケモンが　からだを　くねらせ{FA}そらを　とんでいるのを　みたんだ⋯⋯{FB}そいつは　131ばん　すいどうの　ほうへ\nとんでいったよ⋯⋯{FB}⋯⋯ところで\nなんか　きみ　コゲくさいね{FB}かざんに　でも　いってきた？ | 没人肯相信我，但我确实在天空中\n看到了巨大的宝可梦。{FB}它好像在辗转着\n飞向131号水路。{FB}话说⋯⋯\n唔唔⋯⋯你身上，呃⋯⋯好像有焦味。{FB}你刚从火山或什么地方来吗？ | ok | msgbox; CN faithful |
| 6 | 0x081DFE16 | 0x081DFF3B | FortreeCity_Text_SomethingBlockingGym | ポケモンジムに　いきたいのに\nなにかが　みちを　ふさいでいるのよ！{FB}せっかく　120ばん　どうろで\nポケモン　そだてて　きたのに！ | 我想去宝可梦道馆，\n但有东西堵了路。{FB}在120号道路训练了\n那么久，现在却⋯⋯ | ok | msgbox; CN faithful |
| 7 | 0x081DFE72 | 0x081E00B0 | FortreeCity_Text_SomethingUnseeable | みえない　なにかが　いるようだ | 有什么看不见的东西挡在路上。 | ok | msgbox; CN faithful |
| 8 | 0x081DFE20 | 0x081DFF7D | FortreeCity_Text_ThisTimeIllBeatWinona | あたしの　じまんの　ポケモンで\nこんどこそ　ナギさんに　かってみせるわ！ | 我带着我漂亮又可爱的\n宝可梦一起来了。{FA}这一次，我一定要打败娜琪。 | ok | msgbox; CN faithful |
| 9 | 0x081DFE2A | 0x081DFFA2 | FortreeCity_Text_TreesGrowByDrinkingRainwater | あめが　じめんに　すいこまれて\nその　みずを　すって　きがそだつ⋯⋯{FB}みずと　つちが　りょうほう　あるから\nこの　ヒワマキシティも　あるのよね | 树木吸收了渗进地面的雨水，\n慢慢长大⋯⋯{FB}我们茵郁市就是在\n水和土地上建造起来的。 | ok | msgbox; CN faithful |
| 10 | 0x081DFE7C | 0x081E00C0 | FortreeCity_Text_UnseeableUseDevonScope | みえない　なにかが　いるようだ{FB}デボンスコープを　つかいますか？ | 有什么看不见的东西挡在路上。{FB}要使用得文侦测镜吗？ | ok | msgbox; CN faithful |
| 11 | 0x081DFE91 | 0x081E00E1 | FortreeCity_Text_UsedDevonScopePokemonFled | {PLAYER}は\nデボンスコープを　つかった！{FB}とうめいに　なっていた\nポケモンの　すがたが　まるわかりだ！{FB}ポケモンは\nおどろいて　にげだした！ | {PLAYER}使用得文侦测镜。{FB}看不见的宝可梦\n现出了原形！{FB}受惊的宝可梦溜掉了！ | ok | msgbox; CN faithful |
