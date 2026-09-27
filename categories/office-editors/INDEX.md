# office-editors

> Category node. **Interactive** office editing on the web: editor SDKs and spreadsheet-like data grids you embed into your own product, plus document servers and spreadsheet platforms you self-host and wire in. The difference from [office-automation](../office-automation/INDEX.md): that category *writes the file*; this one *gives a human (or an agent) a surface to edit it in*.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Univer** | Use it when you are *building a product* that needs an embedded spreadsheet/document editor you can restyle and extend plugin-by-plugin under Apache-2.0 — but collaboration, xlsx import/export, charts and pivot tables are paid Pro, the 1.0 line shipped in 2026-09, and one vendor owns the roadmap. | A (6/6) | [→](univer.md) |
| **Fortune Sheets** | Use it when a React app needs a quick MIT-licensed Excel-like grid with an op stream for your own persistence — but it is a Luckysheet descendant with the same feature ceiling, no built-in xlsx I/O, and no commit since 2025-12-15. | B (5/6) | [→](fortune-sheets.md) |
| **Handsontable** | Use it when an internal data-entry grid needs 15 years of hardened spreadsheet UX (validation, conditional formatting, 400 formulas) and you have budget for a commercial license — for free commercial use, pick Jspreadsheet CE or Fortune Sheets instead. | A (5/6) | [→](handsontable.md) |
| **Jspreadsheet** | Use it when you want the lightest MIT vanilla-JS grid with typed columns and Excel copy/paste — and you accept the community edition is the free tier of a Pro product, with GitHub releases trailing the npm package. | B (5/6) | [→](jspreadsheet.md) |
| **Grist** | Use it when a team wants a *product* — a self-hosted spreadsheet whose columns are typed database fields with Python formulas, per-row permissions and webhooks — not a component to embed; a French-government-backed Apache-2.0 core with an active monthly release line. | A (5/6) | [→](grist.md) |
| **ONLYOFFICE Docs** | Use it when your drive/CRM/LMS needs "click a .docx → full editor with real-time co-editing" in one Docker container with true OOXML fidelity — but it is AGPL, the Community edition recommends ≤20 concurrent connections, and the GitHub repo is packaging only. | B (6/6) | [→](onlyoffice-documentserver.md) |
| **Collabora Online** | Use it when you run (or integrate with) a WOPI-capable file platform like Nextcloud and want the LibreOffice rendering engine in the browser — but active development lives on Gerrit, not this GitHub repo, and there is no UI SDK here to embed. | A (5/6) | [→](collabora-online.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Univer](univer.md) | ✅ | A (6/6) | The embed-and-build SDK: canvas rendering, formula engine, sheets+docs in one Apache-2.0 package, headless in Node — at the cost of Pro-gated collaboration/import-export and a 4-year-old, single-vendor codebase. |
| [Fortune Sheets](fortune-sheets.md) | ✅ | B (5/6) | The MIT drop-in grid React app inherited from Luckysheet with an op stream for your own backend; free and simple, but it has sat untouched since 2025-12 and has no xlsx I/O of its own. |
| [Handsontable](handsontable.md) | ✅ | A (5/6) | The 15-year-old data-grid incumbent: deepest spreadsheet-edit UX in DOM and steady releases — once you pay, because commercial use is not free under its custom license. |
| [Jspreadsheet](jspreadsheet.md) | ✅ | B (5/6) | The MIT vanilla-JS grid (ex-jExcel) with typed columns and Excel paste; the cheapest serious grid, but the community edition is a marketing funnel to Pro and its GitHub releases trail npm. |
| [Grist](grist.md) | ✅ | A (5/6) | The self-hostable spreadsheet-database *product* with Python formulas and per-row access rules; you run it, you don't embed it — and the free core is open-core behind a source-available full edition. |
| [ONLYOFFICE Docs](onlyoffice-documentserver.md) | ✅ | B (6/6) | The all-in-one AGPL document server: real .docx/.xlsx/.pptx fidelity, built-in co-editing, one docker container — sized for a "click file → editor" drive, not for rebuilding your product's UI. |
| [Collabora Online](collabora-online.md) | ✅ | A (5/6) | The LibreOffice-engine document server behind WOPI: maximal format coverage from a mature C++ team — but GitHub is an issue mirror (code lives on Gerrit) and integration means running a WOPI host. |

## What belongs here

Repositories whose primary job is a **human-interactive editing surface** for spreadsheet/document/presentation content in a browser or app: embedded editor SDKs and frameworks, data-grid components with spreadsheet controls, self-hostable document servers, and spreadsheet-platform applications. Not programmatic Office-file authoring without a UI (→ [office-automation](../office-automation/INDEX.md)), not document ingestion/parsing (→ [document-parsing](../document-parsing/INDEX.md)), not archiving suites (→ [document-management](../document-management/INDEX.md)), not design/diagram canvases (→ [design-editors](../design-editors/INDEX.md), [diagramming](../diagramming/INDEX.md)). Whiteboards with only drawing semantics stay in [diagramming](../diagramming/INDEX.md); once a grid has formulas, cell types, and editing UX, it belongs here.
