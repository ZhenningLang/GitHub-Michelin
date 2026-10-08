# ops-infra

> 分类节点。面向服务器、指标、TLS、镜像、代理、远程访问与密码管理的可自托管基础设施和运维工具。
> ← 返回 [dev-utilities](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Cockpit** | 当你需要为少数几台 Linux 服务器用浏览器做 systemd 原生的图形化管理时用它。 | B（5/6） | [→](cockpit.zh.md) |
| **Telegraf** | 当你需要一个插件驱动的 agent 把异构指标/日志统一采集并路由到多种后端时用它。 | A（6/6） | [→](telegraf.zh.md) |
| **Certbot** | 当系统管理员要自动签发并续期免费 Let's Encrypt TLS 证书时用它——不过反向代理自带的自动 TLS 常让它显得多余。 | A（5/6） | [→](certbot.zh.md) |
| **SlimToolkit** | 当你想在不重写 Dockerfile 的情况下自动瘦身并加固臃肿的容器镜像时用它——注意它可能删掉运行时动态加载的文件。 | B（6/6） | [→](slim.zh.md) |
| **Clash Verge Rev** | 当你在桌面电脑上有一份 Clash 格式订阅，想用 TUN 模式让整台机器（包括终端工具）按规则分流时用它——但它只有桌面版，TUN 还需要装特权服务或提权运行。 | B（6/6） | [→](clash-verge-rev.zh.md) |
| **RustDesk** | 当你要照看几台不在身边的机器，想要 TeamViewer 式“输 ID 就连”的跨 NAT 体验、撮合和中继服务器又放在自己手里时用它——但开源服务端没有管理后台、SSO 和审计日志，这些在付费的 Server Pro 里。 | A（6/6） | [→](rustdesk.zh.md) |
| **Vaultwarden** | 当你想让家人或小团队继续用 Bitwarden 官方应用、但把密码库放在自己的一台小服务器上时用它——但客户端一更新你就得及时升级服务端，而且没有厂商支持、SAML/SCIM 或内置故障切换。 | B（6/6） | [→](vaultwarden.zh.md) |
| **Descheduler** | 当 Kubernetes 集群已经失衡、你想要一个 CronJob 定期驱逐违反策略的 Pod、让调度器重新安置它们时用它——它不是算出来的 placement 计划。 | A（6/6） | [→](descheduler.zh.md) |
| **JumpServer** | 当你需要一台自建堡垒机（PAM）替人保管目标机凭据、录下每个 SSH、RDP、数据库和 Kubernetes 会话时用它——但社区版上限 5000 台资产，高可用、SSO、改密都在企业版，且每年都有严重级漏洞公告。 | B（6/6） | [→](jumpserver.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Cockpit](cockpit.zh.md) | ✅ | B（5/6） | 当你需要为少数几台 Linux 服务器用浏览器做 systemd 原生的图形化管理时用它。 |
| [Telegraf](telegraf.zh.md) | ✅ | A（6/6） | 当你需要一个插件驱动的 agent 把异构指标/日志统一采集并路由到多种后端时用它。 |
| [Certbot](certbot.zh.md) | ✅ | A（5/6） | 当系统管理员要自动签发并续期免费 Let's Encrypt TLS 证书时用它——不过反向代理自带的自动 TLS 常让它显得多余。 |
| [SlimToolkit](slim.zh.md) | ✅ | B（6/6） | 当你想在不重写 Dockerfile 的情况下自动瘦身并加固臃肿的容器镜像时用它——注意它可能删掉运行时动态加载的文件。 |
| [Clash Verge Rev](clash-verge-rev.zh.md) | ✅ | B（6/6） | 换来用户最多、配置可分层的 mihomo 桌面客户端，代价是所有流量都经用户态进程中转，也不支持手机和无界面主机。 |
| [RustDesk](rustdesk.zh.md) | ✅ | A（6/6） | 换来自托管撮合、NAT 穿透和端到端加密，代价是自己运维 hbbs 和 hbbr，并接受管理功能归付费版的开源核心模式。 |
| [Vaultwarden](vaultwarden.zh.md) | ✅ | B（6/6） | 换来一个 Rust 加 SQLite 的小服务端、功能不设许可门槛，代价是它是非官方重写，没有审计，也不保证新版客户端首日兼容。 |
| [Descheduler](descheduler.zh.md) | ✅ | A（6/6） | 定期驱逐违反 `DeschedulerPolicy` 的 Kubernetes Pod，让 kube-scheduler 重新安置——集群内漂移纠正，不是算出来的 placement 计划。 |
| [JumpServer](jumpserver.zh.md) | ✅ | B（6/6） | 当你需要一台自建堡垒机（PAM）替人保管目标机凭据、录下每个 SSH、RDP、数据库和 Kubernetes 会话时用它——但社区版上限 5000 台资产，高可用、SSO、改密都在企业版，且每年都有严重级漏洞公告。 |

## 什么该放这里

面向服务器、指标、TLS、镜像、代理、远程访问、密码管理，以及 Kubernetes descheduler 这类集群内维护控制器的可自托管基础设施和运维工具。
