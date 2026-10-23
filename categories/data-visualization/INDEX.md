# data-visualization

> Category node. Data-chart compilation and rendering libraries, plus self-hosted BI / exploration dashboards over SQL warehouses.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Flint** | Reuse field meanings and chart mappings across renderers; review overflow warnings and backend-specific limits. | B (6/6) | [→](flint-chart.md) |
| **Rill** | Review metrics and dashboards as YAML/SQL, then explore shared definitions locally or through a managed deployment. | A (6/6) | [→](rill.md) |
| **Apache Superset** | Use it when you want self-hosted SQL BI dashboards and exploration over a warehouse — not infra metrics/observability. | A (6/6) | [→](superset.md) |
| **Evidence** | Use it when analytics engineers want reports as Markdown plus SQL files in git that can be diffed, reviewed and edited by coding agents — but business users cannot click-build questions, and self-hosting gets only Basic Auth after a 2026 rewrite reset the codebase. | B (6/6) | [→](evidence.md) |
| **Metabase** | Use it when non-SQL staff keep queueing simple data questions and you want a self-hosted app, up the same afternoon, where they click a table, filter and save to a shared dashboard — but SSO, row-level security and Git sync are paid; core is AGPL. | A (4/6) | [→](metabase.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Flint](flint-chart.md) | ✅ | B (6/6) | Semantic chart compiler and optional local MCP rendering; not a governed SQL BI portal or complete backend abstraction. |
| [Rill](rill.md) | ✅ | A (6/6) | Code-owned semantic metrics over DuckDB/OLAP; local Developer is not a turnkey governed production portal. |
| [Apache Superset](superset.md) | ✅ | A (6/6) | Self-hosted SQL BI + exploration over warehouses; heavier multi-service deploy than Metabase. |
| [Grafana](../observability/grafana.md) | ✅ | B (5/6) | Metrics/logs/traces observability dashboards — not warehouse BI; different audience. |
| Redash / Tableau / Looker | 未收录 | — | Other BI/analytics tools named across the pages. |

## What belongs here

Tools whose primary job is **turning tabular data into charts**, or **BI dashboards and data exploration over SQL warehouses** for analysts. Chart libraries consume prepared data; BI applications own a broader exploration workflow. Not infra metrics/observability (see `observability`), not document/graph retrieval (see `rag-retrieval`).
