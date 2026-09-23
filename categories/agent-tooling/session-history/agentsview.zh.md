---
name: AgentsView
slug: agentsview
repo: https://github.com/kenn-io/agentsview
category: session-history
tags: [coding-agents, observability, session-search, token-usage, cost-tracking, local-first, claude-code]
language: Go
license: MIT
maturity: v0.34.x, very active but young (2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2026-06-29T04:14:43Z
  default_branch: main
  default_branch_sha: 6804c297c52bfad176baf3e1a1813cbe77e416c4
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:54:15Z
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
        median_ttfr_hours: 12.5
        qualifying_issues: 14
        band: relaxed_solo
        window_offset_days: 12
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: agentsview
        dependent_repos_count: 0
        downloads_last_month: 29440
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
        homebrew_installs_90d: 2557
        homebrew_tier: B
        release_downloads: 223817
        release_assets: 1182
        release_tier: C
        signal_basis: homebrew+releases
        tier_source: homebrew+releases
    longevity:
      grade: C
      raw:
        repo_age_days: 215
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 97
        top1_share: 0.468
        top3_share: 0.719
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

# AgentsView

一个 local-first 的桌面/CLI 应用，在 40+ 个 agent（Claude Code、Codex、Cursor、Gemini 等）之间发现、搜索并分析你的编码 agent 会话——全文搜索、token 用量分析、成本追踪，全在你本机完成，无需账号。

![agentsview — 健康度雷达](../../../assets/health/agentsview.zh.svg)

## 何时使用

你是一名开发者（或小团队负责人），日常同时跑好几个编码 agent——这个仓库用 Claude Code、那个用 Codex，可能还有 Cursor 和 Gemini——结果线索全乱了：上周哪个会话修了那个 bug、你跨 agent 实际烧了多少 token（和多少钱）、你反复重复哪些 prompt。各工具的历史散落在不同的本地目录里，没有一个能给你跨 agent 的视图。你装上 AgentsView（一个 `curl | sh` 的 CLI、Homebrew/桌面应用，或 Docker），让它指向你的机器，它把本地会话日志索引进 SQLite，暴露一个绑定到 `127.0.0.1` 的 Svelte web UI，让你全文搜索每段对话、按 agent 和会话看 token/成本拆分、浏览分析——而不必把你的对话记录发到任何人的云上。

当你想要**对自己 agent 用量的可观测性**（成本控制、「我在哪儿做过 X」、用量模式）、并在意会话数据留在本地时，你会专门选它。可选的 Postgres/DuckDB 后端能让团队共享一个视图——如果你主动开启的话。

## 何时不用

- **你想开箱即用的托管/在线团队看板。** 它是 local-first，默认绑回环；团队共享意味着*你自己*要起 Postgres/DuckDB 并配网络。要 SaaS 的话，这不是。
- **你需要一个成熟、久经考验的工具。** 它只有几个月大却 star 很高——这种组合是炒作/成熟度*风险标记*，不是稳定性的证明；预期会有动荡、破坏性变更和粗糙处。[未验证]
- **你的 agent 不被支持、或没有集中的会话目录。** 它覆盖 40+ agent，但覆盖是逐个 agent 的；有些（如 Aider）因没有集中会话存储而需手动开启。请核实你的 agent 被处理。[未验证]
- **你处在受限的构建环境。** SQLite FTS5 需要 CGO；桌面应用是 Tauri 封装，前端开发需要 Node——用预编译产物没问题，但从源码构建有真实的工具链前置。
- **你反对任何遥测。** 存在匿名 PostHog 遥测（可经环境变量关闭）；若「零外联」是硬要求，请配置关闭并核实。[未验证]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| 各 agent 内置历史（Claude Code 的 `/resume` 等） | 未收录 | 原生零安装召回已经够用时，选各 agent 内置历史。 | 原生、零安装，但单 agent 且无跨工具搜索/成本汇总——正是 AgentsView 填的缺口。 |
| ccusage / token 成本 CLI | 未收录 | 只需要聚焦 agent 成本报告时，选 ccusage 或 token 成本 CLI。 | 聚焦 Claude Code/agent 的 token 成本报告器；范围更窄（成本，常为单 agent），对比 AgentsView 的搜索＋分析＋多 agent。 |
| [Langfuse](../../llm-eval/langfuse.zh.md) / Helicone / 可观测性 SaaS | 部分已收录 | 需要生产级 LLM 可观测性平台时，选 Langfuse 或 Helicone。 | 生产级 LLM 可观测性平台（tracing、evals）；为应用管线而建，通常托管/需埋点，而非对*你自己*编码 agent 会话做 local-first 浏览。 |
| 对 `~/.claude` / 会话目录做 grep | 未收录 | 零依赖本地搜索已经够用时，选 grep 会话目录。 | 零依赖且完全本地，但没有 UI、没有 token/成本计算、没有跨 agent 归一化。 |

## 技术栈

- **后端：** Go（1.26+），主存储为 **SQLite**（FTS5 全文搜索，需 CGO）；可选 **PostgreSQL** 与 **DuckDB** 后端。
- **前端：** Svelte 5 SPA（Vite ＋ TypeScript）。
- **桌面：** Tauri 封装，用于 macOS/Windows 桌面应用。
- **分发：** CLI 安装脚本（shell/PowerShell）、Homebrew、GitHub Releases，以及 Docker 镜像。

## 依赖

- **运行时：** 预编译的二进制/应用自包含；它以你的**本地 agent 会话目录**为数据源，并把索引存进 SQLite。服务默认绑定 `127.0.0.1`。
- **可选基础设施：** 想要团队共享/替代后端时用 PostgreSQL 或 DuckDB。
- **从源码构建：** Go 1.26+、CGO（SQLite FTS5 用），以及前端用的 Node 22+。
- **网络：** 核心功能可离线工作；除非关闭，存在可选的匿名 PostHog 遥测。

## 运维难度

**低到中。** 对单用户，顺路径就是一行安装或一个桌面应用，指向自己机器——没什么要运维的，数据留本地、绑回环。难度上升发生在你（a）从源码构建（CGO ＋ Go ＋ Node 工具链），或（b）在 Postgres/DuckDB 上为团队跑并配真实网络——此时你就拥有了一个数据库和一个对外暴露的服务。因为项目年轻且快速演进，预期版本间会有升级动荡和偶发破坏——运维风险更像「移动靶」而非「跑起来很复杂」。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 12.5 小时，基于 14 个 qualifying issues/PRs。
- **维护（2026-06）。** 极其活跃——2026-02 创建，最后 push 2026-06，快速发布小版本（v0.34.x）。显然在重度开发，不是吃老本。未归档。[推断]
- **治理 / bus factor。** owner 是 `kenn-io` **组织**，但项目**才约 4 个月大**，且头部贡献者（wesm）主导提交——早期阶段、很可能是小核心团队；bus factor 视作未经证明。[推断]
- **年龄与 Lindy——风险。** 2026-02 创建却已约 3.4k star。**年轻＋高 star 是炒作/成熟度风险标记，不是 Lindy 信号**：尚无历史记录，API 与存储格式可能仍会动荡，长期存续未经证明。把它当*新*工具来押注，而非已尘埃落定的东西。[未验证]
- **采用度。** star 增长快、agent 覆盖广，说明早期兴趣真实；能否持续并稳定下来是悬而未决的问题。[未验证]
- **风险标记。** 年轻/炒作错配（见上）；CGO/Tauri/Node 构建复杂度；可选遥测（可关闭）；pre-1.0 版本意味着没有稳定性保证。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 3.4k GitHub star，而仓库创建于 2026-02；star 数对时间敏感，「年轻仓库＋高 star」的组合被当作风险信号而非验证。
- [未验证]「40+ agent」及具体支持列表（Claude Code、Codex、Cursor、Gemini 等，Aider 需手动开启）来自 README，随版本变动；请核实你的 agent。
- [未验证] 技术栈细节（Go 1.26+、SQLite FTS5/CGO、Svelte 5、Tauri、可选 Postgres/DuckDB、Node 22+）取自 README，未在此独立构建/测试。
- [未验证] local-first / 绑回环 /「数据留本机」与可关闭的 PostHog 遥测均为 README 声明，未对运行中的二进制核实。
- [推断] pre-1.0 版本（v0.34.x）被解读为「无稳定性保证 / 预期破坏性变更」，这是从版本方案做出的推断。
