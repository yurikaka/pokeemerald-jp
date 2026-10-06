# Manual review: 035_rustborocity_flat2_2f.json

verdicts: {'ok': 3}

| # | address | original | symbol | JP | CN | verdict | notes |
|---|---|---|---|---|---|---|---|
| 0 | 0x08203FEB | 0x0820402B | RustboroCity_Flat2_2F_Text_DevonWasTinyInOldDays | デボンもな　むかしは\nちいさな　ちいさな　かいしゃ　だったわい | 许多年以前，得文只是个\n微不足道的小公司。 | ok | script msgbox words; CN faithful |
| 1 | 0x08204023 | 0x08204087 | RustboroCity_Flat2_2F_Text_GoingToWorkAtDevonToo | おとうさんは　かいしゃで　おしごと！{FB}ぼくも　おおきく　なったら\nデボンで　はたらくんだ！ | 我爸爸在公司里工作。{FB}我长大后，\n也要去得文工作。 | ok | script msgbox words; CN faithful |
| 2 | 0x08203FFF | 0x0820404B | RustboroCity_Flat2_2F_Text_MyDaddyMadeThisYouCanHaveIt | おとうさんは　かいしゃで　おしごと！{FB}これ　おとうさんが　つくったんだぜ！\nでも　ぼく　まだ　つかえないから　あげるよ | 我爸爸在公司里工作。{FB}他做了这个东西！\n但我不会用，给你吧。 | ok | script msgbox words; CN faithful |
