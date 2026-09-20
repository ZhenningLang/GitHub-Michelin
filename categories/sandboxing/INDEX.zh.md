# sandboxing

> 分类节点。面向不可信负载与 agent 生成代码的沙箱技术——内核／虚拟机级隔离运行时，以及建在其上的 agent 沙箱平台与 SDK。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **gVisor** | 不可信容器必须与宿主内核隔离、又不想跑虚拟机时用它——不需要 KVM，且容器工作流不变。 | A（5/6） | [→](gvisor.zh.md) |
| **Kata Containers** | 想让每个 pod 在轻量虚拟机里拿到真内核、同时 Kubernetes 保持常规 RuntimeClass 工作流时用它。 | A（5/6） | [→](kata-containers.zh.md) |
| **Firecracker** | 你在自建沙箱层、想要一个带控制 API 的极简 KVM microVM 原语（而不是容器运行时）时用它。 | A（5/6） | [→](firecracker.zh.md) |
| **OpenSandbox** | 当你需要自托管隔离沙箱、在 K8s 规模上运行不可信的 agent 生成代码（带出口管控和凭证保险库）时用它——但仓库仅数月之龄（2025-12 创建），其 API 与 Lindy 长期记录尚未经检验。 | B（5/6） | [→](opensandbox.zh.md) |
| **E2B** | 当 agent 需要跑 AI 生成的代码、你想要把沙箱做成 SDK 时用它——默认托管，必须落在自己账号时用 Terraform 自托管到 AWS／GCP。 | A（6/6） | [→](e2b.zh.md) |
| **Agent Substrate** | 当你有一大批大部分时间闲置的有状态 agent 会话、想把它们多路复用到少数预热 Kubernetes pod 上（闲置时存档、按需恢复）时用它——但它处于 1.0 之前、API 不稳定、安全加固尚未做。 | B（4/6） | [→](substrate.zh.md) |
| **Modal client SDK** | 想要 serverless 容器、GPU 与沙箱而什么都不用运维时用它——客户端 SDK 开源，平台闭源且只能托管。 | A（6/6） | [→](modal-client.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [gVisor](gvisor.zh.md) | ✅ | A（5/6） | 不用 KVM 的隔离（用户态内核、过滤后的系统调用面）——比虚拟机更容易落地，但语义与吞吐和真内核不同。 |
| [Kata Containers](kata-containers.zh.md) | ✅ | A（5/6） | 每沙箱一个真内核（轻量虚拟机）加一套做完的 Kubernetes 集成——代价是每个节点都要硬件虚拟化，且多一个 hypervisor 要运维。 |
| [Firecracker](firecracker.zh.md) | ✅ | A（5/6） | 现有攻击面最小的 microVM 原语，而它之上的一切（镜像、调度、快照、多租户）都要你自己建。 |
| [OpenSandbox](opensandbox.zh.md) | ✅ | B（5/6） | 自托管优先的沙箱平台，有文档化协议与多语言 SDK——平台由你运维，且项目年轻。 |
| [E2B](e2b.zh.md) | ✅ | A（6/6） | 最快拿到能用的沙箱（先托管 SDK、后 Terraform 自托管）——自托管只覆盖 AWS／GCP。 |
| [Agent Substrate](substrate.zh.md) | ✅ | B（4/6） | 靠把闲置的有状态 agent 存成快照、塞进预热 pod 来换密度——1.0 之前、出站轮询唤醒不成立、安全加固未做。 |
| [Modal client SDK](modal-client.zh.md) | ✅ | A（6/6） | serverless 容器、GPU 与沙箱都不用运维——不能自托管、没有退路、单一厂商。 |

## 什么该放这里

跑不可信代码的层次与产品：虚拟机／内核级隔离运行时（`gVisor`、`Kata Containers`、`Firecracker`），以及建在其上的 agent 沙箱平台与客户端（`OpenSandbox`、`E2B`、`Agent Substrate`、`Modal` 客户端 SDK）。不含通用容器运行时选型（那是你已经在跑的底座），也不含 agent 框架（见 `agent-frameworks`）。
