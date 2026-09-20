# serving-engines

> Category node. Server-class LLM serving engines and model-serving frameworks — built for GPUs, concurrent requests, and an API boundary.
> ← back to [llm-inference](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **vLLM** | Use it when you want the de-facto open-source LLM serving engine with PagedAttention, continuous batching, and an OpenAI-compatible API — accepting NVIDIA-centric GPU ops and a fast-moving codebase. | A (5/6) | [→](vllm.md) |
| **SGLang** | Use it when you need a fast LLM serving engine with RadixAttention prefix caching and structured generation — ideal for tool-using agents and JSON-mode APIs — accepting a younger, smaller ecosystem than vLLM. | A (5/6) | [→](sglang.md) |
| **TensorRT-LLM** | Use it when you need maximum LLM inference throughput on NVIDIA GPUs and are willing to accept NVIDIA-only lock-in, complex build/engine-compile workflow, and closed-source kernels. | B (4/6) | [→](tensorrt-llm.md) |
| **LMDeploy** | Use it when you want a toolkit that compresses, deploys and serves LLMs with an OpenAI-compatible server — accepting a smaller community and a China-origin ecosystem whose docs are partly Chinese-only. | A (6/6) | [→](lmdeploy.md) |
| **Text Generation Inference (TGI)** | Use it only as a pattern source or for an existing pinned deployment, because the repository is archived — for maintained serving pick vLLM or SGLang, and for local use pick llama.cpp or Ollama. | C (6/6) | [→](text-generation-inference.md) |
| **Ray Serve** | Use it when you need a general-purpose, scalable Python model-serving framework with multi-model composition and autoscaling — but accept Ray's operational complexity and learning curve. | A (6/6) | [→](ray-serve.md) |
| **BentoML** | Use it when you want to package a model plus its preprocessing into a deployable inference API with multi-model pipelines — accepting a heavier framework than a bare serving engine. | B (6/6) | [→](bentoml.md) |
| **Modular Platform (MAX + Mojo)** | Use it when you want a high-performance GPU/CPU inference platform (MAX) plus the Mojo systems language — accepting single-vendor lock-in and partly non-production licensing. | B (5/6) | [→](modular.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [vLLM](vllm.md) | ✅ | A (5/6) | The de-facto open-source serving engine (PagedAttention, continuous batching); NVIDIA-first, fast-moving, operationally heavier than a local runtime. |
| [SGLang](sglang.md) | ✅ | A (5/6) | RadixAttention prefix caching and structured generation for tool-using agents; younger ecosystem than vLLM. |
| [TensorRT-LLM](tensorrt-llm.md) | ✅ | B (4/6) | Highest NVIDIA throughput at the cost of vendor lock-in, an engine compile step, and closed-source kernels. |
| [LMDeploy](lmdeploy.md) | ✅ | A (6/6) | Compression plus serving in one toolkit; smaller community, partly Chinese-only docs. |
| [Text Generation Inference (TGI)](text-generation-inference.md) | ✅ | C (6/6) | Archived by Hugging Face: a pattern source or a pinned existing deployment, not a new default. |
| [Ray Serve](ray-serve.md) | ✅ | A (6/6) | General-purpose Python model serving with multi-model composition and autoscaling; built on Ray, operationally demanding. |
| [BentoML](bentoml.md) | ✅ | B (6/6) | Packages the model and its business logic into a deployable API; more framework than engine. |
| [Modular Platform (MAX + Mojo)](modular.md) | ✅ | B (5/6) | Vendor-built GPU/CPU serving platform plus the Mojo language; single-vendor and partly non-production licensing. |

## What belongs here

Engines and frameworks whose primary job is **serving models to many concurrent requests** behind an API on server-class hardware. Not single-user local runtimes (see `local-runtimes`), not on-device/edge runtimes (see `on-device-ml`), not fine-tuning (see `llm-training`).
