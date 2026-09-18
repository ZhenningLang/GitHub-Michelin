---
name: XlsxWriter
slug: xlsxwriter
repo: https://github.com/jmcnamara/XlsxWriter
homepage: https://xlsxwriter.readthedocs.io
category: office-automation
tags: [xlsx, excel, spreadsheet, python, library, charts, document-generation, office, zero-dependency]
language: Python
license: BSD-2-Clause
maturity: "v3.2.9 (PyPI 2025-09-16), active (last push 2026-08-04); 4.0k stars / 671 forks / 30 open issues, created 2013-01-04 (API-verified), ~13.7-year-old repo"
last_verified: 2026-09-18
type: library
upstream:
  pushed_at: 2026-08-04T23:41:16Z
  default_branch: main
  default_branch_sha: 5d4606d89a955226d2d0825a0f44309043ae7251
  archived: false
health:
  schema: 1
  computed_at: 2026-09-18T12:28:25Z
  overall: B
  overall_score: 3.17
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 45
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 0.6
        qualifying_issues: 4
        band: default
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: xlsxwriter
        dependent_repos_count: 3828
        downloads_last_month: 87471871
        graph_tier: B
        volume_tier: A
        cross_check_divergence: null
    longevity:
      grade: A
      raw:
        repo_age_days: 5005
        last_commit_age_days: 45
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.875
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: BSD-2-Clause
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# XlsxWriter

零依赖的 Python 模块，用于**写入** Excel `.xlsx` 文件——13 年以上历史、生产级稳定，且按设计只写：它无法读取或修改不是它自己创建的工作簿。

![XlsxWriter — 健康度雷达](../../assets/health/xlsxwriter.zh.svg)

## 何时使用

你在一个 Python 服务里从数据生成电子表格——一个财务模型、一份报表导出、一大批带格式的行——而且文件是从零创建而非编辑已有的。你选 XlsxWriter，因为它是做这件事**最轻、最快**的方式：`setup.py` 完全没有声明 `install_requires`，README 写明它 "uses standard libraries only"（2026-09-18 验证），支持 Python 3.8+ 和 PyPy3，带 `Development Status :: 5 - Production/Stable` 分类器，而且在 3,972 个 star 的体量下只有 **30 个 open issue**——一个分诊得异常干净的积压。它覆盖完整格式化、合并单元格、定义名称、图表、自动筛选、数据验证、条件格式、图片（PNG／JPEG／GIF／BMP／WMF／EMF）、富文本多格式字符串、单元格批注、文本框、VBA 宏插入，以及大文件的内存优化模式，外加一流的 Pandas 和 Polars 集成。相对 [OfficeCLI](officecli.zh.md)，你用「单二进制和面向 agent 的 CLI」换来了「一个能锁版本、能写单测、无网络外联的库」；相对 [python-pptx](python-pptx.zh.md)，它是那个仍在积极维护的同胞（python-pptx 自己就依赖 `XlsxWriter>=0.5.7` 来做图表工作簿）。当任务就是「数据 → 新 .xlsx」且仅此而已时，选它。

## 何时不用

- **你需要读取或修改已有工作簿** → XlsxWriter 是只写的，无法打开文件。读写已有 `.xlsx` 请用 openpyxl（`未收录`——原因见「存疑」），消费方是 agent 而非脚本时请用 [OfficeCLI](officecli.zh.md)。
- **消费方是 LLM agent，不是你的代码** → 用 [OfficeCLI](officecli.zh.md)。agent 没法 `import xlsxwriter`；它需要 CLI 或 MCP 接口。XlsxWriter 适合放在**你为 agent 构建的工具内部**，不适合当 agent 的接口。
- **你需要 `.xls`（Excel 97-2003）、CSV 或 ODS 输出** → XlsxWriter 只写 Excel 2007+ 的 `.xlsx`。其他目标格式用 [Pandoc](../markdown-tools/pandoc.zh.md) 或转换器，分隔符文本直接用标准库的 `csv`。
- **公式结果必须缓存在文件里** → XlsxWriter 会写公式但不会计算公式；除非你通过 `write_formula(..., value=)` 提供结果，否则它存的缓存值是 `0`。任何信任缓存而不重算的消费方——尤其是 `data_only=True` 的 openpyxl，以及大多数 headless 读取器——都会看到零。如果你的读取方不会重算，请在写入前自己算好值。
- **数据透视表、切片器或 Power Query** → 不在范围内；它的特性面是图表、格式化和数据。用 [OfficeCLI](officecli.zh.md)，它对多字段分组、计算字段和切片器的数据透视表都有文档。
- **你既要它零依赖、又要它能读文件** → 这两个要求在这里冲突。openpyxl 能读但会拖进 `et_xmlfile`；XlsxWriter 无依赖但只写。先决定哪个约束是承重的。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [OfficeCLI](officecli.zh.md) | ✅ | 如果是 Python 服务生成新工作簿、且你要零依赖、可锁版本和 13 年稳定性，选 XlsxWriter；如果 agent 必须通过 CLI 读取、编辑或创建表格，或你需要数据透视表和切片器，选 OfficeCLI。 | XlsxWriter 只写、没有 agent 接口、没有公开的公式求值；OfficeCLI 能读能改能建并求值（宣称 350+ 函数），但它是 6 个月的单人二进制、无公开测试套件、默认开启自动更新。 |
| openpyxl | 未收录 | 当你必须**读取或修改已有** `.xlsx` 时选 openpyxl——那正是 XlsxWriter 完全做不到的事；当你从零创建文件、且要速度和零依赖时选 XlsxWriter。未收录的原因是它的规范仓库在 Heptapod（Mercurial）而非 GitHub，而本索引的健康度／上游快照工具只支持 GitHub——这是一个已知缺口，不是对它的负面判断。 | openpyxl 用「更慢的写入加一个额外依赖」换来读写能力和公式缓存访问；XlsxWriter 用「无法打开文件」换来速度和零依赖。 |
| [python-pptx](python-pptx.zh.md) | ✅ | 二者不是替代关系而是真实耦合：做 deck 选 python-pptx，并接受它会为图表工作簿拖进 XlsxWriter；交付物就是表格本身时单独选 XlsxWriter。 | python-pptx 自 2024-08-07 起在滑行，而 XlsxWriter 于 2025-09-16 发了 v3.2.9、2026-08-04 还在推——同一个生态，维护状态差别很大。 |
| [MarkItDown](../document-parsing/markitdown.zh.md) | ✅ | 方向是 `.xlsx` → Markdown 供 LLM 摄取时选 MarkItDown；方向是数据 → `.xlsx` 时选 XlsxWriter。两者是管道的两端，从不竞争。 | MarkItDown 只读，且按设计丢弃格式；XlsxWriter 只写，保留完整格式，但读不回任何东西。 |

## 技术栈

纯 Python，`requires-python >=3.8`，支持 PyPy3。**零运行时依赖**——`setup.py` 未声明 `install_requires`（2026-09-18 验证），README 写明 "uses standard libraries only"。打包是经典的 `setup.py` + `setup.cfg`（没有 `pyproject.toml`），版本 3.2.9。直接写 OOXML 的 `SpreadsheetML` ZIP+XML 格式。提供 `constant_memory` 模式，按行顺序写出而不把整个工作簿留在内存里，这是大文件生成背后的机制。附带 `examples/vba_extract.py` 作为安装脚本，用于从启用宏的工作簿里取出 `vbaProject.bin` 以便重新插入。文档在 Read the Docs；默认分支 `main`。

## 依赖

无。Python 3.8+ 及其标准库就是全部要求。不需要 Excel、不需要 LibreOffice、无 C 扩展、无网络访问、无数据库、无 GPU。这是本分类里最强的依赖表现——[python-docx](python-docx.zh.md) 需要 `lxml`，[python-pptx](python-pptx.zh.md) 需要 Pillow + lxml + XlsxWriter，[OfficeCLI](officecli.zh.md) 的 PNG 导出需要外部浏览器。反面是：因为没有任何东西会重算公式，**你自己的代码就成了依赖**——凡是想在文件里缓存计算值都得靠它。

## 运维难度

**低——本分类里最低。** `pip install XlsxWriter`，无服务、无配置、无状态、无外联。约 4k star 只有 30 个 open issue，意味着你可能踩到坑的面积很小且文档充分。运维上需要提前规划两件事：（1）公式缓存——提前决定好是否在 Python 里算出值再传给 `write_formula(..., value=)`，否则下游 headless 读取方会看到 `0`；（2）超大工作簿的内存曲线——打开 `constant_memory` 模式，代价是行必须按顺序写且不能回头改。两者都不是部署负担，而是写代码之前必须做的设计决策。

## 健康度与可持续性

- **维护：活跃且稳定，已验证** —— v3.2.9 发布于 2025-09-16；最后 push 2026-08-04；默认分支 1,492 个 commit（API 2026-09-18 验证）。发版节奏克制而非狂躁，这对一个稳定库是合适的。
- **治理：单人作者，耐力已被证明** —— `jmcnamara`（John McNamara）提交了 1,492 个 commit 中的 1,392 个（**93.3%**）；共 50 位贡献者，第二名 14 个。无基金会或企业背书。[推断] bus factor 是 1，但和 [python-docx](python-docx.zh.md) 一样，它已经在单人维护下存活约 13.7 年且保持活跃——Lindy 先验认可的是已被证明的连续性，不是人头数。
- **年龄／Lindy：两半都强** —— 创建于 2013-01-04（约 13.7 年）**且** 2026 年仍在推。这是本分类里最健康的「年龄 × 仍活跃」组合；[python-pptx](python-pptx.zh.md) 有年龄没活跃度，[OfficeCLI](officecli.zh.md) 有活跃度没年龄。
- **采用度：广且承重** —— 3,972 star／671 fork；`Development Status :: 5 - Production/Stable`；文档化的 Pandas 和 Polars 集成；而且它是 **[python-pptx](python-pptx.zh.md) 的运行时依赖**（`XlsxWriter>=0.5.7`），所以无论作者是否主动选择，它都随大量 Python deck 生成栈一起出货。作者还维护着 Perl 版等价物（`Excel::Writer::XLSX`），说明这是长期的领域投入。[推断]
- **风险标记** —— 无 relicense 历史（一直是 BSD-2-Clause）；无 open-core 功能门；本次评审未发现 CVE 记录；无遥测或网络代码。现存风险很窄：只写的范围意味着它不重写就无法长成编辑工具；以及公式不求值，会在信任缓存的读取方那里静默产出零。

## 存疑（未验证）

- [未验证] openpyxl 在本页多处被点名为读写替代方案，但**未被收录**：它的规范仓库是 `https://foss.heptapod.net/openpyxl/openpyxl`（Mercurial／Heptapod，据 PyPI `Source` 元数据，2026-09-18 验证），且没有官方 GitHub 仓库——只有一个 bitbucket 时代、202 star 的旧克隆。本索引的 `tools/health.py` 和 `tools/upstream_snapshot.py` 都硬解析 `github.com/owner/name`，所以 openpyxl 在这里无法被评分或快照。记为已知索引缺口，不是对 openpyxl 的负面判断。
- [未验证] 「除非提供 `value=`，XlsxWriter 写入的公式缓存结果是 `0`」这一说法——这是该库的文档化行为，也是 [OfficeCLI](officecli.zh.md) 专门做了一个 `FormulaCache` handler 的原因，但本次未对真实工作簿执行验证。
- [未验证] 相对 openpyxl 的写入速度——「更快」反映的是该库只写的设计和社区通常的说法，不是本次跑出的基准。
- [未验证] `constant_memory` 模式的顺序限制是否会破坏某个具体的图表或格式化特性——该模式的存在已从 README 验证，但其交互矩阵未测试。
- [推断] 作者持续维护 Perl 版 `Excel::Writer::XLSX` 是由 `setup.py` 里的 `jmcnamara@cpan.org` 作者邮箱和该项目的公开历史推断的；本次评审未拉取那个 Perl 仓库。
- [未验证] 50 位列出的贡献者是否覆盖完整历史——GitHub contributors API 有结果上限且排除未关联邮箱的身份，[python-docx](python-docx.zh.md) 就是这种情况；93.3% 的单人占比可能被略微低估或高估。
