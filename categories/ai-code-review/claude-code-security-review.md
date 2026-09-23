---
name: Claude Code Security Review
slug: claude-code-security-review
repo: https://github.com/anthropics/claude-code-security-review
category: ai-code-review
tags: [security, sast, github-action, claude, pr-review, slash-command]
language: Python
license: MIT
maturity: no tagged release, pinned via @main, active (2026-02)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-02-11T18:01:23Z
  default_branch: main
  default_branch_sha: 0c6a49f1fa56a1d472575da86a94dbc1edb78eda
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:41:34Z
  overall: B
  overall_score: 2.5
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 223
        active_weeks_13: 0
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
        repo_age_days: 414
        last_commit_age_days: 223
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.75
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
    adoption: { reason: ambiguous }
---

# Claude Code Security Review

Anthropic's AI security reviewer: a GitHub Action (plus a `/security-review` Claude Code slash command) that reads a PR diff with Claude and posts line-level vulnerability findings.

![claude-code-security-review — health radar](../../assets/health/claude-code-security-review.svg)

## When to use

You're a maintainer of a small-to-mid repo and you want a security gate on pull requests that goes beyond regex/AST pattern matching. Traditional SAST flags the same shapes over and over and misses logic-level bugs — an IDOR that only matters because of how two handlers share a session, an injection that's only reachable through a specific code path. You add this Action to `.github/workflows/`, give it a Claude API key, and on every PR it analyzes only the changed files, reasons about the diff in context, and leaves review comments on the exact lines it thinks are vulnerable, with severity and remediation. Because it's "language agnostic" (it's Claude reading code, not a per-language ruleset), the same workflow covers your Python service, your TypeScript frontend, and your Terraform without separate tooling.

You're also a developer using Claude Code day-to-day who wants the same check before you even open a PR. You run `/security-review` on your pending changes and get the audit locally; you can copy `security-review.md` into your repo's `.claude/commands/` and tune the prompt for your project. The tool's whole pitch is the inverse of noisy scanners: an opinionated false-positive filter that drops DoS/rate-limit/open-redirect-style findings so the comments that land are the ones worth acting on.

## When NOT to use

- **You need to review untrusted / fork PRs.** The README states it is **not hardened against prompt injection** and should only review **trusted PRs**; a malicious diff can attempt to manipulate the reviewer. For public repos you must gate it behind maintainer approval of external contributors — a hard operational constraint, not a nice-to-have.
- **You want a free or local-only scanner.** Every run calls the Claude API and bills tokens (default model `claude-opus-4-1-20250805`, with a 20-min timeout per run). High-PR-volume repos or `run-every-commit: true` can get expensive — a deterministic OSS SAST (Semgrep, CodeQL) has no per-run API cost.
- **You need deterministic, reproducible, compliance-grade results.** An LLM reviewer is non-deterministic: the same diff can surface different findings across runs. If you need a stable rule ID set, suppression baselines, and audit reproducibility, rule-based SAST is a better fit.
- **You need whole-codebase or scheduled deep scans.** It is diff-aware by design (PR changed files); it is not a crawler for finding latent vulns across an entire existing codebase the way a full SAST sweep is.
- **You want SARIF / third-party security-tab integration out of the box.** Output is PR comments plus a results JSON artifact; [未验证] there is no documented native SARIF export, so wiring it into GitHub's code-scanning UI is not turnkey.
- **No tagged releases.** Usage pins `@main`; there is no semver release line, so you trade stability for following an unpinned moving branch (or pin a commit SHA yourself).

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [open-code-review](open-code-review.md) | ✅ | Choose open-code-review for general LLM PR review on GitLab or coding-quality feedback; choose this tool when the gate must be Claude/GitHub-Actions-native and security-specific. | Alibaba LLM-based code reviewer for GitLab/coding-style + quality; this one is security-specific and Claude/GitHub-Actions-native. |
| [react-doctor](react-doctor.md) | ✅ | Choose react-doctor for deterministic React performance, correctness, accessibility, and agent-error diagnostics; choose this tool when the review target is vulnerability reasoning across a PR diff. | React-specific perf/correctness diagnostics, not a security reviewer; different problem entirely. |
| Semgrep | 未收录 | Choose Semgrep when reproducible rule IDs, SARIF, local/free runs, and community rules matter more than LLM context; choose this tool when logic-level security reasoning over a trusted PR diff is the gap. | Deterministic, rule-based SAST with SARIF and a huge community ruleset; fast, free, reproducible — but pattern-bound, weaker on logic/contextual bugs. |
| GitHub CodeQL | 未收录 | Choose CodeQL when native GitHub code scanning and deep dataflow/taint analysis are required; choose this tool when you want Claude-written line comments and remediation prose on changed files. | Deep dataflow/taint analysis, native code-scanning UI, free for public repos; per-language, heavier setup, no LLM remediation prose. |
| Claude Code GitHub Action (general) | 未收录 | Choose the general Claude Code Action for broad PR assistance or coding tasks; choose this tool when you specifically need the security-audit prompt and finding filter. | Anthropic's general-purpose Claude Action for PRs/coding; not specialized for security audit or finding-filtering. |
| Snyk Code | 未收录 | Choose Snyk Code when a managed commercial security dashboard and dependency scanning are part of the requirement; choose this tool for a repo-local OSS Action driven by Claude review comments. | Commercial ML/SAST with a managed dashboard and dependency scanning; hosted SaaS, not a single-repo OSS Action. |

## Tech stack

- **Language:** Python (≈89.6% of repo per GitHub; with some TypeScript/JavaScript for tooling). [未验证] percentages are language-bar snapshots and drift.
- **Runtime model:** Claude (Claude Code) — default `claude-opus-4-1-20250805`, configurable via the `claude-model` input.
- **Delivery:** a composite GitHub Action (`anthropics/claude-code-security-review@main`) plus a `/security-review` Claude Code slash command.
- **Core modules:** `github_action_audit.py` (main audit), `prompts.py` (audit prompt templates), `findings_filter.py` (false-positive filtering), `claude_api_client.py` (API client), `json_parser.py` (robust JSON parsing), `evals/` (eval tooling).
- **Testing:** `pytest claudecode -v`.

## Dependencies

- **Required:** an Anthropic Claude API key (must be enabled for both Claude API and Claude Code) supplied as `claude-api-key` / a GitHub secret.
- **Platform:** GitHub repository with Actions enabled (primary path); can also run locally via the evals framework.
- **Permissions:** workflow needs `pull-requests: write` (to comment) and `contents: read`.
- **Python deps:** `claudecode/requirements.txt` is lightweight — `PyGithub>=1.59.0`, `requests>=2.28.0`, `anthropic>=0.39.0` (parsing uses stdlib). No heavy ML stack, because inference is remote.
- **Claude CLI:** the `claude` command-line tool must be installed separately (the Action handles this); analysis is driven through it, not only the raw API.

## Ops difficulty

**Low.** The happy path is a ~15-line workflow file and one secret — no servers, no datastore, no model to host (inference is the remote Claude API). Ongoing maintenance is mostly two things: cost control (token spend scales with PR volume and `run-every-commit`; mind the 20-min `claudecode-timeout`) and the prompt-injection constraint (you must configure fork/external-contributor approval gating). Tuning the false-positive filter or custom scan instructions is optional file-based config. The main residual risk is operational, not infra: pinning `@main` means upstream changes can alter behavior without a version bump.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-06):** [推断] **coasting, not abandoned.** Last push 2026-02 — roughly four months stale as of 2026-06 — and there has never been a tagged release (usage pins `@main`). For a security gate that means: no version line to anchor on, and behavior can change (or silently stop tracking the current Claude model default) without a signal. Not dead, but slower-moving than its peers here.
- **Governance & backing:** [推断] owned by `anthropics` (the Anthropic org), a vendor with a direct interest in the Claude-Code ecosystem this drives. That cuts bus-factor risk versus a single maintainer, but it's a vendor showcase/companion tool, not a foundation-governed project — Anthropic can re-scope or quietly de-prioritize it.
- **Age & Lindy:** [推断] created 2025-08, ~10 months old as of 2026-06 — **young-to-middling, weak Lindy prior.** The 4-month-stale push on top of a sub-1-year age means it has neither longevity nor strong recent momentum; treat it as a useful-but-unproven tool, not a long-term bet.
- **Risk flags:** [推断] hard constraint, not a flag you can defer: README states it is **not hardened against prompt injection** and must only review trusted PRs — a structural limitation of an LLM reviewer, not a bug that gets patched. Plus per-run Claude API cost and non-determinism (see When NOT to use). MIT license, no relicense history found.

## Caveats (unverified)

- [未验证] `gh` reports `latestRelease: null` and ~5.37k stars as of 2026-02 (last push 2026-02-11); GitHub stars are unreliable and date-sensitive — treat as indicative only.
- [未验证] No documented native SARIF / GitHub code-scanning export; integrating findings into the security tab may require custom glue.
- [未验证] Repo language breakdown (≈89.6% Python / 7.2% TS / 3.2% JS) is a GitHub snapshot and shifts over time.
- [推断] Default model `claude-opus-4-1-20250805` is the README default at time of writing and may be bumped upstream; verify the current default before relying on a specific model/cost profile.
- [推断] Per-run cost and latency depend on diff size, chosen model, and `run-every-commit`; no first-party cost figure is published here.
- [未验证] `claudecode/requirements.txt` (verified 2026-06-26) pins only `PyGithub>=1.59.0`, `requests>=2.28.0`, `anthropic>=0.39.0`; a note states the `claude` CLI must be installed separately — upstream may add deps later.
