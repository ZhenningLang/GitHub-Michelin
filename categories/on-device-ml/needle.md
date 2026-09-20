---
name: Needle
slug: needle
repo: https://github.com/cactus-compute/needle
category: on-device-ml
tags: [tool-calling, function-calling, structured-extraction, embeddings, on-device, edge-ai, quantization, tinyml, small-language-model, cactus]
language: Python SDK over a prebuilt C engine
license: Apache-2.0
maturity: v3.0.2 (2026-09-18), active, ~11.4k stars (as of 2026-09-19); created 2026-02-24 (~7mo)
last_verified: 2026-09-19
type: model
upstream:
  pushed_at: 2026-09-18T16:02:06Z
  default_branch: main
  default_branch_sha: 94df9999d58a67ff29f032a41f31307c05554bd6
  archived: false
health:
  schema: 1
  computed_at: 2026-09-19T10:41:12Z
  overall: B
  overall_score: 2.75
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 8
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
        repo_age_days: 207
        last_commit_age_days: 1
        cohort: model
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 27
        top1_share: 0.827
        top3_share: 0.874
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
    responsiveness: { reason: type_na }
    adoption: { reason: no_package_structural }
---

# Needle

A 2-bit, 8–29 MB on-device foundation model for tool calling, structured extraction and embeddings on phones, wearables, robots and microcontrollers — it deliberately trades general chat capacity for tiny-footprint task accuracy.

![Needle — health radar](../../assets/health/needle.svg)

## When to use

You're building a mobile app, a wearable, a smart-home hub or a robot, and you want it to *act* on natural language: call the right functions with the right arguments, or pull typed fields out of messy text — with nothing leaving the device. The device may be offline, may be a microcontroller with a few MB of RAM, and per-call API cost or data-residency rules rule out a hosted LLM. A general on-device LLM can chat, but it is unreliable at emitting exactly the JSON your app needs, and a server-side function-calling model is far too big to ship.

So you `pip install cactus-needle`, decorate your functions with `@needle.tool` (the signature gives argument types, the docstring is the tool description), and the SDK runs a 2-bit 8–29 MB Needle model through a native engine on the device. Every token is constrained by a byte-level grammar compiled from your schemas, so the emitted call parses by construction; each turn returns `function_calls`, `reasoning` and a `confidence` score, and an off-topic request returns an empty list instead of a hallucinated call. You pick this over a generic runtime because the tool-call behaviour, the grammar guarantee and the confidence head *are* the product — not something you assemble from a prompt and a JSON parser.

## When NOT to use

- **You want a general chatbot / assistant.** Needle explicitly trades general chat capacity for small-footprint tool accuracy. If the job is open-ended conversation or reasoning, use a general small instruct model (e.g. Qwen2.5-0.5B/1.5B, SmolLM2) served with llama.cpp or Ollama instead — this model will be weaker at chat.
- **You need to serve many concurrent users on a GPU.** This is a per-device model plus SDK, with no batching server. For hosted serving, use [vLLM](../llm-inference/serving-engines/vllm.md) or [TGI](../llm-inference/serving-engines/text-generation-inference.md) (or a hosted API) with a larger function-calling model instead.
- **You need a runtime that can host arbitrary models.** Needle ships one model family; it is not a general inference engine. If model choice is the priority, use [llama.cpp](../llm-inference/local-runtimes/llama-cpp.md), [Ollama](../llm-inference/local-runtimes/ollama.md) or [LiteRT-LM](litert-lm.md).
- **You need maximum tool-call accuracy on hard or ambiguous requests.** When accuracy is the binding constraint and a network round-trip is acceptable, use hosted frontier function calling (OpenAI / Gemini) instead. For self-hosted tool calling, do not reach for [Functionary](../function-calling/functionary.md) — it is deprecated; serve a current function-calling model on [vLLM](../llm-inference/serving-engines/vllm.md) or [SGLang](../llm-inference/serving-engines/sglang.md) instead.
- **You must be fully self-contained from the source repo alone.** The repo carries the SDK and the training/export path; the native engine binary and the `.cact` weights are fetched from Hugging Face on first use and cached under `~/.cache/cactus-needle`. For a truly self-contained artifact, vendor engine + weights, or use llama.cpp with a bundled GGUF.
- **Telemetry must be impossible.** Anonymous usage counts are sent by default (disable with `NEEDLE_TELEMETRY=0` or `DO_NOT_TRACK=1`). If policy forbids any phone-home, choose a model/runtime with none.
- **You want best-in-class general embeddings.** The embedding head is tuned for local search/match/routing alongside the task model. For high-quality retrieval, use a dedicated embedding model (BGE, sentence-transformers) instead.
- **You need a long-term stability guarantee or SLA.** Young project, very fast release churn (v3.0.0 → 3.0.2 shipped within two days), vendor-owned roadmap, and a changing weight format. For a multi-year bet, prefer a mature runtime such as [LiteRT-LM](litert-lm.md).

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [llama.cpp](../llm-inference/local-runtimes/llama-cpp.md) + a small instruct GGUF model | ✅ | Pick llama.cpp when one runtime must host any small model with grammar-constrained output and full platform control; pick Needle when you want the tool-call, grammar and confidence behaviour built in rather than assembled. | Generic runtime with a huge model choice and local control, but you hand-assemble the prompt, tool schema, parser and grammar, and get no calibrated confidence or grounding check. |
| [LiteRT-LM](litert-lm.md) | ✅ | Pick LiteRT-LM when you are deploying Gemma-class models on Android/iOS and want Google's runtime to own NPU/GPU acceleration; pick Needle when the model itself must be a task-specialised tool-caller rather than a general Gemma. | First-party mobile accelerators and Google backing, but it is an inference runtime — you still supply the function-calling model and the tool plumbing. |
| FunctionGemma (Google) | 未收录 | Pick FunctionGemma when you want Google's purpose-built on-device function-calling model family (270M and its fine-tunes) and are happy with Hugging Face weights plus LiteRT/llama.cpp; pick Needle when you want tool calling, typed extraction and embeddings from one small model plus a first-party Python SDK. | Similar on-device tool-calling niche with Google weight releases, but no single SDK/grammar/confidence contract — you wire the runtime and parsing yourself, and it ships as a model card rather than a code repo. |
| [Functionary](../function-calling/functionary.md) | ✅ | Treat Functionary as the historical open function-calling lineage only — it is deprecated (the README carries an explicit banner); for maintained self-hosted tool calling, serve a current function-calling model on vLLM/SGLang, or pick Needle when it must run on-device. | The template for JSON-schema tool calling, but abandoned — no security or model updates — and orders of magnitude larger than an on-device model. |
| Cloud function calling (OpenAI / Gemini) | 未收录 | Pick a hosted frontier API when accuracy on hard, ambiguous requests is the constraint and a network round-trip is acceptable; pick Needle when it must run offline per-device with no per-call cost. | Best-in-class accuracy and zero deployment effort, but network dependency, per-call cost and data leaving the device — the opposite tradeoff from this page. |

## Tech stack

- **Model:** a Laddered Simple Attention Network — a Monarch Hadamard MLP in place of the FFN, GQA attention with causal conv taps, an engram n-gram memory read by gather, and multi-lane hyper-connections. Every depth from 2 to 20 layers is a deployable subnetwork, so you can export a smaller model for a smaller device.
- **SDK:** Python (≥3.9) using `ctypes` over a prebuilt native C engine (`libneedle.so` / `.dylib` / `.dll`); the model talks in JSON envelopes.
- **Training / export:** JAX + Flax + Optax with `safetensors` and `sentencepiece` (the `train` extra), exporting to the `.cact` weight format.
- **Weights/format:** `.cact` is mapped and read in place; the shipped quantization is "Cactus Quants" at 2.125 bits per weight.
- **Decoding:** a byte-level grammar compiled from your function/JSON schemas constrains every generated token; a learned head emits the confidence score.

## Dependencies

- **Runtime:** Python ≥3.9 and `huggingface_hub` — the only hard runtime dependency. The native engine binary is auto-downloaded per platform and cached in `~/.cache/cactus-needle`.
- **Weights:** `needle3.cact` / `needle2.cact` are downloaded from the Hugging Face model repos `Cactus-Compute/needle3` and `Cactus-Compute/needle2`; they are **not** in the GitHub repo.
- **Training:** `jax`, `jaxlib`, `flax`, `optax`, `safetensors`, `sentencepiece`; optional `jax-metal` (Apple) or `jax[cuda12]`.
- **Hardware:** 17 published platform folders spanning macOS, Linux (x86_64/arm64/armv7/riscv64/mipsel), Windows, Android, iOS/tvOS/watchOS and WASM/WASM-component. No database, service or cluster to operate.
- **Network:** required on first run to fetch engine + weights unless you pre-vendor them.

## Ops difficulty

**Low to medium.** `pip install cactus-needle` followed by a first call is easy — it auto-fetches the engine and weights, and there is no server or datastore to run. Shipping to a real device or an air-gapped machine is the actual work: `needle build --platform <folder> [--layers N]` stages the engine next to the weights, and you must keep the two in sync across releases (the `.cact` archive carries a generation tag, so a v2 archive will not load against a v3 engine). Local fine-tuning is a CLI (`needle finetune` → adapter → `needle build --lora`), but it needs the JAX training stack, and the 2-bit post-training/quantization behind the shipped model runs on the vendor's hosted platform. Telemetry is opted out with an environment variable.

## Health & viability

- **Maintenance (2026-09-19).** Active: last push 2026-09-18, PyPI 3.0.0 → 3.0.2 shipped 2026-09-17/18, `v3.0.2` tagged. The GitHub Releases list is empty (tags only). Cadence is very fast. [推断]
- **Governance / backing.** Owned by the `cactus-compute` GitHub org (Cactus Compute, Inc.) — a vendor, not a foundation. The roadmap and the 2-bit post-training/quantization pipeline are vendor-controlled, and that pipeline runs on the vendor's hosted platform. Vendor continuity is therefore the longevity bet. [推断]
- **Bus factor.** Concentrated: in the sampled contributor window the top contributor has 251 contributions and the next has 9. [推断] Organizational backing partly offsets this, but it is a concentration risk.
- **Age & Lindy (created 2026-02-24, ~7 months).** Young. ~11.4k stars in ~7 months is a fast, hype-suspect curve rather than social proof. Lindy-unproven — currently active, durability unknown; judge with age × still-active.
- **Adoption.** ~11.4k stars and 727 forks on GitHub; the Hugging Face weight repos show ~24k downloads (needle3, created 2026-09-16) and ~38.5k downloads (needle2). [推断] Real traction in the on-device tool-calling niche; no independent production-user list was confirmed.
- **Risk flags.** Telemetry on by default; fast version and weight-format churn (v2 → v3 changed the `.cact` tag and the engine dispatch); the shipped 2-bit model depends on a proprietary hosted quantization pipeline; headline benchmark numbers are self-reported. License is Apache-2.0 for the code and declared Apache-2.0 on both HF model cards.

## Caveats (unverified)

- [未验证] Benchmark claims ("beats models 10x its size on mobile tool calls", "matches 2–3x bigger models on extraction", "the 121M model does the arithmetic of a 50M one") are the project's own, against unspecified baselines, and were not independently reproduced here.
- [未验证] "8–29 MB" and "2.125 bits per weight" are README / package-metadata figures; the real footprint depends on depth and quantization and was not measured here.
- [未验证] The 17-platform support list is taken from `needle/agent/fetch.py` at verification time; whether every folder currently ships a working engine was not checked.
- [推断] The `arxiv:2607.18363` tag on the `Cactus-Compute/needle2` Hugging Face repo implies a paper; its claims were not read.
- [推断] "Calibrated confidence" and the grounding/validation behaviour are described from the README plus the SDK's validation code; the calibration quality itself is not independently verified.
- [未验证] Hugging Face download and like counts are date-sensitive snapshots.
- [推断] Bus-factor concentration is inferred from the contributors API sample (top 251 vs next 9); the full commit history was not audited.
- [推断] Telemetry payload contents are per the module's own comment (event, version, engine version, OS/arch, Python version, random install id; no prompts or outputs) sent to a vendor Supabase endpoint; the traffic was not captured or audited.
- [未验证] No independent production-user list or third-party integration ecosystem was confirmed.
