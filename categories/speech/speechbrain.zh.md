---
name: SpeechBrain
slug: speechbrain
repo: https://github.com/speechbrain/speechbrain
category: speech
tags: [speech, asr, pytorch, toolkit, speaker-recognition, text-to-speech, research]
language: Python
license: Apache-2.0
maturity: v1.1.0 (2026-03), active, ~11.7k stars (as of 2026-06)
last_verified: 2026-06-28
type: framework
upstream:
  pushed_at: 2026-06-15T11:24:25Z
  default_branch: develop
  default_branch_sha: e5cb1f65b940634215650aa1171e0440d0808123
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:51:39Z
  overall: B
  overall_score: 3.2
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 26
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: D
      raw:
        median_ttfr_hours: 988.1
        qualifying_issues: 6
        band: default
        window_offset_days: 6
        source: pr
        inferred: false
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: A
      raw:
        repo_age_days: 2338
        last_commit_age_days: 26
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 30
        top1_share: 0.232
        top3_share: 0.549
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
    adoption: { reason: ambiguous }
---

# SpeechBrain

一个一站式、基于 PyTorch 的语音工具箱，覆盖语音识别、说话人识别、增强、分离、语种识别、文本转语音等——并带数百份在标准数据集上可直接跑的训练“recipe”。

![speechbrain — 健康度雷达](../../assets/health/speechbrain.zh.svg)

## 何时使用

你是语音 ML 研究者或应用工程师，需要训练（而不只是调用）一个语音模型——比如一个领域专用 ASR 系统、一个说话人确认模型，或一条声源分离管线——而你想站在一个一致的 PyTorch 代码库上，而不是把五个互不兼容的研究仓库硬粘起来。你 clone SpeechBrain，挑一份对应任务和数据集的 recipe（LibriSpeech ASR、VoxCeleb 说话人 ID、WSJ0-mix 分离……），就得到一个可跑的训练脚本、一份描述整个实验的 YAML 驱动配置（HyperPyYAML）、数据管线，以及一个你可以微调的模型。因为一切共享同一框架，换 encoder、换 loss 或换数据集，是改配置和一个类，而不是在项目之间移植代码。

当你既想*用*又想*重训*预训练模型时，你也会选它：SpeechBrain 发布了许多 checkpoint（常通过 Hugging Face），带简单的推理接口，但与黑盒 API 不同，你手里有完整 recipe 去复现或改造它们。当你的工作同时横跨多个语音任务、又希望它们活在一个连贯、文档良好的研究工具箱里而非一堆一次性脚本里时，它最有价值。

## 何时不用

- **你只想用 SOTA 模型转写音频、不训练。** 如果只要推理，`faster-whisper`/Whisper 或托管 STT API 比上手一整套训练框架路径更短。
- **你需要开箱即用的、加固的低延迟生产服务栈。** SpeechBrain 研究与训练优先；产品化（serving、流式、延迟调优、部署）是你的活，有些 recipe 瞄准的是基准而非生产约束。[推断]
- **你被绑死在非 PyTorch 栈上。** 它是 PyTorch 原生的；若你的环境只有 JAX/TF 或受边缘运行时约束，契合度差。
- **你想要一个极小的依赖。** 它拉入 PyTorch 和一整套研究级依赖；它是工具箱，不是可塞进小应用的轻量库。
- **你需要跨版本有保证的长期 API 稳定。** 它是活跃演进的研究工具箱；recipe 和 API 会跨大版本变化（v1.x 线就是一次显著转变），所以请 pin 版本并为迁移留预算。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| NeMo（NVIDIA） | 未收录 | 需要更大、面向 GPU/规模的对话式 AI 工具箱和 NVIDIA 工具链时，选 NeMo。 | ASR/TTS 强且带 NVIDIA 集成，但比 SpeechBrain 更重、更偏厂商生态。 |
| ESPnet | 未收录 | 需要端到端语音处理、深 ASR/TTS recipe 覆盖和研究血统时，选 ESPnet。 | 很强，但历来学习曲线更陡，也更带 Kaldi 味。 |
| Hugging Face Transformers（音频） | 未收录 | 使用或微调 Whisper/Wav2Vec2 这类预训练音频模型已经足够时，选 Transformers 音频模型。 | 模型获取极方便，但不是横跨分离、增强、说话人分割的完整 recipe/训练框架。 |
| Kaldi | 未收录 | 需要经典、高度优化的 ASR 工具箱，并能接受 C++/shell-heavy 工作流时，选 Kaldi。 | 它追求极致控制而非易用；学习曲线陡，且不是 PyTorch 原生。 |
| faster-whisper / [Whisper](../media-processing/video-audio/whisper.zh.md) | 部分已收录 | 只做转写而非多任务语音训练时，选聚焦推理的 Whisper 技术栈。 | 只转写时极佳，但不是多任务训练工具箱。faster-whisper 未单独收录。 |

## 技术栈

- **语言/框架：** Python 跑在 **PyTorch** 上；模型、训练循环和数据管线都是 PyTorch 原生。
- **配置：** **HyperPyYAML**——一个 YAML 超集，描述完整实验（模型、optimizer、数据、超参），让实验声明式且可复现。
- **范围：** 覆盖 ASR、说话人识别/确认、语音增强、声源分离、语种识别、TTS、口语理解等的 recipe 与模块。
- **模型：** 许多预训练 checkpoint，常通过 Hugging Face Hub 分发，带轻量推理封装。

## 依赖

- **运行时：** Python + PyTorch，外加一套科学/音频依赖栈（numpy、torchaudio 等）。认真训练实际上需要 GPU。[推断]
- **数据：** recipe 假定你能拿到相关语料（LibriSpeech、VoxCeleb 等）——数据集由 recipe 脚本下载/准备，不随仓库捆绑。
- **Hugging Face：** 预训练模型推理通常从 HF Hub 拉 checkpoint（需要网络 + HF 可用）。
- **安装：** `pip install speechbrain`，或 clone 仓库直接用/改 recipe。

## 运维难度

**中（研究）/ 偏高（生产）。** 对其本意用途——跑并改造训练 recipe——人体工学不错：装好、挑 recipe、改 YAML、训练。真正的成本在围绕它的 ML 生命周期：获取并准备大数据集、搞定 GPU/算力、长时训练，以及复现基准数字。把训好的模型推到生产（serving、流式、延迟、监控）完全是你的责任，也是更难的那一半。SpeechBrain 本身没有要运维的服务——负担是算力和 ML-ops，而非跑一个 SpeechBrain 守护进程。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 最后 push 于 2026-06；v1.1.0 于 2026-03 在 `develop` 分支发布且活动稳定——处于**活跃**而非吃老本。未归档。[推断]
- **治理 / bus factor。** 一个研究社区项目，由一个可辨识的维护者群体（学术/实验室关联的核心贡献者）而非单人驱动——bus factor 比单人项目宽，但仍是社区/学术资助而非基金会。[未验证]
- **年龄 × Lindy（2026-06）。** 2020-04 创建——约 6 岁且**仍在活跃发布**⇒ 对一个研究工具箱而言是**中到强 Lindy** 信号；它已熬过典型学术仓库的半衰期。[推断]
- **采用度与生态。** 在语音研究中被广泛引用和使用、Hugging Face 上大量预训练模型，加上可观的文档/recipe，都表明它在其细分领域采用度健康。约 180 个 open issue 与一个活跃研究代码库相符。[未验证]
- **风险标记。** Apache-2.0，未发现 relicense 历史。主要风险是研究工具箱的固有风险：跨大版本的 API/recipe 变动，以及一段需你自己补齐的生产落差。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 11.7k star、v1.1.0（2026-03）——star 与版本号对时间敏感，仅供参考。
- [未验证] 除可见的贡献者集合外，确切的维护者/治理结构和资助模型未确认；“研究社区驱动”由贡献者列表和项目学术血统推断。
- [推断] GPU 需求、数据集下载行为，以及预训练推理对 HF Hub 的依赖，由工具箱性质和 README 推断，未逐 recipe 详尽核实。
- [推断] “recipe/API 跨大版本变化”由 v1.x 大版本线的存在推断；具体破坏性变更范围未逐项列举。
- [未验证] 与 NeMo/ESPnet/Kaldi 的对比反映总体定位，而非实测基准。
