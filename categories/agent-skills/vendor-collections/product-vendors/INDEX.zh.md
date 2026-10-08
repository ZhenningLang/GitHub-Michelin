# product-vendors

> [vendor-collections](../INDEX.zh.md) 的叶子。平台或产品厂商发布的第一方捆绑包，教编码 agent 正确使用它自家的产品——AWS、Android、Chrome、Remotion、Cloudflare、Bright Data；不用那家产品就用不上。
> ← 上层 [vendor-collections](../INDEX.zh.md) · 根 [路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Agent Plugins for AWS** | AWS Labs 官方出品的九个 agent 插件集合（serverless、Amplify、SageMaker、迁移、数据库、部署/成本估算等），通过 marketplace 安装、触发短语驱动并接好 AWS MCP server，教 Claude Code / Cursor / Codex 在 AWS 上做架构、部署和运维。 | B（5/6） | [→](aws-agent-plugins.zh.md) |
| **Remotion Agent Skills** | Remotion 官方的 12 个 skill 捆绑包：教编码 agent（Claude Code、Codex、Cursor、Kimi Code）写出正确的 Remotion React 视频代码——经 `npx skills add remotion-dev/skills` 安装，版本与框架同步锁定。 | C（4/5） | [→](remotion-skills.zh.md) |
| **Android Skills** | Google 官方 24 个 skill 包，覆盖模型仍会失手的 Android 活（edge-to-edge、R8、Navigation 3、Play 政策）——用 Android CLI 安装，不是 `npx skills add`。 | B（5/6） | [→](android-skills.zh.md) |
| **Modern Web Guidance** | Google Chrome 官方的“先搜再取”skill：写 HTML/CSS/客户端 JS 前，agent 用本地搜索的 npm CLI 取回一篇经评测打分的现代平台指南（原生 API、Baseline 支持、适度降级）。 | B（5/6） | [→](modern-web-guidance.zh.md) |
| **Agent Toolkit for AWS** | 当你的编码 agent 在真实 AWS 账号里干活、你既要 AWS 当前的剧本、又要 IAM 和 CloudTrail 能把 agent 的调用和你的分开时用：约 114 个 skill 加一个托管 MCP 端点；只管 AWS，托管那一半能看到你的流量。 | A（4/5） | [→](agent-toolkit-for-aws.zh.md) |
| **Cloudflare Skills** | 当你的编码 agent 在 Cloudflare 上搭东西、总凭过时记忆写时用：16 个官方 skill，帮它选对 Cloudflare 产品并先读当前文档，外加一条托管 MCP 配置；只管 Cloudflare，无 tag，多数是指针，需要联网。 | A（4/5） | [→](cloudflare-skills.zh.md) |
| **Bright Data Skills** | 当你的 agent 总撞上 403 和验证页、而你已决定花钱让 Bright Data 来过这一关时用：21 个厂商 skill，把每次抓取分给合适的付费产品并检查封锁页；每次调用都计费，有一个 skill 要 agent 停用内置上网工具，没有 tag，README 的 Quick Start 指向已删除的脚本。 | C（4/5） | [→](brightdata-skills.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Agent Plugins for AWS](aws-agent-plugins.zh.md) | ✅ | B（5/6） | AWS Labs 官方出品的九个 agent 插件集合（serverless、Amplify、SageMaker、迁移、数据库、部署/成本估算等），通过 marketplace 安装、触发短语驱动并接好 AWS MCP server，教 Claude Code / Cursor / Codex 在 AWS 上做架构、部署和运维。 |
| [Remotion Agent Skills](remotion-skills.zh.md) | ✅ | C（4/5） | 厂商权威、版本锁定的 React 视频创作指导；不在带 skill 加载器的 harness 上、或不用 Remotion 就没价值，且内容许可未声明。 |
| [Android Skills](android-skills.zh.md) | ✅ | B（5/6） | Google 官方给模型仍会失手的 Android 活准备的剧本；只覆盖 Android、走 CLI 安装、不接受外部贡献。 |
| [Modern Web Guidance](modern-web-guidance.zh.md) | ✅ | B（5/6） | 浏览器厂商按任务检索的构建指导；`0.0.x` 预览版，每次调用走 npm，遥测默认开启，不检查你的产出。 |
| [Agent Toolkit for AWS](agent-toolkit-for-aws.zh.md) | ✅ | A（4/5） | AWS 对 Labs 插件的继任者：skill 加上经托管端点、打了 agent 标记的调用；只管 AWS，无 tag，不收外部 PR，创业插件带合作伙伴优惠链接。 |
| [Cloudflare Skills](cloudflare-skills.zh.md) | ✅ | A（4/5） | Cloudflare 自家的产品路由，加上指向文档的 skill 和一条托管 MCP 配置；只管 Cloudflare，安装跟着 `main`、版本号靠手改，没有 hook 和评测，路由 skill 就是为推荐 Cloudflare 产品而写。 |
| [Bright Data Skills](brightdata-skills.zh.md) | ✅ | C（4/5） | Bright Data 付费反封锁网络的操作手册，不是抓取器：没有密钥就不能用，每次调用计费，包里没有花费上限；安装跟着 `main`，一组待合并的拉取请求会删掉 21 个里的 17 个，对网站条款和数据法规几乎只字未提。 |

## 什么该放这里

平台或产品厂商发布的第一方捆绑包，教编码 agent 正确使用它自家的产品——AWS、Android、Chrome、Remotion、Cloudflare、Bright Data；不用那家产品就用不上。
