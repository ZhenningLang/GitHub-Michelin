# local-image-generation

> 分类节点。在自己的 GPU、Mac 或 CPU 上本地跑开源权重的图像/视频扩散模型——网页界面、节点图工作流，或嵌进自家应用的原生引擎。
> ← 返回 [on-device-ml](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Stable Diffusion WebUI** | 当你想在 NVIDIA GPU 上用一个标签页式本地 Web UI、完整调参并借用庞大的 A1111 扩展生态做 SD 1.5/SDXL 出图时用它——但核心自 2024-07 起再无提交，新模型家族请用 ComfyUI。 | D（4/6） | [→](stable-diffusion-webui.zh.md) |
| **ComfyUI** | 当你在自己的 GPU 上用开放权重模型生成图像或视频，需要一张可复现的节点图（ControlNet、LoRA、局部重绘、放大），并且只重算改动过的部分时用它——但它没有登录、配额和租户隔离。 | B（5/6） | [→](comfyui.zh.md) |
| **stable-diffusion.cpp** | 当你要把图片/视频扩散生成做成一个不带 Python 的原生二进制，嵌进自己的应用或发到混杂的 CPU/AMD/Mac/NVIDIA 机器上时用它——但功能集固定、没有语义化版本，自带服务无鉴权且单线程排队。 | A（6/6） | [→](stable-diffusion-cpp.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Stable Diffusion WebUI](stable-diffusion-webui.zh.md) | ✅ | D（4/6） | 换来经典 SD 工作流里最大的扩展生态和教程积累；代价是核心冻结、AGPL-3.0 网络 copyleft、没有多用户隔离，以及要自己打理的 Python/CUDA 安装。 |
| [ComfyUI](comfyui.zh.md) | ✅ | B（5/6） | 整条管线尽在掌控、图随每张输出保存，新开放模型支持得快；代价是节点图的学习门槛、需要一块能用的 GPU，路线图由卖 Comfy Cloud 的一家公司掌握。 |
| [stable-diffusion.cpp](stable-diffusion-cpp.zh.md) | ✅ | A（6/6） | 基于 ggml 的 C/C++ 扩散推理引擎（SD、Flux、Qwen-Image、Wan 等），支持 GGUF 量化和 C API；用 ComfyUI/WebUI 的工作流丰富度和插件生态，换一个不带 Python、可嵌入的二进制。 |

## 什么该放这里

在本地硬件上跑开源权重扩散模型、产出图片或视频的界面、工作流引擎和推理库。不收托管的出图服务；不收产出可编辑设计稿的 AI 设计工具（见 `ai-design-generation`）；不收训练扩散模型的研究代码（见 `ml-research`）。
