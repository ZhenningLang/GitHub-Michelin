---
name: wxappUnpacker
slug: wxappunpacker
repo: https://github.com/xdmjun/wxappUnpacker
category: wechat
tags: [wechat, miniprogram, wxapkg, decompiler, reverse-engineering, nodejs]
language: JavaScript
license: GPL-3.0-or-later
maturity: tombstone — repo emptied 2023-04, lineage archived, ~2.4k stars (as of 2026-06)
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2023-04-08T12:38:11Z
  default_branch: master
  default_branch_sha: 7ec65cf2446f02a539001ebbbd6a7afeb49fb74e
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:21:29Z
  overall: E
  overall_score: 0.0
  scored_axes: 4
  applicable_axes: 6
  capped: true
  cap_reason: "source-available/no-license: NONE"
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1263
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
        repo_age_days: 2487
        last_commit_age_days: 1263
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: E
      raw:
        spdx_id: NONE
        permissiveness: source_available
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: empty_or_gated }
---

# wxappUnpacker

一个微信小程序 `.wxapkg` 反编译/解包工具——只不过*这个具体的 fork* 已被清空：`xdmjun/wxappUnpacker` 仓库如今只剩一个 `README.md`，内容就是字符串 `del`。它是一座墓碑，真正能用的代码只活在各个 fork 里。

![wxappunpacker — 健康度雷达](../../../assets/health/wxappunpacker.zh.svg)

## 何时使用

你是移动安全研究者（或者丢了*自己*那个微信小程序源码的开发者），手里拿着从设备上扒下来的 `.wxapkg` 包，需要把这个打包后的二进制还原成可读的 `.wxml` / `.wxss` / `.json` / `.js`，好审计它做了什么或找回素材。wxappUnpacker 这套 Node.js 脚本（`wuWxapkg.js`、`wuWxss.js`、`wuWxml.js`、`wuJs.js`）正是干这个的社区主力反编译器——对着包跑一下启动脚本，它就把工程目录还原出来。

但要清楚你真正该拿的*不是这个仓库*。`xdmjun/wxappUnpacker` 是个空壳。想要能跑的代码，你得去找一个还有人维护的 fork（这条血缘可追溯到 `qwerty472123/wxappUnpacker`，而后者自 2020 年起也已 archived/只读）。把本页当作链条上一个死节点的警示牌，而不是安装目标。

## 何时不用

- **这个仓库没有代码——没有任何东西可装可跑。** 唯一的 HEAD 提交（"del"，2023-04-08）把所有内容替换成了字符串 `del`。`language` 为空，无 LICENSE 文件，无 release，无 tag。专门选 `xdmjun/wxappUnpacker` 就是死路一条。[未验证]
- **整条血缘都已废弃。** 上游 `qwerty472123/wxappUnpacker` 自 2020-04 起 archived（只读），这个 fork 在 2023 年自删。bus factor 实质为零——`.wxapkg` 格式一变，没人会来修。
- **依赖已弃用的 `vm2`。** 保留下来的 fork 代码依赖 `vm2@^3.6.0`，其作者在多个严重沙箱逃逸 CVE 之后已弃用它。拿它处理不受信任的包输入，是实打实的供应链/RCE 风险。[推断]
- **法律 / ToS 风险。** 反编译第三方 `.wxapkg` 等于逆向别人的小程序；这通常违反微信平台条款，也可能侵犯目标 app 的著作权。仅对你自己拥有或有明确授权的 app 才站得住脚。
- **这个 fork 没有明确许可证。** GPL-3.0 只在各 fork 的 `package.json` 里声明；`xdmjun` 根本不带 LICENSE 文件，其再分发条款是未定义的。[未验证]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| qwerty472123/wxappUnpacker（上游） | 未收录 | 原始血缘和更完整的归档代码更重要时，选上游。 | 原始血缘，比这个被清空的 fork 完整，但**自 2020 起 archived/只读**——同样没人维护，只是没被删。 |
| 其它活着的 fork（SangeCoder / PyCoreDev / yangyang5214） | 未收录 | 能跑的代码幸存状态比本清空仓库更重要时，选活着的 fork。 | 能跑的代码幸存于此；PyCoreDev（2023-02）保留了完整代码 + `package.json`。都不大，也没明显维护——按近期活跃度挑，并自己读 diff。 |
| 自写解包脚本 | 未收录 | 只需从 `.wxapkg` 提取素材时，选自写脚本。 | `.wxapkg` 格式有足够文档，临时脚本是存在的；若你只需提取素材而非完整还原源码，这条路可行。 |

## 技术栈

- **语言：** Node.js（CLI 脚本，无构建步骤）。入口脚本 `wuWxapkg.js`（包）、`wuWxss.js`（CSS）、`wuWxml.js`（XML）、`wuJs.js`（JS），辅以 `wuLib.js` / `wuRestoreZ.js` 与 `bingo.sh` / `bingo.bat` 启动器。[推断——从一个活着的 fork 重建；本仓库自身历史已被覆盖]
- **解析/代码生成依赖：** `cheerio`、`css-tree`、`cssbeautify`、`escodegen`、`esprima`、`js-beautify`、`uglify-es`，以及沙箱执行器 `vm2`。

## 依赖

- **运行时：** Node.js。无服务、无数据存储——就是一批做文件变换的脚本。
- **输入：** 一个或多个 `.wxapkg` 包文件（需你另行从设备获取）。
- **危险依赖：** 依赖链里有 `vm2`（已弃用、有沙箱逃逸 CVE 史）（见存疑）。

## 运维难度

**本仓库无从谈起**——没东西可运维。对一个能用的 fork：**低**（clone、`npm install`、对文件跑脚本）。没有服务器、没有状态、没有部署；就是一次性 CLI 变换。唯一真实的运维隐患是：若处理不信任的包，会触及 `vm2` 风险。

## 健康度与可持续性

- **响应速度**：无法计算——no_data。
- **维护（2026-06）。** 已废弃——唯一一次真实提交在 2023-04-08 把仓库清空；2026-06 的 `updated_at` 只是元数据触碰，不是活动。上游 `qwerty472123` 血缘自 2020 起 archived。**是死，不是吃老本。**[未验证]
- **治理 / bus factor。** bus factor 为 **0**：被单个 User 账号所有者删除，上游冻结。整条链上无 release、无 tag、无活跃贡献者。
- **年龄 × Lindy。** 创建于 2019-12，血缘更老（上游约 2020）。这里年龄毫无意义，因为它*不活跃*——Lindy 要求又老**又**活，它在第二条上不及格。[推断]
- **采用度。** ~2.4k star / ~1.35k fork 攒在如今已不存在的代码上；这些 star 是昔日热度的化石，不是维护信号——正是那种该警惕的“流行但已死”异常。[未验证]
- **风险标记。** 自愿自删（动机未确认，大概率法律/ToS）、本 fork 许可证未定义、能用的 fork 里有弃用的 `vm2`，再加上 `.wxapkg` 反编译底层的 ToS/著作权风险。[推断]

## 存疑（未验证）

- [未验证] 流行的“这个仓库被 DMCA / 被下架”说法**得不到**元数据支持：仓库是活的（`disabled: false`、`archived: false`），不是 404/451。证据显示的是一次*自愿*的 "del" 提交，而非平台下架。
- [推断] 所有者很可能出于法律/ToS 顾虑自己抹掉了仓库，但动机未确认。
- [未验证] 本仓库原始的 README、支持范围与确切技术栈都已被覆盖；这里的功能与依赖是从 `PyCoreDev` fork 重建的，该 fork 镜像 `qwerty472123` 血缘，但未必与 `xdmjun` 当年所发完全逐字节一致。
- [推断] `vm2` 的弃用与沙箱逃逸 CVE 史是公认事实；在此具体用法下的可利用性未经审计。
- [未验证] GPL-3.0-or-later 取自各 fork 的 `package.json`；`xdmjun` 仓库不带 LICENSE 文件，其实际条款未定义。
