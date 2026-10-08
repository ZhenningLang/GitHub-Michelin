# image-processing

> 分类节点。图像处理、转换、缩放、合成、格式工具与 HTML 转图片渲染。
> ← 返回[media-processing](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **ImageMagick** | 当脚本或 CI 任务要用一条 shell 命令把 TIFF、PSD、EPS、HEIC、多页 PDF 等 200 多种格式转换、缩放、合成时用它——但不加隔离就去解码不可信的上传图片，CVE 风险源源不断。 | B（5/6） | [→](imagemagick.zh.md) |
| **sharp** | 当 Node.js 的上传处理、构建步骤或 API 路由要在进程内快速把大图转成缩略图和 WebP/AVIF 时用它——但它的预编译二进制解不了 HEIC、PDF、PSD 和相机 RAW。 | A（6/6） | [→](sharp.zh.md) |
| **Screenshot Service** | 通过可隔离、可加固的小型内部 HTTP 服务，把受控 HTML 与 CSS 渲染成 PNG、JPEG 或 WebP。 | D（4/6） | [→](screenshot-service.zh.md) |
| **Magpie** | 在不注入进程的前提下，用 GPU 滤镜（FSR、Anime4K、CRT）把小的或不支持高 DPI 的 Windows 游戏／程序窗口实时放大到全屏。 | B（6/6） | [→](magpie.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [ImageMagick](imagemagick.zh.md) | ✅ | B（5/6） | 格式覆盖最广、命令行可脚本化、各语言都有绑定；代价是解码器攻击面极大、缩放比 sharp 慢，开发集中在两位维护者身上。 |
| [sharp](sharp.zh.md) | ✅ | A（6/6） | 一句 npm install 就拿到 libvips 的速度和低内存；代价是预编译格式集窄、运行时必须能加载 Node-API 原生扩展，项目实际上只靠一位维护者。 |
| [Screenshot Service](screenshot-service.zh.md) | ✅ | D（4/6） | 只有可信 HTML 经隔离内部 endpoint 处理时才选它；浏览器保真度的代价是 Chromium 成本、不安全默认值、仓库许可证未确立，以及大量加固工作。 |
| [Magpie](magpie.zh.md) | ✅ | B（6/6） | 需要不注入进程、带画质滤镜地实时放大某一个 Windows 窗口时选它；它是 GUI 应用而不是库，只支持 Windows，没有 HDR 和补帧，发版也落后于活跃的 dev 分支。 |
| Browserless | 未收录 | — | 需要带队列、并发与 session 控制的共享 headless browser 服务时选它；代价是更大的运维面和 SSPL／商业许可约束。 |
| capture-website-cli | 未收录 | — | 需要通过 CLI 一次性或脚本化截取网页，并使用丰富截图参数时选它；它比运营 API 服务简单，但不提供池化、多租户或持久渲染 endpoint。 |

## 什么该放这里

图像处理、转换、缩放、合成、格式工具、HTML 转图片渲染，以及对正在运行的桌面窗口做实时放大。通用浏览器自动化应归入 `web-automation`；以文档转 PDF 为主的工具应归入文档或 PDF 分类。
