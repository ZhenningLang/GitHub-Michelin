# spec-driven-development

> Category node. Spec-, plan-, and context-first methodologies for driving a coding agent — the process you follow, not the harness you install.
> ← back to [agent-dev-methodology](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **12-Factor Agents** | Use it when a framework-built agent is flaky in production and you want named principles (own your prompts, context window, control flow) to review or redesign it — but it is an essay set with no installable code, idle since 2025-09. | "?" (2/5) | [→](12-factor-agents.md) |
| **Get Shit Done (GSD)** | Use it when you build through a coding agent and want a spec-driven, fresh-context phase pipeline that fights context rot. | D (6/6) | [→](get-shit-done.md) |
| **PURE** | Use it when coding-agent intent lineage must live in Git-tracked specs, schemas, registries, phase gates, and tested Shell scripts; it is an early single-maintainer v0.1 framework. | C (5/6) | [→](pure-agentic.md) |
| **Spec-Anchored Agentic Development** | Use it when permanent capability specs and continuous spec-to-code conformance matter more than broad harness support; the bundle is Claude Code-specific and only days old. | B (3/5) | [→](spec-anchored-agentic-development.md) |
| **Spec Kit** | Use it when your team lets Copilot, Claude Code, Codex or Cursor write features and you want each to leave a reviewable spec → plan → tasks trail before code — but it is overkill for 20-line fixes, and its 1.x CLI changes almost weekly. | A (5/6) | [→](spec-kit.md) |
| **USDAD** | Use it when you want editable, prose-first planner/adversary/architect/executor methodology source; it is a one-commit document artifact, not an installable runtime or enforced workflow. | C (4/5) | [→](usdad.md) |
| **BMAD Method** | Use it when you want a role-driven end-to-end agentic method (analyst, PM, architect, UX, dev, review) rather than a thin spec pipeline — and treat its very fast star curve as unproven. | B (4/6) | [→](bmad-method.md) |
| **Improve** | Use it when you want an expensive model to audit your repo read-only and write self-contained plans for cheaper executor models — it never implements anything itself. | B (4/5) | [→](improve.md) |
| **Agent OS** | Use it when you want project standards installed and injected selectively, with plan shaping before implementation — the release line has been quiet since v3.0.0 (2026-01). | B (4/5) | [→](agent-os.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [12-Factor Agents](12-factor-agents.md) | ✅ | "?" (2/5) | Buys a shared, framework-agnostic vocabulary for production agent design; costs you all the engineering, since it ships principles and snippets, not a runtime or SDK. |
| [Get Shit Done (GSD)](get-shit-done.md) | ✅ | D (6/6) | Use it when you build through a coding agent and want a spec-driven, fresh-context phase pipeline that fights context rot. |
| [PURE](pure-agentic.md) | ✅ | C (5/6) | Git-native intent, schema, registry, handoff, and phase-gate machinery; more executable than prose-only methods, but still early. |
| [Spec-Anchored Agentic Development](spec-anchored-agentic-development.md) | ✅ | B (3/5) | Permanent capability specs and continuous spec-to-code conformance, with a Claude Code-specific bundle and almost no adoption history. |
| [Spec Kit](spec-kit.md) | ✅ | A (5/6) | Buys one agent-agnostic, spec-first loop installed by `specify init`; costs six skill invocations and three Markdown artifacts per feature, plus pinning a fast-moving CLI. |
| [USDAD](usdad.md) | ✅ | C (4/5) | Editable planner/adversary/architect/executor methodology documents, not an installable runtime or mechanically enforced workflow. |
| [BMAD Method](bmad-method.md) | ✅ | B (4/6) | Role-heavy end-to-end method (analyst/PM/architect/UX/dev/review) delivered as skills and agent personas; very young with a suspiciously fast star curve. |
| [Improve](improve.md) | ✅ | B (4/5) | Read-only advisor: audits nine categories, then writes handoff plans a cheap executor runs — unlike spec-first or role-first methods, it never implements. |
| [Agent OS](agent-os.md) | ✅ | B (4/5) | Thin standards-and-spec layer that installs project conventions and injects them selectively; the release line has been quiet since v3.0.0 (2026-01). |
| [SWE-bench](../../llm-eval/swe-bench.md) | ✅ | B (6/6) | Benchmark infrastructure, indexed under `llm-eval` rather than here — it grades patches, it is not a development method. |
| LTBL implementation groups / Beam | 未收录 | — | The LTBL implementation repos named in `study-and-experiments/`. `Beam` is deliberately unauthored: the name search matched apache/beam, while the pages mean a different project — pin the repository by hand first. |

## What belongs here

Prose-first or spec-first methodologies and principle sets that decide *what to write down* and in what order before an agent edits code.
