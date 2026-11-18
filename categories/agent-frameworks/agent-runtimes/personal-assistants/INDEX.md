# personal-assistants

> Category node. Packaged assistants for personal use: phone, voice, desktop and workspace forms remain here; long-lived messaging assistants and rosters of named AI teammates have their own child categories.
> ← back to [agent-runtimes](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **messaging-daemons** | You want a long-lived assistant on your own host or board, reached mainly through existing messaging channels and scheduled jobs. | [→](messaging-daemons/INDEX.md) |
| **ai-teammates** | You want a standing roster of several named bots — each with its own role, model, memory and often its own computer — that you message one by one or in group chats. | [→](ai-teammates/INDEX.md) |

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Cindy** | Continue one Claude Code, Codex or Pi session from your phone and other computers; multi-device features need a vendor account and relay, with analytics on by default. | B (6/6) | [→](cindy.md) |
| **LobsterAI** | You want an office task to work on local files and return through your chat channel; LobsterAI adds a desktop session, artifact and approval layer around an OpenClaw runtime. | B (6/6) | [→](lobsterai.md) |
| **Atomic Agent** | Local-model workstation operator with compact tool prompts; developer preview and default-on analytics. | B (6/6) | [→](atomic-agent.md) |
| **OpenHuman** | Use it when you want a local-first personal assistant that ingests your mail, calendar and repos into Markdown memory on a 20-minute loop and can be forced offline in its Rust core — but it's 7 months old, one author holds most commits, and it's GPL-3.0-only. | B (6/6) | [→](openhuman.md) |
| **OpenMuse** | Use it when you want a self-hosted personal agent with a working computer — persistent browser you can take over, sandboxed Linux terminal, durable approval-gated tasks — but it refuses to start without a CopilotKit cloud key, and the alpha is 12 days old with zero releases. | B (4/6) | [→](openmuse.md) |
| **OpenWorker** | Use it when you want a desktop AI coworker that finishes real tasks with your own model key behind approval gates and a per-call audit trail — but the command sandbox is opt-in, one-click connectors use a closed OAuth broker, and it is a 71-day-old beta. | B (6/6) | [→](openworker.md) |
| **Raven** | Use it when you want one surface that splits a big brief into a task graph and hands the nodes to built-in research/code/design/on-call agents or to Claude Code and Codex — but it's a 4-month-old pre-alpha, the sandbox is off by default, and DAG nodes can bypass it (#796). | B (6/6) | [→](raven.md) |
| **OpenMinis** | Use it when you want an AI agent that does errands on the phone itself — a Linux shell inside an iOS/Android app plus Health, Calendar, Reminders and HomeKit as tools, with your own cloud model — but no model runs on-device, privacy tools default to Bypass, and the repo is a no-PR mirror with one visible committer. | C (6/6) | [→](openminis.md) |
| **Jarvis** | Join room conversations with local speech models and temporary spoken context; non-commercial license and desktop audio setup are the price. | C (5/6) | [→](jarvis.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Cindy](cindy.md) | Indexed | B (6/6) | Full desktop assistant with a phone controller, memory and teams; its account and multi-device backend remain vendor services. |
| [Messaging daemons](messaging-daemons/INDEX.md) | Sub-category | — | Existing chat channels and scheduled jobs are the primary entry points; phone, voice, desktop and workspace forms remain below. |
| [AI teammates](ai-teammates/INDEX.md) | Sub-category | — | A roster of named, long-lived bots you message individually or in groups; one-owner assistants and single host agents stay here. |
| [LobsterAI](lobsterai.md) | ✅ | B (6/6) | You want an office task to work on local files and return through your chat channel; LobsterAI adds a desktop session, artifact and approval layer around an OpenClaw runtime. |
| [Atomic Agent](atomic-agent.md) | ✅ | B (6/6) | Managed llama.cpp and session-scoped approvals; model hardware and outbound reporting need explicit choices. |
| [OpenHuman](openhuman.md) | ✅ | B (6/6) | Local-first desktop assistant that buys context by ingesting your accounts on a 20-minute loop instead of waiting for a learning loop; GPL-3.0-only, heavy build, vendor account by default. |
| [OpenMuse](openmuse.md) | ✅ | B (4/6) | CopilotKit's MIT personal-agent app with a persistent browser and bounded Linux computer; buys that working surface at the price of a mandatory Intelligence (hosted) project key. |
| [OpenWorker](openworker.md) | ✅ | B (6/6) | Desktop cowork app by Andrew Ng's team: human-only floors, standing-approval ladder and audit provenance, ~15 model providers signed-out; sandbox off by default, two-person core, weak issue response. |
| [Raven](raven.md) | ✅ | B (6/6) | EverMind's host agent (nanobot fork) that orchestrates its own specialists and 13 third-party agents as a DAG, with EverOS memory; buys breadth at the price of pre-alpha churn and a sandbox you must enable and verify. |
| [OpenMinis](openminis.md) | ✅ | C (6/6) | Free BYOK phone agent with an in-app Alpine sandbox (iSH on iOS, PRoot on Android) and native bridges to Apple/Android data; buys no-server device integration at the price of iOS background limits, a one-command-at-a-time sandbox and permissive default permissions. |
| [Jarvis](jarvis.md) | ✅ | C (5/6) | Join room conversations with local speech models and temporary spoken context; non-commercial license and desktop audio setup are the price. |

## What belongs here

Packaged assistants for personal use: phone agents, voice companions, desktop coworkers and workspaces. A chat adapter or scheduler alone does not determine the category. Assistants primarily deployed as long-lived services behind existing messaging channels go in [messaging-daemons](messaging-daemons/INDEX.md). Products built around a roster of several named bots you message individually or in group chats go in [ai-teammates](ai-teammates/INDEX.md).
