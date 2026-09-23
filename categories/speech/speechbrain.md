---
name: SpeechBrain
slug: speechbrain
repo: https://github.com/speechbrain/speechbrain
category: speech
tags: [speech, asr, pytorch, toolkit, speaker-recognition, text-to-speech, research]
language: Python
license: Apache-2.0
maturity: v1.1.0 (2026-03), active, ~11.7k stars (as of 2026-06)
last_verified: 2026-06-28
type: framework
upstream:
  pushed_at: 2026-06-15T11:24:25Z
  default_branch: develop
  default_branch_sha: e5cb1f65b940634215650aa1171e0440d0808123
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:51:39Z
  overall: B
  overall_score: 3.2
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 26
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: D
      raw:
        median_ttfr_hours: 988.1
        qualifying_issues: 6
        band: default
        window_offset_days: 6
        source: pr
        inferred: false
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: A
      raw:
        repo_age_days: 2338
        last_commit_age_days: 26
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 30
        top1_share: 0.232
        top3_share: 0.549
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    adoption: { reason: ambiguous }
---

# SpeechBrain

An all-in-one, PyTorch-based speech toolkit covering speech recognition, speaker recognition, enhancement, separation, language identification, text-to-speech and more — with hundreds of ready-to-run training "recipes" on standard datasets.

![speechbrain — health radar](../../assets/health/speechbrain.svg)

## When to use

You're a speech ML researcher or an applied engineer who needs to train (not just call) a speech model — say a domain-specific ASR system, a speaker-verification model, or a source-separation pipeline — and you want to stand on a consistent PyTorch codebase instead of gluing together five incompatible research repos. You clone SpeechBrain, pick a recipe for your task and dataset (LibriSpeech ASR, VoxCeleb speaker ID, WSJ0-mix separation, …), and you get a runnable training script, a YAML-driven config (HyperPyYAML) describing the whole experiment, data pipelines, and a model you can fine-tune. Because everything shares one framework, swapping the encoder, the loss, or the dataset is editing config and a class, not porting code between projects.

You also reach for it when you want pretrained models you can both *use* and *retrain*: SpeechBrain publishes many checkpoints (often via Hugging Face) with simple inference interfaces, but unlike a black-box API you have the full recipe to reproduce or adapt them. It's most valuable when your work spans several speech tasks at once and you want them to live in one coherent, well-documented research toolkit rather than a pile of one-off scripts.

## When NOT to use

- **You just want to transcribe audio with a SOTA model, no training.** If you only need inference, `faster-whisper` / Whisper or a hosted STT API is a shorter path than adopting a full training framework.
- **You need a hardened, low-latency production serving stack out of the box.** SpeechBrain is research-and-training-first; productionizing (serving, streaming, latency tuning, deployment) is your work, and some recipes target benchmarks rather than prod constraints. [推断]
- **You're locked to a non-PyTorch stack.** It is PyTorch-native; if your environment is JAX/TF-only or edge-runtime constrained, the fit is poor.
- **You want a tiny dependency.** It pulls in PyTorch and a research-grade dependency set; it's a toolkit, not a lightweight library to vendor into a small app.
- **You need guaranteed long-term API stability across versions.** It's an actively evolving research toolkit; recipes and APIs change across major versions (the v1.x line was a notable shift), so pin versions and budget for migrations. [推断]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| NeMo (NVIDIA) | 未收录 | Choose NeMo when you need a larger, GPU/scale-oriented conversational-AI toolkit with NVIDIA tooling. | Strong ASR/TTS and NVIDIA integration, but heavier and more vendor-centric than SpeechBrain's lighter research framing. |
| ESPnet | 未收录 | Choose ESPnet when you need end-to-end speech processing with deep ASR/TTS recipe coverage and research lineage. | Powerful, but historically steeper and more Kaldi-flavored than SpeechBrain. |
| Hugging Face Transformers (audio) | 未收录 | Choose Transformers audio models when using or fine-tuning pretrained Whisper/Wav2Vec2-style models is enough. | Excellent model access, but not a full recipe/training framework spanning separation, enhancement, and diarization. |
| Kaldi | 未收录 | Choose Kaldi when you need the classic, highly optimized ASR toolkit and accept C++/shell-heavy workflows. | Maximizes control, not ergonomics; it is far steeper and not PyTorch-native. |
| faster-whisper / [Whisper](../media-processing/video-audio/whisper.md) | 部分已收录 | Choose inference-focused Whisper stacks when transcription is the job, not multi-task speech training. | Excellent if you only transcribe, but not a multi-task training toolkit. faster-whisper is not indexed separately. |

## Tech stack

- **Language / framework:** Python on **PyTorch**; models, training loops, and data pipelines are PyTorch-native.
- **Config:** **HyperPyYAML** — a YAML superset that describes the full experiment (model, optimizer, data, hyperparameters) so experiments are declarative and reproducible.
- **Scope:** recipes and modules for ASR, speaker recognition/verification, speech enhancement, source separation, language ID, TTS, spoken-language understanding, and more.
- **Models:** many pretrained checkpoints, commonly distributed via the Hugging Face Hub with lightweight inference wrappers.

## Dependencies

- **Runtime:** Python + PyTorch, plus a scientific/audio dependency stack (numpy, torchaudio, etc.). A GPU is effectively required for serious training. [推断]
- **Data:** recipes assume you can obtain the relevant corpora (LibriSpeech, VoxCeleb, etc.) — datasets are downloaded/prepared by recipe scripts, not bundled.
- **Hugging Face:** pretrained-model inference typically fetches checkpoints from the HF Hub (network + HF availability).
- **Install:** `pip install speechbrain`, or clone the repo to use/modify recipes directly.

## Ops difficulty

**Medium (research) / higher (production).** For its intended use — running and adapting training recipes — the ergonomics are good: install, pick a recipe, edit a YAML, train. The real cost is the ML lifecycle around it: acquiring and preparing large datasets, securing GPU/compute, long training runs, and reproducing benchmark numbers. Taking a trained model to production (serving, streaming, latency, monitoring) is entirely your responsibility and is the harder half. There's no service to operate from SpeechBrain itself — the burden is compute and ML-ops, not running a SpeechBrain daemon.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-06).** Last pushed 2026-06; v1.1.0 released 2026-03 on the `develop` branch with steady activity — **active**, not coasting. Not archived. [推断]
- **Governance / bus factor.** A research-community project driven by a recognizable maintainer group (academic/lab-affiliated core contributors) rather than a single person — broader bus factor than a solo project, but still community/academic-funded rather than a foundation. [未验证]
- **Age × Lindy (2026-06).** Created 2020-04 — ~6 years old and **still actively shipping** ⇒ a **moderate-to-strong Lindy** signal for a research toolkit; it has outlived the typical academic-repo half-life. [推断]
- **Adoption & ecosystem.** Widely cited and used in speech research, many pretrained models on Hugging Face, and substantial docs/recipes indicate healthy adoption in its niche. ~180 open issues is consistent with an active research codebase. [未验证]
- **Risk flags.** Apache-2.0, no relicense history found. Main risks are research-toolkit risks: API/recipe churn across major versions and a production gap you must close yourself. [推断]

## Caveats (unverified)

- [未验证] ~11.7k stars and v1.1.0 (2026-03) as of 2026-06 — star and version numbers are date-sensitive; treat as indicative only.
- [未验证] The exact maintainer/governance structure and funding model were not confirmed beyond the visible contributor set; "research-community-driven" is inferred from the contributor list and the project's academic lineage.
- [推断] GPU requirement, dataset-download behavior, and HF-Hub dependency for pretrained inference are inferred from the toolkit's nature and README, not exhaustively verified per recipe.
- [推断] "Recipes/APIs change across major versions" is an inference from the existence of a v1.x major line; specific breaking-change scope was not enumerated.
- [未验证] Comparisons to NeMo/ESPnet/Kaldi reflect general positioning, not a measured benchmark.
