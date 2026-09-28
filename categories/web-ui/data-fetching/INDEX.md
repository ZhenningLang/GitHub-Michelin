# data-fetching

> Category node. Client-side data-fetching and server-state caching libraries — request dedupe, stale-while-revalidate caches, mutations and invalidation for REST/GraphQL backends.
> ← back to [web-ui](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **TanStack Query** | Your front-end components each hand-roll fetch + loading + error, fetch the same data twice and show stale rows after a save — and your backend is REST or mixed rather than a GraphQL API that needs a normalized entity cache. | A (5/6) | [→](tanstack-query.md) |
| **TanStack DB** | Each view demands its own join endpoint and every mutation hand-patches the query cache while re-render cascades jank the UI — load normalized collections once and let incremental live queries plus optimistic transactions keep every screen coherent. | B (6/6) | [→](tanstack-db.md) |

## Comparison matrix

| Project | Frameworks | Cache model | Pick it over the rest when | License |
| --- | --- | --- | --- | --- |
| TanStack Query | React, Vue, Solid, Svelte, Preact; Angular/Lit experimental | per-key response cache, stale-while-revalidate, GC | you want explicit staleTime, invalidation by key prefix and one core across frameworks | MIT |
| TanStack DB | React, Vue, Svelte, Solid, Angular | in-memory normalized collections, differential-dataflow live queries, optimistic transactions | data arrives via TanStack Query or a sync engine and you need reactive cross-collection joins and instant optimistic writes | MIT |

## What belongs here

Libraries that fetch, cache and keep server data in sync inside a client app (server-state management). Client-only state stores and routers belong elsewhere.
