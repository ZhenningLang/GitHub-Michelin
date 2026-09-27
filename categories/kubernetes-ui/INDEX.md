# kubernetes-ui

> Category node. UIs to inspect and operate Kubernetes clusters — terminal, desktop, or in-cluster web.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **k9s** | Use it when cluster ops must stay in a terminal — live tables, logs, exec — and a browser is the wrong surface. | A (5/6) | [→](k9s.md) |
| **Headlamp** | Use it when a team needs a shared browser console with RBAC-aware buttons under kubernetes-sigs. | A (6/6) | [→](headlamp.md) |
| **Radar** | Use it when you need topology, Helm/GitOps, audit, and MCP from a local Apache-2.0 binary with no account. | B (6/6) | [→](radar.md) |
| **Freelens** | Use it when you want the old Lens desktop window as MIT software, without a Mirantis account. | A (6/6) | [→](freelens.md) |
| **Lens** | Use it only when the team already pays for Lens Desktop / Teamwork; the GitHub OSS tree is retired. | C (4/6) | [→](lens.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [k9s](k9s.md) | ✅ | A (5/6) | Keyboard TUI over the API; seven years active; no GUI, no shared URL, no MCP. |
| [Headlamp](headlamp.md) | ✅ | A (6/6) | In-cluster or desktop web UI with plugins and SIG governance; diagnosis features are not all built in. |
| [Radar](radar.md) | ✅ | B (6/6) | Local Go binary with topology, GitOps, audit, MCP; eight months old, vendor-backed. |
| [Freelens](freelens.md) | ✅ | A (6/6) | MIT Electron fork of Open Lens; laptop IDE, not an in-cluster console. |
| [Lens](lens.md) | ✅ | C (4/6) | Commercial Mirantis IDE; this repo is not the product you download. |

## What belongs here

Tools whose **primary job** is a human (or agent) UI onto a Kubernetes cluster: browse resources, logs, exec, Helm/GitOps as cluster operations. Not metrics dashboards (see `observability`), not TUI *libraries* (see `terminal-ui`), not in-cluster controllers that rebalance pods (see `dev-utilities` → Descheduler).
