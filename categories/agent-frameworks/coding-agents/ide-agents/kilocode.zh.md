---
name: Kilo Code
slug: kilocode
repo: https://github.com/Kilo-Org/kilocode
category: ide-agents
tags: [coding-agent, vscode-extension, byok, ai-pair-programming, orchestrator, multi-model]
language: TypeScript
license: MIT
maturity: v7.x, very active, ~24.9k stars (2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2026-06-29T11:37:52Z
  default_branch: main
  default_branch_sha: 727ded7c0d38f082c99aa545f8b89b473688650d
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:33:51Z
  overall: A
  overall_score: 3.8
  scored_axes: 5
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
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@kilocode/sdk"
        dependent_repos_count: 0
        downloads_last_month: 6743293
        graph_tier: E
        volume_tier: A
        cross_check_divergence: 1.03
        release_downloads: 204701
        release_assets: 1114
        release_tier: C
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 561
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 442
        top1_share: 0.162
        top3_share: 0.331
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
    responsiveness: { reason: no_window_signal }
---

# Kilo Code

一个住在 IDE 里的开源 AI 编码 agent：一个 VS Code（及 JetBrains）扩展，会规划、跨文件改代码、跑命令、在多个专职模式之间切换——自带 key（BYOK）接入 500+ 模型，按供应商原价计费。

![kilocode — 健康度雷达](../../../../assets/health/kilocode.zh.svg)

## 何时使用

你是个开发者，想要一个自主编码 agent *就在你已经在用的编辑器里*，而不是一个要来回拷贝粘贴的独立对话窗。你正在做一个多文件改动——重构一个 service、接一个新 endpoint、顺着调用图追一个 bug——你希望 agent 读仓库、给出方案、原地改文件、跑测试命令、再给你一份 diff 让你批准。你也不想被绑死在单一模型厂商或一个不透明的订阅价上：你宁愿插上自己的 Anthropic/OpenAI/Gemini/OpenRouter key（或一个本地模型），直接付给供应商。你从 VS Code Marketplace 装上 Kilo Code 扩展，指给它一个模型，然后用自然语言驱动它。

你之所以选它，正是因为想要一个*开源*、在 IDE 内、带显式模式/编排工作流的编码 agent——一个在写任何代码前先设计改动的 `Plan` 模式、一个实现它的 `Code` 模式，外加 `Ask`/`Debug`/`Review` 模式——而不是一条不加区分的单一对话循环。当你的瓶颈是*让一个 agent 在你的仓库里做真实改动*、且你看重 MIT 许可、可自带 key 的工具胜过封闭产品时，它很合适；当你想要一个用来搭*你自己的* agent 的库时则不太合适（见「何时不用」）。

## 何时不用

- **你想要一个用来搭自己 agent 的框架。** 这是最锋利的判别：Kilo Code 是个**最终用户编码 agent**，不是库/SDK。如果你在搭一个定制的多 agent 应用、或你自己的 agent 运行时，你该选框架（[DSPy](../../workflow-builders/dspy.zh.md)、[AgentScope](../../agent-runtimes/agent-sdks/agentscope.zh.md)），而不是一个成品 VS Code 扩展。这里没有一个可以 import 的供应商无关「agent 内核」。
- **你不在受支持的 IDE 里。** 它是 VS Code / JetBrains 扩展。在这些编辑器之外（或纯终端/CI 流程里），在 IDE 内的价值就消失了——要 headless/CLI 用法，你该选一个 CLI 形态的 agent。
- **你需要一个稳定、慢节奏的表面。** 项目发版极猛（当前是 v7.x，新版常在几天内落地；2025-03 才创建）。这种速度对出特性是福音，但你要把团队标准化在它上面的话，耦合的就是这份 churn。
- **你想要成本被完全托管、可预测。** BYOK 意味着*你自己*承担供应商成本管理——token 花销取决于你选哪个模型、agent 干得多狠。一个带统一订阅价的封闭产品会消掉这个变量；Kilo 刻意不这么做。
- **你需要最久经沙场的选项。** 对比 Cursor / GitHub Copilot（多年打磨、海量装机）乃至它更年长的兄弟 Cline / Roo Code，Kilo Code 作为一个具名项目更年轻；对规避风险、承重的采用，要掂量这份成熟度差距。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Cline](cline.zh.md) | ✅ | 想要更精简的开源 VS Code coding-agent 上游时，选 Cline。 | 开源 VS Code 编码 agent；属于 Kilo Code 的血统 [推断]。在 IDE 内的 agent 循环相似；Kilo 在其上叠加了模式/编排和自家模型市场。想要更精简的上游就直接对比。 |
| [Roo Code](roo-code.zh.md) | ✅ | 只把 Roo Code 当设计参考：它已于 2026-05-15 归档，要维护的东西请选 Kilo Code。 | Kilo Code 由其衍生 [推断]，模式模型也重叠——但 Roo Code 的产品已关停、代码已冻结，不再是活选项。 |
| Cursor | 非仓库 | 需要闭源 AI 优先*编辑器*，而不是扩展时，选 Cursor。 | 闭源的 AI 优先*编辑器*（一个 VS Code 分叉），不是扩展；集成很深、付费订阅，没有「按供应商原价的 BYOK」这份开放性。更精致，更不开放。 |
| GitHub Copilot | 非仓库 | 需要微软背书的闭源补全+对话+agent，覆盖 VS Code/JetBrains 时，选 GitHub Copilot。 | 闭源、微软背书的补全+对话+agent，在 VS Code/JetBrains 里；装机量巨大、稳定，厂商托管定价，没有自带 key 的多供应商模型。 |
| [oh-my-claudecode](../orchestration-and-review/oh-my-claudecode.zh.md) | ✅ | 需要架在 Anthropic Claude Code CLI 之上的编排层时，选 oh-my-claudecode。 | 架在 Anthropic Claude Code CLI *之上*的编排层（team 流水线、模型路由、tmux）。Kilo Code 是独立的、在 IDE 内的 agent，不是包另一个 agent CLI 的壳。 |

## 技术栈

- **语言：** TypeScript（主语言，仓库元数据 2026-06-28）。
- **宿主：** 以 **VS Code 扩展**（VS Code Marketplace）和 **JetBrains 插件**（JetBrains Marketplace）分发。
- **agent 表面：** 专职模式——`Code`、`Plan`、`Ask`、`Debug`、`Review`——支撑「先规划再实现」工作流，外加工具使用（改文件、跑终端命令）覆盖你的工作区。
- **模型：** 多供应商 / BYOK，覆盖 500+ 模型（Anthropic、OpenAI、Gemini、OpenRouter、本地……），可任务中途切换模型，按供应商原价计费。

## 依赖

- **必需：** VS Code（或一个 JetBrains IDE）来承载扩展；**一个 LLM 供应商 API key**（或一个本地模型的访问）——没有模型在背后，agent 什么也干不了。
- **安装（VS Code）：** 从 VS Code Marketplace 安装 Kilo Code 扩展（或 `vscode:extension/kilocode.kilo-code`）。
- **安装（JetBrains）：** 从 JetBrains Marketplace 安装 Kilo Code 插件。
- **可选：** 项目还提到一个 Kilo CLI / 更广的「all-in-one agentic engineering platform」；但这里的核心依赖表面是 IDE 扩展。

## 运维难度

**低。** 作为最终用户工具，没有服务要部署或运维：装扩展、贴上供应商 key、选个模型，就走。真正的「运维」是（1）**供应商成本管理**——盯紧 token 花销，因为 BYOK 把账单放在你头上；以及（2）跟上快速发版节奏和偶发的破坏性变更。没有数据存储、没有服务端、没有集群。更隐蔽的成本是仔细 review agent 的改动和命令执行——一个在仓库内跑命令、重写文件的 agent 需要人在环里加上像样的 git 卫生习惯，这是工作流纪律而非运维负担。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 8.1 小时，基于 6 个 qualifying issues/PRs。
- **维护——非常活跃（截至 2026-06）。** 最后推送 2026-06-28；发版节奏很猛（当前约 v7.x，新版常彼此相隔几天落地）。未归档。在被积极、密集地维护。
- **治理与背书——组织持有，看似有资金。** 由一个**组织**（`Kilo-Org`）持有，而非单个用户——比独自一人的仓库是更好的 bus-factor 信号，而「all-in-one agentic engineering platform」的定位暗示这是个商业/有资金的努力，在开源扩展周边搭一个付费平台。[未验证] 资金/商业细节与路线图归属。
- **年龄与 Lindy——年轻、未经证明。** 2025-03 创建，约 1 岁（截至 2026-06）。活跃度高、采用迅猛（约 24.9k star），但没有长期沉淀——是「活跃但未经证明」，而非 Lindy 安全。快速变动的表面 ⇒ 预期 churn。
- **血统作为延续性信号。** 普遍认为它衍生自 Roo Code / Cline 编码 agent 血统 [推断]；若属实，那是超出项目自身日历年龄的设计成熟度——但这也意味着「真正的」上游历史落在兄弟项目里，且当前 README 并未陈述这份血统。[未验证]
- **锁定与风险——低。** MIT 许可、按供应商原价 BYOK，故厂商锁定低：你握着自己的模型 key，可以随时走向兄弟/替代 agent。主要风险是年轻 + 速度，而非许可证。

## 存疑（未验证）

- [未验证] 截至 2026-06-28 约 24.9k star、最新发布 v7.3.54（约 2026-06-23）——AI 编码工具领域 GitHub star 和版本变动飞快，仅供参考。
- [推断] 来自 Roo Code 和 Cline 的血统（Kilo 是吸收了 Cline 特性的 Roo Code 分叉）被广泛报道，也是「超集/合并」说法的依据，但当前仓库 README **并未**陈述它——属历史认知，未在此从仓库重新确认。
- [未验证]「500+ 模型」「零加价」和「all-in-one agentic engineering platform」定位都是项目自己的 README/营销表述；未经独立基准测试，且该平台可能含开源扩展之外的付费/托管组件。
- [未验证] 五个模式（`Code`/`Plan`/`Ask`/`Debug`/`Review`）和内部编排行为均据 README/文档，未对照代码核实；模式集合随版本变动。
- [未验证] JetBrains 插件的存在由 marketplace 链接确认，但其与 VS Code 扩展的能力对等性未经核实。
- [推断] 把它归为 `app`（一个最终用户产品）而非 `framework`/`library` 是判断：它是你拿来用的成品编码 agent，而非你用来搭 agent 的工具包。
