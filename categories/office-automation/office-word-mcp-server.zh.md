---
name: Office-Word-MCP-Server
slug: office-word-mcp-server
repo: https://github.com/GongRzhe/Office-Word-MCP-Server
category: office-automation
tags: [mcp, docx, word, openxml, python, ai-agent, document-generation, archived, office]
language: Python
license: MIT
maturity: "v1.1.11, ARCHIVED 2025-12-31 (last push 2025-12-31); 2.1k stars / 286 forks / 66 open issues, created 2025-03-25 (API-verified), ~9-month lifespan"
last_verified: 2026-09-18
type: service
upstream:
  pushed_at: 2025-12-31T13:23:05Z
  default_branch: main
  default_branch_sha: a3bbbb6d6167e68cf855d73ef7dc6cd8cfbfedba
  archived: true
health:
  schema: 1
  computed_at: 2026-09-22T16:48:00Z
  overall: C
  overall_score: 1.5
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: true
        last_commit_age_days: 265
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: E
      raw:
        median_ttfr_hours: null
        qualifying_issues: 0
        band: default
        window_offset_days: 10
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: office-word-mcp-server
        dependent_repos_count: 0
        downloads_last_month: 44626
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
        tier_source: registry
        archived: true
    longevity:
      grade: E
      raw:
        repo_age_days: 547
        last_commit_age_days: 265
        cohort: service
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 4
        top1_share: 0.455
        top3_share: 0.909
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Office-Word-MCP-Server

一个 MCP server，向 LLM 客户端暴露约 55 个 Word 文档工具——star 数最高的 Word MCP server，且已**被作者于 2025-12-31 归档**。把它当设计参考，不要当依赖。

![Office-Word-MCP-Server — 健康度雷达](../../assets/health/office-word-mcp-server.zh.svg)

## 何时使用

你在维护一个既有 LLM 集成，它已经绑定了这个 server 的 tool schema，而拆掉它的成本高于运行无人维护代码的风险。这是现在唯一该选它的理由。历史上的理由不同，但值得记录下来：你想让一个 LLM 客户端（Claude Desktop、Cursor，或任何支持 MCP 的东西）通过标准化 tool 接口创建和编辑 `.docx`，而不用自己写胶水代码；而这个 server 曾提供 MCP 车道里最广的 Word 工具面——跨 document、content、format、comment、footnote、protection 六个模块约 55 个工具（2026-09-18 在 `word_document_server/tools/` 中验证），其中包括一套体量可观的**脚注／尾注实现**（`footnote_tools.py`，25 KB），而这正是 [python-docx](python-docx.zh.md) 自 2014 年功能请求以来仍然缺的东西。要新建的话：agent 需要三个 Office 格式加渲染回看闭环就选 [OfficeCLI](officecli.zh.md)；只需要 Word 且希望底下是活依赖，就直接调 [python-docx](python-docx.zh.md)。

## 何时不用

- **任何新项目** → 仓库已**归档**（GitHub `archived: true`，最后 push 2025-12-31，API 2026-09-18 验证）。没有修复、没有依赖升级、没有安全响应。要维护中的、面向 agent 的 CLI 请用 [OfficeCLI](officecli.zh.md)，或者自己封装 [python-docx](python-docx.zh.md)。
- **需要 Word→PDF 的 Linux 或 headless 部署** → manifest 声明了 `docx2pdf>=0.1.8`，而它自己在 PyPI 上的简介写着 *"Convert docx to pdf on Windows or macOS directly using Microsoft Word (must be installed)"*——Windows 上走 `win32com`，macOS 上走 JXA／AppleScript（2026-09-18 验证）。server 本身能跑在随仓库提供的 `python:3.11-slim` Docker 镜像里，但那一个工具在那里不可能工作。改用 LibreOffice headless，或 [OfficeCLI](officecli.zh.md) 的 HTML／PNG 路径。
- **Excel 或 PowerPoint** → 只有 Word。作者的姊妹项目 `Office-PowerPoint-MCP-Server`（1,852 star）**同样已归档**（2025-12-31），且从未有过 Excel 等价物。三个格式都要请用 [OfficeCLI](officecli.zh.md)，或按格式分别用 [XlsxWriter](xlsxwriter.zh.md)／[python-pptx](python-pptx.zh.md)。
- **你需要经过审计的行为** → 仓库只有两个测试文件（`tests/test_convert_to_pdf.py`，3.5 KB；`test_formatting.py`，3.3 KB），对应约 55 个工具和一个 30 KB 的 `main.py`。覆盖是演示性的，不是安全网。优先选 [python-docx](python-docx.zh.md)，它背后有 13 年的下游生产使用。
- **你想要小的依赖面** → 它会拖进 `python-docx`、`fastmcp`、`msoffcrypto-tool`、`docx2pdf`，**以及作为运行时依赖的 `pytest>=8.4.2`**（2026-09-18 在 `pyproject.toml` 中验证）——这是个包装瑕疵，而且因为仓库已归档，永远不会被修。直接调 [python-docx](python-docx.zh.md) 只需要两个依赖。
- **你需要文档保护或数字签名可信** → README 宣称支持密码保护、受限编辑，以及「数字签名……验证文档真实性与完整性」。[未验证] OOXML 数字签名的**创建**不是 Python 库能在没有证书链和 Word 自身签名 part 语义的情况下忠实做到的事；在依赖它之前请先对照你的合规要求验证。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [OfficeCLI](officecli.zh.md) | ✅ | 任何新工作都选 OfficeCLI：它在维护中、覆盖 Word 加 Excel 加 PowerPoint、不需要安装 MS Word，还多一个渲染回看闭环；只有当既有集成已经绑定这个 server 的工具名时才选它。 | OfficeCLI 是 CLI，所以 MCP 客户端需要一层封装或用它内置的 MCP 模式；这个 server 从第一天起就是 MCP 原生的，但已归档、只有 Word，且它的 PDF 工具需要真实安装 Word。 |
| [python-docx](python-docx.zh.md) | ✅ | 选 python-docx 并自己写一层薄 MCP——这个 server **就是**那个模式，只是被冻结在时间里了，而 python-docx 是它活着的上游依赖（`python-docx>=1.1.2`）。 | 你得到一个仍在维护的基础和对 tool schema 的完全控制权；代价是失去约 55 个现成工具，包括那套脚注／尾注实现——你得自己从 `footnote_tools.py` 移植。 |
| [Pandoc](../markdown-tools/pandoc.zh.md) | ✅ | 源是 Markdown、docx 只是单向导出时选 Pandoc；LLM 必须迭代式就地编辑一份已有文档时选 Word 编辑 server——那是 Pandoc 完全做不到的。 | Pandoc 一次调用、维护活跃、没有对象模型；这个 server 曾提供通过自然语言工具调用做就地编辑的能力，但现已无人维护。 |
| [MarkItDown](../document-parsing/markitdown.zh.md) | ✅ | 方向是 .docx → Markdown 供 LLM 摄取时选 MarkItDown；方向是 LLM 意图 → .docx 时选 Word 编辑 server。方向相反，而且 MarkItDown 在维护中。 | MarkItDown 只读且按设计丢弃格式；这个 server 保留 OOXML 模型并能写入，但已归档。 |

## 技术栈

Python `>=3.11`，MCP 协议层构建在 `fastmcp>=2.8.1` 上，所有 OOXML 操作走 `python-docx>=1.1.2`（2026-09-18 在 `pyproject.toml` 中验证）。`msoffcrypto-tool>=5.4.2` 处理加密文档，`docx2pdf>=0.1.8` 处理 Word→PDF，而 `pytest>=8.4.2` 被声明为**运行时**依赖。代码结构：`word_document_server/main.py`（30 KB，约 55 个工具定义，49 处脚注引用），外加一个 `tools/` 包，拆成 `content_tools.py`（19.6 KB）、`format_tools.py`（44.2 KB）、`footnote_tools.py`（25 KB）、`protection_tools.py`（10.6 KB）、`extended_document_tools.py`（8.2 KB）、`document_tools.py`（7.8 KB）和 `comment_tools.py`（5 KB）。用 hatchling 打包；入口点 `word_mcp_server`。分发走 `uvx` 或 `pip`；一个 Smithery 生成的 `Dockerfile`（`python:3.11-slim`）和 `smithery.yaml` 支持托管部署，另有 `RENDER_DEPLOYMENT.md`。默认分支 `main`。

## 依赖

一个 Python 3.11+ 运行时和一个支持 MCP 的客户端（Claude Desktop、Cursor，或你自己的）。仅就 PDF 转换工具而言：**必须安装 Microsoft Word**，且**只支持 Windows 或 macOS**——`docx2pdf` 在 Windows 上通过 `win32com`、在 macOS 上通过 JXA 驱动 Word，所以那个工具在 Docker／Linux 路径下不可用。无数据库、无 GPU、自身不提供网络服务（stdio MCP 传输）。因为仓库已归档，这些依赖现在全都失去了对未来上游破坏的锁定保护：`fastmcp` 或 `python-docx` 发一个大版本就可能把它打断，且没有上游修复可用。

## 运维难度

**跑起来低，养起来高。** 运行是琐碎的：在 MCP 客户端配置里写 `uvx --from office-word-mcp-server word_mcp_server`，或构建随仓库提供的 Docker 镜像；stdio 传输意味着没有端口、没有鉴权、不需要看护。养才是问题。仓库已归档，所以 `fastmcp`、`python-docx`、`msoffcrypto-tool` 或 `docx2pdf` 里出 CVE 都没有补丁路径；66 个 issue 开着且会一直开着；而把 `pytest` 声明为运行时依赖意味着你的生产安装会拖进一个测试框架。如果你还是要采用，请 fork 它、用 lockfile 锁死每个依赖（`uv.lock` 已提交，85 KB），并把那个 fork 当作永久属于你。要一条维护中的、agent 人机工程相当的路径，用 [OfficeCLI](officecli.zh.md)（它有内置 MCP server 模式），或者用 [python-docx](python-docx.zh.md) 自己封一个约 200 行的 fastmcp server。

## 健康度与可持续性

- **维护：已死，已验证** —— GitHub `archived: true`；最后 push 2025-12-31；最新 tag v1.1.11；约 9 个月生命周期里（创建于 2025-03-25）默认分支共 69 个 commit。66 个 issue 开着且无关闭路径（API 2026-09-18 验证）。
- **治理：作者主导，随后弃置** —— `GongRzhe` 提交 69 个中的 31 个（45%），`KaliGong` 9 个，`jamesmehorter` 5 个，之后是长尾。按占比算，社区参与度高于 [OfficeCLI](officecli.zh.md)，但绝对工作量少得多：69 个 commit 对 6,128 个。
- **背书与寿命：决定性信号** —— 作者**批量归档了他整个 MCP 组合**：`Office-PowerPoint-MCP-Server`（1,852 star，2025-12-31 归档）、`Gmail-MCP-Server`（1,164 star，2025-08-06 归档）、`terminal-controller-mcp`（97）、`Human-In-the-Loop-MCP-Server`（163）、`Quickchart-MCP-Server`（159）、`A2A-MCP-Server`（148）、`opencv-mcp-server`（111）、`Office-Visio-MCP-Server`（86）、`APIWeaver`（49）等等——约 15 个仓库在 2025-05 至 2025-12 之间被归档（API 2026-09-18 验证）。[推断] 这是退出这个领域，不是针对单个项目的决定，所以不应规划任何复活。
- **年龄／Lindy：两半都不成立** —— 9 个月大且不活跃。先验在这里给不出任何东西；对照它仅仅包装了一下的 [python-docx](python-docx.zh.md)（13 年，仍在发版）。
- **采用度：真实但搁浅** —— 2,106 star／286 fork 让它成为 star 数最高的 Word MCP server，而且当有人问「Word MCP」时，agent 依然会把它翻出来。这正是它被收录的原因：star 数跑在了维护状态前面，只按 star 选型的 agent 会选中一个死项目。
- **风险标记** —— 归档且有 open issue；`pytest` 被声明为运行时依赖；`docx2pdf` 给一个被宣传的功能加上了「必须装 Microsoft Word + 只能 Windows／macOS」的硬地板；MIT 许可，无 relicense 历史，无 open-core 功能门。归档本身就是那个风险标记：任何传递依赖都不会再得到安全响应。

## 存疑（未验证）

- [未验证] 确切的工具数量（约 55）——由统计 `word_document_server/main.py` 里的工具定义模式得出；MCP 注册列表未在运行时枚举。
- [未验证] 宣传的「数字签名……验证文档真实性与完整性」产出的签名能否被 Microsoft Word 认作有效。OOXML 签名创建需要证书链和 Word 的签名 part 语义；本次只观察到 README 主张和 `protection_tools.py`（10.6 KB），未执行。
- [未验证] 脚注／尾注实现能否在真实 Word 中正确往返——`footnote_tools.py` 体量可观（25 KB），README 也记录了脚注转尾注和样式定制，但本次未做基于固定样本的验证。
- [未验证] 在 Docker／Linux 路径下调用时，`docx2pdf` 是干净失败还是挂起或损坏输出——「仅 Windows／macOS」这一要求已从 docx2pdf 自己的 PyPI 元数据验证，但它在本 server 内部的失败形态未实测。
- [推断] 作者退出 MCP 领域是由约 15 个姊妹仓库的归档日期和 star 数推断的；未找到公开的意图声明。
- [未验证] 是否存在某个维护中的社区 fork，会比归档的原仓库更适合采用——本次评审未系统检索。
- [未验证] `fastmcp` 协议层对当前 MCP 客户端版本的运行时兼容性；`fastmcp>=2.8.1` 是一个开放区间且仓库已归档，所以兼容性漂移未被测量。
