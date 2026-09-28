# forms

> 分类节点。表单状态与校验库——保存字段值、是否碰过／改过、错误，运行同步／异步校验，把带类型的值交给提交。
> ← 返回[web-ui](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **TanStack Form** | 表单里每个输入手写一个 `useState`、手动维护 touched、手动给异步校验防抖，字段名写错照样编译通过——而且你想在 React、Vue、Angular、Solid、Svelte 或 Lit 里用同一套带类型、无头的表单模型。 | A（6/6） | [→](tanstack-form.zh.md) |

## 对比矩阵

| 项目 | 支持框架 | 状态模型 | 何时优先选它 | 许可证 |
| --- | --- | --- | --- | --- |
| TanStack Form | React、Vue、Angular、Solid、Svelte、Lit、Preact | 受控，每张表单一个带类型的 store，字段用渲染函数 | 需要从默认值推断类型、异步校验防抖、多个框架共用一个内核——并且能承受 v2 的 API 变更时 | MIT |

## 什么该放这里

在客户端应用里管理表单状态与校验的库（值、错误、是否碰过／改过、提交）。单独的 schema 校验库、UI 输入组件和服务端状态缓存放在别处。
