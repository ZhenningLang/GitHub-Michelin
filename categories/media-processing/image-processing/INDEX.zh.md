# image-processing

> 分类节点。图像处理、转换、缩放、合成、格式工具与 HTML 转图片渲染。
> ← 返回[media-processing](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **ImageMagick** | 使用覆盖 200 多种格式的通用命令行套件与 API，创建、编辑、合成和转换图像。 | B（5/6） | [→](imagemagick.zh.md) |
| **sharp** | 通过 libvips 构建高吞吐的 Node.js 位图缩放与格式转换管线。 | A（6/6） | [→](sharp.zh.md) |
| **Screenshot Service** | 通过可隔离、可加固的小型内部 HTTP 服务，把受控 HTML 与 CSS 渲染成 PNG、JPEG 或 WebP。 | D（4/6） | [→](screenshot-service.zh.md) |
| **Magpie** | 在不注入进程的前提下，用 GPU 滤镜（FSR、Anime4K、CRT）把小的或不支持高 DPI 的 Windows 游戏／程序窗口实时放大到全屏。 | B（6/6） | [→](magpie.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [ImageMagick](imagemagick.zh.md) | ✅ | B（5/6） | 需要广泛格式覆盖、命令行自动化与通用图像合成时选它；它不如 sharp 适合 Node.js 热路径，也不能像浏览器一样排版任意 HTML。 |
| [sharp](sharp.zh.md) | ✅ | A（6/6） | 需要在 Node.js 进程内高速处理已有图片时选它；它避开 Chromium 开销，但不能渲染 HTML、CSS 或 Web font。 |
| [Screenshot Service](screenshot-service.zh.md) | ✅ | D（4/6） | 只有可信 HTML 经隔离内部 endpoint 处理时才选它；浏览器保真度的代价是 Chromium 成本、不安全默认值、仓库许可证未确立，以及大量加固工作。 |
| [Magpie](magpie.zh.md) | ✅ | B（6/6） | 需要不注入进程、带画质滤镜地实时放大某一个 Windows 窗口时选它；它是 GUI 应用而不是库，只支持 Windows，没有 HDR 和补帧，发版也落后于活跃的 dev 分支。 |
| Browserless | 未收录 | — | 需要带队列、并发与 session 控制的共享 headless browser 服务时选它；代价是更大的运维面和 SSPL／商业许可约束。 |
| capture-website-cli | 未收录 | — | 需要通过 CLI 一次性或脚本化截取网页，并使用丰富截图参数时选它；它比运营 API 服务简单，但不提供池化、多租户或持久渲染 endpoint。 |

## 什么该放这里

图像处理、转换、缩放、合成、格式工具、HTML 转图片渲染，以及对正在运行的桌面窗口做实时放大。通用浏览器自动化应归入 `web-automation`；以文档转 PDF 为主的工具应归入文档或 PDF 分类。
