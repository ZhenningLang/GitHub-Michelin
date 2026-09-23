# kubernetes-agents

> Category node. Kubernetes-native agent control planes — agents or agent *tasks* declared and run against a cluster.
> ← back to [agent-frameworks](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **AX** | Use it when a large fleet of idle, stateful agent *tasks* must be declared as YAML (workspace, egress, model) on Kubernetes, with suspend/resume underneath — not when you want the agent itself as a CRD. | B (5/6) | [→](ax.md) |
| **kagent** | Use it when agents should be Kubernetes objects — declared in YAML, run by a controller and engine, with model config, MCP tool servers and OpenTelemetry tracing. | B (5/6) | [→](kagent.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [AX](ax.md) | ✅ | B (5/6) | kubectl-shaped Task YAML on a density runtime — Redis not etcd, no agent engine, Substrate is mandatory. |
| [kagent](kagent.md) | ✅ | B (5/6) | Agents as CRDs get Kubernetes' rollout, RBAC and audit story — at the cost of adopting a young project's resource model and giving agents real cluster credentials. |

## What belongs here

Control planes whose execution model *is* a Kubernetes cluster — either the agent itself as CRDs (kagent) or the sandboxed *task* as YAML stored outside etcd (AX). Code-first agent frameworks live in `agent-runtimes`; the density runtime AX sits on lives in `sandboxing`.
