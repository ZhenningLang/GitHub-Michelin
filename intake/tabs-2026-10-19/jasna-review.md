# Jasna 补丁语义审查

放行 `Kruk2/jasna`。没有必须修复的实质缺陷。

- `allowed`：`["Kruk2/jasna"]`
- `blocked`：`[]`
- 补丁 SHA256：`1ce58cdd50889fa85e7ff476cc2171025b4cd2c3cf7d588c9be6ec5485e0578d`
- 固定上游提交：`099af50a3aac06f14db8d048efd8c6562e2c3d25`
- 补丁：`/Users/zhenninglang/Projects/oss-atlas-tabs-2026-10-19-worker-3-results/kruk2--jasna.patch`

裁决只绑定此补丁。前两项已验收，不重审、不修改其报告。研究正文实际文件名为结果目录中的 `research.md`。

## 必须修复

无。已披露的私有组件、混合许可和可选网络功能，不构成拒收理由。

## 可选改进

无新增实质建议。不追加文风修改。

## 覆盖范围与取证

完整阅读了补丁内双语作者正文，以及 `flows/jasna.json`、`mechanisms/jasna.json`。同时阅读结果 JSON 与研究正文，逐项复核关键边界源码、许可通知和比较材料。

独立重新计算全部 44 份缓存文件的 Git blob SHA，并同时对照 `source-verification.json` 和固定提交的 `tree.json`：**44/44 匹配，零差异，树未截断**。这是原始文件身份核验，不是仅信任作者的 manifest 自述。没有运行这些文件。

## 关键语义裁决

| 边界 | 固定来源与裁决 |
|---|---|
| 公开源码与官方包 | `LICENSING.md:9–20,39–56`、`docs/en/development.md:6–10`、`jasna/license_api.py:12–22` 支撑免费 BasicVSR++ 可独立使用。`jasna/__main__.py:16–24` 的 Linux／Windows 打包入口却先初始化私有运行时。双语页明确区分这两条路径，并指出许可文档的免费 CLI 声明较窄，没有把所有官方包说成纯公开源码。 |
| 付费组件与混合许可 | `assets/THIRD_PARTY_LICENSES.md:41–72`、`assets/THIRD_PARTY_MODELS.md:6–43,87–97` 区分 AGPL 默认、MMagic 的 Apache、LTX Community、模型及厂商条款、专有支持者产物。页面没有把全树或发布包统称 AGPL，也未仅凭混用断言违法。LTX 精确来源与整包许可兼容性仍列为未确立。 |
| 可复现边界 | `RELEASE_SOURCES.md:1–9,78–84` 仍描述 v0.11.1，`pyproject.toml:7` 已为 0.11.3。页面区分当前源码、v0.11.2 发布和旧对应文档，没有声称公开检出能重建完整官方可执行文件。 |
| 流媒体监听与鉴权 | `jasna/streaming.py:125–288,628–641` 显示监听全部接口、无 handler 鉴权、通配 CORS、可经 `/open` 指定已有本地媒体路径；第 27 行加载公共 CDN 脚本。页面给出防火墙或隔离建议，没有把打印 localhost 当访问限制，也没有把静态阅读说成已验证攻击。 |
| 真实默认值 | `jasna/main.py:505–509` 的流媒体是显式启用项。第 591–609 行的导出动作默认 `none`，命令默认为空；`post_export_action.py:42–53` 在 `none` 时直接返回，其余分支才关机或启动 shell。页面明确要求按需授权，不曾声称默认自动执行命令或自动关机。 |
| 生成不等于恢复真实细节 | 修复器 `basicvsrpp_mosaic_restorer.py:55–69` 通过模型生成裁剪帧输出。双语第 94 行明确排除取证级原像素恢复；存疑账本说明看似合理也未必对应被遮住原件。没有照抄 README 对“真实细节”的宣传。 |
| 合法授权与保留原件 | 双语使用场景、快速上手、flow 输入和 mechanism 输入都限制为有权处理的媒体，要求检查结果并保留原件。无需为同一边界再堆一条同义禁用场景。 |
| 三项实现机制 | `clip_tracker.py:190–264` 确认框重叠关联与两倍边界续段；`pipeline_processing.py:62–117,143–159` 确认保留区间、淡化与切镜清空；`frame_queue.py:17–35` 确认按帧数阻塞，但空队列可接纳超预算项目。页面没有承诺绝对显存上限、真实物体身份或无伪影。 |

私有保护实现未公开，因此不能独立认证其激活传输、遥测或设备身份处理。页面已保留这条限制；公开源码中的调用入口不能证明私有实现没有网络行为。

## 分类与比较

保留 `categories/media-processing/` 合理。已检查 `video-audio` 与 `image-processing` 的范围：前者面向应用层以下工具，后者面向图像处理；Jasna 是跨视频和图像的修复应用，不是 NLE 或编解码包装器。没有更准确的现有窄类需要强制迁入。

全库检索没有发现已有 Lada、Video2X 或 Real-ESRGAN 项目页；出现的引用不是独立条目。已读 Lada 与 Video2X 的缓存 README，并打开已收录 FFmpeg 页：比较覆盖最接近的马赛克修复替代，以及整体放大／补帧和确定性媒体变换。没有遗漏更近的已收录替代。

Lada README 的 CPU 路径明确很慢。页面用“评估”而非性能承诺；也没有把 Jasna 的旧版作者跑分当当前硬件保证。

## 图源与机器核验

flow 描述授权媒体输入到导出的使用交接；mechanism 描述跟踪、队列及公开／受保护修复路径。作者正文分别解释三个机制的边界与源码。生成图文不是额外研究来源，页面也没有这样使用它们。

只在内存解析补丁，使用本索引的纯文本生成函数对照生成块；未导入上游模块。机器关键输出：

```text
fixed_sha=099af50a3aac06f14db8d048efd8c6562e2c3d25
checked=44; mismatches=[]; tree_truncated=False
en: authored_techniques=3; flow_text=exact; mechanism_text=exact; mechanism_stamp=match; SVG_XML=valid
zh: authored_techniques=3; flow_text=exact; mechanism_text=exact; mechanism_stamp=match; SVG_XML=valid
patchsha256=1ce58cdd50889fa85e7ff476cc2171025b4cd2c3cf7d588c9be6ec5485e0578d
```

六张 SVG 通过 XML 解析；未做浏览器视觉验收。未安装、激活或执行上游代码、模型、测试、媒体；未读个人数据，未启动服务、探测接口或做攻击。运行质量、速度、私有二进制行为和法律兼容性不在本次验证范围内。

本审查只新增 `jasna-review.md` 与 `jasna-review.json`。未改补丁、categories、README、ledger 或前两项报告。主会话继续逐仓库门禁与交付。
