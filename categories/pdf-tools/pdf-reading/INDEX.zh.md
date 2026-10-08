# pdf-reading

> 分类节点。把 PDF 渲染出来给人看，或用程序读出其中的文本、表格与版面对象。
> ← 返回[pdf-tools](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **PDF.js** | 当你需要在浏览器/Node 里渲染或读取 PDF（Firefox 的引擎）时用它——它不创建也不编辑 PDF。 | A（6/6） | [→](pdfjs.zh.md) |
| **PyMuPDF** | 当大批量的 Python 流水线要在一个快速、离线的包里完成带坐标的文字和表格抽取、页面渲染、涂黑和合并时用它——但它是 AGPL-3.0，闭源软件或 SaaS 要用就得买 Artifex 的商业许可。 | B（6/6） | [→](pymupdf.zh.md) |
| **pdfplumber** | 当机器生成的 PDF（申报文件、通知、价目表）里的表格被抽得糊成一团，你需要字符坐标和可视化调试来把每一行调对时用它——但它没有 OCR，处理不了扫描件。 | B（6/6） | [→](pdfplumber.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [PDF.js](pdfjs.zh.md) | ✅ | A（6/6） | 当你需要在浏览器/Node 里渲染或读取 PDF（Firefox 的引擎）时用它——它不创建也不编辑 PDF。 |
| [PyMuPDF](pymupdf.zh.md) | ✅ | B（6/6） | 一句 pip install 背后是 MuPDF 的 C 引擎，读取、渲染、编辑全包；代价是 AGPL 或付费二选一，Office 支持要另付费，给的是底层字形而不是文档结构。 |
| [pdfplumber](pdfplumber.zh.md) | ✅ | B（6/6） | MIT 许可、纯 Python，每个字符、线条、矩形都能查看和调参；代价是速度远不如 PyMuPDF，项目只靠一位维护者。 |

## 什么该放这里

**读取** PDF 的查看器、渲染器与底层解析库：页面渲染、文本与表格提取、逐字符几何信息。不含把文档解析成结构化 Markdown/JSON 供 gen-AI 消费（见 `document-parsing`），不含 OCR 引擎（见 `ocr`）。
