---
name: PyTorch-GAN
slug: pytorch-gan
repo: https://github.com/eriklindernoren/PyTorch-GAN
category: ml-research
tags: [gan, generative, deep-learning, reference-implementation, educational, pytorch, computer-vision]
language: Python
license: MIT
maturity: educational reference collection, idle since ~2024-06, ~17.5k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2024-06-18T07:08:31Z
  default_branch: master
  default_branch_sha: 36d3c77e5ff20ebe0aeefd322326a134a279b93e
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:42:53Z
  overall: D
  overall_score: 1.0
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
        last_commit_age_days: 2085
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
        repo_age_days: 3076
        last_commit_age_days: 2085
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# PyTorch-GAN

A single-author collection of clean, from-scratch PyTorch implementations of many GAN papers (DCGAN, CycleGAN, WGAN, pix2pix, and dozens more) — built to be *read and learned from*, one self-contained script per architecture, not imported as a dependency.

![pytorch-gan — health radar](../../assets/health/pytorch-gan.svg)

## When to use

You're a student, researcher, or engineer who has read the GAN papers but wants to see the architectures wired up in real, runnable code — the generator/discriminator definitions, the loss functions, the training loop — without the indirection of a heavyweight framework. You clone this repo, open `implementations/dcgan/dcgan.py` (or `cyclegan/`, `wgan_gp/`, `pix2pix/`, …), and get a single compact script that you can read top-to-bottom in one sitting: each model is self-contained, uses plain PyTorch, and maps closely onto the equations in the corresponding paper. You run it on a toy dataset (MNIST/CIFAR) to watch the training dynamics, tweak a layer or a loss term to build intuition, and copy the pattern into your own code.

You reach for this specific repo when you want *breadth of reference under one consistent style*: the same author implemented many GAN variants with a shared structure, so once you've read one you can read the next quickly and compare how, say, WGAN's loss differs from vanilla GAN's. It's a learning map of the classic GAN era, not a toolkit you build a product on.

## When NOT to use

- **You want a library to import and build on.** This is *copy-and-learn* code, not a packaged dependency — there's no PyPI release, no stable API, no abstraction layer. You read the scripts and adapt them; you don't `import pytorch_gan`.
- **You need production-grade or SOTA generation.** These are faithful but minimal educational implementations (small datasets, simple training loops, no distributed training, no mixed precision, no serving). For real generative quality the field has largely moved to **diffusion models** — GANs are no longer the default for image synthesis.
- **You need current architectures.** The collection covers the classic 2014–2018 GAN papers; it does **not** include modern GANs (StyleGAN2/3, etc.) or anything post-diffusion. No new architectures are being added.
- **You want a maintained codebase.** It's effectively done — last pushed ~2024-06 and idle since, with old PyTorch idioms that may need fixups on current versions. [推断] Don't expect bug fixes, dependency bumps, or support.
- **You want the official, paper-accurate weights/numbers.** These are clean re-implementations for learning, not the authors' original repos — don't cite them to reproduce a paper's exact reported metrics; go to each paper's official implementation for that.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| `diffusers` (Hugging Face) | 未收录 | Choose diffusers when you need a maintained library for modern diffusion generation with pretrained pipelines. | Maintained library for **diffusion** models (the modern default for generation) with pretrained pipelines and a real API; solves today's generation problem, but a different model family and not a from-scratch reading aid. |
| Official paper repos (StyleGAN, CycleGAN, …) | 未收录 | Choose official paper repos when you need the authors' own implementations. | The authors' own implementations — paper-accurate weights and numbers, but each is its own codebase with its own style/quirks; not a single consistently-written collection for browsing many GANs side by side. |
| lucidrains' implementations | 未收录 | Choose lucidrains' implementations when you need another clean PyTorch reimplementation body with broader current coverage. | Another prolific single-author body of clean PyTorch reimplementations spanning many architectures (incl. newer ones); often more actively updated, similar "read the code" value, broader/more current scope. |
| torchgan | 未收录 | Choose torchgan when you need an importable GAN library/framework with trainers, losses, and metrics. | An actual GAN *library/framework* (modular trainers, losses, metrics) you import and configure; better if you want reusable building blocks, less suited to reading one paper's architecture end-to-end. |

## Tech stack

- **Language:** Python, plain **PyTorch** — no higher-level training framework (no Lightning/Accelerate), so the training loop is explicit and readable.
- **Structure:** one directory per architecture under `implementations/`, each typically a single self-contained script defining the generator, discriminator, losses, and training loop.
- **Coverage:** classic GAN family — DCGAN, CGAN, WGAN / WGAN-GP, CycleGAN, pix2pix, ACGAN, InfoGAN, BEGAN, ESRGAN, and many more (the README lists each with a link to its paper).
- **Data:** examples run against small standard datasets (e.g. MNIST/CIFAR), downloaded by helper scripts rather than bundled.

## Dependencies

- **Runtime:** Python 3, PyTorch + torchvision, plus the usual numeric stack (numpy) and image helpers; exact pins live in the repo's `requirements.txt` and may be dated. [未验证]
- **Hardware:** a CUDA GPU is recommended for training anything beyond the smallest toy runs; many examples will *run* on CPU but slowly.
- **No service/infra:** nothing to deploy — it's scripts you run locally. The main practical dependency risk is version drift: old PyTorch idioms may need small fixes on a current PyTorch/CUDA stack. [推断]

## Ops difficulty

**Low — there's nothing to operate.** It's a folder of training scripts you run by hand (`python implementations/<name>/<name>.py`), not a service. The only real friction is environment setup: getting a PyTorch/CUDA combo that works on your machine and patching any API calls that have since been deprecated, since the code hasn't been updated to track recent PyTorch releases. There's no deployment, no datastore, no scaling story — by design, because the artifact is *understanding*, not a running system.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (DATED, as of 2026-06):** last pushed **~2024-06**, so roughly **2 years idle** — read as **coasting / effectively done**, not actively maintained. [推断] It still installs and runs (modulo version fixups), but expect no fixes, dependency bumps, or new architectures.
- **Governance / bus factor:** a **single-author** repo (Erik Linder-Norén, a User account, not an org). Classic high-bus-factor / single-maintainer situation — there's no team or foundation behind it; its continued existence is "famous and frozen," not staffed.
- **Age & Lindy verdict (created 2018-04, ~8 yr):** old, but its value is a **frozen reference**, not ongoing maintenance — so plain age × *still-active* doesn't apply the usual way. The Lindy signal here is "this reading material has been useful for years and isn't going anywhere," not "this is a living, evolving project." Judge it as a stable teaching artifact, not a dependency to bet a system on.
- **Relevance decay (flag):** the field moved on. GANs have been **largely superseded by diffusion models** for generation, so the *educational* value (understanding the GAN era) persists while the *practical* value for new generation work has declined. Weigh this if your goal is building something today vs. learning the lineage.
- **Risk flags:** MIT-licensed (no relicense risk); the real risks are idleness and old APIs, not governance traps. [推断]

## Caveats (unverified)

- [未验证] ~17.5k GitHub stars and last push around 2024-06 as of 2026-06; star counts are unreliable and date-sensitive — treat as indicative only.
- [推断] "Idle ~2 years / coasting / effectively done" and "single-author User repo" are inferred from the push date and owner type stated for this task — confirm recent commit/issue activity and ownership against the live repo before relying on them.
- [未验证] The exact list of implemented architectures (DCGAN, CycleGAN, WGAN-GP, pix2pix, etc.) is paraphrased from the README; confirm the current set against the repo's `implementations/` directory.
- [未验证] Dependency pins (PyTorch/torchvision/numpy versions in `requirements.txt`) are not quoted here and may be stale; check the actual file before setting up an environment.
- [推断] "One self-contained script per architecture" and the dataset-download behaviour are inferred from the project's described structure, not verified file-by-file here.
- [推断] The "GANs superseded by diffusion" framing is a general characterization of the generative-modeling field, not a claim specific to this repo's contents.
