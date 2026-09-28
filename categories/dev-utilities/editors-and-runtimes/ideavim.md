---
name: IdeaVim
slug: ideavim
repo: https://github.com/JetBrains/ideavim
category: editors-and-runtimes
tags: [vim, jetbrains, intellij, ide-plugin, editor, keybindings, kotlin]
language: Kotlin
license: MIT
maturity: "2.47.1 (JetBrains Marketplace), very active, ~10.3k stars (as of 2026-09)"
last_verified: 2026-09-28
type: tool
upstream:
  pushed_at: 2026-09-27T09:00:40Z
  default_branch: master
  default_branch_sha: 6e47c141de86a69d9c675fea8a4d6aa4dcd5498f
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T05:58:42Z
  overall: A
  overall_score: 3.75
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: A
      raw:
        repo_age_days: 5682
        last_commit_age_days: 2
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 11
        top1_share: 0.474
        top3_share: 0.965
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: issues_disabled }
    adoption: { reason: ambiguous }
---

# IdeaVim

A Vim emulation plugin for JetBrains IDEs (IntelliJ IDEA, PyCharm, GoLand, WebStorm, Rider, etc.) — Vim motions, modes, registers, macros, and a `.ideavimrc` inside the IDE, maintained by JetBrains itself.

![ideavim — health radar](../../../assets/health/ideavim.svg)

## When to use

You're a developer whose fingers are wired for Vim — `hjkl`, `ciw`, `dd`, visual-block, `.` repeat, macros — but your team's real work lives in IntelliJ/PyCharm/GoLand for the refactoring, debugging, and language intelligence you won't give up. Running actual Vim or Neovim in a terminal means losing the IDE; using the IDE's stock keymap means losing your muscle memory. You install IdeaVim from the plugin marketplace, drop a `~/.ideavimrc` in your home dir (much of your `.vimrc` syntax carries over — you can even `source ~/.vimrc`), and now the editor pane behaves like Vim — modes, operators, registers, marks, macros — while `<Action>(id)` mappings bind IDE actions to Vim keys (`map <leader>r <Action>(RenameElement)`), `:actionlist` helps you find the action ids, and the IdeaVim extension set (`set surround`, `set multiple-cursors`, easymotion…) recreates the plugin behaviors you rely on. You get Vim editing *and* IntelliJ's semantic refactors/debugger in one tool.

You reach for it specifically when the IDE is non-negotiable (large JVM/Kotlin/Go codebase, heavy refactoring, integrated debugger) but you refuse to type like a non-Vim user. It is the canonical, JetBrains-blessed way to do that.

## How it works

IdeaVim is a Vim *engine* written in Kotlin that runs inside the IDE's editor component — it does not embed a real Vim process. It intercepts your keystrokes in the editor pane and runs its own mode state machine (normal/insert/visual): when you type `ciw` it parses the operator and applies the change directly to the IDE's own document model — not to a buffer copy — so IntelliJ's refactorings, debugger, and indexing still operate on the same text you are editing. What stays yours is the configuration: a `~/.ideavimrc` file in Vim-flavored syntax, `set` flags to switch on bundled emulations (surround, multiple-cursors, commentary, easymotion), and `<Action>(ActionId)` mappings that reach IDE features from the Vim keylayer (the README explicitly steers you away from `:action` inside mappings — `<Action>` is the supported form). Keymap clashes are resolved in the IDE's own Vim/Keymap settings pages, and `Tools | Vim` toggles the whole layer off without a restart.

![IdeaVim — backbone user story](../../../assets/flow/ideavim.svg)

<!-- flow-steps:begin (generated from flows/ideavim.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install IdeaVim from the IDE's plugin manager — `Settings | Plugins`
2. **IdeaVim**: Its Vim engine takes over keystroke handling in the editor pane — component: `Vim engine`
3. **You**: Put your Vim-flavoured settings in the ideavimrc file — `~/.ideavimrc`
4. **You**: Bind IDE actions to Vim keys with an Action mapping — `map <leader>r <Action>(RenameElement)`
5. **IdeaVim**: Modes, operators and macros apply to the IDE's own document — refactorings and debugger unchanged

**Value**: Vim muscle memory and JetBrains' semantic tooling in one editor, toggled off any time

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You're not in a JetBrains IDE.** It only works inside IntelliJ-platform IDEs. For VS Code use the VSCodeVim/Neovim extensions; for a terminal use real Vim/Neovim. Wrong host = wrong tool.
- **You want 100% Vim/Neovim fidelity or your full plugin ecosystem.** It's an *emulation* of a large subset, not Vim itself — some obscure commands, edge-case behaviors, and the entire native Vimscript/Lua plugin universe aren't there (IdeaVim has its own smaller extension set). Power users hit gaps. [未验证]
- **You want Neovim's Lua config / LSP / treesitter inside the IDE.** IdeaVim reads a `.ideavimrc`, not your Neovim Lua config; the IDE provides the language intelligence, not Neovim's stack.
- **Minimal/keyboard-light editing.** If you don't already think in Vim, adding a modal layer over the IDE is friction, not speed — learn it deliberately or skip it.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| VSCodeVim | 未收录 | Choose VSCodeVim when VS Code is your editor and you only need Vim emulation there. | Vim emulation for VS Code; same idea on a different host — choose by which IDE you actually use, not by the plugin. |
| vscode-neovim | 未收录 | Choose vscode-neovim when you need a *real* Neovim instance embedded inside VS Code. | Embeds a *real* Neovim instance inside VS Code for higher fidelity + your Neovim config; heavier and VS Code-only, no JetBrains equivalent of this depth. |
| Real Vim / Neovim | 未收录 | Choose real Vim or Neovim when you want the full plugin ecosystem and Lua/LSP instead of IDE integration. | The genuine article with full plugin ecosystem and Lua/LSP; but you lose JetBrains' integrated refactoring/debugger/indexing. |
| JetBrains stock keymap | 未收录 | Choose the JetBrains stock keymap when you need a fully supported setup with no emulation layer. | No emulation layer, fully supported; but no Vim modes/motions — defeats the purpose for a Vim user. |

## Tech stack

- **Language:** Kotlin (JetBrains' language; the plugin runs on the IntelliJ Platform / JVM).
- **Host:** the IntelliJ Platform plugin API — it hooks the editor component of any IntelliJ-based IDE.
- **Config:** a `~/.ideavimrc` file using Vim-style commands/mappings, plus `<Action>(ActionId)` mappings to invoke IDE actions (per current README guidance; `:action` is for one-off invocation, not mappings) and a set of IdeaVim extension plugins.
- **Distribution:** the JetBrains Marketplace (and bundled/installable in IntelliJ-platform IDEs).

## Dependencies

- **Runtime:** a JetBrains IntelliJ-platform IDE (IntelliJ IDEA, PyCharm, GoLand, WebStorm, Rider, CLion, etc.) of a compatible version — the IDE *is* the platform it plugs into.
- **No external services / datastore** — it's an in-IDE plugin; config is a local file.
- **Optional:** companion IdeaVim extension plugins (surround, sneak, etc.) installed alongside.

## Ops difficulty

**Very low.** Install from the plugin marketplace, optionally write a `.ideavimrc`, toggle it on. There's nothing to deploy or operate — it lives entirely inside the IDE you already run. The only "difficulty" is configuration taste (porting `.vimrc` habits, mapping IDE actions) and occasionally an IDE-version compatibility bump, which JetBrains tracks closely since they ship it.

## Health & viability

- **Responsiveness**: Cannot be scored — GitHub issues are disabled; the tracker is JetBrains YouTrack (`VIM` project), which the health scorer cannot read. Not a neglect signal, a measurement gap.
- **Maintenance (2026-09).** Very active — last push 2026-09-27, frequent commits, led by a small JetBrains team (AlexPl292 and others) with thousands of commits. Current Marketplace build 2.47.1 (plugins.jetbrains.com API, 2026-09-28). Distributed via Marketplace rather than GitHub Releases, so "no releases" on GitHub is expected, not a staleness signal. Not archived. [推断：Marketplace 版本与仓库提交节奏的对应关系未逐一核对]
- **Governance / backing.** Owned and maintained by **JetBrains** (an Organization, the IDE vendor itself) — first-party, well-funded stewardship with a direct incentive to keep it working across IDE releases. Among the strongest backing profiles for an IDE plugin. [推断]
- **Age & Lindy.** Created 2011; ~15 years old and **still actively shipping** ⇒ a **strong Lindy** signal — it has tracked the IntelliJ Platform across many major versions and remains the default Vim layer for JetBrains. [推断]
- **Adoption.** ~10.3k GitHub stars (API, 2026-09-28) and **22.1M plugin downloads** reported by the JetBrains Marketplace API for plugin id 164 (2026-09-28) — a package-index figure that understates nothing the way stars do for an IDE plugin; standard inclusion in most JetBrains-Vim user setups. The health scorer still grades adoption `?` because it cannot map a Marketplace artifact to a package registry. [推断：下载数计的是安装面而非活跃用户]
- **Risk flags.** Few — permissive MIT, first-party vendor backing. The structural ceiling is inherent: it's an *emulation* tied to the IntelliJ Platform, so fidelity gaps and platform-version coupling are the real (and bounded) risks, not project abandonment. [推断]

## Caveats (unverified)

- [未验证] ~10.3k GitHub stars as of 2026-09-28 (API-checked); star counts are date-sensitive and indicative only.
- [未验证] Marketplace reports 22.1M downloads for plugin 164 (API, 2026-09-28); this is a cumulative install count, not active users, and the exact release/version cadence + IDE compatibility ranges live on the Marketplace, not enumerated here.
- [未验证] The exact set of supported Vim features vs. gaps (and the IdeaVim extension catalog) shifts version-to-version; verify the specific command/plugin you depend on against current docs.
- [推断] "First-party, well-funded" is inferred from JetBrains ownership; specific staffing/funding allocated to IdeaVim is not stated.
- [推断] Compatibility with any given IDE version is governed by the plugin's declared platform range and changes over time; not asserting a specific matrix here.
