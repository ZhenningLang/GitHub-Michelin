---
name: video-shotcraft
slug: video-shotcraft
repo: https://github.com/Vincentwei1021/video-shotcraft
category: video-production
tags: [agent-skill, remotion, product-video, promo-video, motion-design, video-production]
language: TypeScript
license: Apache-2.0
maturity: plugin manifest v1.0.0 (media-only releases), 9,119 stars, 828 forks, created 2026-07-19, last push 2026-09-09 (as of 2026-09)
last_verified: 2026-09-21
type: skill-pack
upstream:
  pushed_at: 2026-09-09T05:46:40Z
  default_branch: main
  default_branch_sha: 5e71af35a2daee492dd3ea93e5e8903f32dcd13c
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:09:11Z
  overall: B
  overall_score: 2.6
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 13
        active_weeks_13: 9
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: C
      raw:
        registry: null
        canonical_package: null
        release_downloads: 126871
        release_assets: 231
        release_tier: C
        signal_basis: releases
    longevity:
      grade: D
      raw:
        repo_age_days: 65
        last_commit_age_days: 13
        cohort: skill-pack
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 7
        top1_share: 0.659
        top3_share: 0.854
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
    responsiveness: { reason: type_na }
---

# video-shotcraft

一个 Claude Code／Codex 的 skill：把产品或网页变成电影感的宣传片——一套镜头配方卡加一支已验收的 36.2 秒 Remotion 模板，用真实页面截图、2.5D 运镜和卡点声音设计，在本机由 Remotion 组合渲染成片。

![video-shotcraft — 健康度雷达](../../assets/health/video-shotcraft.zh.svg)

## 何时使用

你正要发布一个 web 或桌面产品，需要一支上市视频——不是加个标题条的录屏，而是看起来经过美术指导的东西：真实界面的特写、跟着视线走的运镜、落在节拍上的切换。你的 agent 会写 React，而你更愿意让它用一套有文档的镜头词汇把片子拼出来，而不是自己去手 K 关键帧。

你装好 skill、把产品指给 agent，它会先做一次只读的产品检查，然后给出三条路线：替换素材复现内置的 Ink Press 模板、自主自由创作、或与你共同创作（你确认产品简报、styleframe、镜头映射和分镜）。相对官方 [Remotion Agent Skills](../agent-skills/vendor-collections/remotion-skills.zh.md) 的决定性取舍是：后者教 agent 把引擎写对，而这个提供的是**审美层**——一百多张带 demo 的具名镜头配方、一支可模仿的参考成片、一个锁好版本的 Remotion 工程和一遍音效——于是质量来自素材库而不是模型的动效直觉。相对 [HyperFrames](hyperframes.zh.md)：HyperFrames 从里到外都是 Apache-2.0，而这个 skill 自己的代码是 Apache-2.0，但它面向的引擎是 [Remotion](remotion.zh.md)——后者只对个人和员工不超过三人的公司免费——真正决定二选一的通常就是这个许可问题，而不是功能清单。

## 怎么用起来

这个 skill 是 Markdown 指令加素材：`SKILL.md` 规定模式规则，`references/` 放流水线、审美准则、声音设计与终检清单，`references/shots/` 放镜头配方卡，`demos/` 是每张卡对应的一个 Remotion 组件，`template/` 是一支完整的成片工程。你的 agent 读它被指定的模式，截取你产品真实的页面，然后把整支片子写成 React／Remotion 组合——每个镜头都是一个由归一化进度 `t` 驱动的组件，因此组合是可复现的。渲染就是普通的 Remotion 命令行：先 `npm install`，再 `npx remotion render src/index.ts AiflPromo out/promo.mp4`（模板把 `remotion` 与 `@remotion/cli` 钉在 4.0.484；该工程是 private 的，测试是 vitest，只覆盖纯函数 helper）。这个 skill **不做**的是生成画面、人声或音乐：主体是你的真实截图，动效是代码，音频是仓库里钉住的音效库加卡点规则。交付后还有两个可选出口——一个把成片拆成镜头／转场／字幕／音效轨、可在浏览器里继续编辑的 Motion Workbench，以及一份可编辑的剪映草稿导出——于是你这一侧是产品简报、模式选择和最后的审美裁决，它那一侧是分镜、镜头实现、声音设计和渲染。

![video-shotcraft — 主干用户故事](../../assets/flow/video-shotcraft.zh.svg)

<!-- flow-steps:begin (generated from flows/video-shotcraft.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：把 skill 装进 Claude Code 或 Codex — `npx skills add Vincentwei1021/video-shotcraft`
2. **你**：把产品交给它并要一支宣传片，可以点名镜头卡 — `Use video-shotcraft to create a promo for my desktop product.`
3. **video-shotcraft**：先做一次只读的产品检查，给出三种模式：模板、自主自由创作、共同创作
4. **你**：选一种模式；模板路线就是把你的素材替换进 Ink Press 这支片子里 — `template/TEMPLATE.md`
5. **video-shotcraft**：把每个镜头做成 Remotion 组件：真实截图、2.5D 运镜、卡点音效
6. **video-shotcraft**：在你本机把成片渲染成 MP4 — `npx remotion render src/index.ts AiflPromo out/promo.mp4`

**价值**：一支有真实产品截图、运镜编排到位的电影感宣传片，不用在 After Effects 里手 K 关键帧

</details>
<!-- flow-steps:end -->

## 何时不用

- **你的组织超过三名员工且不打算买 Remotion 许可。** 交付物就是 Remotion 工程，所以引擎那个带资格门槛的许可适用于你要发布的作品。改用 [HyperFrames](hyperframes.zh.md)（Apache-2.0，无人头门槛）或 [anything2explainer](anything2explainer.zh.md)，因为这是锁版本也解决不了的许可问题。
- **你需要旁白、数字人或生成式画面。** 这个 skill 是在真实产品截图之上做动效设计，没有配音或视频生成环节。要带旁白的解说片用 [anything2explainer](anything2explainer.zh.md) 或 [OpenMontage](open-montage.zh.md)；要靠素材驱动的纪录片式混剪也用 [OpenMontage](open-montage.zh.md)。
- **你需要以剪映为主路径的中文短视频工作流。** 在这里剪映只是 Remotion 成片交付后的一个导出出口；要自动化时间轴本身，请用 [JianYing Editor Skill](../media-processing/nle-automation/jianying-editor-skill.zh.md)。
- **你要克隆某支已有爆款视频的结构。** 那是另一种方法——[Hypit](hypit.zh.md) 面向克隆并批量变体；这个面向原创的产品宣传片。
- **你需要稳定性保证、版本化 release 或可长期维护的依赖。** 仓库约 2 个月历史，只有媒体类 release、没有 semver tag，11 个 watcher 对 9.1k star，而且是一位作者的系列仓库之一。请把它当成按 commit vendored、锁版本的素材库，而不是基础设施 [推断]。
- **你要的是有治理、多阶段流水线和 QC 闸门的解说片。** 用 [anything2explainer](anything2explainer.zh.md)，它的全部卖点就是检查点和量化评审；这个 skill 的质量控制是评审清单加上你自己的判断。
- **你的产品截图涉密或受 NDA 约束，而这个工作流会把它们交给第三方。** 整条流水线是本地化的（截图、Remotion 渲染、仓库内音效素材），文档里没有描述任何上传步骤——但在指向未发布界面之前请先自行确认，因为这个 skill 同时也在驱动并非你写的 agent 侧工具。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Remotion Agent Skills](../agent-skills/vendor-collections/remotion-skills.zh.md) | ✅ | 片子是定制的、需要 agent 把引擎写对时选官方 skill；当你想用一套久经验证的镜头库加一支现成模板产出经过美术指导的产品宣传片时选 video-shotcraft，因为官方 skill 给的是 API 知识，没有镜头词汇也没有参考成片。 | 官方 skill 是第一方、与引擎版本同步、对审美不作主张；video-shotcraft 是第三方，带一百多张镜头卡和一支 36.2 秒参考片，同时继承别人的审美和素材结构。 |
| [Remotion](remotion.zh.md) | ✅ | 你在自建组合管线、想要六年历史的框架和 Lambda 渲染器时直接选 Remotion；当你想不设计就拿到产品宣传片那一层——镜头配方、模板、音效、Workbench——时选 video-shotcraft，因为 Remotion 是引擎，这个是它的某一种带观点的用法。 | Remotion 给长寿性、生态和分布式渲染，代价是公司规模许可门槛；video-shotcraft 给通往精致宣传片的捷径，但只有几个月历史、单一作者、绑定一个引擎版本。 |
| [HyperFrames](hyperframes.zh.md) | ✅ | 当许可自由和便于编辑的 HTML 组合模型比动效深度更重要时选 HyperFrames；当成片必须看起来经过刻意编排、且你接受 Remotion 的许可时选 video-shotcraft，因为 HyperFrames 没有任何门槛，但也没有等价的镜头库。 | HyperFrames 是 Apache-2.0、无需打包器且对 CI 友好；video-shotcraft 自身也是 Apache-2.0，但产出的是 Remotion 组合，于是许可与 React 工具链会一并跟来。 |
| [anything2explainer](anything2explainer.zh.md) | ✅ | 片子要用旁白讲解一个主题、并有人工检查点时选 anything2explainer；当片子要用真实界面特写去卖一个产品、且不需要旁白时选 video-shotcraft，因为两者从不同的输入产出不同的东西。 | anything2explainer 有受治理的 9 阶段流水线、量化 QC 和非商用许可；video-shotcraft 是 Apache-2.0、无旁白，代码库许可宽松但很年轻。 |
| After Effects | 未收录 | 由动效设计师主导、手工控制正是目的时用 After Effects；当宣传片必须由 agent 从代码反复重新生成时选 video-shotcraft，因为 AE 是专有图形界面的手工活，没有 agent 能触及的事实源。 | After Effects 提供完全的帧级控制和成熟的专业人才市场；video-shotcraft 用这份控制换取可复现、真实页面截图和可代码评审的成片。 |

## 健康度与可持续性

- **维护（2026-09-21）：** 仓库建于 2026-07-19，最后 push 是 2026-09-09——活跃，但没有任何版本化 release：GitHub 上的两个 release 都是媒体附件（`gallery-media`、`showcase-media`），因此没有 tag 可锁。仓库内 `plugin.json` 声明版本 1.0.0。
- **治理／巴士系数：** 一位作者（`Vincentwei1021`，34 次提交）加五位小贡献者（`skyzhao1223` 6 次、`sarff0` 3 次，另三位各 1–2 次）。个人账号，未见组织、基金会或资金。巴士系数为 1 [推断]。
- **背书与长青度：** 约 2 个月历史。这是本批里最明显的 Lindy 警告：9,119 star 对 11 个 watcher、828 fork，而 188 MB 仓库里主要是画廊素材——这么快涨星却没有相称的关注与贡献基础，是宣传信号而不是耐久性信号 [推断]。作者在做这一类 skill 的系列，说明有一套可复制的流程，但也意味着风险集中。
- **采用与生态：** 有在线画廊站点、多语言 README（英／中／日）、Trendshift 徽章，以及面向 Claude Code 插件市场的 plugin manifest；核验时 6 个 open issue。真实使用是可能的但无法计量——skills 仓库没有下载量或依赖项目数这类数据。
- **风险标记：** 没有 tagged release（无法锁版本）；模板内把引擎钉在 Remotion 4.0.484（升级 Remotion 是你的活）；文档里的数量互相打架（README 抬头写 157 张卡／214 个预览，同一份 README 的更新日志写 152 张卡／209 个预览，Workbench 说明写 216 个动效，而 `SKILL.md` 又写 157——数字请数过目录再用）；许可是分裂的：本仓库 Apache-2.0，而它面向的引擎 Remotion 带资格门槛。

## 存疑（未验证）

- [未验证] 本页没有任何一项被实际执行：没有跑过渲染，也没有渲染过任何一张镜头卡，因此所有质量说法（电影感 2.5D 运镜、卡点音效、预览与渲染像素一致）都只是 README／SKILL.md 的作者自述。
- [未验证] 剪映导出（按镜头切版、原生文字轨重建、音效／BGM 分轨）文档称仅由作者在 macOS 的剪映专业版 11.2 上验证过；本页未复现，其他剪映版本更无从确认。
- [未验证] Workbench 的「预览与渲染帧一致（已做像素一致性验证）」没有实测；把它当作对你自己修改的保证是不成立的。
- [推断] 星数／关注数之比（9,119 star 对 11 watcher、2 个月历史）被解读为榜单曝光驱动而非深度采用；GitHub 不公开来源渠道，所以这是推断，不是刷星的证据。
- [推断] 许可上的连带后果——用它做的宣传片会牵进 Remotion 那个带门槛的许可——来自「生成物是 Remotion 组合」以及模板钉住 `remotion`／`@remotion/cli` 4.0.484 这两点；作者在 README 里没有声明这层耦合。
- [未验证] 素材数量在仓库自己的文档之间就不一致（157／152 张镜头卡；214／209 个预览；Workbench 216 个动效）；`references/shots/` 里的真实数量没有清点。
- [未验证] 钉住的依赖集（`@remotion/cli` 4.0.484、`react` 19.2.7、`typescript` 6.0.3）与「测试只有 vitest」这两点读自 `template/package.json` 和根 `package.json`；没有执行安装或测试。
- [未验证] README 指向同一位作者的姊妹旁白视频 skill；它不是本页场景的替代品，本页也未评估。
- [推断] 188 MB 的仓库体积被归因于画廊／预览素材，依据是目录结构（demos、gallery、assets），并没有做逐目录的体积拆解。
- [推断] 健康度雷达里 `risk_license` 的 A 分只评估本仓库自己的 `LICENSE`；它不会建模「产出 Remotion composition」带来的下游许可暴露，因此不要把这一格绿灯读成「超出 Remotion 员工数阈值也能商用」的放行。
