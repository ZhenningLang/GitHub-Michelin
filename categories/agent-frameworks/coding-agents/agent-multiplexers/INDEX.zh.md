# agent-multiplexers

> 分类节点。专为同时监管多个编程 agent 而做的终端和复用器：它们跟踪每个 agent 是卡住、在干活还是已完成，并把你带到正在等你的那一个。
> ← 返回[coding-agents](../INDEX.zh.md) · root: [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **herdr** | 当你同时监管多个编程 agent、要复用器本体来打 blocked/working/done 标记、并让 agent 之间用 `herdr agent wait/prompt` 互相驱动时用它——但它只有 6 个月大、pre-1.0、实质单人维护。 | B（6/6） | [→](herdr.zh.md) |
| **TUIOS** | 当你在一个终端里同时盯多个编程 agent，想要一个平铺窗口管理器、由守护进程跟踪每个 agent 的状态并把所有待审批和提问收进一个 Inbox 时用它——但它只有 13 个月大、pre-1.0 且有协议破坏、单人维护，pane 默认拥有全部控制权。 | B（6/6） | [→](tuios.zh.md) |
| **cmux** | 当你在 Mac 上并排跑好几个命令行编码 agent，想让终端应用本身给正在等你的那个窗格套上光圈、在竖排侧边栏显示分支/PR/最新消息、旁边再开一个 agent 能操作的浏览器窗格时用它——但它只支持 macOS、才 8 个月大、遥测默认开启，服务端是 BUSL-1.1。 | D（5/6） | [→](cmux.zh.md) |

## 什么该放这里

主要职责是并排托管多个命令行编程 agent、并把每个 agent 的状态（等审批、在干活、已完成）摆到眼前、让一个人能同时监管它们的终端应用、复用器和平铺窗口管理器。不收编程 agent 本身（见 `terminal-agents`）；不收派发、调度或评审 agent 工作的控制面（见 `orchestration-and-review`）；不收不感知 agent 的通用终端复用器（见 `terminal-ui`）。
