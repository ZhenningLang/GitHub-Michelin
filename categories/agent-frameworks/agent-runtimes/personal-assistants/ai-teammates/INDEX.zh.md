# ai-teammates

> 分类节点。你要养一组有名字的常驻 bot——各有自己的角色、模型、记忆，常常还有自己的电脑——逐个私聊或拉进群聊派活。
> ← 返回 [personal-assistants](../INDEX.zh.md) · 根：[分类路由](../../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Rakazo** | 当你想自托管“AI 同事”——每个 bot 有自己的长期对话、定时任务和一台带浏览器、可接管的 Linux 电脑，跑在你的 Docker 主机或沙箱服务上、模型任选——时用它；但它是 7 周大的 beta，实际跟的是 `edge` 镜像，而且 bot 在电脑里执行命令和操作浏览器不经审批。 | B（6/6） | [→](rakazo.zh.md) |
| **OpenMausBot** | 当你已经在为 Claude Code、Codex 或 Grok CLI 付费，想把它们变成一个聊天应用里的一排 bot——各有自己的模型、电脑和连接的应用，权限请求变成“允许 / 拒绝”卡片——时用它；但审批只是各 CLI 自己的模式，统计默认开启，`enterprise/` 是源码可见许可，而且它只有 8 周大、几乎每天发版。 | B（6/6） | [→](openmausbot.zh.md) |
| **OpenDots** | 当你想自己托管、自己改几个有名字的 AI 同事——每个有自己的角色、工具、文档空间和可选的容器电脑，能聊天、打电话或在 Slack 里找到，存页面和调 MCP 写操作前先问你——时用它；但每段对话都存在 CopilotKit Intelligence，模型只走兼容 OpenAI 的接口，而且是个 9 天大的 Alpha 模板。 | B（4/6） | [→](opendots.zh.md) |
| **DS Bot** | 当你想在 DeepSeek Harness 上养一支常驻 Bot 团队——每个有自己的记忆、模型、目录和权限，主 Bot 帮你建好其余成员，群聊由管理员分派工作——时用它；但它是一个只有六周大、锁定 DSH 候选版的插件，安装包未签名，Docker 版默认完全访问。 | C（5/6） | [→](ds-bot.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Rakazo](rakazo.zh.md) | ✅ | B（6/6） | Elie Steinbock 做的 xAI Grok Bot 开源替代：Pi agent 循环加每个 bot 一台会备份的 Docker/E2B/Daytona/Box 电脑，网页、Electron、Expo 三端；换来不依赖托管服务的持久图形电脑，代价是运维重、隔离只靠容器。 |
| [OpenMausBot](openmausbot.zh.md) | ✅ | B（6/6） | Milind Soni 做的 Grok Bot 开源替代：在一个类 Telegram 的应用里驱动你已登录的 agent CLI（claude、codex、grok），电脑可选 Boat、Local VM 或你自己的 Mac，应用接入走 Composio；换来自带 agent、运维轻，代价是审批原样透传、统计默认开启、还有一层开源内核外的 `enterprise/`。 |
| [OpenDots](opendots.zh.md) | ✅ | B（4/6） | CopilotKit 的 MIT 模板：按角色划权限的多个专职 agent，带文档页面、Slack、通话和 OpenBot 电脑；不连云能启动，但不接厂商的 Intelligence 服务就聊不了天。 |
| [DS Bot](ds-bot.zh.md) | ✅ | C（5/6） | Fei2411 做的 DSH 插件兼桌面应用，把 DeepSeek Harness 会话变成带复盘记忆、上下文管家和管理员优先群聊的常驻 Bot；换来按量计费模型上的常驻角色，代价是绑定 DSH 候选版、每轮多出模型调用。 |

## 什么该放这里

产品单位是“一组有名字的常驻 bot”：每个 bot 有自己的身份（角色、模型或人设）、记忆，常常还有自己的电脑或接入的应用，你可以单独找它，也可以在群聊或频道里找它们。单一主人的单个助手——桌面同事、跑腿助理、手机 agent，或把一份需求拆给多个专项 agent 的宿主 agent（[Raven](../raven.zh.md)）——留在 [personal-assistants](../INDEX.zh.md)；主要入口是既有聊天渠道的常驻助手走 [messaging-daemons](../messaging-daemons/INDEX.zh.md)。
