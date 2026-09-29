# vision-and-multimodal

> 分类节点。视觉与视觉-语言研究模型及参考代码——图像 embedding、单目深度、GAN 架构、早期视觉工具路由 agent。
> ← 返回 [ml-research](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **CLIP** | 当你需要零样本图像分类或图文互检 embedding 时用它——原始冻结参考实现；OpenCLIP 有更多权重。 | C（5/6） | [→](clip.zh.md) |
| **TaskMatrix** | 仅用于研究早期视觉工具路由 agent（Visual ChatGPT）——约 2024 年起已停更，别在其上构建。 | "?"（2/6） | [→](taskmatrix.zh.md) |
| **PyTorch-GAN** | 用来读干净的 GAN 参考实现学架构——2024 年起停更、已被扩散模型取代，不是生产代码。 | D（3/6） | [→](pytorch-gan.zh.md) |
| **Depth Anything V2** | 当需要当下默认的单目深度基础模型从单张图估深度（PyTorch／Transformers）时用它——仅 Small 权重为 Apache-2.0，Base／Large／Giant 是 CC-BY-NC-4.0（非商用）。 | C（4/6） | [→](depth-anything-v2.zh.md) |
| **Open-Sora** | 当你要在数据中心 GPU 上按完整公开的配方（代码、数据流水线、成本报告）**训练**或研究视频扩散模型时用它——2025-03 起停更，权重栈牵入 FLUX.1-dev 非商用和腾讯混元许可证。 | B（4/6） | [→](open-sora.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [CLIP](clip.zh.md) | ✅ | C（5/6） | 当你需要零样本图像分类或图文互检 embedding 时用它——原始冻结参考实现；OpenCLIP 有更多权重。 |
| [TaskMatrix](taskmatrix.zh.md) | ✅ | "?"（2/6） | 仅用于研究早期视觉工具路由 agent（Visual ChatGPT）——约 2024 年起已停更，别在其上构建。 |
| [PyTorch-GAN](pytorch-gan.zh.md) | ✅ | D（3/6） | 用来读干净的 GAN 参考实现学架构——2024 年起停更、已被扩散模型取代，不是生产代码。 |
| [Depth Anything V2](depth-anything-v2.zh.md) | ✅ | C（4/6） | 当需要当下默认的单目深度基础模型从单张图估深度（PyTorch／Transformers）时用它——仅 Small 权重为 Apache-2.0，Base／Large／Giant 是 CC-BY-NC-4.0（非商用）。 |
| [Open-Sora](open-sora.zh.md) | ✅ | B（4/6） | 开源 11B 文生／图生视频模型加完整训练配方；是研究产物而非维护中的产品——2025-03 起停更，每卡约 50 GB 显存，Apache-2.0 徽章覆盖不到它加载的 FLUX.1-dev／混元 VAE 权重。 |

## 什么该放这里

输入或输出是**图像**的研究模型与参考实现：视觉-语言 embedding（[CLIP](clip.zh.md)）、单目深度（[Depth Anything V2](depth-anything-v2.zh.md)）、经典 GAN 架构（[PyTorch-GAN](pytorch-gan.zh.md)），早期“LLM 调度视觉模型”的 agent 范式（[TaskMatrix](taskmatrix.zh.md)），以及连同训练配方一起公开的视频生成模型（[Open-Sora](open-sora.zh.md)）。不含从真实采集重建三维（见 `3d-reconstruction`），不含面向终端用户的图像工具（见 `media-processing`）。
