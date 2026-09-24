---
name: MoviePy
slug: moviepy
repo: https://github.com/Zulko/moviepy
category: editing-and-cutting
tags: [video, python, editing, compositing, ffmpeg, effects, text, animation]
language: Python
license: MIT
maturity: v2.0.x, active but slower than peak, ~13k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-03-07T02:47:15Z
  default_branch: master
  default_branch_sha: 7ffa4f00376237137a25fe1c777355c37753e9af
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:39:02Z
  overall: B
  overall_score: 3.17
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
        last_commit_age_days: 27
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: C
      raw:
        median_ttfr_hours: 283.7
        qualifying_issues: 9
        band: default
        window_offset_days: 2
        source: pr
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: moviepy
        dependent_repos_count: 5431
        downloads_last_month: 5642863
        graph_tier: B
        volume_tier: A
        cross_check_divergence: 1.29
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4789
        last_commit_age_days: 27
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.5
        top3_share: 1.0
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

# MoviePy


A Python library for programmatic video editing — cutting, concatenating, compositing, text overlays, and effects — that builds FFmpeg commands under the hood but presents a higher-level, friendlier API.


![MoviePy — health radar](../../../../assets/health/moviepy.svg)

## When to use

You're a data scientist or content-automation engineer who needs to generate video clips programmatically — stitching together segments, adding animated text overlays, applying crossfade transitions, or producing dozens of variant thumbnails from a template. You know FFmpeg exists but you don't want to hand-write `-filter_complex` strings for every operation. You `pip install moviepy`, write `VideoFileClip("input.mp4").subclip(0, 10).fx(vfx.fadeout, 2).write_videofile("output.mp4")`, and the library handles the FFmpeg invocation, frame extraction, and re-assembly behind a Pythonic API. Its sweet spot is batch video editing and simple compositing pipelines where readability and rapid iteration matter more than real-time performance.

## When NOT to use

- **Real-time or streaming processing.** MoviePy is strictly batch/offline; it reads files, processes frames, and writes output — not suitable for live streams or low-latency pipelines.
- **Large-file performance-critical workflows.** It writes intermediate frames to disk (though v2 improved this), making it slower than native FFmpeg for big files or high-resolution footage.
- **You need the absolute fastest transcoding.** Raw FFmpeg CLI or dedicated transcoders like HandBrake will beat MoviePy on speed.
- **You're not in Python.** MoviePy is Python-specific.
- **You need advanced codec tuning or exotic format support.** MoviePy abstracts FFmpeg but may not expose every flag or newest codec option.
- **You need a dependency with active maintenance velocity.** Community activity is slower than its peak; some forks exist but the mainline has a reduced commit cadence.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [FFmpeg](../transcoding-and-pipelines/ffmpeg.md) | ✅ | Choose FFmpeg when you need the universal engine, maximum speed, or full codec control — at the cost of hand-writing commands. | The underlying universal engine; maximum power and speed, but CLI syntax is steep and `-filter_complex` is write-only for complex graphs. |
| [ffmpeg-python](../transcoding-and-pipelines/ffmpeg-python.md) | ✅ | Choose ffmpeg-python when you want Pythonic DAG construction of FFmpeg filter graphs, not higher-level video editing abstractions. | Thin Python wrapper around FFmpeg CLI filter graphs; closer to FFmpeg's concepts, less "video editing" feel than MoviePy. |
| [PyAV](../transcoding-and-pipelines/pyav.md) | ✅ | Choose PyAV when you need in-process libav* bindings for per-frame access or custom decode/encode pipelines. | Pythonic bindings to libav* libraries; in-process frame access, no shelling out; heavier setup, lower-level than MoviePy. |
| [HandBrake](../transcoding-and-pipelines/handbrake.md) | ✅ | Choose HandBrake when you need a GUI or preset-driven batch encoder with built-in quality tuning, not programmatic editing. | Desktop/preset batch encoder with excellent quality presets; not a programmable editing library. |
| [GStreamer](../transcoding-and-pipelines/gstreamer.md) | ✅ | Choose GStreamer when you need a streaming media framework with pipeline graphs and plugin ecosystem, not simple Python scripting. | Industrial-strength streaming media framework; steep learning curve, overkill for simple clip editing. |
| [MLT](mlt.md) / Shotcut | 部分已收录 | Choose MLT when you need a professional non-linear editing engine with timeline support, not a quick Python script. | Professional NLE engine (MLT) and GUI (Shotcut); heavy, timeline-oriented, not lightweight scripting. |
| OpenCV | 未收录 | Choose OpenCV when computer vision or frame-level image processing is the primary task, with video as a side effect. | Computer vision first; can read/write video but lacks editing concepts like clips, transitions, or compositing layers. |

## Tech stack

- **Language:** Python 3.7+; pure Python with some C extensions via dependencies.
- **Core idea:** A high-level video editing API where `VideoClip`, `AudioClip`, and `CompositeVideoClip` objects chain operations (cut, concatenate, overlay, apply effects) and compile to FFmpeg commands under the hood.
- **Surface:** `VideoFileClip`, `ImageClip`, `TextClip`, `CompositeVideoClip`, `concatenate_videoclips`, plus `fx` effects and custom `clip.fl` frame filters.

## Dependencies

- **Runtime:** Python 3.7+ plus **FFmpeg** (must be installed and on PATH) and **ImageMagick** (for text rendering and some effects).
- **Python deps:** NumPy (array operations), Pillow (image I/O), plus imageio and its ffmpeg plugin; install via `pip install moviepy`.
- **No services/DB:** Client-side library; you bring the media files and the external binaries.

## Ops difficulty

**Low.** Installing MoviePy is `pip install moviepy` plus ensuring FFmpeg and ImageMagick are present. The operational weight is in the external binaries: FFmpeg version compatibility (some filters behave differently across versions), ImageMagick policy/security settings (e.g., text rendering can be blocked by policy.xml), and the disk I/O from intermediate frame writes. No servers, databases, or network services to run.

## Health & viability

- **Maintenance (2026-07).** Slower than peak. v2.0.x released and the project is not dead, but commit cadence has dropped from its heyday; treat it as maintained but not rapidly evolving. [推断]
- **Governance / bus factor.** Originally created by Zulko (single author); the repo has attracted contributors over ~10 years but lacks a dedicated foundation or vendor team. A community fork ecosystem exists. [推断]
- **Age & Lindy verdict.** Created ~2014, ~12 years old; the API is stable and widely taught, giving it moderate Lindy signal — but "old + slower-than-peak" is a mixed signal, not strong. [推断]
- **Adoption & ecosystem.** Very widely used in tutorials, data-science notebooks, and content automation; ~13k stars and broad StackOverflow presence mean it's a de-facto standard for Python video editing, which buffers the slower maintenance. [推断]
- **Risk flags.** The main flag is maintenance velocity — fixes and new features arrive more slowly than in 2015–2020; also the FFmpeg and ImageMagick version coupling means breaking changes in those binaries can affect MoviePy behavior. MIT license is permissive and clear. [推断]

## Caveats (unverified)

- [未验证] ~13k stars and exact fork count as of 2026-07; star counts are date-sensitive.
- [推断] "Slower than peak" and reduced commit cadence are inferred from general ecosystem observation and GitHub activity trends, not a maintainer statement.
- [未验证] The exact scope of v2.0 improvements to intermediate frame handling is summarized from release notes, not benchmarked this pass.
- [未验证] Community fork names and activity levels are referenced from general knowledge, not re-verified against live repos.
- [未验证] ImageMagick policy.xml blocking behavior is a known class of issue but not re-tested on current versions.
