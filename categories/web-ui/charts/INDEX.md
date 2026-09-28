# charts

> Category node. Charting libraries you embed in a front-end — turn arrays of data into axes, bars, lines and points inside your app, with tooltips, resize and framework integration.
> ← back to [web-ui](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **TanStack Charts** | Your stock chart components cannot draw the custom layer design wants, and the same chart must render in more than one framework and on the server — one typed mark-and-scale definition with SVG SSR, focus and optional Canvas; Alpha 0.x, two months old. | B (6/6) | [→](tanstack-charts.md) |

## Comparison matrix

| Project | Model | Output | Frameworks | Pick it over the rest when | License |
| --- | --- | --- | --- | --- | --- |
| TanStack Charts | grammar of graphics (marks, channels, scales), custom marks via a scene protocol | SVG (default), Canvas (opt-in), static SVG on the server | React, Preact, Vue, Solid, Svelte, Angular, Lit, Alpine, Octane, React Native (experimental), vanilla DOM | one definition must serve several frameworks and SSR and grow into custom marks — and you can pin an Alpha version | MIT |

## What belongs here

Client-side charting and plotting libraries a developer embeds in application code (chart components, visualization grammars, low-level D3-style primitives). Self-hosted BI tools with queries and saved dashboards belong in `data-visualization`; diagram-as-code tools belong in `diagramming`.
