---
name: Google AI Edge Gallery
slug: ai-edge-gallery
repo: https://github.com/google-ai-edge/gallery
category: on-device-ml
tags: [on-device-llm, edge-ai, litert, gemma, android, ios, multimodal, showcase-app, mcp, benchmark, google-ai-edge, kotlin]
language: Kotlin
license: Apache-2.0
maturity: v1.0.16 (2026-06-23), active, ~23.9k stars (2026-06-26); Google-maintained
last_verified: 2026-06-26
type: app
upstream:
  pushed_at: 2026-06-25T14:33:57Z
  default_branch: main
  default_branch_sha: fbf6926169bc0f0f01f168197d325488721089ba
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:48:45Z
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
        last_commit_age_days: 4
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 37.2
        qualifying_issues: 40
        band: relaxed_solo
        window_offset_days: 9
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: null
        canonical_package: null
        release_downloads: 743362
        release_assets: 60
        release_tier: C
        signal_basis: releases
    longevity:
      grade: C
      raw:
        repo_age_days: 540
        last_commit_age_days: 4
        cohort: app
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 12
        top1_share: 0.286
        top3_share: 0.675
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

# Google AI Edge Gallery

A Google-maintained, end-user showcase **app** that runs open LLMs (Gemma-first) fully on-device — chat, Ask Image, Audio Scribe, Prompt Lab, Agent Skills/MCP and a benchmark tool — on Android, iOS and macOS, powered by LiteRT + Google AI Edge. It is a *runnable demo and evaluation harness*, not a library you embed.

![ai-edge-gallery — health radar](../../assets/health/ai-edge-gallery.svg)

## When to use

You're a mobile PM or applied-ML engineer who has been told "we want an on-device LLM feature — figure out if it's actually viable on the phones our users carry." Before you commit engineering weeks to a custom integration, you want to *feel* what a 1–4B model does on real hardware: how fast it decodes, whether Ask Image-style multimodal is good enough, how a "thinking mode" reasoning trace looks, and what happens to latency and battery on a mid-tier Android device versus your test iPhone. You don't want to build any of that plumbing yet — you want to put a working app in a stakeholder's hand this afternoon.

So you install Google AI Edge Gallery from the Play Store / App Store (or sideload the APK / build it from source), download a Gemma model from the bundled Hugging Face LiteRT Community list, and start poking: run Prompt Lab to sweep temperature/top-k, try Audio Scribe for on-device transcription, wire an Agent Skill through MCP to call a tool, and read the Benchmark numbers (tokens/sec, time-to-first-token) straight off the device. It's the fastest way to *de-risk the decision* and capture concrete latency/quality evidence — and because the same LiteRT runtime underlies the production SDKs, what you observe here roughly predicts what a real integration would feel like.

## When NOT to use

- **It is not an SDK or library — you cannot `import` it.** If you need to embed on-device inference into *your* app, this is the showcase, not the dependency. Reach for [LiteRT-LM](litert-lm.md) (the C++/Kotlin runtime layer) or the MediaPipe LLM Inference API instead; the Gallery is the demo that sits on top of those.
- **Not a model or a runtime you ship.** It's an application binary (Kotlin/Gradle, Apache-2.0). You don't get a reusable inference engine out of it — copying its UI is rebuilding an app, not adopting a library.
- **Heavily Gemma-centric.** The optimized, one-tap catalog is Gemma-family-first; arbitrary Hugging Face architectures or Qwen/Mistral/Phi as first-class citizens are not the design center. For broad model coverage you'd evaluate llama.cpp or MLX.
- **Not for production-grade throughput.** On-device generation on phones is far slower than cloud APIs; multi-minute generations and large contexts are demo-grade, and behavior degrades on memory-constrained devices.
- **Fast-moving, app-store-gated.** It ships on a rapid app cadence (v1.0.11 → v1.0.16 over weeks) and features are explicitly "experimental" (Mobile Actions, Tiny Garden, speculative decoding, NPU/TPU paths); what you benchmark today may move, and platform availability (iOS/macOS) is newer than Android.
- **Closed catalog assumptions.** Models flow through Google's Hugging Face LiteRT Community and LiteRT packaging; importing a truly arbitrary GGUF/ONNX model is not the happy path.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [LiteRT-LM](litert-lm.md) | ✅ | Choose LiteRT-LM when you need the on-device runtime layer shown by the Gallery. | The actual on-device **runtime layer** (C++/Kotlin bindings) the Gallery demos. Choose it to *build* an app; choose the Gallery to *evaluate* before you build. |
| [BitNet](bitnet.md) | ✅ | Choose BitNet when you need a research inference framework for 1-bit/ternary LLMs. | A research **inference framework** for 1-bit/ternary LLMs (extreme CPU efficiency), not a polished demo app — different layer and far narrower model set. |
| [TimesFM](timesfm.md) | ✅ | Choose TimesFM when your task is time-series forecasting, not LLM chat demos. | A time-series **foundation model**, not an LLM chat showcase — adjacent on-device ML but a different task entirely. |
| Ollama | 未收录 | Choose Ollama when you need a desktop/server local-LLM runner with a GGUF catalog and API. | Desktop/server local-LLM runner with a huge GGUF catalog and an API; great on laptops/servers but not a mobile/Android-first on-device showcase. |
| LM Studio | 未收录 | Choose LM Studio when you need a polished desktop GUI for local LLMs. | Polished desktop GUI for running local LLMs (closed-source app); broader model picker, but desktop-only and not mobile on-device. |
| MediaPipe LLM Inference Studio (Google) | 未收录 | Choose MediaPipe LLM Inference Studio when you need the older same-org demo/tooling path. | The older same-org demo/tooling path for on-device LLMs; overlapping intent, superseded in direction by the LiteRT-based Gallery. |

## Tech stack

- **App:** Kotlin (~92% of repo) on Android (Jetpack/Compose-style UI); iOS and macOS builds also shipped.
- **Inference:** LiteRT (the TensorFlow Lite successor) + Google AI Edge on-device APIs; optional GPU and vendor NPU/TPU paths (Qualcomm NPU, Pixel TPU mentioned for specific models).
- **Models:** Gemma family first-class, downloaded from the Hugging Face LiteRT Community; custom litert-lm model import supported.
- **Agent layer:** Model Context Protocol (MCP) tools / modular "Agent Skills"; experimental speculative decoding and Multi-Token Prediction.
- **Build:** Gradle (Android toolchain).

## Dependencies

- **A real device** to be useful: Android 12+, iOS 17+, or macOS; a phone with enough RAM (small-model on-device LLMs commonly want several GB free).
- **A model file** downloaded in-app from the Hugging Face LiteRT Community (network needed once to fetch; inference itself is offline).
- **To build from source:** the Android SDK + Gradle toolchain (see DEVELOPMENT.md); no Bazel needed for the app itself, unlike the underlying runtime.
- **Optional accelerators:** GPU / Qualcomm NPU / Pixel TPU drivers for the hardware-accelerated paths on supported devices.

## Ops difficulty

**Low to consume, N/A to operate.** As an end-user app there's nothing to deploy or run as a service — install from a store or sideload the APK and you're benchmarking in minutes; that's the whole point. "Difficulty" only appears if you (a) build from source, which is a standard Gradle Android build, or (b) try to read it as production architecture — at which point you're really evaluating LiteRT-LM / MediaPipe, where the on-device ops burden (RAM gating, GPU-init/CPU-fallback, KV-cache session limits) actually lives. There is no server, no scaling story, no uptime to maintain.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 14.5 hours across 54 qualifying issues/PRs.
- **Maintenance (as of 2026-06):** last pushed 2026-06, latest release v1.0.16 (2026-06-23) on a very rapid app cadence (v1.0.11 → v1.0.16 over weeks) — **very actively maintained**, but fast enough that features churn release-to-release and several are flagged "experimental."
- **Governance / backing:** organization-owned under `google-ai-edge` and **Google-maintained** — strong backing and resourcing for the underlying LiteRT stack. [推断] Caveat: Google has a track record of sunsetting consumer-facing demo apps, so the *showcase* may be deprioritized even if the runtime endures; this is a showcase on top of the SDKs, not the SDK itself.
- **Age & Lindy verdict (created 2025-03, ~1 yr):** young and riding the on-device-LLM wave — **Lindy-unproven** as a standalone app. But its purpose (de-risk an on-device decision *now*) doesn't require longevity, and it sits on the more durable LiteRT/Google AI Edge runtime, which is the part worth betting on long-term.
- **Risk flags:** app-store-gated distribution and a Gemma-centric, closed-ish catalog (models via Google's Hugging Face LiteRT Community); experimental features may change or be removed. Apache-2.0, no relicense/open-core concern. [推断]

## Caveats (unverified)

- [未验证] Star count ~23.9k is from the GitHub API on 2026-06-26; GitHub stars are unreliable and drift continuously — treat as indicative only.
- [未验证] Latest release 1.0.16 dated 2026-06-23 per the GitHub API; a scraped releases page rendered the year as "2024" — the API date is taken as authoritative, but exact per-version dates were not all cross-checked.
- [未验证] iOS 17+ and macOS support are stated in the README; their maturity relative to the Android build (originally Android-only) is not independently confirmed and may lag.
- [推断] "Gemma 4 family" and the Gemma-centric optimized catalog reflect README framing; the precise list of first-class vs nominally-supported models shifts release-to-release.
- [未验证] On-device throughput, RAM requirements and battery impact vary widely by device/model/quantization; no first-party per-device numbers were verified here.
- [推断] Experimental features (Mobile Actions, Tiny Garden, speculative decoding, NPU/TPU execution, MCP) are labeled experimental and may change or be removed across the fast app cadence.
