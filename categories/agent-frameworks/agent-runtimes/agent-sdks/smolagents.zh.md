---
name: smolagents
slug: smolagents
repo: https://github.com/huggingface/smolagents
category: agent-sdks
tags: [code-agent, react, llm-agent, tool-use, minimal, hugging-face, litellm, mcp]
language: Python
license: Apache-2.0
maturity: v1.x, active, ~28k stars (2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-23T18:34:53Z
  default_branch: main
  default_branch_sha: 526069c1ead958b36d9fd09a6b1ef37f68ed6ade
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:31:42Z
  overall: B
  overall_score: 3.17
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 31
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 35.8
        qualifying_issues: 32
        band: default
        window_offset_days: 7
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: smolagents
        dependent_repos_count: 0
        downloads_last_month: 467299
        graph_tier: E
        volume_tier: B
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 656
        last_commit_age_days: 31
        cohort: library
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 25
        top1_share: 0.429
        top3_share: 0.622
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

# smolagents

一个极简的库，用来构建“用代码思考”的 agent：LLM 不再吐 JSON 工具调用，而是把动作写成 Python 代码片段（`CodeAgent`），在 ReAct 循环里执行——整个 agent 逻辑约 1,000 行、模型无关、并接进 Hugging Face Hub。

![smolagents — 健康度雷达](../../../../assets/health/smolagents.zh.svg)

## 何时使用

你是一名工程师或研究者，想要一个能在一个下午里从头读懂的 agent 循环。你看过那些更重的框架，被它们的抽象税劝退了——graph 构建器、节点注册表、回调管理器——可你真正想要的不过是「LLM 提出一个动作，我们执行它，把结果喂回去，再来一轮」。你选 smolagents，是因为它的内核只有几百行、能在 debugger 里逐步走完，而它的标志性赌注是：agent 的动作是*写 Python*（`CodeAgent`），而不是去填 JSON 工具 schema——这种方式天然可组合（循环、条件、中间变量），多工具任务往往用更少的步数就能完成。你定义几个 `@tool` 函数，通过 LiteLLM 或 HF Inference API 指向任意模型，就有了一个能跑的「代码动作」agent，而不必接受某个框架的世界观。

当你在挑模型、或想贴着 Hugging Face 生态时，它同样合适：同一个 agent 可以跑在托管和本地模型上，工具与 agent 还能推到 Hub、从 Hub 拉回。如果你的价值在于一个*小、透明、可改*、能 fork 并据为己有的循环——而非一个托管平台——那就是 smolagents 的最佳落点。

## 何时不用

- **你需要复杂、有状态的编排——图、分支、持久状态、人在环检查点。** smolagents 是*刻意*极简的；它给你一个循环，不是工作流引擎。要显式的图、条件边和持久化，LangGraph 是更合适的工具，硬往 smolagents 上焊这些只会处处别扭。
- **你扛不起代码执行的安全负担。** 这个 agent 的前提就是*运行模型生成的 Python*。内置的 `LocalPythonExecutor` 被明确声明**不是安全边界**——安全使用意味着接上沙箱（E2B、Modal、Docker 等），这是真实的运维工作，在任何不可信或生产场景里都不能省。
- **你需要稳定、冻结的 API。** 它很年轻（2024-12 创建），处在快速的 v1.x 发版节奏里，接口仍在版本间变动 [推断]。请 pin 住版本，并预期升级时偶尔要做迁移。
- **你想要开箱即用的生产级 agent OS**——多 agent 运行时、消息传递、可观测性、现成的部署方案。smolagents 是库，不是平台；要那些，去看更重的运行时，比如 [AgentScope](agentscope.zh.md)。
- **你是在对照指标优化提示词/程序，而不只是跑一个循环。** 如果目标是被编译、可度量的 LM 程序，而非手写的动作循环，那是 [DSPy](../../workflow-builders/dspy.zh.md) 的活，不是它的。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [LangGraph](langgraph.zh.md) | ✅ | 需要基于图的编排，带持久状态、检查点和人在环时，选 LangGraph。 | 基于图的编排（节点/边、持久状态、检查点、人在环）；处理复杂有状态工作流强得多，但更重、要学的抽象也更多。smolagents 把这些全部换成一个极小可读的循环。 |
| [AgentScope](agentscope.zh.md) | ✅ | 需要带消息传递、可观测性和部署能力的多 agent 运行时/平台时，选 AgentScope。 | 多 agent 运行时/平台（消息传递、可观测性、部署）；是一个生产级「agent OS」，而 smolagents 是你内嵌并据为己有的单循环库。 |
| [DSPy](../../workflow-builders/dspy.zh.md) | ✅ | 需要对照指标编译/优化 LM 程序时，选 DSPy。 | *对照指标编译/优化* LM 程序；范式不同——smolagents 只跑一个「代码动作」循环，不优化提示词或权重。 |
| [CrewAI](crewai.zh.md) | ✅ | 需要基于角色/crew 的多 agent 编排和更高层团队模型时，选 CrewAI。 | 基于角色/crew 的多 agent 编排，走更高层的「一队 agent」模型；比 smolagents 单一透明循环更有结构、也更有主张。 |
| [Pydantic AI](pydantic-ai.zh.md) | ✅ | 需要类型安全、以 Pydantic 为中心的结构化输出框架时，选 Pydantic AI。 | 类型安全、以 Pydantic 为中心的 agent 框架，强调结构化/被校验的输出；smolagents 则倾向「代码即动作」，而非 schema 校验式的工具调用。 |

## 技术栈

- **语言：** Python。
- **核心抽象：** 一个 ReAct 式的 agent 循环；招牌变体是 `CodeAgent`，其动作是一段被执行的 Python 片段，另有 `ToolCallingAgent` 作为 JSON 工具调用的替代。工具就是普通 Python 函数（`@tool`）或 `Tool` 子类。
- **代码执行：** 内置 `LocalPythonExecutor`（有一定隔离，但明确*不是*安全边界），外加远程/托管沙箱集成（E2B、Modal、Docker、Blaxel）。
- **模型网关：** 模型无关——Hugging Face Inference API / 本地 `transformers`，并通过 LiteLLM 实现 provider 无关访问（OpenAI、Anthropic、本地服务等）。
- **生态钩子：** Hugging Face Hub（推/拉工具与 agent）、MCP 工具服务、以及 LangChain 工具互通。（具体集成/版本支持依文档——见存疑。）

## 依赖

- **运行时：** Python（现代 3.x）。调用托管模型时框架本身不需要 GPU；本地跑模型则会引入 `transformers`/`torch` 及其对应的硬件要求。
- **模型：** 至少一个 LM 后端——HF Inference 端点或 API key、一个 LiteLLM 支持的 provider、或本地模型。
- **沙箱（任何不可信使用都需要）：** 一个外部沙箱——E2B / Modal（云）或 Docker（自建）——这是它自身的依赖与运维面，并不内置。
- **安装：** `pip install smolagents`（特定集成有 extras，例如工具/遥测）。

## 运维难度

**原型阶段低，一旦动真格就中等。** 作为库它就是 `pip install` 加几行代码就有一个能跑的循环——无服务、无数据存储、无集群。难度集中在两处，都源于「agent 会运行生成的代码」：其一是**沙箱**——一旦输入不完全可信，你就必须搭起 E2B/Modal/Docker 隔离，并把本地执行器当作不安全；其二是常见的 agent 运维（token 成本、循环/步数上限、重试、可观测性），因为这是一个薄循环而非托管平台，这些得你自己加。请 pin 住版本，以隔离快速变动的 API。

## 健康度与可持续性

- **响应速度**：Grade C——中位首次响应时间 211.9 小时，基于 24 个 qualifying issues/PRs。
- **维护——非常活跃（截至 2026-06）。** 最后推送 2026-06；以轻快的 v1.x 节奏发版（main 上 1,000+ commit）。读起来在积极开发，而非吃老本；未归档。
- **治理与背书——Hugging Face（强信号）。** 归 `huggingface` 组织所有，而非孤身维护者。HF 背书是一个有分量的可持续信号：它是开放模型生态里资源充足的核心玩家，有持续维护工具链的记录——这实质上对冲了项目的年轻。[推断]
- **年龄与 Lindy——年轻、Lindy 未验证，但被背书方对冲。** 2024-12 创建，约 1.5 年（截至 2026-06）。单看「年龄 × 仍活跃」，它**跨不过** [DSPy](../../workflow-builders/dspy.zh.md) 这类更老框架能跨过的 Lindy 门槛——还没有长期记录——但 HF 背书 + 快速采用，相对一个被炒作的个人项目，大幅降低了「它还会不会在」的风险。[推断]
- **采用与生态——快速增长。** ~28k star（2026-06），「code agent」这一理念心智份额广；接入 HF Hub、LiteLLM 与 MCP。star 有噪声，但采用曲线与生态钩子都健康。[未验证]
- **风险信号——长期存在的代码执行安全风险 + API 变动，而非许可。** Apache-2.0，未发现重许可历史。真正持久的风险是内生的：agent 会执行模型生成的代码，所以不安全部署（无沙箱）是一个实打实的攻击面——这是设计的固有属性，不是能等它修掉的 bug。次要风险是年轻 API 在版本间的迁移成本。

## 存疑（未验证）

- [未验证] ~28.1k GitHub star、最新发布 v1.26.0（日期 2026-05），依 GitHub 仓库页；star 数不可靠且对时间敏感，你读到时很可能已有更新版本——仅供参考。
- [未验证] 「2024-12 创建（截至 2026-06 约 1.5 年）」是依仓库历史推断；如该事实关键，请核实确切创建日期。
- [未验证] 「约 1,000 行核心 agent 逻辑」是项目 README 的自述说法，并非对当前代码树的实测行数。
- [未验证] 具体沙箱集成（E2B、Modal、Docker、Blaxel）与生态钩子（LiteLLM provider 清单、MCP、LangChain 互通）依 smolagents 文档/README；依赖前请确认具体集成与版本支持。
- [推断] 「快速变动的 v1.x API / 偶有破坏性变更」是依发版节奏推断，也是年轻 agent 库的通性，未在此对照具体 changelog 确认——升级前请看 changelog。
- [推断] `LocalPythonExecutor`「不是安全边界」是项目自述立场；由此得出的实务结论（不可信输入务必用真正的沙箱）是顺推，但所选沙箱的确切隔离保证仍需你自行核实。
