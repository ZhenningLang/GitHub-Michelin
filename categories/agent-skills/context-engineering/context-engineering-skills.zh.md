---
name: Agent Skills for Context Engineering
slug: context-engineering-skills
repo: https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering
category: context-engineering
tags: [skills, context-engineering, multi-agent, memory, evaluation, harness-engineering, claude-code, plugin]
language: Python
license: MIT
maturity: v2.3.0, active (2026-05)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-05-26T05:36:56Z
  default_branch: main
  default_branch_sha: 25e1fa79a33f0985793bcab3c64dde8d020c5132
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:43:30Z
  overall: B
  overall_score: 2.6
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 43
        active_weeks_13: 5
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 124
        release_assets: 4
        release_tier: D
        signal_basis: releases
    longevity:
      grade: B
      raw:
        repo_age_days: 276
        last_commit_age_days: 43
        cohort: skill-pack
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 11
        top1_share: 0.744
        top3_share: 0.95
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
---

# Agent Skills for Context Engineering

一个 15 个 skill 的插件包，给 coding agent 灌输「上下文工程」（context engineering，管理进入上下文窗口的内容）的纪律，覆盖基础原理、退化、压缩、多 agent 协同、记忆、工具设计、评估与 harness 工程。

![context-engineering-skills — 健康度雷达](../../../assets/health/context-engineering-skills.zh.svg)

## 何时使用

你是搭多 agent 或长跑 agent 系统的工程师，而你的 run 总因为上下文问题崩掉：窗口被陈旧的工具输出塞满、agent 在任务中途「忘掉」早先的决策、子 agent 拿到了错误的状态切片、或者检索把太多内容灌进 prompt 反而拉低了质量。你大致知道这*是*个上下文问题，但没有一套词汇或清单来判断自己落在哪种 failure mode、该怎么修。这个包给你的 agent 一组按需加载的 skill —— `context-fundamentals`、`context-degradation`、`context-compression`、`context-optimization`、`multi-agent-patterns`、`memory-systems`、`tool-design`、`filesystem-context`、`hosted-agents`、`evaluation`、`advanced-evaluation`、`harness-engineering`、`latent-briefing`、`project-development`、`bdi-mental-states` —— 每个都带一份 `SKILL.md` 外加可运行脚本和参考文档，任务触及哪个领域，agent 就加载对应那个。

当你想要一套现成、有主见的语料，而不是从零自己写上下文管理 skill 时，你会选它；尤其当你主要在 Claude Code 里工作（本包通过自带的 marketplace 清单以插件方式安装：`/plugin marketplace add … && /plugin install context-engineering@context-engineering-marketplace`）。单个 skill 文件夹也可以手动拷进 `.claude/skills/`；README 还声称通过 Open Plugins 标准支持 Cursor，所以同一套语料能跨这些 harness 跟着你走。[推断]

## 何时不用

- **你已经在维护自己的上下文 / 记忆 skill 栈。** 这个包又广又有主见（15 个 skill 各有自己的路由）。把它叠在既有的精选体系上，会在压缩、记忆、多 agent 模式上引入重叠、冲突的指导 —— 选一个事实源，别双路由。
- **你不在受支持的 harness 上。** 激活依赖插件 / skill 加载器。它首先是为 Claude Code 构建的（插件 marketplace 清单）；Cursor 支持是 README 声称的 Open Plugins 路径。在自研或不受支持的 agent 上没有加载器来触发这些 skill，光有 markdown 不会自动激活。
- **你要的是可运行的库 / CLI。** 这是塑造行为的 skill 语料，不是你能 `import` 的包。自带脚本是演示和 benchmark，不是产品 API；脱离支持它的 agent，这些 skill 什么都不做。
- **是建议，不是强制。** 行为都活在 agent 自行选择加载并遵循的 prompt / markdown skill 里。没有运行时去强制正确的上下文处理 —— agent 仍可能忽略某个 skill 或路由错。
- **你需要一份稳定、冻结的规范。** 单人维护、迭代快（v2.x，版本间有 router benchmark 和「语料硬化」）。skill 名称、数量、路由会随版本变化；若依赖某个 skill 的具体行为，请 pin 到某个 tag。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [notebooklm-skill](notebooklm-skill.zh.md) | ✅ | 只需要 NotebookLM 式文档接地的单个窄 skill 时，选 notebooklm-skill。 | 同 leaf 的兄弟项，但它是单个窄 skill（NotebookLM 式的文档接地），而非广义的上下文工程语料。要单一能力选它；要整套上下文管理方法论选本包。 |
| [Superpowers](../../agent-dev-methodology/coding-agent-harnesses/superpowers.zh.md) | ✅ | 需要完整 SDLC 方法论（brainstorm→plan→TDD→verify）skill 插件时，选 Superpowers。 | 把完整 SDLC 方法论（brainstorm→plan→TDD→verify）做成 skill 插件；在「安装一套精选 skill 包」这一形态上重叠，但它针对的是*软件开发循环*，不是上下文窗口工程。互补而非替代。 |
| Anthropic 自家的上下文工程指南 / 内置 skill | 未收录 | 需要平台第一方文档与原生 skill 时，选 Anthropic 自家指南或内置能力。 | 平台第一方文档与原生 skill；本包是叠在其上的第三方语料，可能与原生指导重复或冲突，需要自行调和。 |
| 自己仓库里手写的上下文 / 记忆 skill | 未收录 | 需要最高贴合度和零锁定、且愿意自行维护时，选手写 skill。 | 贴合度最高、零锁定，但一切都得你自己写自己维护。本包以一定贴合度换一套现成、跑过 benchmark 的语料。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护（2026-06）：** 活跃——最新 release v2.3.0（2026-05），最后 push 于 2026-05，未归档，版本间有「语料硬化」和 router benchmark 工作。迭代够快，以至 skill 名称/数量/路由会随版本变化。
- **治理 / bus factor：** 这是一个**单人维护、`User` 所有**的仓库（`muratcankoylan`），却背着约 16k stars——这种「人气 vs bus factor」的错配是一个真实的脆弱信号：高 star 的个人仓库一旦作者离开，没有团队或组织来接续。`[推断]`
- **年龄与 Lindy 判断：** 年轻（创建于 2025-12，约半岁）且踩在 2026 年 skill-pack 的热潮上——在 Lindy 维度上**未经验证**。它是一套建议语料、不是承重的运行时，所以它过时的下行风险比库要低，但不要把它的存续性当成已成立。
- **风险旗标：** 仅建议性（agent 可忽略的 prompt/markdown）、激活以 Claude Code 优先（Cursor 支持是 README 声称的）、benchmark 数字为自报——均未独立验证。skill 语料没有 relicense/CVE 之忧，但为可复现请 pin 一个 tag。

## 存疑（未验证）

- [未验证] 元数据（GitHub，截至 2026-06-26）：最新 release v2.3.0（发布于 2026-05-22）、最后 push 2026-05-26、license MIT、主语言 Python、未归档。依赖某个具体版本行为前请重新核验。
- [未验证] star 数（GitHub 2026-06-26 约 16.8k）不可靠且对日期敏感；仅作参考，不作质量信号。
- [未验证] 本次核查时仓库实树为 `skills/` 下 15 个 skill（每个含 `SKILL.md` + `scripts/` + `references/`）；名称和数量随版本变化，请读当前 `skills/` 目录而非信这份清单。
- [未验证] Cursor / Open-Plugins 支持及跨 harness 激活声明来自 README；在 Claude Code 之外的实际激活保真度此处未独立确认。
- [未验证] router benchmark 数据（多前沿模型上的 skill 激活准确率、「skill health 0.9117」）是 README/CHANGELOG 中项目自报的数字，未经独立复现。
- [推断] 因为行为是 agent 加载的 prompt / markdown，强制力是建议性的 ——「模式」是指令而非硬运行时保证；agent 仍可能偏离。
