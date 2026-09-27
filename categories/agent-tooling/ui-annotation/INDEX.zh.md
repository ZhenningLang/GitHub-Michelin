# ui-annotation

> 分类节点。人指着**运行中的应用 UI**——点选、手绘、钉批注——批注以结构化证据（选择器、源码行、diff）抵达编码 agent。与 `supervision-surfaces` 互为姊妹：那边审 agent *写的东西*，这里审应用*渲染出来的东西*。
> ← 返回 [agent-tooling](../INDEX.zh.md) · 根路由：[分类路线](../../../INDEX.zh.md) · English：[INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时使用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Agentation** | 当你的 React 应用肯背一个开发依赖、要点选批注外加 React 组件路径与 dev 构建 `file:line`、再经 MCP 同步给任意终端 agent 时用它——采用度断层第一，许可非 OSI。 | C（4/6） | [→](agentation.zh.md) |
| **Vibe Annotations** | 当看见 UI bug 的人不碰代码时用它：Chrome 扩展批注加后台服务，经 MCP 喂给 Claude Code / Cursor / Codex，还有给队友的文件分享路径。 | C（5/6） | [→](vibe-annotations.zh.md) |
| **Pointa** | 当「不改应用代码」是铁律、且 MIT 是许可硬要求时用它——Chromium 扩展加会讲 MCP 的本地服务，还能把你 Node 后端的 console 日志一并装进 bug 报告。 | C（5/6） | [→](pointa.zh.md) |
| **earmark** | 当你要确定性的源码证据——构建期给 Vite/Next/Svelte 打 `file:line` 戳、CSS 规则行解析、图钉变色跟进的 acknowledge/resolve 闭环——且能接受一个 0 星、休眠的项目时用它。 | C（5/6） | [→](earmark.zh.md) |
| **patch-mark** | 当你要用两行零依赖批注一个不属于你的页面、并希望批注被明确当作「不可信证据」喂给 agent、MCP 面默认只读时用它。 | C（5/6） | [→](patch-mark.zh.md) |
| **markupkit** | 当你的反馈是空间性的——圈、箭头、删除线、拖拽布局 diff，以结构化增量递过去——且不惜自己接管一个休眠的学习型项目时用它。 | C（5/6） | [→](markupkit.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Agentation](agentation.zh.md) | ✅ | C（4/6） | 证据最深（fiber、源码行）、唯一有大众采用度的；代价是一个 React 开发依赖和 source-available 许可。 |
| [Vibe Annotations](vibe-annotations.zh.md) | ✅ | C（5/6） | 零接触广度——设计批注、agent 消化——上限是 content script 能看见的东西。 |
| [Pointa](pointa.zh.md) | ✅ | C（5/6） | MIT 的扩展同乡，带后端日志捕获；更小、更静、十个月大。 |
| [earmark](earmark.zh.md) | ✅ | C（5/6） | 构建期确定性真相（打戳 `file:line`、CSS 规则行），代价是没人承诺继续养它。 |
| [patch-mark](patch-mark.zh.md) | ✅ | C（5/6） | 随处可嵌的 web component，本赛道唯一明示 prompt 注入威胁模型的；没有源码路径保真度。 |
| [markupkit](markupkit.zh.md) | ✅ | C（5/6） | 唯一的手绘/布局 diff 输入模型——把修改画出来而不是说出来——以自述学习型项目的形态存在。 |
| IDE 内嵌浏览器选择器（Cursor、Antigravity、Windsurf） | 非仓库 | — | 零安装、接好了就能用，但绑那个编辑器的预览页签，终端 agent 完全看不见。 |

## 什么归这里

主职是**从运行中的 web UI 捕获视觉、元素级反馈**、并以结构化证据交付给 AI 编码 agent 的工具。不审 agent 产出的工件（见 [`supervision-surfaces`](../supervision-surfaces/INDEX.zh.md)），不做 agent 驱动浏览或测试自动化（见 [`web-automation`](../../web-automation/INDEX.zh.md)），也不是截图 bug 报告的托管服务（非仓库）。
