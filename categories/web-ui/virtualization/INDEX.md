# virtualization

> Category node. List and grid virtualization (windowing) — render only the rows inside the visible window of a long list, table or chat feed, and position them with offsets.
> ← back to [web-ui](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **TanStack Virtual** | A list, table or chat feed with thousands of rows makes the page slow to mount and janky to scroll, and you want to keep your own row markup — a headless virtualizer that computes the visible range and offsets, measures dynamic heights and can pin to the bottom for chat. | A (6/6) | [→](tanstack-virtual.md) |

## Comparison matrix

| Project | Frameworks | Rendering model | Pick it over the rest when | License |
| --- | --- | --- | --- | --- |
| TanStack Virtual | React, Vue, Solid, Svelte, Angular (≥20), Lit, Marko, vanilla | headless: returns visible items + offsets, you render and position | you need your own markup, measured dynamic heights, end-anchored chat, or one virtualizer across frameworks | MIT |

## What belongs here

Libraries that virtualize (window) long lists, grids and feeds in the browser: they decide which items are mounted and where. Full data-grid components, table state libraries and infinite-loading data fetchers belong elsewhere.
