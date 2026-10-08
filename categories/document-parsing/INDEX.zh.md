# document-parsing

> 分类节点。把文档（PDF/DOCX/…）解析/转换成结构化 Markdown/JSON，供 gen-AI 消费。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Docling** | 当你需要把杂乱的 PDF/DOCX/PPTX 解析成干净的结构化 Markdown/JSON 以喂给 RAG 时用它——是解析器，不是文档管理系统。 | A（5/6） | [→](docling.zh.md) |
| **MarkItDown** | 当 agent 或 RAG 流水线要用一次轻量 Python 调用，把混杂的 Office 文件、HTML、EPUB 和简单 PDF 统一转成 Markdown 时用它——但扫描件或复杂版面 PDF 要用 Marker 或 Docling，它没有 OCR 和版面模型。 | B（6/6） | [→](markitdown.zh.md) |
| **olmOCR** | 当你要把成千上万份带公式、表格、多栏版面的 PDF 按阅读顺序转成干净 Markdown、拿去做 LLM 语料时用它——但本地运行要 12 GB 以上显存的 NVIDIA GPU，且上游自 2026-03 起已无提交。 | C（5/6） | [→](olmocr.zh.md) |
| **Marker** | 当你要在自己的机器上把几千份 PDF（论文、教材、扫描件）转成带真表格、LaTeX 公式、按需 OCR 的 Markdown 时用它——但模型权重只对融资或营收低于 500 万美元的主体免费。 | B（6/6） | [→](marker.zh.md) |
| **unstructured** | 当 RAG 流水线面对混杂的 PDF、邮件和 Office 文件，需要带页码元数据的类型化元素和按章节分块，而不只是一个 Markdown 字符串时用它——但开源版的 PDF 表格准确率不如 Docling 和 Marker，且默认开启统计回传。 | A（6/6） | [→](unstructured.zh.md) |
| **any2html** | Use it when you need any2html in this category. | D（5/6） | [→](any2html.zh.md) |
| **Dedoc** | 当内网 Python 管线需要把多格式文档恢复为含层级、表格、注解与附件的逻辑树时用它；要接受较重的 Linux 与系统包依赖，以及对困难扫描件的限制。 | B（5/6） | [→](dedoc.zh.md) |
| **Bella Domify** | 当中文 RAG 摄取需要细粒度 PDF／Office DOM 树和 FastAPI／Kafka／S3 服务集成时用它；许可证声明冲突、可选远端 OCR 与重基础设施是决定性门槛。 | C（5/6） | [→](bella-domify.zh.md) |
| **MinerU Skill** | 当 coding agent 需要通过 CLI／MCP 一条命令把文档交给 MinerU 云端转成 Markdown，并需要批处理、续传或内容工具投递时用它；文件会跨服务边界，且受配额和 API 变化约束。 | C（5/6） | [→](mineru-skill.zh.md) |
| **anydoc** | 当管线收到一堆混杂的 Office（含老 .doc/.ppt/.xls）、OpenDocument、RTF、EPUB 和文字版 PDF，需要毫秒级转成风格一致的 Markdown、又不想装 LibreOffice 或模型时用它；不做 OCR，扫描页会直接失败。 | B（6/6） | [→](anydoc.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Docling](docling.zh.md) | ✅ | A（5/6） | 富文档解析（版面 + 表格）成结构化 Markdown/JSON；模型依赖比纯文本提取更重。 |
| [MarkItDown](markitdown.zh.md) | ✅ | B（6/6） | 换来广泛的格式覆盖、无需 GPU 和模型，代价是版面还原能力弱，部分可选功能还会把文件发给外部大模型或 Azure。 |
| [olmOCR](olmocr.zh.md) | ✅ | C（5/6） | 换来 VLM 级的公式与脏扫描件还原；代价是每页都要 GPU 推理——版面保真不那么要紧时，纯 CPU 的 Docling 或 PyMuPDF 更便宜。 |
| [PageIndex](../rag-retrieval/structured-retrieval/pageindex.zh.md) | ✅ | B（6/6） | 在长结构化文档上建检索索引——位于解析之后，本身不是解析器。 |
| [any2html](any2html.zh.md) | ✅ | D（5/6） | Use it when you need any2html in this category. |
| [Dedoc](dedoc.zh.md) | ✅ | B（5/6） | 多格式逻辑树解析，保留表格、注解与附件；结构比轻量 Markdown 转换更深，但 Linux 依赖更重，对困难扫描件也有限制。 |
| [Bella Domify](bella-domify.zh.md) | ✅ | C（5/6） | 提供 pdf2docx 衍生 DOM 树和服务集成；版面对象丰富，但基础设施重、OCR 可出站，且 GPL v2／v3 声明冲突未解决。 |
| [MinerU Skill](mineru-skill.zh.md) | ✅ | C（5/6） | 面向 agent 的 MinerU 云 API CLI／MCP，带批处理、续传和投递；免本地模型部署，但承担上传、配额和第三方 API 风险。 |
| [anydoc](anydoc.zh.md) | ✅ | B（6/6） | 纯 Rust 转换器，覆盖 20 多种办公、电子书和 PDF 扩展名，带 Node/Python/WASM 绑定；快且无依赖，但不做 OCR、PDF 表格靠启发式，且是年轻的单人 0.x 项目。 |
| LlamaParse / self-hosted MinerU | 未收录 | — | 各页点到的云端与自托管文档解析路径。 |


## 什么该放这里

主要职责是把**文档解析/转换成结构化表示**供 gen-AI/RAG 用的库。不含检索/索引本身（见 `rag-retrieval`），不含文档归档/检索（见 `document-management`），不含纯 OCR（见 `ocr`）。
