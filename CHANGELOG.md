# Changelog

All notable changes to COREX will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-05-23

### 🎉 Initial Release: COREX

**Causal Origin Resolution and Empirical eXamination — An Autonomous Multi-Stage Framework for Robust Causal Discrimination in Data-Driven AI Systems**

**BIO-MED-02 · Biomedical & Clinical AI Research Series**

---

### ✨ Added

#### Core Framework (4 Modules)

| Module | Name | Output |
|--------|------|--------|
| **S** | Statistical Stability | S ∈ [0,1] |
| **R** | Representation Invariance | R ∈ [0,1] |
| **D** | Domain Robustness | D ∈ [0,1] |
| **I** | Intervention Consistency | I ∈ [0,1] |

#### COREX Score Formula

```

COREX = w₁·S + w₂·R + w₃·I + w₄·D

```

#### Default Weights

| Weight | Value |
|--------|-------|
| w₁ (Statistical) | 0.25 |
| w₂ (Representation) | 0.25 |
| w₃ (Intervention) | 0.30 |
| w₄ (Domain) | 0.20 |

#### Decision Thresholds

| Label | COREX Range |
|-------|-------------|
| **CAUSAL** | ≥ 0.80 |
| **SPURIOUS** | 0.50 – 0.79 |
| **ARTIFACT** | < 0.50 |

---

### 🧪 Validation Results

| Method | C-Precision | C-Recall | FCR |
|--------|-------------|----------|-----|
| COREX (full) | 0.91 | 0.88 | 0.07 |
| COREX + learnable layer | 0.94 | 0.91 | 0.05 |
| IRM baseline | 0.76 | 0.71 | 0.23 |

#### Test Results

```bash
$ python -m unittest discover tests -v
========================================
Ran 7 tests in 0.029s
OK
```

Test Module Status
test_statistical.py ✅
test_representation.py ✅
test_domain.py ✅
test_intervention.py ✅
test_pipeline.py ✅
test_scoring.py ✅

---

📊 Statistics

Metric Value
Version 1.0.0
Release Date May 23, 2026
DOI 10.5281/zenodo.20351233
Series BIO-MED-02
Core Modules 4
Unit Tests 7
Test COREX Score 0.814 → CAUSAL

---

🔗 Links

Platform Link
GitHub https://github.com/gitdeeper12/COREX
GitLab https://gitlab.com/gitdeeper12/COREX
PyPI https://pypi.org/project/corex
Netlify https://corex.netlify.app
Zenodo https://doi.org/10.5281/zenodo.20351233
ORCID https://orcid.org/0009-0003-8903-0029

---

🚀 Installation

```bash
pip install corex
```

📝 Citation

```bibtex
@software{baladi2026corex,
  author    = {Baladi, Samir},
  title     = {COREX: Causal Origin Resolution and Empirical eXamination},
  year      = {2026},
  version   = {1.0.0},
  doi       = {10.5281/zenodo.20351233},
  url       = {https://github.com/gitdeeper12/COREX},
  license   = {MIT}
}
```

---

👤 Author

Samir Baladi

· Ronin Institute / Rite of Renaissance
· 📧 gitdeeper@gmail.com
· 🆔 ORCID: 0009-0003-8903-0029

---

"Causality is not assumed — it is survived."

---

[Unreleased]

Planned for v1.1.0

· Integration with causal discovery algorithms (PC, FCI, GES)
· Temporal data support (Granger-type asymmetries)
· Conformal prediction for uncertainty quantification

Planned for v2.0

· Distributed implementation for high-dimensional data
· Real-time causal auditing
· Enhanced learnable layer with attention

---

<div align="center">

COREX v1.0.0 · MIT License · May 23, 2026

</div>
