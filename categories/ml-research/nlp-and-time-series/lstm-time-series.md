---
name: LSTM Neural Network for Time Series Prediction
slug: lstm-time-series
repo: https://github.com/jaungiers/LSTM-Neural-Network-for-Time-Series-Prediction
category: nlp-and-time-series
tags: [lstm, time-series, keras, tensorflow, educational, forecasting, deep-learning]
language: Python
license: AGPL-3.0
maturity: educational article companion, last commit 2019-04, quiet since (as of 2026-10-08), ~5.2k stars
last_verified: 2026-10-08
type: library
upstream:
  pushed_at: 2023-03-24T21:54:57Z
  default_branch: master
  default_branch_sha: da44411c91135b64c02eb60da3c7f574c7c4c253
  archived: false
health:
  schema: 1
  computed_at: 2026-10-08T08:23:02Z
  overall: E
  overall_score: 0.25
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 2718
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: E
      raw:
        repo_age_days: 3581
        last_commit_age_days: 2718
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: D
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# LSTM Neural Network for Time Series Prediction

A compact, article-companion codebase showing how to build a Keras LSTM to predict time-series sequences — demoed on a sine wave and S&P 500 data — built to teach the technique, not to ship as a forecasting library.

![lstm-time-series — health radar](../../../assets/health/lstm-time-series.svg)

## When to use

You're a student or engineer new to sequence models, and you've read about LSTMs for forecasting but want to *see* an end-to-end example: load a CSV window, build a stacked LSTM in Keras, train it, and plot point-by-point vs. full-sequence predictions. You clone this repo, follow its companion article on altumintelligence.com, run `run.py` against the bundled sine-wave and S&P 500 data, and watch the model predict next steps and multi-step sequences. The `config.json` exposes window length, layers, and epochs so you can tweak and re-run to build intuition about how LSTMs handle sequences.

You reach for it as a **learning artifact** — a clean, readable reference implementation tied to a written explanation — when your goal is to understand the mechanics of windowing, normalization, and sequence prediction with a recurrent net, not to deploy a production forecaster.

## How it works

There is no package to import: the repo is one script (`run.py`), a small `core/` module and a `config.json`, and everything you change lives in that config. You point it at a CSV in `data/` (the bundled sine wave or S&P 500 prices), choose the columns, the window length (how many past steps the model sees at once — 50 by default), the layer stack and the epochs. Running `run.py` then does the whole lesson for you: it slices the series into overlapping windows, rescales each window relative to its own first value so the network learns percentage moves rather than raw price levels, builds the stacked LSTM (a recurrent layer that carries a running memory from one time step to the next) exactly as the config lists it, trains it, and plots multi-step predictions on the held-out 15% against the real series. Point-by-point and full-sequence prediction are one commented-out line away in `run.py`. What the plot *means* — and why a good-looking S&P chart is not a trading signal — is explained in the companion article, not by the code.

![lstm-time-series — backbone user story](../../../assets/flow/lstm-time-series.svg)

<!-- flow-steps:begin (generated from flows/lstm-time-series.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Set up an old Python 3.5 + TensorFlow 1 environment with the pinned requirements — `tensorflow-gpu==1.10.0 · keras==2.2.2`
2. **You**: Pick the CSV, columns, window length, layers and epochs — `config.json`
3. **You**: Run the entry script — `run.py`
4. **LSTM Neural Network for Time Series Prediction**: Cuts the series into fixed-length windows and rescales each one relative to its first value
5. **LSTM Neural Network for Time Series Prediction**: Builds the stacked LSTM described in the config, trains it and saves the model
6. **LSTM Neural Network for Time Series Prediction**: Predicts multi-step sequences on the held-out data and plots them against the real series

**Value**: You watch windowing, normalisation and LSTM sequence prediction work end to end, in code short enough to read alongside the article

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You need a production or even current forecasting library.** It's pinned to TensorFlow 1.10 / Keras 2.2 / Python 3.5-era stacks (2018 vintage); those won't install cleanly on a modern environment without significant effort. It is a frozen teaching example, not a maintained tool. [推断]
- **You want state-of-the-art time-series accuracy.** Modern forecasting uses libraries like Darts, GluonTS, Prophet, or transformer-based models; a hand-rolled stacked LSTM from 2018 is a baseline, not a competitive method.
- **Stock-price prediction in particular.** The S&P 500 demo is illustrative; financial price series are near-random-walk and this is not a trading system — treating the demo as alpha is a classic trap.
- **AGPL-3.0 is a problem for you.** This is a strong copyleft / network-copyleft license; embedding it in a closed-source or SaaS product carries obligations most teams won't want for a 200-line example. Re-implement from the article instead.
- **You expected ongoing support.** Single author, no commits since 2019-04, ~40 open issues unanswered — file an issue and nobody is coming.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| Darts | 未收录 | Choose Darts when you need a modern maintained Python forecasting library with many model families. | Modern, maintained Python forecasting library (many models incl. deep learning) with a unified API; production-oriented, far heavier than a teaching script. |
| GluonTS | 未收录 | Choose GluonTS when you need a probabilistic time-series toolkit from AWS. | Probabilistic time-series toolkit (AWS); strong for real forecasting at scale, steeper learning curve, not an intro example. |
| Prophet | 未收录 | Choose Prophet when you need simple decomposition-based forecasting for business seasonality. | Decomposition-based forecasting, trivial to use for business seasonality; not a deep-learning/LSTM demonstration. |
| Keras official RNN tutorials | 未收录 | Choose Keras official tutorials when you need current maintained TF2 examples of the same techniques. | Up-to-date, maintained, TF2 examples of the same techniques; less narrative than the companion article but won't bit-rot the same way. |
| [PyTorch-GAN](../vision-and-multimodal/pytorch-gan.md) | ✅ | Choose PyTorch-GAN when you need the same teaching-repo genre in generative images. | A different domain (generative images) but the same *genre* — a single-author reference-implementation collection meant to teach, not to be a maintained dependency. |

## Tech stack

- **Language:** Python (3.5.x era).
- **Framework:** Keras 2.2.2 on TensorFlow 1.10.0 (GPU build pinned in `requirements.txt`).
- **Data/plotting:** NumPy 1.15, pandas 0.23, Matplotlib 2.2.
- **Shape:** `run.py` entry point, a `core/` module (data loader + model), `config.json` for hyperparameters, bundled CSV data.

## Dependencies

- **Runtime:** a TensorFlow 1.x environment — `tensorflow-gpu==1.10.0`, `keras==2.2.2`, plus pinned NumPy/pandas/Matplotlib. Reproducing this today effectively means an old Python 3.5/3.6 + TF1 environment (Docker/conda), since TF1 is EOL.
- **Hardware:** the pinned requirement is the GPU TF build, but the model is small enough to run on CPU with the TF1 CPU package.
- **Data:** sample sine-wave and S&P 500 CSVs are bundled; bring your own CSV in the same windowed format to use it on other series.

## Ops difficulty

**Medium — entirely because of the dated stack, not the code.** The code itself is simple to run, but standing up a working TensorFlow-1.10 / Keras-2.2 / Python-3.5 environment in 2026 is the real friction: those versions predate current CUDA, won't `pip install` on a modern interpreter, and are best reproduced in an isolated old-Python container. Once the environment exists, training is a single `run.py` on a tiny model — seconds-to-minutes, no infrastructure. There is nothing to "operate"; the difficulty is purely the legacy-dependency archaeology.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-10).** Last commit on the default branch 2019-04 (the 2023-03 `pushed_at` touched no default-branch commit); no releases/tags. ~40 open issues with no maintainer activity ⇒ effectively **frozen/abandoned** as a maintained project — which is fine for a teaching artifact but disqualifying as a dependency. [推断]
- **Governance / bus factor.** Single author (jaungiers); bus factor = 1. The high star count (~5.2k) on a one-person repo idle for ~7 years is **popularity, not health** — a classic "famous tutorial" signal, flag accordingly. [推断]
- **Age & Lindy verdict.** Created 2016-12 (~10 years) but **not still active** (no commits since 2019) ⇒ age alone is *not* Lindy here; old-and-stale fails the still-active test. Its longevity is as a referenced example, not as living software. [推断]
- **Adoption.** ~5.2k stars / ~1.9k forks — widely cloned as a learning reference and forked for coursework; that's its real role. [未验证]
- **Risk flags.** **AGPL-3.0** is the headline risk for reuse (network-copyleft obligations); plus a fully EOL TF1 stack. Both push you toward re-implementing the idea rather than vendoring the repo. [推断]

## Caveats (unverified)

- [未验证] ~5.2k stars / ~2.0k forks / ~42 open issues (~50 issues+PRs) as of 2026-10-08; counts are date-sensitive and indicative only.
- [未验证] Companion article and video links (altumintelligence.com / YouTube) are referenced in the README; their continued availability is not verified here.
- [推断] "Won't install cleanly on modern environments" is inferred from the pinned TF 1.10 / Python 3.5-era requirements (TF1 is EOL), not from a tested install attempt.
- [推断] "Abandoned" is inferred from the 2019-04 last-commit date + no releases + unanswered issues, not from an explicit deprecation notice.
