# captcha

> Category node. CAPTCHA / bot-detection challenges (proof-of-work, click, behavioral).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Cap** | Lightweight self-hosted CAPTCHA alternative: an invisible proof-of-work challenge (SHA-256 nonce in a Rust→WASM worker) issuing a server-verifiable token — no images, no third-party calls. | B (5/6) | [→](capjs.md) |
| **Text_select_captcha** | Use it when automating Chinese click-to-select-text CAPTCHAs (YOLO + Siamese, CPU-only) — there's no LICENSE file, so all rights reserved and legality is the decisive filter. | D (5/6) | [→](text-select-captcha.md) |
| **pytorch-captcha-recognition** | Use it as a readable teaching baseline for fixed-length text-in-image CAPTCHAs via a multi-head CNN — it's a frozen 2020 tutorial, expect to modernize the dated PyTorch APIs. | D (4/6) | [→](pytorch-captcha-recognition.md) |
| **captcha (lepture)** | Use it when a Python web form needs a self-hosted image/audio CAPTCHA renderer with no third-party call — it's render-only and weak against modern OCR, treat it as a UX speed-bump, not security. | B (5/6) | [→](lepture-captcha.md) |
| **NopeCHA** | Use it only for explicitly authorized browser automation that needs unattended coverage across several CAPTCHA families; it depends on a hosted service, and the maintained extension source is closed. | B (6/6) | [→](nopecha-extension.md) |
| **Buster** | Use it when a person needs source-auditable reCAPTCHA audio assistance, or for an explicitly authorized accessibility test; it is human-triggered and reCAPTCHA-only, not deterministic CI or broad unattended solving. | B (5/6) | [→](buster.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Cap](capjs.md) | ✅ | B (5/6) | Lightweight self-hosted CAPTCHA alternative: an invisible proof-of-work challenge (SHA-256 nonce in a Rust→WASM worker) issuing a server-verifiable token — no images, no third-party calls. |
| [Text_select_captcha](text-select-captcha.md) | ✅ | D (5/6) | Use it when automating Chinese click-to-select-text CAPTCHAs (YOLO + Siamese, CPU-only) — there's no LICENSE file, so all rights reserved and legality is the decisive filter. |
| [pytorch-captcha-recognition](pytorch-captcha-recognition.md) | ✅ | D (4/6) | Use it as a readable teaching baseline for fixed-length text-in-image CAPTCHAs via a multi-head CNN — it's a frozen 2020 tutorial, expect to modernize the dated PyTorch APIs. |
| [captcha (lepture)](lepture-captcha.md) | ✅ | B (5/6) | Use it when a Python web form needs a self-hosted image/audio CAPTCHA renderer with no third-party call — it's render-only and weak against modern OCR, treat it as a UX speed-bump, not security. |
| [NopeCHA](nopecha-extension.md) | ✅ | B (6/6) | Authorized unattended browser solving across several CAPTCHA families; broad coverage, but dependent on a hosted service whose maintained extension source is closed. |
| [Buster](buster.md) | ✅ | B (5/6) | Human-triggered, source-auditable reCAPTCHA audio assistance; narrower than solver services and unsuitable as a deterministic CI oracle. |
| hCaptcha / Cloudflare Turnstile / Friendly Captcha / Altcha | 未收录 | — | Other CAPTCHA / bot-detection services named on the page. |

## What belongs here

**CAPTCHA / bot-detection** challenge systems — proof-of-work, click, or behavioral. A standalone domain in this broad index.
