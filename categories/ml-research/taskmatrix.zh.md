---
name: TaskMatrix
slug: taskmatrix
repo: https://github.com/chenfei-wu/TaskMatrix
category: ml-research
tags: [visual-chatgpt, tool-routing, foundation-models, multimodal, agent, abandoned, historical-demo]
language: Python
license: MIT
maturity: "research demo (orig. 'Visual ChatGPT', Microsoft); last pushed 2024-01, no commits since — abandoned in practice (as of 2026-06)"
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2024-01-06T02:41:20Z
  default_branch: main
  default_branch_sha: 4b7664f8d3a23804ac1b795d75a73efd162769f0
  archived: false
health:
  schema: 1
  computed_at: 2026-09-19T08:53:27Z
  overall: "?"
  overall_score: null
  scored_axes: 2
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1100
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: E
      raw:
        repo_age_days: 1219
        last_commit_age_days: 1100
        cohort: app
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_traffic }
    adoption: { reason: no_package_structural }
    governance: { reason: unattributable }
    risk_license: { reason: license_unparsed }
---

# TaskMatrix

一个历史性的研究 demo（最初叫「Visual ChatGPT」，出自微软）：它把 ChatGPT 接到一组固定的视觉基础模型上，让你能用对话来给图片做描述、生成和编辑——作为早期「工具路由 agent」的设计样本很有意思，但自 2024 年初起已停更，并已被现代多模态大模型取代。

![taskmatrix — 健康度雷达](../../assets/health/taskmatrix.zh.svg)

## 何时使用

你是研究者或工程师，想搞清楚第一波 LLM「工具路由 agent」当年是怎么搭的，而且你想读一份具体、能跑的参考实现，而不是一篇论文。你用过 GPT-4o 或 Gemini，那里视觉是原生的；你好奇在多模态模型出现*之前*，人们是怎么把视觉硬接到一个纯文本 ChatGPT 上的：一个 prompt 驱动的路由器（即「Visual ChatGPT」范式）解析用户请求，决定调用约 20 个视觉基础模型里的哪一个（BLIP 描述、Stable Diffusion 文生图、ControlNet/Pix2Pix 编辑、分割、深度等等），把中间图片回填进对话状态，再围绕工具输出拼出一段自然语言回答。TaskMatrix 正是那套设计的干净样本——你读它（也许在一台 GPU 机器上跑起其中一部分）是为了理解那份 manager prompt、工具注册表和图片状态管线，而不是为了把它部署上线。

当你今天要搭*自己的*工具路由 agent、想看一个早期、自包含的「LLM 当编排器、调度重型专家模型」的例子时，它也是有用的教学参考——看看当年的 prompt 脚手架长什么样、它在哪里脆弱，以及为什么原生多模态模型最终把整套范式吸收掉了。

## 何时不用

- **任何你打算持续跑起来的场景。** 仓库自 **2024-01-06** 起再无 commit；它实际上已被废弃（GitHub 上没正式 `archived`，但功能上已死）。读它，别依赖它。
- **你想要一个当下可用的图片对话能力。** 现代多模态大模型（GPT-4o、Gemini、带视觉的 Claude、Qwen-VL）在单个模型里原生做描述 / VQA / 有据推理，不需要托管一整个基础模型动物园。TaskMatrix 存在的全部理由——纯文本 ChatGPT 看不见图——如今已不成立。
- **你想要一个受维护的 agent / 工具路由框架。** 今天的 agent 框架（LangChain、现代 function-calling、基于 MCP 的工具链）做编排远更好，且在持续维护。别在 TaskMatrix 那套定制 prompt 路由器上做新工作。
- **你没法 pin 住又老又重的依赖。** 它会拉进一套 2023 年前后钉死的栈（特定版本的 `transformers`、`diffusers`、`langchain`，Detectron/ControlNet 权重，外加一个 OpenAI key）到一个数 GB 的 GPU 环境里；这些版本已经过时，在当前 CUDA/PyTorch 上未必能干净解析或运行。[未验证]
- **安全 / 供应链敏感。** 停更两年多意味着没有任何补丁；钉死的老依赖会随时间累积已知 CVE。把它当作一次性研究代码，而不是能暴露在外或托付 secret 的东西。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| 现代多模态大模型（GPT-4o / Gemini / 带视觉的 Claude / Qwen-VL） | 未收录 | 需要单个持续维护的模型原生带视觉时，选现代多模态大模型。 | 单个模型原生带视觉——描述、VQA、生成 / 编辑由模型或其内建工具完成；无需托管基础模型动物园，且在持续维护。正是它取代了整套 TaskMatrix 范式。 |
| HuggingGPT / JARVIS | 未收录 | 需要同时代、同样“LLM 控制器调模型目录”思路时，选 HuggingGPT/JARVIS。 | 同时代、同思路——一个 LLM 控制器把任务路由到一批 Hugging Face 模型；任务面更广（不限视觉），同样是研究 demo 而非受维护的产品。 |
| LangChain agents | 未收录 | 需要受维护的通用 LLM 工具编排框架时，选 LangChain agents。 | 受维护的通用 LLM 工具编排框架；你用当下的 function-calling 自己接工具（包括视觉模型），而不是用 TaskMatrix 那套 2023 年手写的 prompt 路由器。 |
| 现代 agent 框架（function-calling / 基于 MCP 的工具链） | 未收录 | 需要当下标准化的 LLM 工具访问方式时，选现代 agent 框架。 | 当下给 LLM 配工具的标准化做法；编排、结构化工具 I/O 和活跃支持都远胜这个定制 demo。 |
| [autoresearch](autoresearch.zh.md) | ✅ | 需要另一个面向 agent 驱动 ML 训练循环的单作者研究 demo 时，选 autoresearch。 | 同样是单作者研究 demo 类 app，但它是个面向 agent 驱动 ML 研究的单卡*训练*循环——问题完全无关；只共享「当参考读、别部署」这个姿态。 |

## 技术栈

- **语言：** Python（仓库约 80%）。
- **控制器：** 一个 LLM（README 面向 OpenAI 的 ChatGPT/`gpt-3.5` 系列，经 OpenAI API 调用），被 prompt 成一个挑选并编排工具的 manager。建在 2023 年代的 LangChain agent 脚手架之上。
- **工具动物园：** 约 20 个作为工具加载的视觉基础模型——图像描述（BLIP）、文生图（Stable Diffusion）、指令 / 编辑与条件化（ControlNet、Pix2Pix）、分割、深度 / 边缘 / 姿态估计、VQA 等（确切集合随版本变化）。
- **机制：** prompt 驱动的路由器解析意图、派发给某个基础模型、把中间图片作为对话状态留存，再围绕输出组织出一段自然语言回复。

## 依赖

- **运行时：** Python 加一套重型 ML 栈——`torch`、`transformers`、`diffusers`、`langchain` 以及各模型专属库，版本钉在 2023 年前后。[未验证]
- **硬件：** 一块显存充裕的 CUDA GPU，以同时托管多个大型视觉模型；纯 CPU 跑生成 / 编辑类工具不现实。
- **外部服务：** 控制器 LLM 需要一个 OpenAI API key（联网 + 费用）。各视觉基础模型的权重需另行下载（数 GB）。
- **可复现性风险：** 因为依赖既老又未对齐当前版本，今天做一次干净安装可能无法解析或运行，需要手工做版本手术——动手前别假设它能跑起来。

## 运维难度

**高，而且不值得花。** 哪怕在 2023 年，这都不是个轻松的搭建：要备一块大显存 GPU、下载数 GB 模型权重、装一棵很深的 ML 依赖树，再配一个 OpenAI key。到了 2026 年，难度因年久而叠加——钉死的依赖版本早于当前 CUDA/PyTorch/`transformers`，所以光是把它启动起来就要预期依赖解析报错和打补丁，还没有维护者可以提 issue。它没有服务级部署方案（没有打包、版本或 CI 可依靠）；它从头到尾就是个 demo。在一台一次性机器上跑其中一部分来研读设计可以，但别把它当生产来运维。

## 健康度与可持续性

- **响应速度**：无法计算——no_data。
- **维护（截至 2026-06）：** 最后一次 push 在 **2024-01-06**，此后再无 commit——**实际上已废弃**（GitHub 上未正式 `archived`，但功能上已死）。[推断] 没有发布、没有修复、也没有维护者可提 issue。
- **治理 / bus factor：** 仓库挂在个人 `User` 账号（chenfei-wu）下，尽管这项工作最初源于微软研究院、名为「Visual ChatGPT」。[推断] 它曾有的机构背书如今已不复存在；当前仓库背后没有团队、也没有路线图。
- **年龄与 Lindy 判定（创建于 2023-03，约 3 年）：** 这是**Lindy 失败**的典型——老到*已经过时*却不再活跃。这里的年龄是负分而非加分：在一个快速演进的栈（CUDA/PyTorch/`transformers`/`diffusers`）面前放任不维护越久，干净安装能跑起来的概率就越低。把它当作多模态之前那个工具路由时代的历史样本来读，别押注于它。
- **风险标记：** 停更两年多 ⇒ 钉死的 2023 年代依赖在无补丁下累积已知 CVE——这是真实的供应链隐患；别把它暴露在外、也别托付 secret。许可为 MIT（已读文件核实），尽管 GitHub API 显示为 `NOASSERTION`。[未验证]

## 存疑（未验证）

- [未验证] 截至 2026-06，约 34.1k GitHub star（34,070），`pushed_at` 为 2024-01-06；star 不可靠且对日期敏感——仅作参考。
- **License：** 仓库的 `LICENSE.txt` 是一份 MIT License（Copyright 2023 Microsoft）——已通过读文件**核实**。注意 GitHub API 把 license 报告为 `NOASSERTION` /「Other」（没有 SPDX 自动匹配），所以某些工具可能显示为未授权；文件本身是 MIT。
- [推断] 该仓库在 GitHub 上**没有**被正式 `archived`，但自 2024-01-06 起再无 commit，实际上已被废弃——这里的「废弃」是从提交历史推断，而非项目声明的状态。
- [未验证] 确切的工具清单（约 20 个视觉基础模型）、控制器模型系列（`gpt-3.5` 时代）以及基于 LangChain 的脚手架，都是从 README 和项目历史转述的；确切集合与版本应在依赖前从当前代码树读取。
- [未验证] 在当前 CUDA/PyTorch 上的依赖陈旧 / 安装报错，是从 2024-01 的冻结和 2023 年代的版本钉死推断的，并非本页做过一次干净安装；若你确要运行，请用一次干净搭建来核实。
