---
name: BitNet
slug: bitnet
repo: https://github.com/microsoft/BitNet
category: on-device-ml
tags: [1-bit-llm, ternary, cpu-inference, quantization, llama-cpp, edge-ai, bitnet-b1.58, microsoft]
language: Python (tooling) + C++ kernels
license: MIT
maturity: No tagged releases; commit-versioned, ~40.3k stars, last push 2026-07-27; created 2024-08; Microsoft-maintained (as of 2026-09-28)
last_verified: 2026-09-28
type: framework
upstream:
  pushed_at: 2026-07-27T05:52:06Z
  default_branch: main
  default_branch_sha: 0b341e582afbf9e1011f24744b554c96a3477eb5
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T07:57:48Z
  overall: B
  overall_score: 3.2
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
        last_commit_age_days: 63
        active_weeks_13: 3
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 44.6
        qualifying_issues: 13
        band: default
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 784
        last_commit_age_days: 63
        cohort: framework
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.579
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

# BitNet

An ordinary laptop CPU chokes on a 7B 4-bit model — slow answers, fans spinning, battery draining. bitnet.cpp is Microsoft's inference runtime for ternary LLMs whose weights are only −1/0/+1 (about 1.58 bits): custom CPU kernels turn the matrix multiplies into lookup-and-add work, so models that were *trained* ternary run fast and cool on plain x86/ARM CPUs. Inference only; no training.

![bitnet — health radar](../../assets/health/bitnet.svg)

## When to use

You're building a local assistant feature into a desktop app that has to ship to ordinary laptops — some Intel/AMD x86, some ARM (Apple silicon, a few Windows-on-ARM machines), often with no usable GPU and only 4–8GB of free RAM. You've already decided you don't want a cloud round-trip: the data is sensitive, you want it to work offline, and you don't want a per-call API bill scaling with your user count. A normal 7B GGUF model in 4-bit still feels heavy on a low-end CPU, and energy/battery cost matters because users complain when a background feature spins the fans.

So you reach for BitNet. You pick a **ternary** model that was actually trained 1.58-bit — BitNet-b1.58-2B-4T is the official one, with community ports like Falcon3 and a Llama3-8B-1.58 — convert it with the repo's setup script, and let `bitnet.cpp`'s I2_S/TL1/TL2 kernels run it. Because the weights are ternary, the matmuls become lookup/add-heavy work that the custom kernels exploit, so on CPU you get a reported multi-x speedup and large energy reduction versus a standard quantized baseline, and a small model fits comfortably in your RAM budget. The framework is a thin llama.cpp derivative, so the `llama-cli`-style runtime and GGUF tooling feel familiar. Since mid-2026 the same engine also runs Microsoft's official 1-bit *embedding* models (BitNet-embedding-0.6B/270M), so retrieval pipelines can join chat on this CPU path.

## How it works

bitnet.cpp is a slim fork of llama.cpp specialized for one model shape: **ternary** weights — every stored weight is just −1, 0, or +1, roughly 1.58 bits per value, and the model was *trained* that way rather than squashed afterwards. That turns the dominant matmul into integer lookups and adds — the custom kernels (I2_S for x86+ARM, TL1 for ARM, TL2 for x86, a lookup-table idea borrowed from Microsoft's T-MAC) exploit the tiny weight alphabet where llama.cpp's generic GEMM loop still multiplies. What you do: build from source (Python ≥ 3.10, CMake ≥ 3.22, Clang ≥ 18, Conda recommended), grab a supported ternary checkpoint from Hugging Face, and run the repo's `setup_env.py` to convert it to the kernel-ready format; day-to-day use is the llama.cpp-style CLI (`run_inference.py`, `-cnv` for chat mode). What it does: executes that converted model on CPU with the reported multi-x speedups and 55–82% energy cuts (README claims, see Caveats), with an optional official GPU kernel path and NPU listed as coming next. What stays yours: choosing from the small curated model list, pinning a commit (there are no tagged releases), and building any UX around the CLI.

![BitNet — backbone user story](../../assets/flow/bitnet.svg)

<!-- flow-steps:begin (generated from flows/bitnet.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Clone the repo and install Python dependencies — `git clone --recursive https://github.com/microsoft/BitNet.git`
2. **You**: Download the official 2B ternary model and run the setup script — `python setup_env.py -md models/BitNet-b1.58-2B-4T -q i2_s`
3. **BitNet**: Converts the weights to the I2_S layout and builds the tuned kernels for your CPU — component: `setup_env.py`
4. **You**: Start a chat loop on the quantized file — `python run_inference.py -m models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf · -cnv`
5. **BitNet**: Decodes with lookup-and-add ternary kernels — fast and low-energy on plain x86/ARM CPUs, no GPU — component: `I2_S kernel`

**Value**: A 2.4B ternary LLM chatting on an ordinary laptop CPU — no GPU, with the README's reported multi-x speedup and large energy savings

</details>
<!-- flow-steps:end -->


## When NOT to use

- **You can't change the model.** BitNet only accelerates models that were *trained* ternary (BitNet-b1.58 lineage, specific Falcon3/Llama3-1.58 ports). You cannot point it at an arbitrary Hugging Face FP16/4-bit model and get the speedup — that's a hard constraint, not a tuning knob. For general GGUF models use plain llama.cpp.
- **You need a frozen, supported runtime.** There are no tagged releases — it's versioned by git commits, and the README markets GPU/NPU paths as "coming"/separate; the project reads more like a research-grade reference implementation than a stable product SDK. Pin a commit and expect churn.
- **You want maximum accuracy or a large model.** 1.58-bit ternary trades quality for size/speed; the well-supported models top out around 2–8B and a tiny ternary model will hallucinate and mis-format more than a same-size 4-bit model. This is for cheap, short, structured CPU workloads, not best-in-class reasoning.
- **You want GPU/mobile as the primary target.** This is a CPU-first framework. GPU support exists but is secondary; there's no first-class Android/iOS SDK. For mobile-LLM ergonomics use a mobile-native runtime (see Comparison).
- **You want a turnkey app or chat UI.** It's a build-from-source CMake/Clang toolchain plus a CLI, not an end-user app — you assemble the UX yourself.
- **Bleeding-edge model coverage.** New ternary models only work once someone wires up the conversion/kernel path; the supported list is small and curated, not "any new model day one".

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [llama.cpp](../llm-inference/local-runtimes/llama-cpp.md) | ✅ | Choose llama.cpp when you need the upstream general-purpose GGUF runtime. | The general-purpose CPU/GPU GGUF runtime BitNet forks; runs *any* quantized model and is far more mature, but its generic 1.5/2-bit quant doesn't match BitNet's purpose-built ternary kernels for natively-1.58-bit models. |
| [LiteRT-LM](litert-lm.md) | ✅ | Choose LiteRT-LM when you need Google's mobile-first on-device LLM runtime. | Google's mobile-first on-device LLM runtime (Gemma-centric, Android/iOS/NPU). Better mobile SDK and accelerator story; not specialized for ternary 1-bit models and CPU energy efficiency the way BitNet is. |
| [Google AI Edge Gallery](ai-edge-gallery.md) | ✅ | Choose Google AI Edge Gallery when you need a demo app/catalog, not a CPU inference engine. | A demo app / catalog for trying on-device models on Android, not a CPU inference engine — different layer entirely; complementary, not a substitute for a runtime. |
| Microsoft T-MAC | 未收录 | Choose T-MAC when you need the low-bit CPU kernel library beneath BitNet. | The low-bit CPU kernel library whose lookup-table method BitNet builds on; a kernel/library layer, whereas BitNet is the packaged end-to-end ternary inference framework. |
| [MLX / mlx-lm (Apple)](mlx-mlx-lm.md) | ✅ | Choose MLX when you need fast Apple-silicon inference with Python/Swift ergonomics. | Fast Apple-silicon inference with clean Python/Swift ergonomics and broad model support, but Apple-only and not specialized for ternary 1-bit weights. |
| [Unsloth](../llm-training/unsloth.md) / GPTQ-AWQ stacks | 部分已收录 | Choose Unsloth or GPTQ/AWQ when you need post-hoc 4-bit quantization for normal models. | Post-hoc quantize normal models to 4-bit; broadly applicable but can't reach 1.58-bit-native efficiency — different quantization philosophy (compress-after vs train-ternary). |

## Tech stack

- **Runtime core:** C++ — a fork/derivative of **llama.cpp**, reusing its GGUF format and CLI/server scaffolding.
- **Custom kernels:** `I2_S` (2-bit symmetric, x86 + ARM), `TL1` (ternary lookup, ARM), `TL2` (ternary lookup, x86); lookup-table approach derived from Microsoft **T-MAC**.
- **Tooling:** Python setup/conversion scripts (`setup_env.py`, `run_inference.py`), Hugging Face CLI for model download.
- **Build:** CMake + Clang/LLVM toolchain.
- **Targets:** x86 and ARM CPUs first-class; GPU path documented separately; NPU listed as upcoming.

## Dependencies

- **Build toolchain:** Python ≥ 3.10, CMake ≥ 3.22, **Clang/LLVM ≥ 18** (a relatively new compiler — a common install snag); Conda recommended.
- **Models:** a *ternary* model in supported format — BitNet-b1.58-2B-4T (official; 2.4B, chat-ready), the official 1-bit embedding models BitNet-embedding-0.6B/270M (added 2026-07), or community ports (Falcon3 1B–10B, Falcon-E, Llama3-8B-1.58, bitnet_b1_58-large/3B), pulled via the Hugging Face CLI and converted by the repo scripts.
- **Hardware:** an x86 or ARM CPU; no GPU required for the CPU path. RAM scales with model size (a 2–3B ternary model is small, but still needs a few GB).
- **No package install** — you build from source; there is no `pip install bitnet` runtime package for the engine.

## Ops difficulty

**Medium.** There's no pip-installable engine: you clone, set up a Conda env, install **Clang ≥ 18** and CMake ≥ 3.22 (the Clang version requirement and platform-specific kernel selection — TL1 on ARM vs TL2 on x86 vs I2_S — are the usual friction points), then run a setup script to convert/quantize the model and build with CMake. Once built, day-to-day inference via the CLI is straightforward and the small models are easy on resources. The bigger operational risks are *project* risks, not runtime ones: no tagged releases (pin a commit), a small/curated model list, and GPU/NPU paths that are still maturing — so treat upgrades and platform expansion as a moving target.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 44.6 hours across 13 qualifying issues/PRs (health scorer, 2026-09-28).
- **Maintenance (2026-09):** last push 2026-07-27 — about 9 weeks idle at verification, with activity in 3 of the last 13 weeks, so the repo reads as **bursty/coasting** rather than week-to-week iteration; the July 2026 news block (official 1-bit embedding models, VibeASR.cpp) shows the team still ships when it moves. No tagged releases means cadence is judged from commit recency, not a release stream.
- **Governance / backing:** Microsoft-owned (`microsoft/BitNet`, Organization); the scorer counts 3 active committers in the last 12 months (~58% from the top one) — a focused Microsoft research team, not an open community. That removes single-maintainer bus-factor risk, but Microsoft is also a serial project-archiver — vendor backing here signals "research reference implementation kept alive," not a productized, SLA-backed SDK.
- **Age & Lindy (created 2024-08, ~2yr):** young and still-active enough to not fail Lindy, but too new to be a proven long-lived bet. [推断] The value rides on the BitNet-b1.58 research line continuing; treat it as **promising-but-unproven** infrastructure.
- **Adoption:** ~40.3k stars (GitHub API, 2026-09-28) is strong attention, but the curated ternary-model list and CPU-first scope keep real production adoption narrow; the health radar could not score this axis this cycle (ambiguous package/dependent signals — the engine is not pip-installable). [未验证]
- **Risk flags:** MIT-licensed (no relicense risk). The live flags are commit-versioning churn (pin a commit), a small supported-model surface, and GPU/NPU paths still maturing. [推断]

## Caveats (unverified)

- [未验证] Speedup and energy figures (ARM ~1.37–5.07x / ~55–70% energy; x86 ~2.37–6.17x / ~72–82% energy; "+1.15–2.1x" from later kernels; 100B model at "5–7 tok/s on a single CPU") are the project's own README claims against unspecified baselines — not independently reproduced here; vary by CPU, model, and kernel.
- [未验证] ~40.3k stars (GitHub API, 2026-09-28) — GitHub stars are unreliable and date-sensitive; treat as indicative only.
- [推断] No GitHub releases/tags were returned (2026-09-28: releases/latest 404, tags empty), so the project appears commit-versioned; "stable API" status and a meaningful version string are therefore inferred from repo state, not stated (the README carries a "version 1.0" badge).
- [未验证] GPU and NPU support status ("GPU available / NPU upcoming") is from README framing; the maturity, performance, and platform coverage of the non-CPU paths are not verified here.
- [推断] Exact supported-model list and required conversion steps shift with the repo; verify a specific model against current `README`/scripts before relying on it.
- [推断] "Fork/derivative of llama.cpp reusing GGUF + CLI" is inferred from the framework's framing and tooling; the precise upstream-sync relationship was not audited.
