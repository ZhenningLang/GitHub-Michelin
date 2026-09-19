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
  computed_at: 2026-07-03T08:23:21Z
  overall: A
  overall_score: 3.83
  scored_axes: 6
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
        median_ttfr_hours: 64.7
        qualifying_issues: 16
        band: default
        window_offset_days: 4
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: faiss-cpu
        dependent_repos_count: 5592
        downloads_last_month: 18313484
        graph_tier: B
        volume_tier: A
        cross_check_divergence: 1.13
    longevity:
      grade: A
      raw:
        repo_age_days: 3433
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 43
        top1_share: 0.21
        top3_share: 0.477
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

A C++ library (with NumPy-friendly Python bindings) from Meta FAIR for efficient similarity search and clustering of dense vectors — the de-facto in-process ANN index (IVF / HNSW / PQ, CPU + GPU) under many vector stores.

![faiss — health radar](../../assets/health/faiss.svg)

## When to use

You're building RAG retrieval or a semantic-search feature and you already have an embedding model producing vectors; what you need is the *index* — a structure that, given a query vector, returns its nearest neighbors in milliseconds out of millions of stored vectors, without you hand-rolling the math. You don't want to stand up and operate a separate vector-database service just to do nearest-neighbor lookup inside one process. You `pip install faiss-cpu`, build an `IndexFlatL2` for an exact baseline, then graduate to `IndexIVFFlat` or `IndexHNSWFlat` (optionally with `IndexIVFPQ` product-quantization to shrink memory) when the corpus grows. The whole index lives in your process memory, `index.add(xb)` ingests your embeddings, `index.search(xq, k)` returns top-k IDs and distances, and `faiss.write_index` / `read_index` lets you snapshot it to a file. It is the fastest, most battle-tested building block for the ANN step itself, and it's the engine many higher-level vector stores wrap internally.

You also reach for it when you outgrow CPU: the same library has a GPU path (`faiss-gpu`, CUDA) that moves index build and search onto the device for large batches, and it does k-means clustering and PQ codebook training as first-class operations — useful when the task is "cluster these embeddings" or "compress this vector set", not only "retrieve top-k". Because it's a library, not a server, it embeds cleanly into a training pipeline, an offline batch job, or a single-binary service.

## When NOT to use

- **You need a managed vector *database*, not a library.** This is the sharpest line: FAISS is an in-process index, not a service. It has **no built-in persistence beyond `write_index`/`read_index` files, no metadata/payload storage, no rich metadata filtering, no CRUD/upsert-by-id transactional model, no replication, no multi-tenancy, and no network API**. If you want any of those, run a vector DB — Qdrant, Milvus, or a graph+vector engine like [FalkorDB](falkordb.md) — many of which use FAISS-style indexes internally but add the operational surface you'd otherwise build yourself.
- **You don't want to own sharding and persistence.** A FAISS index is bounded by one process's RAM (or one GPU's memory). Splitting a corpus across machines, sharding, replicating, and reloading on restart is **your** code to write — there is no cluster.
- **You need attribute/metadata filtering at query time.** FAISS searches vectors and returns IDs; combining "near this vector AND `tenant=x` AND `date>...`" is not its job. Use a store with payload filtering, or filter externally (with the recall caveats that brings).
- **You need graph / multi-hop traversal.** It does flat nearest-neighbor, not relationship walks. For entity/relationship traversal or GraphRAG, see [FalkorDB](falkordb.md).
- **You want zero tuning.** Picking an index type and its parameters (`nlist`, `nprobe`, HNSW `M`/`efSearch`, PQ `m`/`nbits`) is a real recall-vs-latency-vs-memory tradeoff; getting good results assumes some ANN expertise and benchmarking on your own data.
- **You only have a few thousand vectors.** At small scale a brute-force NumPy/`sklearn` cosine search (or pgvector in your existing Postgres) is simpler and the index machinery is overkill.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [FalkorDB](falkordb.md) | ✅ | Choose FalkorDB when you need a persistent graph database with vector and full-text indexing for GraphRAG. | Graph database (Redis module) with vector + full-text indexing for GraphRAG; a persistent multi-query *service* with traversal. FAISS is just the in-process ANN index — no graph, no server, no metadata store. |
| [PageIndex](pageindex.md) | ✅ | Choose PageIndex when you need vectorless reasoning-tree retrieval over one document. | "Vectorless" reasoning-tree retrieval over one document; a different retrieval primitive entirely (LLM navigates a ToC tree, no embeddings/ANN). FAISS is the embedding+ANN path PageIndex deliberately avoids. |
| Qdrant | 未收录 | Choose Qdrant when you need a Rust vector database with payload filtering and persistence. | Rust vector *database* with payload filtering, persistence, gRPC/REST API, sharding/replication; turnkey ops where FAISS is a bare library you wrap and operate yourself. |
| [Milvus](milvus.md) | ✅ | Choose Milvus when you need a distributed vector database with horizontal scale and metadata/control-plane features. | Distributed vector database (often embedding FAISS/HNSW engines under the hood) with horizontal scale, metadata, and a control plane; heavier to run, but you don't build sharding/persistence. |
| hnswlib | 未收录 | Choose hnswlib when a tiny HNSW-only C++/Python library is enough. | Tiny header-only C++/Python HNSW-only library; even lighter than FAISS and easy to embed, but single-algorithm and no GPU / PQ / clustering breadth. |
| ScaNN (Google) | 未收录 | Choose ScaNN when Google's anisotropic-quantization ANN library fits your CPU workload. | Google's anisotropic-quantization ANN library, very strong recall/latency on CPU; narrower index menu and ecosystem than FAISS, no first-class GPU build. |
| pgvector | 未收录 | Choose pgvector when you need vector search inside Postgres with SQL, transactions, and metadata filtering. | Vector search *inside Postgres* (IVFFlat/HNSW) with SQL, transactions, and metadata filtering for free; simpler if your data already lives in Postgres, slower/less flexible than a tuned FAISS index at large scale. |

## Tech stack

- **Language:** C++ core with Python/NumPy bindings (SWIG-generated); CUDA for the GPU build.
- **Index families:** exact (`IndexFlat`), IVF (inverted file: `IndexIVFFlat`, `IndexIVFPQ`), graph (HNSW, NSG), quantization (PQ / OPQ / scalar / additive), binary indexes, plus composite indexes via the `index_factory` string DSL.
- **Also:** k-means clustering, PQ/codebook training, vector transforms (PCA, OPQ), and ID-mapping wrappers (`IndexIDMap`).
- **Build/distribution:** CMake from source; prebuilt `faiss-cpu` / `faiss-gpu` wheels and conda packages for the Python bindings.

## Dependencies

- **Required:** a BLAS implementation (e.g. OpenBLAS / MKL) for the linear-algebra kernels; a C++17 compiler to build from source.
- **Optional (GPU):** NVIDIA CUDA for the GPU build; AMD ROCm and an optional NVIDIA cuVS backend are also supported. [未验证]
- **Python:** the bindings need NumPy; the `faiss-cpu` / `faiss-gpu` wheels bundle the native library so most users never compile.
- **No services:** there is no datastore, broker, or network dependency — the index is an in-process object you optionally serialize to a file.

## Ops difficulty

**Low as a library, but the system around it is yours.** Installing is a single `pip install faiss-cpu` (or `faiss-gpu`), and using it is in-process function calls — nothing to deploy, no daemon, no cluster for FAISS itself. The real cost is everything a vector *database* would otherwise hand you and that you now own: persisting/reloading indexes, sharding across RAM/GPU-memory limits, rebuilding on data changes (most index types don't cheaply delete/update in place), capacity-planning memory (PQ compression vs recall), and tuning index parameters per workload. So "ops" here is mostly *engineering* — you embed FAISS in a service and build the durability, scaling, and filtering layer yourself, which is exactly why managed vector DBs exist on top of indexes like this one.

## Health & viability

- **Responsiveness**: Grade B — median first-response time 64.7 hours across 16 qualifying issues/PRs.
- **Maintenance (2026-06):** last push 2026-06, current release line v1.14.x — **active** and steadily released; a long-running, well-maintained library, not a stalled research drop. [推断]
- **Governance / backing:** Meta FAIR-maintained (`facebookresearch/faiss`, Organization). [推断] Institutional backing removes single-maintainer bus-factor risk; it is core enough to Meta's own retrieval stack and the broader vector-DB ecosystem (many stores wrap it) that it has strong structural reasons to persist.
- **Age & Lindy (created 2017-02, ~9yr):** old **and** still active — a **strong Lindy** bet. Nine years of continuous use and being the de-facto in-process ANN index under many vector databases is about as durable a longevity prior as this space offers. [推断]
- **Adoption / ecosystem:** ~40k stars (volatile, see Caveats) understates it — FAISS is the *engine* embedded inside or benchmarked against by most vector stores; ecosystem dependence is deep and real. [未验证]
- **Risk flags:** MIT (no relicense risk, no open-core gating). The only "risk" is scope: it is a bare library, so you own persistence/sharding/filtering — an engineering cost, not a viability flag.

## Caveats (unverified)

- [未验证] ~40.4k GitHub stars and v1.14.x as the current release line as of 2026-06 — star counts and version are date-sensitive; treat as indicative and re-check the repo.
- [未验证] Language byte split (C++ majority, then Python, then CUDA) is from the GitHub language breakdown at verification time and shifts release-to-release.
- [未验证] The exact set of supported index types, transforms, and backends (CUDA / ROCm / cuVS) is from the README/docs at verification time; confirm the specific feature and platform support for your installed version.
- [推断] "No persistence/metadata/CRUD/filtering/clustering of the service kind" is characterizing FAISS as a library vs a vector DB; some of these gaps are partially addressable with helper wrappers (e.g. `IndexIDMap`, manual ID management) — verify what your version offers before assuming a hard absence.
- [推断] "Many vector stores embed FAISS-style indexes internally" is a general characterization of the ecosystem, not a per-product claim; check each downstream store for its actual engine.
