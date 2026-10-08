# quality-metrics

> 分类节点。感知媒体质量指标与基准测试工具。
> ← 返回[media-processing](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **SSIMULACRA2** | 当你要对照原图给 JPEG XL、AVIF 或 WebP 的编码参数排序，需要一个比 PSNR、SSIM 更贴近人眼评分的静态图分数时用它——但这个上游仓库自 2025-05 起已冻结，仍在维护的拷贝在 libjxl 里。 | C（3/6） | [→](ssimulacra2.zh.md) |
| **VMAF** | Netflix 的、获 Emmy 奖的感知视频质量指标——一个 C 库 `libvmaf`（外加一个 `vmaf` CLI 和一个 Python wrapper），用来评估失真/编码后的视频相对参考在人眼看来有多好，同时还实现了 PSNR、SSIM、MS-SSIM、PSNR-HVS、CIEDE2000 以及 CAMBI 色带检测器。 | B（5/6） | [→](vmaf.zh.md) |

## 什么该放这里

感知媒体质量指标与基准测试工具。
