---
name: tqdm
slug: tqdm
repo: https://github.com/tqdm/tqdm
category: data-tools
tags: [progress-bar, cli, python, jupyter, iterables, dataframes, ux]
language: Python
license: MPL-2.0 AND MIT
maturity: v4.x, active (2026-06), ~31.2k stars
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-17T08:10:21Z
  default_branch: master
  default_branch_sha: 9aff6090b6fa98c88a2dbff8bd9e2a68d9a99c1b
  archived: false
health:
  schema: 1
  computed_at: 2026-09-19T08:50:34Z
  overall: B
  overall_score: 3.0
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 16
        active_weeks_13: 4
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: tqdm
        dependent_repos_count: 136364
        downloads_last_month: 580186396
        graph_tier: A
        volume_tier: A
        cross_check_divergence: null
    longevity:
      grade: A
      raw:
        repo_age_days: 4048
        last_commit_age_days: 16
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 5
        top1_share: 0.909
        top3_share: 0.955
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_traffic }
    risk_license: { reason: license_unparsed }
---

# tqdm

一个快速、低开销的 Python 进度条库——把任意可迭代对象一裹（`for x in tqdm(iterable):`），就得到一条原地自刷新的进度条，带 ETA、速率和百分比，适用于循环、CLI 管道和 notebook，且几乎零依赖。

![tqdm — 健康度雷达](../../../assets/health/tqdm.zh.svg)

## 何时使用

你是数据工程师，在跑一个通宵批处理——循环遍历几百万条记录，每条都调一次外部 API、清洗一行、再写出去。脚本能跑，但你一启动就完全不知道它是十分钟跑完还是六小时，而每千条 `print(i)` 一次又会把终端刷成一堆噪声。你把循环的可迭代对象用 `tqdm(...)` 一裹——一个 import、一次函数调用、不用重构——立刻就有了一行原地更新的进度：`47%|████▋ | 1.4M/3.0M [02:11<02:29, 10.8kit/s]`，带实时 ETA 和吞吐。你一眼就能看出它是卡住了、在变慢，还是按计划推进，而每次迭代这条进度条几乎不花成本（文档称约 60ns 开销）。

当你想在各处都得到同样的进度反馈又不想改代码时，你也会选它：它会自动识别 Jupyter/IPython（`tqdm.notebook`）、能当 Unix 管道计量器（`cat bigfile | tqdm | wc -l`）、能和 pandas 集成（`tqdm.pandas()` 后用 `df.progress_apply(...)`），还为 async、`concurrent.futures` 和 logging 提供了薄封装。因为它是纯 Python、没有任何必需的第三方依赖，把它塞进任何项目——Lambda、受限容器、notebook——都是一行 `pip install`，没有依赖树要审。

## 何时不用

- **超紧的热点内层循环。** 单次迭代成本很小但不为零；在一个每次只做纳秒级工作、却要跑上十亿次的循环里，哪怕约 60ns 也会累积。改成不那么频繁地更新（`miniters`/`mininterval`），或者裹外层循环而非最内层。
- **你要的是结构化日志或遥测，而非给人看的进度条。** tqdm 是 TTY/notebook 的 UX 控件，不是指标管线。要机器可读的进度、耗时或看板，应当输出结构化日志/指标（再路由到类似 [Telegraf](../ops-infra/telegraf.zh.md) 的东西），别去爬一条进度条。
- **你想要丰富的多面板终端 UI。** tqdm 刻意做得极简。要 spinner、多条并发动画进度条、表格和带样式的输出，`rich.progress` 和 `alive-progress` 提供更花哨的 UI——代价是更重的依赖。
- **必须精确的并发 / 异步进度。** 多进程、异步和多条进度条的场景能用，但很折腾：position 管理、跨进程的锁共享、刷新顺序都是常见的坑。单循环进度很简单，多 worker 的聚合进度则要花心思。
- **非交互式日志（CI、文件、journald）。** 回车回刷会在日志文件里变成成千上万行垃圾。你可以配置它（`file=`、`disable=not sys.stderr.isatty()`），但在那种场景里，朴素的百分比日志往往更简单。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| rich.progress | 未收录 | 已经使用 `rich` 或需要精致多列进度 UI 时，选 rich.progress。 | `rich` 库的一部分——花哨得多（颜色、列、多条进度条、spinner、表格），很适合做精致 CLI；依赖更重、API 面也比 tqdm 的一行裹更大。 |
| alive-progress | 未收录 | 需要单条进度条更有动画、视觉更丰富并带实时 spinner 时，选 alive-progress。 | 单条进度条做得更有动画、视觉更丰富，带实时 spinner；生态和集成集比 tqdm 小（没有同等广度的 pandas/notebook/管道支持）。 |
| progressbar2 | 未收录 | 需要更老牌、可配置的 widget 式进度条库时，选 progressbar2。 | 更老牌、可配置的进度条库；基于 widget 的 API 比 `tqdm(iterable)` 啰嗦，现代采用度更小。 |
| 朴素 logging / `print` | 未收录 | 需要零依赖且机器可解析的输出时，选朴素 logging 或 print。 | 零依赖且天然机器可解析；没有 ETA/速率/原地回刷，交互式用又很吵——文件/CI 场景该选它，给人盯着看的 TTY 场景不该选。 |
| [Telegraf](../ops-infra/telegraf.zh.md) | ✅ | 需要指标采集/路由 agent，而不是给人看的进度条时，选 Telegraf。 | 一个指标采集/路由 agent，不是进度条——完全不同的活；当你需要真正的遥测而非给人看的计量器时才用它。 |

## 技术栈

- **语言：** 纯 Python（无编译扩展），支持广泛的 Python 版本。
- **输出后端：** 终端上基于 TTY/ANSI 回车回刷；为 Jupyter/IPython 提供单独的 `tqdm.notebook`（基于 ipywidgets）渲染器；还有一个 CLI 入口（`python -m tqdm`）可当 Unix 管道计量器用。
- **集成：** pandas（`tqdm.pandas()` → `progress_apply`）、`concurrent.futures`（`tqdm.contrib.concurrent`）、asyncio（`tqdm.asyncio`）、`logging` 重定向，以及 `tqdm.contrib` 辅助函数（`tenumerate`、`tzip`、`tmap`）。

## 依赖

- **运行时：** 无必需依赖——核心进度条只用纯 Python 标准库；`pip install tqdm` 不会拉任何强制的第三方包。
- **可选：** notebook 渲染器需要 `ipywidgets`；可选的 `tqdm.contrib.telegram`/`slack`/`discord` 通知器分别需要 `requests`/`slack-sdk`/`discord.py`；若用 pandas 集成则需要 `pandas`。[未验证]
- **安装路径：** PyPI（`pip`）、conda-forge，也进了不少发行版仓库；因为体积极小，被 vendored 进项目里的情况很常见。

## 运维难度

**极低。** 没有任何东西要部署或运维——它就是个 import 进来的库。唯一真正的摩擦是交互式输出行为：要让进度条在嵌套循环、多进程或非 TTY 环境（CI、重定向文件、某些 notebook 配置）下干净渲染，有时需要调参（`position`、`leave`、`file`、`disable`、`dynamic_ncols`）。95% 的用法就是 `from tqdm import tqdm; for x in tqdm(it):`，到此为止。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 仓库在 2026-06 有 push，且有较新发布（v4.68.3，2026-06-17）——处于**活跃**而非废弃。发布节奏成熟偏慢（API 早已稳定），对一个被如此广泛依赖的库来说这是合适的。[推断]
- **治理 / bus factor。** 由 `tqdm` **组织**（而非个人账号）拥有，生命周期里有广泛的贡献者基础；历史上与一位主维护者（Casper da Costa-Luis）关联，因此核心知识的集中度是个轻度 bus-factor 考量，但组织所有权和众多贡献者在一定程度上抵消了它。[推断]
- **年龄与 Lindy 判断。** 2015-06 创建，约 11 年且**仍在活跃发布**⇒ **强 Lindy** 信号——一个稳定、无处不在的基础件，而非被炒作的新秀；裹可迭代对象的 API 多年保持向后兼容。[推断]
- **采用度与生态。** 采用极广——约 31.2k star，依赖足迹巨大（它是 Python 数据/ML 生态相当大一部分的传递依赖）；文档详尽，集成面（pandas/notebook/CLI/async）很宽。[未验证]
- **许可 / 风险标记。** 混合 MIT + MPL-2.0：MIT（原始及其他贡献）加 MPL-2.0（维护者的贡献）——因文件级混合许可，GitHub 报为 NOASSERTION。MPL-2.0 带有文件级 copyleft 义务——作为普通依赖正常使用风险较低，但修改/再分发受 MPL 覆盖的文件则有义务。未发现 relicense 历史或 open-core 收口。[推断]

## 存疑（未验证）

- [未验证] 约 31.2k GitHub star 和“60ns 开销”是项目自己的 / 时间点上的表述——star 数对时间敏感，开销数字依赖基准，二者都仅供参考。
- [未验证] 最新发布 v4.68.3 按 GitHub 标注为 2026-06-17；确切补丁版本和日期随版本变动。
- [未验证] 支持的 Python 版本集合随发布变化——请查当前 `setup.cfg`/`pyproject` 的 classifiers，别凭假设。
- [推断] 许可是仓库 LICENCE 文件中描述的 MPL-2.0 + MIT 混合模型；这里概括为 `MPL-2.0 AND MIT`，GitHub 报为 NOASSERTION——若许可条款对你是承重项，请对照该文件确认。
- [推断] 可选依赖清单（ipywidgets、通知器 SDK、pandas）是从文档化的功能推断而来；确切的 extras 和版本固定由当前打包元数据决定。
- [推断] “强 Lindy”和“活跃”是从年龄 × 近期 push/发布得出的判断，并非对未来维护的保证。
