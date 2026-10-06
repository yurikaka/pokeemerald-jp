# Manual review: 034_rustborocity_flat1_2f.json

verdicts: {'ok': 15}

| # | address | original | symbol | JP | CN | verdict | notes |
|---|---|---|---|---|---|---|---|
| 0 | 0x082037E6 | 0x0820398A | RustboroCity_Flat1_2F_Text_BeenSayingXDoYouKnowBetterPhrase | いまは　{STR_VAR_1}　って\nことばを　つかってるんだけど{FB}おもしろそうな　ことば\nみつけて　きたの？ | 我最近试过说\n“{STR_VAR_1}”逗她笑，{FB}你还知道什么\n更好点的短语吗？ | ok | script msgbox words; CN faithful |
| 1 | 0x08203876 | 0x08203886 | RustboroCity_Flat1_2F_Text_ComingUpWithMealsIsHard | もうね　たいへん　なのよ！{FB}なにが　たいへんって\nそんなの　きまってるでしょ！{FB}まいにちの　おこんだて　よッ！{FB}まいにち　まいにち　かんがえるのって\nほんとうに　たいへん　なんだからッ！ | 唉，天天这样太难了⋯⋯{FB}什么难？\n还用问吗？{FB}当然是考虑一天三餐\n该吃什么。{FB}每天都想着做什么饭\n也不容易。 | ok | script msgbox words; CN faithful |
| 2 | 0x082037C6 | 0x082038E4 | RustboroCity_Flat1_2F_Text_HelloDoYouKnowFunnyPhrase | やあ　いらっしゃい\nハコガミけ　へ　ようこそ！{FB}ちょっと　しつもんが　あるんだけど\nきみ　こもり　したこと　ある？{FB}おじさん　はじめて\nいくじ　してるんだけどさ{FB}うちの　アヤノ\nなかなか　わらって　くれないんだよね{FB}おもしろーい　ことば　で\nわらって　くれないかなーって{FA}おもうんだけど{FA}おもしろーい　ことば　おしえて　くれない？ | 哎，你好！\n欢迎来到箱神家。{FB}问你一个问题，\n你带过小孩吗？{FB}你看，我刚当上爸爸，\n抚养孩子什么的都得从头学。{FB}我现在有点麻烦，\n女儿文乃总是不爱笑。{FB}我想如果给她讲笑话\n她就会笑起来的。{FB}你知道什么有趣的故事\n或短语吗？ | ok | script msgbox words; CN faithful |
| 3 | 0x0820387F | 0x08203BB9 | RustboroCity_Flat1_2F_Text_ItsAPokemonPlushDoll | ポケモンの　ぬいぐるみ　だ！ | 是宝可梦毛绒玩具！ | ok | script msgbox words; CN faithful |
| 4 | 0x0820385A | 0x08203A2F | RustboroCity_Flat1_2F_Text_LetsGiveItATry | なるほどー\nじゃあ　ためして　みようかな | 啊，知道了。\n来试试吧？ | ok | script msgbox words; CN faithful |
| 5 | 0x08203831 | 0x082039FB | RustboroCity_Flat1_2F_Text_LetsGiveItATry2 | なるほどー\nじゃあ　ためして　みようかな | 啊，知道了。\n来试试吧？ | ok | script msgbox words; CN faithful |
| 6 | 0x08203806 | 0x082039D3 | RustboroCity_Flat1_2F_Text_OhIsThatRight | そうか　そうか\nなにか　おもしろそうな　ことばを{FA}みつけたら　おしえて　くれよ | 唉，是吗？{FB}如果你想到什么好主意，\n我洗耳恭听。 | ok | script msgbox words; CN faithful |
| 7 | 0x0820383E | 0x08203A10 | RustboroCity_Flat1_2F_Text_OhShesLaughing | {STR_VAR_1}\n{STR_VAR_1}{FB}わらってる　わらってる！\nなんだか　うれしいなあ | {STR_VAR_1}\n{STR_VAR_1}{FB}啊，太好了，她笑了！\n啊，我也跟她一样开心！ | ok | script msgbox words; CN faithful |
| 8 | 0x08203810 | 0x08203ABC | RustboroCity_Flat1_2F_Text_OhYouDontKnowAny | いい　ことば　しらないかー\nじゃあ　まえの　ことばで{FA}がんばって　あやすかー{FB}おもしろそうな　ことば　みつけたら\nおじさんに　おしえてね | 唉，你也不知道什么好短语啊。\n看来我只能用上次的短语{FA}逗她笑了。{FB}对了，如果你想到了什么，\n要赶快告诉我，好吗？ | ok | script msgbox words; CN faithful |
| 9 | 0x08203867 | 0x08203A44 | RustboroCity_Flat1_2F_Text_ShesNotSmilingAtAll | {STR_VAR_1}\n{STR_VAR_1}{FB}うーん　わらわないなあ\nこのこ　クール　なのかな | {STR_VAR_1}\n{STR_VAR_1}{FB}唔⋯⋯她根本不笑。\n也许文乃生来就很严肃⋯⋯ | ok | script msgbox words; CN faithful |
| 10 | 0x08203827 | 0x08203A9D | RustboroCity_Flat1_2F_Text_ShesNotSmilingAtAll2 | {STR_VAR_1}\n{STR_VAR_1}{FB}うーん　わらわないなあ\nこのこ　クール　なのかな | {STR_VAR_1}\n{STR_VAR_1}{FB}唔⋯⋯她根本不笑。\n也许文乃生来就很严肃⋯⋯ | ok | script msgbox words; CN faithful |
| 11 | 0x08203850 | 0x08203B01 | RustboroCity_Flat1_2F_Text_ThankYouIllGiveYouWallpaper | ありがとう！{FB}きみの　おかげで　アヤノが\nわらって　くれたよ！{FB}じつは　おじさん\nこう　みえても{FB}デボンコーポレーションの\nすごうで　けんきゅういん　なんだよ{FB}そうだなー　じゃあ　おれいに\nきみが　ポケモンを　あずけている{FA}ボックスの　かべがみを{FA}ふやして　あげよう！{FB}かべがみの　なかから\n‘だいすき’って　いうのを　えらぶと{FA}あたらしい　かべがみが　えらべるよ！ | 谢谢！{FB}多亏了你，我亲爱的文乃\n开始笑了！{FB}实际上，虽然我看起来\n很普通，但我是得文{FA}公司的主力研究员之一。{FB}我该做点什么\n报答你？{FB}对了，我给你的\n电脑宝可梦寄放系统里的{FA}盒子加些新的背景图片吧。{FB}在选择背景图案的菜单中\n选择“朋友”，{FB}就能连接到\n新的背景图片。 | ok | script msgbox words; CN faithful |
| 12 | 0x0820381A | 0x08203A63 | RustboroCity_Flat1_2F_Text_ThinkOfMyOwnPhrase | いい　ことば　しらないかー\nじゃあ　じぶんで　かんがえるかー{FB}うーん\n{STR_VAR_1}　とか　どうかな{FA}よし！　ためしてみよう | 唉，你也不知道什么好短语啊。\n那我只能自己想一个了。{FB}嗯⋯⋯\n“{STR_VAR_1}”怎么样？{FA}我们试试看。 | ok | script msgbox words; CN faithful |
| 13 | 0x082037D9 | 0x082039B9 | RustboroCity_Flat1_2F_Text_WonderfulLetsHearSuggestion | そうか　そうか\nじゃあ　さっそく　おしえて　くれよ | 哎，不错，那就听你的，\n说给她听听吧。 | ok | script msgbox words; CN faithful |
| 14 | 0x082037F9 | 0x082039B9 | RustboroCity_Flat1_2F_Text_WonderfulLetsHearSuggestion | そうか　そうか\nじゃあ　さっそく　おしえて　くれよ | 哎，不错，那就听你的，\n说给她听听吧。 | ok | script msgbox words; CN faithful |
