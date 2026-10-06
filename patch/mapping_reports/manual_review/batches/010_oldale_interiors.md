# Manual review: 010_oldale_interiors.json

verdicts: {'ok': 10}

| # | address | original | symbol | JP | CN | verdict | notes |
|---|---|---|---|---|---|---|---|
| 0 | 0x081F28D6 | 0x081F28DD | OldaleTown_House1_Text_LeftPokemonGoesOutFirst | ポケモンしょうぶの　とき\nポケモンの　リストの　ひだりに　いる{FA}ポケモンが　とびだして　たたかうの{FB}だから　つれあるく　ポケモンが　ふえてきたら\nポケモンの　じゅんばんを　かえると{FA}しょうぶが　ゆうりに　なるかも！ | 当宝可梦对战开始时，\n列表左边的那只会先出战。{FB}所以当你有好几只宝可梦时，\n调整好你的宝可梦的排列顺序。{FB}这样你的对战就可能占优势。 | ok | script msgbox words; CN faithful |
| 1 | 0x081F294C | 0x081F295C | OldaleTown_House2_Text_PokemonLevelUp | ポケモンって　たたかうと\nレベルアップして　つよくなるのよ！ | 宝可梦战斗时，\n会获得经验升级变强。 | ok | script msgbox words; CN faithful |
| 2 | 0x081F2955 | 0x081F297B | OldaleTown_House2_Text_YoullGoFurtherWithStrongPokemon | つれて　あるく　ポケモンが　つよかったら\nとおくまで　いけるように　なるね！ | 如果你的宝可梦变强了，\n你就可能走得更远。 | ok | script msgbox words; CN faithful |
| 3 | 0x081F2B6D | 0x081F2B9E | OldaleTown_Mart_Text_ImGoingToBuyPokeBalls | どんどん　モンスターボール　かって\nどんどん　ポケモン　つかまえちゃうわよ！ | 我要买一大堆精灵球，\n然后捕捉一大堆宝可梦！ | ok | script msgbox words; CN faithful |
| 4 | 0x081F2B63 | 0x081F2B7E | OldaleTown_Mart_Text_PokeBallsAreSoldOut | なんでも　うりきれ　らしくて\nモンスターボール　かえないの⋯⋯ | 店员说精灵球\n已经卖光了。 | ok | script msgbox words; CN faithful |
| 5 | 0x081F2B77 | 0x081F2BC5 | OldaleTown_Mart_Text_RestoreHPWithPotion | ポケモンは　たいりょくが　なくなると\nたたかう　げんきも　なくなる{FB}そんな　ときは　キズぐすりを　つかって\nたいりょくを　かいふく　してあげるんだ！ | 如果宝可梦受伤过重昏厥，\n就不能再战斗了。{FB}要想避免宝可梦昏厥，\n就要用伤药恢复它的体力。 | ok | script msgbox words; CN faithful |
| 6 | 0x081F29CF | 0x081F2A31 | OldaleTown_PokemonCenter_1F_Text_PokemonCentersAreGreat | ポケモンセンターって　すごいよな！{FB}ポケモン　なんびき　あずけても\nおかねが　かからないから{FA}どんな　ときでも　あんしん　だよね！ | 宝可梦中心真棒！{FB}你可以随时使用他们\n提供的服务，而且完全免费，{FA}什么也不用担心！ | ok | script msgbox words; CN faithful |
| 7 | 0x081F29ED | 0x081F2AA9 | OldaleTown_PokemonCenter_1F_Text_TradedInWirelessClub | 2かいの　ポケモン　ワイヤレス　クラブは\nつい　さいきん　できたの{FB}あたし　さっそく\nポケモンこうかん　しちゃった！ | 二楼的宝可梦无线俱乐部\n最近刚刚建好，{FB}我马上就去交换了宝可梦。 | ok | script msgbox words; CN faithful |
| 8 | 0x081F29C6 | 0x081F29F5 | OldaleTown_PokemonCenter_1F_Text_TrainersCanUsePC | すみっこに　おいてある　パソコンは\nポケモントレーナーの　ための　ものなんだ{FB}きみも　じゆうに　つかって　いいんだよ！ | 那边角落里的电脑是提供给所有\n宝可梦训练家使用的。{FB}当然，\n你也可以随意使用。 | ok | script msgbox words; CN faithful |
| 9 | 0x081F29E3 | 0x081F2A73 | OldaleTown_PokemonCenter_1F_Text_WirelessClubNotAvailable | 2かいの　ポケモン　ワイヤレス　クラブは\nつい　さいきん　できたの{FB}でも　まだ\nちょうせいちゅう　ですって | 二楼的宝可梦无线俱乐部\n最近刚刚建好，{FB}但据说现在\n还在调整中。 | ok | script msgbox words; CN faithful |
