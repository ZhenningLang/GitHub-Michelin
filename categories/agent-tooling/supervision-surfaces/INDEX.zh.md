# supervision-surfaces

> 分类节点。人查看、批准和引导 agent 工作的界面；终端、浏览器、手机与桌面均可。
> ← 返回 [agent-tooling](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 子分类 | 何时进入 | 路由 |
| --- | --- | --- |
| **人工审查关口** | 你要检查理解、批注计划或 diff，或阅读有源码依据的评审产物。 | [→](human-review-gates/INDEX.zh.md) |
| **Agent 驾驶舱** | 你要持续查看任务、会话、分支、团队或业务工作；不要求项目本身是 agent 执行运行时。 | [→](agent-cockpits/INDEX.zh.md) |

## 对比矩阵

| 选项 | 类型 | 一句话取舍 |
| --- | --- | --- |
| [人工审查关口](human-review-gates/INDEX.zh.md) | 子分类 | Sphinx、Plannotator 与 Whiteboard 聚焦理解或审查单个产物，不负责持续监管总览。 |
| [Agent 驾驶舱](agent-cockpits/INDEX.zh.md) | 子分类 | 任务、会话与业务监管界面；各项目的执行引擎和派发能力不同。 |

## 什么该放这里

主要职责是**人的视图与决定**的界面：评审／批准闸门、会话驾驶舱、共享分支板与多 agent 控制面，不限终端、浏览器或桌面载体。不含以自有执行核心为选型主轴的完整 agent（见 `agent-frameworks`），不含由 LLM 产出评审 finding 的工具（见 `ai-code-review`），不含 agent 运转所依据的任务／计划状态（见 `work-state`），也不是事后的对话记录分析（见 `session-history`）。
