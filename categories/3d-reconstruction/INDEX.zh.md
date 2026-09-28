# 3d-reconstruction

> 分类节点。把真实世界的照片、视频或扫描变成可查看、可编辑的三维场景——相机位姿求解（运动恢复结构）、高斯泼溅与辐射场训练，以及把结果转成网格。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Spirula Studio** | 当你想把视频或照片在一个解压即用的程序里变成高斯泼溅和带贴图的网格、任意厂商 GPU 都能跑（Vulkan）、自带 SfM、抠图和全景／鱼眼支持时用它——代价是只有一位维护者和 GPL-3.0。 | C（6/6） | [→](spirula-studio.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Spirula Studio](spirula-studio.zh.md) | ✅ | C（6/6） | 自包含的 C++ 桌面程序 + 命令行：内置 SfM、AI 抠图、Vulkan 或 CUDA 上的量化泼溅训练、网格提取——代价是巴士因子为一、产品线只有几个月大、特定驱动会崩溃。 |
| LichtFeld Studio · Brush · OpenSplat · gsplat | 未收录 | — | 开源泼溅训练器（仅 NVIDIA 的桌面程序、WebGPU／浏览器训练器、基于 LibTorch 的无界面训练器、PyTorch 研究库）——已在 Spirula Studio 的对比表里权衡，本轮标签页收录批次未添加。 |
| COLMAP · Meshroom | 未收录 | — | 经典的运动恢复结构与稠密摄影测量管线，产出可度量的几何而非 splat——在 Spirula Studio 的“何时不用”里点名，尚未收录。 |

## 什么该放这里

第一职责是**从真实采集重建三维**的仓库：运动恢复结构与多视图立体、高斯泼溅／NeRF 训练器，以及把它们的输出转成网格的工具。不含参数化实体建模（见 `cad`）；不含作为组件使用的单目深度模型（见 `ml-research`）；不含 GIS 地图数据（见 `geospatial`）。
