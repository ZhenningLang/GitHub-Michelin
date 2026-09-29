# prompt-engineering

> Leaf of [agent-skills](../INDEX.md). Writing, generating, and collecting prompts for any AI tool — generator skills, community prompt libraries, and prompt-engineering knowledge bases.
> ← up to [agent-skills](../INDEX.md) · root [route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Collections in this leaf

| Collection | Use when | Health | Page |
| --- | --- | --- | --- |
| **prompt-master** | A Claude skill that generates one-shot optimized prompts for 30+ AI tools (LLMs, coding agents, image/video/voice AI) via intent extraction, template routing, and a 37-pattern anti-pattern checklist. | B (4/5) | [→](prompt-master.md) |
| **prompts.chat** | Self-hostable community platform for sharing, discovering, and collecting ready-made prompts (f.k.a. Awesome ChatGPT Prompts). | B (5/6) | [→](prompts-chat.md) |
| **Prompt Engineering Guide** | Reference knowledge base (guides, papers, notebooks) for learning prompt/context engineering, RAG, and agent techniques. | C (4/5) | [→](prompt-engineering-guide.md) |
| **Claude Code System Prompts** | Read and diff every built-in prompt of a given Claude Code version (tool descriptions, subagents, skills, reminders), extracted from the compiled package on each release with a per-version changelog. | B (4/5) | [→](claude-code-system-prompts.md) |
| **MuseAI-Skills** | Unofficial, unlicensed snapshot of Meta Muse's 68 agent skills plus permission manifests, eval scenarios and runtime scripts — read it to study production connector/consent design; nothing installs or runs. | D (4/5) | [→](museai-skills.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [prompt-master](prompt-master.md) | ✅ | B (4/5) | Generates a tailored prompt per request for a specific target tool; choose it over copying library prompts when the task is novel — but it is single-maintainer and its per-model routing advice decays fast. |
| [prompts.chat](prompts-chat.md) | ✅ | B (5/6) | Browse and copy community-voted ready-made prompts, or self-host a prompt library for your org; no generation pipeline, quality varies per prompt. |
| [prompt-engineering-guide](prompt-engineering-guide.md) | ✅ | C (4/5) | Learn the underlying techniques and research; it teaches principles rather than producing paste-ready prompts, and commit cadence has slowed. |
| [claude-code-system-prompts](claude-code-system-prompts.md) | ✅ | B (4/5) | Tells you which Claude Code built-in instruction changed in a release; read-only, Claude Code only, and the text is Anthropic's proprietary prompts redistributed by a third party. |
| [MuseAI-Skills](museai-skills.md) | ✅ | D (4/5) | A reference corpus for how a shipped consumer agent writes connector skills, permission defaults and evals; unofficial redistribution with no licence, frozen at 2026-09, and non-runnable outside Meta's container. |

## What belongs here

Skills and repos whose primary job is **prompt engineering itself** — generating, improving, collecting, or teaching prompts for LLMs and other AI tools. Domain-specific prompt packs (writing, design, security) stay in their task leaves; this leaf is for tool-agnostic prompt work.
