# nlp-and-time-series

> 分类节点。文本与序列类研究 demo——情感预训练、中文知识图谱流水线、LSTM 时序预测——大多基于陈旧技术栈。
> ← 返回 [ml-research](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **LSTM Neural Network for Time Series Prediction** | 当需要可读的配套示例学习 Keras LSTM 时序预测时用它——它锁定 EOL 的 TF1／Python 3.5 且为 AGPL-3.0，应照文章重写而非直接引入。 | E（4/6） | [→](lstm-time-series.zh.md) |
| **Agriculture Knowledge Graph (AgriKG)** | 当需要中文领域知识图谱完整蓝图与现成数据集（NER、关系抽取、Neo4j、Django）时用它——作者声明已停止维护、技术栈陈旧且 GPL-3.0，应借鉴方法而非照搬代码。 | D（3/6） | [→](agriculture-knowledge-graph.zh.md) |
| **Senta (SKEP)** | 当身处 PaddlePaddle／ERNIE 生态、需要带论文方法的 SKEP 情感分析 checkpoint 时用它——它锁定 EOL 的 PaddlePaddle 1.6.3，环境复原难以避免。 | D（4/6） | [→](senta.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [LSTM Neural Network for Time Series Prediction](lstm-time-series.zh.md) | ✅ | E（4/6） | 当需要可读的配套示例学习 Keras LSTM 时序预测时用它——它锁定 EOL 的 TF1／Python 3.5 且为 AGPL-3.0，应照文章重写而非直接引入。 |
| [Agriculture Knowledge Graph (AgriKG)](agriculture-knowledge-graph.zh.md) | ✅ | D（3/6） | 当需要中文领域知识图谱完整蓝图与现成数据集（NER、关系抽取、Neo4j、Django）时用它——作者声明已停止维护、技术栈陈旧且 GPL-3.0，应借鉴方法而非照搬代码。 |
| [Senta (SKEP)](senta.zh.md) | ✅ | D（4/6） | 当身处 PaddlePaddle／ERNIE 生态、需要带论文方法的 SKEP 情感分析 checkpoint 时用它——它锁定 EOL 的 PaddlePaddle 1.6.3，环境复原难以避免。 |

## 什么该放这里

面向**文本或序列**的研究 demo 与参考实现：情感预训练（[Senta](senta.zh.md)）、带 NER 与关系抽取的中文领域知识图谱流水线（[AgriKG](agriculture-knowledge-graph.zh.md)）、循环网络时序预测（[LSTM 时序预测](lstm-time-series.zh.md)）。多数锁定在已停止维护的框架上——读来学方法，不要直接引入。不含 LLM 训练（见 `llm-training`），不含生产级文档解析（见 `document-parsing`）。
