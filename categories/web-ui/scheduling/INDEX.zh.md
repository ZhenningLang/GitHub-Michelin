# scheduling

> 分类节点。客户端应用里的函数执行时机工具——防抖、节流、限流、排队、批处理，以及暴露 pending 状态的框架 hooks。
> ← 返回[web-ui](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **TanStack Pacer** | 搜索框、自动保存、滚动处理全靠手写 `setTimeout`／`clearTimeout`，而你要的是带类型、带状态、可取消的防抖／节流／限流／排队／批处理，同步异步各有变体——不是服务端配额。 | A（6/6） | [→](tanstack-pacer.zh.md) |

## 对比矩阵

| 项目 | 模式 | 支持框架 | 响应式状态 | 许可证 |
| --- | --- | --- | --- | --- |
| TanStack Pacer | 防抖、节流、限流、排队、批处理，各分同步与异步两版 | vanilla、React、Preact、Solid、Angular（Vue／Svelte 未移植） | 有，基于 TanStack Store；`pacer-lite` 为体积舍弃 | MIT |

## 什么该放这里

在客户端应用里决定函数*何时*运行的库：控制调用频率（防抖／节流／限流）与安排调用次序（排队／批处理），含配套的框架 hooks。带 broker 的分布式作业系统在[task-queue](../../task-queue/INDEX.zh.md)，DAG 编排器在[workflow-orchestration](../../workflow-orchestration/INDEX.zh.md)；在服务端对接口施加的限率属于后端栈，不放这里。
