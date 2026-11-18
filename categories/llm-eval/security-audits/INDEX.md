# security-audits

> Category node. Scan a model, an agent or a whole self-hosted AI stack for known jailbreaks, injections, CVEs and permission breaches before someone else finds them.
> ← back to [llm-eval](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **garak** | Use it when you must sign off a model before launch and want a repeatable scan of known jailbreak, injection, data-leak and malware-generation attacks with per-probe failure rates — but it tests the model, not your app's answer quality or whole deployment. | A (6/6) | [→](garak.md) |
| **AI-Infra-Guard** | Use it when the audit surface is your whole self-hosted AI stack — live-service CVEs, MCP servers, agent skills, jailbreak evals — from one Tencent-built platform, not a single model endpoint. | B (6/6) | [→](ai-infra-guard.md) |
| **iFixAi** | Use it when you need a fast, off-the-shelf audit of whether an agent stays inside its declared roles, tool permissions and honesty rules — 60 fixed inspections, a judge from a different vendor, an A–F grade; young and LLM-judged, with an 18k-star count its usage numbers do not back up. | B (4/6) | [→](ifixai.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [AI-Infra-Guard](ai-infra-guard.md) | ✅ | B (6/6) | Whole-stack AI security self-examination (infra CVEs, MCP, skills, jailbreaks) as a deployed platform; pick garak/promptfoo when a CLI against one model or your own app is enough. |
| [iFixAi](ifixai.md) | ✅ | B (4/6) | Fixed governance checklist for agents (roles, tool permissions, honesty) with a cross-vendor LLM judge; pick promptfoo when you need your own assertions in CI, garak for attack breadth. |
| [garak](garak.md) | ✅ | A (6/6) | Research-derived probe catalog against the model itself with per-probe failure rates; it does not test your app's answers or the deployment around the model. |

## What belongs here

Tools whose primary output is a **security or governance verdict**: red-team probe catalogs against a model, CVE and supply-chain scans of an AI stack, role/permission audits of an agent. Not regression tests you author for your own app (see `app-evals` — promptfoo's red-team mode lives there because its primary job is app evals), not public capability benchmarks (see `benchmarks`), not runtime guardrails (see `agent-governance`).
