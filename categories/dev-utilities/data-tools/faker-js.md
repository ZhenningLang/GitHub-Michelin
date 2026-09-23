---
name: Faker (faker-js)
slug: faker-js
repo: https://github.com/faker-js/faker
category: data-tools
tags: [test-data, mock-data, fixtures, seeding, fake-data, javascript, typescript, locales]
language: TypeScript
license: MIT
maturity: v10.x, active, ~15.4k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-29T02:35:20Z
  default_branch: next
  default_branch_sha: acd5fdaf099bda7cf90c76bf0ae0a33349a54ce7
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:09:14Z
  overall: A
  overall_score: 3.6
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
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 1.6
        qualifying_issues: 12
        band: default
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@faker-js/faker"
        dependent_repos_count: 17617
        downloads_last_month: 64398665
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.0
        release_downloads: 716
        release_assets: 51
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1719
        last_commit_age_days: 0
        cohort: library
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 16
        top1_share: 0.401
        top3_share: 0.631
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Faker (faker-js)

A JavaScript/TypeScript library that generates massive amounts of realistic fake data — names, addresses, finance, commerce, dates, lorem, and more — for tests, seed scripts, and prototypes, in both the browser and Node.js.

![faker-js — health radar](../../../assets/health/faker-js.svg)

## When to use

You're a full-stack developer wiring up a new feature and your tests and local environment are starving for data. The unit tests need a believable `User` — a name, email, avatar URL, a street address that *looks* like a street address — and hand-writing `"John Doe", "123 Main St"` for the tenth time is both tedious and makes every fixture suspiciously identical. Your staging database is empty, so the UI looks broken until someone manually types in rows. You reach for Faker: `faker.person.fullName()`, `faker.internet.email()`, `faker.location.streetAddress()`, `faker.commerce.productName()` — one import, dozens of namespaced generators, and your factory functions now emit varied, realistic-looking records every run. Call `faker.seed(123)` and the same "random" data comes back deterministically, so a failing test reproduces instead of flapping.

You also reach for it to fill a seed script that pumps a few thousand fake orders, customers, and products into a dev database so the dashboard finally has something to render, or to drive Storybook/demo screens with plausible content instead of "Lorem ipsum" everywhere. It runs the same in Node and the browser, ships first-class TypeScript types, and carries 70+ locales so a German or Japanese build gets region-appropriate names and addresses rather than always-American defaults.

## When NOT to use

- **Fake data is not production-representative data.** Faker's output is plausible-looking but statistically uniform-ish noise — it does **not** reflect your real distributions (value skews, null rates, correlations, edge-case clustering). Don't use it to benchmark query performance, validate analytics, or "prove" a model on data that won't match production. [推断]
- **You need schema-aware / relational data modeling.** Faker generates *fields*, not a coherent data graph — it won't keep foreign keys consistent, enforce constraints, or honor your schema. For relational fixtures you still need a factory layer (Fishery, factory_boy-style) or a schema-driven generator on top.
- **Locale coverage is uneven.** "70+ locales" doesn't mean every namespace is complete in every locale; some locales fall back to English or have sparse datasets. Verify the specific locale × module you depend on instead of assuming parity. [未验证]
- **Frontend bundle size matters.** Pulling Faker into shipped client code can add significant weight; it's meant for dev/test, and you generally want it in `devDependencies` and tree-shaken or excluded from production bundles.
- **You need a different language runtime.** This is the JS/TS library; for Python use Python's `Faker`, for Ruby the `faker` gem, etc. — don't shim Node into a non-JS test suite just for fake data.
- **You need guaranteed-unique or exhaustive values at scale.** Random generation collides; for large unique datasets you must layer your own uniqueness/dedup (Faker exposes helpers but does not guarantee global uniqueness across calls). [未验证]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| Python `Faker` | 未收录 | Choose Python Faker when your tests or seeders are Python rather than JavaScript. | The same idea for Python (the JS Faker lineage descends from it); use it when your tests/seeders are Python, not JS. |
| Chance.js | 未收录 | Choose Chance.js when you need a smaller, older random-generator utility with a narrower catalog. | Smaller, older random-generator utility; lighter and dependency-free but a much narrower data catalog and no rich locale system. |
| @ngneat/falso | 未收录 | Choose @ngneat/falso when you need a modern tree-shakeable TypeScript fake-data library. | Modern tree-shakeable TS fake-data library positioned as a lighter, individually-importable alternative; smaller locale/namespace surface than Faker. |
| Mockaroo | 未收录 | Choose Mockaroo when you need hosted, schema-first mock-data export rather than an in-process test library. | Hosted SaaS / schema-first mock-data generator (CSV/JSON/SQL export) — not an in-process library; good for one-off bulk datasets, but it's a service, not a repo you embed in tests. |

## Tech stack

- **Language:** TypeScript (compiled to ESM + CJS), shipping first-class type definitions.
- **Runtime targets:** browser and Node.js from the same package; framework-agnostic.
- **Structure:** namespaced modules (`person`, `location`, `internet`, `finance`, `commerce`, `date`, `lorem`, `image`, …) over a seedable PRNG, plus locale data bundles (70+ locales) imported per-locale.
- **Distribution:** published to npm; per-locale entry points (`@faker-js/faker/locale/*`) so you can import only the locale you need.

## Dependencies

- **Runtime:** a JS runtime (Node.js or a browser) — that's it; Faker is a self-contained library with no external services or datastore.
- **Install:** `npm i -D @faker-js/faker` (typically a dev dependency).
- **Build (from source):** Node.js + the repo's package-manager toolchain (pnpm) to build/test from the repository; exact versions are pinned in the repo at build time.
- **No infrastructure:** no database, server, or network access required to generate data.

## Ops difficulty

**Low.** It's a library, not a service — there's nothing to deploy or operate. Integration cost is `npm install` plus calling generators in your factories/seeders. The few real concerns are hygiene rather than ops: keep it in `devDependencies` so it doesn't bloat production bundles, pin the major version because Faker has reorganized its API across majors (the v5→v6 community-fork transition and later majors renamed/moved methods), and call `faker.seed()` where you need deterministic, reproducible fixtures. Upgrades across major versions can require codemods/renames, so read the migration notes before bumping.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 1.6 hours across 12 qualifying issues/PRs.
- **Maintenance (2026-06).** Last pushed 2026-06 (active); shipping on the v10 line with a steady release cadence and frequent commits — **active**, not coasting. Not archived. [推断]
- **Governance / bus factor.** This is a community **organization** project, not a single-maintainer package — and notably so *by origin*: faker-js was formed in January 2022 after the original `faker.js` was deliberately sabotaged and removed from npm by its sole author. The community fork exists specifically to remove that single-owner rug-pull risk, so the governance structure is a **positive** here — but the lineage is worth knowing when you read older tutorials referencing the dead `faker` package. [推断]
- **Age & Lindy verdict.** ~4 years old **as this org/fork** (created 2022-01) and still actively shipping ⇒ a **moderate-and-improving** Lindy signal: younger than its commit history implies (the underlying idea and data descend from the 2011-era original), but the *governed* incarnation is the one you depend on, and it has now sustained ~4 years of active multi-contributor maintenance. [推断]
- **Adoption & ecosystem.** Very widely used across the JS/TS testing ecosystem (~15.4k stars, heavy npm usage), good docs, 70+ locales, first-class TS types — strong, healthy adoption. [未验证]
- **Risk flags.** Permissive MIT license (the LICENSE file bundles upstream copyright notices, which is why GitHub's auto-detector reports `NOASSERTION`/"Other" rather than "MIT"). The main practical risk is API churn across major versions, not stewardship. [推断]

## Caveats (unverified)

- [未验证] ~15.4k GitHub stars as of 2026-06 and latest release on the v10 line (v10.5.0 reported 2026-06) — star counts and exact version numbers are date-sensitive; treat as indicative and re-verify against the current repo.
- [未验证] GitHub reports the license as `NOASSERTION`/"Other"; the repository's LICENSE file is MIT (it additionally reproduces the original faker.js and upstream Ruby/Perl copyright notices, which defeats GitHub's single-license auto-detection) — confirmed by reading the LICENSE file, recorded here as the reason for the discrepancy.
- [未验证] "70+ locales" is the project's own framing; per-locale completeness varies and some locales fall back to English — verify the specific locale × module you depend on.
- [推断] Faker generates field-level values with no cross-field/relational consistency and no guaranteed global uniqueness; "not production-representative" and "not schema-aware" are inferences about how realistic-but-random data behaves, not measured claims.
- [推断] Frontend bundle-size impact and the dev-dependency recommendation are general guidance; the actual cost depends on your bundler, tree-shaking, and which locales/modules you import.
- [推断] Major-version API churn (renamed/moved methods, the v5→v6 fork transition) is inferred from the project's known reorganizations; check the migration guide for the exact versions you're moving between.
