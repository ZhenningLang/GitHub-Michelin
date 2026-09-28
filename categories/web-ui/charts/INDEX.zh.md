# charts

> 分类节点。嵌进前端的图表库——在你的应用里把数据数组变成坐标轴、柱、线、点，带提示框、尺寸自适应和框架集成。
> ← 返回[web-ui](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **TanStack Charts** | 现成图表组件画不出设计要的自定义图层，同一张图又要在多个框架和服务端渲染时用它——一份带类型的“标记加比例尺”定义，自带服务端 SVG、焦点和可选 Canvas；Alpha 0.x，才两个月大。 | B（6/6） | [→](tanstack-charts.zh.md) |
| **TanStack React Charts** | React DOM 应用里已有基于 `react-charts` 的折线/柱/面积图、迁移前还得让它继续跑时才碰它——序列数组加 `getValue` 轴取值函数，D3 计算、SVG 输出、Voronoi 悬停；2025 年已归档，v3 从未脱离 beta，别在它上面新建图表。 | D（5/6） | [→](tanstack-react-charts.zh.md) |

## 对比矩阵

| 项目 | 模型 | 输出 | 支持框架 | 何时优先选它 | 许可证 |
| --- | --- | --- | --- | --- | --- |
| TanStack Charts | 图形语法（标记、通道、比例尺），可按场景协议自定义标记 | SVG（默认）、Canvas（按需）、服务端静态 SVG | React、Preact、Vue、Solid、Svelte、Angular、Lit、Alpine、Octane、React Native（实验性）、原生 DOM | 一份定义要服务多个框架和服务端渲染、还要长出自定义标记——并且你能锁定 Alpha 版本时 | MIT |
| TanStack React Charts | 序列数组 + 主/副轴取值函数；只有折线、面积、柱、气泡 | SVG（在浏览器里量尺寸；服务端只有固定兜底尺寸） | 仅 React DOM | 你在维护基于它的旧图表、暂时迁不走时——已归档，不再有修复 | MIT |

## 什么该放这里

开发者嵌进应用代码的客户端图表与绘图库（图表组件、可视化语法、D3 式底层原语）。带查询和保存看板的自托管 BI 工具放 `data-visualization`；“图即代码”的示意图工具放 `diagramming`。
