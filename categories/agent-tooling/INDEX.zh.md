# agent-tooling

> 分类节点。面向 AI 编码 agent 的基础设施——任务/工作追踪、持久记忆、agent 状态，以及 agent 把控制权交还给你的人审/批准界面。
> 按**你在循环的哪一段接线**拆成子分类：运行时保住工作状态、回看已经发生过的事、人评审与干预的那块屏、给 harness 外挂新能力。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 子分类 | 何时进入 | 路由 |
| --- | --- | --- |
| **Work State** | agent 总在运行中途丢掉计划、待办或上下文，你需要那份状态落在磁盘上、可被读回时。 | [→](work-state/INDEX.zh.md) |
| **Session History** | 你想检索、回放或结算已经跑过的会话，而且要跨多个 agent 时。 | [→](session-history/INDEX.zh.md) |
| **Supervision Surfaces** | 必须由人来看 agent 的活——评审计划或 diff、批准、同时盯多个 agent——而且不只在终端里看时。 | [→](supervision-surfaces/INDEX.zh.md) |
| **Harness Extensions** | 你在扩展 agent 能触达、能安装的东西——技能包安装器、为只有 GUI 的软件造命令面、把新模型后端桥进 harness 时。 | [→](harness-extensions/INDEX.zh.md) |

## 对比矩阵

| 选项 | 类型 | 一句话取舍 |
| --- | --- | --- |
| [Work State](work-state/INDEX.zh.md) | 子分类 | beads、CCPM、Ralph、Context Mode、Planning with Files——任务、计划与上下文放在聊天窗口之外，agent 才接得上活。 |
| [Session History](session-history/INDEX.zh.md) | 子分类 | AgentsView、Entire——捕获并检索跑过的会话；只读与回放，管不到下一步。 |
| [Supervision Surfaces](supervision-surfaces/INDEX.zh.md) | 子分类 | Plannotator、CloudCLI、Agent Orchestrator、Hermes Workspace——人看的那块屏：批注闸门与驾驶舱，代价是多一个要在本机跑的服务。 |
| [Harness Extensions](harness-extensions/INDEX.zh.md) | 子分类 | Vercel Skills、CLI-Anything、codex-chatgpt-web——拓宽 agent 的触达面（技能包安装器、生成的 CLI harness、模型后端桥），而不是管理它的活。 |

## 什么该放这里

AI **编码 agent** 用来追踪工作、承载状态、并在需要时把控制权交还给你的基础设施——任务/issue 图、会话捕获、规划/上下文管线、评审与批准界面、harness 外挂。不含与 LLM 无关的记忆库（见 `agent-memory`），不含 agent 运行时（见 `agent-frameworks`），也不含 LLM 自动产出的代码评审（见 `ai-code-review`）。按**你接的是循环的哪一段**选子分类：工作状态（`work-state`）、事后历史（`session-history`）、人的界面（`supervision-surfaces`），还是新能力（`harness-extensions`）。
