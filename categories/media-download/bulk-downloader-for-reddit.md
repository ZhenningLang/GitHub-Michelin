---
name: bulk-downloader-for-reddit
slug: bulk-downloader-for-reddit
repo: https://github.com/Serene-Arc/bulk-downloader-for-reddit
category: media-download
tags: [reddit, downloader, archiver, scraping, yt-dlp, python, cli]
language: Python
license: GPL-3.0
maturity: v2.6.2 (2023-01), commits ongoing to 2026-04, ~2.6k stars (as of 2026-06)
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2026-04-12T02:28:43Z
  default_branch: master
  default_branch_sha: 8c293a46843c818bea2c2013db38191867993a14
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:35:17Z
  overall: D
  overall_score: 0.5
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
        last_commit_age_days: 1331
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 31160
        release_assets: 60
        release_tier: D
        signal_basis: releases
    longevity:
      grade: E
      raw:
        repo_age_days: 3022
        last_commit_age_days: 1331
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: D
      raw:
        spdx_id: GPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
    governance: { reason: unattributable }
---

# bulk-downloader-for-reddit

A command-line tool (BDFR) that downloads media and/or archives metadata from Reddit — subreddits, multireddits, users, saved/upvoted posts, or direct links — via the official Reddit OAuth API.

![bulk-downloader-for-reddit — health radar](../../assets/health/bulk-downloader-for-reddit.svg)

## When to use

You're archiving a subreddit before it goes private, or backing up your own saved/upvoted posts, or building a personal dataset of images and videos from a handful of communities. You don't want to click through hundreds of threads, and you want both the *files* (images, galleries, Redgifs/Imgur/YouTube-hosted clips) and the *context* (post titles, scores, comment trees) on disk in a predictable folder layout. You register a Reddit API app for OAuth credentials, then run `bdfr download ./out --subreddit pics --limit 200 --sort top`, or `bdfr clone ./out --user me --upvoted` to grab both files and metadata. BDFR resolves each submission's link through its own resolvers plus yt-dlp, names files by a template you control, dedupes by hash, and keeps a log so re-runs are incremental rather than re-downloading everything.

It's the right reach when you want a *scriptable, reproducible* Reddit archive — three modes (`download` files-only, `archive` metadata-only, `clone` both), YAML config for repeatable jobs, and a folder/naming scheme you can pin down — rather than a one-off browser extension grab.

## When NOT to use

- **You expect to pull more than ~1000 posts from a single source.** This is a hard Reddit API ceiling (listings cap at ~1000), and the README states plainly: "We cannot bypass this." For deep historical archives you need a different approach (e.g. Pushshift-style dumps, where still available).
- **You want a faithful, browsable clone of Reddit.** `clone` retrieves raw data, not a navigable replica — no rendered site, no guaranteed completeness of comment trees.
- **You can't / won't register Reddit API credentials.** Authenticated access uses OAuth2; without an API app many operations won't work.
- **You need a maintained, frequently-released tool.** The last tagged release (v2.6.2) is from early 2023; commits continue but the release cadence has effectively stalled — you may be running from `master` rather than a blessed version (see Health).
- **Content on sites BDFR/yt-dlp can't resolve.** It handles Imgur, Redgifs, galleries, YouTube, and "anything yt-dlp supports," but an unsupported or newly-changed host will simply fail for those links. [推断]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [gallery-dl](gallery-dl.md) | ✅ | Choose gallery-dl when you need a broad multi-site media downloader that includes Reddit. | Broad multi-site media downloader (Reddit among many); strong for *files* across the web, but weaker at Reddit-specific metadata/comment archiving and the three-mode download/archive/clone model. |
| redditdownloader (shadowmoose) | 未收录 | Choose redditdownloader when you need another dedicated Reddit downloader with a web UI. | Another dedicated Reddit downloader with a web UI; more approachable for non-CLI users, but BDFR's scriptable CLI + YAML config suits automation better. [未验证] |
| Pushshift dumps / PRAW scripts | 未收录 | Choose Pushshift dumps or PRAW scripts when you want to bypass tooling and build directly on data/API access. | Going straight to data dumps or the API yourself bypasses tooling and the ~1000 cap (dumps) but is roll-your-own — BDFR packages resolvers, dedup, naming, and logging for you. |
| [yt-dlp](yt-dlp.md) (directly) | ✅ | Choose yt-dlp directly when you only need to download individual hosted-media links. | BDFR *uses* yt-dlp under the hood for hosted media; calling yt-dlp directly works for individual links but lacks Reddit-source enumeration, metadata archiving, and dedup. |

## Tech stack

- **Language:** Python 3.9+.
- **Reddit access:** the official Reddit API over OAuth2 (PRAW-style client) for enumerating submissions and metadata.
- **Media resolution:** built-in per-site resolvers (Imgur, Redgifs, Reddit galleries/video, Vidble, Erome, …) plus **yt-dlp** as the general fallback.
- **Output:** templated file naming, hash-based dedup, structured logs; YAML config for repeatable runs; three modes (download / archive / clone).

## Dependencies

- **Runtime:** Python 3.9+, installed via `pip install bdfr` / pipx (AUR package on Arch).
- **Credentials:** a Reddit API application (OAuth2 client) for authenticated access.
- **Bundled libs:** yt-dlp and per-site resolver code; Reddit API client. [推断]
- **No database / no services** — it writes files and a log to local disk; state is the on-disk output + log.

## Ops difficulty

**Low.** It's a `pip`/pipx install plus a one-time Reddit API app registration, then a CLI invocation (or a cron'd YAML job). There's no server, datastore, or queue to operate; the incremental log makes re-runs cheap and idempotent-ish. The realistic friction is operational, not infrastructural: respecting the ~1000-post ceiling, occasional resolver breakage when a host changes, and the fact that you may be running unreleased `master` code so you own keeping it current and verifying it still works.

## Health & viability

- **Maintenance**: Grade E — 0/13 active weeks in trailing 13; last commit 1331 days ago.
- **Responsiveness**: Cannot be scored — no_traffic.
- **Adoption**: Grade D.
- **Longevity**: Grade E — 3022 days old.
- **Governance**: Cannot be scored — unattributable.
- **Risk / License**: Grade D — GPL-3.0 license.

## Caveats (unverified)

- [未验证] ~2.6k stars as of 2026-06 and v2.6.2 (2023-01) as the last tag — figures are date-sensitive; commit activity to 2026-04 is from the API but the "maintained but unreleased" read is a judgment.
- [未验证] Exact Reddit-API client (PRAW vs custom OAuth client) and the precise current resolver list are inferred from the README, not confirmed against the manifest in this pass.
- [推断] OAuth credential requirement for most operations is the standard Reddit-API posture; the precise set of features that work unauthenticated is not verified here.
- [推断] Per-host failure on unsupported/changed sites is inferred from the resolver+yt-dlp architecture, not a tested enumeration.
