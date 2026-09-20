# peripherals

> Category node. Configure and drive desktop peripherals — Logitech mice, keyboards, receivers, lights and webcams — over HID++ and UVC.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **OpenLogi** | Use it when you want the Options+ feature set — per-app profiles, gestures, keyboard remapping, static RGB, webcam controls — on macOS, Linux and Windows from one TOML config, and you accept a pre-1.0, months-old project with no receiver pairing. | C (5/6) | [→](openlogi.md) |
| **Solaar** | Use it on Linux when the job is device management rather than remapping: pair and unpair receivers, read battery and device state, change HID++ settings — backed by 14 years of still-shipping history, at the cost of Linux-only scope and no camera or RGB. | B (6/6) | [→](solaar.md) |
| **Mouser** | Use it when you want to remap a Logitech HID++ mouse per application from a portable ZIP on Windows/macOS/Linux, with no installer, account or service — and you don't need pairing, keyboards, cameras or per-device mappings. | B (5/6) | [→](mouser.md) |
| **logiops** | Use it on Linux when you want a root systemd daemon reading one declarative `/etc/logid.cfg` instead of a GUI — accepting HID++ 2.0+ mice only, no app awareness, and development that has effectively stopped since 2024. | C (4/6) | [→](logiops.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [OpenLogi](openlogi.md) | ✅ | C (5/6) | Broadest coverage of the four — mouse, keyboard, webcam, lighting, three OSes, GUI + CLI + TOML — but pre-1.0 with no pairing and a single owner. |
| [Solaar](solaar.md) | ✅ | B (6/6) | The mature Linux device manager: pairing, status and settings with a 14-year record; no webcam, no RGB, no per-app profiles, and Linux-first. |
| [Mouser](mouser.md) | ✅ | B (5/6) | Mouse-only and portable: extract and run on all three OSes with per-app profiles; no pairing, global mappings, 7-month history. |
| [logiops](logiops.md) | ✅ | C (4/6) | Daemon plus config file, no GUI: stable and packageable on Linux, but near-dormant development and HID++ 2.0+ only. |
| Logitech Options+ / G HUB | 未收录 | — | Official, closed apps and the only ones with Flow, firmware update and vendor QA — Windows/macOS only, no Linux. |

## What belongs here

Programs that **configure or drive attached desktop peripherals themselves** — reading and writing device settings over the device's own protocol (HID++ for Logitech, UVC for cameras), including receiver pairing, button/gesture mapping, DPI, lighting and input injection.

Not here:

- **Scripting a GUI by coordinates/pixels** — see `desktop-automation`. This category talks to hardware protocols, not to screen pixels or window widgets.
- **Automating a browser or web page** — see `web-automation`.
- **Multi-vendor gaming-mouse configuration daemons** (e.g. libratbag/Piper) — same *shape* (a daemon plus a config front-end) but not the same protocol; not yet indexed.
