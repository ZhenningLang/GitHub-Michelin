# vendor-agents

> First-party coding runtimes from model vendors. This is a product-origin route, not a claim of model lock-in; see each page for custom-endpoint support.
> ← back to [terminal-agents](../INDEX.md) · root: [category route](../../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Codex** | Use it when you already pay for ChatGPT and want that plan to run a sandboxed edit-test-fix loop in your terminal — but custom providers must speak the Responses API, OpenAI accepts no external pull requests, and the 0.x interface changes almost daily. | A (5/6) | [→](codex.md) |
| **Gemini CLI** | Use it when you want a terminal agent you sign into with an ordinary Google account and use free within a daily quota, with a context window large enough for big repos — but it talks only to Gemini, with no offline or local-model path. | A (6/6) | [→](gemini-cli.md) |
| **ZCode** | Use one supplied coding runtime across desktop, web and CLI, with dependency-aware workflows and content-bound project-hook trust; no default OS sandbox and no native Computer Use in the open build. | C (5/6) | [→](zcode.md) |

## Comparison matrix

| Project | In index | Health | Deciding tradeoff |
|---|---|---|---|
| [Codex](codex.md) | ✅ | A (5/6) | Prefer the OpenAI first-party loop and default OS sandbox; custom providers must support Responses. |
| [Gemini CLI](gemini-cli.md) | ✅ | A (6/6) | Prefer Google sign-in and the free daily quota; the runtime is Gemini-only and sandboxing is opt-in. |
| [ZCode](zcode.md) | ✅ | C (5/6) | Supplies its own desktop/web/CLI agent with persisted workflows; you own execution isolation and source-build compliance checks. |

## What belongs here

First-party coding runtimes from model vendors. This is a product-origin route, not a claim of model lock-in; see each page for custom-endpoint support.
