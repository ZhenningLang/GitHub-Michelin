# vision-and-multimodal

> Category node. Vision and vision-language research models and reference code — image embeddings, monocular depth, GAN architectures, early visual tool-routing agents.
> ← back to [ml-research](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **CLIP** | Use it when you need zero-shot image classification or image-text retrieval by writing labels as plain text, straight from OpenAI's original checkpoints — but it is a frozen reference with older ViT/ResNet backbones; OpenCLIP or transformers offer more models and maintenance. | C (5/6) | [→](clip.md) |
| **TaskMatrix** | Use it only to study how Visual ChatGPT routed a text-only ChatGPT to about 20 vision foundation models via prompts — it is abandoned since 2023-06, and modern multimodal LLMs now do the same job natively in one model. | "?" (2/6) | [→](taskmatrix.md) |
| **PyTorch-GAN** | Use it when you want to read classic 2014–2018 GAN papers as one self-contained PyTorch script each (DCGAN, CycleGAN, WGAN-GP, pix2pix) — but the author calls it stale, nothing has landed since 2021, and diffusion has replaced GANs for real generation. | D (3/6) | [→](pytorch-gan.md) |
| **Depth Anything V2** | Use it when you need a dense depth map from a single image — 3D, bokeh, AR occlusion, controllable generation — with off-the-shelf weights — but only Small is Apache-2.0 (Base/Large/Giant are non-commercial CC-BY-NC-4.0) and default output is relative, not metric. | C (4/6) | [→](depth-anything-v2.md) |
| **Open-Sora** | Use it when you must *train* or study a video diffusion model from a fully published recipe (code, data pipeline, cost report) on datacenter GPUs — dormant since 2025-03, and its weight stack pulls in FLUX.1-dev non-commercial and Tencent Hunyuan licenses. | B (4/6) | [→](open-sora.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [CLIP](clip.md) | ✅ | C (5/6) | Buys the canonical, minimal CLIP code and weights; costs a fixed model set that SigLIP and EVA-CLIP now beat, and it only embeds — no captions or answers. |
| [TaskMatrix](taskmatrix.md) | ✅ | "?" (2/6) | Buys a runnable historical example of early tool-routing agents; costs hosting a foundation-model zoo for a capability native vision models and modern function-calling tooling now cover better. |
| [PyTorch-GAN](pytorch-gan.md) | ✅ | D (3/6) | Buys dozens of compact, side-by-side architectures to learn from; costs any library value — no package, no stable API, no modern GANs, and layer configs may differ from the papers. |
| [Depth Anything V2](depth-anything-v2.md) | ✅ | C (4/6) | Buys strong monocular depth in a few lines of PyTorch; costs a frozen research release and license-gated quality — the larger, better checkpoints are off-limits for commercial products. |
| [Open-Sora](open-sora.md) | ✅ | B (4/6) | Open 11B text/image-to-video model plus its full training recipe; research artifact, not a maintained product — dormant since 2025-03, ~50 GB VRAM per GPU, and the Apache-2.0 badge does not cover the FLUX.1-dev / Hunyuan VAE weights it loads. |

## What belongs here

Research models and reference implementations whose input or output is **images**: vision-language embeddings ([CLIP](clip.md)), monocular depth ([Depth Anything V2](depth-anything-v2.md)), classic GAN architectures ([PyTorch-GAN](pytorch-gan.md)), the early LLM-routes-vision-models agent pattern ([TaskMatrix](taskmatrix.md)), and open video-generation models released with their training recipe ([Open-Sora](open-sora.md)). Not 3D reconstruction from captures (see `3d-reconstruction`), not end-user image tools (see `media-processing`).
