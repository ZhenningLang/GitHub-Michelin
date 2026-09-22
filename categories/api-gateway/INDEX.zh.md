# api-gateway

> 分类节点。路由、保护、限流并治理服务与 LLM 流量的 API / AI 网关。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Kong Gateway** | 基于 OpenResty/Nginx 的 API 网关，插件层把一个反向代理变成可编程边界：既管 REST/微服务，也从 3.x 起管 LLM/MCP 流量。 | A（5/6） | [→](kong.zh.md) |
| **Funtool** | 只有精确命中“Windows + Claude Code + NVIDIA”代理路径，而且预打包工具比可审计性更重要时才用它；当前版本只提供二进制，无法从已发布源码重建。 | C（5/6） | [→](funtool.zh.md) |
| **HarnessRouter** | 产品后端需要把 Codex、Claude Code、Hermes 等 harness 统一跑在一个 OpenAI Responses 兼容 API 之后时用它——但它仅约 6 周历史、UHP 标准由单一厂商维护、社区版会话共用同一容器。 | B（5/6） | [→](harnessrouter.zh.md) |
| **LiteLLM** | 多个应用或团队需要一个 OpenAI 兼容端点，带虚拟密钥、预算、花费追踪与故障转移时用它——但完整功能面并非全部 MIT（`enterprise/` 为商业许可）。 | A（4/6） | [→](litellm.zh.md) |
| **Claude Code Router** | 开发者想从本地桌面/CLI 控制面，用条件规则与 fallback 让 Claude Code 等 coding agent 跨模型供应商路由时用它。 | B（6/6） | [→](claude-code-router.zh.md) |
| **CLIProxyAPI** | 想把消费级 CLI/OAuth 登录态复用成 OpenAI/Gemini/Claude 兼容 API 时用它——但这种复用本身带有服务条款与封号风险。 | B（5/6） | [→](cliproxyapi.zh.md) |
| **APISIX** | 当你要 ASF 治理、配置由 etcd 动态驱动、插件在进程内的网关时用它——etcd 控制面也得你自己运维。 | A（5/6） | [→](apisix.zh.md) |
| **Envoy** | 当你要一个由 xDS 驱动的 L4/L7 数据面、且愿意自备控制面时用它——它比开箱即用的 API 网关更底层。 | A（5/6） | [→](envoy.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Kong Gateway](kong.zh.md) | ✅ | A（5/6） | 基于 OpenResty/Nginx 的 API 网关，插件层把一个反向代理变成可编程边界：既管 REST/微服务，也从 3.x 起管 LLM/MCP 流量。 |
| [Funtool](funtool.zh.md) | ✅ | C（5/6） | 面向 Claude Code 与 NVIDIA 模型的窄 Windows 代理，当前实现只分发不透明二进制，没有可审计源码。 |
| [HarnessRouter](harnessrouter.zh.md) | ✅ | B（5/6） | 用一个 OpenAI Responses 兼容 API 覆盖多种 agent harness，代价是约 6 周大的代码库、单一厂商协议、以及共用容器的会话隔离。 |
| [LiteLLM](litellm.zh.md) | ✅ | A（4/6） | provider 覆盖面与成本/治理能力最强的 LLM 网关，代价是 PostgreSQL + Redis 运维和 `enterprise/` 商业边界。 |
| [Claude Code Router](claude-code-router.zh.md) | ✅ | B（6/6） | 面向 coding agent 的本地、配置驱动模型路由，带桌面 UI；单人维护项目，且是持有供应商凭据的本地代理。 |
| [CLIProxyAPI](cliproxyapi.zh.md) | ✅ | B（5/6） | 把消费级 CLI/OAuth 账号变成覆盖多协议的 API；运行轻，但带有固化的服务条款/账号风险，且在主机上保存 token。 |
| [APISIX](apisix.zh.md) | ✅ | A（5/6） | ASF 顶级项目，基于 NGINX/OpenResty，配置由 etcd 动态驱动，进程内插件面很广；控制面是你必须自己运维的硬依赖。 |
| [Envoy](envoy.zh.md) | ✅ | A（5/6） | CNCF 毕业的 L4/L7 数据面，由 xDS 驱动；控制面与 API 管理策略层都由你自己带。 |
| Tyk / KrakenD / New API | 未收录 | — | 各页点到的其他自托管网关。 |

## 什么该放这里

挡在服务或 LLM 前面、做路由/鉴权/限流/可观测的 **API / AI 网关**。不含 agent 框架（见 `agent-frameworks`）。
