---
name: Ponytail
slug: ponytail
repo: https://github.com/DietrichGebert/ponytail
category: engineering
tags: [yagni, over-engineering, behavior-ruleset, agent-skill, multi-harness, token-cost]
language: JavaScript
license: MIT
maturity: v4.10.0, active, ~147k stars (as of 2026-09)
last_verified: 2026-09-28
type: skill-pack
homepage: https://ponytail.dev
upstream:
  pushed_at: 2026-09-14T14:34:56Z
  default_branch: main
  default_branch_sha: e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T09:09:30Z
  overall: B
  overall_score: 3.0
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
        last_commit_age_days: 14
        active_weeks_13: 7
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: C
      raw:
        registry: npmjs.org
        canonical_package: "@dietrichgebert/ponytail"
        dependent_repos_count: 0
        downloads_last_month: 57036
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 108
        last_commit_age_days: 14
        cohort: skill-pack
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 72
        top1_share: 0.524
        top3_share: 0.601
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

# Ponytail

You ask your coding agent for a date picker and it returns flatpickr, a wrapper component, and a stylesheet. Ponytail installs the reflex of the laziest senior dev you've ever met as an always-on ruleset: before writing code the agent must walk a seven-rung ladder (should this exist? does it already? stdlib? native feature?) and hand back the smallest diff that works, with validation, security, and error handling explicitly off the chopping block.

![Ponytail — health radar](../../../assets/health/ponytail.svg)

## When to use

You drive Claude Code, Codex, Copilot CLI, or one of the ~20 other hosts ponytail ships adapters for, and the failure you keep hitting is bloat, not process: the agent adds a dependency where the standard library had it, writes a cache class where `@lru_cache` would do, and leaves a 400-line diff for a 20-line task. You reach for Ponytail when you want a behavior overlay that only *subtracts* code — installable with two slash commands, with intensity levels (`lite/full/ultra/off`), subagent injection you can scope by regex, and a `/ponytail-review` command that hands you a delete-list for an over-engineered diff.

The reason to install a pack instead of writing your own "YAGNI, write one-liners" line: in the author's agentic benchmark the bare prompt is erratic (near or above baseline on several tasks) and was the only arm that dropped a safety guard, while the packaged ruleset landed every run at a claimed 100% safety floor [未验证：作者自建基准，未独立复现，见 benchmarks/results/2026-06-18-agentic.md]. The pack also keeps the discipline coherent across ~20 host adapters via a shared instruction builder, where your hand-rolled rules would drift per editor.

## How it works

You install it once — as a plugin (Claude Code, Codex, Copilot CLI, Grok, Devin, Hermes…) or by copying `AGENTS.md` / the matching rules file on instruction-only hosts (Cursor rules, Windsurf, Cline, Copilot Chat, Aider, Kiro, Zed, Qoder, Amp, Jules). What the project then does for you: its lifecycle hooks — small Node scripts the host runs at session start, on each submitted prompt, and when a subagent spawns — inject the ruleset into the context, track `/ponytail lite|full|ultra|off` level switches (and re-inject on change), and can scope subagent injection via the `PONYTAIL_SUBAGENT_MATCHER` regex. The ruleset itself is prose, not enforcement: the seven-rung ladder (YAGNI → reuse existing code → stdlib → native platform feature → already-installed dependency → one line → minimum that works), run *after* the agent has read the code it touches, plus explicit carve-outs (trust-boundary validation, data-loss error handling, security, accessibility, anything requested), a rule that non-trivial logic leaves one runnable check behind, and a `ponytail:` comment convention that marks deliberate shortcuts with their ceiling and upgrade path. Five companion skills (`/ponytail-review`, `-audit`, `-debt`, `-gain`, `-help`) reuse the same text; an optional MCP server (`ponytail-mcp`) serves the identical ruleset for hosts whose only injection point is the prompt menu. It changes what the agent writes; it does not gate what the agent may ship.

![ponytail — backbone user story](../../../assets/flow/ponytail.svg)

<!-- flow-steps:begin (generated from flows/ponytail.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Add ponytail's plugin marketplace — `/plugin marketplace add DietrichGebert/ponytail`
2. **You**: Install the plugin — as a second, separate prompt — `/plugin install ponytail@ponytail`
3. **Ponytail**: Hooks inject the ruleset at session start and into every spawned subagent — component: `lifecycle hooks`
4. **You**: Ask for the feature exactly as you always would — `Add a cache for these API responses.`
5. **Ponytail**: Before writing code it stops at the first rung that holds: exist? reuse? stdlib? native? one line? — component: `seven-rung ladder`
6. **Ponytail**: Hands back the minimal diff: deliberate corner-cuts marked, one runnable check left behind — `# ponytail: global lock, per-account locks if throughput matters`

**Value**: You stop reviewing 400-line diffs for code the task never asked for — ~54% less code on the author's agentic benchmark, safety guards kept

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You want the agent to follow a whole development process** (brainstorm → plan → TDD → verify), not just write less: use [Superpowers](../../agent-dev-methodology/coding-agent-harnesses/superpowers.md) or [ECC](../../agent-dev-methodology/coding-agent-harnesses/ecc.md) instead — Ponytail installs no workflow, no phases, no subagent pipeline; it only bends what counts as "done code".
- **Your pain is the agent's verbosity, not its volume of code**: pair it with or use [caveman](caveman.md) or [i-have-adhd](i-have-adhd.md) — Ponytail explicitly "governs what you build, not how you talk", and the author's own benchmark shows the terse-prose arm (caveman) cut only −20% LOC and actually *raised* tokens/cost/time on feature tasks.
- **You are on OpenCode 2**: as of 2026-09-28 the plugin implements only the V1 plugin API and silently does nothing on V2 (open issue #863) — copy `AGENTS.md` into your project for instruction-tier behavior, or wait for the V2 entrypoint.
- **You need a deterministic guarantee that over-engineered code won't ship**: this is context-injected persuasion; compliance is model-dependent, and there is no lint-style hard gate — if you need enforcement with evidence, put a line-level CI reviewer such as [Open Code Review](../../ai-code-review/open-code-review.md) in front of the merge, on top of or instead of Ponytail.
- **Cost-sensitivity on deliberative reasoning models**: the README itself warns a terse reasoning model that spends thinking tokens weighing each ladder rung can go the *other* way on cost (it names GPT-5.5) [未验证：作者自述，未复现] — if measured cost matters, run your own comparison before making it always-on, and use `lite` (suggest-only) rather than `full`/`ultra`.
- **Your tasks are already minimal** (CRUD over an existing template): the author's benchmark shows arms converging on irreducible code, so the overlay buys ~0 there while still occupying context every turn — an instruction-only `AGENTS.md` copy, or nothing, is honest.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [caveman](caveman.md) | ✅ | Pair rather than pick: caveman shrinks what the agent says, Ponytail shrinks what it writes — and if you can fix only one axis first, fix the code, because their shared benchmark shows terse prose alone cut little code and raised token spend (+7%) and cost (+3%) on feature tasks. | Stacking two always-on overlays costs context each turn; caveman's optional proxy layer is BSL-1.1 source-available while Ponytail is MIT end to end. |
| [Superpowers](../../agent-dev-methodology/coding-agent-harnesses/superpowers.md) | ✅ | When the agent's failure is process — skipped plans, unverified "done" — pick Superpowers; when the failure is bloat and your process already works, pick Ponytail, which subtracts code without taking over how you work. | Superpowers installs a full methodology (commands, subagents, worktrees) you adopt wholesale; Ponytail installs one behavioral rule with an off-switch and a measured scoreboard. |
| [ECC](../../agent-dev-methodology/coding-agent-harnesses/ecc.md) | ✅ | Pick ECC when you want a batteries-included Claude Code kit (agents, hooks, memory, security scan) as the platform; pick Ponytail when you want to change exactly one failure mode of a working setup — over-engineering — with intensity you can dial. | ECC grows your installed surface and you own the integration; Ponytail stays small but its benefit ceiling is code size and cost, per its own benchmark ("huge where there's bloat to cut, nothing where there isn't"). |
| A bare "write one-liners / YAGNI" line in your AGENTS.md | not a repo | Copying one sentence is free and Ponytail's README admits the honest claim is smaller than the marketing one; the pack earns its install because the packaged ladder is consistent every run and keeps the named safety carve-outs, while the bare prompt arm in the author's benchmark was erratic and the only arm to drop a guard. | Zero install and zero always-on injection vs a plugin, hooks that need `node` on PATH, and prose you hand-maintain instead of the versioned ruleset. |

## Health & viability

- **Maintenance** (verified 2026-09-28 via GitHub API): latest release v4.10.0 on 2026-09-14, same day as the last push; ~10 releases from 2026-06-12 to 2026-09-14, pace slowing versus the June sprint. 310 open issues; earlier hot issues (#126, #65, #97) were engaged and mostly closed, so responsiveness exists but backlog is large for a 3.5-month-old repo.
- **Governance / bus factor**: single personal account (owner type `User`); the top-15 contributor list shows the author at ~114 of ~171 visible contributions [推断：按 contributors API 前 15 名计算，未遍历全部提交], remainder drive-by PRs. No org, no GOVERNANCE/CODEOWNERS/CONTRIBUTING files in the tree; CI does exist (test.yml, publish.yml) with a script that keeps the ~20 rule copies aligned — a real drift control for a ruleset this wide.
- **Backing & longevity**: created 2026-06-12 — too young for any Lindy credit. Funded via GitHub Sponsors plus one visible sponsor (GreenPT logo in README), and the README carries a ponytail.dev waitlist banner reading "Something's coming" [推断：由横幅与域名推断，将出商业产品], so open-core/relicense risk is watch-listed, not observed. MIT license file confirmed by reading `LICENSE` (2026-09-28).
- **Adoption & ecosystem** (dated 2026-09-28): ~147k stars but only ~352 watchers — a virality shape, not a usage shape; verifiable adoption is npm `@dietrichgebert/ponytail` v4.10.0 at ~57k downloads/month (npm API, window 2026-08-28→09-26) and ~20 listed host adapters incl. OpenClaw/ClawHub publishing. Benchmark harness is open and reproducible (`benchmarks/`, promptfoo config), which is above the norm for prompt packs.
- **Risk flags**: the original headline number (80–94% less code) was conceded inflated by a chatty baseline and re-measured (issue #126) — good faith, but it means marketing claims need the benchmark page, not the README hero line. Open as of 2026-09-27: OpenCode 2 no-op (#863); Codex false-positive policy flags (#764) reported by users [未验证：仅见 issue 报告，未复现]. Model-compliance dependence and PATH-sensitive Node hooks are structural, not bugs.

## Caveats (unverified)

- [未验证：未独立复现] All benchmark figures (−54% LOC, −20% cost, −27% time, 100% safe rate; caveman +7% tokens) come from the author's own harness on one repo (full-stack-fastapi-template), one model (Haiku 4.5), n=4; the writeup itself lists these limitations.
- [未验证：作者自述] That deliberative reasoning models (README names GPT-5.5) can end up spending *more* thinking tokens on the ladder — no third-party reproduction found.
- [未验证：未在 OpenCode 2 环境复现] OpenCode 2 plugin no-op claim rests on open issue #863 (created 2026-09-13, still open and active 2026-09-27) and its reporter's fork; not retested here.
- [推断：由 stars 147k vs watchers 352、Trendshift 徽章、发布 3.5 个月推断] Star growth is spike/hype-driven rather than sustained-use growth; treat adoption grade cautiously.
- [推断：仅由 README waitlist 横幅与 ponytail.dev 域名] A commercial product is planned; possible future open-core gating or relicensing — no evidence of either today.
- [推断：contributors API 前 15 名，2026-09-28] Author's commit share ≈ 2/3 → effective single-maintainer bus factor.
- [未验证：仅在 docs/agent-portability.md 数出 ~20+ 适配器条目，未逐一安装测试] The "works with 20 agents" support surface is documented, not independently verified per host.
