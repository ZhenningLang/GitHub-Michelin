# gpu-tooling

> GPU hardware configuration, firmware and performance experiments. Risk-information entries are not installation approval.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
|---|---|---|---|
| **gpu-unlock** | Review an Ampere pre-driver instruction-rate unlock; privileged firmware/register writes, mixed licensing and partial recovery. | C (5/6) | [→](gpu-unlock.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
|---|---|---|---|
| [gpu-unlock](gpu-unlock.md) | ✅ | C (5/6) | Leaves the runtime driver unpatched, but changes boot-time GPU state without compatibility, benefit or rollback guarantees. |

## What belongs here

GPU-specific host integration and hardware-performance tooling, not model-serving engines or ordinary application matrix kernels. Read negative scenarios and permission boundaries before considering hardware experiments.
