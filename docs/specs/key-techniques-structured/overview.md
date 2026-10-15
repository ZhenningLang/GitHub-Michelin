Audience:   P3 实现 agent
Scope:      技术要点改成「机制图 + 每招四行」的结构化写法，lint 硬查，21 对 v2 页全部改写 / Non-scope: 843 对 v1 页、快速上手流程卡、CI 安装 d2
State:      approved
Genre:      G-SPEC
Code-Root:  /Users/zhenninglang/Projects/oss-atlas-wt-techniques
Prefixes:   U-DEC, U-BEH, U-GATE, U-SPK, U-ACC, U-NG, U-DEP, U-CTR, U-DIAG

# key-techniques-structured · G-SPEC 机器版 spec

Planned at: c0f548ab · 2026-10-15

开发路线：/dev-long-run（owner 2026-10-15 选定），分三段，serial：第一段做完停下给 owner 看样板，批准后才开第二段。

## 术语表

- U-DEC: 待决策
- U-BEH: 有意行为变化
- U-GATE: 不可逆动作
- U-SPK: 翻车假设与 spike
- U-ACC: 验收承诺
- U-NG: non-goals
- U-DEP: 新增依赖
- U-CTR: 既有契约与回归红线
- U-DIAG: 根因与现状诊断
- 结构化页：`last_verified` 不早于 `TECHNIQUES_STRUCTURED_FROM`（默认 2026-10-15）的 v2 页，技术要点必须按本 spec 的形状写。
- 机制图：技术要点开头的一张图，画项目内部数据怎么流、每一招落在哪一步；源是 `mechanisms/<stem>.json`，由 `tools/mechanism_card.py` 经本机 d2 渲成 `assets/mechanism/<stem>.svg` 与 `<stem>.zh.svg`。
- 招：技术要点里的一个 `###` 小节，讲一个实现手法，下面固定四行。
- stem：与 `flows/` 相同的命名规则（重复 slug 加类目前缀），复用 `flow_card.flow_stem`。

## TL;DR

技术要点从一段散文改成固定形状：开头一张 d2 机制图（加生成的文字版），之后 2–6 个 `### n. 标题`，每个下面四行「解决 / 做法 / 边界 / 源码」。lint 对 `last_verified >= 2026-10-15` 的页面硬查形状、图与源是否同步；CI 不装 d2，靠图里盖的源文件哈希判断图是否过期。现有 21 对 v2 页全部按新形状改写。

## 根因与现状

[U-DIAG-1|e749] 现有技术要点是成段散文，没有图。21 对 v2 页的中文技术要点去掉链接目标后 300–662 字（中位数 471 字），一共夹了 101 个源码链接，0 张图（2026-10-15 实测）。读者无法逐招扫读：screenshot-to-code 四招挤在一段里，backtrader 每条 bullet 夹 4–6 个链接。owner 原话：「技术要点过于简陋了，我需要结构化的表达和流程图辅助」。

[U-DIAG-2|d90a] 现行契约（tools/schema.md:365-376）只要求「写几招、每招做什么、为什么重要、局限、源码位置」，没有规定形状；lint 只查技术要点存在、非空、中英一致（tools/lint.py:875-952）。所以同一批页面写出了段落、bullet、带前言的 bullet 三种形状。

## 已锁定（owner 2026-10-15，AskUserQuestion）

- 形状：开头一张总图，之后每招一个 `###` 小标题，下面固定四行：解决 / 做法 / 边界 / 源码（英文 Problem / How / Limits / Source）。
- 图：d2 生成 SVG 存 `assets/`，不用页内 Mermaid。
- 约束：写进 tools/schema.md，lint 硬查；改写 21 对（screenshot-to-code + docs/specs/section-contract-v2/sample-pages.md 的 20 对）。
- 路线：/dev-long-run。

## 有意行为变化

[U-BEH-1|a9e0] 新增门槛常量 `TECHNIQUES_STRUCTURED_FROM = os.environ.get("OSS_ATLAS_TECHNIQUES_STRUCTURED_FROM", "2026-10-15")`，判定函数 `techniques_structured(last_verified)` 照抄 `sections_v2()` 的解析与容错。只有 v2 且日期达到门槛的页面走结构化检查；`2026-10-13`/`2026-10-14` 的 v2 页继续接受散文。实测全库达到 `2026-10-13` 的恰好是这 21 对，本 run 全部改写并更新日期，所以收尾时不留散文 v2 页。

[U-BEH-2|c974] 结构化页的技术要点形状（中文页；英文页同形，标签换成英文）：

```markdown
## 技术要点

![<name> — 机制图](../../assets/mechanism/<stem>.zh.svg)

<!-- mechanism:begin (generated from mechanisms/<stem>.json by tools/mechanism_card.py; do not edit) -->
…生成的文字版…
<!-- mechanism:end -->

### 1. <这一招一句话>

- **解决：** <没有这招会出什么问题>
- **做法：** <它具体怎么做，可带一个类比>
- **边界：** <这招管不到什么、什么时候失效>
- **源码：** [`<文件>:<起>–<止>`](https://github.com/<o>/<r>/blob/<sha>/<文件>#L<起>-L<止>)

### 2. …
```

英文标签依次是 `- **Problem:**`、`- **How:**`、`- **Limits:**`、`- **Source:**`；英文图注是 `— mechanism diagram`。规则：图片行与生成区块必须在第一个 `###` 之前；`###` 标题必须形如 `### <n>. <标题>`，n 从 1 连续递增；每个招下恰好四个标签项、顺序固定、值非空；标签项后可有缩进续行；招内不得出现四个标签项以外的顶格内容。

[U-BEH-3|9c11] lint 对结构化页报 ERROR 的情形：缺图片行或图片文件不存在；缺生成区块或区块内容与 `mechanism_card.text_block()` 的输出不一致；SVG 里盖的源哈希与当前 `mechanisms/<stem>.json` 的规范化哈希不一致（提示运行 `python3 tools/mechanism_card.py <page>`）；招少于 2 个；编号不连续；缺标签、标签乱序、标签值为空；「源码」行不含任何 Markdown 链接；中英两页招数不同。招多于 6 个报 WARNING。技术要点含 `<!-- oss-atlas:unresearched -->` 标记时跳过以上结构检查（标记本身已报 ERROR，见 U-CTR-3）。

[U-BEH-4|62e5] 机制图源 `mechanisms/<stem>.json` 的形状（按 U-DEC-1 的推荐写）：

```json
{
  "schema": 1,
  "direction": "right",
  "nodes": [
    {"id": "shot", "en": "Your screenshot", "zh": "你的截图", "kind": "input"},
    {"id": "crop", "en": "Crop assets by Gemini boxes", "zh": "按 Gemini 定位框裁原图", "technique": [2]},
    {"id": "gen",  "en": "create_file writes the page", "zh": "create_file 写整页", "technique": [1]}
  ],
  "edges": [
    {"from": "shot", "to": "crop"},
    {"from": "crop", "to": "gen", "en": "real images", "zh": "真实图片"}
  ],
  "sources": ["https://github.com/abi/screenshot-to-code/blob/a813977/backend/agent/tools.py"]
}
```

校验：3–12 个节点；id 唯一；边的两端存在；`kind` ∈ `input | step | output | external`（缺省 `step`）；`direction` ∈ `right | down`；`technique` 里的编号必须落在页面招的编号范围内，且每个招至少挂一个节点（lint 读页面算招数后交叉校验）；边可带 `"style": "dashed"` 表示兜底或可选路径。节点标签渲染时自动加招编号角标（①②…），让图和下面的小标题对得上。

[U-BEH-5|f2a6] 新生成器 `tools/mechanism_card.py`，用法与 flow_card 对齐：`python3 tools/mechanism_card.py <page>…` 渲染并回写两页，`--all` 处理所有有机制图源的页面，`--check-spec <json>` 只校验不写文件。渲染：JSON → 每种语言一份 d2 源（纯 Python 拼字符串）→ `d2 --layout elk`（本机二进制，经 subprocess）→ SVG，在 SVG 开头插入 `<!-- mechanism-src sha256=<hex> -->`；哈希算在 `json.dumps(spec, sort_keys=True, ensure_ascii=False)` 加生成器常量 `RENDER_VERSION` 上。本机找不到 d2 时退出码 2 并提示 `brew install d2`，不写半成品。文字版由纯 Python 生成（节点按 JSON 顺序列出、每条边一行 `A → B（标签）`），lint 可直接调用复算。

[U-BEH-6|13b7] tools/quality_scan.py 比较技术要点相似度之前，先去掉生成区块、图片行、`###` 标题行和四个标签本身（只剩标签后的正文）。阈值在第三段用改写后的 21 对重新校准，规则不变：中英文各取实测最大值，阈值落在 0.05 网格上且不低于最大值 + 0.10；注释写明样本数、最大值来自哪两页、日期。

[U-BEH-7|c964] 文档同步：tools/schema.md 的 Key techniques 一节改成上面的形状、写法说明与一个完整示例（用 screenshot-to-code）；tools/schema.md:108 表格行补「机制图 + 每招四行」；AGENTS.md 的技术要点描述同步；`.claude/skills/add-project`、`sync-entry`、`read-repo` 三个技能补「写 mechanisms/<stem>.json → 跑 mechanism_card.py」一步；Makefile 加 `mechanisms` 目标，`make test` 加 `tools/test_mechanism_card.py`。

[U-BEH-8|ad24] 改写 21 对页面：每对先跑 `python3 tools/upstream_snapshot.py --page <page>` 对比上游；上游没变则沿用已核实的事实，只重写技术要点；上游变了就按 sync-entry 全流程复核这一对。技术要点按页面里已有链接钉住的 commit 重读源码，拆成 2–6 招，画机制图；每行一两句白话，术语第一次出现时解释。改完把两页 `last_verified` 更新为改写当天（UTC）。

## 待决策

[U-DEC-1|5748] 机制图的源文件用什么格式：一份中英双语的 JSON，由生成器拼出两种语言的 d2；还是中英各手写一份 `.d2` 文件。 裁决（2026-10-15）：选 A，一份中英对照的底稿出两张图。

[U-DEC-2|37de] 闭源分发的页面（funtool、nopecha-extension）和纯清单页（awesome-deep-trading）怎么满足「每页一张图、每招有源码行」。 裁决（2026-10-15）：选 A，照样画图拆招。

[U-DEC-3|b15b] CI 怎么判断图是否过期：图里盖源文件哈希、CI 只比哈希；还是 CI 安装 d2 后重新渲染比对。 裁决（2026-10-15）：选 A，图里记下底稿版本，检查时只比记号。

## 不可逆动作

[U-GATE-1|a0dc] 无。全部改动在 git 里，可整体 revert；843 对 v1 页不动。

## 既有契约与回归红线

[U-CTR-1|dd55] `last_verified` 晚于 UTC 今天是 ERROR（tools/lint.py `today_utc()`，2026-09-22 UTC+8 午夜后写页被 CI 拒的事故）。门槛日期 2026-10-15 等于今天 UTC，可写。

[U-CTR-2|a881] 快速上手的流程卡与 flow-steps 区块不变：`python3 tools/flow_card.py --all` 之后 `git status --porcelain flows assets/flow categories` 除本 run 改写的页面外必须为空。

[U-CTR-3|f178] `<!-- oss-atlas:unresearched -->` 标记仍让 lint 报 ERROR，生成器骨架照旧带标记，不因结构检查多报一串错。

[U-CTR-4|a9bb] 章节契约 v2 的章节顺序、新旧标题互斥、技术要点必需与双语一致（section-contract-v2 的 U-BEH-1 至 U-BEH-8）全部不变。

[U-CTR-5|09a8] 中文页全角标点检查覆盖四行标签：中文标签用全角冒号 `：`；生成区块与代码块照旧不查。

[U-CTR-6|7804] `duplicated-section-prose-reverified` 门禁继续生效：改写后的页面日期更新，会立刻受查重门禁约束，所以 U-BEH-6 的剔除必须先于第二段落地。

## 新增依赖

[U-DEP-1|e4b2] d2 命令行（作者本机，已装 v0.9.0，`/opt/homebrew/bin/d2`）。解决：owner 选定 d2 出图。为什么现有栈不够：仓库现有 SVG 都由纯 Python 手排（flow_card、health_card），通用有向图的自动布局手写成本高。成本：写页的人要装 d2；CI 不装（见 U-DEC-3 推荐）。备选：纯 Python 手排线性图（只能画直线流程，画不了分叉和回环）。

## 边界

[U-NG-1|fbf8] 不动 843 对 v1 页（864 − 21）；它们下次复核时才按新形状写。

[U-NG-2|92de] 不用 Mermaid，不在页面里放图源码。

[U-NG-3|d77b] CI 不安装 d2，不在 CI 里渲染图。

[U-NG-4|52f3] 不改快速上手流程卡的生成器、格式与内容。

[U-NG-5|866a] 不处理 BACKLOG 里「短技术要点按去链接前长度判定」的政策问题，只在第三段校准时记录新数据。

## 翻车假设

[U-SPK-1|f0f2] 假设：d2 能正常排中文、同版本重复渲染输出一致。已验证（2026-10-15，d2 v0.9.0）：同一份含中文的源渲染两次 `cmp` 一致；rsvg 光栅化后中文正常显示、方框宽度够；`--layout elk` 可用。

[U-SPK-2|6dd9] 假设：GitHub 页面上 SVG 里的中文能显示。d2 只内嵌拉丁字体子集，中文靠看图人机器的系统字体兜底 [推断：依据是 SVG 里只有 d2 自带字体声明，没在 GitHub 上实看]。处置：第一段推分支后在 GitHub 文件页实看 screenshot-to-code.zh.md，看不到中文就改为在 SVG 里声明中文字体族兜底。

[U-SPK-3|1059] 假设：闭源页和纯清单页也能画出有意义的图、拆出至少两招。需 spike：第一段样板除 screenshot-to-code 外再做 funtool 一对，owner 看样板时一并判断；判断不通过就回来改 U-DEC-2。

[U-SPK-4|c01c] 假设：剔除标签后，四行结构不会让不同页面的技术要点相似度明显升高。处置：第一段用两个样板页加 19 对旧散文页先算一次，最大值超过现阈值 0.15 就停下报 owner。

## 场景化推演

| Scenario | Actor / Context | Step-by-step path | System touchpoints | Exposed issue | Requirement / Contract |
|---|---|---|---|---|---|
| 新收录 | add-project 写新页 | 写四行招 → 写 mechanisms JSON → 跑 mechanism_card → lint | 生成器、lint 结构检查、哈希比对 | 改了 JSON 忘了重渲染，图过期 | U-BEH-3、U-BEH-5、U-ACC-2 |
| CI 上检查 | 别人的 PR 改了某页 JSON | CI 跑 lint，没有 d2 | 哈希戳 | CI 无法渲染也要能判断过期 | U-DEC-3、U-NG-3 |
| 闭源页 | 改写 funtool | 招的源码行无代码可链 | 「源码」行链接检查 | 必须有出处又不能编源码 | U-DEC-2、U-SPK-3 |
| 批量骨架 | intake_queue_apply 生成新页 | 技术要点只有待研究标记 | 结构检查跳过规则 | 骨架不该多报一串结构错 | U-BEH-3、U-CTR-3 |
| 未改写的 v2 页 | 第二段进行中，10-13 的页还是散文 | 别的 PR 跑 lint | 门槛判定 | 不能因新规则让 main 变红 | U-BEH-1 |

## 方案

方案 A（推荐）：双语 JSON 为源，生成器拼 d2 并渲染，SVG 盖源哈希，页面里放生成的文字版；lint 纯 Python 复核形状、文字版和哈希。优点：中英两张图拓扑必然一致；agent 读文字版就能拿到图的内容；CI 不需要新依赖。代价：JSON 只能表达节点、边、虚线，d2 的分组、形状等高级排版用不上。

方案 B：中英各手写一份 `.d2`，页面直接引用渲染结果。否决理由：两份源会漂移，lint 没法判断中英图是否同一张；文字版要另写一份，又多一处漂移。

方案 C：CI 安装 d2，每次重渲染比对 SVG。否决理由：引入 CI 依赖与版本固定问题，d2 小版本升级就可能让全部 SVG 字节变化、整片报红。

## 现成方案

- 门槛判定 — 停在第 2 级：照抄 `sections_v2()`（tools/lint.py:108 附近）。
- stem 命名 — 停在第 2 级：复用 `flow_card.flow_stem` 与 `duplicate_slugs`（tools/flow_card.py:149-168）。
- 生成区块的写回与漂移检测 — 停在第 2 级：照抄 flow_card 的 `BEGIN`/`END`/`BLOCK_RE` 与 `steps_block` 写回方式（tools/flow_card.py:82-84、470）。
- 章节定位 — 停在第 2 级：复用 `flow_card.section_bounds`（tools/flow_card.py:657）。
- d2 调用 — 停在第 3 级：标准库 `subprocess.run`。
- 哈希 — 停在第 3 级：标准库 `hashlib.sha256`。
- 查重剔除 — 停在第 2 级：在 quality_scan.py 现有去链接函数旁加一个剔除函数。
- 新增依赖：d2（见 U-DEP-1）。

## 改动范围

可改：

```diff
 tools/
+├── mechanism_card.py        # JSON → d2 → SVG + 哈希戳 + 文字版写回
+├── test_mechanism_card.py   # 生成器单测
 ├── lint.py                  # 门槛 + 结构化技术要点检查
 ├── test_lint.py             # 新用例（U-ACC-2）
 ├── quality_scan.py          # 技术要点剔除 + 第三段重校准
 ├── test_quality_scan.py
 └── schema.md                # Key techniques 一节重写
+mechanisms/<stem>.json        # 21 份
+assets/mechanism/<stem>{.svg,.zh.svg}   # 42 张
 AGENTS.md
 Makefile                     # mechanisms 目标、make test
 .claude/skills/{add-project,sync-entry,read-repo}/SKILL.md
 categories/<21 对 v2 页>{.md,.zh.md}
 docs/specs/key-techniques-structured/
```

调用树：

```diff
 lint.check_page(path)
   sections_v2(last_verified)
   check_v2_order(...)
+  if techniques_structured(last_verified):
+      check_structured_techniques(path, text, zh, root)   # 形状、链接、招数
+          mechanism_card.text_block(spec, lang)            # 文字版复算
+          mechanism_card.svg_stamp(svg) == spec_hash(spec) # 过期判断
```

看着相关但别碰：

- `tools/flow_card.py` 与 `flows/`、`assets/flow/` — 快速上手流程卡不变（U-NG-4、U-CTR-2），只 import 它的 stem 与定位函数。
- `.github/workflows/lint.yml` — 不加 d2（U-NG-3）。
- 21 对以外的 `categories/` 页面 — U-NG-1。
- `tools/intake_queue_apply.py`、`tools/agent_skills_intake.py` — 骨架照旧只放待研究标记（U-CTR-3）。

## 验收承诺

[U-ACC-1|fe68] `make gates` 与 `make test` 全绿，贴输出的页数与测试数行。

[U-ACC-2|5306] `tools/test_lint.py` 与 `tools/test_mechanism_card.py` 各有一条编号用例覆盖：缺图片行、图片文件不存在、缺生成区块、生成区块被手改、SVG 哈希过期、招少于 2、编号不连续、缺一个标签、标签乱序、标签值为空、源码行无链接、中英招数不同、节点招编号越界、某招没有节点、`2026-10-14` 的散文 v2 页通过、v1 页不受影响、只有待研究标记的骨架只报标记错误、本机无 d2 时生成器退出码 2。

[U-ACC-3|38e7] 第一段结束时 screenshot-to-code 与 funtool 两对按新形状通过 lint，owner 看过这两个样板并确认，才开第二段。

[U-ACC-4|d331] 收尾时 21 对页面全部是结构化页：`last_verified >= 2026-10-15`，每对有 `mechanisms/<stem>.json` 与两张 SVG；全库再没有 `last_verified` 落在 2026-10-13 至 2026-10-14 的页面。

[U-ACC-5|a970] `python3 tools/mechanism_card.py --all` 连跑两次，第二次 `git status --porcelain` 为空。

[U-ACC-6|37bf] quality_scan.py 的技术要点阈值注释更新为 21 对改写后的实测：样本数、最大值及来自哪两页、日期；新增测试证明两段四行结构相同但正文不同的技术要点不会被判重复，正文雷同的仍会被判重复。

[U-ACC-7|5903] 相对 `c0f548ab` 的改动只落在「改动范围」列出的路径里（验收脚本用 `git diff --name-only` 比对白名单）。

## 实施步骤

### 第一段：契约、生成器、检查、两个样板（serial，结束停下给 owner 看）

1. tools/mechanism_card.py + tools/test_mechanism_card.py — 实现 U-BEH-4/5 — 验证：`python3 -m unittest tools.test_mechanism_card`。
2. tools/lint.py + tools/test_lint.py — 实现 U-BEH-1/3 — 验证：`python3 -m unittest tools.test_lint`。
3. tools/quality_scan.py — 实现 U-BEH-6 的剔除，阈值暂不动；按 U-SPK-4 算一次并记录 — 验证：`python3 -m unittest tools.test_quality_scan`。
4. tools/schema.md、AGENTS.md、Makefile、三个技能 — U-BEH-7 — 验证：`make gates`。
5. screenshot-to-code 与 funtool 两对按 U-BEH-8 改写 — 验证：`make gates`、`python3 tools/mechanism_card.py --all` 无差异、打开四张 SVG 目视。

### 第二段：改写 10 对（sample-pages.md 前 10 对，按 U-BEH-8）

验证：`make gates`；评审至少抽 3 对逐条对照源码核对招与源码行。

### 第三段：改写剩余 9 对 + 查重重校准 + 收尾

改写 sample-pages.md 剩余对（除 funtool 外），按 U-BEH-6 重校准阈值。验证：`make gates`、`make test`、U-ACC-4 至 U-ACC-7 的验收脚本。

```yaml
# spec-contract
checks:
  - "make gates 与 make test 全绿"
  - "test_lint / test_mechanism_card 覆盖 U-ACC-2 列出的 18 种情形"
  - "21 对页面 last_verified >= 2026-10-15 且各有 mechanisms JSON 与两张 SVG"
  - "mechanism_card.py --all 连跑两次无差异"
  - "改动只落在白名单路径"
non_goals:
  - "不动 843 对 v1 页"
  - "不用 Mermaid"
  - "CI 不装 d2"
  - "不改快速上手流程卡"
  - "不处理短技术要点长度政策"
validation_commands:
  - "make gates"
  - "make test"
  - "python3 tools/mechanism_card.py --all && git status --porcelain"
locked_decisions:
  - "技术要点 = 总图 + 每招 ### 小标题 + 解决/做法/边界/源码四行"
  - "图用 d2 生成 SVG 存 assets/"
  - "lint 硬查，改写 21 对"
  - "开发路线 /dev-long-run"
derisk_spikes:
  - type: "外部工具行为（d2 中文与确定性）"
    question: "d2 能否正常排中文且重复渲染输出一致"
    method: "同源渲染两次 cmp + rsvg 光栅化目视"
    status: "verified"
  - type: "外部平台渲染（GitHub 显示 SVG 中文）"
    question: "GitHub 文件页上 SVG 里的中文能否显示"
    method: "第一段推分支后在 GitHub 文件页实看"
    status: "spike-before-implement"
  - type: "数据形态边界（闭源与纯清单页）"
    question: "闭源页能否画出有意义的图并拆出两招"
    method: "第一段做 funtool 样板，owner 判断"
    status: "spike-before-implement"
```
