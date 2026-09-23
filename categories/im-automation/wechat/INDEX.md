# wechat

> Category node. WeChat bots and account tooling — personal-account puppets, client injection, official-channel bridges, and the frameworks behind them.
> ← back to [im-automation](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **ItChat** | Study it only as legacy WeChat-bot code — abandoned, and the web protocol it relies on is defunct, so it mostly doesn't work. | C (4/6) | [→](itchat.md) |
| **WeChatPlugin-MacOS** | Avoid for current WeChat — a macOS WeChat.app binary tweak that breaks on every WeChat update and is ~2y idle; account-ban & security risk. | D (4/6) | [→](wechatplugin-macos.md) |
| **wxpy** | Study it only as legacy WeChat-bot code — archived since 2019 and built on the now-defunct WeChat web protocol, so it mostly doesn't work. | D (5/6) | [→](wxpy.md) |
| **wxappUnpacker** | Use it when you must decompile a WeChat .wxapkg bundle you own back into readable source — but this exact repo is an empty tombstone, so grab a live fork instead. | E (3/6) | [→](wxappunpacker.md) |
| **WeChat Bot** | Use it for a maintained multi-channel Node.js CLI with many LLM backends and local chat analysis, only if you accept that its unofficial personal-WeChat path can trigger warnings or bans. | B (5/6) | [→](wechat-bot.md) |
| **ChatGPT-wechat-bot** | Use it only as a compact 2022–2023 Wechaty/ChatGPT reference; it is stale, hard-codes an old model path, and exposes a personal WeChat account to unofficial-puppet risk. | D (3/6) | [→](chatgpt-wechat-bot.md) |
| **Dify Enterprise WeChat Bot** | Use it only for an isolated Windows prototype pinned to a specific Enterprise WeChat client; the message path includes a closed binary, Workflow support is unfinished, and the project is stale. | C (3/6) | [→](dify-enterprise-wechat-bot.md) |
| **Wechaty** | Use it when you want to own the adapter and command layer of a personal-account bot in TS/Python/Go/Java — check each provider's current status first, and accept puppet risk. | C (5/6) | [→](wechaty.md) |
| **CowAgent** | Use it for a Python-first, multi-channel assistant with pluggable model backends; it is the renamed `zhayujie/chatgpt-on-wechat`, so the current channel adapter is iLink rather than the deleted personal-account path. | B (5/6) | [→](cowagent.md) |
| **WeChatFerry** | Do not deploy it — the maintainer archived the repository, releases are pinned to an old Windows WeChat build, and the whole approach is client injection; use it only for controlled legacy reproductions. | D (6/6) | [→](wechatferry.md) |
| **Dify on WeChat** | Use it when a Dify-to-WeChat bridge must be source-inspectable end to end; weigh that it has had no code change since 2025-04 and still carries personal-account channel risk. | B (3/6) | [→](dify-on-wechat.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [ItChat](itchat.md) | ✅ | C (4/6) | Study it only as legacy WeChat-bot code — abandoned, and the web protocol it relies on is defunct, so it mostly doesn't work. |
| [WeChatPlugin-MacOS](wechatplugin-macos.md) | ✅ | D (4/6) | Avoid for current WeChat — a macOS WeChat.app binary tweak that breaks on every WeChat update and is ~2y idle; account-ban & security risk. |
| [wxpy](wxpy.md) | ✅ | D (5/6) | Study it only as legacy WeChat-bot code — archived since 2019 and built on the now-defunct WeChat web protocol, so it mostly doesn't work. |
| [wxappUnpacker](wxappunpacker.md) | ✅ | E (3/6) | Use it when you must decompile a WeChat .wxapkg bundle you own back into readable source — but this exact repo is an empty tombstone, so grab a live fork instead. |
| [WeChat Bot](wechat-bot.md) | ✅ | B (5/6) | Maintained multi-channel CLI and model adapters, but the unofficial personal-WeChat route carries warning and ban risk. |
| [ChatGPT-wechat-bot](chatgpt-wechat-bot.md) | ✅ | D (3/6) | Small historical Wechaty/ChatGPT example, now stale and still dependent on an unsupported personal-account path. |
| [Dify Enterprise WeChat Bot](dify-enterprise-wechat-bot.md) | ✅ | C (3/6) | Fixed-version Windows Enterprise WeChat bridge to Dify whose helper is a closed binary and whose Workflow path is unfinished. |
| [Wechaty](wechaty.md) | ✅ | C (5/6) | The reusable multi-language framework behind many personal-account bots: pick it to own adapters and state yourself, and read its provider status before betting on a channel. |
| [CowAgent](cowagent.md) | ✅ | B (5/6) | The renamed `zhayujie/chatgpt-on-wechat` lineage, now a multi-channel assistant with many model backends — same repository, so treat older references to that name as this page. |
| [WeChatFerry](wechatferry.md) | ✅ | D (6/6) | Archived Windows-client injection with RPC hooks: reference or controlled legacy reproduction only, since the maintainer closed it and releases are pinned to an old WeChat build. |
| [Dify-on-WeChat](dify-on-wechat.md) | ✅ | B (3/6) | A source-inspectable Dify↔WeChat bridge to evaluate before closed-helper alternatives — but read it as drifting: no code changes since 2025-04. |
| WeCom official APIs | 非仓库 | — | Tencent's hosted WeCom (Enterprise WeChat) server API: no repository, official-channel route for teams that must not take personal-account puppet risk. |

## What belongs here

WeChat-specific bots, account tooling, and the frameworks behind them. Other IM platforms and generic automation stay in the parent node; web/browser automation is `web-automation`, team chat apps are `team-chat`.

