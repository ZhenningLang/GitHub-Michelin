# hackintosh

> Category node. Run macOS on PC hardware Apple never sold — OpenCore boot setup, and the kexts and drivers that make unsupported hardware (GPUs first of all) work under it.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **NullMoth NVIDIA Driver for macOS** | Use it when an OpenCore PC on macOS 15 has only a Turing-or-later GeForce card and keeping that card matters more than stability — accepting a two-day-old single-author kernel driver validated on one RTX 5060, SIP/AMFI/Secure Boot relaxed, and a noncommercial license. | D (4/6) | [→](nvidia-macos-driver.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [NullMoth NVIDIA Driver for macOS](nvidia-macos-driver.md) | ✅ | D (4/6) | The only route to Metal on Turing-and-later NVIDIA cards under Sequoia; pays with an unproven port, relaxed macOS security, binary-only releases and a noncommercial license. |
| AMD Radeon + WhateverGreen | not indexed | — | The stable Hackintosh GPU path: Apple's own drivers with security left on; costs a GPU swap and CUDA on that card. |
| OpenCore Legacy Patcher | not indexed | — | Restores legacy (Kepler-era) GPU acceleration on old real Macs; does not cover Turing-and-later NVIDIA cards. |
| NVIDIA Web Drivers | not a repo | — | NVIDIA's closed drivers, discontinued after macOS 10.13 High Sierra and Pascal. |

## What belongs here

Projects whose job is **getting macOS to boot and drive hardware on machines Apple does not support**: the OpenCore bootloader and its configuration tools, kernel extensions that patch or replace drivers (GPU, audio, USB, Wi-Fi), and drivers for hardware macOS has no support for.

Not here:

- **Running macOS in a virtual machine** — a different shape (hypervisor, not boot chain); not yet indexed.
- **General macOS utilities** that run on any Mac — see `dev-utilities` or `disk-cleanup`.
