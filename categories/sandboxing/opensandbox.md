---
name: OpenSandbox
slug: opensandbox
repo: https://github.com/opensandbox-group/OpenSandbox
category: sandboxing
tags: [sandbox, agent-runtime, code-execution, isolation, kubernetes, docker, microvm]
language: Python
license: Apache-2.0
maturity: v0.x (python SDK v0.1.13), active, ~11.7k stars (as of 2026-06)
last_verified: 2026-06-28
type: framework
upstream:
  pushed_at: 2026-06-29T11:31:31Z
  default_branch: main
  default_branch_sha: 032790072b3efb69a75a2917e26259df49cf7138
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:02:23Z
  overall: B
  overall_score: 3.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 13.9
        qualifying_issues: 44
        band: default
        window_offset_days: 0
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: opensandbox
        dependent_repos_count: 0
        downloads_last_month: 307927
        graph_tier: E
        volume_tier: B
        cross_check_divergence: null
        release_downloads: 7214
        release_assets: 27
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: D
      raw:
        repo_age_days: 279
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 94
        top1_share: 0.361
        top3_share: 0.566
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# OpenSandbox

A general-purpose, secure sandbox runtime and platform for AI agents — multi-language SDKs, a unified sandbox protocol, and Docker/Kubernetes backends for running untrusted agent-generated code, GUI/browser automation, and RL/eval workloads in isolated environments.

![opensandbox — health radar](../../assets/health/opensandbox.svg)

## When to use

You're building a coding agent (or an agent-evaluation harness) and you've hit the wall every such project hits: the model wants to run shell commands, write files, `pip install`, and execute arbitrary code it just generated — and you cannot let that touch your host or your other tenants. You've been stitching together raw Docker `exec` calls, a homegrown filesystem API, and some scary networking, and it doesn't scale past a laptop. You reach for OpenSandbox: you `pip install opensandbox`, point it at a runtime (local Docker for dev, the Kubernetes runtime for fleet scale), and get a uniform API to create a sandbox, run commands, move files in and out, and run a built-in Code Interpreter — with per-sandbox egress controls and a credential vault so the workload never sees your real secrets. The same SDK call works whether you're on one machine or scheduling thousands of sandboxes on a cluster.

You also reach for it when isolation strength is the requirement, not an afterthought: it can run sandboxes on secure container runtimes (gVisor, Kata Containers, Firecracker microVM) rather than plain containers, and it exposes a unified ingress gateway plus a sandbox protocol you can extend with custom runtimes. If you're comparing against hosted code-execution APIs but want to self-host the runtime — keeping the agent's code execution inside your own infra — this is the kind of platform that targets that gap.

## When NOT to use

- **You just need to run one trusted script locally.** If the code is yours and trusted, a plain Docker container or a subprocess is far less machinery than a full sandbox platform with a server, runtime, and protocol.
- **You can use a hosted code-execution API and don't want to operate infra.** Managed sandbox services (E2B, Daytona, vendor code-interpreter APIs) remove the ops burden entirely; OpenSandbox is something you run and keep running.
- **You need a battle-tested, years-proven dependency today.** The repo was created 2025-12 — it is months old. High stars on a months-old project is a hype signal, not a Lindy/track-record signal; APIs and the sandbox protocol may still churn. [推断]
- **Your isolation requirements demand a specific, audited runtime you must certify yourself.** OpenSandbox can drive gVisor/Kata/Firecracker, but you still own configuring and validating that the isolation meets your threat model — the platform integrating them is not a substitute for that review. [未验证]
- **You don't run Kubernetes or Docker and don't want to.** The runtimes are Docker and Kubernetes; there is no serverless/no-infra mode — the orchestration layer is yours to operate.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [E2B](e2b.md) | ✅ | Choose E2B when you want the sandbox as a hosted-or-self-hosted SDK with an interpreter and desktop surfaces; choose OpenSandbox when the platform itself must be self-hosted and extensible. | E2B leads with a polished hosted product and Terraform self-hosting on AWS/GCP; OpenSandbox leads with a self-host-first platform and an extendable sandbox protocol. Both hide the same problem — which sandbox technology to run — behind different bets on who operates it. |
| [Agent Substrate](substrate.md) | ✅ | Choose Substrate when the agents are long-lived and idle-heavy and the cost problem is pod density with snapshot resume; choose OpenSandbox when the job is "run this code in isolation, now". | Substrate multiplexes stateful sessions with suspend/resume; OpenSandbox exposes disposable execution sandboxes. Overlap is only the isolation layer — density versus on-demand execution. |
| [gVisor](gvisor.md) | ✅ | Choose gVisor when you want syscall-level isolation without a VM and will build the sandbox lifecycle yourself; choose OpenSandbox when you want that lifecycle, SDKs and policy delivered. | A userspace kernel used as a runtime class; it is the isolation primitive OpenSandbox-style platforms can drive, not a platform. |
| [Kata Containers](kata-containers.md) | ✅ | Choose Kata when your Kubernetes should give each pod a real kernel in a lightweight VM; choose OpenSandbox when you want a sandbox API instead of a runtime class. | Kata is node-level VM isolation with full container-manager integration; OpenSandbox is the API/lifecycle layer above runtimes like it. |
| [Firecracker](firecracker.md) | ✅ | Choose Firecracker when you are building the sandbox layer and want the minimal KVM microVM primitive; choose OpenSandbox when you want sandboxes as a product. | Firecracker stops at the microVM boundary; OpenSandbox must solve images, scheduling, lifecycle and policy on top of some such primitive. |
| Daytona | 未收录 | Choose Daytona when the need is a hosted-first dev-environment/sandbox platform for agents; choose OpenSandbox when you must self-host the platform. | Adjacent product shape (dev environments rather than an agent code-execution protocol); not indexed in this batch — tracked as backlog rather than justified out of scope by capability. |
| Plain Docker / containerd | 未收录 | Choose Docker or containerd when ubiquitous containers are enough; choose OpenSandbox when the workload is untrusted and needs a sandbox protocol, credential vault and egress policy. | The baseline you are replacing (containerd/runc selection is out of scope here): you get a container, not a sandbox platform. |
| Jupyter Kernel Gateway / nsjail | 未收录 | Choose these when you need narrow, single-purpose code-execution or isolation plumbing; choose OpenSandbox when you want the agent-facing platform around it. | Single-purpose primitives with no multi-tenant platform layer; out of scope for this node rather than addable peers. |

## Tech stack

- **Languages:** Python is the primary language; the project ships SDKs in Python, Java/Kotlin, JavaScript/TypeScript, C#/.NET, and Go.
- **Runtimes:** Docker (local) and a Kubernetes runtime/controller for distributed scheduling.
- **Isolation:** integrates secure container runtimes — gVisor, Kata Containers, and Firecracker microVM — for stronger host/workload separation.
- **Surface:** a `osb` CLI, an MCP server integration, a unified ingress gateway with per-sandbox egress controls, a credential vault, and a documented sandbox protocol (lifecycle + execution APIs) in `specs/`.
- **Built-ins:** Command, Filesystem, and Code Interpreter environments; examples for Claude Code, Chrome/Playwright browser automation, and VNC/VS Code desktops.

## Dependencies

- **Runtime you must run:** a container runtime — Docker for local use, or a Kubernetes cluster for scale (plus the OpenSandbox lifecycle server/controller). This is the load-bearing dependency.
- **Optional secure runtimes:** gVisor, Kata Containers, or Firecracker if you want stronger-than-container isolation — each adds its own host/kernel setup.
- **SDK install:** `pip install opensandbox` (Python), Maven/Gradle artifacts under `com.alibaba.opensandbox`, `@alibaba-group/opensandbox` (npm), a .NET package, and a Go module. The CLI is `opensandbox-cli`.
- **Network:** the ingress gateway and egress controls assume you provide the surrounding network plumbing.

## Ops difficulty

**Medium-to-high.** The local Docker path is approachable for development. Production is a real platform to operate: a lifecycle server, a Kubernetes controller, an ingress gateway, egress policy, and a credential vault — plus, if you want strong isolation, the host-level setup for gVisor/Kata/Firecracker (kernel features, node configuration). You are running a multi-component distributed system whose whole job is to safely execute untrusted code, so getting isolation, networking, and secret handling right is the hard part, and it's security-critical. The project carries an OpenSSF Best Practices badge and a GOVERNANCE.md, which helps, but the operational surface is inherently larger than a single binary or a hosted API.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 13.9 hours across 44 qualifying issues/PRs.
- **Maintenance (2026-06).** Last pushed 2026-06-27; multiple component releases tagged 2026-06-25 (python SDK v0.1.13, java v1.0.15) — **very active** development. Not archived. [推断]
- **Backing & governance (2026-06).** Originated from Alibaba (the repo's own badges/links reference `github.com/alibaba/OpenSandbox`) and now sits under the `opensandbox-group` org with a GOVERNANCE.md, an OpenSSF Best Practices entry, and a CNCF Landscape listing — signals of an intent toward open, multi-maintainer governance backed by a large vendor. [未验证]
- **Age × Lindy (2026-06).** Created 2025-12 — roughly 6 months old. This is a **young project**; Lindy gives it no credit yet. ~11.7k stars on a months-old repo is a strong hype/attention signal but says nothing about longevity. Treat API/protocol stability as unproven. [推断]
- **Adoption & ecosystem.** Broad SDK coverage (5 languages), MCP integration, and CNCF Landscape presence suggest real ecosystem ambition; production-user evidence at this age is thin and unverified. [未验证]
- **Risk flags.** Youth is the main one — API churn and unproven track record. Single large-vendor origin (Alibaba) is a governance consideration despite the multi-maintainer framing; verify how decisions are actually made if you depend on it. [推断]

## Caveats (unverified)

- [未验证] ~11.7k stars and v0.1.13 (python SDK) as of 2026-06 — star and version numbers are date-sensitive and shift release-to-release; treat as indicative only.
- [未验证] The "secure container runtime" support (gVisor/Kata/Firecracker) is claimed in the README; the exact maturity, configuration burden, and isolation guarantees of each were not verified against the source.
- [推断] Alibaba origin is inferred from README badges/links pointing to `github.com/alibaba/OpenSandbox`; the canonical repo is now under `opensandbox-group`. The precise ownership/transfer and governance reality were not confirmed.
- [推断] "Months old + very high stars" is treated as a hype/risk signal per the read-repo methodology, not a verdict on quality; the project may mature, but its Lindy track record does not exist yet.
- [未验证] Comparisons to E2B/Daytona reflect general positioning, not a measured feature-by-feature benchmark.
