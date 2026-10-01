# speech

> 分类节点。语音处理工具包（ASR、TTS、说话人任务）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **SpeechBrain** | 当你需要在一套统一的 PyTorch recipe 代码库上训练和适配语音模型（ASR、说话人识别、语音分离）时用它——但它以研究和训练为先，生产部署和跨版本 API 稳定性得你自己负责。 | B（5/6） | [→](speechbrain.zh.md) |
| **Voicebox** | 当你想要一个自托管的语音 I/O 工作室——克隆音色 TTS、热键 Whisper 听写、MCP/REST 让 agent 发声三合一，且是 MIT——时用它；但它是年轻的单人项目，发布节奏已停滞、自动粘贴目前仅 macOS。 | B（6/6） | [→](voicebox.zh.md) |
| **GPT-SoVITS** | 想要带 WebUI、且有训练路径可继续提升相似度的本地小样本声音克隆时用它；但它只管 TTS，听写、效果、agent 发声都不在其范围，且版本发布稀疏。 | A（5/6） | [→](gpt-sovits.zh.md) |
| **Coqui TTS（idiap 分支）** | 想要带 XTTS v2 克隆与广泛预训练模型覆盖的 Python TTS 库时用它；但它是 MPL-2.0、不提供应用外壳，且是一家已倒闭公司项目的社区分支。 | C（4/6） | [→](coqui-ai-tts.zh.md) |
| **AntSpeaker (MECT)** | 想用零训练的现成微型 PyTorch 检查点（380 万到 960 万参数）判断两段音频是否同一说话人时用它；但权重是 CC-BY-NC-SA（不可商用）、没有训练代码，且仓库是只活了两周的论文发布。 | C（3/6） | [→](antspeaker.zh.md) |
| **VoxCPM** | 想用代码和权重都是 Apache-2.0 的模型自托管声音克隆、或用文字描述设计音色（覆盖 30 种语言）时用它；但要备好约 8 GB 显存的 GPU，长文本得自己切句（单次长输出会漂移），并发服务还要另起引擎。 | B（5/6） | [→](voxcpm.zh.md) |
| **VoiceStudio** | 想要一个本地桌面应用把声音克隆、视频配音、听写和 agent 发声（MCP）一次装齐、还能切换十几个引擎时用它；但默认模型权重禁止商用，应用是 AGPL 且付费 Pro 档正在成形，项目只有半年历史、由一人维护。 | C（5/6） | [→](voicestudio.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [SpeechBrain](speechbrain.zh.md) | ✅ | B（5/6） | 当你需要在一套统一的 PyTorch recipe 代码库上训练和适配语音模型（ASR、说话人识别、语音分离）时用它——但它以研究和训练为先，生产部署和跨版本 API 稳定性得你自己负责。 |
| [Voicebox](voicebox.zh.md) | ✅ | B（6/6） | 当你想要一个自托管的语音 I/O 工作室——克隆音色 TTS、热键 Whisper 听写、MCP/REST 让 agent 发声三合一，且是 MIT——时用它；但它是年轻的单人项目，发布节奏已停滞、自动粘贴目前仅 macOS。 |
| [GPT-SoVITS](gpt-sovits.zh.md) | ✅ | A（5/6） | 想要带 WebUI、且有训练路径可继续提升相似度的本地小样本声音克隆时用它；但它只管 TTS，听写、效果、agent 发声都不在其范围，且版本发布稀疏。 |
| [Coqui TTS（idiap 分支）](coqui-ai-tts.zh.md) | ✅ | C（4/6） | 想要带 XTTS v2 克隆与广泛预训练模型覆盖的 Python TTS 库时用它；但它是 MPL-2.0、不提供应用外壳，且是一家已倒闭公司项目的社区分支。 |
| [AntSpeaker (MECT)](antspeaker.zh.md) | ✅ | C（3/6） | 想用零训练的现成微型 PyTorch 检查点（380 万到 960 万参数）判断两段音频是否同一说话人时用它；但权重是 CC-BY-NC-SA（不可商用）、没有训练代码，且仓库是只活了两周的论文发布。 |
| [VoxCPM](voxcpm.zh.md) | ✅ | B（5/6） | 想用代码和权重都是 Apache-2.0 的模型自托管声音克隆、或用文字描述设计音色（覆盖 30 种语言）时用它；但要备好约 8 GB 显存的 GPU，长文本得自己切句（单次长输出会漂移），并发服务还要另起引擎。 |
| [VoiceStudio](voicestudio.zh.md) | ✅ | C（5/6） | 想要一个本地桌面应用把声音克隆、视频配音、听写和 agent 发声（MCP）一次装齐、还能切换十几个引擎时用它；但默认模型权重禁止商用，应用是 AGPL 且付费 Pro 档正在成形，项目只有半年历史、由一人维护。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

面向**语音**的工具包与应用——识别（ASR）、合成（TTS）、说话人/音频任务。
