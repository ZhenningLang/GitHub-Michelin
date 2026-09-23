# session-history

> 分类节点。把 agent 已经做过的事留成记录，供你事后检索——跨 agent 的会话搜索与 token/成本分析，以及写进 Git 的会话检查点。
> ← 返回 [agent-tooling](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **AgentsView** | 当你同时跑多个编码 agent、想要本地优先的跨 agent 会话搜索与 token／成本分析时用它——但它问世仅数月、尚未到 1.0，要预期频繁变动。 | B（6/6） | [→](agentsview.zh.md) |
| **Entire** | 想把 AI agent 会话以 Git checkpoint 形式与 commit 并列捕获、可搜索可回滚时用它。 | B（6/6） | [→](entire-cli.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [AgentsView](agentsview.zh.md) | ✅ | B（6/6） | 把各 agent 的本地会话日志索引进一个可搜索、可算成本的视图——读侧分析对话记录。 |
| [Entire](entire-cli.zh.md) | ✅ | B（6/6） | 让每次会话与 commit 并列落成 Git 检查点——能回放和回滚工作，而不只是翻记录。 |
| 对 `~/.claude` / 会话目录做 grep | 非仓库 | — | 它不是项目而是一种做法：零依赖且完全本地，但没有 UI、没有 token/成本计算、没有跨 agent 归一化。 |

## 什么该放这里

针对**已结束或进行中会话**的记录与回看：捕获、搜索、用量与成本分析。不含 agent 继续干活所需的状态（见 `work-state`），也不是让你在 agent 中途批准或干预的实时界面（见 `supervision-surfaces`）。
