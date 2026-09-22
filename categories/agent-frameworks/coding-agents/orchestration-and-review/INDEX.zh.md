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
| **SwarmForge** | 当你想要一个自托管的角色流水线（spec→code→clean→architect→harden→QA）跑在自己的仓库上、每个角色一个 git worktree、以 commit 交接时用它——但它没有许可证，也没有 tagged release。 | D（6/6） | [→](swarm-forge.zh.md) |
| **OpenChamber** | 当你用 OpenCode，想要一个跨设备的运行工作台——按目标审计的会话、一条提示词最多五个模型（可各带 worktree）、变更讲解，以及紧挨对话的 git/PR 面板——但要接受一个 12 个月大、单人主控、只绑一个 agent runtime 的应用时用它。 | C（5/6） | [→](openchamber.zh.md) |
| **OpenResearch** | 当 coding agent 和 GPU 都已经到位、缺的只是实验记账——每个实验一条分支的实验树、不可变的提交快照、以及把 run 派到九个算力后端——时用它，代价是接受一个 3.5 个月大、发布极快的应用，且它的托管算力那一半是闭源服务。 | B（5/6） | [→](openresearch.zh.md) |

## 什么该放这里

coding agent 控制平面、多 agent 执行器，以及评审/自动化包装层。
