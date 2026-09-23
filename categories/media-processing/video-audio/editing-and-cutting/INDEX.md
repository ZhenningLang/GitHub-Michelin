# editing-and-cutting

> Leaf of [video-audio](../INDEX.md). Programmatic editing and cutting: libraries that compose or trim a timeline in code, timeline engines you would build an editor on, and tools that decide *where* the cuts go.
> ← up to [video-audio](../INDEX.md) · root [route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **MoviePy** | A Python library for programmatic video editing — cutting, concatenating, compositing, text overlays, and effects — that builds FFmpeg commands under the hood but presents a higher-level, friendlier API. | B (6/6) | [→](moviepy.md) |
| **MLT** | A multimedia framework for building non-linear video editors (NLEs) — timeline tracks, clips, transitions, filters, and compositing, with the actual codec work delegated to FFmpeg/libav underneath. Not a standalone editor; it's the engine that powers Shotcut and Kdenlive. | B (6/6) | [→](mlt.md) |
| **Auto-Editor** | A CLI first-pass editor that labels every moment by loudness (or motion), cuts the silent stretches with a margin, and can export an importable timeline for Premiere/Resolve/Final Cut/ShotCut/Kdenlive instead of a rendered file. | A (6/6) | [→](auto-editor.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [MoviePy](moviepy.md) | ✅ | B (6/6) | Pick it when the edit is a batch job you express in Python and you know the desired timeline; pick [Auto-Editor](auto-editor.md) when the timeline is the unknown (where are the silences?) rather than the input. |
| [Auto-Editor](auto-editor.md) | ✅ | A (6/6) | Pick it to derive the cut from the media (loudness or motion) and hand the result to an NLE as a timeline; pick [MoviePy](moviepy.md) when you need to execute a cut you already decided inside Python. |
| [MLT](mlt.md) | ✅ | B (6/6) | Pick it when you are *building* an editor and need a timeline model with transitions and filters; pick [MoviePy](moviepy.md) when you only need to render a fixed composition, because MLT is a framework, not a finished API. |
| [Concat](../../video-editing/concat.md) | ✅ | C (6/6) | Pick Concat when a human should cut in a GUI that happens to be scriptable; pick this leaf when the edit must run headless in a pipeline, because a desktop editor cannot be scheduled as a batch job. |

## What belongs here

Libraries and engines whose job is to *compose or decide an edit in code*: programmatic cutting/compositing APIs, timeline frameworks you build editors on, and pre-pass tools that choose where the cuts go. Not the codec/transcode layer underneath them (see [transcoding-and-pipelines](../transcoding-and-pipelines/INDEX.md)), not finished GUI editors (see [video-editing](../../video-editing/INDEX.md)), and not automation of someone else's editor (see [nle-automation](../../nle-automation/INDEX.md)).
