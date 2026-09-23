---
name: OpenZL
slug: openzl
repo: https://github.com/facebook/openzl
category: data-tools
tags: [compression, structured-data, codec, columnar, zstd, meta]
language: C
license: BSD-3-Clause
maturity: v0.2.0, active, pre-1.0 (2026-05); format/API still changing
last_verified: 2026-06-26
type: library
upstream:
  pushed_at: 2026-06-26T17:29:05Z
  default_branch: dev
  default_branch_sha: a4d56c1af24b07799d76f0b390201545b33c2157
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:10:02Z
  overall: C
  overall_score: 2.2
  scored_axes: 5
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
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: D
      raw:
        median_ttfr_hours: 749.9
        qualifying_issues: 6
        band: default
        window_offset_days: 0
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 665
        release_assets: 4
        release_tier: D
        signal_basis: releases
    longevity:
      grade: D
      raw:
        repo_age_days: 357
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 34
        top1_share: 0.278
        top3_share: 0.595
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# OpenZL

A format-aware compression framework from Meta: you describe the shape of your structured data and it builds a specialized compressor whose output a single universal decompressor can always read.

![openzl — health radar](../../../assets/health/openzl.svg)

## When to use

You're a data-platform or storage engineer sitting on terabytes of one specific, highly structured payload — fixed-schema telemetry records, columnar feature dumps for an AI training pipeline, arrays of sorted integers, multi-field binary logs. A generic byte-stream compressor (zstd, lz4) treats the whole blob as an opaque sequence and leaves a lot of ratio on the table because it never sees that column 3 is a monotonic timestamp and column 7 is a low-cardinality enum. You've tried hand-rolling a transpose-then-delta-then-zstd pipeline and it works, but it's bespoke per dataset and a pain to maintain. OpenZL lets you instead *describe* the data — via a pre-built profile, the SDDL (Simple Data Description Language), or a custom parser — and it composes primitive codecs into a DAG that splits your records into homogeneous streams (parse → group → transform & compress), applying delta/transpose/dictionary steps where they actually pay off.

The payoff is two-fold: you can get materially better ratio-at-speed than a generic compressor on that specific format, and every frame you produce is readable by OpenZL's single universal decompressor regardless of which graph created it — so consumers don't need to know which specialized compressor was used. Meta states the core has "reached production-readiness" and is "used extensively in production at Meta", which is reassuring if you're considering it for a real ingestion pipeline rather than a one-off.

## When NOT to use

- **Generic / unstructured / text blobs.** OpenZL's leverage comes from format awareness over homogeneous streams (numeric, columnar, tabular). For arbitrary text, source code, mixed web payloads, or "just compress this file", a general-purpose compressor like zstd or brotli is simpler and likely as good — the docs themselves make no generic/text performance claims. [推断]
- **You need format stability TODAY.** The project is explicit: "The API, the compressed format, and the set of codecs and graphs included in OpenZL are all subject to (and will!) change." Only release-tagged commits carry the multi-year decompressibility guarantee; `dev` branch offers "no guarantees whatsoever." Pre-1.0.
- **Small payloads / one-off files.** The describe-the-data + build-a-specialized-compressor workflow has real upfront modeling cost. For a handful of small or heterogeneous files it's overkill versus `zstd -19`.
- **You want a drop-in CLI to replace `gzip`/`zstd`.** This is a framework + library you compose against and a format you adopt, not a transparent stand-in for an existing compressor in your shell pipeline.
- **Non-C/C++ shops wanting zero native build.** It's a C11/C++17 codebase built with CMake/Make; you take on a native toolchain and the maintenance of a format that is still evolving (lock-in to OpenZL's frame format until it stabilizes).
- **Windows-first teams.** Build guidance recommends clang-cl; MSVC "may produce C2099 errors due to limited C11 support."

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [CyberChef](cyberchef.md) | ✅ | Choose CyberChef when analysts need browser-based ad-hoc encode/decode/compress recipes. | Browser-based ad-hoc encode/decode/compress recipes for analysts; interactive and general, not a production library for ratio-tuned structured-data compression. |
| [DevToys](devtoys.md) | ✅ | Choose DevToys when you need a desktop developer-utility hub with built-in one-off compress/format tools. | Desktop developer-utility hub with built-in compress/format tools; convenience for one-off tasks, not a programmable format-aware compressor. |
| zstd | 未收录 | Choose zstd when you need the general-purpose compression baseline. | The general-purpose baseline (also Meta/BSD). Excellent ratio-at-speed on arbitrary bytes; OpenZL targets *beating* it on specific structured formats via format awareness, at the cost of having to describe the data. |
| Parquet + zstd/snappy | 未收录 | Choose Parquet plus zstd/snappy when you need the mainstream columnar-at-rest path. | The mainstream columnar-at-rest path: schema-aware encodings (dictionary/RLE) plus a block codec. Mature and ubiquitous; OpenZL is a lower-level framework letting you build custom codec graphs, not a file format with an ecosystem. |
| BLOSC / blosc2 | 未收录 | Choose BLOSC/blosc2 when you need blocking plus shuffle/bitshuffle meta-compression for numeric arrays. | Blocking + shuffle/bitshuffle meta-compressor aimed at numeric arrays; conceptually similar "transform then compress" idea, narrower scope and more mature than OpenZL. |
| Brotli | 未收录 | Choose Brotli when you need strong general-purpose compression for text/web content. | Strong general-purpose (esp. text/web) compressor; not format-aware for structured numeric data. |

## Tech stack

- **Language:** C (~51%) and C++ (~44.7%) per the repo.
- **Core model:** codecs composed into a directed acyclic graph (DAG); a single universal decompressor that "can decompress anything produced by the compressor, independent of the compression DAG."
- **Data description:** pre-built profiles for known formats, SDDL (Simple Data Description Language), pre-parsed homogeneous streams, or custom parsers.
- **Tooling:** core library plus a CLI (`cli/`), example transforms/parsers, benchmark and test harnesses; Python bindings present (`py/`). [推断] scope of Python bindings unverified beyond directory presence.
- **Build:** CMake (≥ 3.20.2) or Make; requires a C11 + C++17 compiler.

## Dependencies

- **Toolchain:** a compiler supporting C11 and C++17 (GCC/Clang; clang-cl recommended on Windows). CMake ≥ 3.20.2 if using the CMake path.
- **Vendored deps:** the repo carries a `deps/` directory and submodules (`.gitmodules`); the build pulls its own dependencies rather than requiring a heavy external runtime. [推断] exact dependency set not enumerated here.
- **Runtime:** no server/daemon/database — it's an embeddable compression library + CLI, not a service.
- **Install:** build from source (`make`, or `cmake -DCMAKE_BUILD_TYPE=Release ..`); no published package manager artifact verified.

## Ops difficulty

**Low-to-medium as a library; medium as a format commitment.** Operationally there's nothing to run — no service, no DB; you link the library or invoke the CLI. The "low" friction is offset by two real costs: (1) a native C11/C++17 build you must own (CMake/Make, and clang-cl gymnastics on Windows), and (2) the *format-evolution* burden — because the compressed format is still changing pre-1.0, you must pin to release-tagged versions and plan for re-compression / version skew over time, even though release frames stay decompressible "for at least the next several years." The upfront data-modeling effort (writing SDDL / choosing a graph) is a per-dataset design task, not a deploy task.

## Health & viability

- **Responsiveness**: Grade D — median first-response time 749.9 hours across 6 qualifying issues/PRs.
- **Maintenance (2026-06):** **active** — last pushed 2026-06; tagged releases moving (v0.1.0 2025-10 → v0.2.0 2026-05) but explicitly **pre-1.0**, with the format/API/codec set declared as still-changing. [推断]
- **Governance & bus factor:** `Organization`-owned by **Meta** (`facebook`), same house as zstd — strong vendor backing and team governance, low bus-factor risk. Meta states the core "is used extensively in production at Meta," so there's an internal user keeping it alive. [未验证]
- **Age & Lindy (~9mo, created 2025-09):** **young and unproven on Lindy** — too new to bet on durability alone. The mitigant isn't age but the backer's track record (Meta/zstd lineage); still, pre-1.0 means the format itself is a moving target.
- **Risk flags:** **format-evolution lock-in** is the headline risk — only release-tagged frames carry the multi-year decompressibility guarantee; `dev` offers none. Pin to tags and plan for re-compression/version skew. Native C11/C++17 build; weak Windows/MSVC story. [推断]

## Caveats (unverified)

- [未验证] License is BSD; the LICENSE file carries three conditions including the non-endorsement clause, so SPDX `BSD-3-Clause` (Meta's standard license, same family as zstd) — frontmatter reflects this inference, not an SPDX tag declared in-repo (`gh` reports the license as "Other/NOASSERTION").
- [未验证] Latest release v0.2.0 dated 2026-05-07; first public release v0.1.0 on 2025-10-06 (alongside the engineering blog post and whitepaper arXiv:2510.03203). Star count ~3.1k as of 2026-06 — GitHub stars are unreliable and date-sensitive; treat as indicative only.
- [未验证] Language percentages (C ~51% / C++ ~44.7%) are GitHub's linguist estimate and shift over time.
- [推断] "Better ratio than generic compressors on structured data" is the project's framing; no first-party head-to-head benchmark numbers are quoted here — actual gains depend heavily on the dataset and the codec graph you build.
- [推断] Python bindings exist (`py/` directory) but their completeness/stability was not verified.
- [推断] Suitability for text/generic data is judged poor because the docs only demonstrate structured/numeric examples and make no generic-data claims — not an explicit "do not use" statement from the authors.
