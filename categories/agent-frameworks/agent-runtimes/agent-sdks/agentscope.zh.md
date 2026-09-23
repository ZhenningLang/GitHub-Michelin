---
name: AgentScope
slug: agentscope
repo: https://github.com/agentscope-ai/agentscope
category: agent-sdks
tags: [multi-agent, llm-agent, react-agent, observability, message-passing, mcp, tool-use, async, human-in-the-loop]
language: Python
license: Apache-2.0
maturity: v2.0.2, active (2026-06)
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-06-29T06:35:40Z
  default_branch: main
  default_branch_sha: 3467754dc48c7ba12cfce79fae6e0fa39831074b
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:30:42Z
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
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 11.6
        qualifying_issues: 19
        band: default
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: agentscope
        dependent_repos_count: 0
        downloads_last_month: 321531
        graph_tier: E
        volume_tier: B
        cross_check_divergence: 1.02
        release_downloads: 56
        release_assets: 3
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 985
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 90
        top1_share: 0.415
        top3_share: 0.652
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

# AgentScope

一个用于构建并对外服务多智能体 LLM 应用的 Python 框架，倾向于信任模型的推理/工具调用能力而非死板编排，把统一事件总线、细粒度工具权限、OpenTelemetry tracing 直接焊进 agent 循环里。

![agentscope — 健康度雷达](../../../../assets/health/agentscope.zh.svg)

## 何时使用

你是后端或平台工程师，任务是把一个 LLM agent 真正作为线上服务交付——不是 notebook 里的 demo。你需要的不只是一个 ReAct 循环：工具必须跑在隔离沙箱里（用户的 `bash` 调用不能碰到宿主机），线上出问题时每一次模型调用和工具调用都得能追踪，而且人工审核者要能在运行中途批准或拦截一个敏感动作。你还需要这个服务在多租户、多会话并发下稳得住，各自的状态不会互相串。AgentScope 2.0 正是为这条线设计的：它带了基于 FastAPI 的 agent service、对工具和资源做闸门的权限系统、支持 local/Docker/E2B 的 workspace 沙箱后端，以及作为 middleware 接入的 OpenTelemetry tracing——那些你本来要自己手搓的可观测性和隔离，框架直接给你。

另一个适合 AgentScope 的时刻，是你想要一个可组合、事件驱动的 agent，而不是“拼好 prompt 然后祈祷”的脚本。它的 middleware 系统让你能 hook 进推理-行动循环（上下文压缩、工具结果压缩、自定义守卫），统一事件总线把 `REPLY_START` / `MODEL_CALL_START` / `TEXT_BLOCK` 这类事件流式推给前端——`examples/web_ui` 下还有一个预置 Web UI，支持 agent 团队、任务规划和权限控制。如果你的终点是一个可检视、带人工介入、有 UI、可接多种模型后端（DashScope、OpenAI、Anthropic、Gemini、Ollama、xAI）的 agent 应用，这正中靶心。

## 何时不用

- **你想要单文件、零基础设施的 agent。** AgentScope 的价值在于那套 service/权限/可观测/沙箱机制。如果只是想在脚本里跑个用工具的循环，更薄的库（裸 OpenAI SDK 加几个工具，或一个极简 ReAct helper）要学和要部署的面小得多。
- **你优化的是 prompt *程序*，不是编排。** 如果你的问题是“编译并调优 prompt/流水线”而非“运行并服务 agent”，像 [DSPy](../../workflow-builders/dspy.zh.md) 这种程序综合路线是完全不同的工具——AgentScope 不做 prompt 优化。
- **你需要久经考验、生态庞大、有多年第三方集成的框架。** AgentScope 2.0 是近期的一次大重写 [推断]；它的 2.x API 面更新、更小，因此社区配方、Stack Overflow 覆盖和第三方插件都更稀薄。
- **API 抖动是你不能接受的。** v2.0 相对 v1.x 对 `Msg` 类、工具模块和 middleware 做了大幅重构——针对 1.x 写的代码无法干净迁移，而快速演进的 2.x 线可能还会继续变。请 pin 版本。
- **你不是 Python 技术栈。** 它仅支持 Python(>=3.11)，没有一等公民的 TypeScript/Go/Java SDK。
- **你只想要一个托管的 agent 产品。** 这是一个你自己运行和运维的框架，不是托管 SaaS——部署、扩容、模型 API key 都得你自己管。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [DSPy](../../workflow-builders/dspy.zh.md) | ✅ | 需要声明式 prompt/流水线*优化*，而不是多智能体服务运行时时，选 DSPy。 | 声明式的 prompt/流水线*优化*（编译 + 调优程序）；不是多智能体服务运行时。用它提质量，而不是用它编排/服务 agent。 |
| [openfang](../agent-services/openfang.zh.md) | ✅ | 想要另一个已收录、运行时更像 OS 的 agent 框架时，选 openfang。 | 本索引内的同类 agent 框架；设计取向不同——选型前对比 scope/成熟度。[未验证] |
| [Symphony](../agent-services/symphony.zh.md) | ✅ | 需要聚焦自治 coding agent 运行调度的同类框架时，选 Symphony。 | 本索引内的同类多智能体框架；“编排多个 agent”目标有重叠，工效学不同。[未验证] |
| [claude-octopus](../../coding-agents/orchestration-and-review/claude-octopus.zh.md) | ✅ | 需要围绕 Claude 式多智能体工作流的同类项目时，选 claude-octopus。 | 本索引内的同类项目，围绕 Claude 式多智能体工作流；模型聚焦比 AgentScope 的多 provider 服务更窄。 |
| [LangGraph](langgraph.zh.md) | ✅ | 需要生态庞大、控制流显式的图/状态机式编排时，选 LangGraph。 | 图/状态机式编排，生态庞大、控制流显式；比 AgentScope“信任模型”的循环更重、更有主张。 |
| [AutoGen](autogen.zh.md) | ✅ | 需要成熟的对话驱动多智能体框架时，选 AutoGen。 | 成熟的对话驱动多智能体框架；多智能体 scope 可比，抽象不同、社区盘子更大。 |
| [CrewAI](crewai.zh.md) | ✅ | 角色/crew 式 agent 编排和强 DX 比 AgentScope 的服务栈更重要时，选 CrewAI。 | 角色/crew 式 agent 编排，DX 很好；不像 AgentScope 那样强调 service/权限/沙箱/可观测这整套栈。 |

## 技术栈

- **语言：** Python(>=3.11)。
- **核心运行时：** 基于 `asyncio`；模型 SDK `openai`、`anthropic`、`dashscope`（以及可选 `google-genai`、`ollama`、`xai-sdk`）。
- **协议/工具：** 经 `mcp` 接入 Model Context Protocol（统一 `MCPClient`）;`tree_sitter` / `tree_sitter_bash` 做工具/代码处理；`jsonschema`、`docstring_parser`、`json_repair`、`json5` 做工具 schema 与稳健解析。
- **服务层：** FastAPI + Uvicorn agent service（可选 `service` extra）、`apscheduler`、`ag-ui-protocol`;Socket.IO（`python-socketio`）做到前端的事件总线。
- **可观测性：** OpenTelemetry（`opentelemetry-api/sdk/exporter-otlp`、语义约定）以 tracing middleware 形式接入。
- **Workspace/沙箱：** local、Docker(`aiodocker`)、E2B（`e2b`）后端（可选 `workspace` extra）。
- **存储/记忆：** Redis 会话（可选 `storage` extra）;`mem0ai` 集成（可选 `mem0` extra）。

## 依赖

- **运行时：** Python >= 3.11。`pip install agentscope`（或 `uv pip install agentscope`）。
- **始终安装的依赖：** `openai`、`anthropic`、`dashscope`、`mcp`、`httpx`、`numpy`、`aioitertools`、`aiofiles`、`jinja2`、`jsonschema`、`docstring_parser`、`json_repair`、`json5`、`filetype`、`python-datauri`、`python-socketio`、`python-frontmatter`、`shortuuid`、`tree_sitter`、`tree_sitter_bash`，以及 OpenTelemetry 栈（`opentelemetry-api/sdk/exporter-otlp>=1.39.0`）。
- **可选 extras:** `service`(FastAPI/Uvicorn/apscheduler/ag-ui-protocol)、`storage`(redis)、`workspace`(aiodocker/e2b)、`gemini`(google-genai)、`ollama`、`xai`、`tools`(ripgrep)、`mem0`(mem0ai>=2.0.0)。
- **外部基础设施（只在你启用时才需要）:** Docker daemon 或 E2B 账号做沙箱 workspace;Redis 实例做持久化会话；OTLP collector 接收 trace；以及至少一个模型 provider 的 API key。

## 运维难度

**中。** 一个纯进程内的 agent 很简单——装上、设个模型 key、跑起来。难度随着你打开那些“当初选 AgentScope 的理由”而上升：把带多租户/多会话隔离的 FastAPI service 立起来、跑 Docker/E2B 沙箱后端（于是你现在要运维一个容器运行时）、接一个 OTLP collector 才能真正消费 trace、再加 Redis 做持久会话。这些都不算冷僻，但每一个都是要部署和监控的真实活动部件；而快速演进的 2.x 线意味着你应当 pin 版本，并为升级抖动预留预算。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 11.6 小时，基于 19 个 qualifying issues/PRs。
- **维护（2026-06）：** 活跃维护——默认分支 push 于 2026-06-25，最新 release v2.0.2（2026-06-16），未归档。健康的 open issue 数（约 262）配合稳定发版，读作一个有人投入的活项目，而非停滞。
- **治理与背书：** Organization 持有（`agentscope-ai`），以 DashScope（阿里巴巴的模型平台）为默认/一等公民后端——即背后有一个贴近厂商的真实组织，而非单一维护者，bus-factor 上比单用户仓库更稳。它不在中立基金会（Apache/LF/CNCF）之下，故把治理当作贴近厂商的托管来看待（未经确认之处见存疑）。
- **年龄与 Lindy（2026-06）：** 创建于 2024-01，约 2.5 岁——本批中**最老、最成熟**的项目，且仍在活跃发版。Lindy 裁决：**年龄 × 仍活跃，偏有利**（一个多年、有维护的框架）。需注意的是近期的 **v2.0 重写**：*项目*在 Lindy 上很强，但 *2.x API 面*年轻，因此社区配方和第三方集成仍比项目年龄所暗示的稀薄。
- **风险标记：** Apache-2.0（宽松，未见 relicense/CLA 顾虑）。主要风险是 **2.x API 抖动**——v2.0 相对 v1.x 破坏了 `Msg`/工具/middleware，且该线仍在变，故请 pin 版本并为升级预留工作量。未审 CVE。

## 存疑（未验证）

- [未验证] 截至 2026-06,star 约 27.2k（来自 `gh repo view`）。本生态的 GitHub star 不可靠且对时间敏感——仅供参考。
- [未验证] 最新发布 v2.0.2 于 2026-06-16，默认分支最后 push 于 2026-06-25（据 GitHub API）。具体版本/日期会变，请对照仓库重新核实。
- [推断] “v2.0 是一次大重写、对 `Msg`/工具/middleware 有破坏性改动”是从 v2.0.0 release notes 的重构措辞推断而来；迁移前应读官方 changelog 确认确切的破坏性改动清单。
- [未验证] 与同类（openfang、Symphony、claude-octopus）的相对对比是定位草图，不是跑分过的正面对决；选型前请核实每个同类项目的当前 scope。
- [未验证] "production-ready" / “生产级服务”是项目自己在 README 里的说法，并非经独立验证的结论。
- [推断] 受支持的模型 provider 集合与可选 extras 随版本变动；此处列表反映当前 `pyproject.toml`，针对某具体 provider 请重新核实。
