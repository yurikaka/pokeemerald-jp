# 主角家床／电脑花屏：graphics 独立根因与最小修复

日期：2026-10-02。工作分支：`chs-port`。

## 状态与写入边界

- 已读取根目录 `AGENTS.md`，对照 Wokann `dev` 分支，完成离线原版／汉化／修复后验证。
- **已实际修复独立 ROM 副本**：`/tmp/pokeemerald_jp_chs_home_tiles_verified_20261002.gba`。
- 共享 `pokeemerald_jp_chs.gba`、batch、manifest、公共工具、ASM、tracker、计划均未修改；没有 build、commit 或 push。
- **永久源码修复已写入**：`181c0c7` 已从 `patch/batches/415_match_call_0.json` 删除该错误引用。当前构建 ROM `0x347307` 处字节与 baserom 一致（`40 2C 5F 08`），花屏已修复。
- `permanent_fix.pending.patch` 已不再需要（修复已通过 `181c0c7` 落地），文件已删除。

## 根因：压缩图块字节被误当作文本指针

`patch/batches/415_match_call_0.json:974` 的 `reference_writes` 包含：

```json
{
  "address": "0x08347307",
  "original": "0x085F2C40",
  "symbol": "Chs_gText_MatchCallSwimmer_Tony_Intro1",
  "source_symbol": "gText_MatchCallSwimmer_Tony_Intro1"
}
```

该地址不是真正的文本引用槽，而在 `gTileset_BrendansMaysHouse_Tiles` 的 LZ77 压缩流内部。
原始四字节恰好为 `40 2C 5F 08`，数值上与 Tony 的日文文本地址相同；这只是压缩数据碰撞，不能作为引用证据。
`patch/tools/apply_patch.py` 对 batch 的校验只验证原四字节数值，因此该错误引用能够通过校验，并被写成中文文本地址。

本次汉化 ROM 中的覆盖为：

| 内容 | 数值 |
| --- | --- |
| ROM 地址／文件偏移 | `0x08347307`／`0x347307` |
| 原始字节 | `40 2C 5F 08` |
| 被覆盖字节 | `17 02 08 09`，即 `0x09080217` |
| 真实、必须保留的 Tony 文本引用 | `0x085F3AAC`，也指向 `0x09080217` |
| 房屋压缩图块范围 | `[0x083464CC, 0x08347598)`，4,300 字节 |
| 原始／修复后解压长度 | 15,360 字节，480 个 4bpp 图块 |
| 损坏后的解压变化 | 1,019 字节，67 个图块 |
| 损坏后的输入消耗 | 4,302 字节，比资源边界多读 2 字节 |

这四字节横跨三个 LZ77 回溯令牌，而非一个独立的四字节指针：

| 令牌地址 | 原始令牌 | 损坏令牌 | 距离／长度变化 |
| --- | --- | --- | --- |
| `0x08347306` | `10 40` | `10 17` | `65/4 → 24/4` |
| `0x08347308` | `2C 5F` | `02 08` | `3168/5 → 521/3` |
| `0x0834730A` | `08 3D` | `09 3D` | `2110/3 → 2366/3` |

回溯距离和输出长度改变，导致后续图块像素错位；这解释了为什么不是只坏四个像素。
完整令牌、受影响图块 ID、房屋 metatile 坐标及哈希见 `verification.json`。
没有理由重绘床／电脑资产，也无需移动地图、tilemap 或修改布局。

## Wokann 源码与布局证据

对照仓库：`../pokeemerald_wokann_dev`，分支 `dev`，commit `88d22da09cc2d1154bfc76423aa8dbdd67b76bfa`。
其 `baserom_jp.gba` 与本仓库原版 ROM 完全一致，SHA-1 都是 `d7cf8f156ba9c455d164e1ea780a6bf1945465c2`。

以下均为 Wokann 仓库内路径：

- `data/tilesets/headers.inc:130`：`gTileset_Building` 位于 `0x083B7CA4`。
- `data/tilesets/headers.inc:338`：`gTileset_BrendansMaysHouse` 位于 `0x083B7F14`，结构内依次为 tiles、palettes、metatiles、attributes、callback；不是推测附近数据用途。
- `data/tilesets/graphics.inc:773`：房屋 tiles 的 `.incbin` 指向 `data/tilesets/secondary/brendans_mays_house/tiles.4bpp.lz`。
- 该文件 4,300 字节与原 ROM `0x083464CC` 起的数据逐字节一致；下一个 palettes 指针为 `0x08347598`，印证资源边界。
- `data/tilesets/metatiles.inc:145`：房屋 metatiles／attributes 分别来自同目录的两个二进制文件，对应 `0x08397016`／`0x08397C56`。
- `data/layouts/layouts.inc:822` 与 `data/layouts/layouts.json`：二楼为 9×8，使用 Building 主 tileset 和 BrendansMaysHouse 次 tileset；工具另外验证两栋房屋的一楼。
- `include/fieldmap.h:4`：主 tileset 图块和 metatile 基数均为 512，主调色板 6 组，总共 13 组。
- `src/field_camera.c:238`、`include/global.fieldmap.h:49`：metatile 的两层图块、翻转、调色板和 NORMAL 层背景的解码依据；`src/fieldmap.c:830` 为调色板加载依据。
- `src/data/text/match_call_messages.h:83` 定义 Tony 的 Intro1；`:396` 定义 `gMatchCallFlavorTexts`，`:413` 使用 `MCFLAVOR(Swimmer_Tony)`。
- `include/constants/rematches.h:20` 中 Tony 为索引 15；`include/pokenav.h:220` 中 Intro1 为四列中的索引 2。对应表基址 `0x085F39B4` 加 `15 * 16 + 2 * 4`，得到真实槽 `0x085F3AAC`。本仓库 `data/data.s:15762` 的原 ROM 表块起址也一致。

原版与汉化的两份 tileset header、全部主图块、两份 metatiles／attributes、全部两份调色板，以及四间房的地图／边界／layout header 都一致。
唯一房屋压缩流变化就是上述四字节。恢复后整段压缩文件及全部解压字节均与 Wokann／原版一致。

## 截图与离线渲染

已查看用户提供的 `chuang.png`，没有使用 AI 重绘。

- `LittlerootTown_BrendansHouse_2F.png`：左为原版，中为当前汉化 ROM，右为四字节修复后。
- `LittlerootTown_MaysHouse_2F.png`：同样验证女主／另一栋二楼的镜像布局。
- 离线渲染复现了床的条纹错位和电脑桌／椅区域花屏；恢复后两栋房屋四间房的静态背景像素均与原版一致。
- 两栋一楼均没有使用受损图块；两栋二楼各有 8 个受影响 metatile，详见 JSON。
- 将截图房间原点设为 `(64, 24)`，按 RGB 5-bit 归一化比较：床区域为 **1,536/1,536** 像素吻合损坏渲染；电脑区域为 **1,526/1,536**。原版对应为 1,103 和 1,408。
- 电脑区域仍有 10 像素不同，未声称整个截图完全重放。截图所用 ROM 的确切版本／运行状态未确认。
- **没有模拟器验证**。上述均为原始字节、LZ77、静态地图解码和提供截图的比较，不含角色精灵、运行时动画或存档回放。

## 最小修复与验证

1. 实际修复：仅将独立 ROM 副本的文件偏移 `0x347307..0x34730A` 恢复为 `40 2C 5F 08`。
2. `home_tiles_only.ips` 是 17 字节、单一四字节记录的 IPS；独立重放后与修复副本逐字节相同。
3. 全 32 MiB 对比确认只改变四字节；真实 Tony 引用、中文 payload 和其余所有内容保持不变。
4. 两套 tileset、四间房原版／汉化／修复后验证通过；修复后房屋压缩数据、解压数据和背景像素均与原版一致。
5. `python3 -m py_compile patch/tools/verify_home_tiles_graphics.py` 通过。
6. `git apply --check patch/graphics_reports/home_tiles/permanent_fix.pending.patch` 通过；仅检查，未应用。
7. 三项拒绝写入测试通过：覆盖共享输入 ROM、覆盖已有修复文件、再次将已修复 ROM 当作受损输入。

SHA-1：

```text
原版      d7cf8f156ba9c455d164e1ea780a6bf1945465c2
汉化输入  b4efab8c56da349cad339fc314f6a77cf5a9a007
修复副本  42fd0fff88aa773e41d899636ca5e0391a3d7960
```

复现（请选一个不存在的副本路径，工具拒绝覆盖已有 ROM）：

```sh
python3 patch/tools/verify_home_tiles_graphics.py \
  --output-dir /tmp/home_tiles_recheck \
  --repair-rom /tmp/home_tiles_recheck.gba
```

工具仅针对本次已证明的 Tony 指针碰撞，检查资源与原字节后才生成副本；不是通用 ROM 修复器。
IPS 本身不带输入哈希校验，应用前必须确认对应原始字节与版本；优先使用带校验的工具。

## 永久源码修复的协调请求

**只需授权或由主代理执行以下共享文件变更：**

- 文件：`patch/batches/415_match_call_0.json`。
- 删除 `address == 0x08347307` 的一个 `reference_writes` 对象（六行）。
- 保留 `0x085F3AAC` 的真实引用、Tony 的中文文本对象、其他所有未提交文本更改。
- 不需要修改 manifest、公共 build、ASM 或任何 graphics 原始资产。
- 提议补丁：`permanent_fix.pending.patch`。它不自动更新历史 mapping/audit 报告；当前 graphics 报告明确纠正其中的错误引用认定。
- 不建议仅重新生成映射来猜测解决：现有 `port_c_strings.py` 虽已有对齐过滤，但历史 batch 中该错误对象仍然存在。对齐也不能替代源码资源归属验证。

## 本任务新增文件

```text
patch/tools/verify_home_tiles_graphics.py
patch/graphics_reports/home_tiles/README.md
patch/graphics_reports/home_tiles/verification.json
patch/graphics_reports/home_tiles/LittlerootTown_BrendansHouse_2F.png
patch/graphics_reports/home_tiles/LittlerootTown_MaysHouse_2F.png
patch/graphics_reports/home_tiles/home_tiles_only.ips
patch/graphics_reports/home_tiles/permanent_fix.pending.patch
```

额外产物仅位于 `/tmp`：已验证修复 ROM，以及前一轮等价的 `pokeemerald_jp_chs_home_tiles_fixed_20261002.gba` 副本。
