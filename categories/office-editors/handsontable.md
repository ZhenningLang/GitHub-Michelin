---
name: Handsontable
slug: handsontable
repo: https://github.com/handsontable/handsontable
homepage: https://handsontable.com
category: office-editors
tags: [data-grid, spreadsheet-ui, editing, formulas, validation, react, angular, vue, javascript, commercial-license]
language: JavaScript
license: Custom (free non-commercial + paid commercial)
maturity: "18.1.1 (released 2026-09-15), very active (pushed 2026-09-25); 22.1k stars, created 2011-05-23; npm handsontable ~1.16M downloads/month (all API/registry-verified 2026-09-27)"
last_verified: 2026-09-27
type: library
upstream:
  pushed_at: 2026-09-25T16:04:32Z
  default_branch: develop
  default_branch_sha: 1a71fbcf7e6b79f29496fb9cce5352a6862adb17
  archived: false
health:
  schema: 1
  computed_at: 2026-09-27T14:09:35Z
  overall: A
  overall_score: 3.8
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 7.6
        qualifying_issues: 22
        band: default
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: handsontable
        dependent_repos_count: 951
        downloads_last_month: 1195565
        graph_tier: C
        volume_tier: B
        cross_check_divergence: 1.03
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 5606
        last_commit_age_days: 2
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 25
        top1_share: 0.238
        top3_share: 0.556
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Handsontable

Your internal app's power users refuse to fill forms — they want to paste a block from Excel, arrow between cells, drag a fill handle, and get a red border when a value is out of range. Building that keyboard-and-clipboard UX yourself never ends. Handsontable is a JavaScript data grid with spreadsheet look and feel: 15 years of accumulated editing semantics (validation, conditional formatting, merged cells, frozen panes, 400 formulas via HyperFormula) that you mount as a component in React, Angular, Vue — or no framework at all.

![Handsontable — health radar](../../assets/health/handsontable.svg)

## When to use

You're shipping a B2B tool — ERP grid, inventory planner, financial entry sheet — where the data has *your* schema and your backend is the source of truth; you don't need workbooks, sheets tabs, or a document format, you need one editable table that behaves like a spreadsheet. Handsontable is the most battle-tested component in that exact niche (created 2011, still shipping monthly-quality releases in 2026; ~1.16M npm downloads/month). You pick it over [Jspreadsheet CE](jspreadsheet.md) when the enterprise feature surface decides it — server-side data paging, row pagination, merged cells with conditional formatting (all in its README's feature list) — and over [Univer](univer.md) when a DOM grid bound to your own data array is a better fit than adopting a whole editor *framework* with a canvas renderer. And you can name its quiet cost up front: **commercial use requires a paid license** — the repo is no longer open source (MIT → custom non-commercial license at v7.0, 2019, per the vendor's own blog). For many teams that invoice is still cheaper than the engineering quarter they'd spend cloning its keyboard model.

## How it works

You hand the component a 2D array (or objects) plus column declarations — type, editor, validator — and it renders a virtualized DOM table whose cells behave like Excel's: selection, copy/paste to and from real spreadsheets, undo/redo, IME-safe typing. Formula work is delegated to HyperFormula, the same vendor's calculation engine ("400 built-in formulas via native integration", README), so `=VLOOKUP` in a cell actually evaluates and recalculates on edit. Validation and conditional formatting run on the grid's own state, and the server-side data module lets you keep the source of truth in your API with the grid as a paged window over it. What you do: configure columns, wire events (`afterChange` etc.), and buy a license key string for anything commercial — the README's own sample passes `licenseKey: 'non-commercial-and-evaluation'` and says plainly that commercial products need a purchased key.

![handsontable — backbone user story](../../assets/flow/handsontable.svg)

<!-- flow-steps:begin (generated from flows/handsontable.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install the grid (wrappers exist for React/Angular/Vue) — `npm install handsontable`
2. **You**: Declare columns: type, editor, and validator per field — `{ data: 'company', title: 'Company', width: 100 }`
3. **You**: Start on the free evaluation key, swap in the purchased one — `licenseKey: 'non-commercial-and-evaluation'`
4. **Handsontable**: Renders a virtualized grid with spreadsheet keyboard + clipboard — component: `data grid core`
5. **Handsontable**: Evaluates cell formulas through HyperFormula's 400 functions — component: `HyperFormula`
6. **Handsontable**: Runs data validation and conditional formatting as you type — component: `validators & formatting`

**Value**: Power users keep their Excel muscle memory inside your product — and you never write the keyboard, clipboard, and recalculation layer yourself

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You cannot buy a software license** → the free tier covers non-commercial and evaluation use only (README *Licenses* section). For a zero-invoice grid, use [Jspreadsheet CE](jspreadsheet.md) (MIT) or [Fortune Sheets](fortune-sheets.md) (MIT); for a zero-invoice full editor, [Univer](univer.md).
- **You're building a spreadsheet *product*, not a grid *in* a product** → users want tabs, cell comments-as-threads, docx alongside the sheet? That's a document model, which Handsontable explicitly disclaims ("not a spreadsheet", its own FAQ heading). Use [Univer](univer.md) (embed a workbook) or [ONLYOFFICE Docs](onlyoffice-documentserver.md) (drop in a suite).
- **You need .xlsx round-trip as files** → "Export to Excel" ships, but opening arbitrary user-uploaded workbooks with formulas/styles intact is a document-server problem. Choose [ONLYOFFICE Docs](onlyoffice-documentserver.md), or pair the grid with [SheetJS](https://github.com/SheetJS/sheetjs) (`未收录` — file-format library, out of this batch's editor scope; add separately).
- **Your bottleneck is data volume, not editing UX** → tens of thousands of *rows rendered for viewing* is a virtualized-grid-for-analytics job: [AG Grid](https://github.com/ag-grid/ag-grid) (`未收录` — general analytics grid without spreadsheet editing depth; deliberately not added in this batch). Handsontable virtualizes, but its budget is editing interaction, not million-row browsing.
- **You need the engine headless on the server** (batch-apply edits, validate a CSV in a cron) → Handsontable is browser UI; formula math can split off into HyperFormula (`未收录` — separate vendor repo), but if the whole point is headless office runtime, [Univer](univer.md) runs the same stack in Node.
- **Single-vendor dependency scares you** → development is Handsoncode sp. z o.o.; top 3 accounts (warpech 2,554 / jansiegel 1,973 / budnix 1,789) are its team (contributors API 2026-09-27), and the 2019 relicensing shows which way the needle moves when the vendor needs revenue. A foundation-governed alternative in this category is [Grist](grist.md)'s Apache core.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [Jspreadsheet CE](jspreadsheet.md) | ✅ | Pick Handsontable when a paid, 15-year-old enterprise grid with vendor support is the safer bet for a revenue-bearing B2B tool; pick Jspreadsheet when the same job must cost zero license dollars and "Excel-ish paste + typed columns" is 90% of the requirement. | Handsontable buys depth and support on an invoice; Jspreadsheet buys MIT freedom on a thinner (and Pro-funnel-shaped) surface. |
| [Fortune Sheets](fortune-sheets.md) | ✅ | Pick Handsontable for a maintained grid with commercial backing; pick Fortune Sheets when you need full Excel *sheet* semantics (merges, conditional formatting, formula bar) inside one MIT component and can stomach a repo with no commits since 2025-12-15. | Handsontable: supported product, less Excel-shaped, not free. Fortune: more sheet, no support, stalled. |
| [Univer](univer.md) | ✅ | Pick Univer when the deliverable is a workbook experience your users (or agents) drive — tabs, docs, headless Node — under Apache-2.0; pick Handsontable when your product shows a schema-bound editable table and you'd rather configure a grid than assemble an editor framework. | Univer: framework breadth, free license, younger. Handsontable: component simplicity, mature UX, paid. |
| [ONLYOFFICE Docs](onlyoffice-documentserver.md) | ✅ | Pick ONLYOFFICE when users must open and co-edit real .xlsx/.docx files from their storage; Handsontable only when the data lives in *your* tables and the spreadsheet is an input widget, not a document. | ONLYOFFICE: whole suite in a container, AGPL, server to run. Handsontable: npm-sized footprint, file fidelity isn't its job. |
| HyperFormula | `未收录` | If formulas-on-the-server without any UI is the entire need, evaluate HyperFormula (same vendor) before importing a grid at all; `未收录` because this batch indexes editing surfaces, not calculation libraries. | Buys pure-JS formula evaluation; no grid, and it inherits the vendor's open-core posture. |

## Tech stack

JavaScript/TypeScript (GitHub linguist: JS ≈12.1M, TS ≈11.0M bytes, verified 2026-09-27), DOM-based rendering with row/column virtualization, formulas via HyperFormula integration, theming system incl. dark mode, official React/Angular/Vue3 wrappers, SCSS for styles, Jest-based CI on GitHub Actions, CLA on contributions (cla.handsontable.com). Server-side data module for paged API-backed datasets. No canvas engine, no document model — it's a component, by design (README "Is Handsontable a Data Grid or a Spreadsheet?").

## Dependencies

None beyond the browser and a bundler; the npm package includes its framework wrappers as separate packages. No backend of its own — persistence is whatever you already run. Formula evaluation can run in Web Workers (HyperFormula architecture) [未验证 — worker configuration not checked in this review]. A paid license key string is, practically, a build-time dependency for commercial products.

## Ops difficulty

**Low** mechanically: it's an npm dependency with a major-version upgrade rhythm (v18 line, Sept 2026) and paid support tickets if you buy them. **Medium** contractually: upgrades interleave with license renewals (per-seat/per-project pricing at handsontable.com/pricing), and the 2019 MIT→proprietary transition is the standing precedent that terms change. Budget the license conversation once, then it's just another grid to version-bump.

## Health & viability

- **Maintenance: strong and dated.** 18.1.1 released 2026-09-15, pushed 2026-09-25, release candidates flowing the same month (API-verified) — an active commercial train, not a coasting OSS repo.
- **Governance: single-vendor, openly so.** Handsoncode sp. z o.o. (Kraków) is the company behind it; the repo exists to sell the product. Top contributors are the vendor team (warpech 2,554 / jansiegel 1,973 / budnix 1,789, API 2026-09-27). CLA required.
- **Backing & longevity: the category's best Lindy.** Created 2011-05-23 — 15 years *and still active* (age × still-active). It survived jQuery-era competition, React-era competition, and the jExcel/Luckysheet wave; that's the record Univer and Fortune Sheets don't have.
- **Adoption: measured.** The health radar records 1,195,565 monthly npm downloads and 951 dependent repos for `handsontable` (a same-day registry read gives 1,159,820) — the most-downloaded editing surface in this category's batch [推断 — among the 7 pages indexed here].
- **Risk flags** — **it is not open source**: free only for non-commercial/evaluation since v7.0 (2019 blog: "The MIT license has been replaced with a custom free for non-commercial license"); commercial use without a key violates terms even though the code is publicly readable; pricing leverage sits entirely with one Polish company.

## Caveats (unverified)

- [未验证] Current commercial pricing/seat model — handsontable.com/pricing was not fetched; "invoice needed" is sourced from the repo README's license section text.
- [未验证] Exact 2019 relicensing date attributed to v7.0.0 — the vendor blog title ("Handsontable 7.0.0 is here! … MIT license has been replaced") and its HN discussion (Jan 2019) corroborate, but the blog body timestamp wasn't opened.
- [未验证] HyperFormula Web Worker setup and whether formula evaluation stays in-thread by default in v18.
- [未验证] "Export to Excel" fidelity (styles/formulas in output .xlsx) — feature listed in README; no file was produced and opened in Excel here.
- [推断] Calling downloads "the most in this category's batch" compares only the four npm-published members of this batch; Grist/ONLYOFFICE/Collabora don't ship through npm with comparable signal.
