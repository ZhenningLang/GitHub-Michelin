# desktop-automation

> Category node. Programmatic desktop GUI automation (mouse/keyboard/screen).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Cua** | Use it when an agent must operate a whole computer — native desktop apps and OS dialogs, not just a web page — and the run should be isolated. | B (5/6) | [→](cua.md) |
| **PyAutoGUI** | Use it when a Python script must click and type into a GUI-only desktop app on Windows, macOS or Linux — but pixel/coordinate automation breaks silently on DPI, resolution or theme changes, needs a real display, and upstream has been quiet since 2023. | C (4/6) | [→](pyautogui.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Cua](cua.md) | ✅ | B (5/6) | Use it when an agent must operate a whole computer — native desktop apps and OS dialogs, not just a web page — and the run should be isolated. |
| [PyAutoGUI](pyautogui.md) | ✅ | C (4/6) | Buys a dozen-line, cross-platform mouse/keyboard robot with no RPA platform to learn; costs brittleness, no headless mode, and no accessibility-tree awareness. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

Tools that **drive the desktop GUI** (mouse/keyboard/screen). Not web-page automation (see `web-automation`).
