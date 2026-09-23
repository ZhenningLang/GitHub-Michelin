---
name: SkillOpt
slug: skillopt
repo: https://github.com/microsoft/SkillOpt
category: workflow-builders
tags: [agent, prompt-optimization, skills, llm, microsoft, frozen-llm, text-space-optimization]
language: Python
license: MIT
maturity: v0.1.0, active, ~9.6k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-26T03:04:24Z
  default_branch: main
  default_branch_sha: 9969a8f393f3b5ece29715e6e5b07deb5be90741
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:38:07Z
  overall: B
  overall_score: 2.83
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
        last_commit_age_days: 17
        active_weeks_13: 11
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 69.8
        qualifying_issues: 37
        band: default
        window_offset_days: 4
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: skillopt
        dependent_repos_count: 0
        downloads_last_month: 10945
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: D
      raw:
        repo_age_days: 137
        last_commit_age_days: 17
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 62
        top1_share: 0.243
        top3_share: 0.432
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

# SkillOpt

一个文本空间优化器，为一个冻结的 LLM agent“训练”可复用的自然语言 skill 文档——施加经验证门控、由轨迹驱动的编辑，产出一份紧凑、可部署的 `best_skill.md`。

![skillopt — 健康度雷达](../../../assets/health/skillopt.zh.svg)

## 何时使用

你是应用 AI 工程师，手工调一份给 agent 用的长 skill/prompt 文档调到撞墙：你一直在改指令，但你没法微调模型（它被冻结在 API 后面），也分不清每次改动是真有帮助还是只是感觉更好。SkillOpt 把 *skill 文档本身*当作要优化的对象。你把它指向一个带打分函数的基准/任务，一个优化器 LLM 提出对 skill 文本的有界编辑（增/删/替）；每次编辑只有在它抬高一个留出验证分数时才被保留，由真实的 agent rollout 而非感觉来驱动。产出是一份小小的 `best_skill.md`（约 300–2,000 token），你把它放进 agent——部署时无额外推理，而且它是你能读、能 diff、能版本管理的纯文本。它支持多个 LLM 后端（OpenAI、Azure、Claude、Qwen、MiniMax），并与 direct-chat、Codex CLI 和 Claude Code 执行 harness 集成，因此你可以对着你真正发布所用的 harness 来优化 skill。

## 何时不用

- **你没有可打分的基准。** 整个方法是验证门控的——没有一个带可靠分数/eval 的任务，就没有东西能给编辑做门控，优化器也没有信号。
- **你的瓶颈是模型，不是 prompt。** SkillOpt 优化的是*文本*，不是权重。如果冻结模型从根本上做不了这个任务，再好的 skill 文档也救不了——你需要换一个/微调过的模型。
- **你想要一个成熟稳定的框架。** 这是个 v0.1.0 研究发布（2026），没有文档化的失败模式、成本上界或可扩展性边界——预期会有毛刺和 API churn。[推断]
- **优化成本是顾虑。** 轨迹驱动的编辑意味着跨多个 epoch 的大量 agent rollout 和优化器 LLM 调用；一次运行的 API/算力成本在文档里没有上界——投入前先估预算。[推断]
- **你需要离线 / 不出网。** 它驱动外部 LLM API 跑优化器和目标模型；主要工作负载经这些 API 运行，而非本地。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [DSPy](dspy.zh.md) | ✅ | 需要成熟框架来优化 LM 程序和管线，而不是单份可部署 skill 文档时，选 DSPy。 | 在冻结 LLM 上做程序化 prompt/管线优化的成熟框架（compiler、teleprompter）；更广、久经考验，但优化的是 prompt/程序而非单份可部署的 skill 文档。 |
| TextGrad | 未收录 | 想要“对文本反向传播”和自然语言梯度这个机制时，选 TextGrad。 | “对文本反向传播”——用自然语言梯度优化 prompt/文本；文本空间精神相近，更新机制不同，不以 skill 文档产物为中心。 |
| PromptBreeder / APE / OPRO | 未收录 | 想要 LLM 驱动的 prompt 搜索/演化，而不是验证门控的可复用 skill 时，选这些方法。 | LLM 驱动的 prompt 搜索/演化方法；在自动改进 prompt 上有重叠，但通常产出 prompt 字符串，而非经验证门控的可复用 skill 产物。 |
| 手工提示工程 | 未收录 | 无工具、完全掌控、零基础设施比度量和可复现更重要时，选手工提示工程。 | 无工具、完全掌控、零基础设施；但不可度量、不可复现，而且正是 SkillOpt 要自动化掉的那种苦工。 |

## 技术栈

- **语言：** Python（3.10+）。
- **方法：** 文本空间优化——一个优化器 LLM 对 skill 文档发出有界的增/删/替编辑；更新以来自 agent rollout 的留出分数做验证门控。
- **LLM 后端：** OpenAI、Azure、Claude（Anthropic）、Qwen、MiniMax——可插拔的优化器/目标模型。
- **harness：** direct chat、Codex CLI、Claude Code CLI 集成；六个内置基准。
- **产出：** 一份 `best_skill.md` 文本产物（约 300–2,000 token），部署时零额外推理。

## 依赖

- **LLM API 访问：** 优化器和目标模型的 key（OpenAI/Azure/Claude/Qwen/MiniMax 中的一个或多个）。主要工作负载经这些 API 运行。
- **基准/数据集：** 六个内置基准包，或你自己接入的可打分任务。
- **硬件：** 本地测试可选 GPU；主循环由 API 驱动，不受 GPU 约束。
- **网络：** 向所选 LLM 提供方出网——不是离线工具。

## 运维难度

**中。** 没有要跑的服务或数据存储——它是一个你用配置（epoch、batch size 等）调起的 Python 训练/优化循环。运维工作是：为优化器 + 目标模型备好 API key、定义或接入一个可打分基准，以及管理跨 epoch 的大量 rollout/编辑的*成本与耗时*。产出是一份静态文本文件，所以部署很简单（放入 `best_skill.md`）；负担在优化运行本身——它的 API 花费、可复现性以及调优化器——而不是运维任何长期存在的东西。

## 健康度与可持续性

- **响应速度**：Grade B——中位首次响应时间 69.8 小时，基于 37 个 qualifying issues/PRs。
- **维护（2026-06）。** 2026-05 创建；最后 push/提交于 2026-06——在头几周提交非常活跃。v0.1.0。**活跃**且**未归档**，但这是初次发布的速度，而非过往记录。[推断]
- **治理 / 背书。** 发布于 **microsoft** 组织下——强机构背书加一个多贡献者团队（bus factor 比单人仓库好）。注意：Microsoft/MSR 研究仓库的长期支持差异极大；组织背书不是维护保证。[推断]
- **年龄与 Lindy 判断。** **约 1 个月**（2026-05 创建）——**毫无 Lindy**。耐久性视为完全未经验证；这是一个全新的研究产物。[推断]
- **采用度。** star（约 9.6k）和 fork（约 912）的计数经 API 核实，但对一个一个月大的仓库而言异常地高——可能反映发布/Microsoft 组织的曝光（Microsoft + 当下热门的“skills”叙事），**不是**生产采用的证据。视为热度信号，而非社会证明。[未验证]
- **风险标记。** MIT（干净）。主要标记：全新（无寿命）、研究级 v0.1.0 且失败模式/成本上界无文档，以及读起来更像发布热度而非使用度的采用指标。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06，一个约 1 个月大的仓库有约 9.6k star / 约 912 fork——star 计数经 API 核实，但以这个年龄看它异常地高，可能反映发布/Microsoft 组织的曝光，而非生产采用的证据；请高度存疑。
- [未验证] “52 种 model-benchmark-harness 组合”与 skill 文档体量区间（约 300–2,000 token）是项目自报，来自 README——未独立复现。
- [推断] Python 3.10+ 与 GPU 可选是从 README 推断的；此处未对照 manifest 核实。
- [推断] 一次优化运行的成本/耗时在文档里没有上界（“未详述……算力成本阈值”）——“投入前先估预算”的提醒是从轨迹驱动方法做出的推断，而非实测数字。
- [推断] “Microsoft 背书≠维护保证”是对 MSR/Microsoft 研究仓库的一般推断，而非对本项目具体路线图承诺的陈述。
