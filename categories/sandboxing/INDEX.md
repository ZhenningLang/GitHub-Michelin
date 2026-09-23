# sandboxing

> Category node. Sandbox technologies for untrusted and agent-generated workloads — the kernel/VM isolation runtimes, and the agent-facing sandbox platforms and SDKs built on top of them.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **gVisor** | Use it when untrusted containers must be isolated from the host kernel without running a VM — it needs no KVM and keeps your container workflow. | A (6/6) | [→](gvisor.md) |
| **Kata Containers** | Use it when every pod should get a real guest kernel in a lightweight VM, while Kubernetes keeps its normal RuntimeClass workflow. | A (6/6) | [→](kata-containers.md) |
| **Firecracker** | Use it when you are building the sandbox layer yourself and want a minimal KVM microVM primitive with a control API — not a container runtime. | A (6/6) | [→](firecracker.md) |
| **OpenSandbox** | Use it when you must self-host isolated sandboxes to run untrusted agent-generated code at K8s scale with egress controls and a credential vault — but the repo is only months old (created 2025-12), so its API and Lindy track record are unproven. | B (6/6) | [→](opensandbox.md) |
| **E2B** | Use it when an agent needs to run AI-generated code and you want the sandbox as an SDK — hosted by default, Terraform-self-hosted on AWS/GCP when it must live in your own account. | A (6/6) | [→](e2b.md) |
| **Agent Substrate** | Use it when a large fleet of stateful agent sessions sits idle most of the time and you want them multiplexed onto fewer warm Kubernetes pods by checkpointing idle agents and resuming them on demand — but it's pre-1.0 with unstable APIs and no security hardening yet. | B (5/6) | [→](substrate.md) |
| **Modal client SDK** | Use it when you want serverless containers, GPUs and sandboxes without operating anything — the client SDK is open source, the platform is closed and hosted-only. | A (6/6) | [→](modal-client.md) |
| **Microsandbox** | Use it when the sandbox must run on hardware you already own — one binary or SDK, ordinary OCI images, per-sandbox egress policy and host-side secrets, with no daemon and no cluster — but it needs KVM/Apple Silicon/WHP on the host and is still beta. | A (6/6) | [→](microsandbox.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [gVisor](gvisor.md) | ✅ | A (6/6) | Isolation without KVM (userspace kernel, filtered syscall surface) — cheaper to adopt than a VM, but syscall semantics and throughput differ from a real kernel. |
| [Kata Containers](kata-containers.md) | ✅ | A (6/6) | A real kernel per sandbox via lightweight VMs, and a finished Kubernetes integration — at the cost of hardware virtualization on every node and a hypervisor to operate. |
| [Firecracker](firecracker.md) | ✅ | A (6/6) | The smallest-surface microVM primitive there is, and you build everything above it: images, scheduling, snapshots, multi-tenancy. |
| [OpenSandbox](opensandbox.md) | ✅ | B (6/6) | Self-host-first sandbox platform with a documented protocol and multi-language SDKs — you run the platform, and it is young. |
| [E2B](e2b.md) | ✅ | A (6/6) | Fastest path to a working sandbox (hosted SDK first, Terraform self-host later) — self-hosting covers only AWS/GCP. |
| [Agent Substrate](substrate.md) | ✅ | B (5/6) | Density for *stateful* agents by snapshotting idle ones onto warm pods — pre-1.0, ingress-driven wakeups, no security hardening yet. |
| [Modal client SDK](modal-client.md) | ✅ | A (6/6) | Serverless containers, GPUs and sandboxes with nothing to operate — no self-hosting, no exit, single vendor. |
| [Microsandbox](microsandbox.md) | ✅ | A (6/6) | Local-first microVM sandboxes from ordinary OCI images, with Docker-like verbs and no daemon — cross-platform and unprivileged, but it needs hardware virtualization on the host and is beta. |

## What belongs here

Layers and products for running code you do not trust: VM/kernel-level isolation runtimes (`gVisor`, `Kata Containers`, `Firecracker`) and the agent-facing sandbox platforms and clients built on them (`OpenSandbox`, `E2B`, `Agent Substrate`, the `Modal` client SDK). Not general container-runtime selection — that is the platform you already run — and not agent frameworks, which live in `agent-frameworks`.
