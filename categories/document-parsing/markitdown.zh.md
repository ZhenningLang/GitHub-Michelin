---
name: MarkItDown
slug: markitdown
repo: https://github.com/microsoft/markitdown
category: document-parsing
tags: [document-conversion, markdown, pdf, office, llm-ingestion, python]
language: Python
license: MIT
maturity: v0.x, active, 162k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-06-24T15:32:46Z
  default_branch: main
  default_branch_sha: e144e0a2be95b34df17433bac904e635f2c5e551
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:18:04Z
  overall: B
  overall_score: 3.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 7
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 66.6
        qualifying_issues: 36
        band: default
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: markitdown
        dependent_repos_count: 0
        downloads_last_month: 14692950
        graph_tier: E
        volume_tier: A
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 678
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 54
        top1_share: 0.445
        top3_share: 0.533
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# MarkItDown

一款轻量级 Python 库，用于将各类文件和办公文档转换为 Markdown，面向 LLM 摄入和文本分析管线设计，而非高保真的人类阅读。

![MarkItDown — 健康度雷达](../../assets/health/markitdown.zh.svg)

## 何时使用

你在构建 RAG 管线、文档问答系统或需要消费 PDF、Word 文档、PowerPoint 幻灯片、Excel 表格、图像、音频文件和 HTML 页面的智能体。你选择 MarkItDown 而不是 [Docling](docling.zh.md)，是因为你想要一个轻量、pip 可装、无 ML 模型依赖的库，通过简单的 `convert()` API 即可使用，而 Docling 为结构化版面分析引入了更重的依赖。你选择它而不是 unstructured.io，是因为你需要一个本地、免费、MIT 许可的方案，无需企业许可层级或云端依赖。你选择它而不是 Marker 或 LlamaParse，是因为你需要跨格式的广度——不仅是 PDF，还包括 Office、音频、图像和 HTML——在一个库中统一处理。你通过 pip 安装，对文件路径调用 `convert()`，即可获得干净的 Markdown，保留标题、列表、表格和链接，让你的 LLM 无需被二进制噪音或专有格式淹没即可处理。

## 何时不用

- **如果你需要面向人类阅读的高保真文档转换**——请用 [Docling](docling.zh.md) 或专用 PDF 转 Word 工具而不是 MarkItDown，因为 MarkItDown 会扁平化复杂布局，输出针对 LLM 消费优化，对人类读者来说可能不够美观。
- **如果你需要文档编辑或往返转换**——请直接用 python-docx、PyMuPDF 或文档操控库而不是 MarkItDown，因为 MarkItDown 是单向转换（文件 → Markdown），无法写回原始格式。
- **如果你需要精确布局、合并单元格和嵌套表格保留**——请用 Docling 而不是 MarkItDown，因为 Docling 以更高保真度建模文档结构与布局，而 MarkItDown 为 Markdown 输出简化表格并扁平化布局。[未验证]
- **如果你在多租户环境中处理不可信输入**——请用沙箱化转换服务或 LLM 解析 API 而不是 MarkItDown，因为 MarkItDown 以当前进程权限执行 I/O，可访问进程能触及的任何资源。[未验证]
- **如果 OCR 是你的主要用途**——请用 Tesseract、PaddleOCR 或专用 OCR 管线而不是 MarkItDown，因为 MarkItDown 的图像 OCR 仅为便利级别，不如专业 OCR 库成熟和可配置。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Docling](docling.zh.md) | ✅ | 富文档解析，将版面 + 表格解析成结构化 Markdown/JSON。 | Docling 模型依赖更重，聚焦结构化输出；MarkItDown 更轻更简单，专为 LLM 摄入构建。 |
| unstructured.io | 未收录 | 企业级文档解析，带分块和嵌入管线。 | 生态更成熟，有云服务；依赖更重，企业功能可能产生许可费用。 |
| LlamaParse | 未收录 | LlamaIndex 出品的解析服务，托管 API。 | 基于云端，需 API key，对复杂 PDF 表现好；MarkItDown 本地、免费且开源。 |
| [Marker](marker.zh.md) | ✅ | 面向学术论文优化的快速 PDF 转 Markdown 工具。 | 专攻 PDF，声称对研究论文精度高；MarkItDown 覆盖更多格式（Office、音频、HTML 等）。 |
| [PyMuPDF](../pdf-tools/pymupdf.zh.md) | ✅ | 用于提取和操控的底层 Python PDF 库。 | 直接 PDF 页面操控库，非高级 Markdown 转换器；更强大但需要更多代码。 |
| textract | 未收录 | 从多种格式提取文本的 Python 库。 | 更老的项目，格式支持更广，但对 LLM 的 Markdown 结构保留关注较少。 |

## 技术栈

- **Python**——主要实现语言
- **模块化转换器架构**——每种格式有独立转换器（PDF、DOCX、PPTX、XLSX、图像、音频、HTML 等）
- **Markdown 输出**——所有转换的统一目标格式

## 依赖

- **Python 3.9+**——运行时环境
- **可选格式专属依赖**——某些转换器需要额外包（如 OCR、音频转录或高级 PDF 解析）
- **无服务或数据库**——纯库；进程内运行

## 运维难度

**低。**`pip install markitdown` 后导入即可。该库无状态、进程内运行；无需部署服务、管理数据库或维护持久基建。主要运维关注点是保持 Python 环境和可选依赖更新，以及安全提示中提到的输入消毒纪律。

## 健康度与可持续性
- **维护活跃度**：Grade B——最近 13 周中 3 周有提交；最后提交距今 37 天。
- **响应速度**：Grade A——中位首次响应时间 37.3 小时，基于 32 个 qualifying issues/PRs。
- **采用广度**：Grade A——pypi.org 上月下载量 10,869,537（包名：markitdown）。
- **长青度**：Grade C——仓库已创建 597 天。
- **治理集中度**：Grade A——前三贡献者占比 53.6%（?）。
- **许可风险**：Grade A——MIT 许可证。
## 存疑（未验证）

- [未验证] README badge 声明由微软 AutoGen 团队出品；具体团队结构和长期维护承诺未公开记录。
- [未验证] 输出质量因格式和文档复杂度差异显著；“Markdown 为 LLM 优化”的免责声明意味着人类可读性被明确列为次要目标。
- [未验证] 关于 I/O 权限和输入消毒的安全提示在多租户或不可信输入环境中应被视为真实运维关切。
- [推断] 一个 8 个月大的项目拥有 162k star，很可能被微软品牌和 2024–2025 LLM 工具炒作周期放大。
- [未验证] 音频转录和图像 OCR 支持可能需要额外外部依赖（如 Whisper、Tesseract），默认不捆绑。
