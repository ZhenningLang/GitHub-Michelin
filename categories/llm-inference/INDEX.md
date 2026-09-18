# llm-inference

> Category node. High-performance LLM/model inference & serving engines, and AI systems languages.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Modular Platform (MAX + Mojo)** | Use it when you want a high-performance GPU/CPU inference platform (MAX) plus the Mojo systems language — accepting single-vendor lock-in and partly non-production licensing. | B (5/6) | [→](modular.md) |
| **omlx** | Use it when you want a Mac (Apple Silicon) local LLM inference server on MLX with SSD-tiered KV caching — a young single-maintainer repo with a suspicious star count. | B (5/6) | [→](omlx.md) |
| **MTPLX** | Use it when you want the model's own MTP heads to exact-speculatively decode Qwen 3.8 at ~2x plain speed on a Mac with an OpenAI/Anthropic server and app — accepting a ~5-month-old, author-dominated repo and an in-product attribution NOTICE. | B (6/6) | [→](mtplx.md) |
| **TensorRT-LLM** | Use it when you need maximum LLM inference throughput on NVIDIA GPUs and are willing to accept NVIDIA-only lock-in, complex build/engine-compile workflow, and closed-source kernels. | — | [→](tensorrt-llm.md) |
| **vLLM** | Use it when you want the de-facto open-source LLM serving engine with PagedAttention, continuous batching, and an OpenAI-compatible API — accepting NVIDIA-centric GPU ops and a fast-moving codebase. | — | [→](vllm.md) |
| **SGLang** | Use it when you need a fast LLM serving engine with RadixAttention prefix caching and structured generation — ideal for tool-using agents and JSON-mode APIs — accepting a younger, smaller ecosystem than vLLM. | — | [→](sglang.md) |
| **Ray Serve** | Use it when you need a general-purpose, scalable Python model-serving framework with multi-model composition and autoscaling — but accept Ray's operational complexity and learning curve. | — | [→](ray-serve.md) |
| **llama.cpp** | LLM inference in C/C++ | ? (0/6) | [→](llama-cpp.md) |
| **Ollama** | Get up and running with Kimi-K2.6, GLM-5.1, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models. | ? (0/6) | [→](ollama.md) |
| **BentoML** | The easiest way to serve AI apps and models - Build Model Inference APIs, Job queues, LLM apps, Multi-model pipelines, and more! | ? (0/6) | [→](bentoml.md) |
| **LMDeploy** | LMDeploy is a toolkit for compressing, deploying, and serving LLMs. | ? (0/6) | [→](lmdeploy.md) |
| **Text Generation Inference (TGI)** | Large Language Model Text Generation Inference | ? (0/6) | [→](text-generation-inference.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [TensorRT-LLM](tensorrt-llm.md) | ✅ | — | Use it when you need maximum LLM inference throughput on NVIDIA GPUs and are willing to accept NVIDIA-only lock-in, complex build/engine-compile workflow, and closed-source kernels. |
| [Modular Platform (MAX + Mojo)](modular.md) | ✅ | B (5/6) | Use it when you want a high-performance GPU/CPU inference platform (MAX) plus the Mojo systems language — accepting single-vendor lock-in and partly non-production licensing. |
| [omlx](omlx.md) | ✅ | B (5/6) | Use it when you want a Mac (Apple Silicon) local LLM inference server on MLX with SSD-tiered KV caching — a young single-maintainer repo with a suspicious star count. |
| [MTPLX](mtplx.md) | ✅ | B (6/6) | Mac-native exact MTP speculative decode for Qwen 3.8 (~2x plain decode, author-measured); young, author-dominant, attribution NOTICE in license; non-Qwen models fall back to AR-only. |
| [vLLM](vllm.md) | ✅ | — | The de-facto open-source LLM serving engine (PagedAttention, continuous batching), huge community and model coverage; NVIDIA-first, fast-moving codebase. |
| [SGLang](sglang.md) | ✅ | — | Fast LLM serving engine with RadixAttention prefix caching and structured generation; younger ecosystem than vLLM, ideal for tool-using agents. |
| [Ray Serve](ray-serve.md) | ✅ | — | General-purpose scalable Python model-serving framework with multi-model composition and autoscaling; built on Ray, operationally demanding. |
| TGI / BentoML | 未收录 | — | Other LLM inference/serving engines named across the pages. |

## What belongs here

Engines and systems languages whose primary job is **high-performance LLM/model inference and serving**. Not on-device/edge runtimes (see `on-device-ml`), not LLM fine-tuning (see `llm-training`).
