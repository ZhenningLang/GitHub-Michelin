---
name: JianYing Editor Skill
slug: jianying-editor-skill
repo: https://github.com/luoluoluo22/jianying-editor-skill
category: nle-automation
tags: [agent-skill, jianying, capcut, video-editing, nle, python, automation]
language: Python
license: MIT
maturity: VERSION 1.7.0 in-repo (no tagged releases), 3,366 stars, 456 forks, created 2026-01-24, last push 2026-09-11 (as of 2026-09)
last_verified: 2026-09-21
type: skill-pack
upstream:
  pushed_at: 2026-09-11T09:36:48Z
  default_branch: main
  default_branch_sha: 32c56928ded4f9e2c2b80e099dc7abb793d2c30b
  archived: false
health:
  schema: 1
  computed_at: 2026-09-21T04:28:16Z
  overall: C
  overall_score: 2.0
  scored_axes: 3
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 10
        active_weeks_13: 3
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 240
        last_commit_age_days: 10
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.981
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: type_na }
    adoption: { reason: no_package_structural }
    risk_license: { reason: license_unparsed }
---

# JianYing Editor Skill

一个 agent skill：一句话就能变成一份真实的剪映专业版草稿——素材、AI 配音、字幕、配乐和特效铺在轨道上——在 Windows 加剪映 5.9 或更早版本上，它还能替你点导出。

![JianYing Editor Skill — 健康度雷达](../../../assets/health/jianying-editor-skill.zh.svg)

## 何时使用

你用剪映专业版剪中文短视频，慢的不是创作判断，而是组装：把当天素材逐条丢上时间轴、把旁白拆成一句句字幕、对齐配音、从剪映曲库里翻出合适的音乐、按名字套一个转场。你希望这些组装工作交给 coding agent，而判断仍由你自己在剪映里做。

你把 skill 装进 Claude Code／Cursor／Trae，用自然语言说清要什么（「把 D:\素材 剪成 Vlog，配轻快 BGM」），agent 就在你的项目里写一个 Python 脚本把草稿搭出来，你打开剪映渲染导出。相对 [pyJianYingDraft](pyjianyingdraft.zh.md) 的决定性取舍是：后者是许可宽松、由你编程调用的库，有发版历史、不带任何既定套路；这个是打包好的 agent 层——agent 读的规则文件，加上现成的工作流：TTS 配音与字幕对齐、云端素材检索、带智能变焦的录屏、影视解说生成——代价是它属于个人项目、与版本强耦合、且没有 tagged release。相对 [Jianying Headless](jianying-headless.zh.md)，你放弃了 macOS 与较新版本上的应用原生无头导出，换来的是两个库都没有的「从文案到带字幕时间轴」这类高层工作流。

## 怎么用起来

这个 skill 是一摞 Markdown 规则加 Python 脚本，不是一个应用。你提出剪辑需求后，agent 把请求路由到对应的 `rules/*.md`，然后在**你的项目根目录**写一个业务脚本（skill 明确禁止把剪辑脚本放进它自己的目录），脚本通过一段路径探测代码引导，从 `scripts/jy_wrapper.py` 导入 `JyProject`。接下来就是一套正常的创作 API：按正确分辨率创建工程，添加带时间区间的视频／音频／文字片段，生成 TTS 与对齐好的字幕，检索并应用特效，最后调用 `project.save()`，把草稿写进剪映的草稿目录并刷新磁盘上的草稿状态。Python 侧不做任何渲染——像素始终由剪映产出——playbook 里的验收清单查的是草稿结构（存在视频轨、BGM 在音频轨上、旁白有对齐的字幕片段），而不是成片质量。第二套机制是可选的、且与平台绑定：无人值守导出靠 `uiautomation` 驱动应用自己的界面，所以 README 把它限定在 Windows 加剪映 5.9 或更早版本，并把 macOS 当作「生成草稿后手工导出」。

![jianying-editor-skill — 主干用户故事](../../../assets/flow/jianying-editor-skill.zh.svg)

<!-- flow-steps:begin (generated from flows/jianying-editor-skill.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：把仓库放进 AI 编辑器的 skills 目录 — `.claude/skills/jianying-editor`
2. **你**：用自然语言说清要什么——素材、旁白、字幕、配乐 — `帮我随便剪一个视频看看效果`
3. **JianYing Editor Skill**：在你项目根目录写一个 Python 脚本，导入那个封装 — `from jy_wrapper import JyProject`
4. **JianYing Editor Skill**：把素材、配音、字幕、配乐铺到轨道上，存成真实剪映草稿 — `project.save()`
5. **你**：打开剪映专业版，检查时间轴并在剪映里导出

**价值**：一句话换来一条搭好的多轨剪映时间轴，字幕和配音已经对齐

</details>
<!-- flow-steps:end -->

## 何时不用

- **你用 CapCut 国际版，或用手机端剪映。** 它只面向桌面版剪映专业版（JianyingPro），README 明确说别拿这套流程去试国际版。改用至少记录过 CapCut 变体的 [pyJianYingDraft](pyjianyingdraft.zh.md)，或者手工剪。
- **你需要不经人手就产出成片。** 在 macOS 上它只生成草稿；Windows 上的自动导出是 UI 自动化、针对剪映 5.9 或更早，应用控件一变就会失效。无人值守管线请用 [FFmpeg](../video-audio/ffmpeg.zh.md) 或 [MoviePy](../video-audio/moviepy.zh.md) 渲染，macOS 上则用 [Jianying Headless](jianying-headless.zh.md)（非商用许可）。
- **你需要剪映的实时 GPU 能力——智能抠图、美颜、语音识别字幕、一键成片。** README 把这些列为做不到，因为它们不由草稿文件驱动。
- **你想要一个可以锁版本、可以长期维护的依赖。** 它没有 tagged release 可锁（仓库里只有一个 `VERSION` 文件写着 1.7.0），项目约 8 个月历史，而且几乎全部由一位作者完成。任何必须长期存活的东西，底下请垫 [pyJianYingDraft](pyjianyingdraft.zh.md)（Apache-2.0、有发版、跨平台）。
- **你需要在隔离环境或无人值守的机器上跑它，或者手上的素材涉密。** 它安装桌面控制类依赖（`uiautomation`、`pynput`、`playwright`），录屏与导出时会接管屏幕；配音来自 `edge-tts`，文本会发往微软的云服务。请把它放在专用机器或虚拟机上、用可丢弃的数据，而不是放在还存着别的工作成果的主力机上。
- **你正准备照 README 在 Windows 上执行 `irm is.gd/rpb65M | iex`。** 不要把短链管道进 PowerShell：文档冻结之后链接指向的内容仍可能改变，而执行前你没有任何东西可审。请克隆仓库并自己读脚本。
- **你不想让 agent 动创意工程自己的源码树。** 这套流程是故意把生成的 `.py` 脚本写进你当前工作项目的根目录；如果那棵树正在评审或受版本控制，请把它指向一个临时目录。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Jianying Headless](jianying-headless.zh.md) | ✅ | 当成片必须在 macOS 上由剪映自己的引擎不经人手地产出时选 Jianying Headless；当任务是「把一段需求变成带字幕、带配音的时间轴」且你接受手工导出时选本 skill，因为两者解决的是同一条链的不同半段，而 Headless 绑定单个应用版本、且是非商用许可。 | 本 skill 带的是更高层的工作流（TTS、字幕对齐、特效检索、录屏），但 macOS 上没有无人值守导出；Jianying Headless 给原生导出，代价是只支持 macOS、只支持单一版本、且非商用。 |
| [pyJianYingDraft](pyjianyingdraft.zh.md) | ✅ | 当你 code-first、想要 Apache-2.0 且有发版的库来构建时选 pyJianYingDraft；当你要让 coding agent 驱动整个需求、且希望 TTS、字幕对齐、特效名检索都已经规定好时选本 skill，因为 pyJianYingDraft 把这些决策统统留给你的代码。 | pyJianYingDraft 是稳定、不带观点的库；本 skill 是有观点的 agent playbook，但没有发版、只有一位维护者。 |
| [Auto-Editor](../video-audio/auto-editor.zh.md) | ✅ | 需求只是「剪掉冷场、给我一条时间线」时选 Auto-Editor；当时间轴里还要在剪映内组装配音、字幕、配乐和具名特效时选本 skill，因为 Auto-Editor 从不产出剪映工程。 | Auto-Editor 是六年历史、单一二进制、导出可被 NLE 导入的剪切结果；本 skill 面向某一个编辑器的草稿格式和某一套生态，背后的长寿性差得远。 |
| 剪映专业版／CapCut（闭源应用） | 未收录 | 一次性、以后也不再重做的剪辑就用应用本身；当同一套结构要反复按需求生成时选本 skill，因为应用没有可脚本化的创作接口。 | 应用给的是厂商级打磨、全部特效和免费可用的实时 GPU 能力；这个 skill 自动化的是组装，调不动那些实时能力，且应用的格式或界面一变就可能失效。 |

## 健康度与可持续性

- **维护（2026-09-21）：** 仓库建于 2026-01-24，最后 push 是 2026-09-11——活跃，仓库内有 `VERSION` 写着 1.7.0 并有 CHANGELOG，但**没有 tagged release**，因此没有可锁定、可比对的版本化产物。
- **治理／巴士系数：** 一位作者（`luoluoluo22`，114 次贡献）加两位各 1 次提交的贡献者；个人账号，背后没有组织、基金会或资金。对一个替别人做生产工作的工具来说，巴士系数为 1 [推断]。
- **背书与长青度：** 约 8 个月历史、3,366 star、456 fork，另有营销页面（netlify FAQ、B 站介绍），作者围绕它积累了视频观众。年轻且单一作者——这是本页画像里最弱的一环，也是它只适合放进「丢了也不心疼」的管线的原因 [推断]。
- **采用与生态：** 8 个月 3.4k star，中文教程面活跃（使用指南、agent playbook、最小命令 SOP，以及 Vlog／文案转视频／录屏／影视解说等示例）；16 个 watcher、4 个 open issue，说明受众偏使用者而非贡献者。
- **风险标记：** 自动化面就是风险面——草稿格式耦合，加上针对某个固定旧版剪映的 Windows UI 自动化，两者都会因应用更新而失效；`requirements.txt` 钉住了需要屏幕权限的桌面控制包（`uiautomation==2.0.20`、`pynput`、`playwright`）；TTS 文本经 `edge-tts` 离开本机；README 推荐的 Windows 安装方式是一条短链 `iex` 管道。

## 存疑（未验证）

- [未验证] 本页没有任何一项被实际执行：草稿输出、TTS、字幕对齐与导出路径均读自 README、`SKILL.md`、`rules/*.md`、`examples/*.py` 与依赖清单，没有对着剪映跑过。
- [未验证] 平台矩阵（Windows 全支持、含剪映 5.9 及以下的自动导出；macOS 只生成草稿；不支持 CapCut 国际版；不支持手机端）是作者自报且与版本绑定；要验证需要在两种操作系统上具备对应的剪映版本。
- [未验证] 「`uiautomation` 导出在剪映 5.9 及以下最稳」这条在没有 Windows 主机与那个版本编辑器的情况下无法复现；仓库目录树里也没有找到相应的 CI 或测试证据。
- [未验证] 对那条 PowerShell 单行命令的安全判断只基于它的形态（`irm <短链> | iex`）：`is.gd/rpb65M` 指向的内容没有抓取也没有审阅。
- [未验证] `edge-tts` 具体发送什么、发往哪个端点、适用什么条款均未调研；观察到的只有钉住的依赖版本和 README 对微软音色的描述。
- [推断] Apache-2.0 与 MIT 的疑问按 MIT 处理：GitHub API 报 `NOASSERTION`，但 `LICENSE` 文件是 MIT 全文、署名 `Copyright (c) 2026 luoluoluo22`；`NOASSERTION` 视为分类器失败。
- [推断] 与版本耦合意味着剪映一次发版就可能打断原本可用的流程，直到作者重新适配——README 自己写的「剪映 5.9 及以下最稳」「新版本可能受弹窗或控件变化影响」正是这个模式的实例。
- [推断] 巴士系数与 Lindy 的判断来自观察到的贡献者数量、仓库年龄与没有 tagged release 这几点；没有发现资金、赞助或组织背书。
- [未验证] README 里链接的 netlify FAQ 与 B 站介绍未阅读；它们超出仓库自身文档的任何说法，本页都没有覆盖。
