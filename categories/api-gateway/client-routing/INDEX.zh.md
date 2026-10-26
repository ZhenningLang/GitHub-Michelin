# client-routing

> 分类节点。开发者客户端模型路由、供应商切换与 CLI/OAuth 登录桥接。
> ← 返回 [API / AI 网关](../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Funtool** | 只有精确命中“Windows + Claude Code + NVIDIA”代理路径，而且预打包工具比可审计性更重要时才用它；当前版本只提供二进制，无法从已发布源码重建。 | C（5/6） | [→](funtool.zh.md) |
| **Claude Code Router** | 开发者想从本地桌面/CLI 控制面，用条件规则与 fallback 让 Claude Code 等 coding agent 跨模型供应商路由时用它。 | B（6/6） | [→](claude-code-router.zh.md) |
| **CLIProxyAPI** | 想把消费级 CLI/OAuth 登录态复用成 OpenAI/Gemini/Claude 兼容 API 时用它——但这种复用本身带有服务条款与封号风险。 | B（5/6） | [→](cliproxyapi.zh.md) |
| **Magpie (yetone)** | 一个开发者想在菜单栏里把每个 coding agent（Claude Code、Codex、OpenCode 等约 28 个）切到任意厂商的模型时用它——只改单个配置键，再加一个本地协议翻译网关；但它只有约一周历史、单人维护，复用订阅有封号风险。 | C（5/6） | [→](magpie-model-router.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Funtool](funtool.zh.md) | ✅ | C（5/6） | 面向 Claude Code 与 NVIDIA 模型的窄 Windows 代理，当前实现只分发不透明二进制，没有可审计源码。 |
| [Claude Code Router](claude-code-router.zh.md) | ✅ | B（6/6） | 面向 coding agent 的本地、配置驱动模型路由，带桌面 UI；单人维护项目，且是持有供应商凭据的本地代理。 |
| [CLIProxyAPI](cliproxyapi.zh.md) | ✅ | B（5/6） | 把消费级 CLI/OAuth 账号变成覆盖多协议的 API；运行轻，但带有固化的服务条款/账号风险，且在主机上保存 token。 |
| [Magpie (yetone)](magpie-model-router.zh.md) | ✅ | C（5/6） | 给约 28 个 coding agent 用的桌面模型切换器，加一个在 Anthropic/OpenAI 协议间翻译的本地网关，订阅登录可当 provider；只有几天历史、单人维护、会自动更新。 |

## 什么该放这里

围绕开发者编码客户端模型配置、本地请求路由或 CLI/OAuth 登录复用的工具。项目密钥、预算、API 管理或 MCP 策略等共享服务网关放在[父分类](../INDEX.zh.md)。客户端路由不建立进程沙箱，也不代表供应商允许订阅复用。
