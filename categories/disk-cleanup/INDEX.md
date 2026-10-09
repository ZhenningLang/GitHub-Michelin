# disk-cleanup

> Category node. Reclaim disk space and tidy a desktop OS — cache and build-artifact cleaners, space analyzers, duplicate finders, app uninstallers and OS debloat scripts.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **MangoDisk** | Use it when one cleaner must cover macOS, Windows and Linux and you want to read the rule behind every deleted path — accepting permanent deletion, a two-month-old codebase and a single maintainer. | C (6/6) | [→](mangodisk.md) |
| **Win11Debloat** | Use it to strip preinstalled apps, ads, Copilot and telemetry from an unmanaged Windows 10/11 PC from one checklist, with a registry backup to undo — not for domain-managed fleets, image slimming or locked-down PowerShell. | B (6/6) | [→](win11debloat.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [MangoDisk](mangodisk.md) | ✅ | C (6/6) | Auditable TOML rules, strong developer-cache coverage and three OSes in one app — but deletions are permanent, Linux support is weeks old, and the bus factor is one. |
| [Win11Debloat](win11debloat.md) | ✅ | B (6/6) | Six-year-old, very active PowerShell declutter script with per-tweak `.reg` undo files and a JSON registry backup — but it runs as admin, writes machine policies, cannot reinstall removed apps for you, and has one owner. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

End-user tools that free disk space or tidy the operating system: cache and junk cleaners, build-artifact sweepers, disk-usage analyzers, duplicate finders, app uninstallers with leftover removal, and OS declutter scripts that strip preinstalled apps, ads and telemetry from a desktop install (Win11Debloat). Not backup or sync tools, and not server-side log rotation or storage administration (see `dev-utilities/ops-infra`).
