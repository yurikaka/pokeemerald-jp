# Manual review: 171_pokedex.json

verdicts: {'ok': 36, 'ok-intentional': 12}

| # | address | original | symbol | JP | CN | verdict | notes |
|---|---|---|---|---|---|---|---|
| 0 | 0x080BE484 | 0x085C8FA2 | gText_5MarksPokemon | ？？？？？ポケモン | ？？？宝可梦 | ok | PTR-OK, CN faithful |
| 1 | 0x080BEC60 | 0x085C8FD4 | gText_CryOf | の |  | ok-intentional | matches us_chs split CryOf into suffix; color names mix matches upstream |
| 2 | 0x080BEC64 | 0x085C8FD6 | gText_CryOf | なきごえ |  | ok-intentional | matches us_chs split CryOf into suffix; color names mix matches upstream |
| 3 | 0x080BF218 | 0x085C8FDB | gText_SizeComparedTo | と | 与 | ok | PTR-OK, CN faithful |
| 4 | 0x080BF220 | 0x085C8FDD | gText_SizeComparedTo | の　おおきさくらべ | 的体型比较 | ok | PTR-OK, CN faithful |
| 5 | 0x080BF868 | 0x085C8FE7 | gText_PokedexRegistration | ポケモンずかんの　とうろく　かんりょう！ | 图鉴登记完毕。 | ok | PTR-OK, CN faithful |
| 6 | 0x080C0DD8 | 0x085C8FFC | gText_SearchingPleaseWait | けんさくを　しています⋯⋯ | 搜索中⋯⋯\n请稍候。 | ok | PTR-OK, CN faithful |
| 7 | 0x080C1010 | 0x085C900A | gText_SearchCompleted | けんさくが　しゅうりょう　しました！ | 搜索完毕。 | ok | PTR-OK, CN faithful |
| 8 | 0x080C104C | 0x085C901D | gText_NoMatchingPkmnWereFound | がいとう　する　ポケモンは　いませんでした⋯⋯ | 没有找到符合条件的宝可梦。 | ok | PTR-OK, CN faithful |
| 9 | 0x08544134 | 0x085C9035 | gText_SearchForPkmnBasedOnParameters | じょうけんを　していして\nポケモンの　けんさくを　します | 搜索宝可梦\n请选择条件。 | ok | PTR-OK, CN faithful |
| 10 | 0x0854413C | 0x085C9052 | gText_SwitchPokedexListings | ずかんリストの　ならびを　きりかえます | 切换图鉴的排列方式。 | ok | PTR-OK, CN faithful |
| 11 | 0x08544144 | 0x085C9066 | gText_ReturnToPokedex | ずかんに　もどります | 返回图鉴。 | ok | PTR-OK, CN faithful |
| 12 | 0x08544188 | 0x085C9071 | gText_SelectPokedexMode | ずかんモードを　してい　します | 选择图鉴的模式。 | ok | PTR-OK, CN faithful |
| 13 | 0x0854417C | 0x085C9081 | gText_SelectPokedexListingMode | ずかんの　ならびを　してい　します | 选择图鉴的排列模式。 | ok | PTR-OK, CN faithful |
| 14 | 0x0854414C | 0x085C9093 | gText_ListByFirstLetter | なまえの　さいしょの　もじを　してい　します\n　/みつけたポケモンのみ | 按名字的首字母排列。\n仅限已发现的宝可梦。 | ok | PTR-OK, CN faithful |
| 15 | 0x08544158 | 0x085C90B7 | gText_ListByBodyColor | からだの　いろを　してい　します\n　/みつけたポケモンのみ | 按身体颜色排列。\n仅限已发现的宝可梦。 | ok | PTR-OK, CN faithful |
| 16 | 0x08544164 | 0x085C90D5 | gText_ListByType | タイプを　してい　します\n　/つかまえたポケモンのみ | 按属性排列。\n仅限已捕捉的宝可梦。 | ok | PTR-OK, CN faithful |
| 17 | 0x08544170 | 0x085C90D5 | gText_ListByType | タイプを　してい　します\n　/つかまえたポケモンのみ | 按属性排列。\n仅限已捕捉的宝可梦。 | ok | PTR-OK, CN faithful |
| 18 | 0x08544194 | 0x085C90F0 | gText_ExecuteSearchSwitch | けんさく/きりかえを　じっこうします | 执行搜索或切换。 | ok | PTR-OK, CN faithful |
| 19 | 0x08544214 | 0x085C9103 | gText_DexHoennTitle | ホウエン　ずかん | 丰缘图鉴 | ok | PTR-OK, CN faithful |
| 20 | 0x0854421C | 0x085C910C | gText_DexNatTitle | ぜんこく　ずかん | 全国图鉴 | ok | PTR-OK, CN faithful |
| 21 | 0x0854422C | 0x085C9115 | gText_DexSortNumericalTitle | ばんごう　じゅん | 编号模式 | ok | PTR-OK, CN faithful |
| 22 | 0x08544234 | 0x085C911E | gText_DexSortAtoZTitle | ごじゅうおん　じゅん | 拼音模式 | ok | PTR-OK, CN faithful |
| 23 | 0x0854423C | 0x085C9129 | gText_DexSortHeaviestTitle | おもい　じゅん | 体重降序模式 | ok | PTR-OK, CN faithful |
| 24 | 0x08544244 | 0x085C9131 | gText_DexSortLightestTitle | かるい　じゅん | 体重升序模式 | ok | PTR-OK, CN faithful |
| 25 | 0x0854424C | 0x085C9139 | gText_DexSortTallestTitle | たかい　じゅん | 身高降序模式 | ok | PTR-OK, CN faithful |
| 26 | 0x08544254 | 0x085C9141 | gText_DexSortSmallestTitle | ひくい　じゅん | 身高升序模式 | ok | PTR-OK, CN faithful |
| 27 | 0x085442C4 | 0x085C9180 | gText_DexSearchColorRed | あか | 红 | ok-intentional | matches us_chs split CryOf into suffix; color names mix matches upstream |
| 28 | 0x085442CC | 0x085C9183 | gText_DexSearchColorBlue | あお | 蓝色 | ok-intentional | matches us_chs split CryOf into suffix; color names mix matches upstream |
| 29 | 0x085442D4 | 0x085C9186 | gText_DexSearchColorYellow | きいろ | 黄 | ok-intentional | matches us_chs split CryOf into suffix; color names mix matches upstream |
| 30 | 0x085442DC | 0x085C918A | gText_DexSearchColorGreen | みどり | 绿 | ok-intentional | matches us_chs split CryOf into suffix; color names mix matches upstream |
| 31 | 0x085442E4 | 0x085C918E | gText_DexSearchColorBlack | くろ | 黑色 | ok-intentional | matches us_chs split CryOf into suffix; color names mix matches upstream |
| 32 | 0x085442EC | 0x085C9191 | gText_DexSearchColorBrown | ちゃいろ | 棕 | ok-intentional | matches us_chs split CryOf into suffix; color names mix matches upstream |
| 33 | 0x085442F4 | 0x085C9196 | gText_DexSearchColorPurple | むらさき | 紫 | ok-intentional | matches us_chs split CryOf into suffix; color names mix matches upstream |
| 34 | 0x085442FC | 0x085C919B | gText_DexSearchColorGray | はいいろ | 灰 | ok-intentional | matches us_chs split CryOf into suffix; color names mix matches upstream |
| 35 | 0x08544304 | 0x085C91A0 | gText_DexSearchColorWhite | しろ | 白 | ok-intentional | matches us_chs split CryOf into suffix; color names mix matches upstream |
| 36 | 0x0854430C | 0x085C91A3 | gText_DexSearchColorPink | ピンク | 粉色 | ok-intentional | matches us_chs split CryOf into suffix; color names mix matches upstream |
| 37 | 0x08544210 | 0x085C91A7 | gText_DexHoennDescription | ホウエンちほう　ばん　ポケモンずかん | 丰缘地区的图鉴 | ok | PTR-OK, CN faithful |
| 38 | 0x08544218 | 0x085C91BA | gText_DexNatDescription | ぜんこく　ばん　ポケモンずかん | 全国版本的图鉴 | ok | PTR-OK, CN faithful |
| 39 | 0x08544228 | 0x085C91CA | gText_DexSortNumericalDescription | ポケモンを\nばんごうじゅんで　ひょうじ　します | 按图鉴的编号来\n排列宝可梦。 | ok | PTR-OK, CN faithful |
| 40 | 0x08544230 | 0x085C91E2 | gText_DexSortAtoZDescription | みつけたポケモンの　なまえを\nごじゅうおんじゅんで　ひょうじ　します | 按名称顺序排列\n已发现的宝可梦。 | ok | PTR-OK, CN faithful |
| 41 | 0x08544238 | 0x085C9205 | gText_DexSortHeaviestDescription | つかまえたポケモンを\nおもい　じゅんばんで　ひょうじ　します | 按重到轻的顺序来排列\n已获得的宝可梦。 | ok | PTR-OK, CN faithful |
| 42 | 0x08544240 | 0x085C9224 | gText_DexSortLightestDescription | つかまえたポケモンを\nかるい　じゅんばんで　ひょうじ　します | 按轻到重的顺序来排列\n已获得的宝可梦。 | ok | PTR-OK, CN faithful |
| 43 | 0x08544248 | 0x085C9243 | gText_DexSortTallestDescription | つかまえたポケモンを\nしんちょうのたかい　じゅんばんで　ひょうじ　します | 按高到低的顺序来排列\n已获得的宝可梦。 | ok | PTR-OK, CN faithful |
| 44 | 0x08544250 | 0x085C9268 | gText_DexSortSmallestDescription | つかまえたポケモンを\nしんちょうのひくい　じゅんばんで　ひょうじ　します | 按低到高的顺序来排列\n已获得的宝可梦。 | ok | PTR-OK, CN faithful |
| 45 | 0x08544264 | 0x085C928E | gText_DexSearchDontSpecify | してい　しない | 不指定 | ok | PTR-OK, CN faithful |
| 46 | 0x085442BC | 0x085C928E | gText_DexSearchDontSpecify | してい　しない | 不指定 | ok | PTR-OK, CN faithful |
| 47 | 0x0854431C | 0x085C9296 | gText_DexSearchTypeNone | なし | 无 | ok | PTR-OK, CN faithful |
