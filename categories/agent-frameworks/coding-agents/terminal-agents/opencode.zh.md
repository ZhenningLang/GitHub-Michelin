---
name: OpenCode
slug: opencode
repo: https://github.com/anomalyco/opencode
category: terminal-agents
tags: [coding-agent, ai-agent, terminal, cli, typescript]
language: TypeScript
license: MIT
maturity: v0.x, active, 181k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-04T12:37:42Z
  default_branch: dev
  default_branch_sha: 7a8e7c88f495acf5af3e7584e8ec1dbab2fe04ec
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:36:41Z
  overall: A
  overall_score: 3.6
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
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@opencode-ai/cli-linux-x64"
        dependent_repos_count: 0
        downloads_last_month: 554339
        graph_tier: E
        volume_tier: B
        cross_check_divergence: 1.09
        homebrew_installs_90d: 94934
        homebrew_tier: A
        release_downloads: 84114151
        release_assets: 3624
        release_tier: A
        signal_basis: homebrew+releases
        tier_source: homebrew+releases
    longevity:
      grade: C
      raw:
        repo_age_days: 510
        last_commit_age_days: 1
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 429
        top1_share: 0.146
        top3_share: 0.417
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

# OpenCode

一款开源的终端 AI 编码智能体，可编辑文件、执行命令并与现有代码库协同工作。通过 npm 以 `opencode-ai` 安装。

![OpenCode — health radar](../../../../assets/health/opencode.zh.svg)

## 何时使用

你是一位开发者，想用 AI 辅助编码，但拒绝被单一 LLM 厂商锁定。你已经试过 Claude Code（只能调 Claude）和 Codex（只能调 OpenAI），发现一旦模型价格暴涨或能力倒退，你就被困住了。你需要一个模型无关的编码智能体——同一个工具，今天接 GPT-4，明天切 Claude 3.5，后天跑本地 Llama，完全由你决定。你选择 OpenCode 而不是 Claude Code，因为 OpenCode 让你自由切换模型，而 Claude Code 被锁死在 Anthropic。你选择它而不是 Open Interpreter，因为 OpenCode 基于 TypeScript/npm，与你已在使用的 JavaScript 生态更自然地集成。OpenCode 是 MIT 许可的，源码可审计，架构可扩展，你甚至能 fork 出来改适合自己团队的工作流。安装只需 `npm install opencode-ai`，连接 API key，指向仓库——它是驻留在 shell 里、不挑模型的结对编程搭档。

## 何时不用

- **你已经在用 Claude Code 且对 Anthropic 路线图有信心**——如果你只调 Claude、预算固定、对厂商方向有信心，Claude Code 是更 polished 的选择（Claude 专属的上下文优化、Artifacts 集成）。切换到 OpenCode 只会增加配置负担，没有额外收益。请继续使用 Claude Code 而不是 OpenCode，因为当你不需要模型自由时，厂商锁定体验反而更优。
- **团队需要 IDE 内无缝集成**——OpenCode 是 CLI 工具，不是 VS Code 插件。如果你习惯在编辑器里点击按钮让 AI 改代码，请改用 Kilo Code 或 GitHub Copilot，因为它们的 IDE 原生集成提供更顺滑的编辑体验。
- **非技术用户或终端恐惧者**——纯命令行交互，没有 GUI。如果团队里有人不会用终端，这就是门槛。请改用 Claude 网页版或 ChatGPT，因为它们提供熟悉的聊天界面，无需技术设置。
- **追求企业级治理**——无 RBAC、无审计日志、无 admin 面板。它是个人/小团队的开发工具，不是企业平台。如需组织治理，请改用 Dify 或 GitHub Copilot for Business，因为这些平台提供管理控制、审计轨迹和团队管理。
- **你 100% 确定只用一个模型且永远不会换**——OpenCode 的核心价值是模型自由切换。如果你知道未来只用 Claude（或只用 GPT-4），模型无关性对你为零价值。请改用 Claude Code 或 Codex CLI，因为单一厂商工具更简单，且对该模型优化得更紧密。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Open Interpreter](open-interpreter.zh.md) | ✅ | OS 沙箱执行和开源模型 harness 切换是重点时，选 Open Interpreter。 | Open Interpreter 是 Rust 重写，带 OS 沙箱执行；OpenCode 基于 TypeScript/npm，与 JS/TS 工作流更自然集成。 |
| [Hermes Agent](../../agent-runtimes/personal-assistants/hermes-agent.zh.md) | ✅ | 跨会话学习循环和技能创建比专注编码 agent 更重要时，选 Hermes。 | Hermes 侧重跨会话技能创建与个人成长；OpenCode 是专注的编码智能体，没有学习循环。 |
| [AutoGPT](../../workflow-builders/autogpt.zh.md) | ✅ | 需要复杂多步自主工作流自动化，而不是终端结对编程时，选 AutoGPT。 | AutoGPT 面向复杂多步自主任务；OpenCode 是终端结对编程助手。 |
| Claude Code | 未收录 | 能接受专有、订阅绑定的终端 agent，并想要 Anthropic 托管体验时，选 Claude Code。 | 专有、无源码、需订阅；OpenCode 开源且 BYOK。 |
| [Gemini CLI](gemini-cli.zh.md) | ✅ | Google 背书和 Apache-2.0 比 OpenCode 的 MIT/社区模式更重要时，选 Gemini CLI。 | Apache-2.0，Google 背书；OpenCode 是 MIT，社区驱动。 |

## 技术栈

- **TypeScript**——主要实现语言
- **Node.js**——运行时环境
- **npm**——通过 `npm install opencode-ai` 分发
- **Monorepo**——包含 console app 与核心逻辑的多个包

## 依赖

- **Node.js** 运行时（需满足包的版本要求）
- **LLM API key**——OpenAI、Anthropic 或兼容提供商
- **终端 / shell**——主要交互界面
- **Git**——用于与仓库协作

## 运维难度

**低**。安装方式类似 `npm install -g opencode-ai`；智能体作为本地进程运行，无需管理常驻服务。持续负担主要是 API key 轮换与保持 npm 包更新。

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 0 天。
- **响应速度**：无法计算——no_traffic。
- **采用广度**：Grade C——npmjs.org 上月下载量 138,309（包名：@opencode-ai/cli-linux-x64）。
- **长青度**：Grade C——仓库已创建 429 天。
- **治理集中度**：Grade A——前三贡献者占比 45.1%（?）。
- **许可风险**：Grade A——MIT 许可证。
## 存疑（未验证）

- [推断] 2025 年 4 月创建的仓库已有 181k GitHub star，可能受炒作推动，而非有机生产级采用。
- [未验证] 具体 npm 包名与安装路径可能因项目尚处 v0.x 而变动。
- [未验证] 多语言 README 支持（列出 18 余种语言）显示全球化野心，但非英语文档深度未经检验。
- [未验证] `anomalyco` 与任何商业实体或盈利计划之间的关系未公开说明。
