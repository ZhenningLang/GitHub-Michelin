# serving-engines

> Category node. Server-class LLM serving engines and model-serving frameworks — built for GPUs, concurrent requests, and an API boundary.
> ← back to [llm-inference](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **vLLM** | Use it when you want the de-facto open-source LLM serving engine with PagedAttention, continuous batching, and an OpenAI-compatible API — accepting NVIDIA-centric GPU ops and a fast-moving codebase. | A (5/6) | [→](vllm.md) |
| **SGLang** | Use it when agent traffic repeats long shared prompts and needs schema-constrained JSON, so prefix caching and structured generation cut GPU time — but since v0.5.20 it requires CUDA 13, and its ecosystem and track record are younger than vLLM's. | A (5/6) | [→](sglang.md) |
| **TensorRT-LLM** | Use it when you serve high-traffic models on Hopper or Blackwell GPUs and need NVIDIA-tuned kernels, FP4 and rack-scale parallelism to close a throughput gap — but it runs only on recent NVIDIA GPUs and some key kernels ship as precompiled binaries. | B (5/6) | [→](tensorrt-llm.md) |
| **LMDeploy** | Use it when you must serve a 7B–70B open model on older GPUs, consumer cards or Ascend accelerators by quantizing to 4-bit and serving from one CLI — but it is still 0.x with refactors in minor releases and a smaller ecosystem than vLLM. | A (6/6) | [→](lmdeploy.md) |
| **Text Generation Inference (TGI)** | Use it only to keep an existing pinned TGI deployment running while you plan migration, or to read its batching server design — Hugging Face put it in maintenance mode in 2025-12 and archived the repo, so no new models or security fixes arrive. | C (6/6) | [→](text-generation-inference.md) |
| **Ray Serve** | Use it when several models (rankers, classifiers, LLMs) must compose in one Python application with per-model autoscaling across CPU and GPU nodes, ideally where you already run Ray — but for a single LLM it adds a cluster without adding speed. | A (6/6) | [→](ray-serve.md) |
| **BentoML** | Use it when you need to wrap non-chat models or multi-model pipelines with custom Python pre- and post-processing into a batched HTTP API and container image — but development has slowed since Modular's 2026 acquisition and its Kubernetes operator Yatai is archived. | B (6/6) | [→](bentoml.md) |
| **Modular Platform (MAX + Mojo)** | Use it when you want a high-performance GPU/CPU inference platform (MAX) plus the Mojo systems language — accepting single-vendor lock-in and partly non-production licensing. | B (5/6) | [→](modular.md) |
| **SIE (Superlinked Inference Engine)** | Use it when an agent pipeline needs many small models (embed, rerank, OCR, extraction, guards) behind one API with LRU model loading and a Helm/KEDA cluster — accepting a ~6-month-old, single-vendor 0.x codebase with frequent breaking minors. | B (6/6) | [→](sie.md) |
| **llm-d** | Use it when a Kubernetes fleet of vLLM/SGLang pods needs LLM-aware routing (prefix-cache and queue-aware), prefill/decode disaggregation or KV-cache offload from benchmarked Helm/kustomize recipes — accepting a young pre-1.0 CNCF Sandbox stack with heavy cluster ops and component churn between releases. | B (5/6) | [→](llm-d.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [vLLM](vllm.md) | ✅ | A (5/6) | The de-facto open-source serving engine (PagedAttention, continuous batching); NVIDIA-first, fast-moving, operationally heavier than a local runtime. |
| [SGLang](sglang.md) | ✅ | A (5/6) | Prefix reuse and constrained decoding speed up agent workloads, at the cost of a fast release train that needs pinning and revalidation every few weeks. |
| [TensorRT-LLM](tensorrt-llm.md) | ✅ | B (5/6) | First access to NVIDIA hardware features and throughput, at the cost of vendor lock-in, unreadable kernels, telemetry on by default and a slow stable-release cadence. |
| [LMDeploy](lmdeploy.md) | ✅ | A (6/6) | Compression and serving in one toolkit with broad accelerator support, at the cost of API churn between releases and narrower model coverage than vLLM. |
| [Text Generation Inference (TGI)](text-generation-inference.md) | ✅ | C (6/6) | Buys continuity for clients already calling its endpoints and scraping its Prometheus metrics; costs owning image patching yourself and a forced move to vLLM or SGLang. |
| [Ray Serve](ray-serve.md) | ✅ | A (6/6) | Foundation-governed, flexible multi-model composition, at the cost of running a full distributed runtime and debugging Ray's actors and object store when things break. |
| [BentoML](bentoml.md) | ✅ | B (6/6) | One decorated class yields the server, batching and image, at the cost of an extra layer over raw engines and DIY autoscaling on Kubernetes. |
| [Modular Platform (MAX + Mojo)](modular.md) | ✅ | B (5/6) | Vendor-built GPU/CPU serving platform plus the Mojo language; single-vendor and partly non-production licensing. |
| [SIE (Superlinked Inference Engine)](sie.md) | ✅ | B (6/6) | One API and cluster for many small task models (embed/rerank/OCR/extract/guard) with on-demand loading; young single-vendor 0.x, delegates LLM generation to SGLang. |
| [llm-d](llm-d.md) | ✅ | B (5/6) | LLM-aware router plus recipes on top of vLLM/SGLang on Kubernetes (prefix-cache routing, P/D split, KV offload); multi-vendor CNCF Sandbox, young pre-1.0 with heavy cluster ops. |

## What belongs here

Engines and frameworks whose primary job is **serving models to many concurrent requests** behind an API on server-class hardware. Not single-user local runtimes (see `local-runtimes`), not on-device/edge runtimes (see `on-device-ml`), not fine-tuning (see `llm-training`).
