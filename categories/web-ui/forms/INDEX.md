# forms

> Category node. Form state and validation libraries — hold field values, touched/dirty flags and errors, run sync/async validators, and hand typed values to submit.
> ← back to [web-ui](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **TanStack Form** | Your forms hand-roll `useState` per input, touched flags and debounced async checks, and a misspelled field name compiles fine — and you want one typed, headless form model across React, Vue, Angular, Solid, Svelte or Lit. | A (6/6) | [→](tanstack-form.md) |

## Comparison matrix

| Project | Frameworks | State model | Pick it over the rest when | License |
| --- | --- | --- | --- | --- |
| TanStack Form | React, Vue, Angular, Solid, Svelte, Lit, Preact | controlled, one typed store per form, render-prop fields | you need types inferred from default values, async validation debounce and one core across frameworks — and can absorb the v2 API change | MIT |

## What belongs here

Libraries that manage form state and validation inside a client app (values, errors, touched/dirty, submission). Schema validators on their own, UI input components and server-state caches belong elsewhere.
