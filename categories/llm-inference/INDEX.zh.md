# llm-inference

> 分类节点。高性能 LLM/模型推理与服务引擎，以及 AI 系统语言。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Modular Platform (MAX + Mojo)** | 当你想要高性能 GPU/CPU 推理平台（MAX）加 Mojo 系统语言、并接受单厂商绑定与部分非生产许可时用它。 | B（5/6） | [→](modular.zh.md) |
| **omlx** | 当你想在 Mac（Apple Silicon）上用 MLX 跑带 SSD 分层 KV 缓存的本地 LLM 推理服务时用它——年轻的单人仓库，star 数存疑。 | B（5/6） | [→](omlx.zh.md) |
| **MTPLX** | 当你想让模型自带的 MTP 头在 Mac 上以精确投机解码把 Qwen 3.8 跑出约 2 倍速、并要 OpenAI/Anthropic 服务器与应用形态时用它——接受约五个月大、作者主导的仓库与产品内署名条款。 | B（6/6） | [→](mtplx.zh.md) |
| **TensorRT-LLM** | 当你需要在 NVIDIA GPU 上榨取最大 LLM 推理吞吐、并愿意接受仅限 NVIDIA 的绑定、复杂的构建/engine 编译流程以及闭源内核时用它。 | — | [→](tensorrt-llm.zh.md) |
| **vLLM** | 当你想要事实上的开源 LLM 服务引擎，带 PagedAttention、连续批处理和 OpenAI 兼容 API 时用它——接受 NVIDIA 主导的 GPU 运维和快速迭代的代码库。 | — | [→](vllm.zh.md) |
| **SGLang** | 当你需要带 RadixAttention 前缀缓存和结构化生成的快速 LLM 服务引擎——适合工具调用型 agent 和 JSON 模式 API——并接受比 vLLM 更年轻、更小的生态时用它。 | — | [→](sglang.zh.md) |
| **Ray Serve** | 当你需要通用、可扩展的 Python 模型服务框架，支持多模型组合和自动扩缩容时用它——但要接受 Ray 的运维复杂性和学习曲线。 | — | [→](ray-serve.zh.md) |
| **llama.cpp** | LLM inference in C/C++ | ?（0/6） | [→](llama-cpp.zh.md) |
| **Ollama** | Get up and running with Kimi-K2.6, GLM-5.1, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models. | ?（0/6） | [→](ollama.zh.md) |
| **BentoML** | The easiest way to serve AI apps and models - Build Model Inference APIs, Job queues, LLM apps, Multi-model pipelines, and more! | ?（0/6） | [→](bentoml.zh.md) |
| **LMDeploy** | LMDeploy is a toolkit for compressing, deploying, and serving LLMs. | ?（0/6） | [→](lmdeploy.zh.md) |
| **Text Generation Inference (TGI)** | Large Language Model Text Generation Inference | ?（0/6） | [→](text-generation-inference.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Modular Platform (MAX + Mojo)](modular.zh.md) | ✅ | B（5/6） | 当你想要高性能 GPU/CPU 推理平台（MAX）加 Mojo 系统语言、并接受单厂商绑定与部分非生产许可时用它。 |
| [omlx](omlx.zh.md) | ✅ | B（5/6） | 当你想在 Mac（Apple Silicon）上用 MLX 跑带 SSD 分层 KV 缓存的本地 LLM 推理服务时用它——年轻的单人仓库，star 数存疑。 |
| [MTPLX](mtplx.zh.md) | ✅ | B（6/6） | Mac 原生精确 MTP 投机解码跑 Qwen 3.8（约 2 倍速，作者实测）；年轻、作者主导、许可含产品内署名 NOTICE；Qwen 之外的模型退化为纯 AR。 |
| [vLLM](vllm.zh.md) | ✅ | — | 事实上的开源 LLM 服务引擎（PagedAttention、连续批处理），庞大社区与模型覆盖；NVIDIA 优先，代码库快速迭代。 |
| [SGLang](sglang.zh.md) | ✅ | — | 快速 LLM 服务引擎，带 RadixAttention 前缀缓存和结构化生成；比 vLLM 更年轻的生态，适合工具调用型 agent。 |
| [Ray Serve](ray-serve.zh.md) | ✅ | — | 通用可扩展的 Python 模型服务框架，支持多模型组合和自动扩缩容；基于 Ray，运维要求高。 |
| [TensorRT-LLM](tensorrt-llm.zh.md) | ✅ | — | 当你需要在 NVIDIA GPU 上榨取最大 LLM 推理吞吐、并愿意接受仅限 NVIDIA 的绑定、复杂的构建/engine 编译流程以及闭源内核时用它。 |
| TGI / BentoML | 未收录 | — | 各页对比里点到的其他 LLM 推理/服务引擎。 |

## 什么该放这里

主要职责是**高性能 LLM/模型推理与服务**的引擎与系统语言。不含端侧/边缘运行时（见 `on-device-ml`），不含 LLM 微调（见 `llm-training`）。
