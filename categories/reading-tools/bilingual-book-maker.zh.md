---
name: Bilingual Book Maker
slug: bilingual-book-maker
repo: https://github.com/yihong0618/bilingual_book_maker
category: reading-tools
tags: [book-translation, epub, bilingual, cli, litellm]
language: Python
license: MIT
maturity: v1.2.1, active, 9.8k stars (as of 2026-09)
last_verified: 2026-09-18
type: tool
upstream:
  pushed_at: 2026-09-14T07:15:37Z
  default_branch: main
  default_branch_sha: 3f7fc1e21687146e7e3de1d6facdb56960b993a0
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:58:39Z
  overall: A
  overall_score: 3.8
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
        last_commit_age_days: 3
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 32.4
        qualifying_issues: 6
        band: relaxed_solo
        window_offset_days: 1
        source: pr
        inferred: false
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: A
      raw:
        repo_age_days: 1301
        last_commit_age_days: 3
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 21
        top1_share: 0.333
        top3_share: 0.802
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    adoption: { reason: ambiguous }
---

# Bilingual Book Maker

一个 Python CLI：直连 LLM 或机器翻译 API，把 epub/txt/md/srt/pdf 文件做成双语对照的书——支持 OpenAI/Anthropic 格式端点、Gemini/Qwen/Groq/xAI/LiteLLM、本地 Ollama、Codex 订阅，以及传统 MT 引擎——带断点续跑，有 PyPI 包（`bbook-maker`）。

![Bilingual Book Maker — 健康度雷达](../../assets/health/bilingual-book-maker.zh.svg)

## 何时使用

你是一名读者，手上有一本 EPUB（或 txt/md/srt/pdf），想读双语对照版——原文和译文逐段并排——而且你要的是一个 boring、可脚本化的工具，不是一场 agent 会话。你 `pip install bbook_maker`，一条命令加一个 API key（或本地 Ollama 模型、或 Codex 额度）指向文件，它就把整本书流式翻完，`--resume` 兜住中断，最后吐出 `${book_name}_bilingual.epub`。它能进 cron、能批量跑目录、能进 CI——这是 agent 编排式流水线做不到的。

你选它而不是 [translate-book](../agent-skills/ai-writing/translation/translate-book.zh.md)，是因为你要无人值守的 CLI、双语对照输出、以及自由选后端（包括便宜的 MT 引擎），而不是一个必须活在 coding-agent harness 里、只产出单语成书的 skill；你选它而不是 [Read Frog](read-frog.zh.md) 这类浏览器扩展，是因为你要的是一个能发到 Kindle 的**文件**，不是网页上的原地覆盖层。

## 何时不用

- **你要把跨章节术语一致性当一等公民。** 它是段落流式翻译，可选会话上下文（`--use_context session`，按 token 预算压缩）——没有人工整理的术语表、没有逐块术语注入、没有选择性重翻。长书的专有名词漂移是主要痛点时，用 [translate-book](../agent-skills/ai-writing/translation/translate-book.zh.md)。
- **你想让翻译默认跑在 coding-agent 订阅上。** 它的原生路径是 API key（虽有 Codex 路由）。如果你唯一的“LLM 入口”是 Claude Code/Codex harness，用 translate-book 或 [claude_translater](../agent-skills/ai-writing/translation/claude-translater.zh.md)。
- **你只读网页。** 浏览器内阅读加双语覆盖，用 [Read Frog](read-frog.zh.md) 或 [FluentRead](fluentread.zh.md)——不需要文件流水线。
- **你的输入是复杂 PDF。** PDF 输入会退化为双语 `.txt`（会尝试建 EPUB 但可能失败），版式信息丢失。PDF 优先且在意 DOCX/EPUB/PDF 输出保真时，用基于 Calibre 的 translate-book。
- **你没有素材的翻译权利。** 项目自己的免责声明把用途限定在你有权翻译的作品上——受版权保护的商业电子书，请用有授权的翻译服务（未收录，非 repo）。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [translate-book](../agent-skills/ai-writing/translation/translate-book.zh.md) | ✅ | 整书的术语／代词一致性是决定性需求、且你活在 coding-agent harness 里时选 translate-book；要可脚本化的 CLI 批量跑、双语输出、后端自由时选 Bilingual Book Maker。 | BBM 更老（2023）、有打包、MIT、能无人值守地跑任何 OpenAI/Anthropic/MT 端点；translate-book 多了术语表＋相邻上下文机制和多格式输出，但要装 Calibre、Pandoc 和一个交互式 agent。 |
| [claude_translater](../agent-skills/ai-writing/translation/claude-translater.zh.md) | ✅ | 几乎任何情况都选 Bilingual Book Maker 而不是 claude_translater：同是“翻一本书的文件”，但它有许可、有打包、能续跑、还在持续发布。 | claude_translater 仅剩的优势是 Claude CLI 原生的极简和一个 PPTX 翻译器；BBM 覆盖更多输入格式，有真正的发布流程和断点续跑。 |
| [Read Frog](read-frog.zh.md) | ✅ | 阅读发生在浏览器里、要沉浸式覆盖层时选 Read Frog；要一本翻完的双语电子书文件时选 Bilingual Book Maker。 | Read Frog 在网页／字幕上原地翻译（BYOK provider），永远不产出 EPUB；BBM 永远不碰网页。 |
| [FluentRead](fluentread.zh.md) | ✅ | 中文优先的浏览器内翻译、多引擎时选 FluentRead；自有电子书文件和字幕（srt）翻译时选 Bilingual Book Maker。 | FluentRead 活在浏览器标签页里；BBM 是产文件的本地 CLI——两者解的是“跨语言阅读”的两种不同形态。 |

## 技术栈

- **Python 3.10+**——核心 CLI（`make_book.py`），以 `bbook-maker` 发布在 PyPI
- **OpenAI/Anthropic 兼容客户端层**——外加 LiteLLM 集成做后端无关路由
- **ebooklib 式 EPUB 处理**——在 JSON-schema 端点上做标签级分类（`skip`/`translate` 判定）
- **传统 MT 引擎适配器**——Google、彩云、DeepL（含免费版）、腾讯、自定义 API
- **GitHub Actions CI**——用样例书做翻译测试（`make_test_ebook`）

## 依赖

- **Python 3.10+**，`pip install -r requirements.txt`（或 `pip install -U bbook_maker`）
- **一个翻译后端**：OpenAI/Anthropic 格式端点的 API key、Gemini/Qwen/Groq/xAI、LiteLLM、某个 MT 引擎、本地 Ollama 服务，或 Codex CLI 额度
- 托管后端需要**联网或代理**（本地 Ollama 不需要）
- 不需要 Calibre、不需要 Pandoc、不需要数据库

## 运维难度

**低。** 一条 CLI 命令；状态只存在生成的 `${book_name}_bilingual.*` 文件和 `--resume` 簿记里，中断后不重翻接着跑。运维面就是凭据管理（`--key`、`--api_base` 或 `bbm_providers.json`）和挑一个上下文窗口配得上 `--use_context session` 的模型。没有要部署或常驻的东西。

## 健康度与可持续性

- **维护**：活跃——创建于 2023-03-02，最新发布 v1.2.1（2026-09-14），有 tagged release（v1.1.0、v1.2.0、v1.2.1），CI 持续翻样例书（截至 2026-09-18）。
- **治理／bus factor**：单一主导维护者（`yihong0618`）加很广的 contributor 面（1286 fork）；可核实的是他还维护着多个热门 OSS 项目（xiaogpt 约 6.9k star、running_page 约 4.5k star），有不弃坑的记录 [推断]。
- **背书与寿命（Lindy）**：约 3.5 年历史且仍在发版——本对比组里最强的 Lindy 信号；无组织背书，但“年龄×仍活跃”两条都成立。
- **采用与生态**：9.8k star、PyPI 分发、文档化的 provider 矩阵、免责声明和许可姿态都显出维护成熟度。
- **风险信号**：MIT、无换许可历史。持续性维护税来自后端 API 漂移（OpenAI/Anthropic 格式变化）；传统 MT 引擎（Google/DeepL）的翻译质量上限由那些服务决定，不由本工具决定。

## 存疑（未验证）

- [未验证] 各格式的保真度（尤其 PDF→EPUB 回退和 srt 时间轴保留）来自 README；复杂输入此处未实测。
- [未验证] EPUB 标签分类行为（“skip/translate 判定”）只对能持有会话的端点生效；纯 MT 引擎只翻 `p` 标签，诗歌类内容可能被漏掉——各端点的实际覆盖未测。
- [未验证] 每本书的成本和耗时完全取决于所选后端／模型；官方无基准数据。
- [推断] 会话上下文模式（`--use_context session`）改善局部连贯，但默认 8k 的压缩窗口远小于一本书——在长作品上替代不了人工整理的术语表。
- [未验证] Codex 订阅路由的速率限制和条款是否适合批量翻书，未独立确认。
