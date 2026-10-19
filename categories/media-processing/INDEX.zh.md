# media-processing

> 分类节点。对图像、音频和视频进行解码、编码、转码、过滤与质量评分。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 分类 | 何时用 | 路由 |
|---|---|---|
| **video-audio** | 应用层之下的音视频工具——编解码／转码管线、程序化剪辑与剪切、语音与字幕（三个子分类）。 | [→](video-audio/INDEX.zh.md) |
| **video-editing** | 面向最终用户的非线性视频编辑器（NLE 应用）——图形化时间线剪辑，位于编解码工具链之上的应用层。 | [→](video-editing/INDEX.zh.md) |
| **nle-automation** | 对已安装的视频编辑器做程序化控制——生成、修改并经由编辑器自身引擎无界面导出它的原生工程／草稿文件。 | [→](nle-automation/INDEX.zh.md) |
| **image-processing** | 图像处理、转换、缩放与格式工具。 | [→](image-processing/INDEX.zh.md) |
| **quality-metrics** | 感知媒体质量指标与基准测试工具。 | [→](quality-metrics/INDEX.zh.md) |

## 项目

- [Jasna](jasna.zh.md) — 本地追踪并修复视频马赛克；免费 BasicVSR++ 路径源码公开，官方包含私有支持者组件。

## 对比矩阵

| 项目 | 何时用 | 主要约束 | 健康度 |
|---|---|---|---|
| [Jasna](jasna.zh.md) | 移动马赛克区域需要检测、跟踪与时序修复一起工作。 | 显卡专用环境、混合组件许可与不透明支持者运行时。 | C（6/6） |

## 什么该放这里

对图像、音频和视频进行解码、编码、转码、过滤与质量评分。
