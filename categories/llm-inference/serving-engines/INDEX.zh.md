# serving-engines

> 分类节点。服务端级 LLM 推理引擎与模型服务框架——面向 GPU、并发请求和 API 边界。
> ← 返回 [llm-inference](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **vLLM** | 当你想要事实上的开源 LLM 服务引擎，带 PagedAttention、连续批处理和 OpenAI 兼容 API 时用它——接受 NVIDIA 主导的 GPU 运维和快速迭代的代码库。 | A（5/6） | [→](vllm.zh.md) |
| **SGLang** | 当你需要带 RadixAttention 前缀缓存和结构化生成的快速 LLM 服务引擎——适合工具调用型 agent 和 JSON 模式 API——并接受比 vLLM 更年轻、更小的生态时用它。 | A（5/6） | [→](sglang.zh.md) |
| **TensorRT-LLM** | 当你需要在 NVIDIA GPU 上榨取最大 LLM 推理吞吐、并愿意接受仅限 NVIDIA 的绑定、复杂的构建/engine 编译流程以及闭源内核时用它。 | B（5/6） | [→](tensorrt-llm.zh.md) |
| **LMDeploy** | 当你想要一套把 LLM 压缩、部署并服务化的工具包（带 OpenAI 兼容服务端）时用它——接受较小的社区与部分文档仅有中文的生态。 | A（6/6） | [→](lmdeploy.zh.md) |
| **Text Generation Inference (TGI)** | 只把它当模式参考或用于已 pin 住的既有部署，因为仓库已归档——要维护中的服务端选 vLLM 或 SGLang，要本地用选 llama.cpp 或 Ollama。 | C（6/6） | [→](text-generation-inference.zh.md) |
| **Ray Serve** | 当你需要通用、可扩展的 Python 模型服务框架，支持多模型组合和自动扩缩容时用它——但要接受 Ray 的运维复杂性和学习曲线。 | A（6/6） | [→](ray-serve.zh.md) |
| **BentoML** | 当你要把模型连同预处理一起打包成可部署的推理 API、并需要多模型流水线时用它——接受它比裸服务引擎更重。 | B（6/6） | [→](bentoml.zh.md) |
| **Modular Platform (MAX + Mojo)** | 当你想要高性能 GPU/CPU 推理平台（MAX）加 Mojo 系统语言、并接受单厂商绑定与部分非生产许可时用它。 | B（5/6） | [→](modular.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [vLLM](vllm.zh.md) | ✅ | A（5/6） | 事实上的开源服务引擎（PagedAttention、连续批处理）；NVIDIA 优先、迭代快，运维比本地运行时重。 |
| [SGLang](sglang.zh.md) | ✅ | A（5/6） | RadixAttention 前缀缓存与结构化生成，适合工具调用型 agent；生态比 vLLM 年轻。 |
| [TensorRT-LLM](tensorrt-llm.zh.md) | ✅ | B（5/6） | NVIDIA 上的最高吞吐，代价是厂商绑定、engine 编译步骤与闭源内核。 |
| [LMDeploy](lmdeploy.zh.md) | ✅ | A（6/6） | 压缩加服务一体化工具包；社区较小，部分文档仅有中文。 |
| [Text Generation Inference (TGI)](text-generation-inference.zh.md) | ✅ | C（6/6） | 已被 Hugging Face 归档：只当模式参考或用于已 pin 的既有部署，不是新项目默认项。 |
| [Ray Serve](ray-serve.zh.md) | ✅ | A（6/6） | 通用 Python 模型服务，支持多模型组合与自动扩缩容；基于 Ray，运维要求高。 |
| [BentoML](bentoml.zh.md) | ✅ | B（6/6） | 把模型与业务逻辑打包成可部署 API；更像框架而不是引擎。 |
| [Modular Platform (MAX + Mojo)](modular.zh.md) | ✅ | B（5/6） | 厂商自建的 GPU/CPU 服务引擎加 Mojo 语言；单厂商绑定且部分许可非生产可用。 |

## 什么该放这里

主要职责是在服务端硬件上**把模型以 API 形式服务给大量并发请求**的引擎与框架。不含单用户本地运行时（见 `local-runtimes`）、不含端侧/边缘运行时（见 `on-device-ml`）、不含微调（见 `llm-training`）。
