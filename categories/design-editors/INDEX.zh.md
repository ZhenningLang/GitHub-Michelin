# design-editors

> 分类节点。开源设计编辑器——那套本该按席位租的 Figma 级画布，你自己跑：一个人本地优先，或者一队人自托管。
> ← 返回[分类导航](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类下的项目

| 项目 | 何时使用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **OpenPencil** | 需要打开已有的 Figma `.fig` 文件并对它做脚本化处理——查看结构、检查、转换、导出成 JSX——或者想要一个 local-first、AI 原生、没有服务器、没有账号、不上传的编辑器时用它。 | B（6/6） | [→](open-pencil.zh.md) |
| **Penpot** | 一个团队必须在你自己控制的服务器上编辑同一份设计文件——浏览器编辑器、实时多人协作、组件/变体、原型和 design token——而按席位租托管 SaaS 不可行时用它。 | B（5/6） | [→](penpot.zh.md) |

## 横向对比

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [OpenPencil](open-pencil.zh.md) | ✅ | B（6/6） | local-first、MIT、原生 `.fig` 读写加 CLI/MCP/agent 面；pre-1.0 且由一个主导维护者掌握，没有原型、评论和版本历史。 |
| [Penpot](penpot.zh.md) | ✅ | B（5/6） | MPL-2.0 平台，自托管后有真正的账号、角色和原型；代价是一套 Postgres + Valkey + 对象存储服务群，且 SSO/管理控制在付费 Enterprise 层后面。 |
| Figma · Sketch · Adobe XD | 非仓库 | — | 闭源、托管或按厂商授权出售的设计工具——形态上不在收录范围，在各页面里作为替代品点名。 |

## 本分类收什么

主要职责是**设计编辑器**的仓库：一块用来产出 UI 与视觉设计的无限画布——画板、组件、变体、约束、交付——并且由你自己运行，本地或自建服务器。不收把文字变成图的 diagrams-as-code 工具（见 `diagramming`）；不收用 agent 生成设计、却不产出可编辑文档的项目（见 `ai-design-generation`）；不收计算机辅助设计（见 `cad`）。
