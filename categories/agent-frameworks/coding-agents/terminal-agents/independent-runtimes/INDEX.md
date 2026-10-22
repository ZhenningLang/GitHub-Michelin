# independent-runtimes

> Independent/community coding runtimes and supervision surfaces for existing agents. Choose by runtime or supervision mechanism; this does not imply no commercial backing or universal model support.
> ← back to [terminal-agents](../INDEX.md) · root: [category route](../../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Apache Maka (Incubating)** | After an agent crashes, its last tool action should not vanish with the window; Maka records model, tool and permission events in a local runtime ledger shared by desktop and terminal clients. | B (6/6) | [→](maka.md) |
| **aider** | Use it when you want an AI to edit the files you name in your git repo from the terminal, with any model and each change landed as an undoable commit — but it is essentially one maintainer and has not released since 2025-08. | B (6/6) | [→](aider.md) |
| **Freebuff** | Use it when you want a terminal coding agent with no subscription or API key — hosted models paid for by text ads and a daily allowance, with prompts analyzed for ads and no shell-command approval gate. | B (6/6) | [→](freebuff.md) |
| **Letta Code** | Use it when you want one long-lived terminal coding agent that remembers your repo and your corrections across sessions, in git-versioned memory it rewrites itself — but Letta Cloud is the default backend, it ships more than a release a day, and its behaviour drifts as its memory changes. | B (6/6) | [→](letta-code.md) |
| **OmO** | You hand a coding agent a big job and spend the evening steering it back on course. OmO takes the steering over: type `mass ulw` and the job becomes a graph of parallel workers, each on the model that fits it, verified before anything is called done. | B (5/6) | [→](oh-my-openagent.md) |
| **Open Interpreter** | Use it when you want a Codex-style terminal agent to drive cheaper models such as Kimi, GLM, DeepSeek or Qwen with the harness each family is tuned for — but it is a months-old Codex fork, and its famous Python REPL is gone. | A (6/6) | [→](open-interpreter.md) |
| **OpenCode** | Use it when you want one MIT-licensed terminal coding agent that keeps your workflow while swapping among 75+ providers, local models or a ChatGPT or Copilot login — but its defaults let edits and shell commands run without asking, and Claude Pro/Max plans are off-limits. | A (5/6) | [→](opencode.md) |
| **Pi** | Use it when you want a minimal terminal agent whose behaviour comes from files in your repo — skills, prompt templates, TypeScript extensions it can also write itself — and you accept owning the sandbox. | B (5/6) | [→](pi.md) |
| **Prime Agent** | Use it when a long coding session is rotting in the chat window and you want the model to program over a persistent Python kernel, spawn children, and keep running after you detach. | B (6/6) | [→](prime-agent.md) |
| **T3 Code** | Use it when one local GUI should drive already authenticated Codex, Claude, Cursor, and OpenCode CLIs. | A (6/6) | [→](t3code.md) |

## Comparison matrix

| Project | In index | Health | Deciding tradeoff |
|---|---|---|---|
| [Apache Maka (Incubating)](maka.md) | ✅ | B (6/6) | Prefer a shared Runtime Host and recorded execution events; the ledger does not prove patch correctness. |
| [aider](aider.md) | ✅ | B (6/6) | Prefer named-file pair programming and undoable commits over longer autonomous loops. |
| [Freebuff](freebuff.md) | ✅ | B (6/6) | Prefer a hosted model catalog without managing keys or bills; review advertising and code-disclosure costs. |
| [Letta Code](letta-code.md) | ✅ | B (6/6) | Prefer agent-edited cross-session memory over provider breadth or a minimal core. |
| [OmO](oh-my-openagent.md) | ✅ | B (5/6) | Prefer pre-wired orchestration, memory and model mixing; accept its source-available license. |
| [Open Interpreter](open-interpreter.md) | ✅ | A (6/6) | Prefer per-model harnesses on Codex machinery over a different agent loop. |
| [OpenCode](opencode.md) | ✅ | A (5/6) | Prefer provider switching and autonomous plan/build modes over commit-per-edit pair programming. |
| [Pi](pi.md) | ✅ | B (5/6) | Prefer a minimal core with file-based resources and TypeScript extensions; own execution isolation. |
| [Prime Agent](prime-agent.md) | ✅ | B (6/6) | Prefer programmatic context folding and detachable long runs; accept a multi-process runtime without a default sandbox. |
| [T3 Code](t3code.md) | ✅ | A (6/6) | Prefer one GUI supervising existing coding agents rather than replacing their runtimes. |

## What belongs here

Independent/community coding runtimes and supervision surfaces for existing agents. Choose by runtime or supervision mechanism; this does not imply no commercial backing or universal model support.
