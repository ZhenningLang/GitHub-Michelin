---
name: nginx-upload-module
slug: nginx-upload-module
repo: https://github.com/fdintino/nginx-upload-module
category: nginx-modules
tags: [nginx, file-upload, multipart, c-module, web-server]
language: C
license: BSD-3-Clause
maturity: v2.3.0 tag line, low activity (last push 2024-07), ~1.0k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2024-07-17T20:13:04Z
  default_branch: master
  default_branch_sha: 96e64603dc5a588a2d1ae59a62b0019d6b41070c
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:44:22Z
  overall: "?"
  overall_score: null
  scored_axes: 2
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1189
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
        repo_age_days: 6483
        last_commit_age_days: 1189
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_traffic }
    adoption: { reason: ambiguous }
    governance: { reason: unattributable }
    risk_license: { reason: license_unparsed }
---

# nginx-upload-module

一个在服务器边缘处理 `multipart/form-data`（RFC 1867）文件上传的 NGINX C 模块——NGINX 自己把上传流式写到磁盘，只把文件元数据（路径、文件名、大小）传给你的后端，于是你的应用永远不必缓冲原始上传内容。

![nginx-upload-module — 健康度雷达](../../assets/health/nginx-upload-module.zh.svg)

## 何时使用

你有一个跑在 NGINX 后面、接受大文件上传的应用，你不想让应用服务器为了一个客户端用慢连接一点点吐上来的几个 GB 文件，而把一个 worker/线程占用好几分钟。你想让 NGINX——它本就擅长慢客户端 I/O——接收上传并缓冲到磁盘，然后给后端递一个极小的请求，只带已保存文件的路径、原始名、内容类型和大小。你把这个模块编进 NGINX，把 `upload_pass` 指向你的应用端点，配好 `upload_store` 目录，于是上传经 NGINX 落盘，而你的后端拿到的是一个干净、很小、描述该文件的表单 POST，而不是那堆字节本身。

当你需要**断点续传**（模块通过 `Content-Range` 支持一种可续传上传协议）或逐文件哈希/CRC32（让后端不必重读 payload 就能校验完整性）时，它也合适。经典用例是给一个 PHP/Python/Ruby 应用前面加一层上传层——那种应用本来会被大 multipart 体噎住——把重活卸给 NGINX，让应用保持无状态且快。

## 何时不用

- **低活跃、分叉的分叉血统——首要提醒。** 原模块（Valery Kholodkov 所作）已无人维护；这个 `fdintino` 分叉是事实上的延续，但它本身也**低活跃**（最后 push 2024-07，见健康度）。把一个老化的第三方 C 模块编进 NGINX，是一项实打实的维护与安全承诺——采用前请掂量。
- **你能把上传卸给对象存储。** 若客户端能用预签名 URL 直传 S3/GCS，你就完全省掉了上传层磁盘、NGINX 重编和清理问题。这是许多应用的现代默认。
- **你不愿意编译 NGINX。** 它是静态 C 模块（不保证跨版本动态加载）——你要把它编进 NGINX，并在每次 NGINX 升级时重新验证。若你想要纯配置或托管式安装，这就是摩擦。
- **你需要有维护、有厂商支持的路线。** 没有基金会/公司背书；若将来某个 NGINX 版本把它弄坏了，你可能得自己改 C。要有支持的大上传处理，NGINX 自带的 `client_body_*` 缓冲加上应用层的 chunked/tus 协议或许更稳。
- **现代续传/tus 工作流。** 要做稳健的断点续传，专门的 tus 服务器/实现比本模块的续传协议生态更活跃。[未验证]
- **你不打算管的磁盘生命周期。** 它把文件写到 NGINX 机器的 `upload_store`；清理、配额和各种失败态（半截文件、磁盘满）都归你。忘了这点就是运维地雷。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| NGINX `client_body_*` 缓冲 + 应用处理 | 未收录 | 第一方配置比把 multipart 解析从应用卸载出去更重要时，选 NGINX 内置缓冲。 | 更容易长期可用，但应用仍要解析上传，卸载程度不如本模块。 |
| 直传 S3 预签名上传 | 未收录 | 上传字节可以完全绕过你的服务器时，选 S3 预签名直传。 | 扩展性和持久性更好，但会把对象存储和客户端上传逻辑推给产品。 |
| [tusd](tusd.zh.md) | ✅ | 稳健续传上传和 SDK 生态比留在 NGINX 内更重要时，选 tusd。 | 它是独立服务而非 NGINX 模块，但更适合完整 tus 工作流。 |
| [lua-nginx-module](lua-nginx-module.zh.md) | ✅ | 只有当你需要通用 OpenResty 脚本，而不是专用流式 multipart 接收器时，才选 lua-nginx-module。 | 它是可编程边缘运行时，不是专门的上传卸载模块。 |
| 应用框架的上传处理 | 未收录 | 上传足够小，零额外基础设施比边缘卸载更重要时，选应用框架上传处理。 | Django/Rails/Express 能处理，但应用服务器要吸收慢客户端成本。 |

## 技术栈

- **语言：** C——编进服务器的 NGINX HTTP 模块。
- **协议：** 解析 `multipart/form-data`（RFC 1867）；通过 `Content-Range` 支持一种**可续传**上传协议。
- **集成：** 把上传文件流式写到磁盘上的 `upload_store` 目录，然后向 `upload_pass`（你的后端）发一个内部请求，把文件的路径/名/内容类型/大小（及可选的 CRC32/哈希）作为表单字段带上。
- **构建：** 在 NGINX `./configure --add-module=...` 时加入（静态）；动态模块构建对版本敏感。[未验证]

## 依赖

- **一棵用于编译的 NGINX 源码树**——模块编进 NGINX，而非独立加载。
- **本地磁盘**用于 `upload_store`（上传落地的暂存区）——以及它的清理策略。
- **一个后端**接收 `upload_pass` 请求——你自己跑。
- 模块本身**不需要外部服务或数据存储**。

## 运维难度

**中。** 配置直接（几个 `upload_*` 指令），但运维分量在两处。其一，**构建**：它是静态 C 模块，所以你要重编 NGINX 才能加它，并在**每次 NGINX 升级时重新验证**——而因为模块活跃度低，将来某个 NGINX API 变更可能要你自己改 C。其二，**磁盘生命周期**：上传文件落在 NGINX 主机的 `upload_store`；清理、磁盘满处理、中断上传的半截文件清理，以及任何配额，都归你。一旦编好并配上清理任务，它跑起来很安静，但升级/维护这条尾巴是团队最容易低估的部分。

## 健康度与可持续性

- **响应速度**：无法计算——no_data。
- **维护（2026-06）——低活跃。** 最后 push 在 **2024-07**（截至撰写约停滞 2 年）；tag 到 **v2.3.0**。未归档，但读起来是**维护态 / 低活跃**，而非积极开发。这个分叉正是因为上游停摆而存在——所以血统是「需要时续命」，而非生机勃勃。[推断]
- **治理 / bus factor。** `User` 所有（Frankie Dintino 对 Valery Kholodkov 原作的分叉）。一个约 1k star、`User` 所有、低活跃的 C 模块是**明确的 bus-factor 风险**——存续系于一个维护者是否还上心，且无组织背书。[推断]
- **年龄 × Lindy。** 血统很老（本仓库 **2008-12** 创建，约 17 年）——对*概念*和原始代码的 Lindy 很强，但**近期低活跃削弱了「仍活跃」那一半**：老而吃老本，而非老而兴旺。要把年龄 × 活跃度合看；这里活跃度是弱项。[推断]
- **采用度。** 历史上以 NGINX 上传卸载闻名（约 1k star、约 378 fork）；但向对象存储直传和专门 tus 服务器的现代趋势削弱了它的中心地位。许可为 **BSD-3-Clause**（读自 `LICENCE` 文件：© 2006, 2008 Valery Kholodkov，3 句 BSD 文本）。[推断]
- **风险标记。** 把老化、低活跃的第三方 C 编进你的 NGINX 是首要的安全/维护风险——将来某个 NGINX 版本可能弄坏它而没有厂商来修。未发现 relicense 历史。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 1.0k star / 约 55 open issue / 最后 push 2024-07 / tag 到 v2.3.0——易变，请重新核实。
- [未验证] 许可：GitHub API 报 `NOASSERTION`；仓库的 `LICENCE` 文件是 **3 句 BSD** 许可（© 2006, 2008 Valery Kholodkov——「Neither the name... may be used to endorse...」）——此处依据阅读该文件记为 BSD-3-Clause。
- [未验证] 可续传上传协议支持和 CRC32/哈希字段来自模块文档/特性列表；确切的当前行为和 NGINX 版本兼容性未对此处代码核实。
- [未验证] 对当前 NGINX 版本能否干净地做动态模块构建对版本敏感，未核实。
- [推断]「维护态 / 低活跃」与 bus-factor 结论由 push 时间 + 单一 `User` 所有者推断，而非官方项目状态声明。
