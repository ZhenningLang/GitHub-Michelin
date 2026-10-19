# apple-local-inference

> 分类节点。主要部署目标是 Apple 设备，本地推理与集成路径由 MLX、Metal 或 Core ML 决定。
> ← 返回 [on-device-ml](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **TurboFieldfare** | 在 8 GB Mac 上从 SSD 流式读取专家，运行固定 Gemma 4；只支持苹果平台与指定模型。 | C（6/6） | [→](turbo-fieldfare.zh.md) |
| **FluidUse** | Swift 调专用 Core ML 决策，把表单资料匹配到真实 Mac 控件；不是通用隔离代理。 | C（5/6） | [→](fluiduse.zh.md) |
| **uzu** | 当你要把大模型直接跑在自己的 iOS/macOS 应用里，想要一个 Swift/Python/TS SDK 替你挑模型、下载转换好的版本并在苹果 GPU 上运行时用它——但系统要 26.4 以上，只用 Mirai 自有模型格式和托管注册服务，遥测默认开启。 | B（6/6） | [→](uzu.zh.md) |
| **MLX / mlx-lm** | 当你在 Apple 芯片的 Mac 上试 Hugging Face 新模型，想用一个 Python 包完成生成、量化和 LoRA 微调、不必先转 GGUF 时用它——但 mlx_lm.server 不适合生产或多用户服务。 | B（6/6） | [→](mlx-mlx-lm.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [TurboFieldfare](turbo-fieldfare.zh.md) | ✅ | C（6/6） | 固定专家缓冲区以 SSD 读取换较低常驻权重内存；要求 macOS 26 和指定 Gemma 检查点。 |
| [FluidUse](fluiduse.zh.md) | ✅ | C（5/6） | Swift 调专用 Core ML 决策，把表单资料匹配到真实 Mac 控件；不是通用隔离代理。 |
| [uzu](uzu.zh.md) | ✅ | B（6/6） | Mirai 用 Rust 写的引擎，配 Swift/Python/TS 绑定和手写 Metal 4 内核：报目录里的模型名，下载转换好的版本在应用内运行；只限苹果（系统 26.4+），自有模型格式、厂商注册服务、默认开启遥测，单一公司的年轻项目。 |
| [MLX / mlx-lm](mlx-mlx-lm.zh.md) | ✅ | B（6/6） | 当你在 Apple 芯片的 Mac 上试 Hugging Face 新模型，想用一个 Python 包完成生成、量化和 LoRA 微调、不必先转 GGUF 时用它——但 mlx_lm.server 不适合生产或多用户服务。 |

## 什么该放这里

主要围绕 Apple 设备上的 MLX、Metal 或 Core ML 选择本地推理和应用集成方案。Apple 优先不等于 Apple 专属；MLX 也记录了 CUDA/CPU 扩展。仅支持 Mac 不足以让通用运行时或专项模型归入这里。图像／视频扩散先进入 [local-image-generation](../local-image-generation/INDEX.zh.md)；其他本地推理路线留在 [on-device-ml](../INDEX.zh.md)。
