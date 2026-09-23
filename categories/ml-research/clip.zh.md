---
name: CLIP
slug: clip
repo: https://github.com/openai/CLIP
category: ml-research
tags: [zero-shot, image-classification, multimodal, embeddings, retrieval, contrastive, vision-language]
language: Python
license: MIT
maturity: stable reference release, low ongoing maintenance, ~33.9k stars (last pushed 2026-03, as of 2026-06)
last_verified: 2026-06-28
type: model
upstream:
  pushed_at: 2026-03-25T18:46:40Z
  default_branch: main
  default_branch_sha: d05afc436d78f1c48dc0dbf8e5980a9d471f35f6
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:42:23Z
  overall: C
  overall_score: 2.2
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 181
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: clip-openai
        dependent_repos_count: 1
        downloads_last_month: 2941
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 2106
        last_commit_age_days: 181
        cohort: model
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.5
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
  unknowns:
    responsiveness: { reason: type_na }
---

# CLIP

OpenAI 官方的 CLIP（Contrastive Language-Image Pre-training）原始参考实现——一个把图像和文本映射到同一个共享 embedding 空间的模型，于是你可以把标签写成纯文本来给图像分类或检索，无需任何任务专属训练。

![clip — 健康度雷达](../../assets/health/clip.zh.svg)

## 何时使用

你是一名 ML 工程师或研究者，需要在不收集标注数据集、不训练分类器的前提下给图像打标签或做搜索。也许你手里有一堆商品图和一份类目名称清单，或者你想在一个大图库里找出「一只狗接飞盘的照片」。你加载一个预训练 CLIP checkpoint，对图像跑 `clip.encode_image`、对候选 prompt 跑 `clip.encode_text`，把两边归一化后取余弦相似度——得分最高的那个文本标签就是你的零样本预测，而同一批 embedding 又可以直接当检索索引用。因为图像和文本活在同一个向量空间里，分类、检索和粗粒度语义相似都能用一个模型、几行 PyTorch 搞定。

当你想要那份规范、最小的参考时，你也会选这个具体的仓库：原始的 ViT-B/32、ViT-L/14 和 ResNet（RN50 等）权重，以及 OpenAI 当年发布的那套确切预处理，用来复现论文数字，或读懂模型和 tokenizer 究竟是怎么接线的。在转向更重的框架之前，它是理解 CLIP 的最小忠实起点。

## 何时不用

- **你想要一个在生产里持续演进的 CLIP。** 这个原始仓库实际上是冻结的参考——它只带一组固定的 OpenAI checkpoint，几乎不再维护。[推断] 想要更多 checkpoint、训练代码和 patterns map（LAION 训练的模型）请用 OpenCLIP；想要一个有维护、集成良好的 API 请用 Hugging Face `transformers` 里的 CLIP。
- **你需要更新、更强的 backbone。** 这里的 CLIP 是较老的 ViT 和 ResNet 架构；SigLIP（sigmoid loss）和 EVA-CLIP 在现代零样本基准上普遍更强，而 OpenCLIP 暴露了一个宽得多的模型库。
- **你以为它是生成模型。** CLIP 是个*编码器*——它给图文对齐打分，并不给图像写描述或回答问题。要做图到文的生成，你要的是 BLIP / BLIP-2 或某个 VLM，而不是 CLIP。
- **你需要宽广或公平的领域覆盖。** 它带着训练数据（大量网络抓取、偏英文）的偏见和领域缺口；在细粒度、非英文、OCR、计数和专业领域任务上表现会下降，而且零样本得分对 prompt 措辞很敏感、容易脆。
- **你需要一个可 pin 的受维护依赖。** 安装方式是从仓库 `pip install git+...`（不是有版本的 PyPI 包），所以你 pin 的是一个 git ref，而不是一个 release。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| OpenCLIP | 未收录 | 需要开源训练代码和大规模 checkpoint zoo 时，选 OpenCLIP。 | 带训练代码和一大堆 checkpoint（很多在 LAION/DataComp 上训练）的开源复现；当你需要更多或更强的 CLIP 模型、或想自己训练时的事实标准——严格比这个参考仓库更宽。 |
| Hugging Face `transformers` 里的 CLIP | 未收录 | 想把 OpenAI CLIP 权重放进有维护、开箱即用的 API 时，选 Hugging Face transformers。 | 把同一批 OpenAI 权重包进一个有维护、开箱即用的 API（processor、`from_pretrained`、pipeline）；更易集成、更易跟进，代价是更重的 `transformers` 依赖。 |
| SigLIP | 未收录 | 需要用 sigmoid loss 训练的更新图文模型时，选 SigLIP。 | 用 sigmoid loss 训练的更新图文模型；零样本精度通常更高、在规模上更好，但属于不同模型家族——一般通过 OpenCLIP 或 `transformers` 用，而不是这个仓库。 |
| EVA-CLIP | 未收录 | 需要训练配方改良、backbone 更大的放大版 CLIP 时，选 EVA-CLIP。 | 放大的 CLIP，训练配方改良、backbone 更大；精度上限更高，权重和算力更重。 |
| BLIP / BLIP-2 | 未收录 | 需要能生成文本的视觉语言模型时，选 BLIP 或 BLIP-2。 | *生成*文本的视觉语言模型（看图说话、VQA）；解决的是和 CLIP 对比式 embedding/检索不同的问题——不是即插即换的替代。 |

## 技术栈

- **语言：** Python，用法/示例大多以 Jupyter notebook 交付（按 GitHub 语言统计，该仓库约 99% 为 notebook、约 1% 为 Python）。
- **框架：** PyTorch——模型（`clip.load`）、图像编码器（ViT 或改良 ResNet）、文本编码器（Transformer），外加一个 BPE tokenizer。
- **模型变体：** OpenAI 的 checkpoint，包括 ResNet backbone（RN50 及更大）和 Vision Transformer（ViT-B/32、ViT-B/16、ViT-L/14），每个都配自己的预处理 transform。
- **接口：** 一套小 API——`clip.available_models()`、`clip.load(name)`、`model.encode_image`、`model.encode_text`——以及随模型一起返回的预处理 `Compose`。

## 依赖

- **运行时：** Python 和 PyTorch 1.7.1+，加 torchvision，外加小助手 `ftfy`、`regex` 和 `tqdm`（依 README）。
- **预训练权重：** checkpoint 在首次 `clip.load(...)` 时下载（需要网络）并缓存到本地；权重才是实质依赖，不只是代码。
- **硬件：** 能在 CPU 上跑，但除了寥寥几张图以外，强烈建议用 CUDA GPU；更大的 ViT-L/14 需要相应更多显存。[推断]
- **安装：** `pip install git+https://github.com/openai/CLIP.git`——该仓库没有单独有版本的 PyPI release。

## 运维难度

**低。** 没有服务要部署、也没什么要训练——装好包、调 `clip.load`、跑推理即可。现实中的运维活儿在它周边、而非它内部：拉取并缓存权重（以及在离线或 CI 环境里处理那次首载下载）、把 CUDA/PyTorch 版本对齐、为吞吐做批处理 encode，以及打磨 prompt/模板（「a photo of a {label}」），因为零样本精度对措辞敏感。要做大规模服务，你通常会预先算好图像 embedding 存进向量索引、而不是每次查询都重新编码——但那个索引要你自己跑，不属于 CLIP 的一部分。

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护（截至 2026-06）：** 最后一次 push 约在 2026-03，但它实质上是个**冻结的参考**——固定 checkpoint 集、推送稀疏，并非一个仍在演进的代码库。[推断] 把它当作「按设计躺平」：它仍能安装、能跑，但别指望这里出新 backbone、修复或有版本的 PyPI release。
- **治理 / 背书：** 由 OpenAI 这个组织持有——是原始论文仓库，而非社区项目。这带来出处（这是*那份*参考权重 / 预处理），但不承诺持续维护；活跃生态早已迁往 OpenCLIP 和 Hugging Face `transformers`。
- **年龄与 Lindy 判定（创建于 2020-12，约 6 年）：** 既老*又仍被广泛使用*，对 **CLIP 这一思路及这批权重**作为稳定基线而言是强 Lindy 信号。判定是分裂的：*概念 / checkpoint* 经 Lindy 验证、可放心在其上构建；*把这个具体仓库当受维护依赖*则不行——它的长寿是「出名且冻结」，而非「持续维护」。
- **采用度：** CLIP embedding 在检索、零样本分类，以及作为众多下游系统的文 / 图编码器中是基础件；尽管多数生产用户经由 OpenCLIP/`transformers` 而非本仓库消费，这个范式已根深蒂固。
- **风险标记：** 安装是 `pip install git+...`（一个 git ref，而非 release），所以可复现性取决于钉死某个 commit；MIT 许可，无 relicense 风险。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06，约 33.9k GitHub star、最后一次 push 约在 2026-03；star 数不可靠且对日期敏感——仅作参考。
- [推断]「稳定参考发布 / 低维护」是从「这是带固定 checkpoint 集、推送不频繁的原始论文仓库」推断出来的，并非项目声明的状态——依赖前请核对近期的 commit/issue 活跃度。
- [未验证] 确切的依赖下限（PyTorch 1.7.1、torchvision、ftfy、regex、tqdm）取自 README；实际最低版本可能漂移——请对照当前代码树里的 `setup.py`/requirements 核实。
- [未验证] 可用 checkpoint 的集合与名称（RN50、ViT-B/32、ViT-B/16、ViT-L/14 及更大）是从 README/`clip.available_models()` 转述的；确切清单请对照当前仓库确认。
- [推断] GPU 建议与显存随 backbone 大小的敏感度是对 transformer 推理的一般推断，并非本仓库的实测数字。
- [未验证] 偏见与领域缺口的描述来自 CLIP 论文 / model card 的表述，并非本页的独立评测。
