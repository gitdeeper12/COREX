
<div align="center">

<img src="https://corex-causal.netlify.app/logo.png" alt="COREX Logo" width="120" height="120"/>

# COREX

### Causal Origin Resolution and Empirical eXamination

**An Autonomous Multi-Stage Framework for Robust Causal Discrimination in Data-Driven AI Systems**

---

[![PyPI version](https://img.shields.io/pypi/v/corex?color=1A3C6E&label=PyPI&logo=pypi&logoColor=white)](https://pypi.org/project/corex-causal-causal-causal-causal)
[![PyPI downloads](https://img.shields.io/pypi/dm/corex?color=2E75B6&label=Downloads&logo=pypi&logoColor=white)](https://pypi.org/project/corex-causal-causal-causal-causal/#files)
[![Python versions](https://img.shields.io/pypi/pyversions/corex?color=306998&logo=python&logoColor=white)](https://pypi.org/project/corex-causal-causal-causal-causal)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20351233.svg)](https://doi.org/10.5281/zenodo.20351233)
[![OSF Preregistration](https://img.shields.io/badge/OSF-Preregistered-blue?logo=osf&logoColor=white)](https://doi.org/10.17605/OSF.IO/3ABZF)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8903--0029-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0003-8903-0029)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Series](https://img.shields.io/badge/Series-BIO--MED--02-red)](https://osf.io/3ABZF)
[![Website](https://img.shields.io/badge/Website-Live-brightgreen?logo=netlify)](https://corex-causal.netlify.app)

</div>

---

## 📌 Overview

**COREX** is a deterministic, graph-free, model-agnostic computational framework that treats **causality as an empirically testable robustness property** rather than an assumed structural characteristic.

> *"Causality is not assumed, inferred, or interpreted — it is survived or rejected under systematic perturbation tests."*

Contemporary machine learning systems routinely exploit shortcut correlations embedded in training distributions — associations that collapse the moment data distribution shifts, feature encodings change, or interventions are applied. COREX provides a principled four-axis audit pipeline to classify any observed X → Y relationship as:

| Label | COREX Score | Meaning |
|---|---|---|
| 🟢 **CAUSAL** | ≥ 0.80 | Survives all four evaluation axes |
| 🟡 **SPURIOUS** | 0.50 – 0.79 | Breaks under domain shift or intervention |
| 🔴 **REPRESENTATION ARTIFACT** | < 0.50 | Exists only as a function of encoding choice |

---

## 🗂️ Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [COREX Pipeline](#-corex-pipeline)
- [Scoring Function](#-scoring-function)
- [Platforms & Mirrors](#-platforms--mirrors)
- [Clone & Download](#-clone--download)
- [Citation](#-citation)
- [License](#-license)
- [Author](#-author)

---

## ✨ Key Features

- **Four-module evaluation pipeline** — Statistical Stability, Representation Invariance, Domain Robustness, Intervention Consistency
- **No prior causal graph required** — purely empirical robustness testing
- **Model-agnostic** — works as a meta-evaluation layer atop any learned relationship
- **Calibrated causal scoring** — weighted fusion with interpretable decision thresholds
- **Optional learnable inference layer** — adaptive calibration for high-dimensional settings
- **Validated on biomedical signals** — vagus nerve electrophysiology, LPS/SIRS/CAR-T models
- **Full open-source distribution** — available across 11 platforms

---

## 📁 Project Structure

```
COREX/
│
├── corex/                          # Core Python package
│   ├── __init__.py                 # Package entry point & public API
│   ├── pipeline.py                 # Main COREX evaluation pipeline
│   ├── score.py                    # Causal scoring function & decision logic
│   │
│   ├── modules/                    # Evaluation modules
│   │   ├── __init__.py
│   │   ├── statistical.py          # Module 1: Statistical Stability (S)
│   │   ├── representation.py       # Module 2: Representation Invariance (R)
│   │   ├── domain.py               # Module 3: Domain Robustness (D)
│   │   └── intervention.py         # Module 4: Intervention Consistency (I)
│   │
│   ├── learnable/                  # Optional learnable inference layer
│   │   ├── __init__.py
│   │   ├── meta_scorer.py          # Adaptive MLP weight estimator
│   │   └── weights/                # Pre-trained weight checkpoints
│   │       └── default.pt
│   │
│   └── utils/                      # Shared utilities
│       ├── __init__.py
│       ├── transforms.py           # Feature transformation library (φ family)
│       ├── environments.py         # Environment construction & partitioning
│       ├── counterfactual.py       # Intervention simulation engine
│       └── metrics.py              # KL divergence, KS tests, CV, etc.
│
├── benchmarks/                     # Synthetic ground-truth benchmarks
│   ├── generators/
│   │   ├── causal_chain.py         # Class C: true causal chains X→Y→Z
│   │   ├── spurious_confound.py    # Class S: latent confounder H→X, H→Y
│   │   └── artifact_encoding.py    # Class A: encoding-dependent associations
│   ├── run_benchmarks.py           # Full benchmark evaluation script
│   └── results/                    # Pre-computed benchmark outputs
│       └── synthetic_1500.json
│
├── validation/                     # Real-world biomedical validation
│   ├── vagus_nerve/
│   │   ├── preprocess.py           # Electrophysiology signal preprocessing
│   │   ├── feature_extraction.py   # Wavelet, PCA, CNN embedding extraction
│   │   └── evaluate.py             # COREX evaluation on vagal–cytokine data
│   └── results/
│       └── biomedical_validation.json
│
├── examples/                       # Usage examples & tutorials
│   ├── quickstart.py               # Minimal working example
│   ├── synthetic_demo.ipynb        # Jupyter notebook: synthetic datasets
│   ├── biomedical_demo.ipynb       # Jupyter notebook: biomedical signals
│   └── custom_weights.py           # Custom weight configuration example
│
├── tests/                          # Unit and integration tests
│   ├── test_statistical.py
│   ├── test_representation.py
│   ├── test_domain.py
│   ├── test_intervention.py
│   ├── test_pipeline.py
│   └── test_scoring.py
│
├── docs/                           # Documentation source
│   ├── architecture.md             # Pipeline architecture reference
│   ├── modules.md                  # Per-module API documentation
│   ├── scoring.md                  # Scoring function & threshold calibration
│   └── api_reference.md            # Full Python API reference
│
├── paper/                          # Research paper artifacts
│   ├── COREX_Research_Paper.pdf    # Published paper (PDF)
│   ├── COREX_Research_Paper.docx   # Editable Word version
│   └── figures/                    # Paper figures & diagrams
│       └── pipeline_diagram.svg
│
├── .gitlab-ci.yml                  # GitLab CI/CD pipeline
├── .github/                        # GitHub Actions workflows
│   └── workflows/
│       ├── tests.yml
│       └── publish.yml
├── pyproject.toml                  # Build system configuration
├── setup.cfg                       # Package metadata
├── requirements.txt                # Runtime dependencies
├── requirements-dev.txt            # Development dependencies
├── CHANGELOG.md                    # Version history
├── CONTRIBUTING.md                 # Contribution guidelines
├── CODE_OF_CONDUCT.md
├── AUTHORS.md                      # Author and contributor registry
├── LICENSE                         # MIT License
└── README.md                       # This file
```

---

## 🚀 Quick Start

### Installation

```bash
# Install from PyPI
pip install corex-causal-causal-causal-causal

# Install from source
git clone https://github.com/gitdeeper12/COREX.git
cd COREX
pip install -e .
```

### Minimal Example

```python
from corex import CausalEvaluator

# Initialize the evaluator
evaluator = CausalEvaluator()

# Load your data
# X: feature array of shape (n_samples, n_features)
# Y: target array of shape (n_samples,)
result = evaluator.evaluate(X, Y)

print(result.label)          # "CAUSAL" | "SPURIOUS" | "REPRESENTATION_ARTIFACT"
print(result.corex_score)    # float in [0, 1]
print(result.breakdown)      # {"S": 0.91, "R": 0.88, "I": 0.85, "D": 0.90}
print(result.failure_modes)  # list of detected failure modes (if any)
```

### With Custom Weights

```python
from corex import CausalEvaluator

evaluator = CausalEvaluator(
    weights={
        "statistical": 0.25,
        "representation": 0.25,
        "intervention": 0.30,
        "domain": 0.20
    }
)
result = evaluator.evaluate(X, Y, environments=env_labels)
```

### With Learnable Inference Layer

```python
from corex import CausalEvaluator
from corex.learnable import MetaScorer

meta = MetaScorer.from_pretrained("default")
evaluator = CausalEvaluator(meta_scorer=meta)
result = evaluator.evaluate(X, Y)
```

---

## 🧩 COREX Pipeline

```
┌─────────────────────────────────────────────────────┐
│                    Raw Data  D                       │
└────────────────────┬────────────────────────────────┘
                     │
       ┌─────────────┼──────────────┐
       │             │              │
       ▼             ▼              ▼
  Statistical    Representation   Domain Shift
    Module          Module          Module
   (score S)      (score R)       (score D)
       │             │              │
       └─────────────┼──────────────┘
                     │
                     ▼
             Intervention Engine
                  (score I)
                     │
                     ▼
            Causal Scoring Layer
         COREX = w₁S + w₂R + w₃I + w₄D
                     │
                     ▼
           ┌─────────────────┐
           │  Final Decision  │
           │  🟢 CAUSAL       │
           │  🟡 SPURIOUS     │
           │  🔴 ARTIFACT     │
           └─────────────────┘
```

### Module Descriptions

| # | Module | Formula | Description |
|---|--------|---------|-------------|
| 1 | **Statistical Stability (S)** | `S = 1 - mean KL[P(Y\|X,D₁) ‖ P(Y\|X,D₂)]` | Cross-partition conditional invariance |
| 2 | **Representation Invariance (R)** | `R = 1 - (1/\|Φ\|) Σ ‖P(Y\|X) - P(Y\|φ(X))‖₁` | Stability under feature transformations |
| 3 | **Intervention Consistency (I)** | `I = Consistency(do(X=x₁)→Y₁, do(X=x₂)→Y₂)` | Causal effect direction & magnitude stability |
| 4 | **Domain Robustness (D)** | `D = 1 - CV(P(Y\|X, e)) over e ∈ E` | Cross-environment generalization |

---

## 📊 Scoring Function

```
COREX = w₁·S + w₂·R + w₃·I + w₄·D

Default weights:
  w₁ = 0.25  (Statistical Stability)
  w₂ = 0.25  (Representation Invariance)
  w₃ = 0.30  (Intervention Consistency)   ← highest weight: closest proxy to true causality
  w₄ = 0.20  (Domain Robustness)
```

**Decision thresholds:**

| Score Range | Classification | Condition |
|---|---|---|
| `COREX ≥ 0.80` | 🟢 CAUSAL | All modules stable; intervention confirmed |
| `0.50 ≤ COREX < 0.80` | 🟡 SPURIOUS CORRELATION | Domain shift or intervention failure detected |
| `COREX < 0.50` | 🔴 REPRESENTATION ARTIFACT | Representation invariance fails |

---

## 🌐 Platforms & Mirrors

| Platform | URL | Role |
|---|---|---|
| 🐙 **GitHub** (Primary) | [github.com/gitdeeper12/COREX](https://github.com/gitdeeper12/COREX) | Source code, issues, PRs |
| 🦊 **GitLab** (Mirror) | [gitlab.com/gitdeeper12/COREX](https://gitlab.com/gitdeeper12/COREX) | CI/CD mirror |
| 🪣 **Bitbucket** (Mirror) | [bitbucket.org/gitdeeper-12/COREX](https://bitbucket.org/gitdeeper-12/COREX) | Enterprise mirror |
| 🏔️ **Codeberg** (Mirror) | [codeberg.org/gitdeeper12/COREX](https://codeberg.org/gitdeeper12/COREX) | Open-source community |
| 📦 **PyPI** | [pypi.org/project/corex-causal-causal](https://pypi.org/project/corex-causal-causal-causal-causal) | Python package distribution |
| 🔬 **Zenodo** | [doi.org/10.5281/zenodo.20351233](https://doi.org/10.5281/zenodo.20351233) | Citable DOI, paper & data |
| 📋 **OSF Project** | [osf.io/3ABZF](https://osf.io/3ABZF) | Research project registry |
| 📝 **OSF Preregistration** | [doi.org/10.17605/OSF.IO/3ABZF](https://doi.org/10.17605/OSF.IO/3ABZF) | Pre-registered study protocol |
| 🌐 **Website** | [corex-causal.netlify.app](https://corex-causal.netlify.app) | Live documentation & dashboard |
| 🧑‍🔬 **ORCID** | [orcid.org/0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029) | Researcher identity |
| 🗄️ **Internet Archive** | [archive.org/details/osf-registrations-3ABZF](https://archive.org/details/osf-registrations-3ABZF) | Permanent archival copy |

### 🌐 Official Website Pages

| Page | URL |
|---|---|
| Homepage | [corex-causal.netlify.app](https://corex-causal.netlify.app) |
| Dashboard | [corex-causal.netlify.app/dashboard](https://corex-causal.netlify.app/dashboard) |
| Results | [corex-causal.netlify.app/results](https://corex-causal.netlify.app/results) |
| Documentation | [corex-causal.netlify.app/documentation](https://corex-causal.netlify.app/documentation) |

---

## 🔄 Clone & Download

### Git Clone

```bash
# GitHub (Primary)
git clone https://github.com/gitdeeper12/COREX.git

# GitLab (Mirror)
git clone https://gitlab.com/gitdeeper12/COREX.git

# Bitbucket (Mirror)
git clone https://bitbucket.org/gitdeeper-12/COREX.git

# Codeberg (Mirror)
git clone https://codeberg.org/gitdeeper12/COREX.git
```

### Direct ZIP Download

| Source | Link |
|---|---|
| GitHub | [COREX-main.zip](https://github.com/gitdeeper12/COREX/archive/refs/heads/main.zip) |
| GitLab | [COREX-main.zip](https://gitlab.com/gitdeeper12/COREX/-/archive/main/COREX-main.zip) |
| Bitbucket | [COREX-main.zip](https://bitbucket.org/gitdeeper-12/COREX/get/main.zip) |
| Codeberg | [COREX-main.zip](https://codeberg.org/gitdeeper12/COREX/archive/main.zip) |
| PyPI files | [pypi.org/project/corex-causal-causal/#files](https://pypi.org/project/corex-causal-causal-causal-causal/#files) |
| Zenodo record | [doi.org/10.5281/zenodo.20351233](https://doi.org/10.5281/zenodo.20351233) |

---

## 📖 Citation

If COREX contributes to your research, please cite using one of the following formats.

### 📦 PyPI Package

```bibtex
@software{baladi2026corex_pypi,
  author       = {Baladi, Samir},
  title        = {{COREX}: Causal Origin Resolution and Empirical eXamination},
  year         = {2026},
  version      = {1.0.0},
  publisher    = {Python Package Index},
  url          = {https://pypi.org/project/corex-causal-causal-causal-causal},
  note         = {Python package, MIT License}
}
```

### 🔬 Zenodo Archive (Paper & Data)

```bibtex
@dataset{baladi2026corex_zenodo,
  author       = {Baladi, Samir},
  title        = {{COREX}: Causal Origin Resolution and Empirical eXamination — Research Paper and Data},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.20351233},
  url          = {https://doi.org/10.5281/zenodo.20351233},
  series       = {BIO-MED-02}
}
```

### 📝 OSF Preregistration

```bibtex
@misc{baladi2026corex_osf,
  author       = {Baladi, Samir},
  title        = {{COREX} Framework: Pre-registered Study Protocol for Causal Discrimination in Data-Driven Models},
  year         = {2026},
  publisher    = {Open Science Framework},
  doi          = {10.17605/OSF.IO/3ABZF},
  url          = {https://doi.org/10.17605/OSF.IO/3ABZF},
  note         = {OSF Preregistration}
}
```

### 📄 Research Paper

```bibtex
@article{baladi2026corex,
  author       = {Baladi, Samir},
  title        = {{COREX}: An Autonomous Multi-Stage Framework for Robust Causal Discrimination in Data-Driven {AI} Systems},
  year         = {2026},
  month        = {May},
  series       = {BIO-MED-02},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.20351233},
  url          = {https://doi.org/10.5281/zenodo.20351233},
  note         = {Ronin Institute / Rite of Renaissance}
}
```

### APA (inline)

> Baladi, S. (2026). *COREX: An Autonomous Multi-Stage Framework for Robust Causal Discrimination in Data-Driven AI Systems* (Version 1.0.0, Series BIO-MED-02). Zenodo. https://doi.org/10.5281/zenodo.20351233

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Samir Baladi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 👤 Author

**Samir Baladi**
Interdisciplinary AI Researcher — Neural Engineering & Biomedical AI
Ronin Institute / Rite of Renaissance

| Contact | Link |
|---|---|
| 📧 Email | [gitdeeper@gmail.com](mailto:gitdeeper@gmail.com) |
| 🧑‍🔬 ORCID | [0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029) |
| 🐙 GitHub | [github.com/gitdeeper12](https://github.com/gitdeeper12) |
| 🌐 Website | [corex-causal.netlify.app](https://corex-causal.netlify.app) |

---

<div align="center">

**Series BIO-MED-02 · Version 1.0.0 · May 2026**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20351233.svg)](https://doi.org/10.5281/zenodo.20351233)
[![PyPI](https://img.shields.io/pypi/v/corex?color=1A3C6E)](https://pypi.org/project/corex-causal-causal-causal-causal)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*"Causality is not assumed — it is survived."*

</div>
=======
# COREX
Causal Origin Resolution and Empirical eXamination — An Autonomous Multi-Stage Framework for Robust Causal Discrimination in Data-Driven AI Systems
