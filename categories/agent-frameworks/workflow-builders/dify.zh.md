---
name: Dify
slug: dify
repo: https://github.com/langgenius/dify
category: workflow-builders
tags: [agentic-workflow, low-code, rag, mcp, orchestration, nextjs]
language: TypeScript
license: NOASSERTION
maturity: v0.x, active, 147k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-04T10:43:04Z
  default_branch: main
  default_branch_sha: 2e1ab194b718dea0ec364d3f1ae94fa0dd45e9e3
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:37:07Z
  overall: B
  overall_score: 3.2
  scored_axes: 5
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
      grade: A
      raw:
        median_ttfr_hours: 1.1
        qualifying_issues: 15
        band: default
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: dify-client
        dependent_repos_count: 0
        downloads_last_month: 10843
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
        release_downloads: 17383
        release_assets: 30
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1259
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 244
        top1_share: 0.167
        top3_share: 0.324
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Dify

一款用于构建和部署 agentic 工作流的低代码可视化编排平台，内置 RAG、MCP 支持，并可连接多种大模型提供商。

![Dify — 健康度雷达](../../../assets/health/dify.zh.svg)

## 何时使用

你是一支产品团队，需要快速交付 AI 驱动的工作流，又不想从零写起。你想要一个可视化构建器，让非工程师也能设计 agent 流程，而开发者仍能在需要时写代码。你需要内置 RAG 来做文档问答，需要多步工作流编排，还需要通过一个平台连接多种大模型提供商（OpenAI、Anthropic、Gemini、本地模型）。你自托管 Dify，在一个地方迭代聊天机器人、AI 智能体和自动化流水线。选择 Dify 而不是 Langflow，因为 Dify 有更成熟的部署功能、内置 RBAC 和更强的企业导向；选择 Dify 而不是 n8n，因为 Dify 专为 LLM 和智能体工作流打造，而非通用业务自动化。决定取舍：生产就绪的 AI 平台功能，加上低代码的易用性。

## 何时不用

- 如果你需要轻量或一次性脚本，请用 LangChain 或直接 API 调用而不用 Dify，因为 Dify 是完整平台，用它做简单任务属于杀鸡用牛刀。
- 如果你的团队是纯代码优先且排斥可视化工具，请用 LangChain 或 CrewAI 而不用 Dify，因为低代码层对喜欢用 Python 手写每个 agent 循环的开发者来说会成为摩擦。
- 如果你需要严格的开源许可清晰度以进行商业再分发，请用 Langflow 或完全 MIT 许可的项目而不用 Dify，因为 GitHub 元数据将 Dify 许可列为 `NOASSERTION`，商用前必须核实实际条款。
- 如果你只有小资源部署环境，请用更轻量的 Python 脚本或 LangChain 而不用 Dify，因为自托管 Dify 需要 Docker、PostgreSQL、Redis 和向量存储，小 VPS 会吃力。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [LangChain](langchain.zh.md) | ✅ | 需要代码优先的 agent/RAG 库，而不是可视化部署平台时，选 LangChain。 | LangChain 是代码优先的框架；Dify 是带内置 RAG 与部署能力的可视化平台。 |
| [n8n](../../workflow-orchestration/n8n.zh.md) | ✅ | 工作流是更广泛的业务自动化，只顺带使用 AI 节点时，选 n8n。 | n8n 面向更广泛的业务流程自动化；Dify 专为 LLM 和 agent 工作流打造。 |
| [LangFlow](langflow.zh.md) | ✅ | 偏好 Python-first、MIT 许可的可视化构建器，而不是更完整的平台/RBAC 栈时，选 LangFlow。 | 两者都走可视化路线；LangFlow 偏 Python 优先且 MIT 许可，Dify 的部署功能和 RBAC 更成熟。 |
| [AutoGPT](autogpt.zh.md) | ✅ | 目标是完全自主、长时间运行的 agent，而不是人工设计的工作流时，选 AutoGPT。 | AutoGPT 面向完全自主的长期运行 agent；Dify 聚焦有人参与设计的编排式工作流。 |
| [CrewAI](../agent-runtimes/agent-sdks/crewai.zh.md) / LlamaIndex | 部分已收录 | 想要多 agent 团队或 RAG-first 管道，且不需要 Dify 的整合平台时，选这些专项框架。 | CrewAI 偏重多 agent 团队协作；LlamaIndex 偏重 RAG。Dify 把两者整合到一个平台。 |

## 技术栈

- **TypeScript / Next.js**——前端与 API 层
- **Python**——后端工作流引擎与 AI 逻辑
- **PostgreSQL**——主元数据与配置存储
- **Redis**——缓存与消息代理
- **Docker**——容器化部署

## 依赖

- Docker 与 Docker Compose（推荐部署路径）
- PostgreSQL 数据库
- Redis 实例
- 向量数据库（Weaviate、Qdrant 或 Milvus）用于 RAG
- LLM 提供商 API key 或本地模型端点

## 运维难度

**中等**。Docker Compose 是标准路径，但生产运行 Dify 需要管理数据库、Redis、向量存储和 LLM 凭证。升级、PostgreSQL 备份以及 worker 层扩容都会增加运维面。使用云端托管版可省去这些，但会转为 SaaS 依赖。

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 0 天。
- **响应速度**：Grade A——中位首次响应时间 1.1 小时，基于 15 个 qualifying issues/PRs。
- **采用广度**：Grade D——pypi.org 上月下载量 10,843（包名：dify-client）。
- **长青度**：Grade B——仓库已创建 1259 天。
- **治理集中度**：Grade A——前三贡献者占比 32.4%（过去 12 个月内 244 位活跃维护者）。
- **许可风险**：无法计算——custom_modified_license。上游 `LICENSE` 是修改版 Apache License 2.0，额外加入多租户服务商用许可、前端 LOGO/版权信息不可移除等条件；应把 GitHub 的 `NOASSERTION` 当作真实的许可审查信号，而不是解析器误报。
## 存疑（未验证）

- [未验证] GitHub API 返回的许可为 `NOASSERTION`；2026-07-04 直接读取 `LICENSE` 显示其为修改版 Apache License 2.0，附加多租户服务使用、前端 LOGO/版权移除、贡献者授权与外观专利声明等条款。商业再分发或托管多租户使用前需要法律审查。
- [未验证] 生产自托管所需的精确资源（CPU、内存、磁盘）尚未从官方文档确认。
- [推断] 约 3 年的仓库拥有 147k star，可能包含大量炒作驱动的增长；有机的企业级采用需独立验证。
