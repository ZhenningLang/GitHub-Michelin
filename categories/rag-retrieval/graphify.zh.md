---
name: graphify
slug: graphify
repo: https://github.com/safishamsi/graphify
category: rag-retrieval
tags: [knowledge-graph, code-intelligence, tree-sitter, graphrag, leiden, mcp, claude-code, skill]
language: Python
license: MIT
maturity: v0.8.49, active (2026-06)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T10:29:46Z
  default_branch: v8
  default_branch_sha: 36b5e5cb2907dd5ea4e96ec708772742ca98c1e9
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:57:33Z
  overall: B
  overall_score: 3.0
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 6.3
        qualifying_issues: 6
        band: relaxed_solo
        window_offset_days: 5
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: graphifyy
        dependent_repos_count: 0
        downloads_last_month: 788764
        graph_tier: E
        volume_tier: B
        cross_check_divergence: 2.05
        release_downloads: 7051
        release_assets: 158
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: D
      raw:
        repo_age_days: 172
        last_commit_age_days: 2
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 99
        top1_share: 0.637
        top3_share: 0.719
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# graphify

一个 Python CLI + MCP server（同时打包成 AI 编程助手 skill），把一整个目录的代码、schema、脚本、文档和媒体抽成一张可移植、可查询的知识图谱，让 agent 用“问图”代替“grep”。

![graphify — 健康度雷达](../../assets/health/graphify.zh.svg)

## 何时使用

你是一个 coding agent（或正在给 agent 接线的工程师），被丢进一个陌生的中大型仓库，而用户不断抛来跨切面的问题——“谁调用了这个 auth handler”“这张 SQL 表在哪里被写入”“哪个模块负责加载配置”。纯 `grep`/ripgrep 只给你一堆无结构的字符串命中：你得反复重读文件，人肉重建调用链和归属关系，白白烧掉上下文。graphify 用 tree-sitter（36 种语法）在本地抽出 AST 图，把非代码文件（文档、PDF、图片）交给 LLM 生成语义节点，再跑 Leiden 社区检测把结果聚成架构“社区”，最后产出可移植的 `graph.json`，外加交互式 `graph.html` 和 `GRAPH_REPORT.md`。之后你用 `graphify query "问题"`，或把它当 MCP server 接入，得到的是带 `EXTRACTED`/`INFERRED`/`AMBIGUOUS` 置信标签的结构化答案，而不是原始文件堆。

当图谱要跨越的不只是应用代码时，它尤其合适——graphify 有意把 SQL schema、基础设施（Terraform/HCL）、包清单、R/shell 脚本和文档一起喂进同一张图，于是 agent 能把应用代码 + 数据库 + 基础设施放在一起推理。因为它能作为 `/graphify` skill 装进很多 agent（Claude Code、Codex、Cursor、Gemini CLI、OpenCode、Aider 等），还自带 MCP 模式，它能直接嵌进现有 agent 循环，而不必你自己搭一套检索管线。

## 何时不用

- **你要的是持久化、多写入方的图数据库。** graphify 的原生存储是一次性的 `graph.json`（默认 512 MiB 上限）；它能把图 *导出* 成 Cypher 推到 Neo4j/FalkorDB，但自身不是事务型图数据库。如果你需要一个常驻、可查询、可并发更新的图后端，直接用 [FalkorDB](falkordb.zh.md) 或 Neo4j。
- **超大 monorepo / 超大图。** 交互式 HTML 可视化实际上限大约 5000 个节点 [未验证]；超过后只能用原始 JSON，而且在巨大目录树上抽取意味着对非代码文件发起大量 LLM 调用（成本 + 延迟）。
- **你需要确定性、纯离线的抽取。** 代码 AST 抽取是本地的，但文档/PDF/图片的语义节点需要 LLM 后端（Anthropic/OpenAI/Gemini/Ollama/Bedrock 等）——这意味着 API key、成本、非确定性，以及把文件内容发给模型（除非你跑本地 Ollama 后端）。
- **你想要稳定、冻结的 API。** 发版非常频繁（143+ 个 release，截至 2026-06 每周多次）；这是快速迭代、近乎单维护者规模的软件 [推断]——请 pin 版本，并预期命令/输出格式会变动。
- **纯文档 RAG（只有散文、没有代码）。** 如果你的语料是文章/PDF，想要段落级检索（而非代码/实体图），用面向文档结构或向量的方案如 [PageIndex](pageindex.zh.md) 更直接。
- **你只需要面向 code-review 的图。** 针对 PR/diff 范围的评审图，[code-review-graph](code-review-graph.zh.md) 面向那个更窄的工作流。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [FalkorDB](falkordb.zh.md) | ✅ | 需要持久化图数据库，而不是一次性仓库抽取时，选 FalkorDB。 | 真正的持久化图数据库（基于 Redis、Cypher）；graphify 可以往它 *推送*。需要常驻多查询图存储时用 FalkorDB，需要一次性抽取 + 面向 agent 查询时用 graphify。 |
| [PageIndex](pageindex.zh.md) | ✅ | 问题是长文档/PDF 的结构化检索，而不是代码/实体图抽取时，选 PageIndex。 | 面向长文档/PDF 的、基于推理的文档结构索引做 RAG；没有代码 AST 或调用图。是不同的问题：散文检索 vs 代码/实体图。 |
| [code-review-graph](code-review-graph.zh.md) | ✅ | 只需要窄域 PR/code-review 图工作流时，选 code-review-graph。 | 窄域的 PR/code-review 图工作流；graphify 是全仓库 + 多语言 + 多模态，范围更广。 |
| [Sourcegraph](sourcegraph.zh.md) / [SCIP](scip.zh.md) | ✅ | 需要由 language server 支撑的跨仓库精确代码智能时，选 Sourcegraph/SCIP。 | 工业级精确代码智能（跨仓库、language server）；基础设施更重，且不是 agent-skill 形态。graphify 更轻、由 LLM 增强、能直接嵌进 agent 循环。 |
| GitHub `code2graph` / 自写 tree-sitter 脚本 | 未收录 | 控制权比现成查询、聚类、可视化和 agent 集成更重要时，选自写 AST 图。 | 自己搭 AST 图；更可控，但查询、聚类、可视化和 agent 集成都得自己写。 |

## 技术栈

- **语言：** Python（仓库统计 100%，2026-06）。
- **解析：** tree-sitter，内置 36 种语法解析器（Python、TS/JS、Go、Rust、Java、C/C++、C#、Kotlin、Ruby、PHP、Swift、SQL、Terraform/HCL、Apex、CUDA 等）。
- **图分析：** Leiden 社区检测（可选 extra；标注仅 Python < 3.13）。
- **产物：** `graph.json`（完整图）、`graph.html`（交互可视化）、`GRAPH_REPORT.md`。
- **接口：** CLI（`graphify extract|query|export|install`）、MCP server（`python -m graphify.serve`，stdio/HTTP），以及装进多种 agent 的 `/graphify` skill。
- **LLM 后端（用于非代码语义节点）：** Anthropic、OpenAI、Gemini、DeepSeek/Moonshot、Azure OpenAI、Bedrock，或本地 Ollama。

## 依赖

- **运行时：** Python 3.10+ [未验证]；通过 `uv tool install graphifyy`（推荐）、`pipx install graphifyy` 或 `pip install graphifyy` 安装。注意 PyPI 包名是 **`graphifyy`**（双 y），而 CLI 命令是 `graphify`。
- **可选 extras（pip）：** `pdf`、`office`（DOCX/XLSX）、`video`（faster-whisper + yt-dlp）、`neo4j`、`falkordb`、`postgres`、`terraform`、`ollama`、`openai`/`gemini`/`anthropic`/`bedrock`/`azure`、`sql`、`mcp`、`leiden`、`chinese`（jieba）、`all`。
- **外部服务：** 给非代码文件建图需要 LLM 后端（云 API key 或本地 Ollama）；纯代码 AST 抽取是本地的。可选的下游图数据库：Neo4j、FalkorDB、PostgreSQL 内省。
- **安全提示：** v0.8.49 升级了 `starlette` 以修复 CVE-2026-48818 和 CVE-2026-54283（引自 release notes，见存疑）。

## 运维难度

**低到中。** 顺路径是一次 CLI 安装加 `graphify extract .` / `graphify query`，或一行 skill 安装进现有 agent——基础用法无需跑服务，产物是可移植的 JSON 文件。当你接入 LLM 后端（key 管理、按文件计的成本/延迟、把内容发给模型）、把 MCP server 当常驻进程跑、推送到 Neo4j/FalkorDB，或在大仓库上撞到 HTML/节点和 512 MiB 图上限时，难度升到**中**。极高的发版节奏也意味着 pin 版本是这里运维卫生的一部分。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 6.3 小时，基于 6 个 qualifying issues/PRs。
- **维护——活跃。** 最后一次 push 在 2026-06，未归档，发版节奏极高（143+ 个 release，截至 2026-06 每周多次）[未验证]。这里的担忧不是活跃度，而是 churn：标志“还活着”的高速度，也意味着 CLI 表面和输出 schema 会在 minor 版本间变动，所以要 pin 版本。
- **治理 / bus factor——单维护者规模，是个真实的标志。** 仓库为 **User** 所有（`safishamsi/graphify`），约 73k star[未验证]——star 与 bus-factor 的比值很高。没有基金会或厂商托底路线图；单个人的注意力就是依赖。`[推断]` 如果这位维护者停手，项目就会停滞。
- **年龄与 Lindy——年轻、未经证明（创建于 2026-04，截至 2026-06 约 2 个月）。** 太新，还没挣到 Lindy 先验：一个仅几个月、单维护者的仓库上堆着大量 star，是热度而非履历。把它当作有潜力但未定型，而非可长期下注的安全选择。
- **风险标志——快速 churn + LLM 依赖 + CVE 卫生。** 频繁发版意味着破坏性变更；非代码抽取会把文件内容发给 LLM 后端；v0.8.49 升级了 `starlette` 以修复 CVE-2026-48818/54283（引自 release notes，未独立确认）[未验证]。MIT 许可证——未观察到 relicense/open-core 标志。

## 存疑（未验证）

- [未验证] 最新 release v0.8.49 发布于 2026-06-25，约 73.1k star（截至 2026-06-28，经 GitHub API）——这个计数经 API 核实，但其采用度含义未经核实，且 GitHub star 不可靠、对时间敏感；仅供参考。
- [未验证] 最低 Python 3.10 以及“36 种 tree-sitter 语法”/受支持文件类型清单来自 README；依赖某具体语言/格式前请对照已安装版本核实。
- [未验证] ~5000 节点的 HTML 实际上限和 512 MiB 默认图上限是文档默认值；真实上限取决于机器内存和图密度。
- [未验证] 安全 CVE 修复（starlette）引自 release notes；未对照漏洞公告库独立确认。
- [推断] “143+ 个 release、每周多次”暗示这是快速迭代、小团队规模的软件，minor 版本之间 CLI 表面和输出 schema 可能变动。
- [推断] graphify 更适合归类为 `tool`（CLI + MCP server）而非纯 skill-pack，因为它有真实的技术栈、依赖和运维面，不只是一个 prompt 包。
