---
name: dsh-libreoffice-kit
slug: dsh-libreoffice-kit
repo: https://github.com/deepseek-ai/dsh-libreoffice-kit
homepage: https://www.npmjs.com/package/@deepseek-ai/libreoffice-kit
aka: [libreoffice-kit, dsoffice]
category: office-automation
tags: [office-to-pdf, libreoffice, document-conversion, nodejs, wasm, fonts, xlsx-recalculation, document-rendering, deepseek-harness]
language: TypeScript
license: MPL-2.0
maturity: "npm v0.1.5 (2026-10-01; public repo source still at 0.1.3), 0.x, active; 53 stars / 2 forks, repo created 2026-09-30 with history from 2026-09-11 (190 commits, 1 committer), ~379k npm downloads/week (as of 2026-10)"
last_verified: 2026-10-01
type: library
upstream:
  pushed_at: 2026-09-30T07:37:00Z
  default_branch: master
  default_branch_sha: b19bb73c74ed893b8a5d1716d32df32a113ed31b
  archived: false
health:
  schema: 1
  computed_at: 2026-10-01T16:39:15Z
  overall: C
  overall_score: 2.0
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 3
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: "@deepseek-ai/libreoffice-kit"
        dependent_repos_count: 0
        downloads_last_month: 538002
        graph_tier: E
        volume_tier: B
        cross_check_divergence: 1.0
        tier_source: registry
    longevity:
      grade: D
      raw:
        repo_age_days: 1
        last_commit_age_days: 2
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: C
      raw:
        spdx_id: MPL-2.0
        permissiveness: weak_file_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: issues_disabled }
---

# dsh-libreoffice-kit

Your Node service has to turn users' `.docx` / `.xlsx` / `.pptx` into PDFs or page images, and the usual answer — install LibreOffice on every host and shell out to `soffice --headless` — means a large system install, a process you have to babysit, and Chinese text that silently comes out in the wrong font. This kit ships a slimmed, prebuilt LibreOffice engine as an npm dependency and gives you one `render` call that picks fonts you control and tells you which ones the document asked for but did not get.

![dsh-libreoffice-kit — health radar](../../assets/health/dsh-libreoffice-kit.svg)

## When to use

You maintain a Node.js app — an Electron-style desktop client, a document-preview backend, a batch job — that receives Office files and must show them as PDF or PNG. Today you either require users to install LibreOffice, or you bake it into a container image and spawn `soffice --headless --convert-to pdf` per file; then a contract written in 宋体 renders in a fallback face with different line breaks, and you have no way to tell the user "this document wanted SimSun and you don't have it". You want the converter to arrive through `npm install`, run offline with no system LibreOffice, and be explicit about fonts.

Reach for this kit then. npm installs a prebuilt engine for your platform (native on macOS/Windows, a WebAssembly build on Linux); `createConverter()` indexes the font directories you choose, `render` / `convert` / `recalculate` / `renderImages` each run in a fresh private engine process with a deadline, cancellation and byte limits, and the result carries a `missingFonts` list. Pick it over [Gotenberg](https://github.com/gotenberg/gotenberg) when you do not want to run a separate HTTP container, and over `libreoffice-convert`-style wrappers or [unoserver](https://github.com/unoconv/unoserver) when you cannot assume LibreOffice is installed on the host.

## How it works

The repository is a build-and-packaging recipe around upstream LibreOffice (a pinned `LibreOffice/core` submodule for the native helper, LibreOffice 26.8 compiled with Emscripten for WASM) plus a TypeScript Node API. The recipe switches off what a converter does not need — Java/Python scripting, database connectivity, PDF import, help, galleries, online-update and WebDAV/LDAP integrations — statically links what remains, and publishes one engine package per platform as an npm *optional dependency*, so npm downloads only the one matching your OS and CPU. At run time the Node API does the parts LibreOffice leaves to you: it scans font directories with `fontkit` (a JS font-file reader), passes the chosen original font files to the engine, starts a brand-new native process or Node worker with a throwaway profile for every single conversion, enforces input/output size limits and a timeout, and deletes partial output on failure. Think of it as a sealed print shop that comes in the box: you hand over a file path and say where the PDF goes; which fonts are on the shelf is still your decision. Your application still owns authorization, storage and the preview UI.

![dsh-libreoffice-kit — backbone user story](../../assets/flow/dsh-libreoffice-kit.svg)

<!-- flow-steps:begin (generated from flows/dsh-libreoffice-kit.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Add the package to your Node app — `npm install @deepseek-ai/libreoffice-kit@0.1.3`
2. **dsh-libreoffice-kit**: npm pulls only your platform's prebuilt engine: native on macOS/Windows, WASM on Linux — component: `platform engine package`
3. **You**: Create a converter, optionally naming your font directories — `createConverter({ timeoutMs: 120_000 })`
4. **dsh-libreoffice-kit**: Indexes the fonts it may use and caches their metadata on disk — component: `Node API (fontkit)`
5. **You**: Call render with an absolute input path and a not-yet-existing output path
6. **dsh-libreoffice-kit**: Starts a fresh private engine, writes the PDF, returns the backend used and missing fonts — component: `native helper or WASM worker`

**Value**: Office files become PDFs inside your Node process with no LibreOffice install or soffice babysitting, and you learn which requested fonts were missing

</details>
<!-- flow-steps:end -->

## When NOT to use

- **Linux servers that need native speed.** On Linux the released path is the WebAssembly engine — native Linux recipes exist in the repo but no Linux native package is published on npm (only macOS and Windows natives are released). WASM layout and PDF export run on the CPU inside a Node worker, and every render starts a fresh engine; for a high-throughput Linux conversion service, run [Gotenberg](https://github.com/gotenberg/gotenberg) (native LibreOffice in a container behind an HTTP API) or [unoserver](https://github.com/unoconv/unoserver) (a warm LibreOffice listener) instead.
- **You need conversion from Python, Go, Java or a shell.** It is a Node ≥ 22.19 library plus a Node CLI (`dsoffice`). From other runtimes, call LibreOffice headless (`soffice --headless --convert-to pdf`) directly, use unoserver from Python, or put Gotenberg behind HTTP.
- **Minimal containers without fonts.** No fonts are bundled or downloaded; the WASM engine uses only the fonts it imports and rejects with `unavailable` if it finds none. If you cannot ship a font set (CJK coverage especially), a [Gotenberg](https://github.com/gotenberg/gotenberg) image that already carries fonts is less work.
- **You need pixel parity with Microsoft Office.** The README states it does not guarantee identical output to Microsoft Office or between engines; fidelity is checked on six synthetic fixtures on one host. For legal or print-exact output, render with real Office (e.g. the Word-automation PDF path that [Office-Word-MCP-Server](office-word-mcp-server.md) wraps) or a commercial engine.
- **You want to edit Office files, not render them.** Apart from `recalculate` (refresh spreadsheet formulas and save), it does not modify documents. For authoring use [python-docx](python-docx.md), [XlsxWriter](xlsxwriter.md) or [Apache POI](apache-poi.md); for an agent that edits and visually checks its own output use [OfficeCLI](officecli.md).
- **Inputs outside the supported shapes.** `.wps`, RTF/HTML renamed to `.doc`, and Word 2003 XML / SpreadsheetML / DocBook (their XSLT filters are pruned) are rejected; PDF is accepted only as input to PNG rendering, not as a conversion source. Use full LibreOffice for long-tail formats.
- **You need a public, reproducible release trail.** The GitHub repo is a public mirror of an internal repository: it has no Releases, no tags, no CI workflows and no issue tracker, engine archives are published to the *internal* repo's Releases, and on 2026-10-01 npm already served 0.1.5 (which adds a `koffi` dependency) while the mirror's source was 0.1.3. If you must build exactly what you run, pin a version you can rebuild from the mirror, or use upstream LibreOffice.
- **Windows hosts without the VC++ runtime.** The Windows engines require the Microsoft Visual C++ v14 Redistributable for the matching architecture, which is not bundled; on locked-down Windows fleets, plan that install or use a server-side converter.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| LibreOffice headless (`LibreOffice/core`, `soffice --headless --convert-to pdf`) | not indexed | Call LibreOffice directly when it is already installed on the host or the caller is not Node; pick this kit when the converter must arrive via `npm install` and run without a system office suite. | Full format coverage and every filter, but a large system install, per-call process startup and font substitution you cannot see. Not added in this tab batch. |
| Gotenberg (`gotenberg/gotenberg`) | not indexed | Run Gotenberg for a language-neutral conversion service on Linux, especially when you also need HTML/URL → PDF via Chromium; pick this kit for in-process Node conversion with no extra container. | A Docker HTTP API with native LibreOffice and Chromium and an 8-year track record, versus an embedded library whose Linux path is WASM and whose history is weeks long. Not added in this tab batch. |
| unoserver (`unoconv/unoserver`) | not indexed | Choose unoserver in Python stacks that already have LibreOffice and want a warm listener to avoid per-file startup; choose this kit when you cannot rely on an installed LibreOffice. | Reuses one running LibreOffice (faster repeated calls, but shared state and process supervision are yours), versus a fresh isolated engine per render that is safer but pays startup each time. Not added in this tab batch. |
| libreoffice-convert (`elwerene/libreoffice-convert`) | not indexed | Use it for a few lines of Node glue when your hosts already have `soffice`; use this kit when you also need bundled engines, font control, timeouts and size limits. | Tiny MIT wrapper around an installed binary, so it is only as portable as your LibreOffice install and offers none of the font reporting. Not added in this tab batch. |
| [OfficeCLI](officecli.md) | ✅ | Pick OfficeCLI when an agent must create or edit Office files and look at an HTML/PNG render of its own work; pick this kit when you need LibreOffice-grade PDF export of arbitrary incoming documents. | OfficeCLI's renderer is in-house HTML (PNG via an external browser); this kit uses LibreOffice's layout engine but cannot author or edit documents. |

## Tech stack

- **Node API:** TypeScript (ESM) compiled with `tsdown`; tests in `vitest` (29 spec files in `packages/entry/tests`) plus Node test runner scripts under `test/`. Runtime deps in the 0.1.3 source: `fontkit` 2.0.4 (font metadata/glyph coverage), `fflate` (ZIP inspection of OOXML), `saxes` (XML parsing for the `missingFonts` scan); npm 0.1.5 adds `koffi` (a Node FFI library).
- **Engines:** LibreOffice core pinned as a submodule (commit `bce0998`), carrying 63 native patches (static linkage, disabled updates/curl/database dialogs, deterministic font matching, PDFium raster); a C++ helper (`engine/native/worker.cxx`) drives LibreOfficeKit. WASM: LibreOffice 26.8 built with Emscripten 4.0.10 and its own patch set; `soffice.data` resources pruned after build.
- **Packaging:** pnpm workspace; per-platform packages `darwin-arm64`, `darwin-x64`, `win32-arm64`, `win32-x64`, `wasm` (Linux), each carrying `prebuilds.json` integrity inventories, source recipes and license notices.

## Dependencies

- Node.js **≥ 22.19.0**.
- One engine package, installed automatically as an npm optional dependency: ~153 MB unpacked for `darwin-arm64` and ~152 MB for `wasm` (npm 0.1.5). Package managers or install flags that skip optional dependencies leave you with an API that rejects `createConverter` with `unavailable`.
- Fonts supplied by you (system/user font directories or explicit `fontDirectories`); none are bundled.
- Windows: Microsoft Visual C++ v14 Redistributable (x64 or ARM64, matching Node).
- No network at install or run time beyond npm itself; no system LibreOffice.

## Ops difficulty

**Low to medium.** Adding it is one npm dependency and a `createConverter` / `dispose` pair; there is no daemon or port. The work is around it: shipping the right fonts to every host, sizing CPU and memory for per-render engine startup (renders on one converter are serialized; concurrency means more converters, ideally from one `createConverterFactory`), making sure your bundler or installer keeps the optional platform package and its `sources/` + `licenses/` folders (MPL-2.0 redistribution), and tracking a 0.x API that shipped 16 npm versions in 16 days. Rebuilding engines yourself is a different job: a full LibreOffice build per platform, documented in `docs/building.md`.

## Health & viability

- **Maintenance (2026-10-01):** very active — 190 commits between 2026-09-11 and 2026-09-29 in the mirror and npm releases almost daily (0.1.3 → 0.1.5 in two days). But the public mirror is a snapshot: no Releases, tags or CI here, and it lagged npm by two versions on the day checked.
- **Governance / bus factor:** a DeepSeek-org repository whose commits all come from one engineer (`yudshj`); npm lists three maintainers, two of them DeepSeek-affiliated by email. The roadmap is set by DeepSeek Harness's needs — an architecture note in that repo (2026-09-14) moved the kit out of the Harness monorepo so engine builds release on their own cycle.
- **Backing & longevity:** backed by DeepSeek and consumed by DeepSeek Harness (`deepseek-ai/deepseek-harness`, ~242k stars), which pins exact kit versions. Age is weeks, so the Lindy prior gives nothing; its future is tied to Harness keeping this component and keeping the mirror public. The description itself calls it "an internal component used by DeepSeek Harness".
- **Adoption:** 538002 npm downloads in the month to 2026-09-29 (~379k of them in the last week), most plausibly pulled in by Harness installs rather than independent users [推断: the package is two weeks old and the repo has 53 stars]. Issues, discussions and the wiki are disabled on the mirror and its pull-request endpoint returns 404, so outside users have no public channel to report a bug or ask a question.
- **Risk flags:** MPL-2.0 (file-level copyleft — fine to embed, but modified kit/engine files must stay open and the bundled notices must ship). Pre-1.0 with a fast-moving API, a mirror that trails npm, and an "internal component" label that gives outside users no support promise.

## Caveats (unverified)

- [推断] Most npm downloads come from DeepSeek Harness installs rather than direct adopters — based on package age and 53 stars; npm does not expose dependents per download.
- [未验证] WASM-on-Linux conversion speed relative to native LibreOffice — the repo ships benchmark tooling but publishes no results; not run here (needs a Linux host and fixture set).
- [未验证] Fidelity beyond the six synthetic DOCX/XLSX/PPTX fixtures on one macOS ARM64 host that the README reports; real-world documents were not tested.
- [未验证] Whether npm 0.1.4/0.1.5 source will be pushed to the public mirror, and why `koffi` was added — not visible in the mirror as of 2026-10-01.
- [未验证] Peak memory per render — the README notes font and output limits do not bound native memory or temporary disk use; no figures are published.
- [推断] Third npm maintainer (`imccyu`) affiliation — not stated anywhere checked.
