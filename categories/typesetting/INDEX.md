# typesetting

> Category node. Compile a plain-text markup source into a finished typeset document — print PDF, web pages, slides, books or docs.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Asciidoctor** | Use it when technical documentation must publish from a plain-text source to HTML, DocBook, EPUB or man pages — not when you need a typesetting engine or print-grade PDF. | C (4/6) | [→](asciidoctor.md) |
| **LaTeX** | Use it when a venue's class file, decades of packages, or a source language stable for decades decide the outcome — not when nobody will maintain `\begin{}` scaffolding or you need HTML from the same file. | B (6/6) | [→](latex.md) |
| **Quarkdown** | Use it when one Markdown-legible source must compile to a web page, a print PDF, reveal.js slides and a docs site — but not when the deliverable must be Word, the license must be permissive, or print fidelity is the hard requirement. | B (5/6) | [→](quarkdown.md) |
| **Typst** | Use it when you can choose the source language and want print-quality PDF with a short learning curve and an Apache-2.0 toolchain — not when a venue mandates LaTeX class files or the source must stay Markdown. | A (6/6) | [→](typst.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Asciidoctor](asciidoctor.md) | ✅ | C (4/6) | Use it when technical documentation must publish from a plain-text source to HTML, DocBook, EPUB or man pages — not when you need a typesetting engine or print-grade PDF. |
| [LaTeX](latex.md) | ✅ | B (6/6) | Use it when a venue's class file, decades of packages, or a source language stable for decades decide the outcome — not when nobody will maintain `\begin{}` scaffolding or you need HTML from the same file. |
| [Quarkdown](quarkdown.md) | ✅ | B (5/6) | Use it when one Markdown-legible source must compile to a web page, a print PDF, reveal.js slides and a docs site — but not when the deliverable must be Word, the license must be permissive, or print fidelity is the hard requirement. |
| [Typst](typst.md) | ✅ | A (6/6) | Use it when you can choose the source language and want print-quality PDF with a short learning curve and an Apache-2.0 toolchain — not when a venue mandates LaTeX class files or the source must stay Markdown. |

## What belongs here

Tools whose primary job is **compiling a plain-text markup source into a finished typeset document** — a print-ready PDF, a paged article, slides, a book, or a documentation set. The compiler and its layout engine are the product. Not Markdown *parsers* or converters (see `markdown-tools`), not PDF readers or low-level PDF writers (see `pdf-tools`), not tools that turn documents into structured data for gen-AI (see `document-parsing`). Cross-reference: a Markdown-flavored member of this category is still listed here when its defining feature is document output rather than Markdown processing.
