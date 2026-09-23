# local-runtimes

> 分类节点。在你自己的机器上跑模型的消费级硬件运行时——单用户、单机、没有调度器。
> ← 返回 [llm-inference](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **llama.cpp** | 当你想要那个无依赖的 C/C++ 上游引擎、跑在目前最宽的硬件矩阵上、既能嵌入也能本地起服务时用它——接受没有 semver、没有模型管理、只有 flag 级 API。 | A（6/6） | [→](llama-cpp.zh.md) |
| **Ollama** | 当你想要托管的本地模型仓库，配 OpenAI/Anthropic 兼容 API、Docker 部署与客户端 SDK 时用它——接受包装层的参数子集、4096 token 的默认上下文，以及没有服务级批处理。 | A（5/6） | [→](ollama.zh.md) |
| **Magnitude** | 当机器能力未知、你要下载前的速度与内存估算加一键接入已有 coding harness 时用它——接受一个两个月大、单厂商所有、且在 Apple Silicon 上报告比 llama.cpp 慢约 6 倍的仓库。 | B（6/6） | [→](magnitude.zh.md) |
| **omlx** | 当你想在 Mac（Apple Silicon）上用 MLX 跑带 SSD 分层 KV 缓存的本地 LLM 推理服务时用它——年轻的单人仓库，star 数存疑。 | B（5/6） | [→](omlx.zh.md) |
| **MTPLX** | 当你想让模型自带的 MTP 头在 Mac 上以精确投机解码把 Qwen 3.8 跑出约 2 倍速、并要 OpenAI/Anthropic 服务器与应用形态时用它——接受约五个月大、作者主导的仓库与产品内署名条款。 | B（6/6） | [→](mtplx.zh.md) |
| **AirLLM** | 当模型在你需要的形态下装不进显卡、而墙钟时间免费时用它——把检查点从磁盘逐层流式读取的库，显存只需一层的开销，代价是秒到分钟级的每 token 等待。 | B（6/6） | [→](airllm.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [llama.cpp](llama-cpp.zh.md) | ✅ | A（6/6） | 上游 GGUF 引擎，后端矩阵最宽且无运行时依赖；没有 semver、没有模型管理、只有 flag 级控制。 |
| [Ollama](ollama.zh.md) | ✅ | A（5/6） | 托管式模型仓库，配 OpenAI/Anthropic 兼容 API、Docker、MLX 与 llama.cpp 双 runner，客户端生态最深；代价是包装层参数子集与 4096 token 默认上下文。 |
| [Magnitude](magnitude.zh.md) | ✅ | B（6/6） | 下载前的硬件适配估算加一键 harness 接线，面向混合 GPU 机器群；年轻单厂商仓库，Apple Silicon 上报告比 llama.cpp 慢约 6 倍，且只监听回环。 |
| [omlx](omlx.zh.md) | ✅ | B（5/6） | Mac 专属 MLX 服务端，带 SSD 分层 KV 缓存；年轻、实际单人维护。 |
| [MTPLX](mtplx.zh.md) | ✅ | B（6/6） | Mac 专属、针对 Qwen 3.8 的精确 MTP 投机解码；作者主导、含署名 NOTICE，Qwen 之外的模型退化为纯 AR。
| [AirLLM](airllm.zh.md) | ✅ | — | 逐层流式读取的库，靠设备上只留一层在 4–12GB 小卡上跑 70B/671B 级模型；代价是每 token 都要读盘（用户实测 3B 模型 28.6 秒/token），且压缩选项实测更慢而不是更快。 | |

## 什么该放这里

主要职责是**在用户自己的机器上为单个用户跑模型**的运行时——桌面应用、单二进制服务端、可嵌入的引擎。不含带批处理与自动扩缩容的服务端级引擎（见 `serving-engines`）、不含手机/边缘运行时（见 `on-device-ml`）。
