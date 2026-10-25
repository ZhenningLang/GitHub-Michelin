# Stable Video Infinity：来源与许可保留待裁决

**结果为 proposed，未建正式选型页，保留标签。** 2026-10-25研究的默认分支固定于 `557afca50d5766514c67ae39000b03e0dd66d6e5`。本批没有得到对此项目的带警告信息收录豁免；此前四项放行不自动适用。

## 不是因论文或风险拒收

仓库有真实的训练、推理和可复用模型管线，不是只有论文、网页或演示视频。已读的 `train_svi.py`、`test_svi.py`、`diffsynth/pipelines/svi_video.py` 合计2457行，包含历史误差注入、分桶存储、训练损失与逐段视频接续。DiffSynth 是其复用引擎，不是 SVI 算法的同等替代；EverAnimate 也未被证实为继任仓库。

## 可复核的资格疑点

主会话重新计算两份固定Git树，得到以下结果。

| 检查 | 结果 | 固定来源 |
|---|---|---|
| 全树同源 | 319个blob中191个与DiffSynth-Studio v1.1.2完全同SHA | [SVI固定树](https://github.com/vita-epfl/Stable-Video-Infinity/tree/557afca50d5766514c67ae39000b03e0dd66d6e5)；[DiffSynth固定树](https://github.com/modelscope/DiffSynth-Studio/tree/a66203a3914b6ee54240b3cdd1b03408c4f11ec7) |
| Python同源 | 202个Python文件中140个完全同blob | 同上，不凭相似名称推断 |
| SVI根许可 | 实际MIT文本，署名VITA lab at EPFL | [LICENSE](https://github.com/vita-epfl/Stable-Video-Infinity/blob/557afca50d5766514c67ae39000b03e0dd66d6e5/LICENSE) |
| 基础引擎许可 | Apache-2.0；再分发要求向接收者提供许可副本 | [DiffSynth许可第89–128行](https://github.com/modelscope/DiffSynth-Studio/blob/a66203a3914b6ee54240b3cdd1b03408c4f11ec7/LICENSE#L89-L128) |
| 许可文件保留 | SVI固定树中，按license／copying／notice名称查找仅有根MIT文件，未保留对应Apache许可文件 | SVI固定树与许可证正文 |

以上命中本索引 worth-check 的“多数同源”和“原许可保留”门槛。它不证明 SVI 没有原创工作，也不构成侵权、整个MIT无效或所有用途被禁止的法律判断。维护者可裁决是否允许带明确警告作信息收录；这种裁决依然不能替代权利人的授权或补齐上游分发义务。

检查范围有边界：文件名与blob对比覆盖完整固定树；许可正文检索只覆盖已缓存的17个SVI文本文件，未穷尽319个文件中可能存在的其它嵌入形式。因此将其记录为待核的许可保留差异，而不是断言“所有分发渠道都没有提供许可副本”。

## 已核的采用边界

- 默认分支基于Wan2.1，另一个 `svi_wan22` 分支的SVI2.0 Pro仅阅读了文档。不用默认分支旧实现倒证Pro新增能力。
- [训练误差桶](https://github.com/vita-epfl/Stable-Video-Infinity/blob/557afca50d5766514c67ae39000b03e0dd66d6e5/train_svi.py#L776-L938)与[损失更新](https://github.com/vita-epfl/Stable-Video-Infinity/blob/557afca50d5766514c67ae39000b03e0dd66d6e5/train_svi.py#L1099-L1183)训练视频扩散网络，不是修改coding-agent技能的RSI优化器。
- [推理](https://github.com/vita-epfl/Stable-Video-Infinity/blob/557afca50d5766514c67ae39000b03e0dd66d6e5/test_svi.py#L395-L483)逐段接续并保留累积视频。任意长、不漂移、显存和速度均未在本机验证，不能写成保证。
- [提示文件读取](https://github.com/vita-epfl/Stable-Video-Infinity/blob/557afca50d5766514c67ae39000b03e0dd66d6e5/test_svi.py#L31-L60)对赋值形式文本使用Python `exec`；不可信提示文件具有代码执行风险。没有执行该入口。
- 代码、SVI权重、Wan基础模型、数据集和人物素材的许可分别核对。根MIT不代替全部材料的商用权利；公开benchmark卡未声明license字段。

没有生成双语选型页、图卡、健康评分或索引行。资料员的基线 `make gates` 为零错误，只证明未改内容的仓库仍通过，不计成该项目页面验收。没有下载权重或数据，没有安装、训练、推理、启动Gradio，也没有修改个人harness。
