# local-image-generation

> Category node. Run open-weight image/video diffusion models locally on your own GPU, Mac or CPU — a web UI, a node-graph workflow, or a native engine embedded in your app.
> ← back to [on-device-ml](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Stable Diffusion WebUI** | Use it when you want a tabbed local web UI with full parameter control and the large A1111 extension catalog for SD 1.5/SDXL work on an NVIDIA GPU — but its core has had no commit since 2024-07, so newer model families need ComfyUI. | D (4/6) | [→](stable-diffusion-webui.md) |
| **ComfyUI** | Use it when you generate images or video with open-weight models on your own GPU and need a reproducible node graph — ControlNet, LoRA, inpainting, upscaling — that reruns only what changed — but it has no login, quotas or tenant isolation. | B (5/6) | [→](comfyui.md) |
| **stable-diffusion.cpp** | Use it when you must ship image/video diffusion inside your own app or onto mixed CPU/AMD/Mac/NVIDIA machines as one native binary without Python — but expect a fixed feature set, no semver, and a no-auth single-worker server. | A (6/6) | [→](stable-diffusion-cpp.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Stable Diffusion WebUI](stable-diffusion-webui.md) | ✅ | D (4/6) | Buys the biggest extension ecosystem and tutorial base for classic SD workflows; costs a frozen core, AGPL-3.0 network copyleft, no multi-user isolation, and a Python/CUDA install you manage yourself. |
| [ComfyUI](comfyui.md) | ✅ | B (5/6) | Full pipeline control, saved inside every output and quick to support new open models, paid for with a node-graph learning curve, a usable GPU, and a roadmap owned by the company selling Comfy Cloud. |
| [stable-diffusion.cpp](stable-diffusion-cpp.md) | ✅ | A (6/6) | ggml-based C/C++ diffusion engine (SD, Flux, Qwen-Image, Wan…) with GGUF quantization and a C API; trades ComfyUI/WebUI workflow richness and extensions for a Python-free, embeddable binary. |

## What belongs here

UIs, workflow engines and inference libraries that run open-weight diffusion models on local hardware to produce images or video. Not hosted generation services; not AI design tools that output editable design documents (see `ai-design-generation`); not research code for training diffusion models (see `ml-research`).
