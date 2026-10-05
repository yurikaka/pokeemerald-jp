# v3 独立复核（2026-10-04）

## 基准与范围

- 日版 HEAD：`5604922996cc2a53ec7d7dc99253de5e3fb5e950`；美版 HEAD：`1cbb305f7ebd2038f0d0ebcba039b20fe18f21e3`。
- 基于原始报告、当前实际定义、baserom_jp.gba 原地址与 Wokann dev 原文，以及美版 Git `fe570a7e5^` 英文原文。未读取旧 review 的语义判定。
- 本轮只写审查报告，不改游戏文本、代码、ROM，不 commit/push；未做模拟器验证。
- v2范围为115 ERROR + 121 NEEDS_ATTENTION，共236条；并非重新语义审计全部14780条。
- v3范围为原建议报告65项、64个唯一资源；缺少报告提到的 audit_v3_us_only.csv，无法核查声称的484个待移植项。
- JSON保存完整原报告、当前定义、日英原文与地址证据。换行/分页/FD/F7控制符不能按两版字符串表面差异机械同步。
- 长文本的最终换行和显示宽度必须在实施时验证；本文给出的修改方向不是未经编译验证即可写入的字节串。

## 分类数量

- 有意保留：1条。
- 报告错误：2条。
- 需修复：35条。
- 已修复：25条。
- 重复：1条。
- 可选，不列必修：1条。

## 需修复索引

- 3 `AbandonedShip_Corridors_B1F_Text_DuncanPostBattle`：JP+US；船底沉入水中，不是船搁浅。
- 4 `AquaHideout_B1F_Text_Grunt3Intro`：JP+US；おやつ / snacks 是零食；还遗漏打倒捣乱者的动作。
- 6 `BattleFrontier_BattlePikeRoomNormal_Text_AttacksWhenStartled`：JP+US；受惊后突然袭击，不是违抗命令。
- 7 `LilycoveCity_ContestLobby_Text_ContestFeastForEyes`：JP+US；值得画成画的宝可梦，不是已经在画里的宝可梦。
- 8 `MauvilleCity_Text_UncleNoNeedToBeDown`：JP+US；日文是鼓励以后变强；英文反问有什么阻止变强。不是追问增强的动机。
- 9 `MossdeepCity_GameCorner_1F_Text_TalkToOldManToPlay`：JP+US；beside / おとなり 是旁边，不是后面。
- 11 `MossdeepCity_SpaceCenter_1F_Text_HaywireButRocketLaunchImminent`：JP+US；imminent / もうすぐ 是即将发射，不是不停止程序。
- 12 `MoveTutor_Text_SubstituteTeach`：JP+US；突然想到一个主意，不是理解了。
- 13 `Route116_Text_JoeyIntro`：JP+US；rule / つえー 是厉害，不是运用。
- 14 `Route123_Text_BraxtonPostBattle`：JP+US；战斗不辱徽章，而非在此次战斗中获得徽章。
- 15 `SecretBase_Text_Trainer1PreChampion`：JP+US；已经终于获得使用机会，不是仍等着开放。
- 16 `BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteMMon1`：JP+US；decent 是不错；日文说自己培育的。高贵/一对不合适。
- 17 `BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteMMon2Ask`：JP+US；neat 在此是组队不错，不是高雅。
- 18 `BattleFrontier_Lounge5_Text_LadyClaimsSheUnderstandsPokemon`：JP+US；charming / シャレた 是有趣俏皮，不是魔法。
- 19 `BattleFrontier_OutsideEast_Text_ThriveInDarkness`：JP+US；开头已修，邀请探索的结尾仍误译；日英区域差异应保留。
- 20 `DewfordTown_Gym_Text_BrendenIntro`：JP+US；いじ / gumption 是骨气胆识，不是智慧。
- 22 `FortreeCity_House1_Text_GoingToMakeVolbeatStrong`：JP+US；要求同样把正电拍拍培养强大，不是泛泛善待。
- 31 `LilycoveCity_PokemonTrainerFanClub_Text_YoureOneWeWantToWin`：JP+US；为玩家加油，不是想打败玩家，主客体反转。
- 32 `GraniteCave_StevensRoom_Text_ImStevenLetterForMe`：JP+US；所有经常是笔误。
- 36 `gTVPokemonNewsBattleFrontierText11`：JP+US；两个“在”重复，当前仍存在。
- 37 `gTVPokemonNewsBattleFrontierText12`：JP+US；两个“在”重复，当前仍存在。
- 40 `CableClub_Text_ExplainWirelessClub`：JP+US；非首次说明的完整日英原文均有找不到朋友时靠近的提示，当前遗漏。
- 42 `LavaridgeTown_Gym_1F_Text_GeraldIntro`：JP；US澄清单位；日文200度与英文392度是摄氏/华氏区域换算，不是同一数字。“392度”没有单位会误导。
- 43 `LavaridgeTown_Gym_1F_Text_GeraldPostBattle`：JP；US澄清单位；同上一条，原作设定数值是200℃ / 392℉。
- 44 `gText_BecameMoreConsciousOfOtherMons`：JP+US；conscious / きになる 是更加在意，不是担心。
- 46 `[127]`：JP+US；第三世代攀瀑是 EFFECT_HIT，secondaryEffectChance=0，没有招式自带畏缩效果。不能混入第四世代效果。
- 52 `BattleFrontier_Lounge2_Text_AmazingPowersOfObservation`：JP+US；かんさつりょく / powers of observation 是观察力。センパイ是前辈，不应机械修成老师。
- 54 `LilycoveCity_ContestHall_Text_SuchCharmingCuteAppeals`：JP+US；みずあそび / WATER SPORT 是招式玩水；“水之游”不是该招式名。
- 55 `LilycoveCity_CoveLilyMotel_1F_Text_HeardAquaHideoutBusted`：JP+US；有人到捣毁了，混入多余“到”。
- 57 `MossdeepCity_GameCorner_1F_Text_DescribeWhichGame`：JP+US；游戏规则不是宝可梦对战规则。
- 58 `gText_NoticesGoldCard`：JP+US；当前已恢复金卡/金色/四星，但未恢复金卡持有者的限定和两次玩家名。
- 59 `RustboroCity_DevonCorp_1F_Text_HowCouldWeGetRobbed`：JP+US；对已经被抢的事情自责，不能否认“谁会抢”。
- 60 `RustboroCity_PokemonSchool_Text_ExplainPoison`：JP+US；体力P是残留字母，不成词；这里应表示HP。
- 61 `gTVBravoTrainerText00`：JP+US；STR_VAR_1 是训练家，节目介绍的是其宝可梦；Rank 是比赛级别，非取得优胜。保留节目名原英文不必单独认定错误。
- 63 `sText_MysteryGiftVisitingTrainerArrived`：JP；美版已改希望，日版仍是系统。报告“日版无对应”不成立，ROM有0x085FCE8B。

## 逐条复核

### 1 — gText_XNatureObtainedInTrade

结论：**有意保留**。

训练家笔记取消换行是既定布局需求，f6e6cb9 可追溯；不能仅凭原作有换行恢复。

方案：不修改。

原建议：

- 补丁中文：{DYNAMIC_0}{DYNAMIC_2}{DYNAMIC_1}{DYNAMIC_5}的性格，通过交换遇见了它。$
- 理由：JP原0x085CA4F2: {D0}{D2}{D1}{D5}せいかく、\nつうしんこうかんによってであった（有换行）；P无换行 / U有换行。补丁丢了日文原有的换行。
- 修改建议：{DYNAMIC_0}{DYNAMIC_2}{DYNAMIC_1}{DYNAMIC_5}的性格，\n通过交换遇见了它。

当前日版：

`{DYNAMIC 0}{DYNAMIC 2}{DYNAMIC 1}{DYNAMIC 5}的性格，通过交换遇见了它。`

文件：`patch/batches/172_party.json`。

原日文（`0x085CA4F2`）：

`{BYTE_F7}　{BYTE_F7}い{BYTE_F7}あ{BYTE_F7}おせいかく\nつうしんこうかんに　よって　であった`

原英文（`src/strings.c`，`fe570a7e5^`）：

`{DYNAMIC 0}{DYNAMIC 2}{DYNAMIC 1}{DYNAMIC 5} nature,\nobtained in a trade.`

当前美版（`src/strings.c`）：

`{DYNAMIC 0}{DYNAMIC 2}{DYNAMIC 1}{DYNAMIC 5}的性格，\n通过交换遇见了它。`

### 2 — sText_PlayerGotMoney

结论：**报告错误**。

当前结尾明确有 \p，报告展示文本自身也含它。円后置有意。

方案：不修改。

原建议：

- 补丁中文：作为奖金，\n{FD_23}获得了{B_BUFF1}{FC_JPN}¥{FC_ENG}！\p$
- 理由：补丁丢了\p换页符。P: {FD_23}获得了{B_BUFF1}{FC_JPN}¥{FC_ENG}！\p$ / U: {B_PLAYER_NAME}获得了¥{B_BUFF1}！\p$。¥后置不判错，但\p缺失需补回。
- 修改建议：补回末尾的\p。

## 二、美版汉化继承的错误

### 语义误译（13 条）

当前日版：

`作为奖金，\n{FD_23}获得了{FD_00}{JPN}¥{ENG}！\p`

文件：`patch/batches/178_battle_victory.json`。

原日文（`0x085A97B2`）：

`{PLACEHOLDER_23}は　しょうきんとして\n{PLACEHOLDER_00}¥　てにいれた!\p`

Wokann日文（`src/battle_message.c`）：

`{B_PLAYER_NAME}は　しょうきんとして\n{B_BUFF1}¥　てにいれた！\p`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_PLAYER_NAME} got ¥{B_BUFF1}\nfor winning!\p`

当前美版（`src/battle_message.c`）：

`作为奖金，\n{B_PLAYER_NAME}获得了¥{B_BUFF1}！\p`

### 3 — AbandonedShip_Corridors_B1F_Text_DuncanPostBattle

结论：**需修复**。

船底沉入水中，不是船搁浅。

方案：船底已经沉到水里了。\p如果有会潜水的宝可梦，\n也许就能继续前进了……

原建议：

- JP：ふなぞこが　みずの　なかに
しずんで　いるんだよ\pポケモンが　みずに　もぐれる　わざを
つかえたら　さきに　すすめるんだがな……
- EN：The ship's bottom has sunk into the\ndepths.\pIf a POKéMON knew how to go underwater,\nwe might make some progress…$
- 中文：我们的船现在搁浅了。\p如果有会潜水的宝可梦的话，\n或许能帮上什么忙……$
- 理由：JP「ふなぞこが みずの なかに しずんでいる」(船底沉入水中)/EN「The ship's bottom has sunk into the depths」均指沉没，而CHS写成「我们的船现在搁浅了」——「搁浅」意为船只在浅滩受阻，与「沉入水中」语义矛盾。
- 修改建议：我们的船的船底现在沉到水里了。

当前日版：

`我们的船现在搁浅了。\p如果有会潜水的宝可梦的话，\n或许能帮上什么忙……`

文件：`patch/batches/197_abandoned_ship.json`。

原日文（`0x0821ACD0`）：

`ふなぞこが　みずの　なかに\nしずんで　いるんだよ\pポケモンが　みずに　もぐれる　わざを\nつかえたら　さきに　すすめるんだがな……`

Wokann日文（`data/maps/AbandonedShip_Corridors_B1F/scripts.inc`）：

`ふなぞこが　みずの　なかに\nしずんで　いるんだよ\pポケモンが　みずに　もぐれる　わざを\nつかえたら　さきに　すすめるんだがな⋯⋯$`

原英文（`data/maps/AbandonedShip_Corridors_B1F/scripts.inc`，`fe570a7e5^`）：

`The ship's bottom has sunk into the\ndepths.\pIf a POKéMON knew how to go underwater,\nwe might make some progress…$`

当前美版（`data/maps/AbandonedShip_Corridors_B1F/scripts.inc`）：

`我们的船现在搁浅了。\p如果有会潜水的宝可梦的话，\n或许能帮上什么忙……$`

### 4 — AquaHideout_B1F_Text_Grunt3Intro

结论：**需修复**。

おやつ / snacks 是零食；还遗漏打倒捣乱者的动作。

方案：燃料补给完毕！\n零食补给完毕！\p接下来只要打倒\n捣乱的家伙就行了！

原建议：

- JP：ねんりょうの　ほきゅう　オッケイ!
おやつも　ほきゅう　オッケイ!\pあとは　ジャマものを　ぶっとばす　だけ!
- EN：Fuel supply loaded A-OK!\nIn-cruise snacks loaded A-OK!\pNothing left to do but KO a pesky\nmeddler!$
- 中文：燃料供给完成！\n巡航系统正常！\p一切正常，除了一个\n找麻烦的人！$
- 理由：JP「おやつも ほきゅう オッケイ」/EN「In-cruise snacks loaded A-OK」中「おやつ」是零食，CHS误作「巡航系统正常」；且JP「あとは ジャマものを ぶっとばす だけ」(剩下就是干掉捣乱者)/EN「Nothing left to do but KO a pesky meddler」被CHS写成「一切正常，除了一个找麻烦的人」，丢失了「打飞捣乱者」的动作含义。
- 修改建议：燃料补给完毕！\n零食补给完毕！\p接下来只要干掉\n捣乱的家伙就行了！

当前日版：

`燃料供给完成！\n巡航系统正常！\p一切正常，除了一个\n找麻烦的人！`

文件：`patch/batches/141_aquahideout_b1f.json`。

原日文（`0x08217E76`）：

`ねんりょうの　ほきゅう　オッケイ!\nおやつも　ほきゅう　オッケイ!\pあとは　ジャマものを　ぶっとばす　だけ!`

Wokann日文（`data/maps/AquaHideout_B1F/scripts.inc`）：

`ねんりょうの　ほきゅう　オッケイ！\nおやつも　ほきゅう　オッケイ！\pあとは　ジャマものを　ぶっとばす　だけ！$`

原英文（`data/maps/AquaHideout_B1F/scripts.inc`，`fe570a7e5^`）：

`Fuel supply loaded A-OK!\nIn-cruise snacks loaded A-OK!\pNothing left to do but KO a pesky\nmeddler!$`

当前美版（`data/maps/AquaHideout_B1F/scripts.inc`）：

`燃料供给完成！\n巡航系统正常！\p一切正常，除了一个\n找麻烦的人！$`

### 5 — BattleFrontier_BattleDomeBattleRoom_Text_WillTheyRaceToChampionship

结论：**已修复**。

已改为该训练家能否一举夺冠。

方案：不修改。

原建议：

- JP：いっきに　ゆうしょうまで\nのぼりつめて　しまうのでしょうか！？\p$
- EN：Will this TRAINER race to\nthe championship?\p$
- 中文：哪一位训练家进入\n冠军赛了呢？\p$
- 理由：JP「いっきに ゆうしょうまで のぼりつめて しまうのでしょうか」/EN「Will this TRAINER race to the championship?」问的是「这位训练家能否一举登顶」，CHS作「哪一位训练家进入冠军赛了呢」——将「这位(this)」误作「哪一位(which)」，疑问对象完全改变。
- 修改建议：这位训练家会一举登上冠军宝座吗？

当前日版：

`这位训练家能否\n一举夺冠呢？\p`

文件：`patch/batches/200_battle_frontier_battle_dome_battle_room.json`。

原日文（`0x082296B5`）：

`いっきに　ゆうしょうまで\nのぼりつめて　しまうのでしょうか!?\p`

Wokann日文（`data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc`）：

`いっきに　ゆうしょうまで\nのぼりつめて　しまうのでしょうか！？\p$`

原英文（`data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc`，`fe570a7e5^`）：

`Will this TRAINER race to\nthe championship?\p$`

当前美版（`data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc`）：

`这位训练家能否\n一举夺冠呢？\p$`

### 6 — BattleFrontier_BattlePikeRoomNormal_Text_AttacksWhenStartled

结论：**需修复**。

受惊后突然袭击，不是违抗命令。

方案：突然看见人时会受惊，\n然后扑过来攻击……\p您和您的宝可梦还好吗？

原建议：

- JP：きゅうに　ひとを　みると　おどろいて\nおそいかかって　しまうのだ⋯⋯\pきみも　ポケモンも　だいじょうぶか？$
- EN：It attacks without warning if it is\nstartled by another person…\pAre you and your POKéMON all right?$
- 中文：一旦受到了惊吓就会\n无视警告胡乱攻击……\p您和您的宝可梦还好吗？$
- 理由：JP「きゅうに ひとを みると おどろいて おそいかかって しまう」/EN「It attacks without warning if it is startled by another person」中「without warning」指「毫无征兆地」，CHS作「无视警告胡乱攻击」——将「without warning」误读为「无视警告」，且「おそいかかる(猛扑)」被写成「胡乱攻击」，语义错误。
- 修改建议：它一旦突然看到人受了惊吓，就会猛扑过来攻击……

当前日版：

`一旦受到了惊吓就会\n不听指挥胡乱攻击……\p您和您的宝可梦还好吗？`

文件：`patch/batches/212_battle_frontier_battle_pike_room_normal.json`。

原日文（`0x08234E0C`）：

`きゅうに　ひとを　みると　おどろいて\nおそいかかって　しまうのだ……\pきみも　ポケモンも　だいじょうぶか?`

Wokann日文（`data/maps/BattleFrontier_BattlePikeRoomNormal/scripts.inc`）：

`きゅうに　ひとを　みると　おどろいて\nおそいかかって　しまうのだ⋯⋯\pきみも　ポケモンも　だいじょうぶか？$`

原英文（`data/maps/BattleFrontier_BattlePikeRoomNormal/scripts.inc`，`fe570a7e5^`）：

`It attacks without warning if it is\nstartled by another person…\pAre you and your POKéMON all right?$`

当前美版（`data/maps/BattleFrontier_BattlePikeRoomNormal/scripts.inc`）：

`一旦受到了惊吓就会\n不听指挥胡乱攻击……\p您和您的宝可梦还好吗？$`

### 7 — LilycoveCity_ContestLobby_Text_ContestFeastForEyes

结论：**需修复**。

值得画成画的宝可梦，不是已经在画里的宝可梦。

方案：日版：来到华丽大赛会场，\n到处都是值得画下来的\l宝可梦呢！；美版保留视觉盛宴开头，后面改“看看这些让人\n忍不住想画下来的宝可梦！”

原建议：

- JP：いやあ　コンテストかいじょうに　くると
かきがいの　ある　ポケモンが\lいっぱい　だね!
- EN：Wow, coming out to a CONTEST is\na feast for these eyes!\pWould you look at all the POKéMON\nthat just scream to be pain
- 中文：哇，观看华丽大赛\n简直是场视觉盛宴！\p你看过那些\n画里的宝可梦吗？$
- 理由：JP「かきがいのあるポケモンがいっぱいだね」/EN“POKéMON that just scream to be painted”意为“值得入画的宝可梦”，中文“你看过那些画里的宝可梦吗？”把“值得被画下来”误作“画里面的宝可梦”，关系颠倒。
- 修改建议：哇，观看华丽大赛\n简直是场视觉盛宴！\p快看那些值得入画的\n宝可梦！

当前日版：

`哇，观看华丽大赛\n简直是场视觉盛宴！\p你看过那些\n画里的宝可梦吗？`

文件：`patch/batches/126_lilycovecity_contestlobby.json`。

原日文（`0x082076BA`）：

`いやあ　コンテストかいじょうに　くると\nかきがいの　ある　ポケモンが\lいっぱい　だね!`

Wokann日文（`data/maps/LilycoveCity_ContestLobby/scripts.inc`）：

`いやあ　コンテストかいじょうに　くると\nかきがいの　ある　ポケモンが\lいっぱい　だね！$`

原英文（`data/maps/LilycoveCity_ContestLobby/scripts.inc`，`fe570a7e5^`）：

`Wow, coming out to a CONTEST is\na feast for these eyes!\pWould you look at all the POKéMON\nthat just scream to be painted?$`

当前美版（`data/maps/LilycoveCity_ContestLobby/scripts.inc`）：

`哇，观看华丽大赛\n简直是场视觉盛宴！\p你看过那些\n画里的宝可梦吗？$`

### 8 — MauvilleCity_Text_UncleNoNeedToBeDown

结论：**需修复**。

日文是鼓励以后变强；英文反问有什么阻止变强。不是追问增强的动机。

方案：中段改为“今后继续努力，\n变得越来越强就好啦！”；其他叔叔对话不变。

原建议：

- JP：おじさん“ミツルくん\nそんなに　しょげることは　ないよ\pこれから　もっともっと\nつよくなれば　いいじゃないか！\pさあ　うちに　かえろう\nみんな　まってるよ$
- EN：UNCLE: WALLY, there's no need to be so\ndown on yourself.\pWhy, what's keeping you from becoming\nstronger and stronger?
- 中文：叔叔：满充，\n别这么沮丧。\p想想是什么激励着你\n要变得越来越强的？\p好了，我们回家吧，\n大家都在等你呢。$
- 理由：JP「これからもっともっとつよくなればいいじゃないか（以后继续变得越来越强不就好了吗）」/EN「what's keeping you from becoming stronger and stronger?（有什么能阻止你继续变强呢）」均为鼓励继续变强，补丁/美版中文误作「想想是什么激励着你要变得越来越强的」，把EN「what's keeping you from（什么在阻碍你）」误读为「激励」，语义错误。
- 修改建议：以后继续变得越来越强不就好了吗！

当前日版：

`叔叔：满充，\n别这么沮丧。\p想想是什么激励着你\n要变得越来越强的？\p好了，我们回家吧，\n大家都在等你呢。`

文件：`patch/batches/050_mauvillecity.json`。

原日文（`0x081DE0F4`）：

`おじさん“ミツルくん\nそんなに　しょげることは　ないよ\pこれから　もっともっと\nつよくなれば　いいじゃないか!\pさあ　うちに　かえろう\nみんな　まってるよ`

Wokann日文（`data/maps/MauvilleCity/scripts.inc`）：

`おじさん“ミツルくん\nそんなに　しょげることは　ないよ\pこれから　もっともっと\nつよくなれば　いいじゃないか！\pさあ　うちに　かえろう\nみんな　まってるよ$`

原英文（`data/maps/MauvilleCity/scripts.inc`，`fe570a7e5^`）：

`UNCLE: WALLY, there's no need to be so\ndown on yourself.\pWhy, what's keeping you from becoming\nstronger and stronger?\pCome on, let's go home.\nEveryone's waiting for you.$`

当前美版（`data/maps/MauvilleCity/scripts.inc`）：

`叔叔：满充，\n别这么沮丧。\p想想是什么激励着你\n要变得越来越强的？\p好了，我们回家吧，\n大家都在等你呢。$`

### 9 — MossdeepCity_GameCorner_1F_Text_TalkToOldManToPlay

结论：**需修复**。

beside / おとなり 是旁边，不是后面。

方案：仅将“我后面的老人”改为“我旁边的老人”。

原建议：

- JP：ゲームを　するなら\nおとなりの　おじいさんに　いってね$
- EN：If you want to play a game,\nplease tell the old man beside me.$
- 中文：如果您想玩游戏，\n就告诉我后面的老人。$
- 理由：JP「おとなりのおじいさん（旁边的老爷爷）」/EN「the old man beside me（我旁边的老人）」明确方位为「旁边」，补丁/美版中文误作「我后面的老人」，方位错误。
- 修改建议：就告诉我旁边的老人。

当前日版：

`如果您想玩游戏，\n就告诉我后面的老人。`

文件：`patch/batches/151_mossdeepcity_gamecorner_1f.json`。

原日文（`0x08248314`）：

`ゲ-ムを　するなら\nおとなりの　おじいさんに　いってね`

Wokann日文（`data/text/cable_club.inc`）：

`ゲームを　するなら\nおとなりの　おじいさんに　いってね$`

原英文（`data/text/cable_club.inc`，`fe570a7e5^`）：

`If you want to play a game,\nplease tell the old man beside me.$`

当前美版（`data/text/cable_club.inc`）：

`如果您想玩游戏，\n就告诉我后面的老人。$`

### 10 — MossdeepCity_Gym_Text_BlakePostBattle

结论：**已修复**。

尘埃和否认吹气的语义已恢复。

方案：不修改。

原建议：

- JP：モンスタ-ボ-ルは　おおきすぎた
この　わたぼこり　なら　ぜったいに……\pふううううううっ……!\p……　……　……
……　……　……\pちがうぞ!
はないきで　とばして　なんか　いないぞ!
- EN：A POKé BALL was too heavy to lift\npsychically. But this dust bunny…\pWhoooooooooooooooh!\n… … … … … …\pNo, I'm not chea
- 中文：要用精神力举起精灵球还是困难\n了点，但这么小的灰尘的话……\p呜啊啊啊啊啊啊啊！\n…… …… ……\p不不，我没骗人！\n我没吹牛！真的！$
- 理由：JP「ちがうぞ！はないきでとばしてなんかいないぞ（不对！我才没有用嘴吹它！）」/EN「I didn't blow on it!（我没对它吹气！）」中「吹」指用嘴吹气，补丁/美版中文误作「我没吹牛」，「吹气」误译为「吹牛（说大话）」，语义错误。
- 修改建议：我没用嘴吹！真的！

当前日版：

`要用精神力举起精灵球还是困难\n了点，但这么小的灰尘的话……\p呜啊啊啊啊啊啊啊！\n…… …… ……\p不不，我没骗人！\n我可没用嘴吹！真的！`

文件：`patch/batches/152_mossdeepcity_gym.json`。

原日文（`0x0820BA3C`）：

`モンスタ-ボ-ルは　おおきすぎた\nこの　わたぼこり　なら　ぜったいに……\pふううううううっ……!\p……　……　……\n……　……　……\pちがうぞ!\nはないきで　とばして　なんか　いないぞ!`

Wokann日文（`data/maps/MossdeepCity_Gym/scripts.inc`）：

`モンスターボールは　おおきすぎた\nこの　わたぼこり　なら　ぜったいに⋯⋯\pふううううううっ⋯⋯！\p⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯\pちがうぞ！\nはないきで　とばして　なんか　いないぞ！$`

原英文（`data/maps/MossdeepCity_Gym/scripts.inc`，`fe570a7e5^`）：

`A POKé BALL was too heavy to lift\npsychically. But this dust bunny…\pWhoooooooooooooooh!\n… … … … … …\pNo, I'm not cheating!\nI didn't blow on it! Honestly!$`

当前美版（`data/maps/MossdeepCity_Gym/scripts.inc`）：

`要用精神力举起精灵球还是困难\n了点，但这么小的灰尘的话……\p呜啊啊啊啊啊啊啊！\n…… …… ……\p不不，我没骗人！\n我可没用嘴吹！真的！$`

### 11 — MossdeepCity_SpaceCenter_1F_Text_HaywireButRocketLaunchImminent

结论：**需修复**。

imminent / もうすぐ 是即将发射，不是不停止程序。

方案：火箭马上就要发射了！

原建议：

- JP：こんな　さわぎの　とちゅう　だけど……\pもうすぐ　ロケットが　はっしゃ　するぞ!
- EN：I know that things are a little\nhaywire right now, but…\pThe rocket's launch is imminent!$
- 中文：我知道现在一切有些混乱，\n但是……\p火箭发射程序不会停止！$
- 理由：JP「もうすぐロケットがはっしゃするぞ（火箭马上就要发射了）」/EN「The rocket's launch is imminent（火箭发射在即）」明确指发射即将发生，补丁/美版中文误作「火箭发射程序不会停止」，「在即」误译为「不会停止」，语义错误。
- 修改建议：火箭马上就要发射了！

当前日版：

`我知道现在一切有些混乱，\n但是……\p火箭发射程序不会停止！`

文件：`patch/batches/157_mossdeepcity_spacecenter_1f.json`。

原日文（`0x0820D0FD`）：

`こんな　さわぎの　とちゅう　だけど……\pもうすぐ　ロケットが　はっしゃ　するぞ!`

Wokann日文（`data/maps/MossdeepCity_SpaceCenter_1F/scripts.inc`）：

`こんな　さわぎの　とちゅう　だけど⋯⋯\pもうすぐ　ロケットが　はっしゃ　するぞ！$`

原英文（`data/maps/MossdeepCity_SpaceCenter_1F/scripts.inc`，`fe570a7e5^`）：

`I know that things are a little\nhaywire right now, but…\pThe rocket's launch is imminent!$`

当前美版（`data/maps/MossdeepCity_SpaceCenter_1F/scripts.inc`）：

`我知道现在一切有些混乱，\n但是……\p火箭发射程序不会停止！$`

### 12 — MoveTutor_Text_SubstituteTeach

结论：**需修复**。

突然想到一个主意，不是理解了。

方案：“明白了！”改“对了！”。

原建议：

- JP：ふう\nこうやって　おくじょうから\lひろい　せかいを　みていると⋯⋯\pなんにんもの　じぶんが　いて\nいくつもの　じんせいを　たのしめたらなー\lって　おもうの！\lムリな　はなしだけどね　うふふ\pそうだわ　あなたの　ポケモンちゃん！
- EN：When I see the wide world from up\nhere on the roof…\pI think about how nice it would be\nif there were more than just o
- 中文：当我在屋顶上看着\n这广阔的世界时……\p我在想如果这个世界如果\n有不止一个自己该多有趣啊，\l那样我就能体验各种各样的人生了。\p当然这是不可能的。\n嘿嘿……\p明白了！\n不如让你的宝可梦学习替身吧？$
- 理由：JP「そうだわ（对了/我有主意了）」是想出主意的感叹，补丁/美版中文误作「明白了」，语义错误；且「我在想如果这个世界如果有不止一个自己」中「如果」重复，属衍字；其余「なんにんものじぶんがいていくつものじんせいをたのしめたらなー」与「有不止一个自己该多有趣…体验各种各样的人生」语义一致。
- 修改建议：当我在屋顶上看着这广阔的世界时……我在想如果这个世界有不止一个自己该多有趣啊，那样我就能体验各种各样的人生了。当然这是不可能的。嘿嘿……对了！不如让你的宝可梦学习替身吧？

当前日版：

`当我在屋顶上看着\n这广阔的世界时……\p我在想如果这个世界\n有不止一个自己该多有趣啊，\l那样我就能体验各种各样的人生了。\p当然这是不可能的。\n嘿嘿……\p明白了！\n不如让你的宝可梦学习替身吧？`

文件：`patch/batches/340_move_tutors.json`。

原日文（`0x08276436`）：

`ふう\nこうやって　おくじょうから\lひろい　せかいを　みていると……\pなんにんもの　じぶんが　いて\nいくつもの　じんせいを　たのしめたらな-\lって　おもうの!\lムリな　はなしだけどね　うふふ\pそうだわ　あなたの　ポケモンちゃん!\nみがわりの　わざ　おぼえてみない?`

Wokann日文（`data/text/move_tutors.inc`）：

`ふう\nこうやって　おくじょうから\lひろい　せかいを　みていると⋯⋯\pなんにんもの　じぶんが　いて\nいくつもの　じんせいを　たのしめたらなー\lって　おもうの！\lムリな　はなしだけどね　うふふ\pそうだわ　あなたの　ポケモンちゃん！\nみがわりの　わざ　おぼえてみない？$`

原英文（`data/text/move_tutors.inc`，`fe570a7e5^`）：

`When I see the wide world from up\nhere on the roof…\pI think about how nice it would be\nif there were more than just one me\lso I could enjoy all sorts of lives.\pOf course it's not possible.\nGiggle…\pI know! Would you be interested in\nhaving a POKéMON learn SUBSTITUTE?$`

当前美版（`data/text/move_tutors.inc`）：

`当我在屋顶上看着\n这广阔的世界时……\p我在想如果这个世界\n有不止一个自己该多有趣啊，\l那样我就能体验各种各样的人生了。\p当然这是不可能的。\n嘿嘿……\p明白了！\n不如让你的宝可梦学习替身吧？$`

### 13 — Route116_Text_JoeyIntro

结论：**需修复**。

rule / つえー 是厉害，不是运用。

方案：我的宝可梦很厉害！\n你就好好瞧瞧吧！

原建议：

- JP：おれの　ポケモン　つえーぞ！\nちょっと　みてみろよ！$
- EN：My POKéMON rule!\nCheck them out!$
- 中文：我的宝可梦运用！\n你就好好瞧瞧吧！$
- 理由：JP「おれの ポケモン つえーぞ」(我的宝可梦很强)/EN"My POKéMON rule!"→CHS「我的宝可梦运用!」,“运用”意为使用/应用,语义不通
- 修改建议：我的宝可梦很强！

当前日版：

`我的宝可梦运用！\n你就好好瞧瞧吧！`

文件：`patch/batches/028_route116.json`。

原日文（`0x0825D643`）：

`おれの　ポケモン　つえ-ぞ!\nちょっと　みてみろよ!`

Wokann日文（`data/text/trainers.inc`）：

`おれの　ポケモン　つえーぞ！\nちょっと　みてみろよ！$`

原英文（`data/text/trainers.inc`，`fe570a7e5^`）：

`My POKéMON rule!\nCheck them out!$`

当前美版（`data/text/trainers.inc`）：

`我的宝可梦运用！\n你就好好瞧瞧吧！$`

### 14 — Route123_Text_BraxtonPostBattle

结论：**需修复**。

战斗不辱徽章，而非在此次战斗中获得徽章。

方案：这场战斗真是\n无愧于你的道馆徽章！

原建议：

- JP：ジムバッジに　はじない\nたたかい　だったよ！$
- EN：You did your BADGES proud in that\nmatch!$
- 中文：在那样的对战中获得徽章\n是你的骄傲。$
- 理由：JP「ジムバッジに はじない たたかい だったよ」(那场对战无愧于徽章)/EN"You did your BADGES proud"→CHS「在那样的对战中获得徽章是你的骄傲」,把"无愧于徽章"误作"获得徽章是骄傲",主谓关系颠倒
- 修改建议：那场对战无愧于你的道馆徽章！

当前日版：

`在那样的对战中获得徽章\n是你的骄傲。`

文件：`patch/batches/148_route123.json`。

原日文（`0x0825FA26`）：

`ジムバッジに　はじない\nたたかい　だったよ!`

Wokann日文（`data/text/trainers.inc`）：

`ジムバッジに　はじない\nたたかい　だったよ！$`

原英文（`data/text/trainers.inc`，`fe570a7e5^`）：

`You did your BADGES proud in that\nmatch!$`

当前美版（`data/text/trainers.inc`）：

`在那样的对战中获得徽章\n是你的骄傲。$`

### 15 — SecretBase_Text_Trainer1PreChampion

结论：**需修复**。

已经终于获得使用机会，不是仍等着开放。

方案：这个地方很受欢迎，\n总是有人占着。\p我等了很久，\n终于轮到我使用了！

原建议：

- JP：この　ばしょは　にんきが　あるから\nいつも　うまって　いるんだよー\pぼくは　ずっと　まっていて\nやっと　つかえる　ように　なったんだ！$
- EN：This is a popular spot.\nIt's always taken.\pI waited a long time for it to open.\nI finally got to use it!$
- 中文：这个地方非常受欢迎，\n经常会有人来这里。\p我一直在等它打开，\n我一定要得到它！$
- 理由：JP“やっと つかえる ように なったんだ”(终于能用上这里了)/EN“I finally got to use it!”；中文“我一定要得到它”与原文“终于得以使用”语义相反方向，为误译。
- 修改建议：我一直在等它空出来，终于能用上这里了！

### 语义偏差（8 条）

当前日版：

`这个地方非常受欢迎，\n经常会有人来这里。\p我一直在等它打开，\n我一定要得到它！`

文件：`patch/batches/391_secret_base_trainers.json`。

原日文（`0x082453A7`）：

`この　ばしょは　にんきが　あるから\nいつも　うまって　いるんだよ-\pぼくは　ずっと　まっていて\nやっと　つかえる　ように　なったんだ!`

Wokann日文（`data/text/secret_base_trainers.inc`）：

`この　ばしょは　にんきが　あるから\nいつも　うまって　いるんだよー\pぼくは　ずっと　まっていて\nやっと　つかえる　ように　なったんだ！$`

原英文（`data/text/secret_base_trainers.inc`，`fe570a7e5^`）：

`This is a popular spot.\nIt's always taken.\pI waited a long time for it to open.\nI finally got to use it!$`

当前美版（`data/text/secret_base_trainers.inc`）：

`这个地方非常受欢迎，\n经常会有人来这里。\p我一直在等它打开，\n我一定要得到它！$`

### 16 — BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteMMon1

结论：**需修复**。

decent 是不错；日文说自己培育的。高贵/一对不合适。

方案：日版开头“我培育的宝可梦是……”；美版开头“我有两只不错的宝可梦。”；后半招式、物种变量不变。

原建议：

- JP：オレの　そだてた　ポケモンは\n{STR_VAR_1}を　つかう　{STR_VAR_2}と⋯⋯$
- EN：I got a couple decent POKéMON.\nOne {STR_VAR_2} with {STR_VAR_1} and$
- 中文：我有一对高贵的宝可梦。\n一只掌握{STR_VAR_1}的{STR_VAR_2}和$
- 理由：EN「a couple decent POKéMON」意为「几只不错的宝可梦」，JP「そだてた ポケモン」仅为「培育的宝可梦」；补丁中文「高贵的宝可梦」将decent误作「高贵」，语义偏差。
- 修改建议：我有一对不错的宝可梦。\n一只掌握{STR_VAR_1}的{STR_VAR_2}和$

当前日版：

`我有一对高贵的宝可梦。\n一只掌握{FD_02}的{FD_03}和`

文件：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`。

原日文（`0x08226286`）：

`オレの　そだてた　ポケモンは\n{PLACEHOLDER_02}を　つかう　{PLACEHOLDER_03}と……`

Wokann日文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`オレの　そだてた　ポケモンは\n{STR_VAR_1}を　つかう　{STR_VAR_2}と⋯⋯$`

原英文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`，`fe570a7e5^`）：

`I got a couple decent POKéMON.\nOne {STR_VAR_2} with {STR_VAR_1} and$`

当前美版（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`我有一对高贵的宝可梦。\n一只掌握{STR_VAR_1}的{STR_VAR_2}和$`

### 17 — BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteMMon2Ask

结论：**需修复**。

neat 在此是组队不错，不是高雅。

方案：如果我们一起组队\n一定很不错，你觉得呢？；前半的招式、物种变量保留。

原建议：

- JP：{STR_VAR_1}を　つかう　{STR_VAR_2}　だよ\pどう？\nオレと　タッグを　くんでみない？$
- EN：one {STR_VAR_2} with {STR_VAR_1}!\pIt'd be neat if we made a tag team\ntogether, so how about it?$
- 中文：一只掌握{STR_VAR_1}的{STR_VAR_2}！\p如果我们组队，那是多高雅的\n一件事呀，你觉得呢？$
- 理由：EN「It'd be neat if we made a tag team」意为「组队会很不错」；补丁中文「那是多高雅的一件事呀」将neat(很棒)误作「高雅」，语义偏差。
- 修改建议：一只掌握{STR_VAR_1}的{STR_VAR_2}！\p如果我们组队，那就太棒了，\n你觉得呢？$

当前日版：

`一只掌握{FD_02}的{FD_03}！\p如果我们组队，那是多高雅的\n一件事呀，你觉得呢？`

文件：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`。

原日文（`0x082262A3`）：

`{PLACEHOLDER_02}を　つかう　{PLACEHOLDER_03}　だよ\pどう?\nオレと　タッグを　くんでみない?`

Wokann日文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`{STR_VAR_1}を　つかう　{STR_VAR_2}　だよ\pどう？\nオレと　タッグを　くんでみない？$`

原英文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`，`fe570a7e5^`）：

`one {STR_VAR_2} with {STR_VAR_1}!\pIt'd be neat if we made a tag team\ntogether, so how about it?$`

当前美版（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`一只掌握{STR_VAR_1}的{STR_VAR_2}！\p如果我们组队，那是多高雅的\n一件事呀，你觉得呢？$`

### 18 — BattleFrontier_Lounge5_Text_LadyClaimsSheUnderstandsPokemon

结论：**需修复**。

charming / シャレた 是有趣俏皮，不是魔法。

方案：真有意思！\n那位小女孩说她能\l懂得宝可梦的心情！

原建议：

- JP：ポケモンの　きもちが　わかるとは\nあの　おじょうちゃん　なかなか\lシャレた　ことを　もうしますな！$
- EN：How charming!\nThat little lady claims she can\lunderstand POKéMON!$
- 中文：好像魔法一样啊！\n那边那位小女孩说她能\l懂得宝可梦在说什么！$
- 理由：JP「なかなか シャレた ことを もうしますな(真会说俏皮话)」与EN「How charming!」均为赞赏机灵，补丁中文「好像魔法一样啊」将「シャレた(机灵/俏皮)」误作「魔法」，语义错误。
- 修改建议：真有意思！\n那边那位小女孩说她能\l懂得宝可梦的心情！$

当前日版：

`好像魔法一样啊！\n那边那位小女孩说她能\l懂得宝可梦在说什么！`

文件：`patch/batches/399_frontier_lounge5.json`。

原日文（`0x08239538`）：

`ポケモンの　きもちが　わかるとは\nあの　おじょうちゃん　なかなか\lシャレた　ことを　もうしますな!`

Wokann日文（`data/maps/BattleFrontier_Lounge5/scripts.inc`）：

`ポケモンの　きもちが　わかるとは\nあの　おじょうちゃん　なかなか\lシャレた　ことを　もうしますな！$`

原英文（`data/maps/BattleFrontier_Lounge5/scripts.inc`，`fe570a7e5^`）：

`How charming!\nThat little lady claims she can\lunderstand POKéMON!$`

当前美版（`data/maps/BattleFrontier_Lounge5/scripts.inc`）：

`好像魔法一样啊！\n那边那位小女孩说她能\l懂得宝可梦在说什么！$`

### 19 — BattleFrontier_OutsideEast_Text_ThriveInDarkness

结论：**需修复**。

开头已修，邀请探索的结尾仍误译；日英区域差异应保留。

方案：日版邀请在黑暗中拼命探索；美版邀请在黑暗与彻底绝望中探索，不再询问“你是不是也会陷入”。

原建议：

- JP：くらやみが　だいすきな　わたし⋯⋯\nそう⋯⋯　わたしに　ふさわしい　のは⋯⋯\lやはり　この　バトルピラミッド⋯⋯\pネ⋯⋯　あなたも　くらやみの　なかを\nひっしに　さまよって　みない⋯⋯？$
- EN：I thrive in darkness…\nYes… What is worthy of me?\lNone other than the BATTLE PYRAMID…\pWhat say you to wandering in dar
- 中文：我是在黑暗中长大的……\n是的……哪里最适合我？\l必然是对战金字塔……\p在黑暗中探索的时候\n你是不是也会陷入完全的绝望？$
- 理由：JP「くらやみが だいすきな わたし(我最喜欢黑暗)」与EN「I thrive in darkness」均为喜爱/沉浸于黑暗，补丁中文「我是在黑暗中长大的」将「だいすき(喜爱)」误作「长大」，语义错误。
- 修改建议：我最喜欢黑暗了……\n是的……哪里最适合我？\l必然是对战金字塔……\p在黑暗中探索的时候\n你是不是也会陷入完全的绝望？$

当前日版：

`我最喜欢黑暗……\n是的……哪里最适合我？\l必然是对战金字塔……\p在黑暗中探索的时候\n你是不是也会陷入完全的绝望？`

文件：`patch/batches/227_battle_frontier_outside_east.json`。

原日文（`0x08222D54`）：

`くらやみが　だいすきな　わたし……\nそう……　わたしに　ふさわしい　のは……\lやはり　この　バトルピラミッド……\pネ……　あなたも　くらやみの　なかを\nひっしに　さまよって　みない……?`

Wokann日文（`data/maps/BattleFrontier_OutsideEast/scripts.inc`）：

`くらやみが　だいすきな　わたし⋯⋯\nそう⋯⋯　わたしに　ふさわしい　のは⋯⋯\lやはり　この　バトルピラミッド⋯⋯\pネ⋯⋯　あなたも　くらやみの　なかを\nひっしに　さまよって　みない⋯⋯？$`

原英文（`data/maps/BattleFrontier_OutsideEast/scripts.inc`，`fe570a7e5^`）：

`I thrive in darkness…\nYes… What is worthy of me?\lNone other than the BATTLE PYRAMID…\pWhat say you to wandering in darkness\nand in utter and total desperation?$`

当前美版（`data/maps/BattleFrontier_OutsideEast/scripts.inc`）：

`我最喜欢黑暗……\n是的……哪里最适合我？\l必然是对战金字塔……\p在黑暗中探索的时候\n你是不是也会陷入完全的绝望？$`

### 20 — DewfordTown_Gym_Text_BrendenIntro

结论：**需修复**。

いじ / gumption 是骨气胆识，不是智慧。

方案：让你看看\n海之男儿的骨气！

原建议：

- JP：うみの　おとこの　いじを
みせつけて　やるぜぃ!
- EN：I'll show you the gumption of\na sailing man!$
- 中文：让你看看\n水手的智慧！$
- 理由：JP「うみの おとこの いじ(海之男儿的骨气/意气)」与EN「the gumption of a sailing man」均指骨气胆识，补丁中文「水手的智慧」将「いじ(意气)」误作「智慧」，语义错误。
- 修改建议：让你看看\n海之男儿的骨气！$

当前日版：

`让你看看\n水手的智慧！`

文件：`patch/batches/023_dewford_gym.json`。

原日文（`0x081F3395`）：

`うみの　おとこの　いじを\nみせつけて　やるぜぃ!`

Wokann日文（`data/maps/DewfordTown_Gym/scripts.inc`）：

`うみの　おとこの　いじを\nみせつけて　やるぜぃ！$`

原英文（`data/maps/DewfordTown_Gym/scripts.inc`，`fe570a7e5^`）：

`I'll show you the gumption of\na sailing man!$`

当前美版（`data/maps/DewfordTown_Gym/scripts.inc`）：

`让你看看\n水手的智慧！$`

### 21 — EverGrandeCity_PokemonCenter_1F_Text_LeagueAfterVictoryRoad

结论：**已修复**。

现在明确只能继续前进。

方案：不修改。

原建议：

- JP：ポケモンリ-グは
チャンピオンロ-ドを　ぬけると　すぐ!\pここまで　きたら
まえに　すすむしかないわ!
- EN：The POKéMON LEAGUE is only a short\ndistance after the VICTORY ROAD.\pIf you've come this far, what choice\ndo you have
- 中文：穿过冠军之路，\n宝可梦联盟就在眼前。\p已经走了这么远，\n到底是什么让你坚持到现在？$
- 理由：JP「ここまで きたら まえに すすむしかないわ(走到这一步，除了继续前进别无选择)」与EN「what choice do you have but to keep going」均为敦促继续前进的反问；补丁中文「到底是什么让你坚持到现在？」将反问改作追问坚持的原因，语义错误。
- 修改建议：穿过冠军之路，\n宝可梦联盟就在眼前。\p已经走了这么远，\n除了继续前进别无选择！$

当前日版：

`穿过冠军之路，\n宝可梦联盟就在眼前。\p已经走了这么远，\n只能继续前进了！`

文件：`patch/batches/196_pokemon_centers.json`。

原日文（`0x082114A2`）：

`ポケモンリ-グは\nチャンピオンロ-ドを　ぬけると　すぐ!\pここまで　きたら\nまえに　すすむしかないわ!`

Wokann日文（`data/maps/EverGrandeCity_PokemonCenter_1F/scripts.inc`）：

`ポケモンリーグは\nチャンピオンロードを　ぬけると　すぐ！\pここまで　きたら\nまえに　すすむしかないわ！$`

原英文（`data/maps/EverGrandeCity_PokemonCenter_1F/scripts.inc`，`fe570a7e5^`）：

`The POKéMON LEAGUE is only a short\ndistance after the VICTORY ROAD.\pIf you've come this far, what choice\ndo you have but to keep going?$`

当前美版（`data/maps/EverGrandeCity_PokemonCenter_1F/scripts.inc`）：

`穿过冠军之路，\n宝可梦联盟就在眼前。\p已经走了这么远，\n只能继续前进了！$`

### 22 — FortreeCity_House1_Text_GoingToMakeVolbeatStrong

结论：**需修复**。

要求同样把正电拍拍培养强大，不是泛泛善待。

方案：末句改为“你也要把正电拍拍\n培养得更强啊！”

原建议：

- JP：よし　いまから
バルビ-トを　つよく　するぞ-!\lプラスルも　つよく　してやってよ!
- EN：I'm going to make VOLBEAT super\nstrong from this moment on!\pI hope you do the same with PLUSLE!$
- 中文：从现在开始，我要把甜甜萤\n养得壮壮的！\p你也要善待正电拍拍啊！$
- 理由：JP「バルビ-トを つよく するぞ-! プラスルも つよく してやってよ(也要把正电拍拍变强)」与EN「I hope you do the same with PLUSLE!(同样把PLUSLE变强)」均为「变强」；补丁中文与美版中文均为「你也要善待正电拍拍啊」，将「变强」误作「善待」，语义错误。
- 修改建议：从现在开始，我要把甜甜萤\n养得壮壮的！\p你也要把正电拍拍养得壮壮的啊！

当前日版：

`从现在开始，我要把甜甜萤\n养得壮壮的！\p你也要善待正电拍拍啊！`

文件：`patch/batches/107_fortreecity_house1.json`。

原日文（`0x08204334`）：

`よし　いまから\nバルビ-トを　つよく　するぞ-!\lプラスルも　つよく　してやってよ!`

Wokann日文（`data/maps/FortreeCity_House1/scripts.inc`）：

`よし　いまから\nバルビートを　つよく　するぞー！\lプラスルも　つよく　してやってよ！$`

原英文（`data/maps/FortreeCity_House1/scripts.inc`，`fe570a7e5^`）：

`I'm going to make VOLBEAT super\nstrong from this moment on!\pI hope you do the same with PLUSLE!$`

当前美版（`data/maps/FortreeCity_House1/scripts.inc`）：

`从现在开始，我要把甜甜萤\n养得壮壮的！\p你也要善待正电拍拍啊！$`

### 23 — FortreeCity_House3_Text_MetStevenHadAmazingPokemon

结论：**已修复**。

现在明确不止是稀有。

方案：不修改。

原建议：

- JP：ポケモンずかんで
おもいだした　ことが　あるよ\pめずらしい　いしを　さがしてるとき
ダイゴって　トレ-ナ-と　であったけど\lあいつの　ポケモン　すごいね!\pめずらしい　だけでなく
おそろしいほど　きたえられてた!\pもしかしたら　この
- EN：While speaking about POKéDEXES,\nI remembered something.\pI met this TRAINER, STEVEN, when\nI was searching for rare sto
- 中文：说到宝可梦图鉴，\n我想起来了，\p我寻找稀有石头的时候\n遇到了那个叫大吾的训练家。\p哈，他带着一些\n奇妙的宝可梦，\p它们不止是强大，\n还在训练中发挥到了极致！\p他也许比这城镇的\n道馆馆主还要强……$
- 理由：JP「めずらしい だけでなく おそろしいほど きたえられてた(不只是稀有，还被锻炼到了可怕的地步)」与EN「They weren't just rare, they were trained to terrifying extremes」关键形容词是「稀有」；补丁中文与美版中文均为「它们不止是强大，还在训练中发挥到了极致」，将「稀有」误作「强大」，语义错误。
- 修改建议：它们不只是稀有，\n还被锻炼到了可怕的地步！

### 语义反转（8 条）

当前日版：

`说到宝可梦图鉴，\n我想起来了，\p我寻找稀有石头的时候\n遇到了那个叫大吾的训练家。\p哈，他带着一些\n奇妙的宝可梦，\p它们不止是稀有，\n还在训练中发挥到了极致！\p他也许比这城镇的\n道馆馆主还要强……`

文件：`patch/batches/245_fortree_city_house3.json`。

原日文（`0x082050E3`）：

`ポケモンずかんで\nおもいだした　ことが　あるよ\pめずらしい　いしを　さがしてるとき\nダイゴって　トレ-ナ-と　であったけど\lあいつの　ポケモン　すごいね!\pめずらしい　だけでなく\nおそろしいほど　きたえられてた!\pもしかしたら　この　まちの\nジムリ-ダ-よりも　つよいかも……`

Wokann日文（`data/maps/FortreeCity_House3/scripts.inc`）：

`ポケモンずかんで\nおもいだした　ことが　あるよ\pめずらしい　いしを　さがしてるとき\nダイゴって　トレーナーと　であったけど\lあいつの　ポケモン　すごいね！\pめずらしい　だけでなく\nおそろしいほど　きたえられてた！\pもしかしたら　この　まちの\nジムリーダーよりも　つよいかも⋯⋯$`

原英文（`data/maps/FortreeCity_House3/scripts.inc`，`fe570a7e5^`）：

`While speaking about POKéDEXES,\nI remembered something.\pI met this TRAINER, STEVEN, when\nI was searching for rare stones.\pHoo, boy, he had some amazing POKéMON\nwith him.\pThey weren't just rare, they were\ntrained to terrifying extremes!\pHe might even be stronger than the\nGYM LEADER in this town…$`

当前美版（`data/maps/FortreeCity_House3/scripts.inc`）：

`说到宝可梦图鉴，\n我想起来了，\p我寻找稀有石头的时候\n遇到了那个叫大吾的训练家。\p哈，他带着一些\n奇妙的宝可梦，\p它们不止是稀有，\n还在训练中发挥到了极致！\p他也许比这城镇的\n道馆馆主还要强……$`

### 24 — BattlePyramid_Text_FiveTrainersRemaining2

结论：**已修复**。

现在说五位训练家中有人会击败玩家。

方案：不修改。

原建议：

- JP：くやしいー！\pでも　あと　5にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there are five TRAINERS left!\nSomeone will humble you!$
- 中文：真不幸！\p后面还有5位训练家！\n他们中或许有人比你弱！$
- 理由：JP「あと 5にん いる トレーナーが きっと たおしてくれるわ(剩下的5个训练家一定会打败你)」与EN「Someone will humble you!(有人会让你吃瘪)」均为对手将获胜；补丁中文「他们中或许有人比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有5位训练家！\n他们一定会打败你的！$

当前日版：

`真不幸！\p后面还有5位训练家！\n他们中一定有人能打败你！`

文件：`patch/batches/437_checklist_reviewed_indirect_tables.json`。

原日文（`0x0822E429`）：

`くやしい-!\pでも　あと　5にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ`

Wokann日文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`くやしいー！\pでも　あと　5にん　いる　トレーナーが\nきっと　たおしてくれるわ$`

原英文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，`fe570a7e5^`）：

`This is so upsetting!\pBut there are five TRAINERS left!\nSomeone will humble you!$`

当前美版（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`真不幸！\p后面还有5位训练家！\n他们中一定有人能打败你！$`

### 25 — BattlePyramid_Text_FourTrainersRemaining2

结论：**已修复**。

四位训练家的获胜对象已恢复。

方案：不修改。

原建议：

- JP：くやしいー！\pでも　あと　4にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there are four TRAINERS left!\nSomeone will humble you!$
- 中文：真不幸！\p后面还有4位训练家！\n他们中或许有人比你弱！$
- 理由：JP「あと 4にん いる トレーナーが きっと たおしてくれるわ(剩下的4个训练家一定会打败你)」与EN「Someone will humble you!」均为对手将获胜；补丁中文「他们中或许有人比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有4位训练家！\n他们一定会打败你的！$

当前日版：

`真不幸！\p后面还有4位训练家！\n他们中一定有人能打败你！`

文件：`patch/batches/437_checklist_reviewed_indirect_tables.json`。

原日文（`0x0822E451`）：

`くやしい-!\pでも　あと　4にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ`

Wokann日文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`くやしいー！\pでも　あと　4にん　いる　トレーナーが\nきっと　たおしてくれるわ$`

原英文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，`fe570a7e5^`）：

`This is so upsetting!\pBut there are four TRAINERS left!\nSomeone will humble you!$`

当前美版（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`真不幸！\p后面还有4位训练家！\n他们中一定有人能打败你！$`

### 26 — BattlePyramid_Text_OneTrainersRemaining2

结论：**已修复**。

最后一位会击败玩家。

方案：不修改。

原建议：

- JP：くやしいー！\pでも　あと　1にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there's one TRAINER left!\nI'm sure you will be humbled!$
- 中文：真不幸！\p后面还有1位训练家！\n他或许比你弱！$
- 理由：JP「あと 1にん いる トレーナーが きっと たおしてくれるわ(剩下的1个训练家一定会打败你)」与EN「I'm sure you will be humbled!」均为对手将获胜；补丁中文「他或许比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有1位训练家！\n他一定会打败你的！$

当前日版：

`真不幸！\p后面还有1位训练家！\n他一定会打败你！`

文件：`patch/batches/437_checklist_reviewed_indirect_tables.json`。

原日文（`0x0822E4C9`）：

`くやしい-!\pでも　あと　1にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ`

Wokann日文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`くやしいー！\pでも　あと　1にん　いる　トレーナーが\nきっと　たおしてくれるわ$`

原英文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，`fe570a7e5^`）：

`This is so upsetting!\pBut there's one TRAINER left!\nI'm sure you will be humbled!$`

当前美版（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`真不幸！\p后面还有1位训练家！\n他一定会打败你！$`

### 27 — BattlePyramid_Text_SevenTrainersRemaining2

结论：**已修复**。

七位训练家的获胜对象已恢复。

方案：不修改。

原建议：

- JP：くやしいー！\pでも　あと　7にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there are seven TRAINERS left!\nSomeone will humble you!$
- 中文：真不幸！\p后面还有7位训练家！\n他们中或许有人比你弱！$
- 理由：JP「あと 7にん いる トレーナーが きっと たおしてくれるわ(剩下的7个训练家一定会打败你)」与EN「Someone will humble you!」均为对手将获胜；补丁中文「他们中或许有人比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有7位训练家！\n他们一定会打败你的！$

当前日版：

`真不幸！\p后面还有7位训练家！\n他们中一定有人能打败你！`

文件：`patch/batches/437_checklist_reviewed_indirect_tables.json`。

原日文（`0x0822E3D9`）：

`くやしい-!\pでも　あと　7にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ`

Wokann日文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`くやしいー！\pでも　あと　7にん　いる　トレーナーが\nきっと　たおしてくれるわ$`

原英文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，`fe570a7e5^`）：

`This is so upsetting!\pBut there are seven TRAINERS left!\nSomeone will humble you!$`

当前美版（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`真不幸！\p后面还有7位训练家！\n他们中一定有人能打败你！$`

### 28 — BattlePyramid_Text_SixTrainersRemaining2

结论：**已修复**。

六位训练家的获胜对象已恢复。

方案：不修改。

原建议：

- JP：くやしいー！\pでも　あと　6にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there are six TRAINERS left!\nSomeone will humble you!$
- 中文：真不幸！\p后面还有6位训练家！\n他们中或许有人比你弱！$
- 理由：JP「あと 6にん いる トレーナーが きっと たおしてくれるわ(剩下的6个训练家一定会打败你)」与EN「Someone will humble you!」均为对手将获胜；补丁中文「他们中或许有人比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有6位训练家！\n他们一定会打败你的！$

当前日版：

`真不幸！\p后面还有6位训练家！\n他们中一定有人能打败你！`

文件：`patch/batches/437_checklist_reviewed_indirect_tables.json`。

原日文（`0x0822E401`）：

`くやしい-!\pでも　あと　6にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ`

Wokann日文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`くやしいー！\pでも　あと　6にん　いる　トレーナーが\nきっと　たおしてくれるわ$`

原英文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，`fe570a7e5^`）：

`This is so upsetting!\pBut there are six TRAINERS left!\nSomeone will humble you!$`

当前美版（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`真不幸！\p后面还有6位训练家！\n他们中一定有人能打败你！$`

### 29 — BattlePyramid_Text_ThreeTrainersRemaining2

结论：**已修复**。

三位训练家的获胜对象已恢复。

方案：不修改。

原建议：

- JP：くやしいー！\pでも　あと　3にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there are three TRAINERS left!\nSomeone will humble you!$
- 中文：真不幸！\p后面还有3位训练家！\n他们中或许有人比你弱！$
- 理由：JP「あと 3にん いる トレーナーが きっと たおしてくれるわ(剩下的3个训练家一定会打败你)」与EN「Someone will humble you!」均为对手将获胜；补丁中文「他们中或许有人比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有3位训练家！\n他们一定会打败你的！$

当前日版：

`真不幸！\p后面还有3位训练家！\n他们中一定有人能打败你！`

文件：`patch/batches/437_checklist_reviewed_indirect_tables.json`。

原日文（`0x0822E479`）：

`くやしい-!\pでも　あと　3にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ`

Wokann日文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`くやしいー！\pでも　あと　3にん　いる　トレーナーが\nきっと　たおしてくれるわ$`

原英文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，`fe570a7e5^`）：

`This is so upsetting!\pBut there are three TRAINERS left!\nSomeone will humble you!$`

当前美版（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`真不幸！\p后面还有3位训练家！\n他们中一定有人能打败你！$`

### 30 — BattlePyramid_Text_TwoTrainersRemaining2

结论：**已修复**。

两位训练家的获胜对象已恢复。

方案：不修改。

原建议：

- JP：くやしいー！\pでも　あと　2にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there are two TRAINERS left!\nSomeone will humble you!$
- 中文：真不幸！\p后面还有2位训练家！\n他们中或许有人比你弱！$
- 理由：JP「あと 2にん いる トレーナーが きっと たおしてくれるわ(剩下的2个训练家一定会打败你)」与EN「Someone will humble you!」均为对手将获胜；补丁中文「他们中或许有人比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有2位训练家！\n他们一定会打败你的！$

当前日版：

`真不幸！\p后面还有2位训练家！\n他们中一定有人能打败你！`

文件：`patch/batches/437_checklist_reviewed_indirect_tables.json`。

原日文（`0x0822E4A1`）：

`くやしい-!\pでも　あと　2にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ`

Wokann日文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`くやしいー！\pでも　あと　2にん　いる　トレーナーが\nきっと　たおしてくれるわ$`

原英文（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，`fe570a7e5^`）：

`This is so upsetting!\pBut there are two TRAINERS left!\nSomeone will humble you!$`

当前美版（`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`）：

`真不幸！\p后面还有2位训练家！\n他们中一定有人能打败你！$`

### 31 — LilycoveCity_PokemonTrainerFanClub_Text_YoureOneWeWantToWin

结论：**需修复**。

为玩家加油，不是想打败玩家，主客体反转。

方案：嗨，{PLAYER}！\n我们希望你能获胜！；日版仍用 FD_01。

原建议：

- JP：おう　{FD:01}!!
おうえん　してるぞ!!
- EN：Yo, {PLAYER}!\nYou're the one we want to win!$
- 中文：嗨，{PLAYER}！\n我们一直想要胜过你！$
- 理由：JP「おう{FD:01}！！おうえんしてるぞ」/EN“You're the one we want to win!”意为“我们希望你赢、为你加油”，中文“我们一直想要胜过你！”把“希望你获胜”反转为“想要打败你”，语义完全颠倒。
- 修改建议：嗨，{PLAYER}！\n我们希望你能获胜！

### 错字（6 条）

当前日版：

`嗨，{FD_01}！\n我们一直想要胜过你！`

文件：`patch/batches/139_lilycovecity_pokemontrainerfanclub.json`。

原日文（`0x08208BEC`）：

`おう　{PLACEHOLDER_01}!!\nおうえん　してるぞ!!`

Wokann日文（`data/maps/LilycoveCity_PokemonTrainerFanClub/scripts.inc`）：

`おう　{PLAYER}！！\nおうえん　してるぞ！！$`

原英文（`data/maps/LilycoveCity_PokemonTrainerFanClub/scripts.inc`，`fe570a7e5^`）：

`Yo, {PLAYER}!\nYou're the one we want to win!$`

当前美版（`data/maps/LilycoveCity_PokemonTrainerFanClub/scripts.inc`）：

`嗨，{PLAYER}！\n我们一直想要胜过你！$`

### 32 — GraniteCave_StevensRoom_Text_ImStevenLetterForMe

结论：**需修复**。

所有经常是笔误。

方案：“所有经常”改“所以经常”。

原建议：

- JP：ボクの　なまえは　ダイゴ\pめずらしい　いしに　きょうみが　あって
あちこち　たび　してるんだよ\pえっ?
ボクに　てがみ……?
- EN：My name is STEVEN.\pI'm interested in rare stones,\nso I travel here and there.\pOh?\nA LETTER for me?$
- 中文：我的名字是大吾。\p我对稀有的石头很有兴趣，\n所有经常四处旅行。\p哦？\n有给我的信？$
- 理由：JP「めずらしいいしにきょうみがあってあちこちたびしてるんだよ」/EN“I'm interested in rare stones, so I travel”意为“对稀有石头感兴趣，所以经常四处旅行”，中文“所有经常四处旅行”中“所有”系“所以”之误，美版中文同样错写。
- 修改建议：我的名字是大吾。\p我对稀有的石头很有兴趣，\n所以经常四处旅行。\p哦？\n有给我的信？

当前日版：

`我的名字是大吾。\p我对稀有的石头很有兴趣，\n所有经常四处旅行。\p哦？\n有给我的信？`

文件：`patch/batches/027_stevens_room.json`。

原日文（`0x08214107`）：

`ボクの　なまえは　ダイゴ\pめずらしい　いしに　きょうみが　あって\nあちこち　たび　してるんだよ\pえっ?\nボクに　てがみ……?`

Wokann日文（`data/maps/GraniteCave_StevensRoom/scripts.inc`）：

`ボクの　なまえは　ダイゴ\pめずらしい　いしに　きょうみが　あって\nあちこち　たび　してるんだよ\pえっ？\nボクに　てがみ⋯⋯？$`

原英文（`data/maps/GraniteCave_StevensRoom/scripts.inc`，`fe570a7e5^`）：

`My name is STEVEN.\pI'm interested in rare stones,\nso I travel here and there.\pOh?\nA LETTER for me?$`

当前美版（`data/maps/GraniteCave_StevensRoom/scripts.inc`）：

`我的名字是大吾。\p我对稀有的石头很有兴趣，\n所有经常四处旅行。\p哦？\n有给我的信？$`

### 33 — MossdeepCity_StevensHouse_Text_LetterFromSteven

结论：**已修复**。

锻炼/探索旅程以及铁哑铃含义已修复。

方案：不修改。

原建议：

- JP：てがみが　ある!\p……　……　……
……　……　……\p{FD:01}{FD:05}へ\pボクは　おもうことが　あって
しばらく　しゅぎょうを　つづける\lとうぶん　いえに　かえらない\pそこで　おねがいだ\pつくえの　うえにある
モンス
- EN：It's a letter.\p… … … … … …\pTo {PLAYER}{KUN}…\pI've decided to do a little soul-\nsearching and train on the road.\pI d
- 中文：是一封信。\p…… …… ……\p致{PLAYER}{KUN}……\p已我决定踏上自我\n探索与修行之旅。\p短时间内不\n打算回家，\p我想拜托你收下\n桌上的精灵球，\p里面是我最喜欢的宝可梦——\n铁哑铃，\p拜托你照顾好它。\p愿你
- 理由：JP「ボクはおもうことがあってしばらくしゅぎょうをつづける（我有些想法，要继续修行一阵子）」/EN「I've decided to do a little soul-searching and train on the road」中「我已决定」被补丁/美版中文误作「已我决定」，「我」「已」二字顺序颠倒，属错字；其余「短时间内不打算回家」「收下桌上的精灵球」「里面是我最喜欢的宝可梦——铁哑铃」「愿你我终有相逢之日」语义一致。
- 修改建议：我已决定踏上自我探索与修行之旅。

当前日版：

`是一封信。\p…… …… ……\p致{FD_01}{FD_05}……\p我已决定踏上自我\n探索与修行之旅。\p短时间内不\n打算回家，\p我想拜托你收下\n桌上的精灵球，\p里面是我最喜欢的宝可梦——\n铁哑铃，\p拜托你照顾好它。\p愿你我终有相逢之日。\p大吾·兹伏奇`

文件：`patch/batches/159_mossdeepcity_stevenshouse.json`。

原日文（`0x0820CB77`）：

`てがみが　ある!\p……　……　……\n……　……　……\p{PLACEHOLDER_01}{PLACEHOLDER_05}へ\pボクは　おもうことが　あって\nしばらく　しゅぎょうを　つづける\lとうぶん　いえに　かえらない\pそこで　おねがいだ\pつくえの　うえにある\nモンスタ-ボ-ルを　うけとって　ほしい\pなかに　いるのは　ダンバルといって\nボクの　おきにいりの　ポケモンだから\pよろしく　たのむよ\pでは　また　いつか　あおう!\n　　　　　　ツワブキ　ダイゴより`

Wokann日文（`data/maps/MossdeepCity_StevensHouse/scripts.inc`）：

`てがみが　ある！\p⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯\p{PLAYER}{KUN}へ\pボクは　おもうことが　あって\nしばらく　しゅぎょうを　つづける\lとうぶん　いえに　かえらない\pそこで　おねがいだ\pつくえの　うえにある\nモンスターボールを　うけとって　ほしい\pなかに　いるのは　ダンバルといって\nボクの　おきにいりの　ポケモンだから\pよろしく　たのむよ\pでは　また　いつか　あおう！\n　　　　　　ツワブキ　ダイゴより$`

原英文（`data/maps/MossdeepCity_StevensHouse/scripts.inc`，`fe570a7e5^`）：

`It's a letter.\p… … … … … …\pTo {PLAYER}{KUN}…\pI've decided to do a little soul-\nsearching and train on the road.\pI don't plan to return home for some\ntime.\pI have a favor to ask of you.\pI want you to take the POKé BALL on\nthe desk.\pInside it is a BELDUM, my favorite\nPOKéMON.\pI'm counting on you.\pMay our paths cross someday.\pSTEVEN STONE$`

当前美版（`data/maps/MossdeepCity_StevensHouse/scripts.inc`）：

`是一封信。\p…… …… ……\p致{PLAYER}{KUN}……\p我已决定踏上自我\n探索与修行之旅。\p短时间内不\n打算回家，\p我想拜托你收下\n桌上的精灵球，\p里面是我最喜欢的宝可梦——\n铁哑铃，\p拜托你照顾好它。\p愿你我终有相逢之日。\p大吾·兹伏奇$`

### 34 — gTVPokemonNewsBattleFrontierText05

结论：**已修复**。

对战巨蛋单打文本已删除重复在。

方案：不修改。

原建议：

- JP：バトルドーム\nシングル　バトルトーナメントに\lちょうせんした　{STR_VAR_1}さんが\l{STR_VAR_2}　れんぱで\lきろくを　こうしん　しました！\p⋯⋯{STR_VAR_1}さん！$
- EN：The TRAINER {STR_VAR_1} set a new\n{STR_VAR_2}-championship-streak record\lcompeting in the BATTLE DOME's\lSINGLE BATTLE
- 中文：训练家{STR_VAR_1}在\n在对战巨蛋单打对战锦标赛中\l创造了{STR_VAR_2}连冠的新纪录。\p让我们为{STR_VAR_1}欢呼！$
- 理由：JP“バトルドーム シングル バトルトーナメントに ちょうせんした”/EN“competing in the BATTLE DOME's SINGLE BATTLE Tournaments”，中文“训练家{STR_VAR_1}在 在对战巨蛋单打对战锦标赛中”出现“在 在”重复。
- 修改建议：训练家{STR_VAR_1}在对战巨蛋单打对战锦标赛中创造了{STR_VAR_2}连冠的新纪录。让我们为{STR_VAR_1}欢呼！

当前日版：

`训练家{FD_02}在\n对战巨蛋单打对战锦标赛中\l创造了{FD_03}连冠的新纪录。\p让我们为{FD_02}欢呼！`

文件：`patch/batches/386_tv_0.json`。

原日文（`0x082512C1`）：

`バトルド-ム\nシングル　バトルト-ナメントに\lちょうせんした　{PLACEHOLDER_02}さんが\l{PLACEHOLDER_03}　れんぱで\lきろくを　こうしん　しました!\p……{PLACEHOLDER_02}さん!`

Wokann日文（`data/text/tv/battle_frontier_news.inc`）：

`バトルドーム\nシングル　バトルトーナメントに\lちょうせんした　{STR_VAR_1}さんが\l{STR_VAR_2}　れんぱで\lきろくを　こうしん　しました！\p⋯⋯{STR_VAR_1}さん！$`

原英文（`data/text/tv.inc`，`fe570a7e5^`）：

`The TRAINER {STR_VAR_1} set a new\n{STR_VAR_2}-championship-streak record\lcompeting in the BATTLE DOME's\lSINGLE BATTLE Tournaments.\pHere's to {STR_VAR_1}!$`

当前美版（`data/text/tv.inc`）：

`训练家{STR_VAR_1}在\n对战巨蛋单打对战锦标赛中\l创造了{STR_VAR_2}连冠的新纪录。\p让我们为{STR_VAR_1}欢呼！$`

### 35 — gTVPokemonNewsBattleFrontierText06

结论：**已修复**。

对战巨蛋双打文本已删除重复在。

方案：不修改。

原建议：

- JP：バトルドーム\nダブル　バトルトーナメントに\lちょうせんした　{STR_VAR_1}さんが\l{STR_VAR_2}　れんぱで\lきろくを　こうしん　しました！\p⋯⋯{STR_VAR_1}さん！$
- EN：The TRAINER {STR_VAR_1} set a new\n{STR_VAR_2}-championship-streak record\lcompeting in the BATTLE DOME's\lDOUBLE BATTLE
- 中文：训练家{STR_VAR_1}在\n在对战巨蛋双打对战锦标赛中\l创造了{STR_VAR_2}连冠的新纪录。\p让我们为{STR_VAR_1}欢呼！$
- 理由：同[120]，“训练家{STR_VAR_1}在 在对战巨蛋双打对战锦标赛中”出现“在 在”重复。
- 修改建议：训练家{STR_VAR_1}在对战巨蛋双打对战锦标赛中创造了{STR_VAR_2}连冠的新纪录。让我们为{STR_VAR_1}欢呼！

当前日版：

`训练家{FD_02}在\n对战巨蛋双打对战锦标赛中\l创造了{FD_03}连冠的新纪录。\p让我们为{FD_02}欢呼！`

文件：`patch/batches/386_tv_0.json`。

原日文（`0x08251306`）：

`バトルド-ム\nダブル　バトルト-ナメントに\lちょうせんした　{PLACEHOLDER_02}さんが\l{PLACEHOLDER_03}　れんぱで\lきろくを　こうしん　しました!\p……{PLACEHOLDER_02}さん!`

Wokann日文（`data/text/tv/battle_frontier_news.inc`）：

`バトルドーム\nダブル　バトルトーナメントに\lちょうせんした　{STR_VAR_1}さんが\l{STR_VAR_2}　れんぱで\lきろくを　こうしん　しました！\p⋯⋯{STR_VAR_1}さん！$`

原英文（`data/text/tv.inc`，`fe570a7e5^`）：

`The TRAINER {STR_VAR_1} set a new\n{STR_VAR_2}-championship-streak record\lcompeting in the BATTLE DOME's\lDOUBLE BATTLE Tournaments.\pHere's to {STR_VAR_1}!$`

当前美版（`data/text/tv.inc`）：

`训练家{STR_VAR_1}在\n对战巨蛋双打对战锦标赛中\l创造了{STR_VAR_2}连冠的新纪录。\p让我们为{STR_VAR_1}欢呼！$`

### 36 — gTVPokemonNewsBattleFrontierText11

结论：**需修复**。

两个“在”重复，当前仍存在。

方案：删除第二行开头多余的“在”，保留其余文字与变量。

原建议：

- JP：バトルパレス\nシングル　バトルホールに\lちょうせんした　{STR_VAR_1}さんが\l{STR_VAR_2}　れんしょうで\lきろくを　こうしん　しました！\p⋯⋯{STR_VAR_1}さん！$
- EN：The TRAINER {STR_VAR_1} set a new\n{STR_VAR_2}-win-streak record while on\lthe BATTLE PALACE's SINGLE BATTLE\lHALL chall
- 中文：训练家{STR_VAR_1}在\n在对战宫殿单打对战厅中\l创造了{STR_VAR_2}连胜的新纪录。\p让我们为{STR_VAR_1}欢呼！$
- 理由：JP“バトルパレス シングル バトルホールに ちょうせんした”/EN“on the BATTLE PALACE's SINGLE BATTLE HALL challenge”，中文“训练家{STR_VAR_1}在 在对战宫殿单打对战厅中”出现“在 在”重复。
- 修改建议：训练家{STR_VAR_1}在对战宫殿单打对战厅中创造了{STR_VAR_2}连胜的新纪录。让我们为{STR_VAR_1}欢呼！

当前日版：

`训练家{FD_02}在\n在对战宫殿单打对战厅中\l创造了{FD_03}连胜的新纪录。\p让我们为{FD_02}欢呼！`

文件：`patch/batches/386_tv_0.json`。

原日文（`0x0825145F`）：

`バトルパレス\nシングル　バトルホ-ルに\lちょうせんした　{PLACEHOLDER_02}さんが\l{PLACEHOLDER_03}　れんしょうで\lきろくを　こうしん　しました!\p……{PLACEHOLDER_02}さん!`

Wokann日文（`data/text/tv/battle_frontier_news.inc`）：

`バトルパレス\nシングル　バトルホールに\lちょうせんした　{STR_VAR_1}さんが\l{STR_VAR_2}　れんしょうで\lきろくを　こうしん　しました！\p⋯⋯{STR_VAR_1}さん！$`

原英文（`data/text/tv.inc`，`fe570a7e5^`）：

`The TRAINER {STR_VAR_1} set a new\n{STR_VAR_2}-win-streak record while on\lthe BATTLE PALACE's SINGLE BATTLE\lHALL challenge.\pHere's to {STR_VAR_1}!$`

当前美版（`data/text/tv.inc`）：

`训练家{STR_VAR_1}在\n在对战宫殿单打对战厅中\l创造了{STR_VAR_2}连胜的新纪录。\p让我们为{STR_VAR_1}欢呼！$`

### 37 — gTVPokemonNewsBattleFrontierText12

结论：**需修复**。

两个“在”重复，当前仍存在。

方案：删除第二行开头多余的“在”。

原建议：

- JP：バトルパレス\nダブル　バトルホールに\lちょうせんした　{STR_VAR_1}さんが\l{STR_VAR_2}　れんしょうで\lきろくを　こうしん　しました！\p⋯⋯{STR_VAR_1}さん！$
- EN：The TRAINER {STR_VAR_1} set a new\n{STR_VAR_2}-win-streak record while on\lthe BATTLE PALACE's DOUBLE BATTLE\lHALL chall
- 中文：训练家{STR_VAR_1}在\n在对战宫殿双打对战厅中\l创造了{STR_VAR_2}连胜的新纪录。\p让我们为{STR_VAR_1}欢呼！$
- 理由：同[126]，“训练家{STR_VAR_1}在 在对战宫殿双打对战厅中”出现“在 在”重复。
- 修改建议：训练家{STR_VAR_1}在对战宫殿双打对战厅中创造了{STR_VAR_2}连胜的新纪录。让我们为{STR_VAR_1}欢呼！

### 数字范围错误（2 条）

当前日版：

`训练家{FD_02}在\n在对战宫殿双打对战厅中\l创造了{FD_03}连胜的新纪录。\p让我们为{FD_02}欢呼！`

文件：`patch/batches/386_tv_0.json`。

原日文（`0x082514A3`）：

`バトルパレス\nダブル　バトルホ-ルに\lちょうせんした　{PLACEHOLDER_02}さんが\l{PLACEHOLDER_03}　れんしょうで\lきろくを　こうしん　しました!\p……{PLACEHOLDER_02}さん!`

Wokann日文（`data/text/tv/battle_frontier_news.inc`）：

`バトルパレス\nダブル　バトルホールに\lちょうせんした　{STR_VAR_1}さんが\l{STR_VAR_2}　れんしょうで\lきろくを　こうしん　しました！\p⋯⋯{STR_VAR_1}さん！$`

原英文（`data/text/tv.inc`，`fe570a7e5^`）：

`The TRAINER {STR_VAR_1} set a new\n{STR_VAR_2}-win-streak record while on\lthe BATTLE PALACE's DOUBLE BATTLE\lHALL challenge.\pHere's to {STR_VAR_1}!$`

当前美版（`data/text/tv.inc`）：

`训练家{STR_VAR_1}在\n在对战宫殿双打对战厅中\l创造了{STR_VAR_2}连胜的新纪录。\p让我们为{STR_VAR_1}欢呼！$`

### 38 — BattleFrontier_ReceptionGate_Text_Level50Info

结论：**已修复**。

现在明确不会低于50级。

方案：不修改。

原建议：

- JP：レベル50の　コースでは　なまえの　とおり\nレベル50までの　ポケモンを\lちょうせん　させることが　できます\pただし　レベル50より　ひくい　レベルの\nポケモンを　つれた　トレーナーが\lとうじょう　することは　ありません\lくれぐ
- EN：The Level 50 course is open to POKéMON\nup to and including Level 50.\pPlease keep in mind, however, that\nno TRAINER yo
- 中文：Lv. 50级允许等级50级以内的\n宝可梦参加。\p但是，您遇到的训练家不会\n使用等级50以内的宝可梦。\p这是对战开拓区的\n入门级对战，\p我们建议您从这个模式\n开始挑战。$
- 理由：JP「レベル50より ひくい レベルの ポケモンを つれた トレーナーが とうじょう することは ありません」与EN「no TRAINER you face will have any POKéMON below Level 50」均指对手宝可梦不低于50级（实为50级）；补丁中文「不会使用等级50以内的宝可梦」将「低于50级」误作「50级以内」，按中文惯例含50级本身，反而排除了50级，与原文矛盾。
- 修改建议：Lv. 50级允许等级50级以内的\n宝可梦参加。\p但是，您遇到的训练家不会\n使用低于50级的宝可梦。\p这是对战开拓区的\n入门级对战，\p我们建议您从这个模式\n开始挑战。$

当前日版：

`Lv. 50级允许等级50级以内的\n宝可梦参加。\p但是，您遇到的训练家不会\n使用低于50级的宝可梦。\p这是对战开拓区的\n入门级对战，\p我们建议您从这个模式\n开始挑战。`

文件：`patch/batches/230_battle_frontier_reception_gate.json`。

原日文（`0x0823ABB0`）：

`レベル50の　コ-スでは　なまえの　とおり\nレベル50までの　ポケモンを\lちょうせん　させることが　できます\pただし　レベル50より　ひくい　レベルの\nポケモンを　つれた　トレ-ナ-が\lとうじょう　することは　ありません\lくれぐれも　ごちゅうい　ください\pなお　このコ-スが　バトルフロンティアの\nたたかいの　きほんと　なって　いますので\lぜひ　チャレンジして　みてください`

Wokann日文（`data/maps/BattleFrontier_ReceptionGate/scripts.inc`）：

`レベル50の　コースでは　なまえの　とおり\nレベル50までの　ポケモンを\lちょうせん　させることが　できます\pただし　レベル50より　ひくい　レベルの\nポケモンを　つれた　トレーナーが\lとうじょう　することは　ありません\lくれぐれも　ごちゅうい　ください\pなお　このコースが　バトルフロンティアの\nたたかいの　きほんと　なって　いますので\lぜひ　チャレンジして　みてください$`

原英文（`data/maps/BattleFrontier_ReceptionGate/scripts.inc`，`fe570a7e5^`）：

`The Level 50 course is open to POKéMON\nup to and including Level 50.\pPlease keep in mind, however, that\nno TRAINER you face will have any\lPOKéMON below Level 50.\pThis course is the entry level for\nbattles at the BATTLE FRONTIER.\pTo begin, we hope you will challenge\nthis course.$`

当前美版（`data/maps/BattleFrontier_ReceptionGate/scripts.inc`）：

`Lv. 50级允许等级50级以内的\n宝可梦参加。\p但是，您遇到的训练家不会\n使用低于50级的宝可梦。\p这是对战开拓区的\n入门级对战，\p我们建议您从这个模式\n开始挑战。$`

### 39 — BattleFrontier_ReceptionGate_Text_OpenLevelInfo

结论：**已修复**。

现在明确不会低于60级。

方案：不修改。

原建议：

- JP：オープンレベルの　コースでは\nちょうせんに　さんかする　ポケモンの\lレベルに　せいげんが　ありません\pあなたの　ポケモンの　レベルに　あわせて\nたいせんする　トレーナーの　ポケモンの\lレベルが　かわります\pただし　レベル60より
- EN：The Open Level course places no limit\non the levels of POKéMON entering\lchallenges.\pThe levels of your opponents will
- 中文：自由等级对于参加的宝可梦\n没有等级限制。\p对手的宝可梦等级会根据\n您的宝可梦等级进行调整。\p但是，您遇到的训练家不会\n使用等级60以内的宝可梦。$
- 理由：JP「レベル60より ひくい レベルの ポケモンを つれた トレーナーが とうじょう することは ありません」与EN「no TRAINER you face will have any POKéMON below Level 60」均指对手宝可梦不低于60级；补丁中文「不会使用等级60以内的宝可梦」将「低于60级」误作「60级以内」，按中文惯例含60级本身，与原文矛盾。
- 修改建议：自由等级对于参加的宝可梦\n没有等级限制。\p对手的宝可梦等级会根据\n您的宝可梦等级进行调整。\p但是，您遇到的训练家不会\n使用低于60级的宝可梦。$

### 内容遗漏（2 条）

当前日版：

`自由等级对于参加的宝可梦\n没有等级限制。\p对手的宝可梦等级会根据\n您的宝可梦等级进行调整。\p但是，您遇到的训练家不会\n使用低于60级的宝可梦。`

文件：`patch/batches/230_battle_frontier_reception_gate.json`。

原日文（`0x0823AC6C`）：

`オ-プンレベルの　コ-スでは\nちょうせんに　さんかする　ポケモンの\lレベルに　せいげんが　ありません\pあなたの　ポケモンの　レベルに　あわせて\nたいせんする　トレ-ナ-の　ポケモンの\lレベルが　かわります\pただし　レベル60より　ひくい　レベルの\nポケモンを　つれた　トレ-ナ-が\lとうじょう　することは　ありません`

Wokann日文（`data/maps/BattleFrontier_ReceptionGate/scripts.inc`）：

`オープンレベルの　コースでは\nちょうせんに　さんかする　ポケモンの\lレベルに　せいげんが　ありません\pあなたの　ポケモンの　レベルに　あわせて\nたいせんする　トレーナーの　ポケモンの\lレベルが　かわります\pただし　レベル60より　ひくい　レベルの\nポケモンを　つれた　トレーナーが\lとうじょう　することは　ありません$`

原英文（`data/maps/BattleFrontier_ReceptionGate/scripts.inc`，`fe570a7e5^`）：

`The Open Level course places no limit\non the levels of POKéMON entering\lchallenges.\pThe levels of your opponents will\nbe adjusted to match the levels of\lyour POKéMON.\pHowever, no TRAINER you face will\nhave any POKéMON below Level 60.$`

当前美版（`data/maps/BattleFrontier_ReceptionGate/scripts.inc`）：

`自由等级对于参加的宝可梦\n没有等级限制。\p对手的宝可梦等级会根据\n您的宝可梦等级进行调整。\p但是，您遇到的训练家不会\n使用低于60级的宝可梦。$`

### 40 — CableClub_Text_ExplainWirelessClub

结论：**需修复**。

非首次说明的完整日英原文均有找不到朋友时靠近的提示，当前遗漏。

方案：在适配器未连接的说明之前补“如果在联盟交谊厅或直接连接室\n找不到朋友，\p请试着靠近朋友一些。”；不要顺手向首次说明复制此段。

原建议：

- JP：ポケモン　ワイヤレス　クラブでの\nあそびかたを　せつめい　します！\pこちら　2かいには\nふたつの　おへやが　ございます\pひとつめは　ひだりがわの　おへや\nユニオン　ルーム！\pあなたの　ちかくで\nユニオン　ルームに　はいっている
- EN：Let me explain how the POKéMON\nWIRELESS CLUB works.\pOn this, the top floor, there are\ntwo rooms.\pFirst, the room on
- 中文：让我给您介绍一下\n无线俱乐部吧。\p在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接
- 理由：JP「もし ユニオン ルームや ダイレクト コーナーで おともだちが みつからない ときは もうすこし おともだちと ちかづいて みて ください(若在联盟交谊厅或直接连接室找不到朋友，请靠近朋友一些)」与EN「In that case, please move closer to your friends」整段在补丁中文中被遗漏，补丁中文从「交换或对战」直接跳到「如果无线适配器没有连接」，缺失一段提示。
- 修改建议：让我给您介绍一下\n无线俱乐部吧。\p在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果在联盟交谊厅或直接连接室\n找不到朋友的话，\p请试着靠近朋友一些。\p如果无线适配器没有连接，\n您仍然可

当前日版：

`让我给您介绍一下\n无线俱乐部吧。\p在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果无线适配器没有连接，\n您仍然可以使用GBA连接线进行连接。\p这种情况下，\n您就需要进入直接连接室。\p希望您能享受无线连接系统\n的乐趣。`

文件：`patch/batches/359_cable_club.json`。

原日文（`0x08248951`）：

`ポケモン　ワイヤレス　クラブでの\nあそびかたを　せつめい　します!\pこちら　2かいには\nふたつの　おへやが　ございます\pひとつめは　ひだりがわの　おへや\nユニオン　ル-ム!\pあなたの　ちかくで\nユニオン　ル-ムに　はいっている\lみしらぬ　おともだちと\lいろいろな　コミュニケ-ションが\lたのしめます!\pふたつめは　みぎがわの　おへや\nダイレクト　コ-ナ-!\pあなたの　しっている　おともだちと\nポケモンの　こうかんや\lたいせん　などを\lたのしむ　ことが　できます!\pもし　ユニオン　ル-ムや\nダイレクト　コ-ナ-で\lおともだちが　みつからない　ときは\pもうすこし　おともだちと\nちかづいて　みて　ください\pまた　ワイヤレスアダプタが\nつながって　いない　ばあいでも\pみぎがわの　おへやで\nケ-ブル　つうしんが　たのしめます\pそれでは\pワイヤレス　つうしんを\nたのしんで　くださいね!`

Wokann日文（`data/text/cable_club.inc`）：

`ポケモン　ワイヤレス　クラブでの\nあそびかたを　せつめい　します！\pこちら　2かいには\nふたつの　おへやが　ございます\pひとつめは　ひだりがわの　おへや\nユニオン　ルーム！\pあなたの　ちかくで\nユニオン　ルームに　はいっている\lみしらぬ　おともだちと\lいろいろな　コミュニケーションが\lたのしめます！\pふたつめは　みぎがわの　おへや\nダイレクト　コーナー！\pあなたの　しっている　おともだちと\nポケモンの　こうかんや\lたいせん　などを\lたのしむ　ことが　できます！\pもし　ユニオン　ルームや\nダイレクト　コーナーで\lおともだちが　みつからない　ときは\pもうすこし　おともだちと\nちかづいて　みて　ください\pまた　ワイヤレスアダプタが\nつながって　いない　ばあいでも\pみぎがわの　おへやで\nケーブル　つうしんが　たのしめます\pそれでは\pワイヤレス　つうしんを\nたのしんで　くださいね！$`

原英文（`data/text/cable_club.inc`，`fe570a7e5^`）：

`Let me explain how the POKéMON\nWIRELESS CLUB works.\pOn this, the top floor, there are\ntwo rooms.\pFirst, the room on the left.\nIt's the UNION ROOM.\pYou may link up with TRAINERS\naround you who have also entered\lthe UNION ROOM.\pWith them, you may do things like\nchat, battle, and trade.\pSecond, the room on the right is\nthe DIRECT CORNER.\pYou may trade or battle POKéMON\nwith your friends in this room.\pSometimes, you may not be able to\nfind your friends in the UNION ROOM\lor the DIRECT CORNER.\pIn that case, please move closer\nto your friends.\pIf the Wireless Adapter isn't\nconnected, you may still link up\lusing a GBA Game Link cable.\pIf that is the case, you must go\nto the DIRECT CORNER.\pI hope you enjoy the Wireless \nCommunication System.$`

当前美版（`data/text/cable_club.inc`）：

`让我给您介绍一下\n无线俱乐部吧。\p在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果无线适配器没有连接，\n您仍然可以使用GBA连接线进行连接。\p这种情况下，\n您就需要进入直接连接室。\p希望您能享受无线连接系统\n的乐趣。$`

### 41 — CableClub_Text_ExplainWirelessClubFirstTime

结论：**报告错误**。

首次说明的实际日英全文都没有“靠近朋友”这段。不得从非首次说明补入。

方案：不修改。

原建议：

- JP：こちら　2かいには\nふたつの　おへやが　ございます\pひとつめは　ひだりがわの　おへや\nユニオン　ルーム！\pあなたの　ちかくで\nユニオン　ルームに　はいっている\lみしらぬ　おともだちと\lいろいろな　コミュニケーションが\lたのし
- EN：On the top floor, there are two\nrooms.\pFirst, the room on the left.\nIt's the UNION ROOM.\pYou may link up with TRAINE
- 中文：在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或
- 理由：与[661]同一说明文本的另一版本：JP「もし ユニオン ルームや ダイレクト コーナーで おともだちが みつからない ときは もうすこし おともだちと ちかづいて みて ください」与EN「please move closer to your friends」整段在补丁中文中同样被遗漏。
- 修改建议：在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果在联盟交谊厅或直接连接室\n找不到朋友的话，\p请试着靠近朋友一些。\p如果无线适配器没有连接，\n您仍然可以使用GBA连接线进行连接。\p这种情

### 数字错误（单位换算）（2 条）

当前日版：

`在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果无线适配器没有连接，\n您仍然可以使用GBA连接线进行连接。\p这种情况下，\n您就需要进入直接连接室。\p希望您能享受无线连接系统\n的乐趣。`

文件：`patch/batches/359_cable_club.json`。

原日文（`0x082487F6`）：

`こちら　2かいには\nふたつの　おへやが　ございます\pひとつめは　ひだりがわの　おへや\nユニオン　ル-ム!\pあなたの　ちかくで\nユニオン　ル-ムに　はいっている\lみしらぬ　おともだちと\lいろいろな　コミュニケ-ションが\lたのしめます!\pふたつめは　みぎがわの　おへや\nダイレクト　コ-ナ-!\pあなたの　しっている　おともだちと\nポケモンの　こうかんや\lたいせん　などを\lたのしむ　ことが　できます!\pもし　ワイヤレスアダプタが\nつながって　いない　ばあいでも\pみぎがわの　おへやで\nケ-ブル　つうしんが　たのしめます\pそれでは\pワイヤレス　つうしんを\nたのしんで　くださいね!`

Wokann日文（`data/text/cable_club.inc`）：

`こちら　2かいには\nふたつの　おへやが　ございます\pひとつめは　ひだりがわの　おへや\nユニオン　ルーム！\pあなたの　ちかくで\nユニオン　ルームに　はいっている\lみしらぬ　おともだちと\lいろいろな　コミュニケーションが\lたのしめます！\pふたつめは　みぎがわの　おへや\nダイレクト　コーナー！\pあなたの　しっている　おともだちと\nポケモンの　こうかんや\lたいせん　などを\lたのしむ　ことが　できます！\pもし　ワイヤレスアダプタが\nつながって　いない　ばあいでも\pみぎがわの　おへやで\nケーブル　つうしんが　たのしめます\pそれでは\pワイヤレス　つうしんを\nたのしんで　くださいね！$`

原英文（`data/text/cable_club.inc`，`fe570a7e5^`）：

`On the top floor, there are two\nrooms.\pFirst, the room on the left.\nIt's the UNION ROOM.\pYou may link up with TRAINERS\naround you who have also entered\lthe UNION ROOM.\pWith them, you may do things like\nchat, battle, and trade.\pSecond, the room on the right is\nthe DIRECT CORNER.\pYou may trade or battle POKéMON\nwith your friends in this room.\pIf the Wireless Adapter isn't\nconnected, you may still link up\lusing a GBA Game Link cable.\pIf that is the case, you must go\nto the DIRECT CORNER.\pI hope you enjoy the Wireless \nCommunication System.$`

当前美版（`data/text/cable_club.inc`）：

`在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果无线适配器没有连接，\n您仍然可以使用GBA连接线进行连接。\p这种情况下，\n您就需要进入直接连接室。\p希望您能享受无线连接系统\n的乐趣。$`

### 42 — LavaridgeTown_Gym_1F_Text_GeraldIntro

结论：**需修复**。

日文200度与英文392度是摄氏/华氏区域换算，不是同一数字。“392度”没有单位会误导。

方案：日版200℃；美版392℉。不因现实岩浆温度去修改原作数字。

原建议：

- JP：おまえの　ポケモン
200どの　あつさに　たえられるかよ!?
- EN：Can your POKéMON withstand\n392-degree heat?$
- 中文：你的宝可梦能抵挡\n392度的高温吗？$
- 理由：JP「200どのあつさにたえられるか」为200摄氏度，EN“392-degree heat”为392华氏度（200°C=392°F），中文“392度的高温”直接沿用华氏度数值，在中文语境下会被理解为392摄氏度，与日文200度不符。
- 修改建议：你的宝可梦能抵挡\n200度的高温吗？

当前日版：

`你的宝可梦能抵挡\n392度的高温吗？`

文件：`patch/batches/079_lavaridgetown_gym_1f.json`。

原日文（`0x081F4780`）：

`おまえの　ポケモン\n200どの　あつさに　たえられるかよ!?`

Wokann日文（`data/maps/LavaridgeTown_Gym_1F/scripts.inc`）：

`おまえの　ポケモン\n200どの　あつさに　たえられるかよ！？$`

原英文（`data/maps/LavaridgeTown_Gym_1F/scripts.inc`，`fe570a7e5^`）：

`Can your POKéMON withstand\n392-degree heat?$`

当前美版（`data/maps/LavaridgeTown_Gym_1F/scripts.inc`）：

`你的宝可梦能抵挡\n392度的高温吗？$`

### 43 — LavaridgeTown_Gym_1F_Text_GeraldPostBattle

结论：**需修复**。

同上一条，原作设定数值是200℃ / 392℉。

方案：日版温度200℃，美版392℉；保留后续击败我所以能承受的夸张说法。

原建议：

- JP：200どの　あつさ　ってのは
ようがんの　おんど!\pおまえの　ポケモン　おれに　かてたんだから
ようがんの　なかでも　へいき　だろうな!
- EN：The temperature of magma is\n392 degrees.\pYour POKéMON beat me, so they should\neasily survive in magma.$
- 中文：岩浆的温度\n是392度。\p你的宝可梦打败了我，那么在岩浆中\n也应该能比较容易生存下来。$
- 理由：JP「200どのあつさってのはようがんのおんど」为200摄氏度，EN“The temperature of magma is 392 degrees”为392华氏度（=200°C），中文“岩浆的温度是392度”沿用华氏度数值，中文读者会理解为392摄氏度，与日文200度不符。
- 修改建议：岩浆的温度\n是200度。\p你的宝可梦打败了我，那么在岩浆中\n也应该能比较容易生存下来。

### 误译（2 条）

当前日版：

`岩浆的温度\n是392度。\p你的宝可梦打败了我，那么在岩浆中\n也应该能比较容易生存下来。`

文件：`patch/batches/079_lavaridgetown_gym_1f.json`。

原日文（`0x081F47AF`）：

`200どの　あつさ　ってのは\nようがんの　おんど!\pおまえの　ポケモン　おれに　かてたんだから\nようがんの　なかでも　へいき　だろうな!`

Wokann日文（`data/maps/LavaridgeTown_Gym_1F/scripts.inc`）：

`200どの　あつさ　ってのは\nようがんの　おんど！\pおまえの　ポケモン　おれに　かてたんだから\nようがんの　なかでも　へいき　だろうな！$`

原英文（`data/maps/LavaridgeTown_Gym_1F/scripts.inc`，`fe570a7e5^`）：

`The temperature of magma is\n392 degrees.\pYour POKéMON beat me, so they should\neasily survive in magma.$`

当前美版（`data/maps/LavaridgeTown_Gym_1F/scripts.inc`）：

`岩浆的温度\n是392度。\p你的宝可梦打败了我，那么在岩浆中\n也应该能比较容易生存下来。$`

### 44 — gText_BecameMoreConsciousOfOtherMons

结论：**需修复**。

conscious / きになる 是更加在意，不是担心。

方案：“更加担心其他宝可梦”改为“更加在意其他宝可梦”，四个 PAUSE 15 不变。

原建议：

- JP：ほかの　ポケモンが　いつもより\nきに　なって　きた！{PAUSE 0x0F}{PAUSE 0x0F}{PAUSE 0x0F}{PAUSE 0x0F}$
- EN：It became more conscious\nof the other POKéMON.{PAUSE 15}{PAUSE 15}{PAUSE 15}{PAUSE 15}$
- 中文：它变得比平时\n更加担心其他宝可梦了！{PAUSE_15}{PAUSE_15}{PAUSE_15}{PAUSE_15}$
- 理由：JP“ほかの ポケモンが いつもより きに なって きた！”/EN“It became more conscious of the other POKéMON.”——“きになる”此处意为“在意/留意”，中文译成“更加担心其他宝可梦”加入了“担忧”含义；且姊妹文本[677]“变得不那么关注”[679]“完全不关注”均用“关注”，本条用词不一致。
- 修改建议：它变得比平时更加在意其他宝可梦了！

当前日版：

`它变得比平时\n更加担心其他宝可梦了！{FC_08 0f}{FC_08 0f}{FC_08 0f}{FC_08 0f}`

文件：`patch/batches/405_contest_strings.json`。

原日文（`0x0824B70C`）：

`ほかの　ポケモンが　いつもより\nきに　なって　きた!{BYTE_FC}くそ{BYTE_FC}くそ{BYTE_FC}くそ{BYTE_FC}くそ`

Wokann日文（`data/text/contest_strings.inc`）：

`ほかの　ポケモンが　いつもより\nきに　なって　きた！{PAUSE 0x0F}{PAUSE 0x0F}{PAUSE 0x0F}{PAUSE 0x0F}$`

原英文（`data/text/contest_strings.inc`，`fe570a7e5^`）：

`It became more conscious\nof the other POKéMON.{PAUSE 15}{PAUSE 15}{PAUSE 15}{PAUSE 15}$`

当前美版（`data/text/contest_strings.inc`）：

`它变得比平时\n更加担心其他宝可梦了！{PAUSE 15}{PAUSE 15}{PAUSE 15}{PAUSE 15}$`

### 45 — gText_Contest_Shyness

结论：**已修复**。

当前已为扭扭捏捏。

方案：不修改。

原建议：

- JP：モジモジ$
- EN：shyness$
- 中文：扑通扑通$
- 理由：JP“モジモジ”/EN“shyness”（华丽大赛害羞状态，扭捏不安貌），中文译成“扑通扑通”——“扑通扑通”是心跳声，对应的是ドキドキ，与モジモジ的“扭捏”语义不符（[841]ドキドキ/anxiety已另译“慌慌张张”，此处系拟声词错配）。
- 修改建议：扭扭捏捏

### 跨世代机制污染（2 条）

当前日版：

`扭扭捏捏`

文件：`patch/batches/405_contest_strings.json`。

原日文（`0x0824C0D2`）：

`モジモジ`

Wokann日文（`data/text/contest_strings.inc`）：

`モジモジ$`

原英文（`data/text/contest_strings.inc`，`fe570a7e5^`）：

`shyness$`

当前美版（`data/text/contest_strings.inc`）：

`扭扭捏捏$`

### 46 — [127]

结论：**需修复**。

第三世代攀瀑是 EFFECT_HIT，secondaryEffectChance=0，没有招式自带畏缩效果。不能混入第四世代效果。

方案：以惊人的气势扑向对手。；删除畏缩句；字体和换行根据现有描述框重新排，不改招式参数。

原建议：

- JP：たきを　さかのぼるような　いきおいで
てきに　とっしんする
- EN：Charges the foe with speed
to climb waterfalls.
- 中文：以惊人的气势扑向对手。
有时会使对手畏缩。
- 理由：JP「たきを さかのぼるような いきおいで てきに とっしんする」/EN「Charges the foe with speed to climb waterfalls.」均未提及畏缩；JP baserom 招式数据 WATERFALL effect=EFFECT_HIT, secondaryEffectChance=0，第三世代攀瀑无追加效果，20%畏缩是第四世代才加入的机制。
- 修改建议：删除「有时会使对手畏缩。」一句，改为：以惊人的气势扑向对手。

当前日版：

`以惊人的气势扑向对手。\n有时会使对手畏缩。`

文件：`patch/move_descriptions.json`。

原英文（`src/data/text/move_descriptions.h`，`fe570a7e5^`）：

`Charges the foe with speed\nto climb waterfalls.`

当前美版（`src/data/text/move_descriptions.h`）：

`以惊人的气势扑向对手。\n有时会使对手畏缩。`

### 47 — [329]

结论：**已修复**。

已删除后世代等级限制/命中细节。

方案：不修改。

原建议：

- JP：ぜったいれいどで　てきを　おそう
きまると　せんとうふのうになる
- EN：A chilling attack that
causes fainting if it hits.
- 中文：给对手一击昏厥。若冰属性
以外宝可梦使用会难以打中。
- 理由：JP「ぜったいれいどで てきを おそう きまると せんとうふのうになる」/EN「A chilling attack that causes fainting if it hits.」均未提及属性相关命中；第三世代绝对零度命中公式与使用者属性无关，「非冰属性使用难以打中/冰属性免疫」是第七世代起的机制（Bulbapedia: Gen VII onwards, Ice-type immune, non-Ice base 20%）。
- 修改建议：删除「若冰属性以外宝可梦使用会难以打中。」一句。

### 数值错误（2 条）

当前日版：

`以绝对零度攻击对手。\n命中后会使对手一击昏厥。`

文件：`patch/move_descriptions.json`。

原英文（`src/data/text/move_descriptions.h`，`fe570a7e5^`）：

`A chilling attack that\ncauses fainting if it hits.`

当前美版（`src/data/text/move_descriptions.h`）：

`以绝对零度攻击对手。\n命中后会使对手一击昏厥。`

### 48 — [180]

结论：**已修复**。

当前只说减少PP，已删除不符合本作的固定数值。

方案：不修改。

原建议：

- JP：あいてが　だした　わざを　うらんで
その　わざポイントを　へらしてしまう
- EN：Spitefully cuts the PP
of the foe's last move.
- 中文：怨恨对手最后用的招式，
减少4PP该招式。
- 理由：JP「わざポイントを へらしてしまう」/EN「Spitefully cuts the PP of the foe's last move.」未写固定数值；第三世代游戏代码 Cmd_tryspiteppreduce 中 ppToDeduct = (Random() & 3) + 2，即2～5随机扣除，固定扣4是第四世代起的机制。中文「减少4PP」与第三世代实际不符。
- 修改建议：改为：怨恨对手最后用的招式，减少该招式2～5点PP。

当前日版：

`怨恨对手最后用的招式，\n减少该招式的PP。`

文件：`patch/move_descriptions.json`。

原英文（`src/data/text/move_descriptions.h`，`fe570a7e5^`）：

`Spitefully cuts the PP\nof the foe's last move.`

当前美版（`src/data/text/move_descriptions.h`）：

`怨恨对手最后用的招式，\n减少该招式的PP。`

### 49 — [227]

结论：**已修复**。

当前明确2～6回合。

方案：不修改。

原建议：

- JP：てきが　さいごに　つかった　わざを
2ー6かい　れんぞくで　ださせる
- EN：Makes the foe repeat its
last move over 2 to 6 turns.
- 中文：让对手接受再来一次，
在3～6回合内重复最后的招式。
- 理由：JP「2ー6かい れんぞくで ださせる」/EN「Makes the foe repeat its last move over 2 to 6 turns.」均为2～6，中文写成「3～6回合」。
- 修改建议：改为：在2～6回合内重复最后的招式。

### 关键信息替换（2 条）

当前日版：

`让对手接受再来一次，\n在2～6回合内重复最后的招式。`

文件：`patch/move_descriptions.json`。

原英文（`src/data/text/move_descriptions.h`，`fe570a7e5^`）：

`Makes the foe repeat its\nlast move over 2 to 6 turns.`

当前美版（`src/data/text/move_descriptions.h`）：

`让对手接受再来一次，\n在2～6回合内重复最后的招式。`

### 50 — [276]

结论：**已修复**。

当前为红色光辉，非晶莹剔透。

方案：不修改。

原建议：

- JP：おおむかしの ちからが
こめられている という
あかく かがやく たま
- EN：A red, glowing orb
said to contain an
ancient power.
- 中文：散发着红色光辉的
宝珠。据说和丰缘
传说渊源颇深
- 理由：JP原文「おおむかしの ちからが こめられている」(据说蕴含着古老的力量）、EN"said to contain an ancient power"；中文改为"据说和丰缘传说渊源颇深"，删除了"蕴含古老力量"这一关键信息，替换为原文没有的传说关联。
- 修改建议：改为"散发着红色光辉的宝珠，据说其中蕴含着古老的力量"。

当前日版：

`散发着红色光辉的\n宝珠。据说蕴含着\n超古代的力量`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`おおむかしの　ちからが\nこめられている　という\nあかく　かがやく　たま`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A red, glowing orb\nsaid to contain an\nancient power.`

当前美版（`src/data/text/item_descriptions.h`）：

`散发着红色光辉的\n宝珠。据说蕴含着\n超古代的力量`

### 51 — [277]

结论：**已修复**。

当前为蓝色光辉，非晶莹剔透。

方案：不修改。

原建议：

- JP：おおむかしの ちからが
こめられている という
あおく かがやく たま
- EN：A blue, glowing orb
said to contain an
ancient power.
- 中文：散发着蓝色光辉的
宝珠。据说和丰缘
传说渊源颇深
- 理由：JP原文「おおむかしの ちからが こめられている」(据说蕴含着古老的力量）、EN"said to contain an ancient power"；中文改为"据说和丰缘传说渊源颇深"，删除了"蕴含古老力量"这一关键信息，替换为原文没有的传说关联。
- 修改建议：改为"散发着蓝色光辉的宝珠，据说其中蕴含着古老的力量"。

### 语义错误（1 条）

当前日版：

`散发着蓝色光辉的\n宝珠。据说蕴含着\n超古代的力量`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`おおむかしの　ちからが\nこめられている　という\nあおく　かがやく　たま`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A blue, glowing orb\nsaid to contain an\nancient power.`

当前美版（`src/data/text/item_descriptions.h`）：

`散发着蓝色光辉的\n宝珠。据说蕴含着\n超古代的力量`

### 52 — BattleFrontier_Lounge2_Text_AmazingPowersOfObservation

结论：**需修复**。

かんさつりょく / powers of observation 是观察力。センパイ是前辈，不应机械修成老师。

方案：好厉害的观察力！\n前辈果然非同一般！

原建议：

- JP：すっげえ　かんさつりょくー！！\nやっぱ　センパイは　ちがうっすわー$
- EN：What amazing powers of observation!\nMy mentor's like none other!$
- 中文：调查资料好厉害！\n老师果然非同一般！$
- 理由：JP「かんさつりょく」即「观察力」，EN「What amazing powers of observation!」亦为观察力；补丁中文「调查资料好厉害」将观察力误译为「调查资料」，与三方原文不符。
- 修改建议：观察力好厉害！\n老师果然非同一般！$

### 术语错误（1 条）

当前日版：

`调查资料好厉害！\n老师果然非同一般！`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x0823769E`）：

`すっげえ　かんさつりょく-!!\nやっぱ　センパイは　ちがうっすわ-`

Wokann日文（`data/maps/BattleFrontier_Lounge2/scripts.inc`）：

`すっげえ　かんさつりょくー！！\nやっぱ　センパイは　ちがうっすわー$`

原英文（`data/maps/BattleFrontier_Lounge2/scripts.inc`，`fe570a7e5^`）：

`What amazing powers of observation!\nMy mentor's like none other!$`

当前美版（`data/maps/BattleFrontier_Lounge2/scripts.inc`）：

`调查资料好厉害！\n老师果然非同一般！$`

### 53 — BattleFrontier_Lounge7_Text_RockSlideDesc

结论：**已修复**。

恐惧已改畏缩。

方案：不修改。

原建议：

- JP：いわで　こうげき\nてきを　ひるませる\nことが　ある$
- EN：Large boulders\nare hurled. May\ncause flinching.$
- 中文：投出巨大的石块，\n可以使对手\n恐惧。$
- 理由：JP「てきを ひるませる」即「使对手畏缩(flinch)」，EN「May cause flinching」亦为畏缩；补丁中文「可以使对手恐惧」将ひるむ/ flinch误作「恐惧」，且与同文件[121]王者之证描述「使对手畏缩」术语不一致。
- 修改建议：投出巨大的石块，\n可以使对手\n畏缩。$

### 招式名误译（1 条）

当前日版：

`投出巨大的石块，\n可以使对手\n畏缩。`

文件：`patch/batches/224_battle_frontier_lounge7.json`。

原日文（`0x0823A0BF`）：

`いわで　こうげき\nてきを　ひるませる\nことが　ある`

Wokann日文（`data/maps/BattleFrontier_Lounge7/scripts.inc`）：

`いわで　こうげき\nてきを　ひるませる\nことが　ある$`

原英文（`data/maps/BattleFrontier_Lounge7/scripts.inc`，`fe570a7e5^`）：

`Large boulders\nare hurled. May\ncause flinching.$`

当前美版（`data/maps/BattleFrontier_Lounge7/scripts.inc`）：

`投出巨大的石块，\n可以使对手\n畏缩。$`

### 54 — LilycoveCity_ContestHall_Text_SuchCharmingCuteAppeals

结论：**需修复**。

みずあそび / WATER SPORT 是招式玩水；“水之游”不是该招式名。

方案：仅将“水之游”改为“玩水”，其他评委感叹及表演措辞保留。

原建议：

- JP：しんさいん“おお
みんな　かわいい　アピ-ルだなあ!\pおおっ　なんて　かわいい
みずあそびの　アピ-ルなんだろう!
- EN：JUDGE: Oh, such charming and cute\nappeals!\pOh, my goodness! What a perfectly\nadorable WATER SPORT appeal!$
- 中文：评委：啊，如此迷人，\n如此可爱！\p哎，天啊！那水之游\n多么完美，多么可爱！$
- 理由：JP「なんてかわいいみずあそびのアピールなんだろう」/EN“What an adorable WATER SPORT appeal”中的招式みずあそび（WATER SPORT）官方中文名为“玩水”，中文“那水之游多么完美”误作“水之游”，招式名错误。
- 修改建议：评委：啊，如此迷人，\n如此可爱！\p哎，天啊！那玩水\n多么完美，多么可爱！

### 衍字（1 条）

当前日版：

`评委：啊，如此迷人，\n如此可爱！\p哎，天啊！那水之游\n多么完美，多么可爱！`

文件：`patch/batches/125_lilycovecity_contesthall.json`。

原日文（`0x0820804C`）：

`しんさいん“おお\nみんな　かわいい　アピ-ルだなあ!\pおおっ　なんて　かわいい\nみずあそびの　アピ-ルなんだろう!`

Wokann日文（`data/maps/LilycoveCity_ContestHall/scripts.inc`）：

`しんさいん“おお\nみんな　かわいい　アピールだなあ！\pおおっ　なんて　かわいい\nみずあそびの　アピールなんだろう！$`

原英文（`data/maps/LilycoveCity_ContestHall/scripts.inc`，`fe570a7e5^`）：

`JUDGE: Oh, such charming and cute\nappeals!\pOh, my goodness! What a perfectly\nadorable WATER SPORT appeal!$`

当前美版（`data/maps/LilycoveCity_ContestHall/scripts.inc`）：

`评委：啊，如此迷人，\n如此可爱！\p哎，天啊！那水之游\n多么完美，多么可爱！$`

### 55 — LilycoveCity_CoveLilyMotel_1F_Text_HeardAquaHideoutBusted

结论：**需修复**。

有人到捣毁了，混入多余“到”。

方案：“有人到捣毁了”改为“有人捣毁了”。

原建议：

- JP：あ　ごめん　ごめん!
テレビに　むちゅう　だったもんで!\pそういえば　だれかが　アクアだんの
アジトを　かいめつ　させた　らしいね!\pおかげで　さっき　だんたいさん　からの
しゅくはく　よやくが　はいったよ!\pたしか……　ゲ-ムなんと
- EN：Oh, sorry, sorry!\nI was too involved in watching TV!\pI heard that someone busted\nthe TEAM AQUA HIDEOUT.\pThanks to th
- 中文：啊，抱歉，抱歉！\n我看电视看入迷了！\p我听说有人到捣毁了\n海洋队的基地，\p多亏如此，我们刚刚\n接到了一个大团体订房预约，\p是一个公司，叫做……呃……\n游戏什么的……$
- 理由：JP「だれかがアクアだんのアジトをかいめつさせたらしいね」/EN“someone busted the TEAM AQUA HIDEOUT”意为“有人捣毁了海洋队基地”，中文“我听说有人到捣毁了海洋队的基地”中“到”为衍字，文理不通，美版中文同样误写。
- 修改建议：啊，抱歉，抱歉！\n我看电视看入迷了！\p我听说有人捣毁了\n海洋队的基地，\p多亏如此，我们刚刚\n接到了一个大团体订房预约，\p是一个公司，叫做……呃……\n游戏什么的……

### 漏字（1 条）

当前日版：

`啊，抱歉，抱歉！\n我看电视看入迷了！\p我听说有人到捣毁了\n海洋队的基地，\p多亏如此，我们刚刚\n接到了一个大团体订房预约，\p是一个公司，叫做……呃……\n游戏什么的……`

文件：`patch/batches/127_lilycovecity_covelilymotel_1f.json`。

原日文（`0x0820571C`）：

`あ　ごめん　ごめん!\nテレビに　むちゅう　だったもんで!\pそういえば　だれかが　アクアだんの\nアジトを　かいめつ　させた　らしいね!\pおかげで　さっき　だんたいさん　からの\nしゅくはく　よやくが　はいったよ!\pたしか……　ゲ-ムなんとか　っていう\nかいしゃ　だったかな……`

Wokann日文（`data/maps/LilycoveCity_CoveLilyMotel_1F/scripts.inc`）：

`あ　ごめん　ごめん！\nテレビに　むちゅう　だったもんで！\pそういえば　だれかが　アクアだんの\nアジトを　かいめつ　させた　らしいね！\pおかげで　さっき　だんたいさん　からの\nしゅくはく　よやくが　はいったよ！\pたしか⋯⋯　ゲームなんとか　っていう\nかいしゃ　だったかな⋯⋯$`

原英文（`data/maps/LilycoveCity_CoveLilyMotel_1F/scripts.inc`，`fe570a7e5^`）：

`Oh, sorry, sorry!\nI was too involved in watching TV!\pI heard that someone busted\nthe TEAM AQUA HIDEOUT.\pThanks to that, we just booked\na reservation from a big group.\pIt was a company called… Uh…\nGAME something…$`

当前美版（`data/maps/LilycoveCity_CoveLilyMotel_1F/scripts.inc`）：

`啊，抱歉，抱歉！\n我看电视看入迷了！\p我听说有人到捣毁了\n海洋队的基地，\p多亏如此，我们刚刚\n接到了一个大团体订房预约，\p是一个公司，叫做……呃……\n游戏什么的……$`

### 56 — MauvilleCity_Text_UncleCanYouBattleWally

结论：**已修复**。

当前已为满充，不是满冲。

方案：不修改。

原建议：

- JP：おじさん“{PLAYER}{KUN}とやら\nわるいけど　ミツルくんと\lしょうぶ　してあげて　くれないかな？\pこのままだと　なにを　いっても\nきいて　もらえそうに　ないよ$
- EN：UNCLE: {PLAYER}{KUN}, was it?\nOn WALLY's behalf, can I ask you to\lbattle with him just this once?\pI don't think he's
- 中文：叔叔：你是{PLAYER}{KUN}吧？\n为了满充，\l能请你和来一场对战吗？\p我想他现在这样\n是没法听得进劝的。$
- 理由：JP「ミツルくんとしょうぶしてあげてくれないかな（能和满充对战一下吗）」/EN「can I ask you to battle with him just this once?」中对战对象明确，补丁/美版中文「能请你和来一场对战吗」的「和」后缺宾语（应为「和他」），句子不完整。
- 修改建议：能请你和他来一场对战吗？

### 术语误译（1 条）

当前日版：

`叔叔：你是{FD_01}{FD_05}吧？\n为了满充，\l能请你和满充来一场对战吗？\p我想他现在这样\n是没法听得进劝的。`

文件：`patch/batches/050_mauvillecity.json`。

原日文（`0x081DDFD3`）：

`おじさん“{PLACEHOLDER_01}{PLACEHOLDER_05}とやら\nわるいけど　ミツルくんと\lしょうぶ　してあげて　くれないかな?\pこのままだと　なにを　いっても\nきいて　もらえそうに　ないよ`

Wokann日文（`data/maps/MauvilleCity/scripts.inc`）：

`おじさん“{PLAYER}{KUN}とやら\nわるいけど　ミツルくんと\lしょうぶ　してあげて　くれないかな？\pこのままだと　なにを　いっても\nきいて　もらえそうに　ないよ$`

原英文（`data/maps/MauvilleCity/scripts.inc`，`fe570a7e5^`）：

`UNCLE: {PLAYER}{KUN}, was it?\nOn WALLY's behalf, can I ask you to\lbattle with him just this once?\pI don't think he's going to listen to\nany reason the way he is now.$`

当前美版（`data/maps/MauvilleCity/scripts.inc`）：

`叔叔：你是{PLAYER}{KUN}吧？\n为了满充，\l能请你和满充来一场对战吗？\p我想他现在这样\n是没法听得进劝的。$`

### 57 — MossdeepCity_GameCorner_1F_Text_DescribeWhichGame

结论：**需修复**。

游戏规则不是宝可梦对战规则。

方案：将“对战规则”改为“游戏规则”，按现有分页保留其他句子。

原建议：

- JP：ぼくは　ゲームの　せつめいを\nしますよ！\lどの　せつめいを　ききますか？$
- EN：I can explain game rules to you,\nif you'd like.\pWhich game should I describe?$
- 中文：需要的话，\n我可以向您解说对战规则。\p需要解说哪一项？$
- 理由：JP「ゲームのせつめいをしますよ（我来说明游戏规则）」/EN「I can explain game rules to you」中的「ゲーム（游戏）」指嘟嘟利摘树果、宝可梦跳绳等小游戏，补丁/美版中文误作「对战规则」，「游戏」误译为「对战」，术语错误。
- 修改建议：需要的话，我可以向您解说游戏规则。需要解说哪一项？

### 语义缺失（1 条）

当前日版：

`需要的话，\n我可以向您解说对战规则。\p需要解说哪一项？`

文件：`patch/batches/151_mossdeepcity_gamecorner_1f.json`。

原日文（`0x082481AB`）：

`ぼくは　ゲ-ムの　せつめいを\nしますよ!\lどの　せつめいを　ききますか?`

Wokann日文（`data/text/cable_club.inc`）：

`ぼくは　ゲームの　せつめいを\nしますよ！\lどの　せつめいを　ききますか？$`

原英文（`data/text/cable_club.inc`，`fe570a7e5^`）：

`I can explain game rules to you,\nif you'd like.\pWhich game should I describe?$`

当前美版（`data/text/cable_club.inc`）：

`需要的话，\n我可以向您解说对战规则。\p需要解说哪一项？$`

### 58 — gText_NoticesGoldCard

结论：**需修复**。

当前已恢复金卡/金色/四星，但未恢复金卡持有者的限定和两次玩家名。

方案：后半明确“拥有金卡的训练家”，恢复两处 PLAYER；日版使用 FD_01。

原建议：

- JP：そ　それは⋯⋯\nひょっとして　ゴールドカード！？\pああ⋯⋯　きんいろが　まぶしい！\n4つの　ほしが　かがやかしい！\pわたしも　これまでに\nシルバーカードの　トレーナーさんなら\lなんにんか　みてきましたが\lゴールドカードを　おも
- EN：Th-that card…\nCould it be… The GOLD CARD?!\pOh, the gold color is brilliant!\nThe four stars seem to sparkle!\pI've see
- 中文：那、那张卡！？\p那个颜色！！\n那星星的数量！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有比这更厉害的\n训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！$
- 理由：JP「ひょっとして ゴールドカード」「きんいろが まぶしい」「4つの ほしが かがやかしい」/EN「The GOLD CARD」「the gold color is brilliant」「The four stars seem to sparkle」中的关键名词（金卡/金色/四颗星星/闪耀）被补丁中文与美版中文一并丢弃（「那张卡」「那个颜色」「星星的数量」），关键语义缺失
- 修改建议：那、那张卡……\p难道是金卡！？\p啊……金色真是耀眼！\n四颗星星闪闪发光！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但拥有金卡的训练家，\l{PLAYER}您还是第一位！\p那么，请让我为{PLAYER}的\n宝可梦休息一下吧！$

### 语义反转/误译（1 条）

当前日版：

`那、那张卡！？\p难道是金卡！？\p金色真耀眼！！\n四颗星在闪耀！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有比这更厉害的\n训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！`

文件：`patch/batches/196_pokemon_centers.json`。

原日文（`0x08243814`）：

`そ　それは……\nひょっとして　ゴ-ルドカ-ド!?\pああ……　きんいろが　まぶしい!\n4つの　ほしが　かがやかしい!\pわたしも　これまでに\nシルバ-カ-ドの　トレ-ナ-さんなら\lなんにんか　みてきましたが\lゴ-ルドカ-ドを　おもちの　かたは\l{PLACEHOLDER_01}さんが　はじめて　ですよ!\pさあ　{PLACEHOLDER_01}さんの\nポケモンを　やすませて　あげましょう!`

Wokann日文（`data/text/pkmn_center_nurse.inc`）：

`そ　それは⋯⋯\nひょっとして　ゴールドカード！？\pああ⋯⋯　きんいろが　まぶしい！\n4つの　ほしが　かがやかしい！\pわたしも　これまでに\nシルバーカードの　トレーナーさんなら\lなんにんか　みてきましたが\lゴールドカードを　おもちの　かたは\l{PLAYER}さんが　はじめて　ですよ！\pさあ　{PLAYER}さんの\nポケモンを　やすませて　あげましょう！$`

原英文（`data/text/pkmn_center_nurse.inc`，`fe570a7e5^`）：

`Th-that card…\nCould it be… The GOLD CARD?!\pOh, the gold color is brilliant!\nThe four stars seem to sparkle!\pI've seen several TRAINERS with\na SILVER CARD before, but, {PLAYER},\lyou're the first TRAINER I've ever\lseen with a GOLD CARD!\pOkay, {PLAYER}, please allow me\nthe honor of resting your POKéMON!$`

当前美版（`data/text/pkmn_center_nurse.inc`）：

`那、那张卡！？\p难道是金卡！？\p金色真耀眼！！\n四颗星在闪耀！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有比这更厉害的\n训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！$`

### 59 — RustboroCity_DevonCorp_1F_Text_HowCouldWeGetRobbed

结论：**需修复**。

对已经被抢的事情自责，不能否认“谁会抢”。

方案：包裹居然被抢走了，\n我们也太不小心了……

原建议：

- JP：どろぼうに　にもつを　うばわれるなんて\nなんて　ドジなんだろう⋯⋯$
- EN：It's beyond stupid.\nHow could we get robbed?$
- 中文：说什么傻话，\n谁会抢我们的东西？$
- 理由：JP「どろぼうに にもつを うばわれるなんて なんて ドジなんだろう」(包裹被抢,我们真不小心)/EN"It's beyond stupid. How could we get robbed?"→CHS「说什么傻话,谁会抢我们的东西?」,把自责"我们真蠢"误作否认"谁会抢",语义反转
- 修改建议：包裹居然被强盗抢走了，我们也太不小心了……

### 未翻译残留/错字（1 条）

当前日版：

`说什么傻话，\n谁会抢我们的东西？`

文件：`patch/batches/031_rustborocity_devoncorp_1f.json`。

原日文（`0x08201249`）：

`どろぼうに　にもつを　うばわれるなんて\nなんて　ドジなんだろう……`

Wokann日文（`data/maps/RustboroCity_DevonCorp_1F/scripts.inc`）：

`どろぼうに　にもつを　うばわれるなんて\nなんて　ドジなんだろう⋯⋯$`

原英文（`data/maps/RustboroCity_DevonCorp_1F/scripts.inc`，`fe570a7e5^`）：

`It's beyond stupid.\nHow could we get robbed?$`

当前美版（`data/maps/RustboroCity_DevonCorp_1F/scripts.inc`）：

`说什么傻话，\n谁会抢我们的东西？$`

### 60 — RustboroCity_PokemonSchool_Text_ExplainPoison

结论：**需修复**。

体力P是残留字母，不成词；这里应表示HP。

方案：“体力P”改为“HP”，HP保持连续，不跨行拆开。

原建议：

- JP：どくを　うけると\nたいりょくが　へっていきます\pせんとうのあとも　どくは　のこるので\nあるくたびに　たいりょくが　へります\lどくけしで　なおしましょう$
- EN：If a POKéMON is poisoned, it will\nsteadily lose HP.\pThe effects of poison remain after\na battle.\pA poisoned POKéMON'
- 中文：宝可梦中毒后，\n会慢慢损失体力，\p此效果在战斗后\n依然残留。\p在探险中，中毒的宝可梦的体力P\n也会不断减少。\p使用解毒药可解毒。$
- 理由：JP「あるくたびに たいりょくが へります」(每走一步体力减少)/EN"A poisoned POKéMON's HP will drop while it is traveling"→CHS「中毒的宝可梦的体力P也会不断减少」,"体力P"中多余的"P"为HP残留字符
- 修改建议：在探险中，中毒的宝可梦的体力也会不断减少。

### 误译；未翻译残留（1 条）

当前日版：

`宝可梦中毒后，\n会慢慢损失体力，\p此效果在战斗后\n依然残留。\p在探险中，中毒的宝可梦的体力P\n也会不断减少。\p使用解毒药可解毒。`

文件：`patch/batches/038_rustborocity_pokemonschool.json`。

原日文（`0x08202E63`）：

`どくを　うけると\nたいりょくが　へっていきます\pせんとうのあとも　どくは　のこるので\nあるくたびに　たいりょくが　へります\lどくけしで　なおしましょう`

Wokann日文（`data/maps/RustboroCity_PokemonSchool/scripts.inc`）：

`どくを　うけると\nたいりょくが　へっていきます\pせんとうのあとも　どくは　のこるので\nあるくたびに　たいりょくが　へります\lどくけしで　なおしましょう$`

原英文（`data/maps/RustboroCity_PokemonSchool/scripts.inc`，`fe570a7e5^`）：

`If a POKéMON is poisoned, it will\nsteadily lose HP.\pThe effects of poison remain after\na battle.\pA poisoned POKéMON's HP will drop\nwhile it is traveling.\pHeal a poisoning using an ANTIDOTE.$`

当前美版（`data/maps/RustboroCity_PokemonSchool/scripts.inc`）：

`宝可梦中毒后，\n会慢慢损失体力，\p此效果在战斗后\n依然残留。\p在探险中，中毒的宝可梦的体力P\n也会不断减少。\p使用解毒药可解毒。$`

### 61 — gTVBravoTrainerText00

结论：**需修复**。

STR_VAR_1 是训练家，节目介绍的是其宝可梦；Rank 是比赛级别，非取得优胜。保留节目名原英文不必单独认定错误。

方案：“今天我们要介绍的，\n是{STR_VAR_1}的宝可梦！\p这只宝可梦在{STR_VAR_2}\n比赛中达到了{STR_VAR_3}级别。”；日版 FD_02/03/04 保留，控制符按本地模板。

原建议：

- JP：イヤー！\n“ブラボー　トレーナー”の　じかんだ！\pきょうは　{B_COPY_VAR_3}クラスの\n{B_COPY_VAR_2}を　ほこる\l{B_COPY_VAR_1}さんの　ポケモン！$
- EN：Yeah!\nIt's BRAVO TRAINER time!\pToday, we're going to profile a POKéMON\nbelonging to {STR_VAR_1}.\pNow, this POKéMON b
- 中文：太好了！\n现在是BRAVO训练家时间！\p今天我们所要介绍的\n主角就是{STR_VAR_1}。\p现在，这只宝可梦在{STR_VAR_2}\n比赛中荣获{STR_VAR_3}优胜。$
- 理由：JP“ブラボー トレーナー”/EN“BRAVO TRAINER”节目名在中文中直接保留拉丁字母“BRAVO”；EN“boasts a {STR_VAR_3} Rank in the {STR_VAR_2} Category”（JP“{STR_VAR_3}クラスの{STR_VAR_2}をほこる”）意为“拥有某级别头衔”，中文译成“荣获{STR_VAR_3}优胜”把“级别/Rank”误作“夺冠”。
- 修改建议：太好了！现在是喝彩训练家时间！今天我们所要介绍的主角就是{STR_VAR_1}。现在，这只宝可梦在{STR_VAR_2}比赛中达到了{STR_VAR_3}级别。

### 误译/语义缺失（专名丢失、数字丢失、占位符丢失）（1 条）

当前日版：

`太好了！\n现在是BRAVO训练家时间！\p今天我们所要介绍的\n主角就是{FD_02}。\p现在，这只宝可梦在{FD_03}\n比赛中荣获{FD_04}优胜。`

文件：`patch/batches/386_tv_0.json`。

原日文（`0x0824C754`）：

`イヤ-!\n“ブラボ-　トレ-ナ-”の　じかんだ!\pきょうは　{PLACEHOLDER_04}クラスの\n{PLACEHOLDER_03}を　ほこる\l{PLACEHOLDER_02}さんの　ポケモン!`

Wokann日文（`data/text/tv/contest_interview.inc`）：

`イヤー！\n“ブラボー　トレーナー”の　じかんだ！\pきょうは　{B_COPY_VAR_3}クラスの\n{B_COPY_VAR_2}を　ほこる\l{B_COPY_VAR_1}さんの　ポケモン！$`

原英文（`data/text/tv.inc`，`fe570a7e5^`）：

`Yeah!\nIt's BRAVO TRAINER time!\pToday, we're going to profile a POKéMON\nbelonging to {STR_VAR_1}.\pNow, this POKéMON boasts a {STR_VAR_3}\nRank in the {STR_VAR_2} Category.$`

当前美版（`data/text/tv.inc`）：

`太好了！\n现在是BRAVO训练家时间！\p今天我们所要介绍的\n主角就是{STR_VAR_1}。\p现在，这只宝可梦在{STR_VAR_2}\n比赛中荣获{STR_VAR_3}优胜。$`

### 62 — gText_NoticesGoldCard

结论：**重复**。

与58同一 gText_NoticesGoldCard，只修一个资源，两编号都关联同一任务。

方案：不修改；重复项合并至58。

原建议：

- JP：そ　それは⋯⋯\nひょっとして　ゴールドカード！？\pああ⋯⋯　きんいろが　まぶしい！\n4つの　ほしが　かがやかしい！\pわたしも　これまでに\nシルバーカードの　トレーナーさんなら\lなんにんか　みてきましたが\lゴールドカードを　おも
- EN：Th-that card…\nCould it be… The GOLD CARD?!\pOh, the gold color is brilliant!\nThe four stars seem to sparkle!\pI've see
- 中文：那、那张卡！？\p那个颜色！！\n那星星的数量！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有比这更厉害的\n训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！$
- 理由：JP：ひょっとしてゴールドカード！？（"难道是黄金卡！？"）、ああ……きんいろがまぶしい！4つのほしがかがやかしい！（"啊……金色耀眼！四颗星星闪闪发光！"）、{PLAYER}さんははじめてですよ；EN：Could it be… The GOLD CARD?! / Oh, the gold color is brilliant! The four stars seem to sparkle! / {PLAYER}×2；日版补丁中文与美版中文均为"那、那张卡！？""那星星的数量！！"（丢失"金卡"专名与数字"4"及"闪耀"语义）、"比这更厉害的训练家卡"（以模糊表述替代"黄金卡"），并删除了{P
- 修改建议：那、那张卡……！？\p难道是黄金卡！？\p啊……金色的光辉真耀眼！\n四颗星星闪闪发光！\p至今为止我也见过几位\n拥有白银卡的训练家，\l但拥有黄金卡的客人，\l{PLAYER}您还是第一位！\p先让您的宝可梦休息一下吧！

### 翻译错误（1 条）

当前日版：

`那、那张卡！？\p难道是金卡！？\p金色真耀眼！！\n四颗星在闪耀！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有比这更厉害的\n训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！`

文件：`patch/batches/196_pokemon_centers.json`。

原日文（`0x08243814`）：

`そ　それは……\nひょっとして　ゴ-ルドカ-ド!?\pああ……　きんいろが　まぶしい!\n4つの　ほしが　かがやかしい!\pわたしも　これまでに\nシルバ-カ-ドの　トレ-ナ-さんなら\lなんにんか　みてきましたが\lゴ-ルドカ-ドを　おもちの　かたは\l{PLACEHOLDER_01}さんが　はじめて　ですよ!\pさあ　{PLACEHOLDER_01}さんの\nポケモンを　やすませて　あげましょう!`

Wokann日文（`data/text/pkmn_center_nurse.inc`）：

`そ　それは⋯⋯\nひょっとして　ゴールドカード！？\pああ⋯⋯　きんいろが　まぶしい！\n4つの　ほしが　かがやかしい！\pわたしも　これまでに\nシルバーカードの　トレーナーさんなら\lなんにんか　みてきましたが\lゴールドカードを　おもちの　かたは\l{PLAYER}さんが　はじめて　ですよ！\pさあ　{PLAYER}さんの\nポケモンを　やすませて　あげましょう！$`

原英文（`data/text/pkmn_center_nurse.inc`，`fe570a7e5^`）：

`Th-that card…\nCould it be… The GOLD CARD?!\pOh, the gold color is brilliant!\nThe four stars seem to sparkle!\pI've seen several TRAINERS with\na SILVER CARD before, but, {PLAYER},\lyou're the first TRAINER I've ever\lseen with a GOLD CARD!\pOkay, {PLAYER}, please allow me\nthe honor of resting your POKéMON!$`

当前美版（`data/text/pkmn_center_nurse.inc`）：

`那、那张卡！？\p难道是金卡！？\p金色真耀眼！！\n四颗星在闪耀！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有比这更厉害的\n训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！$`

### 63 — sText_MysteryGiftVisitingTrainerArrived

结论：**需修复**。

美版已改希望，日版仍是系统。报告“日版无对应”不成立，ROM有0x085FCE8B。

方案：“系统您可以享受”改为“希望您可以享受”。

原建议：

- EN：Thank you for using the MYSTERY\nGIFT System.\pA TRAINER has arrived in\nSOOTOPOLIS CITY looking for you.\pWe hope you w
- 中文：感谢使用\n神秘礼物系统。\p一位训练家已经来到\n琉璃市寻找您。\p系统您可以享受\n与训练家的对战。\p您可以邀请其他训练家\n通过填写密码。\p试着找寻其他\n有用的密码吧。$
- 理由：美版独有文本（日版无对应）。EN "We hope you will enjoy battling the visiting TRAINER." 被译为"系统您可以享受与训练家的对战"，"We hope"误作"系统"，语义错误；补丁忠实复制美版中文（字节一致），错误继承自美版汉化。
- 修改建议：希望您会喜欢\n与这位训练家的对战。

### 凭空捏造（跨世代文本混入）（1 条）

当前日版：

`感谢使用\n神秘礼物系统。\p一位训练家已经来到\n琉璃市寻找您。\p系统您可以享受\n与训练家的对战。\p您可以邀请其他训练家\n通过填写密码。\p试着找寻其他\n有用的密码吧。`

文件：`patch/batches/471_checklist_mystery_gift_script_texts.json`。

原日文（`0x85fce8b`）：

`ふしぎなおくりもの　を　ごりよう\nいただき　ありがとう　ございます\pルネシティに　トレ-ナ-が\nきている　ようですよ\pぜひ　たいせんを\nたのしんで　くださいませ!\pほかの　あいことば　でも\nべつの　トレ-ナ-が　よべますので\pあいことばを　いろいろと\nさがして　みて　ください`

原英文（`data/scripts/gift_trainer.inc`，`fe570a7e5^`）：

`Thank you for using the MYSTERY\nGIFT System.\pA TRAINER has arrived in\nSOOTOPOLIS CITY looking for you.\pWe hope you will enjoy\nbattling the visiting TRAINER.\pYou may invite other TRAINERS by\nentering other passwords.\pTry looking for other passwords\nthat may work.$`

当前美版（`data/scripts/gift_trainer.inc`）：

`感谢使用\n神秘礼物系统。\p一位训练家已经来到\n琉璃市寻找您。\p希望您可以享受\n与训练家的对战。\p您可以邀请其他训练家\n通过填写密码。\p试着找寻其他\n有用的密码吧。$`

### 64 — [218]

结论：**已修复**。

当前已为不可思议的盒子，不是第四世代透明机器描述。

方案：不修改。

原建议：

- JP：ふしぎな はこ
シルフ カンパニーせい
- EN：A peculiar box made
by SILPH CO.
- 中文：内部储存了各种信
息的透明机器。西
尔佛公司制造
- 理由：JP原文「ふしぎな はこ」(神秘的盒子）、EN原文"A peculiar box made by SILPH CO."；中文写成"内部储存了各种信息的透明机器"。"透明机器/储存各种信息"是第四世代英文版对升级数据的描述（A transparent device filled with all sorts of data），并非本作日文原文内容，属跨世代文本混入、凭空捏造原文没有的形态描述。
- 修改建议：改为"神奇的盒子。西尔佛公司制造"（忠实于ふしぎなはこ/シルフカンパニーせい）。

### 未翻译（1 条）

当前日版：

`不可思议的盒子。\n西尔佛公司制造`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`ふしぎな　はこ\nシルフ　カンパニーせい`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A peculiar box made\nby SILPH CO.`

当前美版（`src/data/text/item_descriptions.h`）：

`不可思议的盒子。\n西尔佛公司制造`

### 65 — [76]

结论：**可选，不列必修**。

CACOPHONY为未使用特性槽。可翻为噪音，但不能作为已知正常游戏可见漏译，需另有可见调用证据。

方案：不修改。

原建议：

- JP：そうおん
- EN：CACOPHONY
- 中文：CACOPHONY
- 理由：JP原文「そうおん」（噪音），EN原文「CACOPHONY」，但JP补丁中文与美版中文均为英文原文「CACOPHONY」，从未翻译。
- 修改建议：噪音

## 三、待移植（484 条）
详见 `audit_v3_us_only.csv`。

当前日版：

`CACOPHONY`

文件：`patch/ability_names.json`。
