# terminal-ui

> Category node. Terminal/CLI UI libraries — colors, TUIs, ASCII art, terminal rendering — plus the terminal multiplexers (tmux, Zellij) that keep panes and sessions alive around those tools.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **colorama** | Use it when a Python CLI must show ANSI colours correctly on legacy Windows consoles too, with near-zero dependencies — but it only translates colour and style codes, and on Linux, macOS or Windows 10+ it does little you couldn't do yourself. | B (5/6) | [→](colorama.md) |
| **asciimatics** | Use it when you need a cross-platform full-screen Python TUI plus an ASCII animation engine on Linux/macOS/Windows — but the widget set is spartan, the API older-style, and it's single-maintainer. | B (5/6) | [→](asciimatics.md) |
| **Terminal Markdown Viewer (mdv)** | Use it when you want a simple Markdown file rendered with colour, tables and highlighted code in a plain terminal over SSH — but it has been unmaintained since 2023-10 and fails on inline HTML, so glow or mdcat are safer. | D (3/6) | [→](terminal-markdown-viewer.md) |
| **ART** | Use it when a Python CLI needs pure-Python figlet-style ASCII text banners with no system binaries — but it's text-to-art only (not image-to-ASCII) and won't match figlet's exact fonts. | B (5/6) | [→](art.md) |
| **asciify** | Use it when you want a one-minute read of the classic image-to-ASCII recipe (downsample, greyscale, brightness ramp) to learn from or reimplement — but the repo has no license, so all rights are reserved, and it has been abandoned since 2018-10. | E (4/6) | [→](asciify.md) |
| **Warp** | Use it when you want command output split into selectable blocks that a built-in coding agent reads in the same session, on macOS, Linux, and Windows alike — but only the AGPL client is open; agent, sync, and auth run on Warp's proprietary servers. | B (5/6) | [→](warp.md) |
| **Alacritty** | Use it when you want a fast GPU-rendered terminal that behaves the same on macOS, Linux, BSD, and Windows and you already leave layout to tmux or a window manager — but it has no tabs, splits, or ligatures by design. | A (6/6) | [→](alacritty.md) |
| **Rich** | Use it when a Python CLI's output needs colour plus layout — aligned tables, progress bars, highlighted code, readable tracebacks — from one print-like API — but it has no event loop for interactive screens, and maintenance now rests on one person. | B (6/6) | [→](rich.md) |
| **Textual** | Use it when a Python CLI has outgrown its flags and people need to browse, filter, and act on data over SSH without building a web app — but since Textualize wound down in 2025 it is essentially one maintainer, and major versions change often. | B (6/6) | [→](textual.md) |
| **tmux** | Use it when a long-running build or server over SSH must outlive the terminal and you want the smallest universal multiplexer for it — but it has no notion of what runs in a pane, so agent supervision is yours to script. | A (6/6) | [→](tmux.md) |
| **Zellij** | Use it when you want terminal multiplexing with discoverability built in (mode hint bar, mouse, layouts, WASM plugins) plus a token-authenticated web client — but it is pre-1.0 with a large issue backlog and its web door needs real TLS work. | A (6/6) | [→](zellij.md) |
| **Pebrel** | Use it when several AI coding CLIs run side by side on Windows and you want each pane to report working/waiting/done with notifications that jump back to it, plus SSH/SFTP in the same app — but it is twelve weeks old, single-maintainer, and Linux/macOS are Preview. | C (5/6) | [→](pebrel.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [colorama](colorama.md) | ✅ | B (5/6) | Gets one code path for coloured output everywhere from a 12-year-old, ubiquitous shim; costs no tables, layout or TUI, no new release since 0.4.6 in 2022, and shrinking relevance as legacy Windows fades. |
| [asciimatics](asciimatics.md) | ✅ | B (5/6) | Use it when you need a cross-platform full-screen Python TUI plus an ASCII animation engine on Linux/macOS/Windows — but the widget set is spartan, the API older-style, and it's single-maintainer. |
| [Terminal Markdown Viewer (mdv)](terminal-markdown-viewer.md) | ✅ | D (3/6) | Gets themed Markdown-to-ANSI from a pip install that also reads stdin; costs a Python runtime, POSIX-only support, no paging or search, and a self-described proof of concept that nobody will fix. |
| [ART](art.md) | ✅ | B (5/6) | Use it when a Python CLI needs pure-Python figlet-style ASCII text banners with no system binaries — but it's text-to-art only (not image-to-ASCII) and won't match figlet's exact fonts. |
| [asciify](asciify.md) | ✅ | E (4/6) | Gets the whole algorithm in one short, legible script; costs any legal right to copy it, no colour or video output, and no maintainer — so reimplement it or use ascii-magic. |
| [Alacritty](alacritty.md) | ✅ | A (6/6) | Ten years of focused, stable rendering speed with minimal config, traded for leaving tabs, splits, ligatures, and AI features to other tools. |
| [Warp](warp.md) | ✅ | B (5/6) | An agent-native terminal workflow across three operating systems, traded for dependence on a VC-backed vendor's cloud and an open codebase with only months of public history. |
| [tmux](tmux.md) | ✅ | A (6/6) | Use it when a long-running build or server over SSH must outlive the terminal and you want the smallest universal multiplexer for it — but it has no notion of what runs in a pane, so agent supervision is yours to script. |
| [Zellij](zellij.md) | ✅ | A (6/6) | Use it when you want terminal multiplexing with discoverability built in (mode hint bar, mouse, layouts, WASM plugins) plus a token-authenticated web client — but it is pre-1.0 with a large issue backlog and its web door needs real TLS work. |
| [Pebrel](pebrel.md) | ✅ | C (5/6) | Windows-first GPU terminal that hooks Claude Code/Codex so panes report agent state, with SSH/SFTP built in; very young, single-maintainer, GPL-3.0. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

Libraries that **render UI in the terminal** — colors, TUIs, ASCII art, styled output — and terminal **multiplexers** (session/pane keepers like tmux, Zellij; agent-aware ones like [herdr](../agent-frameworks/coding-agents/agent-multiplexers/herdr.md) live under `agent-frameworks/coding-agents/orchestration-and-review`).
