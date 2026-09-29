# pdf-reading

> 分类节点。把 PDF 渲染出来给人看，或用程序读出其中的文本、表格与版面对象。
> ← 返回[pdf-tools](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **PDF.js** | 当你需要在浏览器/Node 里渲染或读取 PDF（Firefox 的引擎）时用它——它不创建也不编辑 PDF。 | A（6/6） | [→](pdfjs.zh.md) |
| **PyMuPDF** | PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents. | B（6/6） | [→](pymupdf.zh.md) |
| **pdfplumber** | Plumb a PDF for detailed information about each char, rectangle, line, et cetera — and easily extract text and tables. | B（6/6） | [→](pdfplumber.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [PDF.js](pdfjs.zh.md) | ✅ | A（6/6） | 当你需要在浏览器/Node 里渲染或读取 PDF（Firefox 的引擎）时用它——它不创建也不编辑 PDF。 |
| [PyMuPDF](pymupdf.zh.md) | ✅ | B（6/6） | PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents. |
| [pdfplumber](pdfplumber.zh.md) | ✅ | B（6/6） | Plumb a PDF for detailed information about each char, rectangle, line, et cetera — and easily extract text and tables. |

## 什么该放这里

**读取** PDF 的查看器、渲染器与底层解析库：页面渲染、文本与表格提取、逐字符几何信息。不含把文档解析成结构化 Markdown/JSON 供 gen-AI 消费（见 `document-parsing`），不含 OCR 引擎（见 `ocr`）。
