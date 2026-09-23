---
name: paperless-ngx
slug: paperless-ngx
repo: https://github.com/paperless-ngx/paperless-ngx
category: document-management
tags: [dms, ocr, self-hosted, django, angular, full-text-search, document-archive, homelab, tesseract, gplv3]
language: Python (backend) + TypeScript/Angular (frontend)
license: GPL-3.0
maturity: Mature, active; stable v2.20.x (2026-04), v3.0 in beta as of 2026-06 (see caveats)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T01:18:26Z
  default_branch: dev
  default_branch_sha: 67972a074070c7a7677b423c50a7627c5fbfd060
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:16:53Z
  overall: B
  overall_score: 2.83
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.2
        qualifying_issues: 38
        band: relaxed_solo
        window_offset_days: 13
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: null
        canonical_package: null
        release_downloads: 324957
        release_assets: 100
        release_tier: C
        signal_basis: releases
    longevity:
      grade: A
      raw:
        repo_age_days: 1683
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 50
        top1_share: 0.658
        top3_share: 0.947
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: D
      raw:
        spdx_id: GPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
---

# paperless-ngx

一套自托管文档管理系统（DMS），基于 Django + Angular，配合 PostgreSQL/Redis，把账单、发票、信件等纸质/扫描件自动 OCR、打标签、建索引并提供全文检索。

![paperless-ngx — 健康度雷达](../../assets/health/paperless-ngx.zh.svg)

## 何时使用

你是一家两人会计事务所里那个“顺带管 IT”的人，事务所开在一间空出来的房间里，而文件柜终于把你逼到了墙角：好几年的发票、水电账单、客户信件和收据都塞在纸质文件夹里，每次客户问“我三月那份对账单你到底收到没有？”，你都得翻二十分钟活页夹。办公室网络的角落里本来就摆着一台小 Linux 机器 / NAS 在嗡嗡运转，你只想让每一张扫描件都落到一个真正能搜得到的地方。

于是你用它 Docker 优先的 compose 栈把 paperless-ngx 跑起来，把扫描仪对准 consume 文件夹。现在你把一批扫描件丢进去，paperless 就对它们做 OCR，并按匹配规则自动套上标签、通信方（correspondent）和文档类型——于是那份三月对账单不再需要翻柜子，在 Web UI 里做一次全文检索就能找到。因为这台机器就待在你受信任的内部办公网络上，文档规模也处于个人到小团队级别，这正是 paperless 为之而生的“扫描、归档、然后忘掉”那类活——你并不会去编辑这些文档、也不会把它们送去走审批，只是想让这一堆已完成的纸质文件变得能被找到。

## 何时不用

- **不是安全/合规存储库**——文档以明文形式存储在磁盘上，全文以明文存入数据库，文件名也不加密。内置文档加密功能已被移除（paperless-ng 0.9，v3 再次移除），并且 `[未验证]` 据称维护者表示没有添加静态加密的计划。磁盘级加密得你自己来。
- **不要跑在不可信/共享主机上**——项目明确警告反对这样做。
- **不适合严格的多租户 / 逐文档隐私**——权限/归属模型存在已知缺口（例如经 consume 文件夹导入的文档可能没有 owner，从而对所有用户可见）。它不是一套加固过的多用户系统。
- **不是企业级 EDMS**——没有内置的多步审批工作流、生命周期/留存管理或电子签名（这些请用 Mayan EDMS）。
- **不适合协作撰写/编辑**——它是*已完成*文档的档案库，而非 Google Docs 的替代品。
- **弱硬件上做大批量 OCR 体验差**——OCR 和自动匹配都吃 CPU/RAM；文档自身就建议在受限设备（树莓派等）上削减 worker 数、只处理首页、禁用 NLTK。
- **不支持 Windows**（需要 Linux 主机）。
- **升级锁定 / 维护风险**——社区维护，无商业方背书；大版本会带来重大破坏性变更（v3 移除 API v1、重建 migrations、改动 pre/post-consume 脚本参数）。升级前请锁定版本并阅读 release notes。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| Mayan EDMS | 未收录 | 当工作流、版本管理和企业级细粒度权限是硬需求时，选 Mayan EDMS；当个人或小团队扫描归档更看重 OCR/检索自动化且运维必须保持中等复杂度时，选 paperless-ngx。 | 同样是 Python/Django，但属于更重的企业级 EDMS，带有真正的工作流引擎、版本管理和细粒度权限；运维陡峭得多，对个人扫描档案库而言是杀鸡用牛刀。Apache-2.0（比 paperless 的 GPLv3 更宽松）。 |
| Docspell | 未收录 | 当你要的是邮件优先的收件箱和元数据抽取工作流时，选 Docspell；当 Docker 优先的扫描件归档和更大的自托管 DMS 社区更重要时，保留 paperless-ngx。 | 收件箱/元数据抽取模型，邮件导入能力强；Scala/JVM 技术栈意味着更重的内存占用，社区也比 paperless-ngx 小。 |
| Teedy / sismics docs | 未收录 | 当 Java 技术栈、文档版本管理和适中的资源需求优先时，选 Teedy；当 OCR 和自动打标签才是决定性功能时，保留 paperless-ngx。 | 轻量级 Java DMS，带版本管理、界面干净、资源需求适中；自动 OCR/自动打标签较弱，势头也较小。 |
| OpenDocMan | 未收录 | 只有当你要在既有 PHP 栈上做基础企业文件管控时，才选 OpenDocMan；当核心任务是可检索的 OCR 归档时，保留 paperless-ngx。 | 面向企业文件管控和访问规则的 PHP/MySQL DMS；界面陈旧，没有一流的 OCR/自动打标签——仅当你需要在既有 PHP 栈上做简单 Web 访问控制时才考虑。 |
| 自建（Tesseract + Meilisearch/Elasticsearch + 对象存储） | 未收录 | 只有当加密、schema 或安全约束让 paperless-ngx 不可接受时，才自建；否则 paperless-ngx 已经提供维护中的 ingest/OCR/index/UI 流水线。 | 灵活性最高，对加密/schema 完全掌控，但你得自行搭建并维护整条 ingest/OCR/index/UI 流水线——只有当 paperless 的数据模型或安全约束成为硬伤时才值得。 |

## 技术栈

- Python、Django（后端）；Angular、TypeScript（前端）
- PostgreSQL（推荐）；支持 SQLite 或 MariaDB
- Redis / Valkey（消息代理）
- Tesseract OCR、ImageMagick
- Apache Tika + Gotenberg（可选——Office/HTML 格式）
- Whoosh（搜索，v2）→ Tantivy（搜索，v3）
- Docker / docker-compose

## 依赖

- **PostgreSQL**（推荐；也支持 SQLite 或 MariaDB）
- **Redis 或 Valkey**（必需的消息代理）
- **Tesseract OCR** 4.0.0+ 及语言包
- **ImageMagick** 6+
- **Apache Tika + Gotenberg**——仅在需要导入 Office/非 PDF 格式时
- **Docker + docker-compose**（推荐的部署方式）
- **Linux 主机**（不支持 Windows）；裸机安装时，v3 线上为 Python 3.11–3.14 `[未验证]`（据称 v2.20.x 稳定线仍支持 Python 3.10+）

## 运维难度

**中等。** 多容器 docker-compose 栈（web + worker + Redis + DB，处理 Office 文档还需加 Tika/Gotenberg）。配置完成后日常运维很轻，但是：OCR 吃 CPU/RAM，在低功耗硬件上很慢；数据库和文档/媒体卷的备份都得你自己负责；大版本升级带破坏性变更（v3 移除 API v1、放弃 Python 3.10、重建 migrations、改动 consume 脚本），因此升级需要阅读 release notes。绝不能暴露在不可信主机上。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 1.1 小时，基于 53 个 qualifying issues/PRs。
- **维护（2026-06）。** 最后 push 于 2026-06；稳定的 v2.20.x 线加上正在推进的 v3.0 beta——处于**活跃**开发，未归档。极低的 open issue 数（约 6）显示积极的 triage，而非停滞。[推断]
- **治理 / bus factor。** 由 `paperless-ngx` 组织社区维护——它本身就是原 `paperless`/`paperless-ng` 谱系停滞后的社区延续，这点让人安心（项目**已经**挺过一次维护者交接），但它**没有商业方背书**；存续依赖志愿者的延续性。[推断]
- **年龄与 Lindy 判断。** 作为 `paperless-ngx` 约 4 年（2022-02 创建），经由前身有更深的根基 ⇒ **中等 Lindy** 信号——在 homelab/DMS 细分领域已被验证，但比底层的 paperless 理念年轻。[推断]
- **采用度与生态。** 很强（约 42k star，是自托管 DMS 的默认推荐，按 Docker 优先方式打包）——一个健康、被广泛部署的项目。[未验证]
- **风险标记。** GPL-3.0（未发现 relicense）。真正的标记是**升级锁定 / 破坏性变更**（v3 移除 API v1、重建 migrations、改动 consume 脚本）以及安全姿态（静态明文、权限模型缺口）——升级前锁版本并阅读 release notes。[推断]

## 存疑（未验证）

- **Star 数**——42.5k，来自单次抓取 GitHub 仓库页面（2026-06），未与 API 交叉核对。`[未验证]`
- **Release 版本/日期**——v2.20.15（约 2026-04-27）和 v3.0.0-beta.rc1（约 2026-05-05）来自搜索聚合器（releasebot/newreleases），本次未在 GitHub releases 页面上确认。`[未验证]`
- **v3 特性清单**——tantivy 后端、本地「Paperless AI」、文档版本、OCR 插件框架、移除 API v1、放弃 Python 3.10、consume 脚本变更——取自对 v3 beta 的搜索摘要，而非完整 release notes。`[未验证]`
- **Gotenberg**——基于 `-tika` 的 compose 文件被列为可选配套组件；在抽取出的安装文档中未明确确认。`[未验证]`
- **资源需求**——「吃 CPU/RAM」是根据文档中省资源指引得出的定性判断；官方未发布最低 RAM/CPU 规格。`[未验证]`
