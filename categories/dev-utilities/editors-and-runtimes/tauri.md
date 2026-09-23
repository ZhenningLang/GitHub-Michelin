---
name: Tauri
slug: tauri
repo: https://github.com/tauri-apps/tauri
category: editors-and-runtimes
tags: [desktop-app, mobile-app, webview, rust, cross-platform]
language: Rust
license: Apache-2.0
maturity: v2.x, stable, 108.5k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-06T09:02:49Z
  default_branch: dev
  default_branch_sha: 19027b19f8bd846fc975c38212f364b6f4a9eb86
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:10:53Z
  overall: A
  overall_score: 3.83
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
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 5.1
        qualifying_issues: 39
        band: relaxed_solo
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: crates.io
        canonical_package: tauri-utils
        dependent_repos_count: 4482
        downloads_last_month: 31950151
        graph_tier: B
        volume_tier: A
        cross_check_divergence: 2.62
        release_downloads: 162908
        release_assets: 165
        release_tier: C
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 2628
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 16
        top1_share: 0.479
        top3_share: 0.846
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Tauri

Build smaller, faster, and more secure desktop and mobile applications with a web frontend. A Rust-powered alternative to Electron that uses the OS native webview instead of bundling Chromium.

![Tauri — health radar](../../../assets/health/tauri.svg)

## When to use

You're choosing a cross-platform desktop or mobile framework and bundle size, memory footprint, and developer skill reuse matter. You pick Tauri over Electron because you do not want to ship a full Chromium copy to every user, and your users care about installer size and RAM usage. You pick Tauri over Flutter because your team already knows HTML, CSS, and JavaScript/TypeScript, and you do not want to invest in learning Dart and a new widget system. You wrap your web frontend in a tiny Rust binary that communicates with the OS via a secure API bridge, producing installers for Windows, macOS, Linux, Android, and iOS from a single codebase. You get built-in auto-updaters, system tray support, and native notifications while your users get native-feeling apps with minimal disk and RAM usage.

## When NOT to use

- If you need deeply native widgets (e.g., complex macOS-specific toolbars or Windows UWP integrations), use AppKit or WPF instead of Tauri, because Tauri's webview-based UI will feel like a web app, not a native one.
- If you cannot tolerate OS webview inconsistencies across platforms (WebView2 on Windows, WKWebView on macOS/iOS, WebKitGTK on Linux), use Electron instead of Tauri, because Electron bundles a controlled Chromium version that behaves identically everywhere.
- If your team refuses to install or maintain Rust tooling, use Electron instead of Tauri, because the backend and build system require Rust.
- If your app needs heavy server-side logic co-located with the client, use a backend framework (e.g., FastAPI or Express) alongside your client instead of Tauri, because Tauri is a client-side framework, not a server.
- If you depend on Electron-specific native modules or deep V8/Chromium APIs, use Electron instead of Tauri, because migration to Tauri's webview model is non-trivial.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| Electron | 未收录 | The incumbent desktop web framework. | Electron bundles Chromium, resulting in large binaries and high memory use; Tauri uses the OS webview and is far lighter. |
| Flutter | 未收录 | Google's cross-platform UI framework with native rendering. | Flutter requires learning Dart and its widget system; Tauri reuses web skills but is less native-feeling on desktop. |
| [Clash Verge Rev](../ops-infra/clash-verge-rev.md) | ✅ | A Tauri-based GUI proxy client. | Demonstrates production Tauri usage but is a specific app, not a framework choice. |
| Neutralinojs | 未收录 | Lightweight alternative to Electron with smaller footprint. | Smaller than Electron but less mature ecosystem and fewer platform features than Tauri. |
| WPF / Cocoa / GTK | 未收录 | Platform-native UI toolkits. | True native widgets and performance, but each platform requires separate codebases and expertise. |

## Tech stack

- **Rust** — core framework, binary bundling, and OS API bridge
- **JavaScript / TypeScript** — frontend UI (use any web framework: React, Vue, Svelte, vanilla)
- **WebView** — OS-native webview engine (WKWebView, WebView2, WebKitGTK, Android System WebView)
- **WRY** — Tauri's unified Rust webview layer
- **TAO** — Cross-platform window handling library

## Dependencies

- Rust toolchain (rustc, cargo) for building
- A supported OS webview runtime (usually pre-installed on modern OS versions)
- Node.js / npm (for frontend build tooling, though not for the runtime)
- For mobile: Android SDK / Xcode for building Android/iOS apps

## Ops difficulty

**Low**. Tauri is a build-time framework; the resulting app is a self-contained binary that end users install via standard package installers. Developers need to maintain the Rust toolchain and handle platform-specific build steps for mobile targets. The built-in updater and CI GitHub Action streamline distribution. No ongoing server infrastructure is required for the app itself.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 5.0 hours across 35 qualifying issues.
- **Maintenance**: Very active — pushed daily as of 2026-07, with v2 stable and active community support (1,442 open issues). [推断]
- **Governance**: Owned by the `tauri-apps` organization with a dedicated core team and open governance model. Bus factor is reasonable.
- **Backing**: Backed by the Tauri Collective and Open Collective funding; has corporate sponsors and a non-profit foundation structure. [未验证]
- **Adoption**: Strong adoption with 108.5k stars and many production apps (e.g., [Clash Verge Rev](../ops-infra/clash-verge-rev.md)). Created in 2019, giving it a 7-year track record with steady growth.
- **Risk flags**: No major relicense history. Dual-licensed MIT/Apache-2.0 is permissive. The v1→v2 migration required code changes, so future major versions may also introduce breaking changes. [推断]

## Caveats (unverified)

- [未验证] The exact governance model and foundation details beyond the Open Collective page have not been verified.
- [推断] Mobile support (iOS/Android) is newer in Tauri v2 and may have more edge cases than the mature desktop targets.
- [未验证] Specific production app download counts and enterprise adoption data are not verified.
