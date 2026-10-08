# captcha

> 分类节点。CAPTCHA / 机器人检测挑战（工作量证明、点击、行为式）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Cap** | 轻量、可自托管的 CAPTCHA 替代：无感工作量证明（Rust→WASM worker 做 SHA-256 nonce 搜索）发放服务端可校验 token——无图片、不调第三方。 | C（5/6） | [→](capjs.zh.md) |
| **Text_select_captcha** | 当经授权的自动化要解中文文字点选验证码、想在纯 CPU 上跑（YOLO 检测加孪生网络匹配，走 ONNX）时用它——但仓库没有 LICENSE 文件，默认保留所有权利，合法性是第一道门槛。 | D（5/6） | [→](text-select-captcha.zh.md) |
| **pytorch-captcha-recognition** | 想要一份可读的定长文字验证码教学基线（每个字符位一个 CNN 分类头）时用它——但它是 2020 年冻结的教程，PyTorch API 需要现代化改造，准确率数字也只来自它自己的合成数据。 | D（4/6） | [→](pytorch-captcha-recognition.zh.md) |
| **captcha (lepture)** | 当 Python 表单需要一个自托管、不调第三方的图片或语音验证码，而存储、过期和校验你打算自己写时用它——但扭曲文字挡不住廉价 OCR，只能当减速带，算不上机器人防护。 | B（5/6） | [→](lepture-captcha.zh.md) |
| **NopeCHA** | 仅在明确授权的浏览器自动化需要无人值守覆盖多类验证码时使用；它依赖托管服务，持续维护的扩展源码也已关闭。 | B（6/6） | [→](nopecha-extension.zh.md) |
| **Buster** | 当真人需要源码可审计的 reCAPTCHA 音频辅助，或你在做明确授权的无障碍测试时用它；它由人工触发且只覆盖 reCAPTCHA，不适合作为确定性 CI 或广泛无人值守识别。 | C（6/6） | [→](buster.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Cap](capjs.zh.md) | ✅ | C（5/6） | 轻量、可自托管的 CAPTCHA 替代：无感工作量证明（Rust→WASM worker 做 SHA-256 nonce 搜索）发放服务端可校验 token——无图片、不调第三方。 |
| [Text_select_captcha](text-select-captcha.zh.md) | ✅ | D（5/6） | 换来一条现成的检测加匹配管线，约 300 张标注图就能重训；代价是没有任何使用授权、单作者维护、准确率只是自报。 |
| [pytorch-captcha-recognition](pytorch-captcha-recognition.zh.md) | ✅ | D（4/6） | 换来在学 CTC 或 seq2seq 之前最简单的多头设计范例；代价是不支持变长或扭曲验证码，也没有在维护、可安装的 API。 |
| [captcha (lepture)](lepture-captcha.zh.md) | ✅ | B（5/6） | 换来一个只依赖 Pillow、挑战生命周期全由你掌控的渲染器；代价是状态与校验全得自己写，且毫无对抗鲁棒性。 |
| [NopeCHA](nopecha-extension.zh.md) | ✅ | B（6/6） | 面向明确授权的多类验证码无人值守浏览器识别；覆盖广，但依赖托管服务，持续维护的扩展源码也已关闭。 |
| [Buster](buster.zh.md) | ✅ | C（6/6） | 真人触发、源码可审计的 reCAPTCHA 音频辅助；比识别服务更窄，也不适合作为确定性 CI 判定器。 |
| hCaptcha / Cloudflare Turnstile / Friendly Captcha / Altcha | 未收录 | — | 页面里点到的其他 CAPTCHA / 机器人检测服务。 |

## 什么该放这里

**CAPTCHA / 机器人检测**挑战系统——工作量证明、点击或行为式。本宽泛索引里的一个独立领域。
