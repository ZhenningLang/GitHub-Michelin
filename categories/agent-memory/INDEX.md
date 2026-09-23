# agent-memory

> Category node. Persistent, LLM-agnostic memory an agent reads/writes across sessions.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Mem0** | Use it when your LLM agent must remember users across sessions without bloating the prompt context. | A (6/6) | [→](mem0.md) |
| **Memori** | Use it when you want LLM-agnostic persistent agent memory captured by wrapping your existing client. | B (5/6) | [→](memori.md) |
| **Claude Subconscious** | Use it when you want a background Letta agent to give Claude Code cross-session memory via hooks. | C (5/6) | [→](claude-subconscious.md) |
| **claude-mem** | Use it when your coding agent loses context across sessions and you want local hook/MCP-captured memory compressed and injected back in. | B (6/6) | [→](claude-mem.md) |
| **ByteRover CLI** | Use it when you want a portable, structured memory layer for coding agents with git-like versioning and cloud sync — but it is extremely young (2025-06) and the license is ambiguous. | D (6/6) | [→](byterover.md) |
| **Letta (MemGPT)** | Platform for stateful agents: AI with advanced memory that can learn and self-improve over time. | B (6/6) | [→](letta.md) |
| **Zep** | Zep \| Examples, Integrations, & More | A (4/6) | [→](zep.md) |
| **Graphiti** | Build Real-Time Knowledge Graphs for AI Agents | B (6/6) | [→](graphiti.md) |
| **LangMem** | Use it when you need LangMem for the agent-memory category. | B (5/6) | [→](langmem.md) |
| **Cognee** | Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine. | A (6/6) | [→](cognee.md) |
| **OpenViking** | Use it when several coding agents or a team must share one context store holding both your documents and their long-term memory, and you can run a server — but the main project is AGPL-3.0 and the repo self-labels alpha. | B (6/6) | [→](openviking.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Mem0](mem0.md) | ✅ | A (6/6) | Use it when your LLM agent must remember users across sessions without bloating the prompt context. |
| [Memori](memori.md) | ✅ | B (5/6) | Use it when you want LLM-agnostic persistent agent memory captured by wrapping your existing client. |
| [Claude Subconscious](claude-subconscious.md) | ✅ | C (5/6) | Use it when you want a background Letta agent to give Claude Code cross-session memory via hooks. |
| [claude-mem](claude-mem.md) | ✅ | B (6/6) | Hook/MCP memory wired into a coding agent's session lifecycle (not a model-agnostic app memory API); reported star count is unverified. |
| [ByteRover CLI](byterover.md) | ✅ | D (6/6) | Portable structured memory for coding agents with git-like versioning and cloud sync; extremely young (2025-06) and license ambiguity (NOASSERTION vs Elastic 2.0). |
| [Letta (MemGPT)](letta.md) | ✅ | B (6/6) | Stateful-agent platform whose memory OS the runtime owns; pick it when Letta should own the agent loop, not when you only want context under an existing harness. |
| [Zep](zep.md) | ✅ | A (4/6) | Temporal knowledge-graph memory for facts about users that expire or get superseded; a backend for app memory rather than a coding-agent hook layer. |
| [Cognee](cognee.md) | ✅ | A (6/6) | Self-hosted knowledge-graph memory engine for document-shaped agent memory; heavier to run than a file or SQLite store. |
| [OpenViking](openviking.md) | ✅ | B (6/6) | Self-hosted context database that unifies document RAG and session memory behind one `viking://` tree with per-user isolation; costs a server, two model dependencies and AGPL-3.0. |

## What belongs here

Infrastructure whose primary job is to **store and recall** agent memory across sessions, independent of the model. Not task/issue tracking (see `agent-tooling`), not RAG document retrieval (see `rag-retrieval`).
