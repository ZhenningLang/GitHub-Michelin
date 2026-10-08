# agent-vendors

> [vendor-collections](../INDEX.zh.md) 的叶子。AI 模型、编码 agent 和 agent 工具公司发布的第一方捆绑包——给自家 agent 用的通用 skill 与插件市场（文档、设计、开发流程），不是教你用某个别的产品。
> ← 上层 [vendor-collections](../INDEX.zh.md) · 根 [路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Anthropic Skills** | Anthropic 官方公开的 Agent Skills 合集——自包含的 SKILL.md 目录（文档编辑、设计、MCP 与 skill 编写、沟通），可装进 Claude Code、Claude.ai 或 Claude API。 | A（3/5） | [→](anthropic-skills.zh.md) |
| **Claude Plugins (Official)** | Anthropic 官方的 Claude Code 插件市场：精选的可安装插件目录（命令、agent、skill、MCP server），通过原生 /plugin 系统按名安装。 | A（4/5） | [→](claude-plugins-official.zh.md) |
| **Cursor Plugins** | Cursor 官方插件市场仓库：`/add-plugin <名字>` 把 skill、规则、子 agent、hook 和 MCP 配置装进 Cursor——16 个第一方插件（主打 poteto 的严谨工程工作流 pstack），外加 80 个连到厂商托管 MCP server 的薄连接器。 | B（3/5） | [→](cursor-plugins.zh.md) |
| **MiniMax Skills** | MiniMax 官方约 16 个 Agent Skill 成包（前端/移动端/shader 开发，外加 pdf/docx/xlsx/pptx、音乐与多模态生成），经插件市场装进 Claude Code 等编码 agent。 | B（4/5） | [→](minimax-skills.zh.md) |
| **Anthropic Knowledge Work Plugins** | 当你想要 Anthropic 官方面向知识工作（文档、沟通、研究）的开源插件集（用于 Claude）时用它——非常年轻。 | A（4/5） | [→](knowledge-work-plugins.zh.md) |
| **HumanLayer Skills** | HumanLayer 官方的六个 skill——把改动画清楚（`show-me`）、PR 说明结构化（`visual-pr`）、重写 CLAUDE.md、收紧 React props，外加两个把重复性 agent 任务做成定时 GitHub Actions 循环的 skill，循环带 agent memory 文件与 `/iterate` 评论通道。 | B（4/5） | [→](humanlayer-skills.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Anthropic Skills](anthropic-skills.zh.md) | ✅ | A（3/5） | Anthropic 官方公开的 Agent Skills 合集——自包含的 SKILL.md 目录（文档编辑、设计、MCP 与 skill 编写、沟通），可装进 Claude Code、Claude.ai 或 Claude API。 |
| [Claude Plugins (Official)](claude-plugins-official.zh.md) | ✅ | A（4/5） | Anthropic 官方的 Claude Code 插件市场：精选的可安装插件目录（命令、agent、skill、MCP server），通过原生 /plugin 系统按名安装。 |
| [Cursor Plugins](cursor-plugins.zh.md) | ✅ | B（3/5） | Cursor 原生插件（按角色分模型的评审面板、hook、云端 agent 分发）加一键 SaaS 连接器；只认 Cursor 的加载器，装的永远是没有 tag 的 `main`，多数连接器只是指向厂商托管 server 的配置。 |
| [MiniMax Skills](minimax-skills.zh.md) | ✅ | B（4/5） | MiniMax 官方约 16 个 Agent Skill 成包（前端/移动端/shader 开发，外加 pdf/docx/xlsx/pptx、音乐与多模态生成），经插件市场装进 Claude Code 等编码 agent。 |
| [Anthropic Knowledge Work Plugins](knowledge-work-plugins.zh.md) | ✅ | A（4/5） | 当你想要 Anthropic 官方面向知识工作（文档、沟通、研究）的开源插件集（用于 Claude）时用它——非常年轻。 |
| [HumanLayer Skills](humanlayer-skills.zh.md) | ✅ | B（4/5） | 厂商出品的六个有主张的开发流程 skill，其中两个附带可运行的 CI 循环机制；仅面向 Claude 生态分发、没有可锁定的 release，循环模板默认使用宽松 agent 权限。 |

## 什么该放这里

AI 模型、编码 agent 和 agent 工具公司发布的第一方捆绑包——给自家 agent 用的通用 skill 与插件市场（文档、设计、开发流程），不是教你用某个别的产品。
