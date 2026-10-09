# nginx-modules

> Category node. NGINX / OpenResty extension modules (Lua, upload, etc.).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **lua-nginx-module (ngx_lua)** | Use it when you need real per-request programmability on NGINX (auth, routing, rate-limit) via LuaJIT cosockets — but one blocking call stalls a worker, and you're bound to OpenResty's version-coupled, founder-concentrated core. | A (4/6) | [→](lua-nginx-module.md) |
| **lua-resty-redis** | Use it when your OpenResty edge logic must hit Redis non-blocking on the request hot path with pooling and pipelining — but it works only inside ngx_lua and has no built-in Redis Cluster slot-routing. | B (3/6) | [→](lua-resty-redis.md) |
| **nginx-upload-module** | Use it when your app behind NGINX takes huge multipart uploads and you want NGINX to land them on disk and pass only file metadata upstream — but it's a quiet single-maintainer C fork (last commit 2023-06) you must compile into NGINX. | "?" (2/6) | [→](nginx-upload-module.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [lua-nginx-module (ngx_lua)](lua-nginx-module.md) | ✅ | A (4/6) | Use it when you need real per-request programmability on NGINX (auth, routing, rate-limit) via LuaJIT cosockets — but one blocking call stalls a worker, and you're bound to OpenResty's version-coupled, founder-concentrated core. |
| [lua-resty-redis](lua-resty-redis.md) | ✅ | B (3/6) | Use it when your OpenResty edge logic must hit Redis non-blocking on the request hot path with pooling and pipelining — but it works only inside ngx_lua and has no built-in Redis Cluster slot-routing. |
| [nginx-upload-module](nginx-upload-module.md) | ✅ | "?" (2/6) | Frees app workers from slow multi-GB uploads and adds resumable uploads and per-file hashing; costs a custom NGINX build, disk cleanup you own, and patching C yourself if an NGINX release breaks it. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

**NGINX / OpenResty** extension modules. Full API gateways live in `api-gateway`.
