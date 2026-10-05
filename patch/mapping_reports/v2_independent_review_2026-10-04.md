# v2 独立复核（2026-10-04）

## 基准与范围

- 日版 HEAD：`5604922996cc2a53ec7d7dc99253de5e3fb5e950`；美版 HEAD：`1cbb305f7ebd2038f0d0ebcba039b20fe18f21e3`。
- 基于原始报告、当前实际定义、baserom_jp.gba 原地址与 Wokann dev 原文，以及美版 Git `fe570a7e5^` 英文原文。未读取旧 review 的语义判定。
- 本轮只写审查报告，不改游戏文本、代码、ROM，不 commit/push；未做模拟器验证。
- v2范围为115 ERROR + 121 NEEDS_ATTENTION，共236条；并非重新语义审计全部14780条。
- v3范围为原建议报告65项、64个唯一资源；缺少报告提到的 audit_v3_us_only.csv，无法核查声称的484个待移植项。
- JSON保存完整原报告、当前定义、日英原文与地址证据。换行/分页/FD/F7控制符不能按两版字符串表面差异机械同步。
- 长文本的最终换行和显示宽度必须在实施时验证；本文给出的修改方向不是未经编译验证即可写入的字节串。

## 分类数量

- 不需修复：37条。
- 原问题已消除：117条。
- 需修复：16条。
- 已有移植：64条。
- 译名政策项：2条。

## 需修复索引

- 4397 `MossdeepCity_Gym_Text_CliffordPostBattle`：JP；日英版本差异，不应套用英文败战台词。日文在说道馆馆主年轻有活力，不是在说玩家。
- 4798 `gText_DexSortAtoZDescription`：JP；日文明确是五十音顺序；实际调用 gPokedexOrder_Alphabetical，并未改成中文拼音排序。字母顺序的说明会误导。
- 5803 `gText_NoticesGoldCard`：JP+US；金卡、金色、四颗星已补回，但后半仍没有明确金卡，且遗漏原文两次玩家名；属于部分修复。
- 6256 `BattleFrontier_BattlePikeRoomNormal_Text_AttacksWhenStartled`：JP+US；突然看见人受惊后扑过来，不是“不听指挥”。原文不存在“命令を無視して”。
- 6921 `BattleFrontier_OutsideEast_Text_ThriveInDarkness`：JP+US；第一句已修好；结尾仍将邀请一起探索变成问对方是否绝望。日文没有英文的 total desperation，不强行统一区域差异。
- 7183 `RustboroCity_House3_Text_NamingPikachuPekachu`：JP+US；PEKACHU/ペカチュウ是 PIKACHU/ピカチュウ的轻微改名；“猫卡球”丢失这一笑点。只改对话文本，不改保存的昵称。
- 7184 `RustboroCity_House3_Text_Pekachu`：JP+US；承接上一条的同一昵称与叫声，需一并统一。只改对话资源。
- 7558 `MoveTutor_Text_SubstituteTeach`：JP+US；重复“如果”已经修复；但 そうだわ / I know! 在此是想到一个主意，不是明白了别人说的话。
- 9110 `MauvilleCity_PokemonCenter_1F_Text_LedgesJumpedStory`：JP+US；“几经”和计数已修复，但把 ledges / だんさ译成岩礁，仍然错误；说的是地图可跳下的台阶。
- 10293 `sElixirDesc`：JP+US；原报告针对第四个招式的信息，当前没有该语义遗漏；独立检查发现“10PP”被断成“1\n0PP”，应避免数字跨行。
- 10399 `sSitrusBerryDesc`：JP+US；本作日英原文都明确回复30HP；实际 ITEM_SITRUS_BERRY 的 holdEffectParam 为30。“少量”省略可操作的固定数值。
- 12203 `sText_MysteryGiftVisitingTrainerInstructions`：JP；美版已补“在”；日版仍缺介词。日版有实际资源，并非“无对应”。另发现提示密码与服务名套用了英文版本。
- 12204 `sText_MysteryGiftVisitingTrainerArrived`：JP；美版已经修为希望；日版 batch471 尚为系统。日版原 ROM 0x085FCE8B 有对应文本。
- 13248 `sText_OnlyPkmnForBattle`：JP+US；已有移植，不是遗漏。但“最后1只同行的宝可梦”不等于“唯一能战斗的宝可梦”：还可能有其他濒死宝可梦或蛋。
- 13286 `gText_MomOrDadMightLikeThisProgram`：JP+US；已有移植，不是遗漏。ばんぐみ / program 在这里是电视节目，不是游戏。
- 13293 `gText_PlayerWhitedOut`：JP+US；已有移植，不是遗漏。第一句叹号被移到第二页开头，形成“！玩家……”；日英原文的叹号都在第一句末。

## 逐条复核

### 77 — sHugePowerDescription

结论：**不需修复**。

实际第三世代大力士机制说明；原文简略不等于补充真实倍率就是错误。

方案：保留当前文本/布局。

原报告问题：

CHS添加'物理攻击的威力会变为2倍'。JP'こうげきりょくがたかい'、EN'Raises ATTACK.'均未提及2倍。第三世代大力士确为攻击×2，机制准确但属增补。

当前日版：

`物理攻击的威力会变为2倍`

文件：`patch/ability_descriptions.json`。

原英文（`src/data/text/abilities.h`，`fe570a7e5^`）：

`Raises ATTACK.`

当前美版（`src/data/text/abilities.h`）：

`物理攻击的威力会变为2倍`

### 151 — sPurePowerDescription

结论：**不需修复**。

实际第三世代瑜伽之力机制说明；不要求删除真实倍率。

方案：保留当前文本/布局。

原报告问题：

CHS添加'物理攻击的威力会变为2倍'。JP'こうげきりょくがたかい'、EN'Raises ATTACK.'均未提及2倍。第三世代瑜伽之力确为攻击×2，机制准确但属增补。

当前日版：

`物理攻击的威力会变为2倍`

文件：`patch/ability_descriptions.json`。

原英文（`src/data/text/abilities.h`，`fe570a7e5^`）：

`Raises ATTACK.`

当前美版（`src/data/text/abilities.h`）：

`物理攻击的威力会变为2倍`

### 519 — sSpiteDescription

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS作'减少4PP该招式'，但第三世代怨恨减少PP为2～5随机（非固定4）。JP'そのわざポイントをへらしてしまう'、EN'Spitefully cuts the PP'均未指定具体数值。

当前日版：

`怨恨对手最后用的招式，\n减少该招式的PP。`

文件：`patch/move_descriptions.json`。

原英文（`src/data/text/move_descriptions.h`，`fe570a7e5^`）：

`Spitefully cuts the PP\nof the foe's last move.`

当前美版（`src/data/text/move_descriptions.h`）：

`怨恨对手最后用的招式，\n减少该招式的PP。`

### 613 — sEncoreDescription

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

回合数错误：CHS作'3～6回合'，JP作'2-6かい'、EN作'2 to 6 turns'。第三世代再来一次为2～6回合。

当前日版：

`让对手接受再来一次，\n在2～6回合内重复最后的招式。`

文件：`patch/move_descriptions.json`。

原英文（`src/data/text/move_descriptions.h`，`fe570a7e5^`）：

`Makes the foe repeat its\nlast move over 2 to 6 turns.`

当前美版（`src/data/text/move_descriptions.h`）：

`让对手接受再来一次，\n在2～6回合内重复最后的招式。`

### 725 — sEndeavorDescription

结论：**不需修复**。

蛮干描述按实际伤害机制表达，比原文的差值描述明确，不回退。

方案：保留当前文本/布局。

原报告问题：

JP'じぶんのたいりょくがあいてよりすくないほどダメ-ジをあたえる'、EN'Gains power if the user\'s HP is lower'描述的是抓狂/绝处逢生类效果，与蛮干（使对手HP与自己相同）的实际机制不符。CHS'使对手的HP变得和自己的HP一样'纠正了官方误导性描述，但偏离了JP/EN原文。

当前日版：

`给予伤害，使对手的HP\n变得和自己的HP一样。`

文件：`patch/move_descriptions.json`。

原英文（`src/data/text/move_descriptions.h`，`fe570a7e5^`）：

`Gains power if the user's HP\nis lower than the foe's HP.`

当前美版（`src/data/text/move_descriptions.h`）：

`给予伤害，使对手的HP\n变得和自己的HP一样。`

### 817 — sSheerColdDescription

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS添加'若冰属性以外宝可梦使用会难以打中'。这是第七世代起的机制（冰属性使用一击必杀命中率提高），第三世代中绝对零度对所有属性均为30%命中率。JP'きまるとせんとうふのうになる'、EN'causes fainting if it hits'均未提及属性差异。

当前日版：

`以绝对零度攻击对手。\n命中后会使对手一击昏厥。`

文件：`patch/move_descriptions.json`。

原英文（`src/data/text/move_descriptions.h`，`fe570a7e5^`）：

`A chilling attack that\ncauses fainting if it hits.`

当前美版（`src/data/text/move_descriptions.h`）：

`以绝对零度攻击对手。\n命中后会使对手一击昏厥。`

### 1044 — gTogeticPokedexText

结论：**不需修复**。

原文“心の持ち主”没有严格排除宝可梦；不构成明确事实错误。

方案：保留当前文本/布局。

原报告问题：

CHS增补"或宝可梦"。JP: じゅんすいなこころのもちぬし（心灵纯洁的人）；EN: someone who is pure of heart。CHS作"心灵纯洁的人或宝可梦"。轻微润色，不影响核心事实。

当前日版：

`据说是会带来幸运的宝可梦。如果发现心灵纯洁的人或宝可梦，\n就会现身并将幸福分给他们。`

文件：`patch/pokedex_entries.json`。

Wokann日文（`src/data/pokemon/pokedex_text.h`）：

`こううんを　もたらす　ポケモンと　いわれている。\nじゅんすいな　こころの　もちぬしを　みつけると\nすがたを　あらわし　しあわせを　わけあたえる。`

原英文（`src/data/pokemon/pokedex_text.h`，`fe570a7e5^`）：

`It is said to be a POKéMON that brings good\nfortune. When it spots someone who is pure\nof heart, a TOGETIC appears and shares its\nhappiness with that person.`

当前美版（`src/data/pokemon/pokedex_text.h`）：

`据说是会带来幸运的宝可梦。如果发现心灵纯洁的人或宝可梦，\n就会现身并将幸福分给他们。`

### 1098 — gKingdraPokedexText

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS把"渦潮"译成"巨大海浪"。JP: ふねをのみこむほどおおきなうずしおがはっせいする；EN: it creates a huge whirlpool that can swallow even ships。海浪≠漩涡，物理现象用词错误。

当前日版：

`在深沉的海底里静静地沉睡着。当它浮出水面的时候，会产生足以将船只吞没的巨大漩涡。`

文件：`patch/pokedex_entries.json`。

Wokann日文（`src/data/pokemon/pokedex_text.h`）：

`ふかい　かいていで　しずかに　ねむる。\nすいめんへ　あがってくるとき　ふねを　のみこむ\nほど　おおきな　うずしおが　はっせいする。`

原英文（`src/data/pokemon/pokedex_text.h`，`fe570a7e5^`）：

`It sleeps quietly, deep on the seafloor.\nWhen it comes up to the surface, it\ncreates a huge whirlpool that can swallow\neven ships.`

当前美版（`src/data/pokemon/pokedex_text.h`）：

`在深沉的海底里静静地沉睡着。当它浮出水面的时候，会产生足以将船只吞没的巨大漩涡。`

### 1099 — gPhanpyPokedexText

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS增补了JP/EN没有的"前进"。JP: あつくなるとぱたぱたあおいで すずむ（扇动纳凉）；EN: flaps the ears busily to cool down。CHS作"扇动着前进"，多了"前进"动作。

当前日版：

`小小象的巨大耳朵可以代替扇子，天气热的时候会啪嗒啪嗒扇动耳朵纳凉，\n即使是幼年时力气也非常大。`

文件：`patch/pokedex_entries.json`。

Wokann日文（`src/data/pokemon/pokedex_text.h`）：

`ゴマゾウの　おおきな　みみは　うちわの　かわり。\nあつくなると　ぱたぱた　あおいで　すずむ。\nこどもでも　ちからは　とても　つよい。`

原英文（`src/data/pokemon/pokedex_text.h`，`fe570a7e5^`）：

`PHANPY's big ears serve as broad fans.\nWhen it becomes hot, it flaps the ears\nbusily to cool down. Even the young are\nvery strong.`

当前美版（`src/data/pokemon/pokedex_text.h`）：

`小小象的巨大耳朵可以代替扇子，天气热的时候会啪嗒啪嗒扇动耳朵纳凉，\n即使是幼年时力气也非常大。`

### 1160 — gShedinjaPokedexText

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP: からだの なかは くうどうで まっくら（身体内部中空，一片漆黑）；EN: hollow and utterly dark。CHS作"里面什么也没有"。漆黑≠空无。

当前日版：

`没有拍动翅膀就可以飞在天上的相当特别的宝可梦，身体是中空的，\n里面一片漆黑。`

文件：`patch/pokedex_entries.json`。

Wokann日文（`src/data/pokemon/pokedex_text.h`）：

`ハネを　まったく　うごかして　いないのに\nくうちゅうに　うかんでいる　ふしぎな　ポケモン。\nからだの　なかは　くうどうで　まっくら。`

原英文（`src/data/pokemon/pokedex_text.h`，`fe570a7e5^`）：

`A peculiar POKéMON that floats in air even\nthough its wings remain completely still.\nThe inside of its body is hollow and\nutterly dark.`

当前美版（`src/data/pokemon/pokedex_text.h`）：

`没有拍动翅膀就可以飞在天上的相当特别的宝可梦，身体是中空的，\n里面一片漆黑。`

### 1168 — gSkittyPokedexText

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP: たたかうときは しっぽを けばだたせる（战斗时把尾毛炸开/竖起）；EN: makes its tail puff out。CHS作"拍动尾巴上的毛"。炸开≠拍动。

当前日版：

`以其非常怜爱的动作大受欢迎。战斗的时候会竖起尾巴上的毛。\n能发出尖锐的叫声威吓敌人。`

文件：`patch/pokedex_entries.json`。

Wokann日文（`src/data/pokemon/pokedex_text.h`）：

`あいきょう　たっぷりの　しぐさで　だいにんき。\nたたかう　ときは　しっぽを　けばだたせる。\nするどい　うなりごえを　あげて　てきを　いかく。`

原英文（`src/data/pokemon/pokedex_text.h`，`fe570a7e5^`）：

`A SKITTY's adorably cute behavior makes it\nhighly popular. In battle, it makes its tail\npuff out. It threatens foes with a sharp\ngrowl.`

当前美版（`src/data/pokemon/pokedex_text.h`）：

`以其非常怜爱的动作大受欢迎。战斗的时候会竖起尾巴上的毛。\n能发出尖锐的叫声威吓敌人。`

### 1179 — gPluslePokedexText

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP: りょうてから はっした でんきを ショートさせて ひばなの ボンボンを つくる（将两手释放的电力短路制成火花花球）；EN: By shorting out the electricity it releases from its paws, it creates pom-poms for cheering。CHS作"将电力发射出去做出火花的碰撞效果"，机制（短路→发射）失真，且丢失"加油用花球"用途。

当前日版：

`具有会为伙伴宝可梦加油的习性。可以让两手释放的电力短路，\n制成用于加油的火花花球。`

文件：`patch/pokedex_entries.json`。

Wokann日文（`src/data/pokemon/pokedex_text.h`）：

`なかまの　ポケモンを　おうえんする　しゅうせい。\nりょうてから　はっした　でんきを　ショートさせて\nひばなの　ボンボンを　つくる　ことが　できる。`

原英文（`src/data/pokemon/pokedex_text.h`，`fe570a7e5^`）：

`It has the trait of cheering on its fellow\nPOKéMON. By shorting out the electricity\nit releases from its paws, it creates\npom-poms for cheering.`

当前美版（`src/data/pokemon/pokedex_text.h`）：

`具有会为伙伴宝可梦加油的习性。可以让两手释放的电力短路，\n制成用于加油的火花花球。`

### 1215 — gAnorithPokedexText

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP: さゆう8まいの はねを くねらせて およぐ（摆动8片翅游泳），あしが ハネに かわった（脚变成了翅）；EN: undulating the eight wings。CHS两处作"羽毛"。羽毛专指plumage，该生物用翅状肢游泳。

当前日版：

`以科学的力量从化石中再度复活。会以摆动左右的8片翅膀的方式游动。\n居住在海里的时候脚变成了翅膀。`

文件：`patch/pokedex_entries.json`。

Wokann日文（`src/data/pokemon/pokedex_text.h`）：

`かがくの　ちからで　かせきから　よみがえった。\nさゆう　8まいの　はねを　くねらせて　およぐ。\nうみで　くらすうちに　あしが　ハネに　かわった。`

原英文（`src/data/pokemon/pokedex_text.h`，`fe570a7e5^`）：

`It was resurrected from a fossil using the\npower of science. It swims by undulating\nthe eight wings at its sides. They were\nfeet that adapted to life in the sea.`

当前美版（`src/data/pokemon/pokedex_text.h`）：

`以科学的力量从化石中再度复活。会以摆动左右的8片翅膀的方式游动。\n居住在海里的时候脚变成了翅膀。`

### 1216 — gArmaldoPokedexText

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP: ふだんは ちじょうで くらす（平常在地上/陆地生活）；EN: ARMALDO usually lives on land。CHS作"平常都住在地底下"。陆地≠地底。

当前日版：

`虽然太古盔甲平常都住在陆地上，不过在捕捉猎物的时候就会潜入海中，\n利用两片巨大的翅膀来游泳。`

文件：`patch/pokedex_entries.json`。

Wokann日文（`src/data/pokemon/pokedex_text.h`）：

`ふだんは　ちじょうで　くらす　アーマルドだが\nえものを　とる　ときには　うみに　もぐり\n2まいの　おおきな　はねを　つかって　およぐ。`

原英文（`src/data/pokemon/pokedex_text.h`，`fe570a7e5^`）：

`ARMALDO usually lives on land. However,\nwhen it hunts for prey, it dives beneath\nthe ocean. It swims around using its two\nlarge wings.`

当前美版（`src/data/pokemon/pokedex_text.h`）：

`虽然太古盔甲平常都住在陆地上，不过在捕捉猎物的时候就会潜入海中，\n利用两片巨大的翅膀来游泳。`

### 1218 — gMiloticPokedexText

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP: おおきな みずうみの そこに いる（大湖的底部）；EN: live at the bottom of large lakes。CHS作"生活在广大的湖边"。湖底≠湖边。

当前日版：

`据说它生活在大湖的底部。被人称为最美丽的宝可梦，也被当作绘画与雕刻的对象。`

文件：`patch/pokedex_entries.json`。

Wokann日文（`src/data/pokemon/pokedex_text.h`）：

`おおきな　みずうみの　そこに　いると　いわれる。\nもっとも　うつくしい　ポケモンと　いわれていて\nかいがや　ちょうこくの　モデルと　なっている。`

原英文（`src/data/pokemon/pokedex_text.h`，`fe570a7e5^`）：

`It is said to live at the bottom of\nlarge lakes. Considered to be the most\nbeautiful of all POKéMON, it has been\ndepicted in paintings and statues.`

当前美版（`src/data/pokemon/pokedex_text.h`）：

`据说它生活在大湖的底部。被人称为最美丽的宝可梦，也被当作绘画与雕刻的对象。`

### 1643 — Route104_Text_RouteSignPetalburg

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS作"1O4号道路"（字母O）。JP作"104ばんどうろ"、EN源作"ROUTE 1O4"（美版源亦有笔误）。应为数字104。

当前日版：

`104号道路\nワ橙华市`

文件：`patch/batches/017_route104.json`。

原日文（`0x081E7D65`）：

`ここは　104ばん　どうろ\n{BYTE_FC}しう　トウカシティ`

Wokann日文（`data/maps/Route104/scripts.inc`）：

`ここは　104ばん　どうろ\n{RIGHT_ARROW}　トウカシティ$`

原英文（`data/maps/Route104/scripts.inc`，`fe570a7e5^`）：

`ROUTE 1O4\n{RIGHT_ARROW} PETALBURG CITY$`

当前美版（`data/maps/Route104/scripts.inc`）：

`104号道路\n{RIGHT_ARROW}橙华市$`

### 4394 — MossdeepCity_Gym_Text_BlakePostBattle

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「はないきで とばして なんか いないぞ」(我可没用鼻息吹它)/EN「I didn't blow on it! Honestly!」均指"用嘴/鼻吹气作弊"，CHS「我没吹牛」将"吹"误作"吹牛(说大话)"，语义错误

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

### 4397 — MossdeepCity_Gym_Text_CliffordPostBattle

结论：**需修复**。

日英版本差异，不应套用英文败战台词。日文在说道馆馆主年轻有活力，不是在说玩家。

方案：这里的道馆馆主也一样！\n年轻又充满活力！

原报告问题：

JP「この ジムの リーダーも そりゃもう! わかくて げんき はつらつ ですぞ」主语是"道馆馆主们(年轻有活力)"；EN「It seems that I could not overcome your youthful energy」/CHS「看来我无法胜过你的活力」主语是"你(玩家)的活力"，三方主语不一致

当前日版：

`看来我无法胜过\n你的活力。`

文件：`patch/batches/152_mossdeepcity_gym.json`。

原日文（`0x0820BD63`）：

`この　ジムの　リ-ダ-も　そりゃもう!\nわかくて　げんき　はつらつ　ですぞ`

Wokann日文（`data/maps/MossdeepCity_Gym/scripts.inc`）：

`この　ジムの　リーダーも　そりゃもう！\nわかくて　げんき　はつらつ　ですぞ$`

原英文（`data/maps/MossdeepCity_Gym/scripts.inc`，`fe570a7e5^`）：

`It seems that I could not overcome\nyour youthful energy.$`

当前美版（`data/maps/MossdeepCity_Gym/scripts.inc`）：

`看来我无法胜过\n你的活力。$`

### 4516 — MossdeepCity_StevensHouse_Text_LetterFromSteven

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS「已我决定踏上自我探索与修行之旅」中"已我"为"我已"之误写(字序颠倒)，JP「ボクは おもうことが あって しばらく しゅぎょうを つづける」/EN「I've decided to do a little soul-searching and train on the road」均为"我已决定…"；ref-us-chs 源码 data/maps/MossdeepCity_StevensHouse/scripts.inc:168 原文即作"已我决定"

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

### 4712 — gText_Confirm3

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

Wokann 沿用美版符号名，但 JP 文本语义与符号名倒置：gText_Confirm3 的 JP 文本为「もどる」(返回，用于时钟查看画面的返回按钮)，gText_Cancel4 的 JP 文本为「けってい」(决定，用于时钟设置画面的确认按钮)。补丁 batch(168_core_interfaces.json)按符号名写入 us_encoded_hex 解码为「确定」→ gText_Confirm3 槽、「取消」→ gText_Cancel4 槽，导致日版游戏中返回按钮显示"确定"、决定按钮显示"取消"，标签与功能错位

当前日版：

`返回`

文件：`patch/batches/168_core_interfaces.json`。

原日文（`0x08591C15`）：

`けってい`

Wokann日文（`src/wallclock.c`）：

`もどる　`

原英文（`src/strings.c`，`fe570a7e5^`）：

`CONFIRM`

当前美版（`src/strings.c`）：

`确定`

### 4713 — gText_Cancel4

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

同 3457：gText_Cancel4 的 JP 文本为「けってい」(决定)，补丁按符号名写入「取消」，导致时钟设置画面的确认按钮显示"取消"，标签与功能错位

当前日版：

`确定`

文件：`patch/batches/168_core_interfaces.json`。

原日文（`0x08591C1A`）：

`もどる　`

Wokann日文（`src/wallclock.c`）：

`けってい`

原英文（`src/strings.c`，`fe570a7e5^`）：

`CANCEL`

当前美版（`src/strings.c`）：

`取消`

### 4763 — gText_SizeComparedTo

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「の　おおきさくらべ」/EN「SIZE COMPARED TO 」均为无占位符的片段文本；CHS「{STR_VAR_1}与{STR_VAR_2}的体型比较」凭空引入 {STR_VAR_1}/{STR_VAR_2}，且 ref-us-chs src/pokedex.c:3764 使用处前后未填充 gStringVar1/2，占位符无法正确展开

当前日版：

`的体型比较`

文件：`patch/batches/171_pokedex.json`。

原日文（`0x085C8FDD`）：

`の　おおきさくらべ`

当前日版：

`与`

文件：`patch/batches/171_pokedex.json`。

原日文（`0x085C8FDB`）：

`と`

Wokann日文（`src/data/text/region_texts76.h`）：

`の　おおきさくらべ`

原英文（`src/strings.c`，`fe570a7e5^`）：

`SIZE COMPARED TO `

当前美版（`src/strings.c`）：

`与`

### 4798 — gText_DexSortAtoZDescription

结论：**需修复**。

日文明确是五十音顺序；实际调用 gPokedexOrder_Alphabetical，并未改成中文拼音排序。字母顺序的说明会误导。

方案：按名称顺序排列\n已发现的宝可梦。

原报告问题：

JP「みつけたポケモンの　なまえを　ごじゅうおんじゅんで」限定"已发现的宝可梦"；EN「Spotted and owned POKéMON are listed alphabetically」/CHS「已发现和已获得的宝可梦」范围更广。CHS 忠实翻译 EN，但无法确认日版 ROM 实际行为与哪方一致，需 ROM 验证

当前日版：

`按字母的顺序来排列已发现\n和已获得的宝可梦。`

文件：`patch/batches/171_pokedex.json`。

原日文（`0x085C91E2`）：

`みつけたポケモンの　なまえを\nごじゅうおんじゅんで　ひょうじ　します`

Wokann日文（`src/data/text/region_texts76.h`）：

`みつけたポケモンの　なまえを\nごじゅうおんじゅんで　ひょうじ　します`

原英文（`src/strings.c`，`fe570a7e5^`）：

`Spotted and owned POKéMON are listed\nalphabetically.`

当前美版（`src/strings.c`）：

`按字母的顺序来排列已发现\n和已获得的宝可梦。`

### 5005 — gText_EmptyString6

结论：**不需修复**。

美版资源本来为空；日文计数后缀属于区域显示布局，不能向共享空串随意写入汉字。

方案：保留当前文本/布局。

原报告问题：

JP「ひき」(训练家卡捕获数单位，123ひき) vs EN/CHS 均为空；美版有意留空（符号名即 EmptyString6），属美版与日版的版本差异；该条未被补丁覆盖（NOPATCH），不影响补丁后游戏

Wokann日文（`src/data/text/region_texts101.h`）：

`ひき`

原英文（`src/strings.c`，`fe570a7e5^`）：

``

当前美版（`src/strings.c`）：

``

### 5133 — gRegionMapEntries[87].name

结论：**不需修复**。

MAPSEC_DYNAMIC 空槽是动态地图名占位，不是漏译。

方案：保留当前文本/布局。

原报告问题：

gRegionMapEntries[87].name = MAPSEC_DYNAMIC，为动态地图名占位槽，JP/EN/CHS 三方均为空（设计如此，无实质文本内容）；且未被补丁覆盖

当前日版：

`{'kind': 'us_region_map_table', 'name': 'ChsRegionMapEntries', 'source': '../../pokeemerald_us_chs/src/data/region_map/region_map_sections.json', 'base_offset': '0x57CD6C', 'count': 213, 'stride': 8, 'name_offset': 4, 'source_commit': 'ec1ebe69d'}`

文件：`patch/region_map_names.json`。

### 5261 — gText_UserMoreEasilyStartled

结论：**已有移植**。

对应中文不是同名符号，而是 batch175 ChsContestEffectDesc1：使用这个招式后，会更容易受到干扰。原理由提到另一段表演文本，与此资源不符。

方案：不重复添加。

原报告问题：

US-CHS 在句末添加了'虽然能够演出很好的表演'，JP「アピールが　うまく　きまった！」/EN 'The appeal went well!' 均无此意。

Wokann日文（`data/text/contest_strings.inc`）：

`この　アピールの　あと\nびっくり　しやすく　なってしまう$`

原英文（`data/text/contest_strings.inc`，`fe570a7e5^`）：

`After this move, the user is\nmore easily startled.$`

当前美版（`data/text/contest_strings.inc`）：

`使用这个招式后，\n会更容易受到干扰。$`

### 5324 — gText_Var1AndYouWantedVar2

结论：**不需修复**。

円在数字右侧为明确需求，不能按美版前置货币符号回退。

方案：保留当前文本/布局。

原报告问题：

补丁把 ¥ 移到变量之后：US-CHS'¥{STR_VAR_1}'（¥在前，符合中文习惯），补丁'{STR_VAR_1}¥'。同批其余条目均为 ¥ 在前。

当前日版：

`是{FD_02}啊。\n{FD_03}个一共是{FD_04}¥。`

文件：`patch/batches/177_shop.json`。

原日文（`0x085C991F`）：

`{PLACEHOLDER_02}を　{PLACEHOLDER_03}コで\n{PLACEHOLDER_04}¥　おかいあげですか?`

原英文（`src/strings.c`，`fe570a7e5^`）：

`{STR_VAR_1}? And you wanted {STR_VAR_2}?\nThat will be ¥{STR_VAR_3}.`

当前美版（`src/strings.c`）：

`是{STR_VAR_1}啊。\n{STR_VAR_2}个一共是¥{STR_VAR_3}。`

### 5325 — gText_Var1IsItThatllBeVar2

结论：**不需修复**。

円后置为明确需求。

方案：保留当前文本/布局。

原报告问题：

补丁把 ¥ 移到变量之后：US-CHS'¥{STR_VAR_2}'，补丁'{STR_VAR_2}¥'。

当前日版：

`是{FD_02}啊。\n价格是{FD_03}¥。`

文件：`patch/batches/177_shop.json`。

原日文（`0x085C9936`）：

`{PLACEHOLDER_02}　だね!\n{PLACEHOLDER_03}¥　だけど　かうかい?`

原英文（`src/strings.c`，`fe570a7e5^`）：

`{STR_VAR_1}, is it?\nThat'll be ¥{STR_VAR_2}. Do you want it?`

当前美版（`src/strings.c`）：

`是{STR_VAR_1}啊。\n价格是¥{STR_VAR_2}。`

### 5326 — gText_YouWantedVar1ThatllBeVar2

结论：**不需修复**。

円后置为明确需求。

方案：保留当前文本/布局。

原报告问题：

补丁把 ¥ 移到变量之后：US-CHS'¥{STR_VAR_3}'，补丁'{STR_VAR_3}¥'。

当前日版：

`是{FD_02}啊。\n价格是{FD_03}¥，可以吗？`

文件：`patch/batches/177_shop.json`。

原日文（`0x085C994B`）：

`{PLACEHOLDER_02}　ですね!\n{PLACEHOLDER_03}¥　だけど　かいますか?`

原英文（`src/strings.c`，`fe570a7e5^`）：

`You wanted {STR_VAR_1}?\nThat'll be ¥{STR_VAR_2}. Will that be okay?`

当前美版（`src/strings.c`）：

`是{STR_VAR_1}啊。\n价格是¥{STR_VAR_2}，可以吗？`

### 5336 — sText_PkmnGainedEXP

结论：**不需修复**。

日版原参数为名字和数值；不同于美版 B_BUFF3 拼接。当前保留经验值及叹号，无需新增美版变量。

方案：保留当前文本/布局。

原报告问题：

补丁删除了'\n{B_BUFF3}'（获得的经验值数值）：US-CHS'{STR_VAR_1}获得了\n{B_BUFF3}点经验值！'，补丁'{STR_VAR_1}获得了点经验值！'，数值丢失。

当前日版：

`{FD_00}获得了{FD_01}经验值！\p`

文件：`patch/batches/178_battle_victory.json`。

原日文（`0x085A962B`）：

`{PLACEHOLDER_00}{PLACEHOLDER_01}　けいけんちを　もらった!\p`

Wokann日文（`src/battle_message.c`）：

`{B_BUFF1}{B_BUFF2}　けいけんちを　もらった！\p`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_BUFF1} gained{B_BUFF2}\n{B_BUFF3} EXP. Points!\p`

当前美版（`src/battle_message.c`）：

`{B_BUFF1}获得了{B_BUFF2}\n{B_BUFF3}经验值！\p`

### 5345 — sText_PlayerGotMoney

结论：**不需修复**。

円后置且末尾已有换页符；不是遗漏。

方案：保留当前文本/布局。

原报告问题：

补丁 ¥ 位置错误：US-CHS'¥{B_BUFF1}'（¥在前），补丁'{B_BUFF1}{JPN}¥{ENG}'（¥在中）。

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

### 5346 — sText_PlayerPickedUpMoney

结论：**不需修复**。

円后置为明确需求。

方案：保留当前文本/布局。

原报告问题：

补丁 ¥ 位置错误：US-CHS'¥{B_BUFF1}'，补丁'{B_BUFF1}{JPN}¥{ENG}'。

当前日版：

`{FD_23}捡到了\n{FD_00}{JPN}¥{ENG}！\p`

文件：`patch/batches/178_battle_victory.json`。

原日文（`0x085A9EE5`）：

`{PLACEHOLDER_23}は　{PLACEHOLDER_00}¥\nひろった!\p`

Wokann日文（`src/battle_message.c`）：

`{B_PLAYER_NAME}は　{B_BUFF1}¥\nひろった！\p`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_PLAYER_NAME} picked up\n¥{B_BUFF1}!\p`

当前美版（`src/battle_message.c`）：

`{B_PLAYER_NAME}捡到了\n¥{B_BUFF1}！\p`

### 5355 — BerryTree_Text_BerryGrowthStage3

结论：**不需修复**。

报告理由引用表演文本，但当前条目实际是树果树干长高；符号与理由不匹配。

方案：保留当前文本/布局。

原报告问题：

US-CHS 添加了'漂亮'二字：'完成了漂亮的表演'；JP「アピールが　きまった！」/EN 'The appeal was a success!' 均无'漂亮'之意。

当前日版：

`{FD_02}的树干长高了！`

文件：`patch/batches/179_berry.json`。

原日文（`0x08244F5A`）：

`{PLACEHOLDER_02}の　みきが　おおきく　なってきた!`

Wokann日文（`data/scripts/berry_tree.inc`）：

`{STR_VAR_1}の　みきが　おおきく　なってきた！$`

原英文（`data/scripts/berry_tree.inc`，`fe570a7e5^`）：

`This {STR_VAR_1} plant is growing taller.$`

当前美版（`data/scripts/berry_tree.inc`）：

`{STR_VAR_1}的树干长高了！${STR_VAR_1}正在变得更高。$`

### 5356 — BerryTree_Text_BerryGrowthStage4

结论：**不需修复**。

报告理由引用表演文本，但实际为树果开花，当前 FD_02/03 均保留。

方案：保留当前文本/布局。

原报告问题：

US-CHS 丢失了 {STR_VAR_2} 占位符：JP「{STR_VAR_1}の　{STR_VAR_2}が　きまった！」/EN '{STR_VAR_1}'s {STR_VAR_2} was a success!' 有两个占位符，CHS'完成了{STR_VAR_1}的表演'只有 {STR_VAR_1}。

当前日版：

`{FD_02}的花\n{FD_03}盛开着！`

文件：`patch/batches/179_berry.json`。

原日文（`0x08244F6E`）：

`{PLACEHOLDER_02}の　はなが　{PLACEHOLDER_03}　さいてる!`

Wokann日文（`data/scripts/berry_tree.inc`）：

`{STR_VAR_1}の　はなが　{STR_VAR_2}　さいてる！$`

原英文（`data/scripts/berry_tree.inc`，`fe570a7e5^`）：

`These {STR_VAR_1} flowers are blooming\n{STR_VAR_2}.$`

当前美版（`data/scripts/berry_tree.inc`）：

`{STR_VAR_1}的花\n{STR_VAR_2}盛开着！${STR_VAR_1}的花正在{STR_VAR_2}盛开\n。`

### 5393 — BattleFrontier_Lounge5_Text_NatureGirlNaive

结论：**不需修复**。

报告将合并性格模板拆成不存在的独立符号；应核对 DocileNaiveQuietQuirky，不新增重复文本。

方案：保留当前文本/布局。

原报告问题：

符号 AbandonedShip_Rooms2_1F_Text_NatureGirlNaive 在 Wokann/US-CHS/EN pickle/补丁中均不存在（幽灵符号），真实符号为 _DocileNaiveQuietQuirky。

### 5396 — BattleFrontier_Lounge5_Text_NatureGirlQuiet

结论：**不需修复**。

同上，Quiet 没有此独立资源。

方案：保留当前文本/布局。

原报告问题：

符号 AbandonedShip_Rooms2_1F_Text_NatureGirlQuiet 在 Wokann/US-CHS/EN pickle/补丁中均不存在（幽灵符号），真实符号为 _DocileNaiveQuietQuirky。

### 5422 — sText_PkmnHurtsWith

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 主被动颠倒：JP「{B_DEF_NAME_WITH_PREFIX}の　{B_DEF_ABILITY}で {B_ATK_NAME_WITH_PREFIX}は　きずついた！」/EN '{DEF}'s {ABILITY} hurt {ATK}!' 是 ATK 被 DEF 的特性所伤；CHS'{DEF}因{ABILITY}的{ATK}而受到了伤害！' 写成 DEF 被伤害，逻辑相反。

当前日版：

`{FD_0F}因\n{FD_10}的{FD_19}\l而受到了伤害！`

文件：`patch/batches/188_battle_damage_messages.json`。

原日文（`0x085AA6C6`）：

`{PLACEHOLDER_10}の　{PLACEHOLDER_19}で\n{PLACEHOLDER_0F}は　きずついた!`

Wokann日文（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}の　{B_DEF_ABILITY}で\n{B_ATK_NAME_WITH_PREFIX}は　きずついた！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_DEF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nhurt {B_ATK_NAME_WITH_PREFIX}!`

当前美版（`src/battle_message.c`）：

`{B_ATK_NAME_WITH_PREFIX}因\n{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}\l而受到了伤害！`

### 5438 — sText_PkmnPoisonedBy

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 占位符错乱：JP「{SCR}の　{ABILITY}で {EFF}は　どくをあびた」/EN '{SCR}'s {ABILITY} poisoned {EFF}!'；CHS'因{EFF}的{SCR}，{ABILITY}中毒了！' 把 {ABILITY} 写成中毒主体，因果倒置。

当前日版：

`{FD_11}因\n{FD_13}的{FD_1A}\l而中毒了！`

文件：`patch/batches/189_battle_status_and_core_results.json`。

原日文（`0x085A988E`）：

`{PLACEHOLDER_13}の　{PLACEHOLDER_1A}で\n{PLACEHOLDER_11}は　どくをあびた!`

Wokann日文（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}の　{B_SCR_ACTIVE_ABILITY}で\n{B_EFF_NAME_WITH_PREFIX}は　どくをあびた！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\npoisoned {B_EFF_NAME_WITH_PREFIX}!`

当前美版（`src/battle_message.c`）：

`{B_EFF_NAME_WITH_PREFIX}因\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}的{B_SCR_ACTIVE_ABILITY}\l而中毒了！`

### 5465 — sText_PkmnInLove

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 爱慕方向颠倒：JP「{ATK}は {SCR}に　メロメロだ」/EN '{ATK} is in love with {SCR}!' 是 ATK 爱上 SCR；CHS'{ATK}让{SCR}着迷了！' 写成 ATK 使 SCR 着迷，方向相反。

当前日版：

`{FD_0F}对\n{FD_13}着迷了！`

文件：`patch/batches/189_battle_status_and_core_results.json`。

原日文（`0x085A9AA2`）：

`{PLACEHOLDER_0F}は\n{PLACEHOLDER_13}に　メロメロだ!`

Wokann日文（`src/battle_message.c`）：

`{B_ATK_NAME_WITH_PREFIX}は\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}に　メロメロだ！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_ATK_NAME_WITH_PREFIX} is in love\nwith {B_SCR_ACTIVE_NAME_WITH_PREFIX}!`

当前美版（`src/battle_message.c`）：

`{B_ATK_NAME_WITH_PREFIX}对\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}着迷了！`

### 5488 — sText_PkmnClamped

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 主被动颠倒：JP「{DEF}は　{ATK}の　からに　はさまれた」/EN '{ATK} CLAMPED {DEF}!' 是 DEF 被 ATK 的贝壳夹住；CHS'{ATK}被{DEF}的贝壳夹住了！' 写成 ATK 被夹，颠倒。

当前日版：

`{FD_10}\n被{FD_0F}的贝壳夹住了！`

文件：`patch/batches/190_battle_move_effects.json`。

原日文（`0x085A9CC2`）：

`{PLACEHOLDER_10}は　{PLACEHOLDER_0F}の\nからに　はさまれた!`

Wokann日文（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}は　{B_ATK_NAME_WITH_PREFIX}の\nからに　はさまれた！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_ATK_NAME_WITH_PREFIX} CLAMPED\n{B_DEF_NAME_WITH_PREFIX}!`

当前美版（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}\n被{B_ATK_NAME_WITH_PREFIX}的贝壳夹住了！`

### 5512 — sText_PkmnStayedAwakeUsing

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_10}因{FD_19}\n不会睡着！`

文件：`patch/batches/190_battle_move_effects.json`。

原日文（`0x085A9EA8`）：

`{PLACEHOLDER_10}は\n{PLACEHOLDER_19}で　ねむらない!`

Wokann日文（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}は\n{B_DEF_ABILITY}で　ねむらない！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_DEF_NAME_WITH_PREFIX} stayed awake\nusing its {B_DEF_ABILITY}!`

当前美版（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会睡着！`

### 5585 — sText_PkmnRaisedSpeed

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_13}因{FD_1A}\n速度提高了！`

文件：`patch/batches/191_battle_moves_abilities_results.json`。

原日文（`0x085AA5B0`）：

`{PLACEHOLDER_13}は　{PLACEHOLDER_1A}で\nすばやさが　あがった!`

Wokann日文（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\nすばやさが　あがった！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\nraised its SPEED!`

当前美版（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n速度提高了！`

### 5588 — sText_PkmnRestoredHPUsing

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_10}因{FD_19}\n体力回复了！`

文件：`patch/batches/191_battle_moves_abilities_results.json`。

原日文（`0x085AA5EA`）：

`{PLACEHOLDER_10}は　{PLACEHOLDER_19}で\nかいふくした!`

Wokann日文（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nかいふくした！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_DEF_NAME_WITH_PREFIX} restored HP\nusing its {B_DEF_ABILITY}!`

当前美版（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n体力回复了！`

### 5589 — sText_PkmnChangedTypeWith

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_10}因{FD_19}\n变成了{FD_00}属性！`

文件：`patch/batches/191_battle_moves_abilities_results.json`。

原日文（`0x085AA611`）：

`{PLACEHOLDER_10}は　{PLACEHOLDER_19}で\n{PLACEHOLDER_00}タイプに　なった!`

Wokann日文（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\n{B_BUFF1}タイプに　なった！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_DEF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nmade it the {B_BUFF1} type!`

当前美版（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n变成了{B_BUFF1}属性！`

### 5590 — sText_PkmnPreventsParalysisWith

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_11}因{FD_19}\n不会麻痹！`

文件：`patch/batches/191_battle_moves_abilities_results.json`。

原日文（`0x085AA625`）：

`{PLACEHOLDER_11}は　{PLACEHOLDER_19}で\nまひしない!`

Wokann日文（`src/battle_message.c`）：

`{B_EFF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nまひしない！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_EFF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nprevents paralysis!`

当前美版（`src/battle_message.c`）：

`{B_EFF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会麻痹！`

### 5591 — sText_PkmnPreventsRomanceWith

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_10}因{FD_19}\n不会着迷！`

文件：`patch/batches/191_battle_moves_abilities_results.json`。

原日文（`0x085AA634`）：

`{PLACEHOLDER_10}は　{PLACEHOLDER_19}で\nメロメロに　ならない!`

Wokann日文（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nメロメロに　ならない！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_DEF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nprevents romance!`

当前美版（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会着迷！`

### 5592 — sText_PkmnPreventsPoisoningWith

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_11}因{FD_19}\n不会中毒！`

文件：`patch/batches/191_battle_moves_abilities_results.json`。

原日文（`0x085AA648`）：

`{PLACEHOLDER_11}は　{PLACEHOLDER_19}で\nどくを　うけない!`

Wokann日文（`src/battle_message.c`）：

`{B_EFF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nどくを　うけない！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_EFF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nprevents poisoning!`

当前美版（`src/battle_message.c`）：

`{B_EFF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会中毒！`

### 5593 — sText_PkmnPreventsConfusionWith

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_10}因{FD_19}\n不会混乱！`

文件：`patch/batches/191_battle_moves_abilities_results.json`。

原日文（`0x085AA65A`）：

`{PLACEHOLDER_10}は　{PLACEHOLDER_19}で\nこんらんしない!`

Wokann日文（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nこんらんしない！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_DEF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nprevents confusion!`

当前美版（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会混乱！`

### 5597 — sText_PkmnPreventsStatLossWith

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_13}因{FD_1A}\n能力不会降低！`

文件：`patch/batches/191_battle_moves_abilities_results.json`。

原日文（`0x085AA6B0`）：

`{PLACEHOLDER_13}は　{PLACEHOLDER_1A}で\nのうりょくが　さがらない!`

Wokann日文（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\nのうりょくが　さがらない！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\nprevents stat loss!`

当前美版（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n能力不会降低！`

### 5686 — sText_PkmnsXPreventsBurns

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_11}因{FD_1B}\n不会灼伤！`

文件：`patch/batches/193_battle_safari_item_effects.json`。

原日文（`0x085AA6ED`）：

`{PLACEHOLDER_11}は　{PLACEHOLDER_1B}で\nやけどしない!`

Wokann日文（`src/battle_message.c`）：

`{B_EFF_NAME_WITH_PREFIX}は　{B_EFF_ABILITY}で\nやけどしない！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_EFF_NAME_WITH_PREFIX}'s {B_EFF_ABILITY}\nprevents burns!`

当前美版（`src/battle_message.c`）：

`{B_EFF_NAME_WITH_PREFIX}因{B_EFF_ABILITY}\n不会灼伤！`

### 5687 — sText_PkmnsXBlocksY

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_10}的{FD_19}\n抵御了{FD_14}！`

文件：`patch/batches/193_battle_safari_item_effects.json`。

原日文（`0x085AA6FD`）：

`{PLACEHOLDER_10}は　{PLACEHOLDER_19}で\n{PLACEHOLDER_14}を　うけない!`

Wokann日文（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\n{B_CURRENT_MOVE}を　うけない！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_DEF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nblocks {B_CURRENT_MOVE}!`

当前美版（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}\n抵御了{B_CURRENT_MOVE}！`

### 5688 — sText_PkmnsXRestoredHPALittle2

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_0F}因{FD_18}\n回复了少许HP。`

文件：`patch/batches/193_battle_safari_item_effects.json`。

原日文（`0x085AA721`）：

`{PLACEHOLDER_0F}は　{PLACEHOLDER_18}で\nすこし　かいふく`

Wokann日文（`src/battle_message.c`）：

`{B_ATK_NAME_WITH_PREFIX}は　{B_ATK_ABILITY}で\nすこし　かいふく`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_ATK_NAME_WITH_PREFIX}'s {B_ATK_ABILITY}\nrestored its HP a little!`

当前美版（`src/battle_message.c`）：

`{B_ATK_NAME_WITH_PREFIX}因{B_ATK_ABILITY}\n回复了少许HP。`

### 5690 — sText_PkmnsXPreventsYLoss

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_13}因{FD_1A}\n{FD_00}不会降低！`

文件：`patch/batches/193_battle_safari_item_effects.json`。

原日文（`0x085AA75B`）：

`{PLACEHOLDER_13}は　{PLACEHOLDER_1A}で\n{PLACEHOLDER_00}が　さがらない!`

Wokann日文（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_BUFF1}が　さがらない！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\nprevents {B_BUFF1} loss!`

当前美版（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n{B_BUFF1}不会降低！`

### 5693 — sText_PkmnsXCuredYProblem

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_13}因{FD_1A}\n解除了{FD_00}状态！`

文件：`patch/batches/193_battle_safari_item_effects.json`。

原日文（`0x085AA797`）：

`{PLACEHOLDER_13}は　{PLACEHOLDER_1A}で\n{PLACEHOLDER_00}じょうたいが　なおった!`

Wokann日文（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_BUFF1}じょうたいが　なおった！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\ncured its {B_BUFF1} problem!`

当前美版（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n解除了{B_BUFF1}状态！`

### 5705 — sText_UsingItemTheStatOfPkmnRose

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 占位符严重错乱：JP「{SCR}は　{ITEM}で {STAT}が　{rose}」/EN 'Using {ITEM}, the {STAT} of {SCR} {rose}'；CHS'因为{ITEM}，{STAT}的{SCR}{rose}' 语序完全颠倒，不可读。

当前日版：

`{FD_13}使用{FD_16}，\n{FD_00}{FD_01}`

文件：`patch/batches/193_battle_safari_item_effects.json`。

原日文（`0x085AA89F`）：

`{PLACEHOLDER_13}は　{PLACEHOLDER_16}で\n{PLACEHOLDER_00}が　{PLACEHOLDER_01}`

Wokann日文（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_LAST_ITEM}で\n{B_BUFF1}が　{B_BUFF2}`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`Using {B_LAST_ITEM}, the {B_BUFF1}\nof {B_SCR_ACTIVE_NAME_WITH_PREFIX} {B_BUFF2}`

当前美版（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}使用{B_LAST_ITEM}，\n{B_BUFF1}{B_BUFF2}`

### 5709 — sText_EmptyString4

结论：**不需修复**。

原英文为空，原日文地址解码不能证明该共享空串应被填字。

方案：保留当前文本/布局。

原报告问题：

sText_EmptyString4 的 JP 引用地址处 ROM 解码为'は\n$'，疑似地址错位或占位文本，无法确认真实 JP 文本。

当前日版：

``

文件：`patch/batches/193_battle_safari_item_effects.json`。

原日文（`0x085A963E`）：

`は\n`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

``

当前美版（`src/battle_message.c`）：

``

### 5712 — sText_PkmnMakesGroundMiss

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_10}因{FD_19}\n不会被地面属性的招式击中！`

文件：`patch/batches/193_battle_safari_item_effects.json`。

原日文（`0x085A975F`）：

`{PLACEHOLDER_10}は　{PLACEHOLDER_19}で\nじめんタイプの　わざが　あたらない!`

Wokann日文（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nじめんタイプの　わざが　あたらない！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_DEF_NAME_WITH_PREFIX} makes GROUND\nmoves miss with {B_DEF_ABILITY}!`

当前美版（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会被地面属性的招式击中！`

### 5714 — sText_PkmnsXTookAttack

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_10}的{FD_19}\n吸引了攻击！`

文件：`patch/batches/193_battle_safari_item_effects.json`。

原日文（`0x085AA7CC`）：

`{PLACEHOLDER_10}は　{PLACEHOLDER_19}で\nこうげきを　うけた!`

Wokann日文（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nこうげきを　うけた！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_DEF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\ntook the attack!`

当前美版（`src/battle_message.c`）：

`{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}\n吸引了攻击！`

### 5727 — sText_PkmnsXPreventsFlinching

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_11}因{FD_1B}\n不会畏缩！`

文件：`patch/batches/194_battle_ability_link_facility.json`。

原日文（`0x085AA826`）：

`{PLACEHOLDER_11}は　{PLACEHOLDER_1B}で\nひるまない!`

Wokann日文（`src/battle_message.c`）：

`{B_EFF_NAME_WITH_PREFIX}は　{B_EFF_ABILITY}で\nひるまない！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_EFF_NAME_WITH_PREFIX}'s {B_EFF_ABILITY}\nprevents flinching!`

当前美版（`src/battle_message.c`）：

`{B_EFF_NAME_WITH_PREFIX}因{B_EFF_ABILITY}\n不会畏缩！`

### 5730 — sText_PkmnsXBlocksY2

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_13}的{FD_1A}\n抵御了{FD_14}！`

文件：`patch/batches/194_battle_ability_link_facility.json`。

原日文（`0x085AA70F`）：

`{PLACEHOLDER_13}は　{PLACEHOLDER_1A}で\n{PLACEHOLDER_14}を　うけない!`

Wokann日文（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_CURRENT_MOVE}を　うけない！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\nblocks {B_CURRENT_MOVE}!`

当前美版（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}的{B_SCR_ACTIVE_ABILITY}\n抵御了{B_CURRENT_MOVE}！`

### 5736 — sText_PkmnsXCuredItsYProblem

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

系统性结构错误：JP「{X}は　{Y}で…」/EN '{X}'s {Y}…'（X 的 Y 导致…），CHS 写成'因为{X}，{Y}…' 把 {Y}（特性）变成动作主体，语义荒谬。

当前日版：

`{FD_13}因{FD_1A}\n解除了{FD_00}状态！`

文件：`patch/batches/194_battle_ability_link_facility.json`。

原日文（`0x085AA84B`）：

`{PLACEHOLDER_13}は　{PLACEHOLDER_1A}で\n{PLACEHOLDER_00}が　なおった!`

Wokann日文（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_BUFF1}が　なおった！`

原英文（`src/battle_message.c`，`fe570a7e5^`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\ncured its {B_BUFF1} problem!`

当前美版（`src/battle_message.c`）：

`{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n解除了{B_BUFF1}状态！`

### 5762 — gText_PkmnsNickname

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

补丁把全角问号 ？(3D) 换成半角 ?(AC)：US-CHS'{STR_VAR_1}的昵称？'，补丁'{STR_VAR_1}的昵称?'。轻微。

当前日版：

`{FD_02}的昵称？`

文件：`patch/batches/195_naming_screen.json`。

原日文（`0x08565881`）：

`{PLACEHOLDER_02}　の　ニックネ-ムは?`

原英文（`src/strings.c`，`fe570a7e5^`）：

`{STR_VAR_1}'s nickname?`

当前美版（`src/strings.c`）：

`{STR_VAR_1}的昵称？`

### 5772 — EverGrandeCity_PokemonCenter_1F_Text_LeagueAfterVictoryRoad

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 末句改写：JP「まえに　すすむしかないわ！」/EN 'what choice do you have but to keep going?'（只能继续前进）；CHS'到底是什么让你坚持到现在？'（追问动机），意思改变。

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

### 5795 — SootopolisCity_PokemonCenter_1F_Text_AlwaysBeFriendsWithPokemon

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 弱化：JP「ポケモンと　ともだちで　いるわ」/EN 'I will always be friends with POKéMON'（做朋友）；CHS'我都会和宝可梦在一起'（在一起），'在一起'不等于'交朋友'。

当前日版：

`无论何时，无论何地，\n无论发生什么，\l我都会和宝可梦做朋友。\p和宝可梦交朋友是我的乐趣！`

文件：`patch/batches/196_pokemon_centers.json`。

原日文（`0x0820F117`）：

`どんな　ときでも\nどんな　ことが　あっても\lあたし　ポケモンと　ともだちで　いるわ\pだって　ポケモンと　いっしょだと\nすごく　たのしいもの!`

Wokann日文（`data/maps/SootopolisCity_PokemonCenter_1F/scripts.inc`）：

`どんな　ときでも\nどんな　ことが　あっても\lあたし　ポケモンと　ともだちで　いるわ\pだって　ポケモンと　いっしょだと\nすごく　たのしいもの！$`

原英文（`data/maps/SootopolisCity_PokemonCenter_1F/scripts.inc`，`fe570a7e5^`）：

`Whenever, wherever, and whatever\nhappens, I will always be friends with\lPOKéMON.\pBecause it's fun to be with POKéMON!$`

当前美版（`data/maps/SootopolisCity_PokemonCenter_1F/scripts.inc`）：

`无论何时，无论何地，\n无论发生什么，\l我都会和宝可梦做朋友。\p和宝可梦交朋友是我的乐趣！$`

### 5803 — gText_NoticesGoldCard

结论：**需修复**。

金卡、金色、四颗星已补回，但后半仍没有明确金卡，且遗漏原文两次玩家名；属于部分修复。

方案：保留已恢复的开头；后半改为“但拥有金卡的训练家，\l{PLAYER}您还是第一位！\p那么，请让我为{PLAYER}的\n宝可梦休息一下吧！”；日版用原 FD_01。

原报告问题：

CHS 漏译关键信息：JP「ゴールドカード」「きんいろ」「4つの　ほし」/EN 'GOLD CARD' 'gold color' 'four stars'；CHS 只写'那张卡''那个颜色''那星星的数量'，未点明金卡及四颗星。

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

### 5810 — gText_YouWantTheUsual

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 丢失 {PLAYER} 占位符：JP「{PLAYER}さん　おつかれさまです！」/EN 'I'm delighted to see you, {PLAYER}!'；CHS'辛苦了！要像往常一样吗？' 无玩家名。

当前日版：

`{FD_01}，辛苦了！\n要像往常一样吗？`

文件：`patch/batches/196_pokemon_centers.json`。

原日文（`0x082438B9`）：

`{PLACEHOLDER_01}さん　おつかれさまです!\nいつもので　よろしい　ですね!`

Wokann日文（`data/text/pkmn_center_nurse.inc`）：

`{PLAYER}さん　おつかれさまです！\nいつもので　よろしい　ですね！$`

原英文（`data/text/pkmn_center_nurse.inc`，`fe570a7e5^`）：

`I'm delighted to see you, {PLAYER}!\nYou want the usual, am I right?$`

当前美版（`data/text/pkmn_center_nurse.inc`）：

`{PLAYER}，辛苦了！\n要像往常一样吗？$`

### 5872 — gText_TuckerDefeatSilver

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 文本截断不完整：JP「なんて　こと」/EN 'What the…'；CHS'怎么回……' 缺字，应为'怎么回事'或'怎么会'。

当前日版：

`呃……\n怎么会……`

文件：`patch/batches/198_frontier_brain_quotes.json`。

原日文（`0x08276D8A`）：

`クッ……　なんて　こと……`

Wokann日文（`data/text/frontier_brain.inc`）：

`クッ⋯⋯　なんて　こと⋯⋯$`

原英文（`data/text/frontier_brain.inc`，`fe570a7e5^`）：

`Grr…\nWhat the…$`

当前美版（`data/text/frontier_brain.inc`）：

`呃……\n怎么会……$`

### 5913 — BattleFrontier_BattleArenaBattleRoom_Text_IsThatRight

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 改写：JP「ふーん…へーえ…」(沉吟)/EN 'Is that right? Hmm…'（是吗）；CHS'没有搞错吗？'（质疑出错），语气改变。

当前日版：

`是吗？哈……\n哈哈……`

文件：`patch/batches/199_battle_frontier_arena.json`。

原日文（`0x08230B88`）：

`ふ-ん……　へ-え……　へえぇぇ……`

Wokann日文（`data/maps/BattleFrontier_BattleArenaBattleRoom/scripts.inc`）：

`ふーん⋯⋯　へーえ⋯⋯　へえぇぇ⋯⋯$`

原英文（`data/maps/BattleFrontier_BattleArenaBattleRoom/scripts.inc`，`fe570a7e5^`）：

`Is that right? Hmm…\nHmhm…$`

当前美版（`data/maps/BattleFrontier_BattleArenaBattleRoom/scripts.inc`）：

`是吗？哈……\n哈哈……$`

### 5966 — BattleFrontier_BattleDomeBattleRoom_Text_WillTheyRaceToChampionship

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 改写设问：JP「いっきに　ゆうしょうまで のぼりつめて　しまうのでしょうか！？」/EN 'Will this TRAINER race to the championship?'（能否一举夺冠）；CHS'哪一位训练家进入冠军赛了呢？'（问是哪一位），意思改变。

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

### 5990 — BattleFrontier_BattleDomeBattleRoom_Text_CanWinStreakBeStretched

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 后句改写：JP「かんろく　じゅうぶん！」(信心满满)/EN 'The confidence is there!'；CHS'让我们期待比赛的结果吧！'，意思改变。

当前日版：

`我们的冠军还会继续称霸吗？\n真是信心十足！`

文件：`patch/batches/200_battle_frontier_battle_dome_battle_room.json`。

原日文（`0x08229A4A`）：

`どこまで　かちつづける　つもり　なのか?\nかんろく　じゅうぶん!`

Wokann日文（`data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc`）：

`どこまで　かちつづける　つもり　なのか？\nかんろく　じゅうぶん！$`

原英文（`data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc`，`fe570a7e5^`）：

`Can the win streak be stretched?\nThe confidence is there!$`

当前美版（`data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc`）：

`我们的冠军还会继续称霸吗？\n真是信心十足！$`

### 6024 — BattleFrontier_BattleDomeLobby_Text_TrashedInFirstRound

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 改写：JP「ボコボコに　やられた」(被痛打)/EN 'I got trashed'；CHS'输掉也是预料之中'（预料之中），意思改变。

当前日版：

`比赛的第一场我就碰上了\n一个夺冠热门的选手。\p被打得落花流水……`

文件：`patch/batches/201_battle_frontier_battle_dome_lobby.json`。

原日文（`0x08227C4A`）：

`1かいせんで　いきなり\nゆうしょうこうほと　あたっちゃって\lもう　ボコボコに　やられたよ……`

Wokann日文（`data/maps/BattleFrontier_BattleDomeLobby/scripts.inc`）：

`1かいせんで　いきなり\nゆうしょうこうほと　あたっちゃって\lもう　ボコボコに　やられたよ⋯⋯$`

原英文（`data/maps/BattleFrontier_BattleDomeLobby/scripts.inc`，`fe570a7e5^`）：

`I ran into one of the tournament\nfavorites in the very first round.\pOf course I got trashed…$`

当前美版（`data/maps/BattleFrontier_BattleDomeLobby/scripts.inc`）：

`比赛的第一场我就碰上了\n一个夺冠热门的选手。\p被打得落花流水……$`

### 6092 — BattleFrontier_BattleFactoryLobby_Text_CantFigureOutStaffHints

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS 误译：JP「いい　おとな」/EN 'full-grown man'（成年人）；CHS'经验丰富的人'（有经验者），词义改变。

当前日版：

`你知道这的工作人员会给你\n一些关于你下个对手的提示吧？\p好吧，虽然我是一个成年人，\n但我弄不懂他们的提示。`

文件：`patch/batches/204_battle_frontier_battle_factory_lobby.json`。

原日文（`0x0823198B`）：

`ここの　スタッフさぁ　たたかいの　まえに\nつぎに　たたかう　トレ-ナ-のこと\lちょっとだけ　おしえて　くれるだろ-?\pでも　オレ　いい　おとな　なのに\nあいつらの　せつめいの　いみが\lぜんぜん　わからないんだ　よう`

Wokann日文（`data/maps/BattleFrontier_BattleFactoryLobby/scripts.inc`）：

`ここの　スタッフさぁ　たたかいの　まえに\nつぎに　たたかう　トレーナーのこと\lちょっとだけ　おしえて　くれるだろー？\pでも　オレ　いい　おとな　なのに\nあいつらの　せつめいの　いみが\lぜんぜん　わからないんだ　よう$`

原英文（`data/maps/BattleFrontier_BattleFactoryLobby/scripts.inc`，`fe570a7e5^`）：

`You know how the staff here give you\na few hints about your next opponent?\pWell, I'm a full-grown man, but I have\ntrouble figuring out their hints.$`

当前美版（`data/maps/BattleFrontier_BattleFactoryLobby/scripts.inc`）：

`你知道这的工作人员会给你\n一些关于你下个对手的提示吧？\p好吧，虽然我是一个成年人，\n但我弄不懂他们的提示。$`

### 6256 — BattleFrontier_BattlePikeRoomNormal_Text_AttacksWhenStartled

结论：**需修复**。

突然看见人受惊后扑过来，不是“不听指挥”。原文不存在“命令を無視して”。

方案：突然看见人时会受惊，\n然后扑过来攻击……\p您和您的宝可梦还好吗？

原报告问题：

JP「きゅうに ひとを みると おどろいて おそいかかって しまうのだ」(突然看到人、受惊后发起攻击)/EN "attacks without warning"(攻击出其不意)被译为"无视警告胡乱攻击"；"without warning"(没有预警)≠"无视警告"(无视警告)，语义改变

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

### 6295 — BattleFrontier_BattlePikeThreePathRoom_Text_AromaOfPokemon

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「ポケモンの においが ただよってくるような きがする」(感觉有宝可梦的气味飘来)/EN "distinct aroma of POKéMON wafting"被译为"似乎有宝可梦在里面"；"气味飘来"被改为"宝可梦在里面"，语义改变

当前日版：

`似乎有宝可梦的气味飘来……`

文件：`patch/batches/213_battle_frontier_battle_pike_three_path_room.json`。

原日文（`0x082342AE`）：

`ポケモンの　においが\nただよってくる　ような\lきが　するの　ですが……`

Wokann日文（`data/maps/BattleFrontier_BattlePikeThreePathRoom/scripts.inc`）：

`ポケモンの　においが\nただよってくる　ような\lきが　するの　ですが⋯⋯$`

原英文（`data/maps/BattleFrontier_BattlePikeThreePathRoom/scripts.inc`，`fe570a7e5^`）：

`It seems to have the distinct aroma\nof POKéMON wafting around it…$`

当前美版（`data/maps/BattleFrontier_BattlePikeThreePathRoom/scripts.inc`）：

`似乎有宝可梦的气味飘来……$`

### 6327 — BattleFrontier_BattlePyramidLobby_Text_HintBurn

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「まっかな ほのお」(赤红的/深红的火焰)/EN "bright red flames"被译为"闪亮的火焰"；颜色(红)被改为"闪亮"，语义改变

当前日版：

`我看到了赤红的火焰……\p……你的宝可梦\n正在被烧灼着……`

文件：`patch/batches/214_battle_frontier_battle_pyramid_lobby.json`。

原日文（`0x0822CD0D`）：

`まっかな　ほのおが　みえます……\p……そして\nやけどを　おって　くるしむ\lあなたの　ポケモンの　すがたも……`

Wokann日文（`data/maps/BattleFrontier_BattlePyramidLobby/scripts.inc`）：

`まっかな　ほのおが　みえます⋯⋯\p⋯⋯そして\nやけどを　おって　くるしむ\lあなたの　ポケモンの　すがたも⋯⋯$`

原英文（`data/maps/BattleFrontier_BattlePyramidLobby/scripts.inc`，`fe570a7e5^`）：

`I see bright red flames…\p…And, I see your POKéMON suffering\nfrom burns…$`

当前美版（`data/maps/BattleFrontier_BattlePyramidLobby/scripts.inc`）：

`我看到了赤红的火焰……\p……你的宝可梦\n正在被烧灼着……$`

### 6407 — BattleFrontier_BattleTowerLobby_Text_AboutToFace50thTrainer

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「リボン」/EN "RIBBON"(ribbon,官方中文"缎带")被译为"奖章"(medal)；"缎带"≠"奖章"，术语错误

当前日版：

`下面您即将迎战的是\n第50位训练家了，\p现在起，您每次连续打败7位训练家，\n我们将会把缎带送给您参战的宝可梦。\p祝您好运！`

文件：`patch/batches/217_battle_frontier_battle_tower_lobby.json`。

原日文（`0x082206DE`）：

`いよいよ　つぎは　50にんめの\nトレ-ナ-　ですね!\pこれからは　7にんを　かちぬく　たびに\nあなたの　ポケモンに　きねんリボンが\lおくられますので　がんばって　くださいね!`

Wokann日文（`data/maps/BattleFrontier_BattleTowerLobby/scripts.inc`）：

`いよいよ　つぎは　50にんめの\nトレーナー　ですね！\pこれからは　7にんを　かちぬく　たびに\nあなたの　ポケモンに　きねんリボンが\lおくられますので　がんばって　くださいね！$`

原英文（`data/maps/BattleFrontier_BattleTowerLobby/scripts.inc`，`fe570a7e5^`）：

`You're finally about to face the\n50th TRAINER.\pFrom here on, every time you beat seven\nTRAINERS in a row, your POKéMON will\lreceive a commemorative RIBBON.\pGood luck!$`

当前美版（`data/maps/BattleFrontier_BattleTowerLobby/scripts.inc`）：

`下面您即将迎战的是\n第50位训练家了，\p现在起，您每次连续打败7位训练家，\n我们将会把缎带送给您参战的宝可梦。\p祝您好运！$`

### 6408 — BattleFrontier_BattleTowerLobby_Text_HereAreSomeRibbons

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「リボン」/EN "RIBBON"(ribbon,官方中文"缎带")被译为"奖章"(medal)；"缎带"≠"奖章"，术语错误

当前日版：

`这是连续打败7位\n强大的训练家的奖励。\p{FD_01}得到缎带！`

文件：`patch/batches/217_battle_frontier_battle_tower_lobby.json`。

原日文（`0x08220736`）：

`つよい　トレ-ナ-　7にんを\nかちぬいた　きねんの　リボンを　どうぞ!\p{PLACEHOLDER_01}は　リボンを　もらった!`

Wokann日文（`data/maps/BattleFrontier_BattleTowerLobby/scripts.inc`）：

`つよい　トレーナー　7にんを\nかちぬいた　きねんの　リボンを　どうぞ！\p{PLAYER}は　リボンを　もらった！$`

原英文（`data/maps/BattleFrontier_BattleTowerLobby/scripts.inc`，`fe570a7e5^`）：

`Here are some RIBBONS for beating\nseven tough TRAINERS in a row.\p{PLAYER} received some RIBBONS!$`

当前美版（`data/maps/BattleFrontier_BattleTowerLobby/scripts.inc`）：

`这是连续打败7位\n强大的训练家的奖励。\p{PLAYER}得到缎带！$`

### 6409 — BattleFrontier_BattleTowerLobby_Text_PutRibbonOnMons

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「リボン」/EN "RIBBON"(ribbon,官方中文"缎带")被译为"奖章"(medal)；"缎带"≠"奖章"，术语错误

当前日版：

`{FD_01}给挑战的宝可梦\n戴上了缎带。`

文件：`patch/batches/217_battle_frontier_battle_tower_lobby.json`。

原日文（`0x08220769`）：

`{PLACEHOLDER_01}は　ポケモンに\nリボンを　つけて　あげた!`

Wokann日文（`data/maps/BattleFrontier_BattleTowerLobby/scripts.inc`）：

`{PLAYER}は　ポケモンに\nリボンを　つけて　あげた！$`

原英文（`data/maps/BattleFrontier_BattleTowerLobby/scripts.inc`，`fe570a7e5^`）：

`{PLAYER} put the RIBBONS on\nthe challenger POKéMON.$`

当前美版（`data/maps/BattleFrontier_BattleTowerLobby/scripts.inc`）：

`{PLAYER}给挑战的宝可梦\n戴上了缎带。$`

### 6437 — BattleFrontier_BattleTowerLobby_Text_ExplainLinkMultisChallenge

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「ちがうしゅるいの ポケモンを 2ひきずつ もちより」(每人携带2只不同种类的宝可梦)/EN "enter two different kinds of POKéMON"中的"不同种类"条件，在CHS"携带2只宝可梦和朋友组队进行挑战"中被省略

当前日版：

`对战塔的多人对战间\n是和朋友一起进行\l多人对战的设施。\p您需要先使用无线适配器\n或GBA连接线与朋友连接，\p每人携带2只不同种类的\n宝可梦，和朋友组队挑战。\p对战塔内有很多\n多人对战间，\p供团队对战使用。\n在多人对战间中，\l会有7组训练家等待\p您和您朋友的组队挑战。\n如果顺利战胜7组，\p我们会向您呈上对战点数。\n请注意这里与其他房间不同，\p您不能暂停挑战。一旦挑战开始，\n就需要不间断地进行7次多人对战。`

文件：`patch/batches/217_battle_frontier_battle_tower_lobby.json`。

原日文（`0x08221540`）：

`つうしんマルチ　バトルル-ムは\nワイヤレスアダプタや　つうしんケ-ブルを\lつないだ　ともだちと　ふたりで\lちがう　しゅるいの　ポケモンを\l2ひきずつ　もちより\lマルチバトルで　たたかう　しせつです!\pタワ-ないには　マルチ　バトルル-ムという\nたいせんの　ための　へやが\lたくさん　ようい　されています!\pそれぞれ　マルチ　バトルル-ムには\n7くみの　タッグ　トレ-ナ-が　いて\lあなたと　ともだちの　タッグでの\lチャレンジを　まっています!\pみごと　その　7くみを　たおせたら\nバトルポイントを　しんてい　いたします!\pまた　ほかの　しせつと　ちがって\nここでは　とちゅうで　ちょうせんを\lちゅうだん　できません!\p7かい　れんぞくで　たたかうことに　なるので\nじゅうぶん　ちゅうい　してください!`

Wokann日文（`data/maps/BattleFrontier_BattleTowerLobby/scripts.inc`）：

`つうしんマルチ　バトルルームは\nワイヤレスアダプタや　つうしんケーブルを\lつないだ　ともだちと　ふたりで\lちがう　しゅるいの　ポケモンを\l2ひきずつ　もちより\lマルチバトルで　たたかう　しせつです！\pタワーないには　マルチ　バトルルームという\nたいせんの　ための　へやが\lたくさん　ようい　されています！\pそれぞれ　マルチ　バトルルームには\n7くみの　タッグ　トレーナーが　いて\lあなたと　ともだちの　タッグでの\lチャレンジを　まっています！\pみごと　その　7くみを　たおせたら\nバトルポイントを　しんてい　いたします！\pまた　ほかの　しせつと　ちがって\nここでは　とちゅうで　ちょうせんを\lちゅうだん　できません！\p7かい　れんぞくで　たたかうことに　なるので\nじゅうぶん　ちゅうい　してください！$`

原英文（`data/maps/BattleFrontier_BattleTowerLobby/scripts.inc`，`fe570a7e5^`）：

`The BATTLE TOWER's MULTI BATTLE\nROOMS are facilities for conducting\lMULTI BATTLES with a friend.\pYou must link with your friend using\nWireless Adapters or a Game Boy\lAdvance Game Link cable.\pYou must partner with your friend and\nenter two different kinds of POKéMON.\pThere are many MULTI BATTLE ROOMS\nin the BATTLE TOWER for team battles.\pIn a MULTI BATTLE ROOM, seven\ntag teams await you and your friend\lto make a tag-team challenge.\pIf you manage to defeat all seven\nteams, you will earn Battle Points.\pPlease beware that unlike other ROOMS,\nyou may not interrupt your challenge.\pOnce you start, you must battle seven\nMULTI BATTLES in a row nonstop.$`

当前美版（`data/maps/BattleFrontier_BattleTowerLobby/scripts.inc`）：

`对战塔的多人对战间\n是和朋友一起进行\l多人对战的设施。\p您需要先使用无线适配器\n或GBA连接线与朋友连接，\p每人携带2只不同种类的\n宝可梦，和朋友组队挑战。\p对战塔内有很多\n多人对战间，\p供团队对战使用。\n在多人对战间中，\l会有7组训练家等待\p您和您朋友的组队挑战。\n如果顺利战胜7组，\p我们会向您呈上对战点数。\n请注意这里与其他房间不同，\p您不能暂停挑战。一旦挑战开始，\n就需要不间断地进行7次多人对战。$`

### 6493 — BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice10Reject

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「{PLAYER}さんってのは クールだね」(你真冷酷/冷淡)/EN "You're a calculating one"被译为"你真是个斤斤计较的家伙"；"冷酷"→"斤斤计较(吝啬计较)"，语义改变

当前日版：

`切！\n你真是个冷酷的家伙，{FD_01}！`

文件：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`。

原日文（`0x0822415B`）：

`ぐわ-っ!\n{PLACEHOLDER_01}さん　ってのは　ク-ルだね!`

Wokann日文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`ぐわーっ！\n{PLAYER}さん　ってのは　クールだね！$`

原英文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`，`fe570a7e5^`）：

`Gwaaah!\nYou're a calculating one, {PLAYER}!$`

当前美版（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`切！\n你真是个冷酷的家伙，{PLAYER}！$`

### 6553 — BattleFrontier_BattleTowerMultiPartnerRoom_Text_ExpertFReject

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「つぎに あったときには タッグを くみたいものですね」(下次见面时希望能组队)/EN "Perhaps we can form a team the next time we meet"被译为"希望在我们下一次见面的时候你会回心转意"；"回心转意"(改变主意)为原文没有的附加含义

当前日版：

`希望在我们下一次见面的时候\n能和你组队。`

文件：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`。

原日文（`0x08225579`）：

`つぎに　あったときには\nタッグを　くみたいものですね……`

Wokann日文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`つぎに　あったときには\nタッグを　くみたいものですね⋯⋯$`

原英文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`，`fe570a7e5^`）：

`Perhaps we can form a team the next\ntime we meet.$`

当前美版（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`希望在我们下一次见面的时候\n能和你组队。$`

### 6564 — BattleFrontier_BattleTowerMultiPartnerRoom_Text_SailorAccept

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「とうぜんだよな」(理所当然/我早就料到)/EN "I didn't expect any less!"被译为"这简直太出乎我的意料了"；"理所当然"被反转为"出乎意料"，语义完全相反

当前日版：

`我就知道你会答应！\n我现在就去登记。`

文件：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`。

原日文（`0x082258B4`）：

`とうぜん　だよな!\nいまから　とうろく　してくるぜ!`

Wokann日文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`とうぜん　だよな！\nいまから　とうろく　してくるぜ！$`

原英文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`，`fe570a7e5^`）：

`I didn't expect any less!\nI'll go register now.$`

当前美版（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`我就知道你会答应！\n我现在就去登记。$`

### 6622 — BattleFrontier_BattleTowerMultiPartnerRoom_Text_LassIntro

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「ミニスカート」(训练家职业)/EN "LASS"被译为"一个迷你裙"；"迷你裙"是服装，不能指代人物(对比5373短裤小子/5376登山男/5385千金小姐均译为人物)

当前日版：

`我是短裙少女{FD_02}！`

文件：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`。

原日文（`0x0822477D`）：

`わたし\nミニスカ-ト　{PLACEHOLDER_02}!`

Wokann日文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`わたし\nミニスカート　{STR_VAR_1}！$`

原英文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`，`fe570a7e5^`）：

`I'm {STR_VAR_1}, and I'm a LASS!$`

当前美版（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`我是短裙少女{STR_VAR_1}！$`

### 6660 — BattleFrontier_BattleTowerMultiPartnerRoom_Text_HexManiacMon2Ask

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「どうか わたくしと タッグを くんでいただけませんか？」(拜托了，能和我组队吗？)/EN "I beseech you… Join me in a tag team…"被译为"我看好你……我们组队……"；"我看好你"(看好玩家)为原文没有的含义，原意是谦卑请求，人物语气被改变

当前日版：

`使用{FD_02}的{FD_03}……\p拜托你……\n和我组队吧……`

文件：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`。

原日文（`0x08224EA1`）：

`{PLACEHOLDER_02}を　もつ　{PLACEHOLDER_03}を\nもっております……\pどうか　わたくしと\nタッグを　くんでいただけませんか?`

Wokann日文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`{STR_VAR_1}を　もつ　{STR_VAR_2}を\nもっております⋯⋯\pどうか　わたくしと\nタッグを　くんでいただけませんか？$`

原英文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`，`fe570a7e5^`）：

`{STR_VAR_1}-using {STR_VAR_2}…\pI beseech you…\nJoin me in a tag team…$`

当前美版（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`使用{STR_VAR_1}的{STR_VAR_2}……\p拜托你……\n和我组队吧……$`

### 6692 — BattleFrontier_BattleTowerMultiPartnerRoom_Text_ExpertFMon1

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「わたしの きたえあげた ポケモン」(我训练的宝可梦)/EN "I've raised my POKéMON thoroughly"被译为"我十分的热爱宝可梦"；"训练"(きたえる)→"热爱"，动词完全错误

当前日版：

`我精心培育了宝可梦。\n一只掌握{FD_02}的{FD_03}和`

文件：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`。

原日文（`0x08225515`）：

`わたしの　きたえあげた　ポケモンは\n{PLACEHOLDER_02}を　つかう　{PLACEHOLDER_03}と……`

Wokann日文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`わたしの　きたえあげた　ポケモンは\n{STR_VAR_1}を　つかう　{STR_VAR_2}と⋯⋯$`

原英文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`，`fe570a7e5^`）：

`I've raised my POKéMON thoroughly.\nOne {STR_VAR_2} with {STR_VAR_1} and$`

当前美版（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`我精心培育了宝可梦。\n一只掌握{STR_VAR_1}的{STR_VAR_2}和$`

### 6717 — BattleFrontier_BattleTowerMultiPartnerRoom_Text_PkmnRangerMMon2Ask

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS"你不认为我们我们能构成一支令人印象深刻的队伍吗？"中"我们"重复(我们我们)，明显笔误；JP/EN无此重复

当前日版：

`一只掌握{FD_02}的{FD_03}！\p你不认为我们能构成\n一支令人印象深刻的队伍吗？`

文件：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`。

原日文（`0x082259B5`）：

`{PLACEHOLDER_02}を　つかう　{PLACEHOLDER_03}だ!\pどうだい?\nぼくと　タッグを　くんでみない?`

Wokann日文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`{STR_VAR_1}を　つかう　{STR_VAR_2}だ！\pどうだい？\nぼくと　タッグを　くんでみない？$`

原英文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`，`fe570a7e5^`）：

`one {STR_VAR_2} with {STR_VAR_1}!\pDon't you think we'd make an impressive\ntag team?$`

当前美版（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`一只掌握{STR_VAR_1}的{STR_VAR_2}！\p你不认为我们能构成\n一支令人印象深刻的队伍吗？$`

### 6723 — BattleFrontier_BattleTowerMultiPartnerRoom_Text_AromaLadyMon2Ask

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「{STR_VAR_1}を つかう {STR_VAR_2}です」/EN "one {STR_VAR_2} that uses {STR_VAR_1}."被译为"一只学会{STR_VAR_1}的{STR_VAR_2}
到处旅行。"；"到处旅行"为原文没有的赘余谓语(疑似从Mon1的"つれている"误植)

当前日版：

`一只学会{FD_02}的{FD_03}。\p希望你会喜欢它们。\n你想成为我的搭档吗？`

文件：`patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json`。

原日文（`0x08225AD5`）：

`{PLACEHOLDER_02}を　つかう　{PLACEHOLDER_03}です\pどうでしょう?\nわたくしと　タッグを　くんでみませんか?`

Wokann日文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`{STR_VAR_1}を　つかう　{STR_VAR_2}です\pどうでしょう？\nわたくしと　タッグを　くんでみませんか？$`

原英文（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`，`fe570a7e5^`）：

`one {STR_VAR_2} that uses\n{STR_VAR_1}.\pI hope they strike your fancy.\nWould you care to be my partner?$`

当前美版（`data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc`）：

`一只学会{STR_VAR_1}的{STR_VAR_2}。\p希望你会喜欢它们。\n你想成为我的搭档吗？$`

### 6891 — BattleFrontier_Lounge7_Text_RockSlideDesc

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「てきを ひるませることがある」(使对手畏缩/flinch)/EN "May cause flinching."被译为"可以使对手恐惧"；"畏缩"(flinch，官方术语)≠"恐惧"(fear)，术语错误

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

### 6916 — BattleFrontier_OutsideEast_Text_RankingHallSign

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「きざめ！ さいこうの きろく！」(铭刻吧！最高的纪录！)/EN "Set your sights on new records!"被译为"关注最新的纪录！"；"铭刻/创造纪录"被改为"关注纪录"，动词语义改变

当前日版：

`对战开拓区排名大厅\n向新纪录发起挑战！`

文件：`patch/batches/227_battle_frontier_outside_east.json`。

原日文（`0x08222C23`）：

`バトルフロンティア　ランキングホ-ル\nきざめ!　さいこうの　きろく!`

Wokann日文（`data/maps/BattleFrontier_OutsideEast/scripts.inc`）：

`バトルフロンティア　ランキングホール\nきざめ！　さいこうの　きろく！$`

原英文（`data/maps/BattleFrontier_OutsideEast/scripts.inc`，`fe570a7e5^`）：

`BATTLE FRONTIER RANKING HALL\nSet your sights on new records!$`

当前美版（`data/maps/BattleFrontier_OutsideEast/scripts.inc`）：

`对战开拓区排名大厅\n向新纪录发起挑战！$`

### 6921 — BattleFrontier_OutsideEast_Text_ThriveInDarkness

结论：**需修复**。

第一句已修好；结尾仍将邀请一起探索变成问对方是否绝望。日文没有英文的 total desperation，不强行统一区域差异。

方案：日版结尾：你也要不要在黑暗中\n拼命探索一番……？；美版结尾：你也要不要在黑暗与\n彻底的绝望中探索一番？

原报告问题：

JP「くらやみが だいすきな わたし」(热爱黑暗的我)/EN "I thrive in darkness"被译为"我是在黑暗中长大的"；"热爱"(だいすき)→"长大"，动词完全错误

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

### 6933 — BattleFrontier_OutsideEast_Text_LegendOfBattlePyramid

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「おとこのなかのおとこ あらわれる」(将出现一位真正的男子汉)/EN "there shall appear a man among men."被译为"就会有一个人出现在人群中"；"真正的男子汉"被改为"人群中的一个人"，习语被误译

当前日版：

`你听说过那个关于\n对战金字塔的传说吗？\p当一位勇敢的训练家到达\n金光闪闪的顶峰之时，\l就会有一位真正的男子汉出现。\p你知道这个传说吗？\n哈哈，你当然不知道！\l这是我刚刚编的！\p至于这是什么意思，\n那是，呃，不告诉你！`

文件：`patch/batches/227_battle_frontier_outside_east.json`。

原日文（`0x08223080`）：

`きみは　しって　いるか!?\nバトルピラミッドの　でんせつを!!\pみなぎる　ゆうきを　もつ　トレ-ナ-\nきんじとうの　いただきを　めざすとき\lおとこの　なかの　おとこ　あらわれる\p……どうだ?　しらないだろ-!\nだって　これ　さっき　おれが\lかんがえたんだ　もんな!\pなに?　どういう　いみ　かって?\nチッチッ!!　それは　おしえられないな!`

Wokann日文（`data/maps/BattleFrontier_OutsideEast/scripts.inc`）：

`きみは　しって　いるか！？\nバトルピラミッドの　でんせつを！！\pみなぎる　ゆうきを　もつ　トレーナー\nきんじとうの　いただきを　めざすとき\lおとこの　なかの　おとこ　あらわれる\p⋯⋯どうだ？　しらないだろー！\nだって　これ　さっき　おれが\lかんがえたんだ　もんな！\pなに？　どういう　いみ　かって？\nチッチッ！！　それは　おしえられないな！$`

原英文（`data/maps/BattleFrontier_OutsideEast/scripts.inc`，`fe570a7e5^`）：

`Do you know it?\nThe legend of the BATTLE PYRAMID?\pWhen there comes a confident TRAINER\nreaching for the golden pinnacle,\lthere shall appear a man among men.\pDon't know that legend?\nWell, of course not!\lI just made it up!\pWhat's it supposed to mean?\nThat, my friend, I can't say!$`

当前美版（`data/maps/BattleFrontier_OutsideEast/scripts.inc`）：

`你听说过那个关于\n对战金字塔的传说吗？\p当一位勇敢的训练家到达\n金光闪闪的顶峰之时，\l就会有一位真正的男子汉出现。\p你知道这个传说吗？\n哈哈，你当然不知道！\l这是我刚刚编的！\p至于这是什么意思，\n那是，呃，不告诉你！$`

### 6943 — BattleFrontier_OutsideEast_Text_StickyMonWithLongTail

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「しっぽが ながくって なんか ベタベタした ポケモン」(长着长尾巴、黏糊糊的宝可梦)/EN "a sticky sort of a POKéMON with a long tail"被译为"举着长长尾巴的小小的宝可梦"；关键特征"黏糊糊"(ベタベタ)被省略，另添加了原文没有的"举着""小小的"

当前日版：

`我……\n我看见了！\p是一只长着长长尾巴的\n黏糊糊的宝可梦！\p刚才它藏在一块大石头底下，\n还一直偷偷地盯着我看！`

文件：`patch/batches/227_battle_frontier_outside_east.json`。

原日文（`0x08223411`）：

`ぼぼぼ　ぼく　みちゃったんだっ!!\pこのさきの　いわ　から　しっぽが　ながくって\nなんか　ベタベタした　ポケモンが\lぼくの　こと　じ-っと　のぞいてたんだっ!\pきっと　こわい　ポケモン　だよ-っ!!`

Wokann日文（`data/maps/BattleFrontier_OutsideEast/scripts.inc`）：

`ぼぼぼ　ぼく　みちゃったんだっ！！\pこのさきの　いわ　から　しっぽが　ながくって\nなんか　ベタベタした　ポケモンが\lぼくの　こと　じーっと　のぞいてたんだっ！\pきっと　こわい　ポケモン　だよーっ！！$`

原英文（`data/maps/BattleFrontier_OutsideEast/scripts.inc`，`fe570a7e5^`）：

`I…\nI saw it!\pThere was a sticky sort of a POKéMON\nwith a long tail up ahead!\pIt was hiding under a boulder, and\nit kept staring at me!$`

当前美版（`data/maps/BattleFrontier_OutsideEast/scripts.inc`）：

`我……\n我看见了！\p是一只长着长长尾巴的\n黏糊糊的宝可梦！\p刚才它藏在一块大石头底下，\n还一直偷偷地盯着我看！$`

### 7008 — BattleFrontier_ReceptionGate_Text_Level50Info

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「レベル50より ひくい レベルの ポケモン」(低于50级的宝可梦)/EN "any POKéMON below Level 50"被译为"等级50以内的宝可梦"；"よりひくい"(低于，<50)≠"以内"(≤50)，"以内"包含了50级，与原文(对手为50级、只是不低于50级)矛盾

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

### 7009 — BattleFrontier_ReceptionGate_Text_OpenLevelInfo

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「レベル60より ひくい レベルの ポケモン」(低于60级的宝可梦)/EN "any POKéMON below Level 60"被译为"等级60以内的宝可梦"；"よりひくい"(<60)≠"以内"(≤60)，语义错误

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

### 7069 — FortreeCity_House3_Text_MetStevenHadAmazingPokemon

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「めずらしい だけでなく」(不只是稀有)/EN "They weren't just rare"被译为"不止是强大"；"稀有"(めずらしい)→"强大"，名词完全错误(大吾的宝可梦特点是稀有)

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

### 7096 — LilycoveCity_MoveDeletersHouse_Text_ICanMakeMonForgetMove

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「えーと⋯⋯ そうじゃ わし わすれじいさん」(那个……对了，我是遗忘爷爷)/EN "Uh… Oh, yes, I'm the MOVE DELETER."被译为"那个……俺是谁来着？\p…… …… ……\n…… …… ……\p哦哦，对了！俺是遗忘爷爷哩！"；"俺是谁来着"整段健忘笑话为原文没有的虚构添加

当前日版：

`那个……\n哦，对了！俺是遗忘爷爷哩！\p俺能让宝可梦\n忘记招式。\p你想让俺帮忙吗？`

文件：`patch/batches/259_lilycove_city_move_deleters_house.json`。

原日文（`0x08209E63`）：

`え-と……\nそうじゃ　わし　わすれじいさん\pポケモンの　わざを\nわすれさせる　ことが　できるんじゃ!\pわざを　わすれ　させるかね?`

Wokann日文（`data/maps/LilycoveCity_MoveDeletersHouse/scripts.inc`）：

`えーと⋯⋯\nそうじゃ　わし　わすれじいさん\pポケモンの　わざを\nわすれさせる　ことが　できるんじゃ！\pわざを　わすれ　させるかね？$`

原英文（`data/maps/LilycoveCity_MoveDeletersHouse/scripts.inc`，`fe570a7e5^`）：

`Uh…\nOh, yes, I'm the MOVE DELETER.\pI can make POKéMON forget their moves.\pWould you like me to do that?$`

当前美版（`data/maps/LilycoveCity_MoveDeletersHouse/scripts.inc`）：

`那个……\n哦，对了！俺是遗忘爷爷哩！\p俺能让宝可梦\n忘记招式。\p你想让俺帮忙吗？$`

### 7183 — RustboroCity_House3_Text_NamingPikachuPekachu

结论：**需修复**。

PEKACHU/ペカチュウ是 PIKACHU/ピカチュウ的轻微改名；“猫卡球”丢失这一笑点。只改对话文本，不改保存的昵称。

方案：但给皮卡丘起名叫\n“佩卡丘”，几乎没什么区别吧……\p我想最好起个容易\n让人理解的名字，但是……；美版第二分句可保留“这没什么意义”。

原报告问题：

JP「ピカチュウに ‘ペカチュウ’ってつけても」(给皮卡丘起名叫"佩卡丘")/EN "giving the name PEKACHU to a PIKACHU"被译为"叫皮卡丘为猫卡球"；昵称ペカチュウ(对皮卡丘的微小改动)被误译为"猫卡球"，完全丢失了原文的文字游戏

当前日版：

`但叫皮卡丘为\n猫卡球？这没什么意义。\p我想最好起个容易\n让人理解的名字，但是……`

文件：`patch/batches/299_rustboro_city_house3.json`。

原日文（`0x0820416F`）：

`だからって　ピカチュウに\n‘ペカチュウ’って　つけても\lほとんど　かわって　ないでしょうに……\pまあ　わかりやすいのも\nニックネ-ムには　だいじ　ですけどねぇ`

Wokann日文（`data/maps/RustboroCity_House3/scripts.inc`）：

`だからって　ピカチュウに\n‘ペカチュウ’って　つけても\lほとんど　かわって　ないでしょうに⋯⋯\pまあ　わかりやすいのも\nニックネームには　だいじ　ですけどねぇ$`

原英文（`data/maps/RustboroCity_House3/scripts.inc`，`fe570a7e5^`）：

`But giving the name PEKACHU to\na PIKACHU? It seems pointless.\pI suppose it is good to use a name\nthat's easy to understand, but…$`

当前美版（`data/maps/RustboroCity_House3/scripts.inc`）：

`但叫皮卡丘为\n猫卡球？这没什么意义。\p我想最好起个容易\n让人理解的名字，但是……$`

### 7184 — RustboroCity_House3_Text_Pekachu

结论：**需修复**。

承接上一条的同一昵称与叫声，需一并统一。只改对话资源。

方案：佩卡丘：佩卡！

原报告问题：

JP「ペカチュウ“ぺかー！」/EN "PEKACHU: Peka!"被译为"猫卡球：猫球！"；名字与叫声均承接5931的误译(ペカチュウ→猫卡球，ぺかー→猫球)

当前日版：

`猫卡球：猫球！`

文件：`patch/batches/299_rustboro_city_house3.json`。

原日文（`0x082041BF`）：

`ペカチュウ“ぺか-!`

Wokann日文（`data/maps/RustboroCity_House3/scripts.inc`）：

`ペカチュウ“ぺかー！$`

原英文（`data/maps/RustboroCity_House3/scripts.inc`，`fe570a7e5^`）：

`PEKACHU: Peka!$`

当前美版（`data/maps/RustboroCity_House3/scripts.inc`）：

`猫卡球：猫球！$`

### 7288 — SootopolisCity_Text_WonderWhatWorldIsLike

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS'不知这圆椭的天空的另一端'中'圆椭'为'椭圆'的字序颠倒，不成词；JP「まあるい そら」/ EN 'this round sky' 均指'圆形（椭圆）的天空'。CHS全文：'我……我从未离开过这座城。不知这圆椭的天空的另一端会有什么呢？'

当前日版：

`我……我从未离开过这座城。\p不知这圆形的天空的\n另一端会有什么呢？`

文件：`patch/batches/316_sootopolis_city.json`。

原日文（`0x081E2DD3`）：

`ぼく……　まだ　いちども　このまちから\nそとに　でたこと　ないんだ\pあの　まあるい　そらの　むこうには\nどんな　せかいが　あるのかな?`

Wokann日文（`data/maps/SootopolisCity/scripts.inc`）：

`ぼく⋯⋯　まだ　いちども　このまちから\nそとに　でたこと　ないんだ\pあの　まあるい　そらの　むこうには\nどんな　せかいが　あるのかな？$`

原英文（`data/maps/SootopolisCity/scripts.inc`，`fe570a7e5^`）：

`I… I've never been out of this city.\pI wonder what the world is like on\nthe other side of this round sky?$`

当前美版（`data/maps/SootopolisCity/scripts.inc`）：

`我……我从未离开过这座城。\p不知这圆形的天空的\n另一端会有什么呢？$`

### 7478 — VictoryRoad_B1F_Text_MitchellIntro

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「わたしの ポケモンは すばらしいですよ」/ EN 'My POKéMON are cosmically awe inspiring!' 的命题是'宝可梦本身很出色'；CHS'我的宝可梦的士气已经达到了顶点！'把主语偷换为'士气达到顶点'，改变了原句含义，非单纯意译。

当前日版：

`我的宝可梦\n真是令人惊叹！`

文件：`patch/batches/336_victory_road_b1_f.json`。

原日文（`0x08219AF4`）：

`わたしの　ポケモンは　すばらしいですよ!`

Wokann日文（`data/maps/VictoryRoad_B1F/scripts.inc`）：

`わたしの　ポケモンは　すばらしいですよ！$`

原英文（`data/maps/VictoryRoad_B1F/scripts.inc`，`fe570a7e5^`）：

`My POKéMON are cosmically\nawe inspiring!$`

当前美版（`data/maps/VictoryRoad_B1F/scripts.inc`）：

`我的宝可梦\n真是令人惊叹！$`

### 7558 — MoveTutor_Text_SubstituteTeach

结论：**需修复**。

重复“如果”已经修复；但 そうだわ / I know! 在此是想到一个主意，不是明白了别人说的话。

方案：仅将“明白了！”改为“对了！”，保留后续替身教学。

原报告问题：

CHS'我在想如果这个世界如果有不止一个自己该多有趣啊'中'如果'出现两次，属笔误；JP「なんにんもの じぶんが いて いくつもの じんせいを たのしめたらな- って おもうの」/ EN 'I think about how nice it would be if there were more than just one me so I could enjoy all sorts of lives.' 均为单次条件。us_chs_text 与 chs_text 完全一致，错误继承自美版汉化。

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

### 7635 — Text_MonUsedStrength

结论：**不需修复**。

第一句已带宝可梦名；下一句省略主语可由语境确定，不是必须重复显示第二次名字。

方案：保留当前文本/布局。

原报告问题：

JP 第二句「{FD:02}の かいりきの おかげで いわを おせるように なった!」/ EN "{STR_VAR_1}'s STRENGTH made it possible to move boulders around!" 均重复宝可梦占位符作主语；CHS 第二句'使出了怪力后，可以推动岩石了！'完全丢掉 {STR_VAR_1}。同条内可凭语境推断，但占位符集合与 JP/EN 不一致，属信息丢失。

当前日版：

`{FD_02}使出了怪力！\p使出了怪力后，\n可以推动岩石了！`

文件：`patch/batches/342_field_move_scripts_scripts.json`。

原日文（`0x082567F3`）：

`{PLACEHOLDER_02}　は\nかいりきを　はっきした!\p{PLACEHOLDER_02}の　かいりきの　おかげで\nいわを　おせるように　なった!`

Wokann日文（`data/scripts/field_move_scripts.inc`）：

`{STR_VAR_1}　は\nかいりきを　はっきした！\p{STR_VAR_1}の　かいりきの　おかげで\nいわを　おせるように　なった！$`

原英文（`data/scripts/field_move_scripts.inc`，`fe570a7e5^`）：

`{STR_VAR_1} used STRENGTH!\p{STR_VAR_1}'s STRENGTH made it\npossible to move boulders around!$`

当前美版（`data/scripts/field_move_scripts.inc`）：

`{STR_VAR_1}使出了怪力！\p使出了怪力后，\n可以推动岩石了！$`

### 7886 — MatchCall_BattleFrontierStreakText3

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「{FD:04}れんしょう って すごい きろく なんだろ?」/ EN 'A big {STR_VAR_3}-win streak… That is a big record, isn't it?' 意为'了不起的纪录'；CHS'这是个新纪录，对吧？'加入原文没有的'新'字，改变了评价含义（是否为'新'纪录与是否为'惊人'纪录是两回事）。

当前日版：

`喂你好，{FD_01}！\n是我，{FD_02}。\p我听说你在{FD_03}\n势不可挡！\p一个漂亮的{FD_04}连胜……\n这纪录很了不起，对吧？\p我也要努力了！\n以后联系！`

文件：`patch/batches/343_match_call.json`。

原日文（`0x08268A4C`）：

`おう!　{PLACEHOLDER_01}!\n{PLACEHOLDER_02}だぞ!\p{PLACEHOLDER_03}　で\nおおあばれ　したらしいな!\p{PLACEHOLDER_04}れんしょう　って\nすごい　きろく　なんだろ?\pおれも　まけられね-な!\nじゃ　またな!`

Wokann日文（`data/text/match_call.inc`）：

`おう！　{PLAYER}！\n{STR_VAR_1}だぞ！\p{STR_VAR_2}　で\nおおあばれ　したらしいな！\p{STR_VAR_3}れんしょう　って\nすごい　きろく　なんだろ？\pおれも　まけられねーな！\nじゃ　またな！$`

原英文（`data/text/match_call.inc`，`fe570a7e5^`）：

`Hey there, {PLAYER}!\nIt's me, {STR_VAR_1}.\pI heard you went on a tear at\nthe {STR_VAR_2}!\pA big {STR_VAR_3}-win streak…\nThat is a big record, isn't it?\pI'd better get it together, too!\nCatch you soon!$`

当前美版（`data/text/match_call.inc`）：

`喂你好，{PLAYER}！\n是我，{STR_VAR_1}。\p我听说你在{STR_VAR_2}\n势不可挡！\p一个漂亮的{STR_VAR_3}连胜……\n这纪录很了不起，对吧？\p我也要努力了！\n以后联系！$`

### 7900 — MatchCall_BattleFrontierRecordStreakText3

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

与 idx 6634 为同一模板的重复文本：JP「{FD:04}れんしょう って すごい きろく なんだろ?」/ EN 'That is a big record, isn't it?' 意为'了不起的纪录'，CHS 误作'新纪录'。

当前日版：

`喂你好，{FD_01}！\n是我，{FD_02}。\p我听说你在{FD_03}\n势不可挡！\p一个漂亮的{FD_04}连胜……\n这纪录很了不起，对吧？\p我也要努力了！\n以后联系！`

文件：`patch/batches/343_match_call.json`。

原日文（`0x08268E48`）：

`おう!　{PLACEHOLDER_01}!\n{PLACEHOLDER_02}だぞ!\p{PLACEHOLDER_03}　で\nおおあばれ　したらしいな!\p{PLACEHOLDER_04}れんしょう　って\nすごい　きろく　なんだろ?\pおれも　まけられね-な!\nじゃ　またな!`

Wokann日文（`data/text/match_call.inc`）：

`おう！　{PLAYER}！\n{STR_VAR_1}だぞ！\p{STR_VAR_2}　で\nおおあばれ　したらしいな！\p{STR_VAR_3}れんしょう　って\nすごい　きろく　なんだろ？\pおれも　まけられねーな！\nじゃ　またな！$`

原英文（`data/text/match_call.inc`，`fe570a7e5^`）：

`Hey there, {PLAYER}!\nIt's me, {STR_VAR_1}.\pI heard you went on a tear at\nthe {STR_VAR_2}!\pA big {STR_VAR_3}-win streak…\nThat is a big record, isn't it?\pI'd better get it together, too!\nCatch you soon!$`

当前美版（`data/text/match_call.inc`）：

`喂你好，{PLAYER}！\n是我，{STR_VAR_1}。\p我听说你在{STR_VAR_2}\n势不可挡！\p一个漂亮的{STR_VAR_3}连胜……\n这纪录很了不起，对吧？\p我也要努力了！\n以后联系！$`

### 8076 — CableClub_Text_UnionRoomInfo

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「レベル30までのポケモン2ひきで1たい1のたいせん」/ EN "two POKéMON up to Lv. 30" 均含"以下/或以下"（up to）限定，CHS「您可以拿出2只等级30的宝可梦进行1对1的对战」丢掉该限定，语义从"30级或以下"变为"恰为30级"。

当前日版：

`联盟交谊厅的训练家都是在您周围\n并且也进入了联盟交谊厅的玩家。\p你可以在这里做各种事情，\n比如互相问候。\p您可以拿出2只不超过30级的\n宝可梦进行1对1的对战。\p您也可以和2到5个人\n在这里进行聊天。\p或者您也可以登记宝可梦\n进行交换。\p要进入房间吗？`

文件：`patch/batches/359_cable_club.json`。

原日文（`0x082486D6`）：

`ユニオン　ル-ム　は　あなたの\nちかくで　ユニオン　ル-ムに\lはいっている　ひとが　あらわれます\pかんたんな　あいさつをしたり\pレベル30までの　ポケモン2ひきで\n1たい1の　たいせん\p2にんから　5にんまで　どうじに\nおしゃべりが　できる　チャット\pそして　とうろくしき\nポケモン　こうかんが　たのしめます\pへやに　はいりますか?`

Wokann日文（`data/text/cable_club.inc`）：

`ユニオン　ルーム　は　あなたの\nちかくで　ユニオン　ルームに\lはいっている　ひとが　あらわれます\pかんたんな　あいさつをしたり\pレベル30までの　ポケモン2ひきで\n1たい1の　たいせん\p2にんから　5にんまで　どうじに\nおしゃべりが　できる　チャット\pそして　とうろくしき\nポケモン　こうかんが　たのしめます\pへやに　はいりますか？$`

原英文（`data/text/cable_club.inc`，`fe570a7e5^`）：

`The TRAINERS in the UNION ROOM\nwill be those players around you\lwho have also entered the ROOM.\pYou may do all sorts of things\nhere, such as exchanging greetings.\pYou may enter two POKéMON up to\nLv. 30 for a one-on-one battle.\pYou may take part in a chat with\ntwo to five people.\pOr, you may register a POKéMON for\ntrade.\pWould you like to enter the ROOM?$`

当前美版（`data/text/cable_club.inc`）：

`联盟交谊厅的训练家都是在您周围\n并且也进入了联盟交谊厅的玩家。\p你可以在这里做各种事情，\n比如互相问候。\p您可以拿出2只不超过30级的\n宝可梦进行1对1的对战。\p您也可以和2到5个人\n在这里进行聊天。\p或者您也可以登记宝可梦\n进行交换。\p要进入房间吗？$`

### 8199 — Route108_Text_MatthewPostBattle

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

EN "Some people even go inside that ABANDONED SHIP." CHS「有些人甚至走进了那个\n那艘废弃的船。」——「那个」与「那艘」两个指示词叠加，明显冗余不通。

当前日版：

`有些人甚至会进入\n那艘废弃的船。`

文件：`patch/batches/372_trainer_quotes_01.json`。

原日文（`0x0825ABFF`）：

`すてられぶねの　なかに\nはいっていく　やつらが　いるんだよ!`

Wokann日文（`data/text/trainers.inc`）：

`すてられぶねの　なかに\nはいっていく　やつらが　いるんだよ！$`

原英文（`data/text/trainers.inc`，`fe570a7e5^`）：

`Some people even go inside that\nABANDONED SHIP.$`

当前美版（`data/text/trainers.inc`）：

`有些人甚至会进入\n那艘废弃的船。$`

### 8613 — gText_ApprenticeWhichMove14

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

gText_ApprenticeMoveThanks14 的 CHS 含「虽然这是我最后一次……」一句；JP（よ よし {FD:02} いって みるよ! … て てれるな…… ありがとう … また こんど あえたら…… よろしくね）与 EN（"Oh… Okay! I'll try that {STR_VAR_1}… I hope I can teach that move… nerve-racking… Thank you… If we meet again…"）均无对应。该句实为 gText_ApprenticeWhichMove14 的「こ これで さいごに するからさ」/"I'll make it my last, though…" 串入。

当前日版：

`呃……嗯……\n{FD_01}{FD_05}……？\p拜托，别那样看着我。\p我很紧张……\p我……我再次需要你的建议。\p真的很不好意思问，\p对我的{FD_02}而言，\n{FD_03}和{FD_04}哪个更好？`

文件：`patch/batches/383_apprentice_0.json`。

原日文（`0x082724FC`）：

`あ……　あ……\n{PLACEHOLDER_01}{PLACEHOLDER_05}　だよね?\lそ　そんなに　みないで　くれよ!\lてれるだろ\lまた……　そうだん　させて　くれよ\pは　はずかしながらさ\nポケモンに　おしえる　わざがさ\lきまんないんだ　アドバイス　くれよ!\pポケモンは　{PLACEHOLDER_02}なんだ\nだったら　どっちが　いい　かな……?\n{PLACEHOLDER_03}……　{PLACEHOLDER_04}……`

Wokann日文（`data/text/apprentice.inc`）：

`あ⋯⋯　あ⋯⋯\n{PLAYER}{KUN}　だよね？\lそ　そんなに　みないで　くれよ！\lてれるだろ\lまた⋯⋯　そうだん　させて　くれよ\pは　はずかしながらさ\nポケモンに　おしえる　わざがさ\lきまんないんだ　アドバイス　くれよ！\pポケモンは　{STR_VAR_1}なんだ\nだったら　どっちが　いい　かな⋯⋯？\n{STR_VAR_2}⋯⋯　{STR_VAR_3}⋯⋯$`

原英文（`data/text/apprentice.inc`，`fe570a7e5^`）：

`Er… Um…\n{PLAYER}{KUN}…?\pPlease, don't look at me that way.\nI'm getting all flustered…\lI… I need your advice.\pI… I'm really embarrassed, but I can't\ndecide what move I should teach\lmy POKéMON.\pIt's for my {STR_VAR_1}.\nIf the choices were {STR_VAR_2} or\l{STR_VAR_3}, which would be better?$`

当前美版（`data/text/apprentice.inc`）：

`呃……嗯……\n{PLAYER}{KUN}……？\p拜托，别那样看着我。\p我很紧张……\p我……我再次需要你的建议。\p真的很不好意思问，\p对我的{STR_VAR_1}而言，\n{STR_VAR_2}和{STR_VAR_3}哪个更好？$`

### 8626 — gText_ApprenticeWinSpeechThanks9

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

gText_ApprenticeWinSpeechThanks9（说唱水手角色）CHS「嗯哼，这话真棒！\nSi, bueno！嗯哼，\l我会试着这么说，就像，火腿！」：① "Si, bueno！" 拉丁文残留未译——同角色同文本族的 7388（gText_ApprenticeThanksNoHeldItem9）将其译为「好的，行！」，前后不一致；② EN "like, ham!" 是该角色的押韵口头禅填充词，直译为食物「火腿」在中文里不通（同角色其他行如 7388「就像，猛击！」、7219「就像，酷炫！」均按拟声/语气词处理）。

当前日版：

`{FD_02}\p嗯哼，这话真棒！\n好的，嗯哼！\l我会爽快地试着这么说！\p那么，是时候说再见了！\n感谢你为我做的一切！\p改天和我对战一场，好吗？\n再见！`

文件：`patch/batches/383_apprentice_0.json`。

原日文（`0x082731FF`）：

`{PLACEHOLDER_02}\pあはぁ　それいいね\nオ-ケイ　オ-ケイ!\lおじさん　ババ-っと　いってみるよ!\pそれじゃあ　おわかれだ!\nいままで　いろいろ　ありがとうね\lいつか　しょうぶも　してくれよ!\pアディオ-ス!`

Wokann日文（`data/text/apprentice.inc`）：

`{STR_VAR_1}\pあはぁ　それいいね\nオーケイ　オーケイ！\lおじさん　ババーっと　いってみるよ！\pそれじゃあ　おわかれだ！\nいままで　いろいろ　ありがとうね\lいつか　しょうぶも　してくれよ！\pアディオース！$`

原英文（`data/text/apprentice.inc`，`fe570a7e5^`）：

`{STR_VAR_1}\pUh-huh, that's sweet!\nSi, bueno!\lI'll try saying that, like, ham!\pAnd now, it's time to say good-bye!\nThanks for all sorts of things!\pGive me a battle one day, OK?\nAdios!$`

当前美版（`data/text/apprentice.inc`）：

`{STR_VAR_1}\p嗯哼，这话真棒！\n好的，嗯哼！\l我会爽快地试着这么说！\p那么，是时候说再见了！\n感谢你为我做的一切！\p改天和我对战一场，好吗？\n再见！$`

### 8793 — gTVPokemonNewsBattleFrontierText05

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS「训练家{STR_VAR_1}在\n在对战巨蛋单打对战锦标赛中」出现两个“在”。JP「バトルド-ム シングル バトルト-ナメントに ちょうせんした」、EN「set a new {STR_VAR_2}-championship-streak record competing in the BATTLE DOME's SINGLE BATTLE Tournaments」均为单个介词。

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

### 8794 — gTVPokemonNewsBattleFrontierText06

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS「训练家{STR_VAR_1}在\n在对战巨蛋双打对战锦标赛中」出现两个“在”。JP「バトルド-ム ダブル バトルト-ナメントに ちょうせんした」、EN「competing in the BATTLE DOME's DOUBLE BATTLE Tournaments」均为单个介词。

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

### 8988 — SecretBase_Text_Trainer6Intro

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

同为 Trainer6 的自我介绍文本：本条 CHS「欢迎来到我的精灵研究所，\n我在调查秘密的对战。」与 idx 7741（PreChampion，JP/EN 完全相同）「欢迎来到我的宝可梦研究所，\n我在暗中进行对战研究。」用词不一致。“精灵研究所”非常用译名；“调查秘密的对战”不通（JP ここで ポケモン しょうぶに ついて こっそり べんきょう してるのよ = 暗中研究对战，EN “I carry out research on battling in secrecy”）。

当前日版：

`欢迎来到我的宝可梦研究所，\n我在暗中进行对战研究。\p想试试我有多么强吗？`

文件：`patch/batches/391_secret_base_trainers.json`。

原日文（`0x082453EB`）：

`わたしの　ポケモン　けんきゅうじょへ\nようこそ!\pここで　ポケモン　しょうぶに　ついて\nこっそり　べんきょう　してるのよ\pどう　わたしの　じつりょく　みてみる?`

Wokann日文（`data/text/secret_base_trainers.inc`）：

`わたしの　ポケモン　けんきゅうじょへ\nようこそ！\pここで　ポケモン　しょうぶに　ついて\nこっそり　べんきょう　してるのよ\pどう　わたしの　じつりょく　みてみる？$`

原英文（`data/text/secret_base_trainers.inc`，`fe570a7e5^`）：

`Welcome to my POKéMON LAB.\pI carry out research on battling in\nsecrecy.\pWould you like to see how strong I am?$`

当前美版（`data/text/secret_base_trainers.inc`）：

`欢迎来到我的宝可梦研究所，\n我在暗中进行对战研究。\p想试试我有多么强吗？$`

### 9108 — MauvilleCity_PokemonCenter_1F_Text_CheckedPokedexStory

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS「他校对宝可梦图鉴有\n{STR_VAR_1}次了！」：同上，“校对”不当。JP「なんと {FD:02}かいも ずかんを みた そうだ」、EN「checked a POKéDEX {STR_VAR_1} times」。

当前日版：

`关于{FD_04}是这样流传\n的。\p他查看宝可梦图鉴有\n{FD_02}次了！\p{FD_04}喜欢在宝可梦图鉴中查看\n宝可梦的数据！`

文件：`patch/batches/392_mauville_man_0.json`。

原日文（`0x08255EB9`）：

`{PLACEHOLDER_04}という\nトレ-ナ-の　はなし　だが……\pなんと　{PLACEHOLDER_02}かいも\nずかんを　みた　そうだ!\p{PLACEHOLDER_04}は　ずかんで　ポケモンを\nしらべるのが　だいすきな　トレ-ナ-だな!`

Wokann日文（`data/scripts/mauville_man.inc`）：

`{STR_VAR_3}という\nトレーナーの　はなし　だが⋯⋯\pなんと　{STR_VAR_1}かいも\nずかんを　みた　そうだ！\p{STR_VAR_3}は　ずかんで　ポケモンを\nしらべるのが　だいすきな　トレーナーだな！$`

原英文（`data/scripts/mauville_man.inc`，`fe570a7e5^`）：

`This is a tale of a TRAINER\nnamed {STR_VAR_3}.\pThis TRAINER checked a POKéDEX\n{STR_VAR_1} times!\p{STR_VAR_3} must love inspecting\nPOKéMON in a POKéDEX!$`

当前美版（`data/scripts/mauville_man.inc`）：

`关于{STR_VAR_3}是这样流传\n的。\p他查看宝可梦图鉴有\n{STR_VAR_1}次了！\p{STR_VAR_3}喜欢在宝可梦图鉴中查看\n宝可梦的数据！$`

### 9110 — MauvilleCity_PokemonCenter_1F_Text_LedgesJumpedStory

结论：**需修复**。

“几经”和计数已修复，但把 ledges / だんさ译成岩礁，仍然错误；说的是地图可跳下的台阶。

方案：将两处“岩礁”改为“台阶”；计数、名字占位符及分页保留。

原报告问题：

CHS「他几经跳过\n{STR_VAR_1}次了！」：①“几经”应为“已经”（JP なんと {FD:02}かいも だんさを とびおりた らしい = 居然跳了 N 次）；②“跳过”缺宾语（跳过什么？EN “jumped down ledges {STR_VAR_1} times”）；③“跳过”应为“跳下”（とびおりた = jump down）。

当前日版：

`关于{FD_04}是这样流传\n的。\p他已经跳下\n{FD_02}次岩礁了！\p如果有适合跳跃的岩礁，\n{FD_04}一定会去跳的！`

文件：`patch/batches/392_mauville_man_0.json`。

原日文（`0x08255F9B`）：

`{PLACEHOLDER_04}という\nトレ-ナ-の　はなし　だが……\pなんと　{PLACEHOLDER_02}かいも\nだんさを　とびおりた　らしい!\p{PLACEHOLDER_04}は　だんさを　みると\nとびおりずに　おれない　トレ-ナ-だな!`

Wokann日文（`data/scripts/mauville_man.inc`）：

`{STR_VAR_3}という\nトレーナーの　はなし　だが⋯⋯\pなんと　{STR_VAR_1}かいも\nだんさを　とびおりた　らしい！\p{STR_VAR_3}は　だんさを　みると\nとびおりずに　おれない　トレーナーだな！$`

原英文（`data/scripts/mauville_man.inc`，`fe570a7e5^`）：

`This is a tale of a TRAINER\nnamed {STR_VAR_3}.\pThis TRAINER jumped down ledges\n{STR_VAR_1} times!\pIf there's a ledge to be jumped,\n{STR_VAR_3} can't ignore it!$`

当前美版（`data/scripts/mauville_man.inc`）：

`关于{STR_VAR_3}是这样流传\n的。\p他已经跳下\n{STR_VAR_1}次岩礁了！\p如果有适合跳跃的岩礁，\n{STR_VAR_3}一定会去跳的！$`

### 9114 — MauvilleCity_PokemonCenter_1F_Text_UsedDaycareStory

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS「他在培育屋照顾的宝可梦\n有{STR_VAR_1}只！」：数量单位“只”错误。JP「{FD:02}かいも そだてやに あずけた らしい」、EN「left POKéMON with the DAY CARE {STR_VAR_1} times」——计数的是“寄存次数”（次），不是宝可梦只数。

当前日版：

`关于{FD_04}是这样流传\n的。\p他曾把宝可梦寄存在培育屋\n{FD_02}次！\p{FD_04}一定是一个培育\n宝可梦的老手了！`

文件：`patch/batches/392_mauville_man_0.json`。

原日文（`0x08256150`）：

`{PLACEHOLDER_04}という\nトレ-ナ-の　はなし　だが……\pなんと　{PLACEHOLDER_02}かいも\nそだてやに　あずけた　らしい!\p{PLACEHOLDER_04}は　とにかく　そだてまくる\nモ-レツな　トレ-ナ-に　ちがいない!`

Wokann日文（`data/scripts/mauville_man.inc`）：

`{STR_VAR_3}という\nトレーナーの　はなし　だが⋯⋯\pなんと　{STR_VAR_1}かいも\nそだてやに　あずけた　らしい！\p{STR_VAR_3}は　とにかく　そだてまくる\nモーレツな　トレーナーに　ちがいない！$`

原英文（`data/scripts/mauville_man.inc`，`fe570a7e5^`）：

`This is a tale of a TRAINER\nnamed {STR_VAR_3}.\pThis TRAINER left POKéMON with the\nDAY CARE {STR_VAR_1} times!\p{STR_VAR_3} must be a real go-getter\nwho raises POKéMON aggressively!$`

当前美版（`data/scripts/mauville_man.inc`）：

`关于{STR_VAR_3}是这样流传\n的。\p他曾把宝可梦寄存在培育屋\n{STR_VAR_1}次！\p{STR_VAR_3}一定是一个培育\n宝可梦的老手了！$`

### 9121 — MauvilleCity_PokemonCenter_1F_Text_CheckedPokedexAction

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS「校对图鉴数据」：JP「ずかんを みた」= 查看图鉴，EN「Checked a POKéDEX」。中文“校对”指对照校正文字，与“查看/查阅”不符。

当前日版：

`查看图鉴数据`

文件：`patch/batches/393_mauville_man_1.json`。

原日文（`0x08255EB1`）：

`ずかんを　みた`

Wokann日文（`data/scripts/mauville_man.inc`）：

`ずかんを　みた$`

原英文（`data/scripts/mauville_man.inc`，`fe570a7e5^`）：

`Checked a POKéDEX$`

当前美版（`data/scripts/mauville_man.inc`）：

`查看图鉴数据$`

### 9132 — MauvilleCity_PokemonCenter_1F_Text_UsedDaycareTitle

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS「在培育屋工作的训练家」：JP「そだてやを つかいこなす トレーナー」= 善于使用培育屋的训练家，EN「The DAY CARE-Using Trainer」。“在培育屋工作”意为在培育屋上班，与原文相反。

当前日版：

`善用培育屋的训练家`

文件：`patch/batches/393_mauville_man_1.json`。

原日文（`0x0825612C`）：

`そだてやを　つかいこなす　トレ-ナ-`

Wokann日文（`data/scripts/mauville_man.inc`）：

`そだてやを　つかいこなす　トレーナー$`

原英文（`data/scripts/mauville_man.inc`，`fe570a7e5^`）：

`The DAY CARE-Using Trainer$`

当前美版（`data/scripts/mauville_man.inc`）：

`善用培育屋的训练家$`

### 9156 — GiddyText_SoDesirable

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS「太合意的了！」：JP「あこがれる」= 憧憬/向往，EN「so desirable」。中文“合意”指双方意见一致（agree/consent），与原文语义不符。

当前日版：

` 太令人向往了！`

文件：`patch/batches/395_mauville_man.json`。

原日文（`0x082593F0`）：

`　あこがれる　よね-`

Wokann日文（`data/text/mauville_man.inc`）：

`　あこがれる　よねー$`

原英文（`data/text/mauville_man.inc`，`fe570a7e5^`）：

` so desirable!$`

当前美版（`data/text/mauville_man.inc`）：

` 太令人向往了！$`

### 9174 — CaveOfOrigin_B1F_Text_WallaceStory

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS「正是烈空坐平息了\l那2只宝可梦的的斗争」出现“的的”重复。JP「あの2ひきの たたかいを しずめた」、EN「becalmed the two combatants」。

当前日版：

`啊，你就是{FD_01}{FD_05}吗？\n你的活跃表现我早有耳闻。\p我的名字是米可利。\p曾经是琉璃市的道馆馆主，\n不过因为某些原因，\p现在我把管理道馆的事情\n托付给我的老师亚当了。\p…… …… ……\n…… …… ……\p在这里肆虐的2只宝可梦——\n固拉多和盖欧卡，\l被称为超古代宝可梦，\p然而，超古代宝可梦\n并不止这2只……\p在世界的某处\n还存在着第3只——\p没错，那就是被称为烈空坐\n的超古代宝可梦。\p传说在远古时期，\n正是烈空坐平息了\l那2只宝可梦的斗争。\p可就连我也不清楚它\n如今究竟身在何处……`

文件：`patch/batches/398_player_name_dialogue.json`。

原日文（`0x082191C4`）：

`そうか　きみが　{PLACEHOLDER_01}{PLACEHOLDER_05}……\nきみの　かつやくは　きいているよ\pわたしの　なまえは　ミクリ\nルネの　ジムリ-ダ-を　していたけれど\lちょっと　わけが　あってね\pいまは　ししょうの　アダンさんに\nジムのことは　おまかせして　いるのさ\p……　……　……\n……　……　……\pいま　このまちで　あばれている\nグラ-ドンと　カイオ-ガは\lちょうこだい　ポケモンと　いわれている\pけれど　ちょうこだい　ポケモンは\nあの2ひき　だけじゃ　なかった……\lどこかに　もう1ひき\pそう……　レックウザと　よばれる\nちょうこだい　ポケモンが　いるんだよ\pとおい　むかしに\nあの2ひきの　たたかいを　しずめたのも\lレックウザ　だと　いわれている\pだが　レックウザが　どこに　いるかは\nわたしにも　わからない……`

Wokann日文（`data/maps/CaveOfOrigin_B1F/scripts.inc`）：

`そうか　きみが　{PLAYER}{KUN}⋯⋯\nきみの　かつやくは　きいているよ\pわたしの　なまえは　ミクリ\nルネの　ジムリーダーを　していたけれど\lちょっと　わけが　あってね\pいまは　ししょうの　アダンさんに\nジムのことは　おまかせして　いるのさ\p⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯\pいま　このまちで　あばれている\nグラードンと　カイオーガは\lちょうこだい　ポケモンと　いわれている\pけれど　ちょうこだい　ポケモンは\nあの2ひき　だけじゃ　なかった⋯⋯\lどこかに　もう1ひき\pそう⋯⋯　レックウザと　よばれる\nちょうこだい　ポケモンが　いるんだよ\pとおい　むかしに\nあの2ひきの　たたかいを　しずめたのも\lレックウザ　だと　いわれている\pだが　レックウザが　どこに　いるかは\nわたしにも　わからない⋯⋯$`

原英文（`data/maps/CaveOfOrigin_B1F/scripts.inc`，`fe570a7e5^`）：

`Ah, so you are {PLAYER}{KUN}?\nI've heard tales of your exploits.\pMy name is WALLACE.\pI was once the GYM LEADER of\nSOOTOPOLIS, but something came up.\pSo now, I've entrusted my mentor JUAN\nwith the GYM's operation.\p… … … … … …\n… … … … … …\pGROUDON and KYOGRE, the two POKéMON\nwreaking havoc here, are considered\lto be super-ancient POKéMON.\pBut there aren't just two super-\nancient POKéMON.\pThere is one more somewhere.\pSomewhere, there is a super-\nancient POKéMON named RAYQUAZA.\pIt's said that it was RAYQUAZA that\nbecalmed the two combatants in\lthe distant past.\pBut even I have no clue as to\nRAYQUAZA's whereabouts…$`

当前美版（`data/maps/CaveOfOrigin_B1F/scripts.inc`）：

`啊，你就是{PLAYER}{KUN}吗？\n你的活跃表现我早有耳闻。\p我的名字是米可利。\p曾经是琉璃市的道馆馆主，\n不过因为某些原因，\p现在我把管理道馆的事情\n托付给我的老师亚当了。\p…… …… ……\n…… …… ……\p在这里肆虐的2只宝可梦——\n固拉多和盖欧卡，\l被称为超古代宝可梦，\p然而，超古代宝可梦\n并不止这2只……\p在世界的某处\n还存在着第3只——\p没错，那就是被称为烈空坐\n的超古代宝可梦。\p传说在远古时期，\n正是烈空坐平息了\l那2只宝可梦的斗争。\p可就连我也不清楚它\n如今究竟身在何处……$`

### 9237 — Roulette_Text_YouveWonXCoins

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS「获得了{STR_VAR_1}枚硬币！」：同系列轮盘文本 7976「代币不足」、7982「代币用光了」、7985「代币盒满了」均用“代币”，此处独用“硬币”，术语不统一。

当前日版：

`恭喜中奖！\n获得了{FD_02}枚代币！`

文件：`patch/batches/401_roulette.json`。

原日文（`0x08262D79`）：

`おめでとう　ございます!\nコイン　{PLACEHOLDER_02}まい　はいります!`

Wokann日文（`data/scripts/roulette.inc`）：

`おめでとう　ございます！\nコイン　{STR_VAR_1}まい　はいります！$`

原英文（`data/scripts/roulette.inc`，`fe570a7e5^`）：

`You've won {STR_VAR_1} COINS!$`

当前美版（`data/scripts/roulette.inc`）：

`恭喜中奖！\n获得了{STR_VAR_1}枚代币！$`

### 9381 — gText_Contest_Shyness

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS「扑通扑通」：JP「モジモジ」= 害羞扭捏（bashful fidgeting），EN「shyness」。中文“扑通扑通”是心跳声拟声词，不表示“害羞”。同系列 8132 懒懒洋洋/8133 犹犹豫豫/8134 战战栗栗均为状态词，唯独本条用了拟声词，风格亦不一致。

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

### 9589 — gText_TheQuizAnswerIs

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

EN "The quiz answer is?"（谜题答案是？），CHS 为"谜题答案的是？"——多出一个"的"，语义不通顺，应为"谜题的答案是？"或"谜题答案是什么？"。us_chs_text 同样为"谜题答案的是？"，属美版汉化源错误。

当前日版：

`谜题的答案是？`

文件：`patch/batches/411_strings_c_direct.json`。

原日文（`0x085CBCA0`）：

`クイズの　こたえは?`

Wokann日文（`src/strings.c`）：

`クイズの　こたえは？`

原英文（`src/strings.c`，`fe570a7e5^`）：

`The quiz answer is?`

当前美版（`src/strings.c`）：

`谜题的答案是？`

### 10075 — sText_MemberNoLongerAvailable

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP原文「つごうが　わるくなってしまったメンバ-が　います」/ EN "There is a member who can no longer remain available."（有成员因故无法继续），但CHS文本为"对方好像不方便……"；这与相邻 idx=8826（JP「つごうが　わるいみたい…」/ EN "The other TRAINER appears unavailable…"）的语义互换——两条无线连接提示文本的中文内容被调换了。us_chs_text 侧同样已互换，故属美版汉化源错误，JP移植只是如实搬运。

当前日版：

`有成员不便进行……\p`

文件：`patch/batches/419_union_room_0.json`。

原日文（`0x082C09C4`）：

`つごうが　わるくなってしまった\nメンバ-が　います\p`

Wokann日文（`src/data/union_room3.h`）：

`つごうが　わるくなってしまった\nメンバーが　います\p`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`There is a member who can no\nlonger remain available.\p`

当前美版（`src/data/union_room.h`）：

`有成员不便进行……\p`

### 10076 — sText_TrainerAppearsUnavailable

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP原文「つごうが　わるいみたい…」/ EN "The other TRAINER appears unavailable…"（对方训练家好像不方便），但CHS文本为"有成员不便进行……"；这与相邻 idx=8825（JP「…メンバ-が　います」/ EN "There is a member who can no longer remain available."）的语义互换——两条无线连接提示文本的中文内容被调换了。us_chs_text 侧同样已互换，故属美版汉化源错误，JP移植只是如实搬运。

当前日版：

`对方好像不方便……\p`

文件：`patch/batches/419_union_room_0.json`。

原日文（`0x082C09E8`）：

`つごうが　わるいみたい…\p`

Wokann日文（`src/data/union_room3.h`）：

`つごうが　わるいみたい⋯\p`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`The other TRAINER appears\nunavailable…\p`

当前美版（`src/data/union_room.h`）：

`对方好像不方便……\p`

### 10264 — sDiveBallDesc

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP かいていにいるポケモンがつかまえやすくなる / EN works better on POKéMON on the ocean floor；CHS 译作"容易捕捉生活在水世界的宝可梦"，"水世界"范围大于 JP/EN 的"海底(ocean floor)"，有轻微出入（与美版汉化一致，属继承措辞）。

当前日版：

`有点与众不同的球\n。容易捕捉生活在\n海底的宝可梦`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`かいていに　いる\nポケモンが　つかまえ\nやすくなる　ボール`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A BALL that works\nbetter on POKéMON\non the ocean floor.`

当前美版（`src/data/text/item_descriptions.h`）：

`有点与众不同的球\n。容易捕捉生活在\n海底的宝可梦`

### 10293 — sElixirDesc

结论：**需修复**。

原报告针对第四个招式的信息，当前没有该语义遗漏；独立检查发现“10PP”被断成“1\n0PP”，应避免数字跨行。

方案：能让宝可梦学会的\n4个招式各回复\n10PP；不拆 PP，不加结尾句号。

原报告问题：

JP すべてのわざのわざポイントを10かいふくする / EN Restores the PP of all moves by 10；CHS 与美版一致作"4个招式各回复10PP"，字面"4个"≠JP"所有"（游戏中宝可梦最多学会4招，实际效果等价，属合理意译但字面偏离）。

当前日版：

`能让宝可梦学会的\n4个招式各回复1\n0PP`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`すべての　わざの\nわざポイントを\n10　かいふくする`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`Restores the PP\nof all moves by 10.`

当前美版（`src/data/text/item_descriptions.h`）：

`能让宝可梦学会的\n4个招式各回复1\n0PP。`

### 10294 — sMaxElixirDesc

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP ポケモン1ぴきのすべてのわざポイントをぜんかいふくする / EN Fully restores the PP of a POKéMON's moves；CHS 与美版一致作"4个招式回复所有PP"，字面"4个"≠JP"所有"（实际效果等价，属合理意译但字面偏离）。

当前日版：

`能让宝可梦学会的\n4个招式回复所有\nPP`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`ポケモン　1ぴきの\nすべての　わざポイントを\nぜんかいふくする`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`Fully restores the\nPP of a POKéMON's\nmoves.`

当前美版（`src/data/text/item_descriptions.h`）：

`能让宝可梦学会的\n4个招式回复所有\nPP。`

### 10325 — sRareCandyDesc

结论：**不需修复**。

“充满能量”是对糖果的描述性补充，没有更改升一级的机制。

方案：保留当前文本/布局。

原报告问题：

JP ポケモンのレベルを1あげる（ふしぎなアメ）/ EN Raises the level of a POKéMON by one；CHS 与美版一致作"充满能量的糖果"，JP 仅言"神奇的糖"并无"充满能量"之意，属美版汉化添加的修饰（效果"等级提高1"正确）。

当前日版：

`充满能量的糖果。\n给宝可梦后，等级\n会提高1`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`ポケモンの　レベルを\n1　あげる`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`Raises the level\nof a POKéMON by\none.`

当前美版（`src/data/text/item_descriptions.h`）：

`充满能量的糖果。\n给宝可梦后，等级\n会提高1。`

### 10326 — sPPUpDesc

结论：**不需修复**。

PP Up 小幅提升是实际效果，非必须删掉的错误。

方案：保留当前文本/布局。

原报告问题：

JP わざポイントのさいだいちがあがる / EN Raises the maximum PP of a selected move；CHS 与美版一致作"其中1个招式PP最大值少量提高"，JP/EN 未说明幅度，"少量"为美版汉化添加（效果正确）。

当前日版：

`能让宝可梦学会的\n其中1个招式PP\n最大值少量提高`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`わざポイントの\nさいだいちが　あがる`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`Raises the maximum\nPP of a selected\nmove.`

当前美版（`src/data/text/item_descriptions.h`）：

`能让宝可梦学会的\n其中1个招式PP\n最大值少量提高。`

### 10363 — sPearlDesc

结论：**不需修复**。

小珍珠的“小”没有改变卖价或用途。

方案：保留当前文本/布局。

原报告问题：

JP「きれいな しんじゅ」/EN「A pretty pearl」→CHS「散发着光泽且有点小的珍珠」：其中「有点小」在JP/EN文本中无依据（译者为与大珍珠对比而添加的修饰），不影响效果理解。

当前日版：

`散发着光泽且有点\n小的珍珠。可以在\n商店低价出售`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`きれいな　しんじゅ\nやすく　うれる`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A pretty pearl\nthat would sell at a\ncheap price.`

当前美版（`src/data/text/item_descriptions.h`）：

`散发着光泽且有点\n小的珍珠。可以在\n商店低价出售。`

### 10367 — sNuggetDesc

结论：**不需修复**。

金珠发亮是描述性补充，不构成明确机制错误。

方案：保留当前文本/布局。

原报告问题：

JP「じゅんきんせい」/EN「A nugget of pure gold」→CHS「闪着金光，以纯金制成的珠子」：「闪着金光」在JP/EN文本中无依据，属修饰性添加；「以纯金制成」忠实原文。

当前日版：

`闪着金光，以纯金\n制成的珠子。可以\n在商店高价出售`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`じゅんきん　せい\nたかく　うれる`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A nugget of pure\ngold. Can be sold at\na high price.`

当前美版（`src/data/text/item_descriptions.h`）：

`闪着金光，以纯金\n制成的珠子。可以\n在商店高价出售。`

### 10383 — sWaveMailDesc

结论：**不需修复**。

信纸图案存在区域版本描述差异；不能仅由日文词面否定英文对应物种，暂不统一区域命名。

方案：保留当前文本/布局。

原报告问题：

道具名：JP「クロスメール」（字面为「十字/交叉邮件」）与EN「WAVE MAIL」本身分歧；CHS「波涛邮件」取自EN（所绘为吼吼鲸ホエルコ，波浪意象合理）。非CHS翻译错误，但名称层JP/EN不一致，标注备查。

当前日版：

`印有吼吼鲸的信纸\n，可以让宝可梦携\n带`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`ホエルコの　すがたが\nプリントされた　びんせん\nポケモンに　もたせる`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A WAILMER-print\nMAIL to be held by\na POKéMON.`

当前美版（`src/data/text/item_descriptions.h`）：

`印有吼吼鲸的信纸\n，可以让宝可梦携\n带。`

### 10389 — sRetroMailDesc

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP「3ひきの ポケモンが プリントされた」/EN「drawings of three POKéMON」：「ひき」为个体量词（3只），CHS「印有三种宝可梦」把个体数误作种类数（3个种类）。

当前日版：

`印有三只宝可梦的\n信纸，可以让宝可\n梦携带`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`3ひきの　ポケモンが\nプリントされた　びんせん\nポケモンに　もたせる`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`MAIL featuring the\ndrawings of three\nPOKéMON.`

当前美版（`src/data/text/item_descriptions.h`）：

`印有三只宝可梦的\n信纸，可以让宝可\n梦携带`

### 10399 — sSitrusBerryDesc

结论：**需修复**。

本作日英原文都明确回复30HP；实际 ITEM_SITRUS_BERRY 的 holdEffectParam 为30。“少量”省略可操作的固定数值。

方案：携带后，可以回复\n30HP；不采用后世代百分比机制，不加结尾句号。

原报告问题：

JP「たいりょくを 30 かいふくする」/EN「restores 30 HP in battle」明确为30；CHS与US-CHS一致作「可以回复少量HP」，遗漏了JP/EN明确的关键数值30（注意：虽与US-CHS一致，但仍属边界情况）。

当前日版：

`携带后，可以回复\n少量HP`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`もたせると　じぶんで\nたいりょくを\n30　かいふくする`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A hold item that\nrestores 30 HP in\nbattle.`

当前美版（`src/data/text/item_descriptions.h`）：

`携带后，可以回复\n少量HP。`

### 10400 — sFigyBerryDesc

结论：**不需修复**。

低HP触发及不喜欢味道会混乱是真实效果。

方案：保留当前文本/布局。

原报告问题：

JP「もたせると たいりょくを かいふくできるが こんらんすることがある」/EN「restores HP but may confuse」→CHS「携带后危机时可以回复HP。如果讨厌味道会混乱」：添加了JP/EN文本没有的触发条件「危机时」与混乱条件「讨厌味道」（均符合实际游戏机制，但超出原文文本字面范围；与US-CHS一致，非补丁本次改动）。

当前日版：

`携带后危机时可以\n回复HP。如果\n讨厌味道会混乱`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`もたせると　たいりょくを\nかいふく　できるが\nこんらんする　ことがある`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A hold item that\nrestores HP but\nmay confuse.`

当前美版（`src/data/text/item_descriptions.h`）：

`携带后危机时可以\n回复HP。如果\n讨厌味道会混乱。`

### 10401 — sWikiBerryDesc

结论：**不需修复**。

低HP触发及味道混乱是真实效果。

方案：保留当前文本/布局。

原报告问题：

JP「もたせると たいりょくを かいふくできるが こんらんすることがある」/EN「restores HP but may confuse」→CHS「携带后危机时可以回复HP。如果讨厌味道会混乱」：添加了JP/EN文本没有的触发条件「危机时」与混乱条件「讨厌味道」（均符合实际游戏机制，但超出原文文本字面范围；与US-CHS一致，非补丁本次改动）。

当前日版：

`携带后危机时可以\n回复HP。如果\n讨厌味道会混乱`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`もたせると　たいりょくを\nかいふく　できるが\nこんらんする　ことがある`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A hold item that\nrestores HP but\nmay confuse.`

当前美版（`src/data/text/item_descriptions.h`）：

`携带后危机时可以\n回复HP。如果\n讨厌味道会混乱。`

### 10402 — sMagoBerryDesc

结论：**不需修复**。

低HP触发及味道混乱是真实效果。

方案：保留当前文本/布局。

原报告问题：

JP「もたせると たいりょくを かいふくできるが こんらんすることがある」/EN「restores HP but may confuse」→CHS「携带后危机时可以回复HP。如果讨厌味道会混乱」：添加了JP/EN文本没有的触发条件「危机时」与混乱条件「讨厌味道」（均符合实际游戏机制，但超出原文文本字面范围；与US-CHS一致，非补丁本次改动）。

当前日版：

`携带后危机时可以\n回复HP。如果\n讨厌味道会混乱`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`もたせると　たいりょくを\nかいふく　できるが\nこんらんする　ことがある`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A hold item that\nrestores HP but\nmay confuse.`

当前美版（`src/data/text/item_descriptions.h`）：

`携带后危机时可以\n回复HP。如果\n讨厌味道会混乱。`

### 10403 — sAguavBerryDesc

结论：**不需修复**。

低HP触发及味道混乱是真实效果。

方案：保留当前文本/布局。

原报告问题：

JP「もたせると たいりょくを かいふくできるが こんらんすることがある」/EN「restores HP but may confuse」→CHS「携带后危机时可以回复HP。如果讨厌味道会混乱」：添加了JP/EN文本没有的触发条件「危机时」与混乱条件「讨厌味道」（均符合实际游戏机制，但超出原文文本字面范围；与US-CHS一致，非补丁本次改动）。

当前日版：

`携带后危机时可以\n回复HP。如果\n讨厌味道会混乱`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`もたせると　たいりょくを\nかいふく　できるが\nこんらんする　ことがある`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A hold item that\nrestores HP but\nmay confuse.`

当前美版（`src/data/text/item_descriptions.h`）：

`携带后危机时可以\n回复HP。如果\n讨厌味道会混乱。`

### 10404 — sIapapaBerryDesc

结论：**不需修复**。

低HP触发及味道混乱是真实效果。

方案：保留当前文本/布局。

原报告问题：

JP「もたせると たいりょくを かいふくできるが こんらんすることがある」/EN「restores HP but may confuse」→CHS「携带后危机时可以回复HP。如果讨厌味道会混乱」：添加了JP/EN文本没有的触发条件「危机时」与混乱条件「讨厌味道」（均符合实际游戏机制，但超出原文文本字面范围；与US-CHS一致，非补丁本次改动）。

当前日版：

`携带后危机时可以\n回复HP。如果\n讨厌味道会混乱`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`もたせると　たいりょくを\nかいふく　できるが\nこんらんする　ことがある`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A hold item that\nrestores HP but\nmay confuse.`

当前美版（`src/data/text/item_descriptions.h`）：

`携带后危机时可以\n回复HP。如果\n讨厌味道会混乱。`

### 10437 — sWhiteHerbDesc

结论：**不需修复**。

白色香草一次性恢复被降低的能力，机制补充真实。

方案：保留当前文本/布局。

原报告问题：

JP「さがった のうりょくを もとにもどす」/EN「restores any lowered stat」→CHS「当携带宝可梦能力降低时，仅能回到之前的状态1次」：添加了JP/EN文本没有的「仅能…1次」（实际机制中白色香草为一次性消耗品，信息属实但超出原文文本）。

当前日版：

`当携带宝可梦能力\n降低时，仅能回到\n之前的状态1次`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`ポケモンに　もたせると\nさがった　のうりょくを\nもとにもどす`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A hold item that\nrestores any\nlowered stat.`

当前美版（`src/data/text/item_descriptions.h`）：

`当携带宝可梦能力\n降低时，仅能回到\n之前的状态1次。`

### 10442 — sMentalHerbDesc

结论：**不需修复**。

心灵香草一次性解除着迷，机制补充真实。

方案：保留当前文本/布局。

原报告问题：

JP「メロメロに なったとき なおして くれる」/EN「snaps POKéMON out of infatuation」→CHS「携带后，会解除着迷状态。只能使用1次」：添加了JP/EN文本没有的「只能使用1次」（实际为一次性消耗品，信息属实但超出原文文本）。

当前日版：

`携带后，会解除着\n迷状态。只能使用\n1次`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`もたせた　ポケモンが\nメロメロに　なったとき\nなおして　くれる`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A hold item that\nsnaps POKéMON out\nof infatuation.`

当前美版（`src/data/text/item_descriptions.h`）：

`携带后，会解除着\n迷状态。只能使用\n1次。`

### 10447 — sCleanseTagDesc

结论：**不需修复**。

携带者在首位是有效的实际使用条件，不删除。

方案：保留当前文本/布局。

原报告问题：

JP『ポケモンに もたせると やせいの ポケモンに そうぐう しにくく なる』/EN『A hold item that helps repel wild POKéMON』均未提『最前排』；该限定虽符合实际游戏机制（仅首位携带生效），但属原文没有的信息

当前日版：

`让最前排的宝可\n梦携带，野生宝可\n梦就会不易出现`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`ポケモンに　もたせると\nやせいの　ポケモンに\nそうぐう　しにくく　なる`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A hold item that\nhelps repel wild\nPOKéMON.`

当前美版（`src/data/text/item_descriptions.h`）：

`让最前排的宝可\n梦携带，野生宝可\n梦就会不易出现。`

### 10475 — sUpGradeDesc

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP『ふしぎな はこ シルフ カンパニーせい』（不可思议的盒子，西尔佛公司制造）/EN『A peculiar box made by SILPH CO.』均只说神秘盒子；CHS『内部储存了各种信息的透明机器』凭空增添了『透明机器』『储存各种信息』等原文完全没有的设定

当前日版：

`不可思议的盒子。\n西尔佛公司制造`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`ふしぎな　はこ\nシルフ　カンパニーせい`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A peculiar box made\nby SILPH CO.`

当前美版（`src/data/text/item_descriptions.h`）：

`不可思议的盒子。\n西尔佛公司制造`

### 10477 — sSeaIncenseDesc

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP『すこしだけ みずタイプの わざのいりょくが あがる』明确『稍微』提升（以区别于神秘水滴的全额提升）；CHS『招式会增强』漏译『稍微』

当前日版：

`香气神奇的薰香。\n携带后，水属性的\n招式会稍微增强`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`ポケモンに　もたせると\nすこしだけ　みずタイプの\nわざのいりょくが　あがる`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A hold item that\nslightly boosts\nWATER-type moves.`

当前美版（`src/data/text/item_descriptions.h`）：

`香气神奇的薰香。\n携带后，水属性的\n招式会稍微增强`

### 10478 — sLaxIncenseDesc

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP『てきの めいちゅうりつを すこしだけ さげる』明确『稍微』降低；CHS『对手招式会变得不容易命中』漏译『稍微』

当前日版：

`携带后，对手招式\n会稍微变得难命中\n`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`ポケモンに　もたせると\nてきの　めいちゅうりつを\nすこしだけ　さげる`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A hold item that\nslightly lowers the\nfoe's accuracy.`

当前美版（`src/data/text/item_descriptions.h`）：

`携带后，对手招式\n会稍微变得难命中\n`

### 10520 — sGoodRodDesc

结论：**不需修复**。

新钓竿的形容不构成明确功能错误。

方案：保留当前文本/布局。

原报告问题：

JP『いいつりざお』（好钓竿）/EN『A decent fishing rod』均未提『新』；CHS『不错的新钓竿』中的『新』属原文没有的信息（无关紧要的修饰）

当前日版：

`不错的新钓竿。在\n有水的地方可以钓\n到宝可梦`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`ポケモンを　つるどうぐ\nなかなかの　つりざおと\nいわれている`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A decent fishing\nrod for catching\nwild POKéMON.`

当前美版（`src/data/text/item_descriptions.h`）：

`不错的新钓竿。在\n有水的地方可以钓\n到宝可梦。`

### 10521 — sSuperRodDesc

结论：**不需修复**。

钓竿形容不构成明确功能错误。

方案：保留当前文本/布局。

原报告问题：

JP『すごいつりざお』/EN『The best fishing rod』均未提『最新』；CHS『最新的厉害钓竿』中的『最新』属原文没有的信息

当前日版：

`最新的厉害钓竿。\n在有水的地方可以\n钓到宝可梦`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`ポケモンを　つるどうぐ\nさいこうの　つりざおと\nいわれている`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`The best fishing\nrod for catching\nwild POKéMON.`

当前美版（`src/data/text/item_descriptions.h`）：

`最新的厉害钓竿。\n在有水的地方可以\n钓到宝可梦。`

### 10533 — sRedOrbDesc

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP『おおむかしの ちからが こめられている という』（据说蕴含着超古代的力量）/EN『said to contain an ancient power』；CHS改写为『据说和丰缘传说渊源颇深』，虽贴合背景但替换了原文明确的『超古代的力量』表述

当前日版：

`散发着红色光辉的\n宝珠。据说蕴含着\n超古代的力量`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`おおむかしの　ちからが\nこめられている　という\nあかく　かがやく　たま`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A red, glowing orb\nsaid to contain an\nancient power.`

当前美版（`src/data/text/item_descriptions.h`）：

`散发着红色光辉的\n宝珠。据说蕴含着\n超古代的力量`

### 10534 — sBlueOrbDesc

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP『おおむかしの ちからが こめられている という』（据说蕴含着超古代的力量）/EN『said to contain an ancient power』；CHS改写为『据说和丰缘传说渊源颇深』，虽贴合背景但替换了原文明确的『超古代的力量』表述

当前日版：

`散发着蓝色光辉的\n宝珠。据说蕴含着\n超古代的力量`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`おおむかしの　ちからが\nこめられている　という\nあおく　かがやく　たま`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A blue, glowing orb\nsaid to contain an\nancient power.`

当前美版（`src/data/text/item_descriptions.h`）：

`散发着蓝色光辉的\n宝珠。据说蕴含着\n超古代的力量`

### 10545 — sDevonScopeDesc

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP原文"みえない ポケモンに はんのうして おとをだす デボンの とくせいひん"(会对看不见的宝可梦起反应并发出声音的得文特制产品)，中文"会对看不见的宝可梦起反应的得文特制产品"漏译了"おとをだす"(发出声音)；52poke"发出声音"亦有收录。

当前日版：

`会对看不见的宝可\n梦起反应并发声的\n得文特制产品`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`みえない　ポケモンに\nはんのうして　おとをだす\nデボンの　とくせいひん`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A device by DEVON\nthat signals any\nunseeable POKéMON.`

当前美版（`src/data/text/item_descriptions.h`）：

`会对看不见的宝可\n梦起反应并发声的\n得文特制产品`

### 10555 — sTM10Desc

结论：**不需修复**。

觉醒力量随使用者变化属性/威力是实际第三世代机制。

方案：保留当前文本/布局。

原报告问题：

JP"ポケモンによって てきに あたえる ダメージの りょうが へんかする"只说了"伤害量随使用者宝可梦变化"；中文"招式的威力和属性会随着使用它的宝可梦而改变"多加了"属性变化"(虽符合实际招式效果，但JP招式说明原文未提及)。

当前日版：

`招式的威力和属性\n会随着使用它的\n宝可梦而改变`

文件：`patch/item_descriptions.json`。

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`The attack power\nvaries among\ndifferent POKéMON.`

当前美版（`src/data/text/item_descriptions.h`）：

`招式的威力和属性\n会随着使用它的\n宝可梦而改变。`

### 10571 — sTM26Desc

结论：**不需修复**。

地震的范围包括周围所有目标；有属性免疫不意味着招式范围描述错误。

方案：保留当前文本/布局。

原报告问题：

JP"じめんを つよく ゆらす とんでいる てきいがいに だいダメージを あたえる"(用力摇晃地面，对飞行中的敌人以外造成大伤害)，中文"利用地震的冲击，攻击自己周围所有的宝可梦"改写成了实际战斗效果，既漏了"とんでいる てきいがい"(飞行中除外)也漏了"だいダメージ"(大伤害)。

当前日版：

`利用地震的冲击，\n攻击自己周围\n所有的宝可梦`

文件：`patch/item_descriptions.json`。

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`Causes a quake\nthat has no effect\non flying foes.`

当前美版（`src/data/text/item_descriptions.h`）：

`利用地震的冲击，\n攻击自己周围\n所有的宝可梦。`

### 10609 — sBikeVoucherDesc

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP"ミラクル・サイクルで おりたたみ じてんしゃと こうかん できる かみ"(可在奇迹自行车店兑换折叠自行车的纸券)；中文"给华蓝市的奇迹自行车店就能交换得到自行车"中"给…店"缺少宾语(券)，句式残缺，虽可猜出含义但不合规范。

当前日版：

`可在华蓝市的奇迹\n自行车店兑换折叠\n自行车的纸券`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`ミラクル·サイクルで\nおりたたみ　じてんしゃと\nこうかん　できる　かみ`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A voucher for\nobtaining a bicycle\nfrom the BIKE SHOP.`

当前美版（`src/data/text/item_descriptions.h`）：

`可在华蓝市的奇迹\n自行车店兑换折叠\n自行车的纸券`

### 10612 — sCardKeyDesc

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP"カードで できた カギ シルフカンパニー ビルの ドアロックを はずせる"(卡片式钥匙，可解除西尔佛公司大楼的门锁)；中文"用来打开的西尔佛公司总部大厦门锁的卡片式钥匙"中"用来打开的"多余且句式错乱，另"总部"为原文没有的增补(虽与事实相符)。

当前日版：

`能打开西尔佛公司\n大厦门锁的卡片式\n钥匙`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`カードで　できた　カギ\nシルフカンパニー　ビルの\nドアロックを　はずせる`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A card-type door\nkey used in SILPH\nCO's office.`

当前美版（`src/data/text/item_descriptions.h`）：

`能打开西尔佛公司\n大厦门锁的卡片式\n钥匙`

### 10620 — sFameCheckerDesc

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP"ゆうめいな じんぶつの じょうほうを いつでも みなおすことが できる"(可随时重新查看有名人物的信息)；中文"可以重复查看打听到的有名人物的东西"把"じょうほう"(信息/情报)译成了"东西"，与原文及52poke("有名人物的相关信息")不符。

当前日版：

`可以重复查看打听\n到的有名人物的信\n息`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`ゆうめいな　じんぶつの\nじょうほうを　いつでも\nみなおすことが　できる`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`Stores information\non famous people\nfor instant recall.`

当前美版（`src/data/text/item_descriptions.h`）：

`可以重复查看打听\n到的有名人物的信\n息`

### 10623 — sTeachyTVDesc

结论：**不需修复**。

节目面向新手是用途说明，不构成必须删除的增补。

方案：保留当前文本/布局。

原报告问题：

JP"トレーナーの やくにたつ ばんぐみを みることが できる テレビ"(可收看对训练家有用的节目的电视)；中文"可以收看对新手训练家有帮助的节目的电视"多加了"新手"限定，原文只说训练家。

当前日版：

`可以收看对新手训\n练家有帮助的节目\n的电视`

文件：`patch/item_descriptions.json`。

Wokann日文（`src/data/text/item_descriptions.h`）：

`トレーナーの　やくにたつ\nばんぐみを　みることが\nできる　テレビ`

原英文（`src/data/text/item_descriptions.h`，`fe570a7e5^`）：

`A TV set tuned to\nan advice program\nfor TRAINERS.`

当前美版（`src/data/text/item_descriptions.h`）：

`可以收看对新手训\n练家有帮助的节目\n的电视。`

### 12011 — BattlePyramid_Text_SevenTrainersRemaining2

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP原文「あと Nにん いる トレーナーが きっと たおしてくれるわ」=剩下的N位训练家一定会打败你（替我报仇），EN 'Someone will humble you!'；中文译为'他们中或许有人比你弱'，把'打败你'反转为'比你弱'，语义完全颠倒。

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

### 12012 — BattlePyramid_Text_SixTrainersRemaining2

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP原文「あと Nにん いる トレーナーが きっと たおしてくれるわ」=剩下的N位训练家一定会打败你（替我报仇），EN 'Someone will humble you!'；中文译为'他们中或许有人比你弱'，把'打败你'反转为'比你弱'，语义完全颠倒。

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

### 12013 — BattlePyramid_Text_FiveTrainersRemaining2

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP原文「あと Nにん いる トレーナーが きっと たおしてくれるわ」=剩下的N位训练家一定会打败你（替我报仇），EN 'Someone will humble you!'；中文译为'他们中或许有人比你弱'，把'打败你'反转为'比你弱'，语义完全颠倒。

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

### 12014 — BattlePyramid_Text_FourTrainersRemaining2

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP原文「あと Nにん いる トレーナーが きっと たおしてくれるわ」=剩下的N位训练家一定会打败你（替我报仇），EN 'Someone will humble you!'；中文译为'他们中或许有人比你弱'，把'打败你'反转为'比你弱'，语义完全颠倒。

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

### 12015 — BattlePyramid_Text_ThreeTrainersRemaining2

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP原文「あと Nにん いる トレーナーが きっと たおしてくれるわ」=剩下的N位训练家一定会打败你（替我报仇），EN 'Someone will humble you!'；中文译为'他们中或许有人比你弱'，把'打败你'反转为'比你弱'，语义完全颠倒。

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

### 12016 — BattlePyramid_Text_TwoTrainersRemaining2

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP原文「あと Nにん いる トレーナーが きっと たおしてくれるわ」=剩下的N位训练家一定会打败你（替我报仇），EN 'Someone will humble you!'；中文译为'他们中或许有人比你弱'，把'打败你'反转为'比你弱'，语义完全颠倒。

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

### 12017 — BattlePyramid_Text_OneTrainersRemaining2

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

JP原文「あと Nにん いる トレーナーが きっと たおしてくれるわ」=剩下的N位训练家一定会打败你（替我报仇），EN 'Someone will humble you!'；中文译为'他们中或许有人比你弱'，把'打败你'反转为'比你弱'，语义完全颠倒。

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

### 12056 — BattleFrontier_Lounge2_Text_SalonMaidenIsThere

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

同一NPC（开拓区迷）对话中 FRONTIER BRAINS（フロンティアブレーン）的译名不统一：本条译为"开拓区大脑"，而同系列其余8条（1225/1228/1231/1234/1237/1240/1342/1466）均译为"开拓之脑"。

当前日版：

`告诉你个秘密！\p被亚希达称作开拓之脑\n的顶级训练家之一现在就在那里。\p那里就是由那个名叫对战塔大君的\n神秘的训练家所掌管的。`

文件：`patch/batches/437_checklist_reviewed_indirect_tables.json`。

原日文（`0x08236C08`）：

`しってるかい?\pあそこは　エニシダが\nフロンティアブレ-ンって　よんでる\lトレ-ナ-の　うちの　ひとり……\lタワ-タイク-ンって　いう\lなぞの　トレ-ナ-が　おさめてるのさ!`

Wokann日文（`data/maps/BattleFrontier_Lounge2/scripts.inc`）：

`しってるかい？\pあそこは　エニシダが\nフロンティアブレーンって　よんでる\lトレーナーの　うちの　ひとり⋯⋯\lタワータイクーンって　いう\lなぞの　トレーナーが　おさめてるのさ！$`

原英文（`data/maps/BattleFrontier_Lounge2/scripts.inc`，`fe570a7e5^`）：

`Bet you didn't know this!\pOne of those top TRAINERS that SCOTT\ncalls the FRONTIER BRAINS is there.\pIt's this mysterious TRAINER called\nthe SALON MAIDEN that runs the place.$`

当前美版（`data/maps/BattleFrontier_Lounge2/scripts.inc`）：

`告诉你个秘密！\p被亚希达称作开拓之脑\n的顶级训练家之一现在就在那里。\p那里就是由那个名叫对战塔大君的\n神秘的训练家所掌管的。$`

### 12178 — MagmaHideout_4F_Text_MaxieAwakenGroudon

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

CHS'展示的你全部的力量吧'中'的'字多余，导致语病；EN 'Show me the full extent of your power!'、JP'ほんとうの ちからを わたしに みせて おくれ'（把真正的力量展示给我）均为'向我展示你全部的力量'。

当前日版：

`赤焰松：固拉多……\p无论怎样也不会\n从岩浆中苏醒的你……\p一直在寻求的，\n是这个靛蓝色宝珠吧？\p我已带来了靛蓝色宝珠。\n就让它的光芒唤醒你吧！\p向我展示……\n展示你全部的力量吧！`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x0821CBDC`）：

`マツブサ“マグマに　ねむる　グラ-ドンよ\nなにをしても　めざめなかった　おまえが\lもとめて　いたのは　あいいろのたま……\pそうなんだろう?\pさあ　ここに　もってきて　やったぞ\nこの　かがやきで　めを　さませ!\pそして　ほんとうの　ちからを\nわたしに　みせて　おくれ!`

Wokann日文（`data/maps/MagmaHideout_4F/scripts.inc`）：

`マツブサ“マグマに　ねむる　グラードンよ\nなにをしても　めざめなかった　おまえが\lもとめて　いたのは　あいいろのたま⋯⋯\pそうなんだろう？\pさあ　ここに　もってきて　やったぞ\nこの　かがやきで　めを　さませ！\pそして　ほんとうの　ちからを\nわたしに　みせて　おくれ！$`

原英文（`data/maps/MagmaHideout_4F/scripts.inc`，`fe570a7e5^`）：

`MAXIE: GROUDON…\pNothing could awaken you from your\nsleep bathed in magma…\pThis BLUE ORB is what you sought.\nWasn't it?\pI have brought you the BLUE ORB.\nLet its shine awaken you!\pAnd show me…\nShow me the full extent of your power!$`

当前美版（`data/maps/MagmaHideout_4F/scripts.inc`）：

`赤焰松：固拉多……\p无论怎样也不会\n从岩浆中苏醒的你……\p一直在寻求的，\n是这个靛蓝色宝珠吧？\p我已带来了靛蓝色宝珠。\n就让它的光芒唤醒你吧！\p向我展示……\n展示你全部的力量吧！$`

### 12203 — sText_MysteryGiftVisitingTrainerInstructions

结论：**需修复**。

美版已补“在”；日版仍缺介词。日版有实际资源，并非“无对应”。另发现提示密码与服务名套用了英文版本。

方案：语法先改为“您可以在友好商店\l参与调查。”；完整区域适配应恢复原提示密码“すごい トレーナー / くれ くれ”和 Joy Spot 说明，保留密码原语言、输入及协议逻辑。实际输入验证路径尚需追踪后再落地密码部分。

原报告问题：

EN 'you may take part in a survey at a POKéMON MART'，US-CHS/补丁中文作「您可以进行调查\l友好商店」——缺介词「在」，「进行调查友好商店」搭配不当，语义可辨但生硬，需人工判定是否修正。

当前日版：

`感谢使用\n神秘礼物系统。\p由于拥有神秘卡片\n您可以进行调查\l友好商店。\p通过调查您可以邀请\n训练家去琉璃市。\p……让我给您一个\n调查的密码吧：\p“GIVE ME\nAWESOME TRAINER”\p把这个写在调查上并发送到\n无线连接系统。`

文件：`patch/batches/471_checklist_mystery_gift_script_texts.json`。

原日文（`0x85fcdbc`）：

`ふしぎなおくりもの　を　ごりよう\nいただき　ありがとう　ございます\pこの　ふしぎなカ-ドを　もっていると\nフレンドリ-ショップの　アンケ-トで\pいろいろな　トレ-ナ-を　ルネシティに\nよぶことが　できますよ!\p……ないしょで　ひとつ　アンケ-トの\nあいことばを　おしえて　あげましょう\p‘すごい　トレ-ナ-\n　くれ　くれ’\pこのことばを　アンケ-トに　かいて\nぜひ　ジョイスポットと\lつうしんして　みてください!`

原英文（`data/scripts/gift_trainer.inc`，`fe570a7e5^`）：

`Thank you for using the MYSTERY\nGIFT System.\pBy holding this WONDER CARD, you\nmay take part in a survey at a\lPOKéMON MART.\pUse these surveys to invite\nTRAINERS to SOOTOPOLIS CITY.\p…Let me give you a secret\npassword for a survey:\p“GIVE ME\nAWESOME TRAINER”\pWrite that in on a survey and send\nit to the WIRELESS\lCOMMUNICATION SYSTEM.$`

当前美版（`data/scripts/gift_trainer.inc`）：

`感谢使用\n神秘礼物系统。\p由于拥有神秘卡片\n您可以在友好商店\l参与调查。\p通过调查您可以邀请\n训练家去琉璃市。\p……让我给您一个\n调查的密码吧：\p“GIVE ME\nAWESOME TRAINER”\p把这个写在调查上并发送到\n无线连接系统。$`

### 12204 — sText_MysteryGiftVisitingTrainerArrived

结论：**需修复**。

美版已经修为希望；日版 batch471 尚为系统。日版原 ROM 0x085FCE8B 有对应文本。

方案：仅将“系统您可以享受”改为“希望您可以享受”。

原报告问题：

US-CHS/补丁中文「系统您可以享受\n与训练家的对战」——「系统」一词于此处不通，显系「希望」之误（对应英文惯用 'I hope you enjoy battling the TRAINER' 的服务用语），致整句不通。

当前日版：

`感谢使用\n神秘礼物系统。\p一位训练家已经来到\n琉璃市寻找您。\p系统您可以享受\n与训练家的对战。\p您可以邀请其他训练家\n通过填写密码。\p试着找寻其他\n有用的密码吧。`

文件：`patch/batches/471_checklist_mystery_gift_script_texts.json`。

原日文（`0x85fce8b`）：

`ふしぎなおくりもの　を　ごりよう\nいただき　ありがとう　ございます\pルネシティに　トレ-ナ-が\nきている　ようですよ\pぜひ　たいせんを\nたのしんで　くださいませ!\pほかの　あいことば　でも\nべつの　トレ-ナ-が　よべますので\pあいことばを　いろいろと\nさがして　みて　ください`

原英文（`data/scripts/gift_trainer.inc`，`fe570a7e5^`）：

`Thank you for using the MYSTERY\nGIFT System.\pA TRAINER has arrived in\nSOOTOPOLIS CITY looking for you.\pWe hope you will enjoy\nbattling the visiting TRAINER.\pYou may invite other TRAINERS by\nentering other passwords.\pTry looking for other passwords\nthat may work.$`

当前美版（`data/scripts/gift_trainer.inc`）：

`感谢使用\n神秘礼物系统。\p一位训练家已经来到\n琉璃市寻找您。\p希望您可以享受\n与训练家的对战。\p您可以邀请其他训练家\n通过填写密码。\p试着找寻其他\n有用的密码吧。$`

### 12205 — Text_RepelWoreOff

结论：**不需修复**。

日版为静态喷雾文本；美版脚本已 bufferitemname STR_VAR_1, ITEM_REPEL，变量有明确写入，不会沿用残留。

方案：保留当前文本/布局。

原报告问题：

JP「スプレーのこうかが きれた」/EN "REPEL's effect wore off…" 均无占位符，US-CHS/补丁中文作「{STR_VAR_1}的效果消失了……」——新增 {STR_VAR_1}。若美版引擎在显示前确有向 STR_VAR_1 填入喷雾名称则为有意增强，否则将显示残留/乱码，需核实代码。

当前日版：

`喷雾的效果消失了……`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x0826239C`）：

`スプレ-のこうかが　きれた`

Wokann日文（`data/scripts/repel.inc`）：

`スプレーのこうかが　きれた$`

原英文（`data/scripts/repel.inc`，`fe570a7e5^`）：

`REPEL's effect wore off…$`

当前美版（`data/scripts/repel.inc`）：

`{STR_VAR_1}的效果消失了……$`

### 12230 — BravoTrainerBattleTower_Text_ResponseUnsatisfied

结论：**原问题已消除**。

独立比对下列当前文字、报告原问题以及日英原文：报告所指错误片段已不再出现在当前定义；本结论仅针对所指问题，不宣称整条或其渲染路径绝无其他错误。

方案：不重复执行旧修复。

原报告问题：

EN"…You can't describe it as anything\nelse but "{STR_VAR_1}"!"；US-CHS"…除了{STR_VAR_1}"之外简直\n找不到更合适的描述了！"引号错位，应为 除了"{STR_VAR_1}"之外。

当前日版：

`“{FD_02}。”\n这也太贴切了吧？\p最后和{FD_04}的那场对战\n……除了“{FD_02}”之外简直\l找不到更合适的描述了！\p{FD_03}的失落感\n简直扑面而来呢！`

文件：`patch/batches/439_checklist_common_placeholders.json`。

原日文（`0x0824CF03`）：

`‘{PLACEHOLDER_02}!’\nなるほどねぇ\pたしかに　{PLACEHOLDER_04}さんとの　たたかいは\n‘{PLACEHOLDER_02}’　としか　いいようがない\lたたかい　でしたからねぇ\p{PLACEHOLDER_03}さんの　くやしさが\nよく　つたわってくるよ!　く-!`

Wokann日文（`data/text/tv/battle_tower_broadcast.inc`）：

`‘{B_COPY_VAR_1}！'\nなるほどねぇ\pたしかに　{B_COPY_VAR_3}さんとの　たたかいは\n‘{B_COPY_VAR_1}'　としか　いいようがない\lたたかい　でしたからねぇ\p{B_COPY_VAR_2}さんの　くやしさが\nよく　つたわってくるよ！　くー！$`

原英文（`data/text/tv.inc`，`fe570a7e5^`）：

`“{STR_VAR_1}.”\nNow isn't that fitting?\pThat battle with {STR_VAR_3} at the\nend… You can't describe it as anything\lelse but “{STR_VAR_1}”!\p{STR_VAR_2}'s disappointment comes across\nloud and clear, I'd say!$`

当前美版（`data/text/tv.inc`）：

`“{STR_VAR_1}。”\n这也太贴切了吧？\p最后和{STR_VAR_3}的那场对战\n……除了“{STR_VAR_1}”之外简直\l找不到更合适的描述了！\p{STR_VAR_2}的失落感\n简直扑面而来呢！$`

### 12568 — gText_GlassChair

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

中文"漂亮椅子"误译。JP "ガラスのいす"、EN "GLASS CHAIR" 均为"玻璃椅子"；US-CHS "漂亮椅子"（pretty）语义错误。补丁未收录此条。

当前日版：

`玻璃椅子`

文件：`patch/batches/453_checklist_named_menu_sections.json`。

原日文（`0x085CABA2`）：

`ガラスのいす`

原英文（`src/strings.c`，`fe570a7e5^`）：

`GLASS CHAIR`

当前美版（`src/strings.c`）：

`玻璃椅子`

### 12569 — gText_GlassDesk

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

中文"漂亮桌子"误译，同上。JP "ガラスのつくえ"、EN "GLASS DESK" 应为"玻璃桌子"。补丁未收录此条。

当前日版：

`玻璃桌子`

文件：`patch/batches/453_checklist_named_menu_sections.json`。

原日文（`0x085CABA9`）：

`ガラスのつくえ`

原英文（`src/strings.c`，`fe570a7e5^`）：

`GLASS DESK`

当前美版（`src/strings.c`）：

`玻璃桌子`

### 13242 — sText_Cancel

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`取消`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x08300ABD`）：

`やめる`

Wokann日文（`src/data/trade.h`）：

`やめる`

原英文（`src/data/trade.h`，`fe570a7e5^`）：

`CANCEL`

当前美版（`src/data/trade.h`）：

`取消`

### 13243 — sText_ChooseAPkmn

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`请选择宝可梦。`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x08300AC1`）：

`ポケモンを　えらんで　ください`

Wokann日文（`src/data/trade.h`）：

`ポケモンを　えらんで　ください`

原英文（`src/data/trade.h`，`fe570a7e5^`）：

`Choose a POKéMON.`

当前美版（`src/data/trade.h`）：

`请选择宝可梦。`

### 13244 — sText_Summary

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`查看能力`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x08300AD1`）：

`つよさをみる`

Wokann日文（`src/data/trade.h`）：

`つよさをみる`

原英文（`src/data/trade.h`，`fe570a7e5^`）：

`SUMMARY`

当前美版（`src/data/trade.h`）：

`查看能力`

### 13245 — sText_Trade

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`交换`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x08300AD8`）：

`こうかんにだす`

Wokann日文（`src/data/trade.h`）：

`こうかんにだす`

原英文（`src/data/trade.h`，`fe570a7e5^`）：

`TRADE`

当前美版（`src/data/trade.h`）：

`交换`

### 13246 — sText_Trade2

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`交换`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x08300B1D`）：

`こうかんにだす`

Wokann日文（`src/data/trade.h`）：

`こうかんにだす`

原英文（`src/data/trade.h`，`fe570a7e5^`）：

`TRADE`

当前美版（`src/data/trade.h`）：

`交换`

### 13247 — sText_TheTradeHasBeenCanceled

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`{FC_01 02}{FC_02 01}{FC_03 03}宝可梦交换\n已中止。`

文件：`patch/batches/438_checklist_controls_and_gambler.json`。

原日文（`0x08300B59`）：

`{BYTE_FC}あい{BYTE_FC}いあ{BYTE_FC}ううこうかんは\nキャンセル　されました!`

Wokann日文（`src/data/trade.h`）：

`{COLOR 0x02}{HIGHLIGHT 0x01}{SHADOW 0x03}こうかんは\nキャンセル　されました！`

原英文（`src/data/trade.h`，`fe570a7e5^`）：

`{COLOR DARK_GRAY}{HIGHLIGHT WHITE}{SHADOW LIGHT_GRAY}The trade has\nbeen canceled.`

当前美版（`src/data/trade.h`）：

`{COLOR DARK_GRAY}{HIGHLIGHT WHITE}{SHADOW LIGHT_GRAY}宝可梦交换\n已中止。`

### 13248 — sText_OnlyPkmnForBattle

结论：**需修复**。

已有移植，不是遗漏。但“最后1只同行的宝可梦”不等于“唯一能战斗的宝可梦”：还可能有其他濒死宝可梦或蛋。

方案：交换这只宝可梦后，\n就没有能战斗的宝可梦了。；保留日版原有颜色控制符。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`最后1只同行的宝可梦\n不能用来交换。`

文件：`patch/batches/438_checklist_controls_and_gambler.json`。

原日文（`0x08300B75`）：

`{BYTE_FC}あい{BYTE_FC}いあ{BYTE_FC}ううそのポケモンを　こうかんすると\nせんとうできなくなっちゃうよ!`

Wokann日文（`src/data/trade.h`）：

`{COLOR 0x02}{HIGHLIGHT 0x01}{SHADOW 0x03}そのポケモンを　こうかんすると\nせんとうできなくなっちゃうよ！`

原英文（`src/data/trade.h`，`fe570a7e5^`）：

`That's your only\nPOKéMON for battle.`

当前美版（`src/data/trade.h`）：

`最后1只同行的宝可梦\n不能用来交换。`

### 13249 — sText_WaitingForYourFriend

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`{FC_01 02}{FC_02 01}{FC_03 03}正在等待对方的回复……\n请稍等片刻。`

文件：`patch/batches/438_checklist_controls_and_gambler.json`。

原日文（`0x08300B9E`）：

`{BYTE_FC}あい{BYTE_FC}いあ{BYTE_FC}ううともだちの　しゅうりょうを\nまっています……`

Wokann日文（`src/data/trade.h`）：

`{COLOR 0x02}{HIGHLIGHT 0x01}{SHADOW 0x03}ともだちの　しゅうりょうを\nまっています⋯⋯`

原英文（`src/data/trade.h`，`fe570a7e5^`）：

`{COLOR DARK_GRAY}{HIGHLIGHT WHITE}{SHADOW LIGHT_GRAY}Waiting for your friend\nto finish…`

当前美版（`src/data/trade.h`）：

`{COLOR DARK_GRAY}{HIGHLIGHT WHITE}{SHADOW LIGHT_GRAY}正在等待对方的回复……\n请稍等片刻。`

### 13250 — sText_AwaitingCommunication

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`{FD_02}！\n正在等待其他玩家连接。`

文件：`patch/batches/439_checklist_common_placeholders.json`。

原日文（`0x082C069C`）：

`{PLACEHOLDER_02}!\nともだちからの　れんらくを　まっています`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`{STR_VAR_1}! Awaiting\ncommunication from another player.`

当前美版（`src/data/union_room.h`）：

`{STR_VAR_1}！\n正在等待其他玩家连接。`

### 13251 — sText_CancelModeWithTheseMembers

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`要放弃以当前成员\n进行{FD_02}模式吗？`

文件：`patch/batches/439_checklist_common_placeholders.json`。

原日文（`0x082C092C`）：

`この　メンバ-で　{PLACEHOLDER_02}を\nするのは　やめますか?`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`Cancel {STR_VAR_1} MODE\nwith these members?`

当前美版（`src/data/union_room.h`）：

`要放弃以当前成员\n进行{STR_VAR_1}模式吗？`

### 13252 — sText_OfferToTradeMon

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`有人想用一只\n等级{DYNAMIC 2}的{DYNAMIC 3}\p与您登记的等级{DYNAMIC 0}\n的{DYNAMIC 1}交换。\p要同意交换吗？`

文件：`patch/batches/468_checklist_union_room.json`。

原日文（`0x82c0e68`）：

`とうろく　していた\nLV{BYTE_F7}　の　{BYTE_F7}あ　と\pLV{BYTE_F7}いの　{BYTE_F7}う　の\nこうかん　もうしこみが　きています\pこうかん　しますか?`

Wokann日文（`src/data/union_room7.h`）：

`とうろく　していた\nLV{DYNAMIC 0}の　{DYNAMIC 1}　と\pLV{DYNAMIC 2}の　{DYNAMIC 3}　の\nこうかん　もうしこみが　きています\pこうかん　しますか？`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`There is an offer to trade your\nregistered Lv. {DYNAMIC 0} {DYNAMIC 1}\pin exchange for a\nLv. {DYNAMIC 2} {DYNAMIC 3}.\pWill you accept this trade\noffer?`

当前美版（`src/data/union_room.h`）：

`有人愿意用一只\n等级{DYNAMIC 0}的{DYNAMIC 1}\p与您登记的等级{DYNAMIC 2}\n的{DYNAMIC 3}交换。\p要同意交换吗？`

### 13253 — sText_TrainerAppearsBusy

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`……\n现在好像正在忙……\p`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C0FE0`）：

`……\nいまは　とりこみちゅうの　ようだ\p`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`……\nThe TRAINER appears to be busy…\p`

当前美版（`src/data/union_room.h`）：

`……\n现在好像正在忙……\p`

### 13254 — sText_ChooseTrainer

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`请选择1位训练家。`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C19CC`）：

`ともだちを　えらんでください`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`Please choose a TRAINER.`

当前美版（`src/data/union_room.h`）：

`请选择1位训练家。`

### 13255 — sText_PlayerHasBeenAskedToRegisterYouPleaseWait

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`正在请{FD_02}\n添加您为成员，请稍等！`

文件：`patch/batches/453_checklist_named_menu_sections.json`。

原日文（`0x082C1C94`）：

`{PLACEHOLDER_02}に　メンバ-　とうろくを\nおねがいしています!　おまちください`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`{STR_VAR_1} has been asked to register\nyou as a member. Please wait.`

当前美版（`src/data/union_room.h`）：

`正在请{STR_VAR_1}\n添加您为成员，请稍等！`

### 13256 — sText_Battle

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`对战`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1D38`）：

`たいせん`

Wokann日文（`src/data/union_room8i.h`）：

`たいせん`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`BATTLE`

当前美版（`src/data/union_room.h`）：

`对战`

### 13257 — sText_Chat2

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`聊天`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1D40`）：

`チャット`

Wokann日文（`src/data/union_room8i.h`）：

`チャット`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`CHAT`

当前美版（`src/data/union_room.h`）：

`聊天`

### 13258 — sText_Greetings

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`问候`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1D48`）：

`あいさつ`

Wokann日文（`src/data/union_room8i.h`）：

`あいさつ`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`GREETINGS`

当前美版（`src/data/union_room.h`）：

`问候`

### 13259 — sText_Exit

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`退出`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1D50`）：

`やめる`

Wokann日文（`src/data/union_room8i.h`）：

`やめる`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`EXIT`

当前美版（`src/data/union_room.h`）：

`退出`

### 13260 — sText_Exit2

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`退出`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1D54`）：

`とじる`

Wokann日文（`src/data/union_room8i.h`）：

`とじる`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`EXIT`

当前美版（`src/data/union_room.h`）：

`退出`

### 13261 — sText_Info

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`听说明`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1D58`）：

`せつめいをきく`

Wokann日文（`src/data/union_room8i.h`）：

`せつめいをきく`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`INFO`

当前美版（`src/data/union_room.h`）：

`听说明`

### 13262 — sText_NameWantedOfferLv

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`名字{FC_13 3c}想要{FC_13 6e}给出{FC_13 c6}等级`

文件：`patch/batches/438_checklist_controls_and_gambler.json`。

原日文（`0x082C1D60`）：

`なまえ　　　　ほしいタイプ　あげるポケモン　　レベル`

Wokann日文（`src/data/union_room8j.h`）：

`なまえ　　　　ほしいタイプ　あげるポケモン　　レベル`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`NAME{CLEAR_TO 60}WANTED{CLEAR_TO 110}OFFER{CLEAR_TO 198}LV.`

当前美版（`src/data/union_room.h`）：

`名字{CLEAR_TO 60}想要{CLEAR_TO 110}给出{CLEAR_TO 198}等级`

### 13263 — sText_SingleBattle

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`单打对战`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1D7C`）：

`シングルバトル`

Wokann日文（`src/data/union_room8j.h`）：

`シングルバトル`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`SINGLE BATTLE`

当前美版（`src/data/union_room.h`）：

`单打对战`

### 13264 — sText_DoubleBattle

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`双打对战`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1D84`）：

`ダブルバトル`

Wokann日文（`src/data/union_room8j.h`）：

`ダブルバトル`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`DOUBLE BATTLE`

当前美版（`src/data/union_room.h`）：

`双打对战`

### 13265 — sText_MultiBattle

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`多人对战`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1D8C`）：

`マルチバトル`

Wokann日文（`src/data/union_room8j.h`）：

`マルチバトル`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`MULTI BATTLE`

当前美版（`src/data/union_room.h`）：

`多人对战`

### 13266 — sText_Chat

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`聊天`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1DA0`）：

`チャット`

Wokann日文（`src/data/union_room8j.h`）：

`チャット`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`CHAT`

当前美版（`src/data/union_room.h`）：

`聊天`

### 13267 — sText_Cards

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`卡片`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1DA8`）：

`カ-ド`

Wokann日文（`src/data/union_room8j.h`）：

`カード`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`CARDS`

当前美版（`src/data/union_room.h`）：

`卡片`

### 13268 — sText_WonderCards

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`神秘卡片`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1DAC`）：

`ふしぎなカ-ド`

Wokann日文（`src/data/union_room8j.h`）：

`ふしぎなカード`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`WONDER CARDS`

当前美版（`src/data/union_room.h`）：

`神秘卡片`

### 13269 — sText_WonderNews

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`神秘新闻`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1DB4`）：

`ふしぎなニュ-ス`

Wokann日文（`src/data/union_room8j.h`）：

`ふしぎなニュース`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`WONDER NEWS`

当前美版（`src/data/union_room.h`）：

`神秘新闻`

### 13270 — sText_BerryCrush

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`树果粉碎`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1DCC`）：

`きのみクラッシュ`

Wokann日文（`src/data/union_room8j.h`）：

`きのみクラッシュ`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`BERRY CRUSH`

当前美版（`src/data/union_room.h`）：

`树果粉碎`

### 13271 — sText_RecordCorner

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`记录角`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1DF0`）：

`レコ-ドコ-ナ-`

Wokann日文（`src/data/union_room8j.h`）：

`レコードコーナー`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`RECORD CORNER`

当前美版（`src/data/union_room.h`）：

`记录角`

### 13272 — sText_CoolContest

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`帅气华丽大赛`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1DFC`）：

`かっこよさコンテスト`

Wokann日文（`src/data/union_room8j.h`）：

`かっこよさコンテスト`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`COOL CONTEST`

当前美版（`src/data/union_room.h`）：

`帅气华丽大赛`

### 13273 — sText_BeautyContest

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`美丽华丽大赛`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1E08`）：

`うつくしさコンテスト`

Wokann日文（`src/data/union_room8j.h`）：

`うつくしさコンテスト`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`BEAUTY CONTEST`

当前美版（`src/data/union_room.h`）：

`美丽华丽大赛`

### 13274 — sText_CuteContest

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`可爱华丽大赛`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1E14`）：

`かわいさコンテスト`

Wokann日文（`src/data/union_room8j.h`）：

`かわいさコンテスト`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`CUTE CONTEST`

当前美版（`src/data/union_room.h`）：

`可爱华丽大赛`

### 13275 — sText_SmartContest

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`聪明华丽大赛`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1E20`）：

`かしこさコンテスト`

Wokann日文（`src/data/union_room8j.h`）：

`かしこさコンテスト`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`SMART CONTEST`

当前美版（`src/data/union_room.h`）：

`聪明华丽大赛`

### 13276 — sText_ToughContest

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`强壮华丽大赛`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082C1E2C`）：

`たくましさコンテスト`

Wokann日文（`src/data/union_room8j.h`）：

`たくましさコンテスト`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`TOUGH CONTEST`

当前美版（`src/data/union_room.h`）：

`强壮华丽大赛`

### 13277 — sText_BattleTowerLv50

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`对战塔Lv. 50级`

文件：`patch/batches/479_checklist_frontier_records2.json`。

原日文（`0x82c1e38`）：

`バトルタワ-　レベル50`

Wokann日文（`src/data/union_room8j.h`）：

`　バトルタワー　レベル50`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`BATTLE TOWER LV. 50`

当前美版（`src/data/union_room.h`）：

`对战塔Lv. 50级`

### 13278 — sText_BattleTowerOpenLv

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`对战塔自由等级`

文件：`patch/batches/479_checklist_frontier_records2.json`。

原日文（`0x82c1e48`）：

`バトルタワ-　オ-プンレベル`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`BATTLE TOWER OPEN LEVEL`

当前美版（`src/data/union_room.h`）：

`对战塔自由等级`

### 13279 — sText_TrainerCardInfoPage1

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`这是{DYNAMIC 0} {DYNAMIC 1}的\n训练家卡……\l{DYNAMIC 2}\p图鉴：{DYNAMIC 3}\n时间：{DYNAMIC 4}：{DYNAMIC 5}\p`

文件：`patch/batches/446_checklist_reviewed_card_quiz_slots.json`。

原日文（`0x082C1F1C`）：

`{BYTE_F7}　の　{BYTE_F7}あの\nトレ-ナ-カ-ドを　みせてもらった\l{BYTE_F7}い\pポケモンずかん　{BYTE_F7}う\nプレイ　じかん　{BYTE_F7}え:{BYTE_F7}お\p`

Wokann日文（`src/data/union_room8l.h`）：

`{DYNAMIC 0}の　{DYNAMIC 1}の\nトレーナーカードを　みせてもらった\l{DYNAMIC 2}\pポケモンずかん　{DYNAMIC 3}\nプレイ　じかん　{DYNAMIC 4}:{DYNAMIC 5}\p`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`This is {DYNAMIC 0} {DYNAMIC 1}'s\nTRAINER CARD…\l{DYNAMIC 2}\pPOKéDEX: {DYNAMIC 3}\nTIME:    {DYNAMIC 4}:{DYNAMIC 5}\p`

当前美版（`src/data/union_room.h`）：

`这是{DYNAMIC 0} {DYNAMIC 1}的\n训练家卡……\l{DYNAMIC 2}\p图鉴：{DYNAMIC 3}\n时间：{DYNAMIC 4}：{DYNAMIC 5}\p`

### 13280 — sText_TrainerCardInfoPage2

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

` 对战：胜：{DYNAMIC 0} 负：{DYNAMIC 2}\n交换次数：{DYNAMIC 3}\p“{DYNAMIC 4} {DYNAMIC 5}\n{DYNAMIC 6} {DYNAMIC 7}”\p`

文件：`patch/batches/446_checklist_reviewed_card_quiz_slots.json`。

原日文（`0x082C1F54`）：

`たいせん　かち{BYTE_F7}　　まけ{BYTE_F7}い\nこうかん　{BYTE_F7}うかい\p‘{BYTE_F7}え　{BYTE_F7}お\n　{BYTE_F7}か　{BYTE_F7}き\p`

Wokann日文（`src/data/union_room8l.h`）：

`たいせん　かち{DYNAMIC 0}　まけ{DYNAMIC 2}\nこうかん　{DYNAMIC 3}かい\p‘{DYNAMIC 4}　{DYNAMIC 5}\n　{DYNAMIC 6}　{DYNAMIC 7}\p${DYNAMIC 1}‘これからも　よろしく！{PAUSE 60}$　　{DYNAMIC 1}‘これからも　よろしくね！{PAUSE 60}`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`BATTLES: WINS: {DYNAMIC 0}  LOSSES: {DYNAMIC 2}\nTRADES: {DYNAMIC 3}\p“{DYNAMIC 4} {DYNAMIC 5}\n{DYNAMIC 6} {DYNAMIC 7}”\p`

当前美版（`src/data/union_room.h`）：

` 对战：胜：{DYNAMIC 0} 负：{DYNAMIC 2}\n交换次数：{DYNAMIC 3}\p“{DYNAMIC 4} {DYNAMIC 5}\n{DYNAMIC 6} {DYNAMIC 7}”\p`

### 13281 — sText_GladToMeetYouMale

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`{DYNAMIC 1}：很高兴认识你！{FC_08 3c}`

文件：`patch/batches/468_checklist_union_room.json`。

原日文（`0x82c1f7c`）：

`{BYTE_F7}あ‘これからも　よろしく!{BYTE_FC}くざ`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`{DYNAMIC 1}: Glad to have met you!{PAUSE 60}`

当前美版（`src/data/union_room.h`）：

`{DYNAMIC 1}：很高兴认识你！{PAUSE 60}`

### 13282 — sText_GladToMeetYouFemale

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`{DYNAMIC 1}：很高兴认识你！{FC_08 3c}`

文件：`patch/batches/468_checklist_union_room.json`。

原日文（`0x82c1f90`）：

`{BYTE_F7}あ‘これからも　よろしくね!{BYTE_FC}くざ`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`{DYNAMIC 1}: Glad to meet you!{PAUSE 60}`

当前美版（`src/data/union_room.h`）：

`{DYNAMIC 1}：很高兴认识你！{PAUSE 60}`

### 13283 — sText_FinishedCheckingPlayersTrainerCard

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`{DYNAMIC 1}的训练家卡\n确认完毕。{FC_08 3c}`

文件：`patch/batches/446_checklist_reviewed_card_quiz_slots.json`。

原日文（`0x082C1FAC`）：

`{BYTE_F7}あの　トレ-ナ-カ-ドを\nみおわった!{BYTE_FC}くざ`

Wokann日文（`src/data/union_room8l.h`）：

`{DYNAMIC 1}の　トレーナーカードを\nみおわった！{PAUSE 60}`

原英文（`src/data/union_room.h`，`fe570a7e5^`）：

`Finished checking {DYNAMIC 1}'s\nTRAINER CARD.{PAUSE 60}`

当前美版（`src/data/union_room.h`）：

`{DYNAMIC 1}的训练家卡\n确认完毕。{PAUSE 60}`

### 13284 — gText_PokemartSign

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`“挑选一些便利的道具吧！”\n友好商店`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x082439D6`）：

`べんりなどうぐ　いろいろ　あります\n‘フレンドリィショップ’`

Wokann日文（`data/event_scripts.s`）：

`べんりなどうぐ　いろいろ　あります\n‘フレンドリィショップ'$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`“Selected items for your convenience!”\nPOKéMON MART$`

当前美版（`data/event_scripts.s`）：

`“挑选一些便利的道具吧！”\n友好商店$`

### 13285 — gText_PokemonCenterSign

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`“让您疲劳的伙伴们恢复活力！”\n宝可梦中心`

文件：`patch/batches/450_checklist_verified_event_msgboxes.json`。

原日文（`0x082439F5`）：

`つかれた　ポケモンも　ひとやすみ!\n‘ポケモンセンタ-’`

Wokann日文（`data/event_scripts.s`）：

`つかれた　ポケモンも　ひとやすみ！\n‘ポケモンセンター'$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`“Rejuvenate your tired partners!”\nPOKéMON CENTER$`

当前美版（`data/event_scripts.s`）：

`“让您疲劳的伙伴们恢复活力！”\n宝可梦中心$`

### 13286 — gText_MomOrDadMightLikeThisProgram

结论：**需修复**。

已有移植，不是遗漏。ばんぐみ / program 在这里是电视节目，不是游戏。

方案：仅将“喜欢的游戏”改为“喜欢的节目”，保留父母动态显示变量。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`也许是{FD_02}喜欢的游戏\n…… …… …… …… …… …… …… ……\p该走了！`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243A12`）：

`{PLACEHOLDER_02}が　すきそうな　ばんぐみをやってる!\n…………………………………………………\pさきを　いそがなきゃ!`

Wokann日文（`data/event_scripts.s`）：

`{STR_VAR_1}が　すきそうな　ばんぐみをやってる！\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\pさきを　いそがなきゃ！$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`{STR_VAR_1} might like this program.\n… … … … … … … … … … … … … … … …\pBetter get going!$`

当前美版（`data/event_scripts.s`）：

`也许是{STR_VAR_1}喜欢的游戏\n…… …… …… …… …… …… …… ……\p该走了！$`

### 13287 — gText_WhichFloorWouldYouLike

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`欢迎来到水静百货。\p要去几层？`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243A47`）：

`ミナモ　デパ-トへ　ようこそ!\pなんかいへ　いきますか?`

Wokann日文（`data/event_scripts.s`）：

`ミナモ　デパートへ　ようこそ！\pなんかいへ　いきますか？$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`Welcome to LILYCOVE DEPARTMENT STORE.\pWhich floor would you like?$`

当前美版（`data/event_scripts.s`）：

`欢迎来到水静百货。\p要去几层？$`

### 13288 — gText_SandstormIsVicious

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`沙暴太强了，\n走不过去。`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243A64`）：

`さばくの　すなあらしが　ひどくて\nさきに　すすめない!`

Wokann日文（`data/event_scripts.s`）：

`さばくの　すなあらしが　ひどくて\nさきに　すすめない！$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`The sandstorm is vicious.\nIt's impossible to keep going.$`

当前美版（`data/event_scripts.s`）：

`沙暴太强了，\n走不过去。$`

### 13289 — gText_SelectWithoutRegisteredItem

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`包包里的道具可以\n登录到SELECT上，方便使用。`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243A80`）：

`バッグに　いれてある　どうぐを\nべんりボタンに　とうろく　できます`

Wokann日文（`data/event_scripts.s`）：

`バッグに　いれてある　どうぐを\nべんりボタンに　とうろく　できます$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`An item in the BAG can be\nregistered to SELECT for easy use.$`

当前美版（`data/event_scripts.s`）：

`包包里的道具可以\n登录到SELECT上，方便使用。$`

### 13290 — gText_PokemonTrainerSchoolEmail

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`有一封宝可梦训练家\n学校来的电子邮件。\p…… …… ……\p1只宝可梦最多可以学4个招式。\p训练家的专业程度就可以从其\n为宝可梦所选择的招式中看出来。\p…… …… ……`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243AA2`）：

`パソコンに\nポケモン　トレ-ナ-　こうざの\lメ-ルが　きている!\p……　……　……\pポケモンが　おぼえられる　わざは　4つ!\pどんな　わざを　おぼえさせるかで\nトレ-ナ-の　じつりょくが　とわれます!\p……　……　……`

Wokann日文（`data/event_scripts.s`）：

`パソコンに\nポケモン　トレーナー　こうざの\lメールが　きている！\p⋯⋯　⋯⋯　⋯⋯\pポケモンが　おぼえられる　わざは　4つ！\pどんな　わざを　おぼえさせるかで\nトレーナーの　じつりょくが　とわれます！\p⋯⋯　⋯⋯　⋯⋯$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`There's an e-mail from POKéMON TRAINER\nSCHOOL.\p… … … … … …\pA POKéMON may learn up to four moves.\pA TRAINER's expertise is tested on the\nmove sets chosen for POKéMON.\p… … … … … …$`

当前美版（`data/event_scripts.s`）：

`有一封宝可梦训练家\n学校来的电子邮件。\p…… …… ……\p1只宝可梦最多可以学4个招式。\p训练家的专业程度就可以从其\n为宝可梦所选择的招式中看出来。\p…… …… ……$`

### 13291 — gText_PlayerHouseBootPC

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`{FD_01}登录了电脑。`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243B10`）：

`{PLACEHOLDER_01}は　パソコンの\nスイッチを　いれた!`

Wokann日文（`data/event_scripts.s`）：

`{PLAYER}は　パソコンの\nスイッチを　いれた！$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`{PLAYER} booted up the PC.$`

当前美版（`data/event_scripts.s`）：

`{PLAYER}登录了电脑。$`

### 13292 — gText_PokeblockLinkCanceled

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`已取消连接。`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243B25`）：

`つうしんは　キャンセルされました`

Wokann日文（`data/event_scripts.s`）：

`つうしんは　キャンセルされました$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`The link was canceled.$`

当前美版（`data/event_scripts.s`）：

`已取消连接。$`

### 13293 — gText_PlayerWhitedOut

结论：**需修复**。

已有移植，不是遗漏。第一句叹号被移到第二页开头，形成“！玩家……”；日英原文的叹号都在第一句末。

方案：将“战斗的宝可梦\p！”改为“战斗的宝可梦！\p”，不改其他分页和玩家名路径。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`{FD_01}没有可以\n战斗的宝可梦\p！{FD_01}昏迷了！`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243B4E`）：

`{PLACEHOLDER_01}の　てもとには\nたたかえるポケモンが　もういない!\p{PLACEHOLDER_01}は\nめのまえが　まっくらに　なった!`

Wokann日文（`data/event_scripts.s`）：

`{PLAYER}の　てもとには\nたたかえるポケモンが　もういない！\p{PLAYER}は\nめのまえが　まっくらに　なった！$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`{PLAYER} is out of usable\nPOKéMON!\p{PLAYER} whited out!$`

当前美版（`data/event_scripts.s`）：

`{PLAYER}没有可以\n战斗的宝可梦\p！{PLAYER}昏迷了！$`

### 13294 — gText_RegisteredTrainerinPokeNav

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`把{FD_02} {FD_03}\n登记到宝可导航里了。`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243B7F`）：

`{PLACEHOLDER_02}の　{PLACEHOLDER_03}を\nポケナビに　とうろく　した!`

Wokann日文（`data/event_scripts.s`）：

`{STR_VAR_1}の　{STR_VAR_2}を\nポケナビに　とうろく　した！$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`Registered {STR_VAR_1} {STR_VAR_2}\nin the POKéNAV.$`

当前美版（`data/event_scripts.s`）：

`把{STR_VAR_1} {STR_VAR_2}\n登记到宝可导航里了。$`

### 13295 — gText_ComeBackWithSecretPower

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`你知道招式学习器秘密之力吗？\p我们这些人都喜欢\n招式学习器秘密之力。\p我们的成员之一会把它送给你，\n拿到之后就回来给我看看吧。\p我们会让你成为我们之中的一员，\n还可以秘密卖给你些道具。`

文件：`patch/batches/434_checklist_verified_objects.json`。

原日文（`0x08243B96`）：

`‘ひみつのちから’って\nわざマシン　しってる?\pおれら　わざマシン　‘ひみつのちから’が\nだいすき　なんだ\pおれらの　メンバ-が　どこかで　くれるから\nそれを　もらったら　また　おいで!\pきみも　メンバ-として\nひみつで　いいものを　うってあげるよ`

Wokann日文（`data/event_scripts.s`）：

`‘ひみつのちから'って\nわざマシン　しってる？\pおれら　わざマシン　‘ひみつのちから'が\nだいすき　なんだ\pおれらの　メンバーが　どこかで　くれるから\nそれを　もらったら　また　おいで！\pきみも　メンバーとして\nひみつで　いいものを　うってあげるよ$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`Do you know the TM SECRET POWER?\pOur group, we love the TM SECRET\nPOWER.\pOne of our members will give it to you.\nCome back and show me if you get it.\pWe'll accept you as a member and sell\nyou good stuff in secrecy.$`

当前美版（`data/event_scripts.s`）：

`你知道招式学习器秘密之力吗？\p我们这些人都喜欢\n招式学习器秘密之力。\p我们的成员之一会把它送给你，\n拿到之后就回来给我看看吧。\p我们会让你成为我们之中的一员，\n还可以秘密卖给你些道具。$`

### 13296 — gText_PokerusExplanation

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`交给我的宝可梦\n似乎附上了宝可病毒。\p详细情况不太清楚，\n不过据说，所谓宝可病毒是一种\l附着在宝可梦身上的微小生命体。\p而且在病毒附着期间\n宝可梦好像会成长得特别快。`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243C13`）：

`おあずかりした　ポケモンに\nポケルスが　ついて　いるようです\pくわしいことは　わかって　いないのですが\nポケルスと　いうのは　ポケモンに　くっつく\lちいさな　せいめいたいで\lこれが　ついている　あいだ\lポケモンが　よく　そだつ　みたいです`

Wokann日文（`data/event_scripts.s`）：

`おあずかりした　ポケモンに\nポケルスが　ついて　いるようです\pくわしいことは　わかって　いないのですが\nポケルスと　いうのは　ポケモンに　くっつく\lちいさな　せいめいたいで\lこれが　ついている　あいだ\lポケモンが　よく　そだつ　みたいです$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`Your POKéMON may be infected with\nPOKéRUS.\pLittle is known about the POKéRUS\nexcept that they are microscopic life-\lforms that attach to POKéMON.\pWhile infected, POKéMON are said to\ngrow exceptionally well.$`

当前美版（`data/event_scripts.s`）：

`交给我的宝可梦\n似乎附上了宝可病毒。\p详细情况不太清楚，\n不过据说，所谓宝可病毒是一种\l附着在宝可梦身上的微小生命体。\p而且在病毒附着期间\n宝可梦好像会成长得特别快。$`

### 13297 — gText_DoorOpenedFarAway

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`似乎听到了远处\n某扇门打开了的声音。`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243CBE`）：

`どこか　とおくの　とびらが\nひらいたような　おとだ……`

Wokann日文（`data/event_scripts.s`）：

`どこか　とおくの　とびらが\nひらいたような　おとだ⋯⋯$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`It sounded as if a door opened\nsomewhere far away.$`

当前美版（`data/event_scripts.s`）：

`似乎听到了远处\n某扇门打开了的声音。$`

### 13298 — gText_BigHoleInTheWall

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`墙上有一个大洞。`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243CDA`）：

`かべに　おおきな　あなが　あいている!`

Wokann日文（`data/event_scripts.s`）：

`かべに　おおきな　あなが　あいている！$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`There is a big hole in the wall.$`

当前美版（`data/event_scripts.s`）：

`墙上有一个大洞。$`

### 13299 — gText_SorryWirelessClubAdjustments

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`非常抱歉，\n宝可梦无线俱乐部\l系统正在调整。`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243CEE`）：

`もうしわけ　ございません\nポケモン　ワイヤレス　クラブは\lただいま　ちょうせいちゅう　です`

Wokann日文（`data/event_scripts.s`）：

`もうしわけ　ございません\nポケモン　ワイヤレス　クラブは\lただいま　ちょうせいちゅう　です$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`I'm terribly sorry.\nThe POKéMON WIRELESS CLUB is\lundergoing adjustments now.$`

当前美版（`data/event_scripts.s`）：

`非常抱歉，\n宝可梦无线俱乐部\l系统正在调整。$`

### 13300 — gText_UndergoingAdjustments

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`似乎正在进行\n调整的样子……`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243D1C`）：

`ちょうせいちゅうの　ようだ`

Wokann日文（`data/event_scripts.s`）：

`ちょうせいちゅうの　ようだ$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`It appears to be undergoing\nadjustments…$`

当前美版（`data/event_scripts.s`）：

`似乎正在进行\n调整的样子……$`

### 13301 — gText_PlayerHandedOverTheItem

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`{FD_01}\n交出了{FD_02}。`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243D82`）：

`{PLACEHOLDER_01}は\n{PLACEHOLDER_02}を　わたした!`

Wokann日文（`data/event_scripts.s`）：

`{PLAYER}は\n{STR_VAR_1}を　わたした！$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`{PLAYER} handed over the\n{STR_VAR_1}.$`

当前美版（`data/event_scripts.s`）：

`{PLAYER}\n交出了{STR_VAR_1}。$`

### 13302 — gText_ThankYouForAccessingMysteryGift

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`感谢连接\n神秘礼物系统。`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243D90`）：

`ふしぎな　おくりものを　ごりよう\nいただき　ありがとう　ございます!`

Wokann日文（`data/event_scripts.s`）：

`ふしぎな　おくりものを　ごりよう\nいただき　ありがとう　ございます！$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`Thank you for accessing the\nMYSTERY GIFT System.$`

当前美版（`data/event_scripts.s`）：

`感谢连接\n神秘礼物系统。$`

### 13303 — gText_PlayerFoundOneTMHM

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`{FD_01}找到了{FD_02}\n“{FD_03}”！`

文件：`patch/batches/439_checklist_common_placeholders.json`。

原日文（`0x08243DB3`）：

`{PLACEHOLDER_01}は　{PLACEHOLDER_02}\n‘{PLACEHOLDER_03}’を　みつけた!`

Wokann日文（`data/event_scripts.s`）：

`{PLAYER}は　{STR_VAR_1}\n‘{STR_VAR_2}'を　みつけた！$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`{PLAYER} found one {STR_VAR_1}\n{STR_VAR_2}!$`

当前美版（`data/event_scripts.s`）：

`{PLAYER}找到了{STR_VAR_1}\n“{STR_VAR_2}”！$`

### 13304 — gText_Sudowoodo_Attacked

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`奇怪的树不喜欢\n吼吼鲸洒水壶！\p奇怪的树攻击了过来！`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243DC6`）：

`おかしな　きは\nホエルコじょうろを　いやがっている!\pおかしな　きが　おそいかかってきた!`

Wokann日文（`data/event_scripts.s`）：

`おかしな　きは\nホエルコじょうろを　いやがっている！\pおかしな　きが　おそいかかってきた！$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`The weird tree doesn't like the\nWAILMER PAIL!\pThe weird tree attacked!$`

当前美版（`data/event_scripts.s`）：

`奇怪的树不喜欢\n吼吼鲸洒水壶！\p奇怪的树攻击了过来！$`

### 13305 — gText_LegendaryFlewAway

结论：**已有移植**。

原报告说缺失，但当前已找到实际 JP 定义及原 ROM 引用；见下列当前文本、文件、original地址。不是单凭US符号推断。

方案：不因原报告缺失结论重复移植。

原报告问题：

补丁批次源（batches/*.json 与 texts.json manifest）中无该符号的中文文本：输入 trans_5.json 的 chs_text 为空，补丁源全文检索确认无中文（64 条之一）。无法做四方对照中的“补丁中文”一项；现按 JP/EN/US-CHS 三方给出，待确认补丁是否应补译或符号归属。

当前日版：

`{FD_02}消失不见了……`

文件：`patch/batches/432_checklist_scripts.json`。

原日文（`0x08243DF4`）：

`{PLACEHOLDER_02}は\nどこかへ　とびさって　いった!`

Wokann日文（`data/event_scripts.s`）：

`{STR_VAR_1}は\nどこかへ　とびさって　いった！$`

原英文（`data/event_scripts.s`，`fe570a7e5^`）：

`The {STR_VAR_1} flew away!$`

当前美版（`data/event_scripts.s`）：

`{STR_VAR_1}消失不见了……$`

### 13396 — gMoveNames[12]

结论：**译名政策项**。

报告建议改用另一套招式译名，但不能只靠词面直译判定专名错误；本轮不把全局译名迁移混入事实/参数修复。若决定统一新译名，须连同全部招式名、说明引用和上下游一起审查。

方案：本轮不改；不声称当前名字为任何时期官方译名。

原报告问题：

JP「ハサミギロチン」为“钳+断头台”（ギロチン=guillotine，断头台）之意，EN「Guillotine」同样为断头台；官方中文译名「断头钳」。补丁中文与美版汉化均为「极落钳」，ギロチン被误转写为“极落”，语义完全丢失且无依据。

当前日版：

`极落钳`

文件：`patch/move_names.json`。

### 13450 — gMoveNames[66]

结论：**译名政策项**。

报告建议改用另一套招式译名，但不能只靠词面直译判定专名错误；本轮不把全局译名迁移混入事实/参数修复。若决定统一新译名，须连同全部招式名、说明引用和上下游一起审查。

方案：本轮不改；不声称当前名字为任何时期官方译名。

原报告问题：

JP「じごくぐるま」中「じごく」=地狱（hell），招式为投掷技“地狱翻滚”；EN「Submission」为擒抱降服技，官方中文「地狱翻滚」。补丁中文与美版汉化均为「深渊翻滚」，将“地狱”（じごく）误译为“深渊”（abyss），语义偏差。

当前日版：

`深渊翻滚`

文件：`patch/move_names.json`。
