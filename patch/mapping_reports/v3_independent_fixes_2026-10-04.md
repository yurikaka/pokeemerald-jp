# v3 独立复核方案实施记录（2026-10-04）

## 范围与结果

- 按 `v3_independent_review_2026-10-04` 的35项必修执行：日版35个资源，美版34个资源；第63项美版已修，仅修改日版。
- 第62项为第58项的重复引用，同一金卡资源只修改一次。其余已修、误报、有意排版和可选项未动。
- 本轮不是执行v2/v3合并清单全部46项；v2独有任务留在合并计划中，未标记完成。
- 原报告与独立复核快照保持不变；本文件记录实施后的状态。未commit/push。
- 只改文本资源及金卡玩家名的既有语言切换标记；无ASM、地址覆盖、指针布局、协议、存档写入或字体改动。
- 日版200摄氏度、美版392华氏度：保持区域单位换算，现有字符表没有℃/℉，因此用文字单位。
- 攀瀑不再宣称第三世代有自带畏缩；真实招式参数未修改。
- 无线俱乐部只给非首次说明补靠近朋友提示；首次说明不补。

## 构建与检查

- `jp_make_chs`：PASS
- `jp_make_compare`：PASS: pokeemerald_jp.gba matches rom_jp.sha1
- `us_make`：PASS (non-modern pokeemerald.gba)
- `git_diff_check_both_repositories`：PASS
- `unselected_v3_resources_unchanged`：PASS; suggestion62 aliases fixed58
- `placeholder_and_extended_control_check`：PASS; only two required PLAYER placeholders added in gold-card text; all four PAUSE15 preserved
- `all_original_addresses_and_reference_writes_unchanged`：PASS
- `jp_rom_linked_payload_check`：PASS: 34 batch payloads match generated ASM; description127 updated in the fixed table
- `us_rom_linked_payload_check`：PASS: all34 changed resources match encoded text at linked symbols
- `emulator`：NOT RUN; visual layout and interactive scenes still require emulator testing

## ROM

- `pokeemerald_jp_chs.gba`：SHA-1 `0d03b76d6e042c9ab66302561dbbc11f2c6d889e`。
- `../pokeemerald_us_chs/pokeemerald.gba`：SHA-1 `67c52710cd3afe6d64678f7bc3bdafa67a3cad28`。

## 原地址核验与动态值

- 修改的batch original/reference_writes与HEAD逐项比较相同；没有因美版资源变长复用或推断新日版地址。
- 日版原文与地址证据沿用独立复核中 baserom_jp.gba 解码和 Wokann dev 同名源码交叉核验，详见JSON native_originals及原独立复核JSON。
- 攀瀑机制依据 Wokann `src/data/pokemon/battle_moves.h:1654`：EFFECT_HIT，secondaryEffectChance=0。
- 金卡新增两处 FD01，各自编码为进入日文模式、展开玩家名、恢复中文模式；没有更改名字比较或持久化流程。
- 电视介绍保留 FD02/03/04（训练家、类别、级别），不把级别写成优胜。

## 模拟器回归建议

- 金卡护士对话：两次玩家名、分页、长名字显示。
- 电视BRAVO训练家节目：训练家所有关系、类别与级别、长动态值。
- 首次及再次无线俱乐部说明：只有再次说明包含靠近朋友提示。
- 双打伙伴两段拼接、受惊攻击NPC、火箭发射提示、游戏厅规则、攀瀑说明。
- 本轮未实机或模拟器交互测试，不将构建成功等同于所有页面视觉验收通过。

## 逐项完成记录

### 3. AbandonedShip_Corridors_B1F_Text_DuncanPostBattle

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/197_abandoned_ship.json`。

原日版中文：

我们的船现在搁浅了。\p如果有会潜水的宝可梦的话，\n或许能帮上什么忙……

最终日版中文：

船底已经沉到水里了。\p如果有会潜水的宝可梦，\n也许就能继续前进了……

美版文件：`data/maps/AbandonedShip_Corridors_B1F/scripts.inc`。

原美版中文：

我们的船现在搁浅了。\p如果有会潜水的宝可梦的话，\n或许能帮上什么忙……$

最终美版中文：

船底已经沉到水里了。\p如果有会潜水的宝可梦，\n也许就能继续前进了……$

### 4. AquaHideout_B1F_Text_Grunt3Intro

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/141_aquahideout_b1f.json`。

原日版中文：

燃料供给完成！\n巡航系统正常！\p一切正常，除了一个\n找麻烦的人！

最终日版中文：

燃料补给完毕！\n零食补给完毕！\p接下来只要打倒\n捣乱的家伙就行了！

美版文件：`data/maps/AquaHideout_B1F/scripts.inc`。

原美版中文：

燃料供给完成！\n巡航系统正常！\p一切正常，除了一个\n找麻烦的人！$

最终美版中文：

燃料补给完毕！\n零食补给完毕！\p接下来只要打倒\n捣乱的家伙就行了！$

### 6. BattleFrontier_BattlePikeRoomNormal_Text_AttacksWhenStartled

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/212_battle_frontier_battle_pike_room_normal.json`。

原日版中文：

一旦受到了惊吓就会\n不听指挥胡乱攻击……\p您和您的宝可梦还好吗？

最终日版中文：

突然看见人时会受惊，\n然后扑过来攻击……\p您和您的宝可梦还好吗？

美版文件：`data/maps/BattleFrontier_BattlePikeRoomNormal/scripts.inc`。

原美版中文：

一旦受到了惊吓就会\n不听指挥胡乱攻击……\p您和您的宝可梦还好吗？$

最终美版中文：

突然看见人时会受惊，\n然后扑过来攻击……\p您和您的宝可梦还好吗？$

### 7. LilycoveCity_ContestLobby_Text_ContestFeastForEyes

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/126_lilycovecity_contestlobby.json`。

原日版中文：

哇，观看华丽大赛\n简直是场视觉盛宴！\p你看过那些\n画里的宝可梦吗？

最终日版中文：

来到华丽大赛会场，\n到处都是值得画下来的\l宝可梦呢！

美版文件：`data/maps/LilycoveCity_ContestLobby/scripts.inc`。

原美版中文：

哇，观看华丽大赛\n简直是场视觉盛宴！\p你看过那些\n画里的宝可梦吗？$

最终美版中文：

哇，观看华丽大赛\n简直是场视觉盛宴！\p看看这些让人\n忍不住想画下来的宝可梦！$

### 8. MauvilleCity_Text_UncleNoNeedToBeDown

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/050_mauvillecity.json`。

原日版中文：

叔叔：满充，\n别这么沮丧。\p想想是什么激励着你\n要变得越来越强的？\p好了，我们回家吧，\n大家都在等你呢。

最终日版中文：

叔叔：满充，\n别这么沮丧。\p今后继续努力，\n变得越来越强就好啦！\p好了，我们回家吧，\n大家都在等你呢。

美版文件：`data/maps/MauvilleCity/scripts.inc`。

原美版中文：

叔叔：满充，\n别这么沮丧。\p想想是什么激励着你\n要变得越来越强的？\p好了，我们回家吧，\n大家都在等你呢。$

最终美版中文：

叔叔：满充，\n别这么沮丧。\p今后继续努力，\n变得越来越强就好啦！\p好了，我们回家吧，\n大家都在等你呢。$

### 9. MossdeepCity_GameCorner_1F_Text_TalkToOldManToPlay

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/151_mossdeepcity_gamecorner_1f.json`。

原日版中文：

如果您想玩游戏，\n就告诉我后面的老人。

最终日版中文：

如果您想玩游戏，\n就告诉我旁边的老人。

美版文件：`data/text/cable_club.inc`。

原美版中文：

如果您想玩游戏，\n就告诉我后面的老人。$

最终美版中文：

如果您想玩游戏，\n就告诉我旁边的老人。$

### 11. MossdeepCity_SpaceCenter_1F_Text_HaywireButRocketLaunchImminent

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/157_mossdeepcity_spacecenter_1f.json`。

原日版中文：

我知道现在一切有些混乱，\n但是……\p火箭发射程序不会停止！

最终日版中文：

我知道现在一切有些混乱，\n但是……\p火箭马上就要发射了！

美版文件：`data/maps/MossdeepCity_SpaceCenter_1F/scripts.inc`。

原美版中文：

我知道现在一切有些混乱，\n但是……\p火箭发射程序不会停止！$

最终美版中文：

我知道现在一切有些混乱，\n但是……\p火箭马上就要发射了！$

### 12. MoveTutor_Text_SubstituteTeach

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/340_move_tutors.json`。

原日版中文：

当我在屋顶上看着\n这广阔的世界时……\p我在想如果这个世界\n有不止一个自己该多有趣啊，\l那样我就能体验各种各样的人生了。\p当然这是不可能的。\n嘿嘿……\p明白了！\n不如让你的宝可梦学习替身吧？

最终日版中文：

当我在屋顶上看着\n这广阔的世界时……\p我在想如果这个世界\n有不止一个自己该多有趣啊，\l那样我就能体验各种各样的人生了。\p当然这是不可能的。\n嘿嘿……\p对了！\n不如让你的宝可梦学习替身吧？

美版文件：`data/text/move_tutors.inc`。

原美版中文：

当我在屋顶上看着\n这广阔的世界时……\p我在想如果这个世界\n有不止一个自己该多有趣啊，\l那样我就能体验各种各样的人生了。\p当然这是不可能的。\n嘿嘿……\p明白了！\n不如让你的宝可梦学习替身吧？$

最终美版中文：

当我在屋顶上看着\n这广阔的世界时……\p我在想如果这个世界\n有不止一个自己该多有趣啊，\l那样我就能体验各种各样的人生了。\p当然这是不可能的。\n嘿嘿……\p对了！\n不如让你的宝可梦学习替身吧？$

### 13. Route116_Text_JoeyIntro

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/028_route116.json`。

原日版中文：

我的宝可梦运用！\n你就好好瞧瞧吧！

最终日版中文：

我的宝可梦很厉害！\n你就好好瞧瞧吧！

美版文件：`data/text/trainers.inc`。

原美版中文：

我的宝可梦运用！\n你就好好瞧瞧吧！$

最终美版中文：

我的宝可梦很厉害！\n你就好好瞧瞧吧！$

### 14. Route123_Text_BraxtonPostBattle

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/148_route123.json`。

原日版中文：

在那样的对战中获得徽章\n是你的骄傲。

最终日版中文：

这场战斗真是\n无愧于你的道馆徽章！

美版文件：`data/text/trainers.inc`。

原美版中文：

在那样的对战中获得徽章\n是你的骄傲。$

最终美版中文：

这场战斗真是\n无愧于你的道馆徽章！$

### 15. SecretBase_Text_Trainer1PreChampion

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/391_secret_base_trainers.json`。

原日版中文：

这个地方非常受欢迎，\n经常会有人来这里。\p我一直在等它打开，\n我一定要得到它！

最终日版中文：

这个地方很受欢迎，\n总是有人占着。\p我等了很久，\n终于轮到我使用了！

美版文件：`data/text/secret_base_trainers.inc`。

原美版中文：

这个地方非常受欢迎，\n经常会有人来这里。\p我一直在等它打开，\n我一定要得到它！$

最终美版中文：

这个地方很受欢迎，\n总是有人占着。\p我等了很久，\n终于轮到我使用了！$

### 16. BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteMMon1

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`。

原日版中文：

我有一对高贵的宝可梦。\n一只掌握{FD_02}的{FD_03}和

最终日版中文：

我培育的宝可梦是……\n一只掌握{FD_02}的{FD_03}和

美版文件：`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`。

原美版中文：

我有一对高贵的宝可梦。\n一只掌握{STR_VAR_1}的{STR_VAR_2}和$

最终美版中文：

我有两只不错的宝可梦。\n一只掌握{STR_VAR_1}的{STR_VAR_2}和$

### 17. BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteMMon2Ask

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`。

原日版中文：

一只掌握{FD_02}的{FD_03}！\p如果我们组队，那是多高雅的\n一件事呀，你觉得呢？

最终日版中文：

一只掌握{FD_02}的{FD_03}！\p如果我们一起组队\n一定很不错，你觉得呢？

美版文件：`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`。

原美版中文：

一只掌握{STR_VAR_1}的{STR_VAR_2}！\p如果我们组队，那是多高雅的\n一件事呀，你觉得呢？$

最终美版中文：

一只掌握{STR_VAR_1}的{STR_VAR_2}！\p如果我们一起组队\n一定很不错，你觉得呢？$

### 18. BattleFrontier_Lounge5_Text_LadyClaimsSheUnderstandsPokemon

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/399_frontier_lounge5.json`。

原日版中文：

好像魔法一样啊！\n那边那位小女孩说她能\l懂得宝可梦在说什么！

最终日版中文：

真有意思！\n那位小女孩说她能\l懂得宝可梦的心情！

美版文件：`data/maps/BattleFrontier_Lounge5/scripts.inc`。

原美版中文：

好像魔法一样啊！\n那边那位小女孩说她能\l懂得宝可梦在说什么！$

最终美版中文：

真有意思！\n那位小女孩说她能\l懂得宝可梦的心情！$

### 19. BattleFrontier_OutsideEast_Text_ThriveInDarkness

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/227_battle_frontier_outside_east.json`。

原日版中文：

我最喜欢黑暗……\n是的……哪里最适合我？\l必然是对战金字塔……\p在黑暗中探索的时候\n你是不是也会陷入完全的绝望？

最终日版中文：

我最喜欢黑暗……\n是的……哪里最适合我？\l必然是对战金字塔……\p你也要不要在黑暗中\n拼命探索一番……？

美版文件：`data/maps/BattleFrontier_OutsideEast/scripts.inc`。

原美版中文：

我最喜欢黑暗……\n是的……哪里最适合我？\l必然是对战金字塔……\p在黑暗中探索的时候\n你是不是也会陷入完全的绝望？$

最终美版中文：

我最喜欢黑暗……\n是的……哪里最适合我？\l必然是对战金字塔……\p你也要不要在黑暗与\n彻底的绝望中探索一番？$

### 20. DewfordTown_Gym_Text_BrendenIntro

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/023_dewford_gym.json`。

原日版中文：

让你看看\n水手的智慧！

最终日版中文：

让你看看\n海之男儿的骨气！

美版文件：`data/maps/DewfordTown_Gym/scripts.inc`。

原美版中文：

让你看看\n水手的智慧！$

最终美版中文：

让你看看\n海之男儿的骨气！$

### 22. FortreeCity_House1_Text_GoingToMakeVolbeatStrong

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/107_fortreecity_house1.json`。

原日版中文：

从现在开始，我要把甜甜萤\n养得壮壮的！\p你也要善待正电拍拍啊！

最终日版中文：

从现在开始，我要把甜甜萤\n养得壮壮的！\p你也要把正电拍拍\n培养得更强啊！

美版文件：`data/maps/FortreeCity_House1/scripts.inc`。

原美版中文：

从现在开始，我要把甜甜萤\n养得壮壮的！\p你也要善待正电拍拍啊！$

最终美版中文：

从现在开始，我要把甜甜萤\n养得壮壮的！\p你也要把正电拍拍\n培养得更强啊！$

### 31. LilycoveCity_PokemonTrainerFanClub_Text_YoureOneWeWantToWin

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/139_lilycovecity_pokemontrainerfanclub.json`。

原日版中文：

嗨，{FD_01}！\n我们一直想要胜过你！

最终日版中文：

嗨，{FD_01}！\n我们希望你能获胜！

美版文件：`data/maps/LilycoveCity_PokemonTrainerFanClub/scripts.inc`。

原美版中文：

嗨，{PLAYER}！\n我们一直想要胜过你！$

最终美版中文：

嗨，{PLAYER}！\n我们希望你能获胜！$

### 32. GraniteCave_StevensRoom_Text_ImStevenLetterForMe

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/027_stevens_room.json`。

原日版中文：

我的名字是大吾。\p我对稀有的石头很有兴趣，\n所有经常四处旅行。\p哦？\n有给我的信？

最终日版中文：

我的名字是大吾。\p我对稀有的石头很有兴趣，\n所以经常四处旅行。\p哦？\n有给我的信？

美版文件：`data/maps/GraniteCave_StevensRoom/scripts.inc`。

原美版中文：

我的名字是大吾。\p我对稀有的石头很有兴趣，\n所有经常四处旅行。\p哦？\n有给我的信？$

最终美版中文：

我的名字是大吾。\p我对稀有的石头很有兴趣，\n所以经常四处旅行。\p哦？\n有给我的信？$

### 36. gTVPokemonNewsBattleFrontierText11

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/386_tv_0.json`。

原日版中文：

训练家{FD_02}在\n在对战宫殿单打对战厅中\l创造了{FD_03}连胜的新纪录。\p让我们为{FD_02}欢呼！

最终日版中文：

训练家{FD_02}在\n对战宫殿单打对战厅中\l创造了{FD_03}连胜的新纪录。\p让我们为{FD_02}欢呼！

美版文件：`data/text/tv.inc`。

原美版中文：

训练家{STR_VAR_1}在\n在对战宫殿单打对战厅中\l创造了{STR_VAR_2}连胜的新纪录。\p让我们为{STR_VAR_1}欢呼！$

最终美版中文：

训练家{STR_VAR_1}在\n对战宫殿单打对战厅中\l创造了{STR_VAR_2}连胜的新纪录。\p让我们为{STR_VAR_1}欢呼！$

### 37. gTVPokemonNewsBattleFrontierText12

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/386_tv_0.json`。

原日版中文：

训练家{FD_02}在\n在对战宫殿双打对战厅中\l创造了{FD_03}连胜的新纪录。\p让我们为{FD_02}欢呼！

最终日版中文：

训练家{FD_02}在\n对战宫殿双打对战厅中\l创造了{FD_03}连胜的新纪录。\p让我们为{FD_02}欢呼！

美版文件：`data/text/tv.inc`。

原美版中文：

训练家{STR_VAR_1}在\n在对战宫殿双打对战厅中\l创造了{STR_VAR_2}连胜的新纪录。\p让我们为{STR_VAR_1}欢呼！$

最终美版中文：

训练家{STR_VAR_1}在\n对战宫殿双打对战厅中\l创造了{STR_VAR_2}连胜的新纪录。\p让我们为{STR_VAR_1}欢呼！$

### 40. CableClub_Text_ExplainWirelessClub

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/359_cable_club.json`。

原日版中文：

让我给您介绍一下\n无线俱乐部吧。\p在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果无线适配器没有连接，\n您仍然可以使用GBA连接线进行连接。\p这种情况下，\n您就需要进入直接连接室。\p希望您能享受无线连接系统\n的乐趣。

最终日版中文：

让我给您介绍一下\n无线俱乐部吧。\p在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果在联盟交谊厅或\n直接连接室找不到朋友，\p请试着靠近朋友一些。\p如果无线适配器没有连接，\n您仍然可以使用GBA连接线进行连接。\p这种情况下，\n您就需要进入直接连接室。\p希望您能享受无线连接系统\n的乐趣。

美版文件：`data/text/cable_club.inc`。

原美版中文：

让我给您介绍一下\n无线俱乐部吧。\p在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果无线适配器没有连接，\n您仍然可以使用GBA连接线进行连接。\p这种情况下，\n您就需要进入直接连接室。\p希望您能享受无线连接系统\n的乐趣。$

最终美版中文：

让我给您介绍一下\n无线俱乐部吧。\p在这层有2个房间。\p首先是左边的房间，\n这是联盟交谊厅。\p您能够和那些在您周围并且也进入\n该房间的训练家进行连接。\p您可以和他们一起进行\n聊天、对战或交换。\p其次是右边的房间，\n叫做直接连接室。\p您可以和他们进行\n交换或对战。\p如果在联盟交谊厅或\n直接连接室找不到朋友，\p请试着靠近朋友一些。\p如果无线适配器没有连接，\n您仍然可以使用GBA连接线进行连接。\p这种情况下，\n您就需要进入直接连接室。\p希望您能享受无线连接系统\n的乐趣。$

### 42. LavaridgeTown_Gym_1F_Text_GeraldIntro

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/079_lavaridgetown_gym_1f.json`。

原日版中文：

你的宝可梦能抵挡\n392度的高温吗？

最终日版中文：

你的宝可梦能抵挡\n200摄氏度的高温吗？

美版文件：`data/maps/LavaridgeTown_Gym_1F/scripts.inc`。

原美版中文：

你的宝可梦能抵挡\n392度的高温吗？$

最终美版中文：

你的宝可梦能抵挡\n392华氏度的高温吗？$

实施说明：℃ and ℉ are not mapped in the existing character set. Use 200摄氏度 in JP and 392华氏度 in US; no charmap/font modifications.

### 43. LavaridgeTown_Gym_1F_Text_GeraldPostBattle

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/079_lavaridgetown_gym_1f.json`。

原日版中文：

岩浆的温度\n是392度。\p你的宝可梦打败了我，那么在岩浆中\n也应该能比较容易生存下来。

最终日版中文：

岩浆的温度\n是200摄氏度。\p你的宝可梦打败了我，那么在岩浆中\n也应该能比较容易生存下来。

美版文件：`data/maps/LavaridgeTown_Gym_1F/scripts.inc`。

原美版中文：

岩浆的温度\n是392度。\p你的宝可梦打败了我，那么在岩浆中\n也应该能比较容易生存下来。$

最终美版中文：

岩浆的温度\n是392华氏度。\p你的宝可梦打败了我，那么在岩浆中\n也应该能比较容易生存下来。$

实施说明：℃ and ℉ are not mapped in the existing character set. Use 200摄氏度 in JP and 392华氏度 in US; no charmap/font modifications.

### 44. gText_BecameMoreConsciousOfOtherMons

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/405_contest_strings.json`。

原日版中文：

它变得比平时\n更加担心其他宝可梦了！{FC_08 0f}{FC_08 0f}{FC_08 0f}{FC_08 0f}

最终日版中文：

它变得比平时\n更加在意其他宝可梦了！{FC_08 0f}{FC_08 0f}{FC_08 0f}{FC_08 0f}

美版文件：`data/text/contest_strings.inc`。

原美版中文：

它变得比平时\n更加担心其他宝可梦了！{PAUSE 15}{PAUSE 15}{PAUSE 15}{PAUSE 15}$

最终美版中文：

它变得比平时\n更加在意其他宝可梦了！{PAUSE 15}{PAUSE 15}{PAUSE 15}{PAUSE 15}$

### 46. sWaterfallDescription

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/move_descriptions.json`。

原日版中文：

以惊人的气势扑向对手。\n有时会使对手畏缩。

最终日版中文：

以惊人的气势扑向对手。

美版文件：`src/data/text/move_descriptions.h`。

原美版中文：

以惊人的气势扑向对手。\n有时会使对手畏缩。

最终美版中文：

以惊人的气势扑向对手。

### 52. BattleFrontier_Lounge2_Text_AmazingPowersOfObservation

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/432_checklist_scripts.json`。

原日版中文：

调查资料好厉害！\n老师果然非同一般！

最终日版中文：

好厉害的观察力！\n前辈果然非同一般！

美版文件：`data/maps/BattleFrontier_Lounge2/scripts.inc`。

原美版中文：

调查资料好厉害！\n老师果然非同一般！$

最终美版中文：

好厉害的观察力！\n前辈果然非同一般！$

### 54. LilycoveCity_ContestHall_Text_SuchCharmingCuteAppeals

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/125_lilycovecity_contesthall.json`。

原日版中文：

评委：啊，如此迷人，\n如此可爱！\p哎，天啊！那水之游\n多么完美，多么可爱！

最终日版中文：

评委：啊，如此迷人，\n如此可爱！\p哎，天啊！那玩水\n多么完美，多么可爱！

美版文件：`data/maps/LilycoveCity_ContestHall/scripts.inc`。

原美版中文：

评委：啊，如此迷人，\n如此可爱！\p哎，天啊！那水之游\n多么完美，多么可爱！$

最终美版中文：

评委：啊，如此迷人，\n如此可爱！\p哎，天啊！那玩水\n多么完美，多么可爱！$

### 55. LilycoveCity_CoveLilyMotel_1F_Text_HeardAquaHideoutBusted

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/127_lilycovecity_covelilymotel_1f.json`。

原日版中文：

啊，抱歉，抱歉！\n我看电视看入迷了！\p我听说有人到捣毁了\n海洋队的基地，\p多亏如此，我们刚刚\n接到了一个大团体订房预约，\p是一个公司，叫做……呃……\n游戏什么的……

最终日版中文：

啊，抱歉，抱歉！\n我看电视看入迷了！\p我听说有人捣毁了\n海洋队的基地，\p多亏如此，我们刚刚\n接到了一个大团体订房预约，\p是一个公司，叫做……呃……\n游戏什么的……

美版文件：`data/maps/LilycoveCity_CoveLilyMotel_1F/scripts.inc`。

原美版中文：

啊，抱歉，抱歉！\n我看电视看入迷了！\p我听说有人到捣毁了\n海洋队的基地，\p多亏如此，我们刚刚\n接到了一个大团体订房预约，\p是一个公司，叫做……呃……\n游戏什么的……$

最终美版中文：

啊，抱歉，抱歉！\n我看电视看入迷了！\p我听说有人捣毁了\n海洋队的基地，\p多亏如此，我们刚刚\n接到了一个大团体订房预约，\p是一个公司，叫做……呃……\n游戏什么的……$

### 57. MossdeepCity_GameCorner_1F_Text_DescribeWhichGame

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/151_mossdeepcity_gamecorner_1f.json`。

原日版中文：

需要的话，\n我可以向您解说对战规则。\p需要解说哪一项？

最终日版中文：

需要的话，\n我可以向您解说游戏规则。\p需要解说哪一项？

美版文件：`data/text/cable_club.inc`。

原美版中文：

需要的话，\n我可以向您解说对战规则。\p需要解说哪一项？$

最终美版中文：

需要的话，\n我可以向您解说游戏规则。\p需要解说哪一项？$

### 58. gText_NoticesGoldCard

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/196_pokemon_centers.json`。

原日版中文：

那、那张卡！？\p难道是金卡！？\p金色真耀眼！！\n四颗星在闪耀！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有比这更厉害的\n训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！

最终日版中文：

那、那张卡！？\p难道是金卡！？\p金色真耀眼！！\n四颗星在闪耀！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有金卡的训练家，\n{FD_01}您还是第一位！\p那么，请让我为{FD_01}的\n宝可梦休息一下吧！

美版文件：`data/text/pkmn_center_nurse.inc`。

原美版中文：

那、那张卡！？\p难道是金卡！？\p金色真耀眼！！\n四颗星在闪耀！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有比这更厉害的\n训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！$

最终美版中文：

那、那张卡！？\p难道是金卡！？\p金色真耀眼！！\n四颗星在闪耀！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有金卡的训练家，\n{PLAYER}您还是第一位！\p那么，请让我为{PLAYER}的\n宝可梦休息一下吧！$

实施说明：Add japanese_placeholders:[1] so restored PLAYER substitutions use the existing Japanese-name display path.

### 59. RustboroCity_DevonCorp_1F_Text_HowCouldWeGetRobbed

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/031_rustborocity_devoncorp_1f.json`。

原日版中文：

说什么傻话，\n谁会抢我们的东西？

最终日版中文：

包裹居然被抢走了，\n我们也太不小心了……

美版文件：`data/maps/RustboroCity_DevonCorp_1F/scripts.inc`。

原美版中文：

说什么傻话，\n谁会抢我们的东西？$

最终美版中文：

包裹居然被抢走了，\n我们也太不小心了……$

### 60. RustboroCity_PokemonSchool_Text_ExplainPoison

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/038_rustborocity_pokemonschool.json`。

原日版中文：

宝可梦中毒后，\n会慢慢损失体力，\p此效果在战斗后\n依然残留。\p在探险中，中毒的宝可梦的体力P\n也会不断减少。\p使用解毒药可解毒。

最终日版中文：

宝可梦中毒后，\n会慢慢损失体力，\p此效果在战斗后\n依然残留。\p在探险中，中毒的宝可梦的HP\n也会不断减少。\p使用解毒药可解毒。

美版文件：`data/maps/RustboroCity_PokemonSchool/scripts.inc`。

原美版中文：

宝可梦中毒后，\n会慢慢损失体力，\p此效果在战斗后\n依然残留。\p在探险中，中毒的宝可梦的体力P\n也会不断减少。\p使用解毒药可解毒。$

最终美版中文：

宝可梦中毒后，\n会慢慢损失体力，\p此效果在战斗后\n依然残留。\p在探险中，中毒的宝可梦的HP\n也会不断减少。\p使用解毒药可解毒。$

### 61. gTVBravoTrainerText00

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/386_tv_0.json`。

原日版中文：

太好了！\n现在是BRAVO训练家时间！\p今天我们所要介绍的\n主角就是{FD_02}。\p现在，这只宝可梦在{FD_03}\n比赛中荣获{FD_04}优胜。

最终日版中文：

太好了！\n现在是BRAVO训练家时间！\p今天我们要介绍的，\n是{FD_02}的宝可梦！\p这只宝可梦在{FD_03}\n比赛中达到了{FD_04}级别。

美版文件：`data/text/tv.inc`。

原美版中文：

太好了！\n现在是BRAVO训练家时间！\p今天我们所要介绍的\n主角就是{STR_VAR_1}。\p现在，这只宝可梦在{STR_VAR_2}\n比赛中荣获{STR_VAR_3}优胜。$

最终美版中文：

太好了！\n现在是BRAVO训练家时间！\p今天我们要介绍的，\n是{STR_VAR_1}的宝可梦！\p这只宝可梦在{STR_VAR_2}\n比赛中达到了{STR_VAR_3}级别。$

### 63. sText_MysteryGiftVisitingTrainerArrived

状态：已修改、已构建，未模拟器验收。

日版文件：`patch/batches/471_checklist_mystery_gift_script_texts.json`。

原日版中文：

感谢使用\n神秘礼物系统。\p一位训练家已经来到\n琉璃市寻找您。\p系统您可以享受\n与训练家的对战。\p您可以邀请其他训练家\n通过填写密码。\p试着找寻其他\n有用的密码吧。

最终日版中文：

感谢使用\n神秘礼物系统。\p一位训练家已经来到\n琉璃市寻找您。\p希望您可以享受\n与训练家的对战。\p您可以邀请其他训练家\n通过填写密码。\p试着找寻其他\n有用的密码吧。

美版已修复，本轮保持不变。

实施说明：US already fixed; change JP only. Do not alter Mystery Gift passwords/protocol logic.
