# vision-and-multimodal

> 分类节点。视觉与视觉-语言研究模型及参考代码——图像 embedding、单目深度、GAN 架构、早期视觉工具路由 agent。
> ← 返回 [ml-research](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **CLIP** | 当你想把标签写成纯文本、直接用 OpenAI 原始 checkpoint 做零样本图像分类或图文检索时用它——但它是冻结的参考实现，骨干是较老的 ViT／ResNet；要更多模型和持续维护请用 OpenCLIP 或 transformers。 | C（5/6） | [→](clip.zh.md) |
| **TaskMatrix** | 仅当你想研究 Visual ChatGPT 当年怎样用 prompt 把纯文本 ChatGPT 路由到约 20 个视觉基础模型时用它——它自 2023-06 起已停更，现代多模态大模型在单个模型里就原生做到了。 | "?"（2/6） | [→](taskmatrix.zh.md) |
| **PyTorch-GAN** | 当你想把 2014–2018 年的经典 GAN 论文各对应一个自包含 PyTorch 脚本来读（DCGAN、CycleGAN、WGAN-GP、pix2pix）时用它——但作者已自称停更，2021 年后再无提交，真实生成任务早已转向扩散模型。 | D（3/6） | [→](pytorch-gan.zh.md) |
| **Depth Anything V2** | 当你要从单张图像得到稠密深度图（三维重建、虚化、AR 遮挡、可控生成）又不想训练模型时用它——但只有 Small 权重是 Apache-2.0，Base／Large／Giant 是禁止商用的 CC-BY-NC-4.0，且默认输出是相对深度而非米制。 | C（4/6） | [→](depth-anything-v2.zh.md) |
| **Open-Sora** | 当你要在数据中心 GPU 上按完整公开的配方（代码、数据流水线、成本报告）**训练**或研究视频扩散模型时用它——2025-03 起停更，权重栈牵入 FLUX.1-dev 非商用和腾讯混元许可证。 | B（4/6） | [→](open-sora.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [CLIP](clip.zh.md) | ✅ | C（5/6） | 换来最正统、最精简的 CLIP 代码与权重；代价是模型集合固定、已被 SigLIP 和 EVA-CLIP 超越，而且只做编码，不会生成描述或回答问题。 |
| [TaskMatrix](taskmatrix.zh.md) | ✅ | "?"（2/6） | 换来一个能跑的早期工具路由 agent 历史样本；代价是要托管一整个基础模型动物园，而这份能力如今原生多模态模型和现代函数调用工具做得更好。 |
| [PyTorch-GAN](pytorch-gan.zh.md) | ✅ | D（3/6） | 换来几十个紧凑、可并排对照学习的架构；代价是没有任何库价值——不打包、无稳定接口、不含现代 GAN，层配置也不一定与论文一致。 |
| [Depth Anything V2](depth-anything-v2.zh.md) | ✅ | C（4/6） | 换来几行 PyTorch 就能用的强单目深度；代价是冻结的研究发布和受许可约束的质量——效果更好的大权重不能用于商业产品。 |
| [Open-Sora](open-sora.zh.md) | ✅ | B（4/6） | 开源 11B 文生／图生视频模型加完整训练配方；是研究产物而非维护中的产品——2025-03 起停更，每卡约 50 GB 显存，Apache-2.0 徽章覆盖不到它加载的 FLUX.1-dev／混元 VAE 权重。 |

## 什么该放这里

输入或输出是**图像**的研究模型与参考实现：视觉-语言 embedding（[CLIP](clip.zh.md)）、单目深度（[Depth Anything V2](depth-anything-v2.zh.md)）、经典 GAN 架构（[PyTorch-GAN](pytorch-gan.zh.md)），早期“LLM 调度视觉模型”的 agent 范式（[TaskMatrix](taskmatrix.zh.md)），以及连同训练配方一起公开的视频生成模型（[Open-Sora](open-sora.zh.md)）。不含从真实采集重建三维（见 `3d-reconstruction`），不含面向终端用户的图像工具（见 `media-processing`）。
