Audience:   P3 实现 agent
Scope:      选型页章节契约 v2：新顺序、怎么用起来改名快速上手、新增技术要点，lint 按 last_verified 门槛双轨 / Non-scope: 迁移已有页面（除第二段抽样的 20 对）
State:      approved
Genre:      G-SPEC
Code-Root:  /Users/zhenninglang/Projects/oss-atlas-wt-sections
Prefixes:   U-DEC, U-BEH, U-GATE, U-SPK, U-ACC, U-NG, U-DEP, U-CTR, U-DIAG

# section-contract-v2 · G-SPEC 机器版 spec

Planned at: fd9126dc · 2026-10-13

开发路线：/dev-long-run，分三段（owner 2026-10-13 选定）。

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
- v1 页：`last_verified` 早于门槛日期的页面，按现行规则检查，一个字节都不需要改。
- v2 页：`last_verified` 不早于门槛日期的页面，按本 spec 的新顺序、新标题检查，技术要点必写。
- 门槛日期：常量 `SECTIONS_V2_FROM`，环境变量 `OSS_ATLAS_SECTIONS_V2_FROM` 可覆盖，写法照抄 `FLOW_REQUIRED_FROM`（tools/lint.py:104）。

## TL;DR

新写或复核的页面改用新章节顺序：何时使用 → 何时不用 → 横向对比 → 快问快答（可选）→ 快速上手 → 技术要点 → 技术栈 → 依赖 → 运维难度 → 健康度 → 存疑。lint 按 `last_verified` 是否到门槛日期分两套规则，旧页不动。首个 v2 页是 screenshot-to-code。

## 根因与现状

[U-DIAG-1|0b97] “怎么用起来”被写成内部机制的根因是契约措辞：tools/schema.md:223 要求机制段 “Explain how it works underneath in the simplest terms”，英文标题又叫 `How it works`，写页的 agent 照字面写成了实现原理（2026-10-13 screenshot-to-code 实录，已由 PR #193 修正内容）。现行契约没有任何章节承载“它靠哪几招做到”，所以技术要点只能挤进别的章节。

[U-DIAG-2|bcdb] 现行 lint 只校验两个章节的位置：快问快答（check_qa，tools/lint.py:709）与怎么用起来（check_flow_section，tools/lint.py:628-633）。何时使用、何时不用、横向对比、技术栈、依赖、运维难度、健康度只查存在（required_sections，tools/lint.py:271），不查顺序。

## 已锁定（owner 2026-10-13）

- v2 章节顺序与名称见 TL;DR；英文名依次为 `When to use`、`When NOT to use`、`Comparison`、`Q&A`、`Quick start`、`Key techniques`、`Tech stack`、`Dependencies`、`Ops difficulty`、`Health & viability`、`Caveats (unverified)`。
- “快速上手 / Quick start”就是原“怎么用起来 / How it works”改名，内容改为开发者选定后怎么用起来；流程卡留在这一节。
- 技术要点 v2 页必写；旧页不强制、不迁移。
- skill-pack 类型照旧不写技术栈、依赖、运维难度。

## 有意行为变化

[U-BEH-1|d218] v2 页的全部 H2 必须严格按 TL;DR 顺序出现：快速上手（满足 FLOW 门槛时）、技术要点为必需，快速问答可缺省，skill-pack 缺省技术栈/依赖/运维难度且禁止出现。违反顺序报 ERROR，指出第一个错位的标题。

[U-BEH-2|9524] v2 页出现旧标题 `## How it works` / `## 怎么用起来` 报 ERROR，提示改名为 `## Quick start` / `## 快速上手`。v1 页出现新标题 `Quick start` / `快速上手` / `Key techniques` / `技术要点` 也报 ERROR，提示“新结构需要把 last_verified 更新到门槛之后”，避免半迁移页面。

[U-BEH-3|683e] v2 页缺 `## Key techniques` / `## 技术要点` 报 ERROR；该节为空（只有空白）报 ERROR；双语一方有、一方没有，各自按缺失报错，另在 EN 页报一条“presence must match the bilingual sibling”。

[U-BEH-4|efb8] v2 页快速问答的位置规则改为：紧跟横向对比之后、快速上手之前（快速上手缺省时在技术要点之前）。v1 页维持现行规则（何时使用之后、怎么用起来或何时不用之前）。

[U-BEH-5|8d11] flow_card.py 的章节定位同时认旧标题与新标题：`SECTION` 改为按页面版本取标题，`section_bounds` 先找新标题、找不到再找旧标题。生成的文字版（flow-steps 区块）内容不变。

[U-BEH-6|6b25] 两个批量生成器（tools/intake_queue_apply.py、tools/agent_skills_intake.py）按 v2 顺序产出页面骨架，快速上手与技术要点两节放 `<!-- oss-atlas:unresearched -->` 标记。它们写 `last_verified: {TODAY}`，产出必然是 v2 页。

[U-BEH-7|9f3c] sync-entry 复核旧页即把它升到 v2：bump `last_verified` 前必须手工按新顺序重排、改标题、写技术要点（不提供自动重排工具，见 U-DEC-3 裁决）。复核一页的工作量因此增加一节研究。

[U-BEH-8|d840] v2 页出现规定集合之外的 H2 标题报 ERROR（按 U-DEC-2 的推荐写）。

[U-BEH-9|8223] 第二段把 20 对旧页复核成 v2：按顶层分类分散挑选（每个顶层分类最多 2 对），同分类里挑 `last_verified` 最早的，类型尽量覆盖 tool / library / app / service / framework；每对按 sync-entry 全流程复核（事实重核、快速上手按开发者用法重写、技术要点从源码研究后写、健康度重算）。挑选清单与理由写进本目录 `sample-pages.md`。

[U-BEH-10|a2d5] 第三段把 `Key techniques` / `技术要点` 加入 tools/quality_scan.py 的 `DUP_SECTIONS`：对 21 对 v2 页两两计算该节相似度，中英文各取实测最大值之上的阈值（与现有各节阈值的定法相同，tools/quality_scan.py:55-70 注释），并在注释里写明样本数、实测最大值与日期。

## 待决策

[U-DEC-1|faa5] 门槛日期取 2026-10-13 还是 2026-10-14。2026-10-14 在今天（UTC 2026-10-13）是未来日期，screenshot-to-code 写不进去（lint 对未来日期报 ERROR，见 U-CTR-1），只能等到明天才能合并首个 v2 页。 裁决（2026-10-13）：门槛日期定在 10 月 13 日。

[U-DEC-2|7a9e] v2 页出现规定集合之外的 H2（如 `## Install`、`## Notes`）是报错还是放行。 裁决（2026-10-13）：规定之外的大标题报错。

[U-DEC-3|6ab9] 是否新增确定性重排脚本 `tools/section_order.py`（只搬动章节、改标题，不改内容），供 sync-entry 复核旧页时一键转 v2 骨架，技术要点留 unresearched 标记待写。 裁决（2026-10-13）：不加自动重排工具，复核旧页时手工搬章节。

[U-DEC-4|0a83] 技术要点是否立刻加入 quality_scan.py 的 `DUP_SECTIONS` 重复度检查。阈值需要研究过的页面样本来定，目前只有 1 页。 裁决（2026-10-13）：抽取 20 个项目补写技术要点（按分类分散、优先挑最久没复核的），用这批真实样本定技术要点的查重阈值并加入查重检查。

## 不可逆动作

[U-GATE-1|7a4e] 无。契约改动全在 git 里，可整体 revert；旧页不改，回退不丢内容。

## 既有契约与回归红线

[U-CTR-1|51e3] `last_verified` 晚于 UTC 今天是 ERROR（tools/lint.py `today_utc()`，2026-09-22 UTC+8 午夜后写页被 CI 拒的事故）。门槛日期因此不能晚于首个 v2 页可写的日期。

[U-CTR-2|439f] flow-steps 文字版区块由 tools/flow_card.py 生成，人不手改，lint 对漂移报 ERROR（schema §2）。改名后区块内容必须逐字节不变，否则 864 对页面的预提交钩子会全部重写。

[U-CTR-3|f264] `<!-- oss-atlas:unresearched -->` 标记让 lint 报 ERROR，生成器骨架不能合并（AGENTS.md “Prose nobody earned”）。新增的两节沿用同一标记，不写占位散文。

[U-CTR-4|87bc] FLOW 门槛（`OSS_ATLAS_FLOW_REQUIRED_FROM`，默认 2026-09-20）继续生效：v2 页的快速上手同样受它约束；`OSS_ATLAS_REQUIRE_FLOW=1` 语义不变。

[U-CTR-5|5b47] 快速问答“必须做决定、章节可选、绝不凑数”的规则不变，只改位置。

[U-CTR-6|3cfc] 中文页全角标点规则、双语 frontmatter 一致规则不变；新章节在 `.zh.md` 里同样受全角标点 lint 约束。

## 新增依赖

[U-DEP-1|6ca5] 无。全部用 Python 标准库与仓库已有函数实现。

## 边界

[U-NG-1|6157] 不迁移已有 864 对页面；它们保持旧顺序与旧标题，直到下次复核。

[U-NG-2|bd88] 第一段、第二段不定技术要点的查重阈值；阈值只在第三段用 20 对样本加 screenshot-to-code 共 21 对定。

[U-NG-3|8661] 不改 select-oss 公开技能的读页流程；它按 `When NOT to use` 等标题读，顺序变化不影响（skills/select-oss/SKILL.md:70）。

[U-NG-4|9ced] 不改健康度、对比表、标点等其它 lint 规则。

## 翻车假设

[U-SPK-1|74ff] 假设：全库只有 screenshot-to-code 一对页面 `last_verified >= 2026-10-13`。已验证：`grep -rl "^last_verified: 2026-10-1[3-9]" categories` 返回 2 个文件，均为 screenshot-to-code；`gh pr list --state open` 为空，没有在途分支会带进同日期旧结构页面。

[U-SPK-2|86fa] 假设：改动 flow_card 章节定位不会改变任何已有页面的生成产物。验证方式：实现后跑 `python3 tools/flow_card.py --all` 再 `git status --porcelain categories assets flows`，除 screenshot-to-code 外必须为空。

[U-SPK-3|85c3] 假设：20 对页面的健康度重算能拿到完整数据。已知风险：并发查询外部数据源时 health.py 会写出 “?”（2026-09 实录）。处置：第二段健康度重算一律串行；出现 “?” 先撤回该页改动，等接口恢复再算。

## 场景化推演

| Scenario | Actor / Context | Step-by-step path | System touchpoints | Exposed issue | Requirement / Contract |
|---|---|---|---|---|---|
| 新收录 | add-project 收录新仓库 | 写 v2 页 → 漏写技术要点 → 跑 lint | lint.py 版本判定、必需章节 | 新页漏节必须被拦 | U-BEH-3、U-ACC-2 |
| 复核旧页 | sync-entry 复核 2026-07 写的旧页 | bump last_verified → 仍是旧顺序、旧标题 → lint | 版本判定、旧标题检查 | 半迁移页面必须被拦，且要给出怎么改 | U-BEH-1、U-BEH-2、U-DEC-3 |
| 不碰的旧页 | 864 对旧页在别的 PR 里被预提交钩子扫到 | flow_card --all → lint | flow_card 定位、v1 规则 | 旧页任何产物都不能变 | U-CTR-2、U-SPK-2、U-ACC-3 |
| 批量生成 | intake_queue_apply 生成骨架 | 写 last_verified=今天 → v2 → 两节放标记 | 生成器模板、unresearched 检查 | 骨架必须是 v2 形状且不能合并 | U-BEH-6、U-CTR-3 |

## 方案

方案 A（推荐）：版本由 `last_verified` 与门槛日期决定，一个函数 `sections_v2(last_verified)` 统一判定；v2 页走一个新的有序检查函数 `check_v2_order`，v1 页走现行代码路径不改一行。优点：旧页零风险，判定口径与 FLOW 门槛同构。代价：lint 里两套位置规则并存，直到旧页复核完。

方案 B：按页面实际用了哪个标题判定版本。否决理由：页面可以永远不用新标题而躲开技术要点必写，契约等于没有。

方案 C：一次性脚本迁移全部页面。否决理由：owner 已拍板不迁移（U-NG-1）；且技术要点无法机械生成，迁移后 864 对页面都会挂 unresearched 标记而全部报错。

## 现成方案

- 版本判定 — 停在第 2 级：照抄 `flow_required()`（tools/lint.py:600）。
- 章节定位 — 停在第 2 级：复用 `flow_card.section_bounds` 与 `section_after_heading`（tools/lint.py:701）。
- H2 列表 — 停在第 2 级：复用 check_qa 里已有的 `re.finditer(r"(?m)^##[ \t]+\S.*$", text)`。
- 重排脚本 — 停在第 1 级：不做（U-DEC-3 裁决手工搬）。
- 相似度计算 — 停在第 2 级：复用 quality_scan.py 现有 `duplicated-section-prose` 的比较函数，只加章节名与阈值。
- 新增依赖：无。

## 改动范围

可改：

```diff
 tools/
 ├── lint.py               # 版本判定 + v2 有序检查 + 新旧标题互斥 + 技术要点必需/非空/双语
 ├── flow_card.py          # SECTION 认新旧两个标题
 ├── test_lint.py          # 新增 v2 用例
 ├── test_flow_card.py     # 新标题定位用例
 ├── intake_queue_apply.py # 骨架改 v2 顺序 + 两节标记
 ├── agent_skills_intake.py# 同上
 ├── quality_scan.py       # 第三段：DUP_SECTIONS 加技术要点
 ├── test_quality_scan.py  # 第三段：对应用例（文件不存在则新建）
 └── schema.md             # §2 表格、快速上手与技术要点两节写法、v1/v2 双轨说明
 AGENTS.md                 # 章节描述
 CONTRIBUTING.md           # 第 30 行附近
 README.md / README.zh.md  # 章节表（1236 / 1226 行附近）
 Makefile                  # help 里 How-it-works 字样
 .claude/skills/add-project/SKILL.md
 .claude/skills/sync-entry/SKILL.md   # 复核即升 v2 的步骤
 .claude/skills/read-repo/SKILL.md
 .claude/skills/intake-tabs/SKILL.md  # 引用快速问答位置处
 categories/ai-design-generation/screenshot-to-code{.md,.zh.md}
 categories/<20 对抽样页>              # 第二段
 flows/<20 对抽样页>.json             # 第二段，只在流程卡需要重写时
 docs/specs/section-contract-v2/      # 本 spec + sample-pages.md
```

看着相关但别碰：

- `categories/` 下除 screenshot-to-code 与第二段抽样页外的任何页面 — 旧页不迁移（U-NG-1）。
- `flows/*.json` 与 `assets/flow/*.svg` — 内容不随标题改名而变（U-CTR-2）。
- `skills/select-oss/` — 读页流程不依赖顺序（U-NG-3）。
- `tools/health.py`、`tools/sync-health-to-body.py` — 只碰健康度节，与本次无关。

## 关键接口

```python
SECTIONS_V2_FROM = os.environ.get("OSS_ATLAS_SECTIONS_V2_FROM", "2026-10-13")

def sections_v2(last_verified: object) -> bool: ...   # 同 flow_required 的解析与容错

V2_ORDER_EN = ["## When to use", "## When NOT to use", "## Comparison", "## Q&A",
               "## Quick start", "## Key techniques", "## Tech stack", "## Dependencies",
               "## Ops difficulty", "## Health & viability", "## Caveats"]   # Caveats 前缀匹配
V2_ORDER_ZH = [... 对应中文 ...]

def check_v2_order(path, text, zh, ptype, rep) -> None: ...
```

## 实施步骤

### 第一段：契约与检查脚本（一个 commit）

1. tools/lint.py 与 tools/flow_card.py — 加 `sections_v2`、`check_v2_order`、新旧标题互斥、技术要点检查；v1 路径保持原样；v2 页跳过 check_qa 的 v1 位置分支，改走新位置规则 — 验证：`make test`。
2. tools/test_lint.py、tools/test_flow_card.py — 补用例（见 U-ACC-2）— 验证：`python3 -m unittest tools.test_lint tools.test_flow_card`。
3. 两个生成器 — 改骨架 — 验证：`make test`，并产出一页目测顺序。
4. schema.md、AGENTS.md、CONTRIBUTING.md、README 两份、Makefile、四个技能 — 措辞；sync-entry 写明手工升 v2 的步骤 — 验证：`grep -rn "how it works underneath"` 为空。
5. screenshot-to-code 两页 — 按 v2 重排、改标题、把快问快答第一问移成技术要点 — 验证：`make gates`。
6. 全量回归 — `python3 tools/flow_card.py --all` 后除 screenshot-to-code 外无产物变化 — 验证：`git status --porcelain`。

### 第二段：20 对抽样页复核成 v2（每对一个 commit）

7. 按 U-BEH-9 写 `sample-pages.md`（20 行：页面路径、顶层分类、类型、原 last_verified、挑选理由）— 验证：人工核对每个顶层分类不超过 2 对。
8. 逐对跑 sync-entry 全流程升 v2 — 验证：每对提交前 `make gates` 零 error。健康度重算串行跑，不并发（U-SPK-3）。

### 第三段：技术要点查重阈值（一个 commit）

9. 对 21 对 v2 页两两算技术要点相似度，记录中英文最大值 — 验证：脚本输出贴进 commit message。
10. tools/quality_scan.py 加阈值与注释，补测试 — 验证：`make test` 与 `python3 tools/quality_scan.py --fail-on-gated`。

## 验收承诺

[U-ACC-1|0ffe] `make gates` 与 `make test` 全绿，贴输出行。

[U-ACC-2|52bd] 单测逐条覆盖：v2 缺技术要点报错；v2 技术要点为空报错；v2 顺序错报错（例：横向对比排在快速上手之后）；v2 用旧标题报错；v1 页用新标题报错；v1 旧结构照常通过（零 error）；双语一方缺技术要点报错；v2 快速问答放在何时使用之后报错、放在横向对比之后通过；v2 skill-pack 省略技术栈三节通过；flow_card 在 `## Quick start` 下定位流程卡。

[U-ACC-3|301b] 第一段：除 screenshot-to-code 外，`categories/`、`flows/`、`assets/` 无任何文件变化（`git diff --stat origin/main -- categories flows assets` 只列 screenshot-to-code 相关文件）。

[U-ACC-4|2b52] screenshot-to-code 两页按 v2 通过 lint，且 `## 技术要点` 含原快问快答第一问的全部事实。

[U-ACC-5|2375] 第二段：`sample-pages.md` 列出 20 对；这 20 对页面全部 `last_verified >= 2026-10-13`、按 v2 通过 lint，每对的技术要点写的是该项目源码里看得到的做法（reviewer 抽查至少 5 对，逐条对源码）。

[U-ACC-6|c416] 第三段：`DUP_SECTIONS` 含技术要点中英文阈值，注释写明样本 21 对、实测最大值与日期；`quality_scan.py --fail-on-gated` 通过；新增测试证明两段雷同的技术要点会被报出。

```yaml
# spec-contract
checks:
  - "make gates 与 make test 退出码 0"
  - "test_lint 新增用例覆盖 U-ACC-2 列出的 10 个场景"
  - "第二段 20 对页面按 v2 通过 lint"
  - "第三段 DUP_SECTIONS 含技术要点阈值且注释写明样本数与实测最大值"
  - "第一段 commit 里 categories flows assets 只含 screenshot-to-code 相关文件"
  - "grep -rn 'how it works underneath' tools AGENTS.md CONTRIBUTING.md .claude 为空"
non_goals:
  - "迁移已有 864 对页面"
  - "改 select-oss 读页流程"
validation_commands:
  - "make test"
  - "make gates"
  - "python3 tools/flow_card.py --all && git status --porcelain"
locked_decisions:
  - "v2 顺序：何时使用→何时不用→横向对比→快问快答(可选)→快速上手→技术要点→技术栈→依赖→运维难度→健康度→存疑"
  - "怎么用起来改名快速上手，内容为开发者用法，流程卡留在此节"
  - "技术要点 v2 页必写，旧页不迁移（第二段抽样 20 对除外）"
  - "门槛日期 2026-10-13；规定之外的 H2 报错；不做自动重排工具"
  - "第二段抽 20 对：按顶层分类分散、优先最久没复核"
derisk_spikes:
  - type: "4 数据形态边界"
    question: "门槛日期之后是否只有 screenshot-to-code 一对页面"
    method: "grep last_verified + gh pr list"
    status: "verified"
  - type: "2 实际契约"
    question: "flow_card 改标题定位后已有页面产物是否逐字节不变"
    method: "flow_card --all 后 git status"
    status: "spike-before-implement"
```
