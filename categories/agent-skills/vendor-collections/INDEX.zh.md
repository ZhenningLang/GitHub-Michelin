# vendor-collections

> [agent-skills](../INDEX.zh.md) 的叶子。官方 / 厂商发布的第一方技能与插件捆绑包。
> ← 上层 [agent-skills](../INDEX.zh.md) · 根 [路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Anthropic Skills** | Anthropic 官方公开的 Agent Skills 合集——自包含的 SKILL.md 目录（文档编辑、设计、MCP 与 skill 编写、沟通），可装进 Claude Code、Claude.ai 或 Claude API。 | B（4/5） | [→](anthropic-skills.zh.md) |
| **Agent Plugins for AWS** | AWS Labs 官方出品的九个 agent 插件集合（serverless、Amplify、SageMaker、迁移、数据库、部署/成本估算等），通过 marketplace 安装、触发短语驱动并接好 AWS MCP server，教 Claude Code / Cursor / Codex 在 AWS 上做架构、部署和运维。 | B（5/6） | [→](aws-agent-plugins.zh.md) |
| **Claude Plugins (Official)** | Anthropic 官方的 Claude Code 插件市场：精选的可安装插件目录（命令、agent、skill、MCP server），通过原生 /plugin 系统按名安装。 | A（4/5） | [→](claude-plugins-official.zh.md) |
| **MiniMax Skills** | MiniMax 官方约 16 个 Agent Skill 成包（前端/移动端/shader 开发，外加 pdf/docx/xlsx/pptx、音乐与多模态生成），经插件市场装进 Claude Code 等编码 agent。 | B（4/5） | [→](minimax-skills.zh.md) |
| **Anthropic Knowledge Work Plugins** | 当你想要 Anthropic 官方面向知识工作（文档、沟通、研究）的开源插件集（用于 Claude）时用它——非常年轻。 | B（4/5） | [→](knowledge-work-plugins.zh.md) |
| **Remotion Agent Skills** | Remotion 官方的 12 个 skill 捆绑包：教编码 agent（Claude Code、Codex、Cursor、Kimi Code）写出正确的 Remotion React 视频代码——经 `npx skills add remotion-dev/skills` 安装，版本与框架同步锁定。 | C（4/5） | [→](remotion-skills.zh.md) |
| **HumanLayer Skills** | HumanLayer 官方的六个 skill——把改动画清楚（`show-me`）、PR 说明结构化（`visual-pr`）、重写 CLAUDE.md、收紧 React props，外加两个把重复性 agent 任务做成定时 GitHub Actions 循环的 skill，循环带 agent memory 文件与 `/iterate` 评论通道。 | B（4/5） | [→](humanlayer-skills.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Anthropic Skills](anthropic-skills.zh.md) | ✅ | B（4/5） | Anthropic 官方公开的 Agent Skills 合集——自包含的 SKILL.md 目录（文档编辑、设计、MCP 与 skill 编写、沟通），可装进 Claude Code、Claude.ai 或 Claude API。 |
| [Agent Plugins for AWS](aws-agent-plugins.zh.md) | ✅ | B（5/6） | AWS Labs 官方出品的九个 agent 插件集合（serverless、Amplify、SageMaker、迁移、数据库、部署/成本估算等），通过 marketplace 安装、触发短语驱动并接好 AWS MCP server，教 Claude Code / Cursor / Codex 在 AWS 上做架构、部署和运维。 |
| [Claude Plugins (Official)](claude-plugins-official.zh.md) | ✅ | A（4/5） | Anthropic 官方的 Claude Code 插件市场：精选的可安装插件目录（命令、agent、skill、MCP server），通过原生 /plugin 系统按名安装。 |
| [MiniMax Skills](minimax-skills.zh.md) | ✅ | B（4/5） | MiniMax 官方约 16 个 Agent Skill 成包（前端/移动端/shader 开发，外加 pdf/docx/xlsx/pptx、音乐与多模态生成），经插件市场装进 Claude Code 等编码 agent。 |
| [Anthropic Knowledge Work Plugins](knowledge-work-plugins.zh.md) | ✅ | B（4/5） | 当你想要 Anthropic 官方面向知识工作（文档、沟通、研究）的开源插件集（用于 Claude）时用它——非常年轻。 |
| [Remotion Agent Skills](remotion-skills.zh.md) | ✅ | C（4/5） | 厂商权威、版本锁定的 React 视频创作指导；不在带 skill 加载器的 harness 上、或不用 Remotion 就没价值，且内容许可未声明。 |
| [HumanLayer Skills](humanlayer-skills.zh.md) | ✅ | B（4/5） | 厂商出品的六个有主张的开发流程 skill，其中两个附带可运行的 CI 循环机制；仅面向 Claude 生态分发、没有可锁定的 release，循环模板默认使用宽松 agent 权限。 |

## 什么该放这里

**官方或厂商发布**的技能/插件合集（Anthropic、AWS、MiniMax 等）——第一方捆绑包。
