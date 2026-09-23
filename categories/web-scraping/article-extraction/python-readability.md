---
name: python-readability
slug: python-readability
repo: https://github.com/buriy/python-readability
category: article-extraction
tags: [content-extraction, readability, lxml, article-parsing, python, html]
language: Python
license: Apache-2.0
maturity: v0.8.x, maintained (low cadence), ~2.9k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-01-26T13:06:04Z
  default_branch: master
  default_branch_sha: 701833ccb24f9a15b463434f78229e4d6daf1c79
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:13:26Z
  overall: A
  overall_score: 3.67
  scored_axes: 3
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 26
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: A
      raw:
        repo_age_days: 5622
        last_commit_age_days: 26
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    adoption: { reason: ambiguous }
    governance: { reason: fork }
---

# python-readability

A fast, lxml-based Python port of arc90's Readability — hand it an HTML document and it returns the cleaned main body (`summary()`) and the title (`title()`), stripping nav, ads, and boilerplate.

![python-readability — health radar](../../../assets/health/python-readability.svg)

## When to use

You're writing a Python scraping or content pipeline — feeding an LLM, building a search index, or archiving articles — and `requests.get(url).content` gives you a full page when you want the article. You don't want to spin up a headless browser or a Node DOM just to extract text. You reach for python-readability: `pip install readability-lxml`, then `Document(html).summary()` for the cleaned article HTML and `Document(html).title()` for the title. It's pure Python on lxml, so it's fast and slots straight into a `requests`/`httpx` flow with no browser, no Node, and no service. It descends from the same arc90 Readability lineage as the JS version, so its heuristics are familiar and reasonably robust on real-world pages, with options like `positive_keywords`/`negative_keywords` and `keep_all_images` to tune behavior.

You also reach for it when you specifically want the *Python, lxml* implementation — e.g. you already depend on lxml/cssselect, you want CJK-aware extraction (recent versions improved CJK support), or you need a small, embeddable extractor rather than a heavier ML model. It's the pragmatic default when your stack is Python and the input HTML is already fetched.

## When NOT to use

- **Your pages are JS-rendered.** It parses static HTML; it does not run JavaScript or fetch URLs. For SPAs you must render first (Playwright/headless) and pass the resulting HTML.
- **You want richest extraction/metadata or best benchmark accuracy.** Newer Python extractors (e.g. trafilatura) often extract more metadata and score better on extraction benchmarks; if quality is paramount, evaluate them too. [未验证]
- **You need a maintained, fast-moving project.** Maintenance is real but **slow** — the last tagged release on GitHub is old even though the code is still touched; don't expect rapid fixes. Verify behavior on your inputs. [推断]
- **You need structured field extraction.** It returns the article body + title, not arbitrary structured data (prices, tables, product specs) — that's a different scraping job.
- **You're not in Python.** For JS use [Readability.js](readability-js.md); ports differ in heuristics and output.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Readability.js](readability-js.md) | ✅ | Choose Readability.js when you need Mozilla's JavaScript engine behind Firefox Reader View. | Mozilla's JS engine behind Firefox Reader View; choose by language (JS/Node) — different heuristics, needs a DOM. |
| [dragnet](dragnet.md) | ✅ | Choose dragnet when you need ML-based extraction in Python. | ML-based extraction (Python); can win on some pages but is heavier, has aging pinned deps, and is less maintained. |
| [boilerpipe](boilerpipe.md) | ✅ | Choose boilerpipe when you need Java boilerplate-removal algorithms. | Java boilerplate-removal algorithms; classic but the repo is effectively abandoned (last pushed 2018). |
| [trafilatura](trafilatura.md) | ✅ | Choose trafilatura when you need a modern Python extraction library with benchmarks, metadata, and crawl features. | Modern Python extraction library with strong benchmarks, metadata, and crawl features; often the current Python default — broader scope, heavier. |
| newspaper3k / goose3 | 未收录 | Choose newspaper3k or goose3 when you need article extraction with built-in fetching and metadata. | Article-extraction libraries with built-in fetching and metadata; convenient but historically uneven maintenance. |

## Tech stack

- **Language:** Python.
- **Core deps:** **lxml** (`lxml[html_clean]`, with `lxml-html-clean` on Python <3.11), **chardet** (encoding detection), and **cssselect**.
- **API:** `from readability import Document` → `Document(html).summary()` (cleaned article HTML) and `.title()`; options include `positive_keywords`, `negative_keywords`, `keep_all_images`, and explicit `encoding`.
- **Distribution:** published on PyPI as `readability-lxml` (also conda-forge).

## Dependencies

- **Runtime:** Python plus lxml, chardet, cssselect — all pip-installable, no system services. lxml carries native (libxml2) bindings, so wheels matter on some platforms. [推断]
- **No fetching:** it does not retrieve URLs; you bring the HTML (via `requests`/`httpx`/your crawler).
- **No DOM/Node/browser:** unlike the JS port, no DOM runtime is needed.
- **Install:** `pip install readability-lxml` or `conda install -c conda-forge readability-lxml`.

## Ops difficulty

**Low.** It's a small library, not a service — nothing to deploy or run. The only practical considerations are installing lxml (native dependency; usually a prebuilt wheel, occasionally a build), supplying fetched HTML yourself, and validating extraction quality on your target sites. At scale it's CPU-bound parsing with no external state — trivially parallelizable across workers.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-06).** Last pushed 2026-01, so the repo is **still touched** — but the newest GitHub release tag is old (v0.8.1 dates to 2020), with the changelog mentioning later 0.8.x work; treat it as **maintained but low-cadence / coasting**, not fast-moving. Not archived. [推断]
- **Governance / bus factor.** Owner type is **User** (`buriy`), i.e. an individual-maintainer project with community contributions — a **bus-factor flag**: continuity depends largely on one person. [推断]
- **Age × Lindy (2026-06).** Created 2011-05 — ~15 years old and **still occasionally maintained** ⇒ a **strong Lindy** signal for a small extractor; it has long outlived most peers. Long life here is real durability, not abandonment. [推断]
- **Adoption & ecosystem.** ~2.9k stars, on PyPI and conda-forge, and a long-standing default in many Python scraping stacks indicate solid niche adoption. ~37 open issues is small/manageable. [未验证]
- **Risk flags.** Single-maintainer bus factor and slow cadence are the real ones; for accuracy-critical work, benchmark against trafilatura. Apache-2.0, no relicense history found. [推断]

## Caveats (unverified)

- [未验证] ~2.9k stars as of 2026-06; the newest GitHub release tag is v0.8.1 (2020) while the changelog references later 0.8.x versions — version reporting here is approximate ("v0.8.x"); confirm the exact current PyPI version before pinning.
- [推断] "Maintained but low-cadence / coasting" is inferred from the 2026-01 push date combined with the stale release tag — the gap between code activity and tagged releases.
- [推断] Single-maintainer bus factor is inferred from `owner.type == User`; the actual contributor breadth/succession plan was not verified.
- [推断] lxml's native (libxml2) build/wheel consideration is general lxml knowledge, not verified against this repo's current packaging.
- [未验证] Comparative accuracy vs trafilatura/newspaper3k reflects general positioning, not a measured benchmark.
