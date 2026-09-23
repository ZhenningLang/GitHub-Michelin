---
name: whistle
slug: whistle
repo: https://github.com/avwo/whistle
category: debugging-proxy
tags: [http-proxy, https, debugging, mock, web-ui, traffic-inspection, mitm, websocket]
language: JavaScript
license: MIT
maturity: v2.10.x, active, ~15.6k stars (as of 2026-06)
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2026-06-21T15:35:58Z
  default_branch: master
  default_branch_sha: 6da6e6c174c4d308199b9512c1ce1a7a671893ba
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:06:37Z
  overall: B
  overall_score: 3.0
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
        last_commit_age_days: 2
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 18.4
        qualifying_issues: 15
        band: relaxed_solo
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: npmjs.org
        canonical_package: whistle
        dependent_repos_count: 24
        downloads_last_month: 17165
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4211
        last_commit_age_days: 2
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 6
        top1_share: 0.979
        top3_share: 0.992
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

# whistle

A cross-platform HTTP/HTTPS/HTTP2/WebSocket debugging proxy: you point traffic at it, write rule lines in a web UI, and capture, inspect, rewrite, redirect, and mock requests on the fly — Fiddler/Charles-like, but browser-based and config-driven.

![whistle — health radar](../../assets/health/whistle.svg)

## When to use

You're a web or mobile developer staring at a bug that only happens against the *real* backend — an API returns a field your app chokes on, a CDN serves a stale bundle, or a flow only breaks on a teammate's staging host. You don't want to wait on a backend deploy to test a fix, and you don't want to hard-code mock data into the app. You install whistle (`npm i -g whistle`), start it, point your browser or phone's proxy at it, install its root cert once so HTTPS is decryptable, and now every request flows through a web UI where you can read full request/response pairs. You write a few rule lines — `www.example.com/api/user resBody://{mock.json}` to mock a response, `example.com 127.0.0.1:8080` to redirect a host to local, `example.com/app.js file:///path/app.js` to swap a script for a local file — and the change takes effect on the next request, no redeploy.

It shines when you need to inspect *and* rewrite at once: reproduce a production-only bug by mocking the exact bad payload, debug a mobile app by routing the device through whistle on your laptop, or front-end-test against a backend that isn't ready yet by mocking its endpoints. The rule syntax lives in a file you can version and share, so a whole team can reproduce the same interception setup.

## When NOT to use

- **You need a production gateway / reverse proxy.** whistle is a dev-time debugging proxy, not an edge or API gateway — no clustering, rate-limiting story, auth plugins, or production SLAs. For that use [Kong](../api-gateway/kong.md) (or nginx/Envoy).
- **You want a scraping IP rotation pool.** It interposes on *your* traffic to inspect/rewrite it; it does not source or rotate anonymous upstream proxies. For crawler IP pools see [proxy_pool](../proxy-pool/proxy-pool.md).
- **HTTPS interception is a hard no in your environment.** Decrypting HTTPS requires installing and trusting whistle's root CA on the client — a real attack-surface and policy risk (a trusted MITM cert). On locked-down / corporate / production devices that's often disallowed, and a leaked CA key is dangerous.
- **You need a vendor-backed, multi-maintainer tool with SLAs.** It's effectively a single-maintainer personal repo (owner is a GitHub User, not an org) — a bus-factor risk for anything you can't afford to have stall.
- **You can't read Chinese docs comfortably and want zero friction.** Documentation and much of the community discussion are heavily Chinese; English coverage exists but is thinner. [未验证]
- **You'd rather have a polished native GUI.** If you want a packaged desktop app, Charles or Proxyman fit that mold; if you want a scriptable CLI/Python proxy, mitmproxy is the better tool than a web-UI + rule-file model.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| Charles | 未收录 | Choose Charles when you need a polished paid native desktop proxy. | Paid native desktop proxy; mature, polished GUI for capture/rewrite/throttle, but commercial license and not config-file-driven like whistle's rule syntax. |
| Fiddler | 未收录 | Choose Fiddler when Windows-first debugging proxy heritage and .NET scripting matter. | Long-standing Windows-first debugging proxy (Fiddler Classic / Everywhere); rich .NET ecosystem and FiddlerScript, but heavier and partly commercial/closed. |
| [mitmproxy](mitmproxy.md) | ✅ | Choose mitmproxy when programmable Python interception is the priority. | Open-source (MIT-ish) Python proxy with a strong scripting/addon API and CLI/TUI; better for programmable interception, less of a point-and-click rule UI. |
| [anyproxy](anyproxy.md) | ✅ | Choose AnyProxy when you prefer Alibaba's Node.js proxy and JS rule files. | Alibaba's Node.js HTTP/HTTPS proxy with JS rule files; closer in spirit to whistle but smaller community and you write rules in JS rather than whistle's line syntax. |
| Proxyman | 未收录 | Choose Proxyman when a modern native GUI matters more than npm/web-UI operation. | Modern native macOS/cross-platform debugging proxy with a slick GUI; freemium/commercial, app-based rather than a web-UI + npm tool. |

## Tech stack

- **Language/runtime:** JavaScript on Node.js — installed and run as an npm CLI (`whistle` / `w2`).
- **Architecture:** a local proxy server plus a web UI; traffic is matched against rule lines (a custom whistle rule DSL: pattern → operator like `file://`, `resBody://`, `host`, `req`/`res` modifiers, `weinre`/inspect, etc.).
- **Protocols:** HTTP, HTTPS (via an installable root CA for decryption), HTTP/2, and WebSocket.
- **Extensibility:** a plugin system (whistle plugins published as `whistle.<name>` npm packages) extends matching/processing. [未验证]

## Dependencies

- **Node.js** is the one hard runtime dependency — you need a Node environment to install and run it (`package.json` declares an `engines.node` floor; the exact minimum is set by the repo and moves over time). [未验证]
- **A root CA install** on each client that should have HTTPS decrypted — a setup/operational dependency, not a service.
- No database or external service to stand up; state and rules live locally.

## Ops difficulty

**Low.** It's a single `npm i -g whistle` (or `npx`) then `w2 start`; the web UI runs locally and rules are edited there or in a rule file. The only real friction is HTTPS: generating and installing the root cert on every client/device you want to decrypt, and re-doing it per device/OS. Running it as a shared/team instance, or proxying mobile devices, adds a bit of network setup (everyone points their proxy at the host, trusts the cert), but there's no clustering, datastore, or scaling concern because it's a dev tool, not infrastructure.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 8.9 hours across 15 qualifying issues/PRs.
- **Maintenance (2026-06).** Last pushed 2026-06 and not archived; tags up through v2.10.x indicate it's **actively shipping**, not abandoned. [推断]
- **Governance / bus factor.** The repo owner is a **single GitHub User, not an organization** — effectively one maintainer. That's a real **bus-factor flag**: roadmap and continuity hinge on one person, even though the project is long-lived. [推断]
- **Age & Lindy verdict.** Created 2015-03 (~11 years) and **still active** ⇒ a **strong Lindy** signal for its niche — a debugging proxy that has survived and stayed maintained for a decade is a safer bet than a young one, the single-maintainer caveat notwithstanding. [推断]
- **Adoption.** ~15.6k stars and well-known in the Chinese front-end community; widely used as a Fiddler/Charles alternative there. Star counts are indicative, not proof of current health. [未验证]
- **Risk flags.** MIT-licensed with no relicense history found; the dominant risks are the single-maintainer bus factor and the inherent HTTPS-MITM trust model, not licensing. [推断]

## Caveats (unverified)

- [未验证] ~15.6k stars and v2.10.x as of 2026-06 — star counts and version numbers are date-sensitive and drift; treat as indicative only.
- [未验证] The minimum Node.js version is declared in the repo's `package.json` `engines` field and changes over time; not asserting a specific number here.
- [未验证] "Heavily Chinese documentation" is an inference from the project's origin and community; English docs exist but their completeness wasn't exhaustively audited.
- [未验证] The plugin ecosystem (`whistle.<name>` packages) and the full rule-operator set are described from the project's framing; specific plugins' maturity wasn't individually verified.
- [推断] "Single maintainer" is inferred from the owner being a GitHub User account; the real contributor distribution wasn't measured contributor-by-contributor.
