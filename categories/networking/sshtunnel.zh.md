---
name: sshtunnel
slug: sshtunnel
repo: https://github.com/pahaz/sshtunnel
category: networking
tags: [ssh, port-forwarding, tunnel, python, paramiko, networking]
language: Python
license: MIT
maturity: v0.4.0 (last release 2021), low activity, ~1.3k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2025-08-27T14:29:08Z
  default_branch: master
  default_branch_sha: dc0732884379a19a21bf7a49650d0708519ec54f
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:43:44Z
  overall: B
  overall_score: 2.5
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: D
      raw:
        archived: false
        last_commit_age_days: 391
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: sshtunnel
        dependent_repos_count: 1287
        downloads_last_month: 17633341
        graph_tier: B
        volume_tier: A
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: D
      raw:
        repo_age_days: 4486
        last_commit_age_days: 391
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
    governance: { reason: unattributable }
---

# sshtunnel

一个小巧的 Python 库（兼 CLI），封装 Paramiko，把 SSH 端口转发隧道做成上下文管理器——`with SSHTunnelForwarder(...) as t:` 打开一个本地端口，经由 SSH 堡垒机桥接到你直连不到的服务。

![sshtunnel — 健康度雷达](../../assets/health/sshtunnel.zh.svg)

## 何时使用

你在写一个 Python 脚本，要访问一个跑在私网里的 Postgres（或 Redis，或内部 HTTP API），它只能通过堡垒机走 SSH 才能到达。手动做意味着在 subprocess 里 `ssh -L 5432:db.internal:5432 bastion`，再去猜隧道什么时候起好。改用它来包：`with SSHTunnelForwarder(('bastion', 22), ssh_username=..., remote_bind_address=('db.internal', 5432)) as tunnel:`，然后把你的 DB 客户端指向 `127.0.0.1:tunnel.local_bind_port`。隧道在 `__enter__` 打开、在 `__exit__` 拆除，绑定的本地端口可编程拿到——不用解析 subprocess、不会漏 `ssh` 进程，全程在你的 Python 进程和异常处理里。要脚本化「经跳板机访问私网服务」而又不想自己在 Paramiko 上重写端口转发，这就是干净的做法。

它在临时自动化和数据脚本里最闪光：一次性迁移要打到堡垒机后面的 DB、notebook 从内部服务拉数、或一个需要带启停控制的常驻转发端口的小 daemon。

## 何时不用

- **生产级、长寿命、高吞吐的隧道。** 它是 Paramiko（纯 Python、线程）转发之上的便利封装——脚本够用，但要做持久的生产隧道，原生 `ssh -L`/`autossh` 或一套真正由 SSH config 管理的方案更稳更快。
- **你需要 OpenSSH config 的完整还原度。** 它不会像 OpenSSH 客户端那样照顾你完整的 `~/.ssh/config`（ProxyJump 链、match 块、每一个选项）；复杂的多跳设置用原生 `ssh` 更省心。
- **你已经在直接用 Paramiko。** 如果你的代码已在管理一个 Paramiko `Transport`，再加 `sshtunnel` 就是为 Paramiko 本可经 `Transport.open_channel('direct-tcpip', ...)` 做到的事多加一层——权衡这个依赖。
- **你想要活跃、当前的维护。** 最后一次发布是 **0.4.0（2021-01）**；仓库仍有偶尔提交（最后 push 2025-08），但节奏慢——锁版本并对照你的 Python/Paramiko 版本测试。[未验证]
- **反向隧道 / SOCKS 代理是主要诉求。** 它的甜区是经堡垒机的本地→远程转发；要做通用 SOCKS 或重度反向转发，请找专门的工具。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Paramiko](paramiko.zh.md) | ✅ | 需要完整 SSH/SFTP/传输控制，而不是 sshtunnel 的转发便利封装时，直接选 Paramiko。 | 底层是同一个引擎，但转发和生命周期的人体工学要你自己实现。 |
| 原生 `ssh -L` / `autossh` | 未收录 | 持久隧道需要 config 完整还原、速度和可选自动重连时，选原生 OpenSSH 或 autossh。 | 更适合生产，但它是要管理的进程，不是 Python 内对象。 |
| `subprocess` + `ssh` | 未收录 | 零 Python 依赖值得你自己管理进程就绪状态时，选 `subprocess` 加 `ssh`。 | 保留 OpenSSH 行为，但文本解析、子进程生命周期和失败处理都归你。 |
| AsyncSSH（转发 API） | 未收录 | 代码库已经 asyncio-native，且 SSH 转发应留在事件循环里时，选 AsyncSSH。 | API 不同，也比薄 Paramiko 封装更重，但更适合异步应用。 |

## 技术栈

- **语言：** 纯 Python。
- **核心依赖：** **Paramiko** 做实际的 SSH 传输和 channel 转发；sshtunnel 加上 `SSHTunnelForwarder` 对象、线程、生命周期和一个 CLI。
- **API 面：** 一个上下文管理器 / 启停对象，暴露绑定的本地地址/端口，外加一个 `sshtunnel` 命令行入口。
- **并发：** 线程式，沿用 Paramiko 的阻塞模型——一个（或多个）转发 channel 由后台线程管理。

## 依赖

- **运行时：** Python 3 和 **Paramiko**（它又会拉入 `cryptography`/OpenSSL）。[推断]
- **外部：** 一个你能认证的 SSH 服务端 / 堡垒机，以及从该堡垒机可达的目标服务——sshtunnel 在服务端不跑任何自己的东西。
- **安装：** `pip install sshtunnel`。

## 运维难度

**低（作为库）。** 没有要部署的东西——`pip install` 后用上下文管理器即可。运维上的在意点围绕可靠性和认证：隧道会因网络抖动断开（没有 `autossh` 那样的内置重连），所以长寿命使用需要你自己的 keepalive/重试；凭证/密钥要安全处理；又因为它建在 Paramiko 上，你继承了 Paramiko 的 host-key 策略和锁版本顾虑。对短脚本它几乎零运维；对任何常驻场景，请自己规划重连和监控。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 最后 tag 发布 **0.4.0（2021-01）**；仓库最后 push 2025-08——**低活跃 / 吃老本**，但未归档。成熟且小到「做完了」也说得过去，但别指望快速修 bug。[未验证]
- **治理 / bus factor。** 归个人所有（**pahaz**，约 271 次提交），有一位实质的合作贡献者（fernandezcuesta，约 142 次）——**薄 bus factor**；它是单作者的工具库。[推断]
- **年龄与 Lindy 判断。** **2014** 年创建，约 12 岁；封装很薄且稳定，所以年龄 + 一个小而稳的 API 是*中等* Lindy 信号——但它的健康其实系于底下 **Paramiko** 的持续维护。[推断]
- **采用度。** 约 1.3k star，在需要快速堡垒机隧道的数据/自动化脚本里有广泛使用；在「从 Python 连跳板机后面的 DB」类教程里被频繁引用。[未验证]
- **风险标记。** MIT，无 relicense 历史。主要风险：维护节奏慢，以及完全依赖 Paramiko（它的安全公告和版本漂移会传导到这里）。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 1.3k star / 约 202 fork / 约 81 open issue——对时间敏感，仅供参考。
- [未验证] 最后发布 0.4.0 标注 2021-01；是否有更新的修复只以未发布提交形式存在，未确认——锁版本前查仓库。
- [推断] 确切的传递依赖（Paramiko → cryptography 等）取决于已安装的 Paramiko 版本。
- [未验证] 复杂多跳 / ProxyJump 设置和完整 `~/.ssh/config` 还原度的行为未经核实——那种场景原生 `ssh` 更稳妥。
- [推断] 没有内置自动重连；持久隧道的可靠性取决于你自己的重试层（由它作为薄封装的范围推断）。
