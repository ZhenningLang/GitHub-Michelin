---
name: screenshot-to-code
slug: screenshot-to-code
repo: https://github.com/abi/screenshot-to-code
category: ai-design-generation
tags: [screenshot-to-code, ui-generation, vision-llm, html, tailwind, coding-agent, playwright, self-hosted]
language: Python
license: MIT
maturity: no tagged releases, active, 80.3k stars (as of 2026-10)
last_verified: 2026-10-15
type: app
homepage: https://screenshottocode.com
upstream:
  pushed_at: 2026-10-09T20:02:05Z
  default_branch: main
  default_branch_sha: a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc
  archived: false
health:
  schema: 1
  computed_at: 2026-10-13T05:20:40Z
  overall: B
  overall_score: 3.2
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 3
        active_weeks_13: 3
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 4.4
        qualifying_issues: 3
        band: relaxed_solo
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: B
      raw:
        repo_age_days: 1063
        last_commit_age_days: 3
        cohort: app
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.998
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    adoption: { reason: no_package_structural }
---

# screenshot-to-code

手里只有一张截图或一帧 Figma 设计稿，要把它变成前端代码，光是抠图、估间距就要耗掉一个下午。screenshot-to-code 让视觉模型把这一屏重写成一个 HTML 文件，从截图里把真实图片裁出来用，再自己渲染一遍和原图对照。

![screenshot-to-code — 健康度雷达](../../assets/health/screenshot-to-code.zh.svg)

## 何时使用

你是前端开发，或者一个人做原型的创业者。有人丢给你一张落地页的 PNG——竞品的定价页、设计师的稿子、一个找不到源码的老网站——说明天要一个“能跑的这个”。手工做，就得在修图软件里把 logo 抠出来，用眼睛判断卡片间距是 24px 还是 20px，再把每行文案重新敲一遍。直接丢给通用聊天模型，你会拿到一个意思差不多的页面，原本放图的地方全是 `https://via.placeholder.com/150` 占位框。

输入是像素、目标是尽快做出一个视觉上接近的复刻时，就该想到 screenshot-to-code。它和“把图贴进聊天框”的区别，是三件聊天框自己做不到的事：图片从你的截图里裁，不靠模型编；写完先在真浏览器里渲染、看一眼结果再交给你；一次并行跑四个模型版本，你挑最好的，不用反复重抽。要“照抄一个现成页面”而不是“按简报设计新页面”，选它而不是 [Open Design](open-design.zh.md)；想用自己的模型 key 自建部署、产物文件留在手里，选它而不是托管的 v0。

## 何时不用

- **代码要直接放进现有代码库。** 产出是一个自包含文件，Tailwind 从 `cdn.tailwindcss.com` 加载；选 React 时用 React UMD 包加浏览器内 Babel 编译——没有组件、没有构建步骤、没有设计 token。要让模型用你自己的组件目录拼界面，选 [json-render](json-render.zh.md)；或者在你的仓库里跑编码 agent，配 [Playwright MCP](../web-automation/playwright-family/playwright-mcp.zh.md) 做截图检查。这两条路都写进你真实的工程结构，而不是一次性原型。
- **需要可度量的像素级还原。** 没有相似度指标，也没有“够像就停”的规则（见快问快答）。改用 [Playwright](../web-automation/playwright-family/playwright.zh.md) 的截图比对当打分器，自己搭这个循环，因为数值差异能抓到模型目测放过的间距和字体错误。
- **要的是行为，不是外观。** 它只看得到像素，页面背后的数据、登录、路由、状态都不在输入里。录屏模式靠视频帧推测交互，而且只跑两个版本。改用编码 agent 配 [Playwright MCP](../web-automation/playwright-family/playwright-mcp.zh.md) 直接访问线上站点，因为它能看真实 DOM 和网络请求，不用从画面里猜。
- **你在设计新东西，不是照抄一个页面。** 它的提示词围绕“和提供的截图看起来完全一样”写成。改用 [Open Design](open-design.zh.md)，它按简报加一份 `DESIGN.md` 设计系统驱动你的编码 agent，还能出 deck、图片和视频。
- **付不起前沿模型 API，或者必须用本地模型。** 至少要一个 OpenAI、Anthropic 或 Gemini 的 key；素材裁剪和图片编辑“强烈推荐”再配 Gemini 和 Replicate；每个版本最多花 3 美元才会被中止，一张截图跑四个。README 说走 Ollama 的路线“因效果差不推荐”。如果模型必须是你自己的，改用 [Open Design](open-design.zh.md) 接一个兼容 OpenAI 接口的自带端点，但要接受它不是复刻工具。
- **一点运维都不想做。** 作者的托管产品（screenshottocode.com，后端是另一个闭源仓库）或 Vercel 的 v0 会替你跑——两者都不是仓库。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Open Design](open-design.zh.md) | ✅ | 按简报和设计系统生成新原型、deck 或视频，选 Open Design；任务是照着像素复刻一个现成页面，选 screenshot-to-code。 | Open Design 覆盖多种产物、复用你已装的编码 agent；screenshot-to-code 面窄，但有复刻专用的部件：从截图裁素材、四版本并行、自渲染检查。 |
| [Playwright MCP](../web-automation/playwright-family/playwright-mcp.zh.md) + 你的编码 agent | ✅ | 结果必须进你的仓库、想自己掌控循环，选编码 agent 配 Playwright MCP；想要一个现成的网页版复刻流水线，选 screenshot-to-code。 | 自己搭能产出真实组件、还能加数值比对，但素材裁剪和多版本得自己拼；screenshot-to-code 这些都现成，代价是只产 CDN 单文件。 |
| [json-render](json-render.zh.md) | ✅ | 要模型在你的应用里用现有组件目录拼界面，选 json-render；要把别人给的一屏单独复刻出来，选 screenshot-to-code。 | json-render 把模型关在你的设计系统里，不能自造标记；screenshot-to-code 为贴合像素随意造标记，对你的组件一无所知。 |
| v0（Vercel） | 非仓库 | 想要托管的、偏 React/shadcn 的生成器且自带部署、不需要自建，选 v0；想用自己的 key 自己跑，选 screenshot-to-code。 | v0 是闭源托管服务，绑定 Vercel 的技术栈和定价；screenshot-to-code 是 MIT、可自建，但要自己跑两个进程、自己付模型账单。 |
| Builder.io Visual Copilot | 非仓库 | 源头是 Figma 文件、要映射到你代码里的框架组件，选 Visual Copilot；手里只有一张截图，选 screenshot-to-code。 | 闭源商业 Figma 插件，读的是设计结构而不是像素；screenshot-to-code 任何图片都能用，但拿不到图层和 token 信息。 |

## 快问快答

**它怎么保证完美复刻？**
保证不了。截至提交 `a813977`（2026-10-09），后端里没有任何像素差、SSIM 或其他相似度打分。还原度靠四层叠加：提示词要求文字逐字照抄；图片从原图裁，不生成；模型渲染自己的页面，用眼睛和截图对比；四个版本并行，由人挑最像的。

**那实际上就是基于视觉的闭环？**
是，但是个弱闭环。判官是写代码的同一个模型，靠目测比两张图，它看不出的 4px 间距误差、字重偏差就会留下来。循环在三种情况下停：模型不再调用工具、跑满 30 步、这个版本花费超过 3 美元——从来不是“相似度达到某个值”。自检只是提示词里的一句要求，代码不强制；没装 Chromium 时，这个工具根本不会提供给模型。强闭环还要加一个机器打分层：把两张图对齐、算感知差异、把差得最多的区域画成热力图回传、达到阈值才停。这个仓库没有。

## 快速上手

它作为一个本地网页应用来用：在 `backend/.env`（或设置对话框）里填至少一个模型 key，启动 FastAPI 后端和 Vite 前端——或者一条 `docker-compose up -d --build`——然后打开 `http://localhost:5173`。输入有四种：上传一张或多张截图，或一段录屏；粘贴网址，由你提供的 ScreenshotOne key（一个付费截图 API）去截图，Figma 链接会被拒绝，要先把画板导出成图片；用文字描述页面；或者导入现有 HTML 接着改。你选输出技术栈，应用按你手里有哪些 key 决定跑哪些模型，四个版本（同一页面的不同方案）并排流式出来。之后就像聊天：直接打字提修改，或者切到选择模式点中某个元素，让修改只作用于它；每轮修改返回两个新版本。满意了就复制代码、在新标签页打开，或者点 Download Code 下载 ZIP——裁出的图片平时存在你的后端上，ZIP 会把它们一起打包。它替你做的：初稿、裁图、多个版本和定点修补。留给你的：模型 key 和账单、挑版本，以及把这个靠 CDN 加载的单文件移植进你的真实项目。它内部怎么逼近截图，见技术要点。

![screenshot-to-code — 主干用户故事](../../assets/flow/screenshot-to-code.zh.svg)

<!-- flow-steps:begin (generated from flows/screenshot-to-code.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：把模型 key 写进 backend/.env，启动后端和前端 — `poetry run uvicorn main:app --reload --port 7001 · pnpm dev`
2. **你**：上传截图或录屏，或粘贴网址，选好技术栈
3. **screenshot-to-code**：并排流式给出四个版本，用的是从原图裁出的真实图片 — 组件：`FastAPI 后端`
4. **你**：打字提修改，或在选择模式下点中元素限定范围
5. **screenshot-to-code**：只改你要求的部分，返回两个新版本
6. **你**：复制代码，或下载打包了图片的 ZIP

**价值**：拿到一份带真实图片、能直接打开、可对话修改的单文件复刻页——不用手工切图、手写布局

</details>
<!-- flow-steps:end -->

## 技术要点

![screenshot-to-code — 机制图](../../assets/mechanism/screenshot-to-code.zh.svg)

<!-- mechanism:begin (generated from mechanisms/screenshot-to-code.json by tools/mechanism_card.py; do not edit) -->
<details>
<summary>机制文字版</summary>

- 原始截图
- 截图初稿选择四个模型槽位④
- 每槽位独立的工具调用 agent
- Gemini 定位框换算后裁原图②
- 按需用 Replicate 生成替代图②
- HTML 状态：整页创建或精确替换①
- 可选 Chromium 桌面与手机截图③
- 供人挑选的方案；无机器评分④

- 原始截图 → 截图初稿选择四个模型槽位④
- 截图初稿选择四个模型槽位④ → 每槽位独立的工具调用 agent（并发任务）
- 原始截图 → Gemini 定位框换算后裁原图②（请求裁图时）〔可选／兜底〕
- Gemini 定位框换算后裁原图② → 每槽位独立的工具调用 agent（裁图 URL 与预览）〔可选／兜底〕
- 每槽位独立的工具调用 agent → 按需用 Replicate 生成替代图②〔可选／兜底〕
- 按需用 Replicate 生成替代图② → 每槽位独立的工具调用 agent（图片 URL）〔可选／兜底〕
- 每槽位独立的工具调用 agent → HTML 状态：整页创建或精确替换①（工具结果进入下一模型轮次）
- HTML 状态：整页创建或精确替换① → 可选 Chromium 桌面与手机截图③〔可选／兜底〕
- 可选 Chromium 桌面与手机截图③ → 每槽位独立的工具调用 agent（同一模型目测后可修补）〔可选／兜底〕
- HTML 状态：整页创建或精确替换① → 供人挑选的方案；无机器评分④（各版本输出）

</details>
<!-- mechanism:end -->

### 1. 用工具补丁修改，不反复重写整页

- **解决：** 为了修一个间距重写整页，容易连已经对齐的部分一起改坏。
- **做法：** 提示词要求先用一次 `create_file` 写完整 HTML，再用 `edit_file` 精确替换旧文字；匹配不到就向模型报错。agent（会选择并执行工具的模型）把工具结果送入下一轮。
- **边界：** 精确匹配只约束补丁如何应用，不保证改得对或改得少；运行时不禁止再次调用 `create_file`，“只写一次”是指令，不是硬保证。
- **源码：** [工具指令第 15–19 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/prompts/system_prompt.py#L15-L19)、[创建与替换第 101–257 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/agent/tools/runtime.py#L101-L257)、[工具结果循环第 278–325 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/agent/engine.py#L278-L325)。

### 2. 先裁原图素材，再按需生成替代图

- **解决：** 模型编出的 logo 或照片，会让布局已接近的复刻仍显得不像。
- **做法：** Gemini 用四个数标出素材的矩形位置，坐标统一缩放到 0–1000，后端换算成像素后裁原图。遇到被遮挡的照片、无法单独裁出的背景，提示词要求 agent 调用 Replicate（托管图像生成模型的服务）生成替代图。
- **边界：** 这是模型选择的工具路径，不是裁图失败就自动生成；裁图需要 Gemini 和可用静态图，生成图片则要功能已启用且有 Replicate key。
- **源码：** [素材指令第 21–25 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/prompts/system_prompt.py#L21-L25)、[坐标换算与裁图第 293–343 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/asset_extraction.py#L293-L343)、[Replicate 生成第 259–294 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/agent/tools/runtime.py#L259-L294)、[裁图可用条件第 336–351 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/agent/engine.py#L336-L351)。

### 3. 把浏览器实渲染结果交回同一模型目测

- **解决：** HTML 读起来合理，真正渲染时仍可能布局错乱、间距不对。
- **做法：** 模型若调用 `screenshot_preview`，无头 Chromium（没有窗口的真浏览器）就按桌面和手机两种宽度渲染当前 HTML。两张完整页面截图交回同一模型，提示词要求它检查并修补可见错误。
- **边界：** Chromium 不可用时不提供预览工具，循环也不强制调用或计算相似度分数；停止看模型是否结束、是否到 30 轮或触及有定价模型的预算，不看质量阈值。
- **源码：** [预览返回第 10–99 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/agent/tools/screenshot_preview.py#L10-L99)、[Chromium 渲染第 30–88 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/preview_screenshot/playwright_backend.py#L30-L88)、[工具可用条件第 25–39 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/agent/providers/factory.py#L25-L39)、[预览指令第 19 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/prompts/system_prompt.py#L19-L19)、[循环停止条件第 218–276 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/agent/engine.py#L218-L276)。

### 4. 并行跑独立版本，不只押一个初稿

- **解决：** 同一个模型自检时，可能继续看不出自己初稿里的视觉偏差。
- **做法：** 截图初稿从有 key 的厂商中选出四个模型槽位（四份独立生成任务），每个槽位启动一个 agent 任务并发生成。最后由用户挑方案，不是机器按分数选冠军。
- **边界：** 可用模型少时，多个槽位会重复同一模型；修改和录屏只跑两个版本，不是四个。备选多不等于像素级还原已获证明。
- **源码：** [四槽位默认值第 3–4 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/config.py#L3-L4)、[选择与模式边界第 417–499 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/routes/generate_code.py#L417-L499)、[并发任务第 589–611 行](https://github.com/abi/screenshot-to-code/blob/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc/backend/routes/generate_code.py#L589-L611)。

## 技术栈

- **后端：** Python ≥ 3.10，FastAPI + uvicorn，生成过程走 WebSocket 流式推送；Poetry 管依赖。模型 SDK 为 `openai` 2.16.0、`anthropic` ^0.84、`google-genai`；预览工具用 `playwright`；裁图用 Pillow + `pillow-heif`；视频输入用 `moviepy`；ZIP 导出用 BeautifulSoup。
- **agent 循环：** 一个与模型厂商无关的工具循环（`backend/agent/engine.py`），工具有 `create_file`、`edit_file`、`extract_assets`、`generate_images`、`edit_images`、`remove_backgrounds`、`screenshot_preview`、`save_assets`、`retrieve_option`。
- **前端：** React + Vite + TypeScript，Tailwind，Radix UI，CodeMirror 编辑器；pnpm。
- **产出技术栈：** HTML + Tailwind、HTML + CSS、React + Tailwind、Vue + Tailwind、Bootstrap、Ionic + Tailwind——都是靠 CDN 加载的单文件。

## 依赖

- **至少一个模型 key：** `OPENAI_API_KEY`、`ANTHROPIC_API_KEY` 或 `GEMINI_API_KEY`（写在 `backend/.env` 或设置对话框里）。素材裁剪和录屏模式需要 Gemini。
- **可选 `REPLICATE_API_KEY`**（只能写在 `backend/.env`），用于生成图片、编辑图片和去背景。
- **Chromium**：通过 `poetry run playwright install chromium` 安装，自检要用它；没装时这个工具会被悄悄去掉。
- **Node + pnpm** 跑前端，或者用 Docker Compose 一起跑两个服务。
- 裁出的素材存在 `backend/local_assets`，由后端在 `/local-assets` 下提供；应用内预览依赖后端在跑，ZIP 导出会把它们打包进去。

## 运维难度

**低到中。** 两个进程（FastAPI 在 7001，Vite 在 5173）或一条 `docker-compose up -d --build`，再加 API key 和一次 Chromium 安装。真正持续的成本是模型账单：每张截图最多四个版本，每个版本上限 3 美元（`GENERATION_MAX_COST_USD`），没有定价信息的模型不受这个上限约束。安装步骤里没有任何鉴权，后端只放在本机访问。

## 健康度与可持续性

- **维护：** B 级——2026-10-13 前 3 天还有提交，但最近 13 周里默认分支只有 3 周活跃；从未打过版本标签，只能跟 `main`。提交成批到来，部分来自 agent 写的分支。
- **响应：** A 级——3 个符合条件的 issue，首次响应中位数 4.4 小时（relaxed_solo 档）。
- **采用度：** 无法打分（`?`，没有可统计依赖方的包）。非注册表信号很大：截至 2026-10-13 约 8.03 万星、9.8 千 fork。
- **长寿度：** B 级——2023-11-14 建仓，1063 天（约 2.9 年）且仍活跃。按本索引“年龄 × 仍活跃”的先验，对一个价值随所调用模型变化的工具来说，算可以下注。
- **治理：** C 级——实际上只有一位维护者：Abi Raja 占 99.8% 的提交（`stats_contributors`），12 个月内活跃维护者 2 人。路线图跟着作者的托管产品走（`hosted` 分支、另一个闭源 SaaS 后端、付费墙实验分支），开源仓库的方向由它供给的商业服务决定。
- **风险 / 许可证：** A 级——MIT（版权 2023 Abi Raja），36 个月内没有改许可证。实际风险不在许可证，而在模型更替：默认模型列表和提示词随厂商发布不断重写，不存在可锁定的行为。

## 存疑（未验证）

- [未验证] 输出质量：README 里“最好的模型”排序和演示复刻图都出自作者；仓库自己的评估是 16 张截图由人按 1–4 分打分，`Evaluation.md` 里数据集下载链接仍写着 “TODO”，无法复现。
- [推断] `screenshot_preview` 自检能否可度量地提升还原度，没有公开数据；唯一依据是提示词里的要求和这个工具的存在。
- [未验证] “后端自身没有鉴权”是从安装文档和 `docker-compose.yml` 绑定 `0.0.0.0` 推出来的，没有逐个审查路由。
- [未验证] 录屏模式的效果、以及 README 说的录屏可生成“可用原型”，都没有实际跑过。
- [未验证] 横向对比里 v0 和 Builder.io Visual Copilot 的描述来自它们公开的产品定位，2026-10-13 没有实际试用。
