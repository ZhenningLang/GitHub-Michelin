# component-libraries

> 分类节点。UI 组件库、原语与设计系统构建块。
> ← 返回[web-ui](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Ant Design** | 当 React 中后台以可排序、可筛选的表格和复杂表单为主，又没有设计师，想要一套免费、完整、风格统一的组件时用它——但它只支持 React，v6 还要求 React 18 及以上。 | A（6/6） | [→](ant-design.zh.md) |
| **Chakra UI** | 当小团队用 React 或 Next.js 做有品牌感的 SaaS，想要无障碍组件、用样式属性从同一主题取值并内置暗色模式时用它——但样式仍由 Emotion 在运行时生成，也没有 Ant 那个级别的数据表格和表单引擎。 | A（6/6） | [→](chakra-ui.zh.md) |
| **Material UI (MUI)** | 当没有设计师的 React 团队要快速交付大量增删改查页面，并且能接受 Google Material Design 的长相时用它——但要做出辨识度强的品牌就得逐个组件覆盖样式，以 Tailwind 为主的技术栈还得同时维护两套样式体系。 | A（6/6） | [→](material-ui.zh.md) |
| **Radix UI Primitives** | 当你在搭公司自己的 React 设计系统，需要行为、焦点、键盘和 ARIA 都做好但完全不带样式的下拉、弹窗、提示框时用它——但它没有组合框和日期选择器，维护几乎靠 WorkOS 的一个人，还刚经历近一年的停滞。 | A（6/6） | [→](radix-ui.zh.md) |
| **shadcn/ui** | 当你用 Tailwind 起一个 React 新产品，想把精致、无障碍的组件以源码形式拷进仓库随意修改时用它——但每个拷进来的文件都归你维护，项目方向也倚重创建者一个人的判断。 | A（6/6） | [→](shadcn-ui.zh.md) |
| **TanStack Ranger** | 滑块要双把手、不规则步进数组或对数刻度推子，而标记必须完全归你——无头数值引擎管拖拽、吸附、刻度和百分比，渲染什么都不做；目前只有 React 适配层，API 仍是 0.x。 | C（5/6） | [→](tanstack-ranger.zh.md) |
| **TanStack Select** | 想要一个标记归你、能搜索多选的下拉框，期待 TanStack 式无头引擎——仅列观察名单：`main` 是空脚手架加一份重写 RFC，npm 上没有包；唯一发布过的是停更、无 ARIA、只支持 React 16 的旧 hook `use-select`。 | C（4/6） | [→](tanstack-select.zh.md) |
| **TanStack Table** | 表格要排序、过滤、分页、分组、选行，但 `<table>` 的 DOM 和样式必须完全归你——无头引擎算状态和行模型，标记由你自己渲染。 | A（6/6） | [→](tanstack-table.zh.md) |
| **TanStack Time** | 产品日历要重复日程、拖拽改时长、超订校验，而 DOM 必须归你——无头、Temporal 原生的核心算日期网格、重复展开和冲突。观察名单：未发布的 pre-alpha，npm 上还没有包。 | D（4/6） | [→](tanstack-time.zh.md) |

## 什么该放这里

UI 组件库、原语与设计系统构建块。
