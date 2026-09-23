---
name: stop-slop
slug: stop-slop
repo: https://github.com/hardikpandya/stop-slop
category: de-ai-writing
tags: [agent-skill, de-ai-writing, stop-slop, skill-pack]
language: Markdown
license: MIT
maturity: active, ~13,905 stars (as of 2026-07)
last_verified: 2026-07-16
type: skill-pack
upstream:
  pushed_at: 2026-03-17T18:50:39Z
  default_branch: main
  default_branch_sha: 8da1f030185bdfe8471220585162991eaeb970e9
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:42:07Z
  overall: B
  overall_score: 2.5
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 189
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "N/A"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 254
        last_commit_age_days: 189
        cohort: skill-pack
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.8
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
  unknowns:
    responsiveness: { reason: type_na }
  not_applicable:
    adoption: { reason: no_install_channel }
---
# stop-slop

A skill file for removing AI tells from prose

![stop-slop — 健康度雷达](../../../../assets/health/stop-slop.zh.svg)

## 何时使用

你需要一个短小、强硬的英文 prose 去机器腔规则，让 agent 从 `SKILL.md` 和 references 里加载，并且你更关心快速清掉常见 AI 痕迹，而不是保留所有正式文体习惯时，选 stop-slop。它适合把短规则塞进审稿流程，而不是做完整写作工作台。

上游文档覆盖 Claude Code skill 文件夹、Claude Projects 上传、custom instructions 复制，以及 API / system prompt 中按需加载 `SKILL.md` 和 `references/` 的用法。

## 何时不用

- **你要清理中文文本。** 用 [Humanizer-zh](humanizer-zh.zh.md) 或 [shuorenhua](shuorenhua.zh.md)；stop-slop 主要面向英文 prose。
- **你需要保留正式文体的细腻度。** “去掉所有副词”“必须主动语态”“不要 em dash”这类强规则可能误伤学术、法律、技术或文学写作。
- **你需要 plugin 形式安装。** 本次只在上游文档中核验到手动 skill / API / custom-instruction 用法，没有找到 Claude plugin marketplace 命令。
- **你想做 voice calibration，而不是强硬去味。** [humanizer](humanizer.zh.md) 的循环更宽、更温和；stop-slop 刻意短且硬。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [humanizer](humanizer.zh.md) | ✅ | 需要更完整的英文上游 skill、false-positive 指南和安装路径时选 humanizer。 | humanizer 更宽、更温和；stop-slop 更短、更严格，也更容易复制进本地指令。 |
| [Humanizer-zh](humanizer-zh.zh.md) | ✅ | 简体中文去 AI 味改写选 Humanizer-zh。 | Humanizer-zh 中文优先，并借鉴了部分 stop-slop 思路；stop-slop 是英文强规则基线。 |
| [shuorenhua](shuorenhua.zh.md) | ✅ | 需要中文场景分流和 protected spans 时选 shuorenhua。 | shuorenhua 处理中文工程 / 产品语境；stop-slop 不覆盖。 |
| 自写编辑清单 | 未收录 | 组织已有明确 style rules 时自写。 | 自写能避开 stop-slop 的泛化硬规则，但需要自己维护。 |


## 健康度与可持续性

- **维护快照（2026-07-16）：** GitHub 返回 `archived=false`，`pushed_at=2026-03-17T18:50:39Z`；health 将维护评为 C。
- **采用快照：** 2026-07 约 13,905 个 GitHub stars；这是关注度，不代表硬规则适合每种文体。
- **许可证快照：** 只读上游核验确认 GitHub metadata、根目录 `LICENSE`、README 和 `SKILL.md` 均为 MIT。
- **Lindy / 治理：** 项目很年轻、维护者集合较小；适合作为短规则清单，但还不是长期标准。
- **风险信号：** 强规则可能过宽，尤其在被动语态、副词或 em dash 本来合理的正式文体中。

## 存疑（未验证）

- [未验证] 本次没有在上游文档中找到 plugin marketplace 安装，只核验到手动 skill / API / custom-instruction 用法。
- [推断] 最强的规则是风格偏好，不是普适质量标准；在非口语英文 prose 中应预期 false positives。
