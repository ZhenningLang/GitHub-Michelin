---
name: Ralph for Claude Code
slug: ralph-claude-code
repo: https://github.com/frankbria/ralph-claude-code
category: work-state
tags: [autonomous-loop, claude-code, ralph-technique, exit-detection, bash, circuit-breaker, rate-limiting, tmux-monitor, prd-import, single-provider]
language: Shell
license: MIT
maturity: v0.11.x line per README, active as of 2026-06; no tagged GitHub releases (see caveats)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-20T02:33:03Z
  default_branch: main
  default_branch_sha: 0c1d7bf8395ceb669482c3443162e2cf381f2040
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:24:44Z
  overall: B
  overall_score: 2.67
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 17
        active_weeks_13: 6
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.1
        qualifying_issues: 30
        band: relaxed_solo
        window_offset_days: 2
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: C
      raw:
        repo_age_days: 310
        last_commit_age_days: 17
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 23
        top1_share: 0.726
        top3_share: 0.872
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

# Ralph for Claude Code

一个把 Claude Code CLI 包进自治「Ralph」循环的 Bash 套壳：反复以 `.ralph/PROMPT.md` 为输入重新调用 Claude，直到双条件退出闸门触发；配速率限制、熔断器和 tmux 监控面板，避免循环失控或无止境烧 token。

![ralph-claude-code — 健康度雷达](../../../assets/health/ralph-claude-code.zh.svg)

## 何时使用

你是一名开发者，手上有一份范围清晰的待办——一份 `fix_plan.md` 清单，或一份能转成清单的 PRD——你想让 Claude Code 无人值守地把它们一条条啃完，而不是自己守着一个个 prompt。你试过朴素的「不停说 continue」循环，结果撞上两种失败：要么 Claude 提前宣布胜利（「Phase complete!」）却还有活没干就停了，要么它根本不停，等你醒来 API 预算已耗尽、而那个本该跳闸的熔断器并不存在。你想要 Geoffrey Huntley 那套 Ralph 技法的自治性，又不想自己手搓安全护栏。

于是你在仓库里 `ralph-enable`（或 `ralph-import requirements.md`），把目标写进 `.ralph/PROMPT.md`、任务写进 `.ralph/fix_plan.md`，然后跑 `ralph --monitor`。套壳循环 Claude Code，而它的退出闸门只有在「启发式完成信号」和显式 `EXIT_SIGNAL: true` 同时成立时才触发——所以「Phase complete, moving on」配上 `EXIT_SIGNAL: false` 会继续干。与此同时 tmux 面板显示循环计数、API 调用数 vs 你设的每小时上限、以及熔断器状态；熔断器在连续 3 次无进展或 5 次相同报错后打开；速率限制（默认 100 次/小时）和单循环超时把成本框住。Git 备份分支（`--backup` / `--rollback`）给你一个撤销键，如果不想让它碰宿主机，还能把它接进 Docker 或 E2B 沙箱。

## 何时不用

- **绑死 Claude Code 这一家。** 它是专门套在 Anthropic `claude` CLI 上的壳，当下没有发布任何模型/供应商抽象（README 把多供应商列为 1.0 *之前的计划项*）。你若用 GPT/Gemini/本地 agent，这套壳驱动不了它们。
- **你还没有结构化计划。** Ralph 执行的是 `fix_plan.md` 清单；它是*循环驱动器*，不是规划器、也不是任务图。目标含糊只会换来含糊的自治空转。请把它和真正的任务存储（见 [beads](beads.zh.md)）或规划工作流配对使用。
- **成本敏感 / 只接受人工监督的团队。** 它的设计就是无人值守地大量调用 Claude API，花费随循环数和模型放大。速率限制和熔断器能框住，但若团队要求每个循环都有人盯着，这套自动化对你价值有限。
- **Windows 原生 / 无 Bash 环境。** 它需要 Bash 4.0+、`jq`、`git`、GNU coreutils（macOS 上的 `gtimeout`），面板还要 tmux。这是一个 Unix shell 套壳，不是可移植的二进制。
- **并行 / 高吞吐任务。** 队列条目一次只处理一条，没有并发多 agent 执行。它是串行保姆，不是机群调度器。
- **对成熟度敏感的场景。** 1.0 之前、单维护者主导、GitHub 上无任何 release tag——版本号来自仓库内/README 文本。v0.10 已经把全部文件挪进 `.ralph/`（一次需要 `ralph-migrate` 的破坏性布局变更）；预期 flag 和布局还会继续变。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [beads](beads.zh.md) | ✅ | 需要持久化、带依赖关系的“该做什么”任务图时，选 beads。 | 一个持久化、带依赖关系的*任务图*（「该做什么」的存储）；Ralph 是「把它做掉的循环」。互补——Ralph 甚至能导入 beads 任务——而非互斥。 |
| [CCPM](ccpm.zh.md) | ✅ | 需要 Claude Code 之上的 spec/PRD 驱动项目管理时，选 CCPM。 | 在 Claude Code 之上做 spec/PRD 驱动的项目管理，带 GitHub issue 工作流；偏重规划结构，而非 Ralph 那种带熔断器+速率限制的硬化无人值守跑循环。 |
| [Entire](../session-history/entire-cli.zh.md) | ✅ | 需要更宽的 agent 工作流 CLI 时，选 Entire。 | 一个更宽的 agent 工作流 CLI；在「驱动 agent」上有重叠，但编排模型与 Ralph 的单 prompt Bash 循环不同。 |
| [Context Mode](context-mode.zh.md) | ✅ | 需要上下文/记忆塑形而不是自治完成循环时，选 Context Mode。 | 聚焦于为 agent 塑形上下文/记忆，而非带退出检测的自治完成循环。 |
| Geoffrey Huntley 的原版 Ralph(`while :; claude -p ...`) | 未收录 | 只需要一行 shell 循环原始技法时，选 Geoffrey Huntley 的原版 Ralph。 | 原始技法就是一行 shell 循环；本项目是那个想法加上退出闸门、速率限制、熔断器、监控、备份、沙箱——即裸循环缺的那层安全脚手架。 |
| Aider `--auto` / [OpenHands](../../agent-frameworks/coding-agents/orchestration-and-review/openhands.zh.md) / [SWE-agent](../../agent-frameworks/coding-agents/orchestration-and-review/swe-agent.zh.md) | 部分已收录 | 需要自带循环的通用自治编码 agent 时，选 Aider、OpenHands 或 SWE-agent。 | 自带模型/循环的通用自治编码 agent；不是 Claude-Code-CLI 套壳，也不围绕双条件 `EXIT_SIGNAL` 闸门构建。 |

## 技术栈

- **语言：** Shell / Bash(4.0+)——套壳是一组 shell 脚本（`ralph`、`ralph-monitor`、`ralph-setup`、`ralph-import`、`ralph-queue`、`ralph-enable`、`ralph-migrate`）。
- **驱动对象：** Claude Code CLI(`claude`)，每个循环带项目 prompt 调用一次；JSON 输出格式，失败回退到文本。
- **状态：** `.ralph/` 下的纯文件——`PROMPT.md`、`fix_plan.md`、`AGENT.md`、`status.json`、`.ralph_session`、`logs/ralph.log`（轮转）、`logs/metrics.jsonl`。
- **工具链：** `jq`(JSON)、`git`（备份分支 / 用 commit 数判断进展）、`tmux`（分屏监控）、GNU coreutils `timeout`/`gtimeout`。
- **可选执行环境：** Docker 与 E2B 云沙箱；`gh` CLI 用于 GitHub issue 导入；BATS 用于项目自身的测试套件。

## 依赖

- **必需运行时：** Bash 4.0+（README 提到带 3.x 兼容垫片）、Claude Code CLI（`npm i -g @anthropic-ai/claude-code` 或 npx）、`git`、`jq`、提供 `timeout` 的 GNU coreutils（macOS 上 `brew install coreutils` → `gtimeout`）。
- **推荐：** `tmux`，用于实时监控面板。
- **可选：** `gh`（GitHub CLI）做 issue 导入/生命周期；Docker 做容器沙箱；E2B SDK（`pip install e2b`）做云沙箱运行。
- **一个 Anthropic 账号 / Claude Code 访问权**及 API 预算——循环的全部工作就是反复调用它。

## 运维难度

**低到中。** 安装是 `git clone` + `./install.sh`，装好一批全局命令；单项目层面是 `ralph-enable` 向导或 PRD 导入，顺利时你跑 `ralph --monitor` 看着即可。难度上升的原因：你得保证 Unix 工具链齐全且正确（Bash 版本、`jq`、macOS 上的 coreutils `gtimeout`、tmux）；安全旋钮（`--calls`、`--timeout`、熔断阈值）要你自己按成本容忍度调；`.ralph/` 文件布局和 CLI flag 跨版本变过（v0.10 的破坏性迁移需要 `ralph-migrate`）；无人值守跑起来你仍要盯预算、沙箱成本告警和偶发卡死的循环。让它不进沙箱直接碰真仓库是主要风险——备份分支和 `--rollback` 存在，正是因为自治循环可能把现场弄乱。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 0.1 小时，基于 30 个 qualifying issues/PRs。
- **维护** —— 截至 2026-06 最后 push 在 2026-06，处于 v0.11.x 线，即活跃推进，但**没有任何 GitHub release tag**——版本号来自仓库内 README 文本，而非已发布制品。v0.10 已经把全部文件挪进 `.ralph/`（一次需要 `ralph-migrate` 的破坏性布局变更），所以预期 flag / 布局还会继续变。[推断]
- **治理 / 巴士因子** —— `[推断]` 单维护者、`User` 所有的仓库（`frankbria`）；无 release，无团队或基金会。一人维护的套壳却有约 9.5k star，是巴士因子警示——对你无法重新改造的东西，弃坑与 flag / 布局漂移风险不可忽视。
- **年龄与 Lindy** —— 创建于 2025-08，截至 2026-06 不足一年且仍在 1.0 之前：太年轻，给不出 Lindy 裁决。它封装的是一套已成型的*技法*（Geoffrey Huntley 的 Ralph 循环），但这个具体套壳在长寿上未经检验。
- **风险旗标** —— `[未验证]` MIT，无重新授权历史。结构性风险是**供应商锁定**：它专门套在 Anthropic 的 `claude` CLI 上（多供应商是 1.0 前的*计划项*，尚未交付）。运维上它会无人值守地大量发起付费 API 调用，所以成本失控是真实风险——熔断器和速率限制是仅有的护栏。

## 存疑（未验证）

- [未验证] **没有 GitHub release tag。** `gh repo view` 返回 `latestRelease: null`,Releases 页面写着「There aren't any releases here」。「v0.11.5」/「v0.11.x」版本及整份 changelog（784 个测试、双条件闸门修复等）都来自仓库内 README 文本，而非已发布的 release 制品——版本细节当作仓库自报。
- [未验证] **Star 数约 9.5k**（gh 在 2026-06-26 报 9,464）。该生态的 GitHub star 不可靠且随时间变化，仅作参考。
- [推断] **单维护者 / 1.0 前的不稳定。** 以 owner 命名的仓库、无 release、一次有记录的破坏性 `.ralph/` 布局迁移，加上 README 里 bash-3.x 和误报修复的记录，显示出活跃但不稳定的接口面；对你无法重新改造的东西，弃坑与 flag/布局漂移风险不可忽视。
- [未验证] **安全闸门的确切行为**——双条件退出（`completion_indicators >= 2` 且 `EXIT_SIGNAL: true`）、熔断阈值（3 次无进展 / 5 次相同报错）、默认 100 次/小时、以及 5 小时 API 上限检测，全部来自 README；此处未独立验证，且 LLM 驱动的完成启发式本质上是尽力而为，并非有保证的行为。
- [推断] **多供应商支持是愿景。** README 把供应商抽象列为 1.0 之前的计划项；截至本次核验，它仍是仅支持 Claude-Code-CLI 的套壳。
- [未验证] **Docker/E2B 成本控制**（`--sandbox-max-cost`、`--sandbox-cost-alert`）与「无并行处理」限制是 README 所述，未经独立确认。
