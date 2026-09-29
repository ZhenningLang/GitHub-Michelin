---
name: scriptc
slug: scriptc
repo: https://github.com/vercel-labs/scriptc
category: runtimes-and-compilers
tags: [typescript, javascript, compiler, native-binary, llvm, wasm]
language: TypeScript
license: Apache-2.0
maturity: v0.1.x, experimental, 5.5k stars (as of 2026-09)
last_verified: 2026-09-28
type: tool
homepage: https://scriptc.dev
upstream:
  pushed_at: 2026-09-28T06:41:04Z
  default_branch: main
  default_branch_sha: b900575120d8e75259fa5c76c04a43b0db42cbe7
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T06:51:49Z
  overall: C
  overall_score: 2.33
  scored_axes: 6
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
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 222.2
        qualifying_issues: 27
        band: relaxed_solo
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: npmjs.org
        canonical_package: "@scriptc/runtime"
        dependent_repos_count: 0
        downloads_last_month: 23069
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
        release_downloads: 379
        release_assets: 41
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: D
      raw:
        repo_age_days: 67
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 43
        top1_share: 0.88
        top3_share: 0.907
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# scriptc

你用 TypeScript 写了个小工具，交付却成了麻烦：目标机器要装一整套 Node，或者打出一个比程序本身大几十 MB 的单文件。scriptc 把普通的、带类型的 TypeScript 直接编译成约 320KB 量级的原生可执行文件：二进制里没有 Node、没有 V8、没有任何 JavaScript 引擎。

![scriptc — 健康度雷达](../../../../assets/health/scriptc.zh.svg)

## 何时使用

你在维护一个类型写得干净的小型 TypeScript 程序——内部 CLI、构建工具、webhook 处理器、agent 脚本——而交付环境让「带运行时」变得别扭：瘦身容器里 Node 基础镜像是最厚的一层；目标机器不受你控制；或者用户就该直接拿到一个二进制。`scriptc build hello.ts -o hello` 把这个文件变成原生可执行文件，毫秒级启动，只链接系统 C 库；`scriptc coverage` 还会预先告诉你每条语句能不能静态编译。

选 scriptc 而不是 `bun build --compile` 或 `deno compile`，决定性的取舍是：你要的是二进制体积、启动速度和编译期严格性，而不是生态广度——后两者把完整的 JavaScript 引擎快照进每个二进制，几乎什么 JS 都能跑；scriptc 只编译类型能证明静态的部分，其余的在编译期用带错误码的诊断拒绝——这正是你从 tsc 那里已经习惯的纪律。一份带类型的代码同时要出原生二进制和 WASI 模块时，它也合适。

## 怎么用起来

scriptc 是编译器，不是打包器。真正的 TypeScript 编译器——就是在编辑器里给你做类型检查的那个 tsc——先解析并类型检查你的程序，然后把语法树降成带类型的中间表示（IR：程序的一种可序列化形式，泛型已经特化成具体类型，联合类型变成带标签的值）。从 IR 出发，后端可以写出可读的 C 或 LLVM IR；默认路径把 LLVM IR 交给自带的 LLVM 22 助手生成汇编和目标文件，再由平台链接器把目标文件和一份预编译运行时包（引用计数的值运行时、承载 async/await 的有栈协程、kqueue/epoll 事件循环、原生的 `net`/`http`/`tls` 实现）拼在一起，全程不编译任何 C 代码。内存用引用计数——最后一个引用消失的瞬间值就被释放——引用环则在固定的时点由环收集器回收，没有垃圾回收器。任何构造都不会被悄悄造假：每条语句恰好落在三档之一——编译为原生代码；加了 `--dynamic` 时跑在内嵌的 quickjs-ng 引擎上（为 npm 包的 JavaScript 和 `any` 代码准备，约 620KB）；或者被拒绝，并给出错误码和改写提示。

![scriptc — 主干用户故事](../../../../assets/flow/scriptc.zh.svg)

<!-- flow-steps:begin (generated from flows/scriptc.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：用 npm 装好编译器，照常写有类型的 TS 文件 — `npm install -g scriptc` — 组件：`scriptc CLI（Node 24+）`
2. **你**：不跑在 Node 上，直接要一个独立可执行文件 — `scriptc build hello.ts -o hello`
3. **scriptc**：真正的 tsc 做类型检查，AST 降成带类型 IR — 组件：`tsc 前端`
4. **scriptc**：自带的 LLVM 助手把 IR 编成汇编和目标文件 — 组件：`LLVM 22 助手`
5. **scriptc**：平台链接器把目标文件和预编译运行时包拼起来，全程不编译任何 C 代码 — 组件：`运行时包`
6. **你**：直接运行和分发这个二进制——目标机器不需要 Node，也没有 JS 引擎 — `./hello`

**价值**：约 320KB 的原生二进制，毫秒级启动——目标机器不用装 Node、不带引擎、不需要 node_modules

</details>
<!-- flow-steps:end -->

## 何时不用

- **程序大部分是无类型代码或 npm JavaScript。** 依赖 `any`、松散对象或大量 npm 导入的代码会涌进内嵌的 quickjs 岛——语义正确，但 CPU 密集代码更慢，每次跨界还要付校验成本。改用 `bun build --compile` 或 `deno compile`——它们内嵌完整引擎，任何 JS 原样能跑。
- **依赖 Node 原生插件。** Node-API / `.node` 插件在编译期被直接拒绝（`createRequire` 加载插件也一样）。插件不可替代就留在 Node.js；scriptc 的替代路线是它的原生 FFI——清单声明式的纯 C ABI 链接，但目前不支持变参调用和按值传结构体。
- **需要和 Node 分毫不差的行为。** scriptc 的分歧点有文档但确实存在：类型化数组越界访问会中止进程而不是返回 `undefined`；部分运行时陷阱不可捕获；`Object.keys` 按声明顺序而不是插入顺序；运行时错误不带 `errno`/`syscall`/`path`。依赖 Node 内部行为的程序请留在 Node.js。
- **想要系统级语言的性能。** 数字到处都是 JS 精度的 f64；整数推断和所有权分析是路线图项目，不是已交付能力。要 Rust/Go 级别的内存与整数控制，就写 Rust 或 Go，而不是编译 TypeScript。
- **需要稳定的编译器契约。** v0.x、明晃晃的「Vercel Labs Experiment」实验标签、单一主力维护者、对象 ABI 明确写了「精确到运行时版本兼容，不承诺 semver 稳定」。要让产品在上面编译好几年，先钉死版本，把它当爆炸半径可控的年轻工具——内部 CLI、小型分发工具——而不是平台。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Bun](bun.zh.md) | ✅ | 代码类型干净、二进制必须又小又快启动时，用 scriptc 编译；重度依赖 npm JavaScript 时用 `bun build --compile`，因为内嵌的完整运行时让一切原样能跑。 | scriptc：约 320KB 的原生二进制加编译期拒绝，但只有它的静态面和 quickjs 岛。Bun：npm 兼容性拉满，但二进制是引擎级的体积，启动也更慢。 |
| [Deno](deno.zh.md) | ✅ | 要单文件分发且必须有 V8 的精确语义和 Deno 权限模型时，选 `deno compile`；要「彻底没有引擎」和 tsc 级的类型闸门时，选 scriptc。 | Deno 把完整 V8 运行时快照进产物（更大、要付引擎启动成本）；scriptc 只内嵌自己的 C 运行时，证明不了的直接拒绝。 |
| Node.js SEA | 未收录 | 程序必须在所有环境表现得和 Node 一模一样时，Node 官方的 Single Executable Applications 是保守选择；静态面子集够用时，scriptc 是体积与启动速度的选择。 | SEA 每个产物都装着完整的 Node 二进制；scriptc 把子集编译成原生代码，但这个子集要在编译期过关。本批 tab-intake 未收录。 |
| vercel/pkg | 未收录 | 把 pkg 当作这个问题的归档先祖——把 Node 快照进单文件；如今做任何正经事都选 scriptc 或 Bun/Deno compile，因为 pkg 自 2024 年初就已归档。 | pkg 把整个 Node 运行时冻进每个二进制，现在无人维护；scriptc 只编译类型背书的部分，且在活跃开发。本批 tab-intake 未收录。 |
| AssemblyScript | 未收录 | 目标是 WebAssembly、且能用它那套类 TypeScript 方言和自带标准库写代码时，AssemblyScript 是成熟路线；目标是编译手头这份 Node 风味 TypeScript 时，scriptc 保住真正的 tsc 语义。 | AssemblyScript：成熟且只出 wasm，但它是独立方言（不是你的 TS，也没有 npm）。scriptc：跑你真实的 TypeScript 加 Node API，但很年轻，且只有 WASI Preview 1。本批 tab-intake 未收录。 |

## 技术栈

- **TypeScript 加真正的 tsc API**——前端：解析、按 `es2025` 做类型检查、降成带类型的 IR
- **两个后端**——`--emit=c` 写可读的 C；默认 LLVM 路径把 IR 交给自带的进程外 LLVM 22 助手生成汇编和目标文件
- **C 运行时**（`packages/runtime`）——引用计数加确定性环收集器、承载 async/await 的有栈协程、kqueue/epoll 事件循环、原生的 `net`/`http`/`https`/`tls`（内置 mbedTLS）、zlib、libregexp
- **quickjs-ng**——可选的 `--dynamic` 岛，承载 npm 包 JavaScript 和 `any` 代码
- **编译器本身跑在 Node.js 24+ 上**；pnpm monorepo；正确性由差分测试语料（与 Node 逐字节一致的 stdout/stderr/退出码）、test262、以及 AddressSanitizer 加引用计数审计的测试道守着

## 依赖

- 构建机：Node.js 24 或更新（`npm install -g scriptc`）；`--emit=ir|c|llvm` 只需要 Node
- 原生可执行文件：平台链接器驱动加 SDK/sysroot（用 `SCRIPTC_LINKER` 选择）；在 macOS 15+ arm64 上 clang 只当链接驱动——不编译任何 C
- 交叉编译和 `wasm32-wasi` 目标：PATH 里有 Zig（`SCRIPTC_CC=zigcc SCRIPTC_TARGET=<triple>`）
- 消毒器构建、显式 C 构建、LLVM 回退：需要一个 C 编译器
- 目标机器：什么都不需要——二进制只链接系统 C 库

## 运维难度

**低。** 一条 npm 命令装的 CLI，没有要跑的服务，没有要带的运行时。真正的负担是版本更迭：v0.x 发布极快（约十周里发了 44 个 npm 版本），对象 ABI 明确写着「精确到运行时版本兼容」，所以在 CI 里钉死编译器版本、每次升级后重跑 `scriptc coverage`；平台相关的点（链接器选择、交叉编译要 Zig）是仅有的环境差异。

## 健康度与可持续性

- **维护——非常活跃（2026-09-28 核查）：** 本页核验当天上午仍有提交和议题关闭；v0.1.7 发布于 2026-09-27，是 2026-07-13 以来的第 44 个 npm 版本。
- **治理与巴士系数：** 实质上的单一主力维护者（Chris Tate，Vercel 工程师，约 98% 的贡献量）在 vercel-labs 组织下工作——这是厂商工程师的个人项目，不是社区或基金会。
- **背书与年龄：** Vercel Labs，带明确的「EXPERIMENT」实验标签；仓库创建于 2026-07-22（约两个月大）。年龄乘以活跃度的结论是：活跃，但远年轻到谈不上任何 Lindy 先验——两个月 5.5k star 更像发布热度，不是耐久性证明。
- **采用：** 截至 2026-09-28，近一个月 npm 下载 23,069 次（周下载约 9.5 千）；项目在推进自举里程碑——它自己的 TypeScript 客户端和部分 LLVM 发射器已用 scriptc 编译。
- **风险标记：** v0.x、自我标注实验性；与 Node 的分歧有文档；对象 ABI 不承诺 semver 稳定；未查证已知 CVE。Apache-2.0（直接读过 LICENSE 文件）——干净宽松的许可证。

## 存疑（未验证）

- [未验证] 约 320KB 二进制体积和毫秒级启动来自项目自家文档，未在独立机器上实测。
- [推断] 「quickjs 岛跑 CPU 密集代码更慢」是官方文档的自述，此处没有跑过基准测试。
- [未验证] Vercel 的长期承诺：「Labs 实验」标签不附带产品化保证，文档之外没有找到路线图。
- [未验证] 真实生产环境部署：没有从一手来源确认过——自举里程碑来自项目自己的议题和 CI。
- [推断] 两个月 5.5k star 的轨迹按本索引「年轻高热仓库」的启发式当作热度信号而非持续采用来处理。
