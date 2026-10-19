# apple-local-inference

> Category node. Your primary deployment is an Apple device, and MLX, Metal or Core ML determines the local inference and integration path.
> ← back to [on-device-ml](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **TurboFieldfare** | Run pinned Gemma 4 on an 8 GB Mac by streaming experts from SSD; Apple-only and model-specific. | C (6/6) | [→](turbo-fieldfare.md) |
| **FluidUse** | Call specialized Core ML decisions from Swift and match form values to real Mac controls; not a general isolated agent. | C (5/6) | [→](fluiduse.md) |
| **uzu** | Use it when an LLM must run inside your own iOS/macOS app and you want a Swift/Python/TS SDK that picks, downloads and runs a pre-converted model on the Apple GPU — but it needs OS 26.4+, uses Mirai's own model format and hosted registry, and sends default-on telemetry. | B (6/6) | [→](uzu.md) |
| **MLX / mlx-lm** | Use it when you try new Hugging Face models on an Apple-silicon Mac and want to generate, quantize and LoRA-fine-tune them from one Python package without GGUF conversion — but mlx_lm.server is not meant for production or multi-user serving. | B (6/6) | [→](mlx-mlx-lm.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [TurboFieldfare](turbo-fieldfare.md) | ✅ | C (6/6) | Fixed expert buffers trade SSD reads for lower resident-weight memory; macOS 26 and one pinned Gemma checkpoint. |
| [FluidUse](fluiduse.md) | ✅ | C (5/6) | Call specialized Core ML decisions from Swift and match form values to real Mac controls; not a general isolated agent. |
| [uzu](uzu.md) | ✅ | B (6/6) | Mirai's Rust engine with Swift/Python/TS bindings and hand-written Metal 4 kernels: names a catalog model, downloads a pre-converted copy and runs it in-app; Apple-only (OS 26.4+), own model format, vendor registry and default-on telemetry, young single-company project. |
| [MLX / mlx-lm](mlx-mlx-lm.md) | ✅ | B (6/6) | Use it when you try new Hugging Face models on an Apple-silicon Mac and want to generate, quantize and LoRA-fine-tune them from one Python package without GGUF conversion — but mlx_lm.server is not meant for production or multi-user serving. |

## What belongs here

Local inference and application integration selected primarily around MLX, Metal or Core ML on Apple devices. Apple-first does not mean Apple-only: MLX also documents CUDA/CPU extras. Mac support alone does not qualify a general runtime or task-specific model. For image/video diffusion, enter [local-image-generation](../local-image-generation/INDEX.md) first; other local inference routes remain in [on-device-ml](../INDEX.md).
