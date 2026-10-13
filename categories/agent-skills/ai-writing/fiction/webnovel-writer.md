---
name: Webnovel Writer
slug: webnovel-writer
repo: https://github.com/lingfengQAQ/webnovel-writer
category: fiction
tags: [claude-code, novel-writing, long-form-writing, rag, continuity, story-memory]
language: Python
license: GPL-3.0
maturity: master v6.2.1 critical-bug maintenance only; v8 separate stable branch, 7467 stars (as of 2026-10-13)
last_verified: 2026-10-13
type: tool
upstream:
  pushed_at: 2026-10-12T07:25:52Z
  default_branch: master
  default_branch_sha: 0af0c0b2fc2e4104e8a12c1d62136c6595a6a983
  archived: false
health:
  schema: 1
  computed_at: 2026-10-13T17:08:29Z
  overall: C
  overall_score: 2.33
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
        last_commit_age_days: 6
        active_weeks_13: 7
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 7.5
        qualifying_issues: 13
        band: relaxed_solo
        window_offset_days: 0
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 1175
        release_assets: 61
        release_tier: D
        signal_basis: releases
    longevity:
      grade: C
      raw:
        repo_age_days: 284
        last_commit_age_days: 6
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.997
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: D
      raw:
        spdx_id: GPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
---

# Webnovel Writer

Chapter 80 forgets a clue planted in chapter 12, and your next prompt cannot reconstruct the book's facts. Webnovel Writer's Claude Code branch records chapter facts and derives searchable continuity state instead of relying on chat history alone.

![Webnovel Writer — health radar](../../../../assets/health/webnovel-writer.svg)

## When to use

You're a serial-fiction author already working in Claude Code, and after dozens of chapters your model starts contradicting character motives, timelines, world rules, and planted clues. You need each chapter to pass through context preparation, drafting, review, fact extraction, a chapter commit, and derived state/index/summary projections. Pick Webnovel Writer over a generic writing prompt because it keeps an auditable project-side story system and queryable continuity state instead of treating every chapter as an isolated chat.

This page's source review covers default branch `master`, the v6 Claude Code plugin. The [version policy](https://github.com/lingfengQAQ/webnovel-writer/blob/0af0c0b2fc2e4104e8a12c1d62136c6595a6a983/README.md#L21-L29) now limits v6 maintenance to critical bugs, freezes v7, and names the separate DeepSeek Harness v8 branch as the current stable workbench. Choose v6 for an existing Claude Code manuscript that needs its continuity chain, not as the actively developed newest product; no validated direct migration of an old book to v8 is documented. Semantic retrieval is optional; README documents a BM25 keyword path when embedding credentials are absent.

## When NOT to use

- **You need an independent desktop novel editor or do not use Claude Code.** Pick [novelWriter](https://github.com/saga-soft/novelWriter) or [Manuskript](https://github.com/olivierkes/manuskript) instead; both target standalone long-form writing, while this project's reviewed master branch is a Claude Code plugin.
- **You are drafting a short story, one article, or one-off marketing copy.** Use a focused drafting prompt or a smaller writing skill instead; story contracts, chapter commits, SQLite indexes, projections, and review gates add setup that only pays off when continuity is the real problem.
- **Your policy forbids prose context from reaching external embedding or reranking APIs.** Use a fully local retrieval stack or accept this project's BM25 fallback; its documented semantic-RAG setup uses compatible external embedding and rerank endpoints.
- **You need to distribute a combined proprietary derivative without a GPL review.** Choose a permissively licensed alternative or obtain legal advice first. The reviewed LICENSE is GPL-3.0: distributing covered copies triggers source-disclosure obligations, not AGPL's network-use disclosure rule. The health field `strong_network_copyleft` is the scorer's combined strong/network-copyleft bucket, not evidence that this project is AGPL.
- **You want ongoing feature development or automatic migration to the current workbench.** Evaluate the same repository's v8 branch for a new DeepSeek Harness workflow, or use novelWriter for an independent editor; master v6 now receives critical-bug fixes only, and v6/v8 installation and migration are not interchangeable.
- **You need independently benchmarked proof that it handles a particular novel length.** Treat the project's 2-million-character-scale claim as unverified and validate with a representative manuscript; no public benchmark was found in this review.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Humanizer-zh](../de-ai-writing/humanizer-zh.md) | ✅ | Choose Webnovel Writer when long-running story facts and chapter continuity are the failure mode; choose Humanizer-zh when polishing Chinese prose is the only job. | Webnovel Writer maintains project state and runs a multi-stage writing workflow; Humanizer-zh is a lightweight advisory rewrite skill. |
| [Baoyu Skills](../content-production/baoyu-skills.md) | ✅ | Choose Webnovel Writer for a novel-specific, stateful serial workflow; choose Baoyu Skills for a broad collection of writing and formatting tasks. | The focused plugin brings contracts, indexes, and review overhead; the general pack is lighter but does not provide a novel continuity system. |
| novelWriter | not indexed | Choose novelWriter when a cross-platform, local desktop editor is required; choose this page when Claude Code should actively plan, draft, and reconcile a serial. | novelWriter avoids model/provider and plugin coupling; Webnovel Writer adds agent-driven retrieval and review. |
| Manuskript | not indexed | Choose Manuskript when you want a standalone outlining and writing application; choose this page when chapter facts must feed an agent-readable state system. | Manuskript keeps the author in a desktop workflow; Webnovel Writer depends on Claude Code and Python tooling. |

## Quick start

For the reviewed v6 branch, install the Claude Code marketplace with `claude plugin marketplace add lingfengQAQ/webnovel-writer --scope user`, then `claude plugin install webnovel-writer@webnovel-writer-marketplace --scope user`, and install the Python requirements as shown in the [master README](https://github.com/lingfengQAQ/webnovel-writer/blob/0af0c0b2fc2e4104e8a12c1d62136c6595a6a983/README.md#L129-L199). Run `/webnovel-init` and answer the book-setting questions; it creates the outline, manuscript directories and story-state files. Use `/webnovel-plan 1` and `/webnovel-write 1` to plan the first volume and draft its first chapter, then consult the saved chapter and review output. The plugin organizes context, review and fact projections; you decide the story, resolve blocking issues, keep backups and pay for Claude Code/model usage. Optional semantic retrieval sends text to embedding/rerank endpoints you configure; BM25 means keyword ranking, not a guarantee that arbitrary API failures silently fall back. These are v6 commands, not v8 installation or a validated book-migration procedure.

![webnovel-writer — backbone user story](../../../../assets/flow/webnovel-writer.svg)

<!-- flow-steps:begin (generated from flows/webnovel-writer.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install the v6 Claude Code plugin and Python requirements
2. **You**: Initialize the book and supply its setting and outline — `/webnovel-init`
3. **Webnovel Writer**: Create story contracts and manuscript project files
4. **You**: Request the first chapter after planning its volume — `/webnovel-write 1`
5. **Webnovel Writer**: Prepare context, draft and review the chapter, then record accepted facts — component: `write skill and Python gates`
6. **Webnovel Writer**: Save the chapter and derive queryable continuity state

**Value**: The next chapter can consult saved story facts rather than only chat history

</details>
<!-- flow-steps:end -->

## Key techniques

- **Accept facts before deriving views.** [`webnovel-writer/scripts/data_modules/chapter_commit_service.py:33–190`](https://github.com/lingfengQAQ/webnovel-writer/blob/0af0c0b2fc2e4104e8a12c1d62136c6595a6a983/webnovel-writer/scripts/data_modules/chapter_commit_service.py#L33-L190) validates review, outline fulfillment, ambiguity resolution and extraction artifacts. Blocking review issues, missed nodes or unresolved ambiguities mark the commit rejected; accepted events become the input to state/index/summary/memory/vector writers. Each writer's status is persisted separately, so a saved commit does not imply every projection succeeded. Review and extraction still depend on agents producing trustworthy artifacts.
- **Spend vector work on candidates at larger scale.** [`webnovel-writer/scripts/data_modules/rag_adapter.py:1156–1280`](https://github.com/lingfengQAQ/webnovel-writer/blob/0af0c0b2fc2e4104e8a12c1d62136c6595a6a983/webnovel-writer/scripts/data_modules/rag_adapter.py#L1156-L1280) uses a full vector scan for small indexes, but combines BM25 candidates with recent chunks before vector scoring for larger indexes. It fuses ranks by reciprocal-rank scoring and then calls reranking. Candidate filtering trades recall for bounded work; in the larger-index branch, a failed query embedding returns an empty result, so README's no-key BM25 path must not be confused with universal outage recovery.
- **Separate prompts from executable gates.** [`webnovel-writer/skills/webnovel-write/SKILL.md:22–26,120–168,214–220`](https://github.com/lingfengQAQ/webnovel-writer/blob/0af0c0b2fc2e4104e8a12c1d62136c6595a6a983/webnovel-writer/skills/webnovel-write/SKILL.md#L120-L168) assigns context/review/extraction to different agents and invokes Python precommit checks on their artifacts. The `--minimal` mode explicitly writes a no-review artifact rather than pretending review happened. This is a workflow with bypass modes, not an independent literary-quality detector.

## Tech stack

- **Core:** Python 3.10+ Claude Code plugin with Skills, Agents, Hooks, and a Python CLI.
- **State:** `.story-system` contracts and chapter commits; JSON plus SQLite indexes, vectors, summaries, and memory projections.
- **Dashboard:** FastAPI, Uvicorn, Watchdog, SSE, and a bundled React/Vite frontend.
- **Retrieval:** BM25 plus optional vector, rerank, hybrid, and graph-hybrid paths through OpenAI-compatible endpoints.

## Dependencies

- **Required:** Claude Code plugin runtime and Python 3.10+.
- **Python packages:** `aiohttp`, `filelock`, and `pydantic`; the dashboard additionally uses FastAPI, Uvicorn, HTTPX, and Watchdog.
- **Optional semantic RAG:** compatible embedding and reranking services plus their API credentials. With no embedding key, documented behavior falls back to BM25.
- **Frontend development only:** Node.js/npm; the released dashboard bundle includes built assets for ordinary use.

## Ops difficulty

**Medium.** Installation is a Claude Code Marketplace plugin plus Python dependencies, but a real book project owns contracts, generated SQLite/JSON state, backups, and optional external RAG credentials. The local dashboard binds to loopback by default, yet maintaining a large manuscript still requires backup and upgrade discipline.

## Health & viability

- **Maintenance snapshot (2026-10-13):** unarchived; master HEAD `0af0c0b` dates to 2026-10-07. The master version policy says v6 critical bugs only, while latest repository releases belong to the separate v8 workbench; a maintenance A does not override that support policy.
- **Governance / bus factor:** the current machine block measures two active maintainers with almost all commits from one contributor. README describes spare-time maintenance and lists sponsorships, not a foundation-backed support guarantee. [推断：concentrated contributions and the stated maintenance policy indicate key-maintainer risk]
- **Age / Lindy:** created 2026-01, with less than one year of history; continued commits are useful signals but do not establish long-term durability.
- **Adoption and risk:** 7467 stars are attention, not verified manuscript-scale performance. GPL-3.0 is a distribution constraint. Risk/license D retains the existing combined strong/network-copyleft bucket; it does not add AGPL network-use obligations to GPL.

## Caveats (unverified)

- [未验证：no representative manuscript was run] Continuity at the claimed 2-million-character scale, writing quality and external retrieval performance were not benchmarked; the plugin and providers were not run end to end.
- [未验证：no validated migration procedure in the reviewed version policy] v6/v8 use different installation paths; direct migration of an existing manuscript has not been established by this review.
- [推断：the scorer and rubric combine GPL and AGPL categories] The bucket name `strong_network_copyleft` is ambiguous. Its retained D grade is not a legal claim that GPL requires network-use source disclosure; assess covered-copy distribution under the actual GPL text.
- [推断：concentrated contributions and stated critical-bug support] Keep local backups and a pinned, forkable v6 copy for an existing serial rather than treating stars as a durability guarantee.
