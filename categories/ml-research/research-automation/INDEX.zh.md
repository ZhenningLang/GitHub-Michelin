# research-automation

> 分类节点。把研究闭环本身自动化的流水线与脚手架——由 agent 提出、运行并评估实验（乃至整篇论文）。
> ← 返回 [ml-research](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **autoresearch** | 当你有一块 NVIDIA GPU、想让自己的 coding agent 通宵改 train.py、每轮固定跑 5 分钟、只保留降低验证集 bits-per-byte 的改动时用它——但它不带 agent 运行器，且是无 tag 的 demo，自 2026-03 起未再更新。 | B（4/6） | [→](autoresearch.zh.md) |
| **The AI Scientist** | 当你想让「想法到论文」这整圈全自动跑完——想法生成、查新、实验代码、作图，最后编译出带 LLM 评审的 LaTeX 论文——时用它，但要接受一条绑死模板、自改许可证后冻结、且限制你发布其产出的流水线。 | D（4/6） | [→](ai-scientist.zh.md) |
| **Agent Laboratory** | 当你想让一组扮演角色的 LLM agent 跑「文献回顾→计划→实验→报告」、每阶段由你确认，并且要 MIT 条款和可续跑 checkpoint 时用它，但它自 2025-03 起没有代码改动，还挂着一条无人回应的安全披露。 | C（3/6） | [→](agent-laboratory.zh.md) |
| **RRSI** | 当你想复现或改造“自动改 agent harness”的搜索、并要一套防背题的刹车（有界带标签改动、泄题评审、噪声下限、token 成本规则）时用它——但搜索角色绑死 Vertex AI 上的 Claude，一次运行要跑几千次完整基准。 | C（5/6） | [→](rrsi.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [autoresearch](autoresearch.zh.md) | ✅ | B（4/6） | 换来一套紧凑现成、适合 agent 做 ML 研究的实验循环和指标；代价是 agent 要自带自付、只到单卡规模，结果跨硬件不可比。 |
| [The AI Scientist](ai-scientist.zh.md) | ✅ | D（4/6） | 当你想让「想法到论文」这整圈全自动跑完——想法生成、查新、实验代码、作图，最后编译出带 LLM 评审的 LaTeX 论文——时用它，但要接受一条绑死模板、自改许可证后冻结、且限制你发布其产出的流水线。 |
| [Agent Laboratory](agent-laboratory.zh.md) | ✅ | C（3/6） | 当你想让一组扮演角色的 LLM agent 跑「文献回顾→计划→实验→报告」、每阶段由你确认，并且要 MIT 条款和可续跑 checkpoint 时用它，但它自 2025-03 起没有代码改动，还挂着一条无人回应的安全披露。 |
| [RRSI](rrsi.zh.md) | ✅ | C（5/6） | 当你想复现或改造“自动改 agent harness”的搜索、并要一套防背题的刹车（有界带标签改动、泄题评审、噪声下限、token 成本规则）时用它——但搜索角色绑死 Vertex AI 上的 Claude，一次运行要跑几千次完整基准。 |

## 什么该放这里

第一职责是**把研究闭环本身自动化**的仓库：由 LLM agent 提出改动或想法、跑实验、按指标或评审打分、保留胜出者——包括“想法到论文”流水线（[The AI Scientist](ai-scientist.zh.md)、[Agent Laboratory](agent-laboratory.zh.md)）、通宵单卡训练迭代脚手架（[autoresearch](autoresearch.zh.md)）以及 agent harness 搜索（[RRSI](rrsi.zh.md)）。不含由人主导的交互式研究助手（见 `deep-research`），不含通用编码 agent 编排器（见 `agent-frameworks`），不含训练框架（见 `llm-training`）。
