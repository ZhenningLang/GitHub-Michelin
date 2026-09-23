# document-parsing

> 分类节点。把文档（PDF/DOCX/…）解析/转换成结构化 Markdown/JSON，供 gen-AI 消费。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Docling** | 当你需要把杂乱的 PDF/DOCX/PPTX 解析成干净的结构化 Markdown/JSON 以喂给 RAG 时用它——是解析器，不是文档管理系统。 | A（6/6） | [→](docling.zh.md) |
| **MarkItDown** | 当你需要一个轻量级 Python 库把各类办公文档和文件转成 Markdown 以喂给 LLM 时用它——比 Docling 更简单，但对版面感知较弱。 | B（6/6） | [→](markitdown.zh.md) |
| **olmOCR** | 当你需要把带公式、表格、手写体和多栏版面的复杂 PDF 转成干净 Markdown 以用于 LLM 训练数据集时用它——需要 GPU。 | C（5/6） | [→](olmocr.zh.md) |
| **Marker** | Convert PDF to markdown + JSON quickly with high accuracy | B（5/6） | [→](marker.zh.md) |
| **unstructured** | Convert documents to structured data effortlessly. Unstructured is open-source ETL solution for transforming complex documents into clean, structured formats for language models.  Visit our website to learn more about our enterprise grade Platform product for production grade workflows, partitioning, enrichments, chunking and embedding. | A（6/6） | [→](unstructured.zh.md) |
| **any2html** | Use it when you need any2html in this category. | D（5/6） | [→](any2html.zh.md) |
| **Dedoc** | 当内网 Python 管线需要把多格式文档恢复为含层级、表格、注解与附件的逻辑树时用它；要接受较重的 Linux 与系统包依赖，以及对困难扫描件的限制。 | B（5/6） | [→](dedoc.zh.md) |
| **Bella Domify** | 当中文 RAG 摄取需要细粒度 PDF／Office DOM 树和 FastAPI／Kafka／S3 服务集成时用它；许可证声明冲突、可选远端 OCR 与重基础设施是决定性门槛。 | C（5/6） | [→](bella-domify.zh.md) |
| **MinerU Skill** | 当 coding agent 需要通过 CLI／MCP 一条命令把文档交给 MinerU 云端转成 Markdown，并需要批处理、续传或内容工具投递时用它；文件会跨服务边界，且受配额和 API 变化约束。 | C（5/6） | [→](mineru-skill.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Docling](docling.zh.md) | ✅ | A（6/6） | 富文档解析（版面 + 表格）成结构化 Markdown/JSON；模型依赖比纯文本提取更重。 |
| [MarkItDown](markitdown.zh.md) | ✅ | B（6/6） | 轻量级 Python 库，将办公文档和文件转换为 Markdown 供 LLM 摄入；比 Docling 更简单，但版面感知较弱。 |
| [olmOCR](olmocr.zh.md) | ✅ | C（5/6） | 基于 VLM 的 PDF 线性化，面向 LLM 数据集；支持公式、表格和手写体，但需要 GPU。 |
| [PageIndex](../rag-retrieval/pageindex.zh.md) | ✅ | B（6/6） | 在长结构化文档上建检索索引——位于解析之后，本身不是解析器。 |
| [any2html](any2html.zh.md) | ✅ | D（5/6） | Use it when you need any2html in this category. |
| [Dedoc](dedoc.zh.md) | ✅ | B（5/6） | 多格式逻辑树解析，保留表格、注解与附件；结构比轻量 Markdown 转换更深，但 Linux 依赖更重，对困难扫描件也有限制。 |
| [Bella Domify](bella-domify.zh.md) | ✅ | C（5/6） | 提供 pdf2docx 衍生 DOM 树和服务集成；版面对象丰富，但基础设施重、OCR 可出站，且 GPL v2／v3 声明冲突未解决。 |
| [MinerU Skill](mineru-skill.zh.md) | ✅ | C（5/6） | 面向 agent 的 MinerU 云 API CLI／MCP，带批处理、续传和投递；免本地模型部署，但承担上传、配额和第三方 API 风险。 |
| LlamaParse / self-hosted MinerU | 未收录 | — | 各页点到的云端与自托管文档解析路径。 |


## 什么该放这里

主要职责是把**文档解析/转换成结构化表示**供 gen-AI/RAG 用的库。不含检索/索引本身（见 `rag-retrieval`），不含文档归档/检索（见 `document-management`），不含纯 OCR（见 `ocr`）。
