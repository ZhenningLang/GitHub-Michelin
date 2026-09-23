---
name: copyparty
slug: copyparty
repo: https://github.com/9001/copyparty
category: document-management
tags: [file-server, file-sharing, webdav, ftp, sftp, resumable-upload, dedup, media-indexer, self-hosted, mit]
language: Python
license: MIT
maturity: v1.20.16, active (2026-05); ~45k stars [未验证]
last_verified: 2026-06-26
type: app
upstream:
  pushed_at: 2026-06-26T18:46:37Z
  default_branch: hovudstraum
  default_branch_sha: 4c8203016f089b38281ed922a78255146f099e7b
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:16:39Z
  overall: B
  overall_score: 3.33
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
        last_commit_age_days: 2
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 1.8
        qualifying_issues: 47
        band: relaxed_solo
        window_offset_days: 8
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: copyparty
        dependent_repos_count: 1
        downloads_last_month: 8480
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
        homebrew_installs_90d: 786
        homebrew_tier: B
        release_downloads: 520234
        release_assets: 765
        release_tier: C
        signal_basis: homebrew+releases
        tier_source: homebrew+releases
    longevity:
      grade: A
      raw:
        repo_age_days: 2676
        last_commit_age_days: 2
        cohort: app
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 70
        top1_share: 0.823
        top3_share: 0.854
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

# copyparty

单文件、零必需依赖的便携文件服务器：自带加速断点续传、去重和媒体索引，可通过 HTTP、WebDAV、FTP/FTPS、SFTP、TFTP 和 SMB 访问。

![copyparty — 健康度雷达](../../assets/health/copyparty.zh.svg)

## 何时使用

你是一个小团队的 homelab 负责人，总需要一个地方来「丢文件」——把一批扫描件分享给同事、让不懂技术的客户在网络不稳的情况下也能传上来一个 4 GB 的视频、通过 WebDAV 暴露一个归档让手机能浏览，再给那台只会说 FTP 的老设备留一个 FTP/SFTP 入口。为这些事搭一整套 DMS 或 S3 体系太重了，你也不想仅仅为了搬运字节就装一个数据库加三个服务。你只需拷一个文件——`copyparty-sfx.py`（或者跑官方 Docker 镜像）——指向一个目录，定义几个按卷划分的读写用户，就得到一个浏览器可访问的服务器：带真正的上传 UI、能扛住断线的断点续传多线程上传（`up2k`/`u2c`），以及基于内容匹配的去重，让重复上传不会撑爆磁盘。内置索引器让目录树可按名称、路径、日期、大小和音频标签搜索，并为图片/视频/音频生成缩略图——所以面对一堆媒体和零散文件，它就是「起起来然后不用管」，没有 Postgres、没有 Redis、不用编译 Angular。

它还很适合做更重系统前面的「接收和传输」层：copyparty 的事件钩子（event hooks）和文件解析插件（file-parser plugins）能在每次上传时触发一个程序（移动、转码，或把文件交给真正的 DMS），所以你可以把它当作友好的上传前门，而由下游系统去做 OCR 和归档。

## 何时不用

- **你真正需要的是文档管理系统（OCR + 全文内容检索）。** copyparty 搜索的是*文件名、路径、日期、大小和音频（ID3）标签*——它**不**对扫描件做 OCR，也**不**对文档*内容*做全文索引。要「找出那张提到账号 1234 的发票」，请用 [paperless-ngx](paperless-ngx.zh.md) 或 [Twake Drive](twake-drive.zh.md)，而不是 copyparty。
- **你想要协同文档编辑 / Office 在线协作。** 它能提供文件服务并（对 Markdown）做轻量编辑，但不是 Drive/Office 套件的替代品。
- **你想要一个开箱即安全的公网服务。** 它很强且暴露很多协议；SMB 服务器被明确标注为不安全/慢、「不建议用于 wan」，把这么宽的协议面直接放到公网需要反向代理、TLS 和谨慎配置。它不是一键安全的云盘。
- **你需要文件夹*同步*（双向、Dropbox 式）。** 维护者明确表示永远不会支持完整同步——它是上传/下载/分发，不是同步引擎。
- **你需要生命周期/留存策略、审批流、电子签名、版本管理或审计轨迹。** 这些都不是目标；项目自述的理念是「do all the things, and do an *okay* job」，广度优先而非深度。
- **你需要细粒度、按文档的多租户隐私。** 权限是按卷/按用户的（读/写/移动/删除/管理/隐藏文件），不是按文档的 ACL。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [paperless-ngx](paperless-ngx.zh.md) | ✅ | 当任务是扫描件 OCR、自动打标和文档全文检索时，选 paperless-ngx；当决定性需求是轻量上传下载、多协议文件服务或作为接收前门时，保留 copyparty。 | 真正的 DMS：对扫描件做 OCR + 全文内容检索 + 自动打标，但是一套多容器的 Django/Postgres/Redis 栈。copyparty 完全没有这套 OCR/全文检索流水线；它是轻得多的文件服务器，不是文档归档库。 |
| [Twake Drive](twake-drive.zh.md) | ✅ | 当团队网盘、文档编辑、分享和更丰富权限值得承担平台重量时，选 Twake Drive；当只需要独立文件投递、传输和分发且不想绑定套件时，保留 copyparty。 | 协同云盘，带文档编辑、分享和更丰富的权限模型；运维更重。copyparty 是单文件的文件传输/分发，没有协同编辑，也没有按文档的 ACL。 |
| Nextcloud | 未收录 | 当你需要完整自托管云形态，包括同步客户端、应用、分享和协作能力时，选 Nextcloud；当便携性、协议广度和不依赖数据库比应用生态更重要时，保留 copyparty。 | 完整自托管「云」（文件、同步客户端、应用、分享、可经插件加 OCR），但是很重的 PHP/DB/Redis 栈。copyparty 轻得多、起得快得多，但没有双向同步，也没有应用生态。 |
| Seafile | 未收录 | 当可靠双向同步、增量同步和客户端应用是硬需求时，选 Seafile；当场景是临时上传和多协议文件服务、且明确不需要同步时，保留 copyparty。 | 基于块的同步分享，增量同步强、客户端齐全。copyparty 胜在便携/零依赖和协议广度（WebDAV/FTP/SFTP/TFTP/SMB），但没有真正的同步。 |
| Filebrowser | 未收录 | 当一个更简单的 Go 单二进制 Web 文件管理器已经够用时，选 Filebrowser；当加速断点续传、协议广度或媒体索引才是决定性功能时，保留 copyparty。 | 同类的轻量单二进制 Web 文件管理器（Go）。协议面更窄，没有 `up2k` 式的加速断点续传，也没有媒体索引；但更易理解。 |
| MinIO | 未收录 | 当程序和应用需要 S3 兼容对象存储时，选 MinIO；当需求是面向人的浏览器、WebDAV、FTP 或 SFTP 文件分享和接收时，保留 copyparty。 | S3 兼容对象存储，面向程序/应用访问。形态完全不同——copyparty 是面向人的多协议文件服务器，不是对象存储。 |

## 技术栈

- **语言：** Python（服务端）。浏览器 UI 是原生 JS/HTML/CSS（`up2k` 客户端上传器）。
- **存储/索引：** 普通文件系统；按卷一个 SQLite 数据库（`.hist/up2k.db`）用于文件索引 / 去重 / 标签。
- **协议：** HTTP(S)、WebDAV、FTP(S)、SFTP、TFTP、SMB/CIFS;zeroconf（mDNS/SSDP）发现。
- **可选加速器：** Pillow / pyvips / FFmpeg（缩略图 + 转码）、Mutagen / FFprobe（音频标签）、libraw/rawpy（RAW 缩略图）。全部可选——核心服务器仅靠 Python 即可运行。
- **可扩展性：** 事件钩子和文件解析插件（上传时运行外部程序以追加标签或触发下游处理）。

## 依赖

- **必需：** 仅一个 Python 解释器。项目自述「server only needs Python (2 or 3), all dependencies optional」。建议用现代 Python 3；旧的 Python 2 据称仍可运行 `[未验证]`。
- **可选（按功能开关）:** Pillow / pyvips / FFmpeg 用于缩略图与媒体转码；Mutagen 用于音频元数据；pyvips/libvips、rawpy/libraw 用于额外图像格式。
- **部署产物：** `copyparty-sfx.py`（单个自包含文件）、Windows `copyparty.exe`、官方 Docker 镜像，以及 Arch / Homebrew / NixOS 上的软件包。
- **基础设施：** 不需要外部数据库、消息中间件或其他服务——它确实是自包含的。

## 运维难度

**低**——常见场景：拷一个文件（或 `docker run`），给几个 flag 或一份小配置来定义卷和用户，就起来了——不用准备数据库、没有迁移、没有额外服务。当你（a）启用可选的媒体/缩略图/转码栈（这时要管理 FFmpeg/Pillow 版本），或（b）把它暴露到公网时，难度升到**低到中**：宽广的协议面（WebDAV/FTP/SFTP/TFTP/SMB）意味着你要自己负责 TLS、反向代理、真实 IP 处理，并锁紧风险较高的协议（SMB 被标注为不适合 WAN）。你需要自己备份被服务的目录和 `.hist` 索引。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 1.8 小时，基于 47 个 qualifying issues/PRs。
- **维护（2026-06）。** 发布频繁（v1.20.16，2026-05-26），最后 push 于 2026-06——处于**活跃**、快速迭代，未归档。[推断]
- **治理 / bus factor。** 这是最突出的标记：一个**单维护者、`User` 个人账号所有的仓库**（`9001/copyparty`），约 45k star。如此重的采用度压在一个人身上是实打实的 bus-factor 风险——一旦维护者离开，没有基金会或厂商接手。强主观、单作者的设计（如「永远不会支持同步」）正是其另一面。[推断]
- **年龄与 Lindy 判断。** 约 7 年（2019-05 创建）且仍在活跃维护 ⇒ **中等 Lindy** 信号——足够久、已证明耐用，但它的存续系于维护者本人而非某个机构。[推断]
- **采用度。** 在其细分领域很强（45k star，已打包进 Arch/Homebrew/NixOS、有官方 Docker），而这恰恰让 bus-factor 集中度更值得在意。[未验证]
- **风险标记。** MIT，未发现 relicense 或 open-core；宽广的协议面（SMB 被标注不适合 WAN）是面向公网时的*安全*隐患，与项目可持续性是两回事。[推断]

## 存疑（未验证）

- [未验证] 星标约 45.4k，来自本次一次性 `gh repo view` 拉取（2026-06-26）;GitHub 星标不可靠且与日期相关——仅作参考。
- [未验证] 最新发布 v1.20.16（「s6-ready」）据本次 GitHub API 于 2026-05-26 发布；仓库最后 push 于 2026-06-16。未归档，处于活跃维护。
- [推断] 「单文件 / 零必需依赖」反映项目自述（`copyparty-sfx.py` + 「all dependencies optional」）；当前发布版对应的最低 Python 3 版本未在抓取到的文档中钉死——若依赖某个具体解释器版本，请对照运行的发布版核实。
- [未验证] 搜索基于文件名/路径/日期/大小 + 音频标签；README 中未发现 OCR，也未发现文档全文内容索引——若内容检索是硬性要求，请对照当前文档核实。
- [未验证] 文件解析插件 / 事件钩子可运行外部程序来追加自定义标签或触发下游处理，但开箱即用的（非音频）媒体打标广度——如 EXIF、视频分辨率——在抓取到的文档中未清晰列举。
