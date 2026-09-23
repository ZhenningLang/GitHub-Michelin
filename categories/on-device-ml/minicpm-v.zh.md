---
name: MiniCPM-V
slug: minicpm-v
repo: https://github.com/OpenBMB/MiniCPM-V
category: on-device-ml
tags: [multimodal-llm, vision-language, on-device, edge-ai, image-understanding, video-understanding, gguf, llama-cpp, openbmb, small-model]
language: Python
license: Apache-2.0
maturity: ~25.7k stars, active (last push 2026-06); created 2024-01 (~2.5yr); multiple model generations (MiniCPM-V 4.x / MiniCPM-o) (as of 2026-06-28)
last_verified: 2026-06-28
type: model
upstream:
  pushed_at: 2026-06-25T12:12:59Z
  default_branch: main
  default_branch_sha: 8a2db6841e86b4b1a9b77e016a153c081677ac21
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:49:33Z
  overall: A
  overall_score: 4.0
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 14
        active_weeks_13: 8
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: A
      raw:
        repo_age_days: 967
        last_commit_age_days: 14
        cohort: model
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 15
        top1_share: 0.398
        top3_share: 0.667
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

# MiniCPM-V

OpenBMB 出品的一系列高效“口袋级”多模态 LLM——面向图像、多图与视频理解的小型视觉语言模型（MiniCPM-o 线还加了语音），按高“每参数性能”调优，能跑在手机和边缘硬件上。开放权重，外加推理/部署代码。

![minicpm-v — 健康度雷达](../../assets/health/minicpm-v.zh.svg)

## 何时使用

你在做一个必须“看得见”的产品功能——读小票、描述照片、回答关于一段短视频的问题、对表单做 OCR——而且它得**跑在设备上**，不能走你的云。也许是个移动应用，用户扫描文档，你不能把每张图都传到服务器（隐私、离线可用、按次成本）；也许是个边缘盒子，只有一块普通 GPU 甚至只有一颗还算能打的 CPU。前沿云端 VLM 在这里是杀鸡用牛刀，还要承担网络往返和随用量线性增长的 API 账单；而纯文本小模型根本看不见。

于是你选 MiniCPM-V。你挑一个小模型（比如某代约 1–9B 的 MiniCPM-V / MiniCPM-o），拉取开放权重，沿边缘路径部署：GGUF 构建在 llama.cpp 下运行，宣称在手机上能有每秒数 token 的解码；或者用 int4/AWQ/GPTQ 量化版、Ollama，乃至项目开源的 iOS/Android/HarmonyOS 适配代码。因为模型为高每参数性能调优，你能在几 GB 占用里拿到可用的图像/视频理解，而不必动用数据中心 GPU，整条管线还全程留在本地。

## 何时不用

- **你要前沿多模态质量。** 对最难的视觉/视频推理，顶级云模型（GPT-4o、Gemini）仍然领先——口袋级 VLM 是拿绝对质量换占用。如果精度是硬约束、又付得起云端，请用大模型。
- **你没核对权重许可。** *代码*是 Apache-2.0，但每代模型的**权重**许可与使用条款可能逐代不同（商用条款、注册、可接受使用政策）。请核对你要上线的那个具体模型卡——别假设 Apache 代码许可覆盖了权重。[未验证]
- **你以为是即插即用。** 把一个 VLM 塞进手机或边缘盒子是实打实的工作量：选量化（GGUF/int4/AWQ/GPTQ）、接运行时、把内存/延迟塞进预算、量化后还要重新验证质量。请预留集成成本。
- **你的任务是纯文本。** 这是*多模态*模型；若你不需要视觉/语音，纯文本小语言模型（SLM）做同样的活会更小更快——别为用不上的视觉能力买单。
- **你要一个经过审计、冻结、受支持的 SDK。** 它读起来更像一个模型快速换代的研究机构发布，而非带稳定性承诺、长期支持的产品 SDK。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| Qwen-VL / Qwen2.5-VL（阿里） | 未收录 | 需要覆盖多尺寸的强力开放视觉语言系列时，选 Qwen-VL。 | 覆盖多尺寸的强力开放视觉语言系列；尺寸跨度与生态更广，但其最小档不像 MiniCPM-V 那样专注于手机级端侧占用调优。 |
| LLaVA | 未收录 | 需要影响力很大的开放 VLM 配方/谱系时，选 LLaVA。 | 影响力很大的开放 VLM 配方/谱系；适合研究与微调，但通常更大、开箱即用时对边缘部署的优化更少。 |
| SmolVLM（Hugging Face） | 未收录 | 明确面向端侧的超小 VLM 是优先级时，选 SmolVLM。 | 明确面向端侧的超小 VLM；同属“小 + 多模态”赛道，往往更小，但通常视频能力更弱、型号阵容比 MiniCPM-V 各代要窄。 |
| Phi-3.5-vision（微软） | 未收录 | 需要微软工具链与背书的小视觉模型时，选 Phi-3.5-vision。 | 小而能打的视觉模型，配微软的工具链与背书；图像任务上有竞争力，但视频与语音的故事比 MiniCPM-o 线更弱更窄。 |
| GPT-4o / Gemini（云端） | 未收录 | 前沿质量和零部署成本高于离线/端侧约束时，选云端模型。 | 前沿多模态质量、零部署成本，但仅限云端——网络依赖、按次成本、无离线/端侧，且数据离开设备。与 MiniCPM-V 正好相反的取舍。 |
| [BitNet](bitnet.zh.md) | ✅ | 需要面向 CPU 能效的 1.58-bit 文本 LLM 推理框架时，选 BitNet。 | 面向 CPU 能效的 1.58-bit *文本* LLM 推理框架——层次/模态都不同；它不是视觉模型，与本项目互补而非替代。 |

## 技术栈

- **模型：** transformer 视觉语言模型（视觉编码器 + LLM 主干），分 MiniCPM-V（图像/多图/视频）与 MiniCPM-o（加语音/全模态）两条线，各代参数量大致从约 1B 到约 9B。
- **训练/推理代码：** Python，基于 PyTorch / Hugging Face Transformers；权重经 Hugging Face 分发。
- **量化与边缘格式：** GGUF（给 llama.cpp）、int4（bitsandbytes）、AWQ、GPTQ。
- **服务路径：** 服务器/桌面端用 llama.cpp、Ollama、vLLM、SGLang；移动端用开源的 iOS / Android / HarmonyOS 适配代码。

## 依赖

- **运行时：** 参考路径用 Python + PyTorch + Transformers；或边缘 GGUF 路径用 llama.cpp / Ollama（那条路推理时不需要 Python）。
- **权重：** 按模型代次从 Hugging Face 单独下载——不随仓库打包。磁盘/内存随模型大小与量化变化（量化小模型约几 GB；[未验证] 某 4.x 档引用约 2GB GGUF）。
- **硬件：** 全精度路径有 GPU 更好；量化/GGUF 路径面向 CPU 与移动端（手机级解码是头条用法）。小设备上内存预算才是真正的约束。
- **没有单一的“模型”安装包**——你要自己拼装权重 + 运行时；仓库提供脚本、demo 与边缘适配代码。

## 运维难度

**中等。** 参考路径（加载 HF 模型、跑 demo）在能打的机器上很简单。*边缘*路径——你选它的真正理由——才是工作量所在：选量化格式、在 llama.cpp 或 Ollama 下构建/运行、把设备内存与延迟塞进预算、量化后重新验证质量（小 VLM 量化太狠会明显劣化）。移动端上线用项目开源的 iOS/Android/HarmonyOS 适配代码，这是集成工作，不是即插即用的 SDK。单设备推理没有数据库或集群要运维；摩擦在于部署工程与逐模型的许可/使用尽调，而非运营一个服务。

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护（2026-06）：** 最后 push 在 2026-06，仓库跨越数个模型代次（MiniCPM-V 4.x、MiniCPM-o 4.5/2.6）陆续发布——读起来是**积极迭代**、节奏很快，而非滑行。[推断]
- **治理 / 背书：** OpenBMB（一个有清华关联/学术渊源的开放模型组织）。[推断] 这是组织而非单一维护者的背书，但学术/研究机构的延续性本身是一种风险——研究团队可能重新排期或收掉某条线；这不是大厂的 SLA。
- **年龄与 Lindy（创建于 2024-01，约 2.5 年）：** 年轻但跨代推进很快。**Lindy 未被验证**——太新，还称不上长寿安全赌注；其价值押在 OpenBMB 能否持续这条线上。用年龄 × 仍活跃来看：当前活跃，但尚未被证明耐久。[推断]
- **采用度：** 约 25.7k star，且在开放端侧 VLM 的讨论里有明显存在感（GGUF/Ollama 可用、移动端 demo），说明在其细分赛道上有强开放权重采用。[未验证]
- **风险标记：** 代码是 Apache-2.0（宽松），**但要单独核对每代模型的权重许可/使用条款**——它们可能逐代不同于 Apache 代码许可，这是商用上线前最关键的尽调项。[未验证]

## 存疑（未验证）

- [未验证] star 数约 25.7k（截至 2026-06-28）——GitHub star 不可靠且对日期敏感，仅作参考。
- [未验证] 每代模型的**权重**许可与可接受使用条款（商用、注册）可能不同于 Apache-2.0 *代码*许可，且逐代变化——依赖某个具体模型前请核对其模型卡；本页不断言单一的权重许可。
- [未验证] 创建日期约 2024-01 与“约 2.5 年”年龄为近似值；仓库确切创建时间戳本页未重新核实。
- [未验证] 具体型号阵容、参数量（约 1B / 约 9B 档）与版本号（MiniCPM-V 4.6、MiniCPM-o 4.5）来自核验时的 README 表述，会随版本变动——请对照当前仓库确认。
- [未验证] 端侧性能（“手机上 6–8 tok/s”、约 2GB GGUF 占用）与“逼近 Gemini 2.5 Flash”等对比是项目自报、条件未指明——本页未独立复现；随设备、模型、量化而变。
- [推断] MiniCPM-o 线增加了语音/全模态能力；每代模型确切的模态覆盖是从 README 表述推断的，应逐模型核实。
