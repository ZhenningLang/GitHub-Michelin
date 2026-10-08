# code-intelligence

> Category node. Code-intelligence graphs and code-search indexes that let a coding agent (or a human) ask structural questions about a repository — callers, blast radius, ownership — instead of grepping.
> ← back to [rag-retrieval](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **graphify** | Use it when an agent needs to query a whole repo's code, schemas and docs as a knowledge graph instead of grepping. | C (5/6) | [→](graphify.md) |
| **code-review-graph** | Use it when an AI reviewer keeps burning context on a large repo and you want only the blast-radius files. | B (6/6) | [→](code-review-graph.md) |
| **Understand-Anything** | Use it when you want any codebase turned into an explorable, queryable knowledge graph for an agent — younger and less proven than graphify. | B (6/6) | [→](understand-anything.md) |
| **SCIP** | Use it when code search, review bots or agent retrieval need compiler-accurate definitions and references across a polyglot codebase, indexed once per commit in CI — but it is a format, not a query service, and code must build to be indexed. | A (6/6) | [→](scip.md) |
| **Sourcegraph** | Use it when designing code search across hundreds of repos and you want to read how a real product handled clone syncing, indexing and code navigation — but it is an archived snapshot, Enterprise-licensed after 2023-06, so deploy Zoekt instead. | D (4/6) | [→](sourcegraph.md) |
| **Ix** | Use it when your coding agent keeps grepping a polyglot repo to find callers and blast radius and you can run Docker — accepting a closed-source backend image and a seven-month-old v0.x project. | B (6/6) | [→](ix.md) |
| **Repowise** | Use it when your agent re-expends context rediscovering a big repo every task and you want one keyless local index answering graph, git, health, dead-code and decision questions over MCP — accepting a six-month-old v0.x AGPL vendor project. | C (6/6) | [→](repowise.md) |
| **Jevgrep** | Use it when your agent must orient in an unfamiliar repo by asking what the code does — no index to build — accepting per-query API cost and source uploaded to a hosted evaluator model; two days old, solo-maintained, macOS/Linux only. | C (4/6) | [→](jevgrep.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [graphify](graphify.md) | ✅ | C (5/6) | Use it when an agent needs to query a whole repo's code, schemas and docs as a knowledge graph instead of grepping. |
| [code-review-graph](code-review-graph.md) | ✅ | B (6/6) | Use it when an AI reviewer keeps burning context on a large repo and you want only the blast-radius files. |
| [Understand-Anything](understand-anything.md) | ✅ | B (6/6) | Code → explorable knowledge graph an agent can query; younger than graphify, with an unverified star count and egress boundary. |
| [Ix](ix.md) | ✅ | B (6/6) | Use it when your coding agent keeps grepping a polyglot repo to find callers and blast radius and you can run Docker — accepting a closed-source backend image and a seven-month-old v0.x project. |
| [Repowise](repowise.md) | ✅ | C (6/6) | Use it when your agent re-expends context rediscovering a big repo every task and you want one keyless local index answering graph, git, health, dead-code and decision questions over MCP — accepting a six-month-old v0.x AGPL vendor project. |
| [Jevgrep](jevgrep.md) | ✅ | C (4/6) | Use it when your agent must orient in an unfamiliar repo by asking what the code does — no index to build — accepting per-query API cost and source uploaded to a hosted evaluator model; two days old, solo-maintained, macOS/Linux only. |
| [SCIP](scip.md) | ✅ | A (6/6) | Type-checked precision that grep and tree-sitter graphs cannot match, at the cost of per-language indexers that must each be maintained, indexing only buildable code, and commits concentrated in a couple of maintainers. |
| [Sourcegraph](sourcegraph.md) | ✅ | D (4/6) | Gets the whole product's architecture in one readable tree with its own design docs; costs no patches since 2024-08, a subscription for production use, or forking a three-year-old Apache-2.0 commit yourself. |

## Field evidence: do agents actually use these? (as of 2026-09-30)

Read this before adopting any tool in this category. Public issues, discussions and the projects' own benchmarks point the same way: the bottleneck is not graph quality but whether the agent calls the tool at all, and no project has shown a measurable gain in answer quality.

- **Agents do not call them by default.** graphify measured 8,348 injected nudges yielding 339 calls (~4%), with the nudges costing ~3.7x the tokens of all query output ([graphify#3435](https://github.com/Graphify-Labs/graphify/issues/3435)). Serena's own docs say the agent "will often fail to make proper use of Serena's tools… (a behavior known as agent drift)" ([docs](https://github.com/oraios/serena/blob/main/docs/02-usage/030_clients.md)). Repowise's cross-tool benchmark recorded code-review-graph called 0/15 times on Claude Code and its own call rate dropping from 4/15 to 3/15 on rerun — "Adoption is not a stable property of a tool" ([BENCHMARKS.md:413-469](https://github.com/repowise-dev/repowise/blob/54c9618dac6b8291317138cd9e812e640c9acadf/docs/BENCHMARKS.md#L413-L469)). Tool descriptions matter: Jevgrep's first-call rate went 0/5 → 5/5 after a description rewrite ([jevgrep#29](https://github.com/dzhng/jevgrep/issues/29)).
- **Forcing "graph first" made results worse.** code-review-graph withdrew its instruction to always query the graph before Grep/Read after a user reported models "noticeably worse" at coding ([#314](https://github.com/tirth8205/code-review-graph/issues/314) → [PR #886](https://github.com/tirth8205/code-review-graph/pull/886)). Empty results are read as facts: "Agents read the zero as proof and act on it" ([PR #884](https://github.com/tirth8205/code-review-graph/pull/884)); OpenCode's experimental LSP tool returns empty results instead of initialization errors ([anomalyco/opencode#40413](https://github.com/anomalyco/opencode/issues/40413)).
- **No measured quality gain.** Repowise: "No tool here measurably changed answer quality in either direction" ([BENCHMARKS.md:452-455](https://github.com/repowise-dev/repowise/blob/54c9618dac6b8291317138cd9e812e640c9acadf/docs/BENCHMARKS.md#L452-L455); a competitor's measurement, not neutral). A same-model user A/B found graphify 1.6–1.9x more expensive with the plain agent giving the more complete answer ([graphify#985](https://github.com/Graphify-Labs/graphify/issues/985)). Jevgrep's README reports 8/10 tasks solved with and without it. Reported wins are narrow: tracing forward call chains, reference lookup in repos with many same-name identifiers, and weaker models.
- **Go is a weak spot for tree-sitter graphs.** Against a Go compiler (RTA) call graph, code-review-graph 2.3.7's recall was 0.026–0.032 on gitleaks and 0.086–0.201 on syft; 44% of repowise's own missed edges are dynamic dispatch ([BENCHMARKS.md:74-80, 137](https://github.com/repowise-dev/repowise/blob/54c9618dac6b8291317138cd9e812e640c9acadf/docs/BENCHMARKS.md#L74-L80)). graphify resolved 0 of 21 intra-module Go imports before a fix ([graphify#3746](https://github.com/Graphify-Labs/graphify/issues/3746)). For Go, a real language server (gopls) is the precise route.

Not found: any neutral third-party measurement of task success, and any LSP-vs-grep comparison on Go.

## What belongs here

Tools whose primary job is to **index a codebase for retrieval** — symbol/call graphs, knowledge graphs over code + docs, code-search engines and code-index formats — so an agent reads the right few files instead of the whole tree. Not general document or vector retrieval (see `vector-search`, `structured-retrieval`), not AI code reviewers that comment on PRs (see `ai-code-review`).
