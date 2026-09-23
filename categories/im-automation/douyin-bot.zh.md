---
name: Douyin-Bot
slug: douyin-bot
repo: https://github.com/wangshub/Douyin-Bot
category: im-automation
tags: [douyin, adb, android-automation, face-recognition, bot, python, demo]
language: Python
license: MIT
maturity: v0.0.1 demo, no commits since 2020-05, ~9.6k stars (as of 2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2023-10-03T21:08:46Z
  default_branch: master
  default_branch_sha: 399c19b662ac4ef08fcb37bb16936add3ae1faa8
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:19:30Z
  overall: D
  overall_score: 1.33
  scored_axes: 3
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 2330
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
        repo_age_days: 3040
        last_commit_age_days: 2330
        cohort: app
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
    adoption: { reason: no_package_structural }
    governance: { reason: unattributable }
---

# Douyin-Bot

一个 2018 年的 Python 玩具/demo，通过 ADB 驱动一部真实 Android 手机自动刷抖音，用云 API 给人脸打分，并自动给“漂亮”的视频点赞。很有名，约 9.6k star——但自 2020 年起实质已死。

![douyin-bot — 健康度雷达](../../assets/health/douyin-bot.zh.svg)

## 何时使用

你是开发者，想要一个具体、可读的*屏幕坐标手机自动化*示例——即如何用 Python 经 ADB 驱动一部真机：`screencap` 截图、压缩、发去某处分析，再根据结果发 `input swipe` / `input tap`。Douyin-Bot 正是这个循环的一个小巧而知名的参考：它截抖音 app 的屏、把帧 POST 给一个云端人脸识别 API、读回一个“颜值”分，分数过阈值就点赞/关注，然后划到下一个视频。

实事求是地说，这是它今天*唯一*站得住脚的用法：当历史性的 ADB 自动化样本来读。作为能用的工具，它不行——见下。别部署它。

## 何时不用

- **它对今天的抖音几乎肯定是坏的。** 这套做法是对 2018 年抖音 UI 的硬编码像素坐标（README 只适配了 OnePlus 5 的 1920×1080，一部 2017 年的手机）。此后抖音改版多次；自 2020-05 起代码无维护。在 2026 年 app 上能否工作未经验证，也不预期能用。[推断]
- **它的云依赖已死。** 人脸打分依赖 `ai.qq.com` 上旧的腾讯 AI 开放 API——一个腾讯此后已重组/下线的平台——用的是作者硬编码（如今已失效）的 AppID/AppKey。没有可用的人脸后端，核心功能就是死的。[推断]
- **它是 demo，不是产品。** `VERSION = "0.0.1"`，零 release、零 tag、无测试、无 CI；“homepage”是一篇知乎专栏文章。它是一篇“看 ADB 能干啥”文章的配套。
- **高搭建成本，换不来能用的东西。** 需要真机、USB、ADB、特定的 2017 设备分辨率，换别的屏还要手改坐标 JSON。2018 年钉死的 `requirements.txt`（numpy 1.14、pandas 0.22、Pillow 5.1、scikit-learn 0.19）在现代 Python 上不经编译折腾基本装不上。[推断]
- **ToS / 封号风险。** 自动点赞/关注/评论违反抖音条款；代码里甚至自带一个“随机防 Ban”小手段，等于承认了封号风险。
- **设计上即物化的框架。** 它自陈的目的是按“颜值”给女性打分以自动点赞“漂亮小姐姐”，源码里还有个 `GIRL_MIN_AGE = 14` 常量——单这一点就是红旗。不宜推荐或在其上构建。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| Appium | 未收录 | 稳健的移动 UI 自动化和元素选择器更重要时，选 Appium。 | 有人维护的通用移动 UI 自动化框架（Android/iOS），用元素选择器而非硬编码像素——若你真需要稳健的设备自动化，这才是对的工具。 |
| 纯 ADB + 脚本 | 未收录 | 只需要 Douyin-Bot 演示的 screencap/input 底层机制时，选纯 ADB。 | Douyin-Bot 演示的底层机制；若你只想要 screencap + input 事件，原生 `adb` 更透明，也不绑死在一个已死的云 API 上。 |
| airtest / Poco（网易） | 未收录 | 目标是带 IDE 的图像识别式 UI 自动化时，选 airtest 或 Poco。 | 基于图像识别的游戏/app UI 自动化，带 IDE；坐标/图像驱动设备自动化的、有人维护的国内生态替代。 |

## 技术栈

- **语言：** Python（入口 `douyin-bot.py`；`common/` 放 adb、config、screenshot、apiutil、compression 辅助）。
- **驱动：** ADB——用 `adb screencap` 取帧、`adb shell input swipe/tap` 做动作，对着 USB 连接的 Android 手机。
- **人脸/颜值打分：** `ai.qq.com` 上的远程腾讯 AI 人脸 API（不是本地 OpenCV——没有 cv2 依赖）。Pillow 只用于图片缩放。
- **配置：** `config/` 下按分辨率的坐标 JSON（主要为 OnePlus 5 1920×1080；2020 年加了个 720p 配置）。

## 依赖

- **硬性外部依赖：** 装好并在 PATH 里的 ADB，加一部经 USB 连接的真机。ADB **不在** `requirements.txt` 里——是单独安装的。
- **外部服务：** 一个可用的腾讯 AI 人脸 API 账号（AppID/AppKey）——提交进去的密钥是作者的且已失效（见存疑）。
- **Python 库（`requirements.txt`，2018 年钉死）：** matplotlib 2.2、xlrd 1.1、pandas 0.22、numpy 1.14、Pillow 5.1、scikit-learn 0.19——这些 pin 早于当前解释器的 wheel，今天装起来很痛苦（见存疑）。
- **硬件耦合：** 特定的 2017 手机分辨率；其它设备需手改坐标 JSON。

## 运维难度

**对一个大概率不工作的东西来说，中到高。** 没有服务器要跑，但搭建很琐碎：装 ADB、把真机经 USB 连上、装 2018 年的一套 Python 依赖、弄到（已失效的）腾讯 AI 凭据，再把屏幕坐标校准到你的具体设备。这些都弄完后，硬编码坐标对不上当前抖音 UI、云 API 也没了——所以现实结果是“全都搭好了，然后它不工作”。功夫都在设备/凭据/坐标的管线上，回报近乎为零。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 已废弃——最后一次真实代码提交是 2020-05-06；2023-10 的 `pushed_at` 是元数据churn，不是活动。未 archived，但从来没有 release、tag、测试或 CI。**死掉的 demo。**[推断]
- **治理 / bus factor。** bus factor 为 **1**：个人 User 仓库（`wangshub`），4 个贡献者里只有作者是实质性的。一个个人、无维护的 demo 上有约 9.6k star，正是那种典型的“2018 病毒式博文，而非维护”异常——别把它当健康信号。
- **年龄 × Lindy。** 约 8 岁但已死约 6 年——不过 Lindy 测试，后者要求又老**又**仍活。这里的年龄是化石的年龄，不是耐久度。[推断]
- **采用度。** star/fork 反映的是一篇知名的 2018 知乎文章，而非生产使用。65 个 open issue，无人在处理。
- **风险标记。** 已死的云依赖、ToS/封号风险（它自带防 Ban 手段，等于自认）、源码里硬编码的明文凭据，以及带 `GIRL_MIN_AGE = 14` 常量的物化目的。[推断]

## 存疑（未验证）

- [推断] 2023 的 `pushed_at` 与 2020 的最后一次提交之间的落差是仓库元数据churn，不是真实开发。
- [未验证] 该 bot 对 2026 抖音 UI 是否还能工作——需真机 + 当前 app 才能测；强先验是它不能。
- [未验证] `ai.qq.com` 人脸 API 与硬编码密钥的当前状态；二者推定已失效，但本次未确认。
- [推断] 2018 年钉死的 `requirements.txt` 在现代 Python 上基本装不上，是从版本 pin 推断，未实测。
- [未验证] 截至 2026-06 约 9.6k star；star 数对时间敏感，仅供参考。
