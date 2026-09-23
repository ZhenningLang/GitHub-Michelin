---
name: dragnet
slug: dragnet
repo: https://github.com/dragnet-org/dragnet
category: article-extraction
tags: [content-extraction, machine-learning, boilerplate-removal, python, scikit-learn]
language: Python
license: MIT
maturity: v2.0.x, low-activity / aging deps, ~1.3k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2025-07-08T00:53:21Z
  default_branch: master
  default_branch_sha: 4a1649d9b29bf64ccc5a86200e415e8b04cd257b
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:13:07Z
  overall: D
  overall_score: 1.25
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1962
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: dragnet
        dependent_repos_count: 13
        downloads_last_month: 884
        graph_tier: D
        volume_tier: E
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: E
      raw:
        repo_age_days: 5207
        last_commit_age_days: 1962
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# dragnet

一种用机器学习做网页正文抽取的方法——训练好的模型从页面 HTML 里拉出正文（可选连用户评论一起），靠多样的文本/标记特征而非手调启发式。

![dragnet — 健康度雷达](../../../assets/health/dragnet.zh.svg)

## 何时使用

你在用 Python 搭一条正文抽取管线，而纯启发式抽取器老是把你的页面切错——把正文过裁，或把评论串和样板留下。你想要一个在标注样本上训练过、还能把*正文*和*用户生成评论*区分开的东西。于是你转向 dragnet：`extract_content(html)` 只给你正文，`extract_content_and_comments(html)` 给你正文 + 评论，你可以加载预训练模型（如内置的 `kohlschuetter_readability_weninger` 正文模型），或者——因为它暴露一个 scikit-learn 风格、带 `fit`/`predict` 的抽取器——在你领域的标注页面上**训练你自己的**。它血统是学术的——WWW 2013 那篇“Content Extraction Using Diverse Feature Sets”——所以卖点是一个基于模型、可针对你的数据调优的抽取器，而非固定启发式。

当你有（或能标注）训练数据、想要能靠重训改进的抽取质量、而不愿接受一刀切启发式时，你会专门选它。它是 Python 正文抽取领域里的 ML 选项。

## 何时不用

- **你今天就要一个有维护、好安装的依赖。** 这是最大的存疑：dragnet **低活跃**（最后 push 2025-07，最后发布 2.0.4 在 2019），且 pin 了**老化、狭窄的依赖范围**——尤其 `scikit-learn>=0.15.2,<0.21.0` 和 `ftfy<5.0.0`——与现代 Python/科学栈冲突，会让安装很痛。[推断]
- **你不想要 numpy/scipy/Cython 构建。** 它建在数值栈上、带 Cython 扩展；安装/编译比纯 Python 启发式抽取器重。
- **你只要零训练的像样文章抽取。** 一个启发式库（[Readability.js](readability-js.zh.md)、[python-readability](python-readability.zh.md) 或 trafilatura）轻得多，对许多管线已足够；dragnet 的优势是 ML/评论，而你可能并不需要。
- **你需要现代元数据或爬取支持。** 它返回正文（和评论）字符串；不是像 trafilatura 那样的完整元数据/爬取框架。
- **你需要一个面向未来、被持续打补丁的抽取器。** 鉴于节奏和依赖 pin，把它当作实际处于维护吃老本——别在不自己接管 fork 的情况下，把长寿的关键管线建在它上面。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [python-readability](python-readability.zh.md) | ✅ | 需要更轻的 lxml 启发式抽取器时，选 python-readability。 | lxml 启发式抽取器；轻得多、好装得多、无 ML 训练——但没有学习式/评论分离。 |
| [Readability.js](readability-js.zh.md) | ✅ | 需要 Mozilla 的 JavaScript reader-view 引擎时，选 Readability.js。 | Mozilla 的 JS reader-view 引擎；语言不同、启发式而非 ML、无评论抽取。 |
| [boilerpipe](boilerpipe.zh.md) | ✅ | 需要经典 Java 样板移除算法时，选 boilerpipe。 | Java 样板移除算法（dragnet 的灵感来源之一）；经典但仓库实际已废弃。 |
| [trafilatura](trafilatura.zh.md) | ✅ | 需要现代、活跃维护、带元数据和爬取支持的 Python 抽取器时，选 trafilatura。 | 现代、活跃维护的 Python 抽取器，基准强、带元数据和爬取支持；如今通常是更好的默认——启发式 + 规则而非可训练 ML 模型。 |
| Mozilla fathom / 自建 ML | 未收录 | 需要自己构建学习式抽取时，选 Mozilla fathom 或自建 ML。 | 自己搓学习式抽取；控制更多，但比采用 dragnet 的模型工作量大得多。 |

## 技术栈

- **语言：** Python（为 2.7 开发、后加 Python 3 支持——这本身就是年龄信号）。
- **ML / 数值：** scikit-learn、numpy、scipy、**Cython** 扩展，解析用 lxml，文本修复用 ftfy。
- **模型：** 随包发布预训练 pickle 模型（正文 与 正文+评论 抽取器）；一个 sklearn 风格的 `Extractor`，带 `fit`/`predict`，让你训练自己的。
- **方法：** 基于特征的 ML 抽取（Kohlschütter/Weninger/Readability 衍生特征），依 WWW 2013 论文。

## 依赖

- **运行时：** Python + numpy、scipy、scikit-learn（**pin `<0.21.0`**）、Cython、lxml、ftfy（**`<5.0.0`**）。狭窄/陈旧的 pin 是现代系统上的实际痛点。[推断]
- **构建：** 涉及 Cython 编译；若无兼容 wheel，可能需要一套可用的 C/Cython 工具链。
- **模型：** 预训练 pickle 随包发布（经 `load_pickled_model` 加载）；训练自己的需要标注数据。
- **无服务：** 纯库，无网络无数据存储；HTML 由你提供。

## 运维难度

**中——重在安装，而非运行时。** 运行时是个无状态库：喂 HTML、得正文。难点在于把它*装进*现代环境——鉴于陈旧的 scikit-learn/ftfy pin 和 Cython 构建，你可能需要一个隔离的/更旧的 virtualenv，或自己改 pin，然后验证 pickle 模型在你的科学栈版本下仍能加载。一旦装好，运行它很简单（CPU 受限、可并行）。训练自定义模型则在其上再加一套标注 + ML 工作流。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 最后 push 于 2025-07；最新发布 2.0.4 可追溯到 **2019**。这是**低活跃/吃老本**——偶有改动但非活跃开发。未正式归档，但节奏近乎停滞。[推断]
- **治理 / bus factor。** 归一个 **Organization**（`dragnet-org`）所有、有若干历史贡献者，但活动已变稀——鉴于停滞节奏，有效 bus factor 偏低。[推断]
- **年龄 × Lindy（2026-06）。** 2012-06 创建——约 14 岁，但**没有当前活跃的年龄不算 Lindy 通过**：一个长寿却*吃老本*的项目在代码上耐用、在支持上脆弱。要用 年龄 × 仍活跃，而这里“仍活跃”那一半很弱。[推断]
- **采用度与生态。** 约 1.3k star 和学术血统（WWW 2013）给过它真实的历史采用；如今 Python 社区大体已转向 trafilatura 等有维护的替代品。[未验证]
- **风险标记。** 老化、狭窄的依赖 pin（scikit-learn `<0.21`、ftfy `<5`）和近乎停滞的节奏是主要风险——安装摩擦、上游修复无保证。MIT 许可，未发现 relicense 历史。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 1.3k star；最新发布 2.0.4（2019），最后 push 2025-07——数字对时间敏感，发布/push 之间的落差是吃老本信号。
- [推断] `scikit-learn>=0.15.2,<0.21.0` 和 `ftfy<5.0.0` 的 pin 读自仓库的 requirements/setup；其与现代栈不兼容是推断，且*当前*在某个 Python 版本上的可安装性这里未实际试装。
- [推断] “低活跃/吃老本”和“有效 bus factor 偏低”由节奏（2019 发布、2025-07 push）推断，而非维护者声明。
- [未验证] 内置 pickle 模型在当前 numpy/scikit-learn 下是否仍能干净加载未核实；pickle 跨 sklearn 版本兼容性是已知的脆弱点。
- [未验证] 与 trafilatura/启发式抽取器的相对精度反映总体定位，而非实测基准。
