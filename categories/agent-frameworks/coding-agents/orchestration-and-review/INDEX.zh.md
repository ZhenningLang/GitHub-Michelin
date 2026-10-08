# orchestration-and-review

> 分类节点。coding agent 控制平面、多 agent 执行器，以及评审/自动化包装层。
> ← 返回[coding-agents](../INDEX.zh.md) · root: [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **CC Switch** | 当你在 Claude Code、Codex、Gemini CLI、OpenCode 等几个编码 CLI 之间来回换厂商，想用一个桌面应用替你改写它们的配置、MCP 服务器和技能时用它——但它是单用户图形应用，无界面服务器上用不了，也当不了团队网关。 | B（5/6） | [→](cc-switch.zh.md) |
| **Claude Octopus** | 一个 Claude Code 插件：把单个任务扇出给至多约 8 个其他 AI 模型（Codex、Gemini、Perplexity、Ollama、OpenRouter 等），用它们之间的分歧作为盲点 / 共识闸门，全部由 `/octo:*` 斜杠命令驱动。 | C（6/6） | [→](claude-octopus.zh.md) |
| **oh-my-claudecode** | 架在 Anthropic Claude Code CLI 之上的多智能体编排层：把一队专职 agent 按阶段串成流水线（plan → prd → exec → verify → fix），为每个子任务路由到更便宜或更强的模型，并在 tmux 下跑并行 worker——以 Claude Code 插件形式安装，或通过 `oh-my-claude-sisyphus` npm 包安装。 | B（6/6） | [→](oh-my-claudecode.zh.md) |
| **OpenHands** | 当你想用一个自托管的浏览器控制台，在指定机器上跑 OpenHands、Claude Code、Codex 或 Gemini CLI 会话，再加上定时或 webhook 触发的 agent 任务时用它——但这个仓库 2026 年 7 月才改成 beta 版 Agent Canvas，经典的 `openhands-ai` agent 已不在这里。 | A（6/6） | [→](openhands.zh.md) |
| **SWE-agent** | 当你必须复现已发表的 SWE-agent 结果、用一份 YAML 配置在 Docker 沙箱里批量让模型修仓库 issue 时用它——但维护者已声明它被 mini-swe-agent 取代，新工作别再从它起步。 | B（5/6） | [→](swe-agent.zh.md) |
| **Background Agents（Open-Inspect）** | 当一个可信组织需要自托管的后台 coding-agent 沙箱、集成和自动化时用它。 | B（5/6） | [→](background-agents.zh.md) |
| **SwarmForge** | 当你想要一个自托管的角色流水线（spec→code→clean→architect→harden→QA）跑在自己的仓库上、每个角色一个 git worktree、以 commit 交接时用它——但它没有许可证，也没有 tagged release。 | D（5/6） | [→](swarm-forge.zh.md) |
| **OpenChamber** | 当你用 OpenCode，想要一个跨设备的运行工作台——按目标审计的会话、一条提示词最多五个模型（可各带 worktree）、变更讲解，以及紧挨对话的 git/PR 面板——但要接受一个 12 个月大、单人主控、只绑一个 agent runtime 的应用时用它。 | B（5/6） | [→](openchamber.zh.md) |
| **OpenResearch** | 当 coding agent 和 GPU 都已经到位、缺的只是实验记账——每个实验一条分支的实验树、不可变的提交快照、以及把 run 派到九个算力后端——时用它，代价是接受一个 3.5 个月大、发布极快的应用，且它的托管算力那一半是闭源服务。 | B（6/6） | [→](openresearch.zh.md) |
| **herdr** | 当你同时监管多个编程 agent、要复用器本体来打 blocked/working/done 标记、并让 agent 之间用 `herdr agent wait/prompt` 互相驱动时用它——但它只有 6 个月大、pre-1.0、实质单人维护。 | B（6/6） | [→](herdr.zh.md) |
| **TUIOS** | 当你在一个终端里同时盯多个编程 agent，想要一个平铺窗口管理器、由守护进程跟踪每个 agent 的状态并把所有待审批和提问收进一个 Inbox 时用它——但它只有 13 个月大、pre-1.0 且有协议破坏、单人维护，pane 默认拥有全部控制权。 | B（6/6） | [→](tuios.zh.md) |
| **GitHub Agentic Workflows (gh-aw)** | 当你想让 coding agent 在 GitHub 仓库上无人值守地干杂活（issue 分诊、查 CI 失败、写报告、提文档 PR），用 Markdown 写、编译成 Actions 工作流，agent 只读并在防火墙后运行、只有声明过的写操作才会执行时用它——但它只限 GitHub、处于 Public Preview、每周发版，7 周内出了 11 个安全公告。 | B（4/6） | [→](gh-aw.zh.md) |

## 什么该放这里

coding agent 控制平面、多 agent 执行器，以及评审/自动化包装层。
