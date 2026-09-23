---
name: autoresearch
slug: autoresearch
repo: https://github.com/karpathy/autoresearch
category: ml-research
tags: [llm-training, agentic-research, nanochat, single-gpu, reference-implementation]
language: Python
license: MIT
maturity: no tagged release, active, master @ ~36 commits (as of 2026-03)
last_verified: 2026-06-26
type: app
upstream:
  pushed_at: 2026-03-26T00:07:37Z
  default_branch: master
  default_branch_sha: 228791fb499afffb54b46200aca536f79142f117
  archived: false
health:
  schema: 1
  computed_at: 2026-09-23T07:47:51Z
  overall: B
  overall_score: 2.5
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
        last_commit_age_days: 181
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 7.7
        qualifying_issues: 4
        band: relaxed_solo
        window_offset_days: 6
        source: issue
        inferred: false
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 200
        last_commit_age_days: 181
        cohort: app
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 8
        top1_share: 0.75
        top3_share: 0.821
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    adoption: { reason: no_package_structural }
    risk_license: { reason: license_declared_unverifiable }
---

# autoresearch

一个自包含的单卡 LLM 训练脚手架，设计目标是让 AI agent 在夜里自主迭代 `train.py`——每次跑 5 分钟实验，用验证集 bits-per-byte 打分，只保留能降低 loss 的改动。

![autoresearch — 健康度雷达](../../assets/health/autoresearch.zh.svg)

## 何时使用

你是一名 ML 研究者，或者手里有一块 H100（或类似单卡）的折腾者，隐约觉得：只要给 coding agent 一个足够紧凑的循环，它也许真能做出像样的 ML 研究。你不想要那种跑 10 小时的训练——一个失败的想法就赔上一整夜；你想要固定的 5 分钟预算，让 agent 每小时试约 12 个想法，最后由验证 loss 来当裁判。autoresearch 给你的正是这套脚手架：一个简化、自包含、nanochat 风格的 GPT，全部塞进一个允许 agent 编辑的 `train.py`；一个被冻结的 `prepare.py`，钉死数据和 tokenizer，让多次运行可比；还有一份由你（人类）撰写、用来引导 agent 策略的 `program.md`。你把 agent 指向它，转身离开，第二天早上来看哪些 diff 活了下来。

它同样是一个干净的参考实现，适合用来*研读*或 fork「agent 即研究员」这个范式——val_bpb 这个指标刻意做成与词表大小无关，于是不同架构改动（不同模型维度、Muon 还是 AdamW 等优化器）能被公平比较。如果你想自建一套自主实验 harness，这里是一个最小、易读的起点，而不是一个笨重的框架。

## 何时不用

- **你想要生产级训练框架。** 这是研究 demo / 参考实现，不是受维护的库——没有打 tag 的发布、没有插件 API、没有多卡 / 分布式方案。真要做微调请用框架，而不是它。
- **你没有 NVIDIA GPU。** 它面向单块 NVIDIA GPU（在 H100 上测试过）；其它平台靠社区 fork。而且 5 分钟固定预算意味着结果在不同算力之间明确*不可比*。
- **你以为 agent 是开箱即用的。** autoresearch 提供训练脚手架和指标，但它**不**附带 agent 循环或 LLM API 接线——你得自带 / 自配 coding agent，并自付它的推理费用。
- **你需要可复现、可发表的 benchmark。** 这套以墙钟时间封顶的设计，是用「跨机可比性」换「快速迭代」，这是设计本身决定的；数字只对你的硬件成立。
- **你想训出一个有用的模型。** 重点是研究*循环*，不是训出来的 checkpoint——5 分钟单卡跑出来的是玩具规模的模型，不是能部署的东西。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [llm-circuit-finder](llm-circuit-finder.zh.md) | ✅ | 需要小巧自包含、研究推理期层复制或 circuit 路由的 demo 时，选 llm-circuit-finder。 | 同样是小巧、自包含的研究 demo，但它探索的是在既有大模型上做*推理期*的层复制 / circuit 路由——没有训练循环、没有 agent 驱动的迭代；研究问题完全不同。 |
| nanochat | 未收录 | 需要完整单卡 GPT 训练项目而不是 agentic-research 简化版时，选 nanochat。 | 本项目正是从这个完整单卡 GPT 训练项目简化而来；它面向人类端到端训练一个真正的小型 ChatGPT clone，而非让 agent 在时间预算下改写它。 |
| [nanoGPT](../llm-training/study-and-experiments/nanogpt.zh.md) | ✅ | 当你要读那份最经典的最小 GPT-2 参考实现、并接受它已被上游废弃时选 nanoGPT；当你想让 agent 在固定时间预算下迭代时选 autoresearch，因为 nanoGPT 既没有自动化也没有固定评测 harness。 | nanoGPT 是可读但已冻结、靠手工编辑的 baseline；autoresearch 是在这个想法之上的自动化层，带 5 分钟预算与计分循环。 |
| [The AI Scientist](ai-scientist.zh.md) | ✅ | 需要想法→实验→论文撰写的端到端 agent 科研流水线时，选 The AI Scientist。 | 一条更重的端到端「agent 做科研」流水线（想法→实验→论文撰写）；范围更广、活动部件远多于这个单文件训练循环。 |

## 技术栈

- **语言：** Python（仓库约 83%），模型、优化器和训练循环全部活在一个 `train.py` 里。
- **模型：** nanochat 的简化、自包含单卡实现——一个带 BPE 分词的 GPT，据称支持 Muon + AdamW 优化器。
- **指标：** `val_bpb`（验证集 bits-per-byte），越低越好，且与词表大小无关，让架构改动公平比较。
- **工具：** 用 `uv` 做项目 / 依赖管理；`prepare.py` 做一次性数据 + tokenizer 准备，并被冻结以保证运行可比。
- **人 / agent 分工：** 人类编辑 `program.md`（agent 指令 /「研究组织」框架）；agent 只编辑 `train.py`。

## 依赖

- **运行时：** Python 3.10+；PyTorch。README 称训练代码自包含，「除 PyTorch 和少数小包外无外部依赖」。
- **硬件：** 单块 NVIDIA GPU（在 H100 上测试过）；需要 CUDA。无多卡 / 分布式路径。
- **安装：** 装 `uv`，跑 `uv sync`，再 `uv run prepare.py`（一次性，约 2 分钟），再 `uv run train.py`（每个实验约 5 分钟）。
- **未打包：** coding agent 本体及其 LLM / API 访问——这些需你另行提供并付费。

## 运维难度

**搭起来很低，但 agent 循环要你自己扛。** 跑一个手动实验非常简单——单卡上 `uv sync && uv run prepare.py && uv run train.py`。真正的运维负担在脚手架*之外*：为通宵迭代准备 / 占用一块 NVIDIA GPU（H100 级别）数小时、把 coding agent 接进「编辑—运行—评测」循环、并盯住成本与 agent 失控行为。没有服务要部署、长期也没什么要维护的，但它也不是按个按钮就开跑的自主研究员。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 7.7 小时，基于 4 个 qualifying issues/PRs。
- **维护（截至 2026-06）：** 最后一次 push 在 2026-03，master 约 36 个 commit，无打 tag 的发布。[推断] 说它「活跃」只是指最近被动过，但这是个 demo 分支、不是受维护的产品——没有可读的发布节奏，且可能逐 commit 变化。
- **治理 / bus factor：** 这是挂在 Karpathy 个人账号下（`User`-owned）的单人维护仓库，却背着约 88k star——典型的 **bus-factor 警示**：star 反映的是作者影响力，而非一支团队或持续路线图。[推断] 不含治理结构、也没有隐含的贡献者流程；作者一旦转向，它就会冻结。
- **年龄与 Lindy 判定（创建于 2026-03，约 0 年）：** 全新，靠热度 / star 数而非存活验证撑起来。[推断] **Lindy 上未经证明**——请把它当作参考样本和值得研读的范式，而非长期依赖。它的价值在于那个*想法*（固定预算下「agent 即研究员」），这比任何具体 commit 都更长寿。
- **风险标记：** 无版本 / API 稳定性；agent 循环和 LLM 成本都要自带；「研究 demo」的姿态是明示的。采用 MIT 许可，所以 fork 一份钉死已知可用状态是稳妥之举。[推断]

## 存疑（未验证）

- [未验证] Star / fork 数（约 88.7k stars、约 12.8k forks）和「master 约 36 个 commit」取自 2026-03-26 / 2026-06-26 的 GitHub 页面；star 不可靠且对日期敏感——只作参考。
- [未验证] 不存在打 tag 的发布；「maturity」反映的是活跃的 master 分支，而非一个有版本、API 稳定的项目——行为可能逐 commit 变化。
- [未验证] 优化器集合（Muon + AdamW）、BPE 分词、约 12 实验/小时的吞吐都来自 README / 摘要转述，未独立运行验证——依赖前请对照当前的 `train.py` / `prepare.py`。
- [未验证]「在 H100 上测试过」和「5 分钟墙钟、不含启动 / 编译」是作者自述数字；实际运行时间随 GPU、驱动和编译缓存而变。
- [推断] agent 循环是 BYO（自带 coding agent + LLM API）；仓库本身是训练脚手架和指标。该判断由文件分工推断（`program.md` 人类编辑、`train.py` agent 编辑）——请确认当前代码树是否打包了某个 agent runner。
- [未验证] 跨平台（非 NVIDIA）支持据称只通过社区 fork 存在；本仓库内未经验证。
