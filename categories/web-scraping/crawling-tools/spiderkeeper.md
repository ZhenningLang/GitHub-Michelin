---
name: SpiderKeeper
slug: spiderkeeper
repo: https://github.com/DormyMo/SpiderKeeper
category: crawling-tools
tags: [scrapy, scrapyd, dashboard, admin-ui, scheduler, flask, python]
language: Python
license: MIT
maturity: PyPI v1.2.0 (2017-09), repo stale since 2023-05, ~2.8k stars (as of 2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2023-05-04T20:44:05Z
  default_branch: master
  default_branch_sha: d6156d35a95ba8c3ac759a08367079619555b6dd
  archived: false
health:
  schema: 1
  computed_at: 2026-09-23T07:55:52Z
  overall: E
  overall_score: 0.33
  scored_axes: 3
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 3039
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: spiderkeeper
        dependent_repos_count: 5
        downloads_last_month: 28
        graph_tier: D
        volume_tier: E
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: E
      raw:
        repo_age_days: 3901
        last_commit_age_days: 3039
        cohort: app
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
    risk_license: { reason: license_declared_unverifiable }
---

# SpiderKeeper

A Flask-based admin web UI / dashboard for Scrapy spiders that sits on top of Scrapyd — deploy projects, schedule periodic jobs, and watch run stats from a browser. It crawls nothing itself; it's a management layer over one or more Scrapyd servers. Lightweight, popular, and largely stale.

![spiderkeeper — health radar](../../../assets/health/spiderkeeper.svg)

## When to use

You're running a small crawl operation on Scrapyd and you're tired of `curl`-ing JSON endpoints to deploy and schedule spiders. You want a browser dashboard: upload a project egg with a click, set a spider to run every night on a cron, see which jobs are running/finished, and glance at stats — without writing your own UI. You `pip install spiderkeeper`, point it at your Scrapyd server (`--server=http://localhost:6800`), and get a Flask dashboard on port 5000 with periodic scheduling (via APScheduler), a job board, and a Swagger API. For a single developer or a small team that already runs Scrapyd and wants the simplest possible control panel, SpiderKeeper is the lightweight classic — provided you accept that the software is old (see below).

## When NOT to use

- **Don't adopt it for new 2026 projects.** Repo code is stale since 2023-05 and the PyPI release is frozen at v1.2.0 (2017-09). It pins a 2017-era stack (Flask 0.12, SQLAlchemy 1.1, Werkzeug 0.12), so installing on modern Python (3.11+) means pin-relaxation friction and carrying unpatched transitive deps. [推断]
- **No value without Scrapyd.** It's purely a UI over Scrapyd — if you don't run Scrapy/Scrapyd it does nothing for you. See [Scrapyd](scrapyd.md).
- **Weak security — don't expose it on an untrusted network.** Auth is optional HTTP basic only, defaulting to `admin`/`admin`, with no user management, RBAC, or TLS. Not hardened for multi-tenant or public deployment.
- **Newer alternatives are more capable.** Gerapy (Django+Vue, more modern, distributed management) and ScrapydWeb (multi-node, log parsing, alerts) are the fuller successors in this niche; SpiderKeeper is the older, simpler one.
- **Don't rely on a clean license.** MIT is declared in `setup.py` and the README badge, but the README links a `LICENSE.md` that doesn't exist in the repo — so GitHub detects no license, and the MIT text/copyright grant is asserted but not actually shipped. [推断]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Scrapyd](scrapyd.md) | ✅ | Choose Scrapyd when you need the daemon SpiderKeeper wraps. | The daemon SpiderKeeper wraps — actively maintained, org-backed. SpiderKeeper is a UI *on top of* it, not an alternative to it. |
| Gerapy | 未收录 | Choose Gerapy when you need a Django + Vue dashboard for distributed Scrapy management. | Django + Vue dashboard for distributed Scrapy management; more modern and generally the recommended successor in this niche today. |
| ScrapydWeb | 未收录 | Choose ScrapydWeb when you need a more featureful web UI over Scrapyd. | More featureful web UI over Scrapyd (multi-node, log parsing, email alerts), but itself also fairly stale. |
| Zyte Scrapy Cloud | 未收录 | Choose Zyte Scrapy Cloud when you need a commercial hosted alternative. | Commercial hosted alternative — no self-hosting of the scrapyd+UI stack, at the cost of vendor lock-in and pricing. |

## Tech stack

- **Language:** Python; a Flask web application.
- **Web/UI:** Flask 0.12 + Werkzeug/Jinja2/itsdangerous (2017 versions), Flask-RESTful + flask-restful-swagger for the API/Swagger UI.
- **Storage:** Flask-SQLAlchemy / SQLAlchemy 1.1 — SQLite by default, MySQL via PyMySQL.
- **Scheduling:** APScheduler 3.3 for periodic/cron jobs.
- **Auth:** Flask-BasicAuth (HTTP basic only).
- **Scrapyd link:** `requests` to talk to the Scrapyd JSON API; eggs built with `scrapyd-client`.

## Dependencies

- **Hard dependency:** a running Scrapyd server (`--server=...`, `--type=scrapyd`). SpiderKeeper is useless without it.
- **Runtime:** Python (2017-era pins target Python 2.7 / 3.5; modern Python likely needs pin relaxation — see Caveats).
- **Database:** SQLite by default (zero-config); MySQL optional via PyMySQL.
- **Build/deploy flow:** `scrapyd-client` to package a project egg, uploaded through SpiderKeeper to Scrapyd.

## Ops difficulty

**Low to run, with a stale-software tax.** Day one is easy: `pip install spiderkeeper`, point it at Scrapyd, open port 5000 — SQLite means no database to provision. The friction is keeping a 2017-pinned Flask 0.12 stack installable on a current interpreter, and the security posture: the default `admin`/`admin` basic auth and absence of TLS/RBAC mean you must put it behind a reverse proxy with real auth (or keep it on localhost/VPN) before anyone else can reach it. There's no clustering or HA story — it's a single lightweight Flask process you babysit.

## Health & viability

- **Responsiveness**: Cannot be scored — no_data.
- **Maintenance (2026-06).** Stale / likely abandoned — repo code untouched since 2023-05, PyPI frozen at v1.2.0 since 2017-09, no GitHub releases or tags, ~70 open issues. Not archived, but no release cadence. [推断]
- **Governance / bus factor.** Bus factor **1**: `DormyMo` has ~93 commits, every other contributor 1–3. A single-maintainer User account with no org continuity.
- **Age × Lindy.** Alive since 2016 but silent ~3 years (and the package silent ~9 years) — fails Lindy, which needs old **and** active; an unmaintained tool against a moving Scrapy/Python stack only rots. [推断]
- **Adoption.** ~2.8k stars reflect real past popularity as the simplest Scrapyd dashboard, but momentum has moved to Gerapy/ScrapydWeb. The vendor demo homepage is likely down. [未验证]
- **Risk flags.** Stale dependency floor, default-credential weak auth, single maintainer, and an incomplete license (MIT declared but the license file is missing from the repo). [推断]

## Caveats (unverified)

- [推断] License is *declared* MIT (setup.py + README badge) but the referenced `LICENSE.md` file does not exist in the repo, so the MIT grant is asserted without the actual license text shipping; GitHub metadata reports no license.
- [推断] PyPI v1.2.0 (2017-09) is far staler than the repo (last push 2023-05); the published package being installable on modern Python without pin relaxation is doubtful but untested here.
- [未验证] The vendor demo homepage liveness, and the current relative staleness of ScrapydWeb vs Gerapy, were not independently fetched this session.
- [未验证] ~2.8k stars / ~70 open issues as of 2026-06; counts are date-sensitive and indicative only.
