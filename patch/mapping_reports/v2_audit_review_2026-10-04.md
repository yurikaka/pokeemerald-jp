# v2 审计逐条核验与修复（2026-10-04）

## 范围与限制

输入14780条；236条 ERROR / NEEDS_ATTENTION 全部逐条判定，125条修复（122条涉及日版、3条仅美版）。
1288条 UNTRANSPLANTED 完成映射/调用分类：此前待追踪的143条均有逐项证据，新增修复15条审计记录，另补日版简易聊天的7字词语限制提示。
合计140条审计记录执行修复。弃用定义、无消费者数组/函数、区域差异及非显示比较常量不盲目覆盖。
OK项只核验映射，不代表重新完成语义审查；历史休眠脚本判定保留其证据与原始ROM未改检查，不冒充新语义审查。没有运行模拟器。

## 当前分类

- `mapping_verified_semantics_not_reaudited`：12794
- `accurate_clarification`：24
- `fixed_verified`：122
- `already_fixed`：4
- `localization_choice`：3
- `regional_difference`：1
- `fixed_us_only`：3
- `equivalent_wording`：2
- `reported_ok_not_independently_verified`：462
- `mapping_artifact`：3
- `no_text`：2
- `intentional_adaptation`：6
- `dormant_original_retained`：191
- `already_ported_verified`：1018
- `regional_no_counterpart_verified`：14
- `already_ported_alias_verified`：9
- `unused_definition_verified`：81
- `non_display_comparison_verified`：1
- `fixed_consumer_verified`：10
- `already_ported_graphics_verified`：11
- `regional_display_equivalent_verified`：3
- `regional_ui_already_localized`：2
- `unused_table_verified`：6
- `unused_function_verified`：1
- `fixed_graphics_verified`：5
- `unsupported_terminology_claim`：2

## 未移植项分类

- `dormant_original_retained`：191
- `already_ported_verified`：954
- `regional_no_counterpart_verified`：14
- `already_ported_alias_verified`：9
- `unused_definition_verified`：81
- `non_display_comparison_verified`：1
- `fixed_consumer_verified`：10
- `already_ported_graphics_verified`：11
- `regional_display_equivalent_verified`：3
- `regional_ui_already_localized`：2
- `unused_table_verified`：6
- `unused_function_verified`：1
- `fixed_graphics_verified`：5

## 问题项逐条判定

### CSV 第 77 行 · ability_move / 37 · 

判定：`accurate_clarification`

理由：描述符合第三世代实际机制；有用的准确说明不为逐字复刻模糊原文而删除。

日文：

```text
こうげきりょくが　たかい
```

英文：

```text
Raises ATTACK.
```

报告原中文：

```text
物理攻击的威力会变为2倍
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 77,
    "symbol": "",
    "domain": "ability_move",
    "idx": "37",
    "reason": "描述符合第三世代实际机制；有用的准确说明不为逐字复刻模糊原文而删除。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/ability_descriptions.json",
      "table": "ChsAbilityDescriptions",
      "index": 37,
      "text": "物理攻击的威力会变为2倍",
      "rom_address": "0x0909CAB4",
      "encoded_sha256": "49b95025091ad86cce224b6ec4bed707063616d8e80d1f740d0f49fb19d0e49f",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 151 行 · ability_move / 74 · 

判定：`accurate_clarification`

理由：描述符合第三世代实际机制；有用的准确说明不为逐字复刻模糊原文而删除。

日文：

```text
こうげきりょくが　たかい
```

英文：

```text
Raises ATTACK.
```

报告原中文：

```text
物理攻击的威力会变为2倍
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 151,
    "symbol": "",
    "domain": "ability_move",
    "idx": "74",
    "reason": "描述符合第三世代实际机制；有用的准确说明不为逐字复刻模糊原文而删除。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/ability_descriptions.json",
      "table": "ChsAbilityDescriptions",
      "index": 74,
      "text": "物理攻击的威力会变为2倍",
      "rom_address": "0x0909CF54",
      "encoded_sha256": "49b95025091ad86cce224b6ec4bed707063616d8e80d1f740d0f49fb19d0e49f",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 519 行 · ability_move / 180 · 

判定：`fixed_verified`

理由：第三世代怨恨源码随机减少2～5PP；原文未限定4PP。

日文：

```text
あいてがだしたわざをうらんで
そのわざポイントをへらしてしまう
```

英文：

```text
Spitefully cuts the PP
of the foe's last move.
```

报告原中文：

```text
怨恨对手最后用的招式，
减少4PP该招式。
```

修复前实际中文：

```text
怨恨对手最后用的招式，
减少4PP该招式。
```

最终中文：

```text
怨恨对手最后用的招式，
减少该招式的PP。
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/text/move_descriptions.h",
        "text": "怨恨对手最后用的招式，\n减少该招式的PP。"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/move_descriptions.json",
      "table": "ChsMoveDescriptions",
      "index": 180,
      "text": "怨恨对手最后用的招式，\n减少该招式的PP。",
      "rom_address": "0x09099574",
      "encoded_sha256": "c16638fbd690fdd747601caa7c3b2e85f104638d34b08618aa07f9980e04b9b4",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 613 行 · ability_move / 227 · 

判定：`already_fixed`

理由：67a5276 / 6ffae39ea 已修复再来一次说明。

日文：

```text
てきがさいごにつかったわざを
2-6かいれんぞくでださせる
```

英文：

```text
Makes the foe repeat its
last move over 2 to 6 turns.
```

报告原中文：

```text
让对手接受再来一次，
在3～6回合内重复最后的招式。
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 613,
    "symbol": "",
    "domain": "ability_move",
    "idx": "227",
    "reason": "67a5276 / 6ffae39ea 已修复再来一次说明。",
    "action": "already_fixed"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/move_descriptions.json",
      "table": "ChsMoveDescriptions",
      "index": 227,
      "text": "让对手接受再来一次，\n在2～6回合内重复最后的招式。",
      "rom_address": "0x0909A134",
      "encoded_sha256": "38186afa131556efd48697db2e38841337f3a7e9afa6467e3f409bcfa12d8a76",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 725 行 · ability_move / 283 · 

判定：`accurate_clarification`

理由：描述符合第三世代实际机制；有用的准确说明不为逐字复刻模糊原文而删除。

日文：

```text
じぶんのたいりょくがあいてより
すくないほどダメ-ジをあたえる
```

英文：

```text
Gains power if the user's HP
is lower than the foe's HP.
```

报告原中文：

```text
给予伤害，使对手的HP
变得和自己的HP一样。
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 725,
    "symbol": "",
    "domain": "ability_move",
    "idx": "283",
    "reason": "描述符合第三世代实际机制；有用的准确说明不为逐字复刻模糊原文而删除。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/move_descriptions.json",
      "table": "ChsMoveDescriptions",
      "index": 283,
      "text": "给予伤害，使对手的HP\n变得和自己的HP一样。",
      "rom_address": "0x0909AF34",
      "encoded_sha256": "5933e18e7ea4fe36190bbbe54f7d2d2192f72fc50038cb5d3380c85d383a905d",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 817 行 · ability_move / 329 · 

判定：`fixed_verified`

理由：移除第三世代不存在的使用者冰属性条件。

日文：

```text
ぜったいれいどでてきをおそう
きまるとせんとうふのうになる
```

英文：

```text
A chilling attack that
causes fainting if it hits.
```

报告原中文：

```text
给对手一击昏厥。若冰属性
以外宝可梦使用会难以打中。
```

修复前实际中文：

```text
给对手一击昏厥。若冰属性
以外宝可梦使用会难以打中。
```

最终中文：

```text
以绝对零度攻击对手。
命中后会使对手一击昏厥。
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/text/move_descriptions.h",
        "text": "以绝对零度攻击对手。\n命中后会使对手一击昏厥。"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/move_descriptions.json",
      "table": "ChsMoveDescriptions",
      "index": 329,
      "text": "以绝对零度攻击对手。\n命中后会使对手一击昏厥。",
      "rom_address": "0x0909BAB4",
      "encoded_sha256": "ae7ce5f4bfd061f9fe40db11ee62f7807ac92c82febdd10acd43735da00dfeb1",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 1044 行 · pokedex / 176 · 

判定：`localization_choice`

理由：心灵纯洁的持有者并不排除宝可梦；增补不改变条目核心描述。

日文：

```text
こううんを　もたらす　ポケモンと　いわれている。\nじゅんすいな　こころの　もちぬしを　みつけると\nすがたを　あらわし　しあわせを　わけあたえる。
```

英文：

```text
It is said to be a POKéMON that brings good\nfortune. When it spots someone who is pure\nof heart, a TOGETIC appears and shares its\nhappiness with that person.
```

报告原中文：

```text
据说是会带来幸运的宝可梦。如果发现心灵纯洁的人或宝可梦，\n就会现身并将幸福分给他们。
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 1044,
    "symbol": "",
    "domain": "pokedex",
    "idx": "176",
    "reason": "心灵纯洁的持有者并不排除宝可梦；增补不改变条目核心描述。",
    "action": "localization_choice"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/pokedex_entries.json",
      "table": "ChsPokedexEntries",
      "index": 176,
      "text": "据说是会带来幸运的宝可梦。如果发现心灵纯洁的人或宝可梦，\n就会现身并将幸福分给他们。",
      "rom_address": "0x090A4600",
      "encoded_sha256": "2bb0c42dfbf2349cae4cbd3b7210e17a3faf8a484ba906be2496866d464ec86b",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 1098 行 · pokedex / 230 · 

判定：`fixed_verified`

理由：うずしお / whirlpool 是漩涡，不是海浪。

日文：

```text
ふかい　かいていで　しずかに　ねむる。\nすいめんへ　あがってくるとき　ふねを　のみこむ\nほど　おおきな　うずしおが　はっせいする。
```

英文：

```text
It sleeps quietly, deep on the seafloor.\nWhen it comes up to the surface, it\ncreates a huge whirlpool that can swallow\neven ships.
```

报告原中文：

```text
在深沉的海底里静静地沉睡着。当它浮出水面的时候，会产生足以将船只吞没的巨大海浪。
```

修复前实际中文：

```text
在深沉的海底里静静地沉睡着。当它浮出水面的时候，会产生足以将船只吞没的巨大海浪。
```

最终中文：

```text
在深沉的海底里静静地沉睡着。当它浮出水面的时候，会产生足以将船只吞没的巨大漩涡。
```

证据：

```json
{
  "review": {
    "row_number": 1098,
    "symbol": "",
    "domain": "pokedex",
    "idx": "230",
    "old": "巨大海浪",
    "new": "巨大漩涡",
    "reason": "うずしお / whirlpool 是漩涡，不是海浪。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "gKingdraPokedexText",
    "final_text": "在深沉的海底里静静地沉睡着。当它浮出水面的时候，会产生足以将船只吞没的巨大漩涡。",
    "old_current_text": "在深沉的海底里静静地沉睡着。当它浮出水面的时候，会产生足以将船只吞没的巨大海浪。",
    "changed_files": [
      "patch/pokedex_entries.json",
      "../pokeemerald_us_chs/src/data/pokemon/pokedex_text.h"
    ],
    "us_source_file": "src/data/pokemon/pokedex_text.h",
    "jp_source": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "ふかい　かいていで　しずかに　ねむる。\nすいめんへ　あがってくるとき　ふねを　のみこむ\nほど　おおきな　うずしおが　はっせいする。"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "在深沉的海底里静静地沉睡着。当它浮出水面的时候，会产生足以将船只吞没的巨大漩涡。"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "ふかい　かいていで　しずかに　ねむる。\nすいめんへ　あがってくるとき　ふねを　のみこむ\nほど　おおきな　うずしおが　はっせいする。"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/pokedex_entries.json",
      "table": "ChsPokedexEntries",
      "index": 230,
      "text": "在深沉的海底里静静地沉睡着。当它浮出水面的时候，会产生足以将船只吞没的巨大漩涡。",
      "rom_address": "0x090A5BF8",
      "encoded_sha256": "4453ffd50c3c34fa215e90772d3155d11ee14838dc451eb63e5331fb7700692e",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 1099 行 · pokedex / 231 · 

判定：`fixed_verified`

理由：原文动作目的是纳凉，不是前进。

日文：

```text
ゴマゾウの　おおきな　みみは　うちわの　かわり。\nあつくなると　ぱたぱた　あおいで　すずむ。\nこどもでも　ちからは　とても　つよい。
```

英文：

```text
PHANPY's big ears serve as broad fans.\nWhen it becomes hot, it flaps the ears\nbusily to cool down. Even the young are\nvery strong.
```

报告原中文：

```text
小小象的巨大耳朵可以代替扇子，天气热的时候会啪嗒啪嗒扇动着前进，\n即使是幼年时力气也非常大。
```

修复前实际中文：

```text
小小象的巨大耳朵可以代替扇子，天气热的时候会啪嗒啪嗒扇动着前进，
即使是幼年时力气也非常大。
```

最终中文：

```text
小小象的巨大耳朵可以代替扇子，天气热的时候会啪嗒啪嗒扇动耳朵纳凉，
即使是幼年时力气也非常大。
```

证据：

```json
{
  "review": {
    "row_number": 1099,
    "symbol": "",
    "domain": "pokedex",
    "idx": "231",
    "old": "会啪嗒啪嗒扇动着前进",
    "new": "会啪嗒啪嗒扇动耳朵纳凉",
    "reason": "原文动作目的是纳凉，不是前进。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "gPhanpyPokedexText",
    "final_text": "小小象的巨大耳朵可以代替扇子，天气热的时候会啪嗒啪嗒扇动耳朵纳凉，\n即使是幼年时力气也非常大。",
    "old_current_text": "小小象的巨大耳朵可以代替扇子，天气热的时候会啪嗒啪嗒扇动着前进，\n即使是幼年时力气也非常大。",
    "changed_files": [
      "patch/pokedex_entries.json",
      "../pokeemerald_us_chs/src/data/pokemon/pokedex_text.h"
    ],
    "us_source_file": "src/data/pokemon/pokedex_text.h",
    "jp_source": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "ゴマゾウの　おおきな　みみは　うちわの　かわり。\nあつくなると　ぱたぱた　あおいで　すずむ。\nこどもでも　ちからは　とても　つよい。"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "小小象的巨大耳朵可以代替扇子，天气热的时候会啪嗒啪嗒扇动耳朵纳凉，\n即使是幼年时力气也非常大。"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "ゴマゾウの　おおきな　みみは　うちわの　かわり。\nあつくなると　ぱたぱた　あおいで　すずむ。\nこどもでも　ちからは　とても　つよい。"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/pokedex_entries.json",
      "table": "ChsPokedexEntries",
      "index": 231,
      "text": "小小象的巨大耳朵可以代替扇子，天气热的时候会啪嗒啪嗒扇动耳朵纳凉，\n即使是幼年时力气也非常大。",
      "rom_address": "0x090A5C60",
      "encoded_sha256": "716404392d986e5925c88b1b7cd4cf631ffeec4d64e726308a3643cd86749c80",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 1160 行 · pokedex / 292 · 

判定：`fixed_verified`

理由：原文中空和黑暗是两个事实，恢复后者。

日文：

```text
ハネを　まったく　うごかして　いないのに\nくうちゅうに　うかんでいる　ふしぎな　ポケモン。\nからだの　なかは　くうどうで　まっくら。
```

英文：

```text
A peculiar POKéMON that floats in air even\nthough its wings remain completely still.\nThe inside of its body is hollow and\nutterly dark.
```

报告原中文：

```text
没有拍动翅膀就可以飞在天上的相当特别的宝可梦，身体是中空的，\n里面什么也没有。
```

修复前实际中文：

```text
没有拍动翅膀就可以飞在天上的相当特别的宝可梦，身体是中空的，
里面什么也没有。
```

最终中文：

```text
没有拍动翅膀就可以飞在天上的相当特别的宝可梦，身体是中空的，
里面一片漆黑。
```

证据：

```json
{
  "review": {
    "row_number": 1160,
    "symbol": "",
    "domain": "pokedex",
    "idx": "292",
    "old": "里面什么也没有",
    "new": "里面一片漆黑",
    "reason": "原文中空和黑暗是两个事实，恢复后者。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "gShedinjaPokedexText",
    "final_text": "没有拍动翅膀就可以飞在天上的相当特别的宝可梦，身体是中空的，\n里面一片漆黑。",
    "old_current_text": "没有拍动翅膀就可以飞在天上的相当特别的宝可梦，身体是中空的，\n里面什么也没有。",
    "changed_files": [
      "patch/pokedex_entries.json",
      "../pokeemerald_us_chs/src/data/pokemon/pokedex_text.h"
    ],
    "us_source_file": "src/data/pokemon/pokedex_text.h",
    "jp_source": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "ハネを　まったく　うごかして　いないのに\nくうちゅうに　うかんでいる　ふしぎな　ポケモン。\nからだの　なかは　くうどうで　まっくら。"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "没有拍动翅膀就可以飞在天上的相当特别的宝可梦，身体是中空的，\n里面一片漆黑。"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "ハネを　まったく　うごかして　いないのに\nくうちゅうに　うかんでいる　ふしぎな　ポケモン。\nからだの　なかは　くうどうで　まっくら。"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/pokedex_entries.json",
      "table": "ChsPokedexEntries",
      "index": 292,
      "text": "没有拍动翅膀就可以飞在天上的相当特别的宝可梦，身体是中空的，\n里面一片漆黑。",
      "rom_address": "0x090A7528",
      "encoded_sha256": "268090b1d9c0d220152a4e4e3500c45adac726ca636348e60020390443d73be1",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 1168 行 · pokedex / 300 · 

判定：`fixed_verified`

理由：けばだたせる / puff out 指尾毛竖起。

日文：

```text
あいきょう　たっぷりの　しぐさで　だいにんき。\nたたかう　ときは　しっぽを　けばだたせる。\nするどい　うなりごえを　あげて　てきを　いかく。
```

英文：

```text
A SKITTY's adorably cute behavior makes it\nhighly popular. In battle, it makes its tail\npuff out. It threatens foes with a sharp\ngrowl.
```

报告原中文：

```text
以其非常怜爱的动作大受欢迎。战斗的时候会拍动尾巴上的毛。\n能发出尖锐的叫声威吓敌人。
```

修复前实际中文：

```text
以其非常怜爱的动作大受欢迎。战斗的时候会拍动尾巴上的毛。
能发出尖锐的叫声威吓敌人。
```

最终中文：

```text
以其非常怜爱的动作大受欢迎。战斗的时候会竖起尾巴上的毛。
能发出尖锐的叫声威吓敌人。
```

证据：

```json
{
  "review": {
    "row_number": 1168,
    "symbol": "",
    "domain": "pokedex",
    "idx": "300",
    "old": "会拍动尾巴上的毛",
    "new": "会竖起尾巴上的毛",
    "reason": "けばだたせる / puff out 指尾毛竖起。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "gSkittyPokedexText",
    "final_text": "以其非常怜爱的动作大受欢迎。战斗的时候会竖起尾巴上的毛。\n能发出尖锐的叫声威吓敌人。",
    "old_current_text": "以其非常怜爱的动作大受欢迎。战斗的时候会拍动尾巴上的毛。\n能发出尖锐的叫声威吓敌人。",
    "changed_files": [
      "patch/pokedex_entries.json",
      "../pokeemerald_us_chs/src/data/pokemon/pokedex_text.h"
    ],
    "us_source_file": "src/data/pokemon/pokedex_text.h",
    "jp_source": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "あいきょう　たっぷりの　しぐさで　だいにんき。\nたたかう　ときは　しっぽを　けばだたせる。\nするどい　うなりごえを　あげて　てきを　いかく。"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "以其非常怜爱的动作大受欢迎。战斗的时候会竖起尾巴上的毛。\n能发出尖锐的叫声威吓敌人。"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "あいきょう　たっぷりの　しぐさで　だいにんき。\nたたかう　ときは　しっぽを　けばだたせる。\nするどい　うなりごえを　あげて　てきを　いかく。"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/pokedex_entries.json",
      "table": "ChsPokedexEntries",
      "index": 300,
      "text": "以其非常怜爱的动作大受欢迎。战斗的时候会竖起尾巴上的毛。\n能发出尖锐的叫声威吓敌人。",
      "rom_address": "0x090A7860",
      "encoded_sha256": "6afd4f95702db255b24fe39139783eb2c53077fbe6048675af55ab087fdf95fd",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 1179 行 · pokedex / 311 · 

判定：`fixed_verified`

理由：ショート / shorting out 指短路；ボンボン / pom-poms 指花球。

日文：

```text
なかまの　ポケモンを　おうえんする　しゅうせい。\nりょうてから　はっした　でんきを　ショートさせて\nひばなの　ボンボンを　つくる　ことが　できる。
```

英文：

```text
It has the trait of cheering on its fellow\nPOKéMON. By shorting out the electricity\nit releases from its paws, it creates\npom-poms for cheering.
```

报告原中文：

```text
具有会为伙伴宝可梦加油的习性。可以将两手所散发出的电力发射出去，\n以做出火花的碰撞效果。
```

修复前实际中文：

```text
具有会为伙伴宝可梦加油的习性。可以将两手所散发出的电力发射出去，
以做出火花的碰撞效果。
```

最终中文：

```text
具有会为伙伴宝可梦加油的习性。可以让两手释放的电力短路，
制成用于加油的火花花球。
```

证据：

```json
{
  "review": {
    "row_number": 1179,
    "symbol": "",
    "domain": "pokedex",
    "idx": "311",
    "old": "可以将两手所散发出的电力发射出去，\n以做出火花的碰撞效果。",
    "new": "可以让两手释放的电力短路，\n制成用于加油的火花花球。",
    "reason": "ショート / shorting out 指短路；ボンボン / pom-poms 指花球。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "gPluslePokedexText",
    "final_text": "具有会为伙伴宝可梦加油的习性。可以让两手释放的电力短路，\n制成用于加油的火花花球。",
    "old_current_text": "具有会为伙伴宝可梦加油的习性。可以将两手所散发出的电力发射出去，\n以做出火花的碰撞效果。",
    "changed_files": [
      "patch/pokedex_entries.json",
      "../pokeemerald_us_chs/src/data/pokemon/pokedex_text.h"
    ],
    "us_source_file": "src/data/pokemon/pokedex_text.h",
    "jp_source": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "なかまの　ポケモンを　おうえんする　しゅうせい。\nりょうてから　はっした　でんきを　ショートさせて\nひばなの　ボンボンを　つくる　ことが　できる。"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "具有会为伙伴宝可梦加油的习性。可以让两手释放的电力短路，\n制成用于加油的火花花球。"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "なかまの　ポケモンを　おうえんする　しゅうせい。\nりょうてから　はっした　でんきを　ショートさせて\nひばなの　ボンボンを　つくる　ことが　できる。"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/pokedex_entries.json",
      "table": "ChsPokedexEntries",
      "index": 311,
      "text": "具有会为伙伴宝可梦加油的习性。可以让两手释放的电力短路，\n制成用于加油的火花花球。",
      "rom_address": "0x090A7D2C",
      "encoded_sha256": "09b096b0dfca72406f394a8b7e4b39f84c067a4d47a64b0527ea9c4c1e4d69dc",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 1215 行 · pokedex / 347 · 

判定：`fixed_verified`

理由：はね / wings 在太古羽虫条目是翅状肢。

日文：

```text
かがくの　ちからで　かせきから　よみがえった。\nさゆう　8まいの　はねを　くねらせて　およぐ。\nうみで　くらすうちに　あしが　ハネに　かわった。
```

英文：

```text
It was resurrected from a fossil using the\npower of science. It swims by undulating\nthe eight wings at its sides. They were\nfeet that adapted to life in the sea.
```

报告原中文：

```text
以科学的力量从化石中再度复活。会以摆动左右的8片羽毛的方式游动。\n居住在海里的时候脚变成了羽毛。
```

修复前实际中文：

```text
以科学的力量从化石中再度复活。会以摆动左右的8片羽毛的方式游动。
居住在海里的时候脚变成了羽毛。
```

最终中文：

```text
以科学的力量从化石中再度复活。会以摆动左右的8片翅膀的方式游动。
居住在海里的时候脚变成了翅膀。
```

证据：

```json
{
  "review": {
    "row_number": 1215,
    "symbol": "",
    "domain": "pokedex",
    "idx": "347",
    "old": "羽毛",
    "new": "翅膀",
    "reason": "はね / wings 在太古羽虫条目是翅状肢。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "gAnorithPokedexText",
    "final_text": "以科学的力量从化石中再度复活。会以摆动左右的8片翅膀的方式游动。\n居住在海里的时候脚变成了翅膀。",
    "old_current_text": "以科学的力量从化石中再度复活。会以摆动左右的8片羽毛的方式游动。\n居住在海里的时候脚变成了羽毛。",
    "changed_files": [
      "patch/pokedex_entries.json",
      "../pokeemerald_us_chs/src/data/pokemon/pokedex_text.h"
    ],
    "us_source_file": "src/data/pokemon/pokedex_text.h",
    "jp_source": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "かがくの　ちからで　かせきから　よみがえった。\nさゆう　8まいの　はねを　くねらせて　およぐ。\nうみで　くらすうちに　あしが　ハネに　かわった。"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "以科学的力量从化石中再度复活。会以摆动左右的8片翅膀的方式游动。\n居住在海里的时候脚变成了翅膀。"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/pokemon/pokedex_text.h",
        "text": "かがくの　ちからで　かせきから　よみがえった。\nさゆう　8まいの　はねを　くねらせて　およぐ。\nうみで　くらすうちに　あしが　ハネに　かわった。"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/pokedex_entries.json",
      "table": "ChsPokedexEntries",
      "index": 347,
      "text": "以科学的力量从化石中再度复活。会以摆动左右的8片翅膀的方式游动。\n居住在海里的时候脚变成了翅膀。",
      "rom_address": "0x090A8C60",
      "encoded_sha256": "a70247684c16303a1e6c56519dfd8aa59576d6e26ae4ad00daea26ba3d50b0e2",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 1216 行 · pokedex / 348 · 

判定：`already_fixed`

理由：39e1ca1 / b08e5a919 已修复两条图鉴栖息地。

日文：

```text
ふだんは　ちじょうで　くらす　アーマルドだが\nえものを　とる　ときには　うみに　もぐり\n2まいの　おおきな　はねを　つかって　およぐ。
```

英文：

```text
ARMALDO usually lives on land. However,\nwhen it hunts for prey, it dives beneath\nthe ocean. It swims around using its two\nlarge wings.
```

报告原中文：

```text
虽然太古盔甲平常都住在地底下，不过在捕捉猎物的时候就会潜入海中，\n利用两片巨大的翅膀来游泳。
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 1216,
    "symbol": "",
    "domain": "pokedex",
    "idx": "348",
    "reason": "39e1ca1 / b08e5a919 已修复两条图鉴栖息地。",
    "action": "already_fixed"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/pokedex_entries.json",
      "table": "ChsPokedexEntries",
      "index": 348,
      "text": "虽然太古盔甲平常都住在陆地上，不过在捕捉猎物的时候就会潜入海中，\n利用两片巨大的翅膀来游泳。",
      "rom_address": "0x090A8CD4",
      "encoded_sha256": "51125563d808752d0b758046c20b11fbef629f7c829bc75d3ad2d5dabc628e9f",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 1218 行 · pokedex / 350 · 

判定：`already_fixed`

理由：39e1ca1 / b08e5a919 已修复两条图鉴栖息地。

日文：

```text
おおきな　みずうみの　そこに　いると　いわれる。\nもっとも　うつくしい　ポケモンと　いわれていて\nかいがや　ちょうこくの　モデルと　なっている。
```

英文：

```text
It is said to live at the bottom of\nlarge lakes. Considered to be the most\nbeautiful of all POKéMON, it has been\ndepicted in paintings and statues.
```

报告原中文：

```text
据说它生活在广大的湖边。被人称为最美丽的宝可梦，也被当作绘画与雕刻的对象。
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 1218,
    "symbol": "",
    "domain": "pokedex",
    "idx": "350",
    "reason": "39e1ca1 / b08e5a919 已修复两条图鉴栖息地。",
    "action": "already_fixed"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/pokedex_entries.json",
      "table": "ChsPokedexEntries",
      "index": 350,
      "text": "据说它生活在大湖的底部。被人称为最美丽的宝可梦，也被当作绘画与雕刻的对象。",
      "rom_address": "0x090A8DAC",
      "encoded_sha256": "d4ef024443c6070d4e65e9620ff69d6f27c5d1c42687d2f4de6c896acd6d7ff9",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 1643 行 · ported_batch / 388 · Route104_Text_RouteSignPetalburg

判定：`already_fixed`

理由：e405b84 / 0b86060f1 已把1O4改为104。

日文：

```text
ここは　104ばん　どうろ\n{RIGHT_ARROW}　トウカシティ
```

英文：

```text
ROUTE 1O4\n{RIGHT_ARROW} PETALBURG CITY
```

报告原中文：

```text
1O4号道路\n→橙华市$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 1643,
    "symbol": "Route104_Text_RouteSignPetalburg",
    "domain": "ported_batch",
    "idx": "388",
    "reason": "e405b84 / 0b86060f1 已把1O4改为104。",
    "action": "already_fixed"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/Route104/scripts.inc",
        "text": "104号道路\n{RIGHT_ARROW}橙华市$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/Route104/scripts.inc",
        "text": "ここは　104ばん　どうろ\n{RIGHT_ARROW}　トウカシティ$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Route104_Text_RouteSignPetalburg",
      "file": "patch/batches/017_route104.json",
      "payload_address": "0x0900A18D",
      "payload_sha256": "961774bb06de191d29da7ba1fa8e7f331a37db09affe7065f6d8e17aa5ba5620",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x081E751F",
          "original": "0x081E7D65",
          "target": "0x0900A18D",
          "batch": "patch/batches/017_route104.json"
        }
      ]
    }
  ]
}
```

### CSV 第 4394 行 · ported_batch / 3139 · MossdeepCity_Gym_Text_BlakePostBattle

判定：`fixed_verified`

理由：原文否认吹气作弊，不是否认吹牛。

日文：

```text
モンスターボールは　おおきすぎた\nこの　わたぼこり　なら　ぜったいに⋯⋯\pふううううううっ⋯⋯！\p⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯\pちがうぞ！\nはないきで　とばして　なんか　いないぞ！$
```

英文：

```text
A POKé BALL was too heavy to lift\npsychically. But this dust bunny…\pWhoooooooooooooooh!\n… … … … … …\pNo, I'm not cheating!\nI didn't blow on it! Honestly!$
```

报告原中文：

```text
要用精神力举起精灵球还是困难\n了点，但这么小的灰尘的话……\p呜啊啊啊啊啊啊啊！\n…… …… ……\p不不，我没骗人！\n我没吹牛！真的！$
```

修复前实际中文：

```text
要用精神力举起精灵球还是困难
了点，但这么小的灰尘的话……\p呜啊啊啊啊啊啊啊！
…… …… ……\p不不，我没骗人！
我没吹牛！真的！
```

最终中文：

```text
要用精神力举起精灵球还是困难
了点，但这么小的灰尘的话……\p呜啊啊啊啊啊啊啊！
…… …… ……\p不不，我没骗人！
我可没用嘴吹！真的！
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/MossdeepCity_Gym/scripts.inc",
        "text": "要用精神力举起精灵球还是困难\n了点，但这么小的灰尘的话……\\p呜啊啊啊啊啊啊啊！\n…… …… ……\\p不不，我没骗人！\n我可没用嘴吹！真的！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/MossdeepCity_Gym/scripts.inc",
        "text": "モンスターボールは　おおきすぎた\nこの　わたぼこり　なら　ぜったいに⋯⋯\\pふううううううっ⋯⋯！\\p⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯\\pちがうぞ！\nはないきで　とばして　なんか　いないぞ！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_MossdeepCity_Gym_Text_BlakePostBattle",
      "file": "patch/batches/152_mossdeepcity_gym.json",
      "payload_address": "0x090350FF",
      "payload_sha256": "5e9b66518375d5718c572b8ed263ad6f4a32a5c0df8f5075568327d747be3fee",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0820B6A4",
          "original": "0x0820BA3C",
          "target": "0x090350FF",
          "batch": "patch/batches/152_mossdeepcity_gym.json"
        }
      ]
    }
  ]
}
```

### CSV 第 4397 行 · ported_batch / 3142 · MossdeepCity_Gym_Text_CliffordPostBattle

判定：`regional_difference`

理由：日美官方文本不同；当前中文准确跟随英文，不将日版剧情差异强加给美版。

日文：

```text
この　ジムの　リーダーも　そりゃもう！\nわかくて　げんき　はつらつ　ですぞ$
```

英文：

```text
It seems that I could not overcome\nyour youthful energy.$
```

报告原中文：

```text
看来我无法胜过\n你的活力。$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 4397,
    "symbol": "MossdeepCity_Gym_Text_CliffordPostBattle",
    "domain": "ported_batch",
    "idx": "3142",
    "reason": "日美官方文本不同；当前中文准确跟随英文，不将日版剧情差异强加给美版。",
    "action": "regional_difference"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/MossdeepCity_Gym/scripts.inc",
        "text": "看来我无法胜过\n你的活力。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/MossdeepCity_Gym/scripts.inc",
        "text": "この　ジムの　リーダーも　そりゃもう！\nわかくて　げんき　はつらつ　ですぞ$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_MossdeepCity_Gym_Text_CliffordPostBattle",
      "file": "patch/batches/152_mossdeepcity_gym.json",
      "payload_address": "0x090351C5",
      "payload_sha256": "5a7526099a4d793cb8525ee09347ecf850468477fe615386566b7b420e64d738",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0820B745",
          "original": "0x0820BD63",
          "target": "0x090351C5",
          "batch": "patch/batches/152_mossdeepcity_gym.json"
        }
      ]
    }
  ]
}
```

### CSV 第 4516 行 · ported_batch / 3261 · MossdeepCity_StevensHouse_Text_LetterFromSteven

判定：`fixed_verified`

理由：中文语序笔误。

日文：

```text
てがみが　ある！\p⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯\p{PLAYER}{KUN}へ\pボクは　おもうことが　あって\nしばらく　しゅぎょうを　つづける\lとうぶん　いえに　かえらない\pそこで　おねがいだ\pつくえの　うえにある\nモンスターボールを　うけとって　ほしい\pなかに　いるのは　ダンバルといって\nボクの　おきにいりの　ポケモンだから\pよろしく　たのむよ\pでは　また　いつか　あおう！\n　　　　　　ツワブキ　ダイゴより$
```

英文：

```text
It's a letter.\p… … … … … …\pTo {PLAYER}{KUN}…\pI've decided to do a little soul-\nsearching and train on the road.\pI don't plan to return home for some\ntime.\pI have a favor to ask of you.\pI want you to take the POKé BALL on\nthe desk.\pInside it is a BELDUM, my favorite\nPOKéMON.\pI'm counting on you.\pMay our paths cross someday.\pSTEVEN STONE$
```

报告原中文：

```text
是一封信。\p…… …… ……\p致{PLAYER}{KUN}……\p已我决定踏上自我\n探索与修行之旅。\p短时间内不\n打算回家，\p我想拜托你收下\n桌上的精灵球，\p里面是我最喜欢的宝可梦——\n铁哑铃，\p拜托你照顾好它。\p愿你我终有相逢之日。\p大吾·兹伏奇$
```

修复前实际中文：

```text
是一封信。\p…… …… ……\p致{PLAYER}{KUN}……\p已我决定踏上自我
探索与修行之旅。\p短时间内不
打算回家，\p我想拜托你收下
桌上的精灵球，\p里面是我最喜欢的宝可梦——
铁哑铃，\p拜托你照顾好它。\p愿你我终有相逢之日。\p大吾·兹伏奇
```

最终中文：

```text
是一封信。\p…… …… ……\p致{PLAYER}{KUN}……\p我已决定踏上自我
探索与修行之旅。\p短时间内不
打算回家，\p我想拜托你收下
桌上的精灵球，\p里面是我最喜欢的宝可梦——
铁哑铃，\p拜托你照顾好它。\p愿你我终有相逢之日。\p大吾·兹伏奇
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/MossdeepCity_StevensHouse/scripts.inc",
        "text": "是一封信。\\p…… …… ……\\p致{PLAYER}{KUN}……\\p我已决定踏上自我\n探索与修行之旅。\\p短时间内不\n打算回家，\\p我想拜托你收下\n桌上的精灵球，\\p里面是我最喜欢的宝可梦——\n铁哑铃，\\p拜托你照顾好它。\\p愿你我终有相逢之日。\\p大吾·兹伏奇$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/MossdeepCity_StevensHouse/scripts.inc",
        "text": "てがみが　ある！\\p⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯\\p{PLAYER}{KUN}へ\\pボクは　おもうことが　あって\nしばらく　しゅぎょうを　つづける\\lとうぶん　いえに　かえらない\\pそこで　おねがいだ\\pつくえの　うえにある\nモンスターボールを　うけとって　ほしい\\pなかに　いるのは　ダンバルといって\nボクの　おきにいりの　ポケモンだから\\pよろしく　たのむよ\\pでは　また　いつか　あおう！\n　　　　　　ツワブキ　ダイゴより$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_MossdeepCity_StevensHouse_Text_LetterFromSteven",
      "file": "patch/batches/159_mossdeepcity_stevenshouse.json",
      "payload_address": "0x09036F2E",
      "payload_sha256": "22e9e4bb82d991e6784550f5690ca6ef67fc42a4882fac1c80304ef1cfa96edf",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0820C9B0",
          "original": "0x0820CB77",
          "target": "0x09036F2E",
          "batch": "patch/batches/159_mossdeepcity_stevenshouse.json"
        }
      ]
    }
  ]
}
```

### CSV 第 4712 行 · ported_batch / 3457 · gText_Confirm3

判定：`fixed_verified`

理由：Wokann wallclock.c:94/794：实际返回按钮是もどる。

日文：

```text
もどる　
```

英文：

```text
CONFIRM
```

报告原中文：

```text
确定
```

修复前实际中文：

```text
确定
```

最终中文：

```text
返回
```

证据：

```json
{
  "review": {
    "row_number": 4712,
    "symbol": "gText_Confirm3",
    "domain": "ported_batch",
    "idx": "3457",
    "old": "确定",
    "new": "返回",
    "reason": "Wokann wallclock.c:94/794：实际返回按钮是もどる。",
    "scope": "jp_only",
    "action": "fix",
    "final_text": "返回",
    "old_current_text": "确定",
    "changed_files": [
      "patch/batches/168_core_interfaces.json"
    ],
    "us_source_file": "src/strings.c",
    "jp_source": [
      {
        "file": "src/wallclock.c",
        "text": "もどる　"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/strings.c",
        "text": "确定"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/wallclock.c",
        "text": "もどる　"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_Confirm3",
      "file": "patch/batches/168_core_interfaces.json",
      "payload_address": "0x090394C1",
      "payload_sha256": "4de3abc0319fcca61dccb98356b27bf1cec454680dd086d8e168746b0646cfd7",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08134B88",
          "original": "0x08591C15",
          "target": "0x090394C1",
          "batch": "patch/batches/168_core_interfaces.json"
        }
      ]
    }
  ]
}
```

### CSV 第 4713 行 · ported_batch / 3458 · gText_Cancel4

判定：`fixed_verified`

理由：Wokann wallclock.c:93/746：实际设置时钟按钮是けってい。

日文：

```text
けってい
```

英文：

```text
CANCEL
```

报告原中文：

```text
取消
```

修复前实际中文：

```text
取消
```

最终中文：

```text
确定
```

证据：

```json
{
  "review": {
    "row_number": 4713,
    "symbol": "gText_Cancel4",
    "domain": "ported_batch",
    "idx": "3458",
    "old": "取消",
    "new": "确定",
    "reason": "Wokann wallclock.c:93/746：实际设置时钟按钮是けってい。",
    "scope": "jp_only",
    "action": "fix",
    "final_text": "确定",
    "old_current_text": "取消",
    "changed_files": [
      "patch/batches/168_core_interfaces.json"
    ],
    "us_source_file": "src/strings.c",
    "jp_source": [
      {
        "file": "src/wallclock.c",
        "text": "けってい"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/strings.c",
        "text": "取消"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/wallclock.c",
        "text": "けってい"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_Cancel4",
      "file": "patch/batches/168_core_interfaces.json",
      "payload_address": "0x090394C8",
      "payload_sha256": "dff97663df6750593e7af6ff2daf3a90b9b4d179a16df2b9a5efab946ad5379f",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08134CE4",
          "original": "0x08591C1A",
          "target": "0x090394C8",
          "batch": "patch/batches/168_core_interfaces.json"
        }
      ]
    }
  ]
}
```

### CSV 第 4763 行 · ported_batch / 3509 · gText_SizeComparedTo

判定：`fixed_us_only`

理由：US调用StringCopy+StringAppend直接拼玩家名，不展开占位符；JP已用分段适配，仅修US并补后缀。

日文：

```text
の　おおきさくらべ
```

英文：

```text
SIZE COMPARED TO 
```

报告原中文：

```text
{STR_VAR_1}与{STR_VAR_2}的体型比较
```

修复前实际中文：

```text
{STR_VAR_1}与{STR_VAR_2}的体型比较
```

最终中文：

```text
与
```

证据：

```json
{
  "review": {
    "row_number": 4763,
    "symbol": "gText_SizeComparedTo",
    "domain": "ported_batch",
    "idx": "3509",
    "old": "{STR_VAR_1}与{STR_VAR_2}的体型比较",
    "new": "与",
    "reason": "US调用StringCopy+StringAppend直接拼玩家名，不展开占位符；JP已用分段适配，仅修US并补后缀。",
    "scope": "us_only",
    "action": "fix",
    "final_text": "与",
    "old_current_text": "{STR_VAR_1}与{STR_VAR_2}的体型比较",
    "changed_files": [
      "../pokeemerald_us_chs/src/strings.c"
    ],
    "us_source_file": "src/strings.c",
    "jp_source": [
      {
        "file": "src/data/text/region_texts76.h",
        "text": "の　おおきさくらべ"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/strings.c",
        "text": "与"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/region_texts76.h",
        "text": "の　おおきさくらべ"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_SizeComparedTo",
      "file": "patch/batches/171_pokedex.json",
      "payload_address": "0x090399F1",
      "payload_sha256": "f3564851798606c5401d29027ad5cfac1b59e84c268916929b53784d4c7af69c",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x080BF220",
          "original": "0x085C8FDD",
          "target": "0x090399F1",
          "batch": "patch/batches/171_pokedex.json"
        }
      ]
    },
    {
      "payload_symbol": "Chs_gText_SizeComparedToAnd",
      "file": "patch/batches/171_pokedex.json",
      "payload_address": "0x090399FE",
      "payload_sha256": "b2bd2dcf39915ea9926f38a5c049df028283395d2fb37fbfc44996fade15cf91",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x080BF218",
          "original": "0x085C8FDB",
          "target": "0x090399FE",
          "batch": "patch/batches/171_pokedex.json"
        }
      ]
    }
  ]
}
```

### CSV 第 4798 行 · ported_batch / 3545 · gText_DexSortAtoZDescription

判定：`equivalent_wording`

理由：已获得必然也是已发现，两个集合并集不扩大排序范围；无必要改变提示。

日文：

```text
みつけたポケモンの　なまえを\nごじゅうおんじゅんで　ひょうじ　します
```

英文：

```text
Spotted and owned POKéMON are listed\nalphabetically.
```

报告原中文：

```text
按字母的顺序来排列已发现\n和已获得的宝可梦。
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 4798,
    "symbol": "gText_DexSortAtoZDescription",
    "domain": "ported_batch",
    "idx": "3545",
    "reason": "已获得必然也是已发现，两个集合并集不扩大排序范围；无必要改变提示。",
    "action": "equivalent_wording"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/strings.c",
        "text": "按字母的顺序来排列已发现\n和已获得的宝可梦。"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/region_texts76.h",
        "text": "みつけたポケモンの　なまえを\nごじゅうおんじゅんで　ひょうじ　します"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_DexSortAtoZDescription",
      "file": "patch/batches/171_pokedex.json",
      "payload_address": "0x09039C25",
      "payload_sha256": "0aae0d0c3c97bbea137de9521685dda74e17f76d8a8dd477e0186d779f55009f",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08544230",
          "original": "0x085C91E2",
          "target": "0x09039C25",
          "batch": "patch/batches/171_pokedex.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5005 行 · ported_batch / 3752 · gText_EmptyString6

判定：`mapping_artifact`

理由：当前已有训练家卡计数词显示适配；报告按US空字符串判NOPATCH漏掉了该路径。

日文：

```text
ひき
```

英文：

```text

```

报告原中文：

```text

```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 5005,
    "symbol": "gText_EmptyString6",
    "domain": "ported_batch",
    "idx": "3752",
    "reason": "当前已有训练家卡计数词显示适配；报告按US空字符串判NOPATCH漏掉了该路径。",
    "action": "mapping_artifact"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/strings.c",
        "text": ""
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/region_texts101.h",
        "text": "ひき"
      }
    ]
  },
  "mapping": []
}
```

### CSV 第 5133 行 · ported_batch / 3880 · gRegionMapEntries[87].name

判定：`no_text`

理由：动态地区槽的空名称是设计占位，不能汉化为空的名字。

日文：

```text
とくしゅ
```

英文：

```text

```

报告原中文：

```text

```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 5133,
    "symbol": "gRegionMapEntries[87].name",
    "domain": "ported_batch",
    "idx": "3880",
    "reason": "动态地区槽的空名称是设计占位，不能汉化为空的名字。",
    "action": "no_text"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/region_map_names.json",
      "table": "ChsRegionMapEntries",
      "index": 87,
      "text": "",
      "rom_address": "0x090AD138",
      "encoded_sha256": "dc02768fa8d4d5dc2885b82cc85d273447b8e2846ae9ab82c7c3ac52008435c7",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 5261 行 · ported_batch / 4008 · gText_UserMoreEasilyStartled

判定：`fixed_verified`

理由：报告引用理由串条，但实际说明多加了成功表演条件；按当前日英文说明修正。

日文：

```text
この　アピールの　あと\nびっくり　しやすく　なってしまう$
```

英文：

```text
After this move, the user is\nmore easily startled.$
```

报告原中文：

```text
虽然能够演出很好的表演，\n但是之后会更容易受干扰。
```

修复前实际中文：

```text
虽然能够演出很好的表演，
但是之后会更容易受干扰。
```

最终中文：

```text
使用这个招式后，
会更容易受到干扰。
```

证据：

```json
{
  "review": {
    "row_number": 5261,
    "symbol": "gText_UserMoreEasilyStartled",
    "domain": "ported_batch",
    "idx": "4008",
    "old": "虽然能够演出很好的表演，\n但是之后会更容易受干扰。",
    "new": "使用这个招式后，\n会更容易受到干扰。",
    "reason": "报告引用理由串条，但实际说明多加了成功表演条件；按当前日英文说明修正。",
    "scope": "both",
    "action": "fix",
    "final_text": "使用这个招式后，\n会更容易受到干扰。",
    "old_current_text": "虽然能够演出很好的表演，\n但是之后会更容易受干扰。",
    "changed_files": [
      "../pokeemerald_us_chs/data/text/contest_strings.inc",
      "patch/batches/175_summary_info.json"
    ],
    "us_source_file": "data/text/contest_strings.inc",
    "jp_source": [
      {
        "file": "data/text/contest_strings.inc",
        "text": "この　アピールの　あと\nびっくり　しやすく　なってしまう$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/contest_strings.inc",
        "text": "使用这个招式后，\n会更容易受到干扰。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/contest_strings.inc",
        "text": "この　アピールの　あと\nびっくり　しやすく　なってしまう$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "ChsContestEffectDesc1",
      "file": "patch/batches/175_summary_info.json",
      "payload_address": "0x0903BA15",
      "payload_sha256": "c8278ca0736ffb5b5a2b45292450e397fb61c9c31013586cdda561f740d3fa66",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08560BB8",
          "original": "0x0824ACD7",
          "target": "0x0903BA15",
          "batch": "patch/batches/175_summary_info.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5324 行 · ported_batch / 4071 · gText_Var1AndYouWantedVar2

判定：`intentional_adaptation`

理由：数字后显示円是用户要求且符合日版原文；不恢复美版前置金额符号。

日文：

```text
{STR_VAR_1}を　{STR_VAR_2}コで\n{STR_VAR_3}¥　おかいあげですか？$
```

英文：

```text
{STR_VAR_1}? And you wanted {STR_VAR_2}?\nThat will be ¥{STR_VAR_3}.
```

报告原中文：

```text
是{STR_VAR_1}啊。\n{STR_VAR_2}个一共是{STR_VAR_3}¥。$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 5324,
    "symbol": "gText_Var1AndYouWantedVar2",
    "domain": "ported_batch",
    "idx": "4071",
    "reason": "数字后显示円是用户要求且符合日版原文；不恢复美版前置金额符号。",
    "action": "intentional_adaptation"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/strings.c",
        "text": "是{STR_VAR_1}啊。\n{STR_VAR_2}个一共是¥{STR_VAR_3}。"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_Var1AndYouWantedVar2",
      "file": "patch/batches/177_shop.json",
      "payload_address": "0x0903C1B4",
      "payload_sha256": "e4ee7cbddc4efb1e9b5cfd5ecfeac8fd93047ee11dd784cfde8509bdb65d4e00",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x080E03B8",
          "original": "0x085C991F",
          "target": "0x0903C1B4",
          "batch": "patch/batches/177_shop.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5325 行 · ported_batch / 4072 · gText_Var1IsItThatllBeVar2

判定：`intentional_adaptation`

理由：数字后显示円是用户要求且符合日版原文；不恢复美版前置金额符号。

日文：

```text
{STR_VAR_1}　だね！\n{STR_VAR_2}¥　だけど　かうかい？$
```

英文：

```text
{STR_VAR_1}, is it?\nThat'll be ¥{STR_VAR_2}. Do you want it?
```

报告原中文：

```text
是{STR_VAR_1}啊。\n价格是{STR_VAR_2}¥。$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 5325,
    "symbol": "gText_Var1IsItThatllBeVar2",
    "domain": "ported_batch",
    "idx": "4072",
    "reason": "数字后显示円是用户要求且符合日版原文；不恢复美版前置金额符号。",
    "action": "intentional_adaptation"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/strings.c",
        "text": "是{STR_VAR_1}啊。\n价格是¥{STR_VAR_2}。"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_Var1IsItThatllBeVar2",
      "file": "patch/batches/177_shop.json",
      "payload_address": "0x0903C1D0",
      "payload_sha256": "6429227f905b4ea2f055d4c2a0167994452fc394db1dc115d250cf147badcf3b",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x080E01C4",
          "original": "0x085C9936",
          "target": "0x0903C1D0",
          "batch": "patch/batches/177_shop.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5326 行 · ported_batch / 4073 · gText_YouWantedVar1ThatllBeVar2

判定：`intentional_adaptation`

理由：数字后显示円是用户要求且符合日版原文；不恢复美版前置金额符号。

日文：

```text
{STR_VAR_1}　ですね！\n{STR_VAR_2}¥　だけど　かいますか？$
```

英文：

```text
You wanted {STR_VAR_1}?\nThat'll be ¥{STR_VAR_2}. Will that be okay?
```

报告原中文：

```text
是{STR_VAR_1}啊。\n价格是{STR_VAR_2}¥，可以吗？$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 5326,
    "symbol": "gText_YouWantedVar1ThatllBeVar2",
    "domain": "ported_batch",
    "idx": "4073",
    "reason": "数字后显示円是用户要求且符合日版原文；不恢复美版前置金额符号。",
    "action": "intentional_adaptation"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/strings.c",
        "text": "是{STR_VAR_1}啊。\n价格是¥{STR_VAR_2}，可以吗？"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_YouWantedVar1ThatllBeVar2",
      "file": "patch/batches/177_shop.json",
      "payload_address": "0x0903C1E7",
      "payload_sha256": "5496591e862955e4a633db7d44e18b971565aa03ec81cdab63af6e3a6ca15891",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x080E01E8",
          "original": "0x085C994B",
          "target": "0x0903C1E7",
          "batch": "patch/batches/177_shop.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5336 行 · ported_batch / 4083 · sText_PkmnGainedEXP

判定：`intentional_adaptation`

理由：日版经验值模板使用B_BUFF2，JP生产者/现有专用hook与此一致；不能套美版B_BUFF3。

日文：

```text
{B_BUFF1}{B_BUFF2}　けいけんちを　もらった！\p
```

英文：

```text
{B_BUFF1} gained{B_BUFF2}\n{B_BUFF3} EXP. Points!\p
```

报告原中文：

```text
{B_BUFF1}获得了{B_BUFF2}经验值！\p$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 5336,
    "symbol": "sText_PkmnGainedEXP",
    "domain": "ported_batch",
    "idx": "4083",
    "reason": "日版经验值模板使用B_BUFF2，JP生产者/现有专用hook与此一致；不能套美版B_BUFF3。",
    "action": "intentional_adaptation"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_BUFF1}获得了{B_BUFF2}\n{B_BUFF3}经验值！\\p"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_BUFF1}{B_BUFF2}　けいけんちを　もらった！\\p"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnGainedEXP",
      "file": "patch/batches/178_battle_victory.json",
      "payload_address": "0x0903C311",
      "payload_sha256": "0572b6d3499b1fcbf482c4889b942c837c17d25942b64bb2da9ff3e12e7d4b60",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB3E0",
          "original": "0x085A962B",
          "target": "0x0903C311",
          "batch": "patch/batches/178_battle_victory.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5345 行 · ported_batch / 4092 · sText_PlayerGotMoney

判定：`intentional_adaptation`

理由：数字后显示円是用户要求且符合日版原文；不恢复美版前置金额符号。

日文：

```text
{B_PLAYER_NAME}は　しょうきんとして\n{B_BUFF1}¥　てにいれた！\p
```

英文：

```text
{B_PLAYER_NAME} got ¥{B_BUFF1}\nfor winning!\p
```

报告原中文：

```text
作为奖金，\n{B_PLAYER_NAME}获得了{B_BUFF1}{JPN}¥{ENG}！\p$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 5345,
    "symbol": "sText_PlayerGotMoney",
    "domain": "ported_batch",
    "idx": "4092",
    "reason": "数字后显示円是用户要求且符合日版原文；不恢复美版前置金额符号。",
    "action": "intentional_adaptation"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "作为奖金，\n{B_PLAYER_NAME}获得了¥{B_BUFF1}！\\p"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_PLAYER_NAME}は　しょうきんとして\n{B_BUFF1}¥　てにいれた！\\p"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PlayerGotMoney",
      "file": "patch/batches/178_battle_victory.json",
      "payload_address": "0x0903C442",
      "payload_sha256": "eaaef6908caeb7774bdd0e08aa0a88b2b9bf3425ba8bda5550d8e94d53040ce6",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB424",
          "original": "0x085A97B2",
          "target": "0x0903C442",
          "batch": "patch/batches/178_battle_victory.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5346 行 · ported_batch / 4093 · sText_PlayerPickedUpMoney

判定：`intentional_adaptation`

理由：数字后显示円是用户要求且符合日版原文；不恢复美版前置金额符号。

日文：

```text
{B_PLAYER_NAME}は　{B_BUFF1}¥\nひろった！\p
```

英文：

```text
{B_PLAYER_NAME} picked up\n¥{B_BUFF1}!\p
```

报告原中文：

```text
{B_PLAYER_NAME}捡到了\n{B_BUFF1}{JPN}¥{ENG}！\p$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 5346,
    "symbol": "sText_PlayerPickedUpMoney",
    "domain": "ported_batch",
    "idx": "4093",
    "reason": "数字后显示円是用户要求且符合日版原文；不恢复美版前置金额符号。",
    "action": "intentional_adaptation"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_PLAYER_NAME}捡到了\n¥{B_BUFF1}！\\p"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_PLAYER_NAME}は　{B_BUFF1}¥\nひろった！\\p"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PlayerPickedUpMoney",
      "file": "patch/batches/178_battle_victory.json",
      "payload_address": "0x0903C46A",
      "payload_sha256": "361daefa1b321748fa83919e7c915ca721eb9fca5ceab63a9c52707bda74888a",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB598",
          "original": "0x085A9EE5",
          "target": "0x0903C46A",
          "batch": "patch/batches/178_battle_victory.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5355 行 · ported_batch / 4102 · BerryTree_Text_BerryGrowthStage3

判定：`fixed_verified`

理由：报告理由串成华丽大赛；实际日文みきが大きくなってきた指树干长大。

日文：

```text
{STR_VAR_1}の　みきが　おおきく　なってきた！$
```

英文：

```text
This {STR_VAR_1} plant is growing taller.$
```

报告原中文：

```text
{STR_VAR_1}的幼苗长得很漂亮！$
```

修复前实际中文：

```text
{STR_VAR_1}的幼苗长得很漂亮！
```

最终中文：

```text
{STR_VAR_1}的树干长高了！
```

证据：

```json
{
  "review": {
    "row_number": 5355,
    "symbol": "BerryTree_Text_BerryGrowthStage3",
    "domain": "ported_batch",
    "idx": "4102",
    "old": "的幼苗长得很漂亮！",
    "new": "的树干长高了！",
    "reason": "报告理由串成华丽大赛；实际日文みきが大きくなってきた指树干长大。",
    "scope": "both",
    "action": "fix",
    "final_text": "{STR_VAR_1}的树干长高了！",
    "old_current_text": "{STR_VAR_1}的幼苗长得很漂亮！",
    "changed_files": [
      "../pokeemerald_us_chs/data/scripts/berry_tree.inc",
      "patch/batches/179_berry.json"
    ],
    "us_source_file": "data/scripts/berry_tree.inc",
    "jp_source": [
      {
        "file": "data/scripts/berry_tree.inc",
        "text": "{STR_VAR_1}の　みきが　おおきく　なってきた！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/scripts/berry_tree.inc",
        "text": "{STR_VAR_1}的树干长高了！${STR_VAR_1}正在变得更高。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/scripts/berry_tree.inc",
        "text": "{STR_VAR_1}の　みきが　おおきく　なってきた！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BerryTree_Text_BerryGrowthStage3",
      "file": "patch/batches/179_berry.json",
      "payload_address": "0x0903C53B",
      "payload_sha256": "279bc5b86361d990067cef2f5e0f63a5c38b60637fa1910f043c0f10c4138c41",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08244DF7",
          "original": "0x08244F5A",
          "target": "0x0903C53B",
          "batch": "patch/batches/179_berry.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5356 行 · ported_batch / 4103 · BerryTree_Text_BerryGrowthStage4

判定：`fixed_verified`

理由：实际原文花朵开放程度由STR_VAR_2提供；核验生产者后补回，不采用报告表演文本。

日文：

```text
{STR_VAR_1}の　はなが　{STR_VAR_2}　さいてる！$
```

英文：

```text
These {STR_VAR_1} flowers are blooming\n{STR_VAR_2}.$
```

报告原中文：

```text
{STR_VAR_1}开花了！$
```

修复前实际中文：

```text
{STR_VAR_1}开花了！
```

最终中文：

```text
{STR_VAR_1}的花
{STR_VAR_2}盛开着！
```

证据：

```json
{
  "review": {
    "row_number": 5356,
    "symbol": "BerryTree_Text_BerryGrowthStage4",
    "domain": "ported_batch",
    "idx": "4103",
    "old": "{STR_VAR_1}开花了！",
    "new": "{STR_VAR_1}的花\n{STR_VAR_2}盛开着！",
    "reason": "实际原文花朵开放程度由STR_VAR_2提供；核验生产者后补回，不采用报告表演文本。",
    "scope": "both",
    "action": "fix",
    "final_text": "{STR_VAR_1}的花\n{STR_VAR_2}盛开着！",
    "old_current_text": "{STR_VAR_1}开花了！",
    "changed_files": [
      "../pokeemerald_us_chs/data/scripts/berry_tree.inc",
      "patch/batches/179_berry.json"
    ],
    "us_source_file": "data/scripts/berry_tree.inc",
    "jp_source": [
      {
        "file": "data/scripts/berry_tree.inc",
        "text": "{STR_VAR_1}の　はなが　{STR_VAR_2}　さいてる！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/scripts/berry_tree.inc",
        "text": "{STR_VAR_1}的花\n{STR_VAR_2}盛开着！${STR_VAR_1}的花正在{STR_VAR_2}盛开\n。"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/scripts/berry_tree.inc",
        "text": "{STR_VAR_1}の　はなが　{STR_VAR_2}　さいてる！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BerryTree_Text_BerryGrowthStage4",
      "file": "patch/batches/179_berry.json",
      "payload_address": "0x0903C54E",
      "payload_sha256": "05dee9ca53c6849d3b5bd9cbc6d118db0236813e2be8235b295ed0aa9e659007",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08244E09",
          "original": "0x08244F6E",
          "target": "0x0903C54E",
          "batch": "patch/batches/179_berry.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5393 行 · ported_batch / 4140 · BattleFrontier_Lounge5_Text_NatureGirlNaive

判定：`mapping_artifact`

理由：报告引用不存在的独立符号；性格女孩实际由25项已重定向指针表提供，并含合并原文。

日文：

```text

```

英文：

```text

```

报告原中文：

```text

```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 5393,
    "symbol": "BattleFrontier_Lounge5_Text_NatureGirlNaive",
    "domain": "ported_batch",
    "idx": "4140",
    "reason": "报告引用不存在的独立符号；性格女孩实际由25项已重定向指针表提供，并含合并原文。",
    "action": "mapping_artifact"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": []
}
```

### CSV 第 5396 行 · ported_batch / 4143 · BattleFrontier_Lounge5_Text_NatureGirlQuiet

判定：`mapping_artifact`

理由：报告引用不存在的独立符号；性格女孩实际由25项已重定向指针表提供，并含合并原文。

日文：

```text

```

英文：

```text

```

报告原中文：

```text

```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 5396,
    "symbol": "BattleFrontier_Lounge5_Text_NatureGirlQuiet",
    "domain": "ported_batch",
    "idx": "4143",
    "reason": "报告引用不存在的独立符号；性格女孩实际由25项已重定向指针表提供，并含合并原文。",
    "action": "mapping_artifact"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": []
}
```

### CSV 第 5422 行 · ported_batch / 4170 · sText_PkmnHurtsWith

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_DEF_NAME_WITH_PREFIX}の　{B_DEF_ABILITY}で\n{B_ATK_NAME_WITH_PREFIX}は　きずついた！
```

英文：

```text
{B_DEF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nhurt {B_ATK_NAME_WITH_PREFIX}!
```

报告原中文：

```text
{B_DEF_NAME_WITH_PREFIX}\n因{B_DEF_ABILITY}的{B_ATK_NAME_WITH_PREFIX}\l而受到了伤害！
```

修复前实际中文：

```text
{B_DEF_NAME_WITH_PREFIX}
因{B_DEF_ABILITY}的{B_ATK_NAME_WITH_PREFIX}\l而受到了伤害！
```

最终中文：

```text
{B_ATK_NAME_WITH_PREFIX}因
{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}\l而受到了伤害！
```

证据：

```json
{
  "review": {
    "row_number": 5422,
    "symbol": "sText_PkmnHurtsWith",
    "domain": "ported_batch",
    "idx": "4170",
    "old": null,
    "new": "{B_ATK_NAME_WITH_PREFIX}因\n{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}\\l而受到了伤害！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_ATK_NAME_WITH_PREFIX}因\n{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}\\l而受到了伤害！",
    "old_current_text": "{B_DEF_NAME_WITH_PREFIX}\n因{B_DEF_ABILITY}的{B_ATK_NAME_WITH_PREFIX}\\l而受到了伤害！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/188_battle_damage_messages.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}の　{B_DEF_ABILITY}で\n{B_ATK_NAME_WITH_PREFIX}は　きずついた！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_ATK_NAME_WITH_PREFIX}因\n{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}\\l而受到了伤害！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}の　{B_DEF_ABILITY}で\n{B_ATK_NAME_WITH_PREFIX}は　きずついた！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnHurtsWith",
      "file": "patch/batches/188_battle_damage_messages.json",
      "payload_address": "0x0903C911",
      "payload_sha256": "5cb96a8c7eb5839ddf3fb51b5d9b154398e6313d58d78ceec3ea5e2c2da55498",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB6E8",
          "original": "0x085AA6C6",
          "target": "0x0903C911",
          "batch": "patch/batches/188_battle_damage_messages.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5438 行 · ported_batch / 4186 · sText_PkmnPoisonedBy

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}の　{B_SCR_ACTIVE_ABILITY}で\n{B_EFF_NAME_WITH_PREFIX}は　どくをあびた！
```

英文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\npoisoned {B_EFF_NAME_WITH_PREFIX}!
```

报告原中文：

```text
因{B_EFF_NAME_WITH_PREFIX}的{B_SCR_ACTIVE_NAME_WITH_PREFIX}，\n{B_SCR_ACTIVE_ABILITY}中毒了！
```

修复前实际中文：

```text
因{B_EFF_NAME_WITH_PREFIX}的{B_SCR_ACTIVE_NAME_WITH_PREFIX}，
{B_SCR_ACTIVE_ABILITY}中毒了！
```

最终中文：

```text
{B_EFF_NAME_WITH_PREFIX}因
{B_SCR_ACTIVE_NAME_WITH_PREFIX}的{B_SCR_ACTIVE_ABILITY}\l而中毒了！
```

证据：

```json
{
  "review": {
    "row_number": 5438,
    "symbol": "sText_PkmnPoisonedBy",
    "domain": "ported_batch",
    "idx": "4186",
    "old": null,
    "new": "{B_EFF_NAME_WITH_PREFIX}因\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}的{B_SCR_ACTIVE_ABILITY}\\l而中毒了！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_EFF_NAME_WITH_PREFIX}因\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}的{B_SCR_ACTIVE_ABILITY}\\l而中毒了！",
    "old_current_text": "因{B_EFF_NAME_WITH_PREFIX}的{B_SCR_ACTIVE_NAME_WITH_PREFIX}，\n{B_SCR_ACTIVE_ABILITY}中毒了！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/189_battle_status_and_core_results.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}の　{B_SCR_ACTIVE_ABILITY}で\n{B_EFF_NAME_WITH_PREFIX}は　どくをあびた！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_EFF_NAME_WITH_PREFIX}因\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}的{B_SCR_ACTIVE_ABILITY}\\l而中毒了！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}の　{B_SCR_ACTIVE_ABILITY}で\n{B_EFF_NAME_WITH_PREFIX}は　どくをあびた！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnPoisonedBy",
      "file": "patch/batches/189_battle_status_and_core_results.json",
      "payload_address": "0x0903CABC",
      "payload_sha256": "b4e1fc99b589661b5c1b3c4479b088982aff2ba8400e78f810164e96e951e353",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB450",
          "original": "0x085A988E",
          "target": "0x0903CABC",
          "batch": "patch/batches/189_battle_status_and_core_results.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5465 行 · ported_batch / 4213 · sText_PkmnInLove

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_ATK_NAME_WITH_PREFIX}は\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}に　メロメロだ！
```

英文：

```text
{B_ATK_NAME_WITH_PREFIX} is in love\nwith {B_SCR_ACTIVE_NAME_WITH_PREFIX}!
```

报告原中文：

```text
{B_ATK_NAME_WITH_PREFIX}让\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}着迷了！
```

修复前实际中文：

```text
{B_ATK_NAME_WITH_PREFIX}让
{B_SCR_ACTIVE_NAME_WITH_PREFIX}着迷了！
```

最终中文：

```text
{B_ATK_NAME_WITH_PREFIX}对
{B_SCR_ACTIVE_NAME_WITH_PREFIX}着迷了！
```

证据：

```json
{
  "review": {
    "row_number": 5465,
    "symbol": "sText_PkmnInLove",
    "domain": "ported_batch",
    "idx": "4213",
    "old": null,
    "new": "{B_ATK_NAME_WITH_PREFIX}对\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}着迷了！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_ATK_NAME_WITH_PREFIX}对\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}着迷了！",
    "old_current_text": "{B_ATK_NAME_WITH_PREFIX}让\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}着迷了！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/189_battle_status_and_core_results.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_ATK_NAME_WITH_PREFIX}は\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}に　メロメロだ！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_ATK_NAME_WITH_PREFIX}对\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}着迷了！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_ATK_NAME_WITH_PREFIX}は\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}に　メロメロだ！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnInLove",
      "file": "patch/batches/189_battle_status_and_core_results.json",
      "payload_address": "0x0903CDAC",
      "payload_sha256": "51198eb1c0d9fd0546ccfde062d507d2d52556d96f7c87602c52f4a230bd605d",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB4C4",
          "original": "0x085A9AA2",
          "target": "0x0903CDAC",
          "batch": "patch/batches/189_battle_status_and_core_results.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5488 行 · ported_batch / 4236 · sText_PkmnClamped

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_DEF_NAME_WITH_PREFIX}は　{B_ATK_NAME_WITH_PREFIX}の\nからに　はさまれた！
```

英文：

```text
{B_ATK_NAME_WITH_PREFIX} CLAMPED\n{B_DEF_NAME_WITH_PREFIX}!
```

报告原中文：

```text
{B_ATK_NAME_WITH_PREFIX}\n被{B_DEF_NAME_WITH_PREFIX}的贝壳夹住了！
```

修复前实际中文：

```text
{B_ATK_NAME_WITH_PREFIX}
被{B_DEF_NAME_WITH_PREFIX}的贝壳夹住了！
```

最终中文：

```text
{B_DEF_NAME_WITH_PREFIX}
被{B_ATK_NAME_WITH_PREFIX}的贝壳夹住了！
```

证据：

```json
{
  "review": {
    "row_number": 5488,
    "symbol": "sText_PkmnClamped",
    "domain": "ported_batch",
    "idx": "4236",
    "old": null,
    "new": "{B_DEF_NAME_WITH_PREFIX}\n被{B_ATK_NAME_WITH_PREFIX}的贝壳夹住了！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_DEF_NAME_WITH_PREFIX}\n被{B_ATK_NAME_WITH_PREFIX}的贝壳夹住了！",
    "old_current_text": "{B_ATK_NAME_WITH_PREFIX}\n被{B_DEF_NAME_WITH_PREFIX}的贝壳夹住了！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/190_battle_move_effects.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_ATK_NAME_WITH_PREFIX}の\nからに　はさまれた！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}\n被{B_ATK_NAME_WITH_PREFIX}的贝壳夹住了！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_ATK_NAME_WITH_PREFIX}の\nからに　はさまれた！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnClamped",
      "file": "patch/batches/190_battle_move_effects.json",
      "payload_address": "0x0903D02C",
      "payload_sha256": "5f5b35bc7aede49afb01f483c71435940a3386828edd05511251c4d3b67fa6aa",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB520",
          "original": "0x085A9CC2",
          "target": "0x0903D02C",
          "batch": "patch/batches/190_battle_move_effects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5512 行 · ported_batch / 4260 · sText_PkmnStayedAwakeUsing

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_DEF_NAME_WITH_PREFIX}は\n{B_DEF_ABILITY}で　ねむらない！
```

英文：

```text
{B_DEF_NAME_WITH_PREFIX} stayed awake\nusing its {B_DEF_ABILITY}!
```

报告原中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，\n{B_DEF_ABILITY}不会睡着！
```

修复前实际中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，
{B_DEF_ABILITY}不会睡着！
```

最终中文：

```text
{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}
不会睡着！
```

证据：

```json
{
  "review": {
    "row_number": 5512,
    "symbol": "sText_PkmnStayedAwakeUsing",
    "domain": "ported_batch",
    "idx": "4260",
    "old": null,
    "new": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会睡着！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会睡着！",
    "old_current_text": "因为{B_DEF_NAME_WITH_PREFIX}，\n{B_DEF_ABILITY}不会睡着！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/190_battle_move_effects.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は\n{B_DEF_ABILITY}で　ねむらない！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会睡着！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は\n{B_DEF_ABILITY}で　ねむらない！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnStayedAwakeUsing",
      "file": "patch/batches/190_battle_move_effects.json",
      "payload_address": "0x0903D2B1",
      "payload_sha256": "bd975132593b5c5f90e382ab0cc862b3b339c0ad662d086d41876f2a2f427cc7",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB588",
          "original": "0x085A9EA8",
          "target": "0x0903D2B1",
          "batch": "patch/batches/190_battle_move_effects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5585 行 · ported_batch / 4333 · sText_PkmnRaisedSpeed

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\nすばやさが　あがった！
```

英文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\nraised its SPEED!
```

报告原中文：

```text
因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的\n速度提高了！
```

修复前实际中文：

```text
因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的
速度提高了！
```

最终中文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}
速度提高了！
```

证据：

```json
{
  "review": {
    "row_number": 5585,
    "symbol": "sText_PkmnRaisedSpeed",
    "domain": "ported_batch",
    "idx": "4333",
    "old": null,
    "new": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n速度提高了！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n速度提高了！",
    "old_current_text": "因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的\n速度提高了！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/191_battle_moves_abilities_results.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\nすばやさが　あがった！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n速度提高了！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\nすばやさが　あがった！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnRaisedSpeed",
      "file": "patch/batches/191_battle_moves_abilities_results.json",
      "payload_address": "0x0903DB03",
      "payload_sha256": "f88f339e9050b56534ecb64994ebb76f77a69d415fffc850ff80f6f2f7dafecc",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB6B4",
          "original": "0x085AA5B0",
          "target": "0x0903DB03",
          "batch": "patch/batches/191_battle_moves_abilities_results.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5588 行 · ported_batch / 4336 · sText_PkmnRestoredHPUsing

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nかいふくした！
```

英文：

```text
{B_DEF_NAME_WITH_PREFIX} restored HP\nusing its {B_DEF_ABILITY}!
```

报告原中文：

```text
因{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}的\n体力回复了！
```

修复前实际中文：

```text
因{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}的
体力回复了！
```

最终中文：

```text
{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}
体力回复了！
```

证据：

```json
{
  "review": {
    "row_number": 5588,
    "symbol": "sText_PkmnRestoredHPUsing",
    "domain": "ported_batch",
    "idx": "4336",
    "old": null,
    "new": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n体力回复了！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n体力回复了！",
    "old_current_text": "因{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}的\n体力回复了！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/191_battle_moves_abilities_results.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nかいふくした！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n体力回复了！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nかいふくした！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnRestoredHPUsing",
      "file": "patch/batches/191_battle_moves_abilities_results.json",
      "payload_address": "0x0903DB6C",
      "payload_sha256": "17ac975f275ef8e556b31d8c7109042614a1b3aa6f08c0346d4c77dbfa0ea269",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB6C0",
          "original": "0x085AA5EA",
          "target": "0x0903DB6C",
          "batch": "patch/batches/191_battle_moves_abilities_results.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5589 行 · ported_batch / 4337 · sText_PkmnChangedTypeWith

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\n{B_BUFF1}タイプに　なった！
```

英文：

```text
{B_DEF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nmade it the {B_BUFF1} type!
```

报告原中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n变成了{B_BUFF1}属性！
```

修复前实际中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}
变成了{B_BUFF1}属性！
```

最终中文：

```text
{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}
变成了{B_BUFF1}属性！
```

证据：

```json
{
  "review": {
    "row_number": 5589,
    "symbol": "sText_PkmnChangedTypeWith",
    "domain": "ported_batch",
    "idx": "4337",
    "old": null,
    "new": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n变成了{B_BUFF1}属性！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n变成了{B_BUFF1}属性！",
    "old_current_text": "因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n变成了{B_BUFF1}属性！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/191_battle_moves_abilities_results.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\n{B_BUFF1}タイプに　なった！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n变成了{B_BUFF1}属性！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\n{B_BUFF1}タイプに　なった！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnChangedTypeWith",
      "file": "patch/batches/191_battle_moves_abilities_results.json",
      "payload_address": "0x0903DB8A",
      "payload_sha256": "6da98ff85c7ef745774ca787d253b62aec14b37fec185dad1729ff6b49b622a4",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB6C4",
          "original": "0x085AA611",
          "target": "0x0903DB8A",
          "batch": "patch/batches/191_battle_moves_abilities_results.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5590 行 · ported_batch / 4338 · sText_PkmnPreventsParalysisWith

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_EFF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nまひしない！
```

英文：

```text
{B_EFF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nprevents paralysis!
```

报告原中文：

```text
因为{B_EFF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n不会麻痹！
```

修复前实际中文：

```text
因为{B_EFF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}
不会麻痹！
```

最终中文：

```text
{B_EFF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}
不会麻痹！
```

证据：

```json
{
  "review": {
    "row_number": 5590,
    "symbol": "sText_PkmnPreventsParalysisWith",
    "domain": "ported_batch",
    "idx": "4338",
    "old": null,
    "new": "{B_EFF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会麻痹！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_EFF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会麻痹！",
    "old_current_text": "因为{B_EFF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n不会麻痹！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/191_battle_moves_abilities_results.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_EFF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nまひしない！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_EFF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会麻痹！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_EFF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nまひしない！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnPreventsParalysisWith",
      "file": "patch/batches/191_battle_moves_abilities_results.json",
      "payload_address": "0x0903DBAE",
      "payload_sha256": "1c32d52cdfb1dba08e93d445df1aa04edee0dff523901d78f3ba0de2f764b8f8",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB6C8",
          "original": "0x085AA625",
          "target": "0x0903DBAE",
          "batch": "patch/batches/191_battle_moves_abilities_results.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5591 行 · ported_batch / 4339 · sText_PkmnPreventsRomanceWith

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nメロメロに　ならない！
```

英文：

```text
{B_DEF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nprevents romance!
```

报告原中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n不会着迷！
```

修复前实际中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}
不会着迷！
```

最终中文：

```text
{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}
不会着迷！
```

证据：

```json
{
  "review": {
    "row_number": 5591,
    "symbol": "sText_PkmnPreventsRomanceWith",
    "domain": "ported_batch",
    "idx": "4339",
    "old": null,
    "new": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会着迷！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会着迷！",
    "old_current_text": "因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n不会着迷！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/191_battle_moves_abilities_results.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nメロメロに　ならない！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会着迷！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nメロメロに　ならない！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnPreventsRomanceWith",
      "file": "patch/batches/191_battle_moves_abilities_results.json",
      "payload_address": "0x0903DBCA",
      "payload_sha256": "22b6cd8b12b23deca500a11ab1808b32e367ac01be90d4507d84fb37570e8e68",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB6CC",
          "original": "0x085AA634",
          "target": "0x0903DBCA",
          "batch": "patch/batches/191_battle_moves_abilities_results.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5592 行 · ported_batch / 4340 · sText_PkmnPreventsPoisoningWith

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_EFF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nどくを　うけない！
```

英文：

```text
{B_EFF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nprevents poisoning!
```

报告原中文：

```text
因为{B_EFF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n不会中毒！
```

修复前实际中文：

```text
因为{B_EFF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}
不会中毒！
```

最终中文：

```text
{B_EFF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}
不会中毒！
```

证据：

```json
{
  "review": {
    "row_number": 5592,
    "symbol": "sText_PkmnPreventsPoisoningWith",
    "domain": "ported_batch",
    "idx": "4340",
    "old": null,
    "new": "{B_EFF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会中毒！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_EFF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会中毒！",
    "old_current_text": "因为{B_EFF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n不会中毒！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/191_battle_moves_abilities_results.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_EFF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nどくを　うけない！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_EFF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会中毒！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_EFF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nどくを　うけない！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnPreventsPoisoningWith",
      "file": "patch/batches/191_battle_moves_abilities_results.json",
      "payload_address": "0x0903DBE6",
      "payload_sha256": "1d128557d5e342a24375f1efecb040a691971fa5a94fbc233dabf3ca4b1e89d0",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB6D0",
          "original": "0x085AA648",
          "target": "0x0903DBE6",
          "batch": "patch/batches/191_battle_moves_abilities_results.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5593 行 · ported_batch / 4341 · sText_PkmnPreventsConfusionWith

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nこんらんしない！
```

英文：

```text
{B_DEF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nprevents confusion!
```

报告原中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n不会混乱！
```

修复前实际中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}
不会混乱！
```

最终中文：

```text
{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}
不会混乱！
```

证据：

```json
{
  "review": {
    "row_number": 5593,
    "symbol": "sText_PkmnPreventsConfusionWith",
    "domain": "ported_batch",
    "idx": "4341",
    "old": null,
    "new": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会混乱！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会混乱！",
    "old_current_text": "因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n不会混乱！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/191_battle_moves_abilities_results.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nこんらんしない！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会混乱！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nこんらんしない！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnPreventsConfusionWith",
      "file": "patch/batches/191_battle_moves_abilities_results.json",
      "payload_address": "0x0903DC02",
      "payload_sha256": "3d1f5aba721b983d7ef480b2091fa6327a0f99f47507ccdb9db895c00fbc8556",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB6D4",
          "original": "0x085AA65A",
          "target": "0x0903DC02",
          "batch": "patch/batches/191_battle_moves_abilities_results.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5597 行 · ported_batch / 4345 · sText_PkmnPreventsStatLossWith

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\nのうりょくが　さがらない！
```

英文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\nprevents stat loss!
```

报告原中文：

```text
因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的\n能力不会降低！
```

修复前实际中文：

```text
因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的
能力不会降低！
```

最终中文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}
能力不会降低！
```

证据：

```json
{
  "review": {
    "row_number": 5597,
    "symbol": "sText_PkmnPreventsStatLossWith",
    "domain": "ported_batch",
    "idx": "4345",
    "old": null,
    "new": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n能力不会降低！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n能力不会降低！",
    "old_current_text": "因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的\n能力不会降低！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/191_battle_moves_abilities_results.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\nのうりょくが　さがらない！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n能力不会降低！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\nのうりょくが　さがらない！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnPreventsStatLossWith",
      "file": "patch/batches/191_battle_moves_abilities_results.json",
      "payload_address": "0x0903DC90",
      "payload_sha256": "12f494a52fc0208498430f2f54a72ee190f1bd19dcd75f6bc537d9c15aab9c74",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB6E4",
          "original": "0x085AA6B0",
          "target": "0x0903DC90",
          "batch": "patch/batches/191_battle_moves_abilities_results.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5686 行 · ported_batch / 4434 · sText_PkmnsXPreventsBurns

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_EFF_NAME_WITH_PREFIX}は　{B_EFF_ABILITY}で\nやけどしない！
```

英文：

```text
{B_EFF_NAME_WITH_PREFIX}'s {B_EFF_ABILITY}\nprevents burns!
```

报告原中文：

```text
因为{B_EFF_NAME_WITH_PREFIX}，{B_EFF_ABILITY}\n不会灼伤！
```

修复前实际中文：

```text
因为{B_EFF_NAME_WITH_PREFIX}，{B_EFF_ABILITY}
不会灼伤！
```

最终中文：

```text
{B_EFF_NAME_WITH_PREFIX}因{B_EFF_ABILITY}
不会灼伤！
```

证据：

```json
{
  "review": {
    "row_number": 5686,
    "symbol": "sText_PkmnsXPreventsBurns",
    "domain": "ported_batch",
    "idx": "4434",
    "old": null,
    "new": "{B_EFF_NAME_WITH_PREFIX}因{B_EFF_ABILITY}\n不会灼伤！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_EFF_NAME_WITH_PREFIX}因{B_EFF_ABILITY}\n不会灼伤！",
    "old_current_text": "因为{B_EFF_NAME_WITH_PREFIX}，{B_EFF_ABILITY}\n不会灼伤！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/193_battle_safari_item_effects.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_EFF_NAME_WITH_PREFIX}は　{B_EFF_ABILITY}で\nやけどしない！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_EFF_NAME_WITH_PREFIX}因{B_EFF_ABILITY}\n不会灼伤！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_EFF_NAME_WITH_PREFIX}は　{B_EFF_ABILITY}で\nやけどしない！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnsXPreventsBurns",
      "file": "patch/batches/193_battle_safari_item_effects.json",
      "payload_address": "0x0903E540",
      "payload_sha256": "042df14c1e98a36f1aa37956ce98838da9ca73ce61809668f781ec43268b4ef2",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB870",
          "original": "0x085AA6ED",
          "target": "0x0903E540",
          "batch": "patch/batches/193_battle_safari_item_effects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5687 行 · ported_batch / 4435 · sText_PkmnsXBlocksY

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\n{B_CURRENT_MOVE}を　うけない！
```

英文：

```text
{B_DEF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\nblocks {B_CURRENT_MOVE}!
```

报告原中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n抵御了{B_CURRENT_MOVE}！
```

修复前实际中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}
抵御了{B_CURRENT_MOVE}！
```

最终中文：

```text
{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}
抵御了{B_CURRENT_MOVE}！
```

证据：

```json
{
  "review": {
    "row_number": 5687,
    "symbol": "sText_PkmnsXBlocksY",
    "domain": "ported_batch",
    "idx": "4435",
    "old": null,
    "new": "{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}\n抵御了{B_CURRENT_MOVE}！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}\n抵御了{B_CURRENT_MOVE}！",
    "old_current_text": "因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n抵御了{B_CURRENT_MOVE}！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/193_battle_safari_item_effects.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\n{B_CURRENT_MOVE}を　うけない！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}\n抵御了{B_CURRENT_MOVE}！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\n{B_CURRENT_MOVE}を　うけない！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnsXBlocksY",
      "file": "patch/batches/193_battle_safari_item_effects.json",
      "payload_address": "0x0903E55C",
      "payload_sha256": "55e0f38220ec01f58398004e32600c0bc27e258065231700f4cd764e6d6b1a49",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB874",
          "original": "0x085AA6FD",
          "target": "0x0903E55C",
          "batch": "patch/batches/193_battle_safari_item_effects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5688 行 · ported_batch / 4436 · sText_PkmnsXRestoredHPALittle2

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_ATK_NAME_WITH_PREFIX}は　{B_ATK_ABILITY}で\nすこし　かいふく
```

英文：

```text
{B_ATK_NAME_WITH_PREFIX}'s {B_ATK_ABILITY}\nrestored its HP a little!
```

报告原中文：

```text
因为{B_ATK_NAME_WITH_PREFIX}，{B_ATK_ABILITY}\n回复了少许HP。
```

修复前实际中文：

```text
因为{B_ATK_NAME_WITH_PREFIX}，{B_ATK_ABILITY}
回复了少许HP。
```

最终中文：

```text
{B_ATK_NAME_WITH_PREFIX}因{B_ATK_ABILITY}
回复了少许HP。
```

证据：

```json
{
  "review": {
    "row_number": 5688,
    "symbol": "sText_PkmnsXRestoredHPALittle2",
    "domain": "ported_batch",
    "idx": "4436",
    "old": null,
    "new": "{B_ATK_NAME_WITH_PREFIX}因{B_ATK_ABILITY}\n回复了少许HP。",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_ATK_NAME_WITH_PREFIX}因{B_ATK_ABILITY}\n回复了少许HP。",
    "old_current_text": "因为{B_ATK_NAME_WITH_PREFIX}，{B_ATK_ABILITY}\n回复了少许HP。",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/193_battle_safari_item_effects.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_ATK_NAME_WITH_PREFIX}は　{B_ATK_ABILITY}で\nすこし　かいふく"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_ATK_NAME_WITH_PREFIX}因{B_ATK_ABILITY}\n回复了少许HP。"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_ATK_NAME_WITH_PREFIX}は　{B_ATK_ABILITY}で\nすこし　かいふく"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnsXRestoredHPALittle2",
      "file": "patch/batches/193_battle_safari_item_effects.json",
      "payload_address": "0x0903E57C",
      "payload_sha256": "a3284f279212a2722d0bad27970d2c6611b142bbef0923e3c52ea397b48fa54f",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB878",
          "original": "0x085AA721",
          "target": "0x0903E57C",
          "batch": "patch/batches/193_battle_safari_item_effects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5690 行 · ported_batch / 4438 · sText_PkmnsXPreventsYLoss

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_BUFF1}が　さがらない！
```

英文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\nprevents {B_BUFF1} loss!
```

报告原中文：

```text
因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的\n{B_BUFF1}不会降低！
```

修复前实际中文：

```text
因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的
{B_BUFF1}不会降低！
```

最终中文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}
{B_BUFF1}不会降低！
```

证据：

```json
{
  "review": {
    "row_number": 5690,
    "symbol": "sText_PkmnsXPreventsYLoss",
    "domain": "ported_batch",
    "idx": "4438",
    "old": null,
    "new": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n{B_BUFF1}不会降低！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n{B_BUFF1}不会降低！",
    "old_current_text": "因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的\n{B_BUFF1}不会降低！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/193_battle_safari_item_effects.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_BUFF1}が　さがらない！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n{B_BUFF1}不会降低！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_BUFF1}が　さがらない！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnsXPreventsYLoss",
      "file": "patch/batches/193_battle_safari_item_effects.json",
      "payload_address": "0x0903E5C0",
      "payload_sha256": "e581b80ae5516a9dee72425dd1fb84c77e3615202488c357426410d356018513",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB880",
          "original": "0x085AA75B",
          "target": "0x0903E5C0",
          "batch": "patch/batches/193_battle_safari_item_effects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5693 行 · ported_batch / 4441 · sText_PkmnsXCuredYProblem

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_BUFF1}じょうたいが　なおった！
```

英文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\ncured its {B_BUFF1} problem!
```

报告原中文：

```text
因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的\n{B_BUFF1}状态治愈了！
```

修复前实际中文：

```text
因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的
{B_BUFF1}状态治愈了！
```

最终中文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}
解除了{B_BUFF1}状态！
```

证据：

```json
{
  "review": {
    "row_number": 5693,
    "symbol": "sText_PkmnsXCuredYProblem",
    "domain": "ported_batch",
    "idx": "4441",
    "old": null,
    "new": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n解除了{B_BUFF1}状态！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n解除了{B_BUFF1}状态！",
    "old_current_text": "因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的\n{B_BUFF1}状态治愈了！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/193_battle_safari_item_effects.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_BUFF1}じょうたいが　なおった！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n解除了{B_BUFF1}状态！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_BUFF1}じょうたいが　なおった！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnsXCuredYProblem",
      "file": "patch/batches/193_battle_safari_item_effects.json",
      "payload_address": "0x0903E62A",
      "payload_sha256": "c1ab43f09dffcddffe68bea66c166c2135bf02768ab0766de07c0a9276143c3a",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB88C",
          "original": "0x085AA797",
          "target": "0x0903E62A",
          "batch": "patch/batches/193_battle_safari_item_effects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5705 行 · ported_batch / 4453 · sText_UsingItemTheStatOfPkmnRose

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_LAST_ITEM}で\n{B_BUFF1}が　{B_BUFF2}
```

英文：

```text
Using {B_LAST_ITEM}, the {B_BUFF1}\nof {B_SCR_ACTIVE_NAME_WITH_PREFIX} {B_BUFF2}
```

报告原中文：

```text
因为{B_LAST_ITEM}，{B_BUFF1}的\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}{B_BUFF2}
```

修复前实际中文：

```text
因为{B_LAST_ITEM}，{B_BUFF1}的
{B_SCR_ACTIVE_NAME_WITH_PREFIX}{B_BUFF2}
```

最终中文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}使用{B_LAST_ITEM}，
{B_BUFF1}{B_BUFF2}
```

证据：

```json
{
  "review": {
    "row_number": 5705,
    "symbol": "sText_UsingItemTheStatOfPkmnRose",
    "domain": "ported_batch",
    "idx": "4453",
    "old": null,
    "new": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}使用{B_LAST_ITEM}，\n{B_BUFF1}{B_BUFF2}",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}使用{B_LAST_ITEM}，\n{B_BUFF1}{B_BUFF2}",
    "old_current_text": "因为{B_LAST_ITEM}，{B_BUFF1}的\n{B_SCR_ACTIVE_NAME_WITH_PREFIX}{B_BUFF2}",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/193_battle_safari_item_effects.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_LAST_ITEM}で\n{B_BUFF1}が　{B_BUFF2}"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}使用{B_LAST_ITEM}，\n{B_BUFF1}{B_BUFF2}"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_LAST_ITEM}で\n{B_BUFF1}が　{B_BUFF2}"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_UsingItemTheStatOfPkmnRose",
      "file": "patch/batches/193_battle_safari_item_effects.json",
      "payload_address": "0x0903E759",
      "payload_sha256": "2b95ad392eae1a9cb7aebe2f35e6e85f002b76f43caf785e6b10381e47d66769",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB8C0",
          "original": "0x085AA89F",
          "target": "0x0903E759",
          "batch": "patch/batches/193_battle_safari_item_effects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5709 行 · ported_batch / 4457 · sText_EmptyString4

判定：`no_text`

理由：空战斗字符串为占位；须按表槽和EOS识别，不能把相邻は片段当作文本内容。

日文：

```text
は\n$
```

英文：

```text

```

报告原中文：

```text

```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 5709,
    "symbol": "sText_EmptyString4",
    "domain": "ported_batch",
    "idx": "4457",
    "reason": "空战斗字符串为占位；须按表槽和EOS识别，不能把相邻は片段当作文本内容。",
    "action": "no_text"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": ""
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_EmptyString4",
      "file": "patch/batches/193_battle_safari_item_effects.json",
      "payload_address": "0x0903E7DD",
      "payload_sha256": "dc02768fa8d4d5dc2885b82cc85d273447b8e2846ae9ab82c7c3ac52008435c7",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB8D0",
          "original": "0x085A963E",
          "target": "0x0903E7DD",
          "batch": "patch/batches/193_battle_safari_item_effects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5712 行 · ported_batch / 4460 · sText_PkmnMakesGroundMiss

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nじめんタイプの　わざが　あたらない！
```

英文：

```text
{B_DEF_NAME_WITH_PREFIX} makes GROUND\nmoves miss with {B_DEF_ABILITY}!
```

报告原中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，地面属性的招式\n无法击中{B_DEF_ABILITY}！
```

修复前实际中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，地面属性的招式
无法击中{B_DEF_ABILITY}！
```

最终中文：

```text
{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}
不会被地面属性的招式击中！
```

证据：

```json
{
  "review": {
    "row_number": 5712,
    "symbol": "sText_PkmnMakesGroundMiss",
    "domain": "ported_batch",
    "idx": "4460",
    "old": null,
    "new": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会被地面属性的招式击中！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会被地面属性的招式击中！",
    "old_current_text": "因为{B_DEF_NAME_WITH_PREFIX}，地面属性的招式\n无法击中{B_DEF_ABILITY}！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/193_battle_safari_item_effects.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nじめんタイプの　わざが　あたらない！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}因{B_DEF_ABILITY}\n不会被地面属性的招式击中！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nじめんタイプの　わざが　あたらない！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnMakesGroundMiss",
      "file": "patch/batches/193_battle_safari_item_effects.json",
      "payload_address": "0x0903E80D",
      "payload_sha256": "78280bef1cd99f5136777cec85b8a6a9ec1b92a4e6f446b2795f3d4ee1dc60f1",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB8DC",
          "original": "0x085A975F",
          "target": "0x0903E80D",
          "batch": "patch/batches/193_battle_safari_item_effects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5714 行 · ported_batch / 4462 · sText_PkmnsXTookAttack

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nこうげきを　うけた！
```

英文：

```text
{B_DEF_NAME_WITH_PREFIX}'s {B_DEF_ABILITY}\ntook the attack!
```

报告原中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n吸引了攻击！
```

修复前实际中文：

```text
因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}
吸引了攻击！
```

最终中文：

```text
{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}
吸引了攻击！
```

证据：

```json
{
  "review": {
    "row_number": 5714,
    "symbol": "sText_PkmnsXTookAttack",
    "domain": "ported_batch",
    "idx": "4462",
    "old": null,
    "new": "{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}\n吸引了攻击！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}\n吸引了攻击！",
    "old_current_text": "因为{B_DEF_NAME_WITH_PREFIX}，{B_DEF_ABILITY}\n吸引了攻击！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/193_battle_safari_item_effects.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nこうげきを　うけた！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}的{B_DEF_ABILITY}\n吸引了攻击！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_DEF_NAME_WITH_PREFIX}は　{B_DEF_ABILITY}で\nこうげきを　うけた！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnsXTookAttack",
      "file": "patch/batches/193_battle_safari_item_effects.json",
      "payload_address": "0x0903E865",
      "payload_sha256": "2a238d50bbd977df58add12efce130ef1f48d798e1ae64f834bd60f4b207e1c0",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB8E4",
          "original": "0x085AA7CC",
          "target": "0x0903E865",
          "batch": "patch/batches/193_battle_safari_item_effects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5727 行 · ported_batch / 4475 · sText_PkmnsXPreventsFlinching

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_EFF_NAME_WITH_PREFIX}は　{B_EFF_ABILITY}で\nひるまない！
```

英文：

```text
{B_EFF_NAME_WITH_PREFIX}'s {B_EFF_ABILITY}\nprevents flinching!
```

报告原中文：

```text
因为{B_EFF_NAME_WITH_PREFIX}，{B_EFF_ABILITY}\n不会畏缩！
```

修复前实际中文：

```text
因为{B_EFF_NAME_WITH_PREFIX}，{B_EFF_ABILITY}
不会畏缩！
```

最终中文：

```text
{B_EFF_NAME_WITH_PREFIX}因{B_EFF_ABILITY}
不会畏缩！
```

证据：

```json
{
  "review": {
    "row_number": 5727,
    "symbol": "sText_PkmnsXPreventsFlinching",
    "domain": "ported_batch",
    "idx": "4475",
    "old": null,
    "new": "{B_EFF_NAME_WITH_PREFIX}因{B_EFF_ABILITY}\n不会畏缩！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_EFF_NAME_WITH_PREFIX}因{B_EFF_ABILITY}\n不会畏缩！",
    "old_current_text": "因为{B_EFF_NAME_WITH_PREFIX}，{B_EFF_ABILITY}\n不会畏缩！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/194_battle_ability_link_facility.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_EFF_NAME_WITH_PREFIX}は　{B_EFF_ABILITY}で\nひるまない！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_EFF_NAME_WITH_PREFIX}因{B_EFF_ABILITY}\n不会畏缩！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_EFF_NAME_WITH_PREFIX}は　{B_EFF_ABILITY}で\nひるまない！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnsXPreventsFlinching",
      "file": "patch/batches/194_battle_ability_link_facility.json",
      "payload_address": "0x0903EA00",
      "payload_sha256": "0982e8597939ee21054b1370154b4859601b8cb9869a6dd9eda67056c2ecbc63",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB918",
          "original": "0x085AA826",
          "target": "0x0903EA00",
          "batch": "patch/batches/194_battle_ability_link_facility.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5730 行 · ported_batch / 4478 · sText_PkmnsXBlocksY2

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_CURRENT_MOVE}を　うけない！
```

英文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\nblocks {B_CURRENT_MOVE}!
```

报告原中文：

```text
因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}\n抵御了{B_CURRENT_MOVE}！
```

修复前实际中文：

```text
因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}
抵御了{B_CURRENT_MOVE}！
```

最终中文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}的{B_SCR_ACTIVE_ABILITY}
抵御了{B_CURRENT_MOVE}！
```

证据：

```json
{
  "review": {
    "row_number": 5730,
    "symbol": "sText_PkmnsXBlocksY2",
    "domain": "ported_batch",
    "idx": "4478",
    "old": null,
    "new": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}的{B_SCR_ACTIVE_ABILITY}\n抵御了{B_CURRENT_MOVE}！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}的{B_SCR_ACTIVE_ABILITY}\n抵御了{B_CURRENT_MOVE}！",
    "old_current_text": "因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}\n抵御了{B_CURRENT_MOVE}！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/194_battle_ability_link_facility.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_CURRENT_MOVE}を　うけない！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}的{B_SCR_ACTIVE_ABILITY}\n抵御了{B_CURRENT_MOVE}！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_CURRENT_MOVE}を　うけない！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnsXBlocksY2",
      "file": "patch/batches/194_battle_ability_link_facility.json",
      "payload_address": "0x0903EA56",
      "payload_sha256": "4b0dedff360c0bbc82de88e70ab8dc1e9a6c1c296d22a90a4cc05fcfb0f00938",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB924",
          "original": "0x085AA70F",
          "target": "0x0903EA56",
          "batch": "patch/batches/194_battle_ability_link_facility.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5736 行 · ported_batch / 4484 · sText_PkmnsXCuredItsYProblem

判定：`fixed_verified`

理由：核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。

日文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_BUFF1}が　なおった！
```

英文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}'s {B_SCR_ACTIVE_ABILITY}\ncured its {B_BUFF1} problem!
```

报告原中文：

```text
因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的\n{B_BUFF1}状态治愈了！
```

修复前实际中文：

```text
因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的
{B_BUFF1}状态治愈了！
```

最终中文：

```text
{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}
解除了{B_BUFF1}状态！
```

证据：

```json
{
  "review": {
    "row_number": 5736,
    "symbol": "sText_PkmnsXCuredItsYProblem",
    "domain": "ported_batch",
    "idx": "4484",
    "old": null,
    "new": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n解除了{B_BUFF1}状态！",
    "reason": "核对Wokann battle_message.c对应原文及同名US模板；宝可梦为主体，特性/道具是原因；保留日版变量编码和原有标点。",
    "scope": "both",
    "action": "fix",
    "final_text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n解除了{B_BUFF1}状态！",
    "old_current_text": "因为{B_SCR_ACTIVE_NAME_WITH_PREFIX}，{B_SCR_ACTIVE_ABILITY}的\n{B_BUFF1}状态治愈了！",
    "changed_files": [
      "../pokeemerald_us_chs/src/battle_message.c",
      "patch/batches/194_battle_ability_link_facility.json"
    ],
    "us_source_file": "src/battle_message.c",
    "jp_source": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_BUFF1}が　なおった！"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}因{B_SCR_ACTIVE_ABILITY}\n解除了{B_BUFF1}状态！"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/battle_message.c",
        "text": "{B_SCR_ACTIVE_NAME_WITH_PREFIX}は　{B_SCR_ACTIVE_ABILITY}で\n{B_BUFF1}が　なおった！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_PkmnsXCuredItsYProblem",
      "file": "patch/batches/194_battle_ability_link_facility.json",
      "payload_address": "0x0903EB1D",
      "payload_sha256": "c1ab43f09dffcddffe68bea66c166c2135bf02768ab0766de07c0a9276143c3a",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085AB93C",
          "original": "0x085AA84B",
          "target": "0x0903EB1D",
          "batch": "patch/batches/194_battle_ability_link_facility.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5762 行 · ported_batch / 4510 · gText_PkmnsNickname

判定：`fixed_verified`

理由：恢复中文全角问号；不改命名键盘。

日文：

```text
{STR_VAR_1}　の　ニックネームは？$
```

英文：

```text
{STR_VAR_1}'s nickname?
```

报告原中文：

```text
{STR_VAR_1}的昵称?$
```

修复前实际中文：

```text
的昵称?
```

最终中文：

```text
{STR_VAR_1}的昵称？
```

证据：

```json
{
  "review": {
    "row_number": 5762,
    "symbol": "gText_PkmnsNickname",
    "domain": "ported_batch",
    "idx": "4510",
    "old": "的昵称?",
    "new": "的昵称？",
    "reason": "恢复中文全角问号；不改命名键盘。",
    "scope": "jp_only",
    "action": "fix",
    "final_text": "{STR_VAR_1}的昵称？",
    "old_current_text": "的昵称?",
    "changed_files": [
      "patch/batches/195_naming_screen.json"
    ],
    "us_source_file": "src/strings.c",
    "jp_source": []
  },
  "source": {
    "us_sources": [
      {
        "file": "src/strings.c",
        "text": "{STR_VAR_1}的昵称？"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_PkmnsNickname",
      "file": "patch/batches/195_naming_screen.json",
      "payload_address": "0x0903EE48",
      "payload_sha256": "325d8fdc127728fac0db12a1f0314958e803e5ef65fa83a787c35d688396f6ec",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08565CD8",
          "original": "0x08565881",
          "target": "0x0903EE48",
          "batch": "patch/batches/195_naming_screen.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5772 行 · ported_batch / 4520 · EverGrandeCity_PokemonCenter_1F_Text_LeagueAfterVictoryRoad

判定：`fixed_verified`

理由：原文只能继续前进，不是询问动机。

日文：

```text
ポケモンリーグは\nチャンピオンロードを　ぬけると　すぐ！\pここまで　きたら\nまえに　すすむしかないわ！$
```

英文：

```text
The POKéMON LEAGUE is only a short\ndistance after the VICTORY ROAD.\pIf you've come this far, what choice\ndo you have but to keep going?$
```

报告原中文：

```text
穿过冠军之路，\n宝可梦联盟就在眼前。\p已经走了这么远，\n到底是什么让你坚持到现在？$
```

修复前实际中文：

```text
穿过冠军之路，
宝可梦联盟就在眼前。\p已经走了这么远，
到底是什么让你坚持到现在？
```

最终中文：

```text
穿过冠军之路，
宝可梦联盟就在眼前。\p已经走了这么远，
只能继续前进了！
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/EverGrandeCity_PokemonCenter_1F/scripts.inc",
        "text": "穿过冠军之路，\n宝可梦联盟就在眼前。\\p已经走了这么远，\n只能继续前进了！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/EverGrandeCity_PokemonCenter_1F/scripts.inc",
        "text": "ポケモンリーグは\nチャンピオンロードを　ぬけると　すぐ！\\pここまで　きたら\nまえに　すすむしかないわ！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_EverGrandeCity_PokemonCenter_1F_Text_LeagueAfterVictoryRoad",
      "file": "patch/batches/196_pokemon_centers.json",
      "payload_address": "0x0903F04B",
      "payload_sha256": "7a9fb9e3907db969f9a652b8d8eb1c07c8b196e8f5d33103ba27426eda9f9362",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08211431",
          "original": "0x082114A2",
          "target": "0x0903F04B",
          "batch": "patch/batches/196_pokemon_centers.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5795 行 · ported_batch / 4543 · SootopolisCity_PokemonCenter_1F_Text_AlwaysBeFriendsWithPokemon

判定：`fixed_verified`

理由：原文明确说做朋友。

日文：

```text
どんな　ときでも\nどんな　ことが　あっても\lあたし　ポケモンと　ともだちで　いるわ\pだって　ポケモンと　いっしょだと\nすごく　たのしいもの！$
```

英文：

```text
Whenever, wherever, and whatever\nhappens, I will always be friends with\lPOKéMON.\pBecause it's fun to be with POKéMON!$
```

报告原中文：

```text
无论何时，无论何地，\n无论发生什么，\l我都会和宝可梦在一起。\p和宝可梦交朋友是我的乐趣！$
```

修复前实际中文：

```text
无论何时，无论何地，
无论发生什么，\l我都会和宝可梦在一起。\p和宝可梦交朋友是我的乐趣！
```

最终中文：

```text
无论何时，无论何地，
无论发生什么，\l我都会和宝可梦做朋友。\p和宝可梦交朋友是我的乐趣！
```

证据：

```json
{
  "review": {
    "row_number": 5795,
    "symbol": "SootopolisCity_PokemonCenter_1F_Text_AlwaysBeFriendsWithPokemon",
    "domain": "ported_batch",
    "idx": "4543",
    "old": "我都会和宝可梦在一起。",
    "new": "我都会和宝可梦做朋友。",
    "reason": "原文明确说做朋友。",
    "scope": "both",
    "action": "fix",
    "final_text": "无论何时，无论何地，\n无论发生什么，\\l我都会和宝可梦做朋友。\\p和宝可梦交朋友是我的乐趣！",
    "old_current_text": "无论何时，无论何地，\n无论发生什么，\\l我都会和宝可梦在一起。\\p和宝可梦交朋友是我的乐趣！",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/SootopolisCity_PokemonCenter_1F/scripts.inc",
      "patch/batches/196_pokemon_centers.json"
    ],
    "us_source_file": "data/maps/SootopolisCity_PokemonCenter_1F/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/SootopolisCity_PokemonCenter_1F/scripts.inc",
        "text": "どんな　ときでも\nどんな　ことが　あっても\\lあたし　ポケモンと　ともだちで　いるわ\\pだって　ポケモンと　いっしょだと\nすごく　たのしいもの！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/SootopolisCity_PokemonCenter_1F/scripts.inc",
        "text": "无论何时，无论何地，\n无论发生什么，\\l我都会和宝可梦做朋友。\\p和宝可梦交朋友是我的乐趣！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/SootopolisCity_PokemonCenter_1F/scripts.inc",
        "text": "どんな　ときでも\nどんな　ことが　あっても\\lあたし　ポケモンと　ともだちで　いるわ\\pだって　ポケモンと　いっしょだと\nすごく　たのしいもの！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_SootopolisCity_PokemonCenter_1F_Text_AlwaysBeFriendsWithPokemon",
      "file": "patch/batches/196_pokemon_centers.json",
      "payload_address": "0x0903F879",
      "payload_sha256": "3cb5420536b707e350c6991c1f308a7747a3113085c403f32b48cb36dfaeeacc",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0820F03E",
          "original": "0x0820F117",
          "target": "0x0903F879",
          "batch": "patch/batches/196_pokemon_centers.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5803 行 · ported_batch / 4551 · gText_NoticesGoldCard

判定：`fixed_verified`

理由：恢复金卡、金色、四颗星的明确内容。

日文：

```text
そ　それは⋯⋯\nひょっとして　ゴールドカード！？\pああ⋯⋯　きんいろが　まぶしい！\n4つの　ほしが　かがやかしい！\pわたしも　これまでに\nシルバーカードの　トレーナーさんなら\lなんにんか　みてきましたが\lゴールドカードを　おもちの　かたは\l{PLAYER}さんが　はじめて　ですよ！\pさあ　{PLAYER}さんの\nポケモンを　やすませて　あげましょう！$
```

英文：

```text
Th-that card…\nCould it be… The GOLD CARD?!\pOh, the gold color is brilliant!\nThe four stars seem to sparkle!\pI've seen several TRAINERS with\na SILVER CARD before, but, {PLAYER},\lyou're the first TRAINER I've ever\lseen with a GOLD CARD!\pOkay, {PLAYER}, please allow me\nthe honor of resting your POKéMON!$
```

报告原中文：

```text
那、那张卡！？\p那个颜色！！\n那星星的数量！！\p至今为止我也见过几位\n拥有白银卡的训练家。\p但是拥有比这更厉害的\n训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！$
```

修复前实际中文：

```text
那、那张卡！？\p那个颜色！！
那星星的数量！！\p至今为止我也见过几位
拥有白银卡的训练家。\p但是拥有比这更厉害的
训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！
```

最终中文：

```text
那、那张卡！？\p难道是金卡！？\p金色真耀眼！！
四颗星在闪耀！！\p至今为止我也见过几位
拥有白银卡的训练家。\p但是拥有比这更厉害的
训练家卡的客人，\l您还是第一位！\p先让您的宝可梦休息一下吧！
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/pkmn_center_nurse.inc",
        "text": "那、那张卡！？\\p难道是金卡！？\\p金色真耀眼！！\n四颗星在闪耀！！\\p至今为止我也见过几位\n拥有白银卡的训练家。\\p但是拥有比这更厉害的\n训练家卡的客人，\\l您还是第一位！\\p先让您的宝可梦休息一下吧！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/pkmn_center_nurse.inc",
        "text": "そ　それは⋯⋯\nひょっとして　ゴールドカード！？\\pああ⋯⋯　きんいろが　まぶしい！\n4つの　ほしが　かがやかしい！\\pわたしも　これまでに\nシルバーカードの　トレーナーさんなら\\lなんにんか　みてきましたが\\lゴールドカードを　おもちの　かたは\\l{PLAYER}さんが　はじめて　ですよ！\\pさあ　{PLAYER}さんの\nポケモンを　やすませて　あげましょう！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_NoticesGoldCard",
      "file": "patch/batches/196_pokemon_centers.json",
      "payload_address": "0x0903FA9C",
      "payload_sha256": "9e74eda9f19c3273e57e28c3b1ac0db8e2a55e184e90609fa78ba06e564a9268",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08242B2F",
          "original": "0x08243814",
          "target": "0x0903FA9C",
          "batch": "patch/batches/196_pokemon_centers.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5810 行 · ported_batch / 4558 · gText_YouWantTheUsual

判定：`fixed_verified`

理由：原文称呼玩家；新占位符必须保留JP姓名语言包装。

日文：

```text
{PLAYER}さん　おつかれさまです！\nいつもので　よろしい　ですね！$
```

英文：

```text
I'm delighted to see you, {PLAYER}!\nYou want the usual, am I right?$
```

报告原中文：

```text
辛苦了！\n要像往常一样吗？$
```

修复前实际中文：

```text
辛苦了！
要像往常一样吗？
```

最终中文：

```text
{PLAYER}，辛苦了！
要像往常一样吗？
```

证据：

```json
{
  "review": {
    "row_number": 5810,
    "symbol": "gText_YouWantTheUsual",
    "domain": "ported_batch",
    "idx": "4558",
    "old": "辛苦了！",
    "new": "{PLAYER}，辛苦了！",
    "reason": "原文称呼玩家；新占位符必须保留JP姓名语言包装。",
    "scope": "both",
    "action": "fix",
    "final_text": "{PLAYER}，辛苦了！\n要像往常一样吗？",
    "old_current_text": "辛苦了！\n要像往常一样吗？",
    "changed_files": [
      "../pokeemerald_us_chs/data/text/pkmn_center_nurse.inc",
      "patch/batches/196_pokemon_centers.json"
    ],
    "us_source_file": "data/text/pkmn_center_nurse.inc",
    "jp_source": [
      {
        "file": "data/text/pkmn_center_nurse.inc",
        "text": "{PLAYER}さん　おつかれさまです！\nいつもので　よろしい　ですね！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/pkmn_center_nurse.inc",
        "text": "{PLAYER}，辛苦了！\n要像往常一样吗？$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/pkmn_center_nurse.inc",
        "text": "{PLAYER}さん　おつかれさまです！\nいつもので　よろしい　ですね！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_YouWantTheUsual",
      "file": "patch/batches/196_pokemon_centers.json",
      "payload_address": "0x0903FC62",
      "payload_sha256": "60a1b0c38998af3c3313f3e15a824f93e51b1292b5dc1a2408761c59ac4a793e",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08242B48",
          "original": "0x082438B9",
          "target": "0x0903FC62",
          "batch": "patch/batches/196_pokemon_centers.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5872 行 · ported_batch / 4620 · gText_TuckerDefeatSilver

判定：`fixed_verified`

理由：回为会的笔误；保留省略语气。

日文：

```text
クッ⋯⋯　なんて　こと⋯⋯$
```

英文：

```text
Grr…\nWhat the…$
```

报告原中文：

```text
呃……\n怎么回……$
```

修复前实际中文：

```text
呃……
怎么回……
```

最终中文：

```text
呃……
怎么会……
```

证据：

```json
{
  "review": {
    "row_number": 5872,
    "symbol": "gText_TuckerDefeatSilver",
    "domain": "ported_batch",
    "idx": "4620",
    "old": "怎么回……",
    "new": "怎么会……",
    "reason": "回为会的笔误；保留省略语气。",
    "scope": "both",
    "action": "fix",
    "final_text": "呃……\n怎么会……",
    "old_current_text": "呃……\n怎么回……",
    "changed_files": [
      "../pokeemerald_us_chs/data/text/frontier_brain.inc",
      "patch/batches/198_frontier_brain_quotes.json"
    ],
    "us_source_file": "data/text/frontier_brain.inc",
    "jp_source": [
      {
        "file": "data/text/frontier_brain.inc",
        "text": "クッ⋯⋯　なんて　こと⋯⋯$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/frontier_brain.inc",
        "text": "呃……\n怎么会……$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/frontier_brain.inc",
        "text": "クッ⋯⋯　なんて　こと⋯⋯$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_TuckerDefeatSilver",
      "file": "patch/batches/198_frontier_brain_quotes.json",
      "payload_address": "0x0904064B",
      "payload_sha256": "c4fd26b08f9fdeabc0746b7c8c7e237a04bd28d1bd5762e72f11755f9a62918f",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085DD598",
          "original": "0x08276D8A",
          "target": "0x0904064B",
          "batch": "patch/batches/198_frontier_brain_quotes.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5913 行 · ported_batch / 4661 · BattleFrontier_BattleArenaBattleRoom_Text_IsThatRight

判定：`fixed_verified`

理由：恢复沉吟语气，不表示质疑出错。

日文：

```text
ふーん⋯⋯　へーえ⋯⋯　へえぇぇ⋯⋯$
```

英文：

```text
Is that right? Hmm…\nHmhm…$
```

报告原中文：

```text
没有搞错吗？哈……\n哈哈……$
```

修复前实际中文：

```text
没有搞错吗？哈……
哈哈……
```

最终中文：

```text
是吗？哈……
哈哈……
```

证据：

```json
{
  "review": {
    "row_number": 5913,
    "symbol": "BattleFrontier_BattleArenaBattleRoom_Text_IsThatRight",
    "domain": "ported_batch",
    "idx": "4661",
    "old": "没有搞错吗？",
    "new": "是吗？",
    "reason": "恢复沉吟语气，不表示质疑出错。",
    "scope": "both",
    "action": "fix",
    "final_text": "是吗？哈……\n哈哈……",
    "old_current_text": "没有搞错吗？哈……\n哈哈……",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleArenaBattleRoom/scripts.inc",
      "patch/batches/199_battle_frontier_arena.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleArenaBattleRoom/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleArenaBattleRoom/scripts.inc",
        "text": "ふーん⋯⋯　へーえ⋯⋯　へえぇぇ⋯⋯$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleArenaBattleRoom/scripts.inc",
        "text": "是吗？哈……\n哈哈……$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleArenaBattleRoom/scripts.inc",
        "text": "ふーん⋯⋯　へーえ⋯⋯　へえぇぇ⋯⋯$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleArenaBattleRoom_Text_IsThatRight",
      "file": "patch/batches/199_battle_frontier_arena.json",
      "payload_address": "0x09040B8E",
      "payload_sha256": "ffd00415c643545db2165bd0bf8b12980a040ef78a66fe9d81fcff34433cb1fc",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082306D6",
          "original": "0x08230B88",
          "target": "0x09040B8E",
          "batch": "patch/batches/199_battle_frontier_arena.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5966 行 · ported_batch / 4714 · BattleFrontier_BattleDomeBattleRoom_Text_WillTheyRaceToChampionship

判定：`fixed_verified`

理由：原文问能否夺冠，不是问哪位进入决赛。

日文：

```text
いっきに　ゆうしょうまで\nのぼりつめて　しまうのでしょうか！？\p$
```

英文：

```text
Will this TRAINER race to\nthe championship?\p$
```

报告原中文：

```text
哪一位训练家进入\n冠军赛了呢？\p$
```

修复前实际中文：

```text
哪一位训练家进入
冠军赛了呢？\p
```

最终中文：

```text
这位训练家能否
一举夺冠呢？\p
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc",
        "text": "这位训练家能否\n一举夺冠呢？\\p$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc",
        "text": "いっきに　ゆうしょうまで\nのぼりつめて　しまうのでしょうか！？\\p$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleDomeBattleRoom_Text_WillTheyRaceToChampionship",
      "file": "patch/batches/200_battle_frontier_battle_dome_battle_room.json",
      "payload_address": "0x09041B50",
      "payload_sha256": "d3a922f9eb6220103bdec9fa84afc6aa0307e54ce26b4dc66fffe9b0d8dc4a88",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08228BF5",
          "original": "0x082296B5",
          "target": "0x09041B50",
          "batch": "patch/batches/200_battle_frontier_battle_dome_battle_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 5990 行 · ported_batch / 4738 · BattleFrontier_BattleDomeBattleRoom_Text_CanWinStreakBeStretched

判定：`fixed_verified`

理由：原文后句描述信心，不是等待结果。

日文：

```text
どこまで　かちつづける　つもり　なのか？\nかんろく　じゅうぶん！$
```

英文：

```text
Can the win streak be stretched?\nThe confidence is there!$
```

报告原中文：

```text
我们的冠军还会继续称霸吗？\n让我们期待比赛的结果吧！$
```

修复前实际中文：

```text
我们的冠军还会继续称霸吗？
让我们期待比赛的结果吧！
```

最终中文：

```text
我们的冠军还会继续称霸吗？
真是信心十足！
```

证据：

```json
{
  "review": {
    "row_number": 5990,
    "symbol": "BattleFrontier_BattleDomeBattleRoom_Text_CanWinStreakBeStretched",
    "domain": "ported_batch",
    "idx": "4738",
    "old": "让我们期待比赛的结果吧！",
    "new": "真是信心十足！",
    "reason": "原文后句描述信心，不是等待结果。",
    "scope": "both",
    "action": "fix",
    "final_text": "我们的冠军还会继续称霸吗？\n真是信心十足！",
    "old_current_text": "我们的冠军还会继续称霸吗？\n让我们期待比赛的结果吧！",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc",
      "patch/batches/200_battle_frontier_battle_dome_battle_room.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc",
        "text": "どこまで　かちつづける　つもり　なのか？\nかんろく　じゅうぶん！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc",
        "text": "我们的冠军还会继续称霸吗？\n真是信心十足！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleDomeBattleRoom/scripts.inc",
        "text": "どこまで　かちつづける　つもり　なのか？\nかんろく　じゅうぶん！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleDomeBattleRoom_Text_CanWinStreakBeStretched",
      "file": "patch/batches/200_battle_frontier_battle_dome_battle_room.json",
      "payload_address": "0x09041FAB",
      "payload_sha256": "aa960e221a3e88dc75def4a51946da6cc3bb7a981bb4913ff28e86e0faee2512",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08228CEF",
          "original": "0x08229A4A",
          "target": "0x09041FAB",
          "batch": "patch/batches/200_battle_frontier_battle_dome_battle_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6024 行 · ported_batch / 4772 · BattleFrontier_BattleDomeLobby_Text_TrashedInFirstRound

判定：`fixed_verified`

理由：原文被痛打，不只是预期会输。

日文：

```text
1かいせんで　いきなり\nゆうしょうこうほと　あたっちゃって\lもう　ボコボコに　やられたよ⋯⋯$
```

英文：

```text
I ran into one of the tournament\nfavorites in the very first round.\pOf course I got trashed…$
```

报告原中文：

```text
比赛的第一场我就碰上了\n一个夺冠热门的选手。\p输掉也是预料之中……$
```

修复前实际中文：

```text
比赛的第一场我就碰上了
一个夺冠热门的选手。\p输掉也是预料之中……
```

最终中文：

```text
比赛的第一场我就碰上了
一个夺冠热门的选手。\p被打得落花流水……
```

证据：

```json
{
  "review": {
    "row_number": 6024,
    "symbol": "BattleFrontier_BattleDomeLobby_Text_TrashedInFirstRound",
    "domain": "ported_batch",
    "idx": "4772",
    "old": "输掉也是预料之中……",
    "new": "被打得落花流水……",
    "reason": "原文被痛打，不只是预期会输。",
    "scope": "both",
    "action": "fix",
    "final_text": "比赛的第一场我就碰上了\n一个夺冠热门的选手。\\p被打得落花流水……",
    "old_current_text": "比赛的第一场我就碰上了\n一个夺冠热门的选手。\\p输掉也是预料之中……",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleDomeLobby/scripts.inc",
      "patch/batches/201_battle_frontier_battle_dome_lobby.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleDomeLobby/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleDomeLobby/scripts.inc",
        "text": "1かいせんで　いきなり\nゆうしょうこうほと　あたっちゃって\\lもう　ボコボコに　やられたよ⋯⋯$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleDomeLobby/scripts.inc",
        "text": "比赛的第一场我就碰上了\n一个夺冠热门的选手。\\p被打得落花流水……$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleDomeLobby/scripts.inc",
        "text": "1かいせんで　いきなり\nゆうしょうこうほと　あたっちゃって\\lもう　ボコボコに　やられたよ⋯⋯$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleDomeLobby_Text_TrashedInFirstRound",
      "file": "patch/batches/201_battle_frontier_battle_dome_lobby.json",
      "payload_address": "0x09042A92",
      "payload_sha256": "52374794f887af22e76367c0c65beb63279708e21793027701b78520c8edabec",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082273B3",
          "original": "0x08227C4A",
          "target": "0x09042A92",
          "batch": "patch/batches/201_battle_frontier_battle_dome_lobby.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6092 行 · ported_batch / 4840 · BattleFrontier_BattleFactoryLobby_Text_CantFigureOutStaffHints

判定：`fixed_verified`

理由：full-grown man / いいおとな 指成年人。

日文：

```text
ここの　スタッフさぁ　たたかいの　まえに\nつぎに　たたかう　トレーナーのこと\lちょっとだけ　おしえて　くれるだろー？\pでも　オレ　いい　おとな　なのに\nあいつらの　せつめいの　いみが\lぜんぜん　わからないんだ　よう$
```

英文：

```text
You know how the staff here give you\na few hints about your next opponent?\pWell, I'm a full-grown man, but I have\ntrouble figuring out their hints.$
```

报告原中文：

```text
你知道这的工作人员会给你\n一些关于你下个对手的提示吧？\p好吧，虽然我是一个经验丰富的人，\n但我弄不懂他们的提示。$
```

修复前实际中文：

```text
你知道这的工作人员会给你
一些关于你下个对手的提示吧？\p好吧，虽然我是一个经验丰富的人，
但我弄不懂他们的提示。
```

最终中文：

```text
你知道这的工作人员会给你
一些关于你下个对手的提示吧？\p好吧，虽然我是一个成年人，
但我弄不懂他们的提示。
```

证据：

```json
{
  "review": {
    "row_number": 6092,
    "symbol": "BattleFrontier_BattleFactoryLobby_Text_CantFigureOutStaffHints",
    "domain": "ported_batch",
    "idx": "4840",
    "old": "一个经验丰富的人",
    "new": "一个成年人",
    "reason": "full-grown man / いいおとな 指成年人。",
    "scope": "both",
    "action": "fix",
    "final_text": "你知道这的工作人员会给你\n一些关于你下个对手的提示吧？\\p好吧，虽然我是一个成年人，\n但我弄不懂他们的提示。",
    "old_current_text": "你知道这的工作人员会给你\n一些关于你下个对手的提示吧？\\p好吧，虽然我是一个经验丰富的人，\n但我弄不懂他们的提示。",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleFactoryLobby/scripts.inc",
      "patch/batches/204_battle_frontier_battle_factory_lobby.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleFactoryLobby/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleFactoryLobby/scripts.inc",
        "text": "ここの　スタッフさぁ　たたかいの　まえに\nつぎに　たたかう　トレーナーのこと\\lちょっとだけ　おしえて　くれるだろー？\\pでも　オレ　いい　おとな　なのに\nあいつらの　せつめいの　いみが\\lぜんぜん　わからないんだ　よう$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleFactoryLobby/scripts.inc",
        "text": "你知道这的工作人员会给你\n一些关于你下个对手的提示吧？\\p好吧，虽然我是一个成年人，\n但我弄不懂他们的提示。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleFactoryLobby/scripts.inc",
        "text": "ここの　スタッフさぁ　たたかいの　まえに\nつぎに　たたかう　トレーナーのこと\\lちょっとだけ　おしえて　くれるだろー？\\pでも　オレ　いい　おとな　なのに\nあいつらの　せつめいの　いみが\\lぜんぜん　わからないんだ　よう$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleFactoryLobby_Text_CantFigureOutStaffHints",
      "file": "patch/batches/204_battle_frontier_battle_factory_lobby.json",
      "payload_address": "0x09043D9F",
      "payload_sha256": "e110d6eec62854658ed6bda8d5f7e6dd06ab3e5a263864a5e4d4e07dab281737",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08231205",
          "original": "0x0823198B",
          "target": "0x09043D9F",
          "batch": "patch/batches/204_battle_frontier_battle_factory_lobby.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6256 行 · ported_batch / 5004 · BattleFrontier_BattlePikeRoomNormal_Text_AttacksWhenStartled

判定：`fixed_verified`

理由：JP命令を無視して指无视指挥，而非无视警告。

日文：

```text
きゅうに　ひとを　みると　おどろいて\nおそいかかって　しまうのだ⋯⋯\pきみも　ポケモンも　だいじょうぶか？$
```

英文：

```text
It attacks without warning if it is\nstartled by another person…\pAre you and your POKéMON all right?$
```

报告原中文：

```text
一旦受到了惊吓就会\n无视警告胡乱攻击……\p您和您的宝可梦还好吗？$
```

修复前实际中文：

```text
一旦受到了惊吓就会
无视警告胡乱攻击……\p您和您的宝可梦还好吗？
```

最终中文：

```text
一旦受到了惊吓就会
不听指挥胡乱攻击……\p您和您的宝可梦还好吗？
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePikeRoomNormal/scripts.inc",
        "text": "一旦受到了惊吓就会\n不听指挥胡乱攻击……\\p您和您的宝可梦还好吗？$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePikeRoomNormal/scripts.inc",
        "text": "きゅうに　ひとを　みると　おどろいて\nおそいかかって　しまうのだ⋯⋯\\pきみも　ポケモンも　だいじょうぶか？$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattlePikeRoomNormal_Text_AttacksWhenStartled",
      "file": "patch/batches/212_battle_frontier_battle_pike_room_normal.json",
      "payload_address": "0x090466D4",
      "payload_sha256": "5504e27b9c70c6c34765b05dfde9bc9c3e951f634e8e6a482a92fd252ece6fb3",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0823488F",
          "original": "0x08234E0C",
          "target": "0x090466D4",
          "batch": "patch/batches/212_battle_frontier_battle_pike_room_normal.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6295 行 · ported_batch / 5043 · BattleFrontier_BattlePikeThreePathRoom_Text_AromaOfPokemon

判定：`fixed_verified`

理由：原文是气味飘来。

日文：

```text
ポケモンの　においが\nただよってくる　ような\lきが　するの　ですが⋯⋯$
```

英文：

```text
It seems to have the distinct aroma\nof POKéMON wafting around it…$
```

报告原中文：

```text
似乎有宝可梦在里面的感觉……$
```

修复前实际中文：

```text
似乎有宝可梦在里面的感觉……
```

最终中文：

```text
似乎有宝可梦的气味飘来……
```

证据：

```json
{
  "review": {
    "row_number": 6295,
    "symbol": "BattleFrontier_BattlePikeThreePathRoom_Text_AromaOfPokemon",
    "domain": "ported_batch",
    "idx": "5043",
    "old": "似乎有宝可梦在里面的感觉……",
    "new": "似乎有宝可梦的气味飘来……",
    "reason": "原文是气味飘来。",
    "scope": "both",
    "action": "fix",
    "final_text": "似乎有宝可梦的气味飘来……",
    "old_current_text": "似乎有宝可梦在里面的感觉……",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattlePikeThreePathRoom/scripts.inc",
      "patch/batches/213_battle_frontier_battle_pike_three_path_room.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattlePikeThreePathRoom/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattlePikeThreePathRoom/scripts.inc",
        "text": "ポケモンの　においが\nただよってくる　ような\\lきが　するの　ですが⋯⋯$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePikeThreePathRoom/scripts.inc",
        "text": "似乎有宝可梦的气味飘来……$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePikeThreePathRoom/scripts.inc",
        "text": "ポケモンの　においが\nただよってくる　ような\\lきが　するの　ですが⋯⋯$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattlePikeThreePathRoom_Text_AromaOfPokemon",
      "file": "patch/batches/213_battle_frontier_battle_pike_three_path_room.json",
      "payload_address": "0x09046D72",
      "payload_sha256": "bf1c37f99b9fc270cdeb8e8898a02a9bbc2f3a30a6825f1b1f473093586bf972",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08234026",
          "original": "0x082342AE",
          "target": "0x09046D72",
          "batch": "patch/batches/213_battle_frontier_battle_pike_three_path_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6327 行 · ported_batch / 5075 · BattleFrontier_BattlePyramidLobby_Text_HintBurn

判定：`fixed_verified`

理由：bright red / まっかな 指颜色，不是闪亮。

日文：

```text
まっかな　ほのおが　みえます⋯⋯\p⋯⋯そして\nやけどを　おって　くるしむ\lあなたの　ポケモンの　すがたも⋯⋯$
```

英文：

```text
I see bright red flames…\p…And, I see your POKéMON suffering\nfrom burns…$
```

报告原中文：

```text
我看到了闪亮的火焰……\p……你的宝可梦\n正在被烧灼着……$
```

修复前实际中文：

```text
我看到了闪亮的火焰……\p……你的宝可梦
正在被烧灼着……
```

最终中文：

```text
我看到了赤红的火焰……\p……你的宝可梦
正在被烧灼着……
```

证据：

```json
{
  "review": {
    "row_number": 6327,
    "symbol": "BattleFrontier_BattlePyramidLobby_Text_HintBurn",
    "domain": "ported_batch",
    "idx": "5075",
    "old": "闪亮的火焰",
    "new": "赤红的火焰",
    "reason": "bright red / まっかな 指颜色，不是闪亮。",
    "scope": "both",
    "action": "fix",
    "final_text": "我看到了赤红的火焰……\\p……你的宝可梦\n正在被烧灼着……",
    "old_current_text": "我看到了闪亮的火焰……\\p……你的宝可梦\n正在被烧灼着……",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattlePyramidLobby/scripts.inc",
      "patch/batches/214_battle_frontier_battle_pyramid_lobby.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattlePyramidLobby/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidLobby/scripts.inc",
        "text": "まっかな　ほのおが　みえます⋯⋯\\p⋯⋯そして\nやけどを　おって　くるしむ\\lあなたの　ポケモンの　すがたも⋯⋯$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidLobby/scripts.inc",
        "text": "我看到了赤红的火焰……\\p……你的宝可梦\n正在被烧灼着……$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidLobby/scripts.inc",
        "text": "まっかな　ほのおが　みえます⋯⋯\\p⋯⋯そして\nやけどを　おって　くるしむ\\lあなたの　ポケモンの　すがたも⋯⋯$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattlePyramidLobby_Text_HintBurn",
      "file": "patch/batches/214_battle_frontier_battle_pyramid_lobby.json",
      "payload_address": "0x0904756F",
      "payload_sha256": "930c475d9b3f32871e73b93085f3eecbdaa79c639f380f98bcf1d914fd430dbc",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0822C269",
          "original": "0x0822CD0D",
          "target": "0x0904756F",
          "batch": "patch/batches/214_battle_frontier_battle_pyramid_lobby.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6407 行 · ported_batch / 5155 · BattleFrontier_BattleTowerLobby_Text_AboutToFace50thTrainer

判定：`fixed_verified`

理由：リボン / ribbon 对应缎带，统一奖励术语。

日文：

```text
いよいよ　つぎは　50にんめの\nトレーナー　ですね！\pこれからは　7にんを　かちぬく　たびに\nあなたの　ポケモンに　きねんリボンが\lおくられますので　がんばって　くださいね！$
```

英文：

```text
You're finally about to face the\n50th TRAINER.\pFrom here on, every time you beat seven\nTRAINERS in a row, your POKéMON will\lreceive a commemorative RIBBON.\pGood luck!$
```

报告原中文：

```text
下面您即将迎战的是\n第50位训练家了，\p现在起，您每次连续打败7位训练家，\n我们将会把奖章送给您参战的宝可梦。\p祝您好运！$
```

修复前实际中文：

```text
下面您即将迎战的是
第50位训练家了，\p现在起，您每次连续打败7位训练家，
我们将会把奖章送给您参战的宝可梦。\p祝您好运！
```

最终中文：

```text
下面您即将迎战的是
第50位训练家了，\p现在起，您每次连续打败7位训练家，
我们将会把缎带送给您参战的宝可梦。\p祝您好运！
```

证据：

```json
{
  "review": {
    "row_number": 6407,
    "symbol": "BattleFrontier_BattleTowerLobby_Text_AboutToFace50thTrainer",
    "domain": "ported_batch",
    "idx": "5155",
    "old": "奖章",
    "new": "缎带",
    "reason": "リボン / ribbon 对应缎带，统一奖励术语。",
    "scope": "both",
    "action": "fix",
    "final_text": "下面您即将迎战的是\n第50位训练家了，\\p现在起，您每次连续打败7位训练家，\n我们将会把缎带送给您参战的宝可梦。\\p祝您好运！",
    "old_current_text": "下面您即将迎战的是\n第50位训练家了，\\p现在起，您每次连续打败7位训练家，\n我们将会把奖章送给您参战的宝可梦。\\p祝您好运！",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
      "patch/batches/217_battle_frontier_battle_tower_lobby.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
        "text": "いよいよ　つぎは　50にんめの\nトレーナー　ですね！\\pこれからは　7にんを　かちぬく　たびに\nあなたの　ポケモンに　きねんリボンが\\lおくられますので　がんばって　くださいね！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
        "text": "下面您即将迎战的是\n第50位训练家了，\\p现在起，您每次连续打败7位训练家，\n我们将会把缎带送给您参战的宝可梦。\\p祝您好运！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
        "text": "いよいよ　つぎは　50にんめの\nトレーナー　ですね！\\pこれからは　7にんを　かちぬく　たびに\nあなたの　ポケモンに　きねんリボンが\\lおくられますので　がんばって　くださいね！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleTowerLobby_Text_AboutToFace50thTrainer",
      "file": "patch/batches/217_battle_frontier_battle_tower_lobby.json",
      "payload_address": "0x09048BE9",
      "payload_sha256": "9741f9e24549a3f5554b1b5de68072f0f781c96eaf4085439018663dca182984",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0821F81D",
          "original": "0x082206DE",
          "target": "0x09048BE9",
          "batch": "patch/batches/217_battle_frontier_battle_tower_lobby.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6408 行 · ported_batch / 5156 · BattleFrontier_BattleTowerLobby_Text_HereAreSomeRibbons

判定：`fixed_verified`

理由：リボン / ribbon 对应缎带，统一奖励术语。

日文：

```text
つよい　トレーナー　7にんを\nかちぬいた　きねんの　リボンを　どうぞ！\p{PLAYER}は　リボンを　もらった！$
```

英文：

```text
Here are some RIBBONS for beating\nseven tough TRAINERS in a row.\p{PLAYER} received some RIBBONS!$
```

报告原中文：

```text
这是连续打败7位\n强大的训练家的奖励。\p{PLAYER}得到奖章！$
```

修复前实际中文：

```text
这是连续打败7位
强大的训练家的奖励。\p{PLAYER}得到奖章！
```

最终中文：

```text
这是连续打败7位
强大的训练家的奖励。\p{PLAYER}得到缎带！
```

证据：

```json
{
  "review": {
    "row_number": 6408,
    "symbol": "BattleFrontier_BattleTowerLobby_Text_HereAreSomeRibbons",
    "domain": "ported_batch",
    "idx": "5156",
    "old": "奖章",
    "new": "缎带",
    "reason": "リボン / ribbon 对应缎带，统一奖励术语。",
    "scope": "both",
    "action": "fix",
    "final_text": "这是连续打败7位\n强大的训练家的奖励。\\p{PLAYER}得到缎带！",
    "old_current_text": "这是连续打败7位\n强大的训练家的奖励。\\p{PLAYER}得到奖章！",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
      "patch/batches/217_battle_frontier_battle_tower_lobby.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
        "text": "つよい　トレーナー　7にんを\nかちぬいた　きねんの　リボンを　どうぞ！\\p{PLAYER}は　リボンを　もらった！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
        "text": "这是连续打败7位\n强大的训练家的奖励。\\p{PLAYER}得到缎带！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
        "text": "つよい　トレーナー　7にんを\nかちぬいた　きねんの　リボンを　どうぞ！\\p{PLAYER}は　リボンを　もらった！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleTowerLobby_Text_HereAreSomeRibbons",
      "file": "patch/batches/217_battle_frontier_battle_tower_lobby.json",
      "payload_address": "0x09048C60",
      "payload_sha256": "22200611048db1f1e29ce80f81631343f200791bb8be0116de27aefbee6ce269",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0821F7D5",
          "original": "0x08220736",
          "target": "0x09048C60",
          "batch": "patch/batches/217_battle_frontier_battle_tower_lobby.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6409 行 · ported_batch / 5157 · BattleFrontier_BattleTowerLobby_Text_PutRibbonOnMons

判定：`fixed_verified`

理由：リボン / ribbon 对应缎带，统一奖励术语。

日文：

```text
{PLAYER}は　ポケモンに\nリボンを　つけて　あげた！$
```

英文：

```text
{PLAYER} put the RIBBONS on\nthe challenger POKéMON.$
```

报告原中文：

```text
{PLAYER}给挑战的宝可梦\n戴上了奖章。$
```

修复前实际中文：

```text
{PLAYER}给挑战的宝可梦
戴上了奖章。
```

最终中文：

```text
{PLAYER}给挑战的宝可梦
戴上了缎带。
```

证据：

```json
{
  "review": {
    "row_number": 6409,
    "symbol": "BattleFrontier_BattleTowerLobby_Text_PutRibbonOnMons",
    "domain": "ported_batch",
    "idx": "5157",
    "old": "奖章",
    "new": "缎带",
    "reason": "リボン / ribbon 对应缎带，统一奖励术语。",
    "scope": "both",
    "action": "fix",
    "final_text": "{PLAYER}给挑战的宝可梦\n戴上了缎带。",
    "old_current_text": "{PLAYER}给挑战的宝可梦\n戴上了奖章。",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
      "patch/batches/217_battle_frontier_battle_tower_lobby.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
        "text": "{PLAYER}は　ポケモンに\nリボンを　つけて　あげた！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
        "text": "{PLAYER}给挑战的宝可梦\n戴上了缎带。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
        "text": "{PLAYER}は　ポケモンに\nリボンを　つけて　あげた！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleTowerLobby_Text_PutRibbonOnMons",
      "file": "patch/batches/217_battle_frontier_battle_tower_lobby.json",
      "payload_address": "0x09048C98",
      "payload_sha256": "aa39d27e07a5ec5c51d87199d2c74be8096c878717729607f38ce8b55ac78fc1",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0821F7E0",
          "original": "0x08220769",
          "target": "0x09048C98",
          "batch": "patch/batches/217_battle_frontier_battle_tower_lobby.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6437 行 · ported_batch / 5185 · BattleFrontier_BattleTowerLobby_Text_ExplainLinkMultisChallenge

判定：`fixed_verified`

理由：恢复每人2只不同种类的参赛条件。

日文：

```text
つうしんマルチ　バトルルームは\nワイヤレスアダプタや　つうしんケーブルを\lつないだ　ともだちと　ふたりで\lちがう　しゅるいの　ポケモンを\l2ひきずつ　もちより\lマルチバトルで　たたかう　しせつです！\pタワーないには　マルチ　バトルルームという\nたいせんの　ための　へやが\lたくさん　ようい　されています！\pそれぞれ　マルチ　バトルルームには\n7くみの　タッグ　トレーナーが　いて\lあなたと　ともだちの　タッグでの\lチャレンジを　まっています！\pみごと　その　7くみを　たおせたら\nバトルポイントを　しんてい　いたします！\pまた　ほかの　しせつと　ちがって\nここでは　とちゅうで　ちょうせんを\lちゅうだん　できません！\p7かい　れんぞくで　たたかうことに　なるので\nじゅうぶん　ちゅうい　してください！$
```

英文：

```text
The BATTLE TOWER's MULTI BATTLE\nROOMS are facilities for conducting\lMULTI BATTLES with a friend.\pYou must link with your friend using\nWireless Adapters or a Game Boy\lAdvance Game Link cable.\pYou must partner with your friend and\nenter two different kinds of POKéMON.\pThere are many MULTI BATTLE ROOMS\nin the BATTLE TOWER for team battles.\pIn a MULTI BATTLE ROOM, seven\ntag teams await you and your friend\lto make a tag-team challenge.\pIf you manage to defeat all seven\nteams, you will earn Battle Points.\pPlease beware that unlike other ROOMS,\nyou may not interrupt your challenge.\pOnce you start, you must battle seven\nMULTI BATTLES in a row nonstop.$
```

报告原中文：

```text
对战塔的多人对战间\n是和朋友一起进行\l多人对战的设施。\p您需要先使用无线适配器\n或GBA连接线与朋友连接，\p携带2只宝可梦和朋友\n组队进行挑战。\p对战塔内有很多\n多人对战间，\p供团队对战使用。\n在多人对战间中，\l会有7组训练家等待\p您和您朋友的组队挑战。\n如果顺利战胜7组，\p我们会向您呈上对战点数。\n请注意这里与其他房间不同，\p您不能暂停挑战。一旦挑战开始，\n就需要不间断地进行7次多人对战。$
```

修复前实际中文：

```text
对战塔的多人对战间
是和朋友一起进行\l多人对战的设施。\p您需要先使用无线适配器
或GBA连接线与朋友连接，\p携带2只宝可梦和朋友
组队进行挑战。\p对战塔内有很多
多人对战间，\p供团队对战使用。
在多人对战间中，\l会有7组训练家等待\p您和您朋友的组队挑战。
如果顺利战胜7组，\p我们会向您呈上对战点数。
请注意这里与其他房间不同，\p您不能暂停挑战。一旦挑战开始，
就需要不间断地进行7次多人对战。
```

最终中文：

```text
对战塔的多人对战间
是和朋友一起进行\l多人对战的设施。\p您需要先使用无线适配器
或GBA连接线与朋友连接，\p每人携带2只不同种类的
宝可梦，和朋友组队挑战。\p对战塔内有很多
多人对战间，\p供团队对战使用。
在多人对战间中，\l会有7组训练家等待\p您和您朋友的组队挑战。
如果顺利战胜7组，\p我们会向您呈上对战点数。
请注意这里与其他房间不同，\p您不能暂停挑战。一旦挑战开始，
就需要不间断地进行7次多人对战。
```

证据：

```json
{
  "review": {
    "row_number": 6437,
    "symbol": "BattleFrontier_BattleTowerLobby_Text_ExplainLinkMultisChallenge",
    "domain": "ported_batch",
    "idx": "5185",
    "old": "携带2只宝可梦和朋友\n组队进行挑战。",
    "new": "每人携带2只不同种类的\n宝可梦，和朋友组队挑战。",
    "reason": "恢复每人2只不同种类的参赛条件。",
    "scope": "both",
    "action": "fix",
    "final_text": "对战塔的多人对战间\n是和朋友一起进行\\l多人对战的设施。\\p您需要先使用无线适配器\n或GBA连接线与朋友连接，\\p每人携带2只不同种类的\n宝可梦，和朋友组队挑战。\\p对战塔内有很多\n多人对战间，\\p供团队对战使用。\n在多人对战间中，\\l会有7组训练家等待\\p您和您朋友的组队挑战。\n如果顺利战胜7组，\\p我们会向您呈上对战点数。\n请注意这里与其他房间不同，\\p您不能暂停挑战。一旦挑战开始，\n就需要不间断地进行7次多人对战。",
    "old_current_text": "对战塔的多人对战间\n是和朋友一起进行\\l多人对战的设施。\\p您需要先使用无线适配器\n或GBA连接线与朋友连接，\\p携带2只宝可梦和朋友\n组队进行挑战。\\p对战塔内有很多\n多人对战间，\\p供团队对战使用。\n在多人对战间中，\\l会有7组训练家等待\\p您和您朋友的组队挑战。\n如果顺利战胜7组，\\p我们会向您呈上对战点数。\n请注意这里与其他房间不同，\\p您不能暂停挑战。一旦挑战开始，\n就需要不间断地进行7次多人对战。",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
      "patch/batches/217_battle_frontier_battle_tower_lobby.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
        "text": "つうしんマルチ　バトルルームは\nワイヤレスアダプタや　つうしんケーブルを\\lつないだ　ともだちと　ふたりで\\lちがう　しゅるいの　ポケモンを\\l2ひきずつ　もちより\\lマルチバトルで　たたかう　しせつです！\\pタワーないには　マルチ　バトルルームという\nたいせんの　ための　へやが\\lたくさん　ようい　されています！\\pそれぞれ　マルチ　バトルルームには\n7くみの　タッグ　トレーナーが　いて\\lあなたと　ともだちの　タッグでの\\lチャレンジを　まっています！\\pみごと　その　7くみを　たおせたら\nバトルポイントを　しんてい　いたします！\\pまた　ほかの　しせつと　ちがって\nここでは　とちゅうで　ちょうせんを\\lちゅうだん　できません！\\p7かい　れんぞくで　たたかうことに　なるので\nじゅうぶん　ちゅうい　してください！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
        "text": "对战塔的多人对战间\n是和朋友一起进行\\l多人对战的设施。\\p您需要先使用无线适配器\n或GBA连接线与朋友连接，\\p每人携带2只不同种类的\n宝可梦，和朋友组队挑战。\\p对战塔内有很多\n多人对战间，\\p供团队对战使用。\n在多人对战间中，\\l会有7组训练家等待\\p您和您朋友的组队挑战。\n如果顺利战胜7组，\\p我们会向您呈上对战点数。\n请注意这里与其他房间不同，\\p您不能暂停挑战。一旦挑战开始，\n就需要不间断地进行7次多人对战。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerLobby/scripts.inc",
        "text": "つうしんマルチ　バトルルームは\nワイヤレスアダプタや　つうしんケーブルを\\lつないだ　ともだちと　ふたりで\\lちがう　しゅるいの　ポケモンを\\l2ひきずつ　もちより\\lマルチバトルで　たたかう　しせつです！\\pタワーないには　マルチ　バトルルームという\nたいせんの　ための　へやが\\lたくさん　ようい　されています！\\pそれぞれ　マルチ　バトルルームには\n7くみの　タッグ　トレーナーが　いて\\lあなたと　ともだちの　タッグでの\\lチャレンジを　まっています！\\pみごと　その　7くみを　たおせたら\nバトルポイントを　しんてい　いたします！\\pまた　ほかの　しせつと　ちがって\nここでは　とちゅうで　ちょうせんを\\lちゅうだん　できません！\\p7かい　れんぞくで　たたかうことに　なるので\nじゅうぶん　ちゅうい　してください！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleTowerLobby_Text_ExplainLinkMultisChallenge",
      "file": "patch/batches/217_battle_frontier_battle_tower_lobby.json",
      "payload_address": "0x09049530",
      "payload_sha256": "b7327db6cabf4abcfd97c008c55be19fc9201acbc006933fa3e517c7b2a7381f",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0822041D",
          "original": "0x08221540",
          "target": "0x09049530",
          "batch": "patch/batches/217_battle_frontier_battle_tower_lobby.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6493 行 · ported_batch / 5241 · BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice10Reject

判定：`fixed_verified`

理由：拒绝邀请时的クール是冷淡，不是吝啬。

日文：

```text
ぐわーっ！\n{PLAYER}さん　ってのは　クールだね！$
```

英文：

```text
Gwaaah!\nYou're a calculating one, {PLAYER}!$
```

报告原中文：

```text
切！\n你真是个斤斤计较的家伙，{PLAYER}！$
```

修复前实际中文：

```text
切！
你真是个斤斤计较的家伙，{PLAYER}！
```

最终中文：

```text
切！
你真是个冷酷的家伙，{PLAYER}！
```

证据：

```json
{
  "review": {
    "row_number": 6493,
    "symbol": "BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice10Reject",
    "domain": "ported_batch",
    "idx": "5241",
    "old": "斤斤计较的家伙",
    "new": "冷酷的家伙",
    "reason": "拒绝邀请时的クール是冷淡，不是吝啬。",
    "scope": "both",
    "action": "fix",
    "final_text": "切！\n你真是个冷酷的家伙，{PLAYER}！",
    "old_current_text": "切！\n你真是个斤斤计较的家伙，{PLAYER}！",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
      "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "ぐわーっ！\n{PLAYER}さん　ってのは　クールだね！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "切！\n你真是个冷酷的家伙，{PLAYER}！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "ぐわーっ！\n{PLAYER}さん　ってのは　クールだね！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice10Reject",
      "file": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json",
      "payload_address": "0x0904A556",
      "payload_sha256": "ecc1a73ee0ed8fb763c7b12b06c7ad28d33b8de79d34773a713bccd2ea6e77f6",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085BBFE0",
          "original": "0x0822415B",
          "target": "0x0904A556",
          "batch": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6553 行 · ported_batch / 5301 · BattleFrontier_BattleTowerMultiPartnerRoom_Text_ExpertFReject

判定：`fixed_verified`

理由：原文希望下次组队，不要求回心转意。

日文：

```text
つぎに　あったときには\nタッグを　くみたいものですね⋯⋯$
```

英文：

```text
Perhaps we can form a team the next\ntime we meet.$
```

报告原中文：

```text
希望在我们下一次见面的时候\n你会回心转意。$
```

修复前实际中文：

```text
希望在我们下一次见面的时候
你会回心转意。
```

最终中文：

```text
希望在我们下一次见面的时候
能和你组队。
```

证据：

```json
{
  "review": {
    "row_number": 6553,
    "symbol": "BattleFrontier_BattleTowerMultiPartnerRoom_Text_ExpertFReject",
    "domain": "ported_batch",
    "idx": "5301",
    "old": "希望在我们下一次见面的时候\n你会回心转意。",
    "new": "希望在我们下一次见面的时候\n能和你组队。",
    "reason": "原文希望下次组队，不要求回心转意。",
    "scope": "both",
    "action": "fix",
    "final_text": "希望在我们下一次见面的时候\n能和你组队。",
    "old_current_text": "希望在我们下一次见面的时候\n你会回心转意。",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
      "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "つぎに　あったときには\nタッグを　くみたいものですね⋯⋯$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "希望在我们下一次见面的时候\n能和你组队。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "つぎに　あったときには\nタッグを　くみたいものですね⋯⋯$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleTowerMultiPartnerRoom_Text_ExpertFReject",
      "file": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json",
      "payload_address": "0x0904AF07",
      "payload_sha256": "a2e5d008e142aa8f7a152f801c3a8144e0584cc098834a6a8c7c29cb30d83727",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085BC238",
          "original": "0x08225579",
          "target": "0x0904AF07",
          "batch": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6564 行 · ported_batch / 5312 · BattleFrontier_BattleTowerMultiPartnerRoom_Text_SailorAccept

判定：`fixed_verified`

理由：I did not expect any less / 当然 指果然如此，不是出乎意料。

日文：

```text
とうぜん　だよな！\nいまから　とうろく　してくるぜ！$
```

英文：

```text
I didn't expect any less!\nI'll go register now.$
```

报告原中文：

```text
这简直太出乎我的意料了！\n我现在就去登记。$
```

修复前实际中文：

```text
这简直太出乎我的意料了！
我现在就去登记。
```

最终中文：

```text
我就知道你会答应！
我现在就去登记。
```

证据：

```json
{
  "review": {
    "row_number": 6564,
    "symbol": "BattleFrontier_BattleTowerMultiPartnerRoom_Text_SailorAccept",
    "domain": "ported_batch",
    "idx": "5312",
    "old": "这简直太出乎我的意料了！",
    "new": "我就知道你会答应！",
    "reason": "I did not expect any less / 当然 指果然如此，不是出乎意料。",
    "scope": "both",
    "action": "fix",
    "final_text": "我就知道你会答应！\n我现在就去登记。",
    "old_current_text": "这简直太出乎我的意料了！\n我现在就去登记。",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
      "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "とうぜん　だよな！\nいまから　とうろく　してくるぜ！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "我就知道你会答应！\n我现在就去登记。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "とうぜん　だよな！\nいまから　とうろく　してくるぜ！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleTowerMultiPartnerRoom_Text_SailorAccept",
      "file": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json",
      "payload_address": "0x0904B0C3",
      "payload_sha256": "f65e993c98f6523e314230d62cb7151d4cf8d0aac6b558437c9299ea64830460",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085BC2AC",
          "original": "0x082258B4",
          "target": "0x0904B0C3",
          "batch": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6622 行 · ported_batch / 5370 · BattleFrontier_BattleTowerMultiPartnerRoom_Text_LassIntro

判定：`fixed_verified`

理由：原文是训练家职业，而不是自称一件衣物。

日文：

```text
わたし\nミニスカート　{STR_VAR_1}！$
```

英文：

```text
I'm {STR_VAR_1}, and I'm a LASS!$
```

报告原中文：

```text
我是{STR_VAR_1}，一个迷你裙！$
```

修复前实际中文：

```text
我是{STR_VAR_1}，一个迷你裙！
```

最终中文：

```text
我是短裙少女{STR_VAR_1}！
```

证据：

```json
{
  "review": {
    "row_number": 6622,
    "symbol": "BattleFrontier_BattleTowerMultiPartnerRoom_Text_LassIntro",
    "domain": "ported_batch",
    "idx": "5370",
    "old": "我是{STR_VAR_1}，一个迷你裙！",
    "new": "我是短裙少女{STR_VAR_1}！",
    "reason": "原文是训练家职业，而不是自称一件衣物。",
    "scope": "both",
    "action": "fix",
    "final_text": "我是短裙少女{STR_VAR_1}！",
    "old_current_text": "我是{STR_VAR_1}，一个迷你裙！",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
      "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "わたし\nミニスカート　{STR_VAR_1}！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "我是短裙少女{STR_VAR_1}！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "わたし\nミニスカート　{STR_VAR_1}！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleTowerMultiPartnerRoom_Text_LassIntro",
      "file": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json",
      "payload_address": "0x0904BB8C",
      "payload_sha256": "a58d6fb8ae85fb2602a8274e8d53bb717dc96ed0f48682085ef61b570eb7ebb2",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085BC05C",
          "original": "0x0822477D",
          "target": "0x0904BB8C",
          "batch": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6660 行 · ported_batch / 5408 · BattleFrontier_BattleTowerMultiPartnerRoom_Text_HexManiacMon2Ask

判定：`fixed_verified`

理由：I beseech you 是请求，不是看好对方。

日文：

```text
{STR_VAR_1}を　もつ　{STR_VAR_2}を\nもっております⋯⋯\pどうか　わたくしと\nタッグを　くんでいただけませんか？$
```

英文：

```text
{STR_VAR_1}-using {STR_VAR_2}…\pI beseech you…\nJoin me in a tag team…$
```

报告原中文：

```text
使用{STR_VAR_1}的{STR_VAR_2}……\p我看好你……\n我们组队……$
```

修复前实际中文：

```text
使用{STR_VAR_1}的{STR_VAR_2}……\p我看好你……
我们组队……
```

最终中文：

```text
使用{STR_VAR_1}的{STR_VAR_2}……\p拜托你……
和我组队吧……
```

证据：

```json
{
  "review": {
    "row_number": 6660,
    "symbol": "BattleFrontier_BattleTowerMultiPartnerRoom_Text_HexManiacMon2Ask",
    "domain": "ported_batch",
    "idx": "5408",
    "old": "我看好你……\n我们组队……",
    "new": "拜托你……\n和我组队吧……",
    "reason": "I beseech you 是请求，不是看好对方。",
    "scope": "both",
    "action": "fix",
    "final_text": "使用{STR_VAR_1}的{STR_VAR_2}……\\p拜托你……\n和我组队吧……",
    "old_current_text": "使用{STR_VAR_1}的{STR_VAR_2}……\\p我看好你……\n我们组队……",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
      "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "{STR_VAR_1}を　もつ　{STR_VAR_2}を\nもっております⋯⋯\\pどうか　わたくしと\nタッグを　くんでいただけませんか？$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "使用{STR_VAR_1}的{STR_VAR_2}……\\p拜托你……\n和我组队吧……$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "{STR_VAR_1}を　もつ　{STR_VAR_2}を\nもっております⋯⋯\\pどうか　わたくしと\nタッグを　くんでいただけませんか？$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleTowerMultiPartnerRoom_Text_HexManiacMon2Ask",
      "file": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json",
      "payload_address": "0x0904C1D8",
      "payload_sha256": "f166c696d1837b34e36eea949655b4f0e42691773632a80d86b9e85a4bf897f1",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085BC154",
          "original": "0x08224EA1",
          "target": "0x0904C1D8",
          "batch": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6692 行 · ported_batch / 5440 · BattleFrontier_BattleTowerMultiPartnerRoom_Text_ExpertFMon1

判定：`fixed_verified`

理由：raised thoroughly / 鍛え上げた 指培育，而非热爱。

日文：

```text
わたしの　きたえあげた　ポケモンは\n{STR_VAR_1}を　つかう　{STR_VAR_2}と⋯⋯$
```

英文：

```text
I've raised my POKéMON thoroughly.\nOne {STR_VAR_2} with {STR_VAR_1} and$
```

报告原中文：

```text
我十分的热爱宝可梦。\n一只掌握{STR_VAR_1}的{STR_VAR_2}和$
```

修复前实际中文：

```text
我十分的热爱宝可梦。
一只掌握{STR_VAR_1}的{STR_VAR_2}和
```

最终中文：

```text
我精心培育了宝可梦。
一只掌握{STR_VAR_1}的{STR_VAR_2}和
```

证据：

```json
{
  "review": {
    "row_number": 6692,
    "symbol": "BattleFrontier_BattleTowerMultiPartnerRoom_Text_ExpertFMon1",
    "domain": "ported_batch",
    "idx": "5440",
    "old": "我十分的热爱宝可梦。",
    "new": "我精心培育了宝可梦。",
    "reason": "raised thoroughly / 鍛え上げた 指培育，而非热爱。",
    "scope": "both",
    "action": "fix",
    "final_text": "我精心培育了宝可梦。\n一只掌握{STR_VAR_1}的{STR_VAR_2}和",
    "old_current_text": "我十分的热爱宝可梦。\n一只掌握{STR_VAR_1}的{STR_VAR_2}和",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
      "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "わたしの　きたえあげた　ポケモンは\n{STR_VAR_1}を　つかう　{STR_VAR_2}と⋯⋯$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "我精心培育了宝可梦。\n一只掌握{STR_VAR_1}的{STR_VAR_2}和$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "わたしの　きたえあげた　ポケモンは\n{STR_VAR_1}を　つかう　{STR_VAR_2}と⋯⋯$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleTowerMultiPartnerRoom_Text_ExpertFMon1",
      "file": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json",
      "payload_address": "0x0904C787",
      "payload_sha256": "8fd1680109c1aad4d9c6c64abc14a4351702d6133397bbf0ff9759458bd5b5b0",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085BC22C",
          "original": "0x08225515",
          "target": "0x0904C787",
          "batch": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6717 行 · ported_batch / 5465 · BattleFrontier_BattleTowerMultiPartnerRoom_Text_PkmnRangerMMon2Ask

判定：`fixed_verified`

理由：重复字。

日文：

```text
{STR_VAR_1}を　つかう　{STR_VAR_2}だ！\pどうだい？\nぼくと　タッグを　くんでみない？$
```

英文：

```text
one {STR_VAR_2} with {STR_VAR_1}!\pDon't you think we'd make an impressive\ntag team?$
```

报告原中文：

```text
一只掌握{STR_VAR_1}的{STR_VAR_2}！\p你不认为我们我们能构成\n一支令人印象深刻的队伍吗？$
```

修复前实际中文：

```text
一只掌握{STR_VAR_1}的{STR_VAR_2}！\p你不认为我们我们能构成
一支令人印象深刻的队伍吗？
```

最终中文：

```text
一只掌握{STR_VAR_1}的{STR_VAR_2}！\p你不认为我们能构成
一支令人印象深刻的队伍吗？
```

证据：

```json
{
  "review": {
    "row_number": 6717,
    "symbol": "BattleFrontier_BattleTowerMultiPartnerRoom_Text_PkmnRangerMMon2Ask",
    "domain": "ported_batch",
    "idx": "5465",
    "old": "我们我们",
    "new": "我们",
    "reason": "重复字。",
    "scope": "both",
    "action": "fix",
    "final_text": "一只掌握{STR_VAR_1}的{STR_VAR_2}！\\p你不认为我们能构成\n一支令人印象深刻的队伍吗？",
    "old_current_text": "一只掌握{STR_VAR_1}的{STR_VAR_2}！\\p你不认为我们我们能构成\n一支令人印象深刻的队伍吗？",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
      "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "{STR_VAR_1}を　つかう　{STR_VAR_2}だ！\\pどうだい？\nぼくと　タッグを　くんでみない？$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "一只掌握{STR_VAR_1}的{STR_VAR_2}！\\p你不认为我们能构成\n一支令人印象深刻的队伍吗？$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "{STR_VAR_1}を　つかう　{STR_VAR_2}だ！\\pどうだい？\nぼくと　タッグを　くんでみない？$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleTowerMultiPartnerRoom_Text_PkmnRangerMMon2Ask",
      "file": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json",
      "payload_address": "0x0904CC22",
      "payload_sha256": "af04ea8fdf2aac7ef8bff47def8bb441c86fa34511eb9e8e9909c598b1ccda53",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085BC2D0",
          "original": "0x082259B5",
          "target": "0x0904CC22",
          "batch": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6723 行 · ported_batch / 5471 · BattleFrontier_BattleTowerMultiPartnerRoom_Text_AromaLadyMon2Ask

判定：`fixed_verified`

理由：这个模板只列出会某招式的宝可梦，原文没有到处旅行。

日文：

```text
{STR_VAR_1}を　つかう　{STR_VAR_2}です\pどうでしょう？\nわたくしと　タッグを　くんでみませんか？$
```

英文：

```text
one {STR_VAR_2} that uses\n{STR_VAR_1}.\pI hope they strike your fancy.\nWould you care to be my partner?$
```

报告原中文：

```text
一只学会{STR_VAR_1}的{STR_VAR_2}\n到处旅行。\p希望你会喜欢它们。\n你想成为我的搭档吗？$
```

修复前实际中文：

```text
一只学会{STR_VAR_1}的{STR_VAR_2}
到处旅行。\p希望你会喜欢它们。
你想成为我的搭档吗？
```

最终中文：

```text
一只学会{STR_VAR_1}的{STR_VAR_2}。\p希望你会喜欢它们。
你想成为我的搭档吗？
```

证据：

```json
{
  "review": {
    "row_number": 6723,
    "symbol": "BattleFrontier_BattleTowerMultiPartnerRoom_Text_AromaLadyMon2Ask",
    "domain": "ported_batch",
    "idx": "5471",
    "old": "的{STR_VAR_2}\n到处旅行。",
    "new": "的{STR_VAR_2}。",
    "reason": "这个模板只列出会某招式的宝可梦，原文没有到处旅行。",
    "scope": "both",
    "action": "fix",
    "final_text": "一只学会{STR_VAR_1}的{STR_VAR_2}。\\p希望你会喜欢它们。\n你想成为我的搭档吗？",
    "old_current_text": "一只学会{STR_VAR_1}的{STR_VAR_2}\n到处旅行。\\p希望你会喜欢它们。\n你想成为我的搭档吗？",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
      "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "{STR_VAR_1}を　つかう　{STR_VAR_2}です\\pどうでしょう？\nわたくしと　タッグを　くんでみませんか？$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "一只学会{STR_VAR_1}的{STR_VAR_2}。\\p希望你会喜欢它们。\n你想成为我的搭档吗？$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattleTowerMultiPartnerRoom/scripts.inc",
        "text": "{STR_VAR_1}を　つかう　{STR_VAR_2}です\\pどうでしょう？\nわたくしと　タッグを　くんでみませんか？$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_BattleTowerMultiPartnerRoom_Text_AromaLadyMon2Ask",
      "file": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json",
      "payload_address": "0x0904CD61",
      "payload_sha256": "2bb165940422c8c15a85d282d911e57818e5401f92267d2018a5050cea4be0fd",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085BC2F8",
          "original": "0x08225AD5",
          "target": "0x0904CD61",
          "batch": "patch/batches/219_battle_frontier_battle_tower_multi_partner_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6891 行 · ported_batch / 5639 · BattleFrontier_Lounge7_Text_RockSlideDesc

判定：`fixed_verified`

理由：统一第三世代flinch状态术语。

日文：

```text
いわで　こうげき\nてきを　ひるませる\nことが　ある$
```

英文：

```text
Large boulders\nare hurled. May\ncause flinching.$
```

报告原中文：

```text
投出巨大的石块，\n可以使对手\n恐惧。$
```

修复前实际中文：

```text
投出巨大的石块，
可以使对手
恐惧。
```

最终中文：

```text
投出巨大的石块，
可以使对手
畏缩。
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_Lounge7/scripts.inc",
        "text": "投出巨大的石块，\n可以使对手\n畏缩。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_Lounge7/scripts.inc",
        "text": "いわで　こうげき\nてきを　ひるませる\nことが　ある$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_Lounge7_Text_RockSlideDesc",
      "file": "patch/batches/224_battle_frontier_lounge7.json",
      "payload_address": "0x0904F29E",
      "payload_sha256": "e637b17b645576005d79c612cf2e62503a21094bb2b192792f030708265548c9",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08592C9C",
          "original": "0x0823A0BF",
          "target": "0x0904F29E",
          "batch": "patch/batches/224_battle_frontier_lounge7.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6916 行 · ported_batch / 5664 · BattleFrontier_OutsideEast_Text_RankingHallSign

判定：`fixed_verified`

理由：Set your sights on new records 指挑战纪录，而非关注新闻。

日文：

```text
バトルフロンティア　ランキングホール\nきざめ！　さいこうの　きろく！$
```

英文：

```text
BATTLE FRONTIER RANKING HALL\nSet your sights on new records!$
```

报告原中文：

```text
对战开拓区排名大厅\n关注最新的纪录！$
```

修复前实际中文：

```text
对战开拓区排名大厅
关注最新的纪录！
```

最终中文：

```text
对战开拓区排名大厅
向新纪录发起挑战！
```

证据：

```json
{
  "review": {
    "row_number": 6916,
    "symbol": "BattleFrontier_OutsideEast_Text_RankingHallSign",
    "domain": "ported_batch",
    "idx": "5664",
    "old": "关注最新的纪录！",
    "new": "向新纪录发起挑战！",
    "reason": "Set your sights on new records 指挑战纪录，而非关注新闻。",
    "scope": "both",
    "action": "fix",
    "final_text": "对战开拓区排名大厅\n向新纪录发起挑战！",
    "old_current_text": "对战开拓区排名大厅\n关注最新的纪录！",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_OutsideEast/scripts.inc",
      "patch/batches/227_battle_frontier_outside_east.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
        "text": "バトルフロンティア　ランキングホール\nきざめ！　さいこうの　きろく！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
        "text": "对战开拓区排名大厅\n向新纪录发起挑战！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
        "text": "バトルフロンティア　ランキングホール\nきざめ！　さいこうの　きろく！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_OutsideEast_Text_RankingHallSign",
      "file": "patch/batches/227_battle_frontier_outside_east.json",
      "payload_address": "0x0904F7E9",
      "payload_sha256": "a62fc961c174d0e70d98f293ef85bea011960ae57ea59b323f157aa529c7ad7a",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08222B6C",
          "original": "0x08222C23",
          "target": "0x0904F7E9",
          "batch": "patch/batches/227_battle_frontier_outside_east.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6921 行 · ported_batch / 5669 · BattleFrontier_OutsideEast_Text_ThriveInDarkness

判定：`fixed_verified`

理由：JP大好き / EN thrive 不表示童年成长地点。

日文：

```text
くらやみが　だいすきな　わたし⋯⋯\nそう⋯⋯　わたしに　ふさわしい　のは⋯⋯\lやはり　この　バトルピラミッド⋯⋯\pネ⋯⋯　あなたも　くらやみの　なかを\nひっしに　さまよって　みない⋯⋯？$
```

英文：

```text
I thrive in darkness…\nYes… What is worthy of me?\lNone other than the BATTLE PYRAMID…\pWhat say you to wandering in darkness\nand in utter and total desperation?$
```

报告原中文：

```text
我是在黑暗中长大的……\n是的……哪里最适合我？\l必然是对战金字塔……\p在黑暗中探索的时候\n你是不是也会陷入完全的绝望？$
```

修复前实际中文：

```text
我是在黑暗中长大的……
是的……哪里最适合我？\l必然是对战金字塔……\p在黑暗中探索的时候
你是不是也会陷入完全的绝望？
```

最终中文：

```text
我最喜欢黑暗……
是的……哪里最适合我？\l必然是对战金字塔……\p在黑暗中探索的时候
你是不是也会陷入完全的绝望？
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
        "text": "我最喜欢黑暗……\n是的……哪里最适合我？\\l必然是对战金字塔……\\p在黑暗中探索的时候\n你是不是也会陷入完全的绝望？$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
        "text": "くらやみが　だいすきな　わたし⋯⋯\nそう⋯⋯　わたしに　ふさわしい　のは⋯⋯\\lやはり　この　バトルピラミッド⋯⋯\\pネ⋯⋯　あなたも　くらやみの　なかを\nひっしに　さまよって　みない⋯⋯？$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_OutsideEast_Text_ThriveInDarkness",
      "file": "patch/batches/227_battle_frontier_outside_east.json",
      "payload_address": "0x0904F940",
      "payload_sha256": "4e791410ca11fb72227da3b3f041dc40359f6a9ec6497dcd659e03c4b6ef69cf",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08222A21",
          "original": "0x08222D54",
          "target": "0x0904F940",
          "batch": "patch/batches/227_battle_frontier_outside_east.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6933 行 · ported_batch / 5681 · BattleFrontier_OutsideEast_Text_LegendOfBattlePyramid

判定：`fixed_verified`

理由：man among men / 男の中の男 是男子汉，不是在人群出现。

日文：

```text
きみは　しって　いるか！？\nバトルピラミッドの　でんせつを！！\pみなぎる　ゆうきを　もつ　トレーナー\nきんじとうの　いただきを　めざすとき\lおとこの　なかの　おとこ　あらわれる\p⋯⋯どうだ？　しらないだろー！\nだって　これ　さっき　おれが\lかんがえたんだ　もんな！\pなに？　どういう　いみ　かって？\nチッチッ！！　それは　おしえられないな！$
```

英文：

```text
Do you know it?\nThe legend of the BATTLE PYRAMID?\pWhen there comes a confident TRAINER\nreaching for the golden pinnacle,\lthere shall appear a man among men.\pDon't know that legend?\nWell, of course not!\lI just made it up!\pWhat's it supposed to mean?\nThat, my friend, I can't say!$
```

报告原中文：

```text
你听说过那个关于\n对战金字塔的传说吗？\p当一位勇敢的训练家到达\n金光闪闪的顶峰之时，\l就会有一个人出现在人群中。\p你知道这个传说吗？\n哈哈，你当然不知道！\l这是我刚刚编的！\p至于这是什么意思，\n那是，呃，不告诉你！$
```

修复前实际中文：

```text
你听说过那个关于
对战金字塔的传说吗？\p当一位勇敢的训练家到达
金光闪闪的顶峰之时，\l就会有一个人出现在人群中。\p你知道这个传说吗？
哈哈，你当然不知道！\l这是我刚刚编的！\p至于这是什么意思，
那是，呃，不告诉你！
```

最终中文：

```text
你听说过那个关于
对战金字塔的传说吗？\p当一位勇敢的训练家到达
金光闪闪的顶峰之时，\l就会有一位真正的男子汉出现。\p你知道这个传说吗？
哈哈，你当然不知道！\l这是我刚刚编的！\p至于这是什么意思，
那是，呃，不告诉你！
```

证据：

```json
{
  "review": {
    "row_number": 6933,
    "symbol": "BattleFrontier_OutsideEast_Text_LegendOfBattlePyramid",
    "domain": "ported_batch",
    "idx": "5681",
    "old": "就会有一个人出现在人群中。",
    "new": "就会有一位真正的男子汉出现。",
    "reason": "man among men / 男の中の男 是男子汉，不是在人群出现。",
    "scope": "both",
    "action": "fix",
    "final_text": "你听说过那个关于\n对战金字塔的传说吗？\\p当一位勇敢的训练家到达\n金光闪闪的顶峰之时，\\l就会有一位真正的男子汉出现。\\p你知道这个传说吗？\n哈哈，你当然不知道！\\l这是我刚刚编的！\\p至于这是什么意思，\n那是，呃，不告诉你！",
    "old_current_text": "你听说过那个关于\n对战金字塔的传说吗？\\p当一位勇敢的训练家到达\n金光闪闪的顶峰之时，\\l就会有一个人出现在人群中。\\p你知道这个传说吗？\n哈哈，你当然不知道！\\l这是我刚刚编的！\\p至于这是什么意思，\n那是，呃，不告诉你！",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_OutsideEast/scripts.inc",
      "patch/batches/227_battle_frontier_outside_east.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
        "text": "きみは　しって　いるか！？\nバトルピラミッドの　でんせつを！！\\pみなぎる　ゆうきを　もつ　トレーナー\nきんじとうの　いただきを　めざすとき\\lおとこの　なかの　おとこ　あらわれる\\p⋯⋯どうだ？　しらないだろー！\nだって　これ　さっき　おれが\\lかんがえたんだ　もんな！\\pなに？　どういう　いみ　かって？\nチッチッ！！　それは　おしえられないな！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
        "text": "你听说过那个关于\n对战金字塔的传说吗？\\p当一位勇敢的训练家到达\n金光闪闪的顶峰之时，\\l就会有一位真正的男子汉出现。\\p你知道这个传说吗？\n哈哈，你当然不知道！\\l这是我刚刚编的！\\p至于这是什么意思，\n那是，呃，不告诉你！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
        "text": "きみは　しって　いるか！？\nバトルピラミッドの　でんせつを！！\\pみなぎる　ゆうきを　もつ　トレーナー\nきんじとうの　いただきを　めざすとき\\lおとこの　なかの　おとこ　あらわれる\\p⋯⋯どうだ？　しらないだろー！\nだって　これ　さっき　おれが\\lかんがえたんだ　もんな！\\pなに？　どういう　いみ　かって？\nチッチッ！！　それは　おしえられないな！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_OutsideEast_Text_LegendOfBattlePyramid",
      "file": "patch/batches/227_battle_frontier_outside_east.json",
      "payload_address": "0x0904FD6D",
      "payload_sha256": "ed445451656fe3c2877ba788634168e9095400deee8987052a07784c798d4c3c",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08222B29",
          "original": "0x08223080",
          "target": "0x0904FD6D",
          "batch": "patch/batches/227_battle_frontier_outside_east.json"
        }
      ]
    }
  ]
}
```

### CSV 第 6943 行 · ported_batch / 5691 · BattleFrontier_OutsideEast_Text_StickyMonWithLongTail

判定：`fixed_verified`

理由：sticky / ベタベタ 的黏性不是体型小。

日文：

```text
ぼぼぼ　ぼく　みちゃったんだっ！！\pこのさきの　いわ　から　しっぽが　ながくって\nなんか　ベタベタした　ポケモンが\lぼくの　こと　じーっと　のぞいてたんだっ！\pきっと　こわい　ポケモン　だよーっ！！$
```

英文：

```text
I…\nI saw it!\pThere was a sticky sort of a POKéMON\nwith a long tail up ahead!\pIt was hiding under a boulder, and\nit kept staring at me!$
```

报告原中文：

```text
我……\n我看见了！\p是一只举着长长尾巴的\n小小的宝可梦！\p刚才它藏在一块大石头底下，\n还一直偷偷地盯着我看！$
```

修复前实际中文：

```text
我……
我看见了！\p是一只举着长长尾巴的
小小的宝可梦！\p刚才它藏在一块大石头底下，
还一直偷偷地盯着我看！
```

最终中文：

```text
我……
我看见了！\p是一只长着长长尾巴的
黏糊糊的宝可梦！\p刚才它藏在一块大石头底下，
还一直偷偷地盯着我看！
```

证据：

```json
{
  "review": {
    "row_number": 6943,
    "symbol": "BattleFrontier_OutsideEast_Text_StickyMonWithLongTail",
    "domain": "ported_batch",
    "idx": "5691",
    "old": "是一只举着长长尾巴的\n小小的宝可梦！",
    "new": "是一只长着长长尾巴的\n黏糊糊的宝可梦！",
    "reason": "sticky / ベタベタ 的黏性不是体型小。",
    "scope": "both",
    "action": "fix",
    "final_text": "我……\n我看见了！\\p是一只长着长长尾巴的\n黏糊糊的宝可梦！\\p刚才它藏在一块大石头底下，\n还一直偷偷地盯着我看！",
    "old_current_text": "我……\n我看见了！\\p是一只举着长长尾巴的\n小小的宝可梦！\\p刚才它藏在一块大石头底下，\n还一直偷偷地盯着我看！",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_OutsideEast/scripts.inc",
      "patch/batches/227_battle_frontier_outside_east.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
        "text": "ぼぼぼ　ぼく　みちゃったんだっ！！\\pこのさきの　いわ　から　しっぽが　ながくって\nなんか　ベタベタした　ポケモンが\\lぼくの　こと　じーっと　のぞいてたんだっ！\\pきっと　こわい　ポケモン　だよーっ！！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
        "text": "我……\n我看见了！\\p是一只长着长长尾巴的\n黏糊糊的宝可梦！\\p刚才它藏在一块大石头底下，\n还一直偷偷地盯着我看！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_OutsideEast/scripts.inc",
        "text": "ぼぼぼ　ぼく　みちゃったんだっ！！\\pこのさきの　いわ　から　しっぽが　ながくって\nなんか　ベタベタした　ポケモンが\\lぼくの　こと　じーっと　のぞいてたんだっ！\\pきっと　こわい　ポケモン　だよーっ！！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_OutsideEast_Text_StickyMonWithLongTail",
      "file": "patch/batches/227_battle_frontier_outside_east.json",
      "payload_address": "0x090501C6",
      "payload_sha256": "a46b933bba661084ec2dbf70af9b029bbb32f6c0170a64dbbc7884d692e3eb38",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08222BA6",
          "original": "0x08223411",
          "target": "0x090501C6",
          "batch": "patch/batches/227_battle_frontier_outside_east.json"
        },
        {
          "address": "0x0832757E",
          "original": "0x08223411",
          "target": "0x090501C6",
          "batch": "patch/batches/227_battle_frontier_outside_east.json"
        }
      ]
    }
  ]
}
```

### CSV 第 7008 行 · ported_batch / 5756 · BattleFrontier_ReceptionGate_Text_Level50Info

判定：`fixed_verified`

理由：below 50 不包括50本身。

日文：

```text
レベル50の　コースでは　なまえの　とおり\nレベル50までの　ポケモンを\lちょうせん　させることが　できます\pただし　レベル50より　ひくい　レベルの\nポケモンを　つれた　トレーナーが\lとうじょう　することは　ありません\lくれぐれも　ごちゅうい　ください\pなお　このコースが　バトルフロンティアの\nたたかいの　きほんと　なって　いますので\lぜひ　チャレンジして　みてください$
```

英文：

```text
The Level 50 course is open to POKéMON\nup to and including Level 50.\pPlease keep in mind, however, that\nno TRAINER you face will have any\lPOKéMON below Level 50.\pThis course is the entry level for\nbattles at the BATTLE FRONTIER.\pTo begin, we hope you will challenge\nthis course.$
```

报告原中文：

```text
Lv. 50级允许等级50级以内的\n宝可梦参加。\p但是，您遇到的训练家不会\n使用等级50以内的宝可梦。\p这是对战开拓区的\n入门级对战，\p我们建议您从这个模式\n开始挑战。$
```

修复前实际中文：

```text
Lv. 50级允许等级50级以内的
宝可梦参加。\p但是，您遇到的训练家不会
使用等级50以内的宝可梦。\p这是对战开拓区的
入门级对战，\p我们建议您从这个模式
开始挑战。
```

最终中文：

```text
Lv. 50级允许等级50级以内的
宝可梦参加。\p但是，您遇到的训练家不会
使用低于50级的宝可梦。\p这是对战开拓区的
入门级对战，\p我们建议您从这个模式
开始挑战。
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_ReceptionGate/scripts.inc",
        "text": "Lv. 50级允许等级50级以内的\n宝可梦参加。\\p但是，您遇到的训练家不会\n使用低于50级的宝可梦。\\p这是对战开拓区的\n入门级对战，\\p我们建议您从这个模式\n开始挑战。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_ReceptionGate/scripts.inc",
        "text": "レベル50の　コースでは　なまえの　とおり\nレベル50までの　ポケモンを\\lちょうせん　させることが　できます\\pただし　レベル50より　ひくい　レベルの\nポケモンを　つれた　トレーナーが\\lとうじょう　することは　ありません\\lくれぐれも　ごちゅうい　ください\\pなお　このコースが　バトルフロンティアの\nたたかいの　きほんと　なって　いますので\\lぜひ　チャレンジして　みてください$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_ReceptionGate_Text_Level50Info",
      "file": "patch/batches/230_battle_frontier_reception_gate.json",
      "payload_address": "0x0905141F",
      "payload_sha256": "d523c913c337a477bb7d9bee1be43bdd52d7936a38834f3d85f5254112f8dc6b",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0823A506",
          "original": "0x0823ABB0",
          "target": "0x0905141F",
          "batch": "patch/batches/230_battle_frontier_reception_gate.json"
        }
      ]
    }
  ]
}
```

### CSV 第 7009 行 · ported_batch / 5757 · BattleFrontier_ReceptionGate_Text_OpenLevelInfo

判定：`fixed_verified`

理由：报告所谓只允许最高等级不符合当前源码；实际发现60级边界译成以内，原文below60需改为低于60。

日文：

```text
オープンレベルの　コースでは\nちょうせんに　さんかする　ポケモンの\lレベルに　せいげんが　ありません\pあなたの　ポケモンの　レベルに　あわせて\nたいせんする　トレーナーの　ポケモンの\lレベルが　かわります\pただし　レベル60より　ひくい　レベルの\nポケモンを　つれた　トレーナーが\lとうじょう　することは　ありません$
```

英文：

```text
The Open Level course places no limit\non the levels of POKéMON entering\lchallenges.\pThe levels of your opponents will\nbe adjusted to match the levels of\lyour POKéMON.\pHowever, no TRAINER you face will\nhave any POKéMON below Level 60.$
```

报告原中文：

```text
自由等级对于参加的宝可梦\n没有等级限制。\p对手的宝可梦等级会根据\n您的宝可梦等级进行调整。\p但是，您遇到的训练家不会\n使用等级60以内的宝可梦。$
```

修复前实际中文：

```text
自由等级对于参加的宝可梦
没有等级限制。\p对手的宝可梦等级会根据
您的宝可梦等级进行调整。\p但是，您遇到的训练家不会
使用等级60以内的宝可梦。
```

最终中文：

```text
自由等级对于参加的宝可梦
没有等级限制。\p对手的宝可梦等级会根据
您的宝可梦等级进行调整。\p但是，您遇到的训练家不会
使用低于60级的宝可梦。
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_ReceptionGate/scripts.inc",
        "text": "自由等级对于参加的宝可梦\n没有等级限制。\\p对手的宝可梦等级会根据\n您的宝可梦等级进行调整。\\p但是，您遇到的训练家不会\n使用低于60级的宝可梦。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_ReceptionGate/scripts.inc",
        "text": "オープンレベルの　コースでは\nちょうせんに　さんかする　ポケモンの\\lレベルに　せいげんが　ありません\\pあなたの　ポケモンの　レベルに　あわせて\nたいせんする　トレーナーの　ポケモンの\\lレベルが　かわります\\pただし　レベル60より　ひくい　レベルの\nポケモンを　つれた　トレーナーが\\lとうじょう　することは　ありません$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_BattleFrontier_ReceptionGate_Text_OpenLevelInfo",
      "file": "patch/batches/230_battle_frontier_reception_gate.json",
      "payload_address": "0x090514B7",
      "payload_sha256": "1ad1cde45ddcfe8e46b8acfe14e8f52bec9cf378fe582bbe515af76de846ffa9",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0823A514",
          "original": "0x0823AC6C",
          "target": "0x090514B7",
          "batch": "patch/batches/230_battle_frontier_reception_gate.json"
        }
      ]
    }
  ]
}
```

### CSV 第 7069 行 · ported_batch / 5817 · FortreeCity_House3_Text_MetStevenHadAmazingPokemon

判定：`fixed_verified`

理由：rare / 珍しい 指稀有。

日文：

```text
ポケモンずかんで\nおもいだした　ことが　あるよ\pめずらしい　いしを　さがしてるとき\nダイゴって　トレーナーと　であったけど\lあいつの　ポケモン　すごいね！\pめずらしい　だけでなく\nおそろしいほど　きたえられてた！\pもしかしたら　この　まちの\nジムリーダーよりも　つよいかも⋯⋯$
```

英文：

```text
While speaking about POKéDEXES,\nI remembered something.\pI met this TRAINER, STEVEN, when\nI was searching for rare stones.\pHoo, boy, he had some amazing POKéMON\nwith him.\pThey weren't just rare, they were\ntrained to terrifying extremes!\pHe might even be stronger than the\nGYM LEADER in this town…$
```

报告原中文：

```text
说到宝可梦图鉴，\n我想起来了，\p我寻找稀有石头的时候\n遇到了那个叫大吾的训练家。\p哈，他带着一些\n奇妙的宝可梦，\p它们不止是强大，\n还在训练中发挥到了极致！\p他也许比这城镇的\n道馆馆主还要强……$
```

修复前实际中文：

```text
说到宝可梦图鉴，
我想起来了，\p我寻找稀有石头的时候
遇到了那个叫大吾的训练家。\p哈，他带着一些
奇妙的宝可梦，\p它们不止是强大，
还在训练中发挥到了极致！\p他也许比这城镇的
道馆馆主还要强……
```

最终中文：

```text
说到宝可梦图鉴，
我想起来了，\p我寻找稀有石头的时候
遇到了那个叫大吾的训练家。\p哈，他带着一些
奇妙的宝可梦，\p它们不止是稀有，
还在训练中发挥到了极致！\p他也许比这城镇的
道馆馆主还要强……
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/FortreeCity_House3/scripts.inc",
        "text": "说到宝可梦图鉴，\n我想起来了，\\p我寻找稀有石头的时候\n遇到了那个叫大吾的训练家。\\p哈，他带着一些\n奇妙的宝可梦，\\p它们不止是稀有，\n还在训练中发挥到了极致！\\p他也许比这城镇的\n道馆馆主还要强……$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/FortreeCity_House3/scripts.inc",
        "text": "ポケモンずかんで\nおもいだした　ことが　あるよ\\pめずらしい　いしを　さがしてるとき\nダイゴって　トレーナーと　であったけど\\lあいつの　ポケモン　すごいね！\\pめずらしい　だけでなく\nおそろしいほど　きたえられてた！\\pもしかしたら　この　まちの\nジムリーダーよりも　つよいかも⋯⋯$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_FortreeCity_House3_Text_MetStevenHadAmazingPokemon",
      "file": "patch/batches/245_fortree_city_house3.json",
      "payload_address": "0x09052C6C",
      "payload_sha256": "4165f7c1761354bfda95cd4dcc8f65d8358b95193fa2093f8cd7a8b658bbcdad",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082050D3",
          "original": "0x082050E3",
          "target": "0x09052C6C",
          "batch": "patch/batches/245_fortree_city_house3.json"
        }
      ]
    }
  ]
}
```

### CSV 第 7096 行 · ported_batch / 5844 · LilycoveCity_MoveDeletersHouse_Text_ICanMakeMonForgetMove

判定：`fixed_verified`

理由：删除无依据的失忆长段，恢复能让宝可梦忘记招式及询问。

日文：

```text
えーと⋯⋯\nそうじゃ　わし　わすれじいさん\pポケモンの　わざを\nわすれさせる　ことが　できるんじゃ！\pわざを　わすれ　させるかね？$
```

英文：

```text
Uh…\nOh, yes, I'm the MOVE DELETER.\pI can make POKéMON forget their moves.\pWould you like me to do that?$
```

报告原中文：

```text
那个……\n俺是谁来着？\p…… …… ……\n…… …… ……\p哦哦，对了！\n俺是遗忘爷爷哩！\p你是来让宝可梦\n忘记招式的呐？$
```

修复前实际中文：

```text
那个……
俺是谁来着？\p…… …… ……
…… …… ……\p哦哦，对了！
俺是遗忘爷爷哩！\p你是来让宝可梦
忘记招式的呐？
```

最终中文：

```text
那个……
哦，对了！俺是遗忘爷爷哩！\p俺能让宝可梦
忘记招式。\p你想让俺帮忙吗？
```

证据：

```json
{
  "review": {
    "row_number": 7096,
    "symbol": "LilycoveCity_MoveDeletersHouse_Text_ICanMakeMonForgetMove",
    "domain": "ported_batch",
    "idx": "5844",
    "old": null,
    "new": "那个……\n哦，对了！俺是遗忘爷爷哩！\\p俺能让宝可梦\n忘记招式。\\p你想让俺帮忙吗？$",
    "reason": "删除无依据的失忆长段，恢复能让宝可梦忘记招式及询问。",
    "scope": "both",
    "action": "fix",
    "final_text": "那个……\n哦，对了！俺是遗忘爷爷哩！\\p俺能让宝可梦\n忘记招式。\\p你想让俺帮忙吗？",
    "old_current_text": "那个……\n俺是谁来着？\\p…… …… ……\n…… …… ……\\p哦哦，对了！\n俺是遗忘爷爷哩！\\p你是来让宝可梦\n忘记招式的呐？",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/LilycoveCity_MoveDeletersHouse/scripts.inc",
      "patch/batches/259_lilycove_city_move_deleters_house.json"
    ],
    "us_source_file": "data/maps/LilycoveCity_MoveDeletersHouse/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/LilycoveCity_MoveDeletersHouse/scripts.inc",
        "text": "えーと⋯⋯\nそうじゃ　わし　わすれじいさん\\pポケモンの　わざを\nわすれさせる　ことが　できるんじゃ！\\pわざを　わすれ　させるかね？$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/LilycoveCity_MoveDeletersHouse/scripts.inc",
        "text": "那个……\n哦，对了！俺是遗忘爷爷哩！\\p俺能让宝可梦\n忘记招式。\\p你想让俺帮忙吗？$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/LilycoveCity_MoveDeletersHouse/scripts.inc",
        "text": "えーと⋯⋯\nそうじゃ　わし　わすれじいさん\\pポケモンの　わざを\nわすれさせる　ことが　できるんじゃ！\\pわざを　わすれ　させるかね？$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_LilycoveCity_MoveDeletersHouse_Text_ICanMakeMonForgetMove",
      "file": "patch/batches/259_lilycove_city_move_deleters_house.json",
      "payload_address": "0x090532F4",
      "payload_sha256": "bef86f4eb7f0830de37df928c10dcd69ab3d377a0cad9598a700f37c473c16c7",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08209D7E",
          "original": "0x08209E63",
          "target": "0x090532F4",
          "batch": "patch/batches/259_lilycove_city_move_deleters_house.json"
        }
      ]
    }
  ]
}
```

### CSV 第 7183 行 · ported_batch / 5931 · RustboroCity_House3_Text_NamingPikachuPekachu

判定：`localization_choice`

理由：PEKACHU是日美昵称双关；猫卡球是本地化昵称，并非写入存档的种族名错误；不强行音译。

日文：

```text
だからって　ピカチュウに\n‘ペカチュウ’って　つけても\lほとんど　かわって　ないでしょうに⋯⋯\pまあ　わかりやすいのも\nニックネームには　だいじ　ですけどねぇ$
```

英文：

```text
But giving the name PEKACHU to\na PIKACHU? It seems pointless.\pI suppose it is good to use a name\nthat's easy to understand, but…$
```

报告原中文：

```text
但叫皮卡丘为\n猫卡球？这没什么意义。\p我想最好起个容易\n让人理解的名字，但是……$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 7183,
    "symbol": "RustboroCity_House3_Text_NamingPikachuPekachu",
    "domain": "ported_batch",
    "idx": "5931",
    "reason": "PEKACHU是日美昵称双关；猫卡球是本地化昵称，并非写入存档的种族名错误；不强行音译。",
    "action": "localization_choice"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/RustboroCity_House3/scripts.inc",
        "text": "但叫皮卡丘为\n猫卡球？这没什么意义。\\p我想最好起个容易\n让人理解的名字，但是……$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/RustboroCity_House3/scripts.inc",
        "text": "だからって　ピカチュウに\n‘ペカチュウ’って　つけても\\lほとんど　かわって　ないでしょうに⋯⋯\\pまあ　わかりやすいのも\nニックネームには　だいじ　ですけどねぇ$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_RustboroCity_House3_Text_NamingPikachuPekachu",
      "file": "patch/batches/299_rustboro_city_house3.json",
      "payload_address": "0x0905470D",
      "payload_sha256": "cc8ae0eccb9cd644a7a0ba78c48a50eec6b3202377fcecac9ad4ed5688a01fd2",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08204123",
          "original": "0x0820416F",
          "target": "0x0905470D",
          "batch": "patch/batches/299_rustboro_city_house3.json"
        }
      ]
    }
  ]
}
```

### CSV 第 7184 行 · ported_batch / 5932 · RustboroCity_House3_Text_Pekachu

判定：`localization_choice`

理由：与前条猫卡球昵称/叫声成套的本地化，不能单条按种族名修正。

日文：

```text
ペカチュウ“ぺかー！$
```

英文：

```text
PEKACHU: Peka!$
```

报告原中文：

```text
猫卡球：猫球！$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 7184,
    "symbol": "RustboroCity_House3_Text_Pekachu",
    "domain": "ported_batch",
    "idx": "5932",
    "reason": "与前条猫卡球昵称/叫声成套的本地化，不能单条按种族名修正。",
    "action": "localization_choice"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/RustboroCity_House3/scripts.inc",
        "text": "猫卡球：猫球！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/RustboroCity_House3/scripts.inc",
        "text": "ペカチュウ“ぺかー！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_RustboroCity_House3_Text_Pekachu",
      "file": "patch/batches/299_rustboro_city_house3.json",
      "payload_address": "0x0905475B",
      "payload_sha256": "c6c339e012ebeebf3904e542b49d32705cc2b131b8494cff0fef8a31b0ccc078",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08204134",
          "original": "0x082041BF",
          "target": "0x0905475B",
          "batch": "patch/batches/299_rustboro_city_house3.json"
        }
      ]
    }
  ]
}
```

### CSV 第 7288 行 · ported_batch / 6036 · SootopolisCity_Text_WonderWhatWorldIsLike

判定：`fixed_verified`

理由：JPまあるい / EN round 指圆形；圆椭不成词。

日文：

```text
ぼく……　まだ　いちども　このまちから\nそとに　でたこと　ないんだ\pあの　まあるい　そらの　むこうには\nどんな　せかいが　あるのかな?
```

英文：

```text
I… I've never been out of this city.\pI wonder what the world is like on
the other side of this round sky?$
```

报告原中文：

```text
{FC_ENG}我……我从未离开过这座城。\p不知这圆椭的天空的\n另一端会有什么呢？$
```

修复前实际中文：

```text
我……我从未离开过这座城。\p不知这圆椭的天空的
另一端会有什么呢？
```

最终中文：

```text
我……我从未离开过这座城。\p不知这圆形的天空的
另一端会有什么呢？
```

证据：

```json
{
  "review": {
    "row_number": 7288,
    "symbol": "SootopolisCity_Text_WonderWhatWorldIsLike",
    "domain": "ported_batch",
    "idx": "6036",
    "old": "圆椭的天空",
    "new": "圆形的天空",
    "reason": "JPまあるい / EN round 指圆形；圆椭不成词。",
    "scope": "both",
    "action": "fix",
    "final_text": "我……我从未离开过这座城。\\p不知这圆形的天空的\n另一端会有什么呢？",
    "old_current_text": "我……我从未离开过这座城。\\p不知这圆椭的天空的\n另一端会有什么呢？",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/SootopolisCity/scripts.inc",
      "patch/batches/316_sootopolis_city.json"
    ],
    "us_source_file": "data/maps/SootopolisCity/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/SootopolisCity/scripts.inc",
        "text": "ぼく⋯⋯　まだ　いちども　このまちから\nそとに　でたこと　ないんだ\\pあの　まあるい　そらの　むこうには\nどんな　せかいが　あるのかな？$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/SootopolisCity/scripts.inc",
        "text": "我……我从未离开过这座城。\\p不知这圆形的天空的\n另一端会有什么呢？$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/SootopolisCity/scripts.inc",
        "text": "ぼく⋯⋯　まだ　いちども　このまちから\nそとに　でたこと　ないんだ\\pあの　まあるい　そらの　むこうには\nどんな　せかいが　あるのかな？$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_SootopolisCity_Text_WonderWhatWorldIsLike",
      "file": "patch/batches/316_sootopolis_city.json",
      "payload_address": "0x09055F36",
      "payload_sha256": "4f588a94f122a90c6af8d81f49ddbd32aca73e3aa9871fdaf5dd361db4ed7685",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x081E276B",
          "original": "0x081E2DD3",
          "target": "0x09055F36",
          "batch": "patch/batches/316_sootopolis_city.json"
        }
      ]
    }
  ]
}
```

### CSV 第 7478 行 · ported_batch / 6226 · VictoryRoad_B1F_Text_MitchellIntro

判定：`fixed_verified`

理由：原文赞叹宝可梦本身，而非士气。

日文：

```text
わたしの　ポケモンは　すばらしいですよ!
```

英文：

```text
My POKéMON are cosmically
awe inspiring!$
```

报告原中文：

```text
{FC_ENG}我的宝可梦的士气已经\n达到了顶点！$
```

修复前实际中文：

```text
我的宝可梦的士气已经
达到了顶点！
```

最终中文：

```text
我的宝可梦
真是令人惊叹！
```

证据：

```json
{
  "review": {
    "row_number": 7478,
    "symbol": "VictoryRoad_B1F_Text_MitchellIntro",
    "domain": "ported_batch",
    "idx": "6226",
    "old": "我的宝可梦的士气已经\n达到了顶点！",
    "new": "我的宝可梦\n真是令人惊叹！",
    "reason": "原文赞叹宝可梦本身，而非士气。",
    "scope": "both",
    "action": "fix",
    "final_text": "我的宝可梦\n真是令人惊叹！",
    "old_current_text": "我的宝可梦的士气已经\n达到了顶点！",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/VictoryRoad_B1F/scripts.inc",
      "patch/batches/336_victory_road_b1_f.json"
    ],
    "us_source_file": "data/maps/VictoryRoad_B1F/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/VictoryRoad_B1F/scripts.inc",
        "text": "わたしの　ポケモンは　すばらしいですよ！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/VictoryRoad_B1F/scripts.inc",
        "text": "我的宝可梦\n真是令人惊叹！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/VictoryRoad_B1F/scripts.inc",
        "text": "わたしの　ポケモンは　すばらしいですよ！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_VictoryRoad_B1F_Text_MitchellIntro",
      "file": "patch/batches/336_victory_road_b1_f.json",
      "payload_address": "0x09059110",
      "payload_sha256": "82ec9b33f35a1e686d210533c906de2d771c342cb657a5875ad56864ece7fa0f",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082199BA",
          "original": "0x08219AF4",
          "target": "0x09059110",
          "batch": "patch/batches/336_victory_road_b1_f.json"
        }
      ]
    }
  ]
}
```

### CSV 第 7558 行 · ported_batch / 6306 · MoveTutor_Text_SubstituteTeach

判定：`fixed_verified`

理由：重复如果。

日文：

```text
ふう\nこうやって　おくじょうから\lひろい　せかいを　みていると……\pなんにんもの　じぶんが　いて\nいくつもの　じんせいを　たのしめたらな-\lって　おもうの!\lムリな　はなしだけどね　うふふ\pそうだわ　あなたの　ポケモンちゃん!\nみがわりの　わざ　おぼえてみない?
```

英文：

```text
When I see the wide world from up
here on the roof…\pI think about how nice it would be
if there were more than just one me\lso I could enjoy all sorts of lives.\pOf course it's not possible.
Giggle…\pI know! Would you be interested in
having a POKéMON learn SUBSTITUTE?$
```

报告原中文：

```text
{FC_ENG}当我在屋顶上看着\n这广阔的世界时……\p我在想如果这个世界如果\n有不止一个自己该多有趣啊，\l那样我就能体验各种各样的人生了。\p当然这是不可能的。\n嘿嘿……\p明白了！\n不如让你的宝可梦学习替身吧？$
```

修复前实际中文：

```text
当我在屋顶上看着
这广阔的世界时……\p我在想如果这个世界如果
有不止一个自己该多有趣啊，\l那样我就能体验各种各样的人生了。\p当然这是不可能的。
嘿嘿……\p明白了！
不如让你的宝可梦学习替身吧？
```

最终中文：

```text
当我在屋顶上看着
这广阔的世界时……\p我在想如果这个世界
有不止一个自己该多有趣啊，\l那样我就能体验各种各样的人生了。\p当然这是不可能的。
嘿嘿……\p明白了！
不如让你的宝可梦学习替身吧？
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/move_tutors.inc",
        "text": "当我在屋顶上看着\n这广阔的世界时……\\p我在想如果这个世界\n有不止一个自己该多有趣啊，\\l那样我就能体验各种各样的人生了。\\p当然这是不可能的。\n嘿嘿……\\p明白了！\n不如让你的宝可梦学习替身吧？$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/move_tutors.inc",
        "text": "ふう\nこうやって　おくじょうから\\lひろい　せかいを　みていると⋯⋯\\pなんにんもの　じぶんが　いて\nいくつもの　じんせいを　たのしめたらなー\\lって　おもうの！\\lムリな　はなしだけどね　うふふ\\pそうだわ　あなたの　ポケモンちゃん！\nみがわりの　わざ　おぼえてみない？$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_MoveTutor_Text_SubstituteTeach",
      "file": "patch/batches/340_move_tutors.json",
      "payload_address": "0x0905A133",
      "payload_sha256": "d705f69af85617ac31c1b269b5244a67dca72e4bebf31e226cd7f5ab40541a61",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08276AAF",
          "original": "0x08276436",
          "target": "0x0905A133",
          "batch": "patch/batches/340_move_tutors.json"
        }
      ]
    }
  ]
}
```

### CSV 第 7635 行 · ported_batch / 6383 · Text_MonUsedStrength

判定：`equivalent_wording`

理由：前句已提供宝可梦名，后句省略同一主语不丢失语义；无需重复占位符。

日文：

```text
{FD:02}　は\nかいりきを　はっきした!\p{FD:02}の　かいりきの　おかげで\nいわを　おせるように　なった!
```

英文：

```text
{STR_VAR_1} used STRENGTH!\p{STR_VAR_1}'s STRENGTH made it
possible to move boulders around!$
```

报告原中文：

```text
{FC_ENG}{FC_JPN}{STR_VAR_1}{FC_ENG}使出了怪力！\p使出了怪力后，\n可以推动岩石了！$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 7635,
    "symbol": "Text_MonUsedStrength",
    "domain": "ported_batch",
    "idx": "6383",
    "reason": "前句已提供宝可梦名，后句省略同一主语不丢失语义；无需重复占位符。",
    "action": "equivalent_wording"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/scripts/field_move_scripts.inc",
        "text": "{STR_VAR_1}使出了怪力！\\p使出了怪力后，\n可以推动岩石了！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/scripts/field_move_scripts.inc",
        "text": "{STR_VAR_1}　は\nかいりきを　はっきした！\\p{STR_VAR_1}の　かいりきの　おかげで\nいわを　おせるように　なった！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Text_MonUsedStrength",
      "file": "patch/batches/342_field_move_scripts_scripts.json",
      "payload_address": "0x0905B2A5",
      "payload_sha256": "92e175ec4b8641e379c2fbacdf4b4dc66889fa369bd9f7a705c642ed63a7ee7e",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082567A7",
          "original": "0x082567F3",
          "target": "0x0905B2A5",
          "batch": "patch/batches/342_field_move_scripts_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 7886 行 · ported_batch / 6634 · MatchCall_BattleFrontierStreakText3

判定：`fixed_verified`

理由：big record不等于new record。

日文：

```text
おう!　{FD:01}!\n{FD:02}だぞ!\p{FD:03}　で\nおおあばれ　したらしいな!\p{FD:04}れんしょう　って\nすごい　きろく　なんだろ?\pおれも　まけられね-な!\nじゃ　またな!
```

英文：

```text
Hey there, {PLAYER}!
It's me, {STR_VAR_1}.\pI heard you went on a tear at
the {STR_VAR_2}!\pA big {STR_VAR_3}-win streak…
That is a big record, isn't it?\pI'd better get it together, too!
Catch you soon!$
```

报告原中文：

```text
{FC_ENG}喂你好，{FC_JPN}{PLAYER}{FC_ENG}！\n是我，{FC_JPN}{STR_VAR_1}{FC_ENG}。\p我听说你在{FC_JPN}{STR_VAR_2}{FC_ENG}\n势不可挡！\p一个漂亮的{FC_JPN}{STR_VAR_3}{FC_ENG}连胜……\n这是个新纪录，对吧？\p我也要努力了！\n以后联系！$
```

修复前实际中文：

```text
喂你好，{PLAYER}！
是我，{STR_VAR_1}。\p我听说你在{STR_VAR_2}
势不可挡！\p一个漂亮的{STR_VAR_3}连胜……
这是个新纪录，对吧？\p我也要努力了！
以后联系！
```

最终中文：

```text
喂你好，{PLAYER}！
是我，{STR_VAR_1}。\p我听说你在{STR_VAR_2}
势不可挡！\p一个漂亮的{STR_VAR_3}连胜……
这纪录很了不起，对吧？\p我也要努力了！
以后联系！
```

证据：

```json
{
  "review": {
    "row_number": 7886,
    "symbol": "MatchCall_BattleFrontierStreakText3",
    "domain": "ported_batch",
    "idx": "6634",
    "old": "这是个新纪录，对吧？",
    "new": "这纪录很了不起，对吧？",
    "reason": "big record不等于new record。",
    "scope": "both",
    "action": "fix",
    "final_text": "喂你好，{PLAYER}！\n是我，{STR_VAR_1}。\\p我听说你在{STR_VAR_2}\n势不可挡！\\p一个漂亮的{STR_VAR_3}连胜……\n这纪录很了不起，对吧？\\p我也要努力了！\n以后联系！",
    "old_current_text": "喂你好，{PLAYER}！\n是我，{STR_VAR_1}。\\p我听说你在{STR_VAR_2}\n势不可挡！\\p一个漂亮的{STR_VAR_3}连胜……\n这是个新纪录，对吧？\\p我也要努力了！\n以后联系！",
    "changed_files": [
      "../pokeemerald_us_chs/data/text/match_call.inc",
      "patch/batches/343_match_call.json"
    ],
    "us_source_file": "data/text/match_call.inc",
    "jp_source": [
      {
        "file": "data/text/match_call.inc",
        "text": "おう！　{PLAYER}！\n{STR_VAR_1}だぞ！\\p{STR_VAR_2}　で\nおおあばれ　したらしいな！\\p{STR_VAR_3}れんしょう　って\nすごい　きろく　なんだろ？\\pおれも　まけられねーな！\nじゃ　またな！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/match_call.inc",
        "text": "喂你好，{PLAYER}！\n是我，{STR_VAR_1}。\\p我听说你在{STR_VAR_2}\n势不可挡！\\p一个漂亮的{STR_VAR_3}连胜……\n这纪录很了不起，对吧？\\p我也要努力了！\n以后联系！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/match_call.inc",
        "text": "おう！　{PLAYER}！\n{STR_VAR_1}だぞ！\\p{STR_VAR_2}　で\nおおあばれ　したらしいな！\\p{STR_VAR_3}れんしょう　って\nすごい　きろく　なんだろ？\\pおれも　まけられねーな！\nじゃ　またな！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_MatchCall_BattleFrontierStreakText3",
      "file": "patch/batches/343_match_call.json",
      "payload_address": "0x09063489",
      "payload_sha256": "47943089f963e35fc5faec7652086fdd348e7ff31a23ac62c22064b91fd87da4",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085D727C",
          "original": "0x08268A4C",
          "target": "0x09063489",
          "batch": "patch/batches/343_match_call.json"
        }
      ]
    }
  ]
}
```

### CSV 第 7900 行 · ported_batch / 6648 · MatchCall_BattleFrontierRecordStreakText3

判定：`fixed_verified`

理由：big record不等于new record。

日文：

```text
おう!　{FD:01}!\n{FD:02}だぞ!\p{FD:03}　で\nおおあばれ　したらしいな!\p{FD:04}れんしょう　って\nすごい　きろく　なんだろ?\pおれも　まけられね-な!\nじゃ　またな!
```

英文：

```text
Hey there, {PLAYER}!
It's me, {STR_VAR_1}.\pI heard you went on a tear at
the {STR_VAR_2}!\pA big {STR_VAR_3}-win streak…
That is a big record, isn't it?\pI'd better get it together, too!
Catch you soon!$
```

报告原中文：

```text
{FC_ENG}喂你好，{FC_JPN}{PLAYER}{FC_ENG}！\n是我，{FC_JPN}{STR_VAR_1}{FC_ENG}。\p我听说你在{FC_JPN}{STR_VAR_2}{FC_ENG}\n势不可挡！\p一个漂亮的{FC_JPN}{STR_VAR_3}{FC_ENG}连胜……\n这是个新纪录，对吧？\p我也要努力了！\n以后联系！$
```

修复前实际中文：

```text
喂你好，{PLAYER}！
是我，{STR_VAR_1}。\p我听说你在{STR_VAR_2}
势不可挡！\p一个漂亮的{STR_VAR_3}连胜……
这是个新纪录，对吧？\p我也要努力了！
以后联系！
```

最终中文：

```text
喂你好，{PLAYER}！
是我，{STR_VAR_1}。\p我听说你在{STR_VAR_2}
势不可挡！\p一个漂亮的{STR_VAR_3}连胜……
这纪录很了不起，对吧？\p我也要努力了！
以后联系！
```

证据：

```json
{
  "review": {
    "row_number": 7900,
    "symbol": "MatchCall_BattleFrontierRecordStreakText3",
    "domain": "ported_batch",
    "idx": "6648",
    "old": "这是个新纪录，对吧？",
    "new": "这纪录很了不起，对吧？",
    "reason": "big record不等于new record。",
    "scope": "both",
    "action": "fix",
    "final_text": "喂你好，{PLAYER}！\n是我，{STR_VAR_1}。\\p我听说你在{STR_VAR_2}\n势不可挡！\\p一个漂亮的{STR_VAR_3}连胜……\n这纪录很了不起，对吧？\\p我也要努力了！\n以后联系！",
    "old_current_text": "喂你好，{PLAYER}！\n是我，{STR_VAR_1}。\\p我听说你在{STR_VAR_2}\n势不可挡！\\p一个漂亮的{STR_VAR_3}连胜……\n这是个新纪录，对吧？\\p我也要努力了！\n以后联系！",
    "changed_files": [
      "../pokeemerald_us_chs/data/text/match_call.inc",
      "patch/batches/343_match_call.json"
    ],
    "us_source_file": "data/text/match_call.inc",
    "jp_source": [
      {
        "file": "data/text/match_call.inc",
        "text": "おう！　{PLAYER}！\n{STR_VAR_1}だぞ！\\p{STR_VAR_2}　で\nおおあばれ　したらしいな！\\p{STR_VAR_3}れんしょう　って\nすごい　きろく　なんだろ？\\pおれも　まけられねーな！\nじゃ　またな！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/match_call.inc",
        "text": "喂你好，{PLAYER}！\n是我，{STR_VAR_1}。\\p我听说你在{STR_VAR_2}\n势不可挡！\\p一个漂亮的{STR_VAR_3}连胜……\n这纪录很了不起，对吧？\\p我也要努力了！\n以后联系！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/match_call.inc",
        "text": "おう！　{PLAYER}！\n{STR_VAR_1}だぞ！\\p{STR_VAR_2}　で\nおおあばれ　したらしいな！\\p{STR_VAR_3}れんしょう　って\nすごい　きろく　なんだろ？\\pおれも　まけられねーな！\nじゃ　またな！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_MatchCall_BattleFrontierRecordStreakText3",
      "file": "patch/batches/343_match_call.json",
      "payload_address": "0x09063AFD",
      "payload_sha256": "47943089f963e35fc5faec7652086fdd348e7ff31a23ac62c22064b91fd87da4",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085D72EC",
          "original": "0x08268E48",
          "target": "0x09063AFD",
          "batch": "patch/batches/343_match_call.json"
        }
      ]
    }
  ]
}
```

### CSV 第 8076 行 · ported_batch / 6824 · CableClub_Text_UnionRoomInfo

判定：`fixed_verified`

理由：恢复up to限定且明确包含30级。

日文：

```text
ユニオン　ル-ム　は　あなたの\nちかくで　ユニオン　ル-ムに\lはいっている　ひとが　あらわれます\pかんたんな　あいさつをしたり\pレベル30までの　ポケモン2ひきで\n1たい1の　たいせん\p2にんから　5にんまで　どうじに\nおしゃべりが　できる　チャット\pそして　とうろくしき\nポケモン　こうかんが　たのしめます\pへやに　はいりますか?
```

英文：

```text
The TRAINERS in the UNION ROOM
will be those players around you\lwho have also entered the ROOM.\pYou may do all sorts of things
here, such as exchanging greetings.\pYou may enter two POKéMON up to
Lv. 30 for a one-on-one battle.\pYou may take part in a chat with
two to five people.\pOr, you may register a POKéMON for
trade.\pWould you like to enter the ROOM?$
```

报告原中文：

```text
{FC_ENG}联盟交谊厅的训练家都是在您周围\n并且也进入了联盟交谊厅的玩家。\p你可以在这里做各种事情，\n比如互相问候。\p您可以拿出2只等级30的\n宝可梦进行1对1的对战。\p您也可以和2到5个人\n在这里进行聊天。\p或者您也可以登记宝可梦\n进行交换。\p要进入房间吗？$
```

修复前实际中文：

```text
联盟交谊厅的训练家都是在您周围
并且也进入了联盟交谊厅的玩家。\p你可以在这里做各种事情，
比如互相问候。\p您可以拿出2只等级30的
宝可梦进行1对1的对战。\p您也可以和2到5个人
在这里进行聊天。\p或者您也可以登记宝可梦
进行交换。\p要进入房间吗？
```

最终中文：

```text
联盟交谊厅的训练家都是在您周围
并且也进入了联盟交谊厅的玩家。\p你可以在这里做各种事情，
比如互相问候。\p您可以拿出2只不超过30级的
宝可梦进行1对1的对战。\p您也可以和2到5个人
在这里进行聊天。\p或者您也可以登记宝可梦
进行交换。\p要进入房间吗？
```

证据：

```json
{
  "review": {
    "row_number": 8076,
    "symbol": "CableClub_Text_UnionRoomInfo",
    "domain": "ported_batch",
    "idx": "6824",
    "old": "2只等级30的\n宝可梦",
    "new": "2只不超过30级的\n宝可梦",
    "reason": "恢复up to限定且明确包含30级。",
    "scope": "both",
    "action": "fix",
    "final_text": "联盟交谊厅的训练家都是在您周围\n并且也进入了联盟交谊厅的玩家。\\p你可以在这里做各种事情，\n比如互相问候。\\p您可以拿出2只不超过30级的\n宝可梦进行1对1的对战。\\p您也可以和2到5个人\n在这里进行聊天。\\p或者您也可以登记宝可梦\n进行交换。\\p要进入房间吗？",
    "old_current_text": "联盟交谊厅的训练家都是在您周围\n并且也进入了联盟交谊厅的玩家。\\p你可以在这里做各种事情，\n比如互相问候。\\p您可以拿出2只等级30的\n宝可梦进行1对1的对战。\\p您也可以和2到5个人\n在这里进行聊天。\\p或者您也可以登记宝可梦\n进行交换。\\p要进入房间吗？",
    "changed_files": [
      "../pokeemerald_us_chs/data/text/cable_club.inc",
      "patch/batches/359_cable_club.json"
    ],
    "us_source_file": "data/text/cable_club.inc",
    "jp_source": [
      {
        "file": "data/text/cable_club.inc",
        "text": "ユニオン　ルーム　は　あなたの\nちかくで　ユニオン　ルームに\\lはいっている　ひとが　あらわれます\\pかんたんな　あいさつをしたり\\pレベル30までの　ポケモン2ひきで\n1たい1の　たいせん\\p2にんから　5にんまで　どうじに\nおしゃべりが　できる　チャット\\pそして　とうろくしき\nポケモン　こうかんが　たのしめます\\pへやに　はいりますか？$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/cable_club.inc",
        "text": "联盟交谊厅的训练家都是在您周围\n并且也进入了联盟交谊厅的玩家。\\p你可以在这里做各种事情，\n比如互相问候。\\p您可以拿出2只不超过30级的\n宝可梦进行1对1的对战。\\p您也可以和2到5个人\n在这里进行聊天。\\p或者您也可以登记宝可梦\n进行交换。\\p要进入房间吗？$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/cable_club.inc",
        "text": "ユニオン　ルーム　は　あなたの\nちかくで　ユニオン　ルームに\\lはいっている　ひとが　あらわれます\\pかんたんな　あいさつをしたり\\pレベル30までの　ポケモン2ひきで\n1たい1の　たいせん\\p2にんから　5にんまで　どうじに\nおしゃべりが　できる　チャット\\pそして　とうろくしき\nポケモン　こうかんが　たのしめます\\pへやに　はいりますか？$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_CableClub_Text_UnionRoomInfo",
      "file": "patch/batches/359_cable_club.json",
      "payload_address": "0x09066E64",
      "payload_sha256": "3113ce51f6e827df61a5dea7ede6f10b725e01aa0c88c43874d7a7513f373201",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08247273",
          "original": "0x082486D6",
          "target": "0x09066E64",
          "batch": "patch/batches/359_cable_club.json"
        }
      ]
    }
  ]
}
```

### CSV 第 8199 行 · ported_batch / 6947 · Route108_Text_MatthewPostBattle

判定：`fixed_verified`

理由：删除重复指示词。

日文：

```text
すてられぶねの　なかに\nはいっていく　やつらが　いるんだよ!
```

英文：

```text
Some people even go inside that
ABANDONED SHIP.$
```

报告原中文：

```text
{FC_ENG}有些人甚至走进了那个\n那艘废弃的船。$
```

修复前实际中文：

```text
有些人甚至走进了那个
那艘废弃的船。
```

最终中文：

```text
有些人甚至会进入
那艘废弃的船。
```

证据：

```json
{
  "review": {
    "row_number": 8199,
    "symbol": "Route108_Text_MatthewPostBattle",
    "domain": "ported_batch",
    "idx": "6947",
    "old": "有些人甚至走进了那个\n那艘废弃的船。",
    "new": "有些人甚至会进入\n那艘废弃的船。",
    "reason": "删除重复指示词。",
    "scope": "both",
    "action": "fix",
    "final_text": "有些人甚至会进入\n那艘废弃的船。",
    "old_current_text": "有些人甚至走进了那个\n那艘废弃的船。",
    "changed_files": [
      "../pokeemerald_us_chs/data/text/trainers.inc",
      "patch/batches/372_trainer_quotes_01.json"
    ],
    "us_source_file": "data/text/trainers.inc",
    "jp_source": [
      {
        "file": "data/text/trainers.inc",
        "text": "すてられぶねの　なかに\nはいっていく　やつらが　いるんだよ！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/trainers.inc",
        "text": "有些人甚至会进入\n那艘废弃的船。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/trainers.inc",
        "text": "すてられぶねの　なかに\nはいっていく　やつらが　いるんだよ！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Route108_Text_MatthewPostBattle",
      "file": "patch/batches/372_trainer_quotes_01.json",
      "payload_address": "0x090688AE",
      "payload_sha256": "c5e7a6e3f147b4ae9e3b2dae25afbdb595b0612d540275cbb3dcf5a18ba92943",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x081E85C8",
          "original": "0x0825ABFF",
          "target": "0x090688AE",
          "batch": "patch/batches/372_trainer_quotes_01.json"
        }
      ]
    }
  ]
}
```

### CSV 第 8613 行 · ported_batch / 7361 · gText_ApprenticeWhichMove14

判定：`fixed_verified`

理由：报告理由用错感谢模板；实际咨询日英原文也无本句，删除跨条串入句子。

日文：

```text
あ……　あ……\n{FD:01}{FD:05}　だよね?\lそ　そんなに　みないで　くれよ!\lてれるだろ\lまた……　そうだん　させて　くれよ\pは　はずかしながらさ\nポケモンに　おしえる　わざがさ\lきまんないんだ　アドバイス　くれよ!\pポケモンは　{FD:02}なんだ\nだったら　どっちが　いい　かな……?\n{FD:03}……　{FD:04}……
```

英文：

```text
Er… Um…
{PLAYER}{KUN}…?\pPlease, don't look at me that way.
I'm getting all flustered…\lI… I need your advice.\pI… I'm really embarrassed, but I can't
decide what move I should teach\lmy POKéMON.\pIt's for my {STR_VAR_1}.
If the choices were {STR_VAR_2} or\l{STR_VAR_3}, which would be better?$
```

报告原中文：

```text
{FC_ENG}呃……嗯……\n{FC_JPN}{PLAYER}{FC_ENG}{FC_JPN}{KUN}{FC_ENG}……？\p拜托，别那样看着我。\p我很紧张……\p我……我再次需要你的建议。\p虽然这是我最后一次……\p真的很不好意思问，\p对我的{FC_JPN}{STR_VAR_1}{FC_ENG}而言，\n{FC_JPN}{STR_VAR_2}{FC_ENG}和{FC_JPN}{STR_VAR_3}{FC_ENG}哪个更好？$
```

修复前实际中文：

```text
呃……嗯……
{PLAYER}{KUN}……？\p拜托，别那样看着我。\p我很紧张……\p我……我再次需要你的建议。\p虽然这是我最后一次……\p真的很不好意思问，\p对我的{STR_VAR_1}而言，
{STR_VAR_2}和{STR_VAR_3}哪个更好？
```

最终中文：

```text
呃……嗯……
{PLAYER}{KUN}……？\p拜托，别那样看着我。\p我很紧张……\p我……我再次需要你的建议。\p真的很不好意思问，\p对我的{STR_VAR_1}而言，
{STR_VAR_2}和{STR_VAR_3}哪个更好？
```

证据：

```json
{
  "review": {
    "row_number": 8613,
    "symbol": "gText_ApprenticeWhichMove14",
    "domain": "ported_batch",
    "idx": "7361",
    "old": "虽然这是我最后一次……\\p",
    "new": "",
    "reason": "报告理由用错感谢模板；实际咨询日英原文也无本句，删除跨条串入句子。",
    "scope": "both",
    "action": "fix",
    "final_text": "呃……嗯……\n{PLAYER}{KUN}……？\\p拜托，别那样看着我。\\p我很紧张……\\p我……我再次需要你的建议。\\p真的很不好意思问，\\p对我的{STR_VAR_1}而言，\n{STR_VAR_2}和{STR_VAR_3}哪个更好？",
    "old_current_text": "呃……嗯……\n{PLAYER}{KUN}……？\\p拜托，别那样看着我。\\p我很紧张……\\p我……我再次需要你的建议。\\p虽然这是我最后一次……\\p真的很不好意思问，\\p对我的{STR_VAR_1}而言，\n{STR_VAR_2}和{STR_VAR_3}哪个更好？",
    "changed_files": [
      "../pokeemerald_us_chs/data/text/apprentice.inc",
      "patch/batches/383_apprentice_0.json"
    ],
    "us_source_file": "data/text/apprentice.inc",
    "jp_source": [
      {
        "file": "data/text/apprentice.inc",
        "text": "あ⋯⋯　あ⋯⋯\n{PLAYER}{KUN}　だよね？\\lそ　そんなに　みないで　くれよ！\\lてれるだろ\\lまた⋯⋯　そうだん　させて　くれよ\\pは　はずかしながらさ\nポケモンに　おしえる　わざがさ\\lきまんないんだ　アドバイス　くれよ！\\pポケモンは　{STR_VAR_1}なんだ\nだったら　どっちが　いい　かな⋯⋯？\n{STR_VAR_2}⋯⋯　{STR_VAR_3}⋯⋯$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/apprentice.inc",
        "text": "呃……嗯……\n{PLAYER}{KUN}……？\\p拜托，别那样看着我。\\p我很紧张……\\p我……我再次需要你的建议。\\p真的很不好意思问，\\p对我的{STR_VAR_1}而言，\n{STR_VAR_2}和{STR_VAR_3}哪个更好？$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/apprentice.inc",
        "text": "あ⋯⋯　あ⋯⋯\n{PLAYER}{KUN}　だよね？\\lそ　そんなに　みないで　くれよ！\\lてれるだろ\\lまた⋯⋯　そうだん　させて　くれよ\\pは　はずかしながらさ\nポケモンに　おしえる　わざがさ\\lきまんないんだ　アドバイス　くれよ！\\pポケモンは　{STR_VAR_1}なんだ\nだったら　どっちが　いい　かな⋯⋯？\n{STR_VAR_2}⋯⋯　{STR_VAR_3}⋯⋯$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_ApprenticeWhichMove14",
      "file": "patch/batches/383_apprentice_0.json",
      "payload_address": "0x090717C7",
      "payload_sha256": "f0038e7a478a8b33182243ce1d262190189923f3a6d921316aeba1f0dbbc958c",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085DC84C",
          "original": "0x082724FC",
          "target": "0x090717C7",
          "batch": "patch/batches/383_apprentice_0.json"
        }
      ]
    }
  ]
}
```

### CSV 第 8626 行 · ported_batch / 7374 · gText_ApprenticeWinSpeechThanks9

判定：`fixed_verified`

理由：恢复JPババーっと爽快说出的语气，避免无意义食物直译。

日文：

```text
{FD:02}\pあはぁ　それいいね\nオ-ケイ　オ-ケイ!\lおじさん　ババ-っと　いってみるよ!\pそれじゃあ　おわかれだ!\nいままで　いろいろ　ありがとうね\lいつか　しょうぶも　してくれよ!\pアディオ-ス!
```

英文：

```text
{STR_VAR_1}\pUh-huh, that's sweet!
Si, bueno!\lI'll try saying that, like, ham!\pAnd now, it's time to say good-bye!
Thanks for all sorts of things!\pGive me a battle one day, OK?
Adios!$
```

报告原中文：

```text
{FC_ENG}{FC_JPN}{STR_VAR_1}{FC_ENG}\p嗯哼，这话真棒！\nSi, bueno！嗯哼，\l我会试着这么说，就像，火腿！\p那么，是时候说再见了！\n感谢你为我做的一切！\p改天和我对战一场，好吗？\n再见！$
```

修复前实际中文：

```text
{STR_VAR_1}\p嗯哼，这话真棒！
Si, bueno！嗯哼，\l我会试着这么说，就像，火腿！\p那么，是时候说再见了！
感谢你为我做的一切！\p改天和我对战一场，好吗？
再见！
```

最终中文：

```text
{STR_VAR_1}\p嗯哼，这话真棒！
好的，嗯哼！\l我会爽快地试着这么说！\p那么，是时候说再见了！
感谢你为我做的一切！\p改天和我对战一场，好吗？
再见！
```

证据：

```json
{
  "review": {
    "row_number": 8626,
    "symbol": "gText_ApprenticeWinSpeechThanks9",
    "domain": "ported_batch",
    "idx": "7374",
    "old": "Si, bueno！嗯哼，\\l我会试着这么说，就像，火腿！",
    "new": "好的，嗯哼！\\l我会爽快地试着这么说！",
    "reason": "恢复JPババーっと爽快说出的语气，避免无意义食物直译。",
    "scope": "both",
    "action": "fix",
    "final_text": "{STR_VAR_1}\\p嗯哼，这话真棒！\n好的，嗯哼！\\l我会爽快地试着这么说！\\p那么，是时候说再见了！\n感谢你为我做的一切！\\p改天和我对战一场，好吗？\n再见！",
    "old_current_text": "{STR_VAR_1}\\p嗯哼，这话真棒！\nSi, bueno！嗯哼，\\l我会试着这么说，就像，火腿！\\p那么，是时候说再见了！\n感谢你为我做的一切！\\p改天和我对战一场，好吗？\n再见！",
    "changed_files": [
      "../pokeemerald_us_chs/data/text/apprentice.inc",
      "patch/batches/383_apprentice_0.json"
    ],
    "us_source_file": "data/text/apprentice.inc",
    "jp_source": [
      {
        "file": "data/text/apprentice.inc",
        "text": "{STR_VAR_1}\\pあはぁ　それいいね\nオーケイ　オーケイ！\\lおじさん　ババーっと　いってみるよ！\\pそれじゃあ　おわかれだ！\nいままで　いろいろ　ありがとうね\\lいつか　しょうぶも　してくれよ！\\pアディオース！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/apprentice.inc",
        "text": "{STR_VAR_1}\\p嗯哼，这话真棒！\n好的，嗯哼！\\l我会爽快地试着这么说！\\p那么，是时候说再见了！\n感谢你为我做的一切！\\p改天和我对战一场，好吗？\n再见！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/apprentice.inc",
        "text": "{STR_VAR_1}\\pあはぁ　それいいね\nオーケイ　オーケイ！\\lおじさん　ババーっと　いってみるよ！\\pそれじゃあ　おわかれだ！\nいままで　いろいろ　ありがとうね\\lいつか　しょうぶも　してくれよ！\\pアディオース！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_ApprenticeWinSpeechThanks9",
      "file": "patch/batches/383_apprentice_0.json",
      "payload_address": "0x090720DC",
      "payload_sha256": "e0b145813dd7845d246e32efa4519722badfc0322b4cfe0340f34bf1ecc1b1e5",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085DC928",
          "original": "0x082731FF",
          "target": "0x090720DC",
          "batch": "patch/batches/383_apprentice_0.json"
        }
      ]
    }
  ]
}
```

### CSV 第 8793 行 · ported_batch / 7541 · gTVPokemonNewsBattleFrontierText05

判定：`fixed_verified`

理由：重复在。

日文：

```text
バトルド-ム\nシングル　バトルト-ナメントに\lちょうせんした　{FD:02}さんが\l{FD:03}　れんぱで\lきろくを　こうしん　しました!\p……{FD:02}さん!
```

英文：

```text
The TRAINER {STR_VAR_1} set a new
{STR_VAR_2}-championship-streak record\lcompeting in the BATTLE DOME's\lSINGLE BATTLE Tournaments.\pHere's to {STR_VAR_1}!$
```

报告原中文：

```text
{FC_ENG}训练家{FC_JPN}{STR_VAR_1}{FC_ENG}在\n在对战巨蛋单打对战锦标赛中\l创造了{FC_JPN}{STR_VAR_2}{FC_ENG}连冠的新纪录。\p让我们为{FC_JPN}{STR_VAR_1}{FC_ENG}欢呼！$
```

修复前实际中文：

```text
训练家{STR_VAR_1}在
在对战巨蛋单打对战锦标赛中\l创造了{STR_VAR_2}连冠的新纪录。\p让我们为{STR_VAR_1}欢呼！
```

最终中文：

```text
训练家{STR_VAR_1}在
对战巨蛋单打对战锦标赛中\l创造了{STR_VAR_2}连冠的新纪录。\p让我们为{STR_VAR_1}欢呼！
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/tv.inc",
        "text": "训练家{STR_VAR_1}在\n对战巨蛋单打对战锦标赛中\\l创造了{STR_VAR_2}连冠的新纪录。\\p让我们为{STR_VAR_1}欢呼！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/tv/battle_frontier_news.inc",
        "text": "バトルドーム\nシングル　バトルトーナメントに\\lちょうせんした　{STR_VAR_1}さんが\\l{STR_VAR_2}　れんぱで\\lきろくを　こうしん　しました！\\p⋯⋯{STR_VAR_1}さん！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gTVPokemonNewsBattleFrontierText05",
      "file": "patch/batches/386_tv_0.json",
      "payload_address": "0x09076F69",
      "payload_sha256": "903afb24e3274ab981594fb265393f9764eb54e4e2ca141b590fac746baa00c3",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08568FE4",
          "original": "0x082512C1",
          "target": "0x09076F69",
          "batch": "patch/batches/386_tv_0.json"
        }
      ]
    }
  ]
}
```

### CSV 第 8794 行 · ported_batch / 7542 · gTVPokemonNewsBattleFrontierText06

判定：`fixed_verified`

理由：重复在。

日文：

```text
バトルド-ム\nダブル　バトルト-ナメントに\lちょうせんした　{FD:02}さんが\l{FD:03}　れんぱで\lきろくを　こうしん　しました!\p……{FD:02}さん!
```

英文：

```text
The TRAINER {STR_VAR_1} set a new
{STR_VAR_2}-championship-streak record\lcompeting in the BATTLE DOME's\lDOUBLE BATTLE Tournaments.\pHere's to {STR_VAR_1}!$
```

报告原中文：

```text
{FC_ENG}训练家{FC_JPN}{STR_VAR_1}{FC_ENG}在\n在对战巨蛋双打对战锦标赛中\l创造了{FC_JPN}{STR_VAR_2}{FC_ENG}连冠的新纪录。\p让我们为{FC_JPN}{STR_VAR_1}{FC_ENG}欢呼！$
```

修复前实际中文：

```text
训练家{STR_VAR_1}在
在对战巨蛋双打对战锦标赛中\l创造了{STR_VAR_2}连冠的新纪录。\p让我们为{STR_VAR_1}欢呼！
```

最终中文：

```text
训练家{STR_VAR_1}在
对战巨蛋双打对战锦标赛中\l创造了{STR_VAR_2}连冠的新纪录。\p让我们为{STR_VAR_1}欢呼！
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/tv.inc",
        "text": "训练家{STR_VAR_1}在\n对战巨蛋双打对战锦标赛中\\l创造了{STR_VAR_2}连冠的新纪录。\\p让我们为{STR_VAR_1}欢呼！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/tv/battle_frontier_news.inc",
        "text": "バトルドーム\nダブル　バトルトーナメントに\\lちょうせんした　{STR_VAR_1}さんが\\l{STR_VAR_2}　れんぱで\\lきろくを　こうしん　しました！\\p⋯⋯{STR_VAR_1}さん！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gTVPokemonNewsBattleFrontierText06",
      "file": "patch/batches/386_tv_0.json",
      "payload_address": "0x09076FC5",
      "payload_sha256": "b1f84e5221bd5605d02e9b3c20738035d30e5baff810d699c6afb7401220ab15",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08568FE8",
          "original": "0x08251306",
          "target": "0x09076FC5",
          "batch": "patch/batches/386_tv_0.json"
        }
      ]
    }
  ]
}
```

### CSV 第 8988 行 · ported_batch / 7736 · SecretBase_Text_Trainer6Intro

判定：`fixed_verified`

理由：与同角色同原文的PreChampion模板统一；修复病句。

日文：

```text
わたしの　ポケモン　けんきゅうじょへ\nようこそ!\pここで　ポケモン　しょうぶに　ついて\nこっそり　べんきょう　してるのよ\pどう　わたしの　じつりょく　みてみる?
```

英文：

```text
Welcome to my POKéMON LAB.\pI carry out research on battling in
secrecy.\pWould you like to see how strong I am?$
```

报告原中文：

```text
{FC_ENG}欢迎来到我的精灵研究所，\n我在调查秘密的对战。\p想试试我有多么强吗？$
```

修复前实际中文：

```text
欢迎来到我的精灵研究所，
我在调查秘密的对战。\p想试试我有多么强吗？
```

最终中文：

```text
欢迎来到我的宝可梦研究所，
我在暗中进行对战研究。\p想试试我有多么强吗？
```

证据：

```json
{
  "review": {
    "row_number": 8988,
    "symbol": "SecretBase_Text_Trainer6Intro",
    "domain": "ported_batch",
    "idx": "7736",
    "old": "欢迎来到我的精灵研究所，\n我在调查秘密的对战。",
    "new": "欢迎来到我的宝可梦研究所，\n我在暗中进行对战研究。",
    "reason": "与同角色同原文的PreChampion模板统一；修复病句。",
    "scope": "both",
    "action": "fix",
    "final_text": "欢迎来到我的宝可梦研究所，\n我在暗中进行对战研究。\\p想试试我有多么强吗？",
    "old_current_text": "欢迎来到我的精灵研究所，\n我在调查秘密的对战。\\p想试试我有多么强吗？",
    "changed_files": [
      "../pokeemerald_us_chs/data/text/secret_base_trainers.inc",
      "patch/batches/391_secret_base_trainers.json"
    ],
    "us_source_file": "data/text/secret_base_trainers.inc",
    "jp_source": [
      {
        "file": "data/text/secret_base_trainers.inc",
        "text": "わたしの　ポケモン　けんきゅうじょへ\nようこそ！\\pここで　ポケモン　しょうぶに　ついて\nこっそり　べんきょう　してるのよ\\pどう　わたしの　じつりょく　みてみる？$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/secret_base_trainers.inc",
        "text": "欢迎来到我的宝可梦研究所，\n我在暗中进行对战研究。\\p想试试我有多么强吗？$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/secret_base_trainers.inc",
        "text": "わたしの　ポケモン　けんきゅうじょへ\nようこそ！\\pここで　ポケモン　しょうぶに　ついて\nこっそり　べんきょう　してるのよ\\pどう　わたしの　じつりょく　みてみる？$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_SecretBase_Text_Trainer6Intro",
      "file": "patch/batches/391_secret_base_trainers.json",
      "payload_address": "0x0907AB9E",
      "payload_sha256": "fedebde3942f0e5bcef5ba0991ed68e5b82f55dc41d19514db9362268d7dd1ee",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0824616D",
          "original": "0x082453EB",
          "target": "0x0907AB9E",
          "batch": "patch/batches/391_secret_base_trainers.json"
        }
      ]
    }
  ]
}
```

### CSV 第 9108 行 · ported_batch / 7856 · MauvilleCity_PokemonCenter_1F_Text_CheckedPokedexStory

判定：`fixed_verified`

理由：checked不是校对文字。

日文：

```text
{FD:04}という\nトレ-ナ-の　はなし　だが……\pなんと　{FD:02}かいも\nずかんを　みた　そうだ!\p{FD:04}は　ずかんで　ポケモンを\nしらべるのが　だいすきな　トレ-ナ-だな!
```

英文：

```text
This is a tale of a TRAINER
named {STR_VAR_3}.\pThis TRAINER checked a POKéDEX
{STR_VAR_1} times!\p{STR_VAR_3} must love inspecting
POKéMON in a POKéDEX!$
```

报告原中文：

```text
{FC_ENG}关于{FC_JPN}{STR_VAR_3}{FC_ENG}是这样流传\n的。\p他校对宝可梦图鉴有\n{FC_JPN}{STR_VAR_1}{FC_ENG}次了！\p{FC_JPN}{STR_VAR_3}{FC_ENG}喜欢在宝可梦图鉴中查看\n宝可梦的数据！$
```

修复前实际中文：

```text
关于{STR_VAR_3}是这样流传
的。\p他校对宝可梦图鉴有
{STR_VAR_1}次了！\p{STR_VAR_3}喜欢在宝可梦图鉴中查看
宝可梦的数据！
```

最终中文：

```text
关于{STR_VAR_3}是这样流传
的。\p他查看宝可梦图鉴有
{STR_VAR_1}次了！\p{STR_VAR_3}喜欢在宝可梦图鉴中查看
宝可梦的数据！
```

证据：

```json
{
  "review": {
    "row_number": 9108,
    "symbol": "MauvilleCity_PokemonCenter_1F_Text_CheckedPokedexStory",
    "domain": "ported_batch",
    "idx": "7856",
    "old": "他校对宝可梦图鉴有",
    "new": "他查看宝可梦图鉴有",
    "reason": "checked不是校对文字。",
    "scope": "both",
    "action": "fix",
    "final_text": "关于{STR_VAR_3}是这样流传\n的。\\p他查看宝可梦图鉴有\n{STR_VAR_1}次了！\\p{STR_VAR_3}喜欢在宝可梦图鉴中查看\n宝可梦的数据！",
    "old_current_text": "关于{STR_VAR_3}是这样流传\n的。\\p他校对宝可梦图鉴有\n{STR_VAR_1}次了！\\p{STR_VAR_3}喜欢在宝可梦图鉴中查看\n宝可梦的数据！",
    "changed_files": [
      "../pokeemerald_us_chs/data/scripts/mauville_man.inc",
      "patch/batches/392_mauville_man_0.json"
    ],
    "us_source_file": "data/scripts/mauville_man.inc",
    "jp_source": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "{STR_VAR_3}という\nトレーナーの　はなし　だが⋯⋯\\pなんと　{STR_VAR_1}かいも\nずかんを　みた　そうだ！\\p{STR_VAR_3}は　ずかんで　ポケモンを\nしらべるのが　だいすきな　トレーナーだな！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "关于{STR_VAR_3}是这样流传\n的。\\p他查看宝可梦图鉴有\n{STR_VAR_1}次了！\\p{STR_VAR_3}喜欢在宝可梦图鉴中查看\n宝可梦的数据！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "{STR_VAR_3}という\nトレーナーの　はなし　だが⋯⋯\\pなんと　{STR_VAR_1}かいも\nずかんを　みた　そうだ！\\p{STR_VAR_3}は　ずかんで　ポケモンを\nしらべるのが　だいすきな　トレーナーだな！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_MauvilleCity_PokemonCenter_1F_Text_CheckedPokedexStory",
      "file": "patch/batches/392_mauville_man_0.json",
      "payload_address": "0x0907C057",
      "payload_sha256": "dfd6320fc5907c569732372426e6542f486d6e81958dc373a99da3661c5025a4",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0857AE28",
          "original": "0x08255EB9",
          "target": "0x0907C057",
          "batch": "patch/batches/392_mauville_man_0.json"
        }
      ]
    }
  ]
}
```

### CSV 第 9110 行 · ported_batch / 7858 · MauvilleCity_PokemonCenter_1F_Text_LedgesJumpedStory

判定：`fixed_verified`

理由：修复已经的笔误并恢复跳下岩礁的宾语。

日文：

```text
{FD:04}という\nトレ-ナ-の　はなし　だが……\pなんと　{FD:02}かいも\nだんさを　とびおりた　らしい!\p{FD:04}は　だんさを　みると\nとびおりずに　おれない　トレ-ナ-だな!
```

英文：

```text
This is a tale of a TRAINER
named {STR_VAR_3}.\pThis TRAINER jumped down ledges
{STR_VAR_1} times!\pIf there's a ledge to be jumped,
{STR_VAR_3} can't ignore it!$
```

报告原中文：

```text
{FC_ENG}关于{FC_JPN}{STR_VAR_3}{FC_ENG}是这样流传\n的。\p他几经跳过\n{FC_JPN}{STR_VAR_1}{FC_ENG}次了！\p如果有适合跳跃的岩礁，\n{FC_JPN}{STR_VAR_3}{FC_ENG}一定会去跳的！$
```

修复前实际中文：

```text
关于{STR_VAR_3}是这样流传
的。\p他几经跳过
{STR_VAR_1}次了！\p如果有适合跳跃的岩礁，
{STR_VAR_3}一定会去跳的！
```

最终中文：

```text
关于{STR_VAR_3}是这样流传
的。\p他已经跳下
{STR_VAR_1}次岩礁了！\p如果有适合跳跃的岩礁，
{STR_VAR_3}一定会去跳的！
```

证据：

```json
{
  "review": {
    "row_number": 9110,
    "symbol": "MauvilleCity_PokemonCenter_1F_Text_LedgesJumpedStory",
    "domain": "ported_batch",
    "idx": "7858",
    "old": "他几经跳过\n{STR_VAR_1}次了！",
    "new": "他已经跳下\n{STR_VAR_1}次岩礁了！",
    "reason": "修复已经的笔误并恢复跳下岩礁的宾语。",
    "scope": "both",
    "action": "fix",
    "final_text": "关于{STR_VAR_3}是这样流传\n的。\\p他已经跳下\n{STR_VAR_1}次岩礁了！\\p如果有适合跳跃的岩礁，\n{STR_VAR_3}一定会去跳的！",
    "old_current_text": "关于{STR_VAR_3}是这样流传\n的。\\p他几经跳过\n{STR_VAR_1}次了！\\p如果有适合跳跃的岩礁，\n{STR_VAR_3}一定会去跳的！",
    "changed_files": [
      "../pokeemerald_us_chs/data/scripts/mauville_man.inc",
      "patch/batches/392_mauville_man_0.json"
    ],
    "us_source_file": "data/scripts/mauville_man.inc",
    "jp_source": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "{STR_VAR_3}という\nトレーナーの　はなし　だが⋯⋯\\pなんと　{STR_VAR_1}かいも\nだんさを　とびおりた　らしい！\\p{STR_VAR_3}は　だんさを　みると\nとびおりずに　おれない　トレーナーだな！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "关于{STR_VAR_3}是这样流传\n的。\\p他已经跳下\n{STR_VAR_1}次岩礁了！\\p如果有适合跳跃的岩礁，\n{STR_VAR_3}一定会去跳的！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "{STR_VAR_3}という\nトレーナーの　はなし　だが⋯⋯\\pなんと　{STR_VAR_1}かいも\nだんさを　とびおりた　らしい！\\p{STR_VAR_3}は　だんさを　みると\nとびおりずに　おれない　トレーナーだな！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_MauvilleCity_PokemonCenter_1F_Text_LedgesJumpedStory",
      "file": "patch/batches/392_mauville_man_0.json",
      "payload_address": "0x0907C113",
      "payload_sha256": "69b560196a0ac924dc6a356d87b5848e28195b74d6d019f5bcc594425558c96d",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0857AE48",
          "original": "0x08255F9B",
          "target": "0x0907C113",
          "batch": "patch/batches/392_mauville_man_0.json"
        }
      ]
    }
  ]
}
```

### CSV 第 9114 行 · ported_batch / 7862 · MauvilleCity_PokemonCenter_1F_Text_UsedDaycareStory

判定：`fixed_verified`

理由：寄存次数，不是宝可梦只数。

日文：

```text
{FD:04}という\nトレ-ナ-の　はなし　だが……\pなんと　{FD:02}かいも\nそだてやに　あずけた　らしい!\p{FD:04}は　とにかく　そだてまくる\nモ-レツな　トレ-ナ-に　ちがいない!
```

英文：

```text
This is a tale of a TRAINER
named {STR_VAR_3}.\pThis TRAINER left POKéMON with the
DAY CARE {STR_VAR_1} times!\p{STR_VAR_3} must be a real go-getter
who raises POKéMON aggressively!$
```

报告原中文：

```text
{FC_ENG}关于{FC_JPN}{STR_VAR_3}{FC_ENG}是这样流传\n的。\p他在培育屋照顾的宝可梦\n有{FC_JPN}{STR_VAR_1}{FC_ENG}只！\p{FC_JPN}{STR_VAR_3}{FC_ENG}一定是一个培育\n宝可梦的老手了！$
```

修复前实际中文：

```text
关于{STR_VAR_3}是这样流传
的。\p他在培育屋照顾的宝可梦
有{STR_VAR_1}只！\p{STR_VAR_3}一定是一个培育
宝可梦的老手了！
```

最终中文：

```text
关于{STR_VAR_3}是这样流传
的。\p他曾把宝可梦寄存在培育屋
{STR_VAR_1}次！\p{STR_VAR_3}一定是一个培育
宝可梦的老手了！
```

证据：

```json
{
  "review": {
    "row_number": 9114,
    "symbol": "MauvilleCity_PokemonCenter_1F_Text_UsedDaycareStory",
    "domain": "ported_batch",
    "idx": "7862",
    "old": "他在培育屋照顾的宝可梦\n有{STR_VAR_1}只！",
    "new": "他曾把宝可梦寄存在培育屋\n{STR_VAR_1}次！",
    "reason": "寄存次数，不是宝可梦只数。",
    "scope": "both",
    "action": "fix",
    "final_text": "关于{STR_VAR_3}是这样流传\n的。\\p他曾把宝可梦寄存在培育屋\n{STR_VAR_1}次！\\p{STR_VAR_3}一定是一个培育\n宝可梦的老手了！",
    "old_current_text": "关于{STR_VAR_3}是这样流传\n的。\\p他在培育屋照顾的宝可梦\n有{STR_VAR_1}只！\\p{STR_VAR_3}一定是一个培育\n宝可梦的老手了！",
    "changed_files": [
      "../pokeemerald_us_chs/data/scripts/mauville_man.inc",
      "patch/batches/392_mauville_man_0.json"
    ],
    "us_source_file": "data/scripts/mauville_man.inc",
    "jp_source": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "{STR_VAR_3}という\nトレーナーの　はなし　だが⋯⋯\\pなんと　{STR_VAR_1}かいも\nそだてやに　あずけた　らしい！\\p{STR_VAR_3}は　とにかく　そだてまくる\nモーレツな　トレーナーに　ちがいない！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "关于{STR_VAR_3}是这样流传\n的。\\p他曾把宝可梦寄存在培育屋\n{STR_VAR_1}次！\\p{STR_VAR_3}一定是一个培育\n宝可梦的老手了！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "{STR_VAR_3}という\nトレーナーの　はなし　だが⋯⋯\\pなんと　{STR_VAR_1}かいも\nそだてやに　あずけた　らしい！\\p{STR_VAR_3}は　とにかく　そだてまくる\nモーレツな　トレーナーに　ちがいない！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_MauvilleCity_PokemonCenter_1F_Text_UsedDaycareStory",
      "file": "patch/batches/392_mauville_man_0.json",
      "payload_address": "0x0907C288",
      "payload_sha256": "9f23192718ba2573cfe2d8caa930ab010c2926a873fee78cb27f66f0dab0909c",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0857AE88",
          "original": "0x08256150",
          "target": "0x0907C288",
          "batch": "patch/batches/392_mauville_man_0.json"
        }
      ]
    }
  ]
}
```

### CSV 第 9121 行 · ported_batch / 7869 · MauvilleCity_PokemonCenter_1F_Text_CheckedPokedexAction

判定：`fixed_verified`

理由：同上查看图鉴。

日文：

```text
ずかんを　みた
```

英文：

```text
Checked a POKéDEX$
```

报告原中文：

```text
{FC_ENG}校对图鉴数据$
```

修复前实际中文：

```text
校对图鉴数据
```

最终中文：

```text
查看图鉴数据
```

证据：

```json
{
  "review": {
    "row_number": 9121,
    "symbol": "MauvilleCity_PokemonCenter_1F_Text_CheckedPokedexAction",
    "domain": "ported_batch",
    "idx": "7869",
    "old": "校对图鉴数据",
    "new": "查看图鉴数据",
    "reason": "同上查看图鉴。",
    "scope": "both",
    "action": "fix",
    "final_text": "查看图鉴数据",
    "old_current_text": "校对图鉴数据",
    "changed_files": [
      "../pokeemerald_us_chs/data/scripts/mauville_man.inc",
      "patch/batches/393_mauville_man_1.json"
    ],
    "us_source_file": "data/scripts/mauville_man.inc",
    "jp_source": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "ずかんを　みた$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "查看图鉴数据$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "ずかんを　みた$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_MauvilleCity_PokemonCenter_1F_Text_CheckedPokedexAction",
      "file": "patch/batches/393_mauville_man_1.json",
      "payload_address": "0x0907C3DE",
      "payload_sha256": "503af953f39a939c016d81820e0173e6a5fe3abb8cc6aab94410d454245602ac",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0857AE24",
          "original": "0x08255EB1",
          "target": "0x0907C3DE",
          "batch": "patch/batches/393_mauville_man_1.json"
        }
      ]
    }
  ]
}
```

### CSV 第 9132 行 · ported_batch / 7880 · MauvilleCity_PokemonCenter_1F_Text_UsedDaycareTitle

判定：`fixed_verified`

理由：DAY CARE-Using不是在培育屋上班。

日文：

```text
そだてやを　つかいこなす　トレ-ナ-
```

英文：

```text
The DAY CARE-Using Trainer$
```

报告原中文：

```text
{FC_ENG}在培育屋工作的训练家$
```

修复前实际中文：

```text
在培育屋工作的训练家
```

最终中文：

```text
善用培育屋的训练家
```

证据：

```json
{
  "review": {
    "row_number": 9132,
    "symbol": "MauvilleCity_PokemonCenter_1F_Text_UsedDaycareTitle",
    "domain": "ported_batch",
    "idx": "7880",
    "old": "在培育屋工作的训练家",
    "new": "善用培育屋的训练家",
    "reason": "DAY CARE-Using不是在培育屋上班。",
    "scope": "both",
    "action": "fix",
    "final_text": "善用培育屋的训练家",
    "old_current_text": "在培育屋工作的训练家",
    "changed_files": [
      "../pokeemerald_us_chs/data/scripts/mauville_man.inc",
      "patch/batches/393_mauville_man_1.json"
    ],
    "us_source_file": "data/scripts/mauville_man.inc",
    "jp_source": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "そだてやを　つかいこなす　トレーナー$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "善用培育屋的训练家$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/scripts/mauville_man.inc",
        "text": "そだてやを　つかいこなす　トレーナー$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_MauvilleCity_PokemonCenter_1F_Text_UsedDaycareTitle",
      "file": "patch/batches/393_mauville_man_1.json",
      "payload_address": "0x0907C469",
      "payload_sha256": "0b41185a65a42fdcb616c7f1e5dacc66393542672cc043cb6c6d84e027598f14",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0857AE80",
          "original": "0x0825612C",
          "target": "0x0907C469",
          "batch": "patch/batches/393_mauville_man_1.json"
        }
      ]
    }
  ]
}
```

### CSV 第 9156 行 · ported_batch / 7904 · GiddyText_SoDesirable

判定：`fixed_verified`

理由：あこがれる 指憧憬。

日文：

```text
　あこがれる　よね-
```

英文：

```text
 so desirable!$
```

报告原中文：

```text
{FC_ENG} 太合意的了！$
```

修复前实际中文：

```text
 太合意的了！
```

最终中文：

```text
 太令人向往了！
```

证据：

```json
{
  "review": {
    "row_number": 9156,
    "symbol": "GiddyText_SoDesirable",
    "domain": "ported_batch",
    "idx": "7904",
    "old": "太合意的了！",
    "new": "太令人向往了！",
    "reason": "あこがれる 指憧憬。",
    "scope": "both",
    "action": "fix",
    "final_text": " 太令人向往了！",
    "old_current_text": " 太合意的了！",
    "changed_files": [
      "../pokeemerald_us_chs/data/text/mauville_man.inc",
      "patch/batches/395_mauville_man.json"
    ],
    "us_source_file": "data/text/mauville_man.inc",
    "jp_source": [
      {
        "file": "data/text/mauville_man.inc",
        "text": "　あこがれる　よねー$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/mauville_man.inc",
        "text": " 太令人向往了！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/mauville_man.inc",
        "text": "　あこがれる　よねー$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_GiddyText_SoDesirable",
      "file": "patch/batches/395_mauville_man.json",
      "payload_address": "0x0907C903",
      "payload_sha256": "6416295b29737e943888c40ce92d477ba5ef84ddd1f6caeb74ddc646598a418d",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0857AC24",
          "original": "0x082593F0",
          "target": "0x0907C903",
          "batch": "patch/batches/395_mauville_man.json"
        }
      ]
    }
  ]
}
```

### CSV 第 9174 行 · ported_batch / 7922 · CaveOfOrigin_B1F_Text_WallaceStory

判定：`fixed_verified`

理由：重复的。

日文：

```text
そうか　きみが　{FD:01}{FD:05}……\nきみの　かつやくは　きいているよ\pわたしの　なまえは　ミクリ\nルネの　ジムリ-ダ-を　していたけれど\lちょっと　わけが　あってね\pいまは　ししょうの　アダンさんに\nジムのことは　おまかせして　いるのさ\p……　……　……\n……　……　……\pいま　このまちで　あばれている\nグラ-ドンと　カイオ-ガは\lちょうこだい　ポケモンと　いわれている\pけれど　ちょうこだい　ポケモンは\nあの2ひき　だけじゃ　なかった……\lどこかに　もう1ひき\pそう……　レックウザと　よばれる\nちょうこだい　ポケモンが　いるんだよ\pとおい　むかしに\nあの2ひきの　たたかいを　しずめたのも\lレックウザ　だと　いわれている\pだが　レックウザが　どこに　いるかは\nわたしにも　わからない……
```

英文：

```text
Ah, so you are {PLAYER}{KUN}?
I've heard tales of your exploits.\pMy name is WALLACE.\pI was once the GYM LEADER of
SOOTOPOLIS, but something came up.\pSo now, I've entrusted my mentor JUAN
with the GYM's operation.\p… … … … … …
… … … … … …\pGROUDON and KYOGRE, the two POKéMON
wreaking havoc here, are considered\lto be super-ancient POKéMON.\pBut there aren't just two super-
ancient POKéMON.\pThere is one more somewhere.\pSomewhere, there is a super-
ancient POKéMON named RAYQUAZA.\pIt's said that it was RAYQUAZA that
becalmed the two combatants in\lthe distant past.\pBut even I have no clue as to
RAYQUAZA's whereabouts…$
```

报告原中文：

```text
{FC_ENG}啊，你就是{FC_JPN}{PLAYER}{FC_ENG}{FC_JPN}{KUN}{FC_ENG}吗？\n你的活跃表现我早有耳闻。\p我的名字是米可利。\p曾经是琉璃市的道馆馆主，\n不过因为某些原因，\p现在我把管理道馆的事情\n托付给我的老师亚当了。\p…… …… ……\n…… …… ……\p在这里肆虐的2只宝可梦——\n固拉多和盖欧卡，\l被称为超古代宝可梦，\p然而，超古代宝可梦\n并不止这2只……\p在世界的某处\n还存在着第3只——\p没错，那就是被称为烈空坐\n的超古代宝可梦。\p传说在远古时期，\n正是烈空坐平息了\l那2只宝可梦的的斗争。\p可就连我也不清楚它\n如今究竟身在何处……$
```

修复前实际中文：

```text
啊，你就是{PLAYER}{KUN}吗？
你的活跃表现我早有耳闻。\p我的名字是米可利。\p曾经是琉璃市的道馆馆主，
不过因为某些原因，\p现在我把管理道馆的事情
托付给我的老师亚当了。\p…… …… ……
…… …… ……\p在这里肆虐的2只宝可梦——
固拉多和盖欧卡，\l被称为超古代宝可梦，\p然而，超古代宝可梦
并不止这2只……\p在世界的某处
还存在着第3只——\p没错，那就是被称为烈空坐
的超古代宝可梦。\p传说在远古时期，
正是烈空坐平息了\l那2只宝可梦的的斗争。\p可就连我也不清楚它
如今究竟身在何处……
```

最终中文：

```text
啊，你就是{PLAYER}{KUN}吗？
你的活跃表现我早有耳闻。\p我的名字是米可利。\p曾经是琉璃市的道馆馆主，
不过因为某些原因，\p现在我把管理道馆的事情
托付给我的老师亚当了。\p…… …… ……
…… …… ……\p在这里肆虐的2只宝可梦——
固拉多和盖欧卡，\l被称为超古代宝可梦，\p然而，超古代宝可梦
并不止这2只……\p在世界的某处
还存在着第3只——\p没错，那就是被称为烈空坐
的超古代宝可梦。\p传说在远古时期，
正是烈空坐平息了\l那2只宝可梦的斗争。\p可就连我也不清楚它
如今究竟身在何处……
```

证据：

```json
{
  "review": {
    "row_number": 9174,
    "symbol": "CaveOfOrigin_B1F_Text_WallaceStory",
    "domain": "ported_batch",
    "idx": "7922",
    "old": "的的斗争",
    "new": "的斗争",
    "reason": "重复的。",
    "scope": "both",
    "action": "fix",
    "final_text": "啊，你就是{PLAYER}{KUN}吗？\n你的活跃表现我早有耳闻。\\p我的名字是米可利。\\p曾经是琉璃市的道馆馆主，\n不过因为某些原因，\\p现在我把管理道馆的事情\n托付给我的老师亚当了。\\p…… …… ……\n…… …… ……\\p在这里肆虐的2只宝可梦——\n固拉多和盖欧卡，\\l被称为超古代宝可梦，\\p然而，超古代宝可梦\n并不止这2只……\\p在世界的某处\n还存在着第3只——\\p没错，那就是被称为烈空坐\n的超古代宝可梦。\\p传说在远古时期，\n正是烈空坐平息了\\l那2只宝可梦的斗争。\\p可就连我也不清楚它\n如今究竟身在何处……",
    "old_current_text": "啊，你就是{PLAYER}{KUN}吗？\n你的活跃表现我早有耳闻。\\p我的名字是米可利。\\p曾经是琉璃市的道馆馆主，\n不过因为某些原因，\\p现在我把管理道馆的事情\n托付给我的老师亚当了。\\p…… …… ……\n…… …… ……\\p在这里肆虐的2只宝可梦——\n固拉多和盖欧卡，\\l被称为超古代宝可梦，\\p然而，超古代宝可梦\n并不止这2只……\\p在世界的某处\n还存在着第3只——\\p没错，那就是被称为烈空坐\n的超古代宝可梦。\\p传说在远古时期，\n正是烈空坐平息了\\l那2只宝可梦的的斗争。\\p可就连我也不清楚它\n如今究竟身在何处……",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/CaveOfOrigin_B1F/scripts.inc",
      "patch/batches/398_player_name_dialogue.json"
    ],
    "us_source_file": "data/maps/CaveOfOrigin_B1F/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/CaveOfOrigin_B1F/scripts.inc",
        "text": "そうか　きみが　{PLAYER}{KUN}⋯⋯\nきみの　かつやくは　きいているよ\\pわたしの　なまえは　ミクリ\nルネの　ジムリーダーを　していたけれど\\lちょっと　わけが　あってね\\pいまは　ししょうの　アダンさんに\nジムのことは　おまかせして　いるのさ\\p⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯\\pいま　このまちで　あばれている\nグラードンと　カイオーガは\\lちょうこだい　ポケモンと　いわれている\\pけれど　ちょうこだい　ポケモンは\nあの2ひき　だけじゃ　なかった⋯⋯\\lどこかに　もう1ひき\\pそう⋯⋯　レックウザと　よばれる\nちょうこだい　ポケモンが　いるんだよ\\pとおい　むかしに\nあの2ひきの　たたかいを　しずめたのも\\lレックウザ　だと　いわれている\\pだが　レックウザが　どこに　いるかは\nわたしにも　わからない⋯⋯$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/CaveOfOrigin_B1F/scripts.inc",
        "text": "啊，你就是{PLAYER}{KUN}吗？\n你的活跃表现我早有耳闻。\\p我的名字是米可利。\\p曾经是琉璃市的道馆馆主，\n不过因为某些原因，\\p现在我把管理道馆的事情\n托付给我的老师亚当了。\\p…… …… ……\n…… …… ……\\p在这里肆虐的2只宝可梦——\n固拉多和盖欧卡，\\l被称为超古代宝可梦，\\p然而，超古代宝可梦\n并不止这2只……\\p在世界的某处\n还存在着第3只——\\p没错，那就是被称为烈空坐\n的超古代宝可梦。\\p传说在远古时期，\n正是烈空坐平息了\\l那2只宝可梦的斗争。\\p可就连我也不清楚它\n如今究竟身在何处……$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/CaveOfOrigin_B1F/scripts.inc",
        "text": "そうか　きみが　{PLAYER}{KUN}⋯⋯\nきみの　かつやくは　きいているよ\\pわたしの　なまえは　ミクリ\nルネの　ジムリーダーを　していたけれど\\lちょっと　わけが　あってね\\pいまは　ししょうの　アダンさんに\nジムのことは　おまかせして　いるのさ\\p⋯⋯　⋯⋯　⋯⋯\n⋯⋯　⋯⋯　⋯⋯\\pいま　このまちで　あばれている\nグラードンと　カイオーガは\\lちょうこだい　ポケモンと　いわれている\\pけれど　ちょうこだい　ポケモンは\nあの2ひき　だけじゃ　なかった⋯⋯\\lどこかに　もう1ひき\\pそう⋯⋯　レックウザと　よばれる\nちょうこだい　ポケモンが　いるんだよ\\pとおい　むかしに\nあの2ひきの　たたかいを　しずめたのも\\lレックウザ　だと　いわれている\\pだが　レックウザが　どこに　いるかは\nわたしにも　わからない⋯⋯$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_CaveOfOrigin_B1F_Text_WallaceStory",
      "file": "patch/batches/398_player_name_dialogue.json",
      "payload_address": "0x0907CBF9",
      "payload_sha256": "9639614ce73ffb54d3341b11218228198998e19295dfad6e8e374889db21a7a9",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08219103",
          "original": "0x082191C4",
          "target": "0x0907CBF9",
          "batch": "patch/batches/398_player_name_dialogue.json"
        }
      ]
    }
  ]
}
```

### CSV 第 9237 行 · ported_batch / 7987 · Roulette_Text_YouveWonXCoins

判定：`fixed_verified`

理由：与同一轮盘界面统一代币术语。

日文：

```text
おめでとう　ございます!\nコイン　{FD:02}まい　はいります!
```

英文：

```text
You've won {STR_VAR_1} COINS!$
```

报告原中文：

```text
{FC_ENG}恭喜中奖！\n获得了{STR_VAR_1}枚硬币！$
```

修复前实际中文：

```text
恭喜中奖！
获得了{STR_VAR_1}枚硬币！
```

最终中文：

```text
恭喜中奖！
获得了{STR_VAR_1}枚代币！
```

证据：

```json
{
  "review": {
    "row_number": 9237,
    "symbol": "Roulette_Text_YouveWonXCoins",
    "domain": "ported_batch",
    "idx": "7987",
    "old": "枚硬币",
    "new": "枚代币",
    "reason": "与同一轮盘界面统一代币术语。",
    "scope": "both",
    "action": "fix",
    "final_text": "恭喜中奖！\n获得了{STR_VAR_1}枚代币！",
    "old_current_text": "恭喜中奖！\n获得了{STR_VAR_1}枚硬币！",
    "changed_files": [
      "../pokeemerald_us_chs/data/scripts/roulette.inc",
      "patch/batches/401_roulette.json"
    ],
    "us_source_file": "data/scripts/roulette.inc",
    "jp_source": [
      {
        "file": "data/scripts/roulette.inc",
        "text": "おめでとう　ございます！\nコイン　{STR_VAR_1}まい　はいります！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/scripts/roulette.inc",
        "text": "恭喜中奖！\n获得了{STR_VAR_1}枚代币！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/scripts/roulette.inc",
        "text": "おめでとう　ございます！\nコイン　{STR_VAR_1}まい　はいります！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Roulette_Text_YouveWonXCoins",
      "file": "patch/batches/401_roulette.json",
      "payload_address": "0x0907DF49",
      "payload_sha256": "8ba43fda9a9a5d2ee9a28e526400e5e5a3482e5c1fb5cccd50ac52fafae00493",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08141B7C",
          "original": "0x08262D79",
          "target": "0x0907DF49",
          "batch": "patch/batches/401_roulette.json"
        }
      ]
    }
  ]
}
```

### CSV 第 9381 行 · ported_batch / 8131 · gText_Contest_Shyness

判定：`fixed_verified`

理由：モジモジ / shyness 指扭捏，不是心跳声。

日文：

```text
モジモジ
```

英文：

```text
shyness$
```

报告原中文：

```text
{FC_ENG}扑通扑通$
```

修复前实际中文：

```text
扑通扑通
```

最终中文：

```text
扭扭捏捏
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/contest_strings.inc",
        "text": "扭扭捏捏$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/contest_strings.inc",
        "text": "モジモジ$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_Contest_Shyness",
      "file": "patch/batches/405_contest_strings.json",
      "payload_address": "0x0907E9CB",
      "payload_sha256": "3a8f603cd077600f790c8439580e3d8f146a270672305154fd6c469abf7defc5",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x080DCC3C",
          "original": "0x0824C0D2",
          "target": "0x0907E9CB",
          "batch": "patch/batches/405_contest_strings.json"
        }
      ]
    }
  ]
}
```

### CSV 第 9589 行 · ported_batch / 8339 · gText_TheQuizAnswerIs

判定：`fixed_verified`

理由：的语序错误。

日文：

```text
クイズの　こたえは?
```

英文：

```text
The quiz answer is?
```

报告原中文：

```text
{FC_ENG}谜题答案的是？$
```

修复前实际中文：

```text
谜题答案的是？
```

最终中文：

```text
谜题的答案是？
```

证据：

```json
{
  "review": {
    "row_number": 9589,
    "symbol": "gText_TheQuizAnswerIs",
    "domain": "ported_batch",
    "idx": "8339",
    "old": "谜题答案的是？",
    "new": "谜题的答案是？",
    "reason": "的语序错误。",
    "scope": "both",
    "action": "fix",
    "final_text": "谜题的答案是？",
    "old_current_text": "谜题答案的是？",
    "changed_files": [
      "../pokeemerald_us_chs/src/strings.c",
      "patch/batches/411_strings_c_direct.json"
    ],
    "us_source_file": "src/strings.c",
    "jp_source": [
      {
        "file": "src/strings.c",
        "text": "クイズの　こたえは？"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/strings.c",
        "text": "谜题的答案是？"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/strings.c",
        "text": "クイズの　こたえは？"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_gText_TheQuizAnswerIs",
      "file": "patch/batches/411_strings_c_direct.json",
      "payload_address": "0x0907FF8D",
      "payload_sha256": "13f8306f7be1a83caee7c6c4197b9061733bfd79029d17a0e822e75544215987",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08573228",
          "original": "0x085CBCA0",
          "target": "0x0907FF8D",
          "batch": "patch/batches/411_strings_c_direct.json"
        },
        {
          "address": "0x08573258",
          "original": "0x085CBCA0",
          "target": "0x0907FF8D",
          "batch": "patch/batches/411_strings_c_direct.json"
        }
      ]
    }
  ]
}
```

### CSV 第 10075 行 · ported_batch / 8825 · sText_MemberNoLongerAvailable

判定：`fixed_verified`

理由：原文指组内有成员不方便。

日文：

```text
つごうが　わるくなってしまった\nメンバ-が　います\p
```

英文：

```text
There is a member who can no
longer remain available.\p
```

报告原中文：

```text
{FC_ENG}对方好像不方便……\p$
```

修复前实际中文：

```text
对方好像不方便……\p
```

最终中文：

```text
有成员不便进行……\p
```

证据：

```json
{
  "review": {
    "row_number": 10075,
    "symbol": "sText_MemberNoLongerAvailable",
    "domain": "ported_batch",
    "idx": "8825",
    "old": "对方好像不方便……",
    "new": "有成员不便进行……",
    "reason": "原文指组内有成员不方便。",
    "scope": "both",
    "action": "fix",
    "final_text": "有成员不便进行……\\p",
    "old_current_text": "对方好像不方便……\\p",
    "changed_files": [
      "../pokeemerald_us_chs/src/data/union_room.h",
      "patch/batches/419_union_room_0.json"
    ],
    "us_source_file": "src/data/union_room.h",
    "jp_source": [
      {
        "file": "src/data/union_room3.h",
        "text": "つごうが　わるくなってしまった\nメンバーが　います\\p"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "有成员不便进行……\\p"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room3.h",
        "text": "つごうが　わるくなってしまった\nメンバーが　います\\p"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_MemberNoLongerAvailable",
      "file": "patch/batches/419_union_room_0.json",
      "payload_address": "0x09082324",
      "payload_sha256": "cac1d5c9bccf0e318818b83f599c2df3a8206a4e114582dcc94c8e331e6f07c2",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C09E4",
          "original": "0x082C09C4",
          "target": "0x09082324",
          "batch": "patch/batches/419_union_room_0.json"
        },
        {
          "address": "0x082C0A88",
          "original": "0x082C09C4",
          "target": "0x09082324",
          "batch": "patch/batches/419_union_room_0.json"
        }
      ]
    }
  ]
}
```

### CSV 第 10076 行 · ported_batch / 8826 · sText_TrainerAppearsUnavailable

判定：`fixed_verified`

理由：原文指对方训练家不方便。

日文：

```text
つごうが　わるいみたい…\p
```

英文：

```text
The other TRAINER appears
unavailable…\p
```

报告原中文：

```text
{FC_ENG}有成员不便进行……\p$
```

修复前实际中文：

```text
有成员不便进行……\p
```

最终中文：

```text
对方好像不方便……\p
```

证据：

```json
{
  "review": {
    "row_number": 10076,
    "symbol": "sText_TrainerAppearsUnavailable",
    "domain": "ported_batch",
    "idx": "8826",
    "old": "有成员不便进行……",
    "new": "对方好像不方便……",
    "reason": "原文指对方训练家不方便。",
    "scope": "both",
    "action": "fix",
    "final_text": "对方好像不方便……\\p",
    "old_current_text": "有成员不便进行……\\p",
    "changed_files": [
      "../pokeemerald_us_chs/src/data/union_room.h",
      "patch/batches/419_union_room_0.json"
    ],
    "us_source_file": "src/data/union_room.h",
    "jp_source": [
      {
        "file": "src/data/union_room3.h",
        "text": "つごうが　わるいみたい⋯\\p"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "对方好像不方便……\\p"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room3.h",
        "text": "つごうが　わるいみたい⋯\\p"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_sText_TrainerAppearsUnavailable",
      "file": "patch/batches/419_union_room_0.json",
      "payload_address": "0x09082338",
      "payload_sha256": "23621c033d2a86a54372f65f2ddecf93d358f4b5b94724ed016336519624296e",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C0A8C",
          "original": "0x082C09E8",
          "target": "0x09082338",
          "batch": "patch/batches/419_union_room_0.json"
        }
      ]
    }
  ]
}
```

### CSV 第 10264 行 · item / 7 · 

判定：`fixed_verified`

理由：第三世代潜水球匹配海底遭遇场景，不是所有水环境。

日文：

```text
かいていに　いる
ポケモンが　つかまえ
やすくなる　ボール
```

英文：

```text
A BALL that works
better on POKéMON
on the ocean floor.
```

报告原中文：

```text
有点与众不同的球
。容易捕捉生活在
水世界的宝可梦
```

修复前实际中文：

```text
有点与众不同的球
。容易捕捉生活在
水世界的宝可梦
```

最终中文：

```text
有点与众不同的球
。容易捕捉生活在
海底的宝可梦
```

证据：

```json
{
  "review": {
    "row_number": 10264,
    "symbol": "",
    "domain": "item",
    "idx": "7",
    "old": "生活在\n水世界的宝可梦",
    "new": "生活在\n海底的宝可梦",
    "reason": "第三世代潜水球匹配海底遭遇场景，不是所有水环境。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "sDiveBallDesc",
    "final_text": "有点与众不同的球\n。容易捕捉生活在\n海底的宝可梦",
    "old_current_text": "有点与众不同的球\n。容易捕捉生活在\n水世界的宝可梦",
    "changed_files": [
      "patch/item_descriptions.json",
      "../pokeemerald_us_chs/src/data/text/item_descriptions.h"
    ],
    "us_source_file": "src/data/text/item_descriptions.h",
    "jp_source": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "かいていに　いる\nポケモンが　つかまえ\nやすくなる　ボール"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "有点与众不同的球\n。容易捕捉生活在\n海底的宝可梦"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "かいていに　いる\nポケモンが　つかまえ\nやすくなる　ボール"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 7,
      "text": "有点与众不同的球\n。容易捕捉生活在\n海底的宝可梦",
      "rom_address": "0x090915A8",
      "encoded_sha256": "9a70b443d27920fe856a8fce4a4d0fbabf57e640349c2a6720a1733acdbf3f2c",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10293 行 · item / 36 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
すべての　わざの
わざポイントを
10　かいふくする
```

英文：

```text
Restores the PP
of all moves by 10.
```

报告原中文：

```text
能让宝可梦学会的
4个招式各回复1
0PP
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10293,
    "symbol": "",
    "domain": "item",
    "idx": "36",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 36,
      "text": "能让宝可梦学会的\n4个招式各回复1\n0PP",
      "rom_address": "0x09091A74",
      "encoded_sha256": "f86d31adac2897d5ab22fb8063266784522cf1c4228cc5b1b9fa6efe20122c9a",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10294 行 · item / 37 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
ポケモン　1ぴきの
すべての　わざポイントを
ぜんかいふくする
```

英文：

```text
Fully restores the
PP of a POKéMON's
moves.
```

报告原中文：

```text
能让宝可梦学会的
4个招式回复所有
PP
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10294,
    "symbol": "",
    "domain": "item",
    "idx": "37",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 37,
      "text": "能让宝可梦学会的\n4个招式回复所有\nPP",
      "rom_address": "0x09091A9C",
      "encoded_sha256": "d207754a1c3e9103978e1ae40f88d897112fb52bc282e1af911b12e7645428a5",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10325 行 · item / 68 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
ポケモンの　レベルを
1　あげる
```

英文：

```text
Raises the level
of a POKéMON by
one.
```

报告原中文：

```text
充满能量的糖果。
给宝可梦后，等级
会提高1
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10325,
    "symbol": "",
    "domain": "item",
    "idx": "68",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 68,
      "text": "充满能量的糖果。\n给宝可梦后，等级\n会提高1",
      "rom_address": "0x09091E24",
      "encoded_sha256": "4a391f1ac250b12e5ccc81f7f303ffcba9e4629d6542962fd2bcaa87f0a20d28",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10326 行 · item / 69 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
わざポイントの
さいだいちが　あがる
```

英文：

```text
Raises the maximum
PP of a selected
move.
```

报告原中文：

```text
能让宝可梦学会的
其中1个招式PP
最大值少量提高
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10326,
    "symbol": "",
    "domain": "item",
    "idx": "69",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 69,
      "text": "能让宝可梦学会的\n其中1个招式PP\n最大值少量提高",
      "rom_address": "0x09091E50",
      "encoded_sha256": "3e66685ba396d764a142b46f998f252b5da144bd3d5733339b5678745b66933a",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10363 行 · item / 106 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
きれいな　しんじゅ
やすく　うれる
```

英文：

```text
A pretty pearl
that would sell at a
cheap price.
```

报告原中文：

```text
散发着光泽且有点
小的珍珠。可以在
商店低价出售
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10363,
    "symbol": "",
    "domain": "item",
    "idx": "106",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 106,
      "text": "散发着光泽且有点\n小的珍珠。可以在\n商店低价出售",
      "rom_address": "0x09092244",
      "encoded_sha256": "b0048dec73be5b8ddb1eb5646e93f883f5b2dea6c0ec5bec0365e2fc06887e01",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10367 行 · item / 110 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
じゅんきん　せい
たかく　うれる
```

英文：

```text
A nugget of pure
gold. Can be sold at
a high price.
```

报告原中文：

```text
闪着金光，以纯金
制成的珠子。可以
在商店高价出售
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10367,
    "symbol": "",
    "domain": "item",
    "idx": "110",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 110,
      "text": "闪着金光，以纯金\n制成的珠子。可以\n在商店高价出售",
      "rom_address": "0x09092308",
      "encoded_sha256": "70ea3f1f777b0026f061ee06045751c466d95318372443a43ec23b426ec31344",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10383 行 · item / 126 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
ホエルコの　すがたが
プリントされた　びんせん
ポケモンに　もたせる
```

英文：

```text
A WAILMER-print
MAIL to be held by
a POKéMON.
```

报告原中文：

```text
印有吼吼鲸的信纸
，可以让宝可梦携
带
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10383,
    "symbol": "",
    "domain": "item",
    "idx": "126",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 126,
      "text": "印有吼吼鲸的信纸\n，可以让宝可梦携\n带",
      "rom_address": "0x09092470",
      "encoded_sha256": "349a591c85d987655c08a857032d2462cf6378db02fd937097c21cd97e33002c",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10389 行 · item / 132 · 

判定：`fixed_verified`

理由：ひき指个体计数，不是物种数量。

日文：

```text
3ひきの　ポケモンが
プリントされた　びんせん
ポケモンに　もたせる
```

英文：

```text
MAIL featuring the
drawings of three
POKéMON.
```

报告原中文：

```text
印有三种宝可梦的
信纸，可以让宝可
梦携带
```

修复前实际中文：

```text
印有三种宝可梦的
信纸，可以让宝可
梦携带
```

最终中文：

```text
印有三只宝可梦的
信纸，可以让宝可
梦携带
```

证据：

```json
{
  "review": {
    "row_number": 10389,
    "symbol": "",
    "domain": "item",
    "idx": "132",
    "old": "三种宝可梦",
    "new": "三只宝可梦",
    "reason": "ひき指个体计数，不是物种数量。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "sRetroMailDesc",
    "final_text": "印有三只宝可梦的\n信纸，可以让宝可\n梦携带",
    "old_current_text": "印有三种宝可梦的\n信纸，可以让宝可\n梦携带",
    "changed_files": [
      "patch/item_descriptions.json",
      "../pokeemerald_us_chs/src/data/text/item_descriptions.h"
    ],
    "us_source_file": "src/data/text/item_descriptions.h",
    "jp_source": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "3ひきの　ポケモンが\nプリントされた　びんせん\nポケモンに　もたせる"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "印有三只宝可梦的\n信纸，可以让宝可\n梦携带"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "3ひきの　ポケモンが\nプリントされた　びんせん\nポケモンに　もたせる"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 132,
      "text": "印有三只宝可梦的\n信纸，可以让宝可\n梦携带",
      "rom_address": "0x09092568",
      "encoded_sha256": "c7154bcad3ff058e3162530a95345c229b497687415182928aa865a510667e62",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10399 行 · item / 142 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
もたせると　じぶんで
たいりょくを
30　かいふくする
```

英文：

```text
A hold item that
restores 30 HP in
battle.
```

报告原中文：

```text
携带后，可以回复
少量HP
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10399,
    "symbol": "",
    "domain": "item",
    "idx": "142",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 142,
      "text": "携带后，可以回复\n少量HP",
      "rom_address": "0x09092674",
      "encoded_sha256": "9069dc4e3c0d0b5ceb5e91fe8828399ef578402ff87be02d437a89b1ae5115a9",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10400 行 · item / 143 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
もたせると　たいりょくを
かいふく　できるが
こんらんする　ことがある
```

英文：

```text
A hold item that
restores HP but
may confuse.
```

报告原中文：

```text
携带后危机时可以
回复HP。如果
讨厌味道会混乱
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10400,
    "symbol": "",
    "domain": "item",
    "idx": "143",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 143,
      "text": "携带后危机时可以\n回复HP。如果\n讨厌味道会混乱",
      "rom_address": "0x09092690",
      "encoded_sha256": "00f0f8baf6db8519c58b2f536d5aa89f582fd2415ff03cd9960b35847cbc10b8",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10401 行 · item / 144 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
もたせると　たいりょくを
かいふく　できるが
こんらんする　ことがある
```

英文：

```text
A hold item that
restores HP but
may confuse.
```

报告原中文：

```text
携带后危机时可以
回复HP。如果
讨厌味道会混乱
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10401,
    "symbol": "",
    "domain": "item",
    "idx": "144",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 144,
      "text": "携带后危机时可以\n回复HP。如果\n讨厌味道会混乱",
      "rom_address": "0x090926C0",
      "encoded_sha256": "00f0f8baf6db8519c58b2f536d5aa89f582fd2415ff03cd9960b35847cbc10b8",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10402 行 · item / 145 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
もたせると　たいりょくを
かいふく　できるが
こんらんする　ことがある
```

英文：

```text
A hold item that
restores HP but
may confuse.
```

报告原中文：

```text
携带后危机时可以
回复HP。如果
讨厌味道会混乱
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10402,
    "symbol": "",
    "domain": "item",
    "idx": "145",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 145,
      "text": "携带后危机时可以\n回复HP。如果\n讨厌味道会混乱",
      "rom_address": "0x090926F0",
      "encoded_sha256": "00f0f8baf6db8519c58b2f536d5aa89f582fd2415ff03cd9960b35847cbc10b8",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10403 行 · item / 146 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
もたせると　たいりょくを
かいふく　できるが
こんらんする　ことがある
```

英文：

```text
A hold item that
restores HP but
may confuse.
```

报告原中文：

```text
携带后危机时可以
回复HP。如果
讨厌味道会混乱
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10403,
    "symbol": "",
    "domain": "item",
    "idx": "146",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 146,
      "text": "携带后危机时可以\n回复HP。如果\n讨厌味道会混乱",
      "rom_address": "0x09092720",
      "encoded_sha256": "00f0f8baf6db8519c58b2f536d5aa89f582fd2415ff03cd9960b35847cbc10b8",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10404 行 · item / 147 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
もたせると　たいりょくを
かいふく　できるが
こんらんする　ことがある
```

英文：

```text
A hold item that
restores HP but
may confuse.
```

报告原中文：

```text
携带后危机时可以
回复HP。如果
讨厌味道会混乱
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10404,
    "symbol": "",
    "domain": "item",
    "idx": "147",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 147,
      "text": "携带后危机时可以\n回复HP。如果\n讨厌味道会混乱",
      "rom_address": "0x09092750",
      "encoded_sha256": "00f0f8baf6db8519c58b2f536d5aa89f582fd2415ff03cd9960b35847cbc10b8",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10437 行 · item / 180 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
ポケモンに　もたせると
さがった　のうりょくを
もとにもどす
```

英文：

```text
A hold item that
restores any
lowered stat.
```

报告原中文：

```text
当携带宝可梦能力
降低时，仅能回到
之前的状态1次
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10437,
    "symbol": "",
    "domain": "item",
    "idx": "180",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 180,
      "text": "当携带宝可梦能力\n降低时，仅能回到\n之前的状态1次",
      "rom_address": "0x09092CB8",
      "encoded_sha256": "ad76d1cfd815178d05c975826296534edead3ba5872c5d629b1151931962c828",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10442 行 · item / 185 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
もたせた　ポケモンが
メロメロに　なったとき
なおして　くれる
```

英文：

```text
A hold item that
snaps POKéMON out
of infatuation.
```

报告原中文：

```text
携带后，会解除着
迷状态。只能使用
1次
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10442,
    "symbol": "",
    "domain": "item",
    "idx": "185",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 185,
      "text": "携带后，会解除着\n迷状态。只能使用\n1次",
      "rom_address": "0x09092DA8",
      "encoded_sha256": "ed18e654050bc2577ec6cd40cf08832161b617a300721f9eecd17c20ff4349ad",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10447 行 · item / 190 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
ポケモンに　もたせると
やせいの　ポケモンに
そうぐう　しにくく　なる
```

英文：

```text
A hold item that
helps repel wild
POKéMON.
```

报告原中文：

```text
让最前排的宝可
梦携带，野生宝可
梦就会不易出现
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10447,
    "symbol": "",
    "domain": "item",
    "idx": "190",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 190,
      "text": "让最前排的宝可\n梦携带，野生宝可\n梦就会不易出现",
      "rom_address": "0x09092E9C",
      "encoded_sha256": "f6c805590509e1f10454cd8e7dc77cad3f11ded951578170b38eae9fe5eaf79b",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10475 行 · item / 218 · 

判定：`fixed_verified`

理由：按JP/EN原文，仅修文本不改用途。

日文：

```text
ふしぎな　はこ
シルフ　カンパニーせい
```

英文：

```text
A peculiar box made
by SILPH CO.
```

报告原中文：

```text
内部储存了各种信
息的透明机器。西
尔佛公司制造
```

修复前实际中文：

```text
内部储存了各种信
息的透明机器。西
尔佛公司制造
```

最终中文：

```text
不可思议的盒子。
西尔佛公司制造
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "不可思议的盒子。\n西尔佛公司制造"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "ふしぎな　はこ\nシルフ　カンパニーせい"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 218,
      "text": "不可思议的盒子。\n西尔佛公司制造",
      "rom_address": "0x090933C8",
      "encoded_sha256": "4a1936c844cfa0f8234aa64a4b3ec0e675d5cca9130228d62be4a86aa0d5afc6",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10477 行 · item / 220 · 

判定：`fixed_verified`

理由：恢复すこしだけ的程度限定。

日文：

```text
ポケモンに　もたせると
すこしだけ　みずタイプの
わざのいりょくが　あがる
```

英文：

```text
A hold item that
slightly boosts
WATER-type moves.
```

报告原中文：

```text
香气神奇的薰香。
携带后，水属性的
招式会增强
```

修复前实际中文：

```text
香气神奇的薰香。
携带后，水属性的
招式会增强
```

最终中文：

```text
香气神奇的薰香。
携带后，水属性的
招式会稍微增强
```

证据：

```json
{
  "review": {
    "row_number": 10477,
    "symbol": "",
    "domain": "item",
    "idx": "220",
    "old": "水属性的\n招式会增强",
    "new": "水属性的\n招式会稍微增强",
    "reason": "恢复すこしだけ的程度限定。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "sSeaIncenseDesc",
    "final_text": "香气神奇的薰香。\n携带后，水属性的\n招式会稍微增强",
    "old_current_text": "香气神奇的薰香。\n携带后，水属性的\n招式会增强",
    "changed_files": [
      "patch/item_descriptions.json",
      "../pokeemerald_us_chs/src/data/text/item_descriptions.h"
    ],
    "us_source_file": "src/data/text/item_descriptions.h",
    "jp_source": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "ポケモンに　もたせると\nすこしだけ　みずタイプの\nわざのいりょくが　あがる"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "香气神奇的薰香。\n携带后，水属性的\n招式会稍微增强"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "ポケモンに　もたせると\nすこしだけ　みずタイプの\nわざのいりょくが　あがる"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 220,
      "text": "香气神奇的薰香。\n携带后，水属性的\n招式会稍微增强",
      "rom_address": "0x09093418",
      "encoded_sha256": "d636f0ac9e0de55616e7515994ae6d1d2313990c20371a76fe5cf2d4dd6f22a4",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10478 行 · item / 221 · 

判定：`fixed_verified`

理由：恢复稍微；不写死百分比。

日文：

```text
ポケモンに　もたせると
てきの　めいちゅうりつを
すこしだけ　さげる
```

英文：

```text
A hold item that
slightly lowers the
foe's accuracy.
```

报告原中文：

```text
携带后，对手招式
会变得不容易命中

```

修复前实际中文：

```text
携带后，对手招式
会变得不容易命中

```

最终中文：

```text
携带后，对手招式
会稍微变得难命中

```

证据：

```json
{
  "review": {
    "row_number": 10478,
    "symbol": "",
    "domain": "item",
    "idx": "221",
    "old": "对手招式\n会变得不容易命中",
    "new": "对手招式\n会稍微变得难命中",
    "reason": "恢复稍微；不写死百分比。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "sLaxIncenseDesc",
    "final_text": "携带后，对手招式\n会稍微变得难命中\n",
    "old_current_text": "携带后，对手招式\n会变得不容易命中\n",
    "changed_files": [
      "patch/item_descriptions.json",
      "../pokeemerald_us_chs/src/data/text/item_descriptions.h"
    ],
    "us_source_file": "src/data/text/item_descriptions.h",
    "jp_source": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "ポケモンに　もたせると\nてきの　めいちゅうりつを\nすこしだけ　さげる"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "携带后，对手招式\n会稍微变得难命中\n"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "ポケモンに　もたせると\nてきの　めいちゅうりつを\nすこしだけ　さげる"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 221,
      "text": "携带后，对手招式\n会稍微变得难命中\n",
      "rom_address": "0x0909344C",
      "encoded_sha256": "7b5ff7af4fab699aba46d661473e875113f06a5eda6041efdb049a19f1b300f1",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10520 行 · item / 263 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
ポケモンを　つるどうぐ
なかなかの　つりざおと
いわれている
```

英文：

```text
A decent fishing
rod for catching
wild POKéMON.
```

报告原中文：

```text
不错的新钓竿。在
有水的地方可以钓
到宝可梦
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10520,
    "symbol": "",
    "domain": "item",
    "idx": "263",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 263,
      "text": "不错的新钓竿。在\n有水的地方可以钓\n到宝可梦",
      "rom_address": "0x090937B8",
      "encoded_sha256": "6ccf7ee4a70e7d21f9c89df9b5acd528a0901e40d079bf8a1e8f3f1079678d3a",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10521 行 · item / 264 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
ポケモンを　つるどうぐ
さいこうの　つりざおと
いわれている
```

英文：

```text
The best fishing
rod for catching
wild POKéMON.
```

报告原中文：

```text
最新的厉害钓竿。
在有水的地方可以
钓到宝可梦
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10521,
    "symbol": "",
    "domain": "item",
    "idx": "264",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 264,
      "text": "最新的厉害钓竿。\n在有水的地方可以\n钓到宝可梦",
      "rom_address": "0x090937E8",
      "encoded_sha256": "5031f79903b992402471489b2cc5bcff772641287f72126862e4e74dd192103e",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10533 行 · item / 276 · 

判定：`fixed_verified`

理由：原文明确说内含古代力量。

日文：

```text
おおむかしの　ちからが
こめられている　という
あかく　かがやく　たま
```

英文：

```text
A red, glowing orb
said to contain an
ancient power.
```

报告原中文：

```text
散发着红色光辉的
宝珠。据说和丰缘
传说渊源颇深
```

修复前实际中文：

```text
散发着红色光辉的
宝珠。据说和丰缘
传说渊源颇深
```

最终中文：

```text
散发着红色光辉的
宝珠。据说蕴含着
超古代的力量
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "散发着红色光辉的\n宝珠。据说蕴含着\n超古代的力量"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "おおむかしの　ちからが\nこめられている　という\nあかく　かがやく　たま"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 276,
      "text": "散发着红色光辉的\n宝珠。据说蕴含着\n超古代的力量",
      "rom_address": "0x0909398C",
      "encoded_sha256": "90160c4520926af2db87bbbaafdd90e80217bc756eaaee061369bb6122a96fe9",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10534 行 · item / 277 · 

判定：`fixed_verified`

理由：原文明确说内含古代力量。

日文：

```text
おおむかしの　ちからが
こめられている　という
あおく　かがやく　たま
```

英文：

```text
A blue, glowing orb
said to contain an
ancient power.
```

报告原中文：

```text
散发着蓝色光辉的
宝珠。据说和丰缘
传说渊源颇深
```

修复前实际中文：

```text
散发着蓝色光辉的
宝珠。据说和丰缘
传说渊源颇深
```

最终中文：

```text
散发着蓝色光辉的
宝珠。据说蕴含着
超古代的力量
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "散发着蓝色光辉的\n宝珠。据说蕴含着\n超古代的力量"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "おおむかしの　ちからが\nこめられている　という\nあおく　かがやく　たま"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 277,
      "text": "散发着蓝色光辉的\n宝珠。据说蕴含着\n超古代的力量",
      "rom_address": "0x090939C0",
      "encoded_sha256": "1d9fc48d4e4070ed085d77f9d367b6e1d8b4e71aeb90e0d1bf546e7f886b4092",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10545 行 · item / 288 · 

判定：`fixed_verified`

理由：恢复おとをだす发出声音的作用。

日文：

```text
みえない　ポケモンに
はんのうして　おとをだす
デボンの　とくせいひん
```

英文：

```text
A device by DEVON
that signals any
unseeable POKéMON.
```

报告原中文：

```text
会对看不见的宝可
梦起反应的得文特
制产品
```

修复前实际中文：

```text
会对看不见的宝可
梦起反应的得文特
制产品
```

最终中文：

```text
会对看不见的宝可
梦起反应并发声的
得文特制产品
```

证据：

```json
{
  "review": {
    "row_number": 10545,
    "symbol": "",
    "domain": "item",
    "idx": "288",
    "old": "起反应的得文特\n制产品",
    "new": "起反应并发声的\n得文特制产品",
    "reason": "恢复おとをだす发出声音的作用。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "sDevonScopeDesc",
    "final_text": "会对看不见的宝可\n梦起反应并发声的\n得文特制产品",
    "old_current_text": "会对看不见的宝可\n梦起反应的得文特\n制产品",
    "changed_files": [
      "patch/item_descriptions.json",
      "../pokeemerald_us_chs/src/data/text/item_descriptions.h"
    ],
    "us_source_file": "src/data/text/item_descriptions.h",
    "jp_source": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "みえない　ポケモンに\nはんのうして　おとをだす\nデボンの　とくせいひん"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "会对看不见的宝可\n梦起反应并发声的\n得文特制产品"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "みえない　ポケモンに\nはんのうして　おとをだす\nデボンの　とくせいひん"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 288,
      "text": "会对看不见的宝可\n梦起反应并发声的\n得文特制产品",
      "rom_address": "0x09093B48",
      "encoded_sha256": "291e97c29eebf3621235afbe9a9b703d88a3e72f735164c8c1960238d1e1ee53",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10555 行 · item / 298 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
ポケモンによって　てきに
あたえる　ダメージの
りょうが　へんかする
```

英文：

```text

```

报告原中文：

```text
招式的威力和属性
会随着使用它的
宝可梦而改变
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10555,
    "symbol": "",
    "domain": "item",
    "idx": "298",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 298,
      "text": "招式的威力和属性\n会随着使用它的\n宝可梦而改变",
      "rom_address": "0x09093D14",
      "encoded_sha256": "606ce446caf67a52d1e38d1839769b57cd412fe0661e1a99627504fe3b1f1589",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10571 行 · item / 314 · 

判定：`accurate_clarification`

理由：地震攻击范围说明符合机制；飞行免疫由战斗属性机制判定，非说明必须完整枚举的条件。

日文：

```text
じめんを　つよく　ゆらす
とんでいる　てきいがいに
だいダメージを　あたえる
```

英文：

```text

```

报告原中文：

```text
利用地震的冲击，
攻击自己周围
所有的宝可梦
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10571,
    "symbol": "",
    "domain": "item",
    "idx": "314",
    "reason": "地震攻击范围说明符合机制；飞行免疫由战斗属性机制判定，非说明必须完整枚举的条件。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 314,
      "text": "利用地震的冲击，\n攻击自己周围\n所有的宝可梦",
      "rom_address": "0x09094024",
      "encoded_sha256": "e206c3fb3d03d436f70bd7be244dfb13f883d32d87684e1055bd7e1b5c38f51c",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10609 行 · item / 352 · 

判定：`fixed_verified`

理由：修复给店的病句，恢复券及折叠自行车。

日文：

```text
ミラクル·サイクルで
おりたたみ　じてんしゃと
こうかん　できる　かみ
```

英文：

```text
A voucher for
obtaining a bicycle
from the BIKE SHOP.
```

报告原中文：

```text
给华蓝市的奇迹自
行车店就能交换得
到自行车
```

修复前实际中文：

```text
给华蓝市的奇迹自
行车店就能交换得
到自行车
```

最终中文：

```text
可在华蓝市的奇迹
自行车店兑换折叠
自行车的纸券
```

证据：

```json
{
  "review": {
    "row_number": 10609,
    "symbol": "",
    "domain": "item",
    "idx": "352",
    "old": "给华蓝市的奇迹自\n行车店就能交换得\n到自行车",
    "new": "可在华蓝市的奇迹\n自行车店兑换折叠\n自行车的纸券",
    "reason": "修复给店的病句，恢复券及折叠自行车。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "sBikeVoucherDesc",
    "final_text": "可在华蓝市的奇迹\n自行车店兑换折叠\n自行车的纸券",
    "old_current_text": "给华蓝市的奇迹自\n行车店就能交换得\n到自行车",
    "changed_files": [
      "patch/item_descriptions.json",
      "../pokeemerald_us_chs/src/data/text/item_descriptions.h"
    ],
    "us_source_file": "src/data/text/item_descriptions.h",
    "jp_source": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "ミラクル·サイクルで\nおりたたみ　じてんしゃと\nこうかん　できる　かみ"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "可在华蓝市的奇迹\n自行车店兑换折叠\n自行车的纸券"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "ミラクル·サイクルで\nおりたたみ　じてんしゃと\nこうかん　できる　かみ"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 352,
      "text": "可在华蓝市的奇迹\n自行车店兑换折叠\n自行车的纸券",
      "rom_address": "0x090946B4",
      "encoded_sha256": "846f40bb91eec6953cb78b7ed9c9696ddc453f6b8dbe216b566bd797a037d879",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10612 行 · item / 355 · 

判定：`fixed_verified`

理由：多余的导致病句。

日文：

```text
カードで　できた　カギ
シルフカンパニー　ビルの
ドアロックを　はずせる
```

英文：

```text
A card-type door
key used in SILPH
CO's office.
```

报告原中文：

```text
用来打开的西尔佛
公司总部大厦门锁
的卡片式钥匙
```

修复前实际中文：

```text
用来打开的西尔佛
公司总部大厦门锁
的卡片式钥匙
```

最终中文：

```text
能打开西尔佛公司
大厦门锁的卡片式
钥匙
```

证据：

```json
{
  "review": {
    "row_number": 10612,
    "symbol": "",
    "domain": "item",
    "idx": "355",
    "old": "用来打开的西尔佛\n公司总部大厦门锁\n的卡片式钥匙",
    "new": "能打开西尔佛公司\n大厦门锁的卡片式\n钥匙",
    "reason": "多余的导致病句。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "sCardKeyDesc",
    "final_text": "能打开西尔佛公司\n大厦门锁的卡片式\n钥匙",
    "old_current_text": "用来打开的西尔佛\n公司总部大厦门锁\n的卡片式钥匙",
    "changed_files": [
      "patch/item_descriptions.json",
      "../pokeemerald_us_chs/src/data/text/item_descriptions.h"
    ],
    "us_source_file": "src/data/text/item_descriptions.h",
    "jp_source": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "カードで　できた　カギ\nシルフカンパニー　ビルの\nドアロックを　はずせる"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "能打开西尔佛公司\n大厦门锁的卡片式\n钥匙"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "カードで　できた　カギ\nシルフカンパニー　ビルの\nドアロックを　はずせる"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 355,
      "text": "能打开西尔佛公司\n大厦门锁的卡片式\n钥匙",
      "rom_address": "0x0909472C",
      "encoded_sha256": "73c86ea7e1fa7daeadb4cded4ed2b6f71ef63b9939a7fa9878a43384879ef883",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10620 行 · item / 363 · 

判定：`fixed_verified`

理由：じょうほう是信息，不是东西。

日文：

```text
ゆうめいな　じんぶつの
じょうほうを　いつでも
みなおすことが　できる
```

英文：

```text
Stores information
on famous people
for instant recall.
```

报告原中文：

```text
可以重复查看打听
到的有名人物的东
西
```

修复前实际中文：

```text
可以重复查看打听
到的有名人物的东
西
```

最终中文：

```text
可以重复查看打听
到的有名人物的信
息
```

证据：

```json
{
  "review": {
    "row_number": 10620,
    "symbol": "",
    "domain": "item",
    "idx": "363",
    "old": "有名人物的东\n西",
    "new": "有名人物的信\n息",
    "reason": "じょうほう是信息，不是东西。",
    "scope": "both",
    "action": "fix",
    "resolved_symbol": "sFameCheckerDesc",
    "final_text": "可以重复查看打听\n到的有名人物的信\n息",
    "old_current_text": "可以重复查看打听\n到的有名人物的东\n西",
    "changed_files": [
      "patch/item_descriptions.json",
      "../pokeemerald_us_chs/src/data/text/item_descriptions.h"
    ],
    "us_source_file": "src/data/text/item_descriptions.h",
    "jp_source": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "ゆうめいな　じんぶつの\nじょうほうを　いつでも\nみなおすことが　できる"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "可以重复查看打听\n到的有名人物的信\n息"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/text/item_descriptions.h",
        "text": "ゆうめいな　じんぶつの\nじょうほうを　いつでも\nみなおすことが　できる"
      }
    ]
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 363,
      "text": "可以重复查看打听\n到的有名人物的信\n息",
      "rom_address": "0x09094890",
      "encoded_sha256": "fc21dfac22df8ae1f80db9efbe810a4a90e5b002f188be73063ed0da6ce387cd",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 10623 行 · item / 366 · 

判定：`accurate_clarification`

理由：准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。

日文：

```text
トレーナーの　やくにたつ
ばんぐみを　みることが
できる　テレビ
```

英文：

```text
A TV set tuned to
an advice program
for TRAINERS.
```

报告原中文：

```text
可以收看对新手训
练家有帮助的节目
的电视
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 10623,
    "symbol": "",
    "domain": "item",
    "idx": "366",
    "reason": "准确的机制说明或不影响功能理解的修饰；不为原文未逐字列出而删改。",
    "action": "accurate_clarification"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/item_descriptions.json",
      "table": "ChsItemDescriptions",
      "index": 366,
      "text": "可以收看对新手训\n练家有帮助的节目\n的电视",
      "rom_address": "0x09094920",
      "encoded_sha256": "85f868a6e07d2a5c36c8e0556ef3702e71f47a5a431578198f8b26bd587ebe30",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 12011 行 · untransplanted_full /  · BattlePyramid_Text_SevenTrainersRemaining2

判定：`fixed_verified`

理由：原文有人会打败玩家，不是比玩家弱。

日文：

```text
くやしいー！\pでも　あと　7にん　いる　トレーナーが\nきっと　たおしてくれるわ$
```

英文：

```text
This is so upsetting!\pBut there are seven TRAINERS left!\nSomeone will humble you!$
```

报告原中文：

```text
真不幸！\p后面还有7位训练家！\n他们中或许有人比你弱！$
```

修复前实际中文：

```text
真不幸！\p后面还有7位训练家！
他们中或许有人比你弱！
```

最终中文：

```text
真不幸！\p后面还有7位训练家！
他们中一定有人能打败你！
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "真不幸！\\p后面还有7位训练家！\n他们中一定有人能打败你！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "くやしいー！\\pでも　あと　7にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_BattlePyramid_Text_SevenTrainersRemaining2",
      "file": "patch/batches/437_checklist_reviewed_indirect_tables.json",
      "payload_address": "0x09087E3C",
      "payload_sha256": "6cfa619b4b5f355020bc104821310bce84755d57831b6f3cd5d23922a9ace785",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085DF55C",
          "original": "0x0822E3D9",
          "target": "0x09087E3C",
          "batch": "patch/batches/437_checklist_reviewed_indirect_tables.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12012 行 · untransplanted_full /  · BattlePyramid_Text_SixTrainersRemaining2

判定：`fixed_verified`

理由：原文有人会打败玩家，不是比玩家弱。

日文：

```text
くやしいー！\pでも　あと　6にん　いる　トレーナーが\nきっと　たおしてくれるわ$
```

英文：

```text
This is so upsetting!\pBut there are six TRAINERS left!\nSomeone will humble you!$
```

报告原中文：

```text
真不幸！\p后面还有6位训练家！\n他们中或许有人比你弱！$
```

修复前实际中文：

```text
真不幸！\p后面还有6位训练家！
他们中或许有人比你弱！
```

最终中文：

```text
真不幸！\p后面还有6位训练家！
他们中一定有人能打败你！
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "真不幸！\\p后面还有6位训练家！\n他们中一定有人能打败你！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "くやしいー！\\pでも　あと　6にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_BattlePyramid_Text_SixTrainersRemaining2",
      "file": "patch/batches/437_checklist_reviewed_indirect_tables.json",
      "payload_address": "0x0908808C",
      "payload_sha256": "44353cb52ef4e1f428d0ca4eda7ef0fba0a57dc05a50bdd6ead36c8a4af0a69a",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085DF558",
          "original": "0x0822E401",
          "target": "0x0908808C",
          "batch": "patch/batches/437_checklist_reviewed_indirect_tables.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12013 行 · untransplanted_full /  · BattlePyramid_Text_FiveTrainersRemaining2

判定：`fixed_verified`

理由：原文有人会打败玩家，不是比玩家弱。

日文：

```text
くやしいー！\pでも　あと　5にん　いる　トレーナーが\nきっと　たおしてくれるわ$
```

英文：

```text
This is so upsetting!\pBut there are five TRAINERS left!\nSomeone will humble you!$
```

报告原中文：

```text
真不幸！\p后面还有5位训练家！\n他们中或许有人比你弱！$
```

修复前实际中文：

```text
真不幸！\p后面还有5位训练家！
他们中或许有人比你弱！
```

最终中文：

```text
真不幸！\p后面还有5位训练家！
他们中一定有人能打败你！
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "真不幸！\\p后面还有5位训练家！\n他们中一定有人能打败你！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "くやしいー！\\pでも　あと　5にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_BattlePyramid_Text_FiveTrainersRemaining2",
      "file": "patch/batches/437_checklist_reviewed_indirect_tables.json",
      "payload_address": "0x0908774E",
      "payload_sha256": "ab8f5b2ab81f858ef75d5db192dc02611dd674e7c606c599a032e9687d169fdb",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085DF554",
          "original": "0x0822E429",
          "target": "0x0908774E",
          "batch": "patch/batches/437_checklist_reviewed_indirect_tables.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12014 行 · untransplanted_full /  · BattlePyramid_Text_FourTrainersRemaining2

判定：`fixed_verified`

理由：原文有人会打败玩家，不是比玩家弱。

日文：

```text
くやしいー！\pでも　あと　4にん　いる　トレーナーが\nきっと　たおしてくれるわ$
```

英文：

```text
This is so upsetting!\pBut there are four TRAINERS left!\nSomeone will humble you!$
```

报告原中文：

```text
真不幸！\p后面还有4位训练家！\n他们中或许有人比你弱！$
```

修复前实际中文：

```text
真不幸！\p后面还有4位训练家！
他们中或许有人比你弱！
```

最终中文：

```text
真不幸！\p后面还有4位训练家！
他们中一定有人能打败你！
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "真不幸！\\p后面还有4位训练家！\n他们中一定有人能打败你！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "くやしいー！\\pでも　あと　4にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_BattlePyramid_Text_FourTrainersRemaining2",
      "file": "patch/batches/437_checklist_reviewed_indirect_tables.json",
      "payload_address": "0x0908799E",
      "payload_sha256": "7f5878b0c65e7ce92273ef4ceae54efdc7147cc6452050169156524469e68009",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085DF550",
          "original": "0x0822E451",
          "target": "0x0908799E",
          "batch": "patch/batches/437_checklist_reviewed_indirect_tables.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12015 行 · untransplanted_full /  · BattlePyramid_Text_ThreeTrainersRemaining2

判定：`fixed_verified`

理由：原文有人会打败玩家，不是比玩家弱。

日文：

```text
くやしいー！\pでも　あと　3にん　いる　トレーナーが\nきっと　たおしてくれるわ$
```

英文：

```text
This is so upsetting!\pBut there are three TRAINERS left!\nSomeone will humble you!$
```

报告原中文：

```text
真不幸！\p后面还有3位训练家！\n他们中或许有人比你弱！$
```

修复前实际中文：

```text
真不幸！\p后面还有3位训练家！
他们中或许有人比你弱！
```

最终中文：

```text
真不幸！\p后面还有3位训练家！
他们中一定有人能打败你！
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "真不幸！\\p后面还有3位训练家！\n他们中一定有人能打败你！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "くやしいー！\\pでも　あと　3にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_BattlePyramid_Text_ThreeTrainersRemaining2",
      "file": "patch/batches/437_checklist_reviewed_indirect_tables.json",
      "payload_address": "0x090882DC",
      "payload_sha256": "fbbddf7df8448f6d0a8357ed3abc2c99219d8a4a2a9fc5b24af0b940f66d00a9",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085DF54C",
          "original": "0x0822E479",
          "target": "0x090882DC",
          "batch": "patch/batches/437_checklist_reviewed_indirect_tables.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12016 行 · untransplanted_full /  · BattlePyramid_Text_TwoTrainersRemaining2

判定：`fixed_verified`

理由：原文有人会打败玩家，不是比玩家弱。

日文：

```text
くやしいー！\pでも　あと　2にん　いる　トレーナーが\nきっと　たおしてくれるわ$
```

英文：

```text
This is so upsetting!\pBut there are two TRAINERS left!\nSomeone will humble you!$
```

报告原中文：

```text
真不幸！\p后面还有2位训练家！\n他们中或许有人比你弱！$
```

修复前实际中文：

```text
真不幸！\p后面还有2位训练家！
他们中或许有人比你弱！
```

最终中文：

```text
真不幸！\p后面还有2位训练家！
他们中一定有人能打败你！
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "真不幸！\\p后面还有2位训练家！\n他们中一定有人能打败你！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "くやしいー！\\pでも　あと　2にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_BattlePyramid_Text_TwoTrainersRemaining2",
      "file": "patch/batches/437_checklist_reviewed_indirect_tables.json",
      "payload_address": "0x0908852A",
      "payload_sha256": "815c5c7f4e8d6bc28e4ee6cc9e3a69f42c8ddfbd493092700128a4553083f7cb",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085DF548",
          "original": "0x0822E4A1",
          "target": "0x0908852A",
          "batch": "patch/batches/437_checklist_reviewed_indirect_tables.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12017 行 · untransplanted_full /  · BattlePyramid_Text_OneTrainersRemaining2

判定：`fixed_verified`

理由：同系列单人模板恢复原意。

日文：

```text
くやしいー！\pでも　あと　1にん　いる　トレーナーが\nきっと　たおしてくれるわ$
```

英文：

```text
This is so upsetting!\pBut there's one TRAINER left!\nI'm sure you will be humbled!$
```

报告原中文：

```text
真不幸！\p后面还有1位训练家！\n他或许比你弱！$
```

修复前实际中文：

```text
真不幸！\p后面还有1位训练家！
他或许比你弱！
```

最终中文：

```text
真不幸！\p后面还有1位训练家！
他一定会打败你！
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "真不幸！\\p后面还有1位训练家！\n他一定会打败你！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_BattlePyramidFloor/scripts.inc",
        "text": "くやしいー！\\pでも　あと　1にん　いる　トレーナーが\nきっと　たおしてくれるわ$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_BattlePyramid_Text_OneTrainersRemaining2",
      "file": "patch/batches/437_checklist_reviewed_indirect_tables.json",
      "payload_address": "0x09087BF6",
      "payload_sha256": "77f9fa89fe5d025d323a4309d615f216d3eee5831d5a6111c94f34056f1e4f31",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085DF544",
          "original": "0x0822E4C9",
          "target": "0x09087BF6",
          "batch": "patch/batches/437_checklist_reviewed_indirect_tables.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12056 行 · untransplanted_full /  · BattleFrontier_Lounge2_Text_SalonMaidenIsThere

判定：`fixed_verified`

理由：统一同系列Frontier Brains术语。

日文：

```text
しってるかい？\pあそこは　エニシダが\nフロンティアブレーンって　よんでる\lトレーナーの　うちの　ひとり⋯⋯\lタワータイクーンって　いう\lなぞの　トレーナーが　おさめてるのさ！$
```

英文：

```text
Bet you didn't know this!\pOne of those top TRAINERS that SCOTT\ncalls the FRONTIER BRAINS is there.\pIt's this mysterious TRAINER called\nthe SALON MAIDEN that runs the place.$
```

报告原中文：

```text
告诉你个秘密！\p被亚希达称作开拓区大脑\n的顶级训练家之一现在就在那里。\p那里就是由那个名叫对战塔大君的\n神秘的训练家所掌管的。$
```

修复前实际中文：

```text
告诉你个秘密！\p被亚希达称作开拓区大脑
的顶级训练家之一现在就在那里。\p那里就是由那个名叫对战塔大君的
神秘的训练家所掌管的。
```

最终中文：

```text
告诉你个秘密！\p被亚希达称作开拓之脑
的顶级训练家之一现在就在那里。\p那里就是由那个名叫对战塔大君的
神秘的训练家所掌管的。
```

证据：

```json
{
  "review": {
    "row_number": 12056,
    "symbol": "BattleFrontier_Lounge2_Text_SalonMaidenIsThere",
    "domain": "untransplanted_full",
    "idx": "",
    "old": "开拓区大脑",
    "new": "开拓之脑",
    "reason": "统一同系列Frontier Brains术语。",
    "scope": "both",
    "action": "fix",
    "final_text": "告诉你个秘密！\\p被亚希达称作开拓之脑\n的顶级训练家之一现在就在那里。\\p那里就是由那个名叫对战塔大君的\n神秘的训练家所掌管的。",
    "old_current_text": "告诉你个秘密！\\p被亚希达称作开拓区大脑\n的顶级训练家之一现在就在那里。\\p那里就是由那个名叫对战塔大君的\n神秘的训练家所掌管的。",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/BattleFrontier_Lounge2/scripts.inc",
      "patch/batches/437_checklist_reviewed_indirect_tables.json"
    ],
    "us_source_file": "data/maps/BattleFrontier_Lounge2/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/BattleFrontier_Lounge2/scripts.inc",
        "text": "しってるかい？\\pあそこは　エニシダが\nフロンティアブレーンって　よんでる\\lトレーナーの　うちの　ひとり⋯⋯\\lタワータイクーンって　いう\\lなぞの　トレーナーが　おさめてるのさ！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/BattleFrontier_Lounge2/scripts.inc",
        "text": "告诉你个秘密！\\p被亚希达称作开拓之脑\n的顶级训练家之一现在就在那里。\\p那里就是由那个名叫对战塔大君的\n神秘的训练家所掌管的。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/BattleFrontier_Lounge2/scripts.inc",
        "text": "しってるかい？\\pあそこは　エニシダが\nフロンティアブレーンって　よんでる\\lトレーナーの　うちの　ひとり⋯⋯\\lタワータイクーンって　いう\\lなぞの　トレーナーが　おさめてるのさ！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_BattleFrontier_Lounge2_Text_SalonMaidenIsThere",
      "file": "patch/batches/437_checklist_reviewed_indirect_tables.json",
      "payload_address": "0x0908713B",
      "payload_sha256": "b7ea14816439f03548a2c9671002d9aa367eee011c72eebb2c8e5c0433d30d73",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x085926AC",
          "original": "0x08236C08",
          "target": "0x0908713B",
          "batch": "patch/batches/437_checklist_reviewed_indirect_tables.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12178 行 · untransplanted_full /  · MagmaHideout_4F_Text_MaxieAwakenGroudon

判定：`fixed_verified`

理由：多余的。

日文：

```text
マツブサ“マグマに　ねむる　グラードンよ\nなにをしても　めざめなかった　おまえが\lもとめて　いたのは　あいいろのたま⋯⋯\pそうなんだろう？\pさあ　ここに　もってきて　やったぞ\nこの　かがやきで　めを　さませ！\pそして　ほんとうの　ちからを\nわたしに　みせて　おくれ！$
```

英文：

```text
MAXIE: GROUDON…\pNothing could awaken you from your\nsleep bathed in magma…\pThis BLUE ORB is what you sought.\nWasn't it?\pI have brought you the BLUE ORB.\nLet its shine awaken you!\pAnd show me…\nShow me the full extent of your power!$
```

报告原中文：

```text
赤焰松：固拉多……\p无论怎样也不会\n从岩浆中苏醒的你……\p一直在寻求的，\n是这个靛蓝色宝珠吧？\p我已带来了靛蓝色宝珠。\n就让它的光芒唤醒你吧！\p向我展示……\n展示的你全部的力量吧！$
```

修复前实际中文：

```text
赤焰松：固拉多……\p无论怎样也不会
从岩浆中苏醒的你……\p一直在寻求的，
是这个靛蓝色宝珠吧？\p我已带来了靛蓝色宝珠。
就让它的光芒唤醒你吧！\p向我展示……
展示的你全部的力量吧！
```

最终中文：

```text
赤焰松：固拉多……\p无论怎样也不会
从岩浆中苏醒的你……\p一直在寻求的，
是这个靛蓝色宝珠吧？\p我已带来了靛蓝色宝珠。
就让它的光芒唤醒你吧！\p向我展示……
展示你全部的力量吧！
```

证据：

```json
{
  "review": {
    "row_number": 12178,
    "symbol": "MagmaHideout_4F_Text_MaxieAwakenGroudon",
    "domain": "untransplanted_full",
    "idx": "",
    "old": "展示的你全部的力量吧！",
    "new": "展示你全部的力量吧！",
    "reason": "多余的。",
    "scope": "both",
    "action": "fix",
    "final_text": "赤焰松：固拉多……\\p无论怎样也不会\n从岩浆中苏醒的你……\\p一直在寻求的，\n是这个靛蓝色宝珠吧？\\p我已带来了靛蓝色宝珠。\n就让它的光芒唤醒你吧！\\p向我展示……\n展示你全部的力量吧！",
    "old_current_text": "赤焰松：固拉多……\\p无论怎样也不会\n从岩浆中苏醒的你……\\p一直在寻求的，\n是这个靛蓝色宝珠吧？\\p我已带来了靛蓝色宝珠。\n就让它的光芒唤醒你吧！\\p向我展示……\n展示的你全部的力量吧！",
    "changed_files": [
      "../pokeemerald_us_chs/data/maps/MagmaHideout_4F/scripts.inc",
      "patch/batches/432_checklist_scripts.json"
    ],
    "us_source_file": "data/maps/MagmaHideout_4F/scripts.inc",
    "jp_source": [
      {
        "file": "data/maps/MagmaHideout_4F/scripts.inc",
        "text": "マツブサ“マグマに　ねむる　グラードンよ\nなにをしても　めざめなかった　おまえが\\lもとめて　いたのは　あいいろのたま⋯⋯\\pそうなんだろう？\\pさあ　ここに　もってきて　やったぞ\nこの　かがやきで　めを　さませ！\\pそして　ほんとうの　ちからを\nわたしに　みせて　おくれ！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/maps/MagmaHideout_4F/scripts.inc",
        "text": "赤焰松：固拉多……\\p无论怎样也不会\n从岩浆中苏醒的你……\\p一直在寻求的，\n是这个靛蓝色宝珠吧？\\p我已带来了靛蓝色宝珠。\n就让它的光芒唤醒你吧！\\p向我展示……\n展示你全部的力量吧！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/maps/MagmaHideout_4F/scripts.inc",
        "text": "マツブサ“マグマに　ねむる　グラードンよ\nなにをしても　めざめなかった　おまえが\\lもとめて　いたのは　あいいろのたま⋯⋯\\pそうなんだろう？\\pさあ　ここに　もってきて　やったぞ\nこの　かがやきで　めを　さませ！\\pそして　ほんとうの　ちからを\nわたしに　みせて　おくれ！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_MagmaHideout_4F_Text_MaxieAwakenGroudon",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x090849F7",
      "payload_sha256": "731591bea7cc710e3951c6a64a5560b2a983fe74bf19f4549d4ccb6168736172",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0821C888",
          "original": "0x0821CBDC",
          "target": "0x090849F7",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12203 行 · untransplanted_full /  · sText_MysteryGiftVisitingTrainerInstructions

判定：`fixed_us_only`

理由：恢复介词；US配信脚本，无JP对应不新增ROM覆盖。

日文：

```text

```

英文：

```text
Thank you for using the MYSTERY\nGIFT System.\pBy holding this WONDER CARD, you\nmay take part in a survey at a\lPOKéMON MART.\pUse these surveys to invite\nTRAINERS to SOOTOPOLIS CITY.\p…Let me give you a secret\npassword for a survey:\p“GIVE ME\nAWESOME TRAINER”\pWrite that in on a survey and send\nit to the WIRELESS\lCOMMUNICATION SYSTEM.$
```

报告原中文：

```text
感谢使用\n神秘礼物系统。\p由于拥有神秘卡片\n您可以进行调查\l友好商店。\p通过调查您可以邀请\n训练家去琉璃市。\p……让我给您一个\n调查的密码吧：\p“GIVE ME\nAWESOME TRAINER”\p把这个写在调查上并发送到\n无线连接系统。$
```

修复前实际中文：

```text
感谢使用
神秘礼物系统。\p由于拥有神秘卡片
您可以进行调查\l友好商店。\p通过调查您可以邀请
训练家去琉璃市。\p……让我给您一个
调查的密码吧：\p“GIVE ME
AWESOME TRAINER”\p把这个写在调查上并发送到
无线连接系统。
```

最终中文：

```text
感谢使用
神秘礼物系统。\p由于拥有神秘卡片
您可以在友好商店\l参与调查。\p通过调查您可以邀请
训练家去琉璃市。\p……让我给您一个
调查的密码吧：\p“GIVE ME
AWESOME TRAINER”\p把这个写在调查上并发送到
无线连接系统。
```

证据：

```json
{
  "review": {
    "row_number": 12203,
    "symbol": "sText_MysteryGiftVisitingTrainerInstructions",
    "domain": "untransplanted_full",
    "idx": "",
    "old": "您可以进行调查\\l友好商店。",
    "new": "您可以在友好商店\\l参与调查。",
    "reason": "恢复介词；US配信脚本，无JP对应不新增ROM覆盖。",
    "scope": "us_only",
    "action": "fix",
    "final_text": "感谢使用\n神秘礼物系统。\\p由于拥有神秘卡片\n您可以在友好商店\\l参与调查。\\p通过调查您可以邀请\n训练家去琉璃市。\\p……让我给您一个\n调查的密码吧：\\p“GIVE ME\nAWESOME TRAINER”\\p把这个写在调查上并发送到\n无线连接系统。",
    "old_current_text": "感谢使用\n神秘礼物系统。\\p由于拥有神秘卡片\n您可以进行调查\\l友好商店。\\p通过调查您可以邀请\n训练家去琉璃市。\\p……让我给您一个\n调查的密码吧：\\p“GIVE ME\nAWESOME TRAINER”\\p把这个写在调查上并发送到\n无线连接系统。",
    "changed_files": [
      "../pokeemerald_us_chs/data/scripts/gift_trainer.inc"
    ],
    "us_source_file": "data/scripts/gift_trainer.inc",
    "jp_source": []
  },
  "source": {
    "us_sources": [
      {
        "file": "data/scripts/gift_trainer.inc",
        "text": "感谢使用\n神秘礼物系统。\\p由于拥有神秘卡片\n您可以在友好商店\\l参与调查。\\p通过调查您可以邀请\n训练家去琉璃市。\\p……让我给您一个\n调查的密码吧：\\p“GIVE ME\nAWESOME TRAINER”\\p把这个写在调查上并发送到\n无线连接系统。$"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_471_sText_MysteryGiftVisitingTrainerInstructions",
      "file": "patch/batches/471_checklist_mystery_gift_script_texts.json",
      "payload_address": "0x0908E442",
      "payload_sha256": "71cf535cd67dc40b4baa7085670dd1b0b482c4014d66dddb50eb6e26b6e68f62",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x85fcda9",
          "original": "0x85fcdbc",
          "target": "0x0908E442",
          "batch": "patch/batches/471_checklist_mystery_gift_script_texts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12204 行 · untransplanted_full /  · sText_MysteryGiftVisitingTrainerArrived

判定：`fixed_us_only`

理由：系统是希望的误写；日版缺此配信脚本，不新增猜测ROM覆盖。

日文：

```text

```

英文：

```text
Thank you for using the MYSTERY\nGIFT System.\pA TRAINER has arrived in\nSOOTOPOLIS CITY looking for you.\pWe hope you will enjoy\nbattling the visiting TRAINER.\pYou may invite other TRAINERS by\nentering other passwords.\pTry looking for other passwords\nthat may work.$
```

报告原中文：

```text
感谢使用\n神秘礼物系统。\p一位训练家已经来到\n琉璃市寻找您。\p系统您可以享受\n与训练家的对战。\p您可以邀请其他训练家\n通过填写密码。\p试着找寻其他\n有用的密码吧。$
```

修复前实际中文：

```text
感谢使用
神秘礼物系统。\p一位训练家已经来到
琉璃市寻找您。\p系统您可以享受
与训练家的对战。\p您可以邀请其他训练家
通过填写密码。\p试着找寻其他
有用的密码吧。
```

最终中文：

```text
感谢使用
神秘礼物系统。\p一位训练家已经来到
琉璃市寻找您。\p希望您可以享受
与训练家的对战。\p您可以邀请其他训练家
通过填写密码。\p试着找寻其他
有用的密码吧。
```

证据：

```json
{
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
  },
  "source": {
    "us_sources": [
      {
        "file": "data/scripts/gift_trainer.inc",
        "text": "感谢使用\n神秘礼物系统。\\p一位训练家已经来到\n琉璃市寻找您。\\p希望您可以享受\n与训练家的对战。\\p您可以邀请其他训练家\n通过填写密码。\\p试着找寻其他\n有用的密码吧。$"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_471_sText_MysteryGiftVisitingTrainerArrived",
      "file": "patch/batches/471_checklist_mystery_gift_script_texts.json",
      "payload_address": "0x0908E50B",
      "payload_sha256": "f5436859855580ae812191856cde6d2605c114e0f35498ef5288aef537fc2447",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x85fcdb4",
          "original": "0x85fce8b",
          "target": "0x0908E50B",
          "batch": "patch/batches/471_checklist_mystery_gift_script_texts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12205 行 · untransplanted_full /  · Text_RepelWoreOff

判定：`fixed_verified`

理由：实查当前batch432仍是FD02。US脚本填入STR_VAR_1，但Wokann repel.inc及UpdateRepelCounter不填入变量，JP须使用通用静态喷雾提示。

日文：

```text
スプレーのこうかが　きれた$
```

英文：

```text
REPEL's effect wore off…$
```

报告原中文：

```text
{STR_VAR_1}的效果消失了……$
```

修复前实际中文：

```text
{STR_VAR_1}的效果消失了……
```

最终中文：

```text
喷雾的效果消失了……
```

证据：

```json
{
  "review": {
    "row_number": 12205,
    "symbol": "Text_RepelWoreOff",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "实查当前batch432仍是FD02。US脚本填入STR_VAR_1，但Wokann repel.inc及UpdateRepelCounter不填入变量，JP须使用通用静态喷雾提示。",
    "action": "fix",
    "scope": "jp_only",
    "old": null,
    "new": "喷雾的效果消失了……$",
    "final_text": "喷雾的效果消失了……",
    "old_current_text": "{STR_VAR_1}的效果消失了……",
    "changed_files": [
      "patch/batches/432_checklist_scripts.json"
    ],
    "us_source_file": "data/scripts/repel.inc",
    "jp_source": [
      {
        "file": "data/scripts/repel.inc",
        "text": "スプレーのこうかが　きれた$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/scripts/repel.inc",
        "text": "{STR_VAR_1}的效果消失了……$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/scripts/repel.inc",
        "text": "スプレーのこうかが　きれた$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_Text_RepelWoreOff",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09084DDD",
      "payload_sha256": "ae78cc7fdd2d57c14a83baa746736e385c9f7da43b5f78d53ec80eb247afa58c",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08262395",
          "original": "0x0826239C",
          "target": "0x09084DDD",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12230 行 · untransplanted_full /  · BravoTrainerBattleTower_Text_ResponseUnsatisfied

判定：`fixed_verified`

理由：补回配对引号。

日文：

```text
‘{B_COPY_VAR_1}！'
なるほどねぇ
[P]
たしかに　{B_COPY_VAR_3}さんとの　たたかいは
‘{B_COPY_VAR_1}'　としか　いいようがない
たたかい　でしたからねぇ
[P]
{B_COPY_VAR_2}さんの　くやしさが
よく　つたわってくるよ！　くー！
```

英文：

```text
“{STR_VAR_1}.”\nNow isn't that fitting?\pThat battle with {STR_VAR_3} at the\nend… You can't describe it as anything\lelse but “{STR_VAR_1}”!\p{STR_VAR_2}'s disappointment comes across\nloud and clear, I'd say!$
```

报告原中文：

```text
“{STR_VAR_1}。”\n这也太贴切了吧？\p最后和{STR_VAR_3}的那场对战\n……除了{STR_VAR_1}”之外简直\l找不到更合适的描述了！\p{STR_VAR_2}的失落感\n简直扑面而来呢！$
```

修复前实际中文：

```text
“{STR_VAR_1}。”
这也太贴切了吧？\p最后和{STR_VAR_3}的那场对战
……除了{STR_VAR_1}”之外简直\l找不到更合适的描述了！\p{STR_VAR_2}的失落感
简直扑面而来呢！
```

最终中文：

```text
“{STR_VAR_1}。”
这也太贴切了吧？\p最后和{STR_VAR_3}的那场对战
……除了“{STR_VAR_1}”之外简直\l找不到更合适的描述了！\p{STR_VAR_2}的失落感
简直扑面而来呢！
```

证据：

```json
{
  "review": {
    "row_number": 12230,
    "symbol": "BravoTrainerBattleTower_Text_ResponseUnsatisfied",
    "domain": "untransplanted_full",
    "idx": "",
    "old": "……除了{STR_VAR_1}”之外简直",
    "new": "……除了“{STR_VAR_1}”之外简直",
    "reason": "补回配对引号。",
    "scope": "both",
    "action": "fix",
    "final_text": "“{STR_VAR_1}。”\n这也太贴切了吧？\\p最后和{STR_VAR_3}的那场对战\n……除了“{STR_VAR_1}”之外简直\\l找不到更合适的描述了！\\p{STR_VAR_2}的失落感\n简直扑面而来呢！",
    "old_current_text": "“{STR_VAR_1}。”\n这也太贴切了吧？\\p最后和{STR_VAR_3}的那场对战\n……除了{STR_VAR_1}”之外简直\\l找不到更合适的描述了！\\p{STR_VAR_2}的失落感\n简直扑面而来呢！",
    "changed_files": [
      "../pokeemerald_us_chs/data/text/tv.inc",
      "patch/batches/439_checklist_common_placeholders.json"
    ],
    "us_source_file": "data/text/tv.inc",
    "jp_source": [
      {
        "file": "data/text/tv/battle_tower_broadcast.inc",
        "text": "‘{B_COPY_VAR_1}！'\nなるほどねぇ\\pたしかに　{B_COPY_VAR_3}さんとの　たたかいは\n‘{B_COPY_VAR_1}'　としか　いいようがない\\lたたかい　でしたからねぇ\\p{B_COPY_VAR_2}さんの　くやしさが\nよく　つたわってくるよ！　くー！$"
      }
    ]
  },
  "source": {
    "us_sources": [
      {
        "file": "data/text/tv.inc",
        "text": "“{STR_VAR_1}。”\n这也太贴切了吧？\\p最后和{STR_VAR_3}的那场对战\n……除了“{STR_VAR_1}”之外简直\\l找不到更合适的描述了！\\p{STR_VAR_2}的失落感\n简直扑面而来呢！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/text/tv/battle_tower_broadcast.inc",
        "text": "‘{B_COPY_VAR_1}！'\nなるほどねぇ\\pたしかに　{B_COPY_VAR_3}さんとの　たたかいは\n‘{B_COPY_VAR_1}'　としか　いいようがない\\lたたかい　でしたからねぇ\\p{B_COPY_VAR_2}さんの　くやしさが\nよく　つたわってくるよ！　くー！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_439_BravoTrainerBattleTower_Text_ResponseUnsatisfied",
      "file": "patch/batches/439_checklist_common_placeholders.json",
      "payload_address": "0x09089B8E",
      "payload_sha256": "941aa474a660aab1f6209239794a61d14b31d2c10e4789aadf7c70d93b38b682",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08568D20",
          "original": "0x0824CF03",
          "target": "0x09089B8E",
          "batch": "patch/batches/439_checklist_common_placeholders.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12568 行 · untransplanted_full /  · gText_GlassChair

判定：`fixed_verified`

理由：Glass是玻璃；JP脚本菜单实有gText_GlassChair的已验证覆盖。

日文：

```text
ガラスのいす
```

英文：

```text
GLASS CHAIR
```

报告原中文：

```text
漂亮椅子
```

修复前实际中文：

```text
漂亮椅子
```

最终中文：

```text
玻璃椅子
```

证据：

```json
{
  "review": {
    "row_number": 12568,
    "symbol": "gText_GlassChair",
    "domain": "untransplanted_full",
    "idx": "",
    "old": "漂亮椅子",
    "new": "玻璃椅子",
    "reason": "Glass是玻璃；JP脚本菜单实有gText_GlassChair的已验证覆盖。",
    "scope": "both",
    "action": "fix",
    "final_text": "玻璃椅子",
    "old_current_text": "漂亮椅子",
    "changed_files": [
      "../pokeemerald_us_chs/src/strings.c",
      "patch/batches/453_checklist_named_menu_sections.json"
    ],
    "us_source_file": "src/strings.c",
    "jp_source": []
  },
  "source": {
    "us_sources": [
      {
        "file": "src/strings.c",
        "text": "玻璃椅子"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_453_gText_GlassChair",
      "file": "patch/batches/453_checklist_named_menu_sections.json",
      "payload_address": "0x0908CA3B",
      "payload_sha256": "b71ed62a14d5ec489cf432f3d776378a9f4e53a72d3ee248fe7015ca0c00dd07",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08563A50",
          "original": "0x085CABA2",
          "target": "0x0908CA3B",
          "batch": "patch/batches/453_checklist_named_menu_sections.json"
        }
      ]
    }
  ]
}
```

### CSV 第 12569 行 · untransplanted_full /  · gText_GlassDesk

判定：`fixed_verified`

理由：同上Glass Desk。

日文：

```text
ガラスのつくえ
```

英文：

```text
GLASS DESK
```

报告原中文：

```text
漂亮桌子
```

修复前实际中文：

```text
漂亮桌子
```

最终中文：

```text
玻璃桌子
```

证据：

```json
{
  "review": {
    "row_number": 12569,
    "symbol": "gText_GlassDesk",
    "domain": "untransplanted_full",
    "idx": "",
    "old": "漂亮桌子",
    "new": "玻璃桌子",
    "reason": "同上Glass Desk。",
    "scope": "both",
    "action": "fix",
    "final_text": "玻璃桌子",
    "old_current_text": "漂亮桌子",
    "changed_files": [
      "../pokeemerald_us_chs/src/strings.c",
      "patch/batches/453_checklist_named_menu_sections.json"
    ],
    "us_source_file": "src/strings.c",
    "jp_source": []
  },
  "source": {
    "us_sources": [
      {
        "file": "src/strings.c",
        "text": "玻璃桌子"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_453_gText_GlassDesk",
      "file": "patch/batches/453_checklist_named_menu_sections.json",
      "payload_address": "0x0908CA46",
      "payload_sha256": "8f4e04427ffa1eeff6134d4dd7de671298611491ba3562bfa3ce984a676d71e2",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08563A58",
          "original": "0x085CABA9",
          "target": "0x0908CA46",
          "batch": "patch/batches/453_checklist_named_menu_sections.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13242 行 · untransplanted_full /  · sText_Cancel

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
やめる
```

英文：

```text
CANCEL
```

报告原中文：

```text
取消
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13242,
    "symbol": "sText_Cancel",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/trade.h",
        "text": "取消"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/trade.h",
        "text": "やめる"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_Cancel",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x090859FC",
      "payload_sha256": "de4a4104c9d19c2c91e134119911032ba6e4bbf401766b4dfd6f2f4accca5fa4",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08300AFC",
          "original": "0x08300ABD",
          "target": "0x090859FC",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13243 行 · untransplanted_full /  · sText_ChooseAPkmn

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
ポケモンを　えらんで　ください
```

英文：

```text
Choose a POKéMON.
```

报告原中文：

```text
请选择宝可梦。
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13243,
    "symbol": "sText_ChooseAPkmn",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/trade.h",
        "text": "请选择宝可梦。"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/trade.h",
        "text": "ポケモンを　えらんで　ください"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_ChooseAPkmn",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A18",
      "payload_sha256": "8b6dad0bac27455ed8891be5c45d389e325d62a00299994736a806eb1a3955f3",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08300B00",
          "original": "0x08300AC1",
          "target": "0x09085A18",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13244 行 · untransplanted_full /  · sText_Summary

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
つよさをみる
```

英文：

```text
SUMMARY
```

报告原中文：

```text
查看能力
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13244,
    "symbol": "sText_Summary",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/trade.h",
        "text": "查看能力"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/trade.h",
        "text": "つよさをみる"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_Summary",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085AB7",
      "payload_sha256": "465c2deae26cc88db9b07aff0184ae5c2da0c86debd96fe864cb53e0bf4a055c",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08300B04",
          "original": "0x08300AD1",
          "target": "0x09085AB7",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13245 行 · untransplanted_full /  · sText_Trade

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
こうかんにだす
```

英文：

```text
TRADE
```

报告原中文：

```text
交换
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13245,
    "symbol": "sText_Trade",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/trade.h",
        "text": "交换"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/trade.h",
        "text": "こうかんにだす"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_Trade",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085AD1",
      "payload_sha256": "dc900887eccc0012b1618843b31fbd1ddc1fe4ddc1208bcdc2342cc025195d01",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08300B08",
          "original": "0x08300AD8",
          "target": "0x09085AD1",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13246 行 · untransplanted_full /  · sText_Trade2

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
こうかんにだす
```

英文：

```text
TRADE
```

报告原中文：

```text
交换
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13246,
    "symbol": "sText_Trade2",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/trade.h",
        "text": "交换"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/trade.h",
        "text": "こうかんにだす"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_Trade2",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085AD8",
      "payload_sha256": "dc900887eccc0012b1618843b31fbd1ddc1fe4ddc1208bcdc2342cc025195d01",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08300B30",
          "original": "0x08300B1D",
          "target": "0x09085AD8",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13247 行 · untransplanted_full /  · sText_TheTradeHasBeenCanceled

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{COLOR 0x02}{HIGHLIGHT 0x01}{SHADOW 0x03}こうかんは
キャンセル　されました！
```

英文：

```text
{COLOR DARK_GRAY}{HIGHLIGHT WHITE}{SHADOW LIGHT_GRAY}The trade has\nbeen canceled.
```

报告原中文：

```text
{COLOR DARK_GRAY}{HIGHLIGHT WHITE}{SHADOW LIGHT_GRAY}宝可梦交换\n已中止。
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13247,
    "symbol": "sText_TheTradeHasBeenCanceled",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/trade.h",
        "text": "{COLOR DARK_GRAY}{HIGHLIGHT WHITE}{SHADOW LIGHT_GRAY}宝可梦交换\n已中止。"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/trade.h",
        "text": "{COLOR 0x02}{HIGHLIGHT 0x01}{SHADOW 0x03}こうかんは\nキャンセル　されました！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_438_sText_TheTradeHasBeenCanceled",
      "file": "patch/batches/438_checklist_controls_and_gambler.json",
      "payload_address": "0x09089A0E",
      "payload_sha256": "9a95502cd5b5f0c80e387f2f2c03ad2279ce99959ff1eab44f9257c50b1cc6bb",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08300BE0",
          "original": "0x08300B59",
          "target": "0x09089A0E",
          "batch": "patch/batches/438_checklist_controls_and_gambler.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13248 行 · untransplanted_full /  · sText_OnlyPkmnForBattle

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{COLOR 0x02}{HIGHLIGHT 0x01}{SHADOW 0x03}そのポケモンを　こうかんすると
せんとうできなくなっちゃうよ！
```

英文：

```text
That's your only\nPOKéMON for battle.
```

报告原中文：

```text
最后1只同行的宝可梦\n不能用来交换。
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13248,
    "symbol": "sText_OnlyPkmnForBattle",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/trade.h",
        "text": "最后1只同行的宝可梦\n不能用来交换。"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/trade.h",
        "text": "{COLOR 0x02}{HIGHLIGHT 0x01}{SHADOW 0x03}そのポケモンを　こうかんすると\nせんとうできなくなっちゃうよ！"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_438_sText_OnlyPkmnForBattle",
      "file": "patch/batches/438_checklist_controls_and_gambler.json",
      "payload_address": "0x090899E9",
      "payload_sha256": "b96b3e419cec0d1af4fafe993ca21766cbc8ce451e298ce40f2d4185ffb57280",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08300BE4",
          "original": "0x08300B75",
          "target": "0x090899E9",
          "batch": "patch/batches/438_checklist_controls_and_gambler.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13249 行 · untransplanted_full /  · sText_WaitingForYourFriend

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{COLOR 0x02}{HIGHLIGHT 0x01}{SHADOW 0x03}ともだちの　しゅうりょうを
まっています⋯⋯
```

英文：

```text
{COLOR DARK_GRAY}{HIGHLIGHT WHITE}{SHADOW LIGHT_GRAY}Waiting for your friend\nto finish…
```

报告原中文：

```text
{COLOR DARK_GRAY}{HIGHLIGHT WHITE}{SHADOW LIGHT_GRAY}正在等待对方的回复……\n请稍等片刻。
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13249,
    "symbol": "sText_WaitingForYourFriend",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/trade.h",
        "text": "{COLOR DARK_GRAY}{HIGHLIGHT WHITE}{SHADOW LIGHT_GRAY}正在等待对方的回复……\n请稍等片刻。"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/trade.h",
        "text": "{COLOR 0x02}{HIGHLIGHT 0x01}{SHADOW 0x03}ともだちの　しゅうりょうを\nまっています⋯⋯"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_438_sText_WaitingForYourFriend",
      "file": "patch/batches/438_checklist_controls_and_gambler.json",
      "payload_address": "0x09089A2D",
      "payload_sha256": "66561d502a4ecaee284d88435613a645ee6365d254a41c50d6c157d6e0cb4ce9",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08300BEC",
          "original": "0x08300B9E",
          "target": "0x09089A2D",
          "batch": "patch/batches/438_checklist_controls_and_gambler.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13250 行 · untransplanted_full /  · sText_AwaitingCommunication

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{B_COPY_VAR_1}！
ともだちからの　れんらくを　まっています
```

英文：

```text
{STR_VAR_1}! Awaiting\ncommunication from another player.
```

报告原中文：

```text
{STR_VAR_1}！\n正在等待其他玩家连接。
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13250,
    "symbol": "sText_AwaitingCommunication",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "{STR_VAR_1}！\n正在等待其他玩家连接。"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_439_sText_AwaitingCommunication",
      "file": "patch/batches/439_checklist_common_placeholders.json",
      "payload_address": "0x0908BFDF",
      "payload_sha256": "cc897a26c10eab63af86f1146c7a381a8e0cf288cea44c8987ce015e0391379a",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x080121D0",
          "original": "0x082C069C",
          "target": "0x0908BFDF",
          "batch": "patch/batches/439_checklist_common_placeholders.json"
        },
        {
          "address": "0x0801252C",
          "original": "0x082C069C",
          "target": "0x0908BFDF",
          "batch": "patch/batches/439_checklist_common_placeholders.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13251 行 · untransplanted_full /  · sText_CancelModeWithTheseMembers

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
この　メンバーで　{B_COPY_VAR_1}を
するのは　やめますか？
```

英文：

```text
Cancel {STR_VAR_1} MODE\nwith these members?
```

报告原中文：

```text
要放弃以当前成员\n进行{STR_VAR_1}模式吗？
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13251,
    "symbol": "sText_CancelModeWithTheseMembers",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "要放弃以当前成员\n进行{STR_VAR_1}模式吗？"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_439_sText_CancelModeWithTheseMembers",
      "file": "patch/batches/439_checklist_common_placeholders.json",
      "payload_address": "0x0908C001",
      "payload_sha256": "813b9a6163dc357de1f423fcc2517a4d61c736828e002ba713b1e76de8cc0855",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08012910",
          "original": "0x082C092C",
          "target": "0x0908C001",
          "batch": "patch/batches/439_checklist_common_placeholders.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13252 行 · untransplanted_full /  · sText_OfferToTradeMon

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
とうろく　していた
LV{DYNAMIC 0}の　{DYNAMIC 1}　と\pLV{DYNAMIC 2}の　{DYNAMIC 3}　の
こうかん　もうしこみが　きています\pこうかん　しますか？
```

英文：

```text
There is an offer to trade your\nregistered Lv. {DYNAMIC 0} {DYNAMIC 1}\pin exchange for a\nLv. {DYNAMIC 2} {DYNAMIC 3}.\pWill you accept this trade\noffer?
```

报告原中文：

```text
有人愿意用一只\n等级{DYNAMIC 0}的{DYNAMIC 1}\p与您登记的等级{DYNAMIC 2}\n的{DYNAMIC 3}交换。\p要同意交换吗？
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13252,
    "symbol": "sText_OfferToTradeMon",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "有人愿意用一只\n等级{DYNAMIC 0}的{DYNAMIC 1}\\p与您登记的等级{DYNAMIC 2}\n的{DYNAMIC 3}交换。\\p要同意交换吗？"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room7.h",
        "text": "とうろく　していた\nLV{DYNAMIC 0}の　{DYNAMIC 1}　と\\pLV{DYNAMIC 2}の　{DYNAMIC 3}　の\nこうかん　もうしこみが　きています\\pこうかん　しますか？"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_468_sText_OfferToTradeMon",
      "file": "patch/batches/468_checklist_union_room.json",
      "payload_address": "0x0908E10C",
      "payload_sha256": "41878fde8c0e7a031bc5469ca6aebc8fb9df9db2b23243181878958922ff4707",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x8017a64",
          "original": "0x82c0e68",
          "target": "0x0908E10C",
          "batch": "patch/batches/468_checklist_union_room.json"
        },
        {
          "address": "0x82c0f1c",
          "original": "0x82c0e68",
          "target": "0x0908E10C",
          "batch": "patch/batches/468_checklist_union_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13253 行 · untransplanted_full /  · sText_TrainerAppearsBusy

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
⋯⋯
いまは　とりこみちゅうの　ようだ\p
```

英文：

```text
……\nThe TRAINER appears to be busy…\p
```

报告原中文：

```text
……\n现在好像正在忙……\p
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13253,
    "symbol": "sText_TrainerAppearsBusy",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "……\n现在好像正在忙……\\p"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_TrainerAppearsBusy",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085ADF",
      "payload_sha256": "884a4c8955bff896484990e41fc8077bfdfe79826ae82ea3c76ae23343967e69",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x080156B4",
          "original": "0x082C0FE0",
          "target": "0x09085ADF",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        },
        {
          "address": "0x080156E8",
          "original": "0x082C0FE0",
          "target": "0x09085ADF",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        },
        {
          "address": "0x080175E8",
          "original": "0x082C0FE0",
          "target": "0x09085ADF",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13254 行 · untransplanted_full /  · sText_ChooseTrainer

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
ともだちを　えらんでください
```

英文：

```text
Please choose a TRAINER.
```

报告原中文：

```text
请选择1位训练家。
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13254,
    "symbol": "sText_ChooseTrainer",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "请选择1位训练家。"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_ChooseTrainer",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A29",
      "payload_sha256": "fb18155be56e2beb226c1ac5d70d4e648b9b05586423e3da5134e372cb255306",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08014AEC",
          "original": "0x082C19CC",
          "target": "0x09085A29",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13255 行 · untransplanted_full /  · sText_PlayerHasBeenAskedToRegisterYouPleaseWait

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{B_COPY_VAR_1}に　メンバー　とうろくを
おねがいしています！　おまちください
```

英文：

```text
{STR_VAR_1} has been asked to register\nyou as a member. Please wait.
```

报告原中文：

```text
正在请{STR_VAR_1}\n添加您为成员，请稍等！
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13255,
    "symbol": "sText_PlayerHasBeenAskedToRegisterYouPleaseWait",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "正在请{STR_VAR_1}\n添加您为成员，请稍等！"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_453_sText_PlayerHasBeenAskedToRegisterYouPleaseWait",
      "file": "patch/batches/453_checklist_named_menu_sections.json",
      "payload_address": "0x0908CF8B",
      "payload_sha256": "f3e2a890dce9d195c3ea915d9348baf6b598240993cee73d04eaccb362212651",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08012C5C",
          "original": "0x082C1C94",
          "target": "0x0908CF8B",
          "batch": "patch/batches/453_checklist_named_menu_sections.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13256 行 · untransplanted_full /  · sText_Battle

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
たいせん
```

英文：

```text
BATTLE
```

报告原中文：

```text
对战
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13256,
    "symbol": "sText_Battle",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "对战"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8i.h",
        "text": "たいせん"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_Battle",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x090859DB",
      "payload_sha256": "e73b6f58266410855d30a63428e8c34daaac9f2585ce1e15fc1a3820a2934a3b",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C2134",
          "original": "0x082C1D38",
          "target": "0x090859DB",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13257 行 · untransplanted_full /  · sText_Chat2

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
チャット
```

英文：

```text
CHAT
```

报告原中文：

```text
聊天
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13257,
    "symbol": "sText_Chat2",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "聊天"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8i.h",
        "text": "チャット"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_Chat2",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A11",
      "payload_sha256": "70af6f639449dbbc0ca217d2efdcf8b3391fefbe0b46b2244ad7efcf67d172be",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C213C",
          "original": "0x082C1D40",
          "target": "0x09085A11",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13258 行 · untransplanted_full /  · sText_Greetings

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
あいさつ
```

英文：

```text
GREETINGS
```

报告原中文：

```text
问候
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13258,
    "symbol": "sText_Greetings",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "问候"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8i.h",
        "text": "あいさつ"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_Greetings",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A74",
      "payload_sha256": "38c9d09296c0224a833fbf9f16d09176d6da9c10675bdf679808e30925c0b7d7",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C212C",
          "original": "0x082C1D48",
          "target": "0x09085A74",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13259 行 · untransplanted_full /  · sText_Exit

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
やめる
```

英文：

```text
EXIT
```

报告原中文：

```text
退出
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13259,
    "symbol": "sText_Exit",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "退出"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8i.h",
        "text": "やめる"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_Exit",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A66",
      "payload_sha256": "675b4d9dbea7c7f38f868be527f54c10f99f2fa8f04d1381598ead83be402f99",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C2144",
          "original": "0x082C1D50",
          "target": "0x09085A66",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        },
        {
          "address": "0x082C217C",
          "original": "0x082C1D50",
          "target": "0x09085A66",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        },
        {
          "address": "0x082C222C",
          "original": "0x082C1D50",
          "target": "0x09085A66",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13260 行 · untransplanted_full /  · sText_Exit2

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
とじる
```

英文：

```text
EXIT
```

报告原中文：

```text
退出
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13260,
    "symbol": "sText_Exit2",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "退出"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8i.h",
        "text": "とじる"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_Exit2",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A6D",
      "payload_sha256": "675b4d9dbea7c7f38f868be527f54c10f99f2fa8f04d1381598ead83be402f99",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C22A4",
          "original": "0x082C1D54",
          "target": "0x09085A6D",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13261 行 · untransplanted_full /  · sText_Info

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
せつめいをきく
```

英文：

```text
INFO
```

报告原中文：

```text
听说明
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13261,
    "symbol": "sText_Info",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "听说明"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8i.h",
        "text": "せつめいをきく"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_Info",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A7B",
      "payload_sha256": "d0bb29add2715899308e63bed8cf7ea1285e6fd5425e6852b95d8538a345af35",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C2174",
          "original": "0x082C1D58",
          "target": "0x09085A7B",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13262 行 · untransplanted_full /  · sText_NameWantedOfferLv

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
なまえ　　　　ほしいタイプ　あげるポケモン　　レベル
```

英文：

```text
NAME{CLEAR_TO 60}WANTED{CLEAR_TO 110}OFFER{CLEAR_TO 198}LV.
```

报告原中文：

```text
名字{CLEAR_TO 60}想要{CLEAR_TO 110}给出{CLEAR_TO 198}等级
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13262,
    "symbol": "sText_NameWantedOfferLv",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "名字{CLEAR_TO 60}想要{CLEAR_TO 110}给出{CLEAR_TO 198}等级"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "なまえ　　　　ほしいタイプ　あげるポケモン　　レベル"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_438_sText_NameWantedOfferLv",
      "file": "patch/batches/438_checklist_controls_and_gambler.json",
      "payload_address": "0x090899CD",
      "payload_sha256": "3aff1141a338f36186900cda2671a38a72932b44e31329c1db280808b6a7e433",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08016C74",
          "original": "0x082C1D60",
          "target": "0x090899CD",
          "batch": "patch/batches/438_checklist_controls_and_gambler.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13263 行 · untransplanted_full /  · sText_SingleBattle

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
シングルバトル
```

英文：

```text
SINGLE BATTLE
```

报告原中文：

```text
单打对战
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13263,
    "symbol": "sText_SingleBattle",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "单打对战"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "シングルバトル"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_SingleBattle",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A98",
      "payload_sha256": "045a8fcd62bed4b9ec09c6e47ed508295f3ea2002da0ed859a373af8ac1cd202",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1E5C",
          "original": "0x082C1D7C",
          "target": "0x09085A98",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13264 行 · untransplanted_full /  · sText_DoubleBattle

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
ダブルバトル
```

英文：

```text
DOUBLE BATTLE
```

报告原中文：

```text
双打对战
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13264,
    "symbol": "sText_DoubleBattle",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "双打对战"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "ダブルバトル"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_DoubleBattle",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A5B",
      "payload_sha256": "2f343127b4d2586b3b82b97d6792f10f4a0377bd165e3b1a00547e30cd7e82ff",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1E60",
          "original": "0x082C1D84",
          "target": "0x09085A5B",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13265 行 · untransplanted_full /  · sText_MultiBattle

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
マルチバトル
```

英文：

```text
MULTI BATTLE
```

报告原中文：

```text
多人对战
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13265,
    "symbol": "sText_MultiBattle",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "多人对战"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "マルチバトル"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_MultiBattle",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A84",
      "payload_sha256": "f1259f91a34f9ad45e1fa31ad5ff414579537c15c7b05a814009c1b2e4c1bc19",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1E64",
          "original": "0x082C1D8C",
          "target": "0x09085A84",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13266 行 · untransplanted_full /  · sText_Chat

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
チャット
```

英文：

```text
CHAT
```

报告原中文：

```text
聊天
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13266,
    "symbol": "sText_Chat",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "聊天"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "チャット"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_Chat",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A0A",
      "payload_sha256": "70af6f639449dbbc0ca217d2efdcf8b3391fefbe0b46b2244ad7efcf67d172be",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1E6C",
          "original": "0x082C1DA0",
          "target": "0x09085A0A",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13267 行 · untransplanted_full /  · sText_Cards

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
カード
```

英文：

```text
CARDS
```

报告原中文：

```text
卡片
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13267,
    "symbol": "sText_Cards",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "卡片"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "カード"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_Cards",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A03",
      "payload_sha256": "b800c01b71d3aa3139bf72c6167835c3fa59b2e7c7494070a8bfd5439b9da410",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1E78",
          "original": "0x082C1DA8",
          "target": "0x09085A03",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13268 行 · untransplanted_full /  · sText_WonderCards

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
ふしぎなカード
```

英文：

```text
WONDER CARDS
```

报告原中文：

```text
神秘卡片
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13268,
    "symbol": "sText_WonderCards",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "神秘卡片"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "ふしぎなカード"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_WonderCards",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085AF6",
      "payload_sha256": "493aa950b59eaabbd5c66968947d512379643393f4ca31b84ae00896acd2fab1",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1E70",
          "original": "0x082C1DAC",
          "target": "0x09085AF6",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13269 行 · untransplanted_full /  · sText_WonderNews

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
ふしぎなニュース
```

英文：

```text
WONDER NEWS
```

报告原中文：

```text
神秘新闻
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13269,
    "symbol": "sText_WonderNews",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "神秘新闻"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "ふしぎなニュース"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_WonderNews",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085B01",
      "payload_sha256": "6b584ba7bf6d09a537d5d26b80fa9b02ca9c58cce078c66471858880d3d0cce1",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1E74",
          "original": "0x082C1DB4",
          "target": "0x09085B01",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13270 行 · untransplanted_full /  · sText_BerryCrush

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
きのみクラッシュ
```

英文：

```text
BERRY CRUSH
```

报告原中文：

```text
树果粉碎
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13270,
    "symbol": "sText_BerryCrush",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "树果粉碎"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "きのみクラッシュ"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_BerryCrush",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x090859F1",
      "payload_sha256": "4d7fb4e707cbf6b39a6a4da03dc8fa146af6db9df7dbca4f784bc20db79dd162",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1E80",
          "original": "0x082C1DCC",
          "target": "0x090859F1",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13271 行 · untransplanted_full /  · sText_RecordCorner

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
レコードコーナー
```

英文：

```text
RECORD CORNER
```

报告原中文：

```text
记录角
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13271,
    "symbol": "sText_RecordCorner",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "记录角"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "レコードコーナー"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_RecordCorner",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A8F",
      "payload_sha256": "5d8495c93877c0c205c8e4839b7f3ef402e2492079f614975e108d5506585208",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1E94",
          "original": "0x082C1DF0",
          "target": "0x09085A8F",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13272 行 · untransplanted_full /  · sText_CoolContest

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
かっこよさコンテスト
```

英文：

```text
COOL CONTEST
```

报告原中文：

```text
帅气华丽大赛
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13272,
    "symbol": "sText_CoolContest",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "帅气华丽大赛"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "かっこよさコンテスト"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_CoolContest",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A3D",
      "payload_sha256": "87ae68995c3e932a0cf87e6f1c6dfa032e0657ae17cb33f108d91f82b3310ab7",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1EB4",
          "original": "0x082C1DFC",
          "target": "0x09085A3D",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13273 行 · untransplanted_full /  · sText_BeautyContest

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
うつくしさコンテスト
```

英文：

```text
BEAUTY CONTEST
```

报告原中文：

```text
美丽华丽大赛
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13273,
    "symbol": "sText_BeautyContest",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "美丽华丽大赛"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "うつくしさコンテスト"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_BeautyContest",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x090859E2",
      "payload_sha256": "d987df97a585825b257376cab3a4acdf2d118714b6587a3f65640d9f548beff1",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1EB8",
          "original": "0x082C1E08",
          "target": "0x090859E2",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13274 行 · untransplanted_full /  · sText_CuteContest

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
かわいさコンテスト
```

英文：

```text
CUTE CONTEST
```

报告原中文：

```text
可爱华丽大赛
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13274,
    "symbol": "sText_CuteContest",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "可爱华丽大赛"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "かわいさコンテスト"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_CuteContest",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085A4C",
      "payload_sha256": "fb7062050b0e52f4b5ccbaf73475acff6efcf2f13c6b1cbee1a88f1fc626b930",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1EBC",
          "original": "0x082C1E14",
          "target": "0x09085A4C",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13275 行 · untransplanted_full /  · sText_SmartContest

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
かしこさコンテスト
```

英文：

```text
SMART CONTEST
```

报告原中文：

```text
聪明华丽大赛
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13275,
    "symbol": "sText_SmartContest",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "聪明华丽大赛"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "かしこさコンテスト"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_SmartContest",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085AA3",
      "payload_sha256": "fa50830db7d3980bfe30cb97e4bf48d797eb4dc7b113e5cbf2b8f3d46655669c",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1EC0",
          "original": "0x082C1E20",
          "target": "0x09085AA3",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13276 行 · untransplanted_full /  · sText_ToughContest

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
たくましさコンテスト
```

英文：

```text
TOUGH CONTEST
```

报告原中文：

```text
强壮华丽大赛
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13276,
    "symbol": "sText_ToughContest",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "强壮华丽大赛"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "たくましさコンテスト"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_sText_ToughContest",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x09085AC2",
      "payload_sha256": "e4205e7c89f010a64e6e613ccf36327016f74bee1dd2139ae59829c1e97e7e25",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082C1EC4",
          "original": "0x082C1E2C",
          "target": "0x09085AC2",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13277 行 · untransplanted_full /  · sText_BattleTowerLv50

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
　バトルタワー　レベル50
```

英文：

```text
BATTLE TOWER LV. 50
```

报告原中文：

```text
对战塔Lv. 50级
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13277,
    "symbol": "sText_BattleTowerLv50",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "对战塔Lv. 50级"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8j.h",
        "text": "　バトルタワー　レベル50"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_479_sText_BattleTowerLv50",
      "file": "patch/batches/479_checklist_frontier_records2.json",
      "payload_address": "0x0908ED72",
      "payload_sha256": "186b3b154369a3b8020a95739cc66f5f5d04cb8102ca4e1ae31b642dca80e705",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x82c1ec8",
          "original": "0x82c1e38",
          "target": "0x0908ED72",
          "batch": "patch/batches/479_checklist_frontier_records2.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13278 行 · untransplanted_full /  · sText_BattleTowerOpenLv

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
　　　バトルタワー　オープンレベル
```

英文：

```text
BATTLE TOWER OPEN LEVEL
```

报告原中文：

```text
对战塔自由等级
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13278,
    "symbol": "sText_BattleTowerOpenLv",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "对战塔自由等级"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_479_sText_BattleTowerOpenLv",
      "file": "patch/batches/479_checklist_frontier_records2.json",
      "payload_address": "0x0908ED83",
      "payload_sha256": "142ce55dbfc091e8a4c930ea81a7e2591f185f8d69c1f046bf1f0435b8d390fb",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x82c1e90",
          "original": "0x82c1e48",
          "target": "0x0908ED83",
          "batch": "patch/batches/479_checklist_frontier_records2.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13279 行 · untransplanted_full /  · sText_TrainerCardInfoPage1

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{DYNAMIC 0}の　{DYNAMIC 1}の
トレーナーカードを　みせてもらった\l{DYNAMIC 2}\pポケモンずかん　{DYNAMIC 3}
プレイ　じかん　{DYNAMIC 4}:{DYNAMIC 5}\p
```

英文：

```text
This is {DYNAMIC 0} {DYNAMIC 1}'s\nTRAINER CARD…\l{DYNAMIC 2}\pPOKéDEX: {DYNAMIC 3}\nTIME:    {DYNAMIC 4}:{DYNAMIC 5}\p
```

报告原中文：

```text
这是{DYNAMIC 0} {DYNAMIC 1}的\n训练家卡……\l{DYNAMIC 2}\p图鉴：{DYNAMIC 3}\n时间：{DYNAMIC 4}：{DYNAMIC 5}\p
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13279,
    "symbol": "sText_TrainerCardInfoPage1",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "这是{DYNAMIC 0} {DYNAMIC 1}的\n训练家卡……\\l{DYNAMIC 2}\\p图鉴：{DYNAMIC 3}\n时间：{DYNAMIC 4}：{DYNAMIC 5}\\p"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8l.h",
        "text": "{DYNAMIC 0}の　{DYNAMIC 1}の\nトレーナーカードを　みせてもらった\\l{DYNAMIC 2}\\pポケモンずかん　{DYNAMIC 3}\nプレイ　じかん　{DYNAMIC 4}:{DYNAMIC 5}\\p"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_446_sText_TrainerCardInfoPage1",
      "file": "patch/batches/446_checklist_reviewed_card_quiz_slots.json",
      "payload_address": "0x0908C2B1",
      "payload_sha256": "e57e95166052d3682f1285543cdf4fd5c10c8d2afb5af3e2f714c34518a1c8e9",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08017E74",
          "original": "0x082C1F1C",
          "target": "0x0908C2B1",
          "batch": "patch/batches/446_checklist_reviewed_card_quiz_slots.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13280 行 · untransplanted_full /  · sText_TrainerCardInfoPage2

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
たいせん　かち{DYNAMIC 0}　まけ{DYNAMIC 2}
こうかん　{DYNAMIC 3}かい\p‘{DYNAMIC 4}　{DYNAMIC 5}
　{DYNAMIC 6}　{DYNAMIC 7}\p${DYNAMIC 1}‘これからも　よろしく！{PAUSE 60}$　　{DYNAMIC 1}‘これからも　よろしくね！{PAUSE 60}
```

英文：

```text
BATTLES: WINS: {DYNAMIC 0}  LOSSES: {DYNAMIC 2}\nTRADES: {DYNAMIC 3}\p“{DYNAMIC 4} {DYNAMIC 5}\n{DYNAMIC 6} {DYNAMIC 7}”\p
```

报告原中文：

```text
 对战：胜：{DYNAMIC 0} 负：{DYNAMIC 2}\n交换次数：{DYNAMIC 3}\p“{DYNAMIC 4} {DYNAMIC 5}\n{DYNAMIC 6} {DYNAMIC 7}”\p
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13280,
    "symbol": "sText_TrainerCardInfoPage2",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": " 对战：胜：{DYNAMIC 0} 负：{DYNAMIC 2}\n交换次数：{DYNAMIC 3}\\p“{DYNAMIC 4} {DYNAMIC 5}\n{DYNAMIC 6} {DYNAMIC 7}”\\p"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8l.h",
        "text": "たいせん　かち{DYNAMIC 0}　まけ{DYNAMIC 2}\nこうかん　{DYNAMIC 3}かい\\p‘{DYNAMIC 4}　{DYNAMIC 5}\n　{DYNAMIC 6}　{DYNAMIC 7}\\p${DYNAMIC 1}‘これからも　よろしく！{PAUSE 60}$　　{DYNAMIC 1}‘これからも　よろしくね！{PAUSE 60}"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_446_sText_TrainerCardInfoPage2",
      "file": "patch/batches/446_checklist_reviewed_card_quiz_slots.json",
      "payload_address": "0x0908C2FC",
      "payload_sha256": "34d08dc513475cb90b860238660571af90ab1215f930b7421bebfb90a8533684",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08017E80",
          "original": "0x082C1F54",
          "target": "0x0908C2FC",
          "batch": "patch/batches/446_checklist_reviewed_card_quiz_slots.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13281 行 · untransplanted_full /  · sText_GladToMeetYouMale

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{DYNAMIC 1}‘これからも　よろしく！{PAUSE 60} [Wokann注: 该符号为sText_TrainerCardInfoPage2+0x28偏移引用]
```

英文：

```text
{DYNAMIC 1}: Glad to have met you!{PAUSE 60}
```

报告原中文：

```text
{DYNAMIC 1}：很高兴认识你！{PAUSE 60}
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13281,
    "symbol": "sText_GladToMeetYouMale",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "{DYNAMIC 1}：很高兴认识你！{PAUSE 60}"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_468_sText_GladToMeetYouMale",
      "file": "patch/batches/468_checklist_union_room.json",
      "payload_address": "0x0908E161",
      "payload_sha256": "4d2967aefb217e44bcc8701552059a7c2101efe1c431faca78afd8bfa7af7eee",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x82c1fa4",
          "original": "0x82c1f7c",
          "target": "0x0908E161",
          "batch": "patch/batches/468_checklist_union_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13282 行 · untransplanted_full /  · sText_GladToMeetYouFemale

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{DYNAMIC 1}‘これからも　よろしくね！{PAUSE 60} [Wokann注: 该符号为sText_TrainerCardInfoPage2+0x3C偏移引用]
```

英文：

```text
{DYNAMIC 1}: Glad to meet you!{PAUSE 60}
```

报告原中文：

```text
{DYNAMIC 1}：很高兴认识你！{PAUSE 60}
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13282,
    "symbol": "sText_GladToMeetYouFemale",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "{DYNAMIC 1}：很高兴认识你！{PAUSE 60}"
      }
    ],
    "wokann_sources": []
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_468_sText_GladToMeetYouFemale",
      "file": "patch/batches/468_checklist_union_room.json",
      "payload_address": "0x0908E17D",
      "payload_sha256": "4d2967aefb217e44bcc8701552059a7c2101efe1c431faca78afd8bfa7af7eee",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x82c1fa8",
          "original": "0x82c1f90",
          "target": "0x0908E17D",
          "batch": "patch/batches/468_checklist_union_room.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13283 行 · untransplanted_full /  · sText_FinishedCheckingPlayersTrainerCard

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{DYNAMIC 1}の　トレーナーカードを
みおわった！{PAUSE 60}
```

英文：

```text
Finished checking {DYNAMIC 1}'s\nTRAINER CARD.{PAUSE 60}
```

报告原中文：

```text
{DYNAMIC 1}的训练家卡\n确认完毕。{PAUSE 60}
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13283,
    "symbol": "sText_FinishedCheckingPlayersTrainerCard",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "src/data/union_room.h",
        "text": "{DYNAMIC 1}的训练家卡\n确认完毕。{PAUSE 60}"
      }
    ],
    "wokann_sources": [
      {
        "file": "src/data/union_room8l.h",
        "text": "{DYNAMIC 1}の　トレーナーカードを\nみおわった！{PAUSE 60}"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_446_sText_FinishedCheckingPlayersTrainerCard",
      "file": "patch/batches/446_checklist_reviewed_card_quiz_slots.json",
      "payload_address": "0x0908C290",
      "payload_sha256": "ac69dc841628612c826ad042bb5aa6c4f00be1072e215f52eef0a155f94dfcb2",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08017E84",
          "original": "0x082C1FAC",
          "target": "0x0908C290",
          "batch": "patch/batches/446_checklist_reviewed_card_quiz_slots.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13284 行 · untransplanted_full /  · gText_PokemartSign

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
べんりなどうぐ　いろいろ　あります
‘フレンドリィショップ'$
```

英文：

```text

```

报告原中文：

```text
“挑选一些便利的道具吧！”\n友好商店$“让您疲劳的伙伴们恢复活力！”\n宝可梦中心$也许是{STR_VAR_1}喜欢的游戏\n…… …… …… …… …… …… …… ……\p该走了！$欢迎来到水静百货。\p要去几层？$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13284,
    "symbol": "gText_PokemartSign",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "“挑选一些便利的道具吧！”\n友好商店$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "べんりなどうぐ　いろいろ　あります\n‘フレンドリィショップ'$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_gText_PokemartSign",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x090857CF",
      "payload_sha256": "d808a9d7dd2c34e2be9e20f616e1228662e7736ebe2b7c5b7e2dcd00671b3545",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08242EF8",
          "original": "0x082439D6",
          "target": "0x090857CF",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13285 行 · untransplanted_full /  · gText_PokemonCenterSign

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
つかれた　ポケモンも　ひとやすみ！
‘ポケモンセンター'$
```

英文：

```text

```

报告原中文：

```text
“让您疲劳的伙伴们恢复活力！”\n宝可梦中心$也许是{STR_VAR_1}喜欢的游戏\n…… …… …… …… …… …… …… ……\p该走了！$欢迎来到水静百货。\p要去几层？$沙暴太强了，\n走不过去。$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13285,
    "symbol": "gText_PokemonCenterSign",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "“让您疲劳的伙伴们恢复活力！”\n宝可梦中心$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "つかれた　ポケモンも　ひとやすみ！\n‘ポケモンセンター'$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_450_gText_PokemonCenterSign",
      "file": "patch/batches/450_checklist_verified_event_msgboxes.json",
      "payload_address": "0x0908C6B2",
      "payload_sha256": "d1a1cacf77c5506db56785fc6aa974a7e87418c4d673c486d7c14692698ef4f5",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08242F01",
          "original": "0x082439F5",
          "target": "0x0908C6B2",
          "batch": "patch/batches/450_checklist_verified_event_msgboxes.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13286 行 · untransplanted_full /  · gText_MomOrDadMightLikeThisProgram

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{STR_VAR_1}が　すきそうな　ばんぐみをやってる！
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\pさきを　いそがなきゃ！$
```

英文：

```text

```

报告原中文：

```text
也许是{STR_VAR_1}喜欢的游戏\n…… …… …… …… …… …… …… ……\p该走了！$欢迎来到水静百货。\p要去几层？$沙暴太强了，\n走不过去。$包包里的道具可以\n登录到SELECT上，方便使用。$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13286,
    "symbol": "gText_MomOrDadMightLikeThisProgram",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "也许是{STR_VAR_1}喜欢的游戏\n…… …… …… …… …… …… …… ……\\p该走了！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "{STR_VAR_1}が　すきそうな　ばんぐみをやってる！\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\\pさきを　いそがなきゃ！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_MomOrDadMightLikeThisProgram",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09084E40",
      "payload_sha256": "3b6faf61db735b0841390a6babde24ba8583f87484842a05e2bb9bb19d6465c8",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0824C4FF",
          "original": "0x08243A12",
          "target": "0x09084E40",
          "batch": "patch/batches/432_checklist_scripts.json"
        },
        {
          "address": "0x0824C54D",
          "original": "0x08243A12",
          "target": "0x09084E40",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13287 行 · untransplanted_full /  · gText_WhichFloorWouldYouLike

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
ミナモ　デパートへ　ようこそ！\pなんかいへ　いきますか？$
```

英文：

```text

```

报告原中文：

```text
欢迎来到水静百货。\p要去几层？$沙暴太强了，\n走不过去。$包包里的道具可以\n登录到SELECT上，方便使用。$有一封宝可梦训练家\n
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13287,
    "symbol": "gText_WhichFloorWouldYouLike",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "欢迎来到水静百货。\\p要去几层？$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "ミナモ　デパートへ　ようこそ！\\pなんかいへ　いきますか？$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_WhichFloorWouldYouLike",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x0908511C",
      "payload_sha256": "8423aedf33abfe800c3f098d2611e40cae72053439e4c27bbffa5bb3f5c7103b",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0820B1A6",
          "original": "0x08243A47",
          "target": "0x0908511C",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13288 行 · untransplanted_full /  · gText_SandstormIsVicious

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
さばくの　すなあらしが　ひどくて
さきに　すすめない！$
```

英文：

```text

```

报告原中文：

```text
沙暴太强了，\n走不过去。$包包里的道具可以\n登录到SELECT上，方便使用。$有一封宝可梦训练家\n学校来的电子邮件。\p…… …… ……\p1只宝可梦最多可以学4个招式。\p训练家的专业程度就可以从其\n为宝可梦所选择的招式中看出来。\p…… …… ……$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13288,
    "symbol": "gText_SandstormIsVicious",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "沙暴太强了，\n走不过去。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "さばくの　すなあらしが　ひどくて\nさきに　すすめない！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_SandstormIsVicious",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x0908503C",
      "payload_sha256": "1dc9fb172684665f460da1264bcb10a53012c8e1f8ac3cf591729315b807f77c",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x081EA3ED",
          "original": "0x08243A64",
          "target": "0x0908503C",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13289 行 · untransplanted_full /  · gText_SelectWithoutRegisteredItem

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
バッグに　いれてある　どうぐを
べんりボタンに　とうろく　できます$
```

英文：

```text

```

报告原中文：

```text
包包里的道具可以\n登录到SELECT上，方便使用。$有一封宝可梦训练家\n学校来的电子邮件。\p…… …… ……\p1只宝可梦最多可以学4个招式。\p训练家的专业程度就可以从其\n为宝可梦所选择的招式中看出来。\p…… …… ……${PLAYER}登录了电脑。$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13289,
    "symbol": "gText_SelectWithoutRegisteredItem",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "包包里的道具可以\n登录到SELECT上，方便使用。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "バッグに　いれてある　どうぐを\nべんりボタンに　とうろく　できます$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_SelectWithoutRegisteredItem",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09085056",
      "payload_sha256": "3c76d918b1aff30b7629b413af982579fe89171217e7b3d7266f6130c2f0f956",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082440DF",
          "original": "0x08243A80",
          "target": "0x09085056",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13290 行 · untransplanted_full /  · gText_PokemonTrainerSchoolEmail

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
パソコンに
ポケモン　トレーナー　こうざの\lメールが　きている！\p⋯⋯　⋯⋯　⋯⋯\pポケモンが　おぼえられる　わざは　4つ！\pどんな　わざを　おぼえさせるかで
トレーナーの　じつりょくが　とわれます！\p⋯⋯　⋯⋯　⋯⋯$
```

英文：

```text

```

报告原中文：

```text
有一封宝可梦训练家\n学校来的电子邮件。\p…… …… ……\p1只宝可梦最多可以学4个招式。\p训练家的专业程度就可以从其\n为宝可梦所选择的招式中看出来。\p…… …… ……${PLAYER}登录了电脑。$已取消连接。$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13290,
    "symbol": "gText_PokemonTrainerSchoolEmail",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "有一封宝可梦训练家\n学校来的电子邮件。\\p…… …… ……\\p1只宝可梦最多可以学4个招式。\\p训练家的专业程度就可以从其\n为宝可梦所选择的招式中看出来。\\p…… …… ……$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "パソコンに\nポケモン　トレーナー　こうざの\\lメールが　きている！\\p⋯⋯　⋯⋯　⋯⋯\\pポケモンが　おぼえられる　わざは　4つ！\\pどんな　わざを　おぼえさせるかで\nトレーナーの　じつりょくが　とわれます！\\p⋯⋯　⋯⋯　⋯⋯$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_PokemonTrainerSchoolEmail",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09084EE1",
      "payload_sha256": "d67de193ce88e4ec3aaccdde0412a861835615e5559218be9cd126cf8595e837",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x081F01FD",
          "original": "0x08243AA2",
          "target": "0x09084EE1",
          "batch": "patch/batches/432_checklist_scripts.json"
        },
        {
          "address": "0x081F0DBA",
          "original": "0x08243AA2",
          "target": "0x09084EE1",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13291 行 · untransplanted_full /  · gText_PlayerHouseBootPC

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{PLAYER}は　パソコンの
スイッチを　いれた！$
```

英文：

```text

```

报告原中文：

```text
{PLAYER}登录了电脑。$已取消连接。$Want to give a nickname to\nthe {STR_VAR_2} you received?${PLAYER}没有可以\n战斗的宝可梦\p！{PLAYER}昏迷了！$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13291,
    "symbol": "gText_PlayerHouseBootPC",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "{PLAYER}登录了电脑。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "{PLAYER}は　パソコンの\nスイッチを　いれた！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_PlayerHouseBootPC",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09084E8E",
      "payload_sha256": "11337994758f7a149cfb2887c38156c31f6e86c9ff01a46307f83a88e4f555b4",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x081F01E2",
          "original": "0x08243B10",
          "target": "0x09084E8E",
          "batch": "patch/batches/432_checklist_scripts.json"
        },
        {
          "address": "0x081F0DCF",
          "original": "0x08243B10",
          "target": "0x09084E8E",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13292 行 · untransplanted_full /  · gText_PokeblockLinkCanceled

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
つうしんは　キャンセルされました$
```

英文：

```text

```

报告原中文：

```text
已取消连接。$Want to give a nickname to\nthe {STR_VAR_2} you received?${PLAYER}没有可以\n战斗的宝可梦\p！{PLAYER}昏迷了！$把{STR_VAR_1} {STR_VAR_2}\n
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13292,
    "symbol": "gText_PokeblockLinkCanceled",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "已取消连接。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "つうしんは　キャンセルされました$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_PokeblockLinkCanceled",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09084ED2",
      "payload_sha256": "1726ed4651e8eaab76996bfd3d6e609d6ab75e7909a1653304cc5401eaa91dd3",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x082592C5",
          "original": "0x08243B25",
          "target": "0x09084ED2",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13293 行 · untransplanted_full /  · gText_PlayerWhitedOut

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{PLAYER}の　てもとには
たたかえるポケモンが　もういない！\p{PLAYER}は
めのまえが　まっくらに　なった！$
```

英文：

```text

```

报告原中文：

```text
{PLAYER}没有可以\n战斗的宝可梦\p！{PLAYER}昏迷了！$把{STR_VAR_1} {STR_VAR_2}\n登记到宝可导航里了。$你知道招式学习器秘密之力吗？\p我们这些人都喜欢\n招式学习器秘密之力。\p我们的成员之一会把它送给你，\n
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13293,
    "symbol": "gText_PlayerWhitedOut",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "{PLAYER}没有可以\n战斗的宝可梦\\p！{PLAYER}昏迷了！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "{PLAYER}の　てもとには\nたたかえるポケモンが　もういない！\\p{PLAYER}は\nめのまえが　まっくらに　なった！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_PlayerWhitedOut",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09084EA3",
      "payload_sha256": "489e194afb7e6133336af9d1fb079f9009ac6325c6a3ac22c80ffa8941e237c8",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08244104",
          "original": "0x08243B4E",
          "target": "0x09084EA3",
          "batch": "patch/batches/432_checklist_scripts.json"
        },
        {
          "address": "0x08244123",
          "original": "0x08243B4E",
          "target": "0x09084EA3",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13294 行 · untransplanted_full /  · gText_RegisteredTrainerinPokeNav

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{STR_VAR_1}の　{STR_VAR_2}を
ポケナビに　とうろく　した！$
```

英文：

```text

```

报告原中文：

```text
把{STR_VAR_1} {STR_VAR_2}\n登记到宝可导航里了。$你知道招式学习器秘密之力吗？\p我们这些人都喜欢\n招式学习器秘密之力。\p我们的成员之一会把它送给你，\n拿到之后就回来给我看看吧。\p我们会让你成为我们之中的一员，\n还可以秘密卖给你些道具。$交给我的宝可梦\n
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13294,
    "symbol": "gText_RegisteredTrainerinPokeNav",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "把{STR_VAR_1} {STR_VAR_2}\n登记到宝可导航里了。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "{STR_VAR_1}の　{STR_VAR_2}を\nポケナビに　とうろく　した！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_RegisteredTrainerinPokeNav",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09085015",
      "payload_sha256": "bd5f1ec67e0171ccc1c48365ea3f3e88b0088187d4f597ae63a018335cea4bdb",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08244D04",
          "original": "0x08243B7F",
          "target": "0x09085015",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13295 行 · untransplanted_full /  · gText_ComeBackWithSecretPower

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
‘ひみつのちから'って
わざマシン　しってる？\pおれら　わざマシン　‘ひみつのちから'が
だいすき　なんだ\pおれらの　メンバーが　どこかで　くれるから
それを　もらったら　また　おいで！\pきみも　メンバーとして
ひみつで　いいものを　うってあげるよ$
```

英文：

```text

```

报告原中文：

```text
你知道招式学习器秘密之力吗？\p我们这些人都喜欢\n招式学习器秘密之力。\p我们的成员之一会把它送给你，\n拿到之后就回来给我看看吧。\p我们会让你成为我们之中的一员，\n还可以秘密卖给你些道具。$交给我的宝可梦\n似乎附上了宝可病毒。\p详细情况不太清楚，\n不过据说，所谓宝可病毒是一种\l附着在宝可梦身上的微小生命体。\p而且在病毒附着期间\n
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13295,
    "symbol": "gText_ComeBackWithSecretPower",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "你知道招式学习器秘密之力吗？\\p我们这些人都喜欢\n招式学习器秘密之力。\\p我们的成员之一会把它送给你，\n拿到之后就回来给我看看吧。\\p我们会让你成为我们之中的一员，\n还可以秘密卖给你些道具。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "‘ひみつのちから'って\nわざマシン　しってる？\\pおれら　わざマシン　‘ひみつのちから'が\nだいすき　なんだ\\pおれらの　メンバーが　どこかで　くれるから\nそれを　もらったら　また　おいで！\\pきみも　メンバーとして\nひみつで　いいものを　うってあげるよ$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_gText_ComeBackWithSecretPower",
      "file": "patch/batches/434_checklist_verified_objects.json",
      "payload_address": "0x090854F0",
      "payload_sha256": "3a96e2384e8da8eaabdc2ef45e52148ec179a22774287a73e5495fd4bc2f3762",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x081DC504",
          "original": "0x08243B96",
          "target": "0x090854F0",
          "batch": "patch/batches/434_checklist_verified_objects.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13296 行 · untransplanted_full /  · gText_PokerusExplanation

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
おあずかりした　ポケモンに
ポケルスが　ついて　いるようです\pくわしいことは　わかって　いないのですが
ポケルスと　いうのは　ポケモンに　くっつく\lちいさな　せいめいたいで\lこれが　ついている　あいだ\lポケモンが　よく　そだつ　みたいです$
```

英文：

```text

```

报告原中文：

```text
交给我的宝可梦\n似乎附上了宝可病毒。\p详细情况不太清楚，\n不过据说，所谓宝可病毒是一种\l附着在宝可梦身上的微小生命体。\p而且在病毒附着期间\n宝可梦好像会成长得特别快。$似乎听到了远处\n某扇门打开了的声音。$墙上有一个大洞。$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13296,
    "symbol": "gText_PokerusExplanation",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "交给我的宝可梦\n似乎附上了宝可病毒。\\p详细情况不太清楚，\n不过据说，所谓宝可病毒是一种\\l附着在宝可梦身上的微小生命体。\\p而且在病毒附着期间\n宝可梦好像会成长得特别快。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "おあずかりした　ポケモンに\nポケルスが　ついて　いるようです\\pくわしいことは　わかって　いないのですが\nポケルスと　いうのは　ポケモンに　くっつく\\lちいさな　せいめいたいで\\lこれが　ついている　あいだ\\lポケモンが　よく　そだつ　みたいです$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_PokerusExplanation",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09084F72",
      "payload_sha256": "9d9142cd133f76f9cb88c0a66a1fba8b053937f9e1c9987f1c0bfa4c2b27de40",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08242AFA",
          "original": "0x08243C13",
          "target": "0x09084F72",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13297 行 · untransplanted_full /  · gText_DoorOpenedFarAway

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
どこか　とおくの　とびらが
ひらいたような　おとだ⋯⋯$
```

英文：

```text

```

报告原中文：

```text
似乎听到了远处\n某扇门打开了的声音。$墙上有一个大洞。$非常抱歉，\n宝可梦无线俱乐部\l系统正在调整。$似乎正在进行\n调整的样子……$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13297,
    "symbol": "gText_DoorOpenedFarAway",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "似乎听到了远处\n某扇门打开了的声音。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "どこか　とおくの　とびらが\nひらいたような　おとだ⋯⋯$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_DoorOpenedFarAway",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09084E05",
      "payload_sha256": "8e8fead750a4db8e9871a9ded0abea9b7b5525c000b2938d2209b816c0befa70",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0821BB8A",
          "original": "0x08243CBE",
          "target": "0x09084E05",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13298 行 · untransplanted_full /  · gText_BigHoleInTheWall

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
かべに　おおきな　あなが　あいている！$
```

英文：

```text

```

报告原中文：

```text
墙上有一个大洞。$非常抱歉，\n宝可梦无线俱乐部\l系统正在调整。$似乎正在进行\n调整的样子……$I'm terribly sorry. The TRADE CENTER\n
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13298,
    "symbol": "gText_BigHoleInTheWall",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "墙上有一个大洞。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "かべに　おおきな　あなが　あいている！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_BigHoleInTheWall",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09084DF2",
      "payload_sha256": "0aad156e3801f9c0d76a0ac7627d9fa71a40de4883b710fea936af7f0015d989",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08213E74",
          "original": "0x08243CDA",
          "target": "0x09084DF2",
          "batch": "patch/batches/432_checklist_scripts.json"
        },
        {
          "address": "0x0821B85A",
          "original": "0x08243CDA",
          "target": "0x09084DF2",
          "batch": "patch/batches/432_checklist_scripts.json"
        },
        {
          "address": "0x0821B98D",
          "original": "0x08243CDA",
          "target": "0x09084DF2",
          "batch": "patch/batches/432_checklist_scripts.json"
        },
        {
          "address": "0x0821BB2A",
          "original": "0x08243CDA",
          "target": "0x09084DF2",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13299 行 · untransplanted_full /  · gText_SorryWirelessClubAdjustments

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
もうしわけ　ございません
ポケモン　ワイヤレス　クラブは\lただいま　ちょうせいちゅう　です$
```

英文：

```text

```

报告原中文：

```text
非常抱歉，\n宝可梦无线俱乐部\l系统正在调整。$似乎正在进行\n调整的样子……$I'm terribly sorry. The TRADE CENTER\nis undergoing inspections.$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13299,
    "symbol": "gText_SorryWirelessClubAdjustments",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "非常抱歉，\n宝可梦无线俱乐部\\l系统正在调整。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "もうしわけ　ございません\nポケモン　ワイヤレス　クラブは\\lただいま　ちょうせいちゅう　です$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_SorryWirelessClubAdjustments",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09085084",
      "payload_sha256": "606511a1ab576290da66c3a6eaa6e7f983824603af55e8df7fb84f7fb96307d2",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08247016",
          "original": "0x08243CEE",
          "target": "0x09085084",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13300 行 · untransplanted_full /  · gText_UndergoingAdjustments

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
ちょうせいちゅうの　ようだ$
```

英文：

```text

```

报告原中文：

```text
似乎正在进行\n调整的样子……$I'm terribly sorry. The TRADE CENTER\nis undergoing inspections.$I'm terribly sorry. The RECORD CORNER\n
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13300,
    "symbol": "gText_UndergoingAdjustments",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "似乎正在进行\n调整的样子……$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "ちょうせいちゅうの　ようだ$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_UndergoingAdjustments",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09085100",
      "payload_sha256": "deb8d1278a20d91a0baa9bb355402c7975c177434ae27345011255833a4e414a",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08247020",
          "original": "0x08243D1C",
          "target": "0x09085100",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13301 行 · untransplanted_full /  · gText_PlayerHandedOverTheItem

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{PLAYER}は
{STR_VAR_1}を　わたした！$
```

英文：

```text

```

报告原中文：

```text
{PLAYER}\n交出了{STR_VAR_1}。$感谢连接\n神秘礼物系统。${PLAYER}找到了{STR_VAR_1}\n“{STR_VAR_2}”！$奇怪的树不喜欢\n
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13301,
    "symbol": "gText_PlayerHandedOverTheItem",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "{PLAYER}\n交出了{STR_VAR_1}。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "{PLAYER}は\n{STR_VAR_1}を　わたした！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_PlayerHandedOverTheItem",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09084E76",
      "payload_sha256": "57a25be67073ab35d708aab840cf79c8e32d198ee1174774249d4c187084e515",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0824346F",
          "original": "0x08243D82",
          "target": "0x09084E76",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13302 行 · untransplanted_full /  · gText_ThankYouForAccessingMysteryGift

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
ふしぎな　おくりものを　ごりよう
いただき　ありがとう　ございます！$
```

英文：

```text

```

报告原中文：

```text
感谢连接\n神秘礼物系统。${PLAYER}找到了{STR_VAR_1}\n“{STR_VAR_2}”！$奇怪的树不喜欢\n吼吼鲸洒水壶！\p奇怪的树攻击了过来！${STR_VAR_1}消失不见了……$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13302,
    "symbol": "gText_ThankYouForAccessingMysteryGift",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "感谢连接\n神秘礼物系统。$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "ふしぎな　おくりものを　ごりよう\nいただき　ありがとう　ございます！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_ThankYouForAccessingMysteryGift",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x090850E6",
      "payload_sha256": "b98324358d1f121fdf4a959a2a480d5cd99cb3fc4f564d672861756d2dd410ef",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0824681A",
          "original": "0x08243D90",
          "target": "0x090850E6",
          "batch": "patch/batches/432_checklist_scripts.json"
        },
        {
          "address": "0x08246862",
          "original": "0x08243D90",
          "target": "0x090850E6",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13303 行 · untransplanted_full /  · gText_PlayerFoundOneTMHM

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{PLAYER}は　{STR_VAR_1}
‘{STR_VAR_2}'を　みつけた！$
```

英文：

```text

```

报告原中文：

```text
{PLAYER}找到了{STR_VAR_1}\n“{STR_VAR_2}”！$奇怪的树不喜欢\n吼吼鲸洒水壶！\p奇怪的树攻击了过来！${STR_VAR_1}消失不见了……$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13303,
    "symbol": "gText_PlayerFoundOneTMHM",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "{PLAYER}找到了{STR_VAR_1}\n“{STR_VAR_2}”！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "{PLAYER}は　{STR_VAR_1}\n‘{STR_VAR_2}'を　みつけた！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_ChecklistLiteral_439_gText_PlayerFoundOneTMHM",
      "file": "patch/batches/439_checklist_common_placeholders.json",
      "payload_address": "0x0908BE1D",
      "payload_sha256": "52174ebc61b7c69ddf96c3be0e47062ec5f481d7a5b3d5504a673d55f95fba12",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08242D28",
          "original": "0x08243DB3",
          "target": "0x0908BE1D",
          "batch": "patch/batches/439_checklist_common_placeholders.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13304 行 · untransplanted_full /  · gText_Sudowoodo_Attacked

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
おかしな　きは
ホエルコじょうろを　いやがっている！\pおかしな　きが　おそいかかってきた！$
```

英文：

```text

```

报告原中文：

```text
奇怪的树不喜欢\n吼吼鲸洒水壶！\p奇怪的树攻击了过来！${STR_VAR_1}消失不见了……$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13304,
    "symbol": "gText_Sudowoodo_Attacked",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "奇怪的树不喜欢\n吼吼鲸洒水壶！\\p奇怪的树攻击了过来！$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "おかしな　きは\nホエルコじょうろを　いやがっている！\\pおかしな　きが　おそいかかってきた！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_Sudowoodo_Attacked",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x090850B1",
      "payload_sha256": "2aa1a32048c77bb9c4ea24e5bb683412aa509cbe0c62685450570cdc73a74f44",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x08222AAF",
          "original": "0x08243DC6",
          "target": "0x090850B1",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13305 行 · untransplanted_full /  · gText_LegendaryFlewAway

判定：`already_ported_verified`

理由：必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。

日文：

```text
{STR_VAR_1}は
どこかへ　とびさって　いった！$
```

英文：

```text

```

报告原中文：

```text
{STR_VAR_1}消失不见了……$
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13305,
    "symbol": "gText_LegendaryFlewAway",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "必须按已验证对象/别名或现有覆盖核对，报告缺独立符号不等于缺中文；保留当前文字，记录实际覆盖证据。",
    "action": "verify_mapping"
  },
  "source": {
    "us_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "{STR_VAR_1}消失不见了……$"
      }
    ],
    "wokann_sources": [
      {
        "file": "data/event_scripts.s",
        "text": "{STR_VAR_1}は\nどこかへ　とびさって　いった！$"
      }
    ]
  },
  "mapping": [
    {
      "payload_symbol": "Chs_Checklist_gText_LegendaryFlewAway",
      "file": "patch/batches/432_checklist_scripts.json",
      "payload_address": "0x09084E2B",
      "payload_sha256": "bb7d57eba2a72db4ec64141953d7a08b73124aebfdf06221ebee3d912605aa68",
      "rom_bytes_match": true,
      "references": [
        {
          "address": "0x0821C002",
          "original": "0x08243DF4",
          "target": "0x09084E2B",
          "batch": "patch/batches/432_checklist_scripts.json"
        },
        {
          "address": "0x082441AD",
          "original": "0x08243DF4",
          "target": "0x09084E2B",
          "batch": "patch/batches/432_checklist_scripts.json"
        }
      ]
    }
  ]
}
```

### CSV 第 13396 行 · untransplanted_full /  · gMoveNames[12]

判定：`unsupported_terminology_claim`

理由：命名属于既定中文本地化术语；报告把旧译名当作唯一官方译名，未给可验证出处，不凭逐词直译替换现有招式名。

日文：

```text
ハサミギロチン$
```

英文：

```text
GUILLOTINE
```

报告原中文：

```text
极落钳
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13396,
    "symbol": "gMoveNames[12]",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "命名属于既定中文本地化术语；报告把旧译名当作唯一官方译名，未给可验证出处，不凭逐词直译替换现有招式名。",
    "action": "unsupported_terminology_claim"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/move_names.json",
      "table": "ChsMoveNames",
      "index": 12,
      "text": "极落钳",
      "rom_address": "0x09095190",
      "encoded_sha256": "42d432a10d72dd78ac544348d327963d56d819691f917cdb44fdc38694fbb833",
      "rom_bytes_match": true
    }
  ]
}
```

### CSV 第 13450 行 · untransplanted_full /  · gMoveNames[66]

判定：`unsupported_terminology_claim`

理由：命名属于既定中文本地化术语；报告把旧译名当作唯一官方译名，未给可验证出处，不凭逐词直译替换现有招式名。

日文：

```text
じごくぐるま$$
```

英文：

```text
SUBMISSION
```

报告原中文：

```text
深渊翻滚
```

修复前实际中文：

```text

```

最终中文：

```text

```

证据：

```json
{
  "review": {
    "row_number": 13450,
    "symbol": "gMoveNames[66]",
    "domain": "untransplanted_full",
    "idx": "",
    "reason": "命名属于既定中文本地化术语；报告把旧译名当作唯一官方译名，未给可验证出处，不凭逐词直译替换现有招式名。",
    "action": "unsupported_terminology_claim"
  },
  "source": {
    "us_sources": [],
    "wokann_sources": []
  },
  "mapping": [
    {
      "file": "patch/move_names.json",
      "table": "ChsMoveNames",
      "index": 66,
      "text": "深渊翻滚",
      "rom_address": "0x090954F0",
      "encoded_sha256": "30c857fd20382c4a4a236f1e0e6c57fb846c0fe7eb64e003800a749918c5e4ed",
      "rom_bytes_match": true
    }
  ]
}
```

## 原143条待追踪项的最终判定

### CSV 第 10745 行 · TrainerHill_Entrance_Text_StillGettingReady

判定：`regional_no_counterpart_verified`

理由：美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10745,
  "symbol": "TrainerHill_Entrance_Text_StillGettingReady",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "line": 186,
      "text": "msgbox TrainerHill_Entrance_Text_StillGettingReady, MSGBOX_DEFAULT"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "line": 283,
      "text": "TrainerHill_Entrance_Text_StillGettingReady:"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "sha256": "49730d0d4cac5516bd183d769947de84725f31e6acdc555bf5650bed54f220b2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "sha256": "11a0a764a99b7bec09f0b82d0268cf399385d679910fa091f6b0cba468e7fcd2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/battle_frontier/trainer_hill.h",
      "sha256": "776f2704d6c08804d24779fb995c5ad10081d1e87fd987591c3448328e4d5c17"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/trainer_hill.c",
      "sha256": "2c9eceed407cadae379a50030855700dcd326e8db7e8ebc376cd49465ebf2421"
    }
  ]
}
```

### CSV 第 10748 行 · TrainerHill_Entrance_Text_CantWaitToTestTheWaters

判定：`regional_no_counterpart_verified`

理由：美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10748,
  "symbol": "TrainerHill_Entrance_Text_CantWaitToTestTheWaters",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "line": 223,
      "text": "msgbox TrainerHill_Entrance_Text_CantWaitToTestTheWaters, MSGBOX_NPC"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "line": 354,
      "text": "TrainerHill_Entrance_Text_CantWaitToTestTheWaters:"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "sha256": "49730d0d4cac5516bd183d769947de84725f31e6acdc555bf5650bed54f220b2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "sha256": "11a0a764a99b7bec09f0b82d0268cf399385d679910fa091f6b0cba468e7fcd2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/battle_frontier/trainer_hill.h",
      "sha256": "776f2704d6c08804d24779fb995c5ad10081d1e87fd987591c3448328e4d5c17"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/trainer_hill.c",
      "sha256": "2c9eceed407cadae379a50030855700dcd326e8db7e8ebc376cd49465ebf2421"
    }
  ]
}
```

### CSV 第 10749 行 · TrainerHill_Entrance_Text_DoYouKnowWhenTheyOpen

判定：`regional_no_counterpart_verified`

理由：美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10749,
  "symbol": "TrainerHill_Entrance_Text_DoYouKnowWhenTheyOpen",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "line": 232,
      "text": "msgbox TrainerHill_Entrance_Text_DoYouKnowWhenTheyOpen, MSGBOX_NPC"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "line": 360,
      "text": "TrainerHill_Entrance_Text_DoYouKnowWhenTheyOpen:"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "sha256": "49730d0d4cac5516bd183d769947de84725f31e6acdc555bf5650bed54f220b2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "sha256": "11a0a764a99b7bec09f0b82d0268cf399385d679910fa091f6b0cba468e7fcd2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/battle_frontier/trainer_hill.h",
      "sha256": "776f2704d6c08804d24779fb995c5ad10081d1e87fd987591c3448328e4d5c17"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/trainer_hill.c",
      "sha256": "2c9eceed407cadae379a50030855700dcd326e8db7e8ebc376cd49465ebf2421"
    }
  ]
}
```

### CSV 第 10767 行 · sText_MysteryGiftOldSeaMapBagFull

判定：`already_ported_alias_verified`

理由：实际日版是同一消息的别名：真正开始在0x085FD1A1，vmessage参数0x085FD0F0已指向现有汉化，旧清单0x085FD1A5只指到中段。报告称日版无配信脚本过度推断；Wokann data/mystery_event_msg.s保留了该配信区。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_alias_verified",
  "reason": "实际日版是同一消息的别名：真正开始在0x085FD1A1，vmessage参数0x085FD0F0已指向现有汉化，旧清单0x085FD1A5只指到中段。报告称日版无配信脚本过度推断；Wokann data/mystery_event_msg.s保留了该配信区。",
  "aliases_payloads": [
    "Chs_ChecklistLiteral_463_sText_AuroraTicketBagFull"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10767,
  "symbol": "sText_MysteryGiftOldSeaMapBagFull",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/scripts/gift_old_sea_map.inc",
      "line": 24,
      "text": "vmessage sText_MysteryGiftOldSeaMapBagFull"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "data/scripts/gift_old_sea_map.inc",
      "line": 53,
      "text": "sText_MysteryGiftOldSeaMapBagFull:"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/scripts/gift_old_sea_map.inc",
      "sha256": "e035c82e4aba98e918179d1ba06fb07b0713b442d368b27bfefe430b4f480ecb"
    }
  ]
}
```

### CSV 第 10796 行 · CableClub_Text_CantMixWithJapaneseGame

判定：`regional_no_counterpart_verified`

理由：此文本属于海外版与日版混合记录的版本兼容性限制；JP cable_club脚本不含美版Japanese-game限制分支。保留日版原有联机判断，不注入错误的区域提示。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "此文本属于海外版与日版混合记录的版本兼容性限制；JP cable_club脚本不含美版Japanese-game限制分支。保留日版原有联机判断，不注入错误的区域提示。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10796,
  "symbol": "CableClub_Text_CantMixWithJapaneseGame",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/text/cable_club.inc",
      "line": 123,
      "text": "CableClub_Text_CantMixWithJapaneseGame:"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "data/scripts/cable_club.inc",
      "line": 558,
      "text": "msgbox CableClub_Text_CantMixWithJapaneseGame, MSGBOX_DEFAULT"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/scripts/cable_club.inc",
      "sha256": "a574e2f4b5471100049942fa945e73e107357e436b0a10034e1b569d531e2519"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "data/text/cable_club.inc",
      "sha256": "f7b2de549908a545b90d61d389647c7e64d86ea262a8929175a6f2ed3310557b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "data/scripts/cable_club.inc",
      "sha256": "d006fdc431233ff4f23dd3f4553c53f806f2f61aa2f34f3850bcb0a0712a2f04"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "data/text/cable_club.inc",
      "sha256": "f32c1e3c5d4bf6e9fe62c7105a7f6aa796576d2f14a0c27f27c06f5e5c4e95a4"
    }
  ]
}
```

### CSV 第 10823 行 · gText_MoveInterfacePPType

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10823,
  "symbol": "gText_MoveInterfacePPType",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "line": 1279,
      "text": "const u8 gText_MoveInterfacePPType[] = _(\"{PALETTE 5}{COLOR_HIGHLIGHT_SHADOW DYNAMIC_COLOR4 DYNAMIC_COLOR5 DYNAMIC_COLOR6}PP\\n属性/\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "line": 244,
      "text": "extern const u8 gText_MoveInterfacePPType[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "sha256": "e549eabe2a22b203bb4e2df7976b7b4874f1d7f6ccd2b9eb335cd46dee8feb19"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "sha256": "08d9e720b8f9e303beffa0740de040c9419bb0eeaec1af86b3be1c3397278004"
    }
  ]
}
```

### CSV 第 10829 行 · gText_SpaceAndSpace

判定：`regional_no_counterpart_verified`

理由：Wokann frontier_util.c sub_081A3B68把同一空格串用于列表开头和每个名字间隔，不区分英文最终and；原文0x085ABC6C只是空格。替换为和会给第一个名字也加和，不属于缺失汉化。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "Wokann frontier_util.c sub_081A3B68把同一空格串用于列表开头和每个名字间隔，不区分英文最终and；原文0x085ABC6C只是空格。替换为和会给第一个名字也加和，不属于缺失汉化。",
  "aliases_payloads": [],
  "pointer_expectations": [
    {
      "address": "0x081A3BC0",
      "target": "0x085ABC6C"
    },
    {
      "address": "0x081A3C08",
      "target": "0x085ABC6C"
    }
  ],
  "graphics": [],
  "row_number": 10829,
  "symbol": "gText_SpaceAndSpace",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "line": 1949,
      "text": "StringAppend(gStringVar1, gText_SpaceAndSpace);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "line": 1955,
      "text": "StringAppend(gStringVar1, gText_SpaceAndSpace);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "line": 1962,
      "text": "StringAppend(gStringVar1, gText_SpaceAndSpace);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "line": 1311,
      "text": "const u8 gText_SpaceAndSpace[] = _(\"和\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 1348,
      "text": "extern const u8 gText_SpaceAndSpace[];"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "line": 262,
      "text": "extern const u8 gText_SpaceAndSpace[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 1363,
      "text": "extern const u8 gText_SpaceAndSpace[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "line": 261,
      "text": "extern const u8 gText_SpaceAndSpace[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "sha256": "e549eabe2a22b203bb4e2df7976b7b4874f1d7f6ccd2b9eb335cd46dee8feb19"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "sha256": "08d9e720b8f9e303beffa0740de040c9419bb0eeaec1af86b3be1c3397278004"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "sha256": "be3ec95f9e438f385256ae8a55f53be70677f28d3fa44272f00f2e927c9b868c"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "sha256": "53095a779ff6a673f873ac8b7283e7d4a3aa14a48a872bbfd4a2e43f74b632e3"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/frontier_util.c",
      "sha256": "a5cdb426396e896d097c7cd35d8e00ada1c4585cec7c61c45f21ef725177e463"
    }
  ]
}
```

### CSV 第 10830 行 · gText_BattleWallyName

判定：`non_display_comparison_verified`

理由：此字符串是GetBattleBGM的StringCompare判定目标，不是显示入口。现有补丁把0x0806E0B4的比较目标指向满充实际训练家名字段0x082E8A40，以配合已汉化的训练家表；不再重复翻译独立比较常量。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "non_display_comparison_verified",
  "reason": "此字符串是GetBattleBGM的StringCompare判定目标，不是显示入口。现有补丁把0x0806E0B4的比较目标指向满充实际训练家名字段0x082E8A40，以配合已汉化的训练家表；不再重复翻译独立比较常量。",
  "aliases_payloads": [],
  "pointer_expectations": [
    {
      "address": "0x0806E0B4",
      "target": "0x082E8A40"
    }
  ],
  "graphics": [],
  "row_number": 10830,
  "symbol": "gText_BattleWallyName",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/pokemon.c",
      "line": 6523,
      "text": "if (!StringCompare(gTrainers[gTrainerBattleOpponent_A].trainerName, gText_BattleWallyName))"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "line": 1319,
      "text": "const u8 gText_BattleWallyName[] = _(\"满充\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "line": 270,
      "text": "extern const u8 gText_BattleWallyName[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "line": 269,
      "text": "extern const u8 gText_BattleWallyName[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "sha256": "e549eabe2a22b203bb4e2df7976b7b4874f1d7f6ccd2b9eb335cd46dee8feb19"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "sha256": "08d9e720b8f9e303beffa0740de040c9419bb0eeaec1af86b3be1c3397278004"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/pokemon.c",
      "sha256": "3d1df2637cfac27730a579b9a1ab637b96cb55321df87be744ca22435edf62c3"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "sha256": "53095a779ff6a673f873ac8b7283e7d4a3aa14a48a872bbfd4a2e43f74b632e3"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/pokemon.c",
      "sha256": "41d737504f6a0de8ea07cf3f1cd527fb5641980e5f60c6555c5d828c41f96b6f"
    }
  ]
}
```

### CSV 第 10831 行 · gText_TheGreatNewHope

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10831,
  "symbol": "gText_TheGreatNewHope",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "line": 1364,
      "text": "const u8 gText_TheGreatNewHope[] = _(\"伟大的崭新希望！\\p\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "line": 279,
      "text": "extern const u8 gText_TheGreatNewHope[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "line": 278,
      "text": "extern const u8 gText_TheGreatNewHope[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "sha256": "e549eabe2a22b203bb4e2df7976b7b4874f1d7f6ccd2b9eb335cd46dee8feb19"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "sha256": "08d9e720b8f9e303beffa0740de040c9419bb0eeaec1af86b3be1c3397278004"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "sha256": "53095a779ff6a673f873ac8b7283e7d4a3aa14a48a872bbfd4a2e43f74b632e3"
    }
  ]
}
```

### CSV 第 10832 行 · gText_WillChampionshipDreamComeTrue

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10832,
  "symbol": "gText_WillChampionshipDreamComeTrue",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "line": 1365,
      "text": "const u8 gText_WillChampionshipDreamComeTrue[] = _(\"冠军之梦能否成真？！\\p\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "line": 280,
      "text": "extern const u8 gText_WillChampionshipDreamComeTrue[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "line": 279,
      "text": "extern const u8 gText_WillChampionshipDreamComeTrue[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "sha256": "e549eabe2a22b203bb4e2df7976b7b4874f1d7f6ccd2b9eb335cd46dee8feb19"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "sha256": "08d9e720b8f9e303beffa0740de040c9419bb0eeaec1af86b3be1c3397278004"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "sha256": "53095a779ff6a673f873ac8b7283e7d4a3aa14a48a872bbfd4a2e43f74b632e3"
    }
  ]
}
```

### CSV 第 10833 行 · gText_AFormerChampion

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10833,
  "symbol": "gText_AFormerChampion",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "line": 1366,
      "text": "const u8 gText_AFormerChampion[] = _(\"前冠军！\\p\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "line": 281,
      "text": "extern const u8 gText_AFormerChampion[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "line": 280,
      "text": "extern const u8 gText_AFormerChampion[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "sha256": "e549eabe2a22b203bb4e2df7976b7b4874f1d7f6ccd2b9eb335cd46dee8feb19"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "sha256": "08d9e720b8f9e303beffa0740de040c9419bb0eeaec1af86b3be1c3397278004"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "sha256": "53095a779ff6a673f873ac8b7283e7d4a3aa14a48a872bbfd4a2e43f74b632e3"
    }
  ]
}
```

### CSV 第 10834 行 · gText_ThePreviousChampion

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10834,
  "symbol": "gText_ThePreviousChampion",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "line": 1367,
      "text": "const u8 gText_ThePreviousChampion[] = _(\"上届冠军！\\p\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "line": 282,
      "text": "extern const u8 gText_ThePreviousChampion[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "line": 281,
      "text": "extern const u8 gText_ThePreviousChampion[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "sha256": "e549eabe2a22b203bb4e2df7976b7b4874f1d7f6ccd2b9eb335cd46dee8feb19"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "sha256": "08d9e720b8f9e303beffa0740de040c9419bb0eeaec1af86b3be1c3397278004"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "sha256": "53095a779ff6a673f873ac8b7283e7d4a3aa14a48a872bbfd4a2e43f74b632e3"
    }
  ]
}
```

### CSV 第 10835 行 · gText_TheUnbeatenChampion

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10835,
  "symbol": "gText_TheUnbeatenChampion",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "line": 1368,
      "text": "const u8 gText_TheUnbeatenChampion[] = _(\"不败冠军！\\p\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "line": 283,
      "text": "extern const u8 gText_TheUnbeatenChampion[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "line": 282,
      "text": "extern const u8 gText_TheUnbeatenChampion[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "sha256": "e549eabe2a22b203bb4e2df7976b7b4874f1d7f6ccd2b9eb335cd46dee8feb19"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "sha256": "08d9e720b8f9e303beffa0740de040c9419bb0eeaec1af86b3be1c3397278004"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "sha256": "53095a779ff6a673f873ac8b7283e7d4a3aa14a48a872bbfd4a2e43f74b632e3"
    }
  ]
}
```

### CSV 第 10836 行 · gText_Judgment

判定：`fixed_consumer_verified`

理由：battle_arena.c: sArenaTextJudgment = gUnknown_85ABD3C + 0x72; both typed literal references feed TryGetStatusString; preserve buffer IDs 0/1.

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_consumer_verified",
  "reason": "battle_arena.c: sArenaTextJudgment = gUnknown_85ABD3C + 0x72; both typed literal references feed TryGetStatusString; preserve buffer IDs 0/1.",
  "aliases_payloads": [
    "Chs_V2_gText_Judgment"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "implementation": {
    "symbol": "gText_Judgment",
    "payload_symbol": "Chs_V2_gText_Judgment",
    "final_text": "{B_BUFF1}{CLEAR 13}判定{CLEAR 13}{B_BUFF2}",
    "us_source": {
      "file": "src/battle_message.c",
      "text": "{B_BUFF1}{CLEAR 13}判定{CLEAR 13}{B_BUFF2}"
    },
    "reason": "battle_arena.c: sArenaTextJudgment = gUnknown_85ABD3C + 0x72; both typed literal references feed TryGetStatusString; preserve buffer IDs 0/1.",
    "original_address": "0x085ABDAE",
    "original_hex": "fd0000001a2e13020000fd01ff",
    "wokann_references": [
      {
        "address": "0x081A4FA0",
        "original": "0x085ABDAE",
        "object": "build/pokeemerald-jp/src/battle_arena.o",
        "object_sha256": "8d0919e248785c63125db9ec2d0fa2abcbe5bb5dbdd0fc469e41b05e2c52385f",
        "section": ".text",
        "section_base": "0x081A4E28",
        "section_length": 3556,
        "relocation": "R_ARM_ABS32",
        "referenced_symbol": "gUnknown_85ABD3C",
        "section_offset": 376
      },
      {
        "address": "0x081A5078",
        "original": "0x085ABDAE",
        "object": "build/pokeemerald-jp/src/battle_arena.o",
        "object_sha256": "8d0919e248785c63125db9ec2d0fa2abcbe5bb5dbdd0fc469e41b05e2c52385f",
        "section": ".text",
        "section_base": "0x081A4E28",
        "section_length": 3556,
        "relocation": "R_ARM_ABS32",
        "referenced_symbol": "gUnknown_85ABD3C",
        "section_offset": 592
      }
    ]
  },
  "row_number": 10836,
  "symbol": "gText_Judgment",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_arena.c",
      "line": 420,
      "text": "BattleStringExpandPlaceholdersToDisplayedString(gText_Judgment);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_arena.c",
      "line": 444,
      "text": "BattleStringExpandPlaceholdersToDisplayedString(gText_Judgment);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_arena.c",
      "line": 453,
      "text": "BattleStringExpandPlaceholdersToDisplayedString(gText_Judgment);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_arena.c",
      "line": 462,
      "text": "BattleStringExpandPlaceholdersToDisplayedString(gText_Judgment);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "line": 1375,
      "text": "const u8 gText_Judgment[] = _(\"{B_BUFF1}{CLEAR 13}判定{CLEAR 13}{B_BUFF2}\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "line": 290,
      "text": "extern const u8 gText_Judgment[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "line": 289,
      "text": "extern const u8 gText_Judgment[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/battle_message.h",
      "sha256": "e549eabe2a22b203bb4e2df7976b7b4874f1d7f6ccd2b9eb335cd46dee8feb19"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_arena.c",
      "sha256": "a8e0ff7edd9bc8264afcfc2e2d2ef3b69bb94f6262c588167045d325dd4da4e3"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_message.c",
      "sha256": "08d9e720b8f9e303beffa0740de040c9419bb0eeaec1af86b3be1c3397278004"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/battle_message.h",
      "sha256": "53095a779ff6a673f873ac8b7283e7d4a3aa14a48a872bbfd4a2e43f74b632e3"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/battle_arena.c",
      "sha256": "98183771e202ddc8a4a0e2a3051a65e0cef6feebea7521ab94e3d309d801aa97"
    }
  ]
}
```

### CSV 第 10924 行 · sText_BerryProgramUpdate

判定：`already_ported_graphics_verified`

理由：美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_graphics_verified",
  "reason": "美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "special_validation": "berry_fix_graphics",
  "row_number": 10924,
  "symbol": "sText_BerryProgramUpdate",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 37,
      "text": "static const u8 sText_BerryProgramUpdate[] = _(\"树果问题修复补丁程序\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 319,
      "text": "width = GetStringWidth(FONT_NORMAL, sText_BerryProgramUpdate, 0);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 321,
      "text": "AddTextPrinterParameterized3(WIN_TITLE, FONT_NORMAL, left, 2, sBerryProgramTextColors, TEXT_SKIP_DRAW, sText_BerryProgramUpdate);"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "sha256": "932355e20865f1bdacdd119efa5fbe7f3163a48aa59062cc3d2c021f11e84b6f"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/berry_fix_graphics.c",
      "sha256": "fd9d0133752e34bdaa0aa3c110fee78aefa60c977b387356490b82cce51eb85c"
    }
  ]
}
```

### CSV 第 10925 行 · sText_RubySapphire

判定：`already_ported_graphics_verified`

理由：美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_graphics_verified",
  "reason": "美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "special_validation": "berry_fix_graphics",
  "row_number": 10925,
  "symbol": "sText_RubySapphire",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 38,
      "text": "static const u8 sText_RubySapphire[] = _(\"红宝石·蓝宝石\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 311,
      "text": "width = GetStringWidth(FONT_SMALL, sText_RubySapphire, 0);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 313,
      "text": "AddTextPrinterParameterized3(WIN_GAME_NAMES, FONT_SMALL, left, 3, sGameTitleTextColors, TEXT_SKIP_DRAW, sText_RubySapphire);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 315,
      "text": "width = GetStringWidth(FONT_SMALL, sText_RubySapphire, 0);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 317,
      "text": "AddTextPrinterParameterized3(WIN_TURN_OFF_TITLE, FONT_SMALL, left, 0, sGameTitleTextColors, TEXT_SKIP_DRAW, sText_RubySapphire);"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "sha256": "932355e20865f1bdacdd119efa5fbe7f3163a48aa59062cc3d2c021f11e84b6f"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/berry_fix_graphics.c",
      "sha256": "fd9d0133752e34bdaa0aa3c110fee78aefa60c977b387356490b82cce51eb85c"
    }
  ]
}
```

### CSV 第 10926 行 · sText_Emerald

判定：`already_ported_graphics_verified`

理由：美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_graphics_verified",
  "reason": "美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "special_validation": "berry_fix_graphics",
  "row_number": 10926,
  "symbol": "sText_Emerald",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 39,
      "text": "static const u8 sText_Emerald[] = _(\"绿宝石\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 307,
      "text": "width = GetStringWidth(FONT_SMALL, sText_Emerald, 0);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 309,
      "text": "AddTextPrinterParameterized3(WIN_GAME_NAMES, FONT_SMALL, left, 3, sGameTitleTextColors, TEXT_SKIP_DRAW, sText_Emerald);"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "sha256": "932355e20865f1bdacdd119efa5fbe7f3163a48aa59062cc3d2c021f11e84b6f"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/berry_fix_graphics.c",
      "sha256": "fd9d0133752e34bdaa0aa3c110fee78aefa60c977b387356490b82cce51eb85c"
    }
  ]
}
```

### CSV 第 10927 行 · sText_BerryProgramWillBeUpdatedPressA

判定：`already_ported_graphics_verified`

理由：美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_graphics_verified",
  "reason": "美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "special_validation": "berry_fix_graphics",
  "row_number": 10927,
  "symbol": "sText_BerryProgramWillBeUpdatedPressA",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 40,
      "text": "static const u8 sText_BerryProgramWillBeUpdatedPressA[] = _(\"{COLOR DARK_GRAY}{SHADOW LIGHT_GRAY}{CLEAR_TO 24}针对精灵宝可梦：红宝石·蓝宝石\\n\""
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 140,
      "text": "[SCENE_BEGIN]           = sText_BerryProgramWillBeUpdatedPressA"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "sha256": "932355e20865f1bdacdd119efa5fbe7f3163a48aa59062cc3d2c021f11e84b6f"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/berry_fix_graphics.c",
      "sha256": "fd9d0133752e34bdaa0aa3c110fee78aefa60c977b387356490b82cce51eb85c"
    }
  ]
}
```

### CSV 第 10928 行 · sText_EnsureGBAConnectionMatches

判定：`already_ported_graphics_verified`

理由：美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_graphics_verified",
  "reason": "美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "special_validation": "berry_fix_graphics",
  "row_number": 10928,
  "symbol": "sText_EnsureGBAConnectionMatches",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 43,
      "text": "static const u8 sText_EnsureGBAConnectionMatches[] = _(\"{COLOR DARK_GRAY}{SHADOW LIGHT_GRAY}请确认2台GBA游戏机\\n\""
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 135,
      "text": "[SCENE_ENSURE_CONNECT]  = sText_EnsureGBAConnectionMatches,"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "sha256": "932355e20865f1bdacdd119efa5fbe7f3163a48aa59062cc3d2c021f11e84b6f"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/berry_fix_graphics.c",
      "sha256": "fd9d0133752e34bdaa0aa3c110fee78aefa60c977b387356490b82cce51eb85c"
    }
  ]
}
```

### CSV 第 10929 行 · sText_TurnOffPowerHoldingStartSelect

判定：`already_ported_graphics_verified`

理由：美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_graphics_verified",
  "reason": "美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "special_validation": "berry_fix_graphics",
  "row_number": 10929,
  "symbol": "sText_TurnOffPowerHoldingStartSelect",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 47,
      "text": "static const u8 sText_TurnOffPowerHoldingStartSelect[] = _(\"{COLOR DARK_GRAY}{SHADOW LIGHT_GRAY}请一边按住START键和SELECT键，一边打开\\n\""
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 136,
      "text": "[SCENE_TURN_OFF_POWER]  = sText_TurnOffPowerHoldingStartSelect,"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "sha256": "932355e20865f1bdacdd119efa5fbe7f3163a48aa59062cc3d2c021f11e84b6f"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/berry_fix_graphics.c",
      "sha256": "fd9d0133752e34bdaa0aa3c110fee78aefa60c977b387356490b82cce51eb85c"
    }
  ]
}
```

### CSV 第 10930 行 · sText_TransmittingPleaseWait

判定：`already_ported_graphics_verified`

理由：美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_graphics_verified",
  "reason": "美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "special_validation": "berry_fix_graphics",
  "row_number": 10930,
  "symbol": "sText_TransmittingPleaseWait",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 51,
      "text": "static const u8 sText_TransmittingPleaseWait[] = _(\"正在连接\\n\""
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 137,
      "text": "[SCENE_TRANSMITTING]    = sText_TransmittingPleaseWait,"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "sha256": "932355e20865f1bdacdd119efa5fbe7f3163a48aa59062cc3d2c021f11e84b6f"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/berry_fix_graphics.c",
      "sha256": "fd9d0133752e34bdaa0aa3c110fee78aefa60c977b387356490b82cce51eb85c"
    }
  ]
}
```

### CSV 第 10931 行 · sText_PleaseFollowInstructionsOnScreen

判定：`already_ported_graphics_verified`

理由：美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_graphics_verified",
  "reason": "美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "special_validation": "berry_fix_graphics",
  "row_number": 10931,
  "symbol": "sText_PleaseFollowInstructionsOnScreen",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 54,
      "text": "static const u8 sText_PleaseFollowInstructionsOnScreen[] = _(\"请根据红宝石·蓝宝石\\n\""
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 138,
      "text": "[SCENE_FOLLOW_INSTRUCT] = sText_PleaseFollowInstructionsOnScreen,"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "sha256": "932355e20865f1bdacdd119efa5fbe7f3163a48aa59062cc3d2c021f11e84b6f"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/berry_fix_graphics.c",
      "sha256": "fd9d0133752e34bdaa0aa3c110fee78aefa60c977b387356490b82cce51eb85c"
    }
  ]
}
```

### CSV 第 10932 行 · sText_TransmissionFailureTryAgain

判定：`already_ported_graphics_verified`

理由：美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_graphics_verified",
  "reason": "美版运行时打印字符串，日版LoadBerryFixGraphics加载已烘焙文字的六幅图。现有汉化生成器直接从美版berry_fix_program.c提取对应正文和标题；六幅ROM压缩资源已逐像素核验，区域外图案不变。不是遗漏的独立文本符号。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "special_validation": "berry_fix_graphics",
  "row_number": 10932,
  "symbol": "sText_TransmissionFailureTryAgain",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 56,
      "text": "static const u8 sText_TransmissionFailureTryAgain[] = _(\"\\n{CLEAR_TO 12}连接失败！\\n\""
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "line": 139,
      "text": "[SCENE_TRANSMIT_FAILED] = sText_TransmissionFailureTryAgain,"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_fix_program.c",
      "sha256": "932355e20865f1bdacdd119efa5fbe7f3163a48aa59062cc3d2c021f11e84b6f"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/berry_fix_graphics.c",
      "sha256": "fd9d0133752e34bdaa0aa3c110fee78aefa60c977b387356490b82cce51eb85c"
    }
  ]
}
```

### CSV 第 10935 行 · gText_ExpandedPlaceholder_Sapphire

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10935,
  "symbol": "gText_ExpandedPlaceholder_Sapphire",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 10,
      "text": "const u8 gText_ExpandedPlaceholder_Sapphire[] = _(\"蓝宝石\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 8,
      "text": "extern const u8 gText_ExpandedPlaceholder_Sapphire[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 8,
      "text": "extern const u8 gText_ExpandedPlaceholder_Sapphire[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    }
  ]
}
```

### CSV 第 10936 行 · gText_ExpandedPlaceholder_Ruby

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10936,
  "symbol": "gText_ExpandedPlaceholder_Ruby",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 11,
      "text": "const u8 gText_ExpandedPlaceholder_Ruby[] = _(\"红宝石\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 9,
      "text": "extern const u8 gText_ExpandedPlaceholder_Ruby[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 9,
      "text": "extern const u8 gText_ExpandedPlaceholder_Ruby[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    }
  ]
}
```

### CSV 第 10948 行 · gText_Player

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10948,
  "symbol": "gText_Player",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 39,
      "text": "const u8 gText_Player[] = _(\"玩家\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10949 行 · gText_Pokedex

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10949,
  "symbol": "gText_Pokedex",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 40,
      "text": "const u8 gText_Pokedex[] = _(\"图鉴\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10950 行 · gText_Badges

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10950,
  "symbol": "gText_Badges",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 42,
      "text": "const u8 gText_Badges[] = _(\"徽章\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10951 行 · gText_AButton

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10951,
  "symbol": "gText_AButton",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 43,
      "text": "const u8 gText_AButton[] = _(\"A键\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10952 行 · gText_BButton

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10952,
  "symbol": "gText_BButton",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 44,
      "text": "const u8 gText_BButton[] = _(\"B键\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10953 行 · gText_RButton

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10953,
  "symbol": "gText_RButton",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 45,
      "text": "const u8 gText_RButton[] = _(\"R键\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10954 行 · gText_LButton

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10954,
  "symbol": "gText_LButton",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 46,
      "text": "const u8 gText_LButton[] = _(\"L键\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10955 行 · gText_Start

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10955,
  "symbol": "gText_Start",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 47,
      "text": "const u8 gText_Start[] = _(\"比起\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10956 行 · gText_Select

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10956,
  "symbol": "gText_Select",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 48,
      "text": "const u8 gText_Select[] = _(\"选择\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10957 行 · gText_ControlPad

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10957,
  "symbol": "gText_ControlPad",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 49,
      "text": "const u8 gText_ControlPad[] = _(\"+ 十字键\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10958 行 · gText_LButtonRButton

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10958,
  "symbol": "gText_LButtonRButton",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 50,
      "text": "const u8 gText_LButtonRButton[] = _(\"L键  R键\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10959 行 · gText_Controls

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10959,
  "symbol": "gText_Controls",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 51,
      "text": "const u8 gText_Controls[] = _(\"控制器\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10960 行 · gText_PickOk

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10960,
  "symbol": "gText_PickOk",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 52,
      "text": "ALIGNED(4) const u8 gText_PickOk[] = _(\"{DPAD_UPDOWN}选择 {A_BUTTON}好\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10961 行 · gText_Next

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10961,
  "symbol": "gText_Next",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 53,
      "text": "ALIGNED(4) const u8 gText_Next[] = _(\"{A_BUTTON}下个\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10962 行 · gText_NextBack

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10962,
  "symbol": "gText_NextBack",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 54,
      "text": "ALIGNED(4) const u8 gText_NextBack[] = _(\"{A_BUTTON}下个 {B_BUTTON}返回\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10966 行 · gText_HTHeight

判定：`already_ported_graphics_verified`

理由：日版身高、体重为详情页图块标签；既有build_pokedex_info_gfx.py在图块0x100..0x10B及两处地图位置生成中文。当前ROM解压内容与汉化资源一致。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_graphics_verified",
  "reason": "日版身高、体重为详情页图块标签；既有build_pokedex_info_gfx.py在图块0x100..0x10B及两处地图位置生成中文。当前ROM解压内容与汉化资源一致。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [
    {
      "payload_symbol": "ChsPokedexInfoTilesGfx",
      "file": "patch/gfx/pokedex_info_tiles.4bpp",
      "pointer_address": "0x80bbd6c",
      "compressed": true,
      "decompressed_sha256": "dd630cf473b71211d12ce9726c9a62886e902156e338fb060a22b1c0f99f3e40"
    },
    {
      "payload_symbol": "ChsPokedexInfoTilemap",
      "file": "patch/gfx/pokedex_info_tilemap.bin",
      "pointer_address": "0x80be2e8",
      "compressed": true,
      "decompressed_sha256": "7c69bec22c91b22ac1abd82d222b6141b5ee5f18678e581332d59eadba197eb5"
    }
  ],
  "row_number": 10966,
  "symbol": "gText_HTHeight",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/pokedex.c",
      "line": 4173,
      "text": "PrintInfoScreenText(gText_HTHeight, 0x60, 0x39);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 112,
      "text": "const u8 gText_HTHeight[] = _(\"身高\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 530,
      "text": "extern const u8 gText_HTHeight[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 545,
      "text": "extern const u8 gText_HTHeight[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/pokedex.c",
      "sha256": "cca16be5a53754f8e8232fc74543ad70b2b94b997bee0020518f15ab3812e62c"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/pokedex.c",
      "sha256": "eec88a2a38d8d304c246b2184eee1be27559cc39e421ad920c7bf550f802f3f4"
    }
  ]
}
```

### CSV 第 10967 行 · gText_WTWeight

判定：`already_ported_graphics_verified`

理由：日版身高、体重为详情页图块标签；既有build_pokedex_info_gfx.py在图块0x100..0x10B及两处地图位置生成中文。当前ROM解压内容与汉化资源一致。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_graphics_verified",
  "reason": "日版身高、体重为详情页图块标签；既有build_pokedex_info_gfx.py在图块0x100..0x10B及两处地图位置生成中文。当前ROM解压内容与汉化资源一致。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [
    {
      "payload_symbol": "ChsPokedexInfoTilesGfx",
      "file": "patch/gfx/pokedex_info_tiles.4bpp",
      "pointer_address": "0x80bbd6c",
      "compressed": true,
      "decompressed_sha256": "dd630cf473b71211d12ce9726c9a62886e902156e338fb060a22b1c0f99f3e40"
    },
    {
      "payload_symbol": "ChsPokedexInfoTilemap",
      "file": "patch/gfx/pokedex_info_tilemap.bin",
      "pointer_address": "0x80be2e8",
      "compressed": true,
      "decompressed_sha256": "7c69bec22c91b22ac1abd82d222b6141b5ee5f18678e581332d59eadba197eb5"
    }
  ],
  "row_number": 10967,
  "symbol": "gText_WTWeight",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/pokedex.c",
      "line": 4174,
      "text": "PrintInfoScreenText(gText_WTWeight, 0x60, 0x49);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 113,
      "text": "const u8 gText_WTWeight[] = _(\"体重\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 531,
      "text": "extern const u8 gText_WTWeight[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 546,
      "text": "extern const u8 gText_WTWeight[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/pokedex.c",
      "sha256": "cca16be5a53754f8e8232fc74543ad70b2b94b997bee0020518f15ab3812e62c"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/pokedex.c",
      "sha256": "eec88a2a38d8d304c246b2184eee1be27559cc39e421ad920c7bf550f802f3f4"
    }
  ]
}
```

### CSV 第 10968 行 · gText_HOFDexRating

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10968,
  "symbol": "gText_HOFDexRating",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 167,
      "text": "const u8 gText_HOFDexRating[] = _(\"已发现的宝可梦：{STR_VAR_1}！\\n已捕捉的宝可梦：{STR_VAR_2}！\\p小田卷博士的图鉴评价！\\p小田卷博士：让我看看……\\p\");"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10969 行 · gText_HOFDexSaving

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10969,
  "symbol": "gText_HOFDexSaving",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 168,
      "text": "const u8 gText_HOFDexSaving[] = _(\"正在写入记录……\\n请勿切断电源。\");"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10970 行 · gText_Pokemon4

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10970,
  "symbol": "gText_Pokemon4",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 179,
      "text": "const u8 gText_Pokemon4[] = _(\"宝可梦\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10971 行 · gText_Cancel7

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10971,
  "symbol": "gText_Cancel7",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 192,
      "text": "const u8 gText_Cancel7[] = _(\"取消\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10972 行 · gText_Berry2

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10972,
  "symbol": "gText_Berry2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 219,
      "text": "const u8 gText_Berry2[] = _(\"树果\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10978 行 · gText_Tasty

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10978,
  "symbol": "gText_Tasty",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 331,
      "text": "const u8 gText_Tasty[] = _(\"美味\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10979 行 · gText_Feel

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10979,
  "symbol": "gText_Feel",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 332,
      "text": "const u8 gText_Feel[] = _(\"细腻度\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10980 行 · gText_Moves

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10980,
  "symbol": "gText_Moves",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 368,
      "text": "const u8 gText_Moves[] = _(\"招式\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10981 行 · gText_PkmnRegainhedHealth

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10981,
  "symbol": "gText_PkmnRegainhedHealth",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 416,
      "text": "const u8 gText_PkmnRegainhedHealth[] = _(\"{STR_VAR_1}回复体力了！{PAUSE_UNTIL_PRESS}\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10982 行 · gText_TeachWhichPokemon2

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10982,
  "symbol": "gText_TeachWhichPokemon2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 428,
      "text": "const u8 gText_TeachWhichPokemon2[] = _(\"要让哪只宝可梦学习？\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10983 行 · gText_Events

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10983,
  "symbol": "gText_Events",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 505,
      "text": "const u8 gText_Events[] = _(\"事件\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10984 行 · gText_ApostropheSBase

判定：`fixed_consumer_verified`

理由：secret_base.c GetSecretBaseName copies saved trainer name then appends display suffix. Compact token occupies same 4 bytes including EOS as original; persistent trainerName bytes remain Japanese.

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_consumer_verified",
  "reason": "secret_base.c GetSecretBaseName copies saved trainer name then appends display suffix. Compact token occupies same 4 bytes including EOS as original; persistent trainerName bytes remain Japanese.",
  "aliases_payloads": [
    "Chs_V2_gText_ApostropheSBase"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "implementation": {
    "symbol": "gText_ApostropheSBase",
    "payload_symbol": "Chs_V2_gText_ApostropheSBase",
    "final_text": "的基地",
    "us_source": {
      "file": "src/strings.c",
      "text": "的基地"
    },
    "reason": "secret_base.c GetSecretBaseName copies saved trainer name then appends display suffix. Compact token occupies same 4 bytes including EOS as original; persistent trainerName bytes remain Japanese.",
    "original_address": "0x085CA654",
    "original_hex": "000711ff",
    "wokann_references": [
      {
        "address": "0x080EA468",
        "original": "0x085CA654",
        "object": "build/pokeemerald-jp/src/secret_base.o",
        "object_sha256": "282a337077ef0ef5d1ed0838a7102ba69de51bc36e4a39ddfee00c6b5e168ae8",
        "section": ".text",
        "section_base": "0x080E977C",
        "section_length": 13060,
        "relocation": "R_ARM_ABS32",
        "referenced_symbol": "gUnknown_85CA593",
        "section_offset": 3308
      }
    ]
  },
  "row_number": 10984,
  "symbol": "gText_ApostropheSBase",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 530,
      "text": "const u8 gText_ApostropheSBase[] = _(\"的基地\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/secret_base.c",
      "line": 732,
      "text": "return StringAppend(dest, gText_ApostropheSBase);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 166,
      "text": "extern const u8 gText_ApostropheSBase[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 166,
      "text": "extern const u8 gText_ApostropheSBase[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/secret_base.c",
      "sha256": "ab21b7e4e1786ebada597ed2252f8a1efbd7f41efe32b45d1bff1c2a47ddb1cf"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/secret_base.c",
      "sha256": "7459e4483a9e49270d674337d13506b9b5278be9592bc35a42ecd70796524310"
    }
  ]
}
```

### CSV 第 10985 行 · gText_MustBePlacedOnDesk

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10985,
  "symbol": "gText_MustBePlacedOnDesk",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 560,
      "text": "const u8 gText_MustBePlacedOnDesk[] = _(\"无法放在这里。\\n这里只能放桌子。\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10987 行 · gText_Littleroot

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10987,
  "symbol": "gText_Littleroot",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 606,
      "text": "const u8 gText_Littleroot[] = _(\"未白镇\"); // Unused. Given the context, Briney may at one point have been able to sail the player here"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10988 行 · gText_Lilycove

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10988,
  "symbol": "gText_Lilycove",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 607,
      "text": "const u8 gText_Lilycove[] = _(\"水静市\");     // Unused. Given the context, Briney may at one point have been able to sail the player here"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10989 行 · gText_Judging

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10989,
  "symbol": "gText_Judging",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 614,
      "text": "const u8 gText_Judging[] = _(\"判定\"); //unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10990 行 · gText_Count

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10990,
  "symbol": "gText_Count",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 622,
      "text": "const u8 gText_Count[] = _(\"计数\"); //unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10991 行 · gText_Toxic

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10991,
  "symbol": "gText_Toxic",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 632,
      "text": "const u8 gText_Toxic[] = _(\"剧毒\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10992 行 · gText_Ok3

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10992,
  "symbol": "gText_Ok3",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 633,
      "text": "const u8 gText_Ok3[] = _(\"好了\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10993 行 · gText_Quit

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10993,
  "symbol": "gText_Quit",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 634,
      "text": "const u8 gText_Quit[] = _(\"退出\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10994 行 · gText_Info4

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10994,
  "symbol": "gText_Info4",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 639,
      "text": "const u8 gText_Info4[] = _(\"查看信息\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 10995 行 · gText_MrBriney

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 10995,
  "symbol": "gText_MrBriney",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 643,
      "text": "const u8 gText_MrBriney[] = _(\"哈奇老人\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11002 行 · gText_NormalTagMatch

判定：`regional_no_counterpart_verified`

理由：美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11002,
  "symbol": "gText_NormalTagMatch",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 753,
      "text": "const u8 gText_NormalTagMatch[] = _(\"普通类比赛\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/trainer_hill.c",
      "line": 244,
      "text": "[HILL_MODE_NORMAL]  = gText_NormalTagMatch,"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/script_menu.h",
      "line": 767,
      "text": "{gText_NormalTagMatch},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 1292,
      "text": "extern const u8 gText_NormalTagMatch[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 1307,
      "text": "extern const u8 gText_NormalTagMatch[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/script_menu.h",
      "sha256": "ed471a1750e878835b86f23665980e9f93e0a21e75405a5bfc37c55cb63375c9"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/trainer_hill.c",
      "sha256": "f628db860bce7bd1548dcf3dcc080cc037a2e2c0672db449b082c8a49d11334a"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "sha256": "11a0a764a99b7bec09f0b82d0268cf399385d679910fa091f6b0cba468e7fcd2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/battle_frontier/trainer_hill.h",
      "sha256": "776f2704d6c08804d24779fb995c5ad10081d1e87fd987591c3448328e4d5c17"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/trainer_hill.c",
      "sha256": "2c9eceed407cadae379a50030855700dcd326e8db7e8ebc376cd49465ebf2421"
    }
  ]
}
```

### CSV 第 11003 行 · gText_VarietyTagMatch

判定：`regional_no_counterpart_verified`

理由：美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11003,
  "symbol": "gText_VarietyTagMatch",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 754,
      "text": "const u8 gText_VarietyTagMatch[] = _(\"多样类比赛\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/trainer_hill.c",
      "line": 245,
      "text": "[HILL_MODE_VARIETY] = gText_VarietyTagMatch,"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/script_menu.h",
      "line": 768,
      "text": "{gText_VarietyTagMatch},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 1293,
      "text": "extern const u8 gText_VarietyTagMatch[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 1308,
      "text": "extern const u8 gText_VarietyTagMatch[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/script_menu.h",
      "sha256": "ed471a1750e878835b86f23665980e9f93e0a21e75405a5bfc37c55cb63375c9"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/trainer_hill.c",
      "sha256": "f628db860bce7bd1548dcf3dcc080cc037a2e2c0672db449b082c8a49d11334a"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "sha256": "11a0a764a99b7bec09f0b82d0268cf399385d679910fa091f6b0cba468e7fcd2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/battle_frontier/trainer_hill.h",
      "sha256": "776f2704d6c08804d24779fb995c5ad10081d1e87fd987591c3448328e4d5c17"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/trainer_hill.c",
      "sha256": "2c9eceed407cadae379a50030855700dcd326e8db7e8ebc376cd49465ebf2421"
    }
  ]
}
```

### CSV 第 11004 行 · gText_UniqueTagMatch

判定：`regional_no_counterpart_verified`

理由：美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11004,
  "symbol": "gText_UniqueTagMatch",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 755,
      "text": "const u8 gText_UniqueTagMatch[] = _(\"唯一类比赛\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/trainer_hill.c",
      "line": 246,
      "text": "[HILL_MODE_UNIQUE]  = gText_UniqueTagMatch,"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/script_menu.h",
      "line": 769,
      "text": "{gText_UniqueTagMatch},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 1294,
      "text": "extern const u8 gText_UniqueTagMatch[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 1309,
      "text": "extern const u8 gText_UniqueTagMatch[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/script_menu.h",
      "sha256": "ed471a1750e878835b86f23665980e9f93e0a21e75405a5bfc37c55cb63375c9"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/trainer_hill.c",
      "sha256": "f628db860bce7bd1548dcf3dcc080cc037a2e2c0672db449b082c8a49d11334a"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "sha256": "11a0a764a99b7bec09f0b82d0268cf399385d679910fa091f6b0cba468e7fcd2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/battle_frontier/trainer_hill.h",
      "sha256": "776f2704d6c08804d24779fb995c5ad10081d1e87fd987591c3448328e4d5c17"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/trainer_hill.c",
      "sha256": "2c9eceed407cadae379a50030855700dcd326e8db7e8ebc376cd49465ebf2421"
    }
  ]
}
```

### CSV 第 11005 行 · gText_ExpertTagMatch

判定：`regional_no_counterpart_verified`

理由：美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "美版Trainer Hill包含殿堂前关闭分支和四种挑战模式；日版入口脚本直接使用trainerhill_getusingereader并开始挑战，没有对应关闭分支或HILL_MODE选择。已对照完整JP入口脚本、trainer_hill.c及数据，不能给不存在的资源伪造地址。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11005,
  "symbol": "gText_ExpertTagMatch",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 756,
      "text": "const u8 gText_ExpertTagMatch[] = _(\"专家类比赛\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/trainer_hill.c",
      "line": 247,
      "text": "[HILL_MODE_EXPERT]  = gText_ExpertTagMatch,"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/script_menu.h",
      "line": 770,
      "text": "{gText_ExpertTagMatch},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 1295,
      "text": "extern const u8 gText_ExpertTagMatch[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 1310,
      "text": "extern const u8 gText_ExpertTagMatch[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/script_menu.h",
      "sha256": "ed471a1750e878835b86f23665980e9f93e0a21e75405a5bfc37c55cb63375c9"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/trainer_hill.c",
      "sha256": "f628db860bce7bd1548dcf3dcc080cc037a2e2c0672db449b082c8a49d11334a"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "data/maps/TrainerHill_Entrance/scripts.inc",
      "sha256": "11a0a764a99b7bec09f0b82d0268cf399385d679910fa091f6b0cba468e7fcd2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/battle_frontier/trainer_hill.h",
      "sha256": "776f2704d6c08804d24779fb995c5ad10081d1e87fd987591c3448328e4d5c17"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/trainer_hill.c",
      "sha256": "2c9eceed407cadae379a50030855700dcd326e8db7e8ebc376cd49465ebf2421"
    }
  ]
}
```

### CSV 第 11008 行 · gText_YourPartysFull

判定：`already_ported_alias_verified`

理由：日版StorageMessage表的同行已满项共享PartyFull文本。0x0854CA8C已重定向，显示含义一致，不需要重复覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_alias_verified",
  "reason": "日版StorageMessage表的同行已满项共享PartyFull文本。0x0854CA8C已重定向，显示含义一致，不需要重复覆盖。",
  "aliases_payloads": [
    "Chs_ChecklistLiteral_448_gText_PartyFull"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11008,
  "symbol": "gText_YourPartysFull",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 876,
      "text": "const u8 gText_YourPartysFull[] = _(\"同行的宝可梦已满！{PAUSE_UNTIL_PRESS}\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/pokemon_storage_system.c",
      "line": 1081,
      "text": "[MSG_PARTY_FULL]           = {gText_YourPartysFull,          MSG_VAR_NONE},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 1994,
      "text": "extern const u8 gText_YourPartysFull[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2009,
      "text": "extern const u8 gText_YourPartysFull[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/pokemon_storage_system.c",
      "sha256": "ae564e3927689c21766f8dd3dc8b57ce431fc7195a76fd1d8c3e982d5931c219"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    }
  ]
}
```

### CSV 第 11012 行 · gText_WhatWouldYouLikeToDo

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11012,
  "symbol": "gText_WhatWouldYouLikeToDo",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 930,
      "text": "const u8 gText_WhatWouldYouLikeToDo[] = _(\"请选择。\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11013 行 · gText_Call2

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11013,
  "symbol": "gText_Call2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 963,
      "text": "const u8 gText_Call2[] = _(\"呼叫\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11014 行 · gText_UnusedExit

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11014,
  "symbol": "gText_UnusedExit",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 964,
      "text": "const u8 gText_UnusedExit[] = _(\"退出\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11015 行 · gText_NatureSlash

判定：`fixed_consumer_verified`

理由：use_pokeblock.c UpdateMonInfoText copies prefix to scratch at +0x804A then StringCopyPadded nature. Compact prefix occupies 3 bytes before EOS, max localized nature adds 9 bytes; fits 14-byte range before +0x8058.

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_consumer_verified",
  "reason": "use_pokeblock.c UpdateMonInfoText copies prefix to scratch at +0x804A then StringCopyPadded nature. Compact prefix occupies 3 bytes before EOS, max localized nature adds 9 bytes; fits 14-byte range before +0x8058.",
  "aliases_payloads": [
    "Chs_V2_gText_NatureSlash"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "implementation": {
    "symbol": "gText_NatureSlash",
    "payload_symbol": "Chs_V2_gText_NatureSlash",
    "final_text": "性格/",
    "us_source": {
      "file": "src/strings.c",
      "text": "性格/"
    },
    "reason": "use_pokeblock.c UpdateMonInfoText copies prefix to scratch at +0x804A then StringCopyPadded nature. Compact prefix occupies 3 bytes before EOS, max localized nature adds 9 bytes; fits 14-byte range before +0x8058.",
    "original_address": "0x085CB7A2",
    "original_hex": "0e020608baff",
    "wokann_references": [
      {
        "address": "0x08167A80",
        "original": "0x085CB7A2",
        "object": "build/pokeemerald-jp/src/use_pokeblock.o",
        "object_sha256": "a2d84f5ee43f8301458e57dc87b290fd6d99679bfb1475873b44ef3eb8a7d1aa",
        "section": ".text",
        "section_base": "0x08166010",
        "section_length": 8620,
        "relocation": "R_ARM_ABS32",
        "referenced_symbol": "gText_NumberOfBattles",
        "section_offset": 6768
      }
    ]
  },
  "row_number": 11015,
  "symbol": "gText_NatureSlash",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 981,
      "text": "const u8 gText_NatureSlash[] = _(\"性格/\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/use_pokeblock.c",
      "line": 1394,
      "text": "str = StringCopy(sMenu->info.natureText, gText_NatureSlash);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 32,
      "text": "extern const u8 gText_NatureSlash[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 32,
      "text": "extern const u8 gText_NatureSlash[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/use_pokeblock.c",
      "sha256": "5a3242ae92028f67c5323e3a3dfbf0cdbfea9fcb655ea93012ab27c3081945ae"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/use_pokeblock.c",
      "sha256": "b0ec9b7fcf16758ead28836cc1f27919fa959e0aad9147397bff82e7c53d1a69"
    }
  ]
}
```

### CSV 第 11016 行 · gText_AndMakeAMessage

判定：`fixed_consumer_verified`

理由：日版3列×2行输入把美版两段提示合成一句，过去只移植了第一段。现在将美版两段中文合并为完整一句；下一行保留并汉化日版独有的7字词语限制，不改变键盘、词语ID或输入布局。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_consumer_verified",
  "reason": "日版3列×2行输入把美版两段提示合成一句，过去只移植了第一段。现在将美版两段中文合并为完整一句；下一行保留并汉化日版独有的7字词语限制，不改变键盘、词语ID或输入布局。",
  "aliases_payloads": [
    "Chs_ChecklistLiteral_473_gText_CombineSixWordsOrPhrases",
    "Chs_V2_EasyChatSevenCharacters"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11016,
  "symbol": "gText_AndMakeAMessage",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 449,
      "text": ".instructionsText2 = gText_AndMakeAMessage,"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 461,
      "text": ".instructionsText2 = gText_AndMakeAMessage,"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 473,
      "text": ".instructionsText2 = gText_AndMakeAMessage,"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1001,
      "text": "const u8 gText_AndMakeAMessage[] = _(\"构成一段信息。\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2614,
      "text": "extern const u8 gText_AndMakeAMessage[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "sha256": "ee27e73604c0d93c0bfc7c956483cac219ad62221e2d10bcc0fb252570a2be26"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/easy_chat.c",
      "sha256": "f4a4a79ed1ed54d7b39f71eaa8301d3e11c5f4bb5a263589bf8bc76649e61cba"
    }
  ]
}
```

### CSV 第 11020 行 · gText_QuitEditing2

判定：`already_ported_alias_verified`

理由：第二份重复定义本身未引用；活跃QuitEditing在easy_chat.o的0x0811C388已汉化。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_alias_verified",
  "reason": "第二份重复定义本身未引用；活跃QuitEditing在easy_chat.o的0x0811C388已汉化。",
  "aliases_payloads": [
    "Chs_gText_QuitEditing"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11020,
  "symbol": "gText_QuitEditing2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1040,
      "text": "const u8 gText_QuitEditing2[] = _(\"停止编辑吗？\"); // Unused"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/strings.c",
      "line": 234,
      "text": "STRINGS_EASY_CHAT const u8 gText_QuitEditing2[] = _(\"へんしゅうを　やめますか？\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/strings.c",
      "sha256": "dcdac81163b41b04dddb1e039ee90e972dfcafac9bac78a3ef6f7d040160d06b"
    }
  ]
}
```

### CSV 第 11027 行 · gText_StopGivingPkmnMail2

判定：`already_ported_alias_verified`

理由：第二份重复定义未引用；活跃StopGivingPkmnMail在0x0811C35C已汉化。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_alias_verified",
  "reason": "第二份重复定义未引用；活跃StopGivingPkmnMail在0x0811C35C已汉化。",
  "aliases_payloads": [
    "Chs_gText_StopGivingPkmnMail"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11027,
  "symbol": "gText_StopGivingPkmnMail2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1050,
      "text": "const u8 gText_StopGivingPkmnMail2[] = _(\"放弃让宝可梦携带邮件吗？\"); // Unused"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/strings.c",
      "line": 244,
      "text": "STRINGS_EASY_CHAT const u8 gText_StopGivingPkmnMail2[] = _(\"メールを　もたせるのを　やめますか？\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/strings.c",
      "sha256": "dcdac81163b41b04dddb1e039ee90e972dfcafac9bac78a3ef6f7d040160d06b"
    }
  ]
}
```

### CSV 第 11030 行 · gText_First

判定：`regional_display_equivalent_verified`

理由：日版DoTVShowPokemonLotteryWinnerFlashReport不复制一等/二等/三等独立字符串，而把whichPrize交给TV_PrintIntToStringVar；已汉化的节目模板接收这个数字并显示奖级。新复制一个美版枚举字符串不会覆盖日版调用，不能据缺少符号判遗漏。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_display_equivalent_verified",
  "reason": "日版DoTVShowPokemonLotteryWinnerFlashReport不复制一等/二等/三等独立字符串，而把whichPrize交给TV_PrintIntToStringVar；已汉化的节目模板接收这个数字并显示奖级。新复制一个美版枚举字符串不会覆盖日版调用，不能据缺少符号判遗漏。",
  "aliases_payloads": [
    "Chs_gTVPokemonLotteryWinnerFlashReportText00"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11030,
  "symbol": "gText_First",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/tv.c",
      "line": 6018,
      "text": "StringCopy(gStringVar2, gText_First);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1124,
      "text": "const u8 gText_First[] = _(\"一等\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 110,
      "text": "extern const u8 gText_First[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 110,
      "text": "extern const u8 gText_First[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/tv.c",
      "sha256": "927fae4d009fd552e125100b62fd5ac8e020bdbef6061337d20746b143deb4fc"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/tv.c",
      "sha256": "3b402a76f5ae8c83c5a94ba7c52273ca33627f865a155722cc9438f816138688"
    }
  ]
}
```

### CSV 第 11031 行 · gText_Second

判定：`regional_display_equivalent_verified`

理由：日版DoTVShowPokemonLotteryWinnerFlashReport不复制一等/二等/三等独立字符串，而把whichPrize交给TV_PrintIntToStringVar；已汉化的节目模板接收这个数字并显示奖级。新复制一个美版枚举字符串不会覆盖日版调用，不能据缺少符号判遗漏。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_display_equivalent_verified",
  "reason": "日版DoTVShowPokemonLotteryWinnerFlashReport不复制一等/二等/三等独立字符串，而把whichPrize交给TV_PrintIntToStringVar；已汉化的节目模板接收这个数字并显示奖级。新复制一个美版枚举字符串不会覆盖日版调用，不能据缺少符号判遗漏。",
  "aliases_payloads": [
    "Chs_gTVPokemonLotteryWinnerFlashReportText00"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11031,
  "symbol": "gText_Second",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/tv.c",
      "line": 6020,
      "text": "StringCopy(gStringVar2, gText_Second);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1125,
      "text": "const u8 gText_Second[] = _(\"二等\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 111,
      "text": "extern const u8 gText_Second[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 111,
      "text": "extern const u8 gText_Second[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/tv.c",
      "sha256": "927fae4d009fd552e125100b62fd5ac8e020bdbef6061337d20746b143deb4fc"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/tv.c",
      "sha256": "3b402a76f5ae8c83c5a94ba7c52273ca33627f865a155722cc9438f816138688"
    }
  ]
}
```

### CSV 第 11032 行 · gText_Third

判定：`regional_display_equivalent_verified`

理由：日版DoTVShowPokemonLotteryWinnerFlashReport不复制一等/二等/三等独立字符串，而把whichPrize交给TV_PrintIntToStringVar；已汉化的节目模板接收这个数字并显示奖级。新复制一个美版枚举字符串不会覆盖日版调用，不能据缺少符号判遗漏。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_display_equivalent_verified",
  "reason": "日版DoTVShowPokemonLotteryWinnerFlashReport不复制一等/二等/三等独立字符串，而把whichPrize交给TV_PrintIntToStringVar；已汉化的节目模板接收这个数字并显示奖级。新复制一个美版枚举字符串不会覆盖日版调用，不能据缺少符号判遗漏。",
  "aliases_payloads": [
    "Chs_gTVPokemonLotteryWinnerFlashReportText00"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11032,
  "symbol": "gText_Third",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/tv.c",
      "line": 6022,
      "text": "StringCopy(gStringVar2, gText_Third);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1126,
      "text": "const u8 gText_Third[] = _(\"三等\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 112,
      "text": "extern const u8 gText_Third[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 112,
      "text": "extern const u8 gText_Third[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/tv.c",
      "sha256": "927fae4d009fd552e125100b62fd5ac8e020bdbef6061337d20746b143deb4fc"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/tv.c",
      "sha256": "3b402a76f5ae8c83c5a94ba7c52273ca33627f865a155722cc9438f816138688"
    }
  ]
}
```

### CSV 第 11035 行 · gText_Upper

判定：`regional_ui_already_localized`

理由：美版Upper/Lower表示拉丁键盘大小写；日版sKeyboardPageTitleTexts是平假名、片假名、ABC等页面。现有日版平假名/片假名标题已汉化，不能替换成大写/小写；键盘内容保持不变。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_ui_already_localized",
  "reason": "美版Upper/Lower表示拉丁键盘大小写；日版sKeyboardPageTitleTexts是平假名、片假名、ABC等页面。现有日版平假名/片假名标题已汉化，不能替换成大写/小写；键盘内容保持不变。",
  "aliases_payloads": [
    "Chs_URChatKb_平假名",
    "Chs_URChatKb_片假名"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11035,
  "symbol": "gText_Upper",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1250,
      "text": "const u8 gText_Upper[] = _(\"大写\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/union_room_chat.c",
      "line": 747,
      "text": "[UNION_ROOM_KB_PAGE_UPPER]    = {gText_Upper, {NULL}},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2849,
      "text": "extern const u8 gText_Upper[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2881,
      "text": "extern const u8 gText_Upper[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/union_room_chat.c",
      "sha256": "77aacf5b2453e7599f359d8788d0595ae1527f4841a09034aad3348c9eb06242"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/union_room8x.h",
      "sha256": "581d47d940bae7b1cd36eb0a22302c4f16f80b9326e2e38cdddec3bd5075b3ce"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/union_room_chat.c",
      "sha256": "2c71162e3ca1a767b7c1b2c4bdd93bbad4095f0581d1c59877386bb8641c04f2"
    }
  ]
}
```

### CSV 第 11036 行 · gText_Lower

判定：`regional_ui_already_localized`

理由：美版Upper/Lower表示拉丁键盘大小写；日版sKeyboardPageTitleTexts是平假名、片假名、ABC等页面。现有日版平假名/片假名标题已汉化，不能替换成大写/小写；键盘内容保持不变。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_ui_already_localized",
  "reason": "美版Upper/Lower表示拉丁键盘大小写；日版sKeyboardPageTitleTexts是平假名、片假名、ABC等页面。现有日版平假名/片假名标题已汉化，不能替换成大写/小写；键盘内容保持不变。",
  "aliases_payloads": [
    "Chs_URChatKb_平假名",
    "Chs_URChatKb_片假名"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11036,
  "symbol": "gText_Lower",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1251,
      "text": "const u8 gText_Lower[] = _(\"小写\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/union_room_chat.c",
      "line": 748,
      "text": "[UNION_ROOM_KB_PAGE_LOWER]    = {gText_Lower, {NULL}},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2850,
      "text": "extern const u8 gText_Lower[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2882,
      "text": "extern const u8 gText_Lower[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/union_room_chat.c",
      "sha256": "77aacf5b2453e7599f359d8788d0595ae1527f4841a09034aad3348c9eb06242"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/union_room8x.h",
      "sha256": "581d47d940bae7b1cd36eb0a22302c4f16f80b9326e2e38cdddec3bd5075b3ce"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/union_room_chat.c",
      "sha256": "2c71162e3ca1a767b7c1b2c4bdd93bbad4095f0581d1c59877386bb8641c04f2"
    }
  ]
}
```

### CSV 第 11037 行 · gText_Others

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11037,
  "symbol": "gText_Others",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1252,
      "text": "const u8 gText_Others[] = _(\"其他\");"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11039 行 · gText_BerryCrush2

判定：`fixed_consumer_verified`

理由：berry_crush.c ranking title: original gUnknown_85CCA70 is passed to width measurement and title printer.

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_consumer_verified",
  "reason": "berry_crush.c ranking title: original gUnknown_85CCA70 is passed to width measurement and title printer.",
  "aliases_payloads": [
    "Chs_V2_gText_BerryCrush2"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "implementation": {
    "symbol": "gText_BerryCrush2",
    "payload_symbol": "Chs_V2_gText_BerryCrush2",
    "final_text": "树果粉碎",
    "us_source": {
      "file": "src/strings.c",
      "text": "树果粉碎"
    },
    "reason": "berry_crush.c ranking title: original gUnknown_85CCA70 is passed to width measurement and title printer.",
    "original_address": "0x085CCA70",
    "original_hex": "0719205877a05c85ff",
    "wokann_references": [
      {
        "address": "0x080221B0",
        "original": "0x085CCA70",
        "object": "build/pokeemerald-jp/src/berry_crush.o",
        "object_sha256": "2951e01b57a8312bb4542b78364c6d6cc1532f0c7e9289e62fe0d7d7df3aa5cf",
        "section": ".text.sub_08021FC0",
        "section_base": "0x08021FC0",
        "section_length": 624,
        "relocation": "R_ARM_ABS32",
        "referenced_symbol": "gUnknown_85CCA70",
        "section_offset": 496
      }
    ]
  },
  "row_number": 11039,
  "symbol": "gText_BerryCrush2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1326,
      "text": "const u8 gText_BerryCrush2[] = _(\"树果粉碎\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_crush.c",
      "line": 1812,
      "text": "xPos = 96 - GetStringWidth(FONT_NORMAL, gText_BerryCrush2, -1) / 2u;"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_crush.c",
      "line": 1813,
      "text": "AddTextPrinterParameterized3(tWindowId, FONT_NORMAL, xPos, 1, sTextColorTable[COLORID_BLUE], 0, gText_BerryCrush2);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2908,
      "text": "extern const u8 gText_BerryCrush2[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2940,
      "text": "extern const u8 gText_BerryCrush2[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_crush.c",
      "sha256": "eecf70d1135bb4b402061108df70b3a17f9ae6ad55728c910cf724405a64934e"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/berry_crush.c",
      "sha256": "6b1db336d37f42eaea8d572af08ca0a1f81e5bd77f15e1ba3aa91954b1277307"
    }
  ]
}
```

### CSV 第 11040 行 · gText_UnusedCancel

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11040,
  "symbol": "gText_UnusedCancel",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1332,
      "text": "const u8 gText_UnusedCancel[] = _(\"取消\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11052 行 · gText_LinkContestResults

判定：`fixed_consumer_verified`

理由：frontier_util.c contest records title expanded into gStringVar4; original player placeholder 1 is Japanese playerName.

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_consumer_verified",
  "reason": "frontier_util.c contest records title expanded into gStringVar4; original player placeholder 1 is Japanese playerName.",
  "aliases_payloads": [
    "Chs_V2_gText_LinkContestResults"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "implementation": {
    "symbol": "gText_LinkContestResults",
    "payload_symbol": "Chs_V2_gText_LinkContestResults",
    "final_text": "{PLAYER}的连接华丽大赛成绩",
    "us_source": {
      "file": "src/strings.c",
      "text": "{PLAYER}的连接华丽大赛成绩"
    },
    "reason": "frontier_util.c contest records title expanded into gStringVar4; original player placeholder 1 is Japanese playerName.",
    "original_address": "0x085CCEA5",
    "original_hex": "fd01190012030c2e005a7e635d64000e020e07ff",
    "wokann_references": [
      {
        "address": "0x081A2F60",
        "original": "0x085CCEA5",
        "object": "build/pokeemerald-jp/src/frontier_util.o",
        "object_sha256": "9a116d95e4a9449226dd5d0b13b33dac26c6170b22ec7a54ebfd1c30ba066605",
        "section": ".text",
        "section_base": "0x081A1628",
        "section_length": 14336,
        "relocation": "R_ARM_ABS32",
        "referenced_symbol": "gUnknown_85CCA7C",
        "section_offset": 6456
      }
    ]
  },
  "row_number": 11052,
  "symbol": "gText_LinkContestResults",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "line": 1490,
      "text": "StringExpandPlaceholders(gStringVar4, gText_LinkContestResults);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1399,
      "text": "const u8 gText_LinkContestResults[] = _(\"{PLAYER}的连接华丽大赛成绩\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 1343,
      "text": "extern const u8 gText_LinkContestResults[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 1358,
      "text": "extern const u8 gText_LinkContestResults[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "sha256": "be3ec95f9e438f385256ae8a55f53be70677f28d3fa44272f00f2e927c9b868c"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/frontier_util.c",
      "sha256": "a5cdb426396e896d097c7cd35d8e00ada1c4585cec7c61c45f21ef725177e463"
    }
  ]
}
```

### CSV 第 11053 行 · gText_Pokemon3

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11053,
  "symbol": "gText_Pokemon3",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1405,
      "text": "const u8 gText_Pokemon3[] = _(\"宝可梦\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11054 行 · gText_Lv502

判定：`already_ported_alias_verified`

理由：日版各记录窗口共用0x085DD40E的RecordsLv50。现有完整文字和指针覆盖已验证，独立美版Lv502不是额外的日版资源。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_alias_verified",
  "reason": "日版各记录窗口共用0x085DD40E的RecordsLv50。现有完整文字和指针覆盖已验证，独立美版Lv502不是额外的日版资源。",
  "aliases_payloads": [
    "Chs_ChecklistLiteral_gText_RecordsLv50"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11054,
  "symbol": "gText_Lv502",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "line": 1060,
      "text": "AddTextPrinterParameterized(gRecordsWindowId, FONT_NORMAL, gText_Lv502, 16, 49, TEXT_SKIP_DRAW, NULL);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "line": 1127,
      "text": "AddTextPrinterParameterized(gRecordsWindowId, FONT_NORMAL, gText_Lv502, 8, 33, TEXT_SKIP_DRAW, NULL);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "line": 1203,
      "text": "AddTextPrinterParameterized(gRecordsWindowId, FONT_NORMAL, gText_Lv502, 16, 49, TEXT_SKIP_DRAW, NULL);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "line": 1255,
      "text": "AddTextPrinterParameterized(gRecordsWindowId, FONT_NORMAL, gText_Lv502, 8, 33, TEXT_SKIP_DRAW, NULL);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "line": 1318,
      "text": "AddTextPrinterParameterized(gRecordsWindowId, FONT_NORMAL, gText_Lv502, 16, 49, TEXT_SKIP_DRAW, NULL);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "line": 1407,
      "text": "AddTextPrinterParameterized(gRecordsWindowId, FONT_NORMAL, gText_Lv502, 8, 33, TEXT_SKIP_DRAW, NULL);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "line": 1468,
      "text": "AddTextPrinterParameterized(gRecordsWindowId, FONT_NORMAL, gText_Lv502, 8, 49, TEXT_SKIP_DRAW, NULL);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1439,
      "text": "const u8 gText_Lv502[] = _(\"Lv. 50级\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 1324,
      "text": "extern const u8 gText_Lv502[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 1339,
      "text": "extern const u8 gText_Lv502[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "sha256": "be3ec95f9e438f385256ae8a55f53be70677f28d3fa44272f00f2e927c9b868c"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    }
  ]
}
```

### CSV 第 11056 行 · gText_TimesCleared

判定：`already_ported_alias_verified`

理由：日版共享0x085DD461模板，通过/连续过关显示项0x081A25EC已经重定向；统计变量仍由原PikePrintCleared生产。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_alias_verified",
  "reason": "日版共享0x085DD461模板，通过/连续过关显示项0x081A25EC已经重定向；统计变量仍由原PikePrintCleared生产。",
  "aliases_payloads": [
    "Chs_ChecklistLiteral_439_gText_FrontierFacilityClearStreak"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11056,
  "symbol": "gText_TimesCleared",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "line": 1260,
      "text": "PikePrintCleared(gText_Total, gText_TimesCleared, gSaveBlock2Ptr->frontier.pikeTotalStreaks[FRONTIER_LVL_50], 64, 114, 65);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "line": 1263,
      "text": "PikePrintCleared(gText_Total, gText_TimesCleared, gSaveBlock2Ptr->frontier.pikeTotalStreaks[FRONTIER_LVL_OPEN], 64, 114, 129);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1450,
      "text": "const u8 gText_TimesCleared[] = _(\"通过次数：{CLEAR 5}{STR_VAR_1}\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 1335,
      "text": "extern const u8 gText_TimesCleared[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 1350,
      "text": "extern const u8 gText_TimesCleared[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/frontier_util.c",
      "sha256": "be3ec95f9e438f385256ae8a55f53be70677f28d3fa44272f00f2e927c9b868c"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    }
  ]
}
```

### CSV 第 11077 行 · gText_Days

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11077,
  "symbol": "gText_Days",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1505,
      "text": "const u8 gText_Days[] = _(\"天\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11078 行 · gText_TimeColon2

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11078,
  "symbol": "gText_TimeColon2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1506,
      "text": "const u8 gText_TimeColon2[] = _(\"时间：\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11079 行 · gText_GameTime

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11079,
  "symbol": "gText_GameTime",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1507,
      "text": "const u8 gText_GameTime[] = _(\"游戏时间\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11080 行 · gText_RTCTime

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11080,
  "symbol": "gText_RTCTime",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1508,
      "text": "const u8 gText_RTCTime[] = _(\"时钟时间\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11081 行 · gText_UpdatedTime

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11081,
  "symbol": "gText_UpdatedTime",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1509,
      "text": "const u8 gText_UpdatedTime[] = _(\"更新时间\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11082 行 · gJPText_Player

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11082,
  "symbol": "gJPText_Player",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1536,
      "text": "const u8 gJPText_Player[] = _(\"玩家\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11083 行 · gText_ByeByeVar1

判定：`fixed_consumer_verified`

理由：JP/US原文占位符均为FD03（STR_VAR_2），无需重新编号；仅增加日文昵称模式包裹，保持交换及存档数据。Wokann trade.c STATE_BYE_BYE 有两个独立打印调用。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_consumer_verified",
  "reason": "JP/US原文占位符均为FD03（STR_VAR_2），无需重新编号；仅增加日文昵称模式包裹，保持交换及存档数据。Wokann trade.c STATE_BYE_BYE 有两个独立打印调用。",
  "aliases_payloads": [
    "Chs_V2_gText_ByeByeVar1"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "implementation": {
    "symbol": "gText_ByeByeVar1",
    "payload_symbol": "Chs_V2_gText_ByeByeVar1",
    "final_text": "再见，{STR_VAR_2}！",
    "us_source": {
      "file": "src/strings.c",
      "text": "再见，{STR_VAR_2}！"
    },
    "reason": "JP/US原文占位符均为FD03（STR_VAR_2），无需重新编号；仅增加日文昵称模式包裹，保持交换及存档数据。Wokann trade.c STATE_BYE_BYE 有两个独立打印调用。",
    "original_address": "0x0830D24F",
    "original_hex": "4602460200fd03abff",
    "wokann_references": [
      {
        "address": "0x0807BC10",
        "original": "0x0830D24F",
        "object": "build/pokeemerald-jp/src/trade.o",
        "object_sha256": "b3b6fd05a00e1bc78a1adf3cf4c18153645e5e281dfbd2de0296a523692ed56a",
        "section": ".text.DoTradeAnim_Cable",
        "section_base": "0x0807B624",
        "section_length": 5084,
        "relocation": "R_ARM_ABS32",
        "referenced_symbol": "gUnknown_830D24F",
        "section_offset": 1516
      },
      {
        "address": "0x0807CFEC",
        "original": "0x0830D24F",
        "object": "build/pokeemerald-jp/src/trade.o",
        "object_sha256": "b3b6fd05a00e1bc78a1adf3cf4c18153645e5e281dfbd2de0296a523692ed56a",
        "section": ".text.DoTradeAnim_Wireless",
        "section_base": "0x0807CA00",
        "section_length": 5196,
        "relocation": "R_ARM_ABS32",
        "referenced_symbol": "gUnknown_830D24F",
        "section_offset": 1516
      }
    ]
  },
  "row_number": 11083,
  "symbol": "gText_ByeByeVar1",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1549,
      "text": "const u8 gText_ByeByeVar1[] = _(\"再见，{STR_VAR_2}！\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/trade.c",
      "line": 3473,
      "text": "StringExpandPlaceholders(gStringVar4, gText_ByeByeVar1);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/trade.c",
      "line": 3944,
      "text": "StringExpandPlaceholders(gStringVar4, gText_ByeByeVar1);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2161,
      "text": "extern const u8 gText_ByeByeVar1[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2179,
      "text": "extern const u8 gText_ByeByeVar1[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/trade.c",
      "sha256": "e605c07cacf8521ffd41e90e5f8b55210a44aa479abc94980dc0fc665e6ec70f"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/trade.c",
      "sha256": "6580960fa2f930e89a8dc288220162c59581d563d3cd4040f9010e1301014183"
    }
  ]
}
```

### CSV 第 11084 行 · gText_MixingRecords

判定：`fixed_consumer_verified`

理由：record_mixing.c Task_MixingRecordsRecv passes gContestEffectFuncs+0xC0 to PrintTextOnRecordMixing. Separate from already localized completion at 0x08566CB1.

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_consumer_verified",
  "reason": "record_mixing.c Task_MixingRecordsRecv passes gContestEffectFuncs+0xC0 to PrintTextOnRecordMixing. Separate from already localized completion at 0x08566CB1.",
  "aliases_payloads": [
    "Chs_V2_gText_MixingRecords"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "implementation": {
    "symbol": "gText_MixingRecords",
    "payload_symbol": "Chs_V2_gText_MixingRecords",
    "final_text": "混合记录中……",
    "us_source": {
      "file": "src/strings.c",
      "text": "混合记录中……"
    },
    "reason": "record_mixing.c Task_MixingRecordsRecv passes gContestEffectFuncs+0xC0 to PrintTextOnRecordMixing. Separate from already localized completion at 0x08566CB1.",
    "original_address": "0x08566CA4",
    "original_hex": "7a5aae952d001f3f13021f0dff",
    "wokann_references": [
      {
        "address": "0x080E6B74",
        "original": "0x08566CA4",
        "object": "build/pokeemerald-jp/src/record_mixing.o",
        "object_sha256": "49e336afacbd0b633ec282a6e438ed2e8e8724babf374714440bfc1ed13c2d44",
        "section": ".text",
        "section_base": "0x080E63C4",
        "section_length": 7960,
        "relocation": "R_ARM_ABS32",
        "referenced_symbol": "gContestEffectFuncs",
        "section_offset": 1968
      }
    ]
  },
  "row_number": 11084,
  "symbol": "gText_MixingRecords",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1587,
      "text": "const u8 gText_MixingRecords[] = _(\"混合记录中……\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/record_mixing.c",
      "line": 396,
      "text": "PrintTextOnRecordMixing(gText_MixingRecords);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 176,
      "text": "extern const u8 gText_MixingRecords[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 176,
      "text": "extern const u8 gText_MixingRecords[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/record_mixing.c",
      "sha256": "04656395af99b72d75ee73f270d022f9949e4c8e55df9acb536e9f3a9759616c"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/record_mixing.c",
      "sha256": "25950d1c6ca61593b3c4357fc6b7695033065b313ec5d690b888017c945d537e"
    }
  ]
}
```

### CSV 第 11085 行 · gText_CantSelectSamePkmn

判定：`fixed_consumer_verified`

理由：battle_factory_screen.c Select_PrintCantSelectSameMon: directly passed to AddTextPrinterParameterized.

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_consumer_verified",
  "reason": "battle_factory_screen.c Select_PrintCantSelectSameMon: directly passed to AddTextPrinterParameterized.",
  "aliases_payloads": [
    "Chs_V2_gText_CantSelectSamePkmn"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "implementation": {
    "symbol": "gText_CantSelectSamePkmn",
    "payload_symbol": "Chs_V2_gText_CantSelectSamePkmn",
    "final_text": "不能选择相同的宝可梦。",
    "us_source": {
      "file": "src/strings.c",
      "text": "不能选择相同的宝可梦。"
    },
    "reason": "battle_factory_screen.c Select_PrintCantSelectSameMon: directly passed to AddTextPrinterParameterized.",
    "original_address": "0x085DBC11",
    "original_hex": "05153d9f59737e1a000427491f0e2eff",
    "wokann_references": [
      {
        "address": "0x0819B79C",
        "original": "0x085DBC11",
        "object": "build/pokeemerald-jp/src/battle_factory_screen.o",
        "object_sha256": "9cacfc05f87306ba915f9fa86bdf4aa94513119c47da1926d9e1de6267678ff8",
        "section": ".text",
        "section_base": "0x0819A0EC",
        "section_length": 22428,
        "relocation": "R_ARM_ABS32",
        "referenced_symbol": "gUnknown_85DBC11",
        "section_offset": 5808
      }
    ]
  },
  "row_number": 11085,
  "symbol": "gText_CantSelectSamePkmn",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_factory_screen.c",
      "line": 1914,
      "text": "AddTextPrinterParameterized(SELECT_WIN_INFO, FONT_NORMAL, gText_CantSelectSamePkmn, 2, 5, 0, NULL);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1623,
      "text": "const u8 gText_CantSelectSamePkmn[] = _(\"不能选择相同的宝可梦。\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 3001,
      "text": "extern const u8 gText_CantSelectSamePkmn[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 3033,
      "text": "extern const u8 gText_CantSelectSamePkmn[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/battle_factory_screen.c",
      "sha256": "915d7972dd64610ebe7e1f5824030de20bd5317524b9a65eb59dfafb2f382444"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/battle_factory_screen.c",
      "sha256": "3504657de45710102bc57c4fb3286df8c901d1e37d48fe7b964e7ed8fff460c5"
    }
  ]
}
```

### CSV 第 11086 行 · gText_F700Players

判定：`unused_table_verified`

理由：四条只被gTextTable_Players静态数组引用，而该数组在完整US源码中没有消费者。不能把数组内部的引用误认为游戏显示调用。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_table_verified",
  "reason": "四条只被gTextTable_Players静态数组引用，而该数组在完整US源码中没有消费者。不能把数组内部的引用误认为游戏显示调用。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "unused_parent": "gTextTable_Players",
  "row_number": 11086,
  "symbol": "gText_F700Players",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1650,
      "text": "const u8 gText_F700Players[] = _(\"{DYNAMIC 0}名玩家\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1656,
      "text": "gText_F700Players,"
    }
  ],
  "unused_parent_occurrences": [
    {
      "file": "src/strings.c",
      "line": 1655,
      "text": "const u8 *const gTextTable_Players[] = {"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11087 行 · gText_F701Players

判定：`unused_table_verified`

理由：四条只被gTextTable_Players静态数组引用，而该数组在完整US源码中没有消费者。不能把数组内部的引用误认为游戏显示调用。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_table_verified",
  "reason": "四条只被gTextTable_Players静态数组引用，而该数组在完整US源码中没有消费者。不能把数组内部的引用误认为游戏显示调用。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "unused_parent": "gTextTable_Players",
  "row_number": 11087,
  "symbol": "gText_F701Players",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1651,
      "text": "const u8 gText_F701Players[] = _(\"{DYNAMIC 1}名玩家\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1657,
      "text": "gText_F701Players,"
    }
  ],
  "unused_parent_occurrences": [
    {
      "file": "src/strings.c",
      "line": 1655,
      "text": "const u8 *const gTextTable_Players[] = {"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11088 行 · gText_F702Players

判定：`unused_table_verified`

理由：四条只被gTextTable_Players静态数组引用，而该数组在完整US源码中没有消费者。不能把数组内部的引用误认为游戏显示调用。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_table_verified",
  "reason": "四条只被gTextTable_Players静态数组引用，而该数组在完整US源码中没有消费者。不能把数组内部的引用误认为游戏显示调用。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "unused_parent": "gTextTable_Players",
  "row_number": 11088,
  "symbol": "gText_F702Players",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1652,
      "text": "const u8 gText_F702Players[] = _(\"{DYNAMIC 2}名玩家\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1658,
      "text": "gText_F702Players,"
    }
  ],
  "unused_parent_occurrences": [
    {
      "file": "src/strings.c",
      "line": 1655,
      "text": "const u8 *const gTextTable_Players[] = {"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11089 行 · gText_F703Players

判定：`unused_table_verified`

理由：四条只被gTextTable_Players静态数组引用，而该数组在完整US源码中没有消费者。不能把数组内部的引用误认为游戏显示调用。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_table_verified",
  "reason": "四条只被gTextTable_Players静态数组引用，而该数组在完整US源码中没有消费者。不能把数组内部的引用误认为游戏显示调用。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "unused_parent": "gTextTable_Players",
  "row_number": 11089,
  "symbol": "gText_F703Players",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1653,
      "text": "const u8 gText_F703Players[] = _(\"{DYNAMIC 3}名玩家\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1659,
      "text": "gText_F703Players"
    }
  ],
  "unused_parent_occurrences": [
    {
      "file": "src/strings.c",
      "line": 1655,
      "text": "const u8 *const gTextTable_Players[] = {"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11094 行 · gText_ReadNewsThatArrived

判定：`unused_table_verified`

理由：两条仅位于美版sUnusedMenuTexts数组；全US源码中该数组没有调用。Wokann不存在对应活跃菜单项，此次不移植弃用表。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_table_verified",
  "reason": "两条仅位于美版sUnusedMenuTexts数组；全US源码中该数组没有调用。Wokann不存在对应活跃菜单项，此次不移植弃用表。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "unused_parent": "sUnusedMenuTexts",
  "row_number": 11094,
  "symbol": "gText_ReadNewsThatArrived",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/mystery_gift_menu.c",
      "line": 361,
      "text": "gText_ReadNewsThatArrived,"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1672,
      "text": "ALIGNED(4) const u8 gText_ReadNewsThatArrived[] = _(\"阅读最新的新闻。\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2782,
      "text": "extern const u8 gText_ReadNewsThatArrived[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2814,
      "text": "extern const u8 gText_ReadNewsThatArrived[];"
    }
  ],
  "unused_parent_occurrences": [
    {
      "file": "src/mystery_gift_menu.c",
      "line": 358,
      "text": "static const u8 *const sUnusedMenuTexts[] = {"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/mystery_gift_menu.c",
      "sha256": "a79f6f4ab3f47e8438d8fc1cc77d55ebe99f6eedd2ea333f7659900ae30fec05"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    }
  ]
}
```

### CSV 第 11095 行 · gText_ReturnToTitle

判定：`unused_table_verified`

理由：两条仅位于美版sUnusedMenuTexts数组；全US源码中该数组没有调用。Wokann不存在对应活跃菜单项，此次不移植弃用表。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_table_verified",
  "reason": "两条仅位于美版sUnusedMenuTexts数组；全US源码中该数组没有调用。Wokann不存在对应活跃菜单项，此次不移植弃用表。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "unused_parent": "sUnusedMenuTexts",
  "row_number": 11095,
  "symbol": "gText_ReturnToTitle",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/mystery_gift_menu.c",
      "line": 362,
      "text": "gText_ReturnToTitle"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1673,
      "text": "ALIGNED(4) const u8 gText_ReturnToTitle[] = _(\"返回标题画面。\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2783,
      "text": "extern const u8 gText_ReturnToTitle[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2815,
      "text": "extern const u8 gText_ReturnToTitle[];"
    }
  ],
  "unused_parent_occurrences": [
    {
      "file": "src/mystery_gift_menu.c",
      "line": 358,
      "text": "static const u8 *const sUnusedMenuTexts[] = {"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/mystery_gift_menu.c",
      "sha256": "a79f6f4ab3f47e8438d8fc1cc77d55ebe99f6eedd2ea333f7659900ae30fec05"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    }
  ]
}
```

### CSV 第 11096 行 · gText_CommunicationStandbyBButtonCancel

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11096,
  "symbol": "gText_CommunicationStandbyBButtonCancel",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1678,
      "text": "ALIGNED(4) const u8 gText_CommunicationStandbyBButtonCancel[] = _(\"正在等待连接……\\nB键：取消\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11099 行 · gText_PickOKCancel

判定：`regional_no_counterpart_verified`

理由：美版顶部菜单支持useCancel选择PickOKExit/PickOKCancel；日版PrintMysteryGiftOrEReaderTopMenu只在普通/读卡器两种模式下选择PickOKExit或DecideStop，不存在对应useCancel分支。原有JP选项已移植，不新增无调用的第三个模板。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "美版顶部菜单支持useCancel选择PickOKExit/PickOKCancel；日版PrintMysteryGiftOrEReaderTopMenu只在普通/读卡器两种模式下选择PickOKExit或DecideStop，不存在对应useCancel分支。原有JP选项已移植，不新增无调用的第三个模板。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11099,
  "symbol": "gText_PickOKCancel",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/mystery_gift_menu.c",
      "line": 494,
      "text": "options = !useCancel ? gText_PickOKExit : gText_PickOKCancel;"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1721,
      "text": "ALIGNED(4) const u8 gText_PickOKCancel[] = _(\"{DPAD_UPDOWN}选择 {A_BUTTON}确认 {B_BUTTON}取消\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2767,
      "text": "extern const u8 gText_PickOKCancel[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2799,
      "text": "extern const u8 gText_PickOKCancel[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/mystery_gift_menu.c",
      "sha256": "a79f6f4ab3f47e8438d8fc1cc77d55ebe99f6eedd2ea333f7659900ae30fec05"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/mystery_gift_menu.c",
      "sha256": "ad09c7c00c7e934354236894160e5e74cd2bdf59aa6a07e9708d4b0ff216264a"
    }
  ]
}
```

### CSV 第 11100 行 · gText_Exit4

判定：`unused_function_verified`

理由：唯一US调用在static UNUSED GetDaycareLevelMenuText，完整US源码只有该函数定义而没有调用。实际培育屋菜单使用独立gText_Exit，已经汉化；不覆盖未调用的旧模板。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_function_verified",
  "reason": "唯一US调用在static UNUSED GetDaycareLevelMenuText，完整US源码只有该函数定义而没有调用。实际培育屋菜单使用独立gText_Exit，已经汉化；不覆盖未调用的旧模板。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "unused_parent": "GetDaycareLevelMenuText",
  "row_number": 11100,
  "symbol": "gText_Exit4",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/daycare.c",
      "line": 1156,
      "text": "StringAppend(dest, gText_Exit4);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1736,
      "text": "const u8 gText_Exit4[] = _(\"退出\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2089,
      "text": "extern const u8 gText_Exit4[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2107,
      "text": "extern const u8 gText_Exit4[];"
    }
  ],
  "unused_parent_occurrences": [
    {
      "file": "src/daycare.c",
      "line": 1140,
      "text": "static void UNUSED GetDaycareLevelMenuText(struct DayCare *daycare, u8 *dest)"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/daycare.c",
      "sha256": "a26e00d7f80a46f9f45dd6500222393fa62feb81247ca6f0a66554d87ab9a690"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/daycare.c",
      "sha256": "597c1174ce15ef64f2b9b2fcb9680d75337e7018631d2d2f8ec9c7a698a8c3c5"
    }
  ]
}
```

### CSV 第 11101 行 · gText_MoveRelearnedPkmnDidNotLearnMove

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11101,
  "symbol": "gText_MoveRelearnedPkmnDidNotLearnMove",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1752,
      "text": "const u8 gText_MoveRelearnedPkmnDidNotLearnMove[] = _(\"{STR_VAR_1}没有学习{STR_VAR_2}。\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11102 行 · gText_NoWeather

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11102,
  "symbol": "gText_NoWeather",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1799,
      "text": "const u8 gText_NoWeather[] = _(\"天气正常\"); // Below are unused debug names for weather types"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11103 行 · gText_Sunny

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11103,
  "symbol": "gText_Sunny",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1800,
      "text": "const u8 gText_Sunny[] = _(\"晴天\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11104 行 · gText_Sunny2

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11104,
  "symbol": "gText_Sunny2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1801,
      "text": "const u8 gText_Sunny2[] = _(\"晴天2\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11105 行 · gText_Rain

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11105,
  "symbol": "gText_Rain",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1802,
      "text": "const u8 gText_Rain[] = _(\"下雨\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11106 行 · gText_Snow

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11106,
  "symbol": "gText_Snow",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1803,
      "text": "const u8 gText_Snow[] = _(\"下雪\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11107 行 · gText_Lightning

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11107,
  "symbol": "gText_Lightning",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1804,
      "text": "const u8 gText_Lightning[] = _(\"闪电\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11108 行 · gText_Fog

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11108,
  "symbol": "gText_Fog",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1805,
      "text": "const u8 gText_Fog[] = _(\"雾\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11109 行 · gText_VolcanoAsh

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11109,
  "symbol": "gText_VolcanoAsh",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1806,
      "text": "const u8 gText_VolcanoAsh[] = _(\"火山灰\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11110 行 · gText_Sandstorm

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11110,
  "symbol": "gText_Sandstorm",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1807,
      "text": "const u8 gText_Sandstorm[] = _(\"沙尘暴\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11111 行 · gText_Fog2

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11111,
  "symbol": "gText_Fog2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1808,
      "text": "const u8 gText_Fog2[] = _(\"雾2\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11112 行 · gText_Seafloor

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11112,
  "symbol": "gText_Seafloor",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1809,
      "text": "const u8 gText_Seafloor[] = _(\"海底\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11113 行 · gText_Cloudy

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11113,
  "symbol": "gText_Cloudy",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1810,
      "text": "const u8 gText_Cloudy[] = _(\"多云\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11114 行 · gText_Sunny3

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11114,
  "symbol": "gText_Sunny3",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1811,
      "text": "const u8 gText_Sunny3[] = _(\"晴天3\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11115 行 · gText_HeavyRain

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11115,
  "symbol": "gText_HeavyRain",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1812,
      "text": "const u8 gText_HeavyRain[] = _(\"大雨\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11116 行 · gText_Seafloor2

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11116,
  "symbol": "gText_Seafloor2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1813,
      "text": "const u8 gText_Seafloor2[] = _(\"海底2\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    }
  ]
}
```

### CSV 第 11117 行 · gText_DelAll

判定：`fixed_graphics_verified`

理由：日版不是不存在这些按钮，而是把文字烘焙在gEasyChatWindow_Gfx里。LoadEasyChatScreen加载图块和地图；AdjustBgTilemapForFooter在普通、测验、回答三种布局间复制两行。已替换对应矩形，保留原边框、调色板和光标坐标。文字取自当前美版strings.c。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_graphics_verified",
  "reason": "日版不是不存在这些按钮，而是把文字烘焙在gEasyChatWindow_Gfx里。LoadEasyChatScreen加载图块和地图；AdjustBgTilemapForFooter在普通、测验、回答三种布局间复制两行。已替换对应矩形，保留原边框、调色板和光标坐标。文字取自当前美版strings.c。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [
    {
      "payload_symbol": "ChsEasyChatFooterTiles",
      "file": "build/patch/easy_chat_footer_tiles.4bpp",
      "pointer_address": "0x0811C944",
      "compressed": true,
      "decompressed_sha256": "2e89f2d0f0bdd7c079a590f52475ae35f4832c5b12b230897c06c449fc23fe68"
    },
    {
      "payload_symbol": "ChsEasyChatFooterMap",
      "file": "build/patch/easy_chat_footer_map.bin",
      "pointer_address": "0x0811C948",
      "compressed": true,
      "decompressed_sha256": "6cf41cc518737289a2ec94f1e2993b965122e64fd9c24bc3bb189a640efe5f0f"
    }
  ],
  "row_number": 11117,
  "symbol": "gText_DelAll",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 1207,
      "text": "[FOOTER_NORMAL] = {gText_DelAll, gText_Cancel5, gText_Ok2, NULL},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 1208,
      "text": "[FOOTER_QUIZ]   = {gText_DelAll, gText_Cancel5, gText_Ok2, gText_Quiz},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 1209,
      "text": "[FOOTER_ANSWER] = {gText_DelAll, gText_Cancel5, gText_Ok2, gText_Answer},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1814,
      "text": "const u8 gText_DelAll[] = _(\"全部清除\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2657,
      "text": "extern const u8 gText_DelAll[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2675,
      "text": "extern const u8 gText_DelAll[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "sha256": "ee27e73604c0d93c0bfc7c956483cac219ad62221e2d10bcc0fb252570a2be26"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/easy_chat.c",
      "sha256": "f4a4a79ed1ed54d7b39f71eaa8301d3e11c5f4bb5a263589bf8bc76649e61cba"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/graphics.c",
      "sha256": "a21b78f3071a18542cfc3eea84bddd393bf575374a1ef1d8c784ed026a33a643"
    }
  ]
}
```

### CSV 第 11118 行 · gText_Cancel5

判定：`fixed_graphics_verified`

理由：日版不是不存在这些按钮，而是把文字烘焙在gEasyChatWindow_Gfx里。LoadEasyChatScreen加载图块和地图；AdjustBgTilemapForFooter在普通、测验、回答三种布局间复制两行。已替换对应矩形，保留原边框、调色板和光标坐标。文字取自当前美版strings.c。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_graphics_verified",
  "reason": "日版不是不存在这些按钮，而是把文字烘焙在gEasyChatWindow_Gfx里。LoadEasyChatScreen加载图块和地图；AdjustBgTilemapForFooter在普通、测验、回答三种布局间复制两行。已替换对应矩形，保留原边框、调色板和光标坐标。文字取自当前美版strings.c。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [
    {
      "payload_symbol": "ChsEasyChatFooterTiles",
      "file": "build/patch/easy_chat_footer_tiles.4bpp",
      "pointer_address": "0x0811C944",
      "compressed": true,
      "decompressed_sha256": "2e89f2d0f0bdd7c079a590f52475ae35f4832c5b12b230897c06c449fc23fe68"
    },
    {
      "payload_symbol": "ChsEasyChatFooterMap",
      "file": "build/patch/easy_chat_footer_map.bin",
      "pointer_address": "0x0811C948",
      "compressed": true,
      "decompressed_sha256": "6cf41cc518737289a2ec94f1e2993b965122e64fd9c24bc3bb189a640efe5f0f"
    }
  ],
  "row_number": 11118,
  "symbol": "gText_Cancel5",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 1207,
      "text": "[FOOTER_NORMAL] = {gText_DelAll, gText_Cancel5, gText_Ok2, NULL},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 1208,
      "text": "[FOOTER_QUIZ]   = {gText_DelAll, gText_Cancel5, gText_Ok2, gText_Quiz},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 1209,
      "text": "[FOOTER_ANSWER] = {gText_DelAll, gText_Cancel5, gText_Ok2, gText_Answer},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1815,
      "text": "const u8 gText_Cancel5[] = _(\"取消\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2658,
      "text": "extern const u8 gText_Cancel5[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2676,
      "text": "extern const u8 gText_Cancel5[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "sha256": "ee27e73604c0d93c0bfc7c956483cac219ad62221e2d10bcc0fb252570a2be26"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/easy_chat.c",
      "sha256": "f4a4a79ed1ed54d7b39f71eaa8301d3e11c5f4bb5a263589bf8bc76649e61cba"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/graphics.c",
      "sha256": "a21b78f3071a18542cfc3eea84bddd393bf575374a1ef1d8c784ed026a33a643"
    }
  ]
}
```

### CSV 第 11119 行 · gText_Ok2

判定：`fixed_graphics_verified`

理由：日版不是不存在这些按钮，而是把文字烘焙在gEasyChatWindow_Gfx里。LoadEasyChatScreen加载图块和地图；AdjustBgTilemapForFooter在普通、测验、回答三种布局间复制两行。已替换对应矩形，保留原边框、调色板和光标坐标。文字取自当前美版strings.c。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_graphics_verified",
  "reason": "日版不是不存在这些按钮，而是把文字烘焙在gEasyChatWindow_Gfx里。LoadEasyChatScreen加载图块和地图；AdjustBgTilemapForFooter在普通、测验、回答三种布局间复制两行。已替换对应矩形，保留原边框、调色板和光标坐标。文字取自当前美版strings.c。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [
    {
      "payload_symbol": "ChsEasyChatFooterTiles",
      "file": "build/patch/easy_chat_footer_tiles.4bpp",
      "pointer_address": "0x0811C944",
      "compressed": true,
      "decompressed_sha256": "2e89f2d0f0bdd7c079a590f52475ae35f4832c5b12b230897c06c449fc23fe68"
    },
    {
      "payload_symbol": "ChsEasyChatFooterMap",
      "file": "build/patch/easy_chat_footer_map.bin",
      "pointer_address": "0x0811C948",
      "compressed": true,
      "decompressed_sha256": "6cf41cc518737289a2ec94f1e2993b965122e64fd9c24bc3bb189a640efe5f0f"
    }
  ],
  "row_number": 11119,
  "symbol": "gText_Ok2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 1207,
      "text": "[FOOTER_NORMAL] = {gText_DelAll, gText_Cancel5, gText_Ok2, NULL},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 1208,
      "text": "[FOOTER_QUIZ]   = {gText_DelAll, gText_Cancel5, gText_Ok2, gText_Quiz},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 1209,
      "text": "[FOOTER_ANSWER] = {gText_DelAll, gText_Cancel5, gText_Ok2, gText_Answer},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1816,
      "text": "const u8 gText_Ok2[] = _(\"好了\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2659,
      "text": "extern const u8 gText_Ok2[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2677,
      "text": "extern const u8 gText_Ok2[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "sha256": "ee27e73604c0d93c0bfc7c956483cac219ad62221e2d10bcc0fb252570a2be26"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/easy_chat.c",
      "sha256": "f4a4a79ed1ed54d7b39f71eaa8301d3e11c5f4bb5a263589bf8bc76649e61cba"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/graphics.c",
      "sha256": "a21b78f3071a18542cfc3eea84bddd393bf575374a1ef1d8c784ed026a33a643"
    }
  ]
}
```

### CSV 第 11120 行 · gText_Quiz

判定：`fixed_graphics_verified`

理由：日版不是不存在这些按钮，而是把文字烘焙在gEasyChatWindow_Gfx里。LoadEasyChatScreen加载图块和地图；AdjustBgTilemapForFooter在普通、测验、回答三种布局间复制两行。已替换对应矩形，保留原边框、调色板和光标坐标。文字取自当前美版strings.c。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_graphics_verified",
  "reason": "日版不是不存在这些按钮，而是把文字烘焙在gEasyChatWindow_Gfx里。LoadEasyChatScreen加载图块和地图；AdjustBgTilemapForFooter在普通、测验、回答三种布局间复制两行。已替换对应矩形，保留原边框、调色板和光标坐标。文字取自当前美版strings.c。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [
    {
      "payload_symbol": "ChsEasyChatFooterTiles",
      "file": "build/patch/easy_chat_footer_tiles.4bpp",
      "pointer_address": "0x0811C944",
      "compressed": true,
      "decompressed_sha256": "2e89f2d0f0bdd7c079a590f52475ae35f4832c5b12b230897c06c449fc23fe68"
    },
    {
      "payload_symbol": "ChsEasyChatFooterMap",
      "file": "build/patch/easy_chat_footer_map.bin",
      "pointer_address": "0x0811C948",
      "compressed": true,
      "decompressed_sha256": "6cf41cc518737289a2ec94f1e2993b965122e64fd9c24bc3bb189a640efe5f0f"
    }
  ],
  "row_number": 11120,
  "symbol": "gText_Quiz",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 1208,
      "text": "[FOOTER_QUIZ]   = {gText_DelAll, gText_Cancel5, gText_Ok2, gText_Quiz},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1817,
      "text": "const u8 gText_Quiz[] = _(\"测验\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2660,
      "text": "extern const u8 gText_Quiz[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2678,
      "text": "extern const u8 gText_Quiz[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "sha256": "ee27e73604c0d93c0bfc7c956483cac219ad62221e2d10bcc0fb252570a2be26"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/easy_chat.c",
      "sha256": "f4a4a79ed1ed54d7b39f71eaa8301d3e11c5f4bb5a263589bf8bc76649e61cba"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/graphics.c",
      "sha256": "a21b78f3071a18542cfc3eea84bddd393bf575374a1ef1d8c784ed026a33a643"
    }
  ]
}
```

### CSV 第 11121 行 · gText_Answer

判定：`fixed_graphics_verified`

理由：日版不是不存在这些按钮，而是把文字烘焙在gEasyChatWindow_Gfx里。LoadEasyChatScreen加载图块和地图；AdjustBgTilemapForFooter在普通、测验、回答三种布局间复制两行。已替换对应矩形，保留原边框、调色板和光标坐标。文字取自当前美版strings.c。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_graphics_verified",
  "reason": "日版不是不存在这些按钮，而是把文字烘焙在gEasyChatWindow_Gfx里。LoadEasyChatScreen加载图块和地图；AdjustBgTilemapForFooter在普通、测验、回答三种布局间复制两行。已替换对应矩形，保留原边框、调色板和光标坐标。文字取自当前美版strings.c。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [
    {
      "payload_symbol": "ChsEasyChatFooterTiles",
      "file": "build/patch/easy_chat_footer_tiles.4bpp",
      "pointer_address": "0x0811C944",
      "compressed": true,
      "decompressed_sha256": "2e89f2d0f0bdd7c079a590f52475ae35f4832c5b12b230897c06c449fc23fe68"
    },
    {
      "payload_symbol": "ChsEasyChatFooterMap",
      "file": "build/patch/easy_chat_footer_map.bin",
      "pointer_address": "0x0811C948",
      "compressed": true,
      "decompressed_sha256": "6cf41cc518737289a2ec94f1e2993b965122e64fd9c24bc3bb189a640efe5f0f"
    }
  ],
  "row_number": 11121,
  "symbol": "gText_Answer",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 1209,
      "text": "[FOOTER_ANSWER] = {gText_DelAll, gText_Cancel5, gText_Ok2, gText_Answer},"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1818,
      "text": "const u8 gText_Answer[] = _(\"回答\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2661,
      "text": "extern const u8 gText_Answer[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 2679,
      "text": "extern const u8 gText_Answer[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "sha256": "ee27e73604c0d93c0bfc7c956483cac219ad62221e2d10bcc0fb252570a2be26"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/easy_chat.c",
      "sha256": "f4a4a79ed1ed54d7b39f71eaa8301d3e11c5f4bb5a263589bf8bc76649e61cba"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/graphics.c",
      "sha256": "a21b78f3071a18542cfc3eea84bddd393bf575374a1ef1d8c784ed026a33a643"
    }
  ]
}
```

### CSV 第 11122 行 · gText_PokeBalls

判定：`regional_no_counterpart_verified`

理由：美版CopyItemNameHandlePlural处理英语BALLS/BERRY/BERRIES复数；日版CopyItemName直接读取道具名，仅谜之果附加のみ，没有英语单复数选择。显示道具名已有汉化，这些复数字符串无独立JP入口。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "美版CopyItemNameHandlePlural处理英语BALLS/BERRY/BERRIES复数；日版CopyItemName直接读取道具名，仅谜之果附加のみ，没有英语单复数选择。显示道具名已有汉化，这些复数字符串无独立JP入口。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11122,
  "symbol": "gText_PokeBalls",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1819,
      "text": "const u8 gText_PokeBalls[] = _(\"精灵球\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/item.c",
      "line": 91,
      "text": "StringCopy(dst, gText_PokeBalls);"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 140,
      "text": "extern const u8 gText_PokeBalls[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 140,
      "text": "extern const u8 gText_PokeBalls[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/item.c",
      "sha256": "6ea3cac9a82b48021d05b9bd0116964ddf912fd0fc19b0ae6b471ec589faf3cd"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/item.c",
      "sha256": "a452b84834b1b6ec955a38074fcaf4550bc8be1aeffd2ba31227d640a00259e7"
    }
  ]
}
```

### CSV 第 11123 行 · gText_Berry

判定：`regional_no_counterpart_verified`

理由：美版CopyItemNameHandlePlural处理英语BALLS/BERRY/BERRIES复数；日版CopyItemName直接读取道具名，仅谜之果附加のみ，没有英语单复数选择。显示道具名已有汉化，这些复数字符串无独立JP入口。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "美版CopyItemNameHandlePlural处理英语BALLS/BERRY/BERRIES复数；日版CopyItemName直接读取道具名，仅谜之果附加のみ，没有英语单复数选择。显示道具名已有汉化，这些复数字符串无独立JP入口。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11123,
  "symbol": "gText_Berry",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1820,
      "text": "const u8 gText_Berry[] = _(\"树果\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/item.c",
      "line": 108,
      "text": "berryString = gText_Berry;"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 142,
      "text": "extern const u8 gText_Berry[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 142,
      "text": "extern const u8 gText_Berry[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/item.c",
      "sha256": "6ea3cac9a82b48021d05b9bd0116964ddf912fd0fc19b0ae6b471ec589faf3cd"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/item.c",
      "sha256": "a452b84834b1b6ec955a38074fcaf4550bc8be1aeffd2ba31227d640a00259e7"
    }
  ]
}
```

### CSV 第 11124 行 · gText_Berries

判定：`regional_no_counterpart_verified`

理由：美版CopyItemNameHandlePlural处理英语BALLS/BERRY/BERRIES复数；日版CopyItemName直接读取道具名，仅谜之果附加のみ，没有英语单复数选择。显示道具名已有汉化，这些复数字符串无独立JP入口。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "美版CopyItemNameHandlePlural处理英语BALLS/BERRY/BERRIES复数；日版CopyItemName直接读取道具名，仅谜之果附加のみ，没有英语单复数选择。显示道具名已有汉化，这些复数字符串无独立JP入口。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11124,
  "symbol": "gText_Berries",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "line": 1821,
      "text": "const u8 gText_Berries[] = _(\"树果\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/item.c",
      "line": 110,
      "text": "berryString = gText_Berries;"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 141,
      "text": "extern const u8 gText_Berries[];"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "line": 141,
      "text": "extern const u8 gText_Berries[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/item.c",
      "sha256": "6ea3cac9a82b48021d05b9bd0116964ddf912fd0fc19b0ae6b471ec589faf3cd"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/strings.c",
      "sha256": "635e8ad35869b9ff728d01aef932d80fd76623224f204fcafc5c7076d7b749c2"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "include/strings.h",
      "sha256": "1a9e10add3505af7155c46cbb63a42a0dceff8796891f2b88029a8e1abd44e0b"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/item.c",
      "sha256": "a452b84834b1b6ec955a38074fcaf4550bc8be1aeffd2ba31227d640a00259e7"
    }
  ]
}
```

### CSV 第 11125 行 · gText_EasyChatKeyboard_ABCDEFothers

判定：`regional_no_counterpart_verified`

理由：美版简易聊天按英文字母分组，日版sEasyChatKeyboardAlphabet按假名分组。不能把美版ABCDEF拉丁行直接覆盖日版假名键盘；此项不属于相同资源的漏翻。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "regional_no_counterpart_verified",
  "reason": "美版简易聊天按英文字母分组，日版sEasyChatKeyboardAlphabet按假名分组。不能把美版ABCDEF拉丁行直接覆盖日版假名键盘；此项不属于相同资源的漏翻。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11125,
  "symbol": "gText_EasyChatKeyboard_ABCDEFothers",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "line": 873,
      "text": "gText_EasyChatKeyboard_ABCDEFothers,"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/text_input_strings.c",
      "line": 4,
      "text": "const u8 gText_EasyChatKeyboard_ABCDEFothers[] = _(\"{CLEAR 11}A{CLEAR 6}B{CLEAR 6}C{CLEAR 26}D{CLEAR 6}E{CLEAR 6}F{CLEAR 26}其他\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "line": 2686,
      "text": "extern const u8 gText_EasyChatKeyboard_ABCDEFothers[];"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "include/strings.h",
      "sha256": "fd60ee0d6784ffbc868a198548a2be5d535dc0ea8ef0a45f036236169f016888"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/easy_chat.c",
      "sha256": "ee27e73604c0d93c0bfc7c956483cac219ad62221e2d10bcc0fb252570a2be26"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/text_input_strings.c",
      "sha256": "2f228192abdd6c520e7f91e427a57128caecdf039e15f039d550ebe17f7c9ac3"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/easy_chat.c",
      "sha256": "f4a4a79ed1ed54d7b39f71eaa8301d3e11c5f4bb5a263589bf8bc76649e61cba"
    }
  ]
}
```

### CSV 第 11693 行 · sText_SpaceMove

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11693,
  "symbol": "sText_SpaceMove",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/trade.h",
      "line": 36,
      "text": "static const u8 sText_SpaceMove[] = _(\"移动\"); // unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/trade.h",
      "sha256": "db456217e6d7b57119fae7cc3098dbfa81446d27007a7acf91c782cf1010d7fe"
    }
  ]
}
```

### CSV 第 11697 行 · sText_PleaseWaitAWhile

判定：`fixed_consumer_verified`

理由：union_room5.h sCommunicatingWaitTexts[2]; union_room.c UR_PrintFieldMessage uses index2 and metBefore. Distinguish from unused identically named berry_blender.c definition.

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "fixed_consumer_verified",
  "reason": "union_room5.h sCommunicatingWaitTexts[2]; union_room.c UR_PrintFieldMessage uses index2 and metBefore. Distinguish from unused identically named berry_blender.c definition.",
  "aliases_payloads": [
    "Chs_V2_sText_PleaseWaitAWhile"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "implementation": {
    "symbol": "sText_PleaseWaitAWhile",
    "payload_symbol": "Chs_V2_sText_PleaseWaitAWhile",
    "final_text": "请稍等……{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.\n{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.",
    "us_source": {
      "file": "src/data/union_room.h",
      "text": "请稍等……{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.\n{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}."
    },
    "reason": "union_room5.h sCommunicatingWaitTexts[2]; union_room.c UR_PrintFieldMessage uses index2 and metBefore. Distinguish from unused identically named berry_blender.c definition.",
    "original_address": "0x082C0C68",
    "original_hex": "0c36030c3603051f1108410b02fc080faffc080faffc080faffc080faffc080faffc080faffefc080faffc080faffc080faffc080faffc080faffc080faffc080faffc080faffc080faffc080faffc080faffc080faffc080faffc080faffc080faffc080faffc080faffc080fafff",
    "wokann_references": [
      {
        "address": "0x082C0CE0",
        "original": "0x082C0C68",
        "object": "build/pokeemerald-jp/src/data/union_room5.o",
        "object_sha256": "25c9ce9d64804ea82c23d98e78671d28305faaf455e6690cced3bace73141df3",
        "section": ".rodata",
        "section_base": "0x082C0B44",
        "section_length": 416,
        "relocation": "R_ARM_ABS32",
        "referenced_symbol": "sText_PleaseWaitAWhile",
        "section_offset": 412
      }
    ]
  },
  "row_number": 11697,
  "symbol": "sText_PleaseWaitAWhile",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_blender.c",
      "line": 286,
      "text": "static const u8 sText_PleaseWaitAWhile[] = _(\"Please wait a while.\");"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "line": 167,
      "text": "ALIGNED(4) static const u8 sText_PleaseWaitAWhile[] = _(\"请稍等……{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.{PAUSE 15}.\\n\""
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "line": 173,
      "text": "sText_PleaseWaitAWhile"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/union_room5.h",
      "line": 29,
      "text": "ALIGNED(4) const u8 sText_PleaseWaitAWhile[] = _("
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/union_room5.h",
      "line": 36,
      "text": "sText_PleaseWaitAWhile,"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/berry_blender.c",
      "sha256": "26c5b6c5d917bed28f71c0f48f0cb62451eb0a840b690aca2fbba705daa5b7bd"
    },
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "sha256": "0dfc0c87d72418d6472d2d0358117023333b9610850c94755e38e924e3fdbb4f"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/union_room5.h",
      "sha256": "1301b930f6f881ff4f8616493781d5ca25c9d89455c97fba6bcf692977860663"
    }
  ]
}
```

### CSV 第 11699 行 · sText_WaitForChatMale2

判定：`already_ported_alias_verified`

理由：美版Unused第二份定义没有调用，日版活跃sText_WaitForChatMale在0x082C10A8已重定向；不能把两个定义混为一个遗漏。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_alias_verified",
  "reason": "美版Unused第二份定义没有调用，日版活跃sText_WaitForChatMale在0x082C10A8已重定向；不能把两个定义混为一个遗漏。",
  "aliases_payloads": [
    "Chs_sText_WaitForChatMale"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11699,
  "symbol": "sText_WaitForChatMale2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "line": 278,
      "text": "ALIGNED(4) static const u8 sText_WaitForChatMale2[] = _(\"想聊天，嗯？\\n好，等下。\"); // Unused"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/union_room8b.h",
      "line": 4,
      "text": "ALIGNED(4) const u8 sText_WaitForChatMale2[] = _("
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "sha256": "0dfc0c87d72418d6472d2d0358117023333b9610850c94755e38e924e3fdbb4f"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "src/data/union_room8b.h",
      "sha256": "e51bcb7e1342c35dddf33f51eff66756d754010f2a5c92d99b5bf15423a88fe4"
    }
  ]
}
```

### CSV 第 11700 行 · sText_ThankYouForRegistering

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11700,
  "symbol": "sText_ThankYouForRegistering",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "line": 440,
      "text": "ALIGNED(4) static const u8 sText_ThankYouForRegistering[] = _(\"我们已经登记了您的宝可梦\\n放在交换公告板用来交换。\\p感谢使用这项服务！\\p\"); // unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "sha256": "0dfc0c87d72418d6472d2d0358117023333b9610850c94755e38e924e3fdbb4f"
    }
  ]
}
```

### CSV 第 11701 行 · sText_NobodyHasRegistered

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11701,
  "symbol": "sText_NobodyHasRegistered",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "line": 441,
      "text": "ALIGNED(4) static const u8 sText_NobodyHasRegistered[] = _(\"没人登记宝可梦\\n在交换公告板用来交换。\\p\"); // unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "sha256": "0dfc0c87d72418d6472d2d0358117023333b9610850c94755e38e924e3fdbb4f"
    }
  ]
}
```

### CSV 第 11702 行 · sText_TradeTrainersWillBeListed

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11702,
  "symbol": "sText_TradeTrainersWillBeListed",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "line": 450,
      "text": "ALIGNED(4) static const u8 sText_TradeTrainersWillBeListed[] = _(\"训练家想要进行的交换\\n会用表格列出来。\"); // unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "sha256": "0dfc0c87d72418d6472d2d0358117023333b9610850c94755e38e924e3fdbb4f"
    }
  ]
}
```

### CSV 第 11703 行 · sText_ChooseTrainerToTradeWith2

判定：`already_ported_alias_verified`

理由：美版第二份未用定义；日版sChooseTrainerTexts[TRADE]在0x082C1BF0使用已移植的第一份文本。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_alias_verified",
  "reason": "美版第二份未用定义；日版sChooseTrainerTexts[TRADE]在0x082C1BF0使用已移植的第一份文本。",
  "aliases_payloads": [
    "Chs_sText_ChooseTrainerToTradeWith"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11703,
  "symbol": "sText_ChooseTrainerToTradeWith2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "line": 451,
      "text": "ALIGNED(4) static const u8 sText_ChooseTrainerToTradeWith2[] = _(\"请选择训练家\\n用来交换宝可梦。\"); // unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "sha256": "0dfc0c87d72418d6472d2d0358117023333b9610850c94755e38e924e3fdbb4f"
    }
  ]
}
```

### CSV 第 11704 行 · sText_AwaitingResponseFromTrainer2

判定：`already_ported_alias_verified`

理由：美版第二份未用定义；日版实际sText_AwaitingResponseFromTrainer在0x082C0DE4已汉化。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "already_ported_alias_verified",
  "reason": "美版第二份未用定义；日版实际sText_AwaitingResponseFromTrainer在0x082C0DE4已汉化。",
  "aliases_payloads": [
    "Chs_sText_AwaitingResponseFromTrainer"
  ],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11704,
  "symbol": "sText_AwaitingResponseFromTrainer2",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "line": 453,
      "text": "ALIGNED(4) static const u8 sText_AwaitingResponseFromTrainer2[] = _(\"等待训练家\\n的回复……\"); // unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "sha256": "0dfc0c87d72418d6472d2d0358117023333b9610850c94755e38e924e3fdbb4f"
    }
  ]
}
```

### CSV 第 11705 行 · sText_NotRegisteredAMonForTrade

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11705,
  "symbol": "sText_NotRegisteredAMonForTrade",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "line": 454,
      "text": "ALIGNED(4) static const u8 sText_NotRegisteredAMonForTrade[] = _(\"还没有登记宝可梦\\n用于交换。\\p\"); // unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "sha256": "0dfc0c87d72418d6472d2d0358117023333b9610850c94755e38e924e3fdbb4f"
    }
  ]
}
```

### CSV 第 11706 行 · sText_MustHaveTwoMonsForDoubleBattle

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11706,
  "symbol": "sText_MustHaveTwoMonsForDoubleBattle",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "line": 516,
      "text": "ALIGNED(4) static const u8 sText_MustHaveTwoMonsForDoubleBattle[] = _(\"要进行双打对战的话，\\n需要至少有2只宝可梦。\\p\"); // Unused"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "src/data/union_room.h",
      "sha256": "0dfc0c87d72418d6472d2d0358117023333b9610850c94755e38e924e3fdbb4f"
    }
  ]
}
```

### CSV 第 11920 行 · gText_UnusedNicknameReceivedPokemon

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11920,
  "symbol": "gText_UnusedNicknameReceivedPokemon",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/event_scripts.s",
      "line": 870,
      "text": "gText_UnusedNicknameReceivedPokemon::"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "data/event_scripts.s",
      "line": 891,
      "text": "gText_UnusedNicknameReceivedPokemon:: @ 0x08243B36"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/event_scripts.s",
      "sha256": "2e69b774359fa211d5f5a810d1a10a7f139d1e15fa09200ebc09a1c37935fe44"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "data/event_scripts.s",
      "sha256": "b8ebffa6fa5289b4573598f8dadd5dde579c295562a3971ae1ea2364ba8ab401"
    }
  ]
}
```

### CSV 第 11921 行 · gText_SorryRecordCornerPreparation

判定：`unused_definition_verified`

理由：逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。

具体实现 / 调用 / 源文件及对象哈希证据：

```json
{
  "decision": "unused_definition_verified",
  "reason": "逐个检索US/JP源码后只有定义或extern声明，没有消费者。US的Unused标注仅作补充，判定依据是实际引用而非名字。已有同文活跃别名另行核验，保留这份弃用定义，不给死文本添加覆盖。",
  "aliases_payloads": [],
  "pointer_expectations": [],
  "graphics": [],
  "row_number": 11921,
  "symbol": "gText_SorryRecordCornerPreparation",
  "source_occurrences": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/event_scripts.s",
      "line": 917,
      "text": "gText_SorryRecordCornerPreparation::"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "data/event_scripts.s",
      "line": 949,
      "text": "gText_SorryRecordCornerPreparation:: @ 0x08243D56"
    }
  ],
  "source_file_hashes": [
    {
      "region": "pokeemerald_us_chs",
      "file": "data/event_scripts.s",
      "sha256": "2e69b774359fa211d5f5a810d1a10a7f139d1e15fa09200ebc09a1c37935fe44"
    },
    {
      "region": "pokeemerald_wokann_dev",
      "file": "data/event_scripts.s",
      "sha256": "b8ebffa6fa5289b4573598f8dadd5dde579c295562a3971ae1ea2364ba8ab401"
    }
  ]
}
```
