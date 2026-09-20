---
name: LiteRT-LM
slug: litert-lm
repo: https://github.com/google-ai-edge/LiteRT-LM
category: on-device-ml
tags: [on-device-llm, edge-ai, litert, gemma, mobile-inference, npu, gpu-acceleration, android, ios, cross-platform, google-ai-edge, quantization]
language: C++ core; bindings Python/Kotlin/C++ stable, Swift/JS preview
license: Apache-2.0
maturity: Pre-1.0, fast cadence; stable v0.13.1 (2026-06-03), v0.14.0-alpha (2026-06-18); Google-maintained
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T08:21:44Z
  default_branch: main
  default_branch_sha: 645fcac1d5b47d1077edb01bc8f104e04c1ae6dc
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T14:54:09Z
  overall: B
  overall_score: 3.17
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 61.3
        qualifying_issues: 36
        band: relaxed_solo
        window_offset_days: 10
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: litert-lm
        dependent_repos_count: 0
        downloads_last_month: 11218
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
    longevity:
      grade: C
      raw:
        repo_age_days: 445
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 32
        top1_share: 0.278
        top3_share: 0.523
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

# LiteRT-LM

Google 在 LiteRT（TensorFlow Lite 的继任者）之上构建的 C++ 编排/运行时层，用于完全**在端侧**运行 LLM——一等支持 Gemma（Llama/Phi/Qwen 名义上支持，但优化程度较低），在 Android、iOS、桌面及边缘硬件上经由 CPU/GPU/NPU 运行；面向需要离线小模型（尤其 Gemma 系列）的 Android/跨平台 App，前提是团队能接受 Google 生态与 Bazel 构建。

![litert-lm — 健康度雷达](../../assets/health/litert-lm.zh.svg)

Google 把 Python/Kotlin/C++ 绑定标记为 *Stable*，但项目本身仍处于 pre-1.0——预期会有破坏性变更；Swift/JS 为预览状态。

## 何时使用

你是一家小创业公司的移动端工程师，正在交付一款私密日记 App,Android 是你的主打平台。你们的产品承诺是：用户的笔记永远不离开手机。所以产品要你做的“总结我这一周”“提取待办事项”这些功能，不能去调云端 LLM——那会破坏隐私叙事，而且以你们的规模，每生成一次摘要都要付一次按调用计费的 API 账单，会悄悄耗光跑道。你需要模型在本地跑、在没信号的飞机上也能用，并且能嵌进你现有的 Kotlin 代码里，而不必自己手搓一套 C++ 推理引擎。

于是你选用 LiteRT-LM。你把一个 **Gemma** 模型打包成 `.litertlm` 格式，通过稳定的 Kotlin 绑定接进来，让运行时在端侧用 CPU、外加可选的 GPU/NPU 加速来驱动。你真正需要的任务——摘要和结构化抽取——正好落在小模型能胜任的短小、结构化负载里；又因为你统一选型为 Gemma，正处在这个运行时的甜点区，而第三方 iPhone 基准也暗示：若你之后再补一个 iOS 版本，Gemma 级的延迟仍站得住脚。你接受“活在 Google 工具链与基于 Bazel 的构建之内”这一取舍，以换取一套 Google 维护的统一运行时，而不必跨平台拼装社区胶水。

## 何时不用

- **它不是通用的多模型运行时**——经过优化的 `.litertlm` 目录高度以 Gemma 为中心。对于任意 Hugging Face 模型、异类架构，或要把 Qwen/Mistral 作为一等公民，llama.cpp 或 MLX 支持的模型远更多，摩擦也更小。
- **不适合云级吞吐/低延迟**——`[未验证]` 据报道端侧推理比云端 API 慢 10–100 倍（第三方基准，非官方）；同步/交互式流程（动辄数分钟的生成）在没有架构层面变通的情况下不可用。
- **在内存受限设备上有风险**——2–4B 模型通常需要 6–8GB RAM,Android 在内存压力下可能杀掉进程；KV cache 在几轮对话后被填满并使输出退化，迫使进行会话轮换。
- **不适合冻结、稳定的 API**——pre-1.0，发布节奏很快 `[推断]`（例如 v0.13.1 → v0.14.0-alpha 在约 2 周内发生）；多个绑定为预览（Swift、JS/Web）或社区（Flutter）状态，意味着持续的变动。
- **生态/格式锁定**——模型必须打包成 Google 的 `.litertlm` 格式，且大多来自 Google 的 HF 社区；你还要承接一套基于 Bazel 的 C++ 构建。
- **不适合大模型/高准确率结果**——这是一个小模型边缘运行时；有团队反馈需要大量防御性工程（输出解析、语种漂移缓解、设备分级）才能获得可靠行为。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [llama.cpp](../llm-inference/local-runtimes/llama-cpp.zh.md) | ✅ | 需要广泛 GGUF 模型/量化支持和无处不在的覆盖面时，选 llama.cpp。 | 模型/量化支持（GGUF 生态）广泛得多、覆盖面无处不在，但跨平台构建更复杂，且没有单一的 Google 官方移动 SDK——你要自己拼装更多胶水。 |
| [MLX / mlx-lm (Apple)](mlx-mlx-lm.zh.md) | ✅ | Apple silicon 速度和干净 Swift/Python 体验最重要时，选 MLX。 | 在许多非 Gemma 模型上比 LiteRT-LM 更快，在 Apple silicon 上有干净的 Swift/Python 体验，但仅限 Apple——无法作为你的跨平台答案。 |
| MediaPipe LLM Inference API (Google) | 未收录 | 想要同一组织里更容易 drop-in 的端侧 LLM 层时，选 MediaPipe LLM Inference API。 | 来自同一组织、更高层、用 `.task` 模型即插即用的端侧 LLM 更易上手，但作为底层编排层的成分更少，在方向上与 LiteRT-LM 重叠/被其取代——是更简单但更不灵活的兄弟方案。 |
| ONNX Runtime (+ GenAI / Mobile) | 未收录 | 需要厂商中立的格式/后端广度时，选 ONNX Runtime。 | 厂商中立、成熟，跨生态支持众多格式与后端，但更重、对最新小型移动 LLM 调优不足，且缺少 LiteRT-LM 在 Gemma 专属移动量化上的优势。 |
| Apple Core ML / Foundation Models | 未收录 | Apple Neural Engine 集成和 OS 级模型是硬需求时，选 Apple 栈。 | 在较新 iPhone 上具备最佳的 Apple Neural Engine 集成与 OS 级模型，但锁定 Apple，转换可能很痛苦，没有通往 Android 或通用边缘硬件的路径。 |

## 技术栈

- C++ 核心运行时；LiteRT（TensorFlow Lite 继任者）推理引擎
- Bazel 构建系统；CMake;Cargo/Rust 工具链
- Python 绑定；Kotlin/JNI(Android);Swift/Metal（iOS/macOS，预览）;JavaScript/WebAssembly（Web，预览）
- `.litertlm` 打包模型格式

## 依赖

- **Bazel** + 固定的 `.bazelversion` 以从源码构建（重型 C++ 工具链）
- **LiteRT 运行时**
- **`.litertlm` 格式的模型**，来自 Hugging Face / Kaggle 上的 LiteRT Community
- **各平台原生工具链**——Android NDK、Xcode(iOS/macOS)、Emscripten(Web)
- **GPU/NPU 厂商驱动**，用于加速后端（NPU 支持受平台限制 / 部分为预览）

## 运维难度

**高。** 从源码构建使用带固定版本的 Bazel 以及庞大的 C++/Rust 工具链——相比 pip 安装一个 wrapper 远非易事。除了构建，端侧 LLM 运维本身就难：设备分级的 RAM 门控（2–4B 模型常需 6–8GB RAM，否则 Android 会杀进程）、GPU 初始化后回退 CPU 的逻辑（GPU 可用性在各设备间不一致）、每隔几轮就做 KV-cache 会话轮换 `[未验证]` 以阻止质量退化，以及防御性输出解析，因为小模型会发出格式错误的 JSON / 错误语种的文本。模型必须转换/打包为 `.litertlm`。多个绑定（Swift、JS、Flutter）为预览/社区状态，因此在 pre-1.0 阶段 API 变动与缺口很可能存在。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 61.3 小时，基于 36 个 qualifying issues/PRs。
- **维护（2026-06）：** 最后 push 在 2026-06，发版节奏很快（稳定版 v0.13.1 → v0.14.0-alpha 在约 2 周内）——明显**活跃**，但处于 pre-1.0，变动正是这种活跃的代价。[推断]
- **治理 / 背书：** 由 Google 在 `google-ai-edge`（Organization）下维护，属于 LiteRT / TensorFlow Lite 谱系。[推断] 这消除了单一维护者的巴士因子风险，但 Google 是出了名的项目杀手（参见 MediaPipe→LiteRT-LM 的重定位）——*运行时*的方向性延续比任何单个绑定或格式存活更可靠。
- **年龄与 Lindy（创建于 2025-04，约 1 年）：** 年轻且被热捧；Lindy 先验很弱——它尚未证明多年存活。押它是为了 Google/LiteRT 的背书与 Gemma 路径，而非长寿记录。[推断]
- **采用度：** 约 5k star（易波动，见存疑）；以 Gemma 为中心的 `.litertlm` 目录与 pre-1.0 绑定（Swift/JS/Flutter 预览）让可投产的面偏窄。[未验证]
- **风险标记：** Apache-2.0（无重新许可风险）。活跃风险是 pre-1.0 的 API 变动，以及 `.litertlm` 格式 + Google 生态锁定。[推断]

## 存疑（未验证）

- **计数** —— stars/forks/issues（5,703 / 596 / 383）取自 2026-06-26 的 GitHub API，会持续漂移；此前一份摘录只报告了约 3,157 stars，因此来源彼此不一致。`[未验证]`
- **吞吐** —— 例如“Gemma 级 E2B 在 iPhone 上达 55.4 tok/s，胜过 MLX 的 47.5 和 llama.cpp 的 37.8”出自第三方 dev.to 基准，非官方；随设备/模型/量化而变。`[未验证]`
- **RAM 数字** —— 每个模型约 1.5–8GB、文件约 3.66GB、纯文本权重约 0.8GB——由博客和 HF 模型卡汇总而来，未对照官方规格核实。`[未验证]`
- **目录广度** —— “仅 Gemma 优化”是第三方评论；README 列出 Llama/Phi-4/Qwen 为受支持，因此名义支持与实际可用的已优化 `.litertlm` 资产之间存在差异，尚未确认。`[未验证]`
- **MediaPipe 关系** —— 相对于较旧的 MediaPipe LLM Inference API 的取代/定位说法属推断，官方概述中并未陈述。`[未验证]`
- **NPU 可用性细节** —— 来自文档摘要；可能与当前发布矩阵不同。`[未验证]`
- **构建难度** —— 由仓库配置（`.bazelrc`、`.bazelversion`、CMake、Cargo）推断，而非实测构建。`[推断]`
