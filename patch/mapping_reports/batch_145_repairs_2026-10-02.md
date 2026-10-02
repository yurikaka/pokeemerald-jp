# Batch 145 修复实施记录（2026-10-02）

全部145条已经复核：121条修复，24条保留。没有待处理项。

修复对象包括US源文本和JP批次；差异不是机械同步，保留JP语言、货币及UI布局。

## 地址与动态文本

- 停止进化：两个省略号覆盖移除，改为Wokann核实的0x0813ECD0 → 0x085ABB28。
- 动态参赛名单：保留名单生成；原JP名单尾は不再输出，换行/提示保留。引用0x081A3E58 → 0x085ABC72及0x081A3E68 → 0x085ABC75均经Wokann和baserom核对。
- 43为寄放提示；44为不参加，原方案中的能参加不适用于JP原文。
- 40战斗FD01不是PLAYER；56只为日版单位；57是姓名追加后缀。这三项为误报。
- 112、125缺少EOS已修复。
- 144原程序允许30级，不能按英文below排除30级。

## 验证

- 121条最终文本与JP编码逐条一致检查通过。
- 24条保留定义与HEAD一致检查通过。
- 所有新增/修改ROM指针均与baserom原值一致。
- US make和JP make chs通过；JP make compare通过。
- 日版旧gbagfx无法读取既有menu_info.png多调色板索引，构建使用US已生成的同一menu_info.png.4bpp；未修改原PNG或图块。
- 无可用模拟器，未宣称游戏内测试通过。
- 本次未commit或push。

## 逐条结果

### 1. Route103_Text_AndrewIntro

- 状态：已修复
- 批次：`patch/batches/012_route103.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
嘎！我的钓鱼线缠成一团，真让人心烦！\n可恶！来对战吧！
```

### 2. Route104_Text_RegisteredBrendan

- 状态：已修复
- 批次：`patch/batches/017_route104.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
{PLAYER}把小悠\n登记到宝可导航里了。
```

### 3. RustboroCity_Gym_Text_RoxannePreRematch

- 状态：已修复
- 批次：`patch/batches/036_rustborocity_gym.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
杜娟：真高兴又见到您。\n我是这里的道馆馆主杜娟。\p自上次见面后，我们都经历了\n许多场对战。\p我想看看彼此变强了多少……\p请与我对战吧！
```

### 4. RustboroCity_Gym_Text_RoxanneRematchNeedTwoMons

- 状态：已修复
- 批次：`patch/batches/036_rustborocity_gym.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
杜娟：真高兴又见到您。\n我是这里的道馆馆主杜娟。\p自上次见面后，我们都经历了\n许多场对战。\p我想看看彼此变强了多少……\p……啊？您只带了1只\n能战斗的宝可梦。\p请带至少2只宝可梦\n再来吧。
```

### 5. SlateportCity_OceanicMuseum_2F_Text_DeepSeawaterDisplay

- 状态：已修复
- 批次：`patch/batches/047_slateportcity_oceanicmuseum_2f.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
海水循环的演示。\p“在海底附近，海水由于\n温度和含盐量的不同，\l形成了环流。”
```

### 6. SlateportCity_OceanicMuseum_2F_Text_SubmersibleReplica

- 状态：已修复
- 批次：`patch/batches/047_slateportcity_oceanicmuseum_2f.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
“潜水舱”\p这是为在海底作业而设计的\n小型无人潜水舱模型！
```

### 7. SlateportCity_PokemonFanClub_Text_LikenMonToSomethingYouLike

- 状态：已修复
- 批次：`patch/batches/048_slateportcity_pokemonfanclub.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
你的{STR_VAR_1}\n被照顾得很好呢。\p如果要把它比作你喜欢的东西，\n会是什么呢？
```

### 8. Route110_Text_JaclynPostBattle

- 状态：已修复
- 批次：`patch/batches/057_route110.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
你会赢仅仅是因为\n那是一个奇迹！是的，一个奇迹！\l别以为你能一直赢！
```

### 9. Route110_Text_JasminePostBattle

- 状态：已修复
- 批次：`patch/batches/057_route110.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
哦，你有道馆徽章？\n难怪你这么强！
```

### 10. Route110_Text_TimmyIntro

- 状态：已修复
- 批次：`patch/batches/057_route110.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我在附近的草丛里发现了很帅的\n宝可梦！
```

### 11. Route110_TrickHouseEnd_Text_AllNightToMakeMechadolls

- 状态：已修复
- 批次：`patch/batches/060_route110_trickhouseend.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我用了一整夜制作机械娃娃，\n又用了一整夜想谜题……\p你几乎和我一样伟大，\n不过还差一、两个档次！
```

### 12. Route110_TrickHousePuzzle1_Text_EddiePostBattle

- 状态：已修复
- 批次：`patch/batches/063_route110_trickhousepuzzle1.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我迷路了，也输掉了对战，\n现在更迷路了……\l我出不去了……
```

### 13. Route110_TrickHousePuzzle5_Text_Mechadoll4Intro

- 状态：已修复
- 批次：`patch/batches/067_route110_trickhousepuzzle5.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
咔嗒、噼啪……\n机械娃娃 4 号就是我！\p我的问答关乎美丽！
```

### 14. Route110_TrickHousePuzzle7_Text_AlvaroPostBattle

- 状态：已修复
- 批次：`patch/batches/069_route110_trickhousepuzzle7.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
啊，不管怎样，\n我们在这种奇怪的地方相识了。\p同为怪人，\n我们都要努力啊！
```

### 15. Route110_TrickHousePuzzle7_Text_EverettIntro

- 状态：已修复
- 批次：`patch/batches/069_route110_trickhousepuzzle7.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
这里真是太挤了……
```

### 16. Route117_Text_AnnaDefeat

- 状态：已修复
- 批次：`patch/batches/071_route117.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
美穗：我和漂亮的学妹在一起！\n请让我赢吧！
```

### 17. LavaridgeTown_Gym_1F_Text_FlanneryRematchDefeat

- 状态：已修复
- 批次：`patch/batches/079_lavaridgetown_gym_1f.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
呼！\n快要爆发了！
```

### 18. Route111_Text_DustyPostBattle

- 状态：已修复
- 批次：`patch/batches/084_route111.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我已经找了 30 年的遗迹！\p等等，已经找了 40 年吗？\n到底是多少年呢？
```

### 19. Route111_Text_DustyPostRematch

- 状态：已修复
- 批次：`patch/batches/084_route111.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我已经找了 30 年的遗迹！\p等等，已经找了 40 年吗？\p嗯……我感觉也许已有 50 年了……\n我到底找了多久？
```

### 20. Route111_Text_MirageTowerHasntBeenSeenSince

- 状态：已修复
- 批次：`patch/batches/084_route111.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
自那以后，\n就再也没见过那座沙塔。\p它果然是幻影之塔吗……
```

### 21. Route111_OldLadysRestStop_Text_DontNeedToBeShy

- 状态：已修复
- 批次：`patch/batches/085_route111_oldladysreststop.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
这样啊……\n真的没问题吗？\l不用客气也没关系哦。
```

### 22. Route112_Text_CarolPostBattle

- 状态：已修复
- 批次：`patch/batches/087_route112.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
不管擅不擅长唱歌或\n宝可梦对战，都不重要。\p只要乐在其中就是胜利！
```

### 23. Route112_Text_LarryPostBattle

- 状态：已修复
- 批次：`patch/batches/087_route112.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我不是因为想妈妈才哭的！\n抽泣……
```

### 24. Route112_Text_MtChimneyCableCarSign

- 状态：已修复
- 批次：`patch/batches/087_route112.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
烟囱山缆车乘车处\n{UP_ARROW} 前方不远处！
```

### 25. Route112_Text_TrentPostBattle

- 状态：已修复
- 批次：`patch/batches/087_route112.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
试着背着几十公斤重的行李，\n一直走在山路上吧。\l那样身体会变得结实哦！
```

### 26. Route113_Text_TiaPostBattle

- 状态：已修复
- 批次：`patch/batches/098_route113.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
宁宁：我们已经攒了不少火山灰！\n肯定够做白色玻璃哨了！
```

### 27. Route113_GlassWorkshop_Text_FunToBlowGlassFlute

- 状态：已修复
- 批次：`patch/batches/099_route113_glassworkshop.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
在老板说话的时候\n吹玻璃哨真好玩，\p呼呼！呼呼！
```

### 28. Route120_Text_ColinPostBattle

- 状态：已修复
- 批次：`patch/batches/114_route120.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
飞翔这招真方便啊，\n你觉得呢？\p当宝可梦飞起来时，\n几乎没什么招式能打中它。
```

### 29. Route120_Text_StevenGiveDevonScope

- 状态：已修复
- 批次：`patch/batches/114_route120.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
大吾：原来如此……\n你的战斗方式很有趣呢。\p比起我们在武斗镇初见时，\n你的宝可梦成长了不少。\p这个得文侦测镜\n送给你。\p说不定还有其他隐藏了\n身形的宝可梦呢。
```

### 30. Route120_Text_StevenReadyForBattle

- 状态：已修复
- 批次：`patch/batches/114_route120.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
大吾：{PLAYER}{KUN}，\n你的宝可梦准备好战斗了吗？
```

### 31. LilycoveCity_Text_SawTallTowerOnRoute131

- 状态：已修复
- 批次：`patch/batches/124_lilycovecity.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我在 131 号水路的附近\n看到过一座高高的塔，\p那会不会是……？
```

### 32. LilycoveCity_Text_SixtyYearsAgoHusbandProposed

- 状态：已修复
- 批次：`patch/batches/124_lilycovecity.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
60 年前，老伴在这里向我\n求婚。\l这片大海至今仍然如此美丽。\p呼呵呵呵呵……
```

### 33. LilycoveCity_ContestHall_Text_CantWinOnBeautyAlone

- 状态：已修复
- 批次：`patch/batches/125_lilycovecity_contesthall.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
只有美丽不可能\n长久获胜下去。\p还得经常为宝可梦梳洗，\n让它像我的宝可梦一样光彩照人。
```

### 34. LilycoveCity_ContestHall_Text_MyAzurillWasDistracted

- 状态：已修复
- 批次：`patch/batches/125_lilycovecity_contesthall.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
哦，不……我的小露力丽\n被其他宝可梦分散注意力了！
```

### 35. LilycoveCity_ContestLobby_Text_MonInNoCondition2

- 状态：已修复
- 批次：`patch/batches/126_lilycovecity_contestlobby.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
您的宝可梦当前状态不佳，\n无法参加这个级别的华丽大赛……
```

### 36. LilycoveCity_PokemonTrainerFanClub_Text_OnlyIRecognizeYourTrueWorth

- 状态：已修复
- 批次：`patch/batches/139_lilycovecity_pokemontrainerfanclub.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
你的真正实力，\n只需我一人知道便好。\p其他人恐怕无法理解\n那隐藏的力量……
```

### 37. Route123_Text_AlbertoPostBattle

- 状态：已修复
- 批次：`patch/batches/148_route123.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我一直在收集鸟类宝可梦\n在战斗中散落的羽毛。\p我想用鸟类宝可梦\n的羽毛来做一顶帽子。
```

### 38. MossdeepCity_GameCorner_1F_Text_PokemonJumpInfo

- 状态：已修复
- 批次：`patch/batches/151_mossdeepcity_gamecorner_1f.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
“宝可梦跳绳”\p用 A 键让您的宝可梦\n跳过藤鞭。\p只有 70 厘米左右以下的小型\n宝可梦可以参加。\p而且，只会游泳、挖掘、飞行的\n宝可梦并不擅长跳跃，\p因此，这些宝可梦\n也无法参加。\p如果大家都及时跳起，\n会有好事情发生。
```

### 39. gText_BattleMenu

- 状态：已复核，保留
- 批次：`patch/batches/168_core_interfaces.json`
- 处理：保留日版80px菜单的CLEAR_TO 48；不是丢失字符。

最终中文：

```text
战斗{FC_CLEAR_TO_30}包包\n宝可梦{FC_CLEAR_TO_30}逃走
```

### 40. sText_AttackerUsedX

- 状态：已复核，保留
- 批次：`patch/batches/169_battle_messages.json`
- 处理：FD 01在战斗占位符表中是B_BUFF2，不是普通脚本PLAYER；现有日版句末叹号及+18招式名称hook保持不变。

最终中文：

```text
{FD_0F}使出了\n{PLAYER}！
```

### 41. gText_MenuRest

- 状态：已修复
- 批次：`patch/batches/170_start_menu.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
休息
```

### 42. gText_MoveToWhere

- 状态：已修复
- 批次：`patch/batches/172_party.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
要移动到哪里？
```

### 43. gText_ChoosePokemon2

- 状态：已修复
- 批次：`patch/batches/172_party.json`
- 处理：Wokann sActionStringTable指向0x085CA0F2，原文是寄放；US PARTY_MSG_CHOOSE_MON_2同样由培育屋调用。两版均改为寄放。

最终中文：

```text
请选择要寄放的宝可梦。
```

### 44. gText_Able

- 状态：已修复
- 批次：`patch/batches/172_party.json`
- 处理：Wokann sDescriptionStringTable第二项指向0x085CA1AB，原文さんかしない，因此JP改为不参加，而不是方案中的能参加。US ABLE改为可参加，保留版本语义差异。

最终中文：

```text
不参加
```

### 45. gText_PkmnNeedsToReplaceMove

- 状态：已修复
- 批次：`patch/batches/172_party.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
{STR_VAR_1}想学习\n{STR_VAR_2}……！\p但是{STR_VAR_1}已经学会了\n4个招式，无法再学更多！\p要忘记一个招式，\n学习{STR_VAR_2}吗？
```

### 46. gUnknown_85CA4A6

- 状态：已复核，保留
- 批次：`patch/batches/172_party.json`
- 处理：保留用户确认的训练家笔记布局、字体及换行；原方案中恢复旧换行的最终文本不执行。

最终中文：

```text
{DYNAMIC_0}{DYNAMIC_2}{DYNAMIC_1}{DYNAMIC_5}的性格，在{DYNAMIC_0}{DYNAMIC_4}{DYNAMIC_1}，\n遇见了当时{LV_2}{DYNAMIC_0}{DYNAMIC_3}{DYNAMIC_1}的它。
```

### 47. gUnknown_85CA4CC

- 状态：已复核，保留
- 批次：`patch/batches/172_party.json`
- 处理：保留用户确认的训练家笔记布局、字体及换行；原方案中恢复旧换行的最终文本不执行。

最终中文：

```text
{DYNAMIC_0}{DYNAMIC_2}{DYNAMIC_1}{DYNAMIC_5}的性格，在{DYNAMIC_0}{DYNAMIC_4}{DYNAMIC_1}孵化了。
```

### 48. gUnknown_85CA4F2

- 状态：已复核，保留
- 批次：`patch/batches/172_party.json`
- 处理：保留用户确认的训练家笔记布局、字体及换行；原方案中恢复旧换行的最终文本不执行。

最终中文：

```text
{DYNAMIC_0}{DYNAMIC_2}{DYNAMIC_1}{DYNAMIC_5}的性格，通过交换遇见了它。
```

### 49. gUnknown_85CA512

- 状态：已复核，保留
- 批次：`patch/batches/172_party.json`
- 处理：保留用户确认的训练家笔记布局、字体及换行；原方案中恢复旧换行的最终文本不执行。

最终中文：

```text
{DYNAMIC_0}{DYNAMIC_2}{DYNAMIC_1}{DYNAMIC_5}的性格，命中注定般地遇见了当时{LV_2}{DYNAMIC_0}{DYNAMIC_3}{DYNAMIC_1}的它。
```

### 50. gUnknown_85CA53B

- 状态：已复核，保留
- 批次：`patch/batches/172_party.json`
- 处理：保留用户确认的训练家笔记布局、字体及换行；原方案中恢复旧换行的最终文本不执行。

最终中文：

```text
{DYNAMIC_0}{DYNAMIC_2}{DYNAMIC_1}{DYNAMIC_5}的性格，好像在{DYNAMIC_0}{DYNAMIC_4}{DYNAMIC_1}，\n遇见了当时{LV_2}{DYNAMIC_0}{DYNAMIC_3}{DYNAMIC_1}的它。
```

### 51. gUnknown_85CA570

- 状态：已复核，保留
- 批次：`patch/batches/172_party.json`
- 处理：保留用户确认的训练家笔记布局、字体及换行；原方案中恢复旧换行的最终文本不执行。

最终中文：

```text
{DYNAMIC_0}{DYNAMIC_2}{DYNAMIC_1}{DYNAMIC_5}的性格，在某个地方，\n遇见了当时{LV_2}{DYNAMIC_0}{DYNAMIC_3}{DYNAMIC_1}的它。
```

### 52. gUnknown_85CA593

- 状态：已复核，保留
- 批次：`patch/batches/172_party.json`
- 处理：保留用户确认的训练家笔记布局、字体及换行；原方案中恢复旧换行的最终文本不执行。

最终中文：

```text
{DYNAMIC_0}{DYNAMIC_2}{DYNAMIC_1}{DYNAMIC_5}的性格，在某个地方孵化了。
```

### 53. gMenuText_Walk

- 状态：已修复
- 批次：`patch/batches/173_bag.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
步行
```

### 54. gUnknown_85C9A6C

- 状态：已复核，保留
- 批次：`patch/batches/173_bag.json`
- 处理：保留用户确认的日版金额后置円及已有菜单适配，不改为元或美元，不恢复US货币控制符。

最终中文：

```text
那么我用{STR_VAR_1}¥跟您收购吧。\n可以吗？
```

### 55. gUnknown_85C9A88

- 状态：已复核，保留
- 批次：`patch/batches/173_bag.json`
- 处理：保留用户确认的日版金额后置円及已有菜单适配，不改为元或美元，不恢复US货币控制符。

最终中文：

```text
给出{STR_VAR_2}，\n拿到了{STR_VAR_1}¥。
```

### 56. gText_TrainerCardPokedexSuffix

- 状态：已复核，保留
- 批次：`patch/batches/174_trainer_card.json`
- 处理：日版数字后原文ひき是只数单位；中文只正确，美版空串不是移除日版单位的依据。

最终中文：

```text
只
```

### 57. gText_Var1sTrainerCard

- 状态：已复核，保留
- 批次：`patch/batches/174_trainer_card.json`
- 处理：Wokann src/trainer_card.c先复制训练家名，再追加本后缀；补STR_VAR_1会重复姓名。保留的训练家卡。

最终中文：

```text
的训练家卡
```

### 58. gText_PokeblocksWithFriends

- 状态：已修复
- 批次：`patch/batches/174_trainer_card.json`
- 处理：改为与朋友制作宝可方块，保留原计数值和卡片渲染路径。

最终中文：

```text
与朋友制作宝可方块
```

### 59. gUnknown_85C9903

- 状态：已复核，保留
- 批次：`patch/batches/177_shop.json`
- 处理：日版购买询问模板和US占位符结构不同；现有单STR_VAR_1路径正确，不额外引入STR_VAR_2。

最终中文：

```text
您要买几个{STR_VAR_1}？
```

### 60. gUnknown_85C991F

- 状态：已复核，保留
- 批次：`patch/batches/177_shop.json`
- 处理：保留用户确认的日版金额后置円及已有菜单适配，不改为元或美元，不恢复US货币控制符。

最终中文：

```text
是{STR_VAR_1}啊。\n{STR_VAR_2}个一共是{STR_VAR_3}¥。
```

### 61. gUnknown_85C9936

- 状态：已复核，保留
- 批次：`patch/batches/177_shop.json`
- 处理：保留用户确认的日版金额后置円及已有菜单适配，不改为元或美元，不恢复US货币控制符。

最终中文：

```text
是{STR_VAR_1}啊。\n价格是{STR_VAR_2}¥。
```

### 62. gUnknown_85C994B

- 状态：已复核，保留
- 批次：`patch/batches/177_shop.json`
- 处理：保留用户确认的日版金额后置円及已有菜单适配，不改为元或美元，不恢复US货币控制符。

最终中文：

```text
是{STR_VAR_1}啊。\n价格是{STR_VAR_2}¥，可以吗？
```

### 63. gText_PkmnStoppedEvolving

- 状态：已修复
- 批次：`patch/batches/186_evolution_messages.json`
- 处理：删除0x0813ECA8和0x0813F7FC上的错误覆盖（两处均为gText_EllipsisQuestionMark）；实际停止进化文本在0x0813ECD0，原指针0x085ABB28。Wokann evolution_scene.c:1209及baserom均核对通过。

最终中文：

```text
什么……？{STR_VAR_1}\n停止进化了！\p
```

### 64. sText_ThrewPokeblockAtPkmn

- 状态：已修复
- 批次：`patch/batches/193_battle_safari_item_effects.json`
- 处理：US POKEBLOCK宏是55 56 57 58 59专用字形，JP不能直接当日文字符使用。JP改为宝可方块，保留FD23/FD06及既有japanese_placeholders；US宏不改。

最终中文：

```text
{B_PLAYER_NAME}朝{B_OPPONENT_MON1_NAME}\n投掷了宝可方块！
```

### 65. gText_PkmnTransferredLanettesPC

- 状态：已修复
- 批次：`patch/batches/194_battle_ability_link_facility.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
已将{STR_VAR_2}传送到\n真由美的电脑上。\p位于盒子\n“{STR_VAR_1}”里。
```

### 66. gText_PkmnTransferredLanettesPCBoxFull

- 状态：已修复
- 批次：`patch/batches/194_battle_ability_link_facility.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
真由美的电脑上的盒子\n“{STR_VAR_3}”已满，\p已将{STR_VAR_2}传送到\n盒子“{STR_VAR_1}”里。
```

### 67. BattleFrontier_BattleArenaLobby_Text_ExplainSkillRules

- 状态：已修复
- 批次：`patch/batches/199_battle_frontier_arena.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
第2个判定准则是“技”。\n这个因素评价宝可梦的\l招式命中。\p如果招式成功生效，\n技的评价就会上升。\p如果招式使用失败，\n技的评价则会下降。\p对于攻击招式，\n如果招式“效果绝佳”的话，\l技的评价就会上升。\l如果“效果不佳”的话，\l技的评价就会下降。\p对于像保护和看穿的招式，\n技的评价是不会上升的。\p如果对手使用了保护或看穿等招式，\n即使您的宝可梦没能成功命中，\l技的评价也不会下降。
```

### 68. BattleFrontier_BattleArenaLobby_Text_NotEnoughValidMonsLvOpen

- 状态：已修复
- 批次：`patch/batches/199_battle_frontier_arena.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
尊敬的挑战者！\p您能够参加对战的\n宝可梦不满3只。\p您需要准备3只\n不同种类的宝可梦，\p且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 69. BattleFrontier_BattleArenaLobby_Text_NotEnoughValidMonsLv50

- 状态：已修复
- 批次：`patch/batches/199_battle_frontier_arena.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
尊敬的挑战者！\p您能够参加对战的\n宝可梦不满3只。\p您需要准备3只等级50以内的\n不同种类的宝可梦，\p且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 70. BattleFrontier_BattleDomeLobby_Text_NotEnoughValidMonsLvOpen

- 状态：已修复
- 批次：`patch/batches/201_battle_frontier_battle_dome_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
很抱歉！\p您能够参加对战的\n宝可梦不满3只。\p您需要准备3只不同种类的\n宝可梦，\p且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 71. BattleFrontier_BattleDomeLobby_Text_NotEnoughValidMonsLv50

- 状态：已修复
- 批次：`patch/batches/201_battle_frontier_battle_dome_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
很抱歉！\p您能够参加对战的\n宝可梦不满3只。\p您需要准备3只等级50以内的\n不同种类的宝可梦，\p且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 72. BattleFrontier_BattlePalaceLobby_Text_NotEnoughValidMonsLv50

- 状态：已修复
- 批次：`patch/batches/208_battle_frontier_battle_palace_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
哎……\p您能够参加对战的\n宝可梦不满3只。\p您需要准备3只等级50以内的\n不同种类的宝可梦，\p并且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 73. BattleFrontier_BattlePalaceLobby_Text_NotEnoughValidMonsLvOpen

- 状态：已修复
- 批次：`patch/batches/208_battle_frontier_battle_palace_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
哎……\p您能够参加对战的\n宝可梦不满3只。\p您需要准备3只\n不同种类的宝可梦，\p并且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 74. BattleFrontier_BattlePikeLobby_Text_NotEnoughValidMonsLv50

- 状态：已修复
- 批次：`patch/batches/210_battle_frontier_battle_pike_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
冒昧打扰，但……\p您能够参加对战的\n宝可梦不满3只。\p您需要准备3只等级50以内的\n不同种类的宝可梦，\p并且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 75. BattleFrontier_BattlePikeLobby_Text_NotEnoughValidMonsLvOpen

- 状态：已修复
- 批次：`patch/batches/210_battle_frontier_battle_pike_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
冒昧打扰，但……\p您能够参加对战的\n宝可梦不满3只。\p您需要准备3只\n不同种类的宝可梦，\p并且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 76. BattleFrontier_BattlePyramidLobby_Text_BagCannotHoldPickItemsToKeep

- 状态：已修复
- 批次：`patch/batches/214_battle_frontier_battle_pyramid_lobby.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
很抱歉，战斗包包装不下\n所有的道具。\p请选择要保留在战斗包包中\n或让宝可梦携带的道具。
```

### 77. BattleFrontier_BattlePyramidLobby_Text_PickItemsToKeep

- 状态：已修复
- 批次：`patch/batches/214_battle_frontier_battle_pyramid_lobby.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
请选择要保留在战斗包包中\n或让宝可梦携带的道具。
```

### 78. BattleFrontier_BattlePyramidLobby_Text_NotEnoughValidMonsLvOpen

- 状态：已修复
- 批次：`patch/batches/214_battle_frontier_battle_pyramid_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
探险家啊，有点小问题！\p您能够参加对战的\n宝可梦不满3只。\p您需要准备3只\n不同种类的宝可梦，\p并且记得要取下它们携带的道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 79. BattleFrontier_BattlePyramidLobby_Text_NotEnoughValidMonsLv50

- 状态：已修复
- 批次：`patch/batches/214_battle_frontier_battle_pyramid_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
探险家啊，有点小问题！\p您能够参加对战的\n宝可梦不满3只。\p您需要准备3只等级50以内的\n不同种类的宝可梦，\p并且记得要取下它们携带的道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 80. BattleFrontier_BattleTowerLobby_Text_NotEnoughValidMonsLv50Singles

- 状态：已修复
- 批次：`patch/batches/217_battle_frontier_battle_tower_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
这位客人！\p您能够参加对战的\n宝可梦不满3只。\p您需要准备3只等级50以内的\n不同种类的宝可梦，\p且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 81. BattleFrontier_BattleTowerLobby_Text_NotEnoughValidMonsLvOpenSingles

- 状态：已修复
- 批次：`patch/batches/217_battle_frontier_battle_tower_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
这位客人！\p您能够参加对战的\n宝可梦不满3只。\p您需要准备3只\n不同种类的宝可梦，\p且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 82. BattleFrontier_BattleTowerLobby_Text_NotEnoughValidMonsLv50Doubles

- 状态：已修复
- 批次：`patch/batches/217_battle_frontier_battle_tower_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
这位客人！\p您能够参加对战的\n宝可梦不满4只。\p您需要准备4只等级50以内的\n不同种类的宝可梦，\p且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 83. BattleFrontier_BattleTowerLobby_Text_NotEnoughValidMonsLvOpenDoubles

- 状态：已修复
- 批次：`patch/batches/217_battle_frontier_battle_tower_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
这位客人！\p您能够参加对战的\n宝可梦不满4只。\p您需要准备4只\n不同种类的宝可梦，\p且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 84. BattleFrontier_BattleTowerLobby_Text_NotEnoughValidMonsLv50Multis

- 状态：已修复
- 批次：`patch/batches/217_battle_frontier_battle_tower_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
这位客人！\p您能够参加对战的\n宝可梦不满2只。\p您需要准备2只等级50以内的\n不同种类的宝可梦，\p且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 85. BattleFrontier_BattleTowerLobby_Text_NotEnoughValidMonsLvOpenMultis

- 状态：已修复
- 批次：`patch/batches/217_battle_frontier_battle_tower_lobby.json`
- 处理：补齐参赛限制和准备好后再来的结束句，保留STR_VAR_1动态禁用种族列表。US gText_Are/gText_Are2改为空列表后缀；JP原は+换行/提示分别在081A3E58、081A3E68重定向为仅换行/提示，名单仍动态生成。

最终中文：

```text
这位客人！\p您能够参加对战的\n宝可梦不满2只。\p您需要准备2只\n不同种类的宝可梦，\p且让它们分别携带不同道具\n才可参加对战。\p此外，下列宝可梦不能参加：\n蛋{STR_VAR_1}。\p准备好后，\n请再来吧。
```

### 86. BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice15Intro

- 状态：已修复
- 批次：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
你好！\n真让人紧张啊。\p我是{STR_VAR_3}，\n{STR_VAR_1}的第{STR_VAR_2}个徒弟。
```

### 87. BattleFrontier_ScottsHouse_Text_YouveCollectedAllSilverSymbols

- 状态：已修复
- 批次：`patch/batches/231_battle_frontier_scotts_house.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
亚希达：在对战开拓区\n玩得开心吗？\p……等等……\n啊！\p你的开拓通行证！\n你已经收集到了\l所有的银色象征！\p简直超乎想象！\n如我所料，你真的强大无比！\p虽说通常我不会这样，\n不过这次就让我破例一回！\p这个送给你。\n相信你一定\n能妥善使用。
```

### 88. EverGrandeCity_ChampionsRoom_Text_BrendanCongratulations

- 状态：已修复
- 批次：`patch/batches/235_ever_grande_city_champions_room.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
小悠：什么？！…… …… ……\n…… …… …… ……\p既然是规定，那也没办法。\p{PLAYER}，干得漂亮！\n恭喜你！
```

### 89. MossdeepCity_House1_Text_DoesntLikeOrDislikePokeblocks

- 状态：已修复
- 批次：`patch/batches/272_mossdeep_city_house1.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
它看来并没什么\n特别喜欢或不喜欢的宝可方块。
```

### 90. MossdeepCity_House1_Text_HusbandCanTellPokeblockMonLikes

- 状态：已修复
- 批次：`patch/batches/272_mossdeep_city_house1.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我的丈夫一眼就能看出\n宝可梦喜欢什么样的宝可方块。
```

### 91. MtPyre_2F_Text_LukeIntro

- 状态：已修复
- 批次：`patch/batches/275_mt_pyre_2_f.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
辉：我们来这儿试胆子。\p呵呵，如果她看到我有多棒，\n一定会迷恋上我的！\p没错！我要打败你，\n让她看看我有多厉害！
```

### 92. MtPyre_4F_Text_TashaPostBattle

- 状态：已修复
- 批次：`patch/batches/277_mt_pyre_5_f.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我想看看可怕的东西……\n我不能离开……\p留下来……\n你不愿意留下来陪我吗？
```

### 93. PacifidlogTown_Text_NeatHousesOnWater

- 状态：已修复
- 批次：`patch/batches/280_pacifidlog_town.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
看，很棒的镇子吧？\n房子都建在水上！\p我就是在这儿出生的！
```

### 94. SootopolisCity_Text_DoorIsClosed

- 状态：已修复
- 批次：`patch/batches/316_sootopolis_city.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
门关着。
```

### 95. SootopolisCity_Text_WeatherWentWild

- 状态：已修复
- 批次：`patch/batches/316_sootopolis_city.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
今天早上天空十分晴朗，\n但是……\p突然间，乌云群聚，\n暴雨倾盆而下，\l还伴着电闪雷鸣。\p天气一下子\n完全乱套了！\p这一切都是因为那两只\n宝可梦吗？
```

### 96. SootopolisCity_Gym_B1F_Text_TiffanyDefeat

- 状态：已修复
- 批次：`patch/batches/318_sootopolis_city_gym_b1_f.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
喂，搞什么？！
```

### 97. MoveTutor_MimicTeach

- 状态：已修复
- 批次：`patch/batches/340_move_tutors.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
啊，孩子！\p我也是个年轻人，\n不过我在模仿这个镇子里的\l老人们的言谈举止。\p怎么样，孩子？\n要我教你的宝可梦\l学习模仿这个招式吗？
```

### 98. MoveTutor_Text_DoubleEdgeTeach

- 状态：已修复
- 批次：`patch/batches/340_move_tutors.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
唉……\p琉璃市道馆馆主可真是\n太让人敬爱不已了。\p但这也意味着会有很多同样被\n他吸引的人做我的竞争对手。\p即使我像舍身冲撞般扑上去，\n也没能引起他的注意。\p那么，让我教你的宝可梦\n学习舍身冲撞！
```

### 99. Text_CantWaterfall

- 状态：已修复
- 批次：`patch/batches/342_field_move_scripts_scripts.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
伴随着巨大的轰响，\n大量的水从上方倾泻而下！
```

### 100. MatchCall_Text_Brendan11

- 状态：已修复
- 批次：`patch/batches/343_match_call.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
小悠：你好，{PLAYER}！\n不觉得这很棒吗？\p即使没有船，\n你也能利用宝可梦招式\l来渡过大海。\p有种宝可梦招式甚至还能\n让你潜入海底呢。\p宝可梦真是无所不能啊！
```

### 101. MatchCall_Text_Brendan13

- 状态：已修复
- 批次：`patch/batches/343_match_call.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
小悠：你好啊，{PLAYER}！\p最近怎么样？\n还在完成宝可梦图鉴吗？\p我听说有关于超古代\n宝可梦的传闻。\l而且不止1只——是3只！\p我好想捕获哪怕1只……
```

### 102. MatchCall_PersonalizedText25

- 状态：已修复
- 批次：`patch/batches/343_match_call.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
呜咽……我是……{STR_VAR_1}……\n……吸……\p今天在课上被杜娟训了。\p但是我并不讨厌她。\p杜娟直接指出了我的错误，\n这样我能吃一堑长一智。\p明天我绝对还要去\n训练师学校！\p回头见！
```

### 103. MatchCall_BattleFrontierRecordStreakText5

- 状态：已修复
- 批次：`patch/batches/343_match_call.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
喂，{PLAYER}{KUN}！\n我是{STR_VAR_1}。\p你在{STR_VAR_2}\n取得{STR_VAR_3}连胜？\l真厉害啊！\p我嘛，还算过得去吧。\n回见！
```

### 104. MatchCall_BattleFrontierRecordStreakText6

- 状态：已修复
- 批次：`patch/batches/343_match_call.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
喂，{PLAYER}{KUN}。\n是我{STR_VAR_1}。你好吗？\p对了，我听说你在{STR_VAR_2}\n完成了{STR_VAR_3}场连胜的壮举。\p我自己也得更加努力了！\n回见！
```

### 105. MatchCall_BattleFrontierRecordStreakText8

- 状态：已修复
- 批次：`patch/batches/343_match_call.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
喂，{PLAYER}{KUN}，你好吗？\n我是{STR_VAR_1}。\l希望你一切顺利。\p不过你好像的确很顺利。\n我听说你在{STR_VAR_2}\l取得了{STR_VAR_3}连胜。\p真是让人震惊！\n我也得努力培养宝可梦了！
```

### 106. MatchCall_BattleDomeText3

- 状态：已修复
- 批次：`patch/batches/343_match_call.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
嘿，你好，{PLAYER}！\n是我啊，{STR_VAR_1}。\l最近怎么样？\p我听说你在{STR_VAR_2}\n取得了{STR_VAR_3}连冠！\p再接再厉啊！\n回头见！
```

### 107. MatchCall_BattleDomeText5

- 状态：已修复
- 批次：`patch/batches/343_match_call.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
喂，{PLAYER}{KUN}！\n我是{STR_VAR_1}。\p我听说你在{STR_VAR_2}\n取得了{STR_VAR_3}连冠！\p我也要加油啊！\n再见啦！
```

### 108. MatchCall_BattleDomeText6

- 状态：已修复
- 批次：`patch/batches/343_match_call.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
嘿，{PLAYER}{KUN}？\n我是{STR_VAR_1}。你还好吗？\p对了，听说你在{STR_VAR_2}\n获得了{STR_VAR_3}连冠。\p我得赶紧训练我的宝可梦，\n不然你要甩开我啦。
```

### 109. MatchCall_BattleDomeText13

- 状态：已修复
- 批次：`patch/batches/343_match_call.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
喂，你好，{PLAYER}{KUN}！\n我是{STR_VAR_1}！\l希望你一切都好。\p据说你在{STR_VAR_2}\n取得了{STR_VAR_3}连冠？\p真佩服你的干劲！\n再见！
```

### 110. Route104_PrettyPetalFlowerShop_Text_ImGrowingFlowers

- 状态：已修复
- 批次：`patch/batches/357_berries.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我正努力向姐姐们学习，\n也在努力种花！\p给！\n这个送给你！
```

### 111. SootopolisCity_Text_LikeSeasonBornIn

- 状态：已修复
- 批次：`patch/batches/357_berries.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
春，夏，秋，冬……\p春天出生的人喜欢春天\n夏天出生的人喜欢夏天吗？
```

### 112. BerryBlender_Text_WhoaAwesome

- 状态：已修复
- 批次：`patch/batches/358_blend_master.json`
- 处理：US原字符串缺少EOS，会串入下一条文本；补$并将JP定义截到太厉害了！。

最终中文：

```text
哇！\n太厉害了！
```

### 113. MossdeepCity_GameCorner_1F_Text_ShortJumpingPokemonAllowed

- 状态：已修复
- 批次：`patch/batches/359_cable_club.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
参加“宝可梦跳绳”的宝可梦\n必须在70厘米以下，\p此外，不会跳跃的\n宝可梦也无法参加，\p比如说，只会游泳、挖掘、\n飞行的宝可梦。\p知道这些就够了。
```

### 114. Route133_Text_MollieDefeat

- 状态：已修复
- 批次：`patch/batches/382_trainer_quotes_11.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我大概已经输了几千次了，\n但输了还是很不甘心。
```

### 115. gText_ApprenticePleaseTeach11

- 状态：已修复
- 批次：`patch/batches/383_apprentice_0.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
A——H——O——Y！\n拼出来就是“Ahoy”，意思是“嗨”！\p我是{STR_VAR_1}，说唱水手！\n现在轮到你了，\l说说你自己吧，试试看！\p嗯哼，嗯哼！\n你叫{PLAYER}{KUN}，\l宝可梦是你的拿手好戏！\p而且你正处在一个微妙的年纪，\n整个世界都是你的舞台！\p总之，我只想说，\n你是我今天交谈过的\l第10位训练家。\p让我们庆祝一下！\p为了纪念，成为我的导师吧！
```

### 116. gText_ApprenticeMoveThanks13

- 状态：已修复
- 批次：`patch/batches/383_apprentice_0.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
嗯，{STR_VAR_1}，好吧。咳咳！\n等我好一点就去教它。\p希望以后还能这样\n继续请你帮忙。
```

### 117. gText_ApprenticeMoveThanks14

- 状态：已修复
- 批次：`patch/batches/383_apprentice_0.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
哦……好的！\n我会试试{STR_VAR_1}。\p希望我能教会它这个招式……\n真让人紧张啊……\p谢谢你，{PLAYER}{KUN}。\n如果再见面，还请你\l像这样帮助我。
```

### 118. gText_ApprenticeMoveThanks15

- 状态：已修复
- 批次：`patch/batches/383_apprentice_0.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
{STR_VAR_1}？\n真的没有问题吗？\p明白了。如果是这样就好。\n感谢你抽空帮忙。\p真希望我的宝可梦\n也能学会这个招式。\p下次再见吧！
```

### 119. gTV3CheersForPokeblocksText05

- 状态：已复核，保留
- 批次：`patch/batches/386_tv_0.json`
- 处理：POKEBLOCK是固定名词的专用图形宏，不是动态占位符；日版当前宝可方块正确，无需回退。

最终中文：

```text
下次节目再见！我们的口号是\n “为宝可方块喝彩！”
```

### 120. BravoTrainerBattleTower_Text_Lost

- 状态：已修复
- 批次：`patch/batches/386_tv_0.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
这对组合最终在第{STR_VAR_2}场\n败给了{STR_VAR_1}。\l虽败犹荣，训练家！\p不过，在挑战赛中这么早\n就遇上{STR_VAR_1}还真是运气不太好。\p我们采访了训练家\n和{STR_VAR_1}之间的比赛的感受。
```

### 121. gTV3CheersForPokeblocksText00

- 状态：已复核，保留
- 批次：`patch/batches/386_tv_0.json`
- 处理：POKEBLOCK是固定名词的专用图形宏，不是动态占位符；日版当前宝可方块正确，无需回退。

最终中文：

```text
主持人：希望大家干劲满满，\n《为宝可方块喝彩》现在开始！\p今天我们要评测的是{STR_VAR_1}\n等人制作的宝可方块。\p事不宜迟，现在就喂给我的\n美食家宝可梦——溶食兽吧。\p…… …… ……\n…… …… ……
```

### 122. gTV3CheersForPokeblocksText02

- 状态：已复核，保留
- 批次：`patch/batches/386_tv_0.json`
- 处理：POKEBLOCK是固定名词的专用图形宏，不是动态占位符；日版当前宝可方块正确，无需回退。

最终中文：

```text
{STR_VAR_1}的混合水平\n仍然有提升的空间。\p如果这位训练家能更熟练些，\n宝可方块的味道会更好。
```

### 123. gTVSafariFanClubText02

- 状态：已复核，保留
- 批次：`patch/batches/386_tv_0.json`
- 处理：POKEBLOCK是固定名词的专用图形宏，不是动态占位符；日版当前宝可方块正确，无需回退。

最终中文：

```text
这位训练家很擅长用宝可方块。\n那次用了{STR_VAR_2}个呢。
```

### 124. gTVSafariFanClubText07

- 状态：已复核，保留
- 批次：`patch/batches/386_tv_0.json`
- 处理：POKEBLOCK是固定名词的专用图形宏，不是动态占位符；日版当前宝可方块正确，无需回退。

最终中文：

```text
这位训练家的确用了宝可方块。\n那次用了{STR_VAR_2}个。\p不过真希望这位训练家\n做得更好一些啊。
```

### 125. TVSecretBaseSecrets_Text_UsedGlassOrnament

- 状态：已修复
- 批次：`patch/batches/388_tv_2.json`
- 处理：US玻璃工艺品文本缺少EOS，导致串入下一段；将末尾分页改为$，JP同样停止在指纹句末。

最终中文：

```text
访客正在观察\n一个玻璃工艺品！\p哦，不！\p访客在摸它！\p上面都是指纹了……
```

### 126. gTVSafariFanClubText08

- 状态：已复核，保留
- 批次：`patch/batches/389_tv_3.json`
- 处理：POKEBLOCK是固定名词的专用图形宏，不是动态占位符；日版当前宝可方块正确，无需回退。

最终中文：

```text
我觉得这位训练家要是用些宝可方块\n会更好，但那次一个都没用呢。
```

### 127. SecretBase_Text_Trainer3PostBattle

- 状态：已修复
- 批次：`patch/batches/391_secret_base_trainers.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
你的秘密基地在哪儿？\n我也会去拜访你的。
```

### 128. MauvilleCity_PokemonCenter_1F_Text_RestedAtHomeTitle

- 状态：已修复
- 批次：`patch/batches/392_mauville_man_0.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
恋家的训练家
```

### 129. MauvilleCity_PokemonCenter_1F_Text_MadePokeblocksAction

- 状态：已复核，保留
- 批次：`patch/batches/392_mauville_man_0.json`
- 处理：POKEBLOCK是固定名词的专用图形宏，不是动态占位符；日版当前宝可方块正确，无需回退。

最终中文：

```text
做宝可方块
```

### 130. MauvilleCity_PokemonCenter_1F_Text_UsedStruggleStory

- 状态：已修复
- 批次：`patch/batches/392_mauville_man_0.json`
- 处理：保留当前招式表名绝境反击；修复把使用次数说成获胜次数。

最终中文：

```text
关于{STR_VAR_3}是这样流传\n的。\p这位训练家被迫使用了\n{STR_VAR_1}次绝境反击！\p{STR_VAR_3}是不向逆境低头的\n顽强训练家！
```

### 131. MauvilleCity_PokemonCenter_1F_Text_CheckedClockAction

- 状态：已修复
- 批次：`patch/batches/393_mauville_man_1.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
看了看时间
```

### 132. BattleFrontier_Lounge5_Text_NatureGirlNoneShown

- 状态：已修复
- 批次：`patch/batches/399_frontier_lounge5.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
嘘！\n真小气！
```

### 133. BattleFrontier_ExchangeServiceCorner_Text_WhiteHerbDesc

- 状态：已修复
- 批次：`patch/batches/400_frontier_exchange.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
携带后能恢复\n下降的能力的道具。
```

### 134. BattleFrontier_ExchangeServiceCorner_Text_KingsRockDesc

- 状态：已修复
- 批次：`patch/batches/400_frontier_exchange.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
携带后攻击命中时，\n有时能使对手畏缩的道具。
```

### 135. Roulette_Text_PlayMinimumWagerIsX

- 状态：已修复
- 批次：`patch/batches/401_roulette.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
这个轮盘台的最低下注额为\n{STR_VAR_1}。要玩吗？
```

### 136. gText_StoodOutAsMuchAsMon

- 状态：已修复
- 批次：`patch/batches/405_contest_strings.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
它和{STR_VAR_1}一样\n引人注目。
```

### 137. gText_AndFillOutTheQuestionnaire

- 状态：已修复
- 批次：`patch/batches/411_strings_c_direct.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
并填写问卷。
```

### 138. gText_Ferry

- 状态：已修复
- 批次：`patch/batches/411_strings_c_direct.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
渡轮
```

### 139. gText_TeachWhichMoveToPkmn

- 状态：已修复
- 批次：`patch/batches/411_strings_c_direct.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
要让{STR_VAR_1}学习\n哪个招式？
```

### 140. gGiftRibbonDescriptionPart1_2004GlobalCup

- 状态：已修复
- 批次：`patch/batches/413_gift_ribbon_descriptions.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
2004年世界杯
```

### 141. gText_MatchCallSisAndBro_LilaAndRoy_Intro1

- 状态：已修复
- 批次：`patch/batches/415_match_call_0.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我们一起享受宝可梦
```

### 142. gText_MatchCallBeauty_Jessica_Intro2

- 状态：已修复
- 批次：`patch/batches/415_match_call_0.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
我好像总会去那里。
```

### 143. gText_MatchCallGentleman_Walter_Intro2

- 状态：已修复
- 批次：`patch/batches/416_match_call_1.json`
- 处理：前一片段已经是我们每天都享用茶水，；本片段只改为这是进口的。，避免重复每天。

最终中文：

```text
这是进口的。
```

### 144. sText_NeedTwoMonsOfLevel30OrLower2

- 状态：已修复
- 批次：`patch/batches/419_union_room_0.json`
- 处理：US union_room.c HasAtLeastTwoMonsOfLevel30OrLower实际比较<=30；保留等级30以内并补齐两只，不采用英文below造成的排除30级错误。

最终中文：

```text
要对战的话，需要两只\n等级30以内的宝可梦。\p
```

### 145. sText_ChatDeclinedFemale

- 状态：已修复
- 批次：`patch/batches/419_union_room_0.json`
- 处理：按该条日英原文和实际调用语境修正；保留既有占位符、模式标志及文本指针。

最终中文：

```text
哦，对不起。\n我现在有太多事情要做。\l下次再聊天吧。\p
```

