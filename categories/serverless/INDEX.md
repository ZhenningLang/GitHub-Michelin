# serverless

> Category node. Kubernetes-native serverless and scale-to-zero platforms — request-driven compute that runs inside a cluster you operate.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Knative Serving** | Use it when HTTP services sit idle most of the day and you want revisioned rollouts plus autoscaling to zero without adopting a FaaS product. | B (5/6) | [→](knative-serving.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Knative Serving](knative-serving.md) | ✅ | B (5/6) | Scale-to-zero, revisions and traffic splitting inside your own cluster — you get portability by operating a CRD control plane, a networking layer and an autoscaler. |

## What belongs here

Serverless/scale-to-zero serving layers you deploy on your own Kubernetes, as opposed to hosted functions platforms (non-repos) or stateful execution runtimes (see `sandboxing`). Knative Eventing and Knative Functions are the sibling projects, not yet indexed.
