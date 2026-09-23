# engineering

> [agent-skills](../INDEX.zh.md) 的叶子。代码质量、Web 性能、测试与科研/工程工作流。
> ← 上层 [agent-skills](../INDEX.zh.md) · 根 [路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Agent Skills (addyosmani)** | 约 24 个生产级工程技能包（质量/安全/web 性能/API/发布），装进 coding agent 并通过约 8 个 SDLC 斜杠命令路由。 | A（4/5） | [→](addyosmani-agent-skills.zh.md) |
| **web-quality-skills** | 含六个技能的 agent 技能包，把 Lighthouse / Core Web Vitals / WCAG / SEO 最佳实践编码成按需加载的指令集，让 coding agent 审计并修复 web 质量问题；属建议层，非测量工具。 | B（4/5） | [→](addyosmani-web-quality.zh.md) |
| **Scientific Agent Skills** | 一个大型 skill 包（约 147 个 skill），把 coding agent 变成生物、化学、医学、药物发现领域的科研助手——每个 skill 用一份带文档的 SKILL.md 封装一个科学 Python 库或数据库，按需加载。 | A（4/5） | [→](scientific-agent-skills.zh.md) |
| **Vercel Agent Skills** | Vercel 官方 agent-skill 包——按需安装的 React/Next.js/Vercel 部署、Web 设计与文档审查指南，采用 agentskills.io/skills.sh 格式。 | C（5/6） | [→](vercel-agent-skills.zh.md) |
| **Waza** | 一套精简的八个「工程习惯」skill 集合（规划、设计、评审、调试、写作、调研、读取、审计），coding agent 可按需加载，覆盖 Claude Code、Codex、Cursor。 | C（5/6） | [→](waza.zh.md) |
| **mattpocock/skills** | Matt Pocock 的工程 skill 包，面向 Claude Code 和 skills.sh，覆盖 grilling、domain docs、TDD、bug 诊断、架构、review、tickets 和实现流程。 | B（4/5） | [→](mattpocock-skills.zh.md) |
| **BrowserAct Skills** | 面向 BrowserAct 的 agent 浏览器自动化技能包：索引式浏览器控制、stealth/private session、远程人工接管，以及 Skill Forge 抓取工作流。 | B（4/5） | [→](browser-act-skills.zh.md) |
| **caveman** | 一个 prompt 与安装器技能包，让多种 coding agent 用刻意简短的“caveman”风格回答，同时保留代码、命令和错误信息。 | C（5/6） | [→](caveman.zh.md) |
| **i-have-adhd** | 一份 10 条规则的回复风格技能：让 coding agent 每轮先说动作、把步骤编号、复述进度，并删掉铺垫与收尾；一套规则覆盖约 15 种 harness。 | A（4/5） | [→](i-have-adhd.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Agent Skills (addyosmani)](addyosmani-agent-skills.zh.md) | ✅ | A（4/5） | 约 24 个生产级工程技能包（质量/安全/web 性能/API/发布），装进 coding agent 并通过约 8 个 SDLC 斜杠命令路由。 |
| [web-quality-skills](addyosmani-web-quality.zh.md) | ✅ | B（4/5） | 含六个技能的 agent 技能包，把 Lighthouse / Core Web Vitals / WCAG / SEO 最佳实践编码成按需加载的指令集，让 coding agent 审计并修复 web 质量问题；属建议层，非测量工具。 |
| [Scientific Agent Skills](scientific-agent-skills.zh.md) | ✅ | A（4/5） | 一个大型 skill 包（约 147 个 skill），把 coding agent 变成生物、化学、医学、药物发现领域的科研助手——每个 skill 用一份带文档的 SKILL.md 封装一个科学 Python 库或数据库，按需加载。 |
| [Vercel Agent Skills](vercel-agent-skills.zh.md) | ✅ | C（5/6） | Vercel 官方 agent-skill 包——按需安装的 React/Next.js/Vercel 部署、Web 设计与文档审查指南，采用 agentskills.io/skills.sh 格式。 |
| [Waza](waza.zh.md) | ✅ | C（5/6） | 一套精简的八个「工程习惯」skill 集合（规划、设计、评审、调试、写作、调研、读取、审计），coding agent 可按需加载，覆盖 Claude Code、Codex、Cursor。 |
| [mattpocock/skills](mattpocock-skills.zh.md) | ✅ | B（4/5） | 面向需求 grilling、domain docs、TDD、bug 诊断、架构、review、tickets 和实现流程的工程过程包。 |
| [BrowserAct Skills](browser-act-skills.zh.md) | ✅ | B（4/5） | 带索引动作、stealth/private session、远程接管和 Skill Forge 的 agent 浏览器自动化层；确定性测试仍用 Playwright。 |
| [caveman](caveman.zh.md) | ✅ | C（5/6） | 给现有 agent 加简短表达覆盖层；改变回复风格，不改变工程流程或上下文设计。 |
| [i-have-adhd](i-have-adhd.zh.md) | ✅ | A（4/5） | 给工作记忆短的读者用的表达覆盖层；改变 agent 的说话方式而非它知道什么——痛点是 token 花销时选 caveman。 |


## 什么该放这里

让编码 agent 更擅长**工程任务**（代码评审、性能、测试、科研工作流）的技能/提示合集。
