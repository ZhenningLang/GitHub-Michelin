# networking

> 分类节点。网络库——SSH、DNS、隧道、RPC 与流量整形。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Paramiko** | 当 Python 代码需要以编程方式建立 SSH／SFTP 连接并执行远程命令时用它——但它是纯 Python（比 OpenSSH 慢）、仅支持线程模型，且采用 LGPL-2.1 许可。 | B（6/6） | [→](paramiko.zh.md) |
| **sshtunnel** | 只在已有 Python 脚本早就依赖它的 `with` 块 SSH 端口转发、经堡垒机连私网数据库时继续用它——新装的版本在 Paramiko 4 及以上直接报错，而且 2021 年后再没发过版。 | B（4/6） | [→](sshtunnel.zh.md) |
| **dnspython** | 当 Python 需要查询任意记录类型、自定义解析器、区域传输、DNSSEC 或 DoH／DoT 时用它——但它绕过 /etc/hosts 与系统解析器，要求 Python 3.10+，且是库而非命令行工具。 | A（5/6） | [→](dnspython.zh.md) |
| **wondershaper** | 当某块 Linux 网卡需要一条命令设好整体上／下行带宽上限、又不想学 tc 语法时用它——但它生成的是 HTB 加 sfq 规则，而非能应对 bufferbloat 的 cake 或 fq_codel，没有按流 QoS，且自 2021 年起已停更。 | E（4/6） | [→](wondershaper.zh.md) |
| **ThriftPy** | 仅当你要在迁移前读懂仍在 import thriftpy 的遗留服务时用它——该仓库已归档且废弃，所有新的 Thrift 开发都应转向仍在维护的 thriftpy2。 | B（5/6） | [→](thriftpy.zh.md) |
| **amneziawg-installer** | 当你所在网络的 DPI 封锁了裸 WireGuard、想在一台干净廉价 VPS 上一条命令装好内核态 AmneziaWG 服务端时用它——但它仅支持 Ubuntu／Debian、要求支持 AWG 2.0 的客户端，且会把整台机器改造成单一用途的加固 VPN 服务器。 | B（6/6） | [→](amneziawg-installer.zh.md) |
| **dae** | 当 Linux 路由器或主机要给整个局域网按规则分流、又希望直连流量由内核经 eBPF 直接转发时用它——但它要求内核 5.17 以上，没有图形界面和 SOCKS／HTTP 入站，且是 AGPL-3.0。 | B（6/6） | [→](dae.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Paramiko](paramiko.zh.md) | ✅ | B（6/6） | 当 Python 代码需要以编程方式建立 SSH／SFTP 连接并执行远程命令时用它——但它是纯 Python（比 OpenSSH 慢）、仅支持线程模型，且采用 LGPL-2.1 许可。 |
| [sshtunnel](sshtunnel.zh.md) | ✅ | B（4/6） | 隧道随代码块自动开关；代价是得把 paramiko 锁在 4 以下、放弃它的安全更新。新代码直接在 Paramiko 或 AsyncSSH 上写转发。 |
| [dnspython](dnspython.zh.md) | ✅ | A（5/6） | 当 Python 需要查询任意记录类型、自定义解析器、区域传输、DNSSEC 或 DoH／DoT 时用它——但它绕过 /etc/hosts 与系统解析器，要求 Python 3.10+，且是库而非命令行工具。 |
| [wondershaper](wondershaper.zh.md) | ✅ | E（4/6） | 换来一个脚本、一行命令的限速；代价是负载下的延迟表现和细粒度控制——手写 tc 或 OpenWrt SQM 两样都做得更好。 |
| [ThriftPy](thriftpy.zh.md) | ✅ | B（5/6） | 仅当你要在迁移前读懂仍在 import thriftpy 的遗留服务时用它——该仓库已归档且废弃，所有新的 Thrift 开发都应转向仍在维护的 thriftpy2。 |
| [amneziawg-installer](amneziawg-installer.zh.md) | ✅ | B（6/6） | 当你所在网络的 DPI 封锁了裸 WireGuard、想在一台干净廉价 VPS 上一条命令装好内核态 AmneziaWG 服务端时用它——但它仅支持 Ubuntu／Debian、要求支持 AWG 2.0 的客户端，且会把整台机器改造成单一用途的加固 VPN 服务器。 |
| [dae](dae.zh.md) | ✅ | B（6/6） | 当 Linux 路由器或主机要给整个局域网按规则分流、又希望直连流量由内核经 eBPF 直接转发时用它——但它要求内核 5.17 以上，没有图形界面和 SOCKS／HTTP 入站，且是 AGPL-3.0。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

面向**网络协议与链路**的库/工具——SSH、DNS、隧道、RPC、带宽整形、透明代理与策略路由。
