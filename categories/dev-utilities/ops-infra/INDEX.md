# ops-infra

> Category node. Self-hostable infrastructure and operational tools for servers, metrics, TLS, images, proxying, remote access, and passwords.
> ← back to [dev-utilities](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Cockpit** | Use it when you need a browser-based, systemd-native admin UI for a few Linux servers. | D (6/6) | [→](cockpit.md) |
| **Telegraf** | Use it when you need one plugin-driven agent to collect and route heterogeneous metrics/logs to many backends. | A (6/6) | [→](telegraf.md) |
| **Certbot** | Use it when a sysadmin must auto-provision & renew free Let's Encrypt TLS certs — though reverse proxies' built-in auto-TLS often makes it redundant. | A (5/6) | [→](certbot.md) |
| **SlimToolkit** | Use it when you want to auto-minify & harden a bloated container image without rewriting the Dockerfile — beware it can strip dynamically-loaded files. | B (6/6) | [→](slim.md) |
| **Clash Verge Rev** | Use it when you want a modern cross-platform GUI proxy client with rule-based routing, built-in mihomo kernel, and TUN mode — but it's desktop-only and GPL-3.0 licensed. | B (6/6) | [→](clash-verge-rev.md) |
| **RustDesk** | Use it when you need an open-source, self-hosted remote desktop for your own machines across platforms — but it requires managing your own relay server or accepting P2P limitations. | A (6/6) | [→](rustdesk.md) |
| **Vaultwarden** | Use it when you want a self-hosted, Bitwarden-compatible password manager in Rust — but it is unofficial, AGPL-3.0, and the core maintainer is a single user. | B (6/6) | [→](vaultwarden.md) |
| **Descheduler** | Use it when a Kubernetes cluster has drifted out of balance and you want a CronJob that evicts pods violating your policy so the scheduler re-places them — not a computed placement plan. | A (6/6) | [→](descheduler.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Cockpit](cockpit.md) | ✅ | D (6/6) | Use it when you need a browser-based, systemd-native admin UI for a few Linux servers. |
| [Telegraf](telegraf.md) | ✅ | A (6/6) | Use it when you need one plugin-driven agent to collect and route heterogeneous metrics/logs to many backends. |
| [Certbot](certbot.md) | ✅ | A (5/6) | Use it when a sysadmin must auto-provision & renew free Let's Encrypt TLS certs — though reverse proxies' built-in auto-TLS often makes it redundant. |
| [SlimToolkit](slim.md) | ✅ | B (6/6) | Use it when you want to auto-minify & harden a bloated container image without rewriting the Dockerfile — beware it can strip dynamically-loaded files. |
| [Clash Verge Rev](clash-verge-rev.md) | ✅ | B (6/6) | Use it when you want a modern cross-platform GUI proxy client with rule-based routing, built-in mihomo kernel, and TUN mode — but it's desktop-only and GPL-3.0 licensed. |
| [RustDesk](rustdesk.md) | ✅ | A (6/6) | Use it when you need an open-source, self-hosted remote desktop for your own machines across platforms — but it requires managing your own relay server or accepting P2P limitations. |
| [Vaultwarden](vaultwarden.md) | ✅ | B (6/6) | Use it when you want a self-hosted, Bitwarden-compatible password manager in Rust — but it is unofficial, AGPL-3.0, and the core maintainer is a single user. |
| [Descheduler](descheduler.md) | ✅ | A (6/6) | Periodically evicts Kubernetes pods that violate your `DeschedulerPolicy` so kube-scheduler re-places them — in-cluster drift correction, not a computed placement plan. |

## What belongs here

Self-hostable infrastructure and operational tools for servers, metrics, TLS, images, proxying, remote access, passwords, and in-cluster maintenance controllers such as the Kubernetes descheduler.
