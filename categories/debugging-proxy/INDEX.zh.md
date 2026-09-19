# debugging-proxy

> 分类节点。HTTP(S)/WebSocket 调试代理——抓取、检查、改写并 mock 流量。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **whistle** | 当 web/移动开发者要通过规则化 Web UI 抓取、检查、改写并 mock HTTP(S)/WebSocket 流量时用它——是开发调试代理，不是生产网关或爬虫代理池。 | B（6/6） | [→](whistle.zh.md) |
| **AnyProxy** | 当你想用纯 JS 规则脚本化地拦截并改写 HTTP/HTTPS 流量、需要一个 Node.js MITM 代理时用它——但 master 自 2020 年已冻结，新项目请优先选 whistle。 | C（4/6） | [→](anyproxy.zh.md) |
| **mitmproxy** | An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers. | A（6/6） | [→](mitmproxy.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [whistle](whistle.zh.md) | ✅ | B（6/6） | 当 web/移动开发者要通过规则化 Web UI 抓取、检查、改写并 mock HTTP(S)/WebSocket 流量时用它——是开发调试代理，不是生产网关或爬虫代理池。 |
| [AnyProxy](anyproxy.zh.md) | ✅ | C（4/6） | 当你想用纯 JS 规则脚本化地拦截并改写 HTTP/HTTPS 流量、需要一个 Node.js MITM 代理时用它——但 master 自 2020 年已冻结，新项目请优先选 whistle。 |
| Charles / Fiddler | 未收录 | — | 各页对比里点到的其他调试代理。 |

## 什么该放这里

主要职责是为开发与调试**抓取、检查、改写并 mock** HTTP(S)/WebSocket 流量的代理。不含生产 API/AI 网关（见 `api-gateway`），不含爬虫代理池（见 `proxy-pool`）。
