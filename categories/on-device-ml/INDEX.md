# on-device-ml

> Category node. Run ML/LLM inference locally on edge devices (phone, laptop, IoT) instead of the cloud.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **local-image-generation** | You want open-weight image/video diffusion models running locally on your own GPU, Mac or CPU. | [→](local-image-generation/INDEX.md) |
| **apple-local-inference** | Outside image/video diffusion, your primary deployment is an Apple device, and MLX, Metal or Core ML determines the local inference and integration path. | [→](apple-local-inference/INDEX.md) |

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **CosmoEdge** | Deploy visually configured video inference and alarms on Sophon, Rockchip or x86; models and capacity stay platform-specific. | B (6/6) | [→](cosmo-edge.md) |
| **LiteRT-LM** | Use it when you want to run Gemma-class LLMs on phone/laptop/edge via Google's LiteRT runtime (CPU/GPU/NPU). | B (6/6) | [→](litert-lm.md) |
| **BitNet** | Use it when you need fast, low-energy CPU inference of natively-trained 1.58-bit ternary LLMs on x86/ARM laptops, offline. | B (5/6) | [→](bitnet.md) |
| **Google AI Edge Gallery** | Use it when you need to demo and benchmark on-device Gemma LLMs on real phones before building. | B (6/6) | [→](ai-edge-gallery.md) |
| **TimesFM** | Use it when you need zero-shot time-series forecasts run locally on CPU/GPU without per-dataset training. | A (5/6) | [→](timesfm.md) |
| **MiniCPM-V** | Use it when you need efficient on-device/edge multimodal (image+video) understanding with a small footprint — verify the per-weight license. | A (4/6) | [→](minicpm-v.md) |
| **MiniCPM** | Use it when a chat, coding or tool-calling assistant must run offline on a laptop, phone or CPU box at 1–2B size (MiniCPM5, Apache-2.0, GGUF 0.66–1.56 GB) — but tune sampling on 4-bit builds and use a runtime that parses its XML tool calls. | B (5/6) | [→](minicpm.md) |
| **Needle** | Use it when a tiny on-device model must do English tool calling, typed extraction or embeddings offline (29–121M params, 2-bit) — but the base model needs a fine-tune and your own guards on refusals. | B (4/6) | [→](needle.md) |
| **BirdNET-Go** | Use it when you want an always-on bird (and bat) sound station on a Raspberry Pi 4/5 or mini PC with a local web dashboard, multiple mics/RTSP streams and MQTT/Home Assistant alerts — but the code and models are non-commercial (CC BY-NC-SA), the default install tracks a single maintainer's nightly build, and batch file analysis belongs to other tools. | B (5/6) | [→](birdnet-go.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Apple local inference](apple-local-inference/INDEX.md) | Sub-category | — | Apple-first MLX, Metal and Core ML integration, not a claim that every project is Apple-only; image/video diffusion keeps its existing task category. |
| [CosmoEdge](cosmo-edge.md) | ✅ | B (6/6) | Deploy visually configured video inference and alarms on Sophon, Rockchip or x86; models and capacity stay platform-specific. |
| [LiteRT-LM](litert-lm.md) | ✅ | B (6/6) | Use it when you want to run Gemma-class LLMs on phone/laptop/edge via Google's LiteRT runtime (CPU/GPU/NPU). |
| [BitNet](bitnet.md) | ✅ | B (5/6) | Use it when you need fast, low-energy CPU inference of natively-trained 1.58-bit ternary LLMs on x86/ARM laptops, offline. |
| [Google AI Edge Gallery](ai-edge-gallery.md) | ✅ | B (6/6) | Use it when you need to demo and benchmark on-device Gemma LLMs on real phones before building. |
| [TimesFM](timesfm.md) | ✅ | A (5/6) | Use it when you need zero-shot time-series forecasts run locally on CPU/GPU without per-dataset training. |
| [MiniCPM-V](minicpm-v.md) | ✅ | A (4/6) | Use it when you need efficient on-device/edge multimodal (image+video) understanding with a small footprint — verify the per-weight license. |
| [MiniCPM](minicpm.md) | ✅ | B (5/6) | Apache-2.0 1–2B text models with per-runtime cookbooks, agent skills and released training data; trades the bigger ecosystem and JSON tool-call format of Qwen/Gemma for documented deployment, and its 4-bit builds loop without sampling tuning. |
| [Needle](needle.md) | ✅ | B (4/6) | English-only on-device tool-calling/extraction/embedding model (29–121M, 2-bit) with grammar-constrained decoding; the base model misses negations, out-of-range values and off-domain requests. |
| [BirdNET-Go](birdnet-go.md) | ✅ | B (5/6) | Self-hosted Go app that classifies live audio with BirdNET v2.4 (plus optional Perch v2 and bat models) and logs detections with clips; trades reproducibility and commercial use for a turnkey 24/7 station — non-OSI licence, nightly-by-default, one maintainer. |
| MLC LLM / ONNX Runtime | 未收录 | — | Other on-device inference runtimes named across the pages (llama.cpp and Ollama are indexed under `llm-inference`). |

## What belongs here

Runtimes and models meant to **run inference locally / on-device** — phone, laptop, edge, CPU. Choose [local-image-generation](local-image-generation/INDEX.md) first for image/video diffusion; otherwise use [apple-local-inference](apple-local-inference/INDEX.md) when the Apple compute stack determines deployment. General runtimes and task-specific models remain here even if they support Mac. Not cloud training (see `llm-training`), not RAG retrieval (see `rag-retrieval`).
