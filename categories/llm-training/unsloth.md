---
name: Unsloth
slug: unsloth
repo: https://github.com/unslothai/unsloth
category: llm-training
tags: [fine-tuning, lora, qlora, triton-kernels, quantization, grpo, single-gpu, vram-efficient]
language: Python
license: Apache-2.0
maturity: "Beta releases (v0.1.x-beta line, 2026-06); very active"
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T11:05:14Z
  default_branch: main
  default_branch_sha: 2f8521ed54b20775025ce28bc9965e97d76318b3
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:33:21Z
  overall: B
  overall_score: 3.4
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: unsloth
        dependent_repos_count: 0
        downloads_last_month: 1019573
        graph_tier: E
        volume_tier: B
        cross_check_divergence: null
        homebrew_installs_90d: 274
        homebrew_tier: C
        release_downloads: 1830603
        release_assets: 140
        release_tier: B
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1028
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 55
        top1_share: 0.481
        top3_share: 0.665
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
---

# Unsloth

Drop-in fine-tuning library that rewrites the hot paths of LoRA/QLoRA/RL training with hand-written Triton kernels to train open LLMs ~2x faster with large VRAM savings on a single GPU.

![unsloth — health radar](../../assets/health/unsloth.svg)

## When to use

You're a developer or solo researcher with a single consumer or workstation GPU (e.g. an RTX 4090, or a free Colab/Kaggle T4) and you want to fine-tune a Llama, Qwen, Mistral, Gemma or gpt-oss model on your own dataset. With stock Hugging Face + PEFT you keep hitting CUDA out-of-memory on QLoRA runs, or a single epoch takes long enough that iteration is painful. Unsloth swaps in its own Triton kernels (RoPE, MLP, attention, padding-free packing) and dynamic 4-bit quantization behind a near drop-in `FastLanguageModel` API, so the same QLoRA job fits in far less VRAM and finishes roughly 2x faster — the vendor cites "up to 2x faster with up to 70% less VRAM," and "80% less VRAM for GRPO" reinforcement-learning runs.

It shines when your constraint is one GPU and your goal is fast, cheap iteration: instruction tuning, domain adaptation, or RL (GRPO/DPO) of reasoning models that the docs claim can run in as little as ~5GB VRAM. Because it sits on top of `transformers`/`trl`, your training script, datasets and exported adapters stay in the familiar Hugging Face ecosystem, and you can export to GGUF/safetensors for downstream inference.

## When NOT to use

- **Multi-GPU / multi-node distributed training.** The open-source core is widely reported to be single-GPU only; multi-GPU scaling is gated behind paid Pro/Enterprise tiers [未验证]. Note the project's own README/site also advertises "Multi-GPU training support" — these claims conflict, so verify against the exact version you install before assuming distributed training works in the free package. If you need FSDP2/DeepSpeed-style sharding today, Axolotl or LLaMA-Factory are safer.
- **Full-parameter fine-tuning of large models.** Unsloth's sweet spot is parameter-efficient (LoRA/QLoRA) tuning that fits one GPU; large-scale full fine-tunes that need sharding fall outside the free single-GPU envelope.
- **Unsupported architectures.** It supports a large but curated model list; a brand-new or exotic architecture may not have optimized kernels until the maintainers add it.
- **Vendor-tier lock-in concerns.** Headline performance numbers (e.g. very high speed/VRAM multipliers) and multi-GPU are tied to commercial tiers; budget for that before committing to a production pipeline.
- **You want a fully config-driven, reproducible team workflow.** Unsloth is library/notebook-first; LLaMA-Factory (YAML + LlamaBoard UI) is more team/repro oriented.
- **Maintenance cadence risk.** It tracks fast-moving model releases on a frequent beta cadence; pin versions, because kernel/model support and APIs shift quickly.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [LLaMA-Factory](llamafactory.md) | ✅ | Choose LLaMA-Factory when broad method/model coverage, YAML, web UI, and multi-GPU matter more than single-GPU speed. | It can use Unsloth as a backend; Unsloth stays narrower but faster on one GPU. |
| [ART](art.md) | ✅ | Choose ART when the training problem is multi-step agent GRPO with tasks, rewards, and rollout orchestration. | ART is agent-first; Unsloth is a general fine-tuning/RL acceleration layer. |
| [Agent Lightning](agent-lightning.md) | ✅ | Choose Agent Lightning when existing agents need RL from execution traces with minimal code changes. | It decouples agent execution from training; Unsloth optimizes kernels rather than agent orchestration. |
| [Axolotl](axolotl.md) | ✅ | Choose Axolotl when first-class multi-GPU FSDP/DeepSpeed and multimodal support matter after outgrowing one GPU. | Stronger for scale-out workflows; Unsloth wins on single-GPU speed and VRAM. |
| [torchtune](torchtune.md) | ✅ | Choose torchtune when native PyTorch recipes with explicit `torch.compile` control are the priority. | More explicit and lower-level, but with narrower model coverage than Unsloth's curated fast path. |
| HF TRL | 未收录 | Choose HF TRL when Hugging Face reference SFT/DPO/GRPO trainers are preferable to an accelerated wrapper. | Unsloth builds on TRL and accelerates it with custom kernels. |

## Tech stack

- **Language:** Python (with a TypeScript Studio UI component).
- **Core acceleration:** hand-written Triton kernels (RoPE, MLP, attention), padding-free packing, dynamic 4-bit quantization; FP8/16-bit/4-bit training paths.
- **Training methods:** LoRA, QLoRA, full fine-tune, and RL (GRPO/DPO) via a near drop-in `FastLanguageModel` API layered over `transformers`/`trl`.
- **Export/inference:** GGUF, LoRA adapters, safetensors; integrates with llama.cpp for inference.
- **Surfaces:** code library (Unsloth Core, Apache-2.0) plus an optional no-code web UI (Unsloth Studio, AGPL-3.0 components) [未验证 on exact licensing split].

## Dependencies

- PyTorch + CUDA (NVIDIA GPU; RTX 30/40/50, Blackwell, DGX cited; macOS and Intel/AMD support reported as expanding) [未验证].
- Triton (kernel compilation).
- Hugging Face `transformers`, `peft`, `trl`, `datasets`, and tokenizers.
- bitsandbytes-style 4-bit quantization stack (Unsloth ships its own dynamic 4-bit variants).
- llama.cpp for GGUF export/inference.

## Ops difficulty

**Low to medium.** For the intended path — one GPU, a Colab/Kaggle/notebook or a single script — it's low: install, swap to `FastLanguageModel`, train. Difficulty rises to medium when you fight CUDA/Triton/PyTorch version matrices on bespoke hardware, or when you try to push past the single-GPU free-tier ceiling (multi-GPU/full fine-tune), where the open-source story is contested and you may need a paid tier.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance — active (as of 2026-06).** Last repo push 2026-06; ships on a fast beta cadence tracking new model releases. Active, not coasting [未验证]. The flip side is churn: kernel/model support and APIs shift quickly, so pin versions.
- **Governance & backing.** Org-owned (`unslothai/`) — a small VC-funded startup with a commercial Pro/Enterprise tier, not a foundation [推断]. The open-source single-GPU core and the gated multi-GPU/headline-perf tiers share one roadmap controlled by the vendor; viability tracks the company's runway, and the free-vs-paid line can move.
- **Age & Lindy verdict — young but fast-proving (created 2023-11, ~2.5y).** Too young for a strong Lindy prior, but ~67k stars (2026-06) and heavy ecosystem use mean it has cleared the "is anyone using this" bar; treat as an established-but-still-young bet, not a decade-stable one [推断].
- **Risk flags.** Open-core: the most-cited capabilities (multi-GPU, top perf multipliers) are tied to commercial tiers, and the OSS-multi-GPU claim is contested (see Caveats). Mixed licensing — Apache-2.0 core with AGPL-3.0 Studio components [未验证]. Budget for the paid tier before betting a production pipeline on it.

## Caveats (unverified)

- [未验证] Specific speed/VRAM multipliers ("2x faster," "70% less VRAM," "80% less VRAM for GRPO," "~5GB GRPO") are vendor claims; real gains depend on model, sequence length, batch size and GPU. LLM-related performance claims are not guaranteed.
- [未验证] Whether multi-GPU training works in the free Apache-2.0 package is contested: the repo/site advertises multi-GPU, while multiple third-party comparisons state OSS is single-GPU only and gate multi-GPU behind Pro/Enterprise. Verify on your installed version.
- [未验证] Star count cited around 67k (2026-06) from the GitHub page; star counts in this ecosystem are unreliable — treat as indicative only.
- [未验证] Exact supported-model count ("500+") and per-architecture kernel coverage vary by release; check the current docs.
- [未验证] Pricing figures for Pro/Enterprise seen in third-party sources are inconsistent; confirm on the official pricing page.
