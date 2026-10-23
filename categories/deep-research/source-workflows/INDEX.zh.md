# source-workflows

> 来源工作流：访问平台、筛选社区证据、追溯原文段落、审查引文。
> ← 返回 [deep-research](../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **imozuru** | 在 Claude Code 中，把陌生领域的主张追到原文段落；交付核对过的摘录，而非综合报告。 | C（4/5） | [→](imozuru.zh.md) |
| **Agent-Reach** | 当你的 agent 需要免付费 API 地读取和搜索网页与社交平台内容时用它。 | B（5/6） | [→](agent-reach.zh.md) |
| **Hyperresearch** | 当你在 Claude Code 里、需要一份引用逐条核验的高风险研究报告时用它——16 步对抗式流水线加持久来源 vault；时间与 token 开销都重，且只支持 Claude Code。 | B（5/6） | [→](hyperresearch.zh.md) |
| **last30days** | 当你想让 agent 汇总最近 30 天 Reddit、X、YouTube、HN、Polymarket 上关于某个主题的讨论、并按互动量排好序时用它——但每次调用要加载约 258 KB 的 skill 提示词，且部分来源依赖抓取和浏览器登录 cookie。 | B（6/6） | [→](last30days.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [imozuru](imozuru.zh.md) | ✅ | C（4/5） | 原文阅读路径加摘录匹配；日文优先、仅十天历史，也不是网络沙箱。 |
| [Agent-Reach](agent-reach.zh.md) | ✅ | B（5/6） | 给自建工作流补平台访问工具；不做迭代式综合，也不写带引用报告。 |
| [Hyperresearch](hyperresearch.zh.md) | ✅ | B（5/6） | 锁死 Claude Code 的 16 步研究流水线，带对抗式 critic、引用核验和持久 vault；pre-1.0 churn 明显，且榜单领先宣称是自测 projection。 |
| [last30days](last30days.zh.md) | ✅ | B（6/6） | 一条斜杠命令把最近 30 天 Reddit／X／YouTube／HN／Polymarket 的信号融合成一份带引用的简报；项目年轻、热度高、上下文开销大，且依赖抓取。 |

## 什么该放这里

当**来源访问、证据筛选或核验**决定工作流时，进入本分支：读取 agent 够不到的平台、筛选近期社区反应、把主张追到原文段落，或依托可复用来源库审查引文。这些工具在已有 agent 宿主中工作；交付物可以是原始内容、核对过的摘录或审查后的报告。Hyperresearch 虽然写报告，决定性取舍仍是来源审查工作流，而非独立研究运行时。

如果你要选择规划并执行整体调研的研究引擎、应用、模型运行时或科学工作台，留在[父分类](../INDEX.zh.md)。这里按任务能力划分，不按实现语言或项目名称划分。单纯的网页抓取基础设施归 [web-scraping](../../web-scraping/INDEX.zh.md)，不放这里。
