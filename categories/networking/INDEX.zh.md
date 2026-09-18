# networking

> 分类节点。网络库——SSH、DNS、隧道、RPC 与流量整形。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Paramiko** | 当 Python 代码需要以编程方式建立 SSH／SFTP 连接并执行远程命令时用它——但它是纯 Python（比 OpenSSH 慢）、仅支持线程模型，且采用 LGPL-2.1 许可。 | B（6/6） | [→](paramiko.zh.md) |
| **sshtunnel** | 当 Python 脚本需要以上下文管理器方式打通到堡垒机后服务的 SSH 端口转发时用它——但它无自动重连，且活跃度低（0.4.0，2021 年）。 | B（5/6） | [→](sshtunnel.zh.md) |
| **dnspython** | 当 Python 需要查询任意记录类型、自定义解析器、区域传输、DNSSEC 或 DoH／DoT 时用它——但它绕过 /etc/hosts 与系统解析器，要求 Python 3.10+，且是库而非命令行工具。 | B（5/6） | [→](dnspython.zh.md) |
| **wondershaper** | 当某块 Linux 网卡需要快速设置上／下行带宽上限、又不想手写 tc 规则时用它——但它基于老式 HTB（不像 cake／fq_codel 那样应对 bufferbloat），仅限 Linux，自 2024 年 7 月起停滞。 | D（4/6） | [→](wondershaper.zh.md) |
| **ThriftPy** | 仅当你要在迁移前读懂仍在 import thriftpy 的遗留服务时用它——该仓库已归档且废弃，所有新的 Thrift 开发都应转向仍在维护的 thriftpy2。 | B（5/6） | [→](thriftpy.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Paramiko](paramiko.zh.md) | ✅ | B（6/6） | 当 Python 代码需要以编程方式建立 SSH／SFTP 连接并执行远程命令时用它——但它是纯 Python（比 OpenSSH 慢）、仅支持线程模型，且采用 LGPL-2.1 许可。 |
| [sshtunnel](sshtunnel.zh.md) | ✅ | B（5/6） | 当 Python 脚本需要以上下文管理器方式打通到堡垒机后服务的 SSH 端口转发时用它——但它无自动重连，且活跃度低（0.4.0，2021 年）。 |
| [dnspython](dnspython.zh.md) | ✅ | B（5/6） | 当 Python 需要查询任意记录类型、自定义解析器、区域传输、DNSSEC 或 DoH／DoT 时用它——但它绕过 /etc/hosts 与系统解析器，要求 Python 3.10+，且是库而非命令行工具。 |
| [wondershaper](wondershaper.zh.md) | ✅ | D（4/6） | 当某块 Linux 网卡需要快速设置上／下行带宽上限、又不想手写 tc 规则时用它——但它基于老式 HTB（不像 cake／fq_codel 那样应对 bufferbloat），仅限 Linux，自 2024 年 7 月起停滞。 |
| [ThriftPy](thriftpy.zh.md) | ✅ | B（5/6） | 仅当你要在迁移前读懂仍在 import thriftpy 的遗留服务时用它——该仓库已归档且废弃，所有新的 Thrift 开发都应转向仍在维护的 thriftpy2。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

面向**网络协议与链路**的库/工具——SSH、DNS、隧道、RPC、带宽整形。
