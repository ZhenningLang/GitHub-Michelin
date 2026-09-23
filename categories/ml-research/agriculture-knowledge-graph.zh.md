---
name: Agriculture Knowledge Graph (AgriKG)
slug: agriculture-knowledge-graph
repo: https://github.com/qq547276542/Agriculture_KnowledgeGraph
category: ml-research
tags: [knowledge-graph, nlp, named-entity-recognition, relation-extraction, neo4j, django, chinese-nlp]
language: Python
license: GPL-3.0
maturity: research project, maintenance stopped (per README), ~4.4k stars (as of 2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2025-02-11T14:23:01Z
  default_branch: master
  default_branch_sha: ccda905b03cacc659ad3a3a65fbc08019bf08ea2
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:40:04Z
  overall: D
  overall_score: 1.0
  scored_axes: 3
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: D
      raw:
        archived: false
        last_commit_age_days: 588
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: D
      raw:
        repo_age_days: 3223
        last_commit_age_days: 588
        cohort: app
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: D
      raw:
        spdx_id: GPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    adoption: { reason: no_package_structural }
    governance: { reason: unattributable }
---

# Agriculture Knowledge Graph (AgriKG)

一个中文研究项目（华师大），端到端构建农业知识图谱——爬虫、实体识别、关系抽取、Neo4j 存储，外加一个带检索与问答的 Django demo——作为参考发布，且作者已明确不再维护。

![agriculture-knowledge-graph — 健康度雷达](../../assets/health/agriculture-knowledge-graph.zh.svg)

## 何时使用

你是个在做中文领域知识图谱的学生或研究者——比如农业，但这套流水线可以泛化——想要一份*跑通的整链示例*：用 Scrapy 爬百科、用 KNN 分类器给约 15 万实体打标、对着 Wikidata 抽关系、把三元组灌进 Neo4j，再用 Django 前端做实体检索、命名实体识别和图上的简单问答。你 clone AgriKG，读它的目录图，复用你需要的部分——已爬好的 `hudong_pedia.csv`、手工标注的 `labels.txt`、预测的实体标签、天气/植物关系 CSV——既当现成数据，也当你自己 KG 流水线的模板。

你把它当作一份中文 KG 系统的**完整、可读蓝图**（以及它自带的数据集），接受它是课程级研究代码、需要你改造，而非拿来即用的产品。

## 何时不用

- **你需要维护中的软件。** README 明白写着项目已停止维护（「由于工作原因，该项目已停止维护」）；把它当冻结的参考，别指望修复，并预留时间复活一套老的 Django/py2neo 栈。[推断]
- **你想要生产级 KG 平台。** 这是研究 demo，不是加固服务——没有鉴权、扩展或运维方案。生产环境请直接用图数据库（Neo4j）配自己的入库，或用托管 KG 框架。
- **你的领域或语言差异很大。** 数据和标注是农业专属且中文；*方法*能迁移，但自带语料不行。别指望在中文农业文本之外有开箱即用的价值。
- **GPL-3.0 与你的分发冲突。** 强 copyleft——把这段代码嵌进闭源产品会带来义务；请提取技术/数据（README 提供数据用于非商业学术用途）而非把 GPL 代码 vendoring 进来。
- **你需要当下的 NER/RE 精度。** 模型（KNN 标签、较老的 RE）是 2017 到 2019 年的东西；现代中文 NLP（transformer NER、LLM 抽取）会大幅胜过它们。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| Neo4j（直接用） | 未收录 | 只需要图数据库层、并准备自建入库流水线时，选 Neo4j。 | 本项目灌入的图数据库；生产级存储加 Cypher，但整条 NLP 入库流水线得你自己搭——AgriKG 恰恰就是把那条流水线做成了示例。 |
| DeepKE | 未收录 | 需要维护中的 transformer 中文知识抽取工具箱时，选 DeepKE。 | 维护中的中文知识抽取工具箱（NER/RE/属性），基于 transformer；是真正可用来搭建的库，而非 AgriKG 那样冻结的端到端 demo。 |
| OpenKG / CN-DBpedia | 未收录 | 需要中文开放知识图谱数据/资源时，选 OpenKG 或 CN-DBpedia。 | 中文开放知识图谱数据/资源；是数据源，而非可运行的流水线加界面。 |
| [TaskMatrix](taskmatrix.zh.md) | ✅ | 需要同一货架上的多模态工具编排研究产物时，选 TaskMatrix。 | 任务无关（多模态 agent / 工具编排），但同一货架——主要作为参考产物发布的研究仓库，而非维护中的产品。 |

## 技术栈

- **语言：** Python；全程中文文本 NLP。
- **爬取：** Scrapy 爬虫（`MyCrawler`、`dfs_tree_crawler`、`wikidataSpider`）抓百科实体和 Wikidata 关系。
- **NLP：** THULAC 分词、用于实体类型预测的 KNN 分类器、fastText（`pyfasttext`）、关系抽取模块。
- **存储：** 经 `py2neo==4.1.0` 用 Neo4j；MongoDB（`pymongo`）存爬取数据；自带 CSV 作为中间数据。
- **前端：** 一个 Django 应用（`demo/`），含检索、NER、问答的视图。

## 依赖

- **运行时服务：** 必须跑起 Neo4j（图存储）和 MongoDB（爬取存储）；Django 应用与两者通信。
- **Python 库（钉死、偏老）：** `Django>=1.11.7`、`py2neo==4.1.0`、`thulac`、`pyfasttext==0.4.5`、`Cython>=0.28.5`、`pinyin`、`pymongo`——其中数个年代久远，在现代 Python 上不钉老解释器可能装不干净。[推断]
- **数据：** 自带不小的 CSV（`hudong_pedia.csv`、`labels.txt`、预测标签、天气/植物关系），免得你为探索图谱而重爬。
- **模型：** 流水线引用的已训练分类器/RE 产物（部分可能需要重生成）。

## 运维难度

**就其形态而言偏高。** 它不是单一二进制或 pip install——要跑完整 demo，你必须起 Neo4j *和* MongoDB、灌入自带数据，并让一套老的 Django 加 py2neo 4.x 加 pyfasttext 跑在兼容的（老）Python 上。尤其 `pyfasttext` 和 `py2neo==4.1.0` 正是那种会跟现代环境对着干的、带 C 扩展/钉死版本的旧依赖。因为无人维护，任何崩坏都得你自己排查，没有上游支援。只跑*数据*（CSV）或某个子流水线，远比复活整条端到端应用便宜。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** README 明确宣布维护已停止。最后 push 于 2025-02（多半是杂务而非功能开发）；无 release/tag。**按作者自述已废弃**——仅供参考。[推断]
- **治理 / bus factor。** 一个大学（华师大）课程/研究项目，主要由一名学生作者（qq547276542）加几位贡献者；bus factor 约 1。约 4.4k star 是**废弃仓库上的学术人气**——是引用/学习信号，不是维护信号；照此标注。[推断]
- **年龄与 Lindy 判断。** 2017-11 创建（约 8 年）但**已声明不维护**⇒ 此处年龄*不赋予* Lindy；它作为被引用的产物存续，而非活的软件。[推断]
- **采用度。** 约 4.4k star / 约 1.6k fork，并有一篇 DASFAA 2019 论文——作为中文 KG 蓝图和数据源被广泛引用与 fork。[未验证]
- **风险标记。** 代码复用上的 **GPL-3.0**（copyleft）；**偏老/偏重的依赖栈**（Neo4j+MongoDB+老 py2neo/pyfasttext）；以及**无上游支持**。按 README，数据可用于非商业学术用途。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 4.4k star / 约 1.6k fork；数字对时间敏感，仅供参考。
- [未验证] 自带已训练模型的确切状态/可重生成性未确认；部分产物可能需要重训才能复现 demo。
- [推断]「依赖在现代 Python 上装不干净」是从钉死的旧版本（`py2neo==4.1.0`、`pyfasttext==0.4.5`、`Django>=1.11.7`）推断，并非来自实测安装。
- [推断]「2025-02 的最后 push 是杂务而非功能」是从 README 明确的不维护声明加与功能活动的间隔推断，并非逐 commit 检查所得。
