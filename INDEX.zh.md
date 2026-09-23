# oss-atlas — 分类路由

> 递归路由根层。Agent 先读这张总表，按「何时进这个分类」选分类，再沿各节点的 `INDEX.zh.md`
> 逐层下钻（树可以很深，不是固定三级），直到项目页。
> English index: [INDEX.md](INDEX.md) · 完整读取流程见 [AGENTS.md](AGENTS.md)

## 分类

| 分类 | 何时进来 | 路由 |
|---|---|---|
| **agent-tooling** | 为 AI 编码 agent 选「任务/工作追踪、持久记忆、agent 状态」，以及 agent 把控制权交还给你的人审/批准界面。 | [→](categories/agent-tooling/INDEX.zh.md) |
| **sandboxing** | 隔离不可信代码与 agent 生成代码——虚拟机／内核级隔离运行时，以及建在其上的沙箱平台。 | [→](categories/sandboxing/INDEX.zh.md) |
| **serverless** | 自己运维的 Kubernetes 原生 serverless／缩容到零服务层。 | [→](categories/serverless/INDEX.zh.md) |
| **document-management** | 选「文档归档/OCR/打标签/全文检索」系统。 | [→](categories/document-management/INDEX.zh.md) |
| **on-device-ml** | 选「在端侧/边缘设备（手机、笔记本、IoT）本地跑模型」的运行时。 | [→](categories/on-device-ml/INDEX.zh.md) |
| **function-calling** | 选「把自然语言请求变成受 schema 约束的工具/函数调用」的模型与服务栈。 | [→](categories/function-calling/INDEX.zh.md) |
| **web-automation** | 选「驱动/自动化 Web 界面」的工具——浏览器自动化，或页内自然语言 GUI agent。 | [→](categories/web-automation/INDEX.zh.md) |
| **llm-training** | 微调或强化训练 LLM 与多步 agent。 | [→](categories/llm-training/INDEX.zh.md) |
| **agent-frameworks** | 构建与运行多步 / 多智能体系统——agent 框架与 agent 操作系统。 | [→](categories/agent-frameworks/INDEX.zh.md) |
| **agent-memory** | 面向 agent、与 LLM 无关的跨会话持久记忆基础设施。 | [→](categories/agent-memory/INDEX.zh.md) |
| **deep-research** | 迭代式多源研究 agent：搜索、抓取、综合成报告。 | [→](categories/deep-research/INDEX.zh.md) |
| **ai-code-review** | LLM 辅助的代码评审：对 diff 或仓库产出行级问题。 | [→](categories/ai-code-review/INDEX.zh.md) |
| **rag-retrieval** | 面向 RAG 的文档索引、代码智能图与图数据库。 | [→](categories/rag-retrieval/INDEX.zh.md) |
| **llm-eval** | 对提示词、agent 与 RAG 做测试、基准与安全红队扫描。 | [→](categories/llm-eval/INDEX.zh.md) |
| **agent-dev-methodology** | 塑造 agent **如何**构建软件的框架与方法论——spec 驱动、上下文工程、persona/命令体系。 | [→](categories/agent-dev-methodology/INDEX.zh.md) |
| **ai-design-generation** | agent 驱动的 UI/设计、幻灯片、社交卡片与 HTML 产物生成。 | [→](categories/ai-design-generation/INDEX.zh.md) |
| **dev-utilities** | 独立开发者工具、数据处理瑞士军刀与可自托管的基础设施。 | [→](categories/dev-utilities/INDEX.zh.md) |
| **frontend-animation** | 面向 Web 的 JavaScript 动画引擎与运动库。 | [→](categories/frontend-animation/INDEX.zh.md) |
| **api-gateway** | 路由、保护、限流并治理服务与 LLM 流量的 API / AI 网关。 | [→](categories/api-gateway/INDEX.zh.md) |
| **geospatial** | 地理信息系统（GIS）——查看、编辑、分析空间数据。 | [→](categories/geospatial/INDEX.zh.md) |
| **team-chat** | 可自托管的团队聊天 / 协作平台、agent 增强工作区与多 LLM 团队聊天。 | [→](categories/team-chat/INDEX.zh.md) |
| **captcha** | CAPTCHA / 机器人检测挑战（工作量证明、点击、行为式）。 | [→](categories/captcha/INDEX.zh.md) |
| **ml-research** | 小而自洽的 ML 研究 demo 与参考实现。 | [→](categories/ml-research/INDEX.zh.md) |
| **agent-skills** | 成体系的 agent 技能、提示词、subagent 人设与 harness 配置合集——按用途领域拆分。 | [→](categories/agent-skills/INDEX.zh.md) |
| **observability** | 在多数据源的指标/日志/追踪之上做看板、告警与可视化。 | [→](categories/observability/INDEX.zh.md) |
| **data-visualization** | 在 SQL 数据仓库之上自托管的 BI / 数据探索看板。 | [→](categories/data-visualization/INDEX.zh.md) |
| **ocr** | 光学字符识别引擎——图像/扫描件转文本。 | [→](categories/ocr/INDEX.zh.md) |
| **document-parsing** | 把文档（PDF/DOCX/…）解析成结构化 Markdown/JSON，供 gen-AI 消费。 | [→](categories/document-parsing/INDEX.zh.md) |
| **office-automation** | 程序化创建、读取、编辑原生 Office 文档（.docx/.xlsx/.pptx）——生成侧，面向脚本与 agent。 | [→](categories/office-automation/INDEX.zh.md) |
| **diagramming** | 从文本生成图表（diagrams-as-code），用于 Markdown、文档和 Web。 | [→](categories/diagramming/INDEX.zh.md) |
| **media-download** | 通过 CLI 或库从流媒体站点下载音视频。 | [→](categories/media-download/INDEX.zh.md) |
| **media-processing** | 解码/编码/转码/滤镜处理音视频（媒体框架与工具链）。 | [→](categories/media-processing/INDEX.zh.md) |
| **llm-chat-ui** | 可自部署、跨多 LLM provider 的 AI 聊天客户端前端（单用户 / BYOK）。 | [→](categories/llm-chat-ui/INDEX.zh.md) |
| **markdown-tools** | Markdown 解析、渲染与写作工具。 | [→](categories/markdown-tools/INDEX.zh.md) |
| **pdf-tools** | 渲染、读取与处理 PDF 文件。 | [→](categories/pdf-tools/INDEX.zh.md) |
| **workflow-orchestration** | 编写、调度并监控批处理数据/工作流管线（DAG 编排器）。 | [→](categories/workflow-orchestration/INDEX.zh.md) |
| **llm-inference** | 高性能 LLM/模型推理与服务引擎，以及 AI 系统语言。 | [→](categories/llm-inference/INDEX.zh.md) |
| **task-queue** | 分布式后台任务执行——任务队列与作业调度器。 | [→](categories/task-queue/INDEX.zh.md) |
| **im-automation** | 即时通讯机器人与自动化（微信等 IM 平台）。 | [→](categories/im-automation/INDEX.zh.md) |
| **web-ui** | 前端 UI/UX 库——产品引导、新手上手、界面组件。 | [→](categories/web-ui/INDEX.zh.md) |
| **proxy-pool** | 面向网络爬虫的自托管轮换代理 IP 池。 | [→](categories/proxy-pool/INDEX.zh.md) |
| **debugging-proxy** | HTTP(S)/WebSocket 调试代理——抓取、检查、改写并 mock 流量。 | [→](categories/debugging-proxy/INDEX.zh.md) |
| **web-scraping** | 从网页抓取并提取内容/结构——文章正文提取与 HTML 解析。 | [→](categories/web-scraping/INDEX.zh.md) |

| **auth** | 认证与授权库——登录提供方与权限规则。 | [→](categories/auth/INDEX.zh.md) |
| **databases** | 数据库与数据库工具——客户端、GUI、同步，以及 Redis/ES 兼容存储。 | [→](categories/databases/INDEX.zh.md) |
| **object-storage** | 你自建的 S3 兼容对象存储服务端。 | [→](categories/object-storage/INDEX.zh.md) |
| **desktop-automation** | 程序化桌面 GUI 自动化（鼠标/键盘/屏幕）。 | [→](categories/desktop-automation/INDEX.zh.md) |
| **game-dev** | 游戏开发库与引擎。 | [→](categories/game-dev/INDEX.zh.md) |
| **kafka-tools** | Apache Kafka 客户端与管理界面。 | [→](categories/kafka-tools/INDEX.zh.md) |
| **networking** | 网络库——SSH、DNS、隧道、RPC 与流量整形。 | [→](categories/networking/INDEX.zh.md) |
| **nginx-modules** | NGINX / OpenResty 扩展模块（Lua、上传等）。 | [→](categories/nginx-modules/INDEX.zh.md) |
| **python-tooling** | Python 开发者工具——编译器、进程注入、notebook、异步 HTTP。 | [→](categories/python-tooling/INDEX.zh.md) |
| **reading-tools** | 阅读工具——阅读模式扩展与 RSS 阅读器。 | [→](categories/reading-tools/INDEX.zh.md) |
| **speech** | 语音处理工具包（ASR、TTS、说话人任务）。 | [→](categories/speech/INDEX.zh.md) |
| **terminal-ui** | 终端/CLI UI 库——着色、TUI、ASCII art、终端渲染。 | [→](categories/terminal-ui/INDEX.zh.md) |
| **video-production** | AI 编排的端到端视频制作——由编码助手内的 agent 驱动研究、脚本撰写、素材生成、合成与渲染。 | [→](categories/video-production/INDEX.zh.md) |
| **investment-finance** | 量化金融、市场数据、交易研究与投资分析工具。 | [→](categories/investment-finance/INDEX.zh.md) |
| **education-tutoring** | AI 辅导、学习助手与教育场景 agent 系统。 | [→](categories/education-tutoring/INDEX.zh.md) |
| **agent-governance** | AI agent 的治理、策略执行、身份、沙箱与可靠性控制。 | [→](categories/agent-governance/INDEX.zh.md) |
| **blockchain-dev-infrastructure** | EVM 与区块链开发网络的 faucet、本地链及配套开发基础设施。 | [→](categories/blockchain-dev-infrastructure/INDEX.zh.md) |
| **social-simulation** | 模拟由 LLM agent 组成的社会——社交媒体世界、舆论动力学与推演沙盒。 | [→](categories/social-simulation/INDEX.zh.md) |
| **osint** | OSINT 侦察——由邮箱/用户名做账户存在性探测、身份档案收集与平台专项调查（授权优先）。 | [→](categories/osint/INDEX.zh.md) |
| **knowledge-base** | 个人知识库与「第二大脑」应用——积累、互链并查询你自己的文档语料，可选由 LLM 维护。 | [→](categories/knowledge-base/INDEX.zh.md) |
| **peripherals** | 配置并驱动桌面外设——罗技鼠标、键盘、接收器、灯与摄像头——通过 HID++ 与 UVC。 | [→](categories/peripherals/INDEX.zh.md) |
| **typesetting** | 把纯文本标记源编译成排版成品——印刷 PDF、网页、幻灯片、书或文档集。 | [→](categories/typesetting/INDEX.zh.md) |
| **decision-models** | 自托管的小模型——把一段文本变成带类型、概率可用的判定：是/否、单选、按档打分。 | [→](categories/decision-models/INDEX.zh.md) |
| **optimization-solvers** | 分配问题、LP／MIP 与约束最优化的求解器与建模 DSL——声明模型，让求解器去搜。 | [→](categories/optimization-solvers/INDEX.zh.md) |
| **cad** | 自己跑的计算机辅助设计——参数化三维实体建模、二维制图，以及其下的几何内核。 | [→](categories/cad/INDEX.zh.md) |
| **desktop-launchers** | 键盘驱动的桌面启动器／命令面板——应用启动、剪贴板历史、片段、快捷链接、窗口管理，一个快捷键全管。 | [→](categories/desktop-launchers/INDEX.zh.md) |
| **design-editors** | 你自己跑的开源设计编辑器——本地优先或自托管的 Figma 级画布。 | [→](categories/design-editors/INDEX.zh.md) |



## 如何新增分类

新分类 = `categories/` 下一个新目录，自带 `INDEX.md` **和** `INDEX.zh.md`，并在本表和
[INDEX.md](INDEX.md) 各加一行。只有当一个项目确实放不进现有分类时才新建。详见
[tools/schema.md](tools/schema.md) 与 `add-project` 技能。
