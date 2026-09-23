---
name: BitNet
slug: bitnet
repo: https://github.com/microsoft/BitNet
category: on-device-ml
tags: [1-bit-llm, ternary, cpu-inference, quantization, llama-cpp, edge-ai, bitnet-b1.58, microsoft]
language: Python (tooling) + C++ kernels
license: MIT
maturity: No tagged releases; commit-versioned, last push 2026-03-10; created 2024-08; Microsoft-maintained (as of 2026-06-26)
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-03-10T07:49:47Z
  default_branch: main
  default_branch_sha: 01eb415772c342d9f20dc42772f1583ae1e5b102
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:48:52Z
  overall: B
  overall_score: 2.5
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 57
        active_weeks_13: 3
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 95.2
        qualifying_issues: 11
        band: default
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: C
      raw:
        repo_age_days: 778
        last_commit_age_days: 57
        cohort: framework
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.579
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# BitNet

微软官方的 **1-bit / 1.58-bit（三值）** LLM 推理框架（`bitnet.cpp`）——一个基于 llama.cpp 派生的运行时，配自研 CPU 内核（I2_S / TL1 / TL2），让 BitNet-b1.58-2B-4T 这类三值模型在 x86 与 ARM CPU 上跑得又快又省电。仅推理，不含训练。

![bitnet — 健康度雷达](../../assets/health/bitnet.zh.svg)

## 何时使用

你在给一个桌面应用加本地助手功能，而它要发给各种普通笔记本——有 Intel/AMD 的 x86，有 ARM（Apple 芯片、少量 Windows-on-ARM），往往没有可用 GPU，空闲内存只有 4–8GB。你已经决定不走云端：数据敏感、要能离线用、也不想让每次调用的 API 账单随用户量线性增长。一个普通 7B 的 4-bit GGUF 模型在低端 CPU 上仍然偏重，而能耗/续航也很要紧——后台功能一转风扇用户就会抱怨。

于是你选 BitNet。你挑一个**真正按三值训练**的模型——官方的 BitNet-b1.58-2B-4T，以及 Falcon3、Llama3-8B-1.58 等社区移植版——用仓库的 setup 脚本转换好，让 `bitnet.cpp` 的 I2_S/TL1/TL2 内核去跑它。因为权重是三值的，矩阵乘法变成以查表/加法为主的运算，正好被自研内核吃透：CPU 上相比标准量化基线能拿到 README 宣称的数倍加速和大幅能耗下降，而小模型也能舒服地塞进你的内存预算。框架本身是 llama.cpp 的薄派生层，所以 `llama-cli` 式运行时和 GGUF 工具链都很眼熟。

## 何时不用

- **你不能换模型。** BitNet 只加速**训练时就是三值**的模型（BitNet-b1.58 系、特定的 Falcon3/Llama3-1.58 移植）。你没法拿任意 Hugging Face 上的 FP16/4-bit 模型来获得加速——这是硬约束，不是可调旋钮。通用 GGUF 模型请用原版 llama.cpp。
- **你要一个冻结、受支持的运行时。** 它没有打 tag 的 release，靠 git commit 版本化；README 把 GPU/NPU 路径标为“即将/独立文档”。它更像一个研究级参考实现，而非稳定的产品 SDK。请 pin 住某个 commit 并预期会有变动。
- **你要最高精度或大模型。** 1.58-bit 三值是拿质量换体积/速度；目前支持良好的模型大概在 2–8B 封顶，同尺寸下三值小模型比 4-bit 更容易幻觉和格式出错。它面向便宜、短、结构化的 CPU 负载，而非顶尖推理。
- **你以 GPU/移动端为主目标。** 这是 CPU 优先的框架。GPU 支持存在但次要，没有一流的 Android/iOS SDK。要移动端 LLM 的工程体验，请用移动原生运行时（见横向对比）。
- **你要开箱即用的应用或聊天界面。** 它是 CMake/Clang 从源码构建的工具链加一个 CLI，不是面向终端用户的应用——UX 要你自己搭。
- **要最新模型覆盖。** 新的三值模型得有人把转换/内核路径接好才能用；支持列表是小而精选的，不是“任何新模型当天可用”。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [llama.cpp](../llm-inference/local-runtimes/llama-cpp.zh.md) | ✅ | 需要 BitNet 所派生的通用 GGUF 运行时时，选 llama.cpp。 | BitNet 所派生的通用 CPU/GPU GGUF 运行时；能跑*任意*量化模型且远更成熟，但它的通用 1.5/2-bit 量化比不上 BitNet 为原生 1.58-bit 模型专门写的三值内核。 |
| [LiteRT-LM](litert-lm.zh.md) | ✅ | 需要谷歌移动优先的端侧 LLM 运行时时，选 LiteRT-LM。 | 谷歌移动优先的端侧 LLM 运行时（以 Gemma 为主，Android/iOS/NPU）。移动 SDK 与加速器生态更好；但不像 BitNet 那样专攻三值 1-bit 模型与 CPU 能效。 |
| [Google AI Edge Gallery](ai-edge-gallery.zh.md) | ✅ | 需要 Android 端侧模型演示应用/目录而非 CPU 推理引擎时，选 Google AI Edge Gallery。 | 一个在 Android 上试玩端侧模型的演示应用/目录，不是 CPU 推理引擎——层次完全不同；与 BitNet 互补而非替代。 |
| Microsoft T-MAC | 未收录 | 需要 BitNet 底层低 bit CPU 内核库时，选 Microsoft T-MAC。 | BitNet 所借鉴查表方法的底层低 bit CPU 内核库；它是内核/库层，而 BitNet 是封装好的端到端三值推理框架。 |
| [MLX / mlx-lm（Apple）](mlx-mlx-lm.zh.md) | ✅ | 需要 Apple 芯片上快速推理和干净 Python/Swift 体验时，选 MLX。 | Apple 芯片上快速推理，Python/Swift 体验干净、模型覆盖广，但仅限 Apple，且不专门针对三值 1-bit 权重。 |
| [Unsloth](../llm-training/unsloth.zh.md) / GPTQ-AWQ 系 | 部分已收录 | 需要把普通模型事后量化到 4-bit 时，选 Unsloth 或 GPTQ/AWQ。 | 把普通模型事后量化到 4-bit；适用面广，但达不到 1.58-bit 原生的效率——量化哲学不同（事后压缩 vs 训练即三值）。 |

## 技术栈

- **运行时核心：** C++——**llama.cpp** 的派生/分叉，复用其 GGUF 格式与 CLI/server 脚手架。
- **自研内核：** `I2_S`（2-bit 对称，x86 + ARM）、`TL1`（三值查表，ARM）、`TL2`（三值查表，x86）；查表法源自微软 **T-MAC**。
- **工具链：** Python 的 setup/转换脚本（`setup_env.py`、`run_inference.py`），用 Hugging Face CLI 下载模型。
- **构建：** CMake + Clang/LLVM 工具链。
- **目标平台：** x86 与 ARM CPU 一流支持；GPU 路径另有文档；NPU 列为即将支持。

## 依赖

- **构建工具链：** Python ≥ 3.9、CMake ≥ 3.22、**Clang/LLVM ≥ 18**（一个相对较新的编译器——常见的安装坑）；推荐 Conda。
- **模型：** 受支持格式的*三值*模型——BitNet-b1.58-2B-4T（官方），或社区移植（Falcon3 1B–10B、Falcon-E、Llama3-8B-1.58、bitnet_b1_58-large/3B），通过 Hugging Face CLI 拉取并用仓库脚本转换。
- **硬件：** x86 或 ARM CPU；CPU 路径不需要 GPU。内存随模型大小变化（2–3B 三值模型很小，但仍需几 GB）。
- **无包安装**——引擎要从源码构建；没有 `pip install bitnet` 之类的运行时包。

## 运维难度

**中等。** 没有可 pip 安装的引擎：你要 clone、配 Conda 环境、装 **Clang ≥ 18** 和 CMake ≥ 3.22（Clang 版本要求与按平台选内核——ARM 用 TL1、x86 用 TL2、I2_S 通吃——是主要摩擦点），再跑 setup 脚本转换/量化模型并用 CMake 构建。构建完成后，日常用 CLI 推理很直接，小模型对资源也友好。更大的运维风险来自*项目*本身而非运行时：没有打 tag 的 release（要 pin commit）、模型列表小而精选、GPU/NPU 路径仍在成熟中——所以把升级和平台扩展当成移动靶子对待。

## 健康度与可持续性

- **响应速度**：Grade B——中位首次响应时间 98.8 小时，基于 7 个 qualifying issues/PRs。
- **维护（2026-06）：** 最后 push 在 2026-03-10——核验时已闲置约 3 个月，因此运行时读起来更像**滑行（coasting）**而非每周活跃迭代。[推断] 没有打 tag 的 release，节奏只能从 commit 新近度判断，而非发版流。
- **治理 / 背书：** 微软所有（`microsoft/BitNet`，Organization）。[推断] 这消除了单一维护者的巴士因子风险，但微软也是个连环砍项目的厂商——这里的厂商背书表示“一个被维持的研究参考实现”，而非产品化、带 SLA 的 SDK。
- **年龄与 Lindy（创建于 2024-08，约 2 年）：** 年轻但仍足够活跃，不算 Lindy 失败，但太新、不足以成为已被验证的长寿赌注。[推断] 其价值押在 BitNet-b1.58 研究线能否持续上；当作**有前景但未被验证**的基础设施看待。
- **采用度：** 约 39k star（易波动，见存疑）说明关注度很强，但精选的三值模型列表与 CPU 优先的范围让真实生产采用面偏窄。[未验证]
- **风险标记：** MIT 许可（无重新许可风险）。当前的活跃风险是 commit 版本化带来的变动（要 pin commit）、受支持模型面很小，以及 GPU/NPU 路径仍在成熟。[推断]

## 存疑（未验证）

- [未验证] 加速与能耗数据（ARM 约 1.37–5.07x / 省 ~55–70% 能耗；x86 约 2.37–6.17x / 省 ~72–82% 能耗；后续内核“+1.15–2.1x”；单 CPU 跑 100B 模型“5–7 tok/s”）是项目 README 自报、对照未指明的基线——本页未独立复现；随 CPU、模型、内核变化。
- [未验证] star 数约 39.5k、fork 约 3.6k（GitHub API，2026-06-26）——star 数不可靠且对日期敏感，仅作参考。
- [推断] 2026-06-26 未查到任何 GitHub release/tag，故项目疑似按 commit 版本化；“稳定 API”状态与有意义的版本号因此是从仓库状态推断，非官方声明。
- [未验证] GPU 与 NPU 支持状态（“GPU 已可用 / NPU 即将”）来自 README 表述；非 CPU 路径的成熟度、性能与平台覆盖本页未验证。
- [推断] 确切的受支持模型列表与所需转换步骤会随仓库变化；依赖某个具体模型前请对照当前 `README`/脚本核实。
- [推断] “派生自 llama.cpp、复用 GGUF + CLI”是从框架表述与工具链推断；与上游的精确同步关系未审计。
