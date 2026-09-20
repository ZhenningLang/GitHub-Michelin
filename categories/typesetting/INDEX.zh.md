# typesetting

> 分类节点。把纯文本标记源编译成排版成品——印刷 PDF、网页、幻灯片、书或文档集。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Asciidoctor** | 当技术文档需要从纯文本源发布成 HTML、DocBook、EPUB 或 man page 时用它——但你需要排版引擎或印刷级 PDF 时不要用。 | C（4/6） | [→](asciidoctor.zh.md) |
| **LaTeX** | 当投稿方的 class 文件、几十年的宏包积累、或几十年稳定的源语言决定结果时用它——但没人愿意维护 `\begin{}` 脚手架、或你需要从同一份文件出 HTML 时不要用。 | B（6/6） | [→](latex.zh.md) |
| **Quarkdown** | 当你需要一份保持 Markdown 可读性的源文件编译成网页、印刷 PDF、reveal.js 幻灯片与文档站时用它——但交付物必须是 Word、许可必须宽松、或印刷保真度是硬要求时不要用。 | B（5/6） | [→](quarkdown.zh.md) |
| **Typst** | 当你能自己选源语言，想要学习曲线短、Apache-2.0 许可的印刷级 PDF 时用它——但投稿方指定 LaTeX class 文件、或源必须保持 Markdown 时不要用。 | A（6/6） | [→](typst.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Asciidoctor](asciidoctor.zh.md) | ✅ | C（4/6） | 当技术文档需要从纯文本源发布成 HTML、DocBook、EPUB 或 man page 时用它——但你需要排版引擎或印刷级 PDF 时不要用。 |
| [LaTeX](latex.zh.md) | ✅ | B（6/6） | 当投稿方的 class 文件、几十年的宏包积累、或几十年稳定的源语言决定结果时用它——但没人愿意维护 `\begin{}` 脚手架、或你需要从同一份文件出 HTML 时不要用。 |
| [Quarkdown](quarkdown.zh.md) | ✅ | B（5/6） | 当你需要一份保持 Markdown 可读性的源文件编译成网页、印刷 PDF、reveal.js 幻灯片与文档站时用它——但交付物必须是 Word、许可必须宽松、或印刷保真度是硬要求时不要用。 |
| [Typst](typst.zh.md) | ✅ | A（6/6） | 当你能自己选源语言，想要学习曲线短、Apache-2.0 许可的印刷级 PDF 时用它——但投稿方指定 LaTeX class 文件、或源必须保持 Markdown 时不要用。 |

## 什么该放这里

主要职责是**把纯文本标记源编译成排版成品**的工具——印刷级 PDF、分页文章、幻灯片、书或文档集。编译器与它的排版引擎才是产品本身。不含 Markdown **解析器**或转换器（见 `markdown-tools`），不含 PDF 阅读器与底层 PDF 写入库（见 `pdf-tools`），也不含把文档变成结构化数据供 gen-AI 消费的工具（见 `document-parsing`）。交叉说明：某个成员即使语法源自 Markdown，只要它的定义性特征是「产出文档成品」，就归在本分类。
