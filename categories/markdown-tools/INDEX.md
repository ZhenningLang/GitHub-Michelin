# markdown-tools

> Category node. Markdown parsing, rendering, and authoring tools.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **CommonMark** | Use it when you need the spec author's reference answer for how a Markdown edge case parses, plus an editable node tree, in JavaScript — but it is CommonMark only: no tables, task lists, strikethrough or extension API. | B (5/6) | [→](commonmark.md) |
| **Markdown Here** | Use it when you write technical email in webmail or Thunderbird and want Markdown code blocks, tables and lists rendered to HTML with one toggle before sending — but upstream is effectively stale, and a Manifest V3 change could break or delist it. | C (4/6) | [→](markdown-here.md) |
| **marked** | Use it when you need a fast, low-level Markdown→HTML parser in JS — but you must sanitize the output yourself and don't need strict CommonMark. | A (5/6) | [→](marked.md) |
| **remark** | Use it when a Node.js docs or content pipeline must lint, rewrite and re-serialize Markdown through an mdast tree — list markers, tables of contents, link paths — but if you only need Markdown to HTML, marked or markdown-it is lighter. | A (6/6) | [→](remark.md) |
| **markdown-it** | Use it when a JavaScript docs site, CMS preview or chat UI turns Markdown into HTML and you need CommonMark behaviour plus custom syntax through plugins — but its flat token stream is for rendering, so linting or rewriting Markdown belongs in remark. | A (6/6) | [→](markdown-it.md) |
| **micromark** | Use it when you need cmark-exact CommonMark parsing in a ~14 kB safe-by-default bundle, or byte-level token positions for a linter or editor — but it gives tokens or HTML, not an editable tree; for transforming Markdown use remark. | B (6/6) | [→](micromark.md) |
| **Pandoc** | Use it when one Markdown, Org or LaTeX source must ship as DOCX, EPUB, PDF, HTML or wiki markup, or a colleague's .docx must come back into Markdown — but rich layouts convert lossily, and it cannot read PDFs. | B (6/6) | [→](pandoc.md) |
| **Goldmark** | Use it when a Go service or tool must render Markdown the way GitHub does, CJK emphasis included, with GFM extensions and no third-party modules — but v2 broke the API and most third-party extensions are not ported yet. | A (6/6) | [→](goldmark.md) |
| **markdownlint** | Use it when Markdown is a deliverable in your repo and you want the MD001–MD060 rules to catch mixed bullets, skipped heading levels or broken anchors in CI and the editor — but this repo is the library; the command is markdownlint-cli2. | A (6/6) | [→](markdownlint.md) |
| **MDX** | Use it when the docs live inside a React/Preact/Vue app and the prose must import and render your own components — not when the deliverable is a standalone PDF, book or publishable document. | B (5/6) | [→](mdx.md) |
| **TanStack Markdown** | Use it when your docs/blog corpus is author-controlled, bundle size is the constraint, and you want HTML/React/Octane renderers to emit identical output from one cached AST — not for untrusted user Markdown or full CommonMark fidelity. | C (5/6) | [→](tanstack-markdown.md) |
| **TanStack Highlight** | Use it when your blog or docs use a short, known list of languages and you want tiny, synchronous, class-only highlighting identical on server and client — not for VS Code-grade accuracy, rare languages, or auto-detection. | B (6/6) | [→](tanstack-highlight.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [CommonMark](commonmark.md) | ✅ | B (5/6) | Strict spec behaviour and a walkable AST in one small library, at the cost of no GFM, no plugins, and unsafe defaults: raw HTML passes through unless you enable safe mode and add a sanitizer. |
| [Markdown Here](markdown-here.md) | ✅ | C (4/6) | Buys Markdown authoring inside compose boxes with no service to run; costs dependence on a slow-moving extension that only works in supported fields — treat it as a convenience you can lose. |
| [marked](marked.md) | ✅ | A (5/6) | Use it when you need a fast, low-level Markdown→HTML parser in JS — but you must sanitize the output yourself and don't need strict CommonMark. |
| [remark](remark.md) | ✅ | A (6/6) | An editable syntax tree plus the unified plugin ecosystem, in exchange for an ESM-only toolchain of many small packages and HTML output that is unsafe until you add rehype-sanitize. |
| [markdown-it](markdown-it.md) | ✅ | A (6/6) | Safe-by-default rendering and hundreds of .use() plugins, in exchange for more concepts than marked, one lead maintainer, and a v15 upgrade that broke deep imports and changed linkify defaults. |
| [micromark](micromark.md) | ✅ | B (6/6) | Reference-grade conformance and positioned tokens in a tiny parser, paid for with extensions that are hard to write, an ESM-only package, and effectively one maintainer. |
| [TanStack Markdown](tanstack-markdown.md) | ✅ | C (5/6) | Use it when your docs/blog corpus is author-controlled, bundle size is the constraint, and you want HTML/React/Octane renderers to emit identical output from one cached AST — not for untrusted user Markdown or full CommonMark fidelity. |
| [TanStack Highlight](tanstack-highlight.md) | ✅ | B (6/6) | Use it when your blog or docs use a short, known list of languages and you want tiny, synchronous, class-only highlighting identical on server and client — not for VS Code-grade accuracy, rare languages, or auto-detection. |

## What belongs here

Tools whose primary job is **parsing, rendering, or authoring Markdown** — parsers, converters, and editor extensions. Not document parsing into structured data for gen-AI (see `document-parsing`), not diagram-from-text generators (see `diagramming`).
