---
name: NetNewsWire
slug: netnewswire
repo: https://github.com/Ranchero-Software/NetNewsWire
category: reading-tools
tags: [rss, feed-reader, atom, macos, ios, swift, native-app]
language: Swift
license: MIT
maturity: v7.1, active (2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2026-06-29T00:41:39Z
  default_branch: main
  default_branch_sha: 3b22efcdc97ece294c7dc746bc4f4917e04042ef
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:13:48Z
  overall: B
  overall_score: 3.4
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 28.4
        qualifying_issues: 35
        band: relaxed_solo
        window_offset_days: 13
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: A
      raw:
        repo_age_days: 3330
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 18
        top1_share: 0.887
        top3_share: 0.984
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
    adoption: { reason: no_package_structural }
---

# NetNewsWire

A free, open-source, native RSS/Atom feed reader for macOS and iOS — fast, no telemetry, and built by the developer who originally created the category-defining Mac feed reader.

![netnewswire — health radar](../../assets/health/netnewswire.svg)

## When to use

You're a Mac and iPhone user who reads a lot — newsletters you'd rather not get in email, a dozen tech blogs, a few news sites, some niche feeds — and you've watched the algorithmic timelines turn into noise. You want a *chronological*, you-own-the-list reading experience: subscribe to feeds, read them in order, mark as read, move on. You don't want a web app that ships your reading habits to an ad network, and you don't want a heavy Electron app that drains battery. You install NetNewsWire from the Mac App Store (or build it from source), point it at your OPML export from whatever reader you're leaving, and you have a native, AppKit/UIKit app that syncs across your Mac and iPhone and just shows you your feeds — no account required to start, no subscription, no ads.

You also reach for it when you already keep your subscriptions in a sync service — Feedly, Feedbin, iCloud, Inoreader, NewsBlur, or a self-hosted FreshRSS/Reader API endpoint — and you want a clean native client on top rather than that service's own web UI. NetNewsWire is the *reading client*, not the sync backend: you bring your account, it gives you a fast Apple-platform front end with keyboard shortcuts, a built-in reader view, and articles cached for offline reading.

## When NOT to use

- **You're not on Apple platforms.** It is macOS + iOS/iPadOS only — there is no Windows, Linux, Android, or web build. If you need cross-platform, this is a hard no.
- **You want a self-hosted sync server.** NetNewsWire is a client; it syncs *through* services (iCloud, Feedbin, Feedly, etc.) but does not host your feeds for other devices/apps. For a server you run, that's FreshRSS / Miniflux / Tiny Tiny RSS territory.
- **You want a read-it-later / annotation / web-clipper suite.** It reads feeds; it is not Instapaper/Pocket/Readwise. There's no highlighting, tagging-as-knowledge-base, or full-text article archive workflow.
- **You depend on social / "smart" discovery feeds.** This is deliberately a plain chronological reader. No algorithmic recommendations, no built-in social graph.
- **You need a polished commercial support contract.** It's a volunteer/community open-source app with no paid tier; support is GitHub issues and a Slack/community, not an SLA.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| Reeder | 未收录 | Choose Reeder when a polished paid Apple-platform reader is acceptable and closed source is not a blocker; choose NetNewsWire when free MIT code, auditability, and no monetization pressure matter more. | Polished commercial Apple-platform reader with broad sync support; closed-source and paid, where NetNewsWire is free/MIT and auditable. |
| [FreshRSS](freshrss.md) | ✅ | Choose FreshRSS when you need the self-hosted feed server and web UI; choose NetNewsWire as the native Apple client that can sit on top of that backend. | Self-hosted PHP feed *server* + web UI; you run it, it syncs to many clients (including NetNewsWire) — a backend, not a native client. |
| Miniflux | 未收录 | Choose Miniflux for a minimalist self-hosted Go backend and web reader; choose NetNewsWire when the value is a native macOS/iOS front end rather than operating a server. | Minimalist self-hosted Go feed reader (server + web); single-binary backend, no native Apple app of its own. |
| Feedly / Inoreader | 未收录 | Choose Feedly or Inoreader when hosted cross-platform discovery, rules, and service features matter; choose NetNewsWire when you want an Apple-native client over a simpler chronological feed list. | Hosted SaaS readers with discovery and rules; cross-platform and feature-rich but proprietary and data-hungry — NetNewsWire can act as a native client to some of these. |
| NewsBlur | 未收录 | Choose NewsBlur when you want a hosted/open-source service stack with training or intelligence features; choose NetNewsWire when local-first native reading is the core requirement. | Open-source hosted reader with training/intelligence features; a full service stack vs NetNewsWire's local-first native client. |

## Tech stack

- **Language:** Swift, targeting Apple's native UI frameworks (AppKit on macOS, UIKit on iOS/iPadOS). [推断]
- **Sync accounts:** built-in support for iCloud, Feedbin, Feedly, Inoreader, NewsBlur, The Old Reader, BazQux, FreshRSS / Reader-API-compatible endpoints, plus local on-device accounts. [未验证]
- **Feed formats:** RSS, Atom, JSON Feed; OPML import/export for subscriptions.
- **Build:** Xcode project; distributed via the Mac App Store and the iOS App Store, and buildable from source.

## Dependencies

- **Runtime:** a Mac (macOS) and/or iPhone/iPad (iOS/iPadOS); no server required for single-device use.
- **Optional sync backend:** an account with one of the supported services if you want cross-device sync (iCloud is the zero-extra-signup path on Apple platforms).
- **Build-time:** Xcode + the Swift toolchain to build from source; minimum OS/Xcode versions are set by the repo and move forward over time. [未验证]

## Ops difficulty

**Low — it's an end-user app, not a service.** For a user, "ops" is installing from the App Store and (optionally) signing into a sync account. There is nothing to deploy or operate. The only burden is on the *contributor/builder* side: cloning, opening in Xcode, and matching the required Xcode/SDK version. If you self-host the *sync* layer (e.g. FreshRSS), that server's ops are separate and not part of NetNewsWire.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 28.4 hours across 35 qualifying issues/PRs.
- **Maintenance (2026-06).** Last pushed 2026-06; iOS 7.1 and mac 7.1 releases shipped in June 2026 with beta builds in between — clearly **active** development, not coasting. Not archived.
- **Governance / bus factor.** Created and led by Brent Simmons (`brentsimmons`), who authored the original NetNewsWire decades ago; there is a real contributor list (vincode-io, Wevah, kielgillard, and others) beyond the lead, but the project's direction is strongly identified with one well-known developer — a moderate bus-factor consideration. [推断]
- **Age & Lindy verdict.** This repo dates to 2017-05 (~9 years), and the NetNewsWire *name/app* is far older than the repo — it's one of the longest-lived Mac feed readers — and it is still actively shipping ⇒ **strong Lindy** signal. (Repo age understates true project age. [未验证])
- **Adoption.** ~10.2k stars, 700+ forks, a known and recommended app in the Apple/RSS community; MIT-licensed and free with no monetization pressure. [未验证]
- **Risk flags.** Volunteer/community model means no commercial SLA and roadmap pace depends on contributor time; Apple-only scope is a portability ceiling, not a health risk. No relicense history found. [推断]

## Caveats (unverified)

- [未验证] ~10.2k stars, 708 forks, 863 open issues as of 2026-06 — star/issue counts are volatile and date-sensitive; treat as indicative.
- [未验证] The exact set of supported sync services (Feedbin/Feedly/Inoreader/NewsBlur/iCloud/FreshRSS/Reader API…) is from project docs and changes release to release; verify the specific account type you need against the current app.
- [推断] AppKit/UIKit native implementation and Swift-only stack is inferred from the language metadata and the app's positioning as a "native" reader, not from a code audit.
- [未验证] The repo's `created_at` (2017-05) reflects this GitHub repository, not the original NetNewsWire's true first-release date, which is substantially earlier.
- [未验证] Minimum supported macOS/iOS and Xcode versions for building from source are governed by the repo and shift over time; not asserting specific numbers here.
