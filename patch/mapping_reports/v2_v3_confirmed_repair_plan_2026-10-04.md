# v2 / v3 独立复核后的修复清单

两轮各自读取原报告和一手证据，判定完成后才按资源合并。审查阶段未修改游戏；后续已按本计划实施，未提交推送。

## 实施进度

- 日版46个去重必修资源全部修复并构建；美版42个资源同步修复。剩余必修任务0项。
- v3的35项见 `v3_independent_fixes_2026-10-04.md`；v2独有11项见 `v2_exclusive_fixes_2026-10-04.md`。
- 两版构建、日版原版compare、文本/ROM编码检查通过；待模拟器交互及画面验收。
- 日版仍输出 `pokeemerald_jp_chs.gba`；未commit/push。

- v2需行动16条，其中部分是原问题已修后新发现的残余/格式问题；v3需行动35项。
- 交集5个资源；合并后46个资源任务；v3第62项并入第58项。
- v2/v3并非全部文本重新翻译清单；未提供的v3 484条清单不计入完成范围。
- 日版独有语义、参数、密码不能直接复制英文；円后置、道具说明不加结尾句号、训练家笔记布局均保持。
- 神秘礼物已核对输入消费方按词条编号校验：日版恢复原日文密码及Joy Spot提示，仅改显示资源。

## 实施前的专项验证

- 攀瀑：Wokann `src/data/pokemon/battle_moves.h:1654` 为 EFFECT_HIT，secondaryEffectChance=0；不是第四世代畏缩。
- 文柚果：Wokann `src/data/items.h:1726` 固定回复参数30，不改成最大HP百分比。
- 图鉴排序：Wokann `src/pokedex.c:3913` 使用原 gPokedexOrder_Alphabetical；未实施拼音排序。
- 神秘礼物：日文原资源0x085FCDBC、0x085FCE8B；Wokann未解析符号不代表日版不存在。
- Repel：美版 `data/scripts/repel.inc:2` 先填 STR_VAR_1；当前不列修复。
- 温度：日版200℃与美版392℉互为换算；实施前检查℃/℉可编码、字体有字形，必要时写中文单位。
- 电视/对话参数：PLAYER、STR_VAR、FD、F7按各自消费者保持，不引入存档写入变化。

## 去重后的任务

### 1. MossdeepCity_Gym_Text_CliffordPostBattle

实施状态：已修复并构建；待模拟器验收。

来源：v2:4397

日版：`patch/batches/152_mossdeepcity_gym.json`

美版：`data/maps/MossdeepCity_Gym/scripts.inc`

范围：JP

原因：日英版本差异，不应套用英文败战台词。日文在说道馆馆主年轻有活力，不是在说玩家。

修复方案/目标文字：

这里的道馆馆主也一样！\n年轻又充满活力！

### 2. gText_DexSortAtoZDescription

实施状态：已修复并构建；待模拟器验收。

来源：v2:4798

日版：`patch/batches/171_pokedex.json`

美版：`src/strings.c`

范围：JP

原因：日文明确是五十音顺序；实际调用 gPokedexOrder_Alphabetical，并未改成中文拼音排序。字母顺序的说明会误导。

修复方案/目标文字：

按名称顺序排列\n已发现的宝可梦。

### 3. gText_NoticesGoldCard

实施状态：已修复并构建；待模拟器验收。

来源：v2:5803、v3:58

日版：`patch/batches/196_pokemon_centers.json`

美版：`data/text/pkmn_center_nurse.inc`

范围：JP+US

原因：金卡、金色、四颗星已补回，但后半仍没有明确金卡，且遗漏原文两次玩家名；属于部分修复。

修复方案/目标文字：

保留已恢复的开头；后半改为“但拥有金卡的训练家，\l{PLAYER}您还是第一位！\p那么，请让我为{PLAYER}的\n宝可梦休息一下吧！”；日版用原 FD_01。

范围：JP+US

原因：当前已恢复金卡/金色/四星，但未恢复金卡持有者的限定和两次玩家名。

修复方案/目标文字：

后半明确“拥有金卡的训练家”，恢复两处 PLAYER；日版使用 FD_01。

### 4. BattleFrontier_BattlePikeRoomNormal_Text_AttacksWhenStartled

实施状态：已修复并构建；待模拟器验收。

来源：v2:6256、v3:6

日版：`patch/batches/212_battle_frontier_battle_pike_room_normal.json`

美版：`data/maps/BattleFrontier_BattlePikeRoomNormal/scripts.inc`

范围：JP+US

原因：突然看见人受惊后扑过来，不是“不听指挥”。原文不存在“命令を無視して”。

修复方案/目标文字：

突然看见人时会受惊，\n然后扑过来攻击……\p您和您的宝可梦还好吗？

范围：JP+US

原因：受惊后突然袭击，不是违抗命令。

修复方案/目标文字：

突然看见人时会受惊，\n然后扑过来攻击……\p您和您的宝可梦还好吗？

### 5. BattleFrontier_OutsideEast_Text_ThriveInDarkness

实施状态：已修复并构建；待模拟器验收。

来源：v2:6921、v3:19

日版：`patch/batches/227_battle_frontier_outside_east.json`

美版：`data/maps/BattleFrontier_OutsideEast/scripts.inc`

范围：JP+US

原因：第一句已修好；结尾仍将邀请一起探索变成问对方是否绝望。日文没有英文的 total desperation，不强行统一区域差异。

修复方案/目标文字：

日版结尾：你也要不要在黑暗中\n拼命探索一番……？；美版结尾：你也要不要在黑暗与\n彻底的绝望中探索一番？

范围：JP+US

原因：开头已修，邀请探索的结尾仍误译；日英区域差异应保留。

修复方案/目标文字：

日版邀请在黑暗中拼命探索；美版邀请在黑暗与彻底绝望中探索，不再询问“你是不是也会陷入”。

### 6. RustboroCity_House3_Text_NamingPikachuPekachu

实施状态：已修复并构建；待模拟器验收。

来源：v2:7183

日版：`patch/batches/299_rustboro_city_house3.json`

美版：`data/maps/RustboroCity_House3/scripts.inc`

范围：JP+US

原因：PEKACHU/ペカチュウ是 PIKACHU/ピカチュウ的轻微改名；“猫卡球”丢失这一笑点。只改对话文本，不改保存的昵称。

修复方案/目标文字：

但给皮卡丘起名叫\n“佩卡丘”，几乎没什么区别吧……\p我想最好起个容易\n让人理解的名字，但是……；美版第二分句可保留“这没什么意义”。

### 7. RustboroCity_House3_Text_Pekachu

实施状态：已修复并构建；待模拟器验收。

来源：v2:7184

日版：`patch/batches/299_rustboro_city_house3.json`

美版：`data/maps/RustboroCity_House3/scripts.inc`

范围：JP+US

原因：承接上一条的同一昵称与叫声，需一并统一。只改对话资源。

修复方案/目标文字：

佩卡丘：佩卡！

### 8. MoveTutor_Text_SubstituteTeach

实施状态：已修复并构建；待模拟器验收。

来源：v2:7558、v3:12

日版：`patch/batches/340_move_tutors.json`

美版：`data/text/move_tutors.inc`

范围：JP+US

原因：重复“如果”已经修复；但 そうだわ / I know! 在此是想到一个主意，不是明白了别人说的话。

修复方案/目标文字：

仅将“明白了！”改为“对了！”，保留后续替身教学。

范围：JP+US

原因：突然想到一个主意，不是理解了。

修复方案/目标文字：

“明白了！”改“对了！”。

### 9. MauvilleCity_PokemonCenter_1F_Text_LedgesJumpedStory

实施状态：已修复并构建；待模拟器验收。

来源：v2:9110

日版：`patch/batches/392_mauville_man_0.json`

美版：`data/scripts/mauville_man.inc`

范围：JP+US

原因：“几经”和计数已修复，但把 ledges / だんさ译成岩礁，仍然错误；说的是地图可跳下的台阶。

修复方案/目标文字：

将两处“岩礁”改为“台阶”；计数、名字占位符及分页保留。

### 10. sElixirDesc

实施状态：已修复并构建；待模拟器验收。

来源：v2:10293

日版：`patch/item_descriptions.json`

美版：`src/data/text/item_descriptions.h`

范围：JP+US

原因：原报告针对第四个招式的信息，当前没有该语义遗漏；独立检查发现“10PP”被断成“1\n0PP”，应避免数字跨行。

修复方案/目标文字：

能让宝可梦学会的\n4个招式各回复\n10PP；不拆 PP，不加结尾句号。

### 11. sSitrusBerryDesc

实施状态：已修复并构建；待模拟器验收。

来源：v2:10399

日版：`patch/item_descriptions.json`

美版：`src/data/text/item_descriptions.h`

范围：JP+US

原因：本作日英原文都明确回复30HP；实际 ITEM_SITRUS_BERRY 的 holdEffectParam 为30。“少量”省略可操作的固定数值。

修复方案/目标文字：

携带后，可以回复\n30HP；不采用后世代百分比机制，不加结尾句号。

### 12. sText_MysteryGiftVisitingTrainerInstructions

实施状态：已修复并构建；待模拟器验收。

来源：v2:12203

日版：`patch/batches/471_checklist_mystery_gift_script_texts.json`

美版：`data/scripts/gift_trainer.inc`

范围：JP

原因：美版已补“在”；日版仍缺介词。日版有实际资源，并非“无对应”。另发现提示密码与服务名套用了英文版本。

修复方案/目标文字：

语法先改为“您可以在友好商店\l参与调查。”；完整区域适配应恢复原提示密码“すごい トレーナー / くれ くれ”和 Joy Spot 说明，保留密码原语言、输入及协议逻辑。实际输入验证路径尚需追踪后再落地密码部分。

### 13. sText_MysteryGiftVisitingTrainerArrived

实施状态：已修复并构建；待模拟器验收。

来源：v2:12204、v3:63

日版：`patch/batches/471_checklist_mystery_gift_script_texts.json`

美版：`data/scripts/gift_trainer.inc`

范围：JP

原因：美版已经修为希望；日版 batch471 尚为系统。日版原 ROM 0x085FCE8B 有对应文本。

修复方案/目标文字：

仅将“系统您可以享受”改为“希望您可以享受”。

范围：JP

原因：美版已改希望，日版仍是系统。报告“日版无对应”不成立，ROM有0x085FCE8B。

修复方案/目标文字：

“系统您可以享受”改为“希望您可以享受”。

### 14. sText_OnlyPkmnForBattle

实施状态：已修复并构建；待模拟器验收。

来源：v2:13248

日版：`patch/batches/438_checklist_controls_and_gambler.json`

美版：`src/data/trade.h`

范围：JP+US

原因：已有移植，不是遗漏。但“最后1只同行的宝可梦”不等于“唯一能战斗的宝可梦”：还可能有其他濒死宝可梦或蛋。

修复方案/目标文字：

交换这只宝可梦后，\n就没有能战斗的宝可梦了。；保留日版原有颜色控制符。

### 15. gText_MomOrDadMightLikeThisProgram

实施状态：已修复并构建；待模拟器验收。

来源：v2:13286

日版：`patch/batches/432_checklist_scripts.json`

美版：`data/event_scripts.s`

范围：JP+US

原因：已有移植，不是遗漏。ばんぐみ / program 在这里是电视节目，不是游戏。

修复方案/目标文字：

仅将“喜欢的游戏”改为“喜欢的节目”，保留父母动态显示变量。

### 16. gText_PlayerWhitedOut

实施状态：已修复并构建；待模拟器验收。

来源：v2:13293

日版：`patch/batches/432_checklist_scripts.json`

美版：`data/event_scripts.s`

范围：JP+US

原因：已有移植，不是遗漏。第一句叹号被移到第二页开头，形成“！玩家……”；日英原文的叹号都在第一句末。

修复方案/目标文字：

将“战斗的宝可梦\p！”改为“战斗的宝可梦！\p”，不改其他分页和玩家名路径。

### 17. AbandonedShip_Corridors_B1F_Text_DuncanPostBattle

实施状态：已修复并构建；待模拟器验收。

来源：v3:3

日版：`patch/batches/197_abandoned_ship.json`

美版：`data/maps/AbandonedShip_Corridors_B1F/scripts.inc`

范围：JP+US

原因：船底沉入水中，不是船搁浅。

修复方案/目标文字：

船底已经沉到水里了。\p如果有会潜水的宝可梦，\n也许就能继续前进了……

### 18. AquaHideout_B1F_Text_Grunt3Intro

实施状态：已修复并构建；待模拟器验收。

来源：v3:4

日版：`patch/batches/141_aquahideout_b1f.json`

美版：`data/maps/AquaHideout_B1F/scripts.inc`

范围：JP+US

原因：おやつ / snacks 是零食；还遗漏打倒捣乱者的动作。

修复方案/目标文字：

燃料补给完毕！\n零食补给完毕！\p接下来只要打倒\n捣乱的家伙就行了！

### 19. LilycoveCity_ContestLobby_Text_ContestFeastForEyes

实施状态：已修复并构建；待模拟器验收。

来源：v3:7

日版：`patch/batches/126_lilycovecity_contestlobby.json`

美版：`data/maps/LilycoveCity_ContestLobby/scripts.inc`

范围：JP+US

原因：值得画成画的宝可梦，不是已经在画里的宝可梦。

修复方案/目标文字：

日版：来到华丽大赛会场，\n到处都是值得画下来的\l宝可梦呢！；美版保留视觉盛宴开头，后面改“看看这些让人\n忍不住想画下来的宝可梦！”

### 20. MauvilleCity_Text_UncleNoNeedToBeDown

实施状态：已修复并构建；待模拟器验收。

来源：v3:8

日版：`patch/batches/050_mauvillecity.json`

美版：`data/maps/MauvilleCity/scripts.inc`

范围：JP+US

原因：日文是鼓励以后变强；英文反问有什么阻止变强。不是追问增强的动机。

修复方案/目标文字：

中段改为“今后继续努力，\n变得越来越强就好啦！”；其他叔叔对话不变。

### 21. MossdeepCity_GameCorner_1F_Text_TalkToOldManToPlay

实施状态：已修复并构建；待模拟器验收。

来源：v3:9

日版：`patch/batches/151_mossdeepcity_gamecorner_1f.json`

美版：`data/text/cable_club.inc`

范围：JP+US

原因：beside / おとなり 是旁边，不是后面。

修复方案/目标文字：

仅将“我后面的老人”改为“我旁边的老人”。

### 22. MossdeepCity_SpaceCenter_1F_Text_HaywireButRocketLaunchImminent

实施状态：已修复并构建；待模拟器验收。

来源：v3:11

日版：`patch/batches/157_mossdeepcity_spacecenter_1f.json`

美版：`data/maps/MossdeepCity_SpaceCenter_1F/scripts.inc`

范围：JP+US

原因：imminent / もうすぐ 是即将发射，不是不停止程序。

修复方案/目标文字：

火箭马上就要发射了！

### 23. Route116_Text_JoeyIntro

实施状态：已修复并构建；待模拟器验收。

来源：v3:13

日版：`patch/batches/028_route116.json`

美版：`data/text/trainers.inc`

范围：JP+US

原因：rule / つえー 是厉害，不是运用。

修复方案/目标文字：

我的宝可梦很厉害！\n你就好好瞧瞧吧！

### 24. Route123_Text_BraxtonPostBattle

实施状态：已修复并构建；待模拟器验收。

来源：v3:14

日版：`patch/batches/148_route123.json`

美版：`data/text/trainers.inc`

范围：JP+US

原因：战斗不辱徽章，而非在此次战斗中获得徽章。

修复方案/目标文字：

这场战斗真是\n无愧于你的道馆徽章！

### 25. SecretBase_Text_Trainer1PreChampion

实施状态：已修复并构建；待模拟器验收。

来源：v3:15

日版：`patch/batches/391_secret_base_trainers.json`

美版：`data/text/secret_base_trainers.inc`

范围：JP+US

原因：已经终于获得使用机会，不是仍等着开放。

修复方案/目标文字：

这个地方很受欢迎，\n总是有人占着。\p我等了很久，\n终于轮到我使用了！

### 26. BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteMMon1

实施状态：已修复并构建；待模拟器验收。

来源：v3:16

日版：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`

美版：`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`

范围：JP+US

原因：decent 是不错；日文说自己培育的。高贵/一对不合适。

修复方案/目标文字：

日版开头“我培育的宝可梦是……”；美版开头“我有两只不错的宝可梦。”；后半招式、物种变量不变。

### 27. BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteMMon2Ask

实施状态：已修复并构建；待模拟器验收。

来源：v3:17

日版：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`

美版：`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`

范围：JP+US

原因：neat 在此是组队不错，不是高雅。

修复方案/目标文字：

如果我们一起组队\n一定很不错，你觉得呢？；前半的招式、物种变量保留。

### 28. BattleFrontier_Lounge5_Text_LadyClaimsSheUnderstandsPokemon

实施状态：已修复并构建；待模拟器验收。

来源：v3:18

日版：`patch/batches/399_frontier_lounge5.json`

美版：`data/maps/BattleFrontier_Lounge5/scripts.inc`

范围：JP+US

原因：charming / シャレた 是有趣俏皮，不是魔法。

修复方案/目标文字：

真有意思！\n那位小女孩说她能\l懂得宝可梦的心情！

### 29. DewfordTown_Gym_Text_BrendenIntro

实施状态：已修复并构建；待模拟器验收。

来源：v3:20

日版：`patch/batches/023_dewford_gym.json`

美版：`data/maps/DewfordTown_Gym/scripts.inc`

范围：JP+US

原因：いじ / gumption 是骨气胆识，不是智慧。

修复方案/目标文字：

让你看看\n海之男儿的骨气！

### 30. FortreeCity_House1_Text_GoingToMakeVolbeatStrong

实施状态：已修复并构建；待模拟器验收。

来源：v3:22

日版：`patch/batches/107_fortreecity_house1.json`

美版：`data/maps/FortreeCity_House1/scripts.inc`

范围：JP+US

原因：要求同样把正电拍拍培养强大，不是泛泛善待。

修复方案/目标文字：

末句改为“你也要把正电拍拍\n培养得更强啊！”

### 31. LilycoveCity_PokemonTrainerFanClub_Text_YoureOneWeWantToWin

实施状态：已修复并构建；待模拟器验收。

来源：v3:31

日版：`patch/batches/139_lilycovecity_pokemontrainerfanclub.json`

美版：`data/maps/LilycoveCity_PokemonTrainerFanClub/scripts.inc`

范围：JP+US

原因：为玩家加油，不是想打败玩家，主客体反转。

修复方案/目标文字：

嗨，{PLAYER}！\n我们希望你能获胜！；日版仍用 FD_01。

### 32. GraniteCave_StevensRoom_Text_ImStevenLetterForMe

实施状态：已修复并构建；待模拟器验收。

来源：v3:32

日版：`patch/batches/027_stevens_room.json`

美版：`data/maps/GraniteCave_StevensRoom/scripts.inc`

范围：JP+US

原因：所有经常是笔误。

修复方案/目标文字：

“所有经常”改“所以经常”。

### 33. gTVPokemonNewsBattleFrontierText11

实施状态：已修复并构建；待模拟器验收。

来源：v3:36

日版：`patch/batches/386_tv_0.json`

美版：`data/text/tv.inc`

范围：JP+US

原因：两个“在”重复，当前仍存在。

修复方案/目标文字：

删除第二行开头多余的“在”，保留其余文字与变量。

### 34. gTVPokemonNewsBattleFrontierText12

实施状态：已修复并构建；待模拟器验收。

来源：v3:37

日版：`patch/batches/386_tv_0.json`

美版：`data/text/tv.inc`

范围：JP+US

原因：两个“在”重复，当前仍存在。

修复方案/目标文字：

删除第二行开头多余的“在”。

### 35. CableClub_Text_ExplainWirelessClub

实施状态：已修复并构建；待模拟器验收。

来源：v3:40

日版：`patch/batches/359_cable_club.json`

美版：`data/text/cable_club.inc`

范围：JP+US

原因：非首次说明的完整日英原文均有找不到朋友时靠近的提示，当前遗漏。

修复方案/目标文字：

在适配器未连接的说明之前补“如果在联盟交谊厅或直接连接室\n找不到朋友，\p请试着靠近朋友一些。”；不要顺手向首次说明复制此段。

### 36. LavaridgeTown_Gym_1F_Text_GeraldIntro

实施状态：已修复并构建；待模拟器验收。

来源：v3:42

日版：`patch/batches/079_lavaridgetown_gym_1f.json`

美版：`data/maps/LavaridgeTown_Gym_1F/scripts.inc`

范围：JP；US澄清单位

原因：日文200度与英文392度是摄氏/华氏区域换算，不是同一数字。“392度”没有单位会误导。

修复方案/目标文字：

日版200℃；美版392℉。不因现实岩浆温度去修改原作数字。

### 37. LavaridgeTown_Gym_1F_Text_GeraldPostBattle

实施状态：已修复并构建；待模拟器验收。

来源：v3:43

日版：`patch/batches/079_lavaridgetown_gym_1f.json`

美版：`data/maps/LavaridgeTown_Gym_1F/scripts.inc`

范围：JP；US澄清单位

原因：同上一条，原作设定数值是200℃ / 392℉。

修复方案/目标文字：

日版温度200℃，美版392℉；保留后续击败我所以能承受的夸张说法。

### 38. gText_BecameMoreConsciousOfOtherMons

实施状态：已修复并构建；待模拟器验收。

来源：v3:44

日版：`patch/batches/405_contest_strings.json`

美版：`data/text/contest_strings.inc`

范围：JP+US

原因：conscious / きになる 是更加在意，不是担心。

修复方案/目标文字：

“更加担心其他宝可梦”改为“更加在意其他宝可梦”，四个 PAUSE 15 不变。

### 39. sWaterfallDescription

实施状态：已修复并构建；待模拟器验收。

来源：v3:46

日版：`patch/move_descriptions.json`

美版：`src/data/text/move_descriptions.h`

范围：JP+US

原因：第三世代攀瀑是 EFFECT_HIT，secondaryEffectChance=0，没有招式自带畏缩效果。不能混入第四世代效果。

修复方案/目标文字：

以惊人的气势扑向对手。；删除畏缩句；字体和换行根据现有描述框重新排，不改招式参数。

### 40. BattleFrontier_Lounge2_Text_AmazingPowersOfObservation

实施状态：已修复并构建；待模拟器验收。

来源：v3:52

日版：`patch/batches/432_checklist_scripts.json`

美版：`data/maps/BattleFrontier_Lounge2/scripts.inc`

范围：JP+US

原因：かんさつりょく / powers of observation 是观察力。センパイ是前辈，不应机械修成老师。

修复方案/目标文字：

好厉害的观察力！\n前辈果然非同一般！

### 41. LilycoveCity_ContestHall_Text_SuchCharmingCuteAppeals

实施状态：已修复并构建；待模拟器验收。

来源：v3:54

日版：`patch/batches/125_lilycovecity_contesthall.json`

美版：`data/maps/LilycoveCity_ContestHall/scripts.inc`

范围：JP+US

原因：みずあそび / WATER SPORT 是招式玩水；“水之游”不是该招式名。

修复方案/目标文字：

仅将“水之游”改为“玩水”，其他评委感叹及表演措辞保留。

### 42. LilycoveCity_CoveLilyMotel_1F_Text_HeardAquaHideoutBusted

实施状态：已修复并构建；待模拟器验收。

来源：v3:55

日版：`patch/batches/127_lilycovecity_covelilymotel_1f.json`

美版：`data/maps/LilycoveCity_CoveLilyMotel_1F/scripts.inc`

范围：JP+US

原因：有人到捣毁了，混入多余“到”。

修复方案/目标文字：

“有人到捣毁了”改为“有人捣毁了”。

### 43. MossdeepCity_GameCorner_1F_Text_DescribeWhichGame

实施状态：已修复并构建；待模拟器验收。

来源：v3:57

日版：`patch/batches/151_mossdeepcity_gamecorner_1f.json`

美版：`data/text/cable_club.inc`

范围：JP+US

原因：游戏规则不是宝可梦对战规则。

修复方案/目标文字：

将“对战规则”改为“游戏规则”，按现有分页保留其他句子。

### 44. RustboroCity_DevonCorp_1F_Text_HowCouldWeGetRobbed

实施状态：已修复并构建；待模拟器验收。

来源：v3:59

日版：`patch/batches/031_rustborocity_devoncorp_1f.json`

美版：`data/maps/RustboroCity_DevonCorp_1F/scripts.inc`

范围：JP+US

原因：对已经被抢的事情自责，不能否认“谁会抢”。

修复方案/目标文字：

包裹居然被抢走了，\n我们也太不小心了……

### 45. RustboroCity_PokemonSchool_Text_ExplainPoison

实施状态：已修复并构建；待模拟器验收。

来源：v3:60

日版：`patch/batches/038_rustborocity_pokemonschool.json`

美版：`data/maps/RustboroCity_PokemonSchool/scripts.inc`

范围：JP+US

原因：体力P是残留字母，不成词；这里应表示HP。

修复方案/目标文字：

“体力P”改为“HP”，HP保持连续，不跨行拆开。

### 46. gTVBravoTrainerText00

实施状态：已修复并构建；待模拟器验收。

来源：v3:61

日版：`patch/batches/386_tv_0.json`

美版：`data/text/tv.inc`

范围：JP+US

原因：STR_VAR_1 是训练家，节目介绍的是其宝可梦；Rank 是比赛级别，非取得优胜。保留节目名原英文不必单独认定错误。

修复方案/目标文字：

“今天我们要介绍的，\n是{STR_VAR_1}的宝可梦！\p这只宝可梦在{STR_VAR_2}\n比赛中达到了{STR_VAR_3}级别。”；日版 FD_02/03/04 保留，控制符按本地模板。
