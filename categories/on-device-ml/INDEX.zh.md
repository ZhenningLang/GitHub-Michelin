# on-device-ml

> 分类节点。在端侧/边缘设备（手机、笔记本、IoT）本地跑 ML/LLM 推理，而非云端。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 子分类 | 何时进入 | 路由 |
| --- | --- | --- |
| **local-image-generation** | 你要在自己的 GPU、Mac 或 CPU 上本地跑开源权重的图像/视频扩散模型。 | [→](local-image-generation/INDEX.zh.md) |

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **LiteRT-LM** | 想用 Google LiteRT 运行时在手机/笔记本/边缘（CPU/GPU/NPU）上跑 Gemma 级 LLM 时用它。 | B（6/6） | [→](litert-lm.zh.md) |
| **BitNet** | 当你要在 x86/ARM 笔记本上离线、快速、低能耗地用 CPU 跑原生三值（1.58-bit） LLM 时使用。 | B（5/6） | [→](bitnet.zh.md) |
| **Google AI Edge Gallery** | 当你想在真机上先体验和基准测试端侧 Gemma LLM、为是否自建集成去风险时用它。 | B（6/6） | [→](ai-edge-gallery.zh.md) |
| **TimesFM** | 当你需要在本地 CPU/GPU 上对时间序列做零样本预测、又不想逐数据集训练时用它。 | A（5/6） | [→](timesfm.zh.md) |
| **MiniCPM-V** | 当你需要小体积、可在端侧/边缘运行的多模态（图像+视频）理解时用它——注意逐权重许可。 | A（4/6） | [→](minicpm-v.zh.md) |
| **MiniCPM** | 当聊天、编码或调工具的助手必须以 1–2B 体量离线跑在笔记本、手机或 CPU 盒子上时用它（MiniCPM5，Apache-2.0，GGUF 0.66–1.56GB）——但 4 bit 版要调采样参数，并选能解析其 XML 工具调用的运行时。 | B（5/6） | [→](minicpm.zh.md) |
| **MLX / mlx-lm** | 当你在 Apple 芯片的 Mac 上试 Hugging Face 新模型，想用一个 Python 包完成生成、量化和 LoRA 微调、不必先转 GGUF 时用它——但 mlx_lm.server 不适合生产或多用户服务。 | B（6/6） | [→](mlx-mlx-lm.zh.md) |
| **Needle** | 当需要一个小体积端侧模型离线完成**英文**工具调用、类型化抽取或嵌入时用它（29–121M 参数、2-bit）——但基座模型需要微调，拒绝类请求要自建守卫。 | B（4/6） | [→](needle.zh.md) |
| **BirdNET-Go** | 当你想在树莓派 4/5 或小主机上搭一个全天候的鸟类（及蝙蝠）声音监测站，带本地网页仪表盘、多路麦克风和 RTSP 音源、MQTT 与 Home Assistant 告警时用它——但代码和模型都禁止商用（CC BY-NC-SA），默认安装跟的是单人维护的每夜构建，批量文件分析要交给别的工具。 | B（5/6） | [→](birdnet-go.zh.md) |
| **uzu** | 当你要把大模型直接跑在自己的 iOS/macOS 应用里，想要一个 Swift/Python/TS SDK 替你挑模型、下载转换好的版本并在苹果 GPU 上运行时用它——但系统要 26.4 以上，只用 Mirai 自有模型格式和托管注册服务，遥测默认开启。 | B（6/6） | [→](uzu.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [LiteRT-LM](litert-lm.zh.md) | ✅ | B（6/6） | 想用 Google LiteRT 运行时在手机/笔记本/边缘（CPU/GPU/NPU）上跑 Gemma 级 LLM 时用它。 |
| [BitNet](bitnet.zh.md) | ✅ | B（5/6） | 当你要在 x86/ARM 笔记本上离线、快速、低能耗地用 CPU 跑原生三值（1.58-bit） LLM 时使用。 |
| [Google AI Edge Gallery](ai-edge-gallery.zh.md) | ✅ | B（6/6） | 当你想在真机上先体验和基准测试端侧 Gemma LLM、为是否自建集成去风险时用它。 |
| [TimesFM](timesfm.zh.md) | ✅ | A（5/6） | 当你需要在本地 CPU/GPU 上对时间序列做零样本预测、又不想逐数据集训练时用它。 |
| [MiniCPM-V](minicpm-v.zh.md) | ✅ | A（4/6） | 当你需要小体积、可在端侧/边缘运行的多模态（图像+视频）理解时用它——注意逐权重许可。 |
| [MiniCPM](minicpm.zh.md) | ✅ | B（5/6） | Apache-2.0 的 1–2B 文本模型，配逐运行时手册、agent 技能和公开训练数据；比起 Qwen/Gemma 少了更大的生态和 JSON 工具调用格式，换来部署全有文档，4 bit 版不调采样会复读。 |
| [Needle](needle.zh.md) | ✅ | B（4/6） | 英语专用的端侧工具调用/抽取/嵌入模型（29–121M、2-bit），解码受 grammar 约束；基座模型在否定、越界取值与域外请求上会失手。 |
| [BirdNET-Go](birdnet-go.zh.md) | ✅ | B（5/6） | 自托管的 Go 应用，用 BirdNET v2.4（可加装 Perch v2 和蝙蝠模型）给实时音频分类，把检出连同录音片段记下来；用可复现性和商用权换一个开箱即用的全天候站点——非 OSI 许可证、默认跟 nightly、单人维护。 |
| [uzu](uzu.zh.md) | ✅ | B（6/6） | Mirai 用 Rust 写的引擎，配 Swift/Python/TS 绑定和手写 Metal 4 内核：报目录里的模型名，下载转换好的版本在应用内运行；只限苹果（系统 26.4+），自有模型格式、厂商注册服务、默认开启遥测，单一公司的年轻项目。 |
| MLC LLM / ONNX Runtime | 未收录 | — | 各页对比里点到的其他端侧推理运行时（llama.cpp 与 Ollama 已收录在 `llm-inference`）。 |

## 什么该放这里

面向**本地/端侧推理**（手机、笔记本、边缘、CPU）的运行时与模型。不含云端训练（见 `llm-training`），不含 RAG 检索（见 `rag-retrieval`）。
