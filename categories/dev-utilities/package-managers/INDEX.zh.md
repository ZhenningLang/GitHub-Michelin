# package-managers

> 分类节点。命令行包管理器本身——在你的机器上解析、下载、安装并链接软件包的那个工具（驱动它的桌面图形前端在 [package-manager-gui](../package-manager-gui/INDEX.zh.md)）。
> ← 返回 [dev-utilities](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **zerobrew** | 当你经常重装同一批 Homebrew 命令行 formula，想让一个和 `brew` 并排的 Rust 客户端把同样的 bottle 快几倍地装上时用它——但它是实验性的，不执行 `post_install`，cask 只支持带二进制产物的。 | B（6/6） | [→](zerobrew.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [zerobrew](zerobrew.zh.md) | ✅ | B（6/6） | 用的是 Homebrew 自己的目录和 bottle，只重定位一次、存进内容寻址仓库，重装就是克隆——代价是项目年轻、近期几乎由一人维护、不跑 post-install、不支持 `.app` cask。 |

zerobrew 页面里提到、但尚未收录的：Homebrew 本身（`Homebrew/brew`）、nanobrew、pkgx、Nix 和 MacPorts。

## 什么该放这里

包管理器本身——解析依赖、把软件包装进某个前缀的命令行工具，不论它读的是哪个生态的包目录。包装它的图形前端放 `package-manager-gui`；语言专属的依赖管理器（pip／uv、npm）跟各自语言的工具放在一起。
