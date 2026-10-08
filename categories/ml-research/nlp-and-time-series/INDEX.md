# nlp-and-time-series

> Category node. Text and sequence research demos — sentiment pretraining, Chinese knowledge-graph pipelines, LSTM time-series forecasting — mostly on dated stacks.
> ← back to [ml-research](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **LSTM Neural Network for Time Series Prediction** | Use it when you want to follow an article step by step and watch a Keras stacked LSTM train and plot predictions on sine-wave and S&P 500 data — but it is pinned to 2018-era TensorFlow 1.10 and Python 3.5, frozen since 2019, and AGPL-3.0. | E (4/6) | [→](lstm-time-series.md) |
| **Agriculture Knowledge Graph (AgriKG)** | Use it as a worked Chinese domain knowledge-graph example — crawler, entity labeling, relation extraction, Neo4j, Django Q&A — with bundled agricultural data — but the author has declared it unmaintained, the stack is dated, and the code is GPL-3.0. | D (3/6) | [→](agriculture-knowledge-graph.md) |
| **Senta (SKEP)** | Use it when you need to reproduce or extend the SKEP sentiment paper with its released Chinese/English checkpoints inside a PaddlePaddle stack — but it is pinned to Paddle 1.6.3 with CUDA 10.1, idle since 2020, and Baidu's newer NLP lives in PaddleNLP. | D (4/6) | [→](senta.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [LSTM Neural Network for Time Series Prediction](lstm-time-series.md) | ✅ | E (4/6) | Buys a readable baseline for LSTM forecasting intuition; costs install archaeology and non-competitive accuracy — Darts or GluonTS for real forecasts, and the S&P demo is no trading signal. |
| [Agriculture Knowledge Graph (AgriKG)](agriculture-knowledge-graph.md) | ✅ | D (3/6) | Buys an end-to-end blueprint and ready corpora to learn from; costs reviving an old Django/py2neo stack under copyleft terms — lift the method, not the code. |
| [Senta (SKEP)](senta.md) | ✅ | D (4/6) | Buys strong reported Chinese sentiment accuracy from a published method; costs a heavy, dated GPU environment — on PyTorch or HF stacks a Hugging Face sentiment model is less friction. |

## What belongs here

Research demos and reference implementations over **text or sequences**: sentiment pretraining ([Senta](senta.md)), a Chinese domain knowledge-graph pipeline with NER and relation extraction ([AgriKG](agriculture-knowledge-graph.md)), and recurrent-net forecasting ([LSTM time series](lstm-time-series.md)). Most are pinned to end-of-life frameworks — read them for method, not to vendor. Not LLM training (see `llm-training`), not production document parsing (see `document-parsing`).
