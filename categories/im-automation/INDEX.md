# im-automation

> Category node. Instant-messaging bots & automation (WeChat and other IM platforms).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)


## Sub-categories

| Category | Use when | Route |
| --- | --- | --- |
| **wechat** | WeChat-specific bots, account tooling, and the frameworks behind them. | [→](wechat/INDEX.md) |

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Douyin-Bot** | Use it only as a historical reference for ADB screen-coordinate phone automation — never deploy it, its 2018 coordinates and dead Tencent face API mean it no longer works. | D (3/6) | [→](douyin-bot.md) |
| **OpeniLink Hub** | Use it when several iLink-connected WeChat bots need a self-hosted control plane, persistence, tracing, and Apps; it is young and explicitly not affiliated with or endorsed by iLink's official team. | B (5/6) | [→](openilink-hub.md) |
| **OpeniLink Go SDK** | Use it when you need raw iLink transport inside an existing Go service and prefer the smallest trust boundary over a control plane; you then own persistence, auth, retrying and operations. | C (4/6) | [→](openilink-sdk-go.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Douyin-Bot](douyin-bot.md) | ✅ | D (3/6) | Use it only as a historical reference for ADB screen-coordinate phone automation — never deploy it, its 2018 coordinates and dead Tencent face API mean it no longer works. |
| [OpeniLink Hub](openilink-hub.md) | ✅ | B (5/6) | Young multi-bot control plane with persistence, tracing, and Apps, without official iLink affiliation or endorsement. |
| [OpeniLink SDK (Go)](openilink-sdk-go.md) | ✅ | C (4/6) | The raw iLink transport for Go services underneath the indexed Hub: smallest trust boundary, and you own persistence, auth, retrying and operations. |

## What belongs here

Bots and automation for **instant-messaging platforms** (WeChat and other IM). WeChat-specific projects live in `wechat/`. Not web/browser automation (see `web-automation`), not team-chat apps (see `team-chat`).

