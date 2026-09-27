---
name: claude-code-harness
slug: claude-code-harness
repo: https://github.com/Chachamaru127/claude-code-harness
category: engineering-workflows
tags: [claude-code, harness-config, sdlc-workflow, slash-commands, plan-work-review, plugin]
language: Shell
license: MIT
maturity: v5.15.0, active (2026-09)
last_verified: 2026-09-27
type: skill-pack
upstream:
  pushed_at: 2026-09-21T01:27:29Z
  default_branch: main
  default_branch_sha: 2b2b74805321089bd9b660a1064fa97556299703
  archived: false
health:
  schema: 1
  computed_at: 2026-09-27T13:46:06Z
  overall: B
  overall_score: 2.6
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
        last_commit_age_days: 21
        active_weeks_13: 11
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 475
        release_assets: 180
        release_tier: D
        signal_basis: releases
    longevity:
      grade: B
      raw:
        repo_age_days: 289
        last_commit_age_days: 21
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 5
        top1_share: 0.923
        top3_share: 0.998
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
    responsiveness: { reason: type_na }
---

# claude-code-harness

Your agent edits files, shells out, and declares "done" — nothing checks any of it beforehand, and the review is whatever the same model feels like writing. claude-code-harness (CCH) bolts a governed plan → work → review → release loop onto Claude Code, Codex CLI, Cursor, and Grok: you approve a generated `spec.md`/`Plans.md` contract before code is written, an independent review gates completion, and a Go binary inspects each tool call — file writes and shell commands — before it executes.

![claude-code-harness — health radar](../../../../assets/health/claude-code-harness.svg)

## When to use

You're a developer who lives in Claude Code and keeps watching the agent do the same thing: it skips writing a spec, jumps straight into code, "fixes" bugs by guessing, lets review and tests happen retroactively (or not at all), and then declares the feature done. You want the agent to behave like a disciplined delivery team — write a spec you approve, break it into a plan, only then implement under TDD, run an independent review pass, and package evidence before it calls anything shipped. You install it via Claude Code's plugin marketplace, run `/harness-setup` once, and now you have named verbs — `/harness-plan` (generate `spec.md` + `Plans.md` as the source of truth), `/harness-work` (execute approved tasks inside the plan), `/harness-review` (verification separate from implementation), `/harness-sync` (report drift between plan and reality), `/harness-release` (package only verified evidence into changelog, tag, and release) — that turn ad-hoc agent coding into a repeatable, contract-driven cycle. Five core verbs sit on top of 23 installed skills (Breezing team execution, `/harness-loop` repeated cycles, a session roster with a local inbox so parallel worktree agents can message each other, and single-screen HTML views — Plan Brief / Progress / Acceptance — so a non-engineer sponsor can approve without reading code).

You reach for it specifically when you want the *whole* plan-to-release spine enforced by both contracts you approve and a runtime gate — not just prompt guidance. The guardrail engine is a single Go binary (`bin/harness`, no Node.js dependency) wired into the agent's hooks: a PreToolUse matcher on `Write|Edit|MultiEdit|Bash|Read` routes every pending tool call through a declarative rule table (R01–R16: direct pushes to main, protected paths, forced pushes, history rewrites) plus five "runtime floor" categories the README says have no global disable switch (billing, network egress, secret reads, production deploys, destruction outside the task worktree). The repo also ships `bin/harness doctor --migration-report`, which inventories duplicate skills, plugin caches, and stale symlinks without deleting anything. Codex CLI, Cursor, and Grok have first-party setup scripts; OpenCode is wired but "runtime parity not claimed". [推断]

## How it works

CCH is two coupled layers under one marketplace plugin. The soft layer is Markdown skills: each verb (`/harness-plan`, `/harness-work`, …) instructs the agent to *write and read contract files* — `spec.md` and `Plans.md` — so stages hand off through committed artifacts rather than conversation memory, and anything the agent has not seen stays recorded as `unknown` instead of being invented. The hard layer is one Go binary registered as Claude Code hooks (`hooks/hooks.json`): on every PreToolUse event it reads the pending tool call from stdin, evaluates the rule table and runtime-floor categories, and answers allow / confirm / deny before the action runs — closer to an airport scanner checking your bag before the gate than a camera reviewing footage afterwards. Model roles are routed separately (a dedicated reviewer definition, a `deep`/advisor route, per-role reasoning effort), and manual per-call model choices override the defaults. Your side of the line: state the outcome and completion criteria, approve or correct the generated contract, and judge the acceptance view; CCH's side: planning, implementing, running checks, reviewing, gating commands, and packaging the release.

![claude-code-harness — backbone user story](../../../../assets/flow/claude-code-harness.svg)

<!-- flow-steps:begin (generated from flows/claude-code-harness.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install it from the Claude Code plugin marketplace — `/plugin install claude-code-harness@claude-code-harness-marketplace` — component: `plugin marketplace`
2. **You**: Run setup once to activate the verbs, hooks, and guardrails — `/harness-setup` — component: `setup skill`
3. **claude-code-harness**: Wires a Go engine into the PreToolUse hook — each file write and command is inspected before it runs — component: `PreToolUse hook → bin/harness`
4. **You**: Hand it your intent plus the completion criterion — `/harness-plan Improve the README onboarding flow` — component: `harness-plan skill`
5. **claude-code-harness**: Inspects the code and writes spec.md + Plans.md: scope, acceptance criteria, unknowns, stop conditions — component: `main agent`
6. **You**: Approve or correct the contract, then start the plan — `/harness-work all` — component: `approval + harness-work`
7. **claude-code-harness**: Implements under the plan, runs required checks, and sends review findings back to the worker — `/harness-review` — component: `worker + guardrail engine`
8. **claude-code-harness**: Packages only verified evidence into CHANGELOG, tag, and release — `/harness-release` — component: `release skill`

**Value**: You approve two contracts; the agent can no longer grade its own homework, and risky commands are inspected before they run

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You already run a curated workflow/methodology stack.** This harness is prescriptive (spec-before-code, TDD-gated work, mandatory review verb). Layering it over an existing plan→ship methodology — gstack, Superpowers, your own commands — invites conflicting routing and double-governance; pick one source of truth.
- **You expect identical guarantees on every agent tool.** The README is explicit that "four install routes are not four identical guarantees": only Claude Code, Codex CLI, Cursor, and Grok pass its own H1–H8 acceptance tier, OpenCode claims no runtime parity, and guardrail coverage differs by host (its own docs list it). On native Codex, child agents can inherit the parent's execution permissions, so the reviewer profile alone is not filesystem isolation.
- **One-off scripts, spikes, non-code tasks.** The plan→work→review→release ceremony is overhead when you just want a quick fix or config tweak; it assumes a real software-change loop with artifacts worth gating.
- **You cannot re-verify after every upstream bump.** Behavior lives in both prompts and the Go rule table, and the upstream shipped a major version (4 → 5) between this page's two verification passes, 20 tags deep in the v5 line (2026-09). Pin a version and re-check what the verbs enforce after upgrading.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [gstack](gstack.md) | ✅ | Choose gstack when you want a role-playing persona command loop instead of contract artifacts plus a runtime gate. | Garry Tan's personal Claude Code setup drives a similar plan → build → review → ship loop, but via ~54 persona/utility skills with no execution-time checker. claude-code-harness is fewer, named verbs over explicit `spec.md`/`Plans.md` contracts and a Go guardrail engine that inspects tool calls before they run; gstack leans on personas and a driven browser. |
| [shaping-skills](shaping-skills.md) | ✅ | Choose shaping-skills when you only need the Shape Up define-what-to-build front end. | Ryan Singer's Shape Up "shaping" pack covers only the *define-what-to-build* front end. This harness covers the full define→implement→review→release spine plus the execution gate, so they're complementary rather than substitutes. |
| [Superpowers](../../../agent-dev-methodology/coding-agent-harnesses/superpowers.md) | ✅ | Choose Superpowers when lean cross-harness methodology matters more than a governed contract loop with a guardrail engine. | Cross-harness skills library with the same brainstorm/plan→TDD→verify spine, packaged for many agents. claude-code-harness now officially covers four hosts too, but its differentiators are the spec/plan contract files, the PreToolUse Go gate, and the release-preflight evidence chain — Superpowers ships none of those and stays methodology-only. |
| harness-mem (optional companion) | 未收录 | Reach for harness-mem only as this project's optional cross-session memory add-on, not as a workflow substitute. | A separate repository by the same author for project-scoped memory across sessions; different concern (agent memory vs delivery loop), deliberately not indexed here. |
| Claude Code's native skills / built-in slash commands | 未收录 | Choose native Claude Code skills when you want the platform's own skill ecosystem without a third-party governance layer. | The platform's own skill ecosystem; this is a third-party bundle layered on top, so it can duplicate or conflict with native commands. |

## Health & viability

- **Responsiveness**: Cannot be scored — type_na.
- **Maintenance (2026-09):** very active — last pushed 2026-09-21, latest release v5.15.0 (2026-09-06), with a dense v5.13.x→v5.15.0 tag cadence in the weeks prior, and only ~15 open issues at that pace. It cuts tagged releases, so you *can* pin a version — but read the churn as a cost too: a major bump (4 → 5) landed since June.
- **Governance & bus factor:** single-maintainer `User`-owned repo (Chachamaru127, ~92% of ~1,250 commits; the next "contributor" is a `claude` bot account — the author builds it with the tool itself). No foundation, no vendor backing; roadmap and continuity rest on one person. ~3.1k stars and 300 forks is real but modest adoption.
- **Age & Lindy verdict:** created 2025-12-12, so under a year old — young and unproven on longevity. The release velocity signals energy, not stability; the fact that it dogfoods its own `spec.md`/`Plans.md` in-repo is a good durability signal for the *method*, not for the project's survival. Not yet a Lindy-safe bet.
- **Risk flags:** the Go gate's deny/allow behavior is wired and documented in code, but its effectiveness against a motivated agent is unproven in the field; cross-host enforcement varies by host; behavior baked into prompts and the rule table shifts across version bumps — pin and re-check after upgrades.

## Caveats (unverified)

- [未验证] The pre-execution gate's real-world effect: the wiring is confirmed in-repo (`hooks/hooks.json` PreToolUse matcher on `Write|Edit|MultiEdit|Bash|Read` → `bin/harness`; `go/DESIGN.md` describes `internal/guardrail` with a declarative rule table and deny/allow verdicts), but no block/allow verdict was independently executed for this page.
- [未验证] The "runtime floor has no global disable switch" claim and per-host hardening parity (`docs/hardening-parity.md`) are README/doc claims; the config surfaces that could weaken them were not audited.
- [未验证] Support tiers (Claude Code / Codex CLI / Cursor / Grok "supported" after H1–H8 checks; Codex app, Hermes Agent, GitHub Copilot CLI "candidate"; OpenCode "internal-compatible") are the project's self-assessment; no host activation was tested here.
- [未验证] Model-role routing defaults (e.g. `deep`/advisor on Fable 5.1 high effort, implementation on Sonnet 5, dedicated reviewer on Sonnet 5 xhigh, Codex routes on GPT-6 astra / GPT-5.6 luna) are README values as of 2026-09-27 and change with releases.
- [未验证] Star count (3,140 per GitHub on 2026-09-27), forks (302), open issues (15), language split (Shell ~48%, Go ~47%, Python ~2%, TS ~2%, JS ~1%), and latest release v5.15.0 (2026-09-06) are dated, date-sensitive metadata.
- [推断] The 23-skill set and verb semantics shift release-to-release (skills like `breezing`, `session-send`, `failure-codifier` exist today); verify the current `skills/` listing rather than relying on this page.
- [推断] Because part of the workflow still lives in prompt/markdown skills, the "mandatory" steps (spec-first, TDD) remain prompt-level instructions — the Go gate hard-blocks operations, not process skipping.
