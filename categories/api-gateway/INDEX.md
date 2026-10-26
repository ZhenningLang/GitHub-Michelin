# api-gateway

> Category node. API / AI gateways that route, secure, rate-limit, and govern service and LLM traffic.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **Client Routing** | One developer needs coding-client model routing, provider switching or CLI/OAuth login bridging rather than shared service governance. | [→](client-routing/INDEX.md) |

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Kong Gateway** | OpenResty/Nginx API gateway whose plugin layer makes one reverse-proxy a programmable edge for REST/microservice traffic and, since 3.x, LLM/MCP traffic. | B (6/6) | [→](kong.md) |
| **HarnessRouter** | Use it when a product backend must run Codex, Claude Code, Hermes and other harnesses behind one OpenAI Responses-compatible API — but it is about six weeks old, the UHP standard is single-vendor, and CE sessions share one container. | B (5/6) | [→](harnessrouter.md) |
| **LiteLLM** | Use it when several apps or teams need one OpenAI-compatible endpoint with virtual keys, budgets, spend tracking and failover — but the full feature set is not all MIT (`enterprise/` is commercial). | A (4/6) | [→](litellm.md) |
| **APISIX** | Use it when you want an ASF-governed gateway with etcd-backed live configuration and in-process plugins — you also operate the etcd control plane. | A (6/6) | [→](apisix.md) |
| **Envoy** | Use it when you need an xDS-driven L4/L7 data plane and will supply your own control plane — it is lower-level than a turnkey API gateway. | A (6/6) | [→](envoy.md) |
| **TokenHub** | Use it when model access must become governed infrastructure — project keys, quotas, routing policy, audit and provider-bill reconciliation in one self-hosted Go gateway; it is ~3 months old at v0.9.0. | B (6/6) | [→](tokenhub.md) |
| **vLLM Semantic Router** | Use it when a platform team serves several models and wants the model chosen per request from its content (domain, difficulty, jailbreak, PII) by YAML policy behind Envoy — it is pre-1.0 and still needs a gateway for keys and rate limits. | B (5/6) | [→](vllm-semantic-router.md) |
| **Monid** | Use it when your agent calls many paid data and media APIs (search, scraping, enrichment, video) and you want each vendor described in one declarative contract that a single engine validates, calls and meters — but the `discover` routing, single key and pricing are hosted and closed, and the repo is about six weeks old. | B (6/6) | [→](monid.md) |
| **Agentgateway** | Several assistants need one MCP endpoint with configured federation and list/call policy; this is not a sandbox or automatic endpoint privacy. | B (6/6) | [→](agentgateway.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Kong Gateway](kong.md) | ✅ | B (6/6) | OpenResty/Nginx API gateway whose plugin layer makes one reverse-proxy a programmable edge for REST/microservice traffic and, since 3.x, LLM/MCP traffic. |
| [HarnessRouter](harnessrouter.md) | ✅ | B (5/6) | One OpenAI Responses-compatible API over many agent harnesses, paid for with a ~6-week-old codebase, a single-vendor protocol, and container-shared session isolation. |
| [LiteLLM](litellm.md) | ✅ | A (4/6) | The LLM gateway with the richest provider and cost/governance surface, at the price of PostgreSQL + Redis ops and a commercial `enterprise/` boundary. |
| [APISIX](apisix.md) | ✅ | A (6/6) | ASF top-level gateway on NGINX/OpenResty with etcd-backed live config and a broad in-process plugin layer; the control plane is a hard dependency you operate. |
| [Envoy](envoy.md) | ✅ | A (6/6) | CNCF-graduated L4/L7 data plane driven by xDS; you bring the control plane and the API-management policy layer. |
| [TokenHub](tokenhub.md) | ✅ | B (6/6) | Governance-first self-hosted AI gateway (Go/SQLite): project keys, quotas, routing, audit and provider-bill reconciliation; very young (v0.9.x) and author-dominated. |
| [vLLM Semantic Router](vllm-semantic-router.md) | ✅ | B (5/6) | Content-aware model selection as an Envoy ExtProc decision layer with its own classifier models; adds a hop and a multi-service stack, and leaves credentials, rate limits and replica scheduling to other layers. |
| [Monid](monid.md) | ✅ | B (6/6) | Open connector standard and engine behind an "OpenRouter for agent tools": ~700 vendor endpoints as declarative files with per-call metering; routing, single key and most of the catalog stay in the closed hosted platform. |
| [Agentgateway](agentgateway.md) | Yes | B (6/6) | MCP-aware federation and explicit list/call policy, not OS isolation; identities, TLS, policy configuration and upstream trust remain your responsibility. |
| Tyk / KrakenD / New API | 未收录 | — | Other self-hosted gateways named across the pages. |

## What belongs here

**API / AI gateways** that sit in front of services, LLMs or MCP servers to route, secure, rate-limit, and observe traffic. Developer-client routing and login bridges belong in [Client Routing](client-routing/INDEX.md); shared service governance stays here. Not agent frameworks (see `agent-frameworks`).
