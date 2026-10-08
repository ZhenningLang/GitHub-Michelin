---
name: sharp
slug: sharp
repo: https://github.com/lovell/sharp
category: image-processing
tags: [image-processing, nodejs, libvips, resize, image-conversion, library]
language: JavaScript
license: Apache-2.0
maturity: v0.35.5 (2026-09-27), active, ~32.7k stars (as of 2026-10)
last_verified: 2026-10-08
type: library
upstream:
  pushed_at: 2026-10-07T15:48:39Z
  default_branch: main
  default_branch_sha: cf6f3a376387e51df46d3688f1dcf34e93595d64
  archived: false
health:
  schema: 1
  computed_at: 2026-10-08T08:22:12Z
  overall: A
  overall_score: 3.5
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
        last_commit_age_days: 1
        active_weeks_13: 11
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 16.4
        qualifying_issues: 24
        band: default
        window_offset_days: 12
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: sharp
        dependent_repos_count: 178353
        downloads_last_month: 415812769
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.04
        release_downloads: 265770024
        release_assets: 618
        release_tier: A
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4797
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 9
        top1_share: 0.828
        top3_share: 0.967
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
# sharp

用户上传的是 1200 万像素的手机原图，你的 Node.js 应用原样吐出去，一个商品页在手机流量下要拉 40 MB 的 JPEG。sharp 让你在 Node 进程里用几行代码把图缩小、重新编码，底下由 C 库 libvips 干活，所以又快又省内存。

![sharp — 健康度雷达](../../../assets/health/sharp.zh.svg)

## 何时使用

你是写 JavaScript/TypeScript 的开发者，应用要处理图片：上传接口得给每张照片生成一张 320 像素缩略图和一张 1600 像素的 WebP，构建步骤要预先生成响应式图片集，或者某个 API 路由按请求实时转换。从 Node 里调 ImageMagick，意味着每台机器都要装系统包、每张图起一个进程；纯 JavaScript 的库装起来省事，可处理一张 4000×3000 的 JPEG 就把 CPU 吃满。用 sharp，`npm install sharp` 之后写一句 `sharp(input).resize({ width: 320 }).webp().toBuffer()`，活儿就在进程内由 npm 为你平台下载好的原生代码完成。

当需求是 **Node.js 服务内部的速度**时，你选它而不是 [ImageMagick](imagemagick.zh.md)——README 称缩放比 ImageMagick 最快的设置还快 4–5 倍，libvips 以流式、低内存的方式处理图片；当 CPU 时间比“不装原生二进制”更要紧时，你选它而不是 Jimp 这类纯 JS 库。你放弃的是格式广度：预编译二进制覆盖 JPEG、PNG、Ultra HDR、WebP、AVIF、TIFF、GIF 以及 SVG 输入，不含 PDF、PSD、RAW 和 HEIC。

## 怎么用起来

sharp 是一个 Node 包，真正处理像素的是底下的 C 库 **libvips**；sharp 通过 **Node-API**（Node 给原生扩展的稳定接口，所以 Deno 和 Bun 也能跑）把它包成一串可以链式调用的 JS 方法。`npm install` 时会从可选依赖 `@img/sharp-*` 里拉下适配你系统的 sharp + libvips 预编译二进制，大多数 macOS / Windows / Linux 机器不需要再装别的。你做的事很少：把图片（文件路径、Buffer 或流）交给 `sharp()`，链式写出要做什么（缩放、转格式、旋转、合成），最后说输出到文件还是 Buffer；解码、色彩空间和透明通道处理、缩放、编码都由 sharp 完成。没有服务、没有配置，就是一个函数库——像一间暗房，你递进去一张配方就行。

![sharp — 主干用户故事](../../../assets/flow/sharp.zh.svg)

<!-- flow-steps:begin (generated from flows/sharp.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：安装，自动下载适配本机的预编译二进制 — `npm install sharp` — 组件：`@img/sharp-* 预编译包`
2. **你**：把图片交给 sharp：文件路径、Buffer 或流 — `sharp('input.jpg')`
3. **你**：链式写出要做什么 — `.resize({ width: 200 }).jpeg({ mozjpeg: true })`
4. **你**：说明输出到哪里 — `.toFile('output.webp') · .toBuffer()`
5. **sharp**：libvips 解码原图 — 组件：`libvips`
6. **sharp**：缩放、转换，正确处理色彩空间和透明通道
7. **sharp**：编码成目标格式，交回文件或 Buffer

**价值**：几行代码把大图转成小而适合网页的图；README 称缩放比 ImageMagick 快 4–5 倍

</details>
<!-- flow-steps:end -->

## 何时不用

- **输入里有 HEIC、PDF、PSD 或相机 RAW。** 预编译二进制解不了这些，你得自己编一个带额外解码器的全局 libvips。格式杂七杂八的老档案，用 [ImageMagick](imagemagick.zh.md)；要在 AWS Lambda 上处理 HEIC，sharp 文档指向打包了定制构建的第三方 Layer。
- **你要把 HTML/CSS（分享卡片、发票）渲染成图片。** sharp 只变换已有的像素，没有排版引擎；用 [Screenshot Service](screenshot-service.zh.md) 或别的无头浏览器渲染器，需要的话再把产物交给 sharp。
- **你的运行时加载不了原生扩展。** sharp 需要支持 Node-API v9 的运行时（Node.js >= 20.9.0、Deno、Bun）；浏览器或没有 Node-API 的边缘平台跑不了。改用纯 JavaScript 的 Jimp（未收录），或者看看可选的 `@img/sharp-wasm32` WebAssembly 版本——它需要支持 Worker 多线程的 Wasm——是否适合你的平台。
- **你想要一个给多个应用共用的缩图服务。** 别自己拿 sharp 包一层 HTTP 服务，直接部署 imgproxy（未收录）：基于 libvips 的 Go 服务，自带 URL 签名和防解压炸弹检查。
- **你还卡在 Node.js 18，或者依赖已被删掉的选项。** v0.35.0（2026-06-10）去掉了 Node 18 支持，带了八项破坏性变更（删除 `install` 脚本、删除已废弃的 `failOnError`、`format.jp2k` 改名等）；包仍是 0.x，小版本升级也可能打破你的代码。迁移前先锁在 `0.34.x`。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [ImageMagick](imagemagick.zh.md) | ✅ | 在 Node.js 服务里缩放、转换常见网页格式，选 sharp；shell 和批处理任务要打开冷门格式（PDF、PSD、RAW）或需要 sharp 没有的操作，选 ImageMagick。 | ImageMagick 有 200 多种格式、命令行和长长的操作清单；代价是要装系统包、每次调用一个子进程、缩放更慢、解码器攻击面大得多。 |
| libvips | 未收录 | 不在 Node.js 上——Python（pyvips）、Go、Ruby、C 或 `vips` 命令行——就直接用 libvips，拿到同一个引擎；在 Node 上，sharp 就是该选的 libvips 绑定，因为它带预编译二进制和更顺手的链式 API。 | 同样的速度和内存表现，暴露的操作更多；但你得自己装 libvips，写更底层的 API。 |
| Jimp | 未收录 | 不允许原生二进制时（受限运行时、要求零依赖的包），选 Jimp；只要图片量稍大，就选 sharp，因为原生 libvips 远快于 JavaScript 的像素循环。 | 纯 JavaScript、MIT、没有原生安装问题；格式更少，每张图的 CPU 和内存开销更高。 |
| imgproxy | 未收录 | 多个应用都要按 URL 实时缩图时，部署 imgproxy；变换属于你自己的 Node 代码路径或构建步骤时，留在 sharp。 | 现成且加固过的 libvips 服务（URL 签名、图片炸弹检查）；多一个要运维的服务，也没有进程内 API。 |
| [Screenshot Service](screenshot-service.zh.md) | ✅ | 源头是 HTML/CSS 而不是图片时，用 Screenshot Service 这类无头浏览器渲染器；有了像素之后才轮到 sharp。 | 排版和网页字体有浏览器级还原度，代价是要跑 Chromium；sharp 便宜得多，但排不了页面。 |

## 技术栈

- **语言：** JavaScript API 加 TypeScript 类型定义；通过 Node-API 用 C++ 胶水层对接 **libvips**（C）。
- **引擎：** libvips（v0.35.5 要求 >= 8.18.7），按需计算、多线程；mozjpeg、libspng、libwebp、libheif（AVIF）等编解码器打包进预编译的 libvips。
- **二进制：** 按平台拆分的可选包（`@img/sharp-<os>-<arch>` + `@img/sharp-libvips-<os>-<arch>`），覆盖 macOS、Linux（glibc 与 musl）、Windows 和 FreeBSD（Wasm）；另有一个 WebAssembly 构建给其他运行时。
- **运行时 JS 依赖：** 只有 `@img/colour`、`detect-libc` 和 `semver`。

## 依赖

- **运行时：** Node.js >= 20.9.0（或支持 Node-API v9 的 Deno/Bun）。Linux 上 x64/ARM64 需要 glibc >= 2.28 或 musl >= 1.2.5；x64 还要求 CPU 支持 SSE4.2。
- **系统库：** 受支持平台上不需要——libvips 就在预编译包里。全局安装的 libvips 可选，Windows 上不支持。
- **从源码构建：** 只在不受支持的平台或需要定制 libvips 时才要；需要 C++17 编译器以及 `node-addon-api` 和 `node-gyp`。

## 运维难度

**低，但有三个打包陷阱。**（1）**跨平台安装：**`npm install` 只按当前机器挑二进制，所以在 macOS 上装好的 `node_modules` 放进 Linux 容器或 AWS Lambda 就跑不了；要么用 `--os/--cpu/--libc` 参数安装，要么在目标镜像里装，并且别让 webpack/esbuild/vite 把 sharp 打进包里（文档给了 `externals` 配置）。（2）**glibc Linux 上的内存：**默认的 glibc 分配器在长期运行的多线程负载下会产生碎片，所以 sharp 在这种环境会主动降低线程并发；文档推荐换 jemalloc，或者用基于 musl 的 Alpine 镜像。（3）**已知冲突：**在同一个 Windows 进程里同时加载 `canvas` 和 sharp，或在 Linux 的 Electron 里用 sharp，可能因库符号冲突而崩溃。

## 健康度与可持续性

- **维护（2026-10）：非常活跃。** 大约每月一个版本（v0.35.4 于 2026-08-26，v0.35.5 于 2026-09-27），每次先发候选版；紧跟 libvips 升级。
- **治理与巴士因子——这是风险。** 实际上是单人维护：Lovell Fuller 贡献了约 83% 的提交，仓库挂在个人账号下；雷达给治理打 D。libvips 的维护者（kleisauke）也参与贡献，部分抵消了这一点。
- **年龄与 Lindy：强。** 2013 年创建，13 年后仍在活跃开发，熬过了好几代 Node.js 和 libvips。
- **采用：极其广泛。** 评分器统计的最近一个月 npm 下载量为 415,812,769 次，依赖它的仓库有 178,353 个，已是 Node 图片处理生态的默认依赖。
- **风险信号。** Apache-2.0，无改许可证历史。13 年了还是 0.x，小版本会带破坏性变更（v0.35.0 有八项）；每次小版本升级前都要读变更日志。

## 存疑（未验证）

- [未验证] 比 ImageMagick/GraphicsMagick 缩放快 4–5 倍，是 README 自己的基准结论，本页没有实测。
- [未验证] 预编译 libvips 里编进了哪些编解码库（mozjpeg、libspng、libheif 等），依据的是 README 的格式清单和对 sharp-libvips 的一般了解，本轮没有读构建清单。
- [推断] “没有 Node-API 的边缘平台跑不了”是从 Node-API v9 这一要求推出来的，没有逐个平台实测。
- [未验证] Jimp 相对 sharp 的性能和格式覆盖本轮没有做基准对比。
