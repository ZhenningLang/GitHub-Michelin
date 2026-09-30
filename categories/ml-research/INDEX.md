# ml-research

> Category node. Small, self-contained ML research demos and reference implementations, split by purpose into three sub-categories; three projects that fit none of them sit directly on this node.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Category | Use when | Route |
| --- | --- | --- |
| **research-automation** | Pipelines and harnesses that automate the research loop itself — an agent proposes, runs and scores experiments (or whole papers). | [→](research-automation/INDEX.md) |
| **vision-and-multimodal** | Vision and vision-language research models and reference code — image embeddings, monocular depth, GAN architectures, early visual tool-routing agents. | [→](vision-and-multimodal/INDEX.md) |
| **nlp-and-time-series** | Text and sequence research demos — sentiment pretraining, Chinese knowledge-graph pipelines, LSTM time-series forecasting — mostly on dated stacks. | [→](nlp-and-time-series/INDEX.md) |

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **context-language-models** | Use it to study or benchmark letting an agent's model edit its own live context (a mirrored transcript file it rewrites with bash) on Harbor tasks, with FLOPs accounting and an SGLang KV-reuse patch — paper code under CC BY-NC 4.0, non-commercial only. | D (4/6) | [→](context-language-models.md) |
| **llm-circuit-finder** | Python toolkit that searches a GGUF model for contiguous reasoning-circuit layer blocks and duplicates them in the forward pass (no training, no weight edits), validated with built-in probes. | D (4/6) | [→](llm-circuit-finder.md) |
| **pymoo** | Use it as the de-facto Python library for evolutionary multi-objective optimization (NSGA-II/III, MOEA/D) to find Pareto fronts — for convex/linear/single-objective problems an LP/gradient solver is far faster. | B (6/6) | [→](pymoo.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [context-language-models](context-language-models.md) | ✅ | D (4/6) | Use it to study or benchmark letting an agent's model edit its own live context (a mirrored transcript file it rewrites with bash) on Harbor tasks, with FLOPs accounting and an SGLang KV-reuse patch — paper code under CC BY-NC 4.0, non-commercial only. |
| [llm-circuit-finder](llm-circuit-finder.md) | ✅ | D (4/6) | Python toolkit that searches a GGUF model for contiguous reasoning-circuit layer blocks and duplicates them in the forward pass (no training, no weight edits), validated with built-in probes. |
| [pymoo](pymoo.md) | ✅ | B (6/6) | Use it as the de-facto Python library for evolutionary multi-objective optimization (NSGA-II/III, MOEA/D) to find Pareto fronts — for convex/linear/single-objective problems an LP/gradient solver is far faster. |
| TransformerLens / minGPT | 未收录 | — | Other research demos / interpretability libs named across the pages. |

## What belongs here

Small, self-contained **ML research demos** and reference implementations meant to read and learn from, not to productionize. Pipelines that automate the research loop itself live in `research-automation/`, vision and vision-language models in `vision-and-multimodal/`, text and sequence demos in `nlp-and-time-series/`; projects that fit none of those (the self-managed-context agent harness [context-language-models](context-language-models.md), the LLM layer-surgery experiment [llm-circuit-finder](llm-circuit-finder.md), the evolutionary multi-objective optimization library [pymoo](pymoo.md)) sit directly on this node. Not training frameworks (see `llm-training`).
