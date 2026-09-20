# kubernetes-agents

> 分类节点。Kubernetes 原生的 agent 框架——把 agent 当作集群资源来声明、部署与治理。
> ← 返回 [agent-frameworks](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **kagent** | 当 agent 应该是 Kubernetes 对象时用它——用 YAML 声明、由控制器与引擎运行，带模型配置、MCP 工具服务器与 OpenTelemetry 追踪。 | B（5/6） | [→](kagent.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [kagent](kagent.zh.md) | ✅ | B（5/6） | agent 做成 CRD 就拿到 Kubernetes 的发布、RBAC 与审计体系——代价是采用一个年轻项目的资源模型，并给 agent 真实的集群凭据。 |

## 什么该放这里

执行模型**就是** Kubernetes 的框架——agent、工具与模型配置都表达为集群资源并由控制器 reconcile。代码优先的 agent 框架与运行时放在 `agent-runtimes`；对大量有状态 agent 沙箱做多路复用的执行层放在 `sandboxing`。
