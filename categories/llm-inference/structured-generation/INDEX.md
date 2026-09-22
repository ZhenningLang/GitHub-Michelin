# structured-generation

> Category node. Constrain the decoder so a model's output matches a structure — JSON Schema, regex, a context-free grammar, or a tool-call wrapper — instead of parsing and retrying.
> ← back to [llm-inference](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **XGrammar** | Use it when you control the model's logits and must guarantee parseable output — a JSON Schema, a regex, a grammar, or a tool call — and want the tightest mask latency available; skip it if you only call a hosted API or already serve on an engine that embeds it. | B (6/6) | [→](xgrammar.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [XGrammar](xgrammar.md) | ✅ | B (6/6) | The default grammar-constrained decoding engine inside vLLM/SGLang/TensorRT-LLM/MLC-LLM: near-free masks and the broadest grammar front-ends, at the cost of a C++ binary dependency and a pre-1.0 API. |

## What belongs here

Libraries and engines whose primary job is **constraining what a model may generate** — token masking against a schema, regex, grammar or tool-call structure. Not the serving engines themselves, even when they embed one of these (see `serving-engines`), and not local runtimes that ship a grammar mode as a side feature (see `local-runtimes`). If your problem is orchestrating several generations rather than constraining one, that is a framework concern, not this node.
