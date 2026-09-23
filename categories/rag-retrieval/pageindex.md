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
  computed_at: 2026-09-22T16:57:54Z
  overall: B
  overall_score: 2.5
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
      grade: C
      raw:
        median_ttfr_hours: 558.2
        qualifying_issues: 7
        band: default
        window_offset_days: 12
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 451
        release_assets: 68
        release_tier: D
        signal_basis: releases
    longevity:
      grade: C
      raw:
        repo_age_days: 539
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 13
        top1_share: 0.685
        top3_share: 0.894
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

# PageIndex

A "vectorless" RAG document index: it builds a table-of-contents-style tree over a long document and lets an LLM reason down the tree to find relevant sections, instead of chunking + embedding + vector similarity search.

![pageindex — health radar](../../assets/health/pageindex.svg)

## When to use

You're building a Q&A or agent over a small set of long, structured documents — financial filings, regulatory PDFs, technical manuals, research papers — and you've watched vector RAG fail in a specific way: it retrieves chunks that are *semantically near* the question but not actually *relevant* to it, and your domain experts can't trust answers that float free of where they came from. You want retrieval to behave like a human analyst flipping to the right section, and you want every answer to cite a concrete page/section so it's auditable. PageIndex resolves this by parsing the document into a hierarchical tree (sections, subsections, summaries) and, at query time, having an LLM *navigate* that tree — reading summaries and reasoning about which branch to descend — rather than comparing embeddings. There's no vector database to stand up, no chunk-size tuning, and no embedding model to host; the index is the document's own structure.

It's a strong fit when "similarity ≠ relevance" is your actual pain and your corpus is bounded enough that per-query LLM tree traversal is affordable. The project reports 98.7% accuracy on the FinanceBench document-QA benchmark [未验证], and it slots naturally into an agentic setup (it ships an example wiring it into the OpenAI Agents SDK), so you can hand a long PDF to an agent that reasons over its structure and returns grounded, page-anchored citations.

## When NOT to use

- **Large-corpus / web-scale retrieval over millions of short docs.** Per-query LLM tree traversal costs tokens and latency on every lookup; for breadth-first search over a huge flat collection, an embedding + ANN vector store (Qdrant / pgvector, 未收录) is far cheaper and faster. The OSS repo targets per-document trees; "million-document scale" is a hosted **PageIndex File System** feature, not the open library. [推断]
- **You need a turnkey, self-contained system with no LLM bill.** Indexing *and* retrieval both call an LLM (OpenAI by default, others via LiteLLM). Every build and every query spends API tokens; there is no local-embedding-only mode.
- **Short, unstructured, or flat documents.** The whole value is the table-of-contents tree. A document with no meaningful section hierarchy (a chat log, a flat CSV, a one-page memo) gives the reasoner nothing to navigate; ordinary chunking is fine.
- **You want the production "Cloud / MCP / API" pipeline, not the repo.** Vectify markets a hosted PageIndex platform (Chat, MCP, managed API, VPC/on-prem). The OSS repo is the indexing core, not that service — don't assume the repo gives you the managed product. [未验证]
- **You need a graph database or multi-hop entity traversal.** PageIndex indexes one document's structure; it is not a knowledge graph. For entity/relationship traversal across a corpus, see [FalkorDB](falkordb.md) or graph builders below.
- **Maturity / stability risk.** No tagged release, MIT but young; APIs and CLI flags may shift release-to-release.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [FalkorDB](falkordb.md) | ✅ | Pick FalkorDB when you need a persistent property graph for GraphRAG, not a per-document reasoning tree. | Property-graph DB for GraphRAG (vector + multi-hop traversal); PageIndex is a per-document reasoning tree, not a graph store — different retrieval primitive. |
| [graphify](graphify.md) | ✅ | Pick graphify when the goal is a code/docs knowledge graph rather than one document's table-of-contents tree. | Builds a knowledge graph from code/docs; PageIndex builds a hierarchical ToC tree of one document and reasons over it — no entity graph. |
| [code-review-graph](code-review-graph.md) | ✅ | Pick code-review-graph when the target is a domain-specific code-review graph. | Domain-specific code-review graph; orthogonal to document tree retrieval. |
| [LlamaIndex](../agent-frameworks/workflow-builders/llamaindex.md) | ✅ | Pick LlamaIndex when you need a broad RAG framework with many index types rather than one vectorless reasoning index. | General RAG framework with many indices incl. a tree/summary index; far broader and embedding-centric, where PageIndex is a focused vectorless reasoning index. |
| RAPTOR | 未收录 | Pick RAPTOR when recursive clustering plus summarization trees and embedding-time retrieval are the desired design. | Recursive clustering + summarization tree for retrieval, but still embedding-retrieved at query time; PageIndex navigates the tree by LLM reasoning instead of vector search. |
| pgvector / Qdrant | 未收录 | Pick a vector store when classic embedding + ANN retrieval is sufficient and cheaper at scale. | Classic embedding + ANN vector retrieval; cheaper at scale and breadth, but exactly the "similarity ≠ relevance" failure mode PageIndex is built to avoid. |

## Tech stack

- **Language:** Python.
- **Indexing:** parses PDF / Markdown into a hierarchical tree (sections, subsections, node summaries) resembling a table of contents.
- **Retrieval:** LLM reasoning over the tree (navigate-and-descend), not vector similarity — no embedding model, no ANN index.
- **LLM access:** OpenAI by default (`OPENAI_API_KEY`); multi-provider via LiteLLM (provider routing claimed in README).
- **Entry point:** `python3 run_pageindex.py --pdf_path <doc>` with options for model, page/token limits, node IDs/summaries.
- **Adjacent (newer) examples:** agentic vectorless RAG via the OpenAI Agents SDK; vision-based RAG over page images.

## Dependencies

- **Runtime:** Python 3; PDF parsing for ingestion.
- **Required:** an LLM API key — `OPENAI_API_KEY` out of the box; other providers routed through LiteLLM.
- **No infra:** no vector database, no embedding service, no separate datastore to operate — the index is files/JSON describing the tree.
- **Cost dependency:** token spend on the LLM is intrinsic to both indexing and querying (not optional infra you can drop).

## Ops difficulty

**Low.** There is almost no infrastructure to run: clone the repo, set an API key, point the script at a PDF, and you get a tree you can query — no vector DB to provision, tune, or back up. The real operational concern is not servers but **LLM cost and latency**: every query reasons over the tree with model calls, so per-query token spend and response time are your scaling ceiling, and you must budget/observe API usage rather than memory or disk. Reproducibility and quality also hinge on the chosen model, which is a moving dependency. For the managed/MCP/VPC pipeline, ops shifts to the hosted product and is out of scope for the OSS repo.

## Health & viability

- **Responsiveness**: Grade C — median first-response time 558.2 hours across 7 qualifying issues/PRs.
- **Maintenance — active.** Default branch last pushed 2026-06, not archived, but there is **no tagged release** at all — "version" is whatever `main` holds, so pin a commit for reproducibility. Active development without semver means you track a moving target. `[未验证]`
- **Governance / backing — single vendor (Vectify AI).** **Organization**-owned (`VectifyAI/PageIndex`), ~33k stars [未验证]. The roadmap is vendor-driven, and the open repo is the *indexing core* of a larger commercial offering (hosted PageIndex Cloud/MCP/API/VPC) — so the OSS surface is a loss-leader for the product, with the usual open-core risk that the best features land in the hosted tier. `[推断]`
- **Age & Lindy — young, ~1 year (created 2025-04).** Old enough to have shipped real benchmarks (98.7% FinanceBench, self-reported [未验证]) but not long enough to be a Lindy-safe bet; APIs/CLI flags can shift release-to-release. Treat as a promising young library, not a settled standard.
- **Adoption / ecosystem — niche but real.** Slots into agentic stacks (OpenAI Agents SDK example), multi-provider via LiteLLM; the "vectorless RAG" framing has visible mindshare. MIT-licensed, no relicense observed — but verify the OSS-vs-hosted boundary before assuming a feature ships in the repo.

## Caveats (unverified)

- [未验证] Stars ~33.4k as of 2026-06 — GitHub stars are unreliable and date-sensitive; indicative only.
- [未验证] The 98.7% FinanceBench accuracy and "significantly outperforms vector RAG" claims are the project's own reported numbers; benchmark results depend on setup and were not independently reproduced here.
- [未验证] LiteLLM multi-provider routing, the OpenAI Agents SDK example, and vision-based RAG are described in project materials at verification time; confirm against the current repo before relying on them.
- [推断] The "PageIndex File System" for million-document scale and the Cloud/MCP/API/VPC offerings appear to be hosted-product features distinct from the OSS repo; the open library targets per-document trees — verify the OSS/hosted boundary before assuming a feature ships in the repo.
- [未验证] No tagged GitHub release at verification time (latestRelease is null); "version" is whatever the default branch holds, so pin a commit for reproducibility.
- [未验证] Exact required Python dependencies and supported input formats beyond PDF/Markdown are from README at verification time and may change.
