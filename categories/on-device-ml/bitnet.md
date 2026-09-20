---
name: BitNet
slug: bitnet
repo: https://github.com/microsoft/BitNet
category: on-device-ml
tags: [1-bit-llm, ternary, cpu-inference, quantization, llama-cpp, edge-ai, bitnet-b1.58, microsoft]
language: Python (tooling) + C++ kernels
license: MIT
maturity: No tagged releases; commit-versioned, last push 2026-03-10; created 2024-08; Microsoft-maintained (as of 2026-06-26)
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-03-10T07:49:47Z
  default_branch: main
  default_branch_sha: 01eb415772c342d9f20dc42772f1583ae1e5b102
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T14:53:27Z
  overall: C
  overall_score: 2.17
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 115
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 98.8
        qualifying_issues: 7
        band: default
        window_offset_days: 11
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
        repo_age_days: 697
        last_commit_age_days: 115
        cohort: framework
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.857
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
---

# BitNet

Microsoft's official inference framework (`bitnet.cpp`) for **1-bit / 1.58-bit (ternary)** LLMs — a fork-of-llama.cpp runtime with custom CPU kernels (I2_S / TL1 / TL2) that runs ternary models like BitNet-b1.58-2B-4T fast and low-energy on x86 and ARM CPUs. Inference only; no training.

![bitnet — health radar](../../assets/health/bitnet.svg)

## When to use

You're building a local assistant feature into a desktop app that has to ship to ordinary laptops — some Intel/AMD x86, some ARM (Apple silicon, a few Windows-on-ARM machines), often with no usable GPU and only 4–8GB of free RAM. You've already decided you don't want a cloud round-trip: the data is sensitive, you want it to work offline, and you don't want a per-call API bill scaling with your user count. A normal 7B GGUF model in 4-bit still feels heavy on a low-end CPU, and energy/battery cost matters because users complain when a background feature spins the fans.

So you reach for BitNet. You pick a **ternary** model that was actually trained 1.58-bit — BitNet-b1.58-2B-4T is the official one, with community ports like Falcon3 and a Llama3-8B-1.58 — convert it with the repo's setup script, and let `bitnet.cpp`'s I2_S/TL1/TL2 kernels run it. Because the weights are ternary, the matmuls become lookup/add-heavy work that the custom kernels exploit, so on CPU you get a reported multi-x speedup and large energy reduction versus a standard quantized baseline, and a small model fits comfortably in your RAM budget. The framework is a thin llama.cpp derivative, so the `llama-cli`-style runtime and GGUF tooling feel familiar.

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

- **Build toolchain:** Python ≥ 3.9, CMake ≥ 3.22, **Clang/LLVM ≥ 18** (a relatively new compiler — a common install snag); Conda recommended.
- **Models:** a *ternary* model in supported format — BitNet-b1.58-2B-4T (official) or community ports (Falcon3 1B–10B, Falcon-E, Llama3-8B-1.58, bitnet_b1_58-large/3B), pulled via the Hugging Face CLI and converted by the repo scripts.
- **Hardware:** an x86 or ARM CPU; no GPU required for the CPU path. RAM scales with model size (a 2–3B ternary model is small, but still needs a few GB).
- **No package install** — you build from source; there is no `pip install bitnet` runtime package for the engine.

## Ops difficulty

**Medium.** There's no pip-installable engine: you clone, set up a Conda env, install **Clang ≥ 18** and CMake ≥ 3.22 (the Clang version requirement and platform-specific kernel selection — TL1 on ARM vs TL2 on x86 vs I2_S — are the usual friction points), then run a setup script to convert/quantize the model and build with CMake. Once built, day-to-day inference via the CLI is straightforward and the small models are easy on resources. The bigger operational risks are *project* risks, not runtime ones: no tagged releases (pin a commit), a small/curated model list, and GPU/NPU paths that are still maturing — so treat upgrades and platform expansion as a moving target.

## Health & viability

- **Responsiveness**: Grade B — median first-response time 98.8 hours across 7 qualifying issues/PRs.
- **Maintenance (2026-06):** last push 2026-03-10 — roughly 3 months idle at verification, so the runtime reads as **coasting**, not actively iterated week-to-week. [推断] No tagged releases means cadence is judged from commit recency, not a release stream.
- **Governance / backing:** Microsoft-owned (`microsoft/BitNet`, Organization). [推断] That removes single-maintainer bus-factor risk, but Microsoft is also a serial project-archiver — vendor backing here signals "research reference implementation kept alive," not a productized, SLA-backed SDK.
- **Age & Lindy (created 2024-08, ~2yr):** young and still-active enough to not fail Lindy, but too new to be a proven long-lived bet. [推断] The value rides on the BitNet-b1.58 research line continuing; treat it as **promising-but-unproven** infrastructure.
- **Adoption:** ~39k stars (volatile, see Caveats) is strong attention, but the curated ternary-model list and CPU-first scope keep real production adoption narrow. [未验证]
- **Risk flags:** MIT-licensed (no relicense risk). The live flags are commit-versioning churn (pin a commit), a small supported-model surface, and GPU/NPU paths still maturing. [推断]

## Caveats (unverified)

- [未验证] Speedup and energy figures (ARM ~1.37–5.07x / ~55–70% energy; x86 ~2.37–6.17x / ~72–82% energy; "+1.15–2.1x" from later kernels; 100B model at "5–7 tok/s on a single CPU") are the project's own README claims against unspecified baselines — not independently reproduced here; vary by CPU, model, and kernel.
- [未验证] Star count ~39.5k and fork count ~3.6k (GitHub API, 2026-06-26) — GitHub stars are unreliable and date-sensitive; treat as indicative only.
- [推断] No GitHub releases/tags were returned (2026-06-26), so the project appears commit-versioned; "stable API" status and a meaningful version string are therefore inferred from repo state, not stated.
- [未验证] GPU and NPU support status ("GPU available / NPU upcoming") is from README framing; the maturity, performance, and platform coverage of the non-CPU paths are not verified here.
- [推断] Exact supported-model list and required conversion steps shift with the repo; verify a specific model against current `README`/scripts before relying on it.
- [推断] "Fork/derivative of llama.cpp reusing GGUF + CLI" is inferred from the framework's framing and tooling; the precise upstream-sync relationship was not audited.
