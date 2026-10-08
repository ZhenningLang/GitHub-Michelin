# reading-tools

> Category node. Reading tools — reader-mode extensions and RSS readers.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Read Frog** | Use it when you learn languages by reading and want bilingual paragraphs, level-aware explanations, read-aloud, custom AI actions, and spaced-repetition word cards with your own AI provider — but its company-controlled dual license and a proprietary layout package since 2026-09 block fully free forks. | B (6/6) | [→](read-frog.md) |
| **FluentRead** | Use it when you want one open-source extension covering bilingual webpages, PDF/ePub, OCR, and video subtitles, with free, bring-your-own-key, or in-browser engines — but it is GPL-3.0, effectively one maintainer, and its zero-config default sends text to public translation endpoints. | C (6/6) | [→](fluentread.md) |
| **Margin Read** | Use it when page text may only go to your own Ollama, LM Studio, or company gateway and you want an MIT extension with a written threat model — but it is a young, now-quiet, single-maintainer Chrome MVP without PDF, subtitles, or OCR. | C (5/6) | [→](margin-read.md) |
| **Pair Translate** | Use it when Read Frog and FluentRead feel too heavy and you want a small bilingual translator sending text straight from the browser to Microsoft, DeepL, or your own LLM including local Ollama — but it is GPL-3.0 and effectively one person's year-old project. | C (5/6) | [→](pair-translate.md) |
| **NetNewsWire** | Use it when you read many feeds on Mac/iPhone and want a fast, ad-free native RSS client you own — but only on Apple platforms, never elsewhere. | B (6/6) | [→](netnewswire.md) |
| **Just Read** | Use it when you want to strip ads and clutter from an article in-browser, your way, with per-site selectors — but it's EULA-licensed source, not real OSS. | C (6/6) | [→](just-read.md) |
| **FreshRSS** | Use it when you want your feed subscriptions and read state on your own VPS, NAS, or Raspberry Pi, synced to any Google Reader–API client — but updates, backups, and TLS are yours forever, and Miniflux is leaner if you skip extensions. | B (6/6) | [→](freshrss.md) |
| **Horizon** | Use it when feeds overflow you and you want a self-hosted LLM pipeline that scores, filters, deduplicates and briefs them bilingually every day — not a reader you browse. | B (6/6) | [→](horizon.md) |
| **Follow Builders** | Use it when you want a no-keys daily digest of what a fixed, author-curated list of AI builders said on X, podcasts and two blogs — but you can't pick the sources and uptime rides on one person's X API bill. | C (4/6) | [→](follow-builders.md) |
| **Bilingual Book Maker** | Use it when you want a scriptable CLI that turns epub/txt/md/srt/pdf into bilingual books via LLM/MT APIs, with resume and PyPI packaging — not an agent pipeline. | A (5/6) | [→](bilingual-book-maker.md) |
| **TranslateBooksWithLLMs** | Use it when a non-developer must translate a whole EPUB/DOCX/SRT/TXT into one target language with formatting kept, a glossary, and resume — via a desktop app on Ollama or a cloud key; single-user localhost only. | C (6/6) | [→](translate-books-with-llms.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Read Frog](read-frog.md) | ✅ | B (6/6) | The richest learning feature set and a fast release cadence, traded for GPL plus commercial dual licensing, a contributor grant to FEELIO, and a closed-source dependency. |
| [FluentRead](fluentread.md) | ✅ | C (6/6) | The broadest reading coverage in one extension, paid for with GPL licensing, a single-maintainer bus factor, and less control over where text goes by default. |
| [Margin Read](margin-read.md) | ✅ | C (5/6) | An auditable data flow and permissive license, traded for a minimal feature set, tiny adoption, and no release since June 2026. |
| [Pair Translate](pair-translate.md) | ✅ | C (5/6) | A lighter footprint with direct provider requests, traded for fewer immersive-translation workflows, adoption an order of magnitude below Read Frog, and broad all-URLs permissions. |
| [NetNewsWire](netnewswire.md) | ✅ | B (6/6) | Use it when you read many feeds on Mac/iPhone and want a fast, ad-free native RSS client you own — but only on Apple platforms, never elsewhere. |
| [Just Read](just-read.md) | ✅ | C (6/6) | Use it when you want to strip ads and clutter from an article in-browser, your way, with per-site selectors — but it's EULA-licensed source, not real OSS. |
| [Bilingual Book Maker](bilingual-book-maker.md) | ✅ | A (5/6) | The mature CLI path for bilingual ebook files: any LLM/MT backend, resume, PyPI — but paragraph-stream translation without a curated glossary. |
| [TranslateBooksWithLLMs](translate-books-with-llms.md) | ✅ | C (6/6) | GUI + CLI whole-file translator with placeholder-checked tags, per-book glossary and SQLite resume — but no PDF, no PyPI package, AGPL, single maintainer, and no multi-user auth. |
| [Horizon](horizon.md) | ✅ | B (6/6) | Self-hosted AI news radar: profile-driven LLM scoring and dedup across RSS/HN/Reddit/Telegram/X, bilingual daily briefing — but ~7 months old, single maintainer, no releases yet. |
| [Follow Builders](follow-builders.md) | ✅ | C (4/6) | Zero-setup agent skill over the author's central daily feed (26 X builders, 6 podcasts, 2 blogs) — but no source control, no LICENSE file, raw-JSON scheduling on Claude Code, and a single maintainer paying for the X API. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

End-user **reading** tools — reader-mode browser extensions, bilingual/immersive translation extensions, RSS/feed readers. Article-extraction libraries live in `web-scraping`.
