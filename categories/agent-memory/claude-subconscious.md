---
name: Claude Subconscious
slug: claude-subconscious
repo: https://github.com/letta-ai/claude-subconscious
category: agent-memory
tags: [claude-code, letta, plugin, cross-session-memory, hooks, demo]
language: TypeScript
license: MIT
maturity: v2.1.1, active demo (2026-06)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-05-13T00:56:41Z
  default_branch: main
  default_branch_sha: 795046e5e5e4edc2d44e0bc21cda9cbd8f4169bb
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:39:12Z
  overall: C
  overall_score: 2.2
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
        last_commit_age_days: 12
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: C
      raw:
        repo_age_days: 252
        last_commit_age_days: 12
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 5
        top1_share: 0.739
        top3_share: 0.958
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
---

# Claude Subconscious

A Claude Code plugin that runs a background Letta agent which watches your sessions, builds long-term memory blocks, and whispers cross-session guidance back into each prompt via hooks.

![claude-subconscious — health radar](../../assets/health/claude-subconscious.svg)

## When to use

You're a Claude Code power user who keeps re-explaining the same things every session — your preferred test runner, the fact that this repo uses pnpm not npm, the architectural decision you made last week that Claude keeps "forgetting." Claude Code's context dies at the end of each session, so the same corrections recur. You want a memory layer that *accumulates* across sessions without you hand-curating a giant CLAUDE.md. Claude Subconscious installs as a plugin and wires four Claude Code hooks: when a session ends it asynchronously ships the full transcript to a Letta agent (in a detached worker, so it never blocks you), the agent reads your files and updates eight persistent memory blocks (`user_preferences`, `project_context`, `pending_items`, `tool_guidelines`, and more), and on your next `UserPromptSubmit` it injects the relevant memory and any "whispered" guidance via stdout — never touching CLAUDE.md.

It fits best when you already live inside the Letta ecosystem (or want an excuse to try it) and treat this as an exploratory, single-developer convenience layer: one shared "agent brain" serving many projects, each project keeping its own conversation bookkeeping under `.letta/claude/`. If you want to *see* what a subconscious-style background memory agent feels like wired into a real coding loop, this is a working, readable reference implementation built on the Letta Code SDK.

## When NOT to use

- **Production / team use.** The authors explicitly state this is "a demo app built using the Letta Code SDK, and is not intended to be used in production," and point you to Letta Code instead. Do not build a team workflow on it.
- **You're not on Claude Code.** It is a Claude Code plugin end-to-end — it depends on Claude Code's hook lifecycle (`SessionStart` / `UserPromptSubmit` / `PreToolUse` / `Stop`). It is *not* an LLM-agnostic, framework-agnostic memory library; [Mem0](mem0.md) or [Memori](memori.md) are the choices if you need memory inside your own agent code.
- **You can't depend on an external Letta server.** It requires a `LETTA_API_KEY` and a reachable Letta backend (cloud `api.letta.com` or self-hosted). No backend, no memory. That's a hard network dependency on every session boundary.
- **Privacy-sensitive code you can't ship off-box.** The Stop hook sends your **full session transcript** to the Letta agent, and the agent can read your files (read-only by default, but `full` mode grants bash + sub-agent spawning). Think before pointing it at a sensitive repo.
- **You want deterministic, auditable, self-hosted memory with no third-party brain.** The memory lives in a Letta agent, not in a local store you fully own; behavior depends on the agent model and Letta API semantics.
- **Latency-/quota-sensitive workflows.** Every session start, prompt, and stop touches the Letta API; quality "requires several sessions" before guidance becomes useful, per the README.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Mem0](mem0.md) | ✅ | Choose Mem0 when portable application memory matters more than a Claude Code plugin. | Framework-agnostic memory **library/API** you embed in your own agent (Python/TS, any LLM); not a Claude Code plugin and not a background "whisper" agent. Pick it for portable, production-oriented memory. |
| [Memori](memori.md) | ✅ | Choose Memori when you need a SQL-native memory backend rather than Claude-Code-bound hooks. | SQL-native open-source memory engine for agents; also LLM/framework-agnostic and self-hostable. Different shape: a memory backend, not a Claude-Code-bound plugin. |
| Letta Code | 未收录 | Choose Letta Code when you want the team's full coding-agent product instead of this demo. | The production sibling from the same team — a full coding agent on the Letta platform. The README explicitly recommends it over this demo for real use. |
| CLAUDE.md (built-in) | 未收录 | Choose CLAUDE.md when manual, deterministic project memory is enough. | Manual, deterministic, zero-dependency project memory. No background learning or cross-project brain; you curate it by hand. Claude Subconscious explicitly avoids writing here. |
| [Cipher](https://github.com/campfirein/cipher) | 未收录 | Choose Cipher when MCP-based memory across IDEs and CLIs matters more than Claude-only hooks. | MCP-based memory layer for coding agents (works across IDEs/CLIs via MCP); broader client support than a single-tool plugin. |

## Tech stack

- **Language:** TypeScript (~85% of repo per GitHub; also some C#, JavaScript, PowerShell). [未验证] language split is GitHub's linguist estimate.
- **Runtime:** Node.js (TypeScript hook scripts: `session_start.ts`, `sync_letta_memory.ts`, `pretool_sync.ts`, `send_messages_to_letta.ts`).
- **Integration surface:** Claude Code plugin + four hooks (`SessionStart`, `UserPromptSubmit`, `PreToolUse`, `Stop`); content injected as stdout XML tags (`<letta_message>`, `<letta_memory_blocks>`, `<letta_memory_update>`).
- **Memory backend:** Letta agent via `@letta-ai/letta-code-sdk`; eight memory blocks; multi-project "one agent, many projects" model.
- **Models:** any LLM provider Letta exposes (OpenAI / Anthropic / Google / others), selected via `LETTA_MODEL`.

## Dependencies

- **Claude Code** (required; version unspecified in README).
- **Node.js** (required; version unspecified).
- **`@letta-ai/letta-code-sdk`** (installed as a dependency).
- **A Letta backend** — cloud (`api.letta.com`) or self-hosted via `LETTA_BASE_URL`.
- **`LETTA_API_KEY`** (mandatory; from app.letta.com). Provider keys may be needed for non-default models.
- **On-disk state:** `.letta/claude/conversations.json`, `.letta/claude/session-{id}.json`, temp logs under `$TMPDIR/letta-claude-sync-$UID/`; global config at `~/.letta/claude-subconscious/config.json`. [推断] exact global config path from README description.

## Ops difficulty

**Low to install, but with an external-service tail.** Install is a two-line plugin command (`/plugin marketplace add …` then `/plugin install …`) plus setting `LETTA_API_KEY`. The catch is operational dependency, not setup complexity: you're now coupled to a Letta server's availability, quotas, and latency on every session boundary, and a detached background worker (120s timeout) does the transcript sync out of band — failures there are silent to the foreground. Self-hosting Letta to remove the cloud dependency raises ops difficulty to **medium**. A Linux `TMPDIR` workaround is noted for tmpfs cross-device errors during install.

## Health & viability

- **Responsiveness**: Cannot be scored — unknown.
- **Maintenance — slowing, demo-stage (as of 2026-06).** Latest release v2.1.1 (2026-03-30, "Bug fixes"); last push 2026-05-13 — a couple of months stale by 2026-06, no recent activity. Not archived, but the cadence reads as coasting on a demo rather than active product development.
- **Governance & backing — vendor demo (Letta).** Owned by `letta-ai`, the same team behind the Letta platform; backing is real, but this repo is explicitly a *demo* and the team points you to Letta Code for production. The org won't vanish, but it has no incentive to harden the demo. [推断]
- **Age & Lindy — young and explicitly not-for-production.** Created 2026-01, ~5 months old (as of 2026-06). No track record and the authors disclaim production use; Lindy does not apply — this is a reference implementation, not a durable bet.
- **Risk flags — external-brain dependency + transcript egress.** MIT (no relicense risk), but every session boundary touches a Letta backend (cloud or self-host), the Stop hook ships your full transcript off-box, and memory lives in a third-party agent, not a store you own. The dominant risks are the explicit demo status, the hard network dependency, and data egress.

## Caveats (unverified)

- [未验证] Latest release v2.1.1 ("Bug fixes"), published 2026-03-30; repo pushed 2026-05-13 — dates per `gh repo view` on 2026-06-26.
- [未验证] ~2.8k stars as of 2026-06 — GitHub stars are unreliable and date-sensitive; indicative only.
- [未验证] Language breakdown (TypeScript ~85.5%, C# ~10.3%, etc.) is GitHub's estimate; the C# share is unexplained by the README and may be tooling/sample code.
- [推断] Required Node.js and Claude Code minimum versions are not stated in the README; treat version compatibility as unverified.
- [推断] The "eight memory blocks" names and global config path are taken from README/architecture prose, not independently inspected in source.
- [未验证] "Not intended for production" is the authors' own framing; no maturity/SLA claims are independently verified.
