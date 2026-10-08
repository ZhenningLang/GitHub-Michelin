# ops-infra

> Category node. Self-hostable infrastructure and operational tools for servers, metrics, TLS, images, proxying, remote access, and passwords.
> ← back to [dev-utilities](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Cockpit** | Use it when you need a browser-based, systemd-native admin UI for a few Linux servers. | B (5/6) | [→](cockpit.md) |
| **Telegraf** | Use it when you need one plugin-driven agent to collect and route heterogeneous metrics/logs to many backends. | A (6/6) | [→](telegraf.md) |
| **Certbot** | Use it when a sysadmin must auto-provision & renew free Let's Encrypt TLS certs — though reverse proxies' built-in auto-TLS often makes it redundant. | A (5/6) | [→](certbot.md) |
| **SlimToolkit** | Use it when you want to auto-minify & harden a bloated container image without rewriting the Dockerfile — beware it can strip dynamically-loaded files. | B (6/6) | [→](slim.md) |
| **Clash Verge Rev** | Use it when a desktop developer with a Clash-format subscription needs rule-based split routing for the whole machine, terminal tools included, via TUN mode — but it is desktop-only and TUN needs a privileged service or an elevated app. | B (6/6) | [→](clash-verge-rev.md) |
| **RustDesk** | Use it when you support a handful of remote machines and want TeamViewer-style ID connections across NAT with the broker and relay on your own server — but the open-source server has no admin console, SSO or audit logs; those are in paid Server Pro. | A (6/6) | [→](rustdesk.md) |
| **Vaultwarden** | Use it when you want your family or small team on Bitwarden's official apps with the vault on a small server you own — but you must update promptly as clients change, and there is no vendor support, SAML/SCIM, or built-in failover. | B (6/6) | [→](vaultwarden.md) |
| **Descheduler** | Use it when a Kubernetes cluster has drifted out of balance and you want a CronJob that evicts pods violating your policy so the scheduler re-places them — not a computed placement plan. | A (6/6) | [→](descheduler.md) |
| **JumpServer** | Use it when you need a self-hosted bastion / PAM that holds target credentials and records every SSH, RDP, database and Kubernetes session — but Community caps at 5,000 assets, HA/SSO/rotation are Enterprise-only, and critical CVEs arrive yearly. | B (6/6) | [→](jumpserver.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Cockpit](cockpit.md) | ✅ | B (5/6) | Use it when you need a browser-based, systemd-native admin UI for a few Linux servers. |
| [Telegraf](telegraf.md) | ✅ | A (6/6) | Use it when you need one plugin-driven agent to collect and route heterogeneous metrics/logs to many backends. |
| [Certbot](certbot.md) | ✅ | A (5/6) | Use it when a sysadmin must auto-provision & renew free Let's Encrypt TLS certs — though reverse proxies' built-in auto-TLS often makes it redundant. |
| [SlimToolkit](slim.md) | ✅ | B (6/6) | Use it when you want to auto-minify & harden a bloated container image without rewriting the Dockerfile — beware it can strip dynamically-loaded files. |
| [Clash Verge Rev](clash-verge-rev.md) | ✅ | B (6/6) | The most-used mihomo desktop GUI with layered config, at the cost of relaying all traffic through a userspace process and no phone or headless support. |
| [RustDesk](rustdesk.md) | ✅ | A (6/6) | Self-hosted brokering with NAT traversal and end-to-end encryption, at the cost of running hbbs and hbbr yourself under an open-core model. |
| [Vaultwarden](vaultwarden.md) | ✅ | B (6/6) | A tiny Rust-plus-SQLite server with no licence-gated features, at the cost of being an unofficial reimplementation without audits or guaranteed day-one client compatibility. |
| [Descheduler](descheduler.md) | ✅ | A (6/6) | Periodically evicts Kubernetes pods that violate your `DeschedulerPolicy` so kube-scheduler re-places them — in-cluster drift correction, not a computed placement plan. |
| [JumpServer](jumpserver.md) | ✅ | B (6/6) | Use it when you need a self-hosted bastion / PAM that holds target credentials and records every SSH, RDP, database and Kubernetes session — but Community caps at 5,000 assets, HA/SSO/rotation are Enterprise-only, and critical CVEs arrive yearly. |

## What belongs here

Self-hostable infrastructure and operational tools for servers, metrics, TLS, images, proxying, remote access, passwords, and in-cluster maintenance controllers such as the Kubernetes descheduler.
