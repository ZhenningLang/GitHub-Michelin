---
name: FluentRead
slug: fluentread
repo: https://github.com/Bistutu/FluentRead
category: reading-tools
tags: [browser-extension, translation, immersive-translation, bilingual-reading, byok, ollama, typescript]
language: TypeScript
license: GPL-3.0
maturity: v0.0.28 manifest, active, ~7.3k stars (as of 2026-07)
last_verified: 2026-07-08
type: tool
upstream:
  pushed_at: 2026-03-07T04:12:24Z
  default_branch: main
  default_branch_sha: ab1be13b31b9aaa874eb7e7d5ac652d722ba649a
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:50:45Z
  overall: C
  overall_score: 2.33
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
        last_commit_age_days: 6
        active_weeks_13: 7
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 10.1
        qualifying_issues: 47
        band: relaxed_solo
        window_offset_days: 3
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 220
        release_assets: 8
        release_tier: D
        signal_basis: releases
    longevity:
      grade: B
      raw:
        repo_age_days: 1006
        last_commit_age_days: 6
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 10
        top1_share: 0.979
        top3_share: 0.989
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: D
      raw:
        spdx_id: GPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
---

# FluentRead

一个开源沉浸式翻译浏览器扩展，面向双语网页阅读、划词翻译、全文翻译、回译，以及 20+ 翻译引擎，包括 OpenAI、DeepSeek、Kimi、Claude、Gemini、Ollama 和 OpenAI-compatible 自定义端点。

![FluentRead — 健康度雷达](../../assets/health/fluentread.zh.svg)

## 何时使用

你是中文用户或团队，想要一个开源沉浸式翻译扩展，体验接近商业版 Immersive Translate：双语对照、仅译文模式、划词翻译、全文翻译悬浮入口，以及一长串传统与 AI 翻译引擎。你希望配置留在本地，用自己的 OpenAI／DeepSeek／Kimi／Claude／Gemini／Ollama 凭据，不依赖官方闭源扩展仓库。

当核心任务是网页阅读和翻译，而不是完整语言学习套件时，选 FluentRead。它比 Read Frog 更早，并明确把自己定位为“Open Immersive Translate”；当你需要 Firefox／Edge／Chrome 商店可用性和许多内置引擎时，选它而不是 Margin Read；当更简洁的翻译优先 UX 比 TTS、YouTube 字幕翻译和语言学习附加功能更重要时，选它而不是 Read Frog。

## 何时不用

- **你需要宽松许可复用或闭源再分发。** 改用 [Margin Read](margin-read.zh.md)；FluentRead 是 GPL-3.0。
- **你需要最清晰的 OpenAI-compatible／本地端点文档。** 改用 [Margin Read](margin-read.zh.md)，或在采用前核验 FluentRead 的 custom engine 源码；FluentRead 支持 `custom` OpenAI-compatible 服务并文档化 Ollama 设置，但协议面没有 Margin Read 的 README 写得那么产品化。
- **你需要字幕、TTS 或语言学习工作流。** 改用 [Read Frog](read-frog.zh.md)；FluentRead 已核验范围是网页／划词／全文翻译、回译、缓存和引擎。
- **你想要强多人维护项目。** 如果更广的贡献者活跃度重要，选 [Read Frog](read-frog.zh.md)；FluentRead 的贡献计数高度集中在 owner 账号。
- **你不能接受浏览器侧 provider 调用。** 改用你自己控制的 server-side 翻译代理，或浏览器内置翻译；FluentRead 会从扩展把文本发给第三方或配置端点，所以 provider 隐私、计费和 rate limit 都归你负责。
- **你需要 GitHub release cadence 作为审计材料。** 改用 [Pair Translate](pair-translate.zh.md) 或 [Margin Read](margin-read.zh.md)；本轮 GitHub API snapshot 没返回 FluentRead 的 Releases 或 tags，商店／package 版本节奏需要另查。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Read Frog](read-frog.zh.md) | ✅ | 当学习功能、TTS、字幕翻译、批量请求和更活跃 release automation 足以抵消更大表面积时，选 Read Frog；当你要聚焦开源沉浸式翻译 UX 时，选 FluentRead。 | Read Frog 更丰富且非常活跃，但更年轻、表面积更大；FluentRead 翻译优先且历史更长，但单维护者集中度更高。 |
| [Margin Read](margin-read.zh.md) | ✅ | 当 MIT 许可、明确 BYOK／本地端点文档和隐私 threat model 是决定因素时，选 Margin Read；当许多引擎和跨商店浏览器支持更重要时，选 FluentRead。 | Margin Read 宽松许可且透明，但仍是早期 Chrome／Chromium 优先；FluentRead 对终端用户更成熟，但 GPL 且端点协议细节没那么显式。 |
| [Pair Translate](pair-translate.zh.md) | ✅ | 当你要较轻量的双语扩展、release zips 和许多 provider 模板时，选 Pair Translate；当目标更接近完整沉浸式翻译阅读时，选 FluentRead。 | Pair Translate 更轻并验证了本地模板；FluentRead 更直接围绕沉浸式翻译定位，star 也更多。 |
| Immersive Translate 官方仓库 | 未收录 | 不要把官方仓库当作开源候选；当你要求源码可见且自管引擎时，选 FluentRead。 | Immersive Translate 是产品标杆，但公开仓库不包含扩展源码。 |
| DeepL / Google Translate 浏览器功能 | 未收录 | 当低设置成本和厂商托管质量更重要时，选内置／厂商翻译；当任务是本地配置、多引擎和双语网页布局时，选 FluentRead。 | 厂商／浏览器翻译更省事，但通常不适合 BYOK／自定义端点，双语阅读可配置性也弱。 |

## 技术栈

- **扩展框架：** WXT Manifest V3，配 Vue 3、Element Plus、webextension-polyfill、WXT storage 和 Vite。
- **翻译服务：** Microsoft、Google、DeepL／DeepLX、小牛、有道、腾讯等传统引擎；OpenAI、Azure OpenAI、Gemini、Claude、DeepSeek、Moonshot／Kimi、Groq、OpenRouter、Ollama／custom 等 AI 引擎。
- **自定义引擎：** 源码含 `custom` 服务，默认指向 `http://localhost:11434/v1/chat/completions`，使用 bearer token，并期待 OpenAI-compatible 的 `choices[0].message.content` 响应形状。
- **文档栈：** 扩展源码旁边有 VitePress／VuePress 文档。
- **工具链：** pnpm 9.x、TypeScript、vue-tsc、通过脚本运行的 Biome／ESLint 类检查，以及 WXT zip／build targets。

## 依赖

- **运行时：** Chrome、Edge、Firefox，或其他兼容浏览器扩展环境。
- **服务商凭据：** 取决于所选引擎的 API key／token／AK／SK／appid／secret 字段。
- **本地 Ollama／custom endpoint：** FAQ 的快速路径要求配置类似 `OLLAMA_ORIGINS="*"` 的 CORS；在共享机器上用之前应审查这个便利设置。
- **构建：** pnpm、Node／TypeScript／Vite／WXT 工具链。

## 运维难度

**个人使用低，私有模型使用中等。** 商店安装和普通 API key 配置很简单。复杂度出现在你需要私有／本地模型路由时：扩展从浏览器调用配置端点，所以 CORS、HTTP vs HTTPS、API key 存储、端点可用性和 provider 响应兼容性都会变成运维约束。团队还应写清允许哪些引擎、secrets 怎么轮换。

## 健康度与可持续性

- **维护（2026-07）。** 仓库未归档，2026-03 仍有 push；package manifest 版本是 0.0.28。GitHub Releases／tags 没有返回，所以仅凭 GitHub 难以审计 release cadence。
- **治理 / bus factor。** User-owned 仓库，贡献高度集中在 `Bistutu`；这是强采用度之外最主要的可持续性弱点。
- **年龄与 Lindy。** 创建于 2023-12，比 2025／2026 的替代品更有历史，但对一个日常依赖的浏览器扩展来说仍偏年轻。
- **采用度。** 约 7.3k star，并有 Chrome／Edge／Firefox 安装链接，说明有明显用户兴趣；商店指标未检查。
- **风险标记。** GPL-3.0、浏览器侧文本外发到所选 provider、未验证的治理／安全文档，以及 Ollama CORS workaround，都需要明确 review。

## 存疑（未验证）

- [未验证] Chrome／Edge／Firefox 商店版本、安装数和审核状态没有检查。
- [未验证] API key／secret 似乎进入扩展配置字段，但静态加密和完整存储生命周期没有审计。
- [未验证] 没有运行时测试所有列出的引擎；文档和源码列表不能替代逐 provider 验证。
- [未验证] 除仓库元数据和贡献集中度外，没有深入测量 issue／PR 响应速度。
- [推断] 单维护者风险来自 top contributor 计数和 User ownership；公开仓库外的私有／社区治理没有验证。
