# debugging-proxy

> 分类节点。HTTP(S)/WebSocket 调试代理——抓取、检查、改写并 mock 流量。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **whistle** | 当 web/移动开发者要通过规则化 Web UI 抓取、检查、改写并 mock HTTP(S)/WebSocket 流量时用它——是开发调试代理，不是生产网关或爬虫代理池。 | B（6/6） | [→](whistle.zh.md) |
| **AnyProxy** | 当你调试 app 流量、想要一个用纯 JavaScript 规则文件改写请求和响应的 Node.js 中间人代理时用它——但 master 自 2020 年起冻结，新项目请优先选 whistle。 | C（4/6） | [→](anyproxy.zh.md) |
| **mitmproxy** | 当你要看清并改写一个你控制不了的客户端发出的 HTTPS 请求、还想用 Python 写脚本处理时用它——但做了证书固定的 App 会拒绝它，得先去固定。 | A（6/6） | [→](mitmproxy.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [whistle](whistle.zh.md) | ✅ | B（6/6） | 当 web/移动开发者要通过规则化 Web UI 抓取、检查、改写并 mock HTTP(S)/WebSocket 流量时用它——是开发调试代理，不是生产网关或爬虫代理池。 |
| [AnyProxy](anyproxy.zh.md) | ✅ | C（4/6） | 换来可脚本化的拦截、web UI 和手机扫码接入；代价是 Node 6 时代的依赖在新版 Node 和更严的系统证书规则下常出问题，发布来源也含糊。 |
| Charles / Fiddler | 未收录 | — | 各页对比里点到的其他调试代理。 |

## 什么该放这里

主要职责是为开发与调试**抓取、检查、改写并 mock** HTTP(S)/WebSocket 流量的代理。不含生产 API/AI 网关（见 `api-gateway`），不含爬虫代理池（见 `proxy-pool`）。
