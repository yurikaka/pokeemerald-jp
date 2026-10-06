# Manual review: 039_rusturftunnel.json

verdicts: {'ok': 16}

| # | address | original | symbol | JP | CN | verdict | notes |
|---|---|---|---|---|---|---|---|
| 0 | 0x0821362C | 0x08213CF3 | RusturfTunnel_Text_BoyfriendOnOtherSideOfRock | この　いわの　むこうに⋯⋯\nわたしの　かれが　いるの{FB}かれ⋯⋯　わたしに　あうため　だけに\nトンネルを　ほってるわけ　じゃないわ{FB}みんなの　ために\nてを　きずつけながらも　がんばってるの | 在岩石的另一边⋯⋯\n是我的男朋友。{FB}他⋯⋯他挖隧道不只是\n为了见我，{FB}他磨破双手、任劳任怨，\n也是为了大家。 | ok | script msgbox/message/trainerbattle words; CN faithful |
| 1 | 0x0821384F | 0x08213991 | RusturfTunnel_Text_ComeAndGetSome | くるのか？\nくるなら　こいよ！ | 怎么，想过来？\n那就放马过来啊！ | ok | script msgbox/message/trainerbattle words; CN faithful |
| 2 | 0x082136CD | 0x08213C7B | RusturfTunnel_Text_ExplainStrength | そいつには　かいりきが　はいっている\nちからもちの　ポケモンに　おぼえさせれば{FA}おおきな　いわを　うごかせるよ | 那个秘传学习器\n里面是怪力。{FB}让力量大的宝可梦学会的话，\n就能够移动更大的石头了。 | ok | script msgbox/message/trainerbattle words; CN faithful |
| 3 | 0x0821389F | 0x08213A18 | RusturfTunnel_Text_GruntDefeat | む　むぐぐー！\nおれの　あくじも　いきどまりかっ！ | 呃啊啊！\n我的犯罪生涯看来要到头了！ | ok | script msgbox/message/trainerbattle words; CN faithful |
| 4 | 0x08213893 | 0x082139B0 | RusturfTunnel_Text_GruntIntro | えーい　くっそー！{FB}うばった　ポケモンは\nなんの　やくにも　たたないし{FB}いいところへ　にげこめたと　おもったのに\nこの　トンネル　いきどまり　じゃねーか！{FB}やい！　おまえ！\nおれと　しょうぶ　するんだな！？ | 该死，真见鬼！{FB}那只当人质的宝可梦\n根本派不上用场！{FB}亏我还拼命逃跑⋯⋯\n逃进了一个死胡同隧道！{FB}嘿！说你呢！\n你想和我打一场是吧？ | ok | script msgbox/message/trainerbattle words; CN faithful |
| 5 | 0x082138A5 | 0x08213A32 | RusturfTunnel_Text_GruntTakePackage | おかしいなあ⋯⋯{FB}リーダーの　はなしでは　なにかの　にもつを\nデボンから　ぬすんでくる　っていう{FA}らくな　しごと　だった　はずなのに⋯⋯{FB}ちぇっ！\nこんなもん　かえして　やらあ！ | 太离谱了⋯⋯{FB}老大明明告诉我\n这任务易如反掌。{FB}只要从得文公司\n偷个包裹就行⋯⋯{FB}切！\n这么想要就还给你！ | ok | script msgbox/message/trainerbattle words; CN faithful |
| 6 | 0x08213984 | 0x08213D8C | RusturfTunnel_Text_MikeDefeat | ポケモン⋯⋯\nちから　つきた⋯⋯ | 我的宝可梦⋯⋯\n耗尽力量了⋯⋯ | ok | script msgbox/message/trainerbattle words; CN faithful |
| 7 | 0x08213980 | 0x08213D51 | RusturfTunnel_Text_MikeIntro | おとこが　やまに　いるから　やまおとこ！{FB}なのに　ポケモンが　やまに　いても\nやまポケモンと　いわないのは　なぜだ？ | 你怎么称呼住在山里的野人？\n登山男，对不对？{FB}为什么不把生活在山里的宝可梦\n叫作登山宝可梦呢？ | ok | script msgbox/message/trainerbattle words; CN faithful |
| 8 | 0x0821398A | 0x08213D9D | RusturfTunnel_Text_MikePostBattle | ここって　ポケモンを　まもるため\nかいはつ　こうじを　やめたんだろ？{FA}それって　いい　はなし　だよな | 他们停工是为了\n保护宝可梦吧？\n真是个暖心故事！ | ok | script msgbox/message/trainerbattle words; CN faithful |
| 9 | 0x08213882 | 0x082139A1 | RusturfTunnel_Text_Peeko | ピーコちゃん“ピ　ピひょー！ | 小皮：皮——皮可！ | ok | script msgbox/message/trainerbattle words; CN faithful |
| 10 | 0x082138EF | 0x08213A8C | RusturfTunnel_Text_PeekoGladToSeeYouSafe | ピーコちゃん！　ぶじで　よかった！ | 小皮！\n你平安无事真是太好了！ | ok | script msgbox/message/trainerbattle words; CN faithful |
| 11 | 0x08213900 | 0x08213A9E | RusturfTunnel_Text_ThankYouLetsGoHomePeeko | あんたは　ピーコちゃんの\nいのちの　おんじん　じゃよ！{FB}わしは　ハギと　いうのじゃが\nきみは⋯⋯？{FB}⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯{FB}そうか　{PLAYER}{KUN}と　いうのか！\nほんとうに　ありがとうよ！{FB}これからさき　こまった　ことが　あったら\nえんりょなく　わしに　いっとくれ！{FB}いつもは　トウカのもりの　ちかくに　ある\nはまべの　こやに　いるからの！{FB}さあ　ピーコちゃん\nわしらの　おうちに　かえろうな！{FB}ピーコちゃん“ピひょーっ！！ | 你是小皮的救命恩人啊！{FB}大家都叫我哈奇老人。\n你是⋯⋯？{FB}⋯⋯　⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯　⋯⋯{FB}原来如此，是{PLAYER}{KUN}啊！\n真的太感谢你了！{FB}以后遇到什么困难\n尽管来找我！{FB}我平时就住在橙华森林\n附近的海边小屋。{FB}来吧，小皮，\n我们回家了。{FB}小皮：皮可！ | ok | script msgbox/message/trainerbattle words; CN faithful |
| 12 | 0x08213664 | 0x08213C05 | RusturfTunnel_Text_ToGetToVerdanturf | カナズミから　シダケに　いこうと　すると\nムロから　カイナと　キンセツを　とおって{FA}いかなきゃ　ならないんだ⋯⋯ | 想要从卡那兹市到绿茵镇，\n你得先到武斗镇，然后穿过{FA}凯那市和紫堇市⋯⋯ | ok | script msgbox/message/trainerbattle words; CN faithful |
| 13 | 0x082136F7 | 0x08213CB3 | RusturfTunnel_Text_WandaReunion | ミチルさん！\nこれから　いつでも　あえます！{FB}ミチル“よかった⋯⋯　です{FB}さあ　わたしの　いえで\nゆっくり　やすんで　ください | 满盈！\n现在我可以随时看到你了！{FB}满盈：真的⋯⋯太好了。{FB}请来我家好好休息吧。 | ok | script msgbox/message/trainerbattle words; CN faithful |
| 14 | 0x0821364F | 0x08213B76 | RusturfTunnel_Text_WhyCantTheyKeepDigging | ⋯⋯{FB}どうして　これいじょう　ほれない⋯⋯\nこの　いわが　かたすぎるのか？{FB}このさきの　シダケタウンという　ところに\nあいする　かのじょが　いるのに⋯⋯{FB}カナズミと　シダケを　トンネルで　むすべば\nまいにち　かのじょに　あいに　いける{FB}それなのに⋯⋯\nおれは　どうすれば　いいんだ⋯⋯ | ⋯⋯{FB}为什么他们停工了？\n是因为岩床太硬吗？{FB}我心爱的人就在隧道那头的\n绿茵镇等着我⋯⋯{FB}如果这条隧道能连通\n卡那兹市和绿茵镇，{FA}我就能天天见到她了⋯⋯{FB}可是现在⋯⋯\n我该怎么办？ | ok | script msgbox/message/trainerbattle words; CN faithful |
| 15 | 0x082136A0 | 0x08213C3E | RusturfTunnel_Text_YouShatteredBoulderTakeHM | なんと！　きみが　この　いわを\nくだいて　くれたんだね{FB}かんしゃの　しるし　として\nこの　ひでんマシンを　うけとってくれ | 哇喔！\n你打碎了挡路的大石头。{FB}这个秘传学习器送给你，\n就当作是我的谢礼吧。 | ok | script msgbox/message/trainerbattle words; CN faithful |
