# api-gateway

> 分类节点。路由、保护、限流并治理服务与 LLM 流量的 API / AI 网关。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Kong Gateway** | 基于 OpenResty/Nginx 的 API 网关，插件层把一个反向代理变成可编程边界：既管 REST/微服务，也从 3.x 起管 LLM/MCP 流量。 | A（5/6） | [→](kong.zh.md) |
| **Funtool** | 只有精确命中“Windows + Claude Code + NVIDIA”代理路径，而且预打包工具比可审计性更重要时才用它；当前版本只提供二进制，无法从已发布源码重建。 | C（5/6） | [→](funtool.zh.md) |
| **HarnessRouter** | 产品后端需要把 Codex、Claude Code、Hermes 等 harness 统一跑在一个 OpenAI Responses 兼容 API 之后时用它——但它仅约 6 周历史、UHP 标准由单一厂商维护、社区版会话共用同一容器。 | B（5/6） | [→](harnessrouter.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Kong Gateway](kong.zh.md) | ✅ | A（5/6） | 基于 OpenResty/Nginx 的 API 网关，插件层把一个反向代理变成可编程边界：既管 REST/微服务，也从 3.x 起管 LLM/MCP 流量。 |
| [Funtool](funtool.zh.md) | ✅ | C（5/6） | 面向 Claude Code 与 NVIDIA 模型的窄 Windows 代理，当前实现只分发不透明二进制，没有可审计源码。 |
| [HarnessRouter](harnessrouter.zh.md) | ✅ | B（5/6） | 用一个 OpenAI Responses 兼容 API 覆盖多种 agent harness，代价是约 6 周大的代码库、单一厂商协议、以及共用容器的会话隔离。 |
| Tyk / KrakenD / Envoy / APISIX / LiteLLM / claude-code-router / CLIProxyAPI / New API | 未收录 | — | 各页提到的通用 API 网关，以及源码可见的 LLM 或 coding-agent 路由替代方案。 |

## 什么该放这里

挡在服务或 LLM 前面、做路由/鉴权/限流/可观测的 **API / AI 网关**。不含 agent 框架（见 `agent-frameworks`）。
