# design-tokens

> 分类节点。获取、核对和门禁设计 token——一个界面赖以搭建的颜色、字号阶梯、间距、圆角和阴影——尤其当事实来源是线上网站、而不是你手写的文件时。
> ← 返回[分类导航](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类下的项目

| 项目 | 何时使用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Dembrandt** | 设计系统唯一的来源是一个线上网址，你需要把它真实的颜色、字体和间距导出成 DTCG/Tailwind/DESIGN.md token——或者要一个 token 漂移就让 CI 失败的门禁——时用它；token 本来就是你自己写的、或你担心的是布局回归时不要用。 | C（5/6） | [→](dembrandt.zh.md) |

## 横向对比

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Dembrandt](dembrandt.zh.md) | ✅ | C（5/6） | MIT 许可的 CLI + MCP 服务器 + GitHub Action，用真浏览器读计算样式，导出 token 或漂移结论；单人维护、1.0 之前，启发式几乎每周都会让基线移动。 |
| Style Dictionary · Project Wallace css-analyzer · BackstopJS | 未收录 | — | 方向相反的 token 构建（手写 token → 各平台）、基于 CSS 源码的静态审计、像素比对的视觉回归——已在 Dembrandt 的对比表里权衡，尚未收录。 |

## 本分类收什么

主要职责是**把设计 token 当数据处理**的仓库：从渲染后的网站或样式表里提取、校验或转换 token，并在 CI 里对它们的变化设门禁。不收设计编辑器（见 `design-editors`）；不收把某个网站的外观带进代码的 agent skill（见 `agent-skills/design/design-to-code`）；不收通用网页抓取（见 `web-scraping`）。
