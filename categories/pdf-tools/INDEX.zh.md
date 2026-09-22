# pdf-tools

> 分类节点。渲染、读取与处理 PDF 文件。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **PDF.js** | 当你需要在浏览器/Node 里渲染或读取 PDF（Firefox 的引擎）时用它——它不创建也不编辑 PDF。 | A（6/6） | [→](pdfjs.zh.md) |
| **pdf-lib** | 当你需要在 JS/TS 里创建或修改 PDF——在浏览器、Node、Deno 或 React Native 中——且不需要原生依赖时用它。 | C（4/6） | [→](pdf-lib.zh.md) |
| **jsPDF** | 当你需要在浏览器里从 HTML、文本和图形生成客户端 PDF——它只创建不编辑已有 PDF——时用它。 | B（6/6） | [→](jspdf.zh.md) |
| **PyMuPDF** | PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents. | B（6/6） | [→](pymupdf.zh.md) |
| **pdfplumber** | Plumb a PDF for detailed information about each char, rectangle, line, et cetera — and easily extract text and tables. | B（6/6） | [→](pdfplumber.zh.md) |
| **OCRmyPDF** | OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched | B（6/6） | [→](ocrmypdf.zh.md) |
| **qpdf** | qpdf: A content-preserving PDF document transformer | B（6/6） | [→](qpdf.zh.md) |
| **SAPP** | 当 PHP 应用必须用 PKCS#12 证书追加签名，同时保留已有 PDF 的修订与对象图时用它；不适合加密 PDF、广泛修复或要求独立验证 PAdES／LTV 的场景。 | B（5/6） | [→](sapp.zh.md) |
| **FPDI** | 当基于 FPDF／TCPDF／tFPDF 的 PHP 应用要把已有 PDF 的页面当模板导入时用它——免费解析器不支持加密文件与压缩交叉引用流。 | A（5/6） | [→](fpdi.zh.md) |
| **pyHanko** | 当 Python 需要按成文记录的 PAdES／LTV 流程创建或验证 PDF 签名时用它——上游仍自标 beta。 | A（6/6） | [→](pyhanko.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [PDF.js](pdfjs.zh.md) | ✅ | A（6/6） | 当你需要在浏览器/Node 里渲染或读取 PDF（Firefox 的引擎）时用它——它不创建也不编辑 PDF。 |
| [pdf-lib](pdf-lib.zh.md) | ✅ | C（4/6） | 当你需要在 JS/TS 里创建或修改 PDF——在浏览器、Node、Deno 或 React Native 中——且不需要原生依赖时用它。 |
| [jsPDF](jspdf.zh.md) | ✅ | B（6/6） | 当你需要在浏览器里从 HTML、文本和图形生成客户端 PDF——它只创建不编辑已有 PDF——时用它。 |
| [SAPP](sapp.zh.md) | ✅ | B（5/6） | PHP 原生增量 PDF 签名与对象操作，可保留修订；规范覆盖比 qpdf 窄，也缺少独立验证的 PAdES／LTV 证据。 |
| [FPDI](fpdi.zh.md) | ✅ | A（5/6） | 在 PHP 写入库里把已有 PDF 的页面当模板导入；免费解析器不支持加密 PDF 与压缩交叉引用流。 |
| [pyHanko](pyhanko.zh.md) | ✅ | A（6/6） | Python 的 PDF 签名、时间戳与验证，带成文记录的 PAdES/LTV 流程；上游仍自标 beta。 |
| OpenPDFSign | 未收录 | — | 各页点到的独立 Java 签名命令行工具。 |

## 什么该放这里

主要职责是**渲染、读取或处理 PDF 文件**的工具——查看器、解析器、生成器与编辑器。不含把文档解析成结构化 Markdown/JSON 供 gen-AI 消费（见 `document-parsing`），不含 OCR 引擎（见 `ocr`）。
