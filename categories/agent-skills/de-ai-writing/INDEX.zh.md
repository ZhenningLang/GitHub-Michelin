# de-ai-writing

> [agent-skills](../INDEX.zh.md) 的叶子。去 AI 味、消除机器腔、让文本更像真人写作。
> ← 上层 [agent-skills](../INDEX.zh.md) · 根[路由](../../../INDEX.zh.md) · English：[INDEX.md](INDEX.md)

## 本叶子条目

| 条目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Humanizer-zh** | 一个简体中文 Claude Code 单技能，按约 24 条清单改写掉文本里的 AI 痕迹，是 blader/humanizer 的本地化版。 | C（4/6） | [→](humanizer-zh.zh.md) |
| **De-AI-Prompt-Enhancer-Writer-Booster-SKILL** | 中文去 AI 味套件，含 `de-AI-writing` 和 `good-writing` 两个 SKILL 文件夹；适合作者风格复现，但许可证不清。 | C（4/6） | [→](de-ai-prompt-enhancer-writer-booster-skill.zh.md) |
| **shuorenhua** | 中文优先的去 AI 味改写 skill，带 protected spans、场景规则、多 harness 文档和 MIT 许可证。 | B（4/6） | [→](shuorenhua.zh.md) |
| **ai-flavor-remover** | 中文单文件 prompt 片段；作者标注只在 Gemini 2.5 Pro 上测试过，不是可安装 skill-pack。 | D（4/6） | [→](ai-flavor-remover.zh.md) |
| **humanizer** | 英文上游 Claude Code skill，用于清理 AI 写作痕迹，带 plugin / install 文档和 MIT 许可证。 | B（4/6） | [→](humanizer.zh.md) |
| **stop-slop** | 短小强硬的英文 prose 去机器腔 skill，适合快速清理，不适合细腻正式文体。 | B（4/6） | [→](stop-slop.zh.md) |
| **avoid-ai-writing** | 英文优先的去 AI 味 skill：自带零依赖 npm 检测器、按命中数卡的 CI / pre-commit 门禁，以及一份公开自身误报率的人控语料。 | B（5/6） | [→](avoid-ai-writing.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Humanizer-zh](humanizer-zh.zh.md) | ✅ | C（4/6） | 中文优先的去 AI 味 skill；作为当前索引里的基线使用。 |
| [Baoyu Skills](../writing/content-production/baoyu-skills.zh.md) | ✅ | B（4/6） | 更宽的中文内容 / 发布套件；Humanizer-zh 更窄，聚焦去 AI 味改写。 |
| 自写 voice guide | 未收录 | — | 更适合一个私有作者或品牌 voice；但不如公共 skill 可复用。 |
| [De-AI-Prompt-Enhancer-Writer-Booster-SKILL](de-ai-prompt-enhancer-writer-booster-skill.zh.md) | ✅ | C（4/6） | 更重的中文 writer-booster 流程；适合作者风格复现，许可证清晰度和中性表达是风险。 |
| [shuorenhua](shuorenhua.zh.md) | ✅ | B（4/6） | 当前更适合作为中文优先、保事实去 AI 味的候选，尤其需要多 harness 复用和 protected spans 时。 |
| [ai-flavor-remover](ai-flavor-remover.zh.md) | ✅ | D（4/6） | 作为 Gemini 测过的 prompt 标本看待，不要当成 OSS 依赖或 Agent Skills 包。 |
| [humanizer](humanizer.zh.md) | ✅ | B（4/6） | 英文上游基线较强且有安装文档；中文 prose 优先看中文本地化方案。 |
| [stop-slop](stop-slop.zh.md) | ✅ | B（4/6） | 最短的英文强规则去机器腔清单；正式 prose 更容易被过度编辑。 |
| [avoid-ai-writing](avoid-ai-writing.zh.md) | ✅ | B（5/6） | 英文档里工程化程度最高：需要去 AI 味流程产出可设 CI 门禁的命中数时选它，而不是拿它的分数去判定作者身份。 |


## 什么该放这里

主要职责是**去除 AI 写作痕迹**、让文本更像真人、保事实改 voice，或执行真人编辑风格规则的 agent skill、prompt 仓库或写作辅助工具。
