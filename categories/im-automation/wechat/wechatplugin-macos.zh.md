---
name: WeChatPlugin-MacOS
slug: wechatplugin-macos
repo: https://github.com/TKkk-iOSer/WeChatPlugin-MacOS
category: wechat
tags: [wechat, macos, im-automation, anti-revoke, auto-reply, objective-c, binary-patch, deprecated]
language: Objective-C
license: MIT
maturity: dated — coasting (last pushed 2024-06, ~2y idle) and version-fragile; patches the macOS WeChat client binary, so it breaks on WeChat updates and is likely non-functional on current WeChat (2026-06)
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2024-06-09T03:27:58Z
  default_branch: master
  default_branch_sha: 113b9a06013ce7b8bd7dc067ee8d4501c1c9075b
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T14:42:03Z
  overall: D
  overall_score: 1.33
  scored_axes: 3
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1200
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: E
      raw:
        repo_age_days: 3361
        last_commit_age_days: 1200
        cohort: tool
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
    responsiveness: { reason: no_traffic }
    adoption: { reason: ambiguous }
    governance: { reason: unattributable }
---

# WeChatPlugin-MacOS

一个 macOS 微信**客户端魔改插件**（微信小助手）——消息防撤回、自动回复、远程控制、微信多开，以及一堆界面便利功能——做法是**把插件注入到 macOS 上的 WeChat.app 里**。**话说白了：它靠对*特定*微信版本的客户端二进制打补丁来工作，所以微信一更新它就坏；仓库已沉寂约 2 年（最后 push 于 2024-06）、针对的是老版本微信，因此在当前微信上几乎可以肯定已经跑不起来了。**

![wechatplugin-macos — 健康度雷达](../../../assets/health/wechatplugin-macos.zh.svg)

## 何时使用

你是个 macOS 微信的资深重度用户，并且刻意**把微信钉死在一个老版本**上——README 针对的就是远古版本（徽章写的是微信 2.3.22，更新日志提到支持到 3.7.0）——你想把那些经典的体验增强找回来：发送方撤回也不消失的消息（防撤回）、按关键词自动回复的机器人、两个微信账号并排多开、窗口置顶，以及 Alfred 快捷发送工作流。你能接受关掉微信的自动更新、把注入式插件装进 `WeChat.app`，也接受一旦让微信更新，整套东西就停摆。在这种狭窄的、冻结版本的设置里，WeChatPlugin-MacOS 是 macOS 微信魔改的范本实现。

现实地说，这基本上是 2026 年还去碰它的**唯一**场景：一个你永不更新的、钉死的老版本 macOS 微信，跑在一个无所谓或低风险的账号上，你看重这些魔改胜过稳定性和账号安全。只要上述任一条件不成立，就请看下文——这是博物馆藏品，不是能拿来搭东西的地基。

## 何时不用

- **你用的是当前 / 自动更新的微信。** 这是最主要的排除项。插件**针对特定微信版本对 WeChat.app 二进制打补丁**，所以**微信每更新一次它就坏一次**——而仓库已沉寂约 2 年、针对的是 2.3.x–3.7.x 这般老的版本，因此在今天发行的微信上**几乎可以肯定已经不可用**。承重判断：这不是“也许需要调一下”，而是“地基没了”。[推断]
- **你在乎这个账号。** 驱动一个被增强 / 注入过的微信客户端，是**违反微信服务条款**的，并带有真实的**限流 / 冻结 / 永久封禁**风险。别拿一个你输不起的账号去试。
- **安全敏感场景。** 你是在**往一个握有你私密对话和通讯录的消息客户端里注入第三方代码**——一个巨大的信任与攻击面（插件能读 / 改微信看到的一切）。一个无人维护的注入器只会放大这种风险。
- **你不在 macOS 上。** 它**仅限 macOS**，打的是桌面版 WeChat.app 的补丁；对 Windows、移动端或服务端自动化，这里什么都没有。
- **你需要可编程 / 受支持的 IM 自动化。** 这是桌面 UI 魔改，不是 API。要做合规自动化，请用**企业微信（WeCom）API** 或**微信公众号 / 小程序**服务端 API；要做个人号风格的机器人，[ItChat](itchat.zh.md) 及其后继者也存在（但它们同样已死 / 脆弱，并带有相同的 ToS 风险）。
- **生产环境或任何必须保持运行的东西。** 一个针对自动更新客户端的无人维护二进制补丁，撑不起一个稳定依赖。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| WeChatTweak-macOS（Sunnyyoung 分叉 / 后继） | 未收录 | 坚持 macOS 微信魔改且想要较新的后继项目时，选 WeChatTweak-macOS。 | macOS 微信魔改的社区后继——同一类防撤回 / 多开功能，但维护更近、带 CLI 安装器；它仍是针对特定微信版本的二进制补丁，因此继承了同样的版本脆弱性和 ToS / 封号风险。如果你执意走这条路，它是更明智的选择。 |
| [ItChat](itchat.zh.md) | ✅ | 需要网页微信协议的可编程库、而非桌面魔改时，选 ItChat。 | 通过（已失效的）网页协议自动化微信**个人号**的 Python 库——是可编程 API，而非桌面客户端魔改。它也已基本死亡且被平台封堵；面不同（网页协议 vs 二进制注入），但“已废弃 + ToS 风险”的结论相同。 |
| 官方微信（不装插件） | 未收录 | 账号安全和干净更新比魔改功能更重要时，选官方微信。 | 受支持的路径：没有防撤回、没有自动回复、没有多开，但它能干净地更新、不是封号风险，也不往你的消息工具里注入外来代码。对任何在乎账号的人来说，这才是诚实的默认选择。 |
| 企业微信 / 公众号 / 小程序 API | 未收录 | 合规的企业或公众平台自动化面能满足需求时，选腾讯官方 API。 | 腾讯**官方、受认可**的自动化面；稳定且有支持，但它们自动化的是企业 / 公众号场景，而非你的个人桌面微信——是合规但不同的产品，并非平替。 |

## 技术栈

- **语言：** Objective-C——一个 macOS WeChat.app 插件，也就是运行在微信进程**内部**的代码。
- **机制：** 对 `WeChat.app` 做二进制 / 运行时**打补丁与注入**（经典的 macOS "tweak" 套路——hook/swizzle 微信自己的 Objective-C 方法，来加入防撤回、自动回复等）。
- **能力面：** 防撤回、按关键词自动回复、远程控制（含通过 AppleScript 辅助脚本做语音 / 系统控制）、微信多开、窗口置顶、会话相关调整，以及 Alfred 工作流集成。
- **耦合：** 与特定微信客户端版本紧耦合——README 明确标注“支持微信 2.3.22 / 3.7.0”，这正是脆弱性的根源。

## 依赖

- **一个特定的、钉死的 macOS WeChat.app**——真正的依赖。插件必须匹配它所针对的微信版本；你通常得**关掉微信的自动更新**来保住一个兼容的版本，而且一般需要非 App Store 版的微信。
- **macOS**（桌面）——没有其他平台适用。
- **辅助功能 / 自动化权限**用于远程控制功能（README 指示在“系统偏好设置 → 安全性与隐私 → 辅助功能”里添加微信和脚本编辑器）。
- **可选：Alfred**，用于快捷发送工作流（一个独立的 `wechat-alfred-workflow` 仓库）。
- **构建：** 若不用预编译安装，从源码编译需要 Xcode / Objective-C 工具链。

## 运维难度

**装起来看似很低，但真正的难点是让它根本能持续工作——而这你基本做不到。** 把插件装进 WeChat.app 是有引导的过程（仓库附了 `Install.md`），顺路径就几步。难的、赢不了的部分是**版本管理**：你必须把微信冻结在一个兼容版本、拒绝每一次更新（微信会反复提示并能自我更新）、在任何被迫升级后重新打补丁——而由于项目约 2 年前就停止跟进新微信版本，根本不存在一个可供打补丁的、面向当前微信的维护版本。没有服务或数据存储要跑；全部运维负担就是用一个无人维护的补丁去对抗一个自动更新的客户端，这是个必败的局面。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）：吃老本 → 实质已死。** 最后 push 于 **2024-06** → 大约**沉寂 2 年**；约 152 个 open issue，单一维护者（owner 类型为 **User**，`TKkk-iOSer`），未归档但也没动静。这是一个滑向废弃、而非活跃的项目。[推断]
- **天生版本脆弱——决定性信号。** 它**给一个自动更新的客户端二进制打补丁**，且绑死特定微信版本。哪怕是维护良好的同类项目，宿主应用一更新就会立刻失效；一个针对 2.3.x–3.7.x 这般老版本的*无人*维护项目，在当前微信上**按其构造就是不可用的**。[推断]
- **Lindy 判断：实践中不通过。** 创建于 **2017-04**（约 9 年），单看年龄像是 Lindy——但 Lindy 是**年龄 × 仍然活跃**，绝不是单看年龄。这里是**长寿但停更，且在结构上注定失败**（一个追逐移动目标、而维护者已停止追逐的补丁）。它的长寿被*抵消*而非*兑现*——正是 Lindy 失效的教科书案例。[推断]
- **治理 / bus factor。** 单一维护者的个人仓库，没有基金会 / 厂商 / 后继接管——bus factor 为一，而工作已经停了。约 14k 的高 star 数反映的是过去的流行，而非当前的健康。[推断]
- **风险标记。** 违反微信 ToS（封号风险）；往私密消息客户端注入第三方代码的安全风险；仅限 macOS；MIT 许可是整幅图景里唯一没有负担的部分。[推断]

## 存疑（未验证）

- [未验证] “约 14.3k star / 2455 fork / 约 152 个 open issue / 388 watcher” 取自 2026-06 的 GitHub API；star/issue/fork 数对时间敏感且不可靠，仅供参考。
- [未验证] “最后 push 于 2024-06” 是本页承重的维护事实（来自 GitHub API 的 `pushed_at`）；仓库**并未**标记 `archived`，README 中也无显式弃用声明——“实质已死 / 在当前微信上不可用” 是从约 2 年沉寂加上版本脆弱机制*推断*而来，并非引自官方声明。
- [推断] “对 WeChat.app 二进制打补丁 / 注入、微信一更新就坏” 这一机制，是从功能集（防撤回、多开、客户端内 UI 魔改）和 README 明确的逐微信版本支持徽章（2.3.22 / 3.7.0）推断而来；确切注入技术未逐行读源码核实。
- [未验证] 它在今天*任何*仍可安装的微信版本上是否还能工作，未做实测；“在当前微信上几乎可以肯定不可用” 的说法是从沉寂时长与所针对版本做出的推断。
- [未验证] WeChatTweak-macOS 对比行（它当前的维护状态与功能对等程度）描述的是大致格局，未对照该仓库当前状态做新一轮核实。
- [推断] 封号 / 违反 ToS 与安全（代码注入）风险是从工具的非官方注入性质做出的推断，而非实测发生率；严重程度因账号和用法而异。
- [未验证] 依赖与安装细节（需关闭自动更新、非 App Store 版微信、辅助功能权限、Xcode 构建）来自 README 和对 macOS 魔改的一般了解，未对照当前源码 / `Install.md` 重新核对。
