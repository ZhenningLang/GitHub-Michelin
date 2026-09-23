---
name: whistle
slug: whistle
repo: https://github.com/avwo/whistle
category: debugging-proxy
tags: [http-proxy, https, debugging, mock, web-ui, traffic-inspection, mitm, websocket]
language: JavaScript
license: MIT
maturity: v2.10.x, active, ~15.6k stars (as of 2026-06)
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2026-06-21T15:35:58Z
  default_branch: master
  default_branch_sha: 6da6e6c174c4d308199b9512c1ce1a7a671893ba
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:06:37Z
  overall: B
  overall_score: 3.0
  scored_axes: 6
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
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 18.4
        qualifying_issues: 15
        band: relaxed_solo
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: npmjs.org
        canonical_package: whistle
        dependent_repos_count: 24
        downloads_last_month: 17165
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4211
        last_commit_age_days: 2
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 6
        top1_share: 0.979
        top3_share: 0.992
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# whistle

跨平台的 HTTP/HTTPS/HTTP2/WebSocket 调试代理：把流量指向它，在 web UI 里写规则行，就能即时抓包、检视、改写、重定向、Mock 请求——类似 Fiddler/Charles，但基于浏览器、由配置驱动。

![whistle — 健康度雷达](../../assets/health/whistle.zh.svg)

## 何时使用

你是一名 Web 或移动端开发者，盯着一个只在对接*真实*后端时才出现的 bug——某个接口返回了让你的 App 崩掉的字段，CDN 发了一份过期的打包文件，或者某条流程只在同事的 staging 主机上挂掉。你不想等后端发版才能验证修复，也不想把 Mock 数据硬编码进 App。你装上 whistle（`npm i -g whistle`），启动它，把浏览器或手机的代理指过去，安装一次它的根证书让 HTTPS 可解密，于是每个请求都流经一个 web UI，你能读到完整的请求/响应对。你写几行规则——`www.example.com/api/user resBody://{mock.json}` Mock 一个响应，`example.com 127.0.0.1:8080` 把某个 host 重定向到本地，`example.com/app.js file:///path/app.js` 把一个脚本换成本地文件——改动在下一个请求就生效，无需重新发布。

它的强项在于检视*与*改写一气呵成：用精确的坏 payload 复现一个只在生产出现的 bug、把设备的流量经笔记本上的 whistle 路由来调试移动 App，或在后端还没就绪时通过 Mock 它的端点来做前端联调。规则语法存在一个可进版本库、可共享的文件里，整个团队都能复现同一套拦截配置。

## 何时不用

- **你需要的是生产网关 / 反向代理。** whistle 是开发期的调试代理，不是边缘或 API 网关——没有集群、限流方案、鉴权插件或生产 SLA。那种场景用 [Kong](../api-gateway/kong.zh.md)（或 nginx/Envoy）。
- **你要的是爬虫 IP 轮换池。** 它介入*你自己*的流量来检视/改写，并不采集或轮换匿名上游代理。爬虫 IP 池请看 [proxy_pool](../proxy-pool/proxy-pool.zh.md)。
- **你的环境绝对不允许 HTTPS 拦截。** 解密 HTTPS 需要在客户端安装并信任 whistle 的根 CA——这是一个真实的攻击面与策略风险（一张被信任的 MITM 证书）。在受管控 / 企业 / 生产设备上这通常被禁止，且 CA 私钥一旦泄露很危险。
- **你需要厂商背书、多人维护、带 SLA 的工具。** 它本质上是一个单维护者的个人仓库（owner 是 GitHub User 而非组织）——对任何你输不起停摆的东西来说，这是 bus-factor 风险。
- **你读中文文档不顺手、希望零摩擦。** 文档和大量社区讨论以中文为主；英文覆盖存在但更薄。[未验证]
- **你更想要打磨过的原生 GUI。** 想要打包好的桌面应用，Charles 或 Proxyman 更对路；想要可脚本化的 CLI/Python 代理，mitmproxy 比 web-UI + 规则文件的模式更合适。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| Charles | 未收录 | 需要打磨成熟的付费原生桌面代理时，选 Charles。 | 付费原生桌面代理；抓包/改写/限速的 GUI 成熟、打磨度高，但需商业授权，且不像 whistle 那样由配置文件规则驱动。 |
| Fiddler | 未收录 | Windows 优先的老牌调试代理和 .NET 脚本生态更重要时，选 Fiddler。 | 老牌、Windows 优先的调试代理（Fiddler Classic / Everywhere）；.NET 生态丰富、有 FiddlerScript，但更重，且部分商业/闭源。 |
| [mitmproxy](mitmproxy.zh.md) | ✅ | 可编程 Python 拦截是优先项时，选 mitmproxy。 | 开源 Python 代理，脚本/插件 API 强，带 CLI/TUI；更适合可编程拦截，少了点点即用的规则 UI。 |
| [anyproxy](anyproxy.zh.md) | ✅ | 更偏好阿里的 Node.js 代理和 JS 规则文件时，选 AnyProxy。 | 阿里的 Node.js HTTP/HTTPS 代理，用 JS 规则文件；气质上更接近 whistle，但社区更小，且规则写在 JS 里而非 whistle 的行语法。 |
| Proxyman | 未收录 | 现代原生 GUI 比 npm/web-UI 运行方式更重要时，选 Proxyman。 | 现代原生 macOS/跨平台调试代理，GUI 精致；freemium/商业，是应用形态而非 web-UI + npm 工具。 |

## 技术栈

- **语言/运行时：** 基于 Node.js 的 JavaScript——以 npm CLI 安装运行（`whistle` / `w2`）。
- **架构：** 一个本地代理服务器加一个 web UI；流量按规则行匹配（一套自有的 whistle 规则 DSL：pattern → 操作符，如 `file://`、`resBody://`、`host`、`req`/`res` 修改符、`weinre`/inspect 等）。
- **协议：** HTTP、HTTPS（通过可安装的根 CA 做解密）、HTTP/2、WebSocket。
- **可扩展性：** 一套插件系统（whistle 插件以 `whistle.<name>` 的 npm 包发布）扩展匹配/处理。[未验证]

## 依赖

- **Node.js** 是唯一的硬运行时依赖——你需要一个 Node 环境来安装和运行它（`package.json` 声明了 `engines.node` 下限，确切最低值由仓库设定且随时间变动）。[未验证]
- **根 CA 安装** 到每个要解密 HTTPS 的客户端——这是个安装/运维层面的依赖，而非一个服务。
- 不需要搭数据库或外部服务；状态和规则都存在本地。

## 运维难度

**低。** 一句 `npm i -g whistle`（或 `npx`）然后 `w2 start` 即可；web UI 跑在本地，规则在界面里或规则文件里编辑。唯一真正的摩擦是 HTTPS：给每个要解密的客户端/设备生成并安装根证书，且每个设备/系统都得重做一遍。把它作为共享/团队实例运行、或代理移动设备，会多一点网络配置（大家把代理指向那台主机、信任证书），但没有集群、数据存储或扩容方面的顾虑，因为它是开发工具而非基础设施。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 18.4 小时，基于 15 个 qualifying issues/PRs。
- **维护（2026-06）。** 最后 push 于 2026-06 且未归档；tag 已到 v2.10.x，表明它在**活跃发布**，并未弃坑。[推断]
- **治理 / bus factor。** 仓库 owner 是**单个 GitHub User 而非组织**——实质上是一名维护者。这是个实打实的 **bus-factor 标记**：路线图与延续性系于一人，尽管项目本身已存在很久。[推断]
- **年龄与 Lindy 判断。** 2015-03 创建（约 11 年）且**仍然活跃**⇒ 对它的细分领域是个**强 Lindy** 信号——一个调试代理能活下来并维护十年，比一个新秀更值得押注，尽管有单维护者这一保留项。[推断]
- **采用度。** ~15.6k star，在中文前端社区相当知名；在那里被广泛当作 Fiddler/Charles 的替代品。star 数仅供参考，不等于当前健康度的证明。[未验证]
- **风险标记。** MIT 许可、未发现 relicense 历史；主要风险是单维护者的 bus factor 与 HTTPS-MITM 固有的信任模型，而非许可问题。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 15.6k star、版本 v2.10.x——star 数和版本号对时间敏感、会漂移，仅供参考。
- [未验证] 最低 Node.js 版本由仓库 `package.json` 的 `engines` 字段声明且随时间变化，这里不断言具体数字。
- [未验证] “文档以中文为主”是从项目起源和社区做出的推断；英文文档存在，但其完整度未被穷尽核查。
- [未验证] 插件生态（`whistle.<name>` 包）与完整的规则操作符集来自项目自身的表述；具体插件的成熟度未逐一核实。
- [推断] “单维护者”是从 owner 为 GitHub User 账号推断而来；真实的贡献者分布未逐人测量。
