---
name: Agent Orchestrator
slug: agent-orchestrator
repo: https://github.com/AgentWrapper/agent-orchestrator
category: supervision-surfaces
tags: [parallel-agents, agentic-ide, git-worktrees, feedback-loops, desktop-app, electron, go-daemon, agent-adapters, tmux, claude-code]
language: Go
license: Apache-2.0
homepage: https://ao-agents.com
maturity: pre-1.0 (latest v0.10.1, 2026-06-28), very active, nightly prereleases; ~7.7k stars (as of 2026-06)
last_verified: 2026-06-29
type: app
upstream:
  pushed_at: 2026-06-29T11:30:35Z
  default_branch: main
  default_branch_sha: 3535d12f2c594ea4549a00c64d9183a2a1bc1622
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:41:29Z
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
        median_ttfr_hours: 6.8
        qualifying_issues: 21
        band: relaxed_solo
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: proxy.golang.org
        canonical_package: github.com/AgentWrapper/agent-orchestrator
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: "?"
        cross_check_divergence: null
        release_downloads: 506011
        release_assets: 1408
        release_tier: C
        signal_basis: releases
        tier_source: releases
    longevity:
      grade: C
      raw:
        repo_age_days: 221
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 96
        top1_share: 0.132
        top3_share: 0.297
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

# Agent Orchestrator

一个“Agentic IDE”——一个常驻的 Go daemon 加上一个 Electron/React 桌面应用，在隔离的 git worktree 里监管多个并行的 AI 编码 agent，并用自动反馈环把 CI 失败、PR review 评论和合并冲突路由回拥有该分支的 agent。

![agent-orchestrator — 健康度雷达](../../../assets/health/agent-orchestrator.zh.svg)

## 何时使用

你是一名资深工程师，同时跑着好几个编码 agent——一个 Claude Code 会话做某个功能、Codex 做重构、Aider 修 bug——已经过了“开一堆终端标签页”的阶段。这些 agent 在同一个工作树上彼此踩脚，你弄不清哪个正干到一半，而当 CI 失败、reviewer 在 PR 上留了评论时，又得你手动把失败信息复制粘贴回对应 agent 的 prompt 里。你想要一个控制面，让每个 agent 各走各的车道，并替你把这些环路闭合，不用你盯着喂。

于是你把 Agent Orchestrator 作为桌面应用装上。它跑一个本地 Go daemon，把每个 agent 生成在它自己的 git worktree 里（macOS/Linux 用 tmux，Windows 用 conpty），这样并行工作永远不会在同一份 checkout 上撞车。你在 GUI 里规划任务、分配给 agent，看着实时状态经 SSE 流进来（底层是带变更数据捕获的 SQLite）。当某个任务的 CI 跑挂了、reviewer 在 PR 上评论了、或出现合并冲突时，orchestrator 会把那个信号直接路由回拥有该分支的 agent——反馈环自己跑起来。因为它通过适配器对接 23+ 种 CLI agent（“只要它能在终端里跑，就能在 Agent Orchestrator 上跑”），你可以混用多家厂商，而不用把整套工作流押在一家身上。当你要监管 N 个跑在真实分支上的并行 agent 时——而非在单仓库里跑单个 agent——你才会选它。

## 何时不用

- **太年轻，下不了定论。** 2026-02 创建——约 4.5 个月大（截至 2026-06）。Lindy 还不给它加分；几个月大的仓库有高 star 是注意力信号，不是履历。别把关键工作流押在它的稳定性上。[推断]
- **pre-1.0 变动 / nightly 节奏。** 它发布 nightly 预发布版，第一个 0.10.x 也才在本文写作前几天打 tag——API、schema 和桌面 UI 都可能随版本变动。需要稳定就钉死版本。
- **单一 User 所有、无基金会。** 仓库的 `owner.type` 是 **User**，而非 Organization 或基金会；一个人（AgentWrapper）加一名头部贡献者集中了 bus factor。路线图与延续性系于一个小团体，而非机构背书。
- **你想要无头 / CI 优先的工具。** 这是一个 GUI 桌面应用（Electron）加本地 daemon——它是为坐在开发者机器上而造，不是为在流水线或服务器上无人值守运行。要可脚本化、无头的 orchestrator，这个不合适。
- **daemon 的安全姿态是硬伤。** 控制 daemon 是“Loopback-Only……在 127.0.0.1 上做 HTTP 控制，**no auth, CORS, or TLS by design**”——对单台可信机器没问题，但这意味着任何本地进程都能驱动它；别暴露该端口，也别在共享/多用户主机上跑。
- **对 worktree 不友好的仓库。** 并行隔离依赖 git worktree；带重 submodule、大量生成产物、或 checkout 级环境无法在 worktree 中存续的仓库，会与该模型相抵。
- **对遥测敏感的环境。** 遥测是存在的（本地默认、远程传输经环境变量 opt-in）——在受限场景部署前先核实开关与你的合规策略。
- **你只跑一个 agent。** 单仓库里的单个 agent 从并行监管控制面里得不到任何东西；在 N=1 时，daemon 加桌面应用纯属额外开销。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [CCPM](../work-state/ccpm.zh.md) | ✅ | 需要现有 harness 内的 PRD→GitHub Issues→并行 worktree 流程时，选 CCPM。 | 规格驱动：PRD → GitHub Issues → git worktree 并行 agent，作为 skill-pack 从你现有 harness 里驱动。CCPM 是流程 + GitHub 原生、无 GUI；Agent Orchestrator 是桌面应用 + daemon，监管活的 agent 并自动路由 CI/review/冲突反馈。处于不同层——你大可用 CCPM 规划、用它来跑。 |
| [OpenSandbox](../../sandboxing/opensandbox.zh.md) | ✅ | 需要在 K8s 规模安全执行不可信 agent 代码的沙箱运行时时，选 OpenSandbox。 | 一个沙箱*运行时*，用于在 K8s 规模上安全执行不可信的 agent 代码（隔离、出口、保险库）。正交：OpenSandbox 隔离的是*执行*；Agent Orchestrator 编排的是跨 worktree 的*agent*。你可以把 agent 跑在沙箱下、再在这里监管它们。 |
| [Planning with Files](../work-state/planning-with-files.zh.md) | ✅ | 轻量 markdown 规划约定已经够用时，选 Planning with Files。 | 轻量的基于文件的规划范式（计划以 agent 读写的 markdown 形式存在）；没有并行监管、没有 GUI、没有反馈环路由。它是这套东西在状态保持上所替代的最小基线。 |
| Conductor / Crystal / Claude Squad | 未收录 | 需要其他 worktree 并行 Claude Code 工具时，选 Conductor、Crystal 或 Claude Squad。 | 其他“在 git worktree 里并行跑 Claude Code agent”的工具（桌面或 TUI）。在核心思路上可直接对比；差异在 agent 广度（Agent Orchestrator 瞄准 23+ 适配器）、反馈环自动化和成熟度——若你已收窄到这个细分，列入候选直接比。 |
| Vibe Kanban | 未收录 | 需要看板优先的多编码 agent 编排体验时，选 Vibe Kanban。 | 看板风格的多编码 agent 编排工具；“监管多个 agent”的目标重叠，但走的是看板优先的交互，而非 worktree-daemon 加反馈环的侧重。 |
| 纯 tmux + `git worktree` 脚本 | 未收录 | 零依赖和完全可脚本化最重要时，选纯 tmux 加 git worktree 脚本。 | 零依赖、完全可脚本化，但 worktree 生命周期、agent 适配器、实时状态 UI、CI/review/冲突路由都得你自己手搓——这正是 Agent Orchestrator 打包好的胶水。 |

## 技术栈

- **后端：** 一个常驻的 Go HTTP daemon（Go 是主语言，约 2.6MB 源码），带入站/出站端口契约；控制面是 loopback-only。
- **前端：** 一个 Electron + React 桌面应用（约 900KB TypeScript），用 TanStack Router/Query 和 shadcn/ui。
- **终端运行时：** Darwin/Linux 用 tmux，Windows 用 conpty，承载每个 agent 的会话。
- **隔离：** git worktree，每个 agent/任务一个，带专属运行时。
- **存储 / 流式：** 带变更数据捕获（CDC）的 SQLite，经 SSE 广播给 UI。
- **agent 接口面：** 23+ 种 CLI 编码 agent 的适配器（Claude Code、Codex、Cursor、OpenCode、Aider、Amp、Goose、Copilot、Grok、Qwen Code、Kimi Code、Cline、Continue、Kiro 等）；其余部分是文档（MDX）。

## 依赖

- **桌面应用 + daemon 本身**——以 Windows `Setup.exe`、macOS DMG、Linux AppImage 分发；Go daemon 在本地 127.0.0.1 上运行。
- **从源码构建的工具链：** Go 1.25+、Node.js 20+、pnpm 和 Git（按 README 的最低要求）。
- **tmux**（Darwin/Linux；Windows 内置 conpty）来支撑终端会话。
- **你要编排的那些编码 agent**——每个 CLI agent（Claude Code、Codex 等）由你自己提供并鉴权；orchestrator 驱动它们，不打包它们。
- **GitHub CLI（`gh`）** 用于带鉴权的 GitHub API 调用（PR/review 反馈环）。

## 运维难度

**对个人是低到中；不是为机群运维而造。** 作为桌面应用，它从打包好的二进制安装、跑在一台开发者机器上——这条路很轻松。复杂度在于运行期而非部署期：你跑着一个本地 daemon，它跨 git worktree 生成多个 agent 进程，因此磁盘与进程压力随并行度上升，而对 worktree 不友好的仓库（submodule、生成产物）会让设置变得别扭。loopback 无鉴权的 daemon 在可信单用户机器上没问题，但**不**适合在共享/多用户主机上跑或对外暴露。没有文档化的多用户/服务器部署方案——这是个人控制面，不是你为团队运维的基础设施。[推断]

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 16.3 小时，基于 8 个 qualifying issues/PRs。
- **维护（2026-06）。** 最后 push 于 2026-06-29，带频繁的 nightly 预发布，v0.10.1 于 2026-06-28 打 tag——**非常活跃**的开发。未归档。另一面：约 588 个未关 issue 配上很高的 fork 数，说明是个快速演进、仍在稳定中的项目。[推断]
- **治理 / bus factor。** `owner.type` 是 **User**，不是 Organization 或基金会。约 36 名贡献者，但贡献集中在头部几人（harshitsinghbhandari、suraj-markup 和所有者 AgentWrapper）；Discord 驱动、带“每日贡献者同步”的社区显出热度，但路线图系于一个小的、个人所有的群体——真实的 bus-factor 风险。[推断]
- **年龄 × Lindy（2026-06）。** 2026-02 创建——约 4.5 个月大。这是一个**非常年轻的项目**；Lindy 不给它加分。把 API/schema/UI 稳定性当成未经验证，寿命未知。
- **采用度与生态。** 约 4.5 个月内约 7.7k star、约 1.1k fork，对一个这个年龄的 User 所有仓库而言异常地高；这*可能*反映真实拉力，也*可能*是炒作/灌水——数据无法区分二者，所以别把它当履历来读。广的 agent 适配器覆盖（23+）是最强的生态信号。[推断]
- **风险标记。** 年轻 + pre-1.0 变动（nightly 节奏）、单一 User 所有且无基金会、loopback 无鉴权的 daemon 姿态、仅 GUI 桌面（非无头）、以及 opt-in 的远程遥测。Apache-2.0，未发现 relicense 历史。[未验证]

## 存疑（未验证）

- [未验证] 约 7.7k star、约 1.1k fork、约 588 个未关 issue、最新 v0.10.1、约 36 名贡献者——均截至 2026-06-29；这些数字对时间敏感且易变（nightly 节奏），仅供参考。
- [推断] “对一个这么年轻的 User 所有仓库而言 star 异常地高”按 read-repo 方法论被标记为可能的炒作/灌水信号——这**不是**断言这些数字被灌水，只是说年龄 + 所有权 + 量级合起来值得警惕；数据既不能证实也不能证伪。
- [未验证] “Loopback-Only……no auth, CORS, or TLS by design”的姿态、遥测（本地默认 / 经环境变量远程 opt-in）、23+ 适配器清单、tmux/conpty 运行时，以及 SQLite-CDC-over-SSE 架构，均取自 README/文档，未在源码中独立核实。
- [推断] 归类为 `type: app`（而非 `tool`），因为主要交付物是一个打包的 Electron **桌面应用**加本地 daemon，而非无头 CLI/库——GUI 才是产品面。
- [未验证] 自动反馈环路由（把 CI 失败、PR review 评论、合并冲突送回拥有该分支的 agent）是项目的招牌声称；其在 23+ 种 agent 上的实际可靠性未经验证，且 LLM/agent 行为从不被保证。
- [未验证] bus-factor 的判断（贡献集中在头部、“每日贡献者同步”的 Discord 节奏）是从贡献者清单与社区信号推断，而非来自治理文档；未确认有 GOVERNANCE/CODEOWNERS。
- [未验证] 与 Conductor / Crystal / Claude Squad / Vibe Kanban 的对比反映同细分内的总体定位，而非逐项实测基准。
