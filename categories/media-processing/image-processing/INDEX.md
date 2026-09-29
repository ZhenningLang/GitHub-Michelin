# image-processing

> Category node. Image processing, conversion, resizing, composition, format tooling, and HTML-to-image rendering.
> ← back to [media-processing](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **ImageMagick** | Use a broad command-line suite and APIs to create, edit, compose, and convert images across 200+ formats. | B (5/6) | [→](imagemagick.md) |
| **sharp** | Build high-throughput Node.js pipelines for resizing and converting existing raster images through libvips. | A (6/6) | [→](sharp.md) |
| **Screenshot Service** | Render controlled HTML and CSS to PNG, JPEG, or WebP through a tiny internal HTTP service that you can isolate and harden. | D (4/6) | [→](screenshot-service.md) |
| **Magpie** | Upscale a small or non-DPI-aware Windows game/app window to full screen in real time with GPU filters (FSR, Anime4K, CRT), without injecting into the process. | B (6/6) | [→](magpie.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [ImageMagick](imagemagick.md) | ✅ | B (5/6) | Pick for broad format coverage, command-line automation, and general image composition; it is less natural than sharp inside a Node.js hot path and cannot lay out arbitrary HTML like a browser. |
| [sharp](sharp.md) | ✅ | A (6/6) | Pick for fast in-process Node.js transforms of existing images; it avoids Chromium overhead but does not render HTML, CSS, or web fonts. |
| [Screenshot Service](screenshot-service.md) | ✅ | D (4/6) | Pick only for trusted HTML behind an isolated internal endpoint; browser fidelity comes with Chromium cost, unsafe defaults, no established repository license, and substantial hardening work. |
| [Magpie](magpie.md) | ✅ | B (6/6) | Pick for live, non-injecting upscaling of one Windows window with image-quality filters; it is a GUI app (not a library), Windows-only, has no HDR or frame generation, and its releases lag the active dev branch. |
| Browserless | 未收录 | — | Pick for a shared headless-browser service with queueing, concurrency, and session controls; it has a much larger operational surface and SSPL/commercial licensing constraints. |
| capture-website-cli | 未收录 | — | Pick for one-off or scripted webpage captures from a CLI with rich capture flags; it is simpler than operating an API service but does not provide pooling, tenancy, or a persistent rendering endpoint. |

## What belongs here

Image processing, conversion, resizing, composition, format tooling, HTML-to-image rendering, and real-time upscaling of a live desktop window. General browser automation belongs under `web-automation`; document-first PDF conversion belongs under document or PDF tooling.
