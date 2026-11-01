# visual-content

> [agent-skills](../INDEX.zh.md) 的分类节点。直属技能生成可执行 HTML／canvas 图表、社交卡片与贴纸；图像模型艺术指导进入子分类。
> ← 上层 [agent-skills](../INDEX.zh.md) · 根[路由](../../../INDEX.zh.md) · English：[INDEX.md](INDEX.md)

## 子分类

| 分类 | 内容 | 路由 |
| --- | --- | --- |
| **image-art-direction** | 提示词、风格配方与构图规则；由宿主图像模型生图。 | [→](image-art-direction/INDEX.zh.md) |

## 本分类集合

| 集合 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **teardown** | 让编码 agent 制作可拆解机器讲解网页和 60 帧视频，复用运动学并用截图拼图自查；只是两天大的模板，不是工程仿真。 | C（4/5） | [→](teardown.zh.md) |
| **fun-isometric** | 让助手用复用动作帧绘制、绑定可修改的画布贴纸；附渲染检查，不是通用动画平台。 | C（4/5） | [→](fun-isometric.zh.md) |
| **Guizang Social Card Skill** | 当你在 Claude Code/Codex 里想让 agent 用锁定的编辑风/瑞士风生成小红书图文或公众号封面对（单文件 HTML 渲染成 PNG）时使用。 | D（3/5） | [→](guizang-social-card.zh.md) |
| **Lieflat Charts** | 当你想让编码助手把数据做成模板锁定、可直接发布的单文件 HTML 图表或 12 套中英双语整页报告、整套交付共用一种编辑风视觉语言时用它。 | C（3/5） | [→](lieflat-charts.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [teardown](teardown.zh.md) | 已收录 | C（4/5） | 三个完整 3D 机构和网页转影片流程；需要 GPU 渲染，并手动补回构建时剥离的第三方声明。 |
| [fun-isometric](fun-isometric.zh.md) | 已收录 | C（4/5） | 外观受限的动态贴纸组件，支持本地渲染；仅一天历史，须审查浏览器下载与许可正文保留。 |
| [Guizang Social Card Skill](guizang-social-card.zh.md) | ✅ | D（3/5） | 把社交卡片和封面做成 HTML 到 PNG 产物；很年轻且 AGPL。 |
| [Guizang PPT Skill](../slides-ppt/guizang-ppt.zh.md) | ✅ | C（4/5） | 当产物是完整 deck、不是独立卡片或文章配图时选它。 |
| [HTML Anything](../../ai-design-generation/html-anything.zh.md) | ✅ | B（5/6） | 更宽的 HTML 产物生成器；不如本叶子聚焦某个视觉内容表面。 |
| [Lieflat Charts](lieflat-charts.zh.md) | ✅ | C（3/5） | 数据可视化路线：模板锁定的图表与双语 HTML 报告，双击即开的单文件；很年轻、单人维护，PolyForm Noncommercial 许可让对外商用要付费授权。 |

## 什么该放这里

直属条目通过可执行 HTML／canvas 生成可编辑的发布用视觉内容。提示词驱动的图像艺术指导进入 [image-art-direction](image-art-direction/INDEX.zh.md)；生图应用与运行时归入 [ai-design-generation](../../ai-design-generation/INDEX.zh.md)。
