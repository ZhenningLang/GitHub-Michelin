# data-fetching

> 分类节点。客户端取数与服务端状态缓存库——请求去重、“先旧后新”缓存、写操作与失效，面向 REST／GraphQL 后端。
> ← 返回[web-ui](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **TanStack Query** | 前端组件各自手写请求加 loading 加 error，同一份数据拉两遍，保存后还显示旧行——而且后端是 REST 或混合接口，不是需要按实体归一化缓存的 GraphQL。 | A（5/6） | [→](tanstack-query.zh.md) |
| **TanStack DB** | 每个视图都要求后端单开联表接口，每次写操作都要手补查询缓存、层层重渲染把界面拖卡——把规范化集合一次性装进客户端，让增量活查询加乐观事务维持所有页面一致。 | B（6/6） | [→](tanstack-db.zh.md) |

## 对比矩阵

| 项目 | 支持框架 | 缓存模型 | 何时优先选它 | 许可证 |
| --- | --- | --- | --- | --- |
| TanStack Query | React、Vue、Solid、Svelte、Preact；Angular／Lit 为实验性 | 按键缓存整份响应，先旧后新，自动回收 | 需要显式 staleTime、按键前缀失效、多个框架共用一个内核时 | MIT |
| TanStack DB | React、Vue、Svelte、Solid、Angular | 内存规范化集合，差分数据流活查询，乐观事务 | 数据经 TanStack Query 或同步引擎到达，需要响应式跨集合联表和即时乐观写入时 | MIT |

## 什么该放这里

在客户端应用里负责取数、缓存并让服务端数据保持同步的库（服务端状态管理）。纯客户端状态库和路由放在别处。
