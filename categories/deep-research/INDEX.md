# deep-research

> Category node. Iterative multi-source research agents that search, scrape, and synthesize.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **deep-research** | Use it when you want to read and fork a ~500-line TypeScript deep-research loop — Firecrawl search plus breadth/depth recursion into a cited report — but it is a single-author 0.0.1 demo with minimal error handling and no cost cap. | B (4/6) | [→](deep-research.md) |
| **Vane** | Use it when you want a self-hosted, privacy-focused Perplexity-style cited answer engine over your own SearxNG and chosen LLM. | B (5/6) | [→](vane.md) |
| **Local Deep Research** | Use it when you need a self-hosted, fully-local deep-research agent that keeps sensitive queries on your own machine. | B (5/6) | [→](local-deep-research.md) |
| **Agent-Reach** | Use it when your agent needs to read and search web plus social platforms without paid APIs. | B (5/6) | [→](agent-reach.md) |
| **MiroThinker** | Use it when you want a self-hosted, open-weights deep-research agent you can study and extend on your own GPUs — but it needs a GPU cluster plus paid external APIs and is under a year old with no Lindy. | B (4/6) | [→](mirothinker.md) |
| **GPT Researcher** | Use it when you want a ready-to-run app that turns one question into a cited multi-page report from the web or your own files — but its defaults send data to OpenAI and Tavily, so local-only use needs your own configuration. | A (6/6) | [→](gpt-researcher.md) |
| **Open Deep Research** | Use it when you are designing your own LangGraph research agent and want a readable supervisor-plus-parallel-researchers blueprint with a benchmark harness — but the repo was archived in 2026, so study or fork it rather than run it. | D (5/6) | [→](open-deep-research.md) |
| **STORM** | Use it when you need a Wikipedia-style long draft with numbered citations on an unfamiliar topic, built from multi-perspective research and an outline — but it has had no merged changes since 2025-09; treat it as a reference implementation. | C (5/6) | [→](storm.md) |
| **node-DeepResearch** | Use it when users ask multi-hop factual questions and you want a self-hosted, OpenAI-compatible endpoint that keeps searching until it has one referenced short answer — but page reading needs Jina's hosted APIs, and its code tool is unsandboxed. | B (4/6) | [→](node-deepresearch.md) |
| **Hyperresearch** | Use it when you're in Claude Code and need a high-stakes, citation-audited research report — a 16-step adversarial pipeline plus a persistent source vault; heavy on time and tokens, Claude-Code-only. | B (5/6) | [→](hyperresearch.md) |
| **last30days** | Use it when you want your agent to brief you on what Reddit, X, YouTube, HN and Polymarket said about a topic in the last 30 days, ranked by engagement — but it loads a ~258 KB skill prompt per call and leans on scraping and browser-session cookies. | B (6/6) | [→](last30days.md) |
| **OpenScience** | Use it when the research task must actually run code on your own files — literature and database search, Python/R kernels, cluster jobs — with every step left in an auditable turn trace. | B (6/6) | [→](openscience.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [deep-research](deep-research.md) | ✅ | B (4/6) | Buys a whole research loop that fits in your head; costs hard dependence on Firecrawl and cloud LLMs, with no production hardening. |
| [Vane](vane.md) | ✅ | B (5/6) | Use it when you want a self-hosted, privacy-focused Perplexity-style cited answer engine over your own SearxNG and chosen LLM. |
| [Local Deep Research](local-deep-research.md) | ✅ | B (5/6) | Use it when you need a self-hosted, fully-local deep-research agent that keeps sensitive queries on your own machine. |
| [Agent-Reach](agent-reach.md) | ✅ | B (5/6) | Use it when your agent needs to read and search web plus social platforms without paid APIs. |
| [MiroThinker](mirothinker.md) | ✅ | B (4/6) | Use it when you want a self-hosted, open-weights deep-research agent you can study and extend on your own GPUs — but it needs a GPU cluster plus paid external APIs and is under a year old with no Lindy. |
| [Hyperresearch](hyperresearch.md) | ✅ | B (5/6) | Claude-Code-locked 16-step research pipeline with adversarial critics, cite-checking, and a persistent vault; pre-1.0 churn and its leaderboard claim is a self-run projection. |
| [last30days](last30days.md) | ✅ | B (6/6) | Slash-command skill that fuses 30 days of Reddit/X/YouTube/HN/Polymarket signal into one cited brief; young, hyped, context-heavy, and dependent on scraping. |
| [OpenScience](openscience.md) | ✅ | B (6/6) | An OpenCode-shaped workbench loaded for science: real kernels, real connectors, real files — young (3 months), churn-heavy, with an account-gated interactive surface. |
| Perplexity / OpenAI Deep Research | 未收录 | — | Other deep-research agents/services named across the pages. |

## What belongs here

Agents whose primary job is **iterative web / multi-source research** — search, fetch, synthesize. Not single-shot RAG indexes (see `rag-retrieval`), not general agent frameworks (see `agent-frameworks`).
