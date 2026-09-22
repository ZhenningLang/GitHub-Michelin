# diagramming

> Category node. Generate diagrams from text (diagrams-as-code) for Markdown, docs, and the web.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Mermaid** | Use it when you want diagrams as version-controlled plain text (flowchart/sequence/ER) rendered in Markdown and docs — not pixel-precise layouts. | A (6/6) | [→](mermaid.md) |
| **flowchart.js** | Use it when you want simple flowcharts authored as git-diffable text and rendered to SVG in the browser — but it only renders, depends on aging Raphael.js, and chokes on complex diagrams. | B (5/6) | [→](flowchart-js.md) |
| **bpmn-js** | Use it when business analysts must author or view standards-correct BPMN 2.0 diagrams inside your web app — but its license mandates a non-removable bpmn.io watermark, so confirm terms before white-labeling. | A (5/6) | [→](bpmn-js.md) |
| **Excalidraw** | Use it when you want a hand-drawn-style collaborative whiteboard for sketching diagrams, wireframes, and architecture flows — but it stores JSON, not plain text, so it is not diffable in Git. | A (6/6) | [→](excalidraw.md) |
| **draw.io** | Use it when the diagram needs precise placement, official cloud/UML/BPMN shape libraries and a file a colleague can edit — its `.drawio` files are plain-text XML that diffs in git, and the app runs fully offline. | B (6/6) | [→](drawio.md) |
| **D2** | Use it when a versioned text diagram should render in CI with a layout engine you choose — MPL-2.0 is file-level copyleft, and no host platform renders it for you. | B (5/6) | [→](d2.md) |
| **PlantUML** | Use it when the DSL must cover many UML and non-UML diagram types and Java or server-side rendering is acceptable — check `LICENSES.md` before redistributing. | B (6/6) | [→](plantuml.md) |
| **PR Lens** | Use it when an agent-written diff is too large to orient yourself in by scrolling, and the change should be drawn — and redrawn on every push — inside the pull request. | C (6/6) | [→](pr-lens.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Mermaid](mermaid.md) | ✅ | A (6/6) | Plain-text diagrams rendered everywhere; trades layout control for portability. |
| [flowchart.js](flowchart-js.md) | ✅ | B (5/6) | Use it when you want simple flowcharts authored as git-diffable text and rendered to SVG in the browser — but it only renders, depends on aging Raphael.js, and chokes on complex diagrams. |
| [bpmn-js](bpmn-js.md) | ✅ | A (5/6) | Use it when business analysts must author or view standards-correct BPMN 2.0 diagrams inside your web app — but its license mandates a non-removable bpmn.io watermark, so confirm terms before white-labeling. |
| [Excalidraw](excalidraw.md) | ✅ | A (6/6) | Hand-drawn-style collaborative whiteboard for sketching diagrams and wireframes; stores JSON not plain text, so not diffable in Git. |
| [draw.io](drawio.md) | ✅ | B (6/6) | Best when placement must be exact, shapes must be the official cloud/UML sets, and the output is a file someone else will edit; choose Mermaid when the diagram should stay text, or Excalidraw when the sketch look is the point. |
| [D2](d2.md) | ✅ | B (5/6) | Declarative diagram language with swappable layout engines and multi-format output; MPL-2.0 is file-level copyleft, and it has far less host-platform rendering than Mermaid. |
| [PlantUML](plantuml.md) | ✅ | B (6/6) | Broad, strict UML coverage from a text DSL, usually rendered by Java or a server; read `LICENSES.md` — the API says LGPL-3.0 while upstream defaults to GPL-3.0-or-later with permissive build options. |
| [PR Lens](pr-lens.md) | ✅ | C (6/6) | Diagrams derived from a diff and posted as a PR comment, redrawn on every push; costs a model call per push and gives up hand-editable source. |
| Graphviz | 未收录 | — | The layout engine itself (dot/neato) is real and active (release 16.1.0, 2026-09-04) but its canonical repository is on GitLab; `tools/upstream_snapshot.py` and `tools/health.py` only read GitHub, so it cannot get an upstream snapshot or a health radar under the current contract. |

## What belongs here

Libraries/tools whose primary job is **turning text into diagrams** (diagrams-as-code) or rendering them. Not freeform whiteboard apps as the main use case, not UI animation (see `frontend-animation`).
