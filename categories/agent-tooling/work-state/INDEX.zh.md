# work-state

> 分类节点。把 agent 的*下一步是什么*放在聊天窗口之外——任务/issue 图、落在磁盘上的计划、无人值守的循环驱动器，以及熬得过 compaction 的运行期上下文。
> ← 返回 [agent-tooling](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **beads** | 当 AI agent 跨会话丢失任务状态、你想在仓库里要一张可版本化、感知依赖的任务图时用它。 | B（5/6） | [→](beads.zh.md) |
| **CCPM** | 当一个功能大到单次会话装不下、且你想要 PRD 转 GitHub Issues 的规格加上 git worktree 并行 agent 时使用。 | C（4/5） | [→](ccpm.zh.md) |
| **Ralph for Claude Code** | 想让 Claude Code 无人值守地啃完 fix_plan.md 清单、又要速率限制/熔断器/双条件退出闸门兜底时用它。 | C（5/6） | [→](ralph-claude-code.zh.md) |
| **Context Mode** | 当 coding agent 把上下文耗在原始工具输出上、你想要沙箱执行加熬过 compaction 的会话记忆时用它。 | D（6/6） | [→](context-mode.zh.md) |
| **Planning with Files** | 当长任务 agent 总在 /clear、上下文压缩或崩溃中丢失计划时用它把计划落到磁盘。 | B（5/6） | [→](planning-with-files.zh.md) |
| **LoopX** | 当 agent 的工作要跨天、跨重启、跨运行时持续推进，且需要持久目标、人工门禁、配额与证据治理每一轮时用它。 | B（6/6） | [→](loopx.zh.md) |
| **Token Optimizer** | 当 coding agent 的 token 烧在工具输出、重复读取和 compaction 丢失上、你又想要钩子层压缩、compaction 检查点和本地美元台账时用它——代价是接受其非商用许可证。 | C（5/6） | [→](token-optimizer.zh.md) |
| **RTK** | 智能体的上下文被一屏屏“测试通过”和 `git push` 进度行塞满；RTK 挂钩智能体的 shell 命令，只交回失败项和一行确认（只管 Bash 输出；Apache-2.0）。 | A（5/6） | [→](rtk.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [beads](beads.zh.md) | ✅ | B（5/6） | 仓库内可版本化、感知依赖的 issue 图——当 agent 自己读写这份待办时最合身。 |
| [CCPM](ccpm.zh.md) | ✅ | C（4/5） | PRD 转 GitHub Issues 加并行 worktree agent——换来 issue 跟踪器的事实源与并发，代价是丢掉 Git 内状态。 |
| [Ralph for Claude Code](ralph-claude-code.zh.md) | ✅ | C（5/6） | 带护栏的无人值守清单循环——它驱动 agent，不负责存放工作本身。 |
| [Context Mode](context-mode.zh.md) | ✅ | D（6/6） | 沙箱挡掉工具噪声、记忆熬过压缩——它管上下文，不管任务清单。 |
| [Planning with Files](planning-with-files.zh.md) | ✅ | B（5/6） | 把计划当普通文件落盘——从 /clear 恢复最便宜，但没有图与依赖语义。 |
| [LoopX](loopx.zh.md) | ✅ | B（6/6） | 状态内核加配额门控的多运行时心跳驱动——本分类里治理最完整的一套，代价是 fail-closed 协议和一个极年轻、高速变动的表面。 |
| [Token Optimizer](token-optimizer.zh.md) | ✅ | C（5/6） | 钩子层压缩加 compaction 检查点加本地美元台账，覆盖约 10 个 coding agent；source-available 非商用许可证，7 个月大的单人维护表面。 |
| [RTK](rtk.zh.md) | ✅ | A（5/6） | 只压 shell 输出——一个 Apache-2.0 的 Rust 单二进制，改写智能体的 Bash 命令并保留退出码；没有检查点，除 `rtk gain` 外没有台账，读文件会绕过它。 |
| Taskmaster / GitHub Issues + gh / Linear | 未收录 | — | 各页对比里点到的其他 agent 任务/工作追踪后端。 |

## 什么该放这里

**工作进行中** agent 需要的状态：任务与 issue 图、计划文件、清单驱动的无人值守循环、运行期上下文与记忆。不含事后回看已经发生过的事（见 `session-history`），不含人观看或批准时用的界面（见 `supervision-surfaces`），也不含 prompt/skill 技能包（见 `agent-skills`）。
