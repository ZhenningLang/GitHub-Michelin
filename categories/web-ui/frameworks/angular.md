---
name: Angular
slug: angular
repo: https://github.com/angular/angular
category: frameworks
tags: [web-framework, typescript, spa, pwa, enterprise, frontend]
language: TypeScript
license: MIT
maturity: v19.x, stable, 100.4k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T21:10:34Z
  default_branch: main
  default_branch_sha: b126dc9726789ad5ca3b26e497725e6a05031ed3
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:16:33Z
  overall: A
  overall_score: 4.0
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
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.0
        qualifying_issues: 28
        band: default
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@angular/core"
        dependent_repos_count: 768558
        downloads_last_month: 20872075
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.05
        release_downloads: 324
        release_assets: 6
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4387
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 89
        top1_share: 0.162
        top3_share: 0.36
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

# Angular

A comprehensive web development platform for building mobile and desktop web applications using TypeScript. Built and maintained by Google with a strong focus on enterprise-scale apps.

![Angular — health radar](../../../assets/health/angular.svg)

## When to use

You're an enterprise team building a large, complex web application with dozens of screens, strict coding standards, and a need for long-term maintainability. You evaluate React, but its "bring your own everything" philosophy means you would spend weeks choosing and wiring together routing, state management, and form validation libraries. You evaluate Vue, but its gentler learning curve comes with less built-in structure for large teams. You choose Angular because it ships with everything you need: a powerful CLI for scaffolding, a reactive forms system, an HTTP client, a router with lazy loading, and a first-class TypeScript experience. You don't want to spend weeks evaluating and wiring together third-party libraries for routing, state management, or form validation. Angular's opinionated structure means new hires can onboard faster because the codebase follows predictable patterns, and Google's long-term backing gives you confidence the framework will still be maintained in five years.

## When NOT to use

- **If you need a small landing page, blog, or simple CRUD with fewer than 10 screens, use Vite + React or Vue instead of Angular, because** Angular's boilerplate and build complexity are overkill for small projects. You will ship faster with a lighter stack.
- **If your team avoids TypeScript, use plain React or Vue instead of Angular, because** Angular is deeply TypeScript-native. If your team prefers plain JavaScript or finds TS decorators and complex types burdensome, friction will be constant.
- **If you need rapid prototyping or a quick MVP, use Next.js or Vue instead of Angular, because** Angular's strict module system, build pipeline, and boilerplate slow down quick iterations. A lighter framework is better for hackathons and prototypes.
- **If you need SEO-first static sites, use Next.js or Nuxt instead of Angular, because** while Angular has SSR (Angular Universal), it is not as seamless as Next.js or Nuxt for static site generation. If your content is mostly static and SEO-critical, those frameworks are the better choice.
- **If you need mixed-framework micro-frontends, use React-based micro-frontends with module federation instead of Angular, because** Angular's zone.js and Ivy compiler create integration friction when mixing with non-Angular micro-frontends. If your architecture requires mixed-framework shells, the complexity is real.
- **If bundle size is critical for low-bandwidth or mobile-first markets, use Svelte or Preact instead of Angular, because** Angular's core framework is larger than React or Vue. For apps targeting low-bandwidth or mobile-first emerging markets, the initial payload can be a concern.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [React](react.md) | ✅ | Choose React when you want the largest UI ecosystem and a "just JavaScript" philosophy. | React is more flexible and has a larger job market; Angular is more opinionated and ships with more built-in tooling, reducing decision fatigue. |
| [Vue.js](vue.md) | ✅ | Choose Vue when you need a progressive framework with a gentler learning curve and excellent documentation. | Vue is easier to adopt incrementally; Angular demands all-in commitment but rewards it with stronger enterprise structure. |
| [Svelte](svelte.md) | ✅ | Choose Svelte when you want compile-time components with minimal runtime overhead and no virtual DOM. | Svelte is faster and simpler for small-to-medium apps; Angular has deeper enterprise support, more third-party integrations, and a longer track record. |
| [SvelteKit](sveltekit.md) | ✅ | Choose SvelteKit when you want Svelte's full-stack meta-framework rather than a standalone component framework. | SvelteKit adds routing, SSR, and app conventions around Svelte; Angular remains more enterprise-opinionated and longer-established. |
| [Next.js](nextjs.md) | ✅ | Choose Next.js when you need React-based SSR/SSG with a dominant full-stack ecosystem. | Next.js is the default for React-based SSR/SEO; Angular Universal exists but is less dominant in that niche. |
| [shadcn/ui](../component-libraries/shadcn-ui.md) | ✅ | A component distribution model, not a framework — often used inside React. | Not a direct substitute; shadcn/ui is about component ownership, Angular is a full application framework. |
| [Lit](lit.md) | ✅ | Lightweight library for building standards-based web components with a tiny runtime. | Lit is for building interoperable components, not full SPAs; Angular is a complete framework with routing, DI, and CLI. Choose Lit for design systems that must work across frameworks. |

## Tech stack

- **TypeScript** — primary language; Angular is one of the earliest frameworks to go all-in on TS
- **RxJS** — reactive programming library for async operations and state management
- **Zone.js** — change detection mechanism (being phased out in favor of signals)
- **Angular CLI** — build, test, and scaffolding toolchain based on Webpack / esbuild
- **Angular Universal** — server-side rendering (SSR) and static site generation (SSG)
- **Angular Material** — official Material Design component library
- **Ivy** — next-generation compilation and rendering pipeline
- **Signals** — modern fine-grained reactivity system (introduced in v16+, replacing zone.js gradually)

## Dependencies

- **Node.js** — runtime for the CLI and build tools (LTS recommended)
- **TypeScript** — the framework is designed around TS; plain JS is not practical
- **A modern browser** — Angular supports evergreen browsers; IE11 support has been dropped
- **Optional: Angular Universal** — for SSR, a Node.js server is required
- **Optional: Angular Material** — if you want pre-built Material Design components (not required)
- **Optional: NgRx / Akita / NGXS** — for complex state management beyond RxJS services
- **Build tools**: The CLI abstracts Webpack / esbuild / Vite, but you may need to customize builders for advanced use cases

## Ops difficulty

**Low to Medium**. Angular apps are static SPAs (or SSR apps) that deploy to any CDN or web server. The CLI handles the build pipeline, tree-shaking, and optimization. Complexity arises when:
- You need custom Webpack configs (e.g., for micro-frontends or legacy module federation)
- You enable SSR and must run a Node.js server
- You manage monorepos with multiple Angular apps (Nx is the common solution)
- You upgrade major versions (Angular's 6-month release cycle means annual upgrades are needed)

## Health & viability
- **Maintenance**: Grade A — 13/13 active weeks in trailing 13; last commit 1 days ago.
- **Responsiveness**: Grade A — median first-response time 0.0 hours across 18 qualifying issues/PRs.
- **Adoption**: Grade A — 24,664,067 monthly downloads via npmjs.org (package: @angular/core).
- **Longevity**: Grade A — 4,306 days old.
- **Governance**: Grade A — top-3 contributor share 36.8% (?).
- **Risk / License**: Grade A — MIT license.
## Caveats (unverified)

- [推断] Angular's zone.js to signals migration timeline and the exact proportion of Google-internal apps using Angular have not been verified.
- [未验证] The precise number of enterprise production deployments and their scale has not been independently audited.
- [未验证] Angular's market share relative to React and Vue in new project starts is inferred from job postings and community surveys, not hard data.
- [推断] Micro-frontend integration with non-Angular shells is possible but the exact friction level depends on the module-federation setup.
- [推断] The actual performance impact of Angular's bundle size compared to React or Vue varies by application and optimization strategy.
