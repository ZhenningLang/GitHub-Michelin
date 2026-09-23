---
name: Stable Diffusion WebUI
slug: stable-diffusion-webui
repo: https://github.com/AUTOMATIC1111/stable-diffusion-webui
category: on-device-ml
tags: [diffusion-model, image-generation, gradio, pytorch, gpu, local-inference]
language: Python
license: AGPL-3.0
maturity: v1.x, active, 164k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-03-02T07:00:53Z
  default_branch: master
  default_branch_sha: 82a973c04367123ae98bd9abdf80d9eda9b910e2
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:49:50Z
  overall: C
  overall_score: 1.6
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 787
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 92.2
        qualifying_issues: 3
        band: relaxed_solo
        window_offset_days: 3
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: null
        canonical_package: null
        release_downloads: 5810113
        release_assets: 5
        release_tier: B
        signal_basis: releases
    longevity:
      grade: E
      raw:
        repo_age_days: 1492
        last_commit_age_days: 787
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: D
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    governance: { reason: unattributable }
---

# Stable Diffusion WebUI

基于 Gradio 构建的 Stable Diffusion 图像生成 Web 界面，支持 txt2img、img2img、局部重绘、扩图、超分及丰富的插件生态，面向本地 GPU 推理。

![Stable Diffusion WebUI — 健康度雷达](../../assets/health/stable-diffusion-webui.zh.svg)

## 何时使用

你是一名创作者、研究者或开发者，想在自有硬件上用文本提示生成图像或编辑现有图像。你需要一个本地 Web UI，可以在里面写提示词、调整采样参数、做局部重绘来移除或添加对象、运行 img2img 进行风格迁移，并用文本反演训练自定义嵌入。你选择 Stable Diffusion WebUI 而不是 ComfyUI，因为你想要传统的标签页界面而非节点图；你选它而不是 InvokeAI，因为它的扩展生态更大、文档更丰富；你偏好它而不是 Fooocus，因为你需要完整的参数控制而非简化预设。你有一块至少 6–8 GB 显存的 NVIDIA GPU，并熟悉安装 Python 包和管理模型 checkpoint。你安装 WebUI，下载 Stable Diffusion checkpoint，打开浏览器标签页即可开始生成——无需云积分、无需 API key，对模型和输出完全可控。

## 何时不用

- **纯 CPU 推理。**如果你没有 GPU 却需要运行 diffusion 模型，请改用 Midjourney 或 DALL-E 等云 API，而不是 Stable Diffusion WebUI，因为 diffusion 模型在 CPU 上运行极慢（单张图需数分钟），本工具为 CUDA GPU 设计。
- **未核查 AGPL-3.0 的商业用途。**如果你需要本地运行且对商业衍生限制更宽松的 diffusion 工具，请改用 ComfyUI（GPL-3.0，copyleft 范围不同）或云 API，而不是 Stable Diffusion WebUI，因为它的 AGPL-3.0 带有强网络 copyleft 义务，可能影响你的分发计划。
- **零配置或非技术用户。**如果你想要一键消费级体验，不想管理 Python、CUDA 和模型权重，请改用 Fooocus 或 Midjourney 等云服务，而不是 Stable Diffusion WebUI，因为安装需要 Python、PyTorch、CUDA 驱动，并管理数 GB 的模型文件。
- **团队多用户部署。**如果你需要内置 RBAC、队列管理或用户隔离的共享服务器，请改用 ComfyUI（队列管理更好）或托管云 API，而不是 Stable Diffusion WebUI，因为它没有原生多用户隔离，并发用户会互相干扰生成任务和设置。
- **偏好托管云服务。**如果你不想管理 GPU、驱动和模型文件，想要托管 API，请改用 Midjourney、DALL-E 或 Stable Diffusion API 服务，而不是 Stable Diffusion WebUI，因为它严格自托管。
- **严格可复现需求。**如果你需要跨机器可复现、版本可控的工作流，请改用 ComfyUI 搭配 JSON 工作流导出，或以编程方式使用 Diffusers（Hugging Face），而不是 Stable Diffusion WebUI，因为它暴露了数百个参数、采样器选择和扩展交互，在不同 PyTorch/CUDA 版本下复现完全一致很困难。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [ComfyUI](comfyui.zh.md) | ✅ | 面向 diffusion 的节点式模块化工作流引擎。 | ComfyUI 通过节点图提供更深度定制，更适合批量管线；WebUI 对 casual 探索更友好，界面更简单传统。 |
| InvokeAI | 未收录 | 更精致的创意画布，支持统一画布与图层。 | 更聚焦艺术工作流，自带画布；扩展生态不如 WebUI 丰富。 |
| Fooocus | 未收录 | 简化的一键式 UI，强调易用性。 | 预设精简、控制项最少；对新手友好，但对高级用户限制较大。 |
| DiffusionBee | 未收录 | macOS 原生 Stable Diffusion 桌面应用。 | 无命令行或扩展生态；针对 Apple Silicon 优化，但平台锁定。 |
| Midjourney / DALL-E | 未收录 | 闭源、纯云端图像生成服务。 | 专有模型、订阅制、无本地控制；WebUI 开源且在你自己的 GPU 上运行。 |

## 技术栈

- **Python**——主要实现语言
- **Gradio**——前端 Web UI 框架
- **PyTorch**——模型推理的深度学习框架
- **CUDA**——通过 NVIDIA 驱动进行 GPU 加速
- **Stable Diffusion 模型**——运行时加载的社区 checkpoint、LoRA、嵌入和 VAE

## 依赖

- **NVIDIA GPU**，至少 6 GB 显存（大模型和高分辨率推荐 8 GB+）
- **Python 3.10+** 及匹配的 PyTorch/CUDA 版本
- **模型 checkpoint**——从社区 hub（如 Civitai、Hugging Face）下载的数 GB `.safetensors` 或 `.ckpt` 文件
- **可选：xformers**——用于内存高效 attention 和加速
- **可选：GFPGAN、CodeFormer、RealESRGAN**——用于 Extras 标签页的人脸修复和超分

## 运维难度

**中等。** 基础安装有一键脚本，但真正的负担在于保持 Python 环境、PyTorch、CUDA 驱动和扩展生态的兼容性。扩展更新可能在 `git pull` 后破坏 WebUI，模型文件占用数十 GB 磁盘空间。GPU 温度管理、显存限制和 batch size 调优是持续的关注点。对个人工作站而言可管理；对共享服务器或生产管线，要预期频繁排障。

## 健康度与可持续性
- **维护活跃度**：Grade E——最近 13 周中 0 周有提交；最后提交距今 787 天。
- **响应速度**：Grade A——中位首次响应时间 92.2 小时，基于 3 个 qualifying issues/PRs。
- **采用广度**：无法计算——unknown。
- **长青度**：Grade E——仓库已创建 1492 天。
- **治理集中度**：无法计算——unknown。
- **许可风险**：Grade D——AGPL-3.0 许可证。
## 存疑（未验证）

- [未验证] `AUTOMATIC1111` 用户账户的精确维护状态及其持续可用性未公开记录；bus factor 是真实关切。
- [未验证] 2026-03-02 的上次推送日期意味着验证时已有约 4 个月空白；在假设项目仍保持此前节奏前，请核实当前活跃度。
- [未验证] 单个模型 checkpoint 和扩展带有各自的许可和安全过滤器；工具的 AGPL-3.0 不约束你下载的权重。
- [推断] 164k star 数既反映真实受欢迎度，也来自 2022–2023 的 AI 绘画热潮；部分曝光由炒作驱动，而非当前活跃用户信号。
- [未验证] 具体显存需求因模型大小、分辨率和启用的扩展差异巨大；"6–8 GB" 是经验法则，非保证。
