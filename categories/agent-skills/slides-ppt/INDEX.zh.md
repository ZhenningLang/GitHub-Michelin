# slides-ppt

> [agent-skills](../INDEX.zh.md) 的叶子。面向演示文稿与幻灯片 deck 的 agent 生成技能。
> ← 上层 [agent-skills](../INDEX.zh.md) · 根[路由](../../../INDEX.zh.md) · English：[INDEX.md](INDEX.md)

## 本叶子集合

| 集合 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Guizang PPT Skill** | 当你想让 agent 把文章变成有设计感的单文件 HTML 翻页 PPT（杂志风或瑞士风）时用它。 | C（4/5） | [→](guizang-ppt.zh.md) |
| **ppt-master** | 把文档、笔记、参考资料或已有 `.pptx` 变成原生可编辑 PowerPoint deck 的 agent workflow。 | B（5/6） | [→](ppt-master.zh.md) |
| **frontend-slides** | 面向单文件 HTML presentation 和 PPT-to-web conversion 的 coding-agent skill，带视觉风格预览选择。 | B（4/5） | [→](frontend-slides.zh.md) |
| **html-ppt-skill** | HTML PPT Studio，内置 36 个主题、15 个 full-deck templates、31 个布局、47 个动画和 presenter mode。 | C（4/5） | [→](html-ppt-skill.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Guizang PPT Skill](guizang-ppt.zh.md) | ✅ | C（4/5） | 有强审美约束的单文件 HTML deck skill，锁定编辑杂志风与瑞士风视觉系统。 |
| [HTML Anything](../../ai-design-generation/html-anything.zh.md) | ✅ | B（5/6） | 更宽的 Markdown 到 HTML 产物生成器；不如本叶子的 deck 工作流专门，也没这么强约束。 |
| [Open Design](../../ai-design-generation/open-design.zh.md) | ✅ | B（6/6） | 更宽的本地设计 studio；当 deck 只是 UI、卡片、图像、视频中的一种产物时选它。 |
| Slidev / Marp | 未收录 | — | 更成熟的开发者 deck 框架；不是 agent skill 优先，也没有内建强 art direction。 |
| [ppt-master](ppt-master.zh.md) | ✅ | B（5/6） | `.pptx` 可编辑性是硬约束时最合适；比 HTML deck skills 更重，依赖本地 Python 和模型质量。 |
| [frontend-slides](frontend-slides.zh.md) | ✅ | B（4/5） | 最适合 web-first deck 和 PPT-to-web conversion，带视觉预览选择。 |
| [html-ppt-skill](html-ppt-skill.zh.md) | ✅ | C（4/5） | 需要大型内建 HTML deck runtime / catalog 和 presenter mode 时最合适。 |


## 什么该放这里

主要产物是**演示文稿 / 幻灯片 deck** 的 agent skill：HTML 翻页 deck、类 PPT deck、Keynote 风格 deck，或幻灯片专用生成工作流。
