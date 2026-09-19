---
name: Vercel Agent Skills
slug: vercel-agent-skills
repo: https://github.com/vercel-labs/agent-skills
category: engineering
tags: [agent-skills, react, nextjs, vercel, web-performance, code-review, skills-sh]
language: JavaScript
license: MIT
maturity: no tagged releases, active (pushed 2026-06), ~28.3k stars (as of 2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-10T21:21:47Z
  default_branch: main
  default_branch_sha: f8a72b9603728bb92a217a879b7e62e43ad76c81
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T10:44:50Z
  overall: B
  overall_score: 2.5
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 23
        active_weeks_13: 7
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 207
        last_commit_age_days: 23
        cohort: skill-pack
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 23
        top1_share: 0.251
        top3_share: 0.575
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: E
      raw:
        spdx_id: NONE
        permissiveness: source_available
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
    adoption: { reason: no_package_structural }
---

# Vercel Agent Skills

Vercel's official collection of agent skills — install-on-demand audit/build guides for React, Next.js, Vercel deploys, web design, and docs — packaged in the [agentskills.io](https://agentskills.io/) / [skills.sh](https://skills.sh/) format.

![vercel-agent-skills — health radar](../../../assets/health/vercel-agent-skills.svg)

## When to use

You're a frontend or full-stack engineer shipping a Next.js app on Vercel, working through a coding agent (Claude Code, Claude Desktop, or another harness that speaks the Agent Skills format). Your agent writes React that technically works but quietly regresses Core Web Vitals — request waterfalls, oversized bundles, needless re-renders — and you don't have Vercel's internal performance handbook memorized to catch it in review. Or your function bill crept up and you can't tell which routes are the cost drivers. You want the agent to apply Vercel Engineering's actual house rules instead of generic advice.

You run `npx skills add vercel-labs/agent-skills` and the agent gains a menu of on-demand skills it loads when the task matches: `react-best-practices` (40+ perf rules across 8 categories — waterfalls, bundle size, server-side perf), `composition-patterns` (avoid boolean-prop proliferation), `react-view-transitions`, `react-native-skills`, `web-design-guidelines` (100+ accessibility/UX rules), `writing-guidelines` (Vercel's writing handbook for docs review), `vercel-optimize` (pulls real Vercel metrics first, then audits only the routes those metrics flag for cost/caching/ISR/function issues), plus deploy helpers (`deploy-to-vercel`, `vercel-cli-with-tokens`). You reach for it when your stack *is* React + Vercel and you want the vendor's own opinionated guidance applied automatically rather than authoring those rule sets yourself.

## When NOT to use

- **You're not on React/Next.js/Vercel.** The bulk of the value is React perf rules, Next.js patterns, and Vercel-specific deploy/cost audits. On a Vue/Svelte/Astro or non-Vercel-hosted stack, most skills don't apply and the deploy/optimize skills assume the Vercel platform outright.
- **You already run a curated web-quality skill stack.** If you've installed another web-perf or accessibility skill pack, layering Vercel's on top risks conflicting rule sets and double-routing during review — pick one source of truth per concern.
- **Your harness doesn't speak the Agent Skills format.** These activate via the agentskills.io / skills.sh loading mechanism; on a harness with no such loader, the markdown won't auto-fire and you'd be copy-pasting prompts by hand.
- **You want enforcement, not advice.** Rules live in prompt/markdown the agent *should* follow; nothing blocks a merge or fails CI. It's advisory review guidance, not a gate.
- **You need version stability.** No tagged releases as of this check — you track a moving `main`, so rule sets and skill boundaries can shift between pulls. [推断]
- **You want a runnable library/CLI.** There's nothing to `import`; the helper scripts run *inside* a skill the agent invokes, not as a standalone tool you call yourself.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Agent Skills (addyosmani)](addyosmani-agent-skills.md) | ✅ | Pick Addy Osmani's pack when you trust its broader personal engineering rules more than Vercel-specific rules. | Addy Osmani's personal engineering skill set; overlapping web-perf/quality focus but maintained by an individual and not Vercel-platform-coupled. Compare on which rule sources you trust and whether you're on Vercel. |
| [web-quality-skills](addyosmani-web-quality.md) | ✅ | Pick web-quality-skills for vendor-neutral performance, accessibility, and quality auditing. | Dedicated web-quality/perf/accessibility skills; narrower than Vercel's broader bundle (deploy + optimize + React patterns) but vendor-neutral, so it travels off Vercel. |
| [Waza](waza.md) | ✅ | Pick Waza when general engineering habits matter more than React/Vercel platform rules. | Another engineering skill pack in this leaf; compare on domain coverage and which workflows each actually encodes. |
| [Scientific Agent Skills](scientific-agent-skills.md) | ✅ | Pick Scientific Agent Skills for research/data workflows outside web/frontend engineering. | Scientific/eng-workflow skills — different domain (research/data) than web/frontend engineering; complementary, not a substitute. |
| [Superpowers](../../agent-dev-methodology/coding-agent-harnesses/superpowers.md) | ✅ | Pick methodology packs when you need planning/TDD discipline rather than React/Vercel domain rules. | General SDLC/methodology skill packs shape *how* the agent works (TDD, planning); Vercel's pack supplies *domain* rules for React/Vercel. Often run together, not either/or. |

## Health & viability

- **Responsiveness**: Cannot be scored — type_na.
- **Maintenance (2026-06):** active — last push 2026-06, not archived, but no tagged releases, so you track a moving `main` and rule sets can shift between pulls.
- **Governance & backing:** `Organization`-owned under `vercel-labs` — vendor-backed by Vercel, which is a longevity plus (real company, real eng team owns the roadmap), but it's a single-vendor `labs` repo, so it can be deprioritized or archived at the vendor's discretion. [推断]
- **Age & Lindy:** created 2025-12, so only months old as of 2026-06 — young; unproven on Lindy despite ~28k stars. Vendor backing is the stronger durability signal here, not age.
- **Risk flags:** advisory-only (prompt/markdown, nothing fails the build); Vercel-platform coupling in the deploy/optimize skills means value drops sharply off React + Vercel; license rests on a README declaration only (no LICENSE file / empty license API on 2026-06-26). [未验证]

## Caveats (unverified)

- [未验证] License is MIT per the repo README's `## License` section; the GitHub license API and a top-level `LICENSE` file both returned empty on 2026-06-26, so the SPDX id rests on the README declaration alone — confirm before relying on it.
- [未验证] Primary language reported as JavaScript by GitHub metadata (2026-06-26); the substance is markdown skill definitions plus helper scripts, so the language tag reflects tooling/scripts, not a runnable JS app.
- [未验证] No tagged releases / `latestRelease` is null as of 2026-06-26; "maturity" is inferred from last push (2026-06-10) and activity, not a semver.
- [未验证] Star count (~28.3k per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, not a quality signal.
- [未验证] The skill inventory (vercel-optimize, react-best-practices, composition-patterns, react-view-transitions, react-native-skills, web-design-guidelines, writing-guidelines, deploy-to-vercel, vercel-cli-with-tokens) and rule counts (40+/100+/80+/16) are from the README and `skills/` listing on 2026-06-26; verify the live directory rather than trusting this snapshot, since it tracks an untagged `main`.
- [推断] Activation fidelity depends on each harness's Agent Skills loader; README names claude.ai/Claude Desktop explicitly, but behavior on other harnesses is not independently confirmed here.
- [推断] Because rules are prompt/markdown the agent loads, enforcement is advisory — the agent can deviate and nothing fails the build.
