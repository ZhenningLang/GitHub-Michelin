---
name: socialscan
slug: socialscan
repo: https://github.com/iojw/socialscan
category: osint
tags: [osint, email, username, account-existence, availability-check, python]
language: Python
license: MPL-2.0
maturity: v2.0.1 (2024-01), sporadic activity (pushed 2026-08), 1.8k stars (as of 2026-09)
last_verified: 2026-09-18
type: tool
upstream:
  pushed_at: 2026-08-03T20:47:15Z
  default_branch: master
  default_branch_sha: 5ae42d0f82b0ebd717b3ae52b693b4ececa902b1
  archived: false
health:
  schema: 1
  computed_at: 2026-09-18T14:15:00Z
  overall: D
  overall_score: 0.75
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 971
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: socialscan
        dependent_repos_count: 18
        downloads_last_month: 15470
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
    longevity:
      grade: E
      raw:
        repo_age_days: 2770
        last_commit_age_days: 971
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: C
      raw:
        spdx_id: MPL-2.0
        permissiveness: weak_file_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# socialscan

异步的邮箱/用户名可用性检查器，直接查询平台**注册端点**（CSRF token、headers、cookies）而不是抓个人页——本类目里「可用/已占用」信号最干净的工具，代价是只覆盖约 11 个平台。

![socialscan — 健康度雷达](../../assets/health/socialscan.zh.svg)

## 何时使用

你在做品牌保护、抢注检查或授权范围内的 OSINT，需要一个**可信**的判定：某个邮箱或用户名在主流平台上是否已被占用。你运行 `socialscan user@example.com somehandle`（或把它当 Python 库 import），它并发查询各平台的注册流程，逐条返回 AVAILABLE / TAKEN / INVALID。因为它对话的是真实注册表单用的同一个端点，所以避开了个人页探测的经典假阳性（`admin` 这类保留名会正确显示为已占用，被删/被封的 handle 也不会误报可用）。

当「有人维护的正确性」比广度更重要时，你选 socialscan 而不是 [holehe](holehe.zh.md)：holehe 覆盖 120+ 邮箱站点但 2024-09 起停止维护，而 socialscan 仍有提交（最后 push 2026-08），且平台列表窄、更容易逐一复验。当你的真实问题是「这个标识符还能不能注册」而不是「这个人已经存在于哪里」时，你选它而不是 [Sherlock](sherlock.zh.md)/[Maigret](maigret.zh.md)——而且 MPL-2.0 是本类目最宽松的许可证。

## 何时不用

- **你需要广覆盖。** 总共约 11 个平台（邮箱：Instagram、Twitter、GitHub、Tumblr、Lastfm、Pinterest、Firefox；用户名另加 Snapchat、GitLab、Reddit、Yahoo）。要 120+ 邮箱站点用复验过的 [holehe](holehe.zh.md) fork；要 3000+ 用户名站点用 [Maigret](maigret.zh.md)。
- **你在建人物档案，不是查可用性。** 用 [Maigret](maigret.zh.md)——它提取个人页数据、ID 和交叉链接；socialscan 只回答占用/可用。
- **你需要 Google 生态深度情报。** 用 [GHunt](ghunt.zh.md)；socialscan 没有 Google 模块。
- **你需要保证有人维护的依赖。** 最后的 release v2.0.1 是 2024-01 的，贡献者约 7 人；提交零星。生产使用前钉住版本并复验模块。[推断]
- **你把「100% accuracy」当合同。** 那是作者对注册端点方法的 README 主张；注册流程会变，任何模块都可能无声腐化——把逐平台结果当可测试的假设，不是保证。
- **你没有所查标识符的授权。** 批量核查第三方邮箱与其他同类工具一样有法律/ToS 问题。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [holehe](holehe.zh.md) | 已收录 | 需要在它覆盖的约 11 个平台上拿到有人维护的准确判定时选 socialscan；只有需要 120+ 站点广度或恢复信息泄露方法时，才选 fork 并复验后的 holehe。 | socialscan 窄但信号干净、MPL-2.0；holehe 广但 2024-09 起弃养、GPL-3.0。 |
| [Maigret](maigret.zh.md) | 已收录 | 手里是用户名、要跨 3000+ 站点的完整档案时选 Maigret；问题纯粹是「这个标识符能不能注册」时选 socialscan。 | Maigret 用重型机械回答「这个人存在于哪里」；socialscan 用最小依赖（aiohttp、tqdm、colorama）回答「占没占」。 |
| [Sherlock](sherlock.zh.md) | 已收录 | 要在 480+ 网络查存在性时选 Sherlock；在它覆盖的平台上不能容忍个人页启发式假阳性时选 socialscan。 | Sherlock 更广、社区验证充分但更粗；socialscan 更窄但注册端点级准确，且同时支持邮箱。 |
| [GHunt](ghunt.zh.md) | 已收录 | 要做认证式 Google 账户调查时选 GHunt；要做无认证的多平台可用性检查时选 socialscan。 | GHunt 需要你的 Google 会话 cookie 且有 ToS 风险；socialscan 只需要能访问注册表单的网络。 |

## 技术栈

- **语言：** Python（setup.py 声明 `python_requires>=3.6`；CI 矩阵历史上覆盖更新版本）。
- **异步：** asyncio + aiohttp——所有平台查询并发执行（作者基准：约 100 次查询 ~4 秒）。
- **探测方法：** 逐平台模块复刻注册流程——取 CSRF token、设置 headers/cookies、提交标识符、把响应分类为 available/taken/invalid。
- **接口：** CLI（`socialscan` 控制台命令，带 `--platforms`、`--view-by`、`--available-only`）与可 import 的 Python API。
- **质量设施：** tests 目录 + tox/flake8 配置（本类目罕见）；遗留 Travis CI 配置。

## 依赖

- Python 运行时；`pip install socialscan`。运行时依赖极少：aiohttp、tqdm、colorama。
- 对约 11 个平台注册端点的出站 HTTPS；无 API key、无数据库、无自建服务。
- 未见代理支持的文档——单 IP 持续批量跑会撞平台限流。

## 运维难度

**低。** pip 即装、零配置、无状态一次性运行，模块面小（约 11 个平台），一个团队一下午就能手工复验一遍。唯一的持续负担是全类目共有的：平台会改注册流程，所以要定期复验并钉住版本；它没有 Maigret 那种自动更新的站点数据库。

## 健康度与可持续性

- **维护情况（2026-09）：** 未归档；最后 push 2026-08-03，但最后的 release v2.0.1 是 2024-01——零星提交、无发版节奏。活着，但在滑行。
- **治理 / bus factor：** 个人仓库（iojw），约 7 个贡献者；实质单人维护。未发现组织或商业支持。
- **年龄 × Lindy：** 创建于 2019-02（约 7.5 年）且仍有提交——年龄×活跃信号尚可，弱于 Maigret/Sherlock，因为活动零星。
- **采用信号：** 1.8k star / 221 fork；PyPI 上月下载 15,470 次（2026-09 实测）；社区远小于 Sherlock（92k）和 Maigret（37.7k）。
- **风险标记：** MPL-2.0 是文件级 copyleft（类目内最温和）；无代理/轮换方案；平台模块腐化风险；「100% accuracy」是未验证的作者主张。

## 存疑（未验证）

- [未验证] 「100% accuracy」与「约 100 次查询 ~4 秒」是作者 README 自报数字；本条目未独立复现。
- [未验证] 未实测当前逐平台模块健康度；平台列表取自 2026-09 的 README，v2.0.1（2024-01）之后流程可能已变。
- [推断] 2026-08 有 push 但无 release，说明维护是响应式的（依赖升级/小修复）而非功能开发。
- [推断] 无文档化代理支持意味着批量使用会被平台限流或封 IP。
