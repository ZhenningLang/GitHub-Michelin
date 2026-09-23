---
name: Entire
slug: entire-cli
repo: https://github.com/entireio/cli
category: session-history
tags: [ai-agents, session-capture, git-hooks, checkpoints, rewind, transcript, audit, go, cli, multi-agent]
language: Go
license: MIT
maturity: v0.7.x line, active as of 2026-06 (latest release v0.7.7, 2026-06-18); pre-1.0
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T10:53:54Z
  default_branch: main
  default_branch_sha: 1514b12a453ecf5eb8133735971aaac106556c31
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:54:17Z
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
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 8.1
        qualifying_issues: 18
        band: relaxed_solo
        window_offset_days: 13
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 70632
        release_assets: 700
        release_tier: D
        signal_basis: releases
    longevity:
      grade: C
      raw:
        repo_age_days: 263
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 64
        top1_share: 0.23
        top3_share: 0.455
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

# Entire

一个 Git 原生 CLI（`entire`），挂进你的 Git 工作流，自动捕获 AI 编码 agent 的会话——提示、回复、工具调用、改动文件、token 用量——并以 checkpoint 形式索引到一条独立的 `entire/checkpoints/v1` 分支上、与你的 commit 并列，从而得到一份可搜索、可回滚的「代码是怎么写出来的」记录。单一 Go 二进制；核心功能完全本地、无需托管账号。

![entire-cli — 健康度雷达](../../../assets/health/entire-cli.zh.svg)

## 何时使用

你是一名开发者（或小团队），在一个 Git 仓库里用各种编码 agent 干真实的功能活——今天 Claude Code，明天 Codex 或 Gemini。代码本身落地没问题，但三周后 review 时有人问「这个重试循环为什么这么写」，答案当初就藏在某段 agent transcript 里，早被压缩掉、灰飞烟灭了。更糟的是，agent 偶尔会把一段会话开到沟里，把几个文件搅乱，这时你巴不得能「回滚到它跑偏之前」，而不必手动去理一棵乱掉的工作树。与此同时，你也不希望这些 AI 记账信息污染你真正的 commit 历史。

于是你在仓库里 `entire enable`，把它对准你的 agent。现在每次会话都通过 Git hooks 自动捕获：提示、回复、工具调用、改动文件和时间戳被 checkpoint（12 位 hex ID）到专用的 `entire/checkpoints/v1` 分支上——你的工作分支保持干净，Entire 绝不在上面提交。会话跑坏时用 `entire session resume <branch>` 恢复到最近一次 checkpoint 的状态；几个月后，解释某个决策的 transcript 仍然索引在那条 commit 旁边。它跨多种 agent、兼容 Git worktree，所以不管哪个工具写的代码，溯源记录都是统一的。

## 何时不用

- **会带敏感提示的公开仓库** —— transcript 是存*在你的 git 仓库里*、落在 `entire/checkpoints/v1` 分支上的；仓库一旦公开，这些数据任何人都能看到。密钥脱敏只是项目自称的「尽力而为（best-effort）」，而且会话中途用的临时 shadow 分支可能含未脱敏数据、绝不能被 push。把它当作一个真实的数据泄露面来对待，而不是装好就不管。
- **pre-1.0 成熟度** —— 最新 release 是 v0.7.7（2026-06）；命令和落盘格式仍可能变（`entire checkpoint rewind` 命令已被标记 deprecated）。当你需要稳定冻结的接口或正式兼容性保证时，它不是合适选择。
- **指望每个 agent/IDE 都能回滚** —— 回滚支持参差不齐：Cursor IDE 据称不支持 rewind，Pi 不支持 subagent 捕获，Copilot 只支持 CLI（不含 VS Code 集成）。依赖它的恢复能力前，先核对你具体用的那个 agent。
- **任务 / 依赖跟踪** —— Entire 是一个*捕获与溯源*层，不是任务图。它记录 agent 做了什么，但不建模哪些工作阻塞哪些、也不给出「就绪」任务——那是另一类工具（[beads](../work-state/beads.zh.md)）。
- **跨仓库 / 全组织审计看板** —— 这份记录是按仓库、git 分支本地、CLI 驱动的。核心工具并不暗示有托管 Web 看板、跨仓库搜索或团队分析视图。
- **非 Git 或非 agent 工作流** —— 整套机制就是 Git hooks + 一条 checkpoints 分支；没有 Git、也没有受支持的 agent 产出会话，就根本没东西可捕获。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [beads](../work-state/beads.zh.md) | ✅ | 需要相邻的任务图/结构化记忆层时，选 beads。 | 解决的是相邻问题：依赖感知的*任务图* / 结构化 agent 记忆（接下来做什么、什么被阻塞），由版本化 SQL 支撑。Entire 捕获的是*已经发生了什么*（transcript/checkpoint）用于溯源与回滚——互补，而非替代。 |
| [CCPM](../work-state/ccpm.zh.md) | ✅ | 需要基于 spec/issue/多 agent 并行的 Claude-Code 项目管理流程时，选 CCPM。 | 一套 Claude-Code 项目管理工作流（基于 GitHub Issues 的 spec/issue/多 agent 并行）。属于流程/协调层，不是会话 transcript 的捕获与回滚层。 |
| 裸 Git + agent 自带的会话日志 | 未收录 | 零额外工具比统一溯源更重要时，选裸 Git 加 agent 自带日志。 | 零额外工具，但 agent 日志按工具各自分散、不与 commit 索引、不可统一回滚，要么乱要么根本进不了仓库。Entire 就是那个统一的捕获/索引层。 |
| Specstory / agent transcript 导出工具 | 未收录 | 导出的聊天记录已经够用时，选 Specstory 或其他 transcript 导出工具。 | 其它工具也能持久化 agent 聊天 transcript，但通常是导出成文件/markdown，而非绑定到 commit 的 Git-checkpoint 溯源、且带回滚机制。替换前先核对功能对齐度。 |
| Reflog / `git stash` + 手动快照 | 未收录 | 原生工作树状态恢复已经够用时，选 reflog、git stash 或手动快照。 | 你本来就有的原生恢复原语，但它们只捕获工作树状态——没有提示/回复/工具调用上下文、没有按会话索引、没有 agent 感知的脱敏。 |

## 技术栈

- Go（按仓库语言统计约 98–99%）—— 以单一二进制 `entire` 分发。
- 以 Git hooks 作为捕获机制；以专用的 `entire/checkpoints/v1` 分支作为会话元数据的存储位置，与代码 commit 分离。
- 12 位 hex checkpoint ID；按 agent 安装 hook。
- 自动摘要据称在 Claude CLI 可用时调用它。
- 分发方式：Homebrew cask（`brew install --cask entire`）、安装脚本（`curl … entire.io/install.sh`）、Scoop（Windows）以及 `go install`。

## 依赖

- **Git** —— 必需；整套捕获模型就是 Git hooks + 一条 checkpoints 分支。
- **一个受支持的 agent** —— claude-code、codex、gemini、opencode、cursor、factoryai-droid、copilot-cli 之一（据 README）；Codex 还需在 `.codex/config.toml` 里设 `codex_hooks = true`。
- **可选** —— Claude CLI 用于自动摘要；`entire login` 设备认证存在但核心功能不需要。Go + `mise` 列在开发依赖里，非运行时依赖。
- 核心本地使用不需要数据库、服务器或托管后端。

## 运维难度

**低。** 装好单一二进制、跑 `entire enable`，捕获就经由 Git hooks 发生，没有要运维的服务——`entire status` / `entire doctor` 管健康，`entire disable` / `entire clean` 退出。真正的运维负担不是基础设施，而是*治理*：因为 transcript 会落到仓库内的一条分支上，你必须决定分支推送/可见性策略、信任 best-effort 脱敏、并避免推送临时 shadow 分支——也就是说，成本在数据处理纪律，而不在部署。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 17.1 小时，基于 35 个 qualifying issues/PRs。
- **维护** —— 截至 2026-06 最后 push 在 2026-06，近期有 release（v0.7.7，2026-06-18）：活跃开发中。据称约 103 个 release，说明有真实的发布节奏——但仍在 1.0 之前，且一个命令（`entire checkpoint rewind`）已被弃用，接口和落盘格式仍可能变。[推断]
- **治理 / 巴士因子** —— `Organization` 所有（`entireio`），比个人仓库是更好的信号，但它仍是个小型厂商主导的项目（有 `entire.io` 安装站和 `entire login` 设备认证，暗示背后有商业方），没有基金会或正式治理。约 4.5k star 不算高，采用仍处早期。[推断]
- **年龄与 Lindy** —— 创建于 2026-01，截至 2026-06 仅数月：太年轻，给不出 Lindy 裁决，且仍在 1.0 之前。请按发布节奏而非履历来评判它。
- **风险旗标** —— `[未验证]` MIT，无重新授权历史。最突出的风险是**数据暴露而非授权**：transcript（提示/回复）存在你 git 仓库*内部*的一条分支上，密钥脱敏只是项目自称的「尽力而为」，且临时 shadow 分支可能含未脱敏数据——在公开仓库上是一个真实的暴露面。

## 存疑（未验证）

- [未验证] star 数约 4.55k（截至 2026-06）—— GitHub star 不可靠且对日期敏感，仅供参考。
- [未验证] 语言占比（约 98.6% Go）与「103 个 release」这一数字取自抓取时的 repo/README，未独立复核。
- [未验证] 各 agent 的回滚缺口（Cursor 无 rewind、Pi 无 subagent 捕获、Copilot 仅 CLI）来自项目自己的 README；行为可能随版本变化——请对照你的 agent/版本核实。
- [未验证] 密钥脱敏是项目自称的「best-effort」；覆盖范围与失效模式未经独立审计。公开仓库下不要当作保证。
- [推断] Entire 与 beads 这类任务图工具解决的是不同层（溯源/回滚 vs 任务状态）；「互补而非替代」是推理，不是经过验证的集成。
- [未验证] 未收录替代项的对比行（Specstory 式导出工具、通用 transcript 工具）基于品类常识描述，未做逐功能审计。
