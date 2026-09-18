# prompt-engineering

> Leaf of [agent-skills](../INDEX.md). Writing, generating, and collecting prompts for any AI tool — generator skills, community prompt libraries, and prompt-engineering knowledge bases.
> ← up to [agent-skills](../INDEX.md) · root [route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Collections in this leaf

| Collection | Use when | Health | Page |
| --- | --- | --- | --- |
| **prompt-master** | A Claude skill that generates one-shot optimized prompts for 30+ AI tools (LLMs, coding agents, image/video/voice AI) via intent extraction, template routing, and a 37-pattern anti-pattern checklist. | B (4/6) | [→](prompt-master.md) |
| **prompts.chat** | Self-hostable community platform for sharing, discovering, and collecting ready-made prompts (f.k.a. Awesome ChatGPT Prompts). | A (4/6) | [→](prompts-chat.md) |
| **Prompt Engineering Guide** | Reference knowledge base (guides, papers, notebooks) for learning prompt/context engineering, RAG, and agent techniques. | C (4/6) | [→](prompt-engineering-guide.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [prompt-master](prompt-master.md) | ✅ | B (4/6) | Generates a tailored prompt per request for a specific target tool; choose it over copying library prompts when the task is novel — but it is single-maintainer and its per-model routing advice decays fast. |
| [prompts.chat](prompts-chat.md) | ✅ | A (4/6) | Browse and copy community-voted ready-made prompts, or self-host a prompt library for your org; no generation pipeline, quality varies per prompt. |
| [prompt-engineering-guide](prompt-engineering-guide.md) | ✅ | C (4/6) | Learn the underlying techniques and research; it teaches principles rather than producing paste-ready prompts, and commit cadence has slowed. |

## What belongs here

Skills and repos whose primary job is **prompt engineering itself** — generating, improving, collecting, or teaching prompts for LLMs and other AI tools. Domain-specific prompt packs (writing, design, security) stay in their task leaves; this leaf is for tool-agnostic prompt work.
