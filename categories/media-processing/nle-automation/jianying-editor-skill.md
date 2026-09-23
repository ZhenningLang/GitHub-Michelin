---
name: JianYing Editor Skill
slug: jianying-editor-skill
repo: https://github.com/luoluoluo22/jianying-editor-skill
category: nle-automation
tags: [agent-skill, jianying, capcut, video-editing, nle, python, automation]
language: Python
license: MIT
maturity: VERSION 1.7.0 in-repo (no tagged releases), 3,366 stars, 456 forks, created 2026-01-24, last push 2026-09-11 (as of 2026-09)
last_verified: 2026-09-21
type: skill-pack
upstream:
  pushed_at: 2026-09-11T09:36:48Z
  default_branch: main
  default_branch_sha: 32c56928ded4f9e2c2b80e099dc7abb793d2c30b
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:37:04Z
  overall: C
  overall_score: 2.0
  scored_axes: 3
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 11
        active_weeks_13: 3
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "N/A"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 242
        last_commit_age_days: 11
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.981
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: type_na }
    risk_license: { reason: license_unparsed }
  not_applicable:
    adoption: { reason: no_install_channel }
---

# JianYing Editor Skill

An agent skill that turns a sentence into a real 剪映 (Jianying Pro) draft — media, TTS voiceover, subtitles, music and effects laid onto tracks — and on Windows with 剪映 5.9 or older can also click export for you.

![JianYing Editor Skill — health radar](../../../assets/health/jianying-editor-skill.svg)

## When to use

You edit Chinese short-form video in 剪映专业版 and the slow part is not the creative decisions but the assembly: dropping the day's footage on a timeline, splitting the narration into subtitle lines, matching a voiceover, pulling a track off the 剪映 music library, applying a transition by name. You want your coding agent to do that assembly while you keep judging the result in 剪映 itself.

You install the skill into Claude Code / Cursor / Trae, describe the video in plain language ("把 D:\素材 剪成 Vlog，配轻快 BGM"), and the agent writes a Python script in your project that builds the draft; you then open 剪映 and render. The deciding tradeoff against [pyJianYingDraft](pyjianyingdraft.md): that one is a permissively licensed library you program against, with a release history and no bundled opinions; this one is a packaged agent layer — rules files the agent reads, plus ready workflows for TTS narration and subtitle alignment, cloud-asset search, screen recording with smart zoom, and film-commentary generation — at the cost of being a personal, version-coupled skill with no tagged releases. Against [Jianying Headless](jianying-headless.md), you give up the app's own headless export on macOS and current versions, and in exchange you get the higher-level "script to subtitled timeline" workflows that neither library ships.

## How it works

The skill is a folder of Markdown rules plus Python scripts, not an application. When you ask for an edit, the agent routes the request to the relevant `rules/*.md` file, then writes a business script **into your project root** (the skill forbids putting edit scripts inside its own directory) that bootstraps the wrapper through a path-discovery block and imports `JyProject` from `scripts/jy_wrapper.py`. From there the script is a normal authoring API: create the project at the right resolution, add media/audio/text segments with time ranges, generate TTS and time-aligned subtitles, search and apply effects, then call `project.save()`, which writes the draft into the 剪映 drafts folder and refreshes the draft state on disk. Nothing renders in Python — the pixels still come from 剪映, and the playbook's acceptance checklist is about draft structure (a video track exists, BGM sits on an audio track, narration has aligned subtitle segments) rather than output quality. The second mechanism is optional and platform-bound: unattended export drives the app's own UI through `uiautomation`, which is why the README keeps it on Windows with 剪映 5.9 or older and treats macOS as generate-then-export-by-hand.

![jianying-editor-skill — backbone user story](../../../assets/flow/jianying-editor-skill.svg)

<!-- flow-steps:begin (generated from flows/jianying-editor-skill.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Drop the repo into your AI editor's skills directory — `.claude/skills/jianying-editor`
2. **You**: Say what you want in plain language — footage, narration, subtitles, music — `帮我随便剪一个视频看看效果`
3. **JianYing Editor Skill**: Writes a Python script into your project root that imports the wrapper — `from jy_wrapper import JyProject`
4. **JianYing Editor Skill**: Lays media, TTS voiceover, subtitles and music onto tracks and saves a real 剪映 draft — `project.save()`
5. **You**: Open 剪映专业版 and render the assembled timeline there

**Value**: A multi-track 剪映 timeline assembled from one sentence, with subtitles and voiceover already aligned

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You use CapCut international, or 剪映 on mobile.** Only the desktop 剪映专业版 (JianyingPro) is targeted; the README says explicitly not to attempt the international app with this flow. Use [pyJianYingDraft](pyjianyingdraft.md), which at least documents a CapCut variant, or edit by hand.
- **You need the render produced without a human.** On macOS this generates drafts only; the Windows auto-export is UI automation against 剪映 5.9 or older and breaks when the app's controls move. For an unattended pipeline, render with [FFmpeg](../video-audio/transcoding-and-pipelines/ffmpeg.md) or [MoviePy](../video-audio/editing-and-cutting/moviepy.md), or use [Jianying Headless](jianying-headless.md) on macOS (non-commercial licence).
- **You need 剪映's realtime GPU features — 智能抠图, 美颜, ASR subtitle recognition, 一键成片.** The README lists these as out of reach because they are not driven by draft files.
- **You want a dependency you can pin and support.** There are no tagged releases to pin (the repo carries a `VERSION` file at 1.7.0), the project is ~8 months old, and one author owns essentially all of it. Put [pyJianYingDraft](pyjianyingdraft.md) (Apache-2.0, released, cross-platform) underneath anything you have to keep alive.
- **You need this to run in an isolated or unattended machine — or you handle confidential footage.** The skill installs desktop-control dependencies (`uiautomation`, `pynput`, `playwright`) and is meant to take over the screen for recording and export; voices come from `edge-tts`, which sends text to Microsoft's cloud service. Run it on a dedicated machine or VM with disposable data instead of a workstation holding unrelated work.
- **You are about to follow the README's Windows one-liner `irm is.gd/rpb65M | iex`.** Do not pipe a shortened URL into PowerShell: the target can change after the docs are frozen and there is nothing to review before execution. Clone the repository and read the scripts instead.
- **You want the agent to touch your creative project's source tree.** The workflow deliberately writes generated `.py` scripts into your working project's root; point it at a scratch directory if that tree is under review or under version control.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [Jianying Headless](jianying-headless.md) | ✅ | When the deliverable must come out of 剪映's own engine on macOS without a human, pick Jianying Headless; pick this skill when the work is "turn a brief into a subtitled, voiced timeline" and you will export by hand, because the two solve different halves and Headless is pinned to one app build under a non-commercial licence. | This skill carries the higher-level workflows (TTS, subtitle alignment, effect search, screen recording) but no unattended export on macOS; Jianying Headless gives native export at the price of a macOS-only, single-version, non-commercial bridge. |
| [pyJianYingDraft](pyjianyingdraft.md) | ✅ | When you are code-first, want Apache-2.0 and a released library to build on, pick pyJianYingDraft; pick this skill when a coding agent should drive the whole request and you want TTS, subtitle alignment and effect-name lookup already specified, because pyJianYingDraft leaves every one of those decisions to your code. | pyJianYingDraft is a stable library with no opinions; this skill is an opinionated agent playbook with no releases and a single maintainer. |
| [Auto-Editor](../video-audio/editing-and-cutting/auto-editor.md) | ✅ | When the requirement is only "cut the dead air and give me a timeline", pick Auto-Editor; pick this skill when the timeline also needs voiceover, subtitles, music and named effects assembled inside 剪映, because Auto-Editor never produces a 剪映 project. | Auto-Editor is a six-year-old single-binary CLI that exports NLE-importable cuts; this skill targets one editor's draft format and one ecosystem, with far less longevity behind it. |
| 剪映专业版 / CapCut (closed app) | 未收录 | When the edit is a one-off you will keep anyway, use the app; pick this skill when the same structure has to be produced repeatedly from a brief, because the app has no scriptable authoring surface. | The app gives vendor polish, every effect and realtime GPU features for free; the skill automates assembly but cannot call those realtime features and breaks when the app's format or UI shifts. |

## Health & viability

- **Maintenance (2026-09-21):** created 2026-01-24, last push 2026-09-11 — active, with the in-repo `VERSION` at 1.7.0 and a CHANGELOG, but **no tagged releases**, so there is no versioned artifact to pin or diff against.
- **Governance / bus factor:** one author (`luoluoluo22`, 114 contributions) with two single-commit contributors; a personal user account with no organisation, foundation or funding behind it. Bus factor 1 on a tool that automates other people's production work [推断].
- **Backing & Lindy:** ~8 months old with 3,366 stars, 456 forks and a marketing page (netlify FAQ, Bilibili walkthrough); the author built a video-sharing audience around it. Young and single-author — the weakest part of this page's profile, and the reason it belongs in a pipeline you can afford to lose [推断].
- **Adoption & ecosystem:** 3.4k stars at 8 months with an active Chinese-language tutorial surface (usage guide, agent playbook, minimal-command SOP, examples for Vlog / script-to-video / recording / commentary); 16 watchers and 4 open issues suggest a mostly consumer audience rather than contributors.
- **Risk flags:** the automation surface is the risk surface — draft-format coupling plus Windows UI Automation against a pinned old 剪映 build, both of which break on application updates; `requirements.txt` pins desktop-control packages (`uiautomation==2.0.20`, `pynput`, `playwright`) that need screen access; TTS text leaves the machine via `edge-tts`; the README's recommended Windows install is a shortened-URL `iex` pipe.

## Caveats (unverified)

- [未验证] Nothing on this page was executed: the draft output, TTS, subtitle alignment and export paths were read from the README, `SKILL.md`, `rules/*.md`, `examples/*.py` and the dependency manifest, not run against 剪映.
- [未验证] The platform matrix (Windows full support including auto-export on 剪映 5.9 or lower; macOS draft-generation only; no CapCut international; no mobile) is author-reported and version-bound; verifying it needs those exact 剪映 builds on both operating systems.
- [未验证] The claim that `uiautomation` export is "most stable" on 剪映 5.9 or lower is not reproducible here without a Windows host and that editor build; no CI or test evidence of it was found in the repository tree.
- [未验证] The security reading of the PowerShell one-liner is limited to its shape (`irm <shortened URL> | iex`): the content behind `is.gd/rpb65M` was not fetched or reviewed.
- [未验证] What `edge-tts` transmits, to which endpoint, and under which terms was not researched; only the pinned dependency version and the README's description of Microsoft voices were observed.
- [推断] The Apache-2.0-vs-MIT question resolves to MIT: the GitHub API reports `NOASSERTION`, but the `LICENSE` file is the MIT text naming `Copyright (c) 2026 luoluoluo22`; the `NOASSERTION` is treated as a classifier failure.
- [推断] Version coupling means a 剪映 release can break a workflow that previously worked, until the author re-adapts it — the README's own "剪映 5.9 及以下最稳" and "新版本可能受弹窗或控件变化影响" statements are instances of this pattern.
- [推断] Bus-factor and Lindy readings follow from the observed contributor counts, repository age and absence of tagged releases; no funding, sponsorship or organisational backing was found.
- [未验证] The netlify FAQ page and Bilibili walkthrough linked from the README were not read; anything they claim beyond the repository's own documentation is unaccounted for here.
