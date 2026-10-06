# Manual review: 022_dewford_town.json

verdicts: {'ok': 27, 'ok-intentional': 1}

| # | address | original | symbol | JP | CN | verdict | notes |
|---|---|---|---|---|---|---|---|
| 0 | 0x081E76BC | 0x081E522C | DewfordTown_Text_BrineyLandedInDewford | ハギ“ほい！　ムロタウンに　とうちゃく！{FB}ふねに　のりたくなったら\nまた　わしに　こえを　かけておくれ！ | 哈奇：喂！\n我们到武斗镇了！{FB}想再出海随时叫我！ | ok | script msgbox/message words; CN faithful |
| 1 | 0x081E874B | 0x081E522C | DewfordTown_Text_BrineyLandedInDewford | ハギ“ほい！　ムロタウンに　とうちゃく！{FB}ふねに　のりたくなったら\nまた　わしに　こえを　かけておくれ！ | 哈奇：喂！\n我们到武斗镇了！{FB}想再出海随时叫我！ | ok | script msgbox/message words; CN faithful |
| 2 | 0x081E4EEB | 0x081E8BC7 | DewfordTown_Text_BrineyLandedInSlateport | ハギ“ほい！　カイナに　とうちゃく！{FB}ふねに　のりたくなったら\nまた　わしに　こえを　かけておくれ！ | 哈奇：好了！\n我们到凯那市了！{FB}你还想出海的话\n就来找我吧！ | ok | script msgbox/message words; CN faithful |
| 3 | 0x081E4EE2 | 0x081E8B34 | DewfordTown_Text_BrineyLandedInSlateportDeliverGoods | ハギ“ほい！　カイナに　とうちゃく！{FB}たしか　クスノキさんに\nデボンのにもつを　とどけるんだったな！ | 哈奇：好了！\n我们到凯那市了！{FB}我想你是要去找\n楠木馆长送得文的物品吧？ | ok | script msgbox/message words; CN faithful |
| 4 | 0x081E4DA8 | 0x081E5420 | DewfordTown_Text_FishingAdvice | なんだよ　ガッカリ　しないでよ！\nつりの　コツを　おしえて　あげるから！{FB}まずは　すいめんに　むかって\nつりざおを　つかう！{FB}そして　きもちを　しゅうちゅう　させ⋯⋯\nひいてる　ひいてる！！　となったら{FA}すばやく　つりざおを　ひくんだ！{FB}すぐに　ひきあげられる　ときも　あるけど\nおおものは　なんども　タイミングを{FA}あわせる　ひつようが　あるんだよ！ | 好了，别沮丧，！\n我给你点钓鱼的建议。{FB}首先，面对水面，\n甩出钓竿。{FB}集中精神⋯⋯\n鱼咬钩的时候，拉起钓竿。{FB}有时你马上就能钓到什么，\n但想钓大家伙的话，{FA}你就得计算好钓竿的晃动次数{FA}才能拖它们上来。 | ok-intentional | US汉化 upstream typo '别沮丧，！' (extra ， before ！); recorded in FINDINGS.md |
| 5 | 0x081E4D32 | 0x081E52F3 | DewfordTown_Text_GettingItchToFish | このへんは　つりの　めいしょ　なんだ\nきみも　つりが　したくなった？ | 这里是著名的钓场。\n你渴望钓鱼吗？ | ok | script msgbox/message words; CN faithful |
| 6 | 0x081E4D51 | 0x081E5316 | DewfordTown_Text_GiveYouOneOfMyRods | うんうん　うれしいな\nわたしの　つりざお　わけてあげよう！ | 我听到了，\n我真高兴你能这么说！{FB}我就把我的钓竿给你一支吧。 | ok | script msgbox/message words; CN faithful |
| 7 | 0x081E4CEA | 0x081E5209 | DewfordTown_Text_GoDeliverIllBeWaiting | ハギ“では　てがみを　とどけておいで\nわしは　ここで　まっておるから | 哈奇：那你去送信吧，\n我就在这儿等着。 | ok | script msgbox/message words; CN faithful |
| 8 | 0x081E4D9E | 0x081E5401 | DewfordTown_Text_GreatHaulInSomeBigOnes | そうか！　そりゃ　すごい！\nおおものを　つりあげて　くれよ！ | 是吗！太好了！\n继续钓更大的鱼吧！ | ok | script msgbox/message words; CN faithful |
| 9 | 0x081E4D15 | 0x081E5149 | DewfordTown_Text_GymSign | ムロ　タウン　ポケモンジム\nリーダー　トウキ{FA}かくとう　ビッグウェーブ！ | 武斗镇宝可梦道馆\n馆主：藤树{FA}“格斗浪潮！” | ok | script msgbox/message words; CN faithful |
| 10 | 0x081E4D1E | 0x081E516E | DewfordTown_Text_HallSign | ‘ムロの　しゅうかいじょ’\nみんなの　じょうほう　こうかんの　ばしょ | 武斗镇大厅\n“信息交换处！” | ok | script msgbox/message words; CN faithful |
| 11 | 0x081E50E6 | 0x081E5626 | DewfordTown_Text_HearOfAnyTrendsComeShareWithMe | じゃあ　あたらしい　りゅうこうが　あったら\nまた　きかせて　くれよ！ | 那，如果你听说了什么\n新的流行词，来跟我说说好吗？ | ok | script msgbox/message words; CN faithful |
| 12 | 0x081E4D7B | 0x081E53EF | DewfordTown_Text_HowsYourFishing | よっ！\nつりの　ちょうしは　どう？ | 哟！\n鱼钓得怎么样了？ | ok | script msgbox/message words; CN faithful |
| 13 | 0x081E4CCC | 0x081E52CD | DewfordTown_Text_JustTellMeWhenYouNeedToSetSail | ハギ“ふねに　のる　ひつようが　あるときは\nいつでも　こえを　かけておくれ | 哈奇：想再出海随时叫我！ | ok | script msgbox/message words; CN faithful |
| 14 | 0x081E50DC | 0x081E556D | DewfordTown_Text_OfCourseIKnowAboutThat | え？　“{STR_VAR_2}”？{FB}⋯⋯{FB}⋯あ！　あぁ！\nしってる　しってるよ！{FB}もっ　もちろん　しってるさ！\n“{STR_VAR_2}”　だろ？{FB}いいよね！\n“{STR_VAR_2}”　って！{FB}いま　すごく　はやってる　よね\nぼくが　しらないはず　ないじゃ　ないか！{FB}“{STR_VAR_1}”　なんて\nもう　じだいおくれ{FB}いまは　“{STR_VAR_2}”の\nじだい　だね！ | 呃？\n“{STR_VAR_2}”？{FB}⋯⋯{FB}⋯⋯呃⋯⋯对！没错！\n我知道！一直都知道！{FB}我当然知道！\n“{STR_VAR_2}”，对吗？{FB}对，是它，就是它！\n“{STR_VAR_2}”{FA}不就是最酷的词吗？{FB}不就是在潮流最尖端的词吗？\n你以为我不知道吗？{FB}“{STR_VAR_1}”⋯⋯\n那只是，呃，五分钟前的事了，{FB}现在，“{STR_VAR_2}”才是\n最重要最时兴的！ | ok | script msgbox/message words; CN faithful |
| 15 | 0x081E4CAC | 0x081E5291 | DewfordTown_Text_PetalburgWereSettingSail | ハギ“トウカシティ　か{FB}よっしゃ！　いくぞ　ピーコちゃん！ | 哈奇：橙华市是吗？{FB}起锚！\n小皮，亲爱的，出海了！ | ok | script msgbox/message words; CN faithful |
| 16 | 0x081E4CF4 | 0x081E51E2 | DewfordTown_Text_PetalburgWereSettingSail2 | ハギ“では　トウカに　もどると　しよう！{FB}よっしゃ！　いくぞ　ピーコちゃん！ | 哈奇：目标，橙华市！{FB}起锚！\n小皮，亲爱的，出海了！ | ok | script msgbox/message words; CN faithful |
| 17 | 0x081E4CD7 | 0x081E51BF | DewfordTown_Text_SetSailBackToPetalburg | ハギ“てがみは　とどけたのかい？{FB}それとも　トウカに　もどるのかね？ | 哈奇：你已经送完信了吗？{FB}还是你想回橙华市去？ | ok | script msgbox/message words; CN faithful |
| 18 | 0x081E4CBC | 0x081E52AF | DewfordTown_Text_SlateportWereSettingSail | ハギ“カイナシティ　か{FB}よっしゃ！　いくぞ　ピーコちゃん！ | 哈奇：凯那市是吗？{FB}起锚！\n小皮，亲爱的，出海了！ | ok | script msgbox/message words; CN faithful |
| 19 | 0x081E50A4 | 0x081E5546 | DewfordTown_Text_TellMeWhatsNewAndIn | え？\nはやって　ないの！？{FB}じゃあ　いま　なにが　はやってるか\nきかせてよ！ | 嗯？\n这不是现在最流行的吗？{FB}哎，那么，你得告诉我，\n现在最流行的是什么？ | ok | script msgbox/message words; CN faithful |
| 20 | 0x081E4D72 | 0x081E53E0 | DewfordTown_Text_ThatsTooBadThen | あらら⋯⋯\nそれは　ざんねん | 哦，是吗？\n真遗憾。 | ok | script msgbox/message words; CN faithful |
| 21 | 0x081E4D68 | 0x081E5334 | DewfordTown_Text_ThrowInFishingAdvice | よーしっ　だいサービス！\nつりの　コツも　せつめい　しておくよ！{FB}まずは　すいめんに　むかって\nつりざおを　つかう！{FB}そして　きもちを　しゅうちゅう　させ⋯⋯\nひいてる　ひいてる！！　となったら{FA}すばやく　つりざおを　ひくんだ！{FB}すぐに　ひきあげられる　ときも　あるけど\nおおものは　なんども　タイミングを{FA}あわせる　ひつようが　あるんだよ！ | 作为附送，\n我给你几条钓鱼的建议吧！{FB}首先，面对水面，\n甩出钓竿。{FB}集中精神⋯⋯\n鱼咬钩的时候，拉起钓竿。{FB}有时你马上就能钓到什么，\n但想钓大家伙的话，{FA}你就得计算好钓的晃动次数{FA}才能拖它们上来。 | ok | script msgbox/message words; CN faithful |
| 22 | 0x081E4D03 | 0x081E50F8 | DewfordTown_Text_TinyIslandCommunity | ムロタウンって　ちいさな　しま　だから\nなにかが　はやりだすと{FA}みんな　すぐに　まねを　するのよね | 武斗镇是个很小的岛镇，\n如果什么在这儿流行起来，{FA}很快所有人都会开始谈论。 | ok | script msgbox/message words; CN faithful |
| 23 | 0x081E4D0C | 0x081E512A | DewfordTown_Text_TownSign | ここは　ムロ　タウン\nあおい　うみに　うかぶ　ちいさな　しま | 这里是武斗镇。\n“漂浮在蓝海上的小岛。” | ok | script msgbox/message words; CN faithful |
| 24 | 0x081E4C6D | 0x081E5261 | DewfordTown_Text_WhereAreWeBound | ハギ“やあ！　きみのため　なら\nいつでも　ふねを　だそう！{FB}きみが　いきたいのは　どこ　かな？ | 哈奇：喂！\n为了你我随时都能出海！{FB}说吧朋友，\n这次想去哪儿？ | ok | script msgbox/message words; CN faithful |
| 25 | 0x081E50F0 | 0x081E55FE | DewfordTown_Text_XHuhIThinkYIsCool | ふーん\n“{STR_VAR_2}”　か⋯{FB}でも　ぼくは\n“{STR_VAR_1}”　のほうが{FA}いいと　おもうけどね | 唔⋯⋯\n“{STR_VAR_2}”？{FB}但我觉得，\n“{STR_VAR_1}”{FA}才是最棒的。 | ok | script msgbox/message words; CN faithful |
| 26 | 0x081E507B | 0x081E54D0 | DewfordTown_Text_XIsTheBiggestHappeningThingRight | ぼく　はやってる　ものが　すきで\nいつも　チェック　してるんだ{FB}ねぇ　“{STR_VAR_1}”って\nしってるかい？{FB}もちろん　しってるよね！{FB}だって　いま\n“{STR_VAR_1}”が{FA}だいりゅうこう　してるからね！{FB}きみの　まわりでも\n“{STR_VAR_1}”が{FA}はやってる　だろ？ | 我知道什么在发生，什么最时髦，\n我一直在调查。{FB}你听说过这个新词\n“{STR_VAR_1}”吗？{FB}没错！\n你当然知道！{FB}我是说，嘘\n“{STR_VAR_1}”⋯⋯{FA}是现在最新最热的词！{FB}无论你从哪儿来，\n“{STR_VAR_1}”{FA}都是最重要的事，对吗？ | ok | script msgbox/message words; CN faithful |
| 27 | 0x081E509A | 0x081E5649 | DewfordTown_Text_YeahDefinitionOfInRightNow | そうだろ！{FB}やっぱり　いまは\n“{STR_VAR_1}”　だよね！ | 没错，完全正确！{FB}现在“{STR_VAR_1}”\n就是流行！ | ok | script msgbox/message words; CN faithful |
