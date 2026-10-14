---
name: NopeCHA
slug: nopecha-extension
repo: https://github.com/NopeCHALLC/nopecha-extension
category: captcha
tags: [captcha, browser-extension, captcha-solving, browser-automation, hosted-api]
language: JavaScript
license: MIT
maturity: stable 0.6.1, prerelease 0.6.2-rc.2, 11033 stars; current source closed (as of 2026-10-14)
last_verified: 2026-10-14
type: tool
upstream:
  pushed_at: 2026-10-02T18:27:45Z
  default_branch: main
  default_branch_sha: 5b198e1c256afddfc6ae4b01544d357e79ee4544
  archived: false
health:
  schema: 1
  computed_at: 2026-10-14T06:57:22Z
  overall: B
  overall_score: 3.33
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
        last_commit_age_days: 12
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 1.9
        qualifying_issues: 30
        band: relaxed_solo
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: null
        canonical_package: null
        release_downloads: 2810100
        release_assets: 120
        release_tier: B
        signal_basis: releases
    longevity:
      grade: A
      raw:
        repo_age_days: 1301
        last_commit_age_days: 12
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.571
        top3_share: 1.0
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

# NopeCHA

授权的浏览器测试遇到多类验证码，你不想逐类接接口；NopeCHA 用一个扩展连接托管服务，但当前实现闭源，不能从此仓库重建。

![NopeCHA 健康度雷达](../../assets/health/nopecha-extension.zh.svg)

当前产品不是可审查的开源扩展。保留的 MIT 仓库和历史 0.3.3 源码，不能证明当前二进制的许可或实现。

## 何时使用

你是自动化工程师，正在测试自己的应用，或测试一个已获得明确授权的预发布环境。测试旅程里出现多类验证码，静态 fixture 又不足以覆盖真实交互。你想给 Chrome、Firefox、Selenium、Puppeteer 或其他 Chromium 自动化环境装一个扩展，而不是为每类挑战分别接 solver。NopeCHA 会在浏览器中检测支持的挑战，并把识别工作提交给托管的 NopeCHA API。

当你需要无人值守地覆盖多类验证码，并愿意用本地可审计性和人工触发式无障碍体验来换取更广的自动化覆盖时，可以在 Buster 与 NopeCHA 之间选择后者。这个选择只有在系统所有者已授权测试、允许外部 API 处理数据，并且测试计划能容忍成功率、额度和服务可用性变化时才成立。

## 何时不用

- **你不拥有目标系统，也没有明确授权。** 不要用 NopeCHA 或其他 solver 规避第三方访问控制；改用站点官方 API、验证码提供方的测试密钥，或所有者提供的测试环境。
- **你需要审计当前实现的完整源码。** 人工触发的 reCAPTCHA 音频辅助可用 Buster；授权测试也可用 Playwright 配合测试 fixture。NopeCHA 持续维护的 0.6.x 扩展源码不在默认分支中。
- **挑战数据不能离开你的环境。** 使用提供方测试密钥或本地模拟；README 描述的是托管 API 依赖，不是离线识别器。
- **你需要确定性的 CI，而不是真实验证码识别。** 用 Playwright mock 验证响应，或使用官方验证码测试密钥；没有 solver 能承诺面对持续变化的挑战仍稳定识别。
- **你只需要帮助真人处理 reCAPTCHA 音频挑战。** 用 Buster；它是用户主动触发的音频辅助流程，不是广覆盖的无人值守识别服务。
- **你需要源码级库接口，而不是装一个全浏览器扩展。** 可在同一授权边界内评估 2captcha-python 这类服务 SDK，同时接受它单独带来的服务、隐私和计费取舍。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Buster](buster.zh.md) | 已收录 | 需要真人触发、源码可审计的 reCAPTCHA 音频辅助时选 Buster；只有在已授权且要无人值守覆盖多类验证码时，才选 NopeCHA。 | Buster 更窄，可走本地或远端语音识别；NopeCHA 覆盖更广，但当前实现闭源并依赖托管服务。 |
| 2captcha-python | 未收录 | Python 程序需要明确的 API 客户端，而不是浏览器扩展时，选 2captcha-python；需要浏览器侧检测与交互时再选 NopeCHA。 | 两者都依赖外部识别服务，但接口、价格、数据处理和支持范围不同。 |
| [Text_select_captcha](text-select-captcha.zh.md) | 已收录 | 已授权场景需要本地中文点选文字管线时，选 Text_select_captcha；需要一个服务覆盖多类浏览器验证码时，选 NopeCHA。 | Text_select_captcha 本地且专用，但没有许可授权；NopeCHA 更广，却不公开当前实现。 |

## 快速上手

仅在自有或明确授权环境中，使用 [README.md:100–118](https://github.com/NopeCHALLC/nopecha-extension/blob/5b198e1c256afddfc6ae4b01544d357e79ee4544/README.md#L100-L118) 的 Chrome、Firefox 商店链接，或选择固定发布包。稳定版 0.6.1 与较新的预发布版 0.6.2-rc.2 分开；历史 0.3.3 构建不是当前安装路径。README 称安装后会自动处理支持的网页，并提供按 IP 计数的每日最多 100 次无密钥请求；这是厂商条款，不是独立验证的服务保证。自动化浏览器集成应按其链接文档操作，不从历史源码猜当前参数。你负责授权、浏览器隔离、允许的外发数据和付费额度；厂商提供当前二进制与托管识别，内部机制在此无源码可查。

![NopeCHA — 主干用户故事](../../assets/flow/nopecha-extension.zh.svg)

<!-- flow-steps:begin (generated from flows/nopecha-extension.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：确认测试授权，选择浏览器与允许的数据外发
2. **NopeCHA**：提供对应扩展商店入口与发布构建 — 组件：`公开文档与分发`
3. **你**：安装固定的当前产物，不用已停支持的历史构建
4. **NopeCHA**：说明支持网页的自动处理与按 IP 计数的无密钥额度 — 组件：`文档声明的厂商服务`

**价值**：取得文档可核的当前分发路径；闭源实现和服务保证仍未审查

</details>
<!-- flow-steps:end -->

## 技术要点

- **当前可见的是分发边界，不是识别算法。** [README.md:100–118](https://github.com/NopeCHALLC/nopecha-extension/blob/5b198e1c256afddfc6ae4b01544d357e79ee4544/README.md#L100-L118) 组织商店入口，把按 IP 计数的无密钥使用与账号额度分开；[README.md:160–173](https://github.com/NopeCHALLC/nopecha-extension/blob/5b198e1c256afddfc6ae4b01544d357e79ee4544/README.md#L160-L173) 明确用发布构建替代当前公开源码。这解释获取方式与厂商依赖；当前检测、模型和在线强化学习内部无源码可查，本页不为其实现背书。
- **仅历史 0.3.3：按挑战族分开注入页面框架。** [manifest.base.json:3–100](https://github.com/NopeCHALLC/nopecha-extension/blob/6d97479a82a9792b3b6741e751964867523d66a5/manifest.base.json#L3-L100) 声明全框架脚本、提供方网址模式，以及文档开始或结束时注入。旧扩展由浏览器侧处理器组成，不是一个进程内接口，并有广泛网页访问面。这些是历史清单事实，不代表维护中的 0.6.x 权限或识别机制。
- **仅历史 0.3.3：共享源码加浏览器专属打包。** [build.py:193–250](https://github.com/NopeCHALLC/nopecha-extension/blob/6d97479a82a9792b3b6741e751964867523d66a5/build.py#L193-L250) 读取基础清单，复制共享及浏览器专属文件，删除模块导出生成 `utils.js`，合并权限后写清单和归档。它同步了旧工具代码的两种变体，不能复现构建当前闭源分发包。

## 技术栈

- **当前分发：** GitHub release 和浏览器商店提供预构建的 Chromium、Firefox 扩展包。
- **托管后端：** 浏览器扩展调用 NopeCHA API 做多模态验证码识别；当前服务端与模型实现不在本仓库中。
- **历史开源分支：** `legacy-oss` 包含处理 reCAPTCHA、hCaptcha、FunCaptcha、AWS WAF 和文字验证码的 JavaScript WebExtension content scripts，以及 Python 构建脚本。
- **浏览器权限：** 历史 Manifest V3 构建申请广泛的 host 权限，并向挑战 frame 注入脚本；当前 0.6.x 的权限应从实际分发包重新检查。

## 依赖

- Chrome、Chromium 或 Firefox，并从商店或 release 安装扩展。
- 能访问托管的 NopeCHA API；更高额度和部分能力需要 NopeCHA 账号与 API key。
- Selenium、Puppeteer 或 Playwright 由外围自动化流程提供，不属于本仓库的运行依赖。
- 目标所有者授权、测试凭据和验证码提供方认可的测试配置仍是运行前提。

## 运维难度

**安装低，长期依赖中等。** 装扩展很简单，但测试可靠性取决于第三方 API、持续变化的验证码实现、额度、商店或 release 更新，以及浏览器权限。应固定扩展产物，在隔离测试 profile 中运行，尽可能限制目标 host，并为 CI 保留确定性的 mock 路径。识别失败应作为预期分支处理，不能据此断言目标系统不可用。

## 健康度与可持续性

- **实测信号（2026-10-14）：** B/A/B/A/C/A，整体 B，覆盖 6/6 轴，无未知轴。许可 A 来自仓库 MIT 文件，不是闭源二进制的法律结论。
- **维护情况：** 主分支在 2026-10 有更新；稳定版 0.6.1 发布于 2026-06-11，预发布版 0.6.2-rc.2 发布于 2026-08-20。它度量公开分发活动，不证明私有开发过程可见。
- **治理：** 仓库属于个人账号，服务路线由 NopeCHA 控制；用户无法只依靠默认分支独立维护当前扩展实现。
- **年龄与 Lindy：** 仓库约三年，并且仍在发版，这是有限的正向信号；但 2023 年的闭源转向削弱了它作为开源依赖的耐久性。
- **采用信号：** 11033 star 与实测发布下载量表明关注和获取，不代表准确率、授权或服务连续性。
- **风险标记：** 当前源码闭源、依赖托管服务、浏览器访问面广、当前二进制许可边界不清，以及验证码对抗环境可能随时造成能力回退。

## 存疑（未验证）

- [未验证：当前实现无源码可查] 当前 0.6.x 检测、模型、网络处理与强化学习不能在此审查或重建；公开 README 声明与历史 0.3.3 打包不算当前实现证据。
- [未验证] 已实读仓库 MIT LICENSE，但它是否覆盖当前闭源的 0.6.x 二进制和托管服务组件并不清楚；再分发或内置前应取得维护者说明。
- [未验证] 支持的挑战类型、免费额度、价格、保留策略和数据处理行为都可能在仓库外变化。
- [未验证] 不保证识别、解题成功或持续适配挑战变化；README 中的效果描述没有经过独立基准验证。
- [未验证：未下载或运行闭源产物] 没有测试商店或发布包权限、实际数据去向、额度执行和浏览器行为；厂商的 100 次额度是有日期的文档，不是实测或服务等级保证。
- [推断：默认分支无实现，历史源码为JavaScript] `language: JavaScript` 记录历史扩展语言，不是已证实的当前二进制语言；GitHub 对主线返回 null。
- [推断] 合法使用取决于目标所有权、明确授权、提供方条款和当地法律；本页是选型信息，不是法律意见。
