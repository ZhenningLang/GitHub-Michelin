# nle-automation

> Category node. Programmatic control of an existing video editor: generate, mutate, and headlessly export a GUI NLE's own project (draft) files through the editor's engine — the automation layer beside the editor, not the editor itself.
> ← back to [media-processing](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Jianying Headless** | Use it when a macOS 剪映 professional workflow needs agent-generated *editable* drafts — real multi-track projects, plus native MP4 export from the app's own engine — but it is 5 days old, single-maintainer, tied to one app build, and non-commercial only. | D (4/6) | [→](jianying-headless.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Jianying Headless](jianying-headless.md) | ✅ | D (4/6) | Agent-written editable 剪映 drafts plus native export through the app's own engine; paid for with macOS 26 + one pinned 剪映 build, a per-machine compiled bridge, and a non-commercial license. |
| pyJianYingDraft | 未收录 | — | Pure Python draft writing without the app; it cannot render, and encrypted draft formats are out of its reach. |
| 剪映专业版 / CapCut (closed app) | 未收录 | — | Manual timeline craft with the vendor's own polish; no supported automation surface. |

## What belongs here

Tools whose primary job is to **drive an existing video editor programmatically** — writing or mutating the editor's native project/draft files, registering projects, or exporting through the editor's own engine (bridges, draft builders, scripting APIs). Not the editors themselves (see [video-editing](../video-editing/INDEX.md)), not codec/transcode toolchains (see [video-audio](../video-audio/INDEX.md)), not end-to-end generation pipelines that produce finished videos (see [video-production](../../video-production/INDEX.md)), and not GUI-driving desktop automation (see [desktop-automation](../../desktop-automation/INDEX.md)).
