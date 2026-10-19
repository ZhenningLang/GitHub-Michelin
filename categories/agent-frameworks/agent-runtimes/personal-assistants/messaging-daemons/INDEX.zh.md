# messaging-daemons

> 分类节点。你要在自有主机或小板上常驻助手，主要通过现有聊天渠道和定时任务使用。
> ← 返回 [personal-assistants](../INDEX.zh.md) · 根：[分类路由](../../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Octop** | 家里或小团队要在飞书/企微上共用隔离 Agent、对话留在本机磁盘时用它——不是现成办公技能，LangGraph 内核仍是未公开源码的 wheel。 | B（5/6） | [→](octop.zh.md) |
| **PicoClaw** | 小型 ARM、MIPS、RISC-V Linux 板子要用聊天接任务，又不想维护解释器环境时选它；模型推理另配，远程命令默认开启，进程隔离默认关闭。 | B（6/6） | [→](picoclaw.zh.md) |
| **Hermes Agent** | 当你想在自己的 VPS 上养一个长期在线的助手，能跑 shell 和定时任务、记得你的环境、在 Telegram 或 Slack 上回你时用它——但技能和记忆一变它的做法就跟着变，项目也才约 15 个月大。 | A（4/6） | [→](hermes-agent.zh.md) |
| **OpenClaw** | 当你想在自己电脑上跑一个个人助手，在 WhatsApp、iMessage、Slack、Telegram 等 20 多个渠道里带着同一份记忆应答你时用它——但一个 Gateway 就是一个信任域，互不信任的人不能共用一套部署。 | B（5/6） | [→](openclaw.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Octop](octop.zh.md) | ✅ | B（5/6） | 腾讯云的自托管多用户助手，飞书/企微加一个 Python 进程；两个月大，Agent 运行时是 GitHub 404 的 PyPI wheel。 |
| [PicoClaw](picoclaw.zh.md) | ✅ | B（6/6） | 可交叉编译的 Go 核心带聊天接入、工具和本地状态；换来小板子上的部署便利，不是本地模型推理，也不是默认开启的系统沙箱。 |
| [Hermes Agent](hermes-agent.zh.md) | ✅ | A（4/6） | 换来由你掌控的持续积累：有上限的记忆、自己写的技能、会话搜索和定时器；代价是行为不确定、没有企业治理（无 SSO、RBAC、审计），也没有 Lindy 记录。 |
| [OpenClaw](openclaw.zh.md) | ✅ | B（5/6） | 换来最广的聊天渠道覆盖，外加手机和桌面配套 App；代价是没有租户隔离、SSO 和审计日志，而且项目还不满一岁。 |

## 什么该放这里

自托管的常驻助手，主要通过既有消息渠道和定时任务接活。伴随客户端或仪表盘不改变此归属。仅有聊天或定时能力并不足够；桌面产物层、摄取式记忆界面与任务图工作区仍留在 [personal-assistants](../INDEX.zh.md)。
