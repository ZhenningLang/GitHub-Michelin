---
name: Auto-Editor
slug: auto-editor
repo: https://github.com/WyattBlue/auto-editor
category: video-audio
tags: [video-editing, silence-removal, rough-cut, transcription, subtitle, nle-export, cli, nim]
language: Nim
license: Unlicense
maturity: 31.6.0 (released 2026-09-06), created 2020-04-30, ~5.3k stars / 655 forks, active (as of 2026-09)
last_verified: 2026-09-21
type: tool
upstream:
  pushed_at: 2026-09-19T14:52:15Z
  default_branch: master
  default_branch_sha: 7796222139b5d87fe32247f8a60a931b02006db5
  archived: false
health:
  schema: 1
  computed_at: 2026-09-21T02:29:42Z
  overall: B
  overall_score: 3.17
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 2.5
        qualifying_issues: 4
        band: relaxed_solo
        window_offset_days: 9
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: auto-editor
        dependent_repos_count: 4
        downloads_last_month: 18055
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
    longevity:
      grade: A
      raw:
        repo_age_days: 2335
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.999
        top3_share: 1.0
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

# Auto-Editor

命令行版「一遍粗剪」工具：把素材交给它，它靠响度（也可换成运动或你自己的字幕文本）判断哪里是冷场，直接剪掉，然后输出成片，或者输出一份 Premiere / Resolve / Final Cut / Shotcut / Kdenlive 能直接打开的工程。

![Auto-Editor — 健康度雷达](../../../assets/health/auto-editor.zh.svg)

## 何时使用

你录的是长篇口播素材——访谈、教程、播客、带旁白的录屏——而第一个小时永远花在同一件事上：拖时间轴，把静音段删掉。你希望在打开剪辑软件之前先完成这一遍，而且希望「切在哪里」这个**判断**由机器来做，而不是由你先想好切点、再让工具执行。

选 Auto-Editor，是因为一条命令、不需要建工程，就能把一小时素材变成粗剪；而且它把结果以两种形态交还给你：渲染好的 `video_ALTERED.mp4`，或者一份切点已经排好、原素材不重新编码的时间线工程。和最近替代品相比的决定性取舍是：[MoviePy](moviepy.zh.md) 和 FFmpeg 给你的是**机制**，保留还是剪掉的规则得你自己写；[Descript](https://descript.com) 的编辑界面更好用，但是闭源、绑账号、按席位收费——Auto-Editor 是「把静音剪掉」这件事的本地可脚本化版本。它还顺带覆盖转写这条路：`auto-editor whisper` 先出 SRT，再用 `--edit word:<值>` 按**说了什么**而不是按响度来剪。

## 怎么用起来

Auto-Editor 读素材的音轨（默认方法就是 `--edit audio:threshold=0.04`），按时间测响度，给每一刻打一个整数**标签**——`0` 表示静音、`1` 表示有效——再按标签执行动作（剪掉、保留、变速）。你控制的是规则而不是每一个切点：阈值可以用百分比或 dB，静音录屏可以把 audio 换成 `motion`，还能用 `--edit:N` / `--when:N` 加到 255 个标签类，用 `--margin` 给切点留余量避免削掉辅音。输出端刻意做成两头：要么用自带的 FFmpeg 编码写出新的媒体文件，要么写出一份引用原始素材的工程文件——所以交给人工剪辑收尾时不用重编码，也不会损失任何信息。留给你自己的是两件事：挑一个匹配你现场底噪的阈值，以及决定交付物是文件还是工程。

![auto-editor — 主干用户故事](../../../assets/flow/auto-editor.zh.svg)

<!-- flow-steps:begin (generated from flows/auto-editor.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：装好 CLI：Homebrew、AUR 或官方二进制 — `brew install auto-editor`
2. **你**：一条命令指向素材，不需要先建工程 — `auto-editor video.mp4`
3. **Auto-Editor**：逐段测响度，把每一刻标成静音（0）或有效（1）
4. **Auto-Editor**：剪掉静音，两边各留 0.2 秒，写出 video_ALTERED.mp4
5. **你**：要人工收尾时，导出时间线而不是成片 — `auto-editor video.mp4 --export resolve`
6. **Auto-Editor**：写出引用原素材的工程文件，不重新编码

**价值**：不用把素材听一遍就得到无冷场的成片，或直接交给剪辑师一条可编辑时间线

</details>
<!-- flow-steps:end -->

## 何时不用

- **这次的剪辑是创作而不是机械活。** Auto-Editor 没有时间线界面、没有回放预览、不做多机位、不做调色——它只按数值规则决定留或剪。要界面就用 [Concat](../video-editing/concat.zh.md) 或 [OpenCut](../video-editing/opencut.zh.md)，需要人逐帧判断就用商业 NLE（未收录）。
- **这一步要嵌进你自己的 Python 管线。** 直接用 [MoviePy](moviepy.zh.md) 或 [FFmpeg](ffmpeg.zh.md)：Auto-Editor 是带 CLI 的二进制程序，不是库，嵌进去意味着 shell 调用加解析输出。需要帧级访问就用 [PyAV](pyav.zh.md)。
- **你要托管式的多人文本剪辑。** 那是 [Descript](https://descript.com)（未收录）一类 SaaS，代价是素材要离开本机；Auto-Editor 全离线，没有 Web 界面也没有审阅流程。
- **部署脚本里写着 `pip install auto-editor`。** 作者已经**停止在 PyPI 发布 CLI**，安装页写得很明确——请改成固定 Homebrew formula、AUR 包或 release 二进制。
- **你对转写质量有硬要求，或者需要说话人分离。** `whisper` 子命令只内置 whisper.cpp 这条路（Whisper GGML 模型、NVIDIA Parakeet GGUF，或 macOS 26+ 的 Apple 端上转写）；需要说话人分离、以翻译为主的工作流或托管 API，就自己上 [OpenAI Whisper](whisper.zh.md) 或云端 ASR。
- **素材很大而磁盘不够。** 默认路径是写出**新文件**而不是原地剪；只想知道会剪掉哪些片段时，先跑 `--preview`。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [FFmpeg](ffmpeg.zh.md) | ✅ | 如果你已经在写滤镜图、只需要**检测**静音，选 FFmpeg 的 `silencedetect`；如果你要的是「连切点和输出一起搞定」，选 Auto-Editor，因为 `silencedetect` 只打印时间戳，把它们变成片段和一次编码仍是你的活。 | FFmpeg 是万能引擎、对你的剪辑不持任何观点；Auto-Editor 是有观点的封装，还能产出 Premiere / Resolve / FCP 一类的工程文件。 |
| [MoviePy](moviepy.zh.md) | ✅ | 如果剪辑是程序化的、你清楚要什么时间线，选 MoviePy；如果**时间线本身就是未知量**（静音在哪），选 Auto-Editor，因为 MoviePy 执行你的决定，Auto-Editor 从素材里推导这个决定。 | MoviePy：Python API、进程内、到处能渲染；Auto-Editor：二进制 CLI，自带标签/动作模型并能交棒给 NLE。 |
| [OpenAI Whisper](whisper.zh.md) | ✅ | 如果只要转写，选 Whisper（或云端 ASR）；如果转写是**用来剪的输入**，选 Auto-Editor，因为 `auto-editor whisper … --format srt` 加 `--edit word:question` 能按说话内容剪，而 Whisper 自己做不到。 | Whisper：顶尖 ASR，没有剪辑模型，一切靠你写脚本；Auto-Editor：内置 GGML/Parakeet 一条路加剪辑模型，但不做说话人分离，质量旋钮也只有内置模型那几个。 |
| [Concat](../video-editing/concat.zh.md) | ✅ | 如果需要人来看和调整切点，选 Concat 或商业 NLE；如果第一遍是机械活、只有收尾需要人工，选 Auto-Editor，因为 Concat 是你要去操作的完整 AGPL 编辑器，而 Auto-Editor 是你脚本里的一道前置工序。 | Concat：可交互、全平台渲染、还是 beta；Auto-Editor：一次成型、没有界面，并且喂给你已经在用的编辑器。 |
| Descript（闭源 SaaS） | 未收录 | 如果在浏览器里按文稿剪辑、还要团队审阅，且不在意素材上云，选 Descript；如果素材不能离开本机或必须跑在 CI 里，选 Auto-Editor，因为 Descript 绑账号、按席位收费且闭源。 | Descript：成熟的文本剪辑与协作；Auto-Editor：离线、免费、可脚本化，但没有转写界面和审阅流程。 |

## 技术栈

- 用 **Nim** 写成（`src/` 下 71 个 `.nim` 文件），交付形态是一个 CLI 二进制，外加由 `docs/` 生成的文档站。
- 剪切/编码走自带的 FFmpeg 写出层；转写用 whisper.cpp / GGML 模型（Whisper、NVIDIA Parakeet GGUF），macOS 26+ 可用系统自带的 Apple 转写。
- 标签/动作模型：整数标签（`0` 静音、`1` 有效，`--edit:N` / `--when:N` 最多到 255），每个标签配 `cut`、`nil`、`speed:8` 这类动作。
- 交给剪辑软件的是有文档的时间线格式（站上有 v1/v2/v3 三版说明），另有 Premiere、Resolve、Final Cut Pro、Shotcut、Kdenlive 与 `clip-sequence` 导出器。
- 仓内自带 4 个一方 agent skill（`auto-editor`、`-effects`、`-export`、`-transcribe`），可用 `npx skills add WyattBlue/auto-editor` 安装。
- CI：`.github/workflows/build.yml` 与 `smoke.yml`。

## 依赖

- **二进制安装（推荐）：** 官方未签名 release 二进制；Homebrew（`brew install auto-editor`，其依赖会带上 `ffmpeg`、`ggml`、`whisper.cpp`）；Arch AUR（`yay -S auto-editor`）。
- **源码构建：** Nim + nimble，外加 cmake、meson、ninja；静态构建用 `nimble makeff && nimble make`。
- **转写（可选）：** 自己下载的 GGML 模型文件（如 `ggml-medium.en.bin`），或 Apple 自带转写；麦克风录制用 `:mic`，只需要一个输入设备。
- **URL 输入（可选）：** `PATH` 上有一个 `yt-dlp` 二进制。
- 不需要服务器、数据库、GPU、账号或联网；pip 渠道已停止发布。

## 运维难度

**运行很低，保持版本较新是低到中。** 没有要部署或监控的东西——一个二进制、没有常驻进程、没有状态。摩擦在打包而不在运行：release 二进制未签名（macOS 会出现「未知开发者」提示与 Gatekeeper 阻拦），PyPI 渠道已死，所以老运维手册里的 `pip install auto-editor` 会装到一个过期版本，源码构建则要 Nim 工具链和 FFmpeg 开发库。开转写还要额外准备本地模型文件。建议照着生产要用的那个版本和阈值跑一次验证，因为「哪个阈值合适」取决于你的录音现场，不取决于工具。

## 健康度与可持续性

- **维护（雷达 A，2026-09-21）：** 稳定得少见。创建于 2020-04-30，累计 2,531 次提交，最后推送 2026-09-19，release 31.4.2 → 31.5.0 → 31.6.0 分别落在 2026-07-31 / 08-13 / 09-06；**open issue 为 0**，且 Issues 与 Discussions 都开着，近期 4 个合格 issue 的首次响应中位数约 2.5 小时（雷达 A），CI 有 `build.yml` 与 `smoke.yml`。
- **治理 / bus factor（雷达 C）：** 15 位贡献者里作者 `WyattBlue` 占 99.1% 的提交——教科书式的单点故障，缓解因素是六年半持续的发布纪律。背后没有基金会、公司或商业实体。[推断] Nim 代码库会缩小顺手贡献者的池子，所以 bus factor 不太可能自己改善。
- **背书与 Lindy（雷达 A）：** 本批里 Lindy 位置最好的一个——已有 2,335 天且仍在发布，正是本索引奖励的那条先验；时间线格式文档从 v1 写到 v3，说明核心已经形式化，而不是不断堆补丁。
- **采用与生态（雷达 D）：** 约 5.3k stars / 655 forks，进了 Homebrew 和 AUR，另有在线版/桌面版产品与仓内 4 个 agent skill——关注度已经转成了分发渠道，而不只是点赞。这个轴分数低是注册表的副产品：已停发的 PyPI 包每月仍有 18,055 次下载，而它解析到的是过期的 29.3.1，所以按包指标衡量的采用度低估了真实使用。
- **风险信号（雷达 A）：** 仓库是 **Unlicense**（公有领域），但 README 说明 release **二进制**可能带其他开源许可，在线版/桌面版的自有素材另按专有许可发布——不要假设整条链都是公有领域。实际风险是 pip 渠道停发：旧自动化会一直装到落后发布线近一年的版本。

## 存疑（未验证）

- [未验证] 本页没有实际执行过任何命令：所有命令来自 2026-09-21 读到的 README、`https://auto-editor.com/docs/cookbook` 与 `https://auto-editor.com/installing`。
- [未验证] star / fork / 提交 / issue 数是 2026-09-21 的 GitHub API 时点值，在这种活跃仓上变化很快。
- [未验证]「pip 渠道已停发」来自安装页，而注册表仍在提供 `auto-editor` 29.3.1 且上月约 1.8 万次下载——这组合只是指标快照，`pip install auto-editor` 现在是否仍能成功没有实测。
- [未验证] 转写相关说法（「Parakeet 最准」）与各后端行为（Apple 模型需要下载、语言自动识别受限）出自仓内 skill 文档，不是本页跑出的基准测试。
- [未验证] 4 个内置 skill 在各 harness（Claude Code / Codex / Cursor / Kimi）里的触发保真度未测；只核实了 `skills/` 目录里的存在性。
- [推断] 把 open issue 为 0 读作分流很快，而不是零缺陷——issue 功能是开着的，所以这个快照下队列确实是空的。
- [未验证] release 二进制的许可差异与在线版专有素材的边界都是 README 的说法，本页没有做许可审计。
- [未验证] 文档所列支持媒体之外的容器，以及阈值选错导致误标时的行为，都没有实测；阈值的正确性取决于你的现场底噪，不取决于工具。
