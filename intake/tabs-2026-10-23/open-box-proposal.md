# Open-Box：公开仓库不等于开源产品

检查日为 2026-10-23 UTC；固定提交为 `eabc31f0d0653d23aadcd0b1794f2776bd2c7eac`。

**裁决：propose，保留标签，不生成开源选型页。** 主会话已复核 LICENSE 正文和资料员证据。不是因体量、年轻、单作者或网络代理功能拒收，而是产品本身明确非开源。

- [LICENSE 第 1–18 行](https://github.com/liandu2024/Open-Box/blob/eabc31f0d0653d23aadcd0b1794f2776bd2c7eac/LICENSE#L1-L18)明确自有代码与资产非开源；允许下载、部署及为自身部署修改公开脚本，不授权任意再分发整个产品。
- [第 20–43 行](https://github.com/liandu2024/Open-Box/blob/eabc31f0d0653d23aadcd0b1794f2776bd2c7eac/LICENSE#L20-L43)限制再分发、衍生专有版本及逆向；第三方原有开源权利和早期版本已获许可不因此撤销。
- [COPYRIGHT](https://github.com/liandu2024/Open-Box/blob/eabc31f0d0653d23aadcd0b1794f2776bd2c7eac/COPYRIGHT.md)与 README 将公开仓库定位为部署、发行和反馈入口。69 个公开文件中确有部署和验证资产，但自有核心与面板实现未在该树公开。没有把公开脚本误判成空仓库，也没有以 sing-box 的许可代替整包许可。

产品用于路由器和客户端的透明代理、DNS 与连接分流。公开安装入口需要高网络权限并会改变服务与防火墙；容器需 `NET_ADMIN`、`NET_RAW` 与 TUN。卸载默认保留数据，完整系统恢复未实测。核心未公开，本次不验证真实流量、隐私、性能与稳定性。

维护者可选择保持其为范围外产品线索，或要求针对真正可复用且具有明确开源许可的子组件另做资格研究；不能把专有整包标成开源。单独可研究 sing-box 和 zashboard，但本批不自动扩收它们。

没有安装、执行、解包上游、读取个人凭据或修改 harness。该网络产品没有新的个人助手工作流接入建议。页面验证不适用，零页 scoped scan 不算内容审查通过。
