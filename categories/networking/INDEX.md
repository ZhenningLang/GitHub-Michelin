# networking

> Category node. Networking libraries — SSH, DNS, tunnels, RPC, and traffic shaping.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Paramiko** | Use it when Python code must open SSH/SFTP connections and run remote commands programmatically — but it's pure-Python (slower than OpenSSH), threading-only, and LGPL-2.1. | B (6/6) | [→](paramiko.md) |
| **sshtunnel** | Use it only when an existing Python script already relies on its with-block SSH port forward to a database behind a bastion — a fresh install breaks on Paramiko 4+, and there has been no release since 2021. | B (4/6) | [→](sshtunnel.md) |
| **dnspython** | Use it when Python needs arbitrary record types, custom resolvers, zone transfers, DNSSEC, or DoH/DoT — but it bypasses /etc/hosts and the OS resolver, requires Python 3.10+, and is a library not a CLI. | A (5/6) | [→](dnspython.md) |
| **wondershaper** | Use it when one Linux NIC needs a quick overall up/down bandwidth ceiling without learning tc syntax — but it builds HTB/sfq rules rather than bufferbloat-aware cake or fq_codel, has no per-flow QoS, and has been dormant since 2021. | E (4/6) | [→](wondershaper.md) |
| **ThriftPy** | Use it only to understand a legacy service still importing thriftpy before migrating — the repo is archived and deprecated, so all new Thrift work should go to the maintained thriftpy2. | B (5/6) | [→](thriftpy.md) |
| **amneziawg-installer** | Use it when DPI blocks plain WireGuard on your network and you want a one-command, in-kernel AmneziaWG server on a clean cheap VPS — but it's Ubuntu/Debian-only, needs AWG-2.0-capable clients, and rebuilds the box into a single-purpose hardened VPN server. | B (6/6) | [→](amneziawg-installer.md) |
| **dae** | Use it when a Linux router or host must split-route a whole LAN between direct and proxy nodes and you want direct traffic forwarded in-kernel via eBPF — but it needs kernel 5.17+, has no GUI or SOCKS/HTTP inbound, and is AGPL-3.0. | B (6/6) | [→](dae.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Paramiko](paramiko.md) | ✅ | B (6/6) | Use it when Python code must open SSH/SFTP connections and run remote commands programmatically — but it's pure-Python (slower than OpenSSH), threading-only, and LGPL-2.1. |
| [sshtunnel](sshtunnel.md) | ✅ | B (4/6) | A context-managed tunnel that opens and closes with your code, at the cost of pinning paramiko below 4 and forgoing its security releases; for new code, write the forward on Paramiko or AsyncSSH. |
| [dnspython](dnspython.md) | ✅ | A (5/6) | Use it when Python needs arbitrary record types, custom resolvers, zone transfers, DNSSEC, or DoH/DoT — but it bypasses /etc/hosts and the OS resolver, requires Python 3.10+, and is a library not a CLI. |
| [wondershaper](wondershaper.md) | ✅ | E (4/6) | Buys a one-line throttle from a single script; costs latency quality under load and fine-grained control — hand-written tc or OpenWrt SQM do both better. |
| [ThriftPy](thriftpy.md) | ✅ | B (5/6) | Use it only to understand a legacy service still importing thriftpy before migrating — the repo is archived and deprecated, so all new Thrift work should go to the maintained thriftpy2. |
| [amneziawg-installer](amneziawg-installer.md) | ✅ | B (6/6) | Use it when DPI blocks plain WireGuard on your network and you want a one-command, in-kernel AmneziaWG server on a clean cheap VPS — but it's Ubuntu/Debian-only, needs AWG-2.0-capable clients, and rebuilds the box into a single-purpose hardened VPN server. |
| [dae](dae.md) | ✅ | B (6/6) | Use it when a Linux router or host must split-route a whole LAN between direct and proxy nodes and you want direct traffic forwarded in-kernel via eBPF — but it needs kernel 5.17+, has no GUI or SOCKS/HTTP inbound, and is AGPL-3.0. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

Libraries/tools for **network protocols and links** — SSH, DNS, tunnels, RPC, bandwidth shaping, transparent proxying and policy routing.
