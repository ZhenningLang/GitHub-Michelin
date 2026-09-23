---
name: React Doctor
slug: react-doctor
repo: https://github.com/millionco/react-doctor
category: ai-code-review
tags: [react, static-analysis, agent-skill, oxlint, code-review, linter]
language: TypeScript
license: LicenseRef-Modified-MIT
maturity: oxlint-plugin-react-doctor@0.5.8, active (2026-06)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T11:33:33Z
  default_branch: main
  default_branch_sha: e2393c4a6b842efc72d5c225273c0de918a13450
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:56:44Z
  overall: B
  overall_score: 3.2
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
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.2
        qualifying_issues: 55
        band: relaxed_solo
        window_offset_days: 7
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: oxlint-plugin-react-doctor
        dependent_repos_count: 0
        downloads_last_month: 5826524
        graph_tier: E
        volume_tier: A
        cross_check_divergence: 1.04
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 221
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 17
        top1_share: 0.65
        top3_share: 0.935
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# React Doctor

A deterministic static analyzer for React that catches the bad code coding agents write — runnable as a one-shot `npx` audit, an installable agent skill, an oxlint/ESLint plugin, or in CI.

![react-doctor — health radar](../../assets/health/react-doctor.svg)

## When to use

You're a frontend engineer letting a coding agent (Claude Code, Cursor, Codex, OpenCode) churn out React components for a Next.js or Vite app. The diffs look plausible and tests pass, but the agent keeps reaching for `useEffect` where it shouldn't, uses array indices as keys, recreates objects every render, and quietly introduces accessibility and security regressions you only notice in review — or in production. You want a fast, repeatable gate that flags exactly these React-specific mistakes without you re-reading every line. You run `npx react-doctor@latest` and get a deterministic audit across state & effects, performance, architecture, security, and accessibility — the same input always yields the same findings, so it's reviewable and CI-friendly.

The bigger win is closing the loop with the agent itself. After the first audit you run `npx react-doctor@latest install` to drop it in as a skill for your agent, so future edits are checked against the same rule set and the agent learns to fix (and stop reintroducing) the issues it just made. Because it also ships oxlint and ESLint plugins, a language server, and VSCode/Zed extensions, the same rules can live in your editor and in a GitHub Actions PR scan — one consistent React rule set across agent, editor, and CI instead of relying on an LLM reviewer to re-judge the code each time.

## When NOT to use

- **You're not writing React.** It is React-specific by design (works across Next.js, Vite, TanStack, React Native, Expo) — but for Vue, Svelte, Angular, or backend code it does nothing. Use a general reviewer instead.
- **You want semantic, intent-level review of *any* language.** React Doctor runs a fixed catalog of React rules deterministically; it is not an LLM that reasons about business logic, naming, or architecture in prose. For LLM-driven, language-agnostic review see [open-code-review](open-code-review.md) or [claude-code-security-review](claude-code-security-review.md).
- **Security is your primary need.** It has a security category, but it is a broad React linter, not a dedicated vulnerability/taint-analysis reviewer. A security-focused tool will go deeper on auth, injection, and data-flow.
- **License-sensitive / vendored builds.** The license is a **Modified MIT** (not standard SPDX MIT): it adds restrictions — notably around using the software for AI training/fine-tuning and around commercial hosting — so do not treat it as a permissive MIT dependency without reading the actual terms. [推断] this can matter for redistribution or building a competing service.
- **You need rule stability / a frozen API.** It is pre-1.0 and moving fast (multiple packages, frequent releases); rules and config (`doctor.config.ts`) may shift between versions, so pin if a CI gate depends on exact findings.
- **You don't want a multi-package toolchain.** The repo is a Turbo monorepo (core, api, language-server, oxlint/ESLint plugins, editor extensions, CLI). If you only want a single library import, the surface area is larger than you need.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [open-code-review](open-code-review.md) | ✅ | Choose open-code-review when you need language-agnostic LLM judgment over PR logic; choose React Doctor when repeatable React-specific agent-error rules are the gate. | LLM-driven, language-agnostic PR review (Alibaba); reasons about logic in prose. React Doctor is deterministic, React-only, rule-based — repeatable but no semantic judgment. |
| [claude-code-security-review](claude-code-security-review.md) | ✅ | Choose claude-code-security-review when security vulnerability reasoning is the primary job; choose React Doctor for broad React lint, performance, accessibility, and correctness checks. | Claude-based security-focused review (Anthropic); deep, language-agnostic vuln reasoning. React Doctor is a broad React linter, not a dedicated security analyzer. |
| eslint-plugin-react-hooks / react | 未收录 | Choose the official React lint rules for canonical hooks coverage with the smallest conceptual surface; choose React Doctor when the agent-skill workflow and extra agent-error rules are the value. | The canonical React lint rules; React Doctor overlaps but adds an agent-skill workflow, an oxlint plugin, and curated agent-error rules beyond the official sets. |
| oxlint | 未收录 | Choose oxlint when the need is a fast Rust linter host; choose React Doctor when you need the React-specific rule pack that can run through oxlint. | The fast Rust linter React Doctor ships a plugin for; oxlint is the engine/host, React Doctor supplies the React-specific agent-facing rule pack. |
| Biome | 未收录 | Choose Biome for all-in-one JS/TS formatting and broad linting; choose React Doctor when the deciding need is catching agent-written React anti-patterns. | All-in-one Rust formatter+linter; broad JS/TS lint coverage but not focused on catching agent-written React anti-patterns specifically. |

## Tech stack

- **Language:** TypeScript (ESM, `"type": "module"`).
- **Monorepo:** Turbo-managed packages — `core`, `api`, `language-server`, `oxlint-plugin-react-doctor`, `eslint-plugin-react-doctor`, `react-doctor` (CLI), `vscode-react-doctor`, `zed-react-doctor`, `deslop-cli`, `deslop-js`, `website`.
- **Lint engines:** ships both an **oxlint** plugin and an **ESLint** plugin (the latest release is `oxlint-plugin-react-doctor@0.5.8`).
- **Editor/IDE:** a language server plus VSCode and Zed extensions.
- **Distribution:** CLI via `npx react-doctor@latest`; agent skill via `npx react-doctor@latest install`; CI via `npx react-doctor@latest ci install` (GitHub Actions PR scanning). Config in `doctor.config.ts`.
- **Build/dev tooling:** vite-plus, Changesets for releases, ts-json-schema-generator.

## Dependencies

- **Runtime:** Node.js + a package runner (`npx`/pnpm). No database or server to host — it is a local/CLI static analyzer.
- **Engine:** oxlint when using the oxlint plugin path; ESLint when using the ESLint plugin path. [推断] core analysis runs without a separate engine via the CLI, but plugin paths require their host linter.
- **Project:** an existing React/TypeScript codebase to scan (Next.js, Vite, TanStack, React Native, Expo all stated as supported).
- **Install:** zero persistent install for a one-shot audit (`npx react-doctor@latest`); the skill/CI installers add config and a skill file to your repo/agent.

## Ops difficulty

**Low.** For the common case it is a single `npx` command with nothing to deploy, host, or maintain — no server, no datastore, deterministic output that slots into CI. Difficulty rises only mildly: wiring it as a GitHub Actions gate, tuning `doctor.config.ts`, or adopting the oxlint/ESLint plugins into an existing lint setup means version-pinning and config reconciliation. The pre-1.0, multi-package nature means you should pin versions if a CI gate depends on exact findings.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 0.2 hours across 55 qualifying issues/PRs.
- **Maintenance (2026-06):** [推断] actively maintained — repo last pushed 2026-06-25, plugin `oxlint-plugin-react-doctor@0.5.8` released 2026-06-20, frequent multi-package releases via Changesets. Low open-issue count (~44) for ~13k stars. Momentum is healthy as of 2026-06.
- **Governance & backing:** [推断] under the `millionco` org (the team behind Million.js, a known React-performance project), so there's an established React-tooling org and brand behind it rather than a lone hobbyist — lower bus-factor than a single-maintainer repo. Still single-vendor, not foundation-governed.
- **Age & Lindy:** [推断] created 2026-02, ~4 months old as of 2026-06 — **very young; no Lindy track record.** It's pre-1.0 and moving fast across a multi-package monorepo, so the rule catalog and `doctor.config.ts` can shift between versions; pin if a CI gate depends on exact findings.
- **Risk flags:** [推断] **license is the standout flag** — `LicenseRef-Modified-MIT` (gh reports "Other"), adding non-standard restrictions around AI training/fine-tuning and commercial hosting. Do **not** treat it as permissive MIT for redistribution or building a competing service; read the actual LICENSE. No CVEs observed.

## Caveats (unverified)

- [未验证] Star count ~13.1k as of 2026-06 (GitHub stars are unreliable and date-sensitive; indicative only).
- [未验证] Latest release `oxlint-plugin-react-doctor@0.5.8` published 2026-06-20; repo last pushed 2026-06-25. Individual package versions (CLI, core) may differ from the plugin's tag.
- [未验证] The full rule catalog is not enumerated here; the README names categories (state & effects, performance, architecture, security, accessibility) and one example rule (`react-doctor/no-array-index-as-key`) — verify the exact rule set against the current repo.
- [推断] The "Modified MIT" license adds non-standard restrictions (AI-training/fine-tuning, commercial hosting); `gh` reports the license as "Other". Treat licensing implications as requiring a read of the actual LICENSE, not an assumed MIT.
- [推断] Agent-skill "learning" means the agent reads the installed rule/skill file and applies fixes; it is not model weight training. Behavior across different agents is not guaranteed.
- [未验证] Framework support claims (Next.js/Vite/TanStack/React Native/Expo) are from the project's own description, not independently benchmarked.
