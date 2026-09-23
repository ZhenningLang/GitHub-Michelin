---
name: Paramiko
slug: paramiko
repo: https://github.com/paramiko/paramiko
category: networking
tags: [ssh, sshv2, sftp, python, networking, crypto, protocol]
language: Python
license: LGPL-2.1
maturity: stable, active, ~9.8k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-05-09T19:58:37Z
  default_branch: main
  default_branch_sha: d60d5c17d78f344b51ed651e796d2931133a9b22
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:43:34Z
  overall: B
  overall_score: 2.83
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 24
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: C
      raw:
        median_ttfr_hours: 208.1
        qualifying_issues: 11
        band: default
        window_offset_days: 3
        source: pr
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: paramiko
        dependent_repos_count: 30613
        downloads_last_month: 124717264
        graph_tier: A
        volume_tier: A
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 6442
        last_commit_age_days: 24
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.976
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: C
      raw:
        spdx_id: LGPL-2.1
        permissiveness: weak_file_copyleft
        relicense_36mo: false
        content_license: null
---

# Paramiko

最主流的纯 Python SSHv2 协议实现——客户端与服务端，带 SFTP——让 Python 代码无需 shell 调用 `ssh` 二进制就能打开 SSH 连接、跑远程命令、传文件。

![paramiko — 健康度雷达](../../assets/health/paramiko.zh.svg)

## 何时使用

你在写一个 Python 自动化工具——部署脚本、网络设备采集器、CI 步骤——它得通过 SSH 登录远程主机、跑命令、把文件拉回来。你不想 `subprocess` 系统的 `ssh` 客户端（脆弱的引号转义、host-key 交互提示、没有结构化错误处理），也不想依赖容器里装着某个 CLI。你 `pip install paramiko`，打开一个 `SSHClient`，用 key 或密码 `connect()`，于是你就有了可编程的 `exec_command()`——返回真正的 stdin/stdout/stderr 文件对象——外加一个 `open_sftp()` 通道做上传下载，全程进程内，抛出你能捕获并重试的 Python 异常。当你需要精细控制时——自定义 `Transport`、端口转发、agent 转发，甚至用 Python 起一个 SSH*服务端*——Paramiko 把上层工具所依赖的协议层暴露给你。

它也是你间接继承下来的底座：**Fabric**（远程任务执行）和 **Ansible** 的 SSH 连接插件都构建在 Paramiko 之上，所以理解它在你排查它们的连接行为时很有用。当你想要的是一个库而非一个框架时——原始的 SSH/SFTP 传输、归你代码所有——直接选 Paramiko。

## 何时不用

- **你只需要跑几个远程任务，而非实现 SSH。** 对于「在这些主机上跑这条命令」这类高层工作流，**Fabric**（它封装了 Paramiko）样板代码少得多。Paramiko 是底层传输；直接用它意味着连接、host key 和线程都得你自己管。
- **你需要最高吞吐 / 与原生 OpenSSH 对齐。** 作为纯 Python，Paramiko 在批量 SFTP 传输上比 C 写的 OpenSSH 客户端慢，也不一定能匹配 OpenSSH 的每一个配置项、cipher 或 `~/.ssh/config` 细节。大量文件搬运走真客户端的 `rsync`/`scp` 可能更快。
- **你需要某个很新的加密算法或 OpenSSH 特性首日可用。** Paramiko 历史上在一些较新 key 类型/算法上落后于 OpenSSH；请核实你需要的 KEX/cipher/host-key 算法在你锁定的版本里被支持。[未验证]
- **LGPL-2.1 对你的分发模式有问题。** Paramiko 是 **LGPL-2.1**，而非 Python 生态常见的 MIT/BSD。对多数应用（动态链接 / pip 导入）这没问题，但若你做静态打包或有严格许可政策，请审查。[推断]
- **你要 async 原生的 I/O。** Paramiko 面向线程/阻塞；要 asyncio 原生的 SSH，**AsyncSSH** 是为此打造的替代品。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| AsyncSSH | 未收录 | 代码库是 asyncio 原生，并希望 SSH 客户端/服务端 API 围绕 `await` 设计时，选 AsyncSSH。 | asyncio 原生的 SSHv2 客户端+服务端，现代算法支持广；更适合 async 代码库，但 API 不同（基于 await）且依赖它的生态更小。 |
| Fabric | 未收录 | 需要构建在 Paramiko 之上的高层远程任务编排时，选 Fabric。 | 构建*在* Paramiko 之上的高层远程执行框架；做任务编排很好，但它是上面那层，不是传输库。 |
| `subprocess` + 系统 `ssh` | 未收录 | 零 Python 依赖和完全 OpenSSH 对齐比稳健 Python API 更重要时，选系统 `ssh`。 | 零 Python 依赖、与 OpenSSH 完全对齐，但脆弱（文本解析、引号、host-key 提示），且要求 `ssh` 二进制存在。 |
| libssh2 / ssh2-python | 未收录 | 传输速度和 C 后端依赖比 Python 风格 API 更重要时，选 libssh2 绑定。 | C 库绑定——传输更快，但带一个编译依赖、Python 风格的 API 更薄。 |
| [`sshtunnel`](sshtunnel.zh.md) | ✅ | 只需要一个薄 Paramiko 封装来做端口转发隧道时，选 sshtunnel。 | 一个只做端口转发隧道的薄 Paramiko*封装*——范围更窄，建在同一引擎上。 |

## 技术栈

- **语言：** 纯 Python（自身无 C 扩展）。
- **加密：** 依赖 **`cryptography`** 包（并经它依赖 OpenSSL）来做 cipher、密钥交换和密钥处理——真正的原语是经由这个依赖走原生代码。
- **协议面：** SSHv2 传输、认证（密码/公钥/键盘交互/GSS-API）、channel、`exec`/`shell`、SFTP 子系统，以及一个 SSH*服务端*实现。
- **并发模型：** 线程/阻塞 socket；每个 `Transport` 跑一个后台线程。

## 依赖

- **运行时：** Python 3 加 **`cryptography`** 库（它会拉入一个编译好的 OpenSSL 后端）；可选地用 PyNaCl/bcrypt 处理某些 key 格式，用 `gssapi`/`pyasn1` 做 GSS-API/Kerberos 认证。[推断]
- **外部服务：** 自身没有——你把它指向你已经在跑的任何 SSH 服务端。
- **构建/安装：** `pip install paramiko`；唯一非纯 Python 的部分是 `cryptography` wheel 的原生后端。

## 运维难度

**低（作为库）。** 没有要部署的东西——它就是在你应用里 `pip install paramiko`。运维上的摩擦在*使用*层面：host-key 校验策略（生产里别无脑 `AutoAddPolicy`）、线程/连接的生命周期与清理、长连接上的超时与 keepalive，以及锁版本——因为 `cryptography` 依赖和受支持算法会随时间变。长跑的多主机自动化需要你自己做连接池和错误处理，因为 Paramiko 给你的是传输，不是编排。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 4.0 小时，基于 5 个 qualifying issues/PRs。
- **维护（2026-06）。** 仓库最后 push 于 2026-05——**活跃**，未归档。发布主要走 **PyPI**（这里 GitHub Releases 列表为空），所以节奏要看 PyPI/changelog 而非 git tag。[未验证]
- **治理 / bus factor。** 归 **`paramiko` 组织**，但历史上压倒性地由一位维护者驱动（**bitprophet** / Jeff Forcier，约 2,800 次提交，第二名仅数百次）——尽管有组织外壳，这仍是真实的 **bus-factor** 考量。[推断]
- **年龄与 Lindy 判断。** **2009** 年创建，约 17 岁且**仍活跃**⇒ **强 Lindy** 信号：它是事实上的 Python SSH 库，被 Fabric、Ansible 和一大片 Python 基础设施工具依赖。[推断]
- **采用度。** 约 9.8k star、2k+ fork，加上经由下游工具（Ansible、Fabric、pysftp 之类封装）的巨量传递使用——采用度毋庸置疑。约 1.2k 个 open issue 反映的是庞大的面和悠久历史，而非弃坑。[未验证]
- **风险标记。** **LGPL-2.1**（在该生态里少见——做静态链接/严格政策分发时需审查）和单一维护者集中度是要权衡的两点；未发现 relicense 历史。作为 SSH/加密库它也是安全敏感依赖——跟踪它的安全公告并保持 `cryptography` 更新。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 9.8k star / 约 2,059 fork / 约 1,180 open issue——数字对时间敏感，仅供参考。
- [未验证] 发布走 PyPI；空的 GitHub Releases 列表**不**代表不活跃——请在 PyPI/changelog 上核实当前版本与节奏。
- [推断] 确切的传递依赖集（PyNaCl/bcrypt/gssapi 等 extra）取决于版本和所选安装 extra，这里未锁定。
- [未验证] 相对当前 OpenSSH 的具体较新 KEX/cipher/host-key 算法支持随版本而定——请对照你锁定的版本确认。
- [推断] LGPL-2.1 相对你分发模式的义务是法律判断，这里不断言它是阻断项。
