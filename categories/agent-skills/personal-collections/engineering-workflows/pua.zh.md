---
name: PUA
slug: pua
repo: https://github.com/tanweai/pua
category: engineering-workflows
tags: [skill-pack, persistence, debugging, high-agency, claude-code, multi-harness]
language: TypeScript
license: MIT
maturity: v3.5.0, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-17T15:15:16Z
  default_branch: main
  default_branch_sha: d602b75218600aa9063fb2464e22be81388c6e68
  archived: false
health:
  schema: 1
  computed_at: 2026-09-23T07:34:49Z
  overall: C
  overall_score: 1.75
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 14
        active_weeks_13: 4
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 71
        release_assets: 4
        release_tier: D
        signal_basis: releases
    longevity:
      grade: C
      raw:
        repo_age_days: 199
        last_commit_age_days: 14
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 11
        top1_share: 0.832
        top3_share: 0.936
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: type_na }
    risk_license: { reason: license_declared_unverifiable }
---

# PUA

一个高能动性人设 skill 包：把你的 coding agent 设定成「被放进 30 天 PIP 的 P8 工程师」，用「职场 PUA / PIP」话术逼它穷尽排查手段，而不是早早放弃。

![pua — 健康度雷达](../../../../assets/health/pua.zh.svg)

## 何时使用

你是一名在跑 Claude Code（或 Codex CLI、Cursor、Kiro、OpenCode……）的开发者，而你的 agent 总是太早投降：报错两次就耸耸肩说「这是已知限制」然后停手——或者根本没重跑那条失败命令，就宣称已经修好了。你希望它像个倔强的资深工程师那样，在真正穷尽所有路径之前把「我做不到」当作不可接受。PUA 装上一套人设，把 agent 重塑为「曾被寄予厚望、如今进了绩效改进计划的 P8」，并随失败累积逐级加压：L0 正常 → L1「换一个根本不同的思路」→ L2「搜索 + 读源码 + 提三个假设」→ L3「完成 7 点检查清单」→ L4「绝望模式」。叠在上面的是「三条红线」（不许虚报完成、用工具核实事实、放弃前先穷尽方案）以及方法论路由：挑一种排查策略，失败重复时轮换。

当你宁可采用一套有主张、带戏剧化的「坚持」覆盖层，也不想自己手写「别放弃」式提示时，就会用它；尤其当你希望这种推力能跨 harness 跟着你走。仓库为各平台分别打包了资产（Claude Code 插件、Codex skills、Cursor `.mdc` 规则、Kiro steering、VSCode/Copilot 指令，以及 `/pua:p7`、`/pua:p9`、`/pua:p10`、`/pua:yes`、`/pua:mama` 等人设变体）。在 Claude Code 上它不止于纯提示：v3 实现接了 `SessionStart` / `PostToolUse` / `UserPromptSubmit` 钩子来注入上下文，比纯提示文本更确定。[推断]

## 何时不用

- **你已经有一套「坚持 / 排查」纪律。** 如果你的栈里已经强制 verification-before-completion、系统化排查，或「没证据不许声称完成」（很多精选 skill 系统都有），PUA 的三条红线会重叠，它的人设提示会和你的双重路由或互相打架。只留一个事实源。
- **你要的是强制，而不是氛围。** 在 Claude Code 钩子路径之外，这套人设就是提示注入——agent 可以无视「L4 绝望模式」，就像它无视任何指令一样。它提高坚持的概率，但不强制坚持。
- **「PUA」这个框架本身让你无法接受。** 整个卖点就是心理施压话术（中式职场管理 + 西方 PIP 文化）。如果你反感这种调性、想要中性语气，或要给别人配 agent，那么主题本身就是产品，无法干净地剥掉。
- **你不在受支持的 harness 上。** 激活依赖各平台的加载器（Claude `Skill`/插件、Codex skills、Cursor 规则、Kiro steering）。在自研或不受支持的 agent 上，markdown 本身什么都不做。
- **单人维护、迭代快、主题厚重。** 频繁发版（v3.x），行为烤进人设提示；一次版本升级可能改掉加压逻辑或某些「味道」。建议锁版本，升级后复查。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [antfu/skills](antfu-skills.zh.md) | ✅ | 需要广谱工具型个人 skill 合集，而不是“坚持”人设覆盖层时，选 antfu/skills。 | 一位维护者的个人通用 skill 合集；偏广谱工具型 skill，没有人设 / 加压主题。PUA 是单一目的：只加一层「坚持」人设，不是工具箱。 |
| [awesome-claude-code-subagents](../../subagent-collections/awesome-claude-code-subagents.zh.md) | ✅ | 需要按角色分发任务的专家目录时，选 awesome-claude-code-subagents。 | 一个庞大的按角色分发任务的 subagent 目录。PUA 不是专家名册——它是改变单个 agent「怎么坚持」的行为覆盖层。 |
| [Superpowers](../../../agent-dev-methodology/coding-agent-harnesses/superpowers.zh.md) | ✅ | 需要完整 brainstorm→plan→TDD→verify SDLC 方法论包时，选 Superpowers。 | 完整的 brainstorm→plan→TDD→verify SDLC 方法论包；其 `verification-before-completion` / `systematic-debugging` 与 PUA 的红线重叠，但交付的是整套生命周期，而 PUA 只是带人设外皮的「坚持 / 反放弃」层。 |
| 平台内置 skills / 原生 slash 命令 | 未收录 | 优先使用平台维护的原生 skill 面时，选内置 slash 命令。 | 平台自身的 skill 面；PUA 是叠在上面的第三方人设包，可能与原生行为重复或冲突。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护** —— 非常活跃且迭代快：最新发布 v3.5.0（2026-06），最后推送 2026-06，未归档（截至 2026-06）。频繁的 v3.x 发版意味着加压逻辑和「味道」可能在版本间变动——锁版本，升级后复查。
- **治理与 bus factor** —— 单维护者的个人仓库（`User` 所有）；约 18k stars，但路线图和整套人设主题都由一个作者把控。厚重主题 + 单人维护 = 实打实的关键人风险。
- **年龄与 Lindy** —— 创建于 2026-03，截至 2026-06 约 0 年：年轻且明显被热捧（短期内 star 数高），因此 Lindy 上未经验证。Star 反映关注度而非耐久度——当作押注一个趋势，而非已沉淀的工具。
- **风险旗标** —— 「PUA / PIP」心理施压框架就是产品本体，无法干净剥离；对中性语气或共享 agent 的场景是劝退点。License 按 README 记为 MIT，但 2026-06 时 `licenseInfo` 为 null——依赖前请核实。

## 存疑（未验证）

- [未验证] 2026-06-26 的 `gh` 元数据报告 `licenseInfo: null`（未检测到 LICENSE 文件），但 README 页脚声明 MIT；frontmatter 按 README 记为 MIT——依赖前请核实真实许可证。
- [未验证] 最新发布报告为 v3.5.0（2026-06-12 发布），仓库最后 push 于 2026-06-17，主语言 TypeScript，未归档，创建于 2026-03——以上为 2026-06-26 的 GitHub 元数据；依赖某具体版本行为前请复核。
- [未验证] star 数（2026-06-26 GitHub 显示约 18.5k）不可靠且对日期敏感；仅作参考，不作质量信号。
- [未验证] 受支持 harness 列表（Claude Code、Codex CLI、Cursor、Kiro、CodeBuddy、OpenClaw、Google Antigravity、OpenCode、VSCode/Copilot，及实验性 pi / Trae）与安装方式（`npx skills add`、`claude plugin install`、手动 curl）均来自 README；各 harness 的实际激活保真度未在此独立确认。
- [未验证] 命令 / 味道列表（`/pua:pua`、`/pua:on`、`/pua:off`、`/pua:p7`、`/pua:p9`、`/pua:p10`、`/pua:yes`、`/pua:mama`、`/pua:pua-loop`、`/pua:survey`、`/pua:flavor`、`/pua:kpi`）与 L0–L4 加压表均来自 README，可能随版本变化。
- [推断] 由于行为活在 agent 加载的人设提示里，除 Claude Code 钩子注入上下文之处外，强制是建议性的；「L4 绝望模式」和三条红线是提示级指令，不是硬保证，且实际钩子覆盖未在此核实。
