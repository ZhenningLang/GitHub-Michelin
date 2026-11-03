# memory-offload

> Category node. Local inference when model weights exceed VRAM or RAM: layer streaming, expert caches, and CPU/GPU execution across memory tiers.
> Back to [local-runtimes](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Strata** | Run a supported oversized Qwen or DeepSeek model on a personal workstation with CPU/GPU expert execution and guided setup; accept large RAM/SSD needs and a 40-day, author-dominated history. | B (5/6) | [→](strata.md) |
| **AirLLM** | Use it when a model will not fit your card in the form you need and wall-clock time is free — a library that streams the checkpoint off disk one layer at a time so VRAM costs one layer, at seconds-to-minutes per token. | B (6/6) | [→](airllm.md) |
| **FreeToken** | Use it when one NVIDIA desktop must serve a Mixture-of-Experts model bigger than its VRAM to your coding agent — experts live in host RAM with a GPU cache — accepting a ~2-month-old, Linux-plus-NVIDIA-only v0.1.x engine with no API auth. | B (6/6) | [→](freetoken.md) |
| **DwarfStar (ds4)** | Use it when you own a 96 GB+ Mac, a DGX Spark or a Strix Halo box and want one of a few frontier MoE models (DeepSeek V4, GLM 5.x, Qwen3.8) driving your coding agent locally, spilling to SSD when RAM runs out — accepting a five-month-old, single-maintainer, release-less engine that loads only its own GGUF files. | B (6/6) | [→](ds4.md) |
| **Edge0** | Use it when you want a 35B-class MoE model on a 16–24 GB Mac (or a phone) and memory, not model choice, is the constraint — experts stream from the SSD with a trained one-step-ahead predictor — accepting exactly two preview models, a small accuracy loss versus fp16, and a one-month-old, release-less repo. | C (6/6) | [→](edge0.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Strata](strata.md) | indexed | B (5/6) | Curated model-specific memory tiers, desktop/Terminal and compatible coding APIs; narrow model packs, hardware-dependent fit, large storage and very young governance. |
| [AirLLM](airllm.md) | ✅ | B (6/6) | Layer-streaming library that runs a 70B/671B-class model on a 4–12GB card by keeping one layer on the device; the price is a disk read per token (users report 28.6 s/token on a 3B) and a compression option that measures slower, not faster. |
| [FreeToken](freetoken.md) | ✅ | B (6/6) | Serves frontier MoE checkpoints (safetensors) on one consumer NVIDIA card by keeping experts in host RAM and auto-sizing a GPU expert cache, with OpenAI/Anthropic APIs and `ft launch` for coding agents; Linux+NVIDIA only, needs RAM ≈ expert weights, v0.1.x format churn, no HTTP auth. |
| [DwarfStar (ds4)](ds4.md) | ✅ | B (6/6) | Narrow C engine hand-fitted to a few frontier MoE models on Metal, CUDA and ROCm, with 2-bit expert quantization, SSD streaming for models larger than RAM, two-machine RDMA tensor parallelism and OpenAI/Anthropic APIs; loads only its own GGUFs, no releases, single maintainer, no API auth. |
| [Edge0](edge0.md) | ✅ | C (6/6) | Streams MoE experts from SSD with trained prerouter heads plus Recover-LoRA, so a 35B tier runs in ~3 GiB peak active memory on Apple Silicon, with iOS/Android/macOS/Windows apps; only its own two preview checkpoints, macOS-only Python framework, exact mlx pins, single-slot server with no auth. |

## What belongs here

Local runtimes whose deciding constraint is **fitting model weights beyond one memory tier**, through weight streaming or CPU/GPU expert offload. This is not a promise of low host-RAM use: FreeToken keeps all experts in host RAM, while AirLLM also streams dense models. KV-cache-only tiering and broad local model management stay in [local-runtimes](../INDEX.md).
