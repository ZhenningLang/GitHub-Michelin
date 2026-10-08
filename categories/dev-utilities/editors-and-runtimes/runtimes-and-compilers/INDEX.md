# runtimes-and-compilers

> Category node. Where your code runs and what it ships as — JS/TS runtimes, ahead-of-time compilers to native or WASI, and web-frontend desktop app shells.
> ← back to [editors-and-runtimes](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Deno** | Use it when starting a new TypeScript backend, CLI or script where deny-by-default file, network and env access plus built-in fmt, lint and test matter more than running an existing Node codebase unchanged — but large Node migrations and native addons fit poorly. | A (6/6) | [→](deno.md) |
| **Bun** | Use it when a Node.js TypeScript project wants one fast binary to run .ts files, install packages, bundle and test — but Node API coverage is incomplete, v1.4 just rewrote the codebase from Zig to Rust, and there is no permission sandbox. | A (5/6) | [→](bun.md) |
| **Tauri** | Use it when a web-frontend desktop app must ship a small installer and low memory instead of bundling Chromium like Electron — but rendering differs across OS webviews, Linux needs webkit2gtk 4.1, and native logic must be written in Rust. | A (6/6) | [→](tauri.md) |
| **scriptc** | Use it when a well-typed TypeScript CLI or small server must ship as a small, fast-starting native binary or WASI module — but it's a 2-month-old Vercel Labs experiment that rejects what it can't compile statically. | C (6/6) | [→](scriptc.md) |
| **NetWasm** | Use it when a C# program must ship as one tiny standalone WASI component — GC linked in, no .NET runtime on the target — but it's a 7-week-old, single-maintainer pre-1.0 project whose tooling carries a custom non-open-source license. | C (4/6) | [→](netwasm.md) |
| **Effect** | Use it when a long-lived TypeScript service keeps failing in ways its types never mentioned and you want errors, dependencies and cancellation checked by `tsc` on one zero-dependency runtime — but the model is viral, 4.0 is a week old, and the HTTP/SQL/RPC/workflow modules are still marked unstable. | A (6/6) | [→](effect.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Deno](deno.md) | ✅ | A (6/6) | A sandboxed runtime and complete toolchain in one binary, at the cost of new conventions (permission flags, deno.json, JSR) and only partial compatibility with Node's node_modules layout. |
| [Bun](bun.md) | ✅ | A (5/6) | Fewer tools and shorter waits with the same package.json, at the cost of runtime compatibility gaps and a company-owned roadmap (Oven, now part of Anthropic). |
| [Tauri](tauri.md) | ✅ | A (6/6) | Small binaries and a capability-based permission model, at the cost of per-platform rendering differences and a Rust toolchain the team must adopt. |
| [scriptc](scriptc.md) | ✅ | C (6/6) | Use it when a well-typed TypeScript CLI or small server must ship as a small, fast-starting native binary or WASI module — but it's a 2-month-old Vercel Labs experiment that rejects what it can't compile statically. |
| [NetWasm](netwasm.md) | ✅ | C (4/6) | Use it when a C# program must ship as one tiny standalone WASI component — GC linked in, no .NET runtime on the target — but it's a 7-week-old, single-maintainer pre-1.0 project whose tooling carries a custom non-open-source license. |
| [Effect](effect.md) | ✅ | A (6/6) | Use it when a long-lived TypeScript service keeps failing in ways its types never mentioned and you want errors, dependencies and cancellation checked by `tsc` on one zero-dependency runtime — but the model is viral, 4.0 is a week old, and the HTTP/SQL/RPC/workflow modules are still marked unstable. |

## What belongs here

General-purpose runtimes (Deno, Bun), compilers that turn a program into a standalone native binary or WASI module (scriptc, NetWasm), and app runtimes that package a web frontend as a desktop/mobile app (Tauri). Also in-language runtime libraries that replace the platform's own async and error model for a whole application (Effect). Not framework-specific scaffolding or devtools (see `tanstack-tooling`), not editors (see `code-editors`).
