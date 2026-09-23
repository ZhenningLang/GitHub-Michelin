---
name: Depth Anything V2
slug: depth-anything-v2
repo: https://github.com/DepthAnything/Depth-Anything-V2
category: ml-research
tags: [monocular-depth, depth-estimation, computer-vision, foundation-model, pytorch, dpt, vision-transformer]
language: Python
license: Apache-2.0
maturity: NeurIPS 2024 release, code active, ~8.3k stars (as of 2026-06)
last_verified: 2026-06-28
type: model
upstream:
  pushed_at: 2026-03-24T10:59:06Z
  default_branch: main
  default_branch_sha: a561b849ebae10a6f5ef49e26c83cbbcd36c71bf
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:42:23Z
  overall: C
  overall_score: 2.25
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 182
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 831
        last_commit_age_days: 182
        cohort: model
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
    adoption: { reason: no_package_structural }
---

# Depth Anything V2

一个单目深度估计的基础模型（NeurIPS 2024）：输入一张图，输出稠密深度图——四种基于 ViT 的模型规模，比 V1 和基于 SD 的深度模型更快更锐，围绕已发布 checkpoint 配了一个小巧的 PyTorch 推理仓库。

![depth-anything-v2 — 健康度雷达](../../assets/health/depth-anything-v2.zh.svg)

## 何时使用

你是个需要从*单张*图像取深度的 CV 工程师、机器人开发者或创意工具开发者——没有双目装置、没有 LiDAR——用于三维重建、背景分割/虚化、新视角合成、AR 遮挡，或可控的图像/视频生成。你不想训练深度模型；你想要一个开箱即用的强模型。你 `git clone`、`pip install -r requirements.txt`、下载一个 checkpoint（追求速度用 Small 25M，追求质量用 Large 335M），几行代码调 `model.infer_image(cv2_image)` 拿到一张 `HxW` 深度图。批量/视频用自带的 `run.py` / `run_video.py`，或直接从 Hugging Face Transformers 加载。需要绝对尺度而非相对深度时，还有单独的 metric-depth 模型。

你把它当作**当下默认的单目深度基础模型**，当相对深度的质量、速度、以及与 PyTorch/Transformers 的易集成，比自己造任何东西更重要时——它是这个细分领域里当前被引用最多、支持最好的选择。[推断]

## 何时不用

- **你需要主模型开箱即用的 metric 深度。** 招牌的相对深度 checkpoint 给的是*相对*深度（尺度/位移不定）；要绝对 metric 深度，必须用单独的 `metric_depth/` 模型，且那里的精度依赖领域。别以为默认输出就是以米为单位。[推断]
- **你已经有双目/LiDAR。** 标定好的双目对或深度传感器直接给出有度量基准的深度；单目模型是单相机情形的退路，不是真实深度硬件的替代。
- **许可：盯模型权重，别只看代码。** *代码*是 Apache-2.0，但按 README，**只有 Small 模型是 Apache-2.0；Base/Large/Giant 权重是 CC-BY-NC-4.0（非商用）**。对商业产品而言，较大的 checkpoint 除非另行安排否则禁用——这是最重要的一条注意事项。
- **无 GPU 的边缘端硬实时。** Large 模型很重；连 Small 也受益于 GPU。仅 CPU 的边缘端、又有紧的延迟/功耗预算，需要更小/量化的模型并实测。
- **分布外场景的正确性保证。** 它鲁棒，但仍是学习得到的模型——透明/反光表面、极端场景、异常相机都可能失败；请在你自己的数据上验证。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| Depth Anything V1 | 未收录 | 只有流水线钉死 V1 时，才选 Depth Anything V1。 | 前作；按作者说法 V2 在细节上更锐、更鲁棒——除非你有钉死 V1 的流水线，否则用 V2。 |
| MiDaS / DPT（Intel ISL） | 未收录 | 需要更早、广泛使用的单目深度模型时，选 MiDaS/DPT。 | 更早、广泛使用的单目深度模型；成熟且许可宽松，但在细节/鲁棒性上普遍被 Depth Anything V2 超过。[推断] |
| Marigold（基于 SD） | 未收录 | 需要基于扩散的深度估计时，选 Marigold。 | 基于扩散的深度；质量可以很高，但更慢、参数更多——V2 明确以更快推理 / 更少参数为目标。 |
| ZoeDepth | 未收录 | 需要带绝对尺度的 metric 单目深度时，选 ZoeDepth。 | metric 单目深度；当你专门需要绝对尺度而非相对深度时的直接替代。 |
| [CLIP](clip.zh.md) | ✅ | 需要同一货架上的视觉语言模型，而非单目深度时，选 CLIP。 | 任务不同（视觉语言），但同一货架——广泛采用的已发布基础模型，产品就是它的 checkpoint。 |

## 技术栈

- **语言：** Python。
- **框架：** PyTorch 加 torchvision；用 OpenCV 做图像 I/O；用 Gradio 做 demo 应用。
- **架构：** DPT 头接 DINOv2 ViT 编码器（vits/vitb/vitl/vitg）——四种规模，从 24.8M 到 1.3B 参数。
- **集成：** 可经 Hugging Face Transformers 加载（`depth-anything-v2` 模型文档）；存在面向 Apple 设备的 Core ML 转换（社区/官方）。

## 依赖

- **运行时：** `torch`、`torchvision`、`opencv-python`、`matplotlib`、`gradio`/`gradio_imageslider`（用于 demo）。
- **硬件：** 对 Large 模型，GPU（CUDA）是实际路径；按示例的设备选择，较小模型可在 MPS/CPU 上跑。
- **权重：** checkpoint 从 Hugging Face 单独下载（Small/Base/Large；Giant「即将推出」）；不随仓库打包。
- **可选：** 若用 `pipeline` 而非仓库自带加载器，则需 Hugging Face Transformers。

## 运维难度

**推理而言低到中。** 作为模型发布，它*用*起来很容易：装依赖、拉 checkpoint、调 `infer_image`。主要的运维考量是挑规模/延迟的权衡（Small 还是 Large）、为较大模型配 GPU，以及——真正的坑——跟踪哪个 checkpoint 的许可适合你的用途。没有服务要运维；要产品化，工作是标准的模型服务（批处理、GPU 显存、可能 ONNX/Core ML 导出），并非这个仓库特有。训练/微调是另一回事、更重，也不是常见路径。

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护（2026-06）。** 最后 push 于 2026-03；issue 流活跃（约 240 个 open，与高使用量相符）。代码仓库在发布后**积极维护**，同一脉络下有后续项目（Video Depth Anything、Prompt Depth Anything）。[推断]
- **治理 / 背书。** 由 **港大与 TikTok/字节跳动**的研究者撰写（Organization 拥有的仓库，`DepthAnything` 组织）。机构加大厂背书，加一篇 NeurIPS 2024 论文——很强的可持续性信号；路线图由研究团队主导。[推断]
- **年龄与 Lindy 判断。** 2024-06 创建（约 2 年）——**年轻**，故 Lindy 在任一方向都给不了多少先验；这个赌注靠采用度加活跃维护加背书，目前都很强，而非靠长寿。[推断]
- **采用度。** 约 8.3k star / 约 865 fork，有 Hugging Face Spaces demo、Transformers 集成、Apple Core ML 支持——作为首选单目深度模型，被广泛而迅速地采用。[未验证]
- **风险标记。** 决定性的一项是**权重的拆分许可**（Small 为 Apache-2.0，Base/Large/Giant 为 CC-BY-NC-4.0）——一个区别于 Apache-2.0 代码的商用陷阱。另外：项目年轻（履历较短），以及 README 提到的 2024 年一次短暂的 GitHub 下架（仓库已恢复）。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 8.3k star / 约 865 fork / 约 240 个 open issue；数字对时间敏感，仅供参考。
- [未验证] 模型许可拆分（Small 为 Apache-2.0；Base/Large/Giant 为 CC-BY-NC-4.0）取自 README 的 LICENSE 说明——商用前请在每个 checkpoint 的 Hugging Face 页面核实确切许可。
- [未验证]「Giant」模型标注为「即将推出」；其在任一时刻的可用性/许可应直接核查。
- [推断]「被引用最多 / 当下默认单目深度模型」是从星标加 Transformers/Core ML 集成加 NeurIPS 论文推断，并非实测排名。
- [推断]「在细节/鲁棒性上超过 MiDaS/DPT」反映作者主张加普遍反响，并非此处独立跑的基准。
