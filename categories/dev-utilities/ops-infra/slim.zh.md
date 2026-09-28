---
name: SlimToolkit
slug: slim
repo: https://github.com/slimtoolkit/slim
category: ops-infra
tags: [containers, docker, image-optimization, security, seccomp, apparmor, minification, cncf]
language: Go
license: Apache-2.0
maturity: "v1.40.11 (2024-02), coasting, ~23.4k stars (as of 2026-09); CNCF Sandbox"
last_verified: 2026-09-28
type: tool
upstream:
  pushed_at: 2026-09-19T23:40:59Z
  default_branch: master
  default_branch_sha: 976805241c0000c0114b095e384657e0e98ccaaa
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T05:51:16Z
  overall: B
  overall_score: 3.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 8
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.8
        qualifying_issues: 3
        band: relaxed_solo
        window_offset_days: 1
        source: pr
        inferred: false
    adoption:
      grade: C
      raw:
        registry: proxy.golang.org
        canonical_package: github.com/slimtoolkit/slim
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: "?"
        cross_check_divergence: null
        release_downloads: 493684
        release_assets: 50
        release_tier: C
        signal_basis: releases
        tier_source: releases
    longevity:
      grade: A
      raw:
        repo_age_days: 4037
        last_commit_age_days: 8
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 4
        top1_share: 0.25
        top3_share: 0.75
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# SlimToolkit

一个 CLI：它检查一个容器镜像，把它跑起来观察实际用到了什么，然后产出一个最小化、加固过的镜像——通常体积缩小数倍乃至几十倍——全程不改你的 Dockerfile，还能顺带自动生成 Seccomp/AppArmor 安全配置。

![slim — 健康度雷达](../../../assets/health/slim.zh.svg)

## 何时使用

你是个平台工程师，接手了一堆基于 `ubuntu:22.04` 或完整 `python:3.12` 基础镜像构建的应用镜像。每个都塞着几百兆运行时根本不碰的 shell 工具、包管理器和共享库——拖慢拉取、扩大攻击面，还让漏洞扫描器为一堆你压根不调用的包疯狂报 CVE。把每个 Dockerfile 重写成 distroless 或多阶段构建才是“正确”的修法，但你手下有几十个团队，这个季度没人想冒着把构建搞挂的风险。于是你跑 `slim build your-image:latest`：SlimToolkit 把容器启起来、对它施加负载（HTTP 探针或你自己的测试命令）、观察实际用到了哪些文件和系统调用，然后产出一个把没用到的东西全剥掉的 `.slim` 变体——经常小上 10–30 倍——而 entrypoint 和行为保持不变。作为附赠，它还能丢出一份生成好的 Seccomp 和 AppArmor 配置，让你不必手工审计 Linux 系统调用就能把容器锁紧。

当你想*现在*就拿到体积和攻击面的收益、对着自己并不掌握源码的镜像、又不想先逼着每个团队做基础镜像迁移时，你会选它。它最大的价值是作为推镜像入库前的一道改造/优化 pass，而不是最初构建镜像的那个东西。

## 怎么用起来

Slim 是一个披着 CLI 外衣的动态分析器，不是静态的 Dockerfile 改写器。你跑 `slim build <image>`，它会通过本地 Docker daemon 拉取镜像、启动一个临时容器并对它*施压*——一个 HTTP 探针去访问容器暴露的端口，加上你用 `--exec` 声明的命令——同时记录运行中的进程实际发生的每一次文件访问和系统调用。施压阶段结束后，它重建一个只包含观察到被用到的产物（外加你用 `--include-path` 白名单强行保留的内容）的新镜像，打上 `.slim` 标签，并写出附属产物：一份 Seccomp 配置（观察到的系统调用集合，可以用 `docker run --security-opt seccomp:...` 直接加载）和一份 AppArmor 配置。仍然归你的部分是：让施压有代表性——探针、测试流量或覆盖你在乎的代码路径的 `--exec` 命令——以及在推镜像之前端到端验证最小化后的镜像确实还能跑。`slim xray` 提供同一套观察流程但不重建，只出一份检查报告。

![SlimToolkit — 主干用户故事](../../../assets/flow/slim.zh.svg)

<!-- flow-steps:begin (generated from flows/slim.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：装上 CLI — `brew install docker-slim`
2. **你**：一条命令指向本地任意镜像 — `slim build your-name/your-app`
3. **SlimToolkit**：启动容器，用 HTTP 探针和你给的 --exec 命令施压 — 组件：`HTTP 探针`
4. **SlimToolkit**：记录实际用到的文件和系统调用，重建只含这些产物的 .slim 镜像 — 组件：`build 命令`
5. **你**：跑一下瘦身后的镜像，验证行为不变 — `docker run archlinux:curl curl checkip.amazonaws.com`

**价值**：不改 Dockerfile，镜像最多小 30 倍，还附带生成好的 Seccomp/AppArmor 配置

</details>
<!-- flow-steps:end -->

## 何时不用

- **你的应用在运行时动态加载文件。** SlimToolkit 只保留它*观察到*被用过的东西。任何惰性加载的内容——只在你探针没触发的代码路径里才命中的插件目录、locale/时区数据、模板、按需加载的原生库、`dlopen` 进来的模块——都可能被剥掉，而镜像只会在生产环境里坏给你看。从源头修的替代方案（distroless + 多阶段）更可预测，因为镜像里有什么是*你*声明的。
- **你本可以直接改 Dockerfile。** 如果构建在你手里，一个 `distroless`/多阶段基础镜像或 `--no-install-recommends` 的纪律能在源头确定性地解决膨胀，没有“靠运行时 tracing”这一步会出错。靠观察做最小化，是给你*改不动*的镜像准备的改造手段。
- **你需要调试产出的镜像。** 剥光的镜像没有 shell、没有包管理器、连 `ls` 都没有——`kubectl exec` / `docker exec` 进去会很难受。这和 distroless 是同一种取舍，只是在这里它是副作用而非主动选择。
- **你想要漏洞扫描器或 SBOM。** SlimToolkit *缩小*攻击面，但既不枚举/报告 CVE，也不产出 SBOM——那是 Trivy/Grype/Syft 的活。它和扫描器配合用，不是替代品。
- **你的 CI 跑不了特权容器。** 生成 Seccomp 配置需要以特权模式、带 `SYS_ADMIN` 能力运行目标容器，而整条流程都需要一个可达的真实容器运行时（Docker daemon）。锁死的或 rootless 的 CI、没有 daemon 的构建集群，都会让集成变得不简单。
- **对覆盖率敏感的正确性。** 因为存活下来的内容取决于你的探针实际跑到了什么，结果质量只和你在最小化时对容器的测试覆盖一样好——压得不够就会发出一个坏镜像；这是每条流水线实打实的集成成本，不是即插即用。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| Distroless（GoogleContainerTools） | 未收录 | 可以在极小基础镜像上重新构建，而不是缩减已有镜像时，选 Distroless。 | 你*拿来构建*的极小基础镜像——确定性、无运行时 tracing，但你得重构 Dockerfile（多阶段）并掌握源码。SlimToolkit 则是对已构建好的镜像做改造。 |
| 多阶段 / 手工优化 Dockerfile | 未收录 | 掌握源码级构建且追求可预测最小镜像时，选多阶段或手工优化 Dockerfile。 | 源头级修法：最小、最可预测、完全可控——但前提是你掌握并能改每个构建。SlimToolkit 的卖点是“不改 Dockerfile”。 |
| Trivy / Grype（扫描器） | 未收录 | 需要报告 CVE 或产出 SBOM，而不是缩减镜像时，选 Trivy 或 Grype。 | 发现并报告 CVE / 产出 SBOM；它们*度量*攻击面，不*缩小*攻击面。互补，而非替代。 |
| DockerSlim（前身） | 未收录 | 把 DockerSlim 当作前身/命名历史，而不是另一个当前项目来选。 | 不是另一个项目——DockerSlim 已改名为 Slim/SlimToolkit；同一套代码、同一套 `slim build` 流程。[推断] |
| Docker `docker build --squash` / 层压平 | 未收录 | 只需要减少层数而不是内容级最小化时，选层压平。 | 减少层数/重复，而非*内容*——每个没用到的二进制都还在。机制不同，收益小得多。 |

## 技术栈

- **语言：** Go（单一 CLI 二进制，`slim`）。
- **机制：** 动态分析——它把目标容器启起来，在施压阶段（HTTP 探针和/或用户提供的命令）观察文件访问和系统调用，再重建一个只含观察到被用过的产物的镜像。
- **容器运行时集成：** 与 Docker daemon 通信来拉取、运行、重建镜像（使用 `go-dockerclient`）；支持给临时容器传 host-config / capabilities。
- **安全配置：** 从观察到的系统调用/行为集合自动生成 Seccomp 和 AppArmor 配置。

## 依赖

- **一个容器运行时——必需。** 它需要一个可达的 Docker daemon（或兼容运行时）来检查、运行、重建镜像；这不是纯静态分析器。[推断]
- **生成配置需要提权。** Seccomp 配置生成会以特权模式运行容器并加上 `SYS_ADMIN` 能力——这是项目自己文档里写的。
- **状态卷。** 在容器里运行时，它会把执行状态（含生成的配置）持久化到一个 Docker 卷（默认 `slim-state`），或由你自己挂载。
- **安装路径：** 官方发布预编译二进制、Homebrew formula（`docker-slim`）以及容器镜像。

## 运维难度

**中等。** 作为交互式桌面/CI 工具，它没有常驻服务——装上二进制、调 `slim build <image>` 即可。真正的成本在集成与验证：你必须给它一种有代表性的方式去*施压*容器（探针、测试流量，或对它观察不到的路径用 `--include-*` 白名单），否则它会剥得太狠；然后你必须在信任产出之前端到端验证最小化后的镜像确实还能工作。把它接进 CI 意味着给 runner 一个 Docker daemon、（为了 Seccomp）特权执行，外加一道回归闸门，在过度最小化进生产前把它拦下来。跑起来不难，安全地集成才是真功夫。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 0.8 小时，基于 3 个 qualifying PRs（窗口内 issue 流量太薄，未构成样本）。
- **维护（2026-09）。** 仓库**未归档**，默认分支仍偶有真正的修复——例如 2026-08-02 修畸形 Dockerfile 触发 panic 的提交、2026-09-19 修 HTTP 探针示例的提交（GitHub 提交 API）——夹杂在 dependabot/CI bump 之间，但**最后一个打 tag 的 release 仍是 2024-02 的 v1.40.11**，断档已到约 2.5 年。读起来像**有人维护但在吃老本**：活着、没废弃，但没在按节奏发功能版本。[推断]
- **治理 / bus factor。** **CNCF Sandbox** 项目（README 中确认），有一份列了两位 maintainer 的 `MAINTAINERS.md`——但创建者 **Kyle Quest（@kcq）**约 816 次提交，下一位人类贡献者远远落后，且 `GOVERNANCE.md` 里直接写着 "TBD"。所以 Sandbox 身份带来的是生态可见度，**而非**深厚的、基金会运营的治理梯队——bus factor 集中在一个人身上。[推断]
- **背书与长期性。** 据 README 由 **Root.io（前身 Slim.AI）**支持；一家商业厂商的兴趣是长期性加分，但也把势头绑在了那家公司的优先级上。[推断]
- **年龄与 Lindy。** **2015-09** 创建（作为 DockerSlim）⇒ 约 11 岁且 2026 年仍有改动——一个**偏强的 Lindy** 信号：在其细分领域是个久经使用、广为人知的工具，但被上面那条停滞的发布节奏打了折扣。要把年龄 × 仍活跃一起看——它过关，但在“仍有活跃功能开发”这条轴上只是勉强过。[推断]
- **风险标记。** Apache-2.0，未发现 relicense 历史。主要标记：单一维护者集中、2024→2026 的发布断档，以及 CNCF Sandbox 身份下却 "GOVERNANCE: TBD"。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-09 约 23.4k GitHub star、213 个 open issue（GitHub API）——star/issue 数对时间敏感，作为健康代理并不可靠，仅供参考。
- [未验证] “小 10–30 倍” / “最高 30 倍”是项目 README 自己的表述；实际缩减极度依赖镜像本身（README 自己的例子从已是 distroless 基础镜像上的约 1.8 倍，到臃肿的 `ubuntu:14.04` 上的约 284 倍都有）。别承诺一个固定比例。
- [推断] “维护但吃老本”是从提交内容（多为 dependabot/CI）加上 2024-02 的最后发布推断而来，不是说功能开发已正式停止。
- [推断] 确切的运行时要求（具体到 Docker daemon，还是任意 OCI 运行时）及最低版本是从 README/用法推断的，这里未钉死——若对你是 load-bearing，请对照你运行时的当前文档核实。
- [推断] CNCF "Sandbox"（非 Incubating/Graduated）层级与 Root.io 背书在 2026-09-28 对照 README 再次确认；CNCF 分层会变——若这点 load-bearing，请去 CNCF landscape 重核。
