# visual-artifacts

> [design](../INDEX.zh.md) 的叶子。**交付物本身就是视觉产物**的 skill——可编辑技术图、HTML 原生原型、幻灯片、动画、信息图。它们生成的是供人查看的文件，而不是引导 UI 代码、也不是复制某个具名设计。
> ← 上层 [design](../INDEX.zh.md) · 根 [路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **archify** | 面向架构、工作流、时序、数据流和生命周期图的 agent skill，输出自包含图表并带主题切换和导出控制。 | B（4/6） | [→](archify.zh.md) |
| **drawio-skill** | 一个 agent skill：把自然语言、代码、IaC 和接口 schema 变成可编辑的 `.drawio`，并能在源改动后重新同步而不丢手工版式。 | B（4/5） | [→](drawio-skill.zh.md) |
| **huashu-design** | 面向原型、slide deck、可编辑 PPTX、动画 / MP4 / GIF、信息图和视觉 artifact 生成的 HTML-native design skill。 | B（5/6） | [→](huashu-design.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [archify](archify.zh.md) | ✅ | B（4/6） | 最适合技术图表；需要 WYSIWYG 编辑时用人工图表编辑器。 |
| [drawio-skill](drawio-skill.zh.md) | ✅ | B（4/5） | 交付物是可编辑、且要跟着真实源走的 `.drawio` 时最合适；图要保持纯文本用 Mermaid，不能装 draw.io 用 archify。 |
| [huashu-design](huashu-design.zh.md) | ✅ | B（5/6） | 最适合 agent 生成 HTML 视觉 artifact；实现交接看 Stitch，轻量 UI 审美指导看 Taste-Skill。 |


## 什么该放这里

**产出可视化交付物**的 agent skill——图文件、HTML 原型、deck、信息图、渲染动画。发布场景的视觉内容（社交卡片、文章配图）在 [visual-content](../../visual-content/INDEX.zh.md)，专门的 deck 工具链在 [slides-ppt](../../slides-ppt/INDEX.zh.md)；作用于落地 UI 代码的品味指导看 [ui-taste](../ui-taste/INDEX.zh.md)。
