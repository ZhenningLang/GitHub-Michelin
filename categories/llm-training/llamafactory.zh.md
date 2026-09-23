---
name: LlamaFactory
slug: llamafactory
repo: https://github.com/hiyouga/LlamaFactory
category: llm-training
tags: [fine-tuning, lora, qlora, peft, rlhf, dpo, web-ui, vlm, multimodal, no-code]
language: Python
license: Apache-2.0
maturity: v0.9.5, active (2026-06)
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-06-26T07:32:10Z
  default_branch: main
  default_branch_sha: 9c0b4b38357262e53baca2b26f00499a5c243c56
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:31:04Z
  overall: B
  overall_score: 3.0
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 8
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: C
      raw:
        median_ttfr_hours: 221.5
        qualifying_issues: 27
        band: default
        window_offset_days: 9
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: llamafactory
        dependent_repos_count: 0
        downloads_last_month: 19727
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
        release_downloads: 5324
        release_assets: 6
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1213
        last_commit_age_days: 8
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 32
        top1_share: 0.341
        top3_share: 0.556
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# LlamaFactory

零代码、配置驱动的统一微调框架，把 100+ LLM/VLM 的微调收敛到一套 CLI、一个 Gradio Web UI（LlamaBoard）和一个 OpenAI 兼容 API 之下。

![llamafactory — 健康度雷达](../../assets/health/llamafactory.zh.svg)

## 何时使用

你是 ML 工程师或应用研究员，需要微调各种各样的开源模型——这周是 Qwen3，下周是 Llama-4，再后面又来个多模态 Qwen-VL——而你不想为每种架构重写一套训练循环，也不想到处翻不同的仓库。你还希望能在不同方法之间自由切换（LoRA → QLoRA → 全量微调 → DPO/PPO）而不必重新搭数据管线。LlamaFactory 用一套声明式接口解决这个问题：你注册数据集、选好模型和 `stage`/`finetuning_type`，它就在 100+ 受支持模型间把流程分发到正确的路径上。同一份 YAML 配置既能在 CLI（`llamafactory-cli train`）运行，也能在 LlamaBoard 里实时编辑——你可以先在浏览器里快速试，再把配置提交进仓库做可复现训练。

当做微调的人并不是全职训练工程师时，它同样很合适。LlamaBoard Web UI 让你不碰 Python 就能启动 SFT 或偏好优化任务、看 loss 曲线、跑简单的对话评测，降低了领域专家把模型适配到自有数据上的门槛。底层它依旧依托标准的 Hugging Face 栈（transformers/peft/trl），并叠加 FlashAttention-2、Unsloth kernel、vLLM/SGLang 等加速件，因此你得到便利层的同时，并没有和生态原语脱节。

## 何时不用

- **你要单卡极致速度/显存效率。** 据报道，在其支持的模型家族上，[Unsloth](unsloth.zh.md) 的自定义 Triton kernel 单卡更快、更省显存；LlamaFactory 可选包装 Unsloth，但自身分发层会带来初始化开销。[未验证] 具体跑分随配置变化很大。
- **你需要 agent 化 / 多轮 RL 或环境奖励训练。** LlamaFactory 面向 SFT→偏好优化（DPO/KTO/ORPO/SimPO/PPO）这条线，而非基于 rollout 的 agent RL——看 [ART](art.zh.md) 或 [Agent Lightning](agent-lightning.zh.md)。
- **你想要一个完全自己掌控、可审计的极简训练循环。** 框架抽象很厚；一旦在某个 `stage`/`template` 交互的深处出问题，排查就意味着要穿过 LlamaFactory 叠在 transformers/trl 之上的分发层。更薄的库（torchtune、HF TRL）可能更易推理。
- **配置膨胀 / 模板锁定。** 行为由模型 `template` 和庞大的配置面驱动；把自定义对话模板或非常规数据格式调对可能很繁琐，而且你会被绑定在 LlamaFactory 的抽象和发版节奏上。
- **追最前沿架构的第一天。** 新模型支持依赖 LlamaFactory 发版把 template/分发接通，可能比 transformers 原生集成滞后。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Unsloth](unsloth.zh.md) | ✅ | 单卡速度和省显存比广泛模型／方法覆盖更重要时，选 Unsloth。 | 工作流更窄，多卡故事更弱，但自定义 kernel 的 LoRA/QLoRA 效率更强。 |
| [ART](art.zh.md) | ✅ | 目标是带 GRPO 式 rollout 的 agentic RL，而不是 SFT 或偏好微调时，选 ART。 | 它解决的是从 rollout 训练 agent，不是通用微调工作台。 |
| [Agent Lightning](agent-lightning.zh.md) | ✅ | 需要从现有 agent 自身执行轨迹中训练时，选 Agent Lightning。 | 它是 agent-RL 基础设施，不是通用 SFT/LoRA 工具箱。 |
| [axolotl](axolotl.zh.md) | ✅ | 需要 YAML 驱动、多卡优先，并开箱带 FSDP/DeepSpeed 的生产训练时，选 axolotl。 | 它更偏可复现生产运行；LlamaFactory 多了 Web UI 和更广的零代码面。 |
| [torchtune](torchtune.zh.md) | ✅ | 精简、原生 PyTorch、端到端自己掌控，比大型框架更重要时，选 torchtune。 | 开箱能力更少、无 Web UI，但更容易推理。 |
| HF TRL | 未收录 | 想要底层 SFT/DPO/PPO trainer，并愿意自己接线时，选 HF TRL。 | 比 LlamaFactory 更可控、抽象更少，但集成工作更多。 |
| Swift(ModelScope) | 未收录 | ModelScope 生态更契合，且同样需要广覆盖微调框架时，选 Swift。 | 覆盖面与 LlamaFactory 重叠；生态偏好是决定性取舍。 |

## 技术栈

- **语言：** Python（仓库约 99%）。
- **核心：** Hugging Face `transformers`、`peft`、`trl`、`accelerate`、`datasets`、`torch`。
- **UI/API:** Gradio(LlamaBoard Web UI);OpenAI 兼容 HTTP API 服务。
- **加速：** FlashAttention-2、可选 Unsloth kernel、可选量化（bitsandbytes / GPTQ / AWQ）、DeepSpeed 与 FSDP 分布式训练、vLLM / SGLang 推理。
- **方法：** 预训练、SFT、奖励建模、PPO、DPO、KTO、ORPO、SimPO；全量 / freeze / LoRA / QLoRA / OFT / QOFT。
- **跟踪：** Weights & Biases、SwanLab、TensorBoard。

## 依赖

- **运行时：** Python ≥ 3.11;PyTorch ≥ 2.0（推荐 2.6）。任何真实训练都需要 CUDA GPU（CPU 仅适合最简单的冒烟测试）；支持昇腾 NPU。
- **必需 Python 依赖（v0.9.5）:** `transformers` ≥ 4.49、`peft` ≥ 0.14、`trl` ≥ 0.8.6、`accelerate` ≥ 0.34、`datasets` ≥ 2.16、`torchvision` ≥ 0.15（版本依 PyPI 元数据，推荐 pin 更高）。
- **可选分组：** `deepspeed`、`bitsandbytes`、`vllm`、`flash-attn`、`galore`、`badam`、`awq`/`gptq`、metrics/tracking 额外项——通过 pip extras 安装（`pip install "llamafactory[...]"`）。
- **安装：** `pip install llamafactory`，或官方 Docker 镜像 `hiyouga/llamafactory`。

## 运维难度

**低到中。** 走顺路径时——单卡、受支持模型、通过 LlamaBoard 或一行 CLI 跑 LoRA/QLoRA——它是把微调跑起来最简单的方式之一，Docker 镜像也消除了大部分环境痛点。难度升到**中**的场景：多卡/分布式（DeepSpeed ZeRO stage / FSDP / Ray 配置会和库版本、显存交互，是常见的不兼容来源）、自定义对话模板或非标准数据格式，以及 PyTorch 训练生态固有的 CUDA/flash-attn/bitsandbytes 版本匹配摩擦。

## 健康度与可持续性

- **响应速度**：Grade C——中位首次响应时间 221.5 小时，基于 27 个 qualifying issues/PRs。
- **维护——非常活跃（截至 2026-06）。** 仓库 2026-06 有推送；最新 release v0.9.5 据称 2026-05-30，tracker 繁忙（约 1k 未决 issue——偏高，但与约 72k star 和快速扩张的模型矩阵成比例）。未归档。[未验证]
- **治理与 bus factor——单一维护者，是个实打实的标记。** 仓库由 **User 持有**（`hiyouga`），却背着约 72k star——这是典型的 bus-factor 信号：巨大的采用量集中在一个人的账号上，看不到基金会或公司结构。虽有贡献者社区，但方向由这位具名 owner 把控；一旦该维护者退场，延续性就不确定。[推断]
- **年龄与 Lindy——中等，趋势向强。** 创建于 2023-05，约 3 年且持续高强度活跃——它已成为开源模型微调的事实默认之一，即便绝对年龄尚轻，这也是采用驱动的强 Lindy 信号。耐久性的疑问在治理（见上），而非活跃度。
- **采用与生态。** 是使用最广的 SFT/LoRA 前端之一；模型/方法覆盖广，有 Web UI（LlamaBoard）、Docker 镜像，且依托标准 HF 栈（transformers/peft/trl），与生态连接良好而非孤岛。
- **风险标记——首要是 bus factor。** Apache-2.0，不断言重新授权/CVE 历史。最主要的风险是这个高风险、被广泛依赖的仓库的单一维护者治理；次要风险是 template/配置锁定，以及对全新架构第一天支持的滞后（见「何时不用」）。

## 存疑（未验证）

- [未验证] 据称 v0.9.5 发布于 2026-05-30；截至 2026-06 star 约 72.5k——本生态的 GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 与 Unsloth/axolotl/torchtune 的具体吞吐/显存对比来自第三方博客跑分，随配置、模型、硬件差异极大；无一方官方保证。
- [推断] 受支持的模型/方法集合随版本变动；“100+ 模型”是项目自己的表述——依赖某具体模型前请对照当前仓库核实其支持情况。
