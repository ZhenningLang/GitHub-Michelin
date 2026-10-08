---
name: wxpy
slug: wxpy
repo: https://github.com/youfou/wxpy
category: wechat
tags: [wechat, im-automation, chatbot, python, web-protocol, deprecated, personal-account, itchat]
language: Python
license: MIT
maturity: abandoned — archived (last push 2019-07; last commit 2017-07-29, last release 0.3.9.8 2017-06); built on the same now-defunct WeChat web protocol as ItChat, mostly non-functional for new accounts (as of 2026-10-08)
last_verified: 2026-10-08
type: library
upstream:
  pushed_at: 2019-07-14T17:59:47Z
  default_branch: master
  default_branch_sha: ab63e12da822dc85615fa203e5be9fa28ae0b59f
  archived: true
health:
  schema: 1
  computed_at: 2026-10-08T08:20:05Z
  overall: D
  overall_score: 1.2
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: true
        last_commit_age_days: 3358
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: E
      raw:
        median_ttfr_hours: null
        qualifying_issues: 0
        band: default
        window_offset_days: 10
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: wxpy
        package_link: ecosystems_repository_url
        dependent_repos_count: 182
        downloads_last_month: 542
        graph_tier: C
        volume_tier: E
        cross_check_divergence: null
        tier_source: registry
        archived: true
    longevity:
      grade: E
      raw:
        repo_age_days: 3517
        last_commit_age_days: 3358
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    governance: { reason: unattributable }
---

# wxpy

An elegant Python API for WeChat **personal** accounts — a friendly, higher-level wrapper over [ItChat](itchat.md)'s web-WeChat protocol, historically used to build chatbots and account automation. **Read this plainly: the repo was archived in 2019-07 (read-only, abandoned), and the WeChat web (`wx.qq.com`) login protocol it relies on — the very same one ItChat uses — has been largely shut down, so for most accounts wxpy no longer logs in or works at all.** It survives as reference code and nostalgia, not as a tool you can ship today.

![wxpy — health radar](../../../assets/health/wxpy.svg)

## When to use

You're a developer or researcher excavating the older generation of Chinese WeChat-bot projects — a wave of 2017–2019 tutorials, "build a WeChat bot in 30 lines" blog posts, and toy automation repos were written on wxpy because its API was noticeably nicer than raw ItChat (`bot.friends()`, `bot.groups()`, `@bot.register()`, friendly `Chat`/`Friend`/`Group` objects). You've inherited or are studying one of those repos and want to understand the model: how it wrapped the QR-login + `synccheck` long-poll flow into clean Python objects and a decorator-based message router. For *reading and learning from that body of code* — and appreciating a well-designed wrapper API — wxpy is a pleasant, well-documented reference.

That is realistically the only safe reason to reach for it in 2026. If your actual goal is to *run* new WeChat automation, wxpy is the wrong starting point (see below): it is an archived wrapper over a defunct protocol — a museum piece that shows good API taste, not a dependency for a new build.

## How it works

wxpy does not speak to WeChat itself: it installs a pinned old ItChat (`itchat==1.2.32`) and lets that library handle the web-WeChat login and message polling. **What wxpy adds is the object layer**: after `Bot()` logs you in by QR code, your friends, groups and official accounts are Python objects you can search (`bot.friends().search(...)`) and call (`my_friend.send(...)`), instead of the raw dicts ItChat hands back. **You write reply functions** and register them with `@bot.register(...)` for a chat, a friend or a message type; wxpy routes each new message to the most recently registered match, runs it on a worker thread, and sends back whatever the function returns. You keep the process alive with `bot.join()` or the interactive `embed()` console. As with ItChat, the card shows the path from when the web login was open — today most accounts stop at the QR scan.

![wxpy — backbone user story](../../../assets/flow/wxpy.svg)

<!-- flow-steps:begin (generated from flows/wxpy.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install it into Python 3.4–3.6 or 2.7 — `pip install -U wxpy`
2. **You**: Create a bot and scan the QR code with your phone — `bot = Bot()`
3. **wxpy**: Logs in through its pinned ItChat and turns friends, groups and official accounts into objects — component: `ItChat 1.2.32 underneath`
4. **You**: Register a reply function for a chat, a friend, or a message type — `@bot.register(my_friend)`
5. **wxpy**: Routes each new message to the last-registered matching function, on worker threads
6. **wxpy**: Sends the function's return value back into that chat

**Value**: Personal-account automation in object-style Python instead of raw ItChat dicts — while the web login worked

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You want WeChat automation that actually works today.** This is the dominant reason. wxpy sits on top of ItChat, which sits on WeChat's **web/`wx.qq.com` login protocol** — and Tencent progressively disabled that protocol. **Most accounts, especially newer ones, simply cannot log in through it anymore.** [未验证] The wrapper isn't broken in its own code so much as the platform pulled the rug out from under the layer beneath it.
- **It is archived and abandoned.** The repo is **archived** (GitHub read-only; last push 2019-07, last commit 2017-07-29 — ~9 years without code changes), single-maintainer (owner `youfou`). No PRs, no releases, no protocol fixes will ever land — archiving is the maintainer's explicit "this is done" signal.
- **Account-ban / ToS risk.** Driving a *personal* WeChat account through an unofficial reverse-engineered protocol **violates WeChat's Terms of Service** and carries a real risk of the account being **rate-limited, frozen, or permanently banned.** Don't point it at an account you care about.
- **You need a supported path for IM automation.** Use **official** surfaces: the **WeCom (企业微信 / WeChat Work) API** and **WeChat Official Account / Mini-Program** server APIs are the sanctioned, maintained channels. For personal-account-style automation, **wechaty** is the more actively maintained successor abstraction — though it inherits the same upstream-platform and ToS exposure, so adopt it with caution.
- **Production or anything customer-facing.** An archived wrapper on a defunct protocol cannot underpin a product or a business commitment — and unlike its base, it isn't even receiving the dependency drift fixes a coasting project might.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [ItChat](itchat.md) | ✅ | Choose ItChat when you need wxpy's lower-level base layer rather than its object wrapper. | wxpy's **own base layer** — the lower-level web-WeChat library wxpy wraps. Also abandoned and also non-functional on the dead web protocol; wxpy adds a nicer object API on top but inherits *every* viability problem ItChat has, plus its own 2019 archival. Strictly downstream — no reason to prefer wxpy for new work over either. |
| [wechaty](wechaty.md) | ✅ | Choose wechaty when a maintained multi-language bot framework is worth the puppet risk. | Actively-maintained multi-language (TS/Python/Go/Java) conversational-bot framework with pluggable "puppets"; the de-facto successor for personal-account-style WeChat bots, but still rides on unofficial/3rd-party access channels and the same ToS/ban exposure — pick a puppet carefully. |
| WeCom / Official WeChat Work API | 未收录 | Choose WeCom when official enterprise messaging automation is acceptable. | Tencent's **official, sanctioned** enterprise messaging API; stable and supported, but it automates *WeCom* accounts/contacts, not arbitrary personal WeChat accounts — a different (legitimate) surface, not a drop-in replacement. |
| WeChat Official Account / Mini-Program server APIs | 未收录 | Choose official account or mini-program APIs for supported public-account automation. | Official server-side APIs for *public accounts* and mini-programs; fully supported but a different product surface (broadcast/service accounts), not personal 1:1 IM automation. |

## Tech stack

- **Language:** Python — the README lists 3.4–3.6 and 2.7 (pure-Python, no native extensions); nothing newer was ever declared.
- **Built on ItChat:** wxpy is fundamentally a **wrapper over [ItChat](itchat.md)** — it reuses ItChat's web-WeChat mechanism (QR-code login against `wx.qq.com`, session/cookie management, the long-polling `synccheck` message loop) and layers an object model on top; `setup.py` pins `itchat==1.2.32`, and the README says ItChat's raw calls can still be mixed in.
- **API surface:** friendlier abstractions than raw ItChat — `Bot`, `Friend`, `Group`, `MP`, `Chat` objects; `@bot.register(...)` message-handler decorator; search/filter helpers; plus convenience integrations (e.g. Tuling chatbot, puppet-style auto-reply) documented in its era.
- **Capabilities:** send/receive text, images, files; friend and group (chatroom) management — all scoped to a single logged-in personal account.

## Dependencies

- **Runtime:** a Python interpreter plus `setup.py`'s three requirements — **`itchat==1.2.32`** (pinned to an exact, older ItChat), `requests`, `future` — and whatever ItChat pulls in (`pyqrcode`, `pypng`). pip-installable.
- **The real dependency is a working web-WeChat session** — and *that* is the broken link: it needs Tencent's web-login endpoint to accept your account, which for most accounts it no longer does. Nothing in local dependency management fixes a server-side block.
- **A scannable WeChat account** on a phone to complete QR login each session; sessions are not durable and re-login is frequent.

## Ops difficulty

**Low to run, but that's beside the point — viability, not ops, is the blocker.** Install and a "hello world" auto-reply bot are genuinely a few lines (`bot = Bot()` plus a `@bot.register()` handler), and wxpy's docs were better than most. But the hard part is entirely external: getting the login to succeed *at all* on the defunct web protocol, keeping a flaky session alive, and accepting that the logging-in account is exposed to throttling or banning. There is no server, datastore, or cluster to operate — the difficulty is that the thing it ultimately talks to has mostly been turned off, and no operator effort restores it.

## Health & viability

- **Responsiveness**: Grade E.
- **Maintenance (2026-10): archived → dead.** The repo is **archived** (last push 2019-07; last commit **2017-07-29**, last release 0.3.9.8 in 2017-06), making it GitHub read-only — single-maintainer (owner `youfou`), no releases, no triage, no PRs accepted. Archiving is the maintainer's explicit end-of-life flag; this is not "coasting," it is closed.
- **Platform pulled the rug — compounded by its base.** wxpy wraps **ItChat**, and **WeChat largely disabled the web-login protocol both depend on**, so wxpy is *non-functional for most accounts* regardless of its own code. It is abandoned **and** structurally obsolete **and** one layer removed from the protocol break — strictly worse off than the base it sits on. [未验证]
- **Lindy verdict: FAILS, hard.** Created **2017-02** (~9 years old), so on age alone it might look Lindy — but Lindy is **age × still-active**, never age alone. Here it is **long-lived *and* explicitly archived *and* running on a protocol the platform removed** — the textbook case where the age signal is *negated*, not earned. Its longevity is not durability. [推断]
- **Governance / bus factor.** Single-maintainer hobby project, no foundation, vendor, or successor stewardship — bus factor of one, and the repo is frozen, so even that one has formally stepped away. [推断]
- **Risk flags.** Against WeChat ToS; account-ban exposure; unofficial reverse-engineered protocol the vendor actively closes off; depends transitively on an also-abandoned library. MIT license is the only un-encumbered part of the picture. [推断]

## Caveats (unverified)

- [未验证] "~14.3k stars" is from the GitHub repo page as of 2026-06; star counts are date-sensitive and unreliable — treat as indicative only.
- [推断] The archival date is not exposed by the API; "archived around 2019-07" is inferred from the last `pushed_at` (2019-07-14). The last commit (2017-07-29) and `archived: true` were checked on 2026-10-08.
- [未验证] The claim that WeChat **disabled the web-login protocol** so wxpy/ItChat "mostly don't work for new accounts" is widely reported by the community and consistent with both projects' dormancy, but neither repo carries an explicit Tencent deprecation notice — this is inferred from platform behavior, not quoted from an official statement.
- [未验证] "wxpy is a wrapper over ItChat" is confirmed by `setup.py` (`itchat==1.2.32`) and the README; which ItChat internals it reuses vs. reimplements was not traced in source.
- [未验证] Comparison rows (wechaty's current activity, exact WeCom/Official-Account API scope) describe the general landscape and were not freshly re-verified against each project's current state.
- [推断] Account-ban / ToS-violation risk is an inference from the unofficial-protocol nature of the tool, not a measured ban rate; severity varies by account and usage.
