---
name: dnspython
slug: dnspython
repo: https://github.com/rthalley/dnspython
category: networking
tags: [dns, python, resolver, dnssec, doh, doq, asyncio, networking]
language: Python
license: ISC
maturity: v2.8.0 (2025-09), active, ~2.7k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-28T01:01:37Z
  default_branch: main
  default_branch_sha: fa5e8ccc1df870b70ec514865f9d5e703917a234
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:43:29Z
  overall: A
  overall_score: 3.6
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
        last_commit_age_days: 3
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 47.9
        qualifying_issues: 18
        band: default
        window_offset_days: 0
        source: pr
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: dnspython
        dependent_repos_count: 46555
        downloads_last_month: 214730536
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.0
        release_downloads: 2539
        release_assets: 12
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 5508
        last_commit_age_days: 3
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 19
        top1_share: 0.747
        top3_share: 0.808
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# dnspython

A powerful, pure-Python DNS toolkit — both high-level resolution (`dns.resolver`) and low-level message/record manipulation (queries, zone transfers, dynamic updates, TSIG, DNSSEC, and modern transports: UDP/TCP, DoH, DoT, DoQ).

![dnspython — health radar](../../assets/health/dnspython.svg)

## When to use

You're building a Python service — a mail server's SPF/MX checker, a security tool that enumerates DNS records, a health-checker that must resolve a name a *specific* way — and the standard library's `socket.getaddrinfo()` is too blunt. It only does A/AAAA via the OS resolver; it can't query arbitrary record types, talk to a specific nameserver, do a zone transfer (AXFR), validate DNSSEC, or send a query over DNS-over-HTTPS. You `pip install dnspython`, then `dns.resolver.resolve('example.com', 'MX')` gives you structured `MX` records; `dns.query.https(...)` sends the query encrypted to a DoH endpoint; `dns.zone.from_xfr(dns.query.xfr(...))` pulls a whole zone. Records are real typed objects, not strings to re-parse. When you need to *construct* DNS — dynamic DNS updates with `dns.update`, TSIG-signed messages, or crafting raw wire-format packets — it gives you the full message model that the stdlib never exposes.

It's also the substrate under much of the Python networking/security ecosystem: when a tool needs to "do DNS properly" rather than shell out to `dig`, it almost always reaches for dnspython. Use it directly when you need typed records, non-default resolvers, modern encrypted transports, or zone/DNSSEC operations from Python.

## When NOT to use

- **You only need a basic forward lookup.** For "give me the IP of this host," `socket.getaddrinfo()` / `socket.gethostbyname()` is simpler, uses the OS resolver (and `/etc/hosts`), and adds no dependency — the dnspython docs themselves say so.
- **You rely on `/etc/hosts` or OS resolver behavior.** dnspython talks DNS directly and **does not consult `/etc/hosts`** or your OS resolver config the way the system resolver does; results can legitimately differ from `ping`/`getent`. [未验证]
- **You're not on Python 3.10+.** Recent versions require **Python 3.10 or later** (Python 2 support ended at 1.16.0); on older interpreters you're stuck on old releases. [未验证]
- **You want a command-line DNS tool.** It's a *library*, not a CLI — for interactive lookups `dig`/`drill`/`kdig` are the right tools; dnspython is for code.
- **You expect DNSSEC/DoH/DoQ with zero extra deps.** The core is pure-Python, but DNSSEC needs `cryptography`, DoH needs `httpx`, IDNA needs `idna`, DoQ is experimental — install the right extras and treat DoQ as not-yet-stable.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| `socket.getaddrinfo` (stdlib) | 未收录 | Choose `socket.getaddrinfo` when zero dependencies and OS resolver behavior matter more than DNS protocol control. | Uses `/etc/hosts` and system config, but only covers basic forward host-to-address lookups. |
| `dig` / `drill` / `kdig` (CLI) | 未收录 | Choose CLI tools when the job is interactive DNS debugging from a shell, not in-process Python logic. | Full-featured for humans, but a subprocess to parse rather than a typed Python API. |
| aiodns / pycares | 未收录 | Choose aiodns or pycares when async lookup speed is enough and you do not need dnspython's full record/message model. | Thin C-Ares lookup layer, not a zone/DNSSEC/custom-message toolkit. |
| `getdns` Python bindings | 未收录 | Choose getdns bindings when stub-resolver and DNSSEC features from the getdns C library justify a native dependency. | Smaller Python ecosystem than dnspython and more native-library coupling. |

## Tech stack

- **Language:** pure Python core (the typed record/message model, resolver, transports are Python).
- **Transports:** UDP, TCP, DNS-over-TLS (DoT), DNS-over-HTTPS (DoH, via httpx), and experimental DNS-over-QUIC (DoQ).
- **Async:** supports both **asyncio** (stdlib) and **Trio** (optional extra) alongside the synchronous API.
- **Crypto/DNSSEC:** DNSSEC validation/signing via the **`cryptography`** package when installed.

## Dependencies

- **Runtime:** Python **3.10+**; the core needs no third-party packages. Optional extras pull in: `cryptography` (DNSSEC), `httpx` (DoH), `idna` (IDNA), `trio` (Trio async), `aioquic` (DoQ), `wmi` (Windows resolver config). [推断]
- **External services:** none of its own — it talks to whatever DNS servers/resolvers you target.
- **Install:** `pip install dnspython` (or `dnspython[dnssec,doh,...]` for extras).

## Ops difficulty

**Low (as a library).** Nothing to deploy — `pip install` and import. The operational nuance is in *correct usage*: choosing the right transport (and installing its extra), setting timeouts/retries on flaky networks, deciding whether to honor the system resolver vs query a fixed server, and remembering it bypasses `/etc/hosts` (so test environments that rely on hosts-file overrides won't behave as with the OS resolver). DNSSEC and DoQ paths carry extra dependency/maturity considerations. For typical resolution it's effectively zero-ops; the care is in DNS semantics, not deployment.

## Health & viability

- **Responsiveness**: Grade B — median first-response time 76.1 hours across 3 qualifying issues/PRs.
- **Maintenance (2026-06).** Repo last pushed 2026-06; latest release **v2.8.0 (2025-09)**, with 2.7.0 (2024-10) and 2.6.1 (2024-02) before it — a steady annual-ish release cadence, **actively maintained**, not archived. Notably **only ~4 open issues**, signaling tight triage. [未验证]
- **Governance / bus factor.** Owner type is **User** (Bob Halley / rthalley, ~1,850 commits) with a meaningful second contributor (bwelling, ~200) and dependabot — a **single-primary-maintainer** project, so bus factor is the main governance caveat despite long, careful upkeep. [推断]
- **Age & Lindy verdict.** Created **2011**, ~15 years old and **still actively releasing** ⇒ a **strong Lindy** signal: it is the de-facto Python DNS library, depended on across the security/networking ecosystem. [推断]
- **Adoption.** ~2.7k stars and very heavy transitive use (mail, security, infra tools that "do DNS properly" use it); excellent docs at dnspython.org. [未验证]
- **Risk flags.** **ISC** license (confirmed by reading the LICENSE file — GitHub's API reported `NOASSERTION`); ISC is a permissive, MIT-equivalent license, no relicense history found. The single-maintainer concentration is the standing risk. [未验证]

## Caveats (unverified)

- [未验证] License is **ISC** per the repo's LICENSE file; GitHub's API returned `NOASSERTION` (it didn't auto-classify it) — confirmed by reading the file, but re-verify if it matters legally.
- [未验证] ~2.7k stars / ~561 forks / ~4 open issues as of 2026-06 — date-sensitive, indicative only.
- [未验证] "Python 3.10+ required" reflects recent releases; the exact minimum for the version you pin should be checked against its metadata.
- [推断] The optional-extras mapping (cryptography/httpx/idna/trio/aioquic/wmi) is from the docs; exact extra names/requirements can shift between releases.
- [推断] DoQ (DNS-over-QUIC) is documented as experimental — treat its stability/API as not guaranteed.
