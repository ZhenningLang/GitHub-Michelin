---
name: Deno
slug: deno
repo: https://github.com/denoland/deno
category: editors-and-runtimes
tags: [javascript, typescript, runtime, secure-by-default, webassembly]
language: Rust
license: MIT
maturity: v2.x, stable, 107.3k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-06T09:16:36Z
  default_branch: main
  default_branch_sha: 34e593a462d1bb1b6e525ae8ee1534738b9a4b2e
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:10:42Z
  overall: A
  overall_score: 4.0
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 16.5
        qualifying_issues: 18
        band: relaxed_solo
        window_offset_days: 1
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: crates.io
        canonical_package: deno_core
        dependent_repos_count: 396
        downloads_last_month: 7904610
        graph_tier: C
        volume_tier: A
        cross_check_divergence: 4.85
        homebrew_installs_90d: 155642
        homebrew_tier: A
        release_downloads: 35229439
        release_assets: 2628
        release_tier: A
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 3053
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 93
        top1_share: 0.354
        top3_share: 0.609
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Deno

A modern runtime for JavaScript, TypeScript, and WebAssembly with secure defaults and a great developer experience. Built on V8, Rust, and Tokio.

![Deno — health radar](../../../assets/health/deno.svg)

## When to use

You're choosing a JavaScript/TypeScript runtime for a new server-side project or CLI tool and you want a modern, secure toolchain. You pick Deno over Node.js because you're tired of `node_modules` bloat, `package.json` dependency hell, and the need for external tooling (ts-node, nodemon, eslint, prettier). You want a runtime that treats TypeScript as a first-class citizen, has built-in formatting, linting, and testing, and enforces security permissions by default. You pick Deno over Bun because Deno has a standard OSI license (MIT), a longer track record (8 years vs 5 years), and stronger WebAssembly integration. You install Deno with a single shell command, write `.ts` files that run directly, and ship a compiled standalone binary when you're ready. Deno's standard library and npm compatibility mean you can bring your existing packages along while enjoying a modern toolchain.

## When NOT to use

- If you have an existing Node.js monolith with native Node.js addons, C++ bindings, or deep `node-gyp` dependencies, use Node.js instead of Deno, because complex projects with native modules are unlikely to migrate smoothly.
- If you rely on npm packages that depend on Node.js-specific APIs or post-install scripts, use Node.js instead of Deno, because some packages may not work under Deno's npm compatibility layer.
- If your entire team knows Node.js and no one has Deno experience, and the project is short-term, use Node.js instead of Deno, because the productivity hit during onboarding may outweigh the benefits.
- If you need to optimize at the V8 level, stay on Node.js instead of Deno, because both use the same V8 engine and CPU-bound performance is identical.
- If you want fully portable serverless code without proprietary edge runtime lock-in, use Node.js or Cloudflare Workers instead of Deno, because Deno Deploy is a proprietary service.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| Node.js | 未收录 | The incumbent JS/TS runtime with the largest ecosystem. | Node.js has the deepest npm ecosystem and broadest hosting support; Deno offers a cleaner, more secure developer experience but a smaller community. |
| [Bun](bun.md) | ✅ | Fast all-in-one JS runtime with bundler and package manager built in. | Bun is faster and also treats TypeScript as first-class, but it is younger and less proven than Deno. |
| [Supabase](../../databases/database-engines/supabase.md) | ✅ | Uses Deno for edge functions. | Not a runtime comparison per se, but demonstrates Deno's production use in serverless edge contexts. |
| Wasmer / Wasmtime | 未收录 | Pure WebAssembly runtimes. | These are for Wasm modules, not JS/TS applications; Deno can run Wasm but is primarily a JS runtime. |

## Tech stack

- **Rust** — core runtime, HTTP server, and sandboxing layer
- **V8** — JavaScript engine (same as Node.js and Chrome)
- **Tokio** — async runtime for Rust, powering Deno's I/O
- **TypeScript** — first-class language support (transpiled internally)
- **WebAssembly** — supports running Wasm modules alongside JS/TS

## Dependencies

- Deno binary (single executable, no external runtime needed)
- For compilation: a C++ linker if producing standalone binaries (Deno uses `deno compile`)
- Optional: npm packages via `npm:` specifiers or JSR (JavaScript Registry) packages
- No `node_modules` or `package.json` required for Deno-native projects

## Ops difficulty

**Low**. Deno is a single binary that runs on major OSs. For deployment, you can run `deno run` directly, compile to a standalone binary with `deno compile`, or deploy to Deno Deploy (managed edge). The built-in toolchain (test, fmt, lint, bench) reduces the need for separate devDependencies. No `node_modules` bloat simplifies CI/CD caching and Docker image sizes.

## Health & viability
- **Maintenance**: Grade A — 13/13 active weeks in trailing 13; last commit 1 days ago.
- **Responsiveness**: Grade A — median first-response time 16.5 hours across 18 qualifying issues/PRs.
- **Adoption**: Grade A — 7,904,610 monthly downloads via crates.io (package: deno_core).
- **Longevity**: Grade A — 3053 days old.
- **Governance**: Grade A — top-3 contributor share 60.9% (?).
- **Risk / License**: Grade A — MIT license.
## Caveats (unverified)

- [未验证] Deno Land Inc. has raised venture funding; the exact funding rounds and investors have not been verified from primary sources.
- [推断] Deno Deploy's proprietary edge runtime may create incentives to prioritize Deno-specific APIs over standard web compatibility in the future.
- [未验证] The exact number of production deployments and enterprise users beyond Supabase has not been verified.
