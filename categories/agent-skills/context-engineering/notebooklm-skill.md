---
name: NotebookLM Claude Code Skill
slug: notebooklm-skill
repo: https://github.com/PleasePrompto/notebooklm-skill
category: context-engineering
tags: [claude-code, skill, notebooklm, browser-automation, rag-alternative, context-engineering]
language: Python
license: MIT
maturity: v1.3.0, active (2025-11)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2025-11-21T17:42:12Z
  default_branch: master
  default_branch_sha: eea5cb28ba79ab8b078a1eaa44ce9ec44f75dbf8
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:37:43Z
  overall: D
  overall_score: 1.0
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: true
        last_commit_age_days: 12
        active_weeks_13: 1
        carve_out: null
    responsiveness:
      grade: E
      raw:
        median_ttfr_hours: null
        qualifying_issues: 0
        band: relaxed_solo
        window_offset_days: 10
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: E
      raw:
        repo_age_days: 339
        last_commit_age_days: 12
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
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
    adoption: { reason: ambiguous }
---

# NotebookLM Claude Code Skill

A Claude Code skill that drives a real Chrome browser to query your Google NotebookLM notebooks, so the agent pulls source-grounded, citation-backed answers from your own uploaded docs instead of reading files (or hallucinating).

![notebooklm-skill — health radar](../../../assets/health/notebooklm-skill.svg)

## When to use

You're a developer using Claude Code with a large body of reference material — vendor SDK docs, an internal wiki, a workshop manual, a sprawling set of PDFs — that the agent keeps mishandling. When you say "search my docs," it reads file after file (burning tokens), grep-matches keywords and misses the connections between documents, and when it can't find an API it invents a plausible-looking one. You've already uploaded those same docs to Google NotebookLM, where Gemini has pre-processed them into a source-grounded knowledge base, but you're stuck copy-pasting questions and answers between the NotebookLM browser tab and your editor.

You install this skill (`git clone` into `~/.claude/skills/notebooklm/`) so Claude can talk to NotebookLM directly. On first use it self-provisions an isolated `.venv` and a real Chrome instance; you do a one-time Google login in a headful browser window, share each notebook by link, and register it in a small local library with tags. From then on, when you ask "what do my React docs say about hooks?", Claude picks the right notebook, runs the Python script, opens a fresh browser, asks Gemini, and gets a synthesized, citation-backed answer back in the CLI — then uses that to write correct code. It's a retrieval bridge: NotebookLM does the grounding, the skill is the plumbing that lets the agent reach it without you in the loop.

## When NOT to use

- **You don't (or won't) put your docs in Google NotebookLM.** This is a *bridge*, not a RAG engine. It has no embeddings, no vector store, no local index of its own — if your knowledge isn't already in a NotebookLM notebook (and shared "anyone with link"), there is nothing to query. For a self-hosted local RAG you want a different tool entirely.
- **You're not on local Claude Code.** It works *only* with a local Claude Code install. The web UI sandboxes skills without network access, so the browser automation it depends on cannot run. No Codex/Cursor support here — that's the separate [MCP server](https://github.com/PleasePrompto/notebooklm-mcp), not this skill.
- **Automating a Google account is a problem for you.** It logs into and drives Google with a real Chrome session. The author explicitly recommends a *dedicated* Google account and warns automated usage may be detected or flagged; that is a real ToS/account-risk surface, not a hypothetical. [未验证]
- **You need stateful, multi-turn research.** The session model is stateless — each question opens a fresh browser and closes it; there's no persistent chat context and answers can't reference "the previous answer." Multi-step depth comes from the agent re-asking, not from a held session.
- **You're sensitive to NotebookLM's own limits.** Free-tier daily query limits, manual upload, and the public-link share requirement are all NotebookLM constraints this skill inherits and cannot remove.
- **You want a hands-off, hardened dependency.** It auto-installs Google Chrome and a Playwright-based automation stack on first run, and leans on anti-detection ("humanization") heuristics that can break when Google's UI or detection changes.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Agent Skills for Context Engineering](context-engineering-skills.md) | ✅ | Choose Agent Skills for Context Engineering when you need a broader context-methodology pack. | A broader context-engineering *skill pack* (multiple prompt/skill files for context plumbing); this repo is a single, runnable retrieval bridge to one external service (NotebookLM) rather than a methodology bundle. |
| notebooklm-mcp (same author) | 未收录 | Choose notebooklm-mcp when persistent MCP sessions across tools matter more than a single Claude Code skill. | The MCP-server sibling: persistent chat sessions, TypeScript/npm, and multi-tool support (Claude Code, Codex, Cursor). Choose it for stateful research across tools; choose this skill for a zero-server, Python, Claude-Code-only clone-and-go install. |
| Local RAG stacks (LlamaIndex / LangChain retrievers, etc.) | 未收录 | Choose local RAG when you need self-hosted embeddings and vector storage end-to-end. | Self-hosted embeddings + vector DB you own end-to-end; higher setup cost (chunking, embeddings, infra) but no third-party account, no public-share requirement, no browser automation. This skill trades that control for NotebookLM's pre-built Gemini grounding. |
| Built-in file reading / grep retrieval | 未收录 | Choose built-in retrieval when Claude Code's default file access is sufficient. | What Claude Code does by default — high token cost, keyword-shaped retrieval, hallucination on gaps. This skill exists specifically to replace that for doc-heavy tasks. |

## Tech stack

- **Language:** Python (3.8+ per the README badge). [未验证]
- **Browser automation:** `patchright==1.55.2` — a Playwright-based, stealth-oriented automation library — driving **real Google Chrome** (not Chromium) for fingerprint consistency and anti-detection.
- **Config:** `python-dotenv==1.0.0`.
- **Skill surface:** a `SKILL.md` instruction file plus three scripts — `ask_question.py` (query), `notebook_manager.py` (library management), `auth_manager.py` (Google auth). A local `data/` folder (`library.json`, `auth_info.json`, `browser_state/`) holds library + session state and is git-ignored.

## Dependencies

- **Local Claude Code** (not the web UI) on your own machine — hard requirement; the sandbox has no network access for the browser.
- **An active Google account** with access to NotebookLM, plus notebooks you've uploaded docs to and shared by public link.
- **Google Chrome** and the Python automation stack — auto-installed into an isolated `.venv` inside the skill folder on first use (no global installs, but it does pull Chrome down).
- **Internet access** to reach NotebookLM at query time.
- NotebookLM's own service (Gemini-backed); you're subject to its free-tier daily query limits.

## Ops difficulty

**Low-to-medium for an individual; medium once you count the account risk.** Install is a single `git clone`, and the venv/Chrome bootstrap is automatic — there's no server to run, no DB, no deploy. The ongoing burden is the auth and the fragility: you do a one-time interactive Google login (and re-login when the session expires), you must keep notebooks uploaded and link-shared, and the whole thing rides on browser automation against a third-party UI plus anti-detection heuristics — both of which can break without warning when Google changes things. The recommendation to use a throwaway Google account, and the "can't guarantee Google won't detect or flag automated usage" disclaimer, push this above a trivial dev-tool in real-world operational risk. [未验证]

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-06):** likely **coasting / quiet** — latest release v1.3.0 and last push both 2025-11, i.e. ~7 months without a commit as of 2026-06. Not archived, but the gap is a yellow flag for a tool whose whole job is automating a third-party UI (Google NotebookLM) that drifts.
- **Governance / bus factor:** single-maintainer, `User`-owned repo (`PleasePrompto`) at ~7k stars — popular but thin on continuity. The author also ships a separate MCP-server sibling, so attention may be split across the two.
- **Age & Lindy verdict:** young (created 2025-10) *and* apparently dormant — the worst Lindy quadrant for a fragility-prone tool: too new to have a track record, and not actively maintained against the moving target it automates.
- **Risk flags:** the core dependency is browser automation against Google's live UI plus anti-detection heuristics — it can break with no warning when Google changes things, and the author warns of ToS/account-flagging risk. A maintenance gap amplifies that fragility; verify it still works before relying on it.

## Caveats (unverified)

- [未验证] Latest release reported as v1.3.0 ("Timeout Fix & Thinking Detection", published 2025-11-21) with the repo last pushed the same day; license MIT and primary language Python per GitHub metadata as of 2026-06-26. The pace suggests the project may be quiet since late 2025 — re-verify maintenance status and pin behavior before relying on it.
- [未验证] Star count (~7.2k per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, not a quality signal.
- [未验证] Pinned dependency versions (`patchright==1.55.2`, `python-dotenv==1.0.0`) and Python 3.8+ are taken from the README/requirements references and were not exercised here; the auto-install of Chrome and the venv bootstrap were not run.
- [未验证] Google ToS / account-detection risk: the author states humanization features are built in but cannot guarantee Google won't detect or flag automated usage, and recommends a dedicated account. The actual likelihood of flagging, and whether it violates Google's terms, is not independently confirmed.
- [未验证] The script names (`ask_question.py`, `notebook_manager.py`, `auth_manager.py`), the stateless fresh-browser-per-question session model, and the `data/` layout are from the README/repo tree; exact behavior was not executed or independently verified.
- [推断] "Drastically reduced hallucinations" is the project's claim about NotebookLM's source-grounding; answer quality depends entirely on what you uploaded and on NotebookLM/Gemini, which this skill does not control. Behavior is not guaranteed.
