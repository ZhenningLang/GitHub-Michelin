---
name: FAISS
slug: faiss
repo: https://github.com/facebookresearch/faiss
category: rag-retrieval
tags: [vector-search, ann, similarity-search, embeddings, ivf, hnsw, pq, gpu, clustering]
language: C++
license: MIT
maturity: v1.14.x, active (2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-25T22:18:04Z
  default_branch: main
  default_branch_sha: a6f97750aeaf760c72d0526c3a346513823c4a0c
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:57:06Z
  overall: A
  overall_score: 3.83
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
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 101.7
        qualifying_issues: 21
        band: default
        window_offset_days: 4
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: faiss-cpu
        dependent_repos_count: 5592
        downloads_last_month: 11749699
        graph_tier: B
        volume_tier: A
        cross_check_divergence: 1.02
        homebrew_installs_90d: 1244
        homebrew_tier: B
        signal_basis: homebrew
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 3514
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 47
        top1_share: 0.238
        top3_share: 0.493
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

# FAISS

Meta FAIR 出品的 C++ 库（带 NumPy 友好的 Python 绑定），用于稠密向量的高效相似度检索与聚类——它是众多向量库底层那个事实标准的进程内 ANN 索引（IVF / HNSW / PQ，CPU + GPU）。

![faiss — 健康度雷达](../../assets/health/faiss.zh.svg)

## 何时使用

你在做 RAG 检索或语义搜索功能，已经有一个 embedding 模型在产出向量；你真正需要的是那个*索引*——给一个 query 向量，就能在毫秒级内从几百万条向量里返回它的最近邻，而不必自己手搓那套数学。你也不想仅仅为了在一个进程内做最近邻查找，就去搭起并运维一个独立的向量数据库服务。你 `pip install faiss-cpu`，先建一个 `IndexFlatL2` 拿到精确基线，等语料变大再升级到 `IndexIVFFlat` 或 `IndexHNSWFlat`（必要时叠加 `IndexIVFPQ` 用乘积量化压内存）。整个索引就活在你的进程内存里，`index.add(xb)` 灌入 embedding，`index.search(xq, k)` 返回 top-k 的 ID 和距离，`faiss.write_index` / `read_index` 让你把它快照成文件。对 ANN 这一步本身来说，它是最快、最久经考验的积木，也是许多上层向量库内部包装的那个引擎。

当你超出 CPU 时也会选它：同一个库有 GPU 路径（`faiss-gpu`，CUDA），能把索引构建和检索搬到设备上跑大批量；它还把 k-means 聚类和 PQ 码本训练当作一等操作——当任务是「把这堆 embedding 聚类」或「压缩这组向量」而不只是「检索 top-k」时很有用。因为它是库而非服务，能干净地嵌进训练管线、离线批处理或单二进制服务里。

## 何时不用

- **你要的是托管的向量*数据库*，而不是一个库。** 这是最锋利的界线：FAISS 是进程内索引，不是服务。它**除了 `write_index`/`read_index` 文件外没有内建持久化，没有 metadata/payload 存储，没有丰富的 metadata 过滤，没有按 id 的 CRUD/upsert 事务模型，没有复制，没有多租户，也没有网络 API**。如果你想要这些，就跑一个向量数据库——Qdrant、Milvus，或像 [FalkorDB](falkordb.zh.md) 这样的图+向量引擎——它们当中很多内部就用着 FAISS 风格的索引，只是额外补上了那些你本来要自己造的运维面。
- **你不想自己扛 sharding 和持久化。** 一个 FAISS 索引受限于单进程的 RAM（或单张 GPU 的显存）。把语料拆到多机、分片、复制、重启后重新加载，全是**你的**代码——没有集群这回事。
- **你需要在查询时做属性/metadata 过滤。** FAISS 检索向量、返回 ID；把「靠近这个向量 且 `tenant=x` 且 `date>...`」组合起来不是它的活。请用带 payload 过滤的存储，或在外部过滤（并承担由此带来的召回率代价）。
- **你需要图 / 多跳遍历。** 它只做扁平的最近邻，不做关系游走。要做实体/关系遍历或 GraphRAG，见 [FalkorDB](falkordb.zh.md)。
- **你想要零调参。** 选索引类型及其参数（`nlist`、`nprobe`、HNSW 的 `M`/`efSearch`、PQ 的 `m`/`nbits`）是一个实打实的召回率-延迟-内存权衡；要拿到好结果，需要一定的 ANN 经验并在你自己的数据上做基准测试。
- **你只有几千条向量。** 小规模下，暴力的 NumPy/`sklearn` 余弦检索（或你现有 Postgres 里的 pgvector）更简单，索引那套机制纯属杀鸡用牛刀。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [FalkorDB](falkordb.zh.md) | ✅ | 需要带向量和全文索引的持久化 GraphRAG 图数据库时，选 FalkorDB。 | 图数据库（Redis 模块），带向量 + 全文索引做 GraphRAG；是一个带遍历能力的持久化多查询*服务*。FAISS 只是进程内的 ANN 索引——没有图、没有服务、没有 metadata 存储。 |
| [PageIndex](pageindex.zh.md) | ✅ | 需要单篇文档的无向量推理树检索时，选 PageIndex。 | 对单篇文档做「无向量」推理树检索，是完全不同的检索原语（LLM 在 ToC 树上导航，无 embedding/ANN）。FAISS 正是 PageIndex 刻意回避的那条 embedding+ANN 路径。 |
| Qdrant | 未收录 | 需要带 payload 过滤和持久化的 Rust 向量数据库时，选 Qdrant。 | Rust 写的向量*数据库*，带 payload 过滤、持久化、gRPC/REST API、分片/复制；开箱即运维，而 FAISS 是你要自己包装并运维的裸库。 |
| [Milvus](milvus.zh.md) | ✅ | 需要带水平扩展、metadata 和控制平面的分布式向量数据库时，选 Milvus。 | 分布式向量数据库（底层常嵌 FAISS/HNSW 引擎），带水平扩展、metadata 和控制平面；跑起来更重，但 sharding/持久化不用你造。 |
| hnswlib | 未收录 | 只需要很小的 HNSW-only C++/Python 库时，选 hnswlib。 | 极小的纯头文件 C++/Python HNSW-only 库；比 FAISS 还轻、易嵌入，但单算法，没有 GPU / PQ / 聚类这些广度。 |
| ScaNN（Google） | 未收录 | Google 的各向异性量化 ANN 库适合你的 CPU workload 时，选 ScaNN。 | Google 的各向异性量化 ANN 库，CPU 上召回/延迟很强；索引菜单和生态比 FAISS 窄，也没有一等的 GPU 构建。 |
| pgvector | 未收录 | 需要在 Postgres 内部用 SQL、事务和 metadata 过滤做向量检索时，选 pgvector。 | 在 Postgres *内部*做向量检索（IVFFlat/HNSW），白送 SQL、事务和 metadata 过滤；如果数据本就在 Postgres 里更简单，但在大规模下比调好的 FAISS 索引更慢、更不灵活。 |

## 技术栈

- **语言：** C++ 内核 + Python/NumPy 绑定（SWIG 生成）；GPU 构建用 CUDA。
- **索引家族：** 精确（`IndexFlat`）、IVF（倒排：`IndexIVFFlat`、`IndexIVFPQ`）、图（HNSW、NSG）、量化（PQ / OPQ / 标量 / additive）、二进制索引，以及通过 `index_factory` 字符串 DSL 组合的复合索引。
- **此外：** k-means 聚类、PQ/码本训练、向量变换（PCA、OPQ），以及 ID 映射包装（`IndexIDMap`）。
- **构建/分发：** 从源码用 CMake；Python 绑定有预编译的 `faiss-cpu` / `faiss-gpu` wheel 和 conda 包。

## 依赖

- **必需：** 一个 BLAS 实现（如 OpenBLAS / MKL）做线性代数 kernel；从源码构建需要 C++17 编译器。
- **可选（GPU）：** NVIDIA CUDA 用于 GPU 构建；也支持 AMD ROCm 和可选的 NVIDIA cuVS 后端。[未验证]
- **Python：** 绑定需要 NumPy；`faiss-cpu` / `faiss-gpu` wheel 自带原生库，多数用户根本不用编译。
- **无服务：** 没有数据存储、消息 broker 或网络依赖——索引就是一个进程内对象，你可以选择把它序列化成文件。

## 运维难度

**作为库很低，但围绕它的系统是你的。** 安装就是一句 `pip install faiss-cpu`（或 `faiss-gpu`），用法是进程内的函数调用——FAISS 自身没什么要部署、没有 daemon、没有集群。真正的成本是向量*数据库*本来会替你扛、而现在归你扛的那一切：持久化/重载索引、在 RAM/显存上限之间分片、数据变化时重建（多数索引类型不能廉价地原地删/改）、按内存做容量规划（PQ 压缩 vs 召回）、以及按 workload 调索引参数。所以这里的「运维」主要是*工程*——你把 FAISS 嵌进一个服务，自己造出持久化、扩展和过滤层，而这恰恰就是托管向量数据库要架在这类索引之上的原因。

## 健康度与可持续性

- **响应速度**：Grade B——中位首次响应时间 64.7 小时，基于 16 个 qualifying issues/PRs。
- **维护（2026-06）：** 最后 push 在 2026-06，当前发布线 v1.14.x——**活跃**且稳定发版；是一个长期、维护良好的库，而非停滞的研究投放。[推断]
- **治理 / 背书：** 由 Meta FAIR 维护（`facebookresearch/faiss`，Organization）。[推断] 机构背书消除了单一维护者的巴士因子风险；它对 Meta 自身的检索栈以及更广的向量数据库生态（许多存储都包装它）足够核心，因而有很强的结构性理由长存。
- **年龄与 Lindy（创建于 2017-02，约 9 年）：** 又老**又**仍活跃——**强 Lindy** 赌注。九年持续使用、并作为众多向量数据库底层那个事实标准的进程内 ANN 索引，几乎是这个领域能给出的最耐久的长寿先验。[推断]
- **采用 / 生态：** 约 40k star（易波动，见存疑）其实低估了它——FAISS 是嵌在多数向量库内部、或被它们当基准对照的那个*引擎*；生态依赖又深又真实。[未验证]
- **风险标记：** MIT（无重新许可风险，无 open-core 门槛）。唯一的“风险”是范围：它是裸库，持久化/分片/过滤都归你——这是工程成本，而非可持续性标记。

## 存疑（未验证）

- [未验证] 截至 2026-06 约 40.4k GitHub star、当前发布线为 v1.14.x——star 数和版本对时间敏感，仅供参考，请对照仓库复核。
- [未验证] 语言字节占比（C++ 居多，其次 Python、再次 CUDA）来自核验时的 GitHub 语言统计，随版本变动。
- [未验证] 支持的索引类型、变换和后端（CUDA / ROCm / cuVS）的确切集合来自核验时的 README/文档；请针对你安装的版本确认具体功能与平台支持。
- [推断]「没有服务级别的持久化/metadata/CRUD/过滤/聚类」是把 FAISS 当库而非向量数据库来刻画；其中部分缺口可用辅助包装部分弥补（如 `IndexIDMap`、手动管理 ID）——动手前请核实你的版本提供了什么，别假设是硬缺失。
- [推断]「众多向量库内部嵌入 FAISS 风格索引」是对生态的总体刻画，不是针对某个产品的断言；请逐个核实下游存储实际用的引擎。
