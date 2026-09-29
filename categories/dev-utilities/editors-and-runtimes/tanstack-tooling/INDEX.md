# tanstack-tooling

> Category node. Dev-time tooling around the TanStack stack — scaffolding CLIs, a devtools panel, shared lint/build presets, and an in-browser project runtime.
> ← back to [editors-and-runtimes](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **TanStack CLI** | Use it when you are starting a TanStack Start/Router app and want auth, database, deployment and monitoring composed in as add-ons — not when the stack isn't TanStack, or the project has no `.cta.json` to reconcile against. | B (6/6) | [→](tanstack-cli.md) |
| **TanStack Devtools** | Use it when your Vite app mounts several TanStack (or your own) library devtools and you want one dockable in-page panel plus click-to-source, stripped from production — not for React internals (use React DevTools), non-Vite/Rspack builds, or a dev server others can reach (open command-injection issue #464). | B (6/6) | [→](tanstack-devtools.md) |
| **TanStack Config** | Use it when a TypeScript library in a pnpm monorepo should lint (and, legacy, dual-build ESM/CJS) exactly like TanStack's own packages — not for new builds (TanStack itself moves to tsdown) or release pipelines (use Changesets). | B (6/6) | [→](tanstack-config.md) |
| **TanStack Container** | Use it when your product must run a real Vite / TanStack Start project inside the visitor's browser — install, processes, preview, save/resume — under MIT source with self-hosted assets instead of a closed commercial core — but the npm packages are unpublished as of 2026-09 and the project disclaims being a security boundary. | C (5/6) | [→](tanstack-container.md) |
| **TanStack alt-cli** | Use it only as a pattern source for integration-composition scaffolding — a one-week January-2026 TanStack experiment, archived, whose @tanstack/cli npm name now ships the mainline CLI; for anything you run, use TanStack CLI. | D (5/6) | [→](tanstack-alt-cli.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [TanStack CLI](tanstack-cli.md) | ✅ | B (6/6) | Use it when you are starting a TanStack Start/Router app and want auth, database, deployment and monitoring composed in as add-ons — not when the stack isn't TanStack, or the project has no `.cta.json` to reconcile against. |
| [TanStack Devtools](tanstack-devtools.md) | ✅ | B (6/6) | Use it when your Vite app mounts several TanStack (or your own) library devtools and you want one dockable in-page panel plus click-to-source, stripped from production — not for React internals (use React DevTools), non-Vite/Rspack builds, or a dev server others can reach (open command-injection issue #464). |
| [TanStack Config](tanstack-config.md) | ✅ | B (6/6) | Use it when a TypeScript library in a pnpm monorepo should lint (and, legacy, dual-build ESM/CJS) exactly like TanStack's own packages — not for new builds (TanStack itself moves to tsdown) or release pipelines (use Changesets). |
| [TanStack Container](tanstack-container.md) | ✅ | C (5/6) | Use it when your product must run a real Vite / TanStack Start project inside the visitor's browser — install, processes, preview, save/resume — under MIT source with self-hosted assets instead of a closed commercial core — but the npm packages are unpublished as of 2026-09 and the project disclaims being a security boundary. |
| [TanStack alt-cli](tanstack-alt-cli.md) | ✅ | D (5/6) | Use it only as a pattern source for integration-composition scaffolding — a one-week January-2026 TanStack experiment, archived, whose @tanstack/cli npm name now ships the mainline CLI; for anything you run, use TanStack CLI. |

## What belongs here

Tools published by the TanStack org whose value mostly assumes you are on (or building) the TanStack stack. The TanStack *libraries* themselves (Query, Router, Table, Form) live under `web-ui`. If your stack is not TanStack, start from `runtimes-and-compilers` or the relevant `web-ui` category instead.
