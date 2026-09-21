---
name: sharp
slug: sharp
repo: https://github.com/lovell/sharp
category: image-processing
tags: [media-processing, sharp, library]
language: JavaScript
license: Apache-2.0
maturity: active, ~32,428 stars (as of 2026-07)
last_verified: 2026-07-06
type: library
upstream:
  pushed_at: 2026-07-06T10:07:39Z
  default_branch: main
  default_branch_sha: 6c99758f0557607459dec23350fbf8a098c2b61d
  archived: false
health:
  schema: 1
  computed_at: 2026-07-06T15:48:05Z
  overall: A
  overall_score: 3.5
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 3.6
        qualifying_issues: 16
        band: default
        window_offset_days: 12
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: sharp
        dependent_repos_count: 178353
        downloads_last_month: 272834084
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.01
    longevity:
      grade: A
      raw:
        repo_age_days: 4704
        last_commit_age_days: 0
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 8
        top1_share: 0.844
        top3_share: 0.972
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---
# sharp

High performance Node.js image processing, the fastest module to resize JPEG, PNG, WebP, AVIF and TIFF images. Uses the libvips library.

![sharp — health radar](../../../assets/health/sharp.svg)

## When to use

You're choosing open-source infrastructure for a task that falls into `media-processing` and you need a real repository to evaluate, not just a product name from a comparison table. You reach for sharp when its upstream description matches the job and when adopting an existing project is preferable to writing custom glue from scratch.

This first-pass page exists because sharp was repeatedly useful as a comparison candidate in the atlas backlog. Use it as an intake-backed starting point: verify the upstream README and license, then compare it against the linked neighboring pages before committing to the dependency.

## How it works

sharp is a Node package; the pixel work is done underneath by the C library **libvips**, which sharp wraps in a chainable JavaScript API. `npm install` downloads a prebuilt binary for your platform, so most macOS / Windows / Linux machines need nothing else installed. Your part is small: hand an image (a file path or an in-memory Buffer) to `sharp()`, chain what you want done (resize, convert format, rotate), and say whether the result goes to a file or a Buffer; decoding, resizing and encoding are all sharp's. There is no service and no config — it is just a function library.

![sharp — backbone user story](../../../assets/flow/sharp.svg)

<!-- flow-steps:begin (generated from flows/sharp.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install; a prebuilt binary for your platform is downloaded — `npm install sharp`
2. **You**: Hand sharp an image: a file path or an in-memory Buffer — `sharp('input.jpg')`
3. **You**: Chain the operations you want — `.resize({ width: 200 }).jpeg({ mozjpeg: true })`
4. **You**: Say where the output goes — `.toFile('out.webp') / .toBuffer()`
5. **sharp**: libvips decodes the source image
6. **sharp**: Resizes and converts, handling colour spaces and alpha correctly
7. **sharp**: Encodes to the target format and returns a file or Buffer

**Value**: A few lines turn large images into small web-friendly ones; the README claims 4–5x faster resizing than ImageMagick

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You need a fully reviewed, deeply researched atlas page today.** Use a more mature in-index page from the comparison table until this intake page has been semantically reviewed with the upstream docs.
- **The GitHub metadata flags a blocker for your environment.** If license, archival status, or maintenance cadence is load-bearing, choose a better-verified alternative in this category instead of relying on sharp.
- **Your task needs a narrower or more specialized substitute.** Prefer the existing page whose `When NOT to use` section names your exact constraint; this page is a broad first-pass entry.
- **You cannot afford upstream churn or operational unknowns.** Pick an older in-index project with a clearer Lindy record and documented ops profile.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [ffmpeg-python](../video-audio/transcoding-and-pipelines/ffmpeg-python.md) | ✅ | When you need the established in-index option for this category, compare it against sharp before switching. | sharp is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose sharp only after verifying the repo-specific caveats below. |
| [FFmpeg](../video-audio/transcoding-and-pipelines/ffmpeg.md) | ✅ | When you need the established in-index option for this category, compare it against sharp before switching. | sharp is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose sharp only after verifying the repo-specific caveats below. |
| [ffsubsync](../video-audio/speech-and-subtitles/ffsubsync.md) | ✅ | When you need the established in-index option for this category, compare it against sharp before switching. | sharp is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose sharp only after verifying the repo-specific caveats below. |
| [GStreamer](../video-audio/transcoding-and-pipelines/gstreamer.md) | ✅ | When you need the established in-index option for this category, compare it against sharp before switching. | sharp is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose sharp only after verifying the repo-specific caveats below. |
| Hand-rolled integration | 未收录 | Choose custom code only when the needed scope is tiny and the maintenance burden is clearly lower than adopting this repo. | Custom code avoids a dependency but loses the upstream project, ecosystem, and documented tradeoffs captured here. |

## Tech stack

- **Primary language:** JavaScript per GitHub metadata.
- **Repository:** `lovell/sharp`.
- **Project shape:** categorized as `library` for atlas routing; verify upstream architecture before treating this as a stable API contract.
- **Upstream state:** default branch `main`, last pushed `2026-07-06T10:07:39Z`, archived `false`.

## Dependencies

- **Runtime dependencies:** not exhaustively verified in this intake pass; inspect the upstream dependency manifest before production use.
- **External services:** not exhaustively verified in this intake pass; check whether the project requires databases, queues, cloud APIs, browser runtimes, GPUs, or model-provider credentials.
- **Operational input:** at minimum, you depend on the GitHub repository and its release/update process.

## Ops difficulty

**Unknown to medium until the upstream docs are reread.** Library-style entries may be low effort to try but still need version pinning and upgrade review. App/service/framework entries can carry hidden database, worker, storage, auth, browser, GPU, or cloud-provider requirements, so treat this first-pass entry as an intake marker rather than an ops runbook.

## Health & viability

- **Maintenance snapshot:** GitHub reports `archived=false` and `pushed_at=2026-07-06T10:07:39Z` as of 2026-07-06.
- **Adoption snapshot:** ~32,428 GitHub stars as of 2026-07; stars are only a noisy adoption signal.
- **License snapshot:** `Apache-2.0` from GitHub API; inspect repository license files when the license matters.
- **Lindy and governance:** not fully reviewed in this intake pass. Treat org ownership, project age, release cadence, and bus factor as open review items before long-term adoption.
- **Risk flags:** first-pass page generated from backlog metadata.

## Caveats (unverified)

- [未验证] This is a first-pass intake page generated from GitHub metadata and the 2026-07-06 backlog; before relying on it for a high-stakes selection, reread the upstream README, docs, license file, and release notes.
- [推断] The comparison table uses nearby in-index pages as a starting point; a later semantic review should replace generic neighboring rows with the closest true substitutes.
