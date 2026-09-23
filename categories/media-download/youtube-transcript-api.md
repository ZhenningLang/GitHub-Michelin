---
name: youtube-transcript-api
slug: youtube-transcript-api
repo: https://github.com/jdepoix/youtube-transcript-api
category: media-download
tags: [youtube, transcript, subtitles, captions, scraping, python, library]
language: Python
license: MIT
maturity: v1.2.4, active, ~7.8k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-05-19T18:17:07Z
  default_branch: master
  default_branch_sha: 72d79711ec4db95262660029b4d63298b0820502
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:36:17Z
  overall: B
  overall_score: 3.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 13
        active_weeks_13: 1
        carve_out: mature_library_lindy
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 14.8
        qualifying_issues: 4
        band: default
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: youtube-transcript-api
        dependent_repos_count: 205
        downloads_last_month: 16400197
        graph_tier: C
        volume_tier: A
        cross_check_divergence: 1.04
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 3077
        last_commit_age_days: 13
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 4
        top1_share: 0.765
        top3_share: 0.941
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

# youtube-transcript-api

A Python library that fetches the transcript/subtitles (including auto-generated ones) for a YouTube video — no API key, no headless browser — by calling the same undocumented endpoint the YouTube web client uses.

![youtube-transcript-api — health radar](../../assets/health/youtube-transcript-api.svg)

## When to use

You're building a pipeline that summarizes or indexes YouTube videos — a RAG corpus, a "TL;DR this talk" bot, a research tool that searches across hundreds of lecture transcripts — and you need the spoken text, not the audio. The official YouTube Data API doesn't hand you full caption text without OAuth and channel ownership, and spinning up Selenium to scrape the player is slow and brittle. You `pip install youtube-transcript-api`, then `YouTubeTranscriptApi().fetch(video_id)` returns the timestamped transcript as plain objects you can immediately feed to an LLM or a formatter (SRT/WebVTT/JSON/text). You can ask for a preferred language list, fall back across manual vs auto-generated tracks, and even have YouTube translate the transcript to another language — all in a few lines, key-free.

It shines as a *building block*: it's the transcript-fetch layer under a larger app, used in notebooks and batch jobs where you want timestamped text out of an ID with minimal ceremony. When you run it from your own machine or a residential IP, the no-auth path "just works."

## When NOT to use

- **Cloud / datacenter IPs without proxies.** YouTube actively blocks requests from AWS/GCP/Azure ranges; from a server you'll hit IP bans and need to route through (residential) proxies — the library has built-in Webshare/generic proxy support precisely because of this, but it's now a *requirement*, not a nicety, for reliable cloud use.
- **You need a stable, contractual API.** This rides an **undocumented** endpoint. The maintainer states plainly there is no guarantee it won't break tomorrow if YouTube changes things — don't build something you can't afford to see break on a YouTube-side change.
- **Age-restricted / login-walled videos.** Cookie/auth-based access for restricted content has been hampered by YouTube API changes and is not reliably available. [未验证]
- **Videos with captions disabled.** If the uploader disabled captions and there's no auto-generated track, there's nothing to fetch — it doesn't transcribe audio itself.
- **ToS-sensitive / high-volume scraping at scale.** Mass extraction against an undocumented endpoint sits in a gray area and invites rate-limiting/blocking; for sanctioned bulk access you'd need a different (often paid/proxied) strategy. [推断]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [yt-dlp](yt-dlp.md) (`--write-auto-subs`) | ✅ | Choose yt-dlp when you need a broader downloader that can also pull subtitle tracks. | The heavyweight downloader can also pull subtitle tracks; far broader (media + subs from many sites) but heavier and CLI-oriented — this library is a focused, in-process Python call for transcripts only. |
| YouTube Data API v3 (Captions) | 未收录 | Choose YouTube Data API captions when you need the official contractual API and have the required ownership/OAuth. | Official and contractual, but requires OAuth and (for caption *download*) channel ownership — you generally can't pull arbitrary third-party caption text, which is exactly this library's niche. |
| [Selenium](../web-automation/browser-driver-frameworks/selenium.md) / Playwright scraping | 部分已收录 | Choose browser scraping when you must drive the real player despite the cost and brittleness. | A real browser survives some changes the player itself survives, but it is slow, resource-heavy, and brittle. This library avoids the browser entirely. Playwright is not indexed separately. |
| [Whisper](../media-processing/video-audio/speech-and-subtitles/whisper.md) (transcribe audio) | ✅ | Choose Whisper when you need to generate a transcript from audio with no caption track. | Generates a transcript from the audio when no caption track exists; far more compute and not timestamp-aligned to YouTube's own captions, but works on videos with captions disabled. |

## Tech stack

- **Language:** Python (supports a range of modern 3.x versions; packaged with Poetry).
- **Transport:** plain HTTP requests against YouTube's undocumented web-client transcript endpoint — no headless browser, no official API client.
- **Surface:** an object API (`YouTubeTranscriptApi().fetch(...)`, list/translate transcripts) plus formatters (JSON, WebVTT, SRT, CSV, plain text) and proxy config (Webshare + generic).

## Dependencies

- **Runtime:** Python 3.x and an HTTP stack (`requests`-class). No API key, no browser, no database.
- **Network:** outbound access to YouTube; for cloud/datacenter deployment, a (residential) **proxy** is effectively required to avoid IP blocks.
- **Optional:** Webshare proxy integration is first-class; generic HTTP/HTTPS proxy config is supported.
- **No services to run** — it's an in-process library you import.

## Ops difficulty

**Low to medium.** As a library there's nothing to deploy — `pip install`, import, call. The operational weight is entirely in *staying unblocked*: from a laptop/residential IP it's frictionless; from a server you must wire up and pay for rotating proxies, handle intermittent bans, and be ready to update the package (or wait for a fix) when YouTube changes the endpoint and calls start failing. Treat it as a dependency that can break on someone else's schedule and design retries/fallbacks accordingly.

## Health & viability

- **Responsiveness**: Grade B — median first-response time 14.8 hours across 4 qualifying issues/PRs.
- **Maintenance (2026-06).** Last push 2026-05; v1.2.4 released 2026-01 on a steady release cadence through 2025–2026 — **active**. Not archived. The 1.x line is a relatively recent, maintained API.
- **Governance / bus factor.** Single-maintainer project (jdepoix) with a long tail of contributors. Bus-factor risk exists, but the project has absorbed multiple YouTube-side breakages over its lifetime, which is the relevant survival signal here. [推断]
- **Age & Lindy verdict.** ~8 years old (created 2018-04) and still actively maintained ⇒ a **strong Lindy** signal — it has repeatedly survived YouTube changes, which is the best evidence of durability for a tool riding an undocumented endpoint.
- **Adoption.** ~7.8k stars and widely used as the transcript layer in LLM/RAG and research tooling — broad real-world adoption. [未验证]
- **Risk flags.** The structural risk is **not** governance or licensing (clean MIT) — it's the **undocumented-endpoint dependency**: a unilateral YouTube change can break it at any time, and cloud use now depends on third-party proxies.

## Caveats (unverified)

- [未验证] ~7.8k stars and v1.2.4 (2026-01) as of 2026-06 — figures are date-sensitive and indicative only.
- [未验证] Current state of age-restricted/login-walled access is a moving target tied to YouTube API changes; not confirmed working as of this date.
- [推断] ToS/legal posture of high-volume extraction is an inference about an undocumented endpoint, not legal advice or a confirmed YouTube policy citation.
- [推断] "Survives YouTube changes" durability is inferred from the maintenance history, not a guarantee about future breakage.
