# optimization-solvers

> 分类节点。接收**声明式**最优化模型（分配问题、LP／MIP、约束满足、资源分配）并去搜索一个好解或可证明最优解的库、引擎与规划器——而不是让你自己手搓搜索。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **OR-Tools** | 问题组合性广——路径规划、排程、装箱、指派——而你想要一次安装就同时拿到 CP-SAT、LP／MIP 封装与 routing，并支持 Python／Java／.NET／C++ 时用它。 | A（6/6） | [→](or-tools.zh.md) |
| **HiGHS** | 模型已经是矩阵或 MPS／LP 文件，你想用一个无第三方依赖、MIT 许可的 LP／QP／MIP 引擎、且中间不要夹一层建模框架时用它。 | A（6/6） | [→](highs.zh.md) |
| **Rebalancer** | 当任务是「按这些策略在分片／主机量级重新安置这些对象」——容量、均衡、故障域打散、尽量少搬——而你宁愿声明具名 spec 加一个调好的局部搜索，也不想手写线性规划时用它。 | B（5/6） | [→](rebalancer.zh.md) |
| **Timefold Solver** | JVM 上、计划要在一长串软的、丰富的业务规则下产生——排班、路径、课表——且规则必须一直能以 Java 形式编辑时用它。 | B（6/6） | [→](timefold-solver.zh.md) |
| **OptaPlanner** | 只在要读懂或迁移已有 9.x 代码库时打开：仓库已归档、代码并入 Apache KIE Drools，新工作应该落在 Timefold Solver。 | C（4/6） | [→](optaplanner.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [OR-Tools](or-tools.zh.md) | ✅ | A（6/6） | Google 的组合优化套件——CP-SAT、Glop／PDLP、MIP 封装、routing——一次安装、四种语言；模型由你写，代价是依赖体积。 |
| [HiGHS](highs.zh.md) | ✅ | A（6/6） | 无依赖的 MIT LP／QP／MIP 引擎，既能 `highs model.mps` 也能嵌入式调用——它只管求解，模型自带。 |
| [Rebalancer](rebalancer.zh.md) | ✅ | B（5/6） | Meta 的分配 DSL 加可扩展局部搜索，同一个模型上还有 MIP（HiGHS／Gurobi／Xpress）兜底——场景窄、只有三个月历史，源码构建要拉进 Folly／fbthrift。 |
| [Timefold Solver](timefold-solver.zh.md) | ✅ | B（6/6） | JVM 上基于算分的规划（OptaPlanner 血脉，仍在维护）——规则又软、又多、又常改时最合适；open-core，带商业 Enterprise Edition。 |
| [OptaPlanner](optaplanner.zh.md) | ✅ | C（4/6） | 该血脉已归档的源头：当模式来源或迁移对象来读，绝不要当新依赖。 |
| Gurobi · FICO Xpress | 未收录 | — | 闭源商用 MIP 引擎，按席位授权、带支持——没有公开仓库可收录；OR-Tools 与 Rebalancer 都能调它们。 |

## 什么该放这里

**数学最优化**的求解器、建模层与规划器：分配与资源分配、LP／MIP／整数规划、约束满足与约束规划，以及建立在其上的建模 DSL。不含 ML 研究 demo 与演化算法框架（见 `ml-research`）；不含 DAG 数据流水线编排（见 `workflow-orchestration`）；不含只在 Kubernetes 内部应用 placement 的集群内控制器（见 `dev-utilities/ops-infra`）与任务队列（见 `task-queue`）。
