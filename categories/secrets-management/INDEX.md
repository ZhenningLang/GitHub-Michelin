# secrets-management

> Category node. Self-hosted stores that issue machine credentials — API keys, certificates, database passwords — under identity, policy, and audit.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **OpenBao** | Use it when you need a self-hosted, identity-gated secrets server under MPL after HashiCorp relicensed Vault — but it is a Raft/Postgres cluster you operate, not a drop-in for every Vault plugin. | B (6/6) | [→](openbao.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [OpenBao](openbao.md) | ✅ | B (6/6) | Vault-shaped leases and a barrier under MPL-2.0 and OpenSSF governance — you run the cluster, and some Vault plugins are missing. |

## What belongs here

Servers you operate that store, issue, rotate, and revoke **machine** secrets (API keys, certificates, database passwords, encryption-as-a-service). Not human password managers (those sit with Vaultwarden under ops-infra), not git-file encryptors without a runtime (SOPS), and not hosted cloud secret APIs.
