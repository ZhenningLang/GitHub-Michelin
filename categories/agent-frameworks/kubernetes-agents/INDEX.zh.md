# kubernetes-agents

> 分类节点。Kubernetes 原生的 agent 控制面——把 agent 或 agent *任务*对着集群声明并跑起来。
> ← 返回 [agent-frameworks](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **AX** | 当一大批空闲、有状态的 agent *任务*必须在 Kubernetes 上用 YAML 声明（工作区、出站、模型）、底下还能挂起／恢复时用它——不是把 agent 本身做成 CRD 的那条路。 | B（6/6） | [→](ax.zh.md) |
| **kagent** | 当 agent 应该是 Kubernetes 对象时用它——用 YAML 声明、由控制器与引擎运行，带模型配置、MCP 工具服务器与 OpenTelemetry 追踪。 | B（6/6） | [→](kagent.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [AX](ax.zh.md) | ✅ | B（6/6） | 叠在密度运行时上、像 kubectl 的 Task YAML——对象在 Redis 不在 etcd，不带 agent 引擎，Substrate 是硬依赖。 |
| [kagent](kagent.zh.md) | ✅ | B（6/6） | agent 做成 CRD 就拿到 Kubernetes 的发布、RBAC 与审计体系——代价是采用一个年轻项目的资源模型，并给 agent 真实的集群凭据。 |

## 什么该放这里

执行模型**就是** Kubernetes 集群的控制面——要么把 agent 本身做成 CRD（kagent），要么把沙箱 *任务* 写成 YAML、存在 etcd 之外（AX）。代码优先的 agent 框架放在 `agent-runtimes`；AX 叠着的密度运行时放在 `sandboxing`。
