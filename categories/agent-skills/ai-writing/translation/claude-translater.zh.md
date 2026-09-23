---
name: claude_translater
slug: claude-translater
repo: https://github.com/wizlijun/claude_translater
category: translation
tags: [book-translation, claude-code, shell, calibre, pptx]
language: Python
license: NOASSERTION
maturity: v2.1 per README badge, coasting, 35 stars (as of 2026-09)
last_verified: 2026-09-18
type: tool
upstream:
  pushed_at: 2026-07-14T06:13:15Z
  default_branch: main
  default_branch_sha: 772e639b21be7b82ab2847c84dd86eb87f219f7f
  archived: false
health:
  schema: 1
  computed_at: 2026-09-23T07:31:46Z
  overall: D
  overall_score: 1.25
  scored_axes: 4
  applicable_axes: 6
  capped: true
  cap_reason: "source-available/no-license: NONE"
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 71
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: C
      raw:
        repo_age_days: 439
        last_commit_age_days: 71
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: E
      raw:
        spdx_id: NONE
        permissiveness: source_available
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# claude_translater

一个 shell 脚本＋Claude CLI 的文档翻译工具箱：PDF/DOCX/EPUB 经 Calibre HTMLZ 转成 Markdown 分块，由 Claude CLI 逐步骤翻译，再合并回 HTML；另有一个独立脚本翻译 PPTX。它是 [translate-book](translate-book.zh.md) 的直接灵感来源。

![claude_translater — 健康度雷达](../../../../assets/health/claude-translater.zh.svg)

## 何时使用

你是一个 Claude Code 用户，想要“能跑就行”的最简方案：clone 一个仓库，跑 `./translatebook.sh book.pdf`，让七步 shell 流水线（Calibre 转换→分块→Claude CLI 翻译→合并→HTML→目录→格式转换）干完剩下的活——不装 skill，不学 manifest schema，不需要理解编排规则。而且你手上还有一份 PPT 要翻，这是那些更 fancy 的继任者不碰的：`pptxtrans.py` 通过 python-pptx 处理 PPTX。

你选它而不是 [translate-book](translate-book.zh.md)，只发生在你特别想要几分钟就能读完、随手可改的透明 shell 脚本，或者确实需要 PPTX 翻译时；作为交换，你放弃了并行、断点续跑和术语一致性机制。你选它而不是 [bilingual_book_maker](../../../reading-tools/bilingual-book-maker.zh.md)，是因为你想直接消耗自己的 Claude Code 订阅，而不是去配 API key。

## 何时不用

- **你想要活跃维护的项目。** 最后一次提交是 2026-07-14，全部历史约 17 个 commit，仓库里没有 LICENSE 文件（只有 README 徽章声称 MIT，截至 2026-09-18）——任何长期使用都用 [translate-book](translate-book.zh.md)，它是这条流水线重构后、仍活跃维护的继任者。
- **你要整本书的速度。** 这条流水线驱动 Claude CLI 逐步串行执行，没有并行 subagent、没有断点续跑、没有 manifest 校验。翻书请用 translate-book（并行＋可续跑）或 bilingual_book_maker（可脚本化 API 调用）。
- **你不在 Claude 生态里。** 如果你的 runtime 是 Codex/OpenClaw，或者你想调 OpenAI/DeepL/本地模型，用 bilingual_book_maker——这个工具箱硬绑 Claude CLI。
- **你要跨章节术语一致。** 没有术语表、没有相邻上下文、没有选择性重翻；长书里的专有名词必然漂移。用 translate-book。
- **你要拿去做产品底座。** 没有 LICENSE 文件意味着除了查看代码你没有被授予任何权利——把它当只读参考，基于 MIT 的 translate-book 构建。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [translate-book](translate-book.zh.md) | ✅ | 任何真实的翻书任务都选 translate-book：它把同一条 Calibre→分块→翻译流水线重构成了可移植 skill，带并行 subagent、断点续跑和术语反馈环。 | claude_translater 给你透明、随手可改的 shell 脚本和一个 PPTX 翻译器；translate-book 给你维护中的并行一致版——但需要支持 skill 的 harness，且不覆盖 PPTX。 |
| [bilingual_book_maker](../../../reading-tools/bilingual-book-maker.zh.md) | ✅ | 要有发布、有断点续跑、多模型后端、双语输出的打包 CLI 时选 bilingual_book_maker；只有当你就要 Claude CLI 原生的极简时才选 claude_translater。 | bilingual_book_maker 更老、MIT、有 PyPI 包、适合无人值守；claude_translater 是单人的薄脚本集，无许可无发布流程，但只要你已有 Claude Code 就零 API key 配置。 |
| [Baoyu Skills](../content-production/baoyu-skills.zh.md) | ✅ | 在更大的内容工作流里翻文章／文本时选 Baoyu Skills；只有要 shell 方式的文件级书籍／PPTX 翻译时才选 claude_translater。 | Baoyu 的翻译 skill 是维护中的多模式文本翻译（带术语表），不是文件流水线；claude_translater 端到端处理 PDF/DOCX/EPUB/PPTX 文件，但已不维护且仅限 Claude。 |

## 技术栈

- **Bash＋Python 3.6+**——`translatebook.sh` 编排编了号的步骤脚本（`01_convert_to_htmlz.py` … `07_generate_formats.py`）
- **Calibre（`ebook-convert`）**——统一的 PDF/DOCX/EPUB→HTMLZ 转换路径
- **Claude CLI**——实际执行翻译，由脚本驱动
- **pypandoc**——HTML↔Markdown 转换；**python-pptx**——独立的 PPTX 翻译器
- **HTML 模板**——`template.html`／`template_ebook.html` 用于最终输出

## 依赖

- **Claude CLI（Claude Code）**——硬依赖，所有翻译都走它
- **Calibre**——输入转换和格式输出都要用
- **Python 包**——`python-docx PyMuPDF ebooklib beautifulsoup4 lxml markdown Pillow pdf2image pypandoc`（脚本自动安装），PPTX 额外要 `python-pptx`
- 无数据库、无服务；一切都在本地 temp／output 目录里跑

## 运维难度

**低。** clone、装好 Calibre＋Claude CLI、跑一个 shell 脚本。没有打包、没有发布流程、看不到测试套件；仓库就是一个平铺的脚本集合（还包括好几个实验性的 `epub_to_pdf_*` 变体），出问题时靠读源码调试。多项目并行时 temp 目录识别曾是踩过的坑（见 README 的 v2.1 说明），所以每个目录里串行跑。

## 健康度与可持续性

- **维护**：趋于安静——创建于 2025-07-11，最后提交 2026-07-14，全部约 17 个 commit，0 个 open issue（截至 2026-09-18）。看起来像个人工具到了“自己够用”的状态 [推断]。
- **治理／bus factor**：单人仓库（`wizlijun`）；无贡献流程、无 CI、除了 README 版本徽章外无发布。
- **背书与寿命（Lindy）**：约 14 个月历史但体量极小（35 star、11 fork）；它的历史意义在于 [translate-book](translate-book.zh.md) 明确致谢它为灵感来源，并由活跃维护者把这个想法接了下去。
- **采用与生态**：采用极少；中文 README；无任何包分发——只能 clone 即用。
- **风险信号**：**仓库根目录没有 LICENSE 文件**，尽管 README 徽章写着 MIT（2026-09-18 经仓库文件列表核实）——法律上默认保留所有权利；不要二次分发或拿来做产品。此外无换许可历史、无 CLA。

## 存疑（未验证）

- [未验证] README 里的“v2.1”版本只存在于徽章／更新说明里——没有 git tag 或 release 可以确认它对应什么。
- [未验证] 自动清理 Calibre 标记、页码和杂散标签的能力来自 README 自述；对任意 PDF 的健壮性此处未实测。
- [未验证] `translatebook.sh` 自动安装 Python 依赖时可能完全没有锁版本——`pypandoc`／`PyMuPDF` 的版本漂移可能弄坏流水线 [推断]。
- [推断] 仓库里大量平铺的变体脚本（`epub_to_pdf_converter.py`、`epub_to_pdf_working.py`……）说明是试错式开发；预期存在死代码路径。
- [推断] 0 open issue＋35 star，真实使用量很可能非常小；把“在作者自己的文档上能跑”当作唯一被验证过的范围。
