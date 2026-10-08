# agent-governance

> Category node. AI-agent governance, policy enforcement, identity, sandboxing, and reliability controls for AI agents.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **agent-governance-toolkit** | Microsoft's public-preview governance toolkit for AI agents: policy-gated tool calls, identity/trust, audit/compliance, MCP security gateway, SRE controls, and multi-language SDKs. | B (6/6) | [→](agent-governance-toolkit.md) |
| **SkillSpector** | NVIDIA's security scanner for AI agent skills: pre-install CLI/MCP scanning for prompt injection, exfiltration, dangerous scripts, MCP poisoning, dependencies, and SARIF/JSON evidence. | B (5/6) | [→](skillspector.md) |
| **Snyk Agent Scan** | Snyk's machine-wide scanner for installed MCP servers and agent skills across 14 coding agents; discovery is local, but every verdict comes from Snyk's hosted, closed analysis API (account, quota, data egress). | A (6/6) | [→](agent-scan.md) |
| **claude-skill-audit** | Offline regex scanner for a whole Claude Code `.claude/` directory — skills, agents, hooks, permissions, MCP config, secrets — in zero-dependency TypeScript; one author, 0 stars, shallow checks, use as a quick lint only. | C (5/6) | [→](claude-skill-audit.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [agent-governance-toolkit](agent-governance-toolkit.md) | ✅ | B (6/6) | Broad Microsoft-backed agent governance stack; strong for production policy/audit, heavy if you only need a small middleware check. |
| [SkillSpector](skillspector.md) | ✅ | B (5/6) | Narrow install-time scanner for skill artifacts; pair with runtime governance when tool-call policy and audit are the real problem. |
| [Snyk Agent Scan](agent-scan.md) | ✅ | A (6/6) | One command inventories and risk-scores everything installed, including live MCP tool descriptions; closed hosted detectors, unstable output, and it executes the servers it scans. |
| [claude-skill-audit](claude-skill-audit.md) | ✅ | C (5/6) | Whole-config pattern scan you can read end to end and run offline; unproven, dormant, and blind to scripts, non-English injection and common key formats. |


## What belongs here

Governance, policy enforcement, identity, sandboxing, reliability controls, and install-time security gates for AI agents.
