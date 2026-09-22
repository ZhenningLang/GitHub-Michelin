# llm-eval

> Category node. Test, benchmark, and security-scan (red-team) prompts, agents, and RAG systems.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **promptfoo** | Use it when you need declarative YAML evals plus red-teaming for your LLM app in CI. | A (6/6) | [→](promptfoo.md) |
| **Pezzo** | Use it when a small team wants one self-hosted control plane for prompt versioning plus cost/latency observability — but it looks stalled since mid-2025, so assume you'll maintain it yourself. | C (4/6) | [→](pezzo.md) |
| **DeepEval** | The LLM Evaluation Framework | A (6/6) | [→](deepeval.md) |
| **Ragas** | Supercharge Your LLM Application Evaluations 🚀 | B (6/6) | [→](ragas.md) |
| **garak** | the LLM vulnerability scanner | A (6/6) | [→](garak.md) |
| **Giskard OSS** | 🐢 Open-Source Evaluation & Testing library for LLM Agents | B (6/6) | [→](giskard.md) |
| **Langfuse** | 🪢 Open source AI engineering platform: LLM evals, observability, metrics, prompt management, playground, datasets. Integrates with OpenTelemetry, LangChain, OpenAI SDK, LiteLLM, and more. 🍊YC W23 | A (4/6) | [→](langfuse.md) |
| **chatgpt-comparison-detection** | Human ChatGPT Comparison Corpus (HC3), detectors, and related AI-text detection resources. | E (4/6) | [→](chatgpt-comparison-detection.md) |
| **SWE-bench** | Use it when you need to grade coding-agent patches against real GitHub issues and their tests — each evaluation run needs Docker and a lot of disk. | B (6/6) | [→](swe-bench.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [promptfoo](promptfoo.md) | ✅ | A (6/6) | Use it when you need declarative YAML evals plus red-teaming for your LLM app in CI. |
| [Pezzo](pezzo.md) | ✅ | C (4/6) | Use it when a small team wants one self-hosted control plane for prompt versioning plus cost/latency observability — but it looks stalled since mid-2025, so assume you'll maintain it yourself. |
| Ragas / OpenAI Evals | partly indexed | — | Other LLM eval / red-team frameworks named across the pages; Ragas is indexed in this category, OpenAI Evals is not. |
| [chatgpt-comparison-detection](chatgpt-comparison-detection.md) | ✅ | E (4/6) | Dataset/detector resources for AI-text comparison; use eval frameworks when you need a maintained test runner. |


## What belongs here

Tools whose primary job is to **evaluate, benchmark, or red-team** LLM prompts/agents/RAG. Not code review (see `ai-code-review`), not training (see `llm-training`).
