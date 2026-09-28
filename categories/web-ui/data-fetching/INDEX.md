# data-fetching

> Category node. Client-side data-fetching and server-state caching libraries — request dedupe, stale-while-revalidate caches, mutations and invalidation for REST/GraphQL backends.
> ← back to [web-ui](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **TanStack Query** | Your front-end components each hand-roll fetch + loading + error, fetch the same data twice and show stale rows after a save — and your backend is REST or mixed rather than a GraphQL API that needs a normalized entity cache. | A (5/6) | [→](tanstack-query.md) |

## Comparison matrix

| Project | Frameworks | Cache model | Pick it over the rest when | License |
| --- | --- | --- | --- | --- |
| TanStack Query | React, Vue, Solid, Svelte, Preact; Angular/Lit experimental | per-key response cache, stale-while-revalidate, GC | you want explicit staleTime, invalidation by key prefix and one core across frameworks | MIT |

## What belongs here

Libraries that fetch, cache and keep server data in sync inside a client app (server-state management). Client-only state stores and routers belong elsewhere.
