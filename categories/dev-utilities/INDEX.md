# dev-utilities

> Category node. Standalone devtools, data-wrangling utilities, developer runtimes, and self-hostable infrastructure.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **Data Tools** | Offline transforms, compression, fake data, font tooling, progress bars, and search utilities. | [→](data-tools/INDEX.md) |
| **Binary Analysis** | Inspect source-unavailable programs, collect reverse-engineering evidence, and rebuild candidate source. | [→](binary-analysis/INDEX.md) |
| **Ops Infrastructure** | Server administration, metrics collection, TLS automation, image slimming, proxying, remote desktop, and password infrastructure. | [→](ops-infra/INDEX.md) |
| **Editors & Runtimes** | Code editors, IDE extensions, app runtimes, and JS/TS toolchains. | [→](editors-and-runtimes/INDEX.md) |
| **Package Manager GUIs** | Desktop front ends for command-line package managers — browse, install and upgrade without the terminal (Homebrew on macOS today). | [→](package-manager-gui/INDEX.md) |
| **Package Managers** | The command-line package manager itself — the tool that resolves, downloads and installs packages into a prefix (a faster Homebrew client today). | [→](package-managers/INDEX.md) |

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **OpenRewrite** | Apply type-aware Java migration recipes with reviewable diffs; check newer language-module licenses and artifact download access. | B (5/6) | [→](openrewrite.md) |
| **Keploy** | Record API calls with dependency replies for regression replay; approve kernel privileges and opt into non-JSON body comparison. | A (6/6) | [→](keploy.md) |
| **App Store Connect CLI** | Script Apple release metadata, TestFlight and review operations with a standalone Go CLI. | B (6/6) | [→](app-store-connect-cli.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [OpenRewrite](openrewrite.md) | Indexed | B (5/6) | Reusable JVM transformations, not Moderne's fleet platform; core Apache license does not cover every language module. |
| [Keploy](keploy.md) | Indexed | A (6/6) | Captured regression fixtures rather than hand-written mocks; Linux instrumentation, private parsers, service terms and default non-JSON comparison gaps remain. |
| [App Store Connect CLI](app-store-connect-cli.md) | ✅ | B (6/6) | Apple release API commands without Ruby; still needs credentials, approval and Xcode for local builds, with default-on telemetry. |

| Option | Type | One-line tradeoff |
| --- | --- | --- |
| [Data Tools](data-tools/INDEX.md) | Sub-category | Offline transforms, compression, fake data, font tooling, progress bars, and search utilities. |
| [Binary Analysis](binary-analysis/INDEX.md) | Sub-category | Inspect source-unavailable programs, collect reverse-engineering evidence, and rebuild candidate source. |
| [Ops Infrastructure](ops-infra/INDEX.md) | Sub-category | Server administration, metrics collection, TLS automation, image slimming, proxying, remote desktop, and password infrastructure. |
| [Editors & Runtimes](editors-and-runtimes/INDEX.md) | Sub-category | Code editors, IDE extensions, app runtimes, and JS/TS toolchains. |
| [Package Manager GUIs](package-manager-gui/INDEX.md) | Sub-category | Desktop front ends for command-line package managers — browse, install and upgrade without the terminal (Homebrew on macOS today). |
| [Package Managers](package-managers/INDEX.md) | Sub-category | The command-line package manager itself — the tool that resolves, downloads and installs packages into a prefix (a faster Homebrew client today). |

## What belongs here

Navigate by utility class: data manipulation, binary analysis, operations infrastructure, editors/runtimes, or package-manager front ends.
