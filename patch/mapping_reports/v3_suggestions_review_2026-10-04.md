# v3 建议逐条复核（2026-10-04）

## 范围和结论

对报告65个条目逐条复核；其中金卡提示出现两次，实际64个不同资源。此次只写审查结论，没有修改游戏文本或ROM。
当前基准：日版5604922、美版1cbb305f7。比较当前JSON及C/ASM文本、已有提交和v2记录，并从本地fe570a7e5之前的Git对象读取完整英文地图/事件原文；日文优先读取既有覆盖指向的baserom原文并对照Wokann源码。
v2报告的已修状态只是历史证据，不是本次自动认可的依据。已发现数处旧判断或修复不完整。

- 误报/有意调整：3条
- 建议修复：35条
- 已修复：25条
- 重复：1条
- 可选：1条

## 注意事项

- 第6条：旧v2关于“命令を無視して”的依据不适用于实际覆盖的日文原文，当前“不听指挥”仍需改。
- 第41条：首次无线说明的日英原文确实没有靠近朋友提示，不能套用常规说明。
- 第58/62条：金卡、金色、四星已修，但两个玩家名及黄金卡持有者关系仍没补全。
- 第63条：神秘礼物日版也有对应文本；美版已修，日版仍有系统/希望笔误。
- 第19条：黑暗台词开头已修，后半段邀请句仍误译；日英末句用词有区域差别，不能把英文绝望语义机械套给日文。
- 第48条：怨恨当前不写固定数值，忠实于原文；不用为了详解再增加2～5。
- 保留原有控制符、动态变量、暂停和故意的描述标点。报告中的无换行整段建议不能直接照搬。
- audit_v3_us_only.csv缺失，无法判断声称的484条分别是哪条；本次未把它们当成已审完。

## 逐条总表

| 序号 | 资源 | 判定 | 处理范围 |
| --- | --- | --- | --- |
| 1 | `gText_XNatureObtainedInTrade` | 不采纳：有意排版调整 | 日版；不改 |
| 2 | `sText_PlayerGotMoney` | 误报：控制符已存在 | 日版；不改 |
| 3 | `AbandonedShip_Corridors_B1F_Text_DuncanPostBattle` | 建议修复 | 日版和美版 |
| 4 | `AquaHideout_B1F_Text_Grunt3Intro` | 建议修复 | 日版和美版 |
| 5 | `BattleFrontier_BattleDomeBattleRoom_Text_WillTheyRaceToChampionship` | 已修复 | 日版和美版 |
| 6 | `BattleFrontier_BattlePikeRoomNormal_Text_AttacksWhenStartled` | 建议修复：旧修复错误 | 日版和美版 |
| 7 | `LilycoveCity_ContestLobby_Text_ContestFeastForEyes` | 建议修复 | 日版和美版 |
| 8 | `MauvilleCity_Text_UncleNoNeedToBeDown` | 建议修复 | 日版和美版 |
| 9 | `MossdeepCity_GameCorner_1F_Text_TalkToOldManToPlay` | 建议修复 | 日版和美版 |
| 10 | `MossdeepCity_Gym_Text_BlakePostBattle` | 已修复 | 日版和美版 |
| 11 | `MossdeepCity_SpaceCenter_1F_Text_HaywireButRocketLaunchImminent` | 建议修复 | 日版和美版 |
| 12 | `MoveTutor_Text_SubstituteTeach` | 建议修复：仅剩部分 | 日版和美版 |
| 13 | `Route116_Text_JoeyIntro` | 建议修复 | 日版和美版 |
| 14 | `Route123_Text_BraxtonPostBattle` | 建议修复 | 日版和美版 |
| 15 | `SecretBase_Text_Trainer1PreChampion` | 建议修复 | 日版和美版 |
| 16 | `BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteMMon1` | 建议修复 | 日版和美版 |
| 17 | `BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteMMon2Ask` | 建议修复 | 日版和美版 |
| 18 | `BattleFrontier_Lounge5_Text_LadyClaimsSheUnderstandsPokemon` | 建议修复 | 日版和美版 |
| 19 | `BattleFrontier_OutsideEast_Text_ThriveInDarkness` | 建议修复：报告只解决一半 | 日版和美版 |
| 20 | `DewfordTown_Gym_Text_BrendenIntro` | 建议修复 | 日版和美版 |
| 21 | `EverGrandeCity_PokemonCenter_1F_Text_LeagueAfterVictoryRoad` | 已修复 | 日版和美版 |
| 22 | `FortreeCity_House1_Text_GoingToMakeVolbeatStrong` | 建议修复 | 日版和美版 |
| 23 | `FortreeCity_House3_Text_MetStevenHadAmazingPokemon` | 已修复 | 日版和美版 |
| 24 | `BattlePyramid_Text_FiveTrainersRemaining2` | 已修复 | 日版和美版 |
| 25 | `BattlePyramid_Text_FourTrainersRemaining2` | 已修复 | 日版和美版 |
| 26 | `BattlePyramid_Text_OneTrainersRemaining2` | 已修复 | 日版和美版 |
| 27 | `BattlePyramid_Text_SevenTrainersRemaining2` | 已修复 | 日版和美版 |
| 28 | `BattlePyramid_Text_SixTrainersRemaining2` | 已修复 | 日版和美版 |
| 29 | `BattlePyramid_Text_ThreeTrainersRemaining2` | 已修复 | 日版和美版 |
| 30 | `BattlePyramid_Text_TwoTrainersRemaining2` | 已修复 | 日版和美版 |
| 31 | `LilycoveCity_PokemonTrainerFanClub_Text_YoureOneWeWantToWin` | 建议修复 | 日版和美版 |
| 32 | `GraniteCave_StevensRoom_Text_ImStevenLetterForMe` | 建议修复 | 日版和美版 |
| 33 | `MossdeepCity_StevensHouse_Text_LetterFromSteven` | 已修复 | 日版和美版 |
| 34 | `gTVPokemonNewsBattleFrontierText05` | 已修复 | 日版和美版 |
| 35 | `gTVPokemonNewsBattleFrontierText06` | 已修复 | 日版和美版 |
| 36 | `gTVPokemonNewsBattleFrontierText11` | 建议修复 | 日版和美版 |
| 37 | `gTVPokemonNewsBattleFrontierText12` | 建议修复 | 日版和美版 |
| 38 | `BattleFrontier_ReceptionGate_Text_Level50Info` | 已修复 | 日版和美版 |
| 39 | `BattleFrontier_ReceptionGate_Text_OpenLevelInfo` | 已修复 | 日版和美版 |
| 40 | `CableClub_Text_ExplainWirelessClub` | 建议修复 | 日版和美版 |
| 41 | `CableClub_Text_ExplainWirelessClubFirstTime` | 误报：混淆两个模板 | 两版；不改 |
| 42 | `LavaridgeTown_Gym_1F_Text_GeraldIntro` | 建议修复 | 日版和美版 |
| 43 | `LavaridgeTown_Gym_1F_Text_GeraldPostBattle` | 建议修复 | 日版和美版 |
| 44 | `gText_BecameMoreConsciousOfOtherMons` | 建议修复 | 日版和美版 |
| 45 | `gText_Contest_Shyness` | 已修复 | 日版和美版 |
| 46 | `[127]` | 建议修复 | 日版和美版 |
| 47 | `[329]` | 已修复 | 日版和美版 |
| 48 | `[180]` | 已修复；不必增加数值 | 日版和美版 |
| 49 | `[227]` | 已修复 | 日版和美版 |
| 50 | `[276]` | 已修复 | 日版和美版 |
| 51 | `[277]` | 已修复 | 日版和美版 |
| 52 | `BattleFrontier_Lounge2_Text_AmazingPowersOfObservation` | 建议修复 | 日版和美版 |
| 53 | `BattleFrontier_Lounge7_Text_RockSlideDesc` | 已修复 | 日版和美版 |
| 54 | `LilycoveCity_ContestHall_Text_SuchCharmingCuteAppeals` | 建议修复 | 日版和美版 |
| 55 | `LilycoveCity_CoveLilyMotel_1F_Text_HeardAquaHideoutBusted` | 建议修复 | 日版和美版 |
| 56 | `MauvilleCity_Text_UncleCanYouBattleWally` | 已修复 | 日版和美版 |
| 57 | `MossdeepCity_GameCorner_1F_Text_DescribeWhichGame` | 建议修复 | 日版和美版 |
| 58 | `gText_NoticesGoldCard` | 建议修复：旧修复不完整 | 日版和美版 |
| 59 | `RustboroCity_DevonCorp_1F_Text_HowCouldWeGetRobbed` | 建议修复 | 日版和美版 |
| 60 | `RustboroCity_PokemonSchool_Text_ExplainPoison` | 建议修复 | 日版和美版 |
| 61 | `gTVBravoTrainerText00` | 建议修复：只采纳明确部分 | 日版和美版 |
| 62 | `gText_NoticesGoldCard` | 重复条目 | 归并第58条 |
| 63 | `sText_MysteryGiftVisitingTrainerArrived` | 建议修复：仅日版仍有错误 | 日版 |
| 64 | `[218]` | 已修复 | 日版和美版 |
| 65 | `[76]` | 可选：未使用特性名称 | 两版；可选 |

## 逐条依据与建议

### 1. gText_XNatureObtainedInTrade

判定：**不采纳：有意排版调整**；范围：日版；不改。

理由：f6e6cb9明确把性格后的FE从包括交换文本在内的多种摘要模板删除；当前摘要还有ChsUseMuzaiIfLong按156px切换窄字体。不能把与原版换行不同直接判为遗漏。

建议处理：保留当前排版；若交换宝可梦摘要实测裁切，再针对显示宽度处理，不机械恢复FE。

当前日版中文：

来源：`patch/batches/172_party.json`

```text
{DYNAMIC 0}{DYNAMIC 2}{DYNAMIC 1}{DYNAMIC 5}的性格，通过交换遇见了它。
```

当前美版中文：

来源：`src/strings.c`

```text
{DYNAMIC 0}{DYNAMIC 2}{DYNAMIC 1}{DYNAMIC 5}的性格，
通过交换遇见了它。
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x085CA4F2`

```text
{BYTE_F7}　{BYTE_F7}い{BYTE_F7}あ{BYTE_F7}おせいかく\nつうしんこうかんに　よって　であった
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`src/strings.c`，版本：`fe570a7e5^`

```text
{DYNAMIC 0}{DYNAMIC 2}{DYNAMIC 1}{DYNAMIC 5} nature,
obtained in a trade.
```

v3原报告条目（保留原建议供对照）：

```text
- 补丁中文：{DYNAMIC_0}{DYNAMIC_2}{DYNAMIC_1}{DYNAMIC_5}的性格，通过交换遇见了它。$
- 理由：JP原0x085CA4F2: {D0}{D2}{D1}{D5}せいかく、\nつうしんこうかんによってであった（有换行）；P无换行 / U有换行。补丁丢了日文原有的换行。
- 修改建议：{DYNAMIC_0}{DYNAMIC_2}{DYNAMIC_1}{DYNAMIC_5}的性格，\n通过交换遇见了它。
```

### 2. sText_PlayerGotMoney

判定：**误报：控制符已存在**；范围：日版；不改。

理由：当前batch178末尾3CFBFF明确包含叹号、换页FB和结束FF，报告自己的引文也包含\p。円后置为既定要求。

建议处理：不修改末尾控制符，不改金额符号及其位置。

当前日版中文：

来源：`patch/batches/178_battle_victory.json`

```text
作为奖金，\n{FD_23}获得了{FD_00}{JPN}¥{ENG}！\p
```

当前美版中文：

来源：`src/battle_message.c`

```text
作为奖金，
{B_PLAYER_NAME}获得了¥{B_BUFF1}！\p
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x085A97B2`

```text
{PLACEHOLDER_23}は　しょうきんとして\n{PLACEHOLDER_00}¥　てにいれた!\p
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`src/battle_message.c`，版本：`fe570a7e5^`

```text
{B_PLAYER_NAME} got ¥{B_BUFF1}
for winning!\p
```

v3原报告条目（保留原建议供对照）：

```text
- 补丁中文：作为奖金，\n{FD_23}获得了{B_BUFF1}{FC_JPN}¥{FC_ENG}！\p$
- 理由：补丁丢了\p换页符。P: {FD_23}获得了{B_BUFF1}{FC_JPN}¥{FC_ENG}！\p$ / U: {B_PLAYER_NAME}获得了¥{B_BUFF1}！\p$。¥后置不判错，但\p缺失需补回。
- 修改建议：补回末尾的\p。

## 二、美版汉化继承的错误

### 语义误译（13 条）
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 5345,
    "decision": "intentional_adaptation",
    "review": {
      "row_number": 5345,
      "symbol": "sText_PlayerGotMoney",
      "domain": "ported_batch",
      "idx": "4092",
      "reason": "数字后显示円是用户要求且符合日版原文；不恢复美版前置金额符号。",
      "action": "intentional_adaptation"
    }
  }
]
```

### 3. AbandonedShip_Corridors_B1F_Text_DuncanPostBattle

判定：**建议修复**；范围：日版和美版。

理由：ふなぞこが水の中にしずんでいる / ship’s bottom has sunk均指船底沉入水中，不是搁浅；未说明是说话者自己的船。

建议处理：将第一句改为“这艘船的船底已经沉到水里了。”；保留后面的潜水提示和换页。不照抄报告绕口的“我们的船的船底”。

当前日版中文：

来源：`patch/batches/197_abandoned_ship.json`

```text
我们的船现在搁浅了。\p如果有会潜水的宝可梦的话，\n或许能帮上什么忙……
```

当前美版中文：

来源：`data/maps/AbandonedShip_Corridors_B1F/scripts.inc`

```text
我们的船现在搁浅了。\p如果有会潜水的宝可梦的话，
或许能帮上什么忙……$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0821ACD0`

```text
ふなぞこが　みずの　なかに\nしずんで　いるんだよ\pポケモンが　みずに　もぐれる　わざを\nつかえたら　さきに　すすめるんだがな……
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/AbandonedShip_Corridors_B1F/scripts.inc`，版本：`fe570a7e5^`

```text
The ship's bottom has sunk into the
depths.\pIf a POKéMON knew how to go underwater,
we might make some progress…$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：ふなぞこが　みずの　なかに
しずんで　いるんだよ\pポケモンが　みずに　もぐれる　わざを
つかえたら　さきに　すすめるんだがな……
- EN：The ship's bottom has sunk into the\ndepths.\pIf a POKéMON knew how to go underwater,\nwe might make some progress…$
- 中文：我们的船现在搁浅了。\p如果有会潜水的宝可梦的话，\n或许能帮上什么忙……$
- 理由：JP「ふなぞこが みずの なかに しずんでいる」(船底沉入水中)/EN「The ship's bottom has sunk into the depths」均指沉没，而CHS写成「我们的船现在搁浅了」——「搁浅」意为船只在浅滩受阻，与「沉入水中」语义矛盾。
- 修改建议：我们的船的船底现在沉到水里了。
```

### 4. AquaHideout_B1F_Text_Grunt3Intro

判定：**建议修复**；范围：日版和美版。

理由：おやつ / snacks是零食，不是巡航系统；后半句明确表示剩下要打倒碍事者。

建议处理：采用“燃料补给完毕！\n零食补给完毕！\p接下来只要干掉\n捣乱的家伙就行了！”，保留控制符。

当前日版中文：

来源：`patch/batches/141_aquahideout_b1f.json`

```text
燃料供给完成！\n巡航系统正常！\p一切正常，除了一个\n找麻烦的人！
```

当前美版中文：

来源：`data/maps/AquaHideout_B1F/scripts.inc`

```text
燃料供给完成！
巡航系统正常！\p一切正常，除了一个
找麻烦的人！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08217E76`

```text
ねんりょうの　ほきゅう　オッケイ!\nおやつも　ほきゅう　オッケイ!\pあとは　ジャマものを　ぶっとばす　だけ!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/AquaHideout_B1F/scripts.inc`，版本：`fe570a7e5^`

```text
Fuel supply loaded A-OK!
In-cruise snacks loaded A-OK!\pNothing left to do but KO a pesky
meddler!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：ねんりょうの　ほきゅう　オッケイ!
おやつも　ほきゅう　オッケイ!\pあとは　ジャマものを　ぶっとばす　だけ!
- EN：Fuel supply loaded A-OK!\nIn-cruise snacks loaded A-OK!\pNothing left to do but KO a pesky\nmeddler!$
- 中文：燃料供给完成！\n巡航系统正常！\p一切正常，除了一个\n找麻烦的人！$
- 理由：JP「おやつも ほきゅう オッケイ」/EN「In-cruise snacks loaded A-OK」中「おやつ」是零食，CHS误作「巡航系统正常」；且JP「あとは ジャマものを ぶっとばす だけ」(剩下就是干掉捣乱者)/EN「Nothing left to do but KO a pesky meddler」被CHS写成「一切正常，除了一个找麻烦的人」，丢失了「打飞捣乱者」的动作含义。
- 修改建议：燃料补给完毕！\n零食补给完毕！\p接下来只要干掉\n捣乱的家伙就行了！
```

### 5. BattleFrontier_BattleDomeBattleRoom_Text_WillTheyRaceToChampionship

判定：**已修复**；范围：日版和美版。

理由：两版当前已为“这位训练家能否\n一举夺冠呢？\p”，不再是“哪一位”。

建议处理：无需重复修改。

当前日版中文：

来源：`patch/batches/200_battle_frontier_battle_dome_battle_room.json`

```text
这位训练家能否\n一举夺冠呢？\p
```

当前美版中文：

来源：`data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc`

```text
这位训练家能否
一举夺冠呢？\p$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x082296B5`

```text
いっきに　ゆうしょうまで\nのぼりつめて　しまうのでしょうか!?\p
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc`，版本：`fe570a7e5^`

```text
Will this TRAINER race to
the championship?\p$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：いっきに　ゆうしょうまで\nのぼりつめて　しまうのでしょうか！？\p$
- EN：Will this TRAINER race to\nthe championship?\p$
- 中文：哪一位训练家进入\n冠军赛了呢？\p$
- 理由：JP「いっきに ゆうしょうまで のぼりつめて しまうのでしょうか」/EN「Will this TRAINER race to the championship?」问的是「这位训练家能否一举登顶」，CHS作「哪一位训练家进入冠军赛了呢」——将「这位(this)」误作「哪一位(which)」，疑问对象完全改变。
- 修改建议：这位训练家会一举登上冠军宝座吗？
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 5966,
    "decision": "fixed_verified",
    "review": {
      "row_number": 5966,
      "symbol": "BattleFrontier_BattleDomeBattleRoom_Text_WillTheyRaceToChampionship",
      "domain": "ported_batch",
      "idx": "4714",
      "old": "哪一位训练家进入\n冠军赛了呢？",
      "new": "这位训练家能否\n一举夺冠呢？",
      "reason": "原文问能否夺冠，不是问哪位进入决赛。",
      "scope": "both",
      "action": "fix",
      "final_text": "这位训练家能否\n一举夺冠呢？\\p",
      "old_current_text": "哪一位训练家进入\n冠军赛了呢？\\p",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc",
        "patch/batches/200_battle_frontier_battle_dome_battle_room.json"
      ],
      "us_source_file": "data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc",
          "text": "いっきに　ゆうしょうまで\nのぼりつめて　しまうのでしょうか！？\\p$"
        }
      ]
    }
  }
]
```

### 6. BattleFrontier_BattlePikeRoomNormal_Text_AttacksWhenStartled

判定：**建议修复：旧修复错误**；范围：日版和美版。

理由：实际日文0x08234E0C为“きゅうにひとをみるとおどろいて / おそいかかってしまう”，不存在“命令を無視して”。英文without warning也不是不听指挥。v2把无视警告改为不听指挥仍不正确。

建议处理：前段改为“它突然看到人受惊时，\n就会猛扑过来攻击……”；保留后段“您和您的宝可梦还好吗？”及换页。纠正v2判断依据。

当前日版中文：

来源：`patch/batches/212_battle_frontier_battle_pike_room_normal.json`

```text
一旦受到了惊吓就会\n不听指挥胡乱攻击……\p您和您的宝可梦还好吗？
```

当前美版中文：

来源：`data/maps/BattleFrontier_BattlePikeRoomNormal/scripts.inc`

```text
一旦受到了惊吓就会
不听指挥胡乱攻击……\p您和您的宝可梦还好吗？$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08234E0C`

```text
きゅうに　ひとを　みると　おどろいて\nおそいかかって　しまうのだ……\pきみも　ポケモンも　だいじょうぶか?
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_BattlePikeRoomNormal/scripts.inc`，版本：`fe570a7e5^`

```text
It attacks without warning if it is
startled by another person…\pAre you and your POKéMON all right?$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：きゅうに　ひとを　みると　おどろいて\nおそいかかって　しまうのだ⋯⋯\pきみも　ポケモンも　だいじょうぶか？$
- EN：It attacks without warning if it is\nstartled by another person…\pAre you and your POKéMON all right?$
- 中文：一旦受到了惊吓就会\n无视警告胡乱攻击……\p您和您的宝可梦还好吗？$
- 理由：JP「きゅうに ひとを みると おどろいて おそいかかって しまう」/EN「It attacks without warning if it is startled by another person」中「without warning」指「毫无征兆地」，CHS作「无视警告胡乱攻击」——将「without warning」误读为「无视警告」，且「おそいかかる(猛扑)」被写成「胡乱攻击」，语义错误。
- 修改建议：它一旦突然看到人受了惊吓，就会猛扑过来攻击……
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 6256,
    "decision": "fixed_verified",
    "review": {
      "row_number": 6256,
      "symbol": "BattleFrontier_BattlePikeRoomNormal_Text_AttacksWhenStartled",
      "domain": "ported_batch",
      "idx": "5004",
      "old": "无视警告胡乱攻击",
      "new": "不听指挥胡乱攻击",
      "reason": "JP命令を無視して指无视指挥，而非无视警告。",
      "scope": "both",
      "action": "fix",
      "final_text": "一旦受到了惊吓就会\n不听指挥胡乱攻击……\\p您和您的宝可梦还好吗？",
      "old_current_text": "一旦受到了惊吓就会\n无视警告胡乱攻击……\\p您和您的宝可梦还好吗？",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/BattleFrontier_BattlePikeRoomNormal/scripts.inc",
        "patch/batches/212_battle_frontier_battle_pike_room_normal.json"
      ],
      "us_source_file": "data/maps/BattleFrontier_BattlePikeRoomNormal/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/BattleFrontier_BattlePikeRoomNormal/scripts.inc",
          "text": "きゅうに　ひとを　みると　おどろいて\nおそいかかって　しまうのだ⋯⋯\\pきみも　ポケモンも　だいじょうぶか？$"
        }
      ]
    }
  }
]
```

### 7. LilycoveCity_ContestLobby_Text_ContestFeastForEyes

判定：**建议修复**；范围：日版和美版。

理由：かきがいのある / scream to be painted指值得画下来的宝可梦，不是已经在画里的宝可梦。

建议处理：把后半段改为“快看那些值得入画的\n宝可梦！”；保留视觉盛宴那一段。

当前日版中文：

来源：`patch/batches/126_lilycovecity_contestlobby.json`

```text
哇，观看华丽大赛\n简直是场视觉盛宴！\p你看过那些\n画里的宝可梦吗？
```

当前美版中文：

来源：`data/maps/LilycoveCity_ContestLobby/scripts.inc`

```text
哇，观看华丽大赛
简直是场视觉盛宴！\p你看过那些
画里的宝可梦吗？$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x082076BA`

```text
いやあ　コンテストかいじょうに　くると\nかきがいの　ある　ポケモンが\lいっぱい　だね!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/LilycoveCity_ContestLobby/scripts.inc`，版本：`fe570a7e5^`

```text
Wow, coming out to a CONTEST is
a feast for these eyes!\pWould you look at all the POKéMON
that just scream to be painted?$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：いやあ　コンテストかいじょうに　くると
かきがいの　ある　ポケモンが\lいっぱい　だね!
- EN：Wow, coming out to a CONTEST is\na feast for these eyes!\pWould you look at all the POKéMON\nthat just scream to be pain
- 中文：哇，观看华丽大赛\n简直是场视觉盛宴！\p你看过那些\n画里的宝可梦吗？$
- 理由：JP「かきがいのあるポケモンがいっぱいだね」/EN“POKéMON that just scream to be painted”意为“值得入画的宝可梦”，中文“你看过那些画里的宝可梦吗？”把“值得被画下来”误作“画里面的宝可梦”，关系颠倒。
- 修改建议：哇，观看华丽大赛\n简直是场视觉盛宴！\p快看那些值得入画的\n宝可梦！
```

### 8. MauvilleCity_Text_UncleNoNeedToBeDown

判定：**建议修复**；范围：日版和美版。

理由：これからもっともっとつよくなればいい是在鼓励今后继续变强；英文what’s keeping you from也不是询问激励来源。

建议处理：把中段改为“以后继续变得越来越强\n不就好了吗！”；保留叔叔、满充及回家句。

当前日版中文：

来源：`patch/batches/050_mauvillecity.json`

```text
叔叔：满充，\n别这么沮丧。\p想想是什么激励着你\n要变得越来越强的？\p好了，我们回家吧，\n大家都在等你呢。
```

当前美版中文：

来源：`data/maps/MauvilleCity/scripts.inc`

```text
叔叔：满充，
别这么沮丧。\p想想是什么激励着你
要变得越来越强的？\p好了，我们回家吧，
大家都在等你呢。$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x081DE0F4`

```text
おじさん“ミツルくん\nそんなに　しょげることは　ないよ\pこれから　もっともっと\nつよくなれば　いいじゃないか!\pさあ　うちに　かえろう\nみんな　まってるよ
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/MauvilleCity/scripts.inc`，版本：`fe570a7e5^`

```text
UNCLE: WALLY, there's no need to be so
down on yourself.\pWhy, what's keeping you from becoming
stronger and stronger?\pCome on, let's go home.
Everyone's waiting for you.$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：おじさん“ミツルくん\nそんなに　しょげることは　ないよ\pこれから　もっともっと\nつよくなれば　いいじゃないか！\pさあ　うちに　かえろう\nみんな　まってるよ$
- EN：UNCLE: WALLY, there's no need to be so\ndown on yourself.\pWhy, what's keeping you from becoming\nstronger and stronger?
- 中文：叔叔：满充，\n别这么沮丧。\p想想是什么激励着你\n要变得越来越强的？\p好了，我们回家吧，\n大家都在等你呢。$
- 理由：JP「これからもっともっとつよくなればいいじゃないか（以后继续变得越来越强不就好了吗）」/EN「what's keeping you from becoming stronger and stronger?（有什么能阻止你继续变强呢）」均为鼓励继续变强，补丁/美版中文误作「想想是什么激励着你要变得越来越强的」，把EN「what's keeping you from（什么在阻碍你）」误读为「激励」，语义错误。
- 修改建议：以后继续变得越来越强不就好了吗！
```

### 9. MossdeepCity_GameCorner_1F_Text_TalkToOldManToPlay

判定：**建议修复**；范围：日版和美版。

理由：おとなり / beside明确指旁边，两版当前仍为后面。

建议处理：仅把“我后面的老人”改为“我旁边的老人”。

当前日版中文：

来源：`patch/batches/151_mossdeepcity_gamecorner_1f.json`

```text
如果您想玩游戏，\n就告诉我后面的老人。
```

当前美版中文：

来源：`data/text/cable_club.inc`

```text
如果您想玩游戏，
就告诉我后面的老人。$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08248314`

```text
ゲ-ムを　するなら\nおとなりの　おじいさんに　いってね
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/cable_club.inc`，版本：`fe570a7e5^`

```text
If you want to play a game,
please tell the old man beside me.$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：ゲームを　するなら\nおとなりの　おじいさんに　いってね$
- EN：If you want to play a game,\nplease tell the old man beside me.$
- 中文：如果您想玩游戏，\n就告诉我后面的老人。$
- 理由：JP「おとなりのおじいさん（旁边的老爷爷）」/EN「the old man beside me（我旁边的老人）」明确方位为「旁边」，补丁/美版中文误作「我后面的老人」，方位错误。
- 修改建议：就告诉我旁边的老人。
```

### 10. MossdeepCity_Gym_Text_BlakePostBattle

判定：**已修复**；范围：日版和美版。

理由：两版当前结尾已为“我可没用嘴吹！真的！”，否认吹气作弊，不再误作吹牛。

建议处理：无需重复修改。

当前日版中文：

来源：`patch/batches/152_mossdeepcity_gym.json`

```text
要用精神力举起精灵球还是困难\n了点，但这么小的灰尘的话……\p呜啊啊啊啊啊啊啊！\n…… …… ……\p不不，我没骗人！\n我可没用嘴吹！真的！
```

当前美版中文：

来源：`data/maps/MossdeepCity_Gym/scripts.inc`

```text
要用精神力举起精灵球还是困难
了点，但这么小的灰尘的话……\p呜啊啊啊啊啊啊啊！
…… …… ……\p不不，我没骗人！
我可没用嘴吹！真的！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0820BA3C`

```text
モンスタ-ボ-ルは　おおきすぎた\nこの　わたぼこり　なら　ぜったいに……\pふううううううっ……!\p……　……　……\n……　……　……\pちがうぞ!\nはないきで　とばして　なんか　いないぞ!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/MossdeepCity_Gym/scripts.inc`，版本：`fe570a7e5^`

```text
A POKé BALL was too heavy to lift
psychically. But this dust bunny…\pWhoooooooooooooooh!
… … … … … …\pNo, I'm not cheating!
I didn't blow on it! Honestly!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：モンスタ-ボ-ルは　おおきすぎた
この　わたぼこり　なら　ぜったいに……\pふううううううっ……!\p……　……　……
……　……　……\pちがうぞ!
はないきで　とばして　なんか　いないぞ!
- EN：A POKé BALL was too heavy to lift\npsychically. But this dust bunny…\pWhoooooooooooooooh!\n… … … … … …\pNo, I'm not chea
- 中文：要用精神力举起精灵球还是困难\n了点，但这么小的灰尘的话……\p呜啊啊啊啊啊啊啊！\n…… …… ……\p不不，我没骗人！\n我没吹牛！真的！$
- 理由：JP「ちがうぞ！はないきでとばしてなんかいないぞ（不对！我才没有用嘴吹它！）」/EN「I didn't blow on it!（我没对它吹气！）」中「吹」指用嘴吹气，补丁/美版中文误作「我没吹牛」，「吹气」误译为「吹牛（说大话）」，语义错误。
- 修改建议：我没用嘴吹！真的！
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 4394,
    "decision": "fixed_verified",
    "review": {
      "row_number": 4394,
      "symbol": "MossdeepCity_Gym_Text_BlakePostBattle",
      "domain": "ported_batch",
      "idx": "3139",
      "old": "我没吹牛！真的！",
      "new": "我可没用嘴吹！真的！",
      "reason": "原文否认吹气作弊，不是否认吹牛。",
      "scope": "both",
      "action": "fix",
      "final_text": "要用精神力举起精灵球还是困难\n了点，但这么小的灰尘的话……\\p呜啊啊啊啊啊啊啊！\n…… …… ……\\p不不，我没骗人！\n我可没用嘴吹！真的！",
      "old_current_text": "要用精神力举起精灵球还是困难\n了点，但这么小的灰尘的话……\\p呜啊啊啊啊啊啊啊！\n…… …… ……\\p不不，我没骗人！\n我没吹牛！真的！",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/MossdeepCity_Gym/scripts.inc",
        "patch/batches/152_mossdeepcity_gym.json"
      ],
      "us_source_file": "data/maps/MossdeepCity_Gym/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/MossdeepCity_Gym/scripts.inc",
          "text": "モンスターボールは　おおきすぎた\nこの　わたぼこり　なら　ぜったいに⋯⋯\\pふううううううっ⋯⋯！\\p⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯\\pちがうぞ！\nはないきで　とばして　なんか　いないぞ！$"
        }
      ]
    }
  }
]
```

### 11. MossdeepCity_SpaceCenter_1F_Text_HaywireButRocketLaunchImminent

判定：**建议修复**；范围：日版和美版。

理由：もうすぐ発射 / launch is imminent是马上发射，不是程序不会停止。

建议处理：末句改为“火箭马上就要发射了！”。

当前日版中文：

来源：`patch/batches/157_mossdeepcity_spacecenter_1f.json`

```text
我知道现在一切有些混乱，\n但是……\p火箭发射程序不会停止！
```

当前美版中文：

来源：`data/maps/MossdeepCity_SpaceCenter_1F/scripts.inc`

```text
我知道现在一切有些混乱，
但是……\p火箭发射程序不会停止！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0820D0FD`

```text
こんな　さわぎの　とちゅう　だけど……\pもうすぐ　ロケットが　はっしゃ　するぞ!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/MossdeepCity_SpaceCenter_1F/scripts.inc`，版本：`fe570a7e5^`

```text
I know that things are a little
haywire right now, but…\pThe rocket's launch is imminent!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：こんな　さわぎの　とちゅう　だけど……\pもうすぐ　ロケットが　はっしゃ　するぞ!
- EN：I know that things are a little\nhaywire right now, but…\pThe rocket's launch is imminent!$
- 中文：我知道现在一切有些混乱，\n但是……\p火箭发射程序不会停止！$
- 理由：JP「もうすぐロケットがはっしゃするぞ（火箭马上就要发射了）」/EN「The rocket's launch is imminent（火箭发射在即）」明确指发射即将发生，补丁/美版中文误作「火箭发射程序不会停止」，「在即」误译为「不会停止」，语义错误。
- 修改建议：火箭马上就要发射了！
```

### 12. MoveTutor_Text_SubstituteTeach

判定：**建议修复：仅剩部分**；范围：日版和美版。

理由：重复的“如果”已经删去；“そうだわ”是在想到主意，当前仍译为“明白了”。

建议处理：只把“明白了！”改为“对了！”；保留现有段落、标点和已修好的其他文字，不把整段挤成一行。

当前日版中文：

来源：`patch/batches/340_move_tutors.json`

```text
当我在屋顶上看着\n这广阔的世界时……\p我在想如果这个世界\n有不止一个自己该多有趣啊，\l那样我就能体验各种各样的人生了。\p当然这是不可能的。\n嘿嘿……\p明白了！\n不如让你的宝可梦学习替身吧？
```

当前美版中文：

来源：`data/text/move_tutors.inc`

```text
当我在屋顶上看着
这广阔的世界时……\p我在想如果这个世界
有不止一个自己该多有趣啊，\l那样我就能体验各种各样的人生了。\p当然这是不可能的。
嘿嘿……\p明白了！
不如让你的宝可梦学习替身吧？$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08276436`

```text
ふう\nこうやって　おくじょうから\lひろい　せかいを　みていると……\pなんにんもの　じぶんが　いて\nいくつもの　じんせいを　たのしめたらな-\lって　おもうの!\lムリな　はなしだけどね　うふふ\pそうだわ　あなたの　ポケモンちゃん!\nみがわりの　わざ　おぼえてみない?
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/move_tutors.inc`，版本：`fe570a7e5^`

```text
When I see the wide world from up
here on the roof…\pI think about how nice it would be
if there were more than just one me\lso I could enjoy all sorts of lives.\pOf course it's not possible.
Giggle…\pI know! Would you be interested in
having a POKéMON learn SUBSTITUTE?$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：ふう\nこうやって　おくじょうから\lひろい　せかいを　みていると⋯⋯\pなんにんもの　じぶんが　いて\nいくつもの　じんせいを　たのしめたらなー\lって　おもうの！\lムリな　はなしだけどね　うふふ\pそうだわ　あなたの　ポケモンちゃん！
- EN：When I see the wide world from up\nhere on the roof…\pI think about how nice it would be\nif there were more than just o
- 中文：当我在屋顶上看着\n这广阔的世界时……\p我在想如果这个世界如果\n有不止一个自己该多有趣啊，\l那样我就能体验各种各样的人生了。\p当然这是不可能的。\n嘿嘿……\p明白了！\n不如让你的宝可梦学习替身吧？$
- 理由：JP「そうだわ（对了/我有主意了）」是想出主意的感叹，补丁/美版中文误作「明白了」，语义错误；且「我在想如果这个世界如果有不止一个自己」中「如果」重复，属衍字；其余「なんにんものじぶんがいていくつものじんせいをたのしめたらなー」与「有不止一个自己该多有趣…体验各种各样的人生」语义一致。
- 修改建议：当我在屋顶上看着这广阔的世界时……我在想如果这个世界有不止一个自己该多有趣啊，那样我就能体验各种各样的人生了。当然这是不可能的。嘿嘿……对了！不如让你的宝可梦学习替身吧？
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 7558,
    "decision": "fixed_verified",
    "review": {
      "row_number": 7558,
      "symbol": "MoveTutor_Text_SubstituteTeach",
      "domain": "ported_batch",
      "idx": "6306",
      "old": "我在想如果这个世界如果",
      "new": "我在想如果这个世界",
      "reason": "重复如果。",
      "scope": "both",
      "action": "fix",
      "final_text": "当我在屋顶上看着\n这广阔的世界时……\\p我在想如果这个世界\n有不止一个自己该多有趣啊，\\l那样我就能体验各种各样的人生了。\\p当然这是不可能的。\n嘿嘿……\\p明白了！\n不如让你的宝可梦学习替身吧？",
      "old_current_text": "当我在屋顶上看着\n这广阔的世界时……\\p我在想如果这个世界如果\n有不止一个自己该多有趣啊，\\l那样我就能体验各种各样的人生了。\\p当然这是不可能的。\n嘿嘿……\\p明白了！\n不如让你的宝可梦学习替身吧？",
      "changed_files": [
        "../pokeemerald_us_chs/data/text/move_tutors.inc",
        "patch/batches/340_move_tutors.json"
      ],
      "us_source_file": "data/text/move_tutors.inc",
      "jp_source": [
        {
          "file": "data/text/move_tutors.inc",
          "text": "ふう\nこうやって　おくじょうから\\lひろい　せかいを　みていると⋯⋯\\pなんにんもの　じぶんが　いて\nいくつもの　じんせいを　たのしめたらなー\\lって　おもうの！\\lムリな　はなしだけどね　うふふ\\pそうだわ　あなたの　ポケモンちゃん！\nみがわりの　わざ　おぼえてみない？$"
        }
      ]
    }
  }
]
```

### 13. Route116_Text_JoeyIntro

判定：**建议修复**；范围：日版和美版。

理由：つえーぞ / rule在此是很强、很厉害，中文“运用”不成句。

建议处理：第一句改为“我的宝可梦很强！”，第二句保留。

当前日版中文：

来源：`patch/batches/028_route116.json`

```text
我的宝可梦运用！\n你就好好瞧瞧吧！
```

当前美版中文：

来源：`data/text/trainers.inc`

```text
我的宝可梦运用！
你就好好瞧瞧吧！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0825D643`

```text
おれの　ポケモン　つえ-ぞ!\nちょっと　みてみろよ!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/trainers.inc`，版本：`fe570a7e5^`

```text
My POKéMON rule!
Check them out!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：おれの　ポケモン　つえーぞ！\nちょっと　みてみろよ！$
- EN：My POKéMON rule!\nCheck them out!$
- 中文：我的宝可梦运用！\n你就好好瞧瞧吧！$
- 理由：JP「おれの ポケモン つえーぞ」(我的宝可梦很强)/EN"My POKéMON rule!"→CHS「我的宝可梦运用!」,“运用”意为使用/应用,语义不通
- 修改建议：我的宝可梦很强！
```

### 14. Route123_Text_BraxtonPostBattle

判定：**建议修复**；范围：日版和美版。

理由：ジムバッジに恥じない / did your BADGES proud是在称赞不辱已有徽章，不是在说本场获得徽章。

建议处理：改为“那场对战无愧于\n你的道馆徽章！”。

当前日版中文：

来源：`patch/batches/148_route123.json`

```text
在那样的对战中获得徽章\n是你的骄傲。
```

当前美版中文：

来源：`data/text/trainers.inc`

```text
在那样的对战中获得徽章
是你的骄傲。$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0825FA26`

```text
ジムバッジに　はじない\nたたかい　だったよ!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/trainers.inc`，版本：`fe570a7e5^`

```text
You did your BADGES proud in that
match!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：ジムバッジに　はじない\nたたかい　だったよ！$
- EN：You did your BADGES proud in that\nmatch!$
- 中文：在那样的对战中获得徽章\n是你的骄傲。$
- 理由：JP「ジムバッジに はじない たたかい だったよ」(那场对战无愧于徽章)/EN"You did your BADGES proud"→CHS「在那样的对战中获得徽章是你的骄傲」,把"无愧于徽章"误作"获得徽章是骄傲",主谓关系颠倒
- 修改建议：那场对战无愧于你的道馆徽章！
```

### 15. SecretBase_Text_Trainer1PreChampion

判定：**建议修复**；范围：日版和美版。

理由：やっと使えるようになった / finally got to use表示已经终于用上；always taken也不是经常有人来。

建议处理：建议完整修正为“这个地方非常受欢迎，\n总是被人占着。\p我等了好久才等到它空出来，\n终于能用上这里了！”；不能只改最后一句而留下占用状态误译。

当前日版中文：

来源：`patch/batches/391_secret_base_trainers.json`

```text
这个地方非常受欢迎，\n经常会有人来这里。\p我一直在等它打开，\n我一定要得到它！
```

当前美版中文：

来源：`data/text/secret_base_trainers.inc`

```text
这个地方非常受欢迎，
经常会有人来这里。\p我一直在等它打开，
我一定要得到它！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x082453A7`

```text
この　ばしょは　にんきが　あるから\nいつも　うまって　いるんだよ-\pぼくは　ずっと　まっていて\nやっと　つかえる　ように　なったんだ!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/secret_base_trainers.inc`，版本：`fe570a7e5^`

```text
This is a popular spot.
It's always taken.\pI waited a long time for it to open.
I finally got to use it!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：この　ばしょは　にんきが　あるから\nいつも　うまって　いるんだよー\pぼくは　ずっと　まっていて\nやっと　つかえる　ように　なったんだ！$
- EN：This is a popular spot.\nIt's always taken.\pI waited a long time for it to open.\nI finally got to use it!$
- 中文：这个地方非常受欢迎，\n经常会有人来这里。\p我一直在等它打开，\n我一定要得到它！$
- 理由：JP“やっと つかえる ように なったんだ”(终于能用上这里了)/EN“I finally got to use it!”；中文“我一定要得到它”与原文“终于得以使用”语义相反方向，为误译。
- 修改建议：我一直在等它空出来，终于能用上这里了！

### 语义偏差（8 条）
```

### 16. BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteMMon1

判定：**建议修复**；范围：日版和美版。

理由：decent是不错，不是高贵；日文实际强调自己培育的宝可梦。

建议处理：建议用“我培育了两只不错的宝可梦。\n一只掌握{STR_VAR_1}的{STR_VAR_2}和”，保留此句与下一条拼接关系和动态参数。

当前日版中文：

来源：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`

```text
我有一对高贵的宝可梦。\n一只掌握{FD_02}的{FD_03}和
```

当前美版中文：

来源：`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`

```text
我有一对高贵的宝可梦。
一只掌握{STR_VAR_1}的{STR_VAR_2}和$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08226286`

```text
オレの　そだてた　ポケモンは\n{PLACEHOLDER_02}を　つかう　{PLACEHOLDER_03}と……
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`，版本：`fe570a7e5^`

```text
I got a couple decent POKéMON.
One {STR_VAR_2} with {STR_VAR_1} and$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：オレの　そだてた　ポケモンは\n{STR_VAR_1}を　つかう　{STR_VAR_2}と⋯⋯$
- EN：I got a couple decent POKéMON.\nOne {STR_VAR_2} with {STR_VAR_1} and$
- 中文：我有一对高贵的宝可梦。\n一只掌握{STR_VAR_1}的{STR_VAR_2}和$
- 理由：EN「a couple decent POKéMON」意为「几只不错的宝可梦」，JP「そだてた ポケモン」仅为「培育的宝可梦」；补丁中文「高贵的宝可梦」将decent误作「高贵」，语义偏差。
- 修改建议：我有一对不错的宝可梦。\n一只掌握{STR_VAR_1}的{STR_VAR_2}和$
```

### 17. BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteMMon2Ask

判定：**建议修复**；范围：日版和美版。

理由：neat在此是很棒、不错，不是高雅；日文是邀请组队。

建议处理：采用“如果我们组队，那就太棒了，\n你觉得呢？”；保留之前的招式名和种族名占位符。

当前日版中文：

来源：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`

```text
一只掌握{FD_02}的{FD_03}！\p如果我们组队，那是多高雅的\n一件事呀，你觉得呢？
```

当前美版中文：

来源：`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`

```text
一只掌握{STR_VAR_1}的{STR_VAR_2}！\p如果我们组队，那是多高雅的
一件事呀，你觉得呢？$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x082262A3`

```text
{PLACEHOLDER_02}を　つかう　{PLACEHOLDER_03}　だよ\pどう?\nオレと　タッグを　くんでみない?
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`，版本：`fe570a7e5^`

```text
one {STR_VAR_2} with {STR_VAR_1}!\pIt'd be neat if we made a tag team
together, so how about it?$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：{STR_VAR_1}を　つかう　{STR_VAR_2}　だよ\pどう？\nオレと　タッグを　くんでみない？$
- EN：one {STR_VAR_2} with {STR_VAR_1}!\pIt'd be neat if we made a tag team\ntogether, so how about it?$
- 中文：一只掌握{STR_VAR_1}的{STR_VAR_2}！\p如果我们组队，那是多高雅的\n一件事呀，你觉得呢？$
- 理由：EN「It'd be neat if we made a tag team」意为「组队会很不错」；补丁中文「那是多高雅的一件事呀」将neat(很棒)误作「高雅」，语义偏差。
- 修改建议：一只掌握{STR_VAR_1}的{STR_VAR_2}！\p如果我们组队，那就太棒了，\n你觉得呢？$
```

### 18. BattleFrontier_Lounge5_Text_LadyClaimsSheUnderstandsPokemon

判定：**建议修复**；范围：日版和美版。

理由：シャレた / charming可译有意思、俏皮，不是魔法；日文说懂得宝可梦的心情，而非一定听懂语言。

建议处理：采用“真有意思！\n那边那位小女孩说她能\l懂得宝可梦的心情！”。

当前日版中文：

来源：`patch/batches/399_frontier_lounge5.json`

```text
好像魔法一样啊！\n那边那位小女孩说她能\l懂得宝可梦在说什么！
```

当前美版中文：

来源：`data/maps/BattleFrontier_Lounge5/scripts.inc`

```text
好像魔法一样啊！
那边那位小女孩说她能\l懂得宝可梦在说什么！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08239538`

```text
ポケモンの　きもちが　わかるとは\nあの　おじょうちゃん　なかなか\lシャレた　ことを　もうしますな!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_Lounge5/scripts.inc`，版本：`fe570a7e5^`

```text
How charming!
That little lady claims she can\lunderstand POKéMON!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：ポケモンの　きもちが　わかるとは\nあの　おじょうちゃん　なかなか\lシャレた　ことを　もうしますな！$
- EN：How charming!\nThat little lady claims she can\lunderstand POKéMON!$
- 中文：好像魔法一样啊！\n那边那位小女孩说她能\l懂得宝可梦在说什么！$
- 理由：JP「なかなか シャレた ことを もうしますな(真会说俏皮话)」与EN「How charming!」均为赞赏机灵，补丁中文「好像魔法一样啊」将「シャレた(机灵/俏皮)」误作「魔法」，语义错误。
- 修改建议：真有意思！\n那边那位小女孩说她能\l懂得宝可梦的心情！$
```

### 19. BattleFrontier_OutsideEast_Text_ThriveInDarkness

判定：**建议修复：报告只解决一半**；范围：日版和美版。

理由：喜欢黑暗的开头已经修好；后半段仍把“要不要在黑暗中摸索”的邀请改成询问是否绝望。日文0x08222D54末尾“さまよってみない？”、完整英文What say you to wandering都证实是邀请。

建议处理：保留已修的开头；后段按日文改为“喂……你也要不要到黑暗中\n拼命摸索一番……？”；美版应保留其desperation含义但恢复邀请句式，不强求区域措辞完全相同。

当前日版中文：

来源：`patch/batches/227_battle_frontier_outside_east.json`

```text
我最喜欢黑暗……\n是的……哪里最适合我？\l必然是对战金字塔……\p在黑暗中探索的时候\n你是不是也会陷入完全的绝望？
```

当前美版中文：

来源：`data/maps/BattleFrontier_OutsideEast/scripts.inc`

```text
我最喜欢黑暗……
是的……哪里最适合我？\l必然是对战金字塔……\p在黑暗中探索的时候
你是不是也会陷入完全的绝望？$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08222D54`

```text
くらやみが　だいすきな　わたし……\nそう……　わたしに　ふさわしい　のは……\lやはり　この　バトルピラミッド……\pネ……　あなたも　くらやみの　なかを\nひっしに　さまよって　みない……?
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_OutsideEast/scripts.inc`，版本：`fe570a7e5^`

```text
I thrive in darkness…
Yes… What is worthy of me?\lNone other than the BATTLE PYRAMID…\pWhat say you to wandering in darkness
and in utter and total desperation?$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：くらやみが　だいすきな　わたし⋯⋯\nそう⋯⋯　わたしに　ふさわしい　のは⋯⋯\lやはり　この　バトルピラミッド⋯⋯\pネ⋯⋯　あなたも　くらやみの　なかを\nひっしに　さまよって　みない⋯⋯？$
- EN：I thrive in darkness…\nYes… What is worthy of me?\lNone other than the BATTLE PYRAMID…\pWhat say you to wandering in dar
- 中文：我是在黑暗中长大的……\n是的……哪里最适合我？\l必然是对战金字塔……\p在黑暗中探索的时候\n你是不是也会陷入完全的绝望？$
- 理由：JP「くらやみが だいすきな わたし(我最喜欢黑暗)」与EN「I thrive in darkness」均为喜爱/沉浸于黑暗，补丁中文「我是在黑暗中长大的」将「だいすき(喜爱)」误作「长大」，语义错误。
- 修改建议：我最喜欢黑暗了……\n是的……哪里最适合我？\l必然是对战金字塔……\p在黑暗中探索的时候\n你是不是也会陷入完全的绝望？$
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 6921,
    "decision": "fixed_verified",
    "review": {
      "row_number": 6921,
      "symbol": "BattleFrontier_OutsideEast_Text_ThriveInDarkness",
      "domain": "ported_batch",
      "idx": "5669",
      "old": "我是在黑暗中长大的……",
      "new": "我最喜欢黑暗……",
      "reason": "JP大好き / EN thrive 不表示童年成长地点。",
      "scope": "both",
      "action": "fix",
      "final_text": "我最喜欢黑暗……\n是的……哪里最适合我？\\l必然是对战金字塔……\\p在黑暗中探索的时候\n你是不是也会陷入完全的绝望？",
      "old_current_text": "我是在黑暗中长大的……\n是的……哪里最适合我？\\l必然是对战金字塔……\\p在黑暗中探索的时候\n你是不是也会陷入完全的绝望？",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/BattleFrontier_OutsideEast/scripts.inc",
        "patch/batches/227_battle_frontier_outside_east.json"
      ],
      "us_source_file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
          "text": "くらやみが　だいすきな　わたし⋯⋯\nそう⋯⋯　わたしに　ふさわしい　のは⋯⋯\\lやはり　この　バトルピラミッド⋯⋯\\pネ⋯⋯　あなたも　くらやみの　なかを\nひっしに　さまよって　みない⋯⋯？$"
        }
      ]
    }
  }
]
```

### 20. DewfordTown_Gym_Text_BrendenIntro

判定：**建议修复**；范围：日版和美版。

理由：いじ / gumption偏骨气、胆识和决心，不是智慧。

建议处理：采用“让你看看\n水手的骨气！”。

当前日版中文：

来源：`patch/batches/023_dewford_gym.json`

```text
让你看看\n水手的智慧！
```

当前美版中文：

来源：`data/maps/DewfordTown_Gym/scripts.inc`

```text
让你看看
水手的智慧！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x081F3395`

```text
うみの　おとこの　いじを\nみせつけて　やるぜぃ!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/DewfordTown_Gym/scripts.inc`，版本：`fe570a7e5^`

```text
I'll show you the gumption of
a sailing man!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：うみの　おとこの　いじを
みせつけて　やるぜぃ!
- EN：I'll show you the gumption of\na sailing man!$
- 中文：让你看看\n水手的智慧！$
- 理由：JP「うみの おとこの いじ(海之男儿的骨气/意气)」与EN「the gumption of a sailing man」均指骨气胆识，补丁中文「水手的智慧」将「いじ(意气)」误作「智慧」，语义错误。
- 修改建议：让你看看\n海之男儿的骨气！$
```

### 21. EverGrandeCity_PokemonCenter_1F_Text_LeagueAfterVictoryRoad

判定：**已修复**；范围：日版和美版。

理由：两版当前已为“已经走了这么远，\n只能继续前进了！”。

建议处理：无需重复修改。

当前日版中文：

来源：`patch/batches/196_pokemon_centers.json`

```text
穿过冠军之路，\n宝可梦联盟就在眼前。\p已经走了这么远，\n只能继续前进了！
```

当前美版中文：

来源：`data/maps/EverGrandeCity_PokemonCenter_1F/scripts.inc`

```text
穿过冠军之路，
宝可梦联盟就在眼前。\p已经走了这么远，
只能继续前进了！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x082114A2`

```text
ポケモンリ-グは\nチャンピオンロ-ドを　ぬけると　すぐ!\pここまで　きたら\nまえに　すすむしかないわ!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/EverGrandeCity_PokemonCenter_1F/scripts.inc`，版本：`fe570a7e5^`

```text
The POKéMON LEAGUE is only a short
distance after the VICTORY ROAD.\pIf you've come this far, what choice
do you have but to keep going?$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：ポケモンリ-グは
チャンピオンロ-ドを　ぬけると　すぐ!\pここまで　きたら
まえに　すすむしかないわ!
- EN：The POKéMON LEAGUE is only a short\ndistance after the VICTORY ROAD.\pIf you've come this far, what choice\ndo you have
- 中文：穿过冠军之路，\n宝可梦联盟就在眼前。\p已经走了这么远，\n到底是什么让你坚持到现在？$
- 理由：JP「ここまで きたら まえに すすむしかないわ(走到这一步，除了继续前进别无选择)」与EN「what choice do you have but to keep going」均为敦促继续前进的反问；补丁中文「到底是什么让你坚持到现在？」将反问改作追问坚持的原因，语义错误。
- 修改建议：穿过冠军之路，\n宝可梦联盟就在眼前。\p已经走了这么远，\n除了继续前进别无选择！$
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 5772,
    "decision": "fixed_verified",
    "review": {
      "row_number": 5772,
      "symbol": "EverGrandeCity_PokemonCenter_1F_Text_LeagueAfterVictoryRoad",
      "domain": "ported_batch",
      "idx": "4520",
      "old": "到底是什么让你坚持到现在？",
      "new": "只能继续前进了！",
      "reason": "原文只能继续前进，不是询问动机。",
      "scope": "both",
      "action": "fix",
      "final_text": "穿过冠军之路，\n宝可梦联盟就在眼前。\\p已经走了这么远，\n只能继续前进了！",
      "old_current_text": "穿过冠军之路，\n宝可梦联盟就在眼前。\\p已经走了这么远，\n到底是什么让你坚持到现在？",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/EverGrandeCity_PokemonCenter_1F/scripts.inc",
        "patch/batches/196_pokemon_centers.json"
      ],
      "us_source_file": "data/maps/EverGrandeCity_PokemonCenter_1F/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/EverGrandeCity_PokemonCenter_1F/scripts.inc",
          "text": "ポケモンリーグは\nチャンピオンロードを　ぬけると　すぐ！\\pここまで　きたら\nまえに　すすむしかないわ！$"
        }
      ]
    }
  }
]
```

### 22. FortreeCity_House1_Text_GoingToMakeVolbeatStrong

判定：**建议修复**；范围：日版和美版。

理由：つよくしてやってよ / do the same承接的是把宝可梦养强；单说善待遗漏训练变强。

建议处理：后句改为“你也要把正电拍拍\n养得壮壮的啊！”；不修改交换获得宝可梦的数据或名字。

当前日版中文：

来源：`patch/batches/107_fortreecity_house1.json`

```text
从现在开始，我要把甜甜萤\n养得壮壮的！\p你也要善待正电拍拍啊！
```

当前美版中文：

来源：`data/maps/FortreeCity_House1/scripts.inc`

```text
从现在开始，我要把甜甜萤
养得壮壮的！\p你也要善待正电拍拍啊！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08204334`

```text
よし　いまから\nバルビ-トを　つよく　するぞ-!\lプラスルも　つよく　してやってよ!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/FortreeCity_House1/scripts.inc`，版本：`fe570a7e5^`

```text
I'm going to make VOLBEAT super
strong from this moment on!\pI hope you do the same with PLUSLE!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：よし　いまから
バルビ-トを　つよく　するぞ-!\lプラスルも　つよく　してやってよ!
- EN：I'm going to make VOLBEAT super\nstrong from this moment on!\pI hope you do the same with PLUSLE!$
- 中文：从现在开始，我要把甜甜萤\n养得壮壮的！\p你也要善待正电拍拍啊！$
- 理由：JP「バルビ-トを つよく するぞ-! プラスルも つよく してやってよ(也要把正电拍拍变强)」与EN「I hope you do the same with PLUSLE!(同样把PLUSLE变强)」均为「变强」；补丁中文与美版中文均为「你也要善待正电拍拍啊」，将「变强」误作「善待」，语义错误。
- 修改建议：从现在开始，我要把甜甜萤\n养得壮壮的！\p你也要把正电拍拍养得壮壮的啊！
```

### 23. FortreeCity_House3_Text_MetStevenHadAmazingPokemon

判定：**已修复**；范围：日版和美版。

理由：两版当前均已把“它们不止是强大”改为“它们不止是稀有”。

建议处理：当前后句表达训练至极致，与原意一致；无需重复改写。

当前日版中文：

来源：`patch/batches/245_fortree_city_house3.json`

```text
说到宝可梦图鉴，\n我想起来了，\p我寻找稀有石头的时候\n遇到了那个叫大吾的训练家。\p哈，他带着一些\n奇妙的宝可梦，\p它们不止是稀有，\n还在训练中发挥到了极致！\p他也许比这城镇的\n道馆馆主还要强……
```

当前美版中文：

来源：`data/maps/FortreeCity_House3/scripts.inc`

```text
说到宝可梦图鉴，
我想起来了，\p我寻找稀有石头的时候
遇到了那个叫大吾的训练家。\p哈，他带着一些
奇妙的宝可梦，\p它们不止是稀有，
还在训练中发挥到了极致！\p他也许比这城镇的
道馆馆主还要强……$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x082050E3`

```text
ポケモンずかんで\nおもいだした　ことが　あるよ\pめずらしい　いしを　さがしてるとき\nダイゴって　トレ-ナ-と　であったけど\lあいつの　ポケモン　すごいね!\pめずらしい　だけでなく\nおそろしいほど　きたえられてた!\pもしかしたら　この　まちの\nジムリ-ダ-よりも　つよいかも……
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/FortreeCity_House3/scripts.inc`，版本：`fe570a7e5^`

```text
While speaking about POKéDEXES,
I remembered something.\pI met this TRAINER, STEVEN, when
I was searching for rare stones.\pHoo, boy, he had some amazing POKéMON
with him.\pThey weren't just rare, they were
trained to terrifying extremes!\pHe might even be stronger than the
GYM LEADER in this town…$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：ポケモンずかんで
おもいだした　ことが　あるよ\pめずらしい　いしを　さがしてるとき
ダイゴって　トレ-ナ-と　であったけど\lあいつの　ポケモン　すごいね!\pめずらしい　だけでなく
おそろしいほど　きたえられてた!\pもしかしたら　この
- EN：While speaking about POKéDEXES,\nI remembered something.\pI met this TRAINER, STEVEN, when\nI was searching for rare sto
- 中文：说到宝可梦图鉴，\n我想起来了，\p我寻找稀有石头的时候\n遇到了那个叫大吾的训练家。\p哈，他带着一些\n奇妙的宝可梦，\p它们不止是强大，\n还在训练中发挥到了极致！\p他也许比这城镇的\n道馆馆主还要强……$
- 理由：JP「めずらしい だけでなく おそろしいほど きたえられてた(不只是稀有，还被锻炼到了可怕的地步)」与EN「They weren't just rare, they were trained to terrifying extremes」关键形容词是「稀有」；补丁中文与美版中文均为「它们不止是强大，还在训练中发挥到了极致」，将「稀有」误作「强大」，语义错误。
- 修改建议：它们不只是稀有，\n还被锻炼到了可怕的地步！

### 语义反转（8 条）
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 7069,
    "decision": "fixed_verified",
    "review": {
      "row_number": 7069,
      "symbol": "FortreeCity_House3_Text_MetStevenHadAmazingPokemon",
      "domain": "ported_batch",
      "idx": "5817",
      "old": "它们不止是强大，",
      "new": "它们不止是稀有，",
      "reason": "rare / 珍しい 指稀有。",
      "scope": "both",
      "action": "fix",
      "final_text": "说到宝可梦图鉴，\n我想起来了，\\p我寻找稀有石头的时候\n遇到了那个叫大吾的训练家。\\p哈，他带着一些\n奇妙的宝可梦，\\p它们不止是稀有，\n还在训练中发挥到了极致！\\p他也许比这城镇的\n道馆馆主还要强……",
      "old_current_text": "说到宝可梦图鉴，\n我想起来了，\\p我寻找稀有石头的时候\n遇到了那个叫大吾的训练家。\\p哈，他带着一些\n奇妙的宝可梦，\\p它们不止是强大，\n还在训练中发挥到了极致！\\p他也许比这城镇的\n道馆馆主还要强……",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/FortreeCity_House3/scripts.inc",
        "patch/batches/245_fortree_city_house3.json"
      ],
      "us_source_file": "data/maps/FortreeCity_House3/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/FortreeCity_House3/scripts.inc",
          "text": "ポケモンずかんで\nおもいだした　ことが　あるよ\\pめずらしい　いしを　さがしてるとき\nダイゴって　トレーナーと　であったけど\\lあいつの　ポケモン　すごいね！\\pめずらしい　だけでなく\nおそろしいほど　きたえられてた！\\pもしかしたら　この　まちの\nジムリーダーよりも　つよいかも⋯⋯$"
        }
      ]
    }
  }
]
```

### 24. BattlePyramid_Text_FiveTrainersRemaining2

判定：**已修复**；范围：日版和美版。

理由：当前两版此人数模板已改为一定有人能打败玩家；单人模板为“他一定会打败你”。不再有“比你弱”的反转。

建议处理：保留现有1～7人分别对应的数字、代词和控制符，不照抄报告把全体都断言为能打败玩家。

当前日版中文：

来源：`patch/batches/437_checklist_reviewed_indirect_tables.json`

```text
真不幸！\p后面还有5位训练家！\n他们中一定有人能打败你！
```

当前美版中文：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`

```text
真不幸！\p后面还有5位训练家！
他们中一定有人能打败你！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0822E429`

```text
くやしい-!\pでも　あと　5にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，版本：`fe570a7e5^`

```text
This is so upsetting!\pBut there are five TRAINERS left!
Someone will humble you!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：くやしいー！\pでも　あと　5にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there are five TRAINERS left!\nSomeone will humble you!$
- 中文：真不幸！\p后面还有5位训练家！\n他们中或许有人比你弱！$
- 理由：JP「あと 5にん いる トレーナーが きっと たおしてくれるわ(剩下的5个训练家一定会打败你)」与EN「Someone will humble you!(有人会让你吃瘪)」均为对手将获胜；补丁中文「他们中或许有人比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有5位训练家！\n他们一定会打败你的！$
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 12013,
    "decision": "fixed_verified",
    "review": {
      "row_number": 12013,
      "symbol": "BattlePyramid_Text_FiveTrainersRemaining2",
      "domain": "untransplanted_full",
      "idx": "",
      "old": "他们中或许有人比你弱！",
      "new": "他们中一定有人能打败你！",
      "reason": "原文有人会打败玩家，不是比玩家弱。",
      "scope": "both",
      "action": "fix",
      "final_text": "真不幸！\\p后面还有5位训练家！\n他们中一定有人能打败你！",
      "old_current_text": "真不幸！\\p后面还有5位训练家！\n他们中或许有人比你弱！",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "patch/batches/437_checklist_reviewed_indirect_tables.json"
      ],
      "us_source_file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
          "text": "くやしいー！\\pでも　あと　5にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
        }
      ]
    }
  }
]
```

### 25. BattlePyramid_Text_FourTrainersRemaining2

判定：**已修复**；范围：日版和美版。

理由：当前两版此人数模板已改为一定有人能打败玩家；单人模板为“他一定会打败你”。不再有“比你弱”的反转。

建议处理：保留现有1～7人分别对应的数字、代词和控制符，不照抄报告把全体都断言为能打败玩家。

当前日版中文：

来源：`patch/batches/437_checklist_reviewed_indirect_tables.json`

```text
真不幸！\p后面还有4位训练家！\n他们中一定有人能打败你！
```

当前美版中文：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`

```text
真不幸！\p后面还有4位训练家！
他们中一定有人能打败你！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0822E451`

```text
くやしい-!\pでも　あと　4にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，版本：`fe570a7e5^`

```text
This is so upsetting!\pBut there are four TRAINERS left!
Someone will humble you!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：くやしいー！\pでも　あと　4にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there are four TRAINERS left!\nSomeone will humble you!$
- 中文：真不幸！\p后面还有4位训练家！\n他们中或许有人比你弱！$
- 理由：JP「あと 4にん いる トレーナーが きっと たおしてくれるわ(剩下的4个训练家一定会打败你)」与EN「Someone will humble you!」均为对手将获胜；补丁中文「他们中或许有人比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有4位训练家！\n他们一定会打败你的！$
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 12014,
    "decision": "fixed_verified",
    "review": {
      "row_number": 12014,
      "symbol": "BattlePyramid_Text_FourTrainersRemaining2",
      "domain": "untransplanted_full",
      "idx": "",
      "old": "他们中或许有人比你弱！",
      "new": "他们中一定有人能打败你！",
      "reason": "原文有人会打败玩家，不是比玩家弱。",
      "scope": "both",
      "action": "fix",
      "final_text": "真不幸！\\p后面还有4位训练家！\n他们中一定有人能打败你！",
      "old_current_text": "真不幸！\\p后面还有4位训练家！\n他们中或许有人比你弱！",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "patch/batches/437_checklist_reviewed_indirect_tables.json"
      ],
      "us_source_file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
          "text": "くやしいー！\\pでも　あと　4にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
        }
      ]
    }
  }
]
```

### 26. BattlePyramid_Text_OneTrainersRemaining2

判定：**已修复**；范围：日版和美版。

理由：当前两版此人数模板已改为一定有人能打败玩家；单人模板为“他一定会打败你”。不再有“比你弱”的反转。

建议处理：保留现有1～7人分别对应的数字、代词和控制符，不照抄报告把全体都断言为能打败玩家。

当前日版中文：

来源：`patch/batches/437_checklist_reviewed_indirect_tables.json`

```text
真不幸！\p后面还有1位训练家！\n他一定会打败你！
```

当前美版中文：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`

```text
真不幸！\p后面还有1位训练家！
他一定会打败你！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0822E4C9`

```text
くやしい-!\pでも　あと　1にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，版本：`fe570a7e5^`

```text
This is so upsetting!\pBut there's one TRAINER left!
I'm sure you will be humbled!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：くやしいー！\pでも　あと　1にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there's one TRAINER left!\nI'm sure you will be humbled!$
- 中文：真不幸！\p后面还有1位训练家！\n他或许比你弱！$
- 理由：JP「あと 1にん いる トレーナーが きっと たおしてくれるわ(剩下的1个训练家一定会打败你)」与EN「I'm sure you will be humbled!」均为对手将获胜；补丁中文「他或许比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有1位训练家！\n他一定会打败你的！$
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 12017,
    "decision": "fixed_verified",
    "review": {
      "row_number": 12017,
      "symbol": "BattlePyramid_Text_OneTrainersRemaining2",
      "domain": "untransplanted_full",
      "idx": "",
      "old": "他或许比你弱！",
      "new": "他一定会打败你！",
      "reason": "同系列单人模板恢复原意。",
      "scope": "both",
      "action": "fix",
      "final_text": "真不幸！\\p后面还有1位训练家！\n他一定会打败你！",
      "old_current_text": "真不幸！\\p后面还有1位训练家！\n他或许比你弱！",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "patch/batches/437_checklist_reviewed_indirect_tables.json"
      ],
      "us_source_file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
          "text": "くやしいー！\\pでも　あと　1にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
        }
      ]
    }
  }
]
```

### 27. BattlePyramid_Text_SevenTrainersRemaining2

判定：**已修复**；范围：日版和美版。

理由：当前两版此人数模板已改为一定有人能打败玩家；单人模板为“他一定会打败你”。不再有“比你弱”的反转。

建议处理：保留现有1～7人分别对应的数字、代词和控制符，不照抄报告把全体都断言为能打败玩家。

当前日版中文：

来源：`patch/batches/437_checklist_reviewed_indirect_tables.json`

```text
真不幸！\p后面还有7位训练家！\n他们中一定有人能打败你！
```

当前美版中文：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`

```text
真不幸！\p后面还有7位训练家！
他们中一定有人能打败你！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0822E3D9`

```text
くやしい-!\pでも　あと　7にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，版本：`fe570a7e5^`

```text
This is so upsetting!\pBut there are seven TRAINERS left!
Someone will humble you!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：くやしいー！\pでも　あと　7にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there are seven TRAINERS left!\nSomeone will humble you!$
- 中文：真不幸！\p后面还有7位训练家！\n他们中或许有人比你弱！$
- 理由：JP「あと 7にん いる トレーナーが きっと たおしてくれるわ(剩下的7个训练家一定会打败你)」与EN「Someone will humble you!」均为对手将获胜；补丁中文「他们中或许有人比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有7位训练家！\n他们一定会打败你的！$
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 12011,
    "decision": "fixed_verified",
    "review": {
      "row_number": 12011,
      "symbol": "BattlePyramid_Text_SevenTrainersRemaining2",
      "domain": "untransplanted_full",
      "idx": "",
      "old": "他们中或许有人比你弱！",
      "new": "他们中一定有人能打败你！",
      "reason": "原文有人会打败玩家，不是比玩家弱。",
      "scope": "both",
      "action": "fix",
      "final_text": "真不幸！\\p后面还有7位训练家！\n他们中一定有人能打败你！",
      "old_current_text": "真不幸！\\p后面还有7位训练家！\n他们中或许有人比你弱！",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "patch/batches/437_checklist_reviewed_indirect_tables.json"
      ],
      "us_source_file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
          "text": "くやしいー！\\pでも　あと　7にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
        }
      ]
    }
  }
]
```

### 28. BattlePyramid_Text_SixTrainersRemaining2

判定：**已修复**；范围：日版和美版。

理由：当前两版此人数模板已改为一定有人能打败玩家；单人模板为“他一定会打败你”。不再有“比你弱”的反转。

建议处理：保留现有1～7人分别对应的数字、代词和控制符，不照抄报告把全体都断言为能打败玩家。

当前日版中文：

来源：`patch/batches/437_checklist_reviewed_indirect_tables.json`

```text
真不幸！\p后面还有6位训练家！\n他们中一定有人能打败你！
```

当前美版中文：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`

```text
真不幸！\p后面还有6位训练家！
他们中一定有人能打败你！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0822E401`

```text
くやしい-!\pでも　あと　6にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，版本：`fe570a7e5^`

```text
This is so upsetting!\pBut there are six TRAINERS left!
Someone will humble you!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：くやしいー！\pでも　あと　6にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there are six TRAINERS left!\nSomeone will humble you!$
- 中文：真不幸！\p后面还有6位训练家！\n他们中或许有人比你弱！$
- 理由：JP「あと 6にん いる トレーナーが きっと たおしてくれるわ(剩下的6个训练家一定会打败你)」与EN「Someone will humble you!」均为对手将获胜；补丁中文「他们中或许有人比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有6位训练家！\n他们一定会打败你的！$
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 12012,
    "decision": "fixed_verified",
    "review": {
      "row_number": 12012,
      "symbol": "BattlePyramid_Text_SixTrainersRemaining2",
      "domain": "untransplanted_full",
      "idx": "",
      "old": "他们中或许有人比你弱！",
      "new": "他们中一定有人能打败你！",
      "reason": "原文有人会打败玩家，不是比玩家弱。",
      "scope": "both",
      "action": "fix",
      "final_text": "真不幸！\\p后面还有6位训练家！\n他们中一定有人能打败你！",
      "old_current_text": "真不幸！\\p后面还有6位训练家！\n他们中或许有人比你弱！",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "patch/batches/437_checklist_reviewed_indirect_tables.json"
      ],
      "us_source_file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
          "text": "くやしいー！\\pでも　あと　6にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
        }
      ]
    }
  }
]
```

### 29. BattlePyramid_Text_ThreeTrainersRemaining2

判定：**已修复**；范围：日版和美版。

理由：当前两版此人数模板已改为一定有人能打败玩家；单人模板为“他一定会打败你”。不再有“比你弱”的反转。

建议处理：保留现有1～7人分别对应的数字、代词和控制符，不照抄报告把全体都断言为能打败玩家。

当前日版中文：

来源：`patch/batches/437_checklist_reviewed_indirect_tables.json`

```text
真不幸！\p后面还有3位训练家！\n他们中一定有人能打败你！
```

当前美版中文：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`

```text
真不幸！\p后面还有3位训练家！
他们中一定有人能打败你！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0822E479`

```text
くやしい-!\pでも　あと　3にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，版本：`fe570a7e5^`

```text
This is so upsetting!\pBut there are three TRAINERS left!
Someone will humble you!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：くやしいー！\pでも　あと　3にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there are three TRAINERS left!\nSomeone will humble you!$
- 中文：真不幸！\p后面还有3位训练家！\n他们中或许有人比你弱！$
- 理由：JP「あと 3にん いる トレーナーが きっと たおしてくれるわ(剩下的3个训练家一定会打败你)」与EN「Someone will humble you!」均为对手将获胜；补丁中文「他们中或许有人比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有3位训练家！\n他们一定会打败你的！$
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 12015,
    "decision": "fixed_verified",
    "review": {
      "row_number": 12015,
      "symbol": "BattlePyramid_Text_ThreeTrainersRemaining2",
      "domain": "untransplanted_full",
      "idx": "",
      "old": "他们中或许有人比你弱！",
      "new": "他们中一定有人能打败你！",
      "reason": "原文有人会打败玩家，不是比玩家弱。",
      "scope": "both",
      "action": "fix",
      "final_text": "真不幸！\\p后面还有3位训练家！\n他们中一定有人能打败你！",
      "old_current_text": "真不幸！\\p后面还有3位训练家！\n他们中或许有人比你弱！",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "patch/batches/437_checklist_reviewed_indirect_tables.json"
      ],
      "us_source_file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
          "text": "くやしいー！\\pでも　あと　3にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
        }
      ]
    }
  }
]
```

### 30. BattlePyramid_Text_TwoTrainersRemaining2

判定：**已修复**；范围：日版和美版。

理由：当前两版此人数模板已改为一定有人能打败玩家；单人模板为“他一定会打败你”。不再有“比你弱”的反转。

建议处理：保留现有1～7人分别对应的数字、代词和控制符，不照抄报告把全体都断言为能打败玩家。

当前日版中文：

来源：`patch/batches/437_checklist_reviewed_indirect_tables.json`

```text
真不幸！\p后面还有2位训练家！\n他们中一定有人能打败你！
```

当前美版中文：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`

```text
真不幸！\p后面还有2位训练家！
他们中一定有人能打败你！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0822E4A1`

```text
くやしい-!\pでも　あと　2にん　いる　トレ-ナ-が\nきっと　たおしてくれるわ
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc`，版本：`fe570a7e5^`

```text
This is so upsetting!\pBut there are two TRAINERS left!
Someone will humble you!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：くやしいー！\pでも　あと　2にん　いる　トレーナーが\nきっと　たおしてくれるわ$
- EN：This is so upsetting!\pBut there are two TRAINERS left!\nSomeone will humble you!$
- 中文：真不幸！\p后面还有2位训练家！\n他们中或许有人比你弱！$
- 理由：JP「あと 2にん いる トレーナーが きっと たおしてくれるわ(剩下的2个训练家一定会打败你)」与EN「Someone will humble you!」均为对手将获胜；补丁中文「他们中或许有人比你弱」将「对手打败你」反转为「对手比你弱」，语义完全反转。
- 修改建议：真不幸！\p后面还有2位训练家！\n他们一定会打败你的！$
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 12016,
    "decision": "fixed_verified",
    "review": {
      "row_number": 12016,
      "symbol": "BattlePyramid_Text_TwoTrainersRemaining2",
      "domain": "untransplanted_full",
      "idx": "",
      "old": "他们中或许有人比你弱！",
      "new": "他们中一定有人能打败你！",
      "reason": "原文有人会打败玩家，不是比玩家弱。",
      "scope": "both",
      "action": "fix",
      "final_text": "真不幸！\\p后面还有2位训练家！\n他们中一定有人能打败你！",
      "old_current_text": "真不幸！\\p后面还有2位训练家！\n他们中或许有人比你弱！",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "patch/batches/437_checklist_reviewed_indirect_tables.json"
      ],
      "us_source_file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
          "text": "くやしいー！\\pでも　あと　2にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
        }
      ]
    }
  }
]
```

### 31. LilycoveCity_PokemonTrainerFanClub_Text_YoureOneWeWantToWin

判定：**建议修复**；范围：日版和美版。

理由：おうえんしてる / want you to win是给主角加油，不是希望击败主角。

建议处理：改为“嗨，{PLAYER}！\n我们希望你能获胜！”；保留玩家名占位符。

当前日版中文：

来源：`patch/batches/139_lilycovecity_pokemontrainerfanclub.json`

```text
嗨，{FD_01}！\n我们一直想要胜过你！
```

当前美版中文：

来源：`data/maps/LilycoveCity_PokemonTrainerFanClub/scripts.inc`

```text
嗨，{PLAYER}！
我们一直想要胜过你！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08208BEC`

```text
おう　{PLACEHOLDER_01}!!\nおうえん　してるぞ!!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/LilycoveCity_PokemonTrainerFanClub/scripts.inc`，版本：`fe570a7e5^`

```text
Yo, {PLAYER}!
You're the one we want to win!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：おう　{FD:01}!!
おうえん　してるぞ!!
- EN：Yo, {PLAYER}!\nYou're the one we want to win!$
- 中文：嗨，{PLAYER}！\n我们一直想要胜过你！$
- 理由：JP「おう{FD:01}！！おうえんしてるぞ」/EN“You're the one we want to win!”意为“我们希望你赢、为你加油”，中文“我们一直想要胜过你！”把“希望你获胜”反转为“想要打败你”，语义完全颠倒。
- 修改建议：嗨，{PLAYER}！\n我们希望你能获胜！

### 错字（6 条）
```

### 32. GraniteCave_StevensRoom_Text_ImStevenLetterForMe

判定：**建议修复**；范围：日版和美版。

理由：当前两版都仍是“所有经常四处旅行”；因果句应为所以。

建议处理：仅将“所有”改为“所以”。

当前日版中文：

来源：`patch/batches/027_stevens_room.json`

```text
我的名字是大吾。\p我对稀有的石头很有兴趣，\n所有经常四处旅行。\p哦？\n有给我的信？
```

当前美版中文：

来源：`data/maps/GraniteCave_StevensRoom/scripts.inc`

```text
我的名字是大吾。\p我对稀有的石头很有兴趣，
所有经常四处旅行。\p哦？
有给我的信？$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08214107`

```text
ボクの　なまえは　ダイゴ\pめずらしい　いしに　きょうみが　あって\nあちこち　たび　してるんだよ\pえっ?\nボクに　てがみ……?
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/GraniteCave_StevensRoom/scripts.inc`，版本：`fe570a7e5^`

```text
My name is STEVEN.\pI'm interested in rare stones,
so I travel here and there.\pOh?
A LETTER for me?$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：ボクの　なまえは　ダイゴ\pめずらしい　いしに　きょうみが　あって
あちこち　たび　してるんだよ\pえっ?
ボクに　てがみ……?
- EN：My name is STEVEN.\pI'm interested in rare stones,\nso I travel here and there.\pOh?\nA LETTER for me?$
- 中文：我的名字是大吾。\p我对稀有的石头很有兴趣，\n所有经常四处旅行。\p哦？\n有给我的信？$
- 理由：JP「めずらしいいしにきょうみがあってあちこちたびしてるんだよ」/EN“I'm interested in rare stones, so I travel”意为“对稀有石头感兴趣，所以经常四处旅行”，中文“所有经常四处旅行”中“所有”系“所以”之误，美版中文同样错写。
- 修改建议：我的名字是大吾。\p我对稀有的石头很有兴趣，\n所以经常四处旅行。\p哦？\n有给我的信？
```

### 33. MossdeepCity_StevensHouse_Text_LetterFromSteven

判定：**已修复**；范围：日版和美版。

理由：当前两版已为“我已决定”，语序正确。

建议处理：无需重复修改。

当前日版中文：

来源：`patch/batches/159_mossdeepcity_stevenshouse.json`

```text
是一封信。\p…… …… ……\p致{FD_01}{FD_05}……\p我已决定踏上自我\n探索与修行之旅。\p短时间内不\n打算回家，\p我想拜托你收下\n桌上的精灵球，\p里面是我最喜欢的宝可梦——\n铁哑铃，\p拜托你照顾好它。\p愿你我终有相逢之日。\p大吾·兹伏奇
```

当前美版中文：

来源：`data/maps/MossdeepCity_StevensHouse/scripts.inc`

```text
是一封信。\p…… …… ……\p致{PLAYER}{KUN}……\p我已决定踏上自我
探索与修行之旅。\p短时间内不
打算回家，\p我想拜托你收下
桌上的精灵球，\p里面是我最喜欢的宝可梦——
铁哑铃，\p拜托你照顾好它。\p愿你我终有相逢之日。\p大吾·兹伏奇$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0820CB77`

```text
てがみが　ある!\p……　……　……\n……　……　……\p{PLACEHOLDER_01}{PLACEHOLDER_05}へ\pボクは　おもうことが　あって\nしばらく　しゅぎょうを　つづける\lとうぶん　いえに　かえらない\pそこで　おねがいだ\pつくえの　うえにある\nモンスタ-ボ-ルを　うけとって　ほしい\pなかに　いるのは　ダンバルといって\nボクの　おきにいりの　ポケモンだから\pよろしく　たのむよ\pでは　また　いつか　あおう!\n　　　　　　ツワブキ　ダイゴより
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/MossdeepCity_StevensHouse/scripts.inc`，版本：`fe570a7e5^`

```text
It's a letter.\p… … … … … …\pTo {PLAYER}{KUN}…\pI've decided to do a little soul-
searching and train on the road.\pI don't plan to return home for some
time.\pI have a favor to ask of you.\pI want you to take the POKé BALL on
the desk.\pInside it is a BELDUM, my favorite
POKéMON.\pI'm counting on you.\pMay our paths cross someday.\pSTEVEN STONE$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：てがみが　ある!\p……　……　……
……　……　……\p{FD:01}{FD:05}へ\pボクは　おもうことが　あって
しばらく　しゅぎょうを　つづける\lとうぶん　いえに　かえらない\pそこで　おねがいだ\pつくえの　うえにある
モンス
- EN：It's a letter.\p… … … … … …\pTo {PLAYER}{KUN}…\pI've decided to do a little soul-\nsearching and train on the road.\pI d
- 中文：是一封信。\p…… …… ……\p致{PLAYER}{KUN}……\p已我决定踏上自我\n探索与修行之旅。\p短时间内不\n打算回家，\p我想拜托你收下\n桌上的精灵球，\p里面是我最喜欢的宝可梦——\n铁哑铃，\p拜托你照顾好它。\p愿你
- 理由：JP「ボクはおもうことがあってしばらくしゅぎょうをつづける（我有些想法，要继续修行一阵子）」/EN「I've decided to do a little soul-searching and train on the road」中「我已决定」被补丁/美版中文误作「已我决定」，「我」「已」二字顺序颠倒，属错字；其余「短时间内不打算回家」「收下桌上的精灵球」「里面是我最喜欢的宝可梦——铁哑铃」「愿你我终有相逢之日」语义一致。
- 修改建议：我已决定踏上自我探索与修行之旅。
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 4516,
    "decision": "fixed_verified",
    "review": {
      "row_number": 4516,
      "symbol": "MossdeepCity_StevensHouse_Text_LetterFromSteven",
      "domain": "ported_batch",
      "idx": "3261",
      "old": "已我决定",
      "new": "我已决定",
      "reason": "中文语序笔误。",
      "scope": "both",
      "action": "fix",
      "final_text": "是一封信。\\p…… …… ……\\p致{PLAYER}{KUN}……\\p我已决定踏上自我\n探索与修行之旅。\\p短时间内不\n打算回家，\\p我想拜托你收下\n桌上的精灵球，\\p里面是我最喜欢的宝可梦——\n铁哑铃，\\p拜托你照顾好它。\\p愿你我终有相逢之日。\\p大吾·兹伏奇",
      "old_current_text": "是一封信。\\p…… …… ……\\p致{PLAYER}{KUN}……\\p已我决定踏上自我\n探索与修行之旅。\\p短时间内不\n打算回家，\\p我想拜托你收下\n桌上的精灵球，\\p里面是我最喜欢的宝可梦——\n铁哑铃，\\p拜托你照顾好它。\\p愿你我终有相逢之日。\\p大吾·兹伏奇",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/MossdeepCity_StevensHouse/scripts.inc",
        "patch/batches/159_mossdeepcity_stevenshouse.json"
      ],
      "us_source_file": "data/maps/MossdeepCity_StevensHouse/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/MossdeepCity_StevensHouse/scripts.inc",
          "text": "てがみが　ある！\\p⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯\\p{PLAYER}{KUN}へ\\pボクは　おもうことが　あって\nしばらく　しゅぎょうを　つづける\\lとうぶん　いえに　かえらない\\pそこで　おねがいだ\\pつくえの　うえにある\nモンスターボールを　うけとって　ほしい\\pなかに　いるのは　ダンバルといって\nボクの　おきにいりの　ポケモンだから\\pよろしく　たのむよ\\pでは　また　いつか　あおう！\n　　　　　　ツワブキ　ダイゴより$"
        }
      ]
    }
  }
]
```

### 34. gTVPokemonNewsBattleFrontierText05

判定：**已修复**；范围：日版和美版。

理由：对战巨蛋此模板当前已去掉第二行重复的在。

建议处理：无需重复修改。

当前日版中文：

来源：`patch/batches/386_tv_0.json`

```text
训练家{FD_02}在\n对战巨蛋单打对战锦标赛中\l创造了{FD_03}连冠的新纪录。\p让我们为{FD_02}欢呼！
```

当前美版中文：

来源：`data/text/tv.inc`

```text
训练家{STR_VAR_1}在
对战巨蛋单打对战锦标赛中\l创造了{STR_VAR_2}连冠的新纪录。\p让我们为{STR_VAR_1}欢呼！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x082512C1`

```text
バトルド-ム\nシングル　バトルト-ナメントに\lちょうせんした　{PLACEHOLDER_02}さんが\l{PLACEHOLDER_03}　れんぱで\lきろくを　こうしん　しました!\p……{PLACEHOLDER_02}さん!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/tv.inc`，版本：`fe570a7e5^`

```text
The TRAINER {STR_VAR_1} set a new
{STR_VAR_2}-championship-streak record\lcompeting in the BATTLE DOME's\lSINGLE BATTLE Tournaments.\pHere's to {STR_VAR_1}!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：バトルドーム\nシングル　バトルトーナメントに\lちょうせんした　{STR_VAR_1}さんが\l{STR_VAR_2}　れんぱで\lきろくを　こうしん　しました！\p⋯⋯{STR_VAR_1}さん！$
- EN：The TRAINER {STR_VAR_1} set a new\n{STR_VAR_2}-championship-streak record\lcompeting in the BATTLE DOME's\lSINGLE BATTLE
- 中文：训练家{STR_VAR_1}在\n在对战巨蛋单打对战锦标赛中\l创造了{STR_VAR_2}连冠的新纪录。\p让我们为{STR_VAR_1}欢呼！$
- 理由：JP“バトルドーム シングル バトルトーナメントに ちょうせんした”/EN“competing in the BATTLE DOME's SINGLE BATTLE Tournaments”，中文“训练家{STR_VAR_1}在 在对战巨蛋单打对战锦标赛中”出现“在 在”重复。
- 修改建议：训练家{STR_VAR_1}在对战巨蛋单打对战锦标赛中创造了{STR_VAR_2}连冠的新纪录。让我们为{STR_VAR_1}欢呼！
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 8793,
    "decision": "fixed_verified",
    "review": {
      "row_number": 8793,
      "symbol": "gTVPokemonNewsBattleFrontierText05",
      "domain": "ported_batch",
      "idx": "7541",
      "old": "在\n在对战巨蛋",
      "new": "在\n对战巨蛋",
      "reason": "重复在。",
      "scope": "both",
      "action": "fix",
      "final_text": "训练家{STR_VAR_1}在\n对战巨蛋单打对战锦标赛中\\l创造了{STR_VAR_2}连冠的新纪录。\\p让我们为{STR_VAR_1}欢呼！",
      "old_current_text": "训练家{STR_VAR_1}在\n在对战巨蛋单打对战锦标赛中\\l创造了{STR_VAR_2}连冠的新纪录。\\p让我们为{STR_VAR_1}欢呼！",
      "changed_files": [
        "../pokeemerald_us_chs/data/text/tv.inc",
        "patch/batches/386_tv_0.json"
      ],
      "us_source_file": "data/text/tv.inc",
      "jp_source": [
        {
          "file": "data/text/tv/battle_frontier_news.inc",
          "text": "バトルドーム\nシングル　バトルトーナメントに\\lちょうせんした　{STR_VAR_1}さんが\\l{STR_VAR_2}　れんぱで\\lきろくを　こうしん　しました！\\p⋯⋯{STR_VAR_1}さん！$"
        }
      ]
    }
  }
]
```

### 35. gTVPokemonNewsBattleFrontierText06

判定：**已修复**；范围：日版和美版。

理由：对战巨蛋此模板当前已去掉第二行重复的在。

建议处理：无需重复修改。

当前日版中文：

来源：`patch/batches/386_tv_0.json`

```text
训练家{FD_02}在\n对战巨蛋双打对战锦标赛中\l创造了{FD_03}连冠的新纪录。\p让我们为{FD_02}欢呼！
```

当前美版中文：

来源：`data/text/tv.inc`

```text
训练家{STR_VAR_1}在
对战巨蛋双打对战锦标赛中\l创造了{STR_VAR_2}连冠的新纪录。\p让我们为{STR_VAR_1}欢呼！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08251306`

```text
バトルド-ム\nダブル　バトルト-ナメントに\lちょうせんした　{PLACEHOLDER_02}さんが\l{PLACEHOLDER_03}　れんぱで\lきろくを　こうしん　しました!\p……{PLACEHOLDER_02}さん!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/tv.inc`，版本：`fe570a7e5^`

```text
The TRAINER {STR_VAR_1} set a new
{STR_VAR_2}-championship-streak record\lcompeting in the BATTLE DOME's\lDOUBLE BATTLE Tournaments.\pHere's to {STR_VAR_1}!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：バトルドーム\nダブル　バトルトーナメントに\lちょうせんした　{STR_VAR_1}さんが\l{STR_VAR_2}　れんぱで\lきろくを　こうしん　しました！\p⋯⋯{STR_VAR_1}さん！$
- EN：The TRAINER {STR_VAR_1} set a new\n{STR_VAR_2}-championship-streak record\lcompeting in the BATTLE DOME's\lDOUBLE BATTLE
- 中文：训练家{STR_VAR_1}在\n在对战巨蛋双打对战锦标赛中\l创造了{STR_VAR_2}连冠的新纪录。\p让我们为{STR_VAR_1}欢呼！$
- 理由：同[120]，“训练家{STR_VAR_1}在 在对战巨蛋双打对战锦标赛中”出现“在 在”重复。
- 修改建议：训练家{STR_VAR_1}在对战巨蛋双打对战锦标赛中创造了{STR_VAR_2}连冠的新纪录。让我们为{STR_VAR_1}欢呼！
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 8794,
    "decision": "fixed_verified",
    "review": {
      "row_number": 8794,
      "symbol": "gTVPokemonNewsBattleFrontierText06",
      "domain": "ported_batch",
      "idx": "7542",
      "old": "在\n在对战巨蛋",
      "new": "在\n对战巨蛋",
      "reason": "重复在。",
      "scope": "both",
      "action": "fix",
      "final_text": "训练家{STR_VAR_1}在\n对战巨蛋双打对战锦标赛中\\l创造了{STR_VAR_2}连冠的新纪录。\\p让我们为{STR_VAR_1}欢呼！",
      "old_current_text": "训练家{STR_VAR_1}在\n在对战巨蛋双打对战锦标赛中\\l创造了{STR_VAR_2}连冠的新纪录。\\p让我们为{STR_VAR_1}欢呼！",
      "changed_files": [
        "../pokeemerald_us_chs/data/text/tv.inc",
        "patch/batches/386_tv_0.json"
      ],
      "us_source_file": "data/text/tv.inc",
      "jp_source": [
        {
          "file": "data/text/tv/battle_frontier_news.inc",
          "text": "バトルドーム\nダブル　バトルトーナメントに\\lちょうせんした　{STR_VAR_1}さんが\\l{STR_VAR_2}　れんぱで\\lきろくを　こうしん　しました！\\p⋯⋯{STR_VAR_1}さん！$"
        }
      ]
    }
  }
]
```

### 36. gTVPokemonNewsBattleFrontierText11

判定：**建议修复**；范围：日版和美版。

理由：对战宫殿此模板当前两版仍有“训练家…在\n在对战宫殿…”，与巨蛋模板不同，确实漏修。

建议处理：只删第二行开头多余的“在”；保留训练家名、连胜数及换页。

当前日版中文：

来源：`patch/batches/386_tv_0.json`

```text
训练家{FD_02}在\n在对战宫殿单打对战厅中\l创造了{FD_03}连胜的新纪录。\p让我们为{FD_02}欢呼！
```

当前美版中文：

来源：`data/text/tv.inc`

```text
训练家{STR_VAR_1}在
在对战宫殿单打对战厅中\l创造了{STR_VAR_2}连胜的新纪录。\p让我们为{STR_VAR_1}欢呼！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0825145F`

```text
バトルパレス\nシングル　バトルホ-ルに\lちょうせんした　{PLACEHOLDER_02}さんが\l{PLACEHOLDER_03}　れんしょうで\lきろくを　こうしん　しました!\p……{PLACEHOLDER_02}さん!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/tv.inc`，版本：`fe570a7e5^`

```text
The TRAINER {STR_VAR_1} set a new
{STR_VAR_2}-win-streak record while on\lthe BATTLE PALACE's SINGLE BATTLE\lHALL challenge.\pHere's to {STR_VAR_1}!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：バトルパレス\nシングル　バトルホールに\lちょうせんした　{STR_VAR_1}さんが\l{STR_VAR_2}　れんしょうで\lきろくを　こうしん　しました！\p⋯⋯{STR_VAR_1}さん！$
- EN：The TRAINER {STR_VAR_1} set a new\n{STR_VAR_2}-win-streak record while on\lthe BATTLE PALACE's SINGLE BATTLE\lHALL chall
- 中文：训练家{STR_VAR_1}在\n在对战宫殿单打对战厅中\l创造了{STR_VAR_2}连胜的新纪录。\p让我们为{STR_VAR_1}欢呼！$
- 理由：JP“バトルパレス シングル バトルホールに ちょうせんした”/EN“on the BATTLE PALACE's SINGLE BATTLE HALL challenge”，中文“训练家{STR_VAR_1}在 在对战宫殿单打对战厅中”出现“在 在”重复。
- 修改建议：训练家{STR_VAR_1}在对战宫殿单打对战厅中创造了{STR_VAR_2}连胜的新纪录。让我们为{STR_VAR_1}欢呼！
```

### 37. gTVPokemonNewsBattleFrontierText12

判定：**建议修复**；范围：日版和美版。

理由：对战宫殿此模板当前两版仍有“训练家…在\n在对战宫殿…”，与巨蛋模板不同，确实漏修。

建议处理：只删第二行开头多余的“在”；保留训练家名、连胜数及换页。

当前日版中文：

来源：`patch/batches/386_tv_0.json`

```text
训练家{FD_02}在\n在对战宫殿双打对战厅中\l创造了{FD_03}连胜的新纪录。\p让我们为{FD_02}欢呼！
```

当前美版中文：

来源：`data/text/tv.inc`

```text
训练家{STR_VAR_1}在
在对战宫殿双打对战厅中\l创造了{STR_VAR_2}连胜的新纪录。\p让我们为{STR_VAR_1}欢呼！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x082514A3`

```text
バトルパレス\nダブル　バトルホ-ルに\lちょうせんした　{PLACEHOLDER_02}さんが\l{PLACEHOLDER_03}　れんしょうで\lきろくを　こうしん　しました!\p……{PLACEHOLDER_02}さん!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/tv.inc`，版本：`fe570a7e5^`

```text
The TRAINER {STR_VAR_1} set a new
{STR_VAR_2}-win-streak record while on\lthe BATTLE PALACE's DOUBLE BATTLE\lHALL challenge.\pHere's to {STR_VAR_1}!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：バトルパレス\nダブル　バトルホールに\lちょうせんした　{STR_VAR_1}さんが\l{STR_VAR_2}　れんしょうで\lきろくを　こうしん　しました！\p⋯⋯{STR_VAR_1}さん！$
- EN：The TRAINER {STR_VAR_1} set a new\n{STR_VAR_2}-win-streak record while on\lthe BATTLE PALACE's DOUBLE BATTLE\lHALL chall
- 中文：训练家{STR_VAR_1}在\n在对战宫殿双打对战厅中\l创造了{STR_VAR_2}连胜的新纪录。\p让我们为{STR_VAR_1}欢呼！$
- 理由：同[126]，“训练家{STR_VAR_1}在 在对战宫殿双打对战厅中”出现“在 在”重复。
- 修改建议：训练家{STR_VAR_1}在对战宫殿双打对战厅中创造了{STR_VAR_2}连胜的新纪录。让我们为{STR_VAR_1}欢呼！

### 数字范围错误（2 条）
```

### 38. BattleFrontier_ReceptionGate_Text_Level50Info

判定：**已修复**；范围：日版和美版。

理由：当前两版已明确“不会使用低于50级的宝可梦”，没有排除50本身。

建议处理：无需重复修改。

当前日版中文：

来源：`patch/batches/230_battle_frontier_reception_gate.json`

```text
Lv. 50级允许等级50级以内的\n宝可梦参加。\p但是，您遇到的训练家不会\n使用低于50级的宝可梦。\p这是对战开拓区的\n入门级对战，\p我们建议您从这个模式\n开始挑战。
```

当前美版中文：

来源：`data/maps/BattleFrontier_ReceptionGate/scripts.inc`

```text
Lv. 50级允许等级50级以内的
宝可梦参加。\p但是，您遇到的训练家不会
使用低于50级的宝可梦。\p这是对战开拓区的
入门级对战，\p我们建议您从这个模式
开始挑战。$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0823ABB0`

```text
レベル50の　コ-スでは　なまえの　とおり\nレベル50までの　ポケモンを\lちょうせん　させることが　できます\pただし　レベル50より　ひくい　レベルの\nポケモンを　つれた　トレ-ナ-が\lとうじょう　することは　ありません\lくれぐれも　ごちゅうい　ください\pなお　このコ-スが　バトルフロンティアの\nたたかいの　きほんと　なって　いますので\lぜひ　チャレンジして　みてください
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_ReceptionGate/scripts.inc`，版本：`fe570a7e5^`

```text
The Level 50 course is open to POKéMON
up to and including Level 50.\pPlease keep in mind, however, that
no TRAINER you face will have any\lPOKéMON below Level 50.\pThis course is the entry level for
battles at the BATTLE FRONTIER.\pTo begin, we hope you will challenge
this course.$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：レベル50の　コースでは　なまえの　とおり\nレベル50までの　ポケモンを\lちょうせん　させることが　できます\pただし　レベル50より　ひくい　レベルの\nポケモンを　つれた　トレーナーが\lとうじょう　することは　ありません\lくれぐ
- EN：The Level 50 course is open to POKéMON\nup to and including Level 50.\pPlease keep in mind, however, that\nno TRAINER yo
- 中文：Lv. 50级允许等级50级以内的\n宝可梦参加。\p但是，您遇到的训练家不会\n使用等级50以内的宝可梦。\p这是对战开拓区的\n入门级对战，\p我们建议您从这个模式\n开始挑战。$
- 理由：JP「レベル50より ひくい レベルの ポケモンを つれた トレーナーが とうじょう することは ありません」与EN「no TRAINER you face will have any POKéMON below Level 50」均指对手宝可梦不低于50级（实为50级）；补丁中文「不会使用等级50以内的宝可梦」将「低于50级」误作「50级以内」，按中文惯例含50级本身，反而排除了50级，与原文矛盾。
- 修改建议：Lv. 50级允许等级50级以内的\n宝可梦参加。\p但是，您遇到的训练家不会\n使用低于50级的宝可梦。\p这是对战开拓区的\n入门级对战，\p我们建议您从这个模式\n开始挑战。$
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 7008,
    "decision": "fixed_verified",
    "review": {
      "row_number": 7008,
      "symbol": "BattleFrontier_ReceptionGate_Text_Level50Info",
      "domain": "ported_batch",
      "idx": "5756",
      "old": "不会\n使用等级50以内的宝可梦。",
      "new": "不会\n使用低于50级的宝可梦。",
      "reason": "below 50 不包括50本身。",
      "scope": "both",
      "action": "fix",
      "final_text": "Lv. 50级允许等级50级以内的\n宝可梦参加。\\p但是，您遇到的训练家不会\n使用低于50级的宝可梦。\\p这是对战开拓区的\n入门级对战，\\p我们建议您从这个模式\n开始挑战。",
      "old_current_text": "Lv. 50级允许等级50级以内的\n宝可梦参加。\\p但是，您遇到的训练家不会\n使用等级50以内的宝可梦。\\p这是对战开拓区的\n入门级对战，\\p我们建议您从这个模式\n开始挑战。",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/BattleFrontier_ReceptionGate/scripts.inc",
        "patch/batches/230_battle_frontier_reception_gate.json"
      ],
      "us_source_file": "data/maps/BattleFrontier_ReceptionGate/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/BattleFrontier_ReceptionGate/scripts.inc",
          "text": "レベル50の　コースでは　なまえの　とおり\nレベル50までの　ポケモンを\\lちょうせん　させることが　できます\\pただし　レベル50より　ひくい　レベルの\nポケモンを　つれた　トレーナーが\\lとうじょう　することは　ありません\\lくれぐれも　ごちゅうい　ください\\pなお　このコースが　バトルフロンティアの\nたたかいの　きほんと　なって　いますので\\lぜひ　チャレンジして　みてください$"
        }
      ]
    }
  }
]
```

### 39. BattleFrontier_ReceptionGate_Text_OpenLevelInfo

判定：**已修复**；范围：日版和美版。

理由：当前两版已明确“对手不会使用低于60级的宝可梦”，下限正确。

建议处理：无需重复修改。

当前日版中文：

来源：`patch/batches/230_battle_frontier_reception_gate.json`

```text
自由等级对于参加的宝可梦\n没有等级限制。\p对手的宝可梦等级会根据\n您的宝可梦等级进行调整。\p但是，您遇到的训练家不会\n使用低于60级的宝可梦。
```

当前美版中文：

来源：`data/maps/BattleFrontier_ReceptionGate/scripts.inc`

```text
自由等级对于参加的宝可梦
没有等级限制。\p对手的宝可梦等级会根据
您的宝可梦等级进行调整。\p但是，您遇到的训练家不会
使用低于60级的宝可梦。$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0823AC6C`

```text
オ-プンレベルの　コ-スでは\nちょうせんに　さんかする　ポケモンの\lレベルに　せいげんが　ありません\pあなたの　ポケモンの　レベルに　あわせて\nたいせんする　トレ-ナ-の　ポケモンの\lレベルが　かわります\pただし　レベル60より　ひくい　レベルの\nポケモンを　つれた　トレ-ナ-が\lとうじょう　することは　ありません
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_ReceptionGate/scripts.inc`，版本：`fe570a7e5^`

```text
The Open Level course places no limit
on the levels of POKéMON entering\lchallenges.\pThe levels of your opponents will
be adjusted to match the levels of\lyour POKéMON.\pHowever, no TRAINER you face will
have any POKéMON below Level 60.$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：オープンレベルの　コースでは\nちょうせんに　さんかする　ポケモンの\lレベルに　せいげんが　ありません\pあなたの　ポケモンの　レベルに　あわせて\nたいせんする　トレーナーの　ポケモンの\lレベルが　かわります\pただし　レベル60より
- EN：The Open Level course places no limit\non the levels of POKéMON entering\lchallenges.\pThe levels of your opponents will
- 中文：自由等级对于参加的宝可梦\n没有等级限制。\p对手的宝可梦等级会根据\n您的宝可梦等级进行调整。\p但是，您遇到的训练家不会\n使用等级60以内的宝可梦。$
- 理由：JP「レベル60より ひくい レベルの ポケモンを つれた トレーナーが とうじょう することは ありません」与EN「no TRAINER you face will have any POKéMON below Level 60」均指对手宝可梦不低于60级；补丁中文「不会使用等级60以内的宝可梦」将「低于60级」误作「60级以内」，按中文惯例含60级本身，与原文矛盾。
- 修改建议：自由等级对于参加的宝可梦\n没有等级限制。\p对手的宝可梦等级会根据\n您的宝可梦等级进行调整。\p但是，您遇到的训练家不会\n使用低于60级的宝可梦。$

### 内容遗漏（2 条）
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 7009,
    "decision": "fixed_verified",
    "review": {
      "row_number": 7009,
      "symbol": "BattleFrontier_ReceptionGate_Text_OpenLevelInfo",
      "domain": "ported_batch",
      "idx": "5757",
      "old": "使用等级60以内的宝可梦。",
      "new": "使用低于60级的宝可梦。",
      "reason": "报告所谓只允许最高等级不符合当前源码；实际发现60级边界译成以内，原文below60需改为低于60。",
      "scope": "both",
      "action": "fix",
      "final_text": "自由等级对于参加的宝可梦\n没有等级限制。\\p对手的宝可梦等级会根据\n您的宝可梦等级进行调整。\\p但是，您遇到的训练家不会\n使用低于60级的宝可梦。",
      "old_current_text": "自由等级对于参加的宝可梦\n没有等级限制。\\p对手的宝可梦等级会根据\n您的宝可梦等级进行调整。\\p但是，您遇到的训练家不会\n使用等级60以内的宝可梦。",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/BattleFrontier_ReceptionGate/scripts.inc",
        "patch/batches/230_battle_frontier_reception_gate.json"
      ],
      "us_source_file": "data/maps/BattleFrontier_ReceptionGate/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/BattleFrontier_ReceptionGate/scripts.inc",
          "text": "オープンレベルの　コースでは\nちょうせんに　さんかする　ポケモンの\\lレベルに　せいげんが　ありません\\pあなたの　ポケモンの　レベルに　あわせて\nたいせんする　トレーナーの　ポケモンの\\lレベルが　かわります\\pただし　レベル60より　ひくい　レベルの\nポケモンを　つれた　トレーナーが\\lとうじょう　することは　ありません$"
        }
      ]
    }
  }
]
```

### 40. CableClub_Text_ExplainWirelessClub

判定：**建议修复**；范围：日版和美版。

理由：常规说明的日文0x08248951和fe570a7e5之前完整英文都包含找不到朋友时靠近一些的提示，当前两版都缺此段。

建议处理：在交换或对战段之后、未接无线适配器段之前插入“如果在联盟交谊厅或直接连接室\n找不到朋友的话，\p请试着靠近朋友一些。”，与前后段各用换页分隔。

当前日版中文：

来源：`patch/batches/359_cable_club.json`

```text
让我给您介绍一下\n无线俱乐部吧。\p在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果无线适配器没有连接，\n您仍然可以使用GBA连接线进行连接。\p这种情况下，\n您就需要进入直接连接室。\p希望您能享受无线连接系统\n的乐趣。
```

当前美版中文：

来源：`data/text/cable_club.inc`

```text
让我给您介绍一下
无线俱乐部吧。\p在这层有2个房间。\p首先是左边的房间，
这是联盟交谊厅。\p您能够和那些在您周围并且也进入
该房间的训练家进行连接。\p您可以和他们一起进行
聊天、对战或交换。\p其次是右边的房间，
叫做直接连接室。\p您可以和他们进行
交换或对战。\p如果无线适配器没有连接，
您仍然可以使用GBA连接线进行连接。\p这种情况下，
您就需要进入直接连接室。\p希望您能享受无线连接系统
的乐趣。$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08248951`

```text
ポケモン　ワイヤレス　クラブでの\nあそびかたを　せつめい　します!\pこちら　2かいには\nふたつの　おへやが　ございます\pひとつめは　ひだりがわの　おへや\nユニオン　ル-ム!\pあなたの　ちかくで\nユニオン　ル-ムに　はいっている\lみしらぬ　おともだちと\lいろいろな　コミュニケ-ションが\lたのしめます!\pふたつめは　みぎがわの　おへや\nダイレクト　コ-ナ-!\pあなたの　しっている　おともだちと\nポケモンの　こうかんや\lたいせん　などを\lたのしむ　ことが　できます!\pもし　ユニオン　ル-ムや\nダイレクト　コ-ナ-で\lおともだちが　みつからない　ときは\pもうすこし　おともだちと\nちかづいて　みて　ください\pまた　ワイヤレスアダプタが\nつながって　いない　ばあいでも\pみぎがわの　おへやで\nケ-ブル　つうしんが　たのしめます\pそれでは\pワイヤレス　つうしんを\nたのしんで　くださいね!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/cable_club.inc`，版本：`fe570a7e5^`

```text
Let me explain how the POKéMON
WIRELESS CLUB works.\pOn this, the top floor, there are
two rooms.\pFirst, the room on the left.
It's the UNION ROOM.\pYou may link up with TRAINERS
around you who have also entered\lthe UNION ROOM.\pWith them, you may do things like
chat, battle, and trade.\pSecond, the room on the right is
the DIRECT CORNER.\pYou may trade or battle POKéMON
with your friends in this room.\pSometimes, you may not be able to
find your friends in the UNION ROOM\lor the DIRECT CORNER.\pIn that case, please move closer
to your friends.\pIf the Wireless Adapter isn't
connected, you may still link up\lusing a GBA Game Link cable.\pIf that is the case, you must go
to the DIRECT CORNER.\pI hope you enjoy the Wireless
Communication System.$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：ポケモン　ワイヤレス　クラブでの\nあそびかたを　せつめい　します！\pこちら　2かいには\nふたつの　おへやが　ございます\pひとつめは　ひだりがわの　おへや\nユニオン　ルーム！\pあなたの　ちかくで\nユニオン　ルームに　はいっている
- EN：Let me explain how the POKéMON\nWIRELESS CLUB works.\pOn this, the top floor, there are\ntwo rooms.\pFirst, the room on
- 中文：让我给您介绍一下\n无线俱乐部吧。\p在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接
- 理由：JP「もし ユニオン ルームや ダイレクト コーナーで おともだちが みつからない ときは もうすこし おともだちと ちかづいて みて ください(若在联盟交谊厅或直接连接室找不到朋友，请靠近朋友一些)」与EN「In that case, please move closer to your friends」整段在补丁中文中被遗漏，补丁中文从「交换或对战」直接跳到「如果无线适配器没有连接」，缺失一段提示。
- 修改建议：让我给您介绍一下\n无线俱乐部吧。\p在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果在联盟交谊厅或直接连接室\n找不到朋友的话，\p请试着靠近朋友一些。\p如果无线适配器没有连接，\n您仍然可
```

### 41. CableClub_Text_ExplainWirelessClubFirstTime

判定：**误报：混淆两个模板**；范围：两版；不改。

理由：首次说明的实际日文和fe570a7e5之前完整英文都没有靠近朋友提示：原文从交换/对战直接进入未连接适配器段。报告把上一条常规说明的内容套到此模板。

建议处理：不补不存在的原文，不把两个说明模板强制统一。

当前日版中文：

来源：`patch/batches/359_cable_club.json`

```text
在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果无线适配器没有连接，\n您仍然可以使用GBA连接线进行连接。\p这种情况下，\n您就需要进入直接连接室。\p希望您能享受无线连接系统\n的乐趣。
```

当前美版中文：

来源：`data/text/cable_club.inc`

```text
在这层有2个房间。\p首先是左边的房间，
这是联盟交谊厅。\p您能够和那些在您周围并且也进入
该房间的训练家进行连接。\p您可以和他们一起进行
聊天、对战或交换。\p其次是右边的房间，
叫做直接连接室。\p您可以和他们进行
交换或对战。\p如果无线适配器没有连接，
您仍然可以使用GBA连接线进行连接。\p这种情况下，
您就需要进入直接连接室。\p希望您能享受无线连接系统
的乐趣。$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x082487F6`

```text
こちら　2かいには\nふたつの　おへやが　ございます\pひとつめは　ひだりがわの　おへや\nユニオン　ル-ム!\pあなたの　ちかくで\nユニオン　ル-ムに　はいっている\lみしらぬ　おともだちと\lいろいろな　コミュニケ-ションが\lたのしめます!\pふたつめは　みぎがわの　おへや\nダイレクト　コ-ナ-!\pあなたの　しっている　おともだちと\nポケモンの　こうかんや\lたいせん　などを\lたのしむ　ことが　できます!\pもし　ワイヤレスアダプタが\nつながって　いない　ばあいでも\pみぎがわの　おへやで\nケ-ブル　つうしんが　たのしめます\pそれでは\pワイヤレス　つうしんを\nたのしんで　くださいね!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/cable_club.inc`，版本：`fe570a7e5^`

```text
On the top floor, there are two
rooms.\pFirst, the room on the left.
It's the UNION ROOM.\pYou may link up with TRAINERS
around you who have also entered\lthe UNION ROOM.\pWith them, you may do things like
chat, battle, and trade.\pSecond, the room on the right is
the DIRECT CORNER.\pYou may trade or battle POKéMON
with your friends in this room.\pIf the Wireless Adapter isn't
connected, you may still link up\lusing a GBA Game Link cable.\pIf that is the case, you must go
to the DIRECT CORNER.\pI hope you enjoy the Wireless
Communication System.$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：こちら　2かいには\nふたつの　おへやが　ございます\pひとつめは　ひだりがわの　おへや\nユニオン　ルーム！\pあなたの　ちかくで\nユニオン　ルームに　はいっている\lみしらぬ　おともだちと\lいろいろな　コミュニケーションが\lたのし
- EN：On the top floor, there are two\nrooms.\pFirst, the room on the left.\nIt's the UNION ROOM.\pYou may link up with TRAINE
- 中文：在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或
- 理由：与[661]同一说明文本的另一版本：JP「もし ユニオン ルームや ダイレクト コーナーで おともだちが みつからない ときは もうすこし おともだちと ちかづいて みて ください」与EN「please move closer to your friends」整段在补丁中文中同样被遗漏。
- 修改建议：在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果在联盟交谊厅或直接连接室\n找不到朋友的话，\p请试着靠近朋友一些。\p如果无线适配器没有连接，\n您仍然可以使用GBA连接线进行连接。\p这种情

### 数字错误（单位换算）（2 条）
```

### 42. LavaridgeTown_Gym_1F_Text_GeraldIntro

判定：**建议修复**；范围：日版和美版。

理由：日文写200度，英文数值392与华氏转换200×9/5+32一致。中文无单位的392度造成歧义。

建议处理：改为“你的宝可梦能抵挡\n200度的高温吗？”；如需明确单位，可用“200摄氏度”，具体取决于显示宽度。

当前日版中文：

来源：`patch/batches/079_lavaridgetown_gym_1f.json`

```text
你的宝可梦能抵挡\n392度的高温吗？
```

当前美版中文：

来源：`data/maps/LavaridgeTown_Gym_1F/scripts.inc`

```text
你的宝可梦能抵挡
392度的高温吗？$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x081F4780`

```text
おまえの　ポケモン\n200どの　あつさに　たえられるかよ!?
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/LavaridgeTown_Gym_1F/scripts.inc`，版本：`fe570a7e5^`

```text
Can your POKéMON withstand
392-degree heat?$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：おまえの　ポケモン
200どの　あつさに　たえられるかよ!?
- EN：Can your POKéMON withstand\n392-degree heat?$
- 中文：你的宝可梦能抵挡\n392度的高温吗？$
- 理由：JP「200どのあつさにたえられるか」为200摄氏度，EN“392-degree heat”为392华氏度（200°C=392°F），中文“392度的高温”直接沿用华氏度数值，在中文语境下会被理解为392摄氏度，与日文200度不符。
- 修改建议：你的宝可梦能抵挡\n200度的高温吗？
```

### 43. LavaridgeTown_Gym_1F_Text_GeraldPostBattle

判定：**建议修复**；范围：日版和美版。

理由：与上一条是同一单位转换。不能因真实岩浆温度另行科学改写游戏原文。

建议处理：仅将“岩浆的温度是392度”改成“岩浆的温度是200度”；保留后半段对战台词。

当前日版中文：

来源：`patch/batches/079_lavaridgetown_gym_1f.json`

```text
岩浆的温度\n是392度。\p你的宝可梦打败了我，那么在岩浆中\n也应该能比较容易生存下来。
```

当前美版中文：

来源：`data/maps/LavaridgeTown_Gym_1F/scripts.inc`

```text
岩浆的温度
是392度。\p你的宝可梦打败了我，那么在岩浆中
也应该能比较容易生存下来。$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x081F47AF`

```text
200どの　あつさ　ってのは\nようがんの　おんど!\pおまえの　ポケモン　おれに　かてたんだから\nようがんの　なかでも　へいき　だろうな!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/LavaridgeTown_Gym_1F/scripts.inc`，版本：`fe570a7e5^`

```text
The temperature of magma is
392 degrees.\pYour POKéMON beat me, so they should
easily survive in magma.$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：200どの　あつさ　ってのは
ようがんの　おんど!\pおまえの　ポケモン　おれに　かてたんだから
ようがんの　なかでも　へいき　だろうな!
- EN：The temperature of magma is\n392 degrees.\pYour POKéMON beat me, so they should\neasily survive in magma.$
- 中文：岩浆的温度\n是392度。\p你的宝可梦打败了我，那么在岩浆中\n也应该能比较容易生存下来。$
- 理由：JP「200どのあつさってのはようがんのおんど」为200摄氏度，EN“The temperature of magma is 392 degrees”为392华氏度（=200°C），中文“岩浆的温度是392度”沿用华氏度数值，中文读者会理解为392摄氏度，与日文200度不符。
- 修改建议：岩浆的温度\n是200度。\p你的宝可梦打败了我，那么在岩浆中\n也应该能比较容易生存下来。

### 误译（2 条）
```

### 44. gText_BecameMoreConsciousOfOtherMons

判定：**建议修复**；范围：日版和美版。

理由：気になる / more conscious of在这里表示更在意、更留意；“担心”加入了担忧含义，且与其他关注模板不一致。

建议处理：改为“它变得比平时\n更加在意其他宝可梦了！”；保留原有四个{PAUSE 15}，不照报告删暂停。

当前日版中文：

来源：`patch/batches/405_contest_strings.json`

```text
它变得比平时\n更加担心其他宝可梦了！{FC_08 0f}{FC_08 0f}{FC_08 0f}{FC_08 0f}
```

当前美版中文：

来源：`data/text/contest_strings.inc`

```text
它变得比平时
更加担心其他宝可梦了！{PAUSE 15}{PAUSE 15}{PAUSE 15}{PAUSE 15}$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0824B70C`

```text
ほかの　ポケモンが　いつもより\nきに　なって　きた!{BYTE_FC}くそ{BYTE_FC}くそ{BYTE_FC}くそ{BYTE_FC}くそ
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/contest_strings.inc`，版本：`fe570a7e5^`

```text
It became more conscious
of the other POKéMON.{PAUSE 15}{PAUSE 15}{PAUSE 15}{PAUSE 15}$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：ほかの　ポケモンが　いつもより\nきに　なって　きた！{PAUSE 0x0F}{PAUSE 0x0F}{PAUSE 0x0F}{PAUSE 0x0F}$
- EN：It became more conscious\nof the other POKéMON.{PAUSE 15}{PAUSE 15}{PAUSE 15}{PAUSE 15}$
- 中文：它变得比平时\n更加担心其他宝可梦了！{PAUSE_15}{PAUSE_15}{PAUSE_15}{PAUSE_15}$
- 理由：JP“ほかの ポケモンが いつもより きに なって きた！”/EN“It became more conscious of the other POKéMON.”——“きになる”此处意为“在意/留意”，中文译成“更加担心其他宝可梦”加入了“担忧”含义；且姊妹文本[677]“变得不那么关注”[679]“完全不关注”均用“关注”，本条用词不一致。
- 修改建议：它变得比平时更加在意其他宝可梦了！
```

### 45. gText_Contest_Shyness

判定：**已修复**；范围：日版和美版。

理由：两版当前已为“扭扭捏捏”。

建议处理：无需重复修改。

当前日版中文：

来源：`patch/batches/405_contest_strings.json`

```text
扭扭捏捏
```

当前美版中文：

来源：`data/text/contest_strings.inc`

```text
扭扭捏捏$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0824C0D2`

```text
モジモジ
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/contest_strings.inc`，版本：`fe570a7e5^`

```text
shyness$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：モジモジ$
- EN：shyness$
- 中文：扑通扑通$
- 理由：JP“モジモジ”/EN“shyness”（华丽大赛害羞状态，扭捏不安貌），中文译成“扑通扑通”——“扑通扑通”是心跳声，对应的是ドキドキ，与モジモジ的“扭捏”语义不符（[841]ドキドキ/anxiety已另译“慌慌张张”，此处系拟声词错配）。
- 修改建议：扭扭捏捏

### 跨世代机制污染（2 条）
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 9381,
    "decision": "fixed_verified",
    "review": {
      "row_number": 9381,
      "symbol": "gText_Contest_Shyness",
      "domain": "ported_batch",
      "idx": "8131",
      "old": "扑通扑通",
      "new": "扭扭捏捏",
      "reason": "モジモジ / shyness 指扭捏，不是心跳声。",
      "scope": "both",
      "action": "fix",
      "final_text": "扭扭捏捏",
      "old_current_text": "扑通扑通",
      "changed_files": [
        "../pokeemerald_us_chs/data/text/contest_strings.inc",
        "patch/batches/405_contest_strings.json"
      ],
      "us_source_file": "data/text/contest_strings.inc",
      "jp_source": [
        {
          "file": "data/text/contest_strings.inc",
          "text": "モジモジ$"
        }
      ]
    }
  }
]
```

### 46. [127]

判定：**建议修复**；范围：日版和美版。

理由：Wokann battle_moves.h的MOVE_WATERFALL是EFFECT_HIT、secondaryEffectChance=0；本作攀瀑自身没有畏缩追加效果。两版当前说明仍称有时使对手畏缩。

建议处理：建议用“以逆流攀瀑般的气势\n扑向对手。”，忠实保留日英原文攀瀑意象；或最小改动删除第二句。王者之证等道具效果不属于招式自身描述。

当前日版中文：

来源：`patch/move_descriptions.json`

```text
以惊人的气势扑向对手。
有时会使对手畏缩。
```

当前美版中文：

来源：`src/data/text/move_descriptions.h`

```text
以惊人的气势扑向对手。
有时会使对手畏缩。
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`src/data/text/move_descriptions.h`，版本：`fe570a7e5^`

```text
Charges the foe with speed
to climb waterfalls.
```

v3原报告条目（保留原建议供对照）：

```text
- JP：たきを　さかのぼるような　いきおいで
てきに　とっしんする
- EN：Charges the foe with speed
to climb waterfalls.
- 中文：以惊人的气势扑向对手。
有时会使对手畏缩。
- 理由：JP「たきを さかのぼるような いきおいで てきに とっしんする」/EN「Charges the foe with speed to climb waterfalls.」均未提及畏缩；JP baserom 招式数据 WATERFALL effect=EFFECT_HIT, secondaryEffectChance=0，第三世代攀瀑无追加效果，20%畏缩是第四世代才加入的机制。
- 修改建议：删除「有时会使对手畏缩。」一句，改为：以惊人的气势扑向对手。
```

### 47. [329]

判定：**已修复**；范围：日版和美版。

理由：当前绝对零度说明已删除使用者冰属性命中条件。

建议处理：无需重复修改。

当前日版中文：

来源：`patch/move_descriptions.json`

```text
以绝对零度攻击对手。
命中后会使对手一击昏厥。
```

当前美版中文：

来源：`src/data/text/move_descriptions.h`

```text
以绝对零度攻击对手。
命中后会使对手一击昏厥。
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`src/data/text/move_descriptions.h`，版本：`fe570a7e5^`

```text
A chilling attack that
causes fainting if it hits.
```

v3原报告条目（保留原建议供对照）：

```text
- JP：ぜったいれいどで　てきを　おそう
きまると　せんとうふのうになる
- EN：A chilling attack that
causes fainting if it hits.
- 中文：给对手一击昏厥。若冰属性
以外宝可梦使用会难以打中。
- 理由：JP「ぜったいれいどで てきを おそう きまると せんとうふのうになる」/EN「A chilling attack that causes fainting if it hits.」均未提及属性相关命中；第三世代绝对零度命中公式与使用者属性无关，「非冰属性使用难以打中/冰属性免疫」是第七世代起的机制（Bulbapedia: Gen VII onwards, Ice-type immune, non-Ice base 20%）。
- 修改建议：删除「若冰属性以外宝可梦使用会难以打中。」一句。

### 数值错误（2 条）
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 817,
    "decision": "fixed_verified",
    "review": {
      "row_number": 817,
      "symbol": "",
      "domain": "ability_move",
      "idx": "329",
      "old": "给对手一击昏厥。若冰属性\n以外宝可梦使用会难以打中。",
      "new": "以绝对零度攻击对手。\n命中后会使对手一击昏厥。",
      "reason": "移除第三世代不存在的使用者冰属性条件。",
      "scope": "both",
      "action": "fix",
      "resolved_symbol": "sSheerColdDescription",
      "final_text": "以绝对零度攻击对手。\n命中后会使对手一击昏厥。",
      "old_current_text": "给对手一击昏厥。若冰属性\n以外宝可梦使用会难以打中。",
      "changed_files": [
        "patch/move_descriptions.json",
        "../pokeemerald_us_chs/src/data/text/move_descriptions.h"
      ],
      "us_source_file": "src/data/text/move_descriptions.h",
      "jp_source": []
    }
  }
]
```

### 48. [180]

判定：**已修复；不必增加数值**；范围：日版和美版。

理由：当前怨恨已为“减少该招式的PP”，与日英原文一致。源码确实随机取2～5，但剩余PP不足时还会截断，写精确数值不是修复所必需。

建议处理：保留当前说明。若未来统一采用机制详解，可另行讨论“最多减少2～5点PP”，本次不再次改写。

当前日版中文：

来源：`patch/move_descriptions.json`

```text
怨恨对手最后用的招式，
减少该招式的PP。
```

当前美版中文：

来源：`src/data/text/move_descriptions.h`

```text
怨恨对手最后用的招式，
减少该招式的PP。
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`src/data/text/move_descriptions.h`，版本：`fe570a7e5^`

```text
Spitefully cuts the PP
of the foe's last move.
```

v3原报告条目（保留原建议供对照）：

```text
- JP：あいてが　だした　わざを　うらんで
その　わざポイントを　へらしてしまう
- EN：Spitefully cuts the PP
of the foe's last move.
- 中文：怨恨对手最后用的招式，
减少4PP该招式。
- 理由：JP「わざポイントを へらしてしまう」/EN「Spitefully cuts the PP of the foe's last move.」未写固定数值；第三世代游戏代码 Cmd_tryspiteppreduce 中 ppToDeduct = (Random() & 3) + 2，即2～5随机扣除，固定扣4是第四世代起的机制。中文「减少4PP」与第三世代实际不符。
- 修改建议：改为：怨恨对手最后用的招式，减少该招式2～5点PP。
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 519,
    "decision": "fixed_verified",
    "review": {
      "row_number": 519,
      "symbol": "",
      "domain": "ability_move",
      "idx": "180",
      "old": "减少4PP该招式。",
      "new": "减少该招式的PP。",
      "reason": "第三世代怨恨源码随机减少2～5PP；原文未限定4PP。",
      "scope": "both",
      "action": "fix",
      "resolved_symbol": "sSpiteDescription",
      "final_text": "怨恨对手最后用的招式，\n减少该招式的PP。",
      "old_current_text": "怨恨对手最后用的招式，\n减少4PP该招式。",
      "changed_files": [
        "patch/move_descriptions.json",
        "../pokeemerald_us_chs/src/data/text/move_descriptions.h"
      ],
      "us_source_file": "src/data/text/move_descriptions.h",
      "jp_source": []
    }
  }
]
```

### 49. [227]

判定：**已修复**；范围：日版和美版。

理由：两版再来一次已为2～6回合；此前67a5276/6ffae39ea已修。

建议处理：无需重复修改。

当前日版中文：

来源：`patch/move_descriptions.json`

```text
让对手接受再来一次，
在2～6回合内重复最后的招式。
```

当前美版中文：

来源：`src/data/text/move_descriptions.h`

```text
让对手接受再来一次，
在2～6回合内重复最后的招式。
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`src/data/text/move_descriptions.h`，版本：`fe570a7e5^`

```text
Makes the foe repeat its
last move over 2 to 6 turns.
```

v3原报告条目（保留原建议供对照）：

```text
- JP：てきが　さいごに　つかった　わざを
2ー6かい　れんぞくで　ださせる
- EN：Makes the foe repeat its
last move over 2 to 6 turns.
- 中文：让对手接受再来一次，
在3～6回合内重复最后的招式。
- 理由：JP「2ー6かい れんぞくで ださせる」/EN「Makes the foe repeat its last move over 2 to 6 turns.」均为2～6，中文写成「3～6回合」。
- 修改建议：改为：在2～6回合内重复最后的招式。

### 关键信息替换（2 条）
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 613,
    "decision": "already_fixed",
    "review": {
      "row_number": 613,
      "symbol": "",
      "domain": "ability_move",
      "idx": "227",
      "reason": "67a5276 / 6ffae39ea 已修复再来一次说明。",
      "action": "already_fixed"
    }
  }
]
```

### 50. [276]

判定：**已修复**；范围：日版和美版。

理由：当前宝珠说明已为“据说蕴含着超古代的力量”，不再写与丰缘传说渊源颇深。

建议处理：不重新增加末尾句号或重排已有换行。

当前日版中文：

来源：`patch/item_descriptions.json`

```text
散发着红色光辉的
宝珠。据说蕴含着
超古代的力量
```

当前美版中文：

来源：`src/data/text/item_descriptions.h`

```text
散发着红色光辉的
宝珠。据说蕴含着
超古代的力量
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`src/data/text/item_descriptions.h`，版本：`fe570a7e5^`

```text
A red, glowing orb
said to contain an
ancient power.
```

v3原报告条目（保留原建议供对照）：

```text
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
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 10533,
    "decision": "fixed_verified",
    "review": {
      "row_number": 10533,
      "symbol": "",
      "domain": "item",
      "idx": "276",
      "old": "据说和丰缘\n传说渊源颇深",
      "new": "据说蕴含着\n超古代的力量",
      "reason": "原文明确说内含古代力量。",
      "scope": "both",
      "action": "fix",
      "resolved_symbol": "sRedOrbDesc",
      "final_text": "散发着红色光辉的\n宝珠。据说蕴含着\n超古代的力量",
      "old_current_text": "散发着红色光辉的\n宝珠。据说和丰缘\n传说渊源颇深",
      "changed_files": [
        "patch/item_descriptions.json",
        "../pokeemerald_us_chs/src/data/text/item_descriptions.h"
      ],
      "us_source_file": "src/data/text/item_descriptions.h",
      "jp_source": [
        {
          "file": "src/data/text/item_descriptions.h",
          "text": "おおむかしの　ちからが\nこめられている　という\nあかく　かがやく　たま"
        }
      ]
    }
  }
]
```

### 51. [277]

判定：**已修复**；范围：日版和美版。

理由：当前宝珠说明已为“据说蕴含着超古代的力量”，不再写与丰缘传说渊源颇深。

建议处理：不重新增加末尾句号或重排已有换行。

当前日版中文：

来源：`patch/item_descriptions.json`

```text
散发着蓝色光辉的
宝珠。据说蕴含着
超古代的力量
```

当前美版中文：

来源：`src/data/text/item_descriptions.h`

```text
散发着蓝色光辉的
宝珠。据说蕴含着
超古代的力量
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`src/data/text/item_descriptions.h`，版本：`fe570a7e5^`

```text
A blue, glowing orb
said to contain an
ancient power.
```

v3原报告条目（保留原建议供对照）：

```text
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
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 10534,
    "decision": "fixed_verified",
    "review": {
      "row_number": 10534,
      "symbol": "",
      "domain": "item",
      "idx": "277",
      "old": "据说和丰缘\n传说渊源颇深",
      "new": "据说蕴含着\n超古代的力量",
      "reason": "原文明确说内含古代力量。",
      "scope": "both",
      "action": "fix",
      "resolved_symbol": "sBlueOrbDesc",
      "final_text": "散发着蓝色光辉的\n宝珠。据说蕴含着\n超古代的力量",
      "old_current_text": "散发着蓝色光辉的\n宝珠。据说和丰缘\n传说渊源颇深",
      "changed_files": [
        "patch/item_descriptions.json",
        "../pokeemerald_us_chs/src/data/text/item_descriptions.h"
      ],
      "us_source_file": "src/data/text/item_descriptions.h",
      "jp_source": [
        {
          "file": "src/data/text/item_descriptions.h",
          "text": "おおむかしの　ちからが\nこめられている　という\nあおく　かがやく　たま"
        }
      ]
    }
  }
]
```

### 52. BattleFrontier_Lounge2_Text_AmazingPowersOfObservation

判定：**建议修复**；范围：日版和美版。

理由：かんさつりょく / powers of observation为观察力，不是调查资料。センパイ是前辈，报告保留“老师”也不完全准确。

建议处理：建议用“观察力好厉害！\n前辈果然非同一般！”；报告提出的第一处修正合理，但应同时检查称谓。

当前日版中文：

来源：`patch/batches/432_checklist_scripts.json`

```text
调查资料好厉害！\n老师果然非同一般！
```

当前美版中文：

来源：`data/maps/BattleFrontier_Lounge2/scripts.inc`

```text
调查资料好厉害！
老师果然非同一般！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0823769E`

```text
すっげえ　かんさつりょく-!!\nやっぱ　センパイは　ちがうっすわ-
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_Lounge2/scripts.inc`，版本：`fe570a7e5^`

```text
What amazing powers of observation!
My mentor's like none other!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：すっげえ　かんさつりょくー！！\nやっぱ　センパイは　ちがうっすわー$
- EN：What amazing powers of observation!\nMy mentor's like none other!$
- 中文：调查资料好厉害！\n老师果然非同一般！$
- 理由：JP「かんさつりょく」即「观察力」，EN「What amazing powers of observation!」亦为观察力；补丁中文「调查资料好厉害」将观察力误译为「调查资料」，与三方原文不符。
- 修改建议：观察力好厉害！\n老师果然非同一般！$

### 术语错误（1 条）
```

### 53. BattleFrontier_Lounge7_Text_RockSlideDesc

判定：**已修复**；范围：日版和美版。

理由：两版当前该岩崩解释均已使用畏缩，不再使用恐惧。

建议处理：无需重复修改。

当前日版中文：

来源：`patch/batches/224_battle_frontier_lounge7.json`

```text
投出巨大的石块，\n可以使对手\n畏缩。
```

当前美版中文：

来源：`data/maps/BattleFrontier_Lounge7/scripts.inc`

```text
投出巨大的石块，
可以使对手
畏缩。$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0823A0BF`

```text
いわで　こうげき\nてきを　ひるませる\nことが　ある
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/BattleFrontier_Lounge7/scripts.inc`，版本：`fe570a7e5^`

```text
Large boulders
are hurled. May
cause flinching.$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：いわで　こうげき\nてきを　ひるませる\nことが　ある$
- EN：Large boulders\nare hurled. May\ncause flinching.$
- 中文：投出巨大的石块，\n可以使对手\n恐惧。$
- 理由：JP「てきを ひるませる」即「使对手畏缩(flinch)」，EN「May cause flinching」亦为畏缩；补丁中文「可以使对手恐惧」将ひるむ/ flinch误作「恐惧」，且与同文件[121]王者之证描述「使对手畏缩」术语不一致。
- 修改建议：投出巨大的石块，\n可以使对手\n畏缩。$

### 招式名误译（1 条）
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 6891,
    "decision": "fixed_verified",
    "review": {
      "row_number": 6891,
      "symbol": "BattleFrontier_Lounge7_Text_RockSlideDesc",
      "domain": "ported_batch",
      "idx": "5639",
      "old": "恐惧",
      "new": "畏缩",
      "reason": "统一第三世代flinch状态术语。",
      "scope": "both",
      "action": "fix",
      "final_text": "投出巨大的石块，\n可以使对手\n畏缩。",
      "old_current_text": "投出巨大的石块，\n可以使对手\n恐惧。",
      "changed_files": [
        "../pokeemerald_us_chs/data/maps/BattleFrontier_Lounge7/scripts.inc",
        "patch/batches/224_battle_frontier_lounge7.json"
      ],
      "us_source_file": "data/maps/BattleFrontier_Lounge7/scripts.inc",
      "jp_source": [
        {
          "file": "data/maps/BattleFrontier_Lounge7/scripts.inc",
          "text": "いわで　こうげき\nてきを　ひるませる\nことが　ある$"
        }
      ]
    }
  }
]
```

### 54. LilycoveCity_ContestHall_Text_SuchCharmingCuteAppeals

判定：**建议修复**；范围：日版和美版。

理由：日文为みずあそび，英文为WATER SPORT；当前两版招式名表第346条是玩水，这段仍写水之游。

建议处理：把“水之游”改为“玩水”，保留评委的其他评价。

当前日版中文：

来源：`patch/batches/125_lilycovecity_contesthall.json`

```text
评委：啊，如此迷人，\n如此可爱！\p哎，天啊！那水之游\n多么完美，多么可爱！
```

当前美版中文：

来源：`data/maps/LilycoveCity_ContestHall/scripts.inc`

```text
评委：啊，如此迷人，
如此可爱！\p哎，天啊！那水之游
多么完美，多么可爱！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0820804C`

```text
しんさいん“おお\nみんな　かわいい　アピ-ルだなあ!\pおおっ　なんて　かわいい\nみずあそびの　アピ-ルなんだろう!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/LilycoveCity_ContestHall/scripts.inc`，版本：`fe570a7e5^`

```text
JUDGE: Oh, such charming and cute
appeals!\pOh, my goodness! What a perfectly
adorable WATER SPORT appeal!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：しんさいん“おお
みんな　かわいい　アピ-ルだなあ!\pおおっ　なんて　かわいい
みずあそびの　アピ-ルなんだろう!
- EN：JUDGE: Oh, such charming and cute\nappeals!\pOh, my goodness! What a perfectly\nadorable WATER SPORT appeal!$
- 中文：评委：啊，如此迷人，\n如此可爱！\p哎，天啊！那水之游\n多么完美，多么可爱！$
- 理由：JP「なんてかわいいみずあそびのアピールなんだろう」/EN“What an adorable WATER SPORT appeal”中的招式みずあそび（WATER SPORT）官方中文名为“玩水”，中文“那水之游多么完美”误作“水之游”，招式名错误。
- 修改建议：评委：啊，如此迷人，\n如此可爱！\p哎，天啊！那玩水\n多么完美，多么可爱！

### 衍字（1 条）
```

### 55. LilycoveCity_CoveLilyMotel_1F_Text_HeardAquaHideoutBusted

判定：**建议修复**；范围：日版和美版。

理由：两版当前都有“有人到捣毁了”，多出的到使句子不通。

建议处理：仅删“到”，改为“我听说有人捣毁了\n海洋队的基地，”。

当前日版中文：

来源：`patch/batches/127_lilycovecity_covelilymotel_1f.json`

```text
啊，抱歉，抱歉！\n我看电视看入迷了！\p我听说有人到捣毁了\n海洋队的基地，\p多亏如此，我们刚刚\n接到了一个大团体订房预约，\p是一个公司，叫做……呃……\n游戏什么的……
```

当前美版中文：

来源：`data/maps/LilycoveCity_CoveLilyMotel_1F/scripts.inc`

```text
啊，抱歉，抱歉！
我看电视看入迷了！\p我听说有人到捣毁了
海洋队的基地，\p多亏如此，我们刚刚
接到了一个大团体订房预约，\p是一个公司，叫做……呃……
游戏什么的……$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0820571C`

```text
あ　ごめん　ごめん!\nテレビに　むちゅう　だったもんで!\pそういえば　だれかが　アクアだんの\nアジトを　かいめつ　させた　らしいね!\pおかげで　さっき　だんたいさん　からの\nしゅくはく　よやくが　はいったよ!\pたしか……　ゲ-ムなんとか　っていう\nかいしゃ　だったかな……
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/LilycoveCity_CoveLilyMotel_1F/scripts.inc`，版本：`fe570a7e5^`

```text
Oh, sorry, sorry!
I was too involved in watching TV!\pI heard that someone busted
the TEAM AQUA HIDEOUT.\pThanks to that, we just booked
a reservation from a big group.\pIt was a company called… Uh…
GAME something…$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：あ　ごめん　ごめん!
テレビに　むちゅう　だったもんで!\pそういえば　だれかが　アクアだんの
アジトを　かいめつ　させた　らしいね!\pおかげで　さっき　だんたいさん　からの
しゅくはく　よやくが　はいったよ!\pたしか……　ゲ-ムなんと
- EN：Oh, sorry, sorry!\nI was too involved in watching TV!\pI heard that someone busted\nthe TEAM AQUA HIDEOUT.\pThanks to th
- 中文：啊，抱歉，抱歉！\n我看电视看入迷了！\p我听说有人到捣毁了\n海洋队的基地，\p多亏如此，我们刚刚\n接到了一个大团体订房预约，\p是一个公司，叫做……呃……\n游戏什么的……$
- 理由：JP「だれかがアクアだんのアジトをかいめつさせたらしいね」/EN“someone busted the TEAM AQUA HIDEOUT”意为“有人捣毁了海洋队基地”，中文“我听说有人到捣毁了海洋队的基地”中“到”为衍字，文理不通，美版中文同样误写。
- 修改建议：啊，抱歉，抱歉！\n我看电视看入迷了！\p我听说有人捣毁了\n海洋队的基地，\p多亏如此，我们刚刚\n接到了一个大团体订房预约，\p是一个公司，叫做……呃……\n游戏什么的……

### 漏字（1 条）
```

### 56. MauvilleCity_Text_UncleCanYouBattleWally

判定：**已修复**；范围：日版和美版。

理由：当前两版都已为“能请你和满充来一场对战吗？”，宾语已补齐；不能只凭v3旧快照再次判漏字。

建议处理：无需改成另一个代词版本。

当前日版中文：

来源：`patch/batches/050_mauvillecity.json`

```text
叔叔：你是{FD_01}{FD_05}吧？\n为了满充，\l能请你和满充来一场对战吗？\p我想他现在这样\n是没法听得进劝的。
```

当前美版中文：

来源：`data/maps/MauvilleCity/scripts.inc`

```text
叔叔：你是{PLAYER}{KUN}吧？
为了满充，\l能请你和满充来一场对战吗？\p我想他现在这样
是没法听得进劝的。$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x081DDFD3`

```text
おじさん“{PLACEHOLDER_01}{PLACEHOLDER_05}とやら\nわるいけど　ミツルくんと\lしょうぶ　してあげて　くれないかな?\pこのままだと　なにを　いっても\nきいて　もらえそうに　ないよ
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/MauvilleCity/scripts.inc`，版本：`fe570a7e5^`

```text
UNCLE: {PLAYER}{KUN}, was it?
On WALLY's behalf, can I ask you to\lbattle with him just this once?\pI don't think he's going to listen to
any reason the way he is now.$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：おじさん“{PLAYER}{KUN}とやら\nわるいけど　ミツルくんと\lしょうぶ　してあげて　くれないかな？\pこのままだと　なにを　いっても\nきいて　もらえそうに　ないよ$
- EN：UNCLE: {PLAYER}{KUN}, was it?\nOn WALLY's behalf, can I ask you to\lbattle with him just this once?\pI don't think he's
- 中文：叔叔：你是{PLAYER}{KUN}吧？\n为了满充，\l能请你和来一场对战吗？\p我想他现在这样\n是没法听得进劝的。$
- 理由：JP「ミツルくんとしょうぶしてあげてくれないかな（能和满充对战一下吗）」/EN「can I ask you to battle with him just this once?」中对战对象明确，补丁/美版中文「能请你和来一场对战吗」的「和」后缺宾语（应为「和他」），句子不完整。
- 修改建议：能请你和他来一场对战吗？

### 术语误译（1 条）
```

### 57. MossdeepCity_GameCorner_1F_Text_DescribeWhichGame

判定：**建议修复**；范围：日版和美版。

理由：Wokann日文为游戏说明，英文game rules；该对话是小游戏说明，不是战斗规则。

建议处理：仅将“对战规则”改为“游戏规则”。

当前日版中文：

来源：`patch/batches/151_mossdeepcity_gamecorner_1f.json`

```text
需要的话，\n我可以向您解说对战规则。\p需要解说哪一项？
```

当前美版中文：

来源：`data/text/cable_club.inc`

```text
需要的话，
我可以向您解说对战规则。\p需要解说哪一项？$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x082481AB`

```text
ぼくは　ゲ-ムの　せつめいを\nしますよ!\lどの　せつめいを　ききますか?
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/cable_club.inc`，版本：`fe570a7e5^`

```text
I can explain game rules to you,
if you'd like.\pWhich game should I describe?$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：ぼくは　ゲームの　せつめいを\nしますよ！\lどの　せつめいを　ききますか？$
- EN：I can explain game rules to you,\nif you'd like.\pWhich game should I describe?$
- 中文：需要的话，\n我可以向您解说对战规则。\p需要解说哪一项？$
- 理由：JP「ゲームのせつめいをしますよ（我来说明游戏规则）」/EN「I can explain game rules to you」中的「ゲーム（游戏）」指嘟嘟利摘树果、宝可梦跳绳等小游戏，补丁/美版中文误作「对战规则」，「游戏」误译为「对战」，术语错误。
- 修改建议：需要的话，我可以向您解说游戏规则。需要解说哪一项？

### 语义缺失（1 条）
```

### 58. gText_NoticesGoldCard

判定：**建议修复：旧修复不完整**；范围：日版和美版。

理由：金卡、金色和四星已补，但后段仍写“比这更厉害的训练家卡”，且日英原文的两个PLAYER都没恢复。v2将它标记fixed_verified并不代表全部遗漏已解决。

建议处理：保留已修的前段；把后段明确为“拥有金卡的训练家，{PLAYER}您还是第一位！”并在恢复宝可梦句保留第二个{PLAYER}。动态名仍按日版现有玩家显示逻辑处理，不改存档。

当前日版中文：

来源：`patch/batches/196_pokemon_centers.json`

```text
那、那张卡！？\p难道是金卡！？\p金色真耀眼！！\n四颗星在闪耀！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有比这更厉害的\n训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！
```

当前美版中文：

来源：`data/text/pkmn_center_nurse.inc`

```text
那、那张卡！？\p难道是金卡！？\p金色真耀眼！！
四颗星在闪耀！！\p至今为止我也见过几位
拥有白银卡的训练家。\p但是拥有比这更厉害的
训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08243814`

```text
そ　それは……\nひょっとして　ゴ-ルドカ-ド!?\pああ……　きんいろが　まぶしい!\n4つの　ほしが　かがやかしい!\pわたしも　これまでに\nシルバ-カ-ドの　トレ-ナ-さんなら\lなんにんか　みてきましたが\lゴ-ルドカ-ドを　おもちの　かたは\l{PLACEHOLDER_01}さんが　はじめて　ですよ!\pさあ　{PLACEHOLDER_01}さんの\nポケモンを　やすませて　あげましょう!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/pkmn_center_nurse.inc`，版本：`fe570a7e5^`

```text
Th-that card…
Could it be… The GOLD CARD?!\pOh, the gold color is brilliant!
The four stars seem to sparkle!\pI've seen several TRAINERS with
a SILVER CARD before, but, {PLAYER},\lyou're the first TRAINER I've ever\lseen with a GOLD CARD!\pOkay, {PLAYER}, please allow me
the honor of resting your POKéMON!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：そ　それは⋯⋯\nひょっとして　ゴールドカード！？\pああ⋯⋯　きんいろが　まぶしい！\n4つの　ほしが　かがやかしい！\pわたしも　これまでに\nシルバーカードの　トレーナーさんなら\lなんにんか　みてきましたが\lゴールドカードを　おも
- EN：Th-that card…\nCould it be… The GOLD CARD?!\pOh, the gold color is brilliant!\nThe four stars seem to sparkle!\pI've see
- 中文：那、那张卡！？\p那个颜色！！\n那星星的数量！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有比这更厉害的\n训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！$
- 理由：JP「ひょっとして ゴールドカード」「きんいろが まぶしい」「4つの ほしが かがやかしい」/EN「The GOLD CARD」「the gold color is brilliant」「The four stars seem to sparkle」中的关键名词（金卡/金色/四颗星星/闪耀）被补丁中文与美版中文一并丢弃（「那张卡」「那个颜色」「星星的数量」），关键语义缺失
- 修改建议：那、那张卡……\p难道是金卡！？\p啊……金色真是耀眼！\n四颗星星闪闪发光！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但拥有金卡的训练家，\l{PLAYER}您还是第一位！\p那么，请让我为{PLAYER}的\n宝可梦休息一下吧！$

### 语义反转/误译（1 条）
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 5803,
    "decision": "fixed_verified",
    "review": {
      "row_number": 5803,
      "symbol": "gText_NoticesGoldCard",
      "domain": "ported_batch",
      "idx": "4551",
      "old": "那、那张卡！？\\p那个颜色！！\n那星星的数量！！",
      "new": "那、那张卡！？\\p难道是金卡！？\\p金色真耀眼！！\n四颗星在闪耀！！",
      "reason": "恢复金卡、金色、四颗星的明确内容。",
      "scope": "both",
      "action": "fix",
      "final_text": "那、那张卡！？\\p难道是金卡！？\\p金色真耀眼！！\n四颗星在闪耀！！\\p至今为止我也见过几位\n拥有白银卡的训练家。\\p但是拥有比这更厉害的\n训练家卡的客人，\\l您还是第一位！\\p先让您的宝可梦休息一下吧！",
      "old_current_text": "那、那张卡！？\\p那个颜色！！\n那星星的数量！！\\p至今为止我也见过几位\n拥有白银卡的训练家。\\p但是拥有比这更厉害的\n训练家卡的客人，\\l您还是第一位！\\p先让您的宝可梦休息一下吧！",
      "changed_files": [
        "../pokeemerald_us_chs/data/text/pkmn_center_nurse.inc",
        "patch/batches/196_pokemon_centers.json"
      ],
      "us_source_file": "data/text/pkmn_center_nurse.inc",
      "jp_source": [
        {
          "file": "data/text/pkmn_center_nurse.inc",
          "text": "そ　それは⋯⋯\nひょっとして　ゴールドカード！？\\pああ⋯⋯　きんいろが　まぶしい！\n4つの　ほしが　かがやかしい！\\pわたしも　これまでに\nシルバーカードの　トレーナーさんなら\\lなんにんか　みてきましたが\\lゴールドカードを　おもちの　かたは\\l{PLAYER}さんが　はじめて　ですよ！\\pさあ　{PLAYER}さんの\nポケモンを　やすませて　あげましょう！$"
        }
      ]
    }
  }
]
```

### 59. RustboroCity_DevonCorp_1F_Text_HowCouldWeGetRobbed

判定：**建议修复**；范围：日版和美版。

理由：原文是包裹已经被抢后的自责，不是否认有人会抢东西。

建议处理：改为“包裹居然被小偷抢走了，\n我们也太不小心了……”，保留原文省略号。

当前日版中文：

来源：`patch/batches/031_rustborocity_devoncorp_1f.json`

```text
说什么傻话，\n谁会抢我们的东西？
```

当前美版中文：

来源：`data/maps/RustboroCity_DevonCorp_1F/scripts.inc`

```text
说什么傻话，
谁会抢我们的东西？$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08201249`

```text
どろぼうに　にもつを　うばわれるなんて\nなんて　ドジなんだろう……
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/RustboroCity_DevonCorp_1F/scripts.inc`，版本：`fe570a7e5^`

```text
It's beyond stupid.
How could we get robbed?$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：どろぼうに　にもつを　うばわれるなんて\nなんて　ドジなんだろう⋯⋯$
- EN：It's beyond stupid.\nHow could we get robbed?$
- 中文：说什么傻话，\n谁会抢我们的东西？$
- 理由：JP「どろぼうに にもつを うばわれるなんて なんて ドジなんだろう」(包裹被抢,我们真不小心)/EN"It's beyond stupid. How could we get robbed?"→CHS「说什么傻话,谁会抢我们的东西?」,把自责"我们真蠢"误作否认"谁会抢",语义反转
- 修改建议：包裹居然被强盗抢走了，我们也太不小心了……

### 未翻译残留/错字（1 条）
```

### 60. RustboroCity_PokemonSchool_Text_ExplainPoison

判定：**建议修复**；范围：日版和美版。

理由：当前两版都残留“体力P”，多出的P没有语义。

建议处理：仅删P，保留体力措辞、所有段落和解毒药提示；不拆HP，不额外加句号。

当前日版中文：

来源：`patch/batches/038_rustborocity_pokemonschool.json`

```text
宝可梦中毒后，\n会慢慢损失体力，\p此效果在战斗后\n依然残留。\p在探险中，中毒的宝可梦的体力P\n也会不断减少。\p使用解毒药可解毒。
```

当前美版中文：

来源：`data/maps/RustboroCity_PokemonSchool/scripts.inc`

```text
宝可梦中毒后，
会慢慢损失体力，\p此效果在战斗后
依然残留。\p在探险中，中毒的宝可梦的体力P
也会不断减少。\p使用解毒药可解毒。$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08202E63`

```text
どくを　うけると\nたいりょくが　へっていきます\pせんとうのあとも　どくは　のこるので\nあるくたびに　たいりょくが　へります\lどくけしで　なおしましょう
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/maps/RustboroCity_PokemonSchool/scripts.inc`，版本：`fe570a7e5^`

```text
If a POKéMON is poisoned, it will
steadily lose HP.\pThe effects of poison remain after
a battle.\pA poisoned POKéMON's HP will drop
while it is traveling.\pHeal a poisoning using an ANTIDOTE.$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：どくを　うけると\nたいりょくが　へっていきます\pせんとうのあとも　どくは　のこるので\nあるくたびに　たいりょくが　へります\lどくけしで　なおしましょう$
- EN：If a POKéMON is poisoned, it will\nsteadily lose HP.\pThe effects of poison remain after\na battle.\pA poisoned POKéMON'
- 中文：宝可梦中毒后，\n会慢慢损失体力，\p此效果在战斗后\n依然残留。\p在探险中，中毒的宝可梦的体力P\n也会不断减少。\p使用解毒药可解毒。$
- 理由：JP「あるくたびに たいりょくが へります」(每走一步体力减少)/EN"A poisoned POKéMON's HP will drop while it is traveling"→CHS「中毒的宝可梦的体力P也会不断减少」,"体力P"中多余的"P"为HP残留字符
- 修改建议：在探险中，中毒的宝可梦的体力也会不断减少。

### 误译；未翻译残留（1 条）
```

### 61. gTVBravoTrainerText00

判定：**建议修复：只采纳明确部分**；范围：日版和美版。

理由：STR_VAR_3/日文クラス是参赛级别，不是该级别优胜；“荣获优胜”确实夸大。BRAVO是节目名，保留拉丁名称不能自动等同漏译，也不能无依据当成官方“喝彩训练家”。

建议处理：先把结果句改为“现在，这只宝可梦在{STR_VAR_2}\n类别参加了{STR_VAR_3}级别的比赛。”，保持三种动态值及控制符。节目名中文化若做，须统一该节目所有标题，不只改此条。

当前日版中文：

来源：`patch/batches/386_tv_0.json`

```text
太好了！\n现在是BRAVO训练家时间！\p今天我们所要介绍的\n主角就是{FD_02}。\p现在，这只宝可梦在{FD_03}\n比赛中荣获{FD_04}优胜。
```

当前美版中文：

来源：`data/text/tv.inc`

```text
太好了！
现在是BRAVO训练家时间！\p今天我们所要介绍的
主角就是{STR_VAR_1}。\p现在，这只宝可梦在{STR_VAR_2}
比赛中荣获{STR_VAR_3}优胜。$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x0824C754`

```text
イヤ-!\n“ブラボ-　トレ-ナ-”の　じかんだ!\pきょうは　{PLACEHOLDER_04}クラスの\n{PLACEHOLDER_03}を　ほこる\l{PLACEHOLDER_02}さんの　ポケモン!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/tv.inc`，版本：`fe570a7e5^`

```text
Yeah!
It's BRAVO TRAINER time!\pToday, we're going to profile a POKéMON
belonging to {STR_VAR_1}.\pNow, this POKéMON boasts a {STR_VAR_3}
Rank in the {STR_VAR_2} Category.$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：イヤー！\n“ブラボー　トレーナー”の　じかんだ！\pきょうは　{B_COPY_VAR_3}クラスの\n{B_COPY_VAR_2}を　ほこる\l{B_COPY_VAR_1}さんの　ポケモン！$
- EN：Yeah!\nIt's BRAVO TRAINER time!\pToday, we're going to profile a POKéMON\nbelonging to {STR_VAR_1}.\pNow, this POKéMON b
- 中文：太好了！\n现在是BRAVO训练家时间！\p今天我们所要介绍的\n主角就是{STR_VAR_1}。\p现在，这只宝可梦在{STR_VAR_2}\n比赛中荣获{STR_VAR_3}优胜。$
- 理由：JP“ブラボー トレーナー”/EN“BRAVO TRAINER”节目名在中文中直接保留拉丁字母“BRAVO”；EN“boasts a {STR_VAR_3} Rank in the {STR_VAR_2} Category”（JP“{STR_VAR_3}クラスの{STR_VAR_2}をほこる”）意为“拥有某级别头衔”，中文译成“荣获{STR_VAR_3}优胜”把“级别/Rank”误作“夺冠”。
- 修改建议：太好了！现在是喝彩训练家时间！今天我们所要介绍的主角就是{STR_VAR_1}。现在，这只宝可梦在{STR_VAR_2}比赛中达到了{STR_VAR_3}级别。

### 误译/语义缺失（专名丢失、数字丢失、占位符丢失）（1 条）
```

### 62. gText_NoticesGoldCard

判定：**重复条目**；范围：归并第58条。

理由：与第58条是同一个gText_NoticesGoldCard；同样指向当前两版同一资源，不能再计一条独立修复。

建议处理：合并进第58条处理，不做第二次覆盖。

当前日版中文：

来源：`patch/batches/196_pokemon_centers.json`

```text
那、那张卡！？\p难道是金卡！？\p金色真耀眼！！\n四颗星在闪耀！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有比这更厉害的\n训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！
```

当前美版中文：

来源：`data/text/pkmn_center_nurse.inc`

```text
那、那张卡！？\p难道是金卡！？\p金色真耀眼！！
四颗星在闪耀！！\p至今为止我也见过几位
拥有白银卡的训练家。\p但是拥有比这更厉害的
训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x08243814`

```text
そ　それは……\nひょっとして　ゴ-ルドカ-ド!?\pああ……　きんいろが　まぶしい!\n4つの　ほしが　かがやかしい!\pわたしも　これまでに\nシルバ-カ-ドの　トレ-ナ-さんなら\lなんにんか　みてきましたが\lゴ-ルドカ-ドを　おもちの　かたは\l{PLACEHOLDER_01}さんが　はじめて　ですよ!\pさあ　{PLACEHOLDER_01}さんの\nポケモンを　やすませて　あげましょう!
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/text/pkmn_center_nurse.inc`，版本：`fe570a7e5^`

```text
Th-that card…
Could it be… The GOLD CARD?!\pOh, the gold color is brilliant!
The four stars seem to sparkle!\pI've seen several TRAINERS with
a SILVER CARD before, but, {PLAYER},\lyou're the first TRAINER I've ever\lseen with a GOLD CARD!\pOkay, {PLAYER}, please allow me
the honor of resting your POKéMON!$
```

v3原报告条目（保留原建议供对照）：

```text
- JP：そ　それは⋯⋯\nひょっとして　ゴールドカード！？\pああ⋯⋯　きんいろが　まぶしい！\n4つの　ほしが　かがやかしい！\pわたしも　これまでに\nシルバーカードの　トレーナーさんなら\lなんにんか　みてきましたが\lゴールドカードを　おも
- EN：Th-that card…\nCould it be… The GOLD CARD?!\pOh, the gold color is brilliant!\nThe four stars seem to sparkle!\pI've see
- 中文：那、那张卡！？\p那个颜色！！\n那星星的数量！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有比这更厉害的\n训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！$
- 理由：JP：ひょっとしてゴールドカード！？（"难道是黄金卡！？"）、ああ……きんいろがまぶしい！4つのほしがかがやかしい！（"啊……金色耀眼！四颗星星闪闪发光！"）、{PLAYER}さんははじめてですよ；EN：Could it be… The GOLD CARD?! / Oh, the gold color is brilliant! The four stars seem to sparkle! / {PLAYER}×2；日版补丁中文与美版中文均为"那、那张卡！？""那星星的数量！！"（丢失"金卡"专名与数字"4"及"闪耀"语义）、"比这更厉害的训练家卡"（以模糊表述替代"黄金卡"），并删除了{P
- 修改建议：那、那张卡……！？\p难道是黄金卡！？\p啊……金色的光辉真耀眼！\n四颗星星闪闪发光！\p至今为止我也见过几位\n拥有白银卡的训练家，\l但拥有黄金卡的客人，\l{PLAYER}您还是第一位！\p先让您的宝可梦休息一下吧！

### 翻译错误（1 条）
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 5803,
    "decision": "fixed_verified",
    "review": {
      "row_number": 5803,
      "symbol": "gText_NoticesGoldCard",
      "domain": "ported_batch",
      "idx": "4551",
      "old": "那、那张卡！？\\p那个颜色！！\n那星星的数量！！",
      "new": "那、那张卡！？\\p难道是金卡！？\\p金色真耀眼！！\n四颗星在闪耀！！",
      "reason": "恢复金卡、金色、四颗星的明确内容。",
      "scope": "both",
      "action": "fix",
      "final_text": "那、那张卡！？\\p难道是金卡！？\\p金色真耀眼！！\n四颗星在闪耀！！\\p至今为止我也见过几位\n拥有白银卡的训练家。\\p但是拥有比这更厉害的\n训练家卡的客人，\\l您还是第一位！\\p先让您的宝可梦休息一下吧！",
      "old_current_text": "那、那张卡！？\\p那个颜色！！\n那星星的数量！！\\p至今为止我也见过几位\n拥有白银卡的训练家。\\p但是拥有比这更厉害的\n训练家卡的客人，\\l您还是第一位！\\p先让您的宝可梦休息一下吧！",
      "changed_files": [
        "../pokeemerald_us_chs/data/text/pkmn_center_nurse.inc",
        "patch/batches/196_pokemon_centers.json"
      ],
      "us_source_file": "data/text/pkmn_center_nurse.inc",
      "jp_source": [
        {
          "file": "data/text/pkmn_center_nurse.inc",
          "text": "そ　それは⋯⋯\nひょっとして　ゴールドカード！？\\pああ⋯⋯　きんいろが　まぶしい！\n4つの　ほしが　かがやかしい！\\pわたしも　これまでに\nシルバーカードの　トレーナーさんなら\\lなんにんか　みてきましたが\\lゴールドカードを　おもちの　かたは\\l{PLAYER}さんが　はじめて　ですよ！\\pさあ　{PLAYER}さんの\nポケモンを　やすませて　あげましょう！$"
        }
      ]
    }
  }
]
```

### 63. sText_MysteryGiftVisitingTrainerArrived

判定：**建议修复：仅日版仍有错误**；范围：日版。

理由：美版当前已经把系统改为希望；日版batch471仍是系统。且日版0x085FCE8B有有效日文配信文本和既有覆盖，报告与v2称日版没有对应资源都不正确。

建议处理：只把日版“系统您可以享受”改为“希望您可以享受”，沿用现有已核验资源，不重新猜地址。美版无需重复改。

当前日版中文：

来源：`patch/batches/471_checklist_mystery_gift_script_texts.json`

```text
感谢使用\n神秘礼物系统。\p一位训练家已经来到\n琉璃市寻找您。\p系统您可以享受\n与训练家的对战。\p您可以邀请其他训练家\n通过填写密码。\p试着找寻其他\n有用的密码吧。
```

当前美版中文：

来源：`data/scripts/gift_trainer.inc`

```text
感谢使用
神秘礼物系统。\p一位训练家已经来到
琉璃市寻找您。\p希望您可以享受
与训练家的对战。\p您可以邀请其他训练家
通过填写密码。\p试着找寻其他
有用的密码吧。$
```

既有日版覆盖的原文（只读核验，没有新增地址覆盖）：

原地址：`0x85fce8b`

```text
ふしぎなおくりもの　を　ごりよう\nいただき　ありがとう　ございます\pルネシティに　トレ-ナ-が\nきている　ようですよ\pぜひ　たいせんを\nたのしんで　くださいませ!\pほかの　あいことば　でも\nべつの　トレ-ナ-が　よべますので\pあいことばを　いろいろと\nさがして　みて　ください
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`data/scripts/gift_trainer.inc`，版本：`fe570a7e5^`

```text
Thank you for using the MYSTERY
GIFT System.\pA TRAINER has arrived in
SOOTOPOLIS CITY looking for you.\pWe hope you will enjoy
battling the visiting TRAINER.\pYou may invite other TRAINERS by
entering other passwords.\pTry looking for other passwords
that may work.$
```

v3原报告条目（保留原建议供对照）：

```text
- EN：Thank you for using the MYSTERY\nGIFT System.\pA TRAINER has arrived in\nSOOTOPOLIS CITY looking for you.\pWe hope you w
- 中文：感谢使用\n神秘礼物系统。\p一位训练家已经来到\n琉璃市寻找您。\p系统您可以享受\n与训练家的对战。\p您可以邀请其他训练家\n通过填写密码。\p试着找寻其他\n有用的密码吧。$
- 理由：美版独有文本（日版无对应）。EN "We hope you will enjoy battling the visiting TRAINER." 被译为"系统您可以享受与训练家的对战"，"We hope"误作"系统"，语义错误；补丁忠实复制美版中文（字节一致），错误继承自美版汉化。
- 修改建议：希望您会喜欢\n与这位训练家的对战。

### 凭空捏造（跨世代文本混入）（1 条）
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 12204,
    "decision": "fixed_us_only",
    "review": {
      "row_number": 12204,
      "symbol": "sText_MysteryGiftVisitingTrainerArrived",
      "domain": "untransplanted_full",
      "idx": "",
      "old": "系统您可以享受",
      "new": "希望您可以享受",
      "reason": "系统是希望的误写；日版缺此配信脚本，不新增猜测ROM覆盖。",
      "scope": "us_only",
      "action": "fix",
      "final_text": "感谢使用\n神秘礼物系统。\\p一位训练家已经来到\n琉璃市寻找您。\\p希望您可以享受\n与训练家的对战。\\p您可以邀请其他训练家\n通过填写密码。\\p试着找寻其他\n有用的密码吧。",
      "old_current_text": "感谢使用\n神秘礼物系统。\\p一位训练家已经来到\n琉璃市寻找您。\\p系统您可以享受\n与训练家的对战。\\p您可以邀请其他训练家\n通过填写密码。\\p试着找寻其他\n有用的密码吧。",
      "changed_files": [
        "../pokeemerald_us_chs/data/scripts/gift_trainer.inc"
      ],
      "us_source_file": "data/scripts/gift_trainer.inc",
      "jp_source": []
    }
  }
]
```

### 64. [218]

判定：**已修复**；范围：日版和美版。

理由：两版当前升级数据说明已为“不可思议的盒子。\n西尔佛公司制造”，符合第三世代日英原文。

建议处理：无需重复修改，也不扩展字符映射。

当前日版中文：

来源：`patch/item_descriptions.json`

```text
不可思议的盒子。
西尔佛公司制造
```

当前美版中文：

来源：`src/data/text/item_descriptions.h`

```text
不可思议的盒子。
西尔佛公司制造
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`src/data/text/item_descriptions.h`，版本：`fe570a7e5^`

```text
A peculiar box made
by SILPH CO.
```

v3原报告条目（保留原建议供对照）：

```text
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
```

历史v2记录（不能代替本次复核）：

```json
[
  {
    "row": 10475,
    "decision": "fixed_verified",
    "review": {
      "row_number": 10475,
      "symbol": "",
      "domain": "item",
      "idx": "218",
      "old": null,
      "new": "不可思议的盒子。\n西尔佛公司制造",
      "reason": "按JP/EN原文，仅修文本不改用途。",
      "scope": "both",
      "action": "fix",
      "resolved_symbol": "sUpGradeDesc",
      "final_text": "不可思议的盒子。\n西尔佛公司制造",
      "old_current_text": "内部储存了各种信\n息的透明机器。西\n尔佛公司制造",
      "changed_files": [
        "patch/item_descriptions.json",
        "../pokeemerald_us_chs/src/data/text/item_descriptions.h"
      ],
      "us_source_file": "src/data/text/item_descriptions.h",
      "jp_source": [
        {
          "file": "src/data/text/item_descriptions.h",
          "text": "ふしぎな　はこ\nシルフ　カンパニーせい"
        }
      ]
    }
  }
]
```

### 65. [76]

判定：**可选：未使用特性名称**；范围：两版；可选。

理由：名称表中CACOPHONY确实仍未翻译，日文为そうおん；但Wokann源码只有名称、描述和常量定义，没有宝可梦配置或战斗处理使用此特性。不是普通游戏中的活跃遗漏。

建议处理：若希望完整本地化静态名称表，可把两版此名称改为“噪音”；不要为它新增特性机制或修改宝可梦数据。

当前日版中文：

来源：`patch/ability_names.json`

```text
CACOPHONY
```

当前美版中文：

来源：`src/data/text/abilities.h`

```text
[ABILITY_CACOPHONY] = _("CACOPHONY")
```

英文原文 / 历史源定义（历史表资源若含中文则不作英文原文证据）：

来源：`src/data/text/abilities.h`，版本：`fe570a7e5^`

```text

```

v3原报告条目（保留原建议供对照）：

```text
- JP：そうおん
- EN：CACOPHONY
- 中文：CACOPHONY
- 理由：JP原文「そうおん」（噪音），EN原文「CACOPHONY」，但JP补丁中文与美版中文均为英文原文「CACOPHONY」，从未翻译。
- 修改建议：噪音

## 三、待移植（484 条）
详见 `audit_v3_us_only.csv`。
```
