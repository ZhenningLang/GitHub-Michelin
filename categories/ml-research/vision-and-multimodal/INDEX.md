# vision-and-multimodal

> Category node. Vision and vision-language research models and reference code — image embeddings, monocular depth, GAN architectures, early visual tool-routing agents.
> ← back to [ml-research](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **CLIP** | Use it when you need zero-shot image classification or image↔text retrieval embeddings — the original frozen reference; OpenCLIP has more checkpoints. | C (5/6) | [→](clip.md) |
| **TaskMatrix** | Use it only to study an early visual-tool-routing agent (Visual ChatGPT) — abandoned since ~2024, don't build on it. | "?" (2/6) | [→](taskmatrix.md) |
| **PyTorch-GAN** | Read it to learn GAN architectures from clean reference implementations — idle since 2024 and superseded by diffusion; not production code. | D (3/6) | [→](pytorch-gan.md) |
| **Depth Anything V2** | Use it as the current default monocular-depth foundation model for single-image depth in PyTorch/Transformers — only the Small weights are Apache-2.0; Base/Large/Giant are CC-BY-NC-4.0 (non-commercial). | C (4/6) | [→](depth-anything-v2.md) |
| **Open-Sora** | Use it when you must *train* or study a video diffusion model from a fully published recipe (code, data pipeline, cost report) on datacenter GPUs — dormant since 2025-03, and its weight stack pulls in FLUX.1-dev non-commercial and Tencent Hunyuan licenses. | B (4/6) | [→](open-sora.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [CLIP](clip.md) | ✅ | C (5/6) | Use it when you need zero-shot image classification or image↔text retrieval embeddings — the original frozen reference; OpenCLIP has more checkpoints. |
| [TaskMatrix](taskmatrix.md) | ✅ | "?" (2/6) | Use it only to study an early visual-tool-routing agent (Visual ChatGPT) — abandoned since ~2024, don't build on it. |
| [PyTorch-GAN](pytorch-gan.md) | ✅ | D (3/6) | Read it to learn GAN architectures from clean reference implementations — idle since 2024 and superseded by diffusion; not production code. |
| [Depth Anything V2](depth-anything-v2.md) | ✅ | C (4/6) | Use it as the current default monocular-depth foundation model for single-image depth in PyTorch/Transformers — only the Small weights are Apache-2.0; Base/Large/Giant are CC-BY-NC-4.0 (non-commercial). |
| [Open-Sora](open-sora.md) | ✅ | B (4/6) | Open 11B text/image-to-video model plus its full training recipe; research artifact, not a maintained product — dormant since 2025-03, ~50 GB VRAM per GPU, and the Apache-2.0 badge does not cover the FLUX.1-dev / Hunyuan VAE weights it loads. |

## What belongs here

Research models and reference implementations whose input or output is **images**: vision-language embeddings ([CLIP](clip.md)), monocular depth ([Depth Anything V2](depth-anything-v2.md)), classic GAN architectures ([PyTorch-GAN](pytorch-gan.md)), the early LLM-routes-vision-models agent pattern ([TaskMatrix](taskmatrix.md)), and open video-generation models released with their training recipe ([Open-Sora](open-sora.md)). Not 3D reconstruction from captures (see `3d-reconstruction`), not end-user image tools (see `media-processing`).
