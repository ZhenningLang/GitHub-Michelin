---
name: Faker (faker-js)
slug: faker-js
repo: https://github.com/faker-js/faker
category: data-tools
tags: [test-data, mock-data, fixtures, seeding, fake-data, javascript, typescript, locales]
language: TypeScript
license: MIT
maturity: v10.x, active, ~15.4k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-29T02:35:20Z
  default_branch: next
  default_branch_sha: acd5fdaf099bda7cf90c76bf0ae0a33349a54ce7
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:09:14Z
  overall: A
  overall_score: 3.6
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 1.6
        qualifying_issues: 12
        band: default
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@faker-js/faker"
        dependent_repos_count: 17617
        downloads_last_month: 64398665
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.0
        release_downloads: 716
        release_assets: 51
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1719
        last_commit_age_days: 0
        cohort: library
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 16
        top1_share: 0.401
        top3_share: 0.631
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Faker (faker-js)

一个 JavaScript/TypeScript 库，批量生成逼真的假数据——姓名、地址、金融、商品、日期、lorem 等等——用于测试、seed 脚本和原型，浏览器和 Node.js 都能跑。

![faker-js — 健康度雷达](../../../assets/health/faker-js.zh.svg)

## 何时使用

你是个全栈开发者，正在给新功能接线，而你的测试和本地环境却没数据可用。单元测试需要一个像样的 `User`——一个姓名、一个邮箱、一个头像 URL、一个*看起来像*街道地址的街道地址——而第十次手写 `"John Doe"、"123 Main St"` 既枯燥，又让所有 fixture 长得可疑地一模一样。你的 staging 数据库是空的，于是 UI 看上去像坏了，得有人手动敲行进去。你掏出 Faker：`faker.person.fullName()`、`faker.internet.email()`、`faker.location.streetAddress()`、`faker.commerce.productName()`——一行 import，几十个按命名空间分好的生成器，你的工厂函数从此每次运行都吐出多样、逼真的记录。调一下 `faker.seed(123)`，同一批“随机”数据就确定性地复现，于是失败的测试能重现，而不是飘忽不定。

你也会用它来填一个 seed 脚本，往 dev 库里灌几千条假订单、假客户、假商品，让看板终于有东西可渲染；或者用它给 Storybook/演示页喂上像样的内容，而不是满屏 "Lorem ipsum"。它在 Node 和浏览器里行为一致，自带一流的 TypeScript 类型，并携带 70+ 个 locale，所以德语或日语构建拿到的是符合地区习惯的姓名和地址，而非永远的美式默认值。

## 何时不用

- **假数据不等于能代表生产的真数据。** Faker 的输出看着合理，但本质是接近均匀的噪声——它**不**反映你真实的分布（取值偏态、空值比例、字段相关性、边界值聚集）。别拿它来跑查询性能基准、验证分析口径，或在与生产不符的数据上“证明”某个模型。[推断]
- **你需要 schema 感知 / 关系型数据建模。** Faker 生成的是*字段*，不是一张自洽的数据图——它不会保持外键一致、不会强制约束、也不认识你的 schema。要做关系型 fixture，你仍需在它之上加一层工厂（Fishery、factory_boy 风格）或 schema 驱动的生成器。
- **locale 覆盖参差不齐。** “70+ locale”不代表每个命名空间在每个 locale 里都完整；有些 locale 会回退到英文或数据稀疏。请核实你实际依赖的那个 locale × 模块，别假设全集等质。[未验证]
- **前端打包体积敏感。** 把 Faker 拉进上线的客户端代码会显著增重；它是给 dev/test 用的，一般应放进 `devDependencies`，靠 tree-shaking 处理掉或从生产 bundle 里排除。
- **你的运行时不是 JS。** 这是 JS/TS 库；Python 用 Python 的 `Faker`，Ruby 用 `faker` gem，等等——别只为了造假数据就把 Node 硬塞进非 JS 的测试套件。
- **你需要大规模保证唯一或穷尽取值。** 随机生成会碰撞；要大批量唯一数据，你得自己加一层唯一性/去重（Faker 提供了一些 helper，但不保证跨调用的全局唯一）。[未验证]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| Python `Faker` | 未收录 | 测试或 seeder 是 Python 而不是 JavaScript 时，选 Python Faker。 | Python 版的同一思路（JS Faker 的血缘就源自它）；当你的测试/seeder 是 Python 而非 JS 时用它。 |
| Chance.js | 未收录 | 需要更小、更老、目录更窄的随机生成工具时，选 Chance.js。 | 更小、更老的随机生成工具；更轻、零依赖，但数据目录窄得多，也没有丰富的 locale 体系。 |
| @ngneat/falso | 未收录 | 需要现代、可 tree-shake 的 TypeScript 假数据生成库时，选 @ngneat/falso。 | 现代、可 tree-shake 的 TS 假数据库，主打更轻、可逐个 import 的替代品；locale/命名空间面比 Faker 小。 |
| Mockaroo | 未收录 | 需要托管、schema 优先的 mock 数据导出，而不是进程内测试库时，选 Mockaroo。 | 托管 SaaS / schema 优先的 mock 数据生成器（导出 CSV/JSON/SQL）——不是进程内的库；适合一次性批量造数据，但它是个服务，不是你嵌进测试的仓库。 |

## 技术栈

- **语言：** TypeScript（编译为 ESM + CJS），自带一流类型定义。
- **运行目标：** 同一个包同时面向浏览器和 Node.js；与框架无关。
- **结构：** 在一个可 seed 的 PRNG 之上，按命名空间组织模块（`person`、`location`、`internet`、`finance`、`commerce`、`date`、`lorem`、`image`……），外加按 locale 引入的 locale 数据包（70+ 个 locale）。
- **分发：** 发布到 npm；提供按 locale 的入口（`@faker-js/faker/locale/*`），让你只 import 需要的那个 locale。

## 依赖

- **运行时：** 一个 JS 运行时（Node.js 或浏览器）——仅此而已；Faker 是自包含的库，不需要外部服务或数据存储。
- **安装：** `npm i -D @faker-js/faker`（通常作为 dev 依赖）。
- **从源码构建：** 需要 Node.js 加上仓库的包管理工具链（pnpm）来从仓库构建/测试；确切版本在构建时由仓库锁定。
- **无基础设施：** 生成数据不需要数据库、服务器或网络访问。

## 运维难度

**低。** 它是个库，不是服务——没什么要部署或运维的。接入成本就是 `npm install` 加上在你的工厂/seeder 里调生成器。少数真正要注意的是卫生问题而非运维：把它留在 `devDependencies` 里以免撑大生产 bundle；锁定大版本，因为 Faker 跨大版本重组过 API（v5→v6 社区接管那次以及后来的大版本都重命名/搬动过方法）；在需要确定性、可复现 fixture 的地方调 `faker.seed()`。跨大版本升级可能需要 codemod/改名，升级前先读迁移说明。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 1.6 小时，基于 12 个 qualifying issues/PRs。
- **维护（2026-06）。** 最后 push 于 2026-06（活跃）；在 v10 线上以稳定节奏发布、提交频繁——处于**活跃**而非吃老本。未归档。[推断]
- **治理 / bus factor。** 这是一个社区**组织**项目，而非单一维护者的包——而且这一点*从出身上*就很关键：faker-js 是在 2022 年 1 月、原 `faker.js` 被其唯一作者蓄意破坏并从 npm 下架之后，由社区组建的。这个社区分叉的存在，恰恰是为了消除那种单一拥有者“卷款跑路”（rug-pull）的风险，所以这里的治理结构是个**正面信号**——但当你读到旧教程引用那个已死的 `faker` 包时，了解这段血缘是有用的。[推断]
- **年龄与 Lindy 判断。** 作为这个组织/分叉约 4 年（2022-01 创建）且仍在活跃发布⇒一个**中等且在改善**的 Lindy 信号：它比其提交历史看上去要年轻（底层思路和数据源自 2011 年的原版），但你真正依赖的是这个*有治理*的化身，而它如今已经持续了约 4 年的活跃、多贡献者维护。[推断]
- **采用度与生态。** 在 JS/TS 测试生态里被广泛使用（约 15.4k star，npm 用量很大），文档良好，70+ locale，一流 TS 类型——采用度强劲、健康。[未验证]
- **风险标记。** 宽松的 MIT 许可（LICENSE 文件捆绑了上游的版权声明，这就是为什么 GitHub 自动识别报 `NOASSERTION`/"Other" 而非 "MIT"）。主要的现实风险是跨大版本的 API 变动，而非治理问题。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 15.4k GitHub star，最新发布在 v10 线（v10.5.0 报告于 2026-06）——star 数和确切版本号对时间敏感，仅供参考，请对照当前仓库重核。
- [未验证] GitHub 报告许可为 `NOASSERTION`/"Other"；而仓库的 LICENSE 文件是 MIT（它额外复述了原 faker.js 及上游 Ruby/Perl 的版权声明，这破坏了 GitHub 的单一许可自动识别）——已通过阅读 LICENSE 文件确认，这里记录差异的成因。
- [未验证] “70+ locale”是项目自己的表述；各 locale 的完整度不一，有些会回退到英文——请核实你实际依赖的那个 locale × 模块。
- [推断] Faker 生成的是字段级取值，没有跨字段/关系一致性，也不保证全局唯一；“不能代表生产”和“非 schema 感知”是对逼真但随机的数据如何表现做出的推断，而非实测结论。
- [推断] 前端打包体积影响和 dev 依赖建议是通用指引；实际成本取决于你的打包器、tree-shaking，以及你引入了哪些 locale/模块。
- [推断] 跨大版本的 API 变动（重命名/搬动方法、v5→v6 分叉接管）是从项目已知的重组推断而来；具体迁移的版本区间请查迁移指南。
