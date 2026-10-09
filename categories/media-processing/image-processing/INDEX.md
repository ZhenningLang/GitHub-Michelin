# image-processing

> Category node. Image processing, conversion, resizing, composition, format tooling, and HTML-to-image rendering.
> ← back to [media-processing](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **ImageMagick** | Use it when a script or CI job must convert, resize and composite images across 200+ formats — TIFF, PSD, EPS, HEIC, multi-page PDF — from one shell command — but decoding untrusted uploads without a sandbox is a steady CVE risk. | B (5/6) | [→](imagemagick.md) |
| **sharp** | Use it when a Node.js upload handler, build step or API route must turn large photos into thumbnails and WebP/AVIF in-process and fast — but its prebuilt binaries cannot decode HEIC, PDF, PSD or camera RAW. | A (6/6) | [→](sharp.md) |
| **Screenshot Service** | Render controlled HTML and CSS to PNG, JPEG, or WebP through a tiny internal HTTP service that you can isolate and harden. | D (4/6) | [→](screenshot-service.md) |
| **Magpie** | Upscale a small or non-DPI-aware Windows game/app window to full screen in real time with GPU filters (FSR, Anime4K, CRT), without injecting into the process. | B (6/6) | [→](magpie.md) |
| **PhotoCraft** | Use it when a layered PSD must be edited offline without a Photoshop seat — adjustment layers, masks and type stay live, and a CLI/MCP drives the same engine — but it is a 9-day-old, agent-written early alpha its own team rates ~25–35% ready for daily pro work. | B (6/6) | [→](photocraft.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [ImageMagick](imagemagick.md) | ✅ | B (5/6) | The widest format coverage and a scriptable CLI with bindings for most languages, paid for with a huge decoder attack surface, slower resizing than sharp, and development concentrated in two maintainers. |
| [sharp](sharp.md) | ✅ | A (6/6) | libvips speed and low memory from one npm install, in exchange for a narrow prebuilt format set, a runtime that must load native Node-API add-ons, and a project that is effectively one maintainer. |
| [Screenshot Service](screenshot-service.md) | ✅ | D (4/6) | Pick only for trusted HTML behind an isolated internal endpoint; browser fidelity comes with Chromium cost, unsafe defaults, no established repository license, and substantial hardening work. |
| [Magpie](magpie.md) | ✅ | B (6/6) | Pick for live, non-injecting upscaling of one Windows window with image-quality filters; it is a GUI app (not a library), Windows-only, has no HDR or frame generation, and its releases lag the active dev branch. |
| [PhotoCraft](photocraft.md) | ✅ | B (6/6) | Offline, Photoshop-shaped Rust editor with native PSD layers and a CLI/MCP surface; paid for with extreme youth, a release every day or two, no AI/plug-in compatibility, and an unverifiable clean-room claim. |
| Browserless | 未收录 | — | Pick for a shared headless-browser service with queueing, concurrency, and session controls; it has a much larger operational surface and SSPL/commercial licensing constraints. |
| capture-website-cli | 未收录 | — | Pick for one-off or scripted webpage captures from a CLI with rich capture flags; it is simpler than operating an API service but does not provide pooling, tenancy, or a persistent rendering endpoint. |

## What belongs here

Image processing, conversion, resizing, composition, format tooling, HTML-to-image rendering, real-time upscaling of a live desktop window, and desktop raster image editors (layer/mask/PSD editing apps). General browser automation belongs under `web-automation`; document-first PDF conversion belongs under document or PDF tooling.
