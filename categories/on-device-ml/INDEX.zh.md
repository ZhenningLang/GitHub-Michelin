# on-device-ml

> 分类节点。在端侧/边缘设备（手机、笔记本、IoT）本地跑 ML/LLM 推理，而非云端。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 子分类 | 何时进入 | 路由 |
| --- | --- | --- |
| **local-image-generation** | 你要在自己的 GPU、Mac 或 CPU 上本地跑开源权重的图像/视频扩散模型。 | [→](local-image-generation/INDEX.zh.md) |
| **apple-local-inference** | 不做图像／视频扩散，主要部署目标是 Apple 设备，且 MLX、Metal 或 Core ML 决定本地推理与集成路径。 | [→](apple-local-inference/INDEX.zh.md) |

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **CosmoEdge** | 在 Sophon、Rockchip 或 x86 可视化部署视频推理与告警；模型和容量仍分平台。 | B（6/6） | [→](cosmo-edge.zh.md) |
| **LiteRT-LM** | 想用 Google LiteRT 运行时在手机/笔记本/边缘（CPU/GPU/NPU）上跑 Gemma 级 LLM 时用它。 | B（6/6） | [→](litert-lm.zh.md) |
| **BitNet** | 当你要在 x86/ARM 笔记本上离线、快速、低能耗地用 CPU 跑原生三值（1.58-bit） LLM 时使用。 | B（5/6） | [→](bitnet.zh.md) |
| **Google AI Edge Gallery** | 当你想在真机上先体验和基准测试端侧 Gemma LLM、为是否自建集成去风险时用它。 | B（6/6） | [→](ai-edge-gallery.zh.md) |
| **TimesFM** | 当你需要在本地 CPU/GPU 上对时间序列做零样本预测、又不想逐数据集训练时用它。 | A（5/6） | [→](timesfm.zh.md) |
| **MiniCPM-V** | 当你需要小体积、可在端侧/边缘运行的多模态（图像+视频）理解时用它——注意逐权重许可。 | A（4/6） | [→](minicpm-v.zh.md) |
| **MiniCPM** | 当聊天、编码或调工具的助手必须以 1–2B 体量离线跑在笔记本、手机或 CPU 盒子上时用它（MiniCPM5，Apache-2.0，GGUF 0.66–1.56GB）——但 4 bit 版要调采样参数，并选能解析其 XML 工具调用的运行时。 | B（5/6） | [→](minicpm.zh.md) |
| **Needle** | 当需要一个小体积端侧模型离线完成**英文**工具调用、类型化抽取或嵌入时用它（29–121M 参数、2-bit）——但基座模型需要微调，拒绝类请求要自建守卫。 | B（4/6） | [→](needle.zh.md) |
| **BirdNET-Go** | 当你想在树莓派 4/5 或小主机上搭一个全天候的鸟类（及蝙蝠）声音监测站，带本地网页仪表盘、多路麦克风和 RTSP 音源、MQTT 与 Home Assistant 告警时用它——但代码和模型都禁止商用（CC BY-NC-SA），默认安装跟的是单人维护的每夜构建，批量文件分析要交给别的工具。 | B（5/6） | [→](birdnet-go.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Apple 本地推理](apple-local-inference/INDEX.zh.md) | 子分类 | — | 以 Apple 为主的 MLX、Metal 与 Core ML 集成，不声称每项都是 Apple 专属；图像／视频扩散仍按已有任务子类进入。 |
| [CosmoEdge](cosmo-edge.zh.md) | ✅ | B（6/6） | 在 Sophon、Rockchip 或 x86 可视化部署视频推理与告警；模型和容量仍分平台。 |
| [LiteRT-LM](litert-lm.zh.md) | ✅ | B（6/6） | 想用 Google LiteRT 运行时在手机/笔记本/边缘（CPU/GPU/NPU）上跑 Gemma 级 LLM 时用它。 |
| [BitNet](bitnet.zh.md) | ✅ | B（5/6） | 当你要在 x86/ARM 笔记本上离线、快速、低能耗地用 CPU 跑原生三值（1.58-bit） LLM 时使用。 |
| [Google AI Edge Gallery](ai-edge-gallery.zh.md) | ✅ | B（6/6） | 当你想在真机上先体验和基准测试端侧 Gemma LLM、为是否自建集成去风险时用它。 |
| [TimesFM](timesfm.zh.md) | ✅ | A（5/6） | 当你需要在本地 CPU/GPU 上对时间序列做零样本预测、又不想逐数据集训练时用它。 |
| [MiniCPM-V](minicpm-v.zh.md) | ✅ | A（4/6） | 当你需要小体积、可在端侧/边缘运行的多模态（图像+视频）理解时用它——注意逐权重许可。 |
| [MiniCPM](minicpm.zh.md) | ✅ | B（5/6） | Apache-2.0 的 1–2B 文本模型，配逐运行时手册、agent 技能和公开训练数据；比起 Qwen/Gemma 少了更大的生态和 JSON 工具调用格式，换来部署全有文档，4 bit 版不调采样会复读。 |
| [Needle](needle.zh.md) | ✅ | B（4/6） | 英语专用的端侧工具调用/抽取/嵌入模型（29–121M、2-bit），解码受 grammar 约束；基座模型在否定、越界取值与域外请求上会失手。 |
| [BirdNET-Go](birdnet-go.zh.md) | ✅ | B（5/6） | 自托管的 Go 应用，用 BirdNET v2.4（可加装 Perch v2 和蝙蝠模型）给实时音频分类，把检出连同录音片段记下来；用可复现性和商用权换一个开箱即用的全天候站点——非 OSI 许可证、默认跟 nightly、单人维护。 |
| MLC LLM / ONNX Runtime | 未收录 | — | 各页对比里点到的其他端侧推理运行时（llama.cpp 与 Ollama 已收录在 `llm-inference`）。 |

## 什么该放这里

面向**本地／端侧推理**（手机、笔记本、边缘、CPU）的运行时与模型。图像／视频扩散先选 [local-image-generation](local-image-generation/INDEX.zh.md)；其他任务若由 Apple 计算栈决定部署，再选 [apple-local-inference](apple-local-inference/INDEX.zh.md)。通用运行时与专项模型即使支持 Mac，也可留在本节点。不含云端训练（见 `llm-training`），不含 RAG 检索（见 `rag-retrieval`）。
