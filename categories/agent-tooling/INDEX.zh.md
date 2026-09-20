# agent-tooling

> 分类节点。面向 AI 编码 agent 的基础设施——任务/工作追踪、持久记忆、agent 状态。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **beads** | 当 AI agent 跨会话丢失任务状态、你想在仓库里要一张可版本化、感知依赖的任务图时用它。 | B（6/6） | [→](beads.zh.md) |
| **CCPM** | 当一个功能大到单次会话装不下、且你想要 PRD 转 GitHub Issues 的规格加上 git worktree 并行 agent 时使用。 | B（4/6） | [→](ccpm.zh.md) |
| **Entire** | 想把 AI agent 会话以 Git checkpoint 形式与 commit 并列捕获、可搜索可回滚时用它。 | B（5/6） | [→](entire-cli.zh.md) |
| **Ralph for Claude Code** | 想让 Claude Code 无人值守地啃完 fix_plan.md 清单、又要速率限制/熔断器/双条件退出闸门兜底时用它。 | B（6/6） | [→](ralph-claude-code.zh.md) |
| **Context Mode** | 当 coding agent 把上下文耗在原始工具输出上、你想要沙箱执行加熬过 compaction 的会话记忆时用它。 | D（6/6） | [→](context-mode.zh.md) |
| **Planning with Files** | 当长任务 agent 总在 /clear、上下文压缩或崩溃中丢失计划时用它把计划落到磁盘。 | B（4/6） | [→](planning-with-files.zh.md) |
| **Vercel Skills** | 当你想要一个 npm 风格的 CLI 来跨多个编码 agent 安装、查找、更新 SKILL.md 技能包时使用。 | D（6/6） | [→](vercel-skills.zh.md) |
| **AgentsView** | 当你同时跑多个编码 agent、想要本地优先的跨 agent 会话搜索与 token／成本分析时用它——但它问世仅数月、尚未到 1.0，要预期频繁变动。 | B（6/6） | [→](agentsview.zh.md) |
| **Agent Orchestrator** | 当你要监管多个跑在真实分支上的并行编码 agent、想要一个桌面控制面把每个隔离进 git worktree 并自动路由 CI/review/冲突反馈时用它——但它约 4.5 个月大、尚未到 1.0、单一 User 所有，且 daemon 是 loopback 无鉴权。 | B（5/6） | [→](agent-orchestrator.zh.md) |
| **CLI-Anything** | 当你想让编码 agent 驱动只有 GUI 的软件、走由应用自身引擎支撑的生成式 CLI harness 时用它——但它仍在 1.0 之前，且每个 harness 由社区维护。 | B（6/6） | [→](cli-anything.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [beads](beads.zh.md) | ✅ | B（6/6） | 当 AI agent 跨会话丢失任务状态、你想在仓库里要一张可版本化、感知依赖的任务图时用它。 |
| [CCPM](ccpm.zh.md) | ✅ | B（4/6） | 当一个功能大到单次会话装不下、且你想要 PRD 转 GitHub Issues 的规格加上 git worktree 并行 agent 时使用。 |
| [Entire](entire-cli.zh.md) | ✅ | B（5/6） | 想把 AI agent 会话以 Git checkpoint 形式与 commit 并列捕获、可搜索可回滚时用它。 |
| [Ralph for Claude Code](ralph-claude-code.zh.md) | ✅ | B（6/6） | 想让 Claude Code 无人值守地啃完 fix_plan.md 清单、又要速率限制/熔断器/双条件退出闸门兜底时用它。 |
| [Context Mode](context-mode.zh.md) | ✅ | D（6/6） | 当 coding agent 把上下文耗在原始工具输出上、你想要沙箱执行加熬过 compaction 的会话记忆时用它。 |
| [Planning with Files](planning-with-files.zh.md) | ✅ | B（4/6） | 当长任务 agent 总在 /clear、上下文压缩或崩溃中丢失计划时用它把计划落到磁盘。 |
| [Vercel Skills](vercel-skills.zh.md) | ✅ | D（6/6） | 当你想要一个 npm 风格的 CLI 来跨多个编码 agent 安装、查找、更新 SKILL.md 技能包时使用。 |
| [AgentsView](agentsview.zh.md) | ✅ | B（6/6） | 当你同时跑多个编码 agent、想要本地优先的跨 agent 会话搜索与 token／成本分析时用它——但它问世仅数月、尚未到 1.0，要预期频繁变动。 |
| [Agent Orchestrator](agent-orchestrator.zh.md) | ✅ | B（5/6） | 当你要监管多个跑在真实分支上的并行编码 agent、想要一个桌面控制面把每个隔离进 git worktree 并自动路由 CI/review/冲突反馈时用它——但它约 4.5 个月大、尚未到 1.0、单一 User 所有，且 daemon 是 loopback 无鉴权。 |
| [CLI-Anything](cli-anything.zh.md) | ✅ | B（6/6） | 生成式 CLI harness，驱动应用自身真实后端——对 GUI 软件覆盖面广，但仍在 1.0 之前且由社区维护。 |
| Taskmaster / GitHub Issues + gh / Linear | 未收录 | — | 各页对比里点到的其他 agent 任务/工作追踪后端。 |

## 什么该放这里

AI **编码 agent** 用来追踪工作、承载状态的基础设施——任务/issue 图、会话捕获、规划/上下文管线。不含与 LLM 无关的记忆库（见 `agent-memory`），不含 agent 运行时（见 `agent-frameworks`）。
