# code-intelligence

> Category node. Code-intelligence graphs and code-search indexes that let a coding agent (or a human) ask structural questions about a repository — callers, blast radius, ownership — instead of grepping.
> ← back to [rag-retrieval](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **graphify** | Use it when an agent needs to query a whole repo's code, schemas and docs as a knowledge graph instead of grepping. | C (5/6) | [→](graphify.md) |
| **code-review-graph** | Use it when an AI reviewer keeps burning context on a large repo and you want only the blast-radius files. | B (6/6) | [→](code-review-graph.md) |
| **Understand-Anything** | Use it when you want any codebase turned into an explorable, queryable knowledge graph for an agent — younger and less proven than graphify. | B (6/6) | [→](understand-anything.md) |
| **SCIP** | SCIP Code Intelligence Protocol | A (6/6) | [→](scip.md) |
| **Sourcegraph** | Code AI platform with Code Search & Cody | D (4/6) | [→](sourcegraph.md) |
| **Ix** | Use it when your coding agent keeps grepping a polyglot repo to find callers and blast radius and you can run Docker — accepting a closed-source backend image and a seven-month-old v0.x project. | B (6/6) | [→](ix.md) |
| **Repowise** | Use it when your agent re-expends context rediscovering a big repo every task and you want one keyless local index answering graph, git, health, dead-code and decision questions over MCP — accepting a six-month-old v0.x AGPL vendor project. | C (6/6) | [→](repowise.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [graphify](graphify.md) | ✅ | C (5/6) | Use it when an agent needs to query a whole repo's code, schemas and docs as a knowledge graph instead of grepping. |
| [code-review-graph](code-review-graph.md) | ✅ | B (6/6) | Use it when an AI reviewer keeps burning context on a large repo and you want only the blast-radius files. |
| [Understand-Anything](understand-anything.md) | ✅ | B (6/6) | Code → explorable knowledge graph an agent can query; younger than graphify, with an unverified star count and egress boundary. |
| [Ix](ix.md) | ✅ | B (6/6) | Use it when your coding agent keeps grepping a polyglot repo to find callers and blast radius and you can run Docker — accepting a closed-source backend image and a seven-month-old v0.x project. |
| [Repowise](repowise.md) | ✅ | C (6/6) | Use it when your agent re-expends context rediscovering a big repo every task and you want one keyless local index answering graph, git, health, dead-code and decision questions over MCP — accepting a six-month-old v0.x AGPL vendor project. |
| [SCIP](scip.md) | ✅ | A (6/6) | SCIP Code Intelligence Protocol |
| [Sourcegraph](sourcegraph.md) | ✅ | D (4/6) | Code AI platform with Code Search & Cody |

## What belongs here

Tools whose primary job is to **index a codebase for retrieval** — symbol/call graphs, knowledge graphs over code + docs, code-search engines and code-index formats — so an agent reads the right few files instead of the whole tree. Not general document or vector retrieval (see `vector-search`, `structured-retrieval`), not AI code reviewers that comment on PRs (see `ai-code-review`).
