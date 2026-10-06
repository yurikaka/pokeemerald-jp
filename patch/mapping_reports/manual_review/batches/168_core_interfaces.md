# Manual review: 168_core_interfaces.json

verdicts: {'ok': 32}

| # | address | original | symbol | JP | CN | verdict | notes |
|---|---|---|---|---|---|---|---|
| 0 | 0x08198D40 | 0x085D7B40 | gText_YesNo | はい\nいいえ | 是\n否 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 1 | 0x08134E74 | 0x08591C04 | gText_IsThisTheCorrectTime | この　じかんで　よろしいですか？ | 这是正确的时间吗？ | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 2 | 0x08134B88 | 0x08591C15 | gText_Confirm3 | けってい | 确定 | ok | FIXED: wokann symbol names swapped; content-corrected けってい->确定 |
| 3 | 0x08134CE4 | 0x08591C1A | gText_Cancel4 | もどる　 | 返回 | ok | FIXED: wokann symbol names swapped; content-corrected もどる->返回 |
| 4 | 0x0813420C | 0x085C9363 | gText_BirchInTrouble | オダマキはかせが　ピンチだ！\nポケモンを　だして　たすけてあげよう！ | 小田卷博士遇到麻烦了！\n请拿出宝可梦去救助他吧！ | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 5 | 0x081343AC | 0x085C9386 | gText_ConfirmStarterChoice | このポケモンにしますか？ | 确定选择这只宝可梦？ | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 6 | 0x0809F9BC | 0x08276F58 | gText_ConfirmSave | ここまでの　かつやくを\nポケモンレポートに　かきこみますか？ | 要保存目前为止的\n冒险记录吗？ | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 7 | 0x0809FA84 | 0x08276F77 | gText_AlreadySavedFile | まえに　かかれた　レポートに\nうえから　かいても　いいですか？ | 需要覆盖写入上次的\n保存记录，可以吗？ | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 8 | 0x0809FB1C | 0x08276F97 | gText_SavingDontTurnOff | ポケモンレポートに　かきこんでいます\nでんげんを　きらないで　ください | 正在写入记录⋯⋯\n请勿切断电源。 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 9 | 0x0809FB64 | 0x08276FBB | gText_PlayerSavedGame | {PLAYER}　は\nレポートに　しっかり　かきのこした！ | {PLAYER}\n完好地写下了记录！ | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 10 | 0x0809FA6C | 0x08276FD3 | gText_DifferentSaveFile | ちゅうい！！{FB}“つづきから　はじめる”で\nぼうけん　していた　レポートが{FA}かかれています！{FB}そちらで　プレイしていた　ぼうけんや\nすべての　ポケモン　どうぐ　などが{FA}きえてしまいます⋯⋯{FB}ほんとうに\nうえから　かいても　いいですか？ | 注意！！{FB}在“从记录继续”的选项里\n已经有了一个先前保存的{FA}冒险进度了！{FB}这样做的话，先前的冒险进度\n及所有已得到的宝可梦和道具{FA}全部都会消失⋯⋯{FB}确定要将原来的记录\n从头覆盖掉吗？ | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 11 | 0x0809FB80 | 0x08277048 | gText_SaveError | レポートが　かけませんでした{FB}バックアップカートリッジを\nこうかんしてください！ | 无法写入记录！{FB}请更换卡带的存档用\n记忆电池或电子基板！ | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 12 | 0x08023FB0 | 0x08277071 | gText_SavingDontTurnOffPower | ポケモンレポートに　かきこんでいます\nでんげんを　きらないで　ください | 正在写入记录⋯⋯\n请勿切断电源。 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 13 | 0x0802A0C8 | 0x08277071 | gText_SavingDontTurnOffPower | ポケモンレポートに　かきこんでいます\nでんげんを　きらないで　ください | 正在写入记录⋯⋯\n请勿切断电源。 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 14 | 0x0802D240 | 0x08277071 | gText_SavingDontTurnOffPower | ポケモンレポートに　かきこんでいます\nでんげんを　きらないで　ください | 正在写入记录⋯⋯\n请勿切断电源。 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 15 | 0x0807E7F4 | 0x08277071 | gText_SavingDontTurnOffPower | ポケモンレポートに　かきこんでいます\nでんげんを　きらないで　ください | 正在写入记录⋯⋯\n请勿切断电源。 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 16 | 0x0807EF80 | 0x08277071 | gText_SavingDontTurnOffPower | ポケモンレポートに　かきこんでいます\nでんげんを　きらないで　ください | 正在写入记录⋯⋯\n请勿切断电源。 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 17 | 0x0809FEEC | 0x08277071 | gText_SavingDontTurnOffPower | ポケモンレポートに　かきこんでいます\nでんげんを　きらないで　ください | 正在写入记录⋯⋯\n请勿切断电源。 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 18 | 0x0817379C | 0x08277071 | gText_SavingDontTurnOffPower | ポケモンレポートに　かきこんでいます\nでんげんを　きらないで　ください | 正在写入记录⋯⋯\n请勿切断电源。 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 19 | 0x0805BCC4 | 0x085ABB43 | gText_WhatWillPkmnDo | {FD12}は　どうする？ | {FD12}\n要做什么呢？ | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 20 | 0x0816A2D8 | 0x085ABB57 | gText_WhatWillWallyDo | ミツルは　どうする？ | 满充\n要做什么呢？ | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 21 | 0x0805BCBC | 0x085ABB72 | gText_BattleMenu | たたかう　　バッグ\nポケモン　　にげる | 战斗{FC1330}包包\n宝可梦{FC1330}逃走 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 22 | 0x0816A2D0 | 0x085ABB72 | gText_BattleMenu | たたかう　　バッグ\nポケモン　　にげる | 战斗{FC1330}包包\n宝可梦{FC1330}逃走 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 23 | 0x08059768 | 0x085ABBA1 | gText_MoveInterfaceType | わざタイプ/ | 属性/ | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 24 | 0x08039184 | 0x085ABBC9 | gText_BattleYesNoChoice | {FC0505FC}えすせそはい\nいいえ | {FC0505FC}福镶是\n否 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 25 | 0x0804DCE0 | 0x085ABBC9 | gText_BattleYesNoChoice | {FC0505FC}えすせそはい\nいいえ | {FC0505FC}福镶是\n否 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 26 | 0x0804E038 | 0x085ABBC9 | gText_BattleYesNoChoice | {FC0505FC}えすせそはい\nいいえ | {FC0505FC}福镶是\n否 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 27 | 0x0804E818 | 0x085ABBC9 | gText_BattleYesNoChoice | {FC0505FC}えすせそはい\nいいえ | {FC0505FC}福镶是\n否 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 28 | 0x08056868 | 0x085ABBC9 | gText_BattleYesNoChoice | {FC0505FC}えすせそはい\nいいえ | {FC0505FC}福镶是\n否 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 29 | 0x0805BD14 | 0x085ABBC9 | gText_BattleYesNoChoice | {FC0505FC}えすせそはい\nいいえ | {FC0505FC}福镶是\n否 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 30 | 0x0813EEF4 | 0x085ABBC9 | gText_BattleYesNoChoice | {FC0505FC}えすせそはい\nいいえ | {FC0505FC}福镶是\n否 | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
| 31 | 0x08057BBC | 0x085ABBD8 | gText_BattleSwitchWhich | {FC0505FC}えすせそいれかえる　わざを\nえらんで　ください | {FC0505FC}福镶与哪个招式\n交换位置? | ok | PTR-OK; [24-31] 福镶 are blank spacing glyphs by design |
