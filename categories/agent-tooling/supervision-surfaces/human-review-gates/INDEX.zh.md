# human-review-gates

> 分类节点。人要检查理解、批注或阅读有源码依据的评审产物；不是运行会话的总览界面。
> ← 返回 [supervision-surfaces](../INDEX.zh.md) · 根路由：[分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Sphinx** | 本地 Git 推送前，按源码回答行为题；可绕过的学习辅助，不是发布授权。 | C（5/6） | [→](sphinx.zh.md) |
| **Plannotator** | 当 agent 的产出（计划、diff、HTML 产物）必须由人批注或批准、并把批注当作 agent 下一条指令发回去时用它。 | B（6/6） | [→](plannotator.zh.md) |
| **Whiteboard** | 当你要 coding agent 亲笔「画」出评审——对钉住的分支生成可交互 RFC，图、引文与代码片段都能点回本地 checkout 的确切行——时用它——但它问世约 6 周、v0.1.x，且评审面只读。 | B（5/6） | [→](whiteboard.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Sphinx](sphinx.zh.md) | ✅ | C（5/6） | Git 继续前测试你对已提交行为的预测；增加模型费用与可能误判，不产代码评审意见。 |
| [Plannotator](plannotator.zh.md) | ✅ | B（6/6） | 长在 agent 循环里的人工闸门：批注计划或 diff，决定经 hook 协议回传——代价是极年轻、单人维护。 |
| [Whiteboard](whiteboard.zh.md) | ✅ | B（5/6） | agent 亲笔在钉住的分支上画出可交互 RFC——图与引文点回确切代码；评审面只读、问世约 6 周。 |
| harness 内建的计划批准（Claude Code / Codex） | 非仓库 | — | 零安装，但没有批注、没有渲染后的文档、不留下你批准过什么的记录。 |

## 什么该放这里

按单个计划、diff、设计说明或行为问题组织人工审查。Sphinx 检查理解，Plannotator 接收批注与批准，Whiteboard 展示有源码依据的评审。需要持续监管任务、会话或业务时，转到 [agent-cockpits](../agent-cockpits/INDEX.zh.md)。
