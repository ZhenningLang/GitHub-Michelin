# kubernetes-agents

> Category node. Kubernetes-native agent frameworks — agents declared, deployed and governed as cluster resources.
> ← back to [agent-frameworks](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **kagent** | Use it when agents should be Kubernetes objects — declared in YAML, run by a controller and engine, with model config, MCP tool servers and OpenTelemetry tracing. | B (6/6) | [→](kagent.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [kagent](kagent.md) | ✅ | B (6/6) | Agents as CRDs get Kubernetes' rollout, RBAC and audit story — at the cost of adopting a young project's resource model and giving agents real cluster credentials. |

## What belongs here

Frameworks whose execution model *is* Kubernetes — agents, tools and model configuration expressed as cluster resources and reconciled by a controller. Code-first agent frameworks and runtimes live in `agent-runtimes`; execution layers that multiplex stateful agent sandboxes live in `sandboxing`.
