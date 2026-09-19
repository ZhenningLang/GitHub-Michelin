# on-device-ml

> 分类节点。在端侧/边缘设备（手机、笔记本、IoT）本地跑 ML/LLM 推理，而非云端。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **LiteRT-LM** | 想用 Google LiteRT 运行时在手机/笔记本/边缘（CPU/GPU/NPU）上跑 Gemma 级 LLM 时用它。 | B（6/6） | [→](litert-lm.zh.md) |
| **BitNet** | 当你要在 x86/ARM 笔记本上离线、快速、低能耗地用 CPU 跑原生三值（1.58-bit） LLM 时使用。 | C（6/6） | [→](bitnet.zh.md) |
| **Google AI Edge Gallery** | 当你想在真机上先体验和基准测试端侧 Gemma LLM、为是否自建集成去风险时用它。 | A（5/6） | [→](ai-edge-gallery.zh.md) |
| **TimesFM** | 当你需要在本地 CPU/GPU 上对时间序列做零样本预测、又不想逐数据集训练时用它。 | B（5/6） | [→](timesfm.zh.md) |
| **MiniCPM-V** | 当你需要小体积、可在端侧/边缘运行的多模态（图像+视频）理解时用它——注意逐权重许可。 | A（4/6） | [→](minicpm-v.zh.md) |
| **Stable Diffusion WebUI** | 当你想在自有 GPU 上用本地 Web GUI 进行 Stable Diffusion 图像生成、编辑和超分时用它——但需要技术 setup 和 NVIDIA GPU。 | C（4/6） | [→](stable-diffusion-webui.zh.md) |
| **ComfyUI** | 当你想要一个模块化的节点图界面来在本地构建复杂扩散模型工作流时用它——但学习曲线陡峭，且需要大量 GPU 资源。 | B（5/6） | [→](comfyui.zh.md) |
| **MLX / mlx-lm** | Run LLMs with MLX | B（6/6） | [→](mlx-mlx-lm.zh.md) |
| **Needle** | 端侧 2-bit、8–29 MB 的工具调用/抽取/嵌入模型，解码受 schema grammar 约束，并带 confidence 分数。 | B（4/6） | [→](needle.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [LiteRT-LM](litert-lm.zh.md) | ✅ | B（6/6） | 想用 Google LiteRT 运行时在手机/笔记本/边缘（CPU/GPU/NPU）上跑 Gemma 级 LLM 时用它。 |
| [BitNet](bitnet.zh.md) | ✅ | C（6/6） | 当你要在 x86/ARM 笔记本上离线、快速、低能耗地用 CPU 跑原生三值（1.58-bit） LLM 时使用。 |
| [Google AI Edge Gallery](ai-edge-gallery.zh.md) | ✅ | A（5/6） | 当你想在真机上先体验和基准测试端侧 Gemma LLM、为是否自建集成去风险时用它。 |
| [TimesFM](timesfm.zh.md) | ✅ | B（5/6） | 当你需要在本地 CPU/GPU 上对时间序列做零样本预测、又不想逐数据集训练时用它。 |
| [MiniCPM-V](minicpm-v.zh.md) | ✅ | A（4/6） | 当你需要小体积、可在端侧/边缘运行的多模态（图像+视频）理解时用它——注意逐权重许可。 |
| [Stable Diffusion WebUI](stable-diffusion-webui.zh.md) | ✅ | C（4/6） | 本地 Web GUI，用于在自有 GPU 上进行 Stable Diffusion 图像生成、编辑和超分；需要技术 setup 和 NVIDIA GPU。 |
| [ComfyUI](comfyui.zh.md) | ✅ | B（5/6） | 模块化节点图界面，用于在本地构建复杂扩散模型工作流；学习曲线陡峭，需要大量 GPU 资源。 |
| [Needle](needle.zh.md) | ✅ | B（4/6） | 端侧 2-bit 工具调用 + 结构化抽取 + 嵌入模型，解码受 grammar 约束。 |
| llama.cpp / Ollama / MLC LLM / ONNX Runtime | 未收录 | — | 各页对比里点到的其他端侧推理运行时。 |

## 什么该放这里

面向**本地/端侧推理**（手机、笔记本、边缘、CPU）的运行时与模型。不含云端训练（见 `llm-training`），不含 RAG 检索（见 `rag-retrieval`）。
