---
name: markdown-it
slug: markdown-it
repo: https://github.com/markdown-it/markdown-it
category: markdown-tools
tags: [markdown, parser, commonmark, gfm, plugin, javascript, html, tokenization]
language: JavaScript
license: MIT
maturity: v14.0.x, active, ~18k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-07-03T11:55:46Z
  default_branch: master
  default_branch_sha: 2d9bbea7df2ab1a48caecfafc39cb8599f193d3c
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:34:05Z
  overall: A
  overall_score: 3.5
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 12
        active_weeks_13: 8
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 47.7
        qualifying_issues: 7
        band: default
        window_offset_days: 3
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: markdown-it
        dependent_repos_count: 205037
        downloads_last_month: 105103424
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.03
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4295
        last_commit_age_days: 12
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 12
        top1_share: 0.869
        top3_share: 0.926
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# markdown-it


A fast, pluggable JavaScript markdown parser that follows CommonMark and GFM, tokenizing to an AST before rendering to HTML — the safer, stricter, more extensible alternative to marked.


![markdown-it — health radar](../../assets/health/markdown-it.svg)

## When to use

You're building a static site generator, a documentation system, or a content platform where authors write Markdown and you need reliable, spec-compliant HTML output. You want a parser that strictly follows CommonMark with GFM extensions, and you need the ability to plug in extras — emoji, math rendering, heading anchors, syntax-highlighted code blocks — without rebuilding the parser from scratch. You install `markdown-it`, configure a few plugins, and get clean, safe HTML that you can cache, transform, or inject into your templates. It's the right reach when *correctness and extensibility* matter: your docs site, your CMS, your server-side renderer, or any place where Markdown is user-facing content.

## When NOT to use

- **You need a full AST manipulation toolchain.** markdown-it is a parse-and-render pipeline, not a general document-transform engine. For linting, rewriting, MDX, or arbitrary AST passes, use remark / unified.
- **You want the absolute smallest bundle for simple Markdown→HTML.** marked is leaner and has a smaller API surface for one-call rendering; markdown-it's plugin architecture and token model add weight you may not need.
- **You need non-HTML output natively.** markdown-it renders to HTML; producing PDF, React elements, or other formats requires extra adapters or custom renderer rules. [未验证]
- **You're parsing untrusted Markdown without a sanitizer.** Like marked, markdown-it does not sanitize output HTML by default — raw HTML passes through unless you enable `html: false` or run the output through a sanitizer. [推断]
- **You want a streaming or memory-constrained parser.** For very large documents or streaming tokenization, micromark's streaming-oriented design may be more appropriate.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [marked](marked.md) | ✅ | Choose marked when you want a simpler, faster one-call renderer with a smaller footprint. | Simpler, faster one-call renderer with a smaller footprint; less spec-strict and a smaller plugin catalog. |
| [remark](remark.md) | ✅ | Choose remark when you need a full mdast AST pipeline for parsing, transforming, linting, and serializing Markdown or MDX. | Full mdast AST pipeline for parsing, transforming, linting, and serializing (Markdown, MDX); far more powerful and far heavier — a toolchain, not a one-call renderer. |
| [micromark](micromark.md) | ✅ | Choose micromark when you need the low-level CommonMark/GFM tokenizer underneath remark. | The low-level CommonMark/GFM tokenizer underneath remark; correct and streaming-oriented, but you build the rendering layer yourself. |
| [CommonMark](commonmark.md) | ✅ | Choose CommonMark when you need the spec's own reference implementation rather than a production renderer with plugins. | The spec's own reference implementation; the conformance yardstick, but fewer GFM niceties and not optimized as a production renderer. |
| [Pandoc](pandoc.md) | ✅ | Choose Pandoc when you need a universal document converter across dozens of formats, not just Markdown→HTML. | Haskell-based universal doc converter across dozens of formats; far heavier and not embeddable in a JS app. |
| Showdown | 未收录 | Choose Showdown only when maintaining legacy code that already depends on it. | Older JS markdown converter; less active, less spec-compliant, and generally superseded by markdown-it or marked. |
| [Goldmark](goldmark.md) | ✅ | Choose Goldmark when you're in the Go ecosystem, for example Hugo. | Go's markdown parser, used in Hugo; not available in JS. |

## Tech stack

- **Language:** JavaScript (ES2015+); ships with TypeScript type definitions.
- **Runtime targets:** Node.js and browser; distributed as ESM and UMD builds.
- **Architecture:** Token-based pipeline — a parser turns Markdown into a token stream/AST, then a renderer walks the tokens to emit HTML. Plugins hook into both phases.
- **Standards:** CommonMark spec-compliant core with GFM extensions (tables, strikethrough, task lists, autolinks) available via `@markdown-it/gfm` or built-in options depending on version. [推断]

## Dependencies

- **Runtime:** none required for the core parser — it is self-contained.
- **Plugins:** the ecosystem is npm-based (`markdown-it-emoji`, `markdown-it-anchor`, `markdown-it-math`, `markdown-it-container`, etc.) — each is a separate package you install and register with `.use()`.
- **Install:** `npm install markdown-it`; also available via CDN.

## Ops difficulty

**Low.** It's a library — add it to your dependency tree, require/import it, and call `.render()`. No service to deploy, no datastore to operate. The only operational note is plugin hygiene: each plugin you add is a new dependency to audit and update, and the security model (raw HTML passthrough) requires you to configure `html: false` or sanitize output if your Markdown is untrusted.

## Health & viability

- **Maintenance — active (last push 2026-07).** v14.0.x releases through mid-2026; regular commits and releases for a mature, scope-settled parser. [推断]
- **Governance & bus factor.** Community-maintained under the `markdown-it` org on GitHub — a small team rather than a single person, which de-risks the bus factor versus a one-author library [推断]. Not vendor-controlled; no commercial tier gating features.
- **Age & Lindy verdict — old and still active ⇒ strong Lindy.** Created ~2014 (~12 years old) and still shipping in 2026: a solid age × still-active signal. A parser that has been the default choice for VuePress, VitePress, and many static site generators for years is a safer long-term bet than a young alternative.
- **Adoption & ecosystem.** Widely adopted in the JS static-site ecosystem — VuePress, VitePress, and numerous documentation generators use it. The plugin ecosystem is extensive (emoji, math, anchors, diagrams, containers, etc.) and well-documented. [推断]
- **Risk flags — minimal.** MIT-licensed, no relicensing history, no open-core gating. The main caveat is the same as any Markdown parser: security is on you — raw HTML is not sanitized by default, so configure appropriately for untrusted input.

## Caveats (unverified)

- [未验证] ~18k GitHub stars and v14.0.x line as of 2026-07; star counts and versions drift release-to-release — treat as indicative.
- [推断] "Faster than marked in many benchmarks" reflects community benchmarks; your actual throughput depends on document size, plugin count, and runtime.
- [推断] "Used by VuePress, VitePress" is based on public documentation and dependency trees; confirm for your specific version.
- [未验证] No built-in non-HTML output: producing React elements, PDF, or other formats requires custom renderer rules or third-party adapters.
- [未验证] Plugin count and bundle size correlate — loading many plugins can noticeably increase parse time and bundle size.
