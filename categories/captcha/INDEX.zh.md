# captcha

> 分类节点。CAPTCHA / 机器人检测挑战（工作量证明、点击、行为式）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Cap** | 轻量、可自托管的 CAPTCHA 替代：无感工作量证明（Rust→WASM worker 做 SHA-256 nonce 搜索）发放服务端可校验 token——无图片、不调第三方。 | B（5/6） | [→](capjs.zh.md) |
| **Text_select_captcha** | 当要自动识别中文文字点选验证码（YOLO＋孪生网络，纯 CPU）时用它——仓库无 LICENSE 文件，默认保留所有权利，合法性是决定性门槛。 | D（5/6） | [→](text-select-captcha.zh.md) |
| **pytorch-captcha-recognition** | 当需要定长图片验证码（多头 CNN）的可读教学基线时用它——这是 2020 年冻结的教程，要预期改造过时的 PyTorch API。 | D（4/6） | [→](pytorch-captcha-recognition.zh.md) |
| **captcha (lepture)** | 当 Python 表单需要自托管、无第三方调用的图片／音频验证码渲染器时用它——它只渲染且抵不住现代 OCR，只能当 UX 减速带，而非安全控制。 | B（5/6） | [→](lepture-captcha.zh.md) |
| **NopeCHA** | 仅在明确授权的浏览器自动化需要无人值守覆盖多类验证码时使用；它依赖托管服务，持续维护的扩展源码也已关闭。 | B（6/6） | [→](nopecha-extension.zh.md) |
| **Buster** | 当真人需要源码可审计的 reCAPTCHA 音频辅助，或你在做明确授权的无障碍测试时用它；它由人工触发且只覆盖 reCAPTCHA，不适合作为确定性 CI 或广泛无人值守识别。 | B（5/6） | [→](buster.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Cap](capjs.zh.md) | ✅ | B（5/6） | 轻量、可自托管的 CAPTCHA 替代：无感工作量证明（Rust→WASM worker 做 SHA-256 nonce 搜索）发放服务端可校验 token——无图片、不调第三方。 |
| [Text_select_captcha](text-select-captcha.zh.md) | ✅ | D（5/6） | 当要自动识别中文文字点选验证码（YOLO＋孪生网络，纯 CPU）时用它——仓库无 LICENSE 文件，默认保留所有权利，合法性是决定性门槛。 |
| [pytorch-captcha-recognition](pytorch-captcha-recognition.zh.md) | ✅ | D（4/6） | 当需要定长图片验证码（多头 CNN）的可读教学基线时用它——这是 2020 年冻结的教程，要预期改造过时的 PyTorch API。 |
| [captcha (lepture)](lepture-captcha.zh.md) | ✅ | B（5/6） | 当 Python 表单需要自托管、无第三方调用的图片／音频验证码渲染器时用它——它只渲染且抵不住现代 OCR，只能当 UX 减速带，而非安全控制。 |
| [NopeCHA](nopecha-extension.zh.md) | ✅ | B（6/6） | 面向明确授权的多类验证码无人值守浏览器识别；覆盖广，但依赖托管服务，持续维护的扩展源码也已关闭。 |
| [Buster](buster.zh.md) | ✅ | B（5/6） | 真人触发、源码可审计的 reCAPTCHA 音频辅助；比识别服务更窄，也不适合作为确定性 CI 判定器。 |
| hCaptcha / Cloudflare Turnstile / Friendly Captcha / Altcha | 未收录 | — | 页面里点到的其他 CAPTCHA / 机器人检测服务。 |

## 什么该放这里

**CAPTCHA / 机器人检测**挑战系统——工作量证明、点击或行为式。本宽泛索引里的一个独立领域。
