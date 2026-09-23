---
name: captcha (lepture)
slug: lepture-captcha
repo: https://github.com/lepture/captcha
category: captcha
tags: [captcha, image-captcha, audio-captcha, pillow, python, accessibility]
language: Python
license: BSD-3-Clause
maturity: v0.7.1, low-volume but maintained, ~1.1k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2025-10-21T06:24:16Z
  default_branch: main
  default_branch_sha: 087b30be72640802fddc097472ef35a88020387a
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:01:13Z
  overall: B
  overall_score: 2.6
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 336
        active_weeks_13: 0
        carve_out: mature_library_lindy
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: captcha
        dependent_repos_count: 506
        downloads_last_month: 313940
        graph_tier: C
        volume_tier: B
        cross_check_divergence: null
        release_downloads: 33213
        release_assets: 4
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 4319
        last_commit_age_days: 336
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: BSD-3-Clause
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
---

# captcha (lepture)

一个小巧的 Python 库，把你给定的字符串渲染成扭曲的图片验证码，或合成语音验证码——挑战文本、存储和校验都归你管，它只负责画图和发声。

![lepture-captcha — 健康度雷达](../../assets/health/lepture-captcha.zh.svg)

## 何时使用

你在做一个 Django 或 Flask 表单——注册页、评论框、密码重置流程——想要一个自托管、不调第三方的验证码，挡住机器人猛刷端点。你不想接 reCAPTCHA（会把用户数据送给 Google，还需要一次网络往返），也不想专门起一个服务；你只想在服务端生成一个随机的 4 到 6 位字符串，渲染成带噪点的 PNG，把答案存进 session，提交时比对用户输入。你 `pip install captcha`，调 `ImageCaptcha().generate('A3K9')`，把图片字节交给模板，提交时做相等比较。为视障用户，你再调 `AudioCaptcha().generate(...)`，用同一串码生成读数字的 WAV。它只依赖 Pillow，因此能塞进任何 Python web 栈而无需额外基础设施。

你选它，正是因为想在自己的进程里完全掌控挑战的生命周期——这个库刻意只做*渲染器*。文本生成、与 session/存储的绑定、过期、相等校验都得你自己写，而这恰好是你在规避任何外部验证码依赖时想要的。

## 何时不用

- **你需要对抗现代破解器的真正机器人防护。** 扭曲文字图片验证码会被廉价 OCR 和商业打码服务攻破；本库不声称对抗鲁棒性，也确实没有。要认真防滥用，请用工作量证明 / 行为式挑战（如 [Cap](capjs.zh.md)）或托管反爬服务。[推断]
- **你想要内置校验的开箱即用验证码。** 这只是渲染器——没有挑战存储、没有过期、没有 verify 端点。若你想要「丢进去就能用」，框架插件（django-simple-captcha）或托管控件更合适。
- **以可访问性或国际化为先的挑战。** 语音是用内置语音数据念数字/字符，并非完整的无障碍验证码方案，且内置的语音/字体数据本就是让你替换成自己的。
- **热路径上的高请求量。** 每张图片/语音都是即时渲染（Pillow 栅格化、语音合成）；高流量下你会想要缓存或预生成池，而不是逐请求生成。
- **你以为它会维护状态。** 它只产出字节，别无其他；忘记在服务端绑定并设过期，是最常见的安全失误。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Cap](capjs.zh.md) | ✅ | 需要面向机器人防护的工作量证明或隐形挑战，而不是文字/图片渲染器时，选 Cap。 | 范式不同：无字可读、JS 优先、保护隐私，也不是 Python 图片/语音验证码生成器。 |
| Google reCAPTCHA / hCaptcha | 未收录 | 更强的托管机器人信号比自托管更重要时，选托管 CAPTCHA 服务。 | 有第三方网络调用、隐私/数据共享顾虑，且不能自托管；但信号强于简单生成式挑战。 |
| django-simple-captcha | 未收录 | 需要与 Django 集成、且自带存储与校验的验证码字段时，选 django-simple-captcha。 | 在 Django 之外灵活性差，也比纯渲染器更重。 |
| Pillow（手搓） | 未收录 | 只需要一小段自己完全掌控的自定义绘图代码时，选裸 Pillow。 | 这个库把同样的文字/噪点渲染思路预先打包，并补上语音支持和合理默认值。 |

## 技术栈

- **语言：** Python（按 `pyproject.toml` 要求 >= 3.9），用 setuptools 打包，带类型标注（`py.typed`）。
- **渲染：** 用 Pillow 做图片栅格化（噪声曲线、点、字体扭曲）；模块分为 `captcha.image` 和 `captcha.audio`。
- **语音：** 由内置的逐字符语音 WAV 数据合成（可用 `voicedir` 替换）。
- **分发：** 以 `captcha` 之名发布在 PyPI。

## 依赖

- **运行时：** 只有 Pillow——这就是图片生成的全部依赖面。
- **字体/语音：** 自带内置字体和语音数据；README 建议自备（`fonts=[...]`、`voicedir=...`），既为质量也为避免可预测的素材。
- **需你自备：** 挑战文本生成、存答案的 session/缓存、过期、校验比对——这些库里都没有。
- **安装：** `pip install captcha`；不需要系统服务或数据存储。

## 运维难度

**低。** 它是只有单一依赖的纯库——除了你自己的应用，没什么要部署或运维的。真正的运维考量都在应用层：缓存或预生成图片，免得逐请求的 Pillow 渲染变成 CPU 热点；以及在服务端把生成的答案正确绑定到 session 并设过期。无数据存储、无服务、无后台进程。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 最后 push 于 2025-10；最新 tag 为 v0.7.1。提交量低但并未死掉——小修复在落、依赖（Pillow）有跟进。**维护中、低速**——对一个稳定、范围窄的库而言恰如其分。[推断]
- **治理 / bus factor。** 单一高产维护者（lepture，也是 Authlib/mistune 作者）的个人项目；贡献者列表由 owner 主导。bus-factor 风险真实存在，但被极小的表面积缓解——这个库与其说「活跃」，不如说「做完了」。[推断]
- **年龄与 Lindy 判断。** 2014-11 创建（约 11 年）且仍偶有更新⇒ 对一个小工具来说是不错的 Lindy 信号；它早已活得比多数验证码库都久。[推断]
- **采用度。** 约 1.1k star、约 189 fork，作为轻量自托管验证码生成器散见于 Python web 项目。规模不大但稳定。[未验证]
- **风险标记。** 决定性的风险**不在维护而在适配性**：文字图片验证码对现代自动破解器很弱，与这个仓库多健康无关。把它当作 UX 减速带，而非安全控制。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 1.1k star / 约 189 fork；星标/fork 数对时间敏感，仅供参考。
- [未验证] 观察到的最新 tag 为 v0.7.1；确切发布日期此处未确认（API 只返回 tag，没有 GitHub Releases 条目）。
- [推断]「被现代 OCR/打码服务攻破」是扭曲文字验证码的普遍状态，而非对该渲染器具体产物的实测结论。
- [推断]「维护中、低速」是从提交近况加单一主导贡献者推断而来，并非来自明确的维护策略声明。
