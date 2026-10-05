# v2 独有修复实施记录（2026-10-04）

## 完成范围

- 本轮日版修复11个资源、美版同步修复8个资源；另3个为日版区域适配，美版原文及已修复文本不动。
- 与前轮v3合计：日版46个去重资源全部已修并构建；美版42个资源同步修复。必修清单剩余0项。
- 修复代码/文本仍在工作区，未commit/push。原始独立review保留为审查快照，合并修复计划更新为实施状态。
- 未进行模拟器交互及画面验收，不将编码/构建成功当作全部场景实测通过。

## 构建与回归检查

- `jp_make_chs`：PASS
- `jp_make_compare`：PASS: original JP SHA1 unchanged
- `us_make`：PASS: pokeemerald.gba
- `all46_jp_and42_us_resources_in_rom`：PASS: definitions and linked batch/fixed/pointer-table payloads checked
- `previous_v3_fixes_preserved`：PASS
- `no_address_reference_or_data_logic_changes`：PASS
- `native_japanese_gift_password`：PASS: exact original bytes, FC15/FC16 brackets; longest instruction line156px <=168px
- `trade_message_colors`：PASS: original JP FC0102 FC0201 FC0303 restored
- `git_diff_check`：PASS in both repositories
- `emulator`：NOT RUN; interactive/visual verification pending

## 神秘礼物密码与数据边界

- 原日文提示地址 `0x085FCDBC`，口令保留“すごい トレーナー / くれ くれ”，不复制美版“GIVE ME / AWESOME TRAINER”。
- Wokann `src/easy_chat.c:1700` 从 GetQuestionnaireWordsPtr 取得存档词条编号缓冲区；`src/easy_chat.c:4818` 以ldrh取词条编号逐项比较；`src/mystery_gift.c:406` 对 questionnaireWords 数值逐项比较。不是拿显示文本做strcmp。
- 词条编号：Much/すごい = `0x1421`，Trainer/トレーナー = `0x020B`，Gimme/くれ = `0x1007`（两次）。编号根据 `EC_MASK_BITS=9` 和本地词条常量核对，只记录不修改。
- 只修改这一个说明资源，围绕密码显式进入JPN、结束后恢复ENG；密码本体与原日文ROM字节一致。
- 使用现有text字段编码路径，避免US编码转换把日文假名字节当成中文双字节。未改公共编码器或ASM。
- 说明按原日版恢复Joy Spot服务名；美版对应说明已修语法，仍保留美版密码与服务名。

## 标点与控制符

- 道具描述：日版继续无结尾句号；美版保留既有句号，不新增或全局删除标点。10PP连续，文柚果明确30HP。
- 交换提示恢复原日版三段颜色控制 FC0102 / FC0201 / FC0303；不调整交换判断或队伍数据。
- 全败提示只移动第一句叹号到换页符前；玩家名字FD01及其现有语言包装不变。

## ROM

- `pokeemerald_jp_chs.gba`：SHA-1 `e5b359af6ec53d9588b6eb092770dde0ce3d267c`。
- `../pokeemerald_us_chs/pokeemerald.gba`：SHA-1 `99d17de8d6b09c519baeb3ea5d03619b512f5f99`。

## 逐条完成记录

### 4397. MossdeepCity_Gym_Text_CliffordPostBattle

状态：已修复、已构建；待模拟器验收。

日版文件：`patch/batches/152_mossdeepcity_gym.json`。

原日版中文：

看来我无法胜过\n你的活力。

最终日版中文：

这里的道馆馆主也一样！\n年轻又充满活力！

原日文（Wokann `data/maps/MossdeepCity_Gym/scripts.inc`）：

この　ジムの　リーダーも　そりゃもう！\nわかくて　げんき　はつらつ　ですぞ$

原日文（ROM `0x0820BD63`）：

この　ジムの　リ-ダ-も　そりゃもう!\nわかくて　げんき　はつらつ　ですぞ

原英文（`data/maps/MossdeepCity_Gym/scripts.inc`，`fe570a7e5^`）：

It seems that I could not overcome\nyour youthful energy.$

美版：保留与英文区域版本相符的现有文本；本轮不改。

### 4798. gText_DexSortAtoZDescription

状态：已修复、已构建；待模拟器验收。

日版文件：`patch/batches/171_pokedex.json`。

原日版中文：

按字母的顺序来排列已发现\n和已获得的宝可梦。

最终日版中文：

按名称顺序排列\n已发现的宝可梦。

原日文（Wokann `src/data/text/region_texts76.h`）：

みつけたポケモンの　なまえを\nごじゅうおんじゅんで　ひょうじ　します

原日文（ROM `0x085C91E2`）：

みつけたポケモンの　なまえを\nごじゅうおんじゅんで　ひょうじ　します

原英文（`src/strings.c`，`fe570a7e5^`）：

Spotted and owned POKéMON are listed\nalphabetically.

美版：保留与英文区域版本相符的现有文本；本轮不改。

### 7183. RustboroCity_House3_Text_NamingPikachuPekachu

状态：已修复、已构建；待模拟器验收。

日版文件：`patch/batches/299_rustboro_city_house3.json`。

原日版中文：

但叫皮卡丘为\n猫卡球？这没什么意义。\p我想最好起个容易\n让人理解的名字，但是……

最终日版中文：

但给皮卡丘起名叫\n“佩卡丘”，几乎没什么\l区别吧……\p我想最好起个容易\n让人理解的名字，但是……

原日文（Wokann `data/maps/RustboroCity_House3/scripts.inc`）：

だからって　ピカチュウに\n‘ペカチュウ’って　つけても\lほとんど　かわって　ないでしょうに⋯⋯\pまあ　わかりやすいのも\nニックネームには　だいじ　ですけどねぇ$

原日文（ROM `0x0820416F`）：

だからって　ピカチュウに\n‘ペカチュウ’って　つけても\lほとんど　かわって　ないでしょうに……\pまあ　わかりやすいのも\nニックネ-ムには　だいじ　ですけどねぇ

原英文（`data/maps/RustboroCity_House3/scripts.inc`，`fe570a7e5^`）：

But giving the name PEKACHU to\na PIKACHU? It seems pointless.\pI suppose it is good to use a name\nthat's easy to understand, but…$

美版文件：`data/maps/RustboroCity_House3/scripts.inc`。

原美版中文：

但叫皮卡丘为\n猫卡球？这没什么意义。\p我想最好起个容易\n让人理解的名字，但是……$

最终美版中文：

但给皮卡丘起名叫\n“佩卡丘”？这没什么意义。\p我想最好起个容易\n让人理解的名字，但是……$

### 7184. RustboroCity_House3_Text_Pekachu

状态：已修复、已构建；待模拟器验收。

日版文件：`patch/batches/299_rustboro_city_house3.json`。

原日版中文：

猫卡球：猫球！

最终日版中文：

佩卡丘：佩卡！

原日文（Wokann `data/maps/RustboroCity_House3/scripts.inc`）：

ペカチュウ“ぺかー！$

原日文（ROM `0x082041BF`）：

ペカチュウ“ぺか-!

原英文（`data/maps/RustboroCity_House3/scripts.inc`，`fe570a7e5^`）：

PEKACHU: Peka!$

美版文件：`data/maps/RustboroCity_House3/scripts.inc`。

原美版中文：

猫卡球：猫球！$

最终美版中文：

佩卡丘：佩卡！$

### 9110. MauvilleCity_PokemonCenter_1F_Text_LedgesJumpedStory

状态：已修复、已构建；待模拟器验收。

日版文件：`patch/batches/392_mauville_man_0.json`。

原日版中文：

关于{FD_04}是这样流传\n的。\p他已经跳下\n{FD_02}次岩礁了！\p如果有适合跳跃的岩礁，\n{FD_04}一定会去跳的！

最终日版中文：

关于{FD_04}是这样流传\n的。\p他已经跳下\n{FD_02}次台阶了！\p如果有适合跳跃的台阶，\n{FD_04}一定会去跳的！

原日文（Wokann `data/scripts/mauville_man.inc`）：

{STR_VAR_3}という\nトレーナーの　はなし　だが⋯⋯\pなんと　{STR_VAR_1}かいも\nだんさを　とびおりた　らしい！\p{STR_VAR_3}は　だんさを　みると\nとびおりずに　おれない　トレーナーだな！$

原日文（ROM `0x08255F9B`）：

{PLACEHOLDER_04}という\nトレ-ナ-の　はなし　だが……\pなんと　{PLACEHOLDER_02}かいも\nだんさを　とびおりた　らしい!\p{PLACEHOLDER_04}は　だんさを　みると\nとびおりずに　おれない　トレ-ナ-だな!

原英文（`data/scripts/mauville_man.inc`，`fe570a7e5^`）：

This is a tale of a TRAINER\nnamed {STR_VAR_3}.\pThis TRAINER jumped down ledges\n{STR_VAR_1} times!\pIf there's a ledge to be jumped,\n{STR_VAR_3} can't ignore it!$

美版文件：`data/scripts/mauville_man.inc`。

原美版中文：

关于{STR_VAR_3}是这样流传\n的。\p他已经跳下\n{STR_VAR_1}次岩礁了！\p如果有适合跳跃的岩礁，\n{STR_VAR_3}一定会去跳的！$

最终美版中文：

关于{STR_VAR_3}是这样流传\n的。\p他已经跳下\n{STR_VAR_1}次台阶了！\p如果有适合跳跃的台阶，\n{STR_VAR_3}一定会去跳的！$

### 10293. sElixirDesc

状态：已修复、已构建；待模拟器验收。

日版文件：`patch/item_descriptions.json`。

原日版中文：

能让宝可梦学会的\n4个招式各回复1\n0PP

最终日版中文：

能让宝可梦学会的\n4个招式各回复\n10PP

原日文（Wokann `src/data/text/item_descriptions.h`）：

すべての　わざの\nわざポイントを\n10　かいふくする

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

Restores the PP\nof all moves by 10.

美版文件：`src/data/text/item_descriptions.h`。

原美版中文：

能让宝可梦学会的\n4个招式各回复1\n0PP。

最终美版中文：

能让宝可梦学会的\n4个招式各回复\n10PP。

### 10399. sSitrusBerryDesc

状态：已修复、已构建；待模拟器验收。

日版文件：`patch/item_descriptions.json`。

原日版中文：

携带后，可以回复\n少量HP

最终日版中文：

携带后，可以回复\n30HP

原日文（Wokann `src/data/text/item_descriptions.h`）：

もたせると　じぶんで\nたいりょくを\n30　かいふくする

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

A hold item that\nrestores 30 HP in\nbattle.

美版文件：`src/data/text/item_descriptions.h`。

原美版中文：

携带后，可以回复\n少量HP。

最终美版中文：

携带后，可以回复\n30HP。

### 12203. sText_MysteryGiftVisitingTrainerInstructions

状态：已修复、已构建；待模拟器验收。

日版文件：`patch/batches/471_checklist_mystery_gift_script_texts.json`。

原日版中文：

感谢使用\n神秘礼物系统。\p由于拥有神秘卡片\n您可以进行调查\l友好商店。\p通过调查您可以邀请\n训练家去琉璃市。\p……让我给您一个\n调查的密码吧：\p“GIVE ME\nAWESOME TRAINER”\p把这个写在调查上并发送到\n无线连接系统。

最终日版中文：

感谢使用\n神秘礼物系统。\p拥有这张神秘卡片后，\n您可以在友好商店参与调查。\p通过调查，您可以邀请\n各种训练家来到琉璃市。\p……让我悄悄告诉您\n一个调查用的密码吧：\p“{JPN}すごい　トレーナー\n　くれ　くれ{ENG}”\p请把这个密码填在调查中，\n再与Joy Spot进行通信。

原日文（ROM `0x85fcdbc`）：

ふしぎなおくりもの　を　ごりよう\nいただき　ありがとう　ございます\pこの　ふしぎなカ-ドを　もっていると\nフレンドリ-ショップの　アンケ-トで\pいろいろな　トレ-ナ-を　ルネシティに\nよぶことが　できますよ!\p……ないしょで　ひとつ　アンケ-トの\nあいことばを　おしえて　あげましょう\p‘すごい　トレ-ナ-\n　くれ　くれ’\pこのことばを　アンケ-トに　かいて\nぜひ　ジョイスポットと\lつうしんして　みてください!

原英文（`data/scripts/gift_trainer.inc`，`fe570a7e5^`）：

Thank you for using the MYSTERY\nGIFT System.\pBy holding this WONDER CARD, you\nmay take part in a survey at a\lPOKéMON MART.\pUse these surveys to invite\nTRAINERS to SOOTOPOLIS CITY.\p…Let me give you a secret\npassword for a survey:\p“GIVE ME\nAWESOME TRAINER”\pWrite that in on a survey and send\nit to the WIRELESS\lCOMMUNICATION SYSTEM.$

美版：保留与英文区域版本相符的现有文本；本轮不改。

### 13248. sText_OnlyPkmnForBattle

状态：已修复、已构建；待模拟器验收。

日版文件：`patch/batches/438_checklist_controls_and_gambler.json`。

原日版中文：

最后1只同行的宝可梦\n不能用来交换。

最终日版中文：

{COLOR 2}{HIGHLIGHT 1}{SHADOW 3}交换这只宝可梦后，\n就没有能战斗的宝可梦了。

原日文（Wokann `src/data/trade.h`）：

{COLOR 0x02}{HIGHLIGHT 0x01}{SHADOW 0x03}そのポケモンを　こうかんすると\nせんとうできなくなっちゃうよ！

原日文（ROM `0x08300B75`）：

{BYTE_FC}あい{BYTE_FC}いあ{BYTE_FC}ううそのポケモンを　こうかんすると\nせんとうできなくなっちゃうよ!

原英文（`src/data/trade.h`，`fe570a7e5^`）：

That's your only\nPOKéMON for battle.

美版文件：`src/data/trade.h`。

原美版中文：

最后1只同行的宝可梦\n不能用来交换。

最终美版中文：

交换这只宝可梦后，\n就没有能战斗的宝可梦了。

### 13286. gText_MomOrDadMightLikeThisProgram

状态：已修复、已构建；待模拟器验收。

日版文件：`patch/batches/432_checklist_scripts.json`。

原日版中文：

也许是{FD_02}喜欢的游戏\n…… …… …… …… …… …… …… ……\p该走了！

最终日版中文：

也许是{FD_02}喜欢的节目\n…… …… …… …… …… …… …… ……\p该走了！

原日文（Wokann `data/event_scripts.s`）：

{STR_VAR_1}が　すきそうな　ばんぐみをやってる！\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\pさきを　いそがなきゃ！$

原日文（ROM `0x08243A12`）：

{PLACEHOLDER_02}が　すきそうな　ばんぐみをやってる!\n…………………………………………………\pさきを　いそがなきゃ!

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

{STR_VAR_1} might like this program.\n… … … … … … … … … … … … … … … …\pBetter get going!$

美版文件：`data/event_scripts.s`。

原美版中文：

也许是{STR_VAR_1}喜欢的游戏\n…… …… …… …… …… …… …… ……\p该走了！$

最终美版中文：

也许是{STR_VAR_1}喜欢的节目\n…… …… …… …… …… …… …… ……\p该走了！$

### 13293. gText_PlayerWhitedOut

状态：已修复、已构建；待模拟器验收。

日版文件：`patch/batches/432_checklist_scripts.json`。

原日版中文：

{FD_01}没有可以\n战斗的宝可梦\p！{FD_01}昏迷了！

最终日版中文：

{FD_01}没有可以\n战斗的宝可梦！\p{FD_01}昏迷了！

原日文（Wokann `data/event_scripts.s`）：

{PLAYER}の　てもとには\nたたかえるポケモンが　もういない！\p{PLAYER}は\nめのまえが　まっくらに　なった！$

原日文（ROM `0x08243B4E`）：

{PLACEHOLDER_01}の　てもとには\nたたかえるポケモンが　もういない!\p{PLACEHOLDER_01}は\nめのまえが　まっくらに　なった!

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

{PLAYER} is out of usable\nPOKéMON!\p{PLAYER} whited out!$

美版文件：`data/event_scripts.s`。

原美版中文：

{PLAYER}没有可以\n战斗的宝可梦\p！{PLAYER}昏迷了！$

最终美版中文：

{PLAYER}没有可以\n战斗的宝可梦！\p{PLAYER}昏迷了！$
