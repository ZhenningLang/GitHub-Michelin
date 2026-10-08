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
| **skills-scanner** | Zero-dependency Python CLI that inventories skills, commands and MCP configs across Claude Code, Claude Desktop, Cursor and Windsurf, runs offline rules, and diffs against a SQLite baseline. Dormant since 2026-05 and not on PyPI: a pattern source, not a dependency. | C (5/6) | [→](skills-scanner.md) |
| **agent-guard** | Pre-install gate skill that routes skills, MCP packages, npm/PyPI/Go/cargo packages, release binaries and install scripts to SkillSpector, Cisco mcp-scanner, GuardDog, OpenSSF package-analysis or VirusTotal, and merges them into one fail-closed exit code; no detection of its own, one author, 3 stars. | C (5/6) | [→](agent-guard.md) |
| **Claude Skills Security Guide** | A written catalogue of twelve Claude skill attack vectors with a manual and six defanged example attacks, plus three demo-grade copy-in defence skills (regex scanner, hash manifest, text sanitizer); unmaintained since 2026-03, read it, do not gate on it. | C (4/5) | [→](claude-skills-security-guide.md) |
| **Cisco MCP Scanner** | Cisco's open scanner for MCP servers: pulls every tool, prompt and resource description from a live server, a client config or a saved JSON and flags injection/poisoning text with local YARA rules, plus optional LLM, Cisco-API and LLM-based source-code checks; reports only, no CI exit code or SARIF. | B (6/6) | [→](mcp-scanner.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [agent-governance-toolkit](agent-governance-toolkit.md) | ✅ | B (6/6) | Broad Microsoft-backed agent governance stack; strong for production policy/audit, heavy if you only need a small middleware check. |
| [SkillSpector](skillspector.md) | ✅ | B (5/6) | Narrow install-time scanner for skill artifacts; pair with runtime governance when tool-call policy and audit are the real problem. |
| [Snyk Agent Scan](agent-scan.md) | ✅ | A (6/6) | One command inventories and risk-scores everything installed, including live MCP tool descriptions; closed hosted detectors, unstable output, and it executes the servers it scans. |
| [claude-skill-audit](claude-skill-audit.md) | ✅ | C (5/6) | Whole-config pattern scan you can read end to end and run offline; unproven, dormant, and blind to scripts, non-English injection and common key formats. |
| [skills-scanner](skills-scanner.md) | ✅ | C (5/6) | Machine-wide inventory plus drift baseline with no dependencies; shallow regex/AST rules, one author, silent since 2026-05, install from git only. |
| [agent-guard](agent-guard.md) | ✅ | C (5/6) | One scan-then-install gate across many target types and every local agent; pays with a deep toolchain (uv, Docker, a privileged container) and an unadopted one-author wrapper over upstream scanners. |
| [Claude Skills Security Guide](claude-skills-security-guide.md) | ✅ | C (4/5) | Threat vocabulary, training material and attack fixtures for testing a real scanner; its own scanner rates its defence skills CRITICAL, and nothing runs unless you invoke it. |
| [Cisco MCP Scanner](mcp-scanner.md) | ✅ | B (6/6) | MCP-server-specific checks with rules you can read and an offline mode over saved tool lists; launches the stdio servers it scans, needs an LLM key for anything beyond pattern matching, and you build the CI pass/fail yourself. |


## What belongs here

Governance, policy enforcement, identity, sandboxing, reliability controls, and install-time security gates for AI agents.
