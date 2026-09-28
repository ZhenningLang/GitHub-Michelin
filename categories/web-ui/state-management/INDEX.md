# state-management

> Category node. Client-side state stores — hold shared reactive values outside the component tree, recompute derived values, and let components subscribe to just the slice they read.
> ← back to [web-ui](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **TanStack Store** | Your framework-agnostic library or app core keeps re-writing the same subscribe-and-notify glue per framework, and you want one signal-based store with derived values plus thin adapters that re-render a component only when its selected slice changes. | A (6/6) | [→](tanstack-store.md) |
| **TanStack Persist** | Your UI state resets on every reload and each feature re-writes the localStorage load/parse/save loop; this wraps it in a useState-shaped hook with version busting and expiry — watch-list only, nothing on npm yet. | C (5/6) | [→](tanstack-persist.md) |

## Comparison matrix

| Project | Frameworks | State model | Pick it over the rest when | License |
| --- | --- | --- | --- | --- |
| TanStack Store | React, Preact, Vue, Angular, Solid, Svelte, Lit, Octane | immutable value + updater, derived stores from functions, signals core | the store must live in framework-neutral code, or you want the runtime TanStack Router/Form already use — and can absorb 0.x API churn without persistence/devtools | MIT |
| TanStack Persist | React only (Solid/Preact promised; Vue/Angular/Svelte need contributors) | useState-shaped persisted state, { buster, state, timestamp } envelope, maxAge expiry, select subset | you want TanStack-ecosystem persistence with built-in invalidation and can vendor an unpublished 0.x — not a production install today | MIT |

## What belongs here

Libraries that hold client-side application state and notify UI components when it changes (stores, atoms, signals, state machines used as stores), and libraries that persist that state to browser storage (persistence adapters, persisted-state hooks). Server-state caches and data fetching belong in `data-fetching`; form-specific state belongs in `forms`.
