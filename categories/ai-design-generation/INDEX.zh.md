# ai-design-generation

> 分类节点。agent 驱动的 UI/设计、HTML 产物与图像生成应用和工具。可移植 skill pack 现在放在 [agent-skills](../agent-skills/INDEX.zh.md)。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **json-render** | 当模型必须用你已有的组件在应用里拼界面、而不是发明 JSX 或新设计系统时用它。 | B（6/6） | [→](json-render.zh.md) |
| **HTML Anything** | 当你本机已登录某个 coding-agent CLI、想要零 API key、local-first 地把 Markdown 变成可交付 HTML 并一键导出微信/X/知乎时用它。 | B（5/6） | [→](html-anything.zh.md) |
| **Open Design** | 想要一个 local-first、BYOK 的桌面 studio，让编码 agent 产出 HTML 原型、deck、图像和 HTML→MP4 动效时用它。 | B（6/6） | [→](open-design.zh.md) |
| **Impeccable** | 当你的 AI agent 总是产出同质化前端「AI 味」、需要确定性检测加设计 critique 时使用。 | B（6/6） | [→](impeccable.zh.md) |
| **open-slide** | 想让编码 agent 在固定 1920×1080 画布上写 React 幻灯片、你靠点选元素留言来改稿时用它——deck 要作为可编辑 PowerPoint 文件流转、或要在 CI 里无头导出时不适合。 | C（6/6） | [→](open-slide.zh.md) |
| **SdPaint** | 当你已在跑带 ControlNet 的 AUTOMATIC1111、想让每一笔涂鸦实时变成生成图时用它——但它自身不带模型，且自 2024-04 起停滞。 | D（3/6） | [→](sdpaint.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [json-render](json-render.zh.md) | ✅ | B（6/6） | 当模型必须用你已有的组件在应用里拼界面、而不是发明 JSX 或新设计系统时用它。 |
| [HTML Anything](html-anything.zh.md) | ✅ | B（5/6） | 当你本机已登录某个 coding-agent CLI、想要零 API key、local-first 地把 Markdown 变成可交付 HTML 并一键导出微信/X/知乎时用它。 |
| [Open Design](open-design.zh.md) | ✅ | B（6/6） | 想要一个 local-first、BYOK 的桌面 studio，让编码 agent 产出 HTML 原型、deck、图像和 HTML→MP4 动效时用它。 |
| [Impeccable](impeccable.zh.md) | ✅ | B（6/6） | 当你的 AI agent 总是产出同质化前端「AI 味」、需要确定性检测加设计 critique 时使用。 |
| [open-slide](open-slide.zh.md) | ✅ | C（6/6） | 想让编码 agent 在固定 1920×1080 画布上写 React 幻灯片、你靠点选元素留言来改稿时用它——deck 要作为可编辑 PowerPoint 文件流转、或要在 CI 里无头导出时不适合。 |
| [SdPaint](sdpaint.zh.md) | ✅ | D（3/6） | 换来在自己 GPU 上“靠画不靠写 prompt”的迭代循环；代价是得先搭好 A1111 加 ControlNet，而客户端无人维护，可能与后端 API 渐行渐远。 |
| [Guizang PPT Skill](../agent-skills/slides-ppt/guizang-ppt.zh.md) | ✅ | C（4/5） | 可移植的 deck 生成 skill；因为消费单元是 skill pack，已迁到 agent-skills。 |
| [Guizang Social Card Skill](../agent-skills/visual-content/guizang-social-card.zh.md) | ✅ | D（3/5） | 可移植的社交卡片 skill；因为它装进 agent harness，已迁到 agent-skills。 |
| [ian-xiaohei-illustrations](../agent-skills/visual-content/ian-illustrations.zh.md) | ✅ | B（4/5） | 可移植的文章配图 skill；因为它作为 skill 被选择，已迁到 agent-skills。 |
| v0 / Lovable / tldraw make-real | 未收录 | — | 各页对比里点到的其他 agent 化 UI/设计生成器。 |

## 什么该放这里

职责是用 agent **生成视觉/设计产物**（UI、HTML、图像、幻灯片、卡片）的工具和应用。主要价值是装进 agent harness 的可移植 skill pack，应放到 `agent-skills`。
