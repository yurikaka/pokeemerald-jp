# Manual review: 002_inside_truck.json

verdicts: {'ok': 1}

| # | address | original | symbol | JP | CN | verdict | notes |
|---|---|---|---|---|---|---|---|
| 0 | 0x0821DE17 | 0x0821DE1E | InsideOfTruck_Text_BoxPrintedWithMonLogo | はこには　ポケモンの　えが　かいてある{FB}ポケモンマークの　ひっこしやさん　だ！ | 盒子上印着宝可梦的商标。{FB}这是宝可梦牌\n搬家服务。 | ok | script msgbox word (0F00 ptr 09); CN matches US汉化 (logo=商标) |
