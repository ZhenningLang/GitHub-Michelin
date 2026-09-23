# function-calling

> Category node. Models and serving stacks whose primary job is turning natural-language requests into schema-constrained tool/function calls.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Functionary** | Use it only as the historical reference for open JSON-Schema function calling — it is deprecated; for production serve a current model or go on-device. | B (4/6) | [→](functionary.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Functionary](functionary.md) | ✅ | B (4/6) | The canonical early open function-calling model (JSON-Schema tools, vLLM/SGLang serving) — now deprecated; pattern source only. |
| FunctionGemma (Google) / cloud tool APIs | 未收录 | — | Other function-calling models and APIs named on the page — a model card and hosted services, not indexed repos. |

## What belongs here

**Tool / function calling** as the primary subject — models, serving stacks, and schema/grammar contracts that fill function arguments from natural language. Not general chatbots or on-device runtimes (see `on-device-ml` / `llm-inference`), not agent frameworks (see `agent-frameworks`).
