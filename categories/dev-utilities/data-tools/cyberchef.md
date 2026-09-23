---
name: CyberChef
slug: cyberchef
repo: https://github.com/gchq/CyberChef
category: data-tools
tags: [encoding, encryption, hashing, compression, data-analysis, forensics, web-app, offline, self-hostable, node-library]
language: JavaScript
license: Apache-2.0
maturity: v11.2.0, active (2026-06)
last_verified: 2026-06-26
type: app
upstream:
  pushed_at: 2026-06-26T12:15:28Z
  default_branch: master
  default_branch_sha: 275b594f7c8b0e39880f55e7c1f67dc0a4e73f92
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:09:02Z
  overall: A
  overall_score: 3.67
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 11
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 52.7
        qualifying_issues: 36
        band: relaxed_solo
        window_offset_days: 3
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: npmjs.org
        canonical_package: cyberchef
        dependent_repos_count: 12
        downloads_last_month: 6814
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
        release_downloads: 650622
        release_assets: 99
        release_tier: C
        signal_basis: releases
        tier_source: releases
    longevity:
      grade: A
      raw:
        repo_age_days: 3585
        last_commit_age_days: 1
        cohort: app
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 23
        top1_share: 0.364
        top3_share: 0.647
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

# CyberChef

A fully client-side "Cyber Swiss Army Knife" web app that chains 300+ encode/decode, crypto, compression, hashing and data-analysis operations into reusable visual "recipes" — runnable offline in the browser or as a Node library.

![cyberchef — health radar](../../../assets/health/cyberchef.svg)

## When to use

You're a security analyst, CTF player, or backend engineer staring at a blob of data you don't recognize — maybe a doubly-URL-encoded then Base64'd token, a gzipped payload inside a hex dump, or a timestamp in some format you can't place. Writing a throwaway script for each transform is slow, and pasting sensitive data into a random online decoder is a non-starter. You open CyberChef (the public instance, or a copy you self-host), drag operations into a recipe — `From Base64` → `URL Decode` → `Gunzip` — and watch the output update live at each step. The "Magic" operation can even guess the chain for you when you have no idea what you're looking at. Because everything runs in your browser and nothing is sent to a server, you can safely throw real incident data, keys, or PCAP-extracted strings at it.

You also reach for it when you want that same logic *repeatable*. A recipe serialises into the URL, so you can bookmark or share a deep link that reproduces an exact transform pipeline, drop file inputs up to ~2 GB, set breakpoints to inspect intermediate stages, and — when you've nailed the recipe interactively — call the very same operations programmatically from Node via the `cyberchef` npm package to bake it into a script or pipeline.

## When NOT to use

- **Bulk / high-throughput batch processing.** It's a browser app; for streaming gigabytes through a transform in a server pipeline, a purpose-built CLI or library (`xxd`, `openssl`, `zstd`, a Python script) is faster and scriptable without the SPA overhead. The Node API helps but is still a general-purpose toolbox, not an optimised data-plane.
- **Production cryptography you must trust end-to-end.** CyberChef is for analysis, prototyping and learning — not a vetted crypto library for shipping. Use audited primitives (libsodium, the platform's crypto stdlib) in production code.
- **Strict-egress / air-gapped policy without self-hosting.** The public gchq.github.io instance is convenient but still a third-party site; if policy forbids that, you must self-host the static build (which is fully offline-capable once served).
- **You need a native desktop tool palette.** If you want a local, install-and-go GUI of inspectors/converters rather than a recipe-chaining canvas, a desktop devtools app fits better — see DevToys below.
- **Very large binary forensics / memory analysis.** The ~2 GB input ceiling and in-browser memory model make it unsuitable for full disk images or memory dumps; reach for dedicated forensics suites.
- **Custom operation lock-in.** Adding your own operation means writing it into CyberChef's module/operation framework and rebuilding the bundle; it's not a generic plugin you drop in at runtime.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [DevToys](devtoys.md) | ✅ | Choose DevToys when you need a native cross-platform desktop devtools palette for formatters, converters, and generators. | Native cross-platform desktop devtools palette (formatters, converters, generators); a fixed tool list rather than CyberChef's chainable recipe pipeline + "Magic" auto-detection. |
| [Cockpit](../ops-infra/cockpit.md) | ✅ | Choose Cockpit when you need a web UI for *server administration*, not data transformation. | Web UI for *server administration*, not data transformation — different problem entirely; listed only to disambiguate "web tool" overlap. |
| CyberChef-server | 未收录 | Choose CyberChef-server when you need the official Node wrapper exposing CyberChef recipes over HTTP. | Official Node wrapper exposing CyberChef recipes over HTTP for batch/automation; complements rather than replaces the app. |
| Custom scripts (`openssl`/`xxd`/Python) | 未收录 | Choose custom scripts when you need maximum control, scriptability, and no UI. | Maximum control, scriptable, no UI; but you rewrite per-task and lose the live visual recipe + Magic detection. |
| dCode / online decoders | 未收录 | Choose dCode or online decoders when browser convenience for one-off transforms outweighs offline privacy. | Browser convenience for single transforms; data leaves your machine and no offline/self-host story — the privacy gap CyberChef closes. |

## Tech stack

- **Language:** JavaScript (browser + Node). Webpack 5 bundles a single-page app; Babel (`@babel/preset-env`) transpiles; Grunt orchestrates the build.
- **Crypto/encoding deps:** `crypto-js`, `@noble/hashes`, `node-forge`, `jsrsasign`, `bcryptjs`, `argon2-browser` for the hashing/encryption operations.
- **Data/analysis deps:** `lodash`, `bignumber.js`, `protobufjs`, `cbor`, `bson`, `json5`; `d3`, `jimp`, `tesseract.js` (OCR), `highlight.js` for visualisation.
- **Compression:** `lz-string`, `lz4js`, `browserify-zlib`.
- **Dual distribution:** static web bundle (the SPA) **and** an npm library with ESM + CommonJS entry points (Node wrapper) — same operation set, two delivery modes.

## Dependencies

- **To use the public app:** just a modern browser (README states Chrome 50+ / Firefox 38+). No backend — all processing is client-side.
- **To self-host:** serve the prebuilt static files behind any web server, or run the official Docker image `ghcr.io/gchq/cyberchef:latest`. No database, no server-side runtime required at request time.
- **To build from source / use the Node library:** Node.js v24 (package declares `engines: ">=24 <25"`), then `npm install` and `npx grunt prod` (build) or `npm install cyberchef` to consume the library.

## Ops difficulty

**Low.** As a static single-page app there is nothing stateful to operate: the easiest self-host is dropping the built `assets`/`index.html` on any static host or CDN, or running the published Docker image. There is no database, queue, or background worker, and no inbound data handling to secure server-side because processing is in the client. The only real cost is rebuilding/upgrading the bundle on a new release and the strict Node v24 build requirement, which can bite CI pinned to other Node majors. Running the Node library inside your own service inherits that service's ops profile rather than adding its own.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 52.7 hours across 36 qualifying issues/PRs.
- **Maintenance (2026-06):** **active** — semver-tagged releases (latest v11.2.0, ~2026-06-17), last pushed 2026-06. A mature major-version line with ongoing releases, not coasting. [推断]
- **Governance & bus factor:** `Organization`-owned by **GCHQ** (the UK signals-intelligence agency) — institutional backing rather than a solo maintainer, with a contributor community around it. Unusual but durable sponsor; low bus-factor risk. [推断]
- **Age & Lindy (~10yr, created 2016-11):** **old and still active** — a strong Lindy verdict. A decade of continuous releases plus government backing makes it a safe long-term bet for an analysis tool.
- **Adoption/ecosystem:** de-facto standard "cyber swiss army knife" in security/CTF/forensics circles, dual-distributed (hosted SPA + `cyberchef` npm library) with an official server wrapper; broad real-world use. [推断]
- **Risk flags:** none structural (Apache-2.0, no relicense/open-core history). Practical gates are scope, not viability: not vetted production crypto, and a strict Node v24 build pin can bite CI. [推断]

## Caveats (unverified)

- [未验证] "300+ operations" is the project's commonly-cited framing; the exact operation count shifts release-to-release — verify against the current build before relying on a specific operation existing.
- [未验证] Reported v11.2.0 published 2026-06-17; star count ~35.2k as of 2026-06 — GitHub stars are unreliable and date-sensitive, treat as indicative only.
- [未验证] README states browser support as Chrome 50+ / Firefox 38+ and a ~2 GB file-input ceiling; actual behaviour at the limit depends on the host browser's memory and version.
- [推断] The npm library exposing the operation set as a Node API is real (package `main` points at a Node wrapper), but the npm package's published version may lag the GitHub tag — confirm before pinning.
- [推断] Self-hosted instances are "fully offline-capable once served" based on the client-side-only design; verify your specific build has no CDN/runtime fetches before treating it as air-gapped-safe.
