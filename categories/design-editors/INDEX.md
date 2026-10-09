# design-editors

> Category node. Open-source design editors — the Figma-class canvas you run yourself instead of renting it, either local-first on one machine or self-hosted for a team.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **DesignCraft** | Use it when you must lay out print pages the InDesign way — open and write IDML, export CMYK/PDF/X print PDFs, drive every command from a CLI or MCP — on any OS without a Creative Cloud seat; not when you must open `.indd`, need certified prepress today, or need a format that holds still (v0.x, eight days old). | C (5/6) | [→](designcraft.md) |
| **OpenPencil** | Use it when you must open existing Figma `.fig` files and script them — inspect, lint, convert, export to JSX — or you want a local-first AI-native editor with no server, no account and no upload. | B (6/6) | [→](open-pencil.md) |
| **Penpot** | Use it when a team must edit one design file on servers you control — browser editor, real-time multiplayer, components/variants, prototypes and design tokens — and per-seat hosted SaaS is off the table. | B (5/6) | [→](penpot.md) |
| **VectorCraft** | Use it when you want Illustrator's layout and shortcuts without the subscription — on Linux, FreeBSD or in a browser — to open `.ai`/PDF/EPS/Affinity files, or to let an agent draw and export vector art over its CLI/MCP command surface; days old, so not for deadline work. | C (5/6) | [→](vectorcraft.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [DesignCraft](designcraft.md) | ✅ | C (5/6) | InDesign-style page layout in Rust with two-way IDML, print PDF and a CLI/MCP surface on every OS; eight days old, agent-written, one dominant maintainer, print fidelity unproven. |
| [OpenPencil](open-pencil.md) | ✅ | B (6/6) | Local-first, MIT, native `.fig` I/O plus a CLI/MCP/agent surface; pre-1.0 with one dominant maintainer, and no prototyping, comments or version history. |
| [Penpot](penpot.md) | ✅ | B (5/6) | MPL-2.0 platform you self-host with real accounts, roles and prototyping; costs a Postgres + Valkey + object-store fleet, and SSO/admin sit behind a paid Enterprise tier. |
| [VectorCraft](vectorcraft.md) | ✅ | C (5/6) | MIT/Apache-2.0 Rust clone of the Illustrator workflow with a 685-command CLI/MCP surface; launched 2026-09-30, self-graded 40–55% power-user parity, no hosted PR CI. |
| Figma · Sketch · Adobe XD · Adobe Illustrator · Adobe InDesign | 非仓库 | — | Closed hosted/vendor-licensed design tools — out of scope by shape, named as substitutes inside the pages. |

## What belongs here

Repositories whose primary job is being a **design editor**: an infinite-canvas tool for producing UI and visual designs — frames, components, variants, constraints, handoff — or Illustrator-class vector illustration (paths, Pathfinder, appearance, print/vector file I/O), that you run yourself, locally or on your own servers. Page-layout (InDesign-class) editors for print and publication pages live here too: the same run-it-yourself canvas, aimed at spreads, threaded text and print PDF instead of screens. Not diagrams-as-code or text-to-diagram tools (see `diagramming`); not agent-driven design *generation* that produces no editable document (see `ai-design-generation`); not computer-aided design (see `cad`).
