---
name: Certbot
slug: certbot
repo: https://github.com/certbot/certbot
category: ops-infra
tags: [tls, ssl, acme, lets-encrypt, certificates, https, automation, nginx, apache]
language: Python
license: Apache-2.0
maturity: "v5.8.0, active, ~33.3k stars (as of 2026-09)"
last_verified: 2026-09-28
type: tool
upstream:
  pushed_at: 2026-09-22T03:53:35Z
  default_branch: main
  default_branch_sha: 485649333422392901e7ef891630f0129985df8e
  archived: false
health:
  schema: 1
  computed_at: 2026-10-10T02:36:55Z
  overall: A
  overall_score: 3.8
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 11
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 46.1
        qualifying_issues: 12
        band: relaxed_solo
        window_offset_days: 4
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: certbot
        dependent_repos_count: 470
        downloads_last_month: 451623
        graph_tier: C
        volume_tier: B
        cross_check_divergence: 1.0
        homebrew_installs_90d: 6070
        homebrew_tier: A
        release_downloads: 413800
        release_assets: 487
        release_tier: C
        signal_basis: homebrew+releases
        tier_source: homebrew+releases
    longevity:
      grade: A
      raw:
        repo_age_days: 4350
        last_commit_age_days: 2
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 23
        top1_share: 0.341
        top3_share: 0.821
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Certbot

EFF/Let's Encrypt 的 ACME 客户端，负责申请并自动续期免费、浏览器信任的 TLS 证书，配套插件能把证书直接接进 nginx/Apache。

![certbot — 健康度雷达](../../../assets/health/certbot.zh.svg)

## 何时使用

你是系统管理员，要给几台公网 Web 服务器上 HTTPS——几个 nginx vhost、一台 Apache，也许还有一个只需要把证书放到磁盘上的裸 TCP 服务。你不想买证书，不想让证书在某个假期凌晨 2 点过期，也不想每 90 天手改一遍 `ssl_certificate` 那几行。你装上 Certbot，跑 `certbot --nginx`（或 `--apache`），回答几个提示，它就用 ACME 跟 Let's Encrypt 对话，通过 HTTP-01 或 DNS-01 挑战证明你对域名的控制权，把证书/私钥写到 `/etc/letsencrypt/live/` 下，再改写你的服务器配置指向它们。常见的安装方式（snap、发行版包）还会预装一个 systemd timer 或 cron 项来定期跑 `certbot renew`——官方文档教你用 `systemctl list-timers` 确认装没装上、没装就自己配——而 `renew` 只在证书剩余寿命不足三分之一时才动手，所以一张 90 天的 Let's Encrypt 证书大约在过期前一个月被静默续掉。那个本来要手动操心的证书，变成了主机上一块装好就不用管的部件。

你专门选它，是因为想要那个*参考实现*的 ACME 客户端——EFF 维护的那个、每篇教程默认假设的那个——它对 Web 服务器有一流的集成，还带一大批 DNS 插件（Route 53、Cloudflare、Google 等）来处理需要 DNS-01 的通配符证书。如果你的主机本来就跑 Python，又看重官方、开箱即全的路径而非一个极简 shell 脚本，那 Certbot 就是默认选择。

## 怎么用起来

Certbot 把整套 ACME 流程（证书颁发机构协议，标准化为 RFC 8555）自动化，默认对接 Let's Encrypt：私钥*在你自己的机器上*生成，向 CA 下单，然后通过挑战证明域名控制权——HTTP-01（放一个 CA 能从 80 端口取回的 token 文件）、DNS-01（用 provider 插件发布 TXT 记录）或 TLS-ALPN-01——最后下载签好的证书。Web 服务器插件还多做了一件纯 ACME 客户端不做的事：`--nginx`/`--apache` 安装器会解析服务器自己的配置，把它指向 `/etc/letsencrypt/live/` 下的密钥和证书，reload 服务器，还能顺手配好 http→https 跳转。每次签发都会落一份按证书独立的*续期配置*，之后 `certbot renew` 无需提问就能原样重放——这就是定时器能无人值守跑的原因。仍然归你管的：保证 80 端口（或 DNS API 凭证）可达、续期前后的 *hook*（重载服务器、把证书分发到别的节点）要自己写自己测、以及别把 Let's Encrypt 的速率限制打爆。当前版本默认签发 ECDSA 密钥（RSA 仍可选）。

![Certbot — 主干用户故事](../../../assets/flow/certbot.zh.svg)

<!-- flow-steps:begin (generated from flows/certbot.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：在 Web 服务器上安装 Certbot — `sudo snap install --classic certbot`
2. **你**：对着你的 Web 服务器跑一次 — `sudo certbot --nginx`
3. **Certbot**：本地生成私钥，走 ACME 下单，用 HTTP-01 证明域名控制权 — 组件：`nginx 插件`
4. **Certbot**：保存证书与私钥，改写服务器配置以提供 HTTPS — `/etc/letsencrypt/live/`
5. **Certbot**：定时器周期执行 renew，按证书留存配置在临期时静默续期 — `certbot renew` — 组件：`续期定时器（systemd/cron）`

**价值**：免费、浏览器信任、会自己续期的 HTTPS——没有过期事故，也不用手改证书路径

</details>
<!-- flow-steps:end -->

## 何时不用

- **你想要最小体积。** Certbot 是个重量级 Python 客户端，自带 venv/依赖树。如果你只是要在一台资源受限的机器上拿张证书，单文件小客户端——[acme.sh](#横向对比)（纯 shell）或 [lego](#横向对比)（单个 Go 二进制）——轻得多，也不用拖一套 Python 运行时。
- **你的反向代理已经会做 ACME。** Caddy 开箱即自动签发并续期证书，Traefik 也内建 ACME；如果你前面已经用其中之一兜底，再单独跑一个 Certbot 就是冗余。[推断]
- **你需要内部/私有 CA。** Certbot 对公网 CA（默认 Let's Encrypt）说 ACME。要做内部 PKI / 私有 CA 签发，你应该用 step-ca/smallstep 或你自己 CA 的工具——Let's Encrypt 不会给私有或非公网 DNS 名字签发。
- **你会撞上 Let's Encrypt 速率限制。** 大量签发（很多子域名、频繁重签、CI 抖动）会撞到按域名/按账户的每周限额；据此规划证书（以及用 staging 环境测试）——这是 Let's Encrypt 的约束，不是 Certbot 的 bug。[未验证]
- **你不喜欢这种插件耦合。** `--nginx`/`--apache` 安装器会解析并改写你的服务器配置；遇到非常规或模板化的配置，它可能改错或失败，很多运维更愿意用 `certonly`（只取证书）加上自己的配置管理。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| acme.sh | 未收录 | 想要纯 shell、小体积、DNS API 覆盖很广的 ACME 客户端时，选 acme.sh。 | 纯 shell 的 ACME 客户端，零语言运行时，体积极小，DNS-API 列表庞大；不那么“官方”，没有改写 nginx/apache 配置的安装器——证书得你自己接进去。 |
| lego | 未收录 | 需要静态 Go 二进制，或可嵌入的 Go ACME 库并要求广泛 DNS 支持时，选 lego。 | 单个静态 Go 二进制，既是 ACME 客户端又是 Go 库，DNS provider 支持广；适合嵌入/自动化，但没有 Web 服务器配置安装器。 |
| Caddy（自动 HTTPS） | 未收录 | 可以同时采用一个自动处理 ACME 的 Web 服务器时，选 Caddy。 | 一个本身*就是* ACME 客户端的 Web 服务器——透明签发/续期，不需要单独工具；只有当你同时把 Caddy 当服务器用时它才替代 Certbot。 |
| dehydrated | 未收录 | 想要极简、钩子驱动的 Bash ACME 客户端，且能接受更多 DIY 接线时，选 dehydrated。 | 极简的 Bash ACME 客户端（前身 letsencrypt.sh）；钩子驱动、轻量，但更偏 DIY，生态比 Certbot 小。 |

## 技术栈

- **语言：** Python——以一个 CLI 加一组插件包的形式分发。
- **协议：** ACME（RFC 8555），默认对 Let's Encrypt；支持 HTTP-01、DNS-01 和 TLS-ALPN-01 挑战。默认密钥类型为 ECDSA，RSA 仍可选（README，2026-09）。
- **插件：** nginx（0.8.48+）和 Apache（2.4+）的 authenticator/installer 插件（依 README 支持列表），`webroot`/`standalone` authenticator，以及一族 `certbot-dns-*` 插件（Route 53、Cloudflare、Google、DigitalOcean……）用于 DNS-01。
- **磁盘布局：** 证书/私钥/账户状态放在 `/etc/letsencrypt` 下；续期配置按证书各存一份，所以 `certbot renew` 调用起来是无状态的。

## 依赖

- **运行时：** 一个 Python 解释器加上 Certbot 的依赖树（cryptography、requests、ACME 库等）——比单二进制替代品更重。最低 Python 版本跟随项目当前的支持策略，且随时间变化。[未验证]
- **一个 Web 服务器（用安装器插件时）：** 用 `--nginx`/`--apache` 时需要 nginx 或 Apache；否则不需要——`certonly` 只写证书文件。
- **网络 + 一个公网 CA：** 能出网访问 ACME directory（Let's Encrypt），以及一个你能通过 HTTP-01（80 端口可达）或 DNS-01（DNS API 凭证）证明控制权的域名。
- **安装路径：** 官方 `certbot.eff.org` 交互指南会按操作系统生成安装说明——发行版包（多数发行版）、官方 `snap`、`pip`，以及 Docker 镜像。

## 运维难度

**低**——对常见场景而言。装好、跑 `certbot --nginx`，多数安装方式就替你配好了续期 timer——用 `systemctl list-timers` 确认一次即可；日常维护基本为零——`renew` 自动且幂等。一旦离开顺路径难度就上来：DNS-01/通配符证书需要 provider API 凭证和对应的 `certbot-dns-*` 插件（snap 安装路径还要先 `sudo snap set certbot trust-plugin-with-root=ok`，再 `sudo snap install certbot-dns-cloudflare`，见官方指南）；HTTP-01 需要 80 端口能穿过防火墙/负载均衡到达；nginx/apache 安装器可能解析错非标准配置（很多团队用 `certonly` + 自己的模板化来规避）；续期*钩子*（reload 服务器、把证书分发到其它节点）要你自己写、自己测。在机群规模上，你会想用配置管理来一致地部署 Certbot 和它的续期钩子，而不是逐台手调。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 46.1 小时，基于 12 个 qualifying issues/PRs（评分器，2026-10-10）。
- **维护（2026-09）。** 最后 push 于 2026-09；v5.8.0 于 2026-09-01 发布，前作 v5.7.0 在 2026-07-21——大致每月到两月一个小版本的稳定节奏——处于**活跃**而非吃老本。未归档。[推断]
- **治理 / bus factor。** 归属一个 **Organization**，由 EFF 公开开发，现由 ISRG（Let's Encrypt 的非营利机构）托管——**非营利、团队/基金会背书的治理，bus-factor 低**。它是签发了网上大部分免费证书的那个 CA 的参考客户端，因此有制度性的理由保持维护。[推断]
- **背书与 Lindy。** 2014-11 创建（约 12 年）且**仍在活跃发布**⇒ **强 Lindy** 信号：一个久经实战、长寿的客户端，而非被炒作的新秀。非营利背书（EFF/ISRG）相比单一厂商的商业工具进一步降低了弃坑风险。[推断]
- **许可。** Apache-2.0（读 LICENSE 文件确认；GitHub 报 `NOASSERTION` 只是因为内置的 nginx parser 带 MIT）——宽松、对基金会友好的许可，**无 SSPL/AGPL 那类 relicense 风险**。[推断]
- **采用度。** 近乎普及：Certbot 是无数教程和发行版包里的默认 ACME 客户端，在 Let's Encrypt 生态里有广泛的真实部署。[未验证]

## 存疑（未验证）

- [未验证] 截至 2026-09-28 约 33.3k GitHub star、v5.8.0（2026-09-01 发布）——star 数和版本号对时间敏感，仅供参考。
- [推断] GitHub 的 license API 返回 `NOASSERTION`；按 LICENSE 文件项目实际许可是 Apache-2.0（`NOASSERTION` 是因为内置的 nginx parser 为 MIT）。已读文件确认，但因 API 徽章不一致而标记。
- [未验证] Let's Encrypt 的速率限制（按域名/按账户的每周签发量）是 CA 侧策略，随时间变化——批量签发前请查当前限额；这不是 Certbot 施加的限制。
- [未验证] 最低支持的 Python 版本跟随 Certbot 当前的支持策略，随时间移动，这里不断言具体数字。
- [推断] “Caddy/Traefik 使其冗余”和“nginx/apache 安装器可能改错配置”是基于这些工具工作方式的运维推断，而非对某个具体配置的实测结论。
