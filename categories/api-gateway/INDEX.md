# api-gateway

> Category node. API / AI gateways that route, secure, rate-limit, and govern service and LLM traffic.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Kong Gateway** | OpenResty/Nginx API gateway whose plugin layer makes one reverse-proxy a programmable edge for REST/microservice traffic and, since 3.x, LLM/MCP traffic. | B (6/6) | [→](kong.md) |
| **Funtool** | Use it only for the exact Windows + Claude Code + NVIDIA proxy path when a prebuilt tool matters more than auditability; the current release is binary-only and cannot be rebuilt from published source. | C (5/6) | [→](funtool.md) |
| **HarnessRouter** | Use it when a product backend must run Codex, Claude Code, Hermes and other harnesses behind one OpenAI Responses-compatible API — but it is about six weeks old, the UHP standard is single-vendor, and CE sessions share one container. | B (5/6) | [→](harnessrouter.md) |
| **LiteLLM** | Use it when several apps or teams need one OpenAI-compatible endpoint with virtual keys, budgets, spend tracking and failover — but the full feature set is not all MIT (`enterprise/` is commercial). | A (4/6) | [→](litellm.md) |
| **Claude Code Router** | Use it when a developer wants to route Claude Code and other coding agents across model providers with conditional rules and fallback, from a local desktop/CLI control plane. | B (6/6) | [→](claude-code-router.md) |
| **CLIProxyAPI** | Use it when you want to reuse consumer CLI/OAuth logins as OpenAI/Gemini/Claude-compatible APIs — but the terms-of-service and account-ban risk is inherent to that reuse. | B (5/6) | [→](cliproxyapi.md) |
| **APISIX** | Use it when you want an ASF-governed gateway with etcd-backed live configuration and in-process plugins — you also operate the etcd control plane. | A (6/6) | [→](apisix.md) |
| **Envoy** | Use it when you need an xDS-driven L4/L7 data plane and will supply your own control plane — it is lower-level than a turnkey API gateway. | A (6/6) | [→](envoy.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Kong Gateway](kong.md) | ✅ | B (6/6) | OpenResty/Nginx API gateway whose plugin layer makes one reverse-proxy a programmable edge for REST/microservice traffic and, since 3.x, LLM/MCP traffic. |
| [Funtool](funtool.md) | ✅ | C (5/6) | Narrow Windows proxy for Claude Code and NVIDIA models whose current implementation is distributed as an opaque binary rather than auditable source. |
| [HarnessRouter](harnessrouter.md) | ✅ | B (5/6) | One OpenAI Responses-compatible API over many agent harnesses, paid for with a ~6-week-old codebase, a single-vendor protocol, and container-shared session isolation. |
| [LiteLLM](litellm.md) | ✅ | A (4/6) | The LLM gateway with the richest provider and cost/governance surface, at the price of PostgreSQL + Redis ops and a commercial `enterprise/` boundary. |
| [Claude Code Router](claude-code-router.md) | ✅ | B (6/6) | Local, config-driven model routing for coding agents with a desktop UI; single-maintainer project, and a local proxy that holds provider credentials. |
| [CLIProxyAPI](cliproxyapi.md) | ✅ | B (5/6) | Broad multi-protocol API over consumer CLI/OAuth accounts; light to run, but carries inherent ToS/account risk and stores tokens on the host. |
| [APISIX](apisix.md) | ✅ | A (6/6) | ASF top-level gateway on NGINX/OpenResty with etcd-backed live config and a broad in-process plugin layer; the control plane is a hard dependency you operate. |
| [Envoy](envoy.md) | ✅ | A (6/6) | CNCF-graduated L4/L7 data plane driven by xDS; you bring the control plane and the API-management policy layer. |
| Tyk / KrakenD / New API | 未收录 | — | Other self-hosted gateways named across the pages. |

## What belongs here

**API / AI gateways** that sit in front of services or LLMs to route, secure, rate-limit, and observe traffic. Not agent frameworks (see `agent-frameworks`).
