---
name: Open Interpreter
slug: open-interpreter
repo: https://github.com/openinterpreter/open-interpreter
homepage: https://www.openinterpreter.com/
category: terminal-agents
tags: [coding-agent, terminal, codex-fork, harness, code-execution, mcp, acp, local-models]
language: Rust
license: Apache-2.0
maturity: rust-v0.0.17 (2026-07), active rewrite; ~64k stars (2026-07)
last_verified: 2026-07-01
type: framework
aka: [oi, interpreter]
upstream:
  pushed_at: 2026-07-06T01:41:29Z
  default_branch: main
  default_branch_sha: f3db7fff78125b0d6595e46bcbf43929b1c862a7
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:36:24Z
  overall: A
  overall_score: 3.5
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
        last_commit_age_days: 3
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 164.5
        qualifying_issues: 26
        band: default
        window_offset_days: 12
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: open-interpreter
        dependent_repos_count: 7
        downloads_last_month: 242577
        graph_tier: D
        volume_tier: B
        cross_check_divergence: 5.11
        release_downloads: 85381
        release_assets: 743
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1166
        last_commit_age_days: 3
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 363
        top1_share: 0.161
        top3_share: 0.298
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

# Open Interpreter

一个终端编码 agent，本质是 **OpenAI Codex CLI 的一个 fork**，重新聚焦在「模拟 agent harness」上——让低成本 / 开源模型（DeepSeek、Kimi、Qwen）跑出更好的行为：它在 OS 原生沙箱里执行命令、改文件，从 TUI 里切换模型与 harness，并暴露 skills / MCP / hooks / `AGENTS.md`。

![open-interpreter — 健康度雷达](../../../../assets/health/open-interpreter.zh.svg)

> **身份已变——请先读这段。** 你也许记得的那个项目——那个用 Python 写的「自然语言操作你的电脑」REPL，在本地生成并执行代码——*不是*这个仓库今天交付的东西。那套 Python 代码最后一次发版是 `v0.4.2`（2024-10），如今作为社区 fork 存活在 [`endolith/open-interpreter`](https://github.com/endolith/open-interpreter)。而 `openinterpreter/open-interpreter` 仓库已用 **Rust 重写成 Codex 的 fork**，于 2026 年年中重新发布。下文描述的全部是*当前*这个 Rust 项目。如果你想要的是老的 Python 工具，请用社区 fork，而不是看这一页。

## 何时使用

你是一名开发者，喜欢 Codex / Claude Code 那种终端 agent 工作流，但不想每一轮循环都按前沿模型的价格付费。你手上有更便宜或开源权重的模型——DeepSeek、Kimi、Qwen，或一个本地服务——你也注意到它们表现不如闭源模型，*并不是*因为它们没救，而是因为围着它们的 agent harness（系统提示、工具框定、编辑格式、步数纪律）是为别人的模型调的。你装上 Open Interpreter，敲 `i`，用 `/model` 选模型；再用 `/harness` 切换 **harness**——`native`、`claude-code`、`kimi-cli`、`qwen-code`、`deepseek-tui`、`swe-agent`、`minimal`——去找到最能榨出*你这个*模型本事的提示词/工具脚手架。这个 agent 在 OS 原生沙箱里跑 shell 命令、改文件，能通过内置 QA skill 驱动真实浏览器或原生应用，还能作为 [Agent Client Protocol](https://agentclientprotocol.com/) agent 运行，让你的编辑器直接和它对话。因为它继承了 Codex 的机器，你还开箱即得 `exec`、MCP、skills、hooks、权限与 `AGENTS.md` 支持。

当 harness *本身就是重点*时它最合适：你在为编码任务做低成本模型的基准测试或产品化，想要一个维护中的、Codex 级别的运行时，而其中针对具体模型的脚手架是一等公民、可热切换的旋钮，而不是你每换一个 provider 就重写一遍的东西。

## 何时不用

- **你正打算在一台要紧的机器上跑 LLM 编码 agent——先搞清楚执行风险。** 这是一个会根据模型输出执行 shell 命令、改文件的 agent。它带「原生沙箱」和一层权限/审批，但沙箱 + 审批是缓解，不是豁免：被提示注入的、或单纯出错的模型输出，仍可能在你批准的范围内删文件、外泄密钥、跑破坏性命令。把它当 Codex / Claude Code 对待——审它做了什么、限制它的访问范围、绝不把生产凭据交给它，并在信任它之前读一遍[沙箱与审批文档](https://www.openinterpreter.com/docs/terminal/sandbox)。这个风险是*agentic 代码执行的固有属性*，不是能等它修掉的 bug。[推断]
- **你想要的是老的 Python「对你的电脑说话」REPL。** 它已经从这个仓库消失了（见上面那段）。指望在 `openinterpreter/open-interpreter` 上用 Python `interpreter` 包 / API 来构建，会直接崩——那套 API 属于社区 fork，不属于这个仓库。
- **你需要*这套代码*有稳定 API 或生产业绩。** Rust 重写处在 `rust-v0.0.17`（2026-06）——一条 `0.0.x`、刚出几周的线。请预期变动、破坏性改动和毛刺；尽管仓库 star 很高，它并不是一个冻结、久经沙场的版本（那些 star 是*Python* 项目挣来的）。[推断]
- **你想要一个用来*构建*多 agent 系统的库 / SDK。** 这是一个终端编码 agent（外加一层 ACP / SDK 接口），不是用来以图、消息传递、持久状态组合多个 agent 的编排框架。要那个，去找像 [AgentScope](../../agent-runtimes/agent-sdks/agentscope.zh.md) 或 LangGraph 这样的运行时，而不是它。
- **你更愿意用规范的上游。** 既然它是 Codex 的 fork，如果你并不特别需要那套低成本模型 harness 模拟，OpenAI 自家的 Codex CLI（或 Claude Code）才是上游，团队更大、主线更快——Open Interpreter 骑在它们的 `main` 上，再加一层。
- **模型在循环里的成本/延迟仍会咬人——只是轻一点。** 它的前提是用更便宜的模型来压低单 token 成本，但一个会迭代的 agent（跑 → 观察 → 改 → 再跑）仍要花很多次调用；便宜模型还可能需要*更多*步才收敛，吃掉一部分节省，而 agentic 代码生成依旧非确定、时常出错。
- **你需要浏览器 / 原生应用 QA 模式可靠。** OS / 电脑控制、以及借外部工具（agent-browser、trycua）驱动应用，天然在 OS 版本、应用更新、屏幕状态之间脆弱；好用，但别在没有自己护栏的情况下，把关键工作流压在它上面。[未验证]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| OpenAI Codex CLI | 未收录 | 想要 Open Interpreter fork 的规范上游时，选 OpenAI Codex CLI。 | Open Interpreter fork 的**上游**。规范、团队更大、主线更快；为 OpenAI 模型调优。Open Interpreter 在其上加了可切换的低成本模型 harness 层，并跟踪 Codex 的 `main`。 |
| Claude Code / 类似厂商编码 CLI | 未收录 | 需要打磨良好、绑定特定模型家族的厂商终端编码 agent 时，选 Claude Code 或同类 CLI。 | 打磨良好、有厂商背书的终端编码 agent，绑定特定模型家族；更开箱即用，但并不围绕「为任意便宜 / 开源模型模拟 harness」来设计。 |
| [aider](aider.zh.md) | ✅ | 需要成熟、模型无关、git 感知的终端结对编程工具时，选 aider。 | 成熟、模型无关的终端结对编程工具，聚焦多 provider 下 git 感知的编辑；更轻、更长寿，但不是 Codex 衍生的沙箱化、可切 harness 的运行时。 |
| [smolagents](../../agent-runtimes/agent-sdks/smolagents.zh.md) | ✅ | 需要构建“代码动作”agent 的极小*库*，且由你内嵌和掌控时，选 smolagents。 | 一个用来构建「代码动作」agent 的极小*库*，由你内嵌并据为己有——光谱的另一端：你写循环，而 Open Interpreter 是一个完整的终端编码 agent 应用。 |
| endolith/open-interpreter（老的 Python OI） | 未收录 | 需要原版 Python“自然语言操作电脑”REPL 时，选老的 Python Open Interpreter。 | **原版** Python「自然语言操作电脑」REPL，现由社区维护。如果你真正想要的是这个老 Python 工具就选它；预期社区节奏的维护。 |

## 技术栈

- **内核：** Rust（`codex-rs` 工作区，继承自 OpenAI Codex——许多 crate：cli、exec、MCP、sandbox、ACP server 等）。仓库内还有一层薄薄的 `codex-cli` / npm 打包层和一个文档站。
- **agent harness 层：** Open Interpreter 的标志性新增——可选 harness（`native`、`claude-code`、`claude-code-bare`、`kimi-cli`、`qwen-code`、`deepseek-tui`、`swe-agent`、`minimal`），通过 `/harness` 在运行时切换，每个是为某个模型家族调过的一套提示词/工具/编辑脚手架。
- **执行与沙箱：** 在 macOS、Linux、Windows 上于 OS 原生沙箱里执行命令，带 `exec` 接口、一套权限/审批模型、hooks 与 `AGENTS.md` 支持（均为 Codex 血统）。
- **接口：** 交互式终端 TUI（`i` / `interpreter`）；Agent Client Protocol agent（`interpreter acp`）供编辑器接入；一个 SDK 目录；MCP 客户端支持；一个内置 QA skill，可驱动 web 应用（agent-browser）与原生应用（trycua）。
- **模型：** 从 TUI 切换 provider / 模型（`/model`），面向低成本 / 开源模型（DeepSeek、Kimi、Qwen）等；provider 配置依文档。

## 依赖

- **安装：** macOS/Linux 用一行 shell（`curl … openinterpreter.com/install | sh`），Windows 用一条 PowerShell 命令——注意这是把远程脚本管道进 shell，介意的话请先审一遍。也直接提供预编译安装包。
- **从源码构建：** 需要 Rust 工具链外加 **Bazel**（仓库用 Bazel / `MODULE.bazel`，底下是 Cargo 工作区）以及 `pnpm` 处理 JS / 打包侧——一个不轻松的多语言构建（依清单推断，见存疑）。
- **运行时：** 至少一个模型后端（一个托管 provider 的 API key，或一个本地模型服务）。不内置模型。
- **可选集成：** MCP 服务；`agent-browser`（Vercel Labs）做 web QA；`trycua` 做原生应用控制——各为你按需引入的外部依赖。
- **状态：** 配置与会话状态存在本地 `~/.openinterpreter` 下。

## 运维难度

**跑起来低，跑得*安全*中等，从源码构建高。** 用它就是一行安装加 `i`——无服务、无数据存储，状态是一个本地目录。真正的运维分量和任何执行代码的 agent 一样：决定并落实它被允许做什么（沙箱范围、审批、能看到的凭据）、盯住迭代循环里的 token 花费、并接受非确定的结果。从源码构建是难的那条路：Bazel + Cargo + pnpm 的多语言工具链。而且由于它跟踪 Codex 快速变动的 `main`、自身又在 `0.0.x` 线上，请预期频繁更新和升级时偶发的崩坏。

## 健康度与可持续性

- **响应速度**：Grade B——中位首次响应时间 58.5 小时，基于 18 个 qualifying issues/PRs。
- **维护——活跃、改写进行中（截至 2026-06）。** 最后推送 2026-06-20；未归档；Rust 线在发版（`rust-v0.0.16` / `rust-v0.0.17` 均为 2026-06-20）。但请注意这个**断档**：之前（Python）的发版止于 `v0.4.2`（2024-10-24），即项目大约 **20 个月没有打过 tag 版本**，才迎来 Rust 重启——这是一个真实的不连续，不是稳定节奏。「活跃」这个结论适用于*新*代码库，而它是全新的。[推断]
- **治理与 bus factor——创始人 + 上游 Codex 贡献者。** 由组织所有（`openinterpreter`）；提交历史由创始人（「killian」）加上一串通过「Merge upstream Codex main」进来的 OpenAI Codex 贡献者主导——也就是说大量工程是从 OpenAI 的 Codex 团队*继承*来的，而 OI 自有的那层重度依赖一个很小的核心。项目的路线图被绑在一个它并不掌控的 fork 上。[推断]
- **年龄与 Lindy——仓库老，但*当前*产品不老。** 仓库可追溯到 2023-07（约 3 年），但它今天交付的东西（Rust Codex fork）只有几周 / 几个月。年龄带来的 Lindy 先验**并不转移**：一个刚把自己代码库和身份扔掉的老仓库，更接近一个年轻项目，而非一个被验证过的项目。那 ~64k star 是被弃的 Python 工具挣来的，对新东西的耐久性说明不了什么。[推断]
- **采用与生态——品牌大，新形态未验证。** 来自原始时代的广泛心智份额与 star 数，活跃的 Discord 与文档站；但*Rust / Codex-fork* 这个化身的采用还很早、未被度量。[未验证]
- **风险信号——对一个 fork 的战略依赖 + 代码执行的内生风险，而非许可。** Apache-2.0（无重许可历史）。持久的风险是：（1）它的存亡系于跟踪 OpenAI 的 Codex 上游、以及维护 harness 层的那个小核心；（2）它是一个执行模型生成命令的 agent——一个内生的攻击面——所以它的沙箱 / 审批是承重的。[推断]

## 存疑（未验证）

- [未验证] 仓库事实，截至 2026-07-01 经 GitHub API：2023-07-14 创建、最后推送 2026-06-20、未归档、约 64.2k star、约 5.6k fork、Apache-2.0、语言报告为 Rust、owner 类型为 Organization。star / fork 有噪声且对时间敏感——且此处 star 数早于这次重写，因而高估了新代码库的实际牵引力。仅供参考。
- [未验证] 最新发布 `rust-v0.0.17`（2026-06-20），其前为 `rust-v0.0.16`（2026-06-20）；最后一个*Python 时代*的发布是 `v0.4.2`（2024-10-24，标为预发布）。约 20 个月的发版断档是从发布列表推断，并非维护者声明。
- [推断] 「OpenAI Codex 的 fork」与「为低成本模型模拟 agent harness」是项目自己的 README 说法，并由仓库内含 `codex-rs` / `codex-cli` / `.codex` 目录树、一份指向 `openai/codex/releases` 的 CHANGELOG、以及「Merge upstream Codex main」提交所佐证——但与上游 Codex 的确切差异未在此审计。
- [未验证] harness 列表（`native`、`claude-code`、`claude-code-bare`、`kimi-cli`、`qwen-code`、`deepseek-tui`、`swe-agent`、`minimal`）、QA skill 的浏览器 / 原生应用驱动（agent-browser、trycua）、ACP 支持、以及 MCP / hooks / 权限，均出自当前 README；其确切行为、稳定性与各 OS 支持未在此核实。
- [未验证] 「原版 Python 项目作为社区 fork 存活在 endolith/open-interpreter」是本仓库 README 所述；该 fork 自身的维护状态未独立核实。
- [推断] 从源码用 Bazel + Cargo + pnpm 构建，是从仓库的 `MODULE.bazel`、`Cargo.toml`、`pnpm-lock.yaml` 推断；确切受支持的构建路径可能不同——请遵循安装 / 构建文档。
- [未验证] 「macOS、Linux、Windows 上的原生沙箱」与审批模型是 README 声明（Codex 血统）；其确切隔离保证未经审计——未核实前，别把这个沙箱当作硬安全边界。
