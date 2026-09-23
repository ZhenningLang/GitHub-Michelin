---
name: wondershaper
slug: wondershaper
repo: https://github.com/magnific0/wondershaper
category: networking
tags: [traffic-shaping, bandwidth, qos, tc, htb, linux, shell]
language: Shell
license: GPL-2.0
maturity: stable, low activity (last push 2024-07), ~1.9k stars (as of 2026-06)
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2024-07-25T02:46:32Z
  default_branch: master
  default_branch_sha: 98792b55c2ebf4ab4cafffb0780e0c4185fdc03d
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:43:58Z
  overall: E
  overall_score: 0.25
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1803
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: E
      raw:
        repo_age_days: 5124
        last_commit_age_days: 1803
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: D
      raw:
        spdx_id: GPL-2.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
    governance: { reason: unattributable }
---

# wondershaper

一个单文件 Bash 脚本，封装 Linux `tc`（流量控制），一条命令就给某个网卡的上/下行带宽封顶——`wondershaper -a eth0 -d 8192 -u 2048`，而不是一大堆 HTB 排队规则咒语。

![wondershaper — 健康度雷达](../../assets/health/wondershaper.zh.svg)

## 何时使用

你在一台 Linux 机器上——挂种子的家庭服务器、CI runner、共享开发机、嵌入式网关——某个进程把链路打满了，饿死了别的一切（SSH 变卡、视频通话卡顿）。你不想为了说一句「别让这块网卡超过 8 Mbit 下 / 2 Mbit 上」就去学完整的 `tc` qdisc/class/filter DSL。你装上 wondershaper（就一个脚本），跑 `sudo wondershaper -a eth0 -d 8192 -u 2048`，它就替你建好 HTB 流量整形规则；`wondershaper -c -a eth0` 再把它们清掉。要持久封顶，你放进它提供的 systemd unit 和一个小配置文件，重启后限速会自动重新生效。从「这条链路需要个上限」到一块整形好的网卡，这是不手写 `tc` 的最快路径。

它适合*单台主机*网卡上的临时和轻量持久 QoS：给备份任务限速、别让某个下载器吃光整条管道，或给一台低功耗路由器一个简单的上下行上限。

## 何时不用

- **你需要真正的多类 QoS / 按流优先级。** wondershaper 设的是一个简单的整体上/下行上限（带一些优先级启发式）；要做细粒度的按应用/按 IP 流量分类，请直接写 `tc`/`nftables` 规则，或用路由器系统（OpenWrt 的 SQM/`cake`）。
- **你想要现代的抗 bufferbloat 整形。** 这脚本的血统是基于 HTB 的；要做负载下低延迟，**`cake`** / `fq_codel`（常经 SQM）才是当前最佳实践——在依赖它做 bufferbloat 控制前，先核实这个版本用的是哪种 qdisc。[未验证]
- **你不在带 `tc` 的 Linux 上。** 它是围绕 `iproute2` 的 `tc` 的 Bash 封装；没有 Windows/macOS，且需要 `iproute2` 存在。容器/网络命名空间另有注意事项。
- **你需要跨多台主机集中整形。** 它是按主机的 CLI，不是机群/SDN 控制器——没有中央策略，机器间不协调。
- **你要求上游积极支持。** 仓库最后 push 在 **2024-07**，而且是个又老又薄的脚本；它能用，但当作稳定但吃老本，并对照你的内核/`iproute2` 版本测试。[未验证]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| 裸 `tc`（iproute2） | 未收录 | 完整 qdisc/class/filter 控制值得你直接面对陡峭 traffic-control DSL 时，选裸 `tc`。 | 最灵活；wondershaper 只是这个引擎上的友好封装。 |
| `cake` / SQM（OpenWrt） | 未收录 | 主要问题是负载下 bufferbloat 延迟，且整形器可以放在路由器上时，选 cake 或 SQM。 | 更适合路由器／OpenWrt 设置，不是按主机的快脚本。 |
| `tcconfig`（Python） | 未收录 | 按 IP、端口、丢包或延迟等更丰富的脚本化规则比一个 Bash 文件更重要时，选 `tcconfig`。 | 它在 `tc` 之上功能更丰富，但会引入 Python 依赖。 |
| `trickle` | 未收录 | 只需要限制一个用户态进程，并且想避开 root 级 `tc` 时，选 `trickle`。 | 这是 LD_PRELOAD 的按进程整形，不是网卡级上限。 |
| 手写 Linux `tc` + `fq_codel` | 未收录 | 当前 qdisc 和正确性比封装便利更重要时，选手写 `tc` 加 `fq_codel`。 | 同一引擎、抽象更少，但要写更多配置。 |

## 技术栈

- **语言：** Bash（一个 shell 脚本）——无需编译。
- **引擎：** 来自 **`iproute2`** 的 Linux **`tc`**，施加 **HTB**（分层令牌桶）整形（从最初的 CBQ 升级而来；后续版本改进了 ingress 处理）。
- **持久化：** 一个可选的 **systemd** 服务 unit + 配置文件，在开机时重新施加限速。

## 依赖

- **运行时：** 带流量控制支持的 Linux 内核，并装好 **`iproute2`**（`tc`、`ip`）；施加规则需 **root/sudo**。持久服务可选 **systemd**。
- **外部服务：** 没有——它纯粹是本地内核排队配置。
- **安装：** clone 仓库 / `make install`，或在有的发行版上用包；它就是一个脚本 + 可选的 unit 文件。[推断]

## 运维难度

**低。** 一个脚本，一条命令施加，一条清除；systemd unit 让持久封顶变成拷配置加 enable 的活。真正要在意的是概念而非运维：选对网卡、把速率单位搞对（速率以 **Kbps/千比特** 计，容易和千字节混）、记住它需要 root 且规则是内核状态，不持久化的话重启即失。验证封顶真的生效（且没加延迟）意味着前后跑一次 `iperf`/ping。没有要照看的 daemon——它设好内核 qdisc 就退出了。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 仓库最后 push **2024-07**；这里没有 GitHub tag 发布。实质上**稳定 / 低活跃**——一个少有改动的小而成熟的脚本，但并非积极开发。未归档。[未验证]
- **治理 / bus factor。** owner 类型 **User**（magnific0，约 20 次提交），有几位次要贡献者——一个**单一维护者**的小工具；bus factor 薄，但面也极小。[推断]
- **年龄与 Lindy 判断。** **2012** 年创建（且本身是更古老的 Wondershaper 血统——源自 Linux Advanced Routing HOWTO——的延续）——约 14 岁；老**但安静**，所以 Lindy *中等*：长寿且仍能用，但 HTB 时代的设计相比现代 `cake`/`fq_codel` 已显陈旧。[推断]
- **采用度。** 约 1.9k star，作为 Linux how-to 里首选的「简单带宽限制」脚本有悠久历史；被广泛抄用。[未验证]
- **风险标记。** **GPL-2.0**（copyleft——使用没问题，重分发修改版时相关）。技术风险是相对现代抗 bufferbloat 整形的陈旧，而非许可或一个小脚本的弃坑。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 1.9k star / 约 277 fork——对时间敏感，仅供参考。
- [未验证] 未打 GitHub release；版本/changelog 在脚本/README 里——核实你所装版本的版本号和 qdisc 行为。
- [推断] 当前版本实际施加的 qdisc（HTB 还是更新的）及其 bufferbloat 行为这里未经核实——在你的内核上测。
- [推断] 安装路径（make/包/手动）取决于你的发行版；仓库本质上就是一个脚本加一个可选 systemd unit。
- [未验证] 在容器 / 网络命名空间内以及非 systemd init 上的行为未经核实。
