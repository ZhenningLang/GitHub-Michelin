# vendor-collections

> [agent-skills](../INDEX.zh.md) 的叶子。官方 / 厂商发布的第一方技能与插件捆绑包。
> ← 上层 [agent-skills](../INDEX.zh.md) · 根 [路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Anthropic Skills** | Anthropic 官方公开的 Agent Skills 合集——自包含的 SKILL.md 目录（文档编辑、设计、MCP 与 skill 编写、沟通），可装进 Claude Code、Claude.ai 或 Claude API。 | A（3/5） | [→](anthropic-skills.zh.md) |
| **Agent Plugins for AWS** | AWS Labs 官方出品的九个 agent 插件集合（serverless、Amplify、SageMaker、迁移、数据库、部署/成本估算等），通过 marketplace 安装、触发短语驱动并接好 AWS MCP server，教 Claude Code / Cursor / Codex 在 AWS 上做架构、部署和运维。 | B（5/6） | [→](aws-agent-plugins.zh.md) |
| **Claude Plugins (Official)** | Anthropic 官方的 Claude Code 插件市场：精选的可安装插件目录（命令、agent、skill、MCP server），通过原生 /plugin 系统按名安装。 | A（4/5） | [→](claude-plugins-official.zh.md) |
| **Cursor Plugins** | Cursor 官方插件市场仓库：`/add-plugin <名字>` 把 skill、规则、子 agent、hook 和 MCP 配置装进 Cursor——16 个第一方插件（主打 poteto 的严谨工程工作流 pstack），外加 80 个连到厂商托管 MCP server 的薄连接器。 | B（3/5） | [→](cursor-plugins.zh.md) |
| **MiniMax Skills** | MiniMax 官方约 16 个 Agent Skill 成包（前端/移动端/shader 开发，外加 pdf/docx/xlsx/pptx、音乐与多模态生成），经插件市场装进 Claude Code 等编码 agent。 | B（4/5） | [→](minimax-skills.zh.md) |
| **Anthropic Knowledge Work Plugins** | 当你想要 Anthropic 官方面向知识工作（文档、沟通、研究）的开源插件集（用于 Claude）时用它——非常年轻。 | A（4/5） | [→](knowledge-work-plugins.zh.md) |
| **Remotion Agent Skills** | Remotion 官方的 12 个 skill 捆绑包：教编码 agent（Claude Code、Codex、Cursor、Kimi Code）写出正确的 Remotion React 视频代码——经 `npx skills add remotion-dev/skills` 安装，版本与框架同步锁定。 | C（4/5） | [→](remotion-skills.zh.md) |
| **HumanLayer Skills** | HumanLayer 官方的六个 skill——把改动画清楚（`show-me`）、PR 说明结构化（`visual-pr`）、重写 CLAUDE.md、收紧 React props，外加两个把重复性 agent 任务做成定时 GitHub Actions 循环的 skill，循环带 agent memory 文件与 `/iterate` 评论通道。 | B（4/5） | [→](humanlayer-skills.zh.md) |
| **Android Skills** | Google 官方 24 个 skill 包，覆盖模型仍会失手的 Android 活（edge-to-edge、R8、Navigation 3、Play 政策）——用 Android CLI 安装，不是 `npx skills add`。 | B（5/6） | [→](android-skills.zh.md) |
| **Modern Web Guidance** | Google Chrome 官方的“先搜再取”skill：写 HTML/CSS/客户端 JS 前，agent 用本地搜索的 npm CLI 取回一篇经评测打分的现代平台指南（原生 API、Baseline 支持、适度降级）。 | B（5/6） | [→](modern-web-guidance.zh.md) |
| **Agent Toolkit for AWS** | 当你的编码 agent 在真实 AWS 账号里干活、你既要 AWS 当前的剧本、又要 IAM 和 CloudTrail 能把 agent 的调用和你的分开时用：约 114 个 skill 加一个托管 MCP 端点；只管 AWS，托管那一半能看到你的流量。 | A（4/5） | [→](agent-toolkit-for-aws.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Anthropic Skills](anthropic-skills.zh.md) | ✅ | A（3/5） | Anthropic 官方公开的 Agent Skills 合集——自包含的 SKILL.md 目录（文档编辑、设计、MCP 与 skill 编写、沟通），可装进 Claude Code、Claude.ai 或 Claude API。 |
| [Agent Plugins for AWS](aws-agent-plugins.zh.md) | ✅ | B（5/6） | AWS Labs 官方出品的九个 agent 插件集合（serverless、Amplify、SageMaker、迁移、数据库、部署/成本估算等），通过 marketplace 安装、触发短语驱动并接好 AWS MCP server，教 Claude Code / Cursor / Codex 在 AWS 上做架构、部署和运维。 |
| [Claude Plugins (Official)](claude-plugins-official.zh.md) | ✅ | A（4/5） | Anthropic 官方的 Claude Code 插件市场：精选的可安装插件目录（命令、agent、skill、MCP server），通过原生 /plugin 系统按名安装。 |
| [Cursor Plugins](cursor-plugins.zh.md) | ✅ | B（3/5） | Cursor 原生插件（按角色分模型的评审面板、hook、云端 agent 分发）加一键 SaaS 连接器；只认 Cursor 的加载器，装的永远是没有 tag 的 `main`，多数连接器只是指向厂商托管 server 的配置。 |
| [MiniMax Skills](minimax-skills.zh.md) | ✅ | B（4/5） | MiniMax 官方约 16 个 Agent Skill 成包（前端/移动端/shader 开发，外加 pdf/docx/xlsx/pptx、音乐与多模态生成），经插件市场装进 Claude Code 等编码 agent。 |
| [Anthropic Knowledge Work Plugins](knowledge-work-plugins.zh.md) | ✅ | A（4/5） | 当你想要 Anthropic 官方面向知识工作（文档、沟通、研究）的开源插件集（用于 Claude）时用它——非常年轻。 |
| [Remotion Agent Skills](remotion-skills.zh.md) | ✅ | C（4/5） | 厂商权威、版本锁定的 React 视频创作指导；不在带 skill 加载器的 harness 上、或不用 Remotion 就没价值，且内容许可未声明。 |
| [HumanLayer Skills](humanlayer-skills.zh.md) | ✅ | B（4/5） | 厂商出品的六个有主张的开发流程 skill，其中两个附带可运行的 CI 循环机制；仅面向 Claude 生态分发、没有可锁定的 release，循环模板默认使用宽松 agent 权限。 |
| [Android Skills](android-skills.zh.md) | ✅ | B（5/6） | Google 官方给模型仍会失手的 Android 活准备的剧本；只覆盖 Android、走 CLI 安装、不接受外部贡献。 |
| [Modern Web Guidance](modern-web-guidance.zh.md) | ✅ | B（5/6） | 浏览器厂商按任务检索的构建指导；`0.0.x` 预览版，每次调用走 npm，遥测默认开启，不检查你的产出。 |
| [Agent Toolkit for AWS](agent-toolkit-for-aws.zh.md) | ✅ | A（4/5） | AWS 对 Labs 插件的继任者：skill 加上经托管端点、打了 agent 标记的调用；只管 AWS，无 tag，不收外部 PR，创业插件带合作伙伴优惠链接。 |

## 什么该放这里

**官方或厂商发布**的技能/插件合集（Anthropic、AWS、MiniMax 等）——第一方捆绑包。
