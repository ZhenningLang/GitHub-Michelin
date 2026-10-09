# nginx-modules

> 分类节点。NGINX / OpenResty 扩展模块（Lua、上传等）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **lua-nginx-module (ngx_lua)** | 当你需要在 NGINX 上用 LuaJIT cosocket 实现真正的逐请求可编程能力（鉴权、路由、限流）时用它——但一次阻塞调用就会卡死整个 worker，且你被绑定在 OpenResty 版本耦合、核心团队高度集中的生态上。 | A（4/6） | [→](lua-nginx-module.zh.md) |
| **lua-resty-redis** | 当你的 OpenResty 边缘逻辑要在请求热路径上非阻塞访问 Redis（带连接池和 pipeline）时用它——但它只能在 ngx_lua 内运行，且不内置 Redis Cluster 的槽位路由。 | B（3/6） | [→](lua-resty-redis.zh.md) |
| **nginx-upload-module** | 当 NGINX 后面的应用要接大文件 multipart 上传、你想让 NGINX 自己落盘、只把路径、文件名和大小交给后端时用它——但它是一个低活跃、单人维护的 C 分叉（最后提交 2023-06），每次升级 NGINX 都要重编。 | "?"（2/6） | [→](nginx-upload-module.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [lua-nginx-module (ngx_lua)](lua-nginx-module.zh.md) | ✅ | A（4/6） | 当你需要在 NGINX 上用 LuaJIT cosocket 实现真正的逐请求可编程能力（鉴权、路由、限流）时用它——但一次阻塞调用就会卡死整个 worker，且你被绑定在 OpenResty 版本耦合、核心团队高度集中的生态上。 |
| [lua-resty-redis](lua-resty-redis.zh.md) | ✅ | B（3/6） | 当你的 OpenResty 边缘逻辑要在请求热路径上非阻塞访问 Redis（带连接池和 pipeline）时用它——但它只能在 ngx_lua 内运行，且不内置 Redis Cluster 的槽位路由。 |
| [nginx-upload-module](nginx-upload-module.zh.md) | ✅ | "?"（2/6） | 换来应用 worker 不再被慢速大上传占住，还附带断点续传和逐文件哈希；代价是自编 NGINX、落盘文件的清理归你，NGINX 升级弄坏它时得自己改 C。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

**NGINX / OpenResty** 扩展模块。完整 API 网关见 `api-gateway`。
