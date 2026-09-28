# reading-tools

> Category node. Reading tools — reader-mode extensions and RSS readers.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Read Frog** | Use it when you want a feature-rich open-source immersive/bilingual translation extension with BYOK AI providers, local Ollama/custom endpoints, TTS, and YouTube subtitle translation. | B (6/6) | [→](read-frog.md) |
| **FluentRead** | Use it when you want a Chinese-first open immersive-translation browser extension with many engines, bilingual/full-page translation, and Ollama/custom OpenAI-compatible setup. | C (6/6) | [→](fluentread.md) |
| **Margin Read** | Use it when MIT licensing, explicit BYOK/local endpoint support, and a written privacy threat model matter more than feature completeness. | C (5/6) | [→](margin-read.md) |
| **Pair Translate** | Use it when you want a lighter bilingual webpage translator with direct provider requests, LLM templates, and Chrome/Firefox/Edge distribution. | C (5/6) | [→](pair-translate.md) |
| **NetNewsWire** | Use it when you read many feeds on Mac/iPhone and want a fast, ad-free native RSS client you own — but only on Apple platforms, never elsewhere. | B (6/6) | [→](netnewswire.md) |
| **Just Read** | Use it when you want to strip ads and clutter from an article in-browser, your way, with per-site selectors — but it's EULA-licensed source, not real OSS. | C (6/6) | [→](just-read.md) |
| **FreshRSS** | A free, self-hostable news aggregator… | B (6/6) | [→](freshrss.md) |
| **Horizon** | Use it when feeds overflow you and you want a self-hosted LLM pipeline that scores, filters, deduplicates and briefs them bilingually every day — not a reader you browse. | B (6/6) | [→](horizon.md) |
| **Follow Builders** | Use it when you want a no-keys daily digest of what a fixed, author-curated list of AI builders said on X, podcasts and two blogs — but you can't pick the sources and uptime rides on one person's X API bill. | C (4/6) | [→](follow-builders.md) |
| **Bilingual Book Maker** | Use it when you want a scriptable CLI that turns epub/txt/md/srt/pdf into bilingual books via LLM/MT APIs, with resume and PyPI packaging — not an agent pipeline. | A (5/6) | [→](bilingual-book-maker.md) |
| **TranslateBooksWithLLMs** | Use it when a non-developer must translate a whole EPUB/DOCX/SRT/TXT into one target language with formatting kept, a glossary, and resume — via a desktop app on Ollama or a cloud key; single-user localhost only. | C (6/6) | [→](translate-books-with-llms.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Read Frog](read-frog.md) | ✅ | B (6/6) | Richest open-source AI reading/translation extension here: BYOK providers, local/custom endpoints, TTS, subtitles, and batching — but GPL/commercial-dual licensed and broad-permission. |
| [FluentRead](fluentread.md) | ✅ | C (6/6) | Translation-first open immersive translator with many engines and store links — less explicit than Margin Read on endpoint/privacy boundaries and more single-maintainer concentrated. |
| [Margin Read](margin-read.md) | ✅ | C (5/6) | Best when MIT, BYOK, local OpenAI-compatible runtimes, and privacy docs decide the choice — but early Chrome/Chromium MVP with tiny adoption. |
| [Pair Translate](pair-translate.md) | ✅ | C (5/6) | Lightweight bilingual translator with verified LLM/local templates and active releases — but GPL, young, and browser-side API-key handling remains a trust boundary. |
| [NetNewsWire](netnewswire.md) | ✅ | B (6/6) | Use it when you read many feeds on Mac/iPhone and want a fast, ad-free native RSS client you own — but only on Apple platforms, never elsewhere. |
| [Just Read](just-read.md) | ✅ | C (6/6) | Use it when you want to strip ads and clutter from an article in-browser, your way, with per-site selectors — but it's EULA-licensed source, not real OSS. |
| [Bilingual Book Maker](bilingual-book-maker.md) | ✅ | A (5/6) | The mature CLI path for bilingual ebook files: any LLM/MT backend, resume, PyPI — but paragraph-stream translation without a curated glossary. |
| [TranslateBooksWithLLMs](translate-books-with-llms.md) | ✅ | C (6/6) | GUI + CLI whole-file translator with placeholder-checked tags, per-book glossary and SQLite resume — but no PDF, no PyPI package, AGPL, single maintainer, and no multi-user auth. |
| [Horizon](horizon.md) | ✅ | B (6/6) | Self-hosted AI news radar: profile-driven LLM scoring and dedup across RSS/HN/Reddit/Telegram/X, bilingual daily briefing — but ~7 months old, single maintainer, no releases yet. |
| [Follow Builders](follow-builders.md) | ✅ | C (4/6) | Zero-setup agent skill over the author's central daily feed (26 X builders, 6 podcasts, 2 blogs) — but no source control, no LICENSE file, raw-JSON scheduling on Claude Code, and a single maintainer paying for the X API. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

End-user **reading** tools — reader-mode browser extensions, bilingual/immersive translation extensions, RSS/feed readers. Article-extraction libraries live in `web-scraping`.
