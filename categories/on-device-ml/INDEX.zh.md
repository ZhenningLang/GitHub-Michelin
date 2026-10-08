# on-device-ml

> 分类节点。在端侧/边缘设备（手机、笔记本、IoT）本地跑 ML/LLM 推理，而非云端。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **LiteRT-LM** | 想用 Google LiteRT 运行时在手机/笔记本/边缘（CPU/GPU/NPU）上跑 Gemma 级 LLM 时用它。 | B（6/6） | [→](litert-lm.zh.md) |
| **BitNet** | 当你要在 x86/ARM 笔记本上离线、快速、低能耗地用 CPU 跑原生三值（1.58-bit） LLM 时使用。 | B（5/6） | [→](bitnet.zh.md) |
| **Google AI Edge Gallery** | 当你想在真机上先体验和基准测试端侧 Gemma LLM、为是否自建集成去风险时用它。 | B（6/6） | [→](ai-edge-gallery.zh.md) |
| **TimesFM** | 当你需要在本地 CPU/GPU 上对时间序列做零样本预测、又不想逐数据集训练时用它。 | A（5/6） | [→](timesfm.zh.md) |
| **MiniCPM-V** | 当你需要小体积、可在端侧/边缘运行的多模态（图像+视频）理解时用它——注意逐权重许可。 | A（4/6） | [→](minicpm-v.zh.md) |
| **Stable Diffusion WebUI** | 当你想在 NVIDIA GPU 上用一个标签页式本地 Web UI、完整调参并借用庞大的 A1111 扩展生态做 SD 1.5/SDXL 出图时用它——但核心自 2024-07 起再无提交，新模型家族请用 ComfyUI。 | D（4/6） | [→](stable-diffusion-webui.zh.md) |
| **ComfyUI** | 当你在自己的 GPU 上用开放权重模型生成图像或视频，需要一张可复现的节点图（ControlNet、LoRA、局部重绘、放大），并且只重算改动过的部分时用它——但它没有登录、配额和租户隔离。 | B（5/6） | [→](comfyui.zh.md) |
| **MLX / mlx-lm** | 当你在 Apple 芯片的 Mac 上试 Hugging Face 新模型，想用一个 Python 包完成生成、量化和 LoRA 微调、不必先转 GGUF 时用它——但 mlx_lm.server 不适合生产或多用户服务。 | B（6/6） | [→](mlx-mlx-lm.zh.md) |
| **Needle** | 当需要一个小体积端侧模型离线完成**英文**工具调用、类型化抽取或嵌入时用它（29–121M 参数、2-bit）——但基座模型需要微调，拒绝类请求要自建守卫。 | B（4/6） | [→](needle.zh.md) |
| **stable-diffusion.cpp** | 当你要把图片/视频扩散生成做成一个不带 Python 的原生二进制，嵌进自己的应用或发到混杂的 CPU/AMD/Mac/NVIDIA 机器上时用它——但功能集固定、没有语义化版本，自带服务无鉴权且单线程排队。 | A（6/6） | [→](stable-diffusion-cpp.zh.md) |
| **BirdNET-Go** | 当你想在树莓派 4/5 或小主机上搭一个全天候的鸟类（及蝙蝠）声音监测站，带本地网页仪表盘、多路麦克风和 RTSP 音源、MQTT 与 Home Assistant 告警时用它——但代码和模型都禁止商用（CC BY-NC-SA），默认安装跟的是单人维护的每夜构建，批量文件分析要交给别的工具。 | B（5/6） | [→](birdnet-go.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [LiteRT-LM](litert-lm.zh.md) | ✅ | B（6/6） | 想用 Google LiteRT 运行时在手机/笔记本/边缘（CPU/GPU/NPU）上跑 Gemma 级 LLM 时用它。 |
| [BitNet](bitnet.zh.md) | ✅ | B（5/6） | 当你要在 x86/ARM 笔记本上离线、快速、低能耗地用 CPU 跑原生三值（1.58-bit） LLM 时使用。 |
| [Google AI Edge Gallery](ai-edge-gallery.zh.md) | ✅ | B（6/6） | 当你想在真机上先体验和基准测试端侧 Gemma LLM、为是否自建集成去风险时用它。 |
| [TimesFM](timesfm.zh.md) | ✅ | A（5/6） | 当你需要在本地 CPU/GPU 上对时间序列做零样本预测、又不想逐数据集训练时用它。 |
| [MiniCPM-V](minicpm-v.zh.md) | ✅ | A（4/6） | 当你需要小体积、可在端侧/边缘运行的多模态（图像+视频）理解时用它——注意逐权重许可。 |
| [Stable Diffusion WebUI](stable-diffusion-webui.zh.md) | ✅ | D（4/6） | 换来经典 SD 工作流里最大的扩展生态和教程积累；代价是核心冻结、AGPL-3.0 网络 copyleft、没有多用户隔离，以及要自己打理的 Python/CUDA 安装。 |
| [ComfyUI](comfyui.zh.md) | ✅ | B（5/6） | 整条管线尽在掌控、图随每张输出保存，新开放模型支持得快；代价是节点图的学习门槛、需要一块能用的 GPU，路线图由卖 Comfy Cloud 的一家公司掌握。 |
| [Needle](needle.zh.md) | ✅ | B（4/6） | 英语专用的端侧工具调用/抽取/嵌入模型（29–121M、2-bit），解码受 grammar 约束；基座模型在否定、越界取值与域外请求上会失手。 |
| [stable-diffusion.cpp](stable-diffusion-cpp.zh.md) | ✅ | A（6/6） | 基于 ggml 的 C/C++ 扩散推理引擎（SD、Flux、Qwen-Image、Wan 等），支持 GGUF 量化和 C API；用 ComfyUI/WebUI 的工作流丰富度和插件生态，换一个不带 Python、可嵌入的二进制。 |
| [BirdNET-Go](birdnet-go.zh.md) | ✅ | B（5/6） | 自托管的 Go 应用，用 BirdNET v2.4（可加装 Perch v2 和蝙蝠模型）给实时音频分类，把检出连同录音片段记下来；用可复现性和商用权换一个开箱即用的全天候站点——非 OSI 许可证、默认跟 nightly、单人维护。 |
| MLC LLM / ONNX Runtime | 未收录 | — | 各页对比里点到的其他端侧推理运行时（llama.cpp 与 Ollama 已收录在 `llm-inference`）。 |

## 什么该放这里

面向**本地/端侧推理**（手机、笔记本、边缘、CPU）的运行时与模型。不含云端训练（见 `llm-training`），不含 RAG 检索（见 `rag-retrieval`）。
