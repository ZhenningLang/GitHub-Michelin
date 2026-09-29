# nlp-and-time-series

> Category node. Text and sequence research demos — sentiment pretraining, Chinese knowledge-graph pipelines, LSTM time-series forecasting — mostly on dated stacks.
> ← back to [ml-research](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **LSTM Neural Network for Time Series Prediction** | Use it as a readable article-companion example for learning Keras LSTM time-series forecasting — pinned to EOL TF1/Python 3.5 and AGPL-3.0, re-implement from the article rather than vendoring. | E (4/6) | [→](lstm-time-series.md) |
| **Agriculture Knowledge Graph (AgriKG)** | Use it as a complete blueprint and bundled datasets for a Chinese domain knowledge-graph pipeline (NER, RE, Neo4j, Django) — author-declared unmaintained on a dated GPL-3.0 stack, lift techniques not code. | D (3/6) | [→](agriculture-knowledge-graph.md) |
| **Senta (SKEP)** | Use it when working inside PaddlePaddle/ERNIE and needing SKEP sentiment checkpoints with a published method — pinned to EOL PaddlePaddle 1.6.3, so environment archaeology is unavoidable. | D (4/6) | [→](senta.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [LSTM Neural Network for Time Series Prediction](lstm-time-series.md) | ✅ | E (4/6) | Use it as a readable article-companion example for learning Keras LSTM time-series forecasting — pinned to EOL TF1/Python 3.5 and AGPL-3.0, re-implement from the article rather than vendoring. |
| [Agriculture Knowledge Graph (AgriKG)](agriculture-knowledge-graph.md) | ✅ | D (3/6) | Use it as a complete blueprint and bundled datasets for a Chinese domain knowledge-graph pipeline (NER, RE, Neo4j, Django) — author-declared unmaintained on a dated GPL-3.0 stack, lift techniques not code. |
| [Senta (SKEP)](senta.md) | ✅ | D (4/6) | Use it when working inside PaddlePaddle/ERNIE and needing SKEP sentiment checkpoints with a published method — pinned to EOL PaddlePaddle 1.6.3, so environment archaeology is unavoidable. |

## What belongs here

Research demos and reference implementations over **text or sequences**: sentiment pretraining ([Senta](senta.md)), a Chinese domain knowledge-graph pipeline with NER and relation extraction ([AgriKG](agriculture-knowledge-graph.md)), and recurrent-net forecasting ([LSTM time series](lstm-time-series.md)). Most are pinned to end-of-life frameworks — read them for method, not to vendor. Not LLM training (see `llm-training`), not production document parsing (see `document-parsing`).
