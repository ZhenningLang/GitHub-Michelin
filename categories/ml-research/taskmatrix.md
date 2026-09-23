---
name: TaskMatrix
slug: taskmatrix
repo: https://github.com/chenfei-wu/TaskMatrix
category: ml-research
tags: [visual-chatgpt, tool-routing, foundation-models, multimodal, agent, abandoned, historical-demo]
language: Python
license: MIT
maturity: "research demo (orig. 'Visual ChatGPT', Microsoft); last pushed 2024-01, no commits since — abandoned in practice (as of 2026-06)"
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2024-01-06T02:41:20Z
  default_branch: main
  default_branch_sha: 4b7664f8d3a23804ac1b795d75a73efd162769f0
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:43:05Z
  overall: "?"
  overall_score: null
  scored_axes: 2
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1181
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: E
      raw:
        repo_age_days: 1300
        last_commit_age_days: 1181
        cohort: app
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_window_signal }
    adoption: { reason: no_package_structural }
    governance: { reason: unattributable }
    risk_license: { reason: license_unparsed }
---

# TaskMatrix

A historical research demo (originally "Visual ChatGPT", from Microsoft) that wires ChatGPT to a fixed set of visual foundation models so you can chat to caption, generate, and edit images — interesting as an early tool-routing-agent design, but unmaintained since early 2024 and superseded by modern multimodal LLMs.

![taskmatrix — health radar](../../assets/health/taskmatrix.svg)

## When to use

You're a researcher or engineer studying how the first wave of LLM "tool-routing agents" was built, and you want to read a concrete, runnable reference rather than a paper. You've used GPT-4o or Gemini where vision is native, and you're curious how people bolted vision onto a text-only ChatGPT *before* multimodal models existed: a prompt-driven router (the "Visual ChatGPT" pattern) that parses the user's request, decides which of ~20 visual foundation models (BLIP captioning, Stable Diffusion text-to-image, ControlNet/Pix2Pix editing, segmentation, depth, etc.) to invoke, threads the intermediate images back into the conversation, and stitches a natural-language answer around the tool outputs. TaskMatrix is a clean artifact of that design — you read it (and maybe stand up a piece of it on a GPU box) to understand the manager-prompt, the tool registry, and the image-state plumbing, not to ship it.

It's also a useful teaching reference when you're building your *own* tool-routing agent today and want to see an early, self-contained example of LLM-as-orchestrator over heavyweight specialist models — what the prompt scaffolding looked like, where it was brittle, and why native multimodal models eventually absorbed the whole pattern.

## When NOT to use

- **Anything you intend to keep running.** The repo has had no commits since **2024-01-06**; it is abandoned in practice (not formally `archived`, but functionally dead). Read it, don't depend on it.
- **You want a current image-chat capability.** Modern multimodal LLMs (GPT-4o, Gemini, Claude with vision, Qwen-VL) do captioning / VQA / grounded reasoning natively, in one model, with no foundation-model zoo to host. The whole reason TaskMatrix existed — text-only ChatGPT couldn't see — no longer holds.
- **You want a maintained agent/tool-routing framework.** Today's agent frameworks (LangChain, modern function-calling, MCP-based tooling) do orchestration far better and are actively maintained. Don't build new work on TaskMatrix's bespoke prompt-router.
- **You can't pin old, heavy deps.** It pulls a pinned-circa-2023 stack (specific `transformers`, `diffusers`, `langchain`, Detectron/ControlNet weights, an OpenAI key) onto a multi-GB GPU environment; those versions are stale and may not resolve or run cleanly on current CUDA/PyTorch. [未验证]
- **Security / supply-chain sensitivity.** Unmaintained for 2+ years means no patches; pinned old dependencies accumulate known CVEs over time. Treat it as throwaway research code, not something to expose or trust with secrets.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| Modern multimodal LLMs (GPT-4o / Gemini / Claude vision / Qwen-VL) | 未收录 | Choose modern multimodal LLMs when you need native vision inside one maintained model. | Native vision in a single model — captioning, VQA, generation/editing via the model or its built-in tools; no foundation-model zoo to host, actively maintained. This is what replaced the whole TaskMatrix pattern. |
| HuggingGPT / JARVIS | 未收录 | Choose HuggingGPT/JARVIS when you need the same-era LLM-controller-over-model-catalog idea. | Same era, same idea — an LLM controller that routes tasks to a catalog of Hugging Face models; broader (not vision-only) task scope, also a research demo rather than a maintained product. |
| LangChain agents | 未收录 | Choose LangChain agents when you need a maintained general-purpose LLM tool-orchestration framework. | Maintained, general-purpose LLM tool-orchestration framework; you wire your own tools (including vision models) with current function-calling, instead of TaskMatrix's hand-rolled 2023 prompt-router. |
| Modern agent frameworks (function-calling / MCP-based tooling) | 未收录 | Choose modern agent frameworks when you need current standardized tool access for LLMs. | Current, standardized way to give an LLM tools; far better orchestration, structured tool I/O, and active support than this bespoke demo. |
| [autoresearch](autoresearch.md) | ✅ | Choose autoresearch when you need another single-author research-demo app for agent-driven ML training loops. | Also a single-author research-demo app, but a single-GPU *training* loop for agent-driven ML research — unrelated problem; shares only the "read-it-as-a-reference, don't deploy" posture. |

## Tech stack

- **Language:** Python (~80% per repo).
- **Controller:** an LLM (the README targets OpenAI's ChatGPT/`gpt-3.5` family via the OpenAI API) prompted as a manager that selects and sequences tools. Built on a 2023-era LangChain agent scaffold.
- **Tool zoo:** ~20 visual foundation models loaded as tools — image captioning (BLIP), text-to-image (Stable Diffusion), instruction/edit and conditioning (ControlNet, Pix2Pix), segmentation, depth/edge/pose estimation, VQA, etc. (exact set varies by version).
- **Mechanism:** a prompt-driven router parses intent, dispatches to a foundation model, persists intermediate images as conversation state, and composes a natural-language reply around the outputs.

## Dependencies

- **Runtime:** Python plus a heavy ML stack — `torch`, `transformers`, `diffusers`, `langchain`, and the various model-specific libraries, at versions pinned around 2023. [未验证]
- **Hardware:** a CUDA GPU with substantial VRAM to host multiple large vision models simultaneously; CPU-only is impractical for the generation/editing tools.
- **External services:** an OpenAI API key for the controller LLM (network + cost). Model weights for the visual foundation models must be downloaded (multi-GB).
- **Reproducibility risk:** because deps are old and unpinned-to-current, a clean install today may fail to resolve or run without manual version surgery — budget for that before assuming it works.

## Ops difficulty

**High, and not worth paying.** Even in 2023 this was a non-trivial stand-up: provision a large-VRAM GPU, download many GB of model weights, install a deep ML dependency tree, and supply an OpenAI key. In 2026 the difficulty is compounded by age — the pinned dependency versions predate current CUDA/PyTorch/`transformers` releases, so expect dependency-resolution breakage and patching just to boot it, with no maintainer to file issues against. There's no service-grade deployment story (no packaging, versioning, or CI to lean on); it was always a demo. Run a slice of it on a throwaway box to study the design, but do not operate it.

## Health & viability

- **Responsiveness**: Cannot be scored — no_data.
- **Maintenance (as of 2026-06):** last pushed **2024-01-06**, no commits since — **abandoned in practice** (not formally `archived` on GitHub, but functionally dead). [推断] No releases, no fixes, no maintainer to file issues against.
- **Governance / bus factor:** the repo lives under an individual `User` account (chenfei-wu) though the work originated at Microsoft Research as "Visual ChatGPT." [推断] Whatever institutional backing it once had is gone; there is no team or roadmap behind the current repo.
- **Age & Lindy verdict (created 2023-03, ~3 yr):** this is the **fails-Lindy** case — old *enough to be stale* but no longer active. Age here is a negative, not a positive: the longer it sits unmaintained against a fast-moving stack (CUDA/PyTorch/`transformers`/`diffusers`), the less likely a clean install even runs. Read it as a historical artifact of the pre-multimodal tool-routing era; do not bet on it.
- **Risk flags:** 2+ years unmaintained ⇒ pinned 2023-era deps accumulate known CVEs with no patches — a real supply-chain concern; do not expose it or trust it with secrets. License is MIT (file verified), though GitHub's API shows `NOASSERTION`. [未验证]

## Caveats (unverified)

- [未验证] ~34.1k GitHub stars (34,070) and `pushed_at` 2024-01-06 as of 2026-06; stars are unreliable and date-sensitive — treat as indicative only.
- **License:** the repo's `LICENSE.txt` is an MIT License (Copyright 2023 Microsoft) — **verified** by reading the file. Note that GitHub's API reports the license as `NOASSERTION` / "Other" (no SPDX auto-match), so tooling may show it as unlicensed; the file itself is MIT.
- [推断] The repo is **not** formally `archived` on GitHub, but with no commits since 2024-01-06 it is abandoned in practice — "abandoned" here is inferred from commit history, not a declared project status.
- [未验证] The exact tool roster (~20 visual foundation models), the controller model family (`gpt-3.5`-era), and the LangChain-based scaffold are paraphrased from the README and project history; the precise set and versions should be read off the current tree before relying on them.
- [未验证] Dependency staleness / install breakage on current CUDA/PyTorch is inferred from the 2024-01 freeze and 2023-era pins, not from a fresh install attempt here — verify by trying a clean setup if you must run it.
