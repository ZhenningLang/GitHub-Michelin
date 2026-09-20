# serverless

> 分类节点。Kubernetes 原生的 serverless 与缩容到零平台——跑在你自己运维的集群里的请求驱动计算。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Knative Serving** | 当 HTTP 服务一天里大部分时间闲着、你想要按 revision 的发布加缩容到零，又不想采用某个 FaaS 产品时用它。 | B（5/6） | [→](knative-serving.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Knative Serving](knative-serving.zh.md) | ✅ | B（5/6） | 在自己集群里实现缩容到零、revision 与流量切分——可移植性的代价是要运维一套 CRD 控制面、一层网络与一个扩缩器。 |

## 什么该放这里

部署在你自己的 Kubernetes 上的 serverless／缩容到零服务层，与托管函数平台（非仓库）和有状态执行运行时（见 `sandboxing`）相区分。Knative Eventing 与 Knative Functions 是兄弟项目，尚未收录。
