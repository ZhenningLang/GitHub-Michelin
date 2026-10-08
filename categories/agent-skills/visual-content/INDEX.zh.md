# visual-content

> [agent-skills](../INDEX.zh.md) 的叶子。社交卡片、文章配图、封面和其他视觉内容技能。
> ← 上层 [agent-skills](../INDEX.zh.md) · 根[路由](../../../INDEX.zh.md) · English：[INDEX.md](INDEX.md)

## 本叶子集合

| 集合 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Guizang Social Card Skill** | 当你在 Claude Code/Codex 里想让 agent 用锁定的编辑风/瑞士风生成小红书图文或公众号封面对（单文件 HTML 渲染成 PNG）时使用。 | D（3/5） | [→](guizang-social-card.zh.md) |
| **ian-xiaohei-illustrations** | 当你要为中文文章批量生成风格一致、带小黑 IP 的手绘 16:9 正文配图时用它。 | B（4/5） | [→](ian-illustrations.zh.md) |
| **handraw-style** | 当你想把编号化的手绘画风、版面图型与主题色（279/122/36）交给装好的 agent skill 拼成中英双语生图提示词时用它。 | C（4/5） | [→](handraw-style.zh.md) |
| **hand-drawn-styles** | 当你已经定下几种手绘画风、需要 agent 把每套实测配方原样复现（22 套配方，其中三套带锚点图和验收规则）成可复制的生图提示词时用它。 | C（5/6） | [→](hand-drawn-styles.zh.md) |
| **Lieflat Charts** | 当你想让编码助手把数据做成模板锁定、可直接发布的单文件 HTML 图表或 12 套中英双语整页报告、整套交付共用一种编辑风视觉语言时用它。 | C（3/5） | [→](lieflat-charts.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Guizang Social Card Skill](guizang-social-card.zh.md) | ✅ | D（3/5） | 把社交卡片和封面做成 HTML 到 PNG 产物；很年轻且 AGPL。 |
| [ian-xiaohei-illustrations](ian-illustrations.zh.md) | ✅ | B（4/5） | 固定角色 / IP 的手绘文章配图；不是可编辑 deck 或卡片模板。 |
| [Guizang PPT Skill](../slides-ppt/guizang-ppt.zh.md) | ✅ | C（4/5） | 当产物是完整 deck、不是独立卡片或文章配图时选它。 |
| [HTML Anything](../../ai-design-generation/html-anything.zh.md) | ✅ | B（5/6） | 更宽的 HTML 产物生成器；不如本叶子聚焦某个视觉内容表面。 |
| [handraw-style](handraw-style.zh.md) | ✅ | C（4/5） | 手绘视觉的提示词包路线：编号画风/图型/配色 + 逐模型激活兜底；很年轻、单人维护、打包美术来源有风险。 |
| [hand-drawn-styles](hand-drawn-styles.zh.md) | ✅ | C（5/6） | 手绘视觉的原样配方路线：22 套验证过的画风配方由零依赖渲染器取出，按设计只出提示词；很年轻、单人维护、2026-10-08 才有首个发布，多种画风衍生自 Midjourney 风格码。 |
| [Lieflat Charts](lieflat-charts.zh.md) | ✅ | C（3/5） | 数据可视化路线：模板锁定的图表与双语 HTML 报告，双击即开的单文件；很年轻、单人维护，PolyForm Noncommercial 许可让对外商用要付费授权。 |

## 什么该放这里

主要产物是**发布用视觉内容**的 agent skill：社交卡片、封面、文章配图、金句卡，以及相关渲染产物。
