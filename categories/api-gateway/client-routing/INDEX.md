# client-routing

> Category node. Developer-client model routing, provider switching and CLI/OAuth login bridges.
> ← back to [API / AI gateways](../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Funtool** | Use it only for the exact Windows + Claude Code + NVIDIA proxy path when a prebuilt tool matters more than auditability; the current release is binary-only and cannot be rebuilt from published source. | C (5/6) | [→](funtool.md) |
| **Claude Code Router** | Use it when a developer wants to route Claude Code and other coding agents across model providers with conditional rules and fallback, from a local desktop/CLI control plane. | B (6/6) | [→](claude-code-router.md) |
| **CLIProxyAPI** | Use it when you want to reuse consumer CLI/OAuth logins as OpenAI/Gemini/Claude-compatible APIs — but the terms-of-service and account-ban risk is inherent to that reuse. | B (5/6) | [→](cliproxyapi.md) |
| **Magpie (yetone)** | Use it when one developer wants every coding agent (Claude Code, Codex, OpenCode, ~28 in all) switchable to any vendor's model from a menu bar, via single-key config edits and a local translating gateway — but it is about a week old, single-maintainer, and reusing subscriptions carries account risk. | C (5/6) | [→](magpie-model-router.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Funtool](funtool.md) | ✅ | C (5/6) | Narrow Windows proxy for Claude Code and NVIDIA models whose current implementation is distributed as an opaque binary rather than auditable source. |
| [Claude Code Router](claude-code-router.md) | ✅ | B (6/6) | Local, config-driven model routing for coding agents with a desktop UI; single-maintainer project, and a local proxy that holds provider credentials. |
| [CLIProxyAPI](cliproxyapi.md) | ✅ | B (5/6) | Broad multi-protocol API over consumer CLI/OAuth accounts; light to run, but carries inherent ToS/account risk and stores tokens on the host. |
| [Magpie (yetone)](magpie-model-router.md) | ✅ | C (5/6) | Desktop model switcher plus local Anthropic/OpenAI-translating gateway for ~28 coding agents, with subscription logins as providers; days old, single-maintainer, auto-updating. |

## What belongs here

Tools centered on a developer's coding-client model configuration, local request routing or reuse of CLI/OAuth logins. Shared service gateways with project keys, budgets, API management or MCP policy belong in the [parent category](../INDEX.md). Client routing does not establish a process sandbox or permission to reuse a subscription.
