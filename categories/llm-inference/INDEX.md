# llm-inference

> Category node. High-performance LLM/model inference & serving engines, and AI systems languages.
> Split into sub-categories by **what part of the job you own**: serving many concurrent API requests on server hardware, running one user on their own machine, or constraining what a generation is allowed to produce.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **Serving Engines** | You are putting a model behind an API on server-class GPUs and need batching, prefix caching, or autoscaling. | [→](serving-engines/INDEX.md) |
| **Local Runtimes** | You are running a model for yourself on a laptop, desktop, or single box and need it to just work locally. | [→](local-runtimes/INDEX.md) |
| **Structured Generation** | You control the model's logits and the output must conform to a JSON Schema, regex, grammar, or tool-call structure. | [→](structured-generation/INDEX.md) |

## Comparison matrix

| Option | Type | One-line tradeoff |
| --- | --- | --- |
| [Serving Engines](serving-engines/INDEX.md) | Sub-category | vLLM, SGLang, TensorRT-LLM, LMDeploy, TGI, Ray Serve, BentoML, Modular — throughput and concurrency at the cost of GPU-class ops. |
| [Local Runtimes](local-runtimes/INDEX.md) | Sub-category | llama.cpp, Ollama, Magnitude, omlx, MTPLX — zero-ops local inference at the cost of single-user scale. |
| [Structured Generation](structured-generation/INDEX.md) | Sub-category | XGrammar — guarantee parseable output by masking the decoder, at the cost of a C++ dependency and a pre-1.0 API. |

## What belongs here

Engines and systems languages whose primary job is **LLM/model inference and serving**. Not on-device/edge runtimes (see `on-device-ml`), not LLM fine-tuning (see `llm-training`). Pick a sub-category by scale or role: server-side concurrency (`serving-engines`), single-user local execution (`local-runtimes`), or constraining the decoder's output (`structured-generation`).
