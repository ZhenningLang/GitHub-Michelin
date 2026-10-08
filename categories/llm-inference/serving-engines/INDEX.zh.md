# serving-engines

> 分类节点。服务端级 LLM 推理引擎与模型服务框架——面向 GPU、并发请求和 API 边界。
> ← 返回 [llm-inference](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **vLLM** | 当你想要事实上的开源 LLM 服务引擎，带 PagedAttention、连续批处理和 OpenAI 兼容 API 时用它——接受 NVIDIA 主导的 GPU 运维和快速迭代的代码库。 | A（5/6） | [→](vllm.zh.md) |
| **SGLang** | 当 agent 流量反复带着同一段长提示、又要求输出符合 JSON schema，需要前缀缓存和结构化生成来省 GPU 时间时用它——但 v0.5.20 起要求 CUDA 13，生态和生产记录也比 vLLM 年轻。 | A（5/6） | [→](sglang.zh.md) |
| **TensorRT-LLM** | 当你在 Hopper 或 Blackwell GPU 上服务高流量模型，需要 NVIDIA 调优内核、FP4 和整机柜并行来补上吞吐差距时用它——但它只跑在较新的 NVIDIA GPU 上，部分关键内核还是预编译二进制。 | B（5/6） | [→](tensorrt-llm.zh.md) |
| **LMDeploy** | 当你要在受限或老旧的 GPU、消费级显卡或昇腾等国产加速卡上，用一个命令行把 7B 到 70B 的开源模型量化到 4-bit 再对外服务时用它——但它仍是 0.x，小版本就带重构，生态也比 vLLM 小。 | A（6/6） | [→](lmdeploy.zh.md) |
| **Text Generation Inference (TGI)** | 仅当你要维持一套已 pin 住的 TGI 部署、同时规划迁移，或想研读它的批处理服务设计时用它——Hugging Face 已在 2025-12 将其转入维护模式并归档仓库，不会再有新模型支持和安全修复。 | C（6/6） | [→](text-generation-inference.zh.md) |
| **Ray Serve** | 当排序器、分类器、大模型等多个模型要在一个 Python 应用里组合、各自跨 CPU 和 GPU 节点扩缩，最好团队本来就在跑 Ray 时用它——但只服务一个大模型时，它只多出一个集群，不会更快。 | A（6/6） | [→](ray-serve.zh.md) |
| **BentoML** | 当你要把非聊天类模型或多模型流水线连同自定义 Python 前后处理，打包成带批处理的 HTTP 接口和容器镜像时用它——但自 2026 年被 Modular 收购后开发放缓，Kubernetes operator Yatai 也已归档。 | B（6/6） | [→](bentoml.zh.md) |
| **Modular Platform (MAX + Mojo)** | 当你想要高性能 GPU/CPU 推理平台（MAX）加 Mojo 系统语言、并接受单厂商绑定与部分非生产许可时用它。 | B（5/6） | [→](modular.zh.md) |
| **SIE (Superlinked Inference Engine)** | 当一条 agent 流水线要把许多小模型（向量、重排、OCR、抽取、审核）放在同一个 API 后面、按需加载并用 Helm／KEDA 集群扩缩时用它——接受一个约 6 个月大、单厂商维护、minor 版本常带破坏性变更的 0.x 代码库。 | B（6/6） | [→](sie.zh.md) |
| **llm-d** | 当 Kubernetes 上一批 vLLM／SGLang pod 需要懂大模型的路由（按前缀缓存和排队派单）、预填充／解码拆分或 KV 缓存卸载，并想直接用跑过基准的 Helm／kustomize 配方时用它——接受一个年轻的 1.0 前 CNCF Sandbox 技术栈、较重的集群运维和版本间频繁的组件变动。 | B（5/6） | [→](llm-d.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [vLLM](vllm.zh.md) | ✅ | A（5/6） | 事实上的开源服务引擎（PagedAttention、连续批处理）；NVIDIA 优先、迭代快，运维比本地运行时重。 |
| [SGLang](sglang.zh.md) | ✅ | A（5/6） | 前缀复用和受约束解码加速 agent 负载，代价是版本迭代快，需要钉版本并每隔几周重新验证。 |
| [TensorRT-LLM](tensorrt-llm.zh.md) | ✅ | B（5/6） | 最早用上 NVIDIA 硬件特性和吞吐，代价是厂商绑定、部分内核不可读、默认开启遥测，正式版发布也慢。 |
| [LMDeploy](lmdeploy.zh.md) | ✅ | A（6/6） | 压缩和服务一体、加速卡支持面广，代价是版本间 API 常变，模型覆盖也不如 vLLM。 |
| [Text Generation Inference (TGI)](text-generation-inference.zh.md) | ✅ | C（6/6） | 换来已在调用其接口、抓其 Prometheus 指标的调用方不必马上改；代价是镜像补丁得自己扛，迟早要迁到 vLLM 或 SGLang。 |
| [Ray Serve](ray-serve.zh.md) | ✅ | A（6/6） | 换来基金会治理、灵活的多模型组合，代价是要运行整套分布式运行时，出问题时得先调 Ray 的 actor 和对象存储。 |
| [BentoML](bentoml.zh.md) | ✅ | B（6/6） | 一个加装饰器的类就生成服务、批处理和镜像，代价是比裸引擎多一层，Kubernetes 上的自动扩缩要自己接。 |
| [Modular Platform (MAX + Mojo)](modular.zh.md) | ✅ | B（5/6） | 厂商自建的 GPU/CPU 服务引擎加 Mojo 语言；单厂商绑定且部分许可非生产可用。 |
| [SIE (Superlinked Inference Engine)](sie.zh.md) | ✅ | B（6/6） | 一套 API 和集群服务许多小任务模型（向量／重排／OCR／抽取／审核），按需加载；单厂商、年轻的 0.x，大模型生成交给 SGLang。 |
| [llm-d](llm-d.zh.md) | ✅ | B（5/6） | Kubernetes 上叠在 vLLM／SGLang 之上的大模型感知路由加配方（前缀缓存路由、P/D 拆分、KV 卸载）；多厂商共建的 CNCF Sandbox，年轻、未到 1.0，集群运维重。 |

## 什么该放这里

主要职责是在服务端硬件上**把模型以 API 形式服务给大量并发请求**的引擎与框架。不含单用户本地运行时（见 `local-runtimes`）、不含端侧/边缘运行时（见 `on-device-ml`）、不含微调（见 `llm-training`）。
