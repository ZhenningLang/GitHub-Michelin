Audience:   P3 实现 agent
Scope:      第二段 20 对旧页的冻结复核清单 / Non-scope: 不在 phase 01 复核这些页面
State:      frozen (algorithmic)
Genre:      G-PLAN
Code-Root:  /Users/zhenninglang/Projects/oss-atlas-wt-sections
Prefixes:   none

# 章节契约 v2 · 20 对抽样清单

固定基线：`25b351c6b38523019a288509d45b4063c37a513b`。所有“原日期”和类型均来自该提交，后续更新页面不重新选样。
本表由已批准算法冻结，不是 owner 对具体项目的单独审批。复算脚本位于 phase 目录，随本次 workspace 一并归档；清理 workspace 前应保留脚本。下方算法正文和固定提交仍是可独立复算的依据。

复算命令（在待验收 checkout 根执行，脚本只读 git 基线及本清单）：

```bash
python3 /Users/zhenninglang/Projects/oss-atlas-wt-sections/.long-loop/20261013_section-contract-v2/phases/01_contract/sample_pages.py --root . --check docs/specs/section-contract-v2/sample-pages.md
```

算法：全部英文页按原 `last_verified` 升序，同日按路径字典序；排除 screenshot-to-code，依次取满 20 对，每个顶层分类最多两对，不排除 skill-pack。若 tool、library、app、service、framework 缺席，取该类全库最早页，替换样本中原日期最晚且其类型有至少三页的合格页，继续遵守分类配额；类型全库不存在则注明。本基线五类齐全，无需替换，另包含两对 skill-pack。

| 序号 | 页面路径（EN） | 顶层分类 | type | 原 last_verified | 挑选理由 |
|---|---|---|---|---|---|
| 1 | `categories/agent-frameworks/coding-agents/orchestration-and-review/background-agents.md` | agent-frameworks | app | 2026-07-13 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 2 | `categories/agent-frameworks/coding-agents/terminal-agents/t3code.md` | agent-frameworks | app | 2026-07-13 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 3 | `categories/agent-skills/ai-writing/fiction/webnovel-writer.md` | agent-skills | tool | 2026-07-13 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 4 | `categories/agent-skills/design/ui-taste/hallmark.md` | agent-skills | skill-pack | 2026-07-13 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 5 | `categories/agent-governance/agent-governance-toolkit.md` | agent-governance | tool | 2026-07-16 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 6 | `categories/agent-governance/skillspector.md` | agent-governance | tool | 2026-07-16 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 7 | `categories/document-parsing/any2html.md` | document-parsing | framework | 2026-07-16 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 8 | `categories/education-tutoring/deeptutor.md` | education-tutoring | app | 2026-07-16 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 9 | `categories/investment-finance/awesome-deep-trading.md` | investment-finance | tool | 2026-07-16 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 10 | `categories/investment-finance/backtrader.md` | investment-finance | library | 2026-07-16 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 11 | `categories/llm-eval/chatgpt-comparison-detection.md` | llm-eval | tool | 2026-07-16 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 12 | `categories/media-processing/video-audio/speech-and-subtitles/claude-video.md` | media-processing | app | 2026-07-16 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 13 | `categories/agent-dev-methodology/spec-driven-development/pure-agentic.md` | agent-dev-methodology | framework | 2026-07-17 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 14 | `categories/agent-dev-methodology/spec-driven-development/spec-anchored-agentic-development.md` | agent-dev-methodology | skill-pack | 2026-07-17 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 15 | `categories/api-gateway/funtool.md` | api-gateway | tool | 2026-07-17 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 16 | `categories/blockchain-dev-infrastructure/powfaucet.md` | blockchain-dev-infrastructure | service | 2026-07-17 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 17 | `categories/captcha/buster.md` | captcha | tool | 2026-07-17 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 18 | `categories/captcha/nopecha-extension.md` | captcha | tool | 2026-07-17 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 19 | `categories/document-parsing/bella-domify.md` | document-parsing | library | 2026-07-17 | 按原复核日期及路径排序，顶层分类最多两对。 |
| 20 | `categories/im-automation/openilink-hub.md` | im-automation | app | 2026-07-17 | 按原复核日期及路径排序，顶层分类最多两对。 |

类型计数：app＝5、tool＝8、skill-pack＝2、framework＝2、library＝2、service＝1。phase 02 取 1–5，03 取 6–10，04 取 11–15，05 取 16–20；每对按 sync-entry 全流程复核，逐对提交，健康度串行重算。第一段仅冻结清单，不改这 20 对页。

2026-10-26路径迁移说明（不参与冻结抽样）：第15项保留固定基线中的旧路径；当前入口是[客户端路由分类下的Funtool](../../../categories/api-gateway/client-routing/funtool.md)。读取固定提交或复算清单时仍使用表内路径，不用现路径替换历史样本身份。
