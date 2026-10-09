<p align="center"><img src="assets/logo.svg" width="160" alt="GitHub-Michelin logo"></p>

# GitHub-Michelin（GitHub 米其林）

**一个面向 coding agent 的开源项目「选型」自然语言索引。**
agent 收到任务时读这个索引来挑开源项目——重点是衡量每个候选*何时不该用*，而不只是它能干什么。

> English README: [README.md](README.md)

## 安装

把 GitHub-Michelin 的公开选型 skills 装进你的 coding agent：

- **`select-oss`** —— 为任务选择开源项目、库、工具、框架、模型或系统。
- **`select-agent-skills`** —— 选择可安装的 `SKILL.md` 包和 agent-skill 组合。

这两个 skill 默认通过 HTTP 读取公开索引（无需本地副本），在 clone 内也能直接读本地。

**任意 agent，经 [skills.sh](https://skills.sh)**（Claude Code、Codex、Cursor、OpenCode、Droid、
Kilo、Gemini CLI、Copilot 等 ~70 个 —— CLI 内置了每个 agent 的 skills 路径）：

```bash
# -g 装到全局（所有项目）；去掉 -g 则装到当前项目。用 -a 指定 agent，如 -a claude-code
npx skills add ZhenningLang/GitHub-Michelin -g
```

**手动**（无 Node）—— 把 skill 目录拷进你 agent 的 skills 目录，以 Claude Code 为例：

```bash
git clone https://github.com/ZhenningLang/GitHub-Michelin
cp -r GitHub-Michelin/skills/select-oss ~/.claude/skills/
cp -r GitHub-Michelin/skills/select-agent-skills ~/.claude/skills/
```

skills 从 `raw.githubusercontent.com/ZhenningLang/GitHub-Michelin/main/` 拉取页面；只安装很小的 `SKILL.md`，
因此体积极小、永远读到最新索引。对没有联网能力的 agent，skills 会回退到本地 clone。

维护者还有一个内部 **`project-harvester`** skill，位于 `skills/project-harvester/`，用于批量发现候选项目。
它标记了 `metadata.internal: true`，不属于正常公开安装面。

## 项目总表

完整索引，按分类分组。每个项目有一份英文页（`<slug>.md`）和一份中文页（`<slug>.zh.md`），点击直达。交互式浏览见 [INDEX.zh.md](INDEX.zh.md)；agent 从 [AGENTS.md](AGENTS.md) 开始。

### agent-tooling

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **beads** | 当 AI agent 跨会话丢失任务状态、你想在仓库里要一张可版本化、感知依赖的任务图时用它。 | MIT | B（5/6） | [中](categories/agent-tooling/work-state/beads.zh.md) · [EN](categories/agent-tooling/work-state/beads.md) |
| **CCPM** | 当一个功能大到单次 agent 会话装不下、你想要从 PRD 到 epic 再到 GitHub Issues 的成文规格，加上在 git worktree 里并行的多个 agent 时用它——但它强制依赖 GitHub Issues，且 2026-03 之后再无提交。 | MIT | C（4/5） | [中](categories/agent-tooling/work-state/ccpm.zh.md) · [EN](categories/agent-tooling/work-state/ccpm.md) |
| **Entire** | 想把 AI agent 会话以 Git checkpoint 形式与 commit 并列捕获、可搜索可回滚时用它。 | MIT | B（6/6） | [中](categories/agent-tooling/session-history/entire-cli.zh.md) · [EN](categories/agent-tooling/session-history/entire-cli.md) |
| **dsh-context** | 当你在 DeepSeek Harness 的 Web 界面里干活、需要看清每次请求的上下文窗口由什么组成——分类 token、压缩／剪枝事件、工具归属哪个插件、跨会话花费仪表盘——时用它；但它只支持 dsh、只有 Web 端、问世约 7 周且单人维护。 | Apache-2.0 | B（6/6） | [中](categories/agent-tooling/session-history/dsh-context.zh.md) · [EN](categories/agent-tooling/session-history/dsh-context.md) |
| **Ralph for Claude Code** | 想让 Claude Code 无人值守地啃完 fix_plan.md 清单、又要速率限制/熔断器/双条件退出闸门兜底时用它。 | MIT | C（5/6） | [中](categories/agent-tooling/work-state/ralph-claude-code.zh.md) · [EN](categories/agent-tooling/work-state/ralph-claude-code.md) |
| **Context Mode** | 当 coding agent 把上下文耗在原始工具输出上、你想要沙箱执行加熬过 compaction 的会话记忆时用它。 | Elastic-2.0 | D（6/6） | [中](categories/agent-tooling/work-state/context-mode.zh.md) · [EN](categories/agent-tooling/work-state/context-mode.md) |
| **Planning with Files** | 当长任务 agent 总在 /clear、上下文压缩或崩溃中丢失计划时用它把计划落到磁盘。 | MIT | B（5/6） | [中](categories/agent-tooling/work-state/planning-with-files.zh.md) · [EN](categories/agent-tooling/work-state/planning-with-files.md) |
| **LoopX** | 当 agent 的工作要跨天、跨重启、跨运行时持续推进，且需要持久目标、人工门禁、配额与证据治理每一轮时用它。 | Apache-2.0 | B（6/6） | [中](categories/agent-tooling/work-state/loopx.zh.md) · [EN](categories/agent-tooling/work-state/loopx.md) |
| **Token Optimizer** | 当 coding agent 的 token 烧在工具输出、重复读取和 compaction 丢失上、你又想要钩子层压缩、compaction 检查点和本地美元台账时用它——代价是接受其非商用许可证。 | PolyForm-NC-1.0.0 | C（5/6） | [中](categories/agent-tooling/work-state/token-optimizer.zh.md) · [EN](categories/agent-tooling/work-state/token-optimizer.md) |
| **Vercel Skills** | 当你想要一个 npm 风格的 CLI 来跨多个编码 agent 安装、查找、更新 SKILL.md 技能包时使用。 | MIT | A（6/6） | [中](categories/agent-tooling/harness-extensions/vercel-skills.zh.md) · [EN](categories/agent-tooling/harness-extensions/vercel-skills.md) |
| **AgentsView** | 当你同时跑多个编码 agent、想要本地优先的跨 agent 会话搜索与 token／成本分析时用它——但它问世仅数月、尚未到 1.0，要预期频繁变动。 | MIT | B（6/6） | [中](categories/agent-tooling/session-history/agentsview.zh.md) · [EN](categories/agent-tooling/session-history/agentsview.md) |
| **Agent Orchestrator** | 当你要监管多个跑在真实分支上的并行编码 agent、想要一个桌面控制面把每个隔离进 git worktree 并自动路由 CI／review／冲突反馈时用它——但它约 4.5 个月大、尚未到 1.0、单一 User 所有，且 daemon 是 loopback 无鉴权。 | Apache-2.0 | B（6/6） | [中](categories/agent-tooling/supervision-surfaces/agent-orchestrator.zh.md) · [EN](categories/agent-tooling/supervision-surfaces/agent-orchestrator.md) |
| **CLI-Anything** | 当你想让编码 agent 驱动只有 GUI 的软件、走由应用自身引擎支撑的生成式 CLI harness 时用它——但它仍在 1.0 之前，且每个 harness 由社区维护。 | Apache-2.0 | B（6/6） | [中](categories/agent-tooling/harness-extensions/cli-anything.zh.md) · [EN](categories/agent-tooling/harness-extensions/cli-anything.md) |
| **codex-chatgpt-web** | 当 Codex 配额先耗尽、而付费的 ChatGPT 网页订阅闲着，想让任务改记到 Web 套餐额度上时用它——但它是一条非官方、两个月大、单人维护的浏览器桥，ChatGPT 改 UI 或改政策随时能掐断。 | MIT | C（5/6） | [中](categories/agent-tooling/harness-extensions/codex-chatgpt-web.zh.md) · [EN](categories/agent-tooling/harness-extensions/codex-chatgpt-web.md) |
| **HEY CLI** | 当你的邮件跑在 HEY 上、想把它同时交给终端和编程 agent 时用它——第一方 CLI/TUI、自带 agent skill 和 MCP 服务；但它绑定 37signals 的付费账号、问世仅七个月、且只会说 HEY 的 API。 | MIT | B（6/6） | [中](categories/agent-tooling/harness-extensions/hey-cli.zh.md) · [EN](categories/agent-tooling/harness-extensions/hey-cli.md) |
| **SkillsGate** | 当你的 skill 散落在多个 agent 的隐藏目录里、想要一个桌面界面统一管理时用它——一份真身按 agent 建符号链接、接 skills.sh 目录、能 SSH 推送；但它单人维护、只支持全局安装，锁文件还和 `npx skills` 冲突。 | MIT | B（6/6） | [中](categories/agent-tooling/harness-extensions/skillsgate.zh.md) · [EN](categories/agent-tooling/harness-extensions/skillsgate.md) |
| **TanStack Intent** | 当你维护一个 npm 库、想把给 agent 的说明（`SKILL.md`）打进包里、与已装版本对应并在过期时被标出来时用它——只支持 npm/JS，仍是 v0.x，且只负责送达引导、不保证 agent 照做。 | MIT | B（6/6） | [中](categories/agent-tooling/harness-extensions/tanstack-intent.zh.md) · [EN](categories/agent-tooling/harness-extensions/tanstack-intent.md) |
| **Hermes Workspace** | 当你跑的是 Nous 的 hermes-agent、想把它的状态当 Web 驾驶舱用——聊天、memory、skills、终端、tmux swarm 派发、手机经 PWA/Tailscale 可达——但它的增强面板锚定 Hermes gateway/dashboard API、且问世仅约 6 个月时用它。 | MIT | B（5/6） | [中](categories/agent-tooling/supervision-surfaces/hermes-workspace.zh.md) · [EN](categories/agent-tooling/supervision-surfaces/hermes-workspace.md) |
| **Ekko Studio** | 当你同时跑 Hermes Agent **和** Claude Code／Codex 等编码 agent、想要一个本地控制台——单聊、@ 多 agent 的群聊房间、带审批关口的工作流画布、文件与终端——时用它——但它是 BSL-1.1（2029 年前禁止商用）、建仓一个月就从 MIT 改许可、约 5.5 个月大且基本一人编写。 | BUSL-1.1 | D（6/6） | [中](categories/agent-tooling/supervision-surfaces/ekko-studio.zh.md) · [EN](categories/agent-tooling/supervision-surfaces/ekko-studio.md) |
| **CloudCLI (Claude Code UI)** | 当你的大脑是 Claude Code / Codex / Cursor CLI、想要这些会话的浏览器/移动驾驶舱（文件、终端、git）时用它——但它是 AGPL-3.0-or-later、单人操作形态。 | AGPL-3.0-or-later | B（6/6） | [中](categories/agent-tooling/supervision-surfaces/claudecodeui.zh.md) · [EN](categories/agent-tooling/supervision-surfaces/claudecodeui.md) |
| **Plannotator** | 当 agent 的产出（计划、diff、HTML 产物）必须由人批注或批准、并把批注当作 agent 的下一条指令发回去时用它——但它只有 9 个月大、pre-1.0、单人维护，且开源版的团队分享路线正被托管产品取代。 | MIT OR Apache-2.0 | B（6/6） | [中](categories/agent-tooling/supervision-surfaces/plannotator.zh.md) · [EN](categories/agent-tooling/supervision-surfaces/plannotator.md) |
| **Pi Web** | 当你的编码 agent 是 pi、想要在它自己的磁盘会话、模型与项目文件之上加一层浏览器工作台——恢复／分支会话、查 diff 和 worktree——时用它——但它约 6 个月大、pre-1.0、单人维护，且锚定 pi 的数据目录。 | MIT | B（6/6） | [中](categories/agent-tooling/supervision-surfaces/pi-web.zh.md) · [EN](categories/agent-tooling/supervision-surfaces/pi-web.md) |
| **Whiteboard** | 当你要 coding agent 亲笔「画」出评审——对钉住的分支生成可交互 RFC，图、引文与代码片段都能点回本地 checkout 的确切行——时用它——但它问世约 6 周、v0.1.x，且评审面只读。 | MIT | B（5/6） | [中](categories/agent-tooling/supervision-surfaces/whiteboard.zh.md) · [EN](categories/agent-tooling/supervision-surfaces/whiteboard.md) |
| **Paperclip** | 当你手上已有一支常驻 agent 团队（Claude Code、Codex、OpenClaw、shell／HTTP 机器人），需要一个自托管看板按心跳唤醒它们、一张工单只许一个 agent 领、超预算自动暂停时用它——但它约 7 个月大、已公开 12 条安全公告，且 Windows 上本地运行不可用。 | MIT | B（5/6） | [中](categories/agent-tooling/supervision-surfaces/paperclip.zh.md) · [EN](categories/agent-tooling/supervision-surfaces/paperclip.md) |
| **Agentation** | 当你的 React 应用肯背一个开发依赖、要点选批注外加 React 组件路径与 dev 构建 `file:line`、再经 MCP 同步给任意终端 agent 时用它——采用度断层第一（4.8k 星），许可非 OSI。 | PolyForm-Shield-1.0.0 | C（4/6） | [中](categories/agent-tooling/ui-annotation/agentation.zh.md) · [EN](categories/agent-tooling/ui-annotation/agentation.md) |
| **Vibe Annotations** | 当看见 UI bug 的人不碰代码时用它：Chrome 扩展批注加后台服务，经 MCP 喂给 Claude Code / Cursor / Codex，还带队友文件分享——但单人作者、PolyForm Shield 许可。 | PolyForm-Shield-1.0.0 | C（5/6） | [中](categories/agent-tooling/ui-annotation/vibe-annotations.zh.md) · [EN](categories/agent-tooling/ui-annotation/vibe-annotations.md) |
| **Pointa** | 当「不改应用代码」是铁律、且 MIT 是许可硬要求时用它——Chromium 扩展加会讲 MCP 的本地服务，还能把 Node 后端的 console 日志一并装进 bug 报告；约 6 个月无更新。 | MIT | C（5/6） | [中](categories/agent-tooling/ui-annotation/pointa.zh.md) · [EN](categories/agent-tooling/ui-annotation/pointa.md) |
| **earmark** | 当你要确定性的源码证据——构建期 `file:line` 打戳（Vite/Next/Svelte）、CSS 规则行解析、图钉变色的 acknowledge/resolve MCP 闭环——且能接受一个公开历史只有两天的 0 星项目时用它。 | MIT | C（5/6） | [中](categories/agent-tooling/ui-annotation/earmark.zh.md) · [EN](categories/agent-tooling/ui-annotation/earmark.md) |
| **patch-mark** | 当你要用两行零依赖批注一个不属于你的页面、并希望批注被明确当作「不可信证据」喂给 agent、MCP 面默认只读时用它——两个月大的单人 MIT 项目。 | MIT | C（5/6） | [中](categories/agent-tooling/ui-annotation/patch-mark.zh.md) · [EN](categories/agent-tooling/ui-annotation/patch-mark.md) |
| **markupkit** | 当你的 UI 反馈是空间性的——圈、箭头、删除线、拖拽布局 diff 以结构化增量递过去——且不惜自己接管一个自述休眠的学习型项目时用它。 | MIT | C（5/6） | [中](categories/agent-tooling/ui-annotation/markupkit.zh.md) · [EN](categories/agent-tooling/ui-annotation/markupkit.md) |
| **weave** | 并行 agent 或分支总在同一文件里互不相干的改动上卡住合并、想让 git 比函数和键而不是比行时用它——但它约 8 个月大、pre-1.0、单一核心作者，引擎判定仍在版本间变动。 | MIT OR Apache-2.0 | B（6/6） | [中](categories/agent-tooling/concurrent-editing/weave.zh.md) · [EN](categories/agent-tooling/concurrent-editing/weave.md) |
### sandboxing

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **gVisor** | 不可信容器必须与宿主内核隔离、又不想跑虚拟机时用它——不需要 KVM，且容器工作流不变。 | Apache-2.0 | A（6/6） | [中](categories/sandboxing/gvisor.zh.md) · [EN](categories/sandboxing/gvisor.md) |
| **Kata Containers** | 想让每个 pod 在轻量虚拟机里拿到真内核、同时 Kubernetes 保持常规 RuntimeClass 工作流时用它。 | Apache-2.0 | A（6/6） | [中](categories/sandboxing/kata-containers.zh.md) · [EN](categories/sandboxing/kata-containers.md) |
| **Firecracker** | 你在自建沙箱层、想要一个带控制 API 的极简 KVM microVM 原语（而不是容器运行时）时用它。 | Apache-2.0 | A（6/6） | [中](categories/sandboxing/firecracker.zh.md) · [EN](categories/sandboxing/firecracker.md) |
| **OpenSandbox** | 当你需要自托管隔离沙箱、在 K8s 规模上运行不可信的 agent 生成代码（带出口管控和凭证保险库）时用它——但仓库仅数月之龄（2025-12 创建），其 API 与 Lindy 长期记录尚未经检验。 | Apache-2.0 | B（6/6） | [中](categories/sandboxing/opensandbox.zh.md) · [EN](categories/sandboxing/opensandbox.md) |
| **E2B** | 当 agent 需要跑 AI 生成的代码、你想要把沙箱做成 SDK 时用它——默认托管，必须落在自己账号时用 Terraform 自托管到 AWS／GCP。 | Apache-2.0 | A（6/6） | [中](categories/sandboxing/e2b.zh.md) · [EN](categories/sandboxing/e2b.md) |
| **Agent Substrate** | 当你有一大批大部分时间闲置的有状态 agent 会话、想把它们多路复用到少数预热 Kubernetes pod 上（闲置时存档、按需恢复）时用它——但它处于 1.0 之前、API 不稳定、安全加固尚未做。 | Apache-2.0 | B（5/6） | [中](categories/sandboxing/substrate.zh.md) · [EN](categories/sandboxing/substrate.md) |
| **Modal client SDK** | 想要 serverless 容器、GPU 与沙箱而什么都不用运维时用它——客户端 SDK 开源，平台闭源且只能托管。 | Apache-2.0 | A（6/6） | [中](categories/sandboxing/modal-client.zh.md) · [EN](categories/sandboxing/modal-client.md) |
| **Microsandbox** | 沙箱必须跑在你已有的硬件上时用它——一个二进制或一个 SDK、普通 OCI 镜像、每沙箱出口策略与宿主侧 secret，无守护进程、无集群——但宿主需要 KVM／Apple Silicon／WHP，且仍处于 beta。 | Apache-2.0 | A（6/6） | [中](categories/sandboxing/microsandbox.zh.md) · [EN](categories/sandboxing/microsandbox.md) |
| **Monty** | 模型写的 Python 要在每个请求里跑进你自己的应用时用它——pip 装进来的 Rust 解释器毫秒级开出全新沙箱会话，里面没有文件系统／网络／环境变量，除非你亲手传入——但它只支持一个 Python 子集、没有第三方包，隔离边界是语言本身而非操作系统。 | MIT | A（6/6） | [中](categories/sandboxing/monty.zh.md) · [EN](categories/sandboxing/monty.md) |
| **Cloudflare Computer** | Cloudflare Workers 上的 agent 需要一个能活下去的工作目录时用它——文件放在 Durable Object 的 SQLite 里，一个 exec API 在容器或隔离环境里对它们跑命令或代码——代价是明说的 preview API、约 10 GB 的 workspace 上限和单一厂商锁定。 | MIT | B（6/6） | [中](categories/sandboxing/cloudflare-computer.zh.md) · [EN](categories/sandboxing/cloudflare-computer.md) |
| **Agent Sandbox** | agent 沙箱必须是普通 Kubernetes 对象时用它——每个沙箱一个 CRD，加上模板和预热池，申领直接拿走已起好的 pod——但隔离来自你配置的 gVisor／Kata 运行时类而非项目本身，API 也还在 v1beta1。 | Apache-2.0 | A（6/6） | [中](categories/sandboxing/agent-sandbox.zh.md) · [EN](categories/sandboxing/agent-sandbox.md) |

### serverless

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Knative Serving** | 当 HTTP 服务一天里大部分时间闲着、你想要按 revision 的发布加缩容到零，又不想采用某个 FaaS 产品时用它。 | Apache-2.0 | B（6/6） | [中](categories/serverless/knative-serving.zh.md) · [EN](categories/serverless/knative-serving.md) |

### document-management

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **paperless-ngx** | 想自托管对扫描纸质资料做 OCR + 打标签 + 全文检索时用它。 | GPL-3.0 | B（6/6） | [中](categories/document-management/paperless-ngx.zh.md) · [EN](categories/document-management/paperless-ngx.md) |
| **copyparty** | 需要单文件便携、带断点续传/去重/多协议访问的文件服务器时用它——但它不做 OCR 文档检索。 | MIT | B（6/6） | [中](categories/document-management/copyparty.zh.md) · [EN](categories/document-management/copyparty.md) |
| **Twake Drive** | 当你想在 Twake/Cozy 栈里要一个 Google-Drive 形态的自托管文件网盘（而非 OCR 归档）时用它。 | AGPL-3.0 | B（5/6） | [中](categories/document-management/twake-drive.zh.md) · [EN](categories/document-management/twake-drive.md) |
| **Immich** | 当家里有服务器、想在自己的硬盘上复刻 Google Photos 那套手机自动备份、共享时间线、人脸和按内容搜索时用它——但升级和 3-2-1 备份归你管，要约 6 GB 内存，照片在服务器上是明文。 | AGPL-3.0 | B（6/6） | [中](categories/document-management/immich.zh.md) · [EN](categories/document-management/immich.md) |

### on-device-ml

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **LiteRT-LM** | 想用 Google LiteRT 运行时在手机/笔记本/边缘（CPU/GPU/NPU）上跑 Gemma 级 LLM 时用它。 | Apache-2.0 | B（6/6） | [中](categories/on-device-ml/litert-lm.zh.md) · [EN](categories/on-device-ml/litert-lm.md) |
| **BitNet** | 当你要在 x86/ARM 笔记本上离线、快速、低能耗地用 CPU 跑原生三值（1.58-bit） LLM 时使用。 | MIT | B（5/6） | [中](categories/on-device-ml/bitnet.zh.md) · [EN](categories/on-device-ml/bitnet.md) |
| **Google AI Edge Gallery** | 当你想在真机上先体验和基准测试端侧 Gemma LLM、为是否自建集成去风险时用它。 | Apache-2.0 | B（6/6） | [中](categories/on-device-ml/ai-edge-gallery.zh.md) · [EN](categories/on-device-ml/ai-edge-gallery.md) |
| **TimesFM** | 当你需要在本地 CPU/GPU 上对时间序列做零样本预测、又不想逐数据集训练时用它。 | Apache-2.0 | A（5/6） | [中](categories/on-device-ml/timesfm.zh.md) · [EN](categories/on-device-ml/timesfm.md) |
| **MiniCPM-V** | 当你需要小体积、可在端侧/边缘运行的多模态（图像+视频）理解时用它——注意逐权重许可。 | Apache-2.0 | A（4/6） | [中](categories/on-device-ml/minicpm-v.zh.md) · [EN](categories/on-device-ml/minicpm-v.md) |
| **MiniCPM** | 当聊天、编码或调工具的助手必须以 1–2B 体量离线跑在笔记本、手机或 CPU 盒子上时用它（MiniCPM5，Apache-2.0，GGUF 0.66–1.56GB）——但 4 bit 版要调采样参数，并选能解析其 XML 工具调用的运行时。 | Apache-2.0 | B（5/6） | [中](categories/on-device-ml/minicpm.zh.md) · [EN](categories/on-device-ml/minicpm.md) |
| **Stable Diffusion WebUI** | 当你想在 NVIDIA GPU 上用一个标签页式本地 Web UI、完整调参并借用庞大的 A1111 扩展生态做 SD 1.5/SDXL 出图时用它——但核心自 2024-07 起再无提交，新模型家族请用 ComfyUI。 | AGPL-3.0 | D（4/6） | [中](categories/on-device-ml/local-image-generation/stable-diffusion-webui.zh.md) · [EN](categories/on-device-ml/local-image-generation/stable-diffusion-webui.md) |
| **ComfyUI** | 当你在自己的 GPU 上用开放权重模型生成图像或视频，需要一张可复现的节点图（ControlNet、LoRA、局部重绘、放大），并且只重算改动过的部分时用它——但它没有登录、配额和租户隔离。 | GPL-3.0 | B（5/6） | [中](categories/on-device-ml/local-image-generation/comfyui.zh.md) · [EN](categories/on-device-ml/local-image-generation/comfyui.md) |
| **MLX / mlx-lm** | 当你在 Apple 芯片的 Mac 上试 Hugging Face 新模型，想用一个 Python 包完成生成、量化和 LoRA 微调、不必先转 GGUF 时用它——但 mlx_lm.server 不适合生产或多用户服务。 | MIT | B（6/6） | [EN](categories/on-device-ml/mlx-mlx-lm.md) · [中](categories/on-device-ml/mlx-mlx-lm.zh.md) |
| **Needle** | 当需要一个小体积端侧模型离线完成英文工具调用、类型化抽取与嵌入时用它——29–121M 参数，但基座模型需要微调，拒绝类请求要自建守卫。 | Apache-2.0 | B（4/6） | [中](categories/on-device-ml/needle.zh.md) · [EN](categories/on-device-ml/needle.md) |
| **stable-diffusion.cpp** | 当你要把图片/视频扩散生成做成一个不带 Python 的原生二进制，嵌进自己的应用或发到混杂的 CPU/AMD/Mac/NVIDIA 机器上时用它——但功能集固定、没有语义化版本，自带服务无鉴权且单线程排队。 | MIT | A（6/6） | [中](categories/on-device-ml/local-image-generation/stable-diffusion-cpp.zh.md) · [EN](categories/on-device-ml/local-image-generation/stable-diffusion-cpp.md) |
| **BirdNET-Go** | 当你想在树莓派 4/5 或小主机上搭一个全天候的鸟类（及蝙蝠）声音监测站，带本地网页仪表盘、多路麦克风和 RTSP 音源、MQTT 与 Home Assistant 告警时用它——但代码和模型都禁止商用（CC BY-NC-SA），默认安装跟的是单人维护的每夜构建，批量文件分析要交给别的工具。 | CC-BY-NC-SA-4.0 | B（5/6） | [中](categories/on-device-ml/birdnet-go.zh.md) · [EN](categories/on-device-ml/birdnet-go.md) |
| **uzu** | 当你要把大模型直接跑在自己的 iOS/macOS 应用里，想要一个 Swift/Python/TS SDK 替你挑模型、下载转换好的版本并在苹果 GPU 上运行时用它——但系统要 26.4 以上，只用 Mirai 自有模型格式和托管注册服务，遥测默认开启。 | MIT | B（6/6） | [中](categories/on-device-ml/uzu.zh.md) · [EN](categories/on-device-ml/uzu.md) |

### function-calling

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Functionary** | 只把它当作开源 JSON Schema 函数调用的历史参考——它已废弃；生产环境请用 vLLM/SGLang 服务当前模型，或走端侧 Needle。 | MIT | B（4/6） | [中](categories/function-calling/functionary.zh.md) · [EN](categories/function-calling/functionary.md) |

### web-automation

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **page-agent** | 想在页内用自然语言、通过直接读写 DOM 控制 Web 界面、且无需后端时用它。 | MIT | B（6/6） | [中](categories/web-automation/agent-browser-tools/page-agent.zh.md) · [EN](categories/web-automation/agent-browser-tools/page-agent.md) |
| **Chrome DevTools MCP** | 当 agent 需要驱动并用 DevTools 检查真实 Chrome（性能 trace、网络、控制台、堆内存）时使用。 | Apache-2.0 | A（6/6） | [中](categories/web-automation/agent-browser-tools/chrome-devtools-mcp.zh.md) · [EN](categories/web-automation/agent-browser-tools/chrome-devtools-mcp.md) |
| **Agent Browser** | 当 agent 需要靠 shell 命令通过 CDP 驱动真实 Chrome、用稳定元素引用而非 CSS 选择器操作网页时使用。 | Apache-2.0 | B（5/6） | [中](categories/web-automation/agent-browser-tools/agent-browser.zh.md) · [EN](categories/web-automation/agent-browser-tools/agent-browser.md) |
| **Selenium** | 当你需要跨浏览器、跨语言的 WebDriver 自动化时用它——现代单浏览器体验 Playwright/Cypress 更顺手。 | Apache-2.0 | A（6/6） | [中](categories/web-automation/browser-driver-frameworks/selenium.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/selenium.md) |
| **PhantomJS** | 只在遗留 CI 任务、截图服务或爬虫已经钉死它、你得撑到迁移完成时用它——但它已归档、2018 年起停止开发，新工作请用 Puppeteer 或 Playwright 驱动的无头 Chrome。 | BSD-3-Clause | C（5/6） | [中](categories/web-automation/browser-driver-frameworks/phantomjs.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/phantomjs.md) |
| **Selenium Wire** | 当一套遗留的 Python Selenium 代码已经靠它读取或改写浏览器后台的请求和响应时用它——但它已归档、不再维护，新项目应改用 Selenium 4 的 CDP/BiDi 网络能力或 Playwright。 | MIT | D（5/6） | [中](categories/web-automation/browser-driver-frameworks/selenium-wire.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/selenium-wire.md) |
| **nodriver** | 当 Python 异步代码需要绕过 WebDriver、直接控制 Chromium CDP 时用它——只支持 Chromium、采用 AGPL-3.0，且不是完整测试框架。 | AGPL-3.0 | C（5/6） | [中](categories/web-automation/browser-driver-frameworks/nodriver.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/nodriver.md) |
| **undetected-chromedriver** | 只在要让现成的 Python Selenium 代码绕开 chromedriver 自带的检测标记、又没法重写时用它——PyPI 最后一版停在 2024-02，新项目该用 nodriver 或 SeleniumBase UC Mode。 | GPL-3.0 | C（4/6） | [中](categories/web-automation/browser-driver-frameworks/undetected-chromedriver.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/undetected-chromedriver.md) |
| **Moli** | 当结构优先的 agent 机群要用约 100 MB 的单进程浏览、真实布局与截图只是按需打开的例外，协议面要 CDP+WebDriver 时用它。 | Apache-2.0 OR MIT | B（6/6） | [中](categories/web-automation/browser-driver-frameworks/moli.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/moli.md) |
| **Lightpanda** | 当批量 JS+DOM 提取永远不看像素时用它：无渲染引擎的 Zig 浏览器，自报比 Chrome 省 16 倍内存，带 CDP/BiDi/MCP。 | AGPL-3.0 | B（6/6） | [中](categories/web-automation/browser-driver-frameworks/lightpanda.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/lightpanda.md) |
| **Obscura** | 当对抗性抓取要一个自带 stealth、常开渲染、单文件的 Rust 浏览器时用它。 | Apache-2.0 | B（6/6） | [中](categories/web-automation/browser-driver-frameworks/obscura.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/obscura.md) |
| **Camoufox** | 当 Playwright 爬虫因为浏览器本身被识别而被拦时用它：在引擎层伪装指纹的 Firefox 分支——只有 Firefox、约 1.3 GB、自己声明不适合稳定生产。 | MPL-2.0 | B（6/6） | [中](categories/web-automation/browser-driver-frameworks/camoufox.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/camoufox.md) |
| **rebrowser-playwright** | 只在一个钉在 1.52 的现有 Node.js Playwright 任务因 Chrome 上的 `Runtime.Enable` CDP 信号被识别时用它——预先打好补丁的直接替换包，自 2025-05 起冻结。 | Apache-2.0 | D（3/6） | [中](categories/web-automation/browser-driver-frameworks/rebrowser-playwright.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/rebrowser-playwright.md) |
| **Playwright MCP** | 当支持 MCP 的 agent 需要厂商官方、基于无障碍树快照的确定性浏览器自动化时用它——适合有状态的探索式回路；微软自家 README 把高吞吐 coding agent 引向它的 CLI 兄弟。 | Apache-2.0 | A（6/6） | [中](categories/web-automation/playwright-family/playwright-mcp.zh.md) · [EN](categories/web-automation/playwright-family/playwright-mcp.md) |
| **Playwright CLI** | 当 coding agent（Claude Code、Copilot）需要便宜、token 高效的浏览器命令并装好 SKILLs 时用它——微软自己推荐给 coding agent 的路径；v0.1.x，刚重新定位。 | Apache-2.0 | A（6/6） | [中](categories/web-automation/playwright-family/playwright-cli.zh.md) · [EN](categories/web-automation/playwright-family/playwright-cli.md) |
| **OpenCLI** | 当 agent 必须操作藏在你登录态后面的站点时用它——经扩展+daemon 桥接你已登录的 Chrome，并把站点工作流固化成可复用 CLI 命令；要预期适配器 churn 和真实的信任面。 | Apache-2.0 | B（6/6） | [中](categories/web-automation/agent-browser-tools/opencli.zh.md) · [EN](categories/web-automation/agent-browser-tools/opencli.md) |
| **Browser Harness** | 当 coding agent 必须经 CDP 驱动你已经登录的 Chrome、并把缺的帮手写进本地 workspace 时用它——仍是 Alpha、遥测默认开、没有内层 agent 循环。 | MIT | A（6/6） | [中](categories/web-automation/agent-browser-tools/browser-harness.zh.md) · [EN](categories/web-automation/agent-browser-tools/browser-harness.md) |
| **browser-use** | 当你要在自己的 Python 代码里操作管不了的网站，想把一句话任务交给大模型 agent、而不是给每个站写死选择器时用它——但每一步都是按 token 计费、路径不确定的模型往返；稳定的高频流程还是写 Playwright 脚本。 | MIT | A（6/6） | [EN](categories/web-automation/agent-browser-tools/browser-use.md) · [中](categories/web-automation/agent-browser-tools/browser-use.zh.md) |
| **BrowserSkill** | 当 agent 必须在不动你现有窗口的前提下操作你已登录的 Chromium 时用它——借你已打开的页签要先经你确认，遇到登录或验证码把控制权交还给你；没有确定性站点适配器层，信任面与 OpenCLI 同级（扩展+daemon）。 | MIT | B（6/6） | [中](categories/web-automation/agent-browser-tools/browserskill.zh.md) · [EN](categories/web-automation/agent-browser-tools/browserskill.md) |
| **Playwright** | 当端到端测试时好时坏，又要用一套 API 覆盖 Chromium、Firefox 和 WebKit，靠自动等待、隔离上下文和可回放的 trace 治理不稳定时用它——但它的 Firefox 和 WebKit 是打补丁的构建，要在品牌版 Safari 或 Firefox 上认证需用 Selenium 或真机。 | Apache-2.0 | A（5/6） | [EN](categories/web-automation/playwright-family/playwright.md) · [中](categories/web-automation/playwright-family/playwright.zh.md) |
| **Puppeteer** | 当 Node.js 任务本来就绑定 Chrome（服务端渲染 PDF、定时截图、预渲染单页应用、脚本化登录下载），并且你想用 Chrome 团队维护的参考 CDP 客户端时用它——但它不支持 Safari/WebKit，也没有测试运行器，这两样要用 Playwright。 | Apache-2.0 | A（6/6） | [EN](categories/web-automation/browser-driver-frameworks/puppeteer.md) · [中](categories/web-automation/browser-driver-frameworks/puppeteer.zh.md) |
| **Jev Ultrafast** | 当每步延迟是硬约束、且能接受托管判定 API 时用它——一次请求同时给出每一步的操作与目标元素。 | MIT | C（6/6） | [中](categories/web-automation/agent-browser-tools/jev-ultrafast.zh.md) · [EN](categories/web-automation/agent-browser-tools/jev-ultrafast.md) |
| **PinchTab** | 当 agent 需要一个常驻本地的浏览器服务、经 CLI/HTTP/MCP 编排多个相互隔离的 Chrome 实例与配置档、且要默认全关的能力闸门加提示注入扫描时用它——pre-1.0，实际单维护者。 | MIT | B（6/6） | [中](categories/web-automation/agent-browser-tools/pinchtab.zh.md) · [EN](categories/web-automation/agent-browser-tools/pinchtab.md) |
| **invisible_playwright_mcp** | 当 MCP 助手总被验证码和机器人墙拦住时用它——它驱动一个 C++ 层打过补丁、指纹由种子推导的隐身 Firefox；只支持 Windows/Linux，单人维护，星数继承自改名前的投简历机器人仓库。 | MIT | B（5/6） | [中](categories/web-automation/agent-browser-tools/invisible-playwright-mcp.zh.md) · [EN](categories/web-automation/agent-browser-tools/invisible-playwright-mcp.md) |
| **playwright-bot-bypass** | 当编码 agent 写的脚本在你自己的桌面机上被判成机器人时用它——一个 skill 加一个工厂函数，经 rebrowser-playwright 驱动你带窗口的真 Chrome；必须有显示器，对 IP、行为和验证码类拦截无效，核心依赖自 2025-05 起未发版。 | MIT | C（5/6） | [中](categories/web-automation/agent-browser-tools/playwright-bot-bypass.zh.md) · [EN](categories/web-automation/agent-browser-tools/playwright-bot-bypass.md) |
| **camofox-browser** | 当一个多用户、常驻的 agent 总被弹验证码时用它——在 Camoufox 反检测 Firefox 之上的常驻 REST/MCP/OpenClaw 服务，带按用户隔离的会话和按编号操作的快照；路由默认敞开、遥测默认开启，提交集中在一人，项目才八个月。 | MIT | B（6/6） | [中](categories/web-automation/agent-browser-tools/camofox-browser.zh.md) · [EN](categories/web-automation/agent-browser-tools/camofox-browser.md) |

### llm-training

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **LlamaFactory** | 面向 100+ LLM/VLM 的零代码统一微调框架，自带 Gradio Web UI(LlamaBoard)，覆盖 LoRA/QLoRA/全量微调及 SFT→RLHF 全链路。 | Apache-2.0 | B（6/6） | [中](categories/llm-training/llamafactory.zh.md) · [EN](categories/llm-training/llamafactory.md) |
| **Unsloth** | 基于自定义 Triton kernel 的单卡 LoRA/QLoRA/RL 微调工具，号称在 500+ 开源 LLM 上约 2x 提速并大幅省显存。 | Apache-2.0 | B（5/6） | [中](categories/llm-training/unsloth.zh.md) · [EN](categories/llm-training/unsloth.md) |
| **ART (Agent Reinforcement Trainer)** | 当 Python 命令行需要纯 Python 的 figlet 风格 ASCII 文字横幅、且不依赖系统二进制时用它——但它只做文字转艺术字（不做图片转 ASCII），也不与 figlet 字体完全一致。 | Apache-2.0 | C（5/6） | [中](categories/llm-training/art.zh.md) · [EN](categories/llm-training/art.md) |
| **Agent Lightning** | 微软出品的强化学习/优化训练器，把 agent 执行与训练后端解耦，几乎零改动地优化任意框架（LangChain、AutoGen、OpenAI SDK 等）构建的 agent。 | MIT | B（5/6） | [中](categories/llm-training/agent-lightning.zh.md) · [EN](categories/llm-training/agent-lightning.md) |
| **Colossal-AI** | 当你需要用张量/流水线/ZeRO 并行在多 GPU 上训练/微调大模型时用它——单卡 LoRA 用它是杀鸡用牛刀。 | Apache-2.0 | B（6/6） | [中](categories/llm-training/colossalai.zh.md) · [EN](categories/llm-training/colossalai.md) |
| **Hugging Face TRL** | 当你的技术栈本来就是 transformers + datasets + PEFT，想用 Python 调用经过测试的 SFT、DPO、GRPO 训练器类时用它——但在多机上对 70B 以上或 MoE 模型做 RL，生成吞吐得靠 verl。 | Apache-2.0 | A（6/6） | [EN](categories/llm-training/trl.md) · [中](categories/llm-training/trl.zh.md) |
| **torchtune** | 当你要把现有的 torchtune LoRA/QLoRA 或 DPO 流水线锁在 v0.6.1 继续跑，或想读纯 PyTorch 写成的微调训练循环时用它——但 Meta 已于 2025 年 7 月停止功能开发，新项目不要拿它起步。 | BSD-3-Clause | B（6/6） | [EN](categories/llm-training/torchtune.md) · [中](categories/llm-training/torchtune.zh.md) |
| **Axolotl** | 当团队要反复在多张 GPU 上做微调（LoRA、全参、DPO），想把每次训练写进一个 YAML 而不是手拼 transformers、PEFT 和 DeepSpeed 胶水时用它——但单张消费级显卡、要界面或要写自定义训练循环时不适合。 | Apache-2.0 | B（6/6） | [EN](categories/llm-training/axolotl.md) · [中](categories/llm-training/axolotl.zh.md) |
| **verl** | 当你要在 GPU 集群上对 7B 到 235B 的模型跑 PPO、GRPO 或 DAPO，且每一步都是生成耗时压过训练时用它——但只做 SFT/DPO 或只有一张消费级显卡时，它的搭建成本远高于 TRL 或 Unsloth。 | Apache-2.0 | B（6/6） | [EN](categories/llm-training/verl.md) · [中](categories/llm-training/verl.zh.md) |
| **Soup** | 当一份 YAML 要把微调从 JSONL 一路带到可服务、可导出的模型，而底座装不进你的显卡时用它——当配置契约必须跨版本稳定、或模型本就装得下且要追求速度时不用。 | Apache-2.0 | B（6/6） | [中](categories/llm-training/soup.zh.md) · [EN](categories/llm-training/soup.md) |
| **Miles** | 当你在多节点 GPU 上用 SGLang 生成、Megatron 训练去做大 MoE 模型的强化学习，并需要训推两侧保持一致时用它——单卡、只做 SFT、推理栈是 vLLM 或要求 API 稳定时不用。 | Apache-2.0 | B（5/6） | [中](categories/llm-training/miles.zh.md) · [EN](categories/llm-training/miles.md) |
| **MiniMind** | 用约 3.2k 行手写 PyTorch 把 64M LLM 端到端训一遍（分词器、预训练、SFT、LoRA、MoE、DPO/GRPO、Tool Call 与 Agentic RL），一下午能读完；它是课程，产出的模型是教学产物而非可用模型。 | Apache-2.0 | A（5/6） | [中](categories/llm-training/study-and-experiments/minimind.zh.md) · [EN](categories/llm-training/study-and-experiments/minimind.md) |
| **nanoGPT** | 最经典的极简 GPT 训练参考——约 670 行可读代码、支持 MPS/CPU、checkpoint 与 OpenAI 的 GPT-2 互通；但它只到预训练，没有 SFT 与 RL，且 README 自己已宣布被 nanochat 取代。 | MIT | C（4/6） | [中](categories/llm-training/study-and-experiments/nanogpt.zh.md) · [EN](categories/llm-training/study-and-experiments/nanogpt.md) |
| **Train LLM From Scratch** | 在同一个英文小 GPT 上用纯 PyTorch 手写预训练、SFT、奖励模型、DPO/ORPO/KTO、PPO 和 GRPO，并用同一张 GSM8K 表对比——只能上 GPU 的教程仓库，不发布权重、没有 release，路径按作者机器写死。 | MIT | A（4/6） | [中](categories/llm-training/study-and-experiments/train-llm-from-scratch.zh.md) · [EN](categories/llm-training/study-and-experiments/train-llm-from-scratch.md) |

### agent-frameworks

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Docker Agent** | 你要的 agent 应该是一个可分享的 YAML（模型、工具、队友），由 `docker agent run` 在本地像跑镜像一样执行时选它；循环必须嵌在你代码里时不选。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/agent-runtimes/docker-agent.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/docker-agent.md) |
| **DSPy** | 你有评测数据和指标、想让优化器编译提示词而非手工调时。 | MIT | A（6/6） | [中](categories/agent-frameworks/workflow-builders/dspy.zh.md) · [EN](categories/agent-frameworks/workflow-builders/dspy.md) |
| **AgentScope** | 要把多智能体 LLM 应用作为生产服务交付，需要沙箱工具、权限闸门、tracing 和人工介入时。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/agent-runtimes/agent-sdks/agentscope.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/agentscope.md) |
| **OpenFang** | 想用单个自托管 Rust 二进制、让自治智能体按计划 7×24 无人值守干活时。 | Apache-2.0 OR MIT | C（5/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/openfang.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/openfang.md) |
| **Symphony** | 你的 Linear 待办和 Codex agent 需要一个自托管编排器、按 issue 跑隔离自治实现运行时。 | Apache-2.0 | C（5/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/symphony.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/symphony.md) |
| **Claude Octopus** | 你以 Claude Code 为主力、想让其他 AI 模型在交付前交叉评审任务、揭出盲点时。 | MIT | C（6/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/claude-octopus.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/claude-octopus.md) |
| **oh-my-claudecode** | 你常驻 Claude Code、需要多阶段 agent 团队加模型路由和 tmux 并行编排时。 | MIT | B（6/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/oh-my-claudecode.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/oh-my-claudecode.md) |
| **smolagents** | 当你想要 Hugging Face 出的极简、透明、写代码行动的 agent 循环时用它——不是重型生产 agent 操作系统。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/agent-runtimes/agent-sdks/smolagents.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/smolagents.md) |
| **Kilo Code** | 当你想要一个开源、BYOK、在 VS Code 内的编码 agent（带规划与模式）时用它——是终端用户工具，不是构建 agent 的库。 | MIT | A（6/6） | [中](categories/agent-frameworks/coding-agents/ide-agents/kilocode.zh.md) · [EN](categories/agent-frameworks/coding-agents/ide-agents/kilocode.md) |
| **Parlant** | 当你要构建一个必须靠行为准则严格守规的对客 agent 时用它——简单或自由式 agent 用它过重。 | Apache-2.0 | C（5/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/parlant.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/parlant.md) |
| **SkillOpt** | 当你要针对可打分基准、为冻结的 LLM 优化 Agent 的自然语言技能文档时用它——但没有可靠评测来把关每次编辑，方法就毫无信号，且它还是全新的 v0.1.0。 | MIT | B（6/6） | [中](categories/agent-frameworks/workflow-builders/skillopt.zh.md) · [EN](categories/agent-frameworks/workflow-builders/skillopt.md) |
| **Open Interpreter** | 当你想让 Kimi、GLM、DeepSeek、Qwen 这类便宜模型在 Codex 式终端 agent 里，套上各自家族习惯的 harness 干活时用它——但它是才几个月大的 Codex fork，过去出名的 Python REPL 已经不在这个仓库里。 | Apache-2.0 | A（6/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/open-interpreter.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/open-interpreter.md) |
| **Codex** | 当你已经在付 ChatGPT 的钱，想让这份订阅在终端里跑一个带沙箱的“改代码、跑测试、再修”循环时用它——但自定义模型提供方必须实现 Responses API，OpenAI 不收外部 PR，0.x 接口几乎天天在变。 | Apache-2.0 | A（5/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/codex.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/codex.md) |
| **OpenClaw** | 当你想在自己电脑上跑一个个人助手，在 WhatsApp、iMessage、Slack、Telegram 等 20 多个渠道里带着同一份记忆应答你时用它——但一个 Gateway 就是一个信任域，互不信任的人不能共用一套部署。 | MIT | B（5/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/openclaw.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/openclaw.md) |
| **Octop** | 家里或小团队要在飞书/企微上共用隔离 Agent、对话留在本机磁盘时用它——不是现成办公技能，LangGraph 内核仍是未公开源码的 wheel。 | MIT | B（5/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/octop.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/octop.md) |
| **OpenMuse** | 当你想要一个能派活的自托管个人助理——浏览器接管、隔离 Linux 终端、可恢复且逐项审批的任务——时用它；但它每种模式都强制要求 CopilotKit 云 key，而且是个 12 天大、零 release 的 Alpha。 | MIT | B（4/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/openmuse.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/openmuse.md) |
| **OpenWorker** | 当你想要一个用自己的模型 key、在审批闸门和逐次审计记录下把真活干完的桌面 AI 同事时用它——但命令沙箱要手动开启，一键连接器走闭源 OAuth 中转，而且它是个 71 天大的公测版。 | MIT | B（6/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/openworker.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/openworker.md) |
| **Raven** | 当你想要一个入口把一大份需求拆成任务图、分给自带的调研/编程/设计/值守 agent 或 Claude Code、Codex 时用它——但它是四个月大的 pre-alpha，沙箱默认关闭，DAG 节点还可能绕过沙箱（#796）。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/raven.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/raven.md) |
| **Rakazo** | 当你想自托管“AI 同事”——每个 bot 有自己的长期对话、定时任务和一台带浏览器、可接管的 Linux 电脑，跑在你的 Docker 主机或沙箱服务上、模型任选——时用它；但它是 7 周大的 beta，实际跟的是 `edge` 镜像，而且 bot 在电脑里执行命令和操作浏览器不经审批。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/rakazo.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/rakazo.md) |
| **OpenMinis** | 当你想让 AI agent 直接在手机上办事——iOS / Android 应用里自带 Linux shell，健康、日历、提醒事项、HomeKit 都是它的工具，模型用你自己的云端 key——时用它；但模型不在端侧跑，隐私类工具默认放行，仓库是不收 PR 的镜像、只看得到一个提交者。 | GPL-3.0 | C（6/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/openminis.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/openminis.md) |
| **OpenMausBot** | 当你已经在为 Claude Code、Codex 或 Grok CLI 付费，想把它们变成一个聊天应用里的一排 bot——各有自己的模型、电脑和连接的应用，权限请求变成“允许 / 拒绝”卡片——时用它；但审批只是各 CLI 自己的模式，统计默认开启，`enterprise/` 是源码可见许可，而且它只有 8 周大、几乎每天发版。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/openmausbot.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/openmausbot.md) |
| **OpenDots** | 当你想自己托管、自己改几个有名字的 AI 同事——每个有自己的角色、工具、文档空间和可选的容器电脑，能聊天、打电话或在 Slack 里找到，存页面和调 MCP 写操作前先问你——时用它；但每段对话都存在 CopilotKit Intelligence，模型只走兼容 OpenAI 的接口，而且是个 9 天大的 Alpha 模板。 | MIT | B（4/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/opendots.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/opendots.md) |
| **OpenHuman** | 本地优先的个人 AI 助手：每 20 分钟把邮件、日历、仓库灌成本机 Markdown 记忆，并能在 Rust 内核里强制断网——但它只有 7 个月，绝大多数提交来自一个人，许可是 GPL-3.0-only。 | GPL-3.0-only | B（6/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/openhuman.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/openhuman.md) |
| **CC Switch** | 当你在 Claude Code、Codex、Gemini CLI、OpenCode 等几个编码 CLI 之间来回换厂商，想用一个桌面应用替你改写它们的配置、MCP 服务器和技能时用它——但它是单用户图形应用，无界面服务器上用不了，也当不了团队网关。 | MIT | B（5/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/cc-switch.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/cc-switch.md) |
| **Hermes Agent** | 当你想在自己的 VPS 上养一个长期在线的助手，能跑 shell 和定时任务、记得你的环境、在 Telegram 或 Slack 上回你时用它——但技能和记忆一变它的做法就跟着变，项目也才约 15 个月大。 | MIT | A（4/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/hermes-agent.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/hermes-agent.md) |
| **AutoGPT** | 当一件每周重复的跨应用杂活（读 Gmail、查 CRM、让大模型起草、发到 Slack）要变成在画布上拖出来、或用大白话描述出来的定时 agent 时用它——但平台部分是 PolyForm Shield 许可、不是 OSI 开源，自托管还得跑一大堆服务。 | PolyForm-Shield-1.0.0 (autogpt_platform/, source-available, non-OSI) + MIT (classic/ and the rest) | B（5/6） | [中](categories/agent-frameworks/workflow-builders/autogpt.zh.md) · [EN](categories/agent-frameworks/workflow-builders/autogpt.md) |
| **Dify** | 当团队要做好几个大模型应用（文档问答机器人、工单分诊流程），想在画布上配着知识库搭出来、一发布就有网页界面和 API 时用它——但它的许可不允许未经授权做多租户服务或去掉 logo。 | NOASSERTION (Dify Open Source License — modified Apache-2.0 with multi-tenant and frontend-branding conditions) | B（5/6） | [中](categories/agent-frameworks/workflow-builders/dify.zh.md) · [EN](categories/agent-frameworks/workflow-builders/dify.md) |
| **LangChain** | 当 Python 助手要调用你的工具，又要在 OpenAI、Claude 和本地模型之间切换、不想每家都重写工具格式和调用循环时用它——但单次提示词应用别用，要自己设计控制流时直接用 LangGraph。 | MIT | A（6/6） | [中](categories/agent-frameworks/workflow-builders/langchain.zh.md) · [EN](categories/agent-frameworks/workflow-builders/langchain.md) |
| **OpenCode** | 当你想要一个 MIT 许可的终端编码 agent，工作方式不变，底下在 75+ 家 provider、本地模型或 ChatGPT / Copilot 登录之间随意换时用它——但默认权限放行改文件和 shell 命令、不先问你，也用不了 Claude Pro/Max 订阅。 | MIT | A（5/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/opencode.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/opencode.md) |
| **Prime Agent** | 当长任务把对话窗口塞烂、你要模型对着持久 Python 内核写程序、派子 agent、断开终端还能接着跑时用它——但它默认不是沙箱，仓库也才四个月。 | MIT | B（6/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/prime-agent.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/prime-agent.md) |
| **Letta Code** | 当你想要一个长期存在的终端编码 agent，把你的仓库和你的纠正跨会话记在它自己改写、用 git 记版本的记忆里时用它——但默认后端是 Letta Cloud，一天不止发一个版本，行为也会随记忆变化而漂移。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/letta-code.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/letta-code.md) |
| **Freebuff** | 想要一个不订阅、不填 API key 的终端编码 agent 时用它——但免费模型是拿文字广告、地区分档和提示词分析换来的，后端闭源，shell 命令也没有确认关卡。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/freebuff.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/freebuff.md) |
| **Langflow** | 当你想在画布上把提示词、检索器和工具连起来，在聊天面板里马上试，再把流程当 HTTP API 或 MCP 工具调用时用它——但它的安全公告里有未认证远程代码执行，做不到每周打补丁就别把它暴露出去。 | MIT | B（6/6） | [中](categories/agent-frameworks/workflow-builders/langflow.zh.md) · [EN](categories/agent-frameworks/workflow-builders/langflow.md) |
| **Gemini CLI** | 当你想要一个用普通 Google 账号登录、在每日额度内免费用、上下文窗口装得下大仓库的终端 agent 时用它——但它只连 Gemini，没有离线或本地模型这条路。 | Apache-2.0 | A（6/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/gemini-cli.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/gemini-cli.md) |
| **RTK** | 挂钩编码智能体的 shell 命令，只交回失败项和一行确认而不是整屏输出——只管 Bash（读文件会绕过），v0.x 每周发版，约 8 个月大。 | Apache-2.0 | A（5/6） | [中](categories/agent-tooling/work-state/rtk.zh.md) · [EN](categories/agent-tooling/work-state/rtk.md) |
| **CrewAI** | 当一件知识型工作天然按角色拆分（研究员、分析师、写手），而你宁愿声明智能体和任务、不想亲手连图时用它——但交接由提示词决定，核心包一装就拉进一大串依赖。 | MIT | A（6/6） | [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/crewai.md) · [中](categories/agent-frameworks/agent-runtimes/agent-sdks/crewai.zh.md) |
| **LangGraph** | 当智能体要跑几分钟甚至几天，中途得等人审批、或者要扛过重启接着跑时用它——但循环要一个节点一个节点地拼，官方自托管生产服务器还需要 LangSmith 许可证。 | MIT | A（6/6） | [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/langgraph.md) · [中](categories/agent-frameworks/agent-runtimes/agent-sdks/langgraph.zh.md) |
| **LlamaIndex** | 当 Python 应用要基于你自己的 PDF、wiki 或工单作答，想用几行代码搭好读取、切块、向量化、检索这条管线时用它——但公司重心已转向收费的 LlamaParse，开源框架成了副业。 | MIT | A（6/6） | [EN](categories/agent-frameworks/workflow-builders/llamaindex.md) · [中](categories/agent-frameworks/workflow-builders/llamaindex.zh.md) |
| **AutoGen** | 当你已有跑在 AutoGen AgentChat 或 Core 运行时上的 Python／.NET 多 agent 系统、重写的风险更大时留着用它——但它已进入维护模式，新项目请从 Microsoft Agent Framework 起步。 | MIT (code, LICENSE-CODE) + CC-BY-4.0 (docs) | B（5/6） | [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/autogen.md) · [中](categories/agent-frameworks/agent-runtimes/agent-sdks/autogen.zh.md) |
| **Microsoft Agent Framework** | 微软对 AutoGen + Semantic Kernel 的接班品——agent 优先的 Python／.NET 框架，带类型图工作流、断点续跑和 Foundry 托管。 | MIT | A（6/6） | [中](categories/agent-frameworks/agent-runtimes/agent-sdks/agent-framework.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/agent-framework.md) |
| **Pydantic AI** | 当 Python 服务里需要一步大模型调用、返回经 Pydantic 校验的类型，还想用一个字符串就换模型厂商时用它——但它只支持 Python，API 九个月里就从 V1 升到了 V2。 | MIT | A（6/6） | [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/pydantic-ai.md) · [中](categories/agent-frameworks/agent-runtimes/agent-sdks/pydantic-ai.zh.md) |
| **OpenAI Agents SDK** | 当产品已经跑在 OpenAI 模型上，想用几个原语就拿到工具循环、智能体交接和追踪时用它——但运行没有 Temporal 这类基础设施就扛不过崩溃，非 OpenAI 厂商只能走 beta 适配器。 | MIT | A（6/6） | [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/openai-agents-sdk.md) · [中](categories/agent-frameworks/agent-runtimes/agent-sdks/openai-agents-sdk.zh.md) |
| **Claude Commerce Agents** | 你要在一个卖东西的产品（零售、旅游、票务、电信）里做助手，想直接拿到购物/商家 agent 这一层（prompt、护栏、UI 回填、暂存审批）——当作一份读来 vendor 的蓝图，而不是装来用的依赖。 | Apache-2.0 | C（5/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/commerce-agents.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/commerce-agents.md) |
| **eve** | 你的 agent 要为一个人或一个 webhook 等上好几天、要扛住重新部署，还要能在 Slack／Discord／Teams 上应答——并且是一个可部署的 TypeScript 服务。 | Apache-2.0 | A（6/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/eve.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/eve.md) |
| **Open Executive** | 小公司要把领导问题收成一个自托管高管声音——背后是专家 agent、公司文档和 Slack——而不是自己组装框架，也不是个人传呼机。 | Apache-2.0 | B（4/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/open-executive.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/open-executive.md) |
| **OpenAgentCore** | 你的应用要通过 OpenAI Agents API，在自己的基础设施上按会话开沙箱驱动 Codex、Claude Code 或 MiniMax Code——但它只有十天大、还是不做兼容承诺的 v0.0.x，各 harness 功能不对齐，也没有按会话的网络隔离。 | MIT | C（5/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/openagentcore.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/openagentcore.md) |
| **OpenBot** | 公司要受治理的 AI 同事——每个有自己的浏览器加 shell 容器、每个动作先过策略再留审计、任意 AG-UI agent 可接入——但它是 6 周大的 alpha 模板，缺了 CopilotKit 的 Intelligence 服务就起不来。 | MIT | B（6/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/openbot.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/openbot.md) |
| **Open Dots (Anil-matcha)** | 想从 Telegram 或网页把 Claude Code 任务派进一次性云虚拟机、每个风险动作点按钮审批——但它是挂在一个换过用途的 5.5k 星仓库里、只有十来天的原型，API 无鉴权，只能跑在付费的 Boat 虚拟机上，也没有 LICENSE 文件。 | NONE (no LICENSE file — all rights reserved) | D（4/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/open-dots.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/open-dots.md) |
| **aider** | 当你想在终端里让 AI 改你点名的文件、模型随你选、每次改动都自动成为可 `/undo` 的 git 提交时用它——但它实质上是一人维护，2025-08 之后没有再发版。 | Apache-2.0 | B（6/6） | [EN](categories/agent-frameworks/coding-agents/terminal-agents/aider.md) · [中](categories/agent-frameworks/coding-agents/terminal-agents/aider.zh.md) |
| **Cline** | 装机量最大的开源编辑器／终端／桌面 coding agent——每一次改动和命令都等你批准并留下 checkpoint，模型自带，一天多发。 | Apache-2.0 | B（5/6） | [中](categories/agent-frameworks/coding-agents/ide-agents/cline.zh.md) · [EN](categories/agent-frameworks/coding-agents/ide-agents/cline.md) |
| **Roo Code** | 「按角色分模式」VS Code agent（Code/Architect/Ask/Debug 加自定义 `.roomodes`）的归档起点——当设计参考读，迁移时选 Cline 或 Kilo Code；它的 sunset 公告就推荐 Cline。 | Apache-2.0 | C（6/6） | [中](categories/agent-frameworks/coding-agents/ide-agents/roo-code.zh.md) · [EN](categories/agent-frameworks/coding-agents/ide-agents/roo-code.md) |
| **Continue** | 在最终 2.0.0（2026-06-19）之后转为只读的配置驱动 coding agent——可以研究它「编辑器与 CLI 共用一份 `config.yaml`」的设计，但别采用这个冻结的运行时。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/coding-agents/ide-agents/continue.zh.md) · [EN](categories/agent-frameworks/coding-agents/ide-agents/continue.md) |
| **SWE-agent** | 当你必须复现已发表的 SWE-agent 结果、用一份 YAML 配置在 Docker 沙箱里批量让模型修仓库 issue 时用它——但维护者已声明它被 mini-swe-agent 取代，新工作别再从它起步。 | MIT | B（5/6） | [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/swe-agent.md) · [中](categories/agent-frameworks/coding-agents/orchestration-and-review/swe-agent.zh.md) |
| **Flowise** | 只在你已经跑着 Flowise 聊天流、要决定自己 fork 还是迁走时看它——但仓库已于 2026-08-13 归档、2026-08-31 停止支持，新项目请改用 Langflow 或 Dify。 | NOASSERTION (Apache-2.0 core + commercial license on packages/server/src/enterprise) | D（5/6） | [EN](categories/agent-frameworks/workflow-builders/flowise.md) · [中](categories/agent-frameworks/workflow-builders/flowise.zh.md) |
| **OpenHands** | 当你想用一个自托管的浏览器控制台，在指定机器上跑 OpenHands、Claude Code、Codex 或 Gemini CLI 会话，再加上定时或 webhook 触发的 agent 任务时用它——但这个仓库 2026 年 7 月才改成 beta 版 Agent Canvas，经典的 `openhands-ai` agent 已不在这里。 | MIT | B（6/6） | [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/openhands.md) · [中](categories/agent-frameworks/coding-agents/orchestration-and-review/openhands.zh.md) |
| **T3 Code** | 当一个本地 GUI 要驱动已经认证的 Codex、Claude、Cursor、OpenCode CLI 时用它。 | MIT | A（6/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/t3code.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/t3code.md) |
| **Background Agents（Open-Inspect）** | 当一个可信组织需要自托管的后台 coding-agent 沙箱、集成和自动化时用它。 | MIT | B（5/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/background-agents.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/background-agents.md) |
| **SwarmForge** | 当你想要一个自托管的角色流水线（spec→code→clean→architect→harden→QA）跑在自己的仓库上、每个角色一个 git worktree、以 commit 交接时用它——但它没有许可证，也没有 tagged release。 | NONE（无 LICENSE 文件——保留所有权利） | D（5/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/swarm-forge.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/swarm-forge.md) |
| **OpenChamber** | 当你用 OpenCode，想要一个跨设备的运行工作台——按目标审计的会话、一条提示词最多五个模型（可各带 worktree）、变更讲解，以及紧挨对话的 git/PR 面板——但要接受一个 12 个月大、单人主控、只绑一个 agent runtime 的应用时用它。 | MIT | B（5/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/openchamber.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/openchamber.md) |
| **OpenResearch** | 当 coding agent 和 GPU 都已经到位、缺的只是实验记账——每个实验一条分支的实验树、不可变的提交快照、以及把 run 派到九个算力后端——时用它，代价是接受一个 3.5 个月大、发布极快的应用，且它的托管算力那一半是闭源服务。 | MIT | B（6/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/openresearch.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/openresearch.md) |
| **herdr** | 当你同时监管多个编程 agent、要终端复用器自己打上 blocked/working/done 标记、脱离后 agent 继续跑、并且让 agent 之间用 `herdr agent wait/prompt` 互相驱动时用它——但它只有 6 个月大、pre-1.0、实质单人维护。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/coding-agents/agent-multiplexers/herdr.zh.md) · [EN](categories/agent-frameworks/coding-agents/agent-multiplexers/herdr.md) |
| **TUIOS** | 当你在一个终端里同时盯多个编程 agent，想要一个平铺窗口管理器、由守护进程跟踪每个 agent 的状态并把所有待审批和提问收进一个 Inbox 时用它——但它只有 13 个月大、pre-1.0 且有协议破坏、单人维护，pane 默认拥有全部控制权。 | MIT | B（6/6） | [中](categories/agent-frameworks/coding-agents/agent-multiplexers/tuios.zh.md) · [EN](categories/agent-frameworks/coding-agents/agent-multiplexers/tuios.md) |
| **cmux** | 当你在 Mac 上并排跑好几个命令行编码 agent，想让终端应用本身给正在等你的那个窗格套上光圈、在竖排侧边栏显示分支/PR/最新消息、旁边再开一个 agent 能操作的浏览器窗格时用它——但它只支持 macOS、才 8 个月大、遥测默认开启，服务端是 BUSL-1.1。 | GPL-3.0-or-later (macOS app, CLI, cmux-tui) + BUSL-1.1 (web/, workers and relay services; production use needs a commercial license) | D（5/6） | [中](categories/agent-frameworks/coding-agents/agent-multiplexers/cmux.zh.md) · [EN](categories/agent-frameworks/coding-agents/agent-multiplexers/cmux.md) |
| **GitHub Agentic Workflows (gh-aw)** | 当你想让 coding agent 在 GitHub 仓库上无人值守地干杂活（issue 分诊、查 CI 失败、写报告、提文档 PR），用 Markdown 写、编译成 Actions 工作流，agent 只读并在防火墙后运行、只有声明过的写操作才会执行时用它——但它只限 GitHub、处于 Public Preview、每周发版，7 周内出了 11 个安全公告。 | MIT | B（4/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/gh-aw.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/gh-aw.md) |
| **Codex plugin for Claude Code** | 当你以 Claude Code 为主、手上已有 Codex 登录，想让 OpenAI 的 Codex 不离开会话就审你的改动、或接手卡住的任务时用它——但它只接一家厂商，rescue 默认可写，会泄漏中转进程，而且 2026-07 之后没有合并过任何东西。 | Apache-2.0 | B（5/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/codex-plugin-cc.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/codex-plugin-cc.md) |
| **Harness SDK** | 想要一次调用就有能用的 agent——调好的 prompt、shell／文件／web 工具、代码沙箱、子代理、记忆与会话——而且 Python 与 TypeScript 同接口、每个默认值都可覆盖时用它；要托管运行时或可审查的图就不是它。 | Apache-2.0 | A（6/6） | [中](categories/agent-frameworks/agent-runtimes/agent-sdks/harness-sdk.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/harness-sdk.md) |
| **Pi** | 想要一个极简终端 agent、行为由你仓库里的文件决定——技能、prompt 模板、它自己也能写的 TypeScript 扩展——并且愿意自己承担沙箱时用它。 | MIT | B（5/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/pi.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/pi.md) |
| **OmO** | 想把整件任务交给终端 agent 时用它——`ulw`、`mass ulw` 关键词把工作摊成一张按类别路由、跨订阅模型的依赖图，验证通过才算完成，记忆沉淀进 git——但 SUL-1.0 限制商业再分发，token 是按机队花的，十个月的热度 star 是风险信号而不是 Lindy 记录。 | SUL-1.0 | B（5/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/oh-my-openagent.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/oh-my-openagent.md) |
| **Agent-Native** | 你想让产品里的 agent 真的把活干完，并愿意让一个 TypeScript 应用接管界面、服务端与 Postgres，好让按钮和工具共用同一份实现——但它是半年大的 v0.x，且许可证存疑。 | MIT（声明为 MIT，但无 LICENSE 文件） | C（4/6） | [中](categories/agent-frameworks/workflow-builders/agent-native.zh.md) · [EN](categories/agent-frameworks/workflow-builders/agent-native.md) |
| **TanStack AI** | 当 TypeScript 应用的 AI 界面——流式聊天、带类型的工具、媒体与 agent，横跨七个前端框架——必须站在一套 provider 无关的类型契约上、且不绑任何平台层时用它；agent 活在 Python 里、或你要的是打包好的 `Agent` 类，就不是它。 | MIT | B（6/6） | [中](categories/agent-frameworks/agent-runtimes/agent-sdks/tanstack-ai.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/tanstack-ai.md) |
| **AX** | 当一大批空闲、有状态的 agent *任务*必须在 Kubernetes 上用 YAML 声明（工作区、出站、模型）、底下还能挂起／恢复时用它——不是把 agent 本身做成 CRD 的那条路。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/kubernetes-agents/ax.zh.md) · [EN](categories/agent-frameworks/kubernetes-agents/ax.md) |
| **kagent** | 当 agent 应该是 Kubernetes 对象时用它——用 YAML 声明、由控制器与引擎运行，带模型配置、MCP 工具服务器与 OpenTelemetry 追踪。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/kubernetes-agents/kagent.zh.md) · [EN](categories/agent-frameworks/kubernetes-agents/kagent.md) |
| **OpenClaw Enterprise** | 当多个团队的原版 OpenClaw 或 Codex agent 要在共享 Kubernetes 集群上按租户分命名空间、走 IAM、投递密钥、留不可变版本和审计时用它——不适合个人助手，也还不是正式发布的产品。 | MIT | B（5/6） | [中](categories/agent-frameworks/kubernetes-agents/openclaw-enterprise.zh.md) · [EN](categories/agent-frameworks/kubernetes-agents/openclaw-enterprise.md) |

### agent-memory

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Mem0** | 当你的 LLM agent 需要跨会话记住用户、又不想撑爆 prompt 上下文时用它。 | Apache-2.0 | A（6/6） | [中](categories/agent-memory/app-memory/mem0.zh.md) · [EN](categories/agent-memory/app-memory/mem0.md) |
| **Memori** | 当你想要 LLM 无关、通过包裹现有客户端自动捕获并召回的持久化 agent 记忆时使用。 | Apache-2.0 | B（5/6） | [中](categories/agent-memory/app-memory/memori.zh.md) · [EN](categories/agent-memory/app-memory/memori.md) |
| **Claude Subconscious** | 当你想让一个后台 Letta agent 通过 hook 给 Claude Code 加上跨会话记忆时使用（仅 demo，非生产）。 | MIT | C（5/6） | [中](categories/agent-memory/coding-agent-memory/claude-subconscious.zh.md) · [EN](categories/agent-memory/coding-agent-memory/claude-subconscious.md) |
| **claude-mem** | 当你的编码 agent 跨会话丢失上下文、你想要本地 hook/MCP 捕获并压缩后再注入的记忆时用它（star 数存疑）。 | Apache-2.0 | B（6/6） | [中](categories/agent-memory/coding-agent-memory/claude-mem.zh.md) · [EN](categories/agent-memory/coding-agent-memory/claude-mem.md) |
| **ByteRover CLI** | 只把它当设计参考，或在迁出 `brv` 时看它——但仓库已于 2026 年归档，已知的卡死缺陷不会再修，许可是 Elastic 2.0 而非 OSI；要仍在维护的编码 agent 记忆，改用 Engram 或 claude-mem。 | Elastic-2.0 | D（6/6） | [中](categories/agent-memory/coding-agent-memory/byterover.zh.md) · [EN](categories/agent-memory/coding-agent-memory/byterover.md) |
| **Letta (MemGPT)** | 只在你跑着自托管的 Letta V1 服务器、或被教程带到这个仓库、需要规划迁移时看它——但该服务器已于 2026 年 8 月退役、挪到 `archive` 分支，不再有安全修复；还在维护的 Letta 现在是 Letta Code。 | Apache-2.0 | B（6/6） | [EN](categories/agent-memory/app-memory/letta.md) · [中](categories/agent-memory/app-memory/letta.zh.md) |
| **Zep** | 当你想把带时间维度的用户记忆交给托管服务，并直接用 LangGraph、CrewAI、ADK 或 Pydantic AI 的现成适配包时用它——但这个仓库只是示例和客户端，引擎是闭源付费的 Zep Cloud，自托管的社区版已弃用。 | Apache-2.0 | A（4/6） | [EN](categories/agent-memory/graph-memory/zep.md) · [中](categories/agent-memory/graph-memory/zep.zh.md) |
| **Graphiti** | 当用户的偏好、工作、住址会随时间变化，智能体必须分清哪条事实仍然成立、何时成立时用它——但它从第一天就要 Neo4j、FalkorDB 或 Neptune，每条消息写入都要走几次 LLM 调用。 | Apache-2.0 | B（6/6） | [EN](categories/agent-memory/graph-memory/graphiti.md) · [中](categories/agent-memory/graph-memory/graphiti.zh.md) |
| **LangMem** | 当你的 agent 本来就跑在 LangGraph 上，想要直接用同一个 `BaseStore` 存取记忆的现成工具时用它——但它会拉进整套 LangChain，发版也停在 2025-10 的 0.0.30。 | MIT | B（5/6） | [EN](categories/agent-memory/app-memory/langmem.md) · [中](categories/agent-memory/app-memory/langmem.zh.md) |
| **Cognee** | 当 agent 记忆覆盖的是彼此关联的材料（文档、工单、会议纪要、代码），普通 RAG 一遇到多跳问题就答不上时用它——但每次写入都要花 LLM 调用做图谱抽取，用 Postgres 当图存储只是演示，不能上生产。 | Apache-2.0 | A（5/6） | [EN](categories/agent-memory/graph-memory/cognee.md) · [中](categories/agent-memory/graph-memory/cognee.zh.md) |
| **OpenViking** | 当多个编码 agent 或一个团队需要共用同一份既装文档又装长期记忆的存储、且你能跑一个服务端时用它——但主仓是 AGPL-3.0，仓库自标 alpha。 | AGPL-3.0 | B（6/6） | [EN](categories/agent-memory/coding-agent-memory/openviking.md) · [中](categories/agent-memory/coding-agent-memory/openviking.zh.md) |
| **SimpleMem** | 当你的 LLM 智能体要回答关于长期对话的问题、又不想把原始历史重放进上下文时用它——写入时压缩、有 LoCoMo 公开数字，但仓库年轻学术、PyPI 停在 0.1.0、音视频支持没有基准验证。 | MIT | B（5/6） | [EN](categories/agent-memory/app-memory/simplemem.md) · [中](categories/agent-memory/app-memory/simplemem.zh.md) |
| **Supermemory** | 当你想把整叠上下文管线——事实抽取、矛盾取代、自动到期、按用户画像、RAG 加记忆混合检索——收到一个 API 或一个自托管二进制后面，并接受引擎只发二进制、许可证翻转过一次时用它。 | MIT | A（6/6） | [中](categories/agent-memory/app-memory/supermemory.zh.md) · [EN](categories/agent-memory/app-memory/supermemory.md) |
| **Hindsight** | 当你的 agent 要跨几周记住用户或项目、答得出“谁”“什么时候”这类问题时用它——MIT 许可、自托管的记忆服务（Postgres 加 pgvector），带实体和时间维度召回与 MCP，但每次写入都要花 LLM 调用、认证默认关闭、还没到 1.0。 | MIT | B（4/6） | [EN](categories/agent-memory/app-memory/hindsight.md) · [中](categories/agent-memory/app-memory/hindsight.zh.md) |
| **Beacon** | 当你各家的 agent 经验互相隔绝、想要一份覆盖所有编码会话的本地轨迹加人工把关的经验沉淀时用它。 | MIT | B（6/6） | [EN](categories/agent-memory/coding-agent-memory/agent-beacon.md) · [中](categories/agent-memory/coding-agent-memory/agent-beacon.zh.md) |
| **Engram** | 当你同时用好几个编码 agent、想让它们共用一份由 agent 自己通过 MCP 写入和检索的本地记忆时用它——一个 Go 程序加一个 SQLite 文件，关键词搜索，不做后台采集。 | MIT | B（5/6） | [中](categories/agent-memory/coding-agent-memory/engram.zh.md) · [EN](categories/agent-memory/coding-agent-memory/engram.md) |
| **backpass** | 当你的 `AGENTS.md`／`CLAUDE.md` 跟编码 agent 实际犯的错对不上了，想从磁盘上已有的会话记录里挖出改动——每条有两个会话的原话作证、在 token 预算内逐条由你接受——时用它。 | MIT | B（6/6） | [中](categories/agent-memory/coding-agent-memory/backpass.zh.md) · [EN](categories/agent-memory/coding-agent-memory/backpass.md) |
| **OptMem** | 当你想要零活动部件的编码 agent 记忆——一段贴进去的提示块、一个零依赖的 Python 脚本、一份由 agent 自己经营的只追加日志——且能接受自愿捕获、仅正则的检索和没有许可证时用它。 | NONE (no LICENSE file — all rights reserved) | D（5/6） | [中](categories/agent-memory/coding-agent-memory/optmem.zh.md) · [EN](categories/agent-memory/coding-agent-memory/optmem.md) |
| **deja-vu** | 当你的各家 agent 反复重排你在另一家 agent 里早已修好的问题，而你想直接用 35 家 harness 已经写进磁盘的会话记录建记忆、不要“保存”环节也不要模型账单时用它。 | MIT | B（6/6） | [中](categories/agent-memory/coding-agent-memory/deja-vu.zh.md) · [EN](categories/agent-memory/coding-agent-memory/deja-vu.md) |
| **autoharness** | 当你整天用 Claude Code、想让自己会话里的经验自动变成技能——按使用情况修补、合并、淘汰，没有审阅环节——并且能接受后台跳过权限确认的子会话和一个不到四个月的项目时用它。 | MIT | C（6/6） | [中](categories/agent-memory/coding-agent-memory/autoharness.zh.md) · [EN](categories/agent-memory/coding-agent-memory/autoharness.md) |

### deep-research

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **deep-research** | 当你想读懂并 fork 一个约 500 行的 TypeScript 深度研究循环（Firecrawl 搜索加广度／深度递归，产出带引用的报告）时用它——但它是单作者的 0.0.1 演示，错误处理极简，也没有成本上限。 | MIT | B（4/6） | [中](categories/deep-research/deep-research.zh.md) · [EN](categories/deep-research/deep-research.md) |
| **Vane** | 想要一个自托管、注重隐私的「Perplexity 式」带引用应答引擎，接你自己的 SearxNG 和自选 LLM 时用它。 | MIT | B（5/6） | [中](categories/deep-research/vane.zh.md) · [EN](categories/deep-research/vane.md) |
| **Local Deep Research** | 当你需要一个自托管、可纯本地运行的深度研究 agent、把敏感查询留在自己机器上时用它。 | MIT | B（5/6） | [中](categories/deep-research/local-deep-research.zh.md) · [EN](categories/deep-research/local-deep-research.md) |
| **Agent-Reach** | 当你的 agent 需要免付费 API 地读取和搜索网页与社交平台内容时用它。 | MIT | B（5/6） | [中](categories/deep-research/agent-reach.zh.md) · [EN](categories/deep-research/agent-reach.md) |
| **MiroThinker** | 当你想要一个可在自有 GPU 上研究改造的自托管开源深研 Agent 时用它——但它要 GPU 集群加付费外部 API，且不到一岁、毫无 Lindy 沉淀。 | Apache-2.0 | B（4/6） | [中](categories/deep-research/mirothinker.zh.md) · [EN](categories/deep-research/mirothinker.md) |
| **GPT Researcher** | 当你要一个开箱即用的应用，把一个问题变成一份基于网页或你自己文件、处处带出处的多页报告时用它——但默认配置会把数据发给 OpenAI 和 Tavily，纯本地运行要自己改配置。 | Apache-2.0 | A（6/6） | [EN](categories/deep-research/gpt-researcher.md) · [中](categories/deep-research/gpt-researcher.zh.md) |
| **Open Deep Research** | 当你在 LangGraph 上自建调研智能体、想要一份“主管加并行研究员”的可读蓝图和现成基准脚手架时用它——但仓库已于 2026 年归档，只适合学习或 fork，不适合当依赖运行。 | MIT | D（5/6） | [EN](categories/deep-research/open-deep-research.md) · [中](categories/deep-research/open-deep-research.zh.md) |
| **STORM** | 当你要为一个陌生话题写一篇带编号引用、由多视角调研和大纲搭起来的维基风长文初稿时用它——但它自 2025-09 起没再合入任何改动，当作方法的参考实现看待。 | MIT | C（5/6） | [EN](categories/deep-research/storm.md) · [中](categories/deep-research/storm.zh.md) |
| **node-DeepResearch** | 当用户问需要跳好几步的事实题、你想要一个自部署、兼容 OpenAI 接口、一直搜到能给出带出处短答案的服务时用它——但读网页离不开 Jina 的托管 API，它的代码执行工具也没有沙箱。 | Apache-2.0 | B（4/6） | [EN](categories/deep-research/node-deepresearch.md) · [中](categories/deep-research/node-deepresearch.zh.md) |
| **Hyperresearch** | 当你在 Claude Code 里、需要一份引用逐条核验的高风险研究报告时用它——16 步对抗式流水线加持久来源 vault；时间与 token 开销都重，且只支持 Claude Code。 | MIT | B（5/6） | [中](categories/deep-research/hyperresearch.zh.md) · [EN](categories/deep-research/hyperresearch.md) |
| **last30days** | 当你想让 agent 汇总最近 30 天 Reddit、X、YouTube、HN、Polymarket 上关于某个主题的讨论、并按互动量排好序时用它——但每次调用要加载约 258 KB 的 skill 提示词，且部分来源依赖抓取和浏览器登录 cookie。 | MIT | B（6/6） | [中](categories/deep-research/last30days.zh.md) · [EN](categories/deep-research/last30days.md) |
| **OpenScience** | 当研究任务必须真的在自己的文件上跑代码时用它——文献与数据库检索、Python/R 内核、集群作业、每一步都留在可审计的轮次轨迹里。 | Apache-2.0 | B（6/6） | [中](categories/deep-research/openscience.zh.md) · [EN](categories/deep-research/openscience.md) |

### ai-code-review

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Open Code Review** | 想在 CI 里对 Git diff 拿到精确行级 LLM review 评论、又不被噪声淹没时用它。 | Apache-2.0 | B（5/6） | [中](categories/ai-code-review/open-code-review.zh.md) · [EN](categories/ai-code-review/open-code-review.md) |
| **Claude Code Security Review** | 当你想让 Claude 在每个可信 PR 上读 diff、找逻辑层面的漏洞并在具体行上评论、且不分语言时用它——但它没做 prompt injection 加固，绝不能用在不可信的 fork PR 上。 | MIT | B（4/6） | [中](categories/ai-code-review/claude-code-security-review.zh.md) · [EN](categories/ai-code-review/claude-code-security-review.md) |
| **React Doctor** | 当 coding agent 在写 React、你想要对 React 特有反模式做确定性、可重复的检查时用它。 | LicenseRef-Modified-MIT | B（5/6） | [中](categories/ai-code-review/react-doctor.zh.md) · [EN](categories/ai-code-review/react-doctor.md) |
| **PR-Agent** | 当团队在 GitHub、GitLab、Bitbucket、Azure DevOps 或 Gitea 上，想让每个 PR 一打开就自动写好说明并预审一遍、模型费用直接付给厂商时用它——但它只看压缩后的改动，许可证 14 个月里还换了三次。 | MIT | A（5/6） | [EN](categories/ai-code-review/pr-agent.md) · [中](categories/ai-code-review/pr-agent.zh.md) |
| **Metis** | 当安全团队想让大模型对一个大型 C/C++ 代码库做一遍深入初筛，或者给其他扫描器的 SARIF 降误报，并且只用安全策略允许的模型时用它——但它只是 CLI、没有 PR 机器人，每次运行的结果都会有出入。 | Apache-2.0 | B（5/6） | [EN](categories/ai-code-review/metis.md) · [中](categories/ai-code-review/metis.zh.md) |
| **OpenReview** | 当你的代码在 GitHub、本来就用 Vercel，想要一个 @ 一下就在沙箱里跑 lint 和测试、还能推回修复的 Claude 审查者时用它——但它是一个停更的 Vercel 演示，仓库里没有 LICENSE 文件。 | NOASSERTION | D（5/6） | [EN](categories/ai-code-review/openreview.md) · [中](categories/ai-code-review/openreview.zh.md) |

### rag-retrieval

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **FalkorDB** | 当 GraphRAG 需要在一个低延迟、嵌入 Redis 的引擎里把向量相似与多跳图遍历结合时使用。 | SSPL-1.0 | D（5/6） | [中](categories/rag-retrieval/structured-retrieval/falkordb.zh.md) · [EN](categories/rag-retrieval/structured-retrieval/falkordb.md) |
| **graphify** | 当 agent 需要把整个仓库的代码、schema 和文档当成知识图谱来查询、而非反复 grep 时用它。 | MIT | C（5/6） | [中](categories/rag-retrieval/code-intelligence/graphify.zh.md) · [EN](categories/rag-retrieval/code-intelligence/graphify.md) |
| **code-review-graph** | 当 AI 评审在大仓库里反复烧上下文、你只想喂给它一次改动真正触及（blast-radius）的文件时用它。 | MIT | B（6/6） | [中](categories/rag-retrieval/code-intelligence/code-review-graph.zh.md) · [EN](categories/rag-retrieval/code-intelligence/code-review-graph.md) |
| **PageIndex** | 当向量 RAG 在少量长而有结构的文档上召回相似但不相关的块、且你需要可溯源引用时使用。 | MIT | B（6/6） | [中](categories/rag-retrieval/structured-retrieval/pageindex.zh.md) · [EN](categories/rag-retrieval/structured-retrieval/pageindex.md) |
| **Understand-Anything** | 当你想把任意代码库变成可探索、可提问的知识图谱给 agent 用时用它——比 graphify 更年轻、未经检验。 | MIT | B（6/6） | [中](categories/rag-retrieval/code-intelligence/understand-anything.zh.md) · [EN](categories/rag-retrieval/code-intelligence/understand-anything.md) |
| **FAISS** | 当你需要一个快速的进程内 ANN 向量索引来检索 embedding 时用它——是库，不是托管向量数据库。 | MIT | A（6/6） | [中](categories/rag-retrieval/vector-search/faiss.zh.md) · [EN](categories/rag-retrieval/vector-search/faiss.md) |
| **text2vec** | 当你要一行 pip 拿到偏中文的句向量、或用 CoSENT/SBERT 在自己的样本对上微调，做 FAQ 匹配或语义检索时用它——但它只是编码器（索引要配 FAISS 或 Milvus），单一维护者最后一次发版在 2023-09。 | Apache-2.0 | C（5/6） | [中](categories/rag-retrieval/vector-search/text2vec.zh.md) · [EN](categories/rag-retrieval/vector-search/text2vec.md) |
| **SCIP** | 当你做代码搜索、评审机器人或 agent 检索层，需要跨多语言代码库拿到编译器级精确的定义和引用、并在 CI 里每个提交索引一次时用它——但它只是格式，不是查询服务，而且代码要能构建才能被索引。 | Apache-2.0 | A（6/6） | [EN](categories/rag-retrieval/code-intelligence/scip.md) · [中](categories/rag-retrieval/code-intelligence/scip.zh.md) |
| **Milvus** | 当向量塞不进一台机器的内存，又要元数据过滤、实时增删、副本和横向扩容的检索服务时用它——但你得运维一个带 etcd 和对象存储的分布式集群；几百万条以内用 FAISS，已有 Postgres 就用 pgvector。 | Apache-2.0 | A（6/6） | [EN](categories/rag-retrieval/vector-search/milvus.md) · [中](categories/rag-retrieval/vector-search/milvus.zh.md) |
| **Sourcegraph** | 当你要为几百个仓库设计代码搜索、想读一个真实产品如何处理克隆同步、建索引和代码导航时用它——但这是已归档的快照，2023-06 之后的代码适用企业许可，要部署请改用 Zoekt。 | NOASSERTION (Sourcegraph Enterprise License, source-available; Apache-2.0 up to commit 1cd36d2, 2023-06-13) | D（4/6） | [EN](categories/rag-retrieval/code-intelligence/sourcegraph.md) · [中](categories/rag-retrieval/code-intelligence/sourcegraph.zh.md) |
| **HelixDB** | 当你的 RAG 语料本身就是一张图，你想把向量检索、BM25 和图遍历放进同一个采用 Apache-2.0、由对象存储托底的引擎时用它——但 v3 引擎 2026-07 才开源，且没有可自建的 HA。 | Apache-2.0 | B（6/6） | [中](categories/rag-retrieval/structured-retrieval/helix-db.zh.md) · [EN](categories/rag-retrieval/structured-retrieval/helix-db.md) |
| **Ix** | 当你的编码 agent 总在多语言仓库里 grep 找调用方和影响面、而你能跑 Docker 时用它——代价是后端镜像闭源、项目才七个月大还在 v0.x。 | Apache-2.0 | B（6/6） | [中](categories/rag-retrieval/code-intelligence/ix.zh.md) · [EN](categories/rag-retrieval/code-intelligence/ix.md) |
| **Repowise** | 当你的 agent 每个任务都在大仓库里重新烧上下文找结构、而你想要一个不用 key 的本机索引，通过 MCP 回答图、git、健康度、死代码与决策问题时用它——代价是六个月大、v0.x、AGPL 的厂商项目。 | AGPL-3.0 | C（6/6） | [中](categories/rag-retrieval/code-intelligence/repowise.zh.md) · [EN](categories/rag-retrieval/code-intelligence/repowise.md) |
| **Jevgrep** | 当你的 agent 要在没建过索引的陌生仓库里靠“这段代码在干什么”来定位、并接受按次付费把源码发给托管评测模型时用它——代价是出生两天、单人维护、只有 macOS/Linux。 | MIT | C（4/6） | [中](categories/rag-retrieval/code-intelligence/jevgrep.zh.md) · [EN](categories/rag-retrieval/code-intelligence/jevgrep.md) |

### llm-eval

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **promptfoo** | 当你要用声明式 YAML 给自己的 LLM 应用做评测+红队并接进 CI 时用它。 | MIT | A（6/6） | [中](categories/llm-eval/promptfoo.zh.md) · [EN](categories/llm-eval/promptfoo.md) |
| **Pezzo** | 当小团队想要一个自托管的统一控制台来做 prompt 版本管理加成本／延迟可观测时用它——但它自 2025 年中起疑似停更，请做好自己维护的准备。 | Apache-2.0 | C（5/6） | [中](categories/llm-eval/pezzo.zh.md) · [EN](categories/llm-eval/pezzo.md) |
| **DeepEval** | 当 Python 团队想给 RAG 应用或智能体写 pytest 式回归测试，在 CI 里用忠实度、幻觉等大模型评审指标打分时用它——但每次运行都花评审 token，分数会浮动，配套看板是厂商的商业托管平台。 | Apache-2.0 | A（6/6） | [EN](categories/llm-eval/deepeval.md) · [中](categories/llm-eval/deepeval.zh.md) |
| **Ragas** | 当你改了 RAG 链路的分块、向量模型或生成模型，需要评审大模型为每次改动打出忠实度和上下文召回／精确率时用它——但它只给分数，不提供 CI 通过／失败闸门，且自 2026-02 起再无 PR 合并。 | Apache-2.0 | B（6/6） | [EN](categories/llm-eval/ragas.md) · [中](categories/llm-eval/ragas.zh.md) |
| **garak** | 当模型上线前要由你签字放行，需要一套可重复的扫描，按探针给出越狱、注入、数据泄露、恶意代码生成等已知攻击的失败率时用它——但它只测模型本身，不测应用的回答质量或整套部署。 | Apache-2.0 | A（6/6） | [EN](categories/llm-eval/garak.md) · [中](categories/llm-eval/garak.zh.md) |
| **Giskard OSS** | 当用 Python 3.12+ 的团队想把 RAG 或 agent 的故障钉成带大模型裁判检查的场景测试、上线前还要自动生成攻击提示词时用它——但表格模型扫描只在已不再积极维护的 v2 里，v3 正式版才发布几周。 | Apache-2.0 | B（6/6） | [EN](categories/llm-eval/giskard.md) · [中](categories/llm-eval/giskard.zh.md) |
| **Langfuse** | 当生产中的大模型功能需要给每个请求记嵌套调用轨迹，再加打分、提示词版本和数据集，并且要能自托管时用它——但自托管要运维 Postgres、ClickHouse、Redis 和 S3 存储，部分管理功能还走企业许可。 | NOASSERTION (MIT core; ee/ directories under the commercial Langfuse Enterprise License) | A（5/6） | [EN](categories/llm-eval/langfuse.md) · [中](categories/llm-eval/langfuse.zh.md) |
| **SWE-bench** | 当你要用真实 GitHub issue 及其测试给 coding agent 的补丁打分时用它——每次评测都要 Docker 和大量磁盘。 | MIT | B（6/6） | [中](categories/llm-eval/swe-bench.zh.md) · [EN](categories/llm-eval/swe-bench.md) |
| **Harvey LAB** | 当你要让 agent 做完整套法律任务来做基准——虚构案卷进、备忘录或修订稿出，由两个大模型评委按律师清单判分——时用它；需要 Podman，以及 Anthropic 和 OpenAI 两把密钥。 | MIT | B（6/6） | [中](categories/llm-eval/harvey-labs.zh.md) · [EN](categories/llm-eval/harvey-labs.md) |
| **AI-Infra-Guard** | 当审计面是整套自托管 AI 栈时用它——在线服务 CVE、MCP server、Agent Skill、越狱评测，一个腾讯出品的平台搞定，而不是只盯单个模型端点。 | Apache-2.0 | B（6/6） | [中](categories/llm-eval/ai-infra-guard.zh.md) · [EN](categories/llm-eval/ai-infra-guard.md) |
| **iFixAi** | 当你想快速、开箱即用地审一审 agent 守没守住声明的角色、工具权限和诚实规则时用它——60 项固定检查、另一家厂商的评委、一个 A–F 等级；项目很年轻、靠大模型判分，1.8 万星和它的实际使用量对不上。 | Apache-2.0 | B（4/6） | [中](categories/llm-eval/ifixai.zh.md) · [EN](categories/llm-eval/ifixai.md) |

### agent-dev-methodology

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **12-Factor Agents** | 当一个用大框架搭的 agent 一上生产就抖、你想要一套有名有姓的原则（掌控 prompt、context window、控制流）来评审或重新设计它时用它——但它只是一套文集，没有可安装的代码，2025-09 之后再没更新。 | CC-BY-SA-4.0 (content) / Apache-2.0 (code examples) | "?"（2/5） | [中](categories/agent-dev-methodology/spec-driven-development/12-factor-agents.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/12-factor-agents.md) |
| **Claude Code Templates** | 当你想在一个大目录里逛逛、单点自选地安装现成的 Claude Code agent、命令、hook、MCP 和 skill，而不是自己从头写时，用它。 | MIT | B（6/6） | [中](categories/agent-dev-methodology/coding-agent-harnesses/claude-code-templates.zh.md) · [EN](categories/agent-dev-methodology/coding-agent-harnesses/claude-code-templates.md) |
| **Superpowers** | 当你想给编程 agent 装一套即插即用的「头脑风暴→计划→TDD→验证」SDLC 方法论时用它。 | MIT | B（4/5） | [中](categories/agent-dev-methodology/coding-agent-harnesses/superpowers.zh.md) · [EN](categories/agent-dev-methodology/coding-agent-harnesses/superpowers.md) |
| **SuperClaude Framework** | 当你常驻 Claude Code、想一次装好现成的命令、agent 和行为模式框架时用它。 | MIT | B（6/6） | [中](categories/agent-dev-methodology/coding-agent-harnesses/superclaude.zh.md) · [EN](categories/agent-dev-methodology/coding-agent-harnesses/superclaude.md) |
| **Get Shit Done (GSD)** | 当你靠 coding agent 写代码、想要一条规格驱动、每阶段全新上下文、对抗 context rot 的构建流水线时用它。 | MIT | D（6/6） | [中](categories/agent-dev-methodology/spec-driven-development/get-shit-done.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/get-shit-done.md) |
| **Compound Engineering** | 当你想要一套即插即用的 brainstorm→plan→work→review→compound 循环、并把经验跨会话沉淀复用时，就用它。 | MIT | B（4/5） | [中](categories/agent-dev-methodology/coding-agent-harnesses/compound-engineering.zh.md) · [EN](categories/agent-dev-methodology/coding-agent-harnesses/compound-engineering.md) |
| **ECC** | 当你想要一套有人维护、开箱即全的 Claude Code 底座（skill、agent、hook、memory 加安全扫描）时用它。 | MIT | B（6/6） | [中](categories/agent-dev-methodology/coding-agent-harnesses/ecc.zh.md) · [EN](categories/agent-dev-methodology/coding-agent-harnesses/ecc.md) |
| **LifeOS** | 当你想让 coding agent 跨会话携带*你自己*——沉淀好的个人档案、记忆和现状→理想状态仪表盘——而不是再多一套编码工作流时，用它。 | MIT | B（6/6） | [中](categories/agent-dev-methodology/coding-agent-harnesses/lifeos.zh.md) · [EN](categories/agent-dev-methodology/coding-agent-harnesses/lifeos.md) |
| **Spec Kit** | 当团队把功能代码交给 Copilot、Claude Code、Codex 或 Cursor 写，又想让每个功能先留下 spec → 方案 → 任务清单这条可评审的线索时用它——但 20 行的小修用它不划算，1.x 的 CLI 也几乎每周都在变。 | MIT | A（6/6） | [中](categories/agent-dev-methodology/spec-driven-development/spec-kit.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/spec-kit.md) |
| **Spec-Anchored Agentic Development** | 当永久 capability spec 必须持续充当代码一致性判定器时用它——仅面向 Claude Code，而且问世只有数天。 | MIT | B（3/5） | [中](categories/agent-dev-methodology/spec-driven-development/spec-anchored-agentic-development.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/spec-anchored-agentic-development.md) |
| **USDAD** | 当你想手工改造一套文字优先的多 agent 规格与上下文方法时用它——没有 CLI 或可执行约束。 | MIT | C（4/5） | [中](categories/agent-dev-methodology/spec-driven-development/usdad.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/usdad.md) |
| **QUAD Framework** | 仅当你要研究文档优先的四 Circles 运营模型与部署蓝图时使用——项目已不活跃、采用专有许可，且部分组件不可访问。 | Proprietary | D（5/6） | [中](categories/agent-dev-methodology/study-and-experiments/quad.zh.md) · [EN](categories/agent-dev-methodology/study-and-experiments/quad.md) |
| **LTBL Experiment** | 仅把它当作三个 agent 上下文实验实现的索引——自身没有可运行代码、实验结果或许可授权。 | NOASSERTION | D（4/6） | [中](categories/agent-dev-methodology/study-and-experiments/ltbl-experiment.zh.md) · [EN](categories/agent-dev-methodology/study-and-experiments/ltbl-experiment.md) |
| **PURE** | 当 intent 追溯需要 Git 原生 schema、registry、phase gate 和 Shell 检查时用它——结构明确，但非常年轻。 | MIT | C（5/6） | [中](categories/agent-dev-methodology/spec-driven-development/pure-agentic.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/pure-agentic.md) |
| **Claude Reviews Claude** | 想按章读懂那一个泄露的 Claude Code 版本（v2.1.88，2026 年 3 月）内部有什么时用它——2026-04-01 起冻结、源自专有代码，不能当作今天 Claude Code 的说明。 | MIT | C（4/5） | [中](categories/agent-dev-methodology/study-and-experiments/claude-reviews-claude.zh.md) · [EN](categories/agent-dev-methodology/study-and-experiments/claude-reviews-claude.md) |
| **Learn Claude Code** | 当你想通过亲手重建全部 17 个机制来搞懂 Claude Code 式 agent harness 的原理时用它——但它是课程，不是可 import 的库，也不是生产级 CLI。 | MIT | B（5/6） | [中](categories/agent-dev-methodology/study-and-experiments/learn-claude-code.zh.md) · [EN](categories/agent-dev-methodology/study-and-experiments/learn-claude-code.md) |
| **Claude Code Best Practice** | 把它当 Claude Code 功能与技巧的带出处地图，外加一个“命令 → 子 agent → skill”示例来读——它是 AI 刷新的课程，可能落后于官方文档，不是可安装的 harness，也不是配置项的权威来源。 | MIT | A（3/5） | [中](categories/agent-dev-methodology/study-and-experiments/claude-code-best-practice.zh.md) · [EN](categories/agent-dev-methodology/study-and-experiments/claude-code-best-practice.md) |
| **BMAD Method** | 当你要的是角色驱动的端到端 agent 方法（analyst、PM、架构、UX、开发、复核），而不是薄薄的 spec 管线时用它——并把飞快的涨星曲线当成未经验证。 | MIT | B（4/6） | [中](categories/agent-dev-methodology/spec-driven-development/bmad-method.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/bmad-method.md) |
| **Improve** | 当你想让昂贵模型只读审计仓库、再为便宜执行模型写出可交接的自包含计划时用它——它从不亲自实现。 | MIT | B（4/5） | [中](categories/agent-dev-methodology/spec-driven-development/improve.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/improve.md) |
| **Agent OS** | 当你要把项目 standards 装进去并选择性注入、在实现前先塑形计划时用它——发布线自 v3.0.0（2026-01）后一直很安静。 | MIT | B（4/5） | [中](categories/agent-dev-methodology/spec-driven-development/agent-os.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/agent-os.md) |

### ai-design-generation

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **json-render** | 当模型必须用你已有的组件在应用里拼界面、而不是发明 JSX 或新设计系统时用它。 | Apache-2.0 | B（6/6） | [中](categories/ai-design-generation/json-render.zh.md) · [EN](categories/ai-design-generation/json-render.md) |
| **HTML Anything** | 当你本机已登录某个 coding-agent CLI、想要零 API key、local-first 地把 Markdown 变成可交付 HTML 并一键导出微信/X/知乎时用它。 | Apache-2.0 | B（5/6） | [中](categories/ai-design-generation/html-anything.zh.md) · [EN](categories/ai-design-generation/html-anything.md) |
| **Open Design** | 想要一个 local-first、BYOK 的桌面 studio，让编码 agent 产出 HTML 原型、deck、图像和 HTML→MP4 动效时用它。 | Apache-2.0 | B（6/6） | [中](categories/ai-design-generation/open-design.zh.md) · [EN](categories/ai-design-generation/open-design.md) |
| **Impeccable** | 当你的 AI agent 总是产出同质化前端「AI 味」、需要确定性检测加设计 critique 时使用。 | Apache-2.0 | B（6/6） | [中](categories/ai-design-generation/impeccable.zh.md) · [EN](categories/ai-design-generation/impeccable.md) |
| **open-slide** | 想让编码 agent 在固定 1920×1080 画布上写 React 幻灯片、你靠点选元素留言来改稿时用它——deck 要作为可编辑 PowerPoint 文件流转、或要在 CI 里无头导出时不适合。 | MIT | C（6/6） | [中](categories/ai-design-generation/open-slide.zh.md) · [EN](categories/ai-design-generation/open-slide.md) |
| **ian-xiaohei-illustrations** | 当你要为中文文章批量生成风格一致、带小黑 IP 的手绘 16:9 正文配图时用它。 | MIT | B（4/5） | [中](categories/agent-skills/visual-content/ian-illustrations.zh.md) · [EN](categories/agent-skills/visual-content/ian-illustrations.md) |
| **Guizang PPT Skill** | 当你想让 agent 把文章变成有设计感的单文件 HTML 翻页 PPT（杂志风或瑞士风）时用它。 | AGPL-3.0-only | C（4/5） | [中](categories/agent-skills/slides-ppt/guizang-ppt.zh.md) · [EN](categories/agent-skills/slides-ppt/guizang-ppt.md) |
| **Guizang Social Card Skill** | 当你在 Claude Code/Codex 里想让 agent 用锁定的编辑风/瑞士风生成小红书图文或公众号封面对（单文件 HTML 渲染成 PNG）时使用。 | AGPL-3.0-only | D（3/5） | [中](categories/agent-skills/visual-content/guizang-social-card.zh.md) · [EN](categories/agent-skills/visual-content/guizang-social-card.md) |
| **handraw-style** | 当你想把编号化的手绘画风、版面图型与主题色（279/122/36）交给装好的 agent skill 拼成中英双语生图提示词时用它。 | MIT | C（4/5） | [中](categories/agent-skills/visual-content/handraw-style.zh.md) · [EN](categories/agent-skills/visual-content/handraw-style.md) |
| **hand-drawn-styles** | 当你已经定下几种手绘画风、需要 agent 把每套实测配方原样复现（22 套配方，其中三套带锚点图和验收规则）成可复制的生图提示词时用它。 | MIT | C（5/6） | [中](categories/agent-skills/visual-content/hand-drawn-styles.zh.md) · [EN](categories/agent-skills/visual-content/hand-drawn-styles.md) |
| **Lieflat Charts** | 当你想让编码助手把数据做成模板锁定、可直接发布的单文件 HTML 图表或 12 套中英双语整页报告、整套交付共用一种编辑风视觉语言时用它。 | PolyForm-Noncommercial-1.0.0 | C（3/5） | [中](categories/agent-skills/visual-content/lieflat-charts.zh.md) · [EN](categories/agent-skills/visual-content/lieflat-charts.md) |
| **SdPaint** | 当你已在跑带 ControlNet 的 AUTOMATIC1111、想让每一笔涂鸦实时变成生成图时用它——但它自身不带模型，且自 2024-04 起停滞。 | MIT | D（3/6） | [中](categories/ai-design-generation/sdpaint.zh.md) · [EN](categories/ai-design-generation/sdpaint.md) |
### dev-utilities

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **DevToys** | 当你想把 JWT/Base64 解码、JSON 格式化、diff、哈希等约 30 个开发小工具收进一个离线桌面应用、不再把密钥粘进在线网站时用它——但所有 2.x 构建都是预发布版，更新稀疏且成批出现。 | MIT | B（5/6） | [中](categories/dev-utilities/data-tools/devtoys.zh.md) · [EN](categories/dev-utilities/data-tools/devtoys.md) |
| **CyberChef** | 当你需要在浏览器里离线串联编解码、加解密、压缩和数据分析变换、且数据不能外发时用它。 | Apache-2.0 | A（6/6） | [中](categories/dev-utilities/data-tools/cyberchef.zh.md) · [EN](categories/dev-utilities/data-tools/cyberchef.md) |
| **Cockpit** | 当你需要为少数几台 Linux 服务器用浏览器做 systemd 原生的图形化管理时用它。 | LGPL-2.1-or-later | B（5/6） | [中](categories/dev-utilities/ops-infra/cockpit.zh.md) · [EN](categories/dev-utilities/ops-infra/cockpit.md) |
| **Telegraf** | 当你需要一个插件驱动的 agent 把异构指标/日志统一采集并路由到多种后端时用它。 | MIT | A（6/6） | [中](categories/dev-utilities/ops-infra/telegraf.zh.md) · [EN](categories/dev-utilities/ops-infra/telegraf.md) |
| **OpenZL** | 当你要把 TB 级的某种高度结构化/数值格式压得比通用 zstd 更狠时使用。 | BSD-3-Clause | C（5/6） | [中](categories/dev-utilities/data-tools/openzl.zh.md) · [EN](categories/dev-utilities/data-tools/openzl.md) |
| **Certbot** | 当系统管理员要自动签发并续期免费 Let's Encrypt TLS 证书时用它——不过反向代理自带的自动 TLS 常让它显得多余。 | Apache-2.0 | A（5/6） | [中](categories/dev-utilities/ops-infra/certbot.zh.md) · [EN](categories/dev-utilities/ops-infra/certbot.md) |
| **tqdm** | 当你想给 Python 循环/CLI/notebook 加一个快速、低开销的进度条时用它。 | MPL-2.0 AND MIT | B（5/6） | [中](categories/dev-utilities/data-tools/tqdm.zh.md) · [EN](categories/dev-utilities/data-tools/tqdm.md) |
| **SlimToolkit** | 当你想在不重写 Dockerfile 的情况下自动瘦身并加固臃肿的容器镜像时用它——注意它可能删掉运行时动态加载的文件。 | Apache-2.0 | B（6/6） | [中](categories/dev-utilities/ops-infra/slim.zh.md) · [EN](categories/dev-utilities/ops-infra/slim.md) |
| **Faker (faker-js)** | 当你需要在 JS/TS 里生成逼真的假/mock 数据（姓名、地址、金融…）用于测试和填充时用它。 | MIT | A（5/6） | [中](categories/dev-utilities/data-tools/faker-js.zh.md) · [EN](categories/dev-utilities/data-tools/faker-js.md) |
| **fontTools** | 当你需要对字体做程序化处理——子集化网页字体、转格式、查改表——时用它——但它只编辑字体文件，不绘制字形也不做文字排版。 | MIT | A（6/6） | [中](categories/dev-utilities/data-tools/fonttools.zh.md) · [EN](categories/dev-utilities/data-tools/fonttools.md) |
| **Flashlight** | 仅当你守着一台 macOS 10.10–10.15 老机器、想让原生 Spotlight 直接跑 Python 插件给出结果时用它——但它自 2020 年起已弃，Big Sur 及以后基本不可用，且要关闭 SIP 向系统进程注入代码。 | MIT AND GPL-2.0-only (component split) | E（3/6） | [中](categories/dev-utilities/data-tools/flashlight.zh.md) · [EN](categories/dev-utilities/data-tools/flashlight.md) |
| **IdeaVim** | 当你离不开 JetBrains IDE、又想要 Vim 的动作、模式和 `.ideavimrc` 时用它——但它只是 Vim 子集的模拟，重度用户会撞上还原度的缺口。 | MIT | A（4/6） | [中](categories/dev-utilities/editors-and-runtimes/code-editors/ideavim.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/code-editors/ideavim.md) |
| **VS Code** | 当团队横跨多种语言和操作系统、想用一个编辑器，靠几乎所有工具都先支持的扩展生态拿到语言能力和远程、容器开发时用它——但官方构建带微软遥测和专有许可，换 VSCodium 又会失去微软专有扩展。 | MIT | A（5/6） | [中](categories/dev-utilities/editors-and-runtimes/code-editors/vscode.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/code-editors/vscode.md) |
| **Clash Verge Rev** | 当你在桌面电脑上有一份 Clash 格式订阅，想用 TUN 模式让整台机器（包括终端工具）按规则分流时用它——但它只有桌面版，TUN 还需要装特权服务或提权运行。 | GPL-3.0 | B（6/6） | [中](categories/dev-utilities/ops-infra/clash-verge-rev.zh.md) · [EN](categories/dev-utilities/ops-infra/clash-verge-rev.md) |
| **RustDesk** | 当你要照看几台不在身边的机器，想要 TeamViewer 式“输 ID 就连”的跨 NAT 体验、撮合和中继服务器又放在自己手里时用它——但开源服务端没有管理后台、SSO 和审计日志，这些在付费的 Server Pro 里。 | AGPL-3.0 | A（6/6） | [中](categories/dev-utilities/ops-infra/rustdesk.zh.md) · [EN](categories/dev-utilities/ops-infra/rustdesk.md) |
| **Tauri** | 当一个 Web 前端的桌面应用要做到安装包小、内存低，而不是像 Electron 那样捎带整份 Chromium 时用它——但各系统 webview 渲染不一致，Linux 需要 webkit2gtk 4.1，原生逻辑必须用 Rust 写。 | Apache-2.0 OR MIT | A（6/6） | [中](categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/tauri.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/tauri.md) |
| **Deno** | 当你新起一个 TypeScript 后端、命令行工具或脚本，默认拒绝文件、网络和环境变量访问以及内置 fmt、lint、test 比原样运行现有 Node 代码更重要时用它——但大型 Node 应用迁移和依赖原生插件的项目不合适。 | MIT | A（6/6） | [中](categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/deno.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/deno.md) |
| **Vaultwarden** | 当你想让家人或小团队继续用 Bitwarden 官方应用、但把密码库放在自己的一台小服务器上时用它——但客户端一更新你就得及时升级服务端，而且没有厂商支持、SAML/SCIM 或内置故障切换。 | AGPL-3.0 | B（6/6） | [中](categories/dev-utilities/ops-infra/vaultwarden.zh.md) · [EN](categories/dev-utilities/ops-infra/vaultwarden.md) |
| **Zed** | 当编辑器延迟比扩展数量更重要、你想要一个用 GPU 渲染的原生编辑器，并内置语言服务器、调试器、AI 代理和多人协作时用它——但 VS Code 扩展跑不了，机器必须有可用的显卡驱动，多人协作还要登录 Zed 的服务。 | GPL-3.0-or-later AND Apache-2.0 (per README; GitHub reports NOASSERTION) | A（4/6） | [中](categories/dev-utilities/editors-and-runtimes/code-editors/zed.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/code-editors/zed.md) |
| **BrewUI** | 当你在 macOS 26 上想要 Homebrew 官方 GUI，并且要把底层每条 `brew` 命令显示在可复制的控制台里时用它。 | AGPL-3.0 | C（5/6） | [中](categories/dev-utilities/package-manager-gui/brewui.zh.md) · [EN](categories/dev-utilities/package-manager-gui/brewui.md) |
| **Applite** | 当非技术用户需要在从未有过终端的机器上安装 Mac 应用时用它——它自带 Homebrew，且只管理 cask。 | MIT | A（6/6） | [中](categories/dev-utilities/package-manager-gui/applite.zh.md) · [EN](categories/dev-utilities/package-manager-gui/applite.md) |
| **CaskHub** | 当你在 macOS 15.6+ 上想要最丰富的应用商店式 cask 浏览体验时用它，但要接受内置的遥测。 | MIT | B（6/6） | [中](categories/dev-utilities/package-manager-gui/caskhub.zh.md) · [EN](categories/dev-utilities/package-manager-gui/caskhub.md) |
| **Cork** | 当你想要最完整的 Homebrew 操作面——services、tap、标签、菜单栏更新——并愿意为预编译版付 25€ 时用它。 | NOASSERTION (Commons Clause-based, source-available) | B（5/6） | [中](categories/dev-utilities/package-manager-gui/cork.zh.md) · [EN](categories/dev-utilities/package-manager-gui/cork.md) |
| **Cakebrew** | 只把它当作第一代 Homebrew GUI 的参考；它自 2021 年起实际已无人维护，也没有可安装的 cask。 | GPL-3.0 | D（4/6） | [中](categories/dev-utilities/package-manager-gui/cakebrew.zh.md) · [EN](categories/dev-utilities/package-manager-gui/cakebrew.md) |
| **ripgrep** | 当你或编码 agent 一天要在代码库里搜几十次、想要默认递归、遵守 .gitignore 的快速文本搜索时用它——但不适合要在任意 POSIX 机器上跑的可移植脚本、归档内部搜索，或只知道行为不知道标识符的场景。 | Unlicense OR MIT | B（6/6） | [中](categories/dev-utilities/data-tools/ripgrep.zh.md) · [EN](categories/dev-utilities/data-tools/ripgrep.md) |
| **Bun** | 当一个 Node.js 上的 TypeScript 项目想用一个快速二进制同时负责运行 .ts、装包、打包和测试时用它——但 Node API 尚未完全兼容，v1.4 刚把代码库从 Zig 重写为 Rust，也没有权限沙箱。 | MIT (statically links LGPL-2 JavaScriptCore; GitHub reports NOASSERTION) | A（5/6） | [中](categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/bun.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/bun.md) |
| **scriptc** | 把类型写干净的 TypeScript CLI 和小型服务用真正的 tsc 编译成约 320KB 的原生可执行文件（或 WASI 模块），二进制里没有 JS 引擎——但它只是两个月大的 Vercel Labs 实验，编不了静态的部分会被直接拒绝。 | Apache-2.0 | C（6/6） | [中](categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/scriptc.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/scriptc.md) |
| **TanStack CLI** | 脚手架 TanStack Start／Router 应用，把认证、数据库、部署、监控当作可互相协调的 add-on 组合进去，另有一组面向 agent 的 JSON 内省命令——但它只认 TanStack 栈（前 1.0 变动频繁，遥测默认开启）。 | MIT | B（6/6） | [中](categories/dev-utilities/editors-and-runtimes/tanstack-tooling/tanstack-cli.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/tanstack-tooling/tanstack-cli.md) |
| **TanStack Devtools** | 一个页内可停靠面板，把 TanStack（及自家）库的调试器装成标签页，配套 Vite／Rspack 插件提供点元素跳源码、console 转发和生产构建自动剥离——但仍是 alpha，会把 Solid.js 带进开发包，开发期事件总线还有一份未修的命令注入报告。 | MIT | B（6/6） | [中](categories/dev-utilities/editors-and-runtimes/tanstack-tooling/tanstack-devtools.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/tanstack-tooling/tanstack-devtools.md) |
| **JumpServer** | 当你需要一台自建堡垒机（PAM）替人保管目标机凭据、录下每个 SSH、RDP、数据库和 Kubernetes 会话时用它——但社区版上限 5000 台资产，高可用、SSO、改密都在企业版，且每年都有严重级漏洞公告。 | GPL-3.0 | B（6/6） | [中](categories/dev-utilities/ops-infra/jumpserver.zh.md) · [EN](categories/dev-utilities/ops-infra/jumpserver.md) |
| **TanStack Config** | TanStack 自家库共用的开发期预设：带类型信息的 ESLint 扁平配置、ESM／CJS 双格式 Vite 库构建、TypeDoc 转 Markdown、按提交信息发版的脚本——检查预设用得很广，构建与发布两半在 TanStack 内部已成遗留（转向 tsdown、Changesets）；只支持 pnpm。 | MIT | B（6/6） | [中](categories/dev-utilities/editors-and-runtimes/tanstack-tooling/tanstack-config.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/tanstack-tooling/tanstack-config.md) |
| **zerobrew** | 当你经常重装同一批 Homebrew 命令行 formula，想让一个和 `brew` 并排的 Rust 客户端把同样的 bottle 快几倍地装上时用它——但它是实验性的，不执行 `post_install`，cask 只支持带二进制产物的。 | Apache-2.0 OR MIT | B（6/6） | [中](categories/dev-utilities/package-managers/zerobrew.zh.md) · [EN](categories/dev-utilities/package-managers/zerobrew.md) |
| **TanStack Container** | 把真实的 Vite／TanStack Start 项目（安装、进程、预览、存档恢复）整个跑在访客的浏览器标签页里，MIT 开源、资源自己托管——但 2026-09 时 npm 包还没发布：这是值得跟踪的 pre-alpha 押注，还不是能上线依赖的东西。 | MIT | C（5/6） | [中](categories/dev-utilities/editors-and-runtimes/tanstack-tooling/tanstack-container.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/tanstack-tooling/tanstack-container.md) |
| **TanStack alt-cli** | 2026 年 1 月只活了一周的 TanStack 实验：用 29 个带元数据声明的集成组合出 TanStack Start 项目，并以 MCP 面向 agent 开放脚手架——已归档，`@tanstack/cli` 包名被主线 CLI 收回；当模式参考读，脚手架用 TanStack CLI。 | MIT | D（5/6） | [中](categories/dev-utilities/editors-and-runtimes/tanstack-tooling/tanstack-alt-cli.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/tanstack-tooling/tanstack-alt-cli.md) |
| **NetWasm** | 把可达的 C# 编译成一个极小的独立 WASI 组件——GC 链接在产物里、目标机器不装 .NET 运行时——但它是 7 周大的单人 pre-1.0 项目，编译器工具链挂自定义非开源许可证。 | NOASSERTION (Community License 1.0 tooling + MIT core) | C（4/6） | [中](categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/netwasm.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/netwasm.md) |
| **Effect** | 把 TypeScript 操作的错误、依赖和取消写进类型，并跑在一个零依赖的纤程运行时上，schema、HTTP、SQL 和追踪都在同一个包里——但这套模型会传染，4.0 才发布一周，核心之外的大多数模块还标着 unstable。 | MIT | A（6/6） | [中](categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/effect.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/effect.md) |
| **fzf** | 当你在终端里频繁从长列表（历史命令、文件、分支、进程）里挑一项、想用 CTRL-R、CTRL-T 边敲边筛时用它——但它只过滤喂给它的行、不搜文件内容，而且实际上是单人维护。 | MIT | A（6/6） | [EN](categories/dev-utilities/data-tools/fzf.md) · [中](categories/dev-utilities/data-tools/fzf.zh.md) |
| **jq** | 当终端里满是嵌套 JSON（kubectl、aws、gh api、webhook 负载），你要用一行能接管道的命令抽取或过滤字段时用它——但不适合几 GB 的分析型查询、非 JSON 输入，或超过 2^53 的整数运算。 | MIT | A（5/6） | [EN](categories/dev-utilities/data-tools/jq.md) · [中](categories/dev-utilities/data-tools/jq.zh.md) |
| **Descheduler** | 当 Kubernetes 集群已经失衡、你想要一个 CronJob 定期驱逐违反策略的 Pod、让调度器重新安置它们时用它——它不是算出来的 placement 计划。 | Apache-2.0 | A（6/6） | [中](categories/dev-utilities/ops-infra/descheduler.zh.md) · [EN](categories/dev-utilities/ops-infra/descheduler.md) |

### frontend-animation

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Anime.js** | 零依赖的 JS 动画引擎：统一 animate() API 驱动 CSS、SVG、DOM 属性和 JS 对象，内置时间线、错峰、弹簧缓动和滚动联动。 | MIT | B（5/6） | [中](categories/frontend-animation/anime.zh.md) · [EN](categories/frontend-animation/anime.md) |

### api-gateway

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Kong Gateway** | 基于 OpenResty/Nginx 的 API 网关，插件层把一个反向代理变成可编程边界：既管 REST/微服务，也从 3.x 起管 LLM/MCP 流量。 | Apache-2.0 | B（6/6） | [中](categories/api-gateway/kong.zh.md) · [EN](categories/api-gateway/kong.md) |
| **Funtool** | 只有“Windows＋Claude Code＋NVIDIA”这条精确代理路径命中任务时才用它——当前可执行文件不透明，也无法从公开源码重建。 | MIT | C（5/6） | [中](categories/api-gateway/funtool.zh.md) · [EN](categories/api-gateway/funtool.md) |
| **HarnessRouter** | 把 Codex、Claude Code、Hermes 等 harness 统一跑在一个 OpenAI Responses 兼容 API 之后的自托管网关——但它仅约 6 周历史，UHP 标准由单一厂商维护。 | Apache-2.0 | B（5/6） | [中](categories/api-gateway/harnessrouter.zh.md) · [EN](categories/api-gateway/harnessrouter.md) |
| **LiteLLM** | 覆盖 100 多家供应商的可部署 LLM 网关与 SDK，带虚拟密钥、预算、花费追踪与故障转移——但需要 PostgreSQL/Redis 运维，且有 `enterprise/` 商业边界。 | MIT（核心）+ enterprise/ 商业目录 | A（4/6） | [中](categories/api-gateway/litellm.zh.md) · [EN](categories/api-gateway/litellm.md) |
| **Claude Code Router** | 本地控制面：从桌面/CLI 界面用条件规则与 fallback，让 Claude Code 等 coding agent 跨模型供应商路由。 | MIT | B（6/6） | [中](categories/api-gateway/claude-code-router.zh.md) · [EN](categories/api-gateway/claude-code-router.md) |
| **CLIProxyAPI** | 把消费级 CLI/OAuth 登录态包装成 OpenAI/Gemini/Claude 兼容 API 供其他工具调用——代价是固化的服务条款/账号风险与主机上的 token 存储。 | MIT | B（5/6） | [中](categories/api-gateway/cliproxyapi.zh.md) · [EN](categories/api-gateway/cliproxyapi.md) |
| **APISIX** | 当你要 ASF 治理、配置由 etcd 动态驱动、插件在进程内的网关时用它——etcd 控制面也得你自己运维。 | Apache-2.0 | A（6/6） | [中](categories/api-gateway/apisix.zh.md) · [EN](categories/api-gateway/apisix.md) |
| **Envoy** | 当你要一个由 xDS 驱动的 L4/L7 数据面、且愿意自备控制面时用它——它比开箱即用的 API 网关更底层。 | Apache-2.0 | A（6/6） | [中](categories/api-gateway/envoy.zh.md) · [EN](categories/api-gateway/envoy.md) |
| **TokenHub** | 治理优先的自托管 Go AI 网关：项目 key、配额、路由策略、审计和供应商账单核对——非常年轻（v0.9.x，建于 2026-06）且作者主导。 | Apache-2.0 | B（6/6） | [中](categories/api-gateway/tokenhub.zh.md) · [EN](categories/api-gateway/tokenhub.md) |
| **Magpie (yetone)** | 给约 28 个 coding agent 用的菜单栏模型切换器，外加在 Anthropic 与 OpenAI 接口间翻译的本地网关，订阅登录也能当 provider——只有约一周历史，单人维护。 | MIT | C（5/6） | [中](categories/api-gateway/magpie-model-router.zh.md) · [EN](categories/api-gateway/magpie-model-router.md) |
| **vLLM Semantic Router** | 挂在 Envoy ExtProc 上的决策层，用自带分类器算出的领域、难度、越狱、PII 信号，按 YAML 策略逐请求选模型；还没到 1.0（v0.4，建于 2025-08），密钥和限流仍要靠网关。 | Apache-2.0 | B（5/6） | [中](categories/api-gateway/vllm-semantic-router.zh.md) · [EN](categories/api-gateway/vllm-semantic-router.md) |
| **Monid** | “工具版 OpenRouter”的开源连接器标准和引擎：约 700 个数据和媒体厂商端点写成声明式文件，自带按次用量计量——`discover` 路由、单一 key 和定价在闭源托管侧；仓库约六周大。 | MIT | B（6/6） | [中](categories/api-gateway/monid.zh.md) · [EN](categories/api-gateway/monid.md) |

### geospatial

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **QGIS** | 功能完整、跨平台的桌面 GIS(Qt/C++)：浏览、编辑、分析、发布矢量/栅格/网格/点云空间数据，带 PyQGIS 插件和无界面 Server。 | GPL-2.0-or-later | B（6/6） | [中](categories/geospatial/qgis.zh.md) · [EN](categories/geospatial/qgis.md) |

### team-chat

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Mattermost** | 自托管的 Slack 式协作（聊天、通话、屏幕共享），以单个 Go 二进制跑在 PostgreSQL 上；企业 SSO/合规能力单独授权。 | AGPL-3.0（源码）/ MIT（二进制） | A（5/6） | [中](categories/team-chat/mattermost.zh.md) · [EN](categories/team-chat/mattermost.md) |
| **Zulip** | 自托管、按话题分线程的团队聊天（Apache-2.0），适合异步优先的团队——需一台专用 Ubuntu/Debian 主机，语音/视频交给集成。 | Apache-2.0 | A（6/6） | [中](categories/team-chat/zulip.zh.md) · [EN](categories/team-chat/zulip.md) |
| **Rocket.Chat** | 自托管通信平台（MIT 社区版），带应用市场、全渠道客服与原生联邦——但要运维 MongoDB + NATS + 微服务。 | MIT（社区版）+ EE | A（5/6） | [中](categories/team-chat/rocket-chat.zh.md) · [EN](categories/team-chat/rocket-chat.md) |
| **Buzz** | 自托管 Nostr 工作区，人和 AI agent 是同一条事件日志上的签名同等成员——agent 原生、pre-1.0、基础设施重。 | Apache-2.0 | B（4/6） | [中](categories/team-chat/buzz.zh.md) · [EN](categories/team-chat/buzz.md) |
| **Macro** | 用一个工作区替换 Slack + Linear + Notion + CRM + Gmail 客户端，所有东西在同一个库里互相 @ 链接，并通过 MCP 开放给 agent——AGPL、以托管为主，自托管仍是开发者环境。 | AGPL-3.0 | B（6/6） | [中](categories/team-chat/macro.zh.md) · [EN](categories/team-chat/macro.md) |
| **HiveChat** | 当一个 5–50 人的团队需要自托管聊天前端、由管理员统一握住多家大模型的 API key 并按分组控制可见模型和 token 配额时用它——但它自 2025-09 起再无提交，版本仍是 v0.1.0。 | Apache-2.0 | D（3/6） | [中](categories/team-chat/hivechat.zh.md) · [EN](categories/team-chat/hivechat.md) |

### captcha

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Cap** | 轻量、可自托管的 CAPTCHA 替代：无感工作量证明（Rust→WASM worker 做 SHA-256 nonce 搜索）发放服务端可校验 token——无图片、不调第三方。 | Apache-2.0 | C（5/6） | [中](categories/captcha/capjs.zh.md) · [EN](categories/captcha/capjs.md) |
| **Text_select_captcha** | 当经授权的自动化要解中文文字点选验证码、想在纯 CPU 上跑（YOLO 检测加孪生网络匹配，走 ONNX）时用它——但仓库没有 LICENSE 文件，默认保留所有权利，合法性是第一道门槛。 | NONE (no LICENSE file — all rights reserved) | D（5/6） | [中](categories/captcha/text-select-captcha.zh.md) · [EN](categories/captcha/text-select-captcha.md) |
| **pytorch-captcha-recognition** | 想要一份可读的定长文字验证码教学基线（每个字符位一个 CNN 分类头）时用它——但它是 2020 年冻结的教程，PyTorch API 需要现代化改造，准确率数字也只来自它自己的合成数据。 | Apache-2.0 | D（4/6） | [中](categories/captcha/pytorch-captcha-recognition.zh.md) · [EN](categories/captcha/pytorch-captcha-recognition.md) |
| **captcha (lepture)** | 当 Python 表单需要一个自托管、不调第三方的图片或语音验证码，而存储、过期和校验你打算自己写时用它——但扭曲文字挡不住廉价 OCR，只能当减速带，算不上机器人防护。 | BSD-3-Clause | B（5/6） | [中](categories/captcha/lepture-captcha.zh.md) · [EN](categories/captcha/lepture-captcha.md) |
| **NopeCHA** | 只用于已授权、需无人值守覆盖多类验证码的自动化——持续维护的实现闭源，并依赖托管 API。 | MIT | B（6/6） | [中](categories/captcha/nopecha-extension.zh.md) · [EN](categories/captcha/nopecha-extension.md) |
| **Buster** | 用于真人触发的 reCAPTCHA 音频无障碍辅助或已授权测试——源码可审计、可走本地模型，但覆盖窄且结果不确定。 | GPL-3.0-only | C（6/6） | [中](categories/captcha/buster.zh.md) · [EN](categories/captcha/buster.md) |

### blockchain-dev-infrastructure

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **PoWFaucet** | 当公共 EVM 测试网需要带模块化防滥用控制的 faucet 时用它——热钱包托管、资金补充和高强度服务运维仍由你承担。 | AGPL-3.0 | C（5/6） | [中](categories/blockchain-dev-infrastructure/powfaucet.zh.md) · [EN](categories/blockchain-dev-infrastructure/powfaucet.md) |
### ml-research

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **autoresearch** | 当你有一块 NVIDIA GPU、想让自己的 coding agent 通宵改 train.py、每轮固定跑 5 分钟、只保留降低验证集 bits-per-byte 的改动时用它——但它不带 agent 运行器，且是无 tag 的 demo，自 2026-03 起未再更新。 | MIT | B（4/6） | [中](categories/ml-research/research-automation/autoresearch.zh.md) · [EN](categories/ml-research/research-automation/autoresearch.md) |
| **Context Language Models (CLM)** | 用来研究或评测“让 agent 的模型自己改写实时上下文”（它用 bash 改写一份对话镜像文件）：跑在 Harbor 任务上，带 FLOPs 记账和一个 SGLang KV 复用补丁——论文代码，CC BY-NC 4.0，仅限非商用。 | CC-BY-NC-4.0 | D（4/6） | [EN](categories/ml-research/context-language-models.md) · [中](categories/ml-research/context-language-models.zh.md) |
| **llm-circuit-finder** | 当你手里有本地 GGUF 模型、想搜出该复制哪段连续层块再用探针和 lm-evaluation-harness 量效果时用它——但收益是此消彼长（Devstral 全指标平均反而下降），且它是只支持 GGUF 的一次性 demo。 | MIT | D（4/6） | [中](categories/ml-research/llm-circuit-finder.zh.md) · [EN](categories/ml-research/llm-circuit-finder.md) |
| **CLIP** | 当你想把标签写成纯文本、直接用 OpenAI 原始 checkpoint 做零样本图像分类或图文检索时用它——但它是冻结的参考实现，骨干是较老的 ViT／ResNet；要更多模型和持续维护请用 OpenCLIP 或 transformers。 | MIT | C（5/6） | [中](categories/ml-research/vision-and-multimodal/clip.zh.md) · [EN](categories/ml-research/vision-and-multimodal/clip.md) |
| **TaskMatrix** | 仅当你想研究 Visual ChatGPT 当年怎样用 prompt 把纯文本 ChatGPT 路由到约 20 个视觉基础模型时用它——它自 2023-06 起已停更，现代多模态大模型在单个模型里就原生做到了。 | MIT | "?"（2/6） | [中](categories/ml-research/vision-and-multimodal/taskmatrix.zh.md) · [EN](categories/ml-research/vision-and-multimodal/taskmatrix.md) |
| **PyTorch-GAN** | 当你想把 2014–2018 年的经典 GAN 论文各对应一个自包含 PyTorch 脚本来读（DCGAN、CycleGAN、WGAN-GP、pix2pix）时用它——但作者已自称停更，2021 年后再无提交，真实生成任务早已转向扩散模型。 | MIT | D（3/6） | [中](categories/ml-research/vision-and-multimodal/pytorch-gan.zh.md) · [EN](categories/ml-research/vision-and-multimodal/pytorch-gan.md) |
| **LSTM Neural Network for Time Series Prediction** | 当你想跟着配套文章一步步看一个 Keras 堆叠 LSTM 在正弦波和标普 500 数据上训练、出图时用它——但它钉死在 2018 年前后的 TensorFlow 1.10 与 Python 3.5 上，2019 年起已冻结，且为 AGPL-3.0。 | AGPL-3.0 | E（4/6） | [中](categories/ml-research/nlp-and-time-series/lstm-time-series.zh.md) · [EN](categories/ml-research/nlp-and-time-series/lstm-time-series.md) |
| **Agriculture Knowledge Graph (AgriKG)** | 当你要一份跑通的中文领域知识图谱整链示例（爬虫、实体打标、关系抽取、Neo4j、Django 问答）外加现成农业数据时用它——但作者已声明停止维护，技术栈陈旧，代码是 GPL-3.0。 | GPL-3.0 | D（3/6） | [中](categories/ml-research/nlp-and-time-series/agriculture-knowledge-graph.zh.md) · [EN](categories/ml-research/nlp-and-time-series/agriculture-knowledge-graph.md) |
| **Senta (SKEP)** | 当你身处 PaddlePaddle 栈、要用发布的中英文 checkpoint 复现或扩展 SKEP 情感论文时用它——但它钉死在 Paddle 1.6.3 加 CUDA 10.1 上，自 2020 年起无提交，百度更新的 NLP 工作在 PaddleNLP。 | Apache-2.0 | D（4/6） | [中](categories/ml-research/nlp-and-time-series/senta.zh.md) · [EN](categories/ml-research/nlp-and-time-series/senta.md) |
| **Depth Anything V2** | 当你要从单张图像得到稠密深度图（三维重建、虚化、AR 遮挡、可控生成）又不想训练模型时用它——但只有 Small 权重是 Apache-2.0，Base／Large／Giant 是禁止商用的 CC-BY-NC-4.0，且默认输出是相对深度而非米制。 | Apache-2.0 | C（4/6） | [中](categories/ml-research/vision-and-multimodal/depth-anything-v2.zh.md) · [EN](categories/ml-research/vision-and-multimodal/depth-anything-v2.md) |
| **Open-Sora** | 当你要在数据中心 GPU 上按完整公开的配方（代码、数据流水线、成本报告）**训练**或研究视频扩散模型时用它——2025-03 起停更，权重栈牵入 FLUX.1-dev 非商用和腾讯混元许可证。 | Apache-2.0 | B（4/6） | [中](categories/ml-research/vision-and-multimodal/open-sora.zh.md) · [EN](categories/ml-research/vision-and-multimodal/open-sora.md) |
| **pymoo** | 当需要 Python 演化式多目标优化（NSGA-II/III、MOEA/D）求 Pareto 前沿时用它——若问题是凸／线性／单目标，LP 或梯度求解器要快得多。 | Apache-2.0 | B（6/6） | [中](categories/ml-research/pymoo.zh.md) · [EN](categories/ml-research/pymoo.md) |
| **The AI Scientist** | 当你想让「想法到论文」这整圈全自动跑完——想法生成、查新、实验代码、作图，最后编译出带 LLM 评审的 LaTeX 论文——时用它，但要接受一条绑死模板、自改许可证后冻结、且限制你发布其产出的流水线。 | NOASSERTION (The AI Scientist Source Code License) | D（4/6） | [中](categories/ml-research/research-automation/ai-scientist.zh.md) · [EN](categories/ml-research/research-automation/ai-scientist.md) |
| **Agent Laboratory** | 当你想让一组扮演角色的 LLM agent 跑「文献回顾→计划→实验→报告」、每阶段由你确认，并且要 MIT 条款和可续跑 checkpoint 时用它，但它自 2025-03 起没有代码改动，还挂着一条无人回应的安全披露。 | MIT | C（3/6） | [中](categories/ml-research/research-automation/agent-laboratory.zh.md) · [EN](categories/ml-research/research-automation/agent-laboratory.md) |
| **RRSI** | 当你想复现或改造“自动改 agent harness”的搜索、并要一套防背题的刹车（有界带标签改动、泄题评审、噪声下限、token 成本规则）时用它——但搜索角色绑死 Vertex AI 上的 Claude，一次运行要跑几千次完整基准。 | Apache-2.0 | C（5/6） | [中](categories/ml-research/research-automation/rrsi.zh.md) · [EN](categories/ml-research/research-automation/rrsi.md) |
### agent-skills

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **book-to-skill** | 当编码智能体总要参考几本技术书或一个文档目录，你想把每本变成按章索引的技能、不再每次重贴 PDF 时用它——但它是概括而不是摘录原文，项目也才五个月左右。 | MIT | B（6/6） | [中](categories/agent-skills/book-to-skill.zh.md) · [EN](categories/agent-skills/book-to-skill.md) |
| **distilly** | 当你想把某个人的聊天记录、文档与访谈蒸馏成可安装的 agent 技能，让它用这个人的判断与语气回答时用它。 | MIT | B（4/5） | [中](categories/agent-skills/distilly.zh.md) · [EN](categories/agent-skills/distilly.md) |

#### agent-skills / engineering

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Agent Skills (addyosmani)** | 约 24 个生产级工程技能包（质量/安全/web 性能/API/发布），装进 coding agent 并通过约 8 个 SDLC 斜杠命令路由。 | MIT | A（4/5） | [中](categories/agent-skills/engineering/addyosmani-agent-skills.zh.md) · [EN](categories/agent-skills/engineering/addyosmani-agent-skills.md) |
| **web-quality-skills** | 含六个技能的 agent 技能包，把 Lighthouse / Core Web Vitals / WCAG / SEO 最佳实践编码成按需加载的指令集，让 coding agent 审计并修复 web 质量问题；属建议层，非测量工具。 | MIT | B（4/5） | [中](categories/agent-skills/engineering/addyosmani-web-quality.zh.md) · [EN](categories/agent-skills/engineering/addyosmani-web-quality.md) |
| **Scientific Agent Skills** | 一个大型 skill 包（约 147 个 skill），把 coding agent 变成生物、化学、医学、药物发现领域的科研助手——每个 skill 用一份带文档的 SKILL.md 封装一个科学 Python 库或数据库，按需加载。 | MIT | A（4/5） | [中](categories/agent-skills/engineering/scientific-agent-skills.zh.md) · [EN](categories/agent-skills/engineering/scientific-agent-skills.md) |
| **Auto-Empirical Research Skills** | 当 coding agent 要做社会科学实证论文（双重差分／工具变量／断点／合成控制、稳健性、期刊表格），你需要一份会路由到单个 skill 的目录，而不是通用写代码提示时用它。 | CC-BY-SA-4.0 | C（3/5） | [中](categories/agent-skills/engineering/auto-empirical-research-skills.zh.md) · [EN](categories/agent-skills/engineering/auto-empirical-research-skills.md) |
| **Vercel Agent Skills** | Vercel 官方 agent-skill 包——按需安装的 React/Next.js/Vercel 部署、Web 设计与文档审查指南，采用 agentskills.io/skills.sh 格式。 | MIT | B（4/6） | [中](categories/agent-skills/engineering/vercel-agent-skills.zh.md) · [EN](categories/agent-skills/engineering/vercel-agent-skills.md) |
| **cc-skills-golang** | 当你的 coding agent 写出能编译但不地道的 Go（error 包装、nil 陷阱、命名）时用它——要的是按需加载的 Go 说明书，不是流程／TDD 包。 | MIT | C（5/6） | [中](categories/agent-skills/engineering/cc-skills-golang.zh.md) · [EN](categories/agent-skills/engineering/cc-skills-golang.md) |
| **Waza** | 一套精简的八个「工程习惯」skill 集合（规划、设计、评审、调试、写作、调研、读取、审计），coding agent 可按需加载，覆盖 Claude Code、Codex、Cursor。 | MIT | C（5/6） | [中](categories/agent-skills/engineering/waza.zh.md) · [EN](categories/agent-skills/engineering/waza.md) |

#### agent-skills / design

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Designer Skills** | 覆盖面很广的设计实践 skill pack——9 个 plugin 下共 97 个 skill、30 个 command（研究、设计系统、UX 策略、UI、交互、原型/测试、design ops、工具箱、视觉批评），适用于 Claude Code 和 Gemini CLI。 | MIT | B（4/5） | [中](categories/agent-skills/design/ui-taste/designer-skills.zh.md) · [EN](categories/agent-skills/design/ui-taste/designer-skills.md) |
| **Skills For Design Engineers** | Emil Kowalski 的 13 个 skill：先判断界面该不该动，要动时定曲线、时长和展开位置，附会拦截的动效评审和只读全库体检。 | MIT | B（4/5） | [中](categories/agent-skills/design/ui-taste/emilkowalski-skills.zh.md) · [EN](categories/agent-skills/design/ui-taste/emilkowalski-skills.md) |
| **make-interfaces-feel-better** | 一个单一、聚焦的 agent skill，把约 16 条具体的 UI 打磨原则（同心圆角、可中断过渡、等宽数字、入场/出场动画）注入 coding agent，让界面「感觉」做完了，而不只是功能正确。 | MIT | B（4/5） | [中](categories/agent-skills/design/ui-taste/make-interfaces-feel-better.zh.md) · [EN](categories/agent-skills/design/ui-taste/make-interfaces-feel-better.md) |
| **Stitch Skills** | 一套遵循 Agent Skills 开放标准的技能库，驱动 Google 的 Stitch MCP server 生成 UI 屏幕、在代码与设计间双向转换、抽取 DESIGN.md，并导出 React/React Native/shadcn 组件。 | Apache-2.0 | B（4/5） | [中](categories/agent-skills/design/design-to-code/stitch-skills.zh.md) · [EN](categories/agent-skills/design/design-to-code/stitch-skills.md) |
| **Awesome DESIGN.md** | 当要把某个知名站点的样子变成一份可丢进项目的 DESIGN.md 时用；要自己的品牌或品味 skill、或指望 harness 自动加载时不要用。 | MIT | B（4/5） | [中](categories/agent-skills/design/design-to-code/awesome-design-md.zh.md) · [EN](categories/agent-skills/design/design-to-code/awesome-design-md.md) |
| **Taste-Skill** | 一套可移植、与框架无关的 agent skill 包，给 coding agent 注入审美，阻止千篇一律的 AI-slop 前端，转而产出有意图的布局、排版、动效与留白。 | MIT | B（4/5） | [中](categories/agent-skills/design/ui-taste/taste-skill.zh.md) · [EN](categories/agent-skills/design/ui-taste/taste-skill.md) |
| **UI UX Pro Max Skill** | 一个设计智能 skill pack，通过本地 CSV 检索引擎（风格/配色/字体/规则数据库）和交付前可访问性清单给 coding agent 注入 UI/UX 品味，可装入多种 agent harness。 | MIT | B（5/6） | [中](categories/agent-skills/design/ui-taste/ui-ux-pro-max.zh.md) · [EN](categories/agent-skills/design/ui-taste/ui-ux-pro-max.md) |
| **Hallmark** | 当 Claude Code、Cursor、Codex agent 需要有主张的反 AI 味设计 brief、审计、重设计或研究流程时用它。 | MIT | B（4/5） | [中](categories/agent-skills/design/ui-taste/hallmark.zh.md) · [EN](categories/agent-skills/design/ui-taste/hallmark.md) |
| **drawio-skill** | 一个 agent skill：把自然语言、代码、IaC 和接口 schema 变成可编辑的 `.drawio`，并能在源改动后重新同步而不丢手工版式。 | MIT | B（4/5） | [中](categories/agent-skills/design/visual-artifacts/drawio-skill.zh.md) · [EN](categories/agent-skills/design/visual-artifacts/drawio-skill.md) |
| **Interface Design** | 面向 Claude Code / Codex 产品界面的工艺优先设计工程 skill：意图先行的领域探索、逐组件的强制决策检查点、经 `.interface-design/system.md` 的跨会话记忆，外加严格的 design-review 与限定 diff 范围的 design-deslop 命令。 | MIT | C（4/5） | [中](categories/agent-skills/design/ui-taste/interface-design.zh.md) · [EN](categories/agent-skills/design/ui-taste/interface-design.md) |
| **Anti Slop** | 当 agent 做的 UI 和文案总在编造数据、评价和死链接时用它：38 条规则加一份 PASS/FAIL 交付闸门报告，只做过滤，外观留给你的 `DESIGN.md`。 | MIT | C（5/6） | [中](categories/agent-skills/design/ui-taste/anti-slop.zh.md) · [EN](categories/agent-skills/design/ui-taste/anti-slop.md) |

#### agent-skills / writing

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Baoyu Skills** | 宝玉出品的 20+ 个 coding agent 技能合集（翻译、markdown/HTML 排版、字幕与网页抓取、图片/图表/幻灯片生成），可装入 Claude Code、Codex 等支持 skill 的 harness。 | MIT | B（4/5） | [中](categories/agent-skills/ai-writing/content-production/baoyu-skills.zh.md) · [EN](categories/agent-skills/ai-writing/content-production/baoyu-skills.md) |
| **translate-book** | 面向 Codex、Claude Code 和 OpenClaw 的 agent skill：用并行 subagent 把整本书（PDF/DOCX/EPUB）翻译成任意语言。 | MIT | B（4/5） | [中](categories/agent-skills/ai-writing/translation/translate-book.zh.md) · [EN](categories/agent-skills/ai-writing/translation/translate-book.md) |
| **claude_translater** | shell 脚本＋Claude CLI 的文档翻译工具箱（PDF/DOCX/EPUB/PPTX）；translate-book 的灵感来源，但已不维护且无许可证。 | NOASSERTION | D（4/6） | [中](categories/agent-skills/ai-writing/translation/claude-translater.zh.md) · [EN](categories/agent-skills/ai-writing/translation/claude-translater.md) |
| **Humanizer-zh** | 给已有中文稿去套话和模板腔，同时保住事实、确定程度和作者立场；31 个检查点，不是检测器。 | MIT | C（4/5） | [中](categories/agent-skills/ai-writing/de-ai-writing/humanizer-zh.zh.md) · [EN](categories/agent-skills/ai-writing/de-ai-writing/humanizer-zh.md) |
| **Webnovel Writer** | 当 Claude Code 连载小说需要让章节、事实、检索、审查和摘要在长期写作中保持一致时用它。 | GPL-3.0 | C（6/6） | [中](categories/agent-skills/ai-writing/fiction/webnovel-writer.zh.md) · [EN](categories/agent-skills/ai-writing/fiction/webnovel-writer.md) |
| **chinese-novelist-skill** | 纯提示词、MIT 的中文小说流水线技能包（三层问答、大纲与人物档案、逐章创作、字数校验），无运行时、无检索层。 | MIT | B（4/5） | [中](categories/agent-skills/ai-writing/fiction/chinese-novelist-skill.zh.md) · [EN](categories/agent-skills/ai-writing/fiction/chinese-novelist-skill.md) |
| **Tech-Doc-Style-Chinese** | 面向 Claude Code 和 Codex 的中文技术写作风格 Skill——事实保真的改写与校对合同，配排版与 API 状态参考，外加可进 CI 的零依赖文案检查器。 | MIT | B（4/5） | [中](categories/agent-skills/ai-writing/content-production/tech-doc-style-chinese.zh.md) · [EN](categories/agent-skills/ai-writing/content-production/tech-doc-style-chinese.md) |

#### agent-skills / security

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Anthropic Cybersecurity Skills** | 一个大型网络安全技能包（约 817 个技能），由对齐 MITRE ATT&CK、NIST CSF、ATLAS、D3FEND、NIST AI RMF、MITRE F3 的 SKILL.md runbook 组成，按需加载进 coding agent。 | Apache-2.0 | B（4/5） | [中](categories/agent-skills/security/anthropic-cybersecurity-skills.zh.md) · [EN](categories/agent-skills/security/anthropic-cybersecurity-skills.md) |
| **reverse-skill** | 当你的 AI 编码客户端需要一个通往 45 个逆向/渗透/CTF playbook 的路由器、带授权闸门与证据链报告时用它——双用途内容会触发杀软，且要求信任第三方写的 agent 可执行指令。 | MIT | A（4/5） | [中](categories/agent-skills/security/reverse-skill.zh.md) · [EN](categories/agent-skills/security/reverse-skill.md) |
| **android-reverse-engineering** | 当你只有安卓二进制、要把它调用的 HTTP API 面写成文档时用它——Claude Code 插件，jadx/Fernflower 反编译、恢复被 R8 藏起的 Kotlin 类名、扫 Retrofit/OkHttp/Ktor/Apollo 出端点与鉴权。 | Apache-2.0 | B（4/5） | [中](categories/agent-skills/security/android-reverse-engineering.zh.md) · [EN](categories/agent-skills/security/android-reverse-engineering.md) |

#### agent-skills / context-engineering

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Agent Skills for Context Engineering** | 一个 15 个 skill 的 Claude Code 插件包，灌输上下文工程纪律：基础原理、退化、压缩、多 agent 协同、记忆、工具设计、评估与 harness 工程。 | MIT | B（5/6） | [中](categories/agent-skills/context-engineering/context-engineering-skills.zh.md) · [EN](categories/agent-skills/context-engineering/context-engineering-skills.md) |
| **NotebookLM Claude Code Skill** | 一个 Claude Code skill：用真实 Chrome 驱动查询你的 Google NotebookLM 笔记本，从你自己上传的文档取回有来源依据、带引用的答案，而非逐文件读取或凭空编造。 | MIT | D（5/6） | [中](categories/agent-skills/context-engineering/notebooklm-skill.zh.md) · [EN](categories/agent-skills/context-engineering/notebooklm-skill.md) |

#### agent-skills / prompt-engineering

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **prompt-master** | 一个 Claude skill：通过意图提取、模板路由和 37 条反模式清单，为 30+ AI 工具（LLM、编码 agent、图像/视频/语音 AI）生成一次性优化提示词。 | MIT | B（4/5） | [中](categories/agent-skills/prompt-engineering/prompt-master.zh.md) · [EN](categories/agent-skills/prompt-engineering/prompt-master.md) |
| **prompts.chat** | 可自托管的社区提示词平台：分享、发现、收集现成提示词（前身是 Awesome ChatGPT Prompts）。 | MIT（代码）+ CC0（提示词内容） | B（5/6） | [中](categories/agent-skills/prompt-engineering/prompts-chat.zh.md) · [EN](categories/agent-skills/prompt-engineering/prompts-chat.md) |
| **Prompt Engineering Guide** | 提示词/上下文工程、RAG 与 agent 技术的参考知识库（指南、论文、notebook）。 | MIT | C（4/5） | [中](categories/agent-skills/prompt-engineering/prompt-engineering-guide.zh.md) · [EN](categories/agent-skills/prompt-engineering/prompt-engineering-guide.md) |
| **Claude Code System Prompts** | 查看并对比某个 Claude Code 版本的全部内置提示词（工具说明、子 agent、skill、system reminder），每次发版从编译包里抽取，附逐版本变更日志。 | MIT | B（4/5） | [中](categories/agent-skills/prompt-engineering/claude-code-system-prompts.zh.md) · [EN](categories/agent-skills/prompt-engineering/claude-code-system-prompts.md) |
| **MuseAI-Skills** | Meta Muse 的 68 个 agent skill 及权限清单、评测场景、运行脚本的非官方无授权快照——用来研究生产级连接器与征询设计；什么都装不上、跑不起来。 | 无（无 LICENSE 文件；README 不授予对所存档 Meta Muse 文件的任何权利） | D（4/5） | [中](categories/agent-skills/prompt-engineering/museai-skills.zh.md) · [EN](categories/agent-skills/prompt-engineering/museai-skills.md) |

#### agent-skills / vendor-collections

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Anthropic Skills** | Anthropic 官方公开的 Agent Skills 合集——自包含的 SKILL.md 目录（文档编辑、设计、MCP 与 skill 编写、沟通），可装进 Claude Code、Claude.ai 或 Claude API。 | Apache-2.0 | A（3/5） | [中](categories/agent-skills/vendor-collections/agent-vendors/anthropic-skills.zh.md) · [EN](categories/agent-skills/vendor-collections/agent-vendors/anthropic-skills.md) |
| **Agent Plugins for AWS** | AWS Labs 官方出品的九个 agent 插件集合（serverless、Amplify、SageMaker、迁移、数据库、部署/成本估算等），通过 marketplace 安装、触发短语驱动并接好 AWS MCP server，教 Claude Code / Cursor / Codex 在 AWS 上做架构、部署和运维。 | Apache-2.0 | B（5/6） | [中](categories/agent-skills/vendor-collections/product-vendors/aws-agent-plugins.zh.md) · [EN](categories/agent-skills/vendor-collections/product-vendors/aws-agent-plugins.md) |
| **Claude Plugins (Official)** | Anthropic 官方的 Claude Code 插件市场：精选的可安装插件目录（命令、agent、skill、MCP server），通过原生 /plugin 系统按名安装。 | Apache-2.0 | A（4/5） | [中](categories/agent-skills/vendor-collections/agent-vendors/claude-plugins-official.zh.md) · [EN](categories/agent-skills/vendor-collections/agent-vendors/claude-plugins-official.md) |
| **Cursor Plugins** | Cursor 官方插件市场仓库：`/add-plugin <名字>` 把 skill、规则、子 agent、hook 和 MCP 配置装进 Cursor——16 个第一方插件（主打 poteto 的严谨工程工作流 pstack），外加 80 个连到厂商托管 MCP server 的薄连接器。 | MIT | B（3/5） | [中](categories/agent-skills/vendor-collections/agent-vendors/cursor-plugins.zh.md) · [EN](categories/agent-skills/vendor-collections/agent-vendors/cursor-plugins.md) |
| **MiniMax Skills** | 当你想在 Claude Code、Cursor、Codex 或 OpenCode 里装一套厂商写的 skill，覆盖前端、移动端、shader 开发以及 MiniMax 的文档、音乐、视觉生成时用它——但它仍标 Beta，2026-04-18 之后再没推送。 | MIT | B（4/5） | [中](categories/agent-skills/vendor-collections/agent-vendors/minimax-skills.zh.md) · [EN](categories/agent-skills/vendor-collections/agent-vendors/minimax-skills.md) |
| **Anthropic Knowledge Work Plugins** | 当你想要 Anthropic 官方面向知识工作（文档、沟通、研究）的开源插件集（用于 Claude）时用它——非常年轻。 | Apache-2.0 | A（4/5） | [中](categories/agent-skills/vendor-collections/agent-vendors/knowledge-work-plugins.zh.md) · [EN](categories/agent-skills/vendor-collections/agent-vendors/knowledge-work-plugins.md) |
| **Remotion Agent Skills** | Remotion 官方的 12 个 skill 捆绑包：教编码 agent（Claude Code、Codex、Cursor、Kimi Code）写出正确的 Remotion React 视频代码——经 `npx skills add remotion-dev/skills` 安装，版本与框架同步锁定。 | Not declared | C（4/5） | [中](categories/agent-skills/vendor-collections/product-vendors/remotion-skills.zh.md) · [EN](categories/agent-skills/vendor-collections/product-vendors/remotion-skills.md) |
| **HumanLayer Skills** | HumanLayer 官方的六个 skill——把改动画清楚（`show-me`）、PR 说明结构化（`visual-pr`）、重写 CLAUDE.md、收紧 React props，外加两个把重复性 agent 任务做成定时 GitHub Actions 循环的 skill，循环带 agent memory 文件与 `/iterate` 评论通道。 | MIT | B（4/5） | [中](categories/agent-skills/vendor-collections/agent-vendors/humanlayer-skills.zh.md) · [EN](categories/agent-skills/vendor-collections/agent-vendors/humanlayer-skills.md) |
| **Android Skills** | Google 官方 24 个 skill 包，覆盖模型仍会失手的 Android 活（edge-to-edge、R8、Navigation 3、Play 政策）——用 Android CLI 安装，不是 `npx skills add`。 | Apache-2.0 | B（5/6） | [中](categories/agent-skills/vendor-collections/product-vendors/android-skills.zh.md) · [EN](categories/agent-skills/vendor-collections/product-vendors/android-skills.md) |
| **Modern Web Guidance** | Google Chrome 官方的“先搜再取”skill：写 HTML/CSS/客户端 JS 前，agent 用本地搜索的 npm CLI 取回一篇经评测打分的现代平台指南（原生 API、Baseline 支持、适度降级）。 | Apache-2.0 | B（5/6） | [中](categories/agent-skills/vendor-collections/product-vendors/modern-web-guidance.zh.md) · [EN](categories/agent-skills/vendor-collections/product-vendors/modern-web-guidance.md) |
| **Agent Toolkit for AWS** | 当你的编码 agent 在真实 AWS 账号里干活、你既要 AWS 当前的剧本、又要 IAM 和 CloudTrail 能把 agent 的调用和你的分开时用：约 114 个 skill 加一个托管 MCP 端点；只管 AWS，托管那一半能看到你的流量。 | Apache-2.0 | A（4/5） | [中](categories/agent-skills/vendor-collections/product-vendors/agent-toolkit-for-aws.zh.md) · [EN](categories/agent-skills/vendor-collections/product-vendors/agent-toolkit-for-aws.md) |
| **Cloudflare Skills** | 当你的编码 agent 在 Cloudflare 上搭东西、总凭过时记忆写时用：16 个官方 skill，帮它选对 Cloudflare 产品并先读当前文档，外加一条托管 MCP 配置；只管 Cloudflare，无 tag，多数是指针，需要联网。 | Apache-2.0 | A（4/5） | [中](categories/agent-skills/vendor-collections/product-vendors/cloudflare-skills.zh.md) · [EN](categories/agent-skills/vendor-collections/product-vendors/cloudflare-skills.md) |
| **Bright Data Skills** | 当你的 agent 总撞上 403 和验证页、而你已决定花钱让 Bright Data 来过这一关时用：21 个厂商 skill，把每次抓取分给合适的付费产品并检查封锁页；每次调用都计费，有一个 skill 要 agent 停用内置上网工具，没有 tag，README 的 Quick Start 指向已删除的脚本。 | MIT | C（4/5） | [中](categories/agent-skills/vendor-collections/product-vendors/brightdata-skills.zh.md) · [EN](categories/agent-skills/vendor-collections/product-vendors/brightdata-skills.md) |

#### agent-skills / subagent-collections

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Agency-Agents** | 约 232 个专业 subagent 人格的精选集合（markdown），覆盖 16 个职能部门，附 install/convert 脚本，可部署到 Claude Code 及另外约 11 个 agent harness。 | MIT | A（4/5） | [中](categories/agent-skills/subagent-collections/agency-agents.zh.md) · [EN](categories/agent-skills/subagent-collections/agency-agents.md) |
| **awesome-claude-code-subagents** | 一套精选的 100+ 个 Claude Code subagent 定义合集（每个角色一个 markdown persona），丢进 ~/.claude/agents/ 后 Claude Code 就能把活委派给对应领域专家。 | MIT | A（4/5） | [中](categories/agent-skills/subagent-collections/awesome-claude-code-subagents.zh.md) · [EN](categories/agent-skills/subagent-collections/awesome-claude-code-subagents.md) |
| **wshobson/agents** | 单人维护的大型多 harness 插件市场（约 194 个 subagent、158 个 skill、106 个 command、16 个 orchestrator），用一份 Markdown 源生成各 harness 原生产物，覆盖 Claude Code、Codex CLI、Cursor、OpenCode、Gemini CLI 与 Copilot。 | MIT | B（4/5） | [中](categories/agent-skills/subagent-collections/wshobson-agents.zh.md) · [EN](categories/agent-skills/subagent-collections/wshobson-agents.md) |
| **Council of High Intelligence** | 一个 Claude Code / Codex / Gemini CLI / OpenCode 技能包：把 18 个固定的「思想家」人设拉进一套剧本化多轮审议——盲评、匿名交叉质询、按置信度加权计票，最终由一位不参与辩论的 chairman 写出裁决。 | MIT | B（5/6） | [中](categories/agent-skills/subagent-collections/council-of-high-intelligence.zh.md) · [EN](categories/agent-skills/subagent-collections/council-of-high-intelligence.md) |

#### agent-skills / personal-collections

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **agent-scripts** | 一位维护者用来在 Codex 与 Claude Code 之间共享一份 `AGENTS.MD` 和约 70 个 skill 的权威仓库，靠软链同步脚本分发；更像参考布局而非可移植的 skill 包（不少 skill 默认作者自己的机器）。 | MIT | B（4/5） | [中](categories/agent-skills/personal-collections/engineering-workflows/agent-scripts.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/agent-scripts.md) |
| **antfu/skills** | Anthony Fu 个人精选、面向 Vue/Vite/Nuxt 栈的 agent skill 集合（其 ESLint/pnpm/Vitest/UnoCSS 偏好 + 生成与 vendored 的框架 skill），通过 skills CLI 安装。 | MIT | B（4/5） | [中](categories/agent-skills/personal-collections/engineering-workflows/antfu-skills.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/antfu-skills.md) |
| **claude-code-harness** | 一套个人化的 Claude Code harness：以插件形式装入受治理的 plan → work → review → release 循环（spec 优先契约、TDD 门控执行、独立 review），并附带 Go 原生 doctor CLI 诊断插件缓存与 skill 漂移。 | MIT | B（5/6） | [中](categories/agent-skills/personal-collections/engineering-workflows/claude-code-harness.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/claude-code-harness.md) |
| **dbskill** | 一套个人精选的中文 agent 技能包（约 21 个 /dbs-* 命令），聚焦商业模式诊断、内容创作与个人决策，可安装进 Claude Code 等 harness。 | CC-BY-NC-4.0 | C（4/6） | [中](categories/agent-skills/personal-collections/knowledge-content/dbskill.zh.md) · [EN](categories/agent-skills/personal-collections/knowledge-content/dbskill.md) |
| **Dimillian Skills** | 当你用 OpenAI Codex 做 iOS／macOS 开发、想要现成的 SwiftUI、Swift 并发、模拟器调试和 App Store 发布类 skill 时用它——但它是单作者、只面向 Codex 的快照，2026-03 之后没再更新，而它跟的 Apple beta 变得很快。 | MIT | C（4/5） | [中](categories/agent-skills/personal-collections/engineering-workflows/dimillian-skills.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/dimillian-skills.md) |
| **gstack** | Garry Tan 的私人 Claude Code harness：54 个 skill——约一半是角色人设（CEO 复盘、工程经理、设计师、QA、安全官、发布工程师），另一半是工具命令——外加一个 agent 真正驱动的浏览器，串成一条「规划 → 构建 → 评审 → 发布 → 复盘」冲刺流程。 | MIT | B（4/5） | [中](categories/agent-skills/personal-collections/engineering-workflows/gstack.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/gstack.md) |
| **andrej-karpathy-skills** | 当你的 Claude Code 或 Cursor agent 爱过度设计、顺手改无关文件、没验证就说完成，而你想用一份约 65 行的 `CLAUDE.md` 基础层压住这些毛病时用它——但它只是建议性文字，且是第三方提炼，并非 Karpathy 本人所写。 | MIT | C（3/5） | [中](categories/agent-skills/personal-collections/engineering-workflows/karpathy-skills.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/karpathy-skills.md) |
| **Khazix Skills** | 数字生命卡兹克（Khazix）的个人精选合集，含五个 SKILL.md 标准格式、以中文为主的 Agent Skill：磁盘清理、AI 资讯查询、文档/记忆同步、长文研究报告、公众号风格写作。 | MIT | B（4/5） | [中](categories/agent-skills/personal-collections/knowledge-content/khazix-skills.zh.md) · [EN](categories/agent-skills/personal-collections/knowledge-content/khazix-skills.md) |
| **ljg-skills** | 李继刚的个人 Claude Code 技能合集（20+ 个 skill），面向中文知识工作——读论文/拆书、概念分析、大白话改写、把内容渲染成 PNG 卡片，通过 skills CLI 安装。 | NOASSERTION | B（4/5） | [中](categories/agent-skills/personal-collections/knowledge-content/ljg-skills.zh.md) · [EN](categories/agent-skills/personal-collections/knowledge-content/ljg-skills.md) |
| **PUA** | 一个高能动性人设 skill 包：把 coding agent 设定成「被放进 30 天 PIP 的 P8 工程师」，用职场 PUA/PIP 话术逼它穷尽排查手段而非早早放弃。 | MIT | C（4/6） | [中](categories/agent-skills/personal-collections/engineering-workflows/pua.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/pua.md) |
| **Qiushi-Skill** | 一套方法论 skill 包，用「实事求是」加九个唯物辩证法思维工具（矛盾分析、调查研究、实践认识论等）武装编程 agent，并通过 npx 安装器跨 Claude Code/Cursor/Codex/OpenCode 落地。 | MIT | B（4/6） | [中](categories/agent-skills/personal-collections/engineering-workflows/qiushi-skill.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/qiushi-skill.md) |
| **shaping-skills** | Ryan Singer 的个人 Claude Code 技能包，把 Shape Up 的「shaping」流程（框定问题、breadboarding、产出 framing/kickoff 文档）带进 coding agent，让 AI 在写代码前先帮你想清楚「要做什么」。 | NOASSERTION | E（4/5） | [中](categories/agent-skills/personal-collections/engineering-workflows/shaping-skills.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/shaping-skills.md) |
| **TÂCHES CC Resources** | 当你常驻 Claude Code、总在手搓新的 slash 命令、subagent、hook 或 MCP server，想要一套元生成 skill 加审计 subagent 来规整这件事时用它——但它是单维护者、只认 Claude Code 的快照，2026-04 之后没再更新。 | MIT | C（4/5） | [中](categories/agent-skills/personal-collections/engineering-workflows/taches-cc-resources.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/taches-cc-resources.md) |
| **skills** | Sahil Lavingia 的 Claude Code skill 包，把《The Minimalist Entrepreneur》旅程变成 10 个商业构建命令。 | NOASSERTION | C（4/5） | [中](categories/agent-skills/personal-collections/knowledge-content/slavingia-skills.zh.md) · [EN](categories/agent-skills/personal-collections/knowledge-content/slavingia-skills.md) |
| **canghe-skills** | 苍何个人 Claude Code skills marketplace：覆盖内容发布、图像/视频生成后端、商业情报、提取工具、Obsidian helper、Remotion 指南和文档解析。 | NOASSERTION | D（4/5） | [中](categories/agent-skills/personal-collections/knowledge-content/canghe-skills.zh.md) · [EN](categories/agent-skills/personal-collections/knowledge-content/canghe-skills.md) |
| **patent-disclosure-skill** | 中文优先的八技能 Agent 包：挖掘专利点并撰写发明／实用新型／外观交底书，改写成申请文件，检索国知局记录，把专利解读进 Obsidian 库，并出审查政策简报。 | MIT | B（4/5） | [中](categories/agent-skills/personal-collections/knowledge-content/patent-disclosure-skill.zh.md) · [EN](categories/agent-skills/personal-collections/knowledge-content/patent-disclosure-skill.md) |
| **huashu-skills** | 花叔的内容创作 Skills 合集 - AI审校、选题生成、视频大纲、素材搜索等 11 个实用技能 | NOASSERTION | B（4/5） | [中](categories/agent-skills/ai-writing/content-production/huashu-skills.zh.md) · [EN](categories/agent-skills/ai-writing/content-production/huashu-skills.md) |
| **De-AI-Prompt-Enhancer-Writer-Booster-SKILL** | 中文去 AI 味提示词套件，打包为两个 SKILL 格式文件夹：`de-AI-writing/SKILL.md` 用于清理 AI 腔，`good-writing/SKILL.md` 用于更强的作者风格复现。 | NOASSERTION | C（4/5） | [中](categories/agent-skills/ai-writing/de-ai-writing/de-ai-prompt-enhancer-writer-booster-skill.zh.md) · [EN](categories/agent-skills/ai-writing/de-ai-writing/de-ai-prompt-enhancer-writer-booster-skill.md) |
| **chatgpt-comparison-detection** | Human ChatGPT Comparison Corpus (HC3), Detectors, and more! 🔥 | NOASSERTION | E（4/6） | [中](categories/llm-eval/chatgpt-comparison-detection.zh.md) · [EN](categories/llm-eval/chatgpt-comparison-detection.md) |
| **writing-agent** | 🚀 一个基于 Claude Code (Skills + Subagents) 的“去AI味”全栈写作系统。不仅防套路，更通过专属规则强制注入人类观点与细节，搭配读者测试评估与自动图文排版。全面支持 DeepSeek / 智谱GLM / MiniMax 等国产低成本大模型，提供从选题、风格建模到审稿发布的高维全自动写作工作流。 | MIT | B（5/6） | [中](categories/agent-skills/ai-writing/content-production/writing-agent.zh.md) · [EN](categories/agent-skills/ai-writing/content-production/writing-agent.md) |
| **nuwa-skill** | 你想蒸馏的下一个员工，何必是同事。蒸馏任何人的思维方式——心智模型、决策启发式、表达DNA。Distill how anyone thinks. | MIT | B（4/5） | [中](categories/agent-skills/context-engineering/nuwa-skill.zh.md) · [EN](categories/agent-skills/context-engineering/nuwa-skill.md) |
| **shuorenhua** | 说人话｜中文优先的去 AI 味改写 skill：保事实、分场景、改完可直接发。Chinese-first rewrite skill for Codex / Claude Code / Cursor / ChatGPT — removes AI tone, preserves facts. | MIT | C（5/6） | [中](categories/agent-skills/ai-writing/de-ai-writing/shuorenhua.zh.md) · [EN](categories/agent-skills/ai-writing/de-ai-writing/shuorenhua.md) |
| **ai-flavor-remover** | 一个用于去除“AI 味”的中文单文件 prompt 片段；上游 README 明确说只在 Gemini 2.5 Pro 上测试过。 | NOASSERTION | D（4/6） | [中](categories/agent-skills/ai-writing/de-ai-writing/ai-flavor-remover.zh.md) · [EN](categories/agent-skills/ai-writing/de-ai-writing/ai-flavor-remover.md) |
| **stop-slop** | 用于移除英文 prose 中 AI 痕迹的 skill 文件。 | MIT | B（4/5） | [中](categories/agent-skills/ai-writing/de-ai-writing/stop-slop.zh.md) · [EN](categories/agent-skills/ai-writing/de-ai-writing/stop-slop.md) |
| **humanizer** | 移除英文文本中 AI 写作痕迹的 Claude Code skill。 | MIT | B（5/6） | [中](categories/agent-skills/ai-writing/de-ai-writing/humanizer.zh.md) · [EN](categories/agent-skills/ai-writing/de-ai-writing/humanizer.md) |
| **avoid-ai-writing** | 可移植的去 AI 味写作 skill：自带确定性 npm 检测器、按命中数卡的 CI / pre-commit 门禁，以及一份公开自身误报率的人控语料测量。 | MIT | B（5/6） | [中](categories/agent-skills/ai-writing/de-ai-writing/avoid-ai-writing.zh.md) · [EN](categories/agent-skills/ai-writing/de-ai-writing/avoid-ai-writing.md) |
| **no-ai-slop** | 英文编辑 skill：第一条规则就是保留作者本人的声音——按 20 多种具名 AI 模式做最小有效修改，带 eval.md 自检闭环，detect 模式只引用证据、不猜作者身份。 | MIT | C（5/6） | [中](categories/agent-skills/ai-writing/de-ai-writing/no-ai-slop.zh.md) · [EN](categories/agent-skills/ai-writing/de-ai-writing/no-ai-slop.md) |
| **asd-ste100-skill** | 按 ASD-STE100 受控语言规则改写给 agent 读的英文（工具说明、报错、提示词）的 Claude Code skill：一句一指令、限长、保留确定程度，附可进 CI 的标准库正则 linter。 | MIT | B（4/5） | [中](categories/agent-skills/ai-writing/de-ai-writing/asd-ste100-skill.zh.md) · [EN](categories/agent-skills/ai-writing/de-ai-writing/asd-ste100-skill.md) |
| **lieflat-less-ai-tone** | 中文白名单式去 AI 味 skill：11 条改写规则各附人类与模型的频率倍率，外加一张硬性的“不作为改写理由”表，没命中的句子逐字保留；283 万字语料本身没有公开。 | MIT | C（3/5） | [中](categories/agent-skills/ai-writing/de-ai-writing/lieflat-less-ai-tone.zh.md) · [EN](categories/agent-skills/ai-writing/de-ai-writing/lieflat-less-ai-tone.md) |
| **cangjie-skill** | 把书、长视频、播客、课程、访谈和转写稿蒸馏成可复用、可测试 agent skill pack 的方法论 skill。 | MIT | C（5/6） | [中](categories/agent-skills/context-engineering/cangjie-skill.zh.md) · [EN](categories/agent-skills/context-engineering/cangjie-skill.md) |
| **archify** | Any agent Skill: generate beautiful architecture diagrams with dark/light theme toggle and PNG/JPEG/WebP/SVG export | MIT | B（4/6） | [中](categories/agent-skills/design/visual-artifacts/archify.zh.md) · [EN](categories/agent-skills/design/visual-artifacts/archify.md) |
| **mattpocock/skills** | Matt Pocock 的工程 skill 包，面向 Claude Code 和 skills.sh，覆盖 grilling、domain docs、TDD、bug 诊断、架构、review、tickets 和实现流程。 | MIT | B（4/5） | [中](categories/agent-skills/engineering/mattpocock-skills.zh.md) · [EN](categories/agent-skills/engineering/mattpocock-skills.md) |
| **BrowserAct Skills** | 面向 BrowserAct 的 agent 浏览器自动化技能包：索引式浏览器控制、stealth/private session、远程人工接管，以及 Skill Forge 抓取工作流。 | MIT | B（4/5） | [中](categories/agent-skills/engineering/browser-act-skills.zh.md) · [EN](categories/agent-skills/engineering/browser-act-skills.md) |
| **caveman** | 简短表达技能加可选本地代理：压缩 coding agent 说出来的话，wrap 之后也压缩它读进去的东西，代码、命令和报错原样保留。 | NOASSERTION (MIT + BSL-1.1) | D（6/6） | [中](categories/agent-skills/engineering/caveman.zh.md) · [EN](categories/agent-skills/engineering/caveman.md) |
| **i-have-adhd** | 一份 10 条规则的回复风格技能：让 coding agent 每轮先说动作、把步骤编号、复述进度，并删掉铺垫与收尾；一套规则覆盖约 15 种 agent harness。 | MIT | A（4/5） | [中](categories/agent-skills/engineering/i-have-adhd.zh.md) · [EN](categories/agent-skills/engineering/i-have-adhd.md) |
| **Ponytail** | 常驻的「最懒资深工程师」规则集：coding agent 写码前先走七级 YAGNI 阶梯，只交回能跑的最短 diff；带生命周期 hook、六个 skill 和约 20 种 harness 适配。 | MIT | B（5/6） | [中](categories/agent-skills/engineering/ponytail.zh.md) · [EN](categories/agent-skills/engineering/ponytail.md) |
| **open-seo** | Open source alternative to Semrush and Ahrefs | MIT | B（5/6） | [中](categories/agent-skills/ai-writing/marketing-seo/open-seo.zh.md) · [EN](categories/agent-skills/ai-writing/marketing-seo/open-seo.md) |
| **ai-website-cloner-template** | Clone any website with one command using AI coding agents | MIT | B（4/5） | [中](categories/agent-skills/design/design-to-code/ai-website-cloner-template.zh.md) · [EN](categories/agent-skills/design/design-to-code/ai-website-cloner-template.md) |
| **huashu-design** | Huashu Design · HTML-native design skill for Claude Code · Claude Code 里 HTML 原生的设计 skill · 高保真原型 / 幻灯片 / 动画 + 20 设计哲学 + 5 维评审 + MP4 导出 · Agent-agnostic | MIT | B（5/6） | [中](categories/agent-skills/design/visual-artifacts/huashu-design.zh.md) · [EN](categories/agent-skills/design/visual-artifacts/huashu-design.md) |
| **ppt-master** | AI generates a real, editable PowerPoint from any document — native shapes & animations, editable charts & tables you can change the data on, speaker notes voiced as audio narration, and the option to follow your own .pptx template, not slide images · by Hugo He | MIT | B（5/6） | [中](categories/agent-skills/slides-ppt/ppt-master.zh.md) · [EN](categories/agent-skills/slides-ppt/ppt-master.md) |
| **frontend-slides** | 用 coding agent 的前端能力创建网页演示文稿。 | MIT | B（4/5） | [中](categories/agent-skills/slides-ppt/frontend-slides.zh.md) · [EN](categories/agent-skills/slides-ppt/frontend-slides.md) |
| **html-ppt-skill** | HTML PPT Studio——AgentSkill，内置 36 个主题、15 个 full-deck templates、31 个布局、47 个动画和 presenter mode，用于构建专业静态 HTML 演示文稿。 | MIT | C（4/5） | [中](categories/agent-skills/slides-ppt/html-ppt-skill.zh.md) · [EN](categories/agent-skills/slides-ppt/html-ppt-skill.md) |
| **tacit-mining** | Let AI truly understand you. A Claude Code skill that extracts tacit knowledge through structured dialogue. 隐性知识挖掘技能。 | NOASSERTION | D（4/5） | [中](categories/agent-skills/context-engineering/tacit-mining.zh.md) · [EN](categories/agent-skills/context-engineering/tacit-mining.md) |
| **soul.md** | The best way to build a personality for your agent. Let Claude Code / OpenClaw ingest your data & build your AI soul. | MIT | B（4/5） | [中](categories/agent-skills/context-engineering/soul-md.zh.md) · [EN](categories/agent-skills/context-engineering/soul-md.md) |
| **marketingskills** | Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering. | MIT | B（4/5） | [中](categories/agent-skills/ai-writing/marketing-seo/marketingskills.zh.md) · [EN](categories/agent-skills/ai-writing/marketing-seo/marketingskills.md) |
| **AI Copywriter** | 单文件 Markdown 技能：先问清读者和真实故事，再写标题、微文案、邮件主题行和 LinkedIn 帖子，并逐句对照 33 种 AI 写作痕迹审查。 | MIT | C（3/5） | [中](categories/agent-skills/ai-writing/marketing-seo/ai-copywriter.zh.md) · [EN](categories/agent-skills/ai-writing/marketing-seo/ai-copywriter.md) |
| **OPC Skills** | 一人公司的十个上线杂活技能——SEO／AI 搜索体检并给出可粘贴的 schema，外加域名、logo、需求调研和 Reddit／X 查询，用你自己的 API 密钥运行。 | Apache-2.0 | B（4/5） | [中](categories/agent-skills/ai-writing/marketing-seo/opc-skills.zh.md) · [EN](categories/agent-skills/ai-writing/marketing-seo/opc-skills.md) |

### observability

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Grafana** | 当你需要在 Prometheus/Loki/Elasticsearch 等多数据源之上加一层统一看板和告警时用它——它做可视化，不做存储。 | AGPL-3.0 | B（5/6） | [中](categories/observability/grafana.zh.md) · [EN](categories/observability/grafana.md) |
| **Prometheus** | 当你要在 Kubernetes 或已暴露 /metrics 的云原生软件上拿到每个服务的请求率、错误率、延迟直方图，并用 PromQL 设告警时用它——但本地存储是单节点的，长期保留或高可用要加 Thanos、Mimir 或 VictoriaMetrics。 | Apache-2.0 | A（6/6） | [EN](categories/observability/prometheus.md) · [中](categories/observability/prometheus.zh.md) |
| **OpenTelemetry Collector** | 当多个服务要把链路、指标、日志发往不止一个后端，并希望采样、脱敏、路由都在一份 YAML 里集中配置、而不是写进每个服务时用它——但只有一个服务、一个 OTLP 后端时，它只是多一个进程。 | Apache-2.0 | A（6/6） | [EN](categories/observability/opentelemetry-collector.md) · [中](categories/observability/opentelemetry-collector.zh.md) |
| **Loki** | 当你的 Prometheus + Grafana 体系里，日志账单主要花在没人查的全文索引上，而按应用、命名空间、Pod 这类标签圈定范围的查询就够用时用它——但跨几周的全文检索要扫遍每个块，而且它是 AGPL-3.0。 | AGPL-3.0 | B（6/6） | [EN](categories/observability/loki.md) · [中](categories/observability/loki.zh.md) |
| **Jaeger** | 当一个慢请求穿过几十个服务，你想要一个自托管、原生支持 OpenTelemetry、自带界面、由 CNCF 治理的链路追踪后端时用它——但存储数据库得你自己运维，而且 v1 二进制和 jaeger-client 库都已停止维护。 | Apache-2.0 | A（6/6） | [EN](categories/observability/jaeger.md) · [中](categories/observability/jaeger.zh.md) |

### data-visualization

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Apache Superset** | 当你想要在数据仓库之上自托管 SQL BI 看板与探索时用它——不是基础设施指标/可观测性。 | Apache-2.0 | A（6/6） | [中](categories/data-visualization/superset.zh.md) · [EN](categories/data-visualization/superset.md) |
| **Evidence** | 当分析工程师想把报表写成 git 里的 Markdown 加 SQL 文件，能 diff、能评审、能交给编码 agent 改时用它——但业务人员没法点选出问题，自托管只有 Basic Auth，而且 2026 年的重写让代码库从头来过。 | MIT | B（6/6） | [EN](categories/data-visualization/evidence.md) · [中](categories/data-visualization/evidence.zh.md) |
| **Metabase** | 当不会 SQL 的同事总把简单的数据问题排进你的队列，你想当天就起一个自托管应用、让他们自己点选表、加过滤、存进共享看板时用它——但 SSO、行级权限和 Git 同步都要付费，核心还是 AGPL。 | NOASSERTION (AGPL-3.0 core + Metabase Commercial License on enterprise/) | A（4/6） | [EN](categories/data-visualization/metabase.md) · [中](categories/data-visualization/metabase.zh.md) |

### ocr

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Tesseract** | 当你需要离线、可嵌入、覆盖 100+ 语言、面向清晰印刷文本的 OCR 时用它——不适合野外照片或手写。 | Apache-2.0 | A（6/6） | [中](categories/ocr/tesseract.zh.md) · [EN](categories/ocr/tesseract.md) |
| **LaTeX-OCR (pix2tex)** | 当你要在本地把裁好的印刷体数学公式图片转成 LaTeX（截图 GUI、CLI 或 Python 调用）时用它——但它只认公式、每个输出都要人工核对，且单作者仓库自 2025-01 起没有提交。 | MIT | C（4/6） | [中](categories/ocr/latex-ocr.zh.md) · [EN](categories/ocr/latex-ocr.md) |
| **Laravel OCR** | 当 Laravel 应用需要统一接入本地与云 OCR，并用模板抽取字段时用它——PDF／版面处理较浅，仓库也缺少许可证文件。 | NOASSERTION | D（5/6） | [中](categories/ocr/laravel-ocr.zh.md) · [EN](categories/ocr/laravel-ocr.md) |
| **PaddleOCR** | 当杂乱输入需要现代 detection+recognition、中日韩强项或表格／版式结构，而你能背负 PaddleX、推理引擎与模型下载时用它。 | Apache-2.0 | A（6/6） | [中](categories/ocr/paddleocr.zh.md) · [EN](categories/ocr/paddleocr.md) |
| **EasyOCR** | 当 PyTorch OCR 栈加不错的场景文字默认效果比自己搭预处理更省事时用它——项目最近一次实质发版是 2024-09。 | Apache-2.0 | B（5/6） | [中](categories/ocr/easyocr.zh.md) · [EN](categories/ocr/easyocr.md) |

### document-parsing

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Docling** | 当你需要把杂乱的 PDF/DOCX/PPTX 解析成干净的结构化 Markdown/JSON 以喂给 RAG 时用它——是解析器，不是文档管理系统。 | MIT | A（5/6） | [中](categories/document-parsing/docling.zh.md) · [EN](categories/document-parsing/docling.md) |
| **MarkItDown** | 当 agent 或 RAG 流水线要用一次轻量 Python 调用，把混杂的 Office 文件、HTML、EPUB 和简单 PDF 统一转成 Markdown 时用它——但扫描件或复杂版面 PDF 要用 Marker 或 Docling，它没有 OCR 和版面模型。 | MIT | B（6/6） | [中](categories/document-parsing/markitdown.zh.md) · [EN](categories/document-parsing/markitdown.md) |
| **olmOCR** | 当你要把成千上万份带公式、表格、多栏版面的 PDF 按阅读顺序转成干净 Markdown、拿去做 LLM 语料时用它——但本地运行要 12 GB 以上显存的 NVIDIA GPU，且上游自 2026-03 起已无提交。 | Apache-2.0 | C（5/6） | [中](categories/document-parsing/olmocr.zh.md) · [EN](categories/document-parsing/olmocr.md) |
| **Marker** | 当你要在自己的机器上把几千份 PDF（论文、教材、扫描件）转成带真表格、LaTeX 公式、按需 OCR 的 Markdown 时用它——但模型权重只对融资或营收低于 500 万美元的主体免费。 | Apache-2.0 | B（6/6） | [EN](categories/document-parsing/marker.md) · [中](categories/document-parsing/marker.zh.md) |
| **unstructured** | 当 RAG 流水线面对混杂的 PDF、邮件和 Office 文件，需要带页码元数据的类型化元素和按章节分块，而不只是一个 Markdown 字符串时用它——但开源版的 PDF 表格准确率不如 Docling 和 Marker，且默认开启统计回传。 | Apache-2.0 | A（6/6） | [EN](categories/document-parsing/unstructured.md) · [中](categories/document-parsing/unstructured.zh.md) |
| **any2html** | Use it when you need any2html in the document-parsing area. | NOASSERTION | D（5/6） | [中](categories/document-parsing/any2html.zh.md) · [EN](categories/document-parsing/any2html.md) |
| **Dedoc** | 当混合 PDF 与 Office 归档必须转成带表格和附件的逻辑树时用它——本地解析面广，但 Linux 与系统包依赖很重。 | Apache-2.0 | B（5/6） | [中](categories/document-parsing/dedoc.zh.md) · [EN](categories/document-parsing/dedoc.md) |
| **Bella Domify** | 当 Python RAG 管线需要细粒度 PDF／Office DOM tree 和可选视觉 OCR 时用它——许可证冲突与 provider／基础设施耦合会抬高采用成本。 | GPL-2.0-only | C（5/6） | [中](categories/document-parsing/bella-domify.zh.md) · [EN](categories/document-parsing/bella-domify.md) |
| **MinerU Skill** | 当 agent 需要一条命令完成云端文档转 Markdown、批处理、续跑和投递时用它——文件会离开本地，质量取决于 MinerU。 | MIT | C（5/6） | [中](categories/document-parsing/mineru-skill.zh.md) · [EN](categories/document-parsing/mineru-skill.md) |
| **anydoc** | 当管线收到一堆混杂的 Office（含老 .doc/.ppt/.xls）、OpenDocument、RTF、EPUB 和文字版 PDF，需要毫秒级转成风格一致的 Markdown、又不想装 LibreOffice 或模型时用它；不做 OCR，扫描页会直接失败。 | MIT | B（6/6） | [中](categories/document-parsing/anydoc.zh.md) · [EN](categories/document-parsing/anydoc.md) |

### office-automation

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **OfficeCLI** | 当 agent 必须在一台没有 Python 也没有 Office 的机器上读写、创建全部三个 Office 格式，并且需要**看见**渲染结果时用它——但它只有 6 个月、98% 单人作者、没有公开测试套件，且默认开启自动更新并会改写你的 agent skill 目录。 | Apache-2.0 | B（6/6） | [中](categories/office-automation/officecli.zh.md) · [EN](categories/office-automation/officecli.md) |
| **python-docx** | 当 Python 服务需要就地创建或编辑 Word `.docx`、且要一个能锁版本、已存活 13 年的 MIT 依赖时用它——但没有渲染能力，且脚注／尾注自 2014 年起一直未实现。 | MIT | B（5/6） | [中](categories/office-automation/python-docx.zh.md) · [EN](categories/office-automation/python-docx.md) |
| **python-pptx** | 当你必须用 Python 生成或编辑原生 `.pptx`、且交付物要能在 PowerPoint 里打开时用它——但它自 2024-08-07 起未再发版，动画（2017）和 SmartArt（2014）从未实现。 | MIT | C（4/6） | [中](categories/office-automation/python-pptx.zh.md) · [EN](categories/office-automation/python-pptx.md) |
| **XlsxWriter** | 当 Python 服务从数据生成新的 `.xlsx`、且你要零依赖加 13 年稳定性时用它——但它只写，无法打开已有工作簿，也不计算公式。 | BSD-2-Clause | B（6/6） | [中](categories/office-automation/xlsxwriter.zh.md) · [EN](categories/office-automation/xlsxwriter.md) |
| **Office-Word-MCP-Server** | 只有当既有 LLM 集成已经绑定它那约 55 个 Word tool schema 时才用它——仓库已于 2025-12-31 归档，作者批量归档了约 15 个 MCP server；新工作请用 OfficeCLI，或自己封装 python-docx。 | MIT | C（6/6） | [中](categories/office-automation/office-word-mcp-server.zh.md) · [EN](categories/office-automation/office-word-mcp-server.md) |
| **Office-PowerPoint-MCP-Server** | 只有当既有 LLM 集成已经绑定它的 PowerPoint tool schema 时才用它——同一作者在 2026-03-03 与 Word 姊妹项目一并归档；新工作请封装 python-pptx 或用 OfficeCLI。 | MIT | C（6/6） | [中](categories/office-automation/office-powerpoint-mcp-server.zh.md) · [EN](categories/office-automation/office-powerpoint-mcp-server.md) |
| **Apache POI** | 当 JVM 服务必须读取或原地改 Office 文件时用它——不是 Python agent 路径，也不是转换／打印引擎。 | Apache-2.0 | B（3/6） | [中](categories/office-automation/apache-poi.zh.md) · [EN](categories/office-automation/apache-poi.md) |
| **dsh-libreoffice-kit** | 当 Node.js 应用要离线把收到的 Office 文件转成 PDF／PNG（或重算 `.xlsx`），希望 LibreOffice 引擎随 `npm install` 到位、字体可控时用它——但 Linux 只有 WASM 引擎，项目才几周大，GitHub 仓库是落后于 npm 的镜像。 | MPL-2.0 | C（5/6） | [中](categories/office-automation/dsh-libreoffice-kit.zh.md) · [EN](categories/office-automation/dsh-libreoffice-kit.md) |


### office-editors

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Univer** | 当你在*做一个产品*、需要内嵌一个可以逐插件改版重写的表格/文档编辑器、且要求 Apache-2.0 时用它——但协同、xlsx 导入导出、图表、透视表在付费 Pro，1.0 线 2026-09 才发布，路线图系于单一厂商。 | Apache-2.0 | A（6/6） | [中](categories/office-editors/univer.zh.md) · [EN](categories/office-editors/univer.md) |
| **Fortune Sheets** | 当 React 应用要一个 MIT 的即用型类 Excel 网格、并愿意自己接 op 流做持久化时用它——但它是 Luckysheet 血统、功能上限相同，无内置 xlsx 读写，且 2025-11-06 后无提交。 | MIT | B（5/6） | [中](categories/office-editors/fortune-sheets.zh.md) · [EN](categories/office-editors/fortune-sheets.md) |
| **Handsontable** | 当内部数据录入网格需要 15 年打磨的电子表格交互（校验、条件格式、400 个公式）、且预算容得下商业授权时用它——想免费商用就换 Jspreadsheet CE 或 Fortune Sheets。 | 自定义（非商业免费 + 商业付费） | A（5/6） | [中](categories/office-editors/handsontable.zh.md) · [EN](categories/office-editors/handsontable.md) |
| **Jspreadsheet** | 当你想要最轻的 MIT 原生 JS 网格、带列类型与 Excel 复制粘贴时用它——但要接受社区版是 Pro 产品的免费层、GitHub 发布落后于 npm 包。 | MIT | B（5/6） | [中](categories/office-editors/jspreadsheet.zh.md) · [EN](categories/office-editors/jspreadsheet.md) |
| **Grist** | 当团队要的是一个*成品*——自托管、列即数据库字段、公式用 Python、按行权限、带 webhook 的表格平台——而不是一个可嵌入组件时用它；Apache-2.0 核心有法国政府贡献背书、月度发布活跃。 | Apache-2.0 | A（5/6） | [中](categories/office-editors/grist.zh.md) · [EN](categories/office-editors/grist.md) |
| **ONLYOFFICE Docs** | 当你的网盘/CRM/LMS 需要「点一下 .docx 就进入带实时协同的完整编辑器」、一个 Docker 容器搞定且要真实 OOXML 保真度时用它——但它是 AGPL，社区版建议并发 ≤20，GitHub 仓库只是打包壳。 | AGPL-3.0 | B（6/6） | [中](categories/office-editors/onlyoffice-documentserver.zh.md) · [EN](categories/office-editors/onlyoffice-documentserver.md) |
| **Collabora Online** | 当你运行（或对接）Nextcloud 这类支持 WOPI 的文件平台、想在浏览器里用上 LibreOffice 渲染引擎时用它——但活跃开发在 Gerrit 而非这个 GitHub 仓库，这里也没有可嵌入的 UI SDK。 | MPL-2.0 | A（5/6） | [中](categories/office-editors/collabora-online.zh.md) · [EN](categories/office-editors/collabora-online.md) |
| **GenOffice** | 当*你自己*（而不是你产品的用户）想让 AI 在桌面上直接改真正的 `.docx`/`.xlsx`/`.pptx`、改动以可审阅的修订落下、模型自带 key，还想要 `genoffice` CLI/MCP 让编码 agent 也能这样做时用它——但它是一家初创公司两个月大的 `v0.x` 套件，使用统计默认开启，也不支持 `.doc`/ODF。 | Apache-2.0 | C（5/6） | [中](categories/office-editors/genoffice.zh.md) · [EN](categories/office-editors/genoffice.md) |
| **DeckCraft** | 当你想要一个原生构建、开源的 PowerPoint 式编辑器（macOS/Windows/Linux/FreeBSD/网页），而且每个按钮同时是 agent 能调用、还能看渲染结果的 CLI/MCP 命令时用它——但它是诞生两天、主要由 AI agent 写成的 alpha 前版本，`.pptx` 兼容性只在自己生成的稿子上测过。 | MIT OR Apache-2.0 | C（5/6） | [中](categories/office-editors/deckcraft.zh.md) · [EN](categories/office-editors/deckcraft.md) |
### diagramming

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Mermaid** | 当你想把图表写成可进版本库的纯文本（流程图/时序图/ER），在 Markdown 和文档里渲染时用它——不适合像素级精确排版。 | MIT | A（6/6） | [中](categories/diagramming/mermaid.zh.md) · [EN](categories/diagramming/mermaid.md) |
| **flowchart.js** | 当文档站或 wiki 只需几个判断框和箭头、想写成可 git diff 的文本并在浏览器里画成 SVG 时用它——但它只渲染不编辑，节点类型约 9 种，依赖老旧的 Raphael.js，库代码自 2023 年起未再更新。 | MIT | B（5/6） | [中](categories/diagramming/flowchart-js.zh.md) · [EN](categories/diagramming/flowchart-js.md) |
| **bpmn-js** | 当业务分析师需要在你的 Web 应用里编辑或查看合规的 BPMN 2.0 流程图时用它——但其许可证强制保留不可移除的 bpmn.io 水印，白标前务必先确认条款。 | MIT + bpmn.io watermark clause | B（5/6） | [中](categories/diagramming/bpmn-js.zh.md) · [EN](categories/diagramming/bpmn-js.md) |
| **Excalidraw** | 当你要为会议或设计文档快速画一张手绘风草图，或想在自己的应用里嵌一个 MIT 许可的 React 白板组件时用它——但 JSON 文件在 Git 里没法 diff，可嵌入的 npm 包也不带多人协作。 | MIT | B（6/6） | [中](categories/diagramming/excalidraw.zh.md) · [EN](categories/diagramming/excalidraw.md) |
| **draw.io** | 完整的所见即所得绘图应用，`.drawio` 文件是纯文本 mxGraph XML：官方云／UML／BPMN 形状库、可离线运行的桌面版，文件还能进 Git diff。 | Apache-2.0（图标／stencil 另有附加限制） | B（6/6） | [中](categories/diagramming/drawio.zh.md) · [EN](categories/diagramming/drawio.md) |
| **D2** | 当版本化的文本图要在 CI 里用你指定的布局引擎渲染时用它——MPL-2.0 是文件级 copyleft，而且没有宿主平台替你渲染。 | MPL-2.0 | B（6/6） | [中](categories/diagramming/d2.zh.md) · [EN](categories/diagramming/d2.md) |
| **PlantUML** | 当 DSL 必须覆盖多种 UML 与非 UML 图型、且能接受 Java 或服务端渲染时用它——再分发前先看 `LICENSES.md`。 | LGPL-3.0 | B（6/6） | [中](categories/diagramming/plantuml.zh.md) · [EN](categories/diagramming/plantuml.md) |
| **PR Lens** | 当 agent 写的 diff 大到靠滚动无法建立方向感时用它——让改动被画出来，并在每次 push 时重画，直接落在 PR 里。 | MIT | C（6/6） | [中](categories/diagramming/pr-lens.zh.md) · [EN](categories/diagramming/pr-lens.md) |
### media-download

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **youtube-dl** | 当脚本或老流水线已经钉着 youtube-dl、要靠它约 1000 个站点 extractor 按模板文件名拉取媒体时用它——但最后一个打 tag 的发布还是 2021.12.17，master 自 2025-11 起也无提交，涉及 YouTube 请默认用 yt-dlp 分叉。 | Unlicense | B（6/6） | [中](categories/media-download/youtube-dl.zh.md) · [EN](categories/media-download/youtube-dl.md) |
| **you-get** | 当你想要一个极简 Python CLI 从 YouTube 和大量中文站点（B 站/优酷）抓取音视频时用它——比 yt-dlp 更轻。 | MIT | D（3/6） | [中](categories/media-download/you-get.zh.md) · [EN](categories/media-download/you-get.md) |
| **cobalt** | 当你想自托管一个页面、让网络里任何人粘个社交平台链接就拿到视频或音频、没有广告和追踪器时用它——但 API 是 AGPL-3.0，Web 前端是禁止商用的 CC-BY-NC-SA，它也不是可脚本化的 CLI。 | AGPL-3.0 (API) + CC-BY-NC-SA-4.0 (web frontend) | C（5/6） | [中](categories/media-download/cobalt.zh.md) · [EN](categories/media-download/cobalt.md) |
| **lux** | 当你想用一个静态 Go 单文件下载视频、尤其是 Bilibili、抖音这类中文站点，并塞进精简容器或 CI runner 时用它——但站点覆盖比 yt-dlp 窄、修复更慢，master 自 2025-12 起已无提交。 | MIT | B（5/6） | [中](categories/media-download/lux.zh.md) · [EN](categories/media-download/lux.md) |
| **youtube-transcript-api** | 当你想免密钥地为 RAG／摘要管线取回带时间戳的 YouTube 字幕时用它——但它依赖未公开接口、随时可能失效，且云端／机房 IP 现已必须配付费住宅代理。 | MIT | B（6/6） | [中](categories/media-download/youtube-transcript-api.zh.md) · [EN](categories/media-download/youtube-transcript-api.md) |
| **bulk-downloader-for-reddit** | 当你想用脚本归档某个子版块、用户或自己收藏的帖子——媒体文件连同标题、得分、评论树——走 Reddit OAuth API 时用它——但列表上限约 1000 帖无法绕过，近期登录失败问题未修，最后一次发布还在 2023 年。 | GPL-3.0 | D（4/6） | [中](categories/media-download/bulk-downloader-for-reddit.zh.md) · [EN](categories/media-download/bulk-downloader-for-reddit.md) |
| **yt-dlp** | 当你要把数千个站点里的视频、播客或整个播放列表存成合并好的单个文件，或让定时任务只抓新上传时用它——但它解不了 DRM 流，而且完整支持 YouTube 现在需要装一个 JavaScript 运行时。 | Unlicense | A（6/6） | [中](categories/media-download/yt-dlp.zh.md) · [EN](categories/media-download/yt-dlp.md) |
| **gallery-dl** | 当你想把约 390 个受支持站点上某位画师、某个标签搜索或某个账号的原图全部存下来，并且重跑时只拉新文件时用它——但 2026 年一次 DMCA 通知后开发已迁到 Codeberg，GitHub 仓库只剩发版提交。 | GPL-2.0 | B（6/6） | [EN](categories/media-download/gallery-dl.md) · [中](categories/media-download/gallery-dl.zh.md) |

### media-processing

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **FFmpeg** | 当你需要在管线里解码/编码/转码/滤镜处理几乎任何音视频时用它——注意 LGPL→GPL 的构建授权陷阱。 | LGPL-2.1-or-later | A（4/6） | [中](categories/media-processing/video-audio/transcoding-and-pipelines/ffmpeg.zh.md) · [EN](categories/media-processing/video-audio/transcoding-and-pipelines/ffmpeg.md) |
| **HandBrake** | 当一堆手机视频、录屏或无加密光盘要压成更小、到处能播的 MP4/MKV，并想在图形界面或 HandBrakeCLI 里选个有名字的预设就完事时用它——但它永远重编码，也打不开有拷贝保护的光盘。 | GPL-2.0-only | A（5/6） | [中](categories/media-processing/video-audio/transcoding-and-pipelines/handbrake.zh.md) · [EN](categories/media-processing/video-audio/transcoding-and-pipelines/handbrake.md) |
| **ffmpeg-python** | 当你在 Python 里要拼 trim、concat、overlay 这类滤镜图、手写 -filter_complex 已经读不懂时用它——但它只是替已安装的 ffmpeg 二进制拼命令行，拿不到逐帧数据，且自 2022 年起已停止演进。 | Apache-2.0 | C（4/6） | [中](categories/media-processing/video-audio/transcoding-and-pipelines/ffmpeg-python.zh.md) · [EN](categories/media-processing/video-audio/transcoding-and-pipelines/ffmpeg-python.md) |
| **PyAV** | 当 Python 代码要在同一进程里拿到每一帧解码后的画面和时间戳、并转成 NumPy 数组（比如做机器学习预处理或自定义编码）时用它——但 ffmpeg 命令已经能干完的活，用 PyAV 只会多出工作量。 | BSD-3-Clause | A（6/6） | [中](categories/media-processing/video-audio/transcoding-and-pipelines/pyav.zh.md) · [EN](categories/media-processing/video-audio/transcoding-and-pipelines/pyav.md) |
| **VMAF** | 当你在调编码档位、需要用业界通用的 0—100 感知分对比编解码器与预设时用它——但它只支持全参考，且选错模型会悄悄让跨版本对比失效。 | BSD-2-Clause-Patent | B（5/6） | [中](categories/media-processing/quality-metrics/vmaf.zh.md) · [EN](categories/media-processing/quality-metrics/vmaf.md) |
| **SSIMULACRA2** | 当你要对照原图给 JPEG XL、AVIF 或 WebP 的编码参数排序，需要一个比 PSNR、SSIM 更贴近人眼评分的静态图分数时用它——但这个上游仓库自 2025-05 起已冻结，仍在维护的拷贝在 libjxl 里。 | BSD-3-Clause | C（3/6） | [中](categories/media-processing/quality-metrics/ssimulacra2.zh.md) · [EN](categories/media-processing/quality-metrics/ssimulacra2.md) |
| **m3u8** | 当 Python 代码要把 HLS .m3u8 播放列表（分片、变体流、密钥、不连续点）当类型化对象读取、检查或改写，而不是拿正则去抠时用它——但它只处理播放列表文本，不碰媒体本身，且自 2025-01 起无新提交。 | MIT | C（4/6） | [中](categories/media-processing/video-audio/transcoding-and-pipelines/m3u8.zh.md) · [EN](categories/media-processing/video-audio/transcoding-and-pipelines/m3u8.md) |
| **ffsubsync** | 当字幕整体存在恒定偏移、你想用一条命令做 FFT 音频对齐而不手动设同步点时用它——但它修不了内容内部的逐行／变动漂移，且仅单人维护。 | MIT | B（5/6） | [中](categories/media-processing/video-audio/speech-and-subtitles/ffsubsync.zh.md) · [EN](categories/media-processing/video-audio/speech-and-subtitles/ffsubsync.md) |
| **MoviePy** | 当你要用脚本批量截取、加字幕、合成一批片段，而 FFmpeg 的滤镜字符串已经没人看得懂时用它——但维护处于滑行状态：2025-05 之后没有新版本，README 还在招维护者。 | MIT | B（6/6） | [中](categories/media-processing/video-audio/editing-and-cutting/moviepy.zh.md) · [EN](categories/media-processing/video-audio/editing-and-cutting/moviepy.md) |
| **GStreamer** | 当摄像头、车载屏或分析盒子要在你自己的 C、Rust 或 Python 程序里全天候跑“采集—叠加—编码—推流”管线，并能在运行中改参数时用它——但只是一次性转码文件的话，FFmpeg 命令行代码少得多。 | LGPL-2.1-or-later | A（4/6） | [中](categories/media-processing/video-audio/transcoding-and-pipelines/gstreamer.zh.md) · [EN](categories/media-processing/video-audio/transcoding-and-pipelines/gstreamer.md) |
| **MLT** | 当你要造一个视频编辑器，或做一条需要精确到帧的时间线（轨道、滤镜、转场）、经 FFmpeg 渲染的自动化流水线时用它——但它是框架不是应用，只想剪片请用 Shotcut 或 Kdenlive。 | LGPL-2.1-or-later | B（6/6） | [中](categories/media-processing/video-audio/editing-and-cutting/mlt.zh.md) · [EN](categories/media-processing/video-audio/editing-and-cutting/mlt.md) |
| **OpenAI Whisper** | 当几百小时多语言录音需要在自己机器上转出可检索的文字稿和 .srt 字幕、而不是按分钟付费给云端 API 时用它——但它没有流式模式，实时字幕请用 whisper.cpp 或 faster-whisper。 | MIT | A（5/6） | [中](categories/media-processing/video-audio/speech-and-subtitles/whisper.zh.md) · [EN](categories/media-processing/video-audio/speech-and-subtitles/whisper.md) |
| **sharp** | 当 Node.js 的上传处理、构建步骤或 API 路由要在进程内快速把大图转成缩略图和 WebP/AVIF 时用它——但它的预编译二进制解不了 HEIC、PDF、PSD 和相机 RAW。 | Apache-2.0 | A（6/6） | [EN](categories/media-processing/image-processing/sharp.md) · [中](categories/media-processing/image-processing/sharp.zh.md) |
| **ImageMagick** | 当脚本或 CI 任务要用一条 shell 命令把 TIFF、PSD、EPS、HEIC、多页 PDF 等 200 多种格式转换、缩放、合成时用它——但不加隔离就去解码不可信的上传图片，CVE 风险源源不断。 | ImageMagick | B（5/6） | [EN](categories/media-processing/image-processing/imagemagick.md) · [中](categories/media-processing/image-processing/imagemagick.zh.md) |
| **Screenshot Service** | 仅适合作为隔离的内部 HTML 转图片 worker——API 鉴权已禁用，Chromium 还关闭了 sandbox 与 Web 安全。 | NOASSERTION | D（4/6） | [中](categories/media-processing/image-processing/screenshot-service.zh.md) · [EN](categories/media-processing/image-processing/screenshot-service.md) |
| **Magpie** | 老游戏或固定尺寸的 Windows 程序窗口在高分屏上太小或被拉糊、又不想往进程里注入东西时，用它做实时 GPU 放大（FSR、Anime4K）——但只支持 Windows，没有 HDR 和补帧，发版落后于 dev 分支。 | GPL-3.0 | B（6/6） | [EN](categories/media-processing/image-processing/magpie.md) · [中](categories/media-processing/image-processing/magpie.zh.md) |
| **PhotoCraft** | 没有 Photoshop 席位、又要离线改分层 PSD 时用它——调整图层、蒙版和文字保持可编辑，命令行／MCP 驱动同一个引擎——但它是一个九天大、由 agent 写成的早期 alpha，团队自评日常专业可用度约 25–35%。 | MIT OR Apache-2.0 | B（6/6） | [EN](categories/photo-editing/photocraft.md) · [中](categories/photo-editing/photocraft.zh.md) |
| **Concat** | 当你需要一款当下就能安装运行、原生、离线、可脚本化的类 CapCut 视频编辑器时用它——但它是仅有约 25 天历史的 0.2.x beta、只有一位维护者，且专业能力（遮罩、跟踪、关键帧曲线）仍在路线图上。 | AGPL-3.0-or-later | C（6/6） | [中](categories/media-processing/video-editing/concat.zh.md) · [EN](categories/media-processing/video-editing/concat.md) |
| **OpenCut** | 仅当你打算跟进或基于浏览器／WASM 重写架构开发时用它——其仓库正在重写、不接受外部贡献、不产出可用版本，能用的 classic 版本在已归档仓库里。 | MIT | B（5/6） | [中](categories/media-processing/video-editing/opencut.zh.md) · [EN](categories/media-processing/video-editing/opencut.md) |
| **Palmier Pro** | 当你想让编码 agent 通过本机 MCP 服务，直接改你在 macOS 26 Apple 芯片 Mac 上开着的时间线时用它——但只有 v0.7.6 之前的源码是 GPL，之后的二进制已闭源，AI 生成走厂商按额度计费的后端。 | GPL-3.0 | C（6/6） | [中](categories/media-processing/video-editing/palmier-pro.zh.md) · [EN](categories/media-processing/video-editing/palmier-pro.md) |
| **OpenScreen** | 当你想免费得到 Screen Studio 那种成片感的屏幕演示——录屏后自动出跟随光标的缩放、抹平光标、背景与本地字幕，导出 MP4／GIF——时用它；代价是上游仓库 2026-06 已归档，维护只在社区分支里继续。 | MIT | C（6/6） | [中](categories/media-processing/video-editing/openscreen.zh.md) · [EN](categories/media-processing/video-editing/openscreen.md) |
| **EffectCraft** | 当你想免费、在 Linux 上、或让 agent 通过 MCP 来做 After Effects 式的动态图形——图层、关键帧、表达式、306 个同名效果、Lottie 导出——时用它；代价是只有 8 天历史、代码大多由 agent 编写、打不开 `.aep`，与 After Effects 的保真度也没测过。 | MIT OR Apache-2.0 | B（5/6） | [中](categories/media-processing/video-editing/effectcraft.zh.md) · [EN](categories/media-processing/video-editing/effectcraft.md) |
| **Jianying Headless** | 当 macOS 上的剪映工作流需要 agent 生成**可编辑**草稿——真实多轨工程，并可用应用自己的引擎原生导出 MP4——时用它；代价是仅 5 天历史、单一维护者、绑定某一个应用版本、且仅限非商用。 | Personal Learning and Non-Commercial Use License（NOASSERTION，非 OSI） | D（4/6） | [中](categories/media-processing/nle-automation/jianying-headless.zh.md) · [EN](categories/media-processing/nle-automation/jianying-headless.md) |
| **pyJianYingDraft** | 当 Python 管线需要跨平台产出可编辑剪映草稿、且接受 Apache-2.0 时用它——代价是新版剪映草稿已加密、它自己不做渲染、自带批量导出只支持 Windows 加剪映 6 及更早版本。 | Apache-2.0 | C（5/6） | [中](categories/media-processing/nle-automation/pyjianyingdraft.zh.md) · [EN](categories/media-processing/nle-automation/pyjianyingdraft.md) |
| **JianYing Editor Skill** | 当 coding agent 应该把一句自然语言需求变成真实剪映时间轴——素材、TTS 配音、对齐字幕、配乐与具名特效——而由你在剪映里判断并导出时用它；代价是没有 tagged release、无人值守导出只在 Windows、且会接管屏幕。 | MIT | C（3/5） | [中](categories/media-processing/nle-automation/jianying-editor-skill.zh.md) · [EN](categories/media-processing/nle-automation/jianying-editor-skill.md) |
| **Auto-Editor** | 当反复出现的任务是从长素材里剪掉冷场时用它——按响度／运动打标签的命令行工具，还能导出 Premiere／Resolve／Final Cut／ShotCut／Kdenlive 可导入的时间线；忘了 `pip`，用二进制或 Homebrew 装。 | Unlicense | A（6/6） | [中](categories/media-processing/video-audio/editing-and-cutting/auto-editor.zh.md) · [EN](categories/media-processing/video-audio/editing-and-cutting/auto-editor.md) |

### video-production

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **OpenMontage** | 当你想让 AI 编程助手从一句自然语言描述出发，完成研究、脚本、素材生成、合成与渲染，产出完整视频（解说、预告片、动画、纪录片蒙太奇）时使用。 | AGPL-3.0 | B（5/6） | [中](categories/video-production/open-montage.zh.md) · [EN](categories/video-production/open-montage.md) |
| **HyperFrames** | 当你需要确定性、代码形态的视频——HTML composition 在 CI 里渲染成 MP4——并希望 agent skill 覆盖整条生产回路时用它；它是渲染引擎，不是生成式视频模型。 | Apache-2.0 | B（6/6） | [中](categories/video-production/hyperframes.zh.md) · [EN](categories/video-production/hyperframes.md) |
| **anything2explainer** | 当你想让 Claude Code / Codex skill 把一个主题做成带配音的 MG 科普讲解视频（中文或英文）时用它——9 阶段多 agent 流水线带人工确认点和量化 QC；固定黑底风格，PolyForm 非商用许可。 | PolyForm-Noncommercial-1.0.0 | C（3/5） | [中](categories/video-production/anything2explainer.zh.md) · [EN](categories/video-production/anything2explainer.md) |
| **Hypit** | 当你想让 agent 把某条特定爆款视频克隆成可编辑、词锚定的 SVML workflow，并通过换脸/换词/换 B-roll 批量出变体时用它——agent 优先、非 OSI 许可证、非常年轻。 | Hypit Open Source License（modified Apache-2.0，非 OSI） | C（4/6） | [中](categories/video-production/hypit.zh.md) · [EN](categories/video-production/hypit.md) |
| **Remotion** | 当 React 优先的团队需要久经验证的程序化视频——composition 即 React 组件、经 headless Chrome 渲染、带成熟 Lambda 云渲染——且接受 source-available 许可证（个人与 3 人以下公司免费）时用它。 | Remotion License（source-available，非 OSI） | A（4/6） | [中](categories/video-production/remotion.zh.md) · [EN](categories/video-production/remotion.md) |
| **MoneyPrinterTurbo** | 当你需要一台可自托管的 MIT 家电（WebUI + API），把主题变成近零边际成本的口播库存素材短视频时用它——不做爆款结构克隆，不需要 coding agent。 | MIT | B（6/6） | [中](categories/video-production/moneyprinter-turbo.zh.md) · [EN](categories/video-production/moneyprinter-turbo.md) |
| **video-shotcraft** | 当 coding agent 应该用 150+ 张镜头配方卡、真实页面截图、2.5D 运镜和一支已验收的 Remotion 模板，把你的产品或网页做成电影感宣传片时用它——仅约 2 个月历史、无 tagged release，且产出 Remotion composition，受引擎「3 人以上需付费」的许可门槛约束。 | Apache-2.0 | B（5/6） | [中](categories/video-production/video-shotcraft.zh.md) · [EN](categories/video-production/video-shotcraft.md) |
| **OpenCreator** | 当双语频道或本地化台要把*这一条*视频做字幕、配音、竖屏重切，同一项目里还要写稿和生成，并且已经有 Codex 登录时用它——不是从零做片的管线，也没有 Linux 桌面版。 | Apache-2.0 | B（6/6） | [中](categories/video-production/open-creator.zh.md) · [EN](categories/video-production/open-creator.md) |
| **video-use** | 当 coding agent 该对着一文件夹素材、靠打包转写稿来剪——先确认方案再 ffmpeg——而不是生成底片时用它；硬依赖 ElevenLabs Scribe，22 次提交却有 2.7 万 star。 | MIT | B（4/5） | [中](categories/video-production/video-use.zh.md) · [EN](categories/video-production/video-use.md) |
| **SeeCut** | 当 coding agent 该把真人/数字人口播 A-roll 精剪成高网感动效短视频时用它：画面铺真证据截图，每版都要过一个能看视频的 AI 评委（agy 调 Gemini），交付成片加可选的剪映分层草稿；PolyForm 非商用，验证时仅 4 天龄。 | PolyForm-Noncommercial-1.0.0 | D（4/6） | [中](categories/video-production/seecut.zh.md) · [EN](categories/video-production/seecut.md) |
| **fframes** | 当代码或 agent 写的动效视频要在自己的 GPU 上、不经浏览器快速渲染时用它——Rust + SVG 写帧、链接 libav 编码，每个项目自带给“看不见的作者”检查画面和响度的命令行；MIT 许可，但要原生工具链，1.0 在 2026-09-28 才发布，单人维护。 | MIT | B（4/6） | [中](categories/video-production/fframes.zh.md) · [EN](categories/video-production/fframes.md) |
| **claude-video** | 让 Claude “看视频”的 `/watch` skill：下载视频、抽帧、转录，并把这些证据交给 Claude。 | MIT | C（6/6） | [中](categories/media-processing/video-audio/speech-and-subtitles/claude-video.zh.md) · [EN](categories/media-processing/video-audio/speech-and-subtitles/claude-video.md) |

### llm-chat-ui

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **NextChat** | 当你想要一个私有、可自部署、跨 web/桌面/移动 的多 provider AI 聊天前端时用它——不是多用户 RBAC 团队平台。 | MIT | B（6/6） | [中](categories/llm-chat-ui/nextchat.zh.md) · [EN](categories/llm-chat-ui/nextchat.md) |
| **Open WebUI** | 当你用 Ollama 跑本地模型，想要一个带账号、分组权限和文档问答的 ChatGPT 式网页界面，甚至完全离线运行时用它——但许可证不是 OSI 认可的，超过 50 个用户的部署未经许可不得换品牌。 | NOASSERTION (Open WebUI License — BSD-3-Clause plus a branding clause above 50 users; CLA) | B（5/6） | [中](categories/llm-chat-ui/open-webui.zh.md) · [EN](categories/llm-chat-ui/open-webui.md) |
| **LibreChat** | 当一个组织想要一套挂在 SSO 后面的自托管聊天应用，让员工在同一个菜单里选 OpenAI、Anthropic、Bedrock、Azure 或本地模型，聊天记录留在自己的数据库里时用它——但必须用 MongoDB，且自 2025 年起归 ClickHouse 所有。 | MIT | B（5/6） | [EN](categories/llm-chat-ui/librechat.md) · [中](categories/llm-chat-ui/librechat.zh.md) |

### markdown-tools

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **CommonMark** | 当你要在 JavaScript 里拿到规范作者给出的标准答案、判定某个 Markdown 边界情况该怎么解析，并需要一棵可改写的节点树时用它——但它只做 CommonMark：没有表格、任务列表、删除线，也没有扩展 API。 | BSD-2-Clause | B（5/6） | [中](categories/markdown-tools/commonmark.zh.md) · [EN](categories/markdown-tools/commonmark.md) |
| **Markdown Here** | 当你在网页邮箱或 Thunderbird 里写技术邮件、想用 Markdown 写好代码块、表格和列表，发送前一键渲染成 HTML 时用它——但上游已近停滞，浏览器的 Manifest V3 变化可能让它失效或被下架。 | MIT | C（4/6） | [中](categories/markdown-tools/markdown-here.zh.md) · [EN](categories/markdown-tools/markdown-here.md) |
| **marked** | 当你需要一个快速、底层的 JS Markdown→HTML 解析器时用它——但你得自己做 XSS 消毒，且不要求严格 CommonMark。 | MIT | A（5/6） | [中](categories/markdown-tools/marked.zh.md) · [EN](categories/markdown-tools/marked.md) |
| **remark** | 当你的 Node.js 文档或内容流水线要通过 mdast 语法树检查、改写、再写回 Markdown（列表符号、目录、链接路径）时用它——但只要 Markdown 转 HTML 的话，marked 或 markdown-it 更轻。 | MIT | A（6/6） | [中](categories/markdown-tools/remark.zh.md) · [EN](categories/markdown-tools/remark.md) |
| **markdown-it** | 当你的 JavaScript 文档站、CMS 预览或聊天界面要把 Markdown 转成 HTML，既要符合 CommonMark 又要用插件加自定义语法时用它——但它的扁平 token 流只为渲染设计，检查或改写 Markdown 该用 remark。 | MIT | A（6/6） | [中](categories/markdown-tools/markdown-it.zh.md) · [EN](categories/markdown-tools/markdown-it.md) |
| **micromark** | 当你要在约 14 kB、默认安全的包里得到和 cmark 一致的 CommonMark 解析，或者要给检查器、编辑器拿到精确到字节的 token 位置时用它——但它只给 token 或 HTML，不给可修改的树，要改写 Markdown 请用 remark。 | MIT | B（6/6） | [中](categories/markdown-tools/micromark.zh.md) · [EN](categories/markdown-tools/micromark.md) |
| **Pandoc** | 当同一份 Markdown、Org 或 LaTeX 源文件要交付成 DOCX、EPUB、PDF、HTML 或 wiki 标记，或要把同事的 .docx 转回 Markdown 时用它——但版式复杂的文档会有损，而且它读不了 PDF。 | GPL-2.0 | B（6/6） | [EN](categories/markdown-tools/pandoc.md) · [中](categories/markdown-tools/pandoc.zh.md) |
| **Goldmark** | 当你的 Go 服务或工具要把 Markdown 渲染得和 GitHub 一致（包括中日文加粗），需要 GFM 扩展又不想引入第三方模块时用它——但 v2 改了 API，多数第三方扩展还没迁过来。 | MIT | A（6/6） | [EN](categories/markdown-tools/goldmark.md) · [中](categories/markdown-tools/goldmark.zh.md) |
| **markdownlint** | 当 Markdown 是你仓库的交付物，想用 MD001–MD060 规则在 CI 和编辑器里抓出混用的列表符号、跳级标题、失效锚点时用它——但这个仓库只是库，要命令行请用 markdownlint-cli2。 | MIT | A（6/6） | [EN](categories/markdown-tools/markdownlint.md) · [中](categories/markdown-tools/markdownlint.zh.md) |
| **MDX** | 当文档活在 React／Preact／Vue 应用里、正文需要 import 并渲染你自己的组件时用它——但交付物是独立 PDF、书或可发布文档时不要用。 | MIT | B（5/6） | [中](categories/markdown-tools/mdx.zh.md) · [EN](categories/markdown-tools/mdx.md) |
| **TanStack Markdown** | 当你的文档/博客语料由作者控制、包体积是硬约束，且你要 HTML/React/Octane 三个渲染器从同一份缓存 AST 输出完全一致的页面时用它——不要用它渲染不可信用户 Markdown，也不要指望它严格遵循 CommonMark。 | MIT | C（5/6） | [中](categories/markdown-tools/tanstack-markdown.zh.md) · [EN](categories/markdown-tools/tanstack-markdown.md) |
| **TanStack Highlight** | 当博客或文档只用一小撮已知语言、想要体积极小、同步执行、只带类名且服务端与客户端一致的代码高亮时用它——要 VS Code 级准确度、冷门语言或自动检测语言时不要用。 | MIT | B（6/6） | [中](categories/markdown-tools/tanstack-highlight.zh.md) · [EN](categories/markdown-tools/tanstack-highlight.md) |

### typesetting

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Asciidoctor** | 当技术文档需要从纯文本源发布成 HTML、DocBook、EPUB 或 man page 时用它——但你需要排版引擎或印刷级 PDF 时不要用。 | MIT | B（4/6） | [中](categories/typesetting/asciidoctor.zh.md) · [EN](categories/typesetting/asciidoctor.md) |
| **LaTeX** | 当投稿方的 class 文件、几十年的宏包积累、或几十年稳定的源语言决定结果时用它——但没人愿意维护 `\begin{}` 脚手架、或你需要从同一份文件出 HTML 时不要用。 | LPPL-1.3c | B（6/6） | [中](categories/typesetting/latex.zh.md) · [EN](categories/typesetting/latex.md) |
| **Quarkdown** | 当你需要一份保持 Markdown 可读性的源文件编译成网页、印刷 PDF、reveal.js 幻灯片与文档站时用它——但交付物必须是 Word、许可必须宽松、或印刷保真度是硬要求时不要用。 | GPL-3.0 / AGPL-3.0 | C（6/6） | [中](categories/typesetting/quarkdown.zh.md) · [EN](categories/typesetting/quarkdown.md) |
| **Typst** | 当你能自己选源语言，想要学习曲线短、Apache-2.0 许可的印刷级 PDF 时用它——但投稿方指定 LaTeX class 文件、或源必须保持 Markdown 时不要用。 | Apache-2.0 | A（5/6） | [中](categories/typesetting/typst.zh.md) · [EN](categories/typesetting/typst.md) |

### pdf-tools

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **PDF.js** | 当你需要在浏览器/Node 里渲染或读取 PDF（Firefox 的引擎）时用它——它不创建也不编辑 PDF。 | Apache-2.0 | A（6/6） | [中](categories/pdf-tools/pdf-reading/pdfjs.zh.md) · [EN](categories/pdf-tools/pdf-reading/pdfjs.md) |
| **pdf-lib** | 当你要用同一份 TypeScript 代码在浏览器、Node、Deno 或 React Native 里创建、填写或合并 PDF、且不能有原生依赖时用它——但上游自 2021-11 起冻结，新项目应改用有人维护的 fork `@cantoo/pdf-lib`。 | MIT | C（4/6） | [中](categories/pdf-tools/pdf-generation/pdf-lib.zh.md) · [EN](categories/pdf-tools/pdf-generation/pdf-lib.md) |
| **jsPDF** | 当 Web 应用需要一个“下载 PDF”按钮，在浏览器里按坐标摆放文字和图片生成收据、标签、票据或证书时用它——但它改不了已有 PDF，`html()` 遇到现代 CSS 也会走样。 | MIT | B（5/6） | [中](categories/pdf-tools/pdf-generation/jspdf.zh.md) · [EN](categories/pdf-tools/pdf-generation/jspdf.md) |
| **PyMuPDF** | 当大批量的 Python 流水线要在一个快速、离线的包里完成带坐标的文字和表格抽取、页面渲染、涂黑和合并时用它——但它是 AGPL-3.0，闭源软件或 SaaS 要用就得买 Artifex 的商业许可。 | AGPL-3.0 | B（6/6） | [EN](categories/pdf-tools/pdf-reading/pymupdf.md) · [中](categories/pdf-tools/pdf-reading/pymupdf.zh.md) |
| **pdfplumber** | 当机器生成的 PDF（申报文件、通知、价目表）里的表格被抽得糊成一团，你需要字符坐标和可视化调试来把每一行调对时用它——但它没有 OCR，处理不了扫描件。 | MIT | B（6/6） | [EN](categories/pdf-tools/pdf-reading/pdfplumber.md) · [中](categories/pdf-tools/pdf-reading/pdfplumber.zh.md) |
| **OCRmyPDF** | 当扫描仪不断往文件夹里丢只有图片的 PDF，你想让无人值守的任务把它们原样变成可搜索、可复制的文件（可选 PDF/A）时用它——但它产出的是带隐藏文字层的 PDF，不是给 RAG 用的 Markdown。 | MPL-2.0 | B（6/6） | [EN](categories/pdf-tools/pdf-transform-signing/ocrmypdf.md) · [中](categories/pdf-tools/pdf-transform-signing/ocrmypdf.zh.md) |
| **qpdf** | 当脚本要合并、拆分、重排、加密、线性化或修复 PDF，又不能让页面、字体、表单域被重新渲染时用它——但它不渲染、不抽文字、不画新内容，也不做签名。 | Apache-2.0 | A（6/6） | [EN](categories/pdf-tools/pdf-transform-signing/qpdf.md) · [中](categories/pdf-tools/pdf-transform-signing/qpdf.zh.md) |
| **SAPP** | 当 PHP 应用必须追加 PKCS#12 签名、又不能破坏已有 PDF 修订时用它——规范覆盖较窄，也不支持加密 PDF。 | LGPL-3.0-or-later | B（5/6） | [中](categories/pdf-tools/pdf-transform-signing/sapp.zh.md) · [EN](categories/pdf-tools/pdf-transform-signing/sapp.md) |
| **FPDI** | 当基于 FPDF／TCPDF／tFPDF 的 PHP 应用要把已有 PDF 的页面当模板导入时用它——免费解析器不支持加密文件与压缩交叉引用流。 | MIT | A（5/6） | [中](categories/pdf-tools/pdf-generation/fpdi.zh.md) · [EN](categories/pdf-tools/pdf-generation/fpdi.md) |
| **pyHanko** | 当 Python 需要按成文记录的 PAdES／LTV 流程创建或验证 PDF 签名时用它——上游仍自标 beta。 | MIT | A（6/6） | [中](categories/pdf-tools/pdf-transform-signing/pyhanko.zh.md) · [EN](categories/pdf-tools/pdf-transform-signing/pyhanko.md) |
| **PdfCraft** | 当 macOS、Windows 或 Linux 上的人需要一个离线、免账号的桌面应用来整理、批注、填写、涂黑和加密 PDF（或让 agent 经 MCP 做同样的事）时用它——但它才九天大、尚未 1.0，渲染器是借的，与 Acrobat 的保真度也没测过。 | MIT OR Apache-2.0 | C（5/6） | [中](categories/pdf-tools/pdf-transform-signing/pdfcraft.zh.md) · [EN](categories/pdf-tools/pdf-transform-signing/pdfcraft.md) |
| **PDFMathTranslate** | 科研 PDF 必须保住公式和双栏再翻译时用它——CLI/GUI/Docker，翻译后端多；AGPL，且 1.x 钉着旧版 BabelDOC。 | AGPL-3.0 | C（5/6） | [中](categories/pdf-tools/pdf-translation/pdfmathtranslate.zh.md) · [EN](categories/pdf-tools/pdf-translation/pdfmathtranslate.md) |
| **BabelDOC** | 要嵌入或调试当前 0.6 的保留排版 PDF 翻译引擎时用它——不是面向用户的成品；AGPL，只接 OpenAI，API 不受支持。 | AGPL-3.0 | C（6/6） | [中](categories/pdf-tools/pdf-translation/babeldoc.zh.md) · [EN](categories/pdf-tools/pdf-translation/babeldoc.md) |
| **PDFMathTranslate-next** | 要把 BabelDOC 0.6 当 CLI/网页来跑、默认走硅基流动免费通道时用它——AGPL，Google/Bing 已撤，最后推送 2026-05。 | AGPL-3.0 | D（4/6） | [中](categories/pdf-tools/pdf-translation/pdfmathtranslate-next.zh.md) · [EN](categories/pdf-tools/pdf-translation/pdfmathtranslate-next.md) |
| **pdfcn** | 要用 shadcn CLI 把带主题的 React PDF 组件和整页文档模板（发票、报告、面单）复制进项目、底下跑 Takumi 或 Forme 时用它——只生成新 PDF。 | MIT | B（6/6） | [中](categories/pdf-tools/pdf-generation/pdfcn.zh.md) · [EN](categories/pdf-tools/pdf-generation/pdfcn.md) |

### workflow-orchestration

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Apache Airflow** | 当你要用 Python DAG 加 Web UI 编排定时批处理数据管线时用它——不适合低延迟或事件驱动流。 | Apache-2.0 | A（6/6） | [中](categories/workflow-orchestration/airflow.zh.md) · [EN](categories/workflow-orchestration/airflow.md) |
| **Gaia** | 只在研究“流水线即编译插件”设计（job 是真代码，经 go-plugin 运行）或评估是否 fork 时用它——但仓库已归档，最后一次发布在 2022-01，绝不要用于新的生产部署。 | Apache-2.0 | D（6/6） | [中](categories/workflow-orchestration/gaia.zh.md) · [EN](categories/workflow-orchestration/gaia.md) |
| **Airflow Maintenance DAGs** | 当自管的 Airflow 集群被旧元数据行和陈旧日志拖慢、你想直接拷入现成清理 DAG 时用它——但 `db-cleanup` 默认第一次运行就真删，且依赖随版本变化的内部结构，先 dry-run 并备份。 | Apache-2.0 | D（4/6） | [中](categories/workflow-orchestration/airflow-maintenance-dags.zh.md) · [EN](categories/workflow-orchestration/airflow-maintenance-dags.md) |
| **n8n** | 当小型运维团队要把 SaaS 之间的胶水流程自托管在一张业务同事也看得懂的可视化画布上，靠 1500 多个连接器节点和代码节点兜底时用它——但 Sustainable Use License 不允许转售或嵌入产品，也不适合亚秒级流处理。 | NOASSERTION (fair-code) | A（4/6） | [中](categories/workflow-orchestration/n8n.zh.md) · [EN](categories/workflow-orchestration/n8n.md) |
| **Argo Workflows** | 当批处理或机器学习流水线已经以容器形式跑在 Kubernetes 上，你想用 YAML 写 DAG、每一步都是带重试、产物传递和界面的 pod 时用它——但它离不开 Kubernetes，成千上万个小步骤也要各付一次 pod 启动开销。 | Apache-2.0 | A（6/6） | [EN](categories/workflow-orchestration/argo-workflows.md) · [中](categories/workflow-orchestration/argo-workflows.zh.md) |
| **Prefect** | 当已经能跑的 Python 脚本需要定时、重试、运行历史和告警，又不想改写成 DAG 文件时用它（加装饰器即可，控制流仍是普通 Python）——但要让非工程师搭流程用 n8n，崩溃后要从原步骤精确恢复用 Temporal。 | Apache-2.0 | A（6/6） | [EN](categories/workflow-orchestration/prefect.md) · [中](categories/workflow-orchestration/prefect.zh.md) |
| **Dagster** | 当你负责数仓流水线，要说清哪张表过期了、由哪次运行构建、谁依赖它，想把资产声明成 Python 函数时用它——但 Airflow 的现成算子更多，告警、RBAC、单点登录都只在付费的 Dagster+ 里。 | Apache-2.0 | A（6/6） | [EN](categories/workflow-orchestration/dagster.md) · [中](categories/workflow-orchestration/dagster.zh.md) |
| **Temporal** | 当一个长时间运行的业务流程（支付、履约、开通、AI agent）必须扛过崩溃和发布、从原来那一步接着跑，又想用普通代码来写时用它——但自托管意味着要运维多服务集群，分片数等决定建好就改不了。 | MIT | A（5/6） | [EN](categories/workflow-orchestration/temporal.md) · [中](categories/workflow-orchestration/temporal.zh.md) |
| **TanStack Workflow** | 跨天的持久流程必须嵌在 TypeScript 应用里、落在你自己的数据库上，且不想多运维一个 workflow server 时用它——0.0.x，控制平面界面还没有，运维面要自己拼。 | MIT | C（6/6） | [中](categories/workflow-orchestration/tanstack-workflow.zh.md) · [EN](categories/workflow-orchestration/tanstack-workflow.md) |

### llm-inference

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Modular Platform (MAX + Mojo)** | 当你想要高性能 GPU/CPU 推理平台（MAX）加 Mojo 系统语言、并接受单厂商绑定与部分非生产许可时用它。 | Apache-2.0 (mixed) | B（5/6） | [中](categories/llm-inference/serving-engines/modular.zh.md) · [EN](categories/llm-inference/serving-engines/modular.md) |
| **omlx** | 当你想在 Mac（Apple Silicon）上用 MLX 跑带 SSD 分层 KV 缓存的本地 LLM 推理服务时用它——年轻的单人仓库，star 数存疑。 | Apache-2.0 | B（6/6） | [中](categories/llm-inference/local-runtimes/omlx.zh.md) · [EN](categories/llm-inference/local-runtimes/omlx.md) |
| **MTPLX** | 当你想让模型自带的 MTP 头在 Mac 上以精确投机解码把 Qwen 3.8 跑出约 2 倍速、并要 OpenAI/Anthropic 服务器与应用形态时用它——接受约五个月大、作者主导的仓库与产品内署名条款。 | Apache-2.0（含署名 NOTICE） | B（6/6） | [中](categories/llm-inference/local-runtimes/mtplx.zh.md) · [EN](categories/llm-inference/local-runtimes/mtplx.md) |
| **AirLLM** | 当模型在你需要的形态下装不进显卡、而墙钟时间免费时用它——把检查点从磁盘逐层流式读取的库，显存只需一层的开销，代价是秒到分钟级的每 token 等待。 | Apache-2.0 | B（6/6） | [中](categories/llm-inference/local-runtimes/airllm.zh.md) · [EN](categories/llm-inference/local-runtimes/airllm.md) |
| **TensorRT-LLM** | 当你在 Hopper 或 Blackwell GPU 上服务高流量模型，需要 NVIDIA 调优内核、FP4 和整机柜并行来补上吞吐差距时用它——但它只跑在较新的 NVIDIA GPU 上，部分关键内核还是预编译二进制。 | Apache-2.0 | B（5/6） | [中](categories/llm-inference/serving-engines/tensorrt-llm.zh.md) · [EN](categories/llm-inference/serving-engines/tensorrt-llm.md) |
| **vLLM** | 当你想要事实上的开源 LLM 服务引擎，带 PagedAttention、连续批处理和 OpenAI 兼容 API 时用它——接受 NVIDIA 主导的 GPU 运维和快速迭代的代码库。 | Apache-2.0 | A（5/6） | [中](categories/llm-inference/serving-engines/vllm.zh.md) · [EN](categories/llm-inference/serving-engines/vllm.md) |
| **SGLang** | 当 agent 流量反复带着同一段长提示、又要求输出符合 JSON schema，需要前缀缓存和结构化生成来省 GPU 时间时用它——但 v0.5.20 起要求 CUDA 13，生态和生产记录也比 vLLM 年轻。 | Apache-2.0 | A（5/6） | [中](categories/llm-inference/serving-engines/sglang.zh.md) · [EN](categories/llm-inference/serving-engines/sglang.md) |
| **Ray Serve** | 当排序器、分类器、大模型等多个模型要在一个 Python 应用里组合、各自跨 CPU 和 GPU 节点扩缩，最好团队本来就在跑 Ray 时用它——但只服务一个大模型时，它只多出一个集群，不会更快。 | Apache-2.0 | A（6/6） | [中](categories/llm-inference/serving-engines/ray-serve.zh.md) · [EN](categories/llm-inference/serving-engines/ray-serve.md) |
| **llama.cpp** | 当你想要那个无依赖的 C/C++ 上游引擎、跑在目前最宽的硬件矩阵上、既能嵌入也能本地起服务时用它——接受没有 semver、没有模型管理、只有 flag 级 API。 | MIT | A（6/6） | [EN](categories/llm-inference/local-runtimes/llama-cpp.md) · [中](categories/llm-inference/local-runtimes/llama-cpp.zh.md) |
| **Ollama** | 当你想要托管的本地模型仓库，配 OpenAI/Anthropic 兼容 API、Docker 部署与客户端 SDK 时用它——接受包装层的参数子集、4096 token 的默认上下文，以及没有服务级批处理。 | MIT | A（5/6） | [EN](categories/llm-inference/local-runtimes/ollama.md) · [中](categories/llm-inference/local-runtimes/ollama.zh.md) |
| **BentoML** | 当你要把非聊天类模型或多模型流水线连同自定义 Python 前后处理，打包成带批处理的 HTTP 接口和容器镜像时用它——但自 2026 年被 Modular 收购后开发放缓，Kubernetes operator Yatai 也已归档。 | Apache-2.0 | B（6/6） | [EN](categories/llm-inference/serving-engines/bentoml.md) · [中](categories/llm-inference/serving-engines/bentoml.zh.md) |
| **LMDeploy** | 当你要在受限或老旧的 GPU、消费级显卡或昇腾等国产加速卡上，用一个命令行把 7B 到 70B 的开源模型量化到 4-bit 再对外服务时用它——但它仍是 0.x，小版本就带重构，生态也比 vLLM 小。 | Apache-2.0 | A（6/6） | [EN](categories/llm-inference/serving-engines/lmdeploy.md) · [中](categories/llm-inference/serving-engines/lmdeploy.zh.md) |
| **Text Generation Inference (TGI)** | 仅当你要维持一套已 pin 住的 TGI 部署、同时规划迁移，或想研读它的批处理服务设计时用它——Hugging Face 已在 2025-12 将其转入维护模式并归档仓库，不会再有新模型支持和安全修复。 | Apache-2.0 | C（6/6） | [EN](categories/llm-inference/serving-engines/text-generation-inference.md) · [中](categories/llm-inference/serving-engines/text-generation-inference.zh.md) |
| **Magnitude** | 当机器能力未知、你要下载前的速度与内存估算加一键接入已有 coding harness 时用它——接受一个两个月大、单厂商所有、且在 Apple Silicon 上报告比 llama.cpp 慢约 6 倍的仓库。 | Apache-2.0 | B（6/6） | [EN](categories/llm-inference/local-runtimes/magnitude.md) · [中](categories/llm-inference/local-runtimes/magnitude.zh.md) |
| **Shimmy** | 当磁盘上已有 GGUF 文件、想要单个 Rust 二进制给出 OpenAI／Ollama／Anthropic 兼容 API 时用它——接受一个刚满一年、单人维护、引擎只认证 26 个模型加量化组合的项目。 | Apache-2.0 | B（6/6） | [EN](categories/llm-inference/local-runtimes/shimmy.md) · [中](categories/llm-inference/local-runtimes/shimmy.zh.md) |
| **Airframe** | 当要在自己的 Rust 程序里内嵌 GGUF 推理、且要纯 Rust 构建加一种着色器语言覆盖全显卡（WebGPU）时用它——接受一个约六个月大、单贡献者、只认证 12 个架构家族且含 pending 专利子系统的引擎。 | MIT | C（4/6） | [EN](categories/llm-inference/local-runtimes/airframe.md) · [中](categories/llm-inference/local-runtimes/airframe.zh.md) |
| **FreeToken** | 当一台 NVIDIA 台式机要把比显存还大的 MoE 模型提供给你的编程智能体时用它——专家放内存、显卡只做缓存——接受一个约两个月大、只支持 Linux 加 NVIDIA、接口无鉴权的 v0.1.x 引擎。 | Apache-2.0 | B（6/6） | [EN](categories/llm-inference/local-runtimes/freetoken.md) · [中](categories/llm-inference/local-runtimes/freetoken.zh.md) |
| **Claude Code Local** | 当 Claude Code 额度用完或代码不许上云、想让同一个 `claude` 会话改由 Apple Silicon Mac 上的本地模型回答时用它——接受一个约六个月大、一人维护、一次只服务一个用户、默认用 abliterated 模型的仓库。 | MIT | B（6/6） | [EN](categories/llm-inference/local-runtimes/claude-code-local.md) · [中](categories/llm-inference/local-runtimes/claude-code-local.zh.md) |
| **DwarfStar (ds4)** | 当你有一台 96 GB 以上的 Mac、DGX Spark 或 Strix Halo 主机，想让少数几个前沿 MoE 模型（DeepSeek V4、GLM 5.x、Qwen3.8）在本地驱动编程智能体、内存不够时溢出到固态硬盘时用它——接受一个五个月大、单人维护、没有发布版本、只认自家 GGUF 文件的引擎。 | MIT | B（6/6） | [EN](categories/llm-inference/local-runtimes/ds4.md) · [中](categories/llm-inference/local-runtimes/ds4.zh.md) |
| **Edge0** | 当你想在 16–24 GB 的 Mac（或手机）上跑 35B 档的 MoE 模型、卡住你的是内存而不是模型选择时用它——专家从固态硬盘流式读取，并由训练过的预测器提前一步取来——接受只有两个预览模型、相对 fp16 有少量精度损失、以及一个只有一个月大且没有发布版本的仓库。 | Apache-2.0 | C（6/6） | [EN](categories/llm-inference/local-runtimes/edge0.md) · [中](categories/llm-inference/local-runtimes/edge0.zh.md) |
| **XGrammar** | 当你掌握模型的 logits、必须保证输出可解析——JSON Schema、正则、语法或工具调用——且要尽可能低的掩码延迟时用它；只调托管 API、或已在集成它的引擎上服务时不必用。 | Apache-2.0 | B（6/6） | [EN](categories/llm-inference/structured-generation/xgrammar.md) · [中](categories/llm-inference/structured-generation/xgrammar.zh.md) |
| **SIE (Superlinked Inference Engine)** | 当一条 agent 流水线要把许多小模型（向量、重排、OCR、抽取、审核）放在同一个 API 后面、按需加载并用 Helm／KEDA 集群扩缩时用它——接受一个约 6 个月大、单厂商维护、minor 版本常带破坏性变更的 0.x 代码库。 | Apache-2.0 | B（6/6） | [中](categories/llm-inference/serving-engines/sie.zh.md) · [EN](categories/llm-inference/serving-engines/sie.md) |
| **llm-d** | 当 Kubernetes 上一批 vLLM／SGLang pod 需要懂大模型的路由（按前缀缓存和排队派单）、预填充／解码拆分或 KV 缓存卸载，并想直接用跑过基准的 Helm／kustomize 配方时用它——接受一个年轻的 1.0 前 CNCF Sandbox 技术栈、较重的集群运维和版本间频繁的组件变动。 | Apache-2.0 | B（5/6） | [中](categories/llm-inference/serving-engines/llm-d.zh.md) · [EN](categories/llm-inference/serving-engines/llm-d.md) |
| **InferenceX** | 当你要为前沿模型选 GPU 或推理引擎，想看持续重跑、能追溯到配方的 NVIDIA 与 AMD 吞吐—延迟曲线时用它；要测自己的服务（完整流水线需要 Slurm GPU 集群）或需要联盟审计过的结果时别用。 | Apache-2.0 | B（6/6） | [中](categories/llm-inference/inference-benchmarks/inferencex.zh.md) · [EN](categories/llm-inference/inference-benchmarks/inferencex.md) |

### task-queue

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **XXL-JOB** | 当 Java/Spring 团队需要中心化、可视化、分片的定时作业调度时用它——注意 GPL-3.0 与中心调度器单点。 | GPL-3.0 | C（6/6） | [中](categories/task-queue/xxl-job.zh.md) · [EN](categories/task-queue/xxl-job.md) |
| **Celery** | 当 Python 应用需要把异步/后台任务规模化外包时用它——代价是要跑 broker + worker。 | BSD-3-Clause | A（6/6） | [中](categories/task-queue/celery.zh.md) · [EN](categories/task-queue/celery.md) |
| **Kombu** | 当 Python 服务要在可替换 broker（RabbitMQ、Redis、SQS）间收发消息时用它——虚拟 transport 对 AMQP 的模拟并不完整，换 URL 不等于行为一致。 | BSD-3-Clause | B（6/6） | [中](categories/task-queue/kombu.zh.md) · [EN](categories/task-queue/kombu.md) |
| **Flower** | 当生产 Celery 集群需要实时面板查看、控制 worker 并导出 Prometheus 指标时用它——它能撤销任务，绝不能无鉴权暴露。 | BSD-3-Clause | B（6/6） | [中](categories/task-queue/flower.zh.md) · [EN](categories/task-queue/flower.md) |
| **RQ** | 当 Python 应用已有 Redis 或 Valkey，并需要小而易读的队列加 worker 模型时用它——接受仅 Redis 系传输和另行运维 worker。 | BSD-2-Clause | B（5/6） | [中](categories/task-queue/rq.zh.md) · [EN](categories/task-queue/rq.md) |
| **Dramatiq** | 当 Python 服务想要 actor 式后台处理、并真的能在 RabbitMQ 与 Redis 之间选时用它——前提是能接受 LGPL-3.0 的分发义务。 | LGPL-3.0-or-later | B（6/6） | [中](categories/task-queue/dramatiq.zh.md) · [EN](categories/task-queue/dramatiq.md) |
| **arq** | 当应用已经 asyncio-first、一个小的 Redis 协程队列就够时用它——README 自称 maintenance-only，因此按「稳定但不再演进」预期。 | MIT | B（6/6） | [中](categories/task-queue/arq.zh.md) · [EN](categories/task-queue/arq.md) |
| **PowerJob** | 当 JVM 团队需要带 Web 控制台、支持 DAG 与 map-reduce 的集中式调度/计算平台时用它——稳定版自 2025-08 起未再发版。 | Apache-2.0 | C（3/6） | [中](categories/task-queue/powerjob.zh.md) · [EN](categories/task-queue/powerjob.md) |
### im-automation

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **ItChat** | 仅当你要读懂或接手基于它扫码登录、msg_register 接口写成的老微信机器人代码时用它——它自 2018 年起已废弃，所依赖的网页版微信登录对绝大多数账号已关停，用个人号跑还有封号风险。 | MIT | C（4/6） | [中](categories/im-automation/wechat/itchat.zh.md) · [EN](categories/im-automation/wechat/itchat.md) |
| **WeChatPlugin-MacOS** | 仅当你在 Mac 上把微信刻意钉在 2.3–3.7 这类老版本、想找回防撤回、自动回复和多开时用它——它给 WeChat.app 二进制打补丁，微信每更新一次就坏一次，已约 3 年半没有提交，还有封号风险。 | MIT | D（4/6） | [中](categories/im-automation/wechat/wechatplugin-macos.zh.md) · [EN](categories/im-automation/wechat/wechatplugin-macos.md) |
| **wxpy** | 仅当你要读懂或接手 2017–2019 年用它更顺手的 Bot／Friend／Group 接口写成的微信机器人代码时用它——仓库已归档，它架在 ItChat 的网页版微信登录上，绝大多数账号已登不上，个人号自动化还有封号风险。 | MIT | D（5/6） | [中](categories/im-automation/wechat/wxpy.zh.md) · [EN](categories/im-automation/wechat/wxpy.md) |
| **wxappUnpacker** | 仅当你要反编译自有小程序的 .wxapkg 包、需要顺藤找到 wxappUnpacker 这一系工具时把它当线索——本仓库已清空成只剩一个词的 README，整条血缘都已废弃，留存的 fork 还依赖已弃用的 vm2 沙箱。 | NONE (no LICENSE file; the forks' package.json declare GPL-3.0-or-later) | E（3/6） | [中](categories/im-automation/wechat/wxappunpacker.zh.md) · [EN](categories/im-automation/wechat/wxappunpacker.md) |
| **Douyin-Bot** | 仅当你想读一个用 Python 经 ADB 驱动安卓真机（截屏、打分、滑动／点击）的小巧示例时用它——它自 2020 年起已死，硬编码 2018 年抖音界面坐标，依赖的腾讯人脸 API 也已下线，切勿部署。 | MIT | D（3/6） | [中](categories/im-automation/douyin-bot.zh.md) · [EN](categories/im-automation/douyin-bot.md) |
| **WeChat Bot** | 当一个 Node CLI 必须把微信、飞书、Telegram 与 WhatsApp 接到多个 LLM 时用它——个人微信仍走非官方通道，并伴随账号风险。 | MIT | B（5/6） | [中](categories/im-automation/wechat/wechat-bot.zh.md) · [EN](categories/im-automation/wechat/wechat-bot.md) |
| **ChatGPT-wechat-bot** | 仅把它当作 2022 至 2023 年 Wechaty 与 ChatGPT 的小型参考代码——项目已停滞、默认配置过时，不适合作为生产底座。 | MIT | D（3/6） | [中](categories/im-automation/wechat/chatgpt-wechat-bot.zh.md) · [EN](categories/im-automation/wechat/chatgpt-wechat-bot.md) |
| **OpeniLink Hub** | 当多个 iLink 微信 Bot 需要自托管管理、trace、Webhook 和 App 时用它——项目年轻且无官方关联，还扩大了认证与 Registry 信任边界。 | MIT | B（6/6） | [中](categories/im-automation/openilink-hub.zh.md) · [EN](categories/im-automation/openilink-hub.md) |
| **Dify Enterprise WeChat Bot** | 仅用于维持固定 Windows 企业微信到 Dify 的桌面集成——项目已停滞、包含闭源 helper，Workflow 支持也未完成。 | NOASSERTION | C（3/6） | [中](categories/im-automation/wechat/dify-enterprise-wechat-bot.zh.md) · [EN](categories/im-automation/wechat/dify-enterprise-wechat-bot.md) |
| **Wechaty** | 许多个人号机器人背后的多语言可复用框架：adapter 与命令层要自己掌控，押注某条通道前先确认各 provider 现状。 | Apache-2.0 | C（5/6） | [中](categories/im-automation/wechat/wechaty.zh.md) · [EN](categories/im-automation/wechat/wechaty.md) |
| **CowAgent** | Python-first、多通道、模型后端可插拔的助手；即更名后的 `zhayujie/chatgpt-on-wechat`，通道已换成 iLink，而非被删除的个人号路径。 | MIT | B（5/6） | [中](categories/im-automation/wechat/cowagent.zh.md) · [EN](categories/im-automation/wechat/cowagent.md) |
| **WeChatFerry** | 不要部署：维护者已归档，发版钉在旧版 Windows 微信上，整套方案是客户端注入。 | MIT | D（6/6） | [中](categories/im-automation/wechat/wechatferry.zh.md) · [EN](categories/im-automation/wechat/wechatferry.md) |
| **Dify on WeChat** | 端到端可源码审查的 Dify 到微信桥接——但自 2025-04 起没有代码变更，且仍带个人号通道风险。 | MIT | B（3/6） | [中](categories/im-automation/wechat/dify-on-wechat.zh.md) · [EN](categories/im-automation/wechat/dify-on-wechat.md) |
| **OpeniLink Go SDK** | 嵌进现有 Go 服务的原始 iLink 传输层：信任边界最小，持久化、认证、重试与运维由你承担。 | MIT | C（5/6） | [中](categories/im-automation/openilink-sdk-go.zh.md) · [EN](categories/im-automation/openilink-sdk-go.md) |
### web-ui

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Driver.js** | 当你想在网页上加一个极简、无依赖的产品引导/功能高亮时用它——不是完整的 onboarding 平台。 | MIT | B（5/6） | [中](categories/web-ui/product-tours/driver-js.zh.md) · [EN](categories/web-ui/product-tours/driver-js.md) |
| **Shepherd.js** | 当同一套引导要跑在 React、Angular 和纯 HTML 页面上，并且要等用户真的点了才前进时用它——但自 v14（2024-09）起，有营收的公司哪怕只是做内部看板也要买商业许可。 | AGPL-3.0 | B（4/6） | [中](categories/web-ui/product-tours/shepherd-js.zh.md) · [EN](categories/web-ui/product-tours/shepherd-js.md) |
| **Intro.js** | 当纯 HTML 或原生 JS 站点需要一套逐步聚光的引导，用 data 属性就能配置，还要自带多语言和主题时用它——但它是 AGPL-3.0，商业产品得买授权，眼下所有开发都出自一位贡献者。 | AGPL-3.0 | B（5/6） | [中](categories/web-ui/product-tours/intro-js.zh.md) · [EN](categories/web-ui/product-tours/intro-js.md) |
| **Vue.js** | 当偏后端的团队想用绑定响应式数据的类 HTML 模板，先在现有服务端页面里放一个组件、再逐步长成完整应用时用它——但在欧美招聘市场 React 更占优，路线图也很大程度压在尤雨溪一人身上。 | MIT | A（6/6） | [中](categories/web-ui/frameworks/view-frameworks/vue.zh.md) · [EN](categories/web-ui/frameworks/view-frameworks/vue.md) |
| **Svelte** | 当用户多在中端手机和不稳定网络上、框架运行时的体积成了问题，而团队更习惯写 HTML 和 CSS 时用它——但第三方生态和招聘池都远小于 React 和 Vue。 | MIT | A（6/6） | [中](categories/web-ui/frameworks/view-frameworks/svelte.zh.md) · [EN](categories/web-ui/frameworks/view-frameworks/svelte.md) |
| **shadcn/ui** | 当你用 Tailwind 起一个 React 新产品，想把精致、无障碍的组件以源码形式拷进仓库随意修改时用它——但每个拷进来的文件都归你维护，项目方向也倚重创建者一个人的判断。 | MIT | A（6/6） | [中](categories/web-ui/component-libraries/shadcn-ui.zh.md) · [EN](categories/web-ui/component-libraries/shadcn-ui.md) |
| **Angular** | 当大型 TypeScript 团队需要路由、表单、HTTP、依赖注入和 CLI 都来自同一个统一版本的框架，让各小组接法一致时用它——但对小应用是大材小用，回避 TypeScript 的团队也会一直别扭。 | MIT | A（6/6） | [中](categories/web-ui/frameworks/view-frameworks/angular.zh.md) · [EN](categories/web-ui/frameworks/view-frameworks/angular.md) |
| **Ant Design** | 当 React 中后台以可排序、可筛选的表格和复杂表单为主，又没有设计师，想要一套免费、完整、风格统一的组件时用它——但它只支持 React，v6 还要求 React 18 及以上。 | MIT | A（6/6） | [中](categories/web-ui/component-libraries/ant-design.zh.md) · [EN](categories/web-ui/component-libraries/ant-design.md) |
| **Lit** | 当一套设计系统要同时服务 React、Vue、Angular 和纯 HTML 应用，希望组件按标准自定义元素只发布一次时用它——但它是组件库不是应用框架，而且核心包自 2026 年 5 月以来发版放缓。 | BSD-3-Clause | A（6/6） | [中](categories/web-ui/frameworks/view-frameworks/lit.zh.md) · [EN](categories/web-ui/frameworks/view-frameworks/lit.md) |
| **React** | 当多页面应用需要按共享数据自动重渲染的组件，并且看重最大的生态、最深的招聘池和 React Native 这条移动端路线时用它——但它只是视图层，路由、取数和服务端渲染要靠框架补齐。 | MIT | A（6/6） | [中](categories/web-ui/frameworks/view-frameworks/react.zh.md) · [EN](categories/web-ui/frameworks/view-frameworks/react.md) |
| **Next.js** | 当 React 产品要服务端渲染出能被搜索引擎收录的页面，又想把后端路由放进同一套代码（交易市场、带公开页的 SaaS）时用它——但纯静态内容站用 Astro 更合适，路线图也由 Vercel 一家掌控。 | MIT | A（5/6） | [中](categories/web-ui/frameworks/app-frameworks/nextjs.zh.md) · [EN](categories/web-ui/frameworks/app-frameworks/nextjs.md) |
| **SvelteKit** | 当小团队想用 Svelte，并直接拿到目录即路由、服务端取数、渐进增强的表单，以及适配 Node、Serverless 或静态托管的 adapter 时用它——但 3.0（2026-10）是一次大规模破坏性发布，React 生态也接不进来。 | MIT | A（6/6） | [EN](categories/web-ui/frameworks/app-frameworks/sveltekit.md) · [中](categories/web-ui/frameworks/app-frameworks/sveltekit.zh.md) |
| **Reactour** | 当 React 应用需要一段分步引导或一次性高亮某个元素、希望由 React context 和 `useTour` hook 驱动、且要 MIT 许可时用它——但发版慢（`@reactour/tour` 最后一版是 2025-05 的 3.8.0），且只有一人维护。 | MIT | B（5/6） | [EN](categories/web-ui/product-tours/reactour.md) · [中](categories/web-ui/product-tours/reactour.zh.md) |
| **react-joyride** | 当 React 或 Next.js 应用需要首次引导，步骤要跟住晚挂载或会移动的组件、以 React portal 渲染时用它——但它只支持 React，实际只有一人维护，v2 代码不按指南迁移就升到 v3，引导会悄无声息地失效。 | MIT | B（6/6） | [EN](categories/web-ui/product-tours/react-joyride.md) · [中](categories/web-ui/product-tours/react-joyride.zh.md) |
| **Material UI (MUI)** | 当没有设计师的 React 团队要快速交付大量增删改查页面，并且能接受 Google Material Design 的长相时用它——但要做出辨识度强的品牌就得逐个组件覆盖样式，以 Tailwind 为主的技术栈还得同时维护两套样式体系。 | MIT | A（6/6） | [EN](categories/web-ui/component-libraries/material-ui.md) · [中](categories/web-ui/component-libraries/material-ui.zh.md) |
| **Chakra UI** | 当小团队用 React 或 Next.js 做有品牌感的 SaaS，想要无障碍组件、用样式属性从同一主题取值并内置暗色模式时用它——但样式仍由 Emotion 在运行时生成，也没有 Ant 那个级别的数据表格和表单引擎。 | MIT | A（6/6） | [EN](categories/web-ui/component-libraries/chakra-ui.md) · [中](categories/web-ui/component-libraries/chakra-ui.zh.md) |
| **Radix UI Primitives** | 当你在搭公司自己的 React 设计系统，需要行为、焦点、键盘和 ARIA 都做好但完全不带样式的下拉、弹窗、提示框时用它——但它没有组合框和日期选择器，维护几乎靠 WorkOS 的一个人，还刚经历近一年的停滞。 | MIT | A（6/6） | [EN](categories/web-ui/component-libraries/radix-ui.md) · [中](categories/web-ui/component-libraries/radix-ui.zh.md) |
| **Nuxt** | 当 Vue 团队需要服务端渲染、能被搜索引擎收录的页面，又想把接口写在同一项目的 `server/` 目录、部署到 Node、Serverless 或边缘时用它——但它只支持 Vue，而且 NuxtLabs 加入 Vercel 后，路线图的主人同时拥有 Next.js。 | MIT | A（6/6） | [EN](categories/web-ui/frameworks/app-frameworks/nuxt.md) · [中](categories/web-ui/frameworks/app-frameworks/nuxt.zh.md) |
| **Astro** | 当站点是内容集合、只需少数交互组件时用它——但交付物是带版本的文档站、或站点本质是全栈应用时不要用。 | MIT | A（5/6） | [中](categories/web-ui/frameworks/site-frameworks/astro.zh.md) · [EN](categories/web-ui/frameworks/site-frameworks/astro.md) |
| **Docusaurus** | 当需要第一天就有带版本、可搜索、支持 i18n 的文档站时用它——但站点是通用内容站、或你宁愿自己组装文档那套家具时不要用。 | MIT | B（6/6） | [中](categories/web-ui/frameworks/site-frameworks/docusaurus.zh.md) · [EN](categories/web-ui/frameworks/site-frameworks/docusaurus.md) |
| **Nextra** | 当文档必须活在既有 Next.js 应用里、一层薄 MDX 就够了时用它——但你需要版本化文档、或需要背后有较大维护团队的项目时不要用。 | MIT | B（6/6） | [中](categories/web-ui/frameworks/site-frameworks/nextra.zh.md) · [EN](categories/web-ui/frameworks/site-frameworks/nextra.md) |
| **TanStack Router** | 当 URL 就是应用的状态容器、写错的链接／参数／查询值必须在编译期报错而不是吓到用户时用它——但路由只是寥寥几页静态页面时不要用，需要 RSC 优先架构时选 Next.js。 | MIT | A（6/6） | [中](categories/web-ui/frameworks/app-frameworks/tanstack-router.zh.md) · [EN](categories/web-ui/frameworks/app-frameworks/tanstack-router.md) |
| **TanStack Bling** | 2023 年已归档的 Vite／Astro 插件，把 `server$(fn)` 编译成服务端接口＋浏览器端发请求的替身——只当设计参考，不当依赖；新应用用 TanStack Start 的 `createServerFn`、SolidStart 或 Next.js Server Actions。 | MIT | D（5/6） | [中](categories/web-ui/frameworks/app-frameworks/tanstack-bling.zh.md) · [EN](categories/web-ui/frameworks/app-frameworks/tanstack-bling.md) |
| **TanStack Redact** | 当 Vite＋React 应用的包体积预算被约 69 KB、页面却用不到的 React 运行时吃掉时用它——一个插件把所有 React 导入换成约 23 KB 的同步重新实现——但应用依赖并发特性、构建工具不是 Vite、或需要许可证文件（目前没有）时不要用。 | NOASSERTION | D（6/6） | [中](categories/web-ui/frameworks/view-frameworks/tanstack-redact.zh.md) · [EN](categories/web-ui/frameworks/view-frameworks/tanstack-redact.md) |
| **theSVG** | 需要从一份清单里拿大量品牌 logo（彩色版、文字标、AI 厂商）和 AWS／Azure／GCP 架构图标，形式是带类型的组件、CDN 地址或命令行时用它——但许可证要自己逐个核对，Azure 图标标成 MIT 与微软条款不符。 | MIT | B（6/6） | [中](categories/web-ui/icon-libraries/thesvg.zh.md) · [EN](categories/web-ui/icon-libraries/thesvg.md) |
| **TanStack Query** | 前端组件各自手写请求、loading、error，写完还显示旧数据时用它——按键共享的服务端状态缓存，后台自动重拉、写后失效；它不是客户端状态库，也不是按实体归一化的 GraphQL 缓存。 | MIT | A（5/6） | [中](categories/web-ui/data-fetching/tanstack-query.zh.md) · [EN](categories/web-ui/data-fetching/tanstack-query.md) |
| **TanStack Form** | 表单里每个输入手写状态、touched 和异步校验防抖时用它——无头、带类型的表单 store，字段级和表单级校验，覆盖 React、Vue、Angular、Solid、Svelte、Lit；v2（alpha）会改日常 API。 | MIT | A（6/6） | [中](categories/web-ui/forms/tanstack-form.zh.md) · [EN](categories/web-ui/forms/tanstack-form.md) |
| **TanStack Virtual** | 几千上万行的列表、表格或聊天流挂载慢、滚动卡时用它——无头虚拟器只渲染可见行、标签由你自己写，测量动态行高，能为聊天贴底；它不是现成的列表组件，行数受浏览器元素最大高度限制（约百万行）。 | MIT | A（6/6） | [中](categories/web-ui/virtualization/tanstack-virtual.zh.md) · [EN](categories/web-ui/virtualization/tanstack-virtual.md) |
| **TanStack Store** | 框架无关的库或应用核心需要一份带派生值的响应式 store，再用 React、Vue、Angular、Solid、Svelte、Preact、Lit 的薄适配层只在选中那块变了时重渲染；仍是 0.x，小版本会破坏兼容，没有持久化和 devtools。 | MIT | A（6/6） | [中](categories/web-ui/state-management/tanstack-store.zh.md) · [EN](categories/web-ui/state-management/tanstack-store.md) |
| **TanStack Persist** | 界面状态一刷新就丢、每个功能都在重写 localStorage 的读、解析、存循环时用它——useState 形状的持久化状态钩子，带版本失效、maxAge 过期和子集选择，只面向 Web Storage；仅限观察名单：npm 上没有包、没有 release，成段文档是从兄弟仓库复制的，宣称的跨标签页同步没有接线。 | MIT | C（5/6） | [中](categories/web-ui/state-management/tanstack-persist.zh.md) · [EN](categories/web-ui/state-management/tanstack-persist.md) |
| **TanStack Charts** | 现成图表组件画不出你要的自定义图层、同一张图又要在多个框架和服务端渲染时用它——一份带类型的“标记加比例尺”定义，自带服务端 SVG、键盘焦点和按需 Canvas；它是 Alpha（0.x，小版本会破坏兼容），才两个月大，代码主要出自一位作者。 | MIT | B（6/6） | [中](categories/web-ui/charts/tanstack-charts.zh.md) · [EN](categories/web-ui/charts/tanstack-charts.md) |
| **TanStack React Charts** | 只在迁移前让 React DOM 应用里已有的 `react-charts` 集成继续活着时用它——序列数组加 `getValue` 轴取值函数，D3 计算、画成带 Voronoi 悬停的 SVG；2025 年已归档，v3 仍是 beta，React 18/Next.js 下的提示框问题没人修，新图请用仍在维护的库。 | MIT | D（5/6） | [中](categories/web-ui/charts/tanstack-react-charts.zh.md) · [EN](categories/web-ui/charts/tanstack-react-charts.md) |
| **TanStack Hotkeys** | 手写的 keydown 判断在 Mac 的 Cmd 和 Ctrl 上出错、用户打字时误触发、没法录制和显示用户改的键时用它——带类型的 `Mod+S` 绑定、连按、录制器和格式化工具，有 React、Vue、Angular、Solid、Svelte、Preact、Lit 适配；alpha 期 0.x，小版本会破坏兼容，只发 ESM。 | MIT | B（6/6） | [中](categories/web-ui/keyboard-shortcuts/tanstack-hotkeys.zh.md) · [EN](categories/web-ui/keyboard-shortcuts/tanstack-hotkeys.md) |
| **TanStack Pacer** | 搜索框、自动保存、滚动处理都靠手写 setTimeout/clearTimeout 裹着时用它——带类型的防抖／节流／限流／排队／批处理，同步异步（重试／中止）两套变体，pending 状态可经 TanStack Store 渲染；它不是服务端配额，且 0.x beta 有 API 变动风险。 | MIT | A（6/6） | [中](categories/web-ui/scheduling/tanstack-pacer.zh.md) · [EN](categories/web-ui/scheduling/tanstack-pacer.md) |
| **TanStack Time** | 产品日历要重复日程、拖拽改时长、超订校验，而 DOM 必须归你时关注它——无头、Temporal 原生的核心算日期网格、重复展开和冲突；仅列观察名单：未发布的 pre-alpha，npm 上还没有包。 | MIT | D（4/6） | [中](categories/web-ui/component-libraries/tanstack-time.zh.md) · [EN](categories/web-ui/component-libraries/tanstack-time.md) |


| **TanStack DB** | 每个视图都要求单开联表接口、每次写操作都要手补查询缓存时用它——客户端规范化集合加差分数据流活查询和乐观事务；beta 0.x，不是客户端状态库，也不是持久离线数据库。 | MIT | B（6/6） | [中](categories/web-ui/data-fetching/tanstack-db.zh.md) · [EN](categories/web-ui/data-fetching/tanstack-db.md) |
| **TanStack Ranger** | 滑块要双把手、不规则步进数组或对数刻度推子，而标记必须完全归你时用它——无头数值引擎管拖拽跟踪、吸附、刻度和百分比，不渲染任何东西；目前只有 React 适配层，API 仍是 0.x。 | MIT | C（5/6） | [中](categories/web-ui/component-libraries/tanstack-ranger.zh.md) · [EN](categories/web-ui/component-libraries/tanstack-ranger.md) |
| **TanStack Select** | 想要一个 TanStack 式、能搜索多选的无头下拉引擎时关注它——今天不可用：`main` 是空脚手架加 2026-08 的重写 RFC，npm 上没有包；唯一发布过的是停更、无 ARIA、只支持 React 16 的旧 hook `use-select`。 | MIT | — | [中](categories/web-ui/component-libraries/tanstack-select.zh.md) · [EN](categories/web-ui/component-libraries/tanstack-select.md) |
| **TanStack Table** | 表格要排序、过滤、分页、分组、选行，但 `<table>` 的 DOM 和样式必须完全归你时用它——无头引擎管状态和行模型；它不交付标记、不取数、不带虚拟滚动。 | MIT | A（6/6） | [中](categories/web-ui/component-libraries/tanstack-table.zh.md) · [EN](categories/web-ui/component-libraries/tanstack-table.md) |

### proxy-pool

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **proxy_pool** | 当业余或研究用的爬虫老被封 IP、你想自托管一个免费代理池，让它爬取、校验并通过 Redis 支撑的 HTTP API 吐出可用 IP 时用它——但免费代理又慢又短命且不可信，绝不要让敏感流量经过。 | MIT | C（5/6） | [中](categories/proxy-pool/proxy-pool.zh.md) · [EN](categories/proxy-pool/proxy-pool.md) |
| **ProxyBroker** | 当低风险原型需要临时找一批免费代理、检查匿名度并经一个本地轮换端点提供时用它——但它自 2019-03 起休眠，据报在新版 Python 上不钉死环境普遍跑不起来。 | Apache-2.0 | D（4/6） | [中](categories/proxy-pool/proxybroker.zh.md) · [EN](categories/proxy-pool/proxybroker.md) |
| **Scylla** | 当你想用一条 `docker run` 起一个常驻免费代理服务、通过 JSON API 按 HTTPS 支持、匿名度和国家筛选并带看板时用它——但内置正向代理不支持 HTTPS，发版自 2022 年起停滞。 | Apache-2.0 | D（4/6） | [中](categories/proxy-pool/scylla.zh.md) · [EN](categories/proxy-pool/scylla.md) |
| **haipproxy** | 当多台机器上的大量爬虫需要一个分布式、高可用的免费代理池，并想把收割、校验、调度在 Scrapy + Redis 上解耦时用它——但它自 2019-07 起休眠，跑的是 Python 2/3 过渡期代码，且是最重的代理池。 | MIT | D（4/6） | [中](categories/proxy-pool/haipproxy.zh.md) · [EN](categories/proxy-pool/haipproxy.md) |
### debugging-proxy

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **whistle** | 当 web/移动开发者要通过规则化 Web UI 抓取、检查、改写并 mock HTTP(S)/WebSocket 流量时用它——是开发调试代理，不是生产网关或爬虫代理池。 | MIT | B（6/6） | [中](categories/debugging-proxy/whistle.zh.md) · [EN](categories/debugging-proxy/whistle.md) |
| **AnyProxy** | 当你调试 app 流量、想要一个用纯 JavaScript 规则文件改写请求和响应的 Node.js 中间人代理时用它——但 master 自 2020 年起冻结，新项目请优先选 whistle。 | Apache-2.0 | C（4/6） | [中](categories/debugging-proxy/anyproxy.zh.md) · [EN](categories/debugging-proxy/anyproxy.md) |
| **mitmproxy** | 当你要看清并改写一个你控制不了的客户端发出的 HTTPS 请求、还想用 Python 写脚本处理时用它——但做了证书固定的 App 会拒绝它，得先去固定。 | MIT | A（6/6） | [EN](categories/debugging-proxy/mitmproxy.md) · [中](categories/debugging-proxy/mitmproxy.zh.md) |

### web-scraping

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **newspaper** | 用来从新闻 URL 批量提取正文、作者和元数据——但原版（newspaper3k）已陈旧，活跃路径是 newspaper4k 分叉。 | MIT | B（5/6） | [中](categories/web-scraping/article-extraction/newspaper.zh.md) · [EN](categories/web-scraping/article-extraction/newspaper.md) |
| **requests-html** | 当你在维护一个已经用它、靠一个 `requests` 风格对象完成抓取和 CSS 选择服务端渲染 HTML 的旧脚本时用它——但它自 2019 年起没发过版，JS 渲染还依赖无人维护的 pyppeteer。 | MIT | D（3/6） | [中](categories/web-scraping/crawling-tools/requests-html.zh.md) · [EN](categories/web-scraping/crawling-tools/requests-html.md) |
| **Firecrawl** | 当你的 agent 或 RAG 入库要把 URL、搜索结果或整站变成干净的 Markdown 或 JSON，又不想自己扛渲染、代理和爬取队列时用它——但自托管拿不到只在云上的反爬、页面动作和 Agent，核心还是 AGPL-3.0。 | AGPL-3.0 | B（6/6） | [中](categories/web-scraping/crawling-tools/firecrawl.zh.md) · [EN](categories/web-scraping/crawling-tools/firecrawl.md) |
| **Claude Code Skill Scrapling** | 当你想让 Python 机器上的 Claude Code agent 在遇到 Cloudflare 403 后自己从普通请求升级到隐身浏览器、而不是瞎猜时用它——但它是只有四次提交的单人封装，速查卡已和当前 Scrapling 脱节；库自带的官方 skill 才是有人维护的那份。 | MIT | C（4/5） | [中](categories/web-scraping/crawling-tools/claude-code-skill-scrapling.zh.md) · [EN](categories/web-scraping/crawling-tools/claude-code-skill-scrapling.md) |
| **Scrapling** | 当 Python 爬虫被 Cloudflare 拦住、或网站一改版就坏时用它——隐身 Chromium 抓取器、按相似度找回元素的自适应选择器和类 Scrapy 的爬虫层集于一个包；只对付 Cloudflare，0.x 常有破坏性变更，单人维护。 | BSD-3-Clause | B（6/6） | [中](categories/web-scraping/crawling-tools/scrapling.zh.md) · [EN](categories/web-scraping/crawling-tools/scrapling.md) |
| **trafilatura** | 当你要从几千个管不了的网站页面里抽出正文、标题、作者和日期，又不想按站点写选择器时用它——但它只处理原始 HTML，JavaScript 渲染或被反爬拦截的页面要先用浏览器或隐身抓取器下载。 | Apache-2.0 | A（6/6） | [EN](categories/web-scraping/article-extraction/trafilatura.md) · [中](categories/web-scraping/article-extraction/trafilatura.zh.md) |

### auth

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Authomatic** | 当 Flask、Django 或其他 WSGI 应用需要一层轻薄的“用 Google／GitHub 登录”，横跨 OAuth 1.0a、OAuth 2.0 和 OpenID、会话由你自己管时用它——但发版停在 2024 年的 1.3.0，尚未发布的 2.0 还要移除 OAuth 1.0a。 | MIT | C（5/6） | [中](categories/auth/authomatic.zh.md) · [EN](categories/auth/authomatic.md) |
| **django-rules** | 当 Django 的对象级权限由逻辑决定（如“作者能改自己的帖子”）、你想用可组合的谓词且不加数据库表时用它——但若管理员要在运行时逐对象授权，请用 django-guardian。 | MIT | B（4/6） | [中](categories/auth/django-rules.zh.md) · [EN](categories/auth/django-rules.md) |
| **Keycloak** | 当一堆应用各有各的登录，你想用一台自托管服务器统一处理密码、二次验证、社交和 SAML 登录，并签发带角色的令牌时用它——但它要运维 JVM、数据库和缓存，只有一个应用时太重。 | Apache-2.0 | A（6/6） | [EN](categories/auth/keycloak.md) · [中](categories/auth/keycloak.zh.md) |
| **Casbin** | 当角色判断散落在各个处理函数里，你想用一份模型文件加一张策略表、在进程内一次库调用完成鉴权，Go 或其他七种语言都行时用它——但它不做身份认证，策略集也必须装得进应用内存。 | Apache-2.0 | B（6/6） | [EN](categories/auth/casbin.md) · [中](categories/auth/casbin.zh.md) |
| **OpenFGA** | 当访问权限顺着关系走（文件夹分享给团队、编辑权限沿目录树继承），横跨好几个服务，“列出 Anne 能看到的一切”已经超时时用它——但每次成员或分享变化都得同步写成元组，漏写就会给出错误答案。 | Apache-2.0 | A（6/6） | [EN](categories/auth/openfga.md) · [中](categories/auth/openfga.zh.md) |

### databases

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **PikiwiDB** | 当大规模 Redis 数据集撑爆内存、内存成本成为主要负担时用它——RocksDB 落盘、兼容 Redis 协议，单节点可存数百 GB；但它以延迟换容量，若每次操作都要微秒级则不合适。 | BSD-3-Clause | B（6/6） | [中](categories/databases/database-engines/pikiwidb.zh.md) · [EN](categories/databases/database-engines/pikiwidb.md) |
| **elasticsearch-dsl-py** | 只在阅读或迁移锁定 elasticsearch-dsl 8.17 及更老版本的遗留代码时用它——但它已归档；新代码请装 `elasticsearch>=8.18` 并改用 `elasticsearch.dsl`。 | Apache-2.0 | C（5/6） | [中](categories/databases/database-clients/elasticsearch-dsl-py.zh.md) · [EN](categories/databases/database-clients/elasticsearch-dsl-py.md) |
| **elasticsearch-sql** | 当熟悉 SQL 的团队想免学 JSON Query DSL 直接查 Elasticsearch 时用它——但 Elastic 官方的 SQL／ES\|QL 已与之重叠，能覆盖你的需求时优先用官方特性。 | Apache-2.0 | C（5/6） | [中](categories/databases/database-clients/elasticsearch-sql.zh.md) · [EN](categories/databases/database-clients/elasticsearch-sql.md) |
| **go-mysql-elasticsearch** | 当你要一个单独的 Go 进程，先把 MySQL dump 进 Elasticsearch、再 tail binlog 做单向同步时用它——但它自 2020 年起无人维护，只支持 MySQL 8.0 以下和 ES 6.0 以下。 | MIT | D（4/6） | [中](categories/databases/data-sync/go-mysql-elasticsearch.zh.md) · [EN](categories/databases/data-sync/go-mysql-elasticsearch.md) |
| **python-mysql-replication** | 当你想用纯 Python 原语把 MySQL binlog 流式解析成带类型的事件、自建可控 CDC 循环时用它——但 checkpoint、去重和精确一次投递全得你自己负责。 | Apache-2.0 | B（4/6） | [中](categories/databases/data-sync/python-mysql-replication.zh.md) · [EN](categories/databases/data-sync/python-mysql-replication.md) |
| **PrettyZoo** | 当你想用桌面 GUI 浏览、轻量编辑 ZooKeeper 的 znode 树、节点数据和 ACL，而不想敲 `zkCli.sh` 时用它——但它已归档，作者 2024-01 宣布停止维护。 | Apache-2.0 | D（5/6） | [中](categories/databases/database-clients/prettyzoo.zh.md) · [EN](categories/databases/database-clients/prettyzoo.md) |
| **RDR** | 当 Redis 撞上 maxmemory、你要离线解析 RDB 快照找出吃内存的 key 前缀、又不想给生产加负载时用它——但它自 2020 年起冻结，内存数字也只是近似值。 | Apache-2.0 | D（4/6） | [中](categories/databases/database-clients/rdr.zh.md) · [EN](categories/databases/database-clients/rdr.md) |
| **MCP Toolbox for Databases** | 当生产 agent 要查多种数据库（57 种数据源、Google Cloud 一等公民），且只能走你在 YAML 里声明的参数化语句时用它——但引擎级只读只在 Cloud SQL／AlloyDB／BigQuery 上有，网络默认值也偏宽松。 | Apache-2.0 | A（6/6） | [中](categories/databases/database-clients/mcp-toolbox.zh.md) · [EN](categories/databases/database-clients/mcp-toolbox.md) |
| **Supabase** | 当小团队这个月就要在同一个 Postgres 上拿到认证、自动生成的 API、文件存储和实时更新，并用行级安全做权限时用它——但生产自托管必须有人负责：自托管包只有社区支持，默认配置不安全。 | Apache-2.0 | A（5/6） | [中](categories/databases/database-engines/supabase.zh.md) · [EN](categories/databases/database-engines/supabase.md) |
| **DuckDB** | 当一个脚本、notebook 或 CI 任务要对本地或 S3 上的 Parquet/CSV 直接做快速 SQL 关联和聚合、又不想起服务端时用它——但多个进程要同时写同一个库，或数据超出一台机器时不适合。 | MIT | A（5/6） | [EN](categories/databases/database-engines/duckdb.md) · [中](categories/databases/database-engines/duckdb.zh.md) |
| **ClickHouse** | 当团队要在自托管服务端上，对几亿行以追加为主的事件数据做亚秒级 SQL 聚合、供很多人同时看板时用它——但不适合频繁单行更新的事务负载、不攒批的逐行写入，或一台笔记本单进程用 DuckDB 就能搞定的数据量。 | Apache-2.0 | A（5/6） | [EN](categories/databases/database-engines/clickhouse.md) · [中](categories/databases/database-engines/clickhouse.zh.md) |
| **DBeaver** | 当你要在 Postgres、SQL Server、Oracle、ClickHouse、SQLite 之间来回切，想用一个免费桌面客户端给它们统一配上编辑器、数据表格和 ER 图时用它——但 NoSQL 驱动只在 Pro 版，它也是个偏重的单用户 Eclipse 应用。 | Apache-2.0 | A（6/6） | [EN](categories/databases/database-clients/dbeaver.md) · [中](categories/databases/database-clients/dbeaver.zh.md) |
| **Debezium** | 当搜索索引、缓存或其他服务要跟着一个业务数据库走，而双写或按 `updated_at` 轮询总是不一致、漏掉删除时用它——但默认部署意味着要运维 Kafka 和 Kafka Connect。 | Apache-2.0 | A（5/6） | [EN](categories/databases/data-sync/debezium.md) · [中](categories/databases/data-sync/debezium.zh.md) |
| **Valkey** | 当缓存、会话和限流都跑在 Redis 上，而 Redis 改许可后你需要一个 BSD 许可、厂商中立、可直接替换的版本时用它——但要用 Redis 8 最新的内置功能，或数据集大于内存时不适合。 | BSD-3-Clause | A（6/6） | [EN](categories/databases/database-engines/valkey.md) · [中](categories/databases/database-engines/valkey.zh.md) |
| **Turso Database** | 已经把数据放在 SQLite 文件里的应用、agent 或边缘服务，想要异步 I/O、实验性的多写者 MVCC 或向量检索时用它（Rust 重写版）——但它还没到 1.0、只支持单进程，也还不是完整的 SQLite 超集。 | MIT | A（6/6） | [中](categories/databases/database-engines/turso.zh.md) · [EN](categories/databases/database-engines/turso.md) |

### secrets-management

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **OpenBao** | 需要在 HashiCorp 改 Vault 许可证之后、用 MPL 自托管一套按身份把关的密钥服务端时用它——但它是你自己运维的 Raft／Postgres 集群，不是每个 Vault 插件的即插即用替代。 | MPL-2.0 | B（6/6） | [中](categories/secrets-management/openbao.zh.md) · [EN](categories/secrets-management/openbao.md) |

### object-storage

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Silo** | 你已经在跑 MinIO、而上游社区版已经终结时用它——Silo 让 S3 API、落盘格式与 `MINIO_*` 命名继续可用；代价是可执行文件／软件包／镜像改名为 `silo`，且它是单一维护者对单一代码库的 fork。 | AGPL-3.0 | C（5/6） | [中](categories/object-storage/silo.zh.md) · [EN](categories/object-storage/silo.md) |
| **MinIO** | 用这一页决定你手上已经跑着的 MinIO 怎么办：社区仓库已归档（2026-04）且无人维护，所以这是“迁到在维护的 fork 或别的存储”的选择，而不是新部署的选项。 | AGPL-3.0 | C（6/6） | [中](categories/object-storage/minio.zh.md) · [EN](categories/object-storage/minio.md) |
| **Garage** | 想用几台分散各地、便宜的机器拼出一个 S3 端点、跨站点复制、其中一台离线仍可用时用它——但它的 S3 能力面刻意不完整（没有 ACL／策略语义）。 | AGPL-3.0 | B（4/6） | [中](categories/object-storage/garage.zh.md) · [EN](categories/object-storage/garage.md) |
| **SeaweedFS** | 真正的约束是对象数量——十亿级小文件——且你想要一个 `weed` 二进制同时提供 S3、文件系统与表层、靠加卷服务扩容量时用它。 | Apache-2.0 | B（6/6） | [中](categories/object-storage/seaweedfs.zh.md) · [EN](categories/object-storage/seaweedfs.md) |
| **Ceph** | 你需要基金会治理的同一平台提供对象、块与文件、且养得起一个真正的存储集群时用它——只需要一个 S3 桶时属于过量的工具。 | LGPL-2.1 | A（4/6） | [中](categories/object-storage/ceph.zh.md) · [EN](categories/object-storage/ceph.md) |
| **tusd** | 当用户要在不稳定的网络上传几个 GB 的文件、断了能从断点续传，并且字节直接流进磁盘或 S3/GCS/Azure 而不经过你的应用时用它——但它没有内置分布式锁，横向扩展得靠粘性路由。 | MIT | B（5/6） | [中](categories/object-storage/tusd.zh.md) · [EN](categories/object-storage/tusd.md) |

### desktop-automation

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Cua** | 当 agent 需要操作整台电脑（原生桌面应用、系统弹窗，而非仅网页）、且这次运行需要隔离时使用。 | MIT | B（5/6） | [中](categories/desktop-automation/cua.zh.md) · [EN](categories/desktop-automation/cua.md) |
| **PyAutoGUI** | 当你要用 Python 脚本在 Windows、macOS 或 Linux 上点击、输入一个只有图形界面的桌面程序时用它——但基于坐标和像素的自动化会因 DPI、分辨率或主题变化静默失效，必须有真实显示器，且上游自 2023 年起已无新提交。 | BSD-3-Clause | C（4/6） | [中](categories/desktop-automation/pyautogui.zh.md) · [EN](categories/desktop-automation/pyautogui.md) |
| **Windows-MCP** | 当 Claude、Codex、Gemini 里的 agent 需要按控件名（UI Automation 树）在原生 Windows 程序里点击、输入，并且直接作用在你的真实会话上时使用——没有沙箱，PowerShell、注册表工具和遥测都默认开启。 | MIT | B（6/6） | [中](categories/desktop-automation/windows-mcp.zh.md) · [EN](categories/desktop-automation/windows-mcp.md) |

### mobile-automation

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **baguette** | 当你想无头、可脚本地控制 Apple Silicon 上的 iOS 模拟器——60fps 投屏、宿主机手势注入、多设备 farm——但它需要 Xcode 26，且骑在 SimulatorKit 私有符号上时使用。 | Apache-2.0 | B（6/6） | [中](categories/mobile-automation/baguette.zh.md) · [EN](categories/mobile-automation/baguette.md) |
| **idb** | 当你要从远端客户端用细粒度原语自动化 iOS 模拟器**和**真机时用它——但 iOS 26 打坏了它一部分能力，且每个目标要挂一个 companion 进程。 | MIT | B（6/6） | [中](categories/mobile-automation/idb.zh.md) · [EN](categories/mobile-automation/idb.md) |
| **AXe** | 当你想要一个 `axe tap／type／describe-ui` 命令直接操作模拟器时用它——但它是单人维护，2026-07 后就没动静了。 | MIT | B（6/6） | [中](categories/mobile-automation/axe.zh.md) · [EN](categories/mobile-automation/axe.md) |
| **Appium** | 当你需要一个跨平台、跨语言的 WebDriver 测试框架同时覆盖 iOS 和 Android 时用它——代价是要自己跑一个服务端并逐平台装驱动。 | Apache-2.0 | A（6/6） | [中](categories/mobile-automation/appium.zh.md) · [EN](categories/mobile-automation/appium.md) |
| **WebDriverAgent** | 当你要自己搭 iOS 自动化底层时用它——它就是 Appium 驱动的那个 WebDriver 服务端，多数团队不会单独跑它。 | BSD-3-Clause | A（4/6） | [中](categories/mobile-automation/webdriveragent.zh.md) · [EN](categories/mobile-automation/webdriveragent.md) |
| **Maestro** | 当你想用 YAML 流程、几分钟就能上手做 Android／iOS／Web 的端到端测试时用它——但不支持 iOS 真机。 | Apache-2.0 | A（6/6） | [中](categories/mobile-automation/maestro.zh.md) · [EN](categories/mobile-automation/maestro.md) |
| **Detox** | 当你在测 React Native 应用、想要灰盒同步来压住 flaky 时用它——但它锁 React Native 版本、只支持 JS，且不支持 iOS 真机。 | MIT | B（6/6） | [中](categories/mobile-automation/detox.zh.md) · [EN](categories/mobile-automation/detox.md) |
| **tapflow** | 当团队里不写代码的人要在浏览器里测 iOS／Android 构建、而模拟器跑在你自己的 Mac 上时使用——但 agent 必须是固定在 Xcode 26–27 的 Apple Silicon Mac，只支持模拟器，而且几乎全由一位维护者写成。 | MIT | B（6/6） | [中](categories/mobile-automation/tapflow.zh.md) · [EN](categories/mobile-automation/tapflow.md) |

### game-dev

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **pygame** | 当你在学或教编程、想用几十行可读的 Python 写出一个小型 2D 游戏（窗口、事件循环、精灵、声音）时用它——但它是 CPU 绘制的库，没有编辑器和 3D，且自 2024-09 的 2.6.1 起再没发版。 | LGPL-2.1 | C（4/6） | [中](categories/game-dev/pygame.zh.md) · [EN](categories/game-dev/pygame.md) |
| **kaplay** | 想用纯 JS/TS 零仪式感地做一个 Jam 规模的 2D 网页游戏时用它——但要做长生命周期产品或 3D，停滞的稳定线和纯 2D 定位说明该另寻它路。 | MIT | B（6/6） | [中](categories/game-dev/kaplay.zh.md) · [EN](categories/game-dev/kaplay.md) |
| **pyxel** | 想用 Python 做复古像素风小游戏、要自带精灵／音乐编辑器和一条命令导出网页时用它——但做 3D、现代画风、上商店或主机，或需要团队接手引擎时，固定规格和单人维护说明该另寻它路。 | MIT | B（5/6） | [中](categories/game-dev/pyxel.zh.md) · [EN](categories/game-dev/pyxel.md) |

### kafka-tools

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **UI for Apache Kafka (provectus/kafka-ui)** | 当你想一条 docker run 起一个浏览器面板，看 Kafka broker、topic、消费组 lag 和消息内容时用它——但 provectus 上游自 2024-04 起再无发布，新部署请改用仍在维护的 kafbat/kafka-ui 分叉。 | Apache-2.0 | C（5/6） | [中](categories/kafka-tools/kafka-ui.zh.md) · [EN](categories/kafka-tools/kafka-ui.md) |
| **kafka-python** | 当你想要一个纯 Python、pip install 即装、无需编译 librdkafka 的 Kafka 客户端时用它——但纯 Python 客户端的吞吐追不上 confluent-kafka，且对最新 broker 特性可能滞后支持。 | Apache-2.0 | A（6/6） | [中](categories/kafka-tools/kafka-python.zh.md) · [EN](categories/kafka-tools/kafka-python.md) |

### networking

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Paramiko** | 当 Python 代码需要以编程方式建立 SSH／SFTP 连接并执行远程命令时用它——但它是纯 Python（比 OpenSSH 慢）、仅支持线程模型，且采用 LGPL-2.1 许可。 | LGPL-2.1 | B（6/6） | [中](categories/networking/paramiko.zh.md) · [EN](categories/networking/paramiko.md) |
| **sshtunnel** | 只在已有 Python 脚本早就依赖它的 `with` 块 SSH 端口转发、经堡垒机连私网数据库时继续用它——新装的版本在 Paramiko 4 及以上直接报错，而且 2021 年后再没发过版。 | MIT | B（4/6） | [中](categories/networking/sshtunnel.zh.md) · [EN](categories/networking/sshtunnel.md) |
| **dnspython** | 当 Python 需要查询任意记录类型、自定义解析器、区域传输、DNSSEC 或 DoH／DoT 时用它——但它绕过 /etc/hosts 与系统解析器，要求 Python 3.10+，且是库而非命令行工具。 | ISC | A（5/6） | [中](categories/networking/dnspython.zh.md) · [EN](categories/networking/dnspython.md) |
| **wondershaper** | 当某块 Linux 网卡需要一条命令设好整体上／下行带宽上限、又不想学 tc 语法时用它——但它生成的是 HTB 加 sfq 规则，而非能应对 bufferbloat 的 cake 或 fq_codel，没有按流 QoS，且自 2021 年起已停更。 | GPL-2.0 | E（4/6） | [中](categories/networking/wondershaper.zh.md) · [EN](categories/networking/wondershaper.md) |
| **ThriftPy** | 仅当你要在迁移前读懂仍在 import thriftpy 的遗留服务时用它——该仓库已归档且废弃，所有新的 Thrift 开发都应转向仍在维护的 thriftpy2。 | MIT | B（5/6） | [中](categories/networking/thriftpy.zh.md) · [EN](categories/networking/thriftpy.md) |
| **amneziawg-installer** | 当你所在网络的 DPI 封锁了裸 WireGuard、想在一台干净廉价 VPS 上一条命令装好内核态 AmneziaWG 服务端时用它——但它仅支持 Ubuntu／Debian、要求支持 AWG 2.0 的客户端，且会把整台机器改造成单一用途的加固 VPN 服务器。 | MIT | B（6/6） | [中](categories/networking/amneziawg-installer.zh.md) · [EN](categories/networking/amneziawg-installer.md) |
| **dae** | 当 Linux 路由器或主机要给整个局域网按规则分流、又希望直连流量由内核经 eBPF 直接转发时用它——但它要求内核 5.17 以上，没有图形界面和 SOCKS／HTTP 入站，且是 AGPL-3.0。 | AGPL-3.0 | B（6/6） | [中](categories/networking/dae.zh.md) · [EN](categories/networking/dae.md) |

### nginx-modules

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **lua-nginx-module (ngx_lua)** | 当你需要在 NGINX 上用 LuaJIT cosocket 实现真正的逐请求可编程能力（鉴权、路由、限流）时用它——但一次阻塞调用就会卡死整个 worker，且你被绑定在 OpenResty 版本耦合、核心团队高度集中的生态上。 | BSD-2-Clause | A（4/6） | [中](categories/nginx-modules/lua-nginx-module.zh.md) · [EN](categories/nginx-modules/lua-nginx-module.md) |
| **lua-resty-redis** | 当你的 OpenResty 边缘逻辑要在请求热路径上非阻塞访问 Redis（带连接池和 pipeline）时用它——但它只能在 ngx_lua 内运行，且不内置 Redis Cluster 的槽位路由。 | BSD-2-Clause | B（3/6） | [中](categories/nginx-modules/lua-resty-redis.zh.md) · [EN](categories/nginx-modules/lua-resty-redis.md) |
| **nginx-upload-module** | 当 NGINX 后面的应用要接大文件 multipart 上传、你想让 NGINX 自己落盘、只把路径、文件名和大小交给后端时用它——但它是一个低活跃、单人维护的 C 分叉（最后提交 2023-06），每次升级 NGINX 都要重编。 | BSD-3-Clause | "?"（2/6） | [中](categories/nginx-modules/nginx-upload-module.zh.md) · [EN](categories/nginx-modules/nginx-upload-module.md) |

### python-tooling

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Cython** | 当你已 profile 出的 Python 热点循环需要逼近 C 的速度、或要封装 C／C++ 库时用它——但它会引入 C 编译器和按平台构建 wheel 的流水线负担。 | Apache-2.0 | A（6/6） | [中](categories/python-tooling/cython.zh.md) · [EN](categories/python-tooling/cython.md) |
| **pyrasite** | 当一个卡死或漏内存的 Python 进程不能重启、你必须经 gdb 在它内部执行诊断代码时用它——但注入可能让目标崩溃，限制 ptrace 的主机会挡住它，维护也已近休眠。 | GPL-3.0 | D（4/6） | [中](categories/python-tooling/pyrasite.zh.md) · [EN](categories/python-tooling/pyrasite.md) |
| **gophernotes** | 当你想在 Jupyter 笔记本里用交互式 Go 单元做探索或教程时用它——但它自 2023 年起停滞，且跑的是解释器而非标准 Go。 | MIT | B（5/6） | [中](categories/python-tooling/gophernotes.zh.md) · [EN](categories/python-tooling/gophernotes.md) |
| **GRequests** | 当你想以最小改动、用 `map()` 让一套现有同步 `requests` 代码并发扇出到几百个 URL 时用它——但一 import 它就会经 gevent 给标准库打猴子补丁，可能和 asyncio、多进程或 C 扩展冲突。 | BSD-2-Clause | C（4/6） | [中](categories/python-tooling/grequests.zh.md) · [EN](categories/python-tooling/grequests.md) |
| **memory-analyzer** | 当你万不得已、要经 GDB 给一个运行中的 Linux Python 进程拍一次按类型的对象快照和引用链时用它——但 Meta 已归档它（代码停在 2021，目标是已 EOL 的 3.6/3.7），先试 memray 或 tracemalloc。 | MIT | D（5/6） | [中](categories/python-tooling/memory-analyzer.zh.md) · [EN](categories/python-tooling/memory-analyzer.md) |
| **uv** | 当 Python 项目要同时摆弄 pip、pip-tools、virtualenv、pyenv、pipx，CI 每次安装要几分钟时用它——一个二进制就能装 Python、出跨平台锁文件——但它只管 PyPI 包，路线图归 Astral，而 OpenAI 已宣布收购 Astral。 | Apache-2.0 OR MIT | A（6/6） | [中](categories/python-tooling/uv.zh.md) · [EN](categories/python-tooling/uv.md) |
| **curl_cffi** | 当 Python 客户端被 TLS／JA3 指纹识别拦下、而你需要一个能伪装真实浏览器的 `requests` 风格 API 时用它——但它随包带原生 libcurl，并非纯 Python。 | MIT | A（6/6） | [中](categories/python-tooling/curl-cffi.zh.md) · [EN](categories/python-tooling/curl-cffi.md) |
| **Google Colab CLI** | 当你的 GPU 来自 Colab 套餐、代码却在本地仓库或 agent 写的脚本里时用它——一条命令租下 Colab 虚拟机、跑完文件再释放——但它依赖 Colab 网页会话接口，尚在 1.0 之前，只支持 Linux／macOS，硬件按档位限制。 | Apache-2.0 | B（6/6） | [中](categories/python-tooling/google-colab-cli.zh.md) · [EN](categories/python-tooling/google-colab-cli.md) |

### reading-tools

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Read Frog** | 当你靠读真实文章学外语，想要双语段落、按水平讲解、朗读、自定义 AI 动作和间隔重复生词卡，并接自己的 AI 服务商时用它——但它由公司掌控双授权，2026-09 起还依赖专有排版包，无法 fork 出完全自由的构建。 | GPL-3.0 | B（6/6） | [中](categories/reading-tools/read-frog.zh.md) · [EN](categories/reading-tools/read-frog.md) |
| **FluentRead** | 当你想用一个开源扩展覆盖网页双语对照、PDF/ePub、OCR 和视频字幕，引擎可选免费服务、自带密钥或浏览器内本地模型时用它——但它是 GPL-3.0、实际单人维护，零配置默认会把文本发往公开翻译端点。 | GPL-3.0 | C（6/6） | [中](categories/reading-tools/fluentread.zh.md) · [EN](categories/reading-tools/fluentread.md) |
| **Margin Read** | 当页面文字只能发往你自己的 Ollama、LM Studio 或公司网关，又想要 MIT 许可、写明威胁模型的扩展时用它——但它是年轻的单人维护 Chrome MVP，近期已放缓，不含 PDF、字幕和 OCR。 | MIT | C（5/6） | [中](categories/reading-tools/margin-read.zh.md) · [EN](categories/reading-tools/margin-read.md) |
| **Pair Translate** | 当 Read Frog 和 FluentRead 显得太重，你想要一个小巧的双语翻译扩展，把文本从浏览器直接发给微软、DeepL 或你自己的大模型（含本机 Ollama）时用它——但它是 GPL-3.0，实际是一个人维护、刚满一年的项目。 | GPL-3.0 | C（5/6） | [中](categories/reading-tools/pair-translate.zh.md) · [EN](categories/reading-tools/pair-translate.md) |
| **NetNewsWire** | 当你在 Mac／iPhone 上读大量订阅、想要一个快速无广告、数据自己掌控的原生 RSS 客户端时用它——但它仅限 Apple 平台，别处一概不支持。 | MIT | B（6/6） | [中](categories/reading-tools/netnewswire.zh.md) · [EN](categories/reading-tools/netnewswire.md) |
| **Just Read** | 当你想在浏览器里按自己的方式清掉文章的广告与杂乱、还能按站点记忆选择器时用它——但它是 EULA 授权的源码，并非真正的开源。 | Unlicensed (EULA) | C（6/6） | [中](categories/reading-tools/just-read.zh.md) · [EN](categories/reading-tools/just-read.md) |
| **FreshRSS** | 当你想把订阅和已读状态放在自己的 VPS、NAS 或树莓派上，并让任何兼容 Google Reader 接口的客户端同步时用它——但升级、备份和 TLS 永远是你的事；不需要插件的话，Miniflux 更精简。 | AGPL-3.0 | B（6/6） | [EN](categories/reading-tools/freshrss.md) · [中](categories/reading-tools/freshrss.zh.md) |
| **Horizon** | 当订阅源多到刷不完、你想要一条自托管的 LLM 流水线每天替你打分、筛选、去重并生成双语简报，而不是一个自己刷的阅读器时用它。 | MIT | B（6/6） | [EN](categories/reading-tools/horizon.md) · [中](categories/reading-tools/horizon.zh.md) |
| **Follow Builders** | 当你想不配任何 key 就每天收到一份固定 AI 建造者名单在 X、播客和两个博客上说了什么的摘要时用它——但信源你改不了，可用性系在一个人的 X API 账单上。 | MIT (declared in README; no LICENSE file) | C（4/6） | [EN](categories/reading-tools/follow-builders.md) · [中](categories/reading-tools/follow-builders.zh.md) |
| **Bilingual Book Maker** | 用 AI 翻译把 epub/txt/md/srt/pdf 做成双语对照书的 Python CLI，支持多家 LLM/MT 后端、断点续跑，有 PyPI 包。 | MIT | A（5/6） | [中](categories/reading-tools/bilingual-book-maker.zh.md) · [EN](categories/reading-tools/bilingual-book-maker.md) |
| **TranslateBooksWithLLMs** | 用本地或云端大模型整本翻译 EPUB／DOCX／SRT／TXT 并保住格式的桌面程序加命令行，带术语表和断点续跑。 | AGPL-3.0 | C（6/6） | [中](categories/reading-tools/translate-books-with-llms.zh.md) · [EN](categories/reading-tools/translate-books-with-llms.md) |

### speech

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **SpeechBrain** | 当你需要在一套统一的 PyTorch recipe 代码库上训练和适配语音模型（ASR、说话人识别、语音分离）时用它——但它以研究和训练为先，生产部署和跨版本 API 稳定性得你自己负责。 | Apache-2.0 | B（5/6） | [中](categories/speech/speechbrain.zh.md) · [EN](categories/speech/speechbrain.md) |
| **Voicebox** | 当你想要一个自托管的语音 I/O 工作室——克隆音色 TTS、热键 Whisper 听写、MCP/REST 让 agent 发声三合一，且是 MIT——时用它；但它是年轻的单人项目，发布节奏已停滞、自动粘贴目前仅 macOS。 | MIT | B（6/6） | [中](categories/speech/voicebox.zh.md) · [EN](categories/speech/voicebox.md) |
| **GPT-SoVITS** | 想要带 WebUI、且有训练路径可继续提升相似度的本地小样本声音克隆时用它；但它只管 TTS，听写、效果、agent 发声都不在其范围，且版本发布稀疏。 | MIT | A（5/6） | [中](categories/speech/gpt-sovits.zh.md) · [EN](categories/speech/gpt-sovits.md) |
| **Coqui TTS（idiap 分支）** | 想要带 XTTS v2 克隆与广泛预训练模型覆盖的 Python TTS 库时用它；但它是 MPL-2.0、不提供应用外壳，且是一家已倒闭公司项目的社区分支。 | MPL-2.0 | C（4/6） | [中](categories/speech/coqui-ai-tts.zh.md) · [EN](categories/speech/coqui-ai-tts.md) |
| **AntSpeaker (MECT)** | 想用零训练的现成微型 PyTorch 检查点（380 万到 960 万参数）判断两段音频是否同一说话人时用它；但权重是 CC-BY-NC-SA（不可商用）、没有训练代码，且仓库是只活了两周的论文发布。 | CC-BY-NC-SA-4.0 | C（3/6） | [中](categories/speech/antspeaker.zh.md) · [EN](categories/speech/antspeaker.md) |
| **VoxCPM** | 想用代码和权重都是 Apache-2.0 的模型自托管声音克隆、或用文字描述设计音色（覆盖 30 种语言）时用它；但要备好约 8 GB 显存的 GPU，长文本得自己切句（单次长输出会漂移），并发服务还要另起引擎。 | Apache-2.0 | B（5/6） | [中](categories/speech/voxcpm.zh.md) · [EN](categories/speech/voxcpm.md) |
| **VoiceStudio** | 想要一个本地桌面应用把声音克隆、视频配音、听写和 agent 发声（MCP）一次装齐、还能切换十几个引擎时用它；但默认模型权重禁止商用，应用是 AGPL 且付费 Pro 档正在成形，项目只有半年历史、由一人维护。 | AGPL-3.0 | C（5/6） | [中](categories/speech/voicestudio.zh.md) · [EN](categories/speech/voicestudio.md) |
| **IndexTTS** | 想让同一个克隆音色带出不同情绪——音色取自一段录音，情绪取自另一段录音、8 维向量或一句文字——并说中、英、日、西、阿五种语言时用它；但 B 站许可在月活超 1 亿或年收入超 1 亿元（以中文版为准）时要另行授权，精确时长配音尚未开放，也没有训练代码。 | NOASSERTION（B 站自定义许可） | A（3/6） | [中](categories/speech/index-tts.zh.md) · [EN](categories/speech/index-tts.md) |
| **VibeVoice** | 当你想用一个自托管模型把最长一小时的多人录音直接转成“谁、何时、说了什么”的文字稿（带热词、50 多种语言、vLLM 服务和流式版本），或要一个约 0.3 秒就开口的英文 TTS 时用它——但 7B ASR 模型要 24 GB 以上显存，没有任何带 tag 的发布，而且最出名的多人长对话 TTS 代码已在 2025-09 被移除。 | MIT | A（4/6） | [中](categories/speech/vibevoice.zh.md) · [EN](categories/speech/vibevoice.md) |

### terminal-ui

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **colorama** | 当 Python 命令行要让 ANSI 颜色在老式 Windows 控制台上也正确显示、又想几乎零依赖时用它——但它只翻译颜色和样式码，在 Linux、macOS 或 Windows 10+ 上它能做的你自己也能做。 | BSD-3-Clause | B（5/6） | [中](categories/terminal-ui/colorama.zh.md) · [EN](categories/terminal-ui/colorama.md) |
| **asciimatics** | 当你需要在 Linux／macOS／Windows 上跨平台构建全屏 Python TUI 并附带 ASCII 动画引擎时用它——但它的控件较简陋、API 偏旧式，且为单人维护。 | Apache-2.0 | B（5/6） | [中](categories/terminal-ui/asciimatics.zh.md) · [EN](categories/terminal-ui/asciimatics.md) |
| **Terminal Markdown Viewer (mdv)** | 当你想在 SSH 下的纯终端里一次性渲染一份简单 Markdown（带颜色、表格和代码高亮）时用它——但它自 2023-10 起无人维护，遇到内嵌 HTML 直接失败，glow 或 mdcat 更稳。 | BSD-3-Clause | D（3/6） | [中](categories/terminal-ui/terminal-markdown-viewer.zh.md) · [EN](categories/terminal-ui/terminal-markdown-viewer.md) |
| **ART** | 当 Python 命令行需要纯 Python 的 figlet 风格 ASCII 文字横幅、且不依赖系统二进制时用它——但它只做文字转艺术字（不做图片转 ASCII），也不与 figlet 字体完全一致。 | MIT | B（5/6） | [中](categories/terminal-ui/art.zh.md) · [EN](categories/terminal-ui/art.md) |
| **asciify** | 当你想花一分钟读懂经典的图片转 ASCII 做法（缩小、转灰度、亮度映射字符梯度），拿来学习或自己重写时用它——但仓库没有许可证、默认保留所有权利，且自 2018-10 起已废弃。 | NONE | E（4/6） | [中](categories/terminal-ui/asciify.zh.md) · [EN](categories/terminal-ui/asciify.md) |
| **Warp** | 当你想让终端把每条命令的输出切成可选中的块，由内置编码 agent 直接读取并在同一会话里接着干活，而且要在 macOS、Linux、Windows 上用同一个应用时用它——但只有 AGPL 客户端开源，agent、同步和认证都跑在 Warp 的闭源服务器上。 | AGPL-3.0 | B（5/6） | [中](categories/terminal-ui/warp.zh.md) · [EN](categories/terminal-ui/warp.md) |
| **Alacritty** | 当你想要一个用显卡渲染、在 macOS、Linux、BSD、Windows 上行为一致的快速终端，并且布局已交给 tmux 或窗口管理器时用它——但它设计上就没有标签页、分屏和连字。 | Apache-2.0 | A（6/6） | [中](categories/terminal-ui/alacritty.zh.md) · [EN](categories/terminal-ui/alacritty.md) |

分类顺序见 [INDEX.zh.md](INDEX.zh.md)。
| **Readability.js** | 当你需要用 Firefox 阅读视图那套久经考验的引擎，把网页剥离成纯文章（标题、作者、正文）时用它——但它只解析你传入的 DOM，不会抓取 URL，也不会渲染重 JS 的 SPA。 | Apache-2.0 | [中](categories/web-scraping/article-extraction/readability-js.zh.md) · [EN](categories/web-scraping/article-extraction/readability-js.md) |
| **python-readability** | 当你的 Python 流水线需要从已抓取的 HTML 中用 lxml 快速抽取正文、不依赖浏览器或 Node 时用它——但它单人维护、更新缓慢，而 trafilatura 在抽取基准上往往得分更高。 | Apache-2.0 | [中](categories/web-scraping/article-extraction/python-readability.zh.md) · [EN](categories/web-scraping/article-extraction/python-readability.md) |
| **dragnet** | 当启发式抽取器老把你的页面切错、而你有标注数据想在 Python 里训练一个能把正文和用户评论分开的模型时用它——但它近乎停摆，且把 scikit-learn 钉在 0.21 以下，现代环境里安装很痛苦。 | MIT | [中](categories/web-scraping/article-extraction/dragnet.zh.md) · [EN](categories/web-scraping/article-extraction/dragnet.md) |
| **boilerpipe** | 当 JVM 上的索引器或语料管线要用经典浅层文本特征启发式从原始 HTML 里剥出正文、又不想引入浏览器或 Python 服务时用它——但它实际已废弃（最后 push 在 2018-01），得自己 vendor 并接管修复。 | Apache-2.0 | [中](categories/web-scraping/article-extraction/boilerpipe.zh.md) · [EN](categories/web-scraping/article-extraction/boilerpipe.md) |
| **fuck-login** | 当你想通过可读的 Python 脚本学习 2016–2018 年中文网站登录的底层机制（CSRF token、RSA 加密密码、验证码图片）时用它——但仓库已废弃，多数脚本大概率已失效，且没有许可证。 | NONE | [中](categories/web-scraping/crawling-tools/fuck-login.zh.md) · [EN](categories/web-scraping/crawling-tools/fuck-login.md) |
| **gopup** | 当你在 notebook 里做探索性研究、想不写爬虫就拿到中文公开数据（微博或百度指数、CPI、Shibor）的 DataFrame 时用它——但它自 2023-09 起停滞，TOKEN 接口所在站点已下线，失败还会悄悄返回 `None`。 | NONE | [中](categories/web-scraping/crawling-tools/gopup.zh.md) · [EN](categories/web-scraping/crawling-tools/gopup.md) |
| **PRAW** | 当你的数据源就是 Reddit、想走官方 OAuth 合规路径并自带限速处理时用它——但真正的边界是 Reddit 自家的 API 条款、配额与定价，而非这个库。 | BSD-2-Clause | [中](categories/web-scraping/crawling-tools/praw.zh.md) · [EN](categories/web-scraping/crawling-tools/praw.md) |
| **Scrapyd** | 当你需要把本地 Scrapy 爬虫部署到服务器、通过 HTTP API 做定时与多版本调度时用它——但它只能跑 Scrapy 且默认无鉴权，暴露 6800 端口前务必先加认证。 | BSD-3-Clause | [中](categories/web-scraping/crawling-tools/scrapyd.zh.md) · [EN](categories/web-scraping/crawling-tools/scrapyd.md) |
| **SpiderKeeper** | 当已经在跑 Scrapyd 的小团队想要一个极简浏览器看板来上传 egg、按 cron 调度爬虫、查看作业统计时用它——但最后提交在 2018-05，钉着 2017 年的 Flask 栈，默认账号密码是 admin/admin。 | MIT | [中](categories/web-scraping/crawling-tools/spiderkeeper.zh.md) · [EN](categories/web-scraping/crawling-tools/spiderkeeper.md) |
## 为什么做这个

多数开源 README 是营销：讲它能干啥、为啥好，却**不**告诉你何时*不该*用、和替代怎么比、运维成本多少。
做选型的 agent 恰恰需要这片「负空间」。GitHub-Michelin 把 README 这个体裁反转成**决策支持**体裁。

索引刻意做得「弱」——没有数据库、没有搜索、没有 embedding，就是给 agent 读和推理的 Markdown。
目录结构本身就是「查询 API」。

## 选型信号与启发式

选开源是在赌未来，不只是匹配功能。每页都带一个 **`健康度与可持续性`** 小节——一段有日期、带标注的
判断：维护节奏、治理与 bus factor、背书方、采用度与生态，以及风险旗标（relicense 史、open-core
阉割、CVE）。它要和 `何时不用` 一起看。

有一条先验值得点名——**林迪效应（Lindy effect）**：对非易逝之物（软件、格式、工具），预期*剩余*寿命
随当前年龄增长。一个**持续活跃**了 12 年的项目，比一个半年内爆火的项目更适合长期押注。把它当先验、
不是定律，且永远按 **年龄 × 仍活跃** 一起用：它既给「年轻但被炒作」的仓库降权（star 离谱、未经检验），
也**救不了**「老但已弃」的仓库（光有年龄 ≠ 还活着）；遇到范式更替时还可能误导。每页都记录项目**年龄**，
让这条先验可核查。[推断：林迪只是启发式，不构成对任何具体项目存续的保证。]

## 结构（递归树，双语）

```
INDEX.md / INDEX.zh.md                        # 根：分类路由（英 / 中）
categories/<分类>/INDEX.md / INDEX.zh.md      # 一个分类节点：项目页 + 子分类
categories/<分类>/<子类>/INDEX.md …           # 更深的节点 —— 树随增长自平衡
…/<slug>.md  +  …/<slug>.zh.md                # 一个叶子：英文选型页 + 它的中文兄弟页
```

`categories/` 是一棵**递归、自平衡的树**：某个分类项目过多时会拆成子分类（linter 告警，
`refactor-index` 执行拆分）。英文是 agent 默认读取的 canonical 路径，`.zh.md` 是同一内容的中文版。
| **Rich** | 当 Python 命令行的输出不只要颜色、还要排版（对齐的表格、进度条、代码高亮、好读的报错栈），且想用一个像 `print` 的 API 搞定时用它——但它没有事件循环、做不了交互界面，而且维护如今压在一个人身上。 | MIT | ?（0/6） | [EN](categories/terminal-ui/rich.md) · [中](categories/terminal-ui/rich.zh.md) |
| **Textual** | 当 Python 命令行工具参数多到失控，大家要在 SSH 上浏览、筛选、操作数据，又不想做网页应用时用它——但 Textualize 公司 2025 年收尾后基本只剩作者一人维护，大版本也换得勤。 | MIT | ?（0/6） | [EN](categories/terminal-ui/textual.md) · [中](categories/terminal-ui/textual.zh.md) |
| **tmux** | 当 SSH 上的长任务必须比终端活得久、你要的是最小且无处不在的复用器时用它——但它对 pane 里跑什么一无所知，agent 监管得自己搭胶水。 | ISC | — | [中](categories/terminal-ui/tmux.zh.md) · [EN](categories/terminal-ui/tmux.md) |
| **Zellij** | 当你想要自带可发现性的终端复用（模式提示条、鼠标、布局、WASM 插件）外加 token 鉴权 web client 时用它——但它是 pre-1.0、issue 积压大，且 web 接入要做真 TLS 运维。 | MIT | — | [中](categories/terminal-ui/zellij.zh.md) · [EN](categories/terminal-ui/zellij.md) |
| **Pebrel** | 当你在 Windows 上同时跑好几个 AI 编程命令行，想让每个面板自己报告在跑／在等／跑完，并用通知跳回那个面板，同时 SSH/SFTP 也在同一个应用里时用它——但它只有十二周、单人维护，Linux/macOS 仍是 Preview。 | GPL-3.0-or-later | — | [中](categories/terminal-ui/pebrel.zh.md) · [EN](categories/terminal-ui/pebrel.md) |

### 一个项目页的结构

每页 = **YAML frontmatter（事实，带日期）** + **正文（判断）**。两者刻意分开：事实会过期、需要
重新核验（`last_verified`）；判断是观点，要带标注（`[未验证]` / `[推断]`），绝不当成永恒真理断言。

**Frontmatter**（中英成对、逐字一致——事实与语言无关）：
`name · slug · repo · category · tags · language · license · maturity`（带日期）· `last_verified` · `type`
（`tool | library | app | framework | service | model | skill-pack`）。

**正文小节**（确切集合随 `type` 而定）：

| 小节（英 / 中） | 必需于 | 承载什么 |
|---|---|---|
| `When to use` / `何时使用` | 所有类型 | **触发场景**——什么情况下该想到这个项目，以及它在该场景下为何胜过替代品 |
| `How it works` / `怎么用起来` | 所有类型（回填中） | **主干用户故事**——大白话机制 + 自动生成的双泳道流程图（你做的 / 它做的） |
| `When NOT to use` / `何时不用` | 所有类型 | 决定性筛子：反模式、规模天花板、锁定、维护风险 |
| `Comparison` / `横向对比` | 所有类型 | 与真实替代品的对比表（替代品尚未收录则标 `未收录`） |
| `Tech stack` / `技术栈` | 非 `skill-pack` | 它构建于哪些语言、框架、数据存储 |
| `Dependencies` / `依赖` | 非 `skill-pack` | 你必须自己跑的运行时/基建（数据库、服务、硬件） |
| `Ops difficulty` / `运维难度` | 非 `skill-pack` | 低 / 中 / 高 + 原因 |
| `Health & viability` / `健康度与可持续性` | 所有类型 | 带日期的可持续性判断——维护、治理与 bus factor、背书方、**年龄 × Lindy**、采用度、风险旗标 |
| `Caveats (unverified)` / `存疑（未验证）` | 所有类型 | 不确定性账本——每条未验证事实一个 `[未验证]`/`[推断]` 条目 |

完整契约见 [tools/schema.md](tools/schema.md)；linter（[tools/lint.py](tools/lint.py)）强制这套形状
（小节、中英对齐、中文全角标点、README 对齐）。

## 新鲜度

事实会过期。每页记 `last_verified`。超过 90 天 linter 会告警；`sync-entry` 技能负责对照线上仓库
重核。把任何事实都当作**时点快照**，并按真话纪律标注（`[未验证]` / `[推断]`）。

## 贡献

策展，而非求全。一个项目只有在**确实被评估过**、**且存在真实选型问题**（有值得对比的替代）时才进。
见 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [tools/schema.md](tools/schema.md)。

```bash
python3 tools/lint.py                        # 结构：形状、路由、死链、fanout
python3 tools/reverse_index.py --check       # committed 的 reports/ 必须与页面一致
python3 tools/quality_scan.py --fail-on-gated   # 确定性 triage 分类
# 或：make gates
```

新增、重命名或移动页面会改变 committed 的反向索引——用 `python3 tools/reverse_index.py --write`
在同一次改动里重新生成 `reports/`。

## 许可证

- **工具**（代码，如 `tools/lint.py`）：MIT——见 [LICENSE](LICENSE)。
- **内容**（`categories/` 下的散文、路由页、文档）：CC BY 4.0——见 [LICENSE-CONTENT](LICENSE-CONTENT)。

各项目页描述的是第三方项目，其归属与许可证由各自作者决定；CC BY 4.0 仅覆盖这里的原创分析。

### investment-finance

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **awesome-deep-trading** | List of awesome resources for machine learning-based algorithmic trading | NOASSERTION | D（4/6） | [中](categories/investment-finance/awesome-deep-trading.zh.md) · [EN](categories/investment-finance/awesome-deep-trading.md) |
| **OpenBB** | 每个行情、宏观、公告数据源只封装一次，同时供 Python、REST、MCP 智能体和 Workspace 使用；V5（Apache-2.0）删掉了 yfinance/FMP，安装很重 | Apache-2.0 | B（5/6） | [中](categories/investment-finance/openbb.zh.md) · [EN](categories/investment-finance/openbb.md) |
| **FinRL** | FinRL®:  Financial Reinforcement Learning. 🔥 | NOASSERTION | B（5/6） | [中](categories/investment-finance/finrl.zh.md) · [EN](categories/investment-finance/finrl.md) |
| **qlib** | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://github.com/microsoft/RD-Agent to automate R&D process. | NOASSERTION | B（6/6） | [中](categories/investment-finance/qlib.zh.md) · [EN](categories/investment-finance/qlib.md) |
| **backtrader** | Python Backtesting library for trading strategies | NOASSERTION | D（4/6） | [中](categories/investment-finance/backtrader.zh.md) · [EN](categories/investment-finance/backtrader.md) |
| **yfinance** | Download market data from Yahoo! Finance's API | NOASSERTION | A（6/6） | [中](categories/investment-finance/yfinance.zh.md) · [EN](categories/investment-finance/yfinance.md) |
| **HiThink Financial-API** | 一把 API Key 取同花顺官方 A 股数据（CLI、MCP、REST、Python，长历史落本地 DuckDB）——但 GitHub 仓库已于 2026-10 消失，客户端代码只剩冻结的 Gitee 镜像，npm CLI 和托管服务仍可用 | MIT | "?"（1/6） | [中](categories/investment-finance/financial-api.zh.md) · [EN](categories/investment-finance/financial-api.md) |
| **AKShare** | 免 Key 的 Python 库，把中国市场的公开财经页面封装成一次调用返回 pandas DataFrame | MIT | A（6/6） | [中](categories/investment-finance/akshare.zh.md) · [EN](categories/investment-finance/akshare.md) |
| **Tushare** | Python SDK 加托管 tushare.pro 服务，凭 token 与积分档取 A 股数据 | BSD-3-Clause | D（5/6） | [中](categories/investment-finance/tushare.zh.md) · [EN](categories/investment-finance/tushare.md) |

### education-tutoring

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **DeepTutor** | DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/. | NOASSERTION | B（5/6） | [中](categories/education-tutoring/deeptutor.zh.md) · [EN](categories/education-tutoring/deeptutor.md) |

### agent-governance

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **agent-governance-toolkit** | Microsoft 面向生产 AI agent 的 public-preview 治理工具包：策略门控 tool call、身份 / 信任、审计 / 合规、MCP security gateway、SRE 控制，以及围绕 agent framework 的多语言 SDK。 | MIT | B（6/6） | [中](categories/agent-governance/agent-governance-toolkit.zh.md) · [EN](categories/agent-governance/agent-governance-toolkit.md) |
| **SkillSpector** | NVIDIA 的 AI agent skill 安全扫描器：安装前通过 CLI/MCP 检查 prompt injection、外传、危险脚本、MCP poisoning、依赖，并输出 SARIF/JSON 证据。 | Apache-2.0 | B（5/6） | [中](categories/agent-governance/skillspector.zh.md) · [EN](categories/agent-governance/skillspector.md) |
| **Snyk Agent Scan** | Snyk 的整机扫描器：清点 14 种编程 agent 里已装的 MCP 服务和 skill；发现在本地做，但每个结论都来自 Snyk 托管的闭源分析接口（要账号、有配额、数据外传）。 | Apache-2.0 | A（6/6） | [中](categories/agent-governance/agent-scan.zh.md) · [EN](categories/agent-governance/agent-scan.md) |
| **claude-skill-audit** | 离线正则扫描整个 Claude Code `.claude/` 目录（skill、agent、hook、权限、MCP 配置、密钥）的零依赖 TypeScript 小工具；单一作者、0 star、检测浅，只能当快速 lint 用。 | MIT | C（5/6） | [中](categories/agent-governance/claude-skill-audit.zh.md) · [EN](categories/agent-governance/claude-skill-audit.md) |
| **skills-scanner** | 零依赖的 Python CLI：盘点 Claude Code、Claude Desktop、Cursor、Windsurf 下的 skill、命令和 MCP 配置，离线跑规则，并与 SQLite 基线比对漂移。2026-05 起休眠且未上 PyPI：当模式来源看，不要当依赖用。 | Apache-2.0 | C（5/6） | [中](categories/agent-governance/skills-scanner.zh.md) · [EN](categories/agent-governance/skills-scanner.md) |
| **agent-guard** | 安装前把关的 skill：把 skill、MCP 包、npm/PyPI/Go/cargo 包、release 二进制和安装脚本分派给 SkillSpector、Cisco mcp-scanner、GuardDog、OpenSSF package-analysis 或 VirusTotal，再合并成一个 fail-closed 的退出码；自己没有检测能力，单一作者，3 个 star。 | MIT | C（5/6） | [中](categories/agent-governance/agent-guard.zh.md) · [EN](categories/agent-governance/agent-guard.md) |
| **Claude Skills Security Guide** | 一份 Claude skill 十二种攻击向量的书面目录，附手册和六个去掉杀伤力的示例攻击，外加三个演示水平、可直接拷入的防御 skill（正则扫描器、哈希清单、文本净化器）；2026-03 起无人维护，拿来读，别拿来卡流程。 | MIT | C（4/5） | [中](categories/agent-governance/claude-skills-security-guide.zh.md) · [EN](categories/agent-governance/claude-skills-security-guide.md) |
| **Cisco MCP Scanner** | Cisco 开源的 MCP 服务扫描器：从运行中的服务、客户端配置或存好的 JSON 里拉出每个工具、提示词和资源的描述，用本地 YARA 规则标出注入和投毒文字，另可选 LLM、Cisco 接口和基于 LLM 的源码检查；只出报告，没有给 CI 用的退出码，也没有 SARIF。 | Apache-2.0 | B（6/6） | [中](categories/agent-governance/mcp-scanner.zh.md) · [EN](categories/agent-governance/mcp-scanner.md) |
### social-simulation

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **MiroFish** | 打包好的「上传→模拟→报告」群体智能预测应用：喂一份文档，拿回预测报告和可交互的模拟世界。 | AGPL-3.0 | C（5/6） | [中](categories/social-simulation/mirofish.zh.md) · [EN](categories/social-simulation/mirofish.md) |
| **OASIS** | CAMEL-AI 出品的 pip 可装社交媒体模拟框架（类 Twitter/Reddit，号称最高百万 agent），用代码研究信息传播与极化。 | Apache-2.0 | B（6/6） | [中](categories/social-simulation/oasis.zh.md) · [EN](categories/social-simulation/oasis.md) |
| **AgentSociety** | 清华 FIB Lab 的 LLM 原生社会科学模拟平台：Ray 分布式、实验回放、DuckDB 追踪。 | Apache-2.0 | B（5/6） | [中](categories/social-simulation/agentsociety.zh.md) · [EN](categories/social-simulation/agentsociety.md) |
| **generative_agents** | 2023 年斯坦福「Smallville」原版研究原型（memory stream / reflection / planning）——学开创性架构用，别在上面盖楼。 | Apache-2.0 | D（3/6） | [中](categories/social-simulation/generative-agents.zh.md) · [EN](categories/social-simulation/generative-agents.md) |

### osint

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **holehe** | 通过注册/找回密码端点探测一个邮箱在 120+ 站点是否有账号（不提醒目标）——2024-09 起停止维护，应吸收其方法论与模块表，或 fork 后逐模块复验。 | GPL-3.0 | D（5/6） | [中](categories/osint/holehe.zh.md) · [EN](categories/osint/holehe.md) |
| **socialscan** | 直接查询平台注册端点，拿到干净的邮箱/用户名「可用或已占用」判定——只覆盖约 11 个平台，发版零星。 | MPL-2.0 | D（4/6） | [中](categories/osint/socialscan.zh.md) · [EN](categories/osint/socialscan.md) |
| **Maigret** | 跨 3000+ 站点建立用户名档案：ID 提取、递归搜索、HTML/PDF/XMind 报告——本类目维护最活跃的选择。 | MIT | A（6/6） | [中](categories/osint/maigret.zh.md) · [EN](categories/osint/maigret.md) |
| **Sherlock** | 在 480+ 社交网络做简单、久经考验的用户名存在性核查，组织治理、社区庞大——个人页信号较粗，不做档案提取。 | MIT | A（6/6） | [中](categories/osint/sherlock.zh.md) · [EN](categories/osint/sherlock.md) |
| **GHunt** | 用你自己的 Google 会话对 Google 账户做认证式深挖 OSINT（Gmail→资料、Gaia ID、Drive、BSSID）——能力强，AGPL-3.0，ToS/法律风险最高。 | AGPL-3.0 | B（5/6） | [中](categories/osint/ghunt.zh.md) · [EN](categories/osint/ghunt.md) |
| **GhostTrack** | Termux 上零配置的菜单脚本，打印一个 IP（ipwho.is 的地区/ISP）或手机号（国家、原始运营商、时区）的公开元数据，外加 24 站的粗糙用户名检查——并不能真正定位，用户名结果会误报，无许可证，2024-01 起无人维护。 | NONE (no LICENSE file — all rights reserved) | E（5/6） | [中](categories/osint/ghosttrack.zh.md) · [EN](categories/osint/ghosttrack.md) |

### knowledge-base

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **LLM Wiki** | 当你希望自己的文档被一次性编译成一份本地互链维基、由 LLM 持续保鲜，而不是每次查询都用 RAG 重新推导时用它。 | GPL-3.0 | C（5/6） | [中](categories/knowledge-base/llm-wiki.zh.md) · [EN](categories/knowledge-base/llm-wiki.md) |
| **Logseq** | 当你想要一个本地优先、由你自己撰写并用 Datalog 查询的大纲笔记工具、且 LLM 能力交给插件时用它。 | AGPL-3.0 | B（6/6） | [中](categories/knowledge-base/logseq.zh.md) · [EN](categories/knowledge-base/logseq.md) |
| **SiYuan** | 当你想要一个自托管、块级引用的知识工作空间、让人与 AI 智能体共同编辑时用它——但部分功能需付费（open-core）。 | AGPL-3.0 | B（6/6） | [中](categories/knowledge-base/siyuan.zh.md) · [EN](categories/knowledge-base/siyuan.md) |
| **Khoj** | 当你想要一个可自托管的 AI 第二大脑、从你的文档与网络取答案、并覆盖浏览器／桌面／Obsidian、模型可选本地或在线时用它。 | AGPL-3.0 | C（6/6） | [中](categories/knowledge-base/khoj.zh.md) · [EN](categories/knowledge-base/khoj.md) |
| **Reor** | 当你需要一份「本地优先 AI 笔记」的模式参考时用它；它已归档（2025-05），不要把生产押在它上面。 | AGPL-3.0 | E（5/6） | [中](categories/knowledge-base/reor.zh.md) · [EN](categories/knowledge-base/reor.md) |
| **OpenKB** | 当你希望长文档被 LLM 一次性编译成一份可持久、互相链接的 Markdown 维基、之后再对这份维基提问时用它——无头 CLI，不需要向量库。 | Apache-2.0 | B（6/6） | [中](categories/knowledge-base/openkb.zh.md) · [EN](categories/knowledge-base/openkb.md) |

### peripherals

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **OpenLogi** | 当你想要 Options+ 那套功能——按应用 profile、手势、键盘重映射、静态 RGB、摄像头控制——在 macOS、Linux、Windows 上用同一份 TOML 配置拿到，并且能接受一个尚未 1.0、只有几个月历史、没有接收器配对的项目时用它。 | MIT OR Apache-2.0 | C（5/6） | [中](categories/peripherals/openlogi.zh.md) · [EN](categories/peripherals/openlogi.md) |
| **Solaar** | 在 Linux 上当任务本身是设备管理而不是重映射时用它：配对与解绑接收器、读取电量与设备状态、修改 HID++ 设置——背后是 14 年仍在发版的记录；代价是仅限 Linux，且没有摄像头与 RGB。 | GPL-2.0-or-later | B（6/6） | [中](categories/peripherals/solaar.zh.md) · [EN](categories/peripherals/solaar.md) |
| **Mouser** | 当你想要在 Windows／macOS／Linux 上用便携压缩包按应用重映射罗技 HID++ 鼠标，不需要安装器、账号或服务，并且不要求配对、键盘、摄像头或按设备映射时用它。 | MIT | B（6/6） | [中](categories/peripherals/mouser.zh.md) · [EN](categories/peripherals/mouser.md) |
| **logiops** | 在 Linux 上，当你想要一个读单份声明式 `/etc/logid.cfg` 的 root systemd 守护进程而不是 GUI 时用它——接受只支持 HID++ 2.0+ 鼠标、没有应用感知，且开发自 2024 年起实际已停。 | GPL-3.0-or-later | C（5/6） | [中](categories/peripherals/logiops.zh.md) · [EN](categories/peripherals/logiops.md) |

### decision-models

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Kev** | 当你想要一个自托管、可微调的模型，对一段文本回答带类型的问题（是/否、多选、评分）并给出可用的校准概率时用它——不是托管判定 API，也不是从零训一个分类器。 | Apache-2.0 | C（5/6） | [中](categories/decision-models/kev.zh.md) · [EN](categories/decision-models/kev.md) |
| **Laya** | 当同样的带类型判定（单选、是非、打分）大量重复、你想要一个本地小编码器一次前向就答完、能路由 100 多种语言，并且你愿意微调时用它——它的基础 checkpoint 零样本很弱。 | Apache-2.0 | B（5/6） | [中](categories/decision-models/laya.zh.md) · [EN](categories/decision-models/laya.md) |
| **Simple Jev** | 当你已经在服务一个开源聊天模型、想要 Jev 那套带类型判定接口时用它——一段共享上下文加一组带类型问题进去，概率分布出来，不用解析生成的 JSON；代价是继承底座的判断力与未校准的置信度。 | Apache-2.0 | C（4/6） | [中](categories/decision-models/simple-jev.zh.md) · [EN](categories/decision-models/simple-jev.md) |

### optimization-solvers

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Rebalancer** | 当任务是「按这些策略在分片／主机量级重新安置这些对象」——容量、均衡、故障域打散、尽量少搬——而你宁愿声明具名 spec 加一个调好的局部搜索，也不想手写线性规划时用它。 | Apache-2.0 | B（5/6） | [中](categories/optimization-solvers/rebalancer.zh.md) · [EN](categories/optimization-solvers/rebalancer.md) |
| **OR-Tools** | 问题组合性广——路径规划、排程、装箱、指派——而你想要一次安装就同时拿到 CP-SAT、LP／MIP 封装与 routing，并支持 Python／Java／.NET／C++ 时用它。 | Apache-2.0 | A（6/6） | [中](categories/optimization-solvers/or-tools.zh.md) · [EN](categories/optimization-solvers/or-tools.md) |
| **HiGHS** | 模型已经是矩阵或 MPS／LP 文件，你想用一个无第三方依赖、MIT 许可的 LP／QP／MIP 引擎、且中间不要夹一层建模框架时用它。 | MIT | A（6/6） | [中](categories/optimization-solvers/highs.zh.md) · [EN](categories/optimization-solvers/highs.md) |
| **Timefold Solver** | JVM 上、计划要在一长串软的、丰富的业务规则下产生——排班、路径、课表——且规则必须一直能以 Java 形式编辑时用它。 | Apache-2.0 | B（6/6） | [中](categories/optimization-solvers/timefold-solver.zh.md) · [EN](categories/optimization-solvers/timefold-solver.md) |
| **OptaPlanner** | 只在要读懂或迁移已有 9.x 代码库时打开：仓库已归档、代码并入 Apache KIE Drools，新工作应该落在 Timefold Solver。 | Apache-2.0 | C（4/6） | [中](categories/optimization-solvers/optaplanner.zh.md) · [EN](categories/optimization-solvers/optaplanner.md) |

### cad

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **FreeCAD** | 当你需要一套可编辑的参数化历史加真 B-rep 实体模型——画草图、加约束、Pad/Pocket，之后改一个尺寸让零件自行重建——文件在本地、带 Python API、不用买席位时用它。 | LGPL-2.1-or-later | A（5/6） | [中](categories/cad/freecad.zh.md) · [EN](categories/cad/freecad.md) |

### desktop-launchers

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Tinycast** | 想要一个开源、完全原生、还能直接跑你现有 Raycast 扩展的 macOS 命令面板时用它——但要求 macOS 26+，且项目只有三个月历史、巴士系数为一。 | AGPL-3.0 | B（4/6） | [中](categories/desktop-launchers/tinycast.zh.md) · [EN](categories/desktop-launchers/tinycast.md) |

### design-editors

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **DesignCraft** | 需要按 InDesign 的方式排印刷页面——读写 IDML、导出 CMYK/PDF/X 印刷 PDF、用 CLI 或 MCP 驱动每条命令——而且要在任何系统上、不用 Creative Cloud 座位时用它；必须打开 `.indd`、今天就要过认证印前检查、或需要格式稳定（v0.x，才八天大）时不要用。 | MIT OR Apache-2.0 | C（5/6） | [中](categories/design-editors/designcraft.zh.md) · [EN](categories/design-editors/designcraft.md) |
| **OpenPencil** | 需要打开已有的 Figma `.fig` 文件并对它做脚本化处理——查看结构、检查、转换、导出成 JSX——或者想要一个 local-first、AI 原生、没有服务器、没有账号、不上传的编辑器时用它。 | MIT | B（6/6） | [中](categories/design-editors/open-pencil.zh.md) · [EN](categories/design-editors/open-pencil.md) |
| **Penpot** | 一个团队必须在你自己控制的服务器上编辑同一份设计文件——浏览器编辑器、实时多人协作、组件/变体、原型和 design token——而按席位租托管 SaaS 不可行时用它。 | MPL-2.0 | B（5/6） | [中](categories/design-editors/penpot.zh.md) · [EN](categories/design-editors/penpot.md) |
| **VectorCraft** | 想要 Illustrator 的布局和快捷键又不想付订阅——在 Linux、FreeBSD 或浏览器里——打开 `.ai`/PDF/EPS/Affinity 文件，或者让 agent 通过它的 CLI/MCP 命令接口画图并导出矢量图时用它；项目才几天大，赶工期的活别用。 | MIT OR Apache-2.0 | C（5/6） | [中](categories/design-editors/vectorcraft.zh.md) · [EN](categories/design-editors/vectorcraft.md) |

### learning-resources

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **AI Engineering Hub** | 当你需要某种 LLM 技术栈组合的可运行样例——本地模型 RAG 应用、带联网兜底的 CrewAI 团队、MCP 服务——好从里面抄胶水代码时用它；它是 MIT 许可的演示代码，没有测试、很多文件夹已过时，不能当依赖。 | MIT | A（5/6） | [中](categories/learning-resources/ai-engineering-hub.zh.md) · [EN](categories/learning-resources/ai-engineering-hub.md) |
| **AI Performance Engineering Resources** | 当你需要学或查 GPU／AI 性能工程，想要每个机制对应的权威原文、并且按依赖顺序排好——一次请求 → 一张卡 → 算子 → 引擎 → 分布式服务——而不是一堆博客时用它。 | MIT（仅声明） | C（3/5） | [中](categories/learning-resources/gpu-perf-engineering-resources.zh.md) · [EN](categories/learning-resources/gpu-perf-engineering-resources.md) |
| **HowToLiveLonger（程序员延寿指南）** | 当你想把饮食、饮品、睡眠、运动、体重这些日常习惯，按某项研究报告的全因死亡率变化排在同一页上、每个数字都能追到出处，好决定先改哪件事时用它；不要拿它决定吃药或吃补剂。 | Unlicense | C（3/5） | [中](categories/learning-resources/how-to-live-longer.zh.md) · [EN](categories/learning-resources/how-to-live-longer.md) |

### model-editing

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Heretic** | 当一个对齐后的开源模型拒答那些对你的工作是正当的提示词，而你想自动把拒答方向消融掉、并带一个可量化的质量取舍时用它——一张显卡、不用训练数据、工具侧是 AGPL。 | AGPL-3.0-or-later | B（6/6） | [中](categories/model-editing/heretic.zh.md) · [EN](categories/model-editing/heretic.md) |
| **Remove Refusals with Transformers** | 想要最短、可读的原生 `transformers` 拒答移除配方时用它——两个 Apache-2.0 脚本供阅读与改造，没有优化器、没有导出、也不维护。 | Apache-2.0 | C（5/6） | [中](categories/model-editing/remove-refusals-with-transformers.zh.md) · [EN](categories/model-editing/remove-refusals-with-transformers.md) |
| **abliterator** | 想自己写脚本、针对 TransformerLens 的 hook 逐步检查消融过程时用它——激活缓存、方向打分、改权重——代价是仓库自 2024-06 起停更。 | MIT | D（4/6） | [中](categories/model-editing/abliterator.zh.md) · [EN](categories/model-editing/abliterator.md) |
| **ErisForge** | 想要一个可 `pip` 安装、能对选定解码层消融或“增强”某种行为、能给拒答打分并保存模型的库时用它——代价是单一维护者、仓库没有 `LICENSE` 文件。 | MIT（仅声明） | "?"（2/6） | [中](categories/model-editing/erisforge.zh.md) · [EN](categories/model-editing/erisforge.md) |
| **deccp** | 只在你要它的中文审查关注时用它：一个 Qwen2 去审查概念验证，附手工核对的数据集与文章，作者明确不再支持。 | Apache-2.0 | C（4/6） | [中](categories/model-editing/deccp.zh.md) · [EN](categories/model-editing/deccp.md) |

### pentest

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Pentest Swarm AI** | 当授权的 web／API 范围很宽、既要广度又要「已利用、留证据」的实证发现、且必须用任意支持工具调用的模型自托管（含全本地 Ollama）时用它——代价是 alpha 阶段的 swarm 调度器、AGPL-3.0 和单一维护者的巴士系数。 | AGPL-3.0 | C（6/6） | [中](categories/pentest/pentest-swarm-ai.zh.md) · [EN](categories/pentest/pentest-swarm-ai.md) |
| **Wifit3** | 当授权目标是 Wi-Fi、而你手里是一台没有工具链可装的 Linux／Windows／macOS 笔记本时用它——代价是只有约 19 款受支持 USB 芯片可用、且 v0.x BETA 只有约 3 个月大。 | GPL-2.0 | C（6/6） | [中](categories/pentest/wifit3.zh.md) · [EN](categories/pentest/wifit3.md) |

### disk-cleanup

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **MangoDisk** | 一个清理工具要同时覆盖 macOS、Windows 和 Linux，而且你想读懂每条被删路径背后的规则时用它——代价是永久删除、代码库只有两个月、只有一位维护者。 | GPL-3.0-only | C（6/6） | [中](categories/disk-cleanup/mangodisk.zh.md) · [EN](categories/disk-cleanup/mangodisk.md) |
| **Win11Debloat** | 要在一台不受管的 Windows 10／11 电脑上，用一张清单清掉预装应用、广告、Copilot 和遥测，并留注册表备份可撤回时用它——不适合域管理的机器群、镜像瘦身或 PowerShell 被锁定的环境。 | MIT | B（6/6） | [中](categories/disk-cleanup/win11debloat.zh.md) · [EN](categories/disk-cleanup/win11debloat.md) |

### 3d-reconstruction

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Spirula Studio** | 当你想把视频或照片在一个解压即用的程序里变成高斯泼溅和带贴图的网格、任意厂商 GPU 都能跑（Vulkan）、自带 SfM、抠图和全景／鱼眼支持时用它——代价是只有一位维护者和 GPL-3.0。 | GPL-3.0 | C（6/6） | [中](categories/3d-reconstruction/spirula-studio.zh.md) · [EN](categories/3d-reconstruction/spirula-studio.md) |

### streaming-clients

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **PipePipe** | 想在安卓手机上不登 Google 看 YouTube／B 站／NicoNico、自动跳过赞助片段、免费后台播放时用它——代价是单人维护，YouTube 一改防护就可能播不了。 | GPL-3.0 | B（6/6） | [中](categories/streaming-clients/pipepipe.zh.md) · [EN](categories/streaming-clients/pipepipe.md) |

### computer-vision

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **DeepFace** | 当你想用一次 Python 调用做人脸比对（是不是同一个人）和一对多人脸检索、模型可切换、阈值现成时用它——但被封装的权重各有许可（Buffalo_L 仅限非商业），TensorFlow 总会被装上，种族／情绪分析在欧盟《人工智能法》下受限。 | MIT | B（6/6） | [中](categories/computer-vision/deepface.zh.md) · [EN](categories/computer-vision/deepface.md) |

### meeting-intelligence

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Call.md** | 当你想要一个开源 macOS 会议副驾驶：录下你与对方、会中自动调用你的 MCP 工具、会后自动起草行动项——同时接受录制与转写走 VideoDB 云。 | MIT | C（4/6） | [中](categories/meeting-intelligence/call-md.zh.md) · [EN](categories/meeting-intelligence/call-md.md) |

### social-media-management

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Easel** | 在中文平台（小红书／抖音／知乎／B 站等）运营账号，想要一个自托管智能体工作台覆盖发现→创作→发布→归因、且带账号画像时用它——代价是项目只有一个月大（v0.x），小红书自动化有作者自述的风控暴露。 | Apache-2.0 | B（5/6） | [中](categories/social-media-management/easel.zh.md) · [EN](categories/social-media-management/easel.md) |
| **xiaohongshu-mcp** | 想让你现有的 Agent 通过一个自部署、自带指纹浏览器的 MCP／REST 服务在小红书上搜索、阅读、发帖、评论、点赞时用它——代价是真实的封号风险、单人维护，以及从作者 CDN 下发的不透明预编译浏览器。 | Apache-2.0 | B（6/6） | [中](categories/social-media-management/xiaohongshu-mcp.zh.md) · [EN](categories/social-media-management/xiaohongshu-mcp.md) |

### healthcare-ai

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **OpenMed** | 当临床笔记必须在患者数据绝不出网的前提下产出带类型实体与脱敏副本时用它——代价是每个模型都要在你自己的语料上验证，且发布节奏系于一人。 | Apache-2.0 | B（5/6） | [中](categories/healthcare-ai/openmed.zh.md) · [EN](categories/healthcare-ai/openmed.md) |

### design-tokens

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Dembrandt** | 设计系统唯一的来源是一个线上网址，你需要把它真实的颜色、字体和间距导出成 DTCG/Tailwind/DESIGN.md token——或者要一个 token 漂移就让 CI 失败的门禁——时用它；token 本来就是你自己写的、或你担心的是布局回归时不要用。 | MIT | C（5/6） | [中](categories/design-tokens/dembrandt.zh.md) · [EN](categories/design-tokens/dembrandt.md) |

### photo-editing

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **LightCraft** | 想在本机用上 Lightroom 那套挑片、冲洗、导出的流程又不交订阅，还想让智能体通过 MCP／CLI 来操作时用它——代价是它只有九天大、尚在 1.0 之前，相机色彩靠估算，RAW 格式覆盖也还薄。 | MIT OR Apache-2.0 | B（5/6） | [中](categories/photo-editing/lightcraft.zh.md) · [EN](categories/photo-editing/lightcraft.md) |

### hackintosh

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **NullMoth NVIDIA Driver for macOS** | 当一台跑 macOS 15 的 OpenCore PC 里只有图灵或更新的 GeForce 卡，而且保住这张卡比稳定更重要时用它——代价是一个只有两天历史、单一作者、只在一张 RTX 5060 上验证过的内核驱动，要放宽 SIP／AMFI／安全启动，许可证禁止商用。 | PolyForm-Noncommercial-1.0.0 + LGPL-3.0-or-later + MIT | D（4/6） | [中](categories/hackintosh/nvidia-macos-driver.zh.md) · [EN](categories/hackintosh/nvidia-macos-driver.md) |
