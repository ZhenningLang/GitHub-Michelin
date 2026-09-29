# pdf-tools

> 分类节点。渲染、读取与处理 PDF 文件。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 子分类 | 何时进入 | 路由 |
| --- | --- | --- |
| **PDF 生成** | 你要在应用代码里做出一份新 PDF（发票、面单、报告、拼装文档）。 | [→](pdf-generation/INDEX.zh.md) |
| **PDF 渲染与提取** | 你要显示一份 PDF，或从中取出文本、表格、坐标。 | [→](pdf-reading/INDEX.zh.md) |
| **PDF 改写与签名** | 你手里已有 PDF，要在保住原内容的前提下修复、拆合、变成可搜索，或给它签名。 | [→](pdf-transform-signing/INDEX.zh.md) |
| **PDF 翻译** | 一份（科研）PDF 要翻译，而且译后还得像原文的样子。 | [→](pdf-translation/INDEX.zh.md) |

## 对比矩阵

| 选项 | 类型 | 一句话取舍 |
| --- | --- | --- |
| [PDF 生成](pdf-generation/INDEX.zh.md) | 子分类 | 在代码里创建新 PDF——从零绘制、从 HTML 或组件生成，或把导入的页面拼成新文档。 |
| [PDF 渲染与提取](pdf-reading/INDEX.zh.md) | 子分类 | 把 PDF 渲染出来给人看，或用程序读出其中的文本、表格与版面对象。 |
| [PDF 改写与签名](pdf-transform-signing/INDEX.zh.md) | 子分类 | 原地改写已有 PDF——结构变换、叠加 OCR 文本层，或保留修订历史的数字签名。 |
| [PDF 翻译](pdf-translation/INDEX.zh.md) | 子分类 | 翻译 PDF 并保住版式、公式与分栏。 |

## 什么该放这里

主要职责是**渲染、读取或处理 PDF 文件**的工具——按你对 PDF 做的动作导航：生成新文件、读出内容、改写或签名已有文件，还是保版式翻译。不含把文档解析成结构化 Markdown/JSON 供 gen-AI 消费（见 `document-parsing`），不含 OCR 引擎（见 `ocr`），不含把 PDF 拍扁成文本的双语电子书 CLI（见 `reading-tools`）。
