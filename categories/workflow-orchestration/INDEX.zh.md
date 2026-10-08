# workflow-orchestration

> 分类节点。编写、调度并监控批处理数据/工作流管线（DAG 编排器）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Apache Airflow** | 当你要用 Python DAG 加 Web UI 编排定时批处理数据管线时用它——不适合低延迟或事件驱动流。 | A（6/6） | [→](airflow.zh.md) |
| **Gaia** | 只在研究“流水线即编译插件”设计（job 是真代码，经 go-plugin 运行）或评估是否 fork 时用它——但仓库已归档，最后一次发布在 2022-01，绝不要用于新的生产部署。 | D（6/6） | [→](gaia.zh.md) |
| **Airflow Maintenance DAGs** | 当自管的 Airflow 集群被旧元数据行和陈旧日志拖慢、你想直接拷入现成清理 DAG 时用它——但 `db-cleanup` 默认第一次运行就真删，且依赖随版本变化的内部结构，先 dry-run 并备份。 | D（4/6） | [→](airflow-maintenance-dags.zh.md) |
| **n8n** | 当小型运维团队要把 SaaS 之间的胶水流程自托管在一张业务同事也看得懂的可视化画布上，靠 1500 多个连接器节点和代码节点兜底时用它——但 Sustainable Use License 不允许转售或嵌入产品，也不适合亚秒级流处理。 | A（4/6） | [→](n8n.zh.md) |
| **Argo Workflows** | 当批处理或机器学习流水线已经以容器形式跑在 Kubernetes 上，你想用 YAML 写 DAG、每一步都是带重试、产物传递和界面的 pod 时用它——但它离不开 Kubernetes，成千上万个小步骤也要各付一次 pod 启动开销。 | A（6/6） | [→](argo-workflows.zh.md) |
| **Prefect** | 当已经能跑的 Python 脚本需要定时、重试、运行历史和告警，又不想改写成 DAG 文件时用它（加装饰器即可，控制流仍是普通 Python）——但要让非工程师搭流程用 n8n，崩溃后要从原步骤精确恢复用 Temporal。 | A（6/6） | [→](prefect.zh.md) |
| **Dagster** | 当你负责数仓流水线，要说清哪张表过期了、由哪次运行构建、谁依赖它，想把资产声明成 Python 函数时用它——但 Airflow 的现成算子更多，告警、RBAC、单点登录都只在付费的 Dagster+ 里。 | A（6/6） | [→](dagster.zh.md) |
| **Temporal** | 当一个长时间运行的业务流程（支付、履约、开通、AI agent）必须扛过崩溃和发布、从原来那一步接着跑，又想用普通代码来写时用它——但自托管意味着要运维多服务集群，分片数等决定建好就改不了。 | A（5/6） | [→](temporal.zh.md) |
| **TanStack Workflow** | 跨天的持久流程必须嵌在 TypeScript 应用里、落在你自己的数据库上，且不想多运维一个 workflow server 时用它——0.0.x，控制平面界面还没有，运维面要自己拼。 | C（6/6） | [→](tanstack-workflow.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Apache Airflow](airflow.zh.md) | ✅ | A（6/6） | 当你要用 Python DAG 加 Web UI 编排定时批处理数据管线时用它——不适合低延迟或事件驱动流。 |
| [Gaia](gaia.zh.md) | ✅ | D（6/6） | 换来一份可读参考：用自己的语言写流水线 job、配 Web UI 和调度器；代价是没有补丁和路线图、停在 1.0 之前，今后所有修复都得自己扛。 |
| [Airflow Maintenance DAGs](airflow-maintenance-dags.zh.md) | ✅ | D（4/6） | 换来跑在你现有 Airflow 上、无需新部署的成熟清理配方；代价是破坏性 SQL 风险自负、自 2022-10 起无提交，每逢 Airflow 大版本都得重测。 |
| [n8n](n8n.zh.md) | ✅ | A（4/6） | 可视化、可自托管、非工程师也能改的集成，代价是仅限内部使用的源码可见许可、付费企业功能，以及不适合高吞吐流的数据库驱动引擎。 |
| [TanStack Workflow](tanstack-workflow.zh.md) | ✅ | C（6/6） | Headless 的 TS 持久执行，落在你自己的存储上：不用像 Temporal 那样多运维一个 server，但 store、cron 与运维面都要在 0.0.x 上自己拼。 |

## 什么该放这里

主要职责是把批处理数据/工作流管线作为 DAG **编写、调度与监控**的工具。不含低延迟事件/流处理，不含 agent 构建/运行框架（见 `agent-frameworks`）。
