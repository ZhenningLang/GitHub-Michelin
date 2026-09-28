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

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [graphify](graphify.zh.md) | ✅ | C（5/6） | 当 agent 需要把整个仓库的代码、schema 和文档当成知识图谱来查询、而非反复 grep 时用它。 |
| [code-review-graph](code-review-graph.zh.md) | ✅ | B（6/6） | 当 AI 评审在大仓库里反复烧上下文、你只想喂给它一次改动真正触及（blast-radius）的文件时用它。 |
| [Understand-Anything](understand-anything.zh.md) | ✅ | B（6/6） | 把代码变成 agent 可查询的可探索知识图谱；比 graphify 年轻，star 数与数据外发边界均存疑。 |
| [Ix](ix.zh.md) | ✅ | B（6/6） | 当你的编码 agent 总在多语言仓库里 grep 找调用方和影响面、而你能跑 Docker 时用它——代价是后端镜像闭源、项目才七个月大还在 v0.x。 |
| [Repowise](repowise.zh.md) | ✅ | C（6/6） | 当你的 agent 每个任务都在大仓库里重新烧上下文找结构、而你想要一个不用 key 的本机索引，通过 MCP 回答图、git、健康度、死代码与决策问题时用它——代价是六个月大、v0.x、AGPL 的厂商项目。 |
| [SCIP](scip.zh.md) | ✅ | A（6/6） | SCIP Code Intelligence Protocol |
| [Sourcegraph](sourcegraph.zh.md) | ✅ | D（4/6） | Code AI platform with Code Search & Cody |

## 什么该放这里

主要职责是**为检索而索引代码库**的工具——符号／调用图、覆盖代码与文档的知识图谱、代码搜索引擎与代码索引格式——让 agent 只读对的那几个文件，而不是读整棵树。不含通用文档检索或向量检索（见 `vector-search`、`structured-retrieval`），不含在 PR 上发评论的 AI 代码评审（见 `ai-code-review`）。
