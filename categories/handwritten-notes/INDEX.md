# handwritten-notes

> Category node. Write by hand and mark up photos or PDFs with a stylus — ink-first notebook apps you build or run yourself, not typed-text knowledge bases.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Loose Leaf** | Use it as the complete source of a shipped iPad ink app — strokes that split onto imported photos, scissors that cut them, gesture-driven page stacks — to study or fork; not as a maintained daily note app. | D (3/6) | [→](loose-leaf.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Loose Leaf](loose-leaf.md) | ✅ | D (3/6) | Full MIT source of a once-commercial iPad notes app with unusual scrap and scissor mechanics; pays with an OpenGL ES drawing core, vendored dead SDKs and no maintainer activity since 2023. |
| Saber | not indexed | — | Maintained cross-platform handwriting app (iPad, Android, desktop) under GPL-3.0; the choice for daily notes rather than for studying UIKit internals. |
| Xournal++ | not indexed | — | Long-lived desktop handwriting and PDF annotation (GTK, Linux/macOS/Windows) with Wacom support; no iPad build. |
| Rnote | not indexed | — | Rust/GTK4 sketching and handwritten-notes app for desktop, PDF import and export; no iPad build. |
| Apple PencilKit | not a repo | — | Apple's closed framework for adding Pencil ink to your own iOS app; maintained by Apple, but no scraps, scissors or page model. |

## What belongs here

Apps and app source trees whose primary job is **handwriting with a pen or finger**: ink notebooks, stylus sketching, and marking up imported photos or PDFs by hand.

Not here:

- **Typed-text notes and second brains** (Markdown vaults, outliners) — see `knowledge-base`.
- **Diagram and whiteboard canvases** built from shapes rather than ink — see `diagramming` or `design-editors`.
- **Programmatic PDF editing** (merge, sign, OCR) — see `pdf-tools`.
