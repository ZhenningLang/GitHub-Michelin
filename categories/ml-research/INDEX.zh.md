# ml-research

> 分类节点。小而自洽的 ML 研究 demo 与参考实现，按用途分为三个子类；另有三个不属于任何子类的项目直接挂在本节点。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 分类 | 何时用 | 路由 |
| --- | --- | --- |
| **research-automation** | 把研究闭环本身自动化的流水线与脚手架——由 agent 提出、运行并评估实验（乃至整篇论文）。 | [→](research-automation/INDEX.zh.md) |
| **vision-and-multimodal** | 视觉与视觉-语言研究模型及参考代码——图像 embedding、单目深度、GAN 架构、早期视觉工具路由 agent。 | [→](vision-and-multimodal/INDEX.zh.md) |
| **nlp-and-time-series** | 文本与序列类研究 demo——情感预训练、中文知识图谱流水线、LSTM 时序预测——大多基于陈旧技术栈。 | [→](nlp-and-time-series/INDEX.zh.md) |

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **context-language-models** | 用来研究或评测“让 agent 的模型自己改写实时上下文”（它用 bash 改写一份对话镜像文件）：跑在 Harbor 任务上，带 FLOPs 记账和一个 SGLang KV 复用补丁——论文代码，CC BY-NC 4.0，仅限非商用。 | D（4/6） | [→](context-language-models.zh.md) |
| **llm-circuit-finder** | 当你手里有本地 GGUF 模型、想搜出该复制哪段连续层块再用探针和 lm-evaluation-harness 量效果时用它——但收益是此消彼长（Devstral 全指标平均反而下降），且它是只支持 GGUF 的一次性 demo。 | D（4/6） | [→](llm-circuit-finder.zh.md) |
| **pymoo** | 当需要 Python 演化式多目标优化（NSGA-II/III、MOEA/D）求 Pareto 前沿时用它——若问题是凸／线性／单目标，LP 或梯度求解器要快得多。 | B（6/6） | [→](pymoo.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [context-language-models](context-language-models.zh.md) | ✅ | D（4/6） | 用来研究或评测“让 agent 的模型自己改写实时上下文”（它用 bash 改写一份对话镜像文件）：跑在 Harbor 任务上，带 FLOPs 记账和一个 SGLang KV 复用补丁——论文代码，CC BY-NC 4.0，仅限非商用。 |
| [llm-circuit-finder](llm-circuit-finder.zh.md) | ✅ | D（4/6） | 换来在消费级显卡上免训练做层手术实验；代价是能力画像只是偏移而非提升，代码单人所写、无发布无测试，得自己改着用。 |
| [pymoo](pymoo.zh.md) | ✅ | B（6/6） | 当需要 Python 演化式多目标优化（NSGA-II/III、MOEA/D）求 Pareto 前沿时用它——若问题是凸／线性／单目标，LP 或梯度求解器要快得多。 |
| TransformerLens / minGPT | 未收录 | — | 各页对比里点到的其他研究 demo / 可解释性库。 |

## 什么该放这里

小而自洽、用于研读学习而非投产的 **ML 研究 demo** 与参考实现。把研究闭环本身自动化的流水线在 `research-automation/`，视觉与视觉-语言模型在 `vision-and-multimodal/`，文本与序列类 demo 在 `nlp-and-time-series/`；不属于这三类的（模型自管上下文的 agent 框架 [context-language-models](context-language-models.zh.md)、LLM 层手术实验 [llm-circuit-finder](llm-circuit-finder.zh.md)、演化式多目标优化库 [pymoo](pymoo.zh.md)）直接挂在本节点。不含训练框架（见 `llm-training`）。
