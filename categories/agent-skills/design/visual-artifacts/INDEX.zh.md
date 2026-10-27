# visual-artifacts

> [design](../INDEX.zh.md) 的叶子。**交付物本身就是视觉产物**的 skill——可编辑技术图、HTML 原生原型、幻灯片、动画、信息图。它们生成的是供人查看的文件，而不是引导 UI 代码、也不是复制某个具名设计。
> ← 上层 [design](../INDEX.zh.md) · 根 [路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **baoyu-design** | 仅作信息收录：项目本地设计系统绑定及 HTML／PPTX／视频流程；提取内容权利未清，不批准安装或再分发。 | B（4/5） | [→](baoyu-design.zh.md) |
| **archify** | 面向架构、工作流、时序、数据流和生命周期图的 agent skill，输出自包含图表并带主题切换和导出控制。 | B（4/6） | [→](archify.zh.md) |
| **drawio-skill** | 一个 agent skill：把自然语言、代码、IaC 和接口 schema 变成可编辑的 `.drawio`，并能在源改动后重新同步而不丢手工版式。 | B（4/5） | [→](drawio-skill.zh.md) |
| **diagram-design** | 出可发表、套你品牌的图的 agent skill：先抓你网站的配色字体，再把 44 种编辑风格的图和图表画成单个 HTML+SVG 文件——代价是没有可编辑的源。 | B（4/5） | [→](diagram-design.zh.md) |
| **huashu-design** | 六个候选收敛为三个真实 HTML 初稿，带人工批准、本地视觉检查与外观记忆。 | B（5/6） | [→](huashu-design.zh.md) |
| **visual-explainer** | 把有来源的差异与方案变成图文 HTML，保留源码与反馈；不是可编辑图模型，默认也非完全离线。 | C（5/6） | [→](visual-explainer.zh.md) |
| **Anima** | 把静态生物课变成带来源的交互机制图；科学审查仍由你负责。 | C（4/5） | [→](anima.zh.md) |
| **AI Design Skills** | 规划落地页或把授权静态稿制作成展示流程；只有提示与录制片段，不是完整运行器或保真保证。 | C（4/5） | [→](ai-design-skills.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [baoyu-design](baoyu-design.zh.md) | ✅ | B（4/5） | 研究系统副本绑定与浏览器导出编排；根 MIT 不等于 Claude Design 提取内容已获授权。 |
| [archify](archify.zh.md) | ✅ | B（4/6） | 最适合技术图表；需要 WYSIWYG 编辑时用人工图表编辑器。 |
| [drawio-skill](drawio-skill.zh.md) | ✅ | B（4/5） | 交付物是可编辑、且要跟着真实源走的 `.drawio` 时最合适；图要保持纯文本用 Mermaid，不能装 draw.io 用 archify。 |
| [diagram-design](diagram-design.zh.md) | ✅ | B（4/5） | 图要发表、必须匹配品牌时最合适；图放在 git 里常改用 Mermaid，之后还要有人改用 drawio-skill。 |
| [huashu-design](huashu-design.zh.md) | ✅ | B（5/6） | 需要人工选方向的 HTML 产物时选它；组件交接看 Stitch，应用审美看 Taste-Skill。复用前应审查已披露的提示词来源。 |
| [visual-explainer](visual-explainer.zh.md) | ✅ | C（5/6） | 把有来源的差异与方案变成图文 HTML，保留源码与反馈；不是可编辑图模型，默认也非完全离线。 |
| [Anima](anima.zh.md) | ✅ | C（4/5） | 适合交互式生物结构，不是可编辑架构图；几何检查不验证科学论断。 |
| [AI Design Skills](ai-design-skills.zh.md) | ✅ | C（4/5） | 区分源稿保真、展示／网站动效与确定性录制说明；实现与内容真实性仍由宿主负责。 |


## 什么该放这里

**产出可视化交付物**的 agent skill——图文件、HTML 原型、deck、信息图、渲染动画。发布场景的视觉内容（社交卡片、文章配图）在 [visual-content](../../visual-content/INDEX.zh.md)，专门的 deck 工具链在 [slides-ppt](../../slides-ppt/INDEX.zh.md)；作用于落地 UI 代码的品味指导看 [ui-taste](../ui-taste/INDEX.zh.md)。
