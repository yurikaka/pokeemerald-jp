# Batch 覆盖点类型审查

## 范围及通过条件

审查 `patch/batches/*.json` 的每一条 `reference_writes`，不是只抽查 batch，
也不是只检查原 ROM 的四字节是否等于 `original`。

逐项结果、原 ROM SHA-256、Wokann revision 和统计保存在 `references.json`。
尚未取得双重证据的条目全部列在 `review_queue.md`；不能把这些条目称为已通过。

本轮454份 batch、11770个覆盖点的结果：

| 类别 | 数量 | 含义 |
|---|---:|---|
| 双证据确认 | 10489 | 目标文本字节及引用位置均已确认，包括修复后的056、063及新增的界面引用 |
| 明确错误 | 0 | 本轮确认的056、063错误覆盖已修复 |
| 文本已确认，引用类型未确认 | 653 | 不能仅因目标是文本就认为覆盖位置安全 |
| 引用已定位，目标文本未确认 | 330 | 不能仅凭重定位就认为目标是文本 |
| 两侧证据均不足 | 298 | 必须进一步核对 raw 表、packed 字符串或使用者 |

因此目前不能宣称“全部覆盖点都是真文本”；剩余1281条仍需人工或更强的源级证据。

通过需要同时满足：

1. 原 ROM 四字节与声明的 `original` 一致。
2. 目标完整字节与 Wokann 明确的文本定义或该文本的编译结果一致。
3. 覆盖位置有编译重定位、文本表布局、明确文本符号引用或事件文本指令证据。
4. 不能是已确认的 AI 字节码、事件脚本入口或机器指令。

仅找到同名 C/ASM 标签不是证据。任意二进制中出现 `0xFF` 也不是证据。
仅有 `R_ARM_ABS32` 也不够，因为函数、图片和脚本同样有指针重定位。

`compact_tables` 中两份资源是新生成的表，不直接覆盖原 ROM 数据；其使用者的
ASM hook 不属于 batch `reference_writes` 清单，不能由本报告宣称已经全面审查。

## 确认错误一：batch 056

- 文件：`056_mauvillecity_pokemoncenter_1f.json`
- 错误覆盖位置：`0x0825642D`
- 声明目标：`0x08146E66`
- 中文资源：`Chs_MauvilleCity_PokemonCenter_1F_Text_HearMyStory`

这里不是文本指针。`0x0825642D` 的四字节原值为 `66 6E 14 08`，实际是
`waitmessage` 和 `yesnobox 20, 8` 的指令及参数，恰好可以当整数读成
`0x08146E66`。覆盖会直接破坏事件指令。

Wokann `data/scripts/mauville_man.inc` 中
`MauvilleCity_PokemonCenter_1F_EventScript_GiddyTellTale` 可确认这两个连续命令。
数值 `0x08146E66` 同时位于 `src/battle_transition.c` 的 `FramesCountdown`
函数内部，标签 `_08146E66` 后是 `movs r0, #0; pop {r1}; bx r1`，并不是故事文本。

真正的文本是 `MauvilleCity_PokemonCenter_1F_Text_HearMyStory`，地址
`0x08256362`。它在 `MauvilleCity_PokemonCenter_1F_EventScript_Giddy` 的
`msgbox ..., MSGBOX_YESNO` 中使用；正确指针位置为 `0x082563C8`。
原 ROM 序列为 `0F 00 62 63 25 08 09 05`。

修复方案：删除错误覆盖，改为 `0x082563C8 -> 0x08256362`，保留中文资源。
已按此方案修复，保留原中文资源；错误位置不再覆盖。

## 确认错误二：batch 063

- 文件：`063_route110_trickhousepuzzle1.json`
- 错误覆盖位置：`0x0823C85C`
- 声明目标：`0x0823C8D4`
- 中文资源：`Chs_Route110_TrickHousePuzzle1_Text_WroteSecretCodeLockOpened`

这是脚本调用目标，不是文本指针。Wokann
`data/maps/Route110_TrickHouseEntrance/scripts.inc` 的入口转换脚本使用
`call_if_eq ..., Route110_TrickHouseEntrance_EventScript_CheckReadyForNextPuzzle`。
该脚本入口就是 `0x0823C8D4`，其后执行 `setvar` 和多个 `call_if_eq`。
把该调用目标重定向到中文字符串会将文本当事件指令执行。

真正的文本定义在 `data/maps/Route110_TrickHousePuzzle1/scripts.inc`，地址
`0x0823DF53`。正确使用者是入口文件中的
`Route110_TrickHousePuzzle1_EventScript_Door`，指针位置为 `0x0823D067`。
Wokann 编译对象该位置的重定位直接引用正确文本符号；原 ROM 序列为
`0F 00 53 DF 23 08 09 04`。

修复方案：删除错误覆盖，改为 `0x0823D067 -> 0x0823DF53`，保留中文资源。
已按此方案修复，保留原中文资源；错误位置不再覆盖。

## 先前已修复：batch 071

之前的 `0x0828A74F -> 0x0828AAA5` 是 AI `EFFECT_SWAGGER` 的分支，不是对话。
当前工作区已改为唯一正确的寄养屋对话引用
`0x08257772 -> 0x08257BC6`。该处不再列为当前错误。
详见 `../batch071_swagger_ai_redirect.md`。

## 开始菜单 batch 170 的特别说明

不能仅因 Wokann 某个 raw resource 使用 reset-RTC 的历史标签，就认定这13条
必定不是文本。`src/data/start_menu.h` 将 `gUnknown_84E8C2C` 固定到
`sStartMenuItems`；`src/start_menu.c::PrintStartMenuActions` 按8字节记录读取
第一个字段，送入 `StringExpandPlaceholders` 和文本打印函数；第二个字段是回调。
原 ROM 的 `0x084E8B58` 等位置实际包含日文菜单字符串。

该项必须按实际字节和使用者证明，不能机械删除。自动双证据仍不足的条目保留
在未确认队列中，不因这段人工说明就批量改为自动通过。

## 其他边界

全部11770个指针覆盖位置互不重复，也没有四字节写入范围彼此重叠。
这只能排除 batch 间直接写冲突，不能排除类型错配或遗漏翻译。
本审查不替代模拟器运行测试，也不覆盖 batch 之外的 ASM hook、图片替换和表步长修改。
