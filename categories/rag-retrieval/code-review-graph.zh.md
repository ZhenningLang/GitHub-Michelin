---
name: code-review-graph
slug: code-review-graph
repo: https://github.com/tirth8205/code-review-graph
category: rag-retrieval
tags: [code-intelligence, knowledge-graph, mcp, tree-sitter, context-reduction, blast-radius, graphrag]
language: Python
license: MIT
maturity: v2.3.6, active, beta (2026-06)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-14T17:20:41Z
  default_branch: main
  default_branch_sha: b72413cbd34a4ac08cc60dcdd42df1d02f3fc77d
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:56:56Z
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
        last_commit_age_days: 4
        active_weeks_13: 11
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 403.7
        qualifying_issues: 22
        band: relaxed_solo
        window_offset_days: 13
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: code-review-graph
        dependent_repos_count: 0
        downloads_last_month: 254286
        graph_tier: E
        volume_tier: B
        cross_check_divergence: null
        release_downloads: 27
        release_assets: 3
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 208
        last_commit_age_days: 4
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 98
        top1_share: 0.586
        top3_share: 0.649
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# code-review-graph

一张本地优先的代码智能图：Tree-sitter 把仓库解析成由函数/类/边构成的 SQLite 图，再通过 MCP 把最小的 blast-radius 上下文喂给你的 AI 编码工具，让它只读要紧的部分。

![code-review-graph — 健康度雷达](../../assets/health/code-review-graph.zh.svg)

## 何时使用

你是一名开发者，在一个中到大型仓库里和 AI 编码助手（Claude Code、Cursor、Codex 等）结对，而你总是眼睁睁看着它为了回答“这个改动影响什么？”或“这里 auth 怎么走？”而反复重读半棵代码树烧上下文。每个评审任务都让 token 账单膨胀，agent 却仍然漏掉两跳之外的某个调用方。你想让 agent 读*那对的约 15 个文件*，而不是在 28000 个文件里盲目 grep。你装上 code-review-graph，跑一次 `build`（500 文件约 10 秒），从此 agent 调用 `get_impact_radius`、`get_review_context` 这类 MCP 工具：图会追踪某个变更文件的每个调用方、依赖方和测试，回交一片紧凑的结构切片，而不是原始源码。在它自己基准里的那些仓库上，它自报每问题 token 缩减中位数约 82 倍，且文件保存时增量更新能在 2 秒内对一个 2900 文件的项目重建索引。

当你想在 *CI 里做风险评分的 PR 评审、且不把代码发往任何地方*时，它同样合适：同一套分析作为复合 GitHub Action 运行，完全在你的 runner 上构建并查询图，贴出带风险评分函数和测试缺口的 sticky 评论，并能通过 `fail-on-risk` 卡合并。如果你住在 monorepo 里、想要一个后台守护进程（`crg-daemon`）持续保持多个仓库的图新鲜，这也开箱自带。

## 何时不用

- **你想要一个通用图数据库，而非代码上下文层。** 这是一条固定的代码智能流水线（AST → SQLite → blast-radius），不是可让你在其上构建应用的可查询图存储。要真正的属性/Cypher 图数据库，用 [FalkorDB](falkordb.zh.md)。
- **琐碎 / 单文件改动。** 维护者自己的限制说明指出，对小改动，图上下文可能*超过*直接读文件——结构元数据是开销，直到改动跨多个文件才赚回来。
- **你今天就需要可信的 recall 数字。** 标语式的 "recall 1.0" 被明确指为**循环**——ground truth 来自预测器所走的同一张图。诚实的 co-change 模式被承认“明显更低”且**尚未发布**。[推断] 把影响准确率当作方向性参考，而非保证。
- **超出 Python 的跨文件调用解析。** 流程检测文档记为约 33% recall，且只在 Python 框架模式（FastAPI/httpx）上可靠；JS/Go 流程与搜索排序（MRR 0.35）是明述的弱点。
- **巴士因子 / 成熟度风险。** 这是一个单一维护者、Beta 分级、v2.3.x 的项目（首次 commit 2026-02）。把 GitHub Action pin 到某个 tag、以及快速的发版节奏是缓解手段，但对其 `.code-review-graph/` SQLite 格式和 MCP 工具面的锁定是真实的。
- **你需要对散文做纯文档/段落 RAG。** 它索引的是代码结构而非任意文档——要层级文档检索看 [PageIndex](pageindex.zh.md)。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [FalkorDB](falkordb.zh.md) | ✅ | 需要真正基于 Redis、带 Cypher 和向量搜索的属性图数据库时，选 FalkorDB。 | 一个真正基于 Redis 的属性图数据库，带 Cypher + 向量搜索，你直接查询它；是*底座*而非开箱即用的代码上下文工具。code-review-graph 给你整条 AST→图→MCP 流水线，但建在它自己固定的 SQLite 存储上。 |
| [graphify](graphify.zh.md) | ✅ | 需要另一个面向 agent 检索的代码库建图工具时，选 graphify。 | 同样把代码库变成图供 agent 检索；意图有重叠。code-review-graph 重压在 blast-radius/评审 + 一个 MCP server、宽语言覆盖和一个 CI Action 上。请直接对比 scope/成熟度。 |
| [PageIndex](pageindex.zh.md) | ✅ | 需要面向文档的推理式层级检索时，选 PageIndex。 | 面向*文档*（PDF、长文本）的、基于推理的层级检索，无向量库；输入领域不同——散文而非源码 AST。 |
| [Sourcegraph](sourcegraph.zh.md) / [SCIP](scip.zh.md) | ✅ | 需要成熟、规模化的多仓库代码智能时，选 Sourcegraph 或 SCIP。 | 成熟、规模化的多仓库代码智能与索引；基础设施更重，不是面向 agent token 预算的本地单二进制 MCP 上下文压缩器。 |
| Serena (MCP) | 未收录 | 需要面向 agent 的 LSP 语义代码 MCP server 时，选 Serena。 | 面向 agent 的、基于 LSP 的语义代码 MCP server；以符号/LSP 驱动，而非带 blast-radius + 社区/风险分析的持久化 Tree-sitter 图。 |
| GraphRAG (Microsoft) | 未收录 | 需要 LLM 构建的实体/社区图来做文档 RAG 时，选 GraphRAG。 | LLM 构建的实体/社区图，用于文档 RAG；面向非结构化语料，而非确定性的 AST 派生代码图。 |

## 技术栈

- **语言：** Python（≥ 3.10，测试至 3.13）。
- **解析：** Tree-sitter，经 `tree-sitter` + `tree-sitter-language-pack`；宽语言覆盖（Python、JS/TS/TSX、Go、Rust、Java、C/C++、C#、Ruby、Kotlin、Swift、PHP、Scala、Solidity、Dart 等）加 Jupyter/Databricks `.ipynb`。自定义语言可经 `.code-review-graph/languages.toml` 添加，无需 fork。
- **图/存储：** `.code-review-graph/` 下的本地 SQLite，带 FTS5 全文搜索；`networkx` 跑图算法；社区检测经 Leiden（可选 `igraph`）。
- **服务：** MCP server（`mcp` + `fastmcp`）暴露约 30 个工具和 5 个 prompt 模板；CLI（`code-review-graph`）与守护进程（`crg-daemon`）。
- **可选：** 向量 embedding，经 sentence-transformers / Google Gemini / MiniMax / 任意 OpenAI 兼容端点；Python 调用解析增强经 Jedi;D3.js 交互可视化；导出到 GraphML / Neo4j Cypher / Obsidian / SVG。
- **CI:** 复合 GitHub Action，做风险评分的 PR 评论。

## 依赖

- **运行时：** Python ≥ 3.10。经 `pip install code-review-graph`（或 `pipx`/`uvx`）安装。
- **必需 Python 依赖（v2.3.6）:** `mcp` ≥ 1.0、`fastmcp` ≥ 3.2.4(<4)、`tree-sitter` ≥ 0.23、`tree-sitter-language-pack` ≥ 0.3、`networkx` ≥ 3.2、`watchdog` ≥ 4.0（Python < 3.11 加 `tomli`）。
- **核心存储：** 本地 SQLite 文件——核心图**不需要外部数据库或云服务**。
- **可选分组：** `[embeddings]`(sentence-transformers、numpy)、`[google-embeddings]`、`[communities]`(igraph)、`[enrichment]`(jedi)、`[eval]`(matplotlib)、`[wiki]`(ollama)，或 `[all]`。
- **外部服务仅 opt-in:** 云端 embedding 需要显式出网确认；CI Action 完全在你自己的 runner 上运行，不外发源码。

## 运维难度

**低。** 单条 `pip`/`pipx`/`uvx` 安装，加一条 `install` 命令自动探测受支持的 AI 工具并写入其 MCP 配置；`build` 一次，之后 hooks/watch/daemon 保持新鲜。没有数据库要跑，没有云账号，状态住在本地 SQLite 文件里。升到**低到中**的场景：开启语义 embedding（模型下载、可选云出网和 API key）、跑多仓库守护进程、或把 GitHub Action 用 `fail-on-risk` 接成合并门。可选依赖矩阵（embeddings/communities/enrichment）是版本摩擦最可能冒头的地方。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 134.0 小时，基于 33 个 qualifying issues/PRs。
- **维护（2026-06）：** 最后 push 在 2026-06-14，最新 release v2.3.6 于 2026-06-10——**活跃**，发版节奏很快。[推断] 节奏是优点；但对这么年轻的项目，同样的速度意味着不稳定的 API/格式面。
- **治理 / 巴士因子：** **单一维护者、`User` 所有**（`tirth8205/code-review-graph`），Beta 分级。这是一个真实的**巴士因子标记**：一个仅几个月前创建的个人仓库就有约 18k star，是热度远远跑赢机构背书——路线图背后没有团队或基金会。[推断]
- **年龄与 Lindy（创建于 2026-02，约 0 年）：** **年轻且被热捧——Lindy 先验失败。** 没有记录、未证明多年存活；star 数说明的是关注度而非持久度。把延续性当作未被验证，并把 GitHub Action pin 到某个 tag。[推断]
- **采用 / 生态：** 宽语言覆盖与 MCP + CI 面拉动了 star，但对其 `.code-review-graph/` SQLite 格式与 MCP 工具面的锁定是真实的，而自报基准（约 82 倍那些数字、"recall 1.0"）是循环/未复现的。[未验证]
- **风险标记：** MIT（无重新许可风险）；主导风险是**废弃 / 巴士因子**（单一维护者、约 0 年）与格式锁定，而非许可。[推断]

## 存疑（未验证）

- [未验证] 最新 release v2.3.6 发布于 2026-06-10；仓库创建于 2026-02-26；最后 push 2026-06-14（据 `gh` 元数据 2026-06-26）。版本节奏很快；pin 前请重新核实。
- [未验证] star 数约 18.9k（据 `gh` 2026-06-26）——GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 所有 token 缩减数字（中位数约 82 倍、最大 528 倍、“<2 秒”重建索引、build/延迟表）都是项目自己在 6 个自选仓库上的基准；本页未独立复现。
- [推断] 影响 "recall 1.0" 被自述为循环（图派生的 ground truth）；诚实的 co-change 准确率未发布，故真实世界的影响 precision/recall 未知。
- [未验证] 所述语言覆盖、约 30 个 MCP 工具、受支持编辑器平台均来自 README；确切工作集可能随版本变动。
- [未验证] 许可为 MIT（据 `gh licenseInfo` 与 `pyproject.toml`）；单一维护者（"Tirth"），打包 classifier 标注为 Beta 开发状态。
