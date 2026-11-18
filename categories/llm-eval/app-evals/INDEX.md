# app-evals

> Category node. Regression tests, RAG scores, and production traces/prompt versions for **your own** LLM app, so a prompt or model change cannot silently degrade it.
> ← back to [llm-eval](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **promptfoo** | Use it when you need declarative YAML evals plus red-teaming for your LLM app in CI. | A (6/6) | [→](promptfoo.md) |
| **Pezzo** | Use it when a small team wants one self-hosted control plane for prompt versioning plus cost/latency observability — but it looks stalled since mid-2025, so assume you'll maintain it yourself. | C (5/6) | [→](pezzo.md) |
| **DeepEval** | Use it when a Python team wants pytest-style regression tests for a RAG app or agent, scored in CI by LLM-judge metrics such as faithfulness and hallucination — but each run costs judge tokens, scores wobble, and the dashboard is the vendor's hosted platform. | A (6/6) | [→](deepeval.md) |
| **Ragas** | Use it when you change chunking, embeddings or the generator in a RAG pipeline and need per-change faithfulness and context recall/precision scores from a judge LLM — but it returns scores, not CI pass/fail gates, and no PR has merged since 2026-02. | B (6/6) | [→](ragas.md) |
| **Giskard OSS** | Use it when a Python 3.12+ team wants to pin RAG or agent failures as scenario tests with LLM-judge checks and generate attack prompts before launch — but the tabular ML scan exists only in unmaintained v2, and v3 has been GA for weeks. | B (6/6) | [→](giskard.md) |
| **Langfuse** | Use it when an LLM feature in production needs nested traces of every request plus scoring, prompt versions and datasets in a self-hostable web app — but self-hosting means running Postgres, ClickHouse, Redis and S3 storage, and some admin features are enterprise-licensed. | A (5/6) | [→](langfuse.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [promptfoo](promptfoo.md) | ✅ | A (6/6) | Use it when you need declarative YAML evals plus red-teaming for your LLM app in CI. |
| [Pezzo](pezzo.md) | ✅ | C (5/6) | Use it when a small team wants one self-hosted control plane for prompt versioning plus cost/latency observability — but it looks stalled since mid-2025, so assume you'll maintain it yourself. |
| [DeepEval](deepeval.md) | ✅ | A (6/6) | Evals as Python code in pytest with LLM-judge metrics for RAG and agents; pick promptfoo for a YAML suite run by a CLI, Ragas when you only need RAG scores. |
| [Ragas](ragas.md) | ✅ | B (6/6) | RAG-specific faithfulness and context recall/precision scores in a notebook or script; it returns scores, not CI pass/fail gates — pick DeepEval or promptfoo for gates. |
| [Giskard OSS](giskard.md) | ✅ | B (6/6) | Python scenario tests with LLM-judge checks plus generated attack prompts for RAG/agents; v3 is weeks old and the tabular scan lives only in unmaintained v2. |
| [Langfuse](langfuse.md) | ✅ | A (5/6) | Production traces plus scoring, prompt versions and datasets in one self-hostable app; self-hosting means Postgres, ClickHouse, Redis and S3, and some admin features are enterprise-licensed. |
| OpenAI Evals | 未收录 | — | Another eval framework named across the pages; not yet indexed. |

## What belongs here

Tools that test or observe **your own** LLM application across changes: assertion suites in CI, RAG metric scoring, scenario tests, and the trace + prompt-version platforms that feed them. Not attack scanning of a model or AI stack (see `security-audits`), not fixed public benchmarks (see `benchmarks`).
