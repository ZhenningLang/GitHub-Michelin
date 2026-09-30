# inference-benchmarks

> Category node. Measure how fast models are served — throughput, latency, and interactivity across engines, GPUs, and parallelism settings — rather than how good their answers are.
> ← back to [llm-inference](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **InferenceX** | Use it when you must choose GPUs or serving engines for a frontier model and want continuously re-run, recipe-traceable throughput-vs-latency curves across NVIDIA and AMD — not when you need to benchmark your own server (its full pipeline needs Slurm GPU clusters) or want a consortium-audited result. | B (6/6) | [→](inferencex.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [InferenceX](inferencex.md) | ✅ | B (6/6) | Already-run, cross-vendor, multi-node serving curves re-measured as engine images move; operated by one analysis firm on its own Slurm fleet, so reproducing it yourself is heavy. |

## What belongs here

Projects whose primary job is **measuring LLM serving performance** — load-generation clients, benchmark suites, and continuously published performance results for inference engines and accelerators. Not quality/accuracy evaluation of models or apps (see `llm-eval`), and not the serving engines themselves, even when they ship a bench command (see `serving-engines`).
