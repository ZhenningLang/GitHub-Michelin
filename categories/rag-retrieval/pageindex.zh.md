---
name: PageIndex
slug: pageindex
repo: https://github.com/VectifyAI/PageIndex
category: rag-retrieval
tags: [rag, vectorless, reasoning-retrieval, document-index, tree-index, pdf]
language: Python
license: MIT
maturity: no tagged release, active (2026-06)
last_verified: 2026-06-26
type: library
upstream:
  pushed_at: 2026-06-29T06:58:57Z
  default_branch: main
  default_branch_sha: 293730afbd4319a683fe4aee439360a2b21b8c3c
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:23:04Z
  overall: B
  overall_score: 3.0
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 9
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 51.7
        qualifying_issues: 16
        band: default
        window_offset_days: 12
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 458
        last_commit_age_days: 0
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 9
        top1_share: 0.774
        top3_share: 0.962
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    adoption: { reason: ambiguous }
---

# PageIndex

一个“无向量”（vectorless）的 RAG 文档索引：它为一篇长文档构建一棵类似目录（table of contents）的树，然后让 LLM 沿着树往下推理、定位相关章节，而不是走“切块 + 嵌入 + 向量相似度检索”那条路。

![pageindex — 健康度雷达](../../assets/health/pageindex.zh.svg)

## 何时使用

你在为一小批长而有结构的文档——财报、监管 PDF、技术手册、研究论文——构建问答或 agent，而你已经亲眼看到向量 RAG 在一个具体地方翻车：它召回的 chunk 和问题“语义上接近”，但其实并不“相关”；同时领域专家不敢信任那些和出处脱节的答案。你希望检索像人类分析师那样翻到正确的章节，并且每条答案都标注具体的页/节，从而可审计。PageIndex 用这个思路解决问题：把文档解析成层级树（章、节、节点摘要），在查询时让 LLM 去*导航*这棵树——读摘要、推理该往哪个分支下钻——而不是比对嵌入向量。无需搭建向量库，无需调 chunk 大小，也无需托管嵌入模型；索引就是文档自身的结构。

当“相似 ≠ 相关”正是你的真实痛点、且语料规模有限到能负担每次查询的 LLM 树遍历时，它非常合适。项目自报在 FinanceBench 文档问答基准上达到 98.7% 准确率 [未验证]，并能自然嵌入 agent 流程（仓库附带接入 OpenAI Agents SDK 的示例），于是你可以把一篇长 PDF 交给一个能就其结构推理的 agent，返回带页码锚点、可溯源的引用。

## 何时不用

- **面向数百万短文档的大规模 / web 级检索。** 每次查询都做 LLM 树遍历，每次查找都要花 token 和延迟；对一个巨大扁平集合做广度优先检索时，嵌入 + ANN 向量库（Qdrant / pgvector，未收录）便宜得多也快得多。OSS 仓库面向单文档树；“百万文档规模”是托管版 **PageIndex File System** 的能力，不是开源库的。[推断]
- **你要一套自带闭环、零 LLM 账单的系统。** 建索引*和*检索都调用 LLM（默认 OpenAI，其它经 LiteLLM）。每次建库、每次查询都在花 API token；没有纯本地嵌入的模式。
- **短文档、无结构或扁平文档。** 全部价值都在那棵目录树上。一篇没有有意义章节层级的文档（聊天记录、扁平 CSV、一页备忘）给推理器无可导航之物；普通切块就够了。
- **你想要生产级的“Cloud / MCP / API”管线，而非这个仓库。** Vectify 主推托管版 PageIndex 平台（Chat、MCP、托管 API、VPC/本地部署）。OSS 仓库是索引内核，不是那套服务——别把仓库当成托管产品。[未验证]
- **你需要图数据库或跨语料的多跳实体遍历。** PageIndex 索引的是单篇文档的结构，不是知识图谱。要做跨语料的实体/关系遍历，见 [FalkorDB](falkordb.zh.md) 或下面的图构建工具。
- **成熟度 / 稳定性风险。** 没有打 tag 的 release，MIT 但年轻；API 和 CLI 参数可能随版本变动。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [FalkorDB](falkordb.zh.md) | ✅ | 需要 GraphRAG 的持久化属性图，而不是单文档推理树时，选 FalkorDB。 | 面向 GraphRAG 的属性图数据库（向量 + 多跳遍历）；PageIndex 是单文档推理树，不是图存储——检索原语不同。 |
| [graphify](graphify.zh.md) | ✅ | 目标是代码/文档知识图谱，而不是单篇文档的目录树时，选 graphify。 | 从代码/文档构建知识图谱；PageIndex 为单篇文档构建层级目录树并在其上推理——没有实体图。 |
| [code-review-graph](code-review-graph.zh.md) | ✅ | 目标是专门的 code-review 图时，选 code-review-graph。 | 专做 code-review 的图工具；与文档树检索正交。 |
| [LlamaIndex](../agent-frameworks/workflow-builders/llamaindex.zh.md) | ✅ | 需要包含多种索引类型的通用 RAG 框架，而不是单一无向量推理索引时，选 LlamaIndex。 | 通用 RAG 框架，含多种索引（包括树/摘要索引）；覆盖广得多且以嵌入为中心，而 PageIndex 是聚焦的无向量推理索引。 |
| RAPTOR | 未收录 | 需要递归聚类 + 摘要树，并在查询时仍走嵌入检索时，选 RAPTOR。 | 递归聚类 + 摘要构建检索树，但查询时仍靠嵌入检索；PageIndex 改为用 LLM 推理导航这棵树，而非向量搜索。 |
| pgvector / Qdrant | 未收录 | 经典嵌入 + ANN 向量检索已经足够、且更重视规模成本时，选向量库。 | 经典的嵌入 + ANN 向量检索；在规模与广度上更便宜，但正是 PageIndex 要规避的“相似 ≠ 相关”失败模式。 |

## 技术栈

- **语言：** Python。
- **建索引：** 把 PDF / Markdown 解析成层级树（章、节、节点摘要），形如一份目录。
- **检索：** 在树上做 LLM 推理（导航并下钻），而非向量相似度——无嵌入模型、无 ANN 索引。
- **LLM 接入：** 默认 OpenAI（`OPENAI_API_KEY`）；经 LiteLLM 支持多家（README 声称的多家路由）。
- **入口：** `python3 run_pageindex.py --pdf_path <doc>`，可配模型、页/token 上限、节点 ID/摘要等选项。
- **较新的相邻示例：** 经 OpenAI Agents SDK 的 agent 化无向量 RAG；基于页面图像的视觉 RAG。

## 依赖

- **运行时：** Python 3；摄入阶段需要 PDF 解析。
- **必需：** 一个 LLM API key——开箱即用是 `OPENAI_API_KEY`；其它提供方经 LiteLLM 路由。
- **无基础设施：** 没有向量数据库、没有嵌入服务、没有需要运维的独立数据存储——索引就是描述这棵树的文件/JSON。
- **成本依赖：** 建索引和查询都内在地消耗 LLM token（不是可以拿掉的可选基础设施）。

## 运维难度

**低。** 几乎没有基础设施要跑：克隆仓库、设好 API key、把脚本指向一个 PDF，就得到一棵可查询的树——没有向量库要供给、调优或备份。真正的运维关注点不是服务器，而是 **LLM 成本与延迟**：每次查询都用模型调用在树上推理，所以每次查询的 token 花费和响应时间才是你的扩展上限，你要预算并观测 API 用量，而非内存或磁盘。可复现性与质量还系于所选模型，这是个会变动的依赖。至于托管/MCP/VPC 管线，运维转移到托管产品上，超出 OSS 仓库范围。

## 健康度与可持续性

- **响应速度**：Grade B——中位首次响应时间 51.7 小时，基于 16 个 qualifying issues/PRs。
- **维护——活跃。** 默认分支最后一次 push 在 2026-06，未归档，但**完全没有打 tag 的 release**——“版本”即 `main` 当前内容，为可复现请 pin 到某个 commit。没有 semver 的活跃开发，意味着你跟的是一个移动靶。`[未验证]`
- **治理 / 背书——单一厂商（Vectify AI）。** 仓库为 **Organization** 所有（`VectifyAI/PageIndex`），约 33k star[未验证]。路线图由厂商驱动，且开源仓库是更大商业产品（托管版 PageIndex Cloud/MCP/API/VPC）的*索引内核*——于是 OSS 表面是产品的引流位，带着典型的 open-core 风险：最好的能力落在托管层。`[推断]`
- **年龄与 Lindy——年轻，约 1 年（创建于 2025-04）。** 够久到能跑出真实基准（98.7% FinanceBench，自报[未验证]），但还不够久到成为 Lindy 意义上的安全选择；API/CLI 参数可能随版本变动。当作有潜力的年轻库，而非已定型的标准。
- **采用 / 生态——小众但真实。** 能嵌入 agent 栈（OpenAI Agents SDK 示例），经 LiteLLM 支持多家提供方；“无向量 RAG”的提法有可见的心智占有。MIT 许可证，未观察到 relicense——但在假定某能力在仓库里之前，先核实开源与托管的边界。

## 存疑（未验证）

- [未验证] 截至 2026-06，star 约 33.4k——GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 98.7% FinanceBench 准确率与“显著优于向量 RAG”是项目自报数字；基准结果依赖具体设置，本页未独立复现。
- [未验证] LiteLLM 多提供方路由、OpenAI Agents SDK 示例与视觉 RAG 均来自验证时的项目材料；依赖前请对照当前仓库核实。
- [推断] 面向百万文档规模的 "PageIndex File System" 以及 Cloud/MCP/API/VPC 等似乎是与 OSS 仓库不同的托管产品能力；开源库面向单文档树——假定某能力在仓库里之前，先核实开源/托管的边界。
- [未验证] 验证时 GitHub 无打 tag 的 release（latestRelease 为 null）；“版本”即默认分支当前内容，为可复现请 pin 到某个 commit。
- [未验证] 除 PDF/Markdown 外的确切必需 Python 依赖与支持的输入格式来自验证时的 README，可能变动。
