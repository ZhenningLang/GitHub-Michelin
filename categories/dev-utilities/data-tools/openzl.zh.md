---
name: OpenZL
slug: openzl
repo: https://github.com/facebook/openzl
category: data-tools
tags: [compression, structured-data, codec, columnar, zstd, meta]
language: C
license: BSD-3-Clause
maturity: v0.2.0, active, pre-1.0 (2026-05); format/API still changing
last_verified: 2026-06-26
type: library
upstream:
  pushed_at: 2026-06-26T17:29:05Z
  default_branch: dev
  default_branch_sha: a4d56c1af24b07799d76f0b390201545b33c2157
  archived: false
health:
  schema: 1
  computed_at: 2026-09-19T08:50:26Z
  overall: B
  overall_score: 3.0
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 102.4
        qualifying_issues: 7
        band: default
        window_offset_days: 0
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: D
      raw:
        repo_age_days: 276
        last_commit_age_days: 2
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 29
        top1_share: 0.272
        top3_share: 0.637
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    adoption: { reason: ambiguous }
    risk_license: { reason: license_unparsed }
---

# OpenZL

来自 Meta 的格式感知压缩框架：你描述结构化数据的形状，它据此构建一个专用压缩器，而它产出的所有结果都能被同一个通用解压器读取。

![openzl — 健康度雷达](../../../assets/health/openzl.zh.svg)

## 何时使用

你是数据平台或存储工程师，手里压着 TB 级别的某一种高度结构化负载——固定 schema 的遥测记录、AI 训练管线的列式特征转储、有序整数数组、多字段二进制日志。通用字节流压缩器（zstd、lz4）把整块数据当作不透明序列处理，因此白白浪费了大量压缩比：它永远看不到第 3 列是单调递增的时间戳、第 7 列是低基数枚举。你也试过手搓一条「转置 → delta → zstd」的管线，确实管用，但每个数据集都要单独写一套，维护起来很烦。OpenZL 让你转而去*描述*数据——通过预置 profile、SDDL（Simple Data Description Language）或自定义 parser——它会把原始 codec 组合成一张 DAG，把记录拆成同质流（parse → group → transform & compress），在真正能带来收益的地方施加 delta / 转置 / 字典等步骤。

回报有两层：一是你能在那个特定格式上拿到比通用压缩器更实在的「比率—速度」表现；二是你产出的每一帧，无论由哪张图生成，都能被 OpenZL 唯一的通用解压器读取——下游消费方不必知道用的是哪个专用压缩器。Meta 声称核心已「reached production-readiness」并且「used extensively in production at Meta」，如果你考虑把它放进真实的入库管线而非一次性试验，这点能让人更安心。

## 何时不用

- **通用 / 非结构化 / 文本块。** OpenZL 的杠杆来自对同质流（数值、列式、表格）的格式感知。对任意文本、源代码、混合 Web 负载或「就压一下这个文件」,zstd、brotli 这类通用压缩器更简单，效果大概率也不差——文档本身就没给出任何通用/文本场景的性能主张。[推断]
- **你现在就需要格式稳定。** 项目说得很直白：「The API, the compressed format, and the set of codecs and graphs included in OpenZL are all subject to (and will!) change.」只有 release-tag 提交才带多年解压保证；`dev` 分支「no guarantees whatsoever」。仍是 pre-1.0。
- **小负载 / 一次性文件。** 「描述数据 + 构建专用压缩器」的工作流有实打实的前期建模成本。面对少量小文件或异构文件，这远不如 `zstd -19` 划算。
- **你想要一个能直接替换 `gzip`/`zstd` 的 CLI。** 这是一个你要去组合的框架 + 库，以及一种你要去采用的格式，而不是 shell 管线里现成压缩器的透明替身。
- **不写 C/C++、不想碰原生构建的团队。** 它是 C11/C++17 代码库，用 CMake/Make 构建；你要背上原生工具链，以及对一个仍在演进的格式的维护负担（在格式稳定前会被锁定在 OpenZL 帧格式上）。
- **Windows 优先的团队。** 构建建议用 clang-cl;MSVC「may produce C2099 errors due to limited C11 support」。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [CyberChef](cyberchef.zh.md) | ✅ | 分析师需要浏览器里做临时编解码/压缩 recipe 时，选 CyberChef。 | 浏览器里给分析师做临时编解码/压缩 recipe；交互、通用，不是面向生产、为压缩比调优结构化数据的库。 |
| [DevToys](devtoys.zh.md) | ✅ | 需要桌面开发者工具箱和一次性压缩/格式化小工具时，选 DevToys。 | 桌面开发者工具箱，内置压缩/格式化小工具；方便做一次性任务，而非可编程的格式感知压缩器。 |
| zstd | 未收录 | 需要通用压缩基线时，选 zstd。 | 通用基线（同为 Meta/BSD）。在任意字节上「比率—速度」极佳；OpenZL 的目标是在特定结构化格式上靠格式感知*超过*它，代价是你得先描述数据。 |
| Parquet + zstd/snappy | 未收录 | 需要主流列式落盘路径时，选 Parquet 加 zstd/snappy。 | 主流的列式落盘路径：schema 感知编码（字典/RLE）加块级 codec。成熟且无处不在；OpenZL 是更底层的框架，让你构建自定义 codec 图，而非一种自带生态的文件格式。 |
| BLOSC / blosc2 | 未收录 | 需要面向数值数组的分块加 shuffle/bitshuffle 元压缩时，选 BLOSC/blosc2。 | 面向数值数组的分块 + shuffle/bitshuffle 元压缩器；「先变换再压缩」思路相近，范围更窄、比 OpenZL 更成熟。 |
| Brotli | 未收录 | 需要面向文本/Web 内容的强通用压缩时，选 Brotli。 | 强通用压缩器（尤擅文本/Web）；对结构化数值数据没有格式感知。 |

## 技术栈

- **语言：** 仓库中 C（约 51%）与 C++（约 44.7%）。
- **核心模型：** 把 codec 组合成有向无环图（DAG）；唯一的通用解压器「can decompress anything produced by the compressor, independent of the compression DAG」。
- **数据描述：** 已知格式的预置 profile、SDDL(Simple Data Description Language)、直接传入的同质流，或自定义 parser。
- **工具：** 核心库加 CLI(`cli/`)、示例 transform/parser、benchmark 与测试套件；含 Python 绑定（`py/`）。[推断] Python 绑定的具体范围未超出「目录存在」之外验证。
- **构建：** CMake（≥ 3.20.2）或 Make；需要支持 C11 + C++17 的编译器。

## 依赖

- **工具链：** 支持 C11 与 C++17 的编译器（GCC/Clang;Windows 推荐 clang-cl）。走 CMake 路径需 CMake ≥ 3.20.2。
- **内置依赖：** 仓库带有 `deps/` 目录与子模块（`.gitmodules`）；构建拉取自带依赖，而非要求笨重的外部运行时。[推断] 依赖清单未在此逐项核实。
- **运行时：** 无 server/daemon/数据库——它是可嵌入的压缩库 + CLI，不是服务。
- **安装：** 从源码构建（`make`，或 `cmake -DCMAKE_BUILD_TYPE=Release ..`）；未核实到已发布的包管理器制品。

## 运维难度

**作为库：低到中；作为格式承诺：中。** 运维层面没什么要跑的——没有服务、没有数据库；你链接库或调用 CLI。但这份「低」被两项真实成本抵消：(1) 你得自己背一套原生 C11/C++17 构建（CMake/Make,Windows 上还要折腾 clang-cl）;(2) *格式演进*负担——因为压缩格式在 pre-1.0 阶段仍在变，你必须 pin 到 release-tag 版本，并为长期的重压缩 / 版本错配做预案，尽管 release 产出的帧能「at least the next several years」保持可解压。前期的数据建模工作（写 SDDL / 选图）是每个数据集的设计任务，而不是部署任务。

## 健康度与可持续性

- **响应速度**：Grade B——中位首次响应时间 102.4 小时，基于 7 个 qualifying issues/PRs。
- **维护（2026-06）：** **活跃**——最近 push 在 2026-06；打 tag 的 release 在推进（v0.1.0 2025-10 → v0.2.0 2026-05），但明确仍是 **pre-1.0**，格式/API/codec 集被声明为仍在变动。[推断]
- **治理与 bus factor:** `Organization` 名下，归 **Meta**（`facebook`）所有，与 zstd 同门——厂商背书强、有团队治理，bus-factor 风险低。Meta 声称核心「is used extensively in production at Meta」，说明有内部用户在维系它。[未验证]
- **年龄与 Lindy（约 9 个月，2025-09 创建）：** **年轻、Lindy 上未经检验**——太新，不能仅凭耐久性押注。缓和因素不是年龄而是背书方的记录（Meta/zstd 血统）；但 pre-1.0 意味着格式本身仍是移动靶。
- **风险标记：** **格式演进锁定**是首要风险——只有 release-tag 的帧带多年解压保证，`dev` 分支没有任何保证。请 pin 到 tag，并为重压缩/版本错配做预案。原生 C11/C++17 构建；Windows/MSVC 支持弱。[推断]

## 存疑（未验证）

- [未验证] 许可证为 BSD;LICENSE 文件带三条条件（含非背书条款），故 SPDX 取 `BSD-3-Clause`（Meta 标准许可，与 zstd 同族）——frontmatter 反映的是这一推断，而非仓库内声明的 SPDX 标记（`gh` 报告许可为「Other/NOASSERTION」）。
- [未验证] 最新 release v0.2.0，日期 2026-05-07；首个公开 release v0.1.0 在 2025-10-06（与工程博客和白皮书 arXiv:2510.03203 同期）。截至 2026-06 star 约 3.1k——GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 语言占比（C 约 51% / C++ 约 44.7%）是 GitHub linguist 估算，会随时间变化。
- [推断] 「在结构化数据上压缩比优于通用压缩器」是项目自身的表述；此处未引用任何一方官方的正面对比数字——实际收益高度取决于数据集与你构建的 codec 图。
- [推断] 存在 Python 绑定（`py/` 目录），但其完整性/稳定性未经核实。
- [推断] 判断它不适合文本/通用数据，是因为文档只演示结构化/数值示例、未给出任何通用数据主张——并非作者明确的「不要使用」声明。
