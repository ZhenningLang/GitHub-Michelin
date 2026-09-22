# optimization-solvers

> 分类节点。接收**声明式**最优化模型（分配问题、LP／MIP、约束满足、资源分配）并去搜索一个好解或可证明最优解的库与求解器——而不是让你自己手搓搜索。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Rebalancer** | 当任务是「按这些策略在分片／主机量级重新安置这些对象」——容量、均衡、故障域打散、尽量少搬——而你宁愿声明具名 spec 加一个调好的局部搜索，也不想手写线性规划时用它。 | B（5/6） | [→](rebalancer.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Rebalancer](rebalancer.zh.md) | ✅ | B（5/6） | Meta 的分配 DSL 加可扩展局部搜索，同一个模型上还有 MIP（HiGHS／Gurobi／Xpress）兜底——场景窄、只有三个月历史，源码构建要拉进 Folly／fbthrift。 |
| OR-Tools · HiGHS · Timefold／OptaPlanner · Gurobi／Xpress | 未收录 | — | 通用的 LP／MIP／CP 求解器与启发式规划器——广得多、活得久得多，但模型与搜索都要自己写；Rebalancer 的 MIP 路径本来就调用 HiGHS、Gurobi 与 Xpress，所以这些先是它的后端，然后才是它的对手。 |

## 什么该放这里

**数学最优化**的求解器、建模层与规划器：分配与资源分配、LP／MIP／整数规划、约束满足，以及建立在其上的建模 DSL。不含 ML 研究 demo 与演化算法框架（见 `ml-research`）；不含 DAG 数据流水线编排（见 `workflow-orchestration`）；不含集群内调度器与任务队列（见 `task-queue`）。
