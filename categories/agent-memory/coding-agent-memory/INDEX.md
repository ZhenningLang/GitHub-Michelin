# coding-agent-memory

> Category node. Memory bolted onto coding-agent harnesses you already run — Claude Code, Codex, Cursor, OpenCode — via hooks, plugins, MCP, or a pasted prompt block driving a CLI: session capture, compression, and injection on a developer's machine, plus shared context stores for teams of agents.
> ← back to [agent-memory](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Claude Subconscious** | Use it when you want a background Letta agent to give Claude Code cross-session memory via hooks. | C (5/6) | [→](claude-subconscious.md) |
| **claude-mem** | Use it when your coding agent loses context across sessions and you want local hook/MCP-captured memory compressed and injected back in. | B (6/6) | [→](claude-mem.md) |
| **ByteRover CLI** | Use it when you want a portable, structured memory layer for coding agents with git-like versioning and cloud sync — but it is extremely young (2025-06) and the license is ambiguous. | D (6/6) | [→](byterover.md) |
| **OpenViking** | Use it when several coding agents or a team must share one context store holding both your documents and their long-term memory, and you can run a server — but the main project is AGPL-3.0 and the repo self-labels alpha. | B (6/6) | [→](openviking.md) |
| **Beacon** | Use it when agent knowledge is trapped per-harness — you want one local trace of every coding session and review-gated lessons any harness can load. | B (6/6) | [→](agent-beacon.md) |
| **Engram** | Use it when you run several coding agents and want them all to share one local memory the agent itself writes and searches over MCP — a single Go binary and SQLite file, keyword search, no background capture. | B (5/6) | [→](engram.md) |
| **backpass** | Use it when your `AGENTS.md`/`CLAUDE.md` has drifted from what your coding agents actually get wrong, and you want edits mined from the transcripts already on disk — each backed by quotes from two sessions and accepted one by one, under a token budget. | B (6/6) | [→](backpass.md) |
| **OptMem** | Use it when you want coding-agent memory with zero moving parts — one pasted prompt block, one dependency-free Python script, an agent-curated append-only log — and you can live with voluntary capture, regex-only recall, and no license. | D (5/6) | [→](optmem.md) |
| **deja-vu** | Use it when your agents re-debug fixes you already made in another agent, and you want memory built from the transcripts 35 harnesses already wrote to disk — no capture step, no LLM, lexical search that predates the install. | B (6/6) | [→](deja-vu.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Claude Subconscious](claude-subconscious.md) | ✅ | C (5/6) | Background Letta agent whispering memory into Claude Code via hooks; an exploratory demo, not production. |
| [claude-mem](claude-mem.md) | ✅ | B (6/6) | Hook/MCP memory wired into a coding agent's session lifecycle (not a model-agnostic app memory API); reported star count is unverified. |
| [ByteRover CLI](byterover.md) | ✅ | D (6/6) | Portable structured memory for coding agents with git-like versioning and cloud sync; extremely young (2025-06) and license ambiguity (NOASSERTION vs Elastic 2.0). |
| [OpenViking](openviking.md) | ✅ | B (6/6) | Self-hosted context database that unifies document RAG and session memory behind one `viking://` tree with per-user isolation; costs a server, two model dependencies and AGPL-3.0. |
| [Beacon](agent-beacon.md) | ✅ | B (6/6) | Cross-harness session capture with human-approved lessons; young vendor-backed repo with a hosted funnel. |
| [Engram](engram.md) | ✅ | B (5/6) | Agent-agnostic MCP memory in one Go binary + SQLite FTS5; no extra runtime or LLM bill, but recall depends on the agent choosing to save, and the project is young with very high release churn. |
| [backpass](backpass.md) | ✅ | B (6/6) | Offline batch that proposes evidence-gated edits to the memory file from existing transcripts of 7 agents; no daemon or key of its own, but traces go to your logged-in model, and it is five weeks old with a single maintainer. |
| [OptMem](optmem.md) | ✅ | D (5/6) | One prompt block plus one stdlib-only Python file: the agent itself writes one-line memories to an append-only log and reads a summary tree at wake; nothing automatic, regex-only recall, and no license. |
| [deja-vu](deja-vu.md) | ✅ | B (6/6) | Lexical index of the on-disk transcripts of 35 listed harnesses — searchable history from before you installed it, one Go binary with no LLM in the recall path; young, one maintainer, author-run benchmarks. |

## What belongs here

Memory layers that attach to **coding-agent harnesses you run** (Claude Code, Codex, Cursor, OpenCode, …) through hooks, plugins, MCP, endpoint capture, or a pasted prompt block the agent itself follows — local per-developer stores (claude-mem, claude-subconscious, ByteRover, Beacon, Engram, OptMem), transcript-mined edits to the memory file itself (backpass) and shared multi-agent context servers (OpenViking). The subject is the coding session: decisions, conventions, traces, lessons. Not memory APIs you embed in your own product (see `app-memory`), not graph-shaped engines (see `graph-memory`).
