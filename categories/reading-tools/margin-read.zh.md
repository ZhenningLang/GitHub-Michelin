---
name: Margin Read
slug: margin-read
repo: https://github.com/withmargin/margin-read
category: reading-tools
tags: [browser-extension, translation, bilingual-reading, byok, local-llm, openai-compatible, privacy-first, typescript]
language: TypeScript
license: MIT
maturity: v0.3.7, early MVP, ~27 stars (as of 2026-07)
last_verified: 2026-07-08
type: tool
upstream:
  pushed_at: 2026-06-15T16:22:44Z
  default_branch: main
  default_branch_sha: e8b846283b2722d22d41806d5c7b3ed58e6ec821
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:59:18Z
  overall: C
  overall_score: 1.8
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 63
        active_weeks_13: 1
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 63
        release_assets: 18
        release_tier: D
        signal_basis: releases
    longevity:
      grade: D
      raw:
        repo_age_days: 137
        last_commit_age_days: 63
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 4
        top1_share: 0.98
        top3_share: 0.995
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: too_young }
---

# Margin Read

一个 privacy-first 的 Chrome／Chromium 双语网页翻译扩展，明确走 BYOK：不内置 API key，可配置 OpenAI／Anthropic／Gemini 及兼容端点、本地 OpenAI-compatible runtime，带 threat model 文档，并采用 MIT 许可。

![Margin Read — 健康度雷达](../../assets/health/margin-read.zh.svg)

## 何时使用

你是技术用户，已经有 OpenAI-compatible 网关、Ollama、LM Studio、llama.cpp 或私有模型端点，想要一个把这些边界说清楚的浏览器翻译器。你不需要完整商业沉浸式翻译克隆；你要的是双语网页片段、自己的 provider 凭据、可配置 endpoint，以及说明哪些内容会发送、哪些会缓存、还剩哪些风险的 threat model。

当决定性约束是控制权时，选 Margin Read：MIT 许可、无内置 API key、按项目文档无登录／云同步／默认 telemetry、明确的 OpenAI／Anthropic／Gemini-compatible provider adapter，以及本地 endpoint 示例。当终端用户功能完整度、Firefox／Edge 商店覆盖、字幕／TTS 或更大社区比许可和架构透明性更重要时，改选 Read Frog 或 FluentRead。

## 何时不用

- **你今天就需要完整替代 Immersive Translate。** 改用 [Read Frog](read-frog.zh.md) 或 [FluentRead](fluentread.zh.md)；Margin Read 是早期 MVP，明确不含 PDF、EPUB、OCR、输入框翻译、云同步、账号和官方付费额度系统。
- **你需要 Firefox 作为一等目标。** 改用 [Read Frog](read-frog.zh.md)、[FluentRead](fluentread.zh.md) 或 [Pair Translate](pair-translate.zh.md)；Margin Read 先面向 Chrome／Chromium Manifest V3，并说明 Firefox 还不是主要目标。
- **你想要最强采用度／Lindy 信号。** 改用 [Read Frog](read-frog.zh.md) 或 [FluentRead](fluentread.zh.md)；Margin Read 创建于 2026 年，检查快照里只有几十个 star。
- **你不能信任浏览器扩展存 API key。** 改用不把 key 放浏览器里的 server-side 翻译代理；Margin Read 自己的 threat model 说明扩展存储不是安全保险柜。
- **你翻译的是高度交互应用或异常 DOM。** 先用更成熟扩展；README 点名复杂应用、特殊布局和 aggressive DOM rewriting 会有粗糙边缘。
- **你需要已验证的字幕支持。** 改用 [Read Frog](read-frog.zh.md)；Margin Read 文档里 README 排除项与 changelog／beta guide 的 YouTube caption 测试存在不一致，字幕支持应视为未解决。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Read Frog](read-frog.zh.md) | ✅ | 当成熟功能和跨商店分发比许可简单性更重要时，选 Read Frog；当 MIT 许可、BYOK、本地端点清晰度和隐私文档是硬约束时，选 Margin Read。 | Read Frog 更丰富、采用更多，但 GPL／商业双授权；Margin Read 透明且宽松许可，但早期。 |
| [FluentRead](fluentread.zh.md) | ✅ | 当目标是中文优先、支持许多引擎的开源沉浸式翻译器时，选 FluentRead；当你需要可审计的模型网关／本地 runtime 设置时，选 Margin Read。 | FluentRead 终端用户翻译功能和商店覆盖更广；Margin Read provider 边界更清楚，表面积更小。 |
| [Pair Translate](pair-translate.zh.md) | ✅ | 当你想要轻量翻译器、已验证 provider 模板和 Firefox／Edge 链接时，选 Pair Translate；当隐私 threat model 和 MIT 许可决定选择时，选 Margin Read。 | Pair Translate 浏览器覆盖更广、更新活跃，但 GPL-3.0；Margin Read 更宽松、说明更明确，但 Chrome／Chromium 优先。 |
| Immersive Translate 官方仓库 | 未收录 | 只把官方项目当 UX 标杆；当你要求开源、可审计源码和自管 endpoint 时，选 Margin Read。 | 熟悉的产品类别，但官方公开仓库不是扩展源码仓库。 |
| 自定义 userscript／proxy | 未收录 | 只有当翻译面很小且策略约束很重时，才自写 userscript；当一个带 provider adapter 的维护中扩展骨架能省工作时，选 Margin Read。 | 自写代码有完整策略控制，但失去商店打包、options UI、缓存行为和 provider adapter 维护。 |

## 技术栈

- **Monorepo：** pnpm workspace，包含 `apps/extension` 和 Astro website。
- **扩展：** Manifest V3、TypeScript、Vite、CRXJS、service worker、content scripts、options page、`activeTab`／`storage` 权限，以及 `<all_urls>` host／content-script access。
- **Provider SDK：** OpenAI、Anthropic SDK 和 Google GenAI SDK，provider registry 包含 OpenAI、OpenAI-compatible、Anthropic、Anthropic-compatible 和 Google。
- **本地端点：** 文档示例覆盖 LM Studio、Ollama、llama.cpp server、omlx 和 generic compatible endpoints。
- **质量／安全自动化：** CI 跑 type check、lint、tests、build、extension packaging、release-readiness checks；CodeQL 对 JavaScript／TypeScript 跑 `security-extended` 分析。

## 依赖

- **运行时：** Chrome stable 或支持 Manifest V3 的 Chromium 系浏览器。
- **Provider 凭据／端点：** 原始 provider API key，或在兼容本地端点支持时使用空 key。
- **本地模型服务：** 如果要本地翻译，需要 LM Studio、Ollama、llama.cpp server、omlx，或另一个 OpenAI／Anthropic-compatible endpoint。
- **浏览器 profile 信任：** API key 和翻译缓存存在浏览器 profile 里；请把这个 profile 当成可信边界。
- **构建：** pnpm 10.x、TypeScript、Vite／CRXJS、Vitest 和扩展打包脚本。

## 运维难度

**技术个人低，受策略控制的使用中等。** 安装 Chrome 扩展并指向 API endpoint 很容易。困难在本地／provider 边界：你要运行并保护模型服务，保持 endpoint URL 兼容，选择 persistent 或 session cache，并接受浏览器扩展存储不是保险柜。对团队来说，推荐形态是受控 OpenAI-compatible 网关，加一条写清哪些网站可翻译的规则。

## 健康度与可持续性

- **维护（2026-07）。** 观察到的最新 release 是 2026-06-15 的 v0.3.7，且有 CI、release 和 CodeQL workflow；对一个很年轻的仓库来说，维护卫生不错。
- **治理 / bus factor。** Organization-owned，但公开贡献计数由一名贡献者主导；bus factor 实际仍低。
- **年龄与 Lindy。** 创建于 2026-05，几乎没有 Lindy 证据。请把它当成有潜力的早期项目，不是已证明的长期依赖。
- **采用度。** 检查快照里约 27 star、4 fork：和 Read Frog 或 FluentRead 相比，采用度非常小。
- **风险标记。** 早期 MVP、Chrome／Chromium 优先、宽泛 `<all_urls>` host access、API key 在扩展存储中，以及 provider 侧日志风险，是关键顾虑。

## 存疑（未验证）

- [未验证] Chrome Web Store 详情、安装数、审核状态和当前发布版本未独立检查。
- [未验证] 未运行扩展；provider 支持基于 README 加 provider registry／默认设置路径。
- [未验证] 无默认 telemetry 没有通过全源码审计证明；该结论来自 README、principles 和 threat model 的声明。
- [未验证] Release artifacts 没有检查是否可从源码 reproducible build。
- [推断] Bus factor 风险来自公开贡献分布；组织内部私有团队结构未验证。
- [未验证] YouTube caption／字幕支持在 README 与 changelog／beta docs 之间不一致，未测试前不要依赖。
