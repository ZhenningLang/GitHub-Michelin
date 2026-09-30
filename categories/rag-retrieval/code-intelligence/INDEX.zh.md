# code-intelligence

> 分类节点。代码智能图与代码检索索引：让编码 agent（或人）对一个仓库问结构性问题——谁调用它、改动影响面、归属——而不是反复 grep。
> ← 返回[rag-retrieval](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **graphify** | 当 agent 需要把整个仓库的代码、schema 和文档当成知识图谱来查询、而非反复 grep 时用它。 | C（5/6） | [→](graphify.zh.md) |
| **code-review-graph** | 当 AI 评审在大仓库里反复烧上下文、你只想喂给它一次改动真正触及（blast-radius）的文件时用它。 | B（6/6） | [→](code-review-graph.zh.md) |
| **Understand-Anything** | 当你想把任意代码库变成可探索、可提问的知识图谱给 agent 用时用它——比 graphify 更年轻、未经检验。 | B（6/6） | [→](understand-anything.zh.md) |
| **SCIP** | SCIP Code Intelligence Protocol | A（6/6） | [→](scip.zh.md) |
| **Sourcegraph** | Code AI platform with Code Search & Cody | D（4/6） | [→](sourcegraph.zh.md) |
| **Ix** | 当你的编码 agent 总在多语言仓库里 grep 找调用方和影响面、而你能跑 Docker 时用它——代价是后端镜像闭源、项目才七个月大还在 v0.x。 | B（6/6） | [→](ix.zh.md) |
| **Repowise** | 当你的 agent 每个任务都在大仓库里重新烧上下文摸底、而你要一个不用 key 的本机索引通过 MCP 回答图、git、健康度、死代码与决策问题时用它——代价是六个月大、v0.x、AGPL 的厂商项目。 | C（6/6） | [→](repowise.zh.md) |
| **Jevgrep** | 当你的 agent 要在没建过索引的陌生仓库里靠“这段代码在干什么”来定位、并接受按次付费把源码发给托管评测模型时用它——代价是出生两天、单人维护、只有 macOS/Linux。 | C（4/6） | [→](jevgrep.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [graphify](graphify.zh.md) | ✅ | C（5/6） | 当 agent 需要把整个仓库的代码、schema 和文档当成知识图谱来查询、而非反复 grep 时用它。 |
| [code-review-graph](code-review-graph.zh.md) | ✅ | B（6/6） | 当 AI 评审在大仓库里反复烧上下文、你只想喂给它一次改动真正触及（blast-radius）的文件时用它。 |
| [Understand-Anything](understand-anything.zh.md) | ✅ | B（6/6） | 把代码变成 agent 可查询的可探索知识图谱；比 graphify 年轻，star 数与数据外发边界均存疑。 |
| [Ix](ix.zh.md) | ✅ | B（6/6） | 当你的编码 agent 总在多语言仓库里 grep 找调用方和影响面、而你能跑 Docker 时用它——代价是后端镜像闭源、项目才七个月大还在 v0.x。 |
| [Repowise](repowise.zh.md) | ✅ | C（6/6） | 当你的 agent 每个任务都在大仓库里重新烧上下文找结构、而你想要一个不用 key 的本机索引，通过 MCP 回答图、git、健康度、死代码与决策问题时用它——代价是六个月大、v0.x、AGPL 的厂商项目。 |
| [Jevgrep](jevgrep.zh.md) | ✅ | C（4/6） | 当你的 agent 要在没建过索引的陌生仓库里靠“这段代码在干什么”来定位、并接受按次付费把源码发给托管评测模型时用它——代价是出生两天、单人维护、只有 macOS/Linux。 |
| [SCIP](scip.zh.md) | ✅ | A（6/6） | SCIP Code Intelligence Protocol |
| [Sourcegraph](sourcegraph.zh.md) | ✅ | D（4/6） | Code AI platform with Code Search & Cody |

## 实地证据：agent 真的会用这些工具吗（截至 2026-09-30）

采用本分类任何工具前先读这一节。公开 issue、讨论和各项目自己的基准指向同一个方向：瓶颈不在图谱质量，而在 agent 会不会调用；没有任何项目证明过答案质量有可测的提升。

- **agent 默认不调用。** graphify 实测注入 8,348 次提示只换来 339 次调用（约 4%），提示本身的 token 是全部查询输出的约 3.7 倍（[graphify#3435](https://github.com/Graphify-Labs/graphify/issues/3435)）。Serena 官方文档承认 agent「会经常用不好 Serena 的工具……即所谓 agent drift」（[文档](https://github.com/oraios/serena/blob/main/docs/02-usage/030_clients.md)）。Repowise 的跨工具基准里，code-review-graph 在 Claude Code 上被调用 0/15 次，Repowise 自己重跑从 4/15 掉到 3/15——「调用率不是工具的稳定属性」（[BENCHMARKS.md:413-469](https://github.com/repowise-dev/repowise/blob/54c9618dac6b8291317138cd9e812e640c9acadf/docs/BENCHMARKS.md#L413-L469)）。工具描述的写法影响很大：Jevgrep 改写描述后首调率从 0/5 变成 5/5（[jevgrep#29](https://github.com/dzhng/jevgrep/issues/29)）。
- **强制「先查图」让结果变差。** 用户报告模型写代码「明显变差」后，code-review-graph 撤回了「在 Grep/Read 之前一律先查图」的指令（[#314](https://github.com/tirth8205/code-review-graph/issues/314) → [PR #886](https://github.com/tirth8205/code-review-graph/pull/886)）。空结果会被当成事实：「Agents read the zero as proof and act on it」（[PR #884](https://github.com/tirth8205/code-review-graph/pull/884)）；OpenCode 的实验性 LSP 工具在初始化失败时返回空结果而不是报错（[anomalyco/opencode#40413](https://github.com/anomalyco/opencode/issues/40413)）。
- **没有测到质量提升。** Repowise：「No tool here measurably changed answer quality in either direction」（[BENCHMARKS.md:452-455](https://github.com/repowise-dev/repowise/blob/54c9618dac6b8291317138cd9e812e640c9acadf/docs/BENCHMARKS.md#L452-L455)；竞品方测量，非中立）。有用户做同模型 A/B，graphify 贵 1.6–1.9 倍，不用它的 agent 答得更完整（[graphify#985](https://github.com/Graphify-Labs/graphify/issues/985)）。Jevgrep README 报告用与不用都是 8/10。报告过的增益都很窄：追正向调用链、在同名标识符多的仓库里查引用、弱模型。
- **Go 是 tree-sitter 图谱的弱项。** 以 Go 编译器（RTA）调用图为标准，code-review-graph 2.3.7 在 gitleaks 上召回 0.026–0.032、在 syft 上 0.086–0.201；Repowise 自己漏掉的边有 44% 是动态派发（[BENCHMARKS.md:74-80、137](https://github.com/repowise-dev/repowise/blob/54c9618dac6b8291317138cd9e812e640c9acadf/docs/BENCHMARKS.md#L74-L80)）。graphify 修复前 21 条 Go 模块内 import 一条都没解析出来（[graphify#3746](https://github.com/Graphify-Labs/graphify/issues/3746)）。Go 仓库要精确，走真正的语言服务器（gopls）。

没找到：任何中立第三方的任务成功率测量；任何在 Go 上的 LSP 对 grep 对比。

## 什么该放这里

主要职责是**为检索而索引代码库**的工具——符号／调用图、覆盖代码与文档的知识图谱、代码搜索引擎与代码索引格式——让 agent 只读对的那几个文件，而不是读整棵树。不含通用文档检索或向量检索（见 `vector-search`、`structured-retrieval`），不含在 PR 上发评论的 AI 代码评审（见 `ai-code-review`）。
