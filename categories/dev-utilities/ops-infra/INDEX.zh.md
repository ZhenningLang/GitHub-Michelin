# ops-infra

> 分类节点。面向服务器、指标、TLS、镜像、代理、远程访问与密码管理的可自托管基础设施和运维工具。
> ← 返回 [dev-utilities](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Cockpit** | 当你需要为少数几台 Linux 服务器用浏览器做 systemd 原生的图形化管理时用它。 | D（5/6） | [→](cockpit.zh.md) |
| **Telegraf** | 当你需要一个插件驱动的 agent 把异构指标/日志统一采集并路由到多种后端时用它。 | A（5/6） | [→](telegraf.zh.md) |
| **Certbot** | 当系统管理员要自动签发并续期免费 Let's Encrypt TLS 证书时用它——不过反向代理自带的自动 TLS 常让它显得多余。 | A（4/6） | [→](certbot.zh.md) |
| **SlimToolkit** | 当你想在不重写 Dockerfile 的情况下自动瘦身并加固臃肿的容器镜像时用它——注意它可能删掉运行时动态加载的文件。 | B（4/6） | [→](slim.zh.md) |
| **Clash Verge Rev** | 当你想要一款现代化的跨平台 GUI 代理客户端，支持基于规则的路由、内置 mihomo 内核和 TUN 模式时用它——但仅限桌面端且为 GPL-3.0 许可。 | B（5/6） | [→](clash-verge-rev.zh.md) |
| **RustDesk** | 当你需要一款开源、自托管的跨平台远程桌面来访问自己的机器时用它——但需要自己管理中继服务器或接受 P2P 局限。 | B（5/6） | [→](rustdesk.zh.md) |
| **Vaultwarden** | 当你想要一款自托管的、Rust 编写的 Bitwarden 兼容密码管理器时用它——但它是非官方实现，AGPL-3.0 许可，且核心维护者为单人。 | B（6/6） | [→](vaultwarden.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Cockpit](cockpit.zh.md) | ✅ | D（5/6） | 当你需要为少数几台 Linux 服务器用浏览器做 systemd 原生的图形化管理时用它。 |
| [Telegraf](telegraf.zh.md) | ✅ | A（5/6） | 当你需要一个插件驱动的 agent 把异构指标/日志统一采集并路由到多种后端时用它。 |
| [Certbot](certbot.zh.md) | ✅ | A（4/6） | 当系统管理员要自动签发并续期免费 Let's Encrypt TLS 证书时用它——不过反向代理自带的自动 TLS 常让它显得多余。 |
| [SlimToolkit](slim.zh.md) | ✅ | B（4/6） | 当你想在不重写 Dockerfile 的情况下自动瘦身并加固臃肿的容器镜像时用它——注意它可能删掉运行时动态加载的文件。 |
| [Clash Verge Rev](clash-verge-rev.zh.md) | ✅ | B（5/6） | 当你想要一款现代化的跨平台 GUI 代理客户端，支持基于规则的路由、内置 mihomo 内核和 TUN 模式时用它——但仅限桌面端且为 GPL-3.0 许可。 |
| [RustDesk](rustdesk.zh.md) | ✅ | B（5/6） | 当你需要一款开源、自托管的跨平台远程桌面来访问自己的机器时用它——但需要自己管理中继服务器或接受 P2P 局限。 |
| [Vaultwarden](vaultwarden.zh.md) | ✅ | B（6/6） | 当你想要一款自托管的、Rust 编写的 Bitwarden 兼容密码管理器时用它——但它是非官方实现，AGPL-3.0 许可，且核心维护者为单人。 |

## 什么该放这里

面向服务器、指标、TLS、镜像、代理、远程访问与密码管理的可自托管基础设施和运维工具。
