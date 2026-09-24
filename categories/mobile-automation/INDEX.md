# mobile-automation

> Category node. Programmatically drive iOS/Android simulators, emulators, and devices — inject input, drive the UI, and run end-to-end flows.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **baguette** | Use it when you want headless, scriptable control of an Apple-Silicon iOS Simulator — 60fps streaming, host-side gestures, a multi-device farm — but it needs Xcode 26 and rides private SimulatorKit symbols. | B (6/6) | [→](baguette.md) |
| **idb** | Use it when you must automate iOS simulators AND real devices from a remote client with granular primitives — but iOS 26 broke parts of it and you run a companion per target. | B (6/6) | [→](idb.md) |
| **AXe** | Use it when you want a single `axe tap / type / describe-ui` CLI against a simulator — but it is a single-maintainer project, quiet since 2026-07. | B (6/6) | [→](axe.md) |
| **Appium** | Use it when you need one cross-platform, cross-language WebDriver test framework for iOS and Android — but you install and operate a server plus per-platform drivers. | A (6/6) | [→](appium.md) |
| **WebDriverAgent** | Use it when you are building the iOS automation layer itself — it is the WebDriver server Appium drives — not something most teams run standalone. | A (4/6) | [→](webdriveragent.md) |
| **Maestro** | Use it when you want YAML flows and near-zero onboarding for Android/iOS/web E2E — but physical iOS devices are unsupported. | A (6/6) | [→](maestro.md) |
| **Detox** | Use it when you are testing a React Native app and want gray-box synchronization that fights flakiness — but it locks to RN versions, is JS-only, and iOS physical devices are unsupported. | B (6/6) | [→](detox.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [baguette](baguette.md) | ✅ | B (6/6) | Headless simulator control with streaming + a farm, but Apple-Silicon/Xcode-26-only and on private symbols. |
| [idb](idb.md) | ✅ | B (6/6) | Granular remote primitives for simulators *and* devices, but heavier (companion per target) and iOS-26 regressions are open. |
| [AXe](axe.md) | ✅ | B (6/6) | The simplest simulator input CLI, but single-maintainer and stale since 2026-07. |
| [Appium](appium.md) | ✅ | A (6/6) | The broadest cross-platform framework, at the cost of running a server and installing drivers. |
| [WebDriverAgent](webdriveragent.md) | ✅ | A (4/6) | The iOS engine under Appium's XCUITest driver — a dependency, not a standalone test tool. |
| [Maestro](maestro.md) | ✅ | A (6/6) | Flat YAML flows and the fastest start, but no physical iOS devices. |
| [Detox](detox.md) | ✅ | B (6/6) | Best flakiness control for React Native, but RN-version-locked and JS-only. |
| (non-repo tools named across the pages) | 非仓库 | — | `xcrun simctl` and `XCUITest` ship inside Xcode; see each page's Comparison. |

## What belongs here

Tools that **drive mobile devices and their simulators/emulators** — input injection, UI automation, and E2E test frameworks for iOS (and, where the tool covers it, Android). Not desktop GUI automation (see `desktop-automation`) or web-page automation (see `web-automation`).
