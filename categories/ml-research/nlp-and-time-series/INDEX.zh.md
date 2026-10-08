# nlp-and-time-series

> 分类节点。文本与序列类研究 demo——情感预训练、中文知识图谱流水线、LSTM 时序预测——大多基于陈旧技术栈。
> ← 返回 [ml-research](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **LSTM Neural Network for Time Series Prediction** | 当你想跟着配套文章一步步看一个 Keras 堆叠 LSTM 在正弦波和标普 500 数据上训练、出图时用它——但它钉死在 2018 年前后的 TensorFlow 1.10 与 Python 3.5 上，2019 年起已冻结，且为 AGPL-3.0。 | E（4/6） | [→](lstm-time-series.zh.md) |
| **Agriculture Knowledge Graph (AgriKG)** | 当你要一份跑通的中文领域知识图谱整链示例（爬虫、实体打标、关系抽取、Neo4j、Django 问答）外加现成农业数据时用它——但作者已声明停止维护，技术栈陈旧，代码是 GPL-3.0。 | D（3/6） | [→](agriculture-knowledge-graph.zh.md) |
| **Senta (SKEP)** | 当你身处 PaddlePaddle 栈、要用发布的中英文 checkpoint 复现或扩展 SKEP 情感论文时用它——但它钉死在 Paddle 1.6.3 加 CUDA 10.1 上，自 2020 年起无提交，百度更新的 NLP 工作在 PaddleNLP。 | D（4/6） | [→](senta.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [LSTM Neural Network for Time Series Prediction](lstm-time-series.zh.md) | ✅ | E（4/6） | 换来一个建立 LSTM 预测直觉的可读基线；代价是装环境像考古、精度没有竞争力——真要预测用 Darts 或 GluonTS，标普演示也不是交易信号。 |
| [Agriculture Knowledge Graph (AgriKG)](agriculture-knowledge-graph.zh.md) | ✅ | D（3/6） | 换来一套端到端蓝图和可直接学的语料；代价是要复活老旧的 Django／py2neo 栈并受 copyleft 约束——借方法，别照搬代码。 |
| [Senta (SKEP)](senta.zh.md) | ✅ | D（4/6） | 换来有论文支撑、中文基准上精度不错的情感模型；代价是一套笨重过时的 GPU 环境——PyTorch 或 HF 栈上用 Hugging Face 情感模型摩擦更小。 |

## 什么该放这里

面向**文本或序列**的研究 demo 与参考实现：情感预训练（[Senta](senta.zh.md)）、带 NER 与关系抽取的中文领域知识图谱流水线（[AgriKG](agriculture-knowledge-graph.zh.md)）、循环网络时序预测（[LSTM 时序预测](lstm-time-series.zh.md)）。多数锁定在已停止维护的框架上——读来学方法，不要直接引入。不含 LLM 训练（见 `llm-training`），不含生产级文档解析（见 `document-parsing`）。
