---
name: ffmpeg-python
slug: ffmpeg-python
repo: https://github.com/kkroening/ffmpeg-python
category: video-audio
tags: [ffmpeg, python, bindings, filter-graph, video, audio, transcoding]
language: Python
license: Apache-2.0
maturity: v0.2.x, last commit 2024-08 (coasting), 11k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2024-08-04T00:07:08Z
  default_branch: master
  default_branch_sha: df129c7ba30aaa9ffffb81a48f53aa7253b0b4e6
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:38:14Z
  overall: C
  overall_score: 2.0
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
        last_commit_age_days: 1534
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: ffmpeg-python
        dependent_repos_count: 5000
        downloads_last_month: 7960226
        graph_tier: B
        volume_tier: A
        cross_check_divergence: 1.05
        tier_source: registry
    longevity:
      grade: E
      raw:
        repo_age_days: 3418
        last_commit_age_days: 1534
        cohort: library
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
    responsiveness: { reason: no_window_signal }
    governance: { reason: unattributable }
---

# ffmpeg-python

Python bindings for FFmpeg that let you build complex filter graphs as chained Python expressions instead of hand-writing `-filter_complex` strings — it constructs the FFmpeg command line for you and shells out to the `ffmpeg` binary.

![ffmpeg-python — health radar](../../../assets/health/ffmpeg-python.svg)

## When to use

You're a Python developer doing media work — trimming clips, overlaying watermarks, concatenating segments, normalizing audio — and you've hit the wall where FFmpeg's `-filter_complex` syntax becomes write-only line noise. You want the trim-then-concat-then-overlay graph in your head expressed as readable code you can build up, branch, and reuse. You `pip install ffmpeg-python` and write `ffmpeg.input('in.mp4').hflip().output('out.mp4').run()`, or compose a real DAG: `concat(in.trim(...), in.trim(...)).overlay(overlay.hflip()).drawbox(...).output(...).run()`. The library turns that node graph into the gnarly `-filter_complex` invocation and runs it, so you stay in Python and keep filter logic version-controlled and testable instead of pasted into a shell string.

Its sweet spot is exactly *complex* filter graphs — the README's whole pitch is that other wrappers handle simple cases but lack complex-filter support. If you're scripting non-trivial transcoding/compositing pipelines in Python and already know FFmpeg's concepts, this is the ergonomic front end. [推断]

## When NOT to use

- **You don't have/ want FFmpeg installed.** This is a *thin wrapper that shells out* — it requires the `ffmpeg` binary present on the system; it does no encoding itself.
- **You're not in Python.** It's Python-specific; from another language you'd call FFmpeg directly or use that language's bindings.
- **You need in-process frame access / decoding.** It builds command lines for the FFmpeg CLI; for per-frame numpy access you'd want PyAV (libav bindings) or OpenCV instead. [未验证]
- **You need a long-term-maintained dependency.** The project is **coasting** — last commit 2024-08, with a large open-issue backlog (~525); load-bearing pipelines should account for slow upstream fixes. [推断]
- **Simple one-shot conversions.** If you just need `ffmpeg -i a.mp4 b.mp4`, a `subprocess` call (or a tiny helper) is fewer moving parts than a graph-building library.
- **You want FFmpeg version/feature abstraction.** It passes your graph to whatever `ffmpeg` is installed; filter availability/behavior is the binary's, so it won't shield you from FFmpeg version differences.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [FFmpeg](ffmpeg.md) (the CLI itself) | ✅ | Choose FFmpeg itself when you need the underlying engine and can manage filtergraph strings directly. | The underlying engine; maximal power and the canonical reference, but `-filter_complex` strings are unreadable for complex graphs — which is exactly what this wraps. |
| [PyAV](pyav.md) | ✅ | Choose PyAV when you need Pythonic bindings to the libav* libraries. | Pythonic bindings to the libav* libraries — in-process decode/encode and per-frame access, no shelling out; heavier to install, lower-level than a CLI graph builder. |
| [MoviePy](moviepy.md) | ✅ | Choose MoviePy when you need higher-level Python video editing with effects, compositing, text, and a friendlier API. | Higher-level Python video editing (effects, compositing, text) with a friendlier API; great for editing, less of a thin FFmpeg-graph mapping. |
| subprocess + raw ffmpeg | 未收录 | Choose subprocess + raw ffmpeg when you need zero dependency and total control. | Zero dependency and total control, but you hand-build and escape the `-filter_complex` strings yourself — the pain this library removes. |
| imageio-ffmpeg / fluent-ffmpeg | 未收录 | Choose imageio-ffmpeg or fluent-ffmpeg when you need other-language or narrower-scope FFmpeg wrappers. | Other-language or narrower-scope FFmpeg wrappers (Node's fluent-ffmpeg, Python imageio shim); similar shell-out model, different ergonomics. |

## Tech stack

- **Language:** pure Python; no compiled extension — it generates command-line arguments and uses `subprocess` to invoke FFmpeg.
- **Core idea:** a node-graph/DAG builder where `input`/filter/`output` nodes chain (fluent or functional style) and compile to one `-filter_complex` command line.
- **Surface:** filter functions mirroring FFmpeg filters, plus `.run()`, `.compile()` (inspect the args), and async/overwrite/quiet options.

## Dependencies

- **Runtime:** Python plus the **FFmpeg binary** installed and on PATH — the hard external dependency; the library is useless without it.
- **Python deps:** minimal (`future` historically for Py2/3); install via `pip install ffmpeg-python`.
- **No services/DB:** it's a client-side library that drives a local process; you bring the media files and the FFmpeg install.

## Ops difficulty

**Low for the library, "it depends" for FFmpeg.** Installing and using `ffmpeg-python` is trivial (`pip install`). The operational weight is FFmpeg itself: provisioning the binary (and the codecs/licenses you need) across environments, pinning a version so filter behavior is reproducible, and the CPU/GPU cost of the actual transcoding. The wrapper adds no runtime infrastructure, but it also gives you no isolation from FFmpeg version/codec differences — debugging a failed run often means reading the generated command line (`.compile()`) and reproducing it against your FFmpeg.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-06).** **Coasting.** Last commit 2024-08 (~2 years stale) and a large open-issue backlog (~525) — not archived and not dead, but clearly not actively driven. Treat it as feature-frozen. [推断]
- **Governance / bus factor.** Single-maintainer (`kkroening`) `User` repo. 11k stars on a one-author, stalling library is a **bus-factor flag**: popular and useful, but no team or org behind it. The high open-issue count alongside slow commits underlines this.
- **Age & Lindy verdict.** Created 2017-05, ~9 years old; the API is *stable and proven* (it just wraps FFmpeg's command construction, which doesn't change much), so it remains usable despite stalling — but "old + coasting" is weak Lindy, not strong. [推断]
- **Adoption & ecosystem.** Very widely used (11k stars, common in tutorials/StackOverflow answers); for simple-to-moderate graphs it's effectively a community standard, which buffers the slow maintenance. [推断]
- **Risk flags.** Maintenance velocity is the main one — open PRs/issues linger, so don't expect quick fixes; also the implicit FFmpeg-version coupling (the wrapper won't shield you). Apache-2.0 license is permissive and clear (verified from the repo). [推断]

## Caveats (unverified)

- [未验证] ~11k stars / 946 forks and ~525 open issues as of 2026-06; counts are date-sensitive and (for issues) reflect backlog more than danger.
- [未验证] No tagged GitHub releases were returned by the API this pass; tags (`v0.2.x`) exist on PyPI — version specifics should be confirmed against PyPI before pinning.
- [推断] "Coasting / feature-frozen" is inferred from the 2024-08 last-commit date plus the open-issue backlog, not from a maintainer statement.
- [未验证] The exact filter coverage, async support, and Python-version floor are summarized from README/general knowledge, not a manifest re-read.
- [未验证] PyAV/MoviePy capability contrasts are characterized from general ecosystem knowledge, not re-verified this pass.
