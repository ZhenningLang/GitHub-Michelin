# editing-and-cutting

> Leaf of [video-audio](../INDEX.md). Programmatic editing and cutting: libraries that compose or trim a timeline in code, timeline engines you would build an editor on, and tools that decide *where* the cuts go.
> ← up to [video-audio](../INDEX.md) · root [route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **MoviePy** | Use it when a batch of clips must be cut, captioned and composited from a script and FFmpeg filter strings have become unreadable — but maintenance is coasting: no release since 2025-05 and the README asks for maintainers. | B (6/6) | [→](moviepy.md) |
| **MLT** | Use it when you are building a video editor or an automated pipeline that needs a frame-accurate timeline with tracks, filters and transitions, rendered through FFmpeg — but it is a framework, not an app; to just edit video, use Shotcut or Kdenlive. | B (6/6) | [→](mlt.md) |
| **Auto-Editor** | A CLI first-pass editor that labels every moment by loudness (or motion), cuts the silent stretches with a margin, and can export an importable timeline for Premiere/Resolve/Final Cut/ShotCut/Kdenlive instead of a rendered file. | A (6/6) | [→](auto-editor.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [MoviePy](moviepy.md) | ✅ | B (6/6) | Edits written as plain Python objects with every frame a NumPy array, in exchange for always re-encoding, throughput below raw FFmpeg, and slow responses from a very small maintainer group. |
| [Auto-Editor](auto-editor.md) | ✅ | A (6/6) | Pick it to derive the cut from the media (loudness or motion) and hand the result to an NLE as a timeline; pick [MoviePy](moviepy.md) when you need to execute a cut you already decided inside Python. |
| [MLT](mlt.md) | ✅ | B (6/6) | The timeline engine behind Shotcut and Kdenlive, with melt, XML and C/C++ entry points; you pay with no Python-first API, editorial rather than live-pipeline design, and one lead holding about 60% of commits. |
| [Concat](../../video-editing/concat.md) | ✅ | C (6/6) | Pick Concat when a human should cut in a GUI that happens to be scriptable; pick this leaf when the edit must run headless in a pipeline, because a desktop editor cannot be scheduled as a batch job. |

## What belongs here

Libraries and engines whose job is to *compose or decide an edit in code*: programmatic cutting/compositing APIs, timeline frameworks you build editors on, and pre-pass tools that choose where the cuts go. Not the codec/transcode layer underneath them (see [transcoding-and-pipelines](../transcoding-and-pipelines/INDEX.md)), not finished GUI editors (see [video-editing](../../video-editing/INDEX.md)), and not automation of someone else's editor (see [nle-automation](../../nle-automation/INDEX.md)).
