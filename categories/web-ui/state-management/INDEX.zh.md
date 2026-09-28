# state-management

> 分类节点。客户端状态 store——在组件树外保存共享的响应式值，自动重算派生值，让组件只订阅自己读的那一小块。
> ← 返回[web-ui](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **TanStack Store** | 你的框架无关库或应用核心每个框架都要重写一遍“订阅、通知”的胶水，想要一个带派生值、基于信号的 store，再配上薄适配层，只在组件选中的那一块变了时才重渲染。 | A（6/6） | [→](tanstack-store.zh.md) |
| **TanStack Persist** | 界面状态一刷新就丢，每个功能都在重写 localStorage 的读、解析、存循环；这个库把它收成 useState 形状的钩子，带版本失效和过期——仅限观察名单，npm 上还没有包。 | C（5/6） | [→](tanstack-persist.zh.md) |

## 对比矩阵

| 项目 | 支持框架 | 状态模型 | 何时优先选它 | 许可证 |
| --- | --- | --- | --- | --- |
| TanStack Store | React、Preact、Vue、Angular、Solid、Svelte、Lit、Octane | 不可变值加更新函数，用函数建派生 store，信号内核 | store 必须放在框架无关的代码里，或者你想用 TanStack Router／Form 已经在用的运行时——并且能承受 0.x 的 API 变动、不需要持久化和 devtools 时 | MIT |
| TanStack Persist | 只有 React（Solid／Preact 承诺中；Vue／Angular／Svelte 等贡献者） | useState 形状的持久化状态，{ buster, state, timestamp } 包装，maxAge 过期，select 子集 | 你想要 TanStack 生态的持久化、内置失效语义，并且能以源码方式引入一个未发布的 0.x——今天不是可生产安装的选择 | MIT |

## 什么该放这里

保存客户端应用状态、在状态变化时通知 UI 组件的库（store、原子、信号、当作 store 用的状态机），以及把这些状态持久化到浏览器存储的库（持久化适配层、持久化状态钩子）。服务端状态缓存和数据拉取放 `data-fetching`，表单专用状态放 `forms`。
