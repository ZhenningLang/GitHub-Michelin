# writing

> [agent-skills](../INDEX.zh.md) 的叶子。翻译、长文写作流程、编辑与发布流水线。专门的去 AI 味 / humanizer skill 放在 [de-ai-writing](../de-ai-writing/INDEX.zh.md)。
> ← 上层 [agent-skills](../INDEX.zh.md) · 根 [路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Baoyu Skills** | 宝玉出品的 20+ 个 coding agent 技能合集（翻译、markdown/HTML 排版、字幕与网页抓取、图片/图表/幻灯片生成），可装入 Claude Code、Codex 等支持 skill 的 harness。 | B（4/6） | [→](baoyu-skills.zh.md) |
| **Webnovel Writer** | 面向长篇连载小说的 Claude Code plugin：章节事实、检索、审稿、摘要和连续性状态。 | B（5/6） | [→](webnovel-writer.zh.md) |
| **huashu-skills** | 中文创作者工具箱，含 21 个文章、选题、调研、视频大纲、配图、PDF 导出和创作流程 skill。 | D（4/6） | [→](huashu-skills.zh.md) |
| **writing-agent** | 中文长文生产线，包含分阶段策划、证据账本、审稿、去 AI 味、事实核查闸门和最终 clean text。 | B（4/6） | [→](writing-agent.zh.md) |
| **marketingskills** | 面向 product marketing、CRO、copywriting、SEO、analytics、lifecycle email、ads 和 growth execution 的宽营销 skill pack。 | B（4/6） | [→](marketingskills.zh.md) |
| **open-seo** | 可自托管 SEO app，加 MCP 和 Agent Skills，用于关键词研究、排名跟踪、竞品、反链、审计和 AI visibility。 | B（5/6） | [→](open-seo.zh.md) |
| **translate-book** | 面向 Codex／Claude Code／OpenClaw 的 agent skill：并行 subagent 翻译整本书（PDF/DOCX/EPUB），带术语表钉定和相邻上下文一致性机制。 | B（4/6） | [→](translate-book.zh.md) |
| **claude_translater** | 极简 shell＋Claude CLI 脚本，翻译 PDF/DOCX/EPUB（和 PPTX）——translate-book 的灵感来源，但已不维护且无许可证。 | D（4/6） | [→](claude-translater.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Baoyu Skills](baoyu-skills.zh.md) | ✅ | B（4/6） | 宝玉出品的 20+ 个 coding agent 技能合集（翻译、markdown/HTML 排版、字幕与网页抓取、图片/图表/幻灯片生成），可装入 Claude Code、Codex 等支持 skill 的 harness。 |
| [Webnovel Writer](webnovel-writer.zh.md) | ✅ | B（5/6） | 最适合长篇连载连续性；GPL-3.0 和 Claude Code 绑定是主要取舍。 |
| [huashu-skills](huashu-skills.zh.md) | ✅ | D（4/6） | 宽中文创作者工具箱；许可证不清和 per-skill 安装路径让风险更高。 |
| [writing-agent](writing-agent.zh.md) | ✅ | B（4/6） | 严格中文文章生产线；比模块化 creator / writing skills 更重。 |
| [marketingskills](marketingskills.zh.md) | ✅ | B（4/6） | 最适合 SaaS / growth marketing；不是通用文章写作 pipeline。 |
| [open-seo](open-seo.zh.md) | ✅ | B（5/6） | SEO workflow 需要自托管 app、MCP 和 DataForSEO 付费数据时最合适。 |
| [translate-book](translate-book.zh.md) | ✅ | B（4/6） | 整书翻译的 agent skill 形态：并行 subagent、术语表、断点续跑、多格式输出——但项目年轻、单人维护、绑死 Calibre／Pandoc。 |
| [claude_translater](claude-translater.zh.md) | ✅ | D（4/6） | translate-book 的 shell 脚本原型；只有要随手可改的脚本或 PPTX 翻译时才选——无许可、已不维护。 |


## 什么该放这里

面向**写作任务**的技能合集——翻译、长文写作流程、编辑与发布流水线。专门的去 AI 味 / humanizer skill 放在 [de-ai-writing](../de-ai-writing/INDEX.zh.md)。
