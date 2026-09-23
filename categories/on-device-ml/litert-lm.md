---
name: LiteRT-LM
slug: litert-lm
repo: https://github.com/google-ai-edge/LiteRT-LM
category: on-device-ml
tags: [on-device-llm, edge-ai, litert, gemma, mobile-inference, npu, gpu-acceleration, android, ios, cross-platform, google-ai-edge, quantization]
language: C++ core; bindings Python/Kotlin/C++ stable, Swift/JS preview
license: Apache-2.0
maturity: Pre-1.0, fast cadence; stable v0.13.1 (2026-06-03), v0.14.0-alpha (2026-06-18); Google-maintained
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T08:21:44Z
  default_branch: main
  default_branch_sha: 645fcac1d5b47d1077edb01bc8f104e04c1ae6dc
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:49:11Z
  overall: B
  overall_score: 3.33
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
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 15.8
        qualifying_issues: 48
        band: relaxed_solo
        window_offset_days: 10
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: litert-lm-builder
        dependent_repos_count: 0
        downloads_last_month: 136497
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
        release_downloads: 90741
        release_assets: 133
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 526
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 40
        top1_share: 0.291
        top3_share: 0.522
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# LiteRT-LM

Google's C++ orchestration/runtime layer on top of LiteRT (the TensorFlow Lite successor) for running LLMs fully **on-device** — Gemma first-class (Llama/Phi/Qwen nominally supported but less optimized) on Android, iOS, desktop and edge hardware via CPU/GPU/NPU. Python/Kotlin/C++ bindings are marked *Stable* by Google, but the project itself is pre-1.0 — expect breaking changes; Swift/JS are preview.

![litert-lm — health radar](../../assets/health/litert-lm.svg)

## When to use

You're a mobile engineer at a small startup shipping a private journaling app, and Android is your lead platform. Your product promise is that a user's notes never leave their phone, so the "summarize my week" and "pull out action items" features you've been asked to build can't call a cloud LLM — that would break the privacy story, and at your scale the per-call API bill for every summary would quietly bleed the runway. You need the model to run locally, work on a plane with no signal, and slot into your existing Kotlin codebase without you hand-rolling a C++ inference engine.

So you reach for LiteRT-LM. You package a **Gemma** model into the `.litertlm` format, wire it in through the stable Kotlin bindings, and let the runtime drive CPU with optional GPU/NPU acceleration on-device. The tasks you actually need — summarization and structured extraction — sit squarely in the short, structured workloads a small model handles well, and because you've standardized on Gemma you're in the runtime's sweet spot, with third-party iPhone benchmarks suggesting Gemma-class latency holds up if you later add an iOS build. You accept the tradeoff of living inside Google's tooling and a Bazel-based build in exchange for one Google-maintained runtime instead of stitching together community glue across platforms.

## When NOT to use

- **Not a general-purpose multi-model runtime** — the optimized `.litertlm` catalog is heavily Gemma-centric. For arbitrary Hugging Face models, exotic architectures, or Qwen/Mistral as first-class citizens, llama.cpp or MLX support far more models with less friction.
- **Not for cloud-grade throughput / low latency** — `[未验证]` on-device inference is reported 10–100× slower than cloud APIs (third-party benchmark, not official); synchronous/interactive flows (multi-minute generations) are unusable without architectural workarounds.
- **Risky on memory-constrained devices** — 2–4B models commonly need 6–8GB RAM and Android may kill the process under memory pressure; the KV cache fills after a few turns and degrades output, forcing session rotation.
- **Not for a frozen, stable API** — pre-1.0 with a fast release cadence `[推断]` (e.g. v0.13.1 → v0.14.0-alpha within ~2 weeks); several bindings are preview (Swift, JS/Web) or community (Flutter), implying ongoing churn.
- **Ecosystem / format lock-in** — models must be packaged into Google's `.litertlm` format and largely sourced from Google's HF community; you also inherit a Bazel-based C++ build.
- **Not for large-model / high-accuracy results** — this is a small-model edge runtime; teams report needing heavy defensive engineering (output parsing, language-drift mitigation, device gating) for reliable behavior.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [llama.cpp](../llm-inference/local-runtimes/llama-cpp.md) | ✅ | Choose llama.cpp when you need broad GGUF model/quantization support and ubiquitous reach. | Far broader model/quantization support (GGUF ecosystem) and ubiquitous reach, but more cross-platform build complexity and no single Google-blessed mobile SDK — you assemble more glue. |
| [MLX / mlx-lm (Apple)](mlx-mlx-lm.md) | ✅ | Choose MLX when Apple-silicon speed and clean Swift/Python ergonomics matter most. | Faster than LiteRT-LM on many non-Gemma models with clean Swift/Python ergonomics on Apple silicon, but Apple-only — can't be your cross-platform answer. |
| MediaPipe LLM Inference API (Google) | 未收录 | Choose MediaPipe LLM Inference API when you want an easier same-org drop-in layer. | Higher-level, easier drop-in on-device LLM from the same org using `.task` models, but less of a low-level orchestration layer and overlapping/superseded by LiteRT-LM in direction — the simpler-but-less-flexible sibling. |
| ONNX Runtime (+ GenAI / Mobile) | 未收录 | Choose ONNX Runtime when you need vendor-neutral format/backend breadth. | Vendor-neutral, mature, many formats and backends across ecosystems, but heavier, less tuned for the latest small mobile LLMs, and lacks LiteRT-LM's Gemma-specific mobile quantization wins. |
| Apple Core ML / Foundation Models | 未收录 | Choose Apple's stack when Apple Neural Engine integration and OS models are the hard requirement. | Best Apple Neural Engine integration and OS-level models on newer iPhones, but Apple-locked, conversion can be painful, no path to Android or generic edge hardware. |

## Tech stack

- C++ core runtime; LiteRT (TensorFlow Lite successor) inference engine
- Bazel build system; CMake; Cargo/Rust tooling
- Python bindings; Kotlin/JNI (Android); Swift/Metal (iOS/macOS, preview); JavaScript/WebAssembly (Web, preview)
- `.litertlm` packaged model format

## Dependencies

- **Bazel** + a pinned `.bazelversion` to build from source (heavy C++ toolchain)
- **LiteRT runtime**
- **Models in `.litertlm` format** from the LiteRT Community on Hugging Face / Kaggle
- **Per-platform native toolchains** — Android NDK, Xcode (iOS/macOS), Emscripten (Web)
- **GPU/NPU vendor drivers** for accelerated backends (NPU support is platform-limited / partly preview)

## Ops difficulty

**High.** Building from source uses Bazel with a pinned version and a large C++/Rust toolchain — non-trivial vs pip-installing a wrapper. Beyond the build, on-device LLM ops are inherently hard: device-tier RAM gating (2–4B models often need 6–8GB RAM or Android kills the process), GPU-init-then-CPU-fallback logic (GPU availability is inconsistent across devices), KV-cache session rotation every few turns `[未验证]` to stop quality decay, and defensive output parsing because small models emit malformed JSON / wrong-language text. Models must be converted/packaged to `.litertlm`. Several bindings (Swift, JS, Flutter) are preview/community, so API churn and gaps are likely pre-1.0.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 61.3 hours across 36 qualifying issues/PRs.
- **Maintenance (2026-06):** last push 2026-06 with a fast release cadence (stable v0.13.1 → v0.14.0-alpha within ~2 weeks) — clearly **active**, but pre-1.0, so churn is the cost of that activity. [推断]
- **Governance / backing:** Google-maintained under `google-ai-edge` (Organization), part of the LiteRT / TensorFlow Lite lineage. [推断] Removes single-maintainer bus-factor risk, but Google is a notorious project-killer (cf. the MediaPipe→LiteRT-LM repositioning) — directional continuity of the *runtime* is safer than any one binding or format surviving.
- **Age & Lindy (created 2025-04, ~1yr):** young and hyped; the Lindy prior is weak — it has not yet proven multi-year survival. Bet on it for the Google/LiteRT backing and Gemma path, not for longevity track record. [推断]
- **Adoption:** ~5k stars (volatile, see Caveats); the Gemma-centric `.litertlm` catalog and pre-1.0 bindings (Swift/JS/Flutter preview) keep the production-ready surface narrow. [未验证]
- **Risk flags:** Apache-2.0 (no relicense risk). Live flags are pre-1.0 API churn and `.litertlm` format + Google-ecosystem lock-in. [推断]

## Caveats (unverified)

- **Counts** — stars/forks/issues (5,703 / 596 / 383) are from the GitHub API on 2026-06-26 and drift continuously; an earlier snippet reported only ~3,157 stars, so sources disagree. `[未验证]`
- **Throughput** — e.g. "Gemma-class E2B at 55.4 tok/s beating MLX 47.5 and llama.cpp 37.8 on iPhone" is a third-party dev.to benchmark, not official; varies by device/model/quantization. `[未验证]`
- **RAM figures** — ~1.5–8GB per model, ~3.66GB file, ~0.8GB text-only weights — aggregated from blogs and HF model cards, not verified against official specs. `[未验证]`
- **Catalog breadth** — "Gemma-only optimization" is third-party commentary; the README lists Llama/Phi-4/Qwen as supported, so nominal vs actually-available optimized `.litertlm` assets is unconfirmed. `[未验证]`
- **MediaPipe relationship** — the superseding/positioning vs the older MediaPipe LLM Inference API is inferred, not stated in the official overview. `[未验证]`
- **NPU availability specifics** — from docs summaries; may differ from the current release matrix. `[未验证]`
- **Build difficulty** — inferred from repo config (`.bazelrc`, `.bazelversion`, CMake, Cargo), not a measured build. `[推断]`
