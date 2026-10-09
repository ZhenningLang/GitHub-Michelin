# package-managers

> Category node. Command-line package managers themselves — the tool that resolves, downloads, installs and links packages on your machine (desktop front ends that drive one live in [package-manager-gui](../package-manager-gui/INDEX.md)).
> ← back to [dev-utilities](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **zerobrew** | Use it when you reinstall the same Homebrew command-line formulae often and want the identical bottles installed several times faster by a Rust client beside `brew` — but it is experimental, skips `post_install`, and installs only binary-artifact casks. | B (6/6) | [→](zerobrew.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [zerobrew](zerobrew.md) | ✅ | B (6/6) | Homebrew's own catalogue and bottles, relocated once into a content-addressed store so reinstalls are clones — at the price of a young client whose recent work is mostly one maintainer with no post-install steps and no `.app` casks. |

Not yet indexed but named on the zerobrew page: Homebrew itself (`Homebrew/brew`), nanobrew, pkgx, Nix and MacPorts.

## What belongs here

The package manager itself — a CLI that resolves dependencies and installs packages into a prefix, whatever ecosystem's catalogue it reads. Graphical front ends that wrap one belong in `package-manager-gui`; language-specific dependency managers (pip/uv, npm) stay with their language tooling.
