# translation

> Leaf of [writing](../INDEX.md). Whole-document and whole-book translation skills — file pipelines that turn PDF/DOCX/EPUB into another language through a coding agent.
> ← up to [writing](../INDEX.md) · root [route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Collections in this leaf

| Collection | Use when | Health | Page |
| --- | --- | --- | --- |
| **translate-book** | Agent skill (Codex/Claude Code/OpenClaw) that translates entire books (PDF/DOCX/EPUB) with parallel subagents, glossary pinning, and neighbor-context consistency. | B (4/6) | [→](translate-book.md) |
| **claude_translater** | Minimal shell + Claude CLI scripts that translate PDF/DOCX/EPUB (and PPTX) — the unmaintained, unlicensed inspiration for translate-book. | D (4/6) | [→](claude-translater.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [translate-book](translate-book.md) | ✅ | B (4/6) | Whole-book translation as an agent skill: parallel subagents, glossary, resume, multi-format output — but young, single-maintainer, and Calibre/Pandoc-bound. |
| [claude_translater](claude-translater.md) | ✅ | D (4/6) | The shell-script origin of translate-book; only pick it for raw hackable scripts or PPTX translation — no license, unmaintained. |

## What belongs here

Skills whose job is **translating whole documents or books** into another language. Skills that translate as one step inside a broader content workflow belong in [content-production](../content-production/INDEX.md).
