# oss-atlas

**一个面向 coding agent 的开源项目「选型」自然语言索引。**
agent 收到任务时读这个索引来挑开源项目——重点是衡量每个候选*何时不该用*，而不只是它能干什么。

> English README: [README.md](README.md)

## 安装

把 oss-atlas 的公开选型 skills 装进你的 coding agent：

- **`select-oss`** —— 为任务选择开源项目、库、工具、框架、模型或系统。
- **`select-agent-skills`** —— 选择可安装的 `SKILL.md` 包和 agent-skill 组合。

这两个 skill 默认通过 HTTP 读取公开索引（无需本地副本），在 clone 内也能直接读本地。

**任意 agent，经 [skills.sh](https://skills.sh)**（Claude Code、Codex、Cursor、OpenCode、Droid、
Kilo、Gemini CLI、Copilot 等 ~70 个 —— CLI 内置了每个 agent 的 skills 路径）：

```bash
# -g 装到全局（所有项目）；去掉 -g 则装到当前项目。用 -a 指定 agent，如 -a claude-code
npx skills add ZhenningLang/oss-atlas -g
```

**手动**（无 Node）—— 把 skill 目录拷进你 agent 的 skills 目录，以 Claude Code 为例：

```bash
git clone https://github.com/ZhenningLang/oss-atlas
cp -r oss-atlas/skills/select-oss ~/.claude/skills/
cp -r oss-atlas/skills/select-agent-skills ~/.claude/skills/
```

skills 从 `raw.githubusercontent.com/ZhenningLang/oss-atlas/main/` 拉取页面；只安装很小的 `SKILL.md`，
因此体积极小、永远读到最新索引。对没有联网能力的 agent，skills 会回退到本地 clone。

维护者还有一个内部 **`project-harvester`** skill，位于 `skills/project-harvester/`，用于批量发现候选项目。
它标记了 `metadata.internal: true`，不属于正常公开安装面。

## 项目总表

完整索引，按分类分组。每个项目有一份英文页（`<slug>.md`）和一份中文页（`<slug>.zh.md`），点击直达。交互式浏览见 [INDEX.zh.md](INDEX.zh.md)；agent 从 [AGENTS.md](AGENTS.md) 开始。

### agent-tooling

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **beads** | 当 AI agent 跨会话丢失任务状态、你想在仓库里要一张可版本化、感知依赖的任务图时用它。 | MIT | B（6/6） | [中](categories/agent-tooling/beads.zh.md) · [EN](categories/agent-tooling/beads.md) |
| **CCPM** | 当一个功能大到单次会话装不下、且你想要 PRD 转 GitHub Issues 的规格加上 git worktree 并行 agent 时使用。 | MIT | B（4/6） | [中](categories/agent-tooling/ccpm.zh.md) · [EN](categories/agent-tooling/ccpm.md) |
| **Entire** | 想把 AI agent 会话以 Git checkpoint 形式与 commit 并列捕获、可搜索可回滚时用它。 | MIT | B（5/6） | [中](categories/agent-tooling/entire-cli.zh.md) · [EN](categories/agent-tooling/entire-cli.md) |
| **Ralph for Claude Code** | 想让 Claude Code 无人值守地啃完 fix_plan.md 清单、又要速率限制/熔断器/双条件退出闸门兜底时用它。 | MIT | B（6/6） | [中](categories/agent-tooling/ralph-claude-code.zh.md) · [EN](categories/agent-tooling/ralph-claude-code.md) |
| **Context Mode** | 当 coding agent 把上下文耗在原始工具输出上、你想要沙箱执行加熬过 compaction 的会话记忆时用它。 | Elastic-2.0 | D（6/6） | [中](categories/agent-tooling/context-mode.zh.md) · [EN](categories/agent-tooling/context-mode.md) |
| **Planning with Files** | 当长任务 agent 总在 /clear、上下文压缩或崩溃中丢失计划时用它把计划落到磁盘。 | MIT | B（4/6） | [中](categories/agent-tooling/planning-with-files.zh.md) · [EN](categories/agent-tooling/planning-with-files.md) |
| **Vercel Skills** | 当你想要一个 npm 风格的 CLI 来跨多个编码 agent 安装、查找、更新 SKILL.md 技能包时使用。 | MIT | D（6/6） | [中](categories/agent-tooling/vercel-skills.zh.md) · [EN](categories/agent-tooling/vercel-skills.md) |
| **AgentsView** | 当你同时跑多个编码 agent、想要本地优先的跨 agent 会话搜索与 token／成本分析时用它——但它问世仅数月、尚未到 1.0，要预期频繁变动。 | MIT | B（6/6） | [中](categories/agent-tooling/agentsview.zh.md) · [EN](categories/agent-tooling/agentsview.md) |
| **Agent Orchestrator** | 当你要监管多个跑在真实分支上的并行编码 agent、想要一个桌面控制面把每个隔离进 git worktree 并自动路由 CI／review／冲突反馈时用它——但它约 4.5 个月大、尚未到 1.0、单一 User 所有，且 daemon 是 loopback 无鉴权。 | Apache-2.0 | B（5/6） | [中](categories/agent-tooling/agent-orchestrator.zh.md) · [EN](categories/agent-tooling/agent-orchestrator.md) |
| **CLI-Anything** | 当你想让编码 agent 驱动只有 GUI 的软件、走由应用自身引擎支撑的生成式 CLI harness 时用它——但它仍在 1.0 之前，且每个 harness 由社区维护。 | Apache-2.0 | B（6/6） | [中](categories/agent-tooling/cli-anything.zh.md) · [EN](categories/agent-tooling/cli-anything.md) |
| **Hermes Workspace** | 当你跑的是 Nous 的 hermes-agent、想把它的状态当 Web 驾驶舱用——聊天、memory、skills、终端、tmux swarm 派发、手机经 PWA/Tailscale 可达——但它的增强面板锚定 Hermes gateway/dashboard API、且问世仅约 6 个月时用它。 | MIT | B（5/6） | [中](categories/agent-tooling/hermes-workspace.zh.md) · [EN](categories/agent-tooling/hermes-workspace.md) |
| **CloudCLI (Claude Code UI)** | 当你的大脑是 Claude Code / Codex / Cursor CLI、想要这些会话的浏览器/移动驾驶舱（文件、终端、git）时用它——但它是 AGPL-3.0-or-later、单人操作形态。 | AGPL-3.0-or-later | C（5/6） | [中](categories/agent-tooling/claudecodeui.zh.md) · [EN](categories/agent-tooling/claudecodeui.md) |
### sandboxing

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **gVisor** | 不可信容器必须与宿主内核隔离、又不想跑虚拟机时用它——不需要 KVM，且容器工作流不变。 | Apache-2.0 | A（5/6） | [中](categories/sandboxing/gvisor.zh.md) · [EN](categories/sandboxing/gvisor.md) |
| **Kata Containers** | 想让每个 pod 在轻量虚拟机里拿到真内核、同时 Kubernetes 保持常规 RuntimeClass 工作流时用它。 | Apache-2.0 | A（5/6） | [中](categories/sandboxing/kata-containers.zh.md) · [EN](categories/sandboxing/kata-containers.md) |
| **Firecracker** | 你在自建沙箱层、想要一个带控制 API 的极简 KVM microVM 原语（而不是容器运行时）时用它。 | Apache-2.0 | A（5/6） | [中](categories/sandboxing/firecracker.zh.md) · [EN](categories/sandboxing/firecracker.md) |
| **OpenSandbox** | 当你需要自托管隔离沙箱、在 K8s 规模上运行不可信的 agent 生成代码（带出口管控和凭证保险库）时用它——但仓库仅数月之龄（2025-12 创建），其 API 与 Lindy 长期记录尚未经检验。 | Apache-2.0 | B（5/6） | [中](categories/sandboxing/opensandbox.zh.md) · [EN](categories/sandboxing/opensandbox.md) |
| **E2B** | 当 agent 需要跑 AI 生成的代码、你想要把沙箱做成 SDK 时用它——默认托管，必须落在自己账号时用 Terraform 自托管到 AWS／GCP。 | Apache-2.0 | A（6/6） | [中](categories/sandboxing/e2b.zh.md) · [EN](categories/sandboxing/e2b.md) |
| **Agent Substrate** | 当你有一大批大部分时间闲置的有状态 agent 会话、想把它们多路复用到少数预热 Kubernetes pod 上（闲置时存档、按需恢复）时用它——但它处于 1.0 之前、API 不稳定、安全加固尚未做。 | Apache-2.0 | B（4/6） | [中](categories/sandboxing/substrate.zh.md) · [EN](categories/sandboxing/substrate.md) |
| **Modal client SDK** | 想要 serverless 容器、GPU 与沙箱而什么都不用运维时用它——客户端 SDK 开源，平台闭源且只能托管。 | Apache-2.0 | A（6/6） | [中](categories/sandboxing/modal-client.zh.md) · [EN](categories/sandboxing/modal-client.md) |
| **Microsandbox** | 沙箱必须跑在你已有的硬件上时用它——一个二进制或一个 SDK、普通 OCI 镜像、每沙箱出口策略与宿主侧 secret，无守护进程、无集群——但宿主需要 KVM／Apple Silicon／WHP，且仍处于 beta。 | Apache-2.0 | A（5/6） | [中](categories/sandboxing/microsandbox.zh.md) · [EN](categories/sandboxing/microsandbox.md) |

### serverless

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Knative Serving** | 当 HTTP 服务一天里大部分时间闲着、你想要按 revision 的发布加缩容到零，又不想采用某个 FaaS 产品时用它。 | Apache-2.0 | B（5/6） | [中](categories/serverless/knative-serving.zh.md) · [EN](categories/serverless/knative-serving.md) |

### document-management

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **paperless-ngx** | 想自托管对扫描纸质资料做 OCR + 打标签 + 全文检索时用它。 | GPL-3.0 | B（5/6） | [中](categories/document-management/paperless-ngx.zh.md) · [EN](categories/document-management/paperless-ngx.md) |
| **copyparty** | 需要单文件便携、带断点续传/去重/多协议访问的文件服务器时用它——但它不做 OCR 文档检索。 | MIT | B（6/6） | [中](categories/document-management/copyparty.zh.md) · [EN](categories/document-management/copyparty.md) |
| **Twake Drive** | 当你想在 Twake/Cozy 栈里要一个 Google-Drive 形态的自托管文件网盘（而非 OCR 归档）时用它。 | AGPL-3.0 | B（5/6） | [中](categories/document-management/twake-drive.zh.md) · [EN](categories/document-management/twake-drive.md) |
| **Immich** | 想要一个自托管的 Google Photos 替代品，带 AI 人脸识别、物体识别、智能搜索与移动端同步时用它——但需要大量服务器资源（内存、存储、GPU 跑 ML）。 | AGPL-3.0 | B（6/6） | [中](categories/document-management/immich.zh.md) · [EN](categories/document-management/immich.md) |

### on-device-ml

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **LiteRT-LM** | 想用 Google LiteRT 运行时在手机/笔记本/边缘（CPU/GPU/NPU）上跑 Gemma 级 LLM 时用它。 | Apache-2.0 | B（6/6） | [中](categories/on-device-ml/litert-lm.zh.md) · [EN](categories/on-device-ml/litert-lm.md) |
| **BitNet** | 当你要在 x86/ARM 笔记本上离线、快速、低能耗地用 CPU 跑原生三值（1.58-bit） LLM 时使用。 | MIT | C（6/6） | [中](categories/on-device-ml/bitnet.zh.md) · [EN](categories/on-device-ml/bitnet.md) |
| **Google AI Edge Gallery** | 当你想在真机上先体验和基准测试端侧 Gemma LLM、为是否自建集成去风险时用它。 | Apache-2.0 | A（5/6） | [中](categories/on-device-ml/ai-edge-gallery.zh.md) · [EN](categories/on-device-ml/ai-edge-gallery.md) |
| **TimesFM** | 当你需要在本地 CPU/GPU 上对时间序列做零样本预测、又不想逐数据集训练时用它。 | Apache-2.0 | B（5/6） | [中](categories/on-device-ml/timesfm.zh.md) · [EN](categories/on-device-ml/timesfm.md) |
| **MiniCPM-V** | 当你需要小体积、可在端侧/边缘运行的多模态（图像+视频）理解时用它——注意逐权重许可。 | Apache-2.0 | A（4/6） | [中](categories/on-device-ml/minicpm-v.zh.md) · [EN](categories/on-device-ml/minicpm-v.md) |
| **Stable Diffusion WebUI** | 当你想在自有 GPU 上用本地 Web GUI 进行 Stable Diffusion 图像生成、编辑和超分时用它——但需要技术 setup 和 NVIDIA GPU。 | AGPL-3.0 | C（4/6） | [中](categories/on-device-ml/stable-diffusion-webui.zh.md) · [EN](categories/on-device-ml/stable-diffusion-webui.md) |
| **ComfyUI** | 最强大、最模块化的扩散模型 GUI，带节点图界面，用于在本地构建复杂工作流——但学习曲线陡峭，需要大量 GPU 资源。 | GPL-3.0 | B（5/6） | [中](categories/on-device-ml/comfyui.zh.md) · [EN](categories/on-device-ml/comfyui.md) |
| **MLX / mlx-lm** | Run LLMs with MLX | MIT | B（6/6） | [EN](categories/on-device-ml/mlx-mlx-lm.md) · [中](categories/on-device-ml/mlx-mlx-lm.zh.md) |
| **Needle** | 当需要一个小体积端侧模型离线完成工具调用、类型化抽取与嵌入时用它——它用通用聊天换取 8–29 MB 的任务准确率。 | Apache-2.0 | B（4/6） | [中](categories/on-device-ml/needle.zh.md) · [EN](categories/on-device-ml/needle.md) |

### function-calling

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Functionary** | 只把它当作开源 JSON Schema 函数调用的历史参考——它已废弃；生产环境请用 vLLM/SGLang 服务当前模型，或走端侧 Needle。 | MIT | B（3/6） | [中](categories/function-calling/functionary.zh.md) · [EN](categories/function-calling/functionary.md) |

### web-automation

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **page-agent** | 想在页内用自然语言、通过直接读写 DOM 控制 Web 界面、且无需后端时用它。 | MIT | B（6/6） | [中](categories/web-automation/agent-browser-tools/page-agent.zh.md) · [EN](categories/web-automation/agent-browser-tools/page-agent.md) |
| **Chrome DevTools MCP** | 当 agent 需要驱动并用 DevTools 检查真实 Chrome（性能 trace、网络、控制台、堆内存）时使用。 | Apache-2.0 | A（6/6） | [中](categories/web-automation/agent-browser-tools/chrome-devtools-mcp.zh.md) · [EN](categories/web-automation/agent-browser-tools/chrome-devtools-mcp.md) |
| **Cua** | 当 agent 需要在隔离 VM 沙箱里用视觉操作整台桌面系统（而非仅网页）时使用。 | MIT | B（6/6） | [中](categories/web-automation/agent-browser-tools/cua.zh.md) · [EN](categories/web-automation/agent-browser-tools/cua.md) |
| **Agent Browser** | 当 agent 需要靠 shell 命令通过 CDP 驱动真实 Chrome、用稳定元素引用而非 CSS 选择器操作网页时使用。 | Apache-2.0 | B（6/6） | [中](categories/web-automation/agent-browser-tools/agent-browser.zh.md) · [EN](categories/web-automation/agent-browser-tools/agent-browser.md) |
| **Selenium** | 当你需要跨浏览器、跨语言的 WebDriver 自动化时用它——现代单浏览器体验 Playwright/Cypress 更顺手。 | Apache-2.0 | B（6/6） | [中](categories/web-automation/browser-driver-frameworks/selenium.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/selenium.md) |
| **PhantomJS** | 新项目别用——已归档、停更的可脚本化无头浏览器；改用 Puppeteer/Playwright 的无头 Chrome 或 Selenium。 | BSD-3-Clause | D（5/6） | [中](categories/web-automation/browser-driver-frameworks/phantomjs.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/phantomjs.md) |
| **Selenium Wire** | 当遗留的 Selenium 测试套件需要读取或改写浏览器后台 HTTP 流量时用它——但它已归档，新项目应改用 Selenium 4 原生 CDP/BiDi 或 Playwright。 | MIT | D（5/6） | [中](categories/web-automation/browser-driver-frameworks/selenium-wire.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/selenium-wire.md) |
| **nodriver** | 当 Python 异步代码需要绕过 WebDriver、直接控制 Chromium CDP 时用它——只支持 Chromium、采用 AGPL-3.0，且不是完整测试框架。 | AGPL-3.0 | C（5/6） | [中](categories/web-automation/browser-driver-frameworks/nodriver.zh.md) · [EN](categories/web-automation/browser-driver-frameworks/nodriver.md) |
| **Playwright MCP** | 当支持 MCP 的 agent 需要厂商官方、基于无障碍树快照的确定性浏览器自动化时用它——适合有状态的探索式回路；微软自家 README 把高吞吐 coding agent 引向它的 CLI 兄弟。 | Apache-2.0 | A（6/6） | [中](categories/web-automation/playwright-family/playwright-mcp.zh.md) · [EN](categories/web-automation/playwright-family/playwright-mcp.md) |
| **Playwright CLI** | 当 coding agent（Claude Code、Copilot）需要便宜、token 高效的浏览器命令并装好 SKILLs 时用它——微软自己推荐给 coding agent 的路径；v0.1.x，刚重新定位。 | Apache-2.0 | A（5/6） | [中](categories/web-automation/playwright-family/playwright-cli.zh.md) · [EN](categories/web-automation/playwright-family/playwright-cli.md) |
| **OpenCLI** | 当 agent 必须操作藏在你登录态后面的站点时用它——经扩展+daemon 桥接你已登录的 Chrome，并把站点工作流固化成可复用 CLI 命令；要预期适配器 churn 和真实的信任面。 | Apache-2.0 | B（6/6） | [中](categories/web-automation/agent-browser-tools/opencli.zh.md) · [EN](categories/web-automation/agent-browser-tools/opencli.md) |
| **browser-use** | 🌐 Make websites accessible for AI agents. Automate tasks online with ease. | MIT | B（6/6） | [EN](categories/web-automation/agent-browser-tools/browser-use.md) · [中](categories/web-automation/agent-browser-tools/browser-use.zh.md) |
| **BrowserSkill** | 当 agent 必须在不动你现有窗口的前提下操作你已登录的 Chromium 时用它——借你已打开的页签要先经你确认，遇到登录或验证码把控制权交还给你；没有确定性站点适配器层，信任面与 OpenCLI 同级（扩展+daemon）。 | MIT | B（6/6） | [中](categories/web-automation/agent-browser-tools/browserskill.zh.md) · [EN](categories/web-automation/agent-browser-tools/browserskill.md) |
| **Playwright** | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. | Apache-2.0 | A（5/6） | [EN](categories/web-automation/playwright-family/playwright.md) · [中](categories/web-automation/playwright-family/playwright.zh.md) |
| **Puppeteer** | JavaScript API for Chrome and Firefox | Apache-2.0 | A（5/6） | [EN](categories/web-automation/browser-driver-frameworks/puppeteer.md) · [中](categories/web-automation/browser-driver-frameworks/puppeteer.zh.md) |

### llm-training

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **LlamaFactory** | 面向 100+ LLM/VLM 的零代码统一微调框架，自带 Gradio Web UI(LlamaBoard)，覆盖 LoRA/QLoRA/全量微调及 SFT→RLHF 全链路。 | Apache-2.0 | B（6/6） | [中](categories/llm-training/llamafactory.zh.md) · [EN](categories/llm-training/llamafactory.md) |
| **Unsloth** | 基于自定义 Triton kernel 的单卡 LoRA/QLoRA/RL 微调工具，号称在 500+ 开源 LLM 上约 2x 提速并大幅省显存。 | Apache-2.0 | A（6/6） | [中](categories/llm-training/unsloth.zh.md) · [EN](categories/llm-training/unsloth.md) |
| **ART (Agent Reinforcement Trainer)** | 当 Python 命令行需要纯 Python 的 figlet 风格 ASCII 文字横幅、且不依赖系统二进制时用它——但它只做文字转艺术字（不做图片转 ASCII），也不与 figlet 字体完全一致。 | Apache-2.0 | B（5/6） | [中](categories/llm-training/art.zh.md) · [EN](categories/llm-training/art.md) |
| **Agent Lightning** | 微软出品的强化学习/优化训练器，把 agent 执行与训练后端解耦，几乎零改动地优化任意框架（LangChain、AutoGen、OpenAI SDK 等）构建的 agent。 | MIT | B（5/6） | [中](categories/llm-training/agent-lightning.zh.md) · [EN](categories/llm-training/agent-lightning.md) |
| **Colossal-AI** | 当你需要用张量/流水线/ZeRO 并行在多 GPU 上训练/微调大模型时用它——单卡 LoRA 用它是杀鸡用牛刀。 | Apache-2.0 | B（5/6） | [中](categories/llm-training/colossalai.zh.md) · [EN](categories/llm-training/colossalai.md) |
| **Hugging Face TRL** | Train transformer language models with reinforcement learning. | Apache-2.0 | A（6/6） | [EN](categories/llm-training/trl.md) · [中](categories/llm-training/trl.zh.md) |
| **torchtune** | PyTorch native post-training library | BSD-3-Clause | B（5/6） | [EN](categories/llm-training/torchtune.md) · [中](categories/llm-training/torchtune.zh.md) |
| **Axolotl** | Go ahead and axolotl questions | Apache-2.0 | B（6/6） | [EN](categories/llm-training/axolotl.md) · [中](categories/llm-training/axolotl.zh.md) |
| **verl** | verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework | Apache-2.0 | B（6/6） | [EN](categories/llm-training/verl.md) · [中](categories/llm-training/verl.zh.md) |
| **Soup** | 当一份 YAML 要把微调从 JSONL 一路带到可服务、可导出的模型，而底座装不进你的显卡时用它——当配置契约必须跨版本稳定、或模型本就装得下且要追求速度时不用。 | Apache-2.0 | B（6/6） | [中](categories/llm-training/soup.zh.md) · [EN](categories/llm-training/soup.md) |
| **MiniMind** | 用约 3.2k 行手写 PyTorch 把 64M LLM 端到端训一遍（分词器、预训练、SFT、LoRA、MoE、DPO/GRPO、Tool Call 与 Agentic RL），一下午能读完；它是课程，产出的模型是教学产物而非可用模型。 | Apache-2.0 | A（5/6） | [中](categories/llm-training/study-and-experiments/minimind.zh.md) · [EN](categories/llm-training/study-and-experiments/minimind.md) |
| **nanoGPT** | 最经典的极简 GPT 训练参考——约 670 行可读代码、支持 MPS/CPU、checkpoint 与 OpenAI 的 GPT-2 互通；但它只到预训练，没有 SFT 与 RL，且 README 自己已宣布被 nanochat 取代。 | MIT | C（4/6） | [中](categories/llm-training/study-and-experiments/nanogpt.zh.md) · [EN](categories/llm-training/study-and-experiments/nanogpt.md) |

### agent-frameworks

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **DSPy** | 你有评测数据和指标、想让优化器编译提示词而非手工调时。 | MIT | A（6/6） | [中](categories/agent-frameworks/workflow-builders/dspy.zh.md) · [EN](categories/agent-frameworks/workflow-builders/dspy.md) |
| **AgentScope** | 要把多智能体 LLM 应用作为生产服务交付，需要沙箱工具、权限闸门、tracing 和人工介入时。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/agent-runtimes/agent-sdks/agentscope.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/agentscope.md) |
| **OpenFang** | 想用单个自托管 Rust 二进制、让自治智能体按计划 7×24 无人值守干活时。 | Apache-2.0 OR MIT | B（5/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/openfang.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/openfang.md) |
| **Symphony** | 你的 Linear 待办和 Codex agent 需要一个自托管编排器、按 issue 跑隔离自治实现运行时。 | Apache-2.0 | C（5/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/symphony.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/symphony.md) |
| **Claude Octopus** | 你以 Claude Code 为主力、想让其他 AI 模型在交付前交叉评审任务、揭出盲点时。 | MIT | B（5/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/claude-octopus.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/claude-octopus.md) |
| **oh-my-claudecode** | 你常驻 Claude Code、需要多阶段 agent 团队加模型路由和 tmux 并行编排时。 | MIT | B（5/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/oh-my-claudecode.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/oh-my-claudecode.md) |
| **smolagents** | 当你想要 Hugging Face 出的极简、透明、写代码行动的 agent 循环时用它——不是重型生产 agent 操作系统。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/agent-runtimes/agent-sdks/smolagents.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/smolagents.md) |
| **Kilo Code** | 当你想要一个开源、BYOK、在 VS Code 内的编码 agent（带规划与模式）时用它——是终端用户工具，不是构建 agent 的库。 | MIT | B（6/6） | [中](categories/agent-frameworks/coding-agents/ide-agents/kilocode.zh.md) · [EN](categories/agent-frameworks/coding-agents/ide-agents/kilocode.md) |
| **Parlant** | 当你要构建一个必须靠行为准则严格守规的对客 agent 时用它——简单或自由式 agent 用它过重。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/parlant.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/parlant.md) |
| **SkillOpt** | 当你要针对可打分基准、为冻结的 LLM 优化 Agent 的自然语言技能文档时用它——但没有可靠评测来把关每次编辑，方法就毫无信号，且它还是全新的 v0.1.0。 | MIT | B（6/6） | [中](categories/agent-frameworks/workflow-builders/skillopt.zh.md) · [EN](categories/agent-frameworks/workflow-builders/skillopt.md) |
| **Open Interpreter** | 当你想要一个 Codex-fork 的终端编码 agent、带为低成本／开源模型（DeepSeek、Kimi、Qwen）调过的可切换 harness 时用它——不是老的 Python REPL（那个已迁到社区 fork），而且它是几周大的 0.0.x 重写、会执行代码。 | Apache-2.0 | B（6/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/open-interpreter.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/open-interpreter.md) |
| **Codex** | 当你想要一个轻量级、由 OpenAI 支持的终端编码智能体，能编辑文件、运行测试并提交变更时用它——但需要 OpenAI API 访问权限和网络连接。 | Apache-2.0 | A（5/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/codex.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/codex.md) |
| **OpenClaw** | 在自有设备上跨 20 余条消息渠道运行的个人 AI 助手——但极其年轻，毫无 Lindy 记录。 | MIT | B（4/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/openclaw.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/openclaw.md) |
| **OpenHuman** | 本地优先的个人 AI 助手：每 20 分钟把邮件、日历、仓库灌成本机 Markdown 记忆，并能在 Rust 内核里强制断网——但它只有 7 个月，绝大多数提交来自一个人，许可是 GPL-3.0-only。 | GPL-3.0-only | B（5/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/openhuman.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/openhuman.md) |
| **CC Switch** | 跨平台桌面管理器，统一管理多个 AI 编码智能体（Claude Code、Codex、Gemini CLI 等），支持提供商路由和 MCP——但不足一岁，单人维护，bus factor 为 1。 | MIT | B（4/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/cc-switch.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/cc-switch.md) |
| **Hermes Agent** | Nous Research 构建的带学习循环的自我改进 AI 智能体——但不足一岁，学习循环稳定性未经检验。 | MIT | B（5/6） | [中](categories/agent-frameworks/agent-runtimes/personal-assistants/hermes-agent.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/personal-assistants/hermes-agent.md) |
| **AutoGPT** | 用于创建、部署和管理持续运行 AI 智能体以自动化复杂工作流的平台——但未声明许可，且自托管需要大量资源。 | NOASSERTION | A（4/6） | [中](categories/agent-frameworks/workflow-builders/autogpt.zh.md) · [EN](categories/agent-frameworks/workflow-builders/autogpt.md) |
| **Dify** | 生产就绪的、用于构建 agentic 工作流的低代码可视化平台，内置 RAG 与 MCP 支持——但商用前请核实许可。 | NOASSERTION | B（5/6） | [中](categories/agent-frameworks/workflow-builders/dify.zh.md) · [EN](categories/agent-frameworks/workflow-builders/dify.md) |
| **LangChain** | 代码优先的 LLM agent、工具与记忆组合框架，集成生态庞大——但简单单 prompt 应用别用它。 | MIT | A（6/6） | [中](categories/agent-frameworks/workflow-builders/langchain.zh.md) · [EN](categories/agent-frameworks/workflow-builders/langchain.md) |
| **OpenCode** | 开源终端 AI 编码智能体，可编辑文件、执行命令——但极其年轻（2025-04 创建），无 Lindy 记录。 | MIT | B（5/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/opencode.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/opencode.md) |
| **Langflow** | 可视化拖拽平台，用于构建和部署 LLM 工作流与智能体，内置 API 和 MCP 服务器——但可视化流比代码更难做 diff/审查。 | MIT | A（6/6） | [中](categories/agent-frameworks/workflow-builders/langflow.zh.md) · [EN](categories/agent-frameworks/workflow-builders/langflow.md) |
| **Gemini CLI** | 基于 Google Gemini 模型的开源终端 AI 智能体，带免费层、内置工具和 MCP 支持——但仅限 Google 模型，且非常年轻。 | Apache-2.0 | B（5/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/gemini-cli.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/gemini-cli.md) |
| **RTK** | 在 shell 输出到达 AI 智能体前进行压缩的 CLI 代理，可减少 60–90% 的 token 成本——但极其年轻（6 个月），star 数高得可疑。 | Apache-2.0 | B（5/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/rtk.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/rtk.md) |
| **CrewAI** | Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. | MIT | A（6/6） | [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/crewai.md) · [中](categories/agent-frameworks/agent-runtimes/agent-sdks/crewai.zh.md) |
| **LangGraph** | Build resilient agents. | MIT | A（6/6） | [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/langgraph.md) · [中](categories/agent-frameworks/agent-runtimes/agent-sdks/langgraph.zh.md) |
| **LlamaIndex** | LlamaIndex is the leading document agent and OCR platform | MIT | A（6/6） | [EN](categories/agent-frameworks/workflow-builders/llamaindex.md) · [中](categories/agent-frameworks/workflow-builders/llamaindex.zh.md) |
| **AutoGen** | A programming framework for agentic AI | CC-BY-4.0 | C（6/6） | [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/autogen.md) · [中](categories/agent-frameworks/agent-runtimes/agent-sdks/autogen.zh.md) |
| **Pydantic AI** | AI Agent Framework, the Pydantic way | MIT | A（5/6） | [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/pydantic-ai.md) · [中](categories/agent-frameworks/agent-runtimes/agent-sdks/pydantic-ai.zh.md) |
| **OpenAI Agents SDK** | A lightweight, powerful framework for multi-agent workflows | MIT | A（6/6） | [EN](categories/agent-frameworks/agent-runtimes/agent-sdks/openai-agents-sdk.md) · [中](categories/agent-frameworks/agent-runtimes/agent-sdks/openai-agents-sdk.zh.md) |
| **Claude Commerce Agents** | 你要在一个卖东西的产品（零售、旅游、票务、电信）里做助手，想直接拿到购物/商家 agent 这一层（prompt、护栏、UI 回填、暂存审批）——当作一份读来 vendor 的蓝图，而不是装来用的依赖。 | Apache-2.0 | C（5/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/commerce-agents.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/commerce-agents.md) |
| **eve** | 你的 agent 要为一个人或一个 webhook 等上好几天、要扛住重新部署，还要能在 Slack／Discord／Teams 上应答——并且是一个可部署的 TypeScript 服务。 | Apache-2.0 | A（6/6） | [中](categories/agent-frameworks/agent-runtimes/agent-services/eve.zh.md) · [EN](categories/agent-frameworks/agent-runtimes/agent-services/eve.md) |
| **aider** | aider is AI pair programming in your terminal | Apache-2.0 | B（6/6） | [EN](categories/agent-frameworks/coding-agents/terminal-agents/aider.md) · [中](categories/agent-frameworks/coding-agents/terminal-agents/aider.zh.md) |
| **Cline** | Autonomous coding agent as an SDK, IDE extension, or CLI assistant. | Apache-2.0 | A（6/6） | [EN](categories/agent-frameworks/coding-agents/ide-agents/cline.md) · [中](categories/agent-frameworks/coding-agents/ide-agents/cline.zh.md) |
| **SWE-agent** | SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024] | MIT | A（5/6） | [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/swe-agent.md) · [中](categories/agent-frameworks/coding-agents/orchestration-and-review/swe-agent.zh.md) |
| **Flowise** | Build AI Agents, Visually | NOASSERTION | A（4/6） | [EN](categories/agent-frameworks/workflow-builders/flowise.md) · [中](categories/agent-frameworks/workflow-builders/flowise.zh.md) |
| **OpenHands** | 🙌 OpenHands: AI-Driven Development | NOASSERTION | A（4/6） | [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/openhands.md) · [中](categories/agent-frameworks/coding-agents/orchestration-and-review/openhands.zh.md) |
| **T3 Code** | 当一个本地 GUI 要驱动已经认证的 Codex、Claude、Cursor、OpenCode CLI 时用它。 | MIT | B（6/6） | [中](categories/agent-frameworks/coding-agents/terminal-agents/t3code.zh.md) · [EN](categories/agent-frameworks/coding-agents/terminal-agents/t3code.md) |
| **Background Agents（Open-Inspect）** | 当一个可信组织需要自托管的后台 coding-agent 沙箱、集成和自动化时用它。 | MIT | B（5/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/background-agents.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/background-agents.md) |
| **SwarmForge** | 当你想要一个自托管的角色流水线（spec→code→clean→architect→harden→QA）跑在自己的仓库上、每个角色一个 git worktree、以 commit 交接时用它——但它没有许可证，也没有 tagged release。 | NONE（无 LICENSE 文件——保留所有权利） | D（6/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/swarm-forge.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/swarm-forge.md) |
| **OpenChamber** | 当你用 OpenCode，想要一个跨设备的运行工作台——按目标审计的会话、一条提示词最多五个模型（可各带 worktree）、变更讲解，以及紧挨对话的 git/PR 面板——但要接受一个 12 个月大、单人主控、只绑一个 agent runtime 的应用时用它。 | MIT | C（5/6） | [中](categories/agent-frameworks/coding-agents/orchestration-and-review/openchamber.zh.md) · [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/openchamber.md) |

| **kagent** | 当 agent 应该是 Kubernetes 对象时用它——用 YAML 声明、由控制器与引擎运行，带模型配置、MCP 工具服务器与 OpenTelemetry 追踪。 | Apache-2.0 | — | [中](categories/agent-frameworks/kubernetes-agents/kagent.zh.md) · [EN](categories/agent-frameworks/kubernetes-agents/kagent.md) |

### agent-memory

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Mem0** | 当你的 LLM agent 需要跨会话记住用户、又不想撑爆 prompt 上下文时用它。 | Apache-2.0 | A（6/6） | [中](categories/agent-memory/mem0.zh.md) · [EN](categories/agent-memory/mem0.md) |
| **Memori** | 当你想要 LLM 无关、通过包裹现有客户端自动捕获并召回的持久化 agent 记忆时使用。 | Apache-2.0 | B（5/6） | [中](categories/agent-memory/memori.zh.md) · [EN](categories/agent-memory/memori.md) |
| **Claude Subconscious** | 当你想让一个后台 Letta agent 通过 hook 给 Claude Code 加上跨会话记忆时使用（仅 demo，非生产）。 | MIT | C（6/6） | [中](categories/agent-memory/claude-subconscious.zh.md) · [EN](categories/agent-memory/claude-subconscious.md) |
| **claude-mem** | 当你的编码 agent 跨会话丢失上下文、你想要本地 hook/MCP 捕获并压缩后再注入的记忆时用它（star 数存疑）。 | Apache-2.0 | B（6/6） | [中](categories/agent-memory/claude-mem.zh.md) · [EN](categories/agent-memory/claude-mem.md) |
| **ByteRover CLI** | 当你想要一款可移植的、带 git 式版本控制和云同步的结构化编码 agent 记忆层时用它——但它极其年轻（2025-06 创建），且许可情况模糊。 | NOASSERTION | D（6/6） | [中](categories/agent-memory/byterover.zh.md) · [EN](categories/agent-memory/byterover.md) |
| **Letta (MemGPT)** | Platform for stateful agents: AI with advanced memory that can learn and self-improve over time. | Apache-2.0 | B（5/6） | [EN](categories/agent-memory/letta.md) · [中](categories/agent-memory/letta.zh.md) |
| **Zep** | Zep \| Examples, Integrations, & More | Apache-2.0 | A（4/6） | [EN](categories/agent-memory/zep.md) · [中](categories/agent-memory/zep.zh.md) |
| **Graphiti** | Build Real-Time Knowledge Graphs for AI Agents | Apache-2.0 | B（6/6） | [EN](categories/agent-memory/graphiti.md) · [中](categories/agent-memory/graphiti.zh.md) |
| **LangMem** | 当你需要在 agent-memory 方向评估 LangMem 时用它。 | MIT | B（5/6） | [EN](categories/agent-memory/langmem.md) · [中](categories/agent-memory/langmem.zh.md) |
| **Cognee** | Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine. | Apache-2.0 | A（6/6） | [EN](categories/agent-memory/cognee.md) · [中](categories/agent-memory/cognee.zh.md) |
| **OpenViking** | 当多个编码 agent 或一个团队需要共用同一份既装文档又装长期记忆的存储、且你能跑一个服务端时用它——但主仓是 AGPL-3.0，仓库自标 alpha。 | AGPL-3.0 | B（6/6） | [EN](categories/agent-memory/openviking.md) · [中](categories/agent-memory/openviking.zh.md) |

### deep-research

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **deep-research** | 想要一个极简可读、约 500 行的 TypeScript 深度研究 agent 作为 fork 底座时用它。 | MIT | C（4/6） | [中](categories/deep-research/deep-research.zh.md) · [EN](categories/deep-research/deep-research.md) |
| **Vane** | 想要一个自托管、注重隐私的「Perplexity 式」带引用应答引擎，接你自己的 SearxNG 和自选 LLM 时用它。 | MIT | B（5/6） | [中](categories/deep-research/vane.zh.md) · [EN](categories/deep-research/vane.md) |
| **Local Deep Research** | 当你需要一个自托管、可纯本地运行的深度研究 agent、把敏感查询留在自己机器上时用它。 | MIT | B（6/6） | [中](categories/deep-research/local-deep-research.zh.md) · [EN](categories/deep-research/local-deep-research.md) |
| **Agent-Reach** | 当你的 agent 需要免付费 API 地读取和搜索网页与社交平台内容时用它。 | MIT | B（4/6） | [中](categories/deep-research/agent-reach.zh.md) · [EN](categories/deep-research/agent-reach.md) |
| **MiroThinker** | 当你想要一个可在自有 GPU 上研究改造的自托管开源深研 Agent 时用它——但它要 GPU 集群加付费外部 API，且不到一岁、毫无 Lindy 沉淀。 | Apache-2.0 | C（6/6） | [中](categories/deep-research/mirothinker.zh.md) · [EN](categories/deep-research/mirothinker.md) |
| **GPT Researcher** | An autonomous agent that conducts deep research on any data using any LLM providers | Apache-2.0 | B（6/6） | [EN](categories/deep-research/gpt-researcher.md) · [中](categories/deep-research/gpt-researcher.zh.md) |
| **Open Deep Research** | 当你需要在 deep-research 方向评估 Open Deep Research 时用它。 | MIT | A（5/6） | [EN](categories/deep-research/open-deep-research.md) · [中](categories/deep-research/open-deep-research.zh.md) |
| **STORM** | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. | MIT | C（5/6） | [EN](categories/deep-research/storm.md) · [中](categories/deep-research/storm.zh.md) |
| **node-DeepResearch** | Keep searching, reading webpages, reasoning until it finds the answer (or exceeding the token budget) | Apache-2.0 | C（5/6） | [EN](categories/deep-research/node-deepresearch.md) · [中](categories/deep-research/node-deepresearch.zh.md) |
| **Hyperresearch** | 当你在 Claude Code 里、需要一份引用逐条核验的高风险研究报告时用它——16 步对抗式流水线加持久来源 vault；时间与 token 开销都重，且只支持 Claude Code。 | MIT | B（5/6） | [中](categories/deep-research/hyperresearch.zh.md) · [EN](categories/deep-research/hyperresearch.md) |

### ai-code-review

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Open Code Review** | 想在 CI 里对 Git diff 拿到精确行级 LLM review 评论、又不被噪声淹没时用它。 | Apache-2.0 | B（6/6） | [中](categories/ai-code-review/open-code-review.zh.md) · [EN](categories/ai-code-review/open-code-review.md) |
| **Claude Code Security Review** | 当你想用 Claude 在可信 PR 上做上下文感知的安全审查、且接受按 token 计费与非确定性结果时使用。 | MIT | C（5/6） | [中](categories/ai-code-review/claude-code-security-review.zh.md) · [EN](categories/ai-code-review/claude-code-security-review.md) |
| **React Doctor** | 当 coding agent 在写 React、你想要对 React 特有反模式做确定性、可重复的检查时用它。 | LicenseRef-Modified-MIT | B（5/6） | [中](categories/ai-code-review/react-doctor.zh.md) · [EN](categories/ai-code-review/react-doctor.md) |
| **PR-Agent** | 🚀 PR Agent: The Original Open-Source PR Reviewer.  This project It is not the Qodo free tier. | Apache-2.0 | A（6/6） | [EN](categories/ai-code-review/pr-agent.md) · [中](categories/ai-code-review/pr-agent.zh.md) |
| **Metis** | Metis is an open-source, AI-driven tool for deep security code review | Apache-2.0 | B（5/6） | [EN](categories/ai-code-review/metis.md) · [中](categories/ai-code-review/metis.zh.md) |
| **OpenReview** | An open-source, self-hosted AI code review bot powered by Vercel. | NOASSERTION | D（4/6） | [EN](categories/ai-code-review/openreview.md) · [中](categories/ai-code-review/openreview.zh.md) |

### rag-retrieval

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **FalkorDB** | 当 GraphRAG 需要在一个低延迟、嵌入 Redis 的引擎里把向量相似与多跳图遍历结合时使用。 | SSPL-1.0 | A（4/6） | [中](categories/rag-retrieval/falkordb.zh.md) · [EN](categories/rag-retrieval/falkordb.md) |
| **graphify** | 当 agent 需要把整个仓库的代码、schema 和文档当成知识图谱来查询、而非反复 grep 时用它。 | MIT | B（6/6） | [中](categories/rag-retrieval/graphify.zh.md) · [EN](categories/rag-retrieval/graphify.md) |
| **code-review-graph** | 当 AI 评审在大仓库里反复烧上下文、你只想喂给它一次改动真正触及（blast-radius）的文件时用它。 | MIT | B（6/6） | [中](categories/rag-retrieval/code-review-graph.zh.md) · [EN](categories/rag-retrieval/code-review-graph.md) |
| **PageIndex** | 当向量 RAG 在少量长而有结构的文档上召回相似但不相关的块、且你需要可溯源引用时使用。 | MIT | B（5/6） | [中](categories/rag-retrieval/pageindex.zh.md) · [EN](categories/rag-retrieval/pageindex.md) |
| **Understand-Anything** | 当你想把任意代码库变成可探索、可提问的知识图谱给 agent 用时用它——比 graphify 更年轻、未经检验。 | MIT | B（5/6） | [中](categories/rag-retrieval/understand-anything.zh.md) · [EN](categories/rag-retrieval/understand-anything.md) |
| **FAISS** | 当你需要一个快速的进程内 ANN 向量索引来检索 embedding 时用它——是库，不是托管向量数据库。 | MIT | A（6/6） | [中](categories/rag-retrieval/faiss.zh.md) · [EN](categories/rag-retrieval/faiss.md) |
| **text2vec** | 当你要为中文语义检索或 FAQ 匹配快速拿到句向量、只想一行 pip 装好时用它——它只是编码器，向量索引（FAISS／Milvus）得自己配。 | Apache-2.0 | C（5/6） | [中](categories/rag-retrieval/text2vec.zh.md) · [EN](categories/rag-retrieval/text2vec.md) |
| **SCIP** | SCIP Code Intelligence Protocol | Apache-2.0 | A（6/6） | [EN](categories/rag-retrieval/scip.md) · [中](categories/rag-retrieval/scip.zh.md) |
| **Milvus** | Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search | Apache-2.0 | A（4/6） | [EN](categories/rag-retrieval/milvus.md) · [中](categories/rag-retrieval/milvus.zh.md) |
| **Sourcegraph** | Code AI platform with Code Search & Cody | NOASSERTION | E（3/6） | [EN](categories/rag-retrieval/sourcegraph.md) · [中](categories/rag-retrieval/sourcegraph.zh.md) |

### llm-eval

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **promptfoo** | 当你要用声明式 YAML 给自己的 LLM 应用做评测+红队并接进 CI 时用它。 | MIT | A（6/6） | [中](categories/llm-eval/promptfoo.zh.md) · [EN](categories/llm-eval/promptfoo.md) |
| **Pezzo** | 当小团队想要一个自托管的统一控制台来做 prompt 版本管理加成本／延迟可观测时用它——但它自 2025 年中起疑似停更，请做好自己维护的准备。 | Apache-2.0 | C（4/6） | [中](categories/llm-eval/pezzo.zh.md) · [EN](categories/llm-eval/pezzo.md) |
| **DeepEval** | The LLM Evaluation Framework | Apache-2.0 | A（6/6） | [EN](categories/llm-eval/deepeval.md) · [中](categories/llm-eval/deepeval.zh.md) |
| **Ragas** | Supercharge Your LLM Application Evaluations 🚀 | Apache-2.0 | B（6/6） | [EN](categories/llm-eval/ragas.md) · [中](categories/llm-eval/ragas.zh.md) |
| **garak** | the LLM vulnerability scanner | Apache-2.0 | A（6/6） | [EN](categories/llm-eval/garak.md) · [中](categories/llm-eval/garak.zh.md) |
| **Giskard OSS** | 🐢 Open-Source Evaluation & Testing library for LLM Agents | Apache-2.0 | B（6/6） | [EN](categories/llm-eval/giskard.md) · [中](categories/llm-eval/giskard.zh.md) |
| **Langfuse** | 🪢 Open source AI engineering platform: LLM evals, observability, metrics, prompt management, playground, datasets. Integrates with OpenTelemetry, LangChain, OpenAI SDK, LiteLLM, and more. 🍊YC W23 | NOASSERTION | A（4/6） | [EN](categories/llm-eval/langfuse.md) · [中](categories/llm-eval/langfuse.zh.md) |

### agent-dev-methodology

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **12-Factor Agents** | 当你想用一套生产级 agent 设计原则来指导手写或薄框架 agent 时使用。 | CC-BY-SA-4.0 (content) / Apache-2.0 (code examples) | C（3/6） | [中](categories/agent-dev-methodology/spec-driven-development/12-factor-agents.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/12-factor-agents.md) |
| **Superpowers** | 当你想给编程 agent 装一套即插即用的「头脑风暴→计划→TDD→验证」SDLC 方法论时用它。 | MIT | B（4/6） | [中](categories/agent-dev-methodology/coding-agent-harnesses/superpowers.zh.md) · [EN](categories/agent-dev-methodology/coding-agent-harnesses/superpowers.md) |
| **SuperClaude Framework** | 当你常驻 Claude Code、想一次装好现成的命令、agent 和行为模式框架时用它。 | MIT | B（4/6） | [中](categories/agent-dev-methodology/coding-agent-harnesses/superclaude.zh.md) · [EN](categories/agent-dev-methodology/coding-agent-harnesses/superclaude.md) |
| **Get Shit Done (GSD)** | 当你靠 coding agent 写代码、想要一条规格驱动、每阶段全新上下文、对抗 context rot 的构建流水线时用它。 | MIT | C（6/6） | [中](categories/agent-dev-methodology/spec-driven-development/get-shit-done.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/get-shit-done.md) |
| **Compound Engineering** | 当你想要一套即插即用的 brainstorm→plan→work→review→compound 循环、并把经验跨会话沉淀复用时，就用它。 | MIT | B（4/6） | [中](categories/agent-dev-methodology/coding-agent-harnesses/compound-engineering.zh.md) · [EN](categories/agent-dev-methodology/coding-agent-harnesses/compound-engineering.md) |
| **ECC** | 当你想要一套有人维护、开箱即全的 Claude Code 底座（skill、agent、hook、memory 加安全扫描）时用它。 | MIT | B（6/6） | [中](categories/agent-dev-methodology/coding-agent-harnesses/ecc.zh.md) · [EN](categories/agent-dev-methodology/coding-agent-harnesses/ecc.md) |
| **Spec Kit** | GitHub 出品的面向 AI 编码智能体的 spec-driven 开发方法论——但它极其年轻，且与 GitHub 生态深度绑定。 | MIT | B（5/6） | [中](categories/agent-dev-methodology/spec-driven-development/spec-kit.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/spec-kit.md) |
| **Spec-Anchored Agentic Development** | 当永久 capability spec 必须持续充当代码一致性判定器时用它——仅面向 Claude Code，而且问世只有数天。 | MIT | B（3/6） | [中](categories/agent-dev-methodology/spec-driven-development/spec-anchored-agentic-development.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/spec-anchored-agentic-development.md) |
| **USDAD** | 当你想手工改造一套文字优先的多 agent 规格与上下文方法时用它——没有 CLI 或可执行约束。 | MIT | C（4/6） | [中](categories/agent-dev-methodology/spec-driven-development/usdad.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/usdad.md) |
| **QUAD Framework** | 仅当你要研究文档优先的四 Circles 运营模型与部署蓝图时使用——项目已不活跃、采用专有许可，且部分组件不可访问。 | Proprietary | D（4/6） | [中](categories/agent-dev-methodology/study-and-experiments/quad.zh.md) · [EN](categories/agent-dev-methodology/study-and-experiments/quad.md) |
| **LTBL Experiment** | 仅把它当作三个 agent 上下文实验实现的索引——自身没有可运行代码、实验结果或许可授权。 | NOASSERTION | D（4/6） | [中](categories/agent-dev-methodology/study-and-experiments/ltbl-experiment.zh.md) · [EN](categories/agent-dev-methodology/study-and-experiments/ltbl-experiment.md) |
| **PURE** | 当 intent 追溯需要 Git 原生 schema、registry、phase gate 和 Shell 检查时用它——结构明确，但非常年轻。 | MIT | C（5/6） | [中](categories/agent-dev-methodology/spec-driven-development/pure-agentic.zh.md) · [EN](categories/agent-dev-methodology/spec-driven-development/pure-agentic.md) |
| **Learn Claude Code** | 当你想通过亲手重建全部 17 个机制来搞懂 Claude Code 式 agent harness 的原理时用它——但它是课程，不是可 import 的库，也不是生产级 CLI。 | MIT | B（5/6） | [中](categories/agent-dev-methodology/study-and-experiments/learn-claude-code.zh.md) · [EN](categories/agent-dev-methodology/study-and-experiments/learn-claude-code.md) |

### ai-design-generation

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **HTML Anything** | 当你本机已登录某个 coding-agent CLI、想要零 API key、local-first 地把 Markdown 变成可交付 HTML 并一键导出微信/X/知乎时用它。 | Apache-2.0 | B（5/6） | [中](categories/ai-design-generation/html-anything.zh.md) · [EN](categories/ai-design-generation/html-anything.md) |
| **Open Design** | 想要一个 local-first、BYOK 的桌面 studio，让编码 agent 产出 HTML 原型、deck、图像和 HTML→MP4 动效时用它。 | Apache-2.0 | B（4/6） | [中](categories/ai-design-generation/open-design.zh.md) · [EN](categories/ai-design-generation/open-design.md) |
| **Impeccable** | 当你的 AI agent 总是产出同质化前端「AI 味」、需要确定性检测加设计 critique 时使用。 | Apache-2.0 | B（6/6） | [中](categories/ai-design-generation/impeccable.zh.md) · [EN](categories/ai-design-generation/impeccable.md) |
| **ian-xiaohei-illustrations** | 当你要为中文文章批量生成风格一致、带小黑 IP 的手绘 16:9 正文配图时用它。 | MIT | C（4/6） | [中](categories/agent-skills/visual-content/ian-illustrations.zh.md) · [EN](categories/agent-skills/visual-content/ian-illustrations.md) |
| **Guizang PPT Skill** | 当你想让 agent 把文章变成有设计感的单文件 HTML 翻页 PPT（杂志风或瑞士风）时用它。 | AGPL-3.0-only | C（4/6） | [中](categories/agent-skills/slides-ppt/guizang-ppt.zh.md) · [EN](categories/agent-skills/slides-ppt/guizang-ppt.md) |
| **Guizang Social Card Skill** | 当你在 Claude Code/Codex 里想让 agent 用锁定的编辑风/瑞士风生成小红书图文或公众号封面对（单文件 HTML 渲染成 PNG）时使用。 | AGPL-3.0-only | D（3/6） | [中](categories/agent-skills/visual-content/guizang-social-card.zh.md) · [EN](categories/agent-skills/visual-content/guizang-social-card.md) |
| **SdPaint** | 当你已在跑 AUTOMATIC1111＋ControlNet、想要一个实时草图转图的绘画循环时用它——但它自 2024 年起停滞，且自身不带任何模型。 | MIT | D（3/6） | [中](categories/ai-design-generation/sdpaint.zh.md) · [EN](categories/ai-design-generation/sdpaint.md) |
### dev-utilities

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **DevToys** | 想把 Base64/JSON/哈希/diff 等开发小工具离线本地化、收进一个跨平台桌面应用、不再用不可信在线网站时，用它。 | MIT | B（4/6） | [中](categories/dev-utilities/data-tools/devtoys.zh.md) · [EN](categories/dev-utilities/data-tools/devtoys.md) |
| **CyberChef** | 当你需要在浏览器里离线串联编解码、加解密、压缩和数据分析变换、且数据不能外发时用它。 | Apache-2.0 | B（5/6） | [中](categories/dev-utilities/data-tools/cyberchef.zh.md) · [EN](categories/dev-utilities/data-tools/cyberchef.md) |
| **Cockpit** | 当你需要为少数几台 Linux 服务器用浏览器做 systemd 原生的图形化管理时用它。 | LGPL-2.1-or-later | D（5/6） | [中](categories/dev-utilities/ops-infra/cockpit.zh.md) · [EN](categories/dev-utilities/ops-infra/cockpit.md) |
| **Telegraf** | 当你需要一个插件驱动的 agent 把异构指标/日志统一采集并路由到多种后端时用它。 | MIT | A（5/6） | [中](categories/dev-utilities/ops-infra/telegraf.zh.md) · [EN](categories/dev-utilities/ops-infra/telegraf.md) |
| **OpenZL** | 当你要把 TB 级的某种高度结构化/数值格式压得比通用 zstd 更狠时使用。 | BSD-3-Clause | B（4/6） | [中](categories/dev-utilities/data-tools/openzl.zh.md) · [EN](categories/dev-utilities/data-tools/openzl.md) |
| **Certbot** | 当系统管理员要自动签发并续期免费 Let's Encrypt TLS 证书时用它——不过反向代理自带的自动 TLS 常让它显得多余。 | Apache-2.0 | A（4/6） | [中](categories/dev-utilities/ops-infra/certbot.zh.md) · [EN](categories/dev-utilities/ops-infra/certbot.md) |
| **tqdm** | 当你想给 Python 循环/CLI/notebook 加一个快速、低开销的进度条时用它。 | MPL-2.0 AND MIT | B（4/6） | [中](categories/dev-utilities/data-tools/tqdm.zh.md) · [EN](categories/dev-utilities/data-tools/tqdm.md) |
| **SlimToolkit** | 当你想在不重写 Dockerfile 的情况下自动瘦身并加固臃肿的容器镜像时用它——注意它可能删掉运行时动态加载的文件。 | Apache-2.0 | B（4/6） | [中](categories/dev-utilities/ops-infra/slim.zh.md) · [EN](categories/dev-utilities/ops-infra/slim.md) |
| **Faker (faker-js)** | 当你需要在 JS/TS 里生成逼真的假/mock 数据（姓名、地址、金融…）用于测试和填充时用它。 | MIT | A（5/6） | [中](categories/dev-utilities/data-tools/faker-js.zh.md) · [EN](categories/dev-utilities/data-tools/faker-js.md) |
| **fontTools** | 当你需要对字体做程序化处理——子集化网页字体、转格式、查改表——时用它——但它只编辑字体文件，不绘制字形也不做文字排版。 | MIT | A（6/6） | [中](categories/dev-utilities/data-tools/fonttools.zh.md) · [EN](categories/dev-utilities/data-tools/fonttools.md) |
| **Flashlight** | 当你在维护一台 10.10–10.15 的老 macOS、想给 Spotlight 加插件时用它——但它自 2020 年起已弃，且需关闭 SIP，日常机器上别碰。 | MIT AND GPL-2.0-only (component split) | E（3/6） | [中](categories/dev-utilities/data-tools/flashlight.zh.md) · [EN](categories/dev-utilities/data-tools/flashlight.md) |
| **IdeaVim** | 当你离不开 JetBrains IDE、又想要 Vim 的动作、模式和 `.ideavimrc` 时用它——但它只是 Vim 子集的模拟，重度用户会撞上还原度的缺口。 | MIT | B（5/6） | [中](categories/dev-utilities/editors-and-runtimes/ideavim.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/ideavim.md) |
| **VS Code** | 快速、跨平台、具备智能补全、调试功能和最大扩展市场的代码编辑器——但它是 Electron 应用，且分发版包含微软遥测。 | MIT | B（5/6） | [中](categories/dev-utilities/editors-and-runtimes/vscode.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/vscode.md) |
| **Clash Verge Rev** | 现代化跨平台 GUI 代理客户端，支持基于规则的路由、内置 mihomo 内核和 TUN 模式——但仅限桌面端且为 GPL-3.0 许可。 | GPL-3.0 | B（5/6） | [中](categories/dev-utilities/ops-infra/clash-verge-rev.zh.md) · [EN](categories/dev-utilities/ops-infra/clash-verge-rev.md) |
| **RustDesk** | 开源跨平台自托管远程桌面，用于访问自己的机器——但需要自己管理中继服务器或接受 P2P 局限。 | AGPL-3.0 | B（5/6） | [中](categories/dev-utilities/ops-infra/rustdesk.zh.md) · [EN](categories/dev-utilities/ops-infra/rustdesk.md) |
| **Tauri** | 用 Rust 和操作系统原生 Webview 构建小巧、快速、安全的跨平台桌面与移动应用，替代 Electron。 | Apache-2.0 | A（6/6） | [中](categories/dev-utilities/editors-and-runtimes/tauri.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/tauri.md) |
| **Deno** | 具备安全默认设置、内置工具链和原生 TypeScript 支持的现代 JavaScript/TypeScript 运行时——无需 node_modules，但生态比 Node.js 小。 | MIT | A（6/6） | [中](categories/dev-utilities/editors-and-runtimes/deno.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/deno.md) |
| **Vaultwarden** | 非官方 Bitwarden 兼容服务器，用 Rust 编写，用于自托管密码管理——非官方、AGPL-3.0、单人核心维护者。 | AGPL-3.0 | B（6/6） | [中](categories/dev-utilities/ops-infra/vaultwarden.zh.md) · [EN](categories/dev-utilities/ops-infra/vaultwarden.md) |
| **Zed** | 由 Atom 创作者打造的高性能原生代码编辑器，支持实时多人协作——但扩展生态远小于 VS Code，仅约 4 年历史。 | NOASSERTION | A（4/6） | [中](categories/dev-utilities/editors-and-runtimes/zed.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/zed.md) |
| **BrewUI** | 当你在 macOS 26 上想要 Homebrew 官方 GUI，并且要把底层每条 `brew` 命令显示在可复制的控制台里时用它。 | AGPL-3.0 | C（4/6） | [中](categories/dev-utilities/package-manager-gui/brewui.zh.md) · [EN](categories/dev-utilities/package-manager-gui/brewui.md) |
| **Applite** | 当非技术用户需要在从未有过终端的机器上安装 Mac 应用时用它——它自带 Homebrew，且只管理 cask。 | MIT | B（5/6） | [中](categories/dev-utilities/package-manager-gui/applite.zh.md) · [EN](categories/dev-utilities/package-manager-gui/applite.md) |
| **CaskHub** | 当你在 macOS 15.6+ 上想要最丰富的应用商店式 cask 浏览体验时用它，但要接受内置的遥测。 | MIT | B（5/6） | [中](categories/dev-utilities/package-manager-gui/caskhub.zh.md) · [EN](categories/dev-utilities/package-manager-gui/caskhub.md) |
| **Cork** | 当你想要最完整的 Homebrew 操作面——services、tap、标签、菜单栏更新——并愿意为预编译版付 25€ 时用它。 | NOASSERTION (Commons Clause-based, source-available) | B（4/6） | [中](categories/dev-utilities/package-manager-gui/cork.zh.md) · [EN](categories/dev-utilities/package-manager-gui/cork.md) |
| **Cakebrew** | 只把它当作第一代 Homebrew GUI 的参考；它自 2021 年起实际已无人维护，也没有可安装的 cask。 | GPL-3.0 | E（3/6） | [中](categories/dev-utilities/package-manager-gui/cakebrew.zh.md) · [EN](categories/dev-utilities/package-manager-gui/cakebrew.md) |
| **ripgrep** | 快速、感知 gitignore 的面向行搜索工具，跨平台支持一流；10 年历史，Lindy 信号强劲，单人维护但可靠性高。 | Unlicense | B（6/6） | [中](categories/dev-utilities/data-tools/ripgrep.zh.md) · [EN](categories/dev-utilities/data-tools/ripgrep.md) |
| **Bun** | 一款极速一体化 JavaScript/TypeScript 工具集（运行时、打包器、测试运行器、包管理器）集成在单个二进制文件中——但商用前请核实自定义许可证。 | NOASSERTION | A（5/6） | [中](categories/dev-utilities/editors-and-runtimes/bun.zh.md) · [EN](categories/dev-utilities/editors-and-runtimes/bun.md) |
| **fzf** | :cherry_blossom: A command-line fuzzy finder | MIT | B（6/6） | [EN](categories/dev-utilities/data-tools/fzf.md) · [中](categories/dev-utilities/data-tools/fzf.zh.md) |
| **jq** | Command-line JSON processor | NOASSERTION | B（5/6） | [EN](categories/dev-utilities/data-tools/jq.md) · [中](categories/dev-utilities/data-tools/jq.zh.md) |

### frontend-animation

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Anime.js** | 零依赖的 JS 动画引擎：统一 animate() API 驱动 CSS、SVG、DOM 属性和 JS 对象，内置时间线、错峰、弹簧缓动和滚动联动。 | MIT | B（6/6） | [中](categories/frontend-animation/anime.zh.md) · [EN](categories/frontend-animation/anime.md) |

### api-gateway

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Kong Gateway** | 基于 OpenResty/Nginx 的 API 网关，插件层把一个反向代理变成可编程边界：既管 REST/微服务，也从 3.x 起管 LLM/MCP 流量。 | Apache-2.0 | A（5/6） | [中](categories/api-gateway/kong.zh.md) · [EN](categories/api-gateway/kong.md) |
| **Funtool** | 只有“Windows＋Claude Code＋NVIDIA”这条精确代理路径命中任务时才用它——当前可执行文件不透明，也无法从公开源码重建。 | MIT | C（5/6） | [中](categories/api-gateway/funtool.zh.md) · [EN](categories/api-gateway/funtool.md) |
| **HarnessRouter** | 把 Codex、Claude Code、Hermes 等 harness 统一跑在一个 OpenAI Responses 兼容 API 之后的自托管网关——但它仅约 6 周历史，UHP 标准由单一厂商维护。 | Apache-2.0 | B（5/6） | [中](categories/api-gateway/harnessrouter.zh.md) · [EN](categories/api-gateway/harnessrouter.md) |
| **LiteLLM** | 覆盖 100 多家供应商的可部署 LLM 网关与 SDK，带虚拟密钥、预算、花费追踪与故障转移——但需要 PostgreSQL/Redis 运维，且有 `enterprise/` 商业边界。 | MIT（核心）+ enterprise/ 商业目录 | A（4/6） | [中](categories/api-gateway/litellm.zh.md) · [EN](categories/api-gateway/litellm.md) |
| **Claude Code Router** | 本地控制面：从桌面/CLI 界面用条件规则与 fallback，让 Claude Code 等 coding agent 跨模型供应商路由。 | MIT | B（6/6） | [中](categories/api-gateway/claude-code-router.zh.md) · [EN](categories/api-gateway/claude-code-router.md) |
| **CLIProxyAPI** | 把消费级 CLI/OAuth 登录态包装成 OpenAI/Gemini/Claude 兼容 API 供其他工具调用——代价是固化的服务条款/账号风险与主机上的 token 存储。 | MIT | B（5/6） | [中](categories/api-gateway/cliproxyapi.zh.md) · [EN](categories/api-gateway/cliproxyapi.md) |

### geospatial

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **QGIS** | 功能完整、跨平台的桌面 GIS(Qt/C++)：浏览、编辑、分析、发布矢量/栅格/网格/点云空间数据，带 PyQGIS 插件和无界面 Server。 | GPL-2.0-or-later | A（5/6） | [中](categories/geospatial/qgis.zh.md) · [EN](categories/geospatial/qgis.md) |

### team-chat

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Mattermost** | 自托管的 Slack 式协作（聊天、通话、屏幕共享），以单个 Go 二进制跑在 PostgreSQL 上；企业 SSO/合规能力单独授权。 | AGPL-3.0（源码）/ MIT（二进制） | A（5/6） | [中](categories/team-chat/mattermost.zh.md) · [EN](categories/team-chat/mattermost.md) |
| **Zulip** | 自托管、按话题分线程的团队聊天（Apache-2.0），适合异步优先的团队——需一台专用 Ubuntu/Debian 主机，语音/视频交给集成。 | Apache-2.0 | A（5/6） | [中](categories/team-chat/zulip.zh.md) · [EN](categories/team-chat/zulip.md) |
| **Rocket.Chat** | 自托管通信平台（MIT 社区版），带应用市场、全渠道客服与原生联邦——但要运维 MongoDB + NATS + 微服务。 | MIT（社区版）+ EE | A（5/6） | [中](categories/team-chat/rocket-chat.zh.md) · [EN](categories/team-chat/rocket-chat.md) |
| **Buzz** | 自托管 Nostr 工作区，人和 AI agent 是同一条事件日志上的签名同等成员——agent 原生、pre-1.0、基础设施重。 | Apache-2.0 | B（3/6） | [中](categories/team-chat/buzz.zh.md) · [EN](categories/team-chat/buzz.md) |
| **HiveChat** | 可自托管、管理员统管的中小团队 AI 聊天：管理员配好多家大模型，团队据此聊天，按分组控制可见模型与 token 配额。 | Apache-2.0 | C（3/6） | [中](categories/team-chat/hivechat.zh.md) · [EN](categories/team-chat/hivechat.md) |

### captcha

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Cap** | 轻量、可自托管的 CAPTCHA 替代：无感工作量证明（Rust→WASM worker 做 SHA-256 nonce 搜索）发放服务端可校验 token——无图片、不调第三方。 | Apache-2.0 | B（5/6） | [中](categories/captcha/capjs.zh.md) · [EN](categories/captcha/capjs.md) |
| **Text_select_captcha** | 当要自动识别中文文字点选验证码（YOLO＋孪生网络，纯 CPU）时用它——仓库无 LICENSE 文件，默认保留所有权利，合法性是决定性门槛。 | NONE (no LICENSE file — all rights reserved) | D（5/6） | [中](categories/captcha/text-select-captcha.zh.md) · [EN](categories/captcha/text-select-captcha.md) |
| **pytorch-captcha-recognition** | 当需要定长图片验证码（多头 CNN）的可读教学基线时用它——这是 2020 年冻结的教程，要预期改造过时的 PyTorch API。 | Apache-2.0 | D（4/6） | [中](categories/captcha/pytorch-captcha-recognition.zh.md) · [EN](categories/captcha/pytorch-captcha-recognition.md) |
| **captcha (lepture)** | 当 Python 表单需要自托管、无第三方调用的图片／音频验证码渲染器时用它——它只渲染且抵不住现代 OCR，只能当 UX 减速带，而非安全控制。 | BSD-3-Clause | B（5/6） | [中](categories/captcha/lepture-captcha.zh.md) · [EN](categories/captcha/lepture-captcha.md) |
| **NopeCHA** | 只用于已授权、需无人值守覆盖多类验证码的自动化——持续维护的实现闭源，并依赖托管 API。 | MIT | B（6/6） | [中](categories/captcha/nopecha-extension.zh.md) · [EN](categories/captcha/nopecha-extension.md) |
| **Buster** | 用于真人触发的 reCAPTCHA 音频无障碍辅助或已授权测试——源码可审计、可走本地模型，但覆盖窄且结果不确定。 | GPL-3.0-only | B（5/6） | [中](categories/captcha/buster.zh.md) · [EN](categories/captcha/buster.md) |

### blockchain-dev-infrastructure

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **PoWFaucet** | 当公共 EVM 测试网需要带模块化防滥用控制的 faucet 时用它——热钱包托管、资金补充和高强度服务运维仍由你承担。 | AGPL-3.0 | B（5/6） | [中](categories/blockchain-dev-infrastructure/powfaucet.zh.md) · [EN](categories/blockchain-dev-infrastructure/powfaucet.md) |
### ml-research

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **autoresearch** | 自包含的单卡 LLM 训练脚手架，让 AI agent 通宵自主迭代 train.py——每次跑 5 分钟、按验证集 bits-per-byte 打分，只保留能降 loss 的改动。 | MIT | D（5/6） | [中](categories/ml-research/autoresearch.zh.md) · [EN](categories/ml-research/autoresearch.md) |
| **llm-circuit-finder** | Python 工具集：在 GGUF 模型里搜索连续的「推理电路」层块并在前向传播中复制（不训练、不改权重），再用内置探针验证效果。 | MIT | D（5/6） | [中](categories/ml-research/llm-circuit-finder.zh.md) · [EN](categories/ml-research/llm-circuit-finder.md) |
| **CLIP** | 当你需要零样本图像分类或图文互检 embedding 时用它——原始冻结参考实现；OpenCLIP 有更多权重。 | MIT | C（5/6） | [中](categories/ml-research/clip.zh.md) · [EN](categories/ml-research/clip.md) |
| **TaskMatrix** | 仅用于研究早期视觉工具路由 agent（Visual ChatGPT）——约 2024 年起已停更，别在其上构建。 | MIT | "?"（2/6） | [中](categories/ml-research/taskmatrix.zh.md) · [EN](categories/ml-research/taskmatrix.md) |
| **PyTorch-GAN** | 用来读干净的 GAN 参考实现学架构——2024 年起停更、已被扩散模型取代，不是生产代码。 | MIT | D（4/6） | [中](categories/ml-research/pytorch-gan.zh.md) · [EN](categories/ml-research/pytorch-gan.md) |
| **LSTM Neural Network for Time Series Prediction** | 当需要可读的配套示例学习 Keras LSTM 时序预测时用它——它锁定 EOL 的 TF1／Python 3.5 且为 AGPL-3.0，应照文章重写而非直接引入。 | AGPL-3.0 | E（4/6） | [中](categories/ml-research/lstm-time-series.zh.md) · [EN](categories/ml-research/lstm-time-series.md) |
| **Agriculture Knowledge Graph (AgriKG)** | 当需要中文领域知识图谱完整蓝图与现成数据集（NER、关系抽取、Neo4j、Django）时用它——作者声明已停止维护、技术栈陈旧且 GPL-3.0，应借鉴方法而非照搬代码。 | GPL-3.0 | D（3/6） | [中](categories/ml-research/agriculture-knowledge-graph.zh.md) · [EN](categories/ml-research/agriculture-knowledge-graph.md) |
| **Senta (SKEP)** | 当身处 PaddlePaddle／ERNIE 生态、需要带论文方法的 SKEP 情感分析 checkpoint 时用它——它锁定 EOL 的 PaddlePaddle 1.6.3，环境复原难以避免。 | Apache-2.0 | D（3/6） | [中](categories/ml-research/senta.zh.md) · [EN](categories/ml-research/senta.md) |
| **Depth Anything V2** | 当需要当下默认的单目深度基础模型从单张图估深度（PyTorch／Transformers）时用它——仅 Small 权重为 Apache-2.0，Base／Large／Giant 是 CC-BY-NC-4.0（非商用）。 | Apache-2.0 | B（4/6） | [中](categories/ml-research/depth-anything-v2.zh.md) · [EN](categories/ml-research/depth-anything-v2.md) |
| **pymoo** | 当需要 Python 演化式多目标优化（NSGA-II/III、MOEA/D）求 Pareto 前沿时用它——若问题是凸／线性／单目标，LP 或梯度求解器要快得多。 | Apache-2.0 | C（6/6） | [中](categories/ml-research/pymoo.zh.md) · [EN](categories/ml-research/pymoo.md) |
### agent-skills

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **book-to-skill** | 当你想把技术书籍 PDF（及其他文档格式）转成可安装的 agent 技能以用于 Claude Code、Copilot CLI 或 Amp 时用它。 | MIT | B（6/6） | [中](categories/agent-skills/book-to-skill.zh.md) · [EN](categories/agent-skills/book-to-skill.md) |
| **distilly** | 当你想把某个人的聊天记录、文档与访谈蒸馏成可安装的 agent 技能，让它用这个人的判断与语气回答时用它。 | MIT | B（4/6） | [中](categories/agent-skills/distilly.zh.md) · [EN](categories/agent-skills/distilly.md) |

#### agent-skills / engineering

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Agent Skills (addyosmani)** | 约 24 个生产级工程技能包（质量/安全/web 性能/API/发布），装进 coding agent 并通过约 8 个 SDLC 斜杠命令路由。 | MIT | B（4/6） | [中](categories/agent-skills/engineering/addyosmani-agent-skills.zh.md) · [EN](categories/agent-skills/engineering/addyosmani-agent-skills.md) |
| **web-quality-skills** | 含六个技能的 agent 技能包，把 Lighthouse / Core Web Vitals / WCAG / SEO 最佳实践编码成按需加载的指令集，让 coding agent 审计并修复 web 质量问题；属建议层，非测量工具。 | MIT | B（4/6） | [中](categories/agent-skills/engineering/addyosmani-web-quality.zh.md) · [EN](categories/agent-skills/engineering/addyosmani-web-quality.md) |
| **Scientific Agent Skills** | 一个大型 skill 包（约 147 个 skill），把 coding agent 变成生物、化学、医学、药物发现领域的科研助手——每个 skill 用一份带文档的 SKILL.md 封装一个科学 Python 库或数据库，按需加载。 | MIT | B（4/6） | [中](categories/agent-skills/engineering/scientific-agent-skills.zh.md) · [EN](categories/agent-skills/engineering/scientific-agent-skills.md) |
| **Vercel Agent Skills** | Vercel 官方 agent-skill 包——按需安装的 React/Next.js/Vercel 部署、Web 设计与文档审查指南，采用 agentskills.io/skills.sh 格式。 | MIT | B（4/6） | [中](categories/agent-skills/engineering/vercel-agent-skills.zh.md) · [EN](categories/agent-skills/engineering/vercel-agent-skills.md) |
| **Waza** | 一套精简的八个「工程习惯」skill 集合（规划、设计、评审、调试、写作、调研、读取、审计），coding agent 可按需加载，覆盖 Claude Code、Codex、Cursor。 | MIT | B（4/6） | [中](categories/agent-skills/engineering/waza.zh.md) · [EN](categories/agent-skills/engineering/waza.md) |

#### agent-skills / design

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Designer Skills** | 覆盖面很广的设计实践 skill pack——9 个 plugin 下共 97 个 skill、30 个 command（研究、设计系统、UX 策略、UI、交互、原型/测试、design ops、工具箱、视觉批评），适用于 Claude Code 和 Gemini CLI。 | MIT | B（4/6） | [中](categories/agent-skills/design/designer-skills.zh.md) · [EN](categories/agent-skills/design/designer-skills.md) |
| **Skills For Design Engineers** | Emil Kowalski 的六技能设计工程包，面向 UI motion、动画词汇、Apple 风格界面原则、严格动画评审和动画改进计划。 | MIT | B（4/6） | [中](categories/agent-skills/design/emilkowalski-skills.zh.md) · [EN](categories/agent-skills/design/emilkowalski-skills.md) |
| **make-interfaces-feel-better** | 一个单一、聚焦的 agent skill，把约 16 条具体的 UI 打磨原则（同心圆角、可中断过渡、等宽数字、入场/出场动画）注入 coding agent，让界面「感觉」做完了，而不只是功能正确。 | MIT | C（4/6） | [中](categories/agent-skills/design/make-interfaces-feel-better.zh.md) · [EN](categories/agent-skills/design/make-interfaces-feel-better.md) |
| **Stitch Skills** | 一套遵循 Agent Skills 开放标准的技能库，驱动 Google 的 Stitch MCP server 生成 UI 屏幕、在代码与设计间双向转换、抽取 DESIGN.md，并导出 React/React Native/shadcn 组件。 | Apache-2.0 | B（4/6） | [中](categories/agent-skills/design/stitch-skills.zh.md) · [EN](categories/agent-skills/design/stitch-skills.md) |
| **Taste-Skill** | 一套可移植、与框架无关的 agent skill 包，给 coding agent 注入审美，阻止千篇一律的 AI-slop 前端，转而产出有意图的布局、排版、动效与留白。 | MIT | B（4/6） | [中](categories/agent-skills/design/taste-skill.zh.md) · [EN](categories/agent-skills/design/taste-skill.md) |
| **UI UX Pro Max Skill** | 一个设计智能 skill pack，通过本地 CSV 检索引擎（风格/配色/字体/规则数据库）和交付前可访问性清单给 coding agent 注入 UI/UX 品味，可装入多种 agent harness。 | MIT | B（4/6） | [中](categories/agent-skills/design/ui-ux-pro-max.zh.md) · [EN](categories/agent-skills/design/ui-ux-pro-max.md) |
| **Hallmark** | 当 Claude Code、Cursor、Codex agent 需要有主张的反 AI 味设计 brief、审计、重设计或研究流程时用它。 | MIT | C（4/6） | [中](categories/agent-skills/design/hallmark.zh.md) · [EN](categories/agent-skills/design/hallmark.md) |
| **drawio-skill** | 一个 agent skill：把自然语言、代码、IaC 和接口 schema 变成可编辑的 `.drawio`，并能在源改动后重新同步而不丢手工版式。 | MIT | B（4/6） | [中](categories/agent-skills/design/drawio-skill.zh.md) · [EN](categories/agent-skills/design/drawio-skill.md) |

#### agent-skills / writing

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Baoyu Skills** | 宝玉出品的 20+ 个 coding agent 技能合集（翻译、markdown/HTML 排版、字幕与网页抓取、图片/图表/幻灯片生成），可装入 Claude Code、Codex 等支持 skill 的 harness。 | MIT | B（4/6） | [中](categories/agent-skills/writing/content-production/baoyu-skills.zh.md) · [EN](categories/agent-skills/writing/content-production/baoyu-skills.md) |
| **translate-book** | 面向 Codex、Claude Code 和 OpenClaw 的 agent skill：用并行 subagent 把整本书（PDF/DOCX/EPUB）翻译成任意语言。 | MIT | B（4/6） | [中](categories/agent-skills/writing/translation/translate-book.zh.md) · [EN](categories/agent-skills/writing/translation/translate-book.md) |
| **claude_translater** | shell 脚本＋Claude CLI 的文档翻译工具箱（PDF/DOCX/EPUB/PPTX）；translate-book 的灵感来源，但已不维护且无许可证。 | NOASSERTION | D（4/6） | [中](categories/agent-skills/writing/translation/claude-translater.zh.md) · [EN](categories/agent-skills/writing/translation/claude-translater.md) |
| **Humanizer-zh** | 一个简体中文 Claude Code 单技能，按约 24 条清单改写掉文本里的 AI 痕迹，是 blader/humanizer 的本地化版。 | MIT | C（4/6） | [中](categories/agent-skills/de-ai-writing/humanizer-zh.zh.md) · [EN](categories/agent-skills/de-ai-writing/humanizer-zh.md) |
| **Webnovel Writer** | 当 Claude Code 连载小说需要让章节、事实、检索、审查和摘要在长期写作中保持一致时用它。 | GPL-3.0 | B（5/6） | [中](categories/agent-skills/writing/fiction/webnovel-writer.zh.md) · [EN](categories/agent-skills/writing/fiction/webnovel-writer.md) |
| **chinese-novelist-skill** | 纯提示词、MIT 的中文小说流水线技能包（三层问答、大纲与人物档案、逐章创作、字数校验），无运行时、无检索层。 | MIT | B（4/6） | [中](categories/agent-skills/writing/fiction/chinese-novelist-skill.zh.md) · [EN](categories/agent-skills/writing/fiction/chinese-novelist-skill.md) |

#### agent-skills / security

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Anthropic Cybersecurity Skills** | 一个大型网络安全技能包（约 817 个技能），由对齐 MITRE ATT&CK、NIST CSF、ATLAS、D3FEND、NIST AI RMF、MITRE F3 的 SKILL.md runbook 组成，按需加载进 coding agent。 | Apache-2.0 | B（4/6） | [中](categories/agent-skills/security/anthropic-cybersecurity-skills.zh.md) · [EN](categories/agent-skills/security/anthropic-cybersecurity-skills.md) |
| **reverse-skill** | 当你的 AI 编码客户端需要一个通往 45 个逆向/渗透/CTF playbook 的路由器、带授权闸门与证据链报告时用它——双用途内容会触发杀软，且要求信任第三方写的 agent 可执行指令。 | MIT | B（4/6） | [中](categories/agent-skills/security/reverse-skill.zh.md) · [EN](categories/agent-skills/security/reverse-skill.md) |

#### agent-skills / context-engineering

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Agent Skills for Context Engineering** | 一个 15 个 skill 的 Claude Code 插件包，灌输上下文工程纪律：基础原理、退化、压缩、多 agent 协同、记忆、工具设计、评估与 harness 工程。 | MIT | B（4/6） | [中](categories/agent-skills/context-engineering/context-engineering-skills.zh.md) · [EN](categories/agent-skills/context-engineering/context-engineering-skills.md) |
| **NotebookLM Claude Code Skill** | 一个 Claude Code skill：用真实 Chrome 驱动查询你的 Google NotebookLM 笔记本，从你自己上传的文档取回有来源依据、带引用的答案，而非逐文件读取或凭空编造。 | MIT | C（4/6） | [中](categories/agent-skills/context-engineering/notebooklm-skill.zh.md) · [EN](categories/agent-skills/context-engineering/notebooklm-skill.md) |

#### agent-skills / prompt-engineering

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **prompt-master** | 一个 Claude skill：通过意图提取、模板路由和 37 条反模式清单，为 30+ AI 工具（LLM、编码 agent、图像/视频/语音 AI）生成一次性优化提示词。 | MIT | B（4/6） | [中](categories/agent-skills/prompt-engineering/prompt-master.zh.md) · [EN](categories/agent-skills/prompt-engineering/prompt-master.md) |
| **prompts.chat** | 可自托管的社区提示词平台：分享、发现、收集现成提示词（前身是 Awesome ChatGPT Prompts）。 | MIT（代码）+ CC0（提示词内容） | A（4/6） | [中](categories/agent-skills/prompt-engineering/prompts-chat.zh.md) · [EN](categories/agent-skills/prompt-engineering/prompts-chat.md) |
| **Prompt Engineering Guide** | 提示词/上下文工程、RAG 与 agent 技术的参考知识库（指南、论文、notebook）。 | MIT | C（4/6） | [中](categories/agent-skills/prompt-engineering/prompt-engineering-guide.zh.md) · [EN](categories/agent-skills/prompt-engineering/prompt-engineering-guide.md) |

#### agent-skills / vendor-collections

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Anthropic Skills** | Anthropic 官方公开的 Agent Skills 合集——自包含的 SKILL.md 目录（文档编辑、设计、MCP 与 skill 编写、沟通），可装进 Claude Code、Claude.ai 或 Claude API。 | Apache-2.0 | B（4/6） | [中](categories/agent-skills/vendor-collections/anthropic-skills.zh.md) · [EN](categories/agent-skills/vendor-collections/anthropic-skills.md) |
| **Agent Plugins for AWS** | AWS Labs 官方出品的九个 agent 插件集合（serverless、Amplify、SageMaker、迁移、数据库、部署/成本估算等），通过 marketplace 安装、触发短语驱动并接好 AWS MCP server，教 Claude Code / Cursor / Codex 在 AWS 上做架构、部署和运维。 | Apache-2.0 | A（4/6） | [中](categories/agent-skills/vendor-collections/aws-agent-plugins.zh.md) · [EN](categories/agent-skills/vendor-collections/aws-agent-plugins.md) |
| **Claude Plugins (Official)** | Anthropic 官方的 Claude Code 插件市场：精选的可安装插件目录（命令、agent、skill、MCP server），通过原生 /plugin 系统按名安装。 | Apache-2.0 | B（4/6） | [中](categories/agent-skills/vendor-collections/claude-plugins-official.zh.md) · [EN](categories/agent-skills/vendor-collections/claude-plugins-official.md) |
| **MiniMax Skills** | MiniMax 官方约 16 个 Agent Skill 成包（前端/移动端/shader 开发，外加 pdf/docx/xlsx/pptx、音乐与多模态生成），经插件市场装进 Claude Code 等编码 agent。 | MIT | B（4/6） | [中](categories/agent-skills/vendor-collections/minimax-skills.zh.md) · [EN](categories/agent-skills/vendor-collections/minimax-skills.md) |
| **Anthropic Knowledge Work Plugins** | 当你想要 Anthropic 官方面向知识工作（文档、沟通、研究）的开源插件集（用于 Claude）时用它——非常年轻。 | Apache-2.0 | B（4/6） | [中](categories/agent-skills/vendor-collections/knowledge-work-plugins.zh.md) · [EN](categories/agent-skills/vendor-collections/knowledge-work-plugins.md) |
| **Remotion Agent Skills** | Remotion 官方的 12 个 skill 捆绑包：教编码 agent（Claude Code、Codex、Cursor、Kimi Code）写出正确的 Remotion React 视频代码——经 `npx skills add remotion-dev/skills` 安装，版本与框架同步锁定。 | Not declared | C（4/6） | [中](categories/agent-skills/vendor-collections/remotion-skills.zh.md) · [EN](categories/agent-skills/vendor-collections/remotion-skills.md) |

#### agent-skills / subagent-collections

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Agency-Agents** | 约 232 个专业 subagent 人格的精选集合（markdown），覆盖 16 个职能部门，附 install/convert 脚本，可部署到 Claude Code 及另外约 11 个 agent harness。 | MIT | A（4/6） | [中](categories/agent-skills/subagent-collections/agency-agents.zh.md) · [EN](categories/agent-skills/subagent-collections/agency-agents.md) |
| **awesome-claude-code-subagents** | 一套精选的 100+ 个 Claude Code subagent 定义合集（每个角色一个 markdown persona），丢进 ~/.claude/agents/ 后 Claude Code 就能把活委派给对应领域专家。 | MIT | A（4/6） | [中](categories/agent-skills/subagent-collections/awesome-claude-code-subagents.zh.md) · [EN](categories/agent-skills/subagent-collections/awesome-claude-code-subagents.md) |
| **wshobson/agents** | 单人维护的大型多 harness 插件市场（约 194 个 subagent、158 个 skill、106 个 command、16 个 orchestrator），用一份 Markdown 源生成各 harness 原生产物，覆盖 Claude Code、Codex CLI、Cursor、OpenCode、Gemini CLI 与 Copilot。 | MIT | B（4/6） | [中](categories/agent-skills/subagent-collections/wshobson-agents.zh.md) · [EN](categories/agent-skills/subagent-collections/wshobson-agents.md) |
| **Council of High Intelligence** | 一个 Claude Code / Codex / Gemini CLI / OpenCode 技能包：把 18 个固定的「思想家」人设拉进一套剧本化多轮审议——盲评、匿名交叉质询、按置信度加权计票，最终由一位不参与辩论的 chairman 写出裁决。 | MIT | B（4/6） | [中](categories/agent-skills/subagent-collections/council-of-high-intelligence.zh.md) · [EN](categories/agent-skills/subagent-collections/council-of-high-intelligence.md) |

#### agent-skills / personal-collections

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **antfu/skills** | Anthony Fu 个人精选、面向 Vue/Vite/Nuxt 栈的 agent skill 集合（其 ESLint/pnpm/Vitest/UnoCSS 偏好 + 生成与 vendored 的框架 skill），通过 skills CLI 安装。 | MIT | B（4/6） | [中](categories/agent-skills/personal-collections/engineering-workflows/antfu-skills.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/antfu-skills.md) |
| **claude-code-harness** | 一套个人化的 Claude Code harness：以插件形式装入受治理的 plan → work → review → release 循环（spec 优先契约、TDD 门控执行、独立 review），并附带 Go 原生 doctor CLI 诊断插件缓存与 skill 漂移。 | MIT | B（4/6） | [中](categories/agent-skills/personal-collections/engineering-workflows/claude-code-harness.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/claude-code-harness.md) |
| **dbskill** | 一套个人精选的中文 agent 技能包（约 21 个 /dbs-* 命令），聚焦商业模式诊断、内容创作与个人决策，可安装进 Claude Code 等 harness。 | CC-BY-NC-4.0 | C（3/6） | [中](categories/agent-skills/personal-collections/knowledge-content/dbskill.zh.md) · [EN](categories/agent-skills/personal-collections/knowledge-content/dbskill.md) |
| **Dimillian Skills** | 某开发者个人精选的 16 个自包含 Codex skill，重心压在 Apple 平台（SwiftUI/iOS/macOS），外加几个通用评审/重构 swarm。 | MIT | C（4/6） | [中](categories/agent-skills/personal-collections/engineering-workflows/dimillian-skills.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/dimillian-skills.md) |
| **gstack** | Garry Tan 的私人 Claude Code harness：54 个 skill——约一半是角色人设（CEO 复盘、工程经理、设计师、QA、安全官、发布工程师），另一半是工具命令——外加一个 agent 真正驱动的浏览器，串成一条「规划 → 构建 → 评审 → 发布 → 复盘」冲刺流程。 | MIT | B（4/6） | [中](categories/agent-skills/personal-collections/engineering-workflows/gstack.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/gstack.md) |
| **andrej-karpathy-skills** | 一个行为准则包——单个 CLAUDE.md（加 Cursor 变体和一层薄技能包装），把 Karpathy 关于 LLM 编码陷阱的四条原则（先想后写、简单优先、外科式改动、目标驱动执行）注入 Claude Code / Cursor。 | MIT | C（4/6） | [中](categories/agent-skills/personal-collections/engineering-workflows/karpathy-skills.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/karpathy-skills.md) |
| **Khazix Skills** | 数字生命卡兹克（Khazix）的个人精选合集，含五个 SKILL.md 标准格式、以中文为主的 Agent Skill：磁盘清理、AI 资讯查询、文档/记忆同步、长文研究报告、公众号风格写作。 | MIT | B（4/6） | [中](categories/agent-skills/personal-collections/knowledge-content/khazix-skills.zh.md) · [EN](categories/agent-skills/personal-collections/knowledge-content/khazix-skills.md) |
| **ljg-skills** | 李继刚的个人 Claude Code 技能合集（20+ 个 skill），面向中文知识工作——读论文/拆书、概念分析、大白话改写、把内容渲染成 PNG 卡片，通过 skills CLI 安装。 | NOASSERTION | C（4/6） | [中](categories/agent-skills/personal-collections/knowledge-content/ljg-skills.zh.md) · [EN](categories/agent-skills/personal-collections/knowledge-content/ljg-skills.md) |
| **PUA** | 一个高能动性人设 skill 包：把 coding agent 设定成「被放进 30 天 PIP 的 P8 工程师」，用职场 PUA/PIP 话术逼它穷尽排查手段而非早早放弃。 | MIT | C（4/6） | [中](categories/agent-skills/personal-collections/engineering-workflows/pua.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/pua.md) |
| **Qiushi-Skill** | 一套方法论 skill 包，用「实事求是」加九个唯物辩证法思维工具（矛盾分析、调查研究、实践认识论等）武装编程 agent，并通过 npx 安装器跨 Claude Code/Cursor/Codex/OpenCode 落地。 | MIT | B（4/6） | [中](categories/agent-skills/personal-collections/engineering-workflows/qiushi-skill.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/qiushi-skill.md) |
| **shaping-skills** | Ryan Singer 的个人 Claude Code 技能包，把 Shape Up 的「shaping」流程（框定问题、breadboarding、产出 framing/kickoff 文档）带进 coding agent，让 AI 在写代码前先帮你想清楚「要做什么」。 | NOASSERTION | D（4/6） | [中](categories/agent-skills/personal-collections/engineering-workflows/shaping-skills.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/shaping-skills.md) |
| **TÂCHES CC Resources** | TÂCHES（glittercowboy）的个人化 Claude Code 扩展合集：约 27 个 slash 命令、9 个 skill（多为生成新命令/skill/subagent/hook/MCP server 的元生成器）、3 个审计 subagent 及 hook，作为单个 marketplace 插件安装。 | MIT | C（4/6） | [中](categories/agent-skills/personal-collections/engineering-workflows/taches-cc-resources.zh.md) · [EN](categories/agent-skills/personal-collections/engineering-workflows/taches-cc-resources.md) |
| **skills** | Sahil Lavingia 的 Claude Code skill 包，把《The Minimalist Entrepreneur》旅程变成 10 个商业构建命令。 | NOASSERTION | C（4/6） | [中](categories/agent-skills/personal-collections/knowledge-content/slavingia-skills.zh.md) · [EN](categories/agent-skills/personal-collections/knowledge-content/slavingia-skills.md) |
| **canghe-skills** | 苍何个人 Claude Code skills marketplace：覆盖内容发布、图像/视频生成后端、商业情报、提取工具、Obsidian helper、Remotion 指南和文档解析。 | NOASSERTION | D（4/6） | [中](categories/agent-skills/personal-collections/knowledge-content/canghe-skills.zh.md) · [EN](categories/agent-skills/personal-collections/knowledge-content/canghe-skills.md) |
| **patent-disclosure-skill** | 中文优先的八技能 Agent 包：挖掘专利点并撰写发明／实用新型／外观交底书，改写成申请文件，检索国知局记录，把专利解读进 Obsidian 库，并出审查政策简报。 | MIT | B（4/6） | [中](categories/agent-skills/personal-collections/knowledge-content/patent-disclosure-skill.zh.md) · [EN](categories/agent-skills/personal-collections/knowledge-content/patent-disclosure-skill.md) |
| **huashu-skills** | 花叔的内容创作 Skills 合集 - AI审校、选题生成、视频大纲、素材搜索等 11 个实用技能 | NOASSERTION | D（4/6） | [中](categories/agent-skills/writing/content-production/huashu-skills.zh.md) · [EN](categories/agent-skills/writing/content-production/huashu-skills.md) |
| **De-AI-Prompt-Enhancer-Writer-Booster-SKILL** | 中文去 AI 味提示词套件，打包为两个 SKILL 格式文件夹：`de-AI-writing/SKILL.md` 用于清理 AI 腔，`good-writing/SKILL.md` 用于更强的作者风格复现。 | NOASSERTION | C（4/6） | [中](categories/agent-skills/de-ai-writing/de-ai-prompt-enhancer-writer-booster-skill.zh.md) · [EN](categories/agent-skills/de-ai-writing/de-ai-prompt-enhancer-writer-booster-skill.md) |
| **chatgpt-comparison-detection** | Human ChatGPT Comparison Corpus (HC3), Detectors, and more! 🔥 | NOASSERTION | E（4/6） | [中](categories/llm-eval/chatgpt-comparison-detection.zh.md) · [EN](categories/llm-eval/chatgpt-comparison-detection.md) |
| **writing-agent** | 🚀 一个基于 Claude Code (Skills + Subagents) 的“去AI味”全栈写作系统。不仅防套路，更通过专属规则强制注入人类观点与细节，搭配读者测试评估与自动图文排版。全面支持 DeepSeek / 智谱GLM / MiniMax 等国产低成本大模型，提供从选题、风格建模到审稿发布的高维全自动写作工作流。 | MIT | B（4/6） | [中](categories/agent-skills/writing/content-production/writing-agent.zh.md) · [EN](categories/agent-skills/writing/content-production/writing-agent.md) |
| **nuwa-skill** | 你想蒸馏的下一个员工，何必是同事。蒸馏任何人的思维方式——心智模型、决策启发式、表达DNA。Distill how anyone thinks. | MIT | B（4/6） | [中](categories/agent-skills/context-engineering/nuwa-skill.zh.md) · [EN](categories/agent-skills/context-engineering/nuwa-skill.md) |
| **shuorenhua** | 说人话｜中文优先的去 AI 味改写 skill：保事实、分场景、改完可直接发。Chinese-first rewrite skill for Codex / Claude Code / Cursor / ChatGPT — removes AI tone, preserves facts. | MIT | B（4/6） | [中](categories/agent-skills/de-ai-writing/shuorenhua.zh.md) · [EN](categories/agent-skills/de-ai-writing/shuorenhua.md) |
| **ai-flavor-remover** | 一个用于去除“AI 味”的中文单文件 prompt 片段；上游 README 明确说只在 Gemini 2.5 Pro 上测试过。 | NOASSERTION | D（4/6） | [中](categories/agent-skills/de-ai-writing/ai-flavor-remover.zh.md) · [EN](categories/agent-skills/de-ai-writing/ai-flavor-remover.md) |
| **stop-slop** | 用于移除英文 prose 中 AI 痕迹的 skill 文件。 | MIT | B（4/6） | [中](categories/agent-skills/de-ai-writing/stop-slop.zh.md) · [EN](categories/agent-skills/de-ai-writing/stop-slop.md) |
| **humanizer** | 移除英文文本中 AI 写作痕迹的 Claude Code skill。 | MIT | B（4/6） | [中](categories/agent-skills/de-ai-writing/humanizer.zh.md) · [EN](categories/agent-skills/de-ai-writing/humanizer.md) |
| **avoid-ai-writing** | 可移植的去 AI 味写作 skill：自带确定性 npm 检测器、按命中数卡的 CI / pre-commit 门禁，以及一份公开自身误报率的人控语料测量。 | MIT | B（5/6） | [中](categories/agent-skills/de-ai-writing/avoid-ai-writing.zh.md) · [EN](categories/agent-skills/de-ai-writing/avoid-ai-writing.md) |
| **cangjie-skill** | 把书、长视频、播客、课程、访谈和转写稿蒸馏成可复用、可测试 agent skill pack 的方法论 skill。 | MIT | B（4/6） | [中](categories/agent-skills/context-engineering/cangjie-skill.zh.md) · [EN](categories/agent-skills/context-engineering/cangjie-skill.md) |
| **archify** | Any agent Skill: generate beautiful architecture diagrams with dark/light theme toggle and PNG/JPEG/WebP/SVG export | MIT | B（4/6） | [中](categories/agent-skills/design/archify.zh.md) · [EN](categories/agent-skills/design/archify.md) |
| **mattpocock/skills** | Matt Pocock 的工程 skill 包，面向 Claude Code 和 skills.sh，覆盖 grilling、domain docs、TDD、bug 诊断、架构、review、tickets 和实现流程。 | MIT | B（4/6） | [中](categories/agent-skills/engineering/mattpocock-skills.zh.md) · [EN](categories/agent-skills/engineering/mattpocock-skills.md) |
| **BrowserAct Skills** | 面向 BrowserAct 的 agent 浏览器自动化技能包：索引式浏览器控制、stealth/private session、远程人工接管，以及 Skill Forge 抓取工作流。 | MIT | B（4/6） | [中](categories/agent-skills/engineering/browser-act-skills.zh.md) · [EN](categories/agent-skills/engineering/browser-act-skills.md) |
| **caveman** | 一个 prompt 与安装器技能包，让多种 coding agent 用刻意简短的“caveman”风格回答，同时保留代码、命令和错误信息。 | MIT | C（4/6） | [中](categories/agent-skills/engineering/caveman.zh.md) · [EN](categories/agent-skills/engineering/caveman.md) |
| **open-seo** | Open source alternative to Semrush and Ahrefs | MIT | B（5/6） | [中](categories/agent-skills/writing/marketing-seo/open-seo.zh.md) · [EN](categories/agent-skills/writing/marketing-seo/open-seo.md) |
| **ai-website-cloner-template** | Clone any website with one command using AI coding agents | MIT | B（4/6） | [中](categories/agent-skills/design/ai-website-cloner-template.zh.md) · [EN](categories/agent-skills/design/ai-website-cloner-template.md) |
| **huashu-design** | Huashu Design · HTML-native design skill for Claude Code · Claude Code 里 HTML 原生的设计 skill · 高保真原型 / 幻灯片 / 动画 + 20 设计哲学 + 5 维评审 + MP4 导出 · Agent-agnostic | MIT | B（4/6） | [中](categories/agent-skills/design/huashu-design.zh.md) · [EN](categories/agent-skills/design/huashu-design.md) |
| **ppt-master** | AI generates a real, editable PowerPoint from any document — native shapes & animations, editable charts & tables you can change the data on, speaker notes voiced as audio narration, and the option to follow your own .pptx template, not slide images · by Hugo He | MIT | B（3/6） | [中](categories/agent-skills/slides-ppt/ppt-master.zh.md) · [EN](categories/agent-skills/slides-ppt/ppt-master.md) |
| **frontend-slides** | 用 coding agent 的前端能力创建网页演示文稿。 | MIT | B（4/6） | [中](categories/agent-skills/slides-ppt/frontend-slides.zh.md) · [EN](categories/agent-skills/slides-ppt/frontend-slides.md) |
| **html-ppt-skill** | HTML PPT Studio——AgentSkill，内置 36 个主题、15 个 full-deck templates、31 个布局、47 个动画和 presenter mode，用于构建专业静态 HTML 演示文稿。 | MIT | B（4/6） | [中](categories/agent-skills/slides-ppt/html-ppt-skill.zh.md) · [EN](categories/agent-skills/slides-ppt/html-ppt-skill.md) |
| **tacit-mining** | Let AI truly understand you. A Claude Code skill that extracts tacit knowledge through structured dialogue. 隐性知识挖掘技能。 | NOASSERTION | D（4/6） | [中](categories/agent-skills/context-engineering/tacit-mining.zh.md) · [EN](categories/agent-skills/context-engineering/tacit-mining.md) |
| **soul.md** | The best way to build a personality for your agent. Let Claude Code / OpenClaw ingest your data & build your AI soul. | MIT | B（4/6） | [中](categories/agent-skills/context-engineering/soul-md.zh.md) · [EN](categories/agent-skills/context-engineering/soul-md.md) |
| **marketingskills** | Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering. | MIT | B（4/6） | [中](categories/agent-skills/writing/marketing-seo/marketingskills.zh.md) · [EN](categories/agent-skills/writing/marketing-seo/marketingskills.md) |

### observability

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Grafana** | 当你需要在 Prometheus/Loki/Elasticsearch 等多数据源之上加一层统一看板和告警时用它——它做可视化，不做存储。 | AGPL-3.0 | B（5/6） | [中](categories/observability/grafana.zh.md) · [EN](categories/observability/grafana.md) |
| **Prometheus** | The Prometheus monitoring system and time series database. | Apache-2.0 | A（6/6） | [EN](categories/observability/prometheus.md) · [中](categories/observability/prometheus.zh.md) |
| **OpenTelemetry Collector** | OpenTelemetry Collector | Apache-2.0 | A（5/6） | [EN](categories/observability/opentelemetry-collector.md) · [中](categories/observability/opentelemetry-collector.zh.md) |
| **Loki** | Like Prometheus, but for logs. | AGPL-3.0 | B（6/6） | [EN](categories/observability/loki.md) · [中](categories/observability/loki.zh.md) |
| **Jaeger** | CNCF Jaeger, a Distributed Tracing Platform | Apache-2.0 | A（5/6） | [EN](categories/observability/jaeger.md) · [中](categories/observability/jaeger.zh.md) |

### data-visualization

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Apache Superset** | 当你想要在数据仓库之上自托管 SQL BI 看板与探索时用它——不是基础设施指标/可观测性。 | Apache-2.0 | A（6/6） | [中](categories/data-visualization/superset.zh.md) · [EN](categories/data-visualization/superset.md) |
| **Evidence** | Business intelligence as code: build fast, interactive data visualizations in SQL and markdown | MIT | B（5/6） | [EN](categories/data-visualization/evidence.md) · [中](categories/data-visualization/evidence.zh.md) |
| **Metabase** | The easy-to-use open source Business Intelligence and Embedded Analytics tool that lets everyone work with data :bar_chart: | NOASSERTION | A（4/6） | [EN](categories/data-visualization/metabase.md) · [中](categories/data-visualization/metabase.zh.md) |

### ocr

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Tesseract** | 当你需要离线、可嵌入、覆盖 100+ 语言、面向清晰印刷文本的 OCR 时用它——不适合野外照片或手写。 | Apache-2.0 | A（5/6） | [中](categories/ocr/tesseract.zh.md) · [EN](categories/ocr/tesseract.md) |
| **LaTeX-OCR (pix2tex)** | 当你要把数学公式图片转成 LaTeX（pix2tex）时用它——只管公式、已放缓，VLM 可能更强。 | MIT | C（3/6） | [中](categories/ocr/latex-ocr.zh.md) · [EN](categories/ocr/latex-ocr.md) |
| **Laravel OCR** | 当 Laravel 应用需要统一接入本地与云 OCR，并用模板抽取字段时用它——PDF／版面处理较浅，仓库也缺少许可证文件。 | NOASSERTION | D（5/6） | [中](categories/ocr/laravel-ocr.zh.md) · [EN](categories/ocr/laravel-ocr.md) |

### document-parsing

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Docling** | 当你需要把杂乱的 PDF/DOCX/PPTX 解析成干净的结构化 Markdown/JSON 以喂给 RAG 时用它——是解析器，不是文档管理系统。 | MIT | A（6/6） | [中](categories/document-parsing/docling.zh.md) · [EN](categories/document-parsing/docling.md) |
| **MarkItDown** | 当你需要一个轻量级 Python 库把各类办公文档和文件转成 Markdown 以喂给 LLM 时用它——比 Docling 更简单，但对版面感知较弱。 | MIT | A（6/6） | [中](categories/document-parsing/markitdown.zh.md) · [EN](categories/document-parsing/markitdown.md) |
| **olmOCR** | 当你需要把带公式、表格、手写体和多栏版面的复杂 PDF 转成干净 Markdown 以用于 LLM 训练数据集时用它——需要 GPU。 | Apache-2.0 | C（5/6） | [中](categories/document-parsing/olmocr.zh.md) · [EN](categories/document-parsing/olmocr.md) |
| **Marker** | Convert PDF to markdown + JSON quickly with high accuracy | GPL-3.0 | B（4/6） | [EN](categories/document-parsing/marker.md) · [中](categories/document-parsing/marker.zh.md) |
| **unstructured** | Convert documents to structured data effortlessly. Unstructured is open-source ETL solution for transforming complex documents into clean, structured formats for language models.  Visit our website to learn more about our enterprise grade Platform product for production grade workflows, partitioning, enrichments, chunking and embedding. | Apache-2.0 | A（6/6） | [EN](categories/document-parsing/unstructured.md) · [中](categories/document-parsing/unstructured.zh.md) |
| **any2html** | Use it when you need any2html in the document-parsing area. | NOASSERTION | D（5/6） | [中](categories/document-parsing/any2html.zh.md) · [EN](categories/document-parsing/any2html.md) |
| **Dedoc** | 当混合 PDF 与 Office 归档必须转成带表格和附件的逻辑树时用它——本地解析面广，但 Linux 与系统包依赖很重。 | Apache-2.0 | A（5/6） | [中](categories/document-parsing/dedoc.zh.md) · [EN](categories/document-parsing/dedoc.md) |
| **Bella Domify** | 当 Python RAG 管线需要细粒度 PDF／Office DOM tree 和可选视觉 OCR 时用它——许可证冲突与 provider／基础设施耦合会抬高采用成本。 | GPL-2.0-only | D（5/6） | [中](categories/document-parsing/bella-domify.zh.md) · [EN](categories/document-parsing/bella-domify.md) |
| **MinerU Skill** | 当 agent 需要一条命令完成云端文档转 Markdown、批处理、续跑和投递时用它——文件会离开本地，质量取决于 MinerU。 | MIT | C（5/6） | [中](categories/document-parsing/mineru-skill.zh.md) · [EN](categories/document-parsing/mineru-skill.md) |

### office-automation

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **OfficeCLI** | 当 agent 必须在一台没有 Python 也没有 Office 的机器上读写、创建全部三个 Office 格式，并且需要**看见**渲染结果时用它——但它只有 6 个月、98% 单人作者、没有公开测试套件，且默认开启自动更新并会改写你的 agent skill 目录。 | Apache-2.0 | B（6/6） | [中](categories/office-automation/officecli.zh.md) · [EN](categories/office-automation/officecli.md) |
| **python-docx** | 当 Python 服务需要就地创建或编辑 Word `.docx`、且要一个能锁版本、已存活 13 年的 MIT 依赖时用它——但没有渲染能力，且脚注／尾注自 2014 年起一直未实现。 | MIT | B（5/6） | [中](categories/office-automation/python-docx.zh.md) · [EN](categories/office-automation/python-docx.md) |
| **python-pptx** | 当你必须用 Python 生成或编辑原生 `.pptx`、且交付物要能在 PowerPoint 里打开时用它——但它自 2024-08-07 起未再发版，动画（2017）和 SmartArt（2014）从未实现。 | MIT | C（4/6） | [中](categories/office-automation/python-pptx.zh.md) · [EN](categories/office-automation/python-pptx.md) |
| **XlsxWriter** | 当 Python 服务从数据生成新的 `.xlsx`、且你要零依赖加 13 年稳定性时用它——但它只写，无法打开已有工作簿，也不计算公式。 | BSD-2-Clause | B（6/6） | [中](categories/office-automation/xlsxwriter.zh.md) · [EN](categories/office-automation/xlsxwriter.md) |
| **Office-Word-MCP-Server** | 只有当既有 LLM 集成已经绑定它那约 55 个 Word tool schema 时才用它——仓库已于 2025-12-31 归档，作者批量归档了约 15 个 MCP server；新工作请用 OfficeCLI，或自己封装 python-docx。 | MIT | C（6/6） | [中](categories/office-automation/office-word-mcp-server.zh.md) · [EN](categories/office-automation/office-word-mcp-server.md) |

### diagramming

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Mermaid** | 当你想把图表写成可进版本库的纯文本（流程图/时序图/ER），在 Markdown 和文档里渲染时用它——不适合像素级精确排版。 | MIT | A（6/6） | [中](categories/diagramming/mermaid.zh.md) · [EN](categories/diagramming/mermaid.md) |
| **flowchart.js** | 当你想把简单流程图写成可 git diff 的文本、在浏览器里渲成 SVG 时用它——它只渲染不编辑，依赖老旧的 Raphael.js，复杂图会力不从心。 | MIT | B（5/6） | [中](categories/diagramming/flowchart-js.zh.md) · [EN](categories/diagramming/flowchart-js.md) |
| **bpmn-js** | 当业务分析师需要在你的 Web 应用里编辑或查看合规的 BPMN 2.0 流程图时用它——但其许可证强制保留不可移除的 bpmn.io 水印，白标前务必先确认条款。 | MIT + bpmn.io watermark clause | A（5/6） | [中](categories/diagramming/bpmn-js.zh.md) · [EN](categories/diagramming/bpmn-js.md) |
| **Excalidraw** | 手绘风格的虚拟白板，支持协作和端到端加密——但存为 JSON 而非纯文本，不能在 Git 里 diff。 | MIT | A（6/6） | [中](categories/diagramming/excalidraw.zh.md) · [EN](categories/diagramming/excalidraw.md) |
| **draw.io** | 完整的所见即所得绘图应用，`.drawio` 文件是纯文本 mxGraph XML：官方云／UML／BPMN 形状库、可离线运行的桌面版，文件还能进 Git diff。 | Apache-2.0（图标／stencil 另有附加限制） | B（6/6） | [中](categories/diagramming/drawio.zh.md) · [EN](categories/diagramming/drawio.md) |
### media-download

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **youtube-dl** | 当你需要一个久经考验的 CLI/库从 YouTube 和 1000+ 站点下载音视频时用它——但热门站点优先用更活跃的 yt-dlp 分叉。 | Unlicense | B（6/6） | [中](categories/media-download/youtube-dl.zh.md) · [EN](categories/media-download/youtube-dl.md) |
| **you-get** | 当你想要一个极简 Python CLI 从 YouTube 和大量中文站点（B 站/优酷）抓取音视频时用它——比 yt-dlp 更轻。 | MIT | D（3/6） | [中](categories/media-download/you-get.zh.md) · [EN](categories/media-download/you-get.md) |
| **cobalt** | 当你想要一个干净、可自托管、带 Web UI 和 API、无广告无追踪的媒体下载器时用它——不是可脚本化的 CLI。 | AGPL-3.0 | B（5/6） | [中](categories/media-download/cobalt.zh.md) · [EN](categories/media-download/cobalt.md) |
| **lux** | 当你想要一个快速的单二进制 Go 下载器、对中文视频站点支持好时用它——站点覆盖与更新都不如 yt-dlp。 | MIT | B（5/6） | [中](categories/media-download/lux.zh.md) · [EN](categories/media-download/lux.md) |
| **youtube-transcript-api** | 当你想免密钥地为 RAG／摘要管线取回带时间戳的 YouTube 字幕时用它——但它依赖未公开接口、随时可能失效，且云端／机房 IP 现已必须配付费住宅代理。 | MIT | A（6/6） | [中](categories/media-download/youtube-transcript-api.zh.md) · [EN](categories/media-download/youtube-transcript-api.md) |
| **bulk-downloader-for-reddit** | 当你想通过 OAuth 做可脚本化、可复现的 Reddit 文件加元数据归档时用它——但 Reddit 约 1000 帖的列表上限无法绕过，且发布自 2023 年初已停滞（GPL-3.0）。 | GPL-3.0 | D（4/6） | [中](categories/media-download/bulk-downloader-for-reddit.zh.md) · [EN](categories/media-download/bulk-downloader-for-reddit.md) |
| **yt-dlp** | 当你需要一个活跃维护的 CLI 从 YouTube 和数千站点下载音视频时用它——youtube-dl 的事实继任者，修复更快、功能更多。 | Unlicense | A（6/6） | [中](categories/media-download/yt-dlp.zh.md) · [EN](categories/media-download/yt-dlp.md) |
| **gallery-dl** | Command-line program to download image galleries and collections from several image hosting sites | GPL-2.0 | B（6/6） | [EN](categories/media-download/gallery-dl.md) · [中](categories/media-download/gallery-dl.zh.md) |

### media-processing

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **FFmpeg** | 当你需要在管线里解码/编码/转码/滤镜处理几乎任何音视频时用它——注意 LGPL→GPL 的构建授权陷阱。 | LGPL-2.1-or-later | A（3/6） | [中](categories/media-processing/video-audio/ffmpeg.zh.md) · [EN](categories/media-processing/video-audio/ffmpeg.md) |
| **HandBrake** | 当你需要预设驱动的 GUI 或 CLI 将视频转码/翻录为现代 MP4/MKV 配合 H.264/H.265 时用它——但它是终端用户应用，不是库，且远比原生 FFmpeg 窄。 | GPL-2.0-or-later | A（4/6） | [中](categories/media-processing/video-audio/handbrake.zh.md) · [EN](categories/media-processing/video-audio/handbrake.md) |
| **ffmpeg-python** | 当你想用 Python 编排复杂的 FFmpeg 滤镜图、把不可读的 -filter_complex 字符串换成可读的 DAG 代码时用它——但它自 2024 年起停更、仅单人维护，且仍依赖系统已装 ffmpeg 二进制。 | Apache-2.0 | C（4/6） | [中](categories/media-processing/video-audio/ffmpeg-python.zh.md) · [EN](categories/media-processing/video-audio/ffmpeg-python.md) |
| **PyAV** | 当你需要在 Python 中以进程内方式把视频/音频帧作为 NumPy 数组进行程序化访问时用它——但它比 CLI 包装器更底层、安装更重（需要针对 FFmpeg 头文件编译 Cython 扩展）。 | MIT | A（6/6） | [中](categories/media-processing/video-audio/pyav.zh.md) · [EN](categories/media-processing/video-audio/pyav.md) |
| **VMAF** | 当你在调编码档位、需要用业界通用的 0—100 感知分对比编解码器与预设时用它——但它只支持全参考，且选错模型会悄悄让跨版本对比失效。 | BSD-2-Clause-Patent | B（5/6） | [中](categories/media-processing/quality-metrics/vmaf.zh.md) · [EN](categories/media-processing/quality-metrics/vmaf.md) |
| **SSIMULACRA2** | 当你需要对比图像编解码器（JPEG XL、AVIF、WebP）并需要一个与人类主观评分相关的感知质量分时用它——但它仅限图像，非对称，且采用度不及 VMAF。 | MIT | C（3/6） | [中](categories/media-processing/quality-metrics/ssimulacra2.zh.md) · [EN](categories/media-processing/quality-metrics/ssimulacra2.md) |
| **m3u8** | 当你需要把 HLS 的 .m3u8 清单当作带类型的对象模型来解析或改写、而非正则硬抠时用它——但它仅限 Python 与 HLS，且自 2025 年起沉寂，最新的 rfc8216bis 标签可能滞后。 | MIT | C（3/6） | [中](categories/media-processing/video-audio/m3u8.zh.md) · [EN](categories/media-processing/video-audio/m3u8.md) |
| **ffsubsync** | 当字幕整体存在恒定偏移、你想用一条命令做 FFT 音频对齐而不手动设同步点时用它——但它修不了内容内部的逐行／变动漂移，且仅单人维护。 | MIT | B（5/6） | [中](categories/media-processing/video-audio/ffsubsync.zh.md) · [EN](categories/media-processing/video-audio/ffsubsync.md) |
| **MoviePy** | 当你想用友好的 Python API 做程序化视频编辑——剪辑、合成、文字、特效——时用它——但它是纯离线批处理，对大文件比原生 FFmpeg 慢，且维护速度已从巅峰期下降。 | MIT | B（5/6） | [中](categories/media-processing/video-audio/moviepy.zh.md) · [EN](categories/media-processing/video-audio/moviepy.md) |
| **GStreamer** | 当你需要实时、持久、嵌入应用的音视频管线框架而非 CLI 工具时用它——但要接受陡峭的学习曲线和插件依赖管理。 | LGPL-2.1-or-later | A（4/6） | [中](categories/media-processing/video-audio/gstreamer.zh.md) · [EN](categories/media-processing/video-audio/gstreamer.md) |
| **MLT** | 当你需要构建自定义视频编辑器或需要时间线模型的自动化剪辑管线时用它——但它是框架，不是开箱即用的 NLE，且底层编解码工作委托给 FFmpeg。 | LGPL-2.1-or-later | B（5/6） | [中](categories/media-processing/video-audio/mlt.zh.md) · [EN](categories/media-processing/video-audio/mlt.md) |
| **OpenAI Whisper** | 当你需要通用的多语言语音转文字转写或从音视频英译时用它——但它默认不是实时系统，大模型在 CPU 上很慢，且对非语音内容会幻觉。 | MIT | B（5/6） | [中](categories/media-processing/video-audio/whisper.zh.md) · [EN](categories/media-processing/video-audio/whisper.md) |
| **sharp** | High performance Node.js image processing, the fastest module to resize JPEG, PNG, WebP, AVIF and TIFF images. Uses the libvips library. | Apache-2.0 | A（6/6） | [EN](categories/media-processing/image-processing/sharp.md) · [中](categories/media-processing/image-processing/sharp.zh.md) |
| **ImageMagick** | ImageMagick is a free, open-source software suite for creating, editing, converting, and displaying images. It supports 200+ formats and offers powerful command-line tools and APIs for automation, scripting, and integration across platforms. | NOASSERTION | B（5/6） | [EN](categories/media-processing/image-processing/imagemagick.md) · [中](categories/media-processing/image-processing/imagemagick.zh.md) |
| **Screenshot Service** | 仅适合作为隔离的内部 HTML 转图片 worker——API 鉴权已禁用，Chromium 还关闭了 sandbox 与 Web 安全。 | NOASSERTION | D（4/6） | [中](categories/media-processing/image-processing/screenshot-service.zh.md) · [EN](categories/media-processing/image-processing/screenshot-service.md) |
| **Concat** | 当你需要一款当下就能安装运行、原生、离线、可脚本化的类 CapCut 视频编辑器时用它——但它是仅有约 25 天历史的 0.2.x beta、只有一位维护者，且专业能力（遮罩、跟踪、关键帧曲线）仍在路线图上。 | AGPL-3.0-or-later | C（5/6） | [中](categories/media-processing/video-editing/concat.zh.md) · [EN](categories/media-processing/video-editing/concat.md) |
| **OpenCut** | 仅当你打算跟进或基于浏览器／WASM 重写架构开发时用它——其仓库正在重写、不接受外部贡献、不产出可用版本，能用的 classic 版本在已归档仓库里。 | MIT | B（5/6） | [中](categories/media-processing/video-editing/opencut.zh.md) · [EN](categories/media-processing/video-editing/opencut.md) |
| **Jianying Headless** | 当 macOS 上的剪映工作流需要 agent 生成**可编辑**草稿——真实多轨工程，并可用应用自己的引擎原生导出 MP4——时用它；代价是仅 5 天历史、单一维护者、绑定某一个应用版本、且仅限非商用。 | Personal Learning and Non-Commercial Use License（NOASSERTION，非 OSI） | D（4/6） | [中](categories/media-processing/nle-automation/jianying-headless.zh.md) · [EN](categories/media-processing/nle-automation/jianying-headless.md) |
| **pyJianYingDraft** | 当 Python 管线需要跨平台产出可编辑剪映草稿、且接受 Apache-2.0 时用它——代价是新版剪映草稿已加密、它自己不做渲染、自带批量导出只支持 Windows 加剪映 6 及更早版本。 | Apache-2.0 | C（5/6） | [中](categories/media-processing/nle-automation/pyjianyingdraft.zh.md) · [EN](categories/media-processing/nle-automation/pyjianyingdraft.md) |
| **JianYing Editor Skill** | 当 coding agent 应该把一句自然语言需求变成真实剪映时间轴——素材、TTS 配音、对齐字幕、配乐与具名特效——而由你在剪映里判断并导出时用它；代价是没有 tagged release、无人值守导出只在 Windows、且会接管屏幕。 | MIT | C（3/6） | [中](categories/media-processing/nle-automation/jianying-editor-skill.zh.md) · [EN](categories/media-processing/nle-automation/jianying-editor-skill.md) |
| **Auto-Editor** | 当反复出现的任务是从长素材里剪掉冷场时用它——按响度／运动打标签的命令行工具，还能导出 Premiere／Resolve／Final Cut／ShotCut／Kdenlive 可导入的时间线；忘了 `pip`，用二进制或 Homebrew 装。 | Unlicense | B（6/6） | [中](categories/media-processing/video-audio/auto-editor.zh.md) · [EN](categories/media-processing/video-audio/auto-editor.md) |

### video-production

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **OpenMontage** | 当你想让 AI 编程助手从一句自然语言描述出发，完成研究、脚本、素材生成、合成与渲染，产出完整视频（解说、预告片、动画、纪录片蒙太奇）时使用。 | AGPL-3.0 | C（6/6） | [中](categories/video-production/open-montage.zh.md) · [EN](categories/video-production/open-montage.md) |
| **HyperFrames** | 当你需要确定性、代码形态的视频——HTML composition 在 CI 里渲染成 MP4——并希望 agent skill 覆盖整条生产回路时用它；它是渲染引擎，不是生成式视频模型。 | Apache-2.0 | B（6/6） | [中](categories/video-production/hyperframes.zh.md) · [EN](categories/video-production/hyperframes.md) |
| **anything2explainer** | 当你想让 Claude Code / Codex skill 把一个主题做成带配音的 MG 科普讲解视频（中文或英文）时用它——9 阶段多 agent 流水线带人工确认点和量化 QC；固定黑底风格，PolyForm 非商用许可。 | PolyForm-Noncommercial-1.0.0 | C（3/6） | [中](categories/video-production/anything2explainer.zh.md) · [EN](categories/video-production/anything2explainer.md) |
| **Hypit** | 当你想让 agent 把某条特定爆款视频克隆成可编辑、词锚定的 SVML workflow，并通过换脸/换词/换 B-roll 批量出变体时用它——agent 优先、非 OSI 许可证、非常年轻。 | Hypit Open Source License（modified Apache-2.0，非 OSI） | B（3/6） | [中](categories/video-production/hypit.zh.md) · [EN](categories/video-production/hypit.md) |
| **Remotion** | 当 React 优先的团队需要久经验证的程序化视频——composition 即 React 组件、经 headless Chrome 渲染、带成熟 Lambda 云渲染——且接受 source-available 许可证（个人与 3 人以下公司免费）时用它。 | Remotion License（source-available，非 OSI） | A（4/6） | [中](categories/video-production/remotion.zh.md) · [EN](categories/video-production/remotion.md) |
| **MoneyPrinterTurbo** | 当你需要一台可自托管的 MIT 家电（WebUI + API），把主题变成近零边际成本的口播库存素材短视频时用它——不做爆款结构克隆，不需要 coding agent。 | MIT | A（4/6） | [中](categories/video-production/moneyprinter-turbo.zh.md) · [EN](categories/video-production/moneyprinter-turbo.md) |
| **video-shotcraft** | 当 coding agent 应该用 150+ 张镜头配方卡、真实页面截图、2.5D 运镜和一支已验收的 Remotion 模板，把你的产品或网页做成电影感宣传片时用它——仅约 2 个月历史、无 tagged release，且产出 Remotion composition，受引擎「3 人以上需付费」的许可门槛约束。 | Apache-2.0 | B（4/6） | [中](categories/video-production/video-shotcraft.zh.md) · [EN](categories/video-production/video-shotcraft.md) |
| **claude-video** | 让 Claude “看视频”的 `/watch` skill：下载视频、抽帧、转录，并把这些证据交给 Claude。 | MIT | C（4/6） | [中](categories/media-processing/video-audio/claude-video.zh.md) · [EN](categories/media-processing/video-audio/claude-video.md) |

### llm-chat-ui

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **NextChat** | 当你想要一个私有、可自部署、跨 web/桌面/移动 的多 provider AI 聊天前端时用它——不是多用户 RBAC 团队平台。 | MIT | A（5/6） | [中](categories/llm-chat-ui/nextchat.zh.md) · [EN](categories/llm-chat-ui/nextchat.md) |
| **Open WebUI** | 自托管 AI 聊天平台，内置 RAG、支持 Ollama、可离线运行——但默认偏单用户。 | NOASSERTION | B（5/6） | [中](categories/llm-chat-ui/open-webui.zh.md) · [EN](categories/llm-chat-ui/open-webui.md) |
| **LibreChat** | Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active | MIT | B（6/6） | [EN](categories/llm-chat-ui/librechat.md) · [中](categories/llm-chat-ui/librechat.zh.md) |

### markdown-tools

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **CommonMark** | 当你需要规范合规、可遍历 AST 的 Markdown 官方参考实现时用它——但它不以速度见长，也不支持 GFM 或插件生态。 | BSD-3-Clause | B（5/6） | [中](categories/markdown-tools/commonmark.zh.md) · [EN](categories/markdown-tools/commonmark.md) |
| **Markdown Here** | 当你想用浏览器/Thunderbird 扩展把邮件用 Markdown 写好、发送前渲染成 HTML 时用它——注意维护已放缓。 | MIT | C（4/6） | [中](categories/markdown-tools/markdown-here.zh.md) · [EN](categories/markdown-tools/markdown-here.md) |
| **marked** | 当你需要一个快速、底层的 JS Markdown→HTML 解析器时用它——但你得自己做 XSS 消毒，且不要求严格 CommonMark。 | MIT | A（5/6） | [中](categories/markdown-tools/marked.zh.md) · [EN](categories/markdown-tools/marked.md) |
| **remark** | 当你需要完整的 mdast AST 管线来解析、变换、lint 和序列化 Markdown 时用它——但它是工具链，不是一次调用的渲染器。 | MIT | A（6/6） | [中](categories/markdown-tools/remark.zh.md) · [EN](categories/markdown-tools/remark.md) |
| **markdown-it** | 当你需要一个严格遵循 CommonMark/GFM、可插拔的 JS Markdown→HTML 解析器时用它——但插件生态会增加体积，且处理不受信任内容时仍需消毒。 | MIT | A（6/6） | [中](categories/markdown-tools/markdown-it.zh.md) · [EN](categories/markdown-tools/markdown-it.md) |
| **micromark** | 当你需要一个低层、面向流式处理的 JS CommonMark/GFM 分词器时用它——remark 的底层引擎——但渲染层要你自己搭。 | MIT | B（4/6） | [中](categories/markdown-tools/micromark.zh.md) · [EN](categories/markdown-tools/micromark.md) |
| **Pandoc** | Universal markup converter | GPL-2.0 | B（6/6） | [EN](categories/markdown-tools/pandoc.md) · [中](categories/markdown-tools/pandoc.zh.md) |
| **Goldmark** | :trophy: A markdown parser written in Go. Easy to extend, standard(CommonMark) compliant, well structured. | MIT | B（4/6） | [EN](categories/markdown-tools/goldmark.md) · [中](categories/markdown-tools/goldmark.zh.md) |
| **markdownlint** | A Node.js style checker and lint tool for Markdown/CommonMark files. | MIT | A（6/6） | [EN](categories/markdown-tools/markdownlint.md) · [中](categories/markdown-tools/markdownlint.zh.md) |
| **MDX** | 当文档活在 React／Preact／Vue 应用里、正文需要 import 并渲染你自己的组件时用它——但交付物是独立 PDF、书或可发布文档时不要用。 | MIT | B（5/6） | [中](categories/markdown-tools/mdx.zh.md) · [EN](categories/markdown-tools/mdx.md) |

### typesetting

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Asciidoctor** | 当技术文档需要从纯文本源发布成 HTML、DocBook、EPUB 或 man page 时用它——但你需要排版引擎或印刷级 PDF 时不要用。 | MIT | C（4/6） | [中](categories/typesetting/asciidoctor.zh.md) · [EN](categories/typesetting/asciidoctor.md) |
| **LaTeX** | 当投稿方的 class 文件、几十年的宏包积累、或几十年稳定的源语言决定结果时用它——但没人愿意维护 `\begin{}` 脚手架、或你需要从同一份文件出 HTML 时不要用。 | LPPL-1.3c | B（6/6） | [中](categories/typesetting/latex.zh.md) · [EN](categories/typesetting/latex.md) |
| **Quarkdown** | 当你需要一份保持 Markdown 可读性的源文件编译成网页、印刷 PDF、reveal.js 幻灯片与文档站时用它——但交付物必须是 Word、许可必须宽松、或印刷保真度是硬要求时不要用。 | GPL-3.0 / AGPL-3.0 | B（5/6） | [中](categories/typesetting/quarkdown.zh.md) · [EN](categories/typesetting/quarkdown.md) |
| **Typst** | 当你能自己选源语言，想要学习曲线短、Apache-2.0 许可的印刷级 PDF 时用它——但投稿方指定 LaTeX class 文件、或源必须保持 Markdown 时不要用。 | Apache-2.0 | A（6/6） | [中](categories/typesetting/typst.zh.md) · [EN](categories/typesetting/typst.md) |

### pdf-tools

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **PDF.js** | 当你需要在浏览器/Node 里渲染或读取 PDF（Firefox 的引擎）时用它——它不创建也不编辑 PDF。 | Apache-2.0 | A（6/6） | [中](categories/pdf-tools/pdfjs.zh.md) · [EN](categories/pdf-tools/pdfjs.md) |
| **pdf-lib** | 当你需要在 JS/TS 里创建或修改 PDF——在浏览器、Node、Deno 或 React Native 中——且不需要原生依赖时用它。 | MIT | C（4/6） | [中](categories/pdf-tools/pdf-lib.zh.md) · [EN](categories/pdf-tools/pdf-lib.md) |
| **jsPDF** | 当你需要在浏览器里从 HTML、文本和图形生成客户端 PDF——它只创建不编辑已有 PDF——时用它。 | MIT | B（6/6） | [中](categories/pdf-tools/jspdf.zh.md) · [EN](categories/pdf-tools/jspdf.md) |
| **PyMuPDF** | PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents. | AGPL-3.0 | B（6/6） | [EN](categories/pdf-tools/pymupdf.md) · [中](categories/pdf-tools/pymupdf.zh.md) |
| **pdfplumber** | Plumb a PDF for detailed information about each char, rectangle, line, et cetera — and easily extract text and tables. | MIT | B（6/6） | [EN](categories/pdf-tools/pdfplumber.md) · [中](categories/pdf-tools/pdfplumber.zh.md) |
| **OCRmyPDF** | OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched | MPL-2.0 | B（6/6） | [EN](categories/pdf-tools/ocrmypdf.md) · [中](categories/pdf-tools/ocrmypdf.zh.md) |
| **qpdf** | qpdf: A content-preserving PDF document transformer | Apache-2.0 | B（6/6） | [EN](categories/pdf-tools/qpdf.md) · [中](categories/pdf-tools/qpdf.zh.md) |
| **SAPP** | 当 PHP 应用必须追加 PKCS#12 签名、又不能破坏已有 PDF 修订时用它——规范覆盖较窄，也不支持加密 PDF。 | LGPL-3.0-or-later | B（5/6） | [中](categories/pdf-tools/sapp.zh.md) · [EN](categories/pdf-tools/sapp.md) |

### workflow-orchestration

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Apache Airflow** | 当你要用 Python DAG 加 Web UI 编排定时批处理数据管线时用它——不适合低延迟或事件驱动流。 | Apache-2.0 | A（6/6） | [中](categories/workflow-orchestration/airflow.zh.md) · [EN](categories/workflow-orchestration/airflow.md) |
| **Gaia** | 当作只读参考研究「流水线即编译插件」设计时用它——仓库已归档废弃，绝不可用于新的生产部署。 | Apache-2.0 | D（5/6） | [中](categories/workflow-orchestration/gaia.zh.md) · [EN](categories/workflow-orchestration/gaia.md) |
| **Airflow Maintenance DAGs** | 当自管 Airflow 需要现成 DAG 清理元数据库行和陈旧日志时用它——它执行依赖版本内部结构的破坏性删除，先 dry-run 并备份。 | Apache-2.0 | D（4/6） | [中](categories/workflow-orchestration/airflow-maintenance-dags.zh.md) · [EN](categories/workflow-orchestration/airflow-maintenance-dags.md) |
| **n8n** | 一款 fair-code 工作流自动化平台，原生支持 AI 能力——结合可视化搭建与自定义代码，可自托管或上云，内置 400 余种集成。 | NOASSERTION (fair-code) | A（4/6） | [中](categories/workflow-orchestration/n8n.zh.md) · [EN](categories/workflow-orchestration/n8n.md) |
| **Argo Workflows** | Workflow Engine for Kubernetes | Apache-2.0 | A（4/6） | [EN](categories/workflow-orchestration/argo-workflows.md) · [中](categories/workflow-orchestration/argo-workflows.zh.md) |
| **Prefect** | Prefect is a workflow orchestration framework for building resilient data pipelines in Python. | Apache-2.0 | A（6/6） | [EN](categories/workflow-orchestration/prefect.md) · [中](categories/workflow-orchestration/prefect.zh.md) |
| **Dagster** | An orchestration platform for the development, production, and observation of data assets. | Apache-2.0 | A（6/6） | [EN](categories/workflow-orchestration/dagster.md) · [中](categories/workflow-orchestration/dagster.zh.md) |
| **Temporal** | Temporal service | MIT | A（5/6） | [EN](categories/workflow-orchestration/temporal.md) · [中](categories/workflow-orchestration/temporal.zh.md) |

### llm-inference

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Modular Platform (MAX + Mojo)** | 当你想要高性能 GPU/CPU 推理平台（MAX）加 Mojo 系统语言、并接受单厂商绑定与部分非生产许可时用它。 | Apache-2.0 (mixed) | B（5/6） | [中](categories/llm-inference/serving-engines/modular.zh.md) · [EN](categories/llm-inference/serving-engines/modular.md) |
| **omlx** | 当你想在 Mac（Apple Silicon）上用 MLX 跑带 SSD 分层 KV 缓存的本地 LLM 推理服务时用它——年轻的单人仓库，star 数存疑。 | Apache-2.0 | B（5/6） | [中](categories/llm-inference/local-runtimes/omlx.zh.md) · [EN](categories/llm-inference/local-runtimes/omlx.md) |
| **MTPLX** | 当你想让模型自带的 MTP 头在 Mac 上以精确投机解码把 Qwen 3.8 跑出约 2 倍速、并要 OpenAI/Anthropic 服务器与应用形态时用它——接受约五个月大、作者主导的仓库与产品内署名条款。 | Apache-2.0（含署名 NOTICE） | B（6/6） | [中](categories/llm-inference/local-runtimes/mtplx.zh.md) · [EN](categories/llm-inference/local-runtimes/mtplx.md) |
| **TensorRT-LLM** | 当你需要在 NVIDIA GPU 上榨取最大 LLM 推理吞吐、并愿意接受仅限 NVIDIA 的绑定、复杂的构建/engine 编译流程以及闭源内核时用它。 | Apache-2.0 | B（4/6） | [中](categories/llm-inference/serving-engines/tensorrt-llm.zh.md) · [EN](categories/llm-inference/serving-engines/tensorrt-llm.md) |
| **vLLM** | 当你想要事实上的开源 LLM 服务引擎，带 PagedAttention、连续批处理和 OpenAI 兼容 API 时用它——接受 NVIDIA 主导的 GPU 运维和快速迭代的代码库。 | Apache-2.0 | A（5/6） | [中](categories/llm-inference/serving-engines/vllm.zh.md) · [EN](categories/llm-inference/serving-engines/vllm.md) |
| **SGLang** | 当你需要带 RadixAttention 前缀缓存和结构化生成的快速 LLM 服务引擎——适合工具调用型 agent 和 JSON 模式 API——并接受比 vLLM 更年轻、更小的生态时用它。 | Apache-2.0 | A（5/6） | [中](categories/llm-inference/serving-engines/sglang.zh.md) · [EN](categories/llm-inference/serving-engines/sglang.md) |
| **Ray Serve** | 当你需要通用、可扩展的 Python 模型服务框架，支持多模型组合和自动扩缩容时用它——但要接受 Ray 的运维复杂性和学习曲线。 | Apache-2.0 | A（6/6） | [中](categories/llm-inference/serving-engines/ray-serve.zh.md) · [EN](categories/llm-inference/serving-engines/ray-serve.md) |
| **llama.cpp** | 当你想要那个无依赖的 C/C++ 上游引擎、跑在目前最宽的硬件矩阵上、既能嵌入也能本地起服务时用它——接受没有 semver、没有模型管理、只有 flag 级 API。 | MIT | B（6/6） | [EN](categories/llm-inference/local-runtimes/llama-cpp.md) · [中](categories/llm-inference/local-runtimes/llama-cpp.zh.md) |
| **Ollama** | 当你想要托管的本地模型仓库，配 OpenAI/Anthropic 兼容 API、Docker 部署与客户端 SDK 时用它——接受包装层的参数子集、4096 token 的默认上下文，以及没有服务级批处理。 | MIT | A（4/6） | [EN](categories/llm-inference/local-runtimes/ollama.md) · [中](categories/llm-inference/local-runtimes/ollama.zh.md) |
| **BentoML** | The easiest way to serve AI apps and models - Build Model Inference APIs, Job queues, LLM apps, Multi-model pipelines, and more! | Apache-2.0 | B（6/6） | [EN](categories/llm-inference/serving-engines/bentoml.md) · [中](categories/llm-inference/serving-engines/bentoml.zh.md) |
| **LMDeploy** | LMDeploy is a toolkit for compressing, deploying, and serving LLMs. | Apache-2.0 | A（6/6） | [EN](categories/llm-inference/serving-engines/lmdeploy.md) · [中](categories/llm-inference/serving-engines/lmdeploy.zh.md) |
| **Text Generation Inference (TGI)** | 只把它当模式参考或用于已 pin 住的既有部署，因为仓库已归档——要维护中的服务端选 vLLM 或 SGLang，要本地用选 llama.cpp 或 Ollama。 | Apache-2.0 | C（6/6） | [EN](categories/llm-inference/serving-engines/text-generation-inference.md) · [中](categories/llm-inference/serving-engines/text-generation-inference.zh.md) |
| **Magnitude** | 当机器能力未知、你要下载前的速度与内存估算加一键接入已有 coding harness 时用它——接受一个两个月大、单厂商所有、且在 Apple Silicon 上报告比 llama.cpp 慢约 6 倍的仓库。 | Apache-2.0 | B（6/6） | [EN](categories/llm-inference/local-runtimes/magnitude.md) · [中](categories/llm-inference/local-runtimes/magnitude.zh.md) |

### task-queue

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **XXL-JOB** | 当 Java/Spring 团队需要中心化、可视化、分片的定时作业调度时用它——注意 GPL-3.0 与中心调度器单点。 | GPL-3.0 | B（5/6） | [中](categories/task-queue/xxl-job.zh.md) · [EN](categories/task-queue/xxl-job.md) |
| **Celery** | 当 Python 应用需要把异步/后台任务规模化外包时用它——代价是要跑 broker + worker。 | BSD-3-Clause | B（5/6） | [中](categories/task-queue/celery.zh.md) · [EN](categories/task-queue/celery.md) |
| **Kombu** | 当 Python 服务要在可替换 broker（RabbitMQ、Redis、SQS）间收发消息时用它——虚拟 transport 对 AMQP 的模拟并不完整，换 URL 不等于行为一致。 | BSD-3-Clause | A（5/6） | [中](categories/task-queue/kombu.zh.md) · [EN](categories/task-queue/kombu.md) |
| **Flower** | 当生产 Celery 集群需要实时面板查看、控制 worker 并导出 Prometheus 指标时用它——它能撤销任务，绝不能无鉴权暴露。 | BSD-3-Clause | B（4/6） | [中](categories/task-queue/flower.zh.md) · [EN](categories/task-queue/flower.md) |
### im-automation

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **ItChat** | 仅作为旧版微信机器人代码学习——已停更，且其依赖的网页协议已失效，基本不可用。 | MIT | C（4/6） | [中](categories/im-automation/itchat.zh.md) · [EN](categories/im-automation/itchat.md) |
| **WeChatPlugin-MacOS** | 当前微信别用——一个 patch macOS 微信客户端二进制的小助手，每次微信更新就失效、已 ~2 年没动；有封号与安全风险。 | MIT | D（3/6） | [中](categories/im-automation/wechatplugin-macos.zh.md) · [EN](categories/im-automation/wechatplugin-macos.md) |
| **wxpy** | 仅作为旧版微信机器人代码学习——2019 年起已归档，且基于已失效的微信网页协议，基本不可用。 | MIT | D（5/6） | [中](categories/im-automation/wxpy.zh.md) · [EN](categories/im-automation/wxpy.md) |
| **wxappUnpacker** | 当你需要把自有的微信小程序 .wxapkg 包反编译回可读源码时用它——但本仓库已被清空成墓碑，请改用仍存活的 fork。 | GPL-3.0-or-later | E（4/6） | [中](categories/im-automation/wxappunpacker.zh.md) · [EN](categories/im-automation/wxappunpacker.md) |
| **Douyin-Bot** | 仅当你想要一份 ADB 屏幕坐标手机自动化的历史示例时用它——切勿部署，2018 年的硬编码坐标与失效的腾讯人脸 API 意味着它早已跑不通。 | MIT | D（3/6） | [中](categories/im-automation/douyin-bot.zh.md) · [EN](categories/im-automation/douyin-bot.md) |
| **WeChat Bot** | 当一个 Node CLI 必须把微信、飞书、Telegram 与 WhatsApp 接到多个 LLM 时用它——个人微信仍走非官方通道，并伴随账号风险。 | MIT | B（5/6） | [中](categories/im-automation/wechat-bot.zh.md) · [EN](categories/im-automation/wechat-bot.md) |
| **ChatGPT-wechat-bot** | 仅把它当作 2022 至 2023 年 Wechaty 与 ChatGPT 的小型参考代码——项目已停滞、默认配置过时，不适合作为生产底座。 | MIT | D（3/6） | [中](categories/im-automation/chatgpt-wechat-bot.zh.md) · [EN](categories/im-automation/chatgpt-wechat-bot.md) |
| **OpeniLink Hub** | 当多个 iLink 微信 Bot 需要自托管管理、trace、Webhook 和 App 时用它——项目年轻且无官方关联，还扩大了认证与 Registry 信任边界。 | MIT | B（5/6） | [中](categories/im-automation/openilink-hub.zh.md) · [EN](categories/im-automation/openilink-hub.md) |
| **Dify Enterprise WeChat Bot** | 仅用于维持固定 Windows 企业微信到 Dify 的桌面集成——项目已停滞、包含闭源 helper，Workflow 支持也未完成。 | NOASSERTION | C（3/6） | [中](categories/im-automation/dify-enterprise-wechat-bot.zh.md) · [EN](categories/im-automation/dify-enterprise-wechat-bot.md) |
### web-ui

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Driver.js** | 当你想在网页上加一个极简、无依赖的产品引导/功能高亮时用它——不是完整的 onboarding 平台。 | MIT | B（5/6） | [中](categories/web-ui/product-tours/driver-js.zh.md) · [EN](categories/web-ui/product-tours/driver-js.md) |
| **Shepherd.js** | 当你想要一个稳健、框架无关的产品引导库，支持高级定位和复杂多步骤 onboarding 时用它——但你要接受比 Driver.js 更大的包体积。 | MIT | B（4/6） | [中](categories/web-ui/product-tours/shepherd-js.zh.md) · [EN](categories/web-ui/product-tours/shepherd-js.md) |
| **Intro.js** | 当你想要一个成熟、框架无关、文档详尽的产品引导库时用它——但你要接受非商用 AGPL-3.0，或必须购买商业授权。 | AGPL-3.0 | B（4/6） | [中](categories/web-ui/product-tours/intro-js.zh.md) · [EN](categories/web-ui/product-tours/intro-js.md) |
| **Vue.js** | 当你想要一个渐进式、易于上手的 JavaScript 框架，带优秀文档、温和学习曲线和可增量采纳的架构时用它——但你要接受它在西方就业市场比 React 小，且没有 mega-corporate 背书。 | MIT | A（6/6） | [中](categories/web-ui/frameworks/vue.zh.md) · [EN](categories/web-ui/frameworks/vue.md) |
| **Svelte** | 当你想要一个编译时前端框架，带小包体积、无虚拟 DOM 和可读性强的语法时用它——但你要接受它的生态和就业市场比 React 或 Vue 小。 | MIT | A（6/6） | [中](categories/web-ui/frameworks/svelte.zh.md) · [EN](categories/web-ui/frameworks/svelte.md) |
| **shadcn/ui** | 一套精心设计、无障碍的 React 组件，复制进项目并完全拥有——但它需要 React 和 Tailwind CSS。 | MIT | A（6/6） | [中](categories/web-ui/component-libraries/shadcn-ui.zh.md) · [EN](categories/web-ui/component-libraries/shadcn-ui.md) |
| **Angular** | 当你需要一个成熟、opinionated、带依赖注入和强类型的全栈框架，用于企业级大规模 web 应用时用它——但它很重，小项目用它过度。 | MIT | A（6/6） | [中](categories/web-ui/frameworks/angular.zh.md) · [EN](categories/web-ui/frameworks/angular.md) |
| **Ant Design** | 当你想要一套完整、生产就绪、带企业级设计规范、主题化和无障碍支持的 React UI 组件库时用它——但它仅限 React，且设计风格明显偏「中式企业风」。 | MIT | A（5/6） | [中](categories/web-ui/component-libraries/ant-design.zh.md) · [EN](categories/web-ui/component-libraries/ant-design.md) |
| **Lit** | 当你需要一套轻量、基于标准的 Web Components，能在任何框架中工作时用它——但你要接受生态较小，且需要学习 Web Components。 | BSD-3-Clause | A（6/6） | [中](categories/web-ui/frameworks/lit.zh.md) · [EN](categories/web-ui/frameworks/lit.md) |
| **React** | 当你想要最流行的 UI 库，带庞大生态、深厚的人才池和声明式组件模型时用它——但你要接受需要自己组合路由、状态管理和构建管线。 | MIT | A（6/6） | [中](categories/web-ui/frameworks/react.zh.md) · [EN](categories/web-ui/frameworks/react.md) |
| **Next.js** | 当你想要一个全栈 React 框架，内置 SSR、SSG、基于文件的路由和 API 路由时用它——但你要接受 Vercel 对路线图的影响，以及比纯 React 更强的主见架构。 | MIT | A（5/6） | [中](categories/web-ui/frameworks/nextjs.zh.md) · [EN](categories/web-ui/frameworks/nextjs.md) |
| **SvelteKit** | web development, streamlined | MIT | A（6/6） | [EN](categories/web-ui/frameworks/sveltekit.md) · [中](categories/web-ui/frameworks/sveltekit.zh.md) |
| **Reactour** | Tourist Guide into your React Components | MIT | B（5/6） | [EN](categories/web-ui/product-tours/reactour.md) · [中](categories/web-ui/product-tours/reactour.zh.md) |
| **react-joyride** | Create guided tours in your apps | MIT | B（6/6） | [EN](categories/web-ui/product-tours/react-joyride.md) · [中](categories/web-ui/product-tours/react-joyride.zh.md) |
| **Material UI (MUI)** | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. | MIT | A（5/6） | [EN](categories/web-ui/component-libraries/material-ui.md) · [中](categories/web-ui/component-libraries/material-ui.zh.md) |
| **Chakra UI** | Chakra UI is a component system for building SaaS products with speed ⚡️ | MIT | B（5/6） | [EN](categories/web-ui/component-libraries/chakra-ui.md) · [中](categories/web-ui/component-libraries/chakra-ui.zh.md) |
| **Radix UI Primitives** | Radix Primitives is an open-source UI component library for building high-quality, accessible design systems and web apps. Maintained by @workos. | MIT | B（5/6） | [EN](categories/web-ui/component-libraries/radix-ui.md) · [中](categories/web-ui/component-libraries/radix-ui.zh.md) |
| **Nuxt** | the full-stack Vue framework | MIT | A（6/6） | [EN](categories/web-ui/frameworks/nuxt.md) · [中](categories/web-ui/frameworks/nuxt.zh.md) |
| **Astro** | 当站点是内容集合、只需少数交互组件时用它——但交付物是带版本的文档站、或站点本质是全栈应用时不要用。 | MIT | A（5/6） | [中](categories/web-ui/frameworks/astro.zh.md) · [EN](categories/web-ui/frameworks/astro.md) |
| **Docusaurus** | 当需要第一天就有带版本、可搜索、支持 i18n 的文档站时用它——但站点是通用内容站、或你宁愿自己组装文档那套家具时不要用。 | MIT | B（6/6） | [中](categories/web-ui/frameworks/docusaurus.zh.md) · [EN](categories/web-ui/frameworks/docusaurus.md) |
| **Nextra** | 当文档必须活在既有 Next.js 应用里、一层薄 MDX 就够了时用它——但你需要版本化文档、或需要背后有较大维护团队的项目时不要用。 | MIT | B（6/6） | [中](categories/web-ui/frameworks/nextra.zh.md) · [EN](categories/web-ui/frameworks/nextra.md) |

### proxy-pool

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **proxy_pool** | 当爬虫需要一个走简单 API 的轮换免费代理 IP 池时用它——前提是接受免费代理不稳定、不安全。 | MIT | A（4/6） | [中](categories/proxy-pool/proxy-pool.zh.md) · [EN](categories/proxy-pool/proxy-pool.md) |
| **ProxyBroker** | 当你想为低风险原型用一个本地轮换端点临时凑一批免费公共代理时用它——但它自约 2018 年起实质冻结，在新版 Python 上不锁版本普遍跑不起来。 | Apache-2.0 | D（4/6） | [中](categories/proxy-pool/proxybroker.zh.md) · [EN](categories/proxy-pool/proxybroker.md) |
| **Scylla** | 当你想用一条 Docker 命令跑一个常驻自托管、带 JSON API、质量打分与面板的免费代理池时用它——但其正向代理不支持 HTTPS，且发布自 2022 年起停滞。 | Apache-2.0 | C（3/6） | [中](categories/proxy-pool/scylla.zh.md) · [EN](categories/proxy-pool/scylla.md) |
| **haipproxy** | 当你确实需要为多机大规模爬取搭一个基于 Scrapy＋Redis 的分布式高可用免费代理池时用它——但它自 2022 年起休眠、跑的是 2018 年代 Py2／3 代码，且是最难运维的代理池。 | MIT | D（3/6） | [中](categories/proxy-pool/haipproxy.zh.md) · [EN](categories/proxy-pool/haipproxy.md) |
### debugging-proxy

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **whistle** | 当 web/移动开发者要通过规则化 Web UI 抓取、检查、改写并 mock HTTP(S)/WebSocket 流量时用它——是开发调试代理，不是生产网关或爬虫代理池。 | MIT | B（6/6） | [中](categories/debugging-proxy/whistle.zh.md) · [EN](categories/debugging-proxy/whistle.md) |
| **AnyProxy** | 当你想用纯 JS 规则脚本化地拦截并改写 HTTP/HTTPS 流量、需要一个 Node.js MITM 代理时用它——但 master 自 2020 年已冻结，新项目请优先选 whistle。 | Apache-2.0 | C（4/6） | [中](categories/debugging-proxy/anyproxy.zh.md) · [EN](categories/debugging-proxy/anyproxy.md) |
| **mitmproxy** | An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers. | MIT | A（6/6） | [EN](categories/debugging-proxy/mitmproxy.md) · [中](categories/debugging-proxy/mitmproxy.zh.md) |

### web-scraping

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **newspaper** | 用来从新闻 URL 批量提取正文、作者和元数据——但原版（newspaper3k）已陈旧，活跃路径是 newspaper4k 分叉。 | MIT | B（5/6） | [中](categories/web-scraping/article-extraction/newspaper.zh.md) · [EN](categories/web-scraping/article-extraction/newspaper.md) |
| **requests-html** | 可作为小型 requests + HTML 解析脚本参考——基本停更（~2 年没动），JS 渲染路径脆弱；新项目优先 Playwright + parsel。 | MIT | D（3/6） | [中](categories/web-scraping/crawling-tools/requests-html.zh.md) · [EN](categories/web-scraping/crawling-tools/requests-html.md) |
| **Firecrawl** | 规模化搜索、抓取网页并提取干净 Markdown 或结构化数据的 API——但 AGPL-3.0 可能限制商用。 | AGPL-3.0 | B（6/6） | [中](categories/web-scraping/crawling-tools/firecrawl.zh.md) · [EN](categories/web-scraping/crawling-tools/firecrawl.md) |
| **trafilatura** | Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extraction, output as CSV, JSON, HTML, MD, TXT, XML | Apache-2.0 | B（6/6） | [EN](categories/web-scraping/article-extraction/trafilatura.md) · [中](categories/web-scraping/article-extraction/trafilatura.zh.md) |

### auth

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Authomatic** | 当需要框架无关的 Python 应用通过 OAuth1／OAuth2／OpenID 实现轻量「用 X 登录」、且会话持久化自己负责时用它——但它迭代缓慢，而认证库修复迟缓本身就是安全风险。 | MIT | C（5/6） | [中](categories/auth/authomatic.zh.md) · [EN](categories/auth/authomatic.md) |
| **django-rules** | 当 Django 的对象级权限是由逻辑（谓词）计算得出、而非存储授权、且不想加数据库表时用它——但若管理员需在运行时为单个对象分配权限，则应改用 django-guardian。 | MIT | B（4/6） | [中](categories/auth/django-rules.zh.md) · [EN](categories/auth/django-rules.md) |
| **Keycloak** | Open Source Identity and Access Management For Modern Applications and Services | Apache-2.0 | A（6/6） | [EN](categories/auth/keycloak.md) · [中](categories/auth/keycloak.zh.md) |
| **Casbin** | Apache Casbin: an authorization library that supports access control models like ACL, RBAC, ABAC. | Apache-2.0 | B（5/6） | [EN](categories/auth/casbin.md) · [中](categories/auth/casbin.zh.md) |
| **OpenFGA** | A high performance and flexible authorization/permission engine built for developers and inspired by Google Zanzibar | Apache-2.0 | A（5/6） | [EN](categories/auth/openfga.md) · [中](categories/auth/openfga.zh.md) |

### databases

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **PikiwiDB** | 当大规模 Redis 数据集撑爆内存、内存成本成为主要负担时用它——RocksDB 落盘、兼容 Redis 协议，单节点可存数百 GB；但它以延迟换容量，若每次操作都要微秒级则不合适。 | BSD-3-Clause | A（4/6） | [中](categories/databases/database-engines/pikiwidb.zh.md) · [EN](categories/databases/database-engines/pikiwidb.md) |
| **elasticsearch-dsl-py** | 当你维护仍锁定独立 elasticsearch-dsl 包的旧 Python 代码时才用它——任何新项目它都已归档，请改装 elasticsearch>=8.18 并使用 elasticsearch.dsl。 | Apache-2.0 | D（4/6） | [中](categories/databases/database-clients/elasticsearch-dsl-py.zh.md) · [EN](categories/databases/database-clients/elasticsearch-dsl-py.md) |
| **elasticsearch-sql** | 当熟悉 SQL 的团队想免学 JSON Query DSL 直接查 Elasticsearch 时用它——但 Elastic 官方的 SQL／ES\|QL 已与之重叠，能覆盖你的需求时优先用官方特性。 | Apache-2.0 | B（4/6） | [中](categories/databases/database-clients/elasticsearch-sql.zh.md) · [EN](categories/databases/database-clients/elasticsearch-sql.md) |
| **go-mysql-elasticsearch** | 当你想用单个 Go 二进制 tail MySQL binlog、单向中等规模同步到 Elasticsearch 时用它——但它自 2023 年起无人维护、无任何发布，请当作 fork 自管的项目对待。 | MIT | D（3/6） | [中](categories/databases/data-sync/go-mysql-elasticsearch.zh.md) · [EN](categories/databases/data-sync/go-mysql-elasticsearch.md) |
| **python-mysql-replication** | 当你想用纯 Python 原语把 MySQL binlog 流式解析成带类型的事件、自建可控 CDC 循环时用它——但 checkpoint、去重和精确一次投递全得你自己负责。 | Apache-2.0 | D（5/6） | [中](categories/databases/data-sync/python-mysql-replication.zh.md) · [EN](categories/databases/data-sync/python-mysql-replication.md) |
| **PrettyZoo** | 当你在开发或故障排查时想用友好的桌面 GUI 浏览并轻量编辑 ZooKeeper znode 树时用它——但它自 2023 年起已归档，新 JDK／macOS 可能跑不起来且无上游修复。 | Apache-2.0 | D（4/6） | [中](categories/databases/database-clients/prettyzoo.zh.md) · [EN](categories/databases/database-clients/prettyzoo.md) |
| **RDR** | 当 Redis 触发 maxmemory 告警、需要离线快速按前缀分析 RDB 快照时用它——但内存数字是近似值，且项目已停滞（v0.0.1，2019 年）。 | Apache-2.0 | D（3/6） | [中](categories/databases/database-clients/rdr.zh.md) · [EN](categories/databases/database-clients/rdr.md) |
| **Supabase** | 基于 PostgreSQL 构建的开源 Firebase 替代方案，包含身份认证、自动生成 API、实时订阅、边缘函数和向量存储——但它与 Postgres 深度绑定。 | Apache-2.0 | A（5/6） | [中](categories/databases/database-engines/supabase.zh.md) · [EN](categories/databases/database-engines/supabase.md) |
| **DuckDB** | DuckDB is an analytical in-process SQL database management system | MIT | A（6/6） | [EN](categories/databases/database-engines/duckdb.md) · [中](categories/databases/database-engines/duckdb.zh.md) |
| **ClickHouse** | ClickHouse® is a real-time analytics database management system | Apache-2.0 | A（4/6） | [EN](categories/databases/database-engines/clickhouse.md) · [中](categories/databases/database-engines/clickhouse.zh.md) |
| **DBeaver** | Free universal database tool and SQL client | Apache-2.0 | A（5/6） | [EN](categories/databases/database-clients/dbeaver.md) · [中](categories/databases/database-clients/dbeaver.zh.md) |
| **Debezium** | Change data capture for a variety of databases. Please log issues at https://github.com/debezium/dbz/issues. | Apache-2.0 | A（4/6） | [EN](categories/databases/data-sync/debezium.md) · [中](categories/databases/data-sync/debezium.zh.md) |
| **Valkey** | A flexible distributed key-value database that is optimized for caching and other realtime workloads. | BSD-3-Clause | A（5/6） | [EN](categories/databases/database-engines/valkey.md) · [中](categories/databases/database-engines/valkey.zh.md) |

### object-storage

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Silo** | 你已经在跑 MinIO、而上游社区版已经终结时用它——Silo 让 S3 API、落盘格式与 `MINIO_*` 命名继续可用；代价是可执行文件／软件包／镜像改名为 `silo`，且它是单一维护者对单一代码库的 fork。 | AGPL-3.0 | B（4/6） | [中](categories/object-storage/silo.zh.md) · [EN](categories/object-storage/silo.md) |
| **MinIO** | 用这一页决定你手上已经跑着的 MinIO 怎么办：社区仓库已归档（2026-04）且无人维护，所以这是“迁到在维护的 fork 或别的存储”的选择，而不是新部署的选项。 | AGPL-3.0 | D（5/6） | [中](categories/object-storage/minio.zh.md) · [EN](categories/object-storage/minio.md) |
| **Garage** | 想用几台分散各地、便宜的机器拼出一个 S3 端点、跨站点复制、其中一台离线仍可用时用它——但它的 S3 能力面刻意不完整（没有 ACL／策略语义）。 | AGPL-3.0 | B（4/6） | [中](categories/object-storage/garage.zh.md) · [EN](categories/object-storage/garage.md) |
| **SeaweedFS** | 真正的约束是对象数量——十亿级小文件——且你想要一个 `weed` 二进制同时提供 S3、文件系统与表层、靠加卷服务扩容量时用它。 | Apache-2.0 | B（5/6） | [中](categories/object-storage/seaweedfs.zh.md) · [EN](categories/object-storage/seaweedfs.md) |
| **Ceph** | 你需要基金会治理的同一平台提供对象、块与文件、且养得起一个真正的存储集群时用它——只需要一个 S3 桶时属于过量的工具。 | LGPL-2.1 | A（3/6） | [中](categories/object-storage/ceph.zh.md) · [EN](categories/object-storage/ceph.md) |

### desktop-automation

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **PyAutoGUI** | 当你要在 Windows／macOS／Linux 上脚本化操控没有 API 的桌面应用时用它——但基于坐标和像素的自动化会因分辨率、DPI 或主题变化静默失效，且自 2024 年起已停滞维护。 | BSD-3-Clause | C（4/6） | [中](categories/desktop-automation/pyautogui.zh.md) · [EN](categories/desktop-automation/pyautogui.md) |

### game-dev

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **pygame** | 当你想学做或交付一个带简单游戏循环的小型 2D Python 游戏时用它——但做 3D 或性能敏感的项目它会成瓶颈，请另寻它路。 | LGPL-2.1 | D（6/6） | [中](categories/game-dev/pygame.zh.md) · [EN](categories/game-dev/pygame.md) |

### kafka-tools

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **UI for Apache Kafka (provectus/kafka-ui)** | 当你想用一条 docker run 起一个浏览 Kafka broker、topic 和消费组 lag 的 Web 面板时用它——但 provectus 上游已停摆（末次发布 2024-04），应改用仍在维护的 kafbat/kafka-ui 分叉。 | Apache-2.0 | D（3/6） | [中](categories/kafka-tools/kafka-ui.zh.md) · [EN](categories/kafka-tools/kafka-ui.md) |
| **kafka-python** | 当你想要一个纯 Python、pip install 即装、无需编译 librdkafka 的 Kafka 客户端时用它——但纯 Python 客户端的吞吐追不上 confluent-kafka，且对最新 broker 特性可能滞后支持。 | Apache-2.0 | A（6/6） | [中](categories/kafka-tools/kafka-python.zh.md) · [EN](categories/kafka-tools/kafka-python.md) |

### networking

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Paramiko** | 当 Python 代码需要以编程方式建立 SSH／SFTP 连接并执行远程命令时用它——但它是纯 Python（比 OpenSSH 慢）、仅支持线程模型，且采用 LGPL-2.1 许可。 | LGPL-2.1 | B（6/6） | [中](categories/networking/paramiko.zh.md) · [EN](categories/networking/paramiko.md) |
| **sshtunnel** | 当 Python 脚本需要以上下文管理器方式打通到堡垒机后服务的 SSH 端口转发时用它——但它无自动重连，且活跃度低（0.4.0，2021 年）。 | MIT | B（5/6） | [中](categories/networking/sshtunnel.zh.md) · [EN](categories/networking/sshtunnel.md) |
| **dnspython** | 当 Python 需要查询任意记录类型、自定义解析器、区域传输、DNSSEC 或 DoH／DoT 时用它——但它绕过 /etc/hosts 与系统解析器，要求 Python 3.10+，且是库而非命令行工具。 | ISC | B（5/6） | [中](categories/networking/dnspython.zh.md) · [EN](categories/networking/dnspython.md) |
| **wondershaper** | 当某块 Linux 网卡需要快速设置上／下行带宽上限、又不想手写 tc 规则时用它——但它基于老式 HTB（不像 cake／fq_codel 那样应对 bufferbloat），仅限 Linux，自 2024 年 7 月起停滞。 | GPL-2.0 | D（4/6） | [中](categories/networking/wondershaper.zh.md) · [EN](categories/networking/wondershaper.md) |
| **ThriftPy** | 仅当你要在迁移前读懂仍在 import thriftpy 的遗留服务时用它——该仓库已归档且废弃，所有新的 Thrift 开发都应转向仍在维护的 thriftpy2。 | MIT | B（5/6） | [中](categories/networking/thriftpy.zh.md) · [EN](categories/networking/thriftpy.md) |

### nginx-modules

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **lua-nginx-module (ngx_lua)** | 当你需要在 NGINX 上用 LuaJIT cosocket 实现真正的逐请求可编程能力（鉴权、路由、限流）时用它——但一次阻塞调用就会卡死整个 worker，且你被绑定在 OpenResty 版本耦合、核心团队高度集中的生态上。 | BSD-2-Clause | D（5/6） | [中](categories/nginx-modules/lua-nginx-module.zh.md) · [EN](categories/nginx-modules/lua-nginx-module.md) |
| **lua-resty-redis** | 当你的 OpenResty 边缘逻辑要在请求热路径上非阻塞访问 Redis（带连接池和 pipeline）时用它——但它只能在 ngx_lua 内运行，且不内置 Redis Cluster 的槽位路由。 | BSD-2-Clause | D（4/6） | [中](categories/nginx-modules/lua-resty-redis.zh.md) · [EN](categories/nginx-modules/lua-resty-redis.md) |
| **nginx-upload-module** | 当你想让 NGINX 把大文件 multipart 上传直接落盘、只把文件元数据交给后端时用它——但你在编译一个老化、单人维护的 C 分叉（末次提交 2024-07），如今直传 S3 预签名上传往往更优。 | BSD-3-Clause | "?"（2/6） | [中](categories/nginx-modules/nginx-upload-module.zh.md) · [EN](categories/nginx-modules/nginx-upload-module.md) |
| **tusd** | 当你需要一个基于协议的稳健断点续传上传服务器，能把文件流式写到本地磁盘或云存储时用它——但它是独立服务，不是 NGINX 模块，对小文件/可靠网络可能过度设计。 | MIT | A（5/6） | [中](categories/nginx-modules/tusd.zh.md) · [EN](categories/nginx-modules/tusd.md) |

### python-tooling

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Cython** | 当你已 profile 出的 Python 热点循环需要逼近 C 的速度、或要封装 C／C++ 库时用它——但它会引入 C 编译器和按平台构建 wheel 的流水线负担。 | Apache-2.0 | A（6/6） | [中](categories/python-tooling/cython.zh.md) · [EN](categories/python-tooling/cython.md) |
| **pyrasite** | 当你必须向一个无法重启、卡死或泄漏的运行中 Python 进程注入诊断代码时用它——但注入可能让目标崩溃，只当救火工具用。 | GPL-3.0 | C（4/6） | [中](categories/python-tooling/pyrasite.zh.md) · [EN](categories/python-tooling/pyrasite.md) |
| **gophernotes** | 当你想在 Jupyter 笔记本里用交互式 Go 单元做探索或教程时用它——但它自 2023 年起停滞，且跑的是解释器而非标准 Go。 | MIT | D（3/6） | [中](categories/python-tooling/gophernotes.zh.md) · [EN](categories/python-tooling/gophernotes.md) |
| **GRequests** | 当你想用 `map()` 以最小改动让现有同步 `requests` 代码并发时用它——但 gevent 会猴补丁标准库，可能与你的技术栈冲突。 | BSD-2-Clause | C（4/6） | [中](categories/python-tooling/grequests.zh.md) · [EN](categories/python-tooling/grequests.md) |
| **memory-analyzer** | 当你需要经 GDB 对一个活的 Python 3 进程做一次性按类型内存快照时用它——但 Meta 已归档它（代码停在 2021，目标是 EOL 的 3.6／3.7），优先选 memray／tracemalloc 这类有维护的工具。 | MIT | D（5/6） | [中](categories/python-tooling/memory-analyzer.zh.md) · [EN](categories/python-tooling/memory-analyzer.md) |
| **uv** | 用 Rust 编写的极速 Python 包与项目管理器，以单一工具和通用锁文件替代 pip、poetry 和 pyenv——但仅约 3 年历史，部分边缘情况仍在解决。 | Apache-2.0 | A（6/6） | [中](categories/python-tooling/uv.zh.md) · [EN](categories/python-tooling/uv.md) |
| **curl_cffi** | 当 Python 客户端被 TLS／JA3 指纹识别拦下、而你需要一个能伪装真实浏览器的 `requests` 风格 API 时用它——但它随包带原生 libcurl，并非纯 Python。 | MIT | A（6/6） | [中](categories/python-tooling/curl-cffi.zh.md) · [EN](categories/python-tooling/curl-cffi.md) |

### reading-tools

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Read Frog** | 当你想要功能丰富的开源沉浸式／双语翻译扩展，且需要 BYOK AI provider、本地 Ollama／自定义端点、TTS 和 YouTube 字幕翻译时用它。 | GPL-3.0 | B（6/6） | [中](categories/reading-tools/read-frog.zh.md) · [EN](categories/reading-tools/read-frog.md) |
| **FluentRead** | 当你想要中文优先、支持许多引擎的开源沉浸式翻译浏览器扩展，带双语／全文翻译和 Ollama／自定义 OpenAI-compatible 设置时用它。 | GPL-3.0 | C（6/6） | [中](categories/reading-tools/fluentread.zh.md) · [EN](categories/reading-tools/fluentread.md) |
| **Margin Read** | 当 MIT 许可、明确 BYOK／本地端点支持和写清楚的隐私 threat model 比功能完整度更重要时用它。 | MIT | C（5/6） | [中](categories/reading-tools/margin-read.zh.md) · [EN](categories/reading-tools/margin-read.md) |
| **Pair Translate** | 当你想要更轻量的双语网页翻译器，支持 direct provider requests、LLM 模板和 Chrome／Firefox／Edge 分发时用它。 | GPL-3.0 | C（5/6） | [中](categories/reading-tools/pair-translate.zh.md) · [EN](categories/reading-tools/pair-translate.md) |
| **NetNewsWire** | 当你在 Mac／iPhone 上读大量订阅、想要一个快速无广告、数据自己掌控的原生 RSS 客户端时用它——但它仅限 Apple 平台，别处一概不支持。 | MIT | B（5/6） | [中](categories/reading-tools/netnewswire.zh.md) · [EN](categories/reading-tools/netnewswire.md) |
| **Just Read** | 当你想在浏览器里按自己的方式清掉文章的广告与杂乱、还能按站点记忆选择器时用它——但它是 EULA 授权的源码，并非真正的开源。 | Unlicensed (EULA) | D（6/6） | [中](categories/reading-tools/just-read.zh.md) · [EN](categories/reading-tools/just-read.md) |
| **FreshRSS** | A free, self-hostable news aggregator… | AGPL-3.0 | B（5/6） | [EN](categories/reading-tools/freshrss.md) · [中](categories/reading-tools/freshrss.zh.md) |
| **Bilingual Book Maker** | 用 AI 翻译把 epub/txt/md/srt/pdf 做成双语对照书的 Python CLI，支持多家 LLM/MT 后端、断点续跑，有 PyPI 包。 | MIT | A（5/6） | [中](categories/reading-tools/bilingual-book-maker.zh.md) · [EN](categories/reading-tools/bilingual-book-maker.md) |

### speech

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **SpeechBrain** | 当你需要在一套统一的 PyTorch recipe 代码库上训练和适配语音模型（ASR、说话人识别、语音分离）时用它——但它以研究和训练为先，生产部署和跨版本 API 稳定性得你自己负责。 | Apache-2.0 | A（4/6） | [中](categories/speech/speechbrain.zh.md) · [EN](categories/speech/speechbrain.md) |
| **Voicebox** | 当你想要一个自托管的语音 I/O 工作室——克隆音色 TTS、热键 Whisper 听写、MCP/REST 让 agent 发声三合一，且是 MIT——时用它；但它是年轻的单人项目，发布节奏已停滞、自动粘贴目前仅 macOS。 | MIT | B（5/6） | [中](categories/speech/voicebox.zh.md) · [EN](categories/speech/voicebox.md) |
| **GPT-SoVITS** | 想要带 WebUI、且有训练路径可继续提升相似度的本地小样本声音克隆时用它；但它只管 TTS，听写、效果、agent 发声都不在其范围，且版本发布稀疏。 | MIT | A（5/6） | [中](categories/speech/gpt-sovits.zh.md) · [EN](categories/speech/gpt-sovits.md) |
| **Coqui TTS（idiap 分支）** | 想要带 XTTS v2 克隆与广泛预训练模型覆盖的 Python TTS 库时用它；但它是 MPL-2.0、不提供应用外壳，且是一家已倒闭公司项目的社区分支。 | MPL-2.0 | C（3/6） | [中](categories/speech/coqui-ai-tts.zh.md) · [EN](categories/speech/coqui-ai-tts.md) |

### terminal-ui

| 项目 | 何时用 | 许可 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **colorama** | 当 Python 命令行需要在旧版 Windows 控制台也能正确显示 ANSI 彩色输出时用它——但它只是颜色／样式适配层（不提供表格、TUI 或真彩保证），在现代终端上基本是空操作。 | BSD-3-Clause | B（5/6） | [中](categories/terminal-ui/colorama.zh.md) · [EN](categories/terminal-ui/colorama.md) |
| **asciimatics** | 当你需要在 Linux／macOS／Windows 上跨平台构建全屏 Python TUI 并附带 ASCII 动画引擎时用它——但它的控件较简陋、API 偏旧式，且为单人维护。 | Apache-2.0 | C（4/6） | [中](categories/terminal-ui/asciimatics.zh.md) · [EN](categories/terminal-ui/asciimatics.md) |
| **Terminal Markdown Viewer (mdv)** | 当你想在 SSH 下的纯终端里一次性、只读地渲染带彩色与语法高亮的 Markdown 时用它——但它活跃度低（0.x，2024 年 5 月），glow／mdcat 已是更现代的默认选择。 | BSD-3-Clause | "?"（2/6） | [中](categories/terminal-ui/terminal-markdown-viewer.zh.md) · [EN](categories/terminal-ui/terminal-markdown-viewer.md) |
| **ART** | 当 Python 命令行需要纯 Python 的 figlet 风格 ASCII 文字横幅、且不依赖系统二进制时用它——但它只做文字转艺术字（不做图片转 ASCII），也不与 figlet 字体完全一致。 | MIT | C（4/6） | [中](categories/terminal-ui/art.zh.md) · [EN](categories/terminal-ui/art.md) |
| **asciify** | 当你只想要一份极简易读、可复制粘贴的图片转 ASCII 算法参考时用它——但它没有任何许可证（默认保留所有权利），自 2022 年起无人维护，切勿将其并入产品。 | NONE | E（4/6） | [中](categories/terminal-ui/asciify.zh.md) · [EN](categories/terminal-ui/asciify.md) |
| **Warp** | 带命令块和集成编码 agent 的现代 AI 终端——但 GitHub 仓库仅用于 issue，产品是专有闭源软件。 | AGPL-3.0 | B（6/6） | [中](categories/terminal-ui/warp.zh.md) · [EN](categories/terminal-ui/warp.md) |
| **Alacritty** | 快速、GPU 加速的 OpenGL 终端模拟器，具备合理的默认设置；设计上不支持标签页、分屏和连字——复用请配合 tmux。 | Apache-2.0 | A（6/6） | [中](categories/terminal-ui/alacritty.zh.md) · [EN](categories/terminal-ui/alacritty.md) |

分类顺序见 [INDEX.zh.md](INDEX.zh.md)。
| **Readability.js** | 当你需要用 Firefox 阅读视图那套久经考验的引擎，把网页剥离成纯文章（标题、作者、正文）时用它——但它只解析你传入的 DOM，不会抓取 URL，也不会渲染重 JS 的 SPA。 | Apache-2.0 | [中](categories/web-scraping/article-extraction/readability-js.zh.md) · [EN](categories/web-scraping/article-extraction/readability-js.md) |
| **python-readability** | 当你的 Python 流水线需要从已抓取的 HTML 中用 lxml 快速抽取正文、不依赖浏览器或 Node 时用它——但它单人维护、更新缓慢，而 trafilatura 在抽取基准上往往得分更高。 | Apache-2.0 | [中](categories/web-scraping/article-extraction/python-readability.zh.md) · [EN](categories/web-scraping/article-extraction/python-readability.md) |
| **dragnet** | 当你有标注数据、想要一个可训练、还能把正文与用户评论分离的 ML 抽取器时用它——但它近乎停滞，依赖锁死老旧（scikit-learn<0.21、ftfy<5），在现代技术栈上安装会很痛苦。 | MIT | [中](categories/web-scraping/article-extraction/dragnet.zh.md) · [EN](categories/web-scraping/article-extraction/dragnet.md) |
| **boilerpipe** | 当你确实需要一个 JVM 原生、依赖轻量、基于经典算法的正文抽取器时用它——但仓库实际上已废弃（末次提交 2018-01），内置依赖陈旧，且不会再有安全修复。 | Apache-2.0 | [中](categories/web-scraping/article-extraction/boilerpipe.zh.md) · [EN](categories/web-scraping/article-extraction/boilerpipe.md) |
| **fuck-login** | 当你想读 2016 年代「如何脚本化登录（CSRF／RSA／验证码）」的示例代码时用它——但它自 2018 年起已废弃、无许可证，脚本如今基本失效。 | NONE | [中](categories/web-scraping/crawling-tools/fuck-login.zh.md) · [EN](categories/web-scraping/crawling-tools/fuck-login.md) |
| **gopup** | 当你想一行代码把中国公开数据（搜索指数、CPI、Shibor）拉进 pandas DataFrame 做学术研究时用它——但它自 2023 年起停更、无许可证，源站一变接口就失效。 | NONE | [中](categories/web-scraping/crawling-tools/gopup.zh.md) · [EN](categories/web-scraping/crawling-tools/gopup.md) |
| **PRAW** | 当你的数据源就是 Reddit、想走官方 OAuth 合规路径并自带限速处理时用它——但真正的边界是 Reddit 自家的 API 条款、配额与定价，而非这个库。 | BSD-2-Clause | [中](categories/web-scraping/crawling-tools/praw.zh.md) · [EN](categories/web-scraping/crawling-tools/praw.md) |
| **Scrapyd** | 当你需要把本地 Scrapy 爬虫部署到服务器、通过 HTTP API 做定时与多版本调度时用它——但它只能跑 Scrapy 且默认无鉴权，暴露 6800 端口前务必先加认证。 | BSD-3-Clause | [中](categories/web-scraping/crawling-tools/scrapyd.zh.md) · [EN](categories/web-scraping/crawling-tools/scrapyd.md) |
| **SpiderKeeper** | 当运行 Scrapyd 的小团队想要最简单的浏览器面板来部署和定时调度爬虫时用它——但它自 2023 年已停更且默认 admin/admin 鉴权，切勿暴露在不可信网络。 | MIT | [中](categories/web-scraping/crawling-tools/spiderkeeper.zh.md) · [EN](categories/web-scraping/crawling-tools/spiderkeeper.md) |
## 为什么做这个

多数开源 README 是营销：讲它能干啥、为啥好，却**不**告诉你何时*不该*用、和替代怎么比、运维成本多少。
做选型的 agent 恰恰需要这片「负空间」。oss-atlas 把 README 这个体裁反转成**决策支持**体裁。

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
| **Rich** | Rich is a Python library for rich text and beautiful formatting in the terminal. | MIT | ?（0/6） | [EN](categories/terminal-ui/rich.md) · [中](categories/terminal-ui/rich.zh.md) |
| **Textual** | The lean application framework for Python.  Build sophisticated user interfaces with a simple Python API. Run your apps in the terminal and a web browser. | MIT | ?（0/6） | [EN](categories/terminal-ui/textual.md) · [中](categories/terminal-ui/textual.zh.md) |

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
| **OpenBB** | Open Data Platform for analysts, quants and AI agents. | NOASSERTION | A（5/6） | [中](categories/investment-finance/openbb.zh.md) · [EN](categories/investment-finance/openbb.md) |
| **FinRL** | FinRL®:  Financial Reinforcement Learning. 🔥 | NOASSERTION | B（5/6） | [中](categories/investment-finance/finrl.zh.md) · [EN](categories/investment-finance/finrl.md) |
| **qlib** | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://github.com/microsoft/RD-Agent to automate R&D process. | NOASSERTION | B（5/6） | [中](categories/investment-finance/qlib.zh.md) · [EN](categories/investment-finance/qlib.md) |
| **backtrader** | Python Backtesting library for trading strategies | NOASSERTION | D（4/6） | [中](categories/investment-finance/backtrader.zh.md) · [EN](categories/investment-finance/backtrader.md) |
| **yfinance** | Download market data from Yahoo! Finance's API | NOASSERTION | A（6/6） | [中](categories/investment-finance/yfinance.zh.md) · [EN](categories/investment-finance/yfinance.md) |

### education-tutoring

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **DeepTutor** | DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/. | NOASSERTION | B（5/6） | [中](categories/education-tutoring/deeptutor.zh.md) · [EN](categories/education-tutoring/deeptutor.md) |

### agent-governance

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **agent-governance-toolkit** | Microsoft 面向生产 AI agent 的 public-preview 治理工具包：策略门控 tool call、身份 / 信任、审计 / 合规、MCP security gateway、SRE 控制，以及围绕 agent framework 的多语言 SDK。 | MIT | B（6/6） | [中](categories/agent-governance/agent-governance-toolkit.zh.md) · [EN](categories/agent-governance/agent-governance-toolkit.md) |
| **SkillSpector** | NVIDIA 的 AI agent skill 安全扫描器：安装前通过 CLI/MCP 检查 prompt injection、外传、危险脚本、MCP poisoning、依赖，并输出 SARIF/JSON 证据。 | Apache-2.0 | B（6/6） | [中](categories/agent-governance/skillspector.zh.md) · [EN](categories/agent-governance/skillspector.md) |
### social-simulation

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **MiroFish** | 打包好的「上传→模拟→报告」群体智能预测应用：喂一份文档，拿回预测报告和可交互的模拟世界。 | AGPL-3.0 | C（5/6） | [中](categories/social-simulation/mirofish.zh.md) · [EN](categories/social-simulation/mirofish.md) |
| **OASIS** | CAMEL-AI 出品的 pip 可装社交媒体模拟框架（类 Twitter/Reddit，号称最高百万 agent），用代码研究信息传播与极化。 | Apache-2.0 | B（6/6） | [中](categories/social-simulation/oasis.zh.md) · [EN](categories/social-simulation/oasis.md) |
| **AgentSociety** | 清华 FIB Lab 的 LLM 原生社会科学模拟平台：Ray 分布式、实验回放、DuckDB 追踪。 | Apache-2.0 | B（6/6） | [中](categories/social-simulation/agentsociety.zh.md) · [EN](categories/social-simulation/agentsociety.md) |
| **generative_agents** | 2023 年斯坦福「Smallville」原版研究原型（memory stream / reflection / planning）——学开创性架构用，别在上面盖楼。 | Apache-2.0 | D（3/6） | [中](categories/social-simulation/generative-agents.zh.md) · [EN](categories/social-simulation/generative-agents.md) |

### osint

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **holehe** | 通过注册/找回密码端点探测一个邮箱在 120+ 站点是否有账号（不提醒目标）——2024-09 起停止维护，应吸收其方法论与模块表，或 fork 后逐模块复验。 | GPL-3.0 | D（5/6） | [中](categories/osint/holehe.zh.md) · [EN](categories/osint/holehe.md) |
| **socialscan** | 直接查询平台注册端点，拿到干净的邮箱/用户名「可用或已占用」判定——只覆盖约 11 个平台，发版零星。 | MPL-2.0 | D（4/6） | [中](categories/osint/socialscan.zh.md) · [EN](categories/osint/socialscan.md) |
| **Maigret** | 跨 3000+ 站点建立用户名档案：ID 提取、递归搜索、HTML/PDF/XMind 报告——本类目维护最活跃的选择。 | MIT | B（6/6） | [中](categories/osint/maigret.zh.md) · [EN](categories/osint/maigret.md) |
| **Sherlock** | 在 480+ 社交网络做简单、久经考验的用户名存在性核查，组织治理、社区庞大——个人页信号较粗，不做档案提取。 | MIT | A（6/6） | [中](categories/osint/sherlock.zh.md) · [EN](categories/osint/sherlock.md) |
| **GHunt** | 用你自己的 Google 会话对 Google 账户做认证式深挖 OSINT（Gmail→资料、Gaia ID、Drive、BSSID）——能力强，AGPL-3.0，ToS/法律风险最高。 | AGPL-3.0 | B（5/6） | [中](categories/osint/ghunt.zh.md) · [EN](categories/osint/ghunt.md) |

### knowledge-base

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **LLM Wiki** | 当你希望自己的文档被一次性编译成一份本地互链维基、由 LLM 持续保鲜，而不是每次查询都用 RAG 重新推导时用它。 | GPL-3.0 | B（4/6） | [中](categories/knowledge-base/llm-wiki.zh.md) · [EN](categories/knowledge-base/llm-wiki.md) |
| **Logseq** | 当你想要一个本地优先、由你自己撰写并用 Datalog 查询的大纲笔记工具、且 LLM 能力交给插件时用它。 | AGPL-3.0 | B（5/6） | [中](categories/knowledge-base/logseq.zh.md) · [EN](categories/knowledge-base/logseq.md) |
| **SiYuan** | 当你想要一个自托管、块级引用的知识工作空间、让人与 AI 智能体共同编辑时用它——但部分功能需付费（open-core）。 | AGPL-3.0 | B（5/6） | [中](categories/knowledge-base/siyuan.zh.md) · [EN](categories/knowledge-base/siyuan.md) |
| **Khoj** | 当你想要一个可自托管的 AI 第二大脑、从你的文档与网络取答案、并覆盖浏览器／桌面／Obsidian、模型可选本地或在线时用它。 | AGPL-3.0 | C（6/6） | [中](categories/knowledge-base/khoj.zh.md) · [EN](categories/knowledge-base/khoj.md) |
| **Reor** | 当你需要一份「本地优先 AI 笔记」的模式参考时用它；它已归档（2025-05），不要把生产押在它上面。 | AGPL-3.0 | E（4/6） | [中](categories/knowledge-base/reor.zh.md) · [EN](categories/knowledge-base/reor.md) |
| **OpenKB** | 当你希望长文档被 LLM 一次性编译成一份可持久、互相链接的 Markdown 维基、之后再对这份维基提问时用它——无头 CLI，不需要向量库。 | Apache-2.0 | B（6/6） | [中](categories/knowledge-base/openkb.zh.md) · [EN](categories/knowledge-base/openkb.md) |

### peripherals

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **OpenLogi** | 当你想要 Options+ 那套功能——按应用 profile、手势、键盘重映射、静态 RGB、摄像头控制——在 macOS、Linux、Windows 上用同一份 TOML 配置拿到，并且能接受一个尚未 1.0、只有几个月历史、没有接收器配对的项目时用它。 | MIT OR Apache-2.0 | C（5/6） | [中](categories/peripherals/openlogi.zh.md) · [EN](categories/peripherals/openlogi.md) |
| **Solaar** | 在 Linux 上当任务本身是设备管理而不是重映射时用它：配对与解绑接收器、读取电量与设备状态、修改 HID++ 设置——背后是 14 年仍在发版的记录；代价是仅限 Linux，且没有摄像头与 RGB。 | GPL-2.0-or-later | B（6/6） | [中](categories/peripherals/solaar.zh.md) · [EN](categories/peripherals/solaar.md) |
| **Mouser** | 当你想要在 Windows／macOS／Linux 上用便携压缩包按应用重映射罗技 HID++ 鼠标，不需要安装器、账号或服务，并且不要求配对、键盘、摄像头或按设备映射时用它。 | MIT | B（5/6） | [中](categories/peripherals/mouser.zh.md) · [EN](categories/peripherals/mouser.md) |
| **logiops** | 在 Linux 上，当你想要一个读单份声明式 `/etc/logid.cfg` 的 root systemd 守护进程而不是 GUI 时用它——接受只支持 HID++ 2.0+ 鼠标、没有应用感知，且开发自 2024 年起实际已停。 | GPL-3.0-or-later | C（4/6） | [中](categories/peripherals/logiops.zh.md) · [EN](categories/peripherals/logiops.md) |

### decision-models

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Kev** | 当你想要一个自托管、可微调的模型，对一段文本回答带类型的问题（是/否、多选、评分）并给出可用的校准概率时用它——不是托管判定 API，也不是从零训一个分类器。 | Apache-2.0 | C（4/6） | [中](categories/decision-models/kev.zh.md) · [EN](categories/decision-models/kev.md) |
| **Simple Jev** | 当你已经在服务一个开源聊天模型、想要 Jev 那套带类型判定接口时用它——一段共享上下文加一组带类型问题进去，概率分布出来，不用解析生成的 JSON；代价是继承底座的判断力与未校准的置信度。 | Apache-2.0 | C（4/6） | [中](categories/decision-models/simple-jev.zh.md) · [EN](categories/decision-models/simple-jev.md) |

### optimization-solvers

| 项目 | 何时用 | 许可证 | 健康度 | 页面 |
| --- | --- | --- | --- | --- |
| **Rebalancer** | 当任务是「按这些策略在分片／主机量级重新安置这些对象」——容量、均衡、故障域打散、尽量少搬——而你宁愿声明具名 spec 加一个调好的局部搜索，也不想手写线性规划时用它。 | Apache-2.0 | B（5/6） | [中](categories/optimization-solvers/rebalancer.zh.md) · [EN](categories/optimization-solvers/rebalancer.md) |
