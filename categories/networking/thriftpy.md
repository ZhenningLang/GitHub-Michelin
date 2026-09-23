---
name: ThriftPy
slug: thriftpy
repo: https://github.com/Thriftpy/thriftpy
category: networking
tags: [thrift, rpc, serialization, python, deprecated, archived]
language: Python
license: MIT
maturity: v0.3.9 (2016-08), deprecated + archived, ~1.1k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2018-12-09T14:45:17Z
  default_branch: develop
  default_branch_sha: 0e606f82a3c900e663b63d69f68fc304c5d58dee
  archived: true
health:
  schema: 1
  computed_at: 2026-09-22T16:43:50Z
  overall: B
  overall_score: 2.8
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 17
        active_weeks_13: 5
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: thriftpy
        dependent_repos_count: 286
        downloads_last_month: 38919
        graph_tier: C
        volume_tier: C
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4606
        last_commit_age_days: 17
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
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
---

# ThriftPy

A pure-Python implementation of Apache Thrift that loads a `.thrift` file at runtime and generates the RPC client/server code on the fly — **deprecated and archived**, superseded by [thriftpy2](https://github.com/Thriftpy/thriftpy2).

![thriftpy — health radar](../../assets/health/thriftpy.svg)

## When to use

Honestly, you almost never reach for *this* repo new in 2026 — but here's the scenario where its lineage matters. You're a Python backend engineer at a shop that talks Apache Thrift between services, and the official `thrift` Python binding annoys you: it needs a code-generation step (`thrift --gen py`), the generated code is verbose, and building it can drag in a compiler. You want to just point at the `.thrift` IDL and have working client/server objects appear. ThriftPy's pitch was exactly that: `pingpong = thriftpy.load("pingpong.thrift")` and you get the module in-process, no codegen build step, wire-compatible with upstream Thrift servers/clients. You set up a server with `make_server` and a client with `make_client` in a handful of lines.

In practice today, that pitch lives on in **thriftpy2**, the maintained fork. You'd land on *this* page when you inherit a legacy service still importing `thriftpy` (Python 2.7 era), need to understand what it does before migrating, or are choosing the family and need to know that the active member is thriftpy2, not this archived original.

## When NOT to use

- **It is deprecated and the repo is archived.** The README's first line says migrate to thriftpy2; the GitHub repo is archived (read-only, no new commits/issues). Do not start anything new on it. [推断]
- **No releases since 2016, no pushes since 2018.** Last tag `v0.3.9` is 2016-08; last push 2018-12. It predates modern Python — written for Python 2.7 / 3.4+ — and has no fixes for newer interpreters or CVEs. [未验证]
- **You want the maintained version.** Use **thriftpy2** instead — same load-`.thrift`-at-runtime model, still actively pushed (2026-06), supports current Python.
- **You need protocols/transports beyond its set.** It implements binary/compact/JSON protocols and buffered/framed/tornado/http transports as of 2016; anything newer in Apache Thrift won't be here.
- **You depend on the old tornado integration.** Its async server/client are pinned to `tornado>=4.0,<5.0` and `toro` — both long obsolete; this will not coexist with a modern async stack.
- **You need vendor/foundation support.** It is a community project (originally from eleme), now frozen; no support channel.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| thriftpy2 | 未收录 | Choose thriftpy2 when you need the maintained runtime-load-`.thrift` successor and are leaving this archived repo. | Same model with current Python support; the direct migration target. |
| Apache Thrift (official `thrift` Python lib) | 未收录 | Choose official Apache Thrift when canonical multi-language stubs and foundation governance matter more than runtime IDL loading. | Heavier because of code generation, but broadly supported and the reference implementation. |
| gRPC + Protocol Buffers | 未收录 | Choose gRPC and Protocol Buffers for new RPC designs that do not need Thrift wire compatibility. | Larger modern ecosystem over HTTP/2/protobuf, but it is a migration to a different protocol. |
| Apache Avro | 未收录 | Choose Avro when schema-based serialization in data/Hadoop ecosystems is the deciding constraint. | JSON-defined schemas and RPC support, but not wire-compatible with Thrift. |

## Tech stack

- **Language:** pure Python (CPython 2.7 / 3.4+, PyPy per the 2016 README), with **optional Cython** extensions for the binary/compact protocols and buffered transport to speed up the hot path.
- **Parser:** `ply` (Python Lex-Yacc) is the one hard runtime dependency — it parses the `.thrift` IDL at load time.
- **Protocols:** binary (py + cython), compact (py + cython), JSON. **Transports:** buffered (py + cython), framed, tornado, http.
- **Model:** loads the `.thrift` file into a Python module object at runtime (`thriftpy.load`), optionally via an import hook, instead of an offline codegen step.

## Dependencies

- **Runtime:** `ply>=3.4,<4.0` (required). That's the only mandatory dependency.
- **Optional:** `tornado>=4.0,<5.0` + `toro>=0.6` for the async tornado server/client; `cython>=0.23` at build time to compile the native protocol/transport extensions (falls back to pure Python on PyPy / non-UNIX / when Cython is absent).
- **External services:** none of its own — it's a client/server RPC library; you supply the services that speak Thrift on the wire.

## Ops difficulty

**Low to operate, but high *risk* because it's frozen.** As a library there's nothing to deploy or run beyond `pip install` and your own service process — no datastore, no daemon. The operational burden is entirely the staleness: it targets Python 2.7/3.4 and pins obsolete tornado; on a modern interpreter you may hit incompatibilities, and there will be no upstream fix because the repo is archived. The realistic "ops" task here is **migration to thriftpy2**, not running this. [推断]

## Health & viability

- **Maintenance**: Grade B — 1/13 active weeks in trailing 13; last commit 1 day ago.
- **Responsiveness**: Cannot be scored — no_traffic.
- **Adoption**: Grade C — 19,000 monthly downloads via pypi.org (package: thriftpy).
- **Longevity**: Grade A — 4525 days old.
- **Governance**: Grade D — top-3 contributor share 1.0 (100.0%) (?).
- **Risk / License**: Grade A — MIT license.

## Caveats (unverified)

- [未验证] ~1,148 stars / 281 forks / 72 open issues as of 2026-06 from the GitHub API — star/issue counts are date-sensitive and indicative only; an archived repo's open-issue count is effectively frozen.
- [未验证] Python version support (2.7 / 3.4+ / PyPy) and the exact protocol/transport list are taken from the 2016-era README and `setup.py`; behavior on current Python 3.12+ is not verified and likely degraded.
- [未验证] thriftpy2 facts (active in 2026, ~587 stars) are from the GitHub API snapshot and assumed to be the maintained successor based on the README's migration link; feature parity vs this repo was not exhaustively diffed.
- [推断] "Frozen / will not be fixed" is inferred from the `archived` flag plus deprecation notice, not from a maintainer statement enumerating dropped support.
- [推断] The optional-Cython build fallback behavior is read from `setup.py` logic (UNIX + CPython only), not run/verified here.
