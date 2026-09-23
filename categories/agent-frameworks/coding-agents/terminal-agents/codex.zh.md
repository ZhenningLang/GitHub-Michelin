---
name: Codex
slug: codex
repo: https://github.com/openai/codex
category: terminal-agents
tags: [coding-agent, terminal, ai-agent, openai, code-execution]
language: Rust
license: Apache-2.0
maturity: v0.x, active, 94.8k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-06T08:28:04Z
  default_branch: main
  default_branch_sha: be33f80bc65159c094ecd06bf155afa3061ce23d
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:35:57Z
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
        canonical_package: "@openai/codex"
        dependent_repos_count: 0
        downloads_last_month: 77905874
        graph_tier: E
        volume_tier: A
        cross_check_divergence: 1.02
        homebrew_installs_90d: 283626
        homebrew_tier: A
        release_downloads: 7006482
        release_assets: 16186
        release_tier: B
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 527
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 367
        top1_share: 0.163
        top3_share: 0.312
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
---

# Codex

OpenAI 出品的轻量级编码智能体，在本地终端运行。可读取文件、执行 shell 命令、编辑代码并提交修改——全部通过自然语言界面完成，内置沙箱隔离和 Git 集成。

![Codex — 健康度雷达](../../../../assets/health/codex.zh.svg)

## 何时使用

你是一名开发者，希望有一款 AI 助手直接住在终端里，并能真正修改你的代码库。你用自然语言描述需求——「把这个函数重构为 async/await」或「给这条 API 路由加上错误处理」——Codex 就会读取相关文件、做出编辑、运行测试并提交变更。你偏爱本地工作流而非依赖云 IDE，并且希望智能体拥有真实的 shell 访问权限（带沙箱隔离），从而能够验证自身修改。你可以通过单条 curl 命令或 npm 安装它，并与你现有的 Git 工作流配合。选择 Codex 而不是 Open Interpreter，因为 Codex 是 OpenAI 第一方支持，与 GPT 集成更紧密、体验更精致；选择 Codex 而不是 GitHub Copilot，因为 Codex 是终端原生，可以执行命令，而非仅建议代码。决定取舍：终端优先的编码智能体，拥有真实的文件系统和 shell 访问权限，并由 OpenAI 的模型质量背书。

## 何时不用

- 如果你需要多模型灵活性或想使用本地模型，请用 Open Interpreter 而不用 Codex，因为 Codex 针对 OpenAI 模型优化，不支持其他提供商。
- 如果你处于高度受监管的环境，禁止带 shell 访问权限的 AI 智能体，请用 GitHub Copilot 或 Cursor 而不用 Codex，因为 Codex 在沙箱中执行代码，但仍在你的机器上运行任意命令。
- 如果你想要可视化 IDE 体验，带点按编辑和内联建议，请用 GitHub Copilot 或 Cursor 而不用 Codex，因为 Codex 仅限终端，没有 GUI。
- 如果你需要复杂的多智能体编排，需要多个协作智能体，请用 LangChain 或 AutoGPT 而不用 Codex，因为 Codex 是单智能体编码工具，并非多智能体框架。
- 如果你需要离线运行或本地模型推理，请用 Ollama 或 Open Interpreter 而不用 Codex，因为 Codex 需要联网访问 OpenAI API。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Open Interpreter](open-interpreter.zh.md) | ✅ | 带可切换 harness 的 Codex-fork，面向低成本/开源模型。 | Open Interpreter 支持多家提供商和本地模型；Codex 仅限 OpenAI，但拥有第一方集成与更精致体验。 |
| [OpenCode](opencode.zh.md) | ✅ | 开源终端编码智能体。 | OpenCode 模型无关且由社区驱动；Codex 由 OpenAI 背书，与 GPT 集成更紧密。 |
| [Gemini CLI](gemini-cli.zh.md) | ✅ | Google 的终端 AI 智能体。 | Gemini CLI 仅限 Google 模型且带免费层；Codex 仅限 OpenAI，可能需要 API 额度。 |
| Claude Code | 未收录 | 官方 Anthropic 终端编码智能体。 | 闭源，仅限 Anthropic；Codex 开源且原生终端，但锁定 OpenAI 模型。 |
| GitHub Copilot | 未收录 | AI 结对编程 IDE 扩展。 | Copilot 集成在 IDE 中且按订阅收费；Codex 终端优先、独立运行，可执行 shell 命令。 |

## 技术栈

- **Rust**——核心实现，兼顾性能与安全
- **OpenAI API**——后端 LLM 提供商（GPT-4o / GPT-4.5 级别模型）
- **沙箱隔离**——在 macOS、Linux 和 Windows 上提供操作系统级代码执行沙箱
- **Git**——内置版本控制集成，用于提交变更
- **MCP（Model Context Protocol）**——自定义工具与集成的扩展层

## 依赖

- OpenAI API key（或订阅）
- macOS、Linux 或 Windows 终端
- Git 仓库（推荐，用于变更追踪）
- 网络连接（访问 OpenAI API）

## 运维难度

**低**。Codex 通过 shell 脚本或 npm 安装，作为本地 CLI 进程运行。无需维护服务器。运维负担主要在于管理 OpenAI API 凭证，并在接受智能体修改前进行审查。沙箱机制提供了安全性，但你仍应审计执行的命令。

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 0 天。
- **响应速度**：无法计算——no_traffic。
- **采用广度**：Grade A——npmjs.org 上月下载量 77,905,874（包名：@openai/codex）。
- **长青度**：Grade C——仓库已创建 527 天。
- **治理集中度**：Grade A——前三贡献者占比 31.2%（?）。
- **许可风险**：Grade A——Apache-2.0 许可证。
## 存疑（未验证）

- [未验证] Codex 需要 OpenAI API key；重度使用的确切定价与速率限制尚未核实。
- [推断] 作为 OpenAI 项目，路线图可能优先推动 API 用量或 OpenAI 生态锁定。
- [未验证] 沙箱机制针对恶意对抗性提示的安全保证尚未经过独立审计。
- [推断] 对于 2025-04 创建的项目，star 数极高；部分 inflate 来自 OpenAI 品牌效应，但真实采用度也很强劲。
