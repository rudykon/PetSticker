<p align="center">
  <strong>English</strong> · <a href="README_zh.md">中文</a>
</p>

<p align="center">
  <img src="docs/brand-mark.svg" width="430" alt="PetSticker — WeChat Pet Sticker Designer brand mark">
</p>

<h1 align="center">WeChat Pet Sticker Designer</h1>

<p align="center">
  <strong>Identity-anchored design, three-layer QA, and submission-ready delivery</strong><br>
  A reusable ChatGPT/Codex skill for turning pet references into consistent, reviewable WeChat sticker albums.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/ChatGPT%20%2F%20Codex-Skill-111827?style=flat-square" alt="ChatGPT and Codex skill">
  <img src="https://img.shields.io/badge/Python-%E2%89%A53.9-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.9 or newer">
  <img src="https://img.shields.io/badge/Default%20album-24%20stickers-2F8F83?style=flat-square" alt="24 stickers by default">
  <img src="https://img.shields.io/badge/QA-3%20gates-E76F51?style=flat-square" alt="Three quality gates">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-F4A261?style=flat-square" alt="MIT License"></a>
</p>

<p align="center">
  <a href="#overview">Overview</a> ·
  <a href="#input-output-example">Input → Output</a> ·
  <a href="#workflow">Workflow</a> ·
  <a href="#deliverables">Deliverables</a> ·
  <a href="#quick-start">Quick Start</a> ·
  <a href="#validation">Validation</a> ·
  <a href="#repository-map">Repository</a> ·
  <a href="#license">License</a>
</p>

<p align="center">
  <img src="docs/readme-hero.svg" width="100%" alt="A pet portrait with an expressive, quality-checked sticker collection">
</p>

> [!IMPORTANT]
> **This is a quality-controlled workflow, not a one-click image dump.** Automated checks verify deterministic file requirements; they cannot prove that a sticker has correct anatomy, identity, proportions, semantics, or Chinese text. Always perform the documented per-image visual review and follow the latest official WeChat requirements.

<a id="overview"></a>
## Overview

WeChat Pet Sticker Designer closes the full **design → generation → review → normalization → packaging** loop. It keeps a real pet or approved character reference as the identity anchor, breaks an album into independent assets, generates in small batches, and blocks defective files before release.

| Goal | Method | Result |
| --- | --- | --- |
| Preserve the pet's identity | Lock facial structure, markings, body proportions, tail, collar, and name tag in a character bible | A recognizable character across every scene |
| Prevent structural defects | Review limb/tail counts, attachment points, props, crops, and pose semantics at source resolution | No extra legs, duplicate tails, fused parts, or impossible actions |
| Keep small stickers readable | Use short Chinese captions or universal symbols only when they improve meaning; typeset deterministically when generation is unreliable | Accurate, legible captions without random glyphs |
| Guarantee real transparency | Inspect the alpha channel on colored backgrounds instead of accepting checkerboards or white rectangles | Clean PNG assets without fake transparency or halos |
| Deliver platform-ready files | Validate count, dimensions, format, opacity, naming, manifests, and QA documents | An auditable release directory ready for final submission review |

The repository contains general instructions, templates, validation tools, and this explicitly approved, cropped, metadata-stripped input/output case study. It does **not** contain the original input files, additional pet photos, private identity anchors, high-resolution work files, rejected drafts, or a full generated album.

<a id="input-output-example"></a>
## Input → output example: 布鲁 · Workplace

This release-safe case study shows how one approved pet reference becomes a coherent, platform-ready album. The output preserves Bulu's large upright ears, warm gray-brown coat, light athletic proportions, and expressive face while expanding the character into distinct workplace scenarios.

### Input reference

<p align="center">
  <img src="docs/showcase/workplace/input-reference.jpg" width="280" alt="Cropped input reference photo of Bulu the cat">
</p>

<p align="center"><sub>Cropped to the pet, resized for the README, and stripped of the original file metadata.</sub></p>

<p align="center"><strong>↓ Character bible → Asset plan → Small-batch generation → Three QA gates ↓</strong></p>

### Output sticker selection

| Daily work moments | Support, pressure, and milestones |
| --- | --- |
| ![Clock-in, computer-crash, slacking, and done stickers](docs/showcase/workplace/output-workday.png) | ![Guidance, overload, Happy Friday, and promotion stickers](docs/showcase/workplace/output-milestones.png) |

<p align="center"><sub>Eight representative transparent stickers selected from the complete 24-sticker album.</sub></p>

### Companion detail banner

<p align="center">
  <img src="docs/showcase/workplace/detail-banner.jpg" width="750" alt="Bulu the cat at a bright office desk beside a laptop">
</p>

Only the cropped, metadata-stripped input reference and approved final artwork are shown. The original files, EXIF data, other references, private identity anchors, work files, and rejected drafts remain outside the repository.

<a id="workflow"></a>
## Workflow

```text
[Pet reference]
      |
      v
[Character bible] -> [Asset plan] -> [Small-batch generation]
                                              |
                                              v
                                      [Three QA gates]
                                         |        |
                                       fail      pass
                                         |        |
                                         v        v
                                  [Repair asset] [Validate + release]
                                         |
                                         +------> back to QA
```

The three blocking gates are:

| Gate | What is checked | Blocking failures |
| --- | --- | --- |
| **1. Identity and body** | Face, markings, eyes, ears, chest/abdomen thickness, head-to-body ratio, legs, paws, tail, accessories | Character drift, too fat/thin, changed markings, wrong tag or collar |
| **2. Structure and meaning** | Limb/tail count and attachment, crop boundaries, prop contact, pose, caption, symbol, and distinction across the album | Extra limbs, duplicate tails, fused parts, impossible interaction, wrong text or unclear meaning |
| **3. File requirements** | Count, pixel size, format, alpha/opacity, size warnings, naming, directory layout, manifest and QA files | Missing files, wrong dimensions, fake transparency, invalid JSON, incorrect naming |

Any failure returns only that asset to repair, followed by all three gates again. Passing the script never replaces visual review.

<a id="deliverables"></a>
## Deliverables

A default complete static album contains:

| Asset | Default count | Notes |
| --- | ---: | --- |
| Independent sticker PNGs | 24 | Different expressions, poses, and messaging contexts |
| Character avatar | 1 | Transparent 240 × 240 PNG |
| Detail banner | 1 | Opaque 750 × 400 image; head-and-shoulders composition is preferred |
| Album cover | 1 | Transparent 240 × 240 PNG |
| Chat icon | 1 | Transparent 50 × 50 PNG |
| Tipping prompt | Optional 1 | 750 × 560 image |
| Tipping thanks | Optional 1 | 750 × 750 image |
| Manifest, character bible, QA report | 3 | Audit trail for generation and delivery |

The default release structure is:

```text
project/
├── references_private/        # Original pet photos; excluded from shared releases
├── work/                      # High-resolution sources, drafts and repairs
└── release/
    ├── stickers/              # 01_*.png … 24_*.png
    ├── assets/
    │   ├── character_avatar.png
    │   ├── detail_banner.jpg
    │   ├── album_cover.png
    │   ├── chat_icon.png
    │   ├── tipping_prompt.jpg # optional
    │   └── tipping_thanks.jpg # optional
    ├── manifest.json
    ├── character_bible.md
    └── qa_report.md
```

<a id="quick-start"></a>
## Quick start

### 1. Clone the skill

```bash
git clone https://github.com/rudykon/wechat-pet-sticker-designer.git
cd wechat-pet-sticker-designer
```

Load or copy the whole repository as one skill in a Skills-compatible ChatGPT/Codex environment. Keep `SKILL.md`, `agents/`, `assets/`, `references/`, and `scripts/` together.

### 2. Install the validator dependency

```bash
python3 -m pip install Pillow
```

### 3. Invoke the skill

```text
$wechat-pet-sticker-designer
```

Example request:

```text
Use $wechat-pet-sticker-designer and my uploaded pet references to create a
submission-ready static WeChat sticker album. Preserve the approved body
proportions and name tag, use real transparency, and review every asset for
extra limbs, duplicate tails, incorrect Chinese text, and style drift.
```

The skill asks a question only when a missing choice would materially change the result. Otherwise it establishes the character bible, plans the complete asset list, and begins with a small reviewable batch.

<a id="validation"></a>
## Validation

Validate a complete album with tipping assets and required QA documents:

```bash
python3 scripts/validate_album.py /absolute/path/to/project/release \
  --expected-stickers 24 \
  --with-tipping \
  --require-qa-docs
```

Create a numbered contact sheet for manual review:

```bash
python3 scripts/make_contact_sheet.py \
  /absolute/path/to/project/release/stickers \
  /absolute/path/to/qa_overview.png
```

For machine-readable validation output, add `--json`. Dynamic albums can include GIF stickers with `--allow-gif-stickers` when the current platform specification permits them.

<a id="repository-map"></a>
## Repository map

| Path | Purpose |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Main workflow, review gates, delivery rules, and stop conditions |
| [`agents/openai.yaml`](agents/openai.yaml) | Skill display name, default prompt, product policy, and icon mapping |
| [`references/wechat-assets.md`](references/wechat-assets.md) | WeChat asset dimensions, formats, transparency, and size guidance |
| [`references/character-and-prompts.md`](references/character-and-prompts.md) | Character bible, prompting, Chinese typography, and repair strategy |
| [`references/qa-and-delivery.md`](references/qa-and-delivery.md) | Manual review checklist, exception handling, and delivery protocol |
| [`assets/`](assets) | Character bible, manifest, QA report templates, and skill icon |
| [`scripts/validate_album.py`](scripts/validate_album.py) | Deterministic album and image-file validation |
| [`scripts/make_contact_sheet.py`](scripts/make_contact_sheet.py) | Numbered visual overview generation |

## Privacy and responsible use

- Original pet photos are private references by default and must not be added to public release packages without explicit permission.
- High-resolution work files and rejected generations remain separate from the final release.
- Generated captions must be checked character by character; visual similarity is not sufficient.
- WeChat rules can change. When a current official document conflicts with this repository, the official document takes precedence.
- Do not claim that automated validation proves the absence of anatomy, identity, semantic, or typography defects.

<a id="license"></a>
## License

Repository-authored instructions, templates, and scripts are released under the [MIT License](LICENSE). Pet photos, generated sticker artwork, trademarks, platform specifications, fonts, and third-party materials may have separate rights and terms.
