---
name: Langflow
slug: langflow
repo: https://github.com/langflow-ai/langflow
category: workflow-builders
tags: [agent-workflow, visual-builder, llm, rag, mcp, python]
language: Python
license: MIT
maturity: v1.x, active, 150k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-04T03:07:49Z
  default_branch: main
  default_branch_sha: 315cc41b43c446bfb0e63d420ca55021f6f8987e
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:37:34Z
  overall: B
  overall_score: 3.33
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
        last_commit_age_days: 7
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 56.6
        qualifying_issues: 33
        band: default
        window_offset_days: 1
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: langflow
        dependent_repos_count: 11
        downloads_last_month: 41135
        graph_tier: D
        volume_tier: C
        cross_check_divergence: null
        homebrew_installs_90d: 87
        homebrew_tier: D
        release_downloads: 207598
        release_assets: 221
        release_tier: C
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1322
        last_commit_age_days: 7
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 138
        top1_share: 0.286
        top3_share: 0.449
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

# Langflow

一款可视化平台，用于构建和部署 AI 驱动的智能体与工作流，支持拖拽式界面、内置 API 和 MCP 服务器，可在组件级别用 Python 自定义，并支持所有主流大模型与向量数据库。

![Langflow — 健康度雷达](../../../assets/health/langflow.zh.svg)

## 何时使用

你是一名开发者或 AI 工程师，需要原型化和部署 LLM 驱动的工作流——RAG 管线、多智能体编排或聊天机器人后端——又不想为每个大模型提供商和向量数据库写样板集成代码。你想要一个可视化画布，把节点（LLM、检索器、工具、记忆）连接成流，交互式测试，然后将其暴露为 API 端点或 MCP 工具。你需要支持主流模型（OpenAI、Anthropic、本地模型）、向量库（Pinecone、Weaviate、Chroma），并在可视化编辑器不够用时能下沉到 Python。选择 Langflow 而不是 LangChain，因为 Langflow 既提供可视化画布又提供源码访问，无需手写链式代码；选择 Langflow 而不是 Dify，因为 Langflow 是完全 MIT 许可，更开放于社区驱动的定制。决定取舍：可视化构建器用于快速原型，加上可用 Python 自由定制任何组件的自由度。

## 何时不用

- 如果你排斥可视化编辑器，偏爱纯代码，请用 LangChain 或 CrewAI 而不用 Langflow，因为可视化层对代码优先团队会增加摩擦，而非价值。
- 如果你只需要简单的一次性脚本或单次 API 调用，请用直接 Python 脚本或 HTTP 客户端而不用 Langflow，因为起 Langflow 实例对 trivial 任务来说是杀鸡用牛刀。
- 如果你的团队要求严格的基于 git 的工作流版本控制，需要干净的 diff 和 PR 审查，请用 LangChain 或 Prefect 而不用 Langflow，因为保存为 JSON 的可视化流比代码更难做 diff、审查和合并。
- 如果你需要完整的生产 MLOps 平台，内置监控、tracing 和 A/B 测试，请用 MLflow 或 Weights & Biases 而不用 Langflow，因为 Langflow 不能替代完整的可观测性栈。
- 如果你需要企业级多租户、细粒度 RBAC 和审计追踪，请用 Dify 或商业平台而不用 Langflow，因为自托管 Langflow 只有基础认证，租户隔离不是其首要焦点。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [LangChain](langchain.zh.md) | ✅ | 代码优先的自定义 agent 开发比可视化画布更合适时，选 LangChain。 | LangChain 是编码库；Langflow 是在类似概念之上的可视化层。代码优先团队偏爱 LangChain；可视化优先团队偏爱 Langflow。 |
| [n8n](../../workflow-orchestration/n8n.zh.md) | ✅ | 广泛工作流自动化和集成比 LLM 原生流程编排更重要时，选 n8n。 | n8n 是通用自动化加 AI 能力；Langflow 专为 LLM/智能体工作流设计，模型和向量库集成更深。 |
| [Dify](dify.zh.md) | ✅ | 生产平台能力、RBAC 和云选项比 Langflow 的 MIT/社区定制更重要时，选 Dify。 | 类似的可视化构建器，企业 RBAC 和云服务更强；Langflow 是完全 MIT 许可，更开放于社区驱动的定制。 |
| [AutoGPT](autogpt.zh.md) | ✅ | 目标是自主、持续的任务执行时，选 AutoGPT。 | AutoGPT 面向自主任务执行；Langflow 面向组合式、可交互、带人工监督的工作流。 |
| [CrewAI](../agent-runtimes/agent-sdks/crewai.zh.md) | ✅ | 核心抽象是代码优先、基于角色的多 agent 团队时，选 CrewAI。 | CrewAI 是代码优先、基于角色的多智能体编排；Langflow 是可视化流式编排。 |
| [Flowise](flowise.zh.md) | ✅ | 想要相近的可视化 LLM 构建器，且其生态更适配你的栈时，选 Flowise。 | 功能集非常相似；截至 2026-07，Langflow 社区更大、GitHub 更活跃。 |

## 技术栈

- **Python**——后端运行时与组件逻辑
- **React / React Flow**——拖拽式画布的可视化前端
- **FastAPI**——将工作流暴露为 REST 端点的 API 层
- **SQLAlchemy**——持久化的数据库抽象层
- **LangChain**——底层 LLM 集成与链式原语（组件包装 LangChain 概念）

## 依赖

- **Python 3.10+**——后端运行时
- **数据库**——本地开发用 SQLite，生产持久化推荐 PostgreSQL
- **LLM API key**——OpenAI、Anthropic 或本地模型端点（Ollama、vLLM 等）
- **可选向量数据库**——Chroma、Pinecone、Weaviate 或 Qdrant，用于 RAG 工作流
- **Node.js**——修改 UI 时用于构建前端

## 运维难度

**中等**。本地开发简单（`pip install langflow` 或 Docker）。生产部署需要管理 Python 后端、用于流持久化的数据库，以及可能的向量数据库。可视化流本身需要版本控制纪律——保存为 JSON 的流可以提交到 git，但做 diff 和代码审查很别扭。主要的持续负担是保持 Langflow 版本、LangChain 依赖和模型提供商 API 的同步。

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 7 天。
- **响应速度**：Grade B——中位首次响应时间 56.6 小时，基于 33 个 qualifying issues/PRs。
- **采用广度**：Grade C——pypi.org 上月下载量 41,135（包名：langflow）。
- **长青度**：Grade B——仓库已创建 1322 天。
- **治理集中度**：Grade A——前三贡献者占比 44.9%（过去 12 个月内 138 位活跃维护者）。
- **许可风险**：Grade A——MIT 许可证。
## 存疑（未验证）

- [未验证] `langflow-ai` 与任何商业实体或资金来源之间的确切关系未公开记录。
- [未验证] 对 LangChain 的依赖意味着 Langflow 继承 LangChain 的 API 稳定性和版本决策；上游破坏性变更可能传导。
- [推断] 可视化流的 diff/merge 相比代码仍然别扭；在生产中使用 Langflow 的团队应建立 JSON 流审查纪律。
- [未验证] MCP 服务器和内置 API 功能相对较新；它们在负载下的生产稳定性和性能特征未经独立验证。
- [未验证] 某些高级功能或集成可能需要特定依赖版本，可能与项目环境中其他包冲突。
