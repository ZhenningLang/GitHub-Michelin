---
name: Sherlock
slug: sherlock
repo: https://github.com/sherlock-project/sherlock
category: osint
tags: [osint, username, account-existence, reconnaissance, social-networks, tor, python]
language: Python
license: MIT
maturity: v0.16.2 (2026-09), active, 92.0k stars (as of 2026-09)
last_verified: 2026-09-18
type: tool
upstream:
  pushed_at: 2026-09-18T05:17:01Z
  default_branch: master
  default_branch_sha: 376018708c0f6948d3f978a9ae2915024e794654
  archived: false
health:
  schema: 1
  computed_at: 2026-09-18T14:15:58Z
  overall: A
  overall_score: 3.5
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 9
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 53.9
        qualifying_issues: 9
        band: relaxed_solo
        window_offset_days: 13
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: sherlock-project
        dependent_repos_count: 0
        downloads_last_month: 93809
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
    longevity:
      grade: A
      raw:
        repo_age_days: 2825
        last_commit_age_days: 9
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 23
        top1_share: 0.136
        top3_share: 0.265
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Sherlock

经典用户名猎手：通过个人页探测核查一个 handle 在 481 个社交网络上的存在性，内置 Tor/代理支持和 CSV/XLSX/JSON 导出——用户名 OSINT 最简单、社区验证最充分的入口，代价是信号比档案类工具更粗。

![Sherlock — 健康度雷达](../../assets/health/sherlock.zh.svg)

## 何时使用

你在做授权侦察——交战规则内的红队足迹测绘、品牌/handle 抢注检查，或审计自己的在线存在——需要快速回答「这个用户名存在于哪里」。你运行 `sherlock user1 user2`，它探测其 481 站点数据库（一个声明式的 `data.json`，逐站记录 URL 模式和错误信息匹配），打印找到的账户及链接，可导出 CSV/XLSX/JSON。`--tor`/`--unique-tor` 和 `--proxy` 内建，用于抗限流。

当简单、速度和最小依赖面（requests + 一个 JSON 文件）胜过档案深度时，你选 Sherlock 而不是 [Maigret](maigret.zh.md)——Sherlock 告诉你 handle **在哪里**存在，但不提取个人页内容、ID 或交叉链接。当你的键是用户名、且你想要组织级治理（3 位具名维护者、约 314 个贡献者、发版持续到 2026）而不是个人仓库时，你选它而不是 [holehe](holehe.zh.md)/[socialscan](socialscan.zh.md)。它也是天然的教学样例：站点数据库就是一个可读的 JSON 文件，把用户名存在性探测的原理摊开给你看。

## 何时不用

- **你要的是档案，不是命中清单。** 用 [Maigret](maigret.zh.md)——ID 提取（socid-extractor）、递归搜索、HTML/PDF/XMind 报告、3000+ 站点。Sherlock 到「找到账户」为止。
- **不能容忍假阳性。** Sherlock 的个人页启发式（HTTP 状态码/错误文本匹配）在保留名和被删/被封账户上会失手——这正是 socialscan 的注册端点方法要修的问题。要在其覆盖的约 11 个平台拿「可用/已占用」判定，用 [socialscan](socialscan.zh.md)；查其他站点的存在性，用 Maigret 的结果和 Sherlock 交叉验证。
- **你的输入是邮箱。** 先用 [socialscan](socialscan.zh.md) 或复验过的 [holehe](holehe.zh.md) fork。
- **你手里的 handle 不是对方在别处用的那个。** Sherlock 把整轮扫描押在一个完全相同的字符串上，所以它只能覆盖「这个字符串被复用」的那部分站点；目标在别处另起了名字的那些平台，它看不见，而且加多少站点覆盖也修不了这一点。这时该换的是**键**，不是工具：改用 [socialscan](socialscan.zh.md)（约 11 个平台的服务端「可用/已占用」判定）或复验过的 [holehe](holehe.zh.md)（120+ 站点）去探邮箱，因为换到新平台还继续沿用的概率，地址远高于 handle。[推断]
- **你需要 Google 生态深度。** 用 [GHunt](ghunt.zh.md)。
- **你指望单 IP 安静地无人值守批量扫描。** Sherlock 没有自动更新的站点库，除了 Tor/代理参数外没有绕封锁机制；重度使用需要代理池（`proxy-pool` 类目），且 347 个 open issue 说明站点失效报告会排队。
- **对目标 handle 没有授权。** 与全类目相同的法律/ToS 边界。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Maigret](maigret.zh.md) | 已收录 | 交付物是档案（提取的 ID、递归、报告、3000+ 站点、Tor/I2P）时选 Maigret；交付物是跨 481 站点快速、简单、可审计的存在性清单时选 Sherlock。 | Maigret 用重 poetry 依赖栈和更慢的扫描换深度；Sherlock 用更粗的个人页信号和零提取换简单。 |
| [socialscan](socialscan.zh.md) | 已收录 | 能拿到邮箱、或需要约 11 个平台的注册级「可用/已占用」判定时选 socialscan；只有用户名、且要看这个字符串在 481 个站点哪里被复用时选 Sherlock。 | socialscan 用平台自己的判定替代个人页猜测，且接受邮箱这个跨平台更稳定的键；代价是覆盖平台少 40 倍。 |
| [holehe](holehe.zh.md) | 已收录 | 标识符是邮箱时选 holehe 系工具；是用户名时选 Sherlock——互补阶段，不是替代品。 | holehe 以邮箱为键且已弃养（2024-09）；Sherlock 以用户名为键、组织治理、发版活跃。 |
| [GHunt](ghunt.zh.md) | 已收录 | 要做认证式 Google 账户调查时选 GHunt；要做无认证宽域扫描时选 Sherlock。 | GHunt 用你的 cookie 看进单一生态内部（ToS 风险）；Sherlock 只看多站点的公开个人页表面。 |

## 技术栈

- **语言：** Python ^3.9，poetry-core 构建；以 `sherlock-project` 发布到 PyPI。
- **网络：** 同步 requests（配 certifi、PySocks 走 SOCKS/Tor）——没有异步栈，代码小而可读。
- **站点数据库：** 声明式 `data.json`（截至 2026-09 共 481 条），逐站记录个人页 URL 模式、错误信息匹配器和元数据；贡献者通过 PR 扩展。
- **输出：** 控制台、`--csv`、`--xlsx`、`--json`、逐站文件夹输出；`--browse` 打开找到的个人页。
- **治理：** GitHub 组织（sherlock-project），pyproject 里 3 位具名维护者；主页 sherlockproject.xyz。

## 依赖

- Python 3.9+；`pipx install sherlock-project` 或 `pip install sherlock-project`。运行时依赖极少（requests、colorama、PySocks、certifi、xlsx 用的 openpyxl 系）。
- 对 481 个站点的出站 HTTPS；`--tor`/`--unique-tor` 需要 Tor daemon；`--proxy` 需要 HTTP/SOCKS 代理。
- 无 API key、无数据库服务、无自建服务。

## 运维难度

**低。** 单命令运行、依赖集琐碎、站点库是一个可审计可钉住的 JSON 文件。持续成本在结果卫生：个人页启发式的命中需要人工复核（假阳性），平台变更会弄坏站点模块（盯 issue 队列），Tor/代理路径需要自己的运行时配置。站点库没有自动更新机制——修站点靠升级包。

## 健康度与可持续性

- **维护情况（2026-09）：** 活跃——v0.16.2 于 2026-09-08 发布，默认分支 2026-09-18 有 push；2024 年以来大约每年一个 minor（v0.15.0 2024-07、v0.16.0 2025-09）。
- **治理 / bus factor：** 本类目最强——GitHub 组织所有、3 位具名维护者、约 314 个贡献者、有文档化的贡献流程。不存在单人 bus factor。
- **年龄 × Lindy：** 创建于 2018-12（约 7.7 年）且仍在活跃发版——类目内最好的年龄×活跃信号。
- **采用信号：** 92k star / 10.8k fork——多数用户名 OSINT 教学材料以它为参照；被安全发行版打包。[未验证]
- **风险标记：** MIT 许可；347 个 open issue（多为站点失效报告）说明尽管发版活跃仍有分诊积压；同步设计限制了大规模扫描速度；启发式方法有结构性的假阳/假阴类别。

## 存疑（未验证）

- [未验证] 「被安全发行版打包」（如 Kali）未对照发行版软件包列表核实。
- [未验证] 未逐站实测模块健康度——只对 master 分支 `sherlock_project/resources/data.json` 点过 481 条总数。该文件顶层共 482 个键，其中一个是 `$schema` 元数据键，不是站点。
- [推断] 依据 socialscan 文档化的批评，保留名/被删名上的假阳性是个人页方法的结构性问题；Sherlock 当前确切错误率未测量。
- [推断] 「换到新平台还继续沿用的概率，地址远高于 handle」是从注册/找回密码端点以地址为键推断出的机制结论，不是实测比率——未找到可核对的逐平台 handle 复用率数据。
- [未验证] open issue 积压是否实质拖慢站点库修复，未评估。
