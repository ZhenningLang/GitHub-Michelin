---
name: Auto-Editor
slug: auto-editor
repo: https://github.com/WyattBlue/auto-editor
category: video-audio
tags: [video-editing, silence-removal, audio-analysis, cli, nle-export, first-pass]
language: Nim
license: Unlicense
maturity: v31.6.0 (released 2026-09-06), 5,296 stars, 656 forks, created 2020-04-30, last push 2026-09-19 (as of 2026-09)
last_verified: 2026-09-21
type: tool
upstream:
  pushed_at: 2026-09-19T14:52:15Z
  default_branch: master
  default_branch_sha: 7796222139b5d87fe32247f8a60a931b02006db5
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:37:50Z
  overall: A
  overall_score: 3.5
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
        last_commit_age_days: 3
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 2.5
        qualifying_issues: 4
        band: relaxed_solo
        window_offset_days: 9
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: auto-editor
        dependent_repos_count: 4
        downloads_last_month: 13810
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
        homebrew_installs_90d: 684
        homebrew_tier: B
        release_downloads: 85737
        release_assets: 219
        release_tier: D
        signal_basis: homebrew+releases
        tier_source: homebrew+releases
    longevity:
      grade: A
      raw:
        repo_age_days: 2336
        last_commit_age_days: 3
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.999
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Unlicense
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Auto-Editor

A command-line first-pass editor: it analyzes a recording's loudness (or motion), cuts the silent stretches for you, and can hand the result back as an editable timeline for Premiere, Resolve, Final Cut, ShotCut or Kdenlive.

![Auto-Editor — health radar](../../../assets/health/auto-editor.svg)

## When to use

You have hours of talking-head footage — a stream, a tutorial series, a podcast recording, a screen-share walkthrough — and the first edit is the part nobody wants to do: finding and deleting the dead air. You are not trying to make a creative cut yet; you are trying to get to a tight file so the creative work starts from something watchable.

You run `auto-editor recording.mp4` and get a tightened file back, no project, no timeline, no editor open. The deciding tradeoff against raw [FFmpeg](ffmpeg.md): FFmpeg can do every one of these cuts, but you have to author the filter graph and the decision logic yourself (`silencedetect`, then map timestamps into a `select` expression); Auto-Editor ships that decision layer — the loudness labelling, the margin around speech, the "cut this class, keep that class" model — and also writes the timeline XML for the NLEs you already use. Against [MoviePy](moviepy.md), you get a finished CLI instead of a library you have to program; against [HandBrake](handbrake.md), you get editing decisions instead of transcoding presets.

## How it works

Auto-Editor decodes the file itself (the official binaries bundle their own media stack, so no separate FFmpeg install is required) and then walks the media in small time slices, computing one loudness value per slice. Each slice gets an integer label — `0` for silent, `1` for active — and the default rule (`--edit audio:threshold=0.04,stream=all`) keeps only the active ones. Cutting is not brutal: the `--margin` option, defaulting to `0.2s`, re-inserts a little silence before and after each kept span so speech does not start mid-word or clip. You can move the decision to motion instead (`--edit motion:threshold=0.02`), combine methods (`--edit "(or audio:0.03 motion:0.06)"`), or add further label classes with `--edit:2` / `--when:2` to make some passages play faster rather than get cut. The other half of the tool is the exit ramp: `--export premiere` (or `resolve`, `final-cut-pro`, `shotcut`, `kdenlive`, `clip-sequence`) writes an importable timeline instead of a rendered file, so you can start from its cut and finish by hand. Your side of the line is the policy — which method, which threshold, what to output; its side is finding the silences and doing the cutting.

![auto-editor — backbone user story](../../../assets/flow/auto-editor.svg)

<!-- flow-steps:begin (generated from flows/auto-editor.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Get the official binary onto your PATH — `brew install auto-editor`
2. **You**: Point it at the recording you do not want to scrub through — `auto-editor path/to/your/video.mp4`
3. **Auto-Editor**: Scores every moment by loudness and labels it silent or active
4. **Auto-Editor**: Cuts the silent spans, leaving a margin around speech so cuts feel natural
5. **Auto-Editor**: Writes the edited file itself — no editor window, no timeline session
6. **You**: When you still want to finish by hand, export the timeline instead — `auto-editor example.mp4 --export premiere`
7. **Auto-Editor**: Emits a timeline file the NLE imports as an editable sequence

**Value**: The boring first pass over a long recording — done before you open an editor

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You need frame-accurate creative editing, multiple tracks, or compositing.** This makes one decision (silent vs active) over one input. Use an NLE for the real cut — [Concat](../video-editing/concat.md) or [OpenCut](../video-editing/opencut.md) — or [MoviePy](moviepy.md) when the edit lives in Python.
- **Your audio has no silence to remove — music videos, ambient footage, dense dialogue with a room tone floor.** Loudness labelling has nothing to work with. Switch to `--edit motion`, or use [FFmpeg](ffmpeg.md) and cut by hand.
- **You need the tool as a library inside a service.** Auto-Editor is a CLI with its own binary; embed [MoviePy](moviepy.md), [PyAV](pyav.md) or [ffmpeg-python](ffmpeg-python.md) instead.
- **Your real job is format conversion or shrinking a file, not editing it.** Use [HandBrake](handbrake.md) (presets, hardware encoders) or [FFmpeg](ffmpeg.md).
- **You want the cut decided by speech or scene semantics, not volume.** ASR-driven editing is a different tool class — [Whisper](whisper.md) gives you the transcript, but the cut logic is yours.
- **You distribute software through a managed channel that rejects unsigned binaries.** The official releases are unsigned, and the docs' own advice is to ignore the macOS/Windows "unknown developer" warnings; `brew install auto-editor` is the cleanest path.
- **You are following an old tutorial that says `pip install auto-editor`.** The project states the CLI is no longer published on pip; the PyPI copy is stale, so the pip route silently gives you an old version. Install from the Releases page or Homebrew.
- **You need the hosted "online" or desktop application.** Those products reuse this repository's assets but carry their own proprietary license — the repo's public-domain grant does not cover them.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [FFmpeg](ffmpeg.md) | ✅ | When the edit is one-off and you already think in filter graphs, pick FFmpeg; pick Auto-Editor when the whole job is a repeating "remove the dead air and give me a timeline" pass, because FFmpeg gives you raw primitives and no notion of a silence policy or an NLE hand-off. | Auto-Editor is one binary with the decisions pre-made and XML export built in; FFmpeg is universal and scriptable but puts the labelling, margin and timeline-building logic on you. |
| [MoviePy](moviepy.md) | ✅ | When you are already inside a Python pipeline that composites and re-encodes, pick MoviePy; pick Auto-Editor when the deliverable is a cut of a long recording and you would rather not write the audio-analysis code, because MoviePy is a general editing API and does not ship silence detection. | Auto-Editor's CLI does exactly one job with a labelled-segment model and no code; MoviePy is a library that can express any edit but gives you no built-in policy. |
| [HandBrake](handbrake.md) | ✅ | When you need to transcode a finished file into a distribution format, pick HandBrake; when you need to decide what stays in the file at all, pick Auto-Editor, because HandBrake's presets cannot detect or remove silence. | HandBrake has hardware encoders and battle-tested presets; Auto-Editor decides content rather than format and does not compete on encoding options. |
| Descript | 未收录 | When the editing is text-driven (edit the transcript, the video follows) and a subscription plus cloud upload is acceptable, pick Descript; pick Auto-Editor when the footage must stay local and the pipeline must be scriptable, because Descript is closed SaaS with no CLI you can wire into a batch. | Descript gives a polished interactive text-editing experience; Auto-Editor gives a local, free, unattended pass that leaves an editable timeline in your own NLE. |
| 剪映专业版 / CapCut (closed app) | 未收录 | When the first pass is a one-off and you want vendor polish, do it in the app; pick Auto-Editor when the same trim has to run unattended on every recording you produce, because the app has no supported batch entry point. | The app is free and visual; Auto-Editor is unattended and scriptable but blind to anything except loudness or motion. |

## Tech stack

- Written in **Nim**; the repository is a Nim project built through `nimble` (`nimble makeff` to fetch/build dependencies, `nimble make` for a static binary, `nimble brewmake` for a dynamic build against system FFmpeg libraries).
- `src/` holds the analysis and cut engine (timeline model, edit methods, export backends); `scripts/` and `resources/` hold build and packaging assets.
- `skills/` directory with four agent skills (`auto-editor`, `auto-editor-effects`, `auto-editor-export`, `auto-editor-transcribe`), installed via `npx skills add WyattBlue/auto-editor`.
- Export backends for Premiere XML, DaVinci Resolve, Final Cut Pro, ShotCut and Kdenlive, plus a raw clip-sequence output.
- Optional integration with `yt-dlp` so URLs can be used directly as inputs.

## Dependencies

- **A runtime: none.** The official release binaries are statically built and unsigned; rename the download to `auto-editor` (`auto-editor.exe` on Windows), `chmod +x` on macOS/Linux, and put it on your `PATH`.
- On macOS you can install with `brew install auto-editor`; Arch users have the AUR package (`yay -S auto-editor`). The docs warn that `apt` packages are very old.
- **Building from source** is the heavy path: `nim`, `nimble`, `cmake`, `meson`, `ninja`, and either the static route (`nimble makeff` / `nimble make`) or system FFmpeg libraries for the dynamic one. Windows builds go through WSL.
- **`yt-dlp` is optional** — install it through whatever package manager you like and Auto-Editor will accept URLs as inputs.
- No Python, no Node, no server, no GPU, no cloud account.

## Ops difficulty

**Low.** It is a single binary you run and forget: no daemon, no config file to keep in sync, no database, no service to monitor. The friction is distribution rather than operation — unsigned binaries trip Gatekeeper on macOS and SmartScreen on Windows (unzip, `chmod +x`, clear the warning), and the stale pip package means the two documented install paths disagree about which version you get, so pin the version your pipeline was tested against and update deliberately rather than following whatever `pip` finds.

## Health & viability

- **Maintenance (2026-09-21):** created 2020-04-30, last push 2026-09-19, releases roughly monthly (31.6.0 on 2026-09-06; 31.5.0, 31.4.2, 31.4.0 through July–August). Over six years of continuous, still-active development.
- **Governance / bus factor:** effectively one person — `WyattBlue` accounts for ~2,506 commits against 8 for the next contributor. Bus factor 1 is the main structural risk for anything depending on it long-term [推断].
- **Backing & Lindy:** no foundation or company; a solo project with a website, blog and Discord. Age × still-active is the strongest signal here: six years old and still releasing monthly is a good Lindy profile by this index's prior.
- **Adoption & ecosystem:** 5,296 stars, 656 forks and a documentation set (options reference, cookbook, action docs) deeper than most single-maintainer tools. The radar still scores adoption D, and the measured numbers say why: the only registry signal left is the stale PyPI package (18,055 downloads in the last month, 4 dependent repositories, graph tier D), while the install base that moved to binaries, Homebrew and the AUR is invisible to registry metrics — so treat "how many people actually run this" as unmeasured rather than settled by stars [推断]. The recorded open-issue count is 0, which reads more like an aggressively curated tracker than a measure of popularity [推断].
- **Risk flags:** pip distribution discontinued while old copies remain on PyPI (a silent stale-version trap); release binaries are unsigned; release artifacts "may be under various open source licenses" even though the repository is Unlicense, so do not assume the binaries carry the same public-domain grant; the commercial online/app products are separately licensed.

## Caveats (unverified)

- [未验证] Nothing on this page was executed: the CLI, the cutting quality, and the exported timelines were read from the README, the install documentation and the repository tree, not run on media.
- [未验证] How faithfully each `--export` backend reproduces cuts inside Premiere / Resolve / Final Cut / ShotCut / Kdenlive is untested here; importing a generated timeline into each NLE is the check.
- [未验证] All quality judgments about loudness- or motion-based cutting (how well it separates speech from room tone, how `--margin` feels in practice) are author descriptions and were not measured.
- [未验证] The claim that the official binaries bundle everything needed for decoding was read from the install docs ("build statically" vs "needs ffmpeg libs") and not verified by running a binary on a machine without FFmpeg.
- [未验证] The four `skills/` entries were observed to exist in the repository tree; whether `npx skills add WyattBlue/auto-editor` installs and works was not tested.
- [推断] Bus factor 1 (one author at ~2,506 commits vs 8 for the runner-up) is the abandonment risk; the monthly release cadence argues against it materializing soon.
- [推断] "0 open issues" is inferred to reflect active curation rather than absence of users; issue history was not sampled.
- [未验证] The PyPI package (latest 29.3.1) is presumed stale relative to the GitHub releases (31.6.0) because the docs state pip publication stopped; the difference in behaviour between the two versions was not compared.
- [未验证] The registry figures quoted in Health & viability (18,055 PyPI downloads in the last month, 4 dependent repositories, graph tier D, computed 2026-09-21) are point-in-time snapshot values from the scoring tool, not a trend; they will age and should be re-read with `tools/health.py` rather than quoted later.
