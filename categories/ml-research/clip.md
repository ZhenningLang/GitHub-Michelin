---
name: CLIP
slug: clip
repo: https://github.com/openai/CLIP
category: ml-research
tags: [zero-shot, image-classification, multimodal, embeddings, retrieval, contrastive, vision-language]
language: Python
license: MIT
maturity: stable reference release, low ongoing maintenance, ~33.9k stars (last pushed 2026-03, as of 2026-06)
last_verified: 2026-06-28
type: model
upstream:
  pushed_at: 2026-03-25T18:46:40Z
  default_branch: main
  default_branch_sha: d05afc436d78f1c48dc0dbf8e5980a9d471f35f6
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:42:23Z
  overall: C
  overall_score: 2.2
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 181
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: clip-openai
        dependent_repos_count: 1
        downloads_last_month: 2941
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 2106
        last_commit_age_days: 181
        cohort: model
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.5
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
---

# CLIP

OpenAI's original reference implementation of CLIP (Contrastive Language-Image Pre-training) — a model that maps images and text into one shared embedding space, so you can classify or retrieve images by writing the labels as plain text, with no task-specific training.

![clip — health radar](../../assets/health/clip.svg)

## When to use

You're an ML engineer or researcher who needs to label or search images without collecting a labeled dataset and training a classifier. Maybe you have a pile of product photos and a list of category names, or you want to find "a photo of a dog catching a frisbee" inside a large image collection. You load a pretrained CLIP checkpoint, run `clip.encode_image` over your images and `clip.encode_text` over your candidate prompts, normalize both, and take cosine similarity — the highest-scoring text label is your zero-shot prediction, and the same embeddings double as a retrieval index. Because image and text live in the same vector space, classification, retrieval, and rough semantic similarity all fall out of one model with a handful of lines of PyTorch.

You also reach for this specific repo when you want the canonical, minimal reference: the original ViT-B/32, ViT-L/14, and ResNet (RN50, etc.) weights and the exact preprocessing OpenAI shipped, to reproduce paper numbers or to read how the model and tokenizer are actually wired. It's the smallest faithful starting point for understanding CLIP before you move to a heavier framework.

## When NOT to use

- **You want an actively-developed CLIP for production.** This original repo is effectively a frozen reference — it ships a fixed set of OpenAI checkpoints and sees little ongoing maintenance. [推断] For more checkpoints, training code, and patterns map (LAION-trained models) use OpenCLIP; for a maintained, well-integrated API use Hugging Face `transformers`' CLIP.
- **You need newer / stronger backbones.** CLIP here is older ViT and ResNet architectures; SigLIP (sigmoid loss) and EVA-CLIP generally outperform it on modern zero-shot benchmarks, and OpenCLIP exposes a far wider model zoo.
- **You expect a generative model.** CLIP is an *encoder* — it scores image-text alignment, it does not caption images or answer questions. For image-to-text generation you want BLIP / BLIP-2 or a VLM, not CLIP.
- **You need broad or fair domain coverage.** It carries the biases and domain gaps of its (largely web-scraped, English-centric) training data; performance drops on fine-grained, non-English, OCR, counting, and specialized-domain tasks, and zero-shot scores can be brittle to prompt wording.
- **You need a maintained dependency to pin.** Install is `pip install git+...` off the repo (not a versioned PyPI package), so you're pinning a git ref, not a release. [推断]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| OpenCLIP | 未收录 | Choose OpenCLIP when you need open training code plus a large checkpoint zoo. | Open reproduction with training code and a large zoo of checkpoints (many trained on LAION/DataComp); the de-facto choice when you need more or stronger CLIP models or want to train your own — strictly broader than this reference repo. |
| Hugging Face `transformers` CLIP | 未收录 | Choose Hugging Face transformers when you want the OpenAI CLIP weights behind a maintained batteries-included API. | The same OpenAI weights wrapped in a maintained, batteries-included API (processors, `from_pretrained`, pipelines); easier to integrate and keep current, at the cost of the heavier `transformers` dependency. |
| SigLIP | 未收录 | Choose SigLIP when you need a newer image-text model trained with a sigmoid loss. | Newer image-text model trained with a sigmoid loss; typically stronger zero-shot accuracy and better at scale, but a different model family — usually consumed via OpenCLIP or `transformers`, not this repo. |
| EVA-CLIP | 未收录 | Choose EVA-CLIP when you need scaled CLIP with an improved training recipe and larger backbones. | Scaled CLIP with improved training recipe and larger backbones; higher accuracy ceiling, heavier weights and compute. |
| BLIP / BLIP-2 | 未收录 | Choose BLIP/BLIP-2 when you need vision-language models that generate text. | Vision-language models that *generate* text (captioning, VQA); solve a different problem than CLIP's contrastive embedding/retrieval — not a drop-in substitute. |

## Tech stack

- **Language:** Python, with the usage/examples delivered largely as Jupyter notebooks (the repo is reported as ~99% notebook, ~1% Python by GitHub's language stats).
- **Framework:** PyTorch — the model (`clip.load`), image encoder (ViT or modified ResNet), text encoder (Transformer), and a BPE tokenizer.
- **Model variants:** the OpenAI checkpoints, including ResNet backbones (RN50 and larger) and Vision Transformers (ViT-B/32, ViT-B/16, ViT-L/14), each paired with its own preprocessing transform.
- **Interface:** a small API — `clip.available_models()`, `clip.load(name)`, `model.encode_image`, `model.encode_text` — plus the preprocessing `Compose` returned alongside the model.

## Dependencies

- **Runtime:** Python and PyTorch 1.7.1+ with torchvision, plus small helpers `ftfy`, `regex`, and `tqdm` (per the README).
- **Pretrained weights:** the checkpoints are downloaded on first `clip.load(...)` (network access required) and cached locally; the weights are the substantive dependency, not just the code.
- **Hardware:** runs on CPU, but a CUDA GPU is strongly recommended for anything beyond a few images; larger ViT-L/14 needs correspondingly more VRAM. [推断]
- **Install:** `pip install git+https://github.com/openai/CLIP.git` — there is no separately versioned PyPI release of this repo.

## Ops difficulty

**Low.** There is no service to deploy and nothing to train — install the package, call `clip.load`, and run inference. The realistic operational work is around it, not in it: pulling and caching the weights (and handling that first-load download in air-gapped or CI environments), getting CUDA/PyTorch versions to line up, batching encodes for throughput, and engineering prompts/templates ("a photo of a {label}") since zero-shot accuracy is sensitive to wording. For serving at scale you'd typically precompute and store image embeddings in a vector index rather than re-encode per query, but that index is yours to run, not part of CLIP.

## Health & viability

- **Responsiveness**: Cannot be scored — type_na.
- **Maintenance (as of 2026-06):** last pushed ~2026-03 but effectively a **frozen reference** — a fixed checkpoint set and infrequent commits, not an evolving codebase. [推断] Treat it as coasting-by-design: it still installs and runs, but don't expect new backbones, fixes, or a versioned PyPI release here.
- **Governance / backing:** organization-owned by OpenAI — the original paper repo, not a community project. That gives provenance (these are *the* reference weights/preprocessing) but no commitment to ongoing maintenance; the live ecosystem moved to OpenCLIP and Hugging Face `transformers`.
- **Age & Lindy verdict (created 2020-12, ~6 yr):** old *and still widely used*, which is a strong Lindy signal for the **CLIP idea and these weights** as a stable baseline. The verdict is split: the *concept/checkpoints* are Lindy-proven and safe to build on; *this specific repo as a maintained dependency* is not — its longevity is "famous and frozen," not "actively maintained."
- **Adoption:** CLIP embeddings are foundational across retrieval, zero-shot classification, and as the text/image encoder in many downstream systems; the pattern is deeply entrenched even though most production users consume it via OpenCLIP/`transformers` rather than this repo.
- **Risk flags:** install is `pip install git+...` (a git ref, not a release), so reproducibility hinges on pinning a commit; MIT-licensed, no relicense risk. [推断]

## Caveats (unverified)

- [未验证] ~33.9k GitHub stars and last push around 2026-03 as of 2026-06; star counts are unreliable and date-sensitive — treat as indicative only.
- [推断] "Stable reference release / low ongoing maintenance" is inferred from this being the original paper repo with a fixed checkpoint set and infrequent pushes, not a declared project status — verify recent commit/issue activity before relying on it.
- [未验证] Exact dependency floors (PyTorch 1.7.1, torchvision, ftfy, regex, tqdm) are read off the README; the actual minimum versions can drift — check `setup.py`/`requirements` in the current tree.
- [未验证] The set and names of available checkpoints (RN50, ViT-B/32, ViT-B/16, ViT-L/14, and larger) are paraphrased from the README/`clip.available_models()`; confirm against the current repo for the exact list.
- [推断] GPU recommendation and VRAM sensitivity to backbone size are general inferences about transformer inference, not measured figures from this repo.
- [未验证] Bias and domain-gap characterizations come from the CLIP paper / model card framing, not an independent evaluation here.
