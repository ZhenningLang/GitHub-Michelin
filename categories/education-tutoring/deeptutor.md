---
name: DeepTutor
slug: deeptutor
repo: https://github.com/HKUDS/DeepTutor
category: education-tutoring
tags: [education-tutoring, document-qa, knowledge-base, study-workspace, agent-tools]
language: Python
license: Apache-2.0
maturity: v1.6.14, active, 41531 stars (as of 2026-10-17)
last_verified: 2026-10-17
type: app
upstream:
  pushed_at: 2026-10-16T09:15:09Z
  default_branch: main
  default_branch_sha: 6cf793bd868ba5ecbe64722936d4be8fab5a01df
  archived: false
health:
  schema: 1
  computed_at: 2026-10-17T08:09:10Z
  overall: B
  overall_score: 3.25
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 9
        active_weeks_13: 12
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
        repo_age_days: 293
        last_commit_age_days: 9
        cohort: app
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 97
        top1_share: 0.549
        top3_share: 0.663
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
    adoption: { reason: no_package_structural }
---
# DeepTutor

Your textbook, notes and practice questions sit in separate tabs, while a generic chatbot answers without looking at them. DeepTutor puts document libraries, tool-assisted answers and study workflows in one self-hosted learning workspace.

![deeptutor — health radar](../../assets/health/deeptutor.svg)

## When to use

You are studying a course from uploaded textbooks, asking why a derivation works and turning the same material into practice or reading sessions. Choose DeepTutor when document-grounded chat should live alongside course study, quizzes, reading and saved learning context, rather than building that product around a retrieval library. Its app/CLI and shared agent loop provide those surfaces; the model and retrieved material still determine answer quality.

## When NOT to use

- **You only need a shared chat front end over local models and files.** Choose [Open WebUI](../llm-chat-ui/open-webui.md); DeepTutor's course, practice, memory and tool surfaces add configuration you may not need.
- **You want to publish business workflows behind an API.** Choose [Dify](../agent-frameworks/workflow-builders/dify.md), subject to its license conditions, rather than adapting a learner-oriented product.
- **You need exact control over ingestion/retrieval and a small application surface.** Build with [LlamaIndex](../agent-frameworks/workflow-builders/llamaindex.md); DeepTutor's full package brings the Web/server/model/document stack, not just one query function.
- **Course materials must not leave your system.** Use locally hosted language/embedding models and local parsing, or a smaller local retrieval stack. Self-hosting the UI does not keep excerpts private when configured providers or parsing/search services are remote.
- **Correct grading, teaching efficacy or hostile multi-tenant isolation is a hard guarantee.** Use instructor-reviewed assessment and independently audited deployment controls. Workspace separation is useful, but account settings/credentials/memory remain shared between that account's workspaces, and some execution fallback is documented as best effort.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Open WebUI](../llm-chat-ui/open-webui.md) | ✅ | Choose Open WebUI for a general local-model/document chat portal; choose DeepTutor when reading, practice and course study belong in the same workspace. | Less education-specific surface versus more learning workflow configuration; check Open WebUI's branding/license constraints. |
| [Dify](../agent-frameworks/workflow-builders/dify.md) | ✅ | Choose Dify to design and publish reusable business LLM apps; choose DeepTutor for the learner-facing study experience. | Canvas/API product delivery versus built-in study modes; Dify has its own hosting/license conditions. |
| [LlamaIndex](../agent-frameworks/workflow-builders/llamaindex.md) | ✅ | Choose LlamaIndex when engineers must own each retrieval stage; choose DeepTutor when a study app and CLI are more valuable than minimal integration code. | Fine-grained Python control versus a ready learning product; neither removes provider costs or factual validation. |

## Quick start

For the full local package, use Python `>=3.11,<3.15` and Node.js 20+, choose a persistent runtime-home folder, then follow [README:322–336](https://github.com/HKUDS/DeepTutor/blob/6cf793bd868ba5ecbe64722936d4be8fab5a01df/README.md#L322-L336): `pip install -U deeptutor`, `deeptutor init`, and `deeptutor start` for the Web app. Configure a language-model provider and an embedding provider — the latter turns text into numeric vectors for search — before indexing course material. Create a library with `deeptutor kb create my-kb --doc textbook.pdf`, then use `deeptutor chat --capability deep_solve --kb my-kb`; RAG means retrieving passages to supply to the model. The README still includes `--tool rag`, but the [CLI guide](https://github.com/HKUDS/DeepTutor/blob/6cf793bd868ba5ecbe64722936d4be8fab5a01df/deeptutor_cli/README.md#L65-L75) and [tool composer](https://github.com/HKUDS/DeepTutor/blob/6cf793bd868ba5ecbe64722936d4be8fab5a01df/deeptutor/agents/_shared/tool_composition.py#L186-L211) mount retrieval from the attached library; that extra toggle is unnecessary. DeepTutor parses/indexes the file and runs a tool-assisted answer loop; you supply the material, provider credentials and question, inspect indexing status and verify the answer against its collected sources. You also own persistent data backups, model/embedding charges or local hardware, and any optional parser/search/tool services. Workspaces scope study data, not every account-level setting or memory, as [the workspace guide](https://github.com/HKUDS/DeepTutor/blob/6cf793bd868ba5ecbe64722936d4be8fab5a01df/docs-for-user/workspaces.md#L7-L19) explains.

![deeptutor — backbone user story](../../assets/flow/deeptutor.svg)

<!-- flow-steps:begin (generated from flows/deeptutor.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install and configure language and embedding providers in a persistent runtime home — `pip install -U deeptutor · deeptutor init`
2. **You**: Create a course library from your textbook — `deeptutor kb create my-kb --doc textbook.pdf`
3. **DeepTutor**: Parse and index the material, retaining indexing status — component: `knowledge library + LlamaIndex`
4. **You**: Ask a course question with retrieval enabled for that library — `deeptutor chat --capability deep_solve --kb my-kb`
5. **DeepTutor**: Run bounded model/tool rounds and retain tool evidence — component: `AgentLoop`
6. **DeepTutor**: Return the answer and any collected source references for review

**Value**: Your course materials and a traceable tool-assisted explanation share one study workflow

</details>
<!-- flow-steps:end -->

## Key techniques

![DeepTutor — mechanism diagram](../../assets/mechanism/deeptutor.svg)

<!-- mechanism:begin (generated from mechanisms/deeptutor.json by tools/mechanism_card.py; do not edit) -->
<details>
<summary>Text version of the mechanism</summary>

- Course library documents
- Per-library lock + run journal①
- Indexing worker①
- Dead owner: interrupted / unknown①
- Count real roots before display limit②
- Inventory or unavailable; not index proof②
- Model exploration rounds③
- Dispatch tools / collect sources + replies③
- Bounded settlement / tool-less finish③
- Answer for review, not correctness proof

- Course library documents → Per-library lock + run journal①
- Per-library lock + run journal① → Indexing worker①
- Indexing worker① → Dead owner: interrupted / unknown① (owner dies) [optional/fallback]
- Course library documents → Count real roots before display limit②
- Count real roots before display limit② → Inventory or unavailable; not index proof②
- Model exploration rounds③ → Dispatch tools / collect sources + replies③ (requested)
- Dispatch tools / collect sources + replies③ → Model exploration rounds③ (evidence in next round)
- Model exploration rounds③ → Answer for review, not correctness proof (no tools; answer ready)
- Model exploration rounds③ → Bounded settlement / tool-less finish③ (budget reached)
- Bounded settlement / tool-less finish③ → Answer for review, not correctness proof

</details>
<!-- mechanism:end -->

### 1. Journal indexing ownership and interruption

- **Problem:** A crashed indexing worker must not leave “running” work looking complete or allow a second worker to write concurrently.
- **How:** A per-library operating-system lock protects each new run; durable task and cancellation records retain progress. The status reader presents a dead worker's unfinished documents as unknown and the run as interrupted.
- **Limits:** This makes failures inspectable, not automatically resumable at every instruction: retries reuse validated parser outputs and completed slices, but restart an interrupted stage without a saved checkpoint.
- **Source:** [`indexing_run.py:85–162`](https://github.com/HKUDS/DeepTutor/blob/6cf793bd868ba5ecbe64722936d4be8fab5a01df/deeptutor/knowledge/indexing_run.py#L85-L162), [`indexing_run.py:209–250`](https://github.com/HKUDS/DeepTutor/blob/6cf793bd868ba5ecbe64722936d4be8fab5a01df/deeptutor/knowledge/indexing_run.py#L209-L250).

### 2. Count documents independently of retrieved passages

- **Problem:** Similar passages cannot reliably answer whether a particular file was uploaded.
- **How:** The manifest, a document inventory, walks the actual document root and counts matches before limiting the displayed list. It reports missing roots or non-enumerable remote libraries as unavailable, not as an empty library.
- **Limits:** Remote inventory uses a service-specific reader when one exists; local inventory does not prove that every listed document was successfully indexed.
- **Source:** [`manifest.py:147–239`](https://github.com/HKUDS/DeepTutor/blob/6cf793bd868ba5ecbe64722936d4be8fab5a01df/deeptutor/knowledge/manifest.py#L147-L239), [`manifest.py:242–254`](https://github.com/HKUDS/DeepTutor/blob/6cf793bd868ba5ecbe64722936d4be8fab5a01df/deeptutor/knowledge/manifest.py#L242-L254).

### 3. Return tool evidence to a bounded answer loop

- **Problem:** Retrieved material and user clarifications are lost if each model call starts without the preceding tool results.
- **How:** The loop appends requested tools, their messages and collected sources to the ongoing task, including replies to tool-requested user questions. With no tool request and a complete answer it exits normally; budget exhaustion instead leads to bounded settlement rounds and, if necessary, a tool-less forced finish.
- **Limits:** Budgets bound tool exploration; saved evidence and an eventual answer do not guarantee a correct explanation or grade.
- **Source:** [`agent_loop.py:403–451`](https://github.com/HKUDS/DeepTutor/blob/6cf793bd868ba5ecbe64722936d4be8fab5a01df/deeptutor/agents/loop/agent_loop.py#L403-L451), [`agent_loop.py:480–481`](https://github.com/HKUDS/DeepTutor/blob/6cf793bd868ba5ecbe64722936d4be8fab5a01df/deeptutor/agents/loop/agent_loop.py#L480-L481), [`agent_loop.py:655–743`](https://github.com/HKUDS/DeepTutor/blob/6cf793bd868ba5ecbe64722936d4be8fab5a01df/deeptutor/agents/loop/agent_loop.py#L655-L743), [`agent_loop.py:837–887`](https://github.com/HKUDS/DeepTutor/blob/6cf793bd868ba5ecbe64722936d4be8fab5a01df/deeptutor/agents/loop/agent_loop.py#L837-L887).

## Tech stack

- **Python backend/CLI:** FastAPI, Typer, Pydantic, provider SDKs and shared agent/capability runtimes; main `__version__.py` is 1.6.14.
- **Web:** TypeScript, Next.js 16 and React 19, served through the full package or container.
- **Retrieval/storage:** LlamaIndex with FAISS/BM25 integrations and multiple optional engine connectors; SQLite-backed local state and file-based indexes/settings. The manifest includes server, document and model libraries by default.

## Dependencies

- **Full local install:** Python 3.11–3.14 and Node.js 20+; source development recommends Node 22. Docker bundles the app runtime, but requires a persistent data volume. The separate source CLI-only package omits Web assets/server dependencies.
- **Working model configuration:** a language model for answers and embeddings for ordinary indexed document retrieval; remote providers need credentials and send relevant content outside the app host. Local models need the corresponding hardware/service.
- **Data and integrations:** preserve runtime home and workspace/index storage. Parsing engines, search, GraphRAG/LightRAG, external knowledge stores, speech and agent tools have their own optional packages/services; not every advertised connector is part of the base experience.

## Ops difficulty

**Medium to high.** One local app/container is easy to try, but a reliable course workspace needs provider setup, embedding/index compatibility, parser failure recovery and backups. Shared or remotely reachable deployment adds authentication, grants, network isolation and tool permissions. Do not expose a default trial as a hardened school service; the README distinguishes actual sandbox enforcement from a best-effort local subprocess fallback.


## Health & viability

- **Maintenance (2026-10-17):** unarchived HKUDS repository; default-branch commit and latest release v1.6.14 are from 2026-10-08. README release history shows frequent feature/fix updates, so pin and test upgrades rather than assuming stable behavior from the version number.
- **Machine profile:** overall B (4/6 scored axes); maintenance A, longevity C, governance B and license risk A. Responsiveness is now unknown (`no_window_signal`): the sampled 90-day window contained no qualifying issue/PR response signal, which means unknown, not slow. Adoption remains unknown because the scorer could not attribute a canonical package/install counter, not because no package exists.
- **Adoption / backing:** 41531 stars; the latest release publishes v1.6.14, while the scorer returns `no_package_structural` for adoption. Release availability and stars do not establish measured classroom use or efficacy.
- **Age / license:** created 2025-12-28, 293 days old; HKUDS ownership and a contributor base do not establish a multi-year support history. Apache-2.0 is verified from LICENSE and manifest. [推断：young age and frequent feature changes] Budget for integration churn and instructor review.

## Caveats (unverified)

- [未验证：no application/model/indexing run was performed] Installation, parser accuracy, generated answers and educational outcomes were checked only as source/API claims, not exercised with a course dataset.
- [未验证：scorer lacks attributable installation metrics] The existing adoption unknown persists despite a published PyPI package; this page does not infer usage from stars or replace the machine grade.
- [未验证：no qualifying issue/PR response signal in the sampled 90-day window] Responsiveness is unknown; this run cannot conclude that maintainers respond slowly.
- [推断：293-day age and rapid release history] Its study/tool surface will need upgrade tests and sustained instructor oversight; account/workspace boundaries are not an independently audited isolation guarantee.
