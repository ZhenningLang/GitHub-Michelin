# auth

> Category node. Authentication & authorization libraries — login providers and permission rules.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Authomatic** | Use it when a framework-agnostic Python app needs thin "sign in with X" via OAuth1/OAuth2/OpenID, leaving session persistence to you — but it's low-velocity and an auth lib's slow fix cadence is a security risk. | C (5/6) | [→](authomatic.md) |
| **django-rules** | Use it when Django object-level permissions are computed from logic (predicates), not stored grants, with no DB tables — but if admins must assign per-object permissions at runtime you need django-guardian instead. | B (5/6) | [→](django-rules.md) |
| **Keycloak** | Open Source Identity and Access Management For Modern Applications and Services | A (6/6) | [→](keycloak.md) |
| **Casbin** | Apache Casbin: an authorization library that supports access control models like ACL, RBAC, ABAC. | B (6/6) | [→](casbin.md) |
| **OpenFGA** | A high performance and flexible authorization/permission engine built for developers and inspired by Google Zanzibar | A (6/6) | [→](openfga.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Authomatic](authomatic.md) | ✅ | C (5/6) | Use it when a framework-agnostic Python app needs thin "sign in with X" via OAuth1/OAuth2/OpenID, leaving session persistence to you — but it's low-velocity and an auth lib's slow fix cadence is a security risk. |
| [django-rules](django-rules.md) | ✅ | B (5/6) | Use it when Django object-level permissions are computed from logic (predicates), not stored grants, with no DB tables — but if admins must assign per-object permissions at runtime you need django-guardian instead. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

Libraries whose primary job is **authentication or authorization** — login/OAuth providers, permission/rule engines.
