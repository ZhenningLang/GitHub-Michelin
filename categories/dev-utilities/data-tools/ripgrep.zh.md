---
name: ripgrep
slug: ripgrep
repo: https://github.com/BurntSushi/ripgrep
category: data-tools
tags: [search, grep, regex, cli, rust, gitignore]
language: Rust
license: Unlicense OR MIT
maturity: v15.2.0 (2026-07-15), active, ~68.9k stars (as of 2026-10)
last_verified: 2026-10-08
type: tool
upstream:
  pushed_at: 2026-08-04T13:59:44Z
  default_branch: master
  default_branch_sha: 3fce3b5bb0236da2df6d99672afb8a719642eca7
  archived: false
health:
  schema: 1
  computed_at: 2026-10-08T08:18:24Z
  overall: B
  overall_score: 3.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 65
        active_weeks_13: 4
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 22.6
        qualifying_issues: 21
        band: relaxed_solo
        window_offset_days: 8
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: crates.io
        canonical_package: ripgrep
        dependent_repos_count: 1
        downloads_last_month: 1596244
        graph_tier: D
        volume_tier: A
        cross_check_divergence: 13.63
        homebrew_installs_90d: 207766
        homebrew_tier: A
        release_downloads: 59135258
        release_assets: 678
        release_tier: A
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 3863
        last_commit_age_days: 65
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 6
        top1_share: 0.829
        top3_share: 0.946
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Unlicense
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# ripgrep

你在真实项目里敲 `grep -rn retryBackoff .`，然后干等它爬完 `node_modules`、`target/` 和压缩过的打包产物，再从几百条生成文件里的命中和一行行 “Binary file matches” 中翻出真正有用的那两条。ripgrep（`rg`）搜同一棵目录树，但会跳过 `.gitignore` 里早就声明为噪音的东西，外加隐藏文件和二进制文件，而且快到可以随想随搜。

![ripgrep — 健康度雷达](../../../assets/health/ripgrep.zh.svg)

## 何时使用

你是开发者——或者是一个编码 agent——一天要在代码库里搜几十次：这个函数在哪被调用、哪个配置设了这个开关、还有谁在 import 那个旧模块。仓库里躺着 600 MB 的 `node_modules`、一个构建目录和一些 vendor 代码，于是 `grep -r` 又慢、输出又大多是你根本不想要的命中，而 `git grep` 又看不到你刚新建、还没加入跟踪的文件。你敲 `rg retryBackoff`（或者 `rg -tpy 'def retry'`，只搜 Python 文件），结果按文件分组、带行号，而且只来自你真会去改的那些文件。

做交互式代码搜索时选 ripgrep 而不是 GNU grep，是因为它的默认行为贴合项目的实际布局——默认递归，遵守 `.gitignore`、`.ignore`、`.rgignore`，跳过隐藏文件和二进制文件——而且在始终开启 Unicode 的情况下依然很快。选它而不是 The Silver Searcher（ag），是因为 ag 自 2020 年起就没有新提交；选它而不是 ack，是因为 ripgrep 是一个静态二进制，而不是一段 Perl 脚本；选它而不是 `git grep`，是当你需要在仓库之外搜索，或者要把未跟踪的文件也搜进来时。

## 怎么用起来

你只给 `rg` 一个模式，外加一个可选的路径，剩下的它全包了。它用多个线程同时遍历目录树，在读一个文件之前先拿它去对你的忽略规则，并跳过隐藏文件和看起来是二进制的文件（内容里有 NUL 字节）——所以大部分噪音压根不会被打开。对剩下的每个文件，它用 Rust 的正则引擎去匹配：这个引擎把你的模式编译成有限自动机（一台逐字节读文本、从不回退重试的状态机），并且先用 SIMD 指令（一次比较很多个字节的 CPU 指令）扫描模式里的字面片段，所以大多数行在完整正则运行之前就被排除了。命中结果按文件分组、带行号和颜色打印；加 `--json` 则输出机器可读的格式。**你要决定的是模式本身，以及网撒多大**：`-t`、`-T` 按文件类型包含或排除，`-g` 加 glob，`-u`、`-uu`、`-uuu` 逐级关掉忽略文件、隐藏文件和二进制文件的过滤——当你要找的东西恰好藏在“噪音”里时就用它们。需要前后断言（look-around）或反向引用时切到 PCRE2（`-P`），默认引擎刻意不支持这些。

![ripgrep — 主干用户故事](../../../assets/flow/ripgrep.zh.svg)

<!-- flow-steps:begin (generated from flows/ripgrep.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：从包管理器或 release 页装上 rg 二进制 — `brew install ripgrep · choco install ripgrep` — 组件：`rg 二进制`
2. **你**：在项目根目录搜一个模式——可以只限某种文件类型 — `rg -tpy foo`
3. **ripgrep**：多线程遍历目录树，跳过被 gitignore 的、隐藏的和二进制文件 — 组件：`ignore crate`
4. **ripgrep**：先按字面片段预筛，再对剩下的行跑完整正则 — 组件：`regex crate`
5. **ripgrep**：按文件分组打印命中，带行号和颜色

**价值**：随想随搜整个代码库，不用在 node_modules、构建产物和二进制文件里蹚水

</details>
<!-- flow-steps:end -->

## 何时不用

- **脚本必须在任何 POSIX 机器上原样运行。** ripgrep 没有预装，也不遵循任何标准（它的 README 自己就这么说）。可移植的 shell 脚本、最小化容器和别人的服务器上，用 `grep` 而不是 ripgrep。
- **你要搜 zip、tar、7z 归档内部，或者 PDF、Office 文档。** ripgrep 的 `-z` 只会解压单个压缩文件（gzip、bzip2、xz、lz4、lzma、brotli、zstd），不会打开归档里的成员；文档则要你自己写 `--pre` 预处理器。用 ugrep（未收录），它能直接搜嵌套归档和文档。
- **你不知道标识符，只知道行为。** ripgrep 匹配的是文本；如果没有共同的字面词，它找不到“决定上传失败后何时重试的那段代码”。这种情况用 [Jevgrep](../../rag-retrieval/code-intelligence/jevgrep.zh.md)（由模型排序结果，按查询付费）或基于向量嵌入的代码索引，手里有确切词的时候再用 ripgrep。
- **你要按代码*结构*而不是文本来匹配。** “所有第二个参数里没有 `timeout` 的 `fetch` 调用”写成正则会非常脆弱。用 ast-grep（未收录），它按语法树模式匹配。
- **一个团队整天在同一个巨大的多仓库语料上搜索。** ripgrep 每次运行都重新读文件，不保留索引（源码树里有一个实验性的 `unstable-index` 特性，但没进 release）。要给几百个仓库做常驻的共享搜索，用 Zoekt（未收录）这类带索引的搜索引擎。
- **你就在一个 Git 仓库里，只想搜某个提交时的已跟踪内容。** `git grep` 能搜已跟踪文件或任意历史版本（`git grep foo v1.2`），不用另装任何东西；ripgrep 只看得到磁盘上的文件。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| GNU grep | 未收录 | 写可移植脚本、在不归你管的机器上，用 grep；在自己的键盘前搜代码库，用 ripgrep，这时按忽略规则过滤的默认行为和速度比“到处都有”更重要。 | grep 处处可用、有 POSIX 规范，但递归搜索要加参数，还会扎进被忽略的文件和二进制文件；ripgrep 默认更快、更安静，但得先装上。 |
| git grep | 未收录 | 在仓库内只想搜已跟踪文件或某个历史版本时，用 `git grep`；需要搜未跟踪文件、非仓库目录或按文件类型过滤时，用 ripgrep。 | git grep 无需安装，还能搜任意提交；但它不看未跟踪文件，也只能在 Git 仓库里用。 |
| ugrep | 未收录 | 需要搜归档、PDF、Office 文件，需要模糊匹配或交互式 TUI 时，选 ugrep；纯粹搜源码树时继续用 ripgrep，它的默认行为已是事实标准。 | ugrep 在兼容 grep 的接口后面塞了多得多的功能（归档、模糊搜索、`-Q` TUI、可选索引器）；ripgrep 范围更窄，但用户基础大得多。 |
| The Silver Searcher（ag） | 未收录 | 不要在 ag 上开始新的工作——它自 2020-12 起就没有提交；把现有别名迁到 ripgrep，后者覆盖同样的“按 gitignore 过滤”场景并且仍在维护。 | ag 是最早的“快速、认识 gitignore 的 grep”；如今它带着没人修的 bug，也不会再有新版本。 |
| [Jevgrep](../../rag-retrieval/code-intelligence/jevgrep.zh.md) | ✅ | 问题是一段对行为的描述、手里没有确切词时，试试 Jevgrep；知道确切词时，ripgrep 即刻作答，离线且免费。 | Jevgrep 返回经模型排序、带摘录的一小部分结果，但要花付费 token，还要把代码发给托管模型；ripgrep 返回所有字面命中，不做排序。 |

## 技术栈

- **Rust**（edition 2024，需 Rust 1.96 及以上构建），组织成一组可复用的 crate：`ignore`（带 gitignore 规则的并行目录遍历器）、`globset`、`grep-searcher`、`grep-printer`、`grep-regex`、`grep-pcre2`。
- **正则：** `regex` crate（有限自动机、SIMD 字面量搜索、始终开启 Unicode）；可选 PCRE2，通过 `-P` 或 `--engine auto` 启用。
- **I/O：** 在内存映射（适合单个文件）和增量缓冲读取（适合大目录）之间自动选择。
- **输出：** 人类可读格式，或 `--json`（`delta` 等工具可以直接消费）。

## 依赖

- **运行时：** 无。release 压缩包里只有一个可执行文件（`rg`）；Linux 和 Windows 版本是静态构建，官方 release 还把 PCRE2 静态链接了进去，所以 `-P` 不依赖系统库。
- **平台：** Windows、macOS、Linux，x86_64 与 aarch64（Windows aarch64 自 15.0 起提供，`aarch64-unknown-linux-musl` 自 15.2 起提供）；15.0 起不再提供 `powerpc64` 构建。
- **从源码构建：** 稳定版 Rust 工具链；开启 `--features pcre2` 还需要一个 C 编译器（或通过 `pkg-config` 找到系统 PCRE2）。

## 运维难度

**几乎为零。** 用包管理器安装（`brew install ripgrep`、`choco install ripgrep`、各发行版的包），或者把 release 二进制丢进 `PATH`。行为可以通过 `RIPGREP_CONFIG_PATH` 指向的配置文件调整，团队值得在 dotfiles 里统一这份配置；唯一需要预料到的意外是：发行版的包可能落后一个版本，或者编译时没带 PCRE2。

## 健康度与可持续性

- **维护（2026-10-08）：** 稳定而不忙碌——15.0.0（2025-10）、15.1.0（2025-10）、15.2.0（2026-07-15），主要是 bug 修复和目录遍历性能；默认分支最近一次提交在 2026-08-04，距本次核查 65 天，近 13 周里有 4 周有提交（雷达：B）。对一个功能已基本完成的命令行工具来说，这是成熟的节奏，不是衰退。
- **治理与 bus factor：** 实质上是单人维护——绝大多数提交出自 Andrew Gallant（BurntSushi）；近一年 6 位活跃维护者中，前三贡献者占比 94.6%（雷达：D）。ripgrep 所依赖的 `regex` crate 也由他维护，风险集中，专业积累也集中。
- **年龄与 Lindy：** 2016-03 创建，约 10.5 年，至今仍在发版——对命令行工具来说是很强的 Lindy 信号。
- **采用：** 约 6.89 万 star；crates.io 上月下载 1,596,244 次，90 天 Homebrew 安装约 20.8 万次，release 资产下载约 5900 万次（评分器 2026-10-08 快照）。VS Code 把它作为文本搜索的后端一起分发（VS Code 的 `package.json` 里是 `@vscode/ripgrep-universal`），编码 agent 做代码搜索时也常常直接调用 `rg`。
- **风险信号：** Unlicense 或 MIT 双许可，没有改许可证的历史，也没有商业版。主要风险是 bus factor，但二进制自成一体、grep 随时可以顶上，这让风险缓和不少。

## 存疑（未验证）

- [未验证] 相对 grep、ag、ugrep 的速度说法，来自作者自己的基准测试和 ugrep 自己的基准仓库；结果取决于查询、文件系统和缓存状态。
- [推断] “编码 agent 常常直接调用 `rg`”，依据的是推荐或捆绑它的 agent 工具和本索引里的相关页面，不是使用量调查。
- [未验证] 各发行版的包是否带 PCRE2 因发行版而异；这里只核对了官方 release 流程（`--features pcre2`，静态链接 PCRE2）。
- [推断] `Cargo.toml` 把 `unstable-index` 特性标为“正在积极开发，可能有非常严重的 bug”；它会不会、何时进入 release，未知。
