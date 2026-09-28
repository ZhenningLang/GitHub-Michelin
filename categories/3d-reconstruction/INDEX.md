# 3d-reconstruction

> Category node. Turn real-world photos, video or scans into 3D scenes you can view and edit — camera-pose solving (structure-from-motion), Gaussian-splatting and radiance-field training, and meshing of the result.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Spirula Studio** | Use it when you want video or photos to become a Gaussian splat and textured mesh in one unzip-and-run app on any-vendor GPU (Vulkan), with built-in SfM, masking and 360°/fisheye support — accepting a one-person maintainer and GPL-3.0. | C (6/6) | [→](spirula-studio.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Spirula Studio](spirula-studio.md) | ✅ | C (6/6) | Self-contained C++ desktop app + CLI: built-in SfM, AI masking, quantized splat training on Vulkan or CUDA, meshing — at the cost of a bus factor of one, a few-months-old product line and driver-specific crashes. |
| LichtFeld Studio · Brush · OpenSplat · gsplat | 未收录 | — | Open-source splat trainers (NVIDIA-only desktop app, WebGPU/browser trainer, LibTorch headless trainer, PyTorch research library) — weighed in Spirula Studio's comparison table, not added in this tab-intake batch. |
| COLMAP · Meshroom | 未收录 | — | Classic structure-from-motion and dense photogrammetry pipelines for measured geometry rather than splats — named in Spirula Studio's When NOT to use, not yet indexed. |

## What belongs here

Repositories whose primary job is **reconstructing 3D from real captures**: structure-from-motion and multi-view stereo, Gaussian-splatting / NeRF trainers, and the tools that turn their output into meshes. Not parametric solid modeling (see `cad`); not monocular depth models used as a component (see `ml-research`); not GIS map data (see `geospatial`).
