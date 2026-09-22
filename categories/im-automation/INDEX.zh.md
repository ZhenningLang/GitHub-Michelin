# im-automation

> 分类节点。即时通讯机器人与自动化（微信等 IM 平台）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)


## 子分类

| 分类 | 何时用 | 路由 |
| --- | --- | --- |
| **wechat** | 微信专属的机器人、账号工具，以及支撑它们的框架。 | [→](wechat/INDEX.zh.md) |

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Douyin-Bot** | 仅当你想要一份 ADB 屏幕坐标手机自动化的历史示例时用它——切勿部署，2018 年的硬编码坐标与失效的腾讯人脸 API 意味着它早已跑不通。 | D（3/6） | [→](douyin-bot.zh.md) |
| **OpeniLink Hub** | 当多个接入 iLink 的微信 Bot 需要自托管控制面、持久化、trace 和 App 时用它；项目很年轻，并明确声明与 iLink 官方团队没有关联或背书。 | B（5/6） | [→](openilink-hub.zh.md) |
| **OpeniLink Go SDK** | 当你需要把原始 iLink 传输层嵌进现有 Go 服务，并愿意用最小信任边界换掉控制面时用它；持久化、认证、重试与运维随后都由你承担。 | C（4/6） | [→](openilink-sdk-go.zh.md) |

## 对比矩阵

| 选项 | 已收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Douyin-Bot](douyin-bot.zh.md) | ✅ | D（3/6） | 仅当你想要一份 ADB 屏幕坐标手机自动化的历史示例时用它——切勿部署，2018 年的硬编码坐标与失效的腾讯人脸 API 意味着它早已跑不通。 |
| [OpeniLink Hub](openilink-hub.zh.md) | ✅ | B（5/6） | 带持久化、trace 和 App 的年轻多 Bot 控制面，但没有 iLink 官方关联或背书。 |
| [OpeniLink SDK (Go)](openilink-sdk-go.zh.md) | ✅ | C（4/6） | 已收录 Hub 之下的 Go 版原始 iLink 传输层：信任边界最小，但持久化、认证、重试与运维都要自己扛。 |

## 什么该放这里

面向**即时通讯平台**（微信等 IM）的机器人与自动化。微信专属项目放在 `wechat/`。不含 Web/浏览器自动化（见 `web-automation`），不含团队聊天应用（见 `team-chat`）。

