# video-editing

> 分类节点。面向最终用户的非线性视频编辑器（NLE 应用）——用图形化时间线剪辑、裁剪、合成与导出，区别于编解码工具链与程序化渲染库。
> ← 返回[media-processing](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Concat** | 需要一款当下就能安装运行、原生、离线、可脚本化的类 CapCut 编辑器时用它——代价是仅有 25 天历史的 0.2.x beta 与单一维护者。 | C（5/6） | [→](concat.zh.md) |
| **OpenCut** | 想跟进或基于浏览器／WASM 重写架构开发时用它——不适用于需要可用编辑器的场景，因为仓库正在重写，能用的版本在已归档的 classic 仓库里。 | B（5/6） | [→](opencut.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Concat](concat.zh.md) | ✅ | C（5/6） | 需要原生 Rust 桌面／移动编辑器，自带 FFmpeg 与 Whisper 并暴露 API／CLI／server 时选它；代价是 beta 稳定性与单人 bus factor。 |
| [OpenCut](opencut.zh.md) | ✅ | B（5/6） | 想跟进或基于下一代浏览器／WASM 架构开发时选它；代价是重写期间该仓库不产出可用版本。 |
| CapCut（字节跳动） | 未收录 | — | 需要免费、打磨成熟并带云端 AI 的编辑器时选它；代价是闭源、账号绑定上传、Pro 付费墙且无法自托管。 |
| DaVinci Resolve | 未收录 | — | 一次性剪辑需要专业调色、遮罩与跟踪时选它；代价是庞大的专有应用与陡峭的学习曲线。 |

## 什么该放这里

带图形化时间线的面向最终用户的非线性视频编辑器——人用来剪辑的应用，而不是替人渲染的库。编解码／转码工具链与编辑框架归入 `video-audio`（FFmpeg、MLT、GStreamer）；程序化渲染引擎归入 `video-production`（Remotion、HyperFrames）。
