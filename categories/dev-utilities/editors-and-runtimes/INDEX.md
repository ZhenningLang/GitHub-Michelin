# editors-and-runtimes

> Category node. Code editors, IDE extensions, app runtimes, and JavaScript/TypeScript toolchains.
> ← back to [dev-utilities](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **IdeaVim** | Use it when you live in a JetBrains IDE but want Vim motions, modes, and a `.ideavimrc` — but it's an emulation subset, power users will hit fidelity gaps. | A (4/6) | [→](ideavim.md) |
| **VS Code** | Use it when you need a fast, cross-platform code editor with intelligent completion, debugging, and the largest extension marketplace — but it's Electron-based and the distributed build includes Microsoft telemetry. | A (5/6) | [→](vscode.md) |
| **Tauri** | Use it when you want to build small, fast, secure cross-platform desktop and mobile apps with a web frontend using Rust and native OS webviews instead of Electron. | A (6/6) | [→](tauri.md) |
| **Deno** | Use it when you want a modern JavaScript/TypeScript runtime with secure defaults, built-in tooling, and native TypeScript support without node_modules. | A (6/6) | [→](deno.md) |
| **Bun** | Use it when you want an all-in-one, incredibly fast JavaScript/TypeScript toolkit (runtime, bundler, test runner, package manager) in a single binary — but verify the license before commercial use. | A (5/6) | [→](bun.md) |
| **Zed** | Use it when you want a high-performance, native code editor with real-time multiplayer collaboration — but its extension ecosystem is far smaller than VS Code's and it's only ~4 years old. | A (4/6) | [→](zed.md) |
| **scriptc** | Use it when a well-typed TypeScript CLI or small server must ship as a small, fast-starting native binary or WASI module — but it's a 2-month-old Vercel Labs experiment that rejects what it can't compile statically. | C (6/6) | [→](scriptc.md) |
| **TanStack CLI** | Use it when you are starting a TanStack Start/Router app and want auth, database, deployment and monitoring composed in as add-ons — not when the stack isn't TanStack, or the project has no `.cta.json` to reconcile against. | B (6/6) | [→](tanstack-cli.md) |
| **TanStack Devtools** | Use it when your Vite app mounts several TanStack (or your own) library devtools and you want one dockable in-page panel plus click-to-source, stripped from production — not for React internals (use React DevTools), non-Vite/Rspack builds, or a dev server others can reach (open command-injection issue #464). | B (6/6) | [→](tanstack-devtools.md) |
| **TanStack Config** | Use it when a TypeScript library in a pnpm monorepo should lint (and, legacy, dual-build ESM/CJS) exactly like TanStack's own packages — not for new builds (TanStack itself moves to tsdown) or release pipelines (use Changesets). | B (6/6) | [→](tanstack-config.md) |
| **TanStack Container** | Use it when your product must run a real Vite / TanStack Start project inside the visitor's browser — install, processes, preview, save/resume — under MIT source with self-hosted assets instead of a closed commercial core — but the npm packages are unpublished as of 2026-09 and the project disclaims being a security boundary. | C (5/6) | [→](tanstack-container.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [IdeaVim](ideavim.md) | ✅ | A (4/6) | Use it when you live in a JetBrains IDE but want Vim motions, modes, and a `.ideavimrc` — but it's an emulation subset, power users will hit fidelity gaps. |
| [VS Code](vscode.md) | ✅ | A (5/6) | Use it when you need a fast, cross-platform code editor with intelligent completion, debugging, and the largest extension marketplace — but it's Electron-based and the distributed build includes Microsoft telemetry. |
| [Tauri](tauri.md) | ✅ | A (6/6) | Use it when you want to build small, fast, secure cross-platform desktop and mobile apps with a web frontend using Rust and native OS webviews instead of Electron. |
| [Deno](deno.md) | ✅ | A (6/6) | Use it when you want a modern JavaScript/TypeScript runtime with secure defaults, built-in tooling, and native TypeScript support without node_modules. |
| [Bun](bun.md) | ✅ | A (5/6) | Use it when you want an all-in-one, incredibly fast JavaScript/TypeScript toolkit (runtime, bundler, test runner, package manager) in a single binary — but verify the license before commercial use. |
| [Zed](zed.md) | ✅ | A (4/6) | Use it when you want a high-performance, native code editor with real-time multiplayer collaboration — but its extension ecosystem is far smaller than VS Code's and it's only ~4 years old. |
| [scriptc](scriptc.md) | ✅ | C (6/6) | Use it when a well-typed TypeScript CLI or small server must ship as a small, fast-starting native binary or WASI module — but it's a 2-month-old Vercel Labs experiment that rejects what it can't compile statically. |
| [TanStack CLI](tanstack-cli.md) | ✅ | B (6/6) | Use it when you are starting a TanStack Start/Router app and want auth, database, deployment and monitoring composed in as add-ons — not when the stack isn't TanStack, or the project has no `.cta.json` to reconcile against. |
| [TanStack Devtools](tanstack-devtools.md) | ✅ | B (6/6) | Use it when your Vite app mounts several TanStack (or your own) library devtools and you want one dockable in-page panel plus click-to-source, stripped from production — not for React internals (use React DevTools), non-Vite/Rspack builds, or a dev server others can reach (open command-injection issue #464). |
| [TanStack Config](tanstack-config.md) | ✅ | B (6/6) | Use it when a TypeScript library in a pnpm monorepo should lint (and, legacy, dual-build ESM/CJS) exactly like TanStack's own packages — not for new builds (TanStack itself moves to tsdown) or release pipelines (use Changesets). |
| [TanStack Container](tanstack-container.md) | ✅ | C (5/6) | Use it when your product must run a real Vite / TanStack Start project inside the visitor's browser — install, processes, preview, save/resume — under MIT source with self-hosted assets instead of a closed commercial core — but the npm packages are unpublished as of 2026-09 and the project disclaims being a security boundary. |

## What belongs here

Code editors, IDE extensions, app runtimes, and JavaScript/TypeScript toolchains.
