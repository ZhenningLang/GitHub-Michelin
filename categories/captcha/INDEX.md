# captcha

> Category node. CAPTCHA / bot-detection challenges (proof-of-work, click, behavioral).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Cap** | Lightweight self-hosted CAPTCHA alternative: an invisible proof-of-work challenge (SHA-256 nonce in a Rust→WASM worker) issuing a server-verifiable token — no images, no third-party calls. | C (5/6) | [→](capjs.md) |
| **Text_select_captcha** | Use it when an authorized automation must solve Chinese click-the-characters CAPTCHAs on CPU (YOLO detection plus Siamese matching via ONNX) — but the repo has no LICENSE file, so all rights are reserved, and legality decides first. | D (5/6) | [→](text-select-captcha.md) |
| **pytorch-captcha-recognition** | Use it as a readable teaching baseline for fixed-length text CAPTCHAs, one CNN head per character — but it is a frozen 2020 tutorial whose PyTorch APIs need modernizing, and its accuracy claims come from its own synthetic data. | D (4/6) | [→](pytorch-captcha-recognition.md) |
| **captcha (lepture)** | Use it when a Python web form needs a self-hosted image or audio CAPTCHA with no third-party call and you will write storage, expiry and verification yourself — but distorted text falls to cheap OCR, so it is a speed bump, not bot defense. | B (5/6) | [→](lepture-captcha.md) |
| **NopeCHA** | Use it only for explicitly authorized browser automation that needs unattended coverage across several CAPTCHA families; it depends on a hosted service, and the maintained extension source is closed. | B (6/6) | [→](nopecha-extension.md) |
| **Buster** | Use it when a person needs source-auditable reCAPTCHA audio assistance, or for an explicitly authorized accessibility test; it is human-triggered and reCAPTCHA-only, not deterministic CI or broad unattended solving. | C (6/6) | [→](buster.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Cap](capjs.md) | ✅ | C (5/6) | Lightweight self-hosted CAPTCHA alternative: an invisible proof-of-work challenge (SHA-256 nonce in a Rust→WASM worker) issuing a server-verifiable token — no images, no third-party calls. |
| [Text_select_captcha](text-select-captcha.md) | ✅ | D (5/6) | Buys a ready detection-plus-matching pipeline you can retrain on about 300 labeled images; costs any granted usage rights, with a solo author and self-reported accuracy. |
| [pytorch-captcha-recognition](pytorch-captcha-recognition.md) | ✅ | D (4/6) | Buys the simplest multi-head design to study before CTC or seq2seq; costs any support for variable-length or distorted CAPTCHAs and any maintained, installable API. |
| [captcha (lepture)](lepture-captcha.md) | ✅ | B (5/6) | Buys a Pillow-only renderer with full control of the challenge lifecycle; costs writing every piece of state and verification yourself, with no adversarial robustness. |
| [NopeCHA](nopecha-extension.md) | ✅ | B (6/6) | Authorized unattended browser solving across several CAPTCHA families; broad coverage, but dependent on a hosted service whose maintained extension source is closed. |
| [Buster](buster.md) | ✅ | C (6/6) | Human-triggered, source-auditable reCAPTCHA audio assistance; narrower than solver services and unsuitable as a deterministic CI oracle. |
| hCaptcha / Cloudflare Turnstile / Friendly Captcha / Altcha | 未收录 | — | Other CAPTCHA / bot-detection services named on the page. |

## What belongs here

**CAPTCHA / bot-detection** challenge systems — proof-of-work, click, or behavioral. A standalone domain in this broad index.
