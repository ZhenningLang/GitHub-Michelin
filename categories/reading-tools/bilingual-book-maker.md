---
name: Bilingual Book Maker
slug: bilingual-book-maker
repo: https://github.com/yihong0618/bilingual_book_maker
category: reading-tools
tags: [book-translation, epub, bilingual, cli, litellm]
language: Python
license: MIT
maturity: v1.2.1, active, 9.8k stars (as of 2026-09)
last_verified: 2026-09-18
type: tool
upstream:
  pushed_at: 2026-09-14T07:15:37Z
  default_branch: main
  default_branch_sha: 3f7fc1e21687146e7e3de1d6facdb56960b993a0
  archived: false
health:
  schema: 1
  computed_at: 2026-09-18T06:48:21Z
  overall: A
  overall_score: 3.8
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 4
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 71.0
        qualifying_issues: 6
        band: relaxed_solo
        window_offset_days: 1
        source: pr
        inferred: false
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: A
      raw:
        repo_age_days: 1296
        last_commit_age_days: 4
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 20
        top1_share: 0.336
        top3_share: 0.808
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    adoption: { reason: ambiguous }
---

# Bilingual Book Maker

A Python CLI that turns epub/txt/md/srt/pdf files into bilingual (side-by-side) books by calling LLM or machine-translation APIs directly — OpenAI/Anthropic-format endpoints, Gemini/Qwen/Groq/xAI/LiteLLM, local Ollama, Codex subscription, or classic MT engines — with resume support and a PyPI package (`bbook-maker`).

![Bilingual Book Maker — health radar](../../assets/health/bilingual-book-maker.svg)

## When to use

You're a reader with an EPUB (or txt/md/srt/pdf) you want to read bilingually — original and translation paragraph by paragraph — and you want a boring, scriptable tool, not an agent session. You `pip install bbook_maker`, point it at the file with one command and an API key (or a local Ollama model, or your Codex quota), and it streams through the book with `--resume` covering interruptions, emitting `${book_name}_bilingual.epub` at the end. It fits cron jobs, batch directories, and CI in a way agent-orchestrated pipelines don't.

You pick it over [translate-book](../agent-skills/writing/translate-book.md) when you want unattended CLI execution, bilingual output, and free choice of model backend including cheap MT engines — rather than a skill that must live inside a coding-agent harness and produces a single-language book; you pick it over browser extensions like [Read Frog](read-frog.md) when you need a *file* you can send to your Kindle, not in-place webpage overlays.

## When NOT to use

- **You need cross-chapter term consistency as a first-class feature.** It translates paragraph-stream fashion with optional session context (`--use_context session`, compacted at a token budget) — there is no curated glossary, no per-chunk term tables, no selective re-translation. For long books where proper-noun drift is the main pain, use [translate-book](../agent-skills/writing/translate-book.md) instead.
- **You want the translation to ride your coding-agent subscription by default.** Its native path is API keys (though a Codex route exists). If your only "LLM access" is a Claude Code/Codex harness, use translate-book or [claude_translater](../agent-skills/writing/claude-translater.md) instead.
- **You only read webpages.** For in-browser reading with bilingual overlays, use [Read Frog](read-frog.md) or [FluentRead](fluentread.md) instead — no file pipeline needed.
- **Your input is a complex PDF.** PDF input falls back to a bilingual `.txt` (EPUB creation is attempted but may fail), so layout matters are lost. For PDF-first work where the DOCX/EPUB/PDF output fidelity matters, use translate-book (Calibre-based) instead.
- **You don't have rights to the material.** The project's own disclaimer restricts use to works you may legally translate — for copyrighted commercial ebooks, use a licensed translation service (未收录, non-repo) instead.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [translate-book](../agent-skills/writing/translate-book.md) | ✅ | Choose translate-book when term/pronoun consistency across a whole book is the deciding requirement and you live in a coding-agent harness; choose Bilingual Book Maker for scriptable CLI batch runs, bilingual output, and backend freedom. | BBM is older (2023), packaged, MIT, and runs unattended against any OpenAI/Anthropic/MT endpoint; translate-book adds glossary + neighbor-context machinery and multi-format output, but requires Calibre, Pandoc, and an interactive agent. |
| [claude_translater](../agent-skills/writing/claude-translater.md) | ✅ | Choose Bilingual Book Maker over claude_translater in essentially every case: same "translate a book file" job, but licensed, packaged, resumable, and actively released. | claude_translater's only edges are Claude-CLI-native simplicity and a PPTX translator; BBM covers more input formats with a real release process and resume. |
| [Read Frog](read-frog.md) | ✅ | Choose Read Frog when the reading happens in the browser and you want immersive overlays; choose Bilingual Book Maker when you want a finished bilingual ebook file. | Read Frog translates webpages/subtitles in place with BYOK providers — it never emits an EPUB; BBM never touches a webpage. |
| [FluentRead](fluentread.md) | ✅ | Choose FluentRead for Chinese-first in-browser translation with many engines; choose Bilingual Book Maker for owned ebook files and subtitle (srt) translation. | FluentRead lives in the browser tab; BBM is a local CLI producing files — they solve different shapes of the same "read across languages" problem. |

## Tech stack

- **Python 3.10+** — core CLI (`make_book.py`), distributed on PyPI as `bbook-maker`
- **OpenAI/Anthropic-compatible client layer** — plus LiteLLM integration for backend-agnostic routing
- **ebooklib-style EPUB processing** — tag-level classification (`skip`/`translate` verdicts) on JSON-schema endpoints
- **Classic MT engine adapters** — Google, Caiyun, DeepL(+free), Tencent, custom API
- **GitHub Actions CI** — sample-book translation test (`make_test_ebook`)

## Dependencies

- **Python 3.10+** and `pip install -r requirements.txt` (or `pip install -U bbook_maker`)
- **One translation backend**: an API key for OpenAI/Anthropic-format endpoints, Gemini/Qwen/Groq/xAI, LiteLLM, an MT engine, a local Ollama server, or Codex CLI quota
- **Internet access or proxy** for hosted backends (not needed for local Ollama)
- No Calibre, no Pandoc, no database

## Ops difficulty

**Low.** Single CLI command; state lives in the generated `${book_name}_bilingual.*` files plus `--resume` bookkeeping, so interrupted runs continue without re-translating. The operational surface is credential management (`--key`, `--api_base`, or a `bbm_providers.json` file) and picking a model whose context window suits `--use_context session`. Nothing to deploy or daemonize.

## Health & viability

- **Maintenance:** Active — created 2023-03-02, latest release v1.2.1 on 2026-09-14 with tagged releases (v1.1.0, v1.2.0, v1.2.1) and CI translating a sample book (as of 2026-09-18).
- **Governance / bus factor:** Single lead maintainer (`yihong0618`) with a broad contributor base (1286 forks); the maintainer verifiably runs several other popular OSS projects (xiaogpt ~6.9k stars, running_page ~4.5k stars), a track record of not abandoning projects [推断].
- **Backing & longevity (Lindy):** ~3.5 years old and still shipping — the strongest Lindy signal in this comparison set; no organizational backing, but age × still-active both hold.
- **Adoption & ecosystem:** 9.8k stars, PyPI distribution, documented provider matrix, a disclaimer/license posture that shows maintenance maturity.
- **Risk flags:** MIT, no relicense history. Backend API drift (OpenAI/Anthropic format changes) is the standing maintenance tax; quality on classic MT engines (Google/DeepL) is bounded by those services, not by this tool.

## Caveats (unverified)

- [未验证] Per-format fidelity (especially PDF→EPUB fallback and srt timing preservation) is from the README; complex inputs were not exercised here.
- [未验证] The epub tag-classification behavior ("skip/translate verdicts") applies only to endpoints that can hold a conversation; plain MT engines translate `p` tags only, so poetry/verse may be omitted — coverage per endpoint untested.
- [未验证] Cost and wall-clock time per book depend entirely on the chosen backend/model; no official benchmarks.
- [推断] Session-context mode (`--use_context session`) improves local coherence but its 8k default compaction window is far smaller than a book — it does not substitute for a curated glossary on long works.
- [未验证] The Codex-subscription route's rate limits and terms-of-use fit for bulk book translation are not independently confirmed.
