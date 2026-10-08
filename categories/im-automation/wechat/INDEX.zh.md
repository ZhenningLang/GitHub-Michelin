# wechat

> 分类节点。微信机器人与账号工具——个人号 puppet、客户端注入、官方通道桥接，以及支撑它们的框架。
> ← 返回[im-automation](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **ItChat** | 仅当你要读懂或接手基于它扫码登录、msg_register 接口写成的老微信机器人代码时用它——它自 2018 年起已废弃，所依赖的网页版微信登录对绝大多数账号已关停，用个人号跑还有封号风险。 | C（4/6） | [→](itchat.zh.md) |
| **WeChatPlugin-MacOS** | 仅当你在 Mac 上把微信刻意钉在 2.3–3.7 这类老版本、想找回防撤回、自动回复和多开时用它——它给 WeChat.app 二进制打补丁，微信每更新一次就坏一次，已约 3 年半没有提交，还有封号风险。 | D（4/6） | [→](wechatplugin-macos.zh.md) |
| **wxpy** | 仅当你要读懂或接手 2017–2019 年用它更顺手的 Bot／Friend／Group 接口写成的微信机器人代码时用它——仓库已归档，它架在 ItChat 的网页版微信登录上，绝大多数账号已登不上，个人号自动化还有封号风险。 | D（5/6） | [→](wxpy.zh.md) |
| **wxappUnpacker** | 仅当你要反编译自有小程序的 .wxapkg 包、需要顺藤找到 wxappUnpacker 这一系工具时把它当线索——本仓库已清空成只剩一个词的 README，整条血缘都已废弃，留存的 fork 还依赖已弃用的 vm2 沙箱。 | E（3/6） | [→](wxappunpacker.zh.md) |
| **WeChat Bot** | 当你需要仍在维护、支持多 IM 通道和多种 LLM 后端的 Node.js CLI，并接受非官方个人微信通道可能触发警告或封号时用它。 | B（5/6） | [→](wechat-bot.zh.md) |
| **ChatGPT-wechat-bot** | 只把它当作 2022 至 2023 年的精简 Wechaty／ChatGPT 参考；项目已停更、模型路径陈旧，个人微信号仍承担非官方 puppet 风险。 | D（3/6） | [→](chatgpt-wechat-bot.zh.md) |
| **Dify Enterprise WeChat Bot** | 只用于固定企业微信客户端版本的隔离 Windows 原型；消息链路含闭源二进制，Workflow 支持未完成，项目也已停滞。 | C（3/6） | [→](dify-enterprise-wechat-bot.zh.md) |
| **Wechaty** | 当你想用 TS／Python／Go／Java 自己掌控个人号机器人的 adapter 与命令层时用它——先确认各 provider 的现状，并接受 puppet 风险。 | C（5/6） | [→](wechaty.zh.md) |
| **CowAgent** | 当你要 Python-first、多通道、模型后端可插拔的助手时用它；它就是更名后的 `zhayujie/chatgpt-on-wechat`，当前通道走 iLink，而不是已被删除的个人号路径。 | B（5/6） | [→](cowagent.zh.md) |
| **WeChatFerry** | 不要部署——维护者已归档仓库，发版钉在旧版 Windows 微信上，整套方案是客户端注入；只适合受控的遗留复现。 | D（6/6） | [→](wechatferry.zh.md) |
| **Dify on WeChat** | 当 Dify 到微信的桥接必须端到端可源码审查时用它；但要权衡它自 2025-04 起没有代码变更，且仍承担个人号通道风险。 | B（3/6） | [→](dify-on-wechat.zh.md) |

## 对比矩阵

| 选项 | 已收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [ItChat](itchat.zh.md) | ✅ | C（4/6） | 换来一份讲清网页版微信机器人原理的规整范本；代价是今天跑不起任何自动化——无人维护、协议已死，还违反服务条款。 |
| [WeChatPlugin-MacOS](wechatplugin-macos.zh.md) | ✅ | D（4/6） | 换来冻结版本微信上的经典体验增强；代价是把第三方代码注入装着你私人聊天的客户端、没有更新，还违反服务条款。 |
| [wxpy](wxpy.zh.md) | ✅ | D（5/6） | 换来比裸用 ItChat 更顺手、便于研究老机器人的对象模型；代价是层层死依赖——已归档的封装、废弃的底层库、关停的协议。 |
| [wxappUnpacker](wxappunpacker.zh.md) | ✅ | E（3/6） | 装不到任何东西，只换来一个去找 fork 的名字；能找到的 fork 也没人维护、本仓库无许可证文件，处理不可信包时还有沙箱逃逸风险。 |
| [WeChat Bot](wechat-bot.zh.md) | ✅ | B（5/6） | 仍在维护的多通道 CLI 和模型 adapter，但非官方个人微信路径伴随账号警告与封禁风险。 |
| [ChatGPT-wechat-bot](chatgpt-wechat-bot.zh.md) | ✅ | D（3/6） | 小型历史 Wechaty／ChatGPT 示例，已经停更，仍依赖不受支持的个人号通道。 |
| [Dify Enterprise WeChat Bot](dify-enterprise-wechat-bot.zh.md) | ✅ | C（3/6） | 固定版本 Windows 企业微信到 Dify 的桥接，helper 为闭源二进制，Workflow 通道也未完成。 |
| [Wechaty](wechaty.zh.md) | ✅ | C（5/6） | 许多个人号机器人背后的多语言可复用框架：想自己掌控 adapter 与状态就选它，但押注某条通道前先看它的 provider 现状。 |
| [CowAgent](cowagent.zh.md) | ✅ | B（5/6） | `zhayujie/chatgpt-on-wechat` 更名后的同一血缘，现为多通道助手、支持多种模型后端——仓库没变，别把旧名字当成另一个项目。 |
| [WeChatFerry](wechatferry.zh.md) | ✅ | D（6/6） | 已归档的 Windows 客户端注入 + RPC 钩子：只作参考或受控的遗留复现，维护者已停更，发版也钉在旧版微信上。 |
| [Dify-on-WeChat](dify-on-wechat.zh.md) | ✅ | B（3/6） | 源码可审查的 Dify 到微信桥接，值得优先于闭源 helper 方案评估——但要按「正在漂移」读：2025-04 之后没有代码变更。 |
| 企业微信官方 API | 非仓库 | — | 腾讯托管的 WeCom 服务端 API：没有仓库，是必须规避个人号 puppet 风险时的官方通道路线。 |

## 什么该放这里

微信专属的机器人、账号工具，以及支撑它们的框架。其他 IM 平台与通用自动化留在父节点；Web/浏览器自动化见 `web-automation`，团队聊天应用见 `team-chat`。

