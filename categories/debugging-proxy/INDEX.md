# debugging-proxy

> Category node. HTTP(S)/WebSocket debugging proxies — capture, inspect, rewrite, and mock traffic.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **whistle** | Use it when a web/mobile dev must capture, inspect, rewrite, and mock HTTP(S)/WebSocket traffic via a rule-based web UI — a dev proxy, not a production gateway or scraping pool. | B (6/6) | [→](whistle.md) |
| **AnyProxy** | Use it when you debug app traffic and want a Node.js MITM proxy whose request and response rewrites are plain JavaScript rule files — but master has been frozen since 2020, so prefer whistle for new work. | C (4/6) | [→](anyproxy.md) |
| **mitmproxy** | Use it when you must see and modify the exact HTTPS requests a client you don't control sends, and want to script that in Python — but certificate-pinned apps reject it unless you unpin them first. | A (6/6) | [→](mitmproxy.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [whistle](whistle.md) | ✅ | B (6/6) | Use it when a web/mobile dev must capture, inspect, rewrite, and mock HTTP(S)/WebSocket traffic via a rule-based web UI — a dev proxy, not a production gateway or scraping pool. |
| [AnyProxy](anyproxy.md) | ✅ | C (4/6) | Buys scriptable interception with a web UI and mobile QR setup; costs Node 6-era dependencies that often break on modern Node and OS certificate rules, plus murky release provenance. |
| Charles / Fiddler | 未收录 | — | Other debugging proxies named across the pages. |

## What belongs here

Proxies whose primary job is **capturing, inspecting, rewriting, and mocking** HTTP(S)/WebSocket traffic for development and debugging. Not production API/AI gateways (see `api-gateway`), not scraping proxy pools (see `proxy-pool`).
