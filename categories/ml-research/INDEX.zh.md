# ml-research

> 分类节点。小而自洽的 ML 研究 demo 与参考实现。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **autoresearch** | 自包含的单卡 LLM 训练脚手架，让 AI agent 通宵自主迭代 train.py——每次跑 5 分钟、按验证集 bits-per-byte 打分，只保留能降 loss 的改动。 | D（5/6） | [→](autoresearch.zh.md) |
| **llm-circuit-finder** | Python 工具集：在 GGUF 模型里搜索连续的「推理电路」层块并在前向传播中复制（不训练、不改权重），再用内置探针验证效果。 | D（5/6） | [→](llm-circuit-finder.zh.md) |
| **CLIP** | 当你需要零样本图像分类或图文互检 embedding 时用它——原始冻结参考实现；OpenCLIP 有更多权重。 | C（5/6） | [→](clip.zh.md) |
| **TaskMatrix** | 仅用于研究早期视觉工具路由 agent（Visual ChatGPT）——约 2024 年起已停更，别在其上构建。 | "?"（2/6） | [→](taskmatrix.zh.md) |
| **PyTorch-GAN** | 用来读干净的 GAN 参考实现学架构——2024 年起停更、已被扩散模型取代，不是生产代码。 | D（4/6） | [→](pytorch-gan.zh.md) |
| **LSTM Neural Network for Time Series Prediction** | 当需要可读的配套示例学习 Keras LSTM 时序预测时用它——它锁定 EOL 的 TF1／Python 3.5 且为 AGPL-3.0，应照文章重写而非直接引入。 | E（4/6） | [→](lstm-time-series.zh.md) |
| **Agriculture Knowledge Graph (AgriKG)** | 当需要中文领域知识图谱完整蓝图与现成数据集（NER、关系抽取、Neo4j、Django）时用它——作者声明已停止维护、技术栈陈旧且 GPL-3.0，应借鉴方法而非照搬代码。 | D（3/6） | [→](agriculture-knowledge-graph.zh.md) |
| **Senta (SKEP)** | 当身处 PaddlePaddle／ERNIE 生态、需要带论文方法的 SKEP 情感分析 checkpoint 时用它——它锁定 EOL 的 PaddlePaddle 1.6.3，环境复原难以避免。 | D（3/6） | [→](senta.zh.md) |
| **Depth Anything V2** | 当需要当下默认的单目深度基础模型从单张图估深度（PyTorch／Transformers）时用它——仅 Small 权重为 Apache-2.0，Base／Large／Giant 是 CC-BY-NC-4.0（非商用）。 | B（4/6） | [→](depth-anything-v2.zh.md) |
| **pymoo** | 当需要 Python 演化式多目标优化（NSGA-II/III、MOEA/D）求 Pareto 前沿时用它——若问题是凸／线性／单目标，LP 或梯度求解器要快得多。 | C（6/6） | [→](pymoo.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [autoresearch](autoresearch.zh.md) | ✅ | D（5/6） | 自包含的单卡 LLM 训练脚手架，让 AI agent 通宵自主迭代 train.py——每次跑 5 分钟、按验证集 bits-per-byte 打分，只保留能降 loss 的改动。 |
| [llm-circuit-finder](llm-circuit-finder.zh.md) | ✅ | D（5/6） | Python 工具集：在 GGUF 模型里搜索连续的「推理电路」层块并在前向传播中复制（不训练、不改权重），再用内置探针验证效果。 |
| [CLIP](clip.zh.md) | ✅ | C（5/6） | 当你需要零样本图像分类或图文互检 embedding 时用它——原始冻结参考实现；OpenCLIP 有更多权重。 |
| [TaskMatrix](taskmatrix.zh.md) | ✅ | "?"（2/6） | 仅用于研究早期视觉工具路由 agent（Visual ChatGPT）——约 2024 年起已停更，别在其上构建。 |
| [PyTorch-GAN](pytorch-gan.zh.md) | ✅ | D（4/6） | 用来读干净的 GAN 参考实现学架构——2024 年起停更、已被扩散模型取代，不是生产代码。 |
| [LSTM Neural Network for Time Series Prediction](lstm-time-series.zh.md) | ✅ | E（4/6） | 当需要可读的配套示例学习 Keras LSTM 时序预测时用它——它锁定 EOL 的 TF1／Python 3.5 且为 AGPL-3.0，应照文章重写而非直接引入。 |
| [Agriculture Knowledge Graph (AgriKG)](agriculture-knowledge-graph.zh.md) | ✅ | D（3/6） | 当需要中文领域知识图谱完整蓝图与现成数据集（NER、关系抽取、Neo4j、Django）时用它——作者声明已停止维护、技术栈陈旧且 GPL-3.0，应借鉴方法而非照搬代码。 |
| [Senta (SKEP)](senta.zh.md) | ✅ | D（3/6） | 当身处 PaddlePaddle／ERNIE 生态、需要带论文方法的 SKEP 情感分析 checkpoint 时用它——它锁定 EOL 的 PaddlePaddle 1.6.3，环境复原难以避免。 |
| [Depth Anything V2](depth-anything-v2.zh.md) | ✅ | B（4/6） | 当需要当下默认的单目深度基础模型从单张图估深度（PyTorch／Transformers）时用它——仅 Small 权重为 Apache-2.0，Base／Large／Giant 是 CC-BY-NC-4.0（非商用）。 |
| [pymoo](pymoo.zh.md) | ✅ | C（6/6） | 当需要 Python 演化式多目标优化（NSGA-II/III、MOEA/D）求 Pareto 前沿时用它——若问题是凸／线性／单目标，LP 或梯度求解器要快得多。 |
| TransformerLens / minGPT | 未收录 | — | 各页对比里点到的其他研究 demo / 可解释性库。 |

## 什么该放这里

小而自洽、用于研读学习而非投产的 **ML 研究 demo** 与参考实现。不含训练框架（见 `llm-training`）。
