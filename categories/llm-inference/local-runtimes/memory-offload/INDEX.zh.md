# memory-offload

> 分类节点。模型权重超过显存或内存时，用逐层读取、专家缓存，或跨存储层级的 CPU／GPU 计算进行本地推理。
> 返回 [local-runtimes](../INDEX.zh.md) · 根路由：[分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Strata** | 个人工作站要用 CPU 与 GPU 分担专家计算、运行受支持的大于显存的 Qwen 或 DeepSeek 模型时考虑；接受较大内存与 SSD 需求，以及仅 40 天、作者主导的历史。 | B（5/6） | [→](strata.zh.md) |
| **AirLLM** | 当模型在你需要的形态下装不进显卡、而墙钟时间免费时用它——把检查点从磁盘逐层流式读取的库，显存只需一层的开销，代价是秒到分钟级的每 token 等待。 | B（6/6） | [→](airllm.zh.md) |
| **FreeToken** | 当一台 NVIDIA 台式机要把比显存还大的 MoE 模型提供给你的编程智能体时用它——专家放内存、显卡只做缓存——接受一个约两个月大、只支持 Linux 加 NVIDIA、接口无鉴权的 v0.1.x 引擎。 | B（6/6） | [→](freetoken.zh.md) |
| **DwarfStar (ds4)** | 当你有一台 96 GB 以上的 Mac、DGX Spark 或 Strix Halo 主机，想让少数几个前沿 MoE 模型（DeepSeek V4、GLM 5.x、Qwen3.8）在本地驱动编程智能体、内存不够时溢出到固态硬盘时用它——接受一个五个月大、单人维护、没有发布版本、只认自家 GGUF 文件的引擎。 | B（6/6） | [→](ds4.zh.md) |
| **Edge0** | 当你想在 16–24 GB 的 Mac（或手机）上跑 35B 档的 MoE 模型、卡住你的是内存而不是模型选择时用它——专家从固态硬盘流式读取，并由训练过的预测器提前一步取来——接受只有两个预览模型、相对 fp16 有少量精度损失、以及一个只有一个月大且没有发布版本的仓库。 | C（6/6） | [→](edge0.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Strata](strata.zh.md) | 已收录 | B（5/6） | 模型专用分层内存、桌面与终端、编程兼容接口；代价是模型包范围窄、容量依硬件变化、存储大且治理年轻。 |
| [AirLLM](airllm.zh.md) | ✅ | B（6/6） | 逐层流式读取的库，靠设备上只留一层在 4–12GB 小卡上跑 70B/671B 级模型；代价是每 token 都要读盘（用户实测 3B 模型 28.6 秒/token），且压缩选项实测更慢而不是更快。 |
| [FreeToken](freetoken.zh.md) | ✅ | B（6/6） | 把专家放在内存、自动分配显卡上的专家缓存，让一张消费级 NVIDIA 显卡跑前沿 MoE 检查点（safetensors），提供 OpenAI／Anthropic 接口和接编程智能体的 `ft launch`；只支持 Linux 加 NVIDIA，内存要装下全部专家，v0.1.x 格式常变，HTTP 接口无鉴权。 |
| [DwarfStar (ds4)](ds4.zh.md) | ✅ | B（6/6） | 只为少数几个前沿 MoE 模型手工适配的 C 引擎，覆盖 Metal、CUDA 和 ROCm，带 2 比特专家量化、模型比内存大时的 SSD 流式读取、双机 RDMA 张量并行和 OpenAI／Anthropic 接口；只加载自家 GGUF，没有发布版本，单人维护，接口无鉴权。 |
| [Edge0](edge0.zh.md) | ✅ | C（6/6） | 用训练过的预路由头加 Recover-LoRA 从固态硬盘流式读取 MoE 专家，35B 档在 Apple 芯片上峰值活跃内存约 3 GiB，并配有 iOS／Android／macOS／Windows 应用；只能跑自家两个预览检查点，Python 框架只支持 macOS，mlx 版本锁死，服务端单槽串行且无鉴权。 |

## 什么该放这里

决定性约束是**权重装不进单一存储层级**，需要权重流式读取或 CPU／GPU 专家卸载的本地运行时。这不承诺低主机内存占用：FreeToken 仍把全部专家放在内存，AirLLM 也覆盖稠密模型。仅对 KV 缓存分层，以及通用本地模型管理，留在 [local-runtimes](../INDEX.zh.md)。
