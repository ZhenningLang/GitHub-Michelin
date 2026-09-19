# speech

> 分类节点。语音处理工具包（ASR、TTS、说话人任务）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **SpeechBrain** | 当你需要在一套统一的 PyTorch recipe 代码库上训练和适配语音模型（ASR、说话人识别、语音分离）时用它——但它以研究和训练为先，生产部署和跨版本 API 稳定性得你自己负责。 | A（4/6） | [→](speechbrain.zh.md) |
| **Voicebox** | 当你想要一个自托管的语音 I/O 工作室——克隆音色 TTS、热键 Whisper 听写、MCP/REST 让 agent 发声三合一，且是 MIT——时用它；但它是年轻的单人项目，发布节奏已停滞、自动粘贴目前仅 macOS。 | B（5/6） | [→](voicebox.zh.md) |
| **GPT-SoVITS** | 想要带 WebUI、且有训练路径可继续提升相似度的本地小样本声音克隆时用它；但它只管 TTS，听写、效果、agent 发声都不在其范围，且版本发布稀疏。 | A（5/6） | [→](gpt-sovits.zh.md) |
| **Coqui TTS（idiap 分支）** | 想要带 XTTS v2 克隆与广泛预训练模型覆盖的 Python TTS 库时用它；但它是 MPL-2.0、不提供应用外壳，且是一家已倒闭公司项目的社区分支。 | C（3/6） | [→](coqui-ai-tts.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [SpeechBrain](speechbrain.zh.md) | ✅ | A（4/6） | 当你需要在一套统一的 PyTorch recipe 代码库上训练和适配语音模型（ASR、说话人识别、语音分离）时用它——但它以研究和训练为先，生产部署和跨版本 API 稳定性得你自己负责。 |
| [Voicebox](voicebox.zh.md) | ✅ | B（5/6） | 当你想要一个自托管的语音 I/O 工作室——克隆音色 TTS、热键 Whisper 听写、MCP/REST 让 agent 发声三合一，且是 MIT——时用它；但它是年轻的单人项目，发布节奏已停滞、自动粘贴目前仅 macOS。 |
| [GPT-SoVITS](gpt-sovits.zh.md) | ✅ | A（5/6） | 想要带 WebUI、且有训练路径可继续提升相似度的本地小样本声音克隆时用它；但它只管 TTS，听写、效果、agent 发声都不在其范围，且版本发布稀疏。 |
| [Coqui TTS（idiap 分支）](coqui-ai-tts.zh.md) | ✅ | C（3/6） | 想要带 XTTS v2 克隆与广泛预训练模型覆盖的 Python TTS 库时用它；但它是 MPL-2.0、不提供应用外壳，且是一家已倒闭公司项目的社区分支。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

面向**语音**的工具包与应用——识别（ASR）、合成（TTS）、说话人/音频任务。
