---
name: FalkorDB
slug: falkordb
repo: https://github.com/FalkorDB/FalkorDB
category: rag-retrieval
tags: [graph-database, graphrag, knowledge-graph, opencypher, graphblas, vector-index]
language: C
license: SSPL-1.0
maturity: v4.18.11, active (2026-06)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T00:50:41Z
  default_branch: master
  default_branch_sha: 835d06e617e24f8828c9bd5fd0450b21f496efb2
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:57:09Z
  overall: D
  overall_score: 2.83
  scored_axes: 6
  applicable_axes: 6
  capped: true
  cap_reason: "source-available/no-license: NOASSERTION"
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.8
        qualifying_issues: 33
        band: relaxed_solo
        window_offset_days: 12
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 70360
        release_assets: 616
        release_tier: D
        signal_basis: releases
    longevity:
      grade: A
      raw:
        repo_age_days: 1160
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 15
        top1_share: 0.264
        top3_share: 0.62
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: E
      raw:
        spdx_id: NOASSERTION
        permissiveness: source_available
        relicense_36mo: false
        content_license: null
---

# FalkorDB

一个以稀疏矩阵（GraphBLAS）为底层的属性图数据库，作为 Redis 模块运行，讲 OpenCypher，并叠加向量 + 全文索引，为 LLM 应用的 GraphRAG 检索兜底。

![falkordb — 健康度雷达](../../assets/health/falkordb.zh.svg)

## 何时使用

你正在搭一条 GraphRAG 管线：你已经从语料里抽出实体和关系、落进知识图谱，查询时你想把向量相似（“找出和这个问题相近的 chunk”）和多跳图遍历（“再从这些实体走到相关事实，并把路径引用出来”）结合起来。纯向量库做不了遍历，而一个通用图数据库又意味着在你已有的缓存旁边再立一个更重的独立服务。FalkorDB 用“住在 Redis 里、作为模块运行”来解决这个问题：你把它加载进来，用 OpenCypher 建图、`CREATE VECTOR INDEX` / 建全文索引，然后在同一个低延迟引擎里跑混合检索（向量 + 遍历 + 范围过滤）。它的 GraphBLAS 稀疏矩阵内核让线性代数式的遍历很快，而且你可以在一台服务器上保留许多命名图（`GRAPH.QUERY mygraph ...`）做按租户或按文档的隔离。

如果你来自 RedisGraph、在 Redis 停掉那个模块之后需要一个去处，你也很合适——FalkorDB 接过了“OpenCypher-on-Redis”这套模型，提供了文档化的迁移路径，还附带一个官方 Python GraphRAG-SDK（一个独立的 Apache-2.0 仓库），在其上把 LLM 驱动的建图与检索接通，这样你不必手搓整条摄取循环。

## 何时不用

- **你需要一个无 copyleft / 宽松许可的内核。** FalkorDB 的服务端是 **SSPL-1.0**——非 OSI 认可，其“以服务形式提供该软件”条款对围绕它做托管服务很不友好。如果你所在组织禁用 SSPL/AGPL 一类许可，这就是硬性阻断。（GraphRAG-SDK 客户端是 Apache-2.0，但数据库本身是 SSPL。）
- **你想要跨多机水平分片的图。** 它作为 Redis 模块运行；扩展是 Redis 式的（复制、单节点多图），而非自动图分片。非常大的单个图受限于单节点的内存。[推断]
- **你的数据装不进内存。** 和 Redis 一样，工作集常驻内存、以 RDB/AOF 持久化；它不是面向 PB 级存储、磁盘优先的 OLAP 图引擎。[推断]
- **你只需要向量检索。** 如果没有图/遍历价值——只是对 embedding 做最近邻——一个专用向量库（或 pgvector）更简单，也省得养一个用不充分的图引擎。
- **你想要事实标准的图生态。** Neo4j 的工具链、Bolt 驱动、GDS 算法和招聘人才池都大得多；FalkorDB 更年轻、兼容 OpenCypher，但并非 Neo4j 专有特性的即插即用替代。
- **你无法容忍 Redis 模块的运维耦合。** 你会继承 Redis 7.4 版本要求、模块加载，以及从源码编译时需要 `--recurse-submodules` 的约束。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [graphify](graphify.zh.md) | ✅ | 需要轻量代码/文档建图，而不是图数据库本身时，选 graphify。 | 轻量的代码/文档转图构建器；FalkorDB 是存储+查询引擎，graphify 在其上游做建图——互补，而非替代。 |
| [code-review-graph](code-review-graph.zh.md) | ✅ | 需要专门的 PR/code-review 图工具时，选 code-review-graph。 | 领域专用（代码评审）图工具；FalkorDB 是你会拿来构建这类工具的通用图数据库。 |
| [PageIndex](pageindex.zh.md) | ✅ | 检索原语是推理文档树，而不是属性图数据库时，选 PageIndex。 | 基于推理的文档树 / 检索索引，不是图数据库——检索原语不同（层级索引 vs 属性图）。 |
| Neo4j | 未收录 | 最大属性图生态比 Redis 嵌入或稀疏矩阵速度更重要时，选 Neo4j。 | 业界标准的属性图，生态最大（Bolt、GDS、APOC）；更重，GPLv3/商业许可。FalkorDB 在稀疏矩阵遍历上更快、可嵌入 Redis，但更年轻且为 SSPL。 |
| Memgraph | 未收录 | 想要内存型 Cypher 图数据库，但不想继承 Redis 模块模型时，选 Memgraph。 | 内存型、兼容 Cypher、偏流式的图数据库；BSL 许可。和 FalkorDB 的内存型定位有重叠，但没有 Redis 模块这套模型。 |
| Neptune（AWS） | 未收录 | 想要 AWS 托管图服务，且接受云锁定胜过自托管时，选 Neptune。 | 托管的多模型（Gremlin/openCypher/SPARQL）图服务；不可自托管，绑定 AWS。FalkorDB 可自托管、贴近开源。 |

## 技术栈

- **语言：** C（内核，约占仓库 70%），含 C++ 与一个 Rust 组件；测试用 Python + Gherkin/Cucumber。
- **图引擎：** [GraphBLAS](https://github.com/DrTimothyAldenDavis/GraphBLAS) 稀疏邻接矩阵表示；查询执行表达为线性代数。
- **宿主：** Redis 模块（通过 `loadmodule` / `MODULE LOAD` 加载）；最新版本需要 Redis 7.4。
- **查询语言：** OpenCypher 加专有扩展；索引：向量（相似）、全文、范围。
- **构建：** CMake + Make，`deps/` 下 vendored 子模块。
- **客户端（官方）：** Java、Python、Node.js、Rust、Go、C#；社区 SDK（Ruby、PHP、Elixir 等）。
- **上层：** GraphRAG-SDK（独立的 Apache-2.0 Python 仓库），做 LLM 驱动的建图/检索。

## 依赖

- **运行时：** Redis 7.4（宿主进程）；加载进去的 FalkorDB 模块二进制。
- **从源码：** `git clone --recurse-submodules`、C/C++ 工具链（gcc/clang）、CMake、Make；GraphBLAS 等依赖以子模块 vendored。
- **最省事路径：** 官方 Docker 镜像（`docker run -p 6379:6379 -p 3000:3000 falkordb/falkordb`），打包引擎 + 浏览器 UI（3000 端口）。
- **用于 GraphRAG：** Python GraphRAG-SDK 加一个 LLM 提供方，做实体/关系抽取。

## 运维难度

**低到中。** Docker 让单节点变得很简单——一个容器就给你引擎、持久化和一个 Web UI。日常运维基本就是 Redis 运维：RDB/AOF 持久化、`maxmemory` 调参、复制。难度升到**中**的场景：（a）为自定义平台从源码编译（子模块 + GraphBLAS 构建），（b）需要 HA/复制拓扑，或（c）把大图压向单节点内存上限——因为没有内置的水平图分片。内存容量规划是主要的容量考量。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 10.4 小时，基于 13 个 qualifying issues/PRs。
- **维护（2026-06）：** 最后 push 在 2026-06，当前 release v4.18.11——**活跃**，版本号成熟、点版本发布频繁。[推断] 约 705 个 open issue 读起来是一个繁忙项目上的参与度，而非疏于维护。
- **治理 / 背书：** 由 FalkorDB 公司以组织形式所有（`FalkorDB/FalkorDB`）——一个单一厂商的商业开源项目，而非基金会。[推断] 路线图与许可由厂商控制；巴士因子是机构级而非单一维护者，但厂商的商业模式（托管产品）会塑造方向。
- **年龄与 Lindy（创建于 2023-07，约 3 年）：** 偏年轻但持续活跃，并以 **RedisGraph 继任者**（OpenCypher-on-Redis 血缘）身份继承了可信度。[推断] 已越过年轻即废弃的失败模式；但还不是长期被验证的 Lindy 赌注——可称为已确立但不算老的引擎。
- **采用 / 生态：** 约 4k star（易波动，见存疑）；官方多语言客户端与 GraphRAG-SDK 有助采用，但它要对抗 Neo4j 大得多的生态与招聘人才池。[未验证]
- **风险标记：** **SSPL-1.0——承重标记。** 非 OSI 认可；“以服务形式提供”条款对在其上构建托管服务很不友好，禁用 SSPL/AGPL 一类许可的组织必须止步于此。这是一种刻意的单一厂商许可姿态，而非意外的重新许可。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 star 约 4.66k（GitHub star 不可靠且对时间敏感，仅供参考）。
- [推断] FalkorDB 被广泛描述为 RedisGraph 在 Redis 停掉该模块后的 fork/继任者；存在一份“RedisGraph 迁移到 FalkorDB”的指南，但仓库内 README 并未明确陈述 fork 血缘——断言前请对照项目自身历史核实。
- [推断] 单节点内存上限与缺少自动图分片，是从 Redis 模块架构推断的，并非引自某条明示限制；按你的规模请对照当前文档核实。
- [推断] 内存工作集 + RDB/AOF 持久化，是从 Redis 模块模型推断的；README 并未拼出存储架构。
- [未验证] 具体的语言字节占比（C 约 70%，加 C++/Rust/Python）来自核验时的 GitHub 语言分布，会随版本变动。
- [未验证] 官方客户端 SDK 集合与索引特性（向量 / 全文 / 范围）来自核验时的项目文档；请按你的版本核对当前文档。
