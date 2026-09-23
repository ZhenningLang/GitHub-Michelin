---
name: Bella Domify
slug: bella-domify
repo: https://github.com/LianjiaTech/bella-domify
category: document-parsing
tags: [document-parsing, pdf, office, dom-tree, markdown, table-extraction, vision-ocr, fastapi]
language: Python
license: GPL-2.0-only
maturity: v0.1.6.8 package metadata, no GitHub releases, 86 stars (as of 2026-07)
last_verified: 2026-07-17
type: library
upstream:
  pushed_at: 2025-11-27T08:52:23Z
  default_branch: main
  default_branch_sha: d154bada09ca08331498e24d8875c9df8f651293
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:17:23Z
  overall: C
  overall_score: 1.6
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 36
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: C
      raw:
        repo_age_days: 401
        last_commit_age_days: 36
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.636
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: D
      raw:
        spdx_id: GPL-2.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
---

# Bella Domify

一个从 pdf2docx 衍生的 Python 文档解析器，为 PDF 和常见 Office 格式提供 layout 与 DOM tree 解析，并带可选视觉模型 OCR 和基于 Kafka/S3 的服务模式。

![Bella Domify — 健康度雷达](../../assets/health/bella-domify.zh.svg)

> **许可证冲突：** 仓库实际 `LICENSE` 文件是 GNU GPL version 2 正文，而 `setup.py` 声明 `license="GPL v3"`。Frontmatter 按许可证文件记录为 `GPL-2.0-only`；法律审查应把上游声明视为尚未解决。

## 何时使用

你在搭建中文知识库或 RAG 摄取服务，需要的不只是纯文本：应用希望把 PDF block、section、table、image、header 和 footer 表示为详细文档树，再转换成标准 DOM 或 Markdown。你愿意实现必需的图片存储 provider；如果启用图片 OCR，还会提供 OpenAI-compatible 视觉模型 provider 和用户上下文。Bella Domify 可以作为 Python 包直接转换，也可以通过 FastAPI 服务和异步 worker 运行。

如果 PDF 版面、表格、DOM tree、水印与页眉页脚处理以及评测 fixture 比最小安装更重要，选它而不是 MarkItDown。如果你想把 born-digital PDF 与 Office 的解析逻辑放进自己的进程，同时接受图片理解仍可能调用外部视觉模型，也可以选它而不是纯云端 parser wrapper。

## 何时不用

- **商业分发需要无歧义许可证。** 请改用 [Docling](docling.zh.md) 或 [Unstructured](unstructured.zh.md)；Bella Domify 的 GPL v2 许可证文件与 `setup.py` 中 GPL v3 声明冲突。
- **包括图片 OCR 在内的所有处理都必须离线。** 请改用 [Docling](docling.zh.md)、[Marker](marker.zh.md) 或自托管 OCR；Bella Domify 启用图片 OCR 后，会把图片 URL 发给 OpenAI-compatible vision endpoint。
- **需要有 tag、release 和更长公开稳定记录的解析器。** 请改用 [Docling](docling.zh.md) 或 [Unstructured](unstructured.zh.md)；Bella Domify 没有 GitHub release 或 tag，最后观察到的默认分支 push 在 2025-11。
- **不想实现存储/模型 provider，也不想运维服务基础设施。** 简单转换请用 [MarkItDown](markitdown.zh.md)，进程内解析可用 [Docling](docling.zh.md)；Bella Domify 的 library 配置要求 image provider，service 路径还连接 S3、Kafka 和 File API。
- **只需要快速 Office 转 Markdown。** 请改用 [MarkItDown](markitdown.zh.md)；Bella Domify 会安装 PyMuPDF、OpenCV、数据库、Kafka、云 SDK 和服务依赖，对更窄的任务没有必要。
- **选型前必须拿到可独立复现的准确率。** 请在自己的语料上对 [Docling](docling.zh.md)、[Marker](marker.zh.md) 和 Bella Domify 做 benchmark；仓库对比图基于有限内部评测集，本次没有复现。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Docling](docling.zh.md) | ✅ | 许可证清晰、release 更成熟、本地模型解析和标准 RAG 集成最重要时选 Docling；pdf2docx 衍生 DOM 模型和 provider 式服务集成正好匹配现有 Bella 风格技术栈时选 Bella Domify。 | Docling 更成熟且为 MIT；Bella Domify 暴露详细 PDF 内部结构与服务 hook，但许可证冲突且公开历史更短。 |
| [Unstructured](unstructured.zh.md) | ✅ | 需要生产文档 ETL、connector、partition 和 enrichment 时选 Unstructured；需要较窄的 Python parser、自定义 DOM tree 和贝壳式 service adapter 时选 Bella Domify。 | Unstructured 的 ingestion 生态更广；Bella Domify 提供更偏应用的 provider 与 worker 代码，代价是基础设施耦合。 |
| [MarkItDown](markitdown.zh.md) | ✅ | 需要小型转换依赖和可预期 Markdown 输出时选 MarkItDown；PDF 版面、table object、section 和 image handling 值得引入重栈时选 Bella Domify。 | MarkItDown 易安装但版面感知弱；Bella Domify 结构更丰富，运维也重得多。 |
| [Marker](marker.zh.md) | ✅ | 本地模型驱动 PDF 转 Markdown 保真度是核心时选 Marker；多种 Office 格式和明确 DOM-tree API 更重要时选 Bella Domify。 | Marker 聚焦 PDF 转换与 ML 依赖；Bella Domify 结合规则型 PDF 内部结构、Office adapter 和可选远程视觉 OCR。 |
| [olmOCR](olmocr.zh.md) | ✅ | 需要 GPU 处理视觉困难 PDF 时选 olmOCR；不想采用 GPU VLM 部署架构，而需要服务集成的多格式解析时选 Bella Domify。 | olmOCR 的 GPU/模型体积大，但复杂 PDF 定位更清晰；Bella Domify 把复杂度分散到 Python 包、provider 和基础设施。 |

## 技术栈

- **语言与打包：** Python 包 `bella-domify`；Docker 使用 Python 3.9.19，README 要求 Python `>=3.9`，而 `setup.py` 声明 `>=3.6`。
- **PDF 核心：** 基于 PyMuPDF 的大规模 pdf2docx 衍生对象模型，表示 page、block、span、path、image、section、column、row、cell 和 table。
- **其他格式：** adapter 覆盖 DOC/DOCX、XLS/XLSX、CSV、PPTX、文本、Markdown、JSON 类文本、HTML 和常见图片格式。
- **OCR 路径：** 图片通过 `ImageStorageProvider` 上传；可选 OCR 调用 OpenAI-compatible chat-completions 视觉模型，可输出文本、Markdown 表格或 Mermaid 描述。
- **服务模式：** FastAPI/uvicorn endpoint、Kafka consumer worker、S3-compatible 图片/缓存 provider、File API 集成，以及 INI 文件和环境变量配置。

## 依赖

- **Python 运行时：** PyMuPDF、OpenCV、Pillow、Shapely、python-docx、python-pptx、openpyxl、xlrd、FastAPI、uvicorn、Pydantic、SQLAlchemy/SQLModel、boto3、OpenAI、Kafka 和工具包。
- **系统工具：** Dockerfile 安装 build tool、MySQL client header、OpenGL/glib 库，以及用于 Office 转换的 `unoconv`。
- **Library provider：** 调用方必须提供 `ImageStorageProvider`；OCR 还需要视觉模型列表/provider、模型名和用户上下文。
- **服务基础设施：** 自带 Compose stack 使用 LocalStack S3、Zookeeper、Kafka、document-parser container，以及外部 File API/OpenAI-compatible endpoint。
- **网络边界：** born-digital 解析可以本地运行，但启用图片 OCR 和默认 service integration 后会产生出站调用。

## 运维难度

**谨慎配置的 library 为中，自带 service 为高。** 直接 library 使用可以避开 Kafka 和自带 worker，但仍需 provider 实现和较大的依赖集合。附带 service 会启动 Kafka consumer，使用 S3-compatible 存储与结果缓存，依赖外部文件和视觉模型 API，并包含必须替换而不能直接复制的环境特定 INI 值。团队还要解决 Python 版本与许可证声明冲突、锁定全部依赖，并决定哪些功能可以把文档图片发送到部署边界之外。

## 健康度与可持续性

- **维护，2026-07：** 仓库未归档，但最后观察到的默认分支 push 是 2025-11-27，没有 GitHub release 或 tag。
- **治理：** 仓库属于 LianjiaTech 组织，近期 commit 来自多个账号。Contributor 总量部分继承自 pdf2docx 衍生历史，不能干净地表示 Bella Domify 当前 bus factor。
- **年龄与 Lindy：** 2025-08 创建，公开历史不足一年；即使初始开发期有多个贡献者，Lindy 先验仍然偏弱。[推断]
- **采用度：** 86 个 star 说明有早期兴趣，但已读来源里还没有广泛 release 或 dependent-project 信号。
- **风险标记：** GPL v2/GPL v3 冲突会阻断许可证敏感选型。已提交的 Compose 与生产 INI 还包含环境特定 endpoint 和类似凭据的示例值，不能当作生产默认值。

## 存疑（未验证）

- [未验证] 上游法律意图尚未解决：`LICENSE` 是 GPL version 2 正文，`setup.py` 却声明 GPL v3。本页按实际许可证文件记录 `GPL-2.0-only`，但没有解决冲突。
- [未验证] 仓库有限评测集上的准确率图和对比没有被复现或独立审计。
- [未验证] 本次没有端到端运行关闭 OCR 的纯 library 模式，因此尚未证明哪些 Bella-specific 包与网络集成可以移除。
- [推断] 组织所有权和多个近期 commit author 降低了纯单人项目的表象，但公开历史短、contributor 数据又包含继承历史，当前 bus factor 仍不确定。
- [未验证] README、`setup.py` 与 Dockerfile 对有效 Python 下限意见不一致；采用前应在目标 runtime 上验证已发布包。
