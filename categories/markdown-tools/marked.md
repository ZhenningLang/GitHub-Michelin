---
name: marked
slug: marked
repo: https://github.com/markedjs/marked
category: markdown-tools
tags: [markdown, parser, compiler, html, javascript, gfm, commonmark]
language: JavaScript
license: MIT
maturity: v18.x, active (2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-23T04:04:16Z
  default_branch: master
  default_branch_sha: f8f411256680bfc870a4faba729409be68fcef4b
  archived: false
health:
  schema: 1
  computed_at: 2026-09-19T08:52:24Z
  overall: A
  overall_score: 3.8
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 3
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 6.6
        qualifying_issues: 18
        band: default
        window_offset_days: 6
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: marked
        dependent_repos_count: 468889
        downloads_last_month: 78935009
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 2.67
    longevity:
      grade: A
      raw:
        repo_age_days: 5458
        last_commit_age_days: 3
        cohort: library
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 18
        top1_share: 0.554
        top3_share: 0.662
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# marked

A fast, low-level Markdown parser and compiler for JavaScript — turns Markdown into HTML in a single function call, with no required dependencies and a small API surface ("Built for speed").

![marked — health radar](../../assets/health/marked.svg)

## When to use

You're building a web app — a comment box, a docs viewer, a chat client, a README renderer — and you need to turn user- or author-written Markdown into HTML, in the browser or in Node, without pulling in a heavy toolchain. You want `import { marked } from 'marked'` and then `marked.parse(src)` to just give you an HTML string, fast, with sane GFM-leaning defaults (tables, fenced code, autolinks). You drop it in, wire the output into your DOM (after sanitizing — see below), and you're done; there's no AST to learn, no plugin manifest to assemble, no build step beyond your normal bundler.

It's the right reach when *throughput and simplicity* matter more than strict spec conformance: rendering many small Markdown snippets per page, server-side rendering a docs site, or any place where you'd otherwise hand-roll a regex and regret it. marked compiles to a compact bundle, runs the same in Node and the browser, and exposes just enough hooks (a `renderer`, a `walkTokens` pass, a lexer you can call directly) to customize output without adopting a whole pipeline.

## When NOT to use

- **You need 100% CommonMark conformance.** marked is fast and CommonMark/GFM-*leaning* but is **not** fully spec-compliant by default — edge cases diverge from the reference. If exact spec behavior is a hard requirement, use markdown-it (CommonMark-strict) or remark. [推断]
- **You're rendering untrusted Markdown without sanitizing.** marked does **not** sanitize its output HTML — raw HTML and crafted links pass straight through, so naive use is an XSS hole. You **must** run the output through DOMPurify (or equivalent) yourself; sanitization was deliberately removed from marked's own scope.
- **You want to transform Markdown as an AST / mdast pipeline.** marked's token model is for rendering, not a general document-transform toolchain. For linting, rewriting, MDX, or plugin-based AST passes, reach for remark / unified.
- **You depend on a large plugin ecosystem.** marked has extensions but nothing like markdown-it's plugin catalog. If you need footnotes, containers, KaTeX, task lists, etc. as off-the-shelf plugins, markdown-it or remark will have more ready-made parts.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [markdown-it](markdown-it.md) | ✅ | Choose markdown-it when you need CommonMark-strict parsing, pluggable architecture, and a rich plugin ecosystem. | CommonMark-strict, pluggable architecture with a rich plugin ecosystem; heavier API and a touch slower than marked, but the choice when spec conformance and plugins matter. |
| [remark](remark.md) | ✅ | Choose remark when you need a full mdast AST pipeline for parsing, transforming, linting, and serializing Markdown or MDX. | Full mdast AST pipeline for parsing, transforming, linting, and serializing (Markdown, MDX); far more powerful and far heavier — a toolchain, not a one-call renderer. |
| [micromark](micromark.md) | ✅ | Choose micromark when you need the low-level CommonMark/GFM tokenizer underneath remark. | The low-level CommonMark/GFM tokenizer underneath remark; correct and streaming-oriented, but you build the rendering layer yourself. |
| [CommonMark](commonmark.md) | ✅ | Choose CommonMark when you need the spec's own reference implementation. | The spec's own reference implementation; the conformance yardstick, but fewer GFM niceties and not optimized as a production renderer. |

## Tech stack

- **Language:** JavaScript (the published source ships JS plus TypeScript type definitions; the repo also contains TS and HTML for tooling/docs). [推断]
- **Runtime targets:** runs in Node and in the browser; distributed as ESM and UMD/CJS builds and via CDN.
- **Architecture:** a lexer/tokenizer that turns Markdown into tokens, then a parser/renderer that emits HTML; customization via a `Renderer`, `Tokenizer`, `walkTokens` hook, and an extension API.
- **Flavors:** GFM-leaning defaults (tables, strikethrough, autolinks, fenced code) on top of a CommonMark-ish core.

## Dependencies

- **Runtime:** none required — marked is dependency-light by design and works standalone. [未验证]
- **Sanitizer (yours to add):** for any untrusted input you must pair it with DOMPurify or another HTML sanitizer — not bundled, deliberately your responsibility.
- **Install:** `npm install marked`, or load the prebuilt bundle from a CDN; also exposes a CLI (`marked`) for command-line conversion.

## Ops difficulty

**Low.** It's a library, not a service — there is nothing to deploy or operate beyond adding a dependency to your app. The only real operational concern is the security one: remember to sanitize output before injecting it into the DOM, and pin/track the major version since the API has changed across majors. No datastore, no runtime, no infra.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 6.6 hours across 18 qualifying issues/PRs.
- **Maintenance — active (last push 2026-06).** Regular releases through the v18.x line (v18.0.5 dated 2026-06-04); a healthy, low-issue-count repo (~16 open issues at ~36k stars) for a mature parser whose scope is deliberately small and settled [未验证].
- **Governance & bus factor.** `Org`-owned (`markedjs/`) — a maintainer team / org rather than a single person, which de-risks the bus factor versus a one-author library [推断]. Long-running community project, not vendor-controlled; no commercial tier gating features.
- **Age & Lindy verdict — old and still active ⇒ strong Lindy.** Created 2011 (~15y old) and still shipping in 2026: the textbook age × still-active signal. A 15-year-old parser still cutting releases is about as safe a longevity bet as this category offers; the API has moved across majors, so pin and track the major version.
- **Risk flags — minimal, but security is on you.** MIT-licensed, no relicensing history, no open-core gating. The one standing caveat is by design: marked does **not** sanitize output, so untrusted input must be passed through DOMPurify yourself — a usage responsibility, not a project-health flag.

## Caveats (unverified)

- [未验证] ~36.9k GitHub stars and latest release in the v18.x line (v18.0.5, dated 2026-06-04) as of 2026-06; star counts and versions drift release-to-release — treat as indicative.
- [推断] "Not fully CommonMark-compliant by default" reflects marked's long-standing positioning as a speed-first, spec-leaning parser; exact divergences depend on the version and your config — verify against the current spec test suite if conformance is critical.
- [未验证] "No required runtime dependencies" is marked's own framing; confirm against the current `package.json` for your version, especially if you enable optional features.
- [推断] License is MIT (GitHub's auto-detection may show NOASSERTION for the repo); confirm via the repo's LICENSE file for your pinned version.
