---
name: Memori
slug: memori
repo: https://github.com/MemoriLabs/Memori
category: agent-memory
tags: [agent-memory, persistent-memory, llm-agnostic, mcp, state-management, entity-extraction]
language: Python
license: Apache-2.0
maturity: v3.3.6, active (2026-06)
last_verified: 2026-06-26
type: library
upstream:
  pushed_at: 2026-06-15T23:18:56Z
  default_branch: main
  default_branch_sha: 56600c525ba3046354c17a7663dca06a813a0bb5
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:40:08Z
  overall: B
  overall_score: 2.8
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 5
        active_weeks_13: 4
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 122.2
        qualifying_issues: 5
        band: default
        window_offset_days: 7
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: memori
        dependent_repos_count: 1
        downloads_last_month: 29750
        graph_tier: D
        volume_tier: C
        cross_check_divergence: null
        release_downloads: 42
        release_assets: 4
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 425
        last_commit_age_days: 5
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 40
        top1_share: 0.336
        top3_share: 0.632
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Memori

一个 LLM 无关的记忆层，把 agent 的执行与对话转成结构化、持久化的状态——通过包裹你现有的 LLM 客户端来捕获，后台自动召回，你的热路径里不需要写 `search()` 调用。

![memori — 健康度雷达](../../assets/health/memori.zh.svg)

## 何时使用

你在 OpenAI 或 Anthropic 之上搭一个生产级客服 agent，而你一直在重复解决同一个问题：模型在会话之间什么都不记得，每次对话都从零开始。你不想手搓向量库、写召回胶水、设计记忆 schema——你想要的是 agent 能像人类同事那样*记住这个用户*（他的实体、偏好、过去的决策）。Memori 坐在你的代码和 LLM 之间：你注册现有客户端（`Memori().llm.register(client)`），给某次调用打上 `entity_id` 和 `process_id`，对话就会在后台被自动持久化并召回——于是下一次会话里，相关的 facts、people、preferences、rules 已经在 context 里了，你不用自己写召回管线。

当你想要的记忆是以*agent 做了什么*为锚、而不只是聊天记录时，它很合适——augmentation 层在后台按 entity / process / session 三个层级抽取 attributes、events、facts、people、preferences、relationships、rules、skills，并号称对热路径“零延迟”。因为它定位为 LLM、datastore、framework 三无关（Anthropic、OpenAI、Bedrock、DeepSeek、Gemini、Grok;Agno、LangChain、Pydantic AI），还自带一个 MCP server，你也可以零 SDK 代码地把它接进 Claude Code、Cursor、Codex 或 Warp。

## 何时不用

- **你需要一个完全离线、自包含的库。** 默认 SDK 路径会调用 **Memori Cloud**，并需要 `MEMORI_API_KEY`（在 app.memorilabs.ai 注册）。自托管通过 **BYODB**（自带数据库）实现，但文档里明确点名的 datastore 只有 **TiDB**——README 没写 Postgres/SQLite 支持。[未验证] 如果你要求纯本地运行，这是采用前需要核实的真实约束。
- **你在规避厂商锁定 / SaaS 依赖。** "Advanced Augmentation"（实体/事实/关系抽取，正是这个产品的主要卖点）被描述为无账号也可用但**有速率限制**，完整能力在付费 cloud 账号背后。开源代码和商业 cloud 是交织的；最有价值的行为在脱离 cloud 后可能降级。
- **你想要久经考验、稳定的 API。** 它还年轻（v3.3.6,2026 年发版很快）;API 面以及 cloud/BYODB 的切分仍在变。请 pin 版本，并预期会有 churn。
- **你只需要一个薄薄的向量召回 RAG。** 如果你只想“切块嵌入、top-k 召回”，一个普通向量库或 [Mem0](mem0.zh.md) 比 Memori 的结构化状态 + augmentation 模型更轻。
- **你需要透明、可审计的召回。** 记忆是通过对被包裹客户端的后台自动拦截注入的——quickstart 里没有显式的 `search()` 调用。如果你需要看清并控制每个 prompt 里到底拉进了什么，这种隐式模型会跟你拧着来。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Mem0](mem0.zh.md) | ✅ | 显式 add/search API 和更广的自托管路径更重要时，选 Mem0。 | 被引用最多的 agent 记忆层；在向量库之上提供 add/search API，自托管能力广。Memori 偏向自动客户端拦截 + 结构化 entity/process 状态加一个有主张的 cloud，而 Mem0 召回更显式、datastore 更灵活。 |
| [claude-subconscious](claude-subconscious.zh.md) | ✅ | 明确想要 Claude/Letta 血统的后台记忆实验时，选 claude-subconscious。 | 一个 Claude 专属的后台记忆实验（Letta 血统）；范围比 Memori 的多 provider、多 framework 基础设施窄。 |
| [Letta (MemGPT)](letta.zh.md) | ✅ | 需要把记忆管理 OS 放进有状态 agent runtime 时，选 Letta。 | 带记忆管理 OS 的 agent runtime（分层 context、自编辑记忆）；是更重的有状态 agent 服务，不是即插即用的客户端包裹器。 |
| [Zep](zep.zh.md) | ✅ | 时序知识图谱记忆是主要架构下注时，选 Zep。 | 基于时序知识图谱的记忆服务，自托管/OSS 核心很强；结构化记忆的野心相当，但模型是图优先的。 |
| [LangMem (LangChain)](langmem.zh.md) | ✅ | 记忆工具需要绑定在 LangGraph/LangChain 栈内时，选 LangMem。 | 绑在 LangGraph/LangChain 栈上的记忆工具；独立性不如 Memori 的 framework-无关定位。 |
| 普通向量库（pgvector / Chroma） | 未收录 | 自己掌控 schema 和召回比 augmentation 功能更重要时，选普通向量库。 | schema 和召回都你自己掌控；没有 augmentation、没有 entity 模型、没有 cloud——掌控最大，接线也最多。 |

## 技术栈

- **语言：** Python（约 63%），配 TypeScript SDK（约 18%）;`pip install memori` / `npm install @memorilabs/memori`。
- **记忆模型：** 按 **entity / process / session** 三层级跟踪；后台 "Advanced Augmentation" 抽取 attributes、events、facts、people、preferences、relationships、rules、skills。
- **集成：** 包裹现有 LLM 客户端（OpenAI Chat Completions & Responses API、Anthropic、Bedrock、DeepSeek、Gemini、Grok）;Agno、LangChain、Pydantic AI 框架适配；自带 **MCP server**，可零 SDK 接入 Claude Code / Cursor / Codex / Warp / Antigravity。
- **datastore:** Memori Cloud（托管，默认）或 **BYODB** 自托管——文档明确点名 TiDB（TiDB Zero 供给一次性开发库）。[未验证] README 未记录其他后端。

## 依赖

- **运行时：** Python（SDK）和/或 Node(TS SDK)。默认 cloud 路径需要 `MEMORI_API_KEY`。
- **外部服务：** 默认 Memori Cloud（在 app.memorilabs.ai 建账号）。自托管：一个 BYODB 数据库（文档为 TiDB）。
- **LLM provider:** 至少一个受支持的 provider 客户端（OpenAI、Anthropic 等）——Memori 是你现有 LLM 调用之上的一层，本身不是 LLM。
- **可选：** 支持 MCP 的客户端（Claude Code、Cursor、Codex、Warp）以走零 SDK 的 MCP 路径。

## 运维难度

**cloud 路径低，自托管中到高。** 托管 cloud 的 quickstart 是“零配置”：设个 API key、注册客户端、完事，运维极少。一旦你想避开 SaaS 依赖，就进入 BYODB 领域：你要自己供给并运维数据库（文档为 TiDB），还要承担那些被 cloud 门控或在无账号时被限速的 augmentation 功能。由于开源代码和商业 cloud 是耦合的，真正的运维问题不是“我能不能把容器跑起来”，而是“离开 cloud 后哪些能力还活着”——在投入前请留出时间为你的用例验证这一点。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 14.8 小时，基于 14 个 qualifying issues/PRs。
- **维护（2026-06）：** 活跃且迭代快——最新 release v3.3.6（2026-05），最后 push 于 2026-06，未归档，open issue 很少（约 20）。发版很快，既表明有活力，也意味着接口面不稳定。
- **治理 / bus factor：** 归 `MemoriLabs` 组织所有（即商业 Memori Cloud 背后的公司）。这是单厂商、open-core 的治理——路线图跟着 SaaS 走，不是基金会或社区。`[推断]`
- **年龄与 Lindy 判断：** 约 1 岁（创建于 2025-07）——在 Lindy 维度上年轻且未经验证。没有长期记录可依靠；把存续性当作未决问题，并锁定版本。
- **风险旗标：** open-core / SaaS 耦合是头号风险——最有价值的行为（"Advanced Augmentation"）在无账号时受速率限制，文档里唯一记录的自托管后端是 TiDB，所以离开 cloud 可能让能力降级。在押注纯本地之前先验证 BYODB 路径。

## 存疑（未验证）

- [未验证] 仓库 `LICENSE` 文件为 Apache-2.0（标准文本，无 Commons Clause）；注意 `gh repo view` 报 `license: other`，很可能是附录版权行造成的识别误差——若 license 重要，请对照线上 `LICENSE` 核实。
- [未验证] 最新 release v3.3.6 发布于 2026-05-28;push 于 2026-06-15;star 约 15.4k（截至 2026-06）——GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] BYODB 自托管：README 只点名了 TiDB;Postgres/SQLite 或其他后端未确认，可能不支持。
- [推断] "Advanced Augmentation"（实体/事实/关系抽取）看起来跑在 Memori Cloud，无付费账号时受速率限制；它在完全自托管下能工作到什么程度，README 未确认。
- [推断] 默认 SDK 路径调用 Memori Cloud 且需要 `MEMORI_API_KEY`；完全本地部署可能需要 quickstart 未详述的非默认配置。
- [推断] 后台 augmentation“零延迟”是项目自己的表述；真实影响取决于负载，且未经独立测量。
