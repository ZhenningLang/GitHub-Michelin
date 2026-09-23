# osint

> Category node. OSINT reconnaissance tools — account existence, username dossiers, and
> platform-specific investigation from emails/usernames. Authorization-first: every tool here
> probes third-party services; use only within legal bounds and explicit engagement scope.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **holehe** | Use it to probe whether an email has accounts on 120+ sites via register/forgot-password endpoints without alerting the target — but it is unmaintained since 2024-09, so absorb the methodology and module table, or fork and re-verify modules. | D (5/6) | [→](holehe.md) |
| **socialscan** | Use it for accurate available/taken checks of emails and usernames by querying platform registration endpoints directly — coverage is only ~11 platforms and releases are sporadic. | D (4/6) | [→](socialscan.md) |
| **Maigret** | Use it to build a username dossier across 3000+ sites with ID extraction, recursive search, and HTML/PDF/XMind reports — the most actively maintained pick in this category. | A (6/6) | [→](maigret.md) |
| **Sherlock** | Use it for simple, battle-tested username checks across 480+ social networks with a huge community — coarser profile-page signals than Maigret, no dossier extraction. | A (6/6) | [→](sherlock.md) |
| **GHunt** | Use it for authenticated deep-dive OSINT on a Google account (Gmail address → profile, Maps/reviews traces) — powerful, but AGPL-3.0, needs your Google session cookies, and carries high ToS/legal risk. | B (5/6) | [→](ghunt.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [holehe](holehe.md) | ✅ | D (5/6) | Widest email→account coverage (120+ sites) and the richest leaked-recovery-info method set, but stalled since 2024-09 — module rot is the price of breadth. |
| [socialscan](socialscan.md) | ✅ | D (4/6) | Registration-endpoint queries give the cleanest available/taken verdicts, but only ~11 platforms are covered. |
| [Maigret](maigret.md) | ✅ | A (6/6) | Deepest username dossiers (3000+ sites, ID extraction, recursion, reports), but a heavy dependency surface and slow full scans. |
| [Sherlock](sherlock.md) | ✅ | A (6/6) | Simplest and most community-tested username checker (480+ sites), but profile-page heuristics produce false positives/negatives. |
| [GHunt](ghunt.md) | ✅ | B (5/6) | Only tool here that sees inside the Google ecosystem, but it requires an authenticated Google session and carries the highest legal/ToS risk. |

## What belongs here

**OSINT reconnaissance** repositories: email→account-existence probes, username→dossier collectors,
and platform-specific investigation frameworks. Tools whose primary job is discovering *whether and
where* an identity has registered accounts, and what public traces those accounts leave. Adjacent:
`web-scraping` (generic content extraction), `deep-research` (multi-source research agents).
