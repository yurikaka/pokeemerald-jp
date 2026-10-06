# Manual review: 031_rustborocity_devoncorp_1f.json

verdicts: {'ok': 11}

| # | address | original | symbol | JP | CN | verdict | notes |
|---|---|---|---|---|---|---|---|
| 0 | 0x082010B1 | 0x08201249 | RustboroCity_DevonCorp_1F_Text_HowCouldWeGetRobbed | どろぼうに　にもつを　うばわれるなんて\nなんて　ドジなんだろう⋯⋯ | 包裹居然被抢走了，\n我们也太不小心了⋯⋯ | ok | script msgbox words; CN faithful |
| 1 | 0x0820109D | 0x08201222 | RustboroCity_DevonCorp_1F_Text_OnlyAuthorizedPeopleEnter | おっと　かんけいしゃ　いがいの　かたは\nここから　さきには　はいれませんよ！ | 对不起，\n无关人士请勿入内。 | ok | script msgbox words; CN faithful |
| 2 | 0x082010FF | 0x08201357 | RustboroCity_DevonCorp_1F_Text_ProductDisplay | いろんな　どうぐの　しさくひんが\nガラスケースの　なかに　ならんでいる！{FB}パネルに　せつめいが　かいてあるから\nよんでみよう⋯⋯{FB}‘げんざい　デボン　コーポレーションでは\n　こうぎょう　せいひんの　ほかにも{FA}　にちようひんや　くすりなど{FB}　ひとびとの　くらしに　やくだつ　ものを\n　かいはつ　しています’{FB}‘また　げんざいでは　モンスターボールや\n　ポケナビなどの　トレーナーようひんも{FA}　てがけるように　なりました’ | 玻璃展示柜里放了些\n产品的原型和试验品。{FB}有张卡片上写着说明⋯⋯{FB}“除工业产品外，\n得文如今也开发{FA}日常用品与药品。{FB}近年来，得文致力于\n为宝可梦训练家开发包括精灵球和{FA}宝可导航系统等一系列工具。” | ok | script msgbox words; CN faithful |
| 3 | 0x0820106C | 0x082011A8 | RustboroCity_DevonCorp_1F_Text_RobberWasntVeryBright | たしかに　あの　にもつは\nだいじな　もの　だけど{FA}ほかの　ひとが　ぬすんでいっても{FA}つかえないと　おもうんだよね{FB}ぼくの　すいりでは　あの　どろぼう⋯⋯\nたんなる　マヌケ　なんじゃないかな？ | 被偷走的包裹⋯⋯{FB}虽然确实很重要，\n但也不是所有人都会使用的东西。{FB}我看那个强盗\n没那么聪明。 | ok | script msgbox words; CN faithful |
| 4 | 0x082010F6 | 0x08201284 | RustboroCity_DevonCorp_1F_Text_RocksMetalDisplay | いしや　きんぞくの　サンプルが\nガラスケースの　なかに　ならんでいる！{FB}パネルに　せつめいが　かいてあるから\nよんでみよう⋯⋯{FB}‘デボン　コーポレーションは　もともと\n　やまから　いしを　きりだしたり{FB}　さてつから　てつざいを　つくるために\n　せつりつ　された　かいしゃ　です’{FB}‘やがて　デボン　コーポレーションは\n　ざいりょう　だけに　とどまらず{FB}　さまざまな　こうぎょう　せいひんも\n　つくるように　なったのです’ | 玻璃箱子里展示着\n岩石和金属的样品，{FB}上面有张卡片上\n写了些什么⋯⋯{FB}“得文公司创立时\n仅仅是一家以采石为业的小公司，{FB}同时也利用沙子中的\n铁屑炼铁。{FB}得文从一个微小的\n原材料处理公司起家，{FB}现在已发展成为一个开发出的产品\n覆盖很多工业领域的大型制造商。” | ok | script msgbox words; CN faithful |
| 5 | 0x08201076 | 0x08201208 | RustboroCity_DevonCorp_1F_Text_SoundsLikeStolenGoodsRecovered | どうやら　デボンのにもつは\nもどってきた　らしいね | 听说被抢走的得文的物品\n找回来了。 | ok | script msgbox words; CN faithful |
| 6 | 0x082010EC | 0x08201146 | RustboroCity_DevonCorp_1F_Text_StaffGotRobbed | ドジな　けんきゅういんが\nにもつを　とられちゃって⋯⋯ | 我们的一个调查员被人\n把很重要的包裹抢走了。 | ok | script msgbox words; CN faithful |
| 7 | 0x08201062 | 0x08201162 | RustboroCity_DevonCorp_1F_Text_ThoseShoesAreOurProduct | おっ！　ランニングシューズ！{FB}じぶんたちの　かいしゃの　しょうひんを\nじっさいに　つかっている　ひとを　みると{FA}すごく　うれしくなるよね！ | 哎，那是跑步鞋！\n那也是我们的产品！{FB}每次看到别人使用我们的发明，\n我都会很高兴。 | ok | script msgbox words; CN faithful |
| 8 | 0x082010D8 | 0x08201106 | RustboroCity_DevonCorp_1F_Text_WelcomeToDevonCorp | いらっしゃいませ！\nデボン　コーポレーション　です！{FB}みなさまの　せいかつに　やくだつ\nどうぐや　くすりを　おつくりしてます！ | 您好，欢迎来到\n得文公司。{FB}我们公司发明\n改变人们生活的药品和道具。 | ok | script msgbox words; CN faithful |
| 9 | 0x082010E2 | 0x08201106 | RustboroCity_DevonCorp_1F_Text_WelcomeToDevonCorp | いらっしゃいませ！\nデボン　コーポレーション　です！{FB}みなさまの　せいかつに　やくだつ\nどうぐや　くすりを　おつくりしてます！ | 您好，欢迎来到\n得文公司。{FB}我们公司发明\n改变人们生活的药品和道具。 | ok | script msgbox words; CN faithful |
| 10 | 0x082010A7 | 0x0820126B | RustboroCity_DevonCorp_1F_Text_YoureAlwaysWelcomeHere | やあ！\nきみなら　いつでも　だいかんげい　だよ！ | 您好！\n随时欢迎您来参观！ | ok | script msgbox words; CN faithful |
