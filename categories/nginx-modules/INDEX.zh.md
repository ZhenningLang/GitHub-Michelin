# nginx-modules

> 分类节点。NGINX / OpenResty 扩展模块（Lua、上传等）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **lua-nginx-module (ngx_lua)** | 当你需要在 NGINX 上用 LuaJIT cosocket 实现真正的逐请求可编程能力（鉴权、路由、限流）时用它——但一次阻塞调用就会卡死整个 worker，且你被绑定在 OpenResty 版本耦合、核心团队高度集中的生态上。 | D（5/6） | [→](lua-nginx-module.zh.md) |
| **lua-resty-redis** | 当你的 OpenResty 边缘逻辑要在请求热路径上非阻塞访问 Redis（带连接池和 pipeline）时用它——但它只能在 ngx_lua 内运行，且不内置 Redis Cluster 的槽位路由。 | D（4/6） | [→](lua-resty-redis.zh.md) |
| **nginx-upload-module** | 当你想让 NGINX 把大文件 multipart 上传直接落盘、只把文件元数据交给后端时用它——但你在编译一个老化、单人维护的 C 分叉（末次提交 2024-07），如今直传 S3 预签名上传往往更优。 | "?"（2/6） | [→](nginx-upload-module.zh.md) |
| **tusd** | 当你需要一个基于协议的稳健断点续传上传服务器，能把文件流式写到本地磁盘或云存储时用它——但它是独立服务，不是 NGINX 模块，对小文件/可靠网络可能过度设计。 | A（5/6） | [→](tusd.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [lua-nginx-module (ngx_lua)](lua-nginx-module.zh.md) | ✅ | D（5/6） | 当你需要在 NGINX 上用 LuaJIT cosocket 实现真正的逐请求可编程能力（鉴权、路由、限流）时用它——但一次阻塞调用就会卡死整个 worker，且你被绑定在 OpenResty 版本耦合、核心团队高度集中的生态上。 |
| [lua-resty-redis](lua-resty-redis.zh.md) | ✅ | D（4/6） | 当你的 OpenResty 边缘逻辑要在请求热路径上非阻塞访问 Redis（带连接池和 pipeline）时用它——但它只能在 ngx_lua 内运行，且不内置 Redis Cluster 的槽位路由。 |
| [nginx-upload-module](nginx-upload-module.zh.md) | ✅ | "?"（2/6） | 当你想让 NGINX 把大文件 multipart 上传直接落盘、只把文件元数据交给后端时用它——但你在编译一个老化、单人维护的 C 分叉（末次提交 2024-07），如今直传 S3 预签名上传往往更优。 |
| [tusd](tusd.zh.md) | ✅ | A（5/6） | 当你需要一个基于协议的稳健断点续传上传服务器，能把文件流式写到本地磁盘或云存储时用它——但它是独立服务，不是 NGINX 模块，对小文件/可靠网络可能过度设计。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

**NGINX / OpenResty** 扩展模块。完整 API 网关见 `api-gateway`。
