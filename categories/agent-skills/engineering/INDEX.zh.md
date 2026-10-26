# engineering

> [agent-skills](../INDEX.zh.md) 的分类节点。代码质量、Web 性能、测试与工程流程；行为覆盖层与科研工作流单列子类。
> ← 上层 [agent-skills](../INDEX.zh.md) · 根 [路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 子分类 | 何时进入 | 路由 |
| --- | --- | --- |
| **behavior-overlays** | 改变 agent 的回复风格、写代码习惯或读入上下文，而非接管通用工程流程或补充领域知识。 | [→](behavior-overlays/INDEX.zh.md) |
| **scientific-workflows** | 助手需要科研分析、实证研究或带证据的论文工作流，而非软件开发习惯。 | [→](scientific-workflows/INDEX.zh.md) |

## 本分类合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **awesome-gamedev-agent-skills** | 按引擎与版本路由十种引擎的游戏配方；提供指引，不控制编辑器。 | B（4/5） | [→](awesome-gamedev-agent-skills.zh.md) |
| **SwiftUI Pro** | 专项检查 SwiftUI 的 API、数据流和无障碍；仅为建议，依赖 SDK 版本。 | B（4/5） | [→](swiftui-agent-skill.zh.md) |
| **Agent Skills (addyosmani)** | 约 24 个生产级工程技能包（质量/安全/web 性能/API/发布），装进 coding agent 并通过约 8 个 SDLC 斜杠命令路由。 | A（4/5） | [→](addyosmani-agent-skills.zh.md) |
| **web-quality-skills** | 含六个技能的 agent 技能包，把 Lighthouse / Core Web Vitals / WCAG / SEO 最佳实践编码成按需加载的指令集，让 coding agent 审计并修复 web 质量问题；属建议层，非测量工具。 | B（4/5） | [→](addyosmani-web-quality.zh.md) |
| **Vercel Agent Skills** | Vercel 官方 agent-skill 包——按需安装的 React/Next.js/Vercel 部署、Web 设计与文档审查指南，采用 agentskills.io/skills.sh 格式。 | B（4/6） | [→](vercel-agent-skills.zh.md) |
| **cc-skills-golang** | 当你的 coding agent 写出能编译但不地道的 Go（error 包装、nil 陷阱、命名）时用它——要的是按需加载的 Go 说明书，不是流程／TDD 包。 | C（5/6） | [→](cc-skills-golang.zh.md) |
| **Waza** | 一套精简的八个「工程习惯」skill 集合（规划、设计、评审、调试、写作、调研、读取、审计），coding agent 可按需加载，覆盖 Claude Code、Codex、Cursor。 | C（5/6） | [→](waza.zh.md) |
| **mattpocock/skills** | Matt Pocock 的工程 skill 包，面向 Claude Code 和 skills.sh，覆盖 grilling、domain docs、TDD、bug 诊断、架构、review、tickets 和实现流程。 | B（4/5） | [→](mattpocock-skills.zh.md) |
| **BrowserAct Skills** | 面向 BrowserAct 的 agent 浏览器自动化技能包：索引式浏览器控制、stealth/private session、远程人工接管，以及 Skill Forge 抓取工作流。 | B（4/5） | [→](browser-act-skills.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [awesome-gamedev-agent-skills](awesome-gamedev-agent-skills.zh.md) | ✅ | B（4/5） | 不接编辑器即可补玩法与素材领域配方；模型路由和引擎验收仍需自行负责。 |
| [科研工作流](scientific-workflows/INDEX.zh.md) | 子分类 | — | 科学库、实证方法与带证据的论文；软件开发实践留在本节点。 |
| [SwiftUI Pro](swiftui-agent-skill.zh.md) | ✅ | B（4/5） | 专项参考与文件级修法；不是编译器、性能分析器或模拟器操作工具。 |
| [Agent Skills (addyosmani)](addyosmani-agent-skills.zh.md) | ✅ | A（4/5） | 约 24 个生产级工程技能包（质量/安全/web 性能/API/发布），装进 coding agent 并通过约 8 个 SDLC 斜杠命令路由。 |
| [web-quality-skills](addyosmani-web-quality.zh.md) | ✅ | B（4/5） | 含六个技能的 agent 技能包，把 Lighthouse / Core Web Vitals / WCAG / SEO 最佳实践编码成按需加载的指令集，让 coding agent 审计并修复 web 质量问题；属建议层，非测量工具。 |
| [Vercel Agent Skills](vercel-agent-skills.zh.md) | ✅ | B（4/6） | Vercel 官方 agent-skill 包——按需安装的 React/Next.js/Vercel 部署、Web 设计与文档审查指南，采用 agentskills.io/skills.sh 格式。 |
| [cc-skills-golang](cc-skills-golang.zh.md) | ✅ | C（5/6） | 给 coding agent 按需加载的 Go 习惯用法 skill；不是流程／TDD 包，全装会偏向作者自己的库。 |
| [Waza](waza.zh.md) | ✅ | C（5/6） | 一套精简的八个「工程习惯」skill 集合（规划、设计、评审、调试、写作、调研、读取、审计），coding agent 可按需加载，覆盖 Claude Code、Codex、Cursor。 |
| [mattpocock/skills](mattpocock-skills.zh.md) | ✅ | B（4/5） | 面向需求 grilling、domain docs、TDD、bug 诊断、架构、review、tickets 和实现流程的工程过程包。 |
| [BrowserAct Skills](browser-act-skills.zh.md) | ✅ | B（4/5） | 带索引动作、stealth/private session、远程接管和 Skill Forge 的 agent 浏览器自动化层；确定性测试仍用 Playwright。 |
| [行为覆盖层](behavior-overlays/INDEX.zh.md) | 子分类 | — | 在现有配置上叠加回复形状、写代码习惯与读入上下文压缩；通用工程流程和软件领域指引留在本节点。 |


## 什么该放这里

让编码 agent 更擅长**软件工程任务**的技能／提示合集，覆盖代码评审、性能、测试、浏览器工程、通用工程流程与软件领域指引。回复风格、写代码习惯与读入上下文覆盖层走 [behavior-overlays](behavior-overlays/INDEX.zh.md)。科研分析、实证研究与论文证据流程走 [scientific-workflows](scientific-workflows/INDEX.zh.md)。
