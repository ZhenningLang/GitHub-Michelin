# orchestration-and-review

> 分类节点。coding agent 控制平面、多 agent 执行器，以及评审/自动化包装层。
> ← 返回[coding-agents](../INDEX.zh.md) · root: [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **CC Switch** | 一款跨平台桌面 All-in-One 管理器，用于管理 Claude Code、Claude Desktop、Codex、Gemini CLI、OpenCode、OpenClaw 和 Hermes Agent——基于 Rust 与 Tauri 2 构建。 | B（4/6） | [→](cc-switch.zh.md) |
| **Claude Octopus** | 一个 Claude Code 插件：把单个任务扇出给至多约 8 个其他 AI 模型（Codex、Gemini、Perplexity、Ollama、OpenRouter 等），用它们之间的分歧作为盲点 / 共识闸门，全部由 `/octo:*` 斜杠命令驱动。 | B（5/6） | [→](claude-octopus.zh.md) |
| **oh-my-claudecode** | 架在 Anthropic Claude Code CLI 之上的多智能体编排层：把一队专职 agent 按阶段串成流水线（plan → prd → exec → verify → fix），为每个子任务路由到更便宜或更强的模型，并在 tmux 下跑并行 worker——以 Claude Code 插件形式安装，或通过 `oh-my-claude-sisyphus` npm 包安装。 | B（5/6） | [→](oh-my-claudecode.zh.md) |
| **OpenHands** | 🙌 OpenHands: AI-Driven Development | A（4/6） | [→](openhands.zh.md) |
| **RTK** | 高性能 CLI 代理，在命令输出到达 LLM 上下文前先过滤和压缩，对常见开发命令可减少 60–90% 的 token 消耗，开销低于 10 毫秒。 | B（5/6） | [→](rtk.zh.md) |
| **SWE-agent** | SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024] | A（5/6） | [→](swe-agent.zh.md) |
| **Background Agents（Open-Inspect）** | 当一个可信组织需要自托管的后台 coding-agent 沙箱、集成和自动化时用它。 | B（5/6） | [→](background-agents.zh.md) |

## 什么该放这里

coding agent 控制平面、多 agent 执行器，以及评审/自动化包装层。
