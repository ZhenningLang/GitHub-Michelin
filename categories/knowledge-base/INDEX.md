# knowledge-base

> Category node. Personal knowledge bases and second-brain apps — accumulate, link, and query your own document corpus, optionally LLM-maintained.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **LLM Wiki** | Use it when you want your own documents compiled once into an interlinked local wiki the LLM keeps current, instead of re-deriving answers with RAG on every query. | B (4/6) | [→](llm-wiki.md) |
| **Logseq** | Use it when you want a local-first outliner you author yourself and query with Datalog, with LLM features left to plugins. | B (5/6) | [→](logseq.md) |
| **SiYuan** | Use it when you want a self-hosted block-level knowledge workspace where humans and AI agents co-edit — but some features are paywalled (open-core). | B (5/6) | [→](siyuan.md) |
| **Khoj** | Use it when you want a self-hostable AI second brain that answers from your docs and the web across browser/desktop/Obsidian, with local or online LLMs. | C (6/6) | [→](khoj.md) |
| **Reor** | Use it as a pattern source for local-first AI note-taking; it is archived (2025-05), so do not bet production on it. | E (4/6) | [→](reor.md) |
| **OpenKB** | Use it when you want long documents compiled once by an LLM into a persistent, cross-linked Markdown wiki you query afterwards — headless CLI, no vector DB. | B (6/6) | [→](openkb.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [LLM Wiki](llm-wiki.md) | ✅ | B (4/6) | Compiles sources into a maintained wiki under a co-evolved schema — but it is young (2026-04), single-maintainer, and pre-compiled errors get trusted later. |
| [Logseq](logseq.md) | ✅ | B (5/6) | Mature local-first outliner with Datalog queries and a large community — but the human does the linking, and the DB rewrite is beta with a data-loss warning. |
| [SiYuan](siyuan.md) | ✅ | B (5/6) | Block-level references plus a Go kernel and Docker self-hosting — but open-core paywalls and a single-vendor ecosystem. |
| [Khoj](khoj.md) | ✅ | C (6/6) | Broadest second-brain surface (web/desktop/Obsidian/WhatsApp) over many LLMs — but heavier Python + pgvector ops and a stalled release line. |
| [Reor](reor.md) | ✅ | E (4/6) | Closest direct competitor to LLM Wiki (local embeddings + Ollama + LanceDB) — but archived, so treat it as a pattern source only. |
| [OpenKB](openkb.md) | ✅ | B (6/6) | The headless counterpart to LLM Wiki: CLI + optional API, vectorless PageIndex retrieval, generators (agent skill / deck / graph) — but a 5.5-month-old v0.x whose public merge cadence paused in 2026-07. |
| NotebookLM / Obsidian | 未收录 | — | Hosted SaaS and proprietary freeware named in the pages: no repository to index. |

## What belongs here

User-facing systems where a person **accumulates their own knowledge corpus and queries it** — personal wikis, outliners, and AI "second brain" apps. Not the retrieval infrastructure underneath (see `rag-retrieval`), not memory an agent reads/writes about you (see `agent-memory`), and not team collaboration (see `team-chat`).
