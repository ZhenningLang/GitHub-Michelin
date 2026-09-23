# context-engineering

> [agent-skills](../INDEX.zh.md) 的叶子。组织、压缩、路由 agent 所读的内容。
> ← 上层 [agent-skills](../INDEX.zh.md) · 根 [路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Agent Skills for Context Engineering** | 一个 15 个 skill 的 Claude Code 插件包，灌输上下文工程纪律：基础原理、退化、压缩、多 agent 协同、记忆、工具设计、评估与 harness 工程。 | B（5/6） | [→](context-engineering-skills.zh.md) |
| **NotebookLM Claude Code Skill** | 一个 Claude Code skill：用真实 Chrome 驱动查询你的 Google NotebookLM 笔记本，从你自己上传的文档取回有来源依据、带引用的答案，而非逐文件读取或凭空编造。 | D（5/6） | [→](notebooklm-skill.zh.md) |
| **tacit-mining** | 通过结构化对话提取当前用户隐性判断规则，并写入 `memory/tacit/` fragments 的 Claude Code skill。 | D（4/5） | [→](tacit-mining.zh.md) |
| **soul.md** | 用文件层级包装 digital identity：worldview、style、memory、raw data 和好 / 坏输出示例。 | B（4/5） | [→](soul-md.zh.md) |
| **nuwa-skill** | 把公开人物或主题研究 / 蒸馏成 perspective skill，包含心智模型和诚实边界。 | B（4/5） | [→](nuwa-skill.zh.md) |
| **cangjie-skill** | 把书、长视频、播客、课程、访谈和转写稿蒸馏成可复用、可测试 agent skill pack 的方法论 skill。 | C（5/6） | [→](cangjie-skill.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Agent Skills for Context Engineering](context-engineering-skills.zh.md) | ✅ | B（5/6） | 一个 15 个 skill 的 Claude Code 插件包，灌输上下文工程纪律：基础原理、退化、压缩、多 agent 协同、记忆、工具设计、评估与 harness 工程。 |
| [NotebookLM Claude Code Skill](notebooklm-skill.zh.md) | ✅ | D（5/6） | 一个 Claude Code skill：用真实 Chrome 驱动查询你的 Google NotebookLM 笔记本，从你自己上传的文档取回有来源依据、带引用的答案，而非逐文件读取或凭空编造。 |
| [tacit-mining](tacit-mining.zh.md) | ✅ | D（4/5） | 最适合同意参与的用户挖掘 tacit preferences；许可证清晰度或 memory 隐私是硬约束时慎用。 |
| [soul.md](soul-md.zh.md) | ✅ | B（4/5） | 已有 identity / source 文件，需要打包成持久 persona folder 时最适合。 |
| [nuwa-skill](nuwa-skill.zh.md) | ✅ | B（4/5） | 最适合公开人物 / 主题蒸馏；不适合私人克隆或需要引用依据的 retrieval。 |
| [cangjie-skill](cangjie-skill.zh.md) | ✅ | C（5/6） | 最适合把长材料蒸馏成可复用 skill pack；如果更需要带来源问答，改用检索工具。 |


## 什么该放这里

聚焦**上下文工程**的技能合集——组织、压缩、路由 agent 所读内容。
