# design

> [agent-skills](../INDEX.zh.md) 的叶子。设计审美 / UI-UX 判断——critique、反 AI 味、视觉生成。
> ← 上层 [agent-skills](../INDEX.zh.md) · 根 [路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Designer Skills** | 覆盖面很广的设计实践 skill pack——9 个 plugin 下共 97 个 skill、30 个 command（研究、设计系统、UX 策略、UI、交互、原型/测试、design ops、工具箱、视觉批评），适用于 Claude Code 和 Gemini CLI。 | B（4/5） | [→](designer-skills.zh.md) |
| **Skills For Design Engineers** | Emil Kowalski 的六技能设计工程包，面向 UI motion、动画词汇、Apple 风格界面原则、严格动画评审和动画改进计划。 | B（4/5） | [→](emilkowalski-skills.zh.md) |
| **make-interfaces-feel-better** | 一个单一、聚焦的 agent skill，把约 16 条具体的 UI 打磨原则（同心圆角、可中断过渡、等宽数字、入场/出场动画）注入 coding agent，让界面「感觉」做完了，而不只是功能正确。 | B（4/5） | [→](make-interfaces-feel-better.zh.md) |
| **Stitch Skills** | 一套遵循 Agent Skills 开放标准的技能库，驱动 Google 的 Stitch MCP server 生成 UI 屏幕、在代码与设计间双向转换、抽取 DESIGN.md，并导出 React/React Native/shadcn 组件。 | B（4/5） | [→](stitch-skills.zh.md) |
| **Taste-Skill** | 一套可移植、与框架无关的 agent skill 包，给 coding agent 注入审美，阻止千篇一律的 AI-slop 前端，转而产出有意图的布局、排版、动效与留白。 | B（4/5） | [→](taste-skill.zh.md) |
| **UI UX Pro Max Skill** | 一个设计智能 skill pack，通过本地 CSV 检索引擎（风格/配色/字体/规则数据库）和交付前可访问性清单给 coding agent 注入 UI/UX 品味，可装入多种 agent harness。 | B（5/6） | [→](ui-ux-pro-max.zh.md) |
| **Hallmark** | 当 Claude Code、Cursor、Codex agent 需要有主张的反 AI 味设计 brief、审计、重设计或研究流程时用它。 | B（4/5） | [→](hallmark.zh.md) |
| **archify** | 面向架构、工作流、时序、数据流和生命周期图的 agent skill，输出自包含图表并带主题切换和导出控制。 | B（4/6） | [→](archify.zh.md) |
| **ai-website-cloner-template** | 面向获授权网站重建的 AI coding agent template：截图、设计 token、资产、组件规格、并行 builder 和视觉 QA。 | B（4/5） | [→](ai-website-cloner-template.zh.md) |
| **huashu-design** | 面向原型、slide deck、可编辑 PPTX、动画 / MP4 / GIF、信息图和视觉 artifact 生成的 HTML-native design skill。 | B（5/6） | [→](huashu-design.zh.md) |
| **drawio-skill** | 一个 agent skill：把自然语言、代码、IaC 和接口 schema 变成可编辑的 `.drawio`，并能在源改动后重新同步而不丢手工版式。 | B（4/5） | [→](drawio-skill.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Designer Skills](designer-skills.zh.md) | ✅ | B（4/5） | 覆盖面很广的设计实践 skill pack——9 个 plugin 下共 97 个 skill、30 个 command（研究、设计系统、UX 策略、UI、交互、原型/测试、design ops、工具箱、视觉批评），适用于 Claude Code 和 Gemini CLI。 |
| [Skills For Design Engineers](emilkowalski-skills.zh.md) | ✅ | B（4/5） | 动画和设计工程 taste 是瓶颈时最合适；UX research 或设计系统用更宽的设计包。 |
| [make-interfaces-feel-better](make-interfaces-feel-better.zh.md) | ✅ | B（4/5） | 一个单一、聚焦的 agent skill，把约 16 条具体的 UI 打磨原则（同心圆角、可中断过渡、等宽数字、入场/出场动画）注入 coding agent，让界面「感觉」做完了，而不只是功能正确。 |
| [Stitch Skills](stitch-skills.zh.md) | ✅ | B（4/5） | 一套遵循 Agent Skills 开放标准的技能库，驱动 Google 的 Stitch MCP server 生成 UI 屏幕、在代码与设计间双向转换、抽取 DESIGN.md，并导出 React/React Native/shadcn 组件。 |
| [Taste-Skill](taste-skill.zh.md) | ✅ | B（4/5） | 一套可移植、与框架无关的 agent skill 包，给 coding agent 注入审美，阻止千篇一律的 AI-slop 前端，转而产出有意图的布局、排版、动效与留白。 |
| [UI UX Pro Max Skill](ui-ux-pro-max.zh.md) | ✅ | B（5/6） | 一个设计智能 skill pack，通过本地 CSV 检索引擎（风格/配色/字体/规则数据库）和交付前可访问性清单给 coding agent 注入 UI/UX 品味，可装入多种 agent harness。 |
| [Hallmark](hallmark.zh.md) | ✅ | B（4/5） | 带 build、audit、redesign、study 动词的有主张设计技能；是建议式指导，不是组件库或确定性 linter。 |
| [archify](archify.zh.md) | ✅ | B（4/6） | 最适合技术图表；需要 WYSIWYG 编辑时用人工图表编辑器。 |
| [ai-website-cloner-template](ai-website-cloner-template.zh.md) | ✅ | B（4/5） | 最适合获授权网站重建；不适合 phishing、impersonation 或无授权设计复制。 |
| [huashu-design](huashu-design.zh.md) | ✅ | B（5/6） | 最适合 agent 生成 HTML 视觉 artifact；实现交接看 Stitch，轻量 UI 审美指导看 Taste-Skill。 |
| [drawio-skill](drawio-skill.zh.md) | ✅ | B（4/5） | 交付物是可编辑、且要跟着真实源走的 `.drawio` 时最合适；图要保持纯文本用 Mermaid，不能装 draw.io 用 archify。 |


## 什么该放这里

给 agent **设计审美 / UI-UX 判断**的技能合集——critique、反 AI 味、视觉生成提示。
