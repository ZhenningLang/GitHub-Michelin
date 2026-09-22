# translation

> [ai-writing](../INDEX.zh.md) 的叶子。整文档、整书翻译技能——把 PDF／DOCX／EPUB 通过 coding agent 翻成目标语言的文件流水线。
> ← 上层 [ai-writing](../INDEX.zh.md) · 根 [路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **translate-book** | 面向 Codex／Claude Code／OpenClaw 的 agent skill：并行 subagent 翻译整本书（PDF/DOCX/EPUB），带术语表钉定和相邻上下文一致性机制。 | B（4/6） | [→](translate-book.zh.md) |
| **claude_translater** | 极简 shell＋Claude CLI 脚本，翻译 PDF/DOCX/EPUB（和 PPTX）——translate-book 的灵感来源，但已不维护且无许可证。 | D（4/6） | [→](claude-translater.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [translate-book](translate-book.zh.md) | ✅ | B（4/6） | 整书翻译的 agent skill 形态：并行 subagent、术语表、断点续跑、多格式输出——但项目年轻、单人维护、绑死 Calibre／Pandoc。 |
| [claude_translater](claude-translater.zh.md) | ✅ | D（4/6） | translate-book 的 shell 脚本原型；只有要随手可改的脚本或 PPTX 翻译时才选——无许可、已不维护。 |

## 什么该放这里

面向**整文档／整书翻译**的技能。翻译只是更大内容工作流里一步的，放到 [content-production](../content-production/INDEX.zh.md)。
