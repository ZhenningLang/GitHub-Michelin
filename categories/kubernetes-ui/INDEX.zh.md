# kubernetes-ui

> 分类节点。用来查看和操作 Kubernetes 集群的界面——终端、桌面或集群内网页。
> ← 返回 [分类路由](../../INDEX.zh.md) · English：[INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **k9s** | 集群操作必须留在终端——活表、日志、exec——浏览器是错的表面时用它。 | A（5/6） | [→](k9s.zh.md) |
| **Headlamp** | 团队需要带 RBAC 按钮的共享浏览器控制台、还要挂在 kubernetes-sigs 下时用它。 | A（6/6） | [→](headlamp.zh.md) |
| **Radar** | 要从本机 Apache-2.0 二进制拿到拓扑、Helm／GitOps、审计和 MCP、还不要账号时用它。 | B（6/6） | [→](radar.zh.md) |
| **Freelens** | 要旧版 Lens 桌面窗口、而且必须是 MIT、不要 Mirantis 账号时用它。 | A（6/6） | [→](freelens.zh.md) |
| **Lens** | 只有团队已经在为 Lens Desktop／Teamwork 付钱时用它；GitHub 上的开源树已停。 | C（4/6） | [→](lens.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [k9s](k9s.zh.md) | ✅ | A（5/6） | 对着 API 的键盘 TUI；活跃七年；没有 GUI、没有共享 URL、没有 MCP。 |
| [Headlamp](headlamp.zh.md) | ✅ | A（6/6） | 集群内或桌面网页界面，带插件和 SIG 治理；诊断功能并非全部内置。 |
| [Radar](radar.zh.md) | ✅ | B（6/6） | 本机 Go 二进制，带拓扑、GitOps、审计、MCP；才八个月，厂商托底。 |
| [Freelens](freelens.zh.md) | ✅ | A（6/6） | Open Lens 的 MIT Electron 分支；笔记本 IDE，不是集群内控制台。 |
| [Lens](lens.zh.md) | ✅ | C（4/6） | Mirantis 商业 IDE；这个仓库不是你下载的那个产品。 |

## 什么算本分类

**主业**是给人（或 agent）一个对着 Kubernetes 集群的界面：浏览资源、日志、exec，以及作为集群操作的 Helm／GitOps。不是指标看板（见 `observability`），不是 TUI **库**（见 `terminal-ui`），也不是把 Pod 再平衡的集群内控制器（见 `dev-utilities` → Descheduler）。
