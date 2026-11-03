# local-runtimes

> Category node. Consumer-hardware runtimes that run models on your own machine — one user, one box, no scheduler.
> ← back to [llm-inference](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **Memory Offload** | Your model weights exceed VRAM or RAM and you need layer streaming, expert caching, or CPU/GPU execution across memory tiers. | [→](memory-offload/INDEX.md) |

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **llama.cpp** | Use it when you want the upstream dependency-free C/C++ engine that runs on the widest hardware matrix and can be embedded or served locally — accepting no semver, no model management, and a flag-level API. | A (6/6) | [→](llama-cpp.md) |
| **Ollama** | Use it when you want a managed local model store with an OpenAI/Anthropic-compatible API, Docker deployment and client SDKs — accepting a wrapper's flag subset, a 4096-token default context, and no serving-scale batching. | A (5/6) | [→](ollama.md) |
| **Magnitude** | Use it when the machine's capability is unknown and you want a pre-download speed/memory estimate plus one-click wiring into an existing coding harness — accepting a two-month-old single-vendor repo that reports ~6x slower than llama.cpp on Apple Silicon. | B (6/6) | [→](magnitude.md) |
| **omlx** | Use it when you want a Mac (Apple Silicon) local LLM inference server on MLX with SSD-tiered KV caching — a young single-maintainer repo with a suspicious star count. | B (6/6) | [→](omlx.md) |
| **MTPLX** | Use it when you want the model's own MTP heads to exact-speculatively decode Qwen 3.8 at ~2x plain speed on a Mac with an OpenAI/Anthropic server and app — accepting a ~5-month-old, author-dominated repo and an in-product attribution NOTICE. | B (6/6) | [→](mtplx.md) |
| **Shimmy** | Use it when you have GGUF files on disk and want an OpenAI/Ollama/Anthropic-compatible API from one Rust binary with zero runtime dependencies — accepting a one-year-old single-maintainer project whose engine certifies only 26 model+quant combinations. | B (6/6) | [→](shimmy.md) |
| **Airframe** | Use it when you embed GGUF inference in your own Rust program and need a pure-Rust build with one-shader-language GPU coverage (WebGPU) — accepting a six-month-old, single-contributor engine with 12 certified architecture families and a pending-patent subsystem. | C (4/6) | [→](airframe.md) |
| **Claude Code Local** | Use it when Claude Code's usage limit or a no-cloud rule stops you and you want the same `claude` session answered by a local model on an Apple Silicon Mac — accepting a six-month-old single-maintainer repo, one-user-at-a-time serving, and abliterated default models. | B (6/6) | [→](claude-code-local.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [llama.cpp](llama-cpp.md) | ✅ | A (6/6) | The upstream GGUF engine with the widest backend matrix and no runtime dependencies; no semver, no model management, flag-level control. |
| [Ollama](ollama.md) | ✅ | A (5/6) | Managed model store with OpenAI/Anthropic-compatible API, Docker, MLX+llama.cpp runners and the deepest client ecosystem; wrapper flag subset, 4096-token default context. |
| [Magnitude](magnitude.md) | ✅ | B (6/6) | Pre-download hardware-fit estimates plus one-click harness wiring for mixed-GPU fleets; young single-vendor repo, ~6x slower than llama.cpp on Apple Silicon, loopback only. |
| [omlx](omlx.md) | ✅ | B (6/6) | Mac-only MLX server with SSD-tiered KV caching; young, effectively single-maintainer. |
| [MTPLX](mtplx.md) | ✅ | B (6/6) | Mac-only exact MTP speculative decoding for Qwen 3.8; author-dominated, attribution NOTICE, non-Qwen models fall back to AR.
| [Shimmy](shimmy.md) | ✅ | — | Single Rust binary serving OpenAI/Ollama/Anthropic-compatible APIs from a GGUF path, auto-discovering Ollama/HF model dirs; the engine (Airframe) certifies only 26 model+quant combos, and its LICENSE file contradicts its Cargo.toml (Apache-2.0 vs MIT). |
| [Airframe](airframe.md) | ✅ | — | Pure-Rust WebGPU (WGSL) GGUF inference engine — `cargo build` covers NVIDIA/AMD/Intel/Apple Silicon; young, single-contributor, no LICENSE file, and the FSE subsystem carries a pending US patent. |
| [Claude Code Local](claude-code-local.md) | ✅ | — | MLX server that speaks the Anthropic Messages API to Claude Code and repairs local models' tool calls, with a RAM-sized installer and Desktop launchers; Mac-only, single-threaded, one global prompt cache, no speculative decoding. |

## What belongs here

Runtimes whose primary job is **running a model for one user on their own machine** — desktop apps, single-binary servers, and embeddable engines. Not server-class serving engines with batching and autoscaling (see `serving-engines`), not phone/edge runtimes (see `on-device-ml`).

Keep local model management, broad engines, embedding libraries, and KV-cache-only tiering here. For weight streaming or CPU/GPU expert offload as the deciding constraint, enter [Memory Offload](memory-offload/INDEX.md).
