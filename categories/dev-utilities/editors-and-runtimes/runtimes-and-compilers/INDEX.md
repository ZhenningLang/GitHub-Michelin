# runtimes-and-compilers

> Category node. Where your code runs and what it ships as — JS/TS runtimes, ahead-of-time compilers to native or WASI, and web-frontend desktop app shells.
> ← back to [editors-and-runtimes](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Deno** | Use it when you want a modern JavaScript/TypeScript runtime with secure defaults, built-in tooling, and native TypeScript support without node_modules. | A (6/6) | [→](deno.md) |
| **Bun** | Use it when you want an all-in-one, incredibly fast JavaScript/TypeScript toolkit (runtime, bundler, test runner, package manager) in a single binary — but verify the license before commercial use. | A (5/6) | [→](bun.md) |
| **Tauri** | Use it when you want to build small, fast, secure cross-platform desktop and mobile apps with a web frontend using Rust and native OS webviews instead of Electron. | A (6/6) | [→](tauri.md) |
| **scriptc** | Use it when a well-typed TypeScript CLI or small server must ship as a small, fast-starting native binary or WASI module — but it's a 2-month-old Vercel Labs experiment that rejects what it can't compile statically. | C (6/6) | [→](scriptc.md) |
| **NetWasm** | Use it when a C# program must ship as one tiny standalone WASI component — GC linked in, no .NET runtime on the target — but it's a 7-week-old, single-maintainer pre-1.0 project whose tooling carries a custom non-open-source license. | C (4/6) | [→](netwasm.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Deno](deno.md) | ✅ | A (6/6) | Use it when you want a modern JavaScript/TypeScript runtime with secure defaults, built-in tooling, and native TypeScript support without node_modules. |
| [Bun](bun.md) | ✅ | A (5/6) | Use it when you want an all-in-one, incredibly fast JavaScript/TypeScript toolkit (runtime, bundler, test runner, package manager) in a single binary — but verify the license before commercial use. |
| [Tauri](tauri.md) | ✅ | A (6/6) | Use it when you want to build small, fast, secure cross-platform desktop and mobile apps with a web frontend using Rust and native OS webviews instead of Electron. |
| [scriptc](scriptc.md) | ✅ | C (6/6) | Use it when a well-typed TypeScript CLI or small server must ship as a small, fast-starting native binary or WASI module — but it's a 2-month-old Vercel Labs experiment that rejects what it can't compile statically. |
| [NetWasm](netwasm.md) | ✅ | C (4/6) | Use it when a C# program must ship as one tiny standalone WASI component — GC linked in, no .NET runtime on the target — but it's a 7-week-old, single-maintainer pre-1.0 project whose tooling carries a custom non-open-source license. |

## What belongs here

General-purpose runtimes (Deno, Bun), compilers that turn a program into a standalone native binary or WASI module (scriptc, NetWasm), and app runtimes that package a web frontend as a desktop/mobile app (Tauri). Not framework-specific scaffolding or devtools (see `tanstack-tooling`), not editors (see `code-editors`).
