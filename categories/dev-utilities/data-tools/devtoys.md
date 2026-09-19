---
name: DevToys
slug: devtoys
repo: https://github.com/DevToys-app/DevToys
category: data-tools
tags: [developer-tools, offline, desktop, cross-platform, converters, encoders, formatters, extensible]
language: C#
license: MIT
maturity: v2.0.9.0 (prerelease, 2026-01), active (2026-06)
last_verified: 2026-06-26
type: app
upstream:
  pushed_at: 2026-02-25T11:53:38Z
  default_branch: main
  default_branch_sha: 7e12df8448aa1f6aec4a8736b3e06a1c90530715
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T14:33:29Z
  overall: B
  overall_score: 2.75
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 128
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: B
      raw:
        repo_age_days: 1739
        last_commit_age_days: 128
        cohort: app
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.75
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    adoption: { reason: no_package_structural }
---

# DevToys

An offline, cross-platform desktop "Swiss Army knife" that bundles ~30 small developer utilities (converters, encoders, formatters, generators, testers) behind one native GUI — plus a separate CLI for automation.

![devtoys — health radar](../../../assets/health/devtoys.svg)

## When to use

You're a developer who, twenty times a day, needs to Base64-decode a token, pretty-print a blob of JSON, diff two strings, generate a UUID, convert JSON↔YAML, or hash a file — and you're tired of pasting potentially-sensitive payloads into random "json formatter online" sites whose ad-funded business model you don't trust. DevToys installs as a normal desktop app (Windows, macOS, or Linux), opens instantly, and runs every transformation locally with no network call, so a JWT or a config secret never leaves your machine. You get one searchable window with ~30 tools instead of thirty browser tabs, and a "Smart Detection" feature that guesses which tool you want from whatever you paste.

It also fits when you want the same conveniences in automation: DevToys ships a separate CLI app that exposes the tools for scripting and CI, and both the GUI and CLI are extensible — you can pull in community tools or write your own as a NuGet-distributed extension. So the personal scratchpad and the pipeline step can share the same tool implementations.

## When NOT to use

- **You live in the terminal and want a single binary, not a desktop app.** DevToys is GUI-first; the CLI is a separate companion. For a pure browser/CLI text-transform pipeline, [CyberChef](cyberchef.md) (browser, chainable "recipes") or plain `jq`/`xxd`/`openssl` are lighter weight.
- **You need to chain transforms into a reproducible recipe.** DevToys tools are mostly one-shot, single-tool screens; CyberChef's whole model is composing many operations into a saved, shareable pipeline. DevToys does not (as of v2) offer an equivalent recipe graph. [推断]
- **You need server/headless infrastructure or remote management.** This is a local devtools box, not a service. For host administration use [Cockpit](../ops-infra/cockpit.md); for metrics collection use [Telegraf](../ops-infra/telegraf.md).
- **You depend on a frozen, long-term-stable release.** The current cross-platform 2.x line is published as **prerelease** builds; the last non-prerelease GitHub release is the older Windows-only 1.0.13.0 (2023). If your org bars prerelease software, that's a real gate. [未验证] release-channel policy may change.
- **You need a tool DevToys doesn't have and can't justify an extension.** The built-in set is fixed (~30); anything beyond means finding or authoring an extension, with the maintenance/trust cost that implies.
- **Browser-embeddable / scriptable-in-JS use.** DevToys is a .NET desktop app; you can't drop it into a web page the way CyberChef (pure client-side JS) embeds.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [CyberChef](cyberchef.md) | ✅ | Choose CyberChef when you need browser-based, chainable "recipe" pipelines and deeper crypto/forensics operations. | Browser-based, chainable "recipe" pipelines and crypto/forensics depth; runs anywhere with a browser. DevToys is a native desktop app with OS integration, a CLI companion, and an offline-by-default install, but mostly one-shot tools (no recipe graph). |
| [Cockpit](../ops-infra/cockpit.md) | ✅ | Choose Cockpit when you need web server-administration UI for Linux hosts. | Web server-administration UI for Linux hosts (services, logs, storage); a different job — remote host management vs local dev string-wrangling. |
| [Telegraf](../ops-infra/telegraf.md) | ✅ | Choose Telegraf when you need a metrics/event collection agent for observability pipelines. | Metrics/event collection agent for observability pipelines; not an interactive devtools box. |
| It-Tools | 未收录 | Choose It-Tools when you need a self-hostable web app with a similar grab-bag of dev utilities. | Self-hostable web app with a very similar grab-bag of dev utilities; runs in any browser / Docker. DevToys is native desktop + offline + a CLI; It-Tools is zero-install over HTTP. |
| DevUtils (macOS) | 未收录 | Choose DevUtils when you need a polished native macOS-only equivalent and accept a paid app. | Polished native macOS-only equivalent (paid); DevToys is free, MIT, and cross-platform. |
| [`jq`](jq.md) / `xxd` / `openssl` (CLI) | 部分已收录 | Choose Unix CLI primitives when you need scriptable pipelines with no GUI. | Scriptable Unix primitives, no GUI; better for pipelines, worse for "I just need to eyeball this once." |

## Tech stack

- **Language:** C# (≈73% of the repo) on .NET; UI assets in HTML/SCSS/TypeScript (Blazor Hybrid front end). PowerShell for build/packaging. (percentages per GitHub language stats, 2026-06)
- **UI:** WinUI on Windows and a cross-platform shell rendering a Blazor Hybrid (WebView) UI on macOS/Linux; Fluent/Mica design language. (exact cross-platform host framework not re-confirmed from source this pass — see Caveats)
- **Form factors:** a GUI app and a separate CLI app, sharing the same tool/extension model.
- **Extensibility:** tools are plugins; community + first-party extensions are distributed as NuGet packages and discovered in-app.

## Dependencies

- **Runtime:** none for the user — DevToys ships as a self-contained desktop install per OS (Windows / macOS / Linux). No database, no server, no internet connection required to run the built-in tools.
- **Install:** OS-native installers / package managers (e.g. Microsoft Store / winget on Windows, and macOS/Linux packages); see the project's releases and site for the current channel (exact package-manager IDs not re-verified this pass — see Caveats).
- **Build-from-source:** .NET SDK toolchain (C#), plus the JS/TS asset pipeline for the Blazor UI.
- **Extensions:** optional; pulled as NuGet packages at the user's discretion.

## Ops difficulty

**Low.** For the end user it is a single desktop install with zero services to run, no config, and no network exposure — essentially "install and use," and uninstall is clean. The only ongoing burden is keeping up with prerelease 2.x builds if you want the cross-platform line, and vetting any third-party extension you add (an extension is arbitrary code from NuGet, so it inherits that trust/maintenance cost). There is no deployment, scaling, or backup story because there is no server.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-06):** **active but in prerelease limbo** — repo pushed 2026-02; the cross-platform 2.x line ships only as **prerelease** builds (latest v2.0.9.0, 2026-01), and the last *stable* GitHub release is the Windows-only 1.0.13.0 (2023). Developing, but with no current stable tag. [未验证]
- **Governance & bus factor:** `Organization`-owned (`DevToys-app`) with ~31k stars — community/org project, no large vendor behind it; a small maintainer team rather than a single person. [推断]
- **Age & Lindy (~5yr, created 2021-09):** **mid-aged and active** — enough history to clear a basic Lindy bar, but the unfinished 2.x stabilization tempers the verdict: proven concept, not-yet-frozen current line.
- **Risk flags:** if your org bars prerelease software, the cross-platform line is a real gate; third-party extensions are arbitrary NuGet code (trust/maintenance cost). MIT, no relicense/open-core history.

## Caveats (unverified)

- [未验证] Latest release is v2.0.9.0 published 2026-01-08 and marked **prerelease**; the most recent non-prerelease GitHub release is v1.0.13.0 (2023-07-25, Windows-only 1.x). Repo `pushedAt` 2026-02-25, so development is ongoing — but "stable 2.0" status should be confirmed before relying on it.
- [未验证] Star count ~31.7k as of 2026-06 — GitHub stars are unreliable and date-sensitive; indicative only.
- [推断] Built-in tool count "~30" comes from the project's own "30 tools" framing for 2.0; the exact catalog shifts release-to-release — verify a specific tool exists in your installed build.
- [推断] Cross-platform UI is described as WinUI (Windows) + a Blazor Hybrid WebView shell elsewhere; the precise cross-platform host framework (Uno Platform vs custom) was not re-confirmed from source this pass.
- [未验证] Installation methods (winget / Store / brew / Linux packages) and the CLI's exact command surface were not exhaustively re-verified; check the official site/releases.
- [推断] CyberChef-style recipe chaining is absent in DevToys based on its single-tool UI model; not exhaustively confirmed against the current feature set.
