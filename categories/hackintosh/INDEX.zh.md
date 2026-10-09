# hackintosh

> 分类节点。在苹果从没卖过的 PC 硬件上跑 macOS——OpenCore 引导配置，以及让不受支持的硬件（首先是显卡）在它下面工作的内核扩展和驱动。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **NullMoth NVIDIA Driver for macOS** | 当一台跑 macOS 15 的 OpenCore PC 里只有图灵或更新的 GeForce 卡，而且保住这张卡比稳定更重要时用它——代价是一个只有两天历史、单一作者、只在一张 RTX 5060 上验证过的内核驱动，要放宽 SIP／AMFI／安全启动，许可证禁止商用。 | D（4/6） | [→](nvidia-macos-driver.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [NullMoth NVIDIA Driver for macOS](nvidia-macos-driver.zh.md) | ✅ | D（4/6） | Sequoia 下让图灵及之后的英伟达卡跑 Metal 的唯一途径；代价是未经验证的移植、放宽的 macOS 安全设置、只有二进制的发布和非商业许可证。 |
| AMD Radeon + WhateverGreen | 未收录 | — | 稳定的黑苹果显卡路线：苹果自己的驱动，安全设置保持开启；代价是换显卡，这张卡上也没了 CUDA。 |
| OpenCore Legacy Patcher | 未收录 | — | 在老款真 Mac 上恢复老显卡（开普勒时代）的加速；不覆盖图灵及之后的英伟达卡。 |
| 英伟达 Web Driver | 非仓库 | — | 英伟达的闭源驱动，macOS 10.13 High Sierra 和 Pascal 之后停更。 |

## 什么该放这里

任务是**让 macOS 在苹果不支持的机器上启动并驱动硬件**的项目：OpenCore 引导器及其配置工具，修补或替换驱动（显卡、声卡、USB、Wi-Fi）的内核扩展，以及 macOS 根本不支持的硬件的驱动。

不放这里：

- **在虚拟机里跑 macOS**——形状不同（是虚拟化层，不是引导链）；尚未收录。
- **任何 Mac 都能用的通用 macOS 工具**——见 `dev-utilities` 或 `disk-cleanup`。
