# auth

> Category node. Authentication & authorization libraries — login providers and permission rules.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Authomatic** | Use it when a Flask, Django or other WSGI app needs thin "sign in with Google/GitHub" across OAuth 1.0a, OAuth 2.0 and OpenID while you own sessions — but releases stalled at 1.3.0 (2024) and the unreleased 2.0 drops OAuth 1.0a. | C (5/6) | [→](authomatic.md) |
| **django-rules** | Use it when Django object-level permissions follow from logic such as "authors edit their own posts" and you want composable predicates with no DB tables — but if admins must grant per-object permissions at runtime, use django-guardian. | B (4/6) | [→](django-rules.md) |
| **Keycloak** | Use it when many apps each keep their own login and you want one self-hosted server for passwords, 2FA, social and SAML logins that issues signed role tokens — but it needs JVM, database and cache operations, and is overkill for one app. | A (6/6) | [→](keycloak.md) |
| **Casbin** | Use it when role checks are scattered across handlers and you want one model file plus policy rows enforced by an in-process library call, in Go or seven other languages — but it does no authentication, and the policy set must fit in application memory. | B (6/6) | [→](casbin.md) |
| **OpenFGA** | Use it when access follows relationships (folders shared with teams, editors inheriting down a tree) across several services and "list everything Anne can see" times out — but every membership or share change must also be written as a tuple, or answers go wrong. | A (6/6) | [→](openfga.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Authomatic](authomatic.md) | ✅ | C (5/6) | Buys one framework-agnostic interface over many providers' login handshakes; costs persistence you write yourself and slow security and provider fixes in an auth-critical library. |
| [django-rules](django-rules.md) | ✅ | B (4/6) | Buys declarative, testable rules that drive has_perm, decorators, templates and DRF from one place; costs any stored grants, and predicates re-run on every check. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

Libraries whose primary job is **authentication or authorization** — login/OAuth providers, permission/rule engines.
