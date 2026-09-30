# kubernetes-agents

> Category node. Kubernetes-native agent control planes — agents or agent *tasks* declared and run against a cluster.
> ← back to [agent-frameworks](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **AX** | Use it when a large fleet of idle, stateful agent *tasks* must be declared as YAML (workspace, egress, model) on Kubernetes, with suspend/resume underneath — not when you want the agent itself as a CRD. | B (6/6) | [→](ax.md) |
| **kagent** | Use it when agents should be Kubernetes objects — declared in YAML, run by a controller and engine, with model config, MCP tool servers and OpenTelemetry tracing. | B (6/6) | [→](kagent.md) |
| **OpenClaw Enterprise** | Use it when many teams' stock OpenClaw or Codex agents need per-tenant namespaces, IAM, secret delivery, immutable revisions and audit on a shared Kubernetes cluster — not for one person's assistant, and not yet for a released product. | B (5/6) | [→](openclaw-enterprise.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [AX](ax.md) | ✅ | B (6/6) | kubectl-shaped Task YAML on a density runtime — Redis not etcd, no agent engine, Substrate is mandatory. |
| [kagent](kagent.md) | ✅ | B (6/6) | Agents as CRDs get Kubernetes' rollout, RBAC and audit story — at the cost of adopting a young project's resource model and giving agents real cluster credentials. |
| [OpenClaw Enterprise](openclaw-enterprise.md) | ✅ | B (5/6) | Governance around stock OpenClaw/Codex agents — IAM, secrets, revisions and audit in PostgreSQL — at the cost of Kubernetes, an external database and a month-old, unreleased control plane. |

## What belongs here

Control planes whose execution model *is* a Kubernetes cluster — either the agent itself as CRDs (kagent), the sandboxed *task* as YAML stored outside etcd (AX), or a multi-tenant governance layer that deploys stock agent runtimes onto the cluster (OpenClaw Enterprise). Code-first agent frameworks live in `agent-runtimes`; the density runtime AX sits on lives in `sandboxing`.
