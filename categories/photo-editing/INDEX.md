# photo-editing

> Category node. Open-source photo editors you run yourself — raw developers, photo libraries for culling and non-destructive edits, and raster image editors — instead of renting Lightroom or Photoshop.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **LightCraft** | Use it when you want Lightroom's cull-develop-export workflow locally without a subscription, and want an agent to drive it over MCP/CLI — accepting a nine-day-old pre-1.0 app with estimated camera colour and thin raw-format coverage. | B (5/6) | [→](lightcraft.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [LightCraft](lightcraft.md) | ✅ | B (5/6) | MIT OR Apache-2.0, pure-Rust Lightroom-style library + raw developer with an MCP/CLI command surface; young, AI-agent-built, no measured colour calibration and partial CR3 support. |
| darktable · RawTherapee | 未收录 | — | Mature GPL-3.0 raw developers with far wider camera coverage and colour science, but unfamiliar workflows and no agent interface — weighed in LightCraft's comparison, not yet indexed. |
| Adobe Lightroom · Photoshop | 非仓库 | — | Closed subscription products — out of scope by shape, named as substitutes inside the pages. |

## What belongs here

Repositories whose primary job is **editing photographs**: developing camera raw files, managing a photo library for culling and non-destructive edits, or pixel/layer-based raster editing. Not self-hosted photo backup and sharing servers (see `document-management`, where Immich lives); not vector illustration or UI design canvases (see `design-editors`); not AI image generation; not computer-vision libraries you call from code (see `computer-vision`).
