# on-device-ml

> Category node. Run ML/LLM inference locally on edge devices (phone, laptop, IoT) instead of the cloud.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **LiteRT-LM** | Use it when you want to run Gemma-class LLMs on phone/laptop/edge via Google's LiteRT runtime (CPU/GPU/NPU). | B (6/6) | [→](litert-lm.md) |
| **BitNet** | Use it when you need fast, low-energy CPU inference of natively-trained 1.58-bit ternary LLMs on x86/ARM laptops, offline. | C (6/6) | [→](bitnet.md) |
| **Google AI Edge Gallery** | Use it when you need to demo and benchmark on-device Gemma LLMs on real phones before building. | A (5/6) | [→](ai-edge-gallery.md) |
| **TimesFM** | Use it when you need zero-shot time-series forecasts run locally on CPU/GPU without per-dataset training. | B (5/6) | [→](timesfm.md) |
| **MiniCPM-V** | Use it when you need efficient on-device/edge multimodal (image+video) understanding with a small footprint — verify the per-weight license. | A (4/6) | [→](minicpm-v.md) |
| **Stable Diffusion WebUI** | Use it when you want a local web-based GUI for Stable Diffusion image generation, editing, and upscaling on your own GPU — but it requires technical setup and an NVIDIA GPU. | C (4/6) | [→](stable-diffusion-webui.md) |
| **ComfyUI** | Use it when you want a modular node-graph interface for building complex diffusion-model workflows locally — but it has a steep learning curve and requires significant GPU resources. | B (5/6) | [→](comfyui.md) |
| **MLX / mlx-lm** | Run LLMs with MLX | B (6/6) | [→](mlx-mlx-lm.md) |
| **Needle** | On-device 2-bit, 8–29 MB tool-calling/extraction/embedding model with schema grammar-constrained decoding and a confidence score. | B (4/6) | [→](needle.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [LiteRT-LM](litert-lm.md) | ✅ | B (6/6) | Use it when you want to run Gemma-class LLMs on phone/laptop/edge via Google's LiteRT runtime (CPU/GPU/NPU). |
| [BitNet](bitnet.md) | ✅ | C (6/6) | Use it when you need fast, low-energy CPU inference of natively-trained 1.58-bit ternary LLMs on x86/ARM laptops, offline. |
| [Google AI Edge Gallery](ai-edge-gallery.md) | ✅ | A (5/6) | Use it when you need to demo and benchmark on-device Gemma LLMs on real phones before building. |
| [TimesFM](timesfm.md) | ✅ | B (5/6) | Use it when you need zero-shot time-series forecasts run locally on CPU/GPU without per-dataset training. |
| [MiniCPM-V](minicpm-v.md) | ✅ | A (4/6) | Use it when you need efficient on-device/edge multimodal (image+video) understanding with a small footprint — verify the per-weight license. |
| [Stable Diffusion WebUI](stable-diffusion-webui.md) | ✅ | C (4/6) | Local web-based GUI for Stable Diffusion image generation, editing, and upscaling on your own GPU; requires technical setup and an NVIDIA GPU. |
| [ComfyUI](comfyui.md) | ✅ | B (5/6) | Modular node-graph interface for building complex diffusion-model workflows locally; steep learning curve and significant GPU resources required. |
| [Needle](needle.md) | ✅ | B (4/6) | On-device 2-bit tool-calling + structured extraction + embedding model with grammar-constrained decoding. |
| MLC LLM / ONNX Runtime | 未收录 | — | Other on-device inference runtimes named across the pages (llama.cpp and Ollama are indexed under `llm-inference`). |

## What belongs here

Runtimes and models meant to **run inference locally / on-device** — phone, laptop, edge, CPU. Not cloud training (see `llm-training`), not RAG retrieval (see `rag-retrieval`).
