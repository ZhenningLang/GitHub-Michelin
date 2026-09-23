# package-manager-gui

> Category node. Desktop front ends for command-line package managers — browse, install, upgrade and remove packages without the terminal. All entries today are macOS / Homebrew GUIs.
> ← back to [dev-utilities](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **BrewUI** | Use it when you want Homebrew's own GUI on macOS 26, with every underlying `brew` command shown and streamed in a console you can copy from. | C (5/6) | [→](brewui.md) |
| **Applite** | Use it when a non-technical user needs to install Mac apps on a machine that has never had a terminal — it brings its own Homebrew and manages casks only. | A (6/6) | [→](applite.md) |
| **CaskHub** | Use it when you want the richest App Store-style browsing for Homebrew casks on macOS 15.6+, and accept a built-in telemetry stack. | B (6/6) | [→](caskhub.md) |
| **Cork** | Use it when you want the deepest Homebrew surface — services, taps, tagging, menu-bar updates — and will pay 25€ for the prebuilt. | B (5/6) | [→](cork.md) |
| **Cakebrew** | Use it only as a reference for first-generation Homebrew GUIs; it is effectively unmaintained since 2021 and has no installable cask. | D (4/6) | [→](cakebrew.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [BrewUI](brewui.md) | ✅ | C (5/6) | Official and transparent, with a full console — at the cost of a macOS 26 floor and no tap or prefix management. |
| [Applite](applite.md) | ✅ | A (6/6) | Needs no terminal and no Homebrew, with Brewfile round-tripping — but casks only, and a second Homebrew tree the app owns. |
| [CaskHub](caskhub.md) | ✅ | B (6/6) | The widest catalogue browsing and the strongest recent install reach — but cask-only and shipping Sentry/TelemetryDeck. |
| [Cork](cork.md) | ✅ | B (5/6) | Services, tagging and menu-bar updates brew itself lacks — but 25€ for the prebuilt and a licence that forbids reuse. |
| [Cakebrew](cakebrew.md) | ✅ | D (4/6) | Formula and tap management from an Objective-C era — but the default branch has not moved since 2021. |

## What belongs here

Desktop GUIs that wrap a command-line package manager: catalogue browsing, install/upgrade/uninstall, and whatever administration surface the underlying manager offers. It is not a place for the package managers themselves, nor for app-store clients that do not drive a real package manager.
