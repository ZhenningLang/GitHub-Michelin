# data-tools

> Category node. Offline data transforms, compression, test data, font tooling, progress indicators, and fast search utilities.
> ← back to [dev-utilities](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **DevToys** | Use it when you want about 30 dev utilities (JWT/Base64 decoding, JSON formatting, diff, hashing) in one offline desktop app so secrets never reach online formatters — but every 2.x build is a prerelease and updates arrive in rare bursts. | B (5/6) | [→](devtoys.md) |
| **CyberChef** | Use it when you need to chain encode/decode, crypto, compression and data-analysis transforms offline in your browser. | A (6/6) | [→](cyberchef.md) |
| **OpenZL** | Use it when you must squeeze terabytes of one highly structured/numeric format better than generic zstd. | C (5/6) | [→](openzl.md) |
| **tqdm** | Use it when you want a fast, low-overhead progress bar for Python loops/CLI/notebooks. | B (5/6) | [→](tqdm.md) |
| **Faker (faker-js)** | Use it when you need realistic fake/mock data (names, addresses, finance…) for tests and seeding in JS/TS. | A (5/6) | [→](faker-js.md) |
| **fontTools** | Use it when you need programmatic font surgery — subset webfonts, convert formats, inspect/patch tables — but it edits font files, it won't design glyphs or shape text. | A (6/6) | [→](fonttools.md) |
| **Flashlight** | Use it only on a pinned macOS 10.10–10.15 machine where you want Python plugins answering inside native Spotlight — but it is abandoned since 2020, dead on Big Sur and later, and requires disabling SIP to inject into a system process. | E (3/6) | [→](flashlight.md) |
| **ripgrep** | Use it when you or a coding agent search a codebase many times a day and want recursive, .gitignore-aware, fast text search by default — but not in portable scripts on arbitrary POSIX hosts, inside archives, or when you know only behaviour, not an identifier. | B (6/6) | [→](ripgrep.md) |
| **fzf** | Use it when you constantly pick one item from long terminal lists (history, files, branches, PIDs) and want type-to-filter selection via CTRL-R and CTRL-T — but it only filters lines it is given and is effectively single-maintainer. | A (6/6) | [→](fzf.md) |
| **jq** | Use it when shell output is nested JSON (kubectl, aws, gh api, webhooks) and you need to extract or filter fields in one pipeline-friendly line — but not for multi-gigabyte analytical queries, non-JSON input, or integer math beyond 2^53. | A (5/6) | [→](jq.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [DevToys](devtoys.md) | ✅ | B (5/6) | Local-only, clipboard-aware convenience in one window, at the cost of one-shot tools without recipe chaining and a slow, prerelease-only release line. |
| [CyberChef](cyberchef.md) | ✅ | A (6/6) | Use it when you need to chain encode/decode, crypto, compression and data-analysis transforms offline in your browser. |
| [OpenZL](openzl.md) | ✅ | C (5/6) | Use it when you must squeeze terabytes of one highly structured/numeric format better than generic zstd. |
| [tqdm](tqdm.md) | ✅ | B (5/6) | Use it when you want a fast, low-overhead progress bar for Python loops/CLI/notebooks. |
| [Faker (faker-js)](faker-js.md) | ✅ | A (5/6) | Use it when you need realistic fake/mock data (names, addresses, finance…) for tests and seeding in JS/TS. |
| [fontTools](fonttools.md) | ✅ | A (6/6) | Use it when you need programmatic font surgery — subset webfonts, convert formats, inspect/patch tables — but it edits font files, it won't design glyphs or shape text. |
| [Flashlight](flashlight.md) | ✅ | E (3/6) | Buys extensible Spotlight without installing a separate launcher; costs system-process code injection, SIP disabled, and no fixes — Alfred or Raycast are the maintained route. |
| [ripgrep](ripgrep.md) | ✅ | B (6/6) | Defaults that match real project layouts, plus speed, at the cost of a non-standard, not-preinstalled tool maintained mostly by one person. |

## What belongs here

Offline data transforms, compression, test data, font tooling, progress indicators, and fast search utilities.
