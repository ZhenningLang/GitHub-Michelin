# social-media-management

> Category node. Self-hosted agents and automation that operate real social media accounts end-to-end — trend discovery, content creation, platform-adapted publishing, and performance feedback.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Easel** | Use it when you run accounts on the Chinese platforms (Xiaohongshu/Douyin/Zhihu/Bilibili/…) and want one self-hosted agent workbench covering discover → create → publish → attribute, with per-account profiles — accepting a one-month-old, v0.x project and platform risk-control exposure. | B (5/6) | [→](easel.md) |
| **xiaohongshu-mcp** | Use it when your existing agent (Claude Code, Cursor, n8n…) should search, read, post, comment and like on Xiaohongshu through a self-hosted MCP/REST server with its own fingerprint browser — accepting real account-ban risk, a single maintainer and an opaque prebuilt browser from the author's CDN. | B (6/6) | [→](xiaohongshu-mcp.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Easel](easel.md) | ✅ | B (5/6) | Full Chinese-platform content loop (trends, creation, publishing, attribution) on OpenClaw; one month old at verification, and Xiaohongshu automation carries account-risk warnings from the authors themselves. |
| [xiaohongshu-mcp](xiaohongshu-mcp.md) | ✅ | B (6/6) | One Go binary that gives any MCP client read/write hands on Xiaohongshu; headless and server-friendly, but a second detectable login with ban reports in its own tracker. |
| [OpenClaw](../agent-frameworks/agent-runtimes/personal-assistants/openclaw.md) | ✅ | B (5/6) | The general agent runtime Easel wraps; choose it directly when the job isn't specifically Chinese social-media content ops. |
| [MoneyPrinterTurbo](../video-production/moneyprinter-turbo.md) | ✅ | B (6/6) | Topic → narrated shorts appliance; stops at the video file — no accounts, no publishing, no learning loop. |
| social-auto-upload | 未收录 | — | Upload-only browser automation for ready-made videos; not added in this tab-intake batch. |
| Postiz | 未收录 | — | Self-hosted scheduler for the global platforms (X/Instagram/YouTube); not added in this tab-intake batch. |

## What belongs here

Tools and applications whose primary job is **operating real social media accounts** — discovering trends, creating
platform-adapted content, publishing to logged-in accounts, and reading performance back. Not simulating social
platforms with agents (see `social-simulation`), not video-only production pipelines (see `video-production`), and
not portable card/visual skills you install into an agent you already run (see `agent-skills`).
