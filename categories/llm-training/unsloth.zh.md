---
name: Unsloth
slug: unsloth
repo: https://github.com/unslothai/unsloth
category: llm-training
tags: [fine-tuning, lora, qlora, triton-kernels, quantization, grpo, single-gpu, vram-efficient]
language: Python
license: Apache-2.0
maturity: "Beta releases (v0.1.x-beta line, 2026-06); very active"
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T11:05:14Z
  default_branch: main
  default_branch_sha: 2f8521ed54b20775025ce28bc9965e97d76318b3
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:33:21Z
  overall: B
  overall_score: 3.4
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: unsloth
        dependent_repos_count: 0
        downloads_last_month: 1019573
        graph_tier: E
        volume_tier: B
        cross_check_divergence: null
        homebrew_installs_90d: 274
        homebrew_tier: C
        release_downloads: 1830603
        release_assets: 140
        release_tier: B
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1028
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 55
        top1_share: 0.481
        top3_share: 0.665
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
    responsiveness: { reason: no_window_signal }
---

# Unsloth

近乎 drop-in 的微调库，用手写 Triton kernel 重写 LoRA/QLoRA/RL 训练的热点路径，在单张 GPU 上把开源 LLM 训练提速约 2x 并大幅节省显存。

![unsloth — 健康度雷达](../../assets/health/unsloth.zh.svg)

## 何时使用

你是一名开发者或独立研究者，手头只有一张消费级或工作站 GPU（比如 RTX 4090，或免费的 Colab/Kaggle T4），想在自己的数据集上微调 Llama、Qwen、Mistral、Gemma 或 gpt-oss。用原生 Hugging Face + PEFT 时，你的 QLoRA 任务总是撞上 CUDA 显存不足，或者跑一个 epoch 慢到让迭代变得痛苦。Unsloth 在近乎 drop-in 的 `FastLanguageModel` API 背后换上自家 Triton kernel（RoPE、MLP、attention、padding-free packing）和动态 4-bit 量化，于是同一个 QLoRA 任务占用更少显存、速度大约快一倍——官方宣称「最高 2x 提速、最高省 70% 显存」，GRPO 强化学习「省 80% 显存」。

当你的瓶颈是「只有一张卡」、目标是「快速、低成本迭代」时它最合适：指令微调、领域适配，或对推理类模型做 RL（GRPO/DPO）——文档称最低可在约 5GB 显存内跑 GRPO。由于它构建在 `transformers`/`trl` 之上，你的训练脚本、数据集和导出的 adapter 仍留在熟悉的 Hugging Face 生态里，并可导出为 GGUF/safetensors 供下游推理。

## 何时不用

- **多卡 / 多机分布式训练。** 普遍报道开源核心仅支持单卡，多卡扩展被锁在付费 Pro/Enterprise 层 [未验证]。注意项目自己的 README/官网又宣传「支持多卡训练」——两类说法相互冲突，安装前请按你实际拉到的版本核实，别默认免费包能做分布式。若现在就要 FSDP2/DeepSpeed 式分片，Axolotl 或 LLaMA-Factory 更稳。
- **大模型全参微调。** Unsloth 的甜点区是能塞进单卡的参数高效（LoRA/QLoRA）微调；需要分片的大规模全参微调超出了免费单卡范围。
- **不受支持的架构。** 它支持的模型列表很大但是经过筛选的；全新或冷门架构在维护者补上前可能没有优化 kernel。
- **对厂商分层 lock-in 敏感。** 头条性能数字（极高的提速/省显存倍率）和多卡都绑定在商业层；投产前要为此预留预算。
- **想要完全 config 驱动、可复现的团队工作流。** Unsloth 偏库/notebook；LLaMA-Factory（YAML + LlamaBoard UI）更面向团队与复现。
- **维护节奏风险。** 它以高频 beta 节奏紧跟快速更新的模型发布，请锁版本，因为 kernel/模型支持和 API 变动很快。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [LLaMA-Factory](llamafactory.zh.md) | ✅ | 广泛方法／模型覆盖、YAML、Web UI 和多卡比单卡速度更重要时，选 LLaMA-Factory。 | 它甚至可把 Unsloth 当后端；Unsloth 范围更窄，但单卡更快。 |
| [ART](art.zh.md) | ✅ | 训练问题是多步 agent GRPO，包含任务、奖励和 rollout 编排时，选 ART。 | ART 是 agent-first；Unsloth 是通用微调／RL 加速层。 |
| [Agent Lightning](agent-lightning.zh.md) | ✅ | 现有 agent 需要以最小代码改动从执行轨迹中做 RL 时，选 Agent Lightning。 | 它解耦 agent 执行与训练；Unsloth 优化 kernel，而不是 agent 编排。 |
| [Axolotl](axolotl.zh.md) | ✅ | 超出单卡后需要一等公民式多卡 FSDP/DeepSpeed 和多模态支持时，选 Axolotl。 | 它更适合横向扩展工作流；Unsloth 胜在单卡速度和显存。 |
| [torchtune](torchtune.zh.md) | ✅ | 原生 PyTorch recipe 和显式 `torch.compile` 控制是优先项时，选 torchtune。 | 它更显式、更底层，但模型覆盖窄于 Unsloth 的精选快速路径。 |
| HF TRL | 未收录 | Hugging Face 参考 SFT/DPO/GRPO trainer 比加速包装层更合适时，选 HF TRL。 | Unsloth 构建在 TRL 之上并用自定义 kernel 加速它。 |

## 技术栈

- **语言：** Python（外加 TypeScript 的 Studio UI 组件）。
- **核心加速：** 手写 Triton kernel（RoPE、MLP、attention）、padding-free packing、动态 4-bit 量化；FP8/16-bit/4-bit 训练路径。
- **训练方法：** LoRA、QLoRA、全参微调，以及通过近乎 drop-in 的 `FastLanguageModel`（叠加在 `transformers`/`trl` 上）做 RL（GRPO/DPO）。
- **导出/推理：** GGUF、LoRA adapter、safetensors；与 llama.cpp 集成做推理。
- **形态：** 代码库（Unsloth Core，Apache-2.0）+ 可选的无代码 Web UI（Unsloth Studio，AGPL-3.0 组件）[未验证：具体许可拆分]。

## 依赖

- PyTorch + CUDA（NVIDIA GPU；引用了 RTX 30/40/50、Blackwell、DGX；macOS 与 Intel/AMD 支持据称在扩展中）[未验证]。
- Triton（kernel 编译）。
- Hugging Face `transformers`、`peft`、`trl`、`datasets` 与 tokenizers。
- bitsandbytes 式的 4-bit 量化栈（Unsloth 自带动态 4-bit 变体）。
- llama.cpp 用于 GGUF 导出/推理。

## 运维难度

**低到中。** 走它设计的路径——单卡、一个 Colab/Kaggle/notebook 或单脚本——难度低：装好、换成 `FastLanguageModel`、开训。当你在定制硬件上跟 CUDA/Triton/PyTorch 版本矩阵搏斗、或试图突破单卡免费层天花板（多卡/全参）时，难度升到中——此处开源版的说法存在争议，可能要走付费层。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护——活跃（截至 2026-06）。** 仓库最近一次 push 在 2026-06；以紧跟新模型发布的高频 beta 节奏迭代，是活跃而非吃老本 [未验证]。代价是 churn：kernel/模型支持和 API 变动很快，请锁版本。
- **治理与背书。** 组织所有（`unslothai/`）——一家有商业 Pro/Enterprise 层的小型 VC 资助初创，而非基金会 [推断]。开源单卡核心与被锁的多卡/头条性能层共享同一条由厂商掌控的路线图；可持续性取决于公司的现金流，且免费与付费的分界线可能移动。
- **年龄与 Lindy 判断——年轻但快速证明自己（创建于 2023-11，约 2.5 年）。** 太年轻，给不了强 Lindy 先验；但约 67k star（2026-06）加上生态的重度使用，说明它已越过「到底有没有人用」这道坎；当作一个已立足但仍年轻的押注，而非十年稳态的对象 [推断]。
- **风险标记。** 开放核心：最常被引用的能力（多卡、顶级性能倍率）绑定在商业层，且「开源版支持多卡」一说存在争议（见存疑）。混合许可——Apache-2.0 核心加 AGPL-3.0 的 Studio 组件 [未验证]。在把生产流水线押在它上面之前，先为付费层留预算。

## 存疑（未验证）

- [未验证] 具体的提速/省显存倍率（「2x 提速」「省 70% 显存」「GRPO 省 80% 显存」「约 5GB GRPO」）均为厂商宣称；真实收益取决于模型、序列长度、batch 大小和 GPU。LLM 相关性能宣称不作保证。
- [未验证] 免费 Apache-2.0 包是否支持多卡训练存在争议：仓库/官网宣传多卡，而多个第三方对比称开源版仅单卡、把多卡锁在 Pro/Enterprise。请按你安装的版本核实。
- [未验证] GitHub 页面引用的 star 数约 67k（2026-06）；该生态 star 数不可靠，仅作参考。
- [未验证] 确切的「500+」支持模型数与各架构 kernel 覆盖随版本而变；以当前文档为准。
- [未验证] 第三方来源看到的 Pro/Enterprise 价格不一致；以官方定价页为准。
