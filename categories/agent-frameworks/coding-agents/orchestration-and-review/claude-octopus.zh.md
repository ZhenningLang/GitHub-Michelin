---
name: Claude Octopus
slug: claude-octopus
repo: https://github.com/nyldn/claude-octopus
category: orchestration-and-review
tags: [claude-code, plugin, multi-model, orchestration, slash-commands, blindspot, mcp]
language: Shell
license: MIT
maturity: v9.45.0, active (2026-06)
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-06-25T02:50:04Z
  default_branch: main
  default_branch_sha: 239263db9db25590b0386dbdbb38d0a6fface5c6
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:25:37Z
  overall: B
  overall_score: 2.8
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.3
        qualifying_issues: 47
        band: default
        window_offset_days: 3
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: D
      raw:
        repo_age_days: 169
        last_commit_age_days: 1
        cohort: framework
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 14
        top1_share: 0.94
        top3_share: 0.968
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
    adoption: { reason: registry_no_counts }
---

# Claude Octopus

一个 Claude Code 插件：把单个任务扇出给至多约 8 个其他 AI 模型（Codex、Gemini、Perplexity、Ollama、OpenRouter 等），用它们之间的分歧作为盲点 / 共识闸门，全部由 `/octo:*` 斜杠命令驱动。

![claude-octopus — 健康度雷达](../../../../assets/health/claude-octopus.zh.svg)

## 何时使用

你已经把 Claude Code 当作主力 agent，而且被“自信但错误”的答案坑过——Claude 放过的一个安全漏洞、没人交叉核对就拍板的依赖选型、Claude 自己喜欢但换个模型就会质疑的设计。你不想离开自己的 harness、手动把 prompt 粘到另外五个工具里；你想在*同一个会话里*拿到第二（以及第三、第八）个意见。Claude Octopus 以插件形式安装，给你 `/octo:research`、`/octo:security`、`/octo:council` 这类命令，把同一个任务分发给你已装好的各家 provider CLI(Codex、Gemini、Copilot、Perplexity、Ollama、OpenRouter、Qwen、Antigravity)，再由 Claude 汇总结果并套一个共识闸门，让分歧在合并前而不是合并后浮现。

它最适合的用法，是把这些额外模型当成叠在 Claude 编排之上的*评审 / 调研小组*：用 Double Diamond 这类结构化工作流（`/octo:embrace`）做端到端的功能开发，用多 provider 对抗式评审做代码和安全审查，用带逐模型署名的并行调研。如果你本就为 OpenAI/Gemini/Copilot 订阅付费，或者本地跑 Ollama，你就能不搭新基础设施拿到这些额外视角——Claude 是唯一必需的 provider，其余都自动探测、可选。

## 何时不用

- **你不用 Claude Code。** 这是一个 Claude Code *插件*，不是独立编排器，需要 Claude Code v2.1.14+ 作宿主（Cursor/OpenCode/Codex CLI 有替代安装方式，但属次要）。如果你的 harness 是纯 LangGraph/AutoGen/DSPy，它给不了你什么——见下方对比。
- **你想要一个厂商中立的多 agent 框架。** Claude 被硬编码为必需的编排器 / 综合者，架构是“Claude 指挥、其他模型建言”。如果你需要任何模型都能当控制器的框架，形状就不对。
- **你不愿意安装并认证一堆 provider CLI。** 价值与你跑通了多少个 `codex`/`gemini`/`agy`/`qwen`/`ollama`、外加 Perplexity/OpenRouter 的 API key 成正比。只装 Claude 时，你拿到的基本只是套在单模型外面的 prompt 脚手架。
- **对成本 / 延迟敏感。** 把一个任务扇给多个模型会成倍放大 token 花费和墙钟时间，并拉进付费 provider（Perplexity、OpenRouter;Qwen 的免费 OAuth 档已于 2026-04 结束）。一次共识跑下来并不便宜。
- **你需要可复现、可审计的编排逻辑。** 行为分散在 49+ 斜杠命令、32 个 persona、54 个 skill、hooks 和一个 MCP server 里，大多是 Shell——一个庞大且快速迭代（242 次发布）的表面，你会被它绑定。排查一次错误分发意味着穿过这层插件内部。
- **单厂商 / 数据出域约束。** 把你的代码和 prompt 路由给 OpenAI、Google、Perplexity、OpenRouter 等，可能违反数据处理政策；仅用 Ollama 模式能收窄但消除不了这点。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [oh-my-claudecode](oh-my-claudecode.zh.md) | ✅ | 需要 Claude Code 增强层，但不需要多模型评审核心时，选 oh-my-claudecode。 | 同样是 Claude Code 增强层（配置/skills/体验优化），但不围绕多模型扇出 + 共识构建；Octopus 的整个前提是让*其他*模型来评审 Claude。 |
| [DSPy](../../workflow-builders/dspy.zh.md) | ✅ | 需要模型无关、库形态的程序化 prompt / pipeline 优化框架时，选 DSPy。 | 程序化 prompt / pipeline 优化框架，模型无关、库形态；你写 Python 而非斜杠命令。层次完全不同——是编译，而非 harness 内的评审小组。 |
| [AgentScope](../../agent-runtimes/agent-sdks/agentscope.zh.md) | ✅ | 需要通用多 agent 运行时/库来构建应用时，选 AgentScope。 | 通用多 agent 运行时 / 库，你在其上构建应用；不绑 Claude Code，也不对“盲点共识”持立场。 |
| [Symphony](../../agent-runtimes/agent-services/symphony.zh.md) | ✅ | 需要由跟踪器驱动的 coding-agent 运行编排时，选 Symphony。 | OpenAI 的多 agent 编排；锚定在 OpenAI 而非 Claude，是框架不是插件。 |
| [openfang](../../agent-runtimes/agent-services/openfang.zh.md) | ✅ | 需要编排模型不同的同类 agent 框架时，选 openfang。 | 同类 agent 框架，编排模型不同；选型前先比范围。 |
| crystal / claude-squad | 未收录 | 需要并行跑多个 Claude Code 会话/worktree 时，选 crystal 或 claude-squad。 | 并行跑多个 Claude Code *会话/worktree*；并行发生在多个 Claude 实例之间，而非*不同厂商模型*评审同一个任务。 |

## 技术栈

- **语言：** Shell（约占仓库 88%）,TypeScript（约 8%，即 MCP server），外加 Go 模板、JavaScript 和少量 Python（据 GitHub 语言统计，2026-06）。
- **宿主：** Claude Code 插件——注册 `/octo:*` 斜杠命令、通过 `.claude-plugin/hooks.json` 注册生命周期 hooks（会话起止、prompt 提交、工具调用、compaction），以及一个 MCP server。
- **Providers（经 CLI 分发）:** Claude（必需，编排器）、Codex/OpenAI、Gemini、GitHub Copilot、Perplexity、Ollama（本地）、Qwen、Antigravity(`agy`)、OpenRouter，外加一个通用 OpenAI 兼容 tool-loop agent（v9.45.0 新增）。
- **概念：** Double Diamond 工作流、32 个 persona、54 个 skill、75% 共识质量闸门、用于 CI/review 事件的“reaction engine”，以及可选的 `claude-mem` 记忆集成。[推断] persona/skill/命令的确切数量是项目自己的表述，会随版本变化。

## 依赖

- **必需：** Claude Code v2.1.14+（用 Anthropic 兼容网关需 v2.1.129+），以及运行编排器所需的 Anthropic/Claude 权限。
- **可选 provider CLI（真正的价值所在）:** `codex`、`gemini`、`agy`、`qwen`、`ollama`；外加 Perplexity（`PERPLEXITY_API_KEY`）与 OpenRouter（`OPENROUTER_API_KEY`）的 API key，以及不走 OAuth 时的 `OPENAI_API_KEY`/`GEMINI_API_KEY`/`QWEN_API_KEY`。“Claude 必需，其余全部可选并自动探测。”
- **MCP server（Cursor/独立）:** Node.js + npm（在 `mcp-server/` 里 `npm install`）。
- **状态：** 结果在 `~/.claude-octopus/results/`，日志在 `~/.claude-octopus/logs/`，逐项目状态在 `.octo/`。
- **安装：** `claude plugin marketplace add https://github.com/nyldn/plugins.git`，再 `claude plugin install octo@nyldn-plugins`，然后在会话内 `/octo:setup`。

## 运维难度

**安装低，跑好则中到高。** 装插件就是一条 marketplace 命令加一个 setup 向导，只用 Claude 时开箱即用。难度随你真正想让其贡献的 provider 数量上升：要安装并认证多个厂商 CLI、管理多份 API key/订阅，还要在一条命令扇给多模型时权衡成本与延迟。庞大的 Shell 表面和快速发版节奏（242 次发布，最后推送 2026-06-25）意味着你在对着一个移动靶维护，排查分发或 hook 故障要读插件内部。数据出域审查得你自己来，因为 prompt/代码会发往第三方 provider。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 0.3 小时，基于 47 个 qualifying issues/PRs。
- **维护——非常活跃（截至 2026-06）。** 最后推送 2026-06-25，发版节奏很高（242 次发布，当前 v9.45.0）；未归档。这读起来像在被积极、甚至高频地维护——其反面就是「何时不用」里点到的频繁变动。
- **治理与 bus factor——单维护者 / 个人仓库。** 由个人 GitHub 账号（`nyldn`）持有，而非组织或基金会；路线图掌握在一个人手里。对一个你接进每次会话的工具来说，这是 bus-factor 为一的风险。[推断]
- **年龄与 Lindy——年轻、未经证明。** 2026-01 创建，约 6 个月（截至 2026-06）。活跃度高但无历史沉淀；按「年龄 × 仍活跃」的启发式，它是「活跃但未经证明」，而非 Lindy 意义上的安全押注——其寿命尚未被证明。
- **风险信号——扇出面 + 数据出域。** 其价值取决于把 prompt / 代码路由给第三方 provider（OpenAI/Google/Perplexity/OpenRouter），且行为分布在庞大、快速变动的 Shell/TS 表面上；重许可风险低（MIT），但运维 / 耦合风险是真实的。

## 存疑（未验证）

- [未验证] 截至 2026-06 star 约 3.7k、fork 约 344——本生态 GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] “117 个测试套件通过”“75% 共识质量闸门”“32 persona / 54 skill / 49+ 命令”“至多 8 个模型”均为项目自身 README/徽章口径，未经独立核实，且数量随版本漂移。
- [未验证] v9.45.0 发布日期 2026-06-15 及其更新项（Antigravity 升为一等 provider、通用 OpenAI 兼容 agent、路由覆盖）取自 GitHub release 页面；更早版本的确切语义未审计。
- [未验证] provider 认证细节（如 Qwen 免费 OAuth 档于 2026-04 结束、哪些 provider 走 OAuth、哪些必须用 key）源自 README，可能变动。
- [推断] 多模型“盲点”共识带来的真实质量提升是设计主张；分歧是否能可靠地抓出 bug/安全问题，这里没有独立基准证明。
- [推断] “主语言 Shell”的口径反映行数；编排语义也分布在 TypeScript（MCP）与 prompt/skill markdown 中，语言占比低估了逻辑真正所在的位置。
