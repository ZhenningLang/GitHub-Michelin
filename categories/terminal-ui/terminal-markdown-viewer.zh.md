---
name: Terminal Markdown Viewer (mdv)
slug: terminal-markdown-viewer
repo: https://github.com/axiros/terminal_markdown_viewer
category: terminal-ui
tags: [markdown, terminal, cli, viewer, syntax-highlighting, python, ansi]
language: Python
license: BSD-3-Clause
maturity: v0.x, low-activity (2026-06)
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2024-05-15T12:23:58Z
  default_branch: master
  default_branch_sha: 33d0cf3a1f9acac0c23d9382492ed2ab44fb8833
  archived: false
health:
  schema: 1
  computed_at: 2026-09-19T08:55:24Z
  overall: "?"
  overall_score: null
  scored_axes: 2
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1001
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
        repo_age_days: 4009
        last_commit_age_days: 1001
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_traffic }
    adoption: { reason: ambiguous }
    governance: { reason: unattributable }
    risk_license: { reason: license_unparsed }
---

# Terminal Markdown Viewer (mdv)

一个 Python CLI（`mdv`），把 Markdown 渲染成带样式、彩色、适合终端阅读的文本——表格、带语法高亮的代码块、提示框和主题——让你在纯终端里读 `.md` 文件。

![terminal-markdown-viewer — 健康度雷达](../../assets/health/terminal-markdown-viewer.zh.svg)

## 何时使用

你在通过 SSH 操作一台无界面机器，或常驻在某个 tmux 分屏里，想要真正*读*一份 README 或文档 `.md`，而不是看一墙原始的 `#`、`*` 和反引号。链路里没有（也不想要）浏览器或 GUI Markdown 应用。你运行 `mdv README.md`，文档就被渲染出来：标题、颜色、缩进/带框的代码块、语法高亮片段、表格和列表，按你喜好套主题——全是终端里的 ANSI。它也能从 stdin 读 Markdown，所以你可以把文档或生成的 Markdown 直接管道喂给它，当成 pager 式查看器用。

当任务正是*一次性、只读地把 Markdown 渲染到终端*时你会选它：预览一个文件、瞄一眼 changelog、在 CI 日志里看生成的文档，或在脚本里把它接成“把这段 markdown 漂亮地显示出来”那一步。它是个聚焦的查看器/格式化器，不是编辑器，也不是 TUI 应用。

## 何时不用

- **你想要一个活跃维护、迭代快的工具。** mdv 活跃度低（最后 push 于 2024-05）且停在 0.x 版本；对长期依赖来说，维护更活跃的渲染器（glow、`rich` 的 Markdown、`bat`）可能更稳。[推断]
- **你想要可滚动的 pager / 交互式浏览器。** mdv 是渲染成一段流；如果你要终端内分页、搜索和文件导航，glow 的 TUI 模式或“渲染器 + `less -R`”更合适。
- **你已经在一个 Python 应用里、只需要 Markdown→ANSI。** `rich` 把 Markdown 渲染作为更大样式库的一部分，而你可能本就依赖它——少一个独立工具。
- **你需要忠实、严格符合规范的 CommonMark/GFM 渲染。** 终端渲染器是近似的；复杂的嵌套 Markdown、Markdown 里的 HTML、冷门扩展可能渲染不完美——请对照你的实际文档核实。[未验证]
- **你需要 Windows 优先支持或完全不要 Python。** 它是 Python 工具；若环境在意，单二进制的 Go 渲染器（glow）能省掉 Python 运行时。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| glow | 未收录 | 需要 Go 单二进制 Markdown 渲染器，并带 TUI 浏览器/pager 和主题时，选 glow。 | Go 单二进制 Markdown 渲染器，带 TUI 浏览器/pager 和主题（Charm）；维护活跃、无 Python 运行时——通常是终端读 Markdown 的现代默认选择。 |
| bat | 未收录 | 需要带语法高亮和分页的 `cat` 替代品时，选 bat。 | 带语法高亮和分页的 `cat` 替代；显示的是高亮后的 Markdown *源码*而非渲染结果，但无处不在且快。 |
| [rich（Markdown）](rich.zh.md) | ✅ | Markdown 渲染只是更大 Python 终端样式输出工具集的一部分时，选 rich。 | Python 库，作为更大工具集的一部分把 Markdown 渲染成带样式的终端输出；库优先，不是独立 CLI。 |
| mdcat | 未收录 | 需要 Rust CLI 把 Markdown 渲染到终端，且支持终端内联图片时，选 mdcat。 | Rust CLI，把 Markdown 渲染到终端，在支持的终端上还能内联显示图片；单二进制、活跃。 |
| pandoc + pager | 未收录 | 需要跨多种格式的重量级通用转换时，选 pandoc + pager。 | 把 Markdown 转成多种格式（重量级、通用）；对“只想在终端里看这份 .md”来说是杀鸡用牛刀。 |

## 技术栈

- **语言：** Python（CLI 入口 `mdv`）；通过 `setup.py`/`setup.cfg` 打包，可从 PyPI 安装。
- **渲染：** 解析 Markdown 并输出 ANSI 样式文本——标题、主题色、带框/缩进代码、语法高亮、表格、列表和提示框。
- **输入：** 文件参数或 stdin；可选主题和配置项。
- **打包：** 仓库带 `Dockerfile`，在 pip 安装之外提供容器化运行路径。

## 依赖

- **运行时：** Python 加少量 pip 依赖（Markdown 解析、语法高亮如 Pygments、终端样式）；确切清单见打包元数据。
- **终端：** 一个支持 ANSI 的终端用于彩色/样式输出。
- **无外部服务或数据存储**——它是读文件/stdin、写终端的本地 CLI。

## 运维难度

**低。** 它是单一用途 CLI：`pip install`（或跑 Docker 镜像）后执行 `mdv file.md`。没有要部署的东西，无服务、无状态。唯一摩擦在环境层面——把 Python 版本/依赖弄对，并接受复杂 Markdown 的终端渲染是近似的，因此你可能要调主题或在边角情况下回退到看源码。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 最后 push 于 2024-05；提交稀疏，版本停在 0.x 线。读作**低活跃 / 吃老本**——能用但非活跃开发。未归档。[推断]
- **治理 / 背书。** 归 Axiros 组织（一家公司）所有，外加一小撮贡献者尾巴。组织归属比个人账号略好，但这里的活信号是活跃度而非归属。[推断]
- **年龄与 Lindy 判断。** 约 11 年（2015-07 创建）；存活久但近期活动单薄，所以 Lindy **参半**——够老够稳，但仅凭年龄抵不过缓慢节奏（要用年龄 × 仍活跃一起看）。[推断]
- **采用度。** 约 1.9k star；终端 Markdown 这一小众里一个为人知的老牌项目，如今与更新的 Go/Rust 渲染器（glow、mdcat）竞争。[未验证]
- **风险标记。** 维护速度低是主要一项。许可为 BSD-3-Clause（读自仓库的 LICENSE.txt；GitHub 报 `NOASSERTION`）。未发现 relicense 历史。[未验证]

## 存疑（未验证）

- [未验证] GitHub API 把许可报为 `NOASSERTION`；仓库的 `LICENSE.txt` 是 BSD 三句版许可（Axiros GmbH）。这里按读文件记为 BSD-3-Clause，而非依据 API 徽章。
- [未验证] 截至 2026-06 约 1.9k star、2024-05 最后 push；star 数和活动日期会漂移，仅供参考。
- [未验证] 确切的 Python 最低版本和精确的运行时依赖清单由打包元数据决定且随时间变化，这里不断言具体数值。
- [推断] “低活跃 / 吃老本”是从 2024-05 最后 push 和稀疏提交推断，而非实测的发布频率数字。
- [未验证] 复杂/嵌套 Markdown（Markdown 里的 HTML、冷门扩展）的还原度是终端渲染器固有的局限，而非针对本工具实测的缺陷清单。
