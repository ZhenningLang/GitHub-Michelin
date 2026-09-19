---
name: HiveChat
slug: hivechat
repo: https://github.com/HiveNexus/HiveChat
category: team-chat
tags: [team-chat, multi-llm, self-hosted, nextjs, chatbot, admin-managed]
language: TypeScript
license: Apache-2.0
maturity: v0.1.0, active, ~1.2k stars (as of 2026-06)
last_verified: 2026-06-26
type: app
upstream:
  pushed_at: 2025-09-16T16:08:49Z
  default_branch: main
  default_branch_sha: 9d1e8ed614923dcf74414357e0fe53f66b016c0a
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:17:53Z
  overall: B
  overall_score: 2.75
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 290
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 499
        last_commit_age_days: 290
        cohort: app
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.409
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    adoption: { reason: no_package_structural }
---

# HiveChat

一款可自托管、由管理员统一管理的中小团队 AI 聊天应用：管理员一次配好多家大模型供应商（OpenAI、Claude、Gemini、DeepSeek、Ollama 以及任意 OpenAI 兼容服务），整个团队据此聊天，并按用户分组控制可见模型与 token 配额。

![hivechat — 健康度雷达](../../assets/health/hivechat.zh.svg)

## 何时使用

你是一家 5–50 人公司的技术负责人或 IT 管理员，团队不断要 ChatGPT/Claude 的使用权限。你不想给每家厂商都买席位、不想把原始 API key 发给每个人、也不想让用量无上限地跑；同时你更不愿把内部对话送进一个你无法审计的第三方 SaaS。你想要一个地方：API key 握在*你*手里，由你决定销售组和工程组各能看到哪些模型，给每个分组设月度 token 上限，并且用飞书/钉钉/企业微信登录来拉人进来，而不是再发一套账号密码。

HiveChat 正是为这个形态设计的。你部署一次（Docker Compose 自带 Postgres，或在 Vercel 一键部署），访问 `/setup` 用 `ADMIN_CODE` 建管理员账号，然后在管理后台加供应商和模型。用户登录后从你为其分组开放的模型里挑选，带图片理解、LaTeX/Markdown 渲染、DeepSeek 思维链展示和 MCP 工具服务器；与此同时你在管理端盯着配额。它占的是「自托管、覆盖多家模型 API 的团队前端」这个位置，既不是个人单用户的把玩工具，也不是从零搭聊天的框架。

## 何时不用

- **你是单个用户，想要本地/个人聊天客户端。** 它整套模型都是管理员对团队（Postgres、用户分组、配额、`/setup` 管理流程）。一个人用，Cherry Studio、Chatbox 这类桌面客户端或个人版 LibreChat 更轻。
- **你要纯本地、无服务器、离线运行。** HiveChat 强制依赖 PostgreSQL 后端和一个常驻的 Node/Next.js 服务进程，没有 SQLite 或完全本地的单二进制模式。
- **你需要成熟、久经考验、有长期发布历史的平台。** 它停在 `v0.1.0`，没有任何 git tag/release，默认分支最后一次 push 是 2025-09——早期阶段、单一开发方的节奏。
- **你要做无版权顾虑的 fork 或转售衍生品。** 许可证是 Apache-2.0 *外加商业附加条款*：构建并分发衍生作品需要向作者另行获取商业授权，这并非纯粹的 Apache-2.0。
- **你需要内置之外的可插拔企业 SSO（SAML/OIDC/LDAP）。** 认证为邮箱密码加飞书、钉钉、企业微信；未宣称支持通用企业 IdP 对接。
- **你要的是自托管 RAG / 文档知识库平台。** 它是覆盖模型 API（加 MCP 工具）的聊天前端，不是文档摄取 / 向量检索的知识库。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [LibreChat](../llm-chat-ui/librechat.zh.md) | ✅ | 需要更成熟、更大功能面，包括 RAG、assistants、代码解释器和多种认证后端时，选 LibreChat。 | MIT 许可且功能更广，但运维更重，也不如 HiveChat 专注小团队管理员-配额流程。 |
| [Open WebUI](../llm-chat-ui/open-webui.zh.md) | ✅ | 本地模型服务、RBAC 和 pipelines 比多云供应商配额更重要时，选 Open WebUI。 | 更广也更活跃，但甜点区是 Ollama/本地模型服务，而不是 HiveChat 的按组配额定位。 |
| Lobe Chat | 未收录 | 需要面向个人/进阶玩家的精致多服务商 UI、插件和自托管时，选 Lobe Chat。 | 不那么围绕 token 配额做集中式管理员团队治理。 |
| Chatbox / Cherry Studio | 未收录 | 每个人各自带 key，且不需要中心治理时，选桌面客户端。 | 没有中心管理员、分组、配额或共享服务端。 |
| ChatGPT Team / Claude Team（SaaS） | 未收录 | 能接受零运维和锁定单一模型家族时，选托管团队 SaaS。 | HiveChat 用自托管、多供应商选择和密钥/数据掌控换取这份便利的反面。 |

## 技术栈

- **语言：** TypeScript（约占仓库 99%），少量 CSS/JS/Dockerfile。
- **框架：** Next.js 14（App Router）+ React 18；UI 用 Ant Design 5 + Tailwind CSS。
- **认证：** NextAuth（next-auth 5 beta）配 Drizzle adapter；邮箱密码加飞书/钉钉/企业微信。
- **数据：** PostgreSQL，经 Drizzle ORM（`postgres` / `@neondatabase/serverless` 驱动）；用 `drizzle-kit` 做 schema push 和 seed 脚本。
- **模型 SDK：** `@anthropic-ai/sdk`、`openai`、`@google/generative-ai`，其余长尾走 OpenAI 兼容 HTTP（DeepSeek、Moonshot、火山、千帆、混元、智谱、OpenRouter、Grok、Ollama、SiliconFlow、自定义）。
- **附加：** `@modelcontextprotocol/sdk`（MCP，SSE 模式）、KaTeX + react-markdown/rehype 做数学/Markdown、`@agentic/tavily` 做网络搜索、`sharp` 处理图片、Zustand 管状态。

## 依赖

- **运行时：** Node.js（Next.js 14 服务端）——需常驻服务进程，不是静态站点。
- **数据库：** 强制 PostgreSQL。自托管可用 Docker Compose 自带 Postgres，或在 Vercel 一键路径上用 Neon serverless Postgres。schema 需用 `npm run initdb` 初始化/迁移（每次升版本也要重跑）。
- **配置：** 环境变量，包括首次经 `/setup` 路由建管理员所需的 `ADMIN_CODE`；供应商 API key 通过管理后台录入/存储。
- **可选：** Ollama 或任意 OpenAI 兼容端点接本地/额外模型；MCP 服务器（SSE）接工具；Tavily key 做网络搜索。

## 运维难度

**低到中。** 顺路径——`docker compose up -d`（app + Postgres）、设 `ADMIN_CODE`、跑 `initdb`、访问 `/setup`——对单个小部署确实简单，而 Vercel + Neon 这条路更是完全免去服务器管理。一旦你认真自托管数据库，难度升到**中**：Postgres 备份要你自己扛、每次升级都要迁移（`initdb` 得重跑，且没有发布版本可锁，只能跟着滚动的 `main`）、TLS/反向代理、众多供应商 key 的 secret 存储，以及企业登录（飞书/钉钉/企业微信）的回调配置。作为早期 `v0.1.0` 单一开发方项目，预期要读源码并跟仓库盯破坏性变更。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护——滑行中，并非明确活跃。** 最后一次 push 在 **2025-09**，截至 2026-06 已陈旧约 9 个月；未归档，但跨多个季度无提交是滑行/休眠信号，而非“活跃”。**完全没有 git tag 或 GitHub release**——版本是 `package.json` 里的 `0.1.0`，于是你跟的是一个移动（且停滞）的 `main`，没有 semver 可 pin。`[未验证]`
- **治理 / bus factor——单一厂商，体量很小。** 仓库为 **Organization** 所有（`HiveNexus/HiveChat`），但约 1.2k star[未验证]，且是早期单厂商节奏；路线图握在一个小团队手里。低采用 + 休眠，在这里是真实的弃坑风险组合。
- **年龄与 Lindy——年轻（创建于 2025-02，约 1.3 年）且如今沉寂。** 还不够老到拿到 Lindy 先验，而近期的沉寂进一步侵蚀了这点——一个停止 push 的年轻项目，趋向“过不了 Lindy”的象限，而非“强 Lindy”。在拿团队部署下注前，先确认仓库仍在推进。
- **风险标志——非纯净许可证。** 声称 Apache-2.0 **外加商业附加条款**：构建/分发衍生作品需向作者另行获取商业授权[未验证]。这*不是*纯 Apache-2.0——商用或 fork/转售前请先读 `LICENSE`。内部自托管使用似乎不受影响，但请确认。

## 存疑（未验证）

- [未验证] star 数约 1.2k、`pushedAt` 为 2025-09-16，取自 2026-06-26 的 GitHub API；GitHub star 不可靠、日期会漂移——请对照线上仓库重新核实。
- [未验证] 版本 `0.1.0` 取自 `package.json`；仓库**没有**任何 git tag 或 GitHub release，因此没有 semver 发布历史可锚定成熟度——考虑到最后一次 push 早于本次核实，「active」应谨慎看待。
- [未验证] 许可证是 Apache-2.0 **外加商业附加条款**（`LICENSE` 文件限制未经另行商业授权时构建/分发衍生作品）；frontmatter 为工具链写 `Apache-2.0`，但真实条款并非纯 Apache-2.0——商用/衍生前请先读 `LICENSE`。
- [未验证] 所支持的模型供应商清单、认证集成（飞书/钉钉/企业微信）与能力（MCP SSE、图片理解、网络搜索）均取自 README；依赖前请对照当前代码/管理后台核实。
- [推断] 对比结论（LibreChat/Open WebUI/Lobe Chat 更广或更成熟、桌面客户端缺中心管理）反映的是项目大致定位，不是基准化的正面对比；Open WebUI 已收录，LibreChat、Lobe Chat、桌面客户端和团队 SaaS 未收录。
- [推断] 「中小团队」规模（约 5–50 人）是示意性框定，不是文档明确的硬上限；未找到公开的规模/负载数据。
