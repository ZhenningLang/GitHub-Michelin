---
name: Logseq
slug: logseq
repo: https://github.com/logseq/logseq
category: knowledge-base
tags: [knowledge-base, outliner, local-first, markdown, clojurescript, datalog, privacy, plugin-api, agpl]
language: ClojureScript (app) + Clojure (tooling)
license: AGPL-3.0
maturity: Mature, active; stable 2.0.1 (2026-07), nightly channel published 2026-09; ~45k stars (as of 2026-09)
last_verified: 2026-09-19
type: app
upstream:
  pushed_at: 2026-09-19T15:41:02Z
  default_branch: master
  default_branch_sha: 127e3bb73de4547e85ad077bac616908c04400af
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:25:07Z
  overall: B
  overall_score: 3.17
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 249.2
        qualifying_issues: 20
        band: relaxed_solo
        window_offset_days: 9
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: null
        canonical_package: null
        homebrew_installs_90d: 1260
        homebrew_tier: B
        release_downloads: 89236369
        release_assets: 1070
        release_tier: A
        signal_basis: homebrew+releases
    longevity:
      grade: A
      raw:
        repo_age_days: 2314
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 52
        top1_share: 0.543
        top3_share: 0.798
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: D
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
---

# Logseq

一款隐私优先、本地优先的大纲笔记工具，面向知识管理与协作：你写 markdown／org 块，用引用把它们连起来，并用 Datalog 查询图谱——除非插件引入，否则整个过程没有 LLM 参与。

![Logseq — 健康度雷达](../../assets/health/logseq.zh.svg)

## 何时使用

你是一名用项目符号思考的开发者，想要一个**属于自己**的个人知识库——文件就在磁盘上，不需要账号，打开时不发任何网络请求。你试过 Notion 这类工具，但讨厌笔记躺在别人的数据库里；你想查询自己的图谱（「列出所有带 `#project` 标签、引用了 `[[topic]]`、且本月写入的块」），而不是去问聊天机器人。你还想要一个成熟的应用：多年的发布历史、庞大的插件生态，以及一个可以 `git clone` 的文件格式。

于是你装上 Logseq，指向一个本地文件夹，它就把你的 markdown／org 文件索引成可以引用、可以反链的块。因为编辑器是块式的、一切都是本地 markdown，你便同时得到自己的文件、版本控制，以及覆盖同一张图谱的 Datalog 查询层。当你想要**自己当作者**、拒绝让模型改写笔记时，选它而不是 [LLM Wiki](llm-wiki.zh.md)；当「纯文件大纲工具 + 庞大插件社区」比「块级引用 + 自托管服务端访问」更重要时，选它而不是 [SiYuan](siyuan.zh.md)。

## 何时不用

- **不要指望它替你撰写或维护维基。** Logseq 是人写的；没有把资料编译成页面的摄入流水线。如果维护负担正是你想甩掉的东西，请用 [LLM Wiki](llm-wiki.zh.md) 或 [Khoj](khoj.zh.md) 这类 AI 第二大脑。
- **不要把 DB 版本用在丢不起的东西上。** README 明确说明 DB 版本处于 **beta**、**可能发生数据丢失**，并建议做备份或使用专门的测试图谱；新的移动端应用与 RTC 同步处于 **alpha**。要么留在基于文件的版本，要么保持自动备份——如果你今天就需要一个稳定的存储，它不适合。
- **需要服务端级自托管与第一方移动应用时不要用。** 它没有 Docker 服务端版本；想要一个能从浏览器或容器访问的 Go 内核工作空间，请用 [SiYuan](siyuan.zh.md)。
- **暂时不适合实时团队协作。** RTC 尚在 alpha，也没有针对多写者冲突的加固；团队知识请用 `team-chat` 或托管维基。
- **需要富 WYSIWYG／数据库式工作空间时不要用。** 对非技术用户来说，块式大纲显得简陋；文档型工作空间（SiYuan 或 Notion 风格工具）更合适。
- **无法接受 AGPL-3.0 时不要用。** 若你分发修改后的应用，copyleft 义务适用。[推断]
- **注意贡献者池。** 内核是 ClojureScript／Clojure 加一个 fork 过的 DataScript——小众技术栈，外部贡献更难；bus factor 虽远好于单人项目，但核心仍是一小队人马。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [LLM Wiki](llm-wiki.zh.md) | ✅ | 当由人来写、且应用必须成熟、不依赖模型时，选 Logseq；当簿记（互链、摘要、矛盾标注）应交由 agent 完成时，选 LLM Wiki。 | Logseq 提供久经考验的本地优先大纲工具、Datalog 查询和庞大插件社区，且零 token 成本；LLM Wiki 换来自动编译，但只是 5 个月大、单人维护的桌面应用。 |
| [SiYuan](siyuan.zh.md) | ✅ | 想要纯文件大纲工具加大型插件生态，选 Logseq；需要块级引用、Go 内核、Docker 自托管与移动端时，选 SiYuan。 | 两者都本地优先、都用 AGPL，但 SiYuan 是 open-core、有付费层级，而 Logseq 完全免费；Logseq 插件生态更大，SiYuan 的部署故事（服务端／移动端）更强。 |
| [Khoj](khoj.zh.md) | ✅ | 想在本地撰写并查询结构化笔记时，选 Logseq；想让 AI 跨设备从你的语料作答时，选 Khoj。 | Khoj 增加语义检索、网络搜索与多客户端访问，但每次查询重新检索，且需要 Python/Postgres 服务；Logseq 一切留在本地且结构化，但不替你综合。 |
| [Reor](reor.zh.md) | ✅ | 需要一个维护中、有社区规模的成熟应用时选 Logseq；Reor 只能当模式参考，因为它已归档。 | Reor 曾把本地 LLM／embedding 融入 markdown 编辑器，但 2025-05 停更；Logseq 没有内置 AI，却有一个活着的生态。 |
| Obsidian | 未收录 | 想要最大的插件生态和打磨精致的专有编辑器，选 Obsidian；想要在同样的本地文件模型上获得开源、块引用与 Datalog 查询，选 Logseq。 | Obsidian 是闭源免费软件，打磨更好、采用更广；Logseq 开源（AGPL）、以大纲为先，还能以编程方式查询图谱。 |
| Notion | 未收录 | 想要托管的一体化工作空间、且不介意云端时，选 Notion；当隐私、本地文件与版本控制不可让步时，选 Logseq。 | Notion 是托管 SaaS，有数据库与协作，但没有本地优先的所有权；Logseq 用打磨度与协作换来你拥有的本地 markdown。 |

## 技术栈

- **应用：** ClojureScript + Electron 桌面端（macOS／Windows／Linux），另有网页版 `app.logseq.com`
- **存储：** 磁盘上的 markdown／org 文件（基于文件的版本）；**SQLite** 图谱（beta DB 版本）
- **查询层：** DataScript（fork 的 Datalog 引擎），跑在内存图谱上
- **同步：** RTC（实时协作）处于 alpha；可选的托管 Logseq Sync
- **扩展性：** 插件 API + 插件市场；主题；自定义 CSS
- **构建工具：** Clojure CLI／Java、Node.js、`deps.edn`（前端基于 `shadow-cljs`）

## 依赖

- **桌面应用**——本地单人使用无需运行服务端或数据库；基于文件的版本除安装包外什么都不需要
- **一个本地文件夹**存放图谱（markdown／org 文件）；目录本身就是数据库
- **可选：** 用于多设备或协作的托管 Logseq Sync／RTC；只有从源码构建才需要 Node.js + Java
- **不要求模型 provider**——任何 LLM 用法都来自第三方插件及其自带 key

## 运维难度

**低。** 它是跑在纯文件之上的桌面应用：安装、选文件夹、完事。备份就是把图谱目录拷走（或用 git 提交），没有需要维持存活的服务。真正的坑是 beta DB 版本迁移（数据丢失风险、文档明确要求备份）与插件供应链信任，而不是日常运维。

## 健康度与可持续性

- **维护（2026-09）。** 强：44.9k star，nightly 构建发布到 2026-09-19，2026-07 有稳定版 2.0.1，提交近乎每日。未归档。[推断]
- **治理 / bus factor。** 组织所有，有数位长期核心维护者（头号贡献者约 1.18 万次提交，另有三位在 2000–3000 次区间）——远好于单人项目；但 ClojureScript 内核仍把小圈子外的专业度门槛抬得很高。[推断]
- **年龄与 Lindy。** 2020-05 创建、约 6 年持续活跃 ⇒ 对本地优先笔记应用是**强 Lindy** 信号；它已经挺过多次产品转向。[推断]
- **采用度与生态。** 社区庞大，有插件市场、活跃的论坛／Discord 与社区主题；是该细分领域默认的开源推荐之一。[未验证]
- **风险标记。** AGPL-3.0（未见 relicense 记录）。真正的标记是 **beta DB 版本的数据丢失警告**，以及项目注意力向 DB 图谱的迁移，使经典「基于文件」版本的长期方向不明。[推断]

## 存疑（未验证）

- **基于文件版本的状态**——最初的 markdown 文件版本是被功能冻结、还是与 DB 版本并行开发，README 未说明。[未验证]
- **托管同步的定价／限制**——Logseq Sync 与 RTC 被提及，但其定价、可用性与数据处理方式未在此确认。[未验证]
- **插件 AI 能力**——生态中存在第三方 LLM 插件；其范围、质量与数据处理未做审查。[未验证]
- **采用数字**——44.9k star、2.8k fork 是有日期的 API 快照，不是生产使用的独立证据。[未验证]
- **超大图谱下的 Datalog／查询性能**在本页所读来源中均未被刻画。[未验证]
