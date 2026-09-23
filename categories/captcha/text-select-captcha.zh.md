---
name: Text_select_captcha
slug: text-select-captcha
repo: https://github.com/MgArcher/Text_select_captcha
category: captcha
tags: [captcha, click-captcha, text-select, yolo, siamese-network, onnx, pytorch, chinese]
language: Python
license: NONE (no LICENSE file — all rights reserved)
maturity: no tagged releases, active, last push 2026-05 (verified 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-05-08T05:01:15Z
  default_branch: master
  default_branch_sha: dcd1ac317c73cd29a7e3118f935c2b3fbd34cb02
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:01:32Z
  overall: D
  overall_score: 1.4
  scored_axes: 5
  applicable_axes: 6
  capped: true
  cap_reason: "source-available/no-license: NONE"
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 137
        active_weeks_13: 0
        carve_out: mature_library_lindy
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: B
      raw:
        repo_age_days: 2221
        last_commit_age_days: 137
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: E
      raw:
        spdx_id: NONE
        permissiveness: source_available
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
---

# Text_select_captcha

一个中文深度学习库，用于识别**点选/文字点选验证码**——给一张“按顺序点这些字”的图，它用 YOLO 检测候选字形、用孪生网络（Siamese）把它们与提示匹配，返回点击坐标。

![text-select-captcha — 健康度雷达](../../assets/health/text-select-captcha.zh.svg)

## 何时使用

你是 Python 开发者，写的爬虫或自动化要打一个被*点选文字*验证码挡住的站点——就是那种显示一堆打乱的中文字、让你“按顺序点 春、夏、秋”的。光靠 OCR 解不了：你得*定位*每个候选字形，再把它们对着提示*排序*。这个库正好把整条管线打包好了——用 YOLO 检测器找出字符框，加一个孪生/双生网络把目标字形与候选匹配——并以一个简单调用（外加可选的 FastAPI 服务）暴露出来，返回坐标。它走 ONNX runtime 推理，所以你能在一台普通机器上纯 CPU 跑（README 称 1 核 2G 服务器即可），还能用你自己约 300 张标注图重训，以适配某个站点的字体/风格。

你专门选它，是当你的目标属于交互式*点选*这一族（文字点选 / 选字 / 消消乐式）而非普通图中文字验证码，且你想要一条现成的中文字形管线，而不是自己拼检测 + 匹配。

## 何时不用

- **合法性 / ToS。** 仓库自己的免责声明说仅供研究/学习；破解一个站点的验证码可能违反其条款或当地法律。这是决定性的过滤器——任何实际使用前先确认你有授权。
- **没有开源许可。** 仓库里**没有 LICENSE 文件**，所以它在宽松意义上*不是*开源——默认版权 = 保留所有权利。你并未获得使用、修改或再分发的权利；别在“它是免费的”假设下把它内置进产品。[推断]
- **你的验证码不是点选式。** 对图中文字 OCR、滑块/缺口验证码，或 reCAPTCHA/hCaptcha/Turnstile 行为式挑战，这是错的工具——它专攻点选文字。
- **你需要准确率保证。** README 的“96% 准确率 / 300ms”是作者在自己数据上的数字；真实准确率取决于目标站点的字体、扭曲，以及你是否重训。在你*自己的*验证码上测出来之前，当作宣传。
- **你想要长期支持。** 这是单作者项目，无 tag 发布，且带教程变现倾向（链到一门付费课程）；免费仓库可能落后于付费材料。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Cap](capjs.zh.md) | ✅ | 需要验证码*生成/挑战*系统，而不是 solver 时，选 Cap。 | 它是工作量证明和服务端挑战流，属于问题的另一面。列在这里是为了消歧“captcha”工具，而非作为替代。 |
| ddddocr | 未收录 | 需要流行的中文通用 OCR/验证码库，且要检测、分类、滑块匹配覆盖时，选 ddddocr。 | 覆盖更广，也是 solver；混合验证码类型时常先试它，但只应在授权场景使用。 |
| 商业打码平台 | 未收录 | 能接受人工/混合验证码识别 API 时，选商业打码平台。 | 按次付费、无需自托管模型，但有持续成本、第三方依赖，以及同样的法律问题。 |
| 自建 YOLO + Siamese | 未收录 | 许可清晰和完全可控比直接使用本仓库更重要时，选自建 YOLO + Siamese 管线。 | 整条管线的构建、标注、训练都要你自己做，而这个仓库已把它拼好。 |

## 技术栈

- **模型：** 用于定位字形的 YOLO 系检测器 + 用于把目标与候选匹配的孪生/双生网络；经 **ONNX Runtime** 推理。[推断]
- **服务：** 可选的 **FastAPI** + `uvicorn` HTTP 服务（RESTful API）封装识别器；用 `python-multipart` 上传图片。
- **图像：** OpenCV（`opencv-python-headless`）、Pillow、NumPy；`playwright`/`aiohttp`/`requests` 似用于示例抓取/自动化。
- **训练：** 可在你自己的标注集上训练（README 称约 300 张即可）；更重的训练教程被锁在一门付费课程后。

## 依赖

- **运行时：** Python **3.8+**、ONNX Runtime、OpenCV、Pillow、NumPy，服务用 FastAPI/uvicorn（据 `requirements.txt`）。
- **硬件：** 支持纯 CPU 推理；README 称可在 1 核 2G 机器上跑——推理无需 GPU。
- **模型/权重：** 仓库内随附识别器的 ONNX 模型文件（`model/` 目录）；重训需要你自己的标注图。

## 运维难度

**推理很低；成本在数据而非部署。** 跑它就是 `pip install -r requirements.txt`、加载随附的 ONNX 模型、调识别器（或跑 FastAPI 服务）——纯 CPU，无 GPU 或外部数据存储。真正的功夫在**适配准确率**：若站点的字体/扭曲与随附模型的训练数据不同，你得收集并标注图片再重训，而最详尽的训练指引在一门付费课程后面。还有一个长期的运维现实：目标站点随时可能换验证码，弄坏你的管线——这是军备竞赛，不是装好就不管的依赖。[推断]

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 最后 push 2026-05——近期有改动，所以宽泛意义上**活跃**，但**无 tag 发布**、无 changelog，缺乏版本纪律。[推断]
- **治理 / bus factor。** **单作者**项目（`MgArcher`，约 1.6k star）在个人账号下——明显的 bus-factor 风险；solo 仓库上的高 star 是标记，而非延续性的保证。[推断]
- **年龄与 Lindy 判断。** 2020-08 创建（约 6 年）且仍有改动 ⇒ **中等** Lindy 信号——它已存续数年，但单一维护者加上验证码军备竞赛领域，限制了这个先验能走多远。[推断]
- **背书 / 动机。** README 把项目绑定到一门付费中文 AI 课程（道满PythonAI）并征集捐赠；免费仓库可能部分充当引流，因此最完整的材料可能在付费墙后。[推断]
- **风险标记。** **无许可**（默认保留所有权利）是主导标记——并未授予合法使用权。加上单作者治理、自报准确率，以及验证码 solver 固有的脆弱性。[推断]

## 存疑（未验证）

- [未验证] 仓库内不存在 LICENSE 文件（GitHub 报告无许可）；记为“NONE——保留所有权利”。在没有明确授权的情况下，你无权使用/修改/再分发——依赖前请与作者确认。
- [未验证] 截至 2026-06 约 1.6k star，最后 push 2026-05；无 tag 发布，故不断言版本号。
- [未验证] “96% 准确率”"300–500ms"“约 300 张训练”是作者在自己数据上的 README 说法——未经独立测量；你的结果取决于目标验证码。
- [推断] 模型架构（YOLO 检测器 + Siamese 匹配器、ONNX 推理）是由 README 和 `requirements.txt` 推断，未对源码重新核实。
- [推断] 最详尽的训练教程链到付费课程；免费仓库究竟是完整还是引流，属于推断。
