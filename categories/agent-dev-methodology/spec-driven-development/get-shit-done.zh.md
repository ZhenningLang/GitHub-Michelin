---
name: Get Shit Done (GSD)
slug: get-shit-done
repo: https://github.com/gsd-build/get-shit-done
category: spec-driven-development
tags: [spec-driven, context-engineering, meta-prompting, claude-code, subagents, phase-workflow, multi-runtime]
language: JavaScript
license: MIT
maturity: GitHub release v1.42.3 (2026-05); main README now redirects to open-gsd/gsd-core (as of 2026-06)
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-05-31T17:46:54Z
  default_branch: main
  default_branch_sha: bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815
  archived: true
health:
  schema: 1
  computed_at: 2026-09-22T17:29:32Z
  overall: D
  overall_score: 1.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: true
        last_commit_age_days: 114
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: E
      raw:
        median_ttfr_hours: null
        qualifying_issues: 0
        band: default
        window_offset_days: 10
    adoption:
      grade: D
      raw:
        registry: npmjs.org
        canonical_package: get-shit-done-cc
        dependent_repos_count: 0
        downloads_last_month: 47093
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
        release_downloads: 69
        release_assets: 3
        release_tier: D
        signal_basis: releases
        tier_source: registry
        archived: true
    longevity:
      grade: E
      raw:
        repo_age_days: 282
        last_commit_age_days: 114
        cohort: framework
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 97
        top1_share: 0.454
        top3_share: 0.873
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

# Get Shit Done (GSD)

面向 coding agent 的规格驱动 + 上下文工程工作流：把一个模糊的想法变成 PROJECT/ROADMAP/CONTEXT/PLAN 文档，再让每个阶段在全新的上下文窗口里、由编排好的子代理执行，以对抗 context rot（上下文劣化）。

![get-shit-done — 健康度雷达](../../../assets/health/get-shit-done.zh.svg)

## 何时使用

你是个独立开发者或小团队，靠 agent（Claude Code、OpenCode、Codex、Gemini、Cursor 等）写代码而不是亲手写。你大概率踩过那个经典坑：你描述一个功能，agent 一口气吐出一大坨代码，前几轮质量还行，随着上下文窗口被历史填满逐步劣化——到最后它一脸自信地产出规模一上来就散架的垃圾。你又不想要 BMAD/SpecKit 那种企业仪式（冲刺、故事点、Jira），只想让模型真的理解你在做什么并可靠地交付。GSD 给你装上几个 slash 命令（`/gsd-new-project`、`/gsd-discuss-phase`、`/gsd-plan-phase`、`/gsd-execute-phase`、`/gsd-verify-work`、`/gsd-ship`），带你从访谈 → 调研 → 路线图 → 每阶段上下文 → 原子化计划 → wave 并行执行一路走完，状态全部落在 markdown 里（`PROJECT.md`、`ROADMAP.md`、`STATE.md`、`{phase}-CONTEXT.md`、`{phase}-PLAN.md`）。

它的核心赌注是结构性的：每份原子计划都小到能在自己干净的 20 万 token 窗口里跑，因此实现阶段不会继承一段已经劣化的对话；每个任务单独提交，git 历史保持可审计。如果你想要一个有审批检查点的可复现构建循环（你审路线图、在写任何代码前先塑造每个阶段的 CONTEXT、再做一遍引导式 UAT），并且你以 skip-permissions / 自主模式跑 agent、希望护栏内建在提示里而不是每次临时发挥，那它很合适。

## 何时不用

- **你想要一套极薄、完全自己掌控的提示。** GSD 是个庞大且迭代飞快的系统（`agents/` 里几十个子代理、一个会构建的 TypeScript SDK、覆盖约 13 个运行时的安装逻辑）。如果你想读懂并掌控每一条提示，手写一份小巧的 `CLAUDE.md` 加几个命令更可读。
- **你不信任该项目的治理 / 延续性。** 正统的 `main` README 如今只是一条重定向通知，指向*另一个* org 的仓库（`open-gsd/gsd-core`），而 GitHub 仍报告该仓库未归档、`package.json` 又停在一个领先于最近 tag 发布的 canary 版本——这种割裂的“精神分裂”状态暗示着一次进行中的搬迁/分叉。[推断] 在依赖它之前，先 pin 一个版本并观察开发实际落在哪里。
- **你需要确定性的、非 LLM 的构建编排。** GSD 的“验证”和“wave 执行”是 agent 驱动的提示工作流，不是 CI/构建引擎。[未验证] 其行为随模型和运行时变化，不保证 run-to-run 可复现。
- **你在不受支持或较旧的运行时 / 极小上下文预算下工作。** 它面向特定的几款 agent CLI；默认安装会带来数千 token 的系统提示开销（有 `--minimal` 档，但满血用法假定你跑的是有大上下文、且以 skip-permissions 模式运行的 agent）。
- **加密货币关联对你是红线。** README 显眼地挂着一个 `$GSD` Solana 代币。框架本身是 MIT、不用代币也能用，但如果“和 memecoin 沾边”对你的组织是不可接受的，请把这点纳入考量。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [SuperClaude Framework](../coding-agent-harnesses/superclaude.zh.md) | ✅ | 需要 persona/命令/MCP 框架来重塑单个 agent 行为时，选 SuperClaude Framework。 | persona/命令/MCP 框架，重塑单个 agent 的行为；GSD 更像一条线性的阶段流水线（discuss→plan→execute→verify），配大量子代理 fan-out 和持久化的 spec 文档。 |
| [Superpowers](../coding-agent-harnesses/superpowers.zh.md) | ✅ | 需要广覆盖、可按需组合的 skills/plugin 库时，选 Superpowers。 | 一个广覆盖、可按需组合的 skills/plugin 库；GSD 是一条有主见的端到端项目循环，而非能力大杂烩。 |
| [Compound Engineering](../coding-agent-harnesses/compound-engineering.zh.md) | ✅ | 需要把“agent 反过来改进系统”的复利理念编码进 plugin 时，选 Compound Engineering。 | 把“agent 反过来改进系统”这一复利理念编码进 plugin；规格驱动目标有重叠，面比 GSD 的整条工具链更轻。 |
| [12-Factor Agents](12-factor-agents.zh.md) | ✅ | 需要构建可靠 agent 的原则，而不是可安装命令集时，选 12-Factor Agents。 | 关于如何构建可靠 agent 的原则/方法论文档，不是可安装的命令集；读它看*为什么*，用 GSD 拿可执行的*怎么做*。 |
| [ECC](../coding-agent-harnesses/ecc.zh.md) | ✅ | 需要同类 agent 开发方法论，但想对比另一种编排模型时，选 ECC。 | 同类的 agent 开发方法论，编排模型不同；可直接对比阶段/上下文的处理方式。 |
| [Spec Kit](spec-kit.zh.md) | ✅ | 需要厂商背书的规格驱动工具包（`/specify`、`/plan`、`/tasks`）时，选 Spec Kit。 | 厂商背书的规格驱动工具包（`/specify`、`/plan`、`/tasks`）；GSD 自我定位更轻、更聚焦上下文工程、仪式更少。 |
| [BMAD-METHOD](bmad-method.zh.md) | ✅ | 需要带显式 PM/架构/开发/QA 角色的敏捷 agent 框架时，选 BMAD-METHOD。 | 带显式角色（PM/架构/开发/QA）的敏捷 agent 框架；那种“运营一家软件公司”的更重框架，正是 GSD 刻意拒绝的。 |

## 技术栈

- **语言：** JavaScript（约 73%）+ TypeScript（约 26%）+ Shell（仓库语言统计，2026-06）。
- **分发：** npm 包 `get-shit-done-cc`；安装器 CLI `bin/install.js`（还暴露 `gsd-sdk` / `gsd-tools` 命令）。
- **SDK:** 一个 TypeScript `sdk/` 包（经 `npm run build:sdk` 构建），提供 query/state 工具与各类 freshness 检查；hooks 经 `scripts/build-hooks.js` 生成。
- **安装产物：** slash 命令 / skills（`commands/`，在较新 Claude Code 和 Codex 上以 `skills/gsd-*/SKILL.md` 形式发出）、子代理（`agents/gsd-*.md`）、hooks，以及运行时专属配置（如 Cline 的 `.clinerules`）。
- **目标运行时：** Claude Code、OpenCode、Gemini CLI、Kilo、Codex、Copilot、Cursor、Windsurf、Antigravity、Augment、Trae、CodeBuddy、Cline（依 README 安装矩阵）。
- **状态模型：** 纯 markdown SSOT 文档（`PROJECT.md`、`REQUIREMENTS.md`、`ROADMAP.md`、`STATE.md`，以及每阶段的 `CONTEXT/RESEARCH/PLAN/SUMMARY/VERIFICATION/UAT`），置于 `.planning/` 目录树下。

## 依赖

- **运行时：** Node.js ≥ 22（依 `package.json` `engines`）以运行安装器与 SDK；支持 Mac/Windows/Linux。
- **一个 agent CLI:** 运行期需要上面列出的某款受支持 coding agent——GSD 是提示/编排层，真正干活的是 agent。
- **npm 依赖：** `@anthropic-ai/claude-agent-sdk`、`ws`；可选 `fallow`;dev/测试用 `c8`/`vitest`。
- **安装：** `npx get-shit-done-cc@latest`（交互式选运行时 + 全局/本地），或非交互 flag 如 `npx get-shit-done-cc --claude --global`。
- **推荐模式：** 文档建议把 Claude Code 以 `--dangerously-skip-permissions` 运行（或配一份精挑的 `allow` 列表），以获得无摩擦的自主性。

## 运维难度

**低到中。** 首日安装就是一行 `npx`，产物只是丢进 agent 配置目录的文件——没有服务、没有数据库。“中”来自把它用好：以 skip-permissions 模式跑 agent（这是个真实的 blast-radius 决策）、每阶段的纪律（你得真的去填 `CONTEXT.md` 才能拿到好输出，而不是吃默认值）、跟上飞快的发版节奏，以及——当下最尖锐的——盯紧仓库搬迁，确保你装的是仍在维护的源。[未验证] token/系统提示开销和具体运行时行为随 agent 和版本而变。

## 健康度与可持续性

- **响应速度**：Grade E。
- **维护（2026-06）：** 事实行显示截至本次核验，`gsd-build/get-shit-done` 仓库已**归档（archived=true）**，最后 push 在 2026-05——而 `main` 的 README 现在是一条指向*另一个* org（`open-gsd/gsd-core`）的重定向。把这个仓库读作**已冻结/已搬迁**：开发似乎已转移（或分叉）到别处，当下的事实源很可能已不在这个 URL——安装前请先确认。
- **治理与延续性：** Organization 持有（gsd-build），但「重定向 + 归档」的割裂状态暗示一次进行中的 org 迁移/分叉，而非稳定的托管。这是一个**延续性红旗**：谁掌控路线图、release 落在哪里，当前都不明确。
- **年龄与 Lindy（2026-06）：** 创建于 2025-12，约 6 个月——而正统仓库已经归档。Lindy 裁决：**在这个 URL 上不满足先验**——「年轻*且*在此已弃」是最差象限；任何可持续性现已完全寄于后继仓库（`open-gsd/gsd-core`），需对其单独评估。
- **风险标记：** 归档/重定向的「精神分裂」是首要风险（从一个已死的源安装）。其次：README 的 `$GSD` Solana 代币品牌——MIT 软件不用代币也能用，但对某些组织而言，memecoin 关联是治理/观感上的标记。未审 CVE。

## 存疑（未验证）

- [未验证] GitHub star 数（截至 2026-06 约 64.5k）——star 数不可靠且对时间敏感，仅供参考。
- [未验证] GitHub 最新 tag 发布是 v1.42.3(2026-05-16)，而 `package.json` 显示 `1.50.0-canary.0`;npm 上的 "latest" 可能与二者都不同——依赖某功能前请核实实际装上的版本。
- [推断] `main` README 是一条指向 `open-gsd/gsd-core` 的重定向 stub，而 GitHub 又报告该仓库未归档，这暗示一次进行中的搬迁或分叉；单凭元数据并不能完全看清哪个 org/仓库才是当下的事实源。
- [未验证] 受支持运行时列表、命令名和子代理清单取自仓库自带 README/目录树，随版本变动；请针对你的运行时对照当前源核实。
- [未验证] “fresh-context-per-plan 设计能对抗 context rot 并产出更好结果”这一说法是项目自己的表述加第三方证言；此处未做独立基准验证。LLM 行为不作保证。
- [未验证] README 中引用的 `$GSD` Solana 代币与项目品牌相关联；它与这套 MIT 许可软件之间的关系（治理、资金）在所审材料中未作说明。
