# Manual review: 169_battle_messages.json

verdicts: {'ok': 23, 'ok-intentional': 1}

| # | address | original | symbol | JP | CN | verdict | notes |
|---|---|---|---|---|---|---|---|
| 0 | 0x0814E2B4 | 0x085AAE91 | sText_TwoLinkTrainersWantToBattle | {FD20}と　{FD21}が\nしょうぶを　しかけてきた！ | {FD20}和{FD21}\n前来挑战了！ | ok | PTR-OK, CN faithful |
| 1 | 0x0814E2B8 | 0x085AC12D | sText_TwoLinkTrainersWantToBattlePause | {FD20}と　{FD21}が\nしょうぶを　しかけてきた！{FC0831} | {FD20}和{FD21}\n前来挑战了！{FC0831} | ok | PTR-OK, CN faithful |
| 2 | 0x0814E2D0 | 0x085AAE68 | sText_Trainer1WantsToBattle | {FD1C}の　{FD1D}が\nしょうぶを　しかけてきた！{FB} | {FD1C}{FD1D}\n前来挑战了！{FB} | ok | PTR-OK, CN faithful |
| 3 | 0x0814E30C | 0x085AAE68 | sText_Trainer1WantsToBattle | {FD1C}の　{FD1D}が\nしょうぶを　しかけてきた！{FB} | {FD1C}{FD1D}\n前来挑战了！{FB} | ok | PTR-OK, CN faithful |
| 4 | 0x0814E2E8 | 0x085AAE7F | sText_LinkTrainerWantsToBattle | {FD20}が\nしょうぶを　しかけてきた！ | {FD20}\n前来挑战了！ | ok | PTR-OK, CN faithful |
| 5 | 0x0814E2EC | 0x085AC118 | sText_LinkTrainerWantsToBattlePause | {FD20}が\nしょうぶを　しかけてきた！{FC0831} | {FD20}\n前来挑战了！{FC0831} | ok | PTR-OK, CN faithful |
| 6 | 0x0814E324 | 0x085AAE22 | sText_LegendaryPkmnAppeared | あ！　やせいの\n{RIVAL}が　あらわれた！{FB} | {RIVAL}出现了！{FB} | ok-intentional | matches us_chs which drops 野生的 |
| 7 | 0x0814E334 | 0x085AAE4E | sText_TwoWildPkmnAppeared | あ！　やせいの\n{RIVAL}と　{EVIL_TEAM}が　とびだしてきた！{FB} | 啊！野生的\n{RIVAL}和{EVIL_TEAM}扑过来了！{FB} | ok | PTR-OK, CN faithful |
| 8 | 0x0814E34C | 0x085AAE0C | sText_WildPkmnAppeared | あ！　やせいの\n{RIVAL}が　とびだしてきた！{FB} | 啊！野生的\n{RIVAL}扑过来了！{FB} | ok | PTR-OK, CN faithful |
| 9 | 0x0814E350 | 0x085AAE36 | sText_WildPkmnAppearedPause | あ！　やせいの\n{RIVAL}が　とびだしてきた！{FC087F} | 啊！野生的\n{RIVAL}扑过来了！{FC087F} | ok | PTR-OK, CN faithful |
| 10 | 0x0814E394 | 0x085AAF4B | sText_GoTwoPkmn | ゆけっ！　{KUN}と　{VERSION}！ | 上吧！{KUN}！\n{VERSION}！ | ok | PTR-OK, CN faithful |
| 11 | 0x0814E3A8 | 0x085AAF4B | sText_GoTwoPkmn | ゆけっ！　{KUN}と　{VERSION}！ | 上吧！{KUN}！\n{VERSION}！ | ok | PTR-OK, CN faithful |
| 12 | 0x0814E3B4 | 0x085AAF42 | sText_GoPkmn | ゆけっ！　{KUN}！ | 上吧！{KUN}！ | ok | PTR-OK, CN faithful |
| 13 | 0x0814E3F0 | 0x085AAF06 | sText_TwoLinkTrainersSentOutPkmn | {FD20}は　{EVIL_LEADER}を　くりだした！\n{FD21}は　{EVIL_LEGENDARY}を　くりだした！ | {FD20}派出了{EVIL_LEADER}！\n{FD21}派出了{EVIL_LEGENDARY}！ | ok | PTR-OK, CN faithful |
| 14 | 0x0814E408 | 0x085AAEBA | sText_Trainer1SentOutTwoPkmn | {FD1C}の　{FD1D}は\n{RIVAL}と　{EVIL_TEAM}を　くりだした！ | {FD1C}{FD1D}\n派出了{RIVAL}和{EVIL_TEAM}！ | ok | PTR-OK, CN faithful |
| 15 | 0x0814E40C | 0x085AAEF3 | sText_LinkTrainerSentOutTwoPkmn | {FD20}は\n{RIVAL}と　{EVIL_TEAM}を　くりだした！ | {FD20}派出了\n{RIVAL}和{EVIL_TEAM}！ | ok | PTR-OK, CN faithful |
| 16 | 0x0814E434 | 0x085AAEE4 | sText_LinkTrainerSentOutPkmn | {FD20}は\n{RIVAL}を　くりだした！ | {FD20}派出了\n{RIVAL}！ | ok | PTR-OK, CN faithful |
| 17 | 0x0814E438 | 0x085AAEA7 | sText_Trainer1SentOutPkmn | {FD1C}の　{FD1D}は\n{RIVAL}を　くりだした！ | {FD1C}{FD1D}\n派出了{RIVAL}！ | ok | PTR-OK, CN faithful |
| 18 | 0x0814E50C | 0x085AAF58 | sText_GoPkmn2 | ゆけっ！　{FD00}！ | 上吧！{FD00}！ | ok | PTR-OK, CN faithful |
| 19 | 0x0814E560 | 0x085AAF33 | sText_LinkTrainerMultiSentOutPkmn | {FD22}は\n{FD00}を　くりだした！ | {FD22}派出了\n{FD00}！ | ok | PTR-OK, CN faithful |
| 20 | 0x0814E57C | 0x085AAF24 | sText_LinkTrainerSentOutPkmn2 | {FD20}は\n{FD00}を　くりだした！ | {FD20}派出了\n{FD00}！ | ok | PTR-OK, CN faithful |
| 21 | 0x0814E580 | 0x085AAED1 | sText_Trainer1SentOutPkmn2 | {FD1C}の　{FD1D}は\n{FD00}を　くりだした！ | {FD1C}{FD1D}\n派出了{FD00}！ | ok | PTR-OK, CN faithful |
| 22 | 0x0814E5FC | 0x085AB034 | sText_AttackerUsedX | {FD0F}{FD00}\n{PLAYER} | {FD0F}使出了\n{PLAYER}！ | ok | PTR-OK, CN faithful |
| 23 | 0x085AB73C | 0x085AAA9F | sText_ButNothingHappened | しかし　なにもおこらない | 但是，什么也没有发生！ | ok | PTR-OK, CN faithful |
