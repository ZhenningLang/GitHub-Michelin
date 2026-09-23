# nginx-modules

> Category node. NGINX / OpenResty extension modules (Lua, upload, etc.).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **lua-nginx-module (ngx_lua)** | Use it when you need real per-request programmability on NGINX (auth, routing, rate-limit) via LuaJIT cosockets — but one blocking call stalls a worker, and you're bound to OpenResty's version-coupled, founder-concentrated core. | D (5/6) | [→](lua-nginx-module.md) |
| **lua-resty-redis** | Use it when your OpenResty edge logic must hit Redis non-blocking on the request hot path with pooling and pipelining — but it works only inside ngx_lua and has no built-in Redis Cluster slot-routing. | D (4/6) | [→](lua-resty-redis.md) |
| **nginx-upload-module** | Use it when you want NGINX to stream large multipart uploads to disk and hand your backend just file metadata — but you're compiling an aging, single-maintainer C fork (last push 2024-07); direct-to-S3 presigned uploads often beat it now. | "?" (2/6) | [→](nginx-upload-module.md) |
| **tusd** | Use it when you need a robust, protocol-based resumable upload server that can stream to local disk or cloud storage — but it's a separate service, not an NGINX module, and may be overkill for small, reliable uploads. | B (6/6) | [→](tusd.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [lua-nginx-module (ngx_lua)](lua-nginx-module.md) | ✅ | D (5/6) | Use it when you need real per-request programmability on NGINX (auth, routing, rate-limit) via LuaJIT cosockets — but one blocking call stalls a worker, and you're bound to OpenResty's version-coupled, founder-concentrated core. |
| [lua-resty-redis](lua-resty-redis.md) | ✅ | D (4/6) | Use it when your OpenResty edge logic must hit Redis non-blocking on the request hot path with pooling and pipelining — but it works only inside ngx_lua and has no built-in Redis Cluster slot-routing. |
| [nginx-upload-module](nginx-upload-module.md) | ✅ | "?" (2/6) | Use it when you want NGINX to stream large multipart uploads to disk and hand your backend just file metadata — but you're compiling an aging, single-maintainer C fork (last push 2024-07); direct-to-S3 presigned uploads often beat it now. |
| [tusd](tusd.md) | ✅ | B (6/6) | Use it when you need a robust, protocol-based resumable upload server that can stream to local disk or cloud storage — but it's a separate service, not an NGINX module, and may be overkill for small, reliable uploads. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

**NGINX / OpenResty** extension modules. Full API gateways live in `api-gateway`.
