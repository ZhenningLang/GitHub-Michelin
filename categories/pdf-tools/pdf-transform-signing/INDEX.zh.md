# pdf-transform-signing

> 分类节点。原地改写已有 PDF——结构变换、叠加 OCR 文本层，或保留修订历史的数字签名。
> ← 返回[pdf-tools](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **qpdf** | 当脚本要合并、拆分、重排、加密、线性化或修复 PDF，又不能让页面、字体、表单域被重新渲染时用它——但它不渲染、不抽文字、不画新内容，也不做签名。 | A（6/6） | [→](qpdf.zh.md) |
| **OCRmyPDF** | 当扫描仪不断往文件夹里丢只有图片的 PDF，你想让无人值守的任务把它们原样变成可搜索、可复制的文件（可选 PDF/A）时用它——但它产出的是带隐藏文字层的 PDF，不是给 RAG 用的 Markdown。 | B（6/6） | [→](ocrmypdf.zh.md) |
| **SAPP** | 当 PHP 应用必须用 PKCS#12 证书追加签名，同时保留已有 PDF 的修订与对象图时用它；不适合加密 PDF、广泛修复或要求独立验证 PAdES／LTV 的场景。 | B（5/6） | [→](sapp.zh.md) |
| **pyHanko** | 当 Python 需要按成文记录的 PAdES／LTV 流程创建或验证 PDF 签名时用它——上游仍自标 beta。 | A（6/6） | [→](pyhanko.zh.md) |
| **PdfCraft** | 当 macOS、Windows 或 Linux 上的人需要一个离线、免账号的桌面应用来整理、批注、填写、涂黑和加密 PDF（或让 agent 经 MCP 做同样的事）时用它——但它才九天大、尚未 1.0，渲染器是借的，与 Acrobat 的保真度也没测过。 | C（5/6） | [→](pdfcraft.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [qpdf](qpdf.zh.md) | ✅ | A（6/6） | 近 20 年的命令行工具，任何语言都能调，页面内容逐字节保留；代价是只做结构层面的操作，核心团队只有两个人。 |
| [OCRmyPDF](ocrmypdf.zh.md) | ✅ | B（6/6） | 原页面图像不动，垫上对齐的 OCR 文字层并校验输出；代价是 Tesseract 对手写和手机拍照很弱，路线图系于一位维护者。 |
| [SAPP](sapp.zh.md) | ✅ | B（5/6） | PHP 原生增量 PDF 签名与对象操作，可保留修订；规范覆盖比 qpdf 窄，也缺少独立验证的 PAdES／LTV 证据。 |
| [pyHanko](pyhanko.zh.md) | ✅ | A（6/6） | Python 的 PDF 签名、时间戳与验证，带成文记录的 PAdES/LTV 流程；上游仍自标 beta。 |
| [PdfCraft](pdfcraft.zh.md) | ✅ | C（5/6） | 免费的原生 Acrobat 式桌面工作台，只追加式保存，还带 MCP 工具接口；代价是只有九天的记录、渲染靠借、代码由单一厂商的 agent 编写。 |
| OpenPDFSign | 未收录 | — | 各页点到的独立 Java 签名命令行工具。 |

## 什么该放这里

输入和输出都是**已有 PDF** 的工具、库与桌面工作台：保内容的结构变换、给扫描件叠 OCR 文本层、增量更新式签名与验签（PAdES、PKCS#12、时间戳）。不含生成新文档（见 `pdf-generation`），不含独立 OCR 引擎（见 `ocr`）。
