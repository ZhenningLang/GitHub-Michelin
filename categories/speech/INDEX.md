# speech

> Category node. Speech processing toolkits (ASR, TTS, speaker tasks).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **SpeechBrain** | Use it when you need to train and adapt speech models (ASR, speaker ID, separation) on one coherent PyTorch recipe codebase — but it's research-and-training-first, so production serving and cross-version API stability are your job. | B (5/6) | [→](speechbrain.md) |
| **Voicebox** | Use it when you want a self-hosted voice I/O studio — cloned-voice TTS, hotkey Whisper dictation, and MCP/REST agent speech in one MIT app — but it's a young single-maintainer project with a stalled release cadence and macOS-only auto-paste today. | B (6/6) | [→](voicebox.md) |
| **GPT-SoVITS** | Use it when you want local few-shot voice cloning with a WebUI plus a training path to push similarity — but it's TTS-only, so dictation, effects, and agent voice are out of scope, and releases are sparse. | A (5/6) | [→](gpt-sovits.md) |
| **Coqui TTS (idiap fork)** | Use it when you want a Python TTS library with XTTS v2 cloning and broad pretrained-model coverage — but it's MPL-2.0, ships no app shell, and is a community fork of a shut-down company's project. | C (4/6) | [→](coqui-ai-tts.md) |
| **AntSpeaker (MECT)** | Use it when you need to check whether two voice clips are the same speaker using tiny ready-made PyTorch checkpoints (3.8M–9.6M params) with zero training — but the weights are CC-BY-NC-SA (no commercial use), there is no training code, and the repo is a two-week-old paper release. | C (3/6) | [→](antspeaker.md) |
| **VoxCPM** | Use it when you need self-hosted voice cloning or text-described voice design in 30 languages under Apache-2.0 code *and* weights — but plan on an ~8 GB-VRAM GPU, splitting long text yourself (long single-pass output drifts), and a separate engine for serving. | B (5/6) | [→](voxcpm.md) |
| **VoiceStudio** | Use it when you want one local desktop app for voice cloning, video dubbing, dictation and agent speech (MCP) with a dozen swappable engines — but the default model's weights are non-commercial, the app is AGPL with a forming paid Pro tier, and it is a six-month-old single-maintainer project. | C (5/6) | [→](voicestudio.md) |
| **IndexTTS** | Use it when you need one cloned voice to carry different emotions — timbre from one clip, emotion from another clip, an 8-value vector or a text cue — in zh/en/ja/es/ar — but the bilibili licence needs a separate grant above 100M MAU or RMB 100M revenue (Chinese text governs), exact-duration dubbing is not released, and there is no training code. | A (3/6) | [→](index-tts.md) |
| **VibeVoice** | Use it when you want one self-hosted model to turn up to an hour of multi-speaker audio into a who/when/what transcript (plus hotwords, 50+ languages, a vLLM server and a streaming variant), or an English TTS that starts speaking in ~0.3 s — but the 7B ASR model wants more than 24 GB of VRAM, there are no tagged releases, and the famous long multi-speaker TTS code was removed in 2025-09. | A (4/6) | [→](vibevoice.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [SpeechBrain](speechbrain.md) | ✅ | B (5/6) | Use it when you need to train and adapt speech models (ASR, speaker ID, separation) on one coherent PyTorch recipe codebase — but it's research-and-training-first, so production serving and cross-version API stability are your job. |
| [Voicebox](voicebox.md) | ✅ | B (6/6) | Use it when you want a self-hosted voice I/O studio — cloned-voice TTS, hotkey Whisper dictation, and MCP/REST agent speech in one MIT app — but it's a young single-maintainer project with a stalled release cadence and macOS-only auto-paste today. |
| [GPT-SoVITS](gpt-sovits.md) | ✅ | A (5/6) | Use it when you want local few-shot voice cloning with a WebUI plus a training path to push similarity — but it's TTS-only, so dictation, effects, and agent voice are out of scope, and releases are sparse. |
| [Coqui TTS (idiap fork)](coqui-ai-tts.md) | ✅ | C (4/6) | Use it when you want a Python TTS library with XTTS v2 cloning and broad pretrained-model coverage — but it's MPL-2.0, ships no app shell, and is a community fork of a shut-down company's project. |
| [AntSpeaker (MECT)](antspeaker.md) | ✅ | C (3/6) | Use it when you need to check whether two voice clips are the same speaker using tiny ready-made PyTorch checkpoints (3.8M–9.6M params) with zero training — but the weights are CC-BY-NC-SA (no commercial use), there is no training code, and the repo is a two-week-old paper release. |
| [VoxCPM](voxcpm.md) | ✅ | B (5/6) | Use it when you need self-hosted voice cloning or text-described voice design in 30 languages under Apache-2.0 code *and* weights — but plan on an ~8 GB-VRAM GPU, splitting long text yourself (long single-pass output drifts), and a separate engine for serving. |
| [VoiceStudio](voicestudio.md) | ✅ | C (5/6) | Use it when you want one local desktop app for voice cloning, video dubbing, dictation and agent speech (MCP) with a dozen swappable engines — but the default model's weights are non-commercial, the app is AGPL with a forming paid Pro tier, and it is a six-month-old single-maintainer project. |
| [IndexTTS](index-tts.md) | ✅ | A (3/6) | Use it when you need one cloned voice to carry different emotions — timbre from one clip, emotion from another clip, an 8-value vector or a text cue — in zh/en/ja/es/ar — but the bilibili licence needs a separate grant above 100M MAU or RMB 100M revenue (Chinese text governs), exact-duration dubbing is not released, and there is no training code. |
| [VibeVoice](vibevoice.md) | ✅ | A (4/6) | Use it when you want one self-hosted model to turn up to an hour of multi-speaker audio into a who/when/what transcript (plus hotwords, 50+ languages, a vLLM server and a streaming variant), or an English TTS that starts speaking in ~0.3 s — but the 7B ASR model wants more than 24 GB of VRAM, there are no tagged releases, and the famous long multi-speaker TTS code was removed in 2025-09. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

Toolkits and applications for **speech** — recognition (ASR), synthesis (TTS), speaker/audio tasks.
