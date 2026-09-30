# security

> Leaf of [agent-skills](../INDEX.md). Security review, threat modeling, cybersecurity playbooks.
> ← up to [agent-skills](../INDEX.md) · root [route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Collections in this leaf

| Collection | Use when | Health | Page |
| --- | --- | --- | --- |
| **Anthropic Cybersecurity Skills** | A large (~817 skill) cybersecurity skill pack of SKILL.md runbooks cross-mapped to MITRE ATT&CK, NIST CSF, ATLAS, D3FEND, NIST AI RMF and MITRE F3, loaded on demand into a coding agent. | B (4/5) | [→](anthropic-cybersecurity-skills.md) |
| **reverse-skill** | Use it when your AI coding client needs a router to 45 RE/pentest/CTF playbooks with an authorization gate and evidence-chain reporting — dual-use content that trips AV and requires trusting third-party agent-executable instructions. | A (4/5) | [→](reverse-skill.md) |
| **android-reverse-engineering** | Use it when you must document the HTTP API surface of an Android APK/XAPK/JAR/AAR from its binary alone — a Claude Code plugin that decompiles with jadx/Fernflower, recovers Kotlin class names R8 hid, and sweeps Retrofit/OkHttp/Ktor/Apollo for endpoints and auth. | B (4/5) | [→](android-reverse-engineering.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Anthropic Cybersecurity Skills](anthropic-cybersecurity-skills.md) | ✅ | B (4/5) | A large (~817 skill) cybersecurity skill pack of SKILL.md runbooks cross-mapped to MITRE ATT&CK, NIST CSF, ATLAS, D3FEND, NIST AI RMF and MITRE F3, loaded on demand into a coding agent. |
| [reverse-skill](reverse-skill.md) | ✅ | A (4/5) | Task router to 45 security playbooks with case-guard authorization and a 175-case routing benchmark; ships a WAF/EDR-bypass payload corpus that Defender flags as malware (#125) and an agent bootstrap whose auto-execution is disputed (#134). |
| [android-reverse-engineering](android-reverse-engineering.md) | ✅ | B (4/5) | Single-task Android pipeline: fingerprint → jadx/Fernflower decompile → R8 name recovery → endpoint sweep, returning a two-tier API doc without source code; no authorization gate, install script uses sudo and edits shell rc files (open disclosure #17), macOS bash-3.2 path broken (#30/#31). |

## What belongs here

Skill collections for **security work** — review, threat modeling, cybersecurity playbooks.
