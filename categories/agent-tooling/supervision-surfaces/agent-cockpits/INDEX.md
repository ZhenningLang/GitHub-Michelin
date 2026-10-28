# agent-cockpits

> Category node. View and steer tasks, sessions, teams or business work; these interfaces do not imply a shared execution runtime.
> ← back to [supervision-surfaces](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **OpenBot (Nightly Labs)** | Keep persistent multi-provider assistants, file handoffs and queued messages on one desktop; source-available noncommercial license and full host access by default. | B (4/6) | [→](nightly-openbot.md) |
| **Kandev** | Review parallel coding tasks in a server-first browser workbench with configurable workflow gates and executors; constrain the default listener and archive cleanup. | B (6/6) | [→](kandev.md) |
| **Nezha** | Supervise local Claude Code/Codex tasks with terminal, session and Git views; select worktree mode explicitly and accept startup hook edits. | C (6/6) | [→](nezha.md) |
| **FounderOS** | Put income, inbox and agent work on one local operator screen; real services and agent execution remain separate, and first-run data is fictional. | B (4/6) | [→](founderos.md) |
| **dsh-TUI** | Your DeepSeek Harness session has tools, approvals and background work scattered across text; dsh-TUI projects that state into terminal cards, panels and a session browser. | B (5/6) | [→](dsh-tui.md) |
| **Agor** | Coordinate mixed coding agents and colleagues on live branch boards; BSL, database and execution-security operations remain yours. | D (6/6) | [→](agor.md) |
| **Agent Orchestrator** | Use it when you supervise several parallel coding agents on real branches and want a desktop control plane that isolates each in a git worktree and auto-routes CI/review/conflict feedback — but it's ~4.5 months old, pre-1.0, single-User-owned, with a loopback-no-auth daemon. | B (6/6) | [→](agent-orchestrator.md) |
| **Hermes Workspace** | Use it when you run Nous's hermes-agent and want its state as a web console — chat, memory, skills, terminal, tmux swarm dispatch, phone via PWA/Tailscale — but its enhanced panes are keyed to the Hermes gateway/dashboard APIs and it's ~6 months old. | B (5/6) | [→](hermes-workspace.md) |
| **Ekko Studio** | Use it when you run Hermes Agent *and* coding agents like Claude Code/Codex and want one local console — chats, @mention group rooms, a workflow canvas with approval gates, files and terminal — but it's BSL-1.1 (non-commercial until 2029), relicensed from MIT a month in, ~5.5 months old and mostly one author. | D (6/6) | [→](ekko-studio.md) |
| **CloudCLI (Claude Code UI)** | Use it when your brain is Claude Code / Codex / Cursor CLI and you want a browser/mobile cockpit for those sessions (files, terminal, git) — but it's AGPL-3.0-or-later and single-operator shaped. | B (6/6) | [→](claudecodeui.md) |
| **Pi Web** | Use it when your coding agent is pi and you want a browser workspace over its own on-disk sessions, models and project files — resume/branch conversations, inspect diffs and worktrees — but it's ~6 months old, pre-1.0, single-maintainer, and keyed to pi's data directory. | B (6/6) | [→](pi-web.md) |
| **Paperclip** | Use it when you run a standing team of existing agents (Claude Code, Codex, OpenClaw, shell/HTTP bots) and need one self-hosted board that wakes them on heartbeats, locks each ticket to one agent and pauses anyone over budget — but it's ~7 months old, has 12 published security advisories, and Windows local runs are broken. | B (5/6) | [→](paperclip.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [OpenBot (Nightly Labs)](nightly-openbot.md) | Indexed | B (4/6) | Persistent teammate inboxes and browser/file context rather than branch review; PolyForm Noncommercial, not MIT or host isolation. |
| [Kandev](kandev.md) | 已收录 | B (6/6) | Native server with task workflows, worktrees and remote execution; AGPL, optional authentication and destructive archive lifecycle require deliberate setup. |
| [Nezha](nezha.md) | ✅ | C (6/6) | Tauri desktop for a two-agent task/Git loop; optional worktrees, global Codex hooks, no process persistence across app exit. |
| [FounderOS](founderos.md) | ✅ | B (4/6) | Broad MIT business cockpit over SQLite and external services, not a turnkey autonomous company or multi-user workspace. |
| [dsh-TUI](dsh-tui.md) | ✅ | B (5/6) | Your DeepSeek Harness session has tools, approvals and background work scattered across text; dsh-TUI projects that state into terminal cards, panels and a session browser. |
| [Agor](agor.md) | ✅ | D (6/6) | Coordinate mixed coding agents and colleagues on live branch boards; BSL, database and execution-security operations remain yours. |
| [Agent Orchestrator](agent-orchestrator.md) | ✅ | B (6/6) | A desktop control plane that fans work out to many agents in worktrees and routes CI/review feedback back — breadth over one artifact. |
| [Hermes Workspace](hermes-workspace.md) | ✅ | B (5/6) | Vendor-shaped web console for one agent's whole state; the richest view, the most coupled to its host's APIs. |
| [Ekko Studio](ekko-studio.md) | ✅ | D (6/6) | One local switchboard over Hermes plus six coding-agent CLIs — group rooms and workflow canvas included — paid for with a non-commercial source-available licence. |
| [CloudCLI (Claude Code UI)](claudecodeui.md) | ✅ | B (6/6) | Operate sessions from a browser or phone (files, terminal, git) — steering, not review. |
| [Pi Web](pi-web.md) | ✅ | B (6/6) | Browser workspace over pi's own on-disk state — sessions, models, files — the MIT cockpit for exactly one brain. |
| [Paperclip](paperclip.md) | ✅ | B (5/6) | An org-and-budget control plane over agents you already have — heartbeats, atomic checkout, spend caps, approvals — not a diff-review loop; young, and loopback/tailnet only until you've reviewed its security history. |

## What belongs here

Ongoing supervision organized around tasks, sessions, branches, teams or business work. Business operator screens belong here too; projects need not be execution runtimes. For review of one artifact or a behavior-understanding check, use [human-review-gates](../human-review-gates/INDEX.md).
