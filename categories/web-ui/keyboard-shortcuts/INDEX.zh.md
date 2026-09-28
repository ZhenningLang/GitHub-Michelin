# keyboard-shortcuts

> 分类节点。Web 应用的键盘快捷键库——把组合键和连按绑定到动作，处理 Cmd／Ctrl 的平台差异和输入框，录制用户改的键并把快捷键显示出来。
> ← 返回[web-ui](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **TanStack Hotkeys** | 手写的 `keydown` 判断老出问题——Mac 上 Cmd+S 弹浏览器保存框、用户打字时单键快捷键误触发、录下的自定义按键再也匹配不上——你想要带类型的 `Mod+S` 绑定、连按、录制器和显示格式化，并且有 React、Vue、Angular、Solid、Svelte、Preact、Lit 的适配。 | B（6/6） | [→](tanstack-hotkeys.zh.md) |

## 对比矩阵

| 项目 | 支持框架 | 作用域模型 | 何时优先选它 | 许可证 |
| --- | --- | --- | --- | --- |
| TanStack Hotkeys | React、Preact、Vue、Angular、Solid、Svelte、Lit、原生 JS | 元素 `target` 加每条登记的 `enabled`，单例管理器带重复绑定警告 | 需要带类型的绑定、物理键支持、录制和显示工具，或 React 以外的适配——并且能承受 alpha 期 0.x 的变动和只发 ESM 时 | MIT |

## 什么该放这里

在网页里监听键盘输入、分派快捷键的库：组合键解析、连按、平台修饰键映射、作用域、快捷键录制和显示。命令面板界面放 `component-libraries`；操作系统级的全局热键守护进程不算前端库。
