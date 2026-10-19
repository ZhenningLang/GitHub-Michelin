# render-engines

> 分类节点。你已有脚本、素材与制作方法，需要把代码合成渲染成视频。
> ← 返回 [video-production](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **fframes** | 当代码或 agent 写的动效视频要在自己的 GPU 上、不经浏览器快速渲染时用它——Rust + SVG 写帧、链接 libav 编码，每个项目自带给“看不见的作者”检查画面和响度的命令行；MIT 许可，但要原生工具链，1.0 在 2026-09-28 才发布，单人维护。 | B（4/6） | [→](fframes.zh.md) |
| **Remotion** | 当 React 优先的团队需要久经验证的程序化视频——composition 即 React 组件、带成熟 Lambda 云渲染——且接受 source-available 许可证（3 人以下公司免费）时用它。 | A（4/6） | [→](remotion.zh.md) |
| **HyperFrames** | 当你需要确定性、代码形态的视频——HTML composition 在 CI 里渲染成 MP4——并希望 agent skill 覆盖整条生产回路时用它；它是渲染引擎，不是生成式视频模型。 | B（6/6） | [→](hyperframes.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [fframes](fframes.zh.md) | ✅ | B（4/6） | Rust + SVG 写帧、Skia 在 GPU 上画、经链接的 libav 编码，带给 agent 用的 inspect／strip／audio analyze 命令；MIT，自测比 Remotion 最优配置快约 1.5 倍，代价是原生构建工具链、没有云渲染、1.0 仅两天、巴士因子为 1。 |
| [Remotion](remotion.zh.md) | ✅ | A（4/6） | React 组件式创作加成熟的 Lambda 渲染，但采用 source-available 许可、超公司规模阈值需付费；OpenMontage 内嵌的正是这一类引擎。 |
| [HyperFrames](hyperframes.zh.md) | ✅ | B（6/6） | 确定性的 HTML 转 MP4 渲染，带 20 个 agent skill，Apache-2.0 许可；它是引擎层，不是带治理的管线，也不是生成式画面。 |

## 什么该放这里

用代码定义合成并渲染帧的引擎，包括 HTML、React 和 Rust/SVG 路线。导演技能、制作管线与成品创作应用留在 [video-production](../INDEX.zh.md)。传统编解码与非线性剪辑自动化走 [media-processing](../../media-processing/INDEX.zh.md)。
