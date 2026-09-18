---
name: XlsxWriter
slug: xlsxwriter
repo: https://github.com/jmcnamara/XlsxWriter
homepage: https://xlsxwriter.readthedocs.io
category: office-automation
tags: [xlsx, excel, spreadsheet, python, library, charts, document-generation, office, zero-dependency]
language: Python
license: BSD-2-Clause
maturity: "v3.2.9 (PyPI 2025-09-16), active (last push 2026-08-04); 4.0k stars / 671 forks / 30 open issues, created 2013-01-04 (API-verified), ~13.7-year-old repo"
last_verified: 2026-09-18
type: library
upstream:
  pushed_at: 2026-08-04T23:41:16Z
  default_branch: main
  default_branch_sha: 5d4606d89a955226d2d0825a0f44309043ae7251
  archived: false
health:
  schema: 1
  computed_at: 2026-09-18T12:28:25Z
  overall: B
  overall_score: 3.17
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 45
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 0.6
        qualifying_issues: 4
        band: default
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: xlsxwriter
        dependent_repos_count: 3828
        downloads_last_month: 87471871
        graph_tier: B
        volume_tier: A
        cross_check_divergence: null
    longevity:
      grade: A
      raw:
        repo_age_days: 5005
        last_commit_age_days: 45
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.875
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: BSD-2-Clause
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# XlsxWriter

A zero-dependency Python module for **writing** Excel `.xlsx` files — 13+ years old, production-stable, and write-only by design: it cannot read or modify a workbook it did not create.

![XlsxWriter — health radar](../../assets/health/xlsxwriter.svg)

## When to use

You're generating spreadsheets from data — a financial model, a report export, a large batch of formatted rows — inside a Python service, and the file is created from scratch rather than edited. You reach for XlsxWriter because it is the **leanest and fastest** way to do that: `setup.py` declares no `install_requires` at all and the README states it "uses standard libraries only" (verified 2026-09-18), it supports Python 3.8+ and PyPy3, it carries a `Development Status :: 5 - Production/Stable` classifier, and it keeps only **30 open issues** against 3,972 stars — an unusually well-triaged backlog. It covers full formatting, merged cells, defined names, charts, autofilters, data validation, conditional formatting, images (PNG/JPEG/GIF/BMP/WMF/EMF), rich multi-format strings, cell comments, textboxes, VBA macro insertion, and a memory-optimization mode for large files, plus first-class Pandas and Polars integration. Versus [OfficeCLI](officecli.md) you trade the single binary and the agent-facing CLI for a library you can pin and unit-test with no network egress; versus [python-pptx](python-pptx.md) it is the actively maintained sibling (python-pptx itself depends on `XlsxWriter>=0.5.7` for chart workbooks). Pick it when the job is *data → new .xlsx* and nothing else.

## When NOT to use

- **You need to read or modify an existing workbook** → XlsxWriter is write-only; it cannot open a file. Use openpyxl (`未收录` — see Caveats for why it is not indexed) for read+write of existing `.xlsx`, or [OfficeCLI](officecli.md) when the consumer is an agent rather than a script.
- **The consumer is an LLM agent, not your code** → use [OfficeCLI](officecli.md). An agent cannot `import xlsxwriter`; it needs a CLI or MCP surface. XlsxWriter is the right choice *inside* a tool you build for the agent, not as the agent's interface.
- **You need `.xls` (Excel 97-2003), CSV, or ODS output** → XlsxWriter writes only Excel 2007+ `.xlsx`. Use [Pandoc](../markdown-tools/pandoc.md) or a converter for other targets, and plain `csv` from the stdlib for delimited output.
- **Formula results must be cached in the file** → XlsxWriter writes formulas but cannot calculate them; it stores a cached result of `0` unless you supply one via `write_formula(..., value=)`. Any consumer that trusts the cache without recalculating — notably `openpyxl` with `data_only=True`, and most headless readers — will see zeros. If your reader cannot recalculate, compute values yourself before writing.
- **Pivot tables, slicers, or Power Query** → out of scope; the feature surface is charts, formatting, and data. Use [OfficeCLI](officecli.md), which documents pivot tables with multi-field grouping, calculated fields, and slicers.
- **You need it to stay dependency-free *and* read files** → those two requirements conflict here. openpyxl reads but pulls in `et_xmlfile`; XlsxWriter has no deps but only writes. Decide which constraint is load-bearing first.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [OfficeCLI](officecli.md) | ✅ | Pick XlsxWriter when a Python service generates new workbooks and you want zero dependencies, a pinnable version, and 13 years of stability; pick OfficeCLI when an agent must read, edit, or create spreadsheets through a CLI, or when you need pivot tables and slicers. | XlsxWriter is write-only with no agent surface and no public formula evaluation; OfficeCLI reads, edits, creates, and evaluates 350+ claimed functions, but is a 6-month solo-authored binary with no public test suite and default-on auto-update. |
| openpyxl | 未收录 | Pick openpyxl when you must **read or modify an existing** `.xlsx` — that is the one thing XlsxWriter cannot do at all; pick XlsxWriter when you are creating a file from scratch and want speed plus zero dependencies. Not indexed because its canonical repository is on Heptapod (Mercurial), not GitHub, and this index's health/upstream tooling is GitHub-only — a known gap, not a judgment against it. | openpyxl buys read+write and formula-cache access at the cost of slower writes and an extra dependency; XlsxWriter buys speed and dependency-freedom at the cost of being unable to open a file. |
| [python-pptx](python-pptx.md) | ✅ | Not substitutes but a real coupling: pick python-pptx for the deck and accept that it pulls XlsxWriter in for chart workbooks; pick XlsxWriter alone when the deliverable is the spreadsheet itself. | python-pptx has been coasting since 2024-08-07 while XlsxWriter shipped v3.2.9 on 2025-09-16 and pushed 2026-08-04 — the same ecosystem, very different maintenance states. |
| [MarkItDown](../document-parsing/markitdown.md) | ✅ | Pick MarkItDown when the direction is `.xlsx` → Markdown for LLM ingestion; pick XlsxWriter when the direction is data → `.xlsx`. They are opposite ends of the pipe and never compete. | MarkItDown is read-only and drops formatting by design; XlsxWriter is write-only and preserves full formatting but cannot read anything back. |

## Tech stack

Pure Python, `requires-python >=3.8`, PyPy3 supported. **Zero runtime dependencies** — `setup.py` declares no `install_requires` (verified 2026-09-18) and the README states it "uses standard libraries only". Packaging is classic `setup.py` + `setup.cfg` (no `pyproject.toml`), version 3.2.9. Writes the OOXML `SpreadsheetML` ZIP+XML format directly. Ships a `constant_memory` mode that writes rows sequentially without holding the workbook in memory, which is the mechanism behind large-file generation. Includes `examples/vba_extract.py` as an installed script for pulling `vbaProject.bin` out of a macro-enabled workbook so it can be re-inserted. Docs on Read the Docs; default branch `main`.

## Dependencies

None. Python 3.8+ and its standard library are the entire requirement. No Excel, no LibreOffice, no C extension, no network access, no database, no GPU. This is the strongest dependency story in the category — [python-docx](python-docx.md) needs `lxml`, [python-pptx](python-pptx.md) needs Pillow + lxml + XlsxWriter, and [OfficeCLI](officecli.md) needs an external browser for PNG export. The flip side: because nothing recalculates formulas, **your own code becomes the dependency** for any computed value you want cached in the file.

## Ops difficulty

**Low — the lowest in this category.** `pip install XlsxWriter`, no service, no configuration, no state, no egress. Only 30 open issues against ~4k stars means the surface you are likely to hit a bug in is small and well-documented. Operationally the two things to plan for are: (1) formula caching — decide up front whether you compute values in Python and pass them to `write_formula(..., value=)`, because downstream headless readers will otherwise see `0`; (2) memory profile on very large workbooks — switch on `constant_memory` mode, accepting that rows must then be written in order and cannot be revisited. Neither is a deployment burden; both are design decisions you must make before writing code.

## Health & viability

- **Maintenance: active and steady, verified** — v3.2.9 released 2025-09-16; last push 2026-08-04; 1,492 default-branch commits (API-verified 2026-09-18). Release cadence is measured rather than frantic, which suits a stable library.
- **Governance: single-author, demonstrated endurance** — `jmcnamara` (John McNamara) authored 1,392 of 1,492 commits (**93.3%**); 50 contributors total, second place has 14. No foundation or corporate backing. [推断] Bus factor is 1, but as with [python-docx](python-docx.md) the project has already survived ~13.7 years of solo stewardship while remaining active — the Lindy prior credits demonstrated continuity, not headcount.
- **Age / Lindy: strong on both halves** — created 2013-01-04 (~13.7 years) **and** still pushing in 2026. This is the healthiest age × still-active profile in the category; [python-pptx](python-pptx.md) has the age but not the activity, and [OfficeCLI](officecli.md) has the activity but not the age.
- **Adoption: broad and load-bearing** — 3,972 stars / 671 forks; `Development Status :: 5 - Production/Stable`; documented Pandas and Polars integration; and it is a **runtime dependency of [python-pptx](python-pptx.md)** (`XlsxWriter>=0.5.7`), so it ships inside a large share of Python deck-generation stacks whether or not the author chose it. The author also maintains the Perl equivalent (`Excel::Writer::XLSX`), indicating long-term domain commitment. [推断]
- **Risk flags** — no relicense history (BSD-2-Clause throughout); no open-core gating; no CVE record surfaced during this review; no telemetry or network code. The live risks are narrow: write-only scope means it can never grow into an editing tool without a rewrite, and formula results are not calculated, which silently produces zeros in cache-trusting readers.

## Caveats (unverified)

- [未验证] openpyxl is named as the read+write alternative throughout this page but is **not indexed**: its canonical repository is `https://foss.heptapod.net/openpyxl/openpyxl` (Mercurial/Heptapod, per PyPI `Source` metadata, verified 2026-09-18) and there is no official GitHub repository — only a stale 202-star Bitbucket-era clone. This index's `tools/health.py` and `tools/upstream_snapshot.py` both hard-parse `github.com/owner/name`, so openpyxl cannot be scored or snapshotted here. Recorded as a known index gap, not as a judgment against openpyxl.
- [未验证] The claim that XlsxWriter writes a cached formula result of `0` unless `value=` is supplied — this is the library's documented behaviour and the reason [OfficeCLI](officecli.md) ships a `FormulaCache` handler, but it was not executed against a real workbook in this review.
- [未验证] Relative write speed versus openpyxl — "faster" reflects the library's write-only design and the community's usual framing, not a benchmark run here.
- [未验证] Whether `constant_memory` mode's ordering restriction breaks any specific chart or formatting feature — the mode's existence is verified from the README; its interaction matrix was not tested.
- [推断] The author's continued maintenance of the Perl `Excel::Writer::XLSX` is inferred from the `jmcnamara@cpan.org` author email in `setup.py` and the project's public history; the Perl repository was not fetched for this review.
- [未验证] That 50 listed contributors covers the full history — GitHub's contributors API caps results and excludes unlinked email identities, as it did for [python-docx](python-docx.md); the 93.3% single-author share may be slightly understated or overstated.
