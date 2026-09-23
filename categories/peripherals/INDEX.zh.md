# peripherals

> 分类节点。配置并驱动桌面外设——罗技鼠标、键盘、接收器、灯与摄像头——通过 HID++ 与 UVC。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **OpenLogi** | 当你想要 Options+ 那套功能——按应用 profile、手势、键盘重映射、静态 RGB、摄像头控制——在 macOS、Linux、Windows 上用同一份 TOML 配置拿到，并且能接受一个尚未 1.0、只有几个月历史、没有接收器配对的项目时用它。 | C（5/6） | [→](openlogi.zh.md) |
| **Solaar** | 在 Linux 上当任务本身是设备管理而不是重映射时用它：配对与解绑接收器、读取电量与设备状态、修改 HID++ 设置——背后是 14 年仍在发版的记录；代价是仅限 Linux，且没有摄像头与 RGB。 | B（6/6） | [→](solaar.zh.md) |
| **Mouser** | 当你想要在 Windows／macOS／Linux 上用便携压缩包按应用重映射罗技 HID++ 鼠标，不需要安装器、账号或服务，并且不要求配对、键盘、摄像头或按设备映射时用它。 | B（6/6） | [→](mouser.zh.md) |
| **logiops** | 在 Linux 上，当你想要一个读单份声明式 `/etc/logid.cfg` 的 root systemd 守护进程而不是 GUI 时用它——接受只支持 HID++ 2.0+ 鼠标、没有应用感知，且开发自 2024 年起实际已停。 | C（5/6） | [→](logiops.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [OpenLogi](openlogi.zh.md) | ✅ | C（5/6） | 四者中覆盖面最广——鼠标、键盘、摄像头、灯效，三个系统，GUI + CLI + TOML——但处于 1.0 之前，没有配对，且只有一位所有者。 |
| [Solaar](solaar.zh.md) | ✅ | B（6/6） | 成熟的 Linux 设备管理器：配对、状态与设置，14 年记录；没有摄像头、没有 RGB、没有按应用 profile，且以 Linux 为先。 |
| [Mouser](mouser.zh.md) | ✅ | B（6/6） | 只管鼠标且便携：三个系统解压即用，支持按应用 profile；没有配对、映射为全局、7 个月历史。 |
| [logiops](logiops.zh.md) | ✅ | C（5/6） | 守护进程加配置文件，没有 GUI：在 Linux 上稳定、可打包，但开发近乎休眠，且只支持 HID++ 2.0+。 |
| Logitech Options+／G HUB | 未收录 | — | 官方闭源应用，也是唯一具备 Flow、固件更新与厂商质量保证的选项——仅 Windows／macOS，没有 Linux。 |

## 什么该放这里

**自己配置或驱动已连接桌面外设**的程序——通过设备自身的协议（罗技是 HID++，摄像头是 UVC）读写设备设置，包括接收器配对、按键／手势映射、DPI、灯效与输入注入。

不放这里：

- **按坐标／像素脚本化操作 GUI**——见 `desktop-automation`。本分类跟硬件协议对话，不对屏幕像素或窗口控件下手。
- **自动化浏览器或网页**——见 `web-automation`。
- **多厂商游戏鼠标配置守护进程**（如 libratbag／Piper）——形状相同（守护进程加配置前端），但协议不同；尚未收录。
