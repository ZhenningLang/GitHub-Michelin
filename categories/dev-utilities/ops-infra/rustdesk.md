---
name: RustDesk
slug: rustdesk
repo: https://github.com/rustdesk/rustdesk
category: ops-infra
tags: [remote-desktop, self-hosted, rust, p2p, cross-platform, flutter, remote-control]
language: Rust
license: AGPL-3.0
maturity: active, ~117.4k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-06T09:05:11Z
  default_branch: master
  default_branch_sha: 28930c04635ffbc487175b2b0d62e64fd40ba892
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:13:57Z
  overall: A
  overall_score: 3.5
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
        median_ttfr_hours: 2.9
        qualifying_issues: 9
        band: relaxed_solo
        window_offset_days: 13
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: null
        canonical_package: null
        homebrew_installs_90d: 7952
        homebrew_tier: A
        release_downloads: 73098075
        release_assets: 735
        release_tier: A
        signal_basis: homebrew+releases
    longevity:
      grade: A
      raw:
        repo_age_days: 2185
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 135
        top1_share: 0.255
        top3_share: 0.563
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: D
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
---

# RustDesk

An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer and AnyDesk — built in Rust with a Flutter UI, supporting P2P connections and a self-hosted relay server.

![RustDesk — health radar](../../../assets/health/rustdesk.svg)

## When to use

You're a developer or sysadmin who needs remote access to your own machines — a home server, a workstation in the office, or a family member's PC — and you want to own the infrastructure, not rent it. You pick RustDesk over TeamViewer or AnyDesk because you refuse to pay recurring subscriptions and route your screen data through a third-party cloud you don't control. You pick it over Chrome Remote Desktop because you need a self-hosted option that doesn't lock you into a Google account. You pick it over TightVNC or TigerVNC because you need modern encryption, NAT traversal, and mobile clients out of the box, not raw VNC protocol over a LAN. You install RustDesk on both ends, optionally spin up a small relay server on a VPS, and connect directly with end-to-end encryption. It runs on Windows, macOS, Linux, Android, and iOS, supports file transfer, clipboard sync, and multiple monitors, and the Flutter UI gives it a native feel on each platform.

## When NOT to use

- If you need enterprise-grade support, SLA, or compliance certification, use TeamViewer or AnyDesk enterprise instead of RustDesk, because RustDesk is a community-driven project with no formal support contract, guaranteed response times, or compliance documentation.
- If you want a fully cloud-managed zero-config solution, use Chrome Remote Desktop or TeamViewer instead of RustDesk, because RustDesk's primary value is self-hosting; managing a relay server is extra work you don't need if you just want to install and forget.
- If you need advanced session recording, audit logging, or granular RBAC, use enterprise remote-access platforms like TeamViewer enterprise instead of RustDesk, because RustDesk provides only basic access control and password protection.
- If you need high-performance remote gaming or video editing, use Sunshine + Moonlight instead of RustDesk, because RustDesk is not optimized for low-latency gaming or high-frame-rate video editing remoting.
- If you need seamless Wayland support on Linux, use Chrome Remote Desktop or another alternative instead of RustDesk, because RustDesk's Linux support has historically been stronger on X11. [推断]
- If AGPL-3.0 is incompatible with your use case, use TightVNC or a permissively licensed alternative instead of RustDesk, because the AGPL-3.0 license may restrict how you integrate, distribute, or modify the software in proprietary contexts.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| TeamViewer | 未收录 | Use RustDesk for self-hosted, open-source remote desktop; choose TeamViewer when you need a commercial, cloud-managed remote desktop with enterprise support and cross-platform reliability. | Commercial, cloud-managed remote desktop with enterprise support, session recording, and compliance; requires paid subscription and routes data through their cloud. |
| AnyDesk | 未收录 | Use RustDesk for self-hosted, open-source remote desktop; choose AnyDesk when you want a lightweight, fast proprietary remote desktop with a free tier for personal use. | Lightweight proprietary remote desktop with a free personal tier; fast and simple but closed-source and cloud-dependent. |
| Chrome Remote Desktop | 未收录 | Use RustDesk for self-hosted, open-source remote desktop; choose Chrome Remote Desktop when you want a free, browser-based remote desktop tied to your Google account. | Free, browser-based remote desktop tied to Google account; very simple but requires Google ecosystem and offers no self-hosting. |
| TightVNC / TigerVNC | 未收录 | Use RustDesk for self-hosted, open-source remote desktop with modern encryption; choose TightVNC when you need a traditional VNC server for LAN-based remote access without encryption by default. | Traditional VNC for LAN access; simple and protocol-standard but lacks modern encryption, NAT traversal, and mobile clients without extra setup. |
| Sunshine + Moonlight | 未收录 | Use RustDesk for general-purpose self-hosted remote desktop; choose Sunshine + Moonlight when you need low-latency game streaming or high-frame-rate remote desktop. | Open-source game-streaming host (Sunshine) and client (Moonlight) optimized for low latency and high FPS; narrower use case than general remote desktop. |

## Tech stack

- **Language:** Rust (core engine and networking) with a Flutter/Dart cross-platform UI layer for desktop and mobile.
- **Networking:** P2P with NAT traversal (using hole-punching) and fallback to a relay server when direct connection fails; encrypted with TLS 1.3.
- **UI:** Flutter provides a single codebase for Windows, macOS, Linux, Android, and iOS with platform-native rendering.
- **Media:** Custom video codec pipeline for screen capture and remote display; handles multiple monitors and resolutions.
- **Build:** Rust compiles to native binaries; Flutter bundles the UI assets. Flatpak and other distribution formats are supported.

## Dependencies

- **Client hardware:** A device with a screen and network connection running Windows, macOS, Linux, Android, or iOS. The client app is a native binary installed locally.
- **Server / relay (optional):** For direct P2P, no server is required. For relay fallback or always-on access, you need a small VPS or server to run the `rustdesk-server` relay and ID/registry services. Minimal specs: ~1 CPU, 512 MB RAM, modest bandwidth.
- **Network:** Both sides need internet access (or LAN access for direct P2P). The relay server needs a public IP and open ports (TCP/UDP). Firewalls and NAT must allow the connection path.
- **No external database:** The relay server does not require a database; it is a lightweight stateful daemon.

## Ops difficulty

**Low** for direct P2P personal use: install the client on both machines, exchange the ID and password, and connect. **Medium** for self-hosted relay: you need to deploy the `rustdesk-server` binary (or Docker container) on a VPS, open the required ports, and configure DNS/SSL if you want a branded relay. The main operational concerns are:
- **Security:** You must manage the relay server's access, keep it patched, and rotate keys/passwords. The default setup uses simple password protection; for production, consider additional hardening (fail2ban, VPN overlay, key-based auth).
- **NAT/firewall traversal:** Some corporate networks block P2P traffic, forcing all connections through the relay — which then becomes a bandwidth bottleneck.
- **Updates:** The client and relay must stay version-compatible; mismatched versions can cause connection failures.

## Health & viability
- **Maintenance**: Grade A — 13/13 active weeks in trailing 13; last commit 0 days ago.
- **Responsiveness**: Grade A — median first-response time 6.6 hours across 15 qualifying issues/PRs.
- **Adoption**: Cannot be scored — unknown.
- **Longevity**: Grade A — 2,104 days old.
- **Governance**: Grade A — top-3 contributor share 53.3% (?).
- **Risk / License**: Grade D — AGPL-3.0 license.
## Caveats (unverified)

- [未验证] ~117.4k GitHub stars as of 2026-07-01; star counts are approximate and time-sensitive.
- [未验证] The relay server resource requirements and exact port numbers are inferred from typical self-hosting guides; verify the current `rustdesk-server` docs for production deployment.
- [未验证] TLS 1.3 and encryption details are summarized from the project description; confirm the current encryption protocol and key management for your security review.
- [未验证] Wayland support status and specific compositor compatibility are evolving; test on your target Linux distribution before deploying.
- [推断] Session recording, audit logging, and RBAC are not core features; if compliance requires these, you will need to supplement RustDesk with additional tooling.
- [推断] P2P hole-punching success rate varies by network topology (symmetric NAT, corporate firewalls); plan for relay fallback in restrictive environments.
