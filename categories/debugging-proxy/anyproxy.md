---
name: AnyProxy
slug: anyproxy
repo: https://github.com/alibaba/anyproxy
category: debugging-proxy
tags: [proxy, mitm, http, https, nodejs, debugging, traffic-capture]
language: JavaScript
license: Apache-2.0
maturity: v4.x (npm 4.1.3), master frozen since 2020-06, coasting, ~7.9k stars (as of 2026-06)
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2023-03-06T17:20:04Z
  default_branch: master
  default_branch_sha: b93f948107b956e07c7b68faeff0c777a1f50486
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:06:11Z
  overall: C
  overall_score: 1.5
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 2287
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: C
      raw:
        registry: npmjs.org
        canonical_package: anyproxy
        dependent_repos_count: 238
        downloads_last_month: 7372
        graph_tier: C
        volume_tier: D
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: E
      raw:
        repo_age_days: 4425
        last_commit_age_days: 2287
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# AnyProxy

A fully configurable HTTP/HTTPS man-in-the-middle proxy in Node.js: route your machine's (or a mobile device's) traffic through it to inspect it in a web UI, record it, and rewrite requests/responses with JS rule files. Alibaba-backed — but the master branch hasn't moved since mid-2020.

![anyproxy — health radar](../../assets/health/anyproxy.svg)

## When to use

You're a mobile or web engineer debugging an app's network layer, and you need to *see and rewrite* what it sends — inspect live HTTP/HTTPS traffic, mock a slow or broken backend response, or flip a request's path/headers to test an edge case before the server change ships. You point your phone or browser at AnyProxy, trust its generated root CA so it can decrypt HTTPS, and open its web UI (default port 8002) to watch requests stream by — there's even a QR-code helper to point a mobile device at the proxy. To modify traffic you write a small JS rule file with generator/Promise hooks (`*beforeSendRequest`, `*beforeSendResponse`, `*beforeDealHttpsRequest`) that return modified request/response details, and you can throttle bandwidth or record sessions to an embedded datastore. Install is `npm install -g anyproxy`.

It's a reasonable pick when you specifically want a *scriptable* Node.js proxy whose rules are plain JavaScript you already know — versus a GUI tool like Charles. But weigh its staleness first (below).

## When NOT to use

- **Don't pick it for new work in 2026 — master is frozen.** The last real master commit was 2020-06 ("release 4.1.3"); the latest GitHub release tag is only v4.0.5, with no v4.1.3 tag. ~6 years without a code release and 248 open issues. Alibaba backing has not translated into maintenance. [推断]
- **A more actively maintained Node.js alternative exists.** [whistle](whistle.md) is the actively-developed Node.js MITM debugging proxy in this same niche — prefer it for new setups.
- **Expect cert/runtime friction on modern systems.** It targets the Node 6 era (`engines: node >=6.0.0`) and depends on the deprecated `request` library; on Node 18/20+ and on macOS/iOS with stricter cert-trust and TLS validity rules, old MITM-CA proxies commonly break. Treat compatibility on current OS/Node as unverified until you test it. [推断]
- **Not for production traffic.** It's a debugging/MITM tool by design — recording and throttling add overhead, and routing real traffic through a MITM is a security liability.
- **Provenance is murky.** npm publishes 4.1.3 (plus a 4.2.0-beta) while GitHub's newest release is v4.0.5 with no matching tag — the published 4.1.x line was never cut as a GitHub release, which complicates auditing what you're actually installing.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [whistle](whistle.md) | ✅ | Choose whistle when you need the actively maintained Node.js MITM proxy default. | The actively-maintained Node.js MITM debugging proxy; richer rule system and ongoing releases — the better default for new work in this niche. |
| [mitmproxy](mitmproxy.md) | ✅ | Choose mitmproxy when Python scripting plus CLI/TUI/web UI matter more than Node.js rules. | Python, actively maintained, powerful scripting + TUI/web UI; the go-to programmable MITM proxy if you're not tied to Node.js. |
| Charles / Fiddler | 未收录 | Choose Charles or Fiddler when mature desktop GUI debugging is the priority. | Mature commercial/freeware GUI debugging proxies; polished UX but closed-source and not scriptable in JS the way AnyProxy's rule files are. |
| Proxyman | 未收录 | Choose Proxyman when modern macOS/cross-platform GUI polish matters most. | Modern macOS/cross-platform GUI proxy; great UX, freemium, not a Node.js library you embed. |

## Tech stack

- **Language:** Node.js (`engines: node >=6.0.0` — a very old floor).
- **Server / UI:** `express`, `ws`, `body-parser`, `compression`; web UI built with React 15 / antd 2 / redux / webpack 3 (all several majors behind).
- **MITM / certs:** `node-easy-cert` to generate and sign per-host certs from its own root CA (`bin/anyproxy-ca`, `lib/certMgr.js`).
- **Misc:** `request` (deprecated since 2020), `stream-throttle` (bandwidth), `nedb` (embedded recorder store), `brotli` / `iconv-lite`; async via `co` / `thunkify` / `async@~0.9` generators (pre-async-await).
- **Rule API:** JS rule files — `*beforeSendRequest`, `*beforeSendResponse`, `*beforeDealHttpsRequest` returning modified `requestDetail` / `responseDetail`; samples in `rule_sample/`.

## Dependencies

- **Runtime:** Node.js (built for the Node 6 era; modern Node compatibility is unverified — see Caveats).
- **CA cert:** you must generate and trust its root CA (`anyproxy-ca`) to MITM HTTPS — a device/OS trust step.
- **Storage:** embedded `nedb` for recordings; no external database or service required.
- **Client config:** the device/browser whose traffic you capture must be pointed at the proxy (HTTP proxy setting, or scan the QR helper on mobile).

## Ops difficulty

**Low for casual debugging, with caveats.** `npm install -g anyproxy`, `anyproxy-ca` to set up the cert, then run `anyproxy` and point a client at it — there's no datastore or cluster to operate. The real difficulty is age-driven: installing a Node-6-era package with a deprecated `request` dependency on a current Node runtime, and getting a generated MITM CA trusted on modern macOS/iOS where cert-validity and TLS rules are stricter, can both fail in ways nobody will fix. It's a local developer tool, not a service you'd run in production. [推断]

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-06).** Coasting/effectively abandoned: master code frozen since 2020-06, newest GitHub release v4.0.5, 248 open issues. The 2023-03 `pushed_at` reflects pushes to stale feature branches (20 branches: `typescript`, `optimze_memory_usage`, `feat/websocket_hooks`, several `fix/*`) that never merged to master — not real maintenance. [推断]
- **Governance / backing.** Owned by the Alibaba GitHub org, but heavily single-author in practice (`ottomao` ~168 commits, far ahead of the rest). Big-corp ownership has **not** meant active upkeep — a reminder that org backing ≠ liveness.
- **Age × Lindy.** Created 2014 (~12 years) — old, but **not currently active**, so Lindy doesn't apply: longevity without liveness is not a safety signal. [推断]
- **Adoption.** ~7.9k stars and historically widely used for mobile traffic debugging; ecosystem momentum has shifted toward whistle/mitmproxy/Proxyman.
- **Risk flags.** Dependency rot (deprecated `request`, Node 6 floor, React 15/webpack 3 UI), the npm-vs-GitHub version discrepancy (4.1.3 published, no matching tag), and quiet-internal-deprecation suspicion. Apache-2.0, no relicense history found. [推断]

## Caveats (unverified)

- [推断] The 2023-03 `pushed_at` reflects non-master feature-branch pushes, not master maintenance; master HEAD is the 2020-06 "release 4.1.3" commit.
- [推断] Cert/Node compatibility friction on modern OS/Node was reasoned from the Node 6 floor + deprecated `request` + stricter modern cert/TLS rules — not tested on a current system.
- [推断] "Quietly deprecated internally at Alibaba" is an inference from the frozen master + release gap, not a confirmed statement.
- [未验证] npm `latest` 4.1.3 vs GitHub release v4.0.5 (no v4.1.3 tag); the published 4.1.x line's provenance was not independently audited.
- [未验证] ~7.9k stars as of 2026-06; star counts are date-sensitive and indicative only.
