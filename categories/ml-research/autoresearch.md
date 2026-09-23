---
name: autoresearch
slug: autoresearch
repo: https://github.com/karpathy/autoresearch
category: ml-research
tags: [llm-training, agentic-research, nanochat, single-gpu, reference-implementation]
language: Python
license: MIT
maturity: no tagged release, active, master @ ~36 commits (as of 2026-03)
last_verified: 2026-06-26
type: app
upstream:
  pushed_at: 2026-03-26T00:07:37Z
  default_branch: master
  default_branch_sha: 228791fb499afffb54b46200aca536f79142f117
  archived: false
health:
  schema: 1
  computed_at: 2026-09-23T07:47:51Z
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
        last_commit_age_days: 181
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 7.7
        qualifying_issues: 4
        band: relaxed_solo
        window_offset_days: 6
        source: issue
        inferred: false
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 200
        last_commit_age_days: 181
        cohort: app
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 8
        top1_share: 0.75
        top3_share: 0.821
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    adoption: { reason: no_package_structural }
    risk_license: { reason: license_declared_unverifiable }
---

# autoresearch

A self-contained, single-GPU LLM training harness designed so an AI agent can autonomously iterate on `train.py` overnight — running 5-minute experiments, scoring each by validation bits-per-byte, and keeping only changes that lower the loss.

![autoresearch — health radar](../../assets/health/autoresearch.svg)

## When to use

You're an ML researcher or a tinkerer with one H100 (or similar single GPU) and a hunch that a coding agent could do real ML research if you gave it a tight enough loop. You don't want a 10-hour training run where a single failed idea costs a night; you want a fixed 5-minute budget so an agent can try ~12 ideas an hour and let validation loss be the judge. autoresearch hands you exactly that scaffold: a simplified, self-contained nanochat-style GPT in a single `train.py` that the agent is allowed to edit, a frozen `prepare.py` that pins the data and tokenizer so runs stay comparable, and a `program.md` you (the human) write to steer the agent's strategy. You point your agent at it, walk away, and read the diff that survived in the morning.

It's also a clean reference implementation to read or fork when you want to *study* the "agent-as-researcher" pattern — the val_bpb metric is deliberately vocab-size-independent so architectural changes (different model dims, optimizers like Muon vs AdamW) compare fairly. If you're building your own autonomous-experimentation harness, this is a minimal, legible starting point rather than a heavyweight framework.

## When NOT to use

- **You want a production training framework.** This is a research demo / reference implementation, not a maintained library — no tagged releases, no plugin API, no multi-GPU/distributed story. For real fine-tuning use a framework, not this.
- **You don't have an NVIDIA GPU.** It targets a single NVIDIA GPU (tested on H100); other platforms rely on community forks. The 5-minute fixed budget also means results are explicitly *not comparable* across different compute.
- **You expect the agent to be plug-and-play.** autoresearch supplies the training scaffold and metric; it does **not** ship the agent loop or LLM API wiring — you bring/configure your own coding agent and pay its inference costs.
- **You need reproducible, publishable benchmarks.** The wall-clock-bounded design trades cross-machine comparability for fast iteration by construction; numbers are local to your hardware.
- **You want to train a useful model.** The point is the research *loop*, not the resulting checkpoint — a 5-minute single-GPU run yields a toy-scale model, not something to deploy.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [llm-circuit-finder](llm-circuit-finder.md) | ✅ | Choose llm-circuit-finder when you need a small demo of inference-time layer-duplication/circuit routing. | Also a small self-contained research demo, but explores *inference-time* layer-duplication / circuit routing on existing large models — no training loop, no agent-driven iteration; different research question entirely. |
| nanochat | 未收录 | Choose nanochat when you need the full single-GPU GPT training project this is simplified from. | The full single-GPU GPT training project this is simplified from; meant for humans to train a real small ChatGPT clone end-to-end, not for an agent to mutate under a time budget. |
| [nanoGPT](../llm-training/study-and-experiments/nanogpt.md) | ✅ | Choose nanoGPT when you need the canonical minimal GPT-2 reference to read, and you accept that it is deprecated upstream; choose autoresearch when you want an agent to iterate under a fixed time budget, because nanoGPT offers no automation and no fixed evaluation harness. | nanoGPT is the readable but frozen baseline you edit by hand; autoresearch is the automation layer on top of that idea, with a 5-minute budget and a scored loop. |
| [The AI Scientist](ai-scientist.md) | ✅ | Choose The AI Scientist when you need a heavier idea-to-experiment-to-paper agent-science pipeline. | A heavier end-to-end "agent does science" pipeline (idea→experiment→paper write-up); broader scope and far more moving parts than this single-file training loop. |

## Tech stack

- **Language:** Python (≈83% per repo), with the model, optimizer, and training loop all living in a single `train.py`.
- **Model:** a simplified, self-contained single-GPU implementation of nanochat — a GPT with BPE tokenization, reportedly supporting Muon + AdamW optimizers.
- **Metric:** `val_bpb` (validation bits-per-byte), lower-is-better and vocab-size-independent so architectural changes compare fairly.
- **Tooling:** `uv` as the project/dependency manager; `prepare.py` does one-time data + tokenizer prep and is kept frozen so runs stay comparable.
- **Human/agent split:** humans edit `program.md` (agent instructions / "research org" framing); the agent edits only `train.py`.

## Dependencies

- **Runtime:** Python 3.10+; PyTorch. The README states the training code is self-contained with "no external dependencies beyond PyTorch and a few small packages."
- **Hardware:** a single NVIDIA GPU (tested on H100); CUDA required. No multi-GPU/distributed path.
- **Setup:** install `uv`, run `uv sync`, then `uv run prepare.py` (one-time, ~2 min), then `uv run train.py` (~5 min per experiment).
- **Not bundled:** the coding agent itself and its LLM/API access — you supply and pay for those separately.

## Ops difficulty

**Low to set up, but you own the agent loop.** Getting a manual experiment running is trivial — `uv sync && uv run prepare.py && uv run train.py` on one GPU. The real operational burden is everything *around* the scaffold: provisioning/holding an NVIDIA GPU (H100-class) for hours of overnight iteration, wiring a coding agent to the edit-run-evaluate loop, and watching cost and runaway-agent behavior. There's no service to deploy and nothing to maintain long-term, but it's not a turnkey "press start" autonomous researcher either.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 78.1 hours across 5 qualifying issues/PRs.
- **Maintenance (as of 2026-06):** last pushed 2026-03, ~36 commits on master, no tagged release. [推断] Active in the sense of recently touched, but this is a demo branch, not a maintained product — there is no release cadence to read, and it can change commit-to-commit.
- **Governance / bus factor:** a single-maintainer repo under Karpathy's personal account (`User`-owned) carrying ~88k stars — a textbook **bus-factor flag**: the stars reflect the author's reach, not a team or sustained roadmap. [推断] No governance, no contributors process implied; if the author moves on, it freezes.
- **Age & Lindy verdict (created 2026-03, ~0 yr):** brand-new and ridden on hype/star count, not survival. [推断] **Unproven by Lindy** — judge it as a reference artifact and a pattern to study, not a long-term dependency. Its value is the *idea* (agent-as-researcher under a fixed budget), which outlives any specific commit.
- **Risk flags:** no versioning/API stability; the agent loop and LLM costs are BYO; "research demo" posture is explicit. MIT-licensed, so forking to pin a known-good state is the safe move. [推断]

## Caveats (unverified)

- [未验证] Star/fork counts (~88.7k stars, ~12.8k forks) and "~36 commits on master" are from the GitHub page on 2026-03-26 / 2026-06-26; stars are unreliable and date-sensitive — treat as indicative only.
- [未验证] No tagged release exists; "maturity" reflects an active master branch, not a versioned, API-stable project — behavior can change commit-to-commit.
- [未验证] Optimizer set (Muon + AdamW), BPE tokenization, and ~12 experiments/hour throughput are paraphrased from the README/summary, not independently run — verify against the current `train.py`/`prepare.py` before relying on them.
- [未验证] "Tested on H100" and "5 minutes wall-clock excluding startup/compilation" are the author's stated figures; actual runtime varies with GPU, driver, and compile cache.
- [推断] The agent loop is BYO (bring-your-own coding agent + LLM API); the repo is the training scaffold and metric. Inferred from file roles (`program.md` human-edited, `train.py` agent-edited) — confirm whether any agent runner is bundled in the current tree.
- [未验证] Cross-platform (non-NVIDIA) support is described as existing only via community forks; not verified in this repo.
