# ui-annotation

> Category node. The human points at the **running app's UI** — clicks, strokes, pins — and the annotation travels to a coding agent as structured evidence (selectors, source lines, diffs). Sibling of `supervision-surfaces`, which reviews what the agent *wrote*; here the review target is what the app *renders*.
> ← back to [agent-tooling](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Agentation** | Use it when your React app can carry a dev dependency and you want click-to-annotate with React component paths and dev-build `file:line`, synced to any terminal agent over MCP — the category leader by adoption, under a non-OSI license. | C (4/6) | [→](agentation.md) |
| **Vibe Annotations** | Use it when the person who sees the UI bug doesn't touch code: a Chrome-extension annotator plus a background server that feeds annotations to Claude Code / Cursor / Codex via MCP, with file-sharing for teammates. | C (5/6) | [→](vibe-annotations.md) |
| **Pointa** | Use it when "no app-code changes" is the rule and MIT is the license requirement — a Chromium extension with an MCP-speaking local server that also captures your Node backend's console logs into the same bug report. | C (5/6) | [→](pointa.md) |
| **earmark** | Use it when you want deterministic source evidence — build-time `file:line` stamping for Vite/Next/Svelte, CSS-rule resolution, and a pin-colored acknowledge/resolve loop — and can accept a 0-star, dormant project. | C (5/6) | [→](earmark.md) |
| **patch-mark** | Use it when you must annotate a page you don't own with two lines and zero dependencies, and you want the annotations framed to the agent as untrusted evidence with a read-only-by-default MCP surface. | C (5/6) | [→](patch-mark.md) |
| **markupkit** | Use it when your feedback is spatial — circles, arrows, strikethroughs and drag-to-move layout diffs handed over as structured deltas — and you're fine vendoring a dormant learning project to get it. | C (5/6) | [→](markupkit.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Agentation](agentation.md) | ✅ | C (4/6) | Deepest evidence (fiber, source lines) and the only one with mass adoption; costs a React dev dependency and a source-available license. |
| [Vibe Annotations](vibe-annotations.md) | ✅ | C (5/6) | Zero-touch breadth — designers annotate, agents consume — capped by what a content script can see. |
| [Pointa](pointa.md) | ✅ | C (5/6) | The MIT extension sibling with backend-log capture; smaller, quieter, six months old. |
| [earmark](earmark.md) | ✅ | C (5/6) | Deterministic build-time truth (stamped `file:line`, CSS rule lines) with no guarantee anyone keeps it alive. |
| [patch-mark](patch-mark.md) | ✅ | C (5/6) | Embed-anywhere web component with the niche's only explicit prompt-injection threat model; no source-path fidelity. |
| [markupkit](markupkit.md) | ✅ | C (5/6) | The only freehand/layout-diff input model — draw the fix instead of describing it — as a self-declared learning project. |
| IDE in-app browser pickers (Cursor, Antigravity, Windsurf) | not a repo | — | Zero install and already wired, but bound to that editor's preview tab and invisible to terminal agents. |

## What belongs here

Tools whose primary job is capturing **visual, element-level feedback from a running web UI** and delivering it to an AI coding agent as structured evidence. Not reviewing agent-authored artifacts (that's [`supervision-surfaces`](../supervision-surfaces/INDEX.md)), not agent-driven browsing or test automation (that's [`web-automation`](../../web-automation/INDEX.md)), and not screenshot bug-report SaaS (non-repos).
