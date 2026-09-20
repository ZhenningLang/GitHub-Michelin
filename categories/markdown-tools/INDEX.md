# markdown-tools

> Category node. Markdown parsing, rendering, and authoring tools.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **CommonMark** | Use it when you need the canonical, spec-compliant Markdown reference implementation with a traversable AST — but not for speed, GFM, or a plugin ecosystem. | B (5/6) | [→](commonmark.md) |
| **Markdown Here** | Use it when you want to write email in Markdown and render it before sending via a browser/Thunderbird extension — mind its slow maintenance. | C (4/6) | [→](markdown-here.md) |
| **marked** | Use it when you need a fast, low-level Markdown→HTML parser in JS — but you must sanitize the output yourself and don't need strict CommonMark. | A (5/6) | [→](marked.md) |
| **remark** | Use it when you need a full mdast AST pipeline for parsing, transforming, linting, and serializing Markdown — but it's a toolchain, not a one-call renderer. | A (6/6) | [→](remark.md) |
| **markdown-it** | Use it when you need a strict CommonMark/GFM-compliant, pluggable Markdown→HTML parser in JS — but the plugin ecosystem adds weight and you must still sanitize untrusted input. | A (6/6) | [→](markdown-it.md) |
| **micromark** | Use it when you need a low-level, streaming-friendly CommonMark/GFM tokenizer in JS — the engine underneath remark — but you must build the rendering layer yourself. | B (4/6) | [→](micromark.md) |
| **Pandoc** | Universal markup converter | B (6/6) | [→](pandoc.md) |
| **Goldmark** | :trophy: A markdown parser written in Go. Easy to extend, standard(CommonMark) compliant, well structured. | B (4/6) | [→](goldmark.md) |
| **markdownlint** | A Node.js style checker and lint tool for Markdown/CommonMark files. | A (6/6) | [→](markdownlint.md) |
| **Quarkdown** | Use it when one Markdown-legible source must compile to a web page, a print PDF, reveal.js slides and a docs site — but not when the deliverable must be Word, the license must be permissive, or print fidelity is the hard requirement. | B (5/6) | [→](quarkdown.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [CommonMark](commonmark.md) | ✅ | B (5/6) | Use it when you need the canonical, spec-compliant Markdown reference implementation with a traversable AST — but not for speed, GFM, or a plugin ecosystem. |
| [Markdown Here](markdown-here.md) | ✅ | C (4/6) | Use it when you want to write email in Markdown and render it before sending via a browser/Thunderbird extension — mind its slow maintenance. |
| [marked](marked.md) | ✅ | A (5/6) | Use it when you need a fast, low-level Markdown→HTML parser in JS — but you must sanitize the output yourself and don't need strict CommonMark. |
| [remark](remark.md) | ✅ | A (6/6) | Use it when you need a full mdast AST pipeline for parsing, transforming, linting, and serializing Markdown — but it's a toolchain, not a one-call renderer. |
| [markdown-it](markdown-it.md) | ✅ | A (6/6) | Use it when you need a strict CommonMark/GFM-compliant, pluggable Markdown→HTML parser in JS — but the plugin ecosystem adds weight and you must still sanitize untrusted input. |
| [micromark](micromark.md) | ✅ | B (4/6) | Use it when you need a low-level, streaming-friendly CommonMark/GFM tokenizer in JS — the engine underneath remark — but you must build the rendering layer yourself. |

## What belongs here

Tools whose primary job is **parsing, rendering, or authoring Markdown** — parsers, converters, and editor extensions. Not document parsing into structured data for gen-AI (see `document-parsing`), not diagram-from-text generators (see `diagramming`).
