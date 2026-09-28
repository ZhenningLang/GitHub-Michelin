# state-management

> Category node. Client-side state stores — hold shared reactive values outside the component tree, recompute derived values, and let components subscribe to just the slice they read.
> ← back to [web-ui](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **TanStack Store** | Your framework-agnostic library or app core keeps re-writing the same subscribe-and-notify glue per framework, and you want one signal-based store with derived values plus thin adapters that re-render a component only when its selected slice changes. | A (6/6) | [→](tanstack-store.md) |

## Comparison matrix

| Project | Frameworks | State model | Pick it over the rest when | License |
| --- | --- | --- | --- | --- |
| TanStack Store | React, Preact, Vue, Angular, Solid, Svelte, Lit, Octane | immutable value + updater, derived stores from functions, signals core | the store must live in framework-neutral code, or you want the runtime TanStack Router/Form already use — and can absorb 0.x API churn without persistence/devtools | MIT |

## What belongs here

Libraries that hold client-side application state and notify UI components when it changes (stores, atoms, signals, state machines used as stores). Server-state caches and data fetching belong in `data-fetching`; form-specific state belongs in `forms`.
